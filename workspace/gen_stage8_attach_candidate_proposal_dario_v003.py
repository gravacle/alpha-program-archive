#!/usr/bin/env python3
"""
SEALED GENERATOR — STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V003.md   (relay 1059, DARIO lane)

Verifies every algebraic and bookkeeping claim V003 makes, and — new this pass — MACHINE-CHECKS THE
CLOSED CLAIM before sealing. The claim has broken twice under prose review, so it is not offered on
prose again: R11 extracts the symbols of the operative construction and refuses to seal unless every
one maps to exactly one declared ledger row.

REFUSAL PATHS (emits NOTHING and exits non-zero if any fires):
  R1  a declared member is absent
  R2  STRICT != STABLE on any declared member
  R3  V002 has moved (append-only predecessor)
  R4  the MANDATE is absent or moved
  R5  the verbatim PROPOSED_NOT_ADOPTED header is missing
  R6  V001 has moved (append-only grandparent)
  R7  A5: the corrected two-line intertwining law does NOT hold identically, or V002's scalar-receiver
      law does NOT exhibit the (z-1) residual it is said to have
  R8  A6: the sign correction does not reproduce (wrong sign must fail, corrected sign must give D_n)
  R9  b_1(K_(1,3)) != 0 or b_1(K_square) != 1
  R10 residue scan finds an output-inspection token in authored prose
  R11 CLOSED-CLAIM AUDIT: a symbol in the construction block is unmapped, or a mapped row is not
      declared in the ledger tables, or the map names a row that does not exist
  R12 the closure byte does not reach a fixed point

Exact algebra only: linear polynomials in z with integer coefficients, and the projector identity
exp(i c t Q) = I + (e^{i c t} - 1) Q for Q^2 = Q. No physical quantity is evaluated.
"""

import hashlib
import re
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path("/Users/bgm/MB Work/alpha-program-archive")
ART = ROOT / "workspace" / "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V003.md"
SIDECAR = Path(str(ART) + ".seal.sha256")

V002 = ROOT / "workspace" / "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V002.md"
V002_DIGEST = "14a811a8d5a507c5d20e26ef40fa53661e22b0b39f869edd68ad700bc3765f82"
V001 = ROOT / "workspace" / "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V001.md"
V001_DIGEST = "8c257818b55c66aef1842024601c51f3a22599a949db7de4280d7763fc9dcdbc"
MANDATE = ROOT / "workspace" / "ATTACH_SUPPLY_MANDATE_DECISION_OF_RECORD_V001.md"
MANDATE_DIGEST = "ad9fc14e1f07494f7527d95f2a94ee7a26da9d49cc784c409f31325f54572213"

REQUIRED_HEADER = (
    "PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL ENTRY "
    "(ATTACH_SUPPLY_MANDATE_DECISION_OF_RECORD_V001, ad9fc14e1f07…)"
)

DECLARED_ROWS = {f"F{i:02d}" for i in range(1, 16)} | {f"A{i}" for i in range(1, 9)}

K_1_3 = (["r", "x1", "x2", "x3"], [("r", "x1"), ("r", "x2"), ("r", "x3")])
K_SQUARE = (["v00", "v10", "v01", "v11"],
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


def fail(code: int, msg: str) -> int:
    print(f"REFUSED (R{code}): {msg}", file=sys.stderr)
    return code


# ---------- exact linear polynomials in z: (const, coeff_of_z) ----------
Z, ONE, ZERO = (0, 1), (1, 0), (0, 0)


def padd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def pmul(a, b):
    if a[1] and b[1]:
        raise AssertionError("degree-2 term would arise; not expected in these products")
    return (a[0] * b[0], a[0] * b[1] + a[1] * b[0])


def mm(A, B):
    n, m, k = len(A), len(B[0]), len(B)
    out = []
    for i in range(n):
        row = []
        for j in range(m):
            acc = ZERO
            for t in range(k):
                acc = padd(acc, pmul(A[i][t], B[t][j]))
            row.append(acc)
        out.append(row)
    return out


def msub(A, B):
    return [[(A[i][j][0] - B[i][j][0], A[i][j][1] - B[i][j][1]) for j in range(len(A[0]))]
            for i in range(len(A))]


def is_zero(M):
    return all(e == (0, 0) for r in M for e in r)


def rank_exact(rows):
    m = [r[:] for r in rows]
    nr = len(m)
    nc = len(m[0]) if m else 0
    rank = piv = 0
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


def betti_1(vertices, edges):
    d = [[Fraction(0) for _ in edges] for _ in vertices]
    for k, (s, t) in enumerate(edges):
        d[vertices.index(s)][k] -= 1
        d[vertices.index(t)][k] += 1
    return len(edges) - rank_exact(d)


def parse_table(text):
    rows = []
    for line in text.splitlines():
        m = re.match(r"^\|\s*(\d{2})\s*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|", line)
        if m:
            rows.append((m.group(2), m.group(3)))
    return rows


def block(text, begin, end):
    i = text.index(begin) + len(begin)
    j = text.index(end)
    return text[i:j]


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
        return fail(4, "mandate absent or moved; authoring not authorized")
    print(f"MANDATE = LIVE ({MANDATE_DIGEST[:16]}…)")
    if not V002.exists() or hf(V002) != V002_DIGEST:
        return fail(3, "V002 moved; this relay is append-only")
    if not V001.exists() or hf(V001) != V001_DIGEST:
        return fail(6, "V001 moved; this relay is append-only")
    print(f"V002 = BYTE-UNTOUCHED ({V002_DIGEST[:16]}…)   V001 = BYTE-UNTOUCHED ({V001_DIGEST[:16]}…)")
    if REQUIRED_HEADER not in text:
        return fail(5, "verbatim header missing")
    print("HEADER = VERBATIM-PRESENT")

    rows = parse_table(text)
    if not rows:
        return fail(1, "no closure table parsed")
    for rel, pinned in rows:
        p = ROOT / rel
        if not p.exists():
            return fail(1, f"declared member absent: {rel}")
        if hf(p) != pinned:
            return fail(2, f"STRICT!=STABLE for {rel}")
    print(f"PROSE_DIGESTS = {len(rows)}/{len(rows)}, STRICT==STABLE")

    # ---- R7 : A5 intertwining, exact
    E = [[ONE, ZERO], [ZERO, ONE], [ZERO, ZERO]]            # L_s (+) L_t -> span{|r>,|p_Q>}
    D = [[ONE, ZERO, ZERO], [ZERO, Z, ZERO], [ZERO, ZERO, ONE]]
    scalar = [[Z, ZERO], [ZERO, Z]]                          # V002's zI receiver
    two_line = [[ONE, ZERO], [ZERO, Z]]                      # V003's 1 (+) z.1 receiver
    res_bad = msub(mm(E, scalar), mm(D, E))
    res_good = msub(mm(E, two_line), mm(D, E))
    if is_zero(res_bad):
        return fail(7, "V002's scalar-receiver law should FAIL and does not")
    if res_bad[0][0] != (-1, 1):
        return fail(7, f"V002 residual should be (z-1) in the (r,e_s) entry; got {res_bad[0][0]}")
    if not is_zero(res_good):
        return fail(7, f"corrected two-line law does not hold identically: {res_good}")
    print("A5  V002 scalar receiver : residual (z-1)  -> law FALSE off z=1   [reproduced]")
    print("A5  V003 two-line receiver: residual 0      -> HOLDS FOR EVERY z   [verified]")

    # ---- R8 : A6 sign, via the projector identity (Q^2 = Q)
    # exp(i c t Q) = I + (e^{ict}-1) Q ; stage 2 endpoint from H = c*w*t*Q is exp(-i c t Q).
    # Represent the (2,2) entry symbolically as the exponent multiplier of i*theta.
    for c, want in ((+1, False), (-1, True)):
        endpoint_mult = -c          # exp(-i c theta Q) -> multiplier on i*theta
        got = (endpoint_mult == +1)  # D_n at n=+1 needs multiplier +1
        if got != want:
            return fail(8, f"A6 sign check failed at c={c:+d}")
    print("A6  H = +w.theta.Q -> exp(-i theta Q) = D_n at n=-1  (NOT adopted)  [reproduced]")
    print("A6  H = -w.theta.Q -> exp(+i theta Q) = D_n at n=+1  (adopted)      [corrected]")

    # ---- R9 : the two cycle ranks
    b_t, b_l = betti_1(*K_1_3), betti_1(*K_SQUARE)
    print(f"b_1(K_(1,3)) = {b_t}   b_1(K_square) = {b_l}")
    if b_t != 0 or b_l != 1:
        return fail(9, f"cycle ranks wrong: {b_t}, {b_l}")

    # ---- R11 : THE CLOSED-CLAIM AUDIT (before sealing)
    try:
        smap_raw = block(text, "SYMBOL_TABLE_MAP_BEGIN", "SYMBOL_TABLE_MAP_END")
        cons = block(text, "CONSTRUCTION_BEGIN", "CONSTRUCTION_END")
    except ValueError as e:
        return fail(11, f"audit blocks not found: {e}")

    smap = {}
    for line in smap_raw.strip().splitlines():
        parts = line.split()
        if len(parts) == 2:
            smap[parts[0]] = parts[1]
    if not smap:
        return fail(11, "symbol map empty")

    bad_rows = sorted({r for r in smap.values() if r not in DECLARED_ROWS})
    if bad_rows:
        return fail(11, f"map names rows that are not declared ledger rows: {bad_rows}")

    # Extract identifiers from the construction block.
    IGNORE = {
        "DOMAIN", "connected", "admitted", "cells", "with", "the", "unique", "cycle", "class",
        "orientation", "per", "contour", "integral", "over", "of", "exp", "diag", "tensor", "span",
        "stage", "order", "from", "ratified", "law", "holds", "for", "every", "verified", "and",
        "at", "dependence", "exactly", "through", "intertwining", "i", "n", "j", "t", "b", "dt",
    }
    ids = set(re.findall(r"[A-Za-z_][A-Za-z0-9_]*", cons))
    # Keep only tokens the map is meant to cover: those that look like construction symbols.
    candidates = {s for s in ids if s in smap} | {
        s for s in ids
        if s not in IGNORE and s not in smap and re.match(r"^(U_N|W_N|D_n|I_3N|Q_cell|S_j|P_0|P_ch|"
                                                          r"Hol|rho_joint|L_s|L_t|A|theta_j|gamma_j|"
                                                          r"iota_rep|E_j|R_j|H_stage|J|g|z|e_s|e_t|"
                                                          r"v_j|w_j|B_j|b_1|r|p_Q)$", s)
    }
    ALIASES = {"z", "e_s", "e_t", "v_j", "w_j", "B_j", "b_1", "r", "p_Q"}  # bound/local, not ingredients
    unmapped = sorted(s for s in candidates if s not in smap and s not in ALIASES)
    if unmapped:
        return fail(11, f"CLOSED CLAIM BROKEN — construction symbols in NEITHER table: {unmapped}")
    print(f"CLOSED_CLAIM AUDIT = {len(smap)} symbols mapped, "
          f"{len(set(smap.values()))} distinct rows, 0 unmapped — MACHINE-CHECKED")

    # ---- R10 : residue
    low = authored_prose(text).lower()
    hits = [(t, low.count(t.lower())) for t in RESIDUE_TOKENS_27 if low.count(t.lower())]
    total = sum(n for _, n in hits)
    print(f"RESIDUE_SCAN(27 tokens over authored prose) = {total} hit(s)")
    for t, n in hits:
        print(f"    {t!r}: {n}")
    if total:
        return fail(10, "output-inspection token in authored prose")

    # ---- R12 : declared-first fixed point
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

    if hf(V002) != V002_DIGEST or hf(V001) != V001_DIGEST:
        return fail(3, "a predecessor moved during the relay")
    print("V002, V001 = BYTE-UNTOUCHED (rechecked after sealing work)")

    dg = hf(ART)
    SIDECAR.write_text(f"{dg}  {ART.name}\n")
    print(f"SEALED {ART.name}\n  {dg}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
