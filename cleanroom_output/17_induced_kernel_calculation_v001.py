#!/usr/bin/env python3
"""Cycle 3: induced record-record kernel from source elimination (spec 16).

Written and executed strictly AFTER 16_..._SPEC_V001.md was sealed
(49bd8fbf...). Two methods (2nd-order SW elimination; exact diagonalization)
plus the DC1 filter. Fail-closed require(); python -O safe; no measured
constant; all scales are formal model symbols.
Basis: source in {site1, site2} (one particle) x R1 x R2 (qubits) = 8-dim.
Ordering: |s, r1, r2> with s in {1,2}, r_i in {0,1}; index = 4*(s-1)+2*r1+r2.
"""
import sys
import numpy as np


def require(cond, msg):
    if not cond:
        print("FAIL: " + msg)
        sys.exit(1)


I2 = np.eye(2)
N = np.array([[0.0, 0.0], [0.0, 1.0]])
X = np.array([[0.0, 1.0], [1.0, 0.0]])


def kron3(a, b, c):
    return np.kron(a, np.kron(b, c))


def build_H(h_s, g_N, g_X):
    # source hop: -h_s (|1><2| + |2><1|)_source  (x) I4
    hop_s = np.array([[0.0, -h_s], [-h_s, 0.0]])
    H = kron3(hop_s, I2, I2)
    # site occupation projectors in one-particle sector:
    P1 = np.array([[1.0, 0.0], [0.0, 0.0]])
    P2 = np.array([[0.0, 0.0], [0.0, 1.0]])
    # b_ii couplings: n_i (x) (g_N N_i + g_X X_i)
    H += kron3(P1, g_N * N + g_X * X, I2)
    H += kron3(P2, I2, g_N * N + g_X * X)
    return H


def record_basis_labels():
    return ["00", "01", "10", "11"]


def sw_effective(h_s, g_N, g_X):
    """Second-order effective record Hamiltonian, source ground (bonding)."""
    # source eigenstates: |-> = (|1>+|2>)/sqrt2 (E=-h_s), |+> = (|1>-|2>)/sqrt2 (E=+h_s)
    # coupling operator: V = P1 (x) B1 + P2 (x) B2,  B_i = g_N N_i + g_X X_i
    # <-|P1|-> = <-|P2|-> = 1/2 ; <+|P1|-> = 1/2, <+|P2|-> = -1/2
    B1 = g_N * N + g_X * X
    B2 = g_N * N + g_X * X
    B1f = np.kron(B1, I2)
    B2f = np.kron(I2, B2)
    first = 0.5 * (B1f + B2f)
    # V_{+-} = (1/2)(B1f - B2f); energy denominator E- - E+ = -2 h_s
    Vpm = 0.5 * (B1f - B2f)
    second = -(Vpm @ Vpm) / (2.0 * h_s)
    return first, second


def dc1_filter(M):
    """Project a 4x4 record operator onto the registration-diagonal algebra."""
    D = np.zeros((4, 4))
    for k in range(4):
        D[k, k] = M[k, k]
    return D


def connected_lambda(Mdiag):
    """lambda_c = E(11) - E(01) - E(10) + E(00) from a diagonal record op."""
    return Mdiag[3, 3] - Mdiag[1, 1] - Mdiag[2, 2] + Mdiag[0, 0]


def main():
    h_s = 1.0

    # ---- P2 asymmetry: pure writing coupling (g_N = 0) ------------------
    _, sec_X = sw_effective(h_s, 0.0, 0.37)
    d = dc1_filter(sec_X)
    lam_X = connected_lambda(d)
    # induced connected part must be X1X2-type (off-diagonal): DC1 filter -> 0
    require(abs(lam_X) < 1e-14, "P2: writing-type induces no DC1 lambda_c")
    offdiag_norm = np.linalg.norm(sec_X - dc1_filter(sec_X))
    require(offdiag_norm > 1e-3, "P2: writing-type DOES induce (filtered) terms")
    print("P2a PASS: g_X-only induced kernel is entirely DC1-inadmissible "
          "(filtered to zero); lambda_c = %.3e" % lam_X)

    # ---- P1+P3: pure phase coupling ------------------------------------
    for g_N in (0.2, 0.11, 0.05):
        _, sec_N = sw_effective(h_s, g_N, 0.0)
        d = dc1_filter(sec_N)
        require(np.linalg.norm(sec_N - d) < 1e-14,
                "phase-type induced kernel is already diagonal")
        lam = connected_lambda(d)
        require(abs(lam) > 1e-12, "P1: nonzero connected induced kernel")
        c = lam * h_s / (g_N ** 2)
        require(abs(c - 0.25) < 1e-12,
                "P3: structural coefficient c = 1/4 (got %.15f)" % c)
    print("P1/P3 PASS (SW): lambda_c = (1/4) g_N^2/h_s exactly; "
          "c independent of g_N")

    # ---- mixed coupling: asymmetry survives -----------------------------
    _, sec_M = sw_effective(h_s, 0.13, 0.29)
    lam_M = connected_lambda(dc1_filter(sec_M))
    c_M = lam_M * h_s / (0.13 ** 2)
    require(abs(c_M - 0.25) < 1e-12,
            "P2b: mixed coupling — lambda_c comes only from g_N (c=%.12f)" % c_M)
    print("P2b PASS: with both couplings, lambda_c = (1/4) g_N^2/h_s — "
          "g_X contributes nothing to the durable connected part")

    # ---- F2 cross-check: exact diagonalization -------------------------
    # Extract effective diagonal record energies from exact spectrum:
    # for g_X=0 the full H is block-diagonal in the record basis (N_i
    # conserved); within each record sector (r1,r2) the source sees
    # potential (g_N r1, g_N r2); ground energy of 2x2 block:
    #   E(r1,r2) = (g_N(r1+r2))/2 - sqrt(h_s^2 + (g_N(r1-r2)/2)^2)
    # lambda_c^exact = E(11)-E(01)-E(10)+E(00).
    for g_N in (0.2, 0.05, 0.01):
        H = build_H(h_s, g_N, 0.0)
        # verify block structure: [H, N_i] = 0
        N1f = kron3(I2, N, I2)
        N2f = kron3(I2, I2, N)
        require(np.linalg.norm(H @ N1f - N1f @ H) < 1e-12 and
                np.linalg.norm(H @ N2f - N2f @ H) < 1e-12,
                "exact H conserves registration content when g_X=0")
        Es = {}
        for r1 in (0, 1):
            for r2 in (0, 1):
                block = np.array([
                    [g_N * r1, -h_s],
                    [-h_s, g_N * r2]])
                Es[(r1, r2)] = np.linalg.eigvalsh(block)[0]
        lam_exact = Es[(1, 1)] - Es[(0, 1)] - Es[(1, 0)] + Es[(0, 0)]
        # closed form: E(11)-E(00) = g_N ; E(01)+E(10) = g_N - 2sqrt(h^2+g^2/4) + 2h... compute directly
        c_exact = lam_exact * h_s / (g_N ** 2)
        # SW agreement: c_exact -> 1/4 as g_N -> 0, deviation O(g_N^2/h_s^2)
        dev = abs(c_exact - 0.25)
        bound = 0.5 * (g_N / h_s) ** 2
        require(dev < bound + 1e-9,
                "F2: exact vs SW agree to O(g^2/h^2): g=%.2f dev=%.2e bound=%.2e"
                % (g_N, dev, bound))
        print("F2 check g_N=%.2f: c_exact=%.6f (SW: 0.25, dev %.2e within "
              "O(g^2/h^2)=%.2e)" % (g_N, c_exact, dev, bound))
    print("F2 PASS: methods agree within declared accuracy; no scheme dependence")

    # ---- P4: scale relativity ------------------------------------------
    # lambda_c has dimensions of the model energy scale; only the ratio
    # lambda_c * h_s / g_N^2 is parameter-free. Verify scaling:
    _, a = sw_effective(2.0, 0.1, 0.0)
    _, b = sw_effective(4.0, 0.2, 0.0)
    la = connected_lambda(dc1_filter(a))
    lb = connected_lambda(dc1_filter(b))
    require(abs(la * 2.0 / 0.01 - 0.25) < 1e-12 and
            abs(lb * 4.0 / 0.04 - 0.25) < 1e-12,
            "P4: only the ratio is structural; absolute lambda_c scales")
    print("P4 PASS: lambda_c is scale-relative; the structural content is "
          "the pure number c = 1/4 and the P2 selection asymmetry")

    print("ALL CYCLE-3 PREDICTIONS CONFIRMED: lambda_c = (1/4) g_N^2/h_s; "
          "durable cross-talk sourced by phase-type coupling only; "
          "alpha_computed=false")


if __name__ == "__main__":
    main()
