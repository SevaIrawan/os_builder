#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PostToolUse hook for Bash / Write / Edit. A program can change a gate file without its path
appearing in the command, so after every such call the gate files are compared with the sealed
copy (_guard.py). Without UNLOCK G-01 in the owner's latest message, any change is put back and
reported (exit 2: the message is shown to Claude). With UNLOCK G-01 the new state is sealed."""
import sys
from _common import N, read_input, transcript, deny, latest_owner_text
import _guard


def main():
    inp = read_input()
    L = N.lexicon()
    put_back = _guard.enforce(L, lambda tok: tok in latest_owner_text(transcript(inp)))
    if put_back:
        deny(_guard.message(put_back, L))
    return 0


if __name__ == '__main__':
    sys.exit(main())
