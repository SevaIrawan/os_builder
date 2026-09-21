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

## Standing instruction from the repo owner (2026-09-21) — drafting comments

**Never accuse, blame, or report a person.** This binds every draft written here for sending to a
Jira comment, a Confluence comment, Slack, or anywhere else. Mutual blame is not permitted.

What it forbids in a draft:

- Naming a person as the cause of a gap, an error, a delay, or a missing row.
- Wording that reads as fault even without the word — "X never did", "X failed to", "X's mistake",
  "this was missed by X", "X is late".
- Carrying one person's error to a third party. If something is wrong, it is stated as a fact about
  the object, not reported about the person who produced it.
- Framing our own correction as someone else's failing.

What it still allows, because it is attribution of a statement and not of blame:

- Citing who ruled or answered what, with the comment id — "Kent c50255 ruled Option C",
  "Felix c50261 gave both names". That is the evidence trail every rule in `CLAUDE.md` §1 requires.
- Naming the Owner of a page or an object when the question is who decides, not who is at fault.

How to write it instead: state the fact, cite the source, say what is needed and from whom, and stop.
The object is wrong or missing — that is the sentence. Who produced it is not part of it.

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

## Reading-coverage record for OSD-116 (closed 2026-09-20)

OSD-116 has 151 comments. All were read in full.

- All human comments (Kayden, Alden, Kent, Felix_HR, Zq, Yuki Liew_HR, Bambang): read
  verbatim.
- All Bot_SSC machine audit reports and 裁决准备包: read in full. Rounds 1-6, 9 and 10
  were read first; rounds 7, 8 and 11-16 (comments c49270, c49271, c49318, c49320,
  c49321, c49340, c49345, c49350, c49351, c49399, c49400, c49411, c49412, c49461,
  c49462, c49473, c49474) were read in full afterwards, on the owner's instruction.

No part of OSD-116 is now unread.
