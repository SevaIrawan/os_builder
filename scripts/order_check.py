#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pengklasifikasi perintah. Menjawab satu hal: apakah kalimat Bambang ini
MENGIZINKAN tulisan keluar, atau hanya menyuruh memeriksa.

Bukan penilaian model — daftar kata kerjanya tetap dan bisa dibaca siapa pun.
Sebab keberadaannya: 2026-09-22 v39. Perintahnya 'Kau audit detail menyeluruh
sampai habis', lalu kutulis ke halaman. Perintah baca kuperlakukan sebagai izin
tulis. Di sini itu mustahil: 'audit' tidak ada di daftar WRITE.

Pemakaian:
  python3 scripts/order_check.py --text "<kalimat perintah verbatim>"
  python3 scripts/order_check.py --classify-file <file berisi kalimat>
Keluar 0 = WRITE (boleh menulis). 1 = READONLY. 2 = AMBIGU (wajib tanya dulu).
"""
import argparse, re, sys

# Kata kerja yang MENGIZINKAN tulisan keluar. Harus eksplisit.
WRITE = [
    'tulis', 'tuliskan', 'menulis', 'kirim', 'kirimkan', 'post', 'posting',
    'publish', 'terbitkan', 'update halaman', 'comment', 'komentar', 'balas',
    'submit', 'masukkan ke', 'naikkan versi', 'simpan ke confluence',
    '写', '发', '提交', '回帖', '登记到',
]
# Kata kerja yang HANYA menyuruh memeriksa. Tidak pernah jadi izin tulis.
READONLY = [
    'check', 'cek', 'periksa', 'audit', 'baca', 'bacakan', 'analisa', 'analisis',
    'lihat', 'cari', 'carikan', 'verifikasi', 'review', 'pastikan', 'bandingkan',
    'telusuri', 'jelaskan', 'laporkan', 'ringkas', 'buat draft', 'buat draf',
    'siapkan', 'rancang', 'jalankan skill', 'jalankan nosm',
    '查', '读', '核对', '复核', '审计', '检查',
]

def classify(text):
    t = (text or '').lower()
    w = sorted({k for k in WRITE    if k in t})
    r = sorted({k for k in READONLY if k in t})
    if w and r:   return 'AMBIGU',   w, r, 'Ada kata perintah tulis DAN periksa dalam satu kalimat. Wajib tanya Bambang dulu, jangan pilih sendiri.'
    if w:         return 'WRITE',    w, r, 'Mengizinkan tulisan keluar.'
    if r:         return 'READONLY', w, r, 'Perintah memeriksa saja. TIDAK mengizinkan tulisan keluar.'
    return 'READONLY', w, r, 'Tidak ada kata kerja tulis yang eksplisit. Default: TIDAK mengizinkan.'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--text'); ap.add_argument('--classify-file')
    a = ap.parse_args()
    txt = a.text if a.text is not None else open(a.classify_file, encoding='utf-8').read()
    kind, w, r, why = classify(txt)
    print('perintah : %s' % txt.strip().replace('\n', ' ')[:120])
    print('kata tulis   : %s' % (', '.join(w) or '(tidak ada)'))
    print('kata periksa : %s' % (', '.join(r) or '(tidak ada)'))
    print('KLASIFIKASI  : %s' % kind)
    print('%s' % why)
    return {'WRITE': 0, 'READONLY': 1, 'AMBIGU': 2}[kind]

if __name__ == '__main__':
    sys.exit(main())
