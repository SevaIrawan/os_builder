#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""nosm-sync-check: mechanical comparison of the two controlled copies.

  CLAUDE.md section 一           vs  07.06 (1730347066) section 「流程建设 Skill（正式原文）」
  docs/04-anchor-navigation.md   vs  04 (1676804100) tables 「按工作读取」「登记集」「子页地图」

The live source text is NOT typed or saved by the model. It is taken from the latest
full read of each page in the session transcript (getConfluenceContent, detail=full),
which must be at most MAX_AGE_HOURS old. Sections are located by heading text, not by number.

Usage:  python3 scripts/sync_check.py [--transcript <path>]
Exit 0 = no deployment drift. Exit 1 = drift, or the source read is missing / stale.
"""
import argparse, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nosm_lib as N

SKILL_PAGE, NAV_PAGE = '1730347066', '1676804100'
MAX_AGE_HOURS = 12


def latest_full_read(tr, page, L):
    best = None
    for c in tr.ordered():
        if N.call_content_id(c) == page and N.is_full_page_read(c, L):
            best = c
    return best


def section(body, heading_contains):
    """Text from the '# ' heading containing the phrase to the next '# ' heading."""
    lines = body.split('\n')
    out, on = [], False
    for ln in lines:
        if re.match(r'^# ', ln):
            if on:
                break
            on = heading_contains in ln
            continue
        if on:
            out.append(ln)
    return '\n'.join(out) if on or out else None


def norm(s):
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
    s = s.replace('**', '').replace('`', '').replace('\\', '')
    return re.sub(r'\s+', '', s)


def bullets(t):
    return [norm(l[2:]) for l in t.split('\n') if l.startswith('- ') or l.startswith('* ')]


def tables(txt):
    out, cur = [], None
    for ln in txt.split('\n'):
        if ln.strip().startswith('|'):
            cells = ln.strip().strip('|').split('|')
            if set(''.join(cells).replace(' ', '')) <= set('-:'):
                continue
            if cur is None:
                cur = []
            cur.append([norm(c) for c in cells])
        elif cur:
            out.append(cur); cur = None
    if cur:
        out.append(cur)
    return out


def cmp_list(name, S, Lc, fails, out):
    if len(S) != len(Lc):
        out.append('  %-24s count: source=%d local=%d  *** DIFFERENT ***' % (name, len(S), len(Lc))); fails.append(name)
    bad = 0
    for i, (a, b) in enumerate(zip(S, Lc), 1):
        if a != b:
            bad += 1
            out.append('    *** ITEM %d DIFFERS ***' % i)
            for j in range(min(len(a), len(b))):
                if a[j] != b[j]:
                    out.append('      source: ...%s...' % a[max(0, j - 40):j + 40])
                    out.append('      local : ...%s...' % b[max(0, j - 40):j + 40]); break
            else:
                out.append('      length differs: source=%d local=%d' % (len(a), len(b)))
    if bad:
        fails.append(name)
    out.append('  %-24s identical: %d/%d' % (name, len(S) - bad, len(S)))


def run(tr, L=None, now=None):
    """Returns (ok, lines). Used by this script and by the gate."""
    L = L or N.lexicon()
    now = now or N.now_utc()
    out, fails = [], []
    reads = {}
    for page in (SKILL_PAGE, NAV_PAGE):
        c = latest_full_read(tr, page, L)
        if not c:
            return False, ['no full read (getConfluenceContent detail=full) of page %s in this session' % page]
        age = (now - N.parse_ts(c.ts)).total_seconds() / 3600
        if age > MAX_AGE_HOURS:
            return False, ['latest full read of page %s is %.1f h old (%s); limit %d h - read it again' % (page, age, c.ts, MAX_AGE_HOURS)]
        ok, why = N.fully_read(tr, c)
        if not ok:
            return False, ['page %s: %s' % (page, why)]
        reads[page] = c
        out.append('source %s  v%s  read %s  (%s)' % (page, N.confluence_version(c), c.ts, c.id))

    body = reads[SKILL_PAGE].json()['data']['body']['value']
    src = section(body, '流程建设 Skill（正式原文）')
    if not src:
        return False, out + ['heading 「流程建设 Skill（正式原文）」 not found in 07.06']
    with open(os.path.join(N.ROOT, 'CLAUDE.md'), encoding='utf-8') as f:
        cm = f.read()
    sec = cm[cm.index('## 一、流程建设 Skill'):cm.index('## 二、快速索引')]
    out.append('[1] CLAUDE.md section 一  vs  07.06 「流程建设 Skill（正式原文）」')
    cmp_list('bullets', bullets(src), bullets(sec), fails, out)
    p_s = norm(src.strip().split('\n\n')[0])
    p_l = norm(sec[sec.index('本节是「流程建设 Skill」的唯一规范源'):sec.index('### 流程建设 skill')])
    out.append('  %-24s %s' % ('preamble', 'same' if p_s == p_l else '*** DIFFERENT ***'))
    if p_s != p_l:
        fails.append('preamble')
    f_s = norm(src.split('开发入口的冻结要求', 1)[1]).rstrip('-')
    f_l = norm(sec.split('开发入口的冻结要求', 1)[1]).rstrip('-')
    out.append('  %-24s %s' % ('开发入口的冻结要求', 'same' if f_s == f_l else '*** DIFFERENT ***'))
    if f_s != f_l:
        fails.append('开发入口的冻结要求')

    nbody = reads[NAV_PAGE].json()['data']['body']['value']
    blocks = {}
    for key, phrase in (('A', '按工作读取'), ('B', '登记集'), ('C', '子页地图')):
        s = section(nbody, phrase)
        t = tables(s or '')
        if not t:
            return False, out + ['no table under the heading containing 「%s」 in 04' % phrase]
        blocks[key] = t[0]
    with open(os.path.join(N.ROOT, 'docs', '04-anchor-navigation.md'), encoding='utf-8') as f:
        loc = tables(f.read())
    pairs = [('A 一 动作路由', blocks['A'], loc[0]), ('B 五 登记集', blocks['B'], loc[2]), ('C 六 子页地图', blocks['C'], loc[1])]
    out.append('[2] docs/04-anchor-navigation.md  vs  04')
    for nm, S, Lc in pairs:
        out.append('  --- %s ---' % nm)
        same_cols = len(S[0]) == len(Lc[0])
        out.append('  %-24s source=%d local=%d  %s' % ('column count', len(S[0]), len(Lc[0]), 'same' if same_cols else '*** DIFFERENT ***'))
        if not same_cols:
            fails.append(nm + '/columns')
        out.append('  %-24s %s' % ('header', 'same' if S[0] == Lc[0] else '*** DIFFERENT ***'))
        if S[0] != Lc[0]:
            fails.append(nm + '/header')
        cmp_list('rows', S[1:], Lc[1:], fails, out)
    if fails:
        out.append('VERDICT: DEPLOYMENT DRIFT in %s -> stop, do not work from a stale copy' % ', '.join(fails))
        return False, out
    out.append('VERDICT: no deployment drift')
    return True, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--transcript')
    a = ap.parse_args()
    tr = N.Transcript(N.find_transcript(a.transcript))
    ok, lines = run(tr)
    print('=' * 66); print('nosm-sync-check  controlled copies'); print('=' * 66)
    print('\n'.join(lines))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
