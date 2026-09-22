# Findings Log

> **Nature**: internal repo notes. **Not an official document, not a standard, carries no
> authority.** Nothing here may be used as a basis for configuration or decisions; the
> working basis remains whatever the Confluence pages say at the time of use.
>
> **Recording rules**:
> 1. Observations are **recorded here only**. No edits to Confluence pages, no messages
>    to Slack／Jira／anyone, without an explicit instruction from the repo owner.
> 2. These notes **do not determine** whose concern an observation is, where it should
>    be escalated, or whether it should be acted on at all. That is outside this repo's
>    authority.
> 3. Every entry must name the pages **actually opened and read** (pageId +
>    lastModified as seen), so anything recorded can be re-checked later.
> 4. Append-only. Existing entries are not deleted or rewritten; if the situation
>    changes, add a line to the Status field.

---

## F-001 · 2026-09-20 · 04.11 is not listed in page 04's subpage map

**Status**: recorded. Not reported to anyone. Not acted on.

**Status update, 2026-09-21**: **still open, and wider than recorded.** Page 04 (1676804100)
was opened live today at **v25** (unchanged since 2026-09-05) and its §六 table read in full.
It has 15 rows: 04.0 · 04.1 · 04.2 · 04.3 · 04.4 · **04.4.1** · 04.5 · 04.5.1 · 04.5.2 ·
04.5.3 · 04.6 · 04.7 · 04.8 · 04.9 · 04.10. Absent: **04.11, 04.12, 04.4.2, 04.4.3 and
04.4.4** — five subpages, not one. 04.4.1 being present makes the omission of 04.4.2/3/4
a within-family inconsistency rather than a policy of listing only top-level pages.
04.4.4 was created 2026-09-19 and is at v4 today, so the newest of them post-dates 04 v25.
Page 04's own §九 says verbatim: 「子页新增、废弃、改名、权威边界改变或跨页结构重排时，
必须同步核对本页路由与全部指针。一般正文更新无需复制到本页。」 — so a newly created subpage is
exactly the trigger that rule names. Owner of page 04: Kayden Lee. **Still not reported to
anyone; no instruction given.**

**Found while**: running the `nosm-sync-check` skill (verifying the local copies against
their Confluence sources). This observation is **outside that skill's scope** — the skill
only compares the local copy against its source, it does not check consistency between
source pages. Filed here as a record, not as an output of that skill.

**Pages actually opened and read**:

| pageId | Page | lastModified as read |
| --- | --- | --- |
| 1676804100 | 04｜流程建设与执行治理总纲 | Sep 05, 2026 |
| 1730347066 | 07.06｜建设指南 | Sep 15, 2026 |
| 1764524046 | 04.11｜Slack Channel 登记表 | Aug 24, 2026 |
| 1704362028 | 07｜指南 | Sep 14, 2026 |

**Facts recorded**:

1. 07.06 §三 step 3 instructs that notification Channel IDs be checked against
   「04.11｜Slack Channel 登记表（pageId 1764524046，按 Channel ID 查对，频道名仅辅助）」.
2. The 归口表 in 07.06 §三 names 04.11 again, in the row
   「登记表某一行错了（04.7／04.8／04.9／04.11）」.
3. Page 04 §六「04 子页地图」ends at the 04.10 row — **there is no 04.11 row**. Page 04
   §五「登记集」likewise has no trigger row for the「领域→Slack Channel」mapping.
4. Page 04 §九 states:「子页新增、废弃、改名、权威边界改变或跨页结构重排时，必须同步
   核对本页路由与全部指针」. Per its own text 04.11 was created in 2026-08; as of the
   version of 04 that was read (Sep 05, 2026) it does not appear in the routing tables.
5. Page 04.11 notes of itself:「本页为 2026-08 新设，与旧编号 04.11（今 04.10｜Jira
   共享配置登记表与变更治理）无关」— the number 04.11 was previously used by a
   different page.

**Why recorded rather than acted on**:

- No 04.11 row was added to `docs/04-anchor-navigation.md`. That file mirrors page 04's
  tables; adding a row the source does not have would amount to inventing a standard,
  which `CLAUDE.md` §一 forbids outright.
- No Confluence page was touched — all four were read only.
- Nothing was sent to Slack, Jira, or any other party.

**Circumstances at time of recording**: no build work was in progress, so nothing was
blocked by this.

---

**Re-verification, 2026-09-22 — F-001 HOLDS. Every checkable claim matched the live page verbatim.**
Page 04 (1676804100) re-opened live today, lastModified **Sep 05, 2026** (unchanged). Appended per rule 4.

| F-001 claim | Live result |
| --- | --- |
| §六 has 15 rows: 04.0·04.1·04.2·04.3·04.4·**04.4.1**·04.5·04.5.1·04.5.2·04.5.3·04.6·04.7·04.8·04.9·04.10 | **Exactly those 15, in that order.** ✓ |
| 04.11, 04.12, 04.4.2, 04.4.3, 04.4.4 absent | ✓ none appears |
| §五 登记集 has no 「领域→Slack Channel」 trigger row | ✓ §五 has 6 rows (04.0·04.1·04.7·04.8·04.9·04.10); no 04.11, no Slack row |
| §九 quote 「子页新增、废弃、改名、权威边界改变或跨页结构重排时，必须同步核对本页路由与全部指针。一般正文更新无需复制到本页。」 | ✓ **verbatim**, last line of §九 |

**Two things the earlier entry did not have, found by opening the page rather than trusting it.**

1. **It is stronger than recorded.** 04's own 维护说明 makes the same thing an update trigger a second
   time: 「更新触发：…**04 子页**或 AI 停止条件变化｜**每次更新必须检查：04.x 指针**…」. And 04.11 is not
   decorative — 04.5 §七 item 22 makes it a hard structural-audit gate: 「增补区 D 与增补区 C 升级对象中
   指定的每个 Slack 频道，必须在 04.11｜Slack Channel 登记表（pageId 1764524046）中有对应行…**查无对应行
   ＝失败**」. A page that can fail a Gate is absent from both §五 and §六.

2. **But there is a plausible legitimate reason for three of the five, and F-001 never considered it.**
   04.4.2／04.4.3／04.4.4 are all 调用契约 pages for shared components, and **04.4 §十一 is their index** —
   each row there carries a 契约页 column pointing at them. §六's own 边界铁律 ends 「任何页面不得复制另一个
   SSOT 的值」, so listing them again in 04 could be read as duplication. **This is my inference, not
   04's statement** — 04 nowhere says §六 excludes contract pages. Flagged so the entry is not read as
   stronger than it is. No such alternative index exists for **04.11** or **04.12**, and 04.11 is the
   load-bearing one.

**Net**: F-001 stands as an observation, with its scope honestly narrowed for 04.4.2/3/4. Still not
reported to anyone; Owner of 04 is Kayden Lee.

## F-002 · 2026-09-20 · "实测 404" on the build sheet was a visibility artefact, not absence

**Status**: corrected on the build sheet (v32) on the repo owner's explicit instruction.
The row's owner, 解除判据, 不做的后果 and 状态 were left unchanged.

**Found while**: verifying the ~67 verbatim citations in the S-05 建造单 against their
source pages, at the repo owner's request.

**Pages / objects actually opened and read**:

| pageId | Page / object | lastModified as read |
| --- | --- | --- |
| 2096463922 | 纪律与绩效改进处置｜建造单 | v31, 2026-09-20 04:39 UTC (now v32) |
| 1679032336 | 《Nexmax WFH工作规章制度（正式版）》 | not readable — see below |
| 1712226375 | 07.06.1｜开发规则与避坑指南 | Sep 18, 2026 |
| 1751547935 | 04.4.2｜上下级解析 · 调用契约 | Sep 15, 2026 |

**Facts recorded**:

1. The 页首附表 row for the WFH policy document read:「…HR 部门页第七节 D-04 登记
   pageId 1679032336，**实测 404**」, and from that concluded「无可追溯版本」.
2. Re-probed on 2026-09-20 with two execution identities against the same pageId:
   - Atlassian connector (Backend Operations account) → `404 NOT_FOUND`
   - the builder's own account → `403 FORBIDDEN｜"Space is restricted"`
3. Read together, the two returns establish that **the page exists** and lives in a space
   the build side cannot see. The 404 is a false negative of visibility, not evidence of
   absence.
4. This is the failure mode 07.06.1 **E16** describes (「JQL 查出 0 条，分不清『真的没有』
   还是『看不见』」 — a control probe under the same execution identity is required before
   a zero result can be read as "not there"). 04.4.2 附二 records the same trap being hit
   once before, and later corrected with different evidence.
5. The same reasoning had already been applied **correctly** elsewhere in this flow: the
   seven Collab channels' `channel_not_found` was re-probed and judged a private-channel
   blind spot rather than absence (OSD-116 c50233). The WFH row had not been handled the
   same way.

**What the correction does and does not change**: the item itself still stands — Felix
still owes the document's formal location and current version for the Spec 引用区. Only
the stated evidence and the wording「无可追溯版本」 were corrected. Original text was kept
in place, per the page's own 体例 (「上句原文保留不删」).

---

## F-003 · 2026-09-20 · Two 增补区 A rows missing from the field list in OSD-116 c50237

**Status**: raised to Kent as OSD-116 comment c50249 on the repo owner's explicit
instruction. Kayden was deliberately not tagged — routing left to Kent, as he has been
routing throughout.

**Status correction, 2026-09-20 (same day)**: this entry is **wrong on one of the two
rows**, and so is the comment sent from it. 04.8 was **never opened** before writing
either — it is absent from the "pages actually opened and read" table below, which is the
tell. Opened afterwards (v20, 2026-09-15): **04.8 §三 already registers the entity
「纪律处分记录（Warning Record）」 with its status column defined —
「Active → Expired/Reset；Active → 已解除」 — naming S-05 N13／N26／N27 as the trigger
source.** So `纪律处分记录状态` is the archive card's status column, already registered as
SSOT, not a Jira custom field; 04.8 §五 is explicitly for fields *other than* the status
column and is **not** its home. Consequences: (a) c50237 was **right** to leave it out of
a Jira-field list; (b) the genuine omission is **one** row, `联合评审结果`, not two;
(c) point 2 of c50249 is wrong and needs retracting. Title, facts 4 and 5 and the closing
paragraph of this entry are wrong accordingly. Kept unrewritten per rule 4.

**Status update, 2026-09-21 — this finding is now CLOSED on both rows.**

*Row 1, the genuine omission* `联合评审结果` **(N25) — carried through to approval.**
Kent answered in **c50255**: 「联合评审结果 (N25) → your side (BO). It's a task-card field;
per 04.2 a 任务卡 is an execution card, and per 04.10 §1 execution-card / sub-ticket fields
are the Schema-Owner side — Task vs Sub-ticket doesn't change that… Checked 04.10 v19:
no existing 评审 field → not a duplicate → register as new.」 We then filed it as row 8 of
the 04.10 three-cell request (**c50283**), and Kent approved it with the other twelve in
**c50290**: 「13 项全部准予按「新共享对象」登记」. So the row this finding found missing is now
an approved, registered-pending field.

*Row 2, the wrong point about* `纪律处分记录状态` **— already corrected in the comment itself,
no retraction outstanding.** The 2026-09-20 status correction above said 「point 2 of c50249
is wrong and needs retracting」. Re-read live today: **c50249's current body already carries
the corrected text** — 「The other unlisted row is correctly excluded — 纪律处分记录状态 (N13).
It is not a Jira field. It is the archive card's status column, and 04.8 §三 already registers
it…」 The comment's `updated` timestamp (2026-09-20 21:39:28 +07) is later than its `created`
(20:56:08 +07), i.e. it was edited after sending and the fix went in then. **Nothing is owed
to Kent on this row.** Kent's c50255 independently lands on the same reading
(「Disciplinary-record store → Option C … the 04.1 / 04.8 rows get formalized by Kayden's side」).

**Found while**: the same verification pass as F-002.

**Pages / objects actually opened and read**:

| pageId / id | Page / object | version or date as read |
| --- | --- | --- |
| 2036858900 | 纪律与绩效改进处置｜流程 Spec (增补区 A read in full: 34 rows) | v62, Sep 15 2026 |
| 2096463922 | 纪律与绩效改进处置｜建造单 第一区 | v31 |
| 1738735636 | 04.10｜Jira 共享配置登记表 §1 (scope statement) | read earlier this session |
| 1676640265 | 04.0｜流程/执行层词汇表 §二 (档案卡 status column) | v26 |
| OSD-116 c50233 / c50234 / c50237 / c50244 | comments | read 2026-09-20 |

**Facts recorded**:

1. 增补区 A contains exactly **34 rows**. c50237 states「Spec 增补区 A (34 fields)… 35
   items」 (34 + `审批人` from Notify §9.13) — that count is correct.
2. The two tables in c50237 enumerate only **33 items / 46 fields** (7 sub-ticket + 26
   master). The shortfall is exactly two rows.
3. The two absent rows are `联合评审结果` and `纪律处分记录状态`. Both sit on carriers
   outside the master/sub-ticket split Kent set in c50234:
   - `联合评审结果` — collected at N25; 建造单 第一区 records N25's carrier as a 任务卡
     (`Task 10004`) in the HR Team Project.
   - `纪律处分记录状态` — collected at N13; carrier is the 档案卡 in the independent
     Registry, whose 04.1 row is still 候选｜待 N5, and whose N13／N26／N27 are recorded
     as blocked in the 建造单.
4. Consequence: neither is a 04.10 execution-card registration nor an SSCSD/V1 master
   field in the way the split assumed, so neither was filed anywhere.
5. Separately noted for whoever writes the new Registry's rule page: 04.0 §二 states a
   档案卡's status column is not drawn from the §三 vocabulary and is defined by that
   registry's own rule page — so `Active`／`Expired-Reset`／`已解除` is more likely the
   archive card's own status than a custom field.

**Not determined here**: whose concern each is. c50249 asks Kent to confirm the first and
routes the second toward the 04.8 registration that c50244 places on Kayden's side.

---

## F-004 · 2026-09-20 · 04.3 §六 has no row covering the built `Cancel as Duplicate` exit

**Status**: recorded here only. **Not reported to anyone, not added to the 建造单, not
acted on.** No instruction has been given on this one. **Re-verified 2026-09-20 against the live
page (04.3 v33)**: the 转态权限表 row for a master-ticket cancel by service account is
scoped to the post-待子单完成 abort path, and the 待审批 cancel row is reporter-only — so
the built `Cancel as Duplicate` exit is still uncovered. Finding unchanged.

**Found while**: the same verification pass as F-002.

**Pages / objects actually opened and read**:

| pageId / id | Page / object | version or date as read |
| --- | --- | --- |
| 1676771343 | 04.3｜状态词汇表与 Workflow 配置规范 (§二, §五, §六, §7.1) | Sep 16, 2026 |
| 2096463922 | 纪律与绩效改进处置｜建造单 第二区 + full-text greps | v31 |
| OSD-116 c49324 / c49359 / c49372 / c49403 / c49444 / c49471 / c49481 / c49731 / c49740 | comments | read during the full pass over all OSD-116 comments on 2026-09-20; not re-opened when this entry was written |

**Facts recorded**:

1. The built master-ticket workflow carries transition **id 9 `Cancel as Duplicate`**
   (待审批 → 已取消, 仅服务账号), registered as built in 建造单 第二区.
2. 04.3 §六 转态权限表, as read (lastModified Sep 16 2026 — after the Sep 15 freeze),
   contains **no row** covering a service-account cancel out of 待审批.
3. Kayden raised this repeatedly during the audit rounds (c49324 ②, c49359, c49372 ④,
   c49403 ④, c49444 ④) and classified it 卡建设、须在冻结前解决 (c49471 ⓑ, c49481 ⓑ),
   escalated as IN-041.
4. It does not appear in the final sign-off risk lists; c49740 states「卡建设的无」.
5. Full-text search of the 建造单 (v31) returns **zero** occurrences of 确认重复,
   IN-041, 处理中→已取消 and 无既有出口 — while the transition itself is already built.

**Why recorded rather than acted on**: determining whether this is a 标准缺口 (04.3's
own gap), a 业务歧义, or already settled somewhere not yet read is not this repo's call,
and no instruction has been given. Recorded so it can be re-checked.

---

**Status correction, 2026-09-22 — F-004 has the same defect F-008 had: it named a second evidence
route (IN-041) and never opened it.** Appended, not rewritten, per rule 4.

The entry's own «Why recorded» paragraph admits the possibility — 「or already settled somewhere not
yet read」 — and its evidence table admits the OSD-116 comments were 「not re-opened when this entry
was written」. IN-041 was named in fact 3 and never looked up. It has now been looked up.

**IN-041 appears in exactly one place in the whole NOSM space, and that place is the S-05 Spec
itself** (CQL `space = NOSM AND text ~ "IN-041"` → 1 hit, pageId 2036858900; a Jira-wide
`text ~ "IN-041"` search returns **zero** issues). The Spec carries it as 需技术确认项 item 7, verbatim:

> 7. N07"确认重复→已取消"转态——04.3§六转态权限表当前无对应出口（现有出口为请求人撤回／服务账号或
>    Project Owner中止），实现路径待Alden确认（**已上报治理侧IN-041**）。

**What this changes, and what it does not.**
- **The substance of F-004 is CONFIRMED, and confirmed by the Spec's own words**: 04.3 §六 has no
  covering exit for this transition, and the existing exits are exactly the two F-004 named
  (请求人撤回 ／ 服务账号或 Project Owner 中止).
- **The framing of F-004 is WRONG.** Facts 4 and 5 put it as an item that was classified 卡建设 and
  then vanished from the final sign-off lists and from the 建造单 — i.e. that nobody is holding it.
  That is not the case: it is registered in the Spec's 需技术确认项 as item 7, with the escalation id
  and 「实现路径待 Alden 确认」. 需技术确认项 is the designated place for precisely this, so
  c49740's 「卡建设的无」 is consistent with the item having been carried forward rather than dropped.
  It is held, it is routed to Alden, and it is not ours.
- Fact 5 (zero occurrences in the 建造单) stays true but stops being evidence of neglect: under
  04.5 §五 唯一落点 the Spec is the semantic home and the 建造单 does not duplicate it.

**Net**: F-004's absence claim stands; its "this slipped through" reading is withdrawn. Still not
reported to anyone, still not acted on, and nothing here is a basis for raising it — item 7 already
routes it.

## F-005 · 2026-09-20 · 04.3 §六 does not cover the executor c50244 mandates for N28

**Status**: recorded on the 建造单 (v33) on the repo owner's explicit instruction, as an
open item for the 04.3 Owner. Not reported to anyone else. The row it sits on stays
「待办」; nothing was configured.

**Status update, 2026-09-21 — routed, now waiting on Kayden.** Two things moved today.
(a) We sent **c50263**, withdrawing from our side the 「before, or atomically with」 ordering
constraint that had been raised to Alden in Kent's c50256, because 04.3 §六 already decides
that case verbatim; and we stated that 「Whether N28 (Spec: 对外 status→已取消 during 处理中)
needs an exception to §六 is a question for the 04.3 Owner, not a Mode-5 change for Alden.」
So the open question now sits with **Kayden** (04.3 Owner), not Alden. No reply as of
2026-09-21 18:45 WIB. (b) Kent acknowledged Kayden's ruling in **c50257**: 「N28＝方向 2——
转态权限配 HR Ops & Data 角色组＋守护件；方向 1 记为上线后第二版」, and 「Bambang 的 Mode-5
抢跑约束我已转 Alden」 — that routing is the one we then withdrew in c50263.
04.3 re-checked live today: **still v33**, §六 unchanged. Finding itself unchanged; only its
addressee and its status changed.

**Found while**: drafting the 建造单 update that consumes Kayden's two rulings in
OSD-116 c50244, at the repo owner's request.

**Pages / objects actually opened and read (all on 2026-09-20)**:

| pageId / id | Page / object | version as read |
| --- | --- | --- |
| OSD-116 c50244 | Kayden's ruling, 2026-09-20 13:31 +07 | — |
| OSD-116 c50228 | Kent's escalation (defines 方向 1／方向 2) | — |
| 1676771343 | 04.3｜状态词汇表与 Workflow 配置规范 (§五, §六, page-foot 维护说明) | v33 |
| 1676804100 | 04｜流程建设与执行治理总纲 (§六 子页地图) | v25 |
| 1678573617 | 04.5 (§6.1 基线失效) | v79 |
| 1676738564 | 04.1 (§一 Registry row) | v46 |
| 1690140756 | 04.8 (§三 entity row, §五 Lifecycle Stage) | v20 |
| 1676640265 | 04.0 (§二 档案卡) | v26 |
| 1704362028 | 07｜指南 (§二, §三) | v28 |
| 2096463922 | 纪律与绩效改进处置｜建造单 | v32 → v33 |

**Facts recorded**:

1. c50244 rules that N28 takes 方向 2: the abort stays manual, with the executor widened
   from a single Project Owner to the **HR Ops & Data role group**. (The 方向 1／方向 2
   labels are defined in c50228, not in the ruling itself.)
2. 04.3 §六 转态权限表, row「**主单**转入「已取消」（执行中止）」, reads:
   「**仅服务账号与该主单所在 Project 的 Owner**」. An HR role group is **not** among them.
3. The same section opens with「**不设限制的转态视为配置未完成**」.
4. Configuring N28 as ruled therefore creates a transition permission the table does not
   cover. Whether 04.3 should carry such a row, or the ruling should be reconciled with
   it, is not this side's call.
5. 04.3's Owner is **Kayden Lee** — stated identically in 04.3's own page-foot 维护说明
   and in 04 §六 子页地图. That 维护说明's「更新触发条件」explicitly lists
   「转态权限执法点、撤回规则…变更时更新本页」.
6. **Related to F-004**: both are gaps in the same table (04.3 §六 转态权限表) — F-004 is
   the missing row for the already-built service-account cancel from 待审批; this one is
   the missing row for the mandated HR-role-group abort.

**What was written to the 建造单 (v33, four additions, originals kept)**: the Registry
blocker row (ruling recorded, still blocked, dependency reassigned, plus the read-path
constraint and the 04.8 §三 status-column fact); the N28 blocker row (this finding, plus
the 抢跑 constraint routed to Alden, and the note that 04.5 §6.1 基线失效 is not triggered
because the Spec page is not edited); the §2 transition table row 11; and the §8 guard row.

**Correction carried from F-003**: the earlier draft of the Registry row claimed
`纪律处分记录状态` should be registered at 04.8 §五. That was wrong and was removed before
writing — 04.8 §三 already registers it. See F-003's status correction.

---

**Re-verification, 2026-09-22 — F-005 HOLDS on substance, with two corrections to how it was written.**
04.3 (1676771343) re-opened live today, lastModified **Sep 16, 2026**. Appended per rule 4.

**Verified verbatim.** §六 opens 「Workflow 的每个转态动作都必须限定允许执行者。**不设限制的转态视为配置未完成。**」
✓. 维护说明 「Owner：Kayden Lee」 and 「更新触发条件：…**转态权限执法点、撤回规则**或 Resolution 映射变更时
更新本页」 ✓. The 转态权限表 does carry 「**主单**转入「已取消」（执行中止） | 仅服务账号与该主单所在 Project
的 Owner…」 ✓, and no row admits a role group.

**Correction 1 — F-005 quoted that row TRUNCATED, dropping the row's own pointer.** The full cell reads
「仅服务账号与该主单所在 Project 的 Owner；**触发与动作范围见本节下方撤回规则「进入待子单完成后」条**」.
F-005 stopped at the semicolon. That is the same methodological error as F-004 and F-008 — quoting a row
while omitting the place it sends you. **The pointer has now been followed, and it confirms rather than
overturns**: 撤回规则「进入待子单完成后」 reads 「由处理方依实际情况处理：由**服务账号或 Project Owner**
在同一动作范围内，把已生成、尚未关闭的子单转「已取消」，并将主单转入「已取消」」 — the same two executors,
no role group. The conclusion is unchanged; the quotation discipline was not.

**Concrete consequence now that the pointer is read**: 「该主单所在 Project 的 Owner」 resolves through
04.1 §一, whose SSCSD row gives Owner ＝ **Alden（V1 平台持有）**. So the permitted set for this exit is
**service account ＋ Alden**, and HR Ops & Data is outside it.

**Correction 2 — the framing 「the executor c50244 mandates」 understates where the mismatch comes from.**
The **frozen Spec itself** already carries it, before c50244 (2026-09-20) existed: the N28 row of the
node table names 泳道 ＝ **HR Ops & Data** and its 执行载体 reads 「HR Ops & Data 在「处理中」状态执行中止
（**04.3§六既有「Project Owner中止」出口，不新造转态**）」. So the frozen Spec asserts it reuses an exit
that does not admit its own named executor. c50244 confirmed that direction; it did not create the
mismatch. F-005 should be read as a mismatch **inside the frozen Spec**, which is a stronger and more
accurate statement than a mismatch with a later comment.

**Correction 3 — the F-004 analogue was checked, and it does NOT apply here.** F-004 turned out to be
registered in the Spec's 需技术确认项 as item 7. The same list was read in full today: it has **ten**
items (N01 · N13/N26/N27 · N20/N21 · N22/N23 · N25 · N16 · **N07 确认重复→已取消** · N16 跨部门 ·
N03/N06 Slack · N07 审批交互), and **none of them covers N28's executor**. So unlike F-004, this one has
no registered holder in the Spec — which is exactly why it sits on 建造单 row 19 and why our c50263
routed it to the 04.3 Owner. That routing was correct.

**Net**: F-005's substance survives unchanged and is now better grounded. Two writing defects corrected.

## F-006 — 身份件 (Submission Identity Verifier) status is recorded three ways and two of them are stale

**Found**: 2026-09-21, during the full NOSM version sweep. **Not reported to anyone yet.**

**The fact** (live, 2026-09-21): the platform piece `v0Ta9NW64VJiVQqd` is published.
- `04.9｜n8n Workflow 登记表` **v106** (index row added at v104, status set at v105, 07:52:55Z,
  version message 「身份件行状态改 active·已发布 616bbd91」): row reads
  「active·已发布（versionId＝activeVersionId 616bbd91）。5 节点」.
- `04.9.1｜详情：平台` **v19** (07:52:45Z): status block rewritten to
  「active·已发布（versionId＝activeVersionId `616bbd91-5cd7-4c10-bcc4-ae9052592253`）。5 节点；
  件名已去「DO NOT ACTIVATE · shadow」后缀」.

**The two stale copies**:
1. `04.4｜自动化配置模式库` §十一 shared-component index — the 身份件 row still reads
   「在建（影子·shadow，随模式九批次上生产）」. This is not just a lag: 04.4 was itself
   edited to **v33** at roughly 10:00Z, about two hours *after* 04.9 v105, and that edit
   (the 协作 Thread row) left the 身份件 row untouched. Verified from the v31→v33 diff,
   where the 身份件 row appears as an unchanged context line.
2. `04.4.3｜身份件 · 调用契约` **v6** (2026-09-14) — has not moved at all; still
   「在建·影子·inactive」. Its own 维护说明 lists a status change of the piece as an
   update trigger.

**Why it matters**: 04.5 §五 puts one fact in one place. Here one fact (是否已发布) sits in
four places, two current and two stale. A builder who routes via 04.4 §十一 — which is what
the CLAUDE.md skill text tells us to do for shared components — reads the wrong answer and
would conclude the piece cannot be called. It also affects our own OSD-116 c50279, which
quoted the 04.9.1 **v17** sentence 「模式九批次已上线而本件未随批发布，是否漏带待 Alden 确认」;
that sentence was deleted in v19 and the comment was sent after the deletion.

**Owner**: Alden (page owner of both 04.4 and 04.4.3).

**Not acted on.** No edit, no comment, no report sent. Recorded here and queued as item 10
in `docs/pending-buildsheet-updates.md` for our own 建造单 v34.

**Status update, 2026-09-21 18:45 WIB — re-checked, still open.** Both stale copies are
unchanged: **04.4 still v33** and **04.4.3 still v6**; neither appeared in the second
version sweep. The two current copies are also unchanged (04.9 v106, 04.9.1 v19), so the
disagreement stands exactly as recorded. Still not reported to anyone.

---

## Sync-check history

| Date | Compared | Result |
| --- | --- | --- |
| 2026-09-20 | 07.06 §八 (1730347066, Sep 15 2026) vs `CLAUDE.md` §一 | Identical; no change needed |
| 2026-09-20 | 04 §一/§五/§六 (1676804100, Sep 05 2026) vs `docs/04-anchor-navigation.md` | 3 phrases dropped during an earlier copy; restored to match source (commit `a15c1b3`) |
| 2026-09-21 ~04:00Z | Both copies, per the then-current skill | Reported **"in sync"** — and that report was **incomplete twice over**: the comparison was done by eye and so was blind to a dropped column, and the skill covered only the two local files, so it said nothing about the ~30 other source pages. Both defects are fixed in the skill (commit `ebd09b0`). Kept here because the log must show the miss, not only the fix. |
| 2026-09-21 ~11:00Z | Version sweep of every recorded source page, whole-space CQL | **7 pages had moved**: 07.06.1 v33→v34 · 04.9 v103→v106 · 04.9.1 v17→v19 · 04.7 v45→v46 · 04.4 v31→v33 · 04.4.4 v1→v4 · 04.8 v20→v21. Diffs read; substance in `docs/reading-notes-2026-09-21.md` (commit `dd592bf`). |
| 2026-09-21 ~11:20Z | 07.06 §八 (1730347066, **v30**) vs `CLAUDE.md` §一, by script | **Identical** — 19 bullets and the whole 开发入口的冻结要求 subsection match after normalisation. No drift. |
| 2026-09-21 ~11:20Z | 04 §一/§五/§六 (1676804100, **v25**) vs `docs/04-anchor-navigation.md`, by script | **Drift found and fixed** (commit `ebd09b0`): §一 was missing its 4th column 责任边界 entirely; §五 was missing its 4th column 放行条件 and the section's lead sentence; §六 边界铁律 was missing its closing sentence. All restored verbatim; the three tables now compare row-for-row identical (5 / 7 / 16 rows). |
| 2026-09-21 ~11:30Z | Second version sweep + OSD-116 + #nos-bo | **No Confluence page moved** past the 11:00Z versions (verified per page, not inferred from the CQL list). OSD-116: 163 comments, newest still c50290. #nos-bo: no new top-level message; one thread moved (latest reply 2026-09-21 13:59 +07). (commit `5e5c58f`) |

---

**Status correction, 2026-09-22 — F-006 is WRONG on two points, one of them a quotation that is not
on the page.** Written after the repo owner pointed out that 04.4.3 had never been opened. It has
now been opened live (pageId 2076508181, lastModified 2026-09-14). Appended per rule 4.

**Wrong point 1 — a quotation that does not exist.** F-006 states 「Its own 维护说明 lists a status
change of the piece as an update trigger.」 04.4.3's 维护说明 reads, verbatim and in full:
「更新触发：**输入/输出字段增减、消费者增减**时更新本页并同步 04.4 §十一 与（如有）04.9。」 Two triggers,
and **a status change of the piece is not one of them**. Note also the direction: the sync this page
owes runs **outward** (this page → 04.4 §十一 → 04.9), not inward. So 04.4.3 is not in breach of its
own rule, and F-006's stated basis for calling it a delinquent copy is fabricated.

**Wrong point 2 — the framing 「one fact (是否已发布) sits in four places」 conflates two different
facts.** 04.4 §十一's 状态 column is not a publication flag. Its own rule reads
「「在建」行由建设者开工时自登，**验收通过后**由建设者更新为「可用」」 — it flips on **acceptance**, not on
publication. The same table proves it in the other direction: the 协作 Thread row was set to
「**可用**（Alden 验收 2026-09-21，NSE-1143 c50273）」 while that same row states the piece is
「仍 inactive」 and 「至今零真跑」. So in this table **可用 does not mean active, and 在建 does not mean
unpublished**. 04.4.3 says the same thing in its own words: 「验收：平台侧＝Alden；消费侧＝离职（N3）＋
Grade（N3）」 — acceptance is still outstanding. A piece that is published but not yet accepted is
correctly recorded as 在建. There is no contradiction to report.

**What actually remains, and it is small.** Two descriptions have genuinely fallen behind the facts,
without breaching any page's own update rule:
- 04.4.3's page-head 状态 paragraph still says 「本件自身仍 **inactive**」 and 「**影子 · shadow**」.
  04.9.1 v19 records the piece as `active·已发布` with 「件名已去「DO NOT ACTIVATE · shadow」后缀」.
- 04.4 §十一's 身份件 row still carries the parenthetical 「（影子·shadow，**随模式九批次上生产**）」,
  which describes a future that has since happened.
The 在建 word itself in that row may well be correct, for the reason above.

**This correction also reverses F-006's practical warning.** F-006 says a builder routing via
04.4 §十一 「reads the wrong answer」. For this repo the opposite holds: 建造单 row 32's 解除判据 is
「若走身份件，**待其转「可用」后**本流程方可建 N03 身份认证段」 — the gate for us is **可用**, i.e.
acceptance, which is exactly what 04.4 §十一's column reports. Reading 在建 there gives us the
**right** answer for our own gate. The item `docs/pending-buildsheet-updates.md` butir 10 has been
corrected accordingly.

**Net**: F-006 keeps only a narrow observation about two out-of-date descriptive phrases. Its
contradiction claim, its rule-breach claim and its builder-risk claim are all withdrawn. Nothing was
reported to anyone at any point.

## F-007 · 2026-09-22 · `Withdraw` and `Cancel as Duplicate` leave byte-identical terminal data

**Status**: recorded. Not reported to anyone. Not acted on.

**Pages and objects actually read** (all live, 2026-09-22):
- 04.5.3｜Sandbox 与测试数据策略 (pageId 1729626578, lastModified 2026-09-15) — §一–§五 in full,
  read *before* creating any test ticket.
- 04.3 §7.1／§7.2 as quoted on 建造单 (pageId 2096463922, lastModified 2026-09-20 = v33), 区二.
- Jira, project SSCSD: `getJiraIssueTypeMetaWithFields(SSCSD, 14357, requiredFieldsOnly=false)`;
  `getTransitionsForJiraIssue` on SSCSD-421 and SSCSD-422; `getJiraIssue` with `expand=changelog`
  on both after transitioning.

**What the build sheet says** (区二, transition table):
- transition 8 `Withdraw` → 「Resolution＝**Cancelled**（「取消原因」＝Withdrawn）」
- transition 9 `Cancel as Duplicate` → 「Resolution＝**Cancelled**（「取消原因」＝Duplicate Case）」

**What was measured.** Two fresh TEST tickets were created and each run through one of those
transitions (SSCSD-421 → 8, SSCSD-422 → 9). Each ticket's changelog has **exactly one entry with
two items**: `status` 15855 → 15961, and `resolution` `null` → `10041` Cancelled. Nothing else was
written. `customfield_18054` (Reason) is `null` on both; `customfield_18143` (Rejection Reason) is
`null` on both. No 取消原因 field exists on this issue type at all — the create-screen read returns
48 fields, none of them a cancellation-reason field belonging to S-05.

So after the fact the two tickets are indistinguishable in data: same status, same resolution, no
other marker. A withdrawal by the requester cannot be told apart from a duplicate cancellation.

**Why this is not a contradiction of the existing split.** 「Cancellation Reason (new, not 18054 —
c50234 item 3)」 is a **master-ticket** field, and c50234 item 2 places master-ticket fields in
Alden／V1's domain; OSD-116 c50283 explicitly excluded it from the 13-field request. The field
therefore does not exist yet and the post function has nowhere to write. The **new** part is the
measured consequence: while it does not exist, the two cancellation paths are not separated in the
data, which touches reporting and audit rather than convenience.

**Relation to F-004.** F-004 records that 04.3 §六 has no row covering the built `Cancel as
Duplicate` exit. F-007 is a separate, empirical observation about what the two exits write; it does
not restate or replace F-004.

**Explicitly not done**: no field was created, nothing was written into another flow's field, no
post function was touched, and nobody was told. Both test tickets were left in their terminal state
per 04.5.3 §四 (「永不硬删」).

**Where the raw evidence lives**: `docs/test-evidence-2026-09-22-terminal-transitions.md`.

**Status update, 2026-09-22 (same day) — extended to a third transition, with one distinction.**
Transition 3 `Reject` was live-run on a third TEST ticket (SSCSD-423) after the entry above was
written. Same shape: changelog holds exactly one entry with two items, `status` 15855 → 15850
Rejected and `resolution` `null` → `10042` Rejected; `customfield_18054` and `customfield_18143`
are both `null`. So 区二's 「取消原因」＝**Dismissed** (from Spec N07②) is not written either — the
gap covers all three transitions run today, not two.

**But the consequence is not the same for all three, and must not be flattened.** `Reject` lands on
a *different* resolution (`Rejected` 10042, not `Cancelled` 10041), so it remains distinguishable
from the other two paths; what is missing there is only the reason, not the identity of the path.
The indistinguishability this finding is about holds specifically between `Withdraw` and
`Cancel as Duplicate` — those two are identical in every stored field.

Also measured while doing it: of 04.3 §7.1's four permitted resolutions, three now have observed
ids — **Done ＝ 10000** (SSCSD-411, 2026-09-18), **Cancelled ＝ 10041**, **Rejected ＝ 10042**.
`Rerouted` is not used by this flow (区二: 五态、无「已改道」). `Abort Case`(11) is still unrun, held
on the repo owner's instruction pending B-15.

Still not reported to anyone; still nothing added, changed or configured.

---

**Status correction, 2026-09-22 — one sentence in F-007 over-reaches its evidence.** Appended per rule 4.

F-007 states 「No 取消原因 field exists on this issue type at all — the create-screen read returns
48 fields, none of them a cancellation-reason field belonging to S-05.」 That is inferred from
`getJiraIssueTypeMetaWithFields`, which reports the **create screen only**. A field can exist on an
issue type without being on that screen, and 04.10 §三 records from實測 exactly what then happens:
for cf18203 it notes 「原写「不依赖挂屏」已证伪——实证机器 API 读/写均依赖挂屏（**未挂时读缺键**、写报
not on screen）」. So an unmounted field would be invisible both to the create-screen read and to the
field reads performed here. The inference is therefore not supported by what was done.

**There is also no register to check as a second route, and 04.10 says so itself.** Its 权威边界
reads 「**本页只承载执行卡／子单侧的共享字段；主单字段归 SSCSD/V1**，Registry 实体字段归 04.8 §5」, and
§一 routes 「主单侧对象（SSCSD 四形状、主单字段）→ SSCSD／V1 范畴，Owner：Alden」. A cancellation-reason
field on the master ticket is a **master-ticket** field, so it is outside 04.10 by design. There is no
Confluence register for it to appear in.

**What is unaffected — the measured core.** F-007's conclusion does not rest on the field-existence
inference. It rests on the changelog, which is direct evidence: each of the three transitions produced
**exactly one changelog entry with exactly two items** (`status` and `resolution`) and nothing else.
Whatever fields do or do not exist, **the post functions wrote no cancellation reason**, and no such
value is readable on any of the three tickets.

**Corrected wording for the record**: not 「no such field exists」 but 「the post functions wrote only
status and resolution, and no cancellation-reason value is readable on the ticket; whether an
unmounted field exists was not established and cannot be established by the reads performed here」.
The consequence recorded in F-007 — `Withdraw` and `Cancel as Duplicate` are indistinguishable in
readable data — is unchanged.

## F-008 · 2026-09-22 · The S-05 audit baseline (Spec page v58) is not the Spec's current page version

**Status**: recorded. Not reported to anyone. Not acted on. **Not decided** — the question below
belongs to the 04.5 Owner and the freeze 裁决人, not to this repo.

**Found while**: tracing three version numbers the repo owner asked about after they turned up in the
Spec's §① 状态区. Two of the three resolved cleanly (see «What is not a problem» below); this one did not.

**Pages actually opened and read** (all live, 2026-09-22):

| pageId | Page | lastModified as read |
| --- | --- | --- |
| 2036858900 | 纪律与绩效改进处置｜流程 Spec (S-05) | Sep 15, 2026 |
| 1678573617 | 04.5｜流程 Spec 与建造单：编写与校验规范 | Sep 19, 2026 |

**The rule, verbatim from 04.5 §6.1.** The 审计基线 column format is defined as
「**Spec 页面 v{n}**＋04.5 v{n}（并列适用标准版本）」 — so that number is the Confluence **page**
version. And the invalidation rule reads:

> 基线失效规则：机器报告必须绑定被扫描的 Spec 页面版本与适用标准版本。机器扫描后页面或适用规则发生变化，
> 结果立即失效并须重新进入结构审计；机器通过不得沿用。…**机械判据：状态区校验执行记录最后一行绑定的基线版本
> ≠ 页面当前版本时，该审计结论自动失效，不得被任何下游 Gate 消费；正文修订后须重跑审计或由裁决人显式豁免留痕。**
> 存量豁免：第四节「存量条款」明列的批次与检查项不触发本节基线失效…

The same requirement appears as checklist item 20: 「**状态与记录等值**：状态区声明的状态所绑定的校验执行
记录最后一行基线版本必须等于页面当前版本；不等＝失败（历史留档行除外）。」

**The facts measured.**

1. S-05 §① 状态区 has exactly **one** 结构审计执行记录 row, and its 审计基线 cell reads
   「**Spec v58＋04.5 v69**」, machine-run 2026-09-10 11:43, dual sign-off passed the same day
   (业务签 Kayden Comment 49740, 技术签 Alden Comment 49731).
2. The Spec's page version is **not** v58 any more. Its own 自然语言版本迭代 table shows two
   further semantic versions after the audit, both dated **2026-09-15**: **v26** (N11 对齐裁决收口 —
   writing the alignment resolution into the page and marking it frozen) and **v27（现行版）**
   (backfilling the standard header fields per Alden's NSE-1153 c50014 reverse-link requirement).
   Each of those is at least one page revision, so the current page version is strictly greater than 58.
3. **No explicit 豁免留痕 for the baseline mismatch appears anywhere on the Spec page** — §① has the
   audit row and the 判例引用 list; §⑤ 对齐与结构审计证据 records 「冻结状态：已冻结｜裁决人：Felix｜
   冻结时间：2026-09-15」. Neither records an exemption.
4. **The freeze evidence does not record the frozen page version.** 04.5 §六 「已冻结」 row requires the
   authorised AI to 「记录对齐证据、**冻结页面版本与日期**，并把状态改为「已冻结」」. The date is there
   (2026-09-15); the page version is not — on the Spec, and likewise on the 建造单 状态区 (「已冻结｜
   冻结时间：2026-09-15」).
5. **The §四 存量条款 do not appear to cover this.** Each of them (2026-08-19 / 08-31 / 09-03 / 09-04 /
   09-14 / 09-16) exempts *specific checklist items added on that date* from triggering baseline
   invalidation for existing Specs. None of them speaks to page revisions made by the flow's own Owner
   after the audit. Read as written, they are a different exemption.

**Why this is not obviously a defect, and why it is not mine to call.** Two of the post-audit edits
(semantic v26) are the very writes the lifecycle *requires* in order to freeze — 04.5 §六 instructs the
authorised AI to record the alignment evidence and set the status on the page. Those edits necessarily
bump the page version after the audit baseline was pinned. Read literally, the mechanical rule would
make every freeze invalidate its own audit, which cannot be the intent. 04.5 §6.1 provides the escape
in its own text — 「由裁决人显式豁免留痕」 — so the question is whether such an exemption exists,
is unnecessary, or still needs to be recorded. That call belongs to the 04.5 Owner (Kayden Lee, per
04.5's 维护说明) and to the freeze 裁决人 (Felix). **This entry does not answer it, does not route it,
and nothing here may be used as a basis for proceeding or for stopping.**

**Why it matters for the build, stated without inflating it.** 07.06's 「开发入口的冻结要求」 requires BO
to have read the 冻结版 Spec, the 结构审计通过证据 and the 对齐签收证据 before starting, 「任一缺失即退回
上游」. The evidence exists and is registered; what is unresolved is whether the audit row satisfies
04.5 §6.1's equality rule on today's page. So this is a question about the paperwork of the entry gate,
not a claim that the Spec's content is wrong or that any work done so far was wrong.

**What is NOT a problem — the other two numbers, resolved.**

- 「**当前生效版本：无**」 is **correct and expected**. 04.5 §六 defines 「当前生效版本」 as the 已上线 vN
  state — 含义「当前生效版本，配置与本页一致」, entered only by completing §八's 上线三合一 (Gate 3).
  S-05 is 已冻结, not 已上线 (建造单 区九: 「🔲 未上线」), so having no 生效版本 is exactly right.
- 「**签收绑定 Spec v25**」 vs 「**Spec v58**」 are **two different numbering systems, both legitimate**.
  v25 is the Spec's own 自然语言版本 (dated 2026-09-10, 「双签通过后状态区更新＋对齐期非实质订正」) — the
  semantic version the 18 signatories signed, by the 口令 「签收｜S-05 Spec v25」. v58 is the Confluence
  **page** version, which is what 04.5 §6.1's format mandates for 审计基线. Both rows sit in the same
  §① 状态区 and both write the prefix 「Spec v…」, which is what makes them easy to misread — this
  reader did misread them at first.

**Verification limits, stated plainly.**
- This session has **no Confluence version-history tool**, and `getConfluencePage` returns
  `version: null` for these pages. So I could **not** verify from the page itself that page v58
  corresponds to 2026-09-10, nor what the page's current version number is.
- The figure **v62** used throughout this repo comes from `docs/source-versions.md` and earlier
  sessions, not from today's read. The mismatch in fact 2 does not depend on it: it follows from the
  two post-audit semantic versions being dated after the audit.

**Where the related trace lives**: this entry; no separate file was created.

**Status correction, 2026-09-22 (same day) — F-008 is RETRACTED on its two main claims.**
Written after the repo owner told me to check properly before claiming. Appended, not rewritten,
per rule 4. What follows overrides the entry above wherever they conflict.

**Retracted claim 1 — «the freeze evidence does not record the frozen page version».** This is
**wrong**. It is recorded, and machine-readably. OSD-116 **c50009** (Felix_HR, 2026-09-15 16:06 +07)
is an `OSD-FREEZE` marker carrying verbatim:
`{"specPageId":"2036858900","frozenPageVersion":61,"frozenBy":"Felix","frozenAt":"2026-09-15"}`,
repeated as a single-line marker in **c50013**. The error was mine: I looked only at the Spec page
and did not look at the Feature's comments, which is where the marker lives.

**This repo already had it right.** `docs/source-versions.md` records
「v62 (冻结基线 v61)」, the 建造单 names 「Spec v61」 three times and states explicitly
「`frozenPageVersion` 权威值住 OSD-116 的 `OSD-FREEZE` 标记 Comment，本页不复述（04.5 §五 唯一落点）」,
and Kent's c50071/c50073 handoff already said 「frozen Spec v61」. So the registration is correct,
correctly routed under 04.5 §五's single-landing-point rule, and nothing was missing.

**Retracted claim 2 — the framing that the audit conclusion is auto-invalid and 「不得被任何下游 Gate
消费」.** I had no evidence that this is the gate that actually runs, and there is evidence to the
contrary. On the same day, **Bot_SSC** posted 【开发门禁未过·已退回对齐（Q3-5）】 twice — **c50006**
(16:03) and **c50010** (16:06) — both with a single reason: 「冻结门禁未过：**未找到 OSD-FREEZE 冻结标记**」.
So the machine's development gate checks for the freeze marker, not for baseline/page version equality.
Felix posted the marker at 16:06 and again at 16:12. Presenting the version-equality sentence as the
operative blocker was over-reading on my part.

**What still stands, unchanged and now corroborated.**
- 「当前生效版本：无」 is correct. Corroborated on a second Spec: 员工离职｜流程 Spec (pageId 1711276058,
  read live today) writes 「当前生效版本：**无（尚未上线）**」 with the reason in brackets.
- v25 vs v58 are two different numbering systems. Now corroborated from inside 04.5 itself: its §四
  存量条款 2026-09-04 says 「（**04.5 v62 发布日**）」, and the ledger has 04.5 at v79 today. So 04.5's
  own page version ran v62 (09-04) → **v69** (09-10, the figure in S-05's audit row) → v79 (09-19).
  That ladder is consistent only if the audit row's numbers are **page** versions, as 04.5 §6.1's
  prescribed format 「Spec 页面 v{n}＋04.5 v{n}」 says.

**What remains as an observation, much smaller than the original entry, and not ours.** S-05's
状态区 carries **one** 结构审计执行记录 row (baseline page v58) and no row covering the revisions made
after it. The sister Spec 员工离职 keeps **22** rows — one per revision, including purely
non-substantive ones (双语化, 订正, 分隔符统一, 登记) — and marks superseded rows
「基线已随 04.5 升版失效，留档」 and 「【基线已失效，留档】」. So the mechanism for a moved baseline is
established practice, and S-05 simply has fewer rows. Whether that matters is the Spec Owner's
business (04.5 §五 写权分离), it is not a blocker for the build, and it is **not raised**.

**One fact worth carrying into 验收, not a finding.** The page moved **61 → 62 after the freeze**:
Kent's **c50020** (2026-09-15 17:23) asked Felix to add the 「对应 Feature：OSD-116」 backlink line,
because Alden's new N8 build (NSE-1153 c50014) would otherwise judge it `NO_BACKLINK`. That is the
自然语言 v27 row. So what this repo reads as «the Spec» (page v62) is one revision past the frozen
baseline (page v61), and the delta is that header backlink line. 04.5 §八's DoD requires
「验收前确认实际消费的冻结 Spec 版本与对齐、结构审计证据及冻结基线一致」, so this is stated then. The
建造单 already carries both numbers (「对应 Spec v61 + v62 核对段」), so nothing needs adding.

**Net effect on this entry**: F-008 should be read as **closed and mostly wrong**. It produced no
correct new finding; it produced one correct clarification (the two numbering systems) that was
already implicit in the repo's own ledger. Nothing was reported to anyone at any point.
