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
