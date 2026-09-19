# 04 Anchor Navigation Map（04 锚点导航索引）

> **性质**：指路牌／快速索引，不是规则本体。
> **来源**：Confluence [04｜流程建设与执行治理总纲](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1676804100)（page id `1676804100`，space `NOSM`）。
> **权威使用原则（来自来源页）**：任何人或 AI 不得只读本索引就执行对象级判断。命中某个 04.x 子页后，必须实际打开并读取其当前版本；Jira 是进度事实，Confluence 当前权威页是规则事实。
> **上次同步日期**：2026-09-19（对照来源页 lastModified: Sep 05, 2026）。与来源页不一致时，以 Confluence 当前版本为准，本文件视为过期。

---

## 一、按「当前动作」找该先读什么

| 当前动作 | 现阶段主要执行人 | 先读取 |
| --- | --- | --- |
| 盘点、切分与流程设计 | 部门 HOD／流程 Owner＋协助 AI | 04 第二、三节＋04.5＋07.01／07.02 |
| 三个审计 Gate 与对齐 | 切分审计／验收审计：Kayden 或 Alden（OR）；结构审计：Kayden＋Alden 双签（AND）；对齐：流程 Owner 及相关 HOD／管理层 | 04 第二节 Gate＋Spec／建造单＋对应 Jira 证据 |
| 平台建设 | Alden／BO 建设者＋协助 AI | 04 第二、四、五节＋04.5／04.6／07.04 |
| 验收与上线 | 验收裁决：Kayden 或 Alden；上线：流程 Owner＋BO 建造 Owner | 04 第二、三、五节＋Spec＋建造单＋测试证据 |

---

## 二、04.x 子页地图：哪条规则住哪一页

| 子页 | 唯一职责 | Owner | 当前状态 |
| --- | --- | --- | --- |
| [04.0｜流程／执行层词汇表](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1676640265) | 术语与枚举值的唯一权威定义 | Kayden | 生效 |
| [04.1｜Project 类型与开设判定](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1676738564) | Project 判定、命名、Key 与实例登记 | Kayden | 生效 |
| [04.2｜单据体系](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1676607500) | 主单、子单、维护单等 Issue Type 的语义、触发与阻塞 | Kayden | 生效 |
| [04.3｜状态词汇表与 Workflow 配置规范](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1676771343) | 状态语义、流程形状与 Workflow 逻辑标准 | Kayden | 生效 |
| [04.4｜自动化配置模式库](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1677066244) | 跨部门／跨系统自动化模式与命名 | Alden | 生效（模式持续扩充） |
| [04.4.1｜模式九：Slack 审批卡回调（共享地基）](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1729888419) | Slack 审批卡回调模式的配置与验收规则（候选新增章节，待 Alden 核收并入 04.4 正文） | Alden | 候选模式／待并入 04.4 |
| [04.5｜流程 Spec 与建造单规范](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1678573617) | 双文档架构、Schema、交接与验收 | Kayden | 生效 |
| [04.5.1｜流程 Spec 模板](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1685979182) | Spec 可复制模板与填写示例 | Kayden | 生效 |
| [04.5.2｜建造单模板](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1729626775) | 建造单九区模板与字段结构 | Alden | 生效 |
| [04.5.3｜Sandbox 与测试策略](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1729626578) | 测试环境、数据与通过判据 | Alden | 生效 |
| [04.6｜n8n 使用规范与环境需求](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1690927120) | n8n 环境、部署、权限与使用治理 | Alden | 草拟（待平台侧收口） |
| [04.7｜Router SSOT](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1691254793) | Request Type／Route 实例与生命周期 | Alden | 生效 |
| [04.8｜Registry SSOT](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1690140756) | 持续实体 Owner、Project 与状态结构 | Alden | 草拟 |
| [04.9｜n8n Workflow SSOT](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1693089805) | workflow 身份、Owner、消费关系与证据 | Alden | 生效 |
| [04.10｜Jira 共享配置治理](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1738735636) | 共享对象实例、变更权限、影响与证据 | Kent | 生效 v1 |

**边界铁律**：04.0 管词义；04.1–04.6 管判定与配置方法；04.7–04.9、04.10 管对应实例；04 首页管跨页顺序、Owner、当前状态和停止条件。任何页面不得复制另一个 SSOT 的值。

---

## 三、登记集：新事件必须写入哪个 SSOT

| 触发对象／事件 | 权威落点 | 触发时点 |
| --- | --- | --- |
| 新流程／执行术语 | [04.0｜词汇表](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1676640265) | 第一次进入 Spec 或规则页前 |
| 新开或登记 Project | [04.1｜Project 类型与开设判定](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1676738564) | Project 创建／消费前 |
| 具体 Request Type／Route | [04.7｜Router SSOT](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1691254793) | 设计可校验时先登记 Candidate；上线时再转正式 |
| 持续存在的实体／档案 | [04.8｜Registry SSOT](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1690140756) | 设计确定实体边界后，最迟上线前 |
| 创建或修改 n8n workflow | [04.9｜n8n Workflow 登记表](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1693089805) | 建成当场、启用之前 |
| 创建、复用或修改 Jira 共享对象 | [04.10｜Jira 共享配置登记表](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1738735636) | 配置建成当场、任何流程启用之前 |

---

## 四、示例：如何用本索引回答「这个请求类型归属哪个 Project」

1. 问题类型是「Request Type → Project 归属」→ 对照上表「二、04.x 子页地图」，命中 **04.7｜Router SSOT**。
2. 实际打开 [04.7](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1691254793) 当前版本（不得只看本索引），在路由表本体逐行核对「请求类型」列与「Owner 部门 Project」列。
3. 例：`RT-HR-LEAVE-REQUEST`（Leave Request · 请假）→ Owner 部门 Project = **HR**（主单固定住 SSCSD，Owner 部门只表示权责归属，不是主单住址）。

---

**维护说明**｜本文件是 04 首页导航表（第一、五、六节）的快照索引，用于加速定位，不替代实际打开来源页。04 首页或任一 04.x 子页的 Owner／状态／职责变化时，需人工重新比对并同步本文件。
