#!/usr/bin/env python3
"""
build_b01_carriage_remainder_v001.py -- regenerate the B01 V002->V003 carriage remainder FROM THE
SEALED MANIFEST, with no diff algorithm anywhere in the verification path.

WHY THIS EXISTS.  V003 published a remainder length and digest but never published the replacement
spans its computation excluded.  The digest was real; its INPUT was private, so the claim could not be
falsified -- the target digest cannot define its own input (relay 1014, per the V003 confirm).  This
script closes that: every removed byte interval is published in the manifest and content-addressed on
both sides, so a verifier needs nothing but the three declared inputs and three checks.

DECLARED INPUTS (full paths from the alpha-program-archive root; nothing else is opened):
  workspace/STAGE8_DESC_B01_DARIO_V002.md        the old artifact
  workspace/STAGE8_DESC_B01_DARIO_V003.md        the new artifact
  workspace/b01_carriage_manifest_v001.json      the ordered delta manifest

THE MASK RULE, AS A BYTE OPERATION -- stated because four readings of the word "blank" give four
different digests over the identical block structure, and the choice is invisible in the output:

    Let D_old = [mask_span_old.start, mask_span_old.end) be the half-open interval of the DECIMAL
    DIGIT RUN that immediately follows the byte string "CLOSURE_END_BYTE = " in the old file, and
    D_new likewise in the new file.  The mask is DELETION: those bytes are removed, not replaced by
    a filler of equal width.  A filler of equal width leaves its own bytes in the remainder and
    changes the remainder digest while leaving the block structure identical.  DELETION is the rule
    of record here because it reproduces the opposite lane's independently computed diagnostic
    exactly, which is a stronger ground than my preference.

THE REMAINDER, AS A BYTE OPERATION:

    removal_spans_old := sort(replacement old_spans + [D_old])      (asserted non-overlapping)
    removal_spans_new := sort(replacement new_spans + [D_new])      (asserted non-overlapping)
    remainder_old     := concat of the complement of removal_spans_old in the old file
    remainder_new     := concat of the complement of removal_spans_new in the new file
    CARRIED holds iff remainder_old == remainder_new, and the remainder is those bytes.

WARRANT.  Every check below is fatal.  The script REFUSES TO EMIT a remainder it cannot ground:
file digests, per-span digests on BOTH sides, ordering, non-overlap, exact tiling of the removal
lists against the manifest, and final remainder equality.  Exit 2 on any failure, before any result
line is printed.

Run from workspace/:  cd <archive-root>/workspace && python3 build_b01_carriage_remainder_v001.py
"""

import hashlib
import json
import sys

MANIFEST = 'b01_carriage_manifest_v001.json'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def complement(buf, spans):
    out, pos = [], 0
    for a, b in spans:
        out.append(buf[pos:a])
        pos = b
    out.append(buf[pos:])
    return b''.join(out)


def main():
    problems = []
    with open(MANIFEST) as fh:
        man = json.load(fh)

    old_path = man['old_file'].split('/')[-1]
    new_path = man['new_file'].split('/')[-1]
    with open(old_path, 'rb') as fh:
        A = fh.read()
    with open(new_path, 'rb') as fh:
        B = fh.read()

    # ---- 1. the artifacts are the ones the manifest names
    if sha(A) != man['old_sha256']:
        problems.append('old file digest %s != manifest %s' % (sha(A), man['old_sha256']))
    if sha(B) != man['new_sha256']:
        problems.append('new file digest %s != manifest %s' % (sha(B), man['new_sha256']))

    # ---- 2. the mask spans really are the digit run after the declared key
    KEY = b'CLOSURE_END_BYTE = '
    for buf, span, txt, lbl in ((A, man['mask_span_old'], man['mask_bytes_old'], 'old'),
                                (B, man['mask_span_new'], man['mask_bytes_new'], 'new')):
        a, b = span
        if buf[a - len(KEY):a] != KEY:
            problems.append('%s mask span is not preceded by the declared key' % lbl)
        got = buf[a:b]
        if not got.isdigit():
            problems.append('%s mask span is not a decimal digit run: %r' % (lbl, got))
        if got.decode() != txt:
            problems.append('%s mask bytes %r != manifest %r' % (lbl, got.decode(), txt))
        if b < len(buf) and buf[b:b + 1].isdigit():
            problems.append('%s mask span truncates a longer digit run' % lbl)

    # ---- 3. every replacement span is content-addressed on BOTH sides
    for r in man['replacements']:
        oa, ob = r['old_span']
        na, nb = r['new_span']
        if ob - oa != r['old_len'] or nb - na != r['new_len']:
            problems.append('replacement %d: declared length disagrees with its own span' % r['n'])
        if sha(A[oa:ob]) != r['old_sha256']:
            problems.append('replacement %d: old span digest mismatch' % r['n'])
        if sha(B[na:nb]) != r['new_sha256']:
            problems.append('replacement %d: new span digest mismatch' % r['n'])

    # ---- 4. the removal lists are exactly the replacements plus the mask, ordered and disjoint
    for key, mask, spans, lbl in (('old_span', man['mask_span_old'], man['removal_spans_old'], 'old'),
                                  ('new_span', man['mask_span_new'], man['removal_spans_new'], 'new')):
        expect = sorted([list(r[key]) for r in man['replacements']] + [list(mask)])
        if [list(s) for s in spans] != expect:
            problems.append('%s removal list is not exactly the replacements plus the mask' % lbl)
        prev = 0
        for a, b in spans:
            if a < prev:
                problems.append('%s removal spans overlap or are out of order at [%d,%d)' % (lbl, a, b))
            if b < a:
                problems.append('%s removal span [%d,%d) is inverted' % (lbl, a, b))
            prev = b

    if problems:
        sys.stderr.write('MANIFEST NOT GROUNDED -- refusing to emit:\n  ' + '\n  '.join(problems) + '\n')
        return 2

    ra = complement(A, man['removal_spans_old'])
    rb = complement(B, man['removal_spans_new'])
    if ra != rb:
        sys.stderr.write('REMAINDERS DIFFER -- refusing to emit a carriage claim:\n'
                         '  old %d bytes %s\n  new %d bytes %s\n'
                         % (len(ra), sha(ra), len(rb), sha(rb)))
        return 2

    sys.stderr.write('GROUNDED: %d replacements + 1 mask span, both sides digest-checked; '
                     'removal lists tile; remainders equal\n' % len(man['replacements']))
    print('MASK_RULE       = DELETE the decimal digit run after "CLOSURE_END_BYTE = "')
    print('MASK_SPAN_OLD   = [%d,%d)  bytes %r' % (man['mask_span_old'][0], man['mask_span_old'][1], man['mask_bytes_old']))
    print('MASK_SPAN_NEW   = [%d,%d)  bytes %r' % (man['mask_span_new'][0], man['mask_span_new'][1], man['mask_bytes_new']))
    print('REPLACEMENTS    = %d' % len(man['replacements']))
    print('REMOVED_OLD     = %d bytes of %d' % (sum(b - a for a, b in man['removal_spans_old']), len(A)))
    print('REMOVED_NEW     = %d bytes of %d' % (sum(b - a for a, b in man['removal_spans_new']), len(B)))
    print('REMAINDER_LEN   = %d' % len(ra))
    print('REMAINDER_SHA   = %s' % sha(ra))
    return 0


if __name__ == '__main__':
    sys.exit(main())
