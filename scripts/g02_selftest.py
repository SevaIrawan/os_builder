#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""G-02 self-test.
Part A replays the real n8n writes of 2026-09-23/24 against the session transcript as it was at
that moment: every check must catch what the audit of 2026-09-25 found.
Part B runs synthetic transcripts: each check must block the bad case and let the good case through.
Exit 0 only when every expectation is met."""
import copy, json, os, shutil, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'hooks'))
sys.path.insert(0, HERE)
import nosm_lib as N          # noqa: E402
import g02                    # noqa: E402

L = N.lexicon()
FAIL = []


def expect(label, probs, want, absent=()):
    got = ' | '.join(probs)
    ok = all(any(p.startswith(w) or (' %s ' % w) in (' ' + p) for p in probs) for w in want) \
        and not any(any(p.startswith(a) for p in probs) for a in absent)
    print('%s %s%s' % ('ok  ' if ok else 'FAIL', label, '' if ok else '\n     got: %s' % got[:900]))
    if not ok:
        FAIL.append(label)


# ------------------------------------------------------------------ Part A: replay
def part_a():
    path = os.environ.get('G02_REPLAY_TRANSCRIPT') or N.find_transcript()
    tr = N.Transcript(path)
    cases = [
        ('A1 N05 create 09-23 (07.06.1 only read as summary; no volume; no folder)', 'toolu_01NQpNcAysSvAp4baTuApBKu', ['P1', 'P6', 'P8'], ['P2']),
        ('A2 N20 create 09-24 (07 / 07.06.1 not read that day; no volume; no folder)', 'toolu_01D8q7bxCHZ5Lf1c3MenCKHe', ['P1', 'P6', 'P8'], ['P2']),
        ('A3 N05 setNodeCredential via API 09-24 (07.06.1 E5)', 'toolu_01LPnCJLs18Gx8jp3UERRvPn', ['P4'], []),
        ('A4 N20 wiring update 13:51 (no snapshot, no Jira record)', 'toolu_018JXrVN4yt2tScgRYYJFJEb', ['P5'], ['P2']),
        ('A5 N20 marker update 14:17 (no snapshot, no Jira record)', 'toolu_01VVR2WjZEN9fJNHkeo6P2Bv', ['P5'], ['P2']),
    ]
    for label, cid, want, absent in cases:
        c = tr.calls.get(cid)
        if not c:
            print('skip %s (call not in this transcript)' % label)
            continue
        probs = g02.check_pre(c.name, c.input, tr, L, now=N.parse_ts(c.ts), before_seq=c.seq)
        expect(label, probs, want, absent)
    # C5 tightening: an END marker alone is not a read
    for label, cid, want in [('A6 v44 page printed part by part counts as read', 'toolu_01FbovSo7LxUR38H6e6idpQS', True),
                             ('A7 comments "read" with | tail -1 do not count', 'toolu_01A6zPUXCMUTsxShF5NRerHM', False)]:
        c = tr.calls.get(cid)
        if not c:
            print('skip %s' % label); continue
        ok, why = N.fully_read(tr, c)
        good = ok is want
        print('%s %s (%s)' % ('ok  ' if good else 'FAIL', label, why))
        if not good:
            FAIL.append(label)
    # nothing written since G-02 took effect: the Stop check must not fire on old work
    expect('A8 Stop does not fire on work before effective_from', g02.check_stop(tr, L), [], ['G-02'])


# ------------------------------------------------------------------ Part B: synthetic
class T:
    """Writes a synthetic transcript in the harness JSONL shape."""
    def __init__(self):
        self.lines, self.n, self.t = [], 0, 0

    def ts(self):
        self.t += 1
        return '2099-01-01T00:%02d:%02dZ' % (self.t // 60, self.t % 60)

    def call(self, name, inp, result, is_error=False):
        self.n += 1
        cid = 'toolu_syn%04d' % self.n
        self.lines.append({'type': 'assistant', 'timestamp': self.ts(),
                           'message': {'content': [{'type': 'tool_use', 'id': cid, 'name': name, 'input': inp}]}})
        self.lines.append({'type': 'user', 'timestamp': self.ts(),
                           'message': {'content': [{'type': 'tool_result', 'tool_use_id': cid, 'is_error': is_error,
                                                    'content': result if isinstance(result, str) else json.dumps(result, ensure_ascii=False)}]}})
        return cid

    def page(self, pid, body='x', v=5):
        return self.call('mcp__Atlassian_MCP__getConfluenceContent',
                         {'cloudId': 'c', 'content_id': pid, 'detail': 'full', 'content_format': 'markdown'},
                         {'data': {'id': pid, 'title': 't', 'snapshotToken': 'v:%d' % v, 'body': {'format': 'markdown', 'value': body},
                                   'metadata': {'version': {'number': v}}}})

    def load(self):
        f = tempfile.NamedTemporaryFile('w', suffix='.jsonl', delete=False, encoding='utf-8')
        for d in self.lines:
            f.write(json.dumps(d, ensure_ascii=False) + '\n')
        f.close()
        tr = N.Transcript(f.name)
        os.unlink(f.name)
        return tr


WID = 'G02SELFTESTWF01'
OLD_CODE = "const a = 1;\nreturn [{ json: { a } }];"
WF = {'id': WID, 'name': '纪律与绩效改进处置｜N99｜G02 selftest', 'versionId': 'ver-old-1', 'active': False,
      'settings': {'executionOrder': 'v1'},
      'nodes': [
          {'name': 'C1', 'type': 'n8n-nodes-base.code', 'parameters': {'jsCode': OLD_CODE}},
          {'name': 'H1', 'type': 'n8n-nodes-base.httpRequest', 'parameters': {'method': 'POST', 'url': 'https://x'}},
          {'name': 'J1', 'type': 'n8n-nodes-base.jira', 'parameters': {'resource': 'issue', 'operation': 'get'}}]}


def base(C, with_comment=True, comment_extra='', wf=None):
    t = T()
    t.call('mcp__n8n__get_workflow_details', {'workflowId': WID}, {'workflow': wf or WF})
    for r in C['required_reads']:
        t.page(r['page'])
    flow = C['flows'][0]
    t.page(flow['spec']); t.page(flow['build_sheet'])
    if with_comment:
        body = '<p>%s %s old: %s %s</p>' % (WID, (wf or WF)['versionId'], OLD_CODE, comment_extra)
        t.call('mcp__Atlassian_MCP__addOrEditJiraIssueComment', {'cloudId': 'c', 'issueIdOrKey': flow['feature'], 'commentBody': body},
               {'data': {'message': 'Comment added to %s successfully' % flow['feature'], 'commentId': '1'}})
    return t


def snapshot(C, wf):
    d = os.path.join(N.ROOT, C['snapshot_dir'], WID)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, '%s.json' % wf['versionId']), 'w', encoding='utf-8') as f:
        json.dump(wf, f, ensure_ascii=False)


def upd(ops):
    return ('mcp__n8n__update_workflow', {'workflowId': WID, 'operations': ops})


def part_b():
    C = g02.cfg()
    now = N.parse_ts('2099-01-01T01:00:00Z')
    snapdir = os.path.join(N.ROOT, C['snapshot_dir'], WID)
    try:
        snapshot(C, WF)
        tr = base(C).load()
        good = upd([{'type': 'setNodeParameter', 'nodeName': 'C1', 'path': '/jsCode',
                     'value': "const url = 'https://x//y';\nconst re = /a\\/\\/b/;\n// own-line comment\nreturn [{ json: { url, ok: re.test('a//b') } }];"}])
        expect('B1 good update with snapshot, reads and Jira record passes', g02.check_pre(*good, tr, L, now=now), [], ['P'])
        bad = upd([{'type': 'setNodeParameter', 'nodeName': 'C1', 'path': '/jsCode', 'value': 'return [{ json: { a: 1 } ];'}])
        expect('B2 syntax error blocked (P2)', g02.check_pre(*bad, tr, L, now=now), ['P2'])
        tc = upd([{'type': 'setNodeParameter', 'nodeName': 'C1', 'path': '/jsCode', 'value': 'const a = 1; // trailing\nreturn [];'}])
        expect('B3 trailing // comment blocked (P2)', g02.check_pre(*tc, tr, L, now=now), ['P2'])
        add = upd([{'type': 'addNode', 'node': {'name': 'C2', 'type': 'n8n-nodes-base.code', 'typeVersion': 2,
                                                'parameters': {'jsCode': 'return [{ json: {} ];'}}}])
        expect('B4 syntax error in addNode blocked (P2)', g02.check_pre(*add, tr, L, now=now), ['P2'])
        r1 = upd([{'type': 'setNodeSettings', 'nodeName': 'H1', 'settings': {'retryOnFail': True}}])
        tr_h = base(C, comment_extra='H1').load()
        expect('B5 retryOnFail on POST blocked (P3)', g02.check_pre(*r1, tr_h, L, now=now), ['P3'])
        r2 = upd([{'type': 'setNodeSettings', 'nodeName': 'J1', 'settings': {'retryOnFail': True}}])
        tr_j = base(C, comment_extra='J1').load()
        expect('B6 retryOnFail on Jira get allowed', g02.check_pre(*r2, tr_j, L, now=now), [], ['P3'])
        cr = upd([{'type': 'setNodeCredential', 'nodeName': 'H1', 'credentialKey': 'jiraSoftwareCloudApi', 'credentialId': 'x', 'credentialName': 'Bot'}])
        expect('B7 credential on httpRequest via API blocked (P4)', g02.check_pre(*cr, tr_h, L, now=now), ['P4'])
        tr_nc = base(C, with_comment=False).load()
        expect('B8 no Jira record before change blocked (P5)', g02.check_pre(*good, tr_nc, L, now=now), ['P5'])
        tr_wrong = base(C, with_comment=True).load()
        other = upd([{'type': 'setNodeParameter', 'nodeName': 'H1', 'path': '/url', 'value': 'https://y'}])
        tr_url = base(C, comment_extra='').load()
        expect('B9 Jira record lacking the old value being replaced blocked (P5)',
               g02.check_pre(*other, tr_url, L, now=now), ['P5'])
        wf2 = copy.deepcopy(WF); wf2['name'] = 'changed'
        snapshot(C, wf2)
        expect('B10 snapshot differing from the latest read blocked (P5)', g02.check_pre(*good, tr_wrong, L, now=now), ['P5'])
        snapshot(C, WF)
        late = N.parse_ts('2099-01-02T12:00:00Z')
        expect('B11 rule pages read more than 12 h ago blocked (P1)', g02.check_pre(*good, tr, L, now=late), ['P1'])
        t = base(C); t.page(C['required_reads'][2]['page'], v=6); t.page(C['required_reads'][2]['page'], v=5)
        expect('B12 page read at an older version than one seen blocked (P1)', g02.check_pre(*good, t.load(), L, now=now), ['P1'])

        # create: S-05 has no volume / folder yet
        code = ("import { workflow, node, trigger } from '@n8n/workflow-sdk';\n"
                "const c = node({ type: 'n8n-nodes-base.code', version: 2, config: { name: 'C', parameters: { jsCode: `return [];` } } });\n"
                "export default workflow('x', '纪律与绩效改进处置｜N98｜t').add(c);")
        cr_in = ('mcp__n8n__create_workflow_from_code', {'code': code, 'name': '纪律与绩效改进处置｜N98｜t'})
        expect('B13 create for a flow without 04.9 volume / folder blocked (P6, P8)', g02.check_pre(*cr_in, tr, L, now=now), ['P6', 'P8'], ['P2'])
        orig = g02.cfg
        C2 = copy.deepcopy(C); C2['flows'][0]['registry_volume'] = '9990001'; C2['flows'][0]['folder_id'] = 'FOLDER1'
        g02.cfg = lambda: C2
        try:
            t = base(C2); t.page('9990001')
            tv = t.load()
            ok_in = ('mcp__n8n__create_workflow_from_code', dict(cr_in[1], folderId='FOLDER1'))
            expect('B14 create with volume read and right folder passes', g02.check_pre(*ok_in, tv, L, now=now), [], ['P'])
            expect('B15 create in the wrong folder blocked (P8)', g02.check_pre(*cr_in, tv, L, now=now), ['P8'], ['P6'])
            badcode = ('mcp__n8n__create_workflow_from_code', dict(ok_in[1], code=code.replace('return [];', 'return [;')))
            expect('B16 create with a Code node syntax error blocked (P2)', g02.check_pre(*badcode, tv, L, now=now), ['P2'])
            retry_code = code.replace("config: { name: 'C'", "config: { name: 'C'").replace(
                "export default", "const h = node({ type: 'n8n-nodes-base.httpRequest', version: 4, config: { name: 'H', retryOnFail: true, parameters: { method: 'POST', url: 'https://x' } } });\nexport default")
            rc = ('mcp__n8n__create_workflow_from_code', dict(ok_in[1], code=retry_code))
            expect('B17 create with retryOnFail on a POST node blocked (P3)', g02.check_pre(*rc, tv, L, now=now), ['P3'])
            # publish
            pub = ('mcp__n8n__publish_workflow', {'workflowId': WID})
            t = base(C2); t.page('1693089805', body='index without the id'); t.page('9990001', body='vol')
            expect('B18 publish of an unregistered workflow blocked (P7)', g02.check_pre(*pub, t.load(), L, now=now), ['P7'])
            wfe = copy.deepcopy(WF); wfe['settings']['errorWorkflow'] = C2['error_workflow_id']
            snapshot(C2, wfe)
            t = base(C2, wf=wfe); t.page('1693089805', body='row %s' % WID); t.page('9990001', body='block %s' % WID)
            expect('B19 publish registered + errorWorkflow set passes', g02.check_pre(*pub, t.load(), L, now=now), [], ['P'])
            snapshot(C2, WF)
            t = base(C2); t.page('1693089805', body='row %s' % WID); t.page('9990001', body='block %s' % WID)
            expect('B20 publish without errorWorkflow blocked (P7)', g02.check_pre(*pub, t.load(), L, now=now), ['P7'])
        finally:
            g02.cfg = orig

        # Stop
        C3 = copy.deepcopy(C); C3['effective_from'] = '2000-01-01T00:00:00Z'
        g02.cfg = lambda: C3
        try:
            t = base(C3, with_comment=False)
            t.call('mcp__n8n__update_workflow', good[1], {'workflowId': WID, 'nodeCount': 3})
            expect('B21 Stop: write without read-back (S0)', g02.check_stop(t.load(), L, now=now), ['G-02 S0'])
            wf_new = copy.deepcopy(WF); wf_new['versionId'] = 'ver-new-2'
            t.call('mcp__n8n__get_workflow_details', {'workflowId': WID}, {'workflow': wf_new})
            expect('B22 Stop: read back but no task record, not on build sheet (S1, S3)', g02.check_stop(t.load(), L, now=now), ['G-02 S1', 'G-02 S3'])
            flow = C3['flows'][0]
            t.call('mcp__Atlassian_MCP__addOrEditJiraIssueComment', {'cloudId': 'c', 'issueIdOrKey': flow['feature'],
                   'commentBody': 'record %s ver-new-2' % WID}, {'data': {'message': 'Comment added successfully', 'commentId': '2'}})
            t.page(flow['build_sheet'], body='row %s' % WID, v=6)
            expect('B23 Stop: read-back, task record and build sheet row pass', g02.check_stop(t.load(), L, now=now), [], ['G-02'])
            t2 = T()
            t2.call('mcp__n8n__create_workflow_from_code', {'code': 'x', 'name': WF['name']},
                    {'workflowId': WID, 'name': WF['name'], 'nodeCount': 3})
            t2.call('mcp__n8n__get_workflow_details', {'workflowId': WID}, {'workflow': WF})
            t2.call('mcp__Atlassian_MCP__addOrEditJiraIssueComment', {'cloudId': 'c', 'issueIdOrKey': flow['feature'],
                    'commentBody': '%s %s' % (WID, WF['versionId'])}, {'data': {'message': 'Comment added successfully', 'commentId': '3'}})
            t2.page(flow['build_sheet'], body=WID, v=6)
            expect('B24 Stop: created workflow not in 04.9 (S2)', g02.check_stop(t2.load(), L, now=now), ['G-02 S2'])
        finally:
            g02.cfg = orig
    finally:
        shutil.rmtree(snapdir, ignore_errors=True)
        try:
            os.rmdir(os.path.join(N.ROOT, C['snapshot_dir']))
        except OSError:
            pass


if __name__ == '__main__':
    print('--- Part A: replay of 2026-09-23/24')
    part_a()
    print('--- Part B: synthetic cases')
    part_b()
    print('-' * 60)
    print('G02 SELFTEST: %s' % ('ALL EXPECTATIONS MET' if not FAIL else '%d FAILED: %s' % (len(FAIL), FAIL)))
    sys.exit(1 if FAIL else 0)
