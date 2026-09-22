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
