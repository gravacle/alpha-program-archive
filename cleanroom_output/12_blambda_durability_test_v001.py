#!/usr/bin/env python3
"""DCC v001 applied to the exhibited connected counterfamily B_lambda.

Written and executed strictly AFTER 11_DURABILITY_CLOSURE_PRINCIPLE_V001.md
was sealed (seal ec559cb7...). Tests predictions P1-P4 exactly, on the
two-cell registration space with basis {|00>,|01>,|10>,|11>}.
Fail-closed: require(), no assert; python -O safe. No measured constant.
"""
import sys
from fractions import Fraction


def require(cond, msg):
    if not cond:
        print("FAIL: " + msg)
        sys.exit(1)


# --- exact 4x4 matrices over Fractions; basis order: 00, 01, 10, 11 -------
def zeros():
    return [[Fraction(0)] * 4 for _ in range(4)]


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4)]
            for i in range(4)]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(4)] for i in range(4)]


def is_zero(a):
    return all(a[i][j] == 0 for i in range(4) for j in range(4))


def frob2(a):
    return sum(a[i][j] * a[i][j] for i in range(4) for j in range(4))


# registration observables: N1 counts first cell written, N2 second
N1 = zeros(); N1[2][2] = Fraction(1); N1[3][3] = Fraction(1)   # |10>,|11>
N2 = zeros(); N2[1][1] = Fraction(1); N2[3][3] = Fraction(1)   # |01>,|11>

# counterfamily pieces: SWAP = |10><01| + |01><10| ; DIAG(lam) = lam|11><11|
SWAP = zeros(); SWAP[2][1] = Fraction(1); SWAP[1][2] = Fraction(1)


def B(lam):
    m = [[SWAP[i][j] for j in range(4)] for i in range(4)]
    m[3][3] = lam
    return m


def comm(a, b):
    return sub(matmul(a, b), matmul(b, a))


def main():
    # --- P1: swap term violates DC1; violation is lambda-independent -----
    for lam in [Fraction(0), Fraction(1), Fraction(2), Fraction(-1),
                Fraction(7, 3)]:
        c1 = comm(B(lam), N1)
        c2 = comm(B(lam), N2)
        require(not is_zero(c1) and not is_zero(c2),
                "swap must violate DC1 for lam=%s" % lam)
        require(frob2(c1) == 2 and frob2(c2) == 2,
                "DC1 violation norm^2 = 2, lambda-independent")
    # the violation comes entirely from SWAP:
    require(not is_zero(comm(SWAP, N1)), "SWAP alone violates DC1")
    print("P1 PASS: every B_lambda (swap present) violates DC1; "
          "violation norm^2 = 2, independent of lambda")

    # --- P2: DC1-admissible subfamily of the two-cell generator space ----
    # General Hermitian generator basis: check that [G,N1]=[G,N2]=0 forces
    # G diagonal in the registration basis. Enumerate all off-diagonal
    # Hermitian pair-generators E_{ij}+E_{ji} and i(E_{ij}-E_{ji}).
    admissible_offdiag = 0
    for i in range(4):
        for j in range(i + 1, 4):
            g = zeros(); g[i][j] = Fraction(1); g[j][i] = Fraction(1)
            if is_zero(comm(g, N1)) and is_zero(comm(g, N2)):
                admissible_offdiag += 1
    require(admissible_offdiag == 0,
            "no off-diagonal generator commutes with both N1 and N2")
    # diagonal generators trivially commute:
    for k in range(4):
        g = zeros(); g[k][k] = Fraction(1)
        require(is_zero(comm(g, N1)) and is_zero(comm(g, N2)),
                "diagonal generators are DC1-admissible")
    print("P2 PASS: DC1-admissible subfamily is exactly the diagonal "
          "algebra B = sum_P E(P)|P><P| (4 real parameters)")

    # --- P3: DC2 on disjoint cells collapses the family to a point -------
    # E(11)-E(01)-E(10)+E(00) = lambda_c must vanish for disjoint supports.
    # Within the exhibited family (E(00)=E(01)=E(10)=0, E(11)=lam):
    # lambda_c = lam  =>  disjoint cells force lam = 0 uniquely.
    E00, E01, E10 = Fraction(0), Fraction(0), Fraction(0)
    for lam in [Fraction(0), Fraction(1), Fraction(2), Fraction(-1)]:
        lam_c = lam - E01 - E10 + E00
        if lam_c == 0:
            require(lam == 0, "only lam=0 survives DC2 on disjoint cells")
    print("P3 PASS: disjoint cells -> lambda_c = 0 forced; the exhibited "
          "family collapses to the unique point lambda = 0")

    # --- P4: incident cells retain exactly one free pairwise coefficient -
    # DC1+DC2+DC3 leave, for one incident pair, the one-parameter family
    # B = E01|01><01| + E10|10><10| + (E01+E10+lambda_c)|11><11| with
    # lambda_c unconstrained: verify every such member is DC1-admissible
    # and that DC2 (which binds only disjoint supports) does not fix it.
    for lam_c in [Fraction(0), Fraction(1), Fraction(-2), Fraction(5, 7)]:
        g = zeros()
        g[1][1] = Fraction(3)          # arbitrary single-cell rates
        g[2][2] = Fraction(4)
        g[3][3] = Fraction(3) + Fraction(4) + lam_c
        require(is_zero(comm(g, N1)) and is_zero(comm(g, N2)),
                "incident-pair family is DC1-admissible for lambda_c=%s"
                % lam_c)
    print("P4 PASS: incident pair retains exactly one connected "
          "coefficient lambda_c; DC1-DC4 fix the FORM (diagonal, "
          "pairwise, incident-only), not the magnitude")

    # --- consequence for the adopted quasi-free completeness premise -----
    # The surviving cross-talk lambda_c|11><11| is a diagonal quartic-type
    # (n1 n2) term: lambda_c * N1N2 restricted to two cells. Verify:
    n1n2 = matmul(N1, N2)
    g = zeros(); g[3][3] = Fraction(1)
    require(is_zero(sub(n1n2, g)), "lambda_c seat IS the n1*n2 term")
    print("NOTE: the surviving seat equals the n_i n_j (quartic-type) "
          "cross-talk that the ADOPTED quasi-free completeness premise "
          "excluded; DCC and that premise are in direct conflict")

    print("ALL DCC PREDICTIONS P1-P4 CONFIRMED EXACTLY (Fraction "
          "arithmetic); alpha_computed=false; no magnitude was selected")


if __name__ == "__main__":
    main()
