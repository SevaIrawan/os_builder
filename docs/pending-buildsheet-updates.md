# 建造单 (2096463922) — daftar pembaruan, dengan status per butir

> Catatan kerja builder (Bambang). Setiap butir memakai kebiasaan halaman: 原文保留不删, tambah catatan bertanggal.
> Disusun 2026-09-21. Sumber tiap butir disebut di baris masing-masing.

## Papan status

| | |
|---|---|
| **Versi halaman 建造单 sekarang** | **v37** (2026-09-22 06:53:16.294Z) — ditulis lewat akun Bambang, jalur `edits` node-level |
| **⏳ PENDING** (menunggu, belum ditulis ke Confluence) | **1** — butir 11 (sasarannya tidak ada di halaman; menunggu putusan Bambang) |
| **✅ COMPLETED** (sudah ditulis ke Confluence) | **26** |
| **👁 PANTAU** (tidak mengubah baris apa pun, cuma diawasi) | **1** — butir 16 |
| **Terakhir ditulis ke Confluence** | **2026-09-22 06:53:16Z — v36 → v37** (butir 22–28, 14 operasi: 9 `replaceNode` ＋ 5 `insertNodeAfter`). Sebelumnya **06:41:40Z — v35 → v36** (butir 21, satu `replaceNode`, diff additions 1 / deletions 1). Sebelumnya **06:37:03Z — v34 → v35** (butir 15, satu `insertNodeAfter`, diff additions 1 / deletions 0). Sebelumnya **06:27:52Z — v33 → v34**, 15 operasi `edits` (11 `replaceNode` ＋ 4 `insertNodeBefore`). Didahului `dryRun` yang lulus uji balik: hasil dikurangi sisipan sama persis dengan v33, 1.964 `data-local-id` lama utuh, nol hilang |

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
| 1 | ✅ COMPLETED 2026-09-22 · mendarat di **v34** (06:27:52Z) · bukti baca-balik: `diffConfluenceContentVersions` v33↔v34 sisi server, additions 19 / deletions 11 | 页首附表 baris 19 (N28 案件失效中止的执行人), paragraf 「【2026-09-20 补·04.3 §六 原文的后半句本行此前未录…】」 | Keterangan 「本行此前未录」 tidak benar. Kutipan utuh §六 ada di baris ini sejak v8 (2026-09-18) sampai v27; terpotong di v28 (2026-09-19, ±1 jam setelah c50233); dikembalikan di v31. | 「【2026-09-21 订正｜上句原文保留不删】「本行此前未录」不实：本行自 v8（2026-09-18）至 v27 均载有该句完整原文（含「不得再走本条中止路径」），v28（2026-09-19，c50233 之后约一小时）改写本行时被截至「互斥」，v31 补回。另见 OSD-116 c50263 对 c50233 的更正。」 | Riwayat versi 建造单 (diff v7→v8, v27→v28; pesan versi v31); OSD-116 c50263 |
| 2 | ✅ COMPLETED 2026-09-22 · mendarat di **v34** (06:27:52Z) · bukti baca-balik: `diffConfluenceContentVersions` v33↔v34 sisi server, additions 19 / deletions 11 | 页首附表 baris 6 (七个部门 Collab 频道), kolom 事项 / 解除判据 | 判据 ① dan ③ sudah terpenuhi. 2026-09-21 dibaca via Slack API (read-only, ids_only, include_bots): SSCOS-Bot U0BCPFHGURE ada di ketujuh channel (C0AQ50LC2UE, C0AQ725CVFU, C0AQ3K4T28M, C0AQ0KR5691, C0AQKUBM0PK, C0AQ3L4QZ4M, C0APRJFRFT9) dan di sscos-hr (C0BHL8AE68G). Felix c50261 butir 3 menyatakan bot sudah ditambahkan. 判据 ② (04.11 登记, Alden) masih terbuka. Status tetap 待办. | 「【2026-09-21 补】判据①③已成立：建造侧 2026-09-21 以本人账号只读回读成员名单，@sscos-bot（U0BCPFHGURE）已在七个频道与 sscos-hr 名单内（Felix c50261 第 3 点）。余判据②（04.11 登记）待 Alden。」 | Slack member read 2026-09-21; OSD-116 c50261 |
| 3 | ✅ COMPLETED 2026-09-22 · mendarat di **v34** (06:27:52Z) · bukti baca-balik: `diffConfluenceContentVersions` v33↔v34 sisi server, additions 19 / deletions 11 | 页首附表 baris 12 (Inz9／Marketing 两个 Collab 频道是否仍使用) | Felix c50261 butir 4: kedua channel tetap dipakai terpisah, tidak digabung ke collab-hr-crm (alasan: kepala kedua departemen tidak ada di collab-hr-crm; hindari kepadatan). Bagian bisnis selesai; pendaftaran 04.11 tetap Alden. | 「【2026-09-21 补】Felix c50261 第 4 点：两频道继续分别使用，不并入 collab-hr-crm。业务口径已定；04.11 登记仍待 Alden。」 Status: 待办 → boleh dipertimbangkan 已解封 untuk bagian bisnis (keputusan builder saat update). | OSD-116 c50261 |
| 4 | ✅ COMPLETED 2026-09-22 · mendarat di **v34** (06:27:52Z) · bukti baca-balik: `diffConfluenceContentVersions` v33↔v34 sisi server, additions 19 / deletions 11 | 页首附表 baris 5 (两个 Request Type 双语名称未确认) | Felix c50261 butir 1 memberi nama: SUBMIT 「提交纪律处置申请 · Submit Disciplinary Case」; EVENT 「纪律与绩效事件触发 · Disciplinary & Performance Event Trigger」. 解除判据 belum terpenuhi: 04.7 v45 baris SUBMIT masih 「提交纪律与绩效改进处置申请」 (nama Mandarin berbeda), baris EVENT belum ada nama; 04.7 §四 名称一致 mensyaratkan Spec/04.7/platform sama. Status tetap 阻塞中 sampai 04.7 diselaraskan. | 「【2026-09-21 补】Felix c50261 第 1 点已给出双语名（见左）。04.7 v45 两行尚未回填且 SUBMIT 中文名与 04.7 现行不同，名称一致（04.7 §四）未成立，本行仍阻塞。」 | OSD-116 c50261; 04.7 v45 |
| 5 | ✅ COMPLETED 2026-09-22 · mendarat di **v34** (06:27:52Z) · bukti baca-balik: `diffConfluenceContentVersions` v33↔v34 sisi server, additions 19 / deletions 11 | 页首附表 baris 18 (形状 C 是否须配「已改道」出口), kolom 依赖谁 | Tertulis 「Alden（04.3 Owner）＋Felix（Spec）」. Owner 04.3 adalah Kayden Lee (04.3 维护说明; 04 v25 §六). Baris 19 sudah benar menulis Kayden. | 「【2026-09-21 订正｜原文保留不删】04.3 Owner＝Kayden Lee（04.3 页尾维护说明），非 Alden。」 | 04.3 v33 维护说明; 04 v25 |
| 6 | ✅ COMPLETED 2026-09-22 · mendarat di **v34** (06:27:52Z) · bukti baca-balik: `diffConfluenceContentVersions` v33↔v34 sisi server, additions 19 / deletions 11 | 页首附表 baris 19 (N28), bagian 「抢跑约束待 Alden 背书」 | Setelah c50263, permintaan "before, or atomically with" ditarik dari sisi builder. Pertanyaan yang tersisa: apakah N28 perlu pengecualian terhadap 04.3 §六 互斥 (Owner 04.3 = Kayden). Kent c50256 ke Alden masih terbuka. | 「【2026-09-21 补】建造侧已于 OSD-116 c50263 撤回「先转主单已取消、再取消子单」的抢跑约束；余下问题为 N28 是否需对 04.3 §六 互斥条设例外，归 04.3 Owner。」 | OSD-116 c50263 |
| 7 | ✅ COMPLETED 2026-09-22 · mendarat di **v34** (06:27:52Z) · bukti baca-balik: `diffConfluenceContentVersions` v33↔v34 sisi server, additions 19 / deletions 11 | 已实读的规范源 (页首) | Tambah bacaan 2026-09-21: OSD-116 c50255–c50263; #nos-bo (26 pesan + 8 thread); 04.0 v26 §三 riwayat; 04.3 v33 §六 riwayat v31; 建造单 riwayat versi v3–v33. | 「2026-09-21 增读：OSD-116 c50255～c50263；#nos-bo 全部消息与线程；04.0 v26／04.3 v33 版本历史；本页 v3～v33 版本差异。」 | notes/reading.md |
| 8 | ✅ COMPLETED 2026-09-22 · mendarat di **v34** (06:27:52Z) · bukti baca-balik: `diffConfluenceContentVersions` v33↔v34 sisi server, additions 19 / deletions 11 | 页首附表 baris 30 (四条原地转换使模式九重复裁决主锁失效), kolom 事项 kalimat terakhir | Tertulis 「副锁（marker 回扫）与轮次防过期在 Notify §9.4 与 04.4.1 两页均登记「未实现」」. Sumber tidak menyamakan keduanya: 04.4.1 v13 「已登记的未实现项」 menulis 幂等标记回扫 = 「未实现」 tetapi 轮次防过期 = 「🔲 待定，勿当已生效」; Notify 契约 v13 版本表 menulis 「§9.4 副锁幂等标记只写不扫…；§9.4 轮次防过期 🔲 待定」. Dampak praktis sama (keduanya tidak melindungi hari ini), tapi kata harus ikut sumber. | 「【2026-09-21 订正｜原文保留不删】「均登记「未实现」」不准确：04.4.1 v13 与 Notify 契约 v13 均记 幂等标记回扫＝未实现、轮次防过期＝「🔲 待定，勿当已生效」（未定，非未实现）。OSD-116 c50279 (b) 已按此口径写。」 | 04.4.1 v13 「已登记的未实现项」; Notify 契约 v13 版本表 v5 行与 §9.4; OSD-116 c50279 |
| 9 | ✅ COMPLETED 2026-09-22 · mendarat di **v34** (06:27:52Z) · bukti baca-balik: `diffConfluenceContentVersions` v33↔v34 sisi server, additions 19 / deletions 11 | 建设备注 — daftar 「07.06.1 命中条目 A2/A3/A6/A4/A8/C1/E11/E16/E9/D3/D7」 | 07.06.1 naik v33 → **v34** (2026-09-21 07:11Z, msg 「E16 探针订正；E6 订正；新增 C9」). Daftar 命中条目 kita disusun terhadap v33. Tiga butir berubah isi, dan satu butir baru kena jalur S-05. | 「【2026-09-21 补】07.06.1 已升 v34（本条原按 v33 命中）。本次三项变动：① 新增 **C9**（Slack 三秒窗口：响应动作之前不排 Code 节点），主题速查表「发通知、发邮件、发 Slack」行已由 C1–C6 改为 C1–C6、C9 —— S-05 N03 入口一为 Slack 表单（04.7 本行「载体为Slack表单」），故本条 命中条目 增列 **C9**；② **E6 口径反转**，原「dry-run 会 pin 掉 HTTP 请求」改为「test_workflow 不会替你 pin 掉带凭据的节点，它会真发」，本侧今后一切干测须显式停用写／发节点或显式传 pinData，并核该次执行 pinData 是否为空；③ **E16 订正**，禁止以 /rest/api/3/mypermissions 的 BROWSE_PROJECTS 代替对照探针（单据级 issue security 会令 JQL 恒回空集而权限仍回 true），探针须查一张已知存在的单，且该单为**承重对象**、其用途须在本建造单登记。」 | 07.06.1 v33→v34 diff (additions 15 / deletions 7) |
| 10 | ✅ COMPLETED 2026-09-22 · mendarat di **v34** (06:27:52Z) · bukti baca-balik: `diffConfluenceContentVersions` v33↔v34 sisi server, additions 19 / deletions 11 | 区六 平台件表 — baris 身份件 (Submission Identity Verifier) | Tercatat 在建·影子·inactive. Sejak 2026-09-21 07:52Z sudah **active·已发布**: 04.9 v106 menambah baris index-nya, 04.9.1 v19 menulis versionId＝activeVersionId `616bbd91-5cd7-4c10-bcc4-ae9052592253`, 5 节点, nama sudah dibuang sufiks 「DO NOT ACTIVATE · shadow」. | 「【2026-09-21 补】本件已发布：04.9 v106 索引行新增、04.9.1 v19 状态改 **active·已发布**（versionId＝activeVersionId 616bbd91-5cd7-4c10-bcc4-ae9052592253，5 节点）。04.9.1 v19 并记真实链四例：真上级 identityOk；非上级按业务拒、不告警；**档案查不到**与**档案重复**两种均 fail-closed 且 mustAlert。**【2026-09-22 订正】** 此前本条写 04.4 §十一 与 04.4.3 「不一致，归 Alden」——**不准确，已撤回**。04.4 §十一 的「状态」列不是发布标志：其自身规则为「『在建』行由建设者开工时自登，**验收通过后**由建设者更新为『可用』」，同表 协作 Thread 行即为反证（状态「可用」而件「仍 inactive、至今零真跑」）。04.4.3 亦自载「验收：平台侧＝Alden；消费侧＝离职 N3＋Grade N3」，即验收未完成。故**已发布但未验收的件记为「在建」是正确的**，非漂移。**对本流程的实际意义相反**：建造单 baris 32 解除判据要的是「待其转**『可用』**后本流程方可建 N03 身份认证段」，而「可用」正是该列所报的事；读 04.4 §十一 得到的是**对的**答案。真正滞后的只有两句描述：04.4.3 页首仍写「本件自身仍 inactive」「影子·shadow」，04.4 §十一 该行仍带括注「随模式九批次上生产」。」 | 04.9 v103→v106 diff; 04.9.1 v17→v19 diff |
| 11 | ⏳ PENDING — **tidak ikut v34**: sasarannya baris 「协作 Thread」 **tidak ada** di 区六 建造单 (itu baris 04.4 §十一), dan butir ini sendiri menulis S-05 tidak memakai komponennya. Perlu putusan Bambang: digugurkan, atau dialihkan ke baris lain | 区六 平台件表 — baris 协作 Thread (Collaboration Thread) | Tercatat 在建 (tidak dipakai S-05). Sejak 2026-09-21 statusnya 可用 (Alden NSE-1143 c50273), 04.4 §十一 sudah diubah, halaman kontrak 04.4.4 naik v1 → v4. Tetap inactive dan 零真跑. | 「【2026-09-21 补】04.4 §十一 该行状态已改「可用」（Alden NSE-1143 c50273 验收），契约页 04.4.4 现行 v4。仍 inactive、至今零真跑，S-05 不消费本件，本行仅同步状态。」 | 04.4 v31→v33 diff; 04.4.4 v4 正文 |
| 12 | ✅ COMPLETED 2026-09-22 · mendarat di **v34** (06:27:52Z) · bukti baca-balik: `diffConfluenceContentVersions` v33↔v34 sisi server, additions 19 / deletions 11 — teksnya dilebur ke butir 4, tidak jadi butir tersendiri di halaman | 页首附表 baris 5 (两个 Request Type 双语名称) — pelengkap butir 4 di atas | Butir 4 menyebut 「04.7 v45」. 04.7 sudah **v46** (2026-09-21 06:56Z). Perlu dipastikan agar catatan tidak menyebut versi kedaluwarsa. Isi tidak berubah: diff v45→v46 hanya menyentuh baris RT-HR-RECRUITMENT-SUBMIT dan menambah RT-HR-RECRUITMENT-OFFERWITHDRAW; **kedua baris S-05 tidak berubah satu huruf pun**, keduanya tetap 「候选」. | 「（写 v34 时把butir 4 的「04.7 v45」改为「04.7 v46（2026-09-21 实读）」；结论不变：两行 S-05 逐字未动，仍 候选，名称一致未成立。）」 | 04.7 v45→v46 diff |
| 13 | ✅ COMPLETED 2026-09-22 · mendarat di **v34** (06:27:52Z) · bukti baca-balik: `diffConfluenceContentVersions` v33↔v34 sisi server, additions 19 / deletions 11 | 页首附表 baris 3 (模式九扩展, 阻塞中) · 区一 N07 行 · 区六 | **c50279 sudah terkirim** ke Alden (2026-09-21 15:17). Belum ada balasan Alden sampai 18:30 WIB (diverifikasi: OSD-116 total 163 comment, terbaru tetap c50290). Baris-baris yang dirujuk c50279 belum diberi catatan 「已发出」. | 「【2026-09-21 补】模式九扩展项已按 Kent c50227 ② 汇总为一份请求发出：OSD-116 **c50279**（→ Alden，cc Kent），含六块本体＋四项 add-on（(a) N03 分派钩子 flow 值 `disciplinary-n03`；(b) 原地转换幂等——本侧自建，另请在共享卡表「被哪些 workflow 引用」列补 S-05；(c) 身份件走向；(d) edit 屏前置）＋Data Table 说明。**截至 2026-09-21 18:30 WIB 未获回复，本行仍 阻塞中。**」 | OSD-116 c50279; 评论清单回读 2026-09-21 18:30 WIB |
| 14 | ✅ COMPLETED 2026-09-22 · mendarat di **v34** (06:27:52Z) · bukti baca-balik: `diffConfluenceContentVersions` v33↔v34 sisi server, additions 19 / deletions 11 | 区一 各子单字段行 · 区六 · 页首附表（字段类阻塞行） | **Kent c50290 已批准全部 13 个字段**，并给三处类型裁定、两条建设约束、一处入口裁定与角色分工。建造单尚未登记这一结论。 | 「【2026-09-21 补·依 OSD-116 c50290】Schema Owner Kent 审批结论：**13 项全部准予按「新共享对象」登记**（其已逐项现读 04.10 v19 §三 总表反重复）。三处类型裁定：①「Warning 生效信息」**只登 Warning Effective Date（date）一个字段**，「有效/重置规则」不另设字段——「发 D-6/D-11 时由卡从主单读（Warning 等级＋纪律记录有效期）当场 derive 出【Validity/Reset Rule】文案」，🔴 **本侧因此多一项建设要求：卡需跨单读**；②「PIP 延长周期」定为 **option（15/30/60/90 天）**，非 number，**待 Felix 确认「就 4 档」后锁定**；③其余按本侧所拟。两条建设约束：**Check-in 记录需跨 7 个部门 Team Project 的 context（非 HR-only）**；**判定依据类型两值须与离职流「辞退原因」(Felix c50045) 逐字对齐**。入口裁定：本批走 c48074 轻量入口，**经 Kent 裁定例外不转开 Task**，登记本体落 04.10 §三 总表、按 §2 先登记后启用、于字段建成＋API 回读后补入带证据的登记行。角色分工：**13 个字段的创建、挂屏与 04.10 登记归 Schema Owner 侧（Kent），本侧只负责流程建设与消费**（同 Grade / cf18152-153 分工）。」 | OSD-116 c50290 |
| 15 | ✅ COMPLETED 2026-09-22 · mendarat di **v35** (06:37:03Z) · `insertNodeAfter` pada `<tr>` terakhir `411da44320ce` · bukti baca-balik: `diffConfluenceContentVersions` v34↔v35 **additions 1 / deletions 0**, baris masuk di dalam tabel tepat sebelum paragraf 统计; tabel 33 → **34 baris**. (Percobaan pertama di v34 memakai `appendNodeToEnd` gagal tempat — ketahuan dari `dryRun`, tidak pernah tersimpan.) |
| 16 | 👁 PANTAU | （仅作观察登记，暂不改任何行） | 两份会影响本建造单的草稿已出但**未获批**：① Kent 2026-09-21 13:41 的 **04.10 §二 权责判定标准**草稿（Canvas F0C32N7MYR1）；② Kent 2026-09-21 13:59 的 **改动分级三层文案**草稿（Canvas F0C2TLMGST1），核心机制「拆两个版本号（页面版本号 vs 判据基线号；小改不停机、大改才停）」，Kayden 裁定其停机规则落 **07.04 §10.1**、机器识别方式写进**建造单的暗号表**、**04.12 同步加一行**。 | 暂不写入建造单。待 Kayden 批、Alden 点头并实际落页后，再按落页版本消费。若②落地，本页 **暗号接口契约表**（8 个 `nos-s05-*`）需同步。 | #nos-bo thread 1789704362.435989 回复 3／4／5 |

| 17 | ✅ COMPLETED 2026-09-22 · mendarat di **v34** (06:27:52Z) · bukti baca-balik: `diffConfluenceContentVersions` v33↔v34 sisi server, additions 19 / deletions 11 — teksnya dilebur ke butir 14, tidak jadi butir tersendiri di halaman | 区一 各子单字段行（pelengkap butir 14） | Butir 14 menulis 「「PIP 延长周期」定为 **option（15/30/60/90 天）**，非 number，**待 Felix 确认「就 4 档」后锁定**」. Syarat itu sudah turun 2026-09-22, jadi catatan butir 14 tidak boleh lagi ditulis ke halaman dengan kalimat 「待 Felix 确认」. | 「【2026-09-22 补·依 OSD-116 c50328】Felix 已答 Kent c50290 文末一问，逐字：「**确认，PIP「延长周期」就维持 15 / 30 / 60 / 90 天四档，不开放「视情况」填写其他天数**」；「延长后的周期继续沿用现有 C-10 对应的 Check-in 频率规则即可，**可以按 option 锁定**」。故本字段类型定案为 **option 四值（15／30／60／90 天）**，C-10 Check-in 频率规则不另立。**字段的创建、挂屏与 04.10 登记仍归 Schema Owner 侧（Kent，c50290 角色分工），建造侧只消费。**（写 v34 时同步把butir 14 的「待 Felix 确认「就 4 档」后锁定」改为「已由 c50328 确认，类型锁定为 option 四值」。）」 | OSD-116 c50328；c50290 文末一问 |

| 18 | ✅ COMPLETED 2026-09-22 · mendarat di **v34** (06:27:52Z) · bukti baca-balik: `diffConfluenceContentVersions` v33↔v34 sisi server, additions 19 / deletions 11 | 第八区 —「测试记录」表（加行）＋「测试单登记」表（加两行） | 2026-09-22 建造侧实跑两条终态转换，证据未登记。 | 「**结构测试（2026-09-22，Backend Operations，标题 TEST｜，不涉真实员工，测试单留终态不删）**」新增两行：①判据「回读验证（转换属性·API）」｜测试动作「读 SSCSD-421／SSCSD-422 于 Pending Approval 时的可用转换（`expand=transitions.fields`）」｜证据「两单各回八条（ID 2～9），`hasScreen: false`、`isConditional: false`、`fields: {}`；ID 4／5／6／7 另回 `isLooped: true`，机械印证四条原地转换。ID 1／10／11 仍未覆盖」；②判据「终态转换实跑与其 Resolution post function（04.3 §7.2）」｜测试动作「SSCSD-421 走转换 8 `Withdraw`；SSCSD-422 走转换 9 `Cancel as Duplicate`；SSCSD-423 走转换 3 `Reject`」｜证据「三单 changelog 各**仅一条记录、两个 item**（`status` ＋ `resolution`），无任何人工输入，与状态变更同一条 changelog，印证 §7.2 ①「由 post function 自动写入」：SSCSD-421／422 `status` 15855→**15961 Cancelled**、`resolution` null→**10041 Cancelled**（description「Process aborted (terminated by upstream)」），`resolutiondate` 10:05:57.894+07 与 10:05:49.311+07；SSCSD-423 `status` 15855→**15850 Rejected**、`resolution` null→**10042 Rejected**，`resolutiondate` 10:42:11.206+07。**04.3 §7.1 四值的实测 id 现已登记三个**：Done＝10000（SSCSD-411）、Cancelled＝10041、Rejected＝10042；`Rerouted` 本流程不用（区二：五态、无「已改道」）。**五条 Resolution post function 现已实证四条**：`Complete`／`Withdraw`／`Cancel as Duplicate`／`Reject`，余 `Abort Case`」。「测试单登记」加三行：**SSCSD-421**｜用途「转换 8 `Withdraw` 属性与 Resolution post function 回读」｜末态 Cancelled / Cancelled｜处置「留存不删（04.5.3 §四）。建单时已显式写 assignee＝Backend Operations，未经默认指派规则」；**SSCSD-422**｜用途「转换 9 `Cancel as Duplicate` 同上」｜末态 Cancelled / Cancelled｜处置同前；**SSCSD-423**｜用途「转换 3 `Reject` 同上」｜末态 **Rejected / Rejected**｜处置同前。**另记 04.5.3 §三 双标识的实际状态**：①标题标识成立（两单均 TEST｜ 起头）；②主体标识**无法成立**——2026-09-22 读 `getJiraIssueTypeMetaWithFields(SSCSD, 14357)` 共 48 个字段、仅 `project` 与 `summary` 为 required，**无任何属于 S-05 的主体标识字段**，故按 SSCSD-411 先例不涉任何员工、且不写他流程字段（`Target Employee` cf18047 留空）。本条不声称双标识已满足。 | Jira 实读 2026-09-22（create／getTransitionsForJiraIssue／transitionJiraIssue／getJiraIssue expand=changelog）；04.5.3 v13 §三／§四；`docs/test-evidence-2026-09-22-terminal-transitions.md` |
| 19 | ✅ COMPLETED 2026-09-22 · mendarat di **v34** (06:27:52Z) · bukti baca-balik: `diffConfluenceContentVersions` v33↔v34 sisi server, additions 19 / deletions 11 | 页首附表 baris 28（已解封行的证据边界）＋ 第八区「尚未测试」第一、二行 | Baris 28 解除判据末句写 「其中三条转换的 `hasScreen`／`isConditional` 待补 API 回读，四条终态转换待实跑」，dan 「尚未测试」 第一行写四条全未实跑。Sesudah 2026-09-22 tiga dari empat sudah 实跑；satu sisanya ditahan atas perintah. | 「【2026-09-22 补】四条终态转换实跑进度：**已实跑 3 条**——`Reject`(3)、`Withdraw`(8) 与 `Cancel as Duplicate`(9)，各用一张 TEST 单（SSCSD-423／SSCSD-421／SSCSD-422），证据见第八区。**未实跑 1 条**：`Abort Case`(11)——**按使用者指示暂缓**，待 04.3 Owner 答复页首附表 baris 19 的互斥条口径。**三条转换属性 API 回读仍为 0／3，未动**：`Create`(1)／`Complete`(10)／`Abort Case`(11) 只能在 `Pending Sub-tickets` 态取得，而本轮三单按设计直接由「待审批」入终态（一单一条终态转换）。**故本行仍不得视为判据齐备**。」 | Jira 实读 2026-09-22；建造单 v33 页首附表 baris 28 与 第八区 |
| 20 | ✅ COMPLETED 2026-09-22 · mendarat di **v34** (06:27:52Z) · bukti baca-balik: `diffConfluenceContentVersions` v33↔v34 sisi server, additions 19 / deletions 11 | 区二 转换表 — 转换 3 `Reject`、转换 8 `Withdraw` 与 转换 9 `Cancel as Duplicate` 三行的 post function 列 | 三行分别写 「（「取消原因」＝Withdrawn）」、「（「取消原因」＝Duplicate Case）」 dan 「（「取消原因」＝Dismissed，依 Spec N07②）」. 实跑后**取消原因一律未被写入任何字段**：三单 changelog 各只有 status 与 resolution 两个 item；`customfield_18054`（Reason）与 `customfield_18143`（Rejection Reason）在三单均为 `null`；该 Issue Type 现无属于 S-05 的取消原因字段（create 屏 48 个字段，无一个是）。 | 「【2026-09-22 补·实跑结论】本轮实跑证实：三条转换执行后**均只写 Resolution，取消原因未落任何字段**——`Withdraw`／`Cancel as Duplicate` 写 Cancelled（10041），`Reject` 写 Rejected（10042）；三单 changelog 各仅 status 与 resolution 两个 item，cf18054／cf18143 均 null。与既有分工一致而非冲突：「Cancellation Reason（新字段，非 18054，Kent c50234 第 3 点）」属**主单侧字段**，c50234 第 2 点已划归 Alden／V1，c50283 亦将其排除在本侧 13 项之外，故字段尚不存在、post function 无处可写。**须登记的是其后果，且分两级不可混同**：①该字段建成前，`Withdraw` 与 `Cancel as Duplicate` 两条路径在数据上**完全不可区分**（同 status、同 resolution、无其他标记），影响报表与审计口径，非仅便利性问题；②`Reject` **仍可区分**（Resolution＝Rejected 10042，非 Cancelled 10041），其缺的只是理由（Dismissed），不是路径身份。详见 findings **F-007**。本侧未新建字段、未写他流程字段、未改任何 post function。」 | Jira 实读 2026-09-22；建造单 v33 区二；OSD-116 c50234 第 2／3 点、c50283；`docs/findings.md` F-007 |
| 21 | ✅ COMPLETED 2026-09-22 · mendarat di **v36** (06:41:40Z) · `replaceNode` pada `a99c1693d3d4` · bukti baca-balik: `diffConfluenceContentVersions` v35↔v36 **additions 1 / deletions 1** (satu paragraf), kalimat asli 「共 33 行……待办 24」 utuh dengan koreksi ditempel di belakangnya. Angka koreksi **dihitung mekanis baris demi baris** dari kolom 状态, bukan dikira: 阻塞中 5 ＋ 待办 25 ＋ 已解封 4 ＝ 34 |
| 22 | ✅ COMPLETED 2026-09-22 · mendarat di **v37** (06:53:16Z) · bukti baca-balik: badan v37 dibaca ulang dari server, uji balik **sama persis karakter demi karakter** dengan v36 setelah 14 sisipan dikembalikan; 2.140 `data-local-id` utuh, nol hilang — kolom 回读 转换 3／8／9 (`b7a48c4f-…`／`75e73786-…`／`b1100a06-…`) |
| 23 | ✅ COMPLETED 2026-09-22 · mendarat di **v37** (06:53:16Z) · bukti baca-balik: badan v37 dibaca ulang dari server, uji balik **sama persis karakter demi karakter** dengan v36 setelah 14 sisipan dikembalikan; 2.140 `data-local-id` utuh, nol hilang — post function 转换 8 (`842f22d1-…`) dan 转换 9 (`897f93d7-…`) |
| 24 | ✅ COMPLETED 2026-09-22 · mendarat di **v37** (06:53:16Z) · bukti baca-balik: badan v37 dibaca ulang dari server, uji balik **sama persis karakter demi karakter** dengan v36 setelah 14 sisipan dikembalikan; 2.140 `data-local-id` utuh, nol hilang — 区一 N06 (`452126af-…`) dan N07 (`6556abf7711a`), kolom 状态 |
| 25 | ✅ COMPLETED 2026-09-22 · mendarat di **v37** (06:53:16Z) · bukti baca-balik: badan v37 dibaca ulang dari server, uji balik **sama persis karakter demi karakter** dengan v36 setelah 14 sisipan dikembalikan; 2.140 `data-local-id` utuh, nol hilang — 第八区 (`33b97c1d-…`), kalimat 「其余四条…已配置但未实跑」 |
| 26 | ✅ COMPLETED 2026-09-22 · mendarat di **v37** (06:53:16Z) · bukti baca-balik: badan v37 dibaca ulang dari server, uji balik **sama persis karakter demi karakter** dengan v36 setelah 14 sisipan dikembalikan; 2.140 `data-local-id` utuh, nol hilang — tabel 测试记录 (`7ea6f8f4-…`) **naik 6 → 8 baris data**, dua baris betulan, urutan benar |
| 27 | ✅ COMPLETED 2026-09-22 · mendarat di **v37** (06:53:16Z) · bukti baca-balik: badan v37 dibaca ulang dari server, uji balik **sama persis karakter demi karakter** dengan v36 setelah 14 sisipan dikembalikan; 2.140 `data-local-id` utuh, nol hilang — tabel 测试单登记 (`5e5cda82-…`) **naik 1 → 4 baris data**: SSCSD-421／422／423, urutan benar |
| 28 | ✅ COMPLETED 2026-09-22 · mendarat di **v37** (06:53:16Z) · bukti baca-balik: badan v37 dibaca ulang dari server, uji balik **sama persis karakter demi karakter** dengan v36 setelah 14 sisipan dikembalikan; 2.140 `data-local-id` utuh, nol hilang — paragraf butir 18 (`e8243bb38a83`) ditutup: 「新增两行」／「加三行」 dinyatakan sudah dilaksanakan |

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
