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

## Menutup celah `git commit -a` (perintah Bambang: "UNLOCK G-01 tutup celah git commit -a itu")

- Celahnya: hook hanya memeriksa nama file yang tertulis di perintah Bash. `git commit -a` (commit be9c345) memasukkan `docs/ledger/_draft-registry.json` ke commit tanpa menyebut nama file itu, jadi lolos.
- Perbaikan di `scripts/hooks/pre_tool.py`: untuk setiap perintah git yang bisa memasukkan, mengembalikan, atau membuang perubahan (add, commit, stash, checkout, restore, reset, clean, rm, mv, pull, merge, dan lain-lain), hook membaca `git status` langsung. Kalau ada file gate yang berubah dan perintah itu akan menyentuhnya, perintah diblokir kecuali pesan terakhir owner memuat "UNLOCK G-01".
- Yang diblokir: `git commit -a` / `-am` / `--all`, `git add -A` / `.` / `-u` / folder yang mencakup file gate, `git commit` biasa jika file gate sudah di-stage, `git stash`, `git checkout -- .`, `git reset --hard`, `git -C . commit -a`, `sh -c "git commit -a"`, `cd . && git commit -a`.
- Yang tetap boleh: `git add <path file sendiri> && git commit -F ...`, `git status`, `git diff`, `git log`, `git push`.
- Akibatnya: `_draft-registry.json` ditulis ulang oleh gate setiap kali draft PASS, jadi meng-commit file itu sekarang butuh "UNLOCK G-01".
- Sisa batas (dicatat di `known_limits` G-01): program non-git yang menulis file gate tanpa nama path-nya muncul di perintah tidak terdeteksi.
- Self-test: 84/84 lulus (63 lama + 21 uji git baru).

## Menutup celah program non-git (perintah Bambang: "UNLOCK G-01 tutup juga celah program non-git itu")

- Celahnya: program yang menulis file gate tanpa nama path-nya muncul di perintah tidak bisa dikenali sebelum jalan.
- Perbaikan: salinan resmi (sealed copy) semua file gate disimpan di luar repo (`~/.claude/g01-state/`, kode `scripts/hooks/_guard.py`). File gate dibandingkan dengan salinan itu:
  - sebelum setiap tool call (`pre_tool.py`),
  - setelah setiap Bash / Write / Edit (hook baru `post_guard.py`, didaftarkan di `.claude/settings.json`),
  - saat giliran berakhir (`stop.py`).
- Kalau ada yang beda dan pesan terakhir owner tidak memuat "UNLOCK G-01": isi resmi dikembalikan (file baru dihapus, file terhapus dikembalikan), lalu tool call ditolak atau giliran tidak boleh selesai, dengan daftar file yang dikembalikan.
- Dengan "UNLOCK G-01": keadaan baru disimpan sebagai salinan resmi.
- Daftar file yang dilindungi diambil dari lexicon versi resmi, jadi mengubah `lexicon.json` tidak bisa melepas perlindungan.
- Tulisan sah oleh hook sendiri (`_draft-registry.json` oleh Stop, `consumed.jsonl` oleh PostToolUse) langsung disimpan ke salinan resmi, jadi tidak dikembalikan.
- Perintah yang menyebut `g01-state` diperlakukan sebagai menyentuh file gate.
- Batas yang tersisa (dicatat di `known_limits` G-01):
  1. Perubahan dibatalkan di hook berikutnya, bukan dicegah; selama perintah atau job latar itu masih jalan, perubahannya ada.
  2. Hook, salinan resmi, dan model berjalan sebagai user OS yang sama. Program yang sengaja dibuat untuk mematikan kode hook atau salinan resmi dalam satu langkah tidak bisa dihentikan. Pengaman ini untuk kecelakaan dan jalan pintas, bukan serangan yang disengaja.
  3. Salinan resmi hilang bersama container, lalu dibuat ulang dari clone baru di hook pertama.
- Self-test: 95/95 lulus (84 lama + 11 uji baru: file diubah, file baru, file dihapus, lexicon dipersempit, perubahan terdeteksi di tool call berikutnya dan di Stop, perubahan di bawah UNLOCK tetap, tulisan hook tidak dikembalikan, perintah yang menyebut salinan resmi diblokir).

## Uji langsung pengaman program non-git (perintah Bambang: "Jalankan uji langsung pengaman itu sekarang")

Dijalankan di repo asli, tanpa UNLOCK G-01 di pesan terakhir owner. Alat uji: program kecil di scratchpad (`probe.py`) yang menulis ke file gate. Nama file gate tidak muncul di perintah Bash (`python3 <scratchpad>/probe.py`).

- Kondisi awal: hash gabungan `SKILL.md` nosm-sync-check + `lexicon.json` = `bb3628c9612450890a8e02ccdefdc366facb8fa41d348f9e069a73684b31284a`; `scripts/hooks/live_probe.py` tidak ada; `git status` bersih.
- Uji 1, program jalan biasa: menambah satu baris ke `SKILL.md` dan membuat `scripts/hooks/live_probe.py`.
  - PostToolUse `post_guard.py` langsung menolak: "SKILL.md (changed, put back)" dan "live_probe.py (new file removed)".
  - Sesudahnya: hash kembali `bb3628c9…`, `live_probe.py` tidak ada, `git status` bersih.
- Uji 2, program jalan di latar belakang: menunggu 5 detik, lalu menambah baris kosong ke `lexicon.json` saat tidak ada tool call yang berjalan.
  - Stop hook menangkapnya saat giliran mau berakhir: "lexicon.json (changed, put back)", dan giliran tidak boleh selesai.
  - Pengingat git sistem ("There are uncommitted changes") muncul bersamaan, karena mengecek repo sebelum lexicon selesai dikembalikan.
  - Sesudahnya: hash kembali `bb3628c9…`, `git status` bersih.
- Kesimpulan: kedua jalur (sesudah perintah, dan di akhir giliran) bekerja di sesi nyata. Uji 2 juga memperlihatkan batas (a) di `known_limits`: perubahan sempat ada dari saat job latar menulis sampai Stop hook mengembalikannya. Perubahan dibatalkan, bukan dicegah.
- Temuan sampingan saat mencatat hasil ini: perintah `git commit -m "..."` yang pesannya memuat tanda kurung ditolak dengan alasan "could not be parsed", padahal tidak ada file gate yang berubah. Pemeriksaan git menolak perintah yang tidak bisa diurai sebelum mengecek apakah ada file gate yang berubah. Aman, tapi terlalu ketat. Memperbaikinya perlu UNLOCK G-01.

## Perbaikan pemeriksaan git yang terlalu ketat (perintah Bambang: "UNLOCK G-01 perbaiki pemeriksaan git yang terlalu ketat itu")

- Penyebab 1: perintah dipotong di setiap `(`, `)`, `;`, `|`, `&` sebelum tanda kutip dibaca, jadi tanda kurung di dalam pesan commit memecah kutipan dan perintah dianggap tidak bisa diurai.
  - Perbaikan: perintah sekarang diurai dengan memperhatikan tanda kutip (`shlex` dengan `punctuation_chars`). Tanda kurung di dalam kutipan dibaca sebagai teks, di luar kutipan sebagai pemisah perintah. Backtick dan `$( )` tetap dibaca sebagai perintah git.
- Penyebab 2: perintah yang tidak bisa diurai ditolak sebelum dicek apakah ada file gate yang berubah.
  - Perbaikan: `git status` dicek dulu. Kalau tidak ada file gate yang berbeda dari HEAD, perintah git apa pun diizinkan, karena tidak ada file gate yang bisa terbawa atau terbuang. Perintah yang tidak bisa diurai hanya ditolak kalau ada file gate yang berubah.
- Self-test: 103/103 lulus (95 lama + 8 uji baru):
  - boleh saat bersih: pesan dengan tanda kurung, kutipan tidak seimbang;
  - boleh saat ada file gate berubah: `git add <file sendiri> && git commit -m "... (…; … | …)"`;
  - tetap diblokir saat ada file gate berubah: kutipan tidak seimbang, `` `git stash` ``, `$(git commit -a)`, `(git commit -a -m "a (b) c")`, dua perintah dipisah baris baru.

## Uji langsung pemeriksaan git (perintah Bambang: "Jalankan uji langsung pemeriksaan git itu sekarang", lalu "Jalankan uji git sekarang")

Tahap 1, repo bersih, tanpa UNLOCK, dengan `--dry-run`:
- Lolos: `git commit --dry-run -m "Live test (parens; semicolon | pipe)"` (dulu ditolak "could not be parsed"), `git commit -a --dry-run`, `git add -A --dry-run`. Git menjawab "nothing to commit".
- Diblokir: `git add --dry-run scripts/hooks/pre_tool.py` (aturan lama: perintah menyebut file gate).

Tahap 2, satu baris kosong ditambahkan di akhir `lexicon.json` atas perintah "UNLOCK G-01 buat perubahan kecil di lexicon untuk uji itu" (tidak di-commit), lalu diuji tanpa UNLOCK:
- Diblokir, 6/6:
  - `git commit -a --dry-run`: "git commit -a / --all would commit"
  - `git add -A --dry-run`: "would stage"
  - `git add --dry-run .`: "pathspec covers"
  - `git stash`: "git stash runs while gate files have uncommitted changes"
  - `git commit -m "unbalanced quote`: "could not be parsed while gate files have uncommitted changes"
  - `` echo `git stash` ``: "git stash runs…"
- Lolos: `git add <draft sendiri> && git commit --dry-run -m "Live test (a; b | c)"`, `git status --short`, `git diff --stat`.
- Sesudahnya: baris uji masih ada, `.git/refs/stash` tidak ada (tidak ada yang masuk stash).
- Dua blokir berlebihan ditemukan (hanya terjadi saat ada file gate berubah; arahnya memblokir, tidak meloloskan):
  1. `git stash list` diblokir, padahal hanya membaca.
  2. `echo "git exit=$?"` diblokir: teks berkutip yang memuat kata "git" diurai sebagai perintah git.

## Perbaikan dua blokir berlebihan (perintah Bambang: "UNLOCK G-01 buang baris uji, perbaiki dua blokir itu, lalu catat")

- Baris uji di `lexicon.json` dibuang (`git checkout`), repo bersih lagi.
- Perbaikan 1: sub-perintah yang hanya membaca tidak diblokir: `git stash list`, `git stash show`, `git worktree list`, `git config --get / --list`.
- Perbaikan 2: teks berkutip hanya diurai sebagai perintah bila memang dijalankan shell (`sh`/`bash`/`zsh`/`dash`/`ksh -c`, `eval`, `su`, `script`) atau memuat `$( )` / backtick. `echo "git exit=$?"` dan pesan commit yang menyebut kata git kini dianggap teks.
- Self-test: 114/114 lulus (103 lama + 11 uji baru):
  - lolos saat ada file gate berubah: `git stash list`, `git stash show`, `git status --short; git stash list | wc -l`, `... ; echo "git exit=$?"`, `git commit -m "fix the git gap (stash list)"` setelah `git add` file sendiri;
  - tetap diblokir saat ada file gate berubah: `git stash push`, `git stash pop`, `git commit -m "msg $(git stash)"`, `bash -c 'git add -A'`, `eval "git commit -a -m x"`, `` echo "`git stash`" ``.
- Belum diuji langsung di sesi nyata, karena uji langsung butuh file gate yang berubah dan pesan tanpa UNLOCK, dan baris uji sudah dibuang.
