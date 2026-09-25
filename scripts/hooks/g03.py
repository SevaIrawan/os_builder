# -*- coding: utf-8 -*-
"""G-03: evidence gate for chat answers. Rules live in .claude/gates/G-03-chat-claims.json only.

check_turn(transcript_path, last_message=None) -> list of problems (empty = the turn may end).

Evidence is taken from the session transcript: real tool results and the owner's own messages.
Claude's text and hook messages are never evidence. Claude's tool inputs count only for `code`
tokens (a path or command a successful call was given)."""
import json, os, re
from _common import N

G03_PATH = os.path.join(N.ROOT, '.claude', 'gates', 'G-03-chat-claims.json')

FENCE_RE = re.compile(r'```.*?(```|$)', re.S)
SENT_SPLIT_RE = re.compile(r'\n+|(?<=[.!?。；;])\s+')
TOKEN_RES = [
    ('tool_use_id', re.compile(r'\btoolu_[A-Za-z0-9]{8,}\b')),
    ('issue_key', re.compile(N.ISSUE_KEY_RE)),
    ('date', re.compile(r'\b\d{4}-\d{2}-\d{2}\b')),
    ('page_id', re.compile(r'(?<![\w.])\d{9,11}(?![\w])')),
    ('comment_id', re.compile(r'(?<![\w])c\d{5,6}(?![\w])')),
    ('version', re.compile(r'(?<![\w])v\d+(?:\.\d+)*(?![\w])')),
    ('workflow_id', re.compile(r'(?<![\w])(?=[A-Za-z0-9]*\d)(?=[A-Za-z0-9]*[a-z])(?=[A-Za-z0-9]*[A-Z])[A-Za-z0-9]{16}(?![\w])')),
    ('commit', re.compile(r'(?<![\w])(?=[0-9a-f]*\d)(?=[0-9a-f]*[a-f])[0-9a-f]{7,40}(?![\w])')),
]
CODE_RE = re.compile(r'`([^`\s]{2,120})`')
NUMBER_RE = re.compile(r'(?<![\w.])\d+(?:[.,]\d+)?(?![\w])')
QUOTE_RE = re.compile(r'"([^"\n]{4,300})"|“([^”\n]{4,300})”|「([^」\n]{2,120})」')
LINE_REF_RE = re.compile(r'^(?P<path>[\w./-]+\.[A-Za-z0-9]+):(?P<a>\d+)(?:-(?P<b>\d+))?$')


def cfg():
    with open(G03_PATH, encoding='utf-8') as f:
        return json.load(f)


# ---------------------------------------------------------------- transcript

def load_turn(path):
    """(owner_texts, tool_results, turn_texts, all_claude_texts)
    tool_results: [(tool_name, tool_input, result_text)] for every successful tool call of the session.
    turn_texts: Claude's text blocks since the owner's latest message, oldest first."""
    rows = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            try:
                rows.append(json.loads(line))
            except ValueError:
                continue
    uses, results, owner, turn, mine = {}, [], [], [], []
    for d in rows:
        if d.get('isSidechain'):
            continue
        t, msg = d.get('type'), d.get('message') or {}
        if t == 'assistant':
            for b in msg.get('content') or []:
                if isinstance(b, dict) and b.get('type') == 'tool_use':
                    uses[b['id']] = b
                elif isinstance(b, dict) and b.get('type') == 'text' and b.get('text', '').strip():
                    turn.append(b['text'])
                    mine.append(b['text'])
        elif t == 'user':
            c = msg.get('content')
            if (d.get('origin') or {}).get('kind') == 'human' and not d.get('isMeta') and not d.get('isCompactSummary'):
                text = c if isinstance(c, str) else '\n'.join(
                    b.get('text', '') for b in c or [] if isinstance(b, dict) and b.get('type') == 'text')
                text = N.SYSREM_RE.sub('', text).strip()
                if text:
                    owner.append(text)
                    turn = []                       # a new owner message starts a new turn
            if isinstance(c, list):
                for b in c:
                    if not (isinstance(b, dict) and b.get('type') == 'tool_result') or b.get('is_error'):
                        continue
                    u = uses.get(b.get('tool_use_id'))
                    if not u:
                        continue
                    cont = b.get('content')
                    if isinstance(cont, list):
                        txt = ''.join(x.get('text', '') for x in cont if isinstance(x, dict))
                    else:
                        txt = cont if isinstance(cont, str) else json.dumps(cont, ensure_ascii=False)
                    m = N.PERSIST_RE.search(txt[:600])
                    if m and os.path.exists(m.group(1)):
                        with open(m.group(1), encoding='utf-8', errors='replace') as pf:
                            txt = pf.read()
                    if 'was denied' in txt[:400] or txt.startswith('MCP error'):
                        continue
                    results.append((u['name'], u.get('input') or {}, txt))
    return owner, results, turn, mine


# ---------------------------------------------------------------- tokens

def tokens(sentence):
    """[(kind, token)] for one sentence. Quotes and `code` are taken whole; then ids; then plain numbers."""
    out, taken = [], []

    def free(a, b):
        return all(b <= x or a >= y for x, y in taken)
    for m in QUOTE_RE.finditer(sentence):
        q = next(g for g in m.groups() if g is not None)
        if len(N.norm(q)) >= 4:
            out.append(('quote', q)); taken.append((m.start(), m.end()))
    for m in CODE_RE.finditer(sentence):
        if free(m.start(), m.end()):
            out.append(('code', m.group(1))); taken.append((m.start(), m.end()))
    for kind, rx in TOKEN_RES:
        for m in rx.finditer(sentence):
            if free(m.start(), m.end()):
                out.append((kind, m.group(0))); taken.append((m.start(), m.end()))
    for m in NUMBER_RE.finditer(sentence):
        if free(m.start(), m.end()):
            out.append(('number', m.group(0)))
    return out


class Evidence:
    """What a token may be found in. results: [(tool_name, tool_input, text)]."""
    def __init__(self, owner, results):
        self.results = results
        self.texts = owner + [r[2] for r in results]
        self.norm = [N.norm(t) for t in self.texts]
        # what a real, successful call was: its tool name and the paths / commands it was given (`code` only)
        self.used = [r[0] for r in results] + [str(v) for r in results for k, v in r[1].items()
                                               if k in ('file_path', 'path', 'pattern', 'command')]

    def subset(self, pred):
        return Evidence([], [r for r in self.results if pred(r)])


def found(kind, tok, ev):
    if kind == 'number':
        rx = re.compile(r'(?<![\d])' + re.escape(tok) + r'(?![\d])')
        return any(rx.search(t) for t in ev.texts)
    if kind == 'version':
        n = re.escape(tok[1:])
        rx = re.compile(r'(?<![\w])v:?' + n + r'(?![\d.])|"number"\s*:\s*' + n + r'(?![\d])')
        return any(rx.search(t) for t in ev.texts)
    if kind == 'quote':
        q = N.norm(tok)
        return any(q in t for t in ev.norm)
    if kind == 'code':
        m = LINE_REF_RE.match(tok)
        if m:                           # file.py:120 or file.py:12-19 -> that file was Read and showed those lines
            base = os.path.basename(m.group('path'))
            reads = [r[2] for r in ev.results if r[0] == 'Read' and str(r[1].get('file_path', '')).endswith('/' + base)]
            lines = [m.group('a')] + ([m.group('b')] if m.group('b') else [])
            return bool(reads) and all(any(re.search(r'(?m)^\s*' + x + r'\t', t) for t in reads) for x in lines)
        kv = re.match(r'^([A-Za-z_][\w.]*)=(\S+)$', tok)
        if kv:                          # detail=summary -> a call was given it, or a result shows "detail":"summary"
            k, v = kv.group(1), kv.group(2).strip('"\'')
            if any(str(r[1].get(k)) == v for r in ev.results) or \
                    any(re.search(r'"%s"\s*:\s*"?%s"?' % (re.escape(k), re.escape(v)), t) for t in ev.texts):
                return True
        return any(tok in t for t in ev.texts) or any(tok in u for u in ev.used)
    return any(tok in t for t in ev.texts)


def sentences(text, marker):
    body = FENCE_RE.sub(' ', text)
    for raw in SENT_SPLIT_RE.split(body):
        s = raw.strip()
        if s and re.search(r'[\w㐀-鿿]', s):
            yield s, (marker in s)


def absence_hit(s, C):
    low = s.lower()
    for p in C['absence_phrases']:
        if re.search(r'(?<![a-z])' + re.escape(p.lower()) + r'(?![a-z])', low):
            return p
    return None


def problems_in(text, C, ev, earlier_mine=()):
    """Problems for one text block: [(check, sentence, detail, key)].
    earlier_mine: Claude's own earlier texts. Quoting them is allowed (T1) but proves nothing (T3)."""
    marker = C['unverified_marker']
    mine_norm = [N.norm(t) for t in earlier_mine]
    out = []
    for s, marked in sentences(text, marker):
        if marked:
            continue
        toks = tokens(s)
        self_quotes = [(k, t) for k, t in toks if k == 'quote' and not found(k, t, ev)
                       and any(N.norm(t) in m for m in mine_norm)]
        bad = [(k, t) for k, t in toks if (k, t) not in self_quotes and not found(k, t, ev)]
        for k, t in bad:
            out.append(('T1', s, '%s "%s" is in no tool result of this session and not in your messages' % (k, t), t))
        live_bad = list(self_quotes)
        for rule in C['system_rules']:
            if not re.search(rule['sentence_pattern'], s):
                continue
            live = ev.subset(lambda r: any(r[0].startswith(p) for p in rule['live_tools'])
                             or (r[0] == 'Bash' and any(w in (r[1].get('command') or '') for w in rule['live_bash'])))
            for k, t in toks:
                if k == 'code' and LINE_REF_RE.match(t):
                    continue                   # a line of a local file is not a claim about the outside system
                if k in rule['token_kinds'] and (k, t) not in bad and (k, t) not in self_quotes and not found(k, t, live):
                    live_bad.append((k, t))
                    out.append(('T2', s, '%s "%s" is about %s but was not read from %s itself (%s)' % (
                        k, t, rule['system'], rule['system'], ', '.join(rule['live_tools'] + rule['live_bash'])), t))
        hit = absence_hit(s, C)
        if hit:
            good = [x for x in toks if x not in bad and x not in live_bad and x[0] != 'number']
            if not good:
                out.append(('T3', s, 'absence wording "%s" without a verified id, date, version, quote or `code` '
                                     'in the sentence' % hit, hit))
    return out


def check_turn(transcript_path, last_message=None, C=None):
    C = C or cfg()
    owner, results, turn, mine = load_turn(transcript_path)
    ev = Evidence(owner, results)
    if last_message and (not turn or turn[-1].strip() != last_message.strip()):
        turn.append(last_message)
        mine.append(last_message)
    open_probs = []
    first = len(mine) - len(turn)
    for i, text in enumerate(turn):
        is_fix = text.lstrip().lower().startswith(C['correction_prefix'].lower())
        probs = problems_in(text, C, ev, mine[:first + i])
        if is_fix and not probs:
            # T4: a clean correction resolves an earlier problem only when it restates its token / absence phrase
            low = text.lower()
            open_probs = [p for p in open_probs if p[3].lower() not in low]
            continue
        open_probs.extend(probs)
    return ['G-03 %s: %s -> "%s"' % (k, d, s[:90]) for k, s, d, _ in open_probs]
