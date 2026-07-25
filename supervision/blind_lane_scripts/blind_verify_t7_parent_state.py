#!/usr/bin/env python3
"""Blind independent verification of STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION claims.

Built from scratch. numpy only (eigendecomposition via numpy.linalg).
No measured constants used anywhere.
"""
import numpy as np

np.set_printoptions(precision=3, suppress=False)

# ---------------------------------------------------------------- Dirac setup
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)
SIG = [s1, s2, s3]
I4 = np.eye(4, dtype=complex)

def alpha_mat(i):
    # standard Dirac basis: alpha_i = [[0, sigma_i], [sigma_i, 0]]
    return np.block([[Z2, SIG[i]], [SIG[i], Z2]])

ALPHA = [alpha_mat(i) for i in range(3)]

def h0(p):
    return p[0] * ALPHA[0] + p[1] * ALPHA[1] + p[2] * ALPHA[2]

def C_formula(p):
    return (I4 - h0(p) / np.linalg.norm(p)) / 2.0

def spectral_neg_projector(H):
    """Projector onto strictly negative spectrum via eigendecomposition."""
    w, V = np.linalg.eigh(H)
    P = np.zeros_like(H)
    for k in range(len(w)):
        if w[k] < 0:
            v = V[:, k:k+1]
            P += v @ v.conj().T
    return P, w

# ------------------------------------------------------- Claim 1: fiber checks
print("=" * 72)
print("CLAIM 1: C(p) = (I - h0(p)/|p|)/2 is the negative spectral projector")
print("=" * 72)
test_ps = [
    np.array([1.0, 2.0, -2.0]),          # |p| = 3 (nice norm)
    np.array([0.3, -1.2, 0.7]),          # generic
    np.array([0.0, 0.0, 1.0]),           # axis-aligned
    np.array([1e-8, -2e-8, 1.5e-8]),     # tiny nonzero
    np.array([3e7, -1e8, 7e7]),          # huge
    np.array([-0.577, 0.577, 0.577]),    # near-diagonal direction
]
for p in test_ps:
    pn = np.linalg.norm(p)
    H = h0(p)
    C = C_formula(p)
    Pneg, w = spectral_neg_projector(H)
    e_sq = np.linalg.norm(H @ H - pn**2 * I4)              # h0^2 = |p|^2 I
    e_herm = np.linalg.norm(C - C.conj().T)
    e_idem = np.linalg.norm(C @ C - C)
    e_comm = np.linalg.norm(C @ H - H @ C)
    e_proj = np.linalg.norm(C - Pneg)
    rank = int(round(np.real(np.trace(C))))
    # spectrum on range of C: H C = -|p| C must hold (flat band -|p|)
    e_negrange = np.linalg.norm(H @ C + pn * C)
    evC = np.sort(np.linalg.eigvalsh(C))
    print(f"p={np.array2string(p, precision=2)} |p|={pn:.3e}")
    print(f"  h0^2-|p|^2I: {e_sq:.2e}  herm: {e_herm:.2e}  idem: {e_idem:.2e}"
          f"  [C,h0]: {e_comm:.2e}")
    print(f"  ||C - P_neg(eig)||: {e_proj:.2e}  trace(C)={np.real(np.trace(C)):.16f}"
          f" (rank {rank})")
    print(f"  ||h0 C + |p| C|| (neg flat band): {e_negrange:.2e}")
    print(f"  eig(C): {np.array2string(evC, precision=17)}")
    print(f"  eig(h0)/|p|: {np.array2string(np.sort(w)/pn, precision=17)}")

# --------------------------------------------- Claim 2: nested finite cohorts
print()
print("=" * 72)
print("CLAIM 2: nested inversion-symmetric cohorts, C_n = Q_n C Q_n")
print("=" * 72)
# My own cohort choices (discretionary): three momentum pairs, none zero,
# none parallel, irrational norms.
p1 = np.array([0.3, -1.2, 0.7])
p2 = np.array([2.0, 0.1, -0.5])
p3 = np.array([-0.8, 0.4, 1.9])
pair = lambda p: [p, -p]
cohortA = pair(p1)                       # dim 8
cohortB = pair(p1) + pair(p2)            # dim 16, contains A
cohortC = pair(p1) + pair(p2) + pair(p3) # dim 24, contains B

def build_C_and_H(cohort):
    d = 4 * len(cohort)
    Cn = np.zeros((d, d), dtype=complex)
    Hn = np.zeros((d, d), dtype=complex)
    for k, p in enumerate(cohort):
        Cn[4*k:4*k+4, 4*k:4*k+4] = C_formula(p)
        Hn[4*k:4*k+4, 4*k:4*k+4] = h0(p)
    return Cn, Hn

CA, HA = build_C_and_H(cohortA)
CB, HB = build_C_and_H(cohortB)
CC, HC = build_C_and_H(cohortC)

for name, Cn, Hn, cohort in [("A(dim8)", CA, HA, cohortA),
                             ("B(dim16)", CB, HB, cohortB),
                             ("C(dim24)", CC, HC, cohortC)]:
    d = Cn.shape[0]
    ev = np.sort(np.linalg.eigvalsh(Cn))
    e_herm = np.abs(Cn - Cn.conj().T).max()
    e_idem = np.abs(Cn @ Cn - Cn).max()
    n0 = int(np.sum(ev < 0.5))
    n1 = int(np.sum(ev >= 0.5))
    dev01 = np.abs(ev - np.round(ev)).max()   # deviation from exact {0,1}
    tr = np.real(np.trace(Cn))
    evH = np.linalg.eigvalsh(Hn)
    min_absH = np.abs(evH).min()
    print(f"cohort {name}: herm_err(max)={e_herm:.2e}  idem_err(max)={e_idem:.2e}")
    print(f"  eig(C_n) counts: {n0} near 0, {n1} near 1 (dim/2 = {d//2});"
          f" max|ev - round(ev)| = {dev01:.2e}; trace = {tr:.16f}")
    print(f"  min |eig(h0_n)| = {min_absH:.6f}  (no zero mode iff > 0)")

# cofinality: Q_n C_m Q_n = C_n EXACTLY (block slice = compression since
# Q_n is coordinate projection onto the sub-cohort's fibers)
def compress(Cbig, big, small):
    idx = []
    for p in small:
        for k, q in enumerate(big):
            if np.array_equal(p, q):
                idx.extend(range(4*k, 4*k+4))
                break
    idx = np.array(idx)
    return Cbig[np.ix_(idx, idx)]

pairs = [("Q_A C_B Q_A vs C_A", compress(CB, cohortB, cohortA), CA),
         ("Q_A C_C Q_A vs C_A", compress(CC, cohortC, cohortA), CA),
         ("Q_B C_C Q_B vs C_B", compress(CC, cohortC, cohortB), CB)]
for label, comp, ref in pairs:
    diff = np.abs(comp - ref).max()
    print(f"  cofinality {label}: max|diff| = {diff:.1e}"
          f"  exact_bitwise = {np.array_equal(comp, ref)}")

# also check: does the identity require inversion symmetry? test asymmetric cohort
asym = [p1, p2]  # NOT closed under p -> -p
Casym, Hasym = build_C_and_H(asym)
Casym_from_C = compress(CC, cohortC, asym)
print(f"  control (asymmetric cohort {{p1,p2}}): Q C_C Q = C_asym exact:"
      f" {np.array_equal(Casym_from_C, Casym)};"
      f" eig dev from 0/1: {np.abs(np.sort(np.linalg.eigvalsh(Casym)) - np.round(np.sort(np.linalg.eigvalsh(Casym)))).max():.1e}")

# --------------------------------- Claim 3: finite-Fock Slater cross-check
print()
print("=" * 72)
print("CLAIM 3: Slater-determinant Fock construction reproduces C_A")
print("=" * 72)
d = 8               # modes in cohort A
D = 2 ** d          # Fock dim 256
# Jordan-Wigner fermion operators
sp_ann = np.array([[0, 1], [0, 0]], dtype=complex)  # annihilate |1> -> |0>
sz = np.array([[1, 0], [0, -1]], dtype=complex)
I2f = np.eye(2, dtype=complex)

def jw_annihilator(j, d):
    ops = [sz] * j + [sp_ann] + [I2f] * (d - j - 1)
    M = ops[0]
    for o in ops[1:]:
        M = np.kron(M, o)
    return M

a_ops = [jw_annihilator(j, d) for j in range(d)]
# CAR sanity
car_err = 0.0
for i in range(d):
    for j in range(d):
        anti = a_ops[i] @ a_ops[j].conj().T + a_ops[j].conj().T @ a_ops[i]
        car_err = max(car_err, np.abs(anti - (1.0 if i == j else 0.0) * np.eye(D)).max())
        anti2 = a_ops[i] @ a_ops[j] + a_ops[j] @ a_ops[i]
        car_err = max(car_err, np.abs(anti2).max())
print(f"CAR algebra max error: {car_err:.2e}")

# negative-energy modes of h0 on cohort A
wA, VA = np.linalg.eigh(HA)
neg_idx = np.where(wA < 0)[0]
print(f"h0_A eigenvalues: {np.array2string(np.sort(wA), precision=6)}")
print(f"number of negative modes filled: {len(neg_idx)} (expect {d//2})")

# vacuum = all-unoccupied basis state = index 0 in JW ordering
vac = np.zeros(D, dtype=complex)
vac[0] = 1.0
psi = vac
for k in neg_idx:
    v = VA[:, k]
    b_dag = sum(v[i] * a_ops[i].conj().T for i in range(d))
    psi = b_dag @ psi
norm = np.linalg.norm(psi)
print(f"Slater state norm: {norm:.16f}")
psi = psi / norm

# one-particle covariance from the Fock state: M[i,j] = <psi| a_j^dag a_i |psi>
M = np.zeros((d, d), dtype=complex)
for i in range(d):
    for j in range(d):
        M[i, j] = psi.conj() @ (a_ops[j].conj().T @ (a_ops[i] @ psi))
e_slater = np.abs(M - CA).max()
print(f"max |<a_j^dag a_i>_Slater - (C_A)_ij| = {e_slater:.2e}")

# density matrix checks: unit trace, purity (pure state)
rho = np.outer(psi, psi.conj())
print(f"trace(rho) = {np.real(np.trace(rho)):.16f}; purity tr(rho^2) = "
      f"{np.real(np.trace(rho @ rho)):.16f}")
# pairing anomaly check: <a_i a_j> must vanish for a number-conserving Slater state
pair_err = 0.0
for i in range(d):
    for j in range(d):
        pair_err = max(pair_err, abs(psi.conj() @ (a_ops[i] @ (a_ops[j] @ psi))))
print(f"max |<a_i a_j>| (pairing must vanish): {pair_err:.2e}")

# entropy of C_A eigenvalues -> 0 means no thermal weight
evA = np.linalg.eigvalsh(CA)
ent = 0.0
for lam in evA:
    for x in (lam, 1 - lam):
        if 1e-14 < x < 1 - 1e-14:
            ent += -x * np.log(x)
print(f"quasifree entropy S(C_A) = {ent:.3e} (0 => pure, no thermal parameter)")

# ------------------- Claim 5 numeric leg: restriction blocks == disclosed P_-
print()
print("=" * 72)
print("CLAIM 5 (numeric leg): C_n blocks equal fiberwise 1_(-inf,0)(h_0)")
print("=" * 72)
worst = 0.0
for p in cohortC:
    Pneg, _ = spectral_neg_projector(h0(p))
    worst = max(worst, np.abs(C_formula(p) - Pneg).max())
print(f"max over all 6 cohort momenta of |C(p) - P_neg(p)|: {worst:.2e}")
print("=> restricted state is the disclosed negative-energy quasifree state,")
print("   evaluated fiberwise; nothing else enters the state definition.")
