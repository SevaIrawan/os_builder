#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""nosm-sync-check step 4: every page in the docs/source-versions.md table is checked against its LIVE version.

docs/source-versions.md is a repo note, not a source (docs/working-agreement.md rule 6). It only says which pages
to check and what version was last recorded. The live version is taken from the session transcript: a
getConfluenceContent call on the page (any detail - summary carries the version) or a listConfluenceContentVersions
call, at most MAX_AGE_HOURS old. The model does not type any version.

Usage:  python3 scripts/sweep_check.py [--transcript <path>]
Exit 0 = every page with a pageId was checked live (moved pages are listed, not a failure).
Exit 1 = a page was not checked live in the window, or the table could not be read."""
import argparse, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nosm_lib as N

LEDGER = os.path.join(N.ROOT, 'docs', 'source-versions.md')
MAX_AGE_HOURS = 12
ROW_RE = re.compile(r'^\|\s*(?P<name>[^|]+?)\s*\|\s*(?P<id>\d{9,11})\s*\|\s*(?P<ver>[^|]*?)\s*\|')


def ledger_rows():
    rows = []
    with open(LEDGER, encoding='utf-8') as f:
        for line in f:
            m = ROW_RE.match(line)
            if m:
                v = re.search(r'v(\d+)', m.group('ver'))
                rows.append((m.group('name'), m.group('id'), int(v.group(1)) if v else None))
    return rows


def run(tr, L=None, now=None):
    """(ok, lines)."""
    L = L or N.lexicon()
    now = now or N.now_utc()
    rows = ledger_rows()
    if not rows:
        return False, ['no rows with a pageId found in %s' % N.rel(LEDGER)]
    out, missing, moved = [], [], []
    for name, pid, rec in rows:
        seen = [(s, v, c) for s, v, c in N.page_versions_seen(tr, pid, L)
                if (now - N.parse_ts(c.ts)).total_seconds() / 3600 <= MAX_AGE_HOURS]
        if not seen:
            missing.append(pid)
            out.append('  NOT CHECKED  %s  %s  (recorded v%s)' % (pid, name, rec))
            continue
        live, call = seen[-1][1], seen[-1][2]
        if rec is not None and live != rec:
            moved.append(pid)
            out.append('  MOVED        %s  %s  recorded v%s -> live v%s  (%s)' % (pid, name, rec, live, call.id))
        else:
            out.append('  same         %s  %s  v%s  (%s)' % (pid, name, live, call.id))
    out.append('pages with a pageId: %d; checked live: %d; moved: %d; not checked: %d'
               % (len(rows), len(rows) - len(missing), len(moved), len(missing)))
    if missing:
        out.append('VERDICT: NOT DONE - read each NOT CHECKED page live (getConfluenceContent detail=summary) and run again')
        return False, out
    out.append('VERDICT: every page checked live' + (' - MOVED pages need their diff read and a fresh full read before use' if moved else ''))
    return True, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--transcript')
    a = ap.parse_args()
    tr = N.Transcript(N.find_transcript(a.transcript))
    ok, lines = run(tr)
    print('=' * 66); print('nosm-sync-check  step 4  live versions of the source-versions table'); print('=' * 66)
    print('\n'.join(lines))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
