#!/usr/bin/env python3
"""Fresh-context independent recomputation of the B_lambda restriction test.

Built from the DEFINITION B_lambda = |10><01| + |01><10| + lambda|11><11|
on ordered basis (|00>, |10>, |01>, |11>) -- outer products constructed
programmatically, exact integer/Fraction arithmetic throughout.
No construction-lane code reused.
"""
from fractions import Fraction


BASIS = ("|00>", "|10>", "|01>", "|11>")
IDX = {name: k for k, name in enumerate(BASIS)}


def outer(ket: str, bra: str):
    """|ket><bra| as a 4x4 integer matrix in the declared basis order."""
    m = [[0] * 4 for _ in range(4)]
    m[IDX[ket]][IDX[bra]] = 1
    return m


def madd(a, b):
    return [[a[i][j] + b[i][j] for j in range(4)] for i in range(4)]


def scale(c, a):
    return [[c * a[i][j] for j in range(4)] for i in range(4)]


def build_B(lam: int):
    return madd(madd(outer("|10>", "|01>"), outer("|01>", "|10>")),
                scale(lam, outer("|11>", "|11>")))


def restrict(m, indices):
    return tuple(tuple(m[i][j] for j in indices) for i in indices)


def charpoly_coeffs(A):
    """Coefficients of det(xI - A) = x^n + c1 x^{n-1} + ... + cn,
    via Faddeev-LeVerrier with exact Fractions."""
    n = len(A)
    Af = [[Fraction(A[i][j]) for j in range(n)] for i in range(n)]

    def matmul(X, Y):
        return [[sum(X[i][k] * Y[k][j] for k in range(n)) for j in range(n)]
                for i in range(n)]

    M = [[Fraction(0)] * n for _ in range(n)]
    coeffs = [Fraction(1)]
    c = Fraction(1)
    for k in range(1, n + 1):
        M = [[M[i][j] + (c if i == j else 0) for j in range(n)]
             for i in range(n)]
        M = matmul(Af, M)
        c = -Fraction(sum(M[i][i] for i in range(n)), k)
        coeffs.append(c)
    return coeffs  # [1, c1, c2, c3, c4]


def poly_from_roots_expand(root_multiplicities):
    """Expand prod (x - r)^m into coefficient list [1, c1, ..., cn]."""
    coeffs = [Fraction(1)]
    for r, mult in root_multiplicities:
        for _ in range(mult):
            new = [Fraction(0)] * (len(coeffs) + 1)
            for i, a in enumerate(coeffs):
                new[i] += a
                new[i + 1] -= a * r
            coeffs = new
    return coeffs


def fmt(m):
    return "\n".join("  " + " ".join(str(x) for x in row) for row in m)


B0 = build_B(0)
B1 = build_B(1)

print("B_lambda=0 in basis", BASIS)
print(fmt(B0))
print("B_lambda=1 in basis", BASIS)
print(fmt(B1))

# --- Restriction tests -------------------------------------------------
vac = restrict(B0, (0,)), restrict(B1, (0,))
one = restrict(B0, (1, 2)), restrict(B1, (1, 2))
vac_plus_one = restrict(B0, (0, 1, 2)), restrict(B1, (0, 1, 2))

vacuum_equal = vac[0] == vac[1]
one_record_equal = one[0] == one[1]
vac_one_block_equal = vac_plus_one[0] == vac_plus_one[1]
two_record_00 = B0[3][3]
two_record_11 = B1[3][3]
two_record_differ = two_record_00 != two_record_11

print("\nvacuum restriction equal:              ", vacuum_equal)
print("one-record restriction equal:          ", one_record_equal)
print("vacuum+one-record 3x3 block equal:     ", vac_one_block_equal)
print("two-record element lambda=0:           ", two_record_00)
print("two-record element lambda=1:           ", two_record_11)
print("two-record elements differ:            ", two_record_differ)

# Cross-coupling rows/cols between |11> and the rest must also agree for the
# restriction claim to be honest about the off-block entries:
off0 = [B0[3][j] for j in range(3)] + [B0[i][3] for i in range(3)]
off1 = [B1[3][j] for j in range(3)] + [B1[i][3] for i in range(3)]
print("off-block |11> couplings lambda=0:     ", off0)
print("off-block |11> couplings lambda=1:     ", off1)
print("only diagonal |11><11| entry differs:  ", off0 == off1)

# --- Characteristic polynomials ---------------------------------------
cp0 = charpoly_coeffs(B0)
cp1 = charpoly_coeffs(B1)
claim0 = poly_from_roots_expand([(Fraction(0), 2), (Fraction(1), 1),
                                 (Fraction(-1), 1)])   # x^2 (x-1)(x+1)
claim1 = poly_from_roots_expand([(Fraction(0), 1), (Fraction(1), 2),
                                 (Fraction(-1), 1)])   # x (x-1)^2 (x+1)

print("\ncharpoly lambda=0 coeffs (det(xI-B)):  ", cp0)
print("claimed  x^2*(x-1)*(x+1) coeffs:       ", claim0)
print("charpoly lambda=0 matches claim:       ", cp0 == claim0)
print("charpoly lambda=1 coeffs (det(xI-B)):  ", cp1)
print("claimed  x*(x-1)^2*(x+1) coeffs:       ", claim1)
print("charpoly lambda=1 matches claim:       ", cp1 == claim1)

# --- Optional sympy cross-check ---------------------------------------
try:
    import sympy as sp
    x = sp.symbols("x")
    s0 = sp.Matrix(B0).charpoly(x).as_expr()
    s1 = sp.Matrix(B1).charpoly(x).as_expr()
    e0 = sp.expand(x**2 * (x - 1) * (x + 1))
    e1 = sp.expand(x * (x - 1) ** 2 * (x + 1))
    print("\nsympy charpoly lambda=0:", s0, "== x^2(x-1)(x+1):",
          sp.simplify(s0 - e0) == 0)
    print("sympy charpoly lambda=1:", s1, "== x(x-1)^2(x+1):",
          sp.simplify(s1 - e1) == 0)
except ImportError:
    print("\n(sympy not available; Faddeev-LeVerrier exact result stands)")

ok = all([vacuum_equal, one_record_equal, vac_one_block_equal,
          two_record_differ, off0 == off1, cp0 == claim0, cp1 == claim1])
print("\nINDEPENDENT_B_LAMBDA_RECOMPUTATION_PASS =", ok)
