# Reading notes — S-05 建设 source sweep (2026-09-21)

> Catatan bacaan pribadi builder (Bambang). Bukan dokumen sah; sumber sah tetap halaman Confluence dan komentar Jira yang dirujuk. Versi halaman dan id komentar dicatat pada saat dibaca.

# Reading log 2026-09-21 (no execution; facts only, page/version cited)

## 07｜指南 v28 (2026-09-14)
- §二 通用纪律: 锚点导向 / 链接必读 / 标准页读法(🔲・待定・规划中・锁定 = 缺口, 不得自行填补) / 先查后写 / 登记义务(04.7 两阶段; 04.8; 04.9 三位一体) / 缺口纪律 / 节点编号写法「OS开发流Spec｜N#（节点名）」/ Jira Comment 过程沟通(事件触发才留言; 写前读近期 Comment, 写后回读).
- §三 归口表: 标准页写错/矛盾/缺规则 → 页尾 Owner; 两页矛盾且 Owner 不同 → Kayden; venue #nos-bo C0BRSTNNY4A, six-field format; 3 工作日. 改进提案 → #nos-bo 三段(现状/建议/影响面). 分流: 标准缺口 (修复对象=标准页/登记表) vs 业务歧义 (修复对象=该流程 Spec, 按阶段指南退回).
- 授权总表指针: 不用请示三类与红线 07.06.1 六-2; 测试白名单 04.5.3 §二; 平台件回应时限/缺位代理 04.6 §3.6/§3.4.

## 07.06.1 v34 (2026-09-21 07:11Z) — was v33 (2026-09-18); v33→v34 delta di bagian VERSION SWEEP di bawah
- §三 主题速查 (relevant to S-05 build): 第一次建一条流程 → §四全节+通读§五; 改共享对象 → A7,A6,六-2; Thread 绑定 → C7,C6,A2,A3; 聚合/催办 → C8,C1,D3; 测试件/测试单/清理 → D7,C3,六-2; n8n↔Jira → A2,A3,A4,A8,B1,B3,B5,D2,D8,E11,E16; 发通知 → C1–C6; 上线 → D1,D3,D5,§四7–9; 拿返回值下结论 → E1–E16; 先查找再守护 → E9,E7,D3.
- §四 固定次序: 先读→先分流→先查登记表→先建再登记最后启用→create screen(A6)→dry后run(D1)→回读→bounce(D8)→三合一.
- 六-2 不可逆动作先确认 (确认对象=正在使用 AI 的开发者本人): 删除任何对象; 修改现有共享资源(平台件/共享 Field/Scheme); 批量写>20; 向真实员工手工触发通知/邮件 + 改动后首次真发; workflow 切 active (须平台 Owner 批, 04.6 §3.6 第4步). 不下放写权线: Spec 语义/跨流程衔接措辞. 不用请示: inactive n8n 件新建/修改; 登记处按六-4 自判.
- 六-1 任务记录: Jira comment (做了什么/对象+ID/坑) + description 顶部 📌 现状块.
- 六-4 登记处: n8n→04.9; RT→04.7; 档案/实体→04.8; Project→04.1; Jira 共享配置→04.10; Slack Channel→04.11; 查不到登记处→07 §三缺口回报 (建造单 row 14 Screen 即此).
- Key pits for S-05: A2 幂等闸 (建造单 row 30); A6 create screen (row 14 ④); A7 共享对象; C1 三层通知; C4 验签 fail-closed + 04.6 §3.5 四档; E8 cf ID 不看名字 (cf18002 Talent Status = 在职判据); E11 comment body string vs ADF (marker 回扫); E16 JQL 0 条对照探针.

## 04｜总纲 v25 (2026-09-05)
- §一 平台建设行: 先读 第二、四、五节＋04.5／04.6／07.04; 责任边界「按冻结 Spec 建造并维护建造单；不得擅改业务语义」.
- §二 阶段 6 开发: 主责 Alden／BO 建造 Owner; Gate 「建造单第 1–8 区按适用性完成；实际对象、ID、回读和 Candidate 消费证据齐全」.
- §三 建造单: 「进入开发 Gate 时建立并与 Spec 双向互链」; 结构审计记录住 Feature Comment + Spec 状态区.
- §四 建造单原子动作: 「建页、Spec 双向链接、BO Owner 与来源 Jira Feature 同次登记」; 原子绑定: 无双向入口 = 未完成.
- §七 AI 机器执行合同 8 条 + 强制停止条件 (权威页打不开; 规则冲突; 业务语义未裁决; Owner 不明; 前置未齐; 登记触发命中但无行; 证据缺失; 配置与 Spec/建造单不一致). 停止时指出阻塞对象、阻塞人、恢复条件.
- §六 子页地图 = docs/04-anchor-navigation.md (in sync).

## 04.0 v26 (2026-09-19)
- §二 主单 = Master Ticket; 「住在 SSCSD 的单即主单」; 每类单据对应一个 Jira Issue Type 一一对应 (建造单 row 33 question).
- §三 状态表 载体列硬约束; 已取消: 主单侧=请求人在「待审批」内自助撤回; 子单/任务卡侧=上游中止或误建, 由服务账号或该 Team Project Owner 关闭; 维护单侧=页面 Owner 关闭. 「窗口与转态权限见 04.3 第六节」. 主单终态四个; 子单两个.
- §五 双语格式: 短串 中文 · 英文; 全角「｜」不得出现在名称内; 适用 2026-09-05 起新建/修订.

## 04.2 v40 (2026-09-19)
- §一 单据总表: 主单 Issue Type = Master Ticket, SSCSD; 子单 Sub-ticket 仅编排(服务账号)创建必带阻塞 link; 任务卡 Task; 维护单 GOV. 有人工执行段判断线 = 一处判断三处使用 (04.7 字段 / 04.3 形状 / 子单).
- §二 三条护栏: link 是功能真相; 类型由创建通道决定; 角色不迁移.
- §三 link 拓扑: 阻塞 link 唯一方向 子单→锚点; 星形. 跨流程 Triggers/is triggered by, 锚点对锚点; 触发细节写审计 comment 「由 {上游主单 key} 的 {节点／子单} {事件} 触发」; 不得用 Blocks. (Jira 实名 Trigger id 10075 per Spec T-5.)
- §四 跨流程触发建卡; 无请求人流程同样开主单; 入口类型与审批是两个开关 (S-05 双入口各登记一行).
- §五 标题 `{请求类型}｜{主体标识}`; 子单 `{执行动作}｜{主体标识}`; 「｜」专用.
- §六 维护单三通道 (含受控清单变更, F-172 新增 2026-09-19).

## 04.3 v33 (2026-09-16)
- §一 载体分域表. §二 四形状; 形状 C = 待审批→待子单完成→已完成; 「待审批」三条终态转出 已拒绝/已改道/已取消(请求人撤回); 「待子单完成」中止转出 已取消 (处理方发起) — C,D 均适用. §2.1 已改道 必须带指针, 只在门控段. (建造单 row 18: Spec E 表无已改道 vs 04.3 §二 "另须配置三条终态转出" — 04.5 §七 item 2/15 说无分诊门流程 E 表登记「本流程不使用」.)
- §三 执行卡标准 Workflow 待处理→处理中→已完成 + 已取消; Execution-Card Workflow (Team) + Maintenance-Ticket Workflow (GOV) 两对象.
- §五 对外映射: 待子单完成→处理中 唯一不同名.
- §六 转态权限表 (verbatim key rows): 「待审批」批准/拒绝/改道 = 04.7 该行审批人角色经 Slack 卡校验后服务账号代执行; 主单其余转态 仅服务账号; 执行卡转态 仅 assignee 与 Team Project Owner; 主单转入已取消(撤回) 仅 reporter; 主单转入已取消(执行中止) 「仅服务账号与该主单所在 Project 的 Owner；触发与动作范围见本节下方撤回规则「进入待子单完成后」条」; 执行卡转入已取消 仅服务账号与 Team Project Owner, assignee 不得自行取消.
- §六 撤回规则: 撤回窗口=待审批; 进入待子单完成后不可自助撤回 … 「由服务账号或 Project Owner 在同一动作范围内，把已生成、尚未关闭的子单转「已取消」，并将主单转入「已取消」（转态权限见本节转态权限表）；该转态与 04.4 模式五的全关自动判定互斥——全关子单中只要有一张「已完成」，走模式五自动转「已完成」，不得再走本条中止路径。」
- §七 Resolution 四值 Done/Rejected/Cancelled/Rerouted, 一一对应, 禁止新增 (建造单 row 20); post function 写入; 重开清空; JQL 验收.
- Note: 04.3 v33 message: IN-048 §二适用范围补一句 (2026-09-16). §六 unchanged since v31 (2026-08-18).

## 04.5.2 v11 (2026-09-15) 建造单模板
- 页首 附表 (事项｜依赖谁｜解除判据｜不做的后果｜状态). 九区: 一 配置对应表 (Spec 每行; Route ID + Candidate 链接 for RT rows; 非 RT 行填「不适用」不得留空); 二 状态链表; 三 字段清单 (create screen A6); 四 Automation; 五 n8n 清单 (ID 只在 04.9); 六 复用平台件 (契约页); 七 政策参数; 八 测试与守护记录 (04.5.3 四判据 + 三层守护 + 候选 Route 消费证据行 + 收工整理确认); 九 上线三合一.
- 页首「对应 Spec」「建造状态：与 Spec 生命周期同步（建设中／已上线 vN）」「建造人」.

## 04.5.3 v13 (2026-09-15)
- §一 单实例; TEST｜命名; 非生产件 inactive; 未完成 04.9 登记不得 active; dry/run; 影子件; 收工整理.
- §二 测试档案: 建立方 = Registry 实体 Owner 部门 (员工=HR) 或显式授权人代建; 主体一份; cf17996 指向在职真人 (建设者本人或流程 Owner — 会收到测试通知); cf17994 TEST｜ 前缀; cf17993 无全角竖线; cf18002=Test; cf17995 指向有 Atlassian 账号但名下无其他档案的身份 (留空更糟). (建造单 row 10: NTP-187 复用, 上司 Kent.)
- 测试白名单: 甲 执行者本人 DM; 乙 #nos-bo C0BRSTNNY4A / #nos-ops C0BBT5ZC9L6 带 🧪 标识. 红线三处不发: #sscos-hr C0BHL8AE68G, #epic-nse-1045-squad, #general. 名单增删 = 平台 Owner 一人.
- §三 Jira 双标识 (标题 TEST｜ + 主体指向测试档案); 自动组装标题例外.
- §四 永不硬删; 清理先确认.
- §五 四判据: 真信验收 / 幂等验收 / 回读验证 / 守护登记与演练.

## 04.6 v20 (2026-09-18)
- §二 治理约束: 能 Jira-native 不用 n8n (Spec 须可说明); 判断规则住路由表; 命名 `{流程名}｜{Spec 节点 ID}｜n8n-{动作}`; 变更从 Spec 发起.
- §3.1 self-host n8n2.ohmediaa.com; 运维 Alden, 代理 Kent. §3.3 Bot_SSC 写入; 密钥 Data Table「NOS Platform Secrets」不经 AI; 新建 credential = Alden 与 Kent. §3.4 共用账号; 四条补偿纪律 (Jira 留痕; 平台件编辑串行; 密钥 Owner 填; 缺位代理 Kent 1 工作日). §3.5 三层守护; 重试铁律; nos-ops C0BBT5ZC9L6; 入站数据有误四档 甲1/甲2/乙/丙/丁 + 通用临时提示双语 + 登记要求 (建造单第八区各档落点与演练证据; 执行记录~两周清除, 摘录关键输出). §3.6 发布次序 (草稿→校验+node --check→dry→平台 Owner 批准 1 工作日→bounce); 回滚两层; 变更分级 文档先行. §3.7 实测边界 (50 条; 去重; Data Table 50 行; webhook 重投). §3.8 数据表四类; 建表权仅平台 Owner; 登记 04.9 Data Table 区. §3.9 folder: 平台/每流程一个/数据维护/归档/NOS-Build(停用); folder 不替代登记.
- §四 权威分工: 值类=Data Table; 流程形状=Spec; SLA 数值唯一来源=Spec C 表 (机器直接读); Router Store; 对账件未建.

## 04.8 v21 (2026-09-21 03:59Z — NEWER than v20 read earlier; diff pending)
- §三 纪律处分记录 row: 归属 Project 「🔲 候选｜待N5」 (unchanged); 状态列 Active→Expired/Reset; Active→已解除; 触发 S-05 N13/N26/N27; text still says 「N25（Direct Supervisor/Reporting Line+HR联合评审）」 (Reporting Line removed from Spec v23 — registry text stale; Owner Alden).
- §四 先登记后消费 (字段行); 改字段先看引用; 测试档案例外.
- §五 实体字段表: cf18002 Talent Status (Active 15575/Inactive 15576/Test 15844); cf17996 Direct Supervisor; cf17995 Employee; cf18051 Work Email; cf17998 Department (13 values after 2026-09-11: CRM×4, FOZ, SSC_FA/SSC_HR/SSC_BO, MARKETING, XLOOP, GENERAL SERVICES, NEXMAX, WEALTHPLUS); cf18029 Lifecycle Stage; cf17992 Talent ID; cf17993 Full Name; cf17994 Preferred Name; cf18030 Grade; cf18201 Actual Departure Date; etc. 「被谁消费」 for cf18002/17996/17995/18051/17998: no S-05 (建造单 row 31 stands).
- Owner Alden; 与 04.10 分界 (Registry 私有字段归 04.8).

## 04.10 v19 (2026-09-16) Owner Kent (Schema Owner)
- 纳管: 执行卡域状态集 (To Do 10003·In Progress 12956·Completed 10593·Cancelled 15961); Resolution 值集 Done 10000·Cancelled 10041·Rejected 10042·Rerouted 10043; Execution-Card Workflow bc1c8678… v6; Maintenance-Ticket Workflow 8eac050f…; Execution-Card Workflow Scheme 13093; Sub-ticket 14316; Task 10004; Maintenance Ticket 14311; fields incl Cancellation Reason cf18054 (GOV+薪资流, 跨流程共用 — 建造单 取消原因 question c50233), Slack Thread TS cf18203, Department option changes (cf17998).
- 主单侧对象 (SSCSD 四形状、主单字段) 归 SSCSD/V1 Owner Alden — NOT 04.10. Registry 字段归 04.8.
- §五 变更流程: 申请 = BO Project 开 Task 指派 Schema Owner 三格 (要什么/哪条 Spec 哪一行/为何现有不够); 口头/Slack 不受理; 先登记后启用. 升级线: 涉 SSCSD 主单侧→Alden.
- §四 差异②: Execution-Card Cancel 权限 仅 Bot_SSC＋Administrators, assignee 不可.

## 04.11 v2 (2026-08-24) Owner Alden
- 4 rows: HR sscos-hr C0BHL8AE68G; Finance nos-financial C0BERLRH5B3; BO nos-bo C0BRSTNNY4A (送达未验证); OE 死键 nos-ops C0BBT5ZC9L6. None of S-05's seven Collab channels (建造单 row 6; c50250 item 3).
- 新增领域行前置: 频道已建、Bot 已入、经生产路径首发一条并亲眼读到.

## 07.03 v58 (2026-09-19) 设计指南
- §八 交接契约 mirrors 07.06 §九 (唯一开发依据; 上游证据核验 "缺失、过期或冲突即停止并退回对应 Gate，不由建设方复跑或裁决"; 回问=业务选择题; Spec 写权两类).
- 翻译义务: 外部平台依赖清单 AI 只登记不实测, 实测归技术签.

## 07.04 v27 (2026-09-16) 结构审计指南 Owner Kayden
- 双签 AND; 基线锁 auditedVersion; VERSION_DRIFT = 审计期间页面新版本 → 本轮作废重提. 「Spec 页任何版本变化…旧结论只对旧版本有效」(§一).
- 6.4 技术签 T-1..T-6; T-5 探针任务: 技术签标注→BO 建设团队于开工前置阶段执行, 结论回写 Feature Comment 并同步 Spec 引用区「现状」栏; 未回写视为未具备. (→ S-05: 探针结论已回写 c50233; Spec 引用区「现状」栏仍「待探针」 — 引用区更新是 Spec 语义区? 依赖清单住引用区; 建设侧写权只有两类 → 回写「现状」栏 by BO not listed as permitted; note as question.)
- §8 5: 判例引用落点两处 (Spec 状态区 + Feature Comment 暗号). 8.3 误判豁免暗号 (04.12 索引).
- §九 通过终态 = 四条 Comment + 状态「结构校验通过｜待对齐」.

## 07.05 v5 (2026-09-15) 对齐指南
- N11 原子收口: 回写对齐决议 → Spec 标已冻结 → 回读 frozenPageVersion → N11 最终 Feature Comment with 【OSD-FREEZE｜v1｜FROZEN】 + JSON (specPageId/frozenPageVersion/frozenBy/frozenAt) — 「N12 开发门禁只认此标记」 → 转开发. (S-05: c50009 + c50013 carry it; frozenPageVersion 61.)
- 签收绑定发出时的 Spec 版本; 窗口期内 Spec 变更 = 旧签收失效. Spec 实质变更后原签收只对旧版本有效.

## OS 开发流 Spec v39 (2026-09-10) Owner Kayden (流程), 维护 Kent
- N12 开发建设: 触发「Feature 转入「开发」，且登记的前置依赖均已完成，Spec 状态为「已冻结」」; 完成后触发 「建造单适用区完整，配置回读与测试入口就绪→人工转「验收审计」→N13」.
- C-5 开发 默认 5 工作日 (Kent 校准); C-10 流程 Owner 回应(建设期) 1 工作日, 锚点 = 建造单 Comment 发出→回应 Comment, 每次提问单独起算.
- 全流程规则③ OSD-RETURN/v1 一轮一标记; ④ 已取消 only Kayden/Alden.
- 引用区: 对应建造单 OS 开发流｜建造单 1740439566 (暗号接口契约表 lives there; 04.12 index).

## 04.4.2 v12 (2026-09-15) B6 契约
- active·已发布 2026-09-11 (hf4KKa7CytWxjAFy). op getSupervisor/getDirectReports/isDirectReport; accountId 键; 数据源 cf17995→cf17996; 在职 cf18002 三值; 非 Active 即无效 (Test 上司会 SUPERVISOR_INACTIVE); error codes PROFILE_NOT_FOUND/SUPERVISOR_MISSING/SUPERVISOR_INACTIVE/SUPERVISOR_STATUS_MISSING/INVALID_REQUEST/INTERNAL. 本件不告警; 调用方收到 ok:false 必须告警 nos-ops 或走升级腿 (验收项). 消费者表 lists 离职/Grade only (S-05 not registered — 建造单 row 31).
- 附二: NTP issue security 10876 级别 10344 holders: SSCOS｜HR, SSCOS｜C-Level, cf17995 本人, cf17997, Bot_SSC → Backend Operations / builder account cannot read profiles (建造单 row 10: Kent 档案 Talent Status 本侧读不到).

## Notify 契约 v13 (2026-09-18)
- recipients type user/group/channel; threadTs (new, 恰好一个 channel, 无 approval); approval object §9.1 (approverAccountId, flowKey = 流程稳定名称 not F 编号, round, idempotencyKey, approverFieldId, rejectNotice, actions[decision,label,style,transition,kind,modal,writes,requiresReason(未实现)]).
- §9.4 主锁 = transition 可用性; 副锁 marker 未实现; 轮次防过期 🔲. (建造单 row 30: 原地转换使主锁失效.)
- §9.14 still says 「平台实建未上线」 (contradiction with 04.4.1 v5 已并入生产 2026-08-21 — 建造单 row 25).
- user-DM 解析: cf17995 → cf18051 Work Email → users.lookupByEmail.

## 04.4.4 v4 (2026-09-21 09:50Z) 协作 Thread — not used by S-05. inactive, 零真跑. STATUS BERUBAH: 已验收 (Alden NSE-1143 c50273, 2026-09-21); 04.4 §十一 状态 sudah diubah 「可用」 oleh 建设者. (was: v1 2026-09-19, 未验收)

## 04.5.1 v19 (2026-09-05) Spec 模板 — E 表「已改道｜本流程不使用｜理由」 example; 页尾「对应建造单：设计期填“待建设期建立”；仅在 Spec 已冻结并进入开发后由 BO 建立并回填实链」.

## 04.8 v20→v21 diff (2026-09-21 03:59Z, Kent): only 员工 row — 入职侧转态来源 = S-02 (Kayden c50248). Nothing on S-05. 纪律处分记录 row unchanged.
## 建造单 2096463922: still v33 (2026-09-20 14:55Z). v33 msg: 消费 Kayden c50244 两项裁决 (附表 Registry 行; 附表 N28 行; 区二 转换表 id 11 允许执行者; 第八区 守护登记). v32: WFH 规章行 订正「本侧无读取权限」.
## 04.12 v5 (2026-09-18) Owner Kent: 7 核心 marker 本体 (OSD-CUT-DECISION/SPECS-JSON/CUT-SPAWN/FREEZE/PRECEDENT/EXEMPT/RETURN) 必含字段; OSD-FREEZE fields specPageId/frozenPageVersion/frozenBy/frozenAt; label osd-cut-{n}/osd-batch-{n}; 业务流运行时 marker (nos-…) 不在本页 (建造单 暗号接口契约表 lives in S-05 建造单 line 101).
## 04.4.3 v6 (2026-09-14, TIDAK berubah) 身份件: halaman masih tulis 在建·影子·inactive v0Ta9NW64VJiVQqd — **SUDAH STALE** terhadap 04.9 v106 / 04.9.1 v19 (active·已发布 sejak 2026-09-21 07:52Z). Owner halaman: Alden; 消费者 离职 N3 / Grade N3 (仅通道二); identityOk = sigValid && isDirectReport && clicker==token slackUserId; 调用方 identityOk:false → 阻止 + chat.postMessage 私信回告; mustAlert → 告警 nos-ops.
## 04.9.1 v19 (2026-09-21 07:52Z) — was v17 (2026-09-19): Notify active (被调用: 请假 9/离职 7/Grade 7/调薪 3/改进 1 — no S-05); Slack Approval active v31 50 节点 (分派钩子 known: offboard-n2/grade-n2/align-n10 — no disciplinary-n03); Error Handler active; Policy Engine active; Collaboration Thread inactive; B6 active·已发布 (被调用 no S-05); 身份件 **v19: active·已发布** (versionId＝activeVersionId `616bbd91-5cd7-4c10-bcc4-ae9052592253`, 5 节点, 件名已去「DO NOT ACTIVATE · shadow」后缀; 真实链四例已验: 真上级 identityOk / 非上级按业务拒·不告警 / 档案查不到与档案重复两种均 fail-closed 且 mustAlert). v17 的 「模式九批次已上线而本件未随批发布，是否漏带待 Alden 确认」 **sudah dihapus di v19** — kalimat itu sudah tidak berlaku.
## HR｜盘点与切分 v38 (2026-09-08) 已裁决 Kayden 2026-08-23 auditedVersion 29 (c48783 approvedPageVersion 33 — page metadata says auditedVersion 29; later versions 34/35 N5 修正留痕 c49113/c49116). §三 S-05 row: 链中; 人为入口; 覆盖 P-09/P-10/P-11; Project 已登记 SSCSD 主单 + HR 子单; D-04 决议; 2026-08-31 N5 修正 S-19→S-05 入边 measure 『S-19 绩效评估周期结束，评估结论为不达标』. §五 S-05 High, 前置 无, 同批 纪律绩效改进批 (S-06 Low/S-07 High/S-15 High). D-04 references 《Nexmax WFH工作规章制度（正式版）》 pageId 1679032336 (建造单 row 16: 本侧无读取权限).
## OSD-116 new comments (total now 155):
- c50255 Kent 2026-09-21 11:07 +0700 【Unblock + Route → Bambang】: Registry Option C (read-port service-account only); N28 Direction 2 (permission to HR Ops & Data role group + guard workflow DM); 联合评审结果 (N25) → BO side, register as new; PROCESS ASK: submit N25 + sub-ticket fields via 04.10 Task three-cell request (register-before-build §5); FYI 04.8 v21 S-02.
- c50256 Kent → Alden: Mode-5 race ordering 「void must move the master to Cancelled before, or atomically with, cancelling the remaining sub-tickets」 for endorsement.
- c50071/c50073 Kent handoff (2026-09-16): frozen Spec v61; link type real name `Trigger` id 10075; build in parallel; leave traces on OSD-116; "pre-build alignment 7 categories in the skill" (.claude/skills/build — NOT in this repo; only nosm-sync-check exists).
- c50198 Kent progress check; c50213 Bambang built base framework (Issue Type 14357, Workflow 五态 11 transitions, SSCSD-411); c50227 Kent unblock 8 points; c50228 Kent→Kayden 裁决请求; c50233 Bambang; c50234 Kent; c50237 Bambang field list (48 fields); c50238 Kent routing 业务歧义→Felix; c50244 Kayden ruling; c50249 Bambang addendum; c50250 Bambang → Felix 4 items.
## Spec S-05 v62 slices 1–3 read: ⓪ §一–十七 (目的/入口/资料/HR审核(已改道不适用; 缺位升级; 回避规则)/打回/分流/Show Cause/Warning/有效期内再犯/PIP/严重违纪/Formal Action/知会规则/SLA/终态(Final Outcome 9 类; 取消原因 4 值)/历史记录/观测); 版本表 v1–v27; ①状态区; ②节点表 N01,N03,N04,N05,N06,N07,N08,N09,N10,N12,N13,N25,N26,N27,N14,N15,N16,N17,N20,N21,N22,N23,N24,N28(partial). Break numbers: N02/N11/N18/N19 断号.

## Spec S-05 v62 — slices 4–6 read (A 表 34 rows; B 表 6 roles; C 表 C-1..C-20 (no C-13/15/17/18); D 表 D-1..D-17; E 表 5 states (no 已改道 row); 投影图 + 标注自检; ⑤引用区 incl 需技术确认项 1–10, 设计判断依据留痕; 页尾 证据段 + 维护说明).
- Key: N28 row (末尾): 「HR Ops & Data在「处理中」状态执行中止（04.3§六既有「Project Owner中止」出口，不新造转态）｜对外status→已取消；不登记Final Outcome；已产生的过程记录保留」.
- A 表 「取消原因」 4 values; 「纪律处分记录状态」 row exists in A 表 (N13, 系统维护) — note: F-003 correction says it's the 档案卡 status column (04.8 §三), not a Jira field.
- D-7/D-14/D-15/D-17 → 部门 Collab 频道; D-1/D-13/D-16 → HR 内部固定频道 「具体ID见建造单」.
- E 表: no 「已改道｜本流程不使用」 row (04.5 §七 item 2/15 require it for 无分诊门 flows; ⓪ §四 says 已改道 不适用) — 建造单 row 18 question.
- 需技术确认项 7: N07 确认重复→已取消 no 04.3 §六 exit (IN-041) — findings F-004.
- 引用区 「对应建造单：待建设期由 BO 依 04.5.2 建立并回填链接（当前无对应页面…）」 — not backfilled though 建造单 2096463922 exists.
## Repo docs read: working-rules.md (owner standing instruction 2026-09-20: obey all rules; facts only; read all sources fully; findings reported to owner only; no external writes without instruction); findings.md F-001 (04.11 missing from 04 §六 map), F-002 (WFH 404 visibility), F-003 (c50237 omissions; corrected: only 联合评审结果), F-004 (04.3 §六 no row for built `Cancel as Duplicate` id 9), F-005 (04.3 §六 lacks HR role-group abort executor per c50244); sync-check history.

## 建造单 v33 slices 1–3 read (页首: 对应 Spec v61 + v62 核对段; 已实读规范源清单 2026-09-18/19/20; 附表 33 rows; 对照表 部门→Team Project (13 值; GENERAL SERVICES/NEXMAX 🔲) + 部门→Collab 频道 7 IDs + sscos-hr; 暗号接口契约表 8 markers `nos-s05-*` 拟定·未建; 本轮实建与回读 2026-09-18 (Issue Type 14357; Workflow; schemes 19812/12991 未核); 踩坑 4; 偏差登记 (建设用账号; 转态权限本批未配置; S-05→离职 缺口「过渡处理方式」未登记 — 需 Kent+Felix 业务口径); 建设备注 (主单载体; 技术签附注; 跨流程 link Felix c50045; 审批卡; B6 — 「Spec 仅写缺位由 HR Ops & Data 承接，未定义哪些码计为缺位」 须白话对齐 Felix; 07.06.1 命中条目 A2/A3/A6/A4/A8/C1/E11/E16/E9/D3/D7; 测试 04.5.3; 权限受限).
- Repo draft file docs/drafts/2026-09-20-osd-116-felix-spec-questions.md = c50250 body + verification table (SENT 2026-09-21 06:26 WIB).

## 建造单 v33 slices 4–5 read (区一 24 node rows all 待办/阻塞 mapping to 附表; 区二 5 statuses/11 transitions, id 9 `Cancel as Duplicate`, id 11 允许执行者 HR role-group per c50244, 转态权限 本批未配置; 区三–五 待办; 区六 platform pieces (Notify/审批卡/B6/Policy/Error Handler 可用; 身份件/协作 Thread 在建/不用); 区七 空; 区八 tests SSCSD-411 + NTP-187 自验 only; 区九 空). 04.9 v103 main fully read (§一 三位一体; §四 Data Table 建表权 平台 Owner; no S-05 分册; B6 被调用 lacks S-05).

## OSD-116 comments 0–84 (c48791–c49707) fully read (146,962 chars). Additional facts from chars 88000–end:
- c49399/49400 round-13 machine (Spec v42): B-1(b)×9, B-2, B-4, T-1×2, T-2, T-3, T-4, T-5 — all 待人工裁决, no machine return.
- c49403 Kayden B RETURN r4 (v42): 4 必改 (N14 时限 1 工作日; N08/N15 改真正自动化 不开子单; N14 不成立不回 N07 → 「重定处置工具」分流 N08/N12/N15; 处分类通知 D-3/5/6/8/9/10/12 改私信, Collab 频道只留 D-7/D-14/D-15/D-17) + 5 提点. 未决风险 ①04.11 无登记行 ②04.1 仅 HR/BO/FIN ③离职 入口缺口 Kent ④N07 确认重复→已取消 04.3 §六无出口 (IN-041) ⑤机器 B-1(b) 重复 (IN-035).
- c49411/49412 round-14 machine (v44). c49444 Kayden B RETURN r5 (v44): 回避规则 (HR 成员→Head of HR; Head of HR→COO/CEO); 「案件失效」中止出口 = N28 (取消原因新增枚举「员工已离职／案件失效」; 用 04.3 §六 「Project Owner 中止」出口); 渲染图重插; 审计记录更正 (v19 行 与 页尾 与 c49403 相反).
- c49461/49462 round-15 machine (v51). c49471 Kayden B RETURN r6 (v51): D-3/D-6/D-8 加邮箱保底; N28 模块 自动化→工作流; 版本表 v20 行. 未决风险 split: 卡建设 ⓐ 其余部门无 Team Project (Kayden 裁定 Kent 建) ⓑ 主单 处理中→已取消 无既有出口 (04.0 §三/04.3 §六; 待 Kayden 批 → Alden 修 04.3 §六); 不卡 ⓒ 04.11 8 频道 ⓓ 离职入口 (04.5 §八 带缺口, 只卡解雇路径上线) ⓔ 机器重复标注. c49472 Kent noted.
- c49473/49474 machine (v52, titled 第15轮 but is r16). c49481 Kayden B PASS (v52) — 豁免留痕: 页尾 「第 15 轮业务签 Comment 49461」 应为 49471, 纯引用错字, 对齐阶段由 Felix 改, 不触发基线失效. c49482 Kayden→Alden 三条卡建设 (Team Project; 处理中→已取消 出口 04.3 §六修订意见; 04.11 登记 8 频道).
- c49483 Zq S-19→S-05 衔接调整 (携带字段 +「建议处置工具」; 来自 S-19 的事件跳过直属上级 Slack 卡确认). c49561 Felix 确认 (原 N02 断号). c49612 Kayden 裁定 同上. c49618 Felix: 已改, 补流程动作 转回设计 再重提.
- c49507 Kent NSE-1125; c49545 Kent 6 Team Projects built (CRM 13297/FOZ 13298/INZ9 13299/MKT 13300/WP 13301/XLP 13302; Workflow Scheme 13093; Sub-ticket 14316; Members 空); c49558 Kayden Marketing 归 CRM (MKT 保留不启用); c49559 Kent 归档 MKT; c49600 Kent INZ9 归档 (CRM function), 04.1 v38, 4 组待建, WealthPlus NTP 无值; c49605 Kent 4 组已建 128 人, 升级 WealthPlus 存废 + Lead; c49606 Kayden: W+ 独立部门 挂 Expansion engine; Nexxpay 并入 CRM (NXP 直属 Ethan, W+ Alex); c49705–49707 Kayden/Kent: Nexxpay = CRM division 下 function.
- c49619/49620 machine 第10轮 (v55; SIXQ-14 in 技术区). c49696 Alden T RETURN r1 (v55) — full 6-row table T-1..T-6 (T-6 复用决策 最重: B6 实物 只 getSupervisor/getDirectReports/isDirectReport, cf17997 禁用, SUPERVISOR_MISSING 硬阻断; 无部门/岗位解析器); 4 退回要求 (角色缺位数据源; N09 邮件收信 新平台件; N07 审批交互 超模式九 v5 → 需技术确认项第 10 条; 依赖清单 三列表 9 rows); 建设前必闭合: Registry N5 裁决; 岗位受控清单标准化; 模式九扩展; 邮件收信件; 主单类型+2 RT 人工建. 探针: 7 Collab 频道 + 机器人; N09 附件回贴. HR 固定频道 = sscos-hr C0BHL8AE68G (不用 c49247 dept-hr-internal). 机器包缺陷 转 Kent.

## OSD-3 all 39 comments read (c48075–c49642, 49,632 chars):
- c48075 Kayden 流程说明; c48333 Skill v1.0 Project Instruction for 盘点与切分 (07.01 v34 源); c48352 Felix 提交 r1 (no version) → c48365 machine r1 退回 COM-01; c48367 r2 (v7) → c48368 machine r2 退回 8 (COM-02/05, CON-03/04/05/06, SELF-01/02), DUP-03 待人工; c48380 CUT-GATE-v1 更正 CON-05 → 待人工裁决; 07.01 Skill v1.1 漂移通知; c48403 07.01 v41/07.01.1 v11 优先级表 6 列; c48452 r3 (v12) → c48455 入口失败 (页已 v13) + 预检 CON-02 同批组字符串 / SELF-02 D-10 链位; c48459 r4 (v14) → c48469 machine r4 退回 4 (COM-05/SELF-01 S-11/S-18/S-22; CON-05 组合 key HR＋BO/HR＋FIN; SELF-02 S-17 链末); c48476 r5 (v16) → c48480 machine PASS, 4 待人工 (CON-04/05/06, DUP-03/04); c48524 Kayden 指南更新 (提交 Comment 七字段模板; 提交后冻结页; 枚举对照表); c48643 r6 (v24, 2026-08-20 会议后 25→16 候选) → c48665 machine 退回 4 (S-07 覆盖行/前置/同批组; P-09 双覆盖; S-02/S-07 链位) + c48666 Kayden S-06 Priority / S-11 并入 S-02; c48693 r7 (v26, 15 候选) → c48737 machine PASS r8 (3 待人工); c48748 Kayden 人工退回 r8 (S-03/S-07 「不 spawn Feature」标注; 补登 Grade Spec 1731428411 → S-16; 新增 3 候选 制度规划/功劳记录/目标与绩效闭环; IN-014 N6 缺口); c48756 r9 (v29, 19 候选) → c48757 machine PASS r10 (CON-04/05 5 Project 候选/DUP-03 待人工); c48764 Kayden N5 PASS (v29→30; S-01 RX 复用; S-02 ONB; S-17 COE; S-18 MER; S-19 GPM; 04.1 v32; 转态暂不执行 待 n8n active; S-03/S-07/S-16 空白 Feature 由 Kayden 手动取消 IN-014 过渡); c48775 SPAWN HALTED (无 DECISION marker); c48777 DECISION PASS v30; c48778 HALTED (D-01/D-10 未处置); c48779–48782 Kent/Kayden; c48783 DECISION PASS v33 (取代 48777; 清理 22 处 「待正式Jira N5确认」; v31 表格修复); c48784 HALTED (D-02..D-09 结论列无结案标记); c48787/c48790 SPECS-JSON DERIVED (v33; 48790 omits S-03/S-07/S-16 复用); c48798 SPAWN DONE 16 Features (S-05 → OSD-116, priority High, 前置 无, 同批 纪律绩效改进批; S-06 OSD-123; S-15 OSD-128; S-19 OSD-131; S-14 OSD-127); c48800 Kent CUT-GATE 放行标准 7 条 + OSD-118 junk 待取消; c49113 Kayden N5 修正 (S-19→S-05 边; S-05 链首→链中; v33→v34); c49116 补充 (S-05 第五节 依据 链中, 前置 维持 无; v35); c49642 approvedPageVersion v35→v38 (S-19 驱动源 月度; S-14 并入 S-19, OSD-127 取消; 绩效闭环批 改无).
- S-05 切分审计通过证据 = c48783 (DECISION PASS v33) + c48798 (SPAWN DONE mapping S-05→OSD-116). Current approvedPageVersion v38 (c49642). S-05 row itself unchanged since c49116 per c49642 「切分表其余行…未变」.

## READING SWEEP COMPLETE 2026-09-21. Nothing sent/edited anywhere. Draft (e) in prework/s05_e_draft.md NOT sent.

## OSD-116 re-check 2026-09-21 ~12:00 WIB: total 157 (was 155). New:
- c50257 Kent→Kayden 2026-09-21 11:08 (+07): Ack c50244 两项裁决 — 处分记录=选 C (读取口 只服务账号/指定节点/无人工浏览; 「已让 Bambang 按 N5 建库」; 04.1/04.8 转正式 归 Kayden 侧); N28=方向 2 (转态权限 HR Ops & Data 角色组 + 守护件; 方向 1 上线后第二版; Mode-5 抢跑约束 已转 Alden c50256). Kent 盯 N5 建库 + 04.1/04.8 转正式 到闭环.
- c50259 Bambang→Kent 2026-09-21 11:15 (+07): 「baik brother」 (user's own reply).
- No reply yet from Felix (c50250), Alden (c50256), or Kayden-side 04.1/04.8 转正式.

## #nos-bo (C0BRSTNNY4A) read 2026-09-21: 26 top-level msgs (2026-08-21 → 2026-09-19), pagination says no more. Threads read: 7 of 8 (归口表 thread fetched separately).
- 2026-09-19 18:36 Kayden 【制度更新通告】三步判断 (04.1 §5.1: ①另一方在等? ②=管道对象实例? ③=受控清单变更→GOV 维护单) + 契约锚点 正式概念 (主单 or 实体卡; C 表新增 4 列 只对新建/修订重审 Spec 强制, 存量不追溯) + 维护单扩写. Pages: 04.0 v26 / 04.1 v46 / 04.2 v40 / 04.3 v33 / 04.5 v79 / 07.03 v58 / 07.03.1 v21 (matches what I read). Known cost: Pipeline 流程 不上 JSM board.
- 2026-09-19 13:11 Kent 提议 07.03 §七 加 RT 双语命名 (引 S-05 两个 RT 名待补). Reply Kayden: 已补 07.03 v57 (后 v58) — 「S-05 那两个待补的名字请按这条补齐」.
- 2026-09-18 11:06 Kent 三流程复盘报告 (Canvas F0C2VSAATHA). Thread: Kayden 逐条 (07.07 验收门 方案 A Alden Owner NSE-1147; 权责矩阵 落 04.10 §二; 承重不变量 收拢 + 「改动分级」新增 (判据改动才重钉基线, 非判据改动不停机 → 07.04 §10.1 + 04.12 加行, Kent 起草); 上产时限 待观察; Kayden 自我约束: 影响机器判据的裁决当天回写页面). Kent 定案 + Kayden 回. 
- 2026-09-16 16:10 Kent 【分享】开工前 7 类扫描 + 5 纪律; 「已登进 build skill, Claude 会自动照跑」 (NOTE: repo .claude/skills has only nosm-sync-check — no build skill in this repo).
- 2026-09-16 14:04 Kayden 已定 A (Pipeline 锚点); pages 04.0 v23/04.1 v43/04.2 v37/04.3 v33/04.5 v76; Alden 改 04.4 模式四/五, 04.7 「载体」字段, 04.6 §四. Thread (8 replies): Kent 建设视角 (仪表盘/SLA SSOT C 表 vs store/假期表前置); Alden 倾向 A + 三件; Kayden 定 A; 更正 第三问 → GOV 维护单 (OSD-119 c50053); Alden 认领 → 04.4 v26 / 04.6 v20 / 04.7 v43 done.
- 2026-09-15 13:48 Kent 标准缺口回报 07.06.1 D1 触发词 (风险两尺). Alden reply: 方向认, 「或」不「与」; 已改 07.06.1 v30 / 04.6 v19 / 04.5.3 v13.
- 2026-09-14 19:47 Kent → Alden 04.5.2 待办/阻塞表 (A5). Alden: 同意, 页首附表 不计入九区, 5 列 事项｜依赖谁｜解除判据｜不做的后果｜状态; Kent 落 04.5.2 v11 + 07.06 v30; Kayden 落 04.5 v74 §2.1.
- 2026-09-14 18:02 Kayden 制度讨论 Pipeline 主单 (上半+下半).
- 2026-09-08 13:38 Sinyee 标准缺口回报 测试档案 (04.5.3 vs 04.8 矛盾; C1 Talent Status `Test`; B6 判据). Alden reply: NSE-1143 c49586 — C1 采; 份数 主体一份 上级用真人; B6 判据本轮不动; 04.5.3/04.8 Alden 自改; Kent 两项 (Test 值 04.10 §五; 协调 HR 建测试档案); Departing 已移 Lifecycle Stage (c48632).
- 2026-09-05 15:50 SSCOS-Bot SSCSD-367 AL 自动拒绝 bug (Kayden→Alden 检查).
- 2026-09-04 12:04 主脑(代 Kayden) 归口表通告 (07 §三).
- Older: bot join/test/离职提交 SSCSD-313 (Geri 2026-08-28), member joins 2026-08-21.
- No message in #nos-bo mentions S-05 建造/Registry/N28 directly except Kent 09-19 RT 命名 提议 and Kayden reply. No 标准缺口回报 for S-05 has been posted by BO (consistent with my draft A not sent).

---

# VERSION SWEEP 2026-09-21 ~18:00 WIB (11:00Z) — "update semua ke versi terbaru"

Metode: CQL `space = NOSM AND type = page AND lastmodified >= "2026-09-20 00:00"` atas SELURUH space NOSM
(bukan hanya daftar id yang sudah kita punya), lalu `listConfluenceContentVersions` + `diffConfluenceContentVersions`
per halaman yang bergerak. Jadi hasil ini menutup juga halaman yang belum pernah kita catat.

CQL mengembalikan **18 halaman** yang bergerak sejak 2026-09-20. **7 di antaranya ada di daftar sumber kita.**
11 sisanya milik alur lain (招聘执行 Spec, 新人90天 Spec, Grade 建造单, 员工离职 建造单, OS 开发流 建造单,
04.9.3, 04.9.5, xLoop×2, AMS 归档) — bukan sumber S-05.

## A. Tabel versi (tercatat di notes → live sekarang)

| Halaman | Di notes | Live | Keterangan |
|---|---|---|---|
| 07.06.1 | v33 | **v34** (07:11Z) | msg: 「E16 探针订正；E6 订正；新增 C9」 |
| 04.9 | v103 | **v106** (10:42Z) | v104/v105 msg: 索引表新增身份件一行 → 身份件行状态改 active·已发布 |
| 04.4.4 | v1 | **v4** (09:50Z) | 已验收 Alden c50273 |
| 04.4 | v31 | **v33** (≈10:00Z) | hanya baris 协作 Thread → 可用 |
| 04.9.1 | v17 | **v19** (07:52Z) | 身份件 → active·已发布 |
| 04.7 | v45 | **v46** (06:56Z) | **tidak menyentuh baris S-05** (lihat koreksi di bawah) |
| 04.8 | v20 | **v21** (03:59Z) | sudah dicatat sebelumnya; tidak ada perubahan baru |

Tidak berubah (dikonfirmasi tidak muncul di hasil CQL): 07 v28 · 07.06 v30 · 04 v25 · 04.0 v26 · 04.1 v46 ·
04.2 v40 · 04.3 v33 · 04.4.1 v13 · 04.4.2 v12 · 04.4.3 v6 · 04.5 v79 · 04.5.1 v19 · 04.5.2 v11 · 04.5.3 v13 ·
04.6 v20 · 04.10 v19 · 04.11 v2 · 04.12 v5 · 07.03 v58 · 07.04 v27 · 07.05 v5 · Notify 契约 v13 ·
OS 开发流 Spec v39 · HR 盘点与切分 v38 · Spec S-05 v62 · 建造单 v33 (2026-09-20 21:55 WIB).

## B. KOREKSI atas laporan saya sebelumnya

Saya sebelumnya bilang perubahan 04.7 v46 「menyentuh baris RT-HR-DISCIPLINARY-SUBMIT milik S-05,
blocker 建造单 row 5」. **Itu salah.** Pesan versi v46 menyebut 「SUBMIT 行」 yang dimaksud adalah
**RT-HR-RECRUITMENT-SUBMIT** (S-01 招聘执行), bukan RT-HR-DISCIPLINARY-SUBMIT.
Bukti: diff v45→v46 = 2 tambahan / 1 hapusan, seluruhnya di baris RECRUITMENT
(Replacement 比对 收窄 jadi hanya Position; C-12/C-16/C-18/C-21/C-22/C-23 SLA direvisi)
plus satu baris baru **RT-HR-RECRUITMENT-OFFERWITHDRAW** (N47/N49).
Kedua baris S-05 (RT-HR-DISCIPLINARY-SUBMIT dan RT-HR-DISCIPLINARY-EVENT) muncul di diff hanya
sebagai baris konteks — **tidak berubah satu huruf pun**. Status keduanya tetap 「候选」.

## C. Isi perubahan yang relevan untuk S-05

### C.1 07.06.1 v34 — tiga perubahan, ketiganya kena kita

**(1) C9 BARU｜Slack 三秒窗口：响应动作之前不要排 Code 节点** — juga masuk ke 主题速查表 baris
「发通知、发邮件、发 Slack」 yang sekarang jadi C1–C6、**C9**.
Isi verbatim inti: 「Slack 给的开窗令牌只活 3 秒，而一次执行里**第一个** Code 节点要多花约 2 秒；
响应动作之前排了 Code 节点，这两秒就落在用户的等待里，表单根本弹不出来。」
Cara hindar: 「有硬性回应时限的路径（Slack 开表单、slash 回应）上，响应动作之前**不放任何 Code 节点**
——验签用 Set 加原生 Crypto 节点，响应载荷用 Set 拼；慢活与全部 Code 节点挪到响应之后，
成品用 views.update 之类的二次动作补上。**只换掉验签那一段不够**：紧跟的下一个 Code 节点会接任「第一个」，
那两秒原样搬家。」 验收: startTime 响应节点 − 触发节点 dalam orde ratusan ms, dan 回包 ok=true.
→ **Relevansi S-05**: N03 入口一 adalah Slack 表单 (04.7 baris RT-HR-DISCIPLINARY-SUBMIT: 「载体为Slack表单」),
lewat 分派钩子 `disciplinary-n03` di Slack Approval. Jadi C9 mengikat desain N03 sebelum dibangun.

**(2) E6 DIBALIK TOTAL.** v33: 「test_workflow 的 dry-run 会 pin 掉 HTTP 请求」 (dry-run tidak kirim request nyata).
v34: 「**test\_workflow 不会替你 pin 掉带凭据的节点，它会真发**」 — 「工具说明写着触发节点、带凭据的节点与
HTTP Request 节点会被自动 pin，本实例实测不是——只有你显式传了 pinData 的那些节点被 pin，其余照常真读真写。
拿它当「安全干测」，会真建单、真发消息。」
Cara hindar: nonaktifkan eksplisit node yang menulis/mengirim, atau beri pinData eksplisit; kalau bisa ada
efek samping eksternal → perlakukan sebagai 「改动后的首次真发」 (04.5.3), 受控时段. 验收: baca balik objek
target + cek `pinData` eksekusi (kosong = tidak ada node yang diisolasi).

**(3) E16 DIKOREKSI.** Sekarang eksplisit **melarang** pakai `/rest/api/3/mypermissions` (BROWSE_PROJECTS)
sebagai pengganti probe: 「项目级权限回 true 时，单据级 issue security 仍可能把每一张单都挡掉，
JQL 照样恒回空集，而探针会报「看得见」。」 Probe harus query **satu tiket yang diketahui ada**.
Tambahan baru: 「探针查的那张已知存在的单是**承重对象**——被删或改了 key，闸会每天报错，
须在建造单登记它的用途。」
→ E16 ada di daftar 07.06.1 命中条目 建造单 kita (A2/A3/A6/A4/A8/C1/E11/E16/E9/D3/D7) ⇒ wajib masuk batch v34.

### C.2 04.9 v106 / 04.9.1 v19 — 身份件 sudah hidup

- Baris index baru di 04.9: **NOS | Platform | Submission Identity Verifier — active·已发布**,
  versionId＝activeVersionId `616bbd91-5cd7-4c10-bcc4-ae9052592253`, 5 节点, Owner 平台, 建设者 Geri,
  被调用 离职 N3 / Grade N3.
- 04.9.1 v19 status block: 「真实链四例已验：真上级 identityOk；非上级按业务拒、不告警；
  档案查不到与档案重复两种均 fail-closed 且 mustAlert」.
  → Ini **mengonfirmasi** koreksi kita atas draft Alden butir (c): non-direct-report = penolakan bisnis,
  bukan `ok:false`+mustAlert. Tapi ada kasus **keempat yang belum kita catat**: 「档案重复」 juga
  fail-closed + mustAlert.
- Catatan di 04.9.1 v17 「节点「Call B6 isDirectReport」注记仍写「B6 未发布」，已过时」 sudah **dihapus** di v19.
- 04.9 v106 juga mencatat Grade N3 (bc84c43a) dan Grade N7/N8/N10 (33a1aad5) sudah memasang
  **probe E16**; pada 2026-09-21 `alwaysOutputData` Fetch NTP Name Map dibalik false→true karena
  「探针关掉的是「NTP 看不见」，关不掉「看得见但那条查询回零条」」 — pola yang sama akan kita butuhkan.
- 04.9 v106 mencatat Grade N2 sudah dirombak mengikuti C9 hari ini (slash leg: Set + Crypto native,
  Code node pertama dipindah ke belakang 响应; exec 15938 = 112ms, 15939 = 13ms), dan
  🔴 「UI 存盘再次剥掉两个 webhook 的 `options.rawBody: true`」 (kambuhan E12) — perlu 逐项点名回读.
- Slack Approval di index 04.9 sudah v31·50 节点 (sebelumnya v30·47) — sesuai catatan kita.
  **分派钩子 yang terdaftar tetap tiga**: offboard-n2 / grade-n2 / align-n10. `disciplinary-n03` **belum ada**
  (ini yang diminta di c50279 add-on (a); masih menunggu jawaban Alden).

### C.3 04.4 v33 / 04.4.4 v4 — 协作 Thread naik jadi 可用

Baris 04.4 §十一 「NOS | Platform | Collaboration Thread」 diubah jadi **可用** (Alden c50273, 2026-09-21);
seluruh narasi tiga ronde koreksi versionId dihapus dari sel itu atas perintah Alden c50273 ⑤
「标准页只放结果」. Tetap `inactive` karena belum ada pemanggil dan channel belum ditetapkan Spec.
04.4.4 naik v1→v4 (halaman kontrak; 已验收, ditambah bagian 「开串腿的标题元素拆分」 per Alden c50273 ④).
**Tidak dipakai S-05.**

## D. Temuan baru dari sweep ini (belum dilaporkan ke siapa pun)

1. **04.4 §十一 baris 身份件 masih tertulis 「在建（影子·shadow，随模式九批次上生产）」** padahal
   04.9 v105 (07:52Z) dan 04.9.1 v19 sudah menyatakan active·已发布. 04.4 sendiri diperbarui ≈10:00Z,
   yaitu **sesudah** itu, jadi bukan sekadar urutan waktu. Owner halaman 04.4: Alden.
2. **04.4.3 v6 (halaman kontrak 身份件) masih tertulis 「在建·影子·inactive」** dan belum bergerak sama sekali.
   Owner: Alden. (04.4.3 bagian 「维护说明」 mensyaratkan pembaruan saat status件 berubah.)
   Keduanya = satu fakta dengan tiga落点 yang tidak sinkron — persis jenis masalah yang 04.5 §五 larang.
