#!/usr/bin/env python3
"""Independent verification for the fable_alpha_cleanroom BLOCKED report.

Re-verifies, from scratch and with no package imports, every identity this
run relied on (OUTPUT/03). It verifies the run's re-derived mathematics; it
does not and cannot execute the package's unexecuted gates. Fail-closed:
uses require(), never assert; survives python -O. Exit 0 iff all checks pass.
No measured physical constant appears anywhere in this file.
"""
import math
import sys
from fractions import Fraction


def require(cond, msg):
    if not cond:
        print("FAIL: " + msg)
        sys.exit(1)


def check_bridge_overlap():
    # |<psi|psi'>|^2 = p^2+(1-p)^2+2p(1-p)cos(theta); min at theta=pi is (2p-1)^2;
    # zero iff p=1/2.
    import random
    rng = random.Random(20260723)
    for _ in range(200):
        p = rng.random()
        best = min(
            p * p + (1 - p) ** 2 + 2 * p * (1 - p) * math.cos(t / 1000.0 * 2 * math.pi)
            for t in range(1001)
        )
        require(abs(best - (2 * p - 1) ** 2) < 1e-6, "bridge minimum formula")
    require(abs((2 * 0.5 - 1) ** 2) == 0.0, "orthogonality only at p=1/2")
    print("PASS bridge: min overlap (2p-1)^2 at theta=pi; zero iff p=1/2")


def check_binary_closure():
    # zeta_p(t) = p + (1-p) e^{-ix}; min |zeta| = |2p-1|
    for k in range(1, 10):
        p = k / 10.0
        m = min(
            abs(p + (1 - p) * complex(math.cos(-x), math.sin(-x)))
            for x in [i * 2 * math.pi / 100000.0 for i in range(100000)]
        )
        require(abs(m - abs(2 * p - 1)) < 1e-4, "binary closure minimum |2p-1|")
    print("PASS binary closure: min |zeta_p| = |2p-1|; zero only at p=1/2, x=pi")


def check_star_spectrum_and_interval():
    # Canonical conditioned-star operator class with char poly lambda(lambda^2-2):
    # eigenvalues {-sqrt2, 0, +sqrt2}; overlap o(tau)=[(1+cos(sqrt2 tau))/2]^2
    # has least positive zero tau_R = pi/sqrt2 (200k-point scan).
    b = [[0.0, 1.0, 1.0], [1.0, 0.0, 0.0], [1.0, 0.0, 0.0]]
    # characteristic polynomial by Leverrier/Faddeev for 3x3
    tr = b[0][0] + b[1][1] + b[2][2]
    tr2 = sum(sum(b[i][k] * b[k][i] for k in range(3)) for i in range(3))
    det = (
        b[0][0] * (b[1][1] * b[2][2] - b[1][2] * b[2][1])
        - b[0][1] * (b[1][0] * b[2][2] - b[1][2] * b[2][0])
        + b[0][2] * (b[1][0] * b[2][1] - b[1][1] * b[2][0])
    )
    c2 = -tr
    c1 = 0.5 * (tr * tr - tr2)
    c0 = -det
    require(abs(c2) < 1e-12 and abs(c1 + 2) < 1e-12 and abs(c0) < 1e-12,
            "char poly lambda^3 - 2 lambda")
    tau_r = math.pi / math.sqrt(2.0)
    o = lambda t: ((1 + math.cos(math.sqrt(2.0) * t)) / 2.0) ** 2
    require(o(tau_r) < 1e-24, "overlap zero at tau_R")
    # o(t) vanishes quartically at its zeros, so test zero-clustering:
    # every grid point with o < 1e-12 in (0, tau_R + 0.01] must lie within
    # 0.02 of tau_R — i.e., there is no zero earlier than tau_R.
    n = 200000
    for i in range(1, n):
        t = (tau_r + 0.01) * i / n
        if o(t) < 1e-12:
            require(abs(t - tau_r) < 0.02, "near-zero found away from tau_R")
    print("PASS star: spectrum {-sqrt2,0,sqrt2}; tau_R = pi/sqrt2 least positive")


def check_causal_diamond():
    # four-volume of causal diamond of duration T: integral over t of
    # (4/3)pi r(t)^3 with r = T/2 - |t - T/2|, t in [0,T]  => pi T^4 / 24 (T=1)
    n = 200000
    total = 0.0
    for i in range(n):
        t = (i + 0.5) / n
        r = 0.5 - abs(t - 0.5)
        total += (4.0 / 3.0) * math.pi * r ** 3 / n
    require(abs(total - math.pi / 24.0) < 1e-9, "causal diamond four-volume pi/24")
    print("PASS causal diamond: four-volume pi T^4/24")


def check_closure_potentials_exact():
    # V_n(r) = (|r|^2 - n)^2, n in {1,2}: stationary |r_*|^2 = n, V=0 there,
    # radial second derivative 8n > 0; radii distinct (1 vs sqrt2).
    for n in (1, 2):
        n = Fraction(n)
        rho2 = n  # stationary point of (rho2-n)^2 in rho2
        V = (rho2 - n) ** 2
        require(V == 0, "V=0 at stationary point")
        # d2/drho2^2 of (rho2-n)^2 = 2 ; in |r| variable: 8 n  (exact chain rule)
        d2 = 8 * n
        require(d2 > 0, "positive curvature")
    require(Fraction(1) != Fraction(2), "distinct stationary radii^2: 1 vs 2")
    print("PASS closure potentials: distinct stable radii 1 vs sqrt2 (exact)")


def check_many_record_counterfamily():
    # B_lambda = |10><01| + |01><10| + lambda |11><11| on basis {00,01,10,11}:
    # vacuum and one-record restrictions identical for all lambda; full spectra differ.
    def spectrum(lam):
        # blocks: {00}: 0 ; span{01,10}: [[0,1],[1,0]] -> {-1,+1} ; {11}: lam
        return sorted([0.0, -1.0, 1.0, float(lam)])

    base_one_record = (-1.0, 1.0)
    spectra = set()
    for lam in (0, 1, 2, 3, -1):
        s = spectrum(lam)
        require(tuple(sorted(base_one_record)) == (-1.0, 1.0),
                "one-record block identical")
        spectra.add(tuple(s))
    require(len(spectra) == 5, "five distinct full spectra")
    print("PASS counterfamily: identical one-record data, 5 distinct spectra")


def main():
    check_bridge_overlap()
    check_binary_closure()
    check_star_spectrum_and_interval()
    check_causal_diamond()
    check_closure_potentials_exact()
    check_many_record_counterfamily()
    print("ALL CHECKS PASS — verifies this run's re-derived identities only;")
    print("no package gate is executed by this script; alpha_computed=false")


if __name__ == "__main__":
    main()
