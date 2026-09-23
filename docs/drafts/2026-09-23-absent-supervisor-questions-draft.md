【Spec question → @Felix_HR @Kent】

Interim hand-over

The resignation Spec names @Kent as its flow owner: 「流程 Owner：Kent」.

Felix's comment c49317 (2026-09-03) set the interim path:

「目前人工经通道二提交的方式会保留为建设期的过渡方案」.

The manager submission channel accepts a submission only from the employee's direct supervisor: 「提交人须为离职员工的直属上级」.

Any other submitter is stopped and no case is created: 「阻止提交、不生成主单」.

For the same hand-over, this flow's Spec has HR Ops & Data step in when the supervisor is absent: 「缺位由HR Ops & Data代为补充」.

Until the system entrance is built, who starts the resignation case when 「缺位由HR Ops & Data代为补充」 applies?

A. HR Ops & Data may submit through the manager submission channel for these cases.

B. HR first corrects the employee's record so that a direct supervisor is listed, and that supervisor submits.

C. Another arrangement — please describe.

Which situations count

This flow's Spec already routes the case to HR Ops & Data at submission: 「缺位由 HR Ops & Data 代为受理提交」.

The shared supervisor lookup only reports reporting-line facts and leaves the decision to each flow: 「只回答汇报线事实，不做资格判定」.

It reports these situations separately:

(a) the employee's record lists no direct supervisor

(b) the listed supervisor has been deactivated

(c) the listed supervisor's status is left blank

(d) the employee's own record cannot be found

For this flow, which of (a) to (d) count as 「缺位由HR Ops & Data承接」, and which should go to HR to correct the record first?

Your answers will be copied into the build sheet as given.

—— Bambang
