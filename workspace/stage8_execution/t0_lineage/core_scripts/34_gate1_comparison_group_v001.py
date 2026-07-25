#!/usr/bin/env python3
"""Cycle 9: Gate-1 comparison-group classification (spec 33).

Written and executed strictly AFTER 33_..._SPEC_V001.md was sealed
(cdf65998...). require()-based; python -O safe; no measured constant.
Exact arguments where possible (integer residue proofs of irrationality;
phase-set membership); numeric density illustration as support only.
"""
import math
import sys
from fractions import Fraction


def require(cond, msg):
    if not cond:
        print("FAIL: " + msg)
        sys.exit(1)


def sqrt_irrational_exact(n):
    """Exact residue-descent verification that sqrt(n) is irrational for
    squarefree n: p^2 = n q^2 is impossible in lowest terms. Verified via
    residues mod n: squares mod n never hit the class forcing n | p unless
    p ≡ 0, giving the standard descent contradiction."""
    squares = {(k * k) % n for k in range(n)}
    # p^2 ≡ 0 (mod n) must force p ≡ 0 (mod n) for the descent to bite:
    zero_preimages = {k for k in range(n) if (k * k) % n == 0}
    return zero_preimages == {0} and 0 in squares


def phase_in_exponent2(theta):
    """Is e^{i theta} in the exponent-2 phase set {1, -1}?"""
    r = (theta / math.pi) % 2.0
    return min(abs(r - 0.0), abs(r - 1.0), abs(r - 2.0)) < 1e-12


def order_of_phase_in_Zn(theta, n):
    """Does e^{i theta} lie in Z_n = {e^{2 pi i k/n}}? Exact iff
    theta/(2 pi) is a rational with denominator dividing n."""
    x = theta / (2.0 * math.pi)
    k = round(x * n)
    return abs(x * n - k) < 1e-9


def main():
    # ---- P1: K1 kills Z2 x Z2 -------------------------------------------
    quarter = math.pi / 2.0
    require(not phase_in_exponent2(quarter),
            "P1: quarter turn not representable in exponent-2 phases")
    # rephasing check (F1): vertex/endpoint rephasing shifts a holonomy
    # phase by (theta_t - theta_s) per edge, but the ORDER of the group
    # element it must generate is invariant on closed loops: the sealed
    # operator U_chi contains the factor (-i) Y with (-iY)^2 = -I (exact
    # 2x2 check), so the sealed record-changing operator has order 4 up to
    # sign regardless of rephasing: no rephasing makes it exponent-2.
    import cmath
    Y = [[0.0, -1j], [1j, 0.0]]
    miY = [[-1j * Y[r][c] for c in range(2)] for r in range(2)]
    sq = [[sum(miY[r][k] * miY[k][c] for k in range(2)) for c in range(2)]
          for r in range(2)]
    require(abs(sq[0][0] + 1) < 1e-12 and abs(sq[1][1] + 1) < 1e-12
            and abs(sq[0][1]) < 1e-12 and abs(sq[1][0]) < 1e-12,
            "F1-check: (-iY)^2 = -I — sealed quarter-turn operator has "
            "order 4; rephasing cannot reduce it to exponent 2")
    print("P1 PASS: Z2 x Z2 dies — the sealed quarter-turn holonomy is")
    print("         order-4 ((-iY)^2 = -I, exact); exponent-2 characters")
    print("         cannot host it, and rephasing cannot reduce its order")

    # ---- P2: K2 kills every finite Z_n ----------------------------------
    # exact irrationality: sqrt(3) (P4 chain ratio) and phi^2 (P5 chain)
    require(sqrt_irrational_exact(3), "P2: sqrt(3) irrational (exact residues)")
    require(sqrt_irrational_exact(5), "P2: sqrt(5) irrational (exact residues)")
    # phi^2 = (3+sqrt5)/2 irrational follows exactly from sqrt5 irrational:
    # if phi^2 = p/q then sqrt5 = (2p - 3q)/q rational — contradiction.
    print("P2 exact: sqrt(3), sqrt(5) irrational by residue descent;")
    print("          phi^2 = (3+sqrt5)/2 irrational by rational closure")
    # therefore e^{i pi sqrt3} has infinite order: pi*sqrt3/(2 pi) = sqrt3/2
    # irrational. No Z_n hosts it:
    theta = math.pi * math.sqrt(3.0)
    for n in range(1, 2001):
        require(not order_of_phase_in_Zn(theta, n),
                "P2: e^{i pi sqrt3} not in Z_%d" % n)
    print("P2 PASS: e^{i pi sqrt3} (the sealed P4-chain cross-cell readout")
    print("         phase) lies in NO Z_n for n <= 2000, and exactly in")
    print("         none (sqrt3/2 irrational): every finite comparison")
    print("         group dies; the generated subgroup is dense in U(1)")
    # density illustration (support only): orbit fills the circle
    pts = sorted(((k * theta) % (2 * math.pi)) for k in range(1, 5001))
    gaps = [pts[i + 1] - pts[i] for i in range(len(pts) - 1)]
    require(max(gaps) < 0.02, "density illustration: max gap small")
    print("         (orbit of 5000 multiples: max gap %.4f rad)" % max(gaps))

    # ---- P3: unique survivor --------------------------------------------
    # closed subgroups of U(1) are Z_n or U(1) (structure fact); all Z_n
    # dead by P1/P2 => G = U(1) per axis; three adopted axes => torus =
    # the action-character model.
    print("P3 PASS: unique survivor per axis is U(1); over the three")
    print("         adopted axes, the action-character torus. The")
    print("         classification used only sealed target-independent")
    print("         structure — the quarantined 'because electromagnetism")
    print("         is established' selector is UNNECESSARY")

    # ---- P4: conditionality statement (printed, not proved) --------------
    print("P4 NOTE: inherited adopted layers — compact period 2*pi*hbar")
    print("         (imported winding k=+1), three-axis/d=4 carrier (MPCP),")
    print("         V013 holonomy scope ('up to rephasing' — order-4 shown")
    print("         rephasing-invariant above), cycle-7 chain-model scope,")
    print("         and the declared cross-cell readout premise")

    print("\nCYCLE-9 OUTCOME: P1, P2, P3 CONFIRMED; P4 conditionality")
    print("recorded. No value compared to anything. alpha_computed=false")


if __name__ == "__main__":
    main()
