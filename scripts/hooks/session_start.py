#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SessionStart hook. States the fixed order of work for this repo."""
print('[G-01] Before any NOSM / S-05 work: run skill nosm-sync-check (connectors, scripts/sync_check.py, space sweep). '
      'Outbound writes and drafts are enforced by hooks against .claude/gates/G-01-outbound-write.json. '
      'Nothing is written to Confluence / Jira / Slack / n8n without a WRITE order from the owner.')
