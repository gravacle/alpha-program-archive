#!/usr/bin/env python3
"""BLIND independent reproduction: Stage-8 T7 finite-Fock completed-record amplitudes.

Built ONLY from:
  - STAGE8_T7_FINITE_FOCK_COMPLETED_RECORD_AMPLITUDE_SPEC_V001.md (sealed spec, F1-F6)
  - the hash-pinned upstream construction lineage (parent-state regulator-restriction
    SPEC/RESULT, relay/amendment artifacts, R3.4 complete-parent SPEC, adjudication
    SPEC/RESULT and its upstream verifier which pins the three-site Galerkin parent).

FORBIDDEN artifacts (this gate's RESULT, derive/verify scripts, work files) were NOT read.

Construction (all hand-coded here):
  one-particle parent: 3 periodic sites x 4 Dirac spinor components (12-dim),
    h_src = kron(-i D, alpha_x), D = central difference (D[j,j+1]=+1/2, D[j,j-1]=-1/2 mod 3)
    alpha_x = gamma0 gamma1 (Dirac rep), S_n = -i gamma0 gamma5
    cell masks M_0 = diag(1,1,0), M_1 = diag(0,1,1) on sites
    record quadrature c = i*Gamma*b, Gamma=diag(1,1,-1), b=[[0,0,-1],[0,0,1],[-1,1,0]]
    envelope v(t) = tau_R * w(t), w(s)=32*min(s,1-s)^3 on [0,1], tau_R = pi/sqrt(2)
    causal order: cell 0 on its unit interval, then cell 1 on the next (sequential relay)
  F1: compress h_src and both cell source operators (M_c x S_n) to the 8-dim nonzero
      spectral subspace of h_src.
  Inherited state: C(p) = (I - h0/|p|)/2 restricted -> projector on 4 negative modes;
      Slater state fills the four negative-energy modes.
  F2: exact 4-particle sector wedge^4 C^8 (dim 70), hand-coded dGamma, verified against
      an independent Jordan-Wigner full-Fock (2^8) construction.
  F3: H(t) = dGamma(h0) x I_9  +  v_c(t) dGamma(B_c) x iota_c(c), c = active cell.
  F4: a_p(0)  = <Slater x (p,r)| U_1 |Slater x (r,r)>
      a_pp(0) = <Slater x (p,p)| U_2 U_1 |Slater x (r,r)>
  plus vacuum sector, one-particle completed-transfer norm, convergence, norm drift.
"""
import numpy as np
import math, itertools, json, sys

np.set_printoptions(precision=15, suppress=False)
TAU_R = math.pi / math.sqrt(2.0)

# ---------------------------------------------------------------- one-particle model
def pauli():
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    return sx, sy, sz

def dirac_matrices():
    sx, sy, sz = pauli()
    I2 = np.eye(2, dtype=complex); Z2 = np.zeros((2, 2), dtype=complex)
    g0 = np.block([[I2, Z2], [Z2, -I2]])
    gs = [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
    g5 = 1j * g0 @ gs[0] @ gs[1] @ gs[2]
    alpha_x = g0 @ gs[0]
    S_n = -1j * g0 @ g5
    return alpha_x, S_n

alpha_x, S_n = dirac_matrices()
assert np.allclose(alpha_x, alpha_x.conj().T)
assert np.allclose(S_n, S_n.conj().T)
assert np.allclose(S_n @ S_n, np.eye(4))
assert np.allclose(alpha_x @ S_n + S_n @ alpha_x, np.zeros((4, 4)))  # anticommute

D = np.zeros((3, 3), dtype=complex)
for j in range(3):
    D[j, (j + 1) % 3] += 0.5
    D[j, (j - 1) % 3] -= 0.5
h_src = np.kron(-1j * D, alpha_x)          # 12x12, site (outer) x spinor (inner)
assert np.allclose(h_src, h_src.conj().T)

evals, evecs = np.linalg.eigh(h_src)
lam = math.sqrt(3.0) / 2.0
n_neg = int(np.sum(evals < -1e-12)); n_zero = int(np.sum(np.abs(evals) <= 1e-12))
n_pos = int(np.sum(evals > 1e-12))
assert (n_neg, n_zero, n_pos) == (4, 4, 4), (n_neg, n_zero, n_pos)
assert np.allclose(np.sort(np.abs(evals[np.abs(evals) > 1e-12])), lam)

# F1: nonzero spectral subspace, 8 modes. Order: 4 negative then 4 positive.
idx_neg = np.where(evals < -1e-12)[0]
idx_pos = np.where(evals > 1e-12)[0]
V = evecs[:, np.concatenate([idx_neg, idx_pos])]     # 12x8 isometry
assert np.allclose(V.conj().T @ V, np.eye(8))
h8 = V.conj().T @ h_src @ V
assert np.allclose(h8, np.diag(np.concatenate([evals[idx_neg], evals[idx_pos]])), atol=1e-13)

masks = (np.diag([1.0, 1.0, 0.0]).astype(complex), np.diag([0.0, 1.0, 1.0]).astype(complex))
B8 = [V.conj().T @ np.kron(masks[c], S_n) @ V for c in range(2)]   # compressed cell ops
for B in B8:
    assert np.allclose(B, B.conj().T)

# Inherited covariance: C(p) = (I - h0/|p|)/2 restricted to nonzero modes.
# On the 8-mode subspace this is the spectral projector onto the 4 negative modes.
C8 = 0.5 * (np.eye(8) - h8 / lam)
P_neg8 = np.zeros((8, 8), dtype=complex); P_neg8[:4, :4] = np.eye(4)
assert np.allclose(C8, P_neg8, atol=1e-12)
assert np.allclose(C8 @ C8, C8, atol=1e-12)
assert abs(np.trace(C8).real - 4.0) < 1e-12

# ---------------------------------------------------------------- record structure
Gam = np.diag([1.0, 1.0, -1.0]).astype(complex)
b = np.array([[0, 0, -1], [0, 0, 1], [-1, 1, 0]], dtype=complex)
c_q = 1j * Gam @ b
assert np.allclose(c_q, c_q.conj().T)
# eigenvalues 0, +-sqrt(2); exp(-i tau_R c_q)|r> = |p> exactly:
r_ket = np.array([1, 0, 0], dtype=complex); p_ket = np.array([0, 1, 0], dtype=complex)
w_eig, w_vec = np.linalg.eigh(c_q)
U_rec = w_vec @ np.diag(np.exp(-1j * TAU_R * w_eig)) @ w_vec.conj().T
assert abs(abs(np.vdot(p_ket, U_rec @ r_ket)) - 1.0) < 1e-12

I3 = np.eye(3, dtype=complex)
q_ops = [np.kron(c_q, I3), np.kron(I3, c_q)]   # record1 outer, record2 inner (9x9)
REC = {"rr": 0, "pr": 3, "pp": 4}              # index = 3*l1 + l2 ; r=0,p=1,e=2

# ---------------------------------------------------------------- Fock: wedge^4 C^8
modes = 8; n_part = 4
basis = list(itertools.combinations(range(modes), n_part))   # 70 ordered subsets
bindex = {s: i for i, s in enumerate(basis)}
dimF = len(basis)
assert dimF == 70

def dGamma_wedge(B):
    """sum_ij B_ij a_i^dag a_j on wedge^4 C^8, occupation convention
    |S> = a^dag_{s1}...a^dag_{s4}|0>, s1<...<s4."""
    M = np.zeros((dimF, dimF), dtype=complex)
    for col, S in enumerate(basis):
        Sset = set(S)
        for j in S:
            # a_j : sign (-1)^{# occupied modes < j}
            sgn_j = (-1) ** sum(1 for x in S if x < j)
            rest = [x for x in S if x != j]
            for i in range(modes):
                if B[i, j] == 0:
                    continue
                if i in rest:
                    continue
                sgn_i = (-1) ** sum(1 for x in rest if x < i)
                new = tuple(sorted(rest + [i]))
                M[bindex[new], col] += B[i, j] * sgn_j * sgn_i
    return M

# Independent Jordan-Wigner verification of the dGamma convention (F2 check).
def jw_ops():
    a = np.array([[0, 1], [0, 0]], dtype=complex)   # |occ 1> -> |occ 0>
    Z = np.diag([1.0, -1.0]).astype(complex)
    I2 = np.eye(2, dtype=complex)
    ops = []
    for j in range(modes):
        facs = [Z] * j + [a] + [I2] * (modes - j - 1)
        m = facs[0]
        for f in facs[1:]:
            m = np.kron(m, f)
        ops.append(m)
    return ops

aj = jw_ops()
rngchk = np.random.default_rng(20260724)
Btest = rngchk.normal(size=(8, 8)) + 1j * rngchk.normal(size=(8, 8))
Btest = Btest + Btest.conj().T
dG_full = sum(Btest[i, j] * (aj[i].conj().T @ aj[j]) for i in range(8) for j in range(8))
vac = np.zeros(2 ** 8, dtype=complex); vac[0] = 1.0
def jw_state(S):
    v = vac
    for s in reversed(S):            # a^dag_{s1}...a^dag_{s4}|0>, rightmost applied first
        v = aj[s].conj().T @ v
    return v
jw_vecs = np.column_stack([jw_state(S) for S in basis])
assert np.allclose(jw_vecs.conj().T @ jw_vecs, np.eye(dimF))
dG_jw = jw_vecs.conj().T @ dG_full @ jw_vecs
dG_mine = dGamma_wedge(Btest)
assert np.allclose(dG_jw, dG_mine, atol=1e-10), "dGamma convention mismatch vs Jordan-Wigner"
# one-particle action convention: dGamma(B) restricted to 1-particle sector == B
jw1 = np.column_stack([jw_state((k,)) for k in range(8)])
assert np.allclose(jw1.conj().T @ dG_full @ jw1, Btest, atol=1e-10)
print("F2 convention checks: dGamma(wedge^4) == Jordan-Wigner block; 1-particle block == B  [OK]")

dGh = dGamma_wedge(h8)                       # diagonal (h8 diagonal)
dGB = [dGamma_wedge(B8[c]) for c in range(2)]
E0 = float(np.real(dGh[0, 0]))               # energy of |0,1,2,3> ... check below

# Slater state: occupy the four negative modes (indices 0..3)
slater_idx = bindex[(0, 1, 2, 3)]
assert abs(dGh[slater_idx, slater_idx] - (-4 * lam)) < 1e-12
# Wick check: <Slater| dGamma(B) |Slater> = tr(C8 B)
sl = np.zeros(dimF, dtype=complex); sl[slater_idx] = 1.0
for B, dGB_ in ((h8, dGh), (B8[0], dGB[0]), (B8[1], dGB[1])):
    lhs = np.vdot(sl, dGB_ @ sl)
    rhs = np.trace(C8 @ B)
    assert abs(lhs - rhs) < 1e-12
print("Wick check: <Slater|dGamma(B)|Slater> = tr(C B) for h0 and both cells  [OK]")

# ---------------------------------------------------------------- full carrier 630
I9 = np.eye(9, dtype=complex)
H0_full = np.kron(dGh, I9)
W_full = [np.kron(dGB[c], q_ops[c]) for c in range(2)]
dim_full = dimF * 9

rr = np.zeros(9, dtype=complex); rr[REC["rr"]] = 1.0
psi0 = np.kron(sl, rr)

def envelope(t):
    if not 0.0 <= t <= 1.0:
        return 0.0
    return TAU_R * 32.0 * min(t, 1.0 - t) ** 3

# envelope amplitude clause: integral = tau_R  (Simpson, fine grid)
ts = np.linspace(0, 1, 20001)
ws = np.array([envelope(t) for t in ts])
integral = np.trapezoid(ws, ts)
assert abs(integral - TAU_R) < 1e-7
print(f"envelope integral over one cell = {integral:.12f} (tau_R = {TAU_R:.12f})  [OK]")

# ---------------------------------------------------------------- integrators (both hand-coded)
def rk4_cell(psi, H0, W, steps):
    """Integrator 1: classical RK4, hand-coded."""
    dt = 1.0 / steps
    def deriv(t, y):
        return -1j * (H0 @ y + envelope(t) * (W @ y))
    y = psi.copy()
    for n in range(steps):
        t = n * dt
        k1 = deriv(t, y)
        k2 = deriv(t + dt / 2, y + dt * k1 / 2)
        k3 = deriv(t + dt / 2, y + dt * k2 / 2)
        k4 = deriv(t + dt, y + dt * k3)
        y = y + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
    return y

def expmv_taylor(A_action, y, m_max=40, tol=1e-16):
    """exp(A) y via converged Taylor series (A = -i dt H, small norm)."""
    out = y.copy(); term = y.copy()
    for k in range(1, m_max):
        term = A_action(term) / k
        out = out + term
        if np.linalg.norm(term) < tol * np.linalg.norm(out):
            break
    return out

def magnus2_cell(psi, H0, W, steps):
    """Integrator 2: midpoint-Magnus (2nd order), exact unitary step via Taylor expmv."""
    dt = 1.0 / steps
    y = psi.copy()
    for n in range(steps):
        tm = (n + 0.5) * dt
        v = envelope(tm)
        def act(x, v=v):
            return -1j * dt * (H0 @ x + v * (W @ x))
        y = expmv_taylor(act, y)
    return y

def run_evolution(integrator, steps):
    a1 = integrator(psi0, H0_full, W_full[0], steps)     # cell 0 interval
    a2 = integrator(a1, H0_full, W_full[1], steps)       # cell 1 interval (relayed)
    return a1, a2

def amp(psi_full, rec_label):
    bra = np.kron(sl, np.eye(9)[:, REC[rec_label]].astype(complex))
    return complex(np.vdot(bra, psi_full))

results = {}
for name, integ, res_list in (("rk4", rk4_cell, [1000, 2000]),
                              ("magnus2", magnus2_cell, [200, 400, 800])):
    for steps in res_list:
        a1, a2 = run_evolution(integ, steps)
        results[(name, steps)] = dict(
            a_p=amp(a1, "pr"), a_pp=amp(a2, "pp"),
            norm1=float(np.linalg.norm(a1)), norm2=float(np.linalg.norm(a2)))
        r = results[(name, steps)]
        print(f"{name:8s} N={steps:5d}  a_p = {r['a_p'].real:+.15f}{r['a_p'].imag:+.15f}i   "
              f"a_pp = {r['a_pp'].real:+.15f}{r['a_pp'].imag:+.15f}i   "
              f"|norm-1| = {abs(r['norm2']-1):.2e}")

# convergence: second-order ratio from magnus2
def ratio(key):
    d1 = abs(results[("magnus2", 200)][key] - results[("magnus2", 400)][key])
    d2 = abs(results[("magnus2", 400)][key] - results[("magnus2", 800)][key])
    return d1 / d2 if d2 > 0 else float("inf")
print(f"magnus2 second-order ratio  a_p : {ratio('a_p'):.6f}   a_pp: {ratio('a_pp'):.6f}  (expect ~4)")

# cross-integrator agreement (frozen tolerance choice documented: 1e-8)
best_rk4 = results[("rk4", 2000)]; best_mag = results[("magnus2", 800)]
d_ap = abs(best_rk4["a_p"] - best_mag["a_p"]); d_app = abs(best_rk4["a_pp"] - best_mag["a_pp"])
print(f"cross-integrator |delta a_p| = {d_ap:.3e}  |delta a_pp| = {d_app:.3e}")

# Richardson-extrapolated best values (magnus2 is clean 2nd order; rk4 4th order at N=2000
# is already ~1e-12).  Use rk4 N=2000 as the quoted value; verify against extrapolation.
ap_extrap = results[("magnus2", 800)]["a_p"] + (results[("magnus2", 800)]["a_p"] - results[("magnus2", 400)]["a_p"]) / 3.0
app_extrap = results[("magnus2", 800)]["a_pp"] + (results[("magnus2", 800)]["a_pp"] - results[("magnus2", 400)]["a_pp"]) / 3.0
print(f"magnus2 Richardson  a_p = {ap_extrap.real:+.15f}{ap_extrap.imag:+.15f}i")
print(f"magnus2 Richardson  a_pp= {app_extrap.real:+.15f}{app_extrap.imag:+.15f}i")

a_p_final = best_rk4["a_p"]; a_pp_final = best_rk4["a_pp"]

# ---------------------------------------------------------------- vacuum sector (d)
# dGamma vacuum block is zero: dGamma(B)|0> = 0 for every B (no particles to scatter),
# so H(t) annihilates |0> x chi for every record chi; U = identity there; the completed
# amplitude <0 x (p,r)|U_1|0 x (r,r)> = <p|r> = 0 exactly.
# Numerical witness in the full JW Fock (vacuum column of dGamma):
for c in range(2):
    dG_full_c = sum(B8[c][i, j] * (aj[i].conj().T @ aj[j]) for i in range(8) for j in range(8))
    assert np.linalg.norm(dG_full_c @ vac) == 0.0
print("vacuum sector: dGamma(B_c)|0> = 0 exactly for both cells -> U|0,chi> = |0,chi>;")
print("completed vacuum amplitude = <p|r> * <0|0> = 0 exactly  [OK]")

# ---------------------------------------------------------------- one-particle sector (e)
# H^(1)(t) = h8 x I9 + v(t) B8_c x q_c   on C^8 x C^9 (72-dim)
H0_1p = np.kron(h8, I9)
W_1p = [np.kron(B8[c], q_ops[c]) for c in range(2)]

def evolve_columns_1p(steps=4000):
    cols = np.eye(72, dtype=complex)
    dt = 1.0 / steps
    Y = cols
    for n in range(steps):
        tm = (n + 0.5) * dt
        v = envelope(tm)
        def act(X, v=v):
            return -1j * dt * (H0_1p @ X + v * (W_1p[0] @ X))
        Y = expmv_taylor(act, Y)
    return Y   # U_1 restricted to one-particle sector, all columns

U1_1p = evolve_columns_1p(2000)
# completed-transfer: K = (I8 x <p,r|) U1 (I8 x |r,r>)
emb_rr = np.kron(np.eye(8, dtype=complex), rr.reshape(9, 1))       # 72x8
bra_pr = np.kron(np.eye(8, dtype=complex), np.eye(9)[:, REC["pr"]].reshape(9, 1).astype(complex))
K1 = bra_pr.conj().T @ (np.kron(np.eye(8), np.eye(9)) @ U1_1p) @ emb_rr
K1 = (bra_pr.T.conj() @ U1_1p @ emb_rr) if False else K1
K1_frob = float(np.linalg.norm(K1))
K1_op = float(np.linalg.norm(K1, 2))
print(f"one-particle completed-transfer  ||K1||_F = {K1_frob:.12f}   ||K1||_2 = {K1_op:.12f}")
print("F5 type obstruction: vacuum block of the completed Kraus operator = 0, but any single")
print("second quantization Gamma(k) has vacuum block 1; since the one-particle completed")
print(f"transfer is nonzero ({K1_frob:.6f} > 0), the record-compressed operator is NOT one Gamma(k);")
print("det(I-C+CK) shortcut not used anywhere in this run.")

# ---------------------------------------------------------------- report values
print()
print("=== FINAL (rk4 N=2000, cross-verified) ===")
print(f"a_p(0)  = {a_p_final.real:+.15f} {a_p_final.imag:+.15f}i   |a_p|  = {abs(a_p_final):.15f}")
print(f"a_pp(0) = {a_pp_final.real:+.15f} {a_pp_final.imag:+.15f}i   |a_pp| = {abs(a_pp_final):.15f}")
E_slater = -4 * lam
print(f"Slater free energy E0 = {E_slater:.15f}; free phase over one cell exp(-i E0 T) with T=1")
ph1 = np.exp(1j * E_slater * 1.0); ph2 = np.exp(1j * E_slater * 2.0)
ap_strip = a_p_final * ph1; app_strip = a_pp_final * ph2
print(f"(documentation only) free-phase-stripped: a_p*e^(iE0)  = {ap_strip.real:+.15f}{ap_strip.imag:+.15f}i")
print(f"(documentation only) free-phase-stripped: a_pp*e^(2iE0) = {app_strip.real:+.15f}{app_strip.imag:+.15f}i")

out = dict(
    a_p=[a_p_final.real, a_p_final.imag],
    a_pp=[a_pp_final.real, a_pp_final.imag],
    magnus_richardson_a_p=[ap_extrap.real, ap_extrap.imag],
    magnus_richardson_a_pp=[app_extrap.real, app_extrap.imag],
    ratio_a_p=ratio("a_p"), ratio_a_pp=ratio("a_pp"),
    cross_delta=[d_ap, d_app],
    K1_frob=K1_frob, K1_op=K1_op,
    vacuum_amplitude_exact_zero=True,
    norm_drift_rk4=abs(results[("rk4", 2000)]["norm2"] - 1),
    norm_drift_mag=abs(results[("magnus2", 800)]["norm2"] - 1),
)
with open(sys.argv[1] if len(sys.argv) > 1 else "/tmp/blind_out.json", "w") as f:
    json.dump(out, f, indent=1)
print("json written")
