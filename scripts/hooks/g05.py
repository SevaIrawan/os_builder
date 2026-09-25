# -*- coding: utf-8 -*-
"""G-05: write gate for every outward tool no other gate covers. Rules: .claude/gates/G-05-other-tools.json only.

check(tool_name, tool_input, owner_text, L) -> '' when allowed, else the reason it is blocked."""
import json, os, re
from _common import N

G05_PATH = os.path.join(N.ROOT, '.claude', 'gates', 'G-05-other-tools.json')
COVERED = ('mcp__Atlassian_MCP__', 'mcp__Atlassian_Rovo__', 'mcp__Slack__', 'mcp__n8n__', 'mcp__github__')


def cfg():
    with open(G05_PATH, encoding='utf-8') as f:
        return json.load(f)


def binds(tool):
    return (tool.startswith('mcp__') and not tool.startswith(COVERED)) or tool == cfg()['artifact']['tool']


def is_read(tool, ti, C):
    if tool == C['artifact']['tool']:
        return (ti.get('action') or 'publish') in C['artifact']['read_actions']
    if tool in C['read_tools']:
        return True
    op = tool.split('__', 2)[2] if tool.count('__') >= 2 else tool
    return any(op == v or op.startswith(v + '_') or re.match(re.escape(v) + r'[A-Z]', op) for v in C['read_verbs'])


def check(tool, ti, owner_text, L):
    if not binds(tool):
        return ''
    C = cfg()
    if is_read(tool, ti, C):
        return ''
    cls, _ = N.classify(owner_text, L)
    if cls == 'WRITE':
        return ''
    return ('G-05: %s writes outside the repo and needs a write order in the owner\'s latest message (class now %s; '
            'rules: .claude/gates/G-05-other-tools.json, docs/working-agreement.md rule 4). Ask the owner.' % (tool, cls))
