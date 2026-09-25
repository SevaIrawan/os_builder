# -*- coding: utf-8 -*-
"""G-02: n8n build discipline. Rules and their sources live in .claude/gates/G-02-n8n-build.json only.

check_pre(tool, input, tr, L, now, before_seq)  -> problems before an n8n write (PreToolUse)
check_stop(tr, L, now)                           -> problems that keep the turn open (Stop)
open_items()                                     -> legacy items printed every turn (UserPromptSubmit)

Evidence comes from the session transcript (real tool results) and files in the repo, never from
what the model types. before_seq limits the transcript to calls that happened before the call being
checked (used by the self-test to replay past calls; live hooks see only earlier calls anyway)."""
import json, os, re, subprocess, tempfile
from _common import N
import gate_check

G02_PATH = os.path.join(N.ROOT, '.claude', 'gates', 'G-02-n8n-build.json')
EXTRACT_JS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'g02_extract.js')
INF = 10 ** 12


def cfg():
    with open(G02_PATH, encoding='utf-8') as f:
        return json.load(f)


def write_tools(C):
    return [t for v in C['write_tools'].values() for t in v]


def kind_of(C, tool):
    for k, v in C['write_tools'].items():
        if tool in v:
            return k
    return None


def calls_before(tr, before_seq):
    return [c for c in tr.ordered() if c.seq < before_seq]


def result_json(c):
    j = c.json()
    return j if isinstance(j, dict) else None


def write_ok(c):
    """A write call that really changed n8n: no tool error and no {"error": ...} body."""
    if c.is_error:
        return False
    j = result_json(c)
    return j is not None and not j.get('error')


def written_id(c, C):
    if kind_of(C, c.name) == 'create':
        return (result_json(c) or {}).get('workflowId')
    return c.input.get('workflowId')


def writes_to(tr, C, wid, before_seq, since=None):
    out = []
    for c in calls_before(tr, before_seq):
        if c.name in write_tools(C) and kind_of(C, c.name) != 'run' and write_ok(c) and written_id(c, C) == wid:
            if since is None or (N.parse_ts(c.ts) and N.parse_ts(c.ts) >= since):
                out.append(c)
    return out


def latest_details(tr, C, wid, before_seq, after_seq=-1):
    ds = [c for c in calls_before(tr, before_seq) if c.name == C['details_tool'] and not c.is_error
          and c.input.get('workflowId') == wid and c.seq > after_seq and (result_json(c) or {}).get('workflow')]
    return ds[-1] if ds else None


def workflow_name(tr, C, wid, before_seq):
    d = latest_details(tr, C, wid, before_seq)
    if d:
        return result_json(d)['workflow'].get('name')
    for c in reversed(calls_before(tr, before_seq)):
        if c.name in C['write_tools']['create'] and write_ok(c) and result_json(c).get('workflowId') == wid:
            return result_json(c).get('name')
    return None


def flow_for_name(C, name):
    for f in C['flows']:
        if name and name.startswith(f['name_prefix']):
            return f
    return None


# ---------------------------------------------------------------- page reads (P1, P6, P7, S2, S3)

def page_read(tr, L, C, page, now, before_seq, after_seq=-1, check_age=True):
    """(call, problem). The latest full read of page in (after_seq, before_seq), read to the end,
    at the newest version seen in the session, and (check_age) within read_max_age_min."""
    cs = [c for c in calls_before(tr, before_seq) if c.seq > after_seq and N.is_full_page_read(c, L)
          and N.call_content_id(c) == page]
    if not cs:
        return None, 'page %s not read in full (getConfluenceContent detail=full)' % page
    c = cs[-1]
    if check_age:
        age = gate_check.age_min(c.ts, now)
        if age > C['read_max_age_min']:
            return None, 'page %s last read in full %d min ago (max %d)' % (page, age, C['read_max_age_min'])
    seen = [v for s, v, _ in N.page_versions_seen(tr, page, L) if s < before_seq]
    v = N.confluence_version(c)
    if seen and v is not None and v < max(seen):
        return None, 'page %s read at v%s but v%s was seen later' % (page, v, max(seen))
    ok, why = N.fully_read(tr, c, before_seq=before_seq)
    if not ok:
        return None, 'page %s: %s' % (page, why)
    return c, None


# ---------------------------------------------------------------- code checks (P2)

def extract_sdk_nodes(code):
    r = subprocess.run(['node', EXTRACT_JS], input=code, capture_output=True, text=True, timeout=30)
    if r.returncode != 0:
        raise ValueError('SDK code could not be evaluated for G-02 checks: %s' % (r.stderr.strip()[:300] or 'no output'))
    return json.loads(r.stdout or '[]')


def node_check(code):
    """'' when node --check accepts the code as a Code-node body, else the error text."""
    with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
        f.write('async function __n8n_code_node__() {\n' + code + '\n}\n')
        path = f.name
    try:
        r = subprocess.run(['node', '--check', path], capture_output=True, text=True, timeout=30)
        return '' if r.returncode == 0 else (r.stderr.strip().splitlines() or ['syntax error'])[-1]
    finally:
        os.unlink(path)


REGEX_PREV_WORDS = {'return', 'typeof', 'case', 'in', 'of', 'new', 'delete', 'void', 'throw', 'instanceof', 'else', 'do'}


def trailing_comments(code):
    """Line numbers where a // comment follows code on the same line (07.06.1 D2)."""
    out, i, n, line, has_code, prev, word = [], 0, len(code), 1, False, '', ''
    while i < n:
        ch = code[i]
        if ch == '\n':
            line += 1; has_code = False; i += 1; continue
        if ch in ' \t\r':
            i += 1; continue
        if code.startswith('//', i):
            if has_code:
                out.append(line)
            j = code.find('\n', i); i = n if j < 0 else j; continue
        if code.startswith('/*', i):
            j = code.find('*/', i + 2); j = n if j < 0 else j + 2
            line += code.count('\n', i, j); i = j; continue
        if ch in '"\'':
            j = i + 1
            while j < n and code[j] != ch and code[j] != '\n':
                j += 2 if code[j] == '\\' else 1
            i = j + 1; has_code = True; prev, word = 'a', ''; continue
        if ch == '`':
            j, depth = i + 1, 0
            while j < n:
                c2 = code[j]
                if c2 == '\\':
                    j += 2; continue
                if depth == 0 and c2 == '`':
                    break
                if code.startswith('${', j):
                    depth += 1; j += 2; continue
                if depth and c2 == '}':
                    depth -= 1
                if c2 == '\n':
                    line += 1
                j += 1
            i = j + 1; has_code = True; prev, word = 'a', ''; continue
        if ch == '/' and (prev == '' or prev in '(,=:[!&|?{};+-*%<>~^' or word in REGEX_PREV_WORDS):
            j, cls = i + 1, False
            while j < n and code[j] != '\n':
                c2 = code[j]
                if c2 == '\\':
                    j += 2; continue
                if c2 == '[':
                    cls = True
                elif c2 == ']':
                    cls = False
                elif c2 == '/' and not cls:
                    break
                j += 1
            j += 1
            while j < n and code[j].isalpha():
                j += 1
            i = j; has_code = True; prev, word = 'a', ''; continue
        if ch.isalnum() or ch in '_$':
            j = i
            while j < n and (code[j].isalnum() or code[j] in '_$'):
                j += 1
            word, prev = code[i:j], 'a'; has_code = True; i = j; continue
        prev, word = ch, ''; has_code = True; i += 1
    return out


def code_problems(label, code):
    probs = []
    err = node_check(code)
    if err:
        probs.append('P2 %s: node --check failed: %s' % (label, err))
    tc = trailing_comments(code)
    if tc:
        probs.append('P2 %s: // comment after code on line(s) %s (07.06.1 D2: comments on their own line)' % (label, tc))
    return probs


# ---------------------------------------------------------------- idempotency (P3)

def non_idempotent(C, ntype, params):
    ni = C['non_idempotent']
    if ntype == 'n8n-nodes-base.httpRequest':
        return str(params.get('method') or 'GET').upper() not in ni['http_methods_ok']
    if ntype == 'n8n-nodes-base.jira':
        return str(params.get('operation') or 'create') not in ni['jira_operations_ok']
    return ntype in ni['always_non_idempotent_types']


# ---------------------------------------------------------------- JSON pointer

def pointer_get(obj, path):
    cur = obj
    for part in path.lstrip('/').split('/'):
        part = part.replace('~1', '/').replace('~0', '~')
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur


def as_text(v):
    return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False, separators=(',', ':'))


# ---------------------------------------------------------------- Jira evidence

def jira_comments(tr, C, feature, before_seq, after_seq):
    out = []
    for c in calls_before(tr, before_seq):
        if c.seq <= after_seq or c.name not in C['jira_comment_tools'] or c.is_error:
            continue
        if str(c.input.get('issueIdOrKey', '')).upper() != feature.upper():
            continue
        if 'successfully' not in (c.result or '')[:400] and '"commentId"' not in (c.result or ''):
            continue
        out.append(c)
    return out


def comment_text(c):
    return N.norm(c.input.get('commentBody') or '')


# ---------------------------------------------------------------- PreToolUse

def check_pre(tool, ti, tr, L, now=None, before_seq=INF):
    C = cfg()
    kind = kind_of(C, tool)
    if not kind:
        return []
    now = now or N.now_utc()
    probs = []

    # which workflow, which flow
    if kind == 'create':
        wid, name = None, ti.get('name')
        nodes = None
        try:
            nodes = extract_sdk_nodes(ti.get('code') or '')
        except (ValueError, subprocess.SubprocessError, OSError) as e:
            probs.append('P2 %s' % e)
        if not name:
            m = re.search(r"workflow\(\s*['\"][^'\"]*['\"]\s*,\s*['\"]([^'\"]+)['\"]", ti.get('code') or '')
            name = m.group(1) if m else None
    else:
        wid = ti.get('workflowId')
        name = workflow_name(tr, C, wid, before_seq)
        nodes = None
    flow = flow_for_name(C, name)
    if not flow:
        probs.append('P1 workflow %s (%s) matches no flow in G-02 flows; read the workflow first (get_workflow_details) '
                     'or add the flow to G-02 (owner, UNLOCK G-01)' % (wid or 'new', name))
        return probs

    # P1 reads
    pages = [r['page'] for r in C['required_reads']] + [flow['spec'], flow['build_sheet']]
    for p in pages:
        _, why = page_read(tr, L, C, p, now, before_seq)
        if why:
            probs.append('P1 ' + why)

    # current state of an existing workflow
    last_w = None
    cur = None
    if wid:
        ws = writes_to(tr, C, wid, before_seq)
        last_w = ws[-1].seq if ws else -1
        d = latest_details(tr, C, wid, before_seq, after_seq=last_w)
        cur = result_json(d)['workflow'] if d else None

    def node_of(nm):
        for nd in (cur or {}).get('nodes', []):
            if nd.get('name') == nm:
                return nd
        return None

    ops = ti.get('operations') or []
    added = {o['node']['name']: o['node'] for o in ops if o.get('type') == 'addNode' and isinstance(o.get('node'), dict)}

    # P2 code
    if kind == 'create' and nodes:
        for nd in nodes:
            for key in ('jsCode', 'functionCode'):
                if isinstance(nd['parameters'].get(key), str):
                    probs += code_problems('node "%s"' % nd.get('name'), nd['parameters'][key])
    for o in ops:
        t = o.get('type')
        if t == 'setNodeParameter' and o.get('path') in ('/jsCode', '/functionCode') and isinstance(o.get('value'), str):
            probs += code_problems('node "%s"' % o.get('nodeName'), o['value'])
        elif t == 'updateNodeParameters':
            for key in ('jsCode', 'functionCode'):
                if isinstance((o.get('parameters') or {}).get(key), str):
                    probs += code_problems('node "%s"' % o.get('nodeName'), o['parameters'][key])
        elif t == 'addNode':
            for key in ('jsCode', 'functionCode'):
                v = ((o.get('node') or {}).get('parameters') or {}).get(key)
                if isinstance(v, str):
                    probs += code_problems('node "%s"' % o['node'].get('name'), v)

    # P3 retry
    if kind == 'create' and nodes:
        for nd in nodes:
            retry = nd.get('retryOnFail') or (nd.get('settings') or {}).get('retryOnFail')
            if retry and non_idempotent(C, nd['type'], nd['parameters']):
                probs.append('P3 node "%s" (%s) has retryOnFail on a non-idempotent write' % (nd.get('name'), nd['type']))
    for o in ops:
        if o.get('type') == 'setNodeSettings' and (o.get('settings') or {}).get('retryOnFail') is True:
            nd = added.get(o.get('nodeName')) or node_of(o.get('nodeName'))
            if nd is None:
                probs.append('P3 node "%s": retryOnFail set but the node type is unknown (read the workflow first)' % o.get('nodeName'))
            elif non_idempotent(C, nd.get('type'), nd.get('parameters') or {}):
                probs.append('P3 node "%s" (%s) gets retryOnFail on a non-idempotent write' % (o.get('nodeName'), nd.get('type')))

    # P4 credentials
    for o in ops:
        if o.get('type') == 'setNodeCredential':
            nd = added.get(o.get('nodeName')) or node_of(o.get('nodeName'))
            if nd is None or nd.get('type') == 'n8n-nodes-base.httpRequest':
                probs.append('P4 node "%s": httpRequest credentials cannot be attached through the API '
                             '(07.06.1 E5); attach them in the n8n UI and record the UI check' % o.get('nodeName'))

    # P6 / P8 new workflow
    if kind == 'create':
        if not flow.get('registry_volume'):
            probs.append('P6 flow %s has no 04.9 volume set in G-02: a new workflow cannot be registered in the same step '
                         '(04.9 §一 三位一体, 07.06 §四-5 不得先建后补). %s' % (flow['id'], flow.get('open_question', '')))
        else:
            _, why = page_read(tr, L, C, flow['registry_volume'], now, before_seq)
            if why:
                probs.append('P6 ' + why)
        if not flow.get('folder_id'):
            probs.append('P8 flow %s has no n8n folder set in G-02 (04.6 §3.9: new workflows are created in their flow folder)' % flow['id'])
        elif ti.get('folderId') != flow['folder_id']:
            probs.append('P8 folderId must be %s (flow %s folder, 04.6 §3.9)' % (flow['folder_id'], flow['id']))

    # P5 snapshot + Jira record before changing an existing workflow
    if kind in ('update', 'publish', 'state'):
        if cur is None:
            probs.append('P5 no get_workflow_details of %s after its last write: read the current config first' % wid)
        else:
            vid = cur.get('versionId')
            snap = os.path.join(N.ROOT, C['snapshot_dir'], wid, '%s.json' % vid)
            try:
                with open(snap, encoding='utf-8') as f:
                    same = json.load(f) == cur
            except (OSError, ValueError):
                same = None
            if same is None:
                probs.append('P5 snapshot %s missing (save the get_workflow_details "workflow" object there)' % N.rel(snap))
            elif not same:
                probs.append('P5 snapshot %s differs from the latest get_workflow_details result' % N.rel(snap))
            d = latest_details(tr, C, wid, before_seq, after_seq=last_w)
            need = [wid, vid]
            for o in ops:
                t = o.get('type')
                nd = node_of(o.get('nodeName'))
                if t == 'setNodeParameter' and nd is not None:
                    old = pointer_get(nd.get('parameters') or {}, o.get('path') or '')
                    if old is not None:
                        need.append(as_text(old))
                elif t == 'updateNodeParameters' and nd is not None:
                    for k in (o.get('parameters') or {}):
                        old = (nd.get('parameters') or {}).get(k)
                        if old is not None:
                            need.append(as_text(old))
                elif t in ('removeNode', 'setNodeDisabled', 'setNodeSettings', 'setNodeCredential'):
                    need.append(o.get('nodeName') or '')
                elif t == 'renameNode':
                    need.append(o.get('oldName') or '')
            need = [x for x in need if x]
            good = [c for c in jira_comments(tr, C, flow['feature'], before_seq, d.seq)
                    if all(N.norm(x) in comment_text(c) for x in need)]
            if not good:
                probs.append('P5 no Jira comment on %s after the latest read of %s that records workflow id, versionId %s '
                             'and the old value of everything this call changes (07.06.1 D5, owner chose strict)'
                             % (flow['feature'], wid, vid))

    # P7 publish
    if kind == 'publish':
        vol = flow.get('registry_volume')
        for p in [flow['registry_main']] + ([vol] if vol else []):
            c, why = page_read(tr, L, C, p, now, before_seq, after_seq=last_w)
            if why:
                probs.append('P7 ' + why)
            elif wid not in N.readable(c):
                probs.append('P7 %s is not registered on page %s (04.9 先登记后启用)' % (wid, p))
        if not vol:
            probs.append('P7 flow %s has no 04.9 volume set in G-02' % flow['id'])
        if cur is not None and (cur.get('settings') or {}).get('errorWorkflow') != C['error_workflow_id']:
            probs.append('P7 settings.errorWorkflow is not %s (04.6 §3.5 层一)' % C['error_workflow_id'])
    return probs


# ---------------------------------------------------------------- Stop

def passing_drafts_containing(tr, L, needles):
    import gate_check as G
    for p, lg in _ledgers():
        if lg.get('kind') != 'draft':
            continue
        path = os.path.join(N.ROOT, (lg.get('target') or {}).get('path') or '')
        try:
            with open(path, encoding='utf-8') as f:
                text = N.norm(f.read())
        except OSError:
            continue
        if all(N.norm(x) in text for x in needles):
            R, _ = G.evaluate(lg, tr, L=L)
            if R.ok:
                return N.rel(path)
    return None


def _ledgers():
    from _common import ledgers
    return ledgers()


def check_stop(tr, L, now=None):
    C = cfg()
    now = now or N.now_utc()
    since = N.parse_ts(C['effective_from'])
    probs = []
    wids = []
    created = set()
    for c in tr.ordered():
        if c.name in write_tools(C) and kind_of(C, c.name) != 'run' and write_ok(c):
            t = N.parse_ts(c.ts)
            if not t or t < since:
                continue
            w = written_id(c, C)
            if w and w not in wids:
                wids.append(w)
            if kind_of(C, c.name) == 'create' and w:
                created.add(w)
    for wid in wids:
        last = writes_to(tr, C, wid, INF, since)[-1]
        name = workflow_name(tr, C, wid, INF)
        flow = flow_for_name(C, name)
        d = latest_details(tr, C, wid, INF, after_seq=last.seq)
        if not d:
            probs.append('G-02 S0 %s: no get_workflow_details after the last write (read-back, 07.06 §6.1-3)' % wid)
            continue
        vid = result_json(d)['workflow'].get('versionId')
        if not flow:
            probs.append('G-02 %s (%s) matches no flow in G-02' % (wid, name))
            continue
        if not any(N.norm(wid) in comment_text(c) and N.norm(vid) in comment_text(c)
                   for c in jira_comments(tr, C, flow['feature'], INF, last.seq)):
            if not passing_drafts_containing(tr, L, [wid, vid]):
                probs.append('G-02 S1 %s: no task-record comment on %s with the id and versionId %s, and no passing draft '
                             'of one (07.06.1 §六-1)' % (wid, flow['feature'], vid))
        if wid in created:
            c9, _ = page_read(tr, L, C, flow['registry_main'], now, INF, after_seq=last.seq, check_age=False)
            if not (c9 and wid in N.readable(c9)) and not passing_drafts_containing(tr, L, [wid, '04.9']):
                probs.append('G-02 S2 %s: not in 04.9 and no passing draft asking for its registration (04.9 §一)' % wid)
        cb, _ = page_read(tr, L, C, flow['build_sheet'], now, INF, after_seq=last.seq, check_age=False)
        if not (cb and wid in N.readable(cb)) and not passing_drafts_containing(tr, L, [wid]):
            probs.append('G-02 S3 %s: not on the build sheet after the last write and no passing draft (07.06 收口三件套)' % wid)
    return probs


def open_items():
    C = cfg()
    return C.get('legacy_open_items') or []
