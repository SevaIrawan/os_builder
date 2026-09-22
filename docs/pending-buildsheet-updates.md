# 建造单 (2096463922) — daftar pembaruan, dengan status per butir

> Catatan kerja builder (Bambang). Setiap butir memakai kebiasaan halaman: 原文保留不删, tambah catatan bertanggal.
> Disusun 2026-09-21. Sumber tiap butir disebut di baris masing-masing.

## Papan status

| | |
|---|---|
| **Versi halaman 建造单 sekarang** | **v33** (2026-09-20 14:55:49Z) — diverifikasi dari riwayat versi |
| **⏳ PENDING** (menunggu, belum ditulis ke Confluence) | **16** |
| **✅ COMPLETED** (sudah ditulis ke Confluence) | **0** |
| **👁 PANTAU** (tidak mengubah baris apa pun, cuma diawasi) | **1** — butir 16 |
| **Terakhir ditulis ke Confluence** | belum pernah — belum ada satu butir pun yang naik |

### Arti tiap status

| Status | Artinya | Syarat untuk menyandangnya |
|---|---|---|
| **⏳ PENDING** | Teksnya sudah siap di file ini, **belum ada di halaman Confluence**. Halaman tidak berubah, versi tidak naik. | — |
| **✅ COMPLETED** | Teksnya **sudah benar-benar ada di halaman**. | Tiga-tiganya wajib ada di kolom Status baris itu: **(1)** tanggal tulis, **(2)** nomor versi halaman tempat ia mendarat (mis. v34), **(3)** bukti baca-balik — halaman dibaca ulang setelah ditulis dan teksnya ada. Tanpa ketiganya, baris tetap PENDING walau merasa sudah dikerjakan. |
| **👁 PANTAU** | Butir yang **tidak mengubah baris mana pun** di halaman, cuma perlu diawasi. Tidak pernah jadi COMPLETED. Kalau yang diawasi benar-benar turun jadi aturan, butir ini baru berubah jadi butir PENDING biasa. | — |

### Aturan menaikkan versi

1. **Tidak ada butir yang ditulis ke Confluence tanpa perintah Bambang.** Tidak ada pengecualian.
2. **Satu perintah = satu kali tulis = satu kenaikan versi**, berapa pun butir yang ikut. Versi tidak naik
   per butir. Jadi v33 → v34 bisa memuat satu butir, bisa enam belas — tergantung apa yang kau perintahkan
   ikut pada saat itu.
3. Butir yang tidak ikut pada satu kali tulis **tetap PENDING**, menunggu perintah berikutnya. Butir boleh
   ikut sebagian; tidak harus semua sekaligus.
4. Setelah menulis: baca balik halamannya, catat versi barunya di kolom Status tiap butir yang ikut,
   perbarui papan status di atas, dan catat di bagian **Riwayat penulisan** di bawah.

## Keputusan kerja (Bambang, 2026-09-21)

**建造单 di Confluence (pageId 2096463922) masih v33** — terakhir diubah 2026-09-20 14:55:49Z, diverifikasi
dari riwayat versinya. **Belum ada satu pun butir di halaman ini yang ditulis ke Confluence.**

Itu disengaja. Semua butir **ditampung di repo dulu, untuk satu kali update v33 → v34**. Alasan: batch
sekali tulis menjaga halaman tetap terbaca (kebiasaan halaman itu 原文保留不删 — tiap ronde menambah
paragraf bertanggal, jadi banyak ronde kecil membuat sel jadi tidak terbaca; ini persis penyakit yang
Alden suruh bereskan di 04.4 §十一 dengan c50273 ⑤ 「标准页只放结果」).

**Pemicu untuk menulis v34**: jawaban terbaru dari **Felix, Alden, Kayden, atau Kent** — di comment OSD-116
atau di #nos-bo. Sebelum itu, kerjanya hanya: pantau keempat sumber, tambah butir baru ke daftar ini.
**Tidak ada tulisan ke Confluence, Jira, atau Slack tanpa perintah eksplisit.**

## Status per baris 页首附表

Daftar 待办 / 阻塞中 yang kau susun di 建造单 sekarang punya cermin ber-status di
**`docs/buildsheet-blocker-status.md`** — 33 baris, tiap baris diuji terhadap **解除判据 baris itu sendiri**.
Hasil: **1 baris benar-benar tutup hari ini (baris 12)**, 9 baris bergerak tanpa 判据-nya terpenuhi,
23 baris tidak bergerak. Tally: 阻塞中 tetap 5, 待办 24 → 23, 已解封 4 → 5.

## Siapa yang kita tunggu (status terverifikasi 2026-09-22 ~09:31 WIB)

🔴 **Alden belum berkomentar di OSD-116 sejak 2026-09-10.** Diverifikasi 2026-09-21: namanya tidak muncul di 60
comment terbaru, yang mundur sampai 2026-09-10 12:58. Dicek ulang 2026-09-22 09:31 WIB: comment terbaru
sekarang c50328 (Felix), dan Alden tidak muncul di 8 comment terbaru. Dua permintaan kita menggantung padanya.

| Siapa | Yang ditunggu | Sejak | Sumber |
| --- | --- | --- | --- |
| **Alden** | Balasan **c50279** — Pattern-9 扩展 (6 blok + 4 add-on + catatan Data Table). Ini yang mengunci 页首附表 baris 3 (阻塞中) dan N07. | 2026-09-21 15:17 | OSD-116 c50279 |
| **Alden** | Balasan **c50237** — daftar field sisi 主单 (26 item → 35 field), termasuk 纪律记录有效期 yang butuh **2 field** (Final Written 永不自动失效 tidak bisa diwakili satu field date) dan dua 闭环闸 (离职单关联状态 / 下游流程触发状态) yang harus dibangun sebagai transition validator, bukan field biasa. Kent sudah menetapkan ini domain Alden/V1 (c50234 #2). | 2026-09-19 18:01 | OSD-116 c50237, c50234 |
| **Alden** | Registrasi 8 频道 di **04.11** = 判据② baris 6 建造单. 04.11 masih **v2** (2026-08-24), tidak bergerak di sapuan mana pun. | — | 04.11 v2; butir 2 |
| **Felix** | Menulis sendiri putusannya c50261 (2)(a)(b)(c) ke Spec — 权 tulis Spec ada padanya (04.5 §五). Kent c50238: 「Since S-05 is frozen, Felix decides whether they warrant a Spec change.」 (a) HR判定依据 append-only + timestamp + source-node tag; (b) N17 HR判定依据 wajib untuk ketiga outcome, D-9 【Result Summary】 menarik dari situ; (c) flag 疑似重复 + link Case asal harus tampak di layar review N07. | 2026-09-21 11:56 | OSD-116 c50261, c50238 |
| **Kayden** | Apakah N28 perlu pengecualian terhadap 04.3 §六 互斥 — dirutekan oleh **c50263** kita. Belum dibalas. | 2026-09-21 12:30 | OSD-116 c50263 |
| **Kayden** | Menulis urutan 切 active ke **OS 开发流 Spec** (masih v39). Sudah diputus di #nos-bo, belum turun ke halaman. | 2026-09-19 17:04 | #nos-bo thread 1789704362.435989 |
| **Kayden** | 04.1 / 04.8 转正式登记 untuk Registry 纪律处分记录 (Option C). Kent c50257: 「04.1/04.8 转正式登记归你侧派人」, dan dia akan mengawal sampai tutup. | 2026-09-21 11:08 | OSD-116 c50255, c50257 |
| **Kayden / Alden** | Menyetujui dua draf Kent (04.10 §二 权责判定标准; 改动分级三层文案). Kalau yang kedua turun, **暗号表 建造单 ini ikut kena** + 04.12 tambah satu baris. → butir 16. | 2026-09-21 13:41 / 13:59 | #nos-bo thread yang sama |
| **Kent** | Membuat 13 field, memasang screen, dan mendaftarkannya di 04.10 §三 dengan bukti — **sisi Schema Owner, bukan kita** (c50290). Sebelum itu kita tidak bisa API 回读 maupun mengonsumsinya. | 2026-09-21 17:18 | OSD-116 c50290 |

**Catatan**: Kent c50256 (Mode-5 ordering → Alden) sudah **kita tarik sendiri** lewat c50263, jadi bukan lagi
hal yang kita tunggu dari Alden; sisanya (apakah N28 perlu pengecualian §六) ada di baris Kayden di atas.

**Sudah dijawab, keluar dari daftar tunggu (2026-09-22)**: baris **Felix** soal 「PIP「延长周期」是否就 15/30/60/90
四档」 (一问 Kent di akhir c50290). Felix **c50328** (2026-09-22 08:37 +07) menjawab 「确认，PIP「延长周期」就维持
15 / 30 / 60 / 90 天四档，不开放「视情况」填写其他天数」 dan 「可以按 option 锁定」. Sisa rantai ini ada di baris
**Kent** di atas (membuat field, memasang screen, mendaftar 04.10). → butir **17**.

## Yang TIDAK menunggu siapa pun — bisa dikerjakan kapan saja

> **Dibetulkan 2026-09-22 atas perintah Bambang.** Versi sebelumnya bagian ini mendaftarkan **N28 方向 2**,
> **N5 建库** dan **“memberi tahu Felix testing sudah selesai”** sebagai pekerjaan yang bisa jalan kapan saja.
> Ketiganya tidak benar; alasan per butir ada di bawah. Yang tersisa sebagai pekerjaan sisi kita hanya
> baris 28, dan itu sudah diverifikasi live hari ini.

**Satu-satunya pekerjaan build S-05 yang tidak menunggu siapa pun: sisa 页首附表 baris 28.**

Baris 28 statusnya **已解封 (2026-09-18)**, kolom 依赖谁 = **「建造侧」** (tanpa nama orang lain), dan
解除判据-nya sendiri menyisakan dua hal verbatim: 「其中三条转换的 `hasScreen`／`isConditional` **待补 API
回读**，四条终态转换**待实跑**」. Di 第八区 tabel 「尚未测试」 dua baris teratas ya itu:

| Celah | Isinya |
| --- | --- |
| 四条终态转换实跑 + Resolution post function | `Reject`(3) · `Withdraw`(8) · `Cancel as Duplicate`(9) · `Abort Case`(11) — 「每条各需一张 TEST 单（单据入终态即止）。先例 GPM 用 11 张」 |
| 三条转换属性 API 回读 | `Create`(1) · `Complete`(10) · `Abort Case`(11) — 「单据进入终态后不可再读，须在上一行补测时于 Pending Sub-tickets 态一并取得」 |

Dasar bolehnya jalan — **baris 26, juga 已解封**: Kent c50198 「可先建 Jira 骨架（Issue Type、Workflow
状态链、字段、转换）」, c50073 「全量并行建设，不是阻塞」, dan 「建造人账号已实测持有 Jira admin
settings…边建边登记、Alden 验收后置」.

**Diverifikasi live 2026-09-22, sebelum 09:31 WIB** (bukan dari halaman):
- JQL `project = SSCSD AND issuetype = "Disciplinary Case"` → **hanya satu tiket**: SSCSD-411, status
  `Completed` (10593), resolution `Done` (10000), reporter＝assignee＝Backend Operations. Jadi empat transisi
  terminal itu memang belum pernah dijalankan sekali pun.
- `getTransitions(SSCSD-411)` → **`transitions: []`**. Jadi betul: dari tiket itu tiga atribut tadi sudah tidak
  bisa dibaca lagi. Harus tiket TEST baru, dibaca ketika tiketnya di Pending Sub-tickets.

Empat catatan sebelum dikerjakan:
1. 04.5.3: 测试单留终态不删 → tiap tiket TEST **permanen** di SSCSD. Tindakan tidak bisa dibatalkan, jadi
   07.06.1 §六-2 minta izin eksplisit pemilik repo.
2. SSCSD punya aturan penugasan bawaan — SSCSD-411 waktu dibuat diassign ke Alden lalu diubah balik ke
   Backend Operations (tercatat di 第八区). Tiap tiket baru akan mampir sebentar di queue Alden.
3. `Create`(1) tidak pernah muncul di daftar transisi sebuah tiket, di status apa pun — jadi angka
   `hasScreen`/`isConditional`-nya **tidak dijanjikan** dari endpoint tingkat tiket. Yang pasti bisa:
   `Complete`(10) dan `Abort Case`(11) saat tiket di Pending Sub-tickets.
4. `Abort Case`(11): kolom 允许执行者-nya di 区二 masih 「本批未配置」 jadi teknis bisa dijalankan, tapi node
   N28-nya masih punya pertanyaan terbuka di Kayden (baris 19). Kalau transisi ini ditahan, atribut API
   transisi 11 ikut tertunda karena dibaca dari status yang sama.

**Kerja meja yang juga tidak menunggu siapa pun** (di repo, tidak menyentuh Confluence/Jira/Slack):
- Susun ulang pembelahan **16 baris tabel C** Spec v62 menurut 04.4 §8.1 (「这个被计时的对象在不在 SSCSD
  里」). Angka lama di daftar aksi tidak berdiri (「13 dari 16」 sebenarnya 12; pembelahan 「1 JSM / 15 n8n」
  tidak lolos §8.1), jadi ini harus dibangun ulang sebelum dipakai. Tidak butuh field jam kerja NTP.
- **区四 Automation 规则清单** masih 🔲 待填, dan 填写前置-nya ditulis di halaman itu sendiri: 「须先实读 04.4
  模式库（模式四／五／七／八），命名依 04.4 §十」. Pembacaan dan penyusunan draftnya bisa sekarang.
  Apakah aturannya boleh benar-benar **dibangun** belum dicek — tidak diklaim di sini.
- Rancangan baris 13 (target whitelist + bentuk 测试标识 04.5.3 §三) memang 「名单内自决」, jadi rancangannya
  bisa dibereskan; pemasangannya tetap menunggu 04.9 分册 S-05 (Alden).

**Tiga butir yang dulu ada di sini dan ternyata terkunci:**

| Dulu ditulis di sini | Kenyataannya |
| --- | --- |
| **N28 方向 2** — konfigurasi izin transisi `Abort Case` ke role group HR Ops & Data + 守护件 | **Dua-duanya terkunci.** Izin transisi → **Kayden**: 04.3 v33 §六 untuk pintu itu berbunyi 「仅服务账号与该主单所在 Project 的 Owner」, HR Ops & Data tidak di dalamnya, sedangkan kalimat pembuka §六 「不设限制的转态视为配置未完成」; lebih keras lagi 撤回规则 §六 「全关子单中只要有一张「已完成」，走模式五自动转「已完成」，**不得再走本条中止路径**」. Dirutekan lewat c50263, belum dijawab. 守护件 → **Alden**: 04.9 §三 cuma punya enam 分册, **tidak ada untuk S-05**, sedangkan §一 铁律 三位一体 「缺任一项视为未完成」. → sekarang **B-16** di `docs/action-list.md` |
| **N5 建库** untuk Registry 纪律处分记录 Option C | **Terkunci.** Perintahnya ada (Kayden c50244 「请按 N5 正式建库」, Kent c50255), tapi registrasinya belum turun: 04.1 v46 §一 baris itu masih 「**候选｜待N5**」, Project key 🔲, Owner 🔲. §1.1: 「该状态不可被 Spec、自动化或 **BO** 当作可执行 key」 dan 「N5 人工裁决：仅 Kayden 或 Alden…**BO 无此写权**」; §二: 「查不到已裁决的对应行…**停止建设并退回补齐**」. c50244 sendiri menugaskan 「04.1、04.8 两行由 **Kayden 侧派人**转正式登记」. → sekarang **B-19** |
| **Memberi tahu Felix kalau testing sudah selesai** | **Tidak ada testing yang bisa disebut selesai.** Sampai hari ini belum ada satu pun tes yang dijalankan di S-05 selain 结构测试 2026-09-18; pembacaan daftar anggota channel adalah pengecekan prasyarat, bukan tes. Verifikasi kirim-nyata mustahil sebelum komponennya ada — semua pembangunan n8n S-05 terkunci di 04.9 分册 (B-08), dan baris 13 melarang kiriman tes ke `#sscos-hr` (04.5.3 §二 garis merah). Jadi mengabari Felix 「testing selesai」 sekarang tidak benar. Selain itu ia **tindakan keluar** — tetap butuh perintah pemilik repo, jadi bukan 「bisa dikerjakan kapan saja」 |

| # | Status | Lokasi di 建造单 | Yang salah / berubah | Teks yang diusulkan (tambahan bertanggal) | Sumber |
| --- | --- | --- | --- | --- | --- |
| 1 | ⏳ PENDING | 页首附表 baris 19 (N28 案件失效中止的执行人), paragraf 「【2026-09-20 补·04.3 §六 原文的后半句本行此前未录…】」 | Keterangan 「本行此前未录」 tidak benar. Kutipan utuh §六 ada di baris ini sejak v8 (2026-09-18) sampai v27; terpotong di v28 (2026-09-19, ±1 jam setelah c50233); dikembalikan di v31. | 「【2026-09-21 订正｜上句原文保留不删】「本行此前未录」不实：本行自 v8（2026-09-18）至 v27 均载有该句完整原文（含「不得再走本条中止路径」），v28（2026-09-19，c50233 之后约一小时）改写本行时被截至「互斥」，v31 补回。另见 OSD-116 c50263 对 c50233 的更正。」 | Riwayat versi 建造单 (diff v7→v8, v27→v28; pesan versi v31); OSD-116 c50263 |
| 2 | ⏳ PENDING | 页首附表 baris 6 (七个部门 Collab 频道), kolom 事项 / 解除判据 | 判据 ① dan ③ sudah terpenuhi. 2026-09-21 dibaca via Slack API (read-only, ids_only, include_bots): SSCOS-Bot U0BCPFHGURE ada di ketujuh channel (C0AQ50LC2UE, C0AQ725CVFU, C0AQ3K4T28M, C0AQ0KR5691, C0AQKUBM0PK, C0AQ3L4QZ4M, C0APRJFRFT9) dan di sscos-hr (C0BHL8AE68G). Felix c50261 butir 3 menyatakan bot sudah ditambahkan. 判据 ② (04.11 登记, Alden) masih terbuka. Status tetap 待办. | 「【2026-09-21 补】判据①③已成立：建造侧 2026-09-21 以本人账号只读回读成员名单，@sscos-bot（U0BCPFHGURE）已在七个频道与 sscos-hr 名单内（Felix c50261 第 3 点）。余判据②（04.11 登记）待 Alden。」 | Slack member read 2026-09-21; OSD-116 c50261 |
| 3 | ⏳ PENDING | 页首附表 baris 12 (Inz9／Marketing 两个 Collab 频道是否仍使用) | Felix c50261 butir 4: kedua channel tetap dipakai terpisah, tidak digabung ke collab-hr-crm (alasan: kepala kedua departemen tidak ada di collab-hr-crm; hindari kepadatan). Bagian bisnis selesai; pendaftaran 04.11 tetap Alden. | 「【2026-09-21 补】Felix c50261 第 4 点：两频道继续分别使用，不并入 collab-hr-crm。业务口径已定；04.11 登记仍待 Alden。」 Status: 待办 → boleh dipertimbangkan 已解封 untuk bagian bisnis (keputusan builder saat update). | OSD-116 c50261 |
| 4 | ⏳ PENDING | 页首附表 baris 5 (两个 Request Type 双语名称未确认) | Felix c50261 butir 1 memberi nama: SUBMIT 「提交纪律处置申请 · Submit Disciplinary Case」; EVENT 「纪律与绩效事件触发 · Disciplinary & Performance Event Trigger」. 解除判据 belum terpenuhi: 04.7 v45 baris SUBMIT masih 「提交纪律与绩效改进处置申请」 (nama Mandarin berbeda), baris EVENT belum ada nama; 04.7 §四 名称一致 mensyaratkan Spec/04.7/platform sama. Status tetap 阻塞中 sampai 04.7 diselaraskan. | 「【2026-09-21 补】Felix c50261 第 1 点已给出双语名（见左）。04.7 v45 两行尚未回填且 SUBMIT 中文名与 04.7 现行不同，名称一致（04.7 §四）未成立，本行仍阻塞。」 | OSD-116 c50261; 04.7 v45 |
| 5 | ⏳ PENDING | 页首附表 baris 18 (形状 C 是否须配「已改道」出口), kolom 依赖谁 | Tertulis 「Alden（04.3 Owner）＋Felix（Spec）」. Owner 04.3 adalah Kayden Lee (04.3 维护说明; 04 v25 §六). Baris 19 sudah benar menulis Kayden. | 「【2026-09-21 订正｜原文保留不删】04.3 Owner＝Kayden Lee（04.3 页尾维护说明），非 Alden。」 | 04.3 v33 维护说明; 04 v25 |
| 6 | ⏳ PENDING | 页首附表 baris 19 (N28), bagian 「抢跑约束待 Alden 背书」 | Setelah c50263, permintaan "before, or atomically with" ditarik dari sisi builder. Pertanyaan yang tersisa: apakah N28 perlu pengecualian terhadap 04.3 §六 互斥 (Owner 04.3 = Kayden). Kent c50256 ke Alden masih terbuka. | 「【2026-09-21 补】建造侧已于 OSD-116 c50263 撤回「先转主单已取消、再取消子单」的抢跑约束；余下问题为 N28 是否需对 04.3 §六 互斥条设例外，归 04.3 Owner。」 | OSD-116 c50263 |
| 7 | ⏳ PENDING | 已实读的规范源 (页首) | Tambah bacaan 2026-09-21: OSD-116 c50255–c50263; #nos-bo (26 pesan + 8 thread); 04.0 v26 §三 riwayat; 04.3 v33 §六 riwayat v31; 建造单 riwayat versi v3–v33. | 「2026-09-21 增读：OSD-116 c50255～c50263；#nos-bo 全部消息与线程；04.0 v26／04.3 v33 版本历史；本页 v3～v33 版本差异。」 | notes/reading.md |
| 8 | ⏳ PENDING | 页首附表 baris 30 (四条原地转换使模式九重复裁决主锁失效), kolom 事项 kalimat terakhir | Tertulis 「副锁（marker 回扫）与轮次防过期在 Notify §9.4 与 04.4.1 两页均登记「未实现」」. Sumber tidak menyamakan keduanya: 04.4.1 v13 「已登记的未实现项」 menulis 幂等标记回扫 = 「未实现」 tetapi 轮次防过期 = 「🔲 待定，勿当已生效」; Notify 契约 v13 版本表 menulis 「§9.4 副锁幂等标记只写不扫…；§9.4 轮次防过期 🔲 待定」. Dampak praktis sama (keduanya tidak melindungi hari ini), tapi kata harus ikut sumber. | 「【2026-09-21 订正｜原文保留不删】「均登记「未实现」」不准确：04.4.1 v13 与 Notify 契约 v13 均记 幂等标记回扫＝未实现、轮次防过期＝「🔲 待定，勿当已生效」（未定，非未实现）。OSD-116 c50279 (b) 已按此口径写。」 | 04.4.1 v13 「已登记的未实现项」; Notify 契约 v13 版本表 v5 行与 §9.4; OSD-116 c50279 |
| 9 | ⏳ PENDING | 建设备注 — daftar 「07.06.1 命中条目 A2/A3/A6/A4/A8/C1/E11/E16/E9/D3/D7」 | 07.06.1 naik v33 → **v34** (2026-09-21 07:11Z, msg 「E16 探针订正；E6 订正；新增 C9」). Daftar 命中条目 kita disusun terhadap v33. Tiga butir berubah isi, dan satu butir baru kena jalur S-05. | 「【2026-09-21 补】07.06.1 已升 v34（本条原按 v33 命中）。本次三项变动：① 新增 **C9**（Slack 三秒窗口：响应动作之前不排 Code 节点），主题速查表「发通知、发邮件、发 Slack」行已由 C1–C6 改为 C1–C6、C9 —— S-05 N03 入口一为 Slack 表单（04.7 本行「载体为Slack表单」），故本条 命中条目 增列 **C9**；② **E6 口径反转**，原「dry-run 会 pin 掉 HTTP 请求」改为「test_workflow 不会替你 pin 掉带凭据的节点，它会真发」，本侧今后一切干测须显式停用写／发节点或显式传 pinData，并核该次执行 pinData 是否为空；③ **E16 订正**，禁止以 /rest/api/3/mypermissions 的 BROWSE_PROJECTS 代替对照探针（单据级 issue security 会令 JQL 恒回空集而权限仍回 true），探针须查一张已知存在的单，且该单为**承重对象**、其用途须在本建造单登记。」 | 07.06.1 v33→v34 diff (additions 15 / deletions 7) |
| 10 | ⏳ PENDING | 区六 平台件表 — baris 身份件 (Submission Identity Verifier) | Tercatat 在建·影子·inactive. Sejak 2026-09-21 07:52Z sudah **active·已发布**: 04.9 v106 menambah baris index-nya, 04.9.1 v19 menulis versionId＝activeVersionId `616bbd91-5cd7-4c10-bcc4-ae9052592253`, 5 节点, nama sudah dibuang sufiks 「DO NOT ACTIVATE · shadow」. | 「【2026-09-21 补】本件已发布：04.9 v106 索引行新增、04.9.1 v19 状态改 **active·已发布**（versionId＝activeVersionId 616bbd91-5cd7-4c10-bcc4-ae9052592253，5 节点）。04.9.1 v19 并记真实链四例：真上级 identityOk；非上级按业务拒、不告警；**档案查不到**与**档案重复**两种均 fail-closed 且 mustAlert。⚠️ 04.4 §十一 该行与 04.4.3 v6 契约页**仍写「在建·影子·inactive」**，与 04.9／04.9.1 不一致，归 Alden（见 findings F-006）。」 | 04.9 v103→v106 diff; 04.9.1 v17→v19 diff |
| 11 | ⏳ PENDING | 区六 平台件表 — baris 协作 Thread (Collaboration Thread) | Tercatat 在建 (tidak dipakai S-05). Sejak 2026-09-21 statusnya 可用 (Alden NSE-1143 c50273), 04.4 §十一 sudah diubah, halaman kontrak 04.4.4 naik v1 → v4. Tetap inactive dan 零真跑. | 「【2026-09-21 补】04.4 §十一 该行状态已改「可用」（Alden NSE-1143 c50273 验收），契约页 04.4.4 现行 v4。仍 inactive、至今零真跑，S-05 不消费本件，本行仅同步状态。」 | 04.4 v31→v33 diff; 04.4.4 v4 正文 |
| 12 | ⏳ PENDING | 页首附表 baris 5 (两个 Request Type 双语名称) — pelengkap butir 4 di atas | Butir 4 menyebut 「04.7 v45」. 04.7 sudah **v46** (2026-09-21 06:56Z). Perlu dipastikan agar catatan tidak menyebut versi kedaluwarsa. Isi tidak berubah: diff v45→v46 hanya menyentuh baris RT-HR-RECRUITMENT-SUBMIT dan menambah RT-HR-RECRUITMENT-OFFERWITHDRAW; **kedua baris S-05 tidak berubah satu huruf pun**, keduanya tetap 「候选」. | 「（写 v34 时把butir 4 的「04.7 v45」改为「04.7 v46（2026-09-21 实读）」；结论不变：两行 S-05 逐字未动，仍 候选，名称一致未成立。）」 | 04.7 v45→v46 diff |
| 13 | ⏳ PENDING | 页首附表 baris 3 (模式九扩展, 阻塞中) · 区一 N07 行 · 区六 | **c50279 sudah terkirim** ke Alden (2026-09-21 15:17). Belum ada balasan Alden sampai 18:30 WIB (diverifikasi: OSD-116 total 163 comment, terbaru tetap c50290). Baris-baris yang dirujuk c50279 belum diberi catatan 「已发出」. | 「【2026-09-21 补】模式九扩展项已按 Kent c50227 ② 汇总为一份请求发出：OSD-116 **c50279**（→ Alden，cc Kent），含六块本体＋四项 add-on（(a) N03 分派钩子 flow 值 `disciplinary-n03`；(b) 原地转换幂等——本侧自建，另请在共享卡表「被哪些 workflow 引用」列补 S-05；(c) 身份件走向；(d) edit 屏前置）＋Data Table 说明。**截至 2026-09-21 18:30 WIB 未获回复，本行仍 阻塞中。**」 | OSD-116 c50279; 评论清单回读 2026-09-21 18:30 WIB |
| 14 | ⏳ PENDING | 区一 各子单字段行 · 区六 · 页首附表（字段类阻塞行） | **Kent c50290 已批准全部 13 个字段**，并给三处类型裁定、两条建设约束、一处入口裁定与角色分工。建造单尚未登记这一结论。 | 「【2026-09-21 补·依 OSD-116 c50290】Schema Owner Kent 审批结论：**13 项全部准予按「新共享对象」登记**（其已逐项现读 04.10 v19 §三 总表反重复）。三处类型裁定：①「Warning 生效信息」**只登 Warning Effective Date（date）一个字段**，「有效/重置规则」不另设字段——「发 D-6/D-11 时由卡从主单读（Warning 等级＋纪律记录有效期）当场 derive 出【Validity/Reset Rule】文案」，🔴 **本侧因此多一项建设要求：卡需跨单读**；②「PIP 延长周期」定为 **option（15/30/60/90 天）**，非 number，**待 Felix 确认「就 4 档」后锁定**；③其余按本侧所拟。两条建设约束：**Check-in 记录需跨 7 个部门 Team Project 的 context（非 HR-only）**；**判定依据类型两值须与离职流「辞退原因」(Felix c50045) 逐字对齐**。入口裁定：本批走 c48074 轻量入口，**经 Kent 裁定例外不转开 Task**，登记本体落 04.10 §三 总表、按 §2 先登记后启用、于字段建成＋API 回读后补入带证据的登记行。角色分工：**13 个字段的创建、挂屏与 04.10 登记归 Schema Owner 侧（Kent），本侧只负责流程建设与消费**（同 Grade / cf18152-153 分工）。」 | OSD-116 c50290 |
| 15 | ⏳ PENDING | 页首附表（新增一行「上线次序：切 active 的位置」） · 区九 | Kayden 在 #nos-bo 2026-09-19 17:04 裁定：验收关（N13/N14）与工程审关（切 active）是两道关；并说 「切 active 放在 N14 通过之后、N15 上线之前。这个顺序我会写进 OS 开发流 Spec。」 **OS 开发流 Spec 现行仍 v39，尚未写入**，所以这是已裁未落页。 | 新增待办/阻塞行 —— 事项：「S-05 各 n8n 件切 active 的次序；Kayden 已裁「N14 通过之后、N15 上线之前」，且明确工程审关与验收关是两道关、Alden 拨开关时只核 04.9 登记与守护配置」｜依赖谁：Kayden（落 OS 开发流 Spec）｜解除判据：OS 开发流 Spec 出现该次序条款（现行 v39 无）｜不做的后果：上线批次次序无成文依据，可能与平台侧预期不符｜状态：待办。**来源为 Slack 裁定，非标准页；按 07 §二「Confluence 当前权威页是规则事实」，落页前不得当成已生效规则。** | #nos-bo thread 1789704362.435989 回复 3（Kayden 2026-09-19 17:04）；OS 开发流 Spec v39 |
| 16 | 👁 PANTAU | （仅作观察登记，暂不改任何行） | 两份会影响本建造单的草稿已出但**未获批**：① Kent 2026-09-21 13:41 的 **04.10 §二 权责判定标准**草稿（Canvas F0C32N7MYR1）；② Kent 2026-09-21 13:59 的 **改动分级三层文案**草稿（Canvas F0C2TLMGST1），核心机制「拆两个版本号（页面版本号 vs 判据基线号；小改不停机、大改才停）」，Kayden 裁定其停机规则落 **07.04 §10.1**、机器识别方式写进**建造单的暗号表**、**04.12 同步加一行**。 | 暂不写入建造单。待 Kayden 批、Alden 点头并实际落页后，再按落页版本消费。若②落地，本页 **暗号接口契约表**（8 个 `nos-s05-*`）需同步。 | #nos-bo thread 1789704362.435989 回复 3／4／5 |

| 17 | ⏳ PENDING | 区一 各子单字段行（pelengkap butir 14） | Butir 14 menulis 「「PIP 延长周期」定为 **option（15/30/60/90 天）**，非 number，**待 Felix 确认「就 4 档」后锁定**」. Syarat itu sudah turun 2026-09-22, jadi catatan butir 14 tidak boleh lagi ditulis ke halaman dengan kalimat 「待 Felix 确认」. | 「【2026-09-22 补·依 OSD-116 c50328】Felix 已答 Kent c50290 文末一问，逐字：「**确认，PIP「延长周期」就维持 15 / 30 / 60 / 90 天四档，不开放「视情况」填写其他天数**」；「延长后的周期继续沿用现有 C-10 对应的 Check-in 频率规则即可，**可以按 option 锁定**」。故本字段类型定案为 **option 四值（15／30／60／90 天）**，C-10 Check-in 频率规则不另立。**字段的创建、挂屏与 04.10 登记仍归 Schema Owner 侧（Kent，c50290 角色分工），建造侧只消费。**（写 v34 时同步把butir 14 的「待 Felix 确认「就 4 档」后锁定」改为「已由 c50328 确认，类型锁定为 option 四值」。）」 | OSD-116 c50328；c50290 文末一问 |

## Riwayat penulisan ke Confluence

| Tanggal | Versi | Butir yang ikut | Diperintahkan oleh |
|---|---|---|---|
| — | — | belum ada | — |

## Terkait, sudah terkirim ke Jira (bukan ke halaman 建造单)

Bagian ini soal **komentar OSD-116**, bukan soal halaman 建造单. Status PENDING／COMPLETED di tabel butir
di atas **tidak** dipengaruhi olehnya — komentar terkirim tidak berarti halaman sudah diperbarui.

Status per 2026-09-21 18:30 WIB, diverifikasi dari daftar comment live:
- **c50279** (15:17) Pattern-9 consolidated request → Alden, cc Kent. **Belum dibalas.** → butir 13.
- **c50283** (15:59) 04.10 three-cell request → Kent, cc Alden. **Sudah dibalas: c50290, disetujui penuh.** → butir 14.
- **c50263** (12:30) Correction → Kayden, cc Kent/Alden (N28 抢跑约束 ditarik). → sudah tercermin di butir 6.
- Comment terbaru di OSD-116 tetap **c50290**; total comment 163. Tidak ada balasan Alden atas c50279 maupun atas Kent c50256.

**Diperbarui 2026-09-22 09:31 WIB** (dibaca live, `-created`, 8 comment teratas): comment terbaru sekarang
**c50328** — Felix, 08:37 +07, ditujukan ke Kent, soal empat tingkat PIP 「延长周期」. Total comment **164**.
Jadi hanya **satu** comment baru sejak c50290. Alden tidak muncul di 8 comment teratas: c50279 dan Kent
c50256 tetap belum dibalas.

## Belum masuk daftar (menunggu keputusan pemilik lain)
- 04.7 dua baris nama Request Type: milik Felix/Alden, bukan 建造单.
- Spec v62: putusan Felix c50261 butir 2 (a)(b)(c) harus ditulis Felix sendiri (04.5 §五).
- 引用区「对应建造单」backfill dan status 建设中: tindakan BO di Spec, terpisah dari update 建造单 ini.
