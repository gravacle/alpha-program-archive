"""Independent verification of R3.4 shared-source causal parent result numbers.

Built from the SPEC alone (not the result file's numbers): 3-cell chain,
vertices e_0..e_3 in R^4, d_j = e_{j+1}-e_j, P_j = |d_j><d_j|/2,
B_j = P_j (x) gamma5 (x) c_j acting on its own 3-dim record factor R_j.
"""
import numpy as np

I4v = np.eye(4)          # source vertex space
d = [I4v[j+1] - I4v[j] for j in range(3)]
P = [np.outer(v, v) / 2 for v in d]

g5 = np.diag([1.0, 1.0, -1.0, -1.0])   # gamma^5 (Dirac basis)
c = np.array([[0, 0, -1j],
              [0, 0, +1j],
              [+1j, -1j, 0]])          # record generator on span{r,p,e}
I3 = np.eye(3)

def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = np.kron(out, m)
    return out

def B(j):
    recs = [c if k == j else I3 for k in range(3)]
    return kron(P[j], g5, *recs)

B0, B1, B2 = B(0), B(1), B(2)
fro = lambda M: np.linalg.norm(M, 'fro')

print("Tr(P0P1) =", np.trace(P[0] @ P[1]).real)
print("Tr(P1P2) =", np.trace(P[1] @ P[2]).real)
print("Tr(P0P2) =", np.trace(P[0] @ P[2]).real)
print("||[B0,B1]||_F =", fro(B0 @ B1 - B1 @ B0), " (claim 8.48528137423857 = 6*sqrt2 =", 6*np.sqrt(2), ")")
print("||[B0,B2]||_F =", fro(B0 @ B2 - B2 @ B0))

tau = np.pi / np.sqrt(2)

def expmi(M, s):
    """exp(i s M) for Hermitian M via eigendecomposition."""
    w, V = np.linalg.eigh(M)
    return (V * np.exp(1j * s * w)) @ V.conj().T

U = [expmi(B(j), -tau) for j in range(3)]

# order sensitivity of the completed product
print("||U1U0 - U0U1||-type parent change:", fro((B0 + B1) - (B0 + B1)), "(H unchanged; order lives in the product)")
print("||W(0,1) - W(1,0)||_F =", fro(U[1] @ U[0] - U[0] @ U[1]))

# pointer persistence: source in-sector state x spin x ready records |r,r,r>
# in-sector: use d_0 direction (first cell active), spin up
psi_src = d[0] / np.sqrt(2)
spin = np.array([1.0, 0, 0, 0])
r = np.array([1.0, 0, 0])
psi = psi_src
for blk in (spin, r, r, r):
    psi = np.kron(psi, blk)

W1 = U[0] @ psi                      # after first write
W3 = U[2] @ U[1] @ U[0] @ psi        # after all three

def rec0_prob_p(state):
    # probability that record factor 0 reads |p> (index 1 of R_0)
    t = state.reshape(4, 4, 3, 3, 3)
    return float(np.sum(np.abs(t[:, :, 1, :, :]) ** 2))

p1, p3 = rec0_prob_p(W1), rec0_prob_p(W3)
print("P(record0=|p>) after write 1:", p1)
print("P(record0=|p>) after writes 2,3:", p3, " drift:", abs(p3 - p1))

# [B_k, O_j] = 0 for k>j, O_j on earlier record factor
O0 = kron(np.eye(4), np.eye(4), np.random.default_rng(7).normal(size=(3,3)), I3, I3)
print("||[B2, O_0]||_F =", fro(B2 @ O0 - O0 @ B2))

# reduced source+record0 state drift between event 1 and event 3
def rho_src_rec0(state):
    t = state.reshape(4, 4, 3, 3, 3)          # src, spin, R0, R1, R2
    t2 = np.transpose(t, (0, 2, 1, 3, 4)).reshape(12, 36)
    return t2 @ t2.conj().T
drift = np.linalg.norm(rho_src_rec0(W3) - rho_src_rec0(W1))
print("||rho_src+rec0(3) - rho_src+rec0(1)|| =", drift, " (claim 0.5303300858899105 = 3/(4*sqrt2) =", 3/(4*np.sqrt(2)), ")")

# negative control: stationary recurrence on isolated cell
u = expmi(np.kron(g5, c), -tau)
rp = np.kron(spin, r)
one = u @ rp
two = u @ one
print("recurrence ||U(2tau)|r> - |r>|| =", np.linalg.norm(two - rp))
