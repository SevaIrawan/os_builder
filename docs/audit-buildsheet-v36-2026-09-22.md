# Audit halaman 建造单 v36 — 2026-09-22

> Perintah Bambang: 「Inti nya halaman builder sudah valid tidak, kau check detail dan teliti」.
> Diperiksa pada badan HTML v36 yang dibaca langsung dari server (186.622 karakter), bukan dari salinan repo.

**Jawaban singkat: struktur halaman valid, isinya BELUM konsisten.** Ada **8 titik** yang saling
bertentangan dengan catatan yang baru ditulis di v34. Penyebabnya dari sisi pembangun (aku), bukan dari
mekanisme tulisnya.

---

## 1 · Yang sudah terbukti valid

| Pemeriksaan | Hasil |
|---|---|
| Tag HTML tertutup semua | ✅ nol tag menggantung |
| Nesting | ✅ nol galat |
| Jumlah `<table>` | 15 |
| Konsistensi kolom tiap tabel | ✅ **15/15 seragam** (tiap baris = lebar header-nya) |
| `<tr>` liar di luar tabel | ✅ tidak ada — sisa `appendNodeToEnd` yang gagal di v34 memang tidak pernah tersimpan |
| 页首附表 | 35 baris = 1 header + **34 data** |
| Duplikasi sisipan | ✅ tidak ada. 17 sisipan, 15 muncul tepat 1×; dua yang muncul 2× sudah ditelusuri dan sah: 「04.3 Owner＝Kayden Lee」 (1 kalimat lama di baris N28 sejak v33 ＋ 1 koreksi butir 5) dan 「S-05 各 n8n 件切 active 的次序」 (1 baris tabel baru ＋ 1 kutipan di dalam koreksi butir 21) |
| `data-local-id` | ✅ nol hilang di ketiga penulisan (v34, v35, v36) |
| Paragraf 统计 | ✅ sudah benar — 34 行／阻塞中 5／待办 25／已解封 4, cocok dengan hitungan mekanis baris demi baris |

Ketiga penulisan itu sendiri bersih. Diff sisi server: v33→v34 additions 19/deletions 11;
v34→v35 additions 1/deletions 0; v35→v36 additions 1/deletions 1. Tidak ada teks lama yang hilang.

---

## 2 · Yang TIDAK konsisten — 8 titik, satu akar

Tiga transisi terminal (`Reject` 3 / `Withdraw` 8 / `Cancel as Duplicate` 9) **sudah benar-benar dijalankan
2026-09-22** dengan SSCSD-423 / SSCSD-421 / SSCSD-422. v34 menulis kesimpulannya di tiga tempat. Tetapi
**delapan tempat lain di halaman yang sama masih menyatakan sebaliknya**, atau masih memuat klaim yang
justru dipatahkan oleh eksekusi itu.

| # | Tempat | Bunyi sekarang | Kenyataan |
|---|---|---|---|
| 1 | 区二 转换表, 转换 **3** `Reject`, kolom 回读 | 「…；**未实跑**」 | Sudah dijalankan — SSCSD-423 |
| 2 | 区二 转换表, 转换 **8** `Withdraw`, kolom post function (`842f22d1-…`) | 「Resolution＝Cancelled（**「取消原因」＝Withdrawn**）」 | Eksekusi membuktikan **tidak ada** 取消原因 yang ditulis ke field mana pun (cf18054／cf18143 null; field-nya belum ada) |
| 3 | 区二 转换表, 转换 **8**, kolom 回读 | 「API：同上；**未实跑**」 | Sudah dijalankan — SSCSD-421 |
| 4 | 区二 转换表, 转换 **9** `Cancel as Duplicate`, post function (`897f93d7-…`) | 「Resolution＝Cancelled（**「取消原因」＝Duplicate Case**）」 | Sama seperti no. 2 |
| 5 | 区二 转换表, 转换 **9**, kolom 回读 | 「API：同上；**未实跑**」 | Sudah dijalankan — SSCSD-422 |
| 6 | 区一 配置对应表, baris **N06**, kolom 状态 | 「已建（API 回读）；转态权限待配；**该转换尚未实跑**」 | `Withdraw`(8) sudah dijalankan |
| 7 | 区一 配置对应表, baris **N07**, kolom 状态 | 「…**Reject 已建未实跑**；…」 | `Reject`(3) sudah dijalankan |
| 8 | 第八区, paragraf `33b97c1d-…` | 「其余四条（Reject／Withdraw／Cancel as Duplicate／Abort Case）**已配置但未实跑**」 | Tiga dari empat sudah dijalankan; sisa satu (`Abort Case`) saja |

### Plus satu cacat bentuk

**Butir 18 mendarat sebagai paragraf yang berbunyi seperti instruksi, bukan seperti catatan.** Teksnya di
halaman berbunyi:

> 「結構测试（2026-09-22…）」**新增两行**：①判据「回读验证（转换属性·API）」…；②判据「终态转换实跑…」…
> 「测试单登记」**加三行**：SSCSD-421…SSCSD-422…SSCSD-423…

Tetapi dua tabel yang dimaksud **tidak bertambah baris**:

| Tabel | localId | Isi sekarang |
|---|---|---|
| 第八区「测试记录」 | `7ea6f8f4-…` | **6 baris data**, semuanya bertanggal 2026-09-18. Dua baris yang disebut tidak ada |
| 第八区「测试单登记」 | `5e5cda82-…` | **1 baris data** — hanya SSCSD-411. SSCSD-421／422／423 tidak ada |

Jadi pembaca halaman melihat kalimat 「新增两行」／「加三行」 yang tidak pernah dilaksanakan. Isinya benar;
penempatannya yang salah.

---

## 3 · Kenapa ini terjadi — akarnya satu

`docs/v34-blocks-to-paste.md` disusun untuk **ditempel manusia**: sebelas blok punya jangkar kalimat di sel
tertentu, sedangkan butir **7／9／14／18** dikumpulkan jadi 「empat paragraf baru sebelum judul 一、配置对应表」.
Waktu jalurnya berubah jadi operasi `edits`, aku memindahkan daftar itu apa adanya. Akibatnya:

- **Butir 18** mempertahankan teksnya tetapi kehilangan penempatannya — kalimat 「新增两行」 jadi instruksi
  yang menggantung.
- **Butir 20** ditulis untuk 「转换 3／8／9 三行的 post function 列」, tetapi file blok cuma memberi **satu
  jangkar** (sel 转换 3). Dua sel lain tidak pernah tersentuh — dan aku tidak memeriksa ketidakcocokan
  antara judul butir (tiga baris) dan jangkarnya (satu baris) sebelum menulis.
- **Tidak ada satu butir pun** di daftar v34 yang menyentuh kolom 回读 di 区二, baris N06／N07 di 区一, atau
  kalimat 第八区 tentang 「其余四条」. Padahal semuanya ikut jadi salah begitu tiga transisi dijalankan.

Ini kelalaian pembangun waktu menyusun daftar, bukan cacat jalur `edits` dan bukan akibat perpindahan akun.

---

## 4 · Usulan perbaikan — belum ditulis, menunggu perintah

Delapan titik di atas plus satu cacat bentuk, seluruhnya bisa selesai dalam **satu versi (v37)** dengan
operasi `edits`. Semua mengikuti kebiasaan halaman 原文保留不删 — kalimat lama tidak dihapus, koreksi
ditempel di belakangnya. Dua tabel 第八区 diperbaiki dengan `insertNodeAfter` pada baris terakhirnya, yang
sekarang sudah punya `data-local-id` (sama seperti cara butir 15 mendarat di v35).

| Usul | Operasi | Sasaran |
|---|---|---|
| 22 | `replaceNode` ×3 | Kolom 回读 转换 3／8／9 — tambah keterangan sudah dijalankan ＋ nomor TEST-nya |
| 23 | `replaceNode` ×2 | post function 转换 8 (`842f22d1-…`) dan 转换 9 (`897f93d7-…`) — tempel temuan bahwa 取消原因 tidak jatuh ke field mana pun |
| 24 | `replaceNode` ×2 | 区一 baris N06 dan N07, kolom 状态 |
| 25 | `replaceNode` | 第八区 `33b97c1d-…` — 「其余四条…未实跑」 jadi 「余一条」 |
| 26 | `insertNodeAfter` ×2 | Tabel 测试记录 (`7ea6f8f4-…`) — dua baris betulan |
| 27 | `insertNodeAfter` ×3 | Tabel 测试单登记 (`5e5cda82-…`) — SSCSD-421／422／423 sebagai baris betulan |
| 28 | `replaceNode` | Paragraf butir 18 — begitu baris betulannya ada, tempel keterangan bahwa dua tabel itu sudah diisi, supaya 「新增两行」 tidak lagi terbaca sebagai instruksi menggantung |

Tidak ada satu pun yang ditulis tanpa perintah Bambang.

---

## 5 · Ringkas

- **Struktur halaman: valid.** Tidak ada markup rusak, tidak ada tabel cacat, tidak ada duplikasi, tidak
  ada teks yang hilang. Ketiga penulisan hari ini bersih dan terbukti lewat diff sisi server.
- **Isi halaman: belum konsisten.** Delapan pernyataan masih bertentangan dengan tiga transisi yang sudah
  dijalankan, dan satu paragraf berbunyi seperti instruksi yang belum dikerjakan.
- **Akarnya kelalaianku** waktu memindahkan daftar tempel-manual jadi daftar operasi `edits`, terutama
  butir 20 yang judulnya tiga baris tetapi jangkarnya cuma satu.

---

## 6 · TINDAK LANJUT — butir 22–28 dikerjakan, v37 (2026-09-22 06:53:16.294Z)

Perintah Bambang: 「Kerjakan 22-28 sekarang, satu versi v37」. Seluruhnya masuk **satu versi**,
**14 operasi** (9 `replaceNode` ＋ 5 `insertNodeAfter`), payload 7.390 karakter.

### 6.1 · Dry run menangkap satu kesalahan lagi

Dry run pertama menunjukkan **urutan baris terbalik** di kedua tabel 第八区. Dugaanku salah:
`insertNodeAfter` berulang pada jangkar yang sama ternyata menyisipkan menurut **urutan kirim**
(tiap baris baru masuk sesudah baris yang baru saja disisipkan), bukan terbalik. Urutan dibetulkan,
dry run kedua memastikan: 测试记录 → 回读验证 lalu 终态转换实跑; 测试单登记 → SSCSD-421, 422, 423.

### 6.2 · Verifikasi pada badan v37 yang TERSIMPAN (bukan dry run)

Halaman dibaca ulang dari server sesudah penulisan, lalu diperiksa:

| Pemeriksaan | Hasil |
|---|---|
| Tag menggantung / galat nesting | **nol / nol** |
| 15 tabel, konsistensi kolom | **15/15 seragam** |
| `<tr>` di luar tabel | nol |
| Delapan titik kontradiksi audit §2 | **8/8 sudah dikoreksi** |
| Cacat bentuk butir 18 | **ditutup** — 「新增两行」／「加三行」 dinyatakan sudah dilaksanakan |
| Tabel 测试记录 | 6 → **8 baris data**, urutan benar |
| Tabel 测试单登记 | 1 → **4 baris data** (411, 421, 422, 423), urutan benar |
| 页首附表 | 34 baris, 统计 menyebut 共 34 行 |
| `data-local-id` v36 (2.140) | **utuh, nol hilang**; 45 id baru = 5 `<tr>` ＋ 20 `<td>` ＋ 20 `<p>` |
| **Uji balik**: v37 dikembalikan ke v36 | **sama persis karakter demi karakter** |

### 6.3 · Kalimat 「未实跑」 yang masih ada — semuanya sah

Delapan kemunculan tersisa diperiksa satu per satu:

- **Tiga** benar-benar masih berlaku, semuanya tentang `Abort Case`(11) yang memang belum dijalankan
  atas instruksi Bambang: 区二 转换 11 kolom 回读, 区一 baris N28, dan frasa 「未实跑 1 条：Abort Case(11)」.
- **Lima** adalah kalimat lama yang **sengaja tidak dihapus** (原文保留不删) dengan koreksi tertempel di
  sel/paragraf yang sama, atau kutipan kalimat lama di dalam koreksi itu sendiri.

**Nol pernyataan salah yang berdiri tanpa koreksi.**

### 6.4 · Status

**26 COMPLETED · 1 PENDING · 1 PANTAU.** Sisa satu-satunya: **butir 11** — sasarannya (baris
「协作 Thread」 di 区六) tidak ada di halaman, dan butir itu sendiri menulis S-05 tidak memakai
komponennya. Menunggu putusan Bambang.
