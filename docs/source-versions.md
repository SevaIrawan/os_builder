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
> **Sweep 2026-09-25 ~10:50Z (nosm-sync-check, "hi")**
> Connectors: Atlassian_MCP `atlassianUserInfo` ok (toolu_01UmfairhsGHYTtJ7KWXePwi); Rovo `getConfluencePage` 1704362028 ok
> (toolu_01SAzvVobLn8BTG6yKyPNpFM); n8n `search_workflows` ok (toolu_016EtSznWR66XEdR5Mi1PvQM).
> Controlled copies: `sync_check.py` exit 0 against 07.06 **v30** (toolu_01W8PR2UoDT1kRTsSrq8MZwR) and
> 04 **v25** (toolu_014QiDuog2LBX59mcK1e1ept): 19/19 bullets, preamble and 冻结要求 same; tables 4/4, 6/6, 15/15.
> VERDICT: no deployment drift.
> CQL `space = NOSM AND type = page AND lastmodified >= "2026-09-25"` (toolu_01D8mr5ijRCxT5X1FPF2YLkJ): totalSize **17**;
> control `>= "2026-09-24"` (toolu_01HXd3YBtijrkQ4msqyce4e8): totalSize **50**.
> `sweep_check.py` exit 0: 32 pages with a pageId, 32 checked live, 3 moved, 0 not checked. The two rows without a
> pageId were found by title (toolu_01Rx9Dzj5oSSddTVUAqRXQBA): 07.05 = 1744306526 **v5**, 04.4.2 = 1751547935 **v12**, both unchanged.
> Moved, diff read:
> - **07.06.1 v37 → v38** (toolu_013Lb8wGpxLtYEm24j2M3Whh): C9 规避方式 adds how to tell where time was lost on
>   `expired_trigger_id` (execution start minus `x-slack-request-timestamp`). Version message: 「C9 补排查判别法（签发时刻 vs 执行开始时刻）」.
> - **04.5.3 v15 → v16** (toolu_01YVqpov8nUjAZ145kUXyzy4): example subjectId 「TAL-184 TEST Ali」 → 「TAL-TEST-001 TEST Ali」.
> - **04.9 v114 → v115** (toolu_012AR3GUAnr3M8qiK4Q17Efd): only the Grade N2 index row; adds 「Alden c50515 准发，1a892463 已发布」
>   and Call N3 still disabled. No S-05 row added.
> None of the three changes touches S-05.

| Halaman | pageId | Versi tercatat | Owner |
| --- | --- | --- | --- |
| 07｜指南 | 1704362028 | v28 | Kayden |
| 07.01｜盘点与切分指南 | 1705508891 | v47 | Kayden |
| 07.03｜设计指南 | 1695744021 | v58 | Kayden |
| 07.04｜结构审计指南 | 1744896004 | v27 | Kayden |
| 07.05｜对齐指南 | 1744306526 | v5 | Kayden |
| 07.06｜建设指南 (sumber CLAUDE.md §八) | 1730347066 | **v30** | Alden |
| 07.06.1｜开发规则与避坑指南 | 1712226375 | **v38** | Alden |
| 04｜总纲 (sumber anchor) | 1676804100 | **v25** | Kayden |
| 04.0｜词汇表 | 1676640265 | v26 | Kayden |
| 04.1｜Project 判定 | 1676738564 | v46 | Kayden |
| 04.2｜单据体系 | 1676607500 | **v40** | Kayden |
| 04.3｜状态与 Workflow | 1676771343 | **v35** | Kayden |
| 04.4｜自动化配置模式库 | 1677066244 | **v33** | Alden |
| 04.4.1｜模式九 | 1729888419 | v13 | Alden |
| 04.4.2｜B6 契约 | 1751547935 | v12 | Alden |
| 04.4.3｜身份件契约 | 2076508181 | v6 | Alden |
| 04.4.4｜协作 Thread 契约 | 2102067228 | **v4** | Alden |
| 04.5｜Spec 与建造单规范 | 1678573617 | v79 | Kayden |
| 04.5.1｜Spec 模板 | 1685979182 | v19 | Kayden |
| 04.5.2｜建造单模板 | 1729626775 | v11 | Alden |
| 04.5.3｜Sandbox 与测试 | 1729626578 | **v16** | Alden |
| 04.6｜n8n 使用规范 | 1690927120 | v20 | Alden |
| 04.7｜Router SSOT | 1691254793 | **v51** | Alden |
| 04.8｜Registry SSOT | 1690140756 | **v21** | Alden |
| 04.9｜n8n Workflow SSOT | 1693089805 | **v115** | Alden |
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
