#!/usr/bin/env python3
"""Refinement pass: same sealed construction, higher resolutions, Richardson limits."""
import numpy as np, math, itertools, json

TAU_R = math.pi / math.sqrt(2.0)

def pauli():
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    return sx, sy, sz

sx, sy, sz = pauli()
I2 = np.eye(2, dtype=complex); Z2 = np.zeros((2, 2), dtype=complex)
g0 = np.block([[I2, Z2], [Z2, -I2]])
gs = [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
g5 = 1j * g0 @ gs[0] @ gs[1] @ gs[2]
alpha_x = g0 @ gs[0]; S_n = -1j * g0 @ g5

D = np.zeros((3, 3), dtype=complex)
for j in range(3):
    D[j, (j + 1) % 3] += 0.5
    D[j, (j - 1) % 3] -= 0.5
h_src = np.kron(-1j * D, alpha_x)
evals, evecs = np.linalg.eigh(h_src)
lam = math.sqrt(3.0) / 2.0
idx_neg = np.where(evals < -1e-12)[0]; idx_pos = np.where(evals > 1e-12)[0]
V = evecs[:, np.concatenate([idx_neg, idx_pos])]
h8 = V.conj().T @ h_src @ V
masks = (np.diag([1.0, 1.0, 0.0]).astype(complex), np.diag([0.0, 1.0, 1.0]).astype(complex))
B8 = [V.conj().T @ np.kron(masks[c], S_n) @ V for c in range(2)]

Gam = np.diag([1.0, 1.0, -1.0]).astype(complex)
b = np.array([[0, 0, -1], [0, 0, 1], [-1, 1, 0]], dtype=complex)
c_q = 1j * Gam @ b
I3 = np.eye(3, dtype=complex)
q_ops = [np.kron(c_q, I3), np.kron(I3, c_q)]

modes, n_part = 8, 4
basis = list(itertools.combinations(range(modes), n_part))
bindex = {s: i for i, s in enumerate(basis)}
dimF = len(basis)

def dGamma_wedge(B):
    M = np.zeros((dimF, dimF), dtype=complex)
    for col, S in enumerate(basis):
        for j in S:
            sgn_j = (-1) ** sum(1 for x in S if x < j)
            rest = [x for x in S if x != j]
            for i in range(modes):
                if B[i, j] == 0 or i in rest:
                    continue
                sgn_i = (-1) ** sum(1 for x in rest if x < i)
                new = tuple(sorted(rest + [i]))
                M[bindex[new], col] += B[i, j] * sgn_j * sgn_i
    return M

dGh = dGamma_wedge(h8); dGB = [dGamma_wedge(B8[c]) for c in range(2)]
I9 = np.eye(9, dtype=complex)
H0 = np.kron(dGh, I9)
W = [np.kron(dGB[c], q_ops[c]) for c in range(2)]
sl = np.zeros(dimF, dtype=complex); sl[bindex[(0, 1, 2, 3)]] = 1.0
rr = np.zeros(9, dtype=complex); rr[0] = 1.0
psi0 = np.kron(sl, rr)

def envelope(t):
    if not 0.0 <= t <= 1.0:
        return 0.0
    return TAU_R * 32.0 * min(t, 1.0 - t) ** 3

def rk4_cell(psi, Wc, steps):
    dt = 1.0 / steps
    y = psi.copy()
    for n in range(steps):
        t = n * dt
        def dv(tt, yy):
            return -1j * (H0 @ yy + envelope(tt) * (Wc @ yy))
        k1 = dv(t, y); k2 = dv(t + dt / 2, y + dt * k1 / 2)
        k3 = dv(t + dt / 2, y + dt * k2 / 2); k4 = dv(t + dt, y + dt * k3)
        y = y + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
    return y

def expmv(vfac, y, dt, Wc):
    out = y.copy(); term = y.copy()
    for k in range(1, 60):
        term = (-1j * dt) * (H0 @ term + vfac * (Wc @ term)) / k
        out = out + term
        if np.linalg.norm(term) < 1e-17 * np.linalg.norm(out):
            break
    return out

def mag_cell(psi, Wc, steps):
    dt = 1.0 / steps
    y = psi.copy()
    for n in range(steps):
        y = expmv(envelope((n + 0.5) * dt), y, dt, Wc)
    return y

def amps(integ, steps):
    a1 = integ(psi0, W[0], steps)
    a2 = integ(a1, W[1], steps)
    e_pr = np.kron(sl, np.eye(9)[:, 3].astype(complex))
    e_pp = np.kron(sl, np.eye(9)[:, 4].astype(complex))
    return complex(np.vdot(e_pr, a1)), complex(np.vdot(e_pp, a2))

res = {}
for N in (2000, 4000, 8000):
    res[("rk4", N)] = amps(rk4_cell, N)
    print(f"rk4 N={N}: a_p={res[('rk4',N)][0]:.16f} a_pp={res[('rk4',N)][1]:.16f}", flush=True)
for N in (800, 1600):
    res[("mag", N)] = amps(mag_cell, N)
    print(f"mag N={N}: a_p={res[('mag',N)][0]:.16f} a_pp={res[('mag',N)][1]:.16f}", flush=True)

# Richardson
rk_ap = res[("rk4", 8000)][0] + (res[("rk4", 8000)][0] - res[("rk4", 4000)][0]) / 15
rk_app = res[("rk4", 8000)][1] + (res[("rk4", 8000)][1] - res[("rk4", 4000)][1]) / 15
mg_ap = res[("mag", 1600)][0] + (res[("mag", 1600)][0] - res[("mag", 800)][0]) / 3
mg_app = res[("mag", 1600)][1] + (res[("mag", 1600)][1] - res[("mag", 800)][1]) / 3
print(f"rk4  Richardson a_p = {rk_ap.real:+.16f}{rk_ap.imag:+.16f}i")
print(f"rk4  Richardson a_pp= {rk_app.real:+.16f}{rk_app.imag:+.16f}i")
print(f"mag  Richardson a_p = {mg_ap.real:+.16f}{mg_ap.imag:+.16f}i")
print(f"mag  Richardson a_pp= {mg_app.real:+.16f}{mg_app.imag:+.16f}i")
print(f"|rk-mag| a_p = {abs(rk_ap-mg_ap):.3e}  a_pp = {abs(rk_app-mg_app):.3e}")
print(f"rk4 4th-order ratio a_p  : {abs(res[('rk4',2000)][0]-res[('rk4',4000)][0])/abs(res[('rk4',4000)][0]-res[('rk4',8000)][0]):.4f}")
print(f"rk4 4th-order ratio a_pp : {abs(res[('rk4',2000)][1]-res[('rk4',4000)][1])/abs(res[('rk4',4000)][1]-res[('rk4',8000)][1]):.4f}")
json.dump(dict(a_p=[rk_ap.real, rk_ap.imag], a_pp=[rk_app.real, rk_app.imag]),
          open("refined.json", "w"), indent=1)
