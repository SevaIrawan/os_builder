Update → N20（纪律与绩效改进处置｜N20｜解雇自动开单与交接，ID ToIGnEJmksSPhC85）

节点 "Call Resignation Upstream Trigger Entry" 的 workflowId 占位值已替换为 Geri 登记的离职侧「系统触发入口」实际 ID：qa01CkZBQfx8eLsK（NSE-1137 c50494）。🔲仅此一项参数变更，经 update_workflow 单操作完成，回读确认：active 仍 false、节点数仍 9、其余节点（判定类别映射、连线、凭证配置）逐项比对未变；🔲versionId 由 5e0de1d6 变为 ec07eec2，updatedAt 13:17:43。

🔲未做（刻意暂缓）：员工姓名字段（subjectName）尚未加入 N20 出站调用——对方入口的 Trigger schema 目前仅 5 项，未开该字段槽位，单方加会被对方忽略。已在回复 Geri 的留言中列出对方代码里已引用的字段名（subjectName），待其确认并开放该输入后再补。

🔲dismissalCategoryId 映射未改动：N20 仍只产出 纪律违规→15846、PIP未改善→15847 两值，经核对 Spec v2.9 A 表（04.9.3）确认其余三值（岗位裁撤·组织重组→15848、试用期不通过→15849、其他→15850）非 S-05 判定类型，非本流程缺口。

🔲N20 端到端仍不可 dry-run：对方入口本身仍 inactive、全部写入节点停用，须待其经 Alden 批准发布后才能真跑。

—— Bambang
