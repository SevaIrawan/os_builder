#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Adversarial corpus for G-03 (chat-answer gate). Each case builds a small synthetic transcript,
writes one or more answers, and states whether G-03 must hold it (and which token must be named).

Why it exists: 2026-09-25 two G-03 bugs (a ';' inside a quote, a short quote shifting quote pairing)
were found only when real answers were held, not by the tests. Every check (T1-T4), every token kind,
every outside system and every known edge case gets at least one case that must be held and one that
must pass. Usage: python3 scripts/g03_selftest.py   (exit 0 = all expectations met)"""
import json, os, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'hooks'))
import g03                                    # noqa: E402

FAILS = []
TMP = tempfile.mkdtemp(prefix='g03-')
MARK = '\U0001F532'


class T:
    def __init__(self, owner='cek status'):
        self.lines, self.n = [], 0
        self.owner(owner)

    def owner(self, text):
        self.lines.append({'type': 'user', 'origin': {'kind': 'human'}, 'message': {'content': text}})

    def call(self, name, inp, result):
        self.n += 1
        tid = 'toolu_C%04d' % self.n
        self.lines.append({'type': 'assistant', 'message': {'content': [{'type': 'tool_use', 'id': tid, 'name': name, 'input': inp}]}})
        txt = result if isinstance(result, str) else json.dumps(result, ensure_ascii=False)
        self.lines.append({'type': 'user', 'message': {'content': [{'type': 'tool_result', 'tool_use_id': tid,
                                                                     'content': [{'type': 'text', 'text': txt}]}]}})

    def hook_note(self, text):
        self.lines.append({'type': 'attachment', 'attachment': {'content': text}})

    def say(self, text):
        self.lines.append({'type': 'assistant', 'message': {'content': [{'type': 'text', 'text': text}]}})

    def run(self):
        p = os.path.join(TMP, 't.jsonl')
        with open(p, 'w', encoding='utf-8') as f:
            for d in self.lines:
                f.write(json.dumps(d, ensure_ascii=False) + '\n')
        return g03.check_turn(p)


def base():
    t = T('cek branch claude/x dan halaman')
    t.call('Bash', {'command': 'git log --oneline -3'}, '22bdede Rebuild repo docs\n')
    t.call('mcp__github__list_branches', {'owner': 'o', 'repo': 'r'}, '[{"name":"main","sha":"6e217b41e848814b"}]')
    t.call('Bash', {'command': 'git ls-remote origin main'}, 'dd14bb1d2316abc26bb1\trefs/heads/main\n')
    t.call('mcp__Atlassian_MCP__getConfluenceContent', {'content_id': '1234567890', 'detail': 'summary'},
           {'data': {'id': '1234567890', 'title': '04.9｜登记表', 'snapshotToken': 'v:7',
                     'body': {'value': 'PIP Extension 参数 共 6 个字段；n8n 17 条，N20 37 条'},
                     'metadata': {'version': {'number': 7}}}})
    t.call('mcp__Atlassian_MCP__executeRead', {'name': 'listJiraIssueComments', 'inputs': {'issueIdOrKey': 'OSD-116'}},
           {'data': {'startAt': 0, 'isLast': True, 'comments': [{'id': '50237', 'body': 'PIP 参数 共 8 个字段'}]}})
    t.call('mcp__n8n__get_workflow_details', {'workflowId': 'AbCdEfGh12345678'},
           {'workflow': {'id': 'AbCdEfGh12345678', 'description': 'see NSE-1137 c50494'}})
    t.call('Read', {'file_path': '/r/scripts/x.py'}, '     1\timport os\n     2\tprint(1)\n')
    return t


def case(name, answers, held_token=None, setup=None):
    """held_token=None: must pass. Otherwise: must be held and name held_token."""
    t = base()
    if setup:
        setup(t)
    for a in answers:
        if isinstance(a, tuple) and a[0] == 'owner':
            t.owner(a[1])
        else:
            t.say(a)
    probs = t.run()
    if held_token is None:
        ok = probs == []
    else:
        ok = any(held_token in p for p in probs)
    print('%-4s %s%s' % ('ok' if ok else 'FAIL', name, '' if ok else '   <- %s' % probs))
    if not ok:
        FAILS.append(name)


# ---------------- T1: every token kind, invented vs present
case('T1 commit invented', ['Commit lokal abc1234.'], 'abc1234')
case('T1 commit present (local, non-GitHub sentence)', ['Commit lokal 22bdede.'])
case('T1 pageId invented', ['Page 9876543210 dibaca.'], '9876543210')
case('T1 issue key invented', ['Tiket NSE-9999 dibaca.'], 'NSE-9999')
case('T1 issue key present', ['Tiket OSD-116 dibaca.'])
case('T1 comment id invented', ['Catatan c99999 dibaca.'], 'c99999')
case('T1 version invented', ['Sekarang v99.'], 'v99')
case('T1 version present as v:7', ['Sekarang v7.'])
case('T1 date invented', ['Tanggal 2026-01-01.'], '2026-01-01')
case('T1 workflow id invented', ['Id ZzZzZzZz12345678.'], 'ZzZzZzZz12345678')
case('T1 number invented', ['Jumlahnya 4242.'], '4242')
case('T1 decimal invented', ['Pasal 3.9 berlaku.'], '3.9')
case('T1 number present', ['Jumlahnya 37.'])
case('T1 code invented', ['Lihat `scripts/nope.py`.'], 'scripts/nope.py')
case('T1 code = path a call was given', ['Lihat `x.py`.'])
case('T1 code = tool name called', ['Tool `mcp__n8n__get_workflow_details` dipakai.'])
case('T1 line ref shown by Read', ['Lihat `x.py:2`.'])
case('T1 line ref never shown', ['Lihat `x.py:9`.'], 'x.py:9')
case('T1 key=value a call was given', ['Dibaca dengan `detail=summary`.'])
case('T1 key=value never used', ['Dibaca dengan `detail=outline`.'], 'detail=outline')
case('T1 verbatim quote', ['Isinya "PIP Extension 参数 共 6 个字段".'])
case('T1 paraphrase in quote marks', ['Isinya "PIP Extension 参数有六个字段".'], 'PIP Extension 参数有六个字段')
case('T1 curly quote verbatim', ['Isinya “PIP Extension 参数”.'])
case('T1 corner quote = page title', ['Halaman 「04.9｜登记表」.'])
case('T1 corner quote invented', ['Halaman 「04.9｜总表」.'], '04.9｜总表')
case('T1 token inside bold', ['Versi **v7** dibaca.'])
case('T1 token inside a table row', ['| 1234567890 | v7 |'])
case('T1 invented token inside a table row', ['| 1234567890 | v8 |'], 'v8')
case('T1 token seen only in a hook message', ['Workflow QwErTy12345678Ab masih terbuka.'], 'QwErTy12345678Ab',
     setup=lambda t: t.hook_note('QwErTy12345678Ab: open item'))
case('T1 token seen only in my own earlier text', ['Id QwErTy12345678Ab.', ('owner', 'lanjut'), 'Id QwErTy12345678Ab lagi.'],
     'QwErTy12345678Ab')
case('T1 token the owner wrote', ['Branch `claude/x` dicek.'])

# ---------------- T2: outside systems need a live read of that system
case('T2 GitHub fact from a stale local ref', ['Branch main di GitHub ada di 22bdede.'], '22bdede')
case('T2 GitHub fact from mcp__github__', ['Di GitHub main ada di 6e217b4.'])
case('T2 GitHub fact from git ls-remote', ['Di GitHub main ada di dd14bb1.'])
case('T2 GitHub file claim without a GitHub read', ['File `LICENSE` ada di GitHub.'], 'LICENSE',
     setup=lambda t: t.call('Bash', {'command': 'ls'}, 'LICENSE\n'))
case('T2 Confluence version from Confluence', ['Halaman 1234567890 di v7.'])
case('T2 Confluence version from a repo note', ['Halaman 1234567890 di v12.'], 'v12',
     setup=lambda t: t.call('Bash', {'command': 'cat docs/source-versions.md'}, '| x | 1234567890 | v12 |'))
case('T2 Jira comment read from Jira', ['Komentar c50237 di Jira.'])
case('T2 Jira comment known only from n8n', ['Komentar c50494 ada di Jira.'], 'c50494')
case('T2 n8n workflow from n8n', ['Workflow AbCdEfGh12345678 di n8n.'])
case('T2 n8n workflow known only from a file', ['Workflow XyXyXyXy12345678 di n8n.'], 'XyXyXyXy12345678',
     setup=lambda t: t.call('Read', {'file_path': '/r/g02.json'}, '     1\tXyXyXyXy12345678\n'))

# ---------------- T3: absence wording
case('T3 bare absence', ['Tidak ada commit lama di situ.'], 'tidak ada')
case('T3 absence marked unverified', ['Tidak ada commit lama di situ %s.' % MARK])
case('T3 absence with a verified id', ['Di 1234567890 v7 tidak ada perubahan.'])
case('T3 absence with only a number', ['Tidak ada 37 perubahan.'], 'tidak ada')
case('T3 "sebelum ada" is not absence', ['Sebelum ada izin, saya menunggu.'])
case('T3 English absence', ['The branch was not found.'], 'not found')
case('T3 Chinese absence', ['该字段没有登记。'], '没有')
case('T3 kosong', ['Status git kosong.'], 'kosong')

# ---------------- T4: correction after a hold
case('T4 correction restating the token releases', ['Commit abc1234 dibuat.', 'Koreksi: abc1234 belum dicek %s.' % MARK])
case('T4 correction not restating keeps the hold', ['Commit abc1234 dibuat.', 'Koreksi: maaf.'], 'abc1234')
case('T4 correction with its own error keeps the hold', ['Commit abc1234 dibuat.', 'Koreksi: abc1234 ada di v55.'], 'abc1234')
case('T4 absence correction restating the phrase', ['Tidak ada commit lama.', 'Koreksi: tidak ada commit lama %s.' % MARK])
case('T4 new owner message starts a new turn', ['Commit abc1234 dibuat.', ('owner', 'ok'), 'Siap.'])

# ---------------- skips and sentence splitting
case('fenced code is skipped', ['Jalankan:\n```\ngit reset --hard deadbee1\n```'])
case('sentence with the unverified marker is skipped', ['Commit abc1234 %s.' % MARK])
case('; inside a verbatim quote does not split it', ['Isinya "PIP Extension 参数 共 6 个字段；n8n 17 条，N20 37 条".'])
case('a short quote does not shift quote pairing', ['Kata "n8n" ada di 17 komentar dan "N20" di 37 komentar.'])
case('one bad sentence among good ones', ['Versi v7. Versi v98.'], 'v98')
case('bad token in the second sentence of a bullet', ['- Halaman v7 dibaca. Commit abc1234 dibuat.'], 'abc1234')

print('-' * 60)
print('G03 SELFTEST: %s' % ('ALL EXPECTATIONS MET' if not FAILS else 'FAILED: %d' % len(FAILS)))
sys.exit(1 if FAILS else 0)
