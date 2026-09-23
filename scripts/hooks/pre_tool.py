#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PreToolUse hook. Blocks, before it happens:
  1. any outbound write (Confluence / Jira / Slack) that has no ledger passing G-01 for exactly this input;
  2. any write through the Backend Operations account (mcp__Atlassian_Rovo__*);
  3. n8n writes without a standing WRITE order;
  4. edits to the gate's own files (lexicon.json protected_paths) unless the owner's latest message says UNLOCK G-01.
Exit 0 = allow. Exit 2 = block (stderr is shown to Claude)."""
import json, os, re, sys
from _common import N, read_input, transcript, deny, latest_owner_text, is_gated_tool, ledgers
import gate_check

SAFE_BASH = re.compile(r'^\s*(python3\s+scripts/(gate_check|order_check|read_source|sync_check|selftest)\.py\b|cat\s|head\s|tail\s|grep\s|rg\s|wc\s|ls\b|git\s+(diff|log|show|status)\b|sed\s+-n\s)')


def protected_hit(text, L):
    return [p for p in L['protected_paths'] if p in text]


def main():
    inp = read_input()
    name = inp.get('tool_name', '')
    ti = inp.get('tool_input') or {}
    L = N.lexicon()

    # ---- 4. gate files are not mine to change
    if name in ('Write', 'Edit', 'NotebookEdit', 'MultiEdit'):
        path = N.rel(ti.get('file_path') or ti.get('notebook_path') or '')
        hits = [p for p in L['protected_paths'] if path == p or (p.endswith('/') and path.startswith(p))]
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
        hits = protected_hit(cmd, L)
        if hits and not (SAFE_BASH.match(cmd) and not re.search(r'>|\btee\b|-i\b|\brm\b|\bmv\b|\bcp\b|open\(|write', cmd)):
            tr = transcript(inp)
            if L['order_words']['unlock_token'] not in latest_owner_text(tr):
                deny('G-01: this command touches gate files %s. Needs "%s" in the owner\'s latest message.'
                     % (hits, L['order_words']['unlock_token']))
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

    # ---- 3. n8n: order only
    if name.startswith('mcp__n8n__'):
        order, why = gate_check.find_order(tr, 'outbound', L)
        if not order and not override:
            deny('G-01 B1: n8n write %s without a standing WRITE order. %s' % (name, why))
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
