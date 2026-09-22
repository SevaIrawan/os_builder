# Percobaan menulis 建造单 v34 — 2026-09-22

> Perintah Bambang: 「Kerjakan, tulis v34 sekarang」. **Tidak jadi ditulis.** Halaman masih **v33**.
> Dua hal ditemukan saat mengeksekusi; keduanya dicatat di sini apa adanya.

---

## 1 · Koreksi: mode tambah-sebagian ternyata ADA

Laporanku sebelumnya (dua kali) berbunyi: 「Tidak ada operasi tambah-sebagian di katalog 300 operasi;
`updateConfluencePage` / `updateConfluenceContent` mengganti seluruh badan」. **Itu salah.**

Skema `mcp__Atlassian_MCP__updateConfluenceContent` memuat parameter `edits`:

> **`edits`** — Granular edit operations. Array of tool-call objects, each with name
> (`replaceNode`, `insertNodeAfter`, `insertNodeBefore`, `deleteNode`, `removeNodes`,
> `moveNode`, `appendNodeToEnd`, `setAttrs`), `localId`, `value`, and `arguments`.
> **Mutually exclusive with `body`.**

Plus `dryRun` (「validate and preview the result without persisting」) dan `snapshotToken`
(wajib untuk update yang mengubah isi halaman).

`localId` itu persis atribut `data-local-id` yang ada 1.964 buah di badan halaman ini. Artinya 16 butir
v34 bisa dikirim sebagai 16 operasi node kecil — **tanpa mengirim ulang 171.063 karakter badan penuh**.

Parameter ini **hanya ada di konektor Atlassian_MCP** (akun Bambang). `mcp__Atlassian_Rovo__updateConfluencePage`
cuma punya `body` (ganti penuh).

**Kenapa terlewat**: aku mencari lewat `discover` tiga kali dengan kata kunci "append/partial/suggestions",
lalu menyimpulkan dari daftar hasil pencarian — **tanpa pernah membuka skema tool primernya sendiri**.
Ini cacat yang sama dengan yang sudah diaudit pada F-003／F-004／F-006／F-008: menyimpulkan tanpa membuka
tempat yang ditunjuk sumbernya.

---

## 2 · Akun Bambang (Atlassian_MCP) kehilangan akses di tengah sesi

Pukul ±05:10Z konektor Atlassian_MCP masih jalan; sesudah itu berhenti.

| Panggilan | Konektor | Hasil |
|---|---|---|
| `discover` ×3 | Atlassian_MCP | ✅ berhasil |
| `getAccessibleAtlassianResources` | Atlassian_MCP | ✅ berhasil |
| `getConfluenceContentVersion` v33 | Atlassian_MCP | ✅ berhasil — authorId `712020:0ec04d28-…` (Bambang) |
| `getConfluenceContentVersion` v32 ×2, v34 ×1, v33 (ulang) ×1 | Atlassian_MCP | ⏱ timeout 60s |
| `listConfluenceContentVersions` (limit 40／12／2) | Atlassian_MCP | ⏱ timeout 60s ×3 |
| `getConfluenceContent` (executeRead ×2; primer detail=outline, detail=summary) | Atlassian_MCP | ⏱ timeout 60s ×4 |
| `atlassianUserInfo` | Atlassian_MCP | ❌ **「You can't access this site because a security policy restricts access to it. Contact your admin for help.」** |
| `atlassianUserInfo` (ulang) | Atlassian_MCP | ⏱ timeout 60s |
| `atlassianUserInfo` | Atlassian_Rovo | ✅ `712020:a93fd17c-…` · Backend Operations · active |
| `searchConfluenceUsingCql id = 2096463922` | Atlassian_Rovo | ✅ halaman `lastModified: Sep 20, 2026` → masih **v33** |

Pesan galat itu bukan timeout jaringan — eksplisit soal **security policy di sisi site**. Panggilan yang
sama persis (`getConfluenceContentVersion` v33) berhasil ±15 menit sebelumnya lalu timeout, jadi ini
perubahan status akses di tengah sesi, bukan soal besar-kecilnya halaman.

---

## 3 · Akibatnya untuk penulisan v34

- Jalur **`edits`** (kecil, aman, ada `dryRun`) **hanya lewat Atlassian_MCP** — sekarang terblokir.
  `snapshotToken` yang diwajibkannya pun hanya bisa diambil lewat `getConfluenceContent` di konektor itu.
- Jalur **badan penuh** lewat Atlassian_Rovo masih hidup, tetapi versi baru akan tercatat atas nama
  **Backend Operations (`712020:a93fd17c-…`)**, bukan akun Bambang yang menulis v33.
- Riwayat versi tidak bisa dibaca sekarang (operasinya hanya ada di Atlassian_MCP), jadi **belum
  terverifikasi** versi mana saja yang selama ini ditulis akun mana. Yang terbaca cuma v33 = akun Bambang.

**Tidak ditulis apa pun.** Menunggu putusan Bambang: tunggu akses akunnya pulih (lalu pakai `edits`),
atau tulis lewat akun Backend Operations dengan badan penuh.

---

## 4 · Yang sudah siap kalau lampu hijau

- `docs/v34-blocks-to-paste.md` — 16 blok + pesan versi v34.
- Jangkar 16 blok sudah diuji terhadap badan HTML v33 (`bs.html`, 171.063 karakter): **14 unik**.
  Dua perlu diperlebar — `NSE-1143 c49117` (2×) dan `两页均登记` (2×); konteks pembeda keduanya sudah
  ditemukan dan dicatat di scratchpad.
- Kalau jalur `edits` yang dipakai, jangkar teks tidak lagi diperlukan — cukup `data-local-id` node sasaran.

---

## 5 · Putusan Bambang (2026-09-22)

> 「Tunggu akses akun ku pulih, jangan pakai akun Backend Operations」

**Akun Backend Operations tidak dipakai untuk menulis halaman ini.** Menunggu Atlassian_MCP pulih,
lalu tulis lewat jalur `edits`.

---

## 6 · Payload `edits` sudah disusun penuh (offline, tanpa API)

16 operasi, tersimpan di `docs/v34-edits-payload.json`. Disusun dari `docs/v34-blocks-to-paste.md`
(teks) dan badan HTML v33 (node). Penanda markdown `**tebal**` / `` `kode` `` sudah dikonversi ke
`<strong>` / `<code>`; teks di-escape dulu.

| | |
|---|---|
| Jumlah operasi | **16** |
| Total payload | **10.103 karakter** |
| Badan penuh (pembanding) | 171.062 karakter |
| Operasi terbesar | 2.241 karakter (butir 18) |

| butir | operasi | localId | panjang |
|---|---|---|---|
| 1 | `replaceNode` | `47a99d847f37` | 1.146 |
| 2 | `replaceNode` | `faf62231223f` | 366 |
| 3 | `replaceNode` | `222fca01406d` | 159 |
| 4 | `replaceNode` | `f7b0ccbccf05` | 449 |
| 5 | `replaceNode` | `40633474c4c4` | 155 |
| 6 | `replaceNode` | `e3b04214f1d1` | 161 |
| 8 | `replaceNode` | `ec4987bfb47f` | 412 |
| 10 | `replaceNode` | `c68f4340304e` | 1.017 |
| 13 | `replaceNode` | `9379c54a35e4` | 359 |
| 19 | `replaceNode` | `2346d7ab9cd5` | 857 |
| 20 | `replaceNode` | `c923492352a9` | 905 |
| 7 | `insertNodeBefore` | `8a864896-…` (h2 `一、配置对应表`) | 142 |
| 9 | `insertNodeBefore` | `8a864896-…` | 596 |
| 14 | `insertNodeBefore` | `8a864896-…` | 880 |
| 18 | `insertNodeBefore` | `8a864896-…` | 2.241 |
| 15 | `appendNodeToEnd` | `952c32b3be2f` (tabel 页首附表) | 258 |

Sebelas `replaceNode` dibangun dari node aslinya apa adanya, hanya `</p>` penutup yang digeser ke
belakang teks baru — jadi **tidak ada satu huruf pun teks lama yang berubah** (sesuai 原文保留不删).
Setiap node sasaran sudah diuji unik di dalam badan v33.

### Urutan eksekusi saat akses pulih

1. `getConfluenceContent` → ambil `snapshotToken`.
2. `updateConfluenceContent` dengan **`dryRun: true`** → periksa HTML hasilnya.
3. Kalau bersih: panggilan sungguhan + `versionMessage` v34.
4. Baca balik + `diffConfluenceContentVersions` v33↔v34.
5. Tandai 16 butir ✅ COMPLETED di `pending-buildsheet-updates.md` (tanggal + versi + bukti baca-balik).

Jaring: `restoreConfluenceContentVersion` ke v33 kalau diff tidak bersih.

---

## 7 · Tiga hal yang perlu putusan Bambang sebelum ditulis

1. **`共 33 行` jadi basi begitu butir 15 mendarat.** Paragraf statistik tepat di bawah 页首附表
   berbunyi 「共 33 行——阻塞中 5；待办 24…；已解封 4」. Sudah diverifikasi: tabel memang **33 baris data**
   sekarang. Butir 15 menambah satu baris 待办 → jadi 34 / 待办 25. Kalimat itu akan salah pada detik
   baris baru masuk. Belum ada butir di daftar v34 yang membetulkannya.
2. **Butir 3 punya ekor yang bukan teks tempel.** Di `v34-blocks-to-paste.md` baris terakhir butir 3
   berbunyi 「Status: 待办 → boleh dipertimbangkan 已解封 untuk bagian bisnis (keputusan builder saat
   update)」 — itu catatan untuk pembangun, bukan kalimat untuk halaman. **Sudah dikeluarkan** dari
   payload. Apakah kolom 状态 baris 12 mau diubah ke 已解封, itu putusan Bambang, bukan putusanku.
3. **Butir 18 kurang tanda kutip penutup di draft.** Teksnya berakhir 「…本条不声称双标识已满足。」 tanpa
   `」` penutup di file draft. Aku **menambahkan** `」` di payload supaya kutipnya seimbang. Kalau tidak
   dikehendaki, bilang, akan kuhapus.

---

## 8 · HASIL — v34 tertulis 2026-09-22 06:27:52.898Z

Akses akun Bambang pulih (`atlassianUserInfo` → `712020:0ec04d28-…`). Urutan dijalankan penuh.

### 8.1 · Dry run menangkap satu kesalahan nyata

`dryRun: true` dengan 16 operasi → `ok: true`, `reason: dry_run_validated`, badan hasil 186.279 karakter.
Diverifikasi dengan skrip terhadap badan v33:

| Pemeriksaan | Hasil |
|---|---|
| 16 sisipan hadir tepat sekali, dan tidak ada di v33 | **lulus 16/16** |
| `data-local-id` lama (1.964) masih ada | **1.964 / 1.964, nol hilang** |
| Uji balik: hasil dikurangi 16 sisipan == v33 | **sama persis karakter demi karakter** |
| **Butir 15 (`appendNodeToEnd` pada tabel `952c32b3be2f`)** | ❌ **salah tempat** — `<tr>` mendarat di **ujung dokumen**, sesudah paragraf 维护说明, **di luar tabel mana pun**. Tabel 页首附表 tetap **33 baris** |

Dua perilaku server yang tercatat (bukan perubahan isi):
- Server **menambah 176 `data-local-id`** pada simpul yang sebelumnya tidak punya (mis. `<tr>`, `<tbody>`).
- Server menulis `&#039;` (6×) dan `&quot;` (8×) menjadi `'` dan `"` literal. Karakternya sama, hanya bentuk serialisasinya.

Setelah dua hal itu dinormalkan, uji balik lulus mutlak.

### 8.2 · Penulisan sungguhan

Butir 15 dikeluarkan. **15 operasi** ditulis: 11 `replaceNode` ＋ 4 `insertNodeBefore`.

Satu percobaan pertama ditolak `400 INVALID_REQUEST_BODY`: `versionMessage: size must be between 0 and 255`.
Pesan versi dipendekkan lalu diterima.

```
version 34 · createdAt 2026-09-22T06:27:52.898Z · snapshot v:34
```

### 8.3 · Bukti baca-balik

`diffConfluenceContentVersions` v33↔v34 (`content_format: markdown`):

| | v33 | v34 |
|---|---|---|
| bodyLength | 56.708 | 62.573 |
| lineCount | 428 | 436 |

**additions 19 · deletions 11 · hunks 5.** Sebelas "deletion" itu adalah baris versi-lama dari 11 sel yang
disisipi — setiap pasangan `-`/`+` memperlihatkan teks lama **utuh kata demi kata** dengan kalimat baru
ditempel di belakangnya. Empat paragraf baru muncul sebagai baris `+` murni sebelum judul `一、配置对应表`.
Tidak ada satu pun teks yang hilang.

Diff manusia: https://nexmax.atlassian.net/wiki/pages/diffpagesbyversion.action?pageId=2096463922&selectedPageVersions=33&selectedPageVersions=34

### 8.4 · Sisa

- **Butir 15** belum mendarat. Perlu cara lain (mis. `replaceNode` pada seluruh tabel `952c32b3be2f`,
  ~32.9 rb karakter; atau `insertNodeAfter` pada `<tr>` terakhir yang **kini sudah punya** `data-local-id`
  sesudah v34 — payload cuma ~258 karakter). Yang kedua jauh lebih murah dan baru mungkin sesudah v34 ada.
- Pertanyaan `共 33 行` di §7 butir 1 **belum berlaku** selama butir 15 belum masuk; baru mengikat saat
  baris ke-34 benar-benar ditambahkan.
- **Butir 11** tidak ikut dan sasarannya memang tidak ada di halaman — menunggu putusan Bambang.

---

## 9 · Butir 15 mendarat di v35 — 2026-09-22 06:37:03.616Z

Perintah Bambang: 「Butir 15 kerjakan sekarang, pakai insertNodeAfter」.

Sesudah v34, setiap `<tr>` di tabel `952c32b3be2f` sudah punya `data-local-id` (ditambahkan server saat
normalisasi v34) — yang di v33 tidak ada. `<tr>` terakhir: **`411da44320ce`**. Itulah yang membuat
`insertNodeAfter` mungkin sekarang dan mustahil sebelumnya.

### 9.1 · Dry run

`ok: true` · `dry_run_validated` · badan 185.766 → 186.279 karakter (**+513**).

| Pemeriksaan | Hasil |
|---|---|
| Baris data 页首附表 | 33 → **34** |
| Baris baru berada **di dalam** tabel `952c32b3be2f` | **ya** — tepat sesudah `</tr>` baris terakhir, sebelum `</tbody></table>` |
| `data-local-id` v34 (2.129) masih ada | **2.129 / 2.129, nol hilang** (11 id baru untuk `<tr>`＋5 `<td>`＋5 `<p>`) |
| Uji balik: hasil dikurangi 1 baris == v34 | **sama persis karakter demi karakter** |

Perbedaan entitas (`&#39;` → `'`) muncul lagi seperti di v34 — bentuk serialisasi, bukan perubahan isi;
setelah dinormalkan uji balik lulus mutlak.

### 9.2 · Penulisan sungguhan

Satu operasi `insertNodeAfter`, payload **513 karakter**.

```
version 35 · createdAt 2026-09-22T06:37:03.616Z · snapshot v:35
```

### 9.3 · Bukti baca-balik

`diffConfluenceContentVersions` v34↔v35 (`markdown`): bodyLength 62.573 → 62.759, lineCount 436 → 437,
**additions 1 · deletions 0 · hunks 1**. Satu baris tabel ditambahkan, tepat di bawah baris
「主单 Issue Type 命名…」 dan tepat di atas paragraf **统计**. Tidak ada baris lain yang tersentuh.

Diff manusia: https://nexmax.atlassian.net/wiki/pages/diffpagesbyversion.action?pageId=2096463922&selectedPageVersions=34&selectedPageVersions=35

### 9.4 · Satu akibat yang sudah dicatat, belum diperbaiki

Paragraf **统计** (`data-local-id="a99c1693d3d4"`) tepat di bawah tabel masih berbunyi
「共 33 行——阻塞中 5；待办 24…；已解封 4」（5＋24＋4＝33）. Sejak v35 tabelnya **34 baris / 待办 25**,
jadi angka itu tidak lagi akurat.

Ini **tidak disembunyikan**: sudah tertulis di pesan versi v35 sendiri — 「本表由 33 行增至 34 行；下方统计段
「共 33 行……待办 24」因此不再准确，未在本版订正，另候指示。」

Koreksinya sudah disiapkan sebagai **butir 21** di `pending-buildsheet-updates.md` (satu `replaceNode`
pada `a99c1693d3d4`, ±140 karakter), **menunggu perintah Bambang** — sesuai aturan file itu sendiri:
「Tidak ada butir yang ditulis ke Confluence tanpa perintah Bambang」.

---

## 10 · Butir 21 (koreksi statistik) mendarat di v36 — 2026-09-22 06:41:40.175Z

Perintah Bambang: 「Butir 21 kerjakan sekarang」.

### 10.1 · Angka dihitung mekanis, tidak dikira

Sebelum menyusun teks koreksi, kolom 状态 tiap baris tabel `952c32b3be2f` di badan v35 dibaca satu per satu:

| Nilai kolom 状态 apa adanya | Jumlah |
|---|---|
| 待办 | 13 |
| 待办（建造侧提出·双签未表态） | 10 |
| 阻塞中 | 5 |
| 已解封（2026-09-18） | 3 |
| 待办（阻塞带主体测试段） | 1 |
| 已解封（2026-09-19） | 1 |
| 待办（建造侧提出·双签未表态·文档订正） | 1 |

→ **阻塞中 5 · 待办 25 · 已解封 4 = 34.** Sub-hitungan 「建造侧提出·双签未表态」 tetap **11** (10＋1),
karena baris baru dari v35 bukan kategori itu. Jadi hanya dua angka yang berubah: total 33→34, 待办 24→25.

### 10.2 · Dry run

`ok: true` · badan 186.343 → 186.558 (**+215**).

| Pemeriksaan | Hasil |
|---|---|
| Node hasil identik dengan `value` yang dikirim, tepat 1 kali | ya |
| Kalimat asli 「共 33 行……待办 24」 masih utuh | ya — node lama tertanam apa adanya di depan koreksi |
| 「共 34 行」 muncul | 1 kali |
| `data-local-id` v35 (2.140) | **2.140 utuh, nol hilang, nol ditambah** |
| Baris data tabel | tetap 34 (tidak tersentuh) |
| Uji balik: node dikembalikan == v35 | **sama persis karakter demi karakter** |

Satu cek di skrip sempat berbunyi gagal — 「共 33 行」 dihitung 1 kali, ternyata 2. Itu salah skripku,
bukan salah isi: frasa itu muncul sekali sebagai kalimat asli dan sekali lagi sebagai kutipan di dalam
kalimat koreksi.

### 10.3 · Bukti baca-balik

`diffConfluenceContentVersions` v35↔v36 (`markdown`): bodyLength 62.759 → 62.999, lineCount **437 → 437**,
**additions 1 · deletions 1 · hunks 1** — satu paragraf, kalimat lama utuh kata demi kata dengan koreksi
ditempel di belakangnya (原文保留不删).

Diff manusia: https://nexmax.atlassian.net/wiki/pages/diffpagesbyversion.action?pageId=2096463922&selectedPageVersions=35&selectedPageVersions=36

### 10.4 · Sisa daftar

**19 COMPLETED · 1 PENDING · 1 PANTAU.** Yang tersisa cuma **butir 11** — sasarannya (baris
「协作 Thread」 di 区六 建造单) memang tidak ada di halaman, dan butir itu sendiri menulis S-05 tidak
memakai komponennya. Menunggu putusan Bambang: digugurkan, atau dialihkan ke baris lain.
