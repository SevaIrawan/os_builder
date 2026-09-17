---
name: bo-build
description: Use at the start of, and throughout, any BO 建设／流程建设 task in this repo — before reading a Spec, consuming a 04.7 Candidate, configuring Jira, building or activating an n8n workflow, registering to any SSOT, or reporting a 建设单元 complete. Directs the live read of 07.06｜建设指南「流程建设 Skill（正式原文）」and executes that section as currently written. Carries no rule content of its own.
---

# 流程建设 skill

本文件不是规范源，不承载任何规则内容。

**规范源**：[07.06｜建设指南](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1730347066)（pageId `1730347066`）「流程建设 Skill（正式原文）」一节。

该节原文规定：

> 本节是「流程建设 Skill」的唯一规范源。BO 建设团队使用的 Project Instruction 是受控部署副本，不得反向覆盖本节。每次启动必须先读取本页当前版本执行；副本与本页不一致时，停止执行并报告「部署漂移」。不得把章节号或步骤正文写死在 Project Instruction——按语义标题定位。skill 本身不重复步骤内容，只指挥 AI「先读 07 首页与本页当下版本再动作」——这样步骤更新时 skill 不需要跟着改。

**据此，本 skill 的全部动作是一条**：

用工具打开 `1730347066` 的当下版本，按语义标题定位「流程建设 Skill（正式原文）」与「开发入口的冻结要求」，并按其当下原文逐条执行。该节自身会指向 07 首页、07.06 全文、07.06.1 与 04 系列——按它当下怎么写就怎么读，本文件不复述、不排序、不补充。

本仓库 `CLAUDE.md` §一 是该节的受控部署副本；与来源页不一致时，按上引原文停止执行并报告「部署漂移」。

---

[07｜指南](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1704362028)（`1704362028`）「指南主页面标准骨架」对「正式 Skill 原文」一行规定：*薄 Skill 的正式规范源、适用角色、启动时必读页、停止条件与本阶段结束边界*，且*不得硬编码易漂移章节号或复制权威判据*。以下五项即该要求，一律只放指针，按语义标题定位、读当下版本：

| 项 | 落点 |
| --- | --- |
| 规范源 | 07.06（`1730347066`）「流程建设 Skill（正式原文）」＋「开发入口的冻结要求」 |
| 适用角色 | 同节「流程建设 skill｜适用者：BO 建设团队」 |
| 启动时必读页 | 由上述规范源当下原文指定 |
| 停止条件 | 04（`1676804100`）「强制停止条件」；07.06（`1730347066`）「开发入口的冻结要求」；07.06.1（`1712226375`）「不可逆动作先确认」；07（`1704362028`）「缺口纪律」「标准页读法」 |
| 本阶段结束边界 | 07.06（`1730347066`）「上下游交接契约」 |

全部指针按 pageId。[07｜指南](https://nexmax.atlassian.net/wiki/spaces/NOSM/pages/1704362028)「背景与理由」记载：*曾经在 skill 草稿里写死具体节号（如「04.3 第二节」），页面重排编号后指针全部静默失效，没人发现*。
