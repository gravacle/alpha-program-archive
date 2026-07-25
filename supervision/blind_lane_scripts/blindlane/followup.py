#!/usr/bin/env python3
"""Follow-up checks: rest-endpoint angle-defect scaling, MC seed robustness, P2 ratios."""
import numpy as np

I3 = np.eye(3); I4 = np.eye(4)
sx = np.array([[0,1],[1,0]], complex); I2 = np.eye(2); Z2 = np.zeros((2,2), complex)
def blk(a,b,c,d): return np.block([[a,b],[c,d]])
g0 = blk(I2,Z2,Z2,-I2); g1 = blk(Z2,sx,-sx,Z2); g5 = blk(Z2,I2,I2,Z2)
a1 = g0@g1; Sn = -1j*(g0@g5)
Gam = np.diag([1.,1.,-1.]).astype(complex)
b = np.array([[0,0,-1],[0,0,1],[-1,1,0]], complex); c = 1j*(Gam@b)
tau = np.pi/np.sqrt(2)

def kron(*Ms):
    out = Ms[0]
    for M in Ms[1:]: out = np.kron(out, M)
    return out
P0 = np.zeros((3,3)); P0[0,0]=1
P1s = np.zeros((3,3)); P1s[1,1]=1
chi = np.array([1,0,1j,0], complex)/np.sqrt(2)
er = np.array([1,0,0], complex); ep = np.array([0,1,0], complex)
def env(s):
    if s<=0 or s>=1: return 0.0
    return tau*32*min(s,1-s)**3
def expmi(H,s):
    w,V = np.linalg.eigh(H); return (V*np.exp(-1j*w*s))@V.conj().T
def evolve(Hf,t0,t1,N,dim):
    ns = int(round((t1-t0)*N)); dt = (t1-t0)/ns
    U = np.eye(dim, dtype=complex)
    for k in range(ns): U = expmi(Hf(t0+(k+0.5)*dt), dt)@U
    return U

# rest endpoint: midpoint-quadrature angle defect prediction eps = pi*2*h^2
V1 = kron(P0, Sn, c, I3); psi0 = kron(np.array([1,0,0],complex), chi, er, er)
Pp1 = kron(np.eye(12), np.outer(ep,ep.conj()), I3)
print("rest endpoint, h0=0: P1 defect vs N (predict defect ~ eps^2/2, eps = 2*pi*h^2):")
prev=None
for N in (24,48,96,192):
    U = evolve(lambda t: env(t)*V1, 0,1,N,108)
    P1 = float(np.vdot(U@psi0, Pp1@(U@psi0)).real)
    d = 1-P1; epsp = np.pi*2*(1/N)**2
    print(f"  N={N:3d}: 1-P1 = {d:.6e}  predicted eps^2/2 = {epsp**2/2:.6e}  ratio_prev = "
          f"{(prev/d if prev else float('nan')):.2f}")
    prev = d
# exact-integral rest check: replace Riemann angle by exact tau (single kick)
Uex = expmi(tau*np.kron(np.kron(P0,Sn),np.kron(c,I3)), 1.0)
P1ex = float(np.vdot(Uex@psi0, Pp1@(Uex@psi0)).real)
print(f"  exact accumulated angle (single exp of tau*V1): 1-P1 = {1-P1ex:.3e}  (endpoint exact)")

# MC seeds
for seed in (1,2,3):
    rng = np.random.default_rng(seed)
    n = 4_000_000
    t = rng.uniform(0,1,n); x = rng.uniform(-0.5,0.5,(n,3))
    acc = ((x**2).sum(1) <= np.minimum(t,1-t)**2)
    ts = np.sort(t[acc]); na = ts.size
    W = np.where(ts<=0.5, 8*ts**4, 1-8*(1-ts)**4)
    ks = np.abs(W - np.arange(1,na+1)/na).max()
    print(f"MC pushforward seed={seed}: n_acc={na} KS={ks:.5f} thr95={1.36/np.sqrt(na):.5f} pass={ks<1.36/np.sqrt(na)}")

# P2 convergence ratio (open BC)
Dop = np.array([[0,1,0],[-1,0,1],[0,-1,0]], complex)/2
H0F = kron(np.kron(-1j*Dop, a1), I3, I3)
V2 = kron(P1s, Sn, I3, c)
Pp2 = kron(np.eye(12), I3, np.outer(ep,ep.conj()))
HA = lambda t: H0F + env(t)*V1 + env(t-1)*V2
p2 = {}
p1 = {}
for N in (24,48,96):
    U = evolve(HA,0,2,N,108); psi = U@psi0
    p2[N] = float(np.vdot(psi,Pp2@psi).real); p1[N] = float(np.vdot(psi,Pp1@psi).real)
print(f"P2 ratios (open): (24-48)/(48-96) = {(p2[24]-p2[48])/(p2[48]-p2[96]):.3f}")
print(f"P1 Richardson (open, from 48/96 assuming h^2): {p1[96]+(p1[96]-p1[48])/3:.10f}")
print(f"P2 Richardson (open): {p2[96]+(p2[96]-p2[48])/3:.10f}")
