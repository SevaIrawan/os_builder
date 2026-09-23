# Uji G-01 langsung, 2026-09-23

Perintah Bambang: "Jalankan keduanya", yaitu uji blokir langsung dan uji ujung ke ujung dengan draft asli.

## Uji 1: blokir langsung

- Aksi: `addOrEditJiraIssueComment` ke `ZZZ-1` tanpa ledger.
- Hasil: **diblokir oleh hook PreToolUse sebelum terkirim**.
- Pesan hook: "G-01: no ledger in docs/ledger/ has a payload_file identical to this ... input."

## Uji 2: ujung ke ujung, draft koreksi dua cacat v40

- Draft: `docs/drafts/2026-09-23-v40-correction-draft.md`
- Ledger: `docs/ledger/D-2026-09-23-01.json`
- Pencarian: dua CQL ("PIP Extension", "Show Cause") menghasilkan 4 halaman. Keempatnya dibaca penuh:
  - 建造单 v40, 8/8 bagian lewat read_source.py
  - Spec S-05 v62, 8/8 bagian
  - 04.10 v20, inline
  - 04.7 v49, inline

### Putaran 1: FAIL pada D2 dan D3

- D3: "v40 区三" terbaca sebagai jumlah "40 区". Ini **salah deteksi di skrip**, salahnya ke arah aman. Kalimat draft diubah jadi "建造单 v40 的区三原句" dan D3 lolos.
- D2: dua kutipan Spec (K2, K3) "tidak ditemukan", padahal teksnya ada di sumber. Lihat bug 1.

### Putaran 2: FAIL hanya pada D2 (bug 1)

## Cacat gate yang ditemukan uji ini (belum diperbaiki, file gate terkunci)

1. **TAG_RE di nosm_lib.strip_markup terlalu rakus.** Pola `<[^>]+>` memakan karakter `<` harfiah, misalnya `延期次数\<1` di Spec, sampai ke `>` berikutnya.
   - Akibat A (aman): kutipan yang benar ditolak (D2 di atas).
   - Akibat B (**TIDAK aman**): kalimat draft atau payload yang terapit `<` dan `>` hilang dari pemeriksaan D1. Contoh uji:
     - Input: `打回次数 <2 时可再打回。PIP 参数组已全部建成。延长期 >1 次不允许。`
     - Yang terlihat oleh gate hanya `['打回次数 1 次不允许']`.
     - Kalimat "PIP 参数组已全部建成" lolos tanpa klaim.
   - Usulan perbaikan: `<\/?[A-Za-z][^<>]*>`, hanya tag sungguhan.
2. **Angka setelah "v" terbaca sebagai jumlah** ("v40 区" dibaca sebagai 40 区). Usulan: token yang didahului `v` (nomor versi) tidak dianggap jumlah.
3. **B1 untuk draft menerima perintah draft lama.** Draft ini diizinkan oleh "Buat draft dulu" (2026-09-22 08:40), padahal perintah itu untuk draft Bagian 7, bukan draft ini. Usulan: perintah draft kedaluwarsa setelah N jam, atau harus menyebut sasaran.

Perbaikan ketiganya butuh "UNLOCK G-01" dari Bambang.
