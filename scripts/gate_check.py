#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""G-01 evidence gate. Decides whether a draft or an outbound write may exist.

Nothing typed into the ledger is accepted as evidence on its own:
  - the owner's order is read from the owner's real messages in the session transcript;
  - every source must point at a real tool call in the transcript; version, read time,
    completeness and text are taken from that call's actual result;
  - quotes must be found in that result; counts are recounted here; absence claims must
    point at real searches whose results are re-scanned here;
  - every sentence of the payload / draft must be covered by a claim or by clean boilerplate.

Usage:
  python3 scripts/gate_check.py docs/ledger/<write_id>.json [--transcript P] [--json]
Exit 0 = PASS. Exit 1 = FAIL (the hooks refuse the write / the draft).
The rules themselves are listed once, in .claude/gates/G-01-outbound-write.json.
"""
import argparse, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nosm_lib as N
import sync_check

CONSUMED = os.path.join(N.ROOT, 'docs', 'orders', 'consumed.jsonl')
PAYLOAD_SKIP_KEYS = {'cloudId', 'contentId', 'content_id', 'snapshotToken', 'localId', 'name', 'issueIdOrKey',
                     'contentFormat', 'content_format', 'channel_id', 'thread_ts', 'dryRun', 'id', 'pageId',
                     'spaceId', 'parentId', 'responseFields', 'view', 'workflowId'}


# --------------------------------------------------------------------------- helpers

def age_min(ts, now):
    t = N.parse_ts(ts)
    return (now - t).total_seconds() / 60 if t else 1e9


def consumed_orders():
    out = set()
    if os.path.exists(CONSUMED):
        with open(CONSUMED, encoding='utf-8') as f:
            for line in f:
                try:
                    d = json.loads(line)
                except ValueError:
                    continue
                if d.get('event') == 'consumed':
                    out.add(d.get('order_uuid'))
    return out


def find_order(tr, kind, L, now=None):
    """The standing order for this kind of write, or (None, reason).
    A draft order expires after windows_minutes.draft_order_age: 2026-09-23 live test showed a
    'Buat draft dulu' given the day before for another draft being accepted for a new draft."""
    now = now or N.now_utc()
    allowed = ('WRITE',) if kind == 'outbound' else ('WRITE', 'DRAFT')
    idx = None
    for i in range(len(tr.prompts) - 1, -1, -1):
        cls, _ = N.classify(tr.prompts[i]['text'], L)
        if cls in allowed:
            idx = i; break
    if idx is None:
        return None, 'no owner message in this session is classified %s' % '/'.join(allowed)
    order = tr.prompts[idx]
    if kind == 'draft':
        limit = L['windows_minutes']['draft_order_age']
        if age_min(order['ts'], now) > limit:
            return None, 'latest draft/write order "%s" is %.0f min old (limit %d) - it belongs to earlier work; ask the owner' % (
                order['text'][:60], age_min(order['ts'], now), limit)
    later = tr.prompts[idx + 1:]
    for p in later:
        cls, _ = N.classify(p['text'], L)
        if kind == 'outbound' and cls != 'CONFIRM':
            return None, 'order "%s" is no longer standing: a later owner message (%s, %s) is not a plain confirmation' % (
                order['text'][:60], cls, p['text'][:60])
        if cls == 'STOP':
            return None, 'order "%s" was stopped by a later owner message: "%s"' % (order['text'][:60], p['text'][:60])
    return order, ''


def target_of(tool, inp):
    """(system, id) a write tool call is aimed at."""
    x = inp.get('inputs') if tool.endswith('__executeWrite') or tool.endswith('__executeDestructive') else inp
    x = x or {}
    if 'Confluence' in tool or 'confluence' in json.dumps(inp)[:300].lower() and (x.get('contentId') or x.get('pageId')):
        return 'confluence', str(x.get('contentId') or x.get('content_id') or x.get('pageId') or x.get('parentId') or '')
    if 'Jira' in tool or x.get('issueIdOrKey'):
        return 'jira_comment', str(x.get('issueIdOrKey') or x.get('issueKey') or '')
    if tool.startswith('mcp__Slack__'):
        return 'slack', str(x.get('channel_id') or x.get('channel') or '')
    return 'unknown', ''


def payload_text(tool, inp):
    return '\n'.join(N.flatten_strings(inp, PAYLOAD_SKIP_KEYS))


def more_pages(j):
    flag = [False]

    def walk(o, depth=0):
        if isinstance(o, dict):
            if o.get('hasNextPage') is True or o.get('isLast') is False:
                flag[0] = True
            lk = o.get('_links')
            if isinstance(lk, dict) and lk.get('next'):
                flag[0] = True
            for key in ('comments', 'issues', 'results', 'nodes', 'values'):
                if isinstance(o.get(key), list):
                    tot = o.get('total', o.get('totalCount', o.get('totalSize')))
                    start = o.get('startAt', o.get('start', 0)) or 0
                    if isinstance(tot, int) and tot > start + len(o[key]):
                        flag[0] = True
            for v in o.values():
                walk(v, depth + 1)
        elif isinstance(o, list):
            for v in o:
                walk(v, depth + 1)
    walk(j)
    return flag[0]


def query_key(c):
    x = c.input.get('inputs') if c.name.endswith('executeRead') else c.input
    x = x or {}
    for k in ('cql', 'jql', 'query', 'issueIdOrKey'):
        if x.get(k):
            return '%s|%s|%s' % (c.name, x.get('name', c.input.get('name', '')), x[k])
    return '%s|%s' % (c.name, json.dumps(x, sort_keys=True))


def query_text(c):
    x = c.input.get('inputs') if c.name.endswith('executeRead') else c.input
    return json.dumps(x or {}, ensure_ascii=False)


def discovered_ids(c):
    j = c.json()
    ids = set()
    if j is None:
        return ids
    is_comments = c.name.endswith('executeRead') and c.input.get('name') == 'listJiraIssueComments'
    issue = ((c.input.get('inputs') or {}).get('issueIdOrKey') if is_comments else None)

    def walk(o):
        if isinstance(o, dict):
            if is_comments and 'body' in o and re.fullmatch(r'\d+', str(o.get('id', ''))):
                ids.add('jira_comment:%s:%s' % (issue, o['id']))
            elif re.fullmatch(r'\d{6,}', str(o.get('id', ''))) and (o.get('type') == 'page' or 'title' in o):
                ids.add('confluence:%s' % o['id'])
            if isinstance(o.get('key'), str) and re.fullmatch(r'[A-Z][A-Z0-9]+-\d+', o['key']):
                ids.add('jira:%s' % o['key'])
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(j)
    return ids


def comment_pages_complete(calls):
    """calls: listJiraIssueComments calls for one issue. (ok, reason)."""
    pages = []
    for c in calls:
        j = c.json()
        d = (j or {}).get('data', j) if isinstance(j, dict) else None
        if not isinstance(d, dict) or not isinstance(d.get('comments'), list):
            return False, '%s: result has no comments list' % c.id
        rf = c.input.get('responseFields')
        if rf and not {'comments.body', 'isLast', 'startAt'} <= set(rf):
            return False, '%s: responseFields %s drops comments.body / isLast / startAt' % (c.id, rf)
        if 'isLast' not in d or 'startAt' not in d:
            return False, '%s: result does not show isLast/startAt, completeness cannot be proven' % c.id
        pages.append((d['startAt'], len(d['comments']), d['isLast']))
    pages.sort()
    if not pages or pages[0][0] != 0:
        return False, 'comment pages do not start at startAt=0'
    for (s1, n1, _), (s2, _, _) in zip(pages, pages[1:]):
        if s2 > s1 + n1:
            return False, 'gap in comment pages: startAt %d then %d' % (s1, s2)
    if not pages[-1][2]:
        return False, 'last comment page has isLast=false'
    return True, '%d page(s), isLast reached' % len(pages)


# --------------------------------------------------------------------------- evaluation

class Result:
    def __init__(self):
        self.rows = []

    def add(self, cid, ok, detail=''):
        self.rows.append((cid, bool(ok), detail))

    @property
    def ok(self):
        return all(ok for _, ok, _ in self.rows)

    def failed(self):
        return [c for c, ok, _ in self.rows if not ok]


def evaluate(ledger, tr, now=None, tool_name=None, tool_input=None, L=None):
    L = L or N.lexicon()
    now = now or N.now_utc()
    R = Result()
    kind = ledger.get('kind')
    if kind not in ('outbound', 'draft'):
        R.add('L0', False, 'ledger.kind must be "outbound" or "draft"'); return R, None
    window = L['windows_minutes']['outbound_source_age' if kind == 'outbound' else 'draft_source_age']
    tgt = ledger.get('target') or {}

    # ---------------- A: session prerequisites
    atl = [c for c in tr.ordered() if c.name.startswith('mcp__Atlassian') and not c.is_error and age_min(c.ts, now) <= 720]
    n8n = [c for c in tr.ordered() if c.name in L['tools']['n8n_list'] and not c.is_error and age_min(c.ts, now) <= 720]
    R.add('A1', atl and n8n, 'Atlassian read ok: %s; n8n search_workflows ok: %s (within 12 h)' % (bool(atl), bool(n8n)))
    ok, lines = sync_check.run(tr, L, now)
    R.add('A2', ok, lines[-1] if lines else '')
    sweep = [c for c in tr.ordered() if c.name in L['tools']['confluence_search'] and not c.is_error
             and 'lastmodified' in query_text(c).lower() and 'NOSM' in query_text(c) and age_min(c.ts, now) <= 720]
    R.add('A3', sweep, 'space-wide lastmodified sweep within 12 h: %s' % (sweep[-1].id if sweep else 'NONE'))

    # ---------------- B: authorization
    order, why = find_order(tr, kind, L, now)
    R.add('B1', order is not None, ('order: "%s" (%s)' % (order['text'][:80], order['ts'])) if order else why)
    if kind == 'outbound':
        R.add('B2', order is not None and order['uuid'] not in consumed_orders(),
              'order already used for a previous write' if order and order['uuid'] in consumed_orders() else 'order not used before')
        named = set(re.findall(r'\b[A-Z][A-Z0-9]+-\d+\b', order['text'])) | set(re.findall(r'\b\d{9,11}\b', order['text'])) if order else set()
        tid = str(tgt.get('content_id') or tgt.get('issue') or tgt.get('channel') or '')
        R.add('B3', not named or tid in named, ('order names %s, target is %s' % (sorted(named), tid)) if named else 'order names no target id; target taken from ledger')
        tool = tool_name or ledger.get('tool') or ''
        R.add('B4', not tool.startswith(L['tools']['backend_ops_account_prefix']),
              'tool %s %s' % (tool, 'uses the Backend Operations account - forbidden' if tool.startswith(L['tools']['backend_ops_account_prefix']) else 'ok'))

    # ---------------- payload
    if kind == 'draft':
        p = os.path.join(N.ROOT, tgt.get('path', ''))
        if not tgt.get('path') or not os.path.exists(p):
            R.add('P0', False, 'draft file %s not found' % tgt.get('path')); return R, None
        with open(p, encoding='utf-8') as f:
            ptext = f.read()
        pinput = None
    else:
        pf = ledger.get('payload_file')
        if not pf or not os.path.exists(os.path.join(N.ROOT, pf)):
            R.add('P0', False, 'payload_file missing: %s' % pf); return R, None
        with open(os.path.join(N.ROOT, pf), encoding='utf-8') as f:
            pinput = json.load(f)
        if tool_input is not None:
            same = json.dumps(tool_input, sort_keys=True, ensure_ascii=False) == json.dumps(pinput, sort_keys=True, ensure_ascii=False)
            R.add('P0', same, 'tool input is byte-identical to payload_file' if same else 'tool input differs from payload_file - gate evidence does not cover what is being sent')
            s_tgt = target_of(tool_name, tool_input)
            R.add('P1', s_tgt[1] == str(tgt.get('content_id') or tgt.get('issue') or tgt.get('channel') or ''),
                  'call targets %s:%s, ledger targets %s' % (s_tgt[0], s_tgt[1], tgt))
        ptext = payload_text(ledger.get('tool', ''), pinput)

    # ---------------- C: discovery and sources
    disc = ledger.get('discovery') or {}
    dcalls = []
    bad = []
    for cid in disc.get('calls') or []:
        c = tr.calls.get(cid)
        if not c:
            bad.append('%s not in transcript' % cid); continue
        if c.is_error:
            bad.append('%s returned an error' % cid); continue
        if age_min(c.ts, now) > window:
            bad.append('%s is %.0f min old (limit %d)' % (cid, age_min(c.ts, now), window)); continue
        dcalls.append(c)
    terms = disc.get('topic_terms') or []
    qtexts = [query_text(c) for c in dcalls]
    unsearched = [t for t in terms if not any(t.lower() in q.lower() for q in qtexts)]
    conf = [c for c in dcalls if c.name in L['tools']['confluence_search'] and 'NOSM' in query_text(c)]
    R.add('C1', dcalls and not bad and terms and not unsearched and conf,
          '; '.join(bad + (['topic_terms empty'] if not terms else []) +
                    (['never searched for: %s' % unsearched] if unsearched else []) +
                    ([] if conf else ['no space NOSM Confluence search among discovery calls'])) or
          '%d discovery calls, terms %s all searched' % (len(dcalls), terms))
    by_q = {}
    for c in dcalls:
        by_q.setdefault(query_key(c), []).append(c)
    unpaged = [k.split('|')[-1][:60] for k, cs in by_q.items() if all(more_pages(c.json()) for c in cs)]
    R.add('C2', not unpaged, ('results have further pages never fetched: %s' % unpaged) if unpaged else 'every search reached its last page')

    sources = {s['source_id']: s for s in ledger.get('sources') or [] if s.get('source_id')}
    src_text, src_meta, sbad, sread = {}, {}, [], []
    covered = set()
    for sid, s in sources.items():
        system = s.get('system')
        calls = [tr.calls.get(x) for x in ([s['read_call']] if s.get('read_call') else s.get('read_calls') or [])]
        if not calls or any(c is None for c in calls):
            sbad.append('%s: read call not in transcript' % sid); continue
        stale = [c.id for c in calls if age_min(c.ts, now) > window]
        if stale:
            sbad.append('%s: read %s older than %d min - read it again' % (sid, stale, window)); continue
        if any(c.is_error for c in calls):
            sbad.append('%s: read call returned an error' % sid); continue
        if system == 'confluence':
            c = calls[0]
            if not N.is_full_page_read(c, L) or N.call_content_id(c) != str(s.get('content_id')):
                sbad.append('%s: %s is not a full (detail=full) read of page %s' % (sid, c.id, s.get('content_id'))); continue
            v = N.confluence_version(c)
            later = [(q, vv) for q, vv, _ in N.page_versions_seen(tr, str(s['content_id']), L) if q > c.seq and vv != v]
            if later:
                sbad.append('%s: read at v%s but the transcript later shows v%s - stale' % (sid, v, later[-1][1])); continue
            title = (c.json().get('data') or {}).get('title', '')
            src_meta[sid] = {'version': v, 'title': title, 'ts': c.ts, 'id': str(s['content_id'])}
            covered |= {'confluence:%s' % s['content_id']}
        elif system == 'jira_comments':
            if not all(c.name == L['tools']['execute_read'] and c.input.get('name') == 'listJiraIssueComments'
                       and (c.input.get('inputs') or {}).get('issueIdOrKey') == s.get('issue') for c in calls):
                sbad.append('%s: read_calls must all be listJiraIssueComments on %s' % (sid, s.get('issue'))); continue
            ok, why = comment_pages_complete(calls)
            if not ok:
                sbad.append('%s: %s' % (sid, why)); continue
            src_meta[sid] = {'ts': calls[-1].ts, 'id': s['issue'], 'title': s['issue']}
            covered |= {'jira:%s' % s['issue'], 'jira_comments:%s' % s['issue']}
        elif system == 'jira_issue':
            c = calls[0]
            if c.name not in L['tools']['jira_issue_read'] or c.input.get('issueIdOrKey') != s.get('issue'):
                sbad.append('%s: %s is not a getJiraIssue on %s' % (sid, c.id, s.get('issue'))); continue
            src_meta[sid] = {'ts': c.ts, 'id': s['issue'], 'title': s['issue']}
            covered |= {'jira:%s' % s['issue']}
        elif system == 'slack_thread':
            c = calls[0]
            if c.name not in L['tools']['slack_thread_read'] or c.input.get('channel_id') != s.get('channel') or c.input.get('message_ts') != s.get('ts'):
                sbad.append('%s: %s is not slack_read_thread on %s/%s' % (sid, c.id, s.get('channel'), s.get('ts'))); continue
            src_meta[sid] = {'ts': c.ts, 'id': s.get('ts'), 'title': 'slack'}
        elif system == 'n8n_workflow':
            c = calls[0]
            if c.name not in L['tools']['n8n_workflow_read'] or c.input.get('workflowId') != s.get('workflow_id'):
                sbad.append('%s: %s is not get_workflow_details on %s' % (sid, c.id, s.get('workflow_id'))); continue
            src_meta[sid] = {'ts': c.ts, 'id': s.get('workflow_id'), 'title': 'n8n'}
        else:
            sbad.append('%s: system %r is not an accepted source (repo notes and memory are not sources)' % (sid, system)); continue
        partial = [why for ok, why in (N.fully_read(tr, c) for c in calls) if not ok]
        if partial:
            sread.append('%s: %s' % (sid, '; '.join(partial)))
        src_text[sid] = N.norm('\n'.join(N.readable(c) for c in calls))
    R.add('C4', not sbad, '; '.join(sbad) or '%d sources read live, latest version, within %d min' % (len(sources), window))
    R.add('C5', not sread, '; '.join(sread) or 'every source was delivered to the end')

    found = set()
    for c in dcalls:
        found |= discovered_ids(c)
    excluded = disc.get('excluded') or {}
    weak = [k for k, v in excluded.items() if len((v or '').strip()) < 15]
    uncovered = []
    for i in sorted(found):
        if i in covered or i in excluded:
            continue
        if i.startswith('jira_comment:'):
            issue = i.split(':')[1]
            if 'jira_comments:%s' % issue in covered or 'jira_comments:%s' % issue in excluded:
                continue
        uncovered.append(i)
    R.add('C3', not uncovered and not weak,
          '; '.join((['found by search but neither read nor excluded: %s' % uncovered[:15] + (' (+%d more)' % (len(uncovered) - 15) if len(uncovered) > 15 else '')] if uncovered else []) +
                    (['exclusion reason too short: %s' % weak] if weak else [])) or
          '%d search hits: all read or excluded with a reason' % len(found))

    # ---------------- D: claims against the payload
    claims = ledger.get('claims') or []
    claim_segs, cbad, nbad, abad, nnbad = set(), [], [], [], []
    allowed_vals = set()
    for m in src_meta.values():
        if m.get('version'):
            allowed_vals.add(m['version'])
        if m.get('id') and str(m['id']).isdigit():
            allowed_vals.add(int(m['id']))
    for k in claims:
        text = k.get('text') or ''
        for _, n in N.segments(text):
            claim_segs.add(n)
        if N.PLACEHOLDER in text:
            continue
        sid, quote = k.get('source_id'), k.get('quote') or ''
        if sid not in src_text:
            cbad.append('%s: source %r not a verified source' % (k.get('id'), sid)); continue
        qn = N.norm(quote)
        if len(qn) < 6 or qn not in src_text[sid]:
            cbad.append('%s: quote not found verbatim in %s as read' % (k.get('id'), sid)); continue
        # numbers
        qv, qc = N.quote_values(quote, L), N.quote_count_values(quote, L)
        counts = k.get('counts') or []
        for tok in N.numeric_tokens(text, L):
            if tok['kind'] == 'issue_key':
                # an issue key is an identifier: it must be a source this ledger read, or be quoted
                if N.norm(tok['value']) in qn or any(str(m.get('id')) == tok['value'] for m in src_meta.values()):
                    continue
                nnbad.append('%s: mentions issue %s without reading it or quoting it' % (k.get('id'), tok['value']))
                continue
            if tok['kind'] in ('date', 'page_code'):
                if N.norm(tok['value']) in qn or any(str(m.get('ts', '')).startswith(tok['value']) for m in src_meta.values()):
                    continue
                if tok['kind'] == 'page_code' and any(re.match(re.escape(tok['value']) + r'(?![\d.])', m.get('title', '')) for m in src_meta.values()):
                    continue
                if tok['kind'] == 'page_code':
                    nnbad.append('%s: mentions page %s without reading it or quoting it' % (k.get('id'), tok['value']))
                else:
                    nbad.append('%s: date %s not in quote' % (k.get('id'), tok['value']))
                continue
            if tok['count']:
                if tok['value'] in qc:
                    continue
                hit = None
                for cs in counts:
                    if cs.get('value') != tok['value'] or cs.get('source_id') not in sources:
                        continue
                    s = sources[cs['source_id']]
                    calls = [tr.calls.get(x) for x in ([s['read_call']] if s.get('read_call') else s.get('read_calls') or [])]
                    body = '\n'.join(N.readable(c) for c in calls if c)
                    if cs.get('section'):
                        i0 = body.find(cs['section'])
                        body = body[i0:] if i0 >= 0 else ''
                        nxt = re.search(r'\n#{1,6} ', body[1:])
                        body = body[:nxt.start() + 1] if nxt else body
                    try:
                        got = len(re.findall(cs.get('regex', ''), body, re.M))
                    except re.error as e:
                        got = 'regex error %s' % e
                    hit = got == tok['value']
                    if not hit:
                        nbad.append('%s: says %s but regex counts %s in %s' % (k.get('id'), tok['raw'], got, cs['source_id']))
                    break
                if hit is None:
                    nbad.append('%s: count "%s" is neither stated in the quote nor recounted (counts[])' % (k.get('id'), tok['raw']))
                continue
            if tok['value'] in qv or tok['value'] in allowed_vals:
                continue
            nbad.append('%s: number "%s" does not appear in the quote' % (k.get('id'), tok['raw']))
        # absence
        if N.absence_hits(text, L) and not N.absence_hits(quote, L):
            a = k.get('absence') or {}
            ok, why = True, ''
            sc = [tr.calls.get(x) for x in a.get('searched') or []]
            ctl = tr.calls.get((a.get('control') or {}).get('call', ''))
            if len(set(a.get('searched') or [])) < 2 or any(c is None or c.is_error for c in sc):
                ok, why = False, 'needs >= 2 real, successful searched calls'
            elif not a.get('pattern') or not ctl or ctl.is_error or not (a.get('control') or {}).get('pattern'):
                ok, why = False, 'needs pattern and a control {call, pattern}'
            else:
                try:
                    hits = [c.id for c in sc if re.search(a['pattern'], N.readable(c), re.I)]
                    ctl_ok = re.search(a['control']['pattern'], N.readable(ctl), re.I)
                except re.error as e:
                    hits, ctl_ok = ['regex error %s' % e], None
                stale = [c.id for c in sc + [ctl] if age_min(c.ts, now) > window]
                if hits:
                    ok, why = False, 'pattern IS present in %s - the thing exists' % hits
                elif not ctl_ok:
                    ok, why = False, 'control search did not find its pattern - the method is not shown to work'
                elif ctl.name not in {c.name for c in sc}:
                    ok, why = False, 'control used a different tool than the searches'
                elif stale:
                    ok, why = False, 'searches older than %d min: %s' % (window, stale)
            if not ok:
                abad.append('%s: absence claim (%s): %s' % (k.get('id'), ', '.join(N.absence_hits(text, L)[:3]), why))
        # near names
        tn = N.norm(text)
        for g in L['near_name_groups']:
            for term in g['terms']:
                if N.norm(term) in tn and N.norm(term) not in qn:
                    nnbad.append('%s: says "%s" but the quote does not (group %s)' % (k.get('id'), term, g['terms']))
    R.add('D2', not cbad, '; '.join(cbad) or 'every claim quotes its source verbatim')
    R.add('D3', not nbad, '; '.join(nbad) or 'every number is quoted or recounted')
    R.add('D4', not abad, '; '.join(abad) or 'every absence claim is backed by searches + control')
    R.add('D5', not nnbad, '; '.join(nnbad) or 'near names and page codes used exactly as read')

    # boilerplate
    bp_segs, bpbad = set(), []
    for b in ledger.get('boilerplate') or []:
        for raw, n in N.segments(b):
            bp_segs.add(n)
            struct = any(re.search(p, raw) for p in L['numbers']['structural_label_patterns'])
            if N.absence_hits(raw, L):
                bpbad.append('"%s": absence wording is a claim, not boilerplate' % raw[:40])
            elif N.numeric_tokens(raw, L) and not struct:
                bpbad.append('"%s": numbers are claims, not boilerplate' % raw[:40])
    R.add('D6', not bpbad, '; '.join(bpbad) or 'boilerplate carries no facts')

    # coverage of the text actually going out
    existing = ''
    if kind == 'outbound' and tgt.get('system') == 'confluence':
        reads = [c for c in tr.ordered() if N.call_content_id(c) == str(tgt.get('content_id')) and N.is_full_page_read(c, L)]
        existing = N.norm(N.readable(reads[-1])) if reads else ''
    uncovered_text, blame = [], []
    for raw, n in N.segments(ptext):
        ppl, flt = N.fault_hits(raw, L)
        if ppl and flt:
            blame.append('"%s" (%s + %s)' % (raw[:50], ppl, flt))
        if n in claim_segs or n in bp_segs or (existing and n in existing):
            continue
        uncovered_text.append(raw[:70])
    R.add('D1', not uncovered_text, ('sentences with no claim behind them: %s' % uncovered_text[:8] +
                                     (' (+%d more)' % (len(uncovered_text) - 8) if len(uncovered_text) > 8 else '')) if uncovered_text
          else 'every sentence is a claim, clean boilerplate or unchanged existing text')
    R.add('D7', not blame, ('person named next to fault wording: %s' % blame[:5]) if blame else 'no person is blamed')

    # ---------------- E: target freshness (outbound)
    if kind == 'outbound':
        if tgt.get('system') == 'confluence':
            cid = str(tgt.get('content_id'))
            seen = N.page_versions_seen(tr, cid, L)
            full = [c for c in tr.ordered() if N.call_content_id(c) == cid and N.is_full_page_read(c, L)]
            snap = (pinput or {}).get('snapshotToken') or ((pinput or {}).get('inputs') or {}).get('snapshotToken')
            want = int(snap[2:]) if isinstance(snap, str) and snap.startswith('v:') else None
            latest = seen[-1][1] if seen else None
            fresh = full and age_min(full[-1].ts, now) <= window
            R.add('E1', fresh and (want is None or latest == want),
                  'target v%s last seen, edit based on %s, last full read %s' % (latest, snap, full[-1].ts if full else 'NONE'))
        elif tgt.get('system') == 'jira_comment':
            calls = [c for c in tr.ordered() if c.name == L['tools']['execute_read'] and c.input.get('name') == 'listJiraIssueComments'
                     and (c.input.get('inputs') or {}).get('issueIdOrKey') == tgt.get('issue') and age_min(c.ts, now) <= window]
            ok, why = comment_pages_complete(calls[-3:]) if calls else (False, 'no comment listing within %d min' % window)
            R.add('E1', ok, 'target issue comments read to the end before replying: %s' % why)
        else:
            R.add('E1', True, 'no freshness rule for %s' % tgt.get('system'))
    return R, order


def load_gate_names():
    with open(os.path.join(N.ROOT, '.claude', 'gates', 'G-01-outbound-write.json'), encoding='utf-8') as f:
        g = json.load(f)
    return {c['id']: c['name'] for c in g['checks']}


def render(R, ledger):
    names = load_gate_names()
    out = ['=' * 70, 'G-01 EVIDENCE GATE - %s (%s)' % (ledger.get('write_id', '(no id)'), ledger.get('kind')), '=' * 70]
    order = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'B4', 'P0', 'P1', 'L0', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'E1']
    for cid, ok, detail in sorted(R.rows, key=lambda r: order.index(r[0]) if r[0] in order else 99):
        out.append('%-3s %-30s %s' % (cid, names.get(cid, ''), 'PASS' if ok else 'FAIL'))
        if detail:
            out.append('      %s' % detail)
    out.append('-' * 70)
    out.append(('VERDICT: FAIL on %s -> NOT ALLOWED' % ', '.join(R.failed())) if not R.ok else 'VERDICT: PASS')
    return '\n'.join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('ledger')
    ap.add_argument('--transcript')
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args()
    with open(a.ledger, encoding='utf-8') as f:
        ledger = json.load(f)
    tr = N.Transcript(N.find_transcript(a.transcript))
    R, _ = evaluate(ledger, tr)
    if a.json:
        print(json.dumps({'ok': R.ok, 'rows': R.rows}, ensure_ascii=False))
    else:
        print(render(R, ledger))
    return 0 if R.ok else 1


if __name__ == '__main__':
    sys.exit(main())
