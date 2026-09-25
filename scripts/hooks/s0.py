# -*- coding: utf-8 -*-
"""Session start on "hi" (docs/working-agreement.md rule 23). Rules: G-01-outbound-write.json "session_start".

check(tr, L) -> problems (empty = the turn may end). Only applies when the owner's latest message
starts with "hi"; then every item must appear in the transcript AFTER that message."""
import re
from _common import N
import sweep_check, sync_check

HI = re.compile(r'^\s*hi\b', re.I)
SKILL_PAGE, NAV_PAGE, ROUTER_PAGE = '1730347066', '1676804100', '1691254793'


def check(tr, L):
    if not tr.prompts or not HI.match(tr.prompts[-1]['text']):
        return []
    t0 = N.parse_ts(tr.prompts[-1]['ts'])
    after = [c for c in tr.ordered() if not c.is_error and N.parse_ts(c.ts) and t0 and N.parse_ts(c.ts) > t0]
    probs = []

    def need(ok, item, what):
        if not ok:
            probs.append('%s: %s' % (item, what))

    need(any((c.name == 'Read' and str(c.input.get('file_path', '')).endswith('docs/working-agreement.md')) or
             (c.name == 'Bash' and 'docs/working-agreement.md' in c.input.get('command', '')) for c in after),
         'S0-0', 'docs/working-agreement.md not read since the owner\'s "hi"')
    need(any(c.name.startswith('mcp__Atlassian_MCP__') for c in after), 'S0-1', 'no successful Atlassian_MCP call since "hi"')
    need(any(c.name.startswith('mcp__Atlassian_Rovo__get') or c.name.startswith('mcp__Atlassian_Rovo__search') for c in after),
         'S0-1', 'no successful Atlassian_Rovo read since "hi" (CLAUDE.md §〇 item 2)')
    need(any(c.name in L['tools']['n8n_list'] for c in after), 'S0-1', 'no successful n8n search_workflows since "hi"')

    full = {}
    for c in after:
        if N.is_full_page_read(c, L) and N.call_content_id(c) in (SKILL_PAGE, NAV_PAGE, ROUTER_PAGE):
            ok, _ = N.fully_read(tr, c)
            if ok:
                full[N.call_content_id(c)] = c
    for p in (SKILL_PAGE, NAV_PAGE):
        need(p in full, 'S0-2', 'page %s not read in full (and to the end) since "hi"' % p)
    if SKILL_PAGE in full and NAV_PAGE in full:
        ok, lines = sync_check.run(tr, L)
        need(ok, 'S0-2', 'sync_check does not pass: %s' % (lines[-1] if lines else ''))

    need(any(c.name in L['tools']['confluence_search'] and 'lastmodified' in str(c.input).lower() and 'NOSM' in str(c.input)
             for c in after), 'S0-3', 'no space-wide lastmodified sweep since "hi"')
    try:
        rows = sweep_check.ledger_rows()
    except OSError:
        rows = []
    seen_after = {N.call_content_id(c) for c in after
                  if c.name in L['tools']['confluence_page_read'] or
                  (c.name == L['tools']['execute_read'] and c.input.get('name') == 'listConfluenceContentVersions')}
    missing = [pid for _, pid, _ in rows if pid not in seen_after]
    need(rows and not missing, 'S0-3', '%d page(s) of docs/source-versions.md not read live since "hi": %s'
         % (len(missing), ', '.join(missing[:8]) + (' ...' if len(missing) > 8 else '')) if rows else
         'docs/source-versions.md table unreadable')
    need(ROUTER_PAGE in full, 'S0-4', '04.7 (%s) not read in full since "hi" (CLAUDE.md §〇 acceptance)' % ROUTER_PAGE)
    return probs
