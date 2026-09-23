#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Print a tool result that was too large to arrive inline, one part at a time.

The harness saves oversized tool results to a file and shows only a notice. Reading a
slice of that file and treating it as the whole page is exactly the "read part of it and
assume the rest" failure. This script is the only accepted way to read such a result:
each part ends with an END marker, and the gate counts a source as fully read only when
every part's END marker is present in the transcript.

Usage:
  python3 scripts/read_source.py <tool_use_id> --info
  python3 scripts/read_source.py <tool_use_id> --part <k>
"""
import argparse, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nosm_lib as N


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('call_id')
    ap.add_argument('--part', type=int)
    ap.add_argument('--info', action='store_true')
    ap.add_argument('--transcript')
    a = ap.parse_args()
    tr = N.Transcript(N.find_transcript(a.transcript))
    call = tr.calls.get(a.call_id)
    if not call:
        print('unknown tool_use_id %s' % a.call_id); return 1
    txt = N.readable(call)
    m, sha = N.parts_needed(txt), N.text_sha(txt)
    if a.info or not a.part:
        print('tool=%s chars=%d parts=%d sha=%s persisted=%s' % (call.name, len(txt), m, sha, bool(call.persisted)))
        print('read every part: ' + ' ; '.join('--part %d' % k for k in range(1, m + 1)))
        return 0
    if not 1 <= a.part <= m:
        print('part must be 1..%d' % m); return 1
    s = (a.part - 1) * N.CHUNK
    print('<<<BEGIN %s PART %d/%d sha=%s chars %d-%d of %d>>>' % (a.call_id, a.part, m, sha, s, min(s + N.CHUNK, len(txt)), len(txt)))
    print(txt[s:s + N.CHUNK])
    print(N.end_marker(a.call_id, a.part, m, sha))
    return 0


if __name__ == '__main__':
    sys.exit(main())
