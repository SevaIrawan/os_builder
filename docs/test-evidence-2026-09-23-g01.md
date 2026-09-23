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

## Uji hook akhir giliran (Stop)

- Saat giliran hendak diakhiri, hook Stop **memblokir** karena draft uji gagal G-01 (D2). Terbukti bekerja secara langsung.
- Sesudahnya file draft uji dihapus dari repo. Isinya tetap tersimpan di commit 3b83035. Ledger D-2026-09-23-01.json disimpan sebagai bukti.

## Perbaikan ketiga cacat (perintah Bambang: "UNLOCK G-01 perbaiki ketiga cacat itu")

1. Pola tag sekarang `</?[A-Za-z][^<>]*>`. Karakter `<` harfiah tidak lagi memakan teks. Pada kasus nyata, kutipan K2/K3 sekarang ditemukan di Spec v62.
2. Angka yang didahului `v` sekarang dibaca sebagai nomor versi, bukan jumlah. "v40 区三" tidak lagi dianggap jumlah, sedangkan "共 40 区" tetap tertangkap.
3. Izin draft kedaluwarsa setelah `windows_minutes.draft_order_age` (720 menit). "Buat draft dulu" berumur 1018 menit sekarang ditolak dengan pesan "ask the owner".

Self-test: 59/59 lulus, termasuk lima uji baru untuk ketiga cacat.

## Cacat keempat (ditemukan saat membuat draft koreksi v40, belum diperbaiki)

4. **Nomor issue Jira terbaca sebagai angka.** "OSD-116" menghasilkan angka 116, yang lalu dituntut ada di kutipan. Salahnya ke arah aman. Untuk sumber Confluence, content_id sudah dikecualikan, tetapi kunci issue Jira belum. Usulan: token angka yang merupakan bagian kunci issue (`[A-Z]+-\d+`) diperlakukan sebagai identitas, bukan jumlah. Perbaikan butuh "UNLOCK G-01".
   - Pada draft ini aku menggantinya dengan nomor komentar (c50345, c50237) yang dikutip langsung, jadi aturannya tidak dilonggarkan.

## Draft koreksi dua cacat v40: PASS

- Ledger: `docs/ledger/D-2026-09-23-02.json`
- Draft: `docs/drafts/2026-09-23-v40-correction-draft.md`
- Sumber, semua dibaca penuh:
  - 建造单 v40, 8/8 bagian
  - Spec v62, 8/8 bagian
  - 04.10 v20
  - 04.7 v49
  - 04.8 v21
  - OSD-116, 167 komentar, 25/25 bagian
- Pencarian: tiga CQL dan dua halaman listing komentar; 172 hit, semuanya dibaca.

## Perbaikan cacat keempat (perintah Bambang: "UNLOCK G-01 perbaiki cacat keempat itu")

- Nomor issue Jira (pola `[A-Z][A-Z0-9]+-\d+`, misalnya OSD-116 atau NSE-1126) sekarang dibaca sebagai identitas, bukan angka.
- Aturannya: issue yang disebut dalam klaim harus berupa sumber yang dibaca penuh di ledger, atau tertulis di kutipan. Kalau tidak, D5 menolak.
- "S-05" dan "C-12" tidak dianggap nomor issue.
- Self-test: 63/63 lulus, termasuk empat uji baru.
- Draft koreksi v40 (D-2026-09-23-02) tetap PASS.
