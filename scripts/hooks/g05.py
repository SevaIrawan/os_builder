# -*- coding: utf-8 -*-
"""G-05: write gate for every outward tool no other gate covers. Rules: .claude/gates/G-05-other-tools.json only.

check(tool_name, tool_input, tr, L)  -> '' when allowed, else the reason it is blocked (MCP and built-in tools).
check_bash(cmd, tr, L, shell_segments) -> the same for a Bash command that writes over the network.
An allowed write uses up the owner's write order (one order = one write, as G-01 B2)."""
import json, os, re
from _common import N, append_log
import gate_check

G05_PATH = os.path.join(N.ROOT, '.claude', 'gates', 'G-05-other-tools.json')
COVERED = ('mcp__Atlassian_MCP__', 'mcp__Atlassian_Rovo__', 'mcp__Slack__', 'mcp__n8n__', 'mcp__github__')


def cfg():
    with open(G05_PATH, encoding='utf-8') as f:
        return json.load(f)


def binds(tool):
    return (tool.startswith('mcp__') and not tool.startswith(COVERED)) or tool in cfg()['builtin_tools']


def is_read(tool, ti, C):
    bt = C['builtin_tools'].get(tool)
    if bt:
        return (ti.get('action') or bt.get('default_action', '')) in bt['read_actions']
    if tool in C['read_tools']:
        return True
    op = tool.split('__', 2)[2] if tool.count('__') >= 2 else tool
    return any(op == v or op.startswith(v + '_') or re.match(re.escape(v) + r'[A-Z]', op) for v in C['read_verbs'])


def use_order(tr, L, what):
    """'' and the order is marked used, or the reason there is no usable write order."""
    order, why = gate_check.find_order(tr, 'outbound', L)
    if not order:
        return 'no standing write order (%s)' % why
    if order['uuid'] in gate_check.consumed_orders():
        return 'the write order "%s" was already used for another write (one order = one write)' % order['text'][:60]
    append_log({'event': 'consumed', 'gate': 'G-05', 'order_uuid': order['uuid'], 'order_text': order['text'][:200],
                'tool': what, 'target': 'g05:%s' % what, 'payload_sha': N.text_sha(what + order['uuid']),
                'read_back': True})
    return ''


def deny_text(what, why):
    return ('G-05: %s writes outside the repo and needs its own write order from the owner: %s '
            '(rules: .claude/gates/G-05-other-tools.json, docs/working-agreement.md rule 4). Ask the owner.' % (what, why))


def check(tool, ti, tr, L):
    if not binds(tool):
        return ''
    C = cfg()
    if is_read(tool, ti, C):
        return ''
    why = use_order(tr, L, tool)
    return deny_text(tool, why) if why else ''


def network_write(cmd, shell_segments, C):
    """The first simple command that sends data or a write method over the network, or ''."""
    nw = C['bash_network_write']
    for seg in shell_segments(cmd) or []:
        words = [w for w in seg if not re.match(r'^[A-Za-z_]\w*=', w)] or ['']
        head = os.path.basename(words[0])
        rest = words[1:]
        low = [w.lower() for w in rest]
        if head == 'curl':
            meth = [low[i + 1] for i, w in enumerate(low[:-1]) if w in ('-x', '--request')] + \
                   [w.split('=', 1)[1] for w in low if w.startswith('--request=')] + \
                   [w[2:] for w in low if w.startswith('-x') and len(w) > 2]
            if any(m.upper() in nw['methods'] for m in meth) or \
                    any(w == f or w.startswith(f + '=') for w in rest for f in nw['curl_data_flags']):
                return ' '.join(seg)[:80]
        if head == 'wget' and any(w.split('=', 1)[0] in nw['wget_write_flags'] for w in rest):
            return ' '.join(seg)[:80]
        if head in ('http', 'https') and rest and rest[0].upper() in nw['methods']:
            return ' '.join(seg)[:80]
    return ''


def check_bash(cmd, tr_fn, L, shell_segments):
    """tr_fn: a function returning the transcript (read only when the command really writes)."""
    C = cfg()
    hit = network_write(cmd, shell_segments, C)
    if not hit:
        return ''
    why = use_order(tr_fn(), L, 'Bash: ' + hit)
    return deny_text('this command (%s)' % hit, why) if why else ''
