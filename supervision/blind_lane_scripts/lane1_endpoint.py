import numpy as np

np.set_printoptions(precision=12, suppress=False)

# ---------- Dirac matrices, standard Dirac basis ----------
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)

g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
g1 = np.block([[Z2, sx], [-sx, Z2]]).astype(complex)
g2 = np.block([[Z2, sy], [-sy, Z2]]).astype(complex)
g3 = np.block([[Z2, sz], [-sz, Z2]]).astype(complex)
g5 = 1j * g0 @ g1 @ g2 @ g3          # = [[0,I],[I,0]]
alpha = [g0 @ g1, g0 @ g2, g0 @ g3]  # alpha_i = gamma0 gamma_i

# sanity on gamma5
assert np.allclose(g5, np.block([[Z2, I2], [I2, Z2]]))

# ---------- record generator c_partial (from V002 spec, basis |r>,|p>,|e>) ----------
c = np.array([[0, 0, -1j],
              [0, 0, +1j],
              [+1j, -1j, 0]], dtype=complex)
assert np.allclose(c, c.conj().T), "c_partial Hermitian"

r_vec = np.array([1, 0, 0], dtype=complex)
p_vec = np.array([0, 1, 0], dtype=complex)
e_vec = np.array([0, 0, 1], dtype=complex)
z_vec = (r_vec + p_vec) / np.sqrt(2)
m_vec = (r_vec - p_vec) / np.sqrt(2)
assert np.allclose(c @ z_vec, 0), "c z = 0"
assert np.allclose(c @ c @ m_vec, 2 * m_vec), "c^2 m = 2m"
assert np.allclose(c @ c @ e_vec, 2 * e_vec), "c^2 e = 2e"

# ---------- units ----------
T_R = 1.0
tau_R = np.pi / np.sqrt(2.0)
mu = tau_R / T_R                      # = pi/sqrt2 ; 2 mu^2 = pi^2
I4 = np.eye(4, dtype=complex)
I3 = np.eye(3, dtype=complex)
I12 = np.eye(12, dtype=complex)

def H_of_p(pmag, comp=0):
    """H(p) = alpha_x * p (x) I3  - i mu g0 g5 (x) c_partial ; 1-D tangential momentum
    along axis `comp` (default alpha_1 = g0 g1)."""
    return np.kron(alpha[comp] * pmag, I3) - 1j * mu * np.kron(g0 @ g5, c)

# ---- algebra checks: Hermiticity and frozen H^2 identity, exact structure ----
for pm in (0.0, 0.25, 0.5, 1.0, 2.0, 4.0, 0.7321):
    H = H_of_p(pm)
    assert np.allclose(H, H.conj().T), "H Hermitian"
    H2_expected = pm**2 * I12 + mu**2 * np.kron(I4, c @ c)
    assert np.allclose(H @ H, H2_expected, atol=1e-12), "H^2 = |p|^2 + mu^2 c^2"

# ---------- spin ray: momentum-eigen (eigenvector of alpha_1, eigenvalue +1) ----------
w, v = np.linalg.eigh(alpha[0])
chi = v[:, np.argmin(np.abs(w - 1.0))]   # alpha_1 chi = + chi
chi = chi / np.linalg.norm(chi)
assert np.allclose(alpha[0] @ chi, chi)

def U_eigh(H, t):
    lam, V = np.linalg.eigh(H)
    return V @ np.diag(np.exp(-1j * lam * t)) @ V.conj().T

def U_functional(pmag, t):
    """exp(-iHt) = cos(S t) - i H sin(S t)/S with S = sqrt(H^2):
    S = |p| on zero record sector (c z = 0), S = E(p) on massive sector."""
    H = H_of_p(pmag)
    E = np.sqrt(pmag**2 + 2 * mu**2)
    P0 = np.kron(I4, np.outer(z_vec, z_vec.conj()))
    Pm = np.kron(I4, np.outer(m_vec, m_vec.conj()) + np.outer(e_vec, e_vec.conj()))
    assert np.allclose(P0 + Pm, I12)
    cosS = np.cos(pmag * t) * P0 + np.cos(E * t) * Pm
    sfac0 = t if pmag == 0 else np.sin(pmag * t) / pmag   # sinc limit at p=0
    sinS_over_S = sfac0 * P0 + (np.sin(E * t) / E) * Pm
    return cosS - 1j * H @ sinS_over_S

def transfer_prob(pmag, t=T_R):
    H = H_of_p(pmag)
    U1 = U_eigh(H, t)
    U2 = U_functional(pmag, t)
    dev = np.max(np.abs(U1 - U2))
    psi0 = np.kron(chi, r_vec)
    psi_t = U1 @ psi0
    Ppointer = np.kron(I4, np.outer(p_vec, p_vec.conj()))
    prob_proj = np.real(psi_t.conj() @ Ppointer @ psi_t)   # any spin, pointer record
    amp_same_spin = np.kron(chi, p_vec).conj() @ psi_t     # same spin ray, pointer
    # closed-form from spec decomposition
    E = np.sqrt(pmag**2 + 2 * mu**2)
    A = 0.25 * ((np.cos(pmag * t) - np.cos(E * t))**2 +
                (np.sin(pmag * t) - pmag * np.sin(E * t) / E)**2)
    return prob_proj, abs(amp_same_spin)**2, A, dev

print("p      P_projector           P_samespin            P_closedform          |U1-U2|max")
results = {}
for pm in [0.0, 0.25, 0.5, 1.0, 2.0, 4.0]:
    pp, ps, pa, dev = transfer_prob(pm)
    results[pm] = pp
    print(f"{pm:5.2f}  {pp:.15f}  {ps:.15f}  {pa:.15f}  {dev:.3e}")

# p=0 exactness to machine precision
p0_err = abs(results[0.0] - 1.0)
U0 = U_eigh(H_of_p(0.0), T_R)
psi0 = np.kron(chi, r_vec)
exact_dev = np.linalg.norm(U0 @ psi0 - np.kron(chi, p_vec))  # state = chi (x) |p> exactly?
print("p=0: |P-1| =", p0_err, "  || U psi0 - chi(x)p || =", exact_dev)

# also p=0 exact for arbitrary spin rays (swap is spin-independent at p=0)
rng = np.random.default_rng(7)
worst = 0.0
for _ in range(20):
    x = rng.normal(size=4) + 1j * rng.normal(size=4)
    x /= np.linalg.norm(x)
    worst = max(worst, np.linalg.norm(U0 @ np.kron(x, r_vec) - np.kron(x, p_vec)))
print("p=0 arbitrary-spin worst deviation:", worst)

# ---------- Gaussian packet, width sigma = 0.7 (std of |amplitude|^2), centered p=0 ----------
sigma = 0.7
pg = np.linspace(-10 * sigma, 10 * sigma, 40001)
weight = np.exp(-pg**2 / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))
E = np.sqrt(pg**2 + 2 * mu**2)
Pp = 0.25 * ((np.cos(pg * T_R) - np.cos(E * T_R))**2 +
             (np.sin(np.abs(pg) * T_R) - np.abs(pg) * np.sin(E * T_R) / E)**2)
norm_check = np.trapezoid(weight, pg)
packet_prob = np.trapezoid(weight * Pp, pg)
print("packet weight norm:", norm_check)
print("packet transfer prob (sigma=0.7 in |amp|^2):", f"{packet_prob:.12f}")

# alt convention: sigma=0.7 is width of the AMPLITUDE gaussian -> |amp|^2 std = 0.7/sqrt2
sig2 = 0.7 / np.sqrt(2)
w2 = np.exp(-pg**2 / (2 * sig2**2)) / (sig2 * np.sqrt(2 * np.pi))
alt = np.trapezoid(w2 * Pp, pg)
print("alt convention (amplitude width 0.7):", f"{alt:.12f}")

# ---------- parity condition check ----------
# derived: A_p(t) = (1/2)[ e^{-i s|p| t} - cos(Et) + i s|p| sin(Et)/E ] on spin ray chi
# |A|=1 & no leakage  <=>  sin(Et)=0  (Et = n pi)  and  e^{-i|p|t} = -cos(Et)
#                     <=>  |p| t = k pi  with  (-1)^k = -(-1)^n  i.e.  n+k odd
# p=0, t=T_R=1: E = sqrt(2)mu = pi -> n=1, k=0, n+k=1 odd -> exact. PASS.
E0 = np.sqrt(2) * mu
print("E(0)*T_R/pi =", E0 * T_R / np.pi, " |p|*T_R/pi = 0 -> n=1,k=0, n+k odd: PASS")

# generic p: need E t = n pi AND |p| t = k pi -> E/|p| = n/k rational.
# E/|p| = sqrt(1 + pi^2/p^2); rational only on a measure-zero set of p. Demo:
for pm in [0.25, 0.5, 1.0, 2.0, 4.0]:
    ratio = np.sqrt(pm**2 + np.pi**2) / pm
    print(f"p={pm}: E/|p| = {ratio:.12f}")
