#!/usr/bin/env python3
"""
SEALED GENERATOR — STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V004.md   (relay 1061, DARIO lane)

THE REPAIR THIS GENERATOR EMBODIES
----------------------------------
V003's R11 did not extract generically. It admitted a hard-coded regular-expression inventory and
then placed B_j, v_j and w_j in an ALIASES set labelled "bound/local, not ingredients" — a false
description of three real construction objects. An exemption inside a completeness check is the
defect that check exists to catch.

THERE IS NO ALIAS SET IN THIS FILE. Extraction is generic over every letter-initial identifier in
the construction block. The only residual filter is a CLOSED VOCABULARY read out of the artifact
itself (not hard-coded here), and four invariants make it structurally incapable of holding a
construction symbol:

  INV-1  no vocabulary entry may contain "_"
  INV-2  no vocabulary entry may be a single character
  INV-3  vocabulary and map must be disjoint
  INV-4  every extracted token containing "_" OR of length 1 MUST be in the map

INV-1 with INV-4 would have caught this relay's escape unaided: B_j, v_j and w_j all carry "_".

REFUSAL PATHS (emit NOTHING, exit non-zero):
  R1  a declared member is absent
  R2  STRICT != STABLE on any declared member
  R3  V003 / V002 / V001 moved (append-only predecessors)
  R4  the MANDATE is absent or moved
  R5  the verbatim PROPOSED_NOT_ADOPTED header is missing
  R6  CARRIAGE: either carried region is not byte-identical to its V003 source
  R7  INV-1 violated
  R8  INV-2 violated
  R9  INV-3 violated
  R10 INV-4 violated
  R11 CLOSED-CLAIM: any construction token is neither mapped, nor in the closed vocabulary, nor a
      well-formed row label naming a declared row
  R12 a mapped row is not a declared ledger row
  R13 residue scan finds an output-inspection token in authored prose
  R14 the closure byte does not reach a fixed point
"""

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path("/Users/bgm/MB Work/alpha-program-archive")
ART = ROOT / "workspace" / "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V004.md"
SIDECAR = Path(str(ART) + ".seal.sha256")

PREDECESSORS = {
    "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V003.md":
        "82d5c5dd59d1d0d6981a2cde7244c1dad1a66352c4159b8543f0554777abea31",
    "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V002.md":
        "14a811a8d5a507c5d20e26ef40fa53661e22b0b39f869edd68ad700bc3765f82",
    "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V001.md":
        "8c257818b55c66aef1842024601c51f3a22599a949db7de4280d7763fc9dcdbc",
}
V003 = ROOT / "workspace" / "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V003.md"

MANDATE = ROOT / "workspace" / "ATTACH_SUPPLY_MANDATE_DECISION_OF_RECORD_V001.md"
MANDATE_DIGEST = "ad9fc14e1f07494f7527d95f2a94ee7a26da9d49cc784c409f31325f54572213"

REQUIRED_HEADER = (
    "PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL ENTRY "
    "(ATTACH_SUPPLY_MANDATE_DECISION_OF_RECORD_V001, ad9fc14e1f07…)"
)

DECLARED_ROWS = {f"F{i:02d}" for i in range(1, 16)} | {f"A{i}" for i in range(1, 9)}
ROW_LABEL = re.compile(r"^[FA][0-9]{1,2}$")
IDENT = re.compile(r"[A-Za-z][A-Za-z0-9_]*")

# Carried regions, by V003 line range (1-indexed, inclusive of first, exclusive of last).
CARRIAGE = {
    "REGION A (V003 sections 0-3, lines 81-236)": (81, 237,
        "1d14a748ce71a4ea32dc72566fefb978f24a61a3c5327596ad2e1be701413665"),
    "REGION B (V003 sections 5-7, lines 318-429)": (318, 430,
        "e716d80672b25499fed2ef088614051cc7fa3a6abf47508beca443e33def64b0"),
}

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
    """
    Extract a delimited block, matching the delimiters ONLY at line start.

    This is not cosmetic. The first draft used a bare text.index(), which matched the PROSE mention
    of `CONSTRUCTION_BEGIN`/`CONSTRUCTION_END` in section 4.1 and returned five bytes of English
    instead of the construction. INV-4 caught it immediately by reporting zero structural tokens —
    an impossible result for a block full of subscripted symbols. Line-anchoring removes the
    ambiguity; the invariant is what made the bug visible in one run.
    """
    ma = re.search(rf"^{re.escape(a)}\s*$", text, re.M)
    mb = re.search(rf"^{re.escape(b)}\s*$", text, re.M)
    if not ma or not mb or mb.start() <= ma.end():
        raise ValueError(f"delimiters {a}/{b} not found line-anchored and in order")
    return text[ma.end(): mb.start()]


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
        p = ROOT / "workspace" / name
        if not p.exists() or hf(p) != dg:
            return fail(3, f"predecessor moved or absent: {name}")
    print("V003, V002, V001 = BYTE-UNTOUCHED")

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

    # ---- R6 CARRIAGE : the untouched regions must be byte-identical to V003
    src = V003.read_text().splitlines(keepends=True)
    for label, (lo, hi, expect) in CARRIAGE.items():
        seg = "".join(src[lo - 1: hi - 1])
        d = hs(seg)
        if d != expect:
            return fail(6, f"{label}: V003 source digest {d} != declared {expect}")
        if seg not in text:
            return fail(6, f"{label}: bytes are NOT present verbatim in V004")
        print(f"CARRIAGE {label}: {len(seg.encode()):>6} B  {d[:32]}…  BYTE-IDENTICAL")

    # ---- the map and the closed vocabulary, read from the artifact itself
    smap = {}
    for line in block(text, "SYMBOL_TABLE_MAP_BEGIN", "SYMBOL_TABLE_MAP_END").strip().splitlines():
        parts = line.split()
        if len(parts) == 2:
            smap[parts[0]] = parts[1]
    vocab = set(block(text, "CLOSED_VOCABULARY_BEGIN", "CLOSED_VOCABULARY_END").split())
    if not smap or not vocab:
        return fail(11, "map or vocabulary empty")

    # ---- R12 every mapped row must be a declared ledger row
    bad = sorted({r for r in smap.values() if r not in DECLARED_ROWS})
    if bad:
        return fail(12, f"map names undeclared rows: {bad}")

    # ---- INV-1 / INV-2 / INV-3
    v_under = sorted(w for w in vocab if "_" in w)
    if v_under:
        return fail(7, f"INV-1: vocabulary entries contain '_': {v_under}")
    v_single = sorted(w for w in vocab if len(w) == 1)
    if v_single:
        return fail(8, f"INV-2: single-character vocabulary entries: {v_single}")
    overlap = sorted(vocab & set(smap))
    if overlap:
        return fail(9, f"INV-3: vocabulary and map overlap: {overlap}")
    print(f"INV-1 ok (no '_' in vocabulary)   INV-2 ok (no single-char vocabulary)   "
          f"INV-3 ok (map ∩ vocabulary = empty)")

    # ---- generic extraction; NO alias set, NO hard-coded inventory
    cons = block(text, "CONSTRUCTION_BEGIN", "CONSTRUCTION_END")
    tokens = sorted(set(IDENT.findall(cons)))

    # ---- INV-4 : structural symbols can never be filtered
    structural = [s for s in tokens if "_" in s or len(s) == 1]
    unmapped_structural = sorted(s for s in structural if s not in smap)
    if unmapped_structural:
        return fail(10, f"INV-4: structural tokens not in the map: {unmapped_structural}")
    print(f"INV-4 ok ({len(structural)} structural tokens, all mapped)")

    # ---- R11 the closed claim itself
    row_labels = [s for s in tokens if ROW_LABEL.match(s) and s in DECLARED_ROWS]
    unmapped = sorted(s for s in tokens
                      if s not in smap and s not in vocab and s not in row_labels)
    if unmapped:
        return fail(11, f"CLOSED CLAIM BROKEN — tokens in neither map nor vocabulary: {unmapped}")

    n_sym = len([s for s in tokens if s in smap])
    n_rows = len({smap[s] for s in tokens if s in smap})
    print(f"CLOSED_CLAIM AUDIT (generic, alias-free) = "
          f"{n_sym} symbols / {n_rows} distinct rows / 0 unmapped")
    print(f"    construction tokens {len(tokens)} = {n_sym} mapped "
          f"+ {len([s for s in tokens if s in vocab])} vocabulary "
          f"+ {len(row_labels)} row-label")

    result = f"{n_sym} symbols / {n_rows} distinct rows / 0 unmapped"
    if "MACHINE_CLOSED_CLAIM_RESULT" in text:
        ART.write_text(text.replace("MACHINE_CLOSED_CLAIM_RESULT", result))
        text = ART.read_text()

    # ---- R13 residue
    low = authored_prose(text).lower()
    hits = [(t, low.count(t.lower())) for t in RESIDUE_TOKENS_27 if low.count(t.lower())]
    total = sum(n for _, n in hits)
    print(f"RESIDUE_SCAN(27 tokens over authored prose) = {total} hit(s)")
    for t, n in hits:
        print(f"    {t!r}: {n}")
    if total:
        return fail(13, "output-inspection token in authored prose")

    # ---- R14 declared-first fixed point
    marker = "CLOSURE_DECLARATION_END"
    for _ in range(8):
        body = ART.read_text()
        i = body.find(marker)
        if i < 0:
            return fail(14, "closure end marker absent")
        val = f"{len(body[: i + len(marker)].encode()):08d}"
        new = re.sub(r"CLOSURE_END_BYTE = [0-9X]{8}", f"CLOSURE_END_BYTE = {val}", body)
        new = re.sub(r"end byte [0-9X]{8}", f"end byte {val}", new)
        if new == body:
            print(f"CLOSURE_END_BYTE = {val} (fixed point reached)")
            break
        ART.write_text(new)
    else:
        return fail(14, "closure byte did not reach a fixed point")

    for name, dg in PREDECESSORS.items():
        if hf(ROOT / "workspace" / name) != dg:
            return fail(3, f"predecessor moved during the relay: {name}")
    print("V003, V002, V001 = BYTE-UNTOUCHED (rechecked after sealing work)")

    d = hf(ART)
    SIDECAR.write_text(f"{d}  {ART.name}\n")
    print(f"SEALED {ART.name}\n  {d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
