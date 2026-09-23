---
name: outbound-write-gate
description: Gate wajib sebelum apa pun keluar ke Confluence, Jira, atau Slack. Dua pertanyaan yang dijawab skrip, bukan model - apakah aku diizinkan, dan apakah yang kutulis benar. Dibangun dari pelanggaran nyata, bukan teori.
---

# G-01 — Outbound Write Gate

**Mengikat**: setiap tulisan keluar — halaman Confluence, comment Jira, pesan Slack.
**Tidak mengikat**: file di repo ini, dan jawaban di chat.

```
python3 scripts/gate_check.py docs/ledger/<write_id>.json
```

**Exit 0 → boleh menulis. Exit 1 → dilarang.** Model tidak berhak menilai sendiri bahwa
"sebenarnya sudah cukup". Satu-satunya jalan lewat adalah memperbaiki penyebab sampai skrip
keluar 0.

---

## Gate ini menjawab DUA pertanyaan, dan yang pertama lebih penting

### Pertanyaan 1 — **Apakah aku diizinkan?** (C10, C12, C13, C14)

Versi pertama gate ini punya lubang yang membatalkan seluruh gunanya: kolom `user_order`
**kuisi sendiri**. Gate yang menanyai dirinya sendiri tidak menahan apa pun.

Sekarang izin **diverifikasi, bukan dideklarasikan**:

| Check | Yang dipastikan |
|---|---|
| **C10** | `user_order` sama persis dengan satu baris di `docs/orders/orders.jsonl`. Tidak boleh diketik bebas. |
| **C12** | Baris itu berklasifikasi **WRITE** menurut `scripts/order_check.py`. READONLY atau AMBIGU = dilarang, wajib tanya dulu. |
| **C13** | `consumed_by` masih null. **Satu perintah = satu tulisan.** |
| **C14** | `target` perintah sama dengan sasaran tulisan ini. |

Alur perintah:

```
python3 scripts/order_log.py --add --verbatim "<kalimat Bambang apa adanya>" --target "confluence:<id>"
python3 scripts/order_log.py --list
python3 scripts/order_log.py --consume <order_id> --by <write_id>     # sesudah menulis
```

Klasifikasi dikerjakan daftar kata kerja tetap di `scripts/order_check.py`, bukan oleh
penilaianku. `tulis / kirim / post / publish / balas / 提交` mengizinkan.
`check / cek / periksa / audit / baca / analisa / buat draft / 核对` **tidak pernah** mengizinkan.

**Kenapa ini ada — kejadian nyata, 2026-09-22.** Perintah Bambang:
「Kau audit detail menyeluruh sampai habis dan tidak ada kesimpulan sesat disana」.
Itu perintah **memeriksa**. Aku memeriksa, menemukan lima hal, lalu **menulis sendiri ke halaman
produksi** — lahir **v39**, tanpa disuruh. Diuji ulang pada gate ini: **FAIL di C12**, exit 1.

**Salah ke arah aman itu disengaja.** 「Butir 11 alihkan sekarang」 diklasifikasi READONLY
padahal itu perintah tulis yang sah — `alihkan` tidak ada di daftar. Akibatnya aku bertanya
dulu. Biaya salah-arah-aman: satu pertanyaan. Biaya salah-arah-sebaliknya: v39.
**Jangan pernah melonggarkan daftar WRITE untuk mengurangi pertanyaan.**

### Pertanyaan 2 — **Apakah yang kutulis benar?** (C1–C9, C11)

| Kode | Pola | Kejadian nyata | Check |
|---|---|---|---|
| **R1** | Versi dicatat **nomornya**, isinya tak dibuka | 04.10 naik v20; nomornya kucatat, halamannya tak kubuka — isinya sudah memuat bukti layar ketujuh project, lalu kutulis ke v40 bahwa buktinya "harus dikeluarkan Schema Owner". Bukti itu sudah ada **24 menit** sebelumnya. | **C3** + **C11** |
| **R2** | Klaim tanpa sumber | 「改选项即时生效」·「不得另写映射表」·「重复批准不会被 Jira 拦」 — tiga-tiganya karanganku | **C2**, **C8** |
| **R3** | Angka **disimpulkan** dari rentang nomor | 「SLA 17 条」, sebenarnya **16** | **C4** |
| **R4** | Nama mirip = satu objek | 「PIP 参数组」 vs 「PIP Extension 参数」 → masuk v40 | **C6** |
| **R5** | Ketiadaan sebagai kesimpulan | 「切分审计 nol kemunculan」 lalu berhenti | **C5** |

Sisanya: **C1** ledger ada · **C7** snapshot sasaran diambil hari ini (07 v28 §二 先查后写) ·
**C9** uji balik direncanakan.

Skrip **mendeteksi sendiri** klaim numerik dan klaim-ketiadaan lewat regex pada teks klaim.
Klaim tidak bisa lolos hanya dengan tidak kuberi tanda — itu disengaja.

Klaim yang tidak punya sumber **tidak boleh** jadi pernyataan faktual: tulis `🔲` di teksnya.
Sejalan dengan 07｜指南 §二「标准页读法」— 🔲 adalah celah, **bukan** untuk diisi sendiri.

---

## Urutan lengkap, tiap panah ada penjaganya

```
perintah Bambang masuk   -> order_log.py --add        (diklasifikasi mesin)
  READONLY / AMBIGU?     -> BERHENTI, tanya dulu. Jangan lanjut.
nosm-sync-check          -> sync_check.py             (exit 1 = 部署漂移, berhenti)
  + emit sapuan          -> docs/ledger/_sweep-latest.json
baca penuh yang bergerak -> read_after_move di sapuan itu
bangun claims ledger     -> docs/ledger/<write_id>.json
G-01                     -> gate_check.py             (exit 1 = dilarang menulis)
tulis
sesudahnya               -> order_log.py --consume    (perintah habis, tak bisa dipakai lagi)
```

---

## Lubang yang MASIH ADA — harus dikatakan, bukan disembunyikan

**Tidak ada yang memaksaku menjalankan gate ini.** Semua di atas menahan *kalau* skripnya
dijalankan. Aku masih bisa memanggil tool tulis tanpa menjalankannya sama sekali.

Penutup satu-satunya adalah **hook `PreToolUse` di `.claude/settings.json`** yang memblokir
tool tulis Confluence/Jira/Slack kecuali gate baru saja keluar 0.

**Itu belum dipasang**, karena Bambang punya aturan berdiri: *"Jangan ubah setingan apapun."*
Hook itu mengubah `settings.json`. Jadi keputusannya ada padanya, bukan padaku — dan sampai
dia bilang pasang, gate ini bergantung pada kepatuhanku menjalankannya. Aku tidak boleh
menggambarkannya lebih kuat dari itu.
