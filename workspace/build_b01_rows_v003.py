#!/usr/bin/env python3
"""
build_b01_rows_v003.py -- B01 V003 inventory generator: 32 rows, every digest COMPUTED.

WHAT CHANGED FROM V002 (the four documentary repairs ruled at Q-920):
  (1) SPANS-REQUIRED.  Each S row is a ROW of the sealed prefreeze table, so its byte object is the
      ROW SPAN, not the containing file.  This script LOCATES each of the 26 rows in the sealed
      source, computes its half-open span and the span's SHA-256, and emits them per row.  V002
      emitted the shared document digest for all 26, which addresses the container and not the
      primitive.
  (4) INPUT CUSTODY.  spine_rows.json is now a DECLARED input, sealed with a sidecar, and this
      script BINDS its digest at run time.  It also DERIVES the check the confirm asked for: every
      JSON field is compared against the sealed source row it claims to come from, so the generated
      input is shown to carry the sealed table rather than merely to agree with it.  A mismatch is
      fatal -- the script refuses to emit a table it cannot ground.

DECLARED INPUTS (full paths from the alpha-program-archive root; nothing else is opened):
  workspace/STAGE8_FROZEN_PRIMITIVE_INVENTORY_PREFREEZE_RESULT_V001.md   the 26-row source table
  workspace/spine_rows.json                                              the row extract, now sealed
  workspace/<the six Level-1 authority files named in AUTH below>

Run from workspace/:   cd <archive-root>/workspace && python3 build_b01_rows_v003.py
"""

import hashlib
import json
import re
import sys

SPINE_SRC = 'STAGE8_FROZEN_PRIMITIVE_INVENTORY_PREFREEZE_RESULT_V001.md'
SPINE_JSON = 'spine_rows.json'


def sha_file(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def strip_citation(s):
    """Remove the source's trailing citation parenthetical, the one field difference the confirm
    identified.  Only a trailing group is removed; parentheses inside the primitive itself stay."""
    return re.sub(r'\s*\([^()]*(?:\([^()]*\)[^()]*)*\)\s*$', '', s).strip()


AUTH = [
    ("P-01", "FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md", "action / field-content rule", "microscopic theory premise", "Level-1 postulate (V010.json:25-30)"),
    ("P-02", "PRIMITIVE_VECTORLIKE_CHARGED_SOURCE_BRANCH_V003.md", "source-branch inventory", "source sector", "Level-1 postulate (V010.json:25-30)"),
    ("P-03", "PRIMITIVE_TRANSPORT_ONLY_PHASE_COMPLETE_GENERATOR_PRINCIPLE_V001.md", "generator-class rule", "transport/phase generators", "Level-1 postulate, adopted not derived (V010.json:25-30)"),
    ("P-04", "PRIMITIVE_SOURCE_RECORD_PAIRED_RETURN_IDENTIFICATION_PRINCIPLE_V002.md", "source-record identity hypothesis", "source-record pairing", "Level-1 postulate; derivation false per standing classification"),
    ("P-05", "BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md", "relative onset-saturation rule", "boundary record onset", "Level-1 postulate, adopted not derived (V013.json:31-34)"),
    ("P-06", "SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.md", "zero-flux / no-charged-write rule", "record write gate", "Level-1 postulate, adopted branch rule (V013.json:31-34)"),
]


def locate_source_rows(blob):
    """Return {n: (start, end)} for the 26 rows of the prefreeze section-2 table.

    A row span runs from its leading pipe THROUGH its terminating newline -- the convention the
    audit's own basis rows use and which B01 V002's pinned [32217,32292) fixes."""
    sec = blob.find(b'## 2. Bounded Value-Path Premise Inventory')
    if sec < 0:
        raise SystemExit('FATAL: section 2 heading not found in the sealed source')
    nxt = blob.find(b'\n## ', sec + 1)
    if nxt < 0:
        nxt = len(blob)
    spans = {}
    pos = sec
    while pos < nxt:
        eol = blob.find(b'\n', pos)
        if eol < 0 or eol >= nxt:
            break
        line = blob[pos:eol]
        m = re.match(rb'\| (\d+) \| ', line)
        if m:
            spans[int(m.group(1))] = (pos, eol + 1)
        pos = eol + 1
    return spans


def source_fields(blob, span):
    cells = blob[span[0]:span[1]].decode('utf-8').rstrip('\n').split('|')
    # leading and trailing empties from the outer pipes
    cells = [c.strip() for c in cells[1:-1]]
    return {'n': int(cells[0]), 'primitive': cells[1], 'kind': cells[2],
            'status': cells[3], 'presupposes': cells[4]}


def main():
    with open(SPINE_SRC, 'rb') as fh:
        blob = fh.read()
    spine_digest = hashlib.sha256(blob).hexdigest()
    json_digest = sha_file(SPINE_JSON)
    spans = locate_source_rows(blob)
    with open(SPINE_JSON) as fh:
        rows = json.load(fh)

    # ---- input-custody derivation: every declared JSON field must carry its sealed source row
    problems = []
    if len(rows) != 26:
        problems.append('spine_rows.json carries %d rows, expected 26' % len(rows))
    for r in rows:
        n = r['n']
        if n not in spans:
            problems.append('row %d has no source span' % n)
            continue
        src = source_fields(blob, spans[n])
        if strip_citation(src['primitive']) != r['primitive']:
            problems.append('row %d primitive: %r vs source %r' % (n, r['primitive'], src['primitive']))
        for f in ('kind', 'status', 'presupposes'):
            if src[f] != r[f]:
                problems.append('row %d %s: %r vs source %r' % (n, f, r[f], src[f]))
    if problems:
        sys.stderr.write('INPUT CUSTODY FAILED -- refusing to emit:\n  ' + '\n  '.join(problems) + '\n')
        return 2

    sys.stderr.write('INPUT CUSTODY: spine_rows.json %s\n' % json_digest)
    sys.stderr.write('  26/26 rows carry their sealed source row on all four compared fields\n')
    sys.stderr.write('  (primitive after trailing-citation removal; kind, status, presupposes exact)\n')
    sys.stderr.write('SOURCE: %s %s\n' % (SPINE_SRC, spine_digest))

    print("| id | primitive | mathematical type (kind) | domain (presupposes) | authority | status AS SOURCED | source span | byte digest |")
    print("|---|---|---|---|---|---|---|---|")
    for i, f, typ, dom, auth in AUTH:
        print("| `%s` | `%s` | %s | %s | %s | sealed authority row | whole file | `%s` |"
              % (i, f, typ, dom, auth, sha_file(f)))
    for r in sorted(rows, key=lambda r: r['n']):
        n = r['n']
        s, e = spans[n]
        span_digest = hashlib.sha256(blob[s:e]).hexdigest()
        print("| `S-%02d` | %s | %s | %s | prefreeze result section 2, row %d | **%s** | `[%d,%d)` | `%s` |"
              % (n, r['primitive'], r['kind'], r['presupposes'], n, r['status'], s, e, span_digest))
    return 0


if __name__ == '__main__':
    sys.exit(main())
