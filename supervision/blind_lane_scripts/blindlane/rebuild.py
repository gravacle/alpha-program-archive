"""Blind rebuild of the causal-transported write/tail gate from spec text alone.

Regulator (my reconstruction from the pinned inputs):
 - Chain of N causal cells, vertices v_0..v_N (V = N+1), edges E = N, spacing a = 1.
 - Free incidence tail Hamiltonian H_c = [[0, d^T],[d, 0]] on C^V (+) C^E,
   (d psi)_j = psi_{j+1} - psi_j   (finite-chain version of the pinned
   incidence-continuum block operator, dimensionless a=1 units).
 - Write generator for cell c:  B_c = Q_c  (x) gamma5 (x) c_del,
   Q_c = diag(P_c, 0_E) with P_c = |delta><delta|/<delta,delta>,
   delta = e_{c+1} - e_c (vertex space);  gamma5 = diag(1,-1);
   c_del = [[0,0,-i],[0,0,+i],[+i,-i,0]] on span{|r>,|p>,|e>}.
 - tau_R = pi/sqrt(2); admissible pulses have integral v = tau_R.
 - Ready state: chain = delta/sqrt(2) (in range of P_c), spin = chirality
   eigenstate, record = |r>.  First-pointer probability = P(record = |p>).
"""
import numpy as np

np.set_printoptions(precision=6, suppress=False)
tau_R = np.pi / np.sqrt(2.0)

gamma5 = np.diag([1.0, -1.0]).astype(complex)
c_del = np.array([[0, 0, -1j],
                  [0, 0, +1j],
                  [+1j, -1j, 0]], dtype=complex)

def chain_ops(N):
    V, E = N + 1, N
    d = np.zeros((E, V))
    for j in range(E):
        d[j, j + 1] = 1.0
        d[j, j] = -1.0
    M = V + E
    Hc = np.zeros((M, M))
    Hc[V:, :V] = d
    Hc[:V, V:] = d.T
    return Hc, V, E, M

def cell_Q(N, c):
    V, E = N + 1, N
    delta = np.zeros(V)
    delta[c] = -1.0
    delta[c + 1] = 1.0
    P = np.outer(delta, delta) / (delta @ delta)
    Q = np.zeros((V + E, V + E))
    Q[:V, :V] = P
    return Q, delta

def expm_herm(H, t):
    w, U = np.linalg.eigh(H)
    return (U * np.exp(-1j * w * t)) @ U.conj().T

# ---------------- single-cell setup ----------------
def build_single(N, c):
    Hc, V, E, M = chain_ops(N)
    Q, delta = cell_Q(N, c)
    I2, I3 = np.eye(2), np.eye(3)
    H0 = np.kron(Hc, np.kron(I2, I3)).astype(complex)
    B = np.kron(Q, np.kron(gamma5, c_del))
    # ready state
    chain0 = np.zeros(M); chain0[:V] = delta / np.sqrt(2.0)
    return Hc, H0, B, M, chain0

def ready_state(M, chain0, spin):
    rec = np.zeros(3); rec[0] = 1.0  # |r>
    return np.kron(chain0, np.kron(spin, rec)).astype(complex)

def record_probs(psi, M, nrec=3):
    amp = psi.reshape(M * 2 * (nrec // 3) if False else -1, 3) if False else psi.reshape(-1, 3)
    return np.sum(np.abs(amp) ** 2, axis=0)

N, c = 40, 20
Hc, H0, B, M, chain0 = build_single(N, c)
wHc, UHc = np.linalg.eigh(Hc)
wH0, UH0 = np.linalg.eigh(H0)
wB, UB = np.linalg.eigh(B)

def U0_mat(t):
    return (UH0 * np.exp(-1j * wH0 * t)) @ UH0.conj().T

def UB_mat(theta):  # exp(-i theta B)
    return (UB * np.exp(-1j * wB * theta)) @ UB.conj().T

# ---- sanity: isolated gate ----
spin_up = np.array([1.0, 0.0]); spin_dn = np.array([0.0, 1.0])
for sp, name in [(spin_up, "chir+"), (spin_dn, "chir-")]:
    psi0 = ready_state(M, chain0, sp)
    psi = UB_mat(tau_R) @ psi0
    print(f"isolated gate {name}: record probs (r,p,e) =", record_probs(psi, M))

# ---- (a) commutator ----
C = H0 @ B - B @ H0
normF = np.linalg.norm(C, 'fro')
print("\n(a) ||[H0,B_c]||_F =", normF, " 4*sqrt(3) =", 4 * np.sqrt(3.0))
# edge cell for reference
_, H0e, Be, Me, _ = build_single(N, 0)
print("    edge-cell value =", np.linalg.norm(H0e @ Be - Be @ H0e, 'fro'),
      " 2*sqrt(10) =", 2 * np.sqrt(10.0))

# ---- (b) static covariance failure ----
U0tau = U0_mat(tau_R)
Btrans = U0tau @ B @ U0tau.conj().T
cov_fail = np.linalg.norm(Btrans - B, 'fro')
print("\n(b) ||U0(tau_R) B U0(tau_R)* - B||_F =", cov_fail)
# supremum over t in [0, tau_R]
ts = np.linspace(0, tau_R, 41)
vals = []
for t in ts:
    U0t = U0_mat(t)
    vals.append(np.linalg.norm(U0t @ B @ U0t.conj().T - B, 'fro'))
print("    max over [0,tau_R] =", max(vals), " at t =", ts[int(np.argmax(vals))])
# derivative at 0 should equal ||[H0,B]||_F
print("    d/dt at 0 (= ||[H0,B]||_F):", normF)

# ---- (c) static sum first-pointer probability ----
Hstat = H0 + B
whs, Uhs = np.linalg.eigh(Hstat)
def Ustat(t):
    return (Uhs * np.exp(-1j * whs * t)) @ Uhs.conj().T
for sp, name in [(spin_up, "chir+"), (spin_dn, "chir-")]:
    psi0 = ready_state(M, chain0, sp)
    psi = Ustat(tau_R) @ psi0
    pr = record_probs(psi, M)
    print(f"\n(c) static sum, {name}: record probs (r,p,e) =", pr)

# cross-check with Trotter (method 2) and N-dependence
def taylor_step(applyH, psi, dt, K=18):
    out = psi.copy(); term = psi.copy()
    for k in range(1, K + 1):
        term = (-1j * dt / k) * applyH(term)
        out = out + term
    return out

def static_prob(N, c, spin, nsteps=4000, method="eig"):
    Hc_, H0_, B_, M_, ch0 = build_single(N, c)
    psi0 = ready_state(M_, ch0, spin)
    Hs = H0_ + B_
    if method == "eig":
        w, U = np.linalg.eigh(Hs)
        psi = (U * np.exp(-1j * w * tau_R)) @ (U.conj().T @ psi0)
    else:
        dt = tau_R / nsteps
        psi = psi0
        applyH = lambda v: Hs @ v
        for _ in range(nsteps):
            psi = taylor_step(applyH, psi, dt)
    return record_probs(psi, M_)

print("(c) check N=40 eig     :", static_prob(40, 20, spin_up))
print("(c) check N=40 taylor  :", static_prob(40, 20, spin_up, method="taylor"))
print("(c) check N=80 eig     :", static_prob(80, 40, spin_up))
print("(c) check N=120 eig    :", static_prob(120, 60, spin_up))

# ---- (d) transported parent ----
# exact: U(T,0) = U0(T) exp(-i tau_R B); record prob unaffected by U0
psi0 = ready_state(M, chain0, spin_up)
psi_ex = U0_mat(tau_R) @ (UB_mat(tau_R) @ psi0)
print("\n(d) transported exact: record probs =", record_probs(psi_ex, M))

# numerical: midpoint time slicing of H(t) = H0 + v(t) U0(t) B U0(t)*
def applyU0(psi, t, M_, UHc_, wHc_, nrec):
    # U0 = exp(-i Hc t) on chain factor only
    A = psi.reshape(M_, -1)
    A = (UHc_ * np.exp(-1j * wHc_ * t)) @ (UHc_.conj().T @ A)
    return A.reshape(-1)

def evolve_transported(psi0, profile, T, nsteps, Bmats, pulses, M_, UHc_, wHc_):
    """H(t) = H0 + sum_j v_j(t) U0(t) B_j U0(t)*.  Midpoint Taylor slicing."""
    dt = T / nsteps
    psi = psi0.astype(complex)
    for k in range(nsteps):
        tm = (k + 0.5) * dt
        vs = [p(tm) for p in pulses]
        def applyH(v):
            out = _applyH0(v, M_).astype(complex)
            for vv, Bm in zip(vs, Bmats):
                if vv != 0.0:
                    w = applyU0(v, -tm, M_, UHc_, wHc_, None)
                    w = Bm @ w
                    w = applyU0(w, tm, M_, UHc_, wHc_, None)
                    out += vv * w
            return out
        psi = taylor_step(applyH, psi, dt)
    return psi

def _applyH0(v, M_):
    A = v.reshape(M_, -1)
    return (Hc @ A).reshape(-1)

T = tau_R
sq = lambda t: 1.0 if 0 <= t <= T else 0.0
psi_num = evolve_transported(psi0, None, T, 600, [B], [sq], M, UHc, wHc)
print("(d) transported numeric (midpoint n=600): record probs =",
      record_probs(psi_num, M))
print("    state error vs exact:", np.linalg.norm(psi_num - psi_ex))
