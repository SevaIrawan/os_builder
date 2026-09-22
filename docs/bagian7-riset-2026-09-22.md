# Bagian 7 建造单（政策参数落位） — riset sebelum menulis

Tanggal riset: 2026-09-22 (±15:00 WIB). Semua halaman dibaca **live**, bukan dari salinan lama.
Belum ada satu huruf pun yang ditulis ke Confluence.

## §1 Versi halaman yang dipakai (dicek live hari ini)

| Halaman | pageId | Versi live | Cocok dengan `docs/source-versions.md`? |
|---|---|---|---|
| 04.5.2｜建造单模板 | 1729626775 | **v11** (2026-09-15) | ya |
| Spec S-05 | 2036858900 | **v62** (2026-09-15) | ya |
| 07.06.1｜开发规则与避坑指南 | 1712226375 | **v34** (2026-09-21) | ya |
| 04.9｜n8n Workflow SSOT | 1693089805 | **v106** (2026-09-21) | ya |
| 建造单 S-05 | 2096463922 | **v40** (2026-09-22 07:46Z) | ya |

Salinan lokal `spec.md` (dibaca 2026-09-22 02:46) diverifikasi identik dengan v62 live —
baris pertamanya sama persis dengan excerpt yang dikembalikan server. Jadi bukan dokumen basi.
Salinan lokal 04.9 (`live_0409.md`, dibaca 2026-09-21 23:52) juga masih v106 → masih berlaku.

## §2 Apa sebenarnya isi Bagian 7 menurut standar

Kutipan verbatim dari 04.5.2 v11:

> 「哪些数字会变、住哪、谁改、怎么生效」的参数化登记——改政策＝改数据行不改代码的关键。
> 政策的**业务含义**（额度多少、资格条件）人读权威住政策制度页（Spec 引用区链接），
> 本区只登记参数化落位；仍硬编码在代码内的项如实标注为数据化候选。

Kolom resmi (5): `参数键 | 白话 | 住处 | 变更入口 | 生效方式`

**Jadi Bagian 7 bukan daftar angka kebijakan.** Ia daftar *tempat mendarat* angka itu.
Kalau angkanya masih tertanam di kode, standarnya menyuruh menulisnya apa adanya sebagai
「数据化候选」, bukan menyembunyikannya.

## §3 Preseden — dua build sheet lain

**员工离职｜建造单 (1743716419, v61)** — memakai 5 kolom standar, 3 baris, dan jujur soal hardcode:

| 参数键 | 住处 |
|---|---|
| 结算子单提前天数＝3 | 硬编码在 N6 三分支 Code 节点（**数据化候选**） |
| N9 建单时点＝17:00 GMT+8 | 硬编码在 Schedule Trigger（**数据化候选**） |
| SLA C-1／C-2／C-3 | 人读权威住 Spec C 表；工程侧判定已建，tapi nilai masih hardcode di Code node — **数据化候选**；`生效方式` ditulis 「政策表未建（建表权仅平台 Owner，04.9 第四节）」 |

**目标与绩效闭环管理｜建造单 (2097152003, v8)** — memakai kolom sendiri (`参数 | 白话 | 住处 | 状态`),
semua baris berstatus 「未定稿」 karena halaman kaidahnya belum ada.

Kesimpulan: yang kuikuti adalah **5 kolom standar 04.5.2** (seperti 员工离职), karena build sheet S-05
sejak awal menyatakan dirinya mengikuti 04.5.2.

## §4 Temuan penting: S-05 tidak punya Policy Store

04.9 §四 (v106) mendaftar **12 Data Table**. Yang berkategori 政策表 hanya **satu**:

> `NOS Policy Store (F2 11-col)` · `DsK1slgPdy79LPHu` · 「假期政策数值的运行时权威」 · 政策表 · Owner 平台 · dibaca oleh `NOS | Platform | Policy Engine`

Tidak ada tabel kebijakan untuk disiplin/PIP/Warning. Dan aturannya tegas:

> 建表权仅平台 Owner；建造线需要新表向平台 Owner 申请。

Bagian 6 build sheet S-05 juga **tidak** mendaftar `Policy Engine` sebagai platform piece yang dipakai.

**Akibatnya**: semua nilai sisi rekayasa S-05 saat ini tidak punya tempat mendarat berupa data row →
statusnya 「数据化候选」, persis seperti preseden 员工离职. Ini fakta, bukan kelalaian kita.

Pit yang mengatur tabel kebijakan adalah **07.06.1 B2**「n8n Data Table 默认只回 50 行」 — belum menggigit
selama S-05 tidak punya tabel, tapi wajib dibaca kalau nanti tabelnya dibangun.

## §5 Inventaris parameter S-05 (dari Spec v62, bukan ingatan)

### Sudah punya tempat mendarat yang nyata (dan sudah di-回读)

| Parameter | Tempat mendarat | Bukti |
|---|---|---|
| PIP 延长周期 = 15／30／60／90 天 | option set `customfield_18253` | API readback 2026-09-22; dikunci Kent c50343 |
| Show Cause 解释结果 = 成立／不成立 | option set `customfield_18252` | idem |
| PIP Result = Completed／Extension／Failed | option set `customfield_18254` | idem |
| 判定依据类型 = 纪律违规／PIP未改善 | option set `customfield_18255` | idem; **wajib verbatim sama** dengan 辞退原因 离职流 (Felix c50045) |
| 联合评审结果 = 通过／不通过 | option set `customfield_18257` | idem |

Untuk kelima baris ini: `变更入口` = Schema Owner (Kent) lewat 04.10 §五; `生效方式` = ubah option, langsung berlaku.

### Masih 数据化候选 (nilainya ada, tempat mendaratnya belum dibangun)

| Parameter | Nilai (Spec v62) | Akan mendarat di |
|---|---|---|
| SLA C-1…C-20 (17 baris) | lihat Spec C 表 | 主单 → mesin JSM SLA; 子单/跨对象 → n8n 扫描件 (04.4 §8.1) — dua-duanya belum dibangun |
| 纪律记录有效期 参考值 | Verbal 3 bulan／Written 6 bulan／Final Written「永不自动失效」 | nilai per-kasus ke field 主单 (belum dibangun, ranah Alden/V1); angka rujukannya hanya di Spec |
| 到期前提醒 = 5 天 (C-6) | 5 hari kalender | n8n timer N26 (belum) |
| 打回次数上限 = 2 | 2 | logika kartu N07 (belum; field 打回次数 juga ranah Alden) |
| Show Cause 延期次数上限 = 1 | 1 | logika N10 (belum). `cf18243` hanya menyimpan hitungannya — **belum kuverifikasi** apakah batas 1 dipaksakan di level field |
| Check-in 频率映射 (C-10) | 15天≥1次中期；30天≥每2周1次；60/90天≥每30天1次 | n8n N16 (belum); pengaturan per-kasus di `cf18251` |
| 联合评审触发 = 满12个月零违规 | 12 bulan | n8n timer N25 (belum) |
| Final Outcome 九值 | ⓪区十五节 | field 主单 (belum, Alden/V1) |
| 工作时／日历时 (kalender) | kolom 计时方式 di C 表 | JSM Calendar + n8n; harus seragam dengan jam kerja NTP (04.4 §8.3) — field NTP masih menunggu Alden |

### Yang secara eksplisit BUKAN parameter — wajib dicatat supaya tidak ada yang mengarang ambang

Spec ⑤ 引用区 v62, verbatim:

> N05/N07/N10/N14涉及的"同一次事件""证据不足""严重违纪标准""合理延期原因"等判据，
> 属HR专业判断范畴，**不设机器可执行的数值门槛**……具体清单见《Nexmax WFH工作规章制度（正式版）》3.3节
> "处分执行原则"；……"提前终止条件""PIP Failed后降级或解雇"判据同理。

Dan N05 sendiri tidak punya jendela waktu: 「自动化查重（同员工+疑似同一次仍在处理中的事件）」 — tidak ada angka.

**Catatan jujur**: halaman 《Nexmax WFH工作规章制度（正式版）》 yang disebut sebagai otoritas baca-manusia itu
**tidak bisa dibuka** — baris 16 tabel penghambat build sheet sudah mencatatnya (Backend Operations → 404;
akun Bambang → 403「Space is restricted」), dan Felix masih berutang lokasi resmi + versinya. Jadi kolom
「人读权威」 untuk Bagian 7 belum lengkap, dan itu harus ditulis apa adanya.

## §6 Apa yang TIDAK menghalangi pengisian Bagian 7

- Tidak butuh Alden: mengisi Bagian 7 adalah pendaftaran, bukan pembangunan.
- Tidak termasuk tindakan tak-bisa-dibalik (07.06.1 §六-2) — tidak ada objek yang disentuh.
- Tidak butuh Policy Engine lebih dulu; preseden 员工离职 mengisi Bagian 7 justru untuk mencatat bahwa
  tabel kebijakannya belum ada.
