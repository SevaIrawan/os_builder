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

## Sync-check history

| Date | Compared | Result |
| --- | --- | --- |
| 2026-09-20 | 07.06 §八 (1730347066, Sep 15 2026) vs `CLAUDE.md` §一 | Identical; no change needed |
| 2026-09-20 | 04 §一/§五/§六 (1676804100, Sep 05 2026) vs `docs/04-anchor-navigation.md` | 3 phrases dropped during an earlier copy; restored to match source (commit `a15c1b3`) |
