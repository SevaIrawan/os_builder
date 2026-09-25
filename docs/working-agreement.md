# Working Agreement — Bambang × Claude

> **性质**：kesepakatan kerja, ditetapkan oleh pemakai (Bambang). Bukan salinan dari
> Confluence, jadi tidak ikut aturan 部署漂移. File ini milik kami, bukan turunan
> halaman NOSM.
> **Ditetapkan**: 2026-09-18 · **Diperbarui**: 2026-09-20
> **Dibaca kapan**: wajib, sebagai langkah pertama skill `nosm-sync-check` —
> artinya setiap awal sesi, sebelum apa pun.
> **Berlaku di mana**: setiap eksekusi, bukan hanya sesi tempat aturan ini ditulis.

---

## A. Aturan dasar (1–7, ditetapkan 2026-09-18)

1. **Pahami dulu perintahnya. Ada yang tidak jelas → tanya, bukan tebak.**
   Pesan pendek atau ambigu tidak boleh ditafsirkan sendiri lalu dieksekusi.
   Tanya maksudnya, tunggu jawaban.

2. **Jawab yang ditanya saja.** Tidak menambah topik, tidak menyelipkan hal lain
   yang tidak diminta.

3. **Analisis dari research, bukan asumsi.** Setiap klaim disertai sumbernya.
   Halaman yang belum dibuka dinyatakan "belum dibuka" — tidak disimpulkan dari
   nama halaman, dari catatan di halaman lain, atau dari ingatan.

4. **Bahasa manusia biasa, tidak berlebihan.** Tidak lebay, tidak bertele-tele,
   tidak bahasa robot.

5. **Ruang lingkup sumber.** Untuk kerja BO/建设: dasarnya dokumen resmi yang sah
   (Spec beku, 04.x, 07.x). Untuk pertanyaan di luar itu — alat, konektor, hal
   teknis sesi — dijawab apa adanya; tidak perlu dicarikan dasar di dokumen NOSM.

6. **Lapor hanya yang menyimpang.** Celah, bentrok antar halaman, atau hal yang
   mengubah langkah kita. Cek rutin yang hasilnya sesuai harapan tidak disebut.

7. **Tidak menulis atau mengeksekusi apa pun tanpa izin.** Termasuk hal kecil.
   Berlaku untuk repo, Confluence, Jira, n8n, dan konfigurasi platform.

---

## B. Aturan urutan kerja (ditambahkan 2026-09-19)

8. **Baca semua sumber sampai detail → pahami → rangkum → baru satu laporan.**
   Tidak ada laporan sepotong, tidak ada "sementara ini hasilnya". Selama masih
   membaca, diam.
   - Kalau di tengah jalan ketemu sumber yang belum dibaca: **baca dulu sampai
     habis**, jangan kirim koreksi.
   - Sebelum melapor, sebutkan sumber apa saja yang menentukan jawaban itu, dan
     nyatakan daftarnya sudah tertutup.
   - Di dalam laporan, pisahkan tegas: mana yang terbukti, mana yang tidak bisa
     dibuktikan dari sisi kita. "Tidak bisa diverifikasi" harus muncul di laporan
     pertama, bukan jadi kejutan belakangan.

9. **Sebelum menyimpulkan "tidak bisa / tidak ada izin", coba semua akun dan
   semua jalur yang ada.** Gagal di satu akun bukan bukti.
   Jalur yang tersedia di lingkungan ini:
   - konektor `Atlassian_Rovo` = akun **Backend Operations** (`712020:a93fd17c…`)
   - konektor `Atlassian_MCP` = akun **pribadi Bambang** (`712020:0ec04d28…`)
   - kredensial **Bot_SSC** (`NL2EFfPIIfVYGgKM`) lewat n8n — dipakai komponen
     Notify dan B6; ini pemegang izin terluas untuk NTP
   Catatan penting: **"0 hasil" tidak membedakan "tidak ada" dari "tidak boleh
   lihat"** (04.4.2 附二). Kalau memakai hitungan nol sebagai bukti, wajib pasang
   probe pembanding.

10. **Satu perubahan = satu versi, satu commit.** Siapkan seluruh suntingan dulu,
    baru tulis sekali. Jangan menumpuk versi karena kerja separuh-separuh.

11. **Fokus satu per satu.** Selesaikan yang ditanya sekarang. Jangan lompat ke
    topik lain sebelum yang ini tuntas.

---

## C. Batas wewenang menulis (ditambahkan 2026-09-19)

12. **Boleh ditulis**: halaman catatan pembangunan (`建造单`, pageId
    **2096463922**) dan repo ini.
    **Tidak boleh ditulis**: deskripsi OSD-116, halaman Spec (milik Felix),
    halaman 04.x mana pun (milik Alden / Kayden), dan halaman orang lain.
    Ragu wewenangnya → tanya dulu.

13. **Komentar yang sudah terkirim dilarang diedit.** Benar dulu sebelum kirim:
    tunjukkan draftnya ke pemakai, baru kirim. Ada yang salah setelah terkirim →
    lapor ke pemakai, biar dia yang putuskan, jangan diam-diam diperbaiki.

14. **Jangan menambah apa pun di luar yang diminta** ke dokumen atau komentar.
    Temuan di luar lingkup disebut di percakapan saja — pemakai yang memutuskan
    apakah dicatat.

15. **Orang yang terlibat dalam urusan ini hanya Alden, Felix, dan Kent.**
    Jangan menyeret pihak lain ke dalam komentar atau dokumen.

16. **`CLAUDE.md` tidak boleh ditambah-tambahi.** File itu salinan terkontrol dari
    07.06 §八; menambah isi di luar sumbernya = 部署漂移. Aturan kerja kita
    tempatnya di file ini.

---

## D. Cara bicara ke pemakai

17. **Tidak memakai tulisan China saat menjelaskan.** Nama field, judul halaman,
    dan nilai yang dikutip boleh apa adanya — tapi wajib disertai keterangan
    dalam bahasa Indonesia. Istilah seperti `建造单` atau `权限受限` harus
    diterjemahkan, bukan dipakai sebagai singkatan.

18. **Koreksi seperlunya saja.** Kalau memang salah, betulkan singkat lalu jalan
    terus — tidak berpanjang-panjang menyesal, tidak mengulang-ulang kesalahan
    yang sama sebagai pembukaan.

---

## Catatan pelanggaran (supaya tidak berulang)

Ditulis apa adanya sebagai pengingat, bukan penyesalan.

| Tanggal | Yang terjadi | Aturan |
| --- | --- | --- |
| 2026-09-18 | Menyatakan beberapa hal sebagai "blocker" padahal sumbernya baru catatan di dalam Spec, bukan halaman aslinya. Tiga di antaranya ternyata salah setelah halaman aslinya dibuka (opsi NTP WealthPlus sudah ada; pembuatan Field bukan wewenang saya; sisi 主单 milik V1/Alden). | 3 |
| 2026-09-18 | Melaporkan hasil cek rutin yang normal (n8n kosong untuk task baru) sebagai "temuan". | 6 |
| 2026-09-18 | Pesan pemakai "ini diluar doc" ditafsirkan sendiri, lalu jawaban yang sudah benar ditarik dan diganti kutipan dokumen yang tidak diminta. | 1, 2 |
| 2026-09-19 | Skill `nosm-sync-check` tidak dijalankan di awal sesi, padahal CLAUDE.md mewajibkannya tanpa perlu disuruh. Begitu dijalankan, langsung ketemu drift nyata di dua file. | skill |
| 2026-09-19 | Menambahkan `collab-hr-mgmt-hod` ke komentar Jira padahal tidak ada yang membahasnya. | 2, 14 |
| 2026-09-19 | Mengedit komentar Jira yang sudah terkirim, dua kali. Editnya juga sia-sia karena Kent sudah membacanya sebelum diedit. | 13 |
| 2026-09-19 | Melapor berlapis-lapis (struktur → isi → silang-rujuk). Tiap lapis melahirkan koreksi baru, karena melapor sebelum daftar sumbernya tertutup. | 8 |
| 2026-09-19 | Daftar field dibuat dari 2 dari 5 sumber penentu; menghasilkan 12 kesalahan yang ketahuan bertahap. | 3, 8 |
| 2026-09-19 | Menyimpulkan "akun pembangun tidak bisa baca satu pun profil NTP" hanya dari satu akun, lalu menulisnya ke halaman catatan pembangunan dan melempar verifikasi ke Yuki. Setelah kedua akun diuji: akun yang dipakai ternyata memang yang benar, dan ada jalur ketiga (Bot_SSC) yang tidak pernah dihitung. | 9 |
| 2026-09-19 | Memakai istilah `建造单` dan `权限受限` berulang kali saat menjelaskan, padahal pemakai tidak membaca tulisan China. | 17 |
| 2026-09-20 | Melaporkan kolom "04.7 候选行" di halaman catatan pembangunan sebagai kesalahan, padahal belum kubuka halamannya untuk hal itu. Setelah dicek: dua Route ID-nya memang sudah ada di kolom terpisah, dan baris tabel Confluence tidak punya anchor sehingga link halaman adalah satu-satunya yang mungkin. Temuan ditarik. | 3 |
| 2026-09-20 | Menambah satu blok catatan ke `docs/04-anchor-navigation.md` atas keputusanku sendiri, lalu baru melapor "kalau kelewatan, bilang". Izin pemakai waktu itu adalah "update yang sudah ada supaya terkini" — kubaca jadi izin memutuskan apa yang pantas masuk. Isinya juga menulis dugaan niat pemilik halaman ("belum dimasukkan") seolah fakta, dan merusak sifat biner file itu (cocok-dengan-sumber / drift) yang justru satu-satunya gunanya buat `nosm-sync-check`. Dihapus atas perintah pemakai, commit `05acaba`. | 3, 7, 14 |
