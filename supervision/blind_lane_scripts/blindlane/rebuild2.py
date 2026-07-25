"""Part 2: (e) Moller error, (f) profile independence + slicing convergence,
(g) two-cell causal Moller error, (h) uniqueness check, plus high-precision (c)."""
import numpy as np

tau_R = np.pi / np.sqrt(2.0)
gamma5 = np.diag([1.0, -1.0]).astype(complex)
c_del = np.array([[0, 0, -1j], [0, 0, +1j], [+1j, -1j, 0]], dtype=complex)

def chain_ops(N):
    V, E = N + 1, N
    d = np.zeros((E, V))
    for j in range(E):
        d[j, j + 1] = 1.0; d[j, j] = -1.0
    M = V + E
    Hc = np.zeros((M, M))
    Hc[V:, :V] = d; Hc[:V, V:] = d.T
    return Hc, V, E, M

def cell_Q(N, c):
    V, E = N + 1, N
    delta = np.zeros(V); delta[c] = -1.0; delta[c + 1] = 1.0
    P = np.outer(delta, delta) / 2.0
    Q = np.zeros((V + E, V + E)); Q[:V, :V] = P
    return Q, delta

N, c = 40, 20
Hc, V, E, M = chain_ops(N)
wHc, UHc = np.linalg.eigh(Hc)
Q1, delta1 = cell_Q(N, c)
Q2, delta2 = cell_Q(N, c + 1)

I2, I3, I9 = np.eye(2), np.eye(3), np.eye(9)

# ---------- single cell (record dim 3) ----------
B1s = np.kron(Q1, np.kron(gamma5, c_del))
H0s = np.kron(Hc, np.kron(I2, I3)).astype(complex)
wB1s, UB1s = np.linalg.eigh(B1s)
wH0s, UH0s = np.linalg.eigh(H0s)
Ms = M * 6

def expB1s(theta):
    return (UB1s * np.exp(-1j * wB1s * theta)) @ UB1s.conj().T

def U0s(t):
    return (UH0s * np.exp(-1j * wH0s * t)) @ UH0s.conj().T

def applyH0s(v):
    A = v.reshape(M, -1)
    return (Hc @ A).reshape(-1).astype(complex)

def applyU0s(v, t):
    A = v.reshape(M, -1)
    return ((UHc * np.exp(-1j * wHc * t)) @ (UHc.conj().T @ A)).reshape(-1)

def taylor_step(applyH, psi, dt, K=20):
    out = psi.copy(); term = psi.copy()
    for k in range(1, K + 1):
        term = (-1j * dt / k) * applyH(term)
        out = out + term
    return out

def evolve(psi0, pulses, Bmats, T, nsteps, applyH0, applyU0):
    dt = T / nsteps
    psi = psi0.astype(complex)
    for k in range(nsteps):
        tm = (k + 0.5) * dt
        vs = [p(tm) for p in pulses]
        def applyH(v):
            out = applyH0(v)
            for vv, Bm in zip(vs, Bmats):
                if vv != 0.0:
                    w = applyU0(v, -tm)
                    w = Bm @ w
                    w = applyU0(w, tm)
                    out = out + vv * w
            return out
        psi = taylor_step(applyH, psi, dt)
    return psi

# ready state (chir+)
chain0 = np.zeros(M); chain0[:V] = delta1 / np.sqrt(2.0)
spin = np.array([1.0, 0.0]); rec_r3 = np.array([1.0, 0, 0])
psi0s = np.kron(chain0, np.kron(spin, rec_r3)).astype(complex)

rng = np.random.default_rng(7)
def rand_state(n):
    v = rng.normal(size=n) + 1j * rng.normal(size=n)
    return v / np.linalg.norm(v)

# ---------- high-precision (c) ----------
Hstat = H0s + B1s
w, U = np.linalg.eigh(Hstat)
psi = (U * np.exp(-1j * w * tau_R)) @ (U.conj().T @ psi0s)
pr = np.sum(np.abs(psi.reshape(-1, 3)) ** 2, axis=0)
print("(c) static probs (r,p,e), 12 digits:",
      " ".join(f"{x:.12f}" for x in pr))

# ---------- (e) finite-support Moller error ----------
# pulse: sine bump on [0,T1], then free evolution to t_end
T1 = 2.0
amp = np.pi * tau_R / (2 * T1)
bump = lambda t: amp * np.sin(np.pi * t / T1) if 0 <= t <= T1 else 0.0
print("\nintegral check:", np.trapezoid([bump(t) for t in np.linspace(0, T1, 20001)],
                                        np.linspace(0, T1, 20001)), "vs", tau_R)
t_end = T1 + 3.0
Wexact = expB1s(tau_R)  # candidate Moller: U(t)^* U0(t) = exp(+i tau B)^* ... check sign
errs = []
for _ in range(4):
    psir = rand_state(Ms)
    # numeric U(t_end,0) psi
    psin = evolve(psir, [bump], [B1s], t_end, 3000, applyH0s, applyU0s)
    # exact: U0(t_end) exp(-i tau B) psi
    psie = applyU0s(Wexact @ psir, t_end)
    errs.append(np.linalg.norm(psin - psie))
    # Moller form: U(t)^dagger U0(t) psi = exp(+i tau_R B) psi
print("(e) ||U(t,0)psi - U0(t) e^{-i tau B} psi|| for random psi:", errs)

# convergence of that residual with nsteps (to show it's pure slicing error)
psir = rand_state(Ms)
for n in (500, 1000, 2000, 4000):
    psin = evolve(psir, [bump], [B1s], t_end, n, applyH0s, applyU0s)
    psie = applyU0s(Wexact @ psir, t_end)
    print(f"    nsteps={n}: err={np.linalg.norm(psin-psie):.3e}")

# ---------- (f) profile independence + convergence ratio ----------
T = 2.0
profiles = {
    "square":   lambda t: tau_R / T if 0 <= t <= T else 0.0,
    "sine":     lambda t: (np.pi * tau_R / (2 * T)) * np.sin(np.pi * t / T) if 0 <= t <= T else 0.0,
    "triangle": lambda t: (2 * tau_R / T) * (1 - abs(2 * t / T - 1)) if 0 <= t <= T else 0.0,
    "parabola": lambda t: (6 * tau_R / T ** 3) * t * (T - t) if 0 <= t <= T else 0.0,
}
print("\n(f) profile independence, U(T,0) vs U0(T) e^{-i tau B}, random state:")
psir = rand_state(Ms)
psie = applyU0s(Wexact @ psir, T)
for name, p in profiles.items():
    # trapezoid slicing errors handled by high n
    psin = evolve(psir, [p], [B1s], T, 4000, applyH0s, applyU0s)
    print(f"    {name:9s}: err = {np.linalg.norm(psin - psie):.3e}")

print("\n(f) convergence ratio (sine profile), err(n) and err(2n)/err(n):")
prev = None
for n in (16, 32, 64, 128, 256, 512, 1024):
    psin = evolve(psir, [profiles['sine']], [B1s], T, n, applyH0s, applyU0s)
    e = np.linalg.norm(psin - psie)
    r = "" if prev is None else f"ratio={e/prev:.4f}"
    print(f"    n={n:5d}: err={e:.6e}  {r}")
    prev = e

# ---------- (g) two-cell causal Moller error ----------
# record space 3x3=9; B1 acts on first record factor, B2 on second
B1t = np.kron(Q1, np.kron(gamma5, np.kron(c_del, I3)))
B2t = np.kron(Q2, np.kron(gamma5, np.kron(I3, c_del)))
print("\n[B1,B2] nonzero check:", np.linalg.norm(B1t @ B2t - B2t @ B1t))
Mt = M * 2 * 9
wB1t, UB1t = np.linalg.eigh(B1t)
wB2t, UB2t = np.linalg.eigh(B2t)
def expB(theta, wB, UB):
    return (UB * np.exp(-1j * wB * theta)) @ UB.conj().T
def applyH0t(v):
    A = v.reshape(M, -1)
    return (Hc @ A).reshape(-1).astype(complex)
def applyU0t(v, t):
    A = v.reshape(M, -1)
    return ((UHc * np.exp(-1j * wHc * t)) @ (UHc.conj().T @ A)).reshape(-1)

# causal pulses: cell 1 on [0,T1g], cell 2 on [T1g, 2 T1g]
T1g = 2.0
ampg = np.pi * tau_R / (2 * T1g)
v1 = lambda t: ampg * np.sin(np.pi * t / T1g) if 0 <= t <= T1g else 0.0
v2 = lambda t: ampg * np.sin(np.pi * (t - T1g) / T1g) if T1g <= t <= 2 * T1g else 0.0
Tg = 2 * T1g
EB1 = expB(tau_R, wB1t, UB1t)
EB2 = expB(tau_R, wB2t, UB2t)
errs = []
for _ in range(3):
    psir = rand_state(Mt)
    psin = evolve(psir, [v1, v2], [B1t, B2t], Tg, 3000, applyH0t, applyU0t)
    psie = applyU0t(EB2 @ (EB1 @ psir), Tg)   # ordered product, later left
    errs.append(np.linalg.norm(psin - psie))
print("(g) two-cell causal Moller error (random states):", errs)
# wrong order for contrast
psir = rand_state(Mt)
psin = evolve(psir, [v1, v2], [B1t, B2t], Tg, 3000, applyH0t, applyU0t)
bad = np.linalg.norm(psin - applyU0t(EB1 @ (EB2 @ psir), Tg))
print("    (wrong-order product residual, for contrast):", bad)

# two-cell endpoint: both records flip, first record state preserved
chain0t = np.zeros(M); chain0t[:V] = delta1 / np.sqrt(2.0)
# note: ready source state must be active for both cells? P1 delta1 = delta1; P2 delta1 = -delta2/2... overlap
psi0t = np.kron(chain0t, np.kron(spin, np.kron(rec_r3, rec_r3))).astype(complex)
psi_out = applyU0t(EB2 @ (EB1 @ psi0t), Tg)
A = psi_out.reshape(-1, 9)
prob9 = np.sum(np.abs(A) ** 2, axis=0).reshape(3, 3)
print("    two-cell endpoint joint record probs (rows=rec1 r/p/e, cols=rec2):")
print(np.round(prob9, 6))

# ---------- (h) uniqueness: numerical check of the forced solution ----------
# tilde B(t) = U0(t) B U0(t)* satisfies the functional equation; any solution
# must equal it because setting t=0 in the equation forces tilde B(s)=U0(s) B U0(s)*.
ok = True
for t, s in [(0.3, 0.7), (1.1, 0.4), (0.0, 2.2)]:
    U0t = U0s(t); U0ss = U0s(s)
    lhs = U0s(t + s) @ B1s @ U0s(t + s).conj().T
    rhs = U0ss @ (U0t @ B1s @ U0t.conj().T) @ U0ss.conj().T
    ok &= np.linalg.norm(lhs - rhs) < 1e-10
print("\n(h) transported solution satisfies functional equation:", ok)
