# Tabel C Spec S-05 — pembelahan pembawa timer menurut 04.4 §8.1

> **Sifat**: kerja meja builder (Bambang). **Bukan** salinan halaman Confluence, jadi tidak tunduk aturan
> 部署漂移 dan tidak dihapus `nosm-sync-check`.
>
> **Dibuat** 2026-09-22 atas perintah Bambang (butir 3 dari rekomendasi hari itu).
> **Alasannya**: angka di A-04 lama tidak berdiri, dan `docs/action-list.md` B-17 sudah mencatat pembelahan
> 「1 baris JSM / 15 baris n8n」 harus dibangun ulang sebelum dipakai. File ini pembangunan ulangnya.
>
> **Yang dibaca live 2026-09-22** (bukan dari ingatan atau catatan lama):
> - **04.4｜自动化配置模式库** — §八 模式七 lengkap (§8.1 计时载体, §8.2 送达载体, §8.3 工作时口径).
>   Halaman terakhir diubah 2026-09-21 16:50; versi tercatat di `docs/source-versions.md` = **v33**.
> - **Spec S-05** (pageId 2036858900) — §② 节点表 lengkap (23 node) dan §③ 增补区 C｜SLA细则 lengkap
>   (16 baris). Halaman terakhir diubah **2026-09-15**, dan §① 状态区-nya berbunyi 「状态：**已冻结**」 —
>   dua-duanya dibaca hari ini. Nomor **v62** **tidak** berasal dari pembacaan hari ini (API tidak
>   mengembalikan nomor versi); ia dari `docs/source-versions.md`, yang pada sapuan 2026-09-22 06:21
>   masih mencatat v62 dan tidak bergerak.
>
> **Batas file ini**: ia hanya menjawab satu pertanyaan — **siapa yang menghitung waktu tiap baris C**.
> Ia tidak menetapkan angka, tidak menyentuh konfigurasi, dan tidak memutuskan hal yang bukan wewenang
> builder. Baris yang tidak bisa diputus dengan garis §8.1 ditulis sebagai **butuh putusan**, bukan diisi sendiri.

---

## Garis pemisahnya, verbatim dari 04.4 §8.1

Tabel §8.1 hanya punya dua baris:

| 计时对象 | 载体 | 理由 (dipendekkan) |
| --- | --- | --- |
| SSCSD 内的主单（含「待审批」时限、整单交付时限） | **JSM 原生 SLA 引擎** | per-status 计时、日历切换、达成率报表 semuanya bawaan |
| Team Project 执行卡、Pipeline Project 阶段时限、**跨对象时限**（如「主单创建 → 全部子单关闭」） | **n8n 定时扫描件（Timeout Scan）** | mesin SLA JSM hanya menjangkau单据 di dalam JSM Board |

Lalu kalimat penentunya:

> 判断线只有一句：**这个被计时的对象在不在 SSCSD 里**。在，用原生；不在，用 n8n。不因流程名、不因是否有审批、
> 不因历史实现方式而改变。

Dua kalimat lain dari §八 yang mengikat hasil di bawah:

- **§8.2**: 「无论计时用哪种引擎，**超时升级的通知发送、审批卡重发、催办与告警一律经 n8n 执行，不使用 Jira
  Automation 直发 Slack**」; bentuk konfigurasinya 「原生 SLA breach 事件经 webhook 出到 n8n…；n8n 定时扫描件
  则计时与送达同在一条 workflow 内」. → **Kolom pembawa di bawah cuma soal siapa yang menghitung. Pengiriman
  selalu n8n, tanpa kecuali.**
- **§8.3**: baris bertanda 工作时 口径-nya 「**住 NTP（Registry），由 n8n 在运行时读取**」; untuk mesin JSM,
  「该 Calendar 的取值须与 NTP 口径一致，出现偏差以 NTP 为准订正 Calendar」.

---

## Hasil per baris (16 baris, urut seperti di Spec)

Kolom **objek yang dihitung** diambil dari kolom 执行载体 node yang bersangkutan di §② 节点表, bukan dari
nama node. Kolom 计时方式 dikutip apa adanya dari tabel C.

| # | Baris C | 时限数值 (verbatim) | 计时方式 | Objek yang dihitung, dan di mana ia hidup | Di SSCSD? | **Pembawa timer** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **C-1**｜N07 首次审核 | 2工作日 | 工作时 | N07 执行载体 ＝ 「**主单「待审批」状态上的审批动作**」 → 主单, SSCSD | **Ya** | **JSM 原生 SLA** |
| 2 | **C-2**｜N07 打回补件回复 | 2工作日 | 工作时 | Tetap 主单 di 「待审批」 — Spec 需技术确认项 10 menulis 「案件在补件期间保持待审批状态」 → 主单, SSCSD | **Ya** | **JSM 原生 SLA** (lihat catatan ①) |
| 3 | **C-3**｜N08 Show Cause 文书生成及发出 | **即时（与N07判定同一时点）** | 工作时 | N08 执行载体 ＝ 自动化, 「与判定同一时点自动生成并发出」 → tidak ada obyek Jira yang dihitung | — | **Tidak ada timer** (lihat catatan ②) |
| 4 | **C-4**｜N09 员工回复 Show Cause | 3工作日（延期批准后重新计算，最多批准1次） | 工作时 | N09 执行载体 ＝ **子单**（载体名「等待员工解释」）→ HR Team Project | Tidak | **n8n 定时扫描件** (lihat catatan ③) |
| 5 | **C-5**｜N12 Warning 文书准备及发出 | 当日／1个工作日内 | 工作时 | N12 执行载体 ＝ **子单** → HR Team Project | Tidak | **n8n 定时扫描件** |
| 6 | **C-6**｜N26 到期前提醒 | 到期前5天 | 日历时／定时提醒 | N26 执行载体 ＝ **档案** → Registry Project 纪律处分记录 | Tidak | **n8n 定时扫描件** (lihat catatan ④) |
| 7 | **C-7**｜N26 到期重置 | 按「纪律记录有效期」字段执行 | 日历时／定时提醒 | Sama: **档案** → Registry Project | Tidak | **n8n 定时扫描件** (lihat catatan ⑤) |
| 8 | **C-19**｜N25 联合评审 | 5工作日 | 工作时 | N25 执行载体 ＝ **任务卡（住HR Team Project）** | Tidak | **n8n 定时扫描件** |
| 9 | **C-8**｜N15 PIP 启动 | **即时（与N07判定同一时点）** | 工作时 | N15 执行载体 ＝ 自动化, 「同一时点自动发起启动通知」 → tidak ada obyek yang dihitung | — | **Tidak ada timer** (lihat catatan ②) |
| 10 | **C-9**｜N16 PIP 执行周期 | 15/30/60/90天（视情况） | 日历时 | N16 执行载体 ＝ **子单（住该员工所属部门 Team Project，按 NTP 部门字段解析）** | Tidak | **n8n 定时扫描件** (lihat catatan ⑥) |
| 11 | **C-10**｜N16 Check-in 频率 | 15天PIP≥1次中期；30天≥每2周1次；60/90天≥每30天1次 | 日历时 | Irama Check-in pada **子单 N16** → Team Project departemen karyawan | Tidak | **n8n 定时扫描件** (lihat catatan ⑦) |
| 12 | **C-11**｜N21 离职单信息补齐跟踪 | 2工作日 | 工作时 | Kelengkapan informasi pada **离职主单 流程 lain** (员工离职 Spec), dan 离职主单 hidup di SSCSD | **Bercabang** | 🔴 **Butuh putusan** (lihat catatan ⑧) |
| 13 | **C-12**｜N20 解雇自动开单与交接 | 下一工作日内 | 工作时 | N20 执行载体 ＝ 自动化 (buat 离职主单 ＋ Issue Link) → yang dihitung adalah jalannya otomasi, bukan 单据 di SSCSD | Tidak | **n8n** (lihat catatan ⑨) |
| 14 | **C-14**｜N10 Show Cause 结果判定 | 2工作日 | 工作时 | N10 执行载体 ＝ **子单** → HR Team Project | Tidak | **n8n 定时扫描件** |
| 15 | **C-16**｜N17 PIP 结果评估 | 2工作日 | 工作时 | N17 执行载体 ＝ **子单** → HR Team Project | Tidak | **n8n 定时扫描件** |
| 16 | **C-20**｜N14 严重违纪加速判定 | 1个工作日 | 工作时 | N14 执行载体 ＝ **子单（系统自动设 Urgent Priority）** → HR Team Project | Tidak | **n8n 定时扫描件** |

### Hitungan akhir

| Pembawa | Jumlah | Baris |
| --- | --- | --- |
| **JSM 原生 SLA 引擎** | **2** | C-1, C-2 |
| **n8n 定时扫描件** | **11** | C-4, C-5, C-6, C-7, C-19, C-9, C-10, C-12, C-14, C-16, C-20 |
| **Tidak ada timer** (即时; yang dibutuhkan alarm gagal otomasi) | **2** | C-3, C-8 |
| 🔴 **Butuh putusan** | **1** | C-11 |
| | **16** | |

**Pembelahan lama 「1 baris JSM bawaan (C-1), 15 baris pemindai n8n」 memang tidak berdiri.** Yang benar
**2 · 11 · 2 · 1**. Dua koreksi utamanya: C-2 juga menghitung 主单 di SSCSD (jadi JSM, bukan n8n), dan C-3
serta C-8 tidak punya rentang untuk dihitung sama sekali.

### Kolom 计时方式 — hitungan yang benar

| 计时方式 | Jumlah | Baris |
| --- | --- | --- |
| **工作时** | **12** | C-1, C-2, C-3, C-4, C-5, C-19, C-8, C-11, C-12, C-14, C-16, C-20 |
| **日历时** / 日历时／定时提醒 | **4** | C-6, C-7, C-9, C-10 |

Jadi **「13 dari 16」 di A-04 lama salah; yang benar 12** — sesuai koreksi yang sudah tercatat di B-17.

**Tapi 12 bukan angka yang mengikat B-07.** Yang benar-benar butuh 口径 jam kerja NTP adalah baris yang
punya jam berjalan. C-3 dan C-8 bertanda 工作时 tetapi 时限数值-nya 即时 — tidak ada jam yang jalan, jadi
tidak ada yang perlu dibaca dari NTP. **Yang tergantung B-07 ada 10 baris**: C-1, C-2 (lewat Calendar mesin
JSM, 04.4 §8.3 「该 Calendar 的取值须与 NTP 口径一致」) dan C-4, C-5, C-19, C-11, C-12, C-14, C-16, C-20
(dibaca n8n saat jalan). Empat baris 日历时 tidak menyentuh 口径 jam kerja sama sekali.

---

## Catatan per baris

**① C-2 — pembawanya JSM, tapi kondisi start/stop-nya tidak bisa berbasis status.**
C-1 dan C-2 dua-duanya menghitung 主单 di status yang **sama**, 「待审批」 (15855). Dan 「打回补件」 adalah
transisi di tempat — 建造单 区二 mencatat transisi 4/5/6/7 semuanya `Pending Approval → Pending Approval`.
Jadi pemicu SLA yang bersandar pada masuk/keluar status tidak bisa membedakan C-1 dari C-2, dan berpotensi
tidak menyala sama sekali pada transisi di tempat. Ini **sudah dirutekan ke Alden** sebagai pertanyaan risiko
① di B-09 / 建造单 baris 21, belum dijawab. **File ini tidak memutuskan bentuk kondisinya** — itu konfigurasi
SSCSD, dan 04.1 §六 menempatkannya di lingkup V1: 「Help Center 与 SSCSD 的具体配置属于平台实际配置（V1 范畴）…
此处只出方案与需求文档，最终配置需与 Alden 侧对齐」.

**② C-3 dan C-8 — bukan SLA, tapi alarm gagal otomasi.**
时限数值 dua baris ini 「即时（与N07判定同一时点）」, dan kolom 超时升级对象-nya sendiri berbunyi 「未完成 →
自动化失败告警（**本节点为自动化动作，非人工待办**）」. Tidak ada rentang waktu, jadi garis §8.1 tidak berlaku —
tidak ada obyek yang dihitung. Yang dibutuhkan adalah kaki error komponen n8n-nya: 04.6 §3.5 层一 mewajibkan
tiap komponen memasang `settings.errorWorkflow` → Error Handler (nos-ops) `VUIgv9Ujj1KEoIne`, dan 建造单 区五
sudah mencatat kewajiban itu. **Observasi, bukan temuan**: kolom 计时方式 dua baris ini tetap tertulis 工作时
walau tidak ada jam yang jalan. Tidak ada dampak konfigurasi, jadi tidak diangkat sebagai pertanyaan.

**③ C-4 — pemindainya harus bisa reset, dan punya dua titik pemicu.**
Satu baris ini memuat tiga perilaku: (i) pengingat terakhir otomatis pada **hari kerja ke-2** — tabel C
menandainya 「非升级动作」; (ii) masuk N10 pada akhir **hari kerja ke-3**; (iii) **reset penuh** kalau
perpanjangan disetujui — 「延期批准后重新计算，最多批准1次」, dihitung lewat field 「Show Cause延期次数」
(A 表: initial 0, max 1). Jadi komponen pemindainya bukan pembanding tenggat tunggal.

**④ C-6 — obyeknya belum ada.**
N26 载体-nya 档案 di Registry Project 纪律处分记录, dan Project itu **belum dibuat**: 04.1 §一 baris itu masih
「候选｜待N5」 (B-19 / 建造单 baris 1). Keputusan pembawa timernya tetap bisa ditentukan sekarang — obyeknya
jelas bukan di SSCSD — tapi pembangunannya jelas menunggu.

**⑤ C-7 — secara bentuk bukan SLA, tapi transisi terjadwal.**
Kolom 超时升级对象-nya berbunyi 「到期即按N26规则直接转为已重置，**无超时升级**」. Jadi yang dibutuhkan bukan
pemindai keterlambatan, melainkan pemicu berjadwal yang menjalankan 模式六 档案转态 pada tanggal jatuh tempo.
Pembawanya tetap komponen n8n berjadwal; bedanya aksinya transisi, bukan eskalasi.

**⑥ C-9 — pemindainya harus menjangkau tujuh Team Project.**
N16 子单 「住该员工所属部门 Team Project，按 NTP 部门字段解析」. Team Project yang 运行中 di 04.1 §一 ada tujuh:
HR, BO, FIN, CRM, FOZ, WP, XLP. Jadi satu pemindai harus melintasi ketujuhnya, bukan HR saja.
**Observasi terpisah**: C-9 menulis 「15/30/60/90天（视情况）」. Jawaban Felix c50328 (2026-09-22) menyangkut
**「延长周期」** — parameter Extension di N17 — bukan kata 「视情况」 di C-9 ini. Apakah jawaban itu sekaligus
mengunci C-9 **tidak kusimpulkan**; kalau perlu, itu pertanyaan satu baris ke Felix, dan butuh perintah.

**⑦ C-10 — bukan tenggat, tapi irama.**
Yang dicek bukan satu tanggal jatuh tempo, melainkan apakah Check-in sudah dilakukan sesuai frekuensi
tingkatnya (15 hari ≥1 kali pertengahan; 30 hari ≥ tiap 2 minggu; 60/90 hari ≥ tiap 30 hari). Jadi
pemindainya harus menurunkan jendela yang diharapkan dari tingkat PIP, lalu membandingkannya dengan isi
field 「Check-in记录」 (append-only, butir 4 di c50283 — field-nya sendiri **belum dibuat**, B-14 / Kent).
Bentuknya berbeda dari sepuluh baris pemindai lain dan tidak boleh diborong sebagai "satu pemindai tenggat".

**⑧ C-11 — satu-satunya baris yang garis §8.1 tidak selesaikan sendiri.**
Bacaan harfiahnya: yang dihitung adalah kelengkapan informasi pada **离职主单**, dan semua 主单 hidup di SSCSD
(04.1 §二 butir 1: 「主单行：一律 SSCSD」) → mesin JSM. Tapi dua fakta tidak cocok dengan bacaan itu:
- **Eskalasinya berulang.** Tabel C: 「持续跟踪不解除，直至信息补齐为止」. SLA JSM breach sekali, bukan terus-menerus.
- **单据-nya milik flow lain.** 离职主单 milik 员工离职 Spec; pintu masuk sistemnya sendiri masih celah
  (建造单 baris 8, Kent ＋ Geri), dan konfigurasi SLA di sisi itu bukan wilayah kita.

Sementara §8.1 baris kedua justru menyebut 「**跨对象时限**」 secara eksplisit sebagai wilayah n8n, dan inilah
timer lintas obyek (Case S-05 mengawasi field di 单据 flow lain). **Jadi baris ini tidak kuisi.** Ia perlu
putusan Owner 04.4 (Alden), dan pertanyaannya sudah berbentuk: *apakah timer lintas-flow seperti ini dihitung
「SSCSD 内的主单」 karena 单据-nya di SSCSD, atau 「跨对象时限」 karena yang mengawasi adalah flow lain.*
Mengirim pertanyaan itu adalah tindakan keluar — butuh perintah pemilik repo.

**⑨ C-12 — punya jendela, tapi bentuknya tetap pengawasan otomasi.**
Beda dari C-3/C-8, baris ini punya rentang (「下一工作日内」), jadi ada yang bisa dihitung. Tapi yang dihitung
adalah jalannya otomasi N20, bukan 单据 di SSCSD: kolom 超时升级对象-nya juga 「自动化失败告警（本节点为自动化
动作，非人工待办）」. Bentuk ini persis yang sudah terdaftar di 建造单 区八 守护登记 层三: 「卡死／漏账巡逻 —
状态已走但记录未落」. Jadi pembawanya n8n, dan kemungkinan besar bukan komponen pemindai SLA tersendiri
melainkan bagian komponen 守护 层三. **Pemetaan ke komponen mana persisnya tidak diputus di sini** — itu
keputusan desain komponen, dan pembangunannya terkunci di B-08.

---

## Apa yang terkunci dari hasil ini

Pembelahan di atas sudah selesai dan tidak menunggu siapa pun. **Pembangunannya semua terkunci:**

| Yang mau dibangun | Terkunci oleh |
| --- | --- |
| 11 baris pemindai n8n (dan komponen 守护 untuk C-12) | **B-08** — 04.9 §三 tidak punya 分册 S-05, sedangkan §一 铁律 三位一体 「缺任一项视为未完成」. Alden |
| 2 baris JSM (C-1, C-2) | **04.1 §六** menempatkan konfigurasi SSCSD konkret di lingkup V1 (「此处只出方案与需求文档」); izin Kent c50198 menyebut empat obyek (Issue Type、Workflow 状态链、字段、转换) — **SLA tidak termasuk**. Ditambah dua pertanyaan risiko B-09 ke Alden yang belum dijawab |
| 口径 jam kerja untuk 10 baris | **B-07** — 04.8 §五 baris 「工作时口径字段族（占位）」 masih 「🔲 ID 待 Alden 补」, sedangkan 04.8 §四 melarang memakai field entitas yang belum terdaftar. Alden |
| C-6, C-7 | **B-19** — Registry Project 纪律处分记录 masih 「候选｜待N5」 (04.1 §一). Kayden 侧派人 |
| C-10 | Field 「Check-in记录」 belum dibuat — **B-14**, Kent |
| C-11 | Putusan catatan ⑧ (Alden) ＋ pintu masuk sistem di 员工离职 Spec (建造单 baris 8, Kent ＋ Geri) |

**Yang jadi lebih jelas setelah pembelahan ini**: C-1 dan C-2 tidak tergantung B-08 sama sekali — dua baris
itu mesin JSM, bukan komponen n8n. Jadi begitu jalur konfigurasi SSCSD dibuka (04.1 §六 / izin Alden) dan
Calendar-nya punya 口径 (B-07), dua baris itu bisa jalan tanpa menunggu 04.9 分册. Sebelas baris sisanya tidak.

---

## Riwayat file ini

| Tanggal | Perubahan |
| --- | --- |
| 2026-09-22 | **Audit atas perintah Bambang — satu kesalahan ditemukan dan dibetulkan.** Baris C-2 tadinya menulis 「N07 menulis 『打回补件循环期间保持本状态不变』」. Frasa itu **nol kali** ada di Spec dan **satu kali** di 建造单 区二 (diverifikasi dengan grep) — jadi salah sumber. Diganti ke kalimat Spec yang memang ada: 需技术确认项 10 「案件在补件期间保持待审批状态」 (satu kali di Spec). **Isi pembelahannya tidak berubah** — C-2 tetap JSM. Juga diperjelas: nomor v62 berasal dari ledger, bukan dari pembacaan hari ini. Seluruh aritmetika diverifikasi ulang dengan skrip: 16 baris · 12 工作时 · 4 日历时 · 2 即时 · B-07 mengunci 10 · klasifikasi 2/11/2/1 menutup ke-16 tepat sekali |
| 2026-09-22 | Dibuat. 16 baris tabel C Spec v62 diadu satu per satu ke 04.4 v33 §8.1. Hasil: **2 JSM · 11 n8n · 2 tanpa timer · 1 butuh putusan**. Dua koreksi terhadap angka lama: 「13 dari 16 工作时」 → **12**, dan 「1 JSM / 15 n8n」 → **2 / 11 / 2 / 1**. Satu angka baru: yang benar-benar tergantung B-07 ada **10** baris, bukan 12 |
