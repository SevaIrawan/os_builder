# Versi halaman sumber — halaman Confluence NOSM yang jadi rujukan S-05

> Dipakai skill `nosm-sync-check` langkah 4 (sapuan seluruh space). Satu baris = satu halaman sumber yang
> kita pakai. Kolom "Versi tercatat" = versi terakhir yang kita ketahui. Kalau versi live lebih tinggi,
> baca diff-nya dan halaman itu secara penuh sebelum dipakai lagi.
>
> Metode sapuan: CQL `space = NOSM AND type = page AND lastmodified >= "<tanggal sapuan sebelumnya>"`,
> lalu `listConfluenceContentVersions` + `diffConfluenceContentVersions` untuk tiap halaman di tabel yang bergerak.
> Log sapuan sebelumnya ada di riwayat git (dirapikan 2026-09-25).
>
> **Sapuan terakhir:**
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

Baris ber-`—` pada kolom pageId: id belum dicatat; skill harus mencarinya lewat CQL judul sebelum
menyimpulkan halaman itu tidak berubah.
