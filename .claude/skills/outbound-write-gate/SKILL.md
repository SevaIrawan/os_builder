---
name: outbound-write-gate
description: Steps 1-6 of the G-01 pipeline. Use before writing ANY draft file in docs/ or ANY Confluence / Jira / Slack content. Explains how to build the claims ledger the gate checks against the session transcript. Hooks enforce it - an outbound write without a passing ledger is blocked, and a turn cannot end with a failing draft.
---

# G-01 Evidence Gate (pipeline steps 1-6)

**Rules and check definitions: `.claude/gates/G-01-outbound-write.json` (only there).
Word lists: `.claude/gates/lexicon.json`.** This file explains how to satisfy them.

Two questions, answered by scripts and not by me:
1. **Am I allowed?** The owner's real messages are read from the transcript and classified
   by fixed word lists (B1–B4).
2. **Is every sentence true to a source I read in full, live?** Sources, versions, read
   times, completeness, quotes and counts are taken from the real tool results in the
   transcript (C1–C5, D1–D7, E1).

Nothing I type into a ledger is evidence by itself. A ledger only points at tool calls
(`tool_use_id`s). The script then looks at what those calls really returned.

## Enforcement

| Hook | What it blocks |
|---|---|
| `PreToolUse` (`scripts/hooks/pre_tool.py`) | Any Confluence / Jira / Slack write whose exact input is not the `payload_file` of a ledger that passes **now**. Any write through `mcp__Atlassian_Rovo__` (Backend Operations account). n8n writes without a standing WRITE order. Edits to gate files without `UNLOCK G-01` from the owner. |
| `PostToolUse` (`post_tool.py`) | Marks the order as used (one order = one write) and records what was sent. |
| `Stop` (`stop.py`) | Ending the turn while a changed draft fails G-01, or while a write has not been read back with every sent sentence present. |
| `UserPromptSubmit` (`prompt.py`) | Nothing is blocked. It prints what the owner's message authorises and whether step 0 is still missing. |

## Step 1: Order

Do nothing yourself. `python3 scripts/order_check.py --session` shows how each owner
message is classified. Only **WRITE** authorises an outbound write. **DRAFT** or WRITE
authorises a draft. **READONLY / AMBIGUOUS / STOP** means **ask**, and never guess.
Questions, "kalau…", "aku tulis…" and "kirim kesini" are READONLY on purpose.
A write order dies when the owner sends anything other than a plain "ya / ok / lanjut",
and after one write.

## Step 2: Find every related source

- For each topic term (the objects the text talks about), run a Confluence search with
  `space = NOSM`. If a Jira issue is involved, also run `listJiraIssueComments` on it.
  Fetch every page of every result (C2).
- Put the call ids in `discovery.calls` and the terms in `discovery.topic_terms` (C1).
- Every page, issue or comment the searches return is either a source or goes in
  `discovery.excluded` with a real reason (C3). "Not relevant" alone is too short.

## Step 3: Read every source to the end, live

| Source | Accepted read |
|---|---|
| Confluence page | `mcp__Atlassian_MCP__getConfluenceContent`, `detail=full` |
| Jira comments | `executeRead` `listJiraIssueComments` from `startAt` 0 to `isLast: true`; no `responseFields` that drop `comments.body` |
| Jira issue | `getJiraIssue` |
| Slack thread / n8n workflow | `slack_read_thread` / `get_workflow_details` |

- If a result was saved to a file, run `python3 scripts/read_source.py <tool_use_id> --info`
  and then every `--part k`. A slice read any other way counts as not read (C5).
- The read must be at most 60 min old for outbound and 12 h old for drafts. No later call
  in the transcript may show the page at another version (C4). If the page moved, read it again.
- Repo notes, earlier drafts, summaries and memory are **not** sources.

## Step 4: Ledger `docs/ledger/<write_id>.json`

Schema: `ledger_schema` in the gate file. Per claim:
- `text` is exactly the sentence(s) as they appear in the payload or draft. Every sentence
  needs a claim, clean boilerplate, or (for Confluence edits) must be text already on the page (D1).
- `quote` is copied from the source as read. The script finds it or refuses (D2).
- Any number goes in the quote. A quantity ("16 条", "tujuh project", "四处") must be stated
  as a quantity in the quote, or recounted by `counts: [{value, source_id, regex, section}]` (D3).
- Absence wording ("belum", "tidak ada", "未", "none") that the quote itself does not
  contain needs `absence: {pattern, searched: [2+ calls], control: {call, pattern}}` (D4).
- Near names (e.g. `PIP 参数` / `PIP Extension 参数`) and page codes (`04.10`) are used
  exactly as the quote or the source title has them (D5).
- If you cannot source a sentence, write it with 🔲 and say it is unverified, or leave it out.
- Never put a person's name next to fault wording (D7, `docs/working-agreement.md` rule 18).

Outbound: also save the exact tool input as `payload_file` and set `tool` and `target`.
Draft: `kind: draft`, `target: {system: draft, path}`; the draft file is the payload.

## Step 5: Gate

```
python3 scripts/gate_check.py docs/ledger/<write_id>.json
```
Exit 0 = PASS. The pre-tool hook runs it again at the moment of the call, against the
exact input. Fix the cause, never the gate.

## Step 6: After writing

Read the target again: full page read for Confluence, comment listing for Jira. The Stop
hook blocks until every sent sentence is found in that read-back.

## Related gates

- Chat answers: G-03 (`.claude/gates/G-03-chat-claims.json`), checked by the Stop hook.
- git / GitHub writes: G-04 (`.claude/gates/G-04-repo-write.json`), checked by the PreToolUse hook.
- Every other outward tool (Gmail, Supabase, Vercel, Claude_Code_Remote, Claude_Docs, Artifact publish,
  ArtifactData writes, ArtifactComments replies, and Bash commands that send data with curl / wget / http):
  G-05 (`.claude/gates/G-05-other-tools.json`) - each write needs its own write order from the owner
  (one order = one write, as G-01 B2).
- The hooks fail closed: if the pre-tool hook crashes, an outward call is held; if the Stop hook crashes, the
  turn is held until the hook is fixed or the owner types OVERRIDE G-03.

## What this still does not cover

The `known_limits` lists in the gate files: a quote read wrongly, the meaning of a chat sentence,
and word-list misclassification. If the hooks are not loaded, the gates only run when I run them by
hand. Say so when it matters. Do not describe the gate as stronger than it is.
