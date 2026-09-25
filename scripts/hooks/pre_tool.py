#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PreToolUse hook. Blocks, before it happens:
  1. any outbound write (Confluence / Jira / Slack) that has no ledger passing G-01 for exactly this input;
  2. any write through the Backend Operations account (mcp__Atlassian_Rovo__*);
  3. n8n writes without a standing WRITE order;
  4. edits to the gate's own files (lexicon.json protected_paths) unless the owner's latest message says UNLOCK G-01,
     including git commands that stage, commit, restore or discard them without naming them (git commit -a, git add .).
Exit 0 = allow. Exit 2 = block (stderr is shown to Claude)."""
import json, os, re, shlex, subprocess, sys
from _common import N, read_input, transcript, deny, latest_owner_text, is_gated_tool, ledgers
import _guard
import gate_check

SAFE_BASH = re.compile(r'^\s*(python3\s+scripts/(gate_check|order_check|read_source|sync_check|selftest|g02_selftest)\.py\b|cat\s|head\s|tail\s|grep\s|rg\s|wc\s|ls\b|git\s+(diff|log|show|status)\b|sed\s+-n\s)')

# git subcommands that cannot move a working-tree or index change into history or throw it away
GIT_READONLY = {'status', 'diff', 'log', 'show', 'fetch', 'push', 'ls-files', 'ls-tree', 'rev-parse', 'blame',
                'grep', 'shortlog', 'describe', 'cat-file', 'branch', 'remote', 'help', 'version'}
GIT_GLOBAL_WITH_ARG = {'-C', '-c', '--git-dir', '--work-tree', '--namespace', '--exec-path', '--config-env'}
GIT_ALL_FLAGS = {'-a', '--all', '-A', '-u', '--update', '--include', '-i', '-p', '--patch', '--interactive'}


def protected_hit(text, L):
    return [p for p in L['protected_paths'] if p in text]


def is_protected(path, L):
    return any(path == p or (p.endswith('/') and path.startswith(p)) for p in L['protected_paths'])


def git_lines(*args):
    try:
        r = subprocess.run(['git'] + list(args), cwd=N.ROOT, capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.SubprocessError):
        return None
    return r.stdout.splitlines() if r.returncode == 0 else None


def dirty_protected(L):
    """Protected paths that differ from HEAD (staged, unstaged or untracked). None = git state unreadable."""
    staged = git_lines('diff', '--cached', '--name-only')
    unstaged = git_lines('diff', '--name-only')
    untracked = git_lines('ls-files', '--others', '--exclude-standard')
    if staged is None or unstaged is None or untracked is None:
        return None, None
    return (sorted({p for p in staged + unstaged + untracked if is_protected(p, L)}),
            sorted(p for p in staged if is_protected(p, L)))


SHELL_OPERATORS = {'&&', '||', ';', '|', '&', '(', ')', ';;', '|&'}
SHELL_RUNNERS = {'sh', 'bash', 'zsh', 'dash', 'ksh', 'eval', 'su', 'script'}
GIT_READONLY_SUB = {'stash': {'list', 'show'}, 'worktree': {'list'}, 'config': {'--get', '--list', '-l', '--get-all'}}


def shell_segments(cmd):
    """Split a shell command into simple commands, respecting quotes (a '(' inside a commit message is text).
    None = unbalanced quotes."""
    lex = shlex.shlex(cmd.replace('\n', ' ; '), posix=True, punctuation_chars=True)
    lex.whitespace_split = True
    try:
        toks = list(lex)
    except ValueError:
        return None
    segs, cur = [], []
    for t in toks:
        if t in SHELL_OPERATORS or (t and set(t) <= set('&|;()')):
            if cur:
                segs.append(cur)
            cur = []
        else:
            cur.append(t)
    if cur:
        segs.append(cur)
    return segs


def git_calls(cmd):
    """Each git invocation in a shell command as (subcommand, args). None = the command could not be parsed."""
    out = []
    segs = shell_segments(cmd)
    if segs is None:
        return None
    for raw in segs:
        toks = [t.strip('`') for t in raw]    # `git stash` in backticks
        # quoted text is only a command when a shell runs it (sh -c "...", eval '...') or it holds $( ) / backticks;
        # otherwise "git exit=$?" or a commit message mentioning git is just text
        runs_text = any(os.path.basename(t) in SHELL_RUNNERS for t in toks)
        for r, t in zip(raw, toks):
            if re.search(r'\s', t) and re.search(r'\bgit\b', t) and (runs_text or '$(' in r or '`' in r):
                inner = git_calls(t)
                if inner is None:
                    return None
                out.extend(inner)
        i = next((k for k, t in enumerate(toks) if t == 'git' or t.endswith('/git')), None)
        if i is None:
            continue
        rest = toks[i + 1:]
        while rest and rest[0].startswith('-'):
            opt = rest.pop(0)
            if opt in GIT_GLOBAL_WITH_ARG and rest:
                rest.pop(0)
        out.append((rest[0] if rest else '', rest[1:]))
    return out


def covers(spec, path):
    s = spec[2:] if spec.startswith(':/') else spec
    s = s.rstrip('/')
    if s in ('', '.', '*', ':'):
        return True
    if any(c in s for c in '*?['):
        import fnmatch
        return fnmatch.fnmatch(path, s) or fnmatch.fnmatch(path, s + '/*')
    return path == s or path.startswith(s + '/')


def git_touches_protected(cmd, L):
    """Why this command would stage / commit / restore / discard a protected path, or '' when it cannot."""
    if not re.search(r'\bgit\b', cmd):
        return ''
    calls = git_calls(cmd)
    if calls is not None:
        calls = [(s, a) for s, a in calls
                 if s not in GIT_READONLY and not (a and a[0] in GIT_READONLY_SUB.get(s, ()))]
        if not calls:
            return ''
    dirty, staged = dirty_protected(L)
    if dirty is None:
        return 'git state could not be read'
    if not dirty:                       # no gate file differs from HEAD: no git command can carry or drop one
        return ''
    if calls is None:
        return 'the command could not be parsed while gate files have uncommitted changes %s' % dirty
    for sub, args in calls:
        opts = [a for a in args if a.startswith('-')]
        specs = [a for a in args if not a.startswith('-') and a != '--']
        if sub == 'commit':
            specs = [a for k, a in enumerate(args) if not a.startswith('-') and a != '--'
                     and not (k and args[k - 1] in ('-m', '-F', '--message', '--file', '-C', '-c', '--author', '--date', '--fixup', '--squash'))]
            if any(o in GIT_ALL_FLAGS or re.match(r'^-[a-zA-Z]*a', o) for o in opts):
                return 'git commit -a / --all would commit %s' % dirty
            if staged:
                return 'git commit would commit the staged gate files %s' % staged
            if any(covers(s, p) for s in specs for p in dirty):
                return 'git commit pathspec covers %s' % dirty
            continue
        if sub == 'add':
            if any(o in GIT_ALL_FLAGS for o in opts) or not specs:
                return 'git add %s would stage %s' % (' '.join(opts), dirty)
            if any(covers(s, p) for s in specs for p in dirty):
                return 'git add pathspec covers %s' % dirty
            continue
        if sub in ('checkout', 'restore', 'rm', 'mv') and specs:
            if any(covers(s, p) for s in specs for p in dirty):
                return 'git %s pathspec covers %s' % (sub, dirty)
            continue
        return 'git %s runs while gate files have uncommitted changes %s' % (sub or '(alias?)', dirty)
    return ''


def main():
    inp = read_input()
    name = inp.get('tool_name', '')
    ti = inp.get('tool_input') or {}
    L = N.lexicon()

    # ---- 4. gate files are not mine to change
    # 4a. anything that changed them since the last hook (a program that did not name them) is put back first
    put_back = _guard.enforce(L, lambda tok: tok in latest_owner_text(transcript(inp)))
    if put_back:
        deny(_guard.message(put_back, L))
    L = N.lexicon()                  # re-read: the lexicon itself may have just been put back
    if name in ('Write', 'Edit', 'NotebookEdit', 'MultiEdit'):
        path = N.rel(ti.get('file_path') or ti.get('notebook_path') or '')
        hits = [p for p in L['protected_paths'] if path == p or (p.endswith('/') and path.startswith(p))]
        if _guard.STATE_MARKER in path:
            hits.append(_guard.STATE_MARKER)
        if hits:
            tr = transcript(inp)
            if L['order_words']['unlock_token'] not in latest_owner_text(tr):
                deny('G-01: %s is a gate file. Changing it needs "%s" in the owner\'s latest message. Ask the owner.'
                     % (path, L['order_words']['unlock_token']))
        return 0
    if name == 'Bash':
        cmd = ti.get('command', '')
        if 'G01_HOOK_PROBE' in cmd:
            deny('G-01 hook is active (probe).')
        hits = protected_hit(cmd, L) + ([_guard.STATE_MARKER] if _guard.STATE_MARKER in cmd else [])
        if hits and not (SAFE_BASH.match(cmd) and not re.search(r'>|\btee\b|-i\b|\brm\b|\bmv\b|\bcp\b|open\(|write', cmd)):
            tr = transcript(inp)
            if L['order_words']['unlock_token'] not in latest_owner_text(tr):
                deny('G-01: this command touches gate files %s. Needs "%s" in the owner\'s latest message.'
                     % (hits, L['order_words']['unlock_token']))
        why = git_touches_protected(cmd, L)
        if why:
            tr = transcript(inp)
            if L['order_words']['unlock_token'] not in latest_owner_text(tr):
                deny('G-01: %s. Gate files are committed, restored or discarded only with "%s" in the owner\'s latest message. '
                     'Stage your own files by exact path instead.' % (why, L['order_words']['unlock_token']))
        return 0

    if not is_gated_tool(name, L):
        return 0
    if name == 'mcp__Atlassian_MCP__updateConfluenceContent' and ti.get('dryRun') is True:
        return 0

    tr = transcript(inp)
    override = L['order_words']['override_token'] in latest_owner_text(tr)

    # ---- 2. Backend Operations account
    if name.startswith(L['tools']['backend_ops_account_prefix']) and not override:
        deny('G-01 B4: %s writes as the Backend Operations account. Forbidden by the owner (2026-09-22). '
             'Use the mcp__Atlassian_MCP__ tool (owner\'s account).' % name)

    # ---- 3. n8n: a standing order (G-01 B1), then the build discipline (G-02, .claude/gates/G-02-n8n-build.json)
    if name.startswith('mcp__n8n__'):
        order, why = gate_check.find_order(tr, 'outbound', L)
        if not order and not override:
            deny('G-01 B1: n8n write %s without a standing WRITE order. %s' % (name, why))
        import g02
        probs = g02.check_pre(name, ti, tr, L)
        if probs and g02.cfg()['override_token'] not in latest_owner_text(tr):
            deny('G-02 blocked %s (rules: .claude/gates/G-02-n8n-build.json):\n- %s' % (name, '\n- '.join(probs)))
        return 0

    # ---- 1. content writes: a ledger for exactly this input must pass now
    canon = json.dumps(ti, sort_keys=True, ensure_ascii=False)
    match = None
    for p, lg in ledgers():
        pf = lg.get('payload_file')
        if lg.get('kind') != 'outbound' or not pf:
            continue
        try:
            with open(os.path.join(N.ROOT, pf), encoding='utf-8') as f:
                if json.dumps(json.load(f), sort_keys=True, ensure_ascii=False) == canon:
                    match = (p, lg)
        except (OSError, ValueError):
            continue
    if not match:
        if override:
            return 0
        deny('G-01: no ledger in docs/ledger/ has a payload_file identical to this %s input. '
             'Build the ledger (skill outbound-write-gate), run scripts/gate_check.py, then call the tool with exactly the payload_file content.' % name)
    R, _ = gate_check.evaluate(match[1], tr, tool_name=name, tool_input=ti, L=L)
    if not R.ok and not override:
        deny('G-01 blocked %s using %s\n%s' % (name, N.rel(match[0]), gate_check.render(R, match[1])))
    return 0


if __name__ == '__main__':
    sys.exit(main())
