#!/usr/bin/env python3
"""Cycle 5: elimination with the sealed conditioned-star mediator (spec 22).

Written and executed strictly AFTER 22_..._SPEC_V001.md was sealed
(9fdceb82...). Verifies P1 (gap denominator), P2 (3/16), P3 (SW vs exact),
P4 (reduced family). require()-based; python -O safe; no measured constant.
"""
import math
import sys
from fractions import Fraction
import numpy as np


def require(cond, msg):
    if not cond:
        print("FAIL: " + msg)
        sys.exit(1)


SQ2 = math.sqrt(2.0)


def mediator(mu):
    B = np.array([[0.0, 1.0, 1.0],
                  [1.0, 0.0, 0.0],
                  [1.0, 0.0, 0.0]])
    return mu * B


def check_sealed_spectrum(mu):
    ev = np.linalg.eigvalsh(mediator(mu))
    target = np.array([-SQ2 * mu, 0.0, SQ2 * mu])
    require(np.allclose(np.sort(ev), np.sort(target), atol=1e-12),
            "sealed mediator spectrum mu*{-sqrt2,0,sqrt2}")


def sw_lambda_c(mu, g):
    """Second-order SW: sum over sealed intermediate levels; return
    (lambda_c, per-level connected contributions)."""
    H = mediator(mu)
    ev, V = np.linalg.eigh(H)
    g_idx = int(np.argmin(ev))
    ground = V[:, g_idx]
    # leaf occupation operators (basis: root, a, b)
    n_a = np.diag([0.0, 1.0, 0.0])
    n_b = np.diag([0.0, 0.0, 1.0])
    contribs = []
    lam = 0.0
    for e_idx in range(3):
        if e_idx == g_idx:
            continue
        exc = V[:, e_idx]
        dE = ev[e_idx] - ev[g_idx]
        require(dE > 0, "ground is lowest")
        m1 = float(exc @ n_a @ ground)   # couples to N_1
        m2 = float(exc @ n_b @ ground)   # couples to N_2
        # record operator at this channel: g*(m1 N_1 + m2 N_2)
        # -> -(g^2/dE) (m1 N_1 + m2 N_2)^2 ; N_i^2 = N_i
        # connected N_1 N_2 coefficient: -(g^2/dE) * 2 m1 m2
        contribs.append((ev[e_idx], -2.0 * g * g * m1 * m2 / dE))
        lam += -2.0 * g * g * m1 * m2 / dE
    return lam, contribs


def exact_lambda_c(mu, g):
    def ground_energy(r1, r2):
        Hb = mediator(mu) + g * np.diag([0.0, r1, r2])
        return float(np.linalg.eigvalsh(Hb)[0])
    return (ground_energy(1, 1) - ground_energy(0, 1)
            - ground_energy(1, 0) + ground_energy(0, 0))


def main():
    mu = 1.0
    check_sealed_spectrum(mu)
    m_star = SQ2 * mu

    # ---- P1 + P2: SW result ---------------------------------------------
    for g in (0.1, 0.03):
        lam, contribs = sw_lambda_c(mu, g)
        require(len(contribs) == 2, "both sealed intermediate levels appear")
        # both denominators are multiples of sqrt2*mu = m_*:
        for E_exc, _ in contribs:
            ratio = (E_exc - (-SQ2 * mu)) / m_star
            require(abs(ratio - round(ratio)) < 1e-12,
                    "P1: denominator is an integer multiple of the gap m_*")
        c = lam * m_star / (g * g)
        require(abs(c - 3.0 / 16.0) < 1e-12,
                "P2: structural coefficient 3/16 (got %.15f)" % c)
        # opposite connected signs of the two channels:
        signs = sorted(x[1] / abs(x[1]) for x in contribs)
        require(signs == [-1.0, 1.0], "P2: opposite-sign channels")
    print("P1 PASS: both intermediate denominators are multiples of the gap")
    print("         m_* = sqrt2*mu — the h_s fork resolves to the GAP")
    print("P2 PASS: lambda_c = (3/16) g_N^2/m_* exactly (channels +1/4, -1/16")
    print("         on 1/m_*, opposite signs, both levels contributing)")

    # ---- P3: exact vs SW — HONEST REPORT ---------------------------------
    # The sealed P3 claimed O(g^2/mu^2) convergence. Measure the actual
    # order empirically and test the g->0 limit; report refutation of the
    # sealed exponent if found (no repair of the sealed spec).
    gs = (0.08, 0.04, 0.02, 0.01)
    devs = []
    for g in gs:
        c_ex = exact_lambda_c(mu, g) * m_star / (g * g)
        devs.append(c_ex - 3.0 / 16.0)
        print("P3 data g=%.3f: c_exact=%.8f dev=%.3e" % (g, c_ex, devs[-1]))
    orders = [math.log(abs(devs[i] / devs[i + 1])) / math.log(gs[i] / gs[i + 1])
              for i in range(len(gs) - 1)]
    print("P3 measured convergence orders: %s" % ", ".join("%.3f" % o for o in orders))
    sealed_order_holds = all(o > 1.7 for o in orders)
    linear_order = all(0.8 < o < 1.2 for o in orders)
    require(not sealed_order_holds, "consistency: if sealed O(g^2) held, the "
            "original gate would not have failed")
    require(linear_order, "measured convergence is clean O(g): a third-order "
            "channel exists in the 3-level mediator")
    # Richardson extrapolation for a linear-order sequence: c0 = 2c(g/2)-c(g)
    c_04 = exact_lambda_c(mu, 0.04) * m_star / (0.04 ** 2)
    c_02 = exact_lambda_c(mu, 0.02) * m_star / (0.02 ** 2)
    c_01 = exact_lambda_c(mu, 0.01) * m_star / (0.01 ** 2)
    extrap1 = 2 * c_02 - c_04
    extrap2 = 2 * c_01 - c_02
    require(abs(extrap2 - 3.0 / 16.0) < 3e-4 and
            abs(extrap2 - 3.0 / 16.0) < abs(extrap1 - 3.0 / 16.0) + 1e-12,
            "g->0 limit confirms 3/16 (extrap %.6f)" % extrap2)
    print("P3 VERDICT: REFUTED AS SEALED — convergence is O(g), not O(g^2)")
    print("            (a third-order channel exists: the star ground state")
    print("            has asymmetric occupations, no odd-order cancellation).")
    print("            SUBSTANCE CONFIRMED: Richardson g->0 limit = %.6f ->" % extrap2)
    print("            leading coefficient 3/16 stands; P1/P2 unaffected.")

    # ---- P4: reduced surviving family (mechanical, exact) ----------------
    # rho = (3/16) gN^2/(m_* * E_ref); rates in units 1/T_R:
    # gN in {pi, pi/2}; m_* = pi; E_ref in {pi, pi/sqrt2}
    c_new = Fraction(3, 16)
    fam = set()
    for gc, ga in ((Fraction(1), 0), (Fraction(1, 2), 0)):      # pi-coeff, sqrt2-pow
        for ec, ea in ((Fraction(1), 0), (Fraction(1), -1)):
            coeff = c_new * gc * gc / (Fraction(1) * ec)
            a = 2 * 0 + 2 * ga - 0 - ea   # sqrt2 power (pi powers cancel: 2-1-1)
            while a >= 2:
                coeff, a = coeff * 2, a - 2
            while a <= -2:
                coeff, a = coeff / 2, a + 2
            fam.add((coeff, a))
    expect = {(Fraction(3, 16), 0), (Fraction(3, 16), 1),
              (Fraction(3, 64), 0), (Fraction(3, 64), 1)}
    require(fam == expect, "P4: reduced family {3/64, 3sqrt2/64, 3/16, 3sqrt2/16}")
    print("P4 PASS: with (c, h_s) -> (3/16, m_*) decided by computation, the")
    print("         surviving family reduces 6 -> 4:")
    for coeff, a in sorted(expect):
        s = str(coeff) + ("*sqrt2" if a == 1 else "")
        v = float(coeff) * (SQ2 if a == 1 else 1.0)
        print("           rho = %-12s = %.6f" % (s, v))
    print("\nCYCLE-5 OUTCOME: P1, P2, P4 CONFIRMED; P3 REFUTED AS SEALED")
    print("(convergence exponent wrong in spec; g->0 limit and leading")
    print("coefficient confirmed). No value is compared to anything.")
    print("alpha_computed=false")


if __name__ == "__main__":
    main()
