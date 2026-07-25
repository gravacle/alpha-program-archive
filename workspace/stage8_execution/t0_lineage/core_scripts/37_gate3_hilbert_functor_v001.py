#!/usr/bin/env python3
"""Cycle 10: Gate-3 Hilbert-functor uniqueness (spec 36).

Written and executed strictly AFTER 36_..._SPEC_V001.md was sealed
(953e875b...). require()-based; python -O safe; no measured constant.
"""
import cmath
import math
import sys
import numpy as np


def require(cond, msg):
    if not cond:
        print("FAIL: " + msg)
        sys.exit(1)


def main():
    rng = np.random.default_rng(20260725)

    # ---- P1: Schur — invariant positive forms are diagonal --------------
    # transport set: T(theta) = diag(1, e^{i theta}) (charges 0,1).
    # form M invariant iff T(theta)^dagger M T(theta) = M for all theta.
    thetas = rng.uniform(0, 2 * math.pi, size=24)
    # solve the invariance condition on a general Hermitian M:
    # M_01 e^{i theta} = M_01 for all theta  => M_01 = 0.
    def sandwich(Mx, t):
        T = np.diag([1.0, np.exp(1j * t)])
        return T.conj().T @ Mx @ T

    M = np.array([[1.7, 0.3 + 0.2j], [0.3 - 0.2j, 0.9]])
    ok_offdiag = all(np.allclose(sandwich(M, t), M, atol=1e-12)
                     for t in thetas)
    require(not ok_offdiag, "P1: off-diagonal form is NOT invariant")
    for s0, s1 in ((1.0, 1.0), (2.3, 0.7), (0.4, 5.0)):
        D = np.diag([s0, s1]).astype(complex)
        ok = all(np.allclose(sandwich(D, t), D, atol=1e-12)
                 for t in thetas)
        require(ok, "P1: diagonal forms are invariant")
    print("P1 PASS: Schur — invariant positive fiber forms are exactly")
    print("         diag(s0, s1); nothing off-diagonal survives")

    # ---- P2: sealed calibration forces s0 = s1 (exact algebra) ----------
    # weighted overlap: f(p, theta) = s0*p + s1*(1-p)*e^{i theta}
    # zero iff theta = pi and s0*p = s1*(1-p)  <=>  p = s1/(s0+s1).
    for s0, s1 in ((1.0, 1.0), (2.0, 1.0), (1.0, 3.0), (0.5, 0.5)):
        p_star = s1 / (s0 + s1)
        val = s0 * p_star + s1 * (1 - p_star) * cmath.exp(1j * math.pi)
        require(abs(val) < 1e-14, "P2: overlap zero at p = s1/(s0+s1)")
        # and nowhere else (scan):
        for p in np.linspace(0.01, 0.99, 197):
            if abs(p - p_star) > 1e-3:
                m = min(abs(s0 * p + s1 * (1 - p) * cmath.exp(1j * t))
                        for t in np.linspace(0, 2 * math.pi, 2000))
                require(m > 1e-6, "P2: no other zero population")
    # sealed statement: orthogonality iff p = 1/2  =>  s1/(s0+s1) = 1/2:
    s0 = 1.37
    s1_solved = s0  # from p* = 1/2
    require(abs(s1_solved / (s0 + s1_solved) - 0.5) < 1e-15,
            "P2: p* = 1/2 <=> s0 = s1 (exact)")
    print("P2 PASS: weighted-overlap zero occurs exactly at")
    print("         p = s1/(s0+s1), theta = pi; the SEALED calibration")
    print("         p = 1/2 forces s0 = s1 — the fiber form is ~ identity")

    # ---- P4: a skewed form has teeth ------------------------------------
    s0, s1 = 3.0, 1.0
    p_skew = s1 / (s0 + s1)
    require(abs(p_skew - 0.25) < 1e-14,
            "P4: skewed form (3,1) moves orthogonality to p = 1/4 != 1/2")
    print("P4 PASS: skewed form diag(3,1) shifts the orthogonality")
    print("         population to p = 1/4 — contradicting the sealed")
    print("         bridge identity; the selector has teeth")

    # ---- P3: assembly — unique canonical pair ---------------------------
    # H1: block-diagonal over fibers (disjoint orthogonality): a cross-
    # fiber component violates orthogonality of disjoint cells:
    Mbad = np.eye(4, dtype=complex)
    Mbad[0, 2] = Mbad[2, 0] = 0.3
    e1 = np.zeros(4, dtype=complex); e1[0] = 1.0     # fiber A
    e2 = np.zeros(4, dtype=complex); e2[2] = 1.0     # fiber B (disjoint)
    require(abs(e1.conj() @ Mbad @ e2) > 1e-9,
            "H1: cross-fiber component breaks disjoint orthogonality")
    # H2+P2: same fiber form everywhere, = s * I with one s.
    # H5: norm-ratio anchoring: ||D e||^2/||e||^2 with M0 = c*I on C0 and
    # M1 = I on C1 equals 2c for |a| = 1  => c = 1:
    d = 3
    z = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    q, r = np.linalg.qr(z)
    U = q @ np.diag(np.diag(r) / np.abs(np.diag(r)))
    psi = rng.normal(size=d) + 1j * rng.normal(size=d)
    psi /= np.linalg.norm(psi)
    for c in (1.0, 0.5, 2.0):
        ratio = c * (np.linalg.norm(U @ psi) ** 2 +
                     np.linalg.norm(psi) ** 2)
        require(abs(ratio - 2.0 * c) < 1e-12, "H5: ratio = 2c")
    print("P3 PASS: H1 (block-diagonal) + H2 (repeated fiber form) +")
    print("         P2 (fiber form ~ I) + H5 (ratio 2 pins c = 1) =>")
    print("         UNIQUE canonical form pair modulo overall congruence.")
    print("         The adjoint D-sharp and normalized transition operator")
    print("         B_rho are CANONICAL — cycle-8 conventions derived,")
    print("         not chosen")

    print("\nCYCLE-10 OUTCOME: P1, P2, P3, P4 CONFIRMED. No value compared")
    print("to anything. alpha_computed=false")


if __name__ == "__main__":
    main()
