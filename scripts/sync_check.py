#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""nosm-sync-check langkah 2-5 — perbandingan mekanis dua salinan terkendali.

Pemakaian:
  python3 scripts/sync_check.py --skill-src <file> --nav-src <file>

<file> skill  = teks §八 halaman 07.06 apa adanya (preamble + bullet + 开发入口的冻结要求).
<file> nav    = tiga tabel halaman 04, tiap tabel didahului baris penanda:
                '## TBL-A ...', '## TBL-B ...', '## TBL-C ...'
                A=§一 动作路由, B=§五 登记集, C=§六 子页地图.

Keluar 0 = tidak ada 部署漂移. Keluar 1 = drift (jangan bekerja di atas salinan basi).
Alasan skrip ini ada: perbandingan dengan mata pernah melewatkan kolom yang hilang
(2026-09-21). Bandingkan HEADER dan JUMLAH KOLOM juga, bukan hanya isi baris."""
import argparse, re, sys

def norm(s):
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)          # link markdown -> teksnya
    s = s.replace('**', '').replace('`', '').replace('\\', '')
    return re.sub(r'\s+', '', s)

def bullets(t):
    return [norm(l[2:]) for l in t.split('\n') if l.startswith('- ') or l.startswith('* ')]

def tables(txt):
    out, cur = [], None
    for ln in txt.split('\n'):
        if ln.strip().startswith('|'):
            cells = ln.strip().strip('|').split('|')
            if set(''.join(cells).replace(' ', '')) <= set('-:'):   # baris pemisah
                continue
            (cur if cur is not None else out.append([]) or out[-1]).append if False else None
            if cur is None: cur = []
            cur.append([norm(c) for c in cells])
        elif cur:
            out.append(cur); cur = None
    if cur: out.append(cur)
    return out

def cmp_list(name, S, L, fails):
    ok = True
    if len(S) != len(L):
        print('  %-22s jumlah: sumber=%d lokal=%d  *** BEDA ***' % (name, len(S), len(L)))
        fails.append(name); ok = False
    else:
        print('  %-22s jumlah: %d vs %d  sama' % (name, len(S), len(L)))
    bad = 0
    for i, (a, b) in enumerate(zip(S, L), 1):
        if a != b:
            bad += 1; ok = False
            print('    *** ITEM %d BEDA ***' % i)
            for j in range(min(len(a), len(b))):
                if a[j] != b[j]:
                    print('      sumber: ...%s...' % a[max(0, j-40):j+40])
                    print('      lokal : ...%s...' % b[max(0, j-40):j+40])
                    break
            else:
                print('      panjang beda: sumber=%d lokal=%d' % (len(a), len(b)))
    if bad: fails.append(name)
    print('  %-22s identik: %d/%d' % (name, len(S) - bad, len(S)))
    return ok

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--skill-src', required=True)
    ap.add_argument('--nav-src', required=True)
    ap.add_argument('--claude', default='CLAUDE.md')
    ap.add_argument('--nav', default='docs/04-anchor-navigation.md')
    a = ap.parse_args()
    fails = []

    print('=' * 66); print('nosm-sync-check langkah 2-5 — salinan terkendali'); print('=' * 66)

    # --- CLAUDE.md vs 07.06 §八 ---
    src = open(a.skill_src, encoding='utf-8').read()
    cm  = open(a.claude,    encoding='utf-8').read()
    i, j = cm.index('## 一、流程建设 Skill'), cm.index('## 二、快速索引')
    sec = cm[i:j]
    print('\n[1] CLAUDE.md §一  vs  07.06 §八')
    cmp_list('bulir', bullets(src), bullets(sec), fails)
    p_s = norm(src.split('\n\n')[0])
    p_l = norm(sec[sec.index('本节是「流程建设 Skill」的唯一规范源'):sec.index('### 流程建设 skill')])
    print('  %-22s %s' % ('preamble', 'sama' if p_s == p_l else '*** BEDA ***'))
    if p_s != p_l: fails.append('preamble')
    f_s = norm(src.split('## 开发入口的冻结要求')[1]).rstrip('-')
    f_l = norm(sec.split('开发入口的冻结要求')[1]).rstrip('-')
    print('  %-22s %s' % ('开发入口的冻结要求', 'sama' if f_s == f_l else '*** BEDA ***'))
    if f_s != f_l: fails.append('开发入口的冻结要求')

    # --- anchor vs 04 ---
    ntxt = open(a.nav_src, encoding='utf-8').read()
    blocks = {}
    for part in re.split(r'^## (TBL-[ABC])[^\n]*$', ntxt, flags=re.M)[1:]:
        if part.startswith('TBL-'): key = part; continue
        blocks[key] = tables(part)[0]
    loc = tables(open(a.nav, encoding='utf-8').read())
    # urutan file lokal: §一, §六(peta subhalaman), §五(登记集)
    pairs = [('TBL-A §一 动作路由', blocks['TBL-A'], loc[0]),
             ('TBL-B §五 登记集',   blocks['TBL-B'], loc[2]),
             ('TBL-C §六 子页地图', blocks['TBL-C'], loc[1])]
    print('\n[2] docs/04-anchor-navigation.md  vs  04')
    for nm, S, L in pairs:
        print('  --- %s ---' % nm)
        nc_s, nc_l = len(S[0]), len(L[0])
        print('  %-22s sumber=%d lokal=%d  %s' % ('jumlah kolom', nc_s, nc_l, 'sama' if nc_s == nc_l else '*** BEDA ***'))
        if nc_s != nc_l: fails.append(nm + '/kolom')
        print('  %-22s %s' % ('header', 'sama' if S[0] == L[0] else '*** BEDA ***'))
        if S[0] != L[0]: fails.append(nm + '/header')
        cmp_list('baris', S[1:], L[1:], fails)

    print('-' * 66)
    if fails:
        print('VERDIKT: 部署漂移 pada %s -> HENTIKAN, jangan bekerja di atas salinan basi' % ', '.join(fails))
        return 1
    print('VERDIKT: tidak ada 部署漂移')
    return 0

if __name__ == '__main__':
    sys.exit(main())
