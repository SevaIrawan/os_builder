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

| Halaman | pageId | Versi tercatat | Owner |
| --- | --- | --- | --- |
| 07｜指南 | 1704362028 | v28 | Kayden |
| 07.01｜盘点与切分指南 | 1705508891 | — | Kayden |
| 07.03｜设计指南 | 1695744021 | v58 | Kayden |
| 07.04｜结构审计指南 | 1744896004 | v27 | Kayden |
| 07.05｜对齐指南 | — | v5 | Kayden |
| 07.06｜建设指南 (sumber CLAUDE.md §八) | 1730347066 | **v30** | Alden |
| 07.06.1｜开发规则与避坑指南 | 1712226375 | **v34** | Alden |
| 04｜总纲 (sumber anchor) | 1676804100 | **v25** | Kayden |
| 04.0｜词汇表 | 1676640265 | v26 | Kayden |
| 04.1｜Project 判定 | 1676738564 | v46 | Kayden |
| 04.2｜单据体系 | 1676607500 | v40 | Kayden |
| 04.3｜状态与 Workflow | 1676771343 | v33 | Kayden |
| 04.4｜自动化配置模式库 | 1677066244 | **v33** | Alden |
| 04.4.1｜模式九 | 1729888419 | v13 | Alden |
| 04.4.2｜B6 契约 | — | v12 | Alden |
| 04.4.3｜身份件契约 | 2076508181 | v6 | Alden |
| 04.4.4｜协作 Thread 契约 | 2102067228 | **v4** | Alden |
| 04.5｜Spec 与建造单规范 | 1678573617 | v79 | Kayden |
| 04.5.1｜Spec 模板 | 1685979182 | v19 | Kayden |
| 04.5.2｜建造单模板 | 1729626775 | v11 | Alden |
| 04.5.3｜Sandbox 与测试 | 1729626578 | v13 | Alden |
| 04.6｜n8n 使用规范 | 1690927120 | v20 | Alden |
| 04.7｜Router SSOT | 1691254793 | **v46** | Alden |
| 04.8｜Registry SSOT | 1690140756 | **v21** | Alden |
| 04.9｜n8n Workflow SSOT | 1693089805 | **v106** | Alden |
| 04.9.1｜详情：平台 | 1764622422 | **v19** | Alden |
| 04.10｜Jira 共享配置治理 | 1738735636 | v19 | Kent |
| 04.11｜Slack Channel 登记表 | 1764524046 | v2 | Alden |
| 04.12｜机读标记总清单 | 2091876367 | v5 | Kent |
| Notify 子流程调用契约 | 1603633175 | v13 | Alden |
| OS 开发流｜流程 Spec | 1729200354 | v39 | Kayden／Kent |
| HR｜盘点与切分 | — | v38 | Felix |
| 纪律与绩效改进处置｜流程 Spec (S-05) | 2036858900 | **v62** (冻结基线 v61) | Felix |
| 纪律与绩效改进处置｜建造单 | 2096463922 | **v37** | Bambang (BO) |

**Tebal** = bergerak pada sapuan 2026-09-21 dan sudah dibaca diff-nya (lihat
`docs/reading-notes-2026-09-21.md` bagian VERSION SWEEP).

Baris ber-`—` pada kolom pageId: id belum dicatat; skill harus mencarinya lewat CQL judul sebelum
menyimpulkan halaman itu tidak berubah.
