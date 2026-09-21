# Daftar Aksi — OSD-116 / S-05 (Penanganan Disiplin & Perbaikan Kinerja)

> **Sifat**: file kerja kami. **Bukan** salinan halaman Confluence, jadi **tidak** tunduk
> aturan 部署漂移 (deployment drift) dan tidak akan dihapus `nosm-sync-check`.
> **Satu-satunya file daftar aksi.** Kalau ada aksi baru, masuk ke sini — jangan bikin file lain.
>
> **Terakhir diperbarui**: 2026-09-21 ~19:00 WIB
>
> **Catatan branch**: file ini lahir di branch `claude/new-session-3nlq6e` (2026-09-20). Pembaruan
> 2026-09-21 dikerjakan di branch `claude/new-session-s525sx`; kedua branch belum digabung.

---

## Cara pakai

Tiap baris punya ID. Panggil ID-nya kalau mau aku kerjakan, bahas, atau tutup.
Contoh: *"kerjakan A-02"*, *"A-04 tidak usah dulu"*, *"B-01 sudah dibalas Kent"*.

Empat status:

| Status | Artinya |
|---|---|
| `SEGERA` | Bisa dikerjakan sekarang, tidak ada yang menghalangi, tinggal perintah |
| `MENUNGGU ORANG` | Terhalang jawaban orang lain (Kent / Felix / Alden / Kayden) |
| `MENUNGGU KAU` | Terhalang keputusan Bambang, bukan orang luar |
| `SELESAI` | Sudah beres dan sudah ada buktinya |

**Aturan file ini**: tidak ada baris yang pindah ke `SELESAI` tanpa bukti (nomor commit,
versi halaman, atau nomor komentar). Tidak ada baris ditulis dari dugaan — tiap baris
harus punya sumber yang bisa dibuka.

---

## A · SEGERA

Sudah bisa jalan. Menunggu perintah kau saja.

| ID | Aksi | Dari mana asalnya | Catatan |
|---|---|---|---|
| A-03 | Koordinasi daftar jabatan NTP dengan Alden dan Felix | Kent, instruksi awal di OSD-116 | Jalurnya kini lewat tiket pemeliharaan GOV (gelombang perubahan F-172/F-173/F-176, 2026-09-19, disetujui Kayden). Blocker-nya **tidak** hilang sendiri — lihat B-03. **2026-09-21: tidak ada perubahan** |
| A-04 | Konfigurasi SLA — **hanya bagian yang tidak terhalang**: bangun 15 komponen pemindai n8n dalam keadaan **mati (inactive)**, plus aku susun panduan tombol-per-tombol untuk sisi JSM | Kent, OSD-116 c50227 butir 7: *"no ruling needed, follow 04.4 §8.1"* | Sumbernya sudah kubaca penuh 2026-09-20 (lihat D-11). Isi A-04 = mengonfigurasi 16 baris tabel C (rincian SLA) di Spec beku. Pembagian mesin per 04.4 §8.1 (garis putus: objeknya di dalam SSCSD atau tidak): **1 baris** pakai mesin JSM bawaan (C-1), **15 baris** pakai pemindai n8n. Membangun komponen n8n yang masih mati **tidak perlu izin siapa pun** — 07.06.1 §六-2: yang memutuskan pengembang sendiri. **Yang TIDAK termasuk baris ini**: menyalakan komponen (B-10), menyentuh SLA di SSCSD (B-09). Catatan: angka batas waktu dibaca langsung dari tabel C Spec, bukan dari tabel data n8n (04.6 §四) — jadi tidak perlu minta tabel data baru. **2026-09-21: tidak ada perubahan.** ⚠️ Tapi dua aturan yang mengikat cara membangunnya berubah hari ini — lihat A-06 dan A-07 |
| A-07 | Bangun gudang arsip 纪律处分记录 sesuai N5 (opsi C: read-port hanya akun layanan, di node tertentu, tanpa browse manusia) | Kent OSD-116 **c50255**: 「Build the library per N5」 | ⚠️ **Baca dulu hubungannya dengan B-02**: 判据 baris blocker 建造单 no.1 minta baris 04.1 §一 berubah dulu jadi 「已裁决｜待创建｜{key}」 atau 「运行中」. 04.1 masih v46, barisnya masih 「候选｜待N5」. Apakah gudangnya boleh dibangun sebelum key terdaftar — **belum jelas, jangan diputuskan sendiri** |

**Yang pindah keluar dari bagian ini**: A-01 → D-12 · A-02 → D-13 · A-05 → D-14.
**A-06 dicabut 2026-09-22 → B-16.** Ia ditaruh di sini atas dasar Kent c50255 saja, tanpa diadu ke
04.3 §六. Setelah 04.3 v33 §六 dibaca langsung, ternyata N28 方向 2 **bukan** hal yang tidak menunggu
siapa pun — dua-duanya terkunci. Baris 19 建造单 sebenarnya sudah mencatatnya sejak awal.

## B · MENUNGGU ORANG

Bukan kita yang menghalangi.

🔴 **Fakta yang mengikat seluruh baris Alden di bawah**: Alden **belum berkomentar di OSD-116 sejak
2026-09-10**. Diverifikasi 2026-09-21: namanya tidak muncul di 60 komentar terbaru, yang mundur sampai
2026-09-10 12:58.

| ID | Menunggu siapa | Soal apa | Sejak | Kalau dia jawab, apa yang terbuka |
|---|---|---|---|---|
| B-02 | **Kayden (sisi dia)** | Konversi baris di 04.1 dan 04.8 untuk gudang arsip mandiri (putusan c50244 butir 1, opsi C) | 2026-09-20 | Baris blocker N13/N26/N27 di halaman catatan pembangunan bisa diperbarui. **2026-09-21**: Kent c50257 menegaskan ini sisi Kayden — 「04.1/04.8 转正式登记归你侧派人」 — dan dia akan mengawal sampai tutup. **Dicek hari ini: 04.1 masih v46, 04.8 masih v21, baris 04.1 §一 masih 「候选｜待N5」. Belum bergerak** |
| B-03 | **Alden + Felix** | Daftar jabatan NTP lewat tiket pemeliharaan GOV | belum dimulai | A-03. **2026-09-21: tidak ada perubahan** |
| B-05 | **Alden** | Perluasan kemampuan pola 9 v5 itu sendiri | **sudah dikirim 2026-09-21 15:17** | N07 tidak bisa dibangun sesuai Spec beku tanpa ini. **Statusnya berubah**: dulu 「belum dikirim」, sekarang sudah — OSD-116 **c50279**, enam blok + empat add-on + catatan Data Table. **Belum dibalas.** 判据 baris blocker 建造单 no.3 berbunyi 「平台扩展组件能力并更新 04.4.1」 — 04.4.1 masih v13 |
| B-06 | **Felix** | Isi daftar penyimpangan untuk celah S-05 → proses keluar karyawan | 2026-09-20 | Spec beku mewajibkan penanganan sementaranya dicatat di sana. **Sekarang kosong dan kita tidak boleh mengarangnya.** 2026-09-21: Felix menjawab empat hal lain (c50261), yang ini tidak termasuk |
| B-07 | **Alden** | Kumpulan field jam kerja di NTP (jam masuk/pulang, istirahat, hari libur, cuti umum) | 2026-09-20 | 13 dari 16 baris tabel C berhitung "jam kerja". 04.4 §8.3 melarang angkanya ditulis di dokumen — wajib dibaca dari NTP saat jalan. 04.8 §五 barisnya masih placeholder: `ID 🔲 待 Alden 补`. 04.8 §四 melarang memakai field entitas yang belum terdaftar. **Bukan soal izin — barangnya memang belum ada.** 2026-09-21: 04.8 naik ke v21, tapi perubahannya cuma baris 员工 (sumber transisi sisi onboarding = S-02). Baris ini tidak bergerak |
| B-08 | **Alden** | Buku detail 04.9 untuk S-05 — **juga mengunci bagian 2 dari B-16** | 2026-09-20 | Aturan besi 04.9 §一 "tiga serangkai". **2026-09-21**: 04.9 naik v103 → **v106**. Yang ditambahkan: baris indeks 身份件 dan pembaruan baris keluarga Grade. **Tidak ada buku baru untuk S-05** — dibaca dari diff v103→v106 |
| B-09 | **Alden** | Konfigurasi SLA di SSCSD, berikut **dua pertanyaan risiko** | 2026-09-20 | 04.1 §一: Owner SSCSD = Alden. 04.1 §六: konfigurasi konkret SSCSD adalah lingkup V1 — sisi kita *"hanya mengeluarkan rancangan dan dokumen kebutuhan"*. Dua pertanyaannya: **①** C-1 dan C-2 sama-sama menghitung tiket induk di status **"Pending Approval" yang sama**, sedangkan "kembalikan untuk dilengkapi" adalah transisi di tempat — pemicu berbasis status berpotensi tidak menyala. **②** Menghapus nilai bawaan Jira 8/16 jam bisa mengenai alur lain; mungkin yang benar "tambah, jangan hapus". **2026-09-21: tidak ada perubahan** |
| B-10 | **Alden** (pengganti: **Kent**) | Izin menyalakan komponen n8n | belum berlaku | Baru berlaku setelah komponen A-04 jadi. 04.6 §3.6 langkah 4 + §3.4 butir 4 (Kent boleh menyetujui kalau Alden lewat 1 hari kerja). **2026-09-21 — ada putusan baru yang menyentuh baris ini**: di #nos-bo 2026-09-19 17:04 Kayden menetapkan 工程审关 (menyalakan) dan 验收关 (N13/N14) adalah **dua gerbang berbeda**, dan saat mencolok switch Alden 「只核 04.9 登记和守护配置，不再另审一套标准」. Dia juga menetapkan urutannya: 「切 active 放在 N14 通过之后、N15 上线之前」 dan akan menulisnya ke OS 开发流 Spec. ⚠️ **OS 开发流 Spec masih v39 dan belum memuatnya** — jadi ini putusan yang belum turun ke halaman, belum boleh dipakai sebagai dasar |
| B-11 | **Felix** | Batas waktu keseluruhan per permintaan | 2026-09-20 | Dua baris kita (`RT-HR-DISCIPLINARY-SUBMIT` dan `RT-HR-DISCIPLINARY-EVENT`) kolom SLA berakhir `请求级整单时限 🔲 未定占位`. **2026-09-21: 04.7 naik v45 → v46, tapi kedua baris S-05 tidak berubah satu huruf** (perubahan v46 hanya menyentuh baris RT-HR-RECRUITMENT-SUBMIT dan menambah RT-HR-RECRUITMENT-OFFERWITHDRAW). Masih menunggu |
| B-12 | **Alden** | Registrasi tujuh channel kolaborasi di **04.11** | 2026-09-20 | Pecahan dari B-04 yang tertinggal setelah bagian Felix tutup. Ini 判据② baris blocker 建造单 no.6. **04.11 masih v2 (2026-08-24)** dan tidak muncul di sapuan versi mana pun. 04.5 §七 butir 22 menjadikan ketiadaan baris 04.11 sebagai **gagal audit struktur**, bukan sekadar telat kerja |
| B-13 | **Felix** | Apakah 「延长周期」 PIP benar-benar cuma empat tingkat (15/30/60/90 hari), tanpa kemungkinan 「视情况」 di luar itu | 2026-09-21 | Ditanyakan Kent di akhir **c50290**. **Ini yang mengunci tipe field**: Kent menetapkan option, tapi tidak mengunci sebelum Felix menjawab. Alasannya tabel C-10 Spec cuma mendefinisikan frekuensi Check-in untuk empat tingkat itu |
| B-14 | **Kent** | Membuat 13 field, memasangnya ke screen, dan mendaftarkannya di 04.10 §三 dengan bukti | 2026-09-21 | Kent **c50290**: 「13 个 Jira 字段的创建、挂屏与 04.10 登记＝Schema Owner 侧（我方）；你（Bambang）负责 S-05 流程建设、消费这些字段」. Sebelum fieldnya ada, kita tidak bisa 回读 API apalagi mengonsumsinya |
| B-15 | **Kayden** | Apakah N28 perlu pengecualian terhadap 04.3 §六 互斥条 — **bagian 1 dari B-16** | 2026-09-21 | Dirutekan oleh **c50263** kita. 判据 baris blocker 建造单 no.19 minta dua hal: 执行身份 (sudah beres lewat c50244 → c50257 方向 2) dan 互斥条适用口径 (ini, belum). 04.3 dicek hari ini: masih v33, §六 tidak berubah |
| B-16 | **Kayden** (bagian 1) ＋ **Alden** (bagian 2) | **N28 方向 2 — dua-duanya terkunci, bukan pekerjaan yang bisa jalan sekarang.** Dasarnya Kayden **c50244**: 「方向 2 不动 Spec：Spec 执行者本就是 HR Ops & Data 角色，把转态权限配给该角色组即可；「忘记按」加一个守护件」 | 2026-09-22 (dicabut dari A-06) | **Bagian 1 · izin transisi → Kayden, sudah ada di B-15.** Spec v62 baris N28 menulis 执行者 ＝ HR Ops & Data **dan** 动作 ＝ 「04.3§六既有「Project Owner中止」出口，**不新造转态**」. Tapi 04.3 v33 §六 转态权限表 untuk pintu itu berbunyi 「**仅服务账号与该主单所在 Project 的 Owner**」 — HR Ops & Data tidak ada di dalamnya, sedangkan kalimat pembuka §六 「不设限制的转态视为配置未完成」. Jadi mengkonfigurasi sesuai c50244 justru menciptakan izin yang tabel itu tidak cakup. **Lebih keras lagi**, 撤回规则 §六: 「全关子单中只要有一张「已完成」，走模式五自动转「已完成」，**不得再走本条中止路径**」 — ini larangan, dan pemicu N28 (case 处理中 di tengah N08~N17) lazimnya sudah punya子单 已完成. **c50244 tidak menyentuh bagian ini.** Owner 04.3 ＝ Kayden; sudah dirutekan lewat c50263, belum dijawab. **Bagian 2 · 守护件 → Alden, sudah ada di B-08.** Membangun komponen mati memang keputusan sendiri (07.06.1 六-2), tapi 04.9 §一 铁律 「三位一体…缺任一项视为未完成」 dan 04.9 §三 cuma punya enam 分册 (平台／请假／员工离职／OS 开发流／Grade／Salary·Improvement·运维) — **tidak ada untuk S-05**, dan §三 tidak menulis siapa yang boleh membuat 分册 baru |

**Yang tutup hari ini**: B-01 → D-15 · B-04 → D-14 (sisanya jadi B-12).

## C · MENUNGGU KAU

Terhalang keputusan Bambang. Tidak ada orang luar yang perlu ditunggu.

| ID | Yang perlu diputus | Pilihannya | Dampak |
|---|---|---|---|
| C-07 | Kapan 16 butir daftar v34 ditulis ke 建造单 | sekarang / tunggu balasan | **Sudah kau putuskan 2026-09-21**: tampung di repo, satu kali tulis, pemicunya balasan terbaru dari Felix/Alden/Kayden/Kent. Dicatat di `docs/pending-buildsheet-updates.md`. Baris ini disimpan sebagai catatan putusan, bukan pertanyaan terbuka |

**Yang tutup hari ini**: C-01 → D-12 · C-04 → D-16 · C-05 → D-17 · C-02 dan C-03 → gugur (D-18).

## D · SELESAI

| ID | Aksi | Bukti |
|---|---|---|
| D-01 | Baca ulang penuh seluruh sumber penentu (seri 04, seri 07, kontrak notifikasi, Spec S-05) dan catat versi hidupnya per 2026-09-20 | Tercatat di halaman catatan pembangunan v31, blok tanggal 2026-09-20 |
| D-02 | Perbarui halaman catatan pembangunan dengan 11 sisipan hasil baca ulang; tidak ada satu pun teks lama dihapus | Halaman `2096463922` v30 → **v31** |
| D-03 | Betulkan versi Spec yang tertulis di halaman: hidup di **v62**, bukan v61 | bagian dari v31 |
| D-04 | Sinkronkan tanggal sinkron di `CLAUDE.md` dan `docs/04-anchor-navigation.md` ke 2026-09-20 | commit `9e0c3f1` |
| D-05 | Hapus blok catatan yang kutambahkan ke `docs/04-anchor-navigation.md` tanpa izin | commit `05acaba` |
| D-06 | Catat pelanggaran 2026-09-20 ke `docs/working-agreement.md` | commit `12f3742` |
| D-07 | Simpan draft permintaan Alden supaya bisa dipanggil lagi | commit `cda2e76` |
| D-08 | Baca dan analisis putusan Kayden c50244, termasuk apakah itu perintah ke kita (bukan — dialamatkan ke Kent) | hasil analisis ada di file draft, bagian usulan A/B/C |
| D-09 | Pastikan tidak ada task pembangunan NSE untuk Bambang — NSE-1240 tidak punya anak | dicek 2026-09-20 |
| D-10 | Buat folder kerja draft dan file daftar aksi ini | folder `docs/drafts/` + file ini |
| D-11 | Baca penuh sumber A-04 dan petakan 16 baris tabel C ke mesin penghitungnya | 2026-09-20. Yang dibaca: Kent c50227 butir 7 · 04.4 §八 (v31) · tabel C dan tabel node Spec S-05 (v62) · 04.2 §一 (v40) · 04.7 (v45) · 04.8 (v20) · 04.9 §一/§三 (v103) · 04.10 (v19) · 07.06 §6.2 (v30) · 07.06.1 §三/§四/§六 (v33) · 04.6 §3.6/§3.8/§四 (v20) · 04.1 §一/§三/§五/§六 (v46). Juga dicek: akun pribadi tidak melihat SSCSD; akun layanan melihatnya |

---
| D-12 | Kirim permintaan gabungan perluasan pola 9 ke Alden (A-01, dan ini sekaligus menjawab C-01) | OSD-116 **c50279**, 2026-09-21 15:17 +07 → dikirim ke OSD-116, yaitu pilihan (a) di C-01. ⚠️ Teks yang dikirim **bukan** draft `D-2026-09-20-01` — disusun ulang pada sesi 2026-09-21; draft lama tetap DITAHAN |
| D-13 | Lempar 3 item field yang masih terbuka ke Felix sebagai pertanyaan Spec (A-02) | OSD-116 **c50250**, 2026-09-21 06:26 → **sudah dijawab** Felix di **c50261 butir 2**: (a) `HR判定依据` satu catatan menerus append-only dengan timestamp + tanda node asal; (b) `Result Summary` tanpa field baru — lingkup wajib `HR判定依据` di N17 diperluas ke ketiga outcome; (c) penanda 疑似重复 + link Case asal harus tampak di layar review N07 |
| D-14 | Koordinasi `@sscos-bot` masuk channel kolaborasi (A-05, menutup B-04) | Felix **c50261 butir 3**: tujuh channel sudah ditambahkan. Kent **c50262** menarik "channel ke-8" (`collab-hr-mgmt-hod`) sebagai kesalahannya sendiri — 「The seven you've already handled are the complete set」. Dibaca balik lewat Slack API 2026-09-21: `@sscos-bot` (U0BCPFHGURE) ada di tujuh channel **dan** di `sscos-hr`. Sisa registrasi 04.11 pindah ke **B-12** (Alden), bukan Felix |
| D-15 | Konfirmasi bagian mana dari putusan Kayden c50244 yang diserahkan ke kita (B-01) | Kent **c50255** + **c50257**, 2026-09-21. (b) komponen penjaga dan (c) izin pindah-status HR Ops & Data → **ke kita**, jadi A-06. (a) batasan urutan N28 → Kent naikkan sendiri ke Alden (c50256), lalu **kita tarik** lewat c50263 |
| D-16 | Angkat konflik hak pindah-status (C-04) | Terjawab lewat jalur Kayden: putusan **c50244** → eksekusi Kent **c50257** 「N28＝方向 2——转态权限配 HR Ops & Data 角色组＋守护件」. Sisa pertanyaan 04.3 §六 dirutekan ke Kayden lewat **c50263** kita → sekarang jadi **B-15** |
| D-17 | Perbarui baris blocker di halaman catatan pembangunan dengan putusan c50244 (C-05) | Halaman `2096463922` v31 → **v33** (2026-09-20 14:55:49Z). Empat sisipan: baris Registry di 附表, baris N28 di 附表, kolom 「允许执行者」 transisi id 11 di 区二, baris 「守护登记与演练」 di 区八 |
| D-18 | Tutup C-02 dan C-03 sebagai gugur | Keduanya menyangkut draft `D-2026-09-20-01` (kalimat D-009 di penutup; usulan A dan B). Draft itu **tidak jadi dipakai** — yang dikirim teks baru (D-12). Jadi tidak ada lagi yang perlu diputus di dua baris itu |
| D-19 | Ajukan 13 field 执行卡／子单 lewat jalur tiga kolom 04.10 | OSD-116 **c50283**, 2026-09-21 15:59 → **disetujui penuh** Kent **c50290** 17:18: 「13 项全部准予按「新共享对象」登记」. Tiga putusan tipe menyertainya, dan pembuatan fieldnya jadi **B-14**, bukan kerja kita |
| D-20 | Sapuan versi seluruh halaman sumber, perbaikan drift di anchor, dan upgrade skill `nosm-sync-check` | commit `dd592bf` (tujuh halaman bergerak: 07.06.1 v33→v34, 04.9 v103→v106, 04.9.1 v17→v19, 04.7 v45→v46, 04.4 v31→v33, 04.4.4 v1→v4, 04.8 v20→v21) · `ebd09b0` (anchor kehilangan kolom 责任边界, kolom 放行条件 dan satu kalimat 边界铁律 — dikembalikan verbatim; `CLAUDE.md` dicek dengan skrip, identik) · `5e5c58f` (sapuan kedua: tidak ada versi baru) |
| D-21 | Cermin tabel 待办/阻塞 建造单 dengan status per baris, tiap baris diuji terhadap 解除判据-nya sendiri | commit `24f3013`, file `docs/buildsheet-blocker-status.md`. Hasil: satu baris benar-benar tutup (baris 12, dasar Felix c50261 butir 4), sembilan bergerak tanpa 判据 terpenuhi, 23 tidak bergerak |


⚠️ **Catatan untuk D-11**: versi halaman yang tercatat di sana adalah versi **saat dibaca 2026-09-20** dan
sengaja tidak diubah. Beberapa sudah bergerak sejak itu — lihat D-20 dan `docs/source-versions.md`.

## E · Daftar draft yang belum dikirim

Folder: `docs/drafts/`

| ID draft | File | Perihal | Ke siapa | Status | Aksi terkait |
|---|---|---|---|---|---|
| `D-2026-09-20-01` | `2026-09-20-osd116-alden-pattern9.md` | Permintaan gabungan perluasan pola 9, 13 butir | Alden | **DITAHAN — tidak jadi dipakai.** Yang dikirim 2026-09-21 adalah teks baru (D-12), bukan file ini. File-nya masih ada di branch `claude/new-session-3nlq6e`, belum dibawa ke branch ini | D-12, D-18 |

**Aturan folder draft**: apa pun yang ada di situ **belum terkirim**. Begitu terkirim,
statusnya diubah di file draftnya sendiri dan barisnya di sini pindah ke bagian D.
Tidak ada draft yang dikirim tanpa perintah Bambang.

## Riwayat file ini

| Tanggal | Perubahan |
|---|---|
| 2026-09-20 | File dibuat atas perintah Bambang. Isi awal: 5 baris SEGERA, 6 baris MENUNGGU ORANG, 6 baris MENUNGGU KAU, 10 baris SELESAI, 1 draft |
| 2026-09-20 | A-04 ditulis ulang setelah sumbernya dibaca penuh — dipersempit ke bagian yang tidak terhalang. Ditambah B-07 s/d B-11 (penghalang A-04, semua bersumber) dan D-11. Alarm mulai kerja dipasang untuk 2026-09-21 09:00 UTC+8 (`trig_017MQtQVE6vS9x43b6kBJudi`). Sekarang: 5 SEGERA, 11 MENUNGGU ORANG, 6 MENUNGGU KAU, 11 SELESAI, 1 draft |
| 2026-09-21 | Diperbarui setelah sapuan penuh Confluence + OSD-116 + #nos-bo. **Keluar dari SEGERA**: A-01, A-02, A-05 (selesai). **Masuk SEGERA**: A-06, A-07 (dua-duanya dari Kent c50255). **Tutup**: B-01, B-04, C-01, C-04, C-05; C-02 dan C-03 gugur. **Baru di MENUNGGU ORANG**: B-12 (04.11, Alden), B-13 (empat tingkat PIP, Felix), B-14 (13 field, Kent), B-15 (pengecualian 04.3 §六, Kayden). **Baru di MENUNGGU KAU**: C-07 (sudah diputus: tampung). **C-06 dipindah keluar**: 「jangan menuduh／menyalahkan／mengadu orang」 bukan hal yang perlu diputus — itu aturan yang mengikat setiap draft, dan sudah ditulis di `docs/working-rules.md`. Sekarang: **4 SEGERA · 13 MENUNGGU ORANG · 1 MENUNGGU KAU · 21 SELESAI · 1 draft (gugur)** |
| 2026-09-22 | **A-06 dicabut dari SEGERA → B-16.** Sesudah 04.3 v33 §六, Spec S-05 v62 baris N28, dan 04.9 §一/§三 dibaca langsung: N28 方向 2 terkunci dua-duanya — izin transisi pada Kayden (04.3 §六 tidak mencakup HR Ops & Data, dan 撤回规则 melarang jalur itu bila ada子单 已完成), 守护件 pada Alden (04.9 tidak punya 分册 S-05, sedang 三位一体 melarang bangun-dulu-daftar-belakangan). Sekarang: **3 SEGERA · 14 MENUNGGU ORANG · 1 MENUNGGU KAU · 21 SELESAI** |
