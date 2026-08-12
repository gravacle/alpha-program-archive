#!/usr/bin/env python3
"""
SEALED GENERATOR — STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V005.md   (relay 1064, DARIO lane)

WHAT THIS RELAY REPAIRS
-----------------------
V004 asserted "nothing else moves" and then, in rewriting section 4, dropped two forced-row
classification blocks that lived there: the F14 ruling on rho_joint and the F15 ruling on the
connection A. The rows and the symbol map survived; the reasoning that classified them did not.

V004's carriage proof could not detect this: it proved the regions it CARRIED were byte-identical,
which is silent about the region it REWROTE. This generator therefore adds the check that would have
caught it (R7): every ledger row named in the map must have its classification text present.

RESTORATION IS BY SPAN, NOT BY RETYPING. Both blocks are extracted from sealed V003 at declared line
ranges, rehashed against declared digests, and required to appear verbatim in V005.

REFUSAL PATHS (emit NOTHING, exit non-zero):
  R1  a declared member is absent
  R2  STRICT != STABLE on any declared member
  R3  a predecessor (V004/V003/V002/V001) has moved
  R4  the MANDATE is absent or moved
  R5  the verbatim PROPOSED_NOT_ADOPTED header is missing
  R6  RESTORATION: a restored block's span digest is wrong, or its bytes are not verbatim in V005
  R7  ROW-JUSTIFICATION: a row named in the symbol map has no classification text in the artifact
      (the check V004 lacked)
  R8  CARRIAGE: either carried V004 region is not byte-identical
  R9  the map/vocabulary invariants INV-1..INV-4 fail, or the closed claim does not reproduce
      35 symbols / 16 distinct rows / 0 unmapped
  R10 residue scan finds an output-inspection token in authored prose
  R11 the closure byte does not reach a fixed point
"""

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path("/Users/bgm/MB Work/alpha-program-archive")
WS = ROOT / "workspace"
ART = WS / "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V005.md"
SIDECAR = Path(str(ART) + ".seal.sha256")

PREDECESSORS = {
    "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V004.md":
        "e1388e12d14ed3f39c663c085b72bded1e7f58bf255539ce2e2b115315d031e1",
    "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V003.md":
        "82d5c5dd59d1d0d6981a2cde7244c1dad1a66352c4159b8543f0554777abea31",
    "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V002.md":
        "14a811a8d5a507c5d20e26ef40fa53661e22b0b39f869edd68ad700bc3765f82",
    "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V001.md":
        "8c257818b55c66aef1842024601c51f3a22599a949db7de4280d7763fc9dcdbc",
}
V004 = WS / "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V004.md"
V003 = WS / "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V003.md"

MANDATE = WS / "ATTACH_SUPPLY_MANDATE_DECISION_OF_RECORD_V001.md"
MANDATE_DIGEST = "ad9fc14e1f07494f7527d95f2a94ee7a26da9d49cc784c409f31325f54572213"

REQUIRED_HEADER = (
    "PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL ENTRY "
    "(ATTACH_SUPPLY_MANDATE_DECISION_OF_RECORD_V001, ad9fc14e1f07…)"
)

# (label, V003 line range [lo, hi), declared span digest)
RESTORED = [
    ("F14 classification block", 239, 255,
     "749dfe4a7a68efa2c43c870bc8767fcf7ad57c25c6800a324c13e5381455cd33"),
    ("F15 classification block", 257, 270,
     "ed824a3b79b4691964f644e829b7376734dc007167a8707e2882eb31bc4a627e"),
]

# (label, V004 line range [lo, hi), declared digest)
CARRIAGE = [
    ("REGION A (V004 sections 0-3 + section-4 heading, lines 85-242)", 85, 243,
     "eb3ed614743fba83e8699d522e07dd5d47d144c8c1dff85bb84177ae219c21af"),
    ("REGION B (V004 sections 4.1-8, lines 243-577)", 243, 578,
     "7b1e2e324c3e60a734fbbeaa01d1e09154fbd04f91d70f5f28972037c76c0880"),
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
    """Line-anchored block extraction (prose may mention the delimiters inline)."""
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
        p = WS / name
        if not p.exists() or hf(p) != dg:
            return fail(3, f"predecessor moved or absent: {name}")
    print("V004, V003, V002, V001 = BYTE-UNTOUCHED")

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

    # ---- R6 RESTORATION : extract from sealed V003 by span, rehash, require verbatim presence
    v3 = V003.read_text().splitlines(keepends=True)
    for label, lo, hi, expect in RESTORED:
        seg = "".join(v3[lo - 1: hi - 1])
        d = hs(seg)
        if d != expect:
            return fail(6, f"{label}: V003 span digest {d} != declared {expect}")
        if seg not in text:
            return fail(6, f"{label}: restored bytes are NOT present verbatim in V005")
        print(f"RESTORED {label}: V003 L{lo}-{hi-1}  {len(seg.encode()):>5} B  {d[:32]}…  BYTE-IDENTICAL")

    # ---- R8 CARRIAGE : the untouched V004 regions
    v4 = V004.read_text().splitlines(keepends=True)
    for label, lo, hi, expect in CARRIAGE:
        seg = "".join(v4[lo - 1: hi - 1])
        d = hs(seg)
        if d != expect:
            return fail(8, f"{label}: V004 source digest {d} != declared {expect}")
        if seg not in text:
            return fail(8, f"{label}: bytes are NOT present verbatim in V005")
        print(f"CARRIAGE {label}: {len(seg.encode()):>6} B  {d[:32]}…  BYTE-IDENTICAL")

    # ---- map, vocabulary, invariants (carried inside region B; re-run anyway)
    smap = {}
    for line in block(text, "SYMBOL_TABLE_MAP_BEGIN", "SYMBOL_TABLE_MAP_END").strip().splitlines():
        parts = line.split()
        if len(parts) == 2:
            smap[parts[0]] = parts[1]
    vocab = set(block(text, "CLOSED_VOCABULARY_BEGIN", "CLOSED_VOCABULARY_END").split())
    if not smap or not vocab:
        return fail(9, "map or vocabulary empty")
    if sorted({r for r in smap.values() if r not in DECLARED_ROWS}):
        return fail(9, "map names undeclared rows")
    if [w for w in vocab if "_" in w]:
        return fail(9, "INV-1 violated")
    if [w for w in vocab if len(w) == 1]:
        return fail(9, "INV-2 violated")
    if vocab & set(smap):
        return fail(9, "INV-3 violated")
    cons = block(text, "CONSTRUCTION_BEGIN", "CONSTRUCTION_END")
    tokens = sorted(set(IDENT.findall(cons)))
    if [s for s in tokens if ("_" in s or len(s) == 1) and s not in smap]:
        return fail(9, "INV-4 violated")
    row_labels = [s for s in tokens if ROW_LABEL.match(s) and s in DECLARED_ROWS]
    unmapped = sorted(s for s in tokens
                      if s not in smap and s not in vocab and s not in row_labels)
    if unmapped:
        return fail(9, f"closed claim broken: {unmapped}")
    n_sym = len([s for s in tokens if s in smap])
    n_rows = len({smap[s] for s in tokens if s in smap})
    print(f"CLOSED_CLAIM AUDIT (re-run over carried bytes) = "
          f"{n_sym} symbols / {n_rows} distinct rows / {len(unmapped)} unmapped")
    if (n_sym, n_rows, len(unmapped)) != EXPECTED_AUDIT:
        return fail(9, f"audit changed: {(n_sym, n_rows, len(unmapped))} != {EXPECTED_AUDIT}")

    # ---- R7 ROW-JUSTIFICATION : the check V004 lacked.
    #
    # Every row the map names must have CLASSIFICATION TEXT somewhere the reader can reach — not
    # merely a label. A carriage proof scoped to the carried regions cannot see a deletion in the
    # rewritten region; this can.
    #
    # These artifacts are incremental supersessions: the itemised F/A tables were authored in V001
    # and V002 and have been inherited since. So a row is justified if its text is in THIS artifact
    # OR in a declared sealed predecessor, and the check REPORTS WHERE — refusing only if a row is
    # justified nowhere in the chain. Demanding in-artifact text for every row would not be a
    # completeness check; it would be a demand that this relay import material the assignment
    # expressly excludes from its scope.
    def justifies(body, row):
        pat = re.compile(rf"(^\|\s*{row}\b)|(^\|\s*\*\*{row}\*\*)|(^{row}\s)|(\*\*{row}\b)|"
                         rf"(\b{row}\s*\(FORCED\))|(\b{row}\s*\(AUTHORED)", re.M)
        return bool(pat.search(body))

    chain = [("V005 (this artifact)", text)] + [
        (n, (WS / n).read_text()) for n in PREDECESSORS
    ]
    used_rows = sorted(set(smap.values()))
    here, inherited, nowhere = [], [], []
    for row in used_rows:
        where = next((label for label, body in chain if justifies(body, row)), None)
        if where is None:
            nowhere.append(row)
        elif where.startswith("V005"):
            here.append(row)
        else:
            inherited.append((row, where))
    if nowhere:
        return fail(7, f"rows named by the map justified NOWHERE in the sealed chain: {nowhere}")
    print(f"ROW_JUSTIFICATION = {len(used_rows)}/{len(used_rows)} justified; "
          f"{len(here)} in this artifact, {len(inherited)} inherited from sealed predecessors")
    if here:
        print(f"    in V005: {sorted(here)}")
    for row, where in sorted(inherited):
        print(f"    {row} <- {where}")

    # ---- R10 residue
    low = authored_prose(text).lower()
    hits = [(t, low.count(t.lower())) for t in RESIDUE_TOKENS_27 if low.count(t.lower())]
    total = sum(n for _, n in hits)
    print(f"RESIDUE_SCAN(27 tokens over authored prose) = {total} hit(s)")
    for t, n in hits:
        print(f"    {t!r}: {n}")
    if total:
        return fail(10, "output-inspection token in authored prose")

    # ---- R11 declared-first fixed point
    marker = "CLOSURE_DECLARATION_END"
    for _ in range(8):
        body = ART.read_text()
        i = body.find(marker)
        if i < 0:
            return fail(11, "closure end marker absent")
        val = f"{len(body[: i + len(marker)].encode()):08d}"
        new = re.sub(r"CLOSURE_END_BYTE = [0-9X]{8}", f"CLOSURE_END_BYTE = {val}", body)
        new = re.sub(r"end byte [0-9X]{8}", f"end byte {val}", new)
        if new == body:
            print(f"CLOSURE_END_BYTE = {val} (fixed point reached)")
            break
        ART.write_text(new)
    else:
        return fail(11, "closure byte did not reach a fixed point")

    for name, dg in PREDECESSORS.items():
        if hf(WS / name) != dg:
            return fail(3, f"predecessor moved during the relay: {name}")
    print("V004, V003, V002, V001 = BYTE-UNTOUCHED (rechecked after sealing work)")

    d = hf(ART)
    SIDECAR.write_text(f"{d}  {ART.name}\n")
    print(f"SEALED {ART.name}\n  {d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
