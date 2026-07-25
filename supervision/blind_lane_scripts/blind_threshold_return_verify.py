"""Blind verification lane: R3.4 Lorentzian Threshold-Return SPEC V001.

Rebuilt from spec text only. numpy only.

Conventions (documented):
- Dirac basis: gamma^0 = diag(1,1,-1,-1); gamma^j = [[0, sigma_j], [-sigma_j, 0]];
  gamma^5 = [[0, I2], [I2, 0]].  alpha_D^j = gamma^0 gamma^j.
- S = -i gamma^0 gamma^5.
- c_partial = [[0,0,-i],[0,0,+i],[+i,-i,0]]  (from CHARGED_INCIDENCE spec v002).
- mu = tau_R / T_R = pi/sqrt(2)  (from JOINT_ENDPOINT spec v001, T_R = 1).
- H(p) = alpha . p (x) I3 + mu * (S (x) c_partial)   acting on C4 (x) C3.
- Momentum-space Gaussian: g(p) = pi^(-3/4) * exp(-p^2/2)   (sigma = 1 in the
  convention g ~ exp(-p^2/(2 sigma^2)); ||Psi||_{L2(R^3)} = 1 with d^3p measure).
- Fixed internal vector: chi = u (x) v,
  u = (1, 0, i, 0)/sqrt(2)   (S-eigenvector, eigenvalue +1),
  v = (2, 1, i)/sqrt(6)      (populates all three record bands, <c_partial> != 0).
"""
import numpy as np

np.set_printoptions(precision=12, suppress=False)

I2 = np.eye(2, dtype=complex)
I3 = np.eye(3, dtype=complex)
I4 = np.eye(4, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)

g0 = np.block([[I2, Z2], [Z2, -I2]])
g1 = np.block([[Z2, sx], [-sx, Z2]])
g2 = np.block([[Z2, sy], [-sy, Z2]])
g3 = np.block([[Z2, sz], [-sz, Z2]])
g5 = np.block([[Z2, I2], [I2, Z2]])

alpha = [g0 @ g1, g0 @ g2, g0 @ g3]          # alpha_D^j
S = -1j * (g0 @ g5)

c_partial = np.array([[0, 0, -1j],
                      [0, 0, +1j],
                      [+1j, -1j, 0]], dtype=complex)

mu = np.pi / np.sqrt(2.0)

report = {}

# ---------------------------------------------------------------- (1) ALGEBRA
alg = {}
alg["S_hermitian"] = np.max(np.abs(S - S.conj().T))
alg["S2_minus_I"] = np.max(np.abs(S @ S - I4))
alg["anticomm_alpha_S"] = [np.max(np.abs(a @ S + S @ a)) for a in alpha]
alg["alpha_hermitian"] = [np.max(np.abs(a - a.conj().T)) for a in alpha]
# alpha anticommutation among themselves (needed for (alpha.p)^2 = |p|^2)
ac = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        ac[i, j] = np.max(np.abs(alpha[i] @ alpha[j] + alpha[j] @ alpha[i]
                                 - 2 * (i == j) * I4))
alg["alpha_clifford"] = ac.max()

alg["c_hermitian"] = np.max(np.abs(c_partial - c_partial.conj().T))
evals_c, evecs_c = np.linalg.eigh(c_partial)
alg["spec_c"] = evals_c            # expect {-sqrt2, 0, +sqrt2}
alg["spec_c_err"] = np.max(np.abs(np.sort(evals_c)
                                  - np.array([-np.sqrt(2), 0, np.sqrt(2)])))

# record eigenprojectors P_lambda (3x3), Q_lambda = I4 (x) P_lambda (12x12)
lams = [-np.sqrt(2.0), 0.0, +np.sqrt(2.0)]
P = {}
for lam in lams:
    cols = [evecs_c[:, k] for k in range(3) if abs(evals_c[k] - lam) < 1e-9]
    M = np.stack(cols, axis=1)
    P[lam] = M @ M.conj().T
alg["P_completeness"] = np.max(np.abs(sum(P.values()) - I3))

def H_of(p):  # p: 3-vector
    return (p[0] * np.kron(alpha[0], I3) + p[1] * np.kron(alpha[1], I3)
            + p[2] * np.kron(alpha[2], I3) + mu * np.kron(S, c_partial))

rng = np.random.default_rng(12345)
worst_block = 0.0
worst_commQ = 0.0
for _ in range(20):
    p = rng.normal(size=3)
    H = H_of(p)
    p2 = float(p @ p)
    for lam in lams:
        Q = np.kron(I4, P[lam])
        worst_commQ = max(worst_commQ, np.max(np.abs(H @ Q - Q @ H)))
        # H^2 restricted to eigenspace = (|p|^2 + mu^2 lam^2) * Q
        worst_block = max(worst_block,
                          np.max(np.abs((H @ H) @ Q - (p2 + mu**2 * lam**2) * Q)))
alg["H2_band_dispersion_err"] = worst_block
alg["H_commutes_Q_err"] = worst_commQ

# flat-band check: E_lambda(p) = sqrt(p^2 + mu^2 lam^2) depends on |p| for all lam
alg["flat_band"] = all(
    abs(np.sqrt(1.0 + mu**2 * l**2) - np.sqrt(0.0 + mu**2 * l**2)) > 1e-12
    for l in lams) is False  # True would mean a flat band exists; expect False
# more directly: dE/dp = p/E > 0 for p>0 on every band -> no flat band.

report["algebra"] = alg

# --------------------------------------------------- (2) projector structure
# Pi_(lambda,sigma)(p) = Q_lambda (I + sigma H_lambda/E_lambda)/2
def Pi(p, lam, sigma):
    Q = np.kron(I4, P[lam])
    E = np.sqrt(p @ p + mu**2 * lam**2)
    H = H_of(p)
    return Q @ (np.eye(12) + sigma * (H @ Q) / E) / 2.0

thm = {}
worst_idem = worst_herm = worst_comp = 0.0
for _ in range(10):
    p = rng.normal(size=3)
    tot = np.zeros((12, 12), dtype=complex)
    for lam in lams:
        for sg in (-1, +1):
            Pp = Pi(p, lam, sg)
            worst_idem = max(worst_idem, np.max(np.abs(Pp @ Pp - Pp)))
            worst_herm = max(worst_herm, np.max(np.abs(Pp - Pp.conj().T)))
            tot += Pp
    worst_comp = max(worst_comp, np.max(np.abs(tot - np.eye(12))))
thm["Pi_idempotent_err"] = worst_idem
thm["Pi_hermitian_err"] = worst_herm
thm["Pi_sum_identity_err"] = worst_comp
report["projectors"] = thm

# ------------------------------------------------------------ state choice
u = np.array([1, 0, 1j, 0], dtype=complex) / np.sqrt(2)
v = np.array([2, 1, 1j], dtype=complex) / np.sqrt(6)
chi = np.kron(u, v)
assert abs(np.linalg.norm(chi) - 1) < 1e-14

n_lam = {lam: float(np.real(chi.conj() @ np.kron(I4, P[lam]) @ chi)) for lam in lams}
s_lam = {lam: complex(chi.conj() @ np.kron(S, P[lam]) @ chi) for lam in lams}
report["band_weights_n"] = n_lam
report["band_S_weights_s"] = s_lam
report["u_S_expectation"] = complex(u.conj() @ S @ u)

# Gaussian radial profile, sigma = 1: g(p) = pi^{-3/4} exp(-p^2/2)
gnorm = np.pi ** (-0.75)
def g2(p):  # |g|^2
    return gnorm**2 * np.exp(-p**2)

# ------------------------------------- rho(E) checks: nonneg, L1, threshold
# E-grid per band with sqrt substitution near massive threshold
dens = {}
tot_mass = 0.0
neg_found = 0.0
for lam in lams:
    Eth = mu * abs(lam)
    # substitution E = sqrt(Eth^2 + x^2), x = p in fact (exact coarea inverse);
    # but evaluate rho on an explicit E-grid to confirm integrability directly.
    # use x = sqrt(E - Eth) smoothing on [Eth, Eth+1], then plain GL beyond.
    for (a, b, sub) in [(Eth, Eth + 1.0, True), (Eth + 1.0, np.sqrt(64 + Eth**2), False)]:
        xs, ws = np.polynomial.legendre.leggauss(400)
        if sub:
            xa, xb = 0.0, np.sqrt(b - a)
            x = (xb - xa) / 2 * xs + (xb + xa) / 2
            E = a + x**2
            jac = 2 * x * (xb - xa) / 2
        else:
            E = (b - a) / 2 * xs + (b + a) / 2
            jac = np.full_like(E, (b - a) / 2)
        pE = np.sqrt(np.maximum(E**2 - Eth**2, 0.0))
        for sg in (-1, +1):
            # angular integral of chi* Pi chi over S^2: odd alpha.p term drops,
            # = 4pi * (n_lam + sigma*mu*lam*Re(s_lam)/E)/2
            ang = 4 * np.pi * (n_lam[lam]
                               + sg * mu * lam * np.real(s_lam[lam]) / np.maximum(E, 1e-300)) / 2
            rho = E * pE * g2(pE) * ang
            neg_found = min(neg_found, rho.min())
            m = float(np.sum(ws * jac * rho))
            dens[(lam, sg)] = dens.get((lam, sg), 0.0) + m
            tot_mass += m
report["rho_min_value"] = neg_found          # expect >= 0 (up to quadrature eps)
report["rho_band_masses"] = {str(k): val for k, val in dens.items()}
report["rho_total_mass"] = tot_mass          # expect 1
# threshold behavior sample (massive band): rho ~ C*sqrt(E-Eth) -> 0, no atom
Ethm = mu * np.sqrt(2)
Es = Ethm + np.array([1e-2, 1e-4, 1e-6])
ps = np.sqrt(Es**2 - Ethm**2)
rho_th = Es * ps * g2(ps) * 4 * np.pi * n_lam[np.sqrt(2)] / 2
report["rho_near_threshold(massive,E-Eth=1e-2,1e-4,1e-6)"] = rho_th.tolist()

# ------------------------------------------------- (3) REGRESSION, method (a)
# radial spectral integration:
# A(t) = sum_lam \int_0^inf 4pi p^2 g2(p) [ n_lam cos(E t)
#                                  - i mu lam Re? s_lam sin(E t)/E ] dp
# (s_lam here is complex in general; the correct radial reduction is
#  chi* Q e^{-iHt} Q chi angular-averaged:
#  = cos(Et) n_lam - i sin(Et)/E * [ mu lam s_lam ]  since alpha.p averages out)
xs, ws = np.polynomial.legendre.leggauss(400)
pmax = 8.0
pg = pmax / 2 * xs + pmax / 2
wg = ws * pmax / 2

ts = [0.0, 1.0, 2.0, 4.0, 8.0]
A_a = []
for t in ts:
    acc = 0.0 + 0.0j
    for lam in lams:
        E = np.sqrt(pg**2 + mu**2 * lam**2)
        band = (np.cos(E * t) * n_lam[lam]
                - 1j * np.sin(E * t) / np.where(E == 0, 1.0, E) * (mu * lam * s_lam[lam]))
        acc += np.sum(wg * 4 * np.pi * pg**2 * g2(pg) * band)
    A_a.append(acc)

# ------------------------------------------------- (3) REGRESSION, method (b)
# direct 12x12 evolution, inversion-symmetric angular quadrature:
# Gauss-Legendre in cos(theta) (10 nodes, symmetric) x uniform phi (12 nodes)
nu, nphi = 10, 12
uu, wu = np.polynomial.legendre.leggauss(nu)
phis = 2 * np.pi * np.arange(nphi) / nphi
wphi = 2 * np.pi / nphi
dirs, wang = [], []
for k in range(nu):
    st = np.sqrt(1 - uu[k]**2)
    for ph in phis:
        dirs.append([st * np.cos(ph), st * np.sin(ph), uu[k]])
        wang.append(wu[k] * wphi)
dirs = np.array(dirs)          # (Nang,3), inversion symmetric set
wang = np.array(wang)
# verify inversion symmetry of the direction set
D = {tuple(np.round(d, 12)) for d in dirs}
inv_ok = all(tuple(np.round(-d, 12)) in D for d in dirs)
report["angular_grid_inversion_symmetric"] = inv_ok

# stack H over (radial x angular), eigendecompose once
nrad_b = 300
xb, wb = np.polynomial.legendre.leggauss(nrad_b)
pb = pmax / 2 * xb + pmax / 2
wpb = wb * pmax / 2

Hs = np.empty((nrad_b, len(dirs), 12, 12), dtype=complex)
A1 = np.kron(alpha[0], I3); A2 = np.kron(alpha[1], I3); A3 = np.kron(alpha[2], I3)
M = mu * np.kron(S, c_partial)
for i, p in enumerate(pb):
    for j, d in enumerate(dirs):
        Hs[i, j] = p * (d[0] * A1 + d[1] * A2 + d[2] * A3) + M
evals, evecs = np.linalg.eigh(Hs.reshape(-1, 12, 12))
proj = np.abs(np.einsum('nij,j->ni', evecs.conj().transpose(0, 2, 1), chi))**2  # |<e_k|chi>|^2
evals = evals.reshape(nrad_b, len(dirs), 12)
proj = proj.reshape(nrad_b, len(dirs), 12)

A_b = []
for t in ts:
    phase = np.exp(-1j * evals * t)
    ang_avg = np.einsum('ijk,ijk,j->i', phase, proj, wang)   # sum over dirs,k
    acc = np.sum(wpb * pb**2 * g2(pb) * ang_avg)
    A_b.append(acc)

report["t_values"] = ts
report["A_method_a_radial"] = [complex(z) for z in A_a]
report["A_method_b_direct"] = [complex(z) for z in A_b]
report["method_disagreement"] = [abs(a - b) for a, b in zip(A_a, A_b)]
report["abs_A_a"] = [abs(z) for z in A_a]

# ------------------------------------------ negative control: delta at p = 0
# H(0) = mu S (x) c_partial ; frequencies s*mu*lam, s in {-1,+1} (S-eigenvalue)
H0 = M
e0, V0 = np.linalg.eigh(H0)
w0 = np.abs(V0.conj().T @ chi)**2
report["delta_p0_frequencies"] = sorted(set(np.round(e0, 10)))
tt = np.linspace(0, 4, 4001)
A0 = np.array([np.sum(w0 * np.exp(-1j * e0 * t)) for t in tt])
# exact period: nonzero |frequencies| are sqrt(2)*mu = pi -> period 2*pi/pi = 2
report["delta_p0_A_at_t_0_1_2_3_4"] = [complex(np.sum(w0 * np.exp(-1j * e0 * t)))
                                       for t in [0, 1, 2, 3, 4]]
report["delta_p0_recurrence_|A(2)-A(0)|"] = abs(
    np.sum(w0 * np.exp(-1j * e0 * 2.0)) - np.sum(w0))
report["sqrt2_mu"] = np.sqrt(2) * mu   # expect pi
report["exact_period"] = 2 * np.pi / (np.sqrt(2) * mu)

for k, val in report.items():
    print(k, "=", val)
