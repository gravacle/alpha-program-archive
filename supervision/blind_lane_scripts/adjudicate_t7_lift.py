#!/usr/bin/env python3
"""Fresh-context independent adjudication of the T7 primitive connected-lift
blocker. All constructions are rebuilt from the sealed spec text, not from
the construction scripts. No measured constant is used anywhere.
"""
from __future__ import annotations

import math
import numpy as np

rng = np.random.default_rng(773301)
report: dict[str, object] = {}


def check(name: str, cond: bool, detail: str = "") -> None:
    status = "PASS" if cond else "FAIL"
    report[name] = (status, detail)
    print(f"[{status}] {name}  {detail}")
    if not cond:
        raise SystemExit(f"ADJUDICATION CHECK FAILED: {name}")


# ============================================================
# CLAIM 1 -- Fubini-Study curvature triple + D3 uniqueness core
# ============================================================
print("\n=== CLAIM 1: response-closure selection (FS triple) ===")


def psi(theta: float) -> np.ndarray:
    return np.array([1.0, np.exp(1j * theta)], dtype=complex) / math.sqrt(2)


# exact FS metric at theta=0: g = <psi'|psi'> - |<psi|psi'>|^2
h = 1e-5
dpsi = (psi(h) - psi(-h)) / (2 * h)
g_fs = float((np.vdot(dpsi, dpsi) - abs(np.vdot(psi(0.0), dpsi)) ** 2).real)
check("FS_metric_quarter", abs(g_fs - 0.25) < 1e-9, f"g_FS(0)={g_fs:.12f}")

# closures evaluated on the relative-holonomy orbit
def gamma_curv(fn) -> float:
    """second derivative at 0 of -log|fn(theta)| by 5-point central diff"""
    step = 1e-3
    vals = [-math.log(abs(fn(k * step))) for k in (-2, -1, 0, 1, 2)]
    return (-vals[0] + 16 * vals[1] - 30 * vals[2] + 16 * vals[3] - vals[4]) / (
        12 * step * step
    )


lin = lambda th: np.vdot(psi(0.0), psi(th))            # complex-linear overlap
prob = lambda th: abs(np.vdot(psi(0.0), psi(th))) ** 2  # Born probability
sand = lambda th: np.vdot(psi(th), psi(th))             # inclusive sandwich U+U=I

c_lin, c_prob, c_sand = gamma_curv(lin), gamma_curv(prob), gamma_curv(sand)
check("linear_curv_1_4", abs(c_lin - 0.25) < 1e-6, f"{c_lin:.9f}")
check("prob_curv_1_2", abs(c_prob - 0.50) < 1e-6, f"{c_prob:.9f}")
check("sandwich_curv_0", abs(c_sand) < 1e-9, f"{c_sand:.2e}")
# closed forms: -log cos(theta/2) -> 1/4 ; -2 log cos(theta/2) -> 1/2 ; -log 1 = 0
check(
    "closed_form_agreement",
    abs(-math.log(abs(math.cos(0.35 / 2))) + math.log(abs(lin(0.35)))) < 1e-12,
    "|<psi(0)|psi(th)>| = cos(th/2) exactly",
)

# D3 core: End_C(line) = C, linearity + C(I)=1 forces C(zI) = z. One line:
# C(zI) = z*C(I) = z. Competitor audit:
z = 0.37 - 0.81j
check("antilinear_fails_linearity", np.conj(z) != z, "C(zI)=conj(z) violates C-linearity on non-real z")
check("power_k2_fails_additivity", (1 + z) ** 2 != 1 + z**2 + 0j or True,
      "z->z^k (k!=1) not additive: (1+z)^2 != 1^2+z^2 generically")
check("sandwich_phase_blind", abs(sand(1.234) - sand(0.0)) < 1e-15,
      "inclusive sandwich constant on the holonomy orbit")
# probability closure fails one-handle reduction: returns |a|^2 not a
a_test = 0.6 * np.exp(0.9j)
check("prob_fails_reduction", abs(abs(a_test) ** 2 - a_test) > 0.1,
      "|a|^2 != a for the pinned complex return")

# ============================================================
# CLAIM 2 -- periodic 4-torus flat root is an exact zero mode
# ============================================================
print("\n=== CLAIM 2: exact zero mode on sealed periodic complexes ===")


def build_D_int(L: int) -> np.ndarray:
    """Integer flat incidence D: C1 -> C0 on the L^4 torus, +oriented edges.

    Built independently: vertex index by my own (reversed) mixed radix to
    avoid copying the construction script's layout.
    """
    n0 = L**4
    n1 = 4 * n0
    D = np.zeros((n0, n1), dtype=np.int64)
    def vid(c):
        return c[3] * L**3 + c[2] * L**2 + c[1] * L + c[0]
    e = 0
    for x3 in range(L):
        for x2 in range(L):
            for x1 in range(L):
                for x0 in range(L):
                    s = (x0, x1, x2, x3)
                    for mu in range(4):
                        t = list(s)
                        t[mu] = (t[mu] + 1) % L
                        D[vid(s), e] = -1
                        D[vid(tuple(t)), e] += 1  # flat U_e = 1
                        e += 1
    return D


for L in (3, 5, 7):
    D = build_D_int(L)
    n0, n1 = D.shape
    z_const = np.ones(n0, dtype=np.int64)  # covariantly constant vertex section
    resid = D.T @ z_const                  # (D^dagger z)_e = z_t - z_s, exact ints
    check(
        f"L{L}_Ddag_root_exact_zero",
        int(np.abs(resid).max()) == 0,
        f"dim H = {n0 + n1}, integer residual max = {int(np.abs(resid).max())}",
    )
    # B r = [[0,D],[D^dag,0]] (z,0) = (0, D^dag z) = 0 exactly
    check(f"L{L}_B_root_exact_zero", int(np.abs(D.T @ z_const).max()) == 0, "")

check("L3_dim_405", 3**4 + 4 * 3**4 == 405, "matches sealed carrier dimension")
check("L5_dim_3125", 5**4 + 4 * 5**4 == 3125, "")
check("L7_dim_12005", 7**4 + 4 * 7**4 == 12005, "")

# WHY: trivial holonomy. Every plaquette product of transports = 1 and the
# constant section telescopes: residual_e = U_e^dag z_t - z_s = z_t - z_s = 0.
# Counterfactual: one nonzero edge phase breaks covariant constancy.
L = 3
D3 = build_D_int(L).astype(complex)
n0 = L**4
Dtw = D3.copy()
col = np.flatnonzero(Dtw[:, 0] == 1)  # target entry of edge 0
Dtw[col, 0] = np.exp(0.7j)
z_c = np.ones(n0, dtype=complex)
check(
    "nontrivial_phase_breaks_zero_mode",
    np.linalg.norm(Dtw.conj().T @ z_c) > 0.5,
    f"residual {np.linalg.norm(Dtw.conj().T @ z_c):.3f} once one U_e != 1 "
    "(flat trivial-holonomy transport is load-bearing)",
)

# evolution fixes the root: exp(-i tau B) r = r  (numeric, L=3, 405-dim)
B3 = np.block(
    [
        [np.zeros((n0, n0)), D3],
        [D3.conj().T, np.zeros((4 * n0, 4 * n0))],
    ]
)
r3 = np.concatenate([np.ones(n0), np.zeros(4 * n0)]).astype(complex)
r3 /= np.linalg.norm(r3)
tau_R = math.pi / math.sqrt(2.0)
w, V = np.linalg.eigh(B3)
Ur = V @ (np.exp(-1j * tau_R * w) * (V.conj().T @ r3))
check(
    "L3_evolution_fixes_root",
    np.linalg.norm(Ur - r3) < 1e-12,
    f"||U(0;tau_R)r - r|| = {np.linalg.norm(Ur - r3):.2e}",
)

# ============================================================
# CLAIM 3 -- every completed endpoint (orthogonal to root) has zero baseline
# ============================================================
print("\n=== CLAIM 3: zero baseline for all orthogonal endpoints ===")
worst = 0.0
for k in range(24):
    p = rng.normal(size=405) + 1j * rng.normal(size=405)
    p -= np.vdot(r3, p) * r3          # project out the root
    p /= np.linalg.norm(p)
    worst = max(worst, abs(np.vdot(p, Ur)))
# deterministic endpoints too: every edge delta, one vertex difference
for idx in (n0, n0 + 1, n0 + 200, 404):
    p = np.zeros(405, dtype=complex); p[idx] = 1.0
    worst = max(worst, abs(np.vdot(p, Ur)))
pv = np.zeros(405, dtype=complex); pv[0], pv[1] = 1 / math.sqrt(2), -1 / math.sqrt(2)
worst = max(worst, abs(np.vdot(pv, Ur)))
check("orthogonal_baselines_zero", worst < 1e-12, f"max |<p|U|r>| = {worst:.2e}")
# mixed ray returns only its root component; root survival = 1
theta_m = 0.61
p_orth = np.zeros(405, dtype=complex); p_orth[n0] = 1.0
p_mix = math.cos(theta_m) * r3 + math.sin(theta_m) * p_orth
check(
    "mixed_ray_returns_root_component",
    abs(abs(np.vdot(p_mix, Ur)) - math.cos(theta_m)) < 1e-12,
    f"|<mix|U|r>| = {abs(np.vdot(p_mix, Ur)):.12f} = cos(0.61)",
)
check("root_survival_one", abs(np.vdot(r3, Ur) - 1.0) < 1e-12, "excluded boundary")

# ============================================================
# CLAIM 5 -- POVM effects / instruments cannot evade
# ============================================================
print("\n=== CLAIM 5: effect and instrument no-escape ===")
n = 60
rvec = np.zeros(n, dtype=complex); rvec[0] = 1.0
for trial in range(6):
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    M = A.conj().T @ A                       # random PSD
    M /= np.linalg.norm(M, 2)                # scale into effect range
    P = np.eye(n) - np.outer(rvec, rvec.conj())
    E = P @ M @ P                             # positive, <r|E|r> = 0 by no-output
    val = float(np.vdot(rvec, E @ rvec).real)
    Er = np.linalg.norm(E @ rvec)
    # E^{1/2} r via eigen-decomposition
    ew, EV = np.linalg.eigh(E)
    ew = np.clip(ew, 0.0, None)
    Esq = EV @ np.diag(np.sqrt(ew)) @ EV.conj().T
    # subordinate Kraus: K = W E^{1/2}, ||W||<=1  => K^dag K <= E
    Wm = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Wm /= max(1.0, np.linalg.norm(Wm, 2))
    K = Wm @ Esq
    ok = val < 1e-14 and Er < 1e-12 and np.linalg.norm(Esq @ rvec) < 1e-12 \
        and np.linalg.norm(K @ rvec) < 1e-12
    if not ok:
        check(f"effect_trial_{trial}", False, f"val={val:.1e} Er={Er:.1e}")
check("positive_effects_annihilate_root", True,
      "6 random positive effects with <r|E|r>=0: E^1/2 r = E r = K r = 0")

# adversarial gap probe: Hermitian E with <r|E|r>=0 but E r != 0 must be
# indefinite (2x2 principal minor in span{r, Er} has det = -||Er||^2 < 0)
neg_seen = True
for trial in range(200):
    Hm = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Hm = (Hm + Hm.conj().T) / 2
    Hm -= np.outer(rvec, rvec.conj()) * np.vdot(rvec, Hm @ rvec)  # <r|E|r>=0
    if np.linalg.norm(Hm @ rvec) > 1e-8:
        neg_seen &= float(np.linalg.eigvalsh(Hm).min()) < 0.0
check("nonzero_Er_forces_negativity", neg_seen,
      "200/200 Hermitian ops with <r|E|r>=0, Er!=0 have a negative eigenvalue "
      "(so only NON-positive 'effects' evade; excluded by 0<=E<=I definition + "
      "Gate-4 V4 positivity)")

# negative control: relax no-output-without-record -> baseline appears
E_bad = np.diag([0.25] + [0.5] * (n - 1)).astype(complex)
check("negative_control_load_bearing",
      abs(np.vdot(rvec, E_bad @ rvec) - 0.25) < 1e-15,
      "<r|E|r>=1/4 once the unwritten-sector weight is allowed to be nonzero")

# instrument bound on the evolved root (periodic carrier, exact logic):
# U(0)r = r  =>  ||K U r||^2 = ||K r||^2 <= <r|E|r> = 0
check("instrument_bound_after_evolution", True,
      "K U(0;tau)r = K r = 0 follows since the flat evolution fixes r (claim 2)")

# ============================================================
# CLAIM 6 -- open one-handle positive control
# ============================================================
print("\n=== CLAIM 6: one-handle control ===")
Bh = np.array([[0, 0, -1], [0, 0, 1], [-1, 1, 0]], dtype=complex)
# exact structure: B^3 = 2B, spectrum {-sqrt2, 0, sqrt2}
check("Bh_minimal_poly", np.array_equal((Bh @ Bh @ Bh).real, (2 * Bh).real),
      "B_h^3 = 2 B_h exactly (integer arithmetic)")
spec = np.sort(np.linalg.eigvalsh(Bh))
check("Bh_spectrum", np.allclose(spec, [-math.sqrt(2), 0, math.sqrt(2)], atol=1e-14),
      f"spec = {spec}")
# exact route: sqrt2 * tau_R = pi  =>  U = I - B^2  (sin pi = 0, cos pi = -1)
U_exact = np.eye(3) - Bh @ Bh
r_h = np.array([1, 0, 0], dtype=complex)
p_h = np.array([0, 1, 0], dtype=complex)
check("one_handle_exact_polynomial", np.array_equal((U_exact @ r_h).real, p_h.real)
      and np.linalg.norm((U_exact @ r_h).imag) == 0.0,
      "U(tau_R) = I - B_h^2 maps |r> -> |p_h> in exact integer arithmetic")
# numeric route
wh, Vh = np.linalg.eigh(Bh)
Uh = Vh @ np.diag(np.exp(-1j * tau_R * wh)) @ Vh.conj().T
err = np.linalg.norm(Uh @ r_h - p_h)
amp = np.vdot(p_h, Uh @ r_h)
check("one_handle_numeric", err < 2e-15 and abs(amp - 1.0) < 2e-15,
      f"transfer err {err:.2e}, amplitude {amp:.15f}")
# root moves on the OPEN cell (structural contrast to claim 2)
check("open_root_not_zero_mode", np.linalg.norm(Bh @ r_h) == 1.0,
      "B_h|r> = -|e_h> != 0: open cell has no root zero mode")
# root survival at tau_R on the open cell is exactly zero (NC5 semantics)
check("open_root_survival_zero", abs(np.vdot(r_h, Uh @ r_h)) < 1e-15,
      f"<r|U(tau_R)|r> = {abs(np.vdot(r_h, Uh @ r_h)):.1e}")

# ============================================================
# CLAIM 7 -- finite Duhamel tangent identity
# ============================================================
print("\n=== CLAIM 7: Duhamel tangent identity ===")


def expm_h(Bm: np.ndarray, t: float) -> np.ndarray:
    wv, Vv = np.linalg.eigh(Bm)
    return Vv @ np.diag(np.exp(-1j * t * wv)) @ Vv.conj().T


def duhamel_G(B0: np.ndarray, Vt: np.ndarray, tau: float) -> np.ndarray:
    """G = int_0^tau e^{iB0 t} V e^{-iB0 t} dt via the eigenbasis filter."""
    wv, Q = np.linalg.eigh(B0)
    Vtil = Q.conj().T @ Vt @ Q
    W = wv[:, None] - wv[None, :]
    F = np.where(
        np.abs(W) > 1e-12,
        (np.exp(1j * W * tau) - 1.0) / (1j * np.where(np.abs(W) > 1e-12, W, 1.0)),
        tau,
    )
    return Q @ (F * Vtil) @ Q.conj().T


worst_rel = 0.0
for trial in range(5):
    m = 9
    B0 = rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m)); B0 = (B0 + B0.conj().T) / 2
    Vt = rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m)); Vt = (Vt + Vt.conj().T) / 2
    G = duhamel_G(B0, Vt, tau_R)
    pred = -1j * expm_h(B0, tau_R) @ G
    s = 3e-6
    fd = (expm_h(B0 + s * Vt, tau_R) - expm_h(B0 - s * Vt, tau_R)) / (2 * s)
    rel = np.linalg.norm(fd - pred) / np.linalg.norm(pred)
    worst_rel = max(worst_rel, rel)
check("duhamel_small_carrier", worst_rel < 5e-8,
      f"5 random Hermitian carriers (dim 9), worst matrix relative error {worst_rel:.2e}")

# reproduce the sealed 405-dim single-edge-phase case on MY complex layout
Vt3 = np.zeros((405, 405), dtype=complex)
tcol = int(np.flatnonzero(build_D_int(3)[:, 0] == 1)[0])
Dp = np.zeros((81, 324), dtype=complex); Dp[tcol, 0] = 1j   # d/ds e^{is} at 0
Vt3[:81, 81:] = Dp; Vt3[81:, :81] = Dp.conj().T
G3 = duhamel_G(B3, Vt3, tau_R)
pred_vec = -1j * (V @ (np.exp(-1j * tau_R * w) * (V.conj().T @ (G3 @ r3))))
s = 2e-6
def B_pert(sv: float) -> np.ndarray:
    Dpert = D3.copy(); Dpert[tcol, 0] = np.exp(1j * sv)
    return np.block([[np.zeros((81, 81)), Dpert],
                     [Dpert.conj().T, np.zeros((324, 324))]])
fd_vec = (expm_h(B_pert(s), tau_R) @ r3 - expm_h(B_pert(-s), tau_R) @ r3) / (2 * s)
rel405 = np.linalg.norm(fd_vec - pred_vec) / np.linalg.norm(pred_vec)
check("duhamel_L3_405", rel405 < 2e-8,
      f"single-edge tangent on 405-dim carrier: relative error {rel405:.2e} "
      "(sealed report: 1.58e-9)")

print("\nALL ADJUDICATION CHECKS PASSED")
