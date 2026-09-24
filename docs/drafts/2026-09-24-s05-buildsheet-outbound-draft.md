〔插入位置：配置对应表 表后〕

【2026-09-24 补】N04 路由分发：已建骨架，active 状态 false。

【2026-09-24 补】N05 重复案件与历史记录检查：已建骨架，active 状态 false。

【2026-09-24 补】N20 解雇自动开单与交接：已建骨架，active 状态 false。

登记见「n8n workflow 清单」区。

〔插入位置：workflow 清单区 本区末〕

【2026-09-24 补·本流程首批 workflow 登记】

**N04 路由分发**：全名 纪律与绩效改进处置｜N04｜路由分发，ID `UBLsvYaSlCI3pLWs`，active 状态 false。本件调用 N05 并返回其输出，不做业务判断。登记人 Bambang，登记日期 2026-09-24。

**N05 重复案件与历史记录检查**：全名 纪律与绩效改进处置｜N05｜重复案件与历史记录检查，ID `LJwiAZFfnuq6tmju`，active 状态 false。凭证：节点 "Write Duplicate Marker Comment (internal)" 挂 Bot_SSC (Jira write)，经 UI 手工挂接，UI 目视确认人 Bambang。登记人 Bambang，登记日期 2026-09-24。

**N20 解雇自动开单与交接**：全名 纪律与绩效改进处置｜N20｜解雇自动开单与交接，ID `ToIGnEJmksSPhC85`，active 状态 false。凭证：本件 httpRequest 节点均挂 Bot_SSC (Jira write)，经 UI 手工挂接。UI 目视确认人 Bambang。登记人 Bambang，登记日期 2026-09-24。

本件现行版本（2026-09-24 API 回读）：versionId `e713b9cf-93f5-441f-8ce1-63cbb2b4aed0`，updatedAt 2026-09-24T14:17:58.098Z，active false，节点 10 个。

节点 "Call Resignation Upstream Trigger Entry" 已指向离职侧入口 `qa01CkZBQfx8eLsK`，取代原占位值。该入口全名 员工离职｜上游触发入口（S-05 等上游解雇 → 自动开单）。传入字段 5 项：upstreamSource、upstreamCaseKey、employeeAccountId、dismissalCategoryId、judgmentRef。字段名依 Geri 在 NSE-1137 公布的交接契约。upstreamSource 暂填 `S-05 N20`。该值已于 NSE-1137 c50501 请 Geri 确认。

新增节点 "Check Entry Result"：仅当入口返回 `ok:true` 且带 `issueKey` 时放行，否则抛错中止。`created:false` 带 `issueKey` 为防重复命中，属成功，不重试。

节点 "Create Trigger Link (S-05 to resignation)" 保留在件内，状态为停用。依据员工离职 Spec「系统触发入口」行原文：「同一条规则内建 Trigger link（上游主单 triggers 离职主单，link 类型 10075，主单对主单）并在离职主单写审计备注」。

marker 已改为本页暗号接口契约表登记的 `[[nos-s05-term:<S05主单key>:<离职主单key>]]`。读取节点 "Check Already Triggered" 与写入节点 "Write Triggered Marker Comment (internal)" 同步修改。

07.06.1 原文：「新建 httpRequest 节点仍须 UI 手工挂凭据（API 对 predefinedCredentialType 的挂载被拒）」。

沿用本区既有登记：S-05 的块落在哪一册（新开 04.9.7 还是并入现有册）须由 04.9 Owner（Alden）定，建造侧不自行建页。

〔插入位置：暗号接口契约表 表后〕

【2026-09-24 补｜原文保留不删】「离职交接认领与审计」行：N20 已按本行语法实建，状态由「拟定·未建」改为「已建·inactive」。

本行「写入时机」与实建不符之处如下。

本行原文「建离职单之前先写 S-05 侧」。离职主单 key 由离职侧入口建单后返回，现实建于入口返回 issueKey 之后写入。

本行原文「离职单建成后补写离职侧」。离职侧审计备注现由离职侧入口写入，依据员工离职 Spec「系统触发入口」行：「并在离职主单写审计备注」。

本表约束「先认领后动作」要求写入口在写动作之前先写认领 marker。本件的重复判定读取 S-05 主单 comment 中的 marker。离职侧入口按上游主单 key 防重复开单。本件是否仍须补齐本表上述约束，列入附表。

〔插入位置：测试与守护记录区 测试记录表后〕

【2026-09-24 补】离职侧入口现为骨架，Geri 原文「So today it returns ok:false, created:false with a reason saying exactly that」。入口发布前，本件试跑止于 "Check Entry Result"。本件上线前须挂 `settings.errorWorkflow` → `VUIgv9Ujj1KEoIne`。

〔插入位置：附｜建设待办／阻塞表 表内追加行〕

| 事项 | 依赖谁 | 解除判据 | 不做的后果 | 状态 |
| --- | --- | --- | --- | --- |
| Abort Case（id 11）转态权限配给 HR Ops & Data 角色组，N07「确认重复」同口径 | 建造侧（经 Jira admin console） | 执行顺序依 Kayden 原文：「先把主单转「已取消」，再取消未关子单」 | 「反过来先关子单，模式五会抢先把主单判成「已完成」」 | 待办 |
| 离职侧「系统触发入口」`qa01CkZBQfx8eLsK` 发布 | Geri（入口）＋Alden（发布放行） | 入口经 Alden 放行发布，且「待资料补齐」状态口径已定 | Geri 原文「N20 cannot call it before then either」 | 阻塞中 |
| upstreamSource 取值待 Geri 确认 | Geri | Geri 答复后回读两侧一致 | 该值写入离职侧审计备注「由 {key} 的 {upstreamSource} 触发」 | 待办 |
| 离职侧入口 Trigger link 的 inwardIssue／outwardIssue 方向待 Geri 核对 | Geri | Geri 答复后回读一致 | Kent 契约原文「S-05 triggers resignation」 | 待办 |
| 本件后续须建：D-10 通知 Direct Supervisor、经 B6 解析直属上级、挂 errorWorkflow | 建造侧 | 逐项建成并回读 | Spec 本节点要求：「若系统无法解析出该员工的 Direct Supervisor，系统拦截并告警，转 HR 修正档案后重新解析」 | 待办 |
| Spec 增补区 A 表「离职单关联状态」由 N20／N21 系统写入 | 建造侧 | 字段写入建成并回读 | 该字段记录「该Case交接进员工离职流程的进度」 | 待办 |
| 本件与本页暗号接口契约表「先认领后动作」约束的适用 | 建造侧 | 明确本件侧是否补齐并登记 | 本件重复判定方式与本页约束不一致 | 待办（建造侧提出·双签未表态） |

〔插入位置：附｜建设待办／阻塞表 表后〕

【2026-09-24 补｜原文保留不删】既有行「员工离职 Spec 系统触发接收入口」：入口已由 Geri 建为骨架。入口 ID `qa01CkZBQfx8eLsK`。Geri 原文「It creates nothing until it is published through Alden's gate」。本行状态不变。

【2026-09-24 补｜原文保留不删】建设备注「上下级解析」段中「须经白话对齐向 Felix 确认本流程口径」一句已不适用。Kent 于 OSD-116 原文：「no longer applies — any resolution failure = stop + alert」。

【2026-09-24 补】直属上级缺位规则：Kayden 撤回「直属上级缺位时由 HR Ops & Data 代为受理提交，代提交的案件首层审核自动升至 Head of HR」一句。Felix 原文：「S-05 Spec 已完成对应修订，页面现 v67（内部版本 v28）」。本页凡引用旧缺位处理逻辑者，以 Spec v67 为准。
