---
name: nosm-sync-check
description: Step 0 of every NOSM / BO session. Proves the connectors are live, the two controlled copies (CLAUDE.md, docs/04-anchor-navigation.md) match their Confluence sources, and the whole NOSM space was swept for pages that moved. The G-01 gate refuses every draft and outbound write until this has run in the last 12 hours.
---

# NOSM Sync Check (pipeline step 0)

The order of work, the rules and the checks are defined once, in
`.claude/gates/G-01-outbound-write.json`. This skill is step 0 of that pipeline. It does
not restate the rules. It says what to run.

`CLAUDE.md` is a controlled deployment copy of 07.06 (`1730347066`), and
`docs/04-anchor-navigation.md` is an index of 04 (`1676804100`). If a copy and its source
disagree, **stop and report 部署漂移 (deployment drift)**. Never work from a stale copy.

## When

- First action of a session before any NOSM / S-05 work. The UserPromptSubmit hook reminds
  you when it has not run in the last 12 h.
- Again whenever a draft or an outbound write is due and the last run is older than 12 h.
  Gate checks A1–A3 refuse otherwise.

## Steps, in this order

0. **Read the working agreement first**: `docs/working-agreement.md` — the owner's
   working rules, the only place they are written (24 rules in six parts: understanding
   the order; sources and truth; write authority; writing to other people; how to speak
   to the owner; session start). Read the whole file every session. It is not a
   Confluence copy, so it is not subject to the drift rule — but it governs how the rest
   of this skill and all BO work is carried out. Read it before the connector checks,
   not after. If it seems to conflict with CLAUDE.md or the gate files, stop and ask
   the owner.

1. **Connectors** (gate A1)
   - Atlassian: any successful `mcp__Atlassian_MCP__` read.
   - n8n: `mcp__n8n__search_workflows`.
   - If either fails, stop and report. Do not compare anything against sources you cannot reach.

2. **Read both sources in full** (gate A2 input)
   - `mcp__Atlassian_MCP__getConfluenceContent` with `content_id=1730347066` and then
     `1676804100`, both `detail=full`, `content_format=markdown`.
   - Rovo `getConfluencePage` does not count: it carries no version number.
   - If a result is saved to a file, read every part with
     `python3 scripts/read_source.py <tool_use_id> --part k`. Anything less counts as not read.

3. **Compare mechanically** (gate A2)
   ```
   python3 scripts/sync_check.py
   ```
   The script takes both page bodies from the transcript. You do not save or type them. It
   finds the sections by heading text and compares bullets, preamble, the 冻结要求 paragraph,
   and for each table the column count, header and every row.
   Report the exit code and the output, not an impression.

4. **Sweep the whole space** (gate A3)
   - Run `mcp__Atlassian_MCP__searchConfluence` with
     `cql = space = NOSM AND type = page AND lastmodified >= "<previous sweep date>" order by lastmodified desc`.
     Fetch every page of results.
   - For each hit that `docs/source-versions.md` lists, run `listConfluenceContentVersions`,
     and where it moved, `diffConfluenceContentVersions`. The version message is a hint, not
     the change.
   - Update `docs/source-versions.md` with what changed, citing the call you read it from.
   - A page that moved is not "known" because its number is recorded. Any claim that uses
     it needs a fresh full read, and gate C4 enforces that from the transcript.

5. **Report two results, never merged into one "all in sync"**
   - (a) controlled copies: script exit code, and the page versions it compared;
   - (b) sweep: how many pages moved, which ones the ledger lists, what changed in them.
   - Drift found: quote the delta, copy the source text verbatim into the local file, commit,
     push, tell the owner. Do not paraphrase.
   - Source unreachable: stop. Do not fall back to the local copy.

## Non-goals

- It does not interpret the rules. The Confluence pages own them.
- It does not replace reading the page a task depends on. The gate demands that per source (C4, C5).
- It never writes to Confluence, Jira, Slack or n8n.
