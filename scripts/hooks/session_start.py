#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SessionStart hook. States the fixed order of work for this repo.
The G-01 paragraph below lived in CLAUDE.md until 2026-09-25; CLAUDE.md is a controlled copy of
07.06 and must not carry additions (docs/working-agreement.md rule 14), so it is printed here instead."""
print('[G-01] Before any NOSM / S-05 work: run skill nosm-sync-check (connectors, scripts/sync_check.py, space sweep). '
      'Outbound writes and drafts are enforced by hooks against .claude/gates/G-01-outbound-write.json. '
      'Nothing is written to Confluence / Jira / Slack / n8n without a WRITE order from the owner.')
print('[Rules] The owner\'s working rules are in docs/working-agreement.md (the only place they are written); '
      'read it in full as step 0 of nosm-sync-check. Open work is only in docs/action-list.md. '
      'The only branch of this repo is main.')
print('**Enforced order of work (G-01). Rules: `.claude/gates/G-01-outbound-write.json`, the only place they are written.**\n'
      'Step 0 is skill `nosm-sync-check`. Steps 1-6 are skill `outbound-write-gate`: order, find every related source, '
      'read every source to the end, claims ledger, `scripts/gate_check.py`, read-back.\n'
      'Hooks in `.claude/settings.json` enforce them. A Confluence / Jira / Slack write is blocked unless its exact input '
      'belongs to a ledger that passes the gate at that moment. A write through the Backend Operations account '
      '(`mcp__Atlassian_Rovo__`) is always blocked. A turn cannot end while a changed draft in `docs/` fails the gate, '
      'or while a write has not been read back.\n'
      'Evidence is taken from the session transcript (the owner\'s real messages and the real tool results), '
      'never from what the model types.\n'
      'The nosm-sync-check report keeps its two results apart: (a) the two controlled copies, (b) the space-wide sweep. '
      '(a) passing says nothing about (b).\n'
      'Only the owner can type `OVERRIDE G-01` (let one blocked write through) or `UNLOCK G-01` (change gate files).\n'
      'Chat answers are checked by the Stop hook against G-03 (`.claude/gates/G-03-chat-claims.json`): ids, versions, dates, '
      'numbers, `code` and quotes must come from a tool result of this session; outside-system facts from a live read of that '
      'system; absence claims need a verified token or the \U0001F532 marker. A held answer is corrected with a message '
      'starting "Koreksi". Its limits are listed in that file.\n'
      'Git and GitHub writes are gated by G-04 (`.claude/gates/G-04-repo-write.json`): commit / push need "commit push", '
      'deleting branches / commits / history needs "hapus", in the owner\'s latest message.\n'
      'Every other outward tool (Gmail, Supabase, Vercel, Claude_Code_Remote, Claude_Docs, Artifact publish) is gated by '
      'G-05 (`.claude/gates/G-05-other-tools.json`): a write needs a write order. The hooks fail closed on a crash. '
      'docs/working-agreement.md, CLAUDE.md and docs/04-anchor-navigation.md are gate-protected (UNLOCK G-01).')
