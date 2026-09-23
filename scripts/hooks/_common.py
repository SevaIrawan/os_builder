# -*- coding: utf-8 -*-
"""Shared helpers for the hooks. Hooks read one JSON object on stdin (Claude Code hook input)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import nosm_lib as N          # noqa: E402

LOG = os.path.join(N.ROOT, 'docs', 'orders', 'consumed.jsonl')
REGISTRY = os.path.join(N.ROOT, 'docs', 'ledger', '_draft-registry.json')


def read_input():
    try:
        return json.load(sys.stdin)
    except ValueError:
        return {}


def transcript(inp):
    return N.Transcript(N.find_transcript(inp.get('transcript_path')))


def deny(msg):
    """Exit code 2: the tool call / the stop is blocked and msg is shown to Claude."""
    sys.stderr.write(msg.rstrip() + '\n')
    sys.exit(2)


def append_log(rec):
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    rec['at'] = N.now_utc().isoformat()
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')


def read_log():
    out = []
    if os.path.exists(LOG):
        with open(LOG, encoding='utf-8') as f:
            for line in f:
                try:
                    out.append(json.loads(line))
                except ValueError:
                    pass
    return out


def latest_owner_text(tr):
    return tr.prompts[-1]['text'] if tr.prompts else ''


def is_readonly_tool(name, L):
    return any(name.startswith(p) for p in L['tools']['readonly_prefixes'])


def is_gated_tool(name, L):
    return any(name.startswith(p) for p in L['tools']['gated_prefixes']) and not is_readonly_tool(name, L)


def ledgers():
    d = os.path.join(N.ROOT, 'docs', 'ledger')
    out = []
    for fn in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        if fn.endswith('.json') and not fn.startswith('_') and not fn.endswith('.payload.json'):
            p = os.path.join(d, fn)
            try:
                with open(p, encoding='utf-8') as f:
                    out.append((p, json.load(f)))
            except ValueError:
                pass
    return out
