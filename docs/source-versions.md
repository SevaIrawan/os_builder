# Source version ledger — halaman Confluence NOSM yang jadi rujukan S-05

> Dipakai oleh skill `nosm-sync-check` langkah 6 (version sweep). Satu baris = satu halaman sumber
> yang pernah kita konsumsi. Kolom "Versi tercatat" adalah versi yang jadi dasar catatan/draft kita;
> kalau live lebih tinggi, catatan kita berdiri di atas versi basi sampai diff-nya dibaca.
>
> **Terakhir disapu**: 2026-09-21 ~11:30Z (18:30 WIB), metode: CQL seluruh space NOSM
> `space = NOSM AND type = page AND lastmodified >= "<tanggal sapuan sebelumnya>"`, lalu
> `listConfluenceContentVersions` + `diffConfluenceContentVersions` untuk tiap halaman yang bergerak.
>
> Sapuan 11:30Z: **tidak ada versi baru** dibanding sapuan 11:00Z. Diverifikasi per halaman, bukan
> disimpulkan dari daftar CQL saja — 04.9 tetap v106, 建造单 tetap v33. 04.11 tidak pernah muncul di
> sapuan mana pun sejak 2026-09-20, jadi masih v2 dan 判据② baris 6 建造单 masih terbuka.
>
> **Sapuan 2026-09-22 06:21 WIB (2026-09-21 23:21Z)** — awal sesi, seluruh langkah skill dijalankan.
> CQL seluruh space sejak 2026-09-21 11:30Z mengembalikan **36 halaman**, **tidak satu pun ada di ledger ini**.
> Sepuluh halaman ledger diverifikasi satu per satu lewat `listConfluenceContentVersions`, bukan disimpulkan
> dari timestamp: 07.06 **v30** · 04 **v25** · 07.06.1 **v34** · 04.7 **v46** · 04.9 **v106** · 04.9.1 **v19** ·
> 04.4 **v33** · 04.4.4 **v4** · Spec S-05 **v62** · 建造单 **v33**. Semua sama dengan yang tercatat.
> Yang bergerak milik alur lain: kluster E02／PF-03 (Carlson), xLoop 校验包, 招聘执行 Spec (bergerak lagi
> 2026-09-21 23:31 WIB), 新人90天 Spec, Grade／离职／OS 开发流 建造单, 04.9.3, 04.9.5.
> Dua salinan terkendali dibandingkan dengan skrip pada sapuan ini: **identik, tidak ada 部署漂移**
> — CLAUDE.md 19 bullet + 开发入口的冻结要求; anchor §一 5 baris／4 kolom, §五 7 baris／4 kolom,
> §六 16 baris／4 kolom.
>
> Sumber non-Confluence yang ikut disapu (tidak punya nomor versi, jadi dicatat dengan penanda terakhir).
> Nilai di bawah **dicek ulang pada sapuan 2026-09-22 06:21 WIB dan tidak berubah**:
> **OSD-116** — 163 comment, terbaru **c50290** (Kent, 2026-09-21 17:18 +07). Alden masih belum
> berkomentar sejak 2026-09-10.
> **#nos-bo (C0BRSTNNY4A)** — 15 pesan top-level, terbaru 2026-09-19 18:36 (Kayden). Seluruh jumlah
> balasan thread dan timestamp balasan terakhirnya sama dengan pembacaan sebelumnya; aktivitas terbaru
> tetap **2026-09-21 13:59:29 +07** di thread `1789704362.435989`.

> **Sapuan 2026-09-23 (skill dijalankan penuh, langkah 1–7)**
> Konektor: Atlassian → site `nexmax` (cloudId abf9cc08-…) hidup; n8n → 145 workflow terdaftar, hidup.
> CQL seluruh space sejak 2026-09-21 23:00Z mengembalikan **39 halaman**. Yang ada di ledger ini hanya **tiga**:
> **04.10 → v20** (2026-09-22 07:22:35Z, sudah tercatat, isinya sudah dibaca penuh),
> **建造单 → v40** (2026-09-22 07:46:03Z, tulisan kita sendiri, sudah tercatat),
> **04.7 → v49** (2026-09-22 02:36:12Z — perubahan itu **adalah** v49, jadi angka di ledger sudah mencakupnya; tidak ada gerakan baru).
> 36 sisanya milik alur lain: kluster PF-03／E02 (Carlson), xLoop 校验包, Grade／员工离职 建造单,
> 04.9.3／04.9.4 (分册 alur lain), 招聘执行 Spec, 新人90天 Spec, F4／BLM.
> **Dua belas halaman yang jadi sandaran draf Bagian 7 diverifikasi satu per satu** lewat pembacaan versi
> langsung, bukan disimpulkan dari daftar CQL: 07.06 **v30** · 04 **v25** · 07.06.1 **v34** · 04.4 **v33** ·
> 04.5 **v79** · 04.5.2 **v11** · 04.7 **v49** · 04.9 **v106** · 04.10 **v20** · Spec S-05 **v62** ·
> 建造单 **v40** · Policy Engine 调用契约 (1617985562) **v2**. Semua sama dengan yang dikutip di draf —
> **tidak ada kutipan yang berdiri di atas versi basi**.
> Dua salinan terkendali dibandingkan dengan skrip: **identik, tidak ada 部署漂移** — CLAUDE.md 19 bulir
> + preamble + 开发入口的冻结要求; anchor §一 4 baris/4 kolom, §五 6 baris/4 kolom, §六 15 baris/4 kolom
> (jumlah baris di sini tidak menghitung baris header, berbeda dengan catatan sapuan 2026-09-22).
>
> Sumber non-Confluence pada sapuan ini:
> **OSD-116** — **167 comment**, terbaru **c50345** (Kent, 2026-09-22 14:24 +07). Tidak ada comment baru
> sejak kemarin; **Alden masih belum membalas c50279**.
>
> **Sweep 2026-09-23 01:28Z (nosm-sync-check, new pipeline step 0)**
> Connectors: n8n `search_workflows` ok, 145 workflows (toolu_01YaS4pEWrbm6MhLAwEXYgtv); Atlassian reads ok.
> Controlled copies: `scripts/sync_check.py` exit 0 against 07.06 **v30** (toolu_01ENbiNLkvZwrNhWvkMo2Y8u) and
> 04 **v25** (toolu_012dq8SmGsksRKsVvCUHfRj8): 19/19 bullets, preamble and 冻结要求 same; tables 4/4, 6/6, 15/15.
> CQL `space = NOSM AND type = page AND lastmodified >= "2026-09-22"` (toolu_01KgZyvQVcL9QRZDh7vUxiXx):
> totalSize **32**, one result page. Newest lastModified in the result: 2026-09-22T10:16:33Z (Grade 建造单).
> Three of the 32 are in this ledger, each checked with `listConfluenceContentVersions`:
> 建造单 **v40** 2026-09-22T07:46:03Z (toolu_019FLBs6HWxkRX9A5bhjLwXz) · 04.10 **v20** 2026-09-22T07:22:35Z
> (toolu_01FuzFhLmUtty1W4wnd5tY2t) · 04.7 **v49** 2026-09-22T02:36:12Z (toolu_0161dBQtzKYqcjexGgTZ8aW6).
> All three equal the versions already recorded. No diff to read.
> The other 29 pages are not in this ledger.
> OSD-116 comments and #nos-bo were not part of this run.
>
> **Sweep 2026-09-24 (nosm-sync-check, full run)**
> Connectors: Atlassian reads ok (cloudId abf9cc08-…); n8n `search_workflows` ok.
> Controlled copies: `scripts/sync_check.py` exit 0 against 07.06 **v30** (toolu_019qfms4R9oLjgWv7dJtK8Gv) and
> 04 **v25** (toolu_01EHcBcjMUEXU6Ktf1zuSYMX): 19/19 bullets, preamble and 冻结要求 same; tables 4/4, 6/6, 15/15.
> No deployment drift.
> CQL `space = NOSM AND type = page AND lastmodified >= "2026-09-23"`: totalSize **34**, both pages read
> (25 + 9, cursor-paginated). Six of the 34 are in this ledger; each checked with `listConfluenceContentVersions`:
> **07.06.1 → v37** (was v34, 2026-09-23T10:56:17Z, "E5 补适用范围…") — full current body already read via
> getConfluencePage, no drift risk (07.06.1 is a reference page, not one of the two controlled copies).
> **04.9 → v109** (was v106, 2026-09-23T14:38:30Z, "索引：员工离职 N2 已发布 674e5e5e，Call N3 启用（c50402）") —
> n8n Workflow SSOT index entry for the resignation N2 publish; not S-05-specific.
> **04.11 → v4** (was v2, 2026-09-23T10:48:34Z, "N10 测试期落点改 nos-governance…") — Slack channel registry,
> test-channel addition; not S-05-specific.
> **04.5.3 → v14** (was v13, 2026-09-23T10:47:59Z, "§二 测试白名单加丙 #nos-governance…") — Sandbox/test
> strategy page, same test-channel addition; not S-05-specific.
> **04.7 → v50** (was v49, 2026-09-23T08:50:16Z) — diffed v49→v50: one row added,
> `RT-HR-RESIGNATION-UPSTREAM-TRIGGER`, registering the upstream-trigger entry Kent assigned to Geri+Bambang
> (OSD-116 c50382) as a Candidate Route, naming S-05 N20 as its first caller and flagging
> "HR Ops & Data 成员来源：🔲 过渡期固定名单建设前登记（Geri）" — this is the same open item as NSE-1137
> c50387 ⑦, now also tracked in 04.7. No conflict with anything Bambang has stated.
> **纪律与绩效改进处置｜建造单 (S-05 建造单) → v43** (was v40, 2026-09-23T04:02:11Z) — diffed v40→v43:
> three additive "【补登/订正｜原文保留不删】" blocks quoting c49317 (Felix), c50237/c50234 (Bambang/Kent field
> split) and c50345 (Kent, 13 execution-card fields) verbatim into the build sheet; no deletions, no semantic
> change, nothing new beyond what these sources already said.
> The other 28 pages are not in this ledger (F1/PF-03/E02 cluster, xLoop packets, Grade/员工离职/OS 开发流
> 建造单, 04.9.3/04.9.4/04.9.5, 员工离职｜流程 Spec, HR｜盘点与切分).
> OSD-116 comments and #nos-bo were not re-swept this run (handled separately, see prior turns).
>
> **Sweep 2026-09-24 14:35Z (nosm-sync-check, re-run after 12 h window expired)**
> Connectors: n8n `search_workflows` ok (count 153); Atlassian reads ok.
> Controlled copies: `sync_check.py` against 07.06 **v30** (toolu_01SosMx2N8kSrsBcFZfsk1Hh) and
> 04 **v25** (toolu_01Fb3vLRs4zwnKEbUNh3Gjkn): 19/19 bullets, preamble and 冻结要求 same; tables 4/4, 6/6, 15/15.
> VERDICT: no deployment drift.
> CQL `space = NOSM AND type = page AND lastmodified >= "2026-09-24"`: totalSize **42**, one result page.
> Six of the 42 are in this ledger; each checked with `listConfluenceContentVersions` and diffed:
> **04.3 → v35** (was v33; v34 05:35Z placeholder, v35 05:40Z) — §六 three changes (Kayden OSD-116 c50442/c50445):
> 主单执行中止 allowed executors add 「该 Spec 增补区 B 登记的处置角色组（如 S-05 的 HR Ops & Data）」; the 模式五
> mutual-exclusion sentence gets a 「失效类中止」 exception; new 撤回类／失效类 split, each Spec must tag its 取消原因
> values. Directly relevant to S-05 Abort Case (id 11) and N07 确认重复; c50445 also fixes the order: main ticket
> to 已取消 first, then cancel open sub-tickets.
> **S-05 Spec → v67** (was v62; v63–v67 all 2026-09-24, Felix) — diffed v62→v67 (34 added / 33 removed lines, 17 hunks):
> (a) the 「缺位由 HR Ops & Data 承接／代提交」 wording is replaced everywhere by 「系统无法解析 Direct Supervisor →
> 拦截并告警，转 HR 修正档案后重新提交／解析」 (Kayden c50461, Alden c50468, Kent c50472), touching N03/N07/N16/N17/N20/N21,
> A/B/C/D tables, 投影图自检 and ⑤; (b) A 表 取消原因 values tagged 失效类／撤回类 (c50445). Felix c50486 says this is a
> 建设期注记 without re-audit; Kayden's explicit exemption in c50442/c50445 covers the 取消原因 tagging. Frozen baseline
> recorded in the build sheet is still v61.
> **04.7 → v51** (was v50) — only the RT-HR-RESIGNATION-UPSTREAM-TRIGGER row: N13 absence wording synced to v3.7
> (HR Ops & Data takeover and interim list removed). S-05 rows unchanged.
> **04.5.3 → v15** (was v14) — §二 new exception 「收件人就是主体」 (five conditions) and §三 double-marker item 2 pointer.
> Test policy page, affects how a builder may self-test notifications to the subject.
> **04.9 → v114** (was v109) — index rows for resignation N2/N3 (first real run), OS 开发流 时效件 and C-0 retirement,
> Grade N7/N8/N10 scan, 守护层三, N2; 04.9.4 block count 10→16. No S-05 row (S-05 still has no 04.9 registration).
> **HR｜盘点与切分 → v40** (was v38) — S-01 terminal point, S-02 链中 with new S-02→S-07 edge, S-07 third entry;
> no S-05 row change.
> 纪律与绩效改进处置｜建造单 is not in the 42 results: still **v43** (matches today's full read).
> The other 36 pages are not in this ledger (F1/F2/PF-03/E02 cluster, xLoop, NXP SOP, Grade/员工离职/OS 开发流/目标与绩效
> 建造单, 04.9.3/04.9.4/04.9.5, 员工离职｜流程 Spec, 新人90天框架 Spec, 招聘执行 Spec).
>
> **Sweep 2026-09-25 01:15Z (nosm-sync-check, new session)**
> Connectors: n8n `search_workflows` ok (toolu_016KgLbmgnsQREVvLvQAzmzA, 3 S-05 workflows, all inactive); Atlassian reads ok.
> Controlled copies: `sync_check.py` against 07.06 **v30** (toolu_01Ga17F78QkRc7aRWVxaEQE8) and
> 04 **v25** (toolu_01AFBEu8uDeEYeVDg9mvQpZD): 19/19 bullets, preamble and 冻结要求 same; tables 4/4, 6/6, 15/15.
> VERDICT: no deployment drift.
> CQL `space = NOSM AND type = page AND lastmodified >= "2026-09-24"` (toolu_01EiKMCfxiWH8YbktG6VnUR5): totalSize **43**,
> one result page. Only one hit is newer than the 2026-09-24 14:35Z sweep: 纪律与绩效改进处置｜建造单.
> `listConfluenceContentVersions` on the ledger pages among the hits:
> **纪律与绩效改进处置｜建造单 → v46** (was v43; toolu_017uMggLSGjjzxMdGGHawgEx) — v44/v45/v46 are this session's own writes
> (W-2026-09-24-05/-06/-07, each read back in full); no other author.
> Unchanged against the table: S-05 Spec v67 (toolu_01PgcDXscmK74wxDcy1qVw8z), 04.9 v114 (toolu_01N1ZqDX8vYtAn5TzeuMyBTi),
> 04.7 v51 (toolu_01SkC7ztqfuGj5mhwwbyMuzw), HR｜盘点与切分 v40 (toolu_01WmZDridomUyzX3YnfbEGp8),
> 04.5.3 v15 (toolu_01Cx2FpfYixYyhwrVtxyL5QZ), 04.3 v35 (toolu_01DgbZVdWLTHcrU8NX4qPyGC).
> The other 36 hits are the same non-ledger pages listed in the previous sweep, all last modified before 14:35Z.

| Halaman | pageId | Versi tercatat | Owner |
| --- | --- | --- | --- |
| 07｜指南 | 1704362028 | v28 | Kayden |
| 07.01｜盘点与切分指南 | 1705508891 | — | Kayden |
| 07.03｜设计指南 | 1695744021 | v58 | Kayden |
| 07.04｜结构审计指南 | 1744896004 | v27 | Kayden |
| 07.05｜对齐指南 | — | v5 | Kayden |
| 07.06｜建设指南 (sumber CLAUDE.md §八) | 1730347066 | **v30** | Alden |
| 07.06.1｜开发规则与避坑指南 | 1712226375 | **v37** | Alden |
| 04｜总纲 (sumber anchor) | 1676804100 | **v25** | Kayden |
| 04.0｜词汇表 | 1676640265 | v26 | Kayden |
| 04.1｜Project 判定 | 1676738564 | v46 | Kayden |
| 04.2｜单据体系 | 1676607500 | **v40** | Kayden |
| 04.3｜状态与 Workflow | 1676771343 | **v35** | Kayden |
| 04.4｜自动化配置模式库 | 1677066244 | **v33** | Alden |
| 04.4.1｜模式九 | 1729888419 | v13 | Alden |
| 04.4.2｜B6 契约 | — | v12 | Alden |
| 04.4.3｜身份件契约 | 2076508181 | v6 | Alden |
| 04.4.4｜协作 Thread 契约 | 2102067228 | **v4** | Alden |
| 04.5｜Spec 与建造单规范 | 1678573617 | v79 | Kayden |
| 04.5.1｜Spec 模板 | 1685979182 | v19 | Kayden |
| 04.5.2｜建造单模板 | 1729626775 | v11 | Alden |
| 04.5.3｜Sandbox 与测试 | 1729626578 | **v15** | Alden |
| 04.6｜n8n 使用规范 | 1690927120 | v20 | Alden |
| 04.7｜Router SSOT | 1691254793 | **v51** | Alden |
| 04.8｜Registry SSOT | 1690140756 | **v21** | Alden |
| 04.9｜n8n Workflow SSOT | 1693089805 | **v114** | Alden |
| 04.9.1｜详情：平台 | 1764622422 | **v19** | Alden |
| 04.10｜Jira 共享配置治理 | 1738735636 | **v20** | Kent |
| 04.11｜Slack Channel 登记表 | 1764524046 | **v4** | Alden |
| 04.12｜机读标记总清单 | 2091876367 | v5 | Kent |
| Notify 子流程调用契约 | 1603633175 | v13 | Alden |
| OS 开发流｜流程 Spec | 1729200354 | v39 | Kayden／Kent |
| HR｜盘点与切分 | 1745158181 | **v40** | Felix |
| 纪律与绩效改进处置｜流程 Spec (S-05) | 2036858900 | **v67** (冻结基线 v61) | Felix |
| 纪律与绩效改进处置｜建造单 | 2096463922 | **v46** | Bambang (BO) |

**Tebal** = bergerak pada sapuan 2026-09-21 dan sudah dibaca diff-nya (lihat
`docs/reading-notes-2026-09-21.md` bagian VERSION SWEEP).

Baris ber-`—` pada kolom pageId: id belum dicatat; skill harus mencarinya lewat CQL judul sebelum
menyimpulkan halaman itu tidak berubah.
