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
acted on.** No instruction has been given on this one.

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

## Sync-check history

| Date | Compared | Result |
| --- | --- | --- |
| 2026-09-20 | 07.06 §八 (1730347066, Sep 15 2026) vs `CLAUDE.md` §一 | Identical; no change needed |
| 2026-09-20 | 04 §一/§五/§六 (1676804100, Sep 05 2026) vs `docs/04-anchor-navigation.md` | 3 phrases dropped during an earlier copy; restored to match source (commit `a15c1b3`) |
