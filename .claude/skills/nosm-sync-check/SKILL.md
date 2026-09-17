---
name: nosm-sync-check
description: Use at the start of any BO-building / process-building session in this repo, before reading a Spec, touching a Route, or making any 04.x-governed decision — verifies the repo's CLAUDE.md and docs/04-anchor-navigation.md are still in sync with the live NOSM Confluence source pages (07.06 §8 and 04), per the source's own "deployment drift" rule. Also re-verifies the Atlassian and n8n connectors are live.
---

# NOSM Sync Check

Repo `CLAUDE.md` is an explicitly-declared **controlled deployment copy** of Confluence
page `07.06｜建设指南` §8 (page id `1730347066`), and `docs/04-anchor-navigation.md` is a
snapshot index of page `04｜流程建设与执行治理总纲` (page id `1676804100`). Both source
pages can change independently of this repo. The source page's own rule is:
if the copy and the source disagree, **stop and report "deployment drift"** — never
silently work off a stale copy.

This skill exists so that rule is actually executed, not just written down.

## When to run this

- First action in a new session/device where BO-building work in this repo is about to start.
- Before relying on CLAUDE.md's skill text or the 04.x navigation map to make any
  real decision (Spec review, Route registration, n8n workflow build, audit gate).
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
   and the `开发入口的冻结要求` subsection.

3. **Diff against `CLAUDE.md`** §一 in this repo. Ignore purely cosmetic differences
   (markdown link formatting, heading levels). Any actual wording/rule change counts
   as drift.

4. **Re-fetch the navigation source**: `getConfluencePage` for `pageId=1676804100`.
   Compare its 一/五/六 tables (action routing, SSOT registration targets, 04.x subpage
   map — including each row's Owner and 当前状态) against `docs/04-anchor-navigation.md`.

5. **Report outcome**:
   - **In sync**: say so briefly; update the "上次同步日期" line in both files to today
     only if you actually re-verified (don't bump the date on a skipped check).
   - **Drift found**: do not silently patch and move on. Quote the specific delta,
     update `CLAUDE.md` / `docs/04-anchor-navigation.md` to match the current source
     verbatim (per the source's own "受控部署副本" rule — copy, don't paraphrase),
     commit and push the correction, and tell the user what changed and why.
   - **Source page unreachable**: stop and report — do not fall back to the local
     copy as if it were verified current.

6. **Tandai session ini sebagai terverifikasi** — hanya setelah langkah 1–5 benar-benar
   selesai (in sync, atau drift ditemukan dan sudah dikoreksi). Jangan ditulis kalau
   konektor gagal atau halaman sumber tidak terbuka:

   ```bash
   mkdir -p "$HOME/.claude/nosm-sync-verified" \
     && touch "$HOME/.claude/nosm-sync-verified/$(cat "$HOME/.claude/nosm-current-session")"
   ```

   Gerbang `PreToolUse` (`.claude/hooks/nosm-gate.sh`) membaca penanda ini. Tanpa penanda,
   tulisan ke `CLAUDE.md`, `docs/04-anchor-navigation.md`, `.claude/skills/**`, dan tool
   tulis Confluence/Jira/n8n **ditolak**, bukan sekadar diingatkan. Session id dicatat oleh
   hook `SessionStart` ke `$HOME/.claude/nosm-current-session`.

## Non-goals

- This skill does not re-derive or reinterpret the BO-building rules themselves —
  it only checks whether the local copy matches the source. The rules' content and
  meaning are entirely owned by the Confluence pages.
- This skill does not open every 04.x subpage on every run — the navigation map is a
  routing index by design (see 04 首页 "权威使用原则"); actual object-level decisions
  still require opening the specific subpage the task hits, live, at that time.
