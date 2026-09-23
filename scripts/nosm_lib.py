#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared library for the G-01 gate, the sync check and the hooks.

Design rule: nothing the model types is trusted as evidence. Every fact the gate
relies on is taken from the session transcript (the owner's real messages and the
real tool results), from the repo at a path, or recomputed here.
"""
import datetime, glob, hashlib, html, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEXICON_PATH = os.path.join(ROOT, '.claude', 'gates', 'lexicon.json')
CHUNK = 10000                     # chars per part printed by read_source.py
PLACEHOLDER = '\U0001F532'        # the unverified marker


def lexicon():
    with open(LEXICON_PATH, encoding='utf-8') as f:
        return json.load(f)


def now_utc():
    return datetime.datetime.now(datetime.timezone.utc)


def parse_ts(s):
    if not s:
        return None
    try:
        return datetime.datetime.fromisoformat(s.replace('Z', '+00:00'))
    except ValueError:
        return None


# --------------------------------------------------------------------------- transcript

def find_transcript(explicit=None):
    if explicit:
        return explicit
    if os.environ.get('NOSM_TRANSCRIPT'):
        return os.environ['NOSM_TRANSCRIPT']
    slug = re.sub(r'[^A-Za-z0-9]', '-', ROOT)
    files = glob.glob(os.path.expanduser('~/.claude/projects/%s/*.jsonl' % slug))
    if not files:
        raise SystemExit('no session transcript found for %s' % ROOT)
    return max(files, key=os.path.getmtime)


SYSREM_RE = re.compile(r'<system-reminder>.*?</system-reminder>', re.S)
PERSIST_RE = re.compile(r'Output has been saved to (\S+?\.txt)')


class Call:
    __slots__ = ('id', 'name', 'input', 'ts', 'result', 'is_error', 'persisted', 'seq')

    def full_text(self):
        """Complete raw output of the tool (the persisted file when it was too large)."""
        if self.persisted and os.path.exists(self.persisted):
            with open(self.persisted, encoding='utf-8') as f:
                return f.read()
        return self.result or ''

    def json(self):
        try:
            return json.loads(self.full_text())
        except (ValueError, TypeError):
            return None


class Transcript:
    def __init__(self, path):
        self.path = path
        self.prompts = []          # owner's real messages, oldest first
        self.calls = {}            # tool_use_id -> Call
        self.seq = []              # tool_use_ids in the order their results arrived
        uses = {}
        n = 0
        with open(path, encoding='utf-8') as f:
            for line in f:
                try:
                    d = json.loads(line)
                except ValueError:
                    continue
                t = d.get('type')
                msg = d.get('message') or {}
                if t == 'assistant':
                    for b in msg.get('content') or []:
                        if isinstance(b, dict) and b.get('type') == 'tool_use':
                            uses[b['id']] = b
                elif t == 'user':
                    c = msg.get('content')
                    if (d.get('origin') or {}).get('kind') == 'human' and not d.get('isMeta') \
                            and not d.get('isCompactSummary'):
                        if isinstance(c, str):
                            text = c
                        else:
                            text = '\n'.join(b.get('text', '') for b in c or []
                                             if isinstance(b, dict) and b.get('type') == 'text')
                        text = SYSREM_RE.sub('', text).strip()
                        if text:
                            self.prompts.append({'uuid': d.get('uuid'), 'promptId': d.get('promptId'),
                                                 'ts': d.get('timestamp'), 'text': text})
                    if isinstance(c, list):
                        for b in c:
                            if not (isinstance(b, dict) and b.get('type') == 'tool_result'):
                                continue
                            u = uses.get(b.get('tool_use_id'))
                            if not u:
                                continue
                            cont = b.get('content')
                            if isinstance(cont, list):
                                txt = ''.join(x.get('text', '') for x in cont if isinstance(x, dict))
                            else:
                                txt = cont if isinstance(cont, str) else json.dumps(cont, ensure_ascii=False)
                            k = Call()
                            k.id, k.name, k.input = u['id'], u['name'], u.get('input') or {}
                            k.ts, k.result = d.get('timestamp'), txt
                            k.is_error = bool(b.get('is_error')) or txt.startswith('Error:') and not PERSIST_RE.search(txt) \
                                or txt.startswith('MCP error') or 'was denied' in txt[:400] or ' timed out after' in txt[:200]
                            m = PERSIST_RE.search(txt[:600])
                            k.persisted = m.group(1) if m else None
                            if k.persisted:
                                k.is_error = False
                            k.seq = n
                            n += 1
                            self.calls[k.id] = k
                            self.seq.append(k.id)

    def ordered(self):
        return [self.calls[i] for i in self.seq]

    def after(self, call):
        return [c for c in self.ordered() if c.seq > call.seq]


# --------------------------------------------------------------------------- text

TAG_BLOCK_RE = re.compile(r'</?(p|div|li|ul|ol|tr|table|thead|tbody|h[1-6]|br|blockquote|pre|td|th)\b[^>]*>', re.I)
# Only real tags: '<' followed by a letter or '/letter'. A literal '<' in text (e.g. "次数<2")
# must never be eaten - 2026-09-23 live test: text between '<' and '>' vanished from D1/D2.
TAG_RE = re.compile(r'</?[A-Za-z][^<>]*>')
MDLINK_RE = re.compile(r'\[([^\]]*)\]\([^)]*\)')


def strip_markup(s):
    s = html.unescape(html.unescape(s or ''))
    s = TAG_BLOCK_RE.sub('\n', s)
    s = TAG_RE.sub('', s)
    s = MDLINK_RE.sub(r'\1', s)
    return s


def norm(s):
    """Comparison form: markup, markdown emphasis, escapes and ALL whitespace removed."""
    s = strip_markup(s)
    s = s.replace('**', '').replace('`', '').replace('\\', '').replace('*', '')
    return re.sub(r'\s+', '', s)


SEG_SPLIT_RE = re.compile(r'\n|。|；|;|\||(?<=[.!?])\s+')
LIST_MARK_RE = re.compile(r'^\s*(#{1,6}\s*|[-*+>]\s+|\d+[.)]\s+)')


def segments(text):
    """Split a payload / draft / claim into comparable sentence units."""
    out = []
    for raw in SEG_SPLIT_RE.split(strip_markup(text)):
        raw = LIST_MARK_RE.sub('', raw).strip()
        n = norm(raw)
        if len(n) < 2 or not re.search(r'[A-Za-z0-9㐀-鿿]', n):
            continue
        if set(n) <= set('-:|'):
            continue
        out.append((raw, n))
    return out


def flatten_strings(obj, skip=()):
    out = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in skip:
                continue
            out.extend(flatten_strings(v, skip))
    elif isinstance(obj, list):
        for v in obj:
            out.extend(flatten_strings(v, skip))
    elif isinstance(obj, str):
        out.append(obj)
    return out


def readable(call):
    """Human-readable form of a tool result: what read_source.py prints and what quotes are matched against."""
    j = call.json()
    if j is None:
        return call.full_text()
    data = j.get('data', j) if isinstance(j, dict) else j
    if isinstance(data, dict) and isinstance(data.get('body'), dict) and 'value' in data['body']:
        head = 'TITLE: %s\nID: %s\nVERSION: %s\n\n' % (data.get('title'), data.get('id'),
                                                        ((data.get('metadata') or {}).get('version') or {}).get('number'))
        return head + data['body']['value']
    if isinstance(data, dict) and isinstance(data.get('comments'), list):
        parts = []
        for c in data['comments']:
            parts.append('c%s | %s | %s | parent=%s\n%s' % (
                c.get('id'), (c.get('author') or {}).get('displayName'), c.get('created'),
                c.get('parentId'), strip_markup(c.get('body') or '')))
        return '\n\n'.join(parts)
    return json.dumps(j, ensure_ascii=False, indent=1)


def text_sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:12]


def parts_needed(s):
    return max(1, (len(s) + CHUNK - 1) // CHUNK)


def end_marker(call_id, k, m, sha):
    return '<<<END %s PART %d/%d sha=%s>>>' % (call_id, k, m, sha)


def fully_read(tr, call):
    """(ok, detail). Inline results were delivered whole. Persisted results count as read only
    when every part was printed by read_source.py and the output reached its end marker."""
    if not call.persisted:
        return True, 'inline result'
    if not os.path.exists(call.persisted):
        return False, 'persisted file missing: %s' % call.persisted
    txt = readable(call)
    m, sha = parts_needed(txt), text_sha(txt)
    seen = set()
    for c in tr.after(call):
        if c.name != 'Bash':
            continue
        cmd = c.input.get('command', '')
        if 'read_source.py' not in cmd or call.id not in cmd:
            continue
        for k in range(1, m + 1):
            if end_marker(call.id, k, m, sha) in (c.result or ''):
                seen.add(k)
    missing = [k for k in range(1, m + 1) if k not in seen]
    if missing:
        return False, 'persisted result read only partly: parts %s of %d never printed in full by read_source.py' % (missing, m)
    return True, 'persisted result read in %d/%d parts' % (m, m)


# --------------------------------------------------------------------------- numbers

def _cn_to_int(s):
    digits = {'零': 0, '〇': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}
    units = {'十': 10, '百': 100, '千': 1000, '万': 10000}
    total, cur = 0, 0
    for ch in s:
        if ch in digits:
            cur = digits[ch]
        elif ch in units:
            total += (cur or 1) * units[ch]
            cur = 0
    return total + cur


def _word_numbers(text, L):
    """Indonesian / English number words -> list of (matched_text, value, end_pos)."""
    nums = L['numbers']
    idw, mult, enw = nums['id_words'], nums['id_multipliers'], nums['en_words']
    toks = [(m.group(0), m.start(), m.end()) for m in re.finditer(r'[a-zA-Z]+', text)]
    out, i = [], 0
    while i < len(toks):
        w = toks[i][0].lower()
        base = w[2:] if w.startswith('ke') and w[2:] in idw else w      # ketujuh -> tujuh
        if base in idw or w in enw:
            val = idw.get(base, enw.get(w))
            j, end = i + 1, toks[i][2]
            words = [toks[i][0]]
            while j < len(toks):
                nw = toks[j][0].lower()
                if nw in mult:
                    val = val + 10 if mult[nw] == 'teen' else val * mult[nw]
                elif nw in idw and idw[nw] < 10:
                    val += idw[nw]
                elif nw in enw and enw[nw] < 10 and val >= 20:
                    val += enw[nw]
                elif nw == 'hundred':
                    val *= 100
                else:
                    break
                words.append(toks[j][0]); end = toks[j][2]; j += 1
            out.append((' '.join(words), val, end))
            i = j
        else:
            i += 1
    return out


def _mask_ignored(text, L):
    for p in L['numbers']['ignore_phrases']:
        text = re.sub(re.escape(p), ' ' * len(p), text, flags=re.I)
    return text


ISSUE_KEY_RE = r'(?<![A-Za-z0-9])[A-Z][A-Z0-9]+-\d+(?![\d])'


def numeric_tokens(text, L, include_all_cn=False):
    """Every number stated in text: [{'raw', 'value', 'count': bool}].
    count=True when the number is followed by a counting unit (a quantity claim)."""
    t = _mask_ignored(text, L)
    nums = L['numbers']
    cn = nums['cn_numeral_chars']
    units_cn = sorted(set(nums['cn_measure_words']), key=len, reverse=True)
    units_lat = set(u.lower() for u in nums['count_units_latin'])
    out = []
    # ISO dates / times: one token each, compared as strings
    for m in re.finditer(r'\d{4}-\d{2}-\d{2}(?:[T ][\d:.]+Z?)?', t):
        out.append({'raw': m.group(0), 'value': m.group(0), 'count': False, 'kind': 'date'})
    t2 = re.sub(r'\d{4}-\d{2}-\d{2}(?:[T ][\d:.]+Z?)?', lambda m: ' ' * len(m.group(0)), t)
    # Jira issue keys (OSD-116, NSE-1126): identifiers, never quantities (2026-09-23 defect 4)
    for m in re.finditer(ISSUE_KEY_RE, t2):
        out.append({'raw': m.group(0), 'value': m.group(0), 'count': False, 'kind': 'issue_key'})
    t2 = re.sub(ISSUE_KEY_RE, lambda m: ' ' * len(m.group(0)), t2)
    # page codes 04.10 etc: strings
    for m in re.finditer(L['page_code_pattern'], t2):
        out.append({'raw': m.group(0), 'value': m.group(0), 'count': False, 'kind': 'page_code'})
    t3 = re.sub(L['page_code_pattern'], lambda m: ' ' * len(m.group(0)), t2)
    # arabic numerals
    for m in re.finditer(r'\d+', t3):
        if m.start() > 0 and t3[m.start() - 1] in 'vV':
            # a version number (v40) is an identifier, never a quantity
            out.append({'raw': 'v' + m.group(0), 'value': int(m.group(0)), 'count': False, 'kind': 'version'})
            continue
        after = t3[m.end():m.end() + 12].lstrip()
        after_l = after.lower()
        is_count = any(after.startswith(u) for u in units_cn) or \
            (re.match(r'[a-z]+', after_l) and re.match(r'[a-z]+', after_l).group(0) in units_lat)
        frac = re.match(r'\s*(/|dari|of)\s*\d', t3[m.end():m.end() + 8])
        out.append({'raw': m.group(0), 'value': int(m.group(0)), 'count': bool(is_count or frac), 'kind': 'arabic'})
    # chinese numerals: with a measure word, after 第, or in X分之Y. include_all_cn for quotes.
    for m in re.finditer('[%s]+' % cn, t3):
        s = m.group(0)
        before2, after = t3[max(0, m.start() - 2):m.start()], t3[m.end():m.end() + 3]
        is_count = any(after.startswith(u) for u in units_cn) or after.startswith('分之') or before2 == '分之'
        if include_all_cn or is_count or before2.endswith('第'):
            out.append({'raw': s, 'value': _cn_to_int(s), 'count': bool(is_count), 'kind': 'cn'})
    # word numbers
    for raw, val, end in _word_numbers(t3, L):
        after = t3[end:end + 14].strip().lower()
        w = re.match(r'[a-z]+', after)
        frac = re.match(r'(dari|of)\s', after)
        out.append({'raw': raw, 'value': val, 'count': bool((w and w.group(0) in units_lat) or frac), 'kind': 'word'})
    return out


def quote_values(quote, L):
    return {tok['value'] for tok in numeric_tokens(quote, L, include_all_cn=True)}


def quote_count_values(quote, L):
    return {tok['value'] for tok in numeric_tokens(quote, L, include_all_cn=True) if tok['count']}


def absence_hits(text, L):
    low = (text or '').lower()
    return [p for p in L['absence_phrases'] if p.lower() in low]


def fault_hits(segment, L):
    low = segment.lower()
    ppl = [p for p in L['people'] if p.lower() in low]
    flt = [f for f in L['fault_phrases'] if f.lower() in low]
    return ppl, flt


# --------------------------------------------------------------------------- orders

def classify(text, L=None):
    """Mechanical classification of one owner message.
    Returns (cls, detail). cls in WRITE, DRAFT, READONLY, CONFIRM, STOP, AMBIGUOUS.
    Errors are allowed only in the safe direction: a real order may be classified as
    READONLY/AMBIGUOUS (cost: one question), a non-order must never become WRITE."""
    L = L or lexicon()
    ow = L['order_words']
    t = (text or '').lower().strip()

    def is_cjk(term):
        return re.search(r'[\u3400-\u9fff？]', term) is not None

    def finds(term):
        term = term.lower()
        if term in ('?', '？') or is_cjk(term):
            return [m.start() for m in re.finditer(re.escape(term), t)]
        return [m.start() for m in re.finditer(r'(?<![a-z0-9])' + re.escape(term) + r'(?![a-z0-9])', t)]

    def near_before(pos, words, width):
        window = t[max(0, pos - width):pos]
        for n in words:
            n = n.lower()
            if is_cjk(n):
                if n in window:
                    return True
            elif re.search(r'(?<![a-z])' + re.escape(n) + r'(?![a-z])', window):
                return True
        return False

    w = [k for k in ow['write'] if finds(k)]
    dr = [k for k in ow['draft'] if finds(k)]
    dn = [k for k in ow['draft_noun'] if finds(k)]
    r = [k for k in ow['readonly'] if finds(k)]
    st = [k for k in ow['stop'] if finds(k)]
    q = [k for k in ow['question'] if finds(k)]
    cond = [k for k in ow['conditional'] if finds(k)]
    here = [k for k in ow['chat_destination'] if finds(k)]
    neg = [k for k in w + dr if any(near_before(p, ow['negation'], 25) for p in finds(k))]
    first = [k for k in w if any(near_before(p, ow['first_person'], 12) for p in finds(k))]
    detail = {'write': w, 'draft': dr, 'readonly': r, 'stop': st, 'negated': neg,
              'question': q, 'conditional': cond, 'first_person': first, 'chat_destination': here}
    if ow['override_token'].lower() in t:
        detail['override'] = True
    if st or neg:
        return 'STOP', detail
    if len(t) <= ow['confirm_max_chars'] and re.sub(r'[^a-z\u3400-\u9fff ]', '', t).strip() in [c.lower() for c in ow['confirm']]:
        return 'CONFIRM', detail
    if q or cond or here:
        return 'READONLY', detail
    imperative = [k for k in w if k not in first]
    if imperative and (r or dr or dn):
        return 'AMBIGUOUS', detail
    if imperative:
        return 'WRITE', detail
    if dr:
        return 'DRAFT', detail
    return 'READONLY', detail


# --------------------------------------------------------------------------- misc

def rel(path):
    p = os.path.abspath(path)
    return os.path.relpath(p, ROOT) if p.startswith(ROOT) else path


def is_draft_path(path, L=None):
    L = L or lexicon()
    r = rel(path).replace(os.sep, '/')
    return any(re.search(p, r) for p in L['draft_path_patterns'])


def confluence_version(call):
    j = call.json()
    if not isinstance(j, dict):
        return None
    d = j.get('data', {})
    v = ((d.get('metadata') or {}).get('version') or {}).get('number')
    if v is None and isinstance(d.get('snapshotToken'), str) and d['snapshotToken'].startswith('v:'):
        try:
            v = int(d['snapshotToken'][2:])
        except ValueError:
            v = None
    return v


def call_content_id(call):
    inp = call.input
    if call.name == 'mcp__Atlassian_MCP__executeRead':
        inp = inp.get('inputs') or {}
    for k in ('content_id', 'contentId', 'pageId', 'id'):
        if inp.get(k):
            return str(inp[k])
    m = re.search(r'/pages/(\d+)', inp.get('content_url', '') or '')
    return m.group(1) if m else None


def is_full_page_read(call, L):
    if call.is_error:
        return False
    if call.name in L['tools']['confluence_page_read']:
        detail = call.input.get('detail')
    elif call.name == L['tools']['execute_read'] and call.input.get('name') == 'getConfluenceContent':
        detail = (call.input.get('inputs') or {}).get('detail')
    else:
        return False
    j = call.json()
    body = isinstance(j, dict) and isinstance(j.get('data', {}).get('body'), dict)
    return detail == 'full' and body


def page_versions_seen(tr, content_id, L):
    """Every (seq, version) the transcript shows for a page: full/summary/outline reads and version listings."""
    seen = []
    for c in tr.ordered():
        if c.is_error:
            continue
        if (c.name in L['tools']['confluence_page_read'] or
                (c.name == L['tools']['execute_read'] and c.input.get('name') in ('getConfluenceContent',))):
            if call_content_id(c) == content_id:
                v = confluence_version(c)
                if v:
                    seen.append((c.seq, v, c))
        elif c.name == L['tools']['execute_read'] and c.input.get('name') == 'listConfluenceContentVersions':
            if call_content_id(c) == content_id:
                vs = [int(x) for x in re.findall(r'"number"\s*:\s*(\d+)', c.full_text())]
                if vs:
                    seen.append((c.seq, max(vs), c))
    return seen
