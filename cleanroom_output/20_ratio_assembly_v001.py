#!/usr/bin/env python3
"""Cycle 4 assembly: rho = (1/4) g_N^2/(h_s E_ref) over ALL slot candidates.

Written after spec 19 (sealed 816abd2b...) and the citation-only enumeration
lane. Exact symbolic arithmetic: every value is (Fraction) * sqrt(2)^a *
pi^b * T_R^t. Guardrails: all combinations computed; none highlighted; no
comparison to anything (G2/G3). Fail-closed require(); python -O safe.
Rates are expressed in the package's sealed relational forms (hbar = 1).
"""
import sys
from fractions import Fraction


def require(cond, msg):
    if not cond:
        print("FAIL: " + msg)
        sys.exit(1)


class Sym:
    """value = coeff * sqrt2**a * pi**b * T_R**t  (exact)."""
    def __init__(self, coeff, a, b, t):
        self.c, self.a, self.b, self.t = Fraction(coeff), a, b, t

    def mul(self, o):
        return Sym(self.c * o.c, self.a + o.a, self.b + o.b, self.t + o.t)

    def div(self, o):
        return Sym(self.c / o.c, self.a - o.a, self.b - o.b, self.t - o.t)

    def sq(self):
        return self.mul(self)

    def canon(self):
        # fold sqrt2^2 -> 2 into coeff
        c, a = self.c, self.a
        while a >= 2:
            c, a = c * 2, a - 2
        while a <= -2:
            c, a = c / 2, a + 2
        return Sym(c, a, self.b, self.t)

    def label(self):
        s = self.canon()
        out = str(s.c)
        if s.a == 1:
            out += "*sqrt2"
        if s.a == -1:
            out += "/sqrt2"
        if s.b:
            out += "*pi^%d" % s.b if s.b != 1 else "*pi"
        if s.t:
            out += "*T_R^%d" % s.t
        return out

    def num(self):
        s = self.canon()
        import math
        return float(s.c) * (2 ** 0.5) ** s.a * math.pi ** s.b


# --- slot candidates (rates in sealed relational form; units 1/T_R) -------
# citations per enumeration lane record (see 21_..._RESULT for provenance)
G_N = [
    ("marker pi*hbar per T_R      [bridge gate]", Sym(1, 0, 1, -1)),
    ("FS budget (pi*hbar/2)/T_R   [onset gate]", Sym(Fraction(1, 2), 0, 1, -1)),
]
H_S = [
    ("gap m_* = pi/T_R            [Schur pole]", Sym(1, 0, 1, -1)),
    ("hop mu = (pi/sqrt2)/T_R     [Schur pole]", Sym(1, -1, 1, -1)),
]
E_REF = [
    ("E_*/m_* = pi/T_R            [Schur pole]", Sym(1, 0, 1, -1)),
    ("mu = hbar*tau_R/T_R^2 ~ (pi/sqrt2)/T_R [first-opening]", Sym(1, -1, 1, -1)),
    ("bare hbar/T_R  ** G1-FLAGGED: beyond sealed form **", Sym(1, 0, 0, -1)),
]

C_STRUCT = Sym(Fraction(1, 4), 0, 0, 0)  # cycle-3 coefficient, sealed


def main():
    rows = []
    for gl, g in G_N:
        for hl, h in H_S:
            for el, e in E_REF:
                rho = C_STRUCT.mul(g.sq()).div(h.mul(e)).canon()
                # P1: T_R must cancel exactly
                require(rho.t == 0, "P1 violated: T_R survives in a combo")
                flagged = "FLAGGED" if "FLAGGED" in el else "ok"
                rows.append((rho.label(), rho.num(), flagged, gl, hl, el))
    require(len(rows) == 12, "cartesian product complete (2*2*3)")
    print("P1 PASS: T_R cancels in every combination — the dimensionless")
    print("ratio is independent of the free interval (Families A/C do not")
    print("infect rho). Full table (G2: complete, nothing highlighted):\n")
    print("%-14s %-10s %-8s  provenance" % ("rho (exact)", "numeric", "status"))
    for lab, num, flag, gl, hl, el in rows:
        print("%-14s %-10.6f %-8s  gN=%s | hs=%s | Eref=%s"
              % (lab, num, flag, gl.split("[")[0].strip(),
                 hl.split("[")[0].strip(), el.split("*")[0].strip()))
    unflagged = sorted(set(l for l, n, f, *_ in rows if f == "ok"))
    print("\nDistinct unflagged exact values (%d):" % len(unflagged))
    for v in unflagged:
        print("  " + v)
    flagged_vals = sorted(set(l for l, n, f, *_ in rows if f != "ok"))
    print("Distinct G1-flagged exact values (%d, carried per spec, "
          "not repaired):" % len(flagged_vals))
    for v in flagged_vals:
        print("  " + v)
    print("\nVERDICT INPUT (per G4): three slots carry unresolved sealed")
    print("forks with no in-package selector (enumeration lane record);")
    print("a DISCRETE FAMILY survives. No value is compared to anything.")
    print("alpha_computed=false")


if __name__ == "__main__":
    main()
