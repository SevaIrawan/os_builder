#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PostToolUse hook. After a successful outbound write, marks the standing order as used
(one order = one write) and records the write so the Stop hook can demand a read-back."""
import json, os, sys
from _common import N, read_input, transcript, append_log, is_gated_tool, ledgers
import gate_check


def main():
    inp = read_input()
    name = inp.get('tool_name', '')
    ti = inp.get('tool_input') or {}
    L = N.lexicon()
    if not is_gated_tool(name, L) or name.startswith('mcp__n8n__'):
        return 0
    if name == 'mcp__Atlassian_MCP__updateConfluenceContent' and ti.get('dryRun') is True:
        return 0
    resp = json.dumps(inp.get('tool_response'), ensure_ascii=False)[:2000]
    failed = '"error": true' in resp or '"isError": true' in resp or resp.startswith('"Error') or 'denied' in resp[:300]
    tr = transcript(inp)
    order, _ = gate_check.find_order(tr, 'outbound', L)
    canon = json.dumps(ti, sort_keys=True, ensure_ascii=False)
    wid = None
    for p, lg in ledgers():
        pf = lg.get('payload_file')
        if lg.get('kind') == 'outbound' and pf and os.path.exists(os.path.join(N.ROOT, pf)):
            with open(os.path.join(N.ROOT, pf), encoding='utf-8') as f:
                if json.dumps(json.load(f), sort_keys=True, ensure_ascii=False) == canon:
                    wid = lg.get('write_id')
    sys_, tid = gate_check.target_of(name, ti)
    wdir = os.path.join(N.ROOT, 'docs', 'ledger', '_writes')
    os.makedirs(wdir, exist_ok=True)
    with open(os.path.join(wdir, N.text_sha(canon) + '.json'), 'w', encoding='utf-8') as f:
        json.dump({'tool': name, 'input': ti}, f, ensure_ascii=False, indent=1)
    append_log({'event': 'consumed' if not failed else 'write_failed', 'order_uuid': order and order['uuid'],
                'order_text': order and order['text'][:200], 'write_id': wid, 'tool': name,
                'target': '%s:%s' % (sys_, tid), 'payload_sha': N.text_sha(canon), 'read_back': False})
    return 0


if __name__ == '__main__':
    sys.exit(main())
