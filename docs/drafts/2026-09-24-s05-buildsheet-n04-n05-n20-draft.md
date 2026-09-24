🔲draft 生成时间：2026-09-24T11:52:01Z（Asia/Bangkok 2026-09-24 18:52 +07:00）
目标页：纪律与绩效改进处置｜建造单（pageId 2096463922）
🔲性质：草稿，尚未写入 Confluence，待 Bambang 校对确认后再走 G-01 outbound 流程正式提交。

---

## 🔲五、n8n workflow 清单（新增三行，本区首次登记）

🔲**【2026-09-24 补·本流程首批 n8n 件登记】** 依第一区配置对应表 2026-09-18 已登记「未建（可建）」，现已建成骨架，登记如下：

**N04 路由分发**：Workflow 全名 纪律与绩效改进处置｜N04｜路由分发，ID `UBLsvYaSlCI3pLWs`，active 状态 false（inactive）。🔲无对应共享件（仅 executeWorkflow 调用 N05）。🔲凭证状态不适用（无 httpRequest 节点）。登记人 Bambang，登记日期 2026-09-24。

**N05 重复案件与历史记录检查**：Workflow 全名 纪律与绩效改进处置｜N05｜重复案件与历史记录检查，ID `LJwiAZFfnuq6tmju`，active 状态 false（inactive）。对应共享件为 Jira 原生节点（如 "Confirm Case Visible"，Bot_SSC 建件时自动挂上）。凭证状态：节点 "Write Duplicate Marker Comment (internal)"（httpRequest）→ Bot_SSC (Jira write)，🔲建造人 Bambang 本人报告已于 UI 操作并目视确认已保存；🔲本侧未经 API 独立回读，因 `get_workflow_details` 不回传凭证字段。登记人 Bambang，登记日期 2026-09-24。

**N20 解雇自动开单与交接**：Workflow 全名 纪律与绩效改进处置｜N20｜解雇自动开单与交接，ID `ToIGnEJmksSPhC85`，active 状态 false（inactive）。对应共享件为 B6（`hf4KKa7CytWxjAFy`，直属上下级解析）。凭证状态：节点 "Create Trigger Link (S-05 to resignation)"、"Write Triggered Marker Comment (internal)"（均 httpRequest）→ Bot_SSC (Jira write)，🔲建造人 Bambang 本人报告已于 UI 操作并目视确认已保存；🔲本侧未经 API 独立回读，理由同上。登记人 Bambang，登记日期 2026-09-24。

🔲**未解限制**：N20 workflow 内 Sticky Note 原文记载——"Both httpRequest nodes need Bot_SSC (Jira write) attached manually via desktop browser UI -- API attachment of predefinedCredentialType on a new httpRequest node is rejected (07.06.1 E5), same limitation N05 hit." 即：新建 httpRequest 节点的凭证无法经 API 挂接，须走 UI 手工操作，此为平台限制（07.06.1 E5），N05／N20 同样命中，非本流程个案。

🔲**N20 未解阻塞**：节点 "Call Resignation Upstream Trigger Entry"（executeWorkflow）之 `workflowId` 仍为占位值 `<__PLACEHOLDER_VALUE__Geri's resignation 系统触发入口 workflow id -- not built yet, see OSD-116 c50381 / NSE-1137 c50387/c50435__>`。🔲等待员工离职 Spec「系统触发入口」的实际 n8n workflow ID。🔲2026-09-24 以「系统触发入口／入口／resignation／trigger entry」四组关键词搜索 n8n 全库，均未见对应新建 workflow（本侧搜索结果，未另行独立核验完整性）。

🔲**04.9 登记缺口（沿用页首既有登记，2026-09-18 已记，本次未变）**：本页第五区原文——「本流程在 04.9 尚无详情分册……S-05 的块落在哪一册（新开 04.9.7 还是并入现有册）须由 04.9 Owner（Alden）定，建造侧不自行建页」。🔲N04／N05／N20 暂只记入本页，04.9 索引与详情块待 Alden 指定分册后补登。

---

## 八、测试与守护记录（追加）

**N05／N20**：🔲尚无任何测试记录。🔲N05 workflow description 原文——"Built inactive, needs dry-run + errorWorkflow + Alden approval."；🔲N20 Sticky Note 原文——"N20 -- skeleton, not wired end to end." 两者均未挂 `settings.errorWorkflow`（应挂 `VUIgv9Ujj1KEoIne`，同第六区既有标配）。

---

## 🔲附｜建设待办／阻塞表（追加两行）

**事项一**：Abort Case（id 11）转态权限配给 HR Ops & Data 角色组，N07「确认重复」同口径。🔲依赖 Bambang（经 Jira admin console，无对应 API 操作）。解除判据：权限配置完成并回读确认。🔲不做的后果：该转态路径无法按 04.3 v35 §六执行顺序落地。🔲状态：待办，尚未开始。

🔲**事项二**：N20 node "Call Resignation Upstream Trigger Entry" 之 workflowId 占位。依赖 Geri（建成并 publish 其离职侧「系统触发入口」workflow，回传 ID）。解除判据：Geri 提供实际 workflow ID 且已 publish。🔲不做的后果：N20 无法端到端 dry-run。状态：阻塞中，等待对方。

🔲**04.3 v35 §六（OSD-116 c50442／c50445）已确认适用本流程；缺位规则退回**：Kayden Lee（c50461）原文——「变更：直属上级缺位规则：撤回本卡 2026-09-10 留言中『直属上级缺位时由 HR Ops & Data 代为受理提交，代提交的案件首层审核自动升至 Head of HR』一句」。🔲Alden（c50468）与 Kent（c50472）确认通用规则改为：解析失败一律 stop + alert，HR 修正档案后重新提交。🔲Spec 已由 Felix 同步修订，Felix（c50486）原文——「S-05 Spec 已完成对应修订，页面现 v67（内部版本 v28）」，涉及节点表 N03／N07／N16／N17／N20／N21 与增补区 A／B／C／D 表。🔲本建造单若曾引用旧版缺位处理逻辑，一律以 Spec v67 为准。

---
🔲维护说明｜本稿由 Bambang 通过 Claude Code 起草，尚未提交；提交前须逐项核对上列 🔲 标记项，并按建造单既有纪律（不假填、回读路径注明）补全或订正。
