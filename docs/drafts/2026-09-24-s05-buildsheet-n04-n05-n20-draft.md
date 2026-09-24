🔲draft 生成时间：2026-09-24T14:30:00Z（Asia/Bangkok 2026-09-24 21:30 +07:00）；本稿合并 2026-09-24T11:52:01Z 首稿与其后 N20 接线、marker 订正两轮变更。
目标页：纪律与绩效改进处置｜建造单（pageId 2096463922）
🔲性质：草稿，尚未写入 Confluence；对照本页现行版本起草，提交前须按 G-01 流程重读本页当前版本，并按本页体例以「【2026-09-24 补】」追加、原文保留不删。

---

## 🔲一、配置对应表（N04／N05／N20 三行「状态」列追加补注）

🔲**N04 路由分发**：【2026-09-24 补】已建骨架（inactive），登记见第五区。

🔲**N05 重复案件与历史记录检查**：【2026-09-24 补】已建骨架（inactive），登记见第五区。

🔲**N20 解雇自动开单与交接**：【2026-09-24 补】已建骨架（inactive）并接入离职侧「系统触发入口」，登记见第五区；该入口尚未发布，本件不可端到端运行。

---

## 🔲五、n8n workflow 清单（新增三行，本区首次登记）

🔲**【2026-09-24 补·本流程首批 n8n 件登记】** 依第一区配置对应表 2026-09-18 已登记「未建（可建）」，现已建成骨架，登记如下：

**N04 路由分发**：Workflow 全名 纪律与绩效改进处置｜N04｜路由分发，ID `UBLsvYaSlCI3pLWs`，active 状态 false（inactive）。🔲无对应共享件（仅 executeWorkflow 调用 N05）。🔲凭证状态不适用（无 httpRequest 节点）。登记人 Bambang，登记日期 2026-09-24。

**N05 重复案件与历史记录检查**：Workflow 全名 纪律与绩效改进处置｜N05｜重复案件与历史记录检查，ID `LJwiAZFfnuq6tmju`，active 状态 false（inactive）。对应共享件为 Jira 原生节点（如 "Confirm Case Visible"，Bot_SSC 建件时自动挂上）。凭证状态：节点 "Write Duplicate Marker Comment (internal)"（httpRequest）→ Bot_SSC (Jira write)，🔲建造人 Bambang 本人报告已于 UI 操作并目视确认已保存；🔲本侧未经 API 独立回读，因 `get_workflow_details` 不回传凭证字段。登记人 Bambang，登记日期 2026-09-24。

**N20 解雇自动开单与交接**：Workflow 全名 纪律与绩效改进处置｜N20｜解雇自动开单与交接，ID `ToIGnEJmksSPhC85`，active 状态 false（inactive）。对应共享件为 B6（`hf4KKa7CytWxjAFy`，直属上下级解析）。🔲B6 调用节点尚未建入本件（见附表）。凭证状态：节点 "Create Trigger Link (S-05 to resignation)"、"Write Triggered Marker Comment (internal)"（均 httpRequest）→ Bot_SSC (Jira write)，🔲建造人 Bambang 本人报告已于 UI 操作并目视确认已保存；🔲本侧未经 API 独立回读，理由同上。登记人 Bambang，登记日期 2026-09-24。

**本件现行版本（2026-09-24 API 回读）**：versionId `e713b9cf-93f5-441f-8ce1-63cbb2b4aed0`，updatedAt 2026-09-24T14:17:58.098Z，active false，节点 10 个。

🔲**N20 接线（2026-09-24）**：节点 "Call Resignation Upstream Trigger Entry" 已指向离职侧入口 `qa01CkZBQfx8eLsK`（员工离职｜上游触发入口），取代原占位值。🔲传入字段按 Geri 于 NSE-1137 c50494 公布的五项交接契约：upstreamSource · upstreamCaseKey · employeeAccountId · dismissalCategoryId · judgmentRef。🔲其中 upstreamSource 暂填 `S-05 N20`；该值写入离职侧审计备注「由 {上游主单 key} 的 {upstreamSource} 触发」，已于 NSE-1137 c50501 请 Geri 确认。

🔲**N20 返回判定（2026-09-24 新增节点 "Check Entry Result"）**：离职侧入口返回 `{ok, created, issueKey, reason}`（NSE-1137 c50494）。🔲本节点仅在 `ok:true` 且带 `issueKey` 时放行，否则抛错中止；`created:false` 带 `issueKey` 视为防重复命中、属成功，不重试。

🔲**N20 Trigger link 节点停用（2026-09-24）**：节点 "Create Trigger Link (S-05 to resignation)" 已停用，不删除。依据：员工离职 Spec「系统触发入口」行原文——「同一条规则内建 Trigger link（上游主单 triggers 离职主单，link 类型 10075，主单对主单）并在离职主单写审计备注」；🔲即 Trigger link 由离职侧入口在建单同一规则内建立，S-05 侧再建将产生重复 link。🔲Kent 于 NSE-1137 c50382 亦将 Trigger link 与审计备注列入入口职责。

🔲**N20 marker 订正（2026-09-24）**：marker 由原 `nos-s05-n20-triggered` 改为本页暗号接口契约表登记的 `[[nos-s05-term:<S05主单key>:<离职主单key>]]`，读写两节点同步修改。🔲原 token 与本页登记不符，系建造时未核对本页暗号接口契约表所致；该件自建成至订正均为 inactive、未运行，未产生任何 marker。

🔲**未解限制（凭证挂接）**：07.06.1 E5 原文——「新建 httpRequest 节点仍须 UI 手工挂凭据（API 对 predefinedCredentialType 的挂载被拒）」。🔲N05／N20 同样命中，非本流程个案。

🔲**04.9 登记缺口（沿用本区既有登记，2026-09-20 已记，本次未变）**：本区原文——「S-05 的块落在哪一册（新开 04.9.7 还是并入现有册）须由 04.9 Owner（Alden）定，建造侧不自行建页」。🔲N04／N05／N20 暂只记入本页，04.9 索引与详情块待 Alden 指定分册后补登。

---

## 🔲暗号接口契约表（「离职交接认领与审计」行追加补注）

🔲**【2026-09-24 补｜原文保留不删】** N20 已按本行语法实建：`[[nos-s05-term:<S05主单key>:<离职主单key>]]`，由节点 "Write Triggered Marker Comment (internal)" 写入 S-05 主单、由 "Check Already Triggered" 读取判定。🔲状态由「拟定·未建」改为「已建·inactive」。

🔲本行「写入时机」与实建两处不符，如实登记：

🔲①本行原文「建离职单**之前**先写 S-05 侧」；离职主单 key 于建单前不存在，现 N20 于离职侧入口返回 issueKey 之后写入。

🔲②本行原文「离职单建成后补写离职侧」；离职侧审计备注现由离职侧入口写入，依据同第五区「Trigger link 节点停用」段所引 Spec 原文，S-05 侧不写离职主单。

🔲本表约束「先认领后动作」与「link 判定与 marker 判定并存」两条，N20 现均未满足：N20 于写入后写 marker，且仅读 marker、不读 link。

🔲离职侧入口的防重复开单按上游主单 key 执行：Geri（NSE-1137 c50494）原文「`created:false` with an `issueKey` means the idempotency guard hit on `upstreamCaseKey`」。🔲N20 侧是否仍须补齐上述两条约束，列入附表待定。

---

## 八、测试与守护记录（追加）

**N05／N20**：🔲尚无任何测试记录。🔲N05 workflow description 原文——"Built inactive, needs dry-run + errorWorkflow + Alden approval."；🔲N20 Sticky Note 现行原文——"N20 -- wired to Geri's entry, not yet end to end"。🔲两者均未挂 `settings.errorWorkflow`（应挂 `VUIgv9Ujj1KEoIne`，同第六区既有标配）。

🔲**N20 端到端测试前提**：离职侧入口现为骨架，Geri 原文「So today it returns `ok:false, created:false` with a reason saying exactly that」；🔲故入口发布前，N20 任何试跑均止于 "Check Entry Result"。

---

## 🔲附｜建设待办／阻塞表（追加五行，另补注一行）

**事项一**：Abort Case（id 11）转态权限配给 HR Ops & Data 角色组，N07「确认重复」同口径。🔲依赖 Bambang（经 Jira admin console，无对应 API 操作）。解除判据：权限配置完成并回读确认。🔲不做的后果：该转态路径无法按 04.3 v35 §六执行顺序落地。🔲状态：待办，尚未开始。

🔲**事项二｜离职侧「系统触发入口」发布**：依赖 Geri（入口）与 Alden（发布放行）。🔲解除判据：入口经 Alden 放行发布，且 NSE-1137 c50388 第 1 项（「已建单、待资料补齐」状态）已定。🔲不做的后果：N20 无法端到端运行。🔲状态：阻塞中。

🔲**事项三｜交接契约两项待 Geri 确认**：①upstreamSource 取值；②离职侧入口 Trigger link 的 inward／outward 方向。🔲已于 NSE-1137 c50501 提出。🔲解除判据：Geri 答复并回读 N20 与入口两侧一致。🔲状态：待办。

🔲**事项四｜N20 未建部分**：D-10 通知 Direct Supervisor；经 B6 解析直属上级，解析失败拦截并告警；挂 `settings.errorWorkflow`；写入 Spec 增补区 A 表「离职单关联状态」与「下游流程触发状态／关联 Ticket」两字段。🔲依赖建造侧。🔲状态：待办。

🔲**事项五｜N20 与暗号接口契约表约束**：「先认领后动作」「link 判定与 marker 判定并存」两条于 N20 未满足，见暗号接口契约表本次补注。🔲依赖建造侧（须先定 N20 侧是否仍需补齐）。🔲状态：待办（建造侧提出·双签未表态）。

🔲**补注既有行「员工离职 Spec 系统触发接收入口」**：【2026-09-24 补】入口已由 Geri 建为骨架 `qa01CkZBQfx8eLsK`（NSE-1137 c50494），未发布；本行状态不变。

🔲**04.3 v35 §六（OSD-116 c50442／c50445）已确认适用本流程；缺位规则退回**：Kayden Lee（c50461）原文——「变更：直属上级缺位规则：撤回本卡 2026-09-10 留言中『直属上级缺位时由 HR Ops & Data 代为受理提交，代提交的案件首层审核自动升至 Head of HR』一句」。🔲Alden（c50468）与 Kent（c50472）确认通用规则改为：解析失败一律 stop + alert，HR 修正档案后重新提交。🔲Spec 已由 Felix 同步修订，Felix（c50486）原文——「S-05 Spec 已完成对应修订，页面现 v67（内部版本 v28）」，涉及节点表 N03／N07／N16／N17／N20／N21 与增补区 A／B／C／D 表。🔲本建造单若曾引用旧版缺位处理逻辑，一律以 Spec v67 为准。

---
🔲维护说明｜本稿由 Bambang 通过 Claude Code 起草，尚未提交；提交前须逐项核对上列 🔲 标记项，并按建造单既有纪律（不假填、回读路径注明）补全或订正。
