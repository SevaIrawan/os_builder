---
name: outbound-write-gate
description: Gate wajib sebelum menulis apa pun ke Confluence, Jira, atau Slack. Menutup lima pola kesalahan yang terbukti berulang. Verdikt diberikan oleh skrip, bukan oleh model.
---

# G-01 — Outbound Write Gate

**Berlaku untuk**: setiap tulisan keluar — halaman Confluence, comment Jira, pesan Slack.
**Tidak berlaku untuk**: file di dalam repo ini, dan jawaban di chat.

**Aturan tunggal**: sebelum memanggil tool tulis apa pun ke luar, jalankan

```
python3 scripts/gate_check.py docs/ledger/<write_id>.json
```

**Exit 0 → boleh menulis. Exit 1 → dilarang menulis.**
Model tidak berhak menilai sendiri bahwa "sebenarnya sudah cukup". Satu-satunya jalan lewat
adalah memperbaiki penyebab sampai skrip keluar 0. Satu-satunya pembatalan adalah perintah
tertulis Bambang, dan itu harus tercatat di ledger sebagai `user_override`.

Definisi gate ada di `.claude/gates/G-01-outbound-write.json`. Skrip membaca definisi itu,
jadi menambah check cukup dengan menambah entri di sana.

---

## Kenapa gate ini ada

Lima pola di bawah **bukan hipotesis**. Semuanya benar-benar terjadi pada sesi 2026-09-20…23,
dan dua di antaranya sudah terlanjur mendarat di halaman produksi (建造单 v40).

| Kode | Pola | Kejadian nyata |
|---|---|---|
| **R1** | Versi bergerak dicatat **nomornya**, isinya tidak dibuka | 04.10 naik ke v20; nomornya kucatat, halamannya tak kubuka. Isinya sudah memuat bukti layar untuk ketujuh project — lalu kutulis ke v40 bahwa buktinya "harus dikeluarkan Schema Owner". Bukti itu sudah ada 24 menit sebelum aku menulis. |
| **R2** | Klaim ditulis **tanpa sumber yang bisa dikutip** | 「改选项即时生效」·「不得在件内另写映射表」·「重复批准不会被 Jira 拦」 — tiga-tiganya karanganku, nol sumber, nol uji. |
| **R3** | Angka **disimpulkan** dari rentang penomoran, bukan dihitung | Kutulis 「SLA C-1～C-20（17 条）」. Dihitung baris demi baris: **16**. Penomoran melompat. |
| **R4** | Dua nama mirip dianggap satu objek | 「PIP 参数组」(8 field, sisi induk) vs 「PIP Extension 参数」(6 field, sisi sub) — kutulis "sudah dibangun" untuk yang salah. Mendarat di v40. |
| **R5** | Ketiadaan dilaporkan sebagai **kesimpulan**, bukan sebagai hasil pencarian terbatas | 「切分审计 nol kemunculan di 建造单」 lalu berhenti — padahal kewajibannya membaca buktinya, dan buktinya ada di OSD-3 c48757/c48764. |

Akar bersamanya satu: **aku memperlakukan "sudah tahu" sama dengan "sudah dibuka"**.
Gate ini menolak asumsi itu secara mekanis.

---

## Cara pakai

### 1. Bangun ledger dulu, sebelum menyusun kalimat

`docs/ledger/<write_id>.json`:

```json
{
  "write_id": "contoh-v41",
  "user_order": "kalimat perintah Bambang, verbatim",
  "target": {
    "system": "confluence", "content_id": "2096463922", "method": "edits",
    "target_snapshot": "v:40", "snapshot_read_at": "2026-09-23T08:00:00Z"
  },
  "reverse_test": "badan hasil dikurangi sisipan == badan sebelumnya, byte demi byte",
  "sources": [
    { "source_id": "04.10", "ref": "1738735636", "version": "v20",
      "live_version": "v20", "read_scope": "full", "read_at": "2026-09-23T08:05:00Z" }
  ],
  "claims": [
    { "id": "K1", "text": "kalimat yang akan ditulis",
      "source_id": "04.10", "quote": "kutipan verbatim dari sumber itu",
      "near_names": ["nama lain yang mirip"], "disambiguation": "kutipan yang memisahkan keduanya",
      "numeric": { "count_cmd": "...", "count_output": "..." },
      "absence": { "searched": ["tempat 1", "tempat 2"], "control_probe": "pencarian pembanding yang TERBUKTI mengembalikan hasil" } }
  ]
}
```

Klaim yang **tidak punya sumber** tidak boleh ditulis sebagai pernyataan faktual. Tulis `🔲`
di dalam `text`-nya — skrip akan melewatkannya, dan pembaca halaman melihat lubang, bukan tebakan.
Ini sejalan dengan 07｜指南 §二「标准页读法」: 🔲 adalah celah, **bukan** untuk diisi sendiri.

### 2. Jalankan skrip. Baca verdiktnya. Jangan nilai sendiri.

Skrip **mendeteksi sendiri** klaim numerik dan klaim-ketiadaan dari teks klaim
(regex angka+satuan, dan kata seperti "tidak ada / belum / nol / 未见 / 查不到").
Jadi klaim tidak bisa lolos hanya dengan tidak diberi tanda — itu disengaja.

### 3. FAIL bukan halangan, itu daftar kerja

Tiap FAIL menyebut klaim mana dan kurang apa. Perbaiki penyebabnya, jalankan lagi.

---

## Yang paling sering bikin FAIL (dan itu benar)

- **C3 read_scope** — sumber dibaca `summary` saja. Membaca ringkasan hanya sah untuk klaim
  tentang **nomor versinya sendiri**. Begitu dipakai mengutip isi, wajib `full`, dan wajib
  dibaca **hari ini**. Inilah yang menutup R1; di sinilah cacat v40 seharusnya tertahan.
- **C5 control_probe** — melaporkan "nol" tanpa pencarian pembanding yang terbukti berhasil.
  Nol bisa berarti "tidak ada" atau "tidak terlihat"; keduanya tak terbedakan tanpa probe
  (07.06.1 **E16**).
- **C4** — angka apa pun yang berbentuk jumlah harus punya perintah hitung dan keluarannya.

---

## Hubungan dengan skill lain

`nosm-sync-check` menjawab **"halaman mana yang bergerak"**.
G-01 menjawab **"apakah tulisan ini boleh keluar"**.

Keduanya tidak saling menggantikan, dan ini bukan pembagian teoretis: pada 2026-09-22
`nosm-sync-check` lulus — 04.10 tercatat naik ke v20 dengan benar — **dan tulisannya tetap cacat**,
karena nomor versi tercatat sementara isinya tidak pernah dibuka. G-01 adalah yang menangkap itu.

Urutannya: `nosm-sync-check` dulu (tahu apa yang bergerak) → baca sumber yang bergerak sampai habis
→ bangun ledger → G-01 → baru menulis.
