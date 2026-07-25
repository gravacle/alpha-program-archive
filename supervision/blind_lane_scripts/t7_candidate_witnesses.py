#!/usr/bin/env python3
"""Fresh-lane structural witnesses for the T7 open connected response functor
candidate family. NO kappa_record, NO alpha, NO measured constants.
Only small exact/high-precision structural amplitudes Z(A) at small A.

Conventions (sealed):
  B = [[0, D],[D^dagger, 0]] on C_0 (+) C_1,
  D|e:s->t, phase A_e> = e^{i A_e}|t> - |s>   (unit incidence magnitude),
  tau_R = pi/sqrt(2),
  preparation r = normalized constant section on UNRESOLVED (bulk) vertices only
                  (no-output-without-record forces <p|r>=0),
  completed endpoint = a designated handle endpoint fiber |p>.
"""
import numpy as np

TAU = np.pi / np.sqrt(2.0)

def expmH(B, t):
    """exp(-i t B) for Hermitian B via eigendecomposition."""
    w, V = np.linalg.eigh(B)
    return (V * np.exp(-1j * t * w)) @ V.conj().T

def build_B(nv, edges):
    """edges: list of (s, t, phase). Returns Hermitian B on C^(nv+ne)."""
    ne = len(edges)
    D = np.zeros((nv, ne), dtype=complex)
    for k, (s, t, ph) in enumerate(edges):
        D[t, k] += np.exp(1j * ph)
        D[s, k] -= 1.0
    B = np.zeros((nv + ne, nv + ne), dtype=complex)
    B[:nv, nv:] = D
    B[nv:, :nv] = D.conj().T
    return B

def embed(B_small, idx, dim):
    """Embed operator acting on coordinates idx (list) into C^dim."""
    B = np.zeros((dim, dim), dtype=complex)
    for a, ia in enumerate(idx):
        for b, ib in enumerate(idx):
            B[ia, ib] = B_small[a, b]
    return B

def gamma_hess(afun, a0, h=1e-3):
    """gamma(th) = -log|a(th)/a0|; return gamma''(0) by central difference."""
    gp = -np.log(abs(afun(h) / a0))
    g0 = -np.log(abs(afun(0.0) / a0))
    gm = -np.log(abs(afun(-h) / a0))
    return (gp - 2 * g0 + gm) / h**2

def phase_slope(afun, a0, h=1e-4):
    zp = afun(h) / a0
    zm = afun(-h) / a0
    return (np.angle(zp) - np.angle(zm)) / (2 * h)

print("=" * 78)
print("MODEL M: bulk = 4-cycle (holonomy theta on edge 0), one handle 0->p")
print("vertices 0,1,2,3 bulk; 4 = p endpoint. edges e0..e3 cycle, h:0->4")
print("=" * 78)

NV, NEg = 5, 5
DIM = NV + NEg

def edges_M(th):
    return [(0, 1, th), (1, 2, 0.0), (2, 3, 0.0), (3, 0, 0.0), (0, 4, 0.0)]

# index map: vertices 0..4 ; edges 5..9 (e0,e1,e2,e3,h)
r4 = np.zeros(DIM, dtype=complex); r4[[0, 1, 2, 3]] = 0.5
p_vec = np.zeros(DIM, dtype=complex); p_vec[4] = 1.0

# loop-only operator embedded in DIM (acts on vertices 0..3, edges e0..e3)
def B_loop_M(th):
    Bl = build_B(4, [(0, 1, th), (1, 2, 0.0), (2, 3, 0.0), (3, 0, 0.0)])
    return embed(Bl, [0, 1, 2, 3, 5, 6, 7, 8], DIM)

# handle-only operator embedded (vertices 0,4 ; edge h at index 9)
Bh_small = build_B(2, [(0, 1, 0.0)])   # r=0, p=1, edge
B_handle_M = embed(Bh_small, [0, 4, 9], DIM)

def a_joint(th):
    B = build_B(NV, edges_M(th))
    return p_vec.conj() @ expmH(B, TAU) @ r4

def a_loop_then_open(th):
    return p_vec.conj() @ expmH(B_handle_M, TAU) @ expmH(B_loop_M(th), TAU) @ r4

def a_open_then_loop(th):
    return p_vec.conj() @ expmH(B_loop_M(th), TAU) @ expmH(B_handle_M, TAU) @ r4

for name, f in [("JOINT (single global handle, one interval)", a_joint),
                ("LOOP-THEN-OPEN (bulk tau_R, then handle tau_R)", a_loop_then_open),
                ("OPEN-THEN-LOOP (handle first)", a_open_then_loop)]:
    a0 = f(0.0)
    if abs(a0) < 1e-14:
        print(f"{name}\n  a(0) = 0  -> normalized Z undefined (ZERO BASELINE)")
        continue
    z1 = f(0.1) / a0
    print(f"{name}")
    print(f"  a(0)          = {a0:.12f}   |a(0)| = {abs(a0):.12f}")
    print(f"  Z(0.1)        = {z1:.12f}   |Z(0.1)| = {abs(z1):.12f}")
    print(f"  gamma''(0)    = {gamma_hess(f, a0):+.9f}")
    print(f"  d(arg Z)/dth  = {phase_slope(f, a0):+.9f}")

print()
print("=" * 78)
print("MODEL P: 2-vertex plaquette (edges a: phase th, b: phase 0), relay orders")
print("vertices 0,1 bulk; 2 = p (handle at 1); 3 = q (interior handle at 0)")
print("=" * 78)
# coordinates: v0,v1,p=2,q=3, edges a=4,b=5,hb=6,h0=7
NVp, NEp = 4, 4
DIMp = NVp + NEp
def edges_P(th):
    return [(0, 1, th), (0, 1, 0.0), (1, 2, 0.0), (0, 3, 0.0)]
r2 = np.zeros(DIMp, dtype=complex); r2[[0, 1]] = 1 / np.sqrt(2)
pP = np.zeros(DIMp, dtype=complex); pP[2] = 1.0

def B_of(th, keep):  # keep: subset of edge labels {'a','b','hb','h0'}
    lab = ['a', 'b', 'hb', 'h0']
    idx_v = [0, 1, 2, 3]
    E = edges_P(th)
    edges = [E[i] for i in range(4) if lab[i] in keep]
    eidx = [4 + i for i in range(4) if lab[i] in keep]
    Bs = build_B(4, edges)
    return embed(Bs, idx_v + eidx, DIMp)

def a_P_joint_all(th):     # both handles present, joint
    return pP.conj() @ expmH(B_of(th, {'a', 'b', 'hb', 'h0'}), TAU) @ r2

def a_P_joint_single(th):  # only boundary handle hb, joint
    return pP.conj() @ expmH(B_of(th, {'a', 'b', 'hb'}), TAU) @ r2

def a_P_loop_open(th):     # loop then boundary handle
    return pP.conj() @ expmH(B_of(0, {'hb'}), TAU) @ expmH(B_of(th, {'a', 'b'}), TAU) @ r2

def a_P_seq_S1(th):        # causal cells: c1={a,h0} then c2={b,hb}  (handle-per-cell)
    U1 = expmH(B_of(th, {'a', 'h0'}), TAU)
    U2 = expmH(B_of(0, {'b', 'hb'}), TAU)
    return pP.conj() @ U2 @ U1 @ r2

def a_P_seq_S2(th):        # cells: c1={a} (recordless) then c2={b,hb}
    U1 = expmH(B_of(th, {'a'}), TAU)
    U2 = expmH(B_of(0, {'b', 'hb'}), TAU)
    return pP.conj() @ U2 @ U1 @ r2

def a_P_seq_S3(th):        # swap cell order: c1={b,h0} then c2={a,hb}
    U1 = expmH(B_of(0, {'b', 'h0'}), TAU)
    U2 = expmH(B_of(th, {'a', 'hb'}), TAU)
    return pP.conj() @ U2 @ U1 @ r2

for name, f in [("P-JOINT single boundary handle", a_P_joint_single),
                ("P-JOINT both handles", a_P_joint_all),
                ("P-LOOP-THEN-OPEN", a_P_loop_open),
                ("P-SEQ S1: {a,h0} -> {b,hb}", a_P_seq_S1),
                ("P-SEQ S2: {a} -> {b,hb} (recordless cell)", a_P_seq_S2),
                ("P-SEQ S3: {b,h0} -> {a,hb}", a_P_seq_S3)]:
    a0 = f(0.0)
    if abs(a0) < 1e-14:
        print(f"{name}\n  a(0) = 0 -> ZERO BASELINE, Z undefined")
        continue
    z1 = f(0.1) / a0
    print(f"{name}")
    print(f"  a(0)         = {a0:.12f}  |a(0)| = {abs(a0):.10f}")
    print(f"  |Z(0.1)|     = {abs(z1):.12f}   arg Z(0.1) = {np.angle(z1):+.10f}")
    print(f"  gamma''(0)   = {gamma_hess(f, a0):+.9f}"
          f"   d(argZ)/dth = {phase_slope(f, a0):+.9f}")

print()
print("=" * 78)
print("WITNESS E: mixed cell K_{1,2} (root 0 -> bulk successor 1, root 0 -> p)")
print("does tau_R = pi/sqrt(2) still give exact/complete transfer? ")
print("=" * 78)
Bk12 = build_B(3, [(0, 1, 0.0), (0, 2, 0.0)])   # vertices 0,1(bulk),2(=p); edges 3,4
U12 = expmH(Bk12, TAU)
d0 = np.zeros(5, dtype=complex); d0[0] = 1
out = U12 @ d0
print(f"  |<root|U|root>|      = {abs(out[0]):.10f}   (K13 sealed value: 0)")
print(f"  |<bulk1|U|root>|     = {abs(out[1]):.10f}")
print(f"  |<p|U|root>|         = {abs(out[2]):.10f}   (K13 sealed value: 1)")
print(f"  edge components      = {abs(out[3]):.6f}, {abs(out[4]):.6f}")
# least positive tau with zero root survival for K_{1,2}?
# spectral form: eigenvalues {0,+-1,+-sqrt3}; survival(t) = w0 + w1 cos t + w3 cos(sqrt3 t)
w, V = np.linalg.eigh(Bk12)
weights = {}
for i, lam in enumerate(w):
    key = round(abs(lam) ** 2, 6)
    weights[key] = weights.get(key, 0.0) + abs(V[0, i]) ** 2
print(f"  survival(t) = {weights.get(0.0,0):.6f} + {weights.get(1.0,0):.6f}*cos(t)"
      f" + {weights.get(3.0,0):.6f}*cos(sqrt(3) t)   [real, all-positive weights]")
def surv(t):
    return abs(d0.conj() @ expmH(Bk12, t) @ d0)
ts = np.linspace(0.01, 40.0, 40000)
vals = np.array([surv(t) for t in ts])
mins = [(ts[i], vals[i]) for i in range(1, len(ts) - 1)
        if vals[i] < vals[i - 1] and vals[i] < vals[i + 1]]
print("  first local minima of |<r|U(t)|r>| for K_{1,2}:")
for t, v in mins[:6]:
    print(f"    t = {t:8.4f}   |surv| = {v:.8f}")
print(f"  global min over scan = {vals.min():.8f}  (exact zero requires cos t = cos(sqrt3 t) = -1")
print(f"   simultaneously, impossible for incommensurate 1, sqrt(3) at t>0 ->")
print(f"   NO exact closure tau exists for the mixed K_(1,2) carrier)")
print(f"  sealed tau_R = {TAU:.4f}: K_(1,3) closure is exact there; K_(1,2) is not (0.174 survival).")

print()
print("POSITIVE CONTROL: sealed one-handle exactness in these conventions")
Bh3 = build_B(2, [(0, 1, 0.0)])
u = expmH(Bh3, TAU) @ np.array([1.0, 0, 0], dtype=complex)
print(f"  exp(-i tau_R B_h)|r> components: r={u[0]:.2e}, p={u[1]:.6f}, e={u[2]:.2e}")

print()
print("K_(1,3) closure control: root survival at tau_R for the 3-handle star")
Bstar = build_B(4, [(0, 1, 0.0), (0, 2, 0.0), (0, 3, 0.0)])
d0s = np.zeros(7, dtype=complex); d0s[0] = 1
outs = expmH(Bstar, TAU) @ d0s
print(f"  |<r|U|r>| = {abs(outs[0]):.3e}   endpoint amplitudes: "
      f"{abs(outs[1]):.6f}, {abs(outs[2]):.6f}, {abs(outs[3]):.6f}")

print()
print("=" * 78)
print("WITNESS F: baseline volume scaling of single-global-handle candidates")
print("=" * 78)
for n in [4, 8, 16]:
    edges = [(i, (i + 1) % n, 0.0) for i in range(n)] + [(0, n, 0.0)]
    B = build_B(n + 1, edges)
    r = np.zeros(n + 1 + n + 1, dtype=complex); r[:n] = 1 / np.sqrt(n)
    p = np.zeros(n + 1 + n + 1, dtype=complex); p[n] = 1.0
    aJ = p.conj() @ expmH(B, TAU) @ r
    # loop-then-open baseline = <delta_0|r> = 1/sqrt(n) exactly
    print(f"  n = {n:3d}: joint a(0) = {abs(aJ):.8f}   loop-then-open a(0) = {1/np.sqrt(n):.8f}")
