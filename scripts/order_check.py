#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Classify owner messages mechanically. The word lists live in .claude/gates/lexicon.json.

Classes:
  WRITE      explicit write verb, no check/draft verb, not negated -> may authorise ONE outbound write
  DRAFT      draft verb -> may authorise a draft file in docs/, never an outbound write
  READONLY   check / audit / read / anything else -> authorises nothing outside chat
  CONFIRM    a short "ya / ok / lanjut" -> keeps an earlier order standing
  STOP       stop word, or a write/draft verb that is negated ("jangan tulis") -> cancels earlier orders
  AMBIGUOUS  write verb together with a check/draft verb -> ask first

Why it exists: 2026-09-22 v39. The order was "Kau audit detail menyeluruh sampai habis";
it was treated as permission to write. 'audit' can never authorise a write here.

Usage:
  python3 scripts/order_check.py --text "<message>"
  python3 scripts/order_check.py --session        # classify every owner message in this session
Exit 0 = WRITE, 1 = anything else.
"""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nosm_lib as N


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--text')
    ap.add_argument('--session', action='store_true')
    ap.add_argument('--transcript')
    a = ap.parse_args()
    L = N.lexicon()
    if a.session:
        tr = N.Transcript(N.find_transcript(a.transcript))
        for p in tr.prompts:
            cls, _ = N.classify(p['text'], L)
            print('%s  %-9s  %s' % (p['ts'], cls, p['text'].replace('\n', ' ')[:90]))
        return 0
    cls, d = N.classify(a.text or '', L)
    print('message : %s' % (a.text or '').strip().replace('\n', ' ')[:120])
    for k in ('write', 'draft', 'readonly', 'stop', 'negated'):
        print('%-9s: %s' % (k, ', '.join(d[k]) or '-'))
    print('CLASS    : %s' % cls)
    return 0 if cls == 'WRITE' else 1


if __name__ == '__main__':
    sys.exit(main())
