#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stop hook. The turn cannot end while:
  1. a draft file (lexicon draft_path_patterns) changed since it last passed and its ledger does not pass G-01;
  2. an outbound write succeeded and no later read of the target contains every sentence that was sent;
  3. (G-02) an n8n workflow written this session lacks its read-back, task record or registration;
  3b. (G-01 session_start) the owner opened with "hi" and a session-start step has not run since;
  4. (G-03) the answer of this turn carries a token, quote or absence claim no source shows.
Exit 2 = keep working (stderr is shown to Claude). Exit 0 = may stop."""
import json, os, re, sys
from _common import N, read_input, transcript, deny, append_log, read_log, ledgers, REGISTRY, latest_owner_text
import _guard
import gate_check


def draft_files(L):
    out = []
    for base, _, files in os.walk(os.path.join(N.ROOT, 'docs')):
        for fn in files:
            p = os.path.join(base, fn)
            if N.is_draft_path(p, L):
                out.append(p)
    return sorted(out)


def file_sha(p):
    with open(p, encoding='utf-8', errors='replace') as f:
        return N.text_sha(f.read())


def readback_text(c, system):
    """What a read-back shows. For Confluence the page read also carries the version message
    (metadata.version.message), which a write's versionMessage lands in; it is not part of
    N.readable(), so it is added here."""
    txt = N.readable(c)
    if system == 'confluence':
        j = c.json()
        data = j.get('data', j) if isinstance(j, dict) else {}
        msg = (((data.get('metadata') or {}).get('version') or {}).get('message')) if isinstance(data, dict) else None
        if msg:
            txt += '\n' + msg
    return txt


def load_registry():
    try:
        with open(REGISTRY, encoding='utf-8') as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def main(inp=None):
    inp = read_input() if inp is None else inp
    L = N.lexicon()
    tr = None
    problems = []

    # 0. gate files changed outside the hooks (e.g. by a background program) are put back
    put_back = _guard.enforce(L, lambda tok: tok in latest_owner_text(transcript(inp)))
    if put_back:
        problems.append(_guard.message(put_back, L))

    # 1. drafts
    reg = load_registry()
    changed = [p for p in draft_files(L) if reg.get(N.rel(p), {}).get('sha') != file_sha(p)]
    if changed:
        tr = transcript(inp)
        lgs = ledgers()
        for p in changed:
            r = N.rel(p)
            mine = [(lp, lg) for lp, lg in lgs if lg.get('kind') == 'draft' and (lg.get('target') or {}).get('path') == r]
            if not mine:
                problems.append('draft %s changed but no ledger (kind=draft, target.path=%s) exists' % (r, r)); continue
            lp, lg = max(mine, key=lambda x: os.path.getmtime(x[0]))
            R, _ = gate_check.evaluate(lg, tr, L=L)
            if R.ok:
                reg[r] = {'sha': file_sha(p), 'write_id': lg.get('write_id'), 'passed_at': N.now_utc().isoformat()}
            else:
                problems.append('draft %s fails G-01 (%s):\n%s' % (r, N.rel(lp), gate_check.render(R, lg)))
        with open(REGISTRY, 'w', encoding='utf-8') as f:
            json.dump(reg, f, ensure_ascii=False, indent=1, sort_keys=True)
        _guard.seal(L, only=[N.rel(REGISTRY)])

    # 2. read-back after outbound writes
    log = read_log()
    done = {e.get('payload_sha') for e in log if e.get('event') == 'read_back'}
    # G-05 records its used orders in the same log; those writes have no ledger payload to read back
    pending = [e for e in log if e.get('event') == 'consumed' and e.get('gate') != 'G-05' and e.get('payload_sha') not in done]
    if pending:
        tr = tr or transcript(inp)
        override = L['order_words']['override_token'] in latest_owner_text(tr)
        for e in pending:
            wf = os.path.join(N.ROOT, 'docs', 'ledger', '_writes', e['payload_sha'] + '.json')
            if not os.path.exists(wf):
                problems.append('write %s: payload copy missing (%s)' % (e['payload_sha'], N.rel(wf))); continue
            with open(wf, encoding='utf-8') as f:
                w = json.load(f)
            segs = N.segments(gate_check.payload_text(w['tool'], w['input']))
            system, tid = e['target'].split(':', 1)
            canon = json.dumps(w['input'], sort_keys=True, ensure_ascii=False)
            wcalls = [c for c in tr.ordered() if c.name == w['tool'] and json.dumps(c.input, sort_keys=True, ensure_ascii=False) == canon]
            at = N.parse_ts(e['at'])

            def after_write(c):
                if wcalls:
                    return c.seq > wcalls[-1].seq
                t = N.parse_ts(c.ts)
                return bool(t and t > at)
            reads = []
            for c in tr.ordered():
                if c.is_error or not after_write(c):
                    continue
                if system == 'confluence' and N.call_content_id(c) == tid and N.is_full_page_read(c, L):
                    reads.append(c)
                if system == 'jira_comment' and (
                        (c.name == L['tools']['execute_read'] and c.input.get('name') == 'listJiraIssueComments'
                         and (c.input.get('inputs') or {}).get('issueIdOrKey') == tid) or
                        (c.name in L['tools']['jira_issue_read'] and c.input.get('issueIdOrKey') == tid)):
                    reads.append(c)
                if system == 'slack' and c.name.startswith('mcp__Slack__slack_read_'):
                    reads.append(c)
            if not reads:
                problems.append('write to %s at %s has not been read back. Read the target again in full.' % (e['target'], e['at'])); continue
            text = N.norm('\n'.join(readback_text(c, system) for c in reads))
            missing = [raw[:60] for raw, n in segs if n not in text]
            if missing and not override:
                problems.append('read-back of %s is missing %d sentence(s) that were sent: %s' % (e['target'], len(missing), missing[:5]))
                continue
            append_log({'event': 'read_back', 'payload_sha': e['payload_sha'], 'target': e['target'],
                        'read_calls': [c.id for c in reads], 'missing': missing})

    # 3. G-02: every n8n workflow written since G-02 took effect is read back, recorded and registered
    import g02
    tr = tr or transcript(inp)
    if g02.cfg()['override_token'] not in latest_owner_text(tr):
        problems.extend(g02.check_stop(tr, L))

    # 3b. session start on "hi" (working-agreement rule 23; G-01 "session_start")
    import s0
    if L['order_words']['override_token'] not in latest_owner_text(tr):
        problems.extend('G-01 session start (owner said "hi") %s' % p for p in s0.check(tr, L))

    # 4. G-03: every checkable token in this turn's answer comes from a source (.claude/gates/G-03-chat-claims.json)
    import g03
    C3 = g03.cfg()
    try:
        held = g03.check_turn(tr.path, inp.get('last_assistant_message'), C3)
    except Exception as e:                       # fail closed: an unchecked answer is not let through
        held = ['G-03 could not run (%s: %s). Fix it, or the owner types %s' % (type(e).__name__, e, C3['override_token'])]
    if held and C3['override_token'] in latest_owner_text(tr):
        held = []
    if held:
        problems.extend(held)
        problems.append('G-03: the answer above is held. Write a new message that starts with "%s", restates each '
                        'held token or absence phrase either verified (read the source now) or marked %s, then stop again.'
                        % (C3['correction_prefix'], C3['unverified_marker']))

    if problems:
        deny('G-01/G-02/G-03 Stop check - you may not end the turn yet:\n- ' + '\n- '.join(problems))
    return 0


def owner_override(path):
    """The owner's latest real message holds OVERRIDE G-01 / G-03. Read without nosm_lib, which may be what broke."""
    last = ''
    try:
        with open(path, encoding='utf-8') as f:
            for line in f:
                try:
                    d = json.loads(line)
                except ValueError:
                    continue
                if d.get('type') == 'user' and (d.get('origin') or {}).get('kind') == 'human' and not d.get('isMeta'):
                    c = (d.get('message') or {}).get('content')
                    last = c if isinstance(c, str) else ' '.join(
                        b.get('text', '') for b in c or [] if isinstance(b, dict) and b.get('type') == 'text')
    except (OSError, TypeError):
        return False
    return 'OVERRIDE G-01' in last or 'OVERRIDE G-03' in last


if __name__ == '__main__':
    # Fail closed (2026-09-25): a Stop hook that crashes exits 1 and the turn ends unchecked. Hold it instead,
    # unless the owner's latest message overrides.
    INP = read_input()
    try:
        sys.exit(main(INP))
    except SystemExit as e:
        if e.code in (0, 2, None):
            raise
        err = str(e.code)
    except Exception as e:                      # noqa: BLE001 - any failure of the gate itself
        err = '%s: %s' % (type(e).__name__, e)
    if owner_override(INP.get('transcript_path') or ''):
        sys.exit(0)
    deny('G-01/G-03: the Stop hook failed (%s), so this turn cannot be checked and is held. Fix the hook '
         '(owner: UNLOCK G-01), or the owner types OVERRIDE G-03.' % err)
