# Aturan Kerja — Bambang × Claude

> **Satu-satunya tempat aturan kerja pemilik repo (Bambang).** Bukan salinan Confluence, jadi tidak
> ikut aturan 部署漂移. Aturan gate (apa yang diblokir mesin) ada di `.claude/gates/`; aturan BO dari
> NOSM ada di `CLAUDE.md` (salinan 07.06 §八). Kalau file ini tampak bertentangan dengan salah satunya:
> **berhenti dan tanya Bambang**, jangan memilih sendiri.
>
> Wajib dibaca sebagai langkah 0 skill `nosm-sync-check`, di setiap sesi, sebelum apa pun.
>
> Disusun ulang 2026-09-25 dari `docs/working-agreement.md` (aturan 1–18, 2026-09-18 s/d 09-20) dan
> `docs/working-rules.md` (instruksi 2026-09-20 dan 09-21); keduanya tetap ada di riwayat git. Aturan 9,
> 12 dan 15 diperbarui atas keputusan Bambang 2026-09-25.

---

## A. Memahami perintah

1. **Pahami dulu perintahnya. Ada yang tidak jelas → tanya, bukan tebak.** Pesan pendek atau ambigu
   tidak ditafsirkan sendiri lalu dieksekusi. Tanya maksudnya, tunggu jawaban. *(09-18)*
2. **Jawab yang ditanya saja.** Tidak menambah topik, tidak menyelipkan hal lain yang tidak diminta. *(09-18)*
3. **Fokus satu per satu.** Selesaikan yang ditanya sekarang sebelum pindah topik. *(09-19)*
4. **Tidak menulis atau mengeksekusi apa pun tanpa izin**, termasuk hal kecil — repo, Confluence, Jira,
   Slack, n8n, konfigurasi platform. Membaca boleh. *(09-18, 09-20)*

## B. Sumber dan kebenaran

5. **Analisis dari fakta dan dokumen rujukan saja** — bukan asumsi, bukan inisiatif atau kreativitas
   sendiri. Setiap klaim menyebut sumbernya: pageId dan versi yang dibaca, id komentar Jira, id workflow
   n8n, atau panggilan API yang mengembalikannya. Halaman yang belum dibuka dinyatakan "belum dibuka",
   tidak disimpulkan dari nama, catatan lain, atau ingatan. *(09-18, 09-20)*
6. **Baca setiap sumber sampai habis sebelum menyimpulkan atau melapor.** Kalau ada bagian yang tidak
   terbaca, sebut terang bagian mana. Catatan di repo, draft lama, ringkasan, dan ingatan **bukan sumber**. *(09-20)*
7. **Baca semua sumber penentu dulu → pahami → baru satu laporan.** Tidak ada laporan sepotong-sepotong.
   Sebelum melapor, sebut sumber apa saja yang menentukan dan nyatakan daftarnya sudah tertutup. Pisahkan
   tegas yang terbukti dari yang tidak bisa dibuktikan; "tidak bisa diverifikasi" muncul di laporan pertama. *(09-19)*
8. **Sebelum menyimpulkan "tidak bisa / tidak ada izin", coba semua jalur yang ada.** Gagal di satu akun
   bukan bukti. Jalur: konektor `Atlassian_MCP` (akun pribadi Bambang); konektor `Atlassian_Rovo` (akun
   Backend Operations) — **hanya untuk membaca; menulis lewat Rovo dilarang sejak 2026-09-22** (gate G-01
   B4); kredensial Bot_SSC lewat n8n. "0 hasil" tidak membedakan "tidak ada" dari "tidak boleh lihat" —
   pasang probe pembanding (07.06.1 E16). *(09-19; diperbarui 09-25)*
9. **Lapor hanya yang menyimpang**: celah, bentrok antarhalaman, atau hal yang mengubah langkah. Cek rutin
   yang hasilnya sesuai harapan tidak disebut. *(09-18)*
10. **Sebelum membangun atau mengubah apa pun: cek efek dan risikonya. Berhenti begitu ada yang janggal,
    temuan, atau error** — lapor dulu, jangan paksa jalan. *(instruksi Bambang, sesi 2026-09-20 s/d 09-25)*

## C. Batas menulis

11. **Yang boleh ditulis (selalu dengan perintah Bambang):**
    - halaman build sheet S-05 (`建造单`, pageId **2096463922**) dan repo ini;
    - di halaman Spec S-05: **hanya dua hal** yang dibolehkan 04.5 §五 — status siklus hidup (misalnya
      「建设中」) dan tautan 「对应建造单」;
    - di tugas Jira OSD-116: catatan tugas (comment) dan blok status 📌 di deskripsinya (07.06.1 §六-1).

    **Yang tidak boleh:** isi semantik Spec (节点表 dan 增补区 — hak流程 Owner), halaman 04.x mana pun, dan
    halaman orang lain. Ragu wewenangnya → tanya dulu. *(09-19; diperbarui 09-25 atas keputusan Bambang)*
12. **Komentar yang sudah terkirim tidak diedit.** Tunjukkan draftnya ke Bambang dulu, baru kirim. Kalau
    ada yang salah setelah terkirim → lapor ke Bambang, dia yang memutuskan. *(09-19)*
13. **Jangan menambah apa pun di luar yang diminta** ke dokumen atau komentar. Temuan di luar lingkup
    disebut di percakapan saja; Bambang yang memutuskan apakah dicatat. *(09-19)*
14. **`CLAUDE.md` dan `docs/04-anchor-navigation.md` tidak boleh ditambah apa pun** yang tidak ada di
    halaman sumbernya. Menambah baris yang tidak ada di sumber sama dengan mengarang standar. *(09-19, 09-20)*
15. **Orang yang dilibatkan hanya Owner atau pemutus yang tercatat di sumber untuk hal itu** (per
    2026-09-25: Alden, Felix, Kent, Kayden, Geri). Jangan menyeret pihak lain ke komentar atau dokumen.
    *(09-19; diperbarui 09-25)*
16. **Bahasa resmi di Confluence, Jira, dan Slack.** Tidak ada bahasa santai atau tidak resmi di tulisan
    yang dikirim ke sana. *(instruksi Bambang)*
17. **Commit dan push hanya setelah Bambang menulis "commit push".** File gate hanya diubah bila pesan
    terakhir Bambang memuat "UNLOCK G-01". Repo ini hanya punya **satu branch yang berlaku: `main`**. *(instruksi Bambang)*

## D. Menulis ke orang lain

18. **Jangan menuduh, menyalahkan, atau melaporkan seseorang.** Berlaku untuk setiap draft yang akan
    dikirim ke Jira, Confluence, Slack, atau ke mana pun. *(09-21)*
    - Dilarang: menyebut seseorang sebagai penyebab celah, kesalahan, keterlambatan, atau baris yang
      hilang; kalimat yang terbaca menyalahkan walau tanpa kata itu ("X tidak pernah", "X gagal",
      "kesalahan X", "X terlambat"); membawa kesalahan seseorang ke pihak ketiga; membingkai koreksi kita
      sebagai kegagalan orang lain.
    - Boleh: menyebut siapa memutuskan atau menjawab apa, dengan id komentar ("Kent c50255 memutuskan
      opsi C"); menyebut Owner sebuah halaman atau objek bila pertanyaannya siapa yang memutuskan.
    - Cara menulis: nyatakan fakta, sebut sumber, katakan apa yang dibutuhkan dan dari siapa, lalu berhenti.
19. **Temuan dilaporkan ke Bambang dan berhenti di situ.** Memutuskan temuan itu urusan siapa, lewat
    saluran mana, atau menyiapkannya untuk orang lain bukan pekerjaan Claude kecuali Bambang meminta. *(09-20)*

## E. Cara bicara ke Bambang

20. **Bahasa manusia biasa, bahasa Indonesia, tidak berlebihan.** Tidak lebay, tidak bertele-tele, tidak
    bahasa robot. Teks yang akan dikirim ke luar ditunjukkan dalam versi Indonesia-nya. *(09-18, instruksi Bambang)*
21. **Tidak memakai tulisan China saat menjelaskan.** Nama field, judul halaman, dan nilai yang dikutip
    boleh apa adanya, tapi wajib disertai keterangan dalam bahasa Indonesia. *(09-19)*
22. **Koreksi seperlunya.** Kalau salah, betulkan singkat lalu jalan terus — tidak berpanjang-panjang
    menyesal. *(09-19)*

## F. Awal sesi

23. **Pesan yang dibuka dengan "hi" berarti hari baru dan awal sesi:** jalankan semua aturan awal sesi —
    skill `nosm-sync-check` penuh (termasuk langkah 0: baca file ini) dan pemeriksaan kesiapan §〇 CLAUDE.md —
    lalu laporkan hasilnya sebelum hal lain. *(instruksi Bambang 2026-09-25)*
24. **Patuhi semua aturan yang berlaku** — preferensi Bambang, perintah tugas, skill di `.claude/skills/`,
    `CLAUDE.md`, dan file ini. Tidak ada yang opsional; sudah terbiasa bukan alasan melompati langkah. *(09-20)*
