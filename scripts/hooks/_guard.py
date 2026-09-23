# -*- coding: utf-8 -*-
"""Sealed copy of the gate files (lexicon.json protected_paths).

A command that names a gate file is refused by pre_tool.py before it runs. A program that
writes a gate file without its path appearing in the command cannot be seen in advance, so
every hook compares the gate files with the sealed copy instead:
  - owner's latest message has UNLOCK G-01  -> the current state is sealed (accepted);
  - otherwise any difference                -> the sealed content is put back, the call is refused.
The hooks themselves update the sealed copy for the two files they write (draft registry,
consumed.jsonl) right after writing them.

The sealed copy lives outside the repo (G01_STATE_DIR, default ~/.claude/g01-state/<repo>).
It runs as the same OS user as the model, so it stops accidents and shortcuts, not a
deliberate attack on the state directory itself (see known_limits in the gate file)."""
import base64, hashlib, json, os
from _common import N

STATE_MARKER = 'g01-state'


def state_dir():
    d = os.environ.get('G01_STATE_DIR') or os.path.join(
        os.path.expanduser('~'), '.claude', STATE_MARKER, hashlib.sha256(N.ROOT.encode()).hexdigest()[:12])
    os.makedirs(d, exist_ok=True)
    return d


def baseline_path():
    return os.path.join(state_dir(), 'baseline.json')


def protected_files(L):
    """Every file under the protected paths that exists now (repo-relative)."""
    out = set()
    for p in L['protected_paths']:
        full = os.path.join(N.ROOT, p)
        if p.endswith('/'):
            for base, dirs, files in os.walk(full):
                dirs[:] = [d for d in dirs if d != '__pycache__']
                for fn in files:
                    if not fn.endswith('.pyc'):
                        out.add(N.rel(os.path.join(base, fn)))
        elif os.path.isfile(full):
            out.add(p)
    return out


def _read(rel):
    with open(os.path.join(N.ROOT, rel), 'rb') as f:
        return f.read()


def load():
    try:
        with open(baseline_path(), encoding='utf-8') as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def _save(base):
    tmp = baseline_path() + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(base, f)
    os.replace(tmp, baseline_path())


def seal(L, only=None):
    """Accept the current content of the gate files (all of them, or only the listed paths)."""
    base = load() or {}
    for rel in (only if only is not None else protected_files(L) | set(base)):
        full = os.path.join(N.ROOT, rel)
        if os.path.isfile(full):
            data = _read(rel)
            base[rel] = {'sha': hashlib.sha256(data).hexdigest(), 'b64': base64.b64encode(data).decode()}
        else:
            base.pop(rel, None)
    _save(base)


LEXICON = '.claude/gates/lexicon.json'


def sealed_lexicon(base, fallback):
    try:
        return json.loads(base64.b64decode(base[LEXICON]['b64']).decode('utf-8'))
    except (KeyError, ValueError, TypeError):
        return fallback


def differences(L, base):
    out = []
    for rel in sorted(protected_files(L) | set(base)):
        full = os.path.join(N.ROOT, rel)
        want = base.get(rel)
        have = hashlib.sha256(_read(rel)).hexdigest() if os.path.isfile(full) else None
        if (want and want['sha']) != have:
            out.append((rel, want, have))
    return out


def enforce(L, is_unlocked):
    """Compare the gate files with the sealed copy. Returns the paths put back ([] = nothing to do).
    is_unlocked(token) is only called when something differs (it reads the transcript, which is slow).
    No sealed copy yet (first hook of a fresh clone) -> the current state is sealed."""
    base = load()
    if base is None:
        seal(L)
        return []
    current, L = L, sealed_lexicon(base, L)   # a changed lexicon must not shrink the list of what is protected
    diff = differences(L, base)
    if not diff:
        return []
    if is_unlocked(L['order_words']['unlock_token']):
        seal(current)                # owner-approved: the lexicon as it is now decides what is sealed
        return []
    put_back = []
    for rel, want, have in diff:
        full = os.path.join(N.ROOT, rel)
        if want is None:
            os.remove(full)
            put_back.append(rel + ' (new file removed)')
        else:
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, 'wb') as f:
                f.write(base64.b64decode(want['b64']))
            put_back.append(rel + (' (deleted, put back)' if have is None else ' (changed, put back)'))
    return put_back


def message(put_back, L):
    return ('G-01: gate files were changed outside the hooks without "%s" in the owner\'s latest message, '
            'and have been put back from the sealed copy:\n- %s\nDo not change gate files; ask the owner.'
            % (L['order_words']['unlock_token'], '\n- '.join(put_back)))
