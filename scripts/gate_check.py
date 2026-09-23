#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""G-01 Outbound Write Gate — pemeriksa.
Pemakaian: python3 scripts/gate_check.py <ledger.json>
Keluar 0 = PASS (boleh menulis). Keluar 1 = FAIL (dilarang menulis).
Deteksi klaim numerik / klaim-ketiadaan dilakukan OTOMATIS dari teks klaim,
supaya klaim tidak bisa lolos hanya dengan tidak diberi tanda."""
import json, re, sys, datetime

PLACEHOLDER = '\U0001F532'                      # 🔲
FORBIDDEN_SRC = {'', 'self', 'inference', 'asumsi', 'umum', 'ingatan', 'memory', 'n/a', '-'}
# angka + satuan hitung (CJK atau latin)
NUM_RE = re.compile(r'(\d+)\s*(条|行|个|项|处|张|页|次|列|buah|baris|halaman|butir|item)')
ABSENCE_RE = re.compile(r'(tidak ada|belum ada|belum pernah|nol |tanpa satu ?pun|无任何|没有|未见|不存在|零|查不到|未登记|未提及)', re.I)

def load(p):
    with open(p, encoding='utf-8') as f: return json.load(f)

def main(path):
    L = load(path)
    today = datetime.date.today().isoformat()
    res = []                                    # (check_id, ok, detail)
    def add(cid, ok, detail=''): res.append((cid, ok, detail))

    claims  = L.get('claims', [])
    sources = {s['source_id']: s for s in L.get('sources', [])}
    tgt     = L.get('target', {})

    # C1
    add('C1', bool(claims), 'jumlah klaim = %d' % len(claims))

    # C2 / C8
    c2bad, c8bad = [], []
    for c in claims:
        sid   = (c.get('source_id') or '').strip()
        quote = (c.get('quote') or '').strip()
        text  = c.get('text', '')
        is_ph = PLACEHOLDER in text
        if not is_ph and (not sid or not quote):
            c2bad.append('%s: %s' % (c.get('id'), text[:60]))
        if not is_ph and sid.lower() in FORBIDDEN_SRC:
            c8bad.append('%s: source_id=%r' % (c.get('id'), sid))
    add('C2', not c2bad, '; '.join(c2bad) or 'semua klaim faktual bersumber')
    add('C8', not c8bad, '; '.join(c8bad) or 'tidak ada source_id karangan')

    # C3
    c3bad = []
    used = {(c.get('source_id') or '').strip() for c in claims if PLACEHOLDER not in c.get('text','')}
    for sid in sorted(used - {''}):
        s = sources.get(sid)
        if not s:
            c3bad.append('%s: tidak terdaftar di sources[]' % sid); continue
        if s.get('live_version') != s.get('version'):
            c3bad.append('%s: version=%s tapi live_version=%s' % (sid, s.get('version'), s.get('live_version')))
        if s.get('read_at','')[:10] != today:
            c3bad.append('%s: read_at=%s, bukan hari ini (%s)' % (sid, s.get('read_at'), today))
        vo = all(c.get('version_only') for c in claims if c.get('source_id')==sid)
        if s.get('read_scope') != 'full' and not vo:
            c3bad.append('%s: read_scope=%r padahal dipakai untuk klaim faktual' % (sid, s.get('read_scope')))
    add('C3', not c3bad, '; '.join(c3bad) or '%d sumber dibaca penuh & seversi' % len(used - {''}))

    # C4 (auto-deteksi)
    c4bad = []
    for c in claims:
        if PLACEHOLDER in c.get('text',''): continue
        m = NUM_RE.search(c.get('text',''))
        if m:
            n = c.get('numeric') or {}
            if not n.get('count_cmd') or not n.get('count_output'):
                c4bad.append('%s: memuat "%s" tanpa count_cmd/count_output' % (c.get('id'), m.group(0)))
    add('C4', not c4bad, '; '.join(c4bad) or 'semua angka jumlah dihitung mesin')

    # C5 (auto-deteksi)
    c5bad = []
    for c in claims:
        if PLACEHOLDER in c.get('text',''): continue   # placeholder bukan pernyataan faktual
        if ABSENCE_RE.search(c.get('text','')):
            a = c.get('absence') or {}
            if len(a.get('searched') or []) < 2 or not a.get('control_probe'):
                c5bad.append('%s: klaim ketiadaan tanpa searched>=2 + control_probe' % c.get('id'))
    add('C5', not c5bad, '; '.join(c5bad) or 'setiap klaim ketiadaan punya himpunan cari + probe pembanding')

    # C6
    c6bad = [c['id'] for c in claims if PLACEHOLDER not in c.get('text','') and (c.get('near_names') or []) and not (c.get('disambiguation') or '').strip()]
    add('C6', not c6bad, '; '.join(c6bad) or 'nama mirip sudah dibedakan')

    # C7
    ok7 = bool(tgt.get('target_snapshot')) and tgt.get('snapshot_read_at','')[:10] == today
    add('C7', ok7, 'snapshot=%s dibaca %s (hari ini %s)' % (tgt.get('target_snapshot'), tgt.get('snapshot_read_at'), today))

    # C9
    need9 = tgt.get('system') == 'confluence' and tgt.get('method') == 'edits'
    add('C9', (not need9) or bool((L.get('reverse_test') or '').strip()),
        'uji balik: %s' % ('ada' if (L.get('reverse_test') or '').strip() else 'TIDAK ADA'))

    # C10
    add('C10', bool((L.get('user_order') or '').strip()), 'perintah: %r' % (L.get('user_order') or '')[:60])

    # C11 — halaman yang bergerak pada sapuan terakhir wajib sudah dibaca isinya
    c11bad = []
    try:
        sw = load('docs/ledger/_sweep-latest.json')
    except Exception as e:
        sw = None
        c11bad.append('docs/ledger/_sweep-latest.json tidak terbaca (%s)' % e.__class__.__name__)
    if sw is not None:
        if sw.get('swept_at', '')[:10] != today:
            c11bad.append('swept_at=%s, bukan hari ini (%s)' % (sw.get('swept_at'), today))
        moved = {m['source_id']: m for m in sw.get('moved', [])}
        for sid in sorted(used - {''}):
            m = moved.get(sid)
            if m and not m.get('read_after_move'):
                c11bad.append('%s bergerak %s->%s tapi read_after_move=false' % (sid, m.get('from'), m.get('to')))
            if m and m.get('read_after_move') and not (m.get('how') and m.get('read_at')):
                c11bad.append('%s: read_after_move=true tanpa how/read_at' % sid)
    add('C11', not c11bad, '; '.join(c11bad) or 'semua sumber yang bergerak sudah dibaca setelah bergerak')

    gate = load('.claude/gates/G-01-outbound-write.json')
    names = {c['id']: c['name'] for c in gate['checks']}
    print('=' * 66)
    print('G-01 OUTBOUND WRITE GATE — %s' % L.get('write_id', '(tanpa nama)'))
    print('=' * 66)
    for cid, ok, detail in res:
        print('%-4s %-28s %s' % (cid, names.get(cid, ''), 'PASS' if ok else 'FAIL'))
        if detail: print('       %s' % detail)
    failed = [c for c, ok, _ in res if not ok]
    print('-' * 66)
    if failed:
        print('VERDIKT: FAIL pada %s -> DILARANG MENULIS' % ', '.join(failed)); return 1
    print('VERDIKT: PASS -> boleh menulis'); return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'docs/ledger/current.json'))
