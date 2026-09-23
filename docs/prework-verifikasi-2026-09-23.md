# Pra-kerja S-05 — keempat perintah CLAUDE.md yang belum dijalankan, dijalankan 2026-09-23

Semua dibaca **live**. Tidak ada yang ditulis ke Confluence/Jira/Slack.

## 1. 07｜指南 §二、§三 — dibaca (pageId 1704362028, live **v28**)

Kewajiban skill: 「每次开发前，先读 07｜指南 第二、三节」. Sesi ini belum pernah.

Dua butir §二 yang langsung mengikat pekerjaan Bagian 7:

> **标准页读法**：页面里任何 🔲、「待定」、「规划中」、「锁定」内容一律视为缺口，**不得自行填补或当作已生效标准**

> **先查后写**：任何 Confluence 页面修改前，先拉取页面当前最新版本，不基于记忆或旧版本覆写

Butir pertama membenarkan bentuk draf Bagian 7: sel tanpa sumber ditulis 🔲, bukan diisi.
Butir kedua wajib dijalankan tepat sebelum menulis — snapshot 建造单 harus diambil ulang saat itu juga.

§三 memberi format 标准缺口回报 enam kolom (触发位置／已实际打开读取的页面／想回答的问题／判断／影响／类型确认),
dengan kewajiban memilah dulu: **标准缺口** (perbaikan di halaman standar) vs **业务歧义** (perbaikan di Spec).

## 2. Uji penerimaan §〇 — "buka 04.7, cari Project untuk sebuah Request Type"

Dijalankan sendiri pada 04.7 live (**v49**, 2026-09-22 02:36:12Z), dua baris S-05:

| | RT-HR-DISCIPLINARY-SUBMIT | RT-HR-DISCIPLINARY-EVENT |
|---|---|---|
| 登记阶段 | 候选 | 候选 |
| Owner 部门 Project | **HR**（主单住 SSCSD） | **HR**（主单住 SSCSD） |
| 载体 | 主单（SSCSD） | 主单（SSCSD） |
| 编排 (tujuan sub-tiket) | **HR；员工所属部门（N16）** | **HR；员工所属部门（N16）** |
| Portal Group | —（非 Portal 入口） | —（非 Portal 入口） |
| 需审批 / 有人工执行段 / 跨部门 | 是 / 是 / 是 | 是 / 是 / 是 |

**Dua hal yang terverifikasi live, bukan diasumsikan:**
- Nama dwibahasa **belum di-backfill** — kedua baris masih menulis「双语Request Type／Slack展示名称待流程Owner确认」.
  → baris 5 tabel penghambat **masih terbuka**, persis seperti yang tercatat.
- 请求级整单时限 kedua baris masih **🔲 未定占位** → baris 17 tabel penghambat **masih terbuka**.

## 3. 04.8 §五 实体字段登记表 — dibaca (pageId 1690140756, live **v21**)

Kewajiban skill: 「引用 Registry 实体字段先查 04.8 实体字段登记表…变更先看消费列」.

Lima field NTP yang dikonsumsi S-05 — kolom「被谁消费」**tidak satu pun menyebut S-05**:

| Field | cf | 被谁消费 (kutipan) |
|---|---|---|
| Talent Status | cf18002 | 约 17 个生产件…；B6；请假审批链；离职 N7/N11；Grade 资格过滤 |
| Direct Supervisor | cf17996 | B6 唯一解析源→离职 N3/N4、Grade …；请假 N2 |
| Employee | cf17995 | 全部 accountId 匹配链（B6、Notify DM 解析、请假/离职/Grade） |
| Work Email | cf18051 | Notify 平台件全站 DM 解析；Grade N2；通知邮件保底 |
| Department | cf17998 | Grade D-7/D-8 恭喜文案；部门 HOD 关系解析疑似取数面 |

→ baris 31 tabel penghambat **masih terbuka**, terverifikasi live.

**Dua temuan tambahan dari 04.8 v21:**

(a) Baris 工作时口径字段族 di §五 berbunyi verbatim: 「🔲 ID 待 Alden 补｜上下班／午休／rest day／公共假期（04.4 §8.3 明定住 NTP，n8n 运行时读取）」.
→ ini **sumber resmi** untuk klaim baris 15 draf Bagian 7 (field jam kerja NTP menunggu Alden). Sebelumnya kuambil dari tabel penghambat kita sendiri; sekarang ada sumber SSOT-nya.

(b) **Kemungkinan baris registri keliru — bukan wewenang kita.** §三 baris「纪律处分记录（Warning Record）」berbunyi:
> Final Written Warning满12个月零违规经N25（Direct Supervisor/**Reporting Line**+HR联合评审）通过 → N27…

Tapi Spec S-05 **v23** menghapus peran **Reporting Line** dari seluruh alur
(「B表Reporting Line角色定义行整体删除，⓪区解释该角色的文字一并删除」), dan Spec v62 sudah tidak memuatnya.
Jadi baris 04.8 §三 itu memakai peran yang sudah tidak ada di Spec.
Penyaluran menurut 07.06 §三 归口表: 「登记表某一行错了（04.7／04.8／04.9／04.11）」→ Owner halaman (04.8 = **Alden**), lewat Slack #nos-bo. **Tidak kusentuh.**

## 4. 切分审计通过证据 — DITEMUKAN dan dibaca

Kewajiban skill: 「**Spec 存在不替代切分审计证据；建设者须读取对应 Epic 的切分审计通过证据**」.
Kemarin kucatat "nol kemunculan di 建造单" dan berhenti di situ. Sekarang bukti aslinya sudah dibaca.

**Rantai lengkapnya:**

| Tahap | Letak | Isi |
|---|---|---|
| N4 mesin | OSD-3 **c48757** (2026-08-23 13:00) | 切分审计｜机器报告｜第 10 轮; auditedVersion **29**; 「机器结论：N4 机器审计通过」; 通过 18／退回 0／待人工裁决 3 |
| N5 manusia | OSD-3 **c48764** (2026-08-23 20:30, Kayden) | 「N5 人工裁决通过（第10轮）」; auditedVersion 29 → **approvedPageVersion 30**; S-05 termasuk dalam「其余14项候选（S-03~S-16）…本轮一并确认为最终结论」 |
| Koreksi N5 | OSD-3 **c49113** (2026-08-31, Kayden) | approvedPageVersion → **v34**; baris S-05: 链位 链首→链中, mencatat masuknya edge dari S-19 |
| Koreksi N5 | OSD-3 **c49116** (2026-08-31) | approvedPageVersion → **v35**; §五 baris S-05 disinkronkan: S-19 edge = 运行时触发衔接, **非建设前置**, 前置切分序号 tetap「无」 |
| Pembaruan N5 | OSD-3 **c49642** (2026-09-09, Kayden) | approvedPageVersion → **v38**; perubahan hanya S-19 driver, S-14 masuk S-19, rapikan format; 「切分表其余行…未变」 |

**Halaman 部门页 HR｜盘点与切分** (pageId **1745158181**) live = **v38** = approvedPageVersion v38 → **rantai tertutup dan mutakhir**.

Isi keputusan untuk S-05 (第三节 切分表, kutipan):
> ✅2026-08-20会议裁决新建合并，D-04最终结论，已于2026-08-23经N5正式确认：原纪律事件处理（P-10）与PIP绩效改进（P-11）此前04.5四问判定为"独立机制，不涉及"（互不触发）；本次会议裁决新建合并…**案件并发量低、无人以此为日常工作台、管理问句是单案进度而非漏斗健康度——不建Pipeline Project，维持事件驱动的主单+子单形态。**

- 覆盖盘点行: **P-09、P-10、P-11**
- Project 归属: 已登记｜JSM Board｜**SSCSD**（主单）＋已登记｜Team Project｜**HR**（子单）
- 前置切分序号: **无** — edge S-19→S-05 adalah pemicu runtime, **bukan prasyarat pembangunan** (F-100, c49116)

**Artinya untuk kita:** kewajiban「读取切分审计通过证据」**sudah terpenuhi**, dan isinya **tidak menambah prasyarat baru** pada pembangunan S-05. Ini juga menegaskan bentuk 主单+子单 yang sudah dipakai 建造单 memang hasil keputusan N5, bukan pilihan sisi pembangun.

Catatan: 建造单 saat ini **tidak memuat rujukan apa pun** ke rantai bukti ini. Skill hanya mewajibkan *membaca*, tidak mewajibkan mendaftarkan. Apakah perlu ditambahkan ke 建造单 — keputusan Bambang.
