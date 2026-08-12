#!/usr/bin/env python3
"""
SEALED GENERATOR — STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V007.md   (relay 1071, DARIO lane)

WHAT THIS RELAY REPAIRS
-----------------------
V006 carried V005's body byte-identical and shrank the closure table from 27 members to 6. Every
mechanical check V006 ran was green — because none of them knew that the body holds references INTO
the table. A closure table is not an inventory; it is a NAMESPACE. Cutting it silently repointed
every `member NN` in the carried body: 19 citations left undefined, more rebound onto files they
never named.

R7 is the refusal path that would have caught it, and now does: extract every member-number citation
from the body generically and require that each resolves against the declared table. It is written to
be scope-honest — it reports its own extraction convention and its counts — because the recurring
failure in this artifact's history is checks that are sound about what they measure and silent about
what they do not.

REFUSAL PATHS (emit NOTHING, exit non-zero):
  R1  a declared member is absent
  R2  STRICT != STABLE on any declared member
  R3  a predecessor (V006..V001) has moved
  R4  the MANDATE is absent or moved
  R5  the verbatim PROPOSED_NOT_ADOPTED header is missing
  R6  CARRIAGE: the carried V006 body is not byte-identical / not present verbatim
  R7  CITATIONS: a body member-number citation is UNDEFINED, or is REBOUND relative to V005's table
  R8  TABLE: IDs 01-27 are not V005's rows carried unchanged, or IDs are not a contiguous 01..30
  R9  FENCE BALANCE: final fence depth is not 0
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
ART = WS / "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V007.md"
SIDECAR = Path(str(ART) + ".seal.sha256")

PREDECESSORS = {
    "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V006.md":
        "0701f49e4183c17efc76238b786f1abd54efeca4347c48e11aa48d63c7d6806e",
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
V006 = WS / "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V006.md"
V005 = WS / "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V005.md"

MANDATE = WS / "ATTACH_SUPPLY_MANDATE_DECISION_OF_RECORD_V001.md"
MANDATE_DIGEST = "ad9fc14e1f07494f7527d95f2a94ee7a26da9d49cc784c409f31325f54572213"

REQUIRED_HEADER = (
    "PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL ENTRY "
    "(ATTACH_SUPPLY_MANDATE_DECISION_OF_RECORD_V001, ad9fc14e1f07…)"
)

# The carried body: V006 lines [56, 739) — everything after its closure, minus its final lines.
CARRIED = (56, 739, "7245b1a11d6e91dfdfb1017757cf8a88282dad16f4f78860bc54dab7ef36b6a7", 34297)
TABLE27_DIGEST = "3e0159476a99f3d848b57ebcabd32f1a90595196dc2f6bf7f710c269da9d2fb3"

# Declared citation-extraction convention, reported with the count so the scope is visible.
CITE_RE = re.compile(r"members?\s+((?:\d{2})(?:\s*(?:,|and|/|-)\s*\d{2})*)")
ROW_RE = re.compile(r"^\|\s*(\d{2})\s*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|", re.M)

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
    n = depth = 0
    for line in text.splitlines():
        if line.strip().startswith("```"):
            n += 1
            depth = 1 - depth
    return n, depth


def table(text):
    return {m.group(1): (m.group(2), m.group(3)) for m in ROW_RE.finditer(text)}


def citations(body):
    out = []
    for m in CITE_RE.finditer(body):
        out.extend(re.findall(r"\d{2}", m.group(1)))
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
    print("V006..V001 = BYTE-UNTOUCHED")

    if REQUIRED_HEADER not in text:
        return fail(5, "verbatim header missing")
    print("HEADER = VERBATIM-PRESENT")

    tbl = table(text)
    for rel, pinned in ((v[0], v[1]) for v in tbl.values()):
        p = ROOT / rel
        if not p.exists():
            return fail(1, f"declared member absent: {rel}")
        if hf(p) != pinned:
            return fail(2, f"STRICT!=STABLE for {rel}")
    print(f"PROSE_DIGESTS = {len(tbl)}/{len(tbl)}, STRICT==STABLE")

    # ---- R8 TABLE : contiguous 01..30, and 01-27 are V005's rows unchanged
    ids = sorted(tbl)
    if ids != [f"{i:02d}" for i in range(1, len(ids) + 1)]:
        return fail(8, f"IDs are not contiguous from 01: {ids}")
    v5 = V005.read_text()
    v5tbl = table(v5)
    v5rows = "".join(l + "\n" for l in v5.splitlines() if ROW_RE.match(l + "\n"))
    if hs(v5rows) != TABLE27_DIGEST:
        return fail(8, f"V005 27-row block digest {hs(v5rows)} != declared {TABLE27_DIGEST}")
    for i in (f"{n:02d}" for n in range(1, 28)):
        if tbl.get(i) != v5tbl.get(i):
            return fail(8, f"ID {i} is not V005's row carried unchanged")
    print(f"TABLE = 27-CARRIED + {len(ids)-27}-APPENDED (IDs 01..{ids[-1]}, contiguous, 01-27 == V005)")

    # ---- R6 CARRIAGE
    v6 = V006.read_text().splitlines(keepends=True)
    lo, hi, expect, nbytes = CARRIED
    carried = "".join(v6[lo - 1: hi - 1])
    if hs(carried) != expect or len(carried.encode()) != nbytes:
        return fail(6, f"carried body digest/size mismatch: {hs(carried)} {len(carried.encode())}")
    if carried not in text:
        return fail(6, "carried body not present verbatim in V007")
    print(f"CARRIAGE V006 L{lo}-{hi-1}: {nbytes} B  {expect[:32]}…  BYTE-IDENTICAL")

    # ---- R7 CITATIONS : the check V006 lacked
    body = text[text.index("CLOSURE_DECLARATION_END") + len("CLOSURE_DECLARATION_END"):]
    cites = citations(body)
    undefined = sorted({c for c in cites if c not in tbl})
    rebound = sorted({c for c in cites
                      if c in tbl and c in v5tbl and tbl[c][0] != v5tbl[c][0]})
    if undefined:
        return fail(7, f"body citations UNDEFINED against the table: {undefined}")
    if rebound:
        return fail(7, f"body citations REBOUND relative to V005's table: {rebound}")
    print(f"CITATIONS = {len(cites)}/{len(cites)}-RESOLVE  "
          f"({len(set(cites))} distinct: {sorted(set(cites))})")
    print(f"    extraction convention: {CITE_RE.pattern!r}  — 0 undefined, 0 rebound")

    # ---- R9 fence balance
    n, depth = fence_depth(text)
    print(f"FENCE BALANCE: {n} markers, final depth {depth} -> "
          f"{'BALANCED' if depth == 0 else 'UNBALANCED'}")
    if depth != 0:
        return fail(9, f"fence depth {depth} != 0")

    # ---- R10 closed-claim audit over the carried bytes
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
    print(f"CLOSED_CLAIM AUDIT = {n_sym} symbols / {n_rows} distinct rows / {len(unmapped)} unmapped")
    if (n_sym, n_rows, len(unmapped)) != EXPECTED_AUDIT:
        return fail(10, f"audit changed: {(n_sym, n_rows, len(unmapped))} != {EXPECTED_AUDIT}")

    # ---- R11 residue
    low = authored_prose(text).lower()
    hits = [(t, low.count(t.lower())) for t in RESIDUE_TOKENS_27 if low.count(t.lower())]
    total = sum(k for _, k in hits)
    print(f"RESIDUE_SCAN(27 tokens over authored prose) = {total} hit(s)")
    for t, k in hits:
        print(f"    {t!r}: {k}")
    if total:
        return fail(11, "output-inspection token in authored prose")

    # ---- R12 declared-first fixed point
    marker = "CLOSURE_DECLARATION_END"
    for _ in range(8):
        b = ART.read_text()
        i = b.find(marker)
        if i < 0:
            return fail(12, "closure end marker absent")
        val = f"{len(b[: i + len(marker)].encode()):08d}"
        new = re.sub(r"CLOSURE_END_BYTE = [0-9X]{8}", f"CLOSURE_END_BYTE = {val}", b)
        new = re.sub(r"end byte [0-9X]{8}", f"end byte {val}", new)
        if new == b:
            print(f"CLOSURE_END_BYTE = {val} (fixed point reached)")
            break
        ART.write_text(new)
    else:
        return fail(12, "closure byte did not reach a fixed point")

    for name, dg in PREDECESSORS.items():
        if hf(WS / name) != dg:
            return fail(3, f"predecessor moved during the relay: {name}")
    print("V006..V001 = BYTE-UNTOUCHED (rechecked after sealing work)")

    d = hf(ART)
    SIDECAR.write_text(f"{d}  {ART.name}\n")
    print(f"SEALED {ART.name}\n  {d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
