# -*- coding: utf-8 -*-
"""G-04: git and GitHub write gate. Rules live in .claude/gates/G-04-repo-write.json only.

check(tool_name, tool_input, owner_text, L) -> '' when allowed, else the reason it is blocked.
owner_text is the owner's latest real message (from the transcript)."""
import json, os, re
from _common import N

G04_PATH = os.path.join(N.ROOT, '.claude', 'gates', 'G-04-repo-write.json')


def cfg():
    with open(G04_PATH, encoding='utf-8') as f:
        return json.load(f)


def has_word(text, words):
    low = (text or '').lower()
    return any(re.search(r'(?<![a-z])' + re.escape(w.lower()) + r'(?![a-z])', low) for w in words)


def git_need(sub, args, C):
    """'delete', 'commit_push' or '' for one git invocation."""
    g = C['git']
    opts = [a for a in args if a.startswith('-')]
    plain = [a for a in args if not a.startswith('-')]
    if sub == 'reflog':
        return '' if not plain or plain[0] in g['reflog_read_only'] else 'delete'
    if sub in g['delete_always']:
        return 'delete'
    when = g['delete_when']
    if sub == 'branch' and any(o in when['branch'] or re.match(r'^-[a-zA-Z]*[dDmMcCf]', o) for o in opts):
        return 'delete'
    if sub == 'push':
        if any(o.split('=')[0] in when['push'] or re.match(r'^-[a-zA-Z]*[df]', o) for o in opts) \
                or any(a.startswith(':') or a.startswith('+') for a in plain):
            return 'delete'
        return 'commit_push'
    if sub == 'tag' and any(o in when['tag'] for o in opts):
        return 'delete'
    if sub == 'reset' and (any(o in when['reset'] for o in opts) or [a for a in plain if a != 'HEAD']):
        return 'delete'
    if sub == 'checkout' and (any(o in when['checkout'] for o in opts + args) or '.' in plain):
        return 'delete'
    if sub == 'switch' and any(o in when['switch'] for o in opts):
        return 'delete'
    if sub == 'restore' and set(opts) - {'--staged', '-S'}:
        return 'delete'
    if sub == 'restore' and not opts:
        return 'delete'
    if sub in ('stash', 'worktree', 'remote') and plain and plain[0] in when[sub]:
        return 'delete'
    if sub in g['commit_push']:
        return 'commit_push'
    return ''


def check_bash(cmd, owner_text, L, git_calls):
    C = cfg()
    if not re.search(r'\bgit\b', cmd):
        return ''
    calls = git_calls(cmd)
    if calls is None:
        return 'G-04: the git command could not be parsed; write it plainly so the gate can read it'
    needs = {git_need(s, a, C) for s, a in calls} - {''}
    return verdict(needs, owner_text, L, C, 'git ' + ', git '.join(s for s, _ in calls))


def check_github(tool, owner_text, L):
    C = cfg()
    gt = C['github_tools']
    if any(tool.startswith(p) for p in gt['read_prefixes']):
        return ''
    need = 'delete' if tool in gt['delete'] else 'commit_push' if tool in gt['commit_push'] else 'write'
    return verdict({need}, owner_text, L, C, tool)


def verdict(needs, owner_text, L, C, what):
    if not needs:
        return ''
    cls, _ = N.classify(owner_text, L)
    if cls == 'STOP':
        return 'G-04: %s blocked - the owner\'s latest message is a stop / negation ("%s")' % (what, owner_text[:60])
    missing = []
    for n in sorted(needs):
        if n == 'write':
            if cls != 'WRITE':
                missing.append('a G-01 WRITE order')
        elif not has_word(owner_text, C['words'][n]):
            missing.append(' / '.join('"%s"' % w for w in C['words'][n]))
    if missing:
        return ('G-04: %s needs %s in the owner\'s latest message (rules: .claude/gates/G-04-repo-write.json). '
                'Ask the owner.' % (what, ' and '.join(missing)))
    return ''
