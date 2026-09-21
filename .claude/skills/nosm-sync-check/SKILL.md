---
name: nosm-sync-check
description: Verify the repo's controlled copies (CLAUDE.md, docs/04-anchor-navigation.md) still match their Confluence sources, and sweep every recorded source page for version drift before any NOSM/BO decision is made.
---

# NOSM Sync Check

Repo `CLAUDE.md` is an explicitly-declared **controlled deployment copy** of Confluence
page `07.06｜建设指南` §8 (page id `1730347066`), and `docs/04-anchor-navigation.md` is a
snapshot index of page `04｜流程建设与执行治理总纲` (page id `1676804100`). Both source
pages can change independently of this repo. The source page's own rule is:
if the copy and the source disagree, **stop and report "deployment drift"** — never
silently work off a stale copy.

Beyond those two files, **every other page we have ever quoted can also move**, and a
quote taken from a session cache is not evidence about the live page. This skill exists
so both of those rules are actually executed, not just written down.

## When to run this

- First action in a new session/device where BO-building work in this repo is about to start.
- Before relying on CLAUDE.md's skill text or the 04.x navigation map to make any
  real decision (Spec review, Route registration, n8n workflow build, audit gate).
- **Before sending anything outward** (a Jira comment, a Confluence edit, a Slack message)
  that quotes a Confluence page — run at least step 6 for the pages being quoted.
- Not needed for unrelated chit-chat or work that never touches NOSM/BO rules.

## Steps

1. **Confirm connectors are live** (mirrors CLAUDE.md §〇):
   - Atlassian Rovo: call `getAccessibleAtlassianResources` (or read any NOSM page) —
     must resolve the `nexmax` site.
   - n8n: call `search_workflows` (or equivalent list call) — must return a workflow list.
   - If either fails, stop here and report the connector failure. Do not proceed to
     content comparison with unverifiable source access.

2. **Re-fetch the skill source**: `getConfluencePage` for `cloudId=nexmax.atlassian.net`,
   `pageId=1730347066`, `contentFormat=markdown`. Extract §八「流程建设 Skill（正式原文）」
   — the preamble paragraph, the bullet list under `流程建设 skill｜适用者：BO 建设团队`,
   and the `开发入口的冻结要求` subsection. Save it to a scratchpad file.

3. **Diff against `CLAUDE.md`** §一 in this repo. Ignore purely cosmetic differences
   (markdown link formatting, heading levels). Any actual wording/rule change counts
   as drift.

4. **Re-fetch the navigation source**: `getConfluencePage` for `pageId=1676804100`.
   Compare its 一/五/六 tables (action routing, SSOT registration targets, 04.x subpage
   map — including each row's Owner and 当前状态) against `docs/04-anchor-navigation.md`.

5. **Compare mechanically, not by eye.** Steps 3 and 4 are done with a script, never by
   reading the two texts side by side:
   - Extract the bullets / table rows from both sides, strip markdown links to their text,
     strip `**`, backticks, backslashes and all whitespace, then compare the lists for
     **exact equality**.
   - **Compare the header rows too, and assert the column count matches.** A dropped
     column is invisible when you only compare the columns the local copy happens to have
     — this is exactly how the missing 「责任边界」 and 「放行条件」 columns survived an
     earlier "in sync" report (2026-09-21).
   - Assert the row count matches on both sides before comparing content; a missing row
     is drift, not a formatting difference.
   - Report the script's verdict, not an impression.

6. **Source version sweep.** The two files above are not the only thing that goes stale.
   - Read `docs/source-versions.md` — the ledger of every Confluence page we consume,
     with the version each of our notes and drafts is standing on.
   - Run one CQL query over the **whole space**, not just the page ids on file:
     `space = NOSM AND type = page AND lastmodified >= "<date of the previous sweep>"
     order by lastmodified desc`. Sweeping the whole space is what catches pages that were
     created after the ledger was written (e.g. 04.4.4).
   - For each returned page that appears in the ledger, get its current version with
     `listConfluenceContentVersions`, and where it moved, read
     `diffConfluenceContentVersions` from the recorded version to the current one.
     **The version message is a hint, not the change** — read the diff. (A version message
     naming 「SUBMIT 行」 once meant a completely different row than the one assumed.)
   - Update `docs/source-versions.md` and record the substantive deltas in the reading
     notes. A version number alone is not an update; what changed is.

7. **Jira and Slack sweep — the Confluence sweep does not cover these.**
   Step 6 covers pages. Cards move independently, and a card comment can be newer than anything on
   any page. On 2026-09-22 this was learnt the hard way: a sweep that covered Confluence, OSD-116 and
   #nos-bo reported "nothing moved", while **NSE-1143 c50291** had been posted the evening before —
   newer than the newest OSD-116 comment, and it contradicted a conclusion written minutes earlier.
   - Run `searchJiraIssuesUsingJql` with `updated >= -Nd ORDER BY updated DESC` **on both connectors**.
     They are different accounts and see different projects: the personal account sees OSD, NSE, WT,
     MLKB; the Backend Operations account sees SSCSD, GPM, HR. Neither one alone is the whole picture.
   - **Run a control probe first**, per 07.06.1 E16: query one issue known to exist for that identity
     (`key = SSCSD-411` for Backend Operations, `key = OSD-116` for the personal account). Only once the
     probe returns may an empty result be read as "nothing changed". A JQL that returns zero because the
     identity cannot see the project is indistinguishable from a JQL that returns zero because nothing
     moved.
   - **E16's own limit applies to the probe too** (NSE-1143 c50291 ⑫): an anchor proves *that one issue*
     is visible, not that same-class objects in that project are. A TEST record as anchor gives a false
     positive on coverage — its issue-level security differs from production records'.
   - Then read the cards that matter, at minimum **OSD-116** and **NSE-1143**, newest comment first, and
     stop only when reaching a comment id already on file.
   - Slack: read #nos-bo, and check every thread's reply count and latest-reply timestamp, not just the
     top-level messages. A thread can move while the channel looks unchanged.

8. **Report outcome — say exactly what was checked.**
   - Report steps 2–5, step 6 and step 7 as **three separate results**. Never let "the two controlled
     copies match" be phrased as "all documents are up to date": the copy check covers two
     files, says nothing about the other ~30 source pages, and nothing at all about Jira or Slack.
   - Name the window each sweep covered and the probe that backed it. "Nothing moved" without a stated
     window and a passing probe is not a result.
   - **In sync**: say which files were compared against which page versions; update the
     「上次同步日期」 line in both files only if the comparison actually ran (don't bump the
     date on a skipped check).
   - **Drift found**: do not silently patch and move on. Quote the specific delta,
     update `CLAUDE.md` / `docs/04-anchor-navigation.md` to match the current source
     verbatim (per the source's own "受控部署副本" rule — copy, don't paraphrase),
     commit and push the correction, and tell the user what changed and why.
   - **Source page unreachable**: stop and report — do not fall back to the local
     copy as if it were verified current.

## Quoting discipline (why step 6 exists)

A quote is only evidence about the page version it was taken from. Verifying a draft's
quotes against session-cached files proves the draft matches the cache, not the page.
Before a quote leaves this repo, re-read the quoted page live and confirm the sentence is
still there — a sentence deleted upstream 24 minutes before a comment was sent has already
cost us once (OSD-116 c50279, quoting 04.9.1 v17 after the page had moved to v19).

## Non-goals

- This skill does not re-derive or reinterpret the BO-building rules themselves —
  it only checks whether the local copy matches the source. The rules' content and
  meaning are entirely owned by the Confluence pages.
- This skill does not open every 04.x subpage on every run — the navigation map is a
  routing index by design (see 04 首页 "权威使用原则"); actual object-level decisions
  still require opening the specific subpage the task hits, live, at that time.
  Step 6 checks *whether* a page moved; it does not replace reading the page when the
  task actually depends on it.
- This skill never writes to Confluence, Jira or Slack. It only reads sources and
  updates files in this repo.
