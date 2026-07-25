"""Blind rebuild of the R3.4 causal shared-source Moller/durability regulator.

Construction (documented choices):
  Source space: C^3, vertex basis e0,e1,e2 of a 3-vertex path.
  Rays: d0 = e1-e0, d1 = e2-e1.  Projectors P_j = |d_j><d_j|/2.
  H_S = dd* READ AS the vertex-space operator sum_j |d_j><d_j|
        = path graph Laplacian [[1,-1,0],[-1,2,-1],[0,-1,1]]  (eigs 0,1,3).
        (dd* literally on the edge space would be 2x2 and could not enter
         H_S tensor I_R alongside the 3x3 P_j; the vertex-space reading is
         the only one consistent with the stated parent Hamiltonian.)
  Record factors: R_0, R_1 = C^3 each, basis order (r, p, e).
  c_partial = [[0,0,-i],[0,0,+i],[+i,-i,0]]  (Hermitian, eigs +sqrt2,-sqrt2,0).
  B_j = P_j tensor c_partial,j  -- SPIN FACTOR gamma^5 DROPPED (27-dim total
        space C3 x C3 x C3).  Justification: the durability gate's regulator
        section names only source projectors, source Laplacian and c_partial;
        the outgoing-state spec v002 proves the completed action is the same
        for both chiral eigenvalues and identity on spin.  With one shared
        spin carrier in a chiral eigenstate the 54-dim model factorizes into
        c -> +c or c -> -c in BOTH cells simultaneously; both signs are run.
  H(t) = H_S tensor I9 + v0(t) B0 + v1(t) B1,
  v_j(t) = tau_R * w(t-j), w(s)=32(1/2-|s-1/2|)^3 on [0,1], tau_R=pi/sqrt2.
  Cell 0 active on [0,1], cell 1 on [1,2]; free H_S evolution afterwards.
"""
import numpy as np, json, sys

I3 = np.eye(3, dtype=complex)
I9 = np.eye(9, dtype=complex)
e0, e1v, e2v = np.eye(3, dtype=complex)
d0 = e1v - e0
d1 = e2v - e1v
P0 = np.outer(d0, d0.conj()) / 2.0
P1 = np.outer(d1, d1.conj()) / 2.0
L = np.outer(d0, d0.conj()) + np.outer(d1, d1.conj())    # H_S (vertex reading)
c = np.array([[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]], dtype=complex)
tau = np.pi / np.sqrt(2.0)

def build(sign):
    B0 = np.kron(P0, np.kron(sign * c, I3))
    B1 = np.kron(P1, np.kron(I3, sign * c))
    HS = np.kron(L, I9)
    return HS, B0, B1

def w(s):
    if 0.0 <= s <= 1.0:
        return 32.0 * (0.5 - abs(s - 0.5)) ** 3
    return 0.0

def H_of_t(t, HS, B0, B1, reversed_order=False):
    if not reversed_order:
        a0, a1 = tau * w(t), tau * w(t - 1.0)
    else:  # cell 1 fires first ([0,1]), cell 0 second ([1,2])
        a0, a1 = tau * w(t - 1.0), tau * w(t)
    return HS + a0 * B0 + a1 * B1

def prop_midpoint(t0, t1, n, HS, B0, B1, reversed_order=False, U0=None):
    """Product of exact exponentials of the midpoint Hamiltonian (eigh)."""
    dt = (t1 - t0) / n
    U = np.eye(27, dtype=complex) if U0 is None else U0.copy()
    for k in range(n):
        tm = t0 + (k + 0.5) * dt
        H = H_of_t(tm, HS, B0, B1, reversed_order)
        ev, V = np.linalg.eigh(H)
        U = (V * np.exp(-1j * ev * dt)) @ V.conj().T @ U
    return U

def prop_rk4(t0, t1, n, HS, B0, B1, reversed_order=False, U0=None):
    dt = (t1 - t0) / n
    U = np.eye(27, dtype=complex) if U0 is None else U0.copy()
    f = lambda t, X: -1j * (H_of_t(t, HS, B0, B1, reversed_order) @ X)
    for k in range(n):
        t = t0 + k * dt
        k1 = f(t, U)
        k2 = f(t + dt / 2, U + dt / 2 * k1)
        k3 = f(t + dt / 2, U + dt / 2 * k2)
        k4 = f(t + dt, U + dt * k3)
        U = U + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return U

def expmH(H, t):
    ev, V = np.linalg.eigh(H)
    return (V * np.exp(-1j * ev * t)) @ V.conj().T

# pointer observables
pp = np.diag([0, 1, 0]).astype(complex)          # |p><p| in (r,p,e) order
Z0 = np.kron(I3, np.kron(pp, I3))
Z1 = np.kron(I3, np.kron(I3, pp))

r = np.array([1, 0, 0], dtype=complex)
states = {
    "src_d0_ray": np.kron(d0 / np.sqrt(2), np.kron(r, r)),
    "src_d1_ray": np.kron(d1 / np.sqrt(2), np.kron(r, r)),
    "src_e1_vertex": np.kron(e1v, np.kron(r, r)),
    "src_uniform(kerL)": np.kron((e0 + e1v + e2v) / np.sqrt(3), np.kron(r, r)),
}

def probs(U, psi0, Z):
    v = U @ psi0
    return float(np.real(v.conj() @ (Z @ v)))

out = {}

# ---- structural sanity (parent-spec invariants) ----
HS, B0, B1 = build(+1)
out["TrP0P1"] = float(np.real(np.trace(P0 @ P1)))
out["norm[B0,B1]"] = float(np.linalg.norm(B0 @ B1 - B1 @ B0))
out["norm[B1,Z0]"] = float(np.linalg.norm(B1 @ Z0 - Z0 @ B1))
out["norm[HS,Z0]"] = float(np.linalg.norm(HS @ Z0 - Z0 @ HS))
out["HS_eigs"] = sorted(np.round(np.linalg.eigvalsh(L), 12).tolist())
# completed single-cell endpoint check: exp(-i tau c)
Uc = expmH(c, tau)
out["exp(-i tau c) action"] = {
    "r->p_amp": complex(Uc[1, 0]).__repr__(),
    "p->r_amp": complex(Uc[0, 1]).__repr__(),
    "e->e_amp": complex(Uc[2, 2]).__repr__(),
    "offdiag_leak": float(np.linalg.norm(Uc - np.array([[0,1,0],[1,0,0],[0,0,-1]]))),
}

# ---- main runs: midpoint at three resolutions ----
res = {}
snapshots = {}
for N in (2000, 4000, 8000):
    U1 = prop_midpoint(0.0, 1.0, N, HS, B0, B1)
    U2 = prop_midpoint(1.0, 2.0, N, HS, B0, B1, U0=U1)
    snapshots[N] = (U1, U2)
    entry = {}
    for name, psi in states.items():
        entry[name] = {
            "Pp0_t1": probs(U1, psi, Z0),
            "Pp0_t2": probs(U2, psi, Z0),
            "Pp1_t2": probs(U2, psi, Z1),
        }
    res[N] = entry
out["midpoint"] = res

# convergence ratios (Richardson) on Pp0
conv = {}
for name in states:
    for key in ("Pp0_t1", "Pp0_t2"):
        a = res[2000][name][key]; b = res[4000][name][key]; g = res[8000][name][key]
        denom = b - g
        conv[f"{name}.{key}"] = {
            "q2000": a, "q4000": b, "q8000": g,
            "ratio": (a - b) / denom if abs(denom) > 1e-18 else None,
            "diff_4k_8k": b - g,
        }
out["convergence"] = conv

U1f, U2f = snapshots[8000]

# ---- free evolution t=2 -> t=4 (exact eigh of HS tensor I) ----
Ufree = expmH(HS, 2.0)
U4 = Ufree @ U2f
pers = {}
for name, psi in states.items():
    pers[name] = {"Pp0_t4": probs(U4, psi, Z0),
                  "delta_vs_t2": probs(U4, psi, Z0) - res[8000][name]["Pp0_t2"]}
out["persistence_t4"] = pers

# ---- Moller operator and unitarity ----
Om = expmH(HS, -2.0).conj().T  # exp(+i HS *2)... simpler: expmH gives e^{-iHt}
Om = expmH(HS, -2.0) @ U2f     # e^{+2i HS} = expmH(HS, -2.0)
uerr = np.linalg.norm(Om.conj().T @ Om - np.eye(27))
out["moller_unitarity_frob_err"] = float(uerr)
out["U2_unitarity_frob_err"] = float(np.linalg.norm(U2f.conj().T @ U2f - np.eye(27)))

# ---- causal-order reversal ----
U1r = prop_midpoint(0.0, 1.0, 8000, HS, B0, B1, reversed_order=True)
U2r = prop_midpoint(1.0, 2.0, 8000, HS, B0, B1, reversed_order=True, U0=U1r)
out["order_reversal_frob_||Ufwd-Urev||"] = float(np.linalg.norm(U2f - U2r))
out["order_reversal_relative"] = float(np.linalg.norm(U2f - U2r) / np.linalg.norm(U2f))
rev = {}
for name, psi in states.items():
    rev[name] = {"Pp0_t2_reversed": probs(U2r, psi, Z0),
                 "Pp1_t2_reversed": probs(U2r, psi, Z1)}
out["order_reversal_probs"] = rev

# ---- RK4 cross-check at N=8000 ----
U1k = prop_rk4(0.0, 1.0, 8000, HS, B0, B1)
U2k = prop_rk4(1.0, 2.0, 8000, HS, B0, B1, U0=U1k)
out["rk4_vs_midpoint_||dU||_t2"] = float(np.linalg.norm(U2k - U2f))
rk = {}
for name, psi in states.items():
    rk[name] = {"Pp0_t1": probs(U1k, psi, Z0), "Pp0_t2": probs(U2k, psi, Z0)}
out["rk4_probs"] = rk

# ---- chiral sign flip (c -> -c in both cells): 54-dim reading check ----
HSm, B0m, B1m = build(-1)
U1m = prop_midpoint(0.0, 1.0, 4000, HSm, B0m, B1m)
U2m = prop_midpoint(1.0, 2.0, 4000, HSm, B0m, B1m, U0=U1m)
ch = {}
for name, psi in states.items():
    ch[name] = {"Pp0_t1": probs(U1m, psi, Z0), "Pp0_t2": probs(U2m, psi, Z0)}
out["chiral_minus_probs(N4000)"] = ch
out["chiral_minus_delta_vs_plus"] = {
    name: ch[name]["Pp0_t2"] - res[4000][name]["Pp0_t2"] for name in states}

json.dump(out, open("results.json", "w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
