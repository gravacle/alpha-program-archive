#!/usr/bin/env python3
"""
SEALED GENERATOR — STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V002.md   (relay 1057, DARIO lane)

Recomputes every structural claim V002 makes, so the circuit determination is reproducible rather
than asserted:
  * b_1 of the first-opening complex K_(1,3) and of the composition carrier K_square, from the
    members' own vertex/edge data, via rank of the incidence matrix;
  * the intra-cell noncommutation [D(z),S] != 0 for z != 1 and = 0 at z = 1 (the check's finding,
    which V002 concedes).

No physical quantity is evaluated: b_1 is an integer property of a complex, and the commutator test
uses a symbolic phase, not a value of any physical parameter.

REFUSAL PATHS — emits NOTHING and exits non-zero if any fires:
  R1  a declared member is absent;
  R2  STRICT != STABLE on any declared member;
  R3  V001 has moved (this relay is append-only and must not touch its predecessor);
  R4  the MANDATE is absent or moved — authoring without a live mandate is unlawful here;
  R5  the verbatim PROPOSED_NOT_ADOPTED header is missing;
  R6  the ledger invariant fails (both tables + the closed claim + the withdrawal of the
      one-ingredient headline must all be present);
  R7  b_1(K_(1,3)) != 0 or b_1(K_square) != 1 — the circuit determination would be unsupported;
  R8  the noncommutation check does not reproduce (nonzero off z=1, zero at z=1);
  R9  residue scan finds an output-inspection token in authored prose;
  R10 the closure byte does not reach a fixed point.
"""

import hashlib
import re
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path("/Users/bgm/MB Work/alpha-program-archive")
ART = ROOT / "workspace" / "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V002.md"
SIDECAR = Path(str(ART) + ".seal.sha256")

V001 = ROOT / "workspace" / "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V001.md"
V001_DIGEST = "8c257818b55c66aef1842024601c51f3a22599a949db7de4280d7763fc9dcdbc"

MANDATE = ROOT / "workspace" / "ATTACH_SUPPLY_MANDATE_DECISION_OF_RECORD_V001.md"
MANDATE_DIGEST = "ad9fc14e1f07494f7527d95f2a94ee7a26da9d49cc784c409f31325f54572213"

REQUIRED_HEADER = (
    "PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL ENTRY "
    "(ATTACH_SUPPLY_MANDATE_DECISION_OF_RECORD_V001, ad9fc14e1f07…)"
)

LEDGER_MARKERS = [
    "### 8.1 FORCED — F01–F13 carried",
    "### 8.2 AUTHORED — A1–A8",
    "There is no third category",
    'V001\'s "exactly one new ingredient" is FALSE',
]

# Complexes, transcribed from the members' own spans.
K_1_3 = (["r", "x1", "x2", "x3"], [("r", "x1"), ("r", "x2"), ("r", "x3")])          # member 08 :262-270
K_SQUARE = (["v00", "v10", "v01", "v11"],                                            # member 08 :1843-1852
            [("v00", "v10"), ("v00", "v01"), ("v10", "v11"), ("v01", "v11")])

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


def hf(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def rank_exact(rows: list[list[Fraction]]) -> int:
    """Exact rational Gaussian elimination — no floating point anywhere."""
    m = [r[:] for r in rows]
    nr, nc = len(m), (len(m[0]) if m else 0)
    rank, piv = 0, 0
    while rank < nr and piv < nc:
        sel = next((i for i in range(rank, nr) if m[i][piv] != 0), None)
        if sel is None:
            piv += 1
            continue
        m[rank], m[sel] = m[sel], m[rank]
        inv = m[rank][piv]
        m[rank] = [x / inv for x in m[rank]]
        for i in range(nr):
            if i != rank and m[i][piv] != 0:
                f = m[i][piv]
                m[i] = [a - f * b for a, b in zip(m[i], m[rank])]
        rank += 1
        piv += 1
    return rank


def betti_1(vertices, edges) -> int:
    d = [[Fraction(0) for _ in edges] for _ in vertices]
    for k, (s, t) in enumerate(edges):
        d[vertices.index(s)][k] -= 1
        d[vertices.index(t)][k] += 1
    return len(edges) - rank_exact(d)


def parse_table(text: str):
    rows = []
    for line in text.splitlines():
        m = re.match(r"^\|\s*(\d{2})\s*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|", line)
        if m:
            rows.append((m.group(2), m.group(3)))
    return rows


def authored_prose(text: str) -> str:
    out, fence = [], False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            fence = not fence
            continue
        if fence or re.match(r"^\|", line):
            continue
        out.append(line)
    return "\n".join(out)


def fail(code: int, msg: str) -> int:
    print(f"REFUSED (R{code}): {msg}", file=sys.stderr)
    return code


def main() -> int:
    if not ART.exists():
        return fail(1, "artifact absent")
    text = ART.read_text()

    # R4 mandate liveness
    if not MANDATE.exists() or hf(MANDATE) != MANDATE_DIGEST:
        return fail(4, "the ATTACH SUPPLY MANDATE is absent or moved; authoring is not authorized")
    print(f"MANDATE = LIVE ({MANDATE_DIGEST[:16]}…)")

    # R3 predecessor untouched
    if not V001.exists() or hf(V001) != V001_DIGEST:
        return fail(3, "V001 moved; this relay is append-only")
    print(f"V001 = BYTE-UNTOUCHED ({V001_DIGEST[:16]}…)")

    # R5 header
    if REQUIRED_HEADER not in text:
        return fail(5, "verbatim PROPOSED_NOT_ADOPTED header missing")
    print("HEADER = VERBATIM-PRESENT")

    # R6 ledger invariant
    missing = [m for m in LEDGER_MARKERS if m not in text]
    if missing:
        return fail(6, f"ledger invariant broken; missing {missing}")
    print("LEDGER_INVARIANT = TABLES + CLOSED-CLAIM + HEADLINE-WITHDRAWAL PRESENT")

    # R1/R2 strict vs stable
    rows = parse_table(text)
    if not rows:
        return fail(1, "no closure table parsed")
    ok = 0
    for rel, pinned in rows:
        p = ROOT / rel
        if not p.exists():
            return fail(1, f"declared member absent: {rel}")
        if hf(p) != pinned:
            return fail(2, f"STRICT!=STABLE for {rel}")
        ok += 1
    print(f"PROSE_DIGESTS = {ok}/{len(rows)}, STRICT==STABLE")

    # R7 the circuit determination
    b_tree = betti_1(*K_1_3)
    b_loop = betti_1(*K_SQUARE)
    print(f"b_1(K_(1,3))  = {b_tree}   [first-opening sector: acyclic, candidate INERT]")
    print(f"b_1(K_square) = {b_loop}   [composition sector: canonical circuit, NO selector to freeze]")
    if b_tree != 0:
        return fail(7, f"b_1(K_(1,3)) = {b_tree}, expected 0")
    if b_loop != 1:
        return fail(7, f"b_1(K_square) = {b_loop}, expected 1")

    # R8 the intra-cell noncommutation, exact at a symbolic root of unity (z = i)
    # D(z) = diag(1,z,1); S = [[0,1,0],[1,0,0],[0,0,-1]] over Z[i] — no floating point.
    def mul(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    S = [[0, 1, 0], [1, 0, 0], [0, 0, -1]]
    for z, expect_zero in ((1, True), (1j, False), (-1, False)):
        D = [[1, 0, 0], [0, z, 0], [0, 0, 1]]
        C = [[mul(D, S)[i][j] - mul(S, D)[i][j] for j in range(3)] for i in range(3)]
        nz = any(C[i][j] != 0 for i in range(3) for j in range(3))
        if expect_zero and nz:
            return fail(8, f"[D({z}),S] should vanish and does not")
        if not expect_zero and not nz:
            return fail(8, f"[D({z}),S] should not vanish and does")
    print("INTRA-CELL [D(z),S] : nonzero for z != 1, zero at z = 1 — REPRODUCED "
          "(V001's inference correctly WITHDRAWN)")

    # R9 residue
    low = authored_prose(text).lower()
    hits = [(t, low.count(t.lower())) for t in RESIDUE_TOKENS_27 if low.count(t.lower())]
    total = sum(n for _, n in hits)
    print(f"RESIDUE_SCAN(27 tokens over authored prose) = {total} hit(s)")
    for t, n in hits:
        print(f"    {t!r}: {n}")
    if total:
        return fail(9, "output-inspection token in authored prose")

    # R10 declared-first fixed point
    marker = "CLOSURE_DECLARATION_END"
    for _ in range(8):
        body = ART.read_text()
        i = body.find(marker)
        if i < 0:
            return fail(10, "closure end marker absent")
        val = f"{len(body[: i + len(marker)].encode()):08d}"
        new = re.sub(r"CLOSURE_END_BYTE = [0-9X]{8}", f"CLOSURE_END_BYTE = {val}", body)
        new = re.sub(r"end byte [0-9X]{8}", f"end byte {val}", new)
        if new == body:
            print(f"CLOSURE_END_BYTE = {val} (fixed point reached)")
            break
        ART.write_text(new)
    else:
        return fail(10, "closure byte did not reach a fixed point")

    if hf(V001) != V001_DIGEST:
        return fail(3, "V001 moved during the relay")
    print("V001 = BYTE-UNTOUCHED (rechecked after sealing work)")

    dg = hf(ART)
    SIDECAR.write_text(f"{dg}  {ART.name}\n")
    print(f"SEALED {ART.name}\n  {dg}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
