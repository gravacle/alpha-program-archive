#!/usr/bin/env python3
"""
SEALED GENERATOR — STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V006.md   (relay 1069, DARIO lane)

WHAT THIS RELAY REPAIRS, AND THE MACHINERY GAP IT CLOSES
--------------------------------------------------------
V005 restored two blocks byte-exactly against the spans it was given, and the spans were short by one
line each: F14 lost its CLOSING CODE FENCE, F15 lost its FINAL SENTENCE. Every digest in V005
verified. The bytes matched the spans exactly.

    A SPAN DIGEST CERTIFIES FIDELITY, NOT COMPLETENESS.

V005's generator asked "do these bytes match this span?" and never "is this span a whole block?".
No digest can answer the second question; only a structural test can. This generator adds the two
that would have caught it with nobody reading the file:

  R7  FENCE BALANCE      — walk the artifact, track depth, require final depth 0. Parity is not
                           enough: an even count can still be mismatched.
  R8  COMPLETE-BLOCK     — each restored block, at its CORRECTED span, must occur EXACTLY ONCE.

REFUSAL PATHS (emit NOTHING, exit non-zero):
  R1  a declared member is absent
  R2  STRICT != STABLE on any declared member
  R3  a predecessor (V005..V001) has moved
  R4  the MANDATE is absent or moved
  R5  the verbatim PROPOSED_NOT_ADOPTED header is missing
  R6  CARRIAGE: a carried V005 region is not byte-identical / not present verbatim
  R7  FENCE BALANCE: final fence depth is not 0
  R8  COMPLETE-BLOCK: a block's span digest is wrong, or it does not occur exactly once
  R9  the two inserted lines are not V003's own bytes at the declared lines
  R10 the closed-claim audit does not reproduce 35 / 16 / 0
  R11 residue scan finds an output-inspection token in authored prose
  R12 the closure byte does not reach a fixed point
"""

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path("/Users/bgm/MB Work/alpha-program-archive")
WS = ROOT / "workspace"
ART = WS / "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V006.md"
SIDECAR = Path(str(ART) + ".seal.sha256")

PREDECESSORS = {
    "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V005.md":
        "96ec8bf4e2706eced5b17489d53f3844402331854ed4ea82d54c212dec3a22d7",
    "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V004.md":
        "e1388e12d14ed3f39c663c085b72bded1e7f58bf255539ce2e2b115315d031e1",
    "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V003.md":
        "82d5c5dd59d1d0d6981a2cde7244c1dad1a66352c4159b8543f0554777abea31",
    "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V002.md":
        "14a811a8d5a507c5d20e26ef40fa53661e22b0b39f869edd68ad700bc3765f82",
    "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V001.md":
        "8c257818b55c66aef1842024601c51f3a22599a949db7de4280d7763fc9dcdbc",
}
V005 = WS / "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V005.md"
V003 = WS / "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V003.md"

MANDATE = WS / "ATTACH_SUPPLY_MANDATE_DECISION_OF_RECORD_V001.md"
MANDATE_DIGEST = "ad9fc14e1f07494f7527d95f2a94ee7a26da9d49cc784c409f31325f54572213"

REQUIRED_HEADER = (
    "PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL ENTRY "
    "(ATTACH_SUPPLY_MANDATE_DECISION_OF_RECORD_V001, ad9fc14e1f07…)"
)

# CORRECTED spans — each now a COMPLETE block. (label, V003 [lo, hi), digest, bytes)
COMPLETE_BLOCKS = [
    ("F14", 239, 256, "2aae31641f2802b83334f3e7f3dc1a53630fd36016e411ae55f5c038f75d8783", 1136),
    ("F15", 257, 271, "b9c0208e3d889e66ad6581b39e6f25af7b79f0bedf5fd578914bd00b0490e72e", 724),
]

# The two inserted lines, by V003 line number.
INSERTED = [(255, "F14's closing code fence"), (270, "F15's final sentence")]

# Carried V005 regions (1-indexed [lo, hi)) with declared digests.
CARRIAGE = [
    ("REGION A (V005 lines 96-284)", 96, 285,
     "ea45e4a2417030d07ffac5b8f45c3d30bac6082b497fd23c82288efcb5fc2623"),
    ("REGION B (V005 lines 285-300)", 285, 301,
     "5139f9be0376521f21aacc2e92aed86501124e232ba008d2d8874d37347ae271"),
    ("REGION C (V005 lines 301-693)", 301, 694,
     "28df927ed3315ba5f0c5b1b60deb8634b3164da491f49e3bea9268754261147e"),
]

DECLARED_ROWS = {f"F{i:02d}" for i in range(1, 16)} | {f"A{i}" for i in range(1, 9)}
ROW_LABEL = re.compile(r"^[FA][0-9]{1,2}$")
IDENT = re.compile(r"[A-Za-z][A-Za-z0-9_]*")
EXPECTED_AUDIT = (35, 16, 0)

RESIDUE_TOKENS_27 = [
    "137.03", "1/137", "0.00729", "7.297", "fine structure constant",
    "measured value", "measured alpha", "experimental value", "CODATA", "PDG",
    "observed coupling", "known value", "target value", "matches experiment",
    "agrees with experiment", "numerically equals", "evaluates to",
    "we compute alpha", "alpha =", "kappa_record =", "kappa_Thomson",
    "the answer is", "reproduces the observed", "in excellent agreement",
    "percent agreement", "sigma agreement", "best fit",
]
assert len(RESIDUE_TOKENS_27) == 27


def hf(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def hs(s): return hashlib.sha256(s.encode()).hexdigest()
def fail(c, m):
    print(f"REFUSED (R{c}): {m}", file=sys.stderr)
    return c


def block(text, a, b):
    ma = re.search(rf"^{re.escape(a)}\s*$", text, re.M)
    mb = re.search(rf"^{re.escape(b)}\s*$", text, re.M)
    if not ma or not mb or mb.start() <= ma.end():
        raise ValueError(f"delimiters {a}/{b} not found line-anchored and in order")
    return text[ma.end(): mb.start()]


def fence_depth(text):
    """Walk the file tracking fence depth. Returns (marker_count, final_depth)."""
    n = depth = 0
    for line in text.splitlines():
        if line.strip().startswith("```"):
            n += 1
            depth = 1 - depth
    return n, depth


def parse_members(text):
    out = []
    for line in text.splitlines():
        m = re.match(r"^\|\s*(\d{2})\s*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|", line)
        if m:
            out.append((m.group(2), m.group(3)))
    return out


def authored_prose(text):
    out, fence = [], False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            fence = not fence
            continue
        if fence or re.match(r"^\|", line):
            continue
        out.append(line)
    return "\n".join(out)


def main() -> int:
    if not ART.exists():
        return fail(1, "artifact absent")
    text = ART.read_text()

    if not MANDATE.exists() or hf(MANDATE) != MANDATE_DIGEST:
        return fail(4, "mandate absent or moved")
    print(f"MANDATE = LIVE ({MANDATE_DIGEST[:16]}…)")

    for name, dg in PREDECESSORS.items():
        p = WS / name
        if not p.exists() or hf(p) != dg:
            return fail(3, f"predecessor moved or absent: {name}")
    print("V005, V004, V003, V002, V001 = BYTE-UNTOUCHED")

    if REQUIRED_HEADER not in text:
        return fail(5, "verbatim header missing")
    print("HEADER = VERBATIM-PRESENT")

    members = parse_members(text)
    if not members:
        return fail(1, "no closure table parsed")
    for rel, pinned in members:
        p = ROOT / rel
        if not p.exists():
            return fail(1, f"declared member absent: {rel}")
        if hf(p) != pinned:
            return fail(2, f"STRICT!=STABLE for {rel}")
    print(f"PROSE_DIGESTS = {len(members)}/{len(members)}, STRICT==STABLE")

    v3 = V003.read_text().splitlines(keepends=True)
    v5 = V005.read_text().splitlines(keepends=True)

    # ---- R9 the two inserted lines are V003's own bytes
    for lineno, what in INSERTED:
        src = v3[lineno - 1]
        if src not in text:
            return fail(9, f"inserted line V003 L{lineno} ({what}) not present in V006")
        print(f"INSERTED V003 L{lineno}: {src.rstrip()[:44]!r}  ({what})")

    # ---- R8 COMPLETE BLOCKS at the CORRECTED spans, each exactly once
    for label, lo, hi, expect, nbytes in COMPLETE_BLOCKS:
        seg = "".join(v3[lo - 1: hi - 1])
        d = hs(seg)
        if d != expect:
            return fail(8, f"{label}: V003 span digest {d} != declared {expect}")
        if len(seg.encode()) != nbytes:
            return fail(8, f"{label}: {len(seg.encode())} B != declared {nbytes} B")
        occ = text.count(seg)
        if occ != 1:
            return fail(8, f"{label}: complete block occurs {occ} times, expected exactly 1")
        print(f"COMPLETE-BLOCK {label}: V003 L{lo}-{hi-1}  {nbytes:>5} B  {d[:32]}…  EXACTLY ONCE")

    # ---- R6 CARRIAGE
    for label, lo, hi, expect in CARRIAGE:
        seg = "".join(v5[lo - 1: hi - 1])
        d = hs(seg)
        if d != expect:
            return fail(6, f"{label}: V005 source digest {d} != declared {expect}")
        if seg not in text:
            return fail(6, f"{label}: bytes not present verbatim in V006")
        print(f"CARRIAGE {label}: {len(seg.encode()):>6} B  {d[:32]}…  BYTE-IDENTICAL")

    # ---- R7 FENCE BALANCE (the test V005 lacked)
    n5, d5 = fence_depth(V005.read_text())
    n6, d6 = fence_depth(text)
    print(f"FENCE BALANCE: V006 {n6} markers, final depth {d6} -> "
          f"{'BALANCED' if d6 == 0 else 'UNBALANCED'}   (V005 was {n5}, depth {d5})")
    if d6 != 0:
        return fail(7, f"fence depth {d6} != 0; a fence is left open")

    # ---- R10 closed-claim audit, re-run over the carried bytes
    smap = {}
    for line in block(text, "SYMBOL_TABLE_MAP_BEGIN", "SYMBOL_TABLE_MAP_END").strip().splitlines():
        parts = line.split()
        if len(parts) == 2:
            smap[parts[0]] = parts[1]
    vocab = set(block(text, "CLOSED_VOCABULARY_BEGIN", "CLOSED_VOCABULARY_END").split())
    if [w for w in vocab if "_" in w or len(w) == 1] or (vocab & set(smap)):
        return fail(10, "map/vocabulary invariants violated")
    cons = block(text, "CONSTRUCTION_BEGIN", "CONSTRUCTION_END")
    tokens = sorted(set(IDENT.findall(cons)))
    if [s for s in tokens if ("_" in s or len(s) == 1) and s not in smap]:
        return fail(10, "INV-4 violated")
    row_labels = [s for s in tokens if ROW_LABEL.match(s) and s in DECLARED_ROWS]
    unmapped = sorted(s for s in tokens
                      if s not in smap and s not in vocab and s not in row_labels)
    n_sym = len([s for s in tokens if s in smap])
    n_rows = len({smap[s] for s in tokens if s in smap})
    print(f"CLOSED_CLAIM AUDIT (re-run) = {n_sym} symbols / {n_rows} distinct rows / "
          f"{len(unmapped)} unmapped")
    if (n_sym, n_rows, len(unmapped)) != EXPECTED_AUDIT:
        return fail(10, f"audit changed: {(n_sym, n_rows, len(unmapped))} != {EXPECTED_AUDIT}")

    # ---- R11 residue
    low = authored_prose(text).lower()
    hits = [(t, low.count(t.lower())) for t in RESIDUE_TOKENS_27 if low.count(t.lower())]
    total = sum(n for _, n in hits)
    print(f"RESIDUE_SCAN(27 tokens over authored prose) = {total} hit(s)")
    for t, n in hits:
        print(f"    {t!r}: {n}")
    if total:
        return fail(11, "output-inspection token in authored prose")

    # ---- R12 declared-first fixed point
    marker = "CLOSURE_DECLARATION_END"
    for _ in range(8):
        body = ART.read_text()
        i = body.find(marker)
        if i < 0:
            return fail(12, "closure end marker absent")
        val = f"{len(body[: i + len(marker)].encode()):08d}"
        new = re.sub(r"CLOSURE_END_BYTE = [0-9X]{8}", f"CLOSURE_END_BYTE = {val}", body)
        new = re.sub(r"end byte [0-9X]{8}", f"end byte {val}", new)
        if new == body:
            print(f"CLOSURE_END_BYTE = {val} (fixed point reached)")
            break
        ART.write_text(new)
    else:
        return fail(12, "closure byte did not reach a fixed point")

    for name, dg in PREDECESSORS.items():
        if hf(WS / name) != dg:
            return fail(3, f"predecessor moved during the relay: {name}")
    print("V005..V001 = BYTE-UNTOUCHED (rechecked after sealing work)")

    d = hf(ART)
    SIDECAR.write_text(f"{d}  {ART.name}\n")
    print(f"SEALED {ART.name}\n  {d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
