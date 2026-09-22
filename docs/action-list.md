# Daftar Aksi — OSD-116 / S-05 (Penanganan Disiplin & Perbaikan Kinerja)

> **Sifat**: file kerja kami. **Bukan** salinan halaman Confluence, jadi **tidak** tunduk
> aturan 部署漂移 (deployment drift) dan tidak akan dihapus `nosm-sync-check`.
> **Satu-satunya file daftar aksi.** Kalau ada aksi baru, masuk ke sini — jangan bikin file lain.
>
> **Terakhir diperbarui**: 2026-09-22 ~09:30 WIB
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

**Kosong per 2026-09-22.** Tidak ada satu pun pekerjaan S-05 yang bisa jalan sekarang.

Kelima baris yang pernah ada di sini sudah keluar semua: A-01 → D-12 · A-02 → D-13 · A-05 → D-14
(tiga ini selesai), lalu **A-06 → B-16** · **A-04 → B-17** · **A-03 → B-18** · **A-07 → B-19**
(empat ini ternyata terkunci — masing-masing ditaruh di sini tanpa diadu ke halaman standarnya dulu).

Semuanya bertumpu pada tiga hal di sisi orang lain:

| | Mengunci |
|---|---|
| **B-08** — 04.9 belum punya 分册 S-05 (Alden) | seluruh pembangunan komponen n8n S-05 — B-16 bagian 2, B-17 |
| **B-02** — 04.1／04.8 转正式登记 (Kayden) | N5 建库, lalu N13／N26／N27 — B-19 |
| **B-07** — field jam kerja NTP (Alden) | perhitungan 12 baris SLA 工作时 — B-17 |

## B · MENUNGGU ORANG

Bukan kita yang menghalangi.

🔴 **Fakta yang mengikat seluruh baris Alden di bawah**: Alden **belum berkomentar di OSD-116 sejak
2026-09-10**. Diverifikasi 2026-09-21: namanya tidak muncul di 60 komentar terbaru, yang mundur sampai
2026-09-10 12:58.

| ID | Menunggu siapa | Soal apa | Sejak | Kalau dia jawab, apa yang terbuka |
|---|---|---|---|---|
| B-02 | **Kayden (sisi dia)** | Konversi baris di 04.1 dan 04.8 untuk gudang arsip mandiri (putusan c50244 butir 1, opsi C) — **yang ditunggu oleh B-19** | 2026-09-20 | Baris blocker N13/N26/N27 di halaman catatan pembangunan bisa diperbarui. **2026-09-21**: Kent c50257 menegaskan ini sisi Kayden — 「04.1/04.8 转正式登记归你侧派人」 — dan dia akan mengawal sampai tutup. **Dicek hari ini: 04.1 masih v46, 04.8 masih v21, baris 04.1 §一 masih 「候选｜待N5」. Belum bergerak** |
| B-03 | **Alden + Felix** | Daftar jabatan NTP lewat tiket pemeliharaan GOV — **sama dengan B-18** | belum dimulai | A-03. **2026-09-21: tidak ada perubahan** |
| B-05 | **Alden** | Perluasan kemampuan pola 9 v5 itu sendiri | **sudah dikirim 2026-09-21 15:17** | N07 tidak bisa dibangun sesuai Spec beku tanpa ini. **Statusnya berubah**: dulu 「belum dikirim」, sekarang sudah — OSD-116 **c50279**, enam blok + empat add-on + catatan Data Table. **Belum dibalas.** 判据 baris blocker 建造单 no.3 berbunyi 「平台扩展组件能力并更新 04.4.1」 — 04.4.1 masih v13 |
| B-06 | **Felix** | Isi daftar penyimpangan untuk celah S-05 → proses keluar karyawan | 2026-09-20 | Spec beku mewajibkan penanganan sementaranya dicatat di sana. **Sekarang kosong dan kita tidak boleh mengarangnya.** 2026-09-21: Felix menjawab empat hal lain (c50261), yang ini tidak termasuk |
| B-07 | **Alden** | Kumpulan field jam kerja di NTP (jam masuk/pulang, istirahat, hari libur, cuti umum) — **blocker 2 dari B-17** | 2026-09-20 | 13 dari 16 baris tabel C berhitung "jam kerja". 04.4 §8.3 melarang angkanya ditulis di dokumen — wajib dibaca dari NTP saat jalan. 04.8 §五 barisnya masih placeholder: `ID 🔲 待 Alden 补`. 04.8 §四 melarang memakai field entitas yang belum terdaftar. **Bukan soal izin — barangnya memang belum ada.** 2026-09-21: 04.8 naik ke v21, tapi perubahannya cuma baris 员工 (sumber transisi sisi onboarding = S-02). Baris ini tidak bergerak |
| B-08 | **Alden** | Buku detail 04.9 untuk S-05 — **mengunci bagian 2 dari B-16 dan blocker 1 dari B-17** | 2026-09-20 | Aturan besi 04.9 §一 "tiga serangkai". **2026-09-21**: 04.9 naik v103 → **v106**. Yang ditambahkan: baris indeks 身份件 dan pembaruan baris keluarga Grade. **Tidak ada buku baru untuk S-05** — dibaca dari diff v103→v106 |
| B-09 | **Alden** | Konfigurasi SLA di SSCSD, berikut **dua pertanyaan risiko** | 2026-09-20 | 04.1 §一: Owner SSCSD = Alden. 04.1 §六: konfigurasi konkret SSCSD adalah lingkup V1 — sisi kita *"hanya mengeluarkan rancangan dan dokumen kebutuhan"*. Dua pertanyaannya: **①** C-1 dan C-2 sama-sama menghitung tiket induk di status **"Pending Approval" yang sama**, sedangkan "kembalikan untuk dilengkapi" adalah transisi di tempat — pemicu berbasis status berpotensi tidak menyala. **②** Menghapus nilai bawaan Jira 8/16 jam bisa mengenai alur lain; mungkin yang benar "tambah, jangan hapus". **2026-09-21: tidak ada perubahan** |
| B-10 | **Alden** (pengganti: **Kent**) | Izin menyalakan komponen n8n | belum berlaku | Baru berlaku setelah komponen A-04 jadi. 04.6 §3.6 langkah 4 + §3.4 butir 4 (Kent boleh menyetujui kalau Alden lewat 1 hari kerja). **2026-09-21 — ada putusan baru yang menyentuh baris ini**: di #nos-bo 2026-09-19 17:04 Kayden menetapkan 工程审关 (menyalakan) dan 验收关 (N13/N14) adalah **dua gerbang berbeda**, dan saat mencolok switch Alden 「只核 04.9 登记和守护配置，不再另审一套标准」. Dia juga menetapkan urutannya: 「切 active 放在 N14 通过之后、N15 上线之前」 dan akan menulisnya ke OS 开发流 Spec. ⚠️ **OS 开发流 Spec masih v39 dan belum memuatnya** — jadi ini putusan yang belum turun ke halaman, belum boleh dipakai sebagai dasar |
| B-11 | **Felix** | Batas waktu keseluruhan per permintaan | 2026-09-20 | Dua baris kita (`RT-HR-DISCIPLINARY-SUBMIT` dan `RT-HR-DISCIPLINARY-EVENT`) kolom SLA berakhir `请求级整单时限 🔲 未定占位`. **2026-09-21: 04.7 naik v45 → v46, tapi kedua baris S-05 tidak berubah satu huruf** (perubahan v46 hanya menyentuh baris RT-HR-RECRUITMENT-SUBMIT dan menambah RT-HR-RECRUITMENT-OFFERWITHDRAW). Masih menunggu |
| B-12 | **Alden** | Registrasi tujuh channel kolaborasi di **04.11** | 2026-09-20 | Pecahan dari B-04 yang tertinggal setelah bagian Felix tutup. Ini 判据② baris blocker 建造单 no.6. **04.11 masih v2 (2026-08-24)** dan tidak muncul di sapuan versi mana pun. 04.5 §七 butir 22 menjadikan ketiadaan baris 04.11 sebagai **gagal audit struktur**, bukan sekadar telat kerja |
| B-14 | **Kent** | Membuat 13 field, memasangnya ke screen, dan mendaftarkannya di 04.10 §三 dengan bukti | 2026-09-21 | Kent **c50290**: 「13 个 Jira 字段的创建、挂屏与 04.10 登记＝Schema Owner 侧（我方）；你（Bambang）负责 S-05 流程建设、消费这些字段」. Sebelum fieldnya ada, kita tidak bisa 回读 API apalagi mengonsumsinya. **2026-09-22**: satu syarat yang Kent tunggu sudah turun — Felix **c50328** menjawab 一问 di c50290, jadi tipe 「延长周期」 boleh dikunci sebagai option (15/30/60/90). Pembuatan, pemasangan screen dan registrasi 04.10 tetap sisi Kent |
| B-15 | **Kayden** | Apakah N28 perlu pengecualian terhadap 04.3 §六 互斥条 — **bagian 1 dari B-16** | 2026-09-21 | Dirutekan oleh **c50263** kita. 判据 baris blocker 建造单 no.19 minta dua hal: 执行身份 (sudah beres lewat c50244 → c50257 方向 2) dan 互斥条适用口径 (ini, belum). 04.3 dicek hari ini: masih v33, §六 tidak berubah |
| B-16 | **Kayden** (bagian 1) ＋ **Alden** (bagian 2) | **N28 方向 2 — dua-duanya terkunci, bukan pekerjaan yang bisa jalan sekarang.** Dasarnya Kayden **c50244**: 「方向 2 不动 Spec：Spec 执行者本就是 HR Ops & Data 角色，把转态权限配给该角色组即可；「忘记按」加一个守护件」 | 2026-09-22 (dicabut dari A-06) | **Bagian 1 · izin transisi → Kayden, sudah ada di B-15.** Spec v62 baris N28 menulis 执行者 ＝ HR Ops & Data **dan** 动作 ＝ 「04.3§六既有「Project Owner中止」出口，**不新造转态**」. Tapi 04.3 v33 §六 转态权限表 untuk pintu itu berbunyi 「**仅服务账号与该主单所在 Project 的 Owner**」 — HR Ops & Data tidak ada di dalamnya, sedangkan kalimat pembuka §六 「不设限制的转态视为配置未完成」. Jadi mengkonfigurasi sesuai c50244 justru menciptakan izin yang tabel itu tidak cakup. **Lebih keras lagi**, 撤回规则 §六: 「全关子单中只要有一张「已完成」，走模式五自动转「已完成」，**不得再走本条中止路径**」 — ini larangan, dan pemicu N28 (case 处理中 di tengah N08~N17) lazimnya sudah punya子单 已完成. **c50244 tidak menyentuh bagian ini.** Owner 04.3 ＝ Kayden; sudah dirutekan lewat c50263, belum dijawab. **Bagian 2 · 守护件 → Alden, sudah ada di B-08.** Membangun komponen mati memang keputusan sendiri (07.06.1 六-2), tapi 04.9 §一 铁律 「三位一体…缺任一项视为未完成」 dan 04.9 §三 cuma punya enam 分册 (平台／请假／员工离职／OS 开发流／Grade／Salary·Improvement·运维) — **tidak ada untuk S-05**, dan §三 tidak menulis siapa yang boleh membuat 分册 baru |
| B-17 | **Alden** (dua-duanya) | **Konfigurasi SLA / bangun komponen pemindai n8n — tidak bisa jalan, dan hitungan di A-04 lama salah.** Dasar lama: Kent c50227 butir 7 「no ruling needed, follow 04.4 §8.1」 | 2026-09-22 (dicabut dari A-04) | **Blocker 1 → B-08.** 04.9 §一 铁律 「三位一体：新增 workflow 是不可拆分的动作…**缺任一项视为未完成**」 ＋ 07.06 §四-5 「不得先建后补」. 04.9 §三 tidak punya 分册 S-05, jadi detail block-nya tidak punya tempat — mau satu komponen atau lima belas. **Blocker 2 → B-07.** 04.4 §8.3: baris 工作时 「住 NTP（Registry），由 n8n 在运行时读取」; 04.8 §五 baris 「工作时口径字段族（占位）」 masih **「🔲 ID 待 Alden 补」** sedangkan kolom 被谁消费-nya justru tertulis 「全站 SLA 工作时计时」. **Koreksi fakta atas A-04 lama** (dihitung langsung dari tabel C Spec v62, 16 baris: C-1,2,3,4,5,6,7,8,9,10,11,12,14,16,19,20): ① 「13 dari 16 berhitung jam kerja」 → sebenarnya **12** (kolom 计时方式: 12 工作时, 4 日历时／定时提醒); ② 「1 baris JSM bawaan (C-1), 15 baris pemindai n8n」 **tidak berdiri** — 04.4 §8.1 membelah dengan 「这个被计时的对象在不在 SSCSD 里」, dan **C-1 dan C-2 dua-duanya** menghitung 主单 di 「待审批」 (SSCSD → JSM native, itu wilayah B-09), sementara **C-3 dan C-8** tertulis 「即时（与N07判定同一时点）」 sehingga tidak punya rentang untuk dipindai. Jumlah komponen sebenarnya harus disusun ulang per baris menurut §8.1 sebelum dipakai. **2026-09-22: sudah disusun ulang** — lihat `docs/tabelC-sla-carrier-split.md` (D-23). Hasilnya **2 JSM · 11 n8n · 2 tanpa timer · 1 butuh putusan**, dan yang benar-benar tergantung B-07 ada **10** baris, bukan 12. Dua baris JSM (C-1／C-2) **tidak** tergantung B-08 |
| B-18 | **Alden** ＋ **Felix** | **Standarisasi daftar jabatan (岗位) NTP.** Dicabut dari A-03: isinya memang bukan kerja kita | 2026-09-22 (dicabut dari A-03) | Duplikat sisi-kita dari **B-03**. 建造单 baris 2 (**阻塞中**) menutupnya sendiri, verbatim di kolom 解除判据: 「**本项不因此自动解除**——S-05 无任何节点产出受控清单变更…**属 Alden／Felix 侧动作**。建造侧登记本条只为向其提问时有确定的制度落点可指，**不代为决定清单内容、Owner 或落点**」. Yang tersisa untuk kita hanya bertanya, dan itu tindakan keluar yang butuh perintah pemilik repo. Catatan baris A-03 lama pun sudah menunjuk blocker-nya sendiri (「lihat B-03」), jadi ia memang tidak pernah pantas duduk di SEGERA. 不做的后果 baris 2: 「N07／N14 回避改派无法自动判断」 |
| B-19 | **Kayden (sisi dia)** | **Bangun gudang arsip 纪律处分记录 per N5 (opsi C).** Dicabut dari A-07 | 2026-09-22 (dicabut dari A-07) | Sama isinya dengan **B-02**; baris ini menamai pekerjaannya, B-02 menamai yang ditunggu. Dasar perintahnya ada — Kayden **c50244** 「请按 N5 正式建库」 dan Kent **c50255** 「Build the library per N5」 — **tapi registrasinya belum turun**. 04.1 §一 dibaca live (v46, diubah 2026-09-19, yaitu **sebelum** putusan 09-20): baris 纪律处分记录 masih 「**候选｜待N5**」, Project key 🔲, Owner 🔲, dengan catatan barisnya sendiri 「裁决前不作为可执行登记」. Tiga tempat di 04.1 menutupnya: **§1.1** 「该状态不可被 Spec、自动化或 **BO** 当作可执行 key」; **§一 自检** 「「候选｜待 N5」的行仅是裁决输入，**不属于可执行登记**…进入设计与建设前仍须满足已裁决／运行中登记的唯一性」; **§二** 「查不到已裁决的对应行…**停止建设并退回补齐**」. Dan **§1.1** menutup jalan pintas: 「N5 人工裁决：仅 Kayden 或 Alden 任一人可裁决…**BO 无此写权**」 — jadi kita tidak bisa membangunnya, tidak bisa pula membetulkan barisnya. c50244 sendiri menugaskan 「04.1、04.8 两行由 **Kayden 侧派人**转正式登记」. 不做的后果 建造单 baris 1: 「N13／N26／N27 整段不可建」 |

**Yang tutup hari ini**: B-01 → D-15 · B-04 → D-14 (sisanya jadi B-12).

**Yang tutup 2026-09-22**: B-13 → D-22.

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
| D-25 | Audit seluruh pekerjaan 2026-09-22 atas perintah Bambang | commit di bawah. Yang diadu ulang: **kutipan** (19 frasa di-grep ke `spec.md`／`bs.md` — 18 cocok, **1 salah sumber → dibetulkan**); **aritmetika tabel C** (skrip ulang: 16／12／4／10／2-11-2-1, semua cocok); **keadaan Jira live** (4 tiket Disciplinary Case, status／resolution／assignee／label sesuai catatan, **komentar 0 pada keempatnya** → tidak ada automation yang menyentuhnya, dan tidak ada tiket yang mampir di queue Alden); **hitungan repo** (B=16 · C=1 · D=25 · butir 1–20 tanpa lompatan／duplikat · papan status 19⏳/0✅/1👁 cocok). Satu kesalahan nyata: frasa 「打回补件循环期间保持本状态不变」 diatribusikan ke Spec N07, padahal ada di 建造单 区二 — pembelahan C-2 tidak berubah. Tiga presisi lain diperbaiki |
| D-24 | Jalankan tiga transisi terminal S-05 dan baca balik buktinya | commit di bawah, file `docs/test-evidence-2026-09-22-terminal-transitions.md`. Atas perintah 「Nomor 2 kerjakan, tiga transisi dulu」; 04.5.3 v13 dibaca live lebih dulu. **SSCSD-423 → transisi 3 `Reject`** (status 15855→**15850**, resolution null→**10042 Rejected**) · **SSCSD-421 → 8 `Withdraw`** dan **SSCSD-422 → 9 `Cancel as Duplicate`** (dua-duanya 15855→**15961**, resolution null→**10041 Cancelled**). Ketiganya satu entry changelog dua item, tanpa input manusia → 04.3 §7.2 ① terbukti. **Empat dari lima Resolution post function kini terbukti**; sisa `Abort Case`(11), **ditahan** menunggu B-15. Tiga atribut `Create`(1)／`Complete`(10)／`Abort Case`(11) tetap **0 dari 3** — hanya bisa dibaca di 态 `Pending Sub-tickets`. Jadi **baris 28 belum tuntas** (3/4 dan 0/3). Satu temuan: F-007 diperluas ke tiga transisi |
| D-23 | Susun ulang pembelahan pembawa timer 16 baris tabel C menurut 04.4 §8.1 | commit di bawah, file `docs/tabelC-sla-carrier-split.md`. Dibaca live 2026-09-22: 04.4 v33 §八 lengkap (§8.1／§8.2／§8.3) ＋ Spec S-05 v62 §② 节点表 (23 node) dan §③ C 表 (16 baris). Hasil **2 JSM (C-1, C-2) · 11 n8n · 2 tanpa timer (C-3, C-8 — 即时, yang dibutuhkan alarm gagal otomasi) · 1 butuh putusan (C-11)**. Hitungan diverifikasi dengan skrip terhadap tabel C asli: 16 baris, 12 工作时, 4 日历时, klasifikasi menutup ke-16 baris tepat satu kali |
| D-22 | Tutup B-13 — pertanyaan empat tingkat PIP 「延长周期」 | Felix **c50328**, 2026-09-22 08:37 +07: 「确认，PIP「延长周期」就维持 15 / 30 / 60 / 90 天四档，不开放「视情况」填写其他天数」 dan 「延长后的周期继续沿用现有 C-10 对应的 Check-in 频率规则即可，**可以按 option 锁定**」. Dialamatkan ke **Kent**, bukan ke kita — yang terbuka karenanya ada di sisi Kent (B-14). Tidak ada pekerjaan baru di sisi kita |
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
| 2026-09-22 | **A-04 dicabut dari SEGERA → B-17.** Sesudah 04.4 §八, 04.8 §四/§五, 04.9 §一/§三 dan tabel C Spec v62 dibaca langsung: dua blocker (04.9 分册 dan field jam kerja NTP, dua-duanya Alden), plus dua kesalahan angka di baris lama — 「13 dari 16」 sebenarnya 12, dan pembelahan 「1 JSM / 15 n8n」 tidak berdiri terhadap 04.4 §8.1. Sekarang: **2 SEGERA · 15 MENUNGGU ORANG · 1 MENUNGGU KAU · 21 SELESAI** |
| 2026-09-22 | **Audit seluruh pekerjaan hari ini → D-25.** 19 kutipan di-grep ke sumbernya, aritmetika tabel C diskrip ulang, keadaan Jira dibaca live, hitungan repo dicek. **Satu kesalahan nyata ketemu dan dibetulkan** (salah sumber kutipan di baris C-2), plus tiga presisi. Sekarang: **0 SEGERA · 16 MENUNGGU ORANG · 1 MENUNGGU KAU · 25 SELESAI** |
| 2026-09-22 | **Tiga transisi terminal dijalankan → D-24.** `Reject`／`Withdraw`／`Cancel as Duplicate` masing-masing satu tiket TEST, dijalankan dan dibaca balik; `Abort Case` ditahan menunggu B-15. Baris 28 建造单 sekarang 3/4 transisi dan 0/3 atribut — belum tuntas. Tidak ada setelan harness yang diubah. Sekarang: **0 SEGERA · 16 MENUNGGU ORANG · 1 MENUNGGU KAU · 24 SELESAI** |
| 2026-09-22 | **Pembelahan tabel C dibangun ulang → D-23.** 16 baris diadu satu per satu ke 04.4 §8.1; angka lama diganti (**2 JSM · 11 n8n · 2 tanpa timer · 1 butuh putusan**), dan satu angka baru: B-07 mengunci **10** baris, bukan 12. B-17 diberi penunjuk ke file hasilnya. Sekarang: **0 SEGERA · 16 MENUNGGU ORANG · 1 MENUNGGU KAU · 23 SELESAI** |
| 2026-09-22 | **B-13 tutup → D-22.** Felix menjawab lewat **c50328** (08:37 +07): empat tingkat PIP final, tidak ada 「视情况」, dan tipe option boleh dikunci. Jawabannya ditujukan ke Kent, jadi tidak ada pekerjaan baru di sisi kita — sisanya pindah ke B-14. Sekarang: **0 SEGERA · 16 MENUNGGU ORANG · 1 MENUNGGU KAU · 22 SELESAI** |
| 2026-09-22 | **A-03 → B-18 dan A-07 → B-19; bagian SEGERA kini kosong.** Sesudah 建造单 baris 1／2 dan 04.1 §一／§1.1／§二 dibaca langsung: A-03 memang 「属 Alden／Felix 侧动作」 menurut 解除判据 barisnya sendiri, dan A-07 terhalang baris 04.1 yang masih 「候选｜待N5」 dengan 04.1 melarang BO memperlakukannya sebagai key yang bisa dipakai — sekaligus melarang BO menulis barisnya. Sekarang: **0 SEGERA · 17 MENUNGGU ORANG · 1 MENUNGGU KAU · 21 SELESAI** |
