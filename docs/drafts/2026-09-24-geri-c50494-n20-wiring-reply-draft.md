🔲Reply → @Geri, re c50494/c50495

Done — "Call Resignation Upstream Trigger Entry" now points to `qa01CkZBQfx8eLsK`. 🔲Read back: that is the only change, N20 is still inactive. Understood it stays a no-op (`ok:false`) until it's published through Alden's gate; N20 will only call it for real after that.

🔲On `dismissalCategoryId`: N20's current mapping only produces two of the five cf18199 values — 纪律违规→15846, PIP未改善→15847 — per Kent's original handover contract (c50381), since S-05 is only the first upstream source. 🔲The other three per Spec v2.9 A table (Kent c49103 ②, 04.9.3): 岗位裁撤·组织重组→15848, 试用期不通过→15849, 其他→15850 — none of those are S-05 judgment types, so still not a gap on S-05's side.

🔲On the employee name field: S-05 does carry one. Spec A table field 员工姓名／工号（主体标识）, collected at N01/N03, sourced from NTP, consumed by every downstream node, and it's literally the second segment of the main ticket's title. Your Build Ticket Fields already reads `t.subjectName`, but the Upstream Called trigger doesn't declare it as an input. Once you add `subjectName` there, I'll pass it from N20.

—— Bambang
