#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UserPromptSubmit hook. Prints, as context for this turn, what the owner's message
authorises (mechanical classification) and which session prerequisites are still missing."""
import sys
from _common import N, read_input, transcript
import gate_check, sync_check


def main():
    inp = read_input()
    L = N.lexicon()
    cls, d = N.classify(inp.get('prompt', ''), L)
    meaning = {
        'WRITE': 'may authorise ONE outbound write, only through a ledger that passes G-01',
        'DRAFT': 'authorises a draft file in docs/ (ledger must pass G-01), never an outbound write',
        'READONLY': 'authorises NO write outside the repo. Read, check and report only',
        'CONFIRM': 'keeps the previous order standing, adds nothing',
        'STOP': 'cancels standing orders. Do not write anything outward',
        'AMBIGUOUS': 'mixes write and check/draft words: ASK the owner before any write',
    }[cls]
    lines = ['[G-01] Owner message classified %s: %s.' % (cls, meaning)]
    try:
        tr = transcript(inp)
        now = N.now_utc()
        ok, why = sync_check.run(tr, L, now)
        if not ok:
            lines.append('[G-01] nosm-sync-check not satisfied: %s. Run skill nosm-sync-check before NOSM work.' % why[-1])
        sweep = [c for c in tr.ordered() if c.name in L['tools']['confluence_search'] and not c.is_error
                 and 'lastmodified' in gate_check.query_text(c).lower() and gate_check.age_min(c.ts, now) <= 720]
        if not sweep:
            lines.append('[G-01] No space-wide lastmodified sweep in the last 12 h (nosm-sync-check step 6).')
    except SystemExit:
        pass
    lines.append('[G-01] Rules: .claude/gates/G-01-outbound-write.json. Any number, absence or name you state in chat '
                 'must come from a source read in full in this session; otherwise say it is unverified.')
    print('\n'.join(lines))
    return 0


if __name__ == '__main__':
    sys.exit(main())
