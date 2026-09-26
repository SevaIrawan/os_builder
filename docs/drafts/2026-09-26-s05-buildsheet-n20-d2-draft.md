〔插入位置：八、测试与守护记录 · 测试记录 表后〕

【补｜Code 节点语法自检】

规则出处：D2｜n8n Code 节点改完必须做本地语法检查。

规避方式原文：「Code 节点改完，把代码落到本地跑一次 `node --check`；注释单独占一行，不写在代码行尾。」

验收原文：「贴出 `node --check` 通过的输出。」

检查对象：纪律与绩效改进处置｜N20｜解雇自动开单与交接（`ToIGnEJmksSPhC85`），versionId `e713b9cf-93f5-441f-8ce1-63cbb2b4aed0`。

件内 Code 节点共三个：Check Already Triggered、Map Judgment To Dismissal Category、Check Entry Result。

🔲 三个节点的 jsCode 以 `async function` 包裹后分别执行 `node --check`（Node.js v22.22.2），三者输出均为 `exit 0`（依据为建造侧本地命令输出，G-01 无法核验）。

🔲 检索三份 jsCode 原文中的 `//`，仅 Check Entry Result 第 1、2、3 行命中，三行均以 `//` 起首、独占一行（依据同上）。
