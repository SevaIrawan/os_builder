# Working Rules for Claude in This Repo

> **Nature**: internal note. **Carries no authority of its own.** It records instructions
> already given by the repo owner and rules that already live in authoritative sources
> (`CLAUDE.md`, `.claude/skills/*`, and the Confluence pages those point to). It does not
> create rules. Where it disagrees with an authoritative source, the source wins.
>
> `CLAUDE.md` is a controlled deployment copy of Confluence 07.06 §8 and must not carry
> additions, which is why these standing instructions live here instead.

---

## Standing instruction from the repo owner (2026-09-20)

Recorded because this is a large project and sessions do not carry memory.

1. **Obey every rule already in force** — whatever is in memory/preferences, in the task
   as given, in the skills under `.claude/skills/`, and in `CLAUDE.md`. None of these is
   optional, and familiarity is not a reason to skip a step.

2. **Analyse from facts and reference documents only.** Not from assumption, not from
   personal initiative, not from personal creativity. If a claim cannot be traced to a
   source that was actually opened and read, it does not go in a conclusion.

3. **Read every source and document through to the end before concluding or reporting.**
   No guessing, no extrapolating from a partial read. If part of a source was not read in
   full, say so explicitly and name which part, rather than reporting as if it had been.

## What these mean in practice here

- A finding is reported **to the repo owner and stops there.** Deciding whose concern it
  is, which channel it should go to, or preparing it for anyone else is not Claude's to
  do unless the owner asks. (Source: owner instruction, 2026-09-20; consistent with
  `CLAUDE.md` §1, which has gap reports handed to the user to forward unchanged.)
- Nothing outside this repo is written to without an explicit instruction — no Confluence
  edit, no Slack message, no Jira comment, no n8n change. Reading is fine; writing is not.
- A skill's declared scope is a boundary, not a starting point. `nosm-sync-check` compares
  the local copies against their sources; checking whether two source pages agree with
  each other is outside it.
- Nothing is added to `CLAUDE.md` or `docs/04-anchor-navigation.md` that its source page
  does not contain. Adding a row the source lacks is inventing a standard, which
  `CLAUDE.md` §1 forbids outright.
- Every factual claim reported cites where it came from: pageId and the version or
  lastModified as read, Jira comment id, n8n workflow id, or the API call that returned it.

## Known gap in this session's reading (kept so it is not silently forgotten)

OSD-116 has 151 comments. All human comments were read verbatim. Of the Bot_SSC machine
audit reports, rounds 1–6, 9 and 10 (including their 裁决准备包) were read in full;
round 7 was read in part, and rounds 8 and 11–16 were read only as header plus the
`机器退回项` section. Those rounds' `待人工裁决` tables were not read line by line. They
repeat items already ruled on — a point Kayden makes himself in c49471 — but they were
not read in full, and no conclusion here rests on them.
