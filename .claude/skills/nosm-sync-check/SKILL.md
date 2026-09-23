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

5. **Compare mechanically, not by eye — and not by a script you retype each time.**
   Save the two live sources to the scratchpad, then run the committed comparator:

   ```
   python3 scripts/sync_check.py --skill-src <07.06 §八> --nav-src <04 三张表>
   ```

   The nav source file marks each table with `## TBL-A` (§一 动作路由), `## TBL-B`
   (§五 登记集), `## TBL-C` (§六 子页地图). The script compares **header rows and column
   counts as well as row content**, and exits 1 on any drift. **Report the script's exit
   code and output, not an impression.** A dropped column is invisible when you only
   compare the columns the local copy happens to have — that is exactly how the missing
   「责任边界」 and 「放行条件」 columns survived an earlier "in sync" report (2026-09-21),
   and it is why this comparison is no longer written fresh each run.

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

   - **Emit the sweep as a machine-readable artifact**: write
     `docs/ledger/_sweep-latest.json` with `swept_at`, `window_from`, and one `moved[]`
     entry per ledger page that moved — `from`, `to`, `read_after_move`, `how`, `read_at`,
     `changed`. Anything you did not verify goes in as 🔲 with the reason, never as a guess.
   - **Why an artifact and not a sentence**: on 2026-09-22 this skill PASSED, 04.10 was
     correctly recorded as v19→v20, and the write that followed was still defective —
     because the number was recorded and the page was never opened. Prose telling the model
     to "read the diff" did not bind it. The artifact does: gate **G-01 check C11** reads
     this file and refuses any outbound write whose source moved with
     `read_after_move: false`. Recording a version number is no longer enough to proceed.

7. **Report outcome — say exactly what was checked.**
   - Report steps 2–5 and step 6 as **two separate results**. Never let "the two controlled
     copies match" be phrased as "all documents are up to date": the copy check covers two
     files, and says nothing about the other ~30 source pages.
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
