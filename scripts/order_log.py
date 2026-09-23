#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Daftar perintah — append-only. Satu perintah = satu baris JSON.
Klasifikasi diisi oleh scripts/order_check.py, BUKAN oleh model.

  python3 scripts/order_log.py --add --verbatim "<kalimat Bambang apa adanya>" --target "confluence:2096463922"
  python3 scripts/order_log.py --list
  python3 scripts/order_log.py --consume <order_id> --by <write_id>
"""
import argparse, json, os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from order_check import classify

PATH = 'docs/orders/orders.jsonl'

def rows():
    if not os.path.exists(PATH): return []
    return [json.loads(l) for l in open(PATH, encoding='utf-8') if l.strip()]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--add', action='store_true'); ap.add_argument('--verbatim')
    ap.add_argument('--target'); ap.add_argument('--list', action='store_true')
    ap.add_argument('--consume'); ap.add_argument('--by')
    a = ap.parse_args()

    if a.add:
        if not a.verbatim or not a.target:
            print('--verbatim dan --target wajib'); return 2
        kind, w, r, why = classify(a.verbatim)
        R = rows()
        rec = {
            'order_id': 'O-%s-%02d' % (datetime.date.today().isoformat(), len(R) + 1),
            'received_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'verbatim': a.verbatim, 'target': a.target,
            'classified': kind, 'write_verbs': w, 'readonly_verbs': r, 'why': why,
            'consumed_by': None,
        }
        os.makedirs(os.path.dirname(PATH), exist_ok=True)
        with open(PATH, 'a', encoding='utf-8') as f:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
        print('%s  %s' % (rec['order_id'], kind)); print(why)
        return 0

    if a.list:
        for x in rows():
            print('%-18s %-9s consumed=%-12s %s' % (
                x['order_id'], x['classified'], x['consumed_by'] or '-', x['verbatim'][:56].replace('\n', ' ')))
        return 0

    if a.consume:
        R = rows(); hit = False
        for x in R:
            if x['order_id'] == a.consume:
                if x['consumed_by']:
                    print('SUDAH dipakai oleh %s — satu perintah satu tulisan' % x['consumed_by']); return 1
                x['consumed_by'] = a.by; hit = True
        if not hit: print('order_id tidak ada'); return 1
        with open(PATH, 'w', encoding='utf-8') as f:
            for x in R: f.write(json.dumps(x, ensure_ascii=False) + '\n')
        print('%s -> dipakai oleh %s' % (a.consume, a.by)); return 0

    ap.print_help(); return 2

if __name__ == '__main__':
    sys.exit(main())
