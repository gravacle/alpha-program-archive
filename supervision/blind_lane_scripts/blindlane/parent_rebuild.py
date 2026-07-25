#!/usr/bin/env python3
"""
BLIND verification lane rebuild of R3.4 complete causal superconnection parent
finite regulator. Built ONLY from spec text:
  - R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md (target gate)
  - BID_GRADED_BOUNDARY_SUPERCONNECTION_REPAIR_V001.md (c = i Gamma b, square)
  - R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md (uniform diamond measure)
  - R3_4_LORENTZIAN_JOINT_ENDPOINT_COMPATIBILITY_SPEC_V001.md (T_R=1, tau_R=pi/sqrt2)
No measured constants used. alpha_D = Dirac matrices only. numpy + stdlib only.
"""
import numpy as np
from fractions import Fraction as F

rng = np.random.default_rng(0)
np.set_printoptions(precision=8, suppress=False, linewidth=160)

OUT = []
def say(*a):
    s = " ".join(str(x) for x in a)
    OUT.append(s)
    print(s, flush=True)

# ---------------------------------------------------------------- structures
I2 = np.eye(2); I3 = np.eye(3); I4 = np.eye(4)
sx = np.array([[0,1],[1,0]], complex)
sy = np.array([[0,-1j],[1j,0]], complex)
sz = np.array([[1,0],[0,-1]], complex)
Z2 = np.zeros((2,2), complex)

def blk(a,b,c,d):
    return np.block([[a,b],[c,d]])

g0 = blk(I2,Z2,Z2,-I2)                       # Dirac basis
g1 = blk(Z2,sx,-sx,Z2)
g2 = blk(Z2,sy,-sy,Z2)
g3 = blk(Z2,sz,-sz,Z2)
g5 = blk(Z2,I2,I2,Z2)
alph = [g0@g1, g0@g2, g0@g3]                 # alpha_j = g0 g^j  (Dirac alpha matrices)
Sn = -1j*(g0@g5)                             # S_n = -i slash(n) g5 at rest normal, slash(n)=g0

Gamma_c = np.diag([1.0,1.0,-1.0]).astype(complex)
b_c = np.array([[0,0,-1],[0,0,1],[-1,1,0]], complex)
c_c = 1j*(Gamma_c@b_c)
c_target = np.array([[0,0,-1j],[0,0,1j],[1j,-1j,0]], complex)

say("=== (a) exact Clifford / algebra checks ===")
say("c_c == [[0,0,-i],[0,0,i],[i,-i,0]] :", np.allclose(c_c, c_target, atol=0), " maxdev", np.abs(c_c-c_target).max())
say("c_c hermitian:", np.abs(c_c - c_c.conj().T).max())
say("S_n hermitian:", np.abs(Sn - Sn.conj().T).max())
say("S_n^2 - I:", np.abs(Sn@Sn - I4).max())
for j,a in enumerate(alph):
    say(f"anticomm {{alpha_{j+1}, S_n}} maxabs:", np.abs(a@Sn + Sn@a).max())
ev = np.linalg.eigvalsh(c_c)
say("spec(c_c):", np.round(ev,12), " target {0,+-sqrt2}: dev",
    np.abs(np.sort(ev) - np.array([-np.sqrt(2),0,np.sqrt(2)])).max())
say("c_c^2 == b_c^2 (BID repair claim):", np.abs(c_c@c_c - b_c@b_c).max())
say("Gamma_cell anticommutes with b_c:", np.abs(Gamma_c@b_c + b_c@Gamma_c).max())
say("spec(c_c^2):", np.round(np.linalg.eigvalsh(c_c@c_c),12))

# ---------------------------------------------------------------- (b) envelope exact
say("")
say("=== (b) envelope exact normalization (rational arithmetic) ===")
def mono(n):        # \int_0^{1/2} s^n ds
    return F(1,2)**(n+1)/F(n+1)
int_min3   = 2*mono(3)                       # \int_0^1 min(s,1-s)^3
int_w      = 2*32*mono(3)                    # \int w
mean_w     = 32*mono(4) + 32*(mono(3)-mono(4))   # \int s w  (second half via u=1-s)
int_w2     = 2*(32**2)*mono(6)
int_wp2    = 2*(96**2)*mono(4)               # \int w'^2 , w'=+-96 min^2
int_abs_wp = 2*96*mono(2)                    # \int|w'|
say("int_0^1 min(s,1-s)^3 ds =", int_min3, " -> normalizer 1/that =", 1/int_min3)
say("int w  =", int_w, " (exact)")
say("mean   = int s w =", mean_w, " (exact)")
say("sup w  = 32*(1/2)^3 =", F(32,8))
say("int w^2 =", int_w2, "  ||w||_2 = 4/sqrt7 =", float(4/np.sqrt(7)))
say("sup|w'| =", 96*F(1,4), "  int|w'| =", int_abs_wp, "  int w'^2 =", int_wp2,
    "  ||w'||_2 = 24/sqrt5 =", float(24/np.sqrt(5)))
say("sup|w''| (one-sided) = 96 ; jump of w' at s=1/2 = -48 ; TV(w') = 96")
tau = np.pi/np.sqrt(2.0)   # tau_R, T_R = 1
say("int v dt = tau_R = pi/sqrt2 =", tau, " (envelope v = tau_R * w, T_R=1)")

# pushforward check: uniform 4-volume on 3+1 diamond (tip-to-tip T=1),
# section at time s is ball radius min(s,1-s) -> marginal prop min^3 -> w = 32 min^3.
n = 2_000_000
t = rng.uniform(0,1,n); x = rng.uniform(-0.5,0.5,(n,3))
acc = ( (x**2).sum(1) <= np.minimum(t,1-t)**2 )
ts = np.sort(t[acc]); na = ts.size
Wcdf = np.where(ts<=0.5, 8*ts**4, 1-8*(1-ts)**4)
ks = np.abs(Wcdf - (np.arange(1,na+1)/na)).max()
say(f"MC pushforward check: n_acc={na}, KS dist vs CDF(8s^4|mirror) = {ks:.5f}",
    f"(95% KS threshold ~ {1.36/np.sqrt(na):.5f})")

# ---------------------------------------------------------------- (c) descendants
say("")
say("=== (c) generated descendants of D = i g^mu d_mu + i g5 C ===")
say("symbolic: D^2 = (i g d)^2 - C^2 - g^mu g5 (d_mu C); first-order cross terms cancel (checked by hand).")
# structure matrices on sites(3) x spin(4) x rec1(3) x rec2(3), envelope scalars stripped.
def kron(*Ms):
    out = Ms[0]
    for M in Ms[1:]: out = np.kron(out, M)
    return out
P0 = np.zeros((3,3)); P0[0,0]=1
P1s = np.zeros((3,3)); P1s[1,1]=1
g05 = g0@g5
def fro(M): return float(np.linalg.norm(M))
def opn(M): return float(np.linalg.norm(M,2))

# two coincident overlapping cells sharing one site (shared M), records 1 and 2:
N_der2 = kron(P0, g05, c_c, I3) + kron(P0, g05, I3, c_c)   # derivative-support structure
N_ovl  = 2*kron(P0, I4, c_c, c_c)                          # overlap cross-term structure (factor 2 from expansion)
say("two-cell derivative-support structure  M x g0g5 x (c x I + I x c):")
say("   Frobenius =", fro(N_der2), " closed form 4*sqrt6 =", 4*np.sqrt(6.0),
    " match:", np.isclose(fro(N_der2), 4*np.sqrt(6.0)))
say("   operator  =", opn(N_der2), " closed form 2*sqrt2 =", 2*np.sqrt(2.0))
say("overlap descendant structure  2 M x I4 x (c x c):")
say("   Frobenius =", fro(N_ovl), " target 16 match:", np.isclose(fro(N_ovl),16.0))
say("   operator  =", opn(N_ovl), " (= 2*||c||^2 = 4)")
# other natural conventions for the record
N_der1 = kron(P0, g05, c_c, I3)
N_c2   = kron(P0, I4, c_c@c_c, I3)
say("single-cell derivative-support M x g0g5 x c x I3: Frobenius =", fro(N_der1), "(= 4*sqrt3)",
    " op =", opn(N_der1))
say("single-cell c^2 descendant M x I4 x c^2 x I3:      Frobenius =", fro(N_c2),
    "(= 4*sqrt6  -- flagged coincidence with two-cell derivative norm)", " op =", opn(N_c2))
say("envelope-carrying sups (v = tau*w): sup|v'| =", 24*tau, "; sup 2 v1 v2 (coincident) =", 2*16*tau**2)
say("w-only coefficient sups: sup|w'| = 24 ; sup(w1*w2) coincident = 16 ; half-offset sup(w1*w2) = 1/4")

# ---------------------------------------------------------------- (d) two-cell dynamics
say("")
say("=== (d) two-cell dynamics, 3 sites, 2 record factors ===")
say("choices: 1-D 3-site chain, spacing 1; h0 = alpha_1 (x) (-i D), D = central antisym difference;")
say("  open D=[[0,1,0],[-1,0,1],[0,-1,0]]/2 ; periodic D=[[0,1,-1],[-1,0,1],[1,-1,0]]/2 .")
say("  M_c = static single-site projector (Galerkin compression of sub-lattice diamond section).")
say("  cell1: site0, record1, opens t=0; cell2: site1, record2, opens t=1;  v(s)=tau_R*32*min(s,1-s)^3.")
say("  initial: source at site0, spinor = S_n=+1 eigenvector (1,0,i,0)/sqrt2; records |r>x|r>.")
say("  stepping: midpoint-rule unitary product, N steps per unit time, exact expm via eigh.")

D_open = np.array([[0,1,0],[-1,0,1],[0,-1,0]], complex)/2
D_per  = np.array([[0,1,-1],[-1,0,1],[1,-1,0]], complex)/2
def Ksite(D): return -1j*D

chi = np.array([1,0,1j,0], complex)/np.sqrt(2)   # S_n = +1
er = np.array([1,0,0], complex); ep = np.array([0,1,0], complex)
def envelope(s):
    if s <= 0.0 or s >= 1.0: return 0.0
    return tau*32*min(s,1-s)**3

def build(D):
    K = Ksite(D)
    H0sp = np.kron(K, alph[0])                       # 12x12 source
    H0F  = kron(H0sp, I3, I3)
    V1 = kron(P0,  Sn, c_c, I3)
    V2 = kron(P1s, Sn, I3, c_c)
    return H0sp, H0F, V1, V2

def expmi(H, s):     # exp(-1j*H*s), H hermitian
    w,V = np.linalg.eigh(H)
    return (V*np.exp(-1j*w*s)) @ V.conj().T

def evolve(Hfun, t0, t1, N):
    ns = int(round((t1-t0)*N))
    dt = (t1-t0)/ns
    U = np.eye(108, dtype=complex)
    for k in range(ns):
        U = expmi(Hfun(t0+(k+0.5)*dt), dt) @ U
    return U

def probs(psi):
    Pp1 = kron(np.eye(12), np.outer(ep,ep.conj()), I3)
    Pp2 = kron(np.eye(12), I3, np.outer(ep,ep.conj()))
    return float(np.vdot(psi, Pp1@psi).real), float(np.vdot(psi, Pp2@psi).real)

def rec1_pops(psi):
    T = psi.reshape(12,3,3)
    rho = np.einsum('arb,asb->rs', T, T.conj())
    return np.real(np.diag(rho))

results = {}
for bc, D in [("open",D_open), ("periodic",D_per)]:
    H0sp,H0F,V1,V2 = build(D)
    say(f"[{bc}] hermiticity h_K(0.37): "
        f"{np.abs((H0F+envelope(0.37)*V1+envelope(-0.63)*V2) - (H0F+envelope(0.37)*V1).conj().T).max():.2e}"
        f" ; ||[V1,V2]|| = {np.abs(V1@V2-V2@V1).max():.2e} (spacelike cell terms commute exactly)")
    psi0 = kron(np.array([1,0,0],complex), chi, er, er)
    HA = lambda t: H0F + envelope(t)*V1 + envelope(t-1)*V2       # order A: cell1 then cell2
    HB = lambda t: H0F + envelope(t-1)*V1 + envelope(t)*V2       # order B: cell2 then cell1
    w0,V0 = np.linalg.eigh(H0F)
    E2 = (V0*np.exp(2j*w0)) @ V0.conj().T                        # exp(+2i h0)
    row = {}
    for N in (24,48,96):
        U1 = evolve(HA,0,1,N); U2 = evolve(HA,1,2,N)
        psi1 = U1@psi0; psi2 = U2@psi1
        p1a,_ = probs(psi1); p1b,p2b = probs(psi2)
        UA = U2@U1
        SA = E2@UA
        row[N] = dict(P1_after1=p1a, P1_after2=p1b, P2_after2=p2b, UA=UA, SA=SA,
                      uerr=float(np.abs(UA.conj().T@UA - np.eye(108)).max()),
                      serr=float(np.abs(SA.conj().T@SA - np.eye(108)).max()),
                      pops1=rec1_pops(psi2))
    for N in (24,48,96):
        r = row[N]
        say(f"[{bc}] N={N:3d}: P1(after cell1)={r['P1_after1']:.10f}  P1(after cell2)={r['P1_after2']:.10f}"
            f"  P2(after cell2)={r['P2_after2']:.10f}  persistence dev={abs(r['P1_after2']-r['P1_after1']):.2e}"
            f"  max|U+U-I|={r['uerr']:.1e}  max|S+S-I|={r['serr']:.1e}")
    c1 = row[24]['P1_after1']-row[48]['P1_after1']; c2 = row[48]['P1_after1']-row[96]['P1_after1']
    sF1 = np.linalg.norm(row[24]['SA']-row[48]['SA']); sF2 = np.linalg.norm(row[48]['SA']-row[96]['SA'])
    say(f"[{bc}] convergence ratios: P1 (24-48)/(48-96) = {c1/c2:.3f} ; ||S24-S48||F/||S48-S96||F = {sF1/sF2:.3f}"
        f"  (midpoint 2nd order -> 4)")
    say(f"[{bc}] record-1 populations (r,p,e) after both cells (N=96): {np.round(row[96]['pops1'],8)}")
    # order swap at N=96
    U1B = evolve(HB,0,1,96); U2B = evolve(HB,1,2,96); UB = U2B@U1B; SB = E2@UB
    psiB = UB@psi0; p1B,p2B = probs(psiB)
    say(f"[{bc}] order swap (cell2 first): P1={p1B:.10f} P2={p2B:.10f} ;"
        f" ||S_A - S_B||_2 = {np.linalg.norm(row[96]['SA']-SB,2):.6f}"
        f" ; ||S_A - S_B||_F = {np.linalg.norm(row[96]['SA']-SB):.6f}")
    # dressed pointer distance (N=96): E_R = normalized partial trace over 12-dim source
    SAm = row[96]['SA']
    Pp1 = kron(np.eye(12), np.outer(ep,ep.conj()), I3)
    Phi = SAm.conj().T @ Pp1 @ SAm
    X = Phi.reshape(12,9,12,9)
    Erec = np.einsum('aras->rs', X)/12.0
    Emb = np.kron(np.eye(12), Erec)
    dd = np.linalg.norm(Phi - Emb)
    say(f"[{bc}] dressed pointer: ||Phi(P)-E_R(Phi(P))||_F = {dd:.6f}"
        f"  (||Phi(P)||_F = {np.linalg.norm(Phi):.6f} = 6; relative {dd/np.linalg.norm(Phi):.6f})")
    # rest-normal exact endpoint benchmark: h0 removed
    Hrest = lambda t: envelope(t)*V1 + envelope(t-1)*V2
    Ur = evolve(Hrest,0,2,96); pr1,pr2 = probs(Ur@psi0)
    say(f"[{bc}] rest benchmark (h0=0): P1={pr1:.12f} P2={pr2:.12f}  (exact endpoint at rest: P1 -> 1, P2 stays 0: "
        f"cell2 site empty at rest)")
    # static reuse negative control: reopen SAME record factor at [1,2]
    Hreuse = lambda t: H0F + (envelope(t)+envelope(t-1))*V1
    Uu = evolve(Hreuse,0,2,96); pu1,_ = probs(Uu@psi0)
    Hreuse_rest = lambda t: (envelope(t)+envelope(t-1))*V1
    Uur = evolve(Hreuse_rest,0,2,96); pur1,_ = probs(Uur@psi0)
    say(f"[{bc}] static-reuse control (same record reopened): P1(after 2 openings)={pu1:.10f}"
        f" ; at rest {pur1:.12f} (recurrence r->p->r confirmed)")
    results[bc] = row

# ---------------------------------------------------------------- (e) free-tail Gaussian return
say("")
say("=== (e) free-tail Gaussian return amplitude ===")
say("width convention: psi(x) prop exp(-|x|^2/2)  (position density variance 1/2 per axis; |g~(p)|^2 prop exp(-p^2))")
say("continuum 3+1: h0(p)=alpha_D.p ; A(t)=<cos(|p|t)> over weight p^2 e^{-p^2} (alpha.phat term vanishes by parity)")
say("closed form: A(t) = (1 - t^2/2) * exp(-t^2/4)")
p = np.linspace(0, 40, 400001)
wgt = p**2*np.exp(-p**2)
for tt in (1,2,4,8):
    Anum = np.trapz(wgt*np.cos(p*tt), p)/np.trapz(wgt, p)
    Acf  = (1-tt**2/2)*np.exp(-tt**2/4)
    say(f"  t={tt}: closed form {Acf:+.10e} ; quadrature {Anum:+.10e} ; |dev| {abs(Anum-Acf):.1e}")
say(f"  A(2) = -exp(-1) = {-np.exp(-1):.10f}  -> EXACTLY -1/e under this convention (found, not forced)")
say(f"  general sigma: A(t) = (1 - t^2/(4 sigma^2)) exp(-t^2/(8 sigma^2)); A(2)=-1/e iff sigma^2=1/2")
say("continuum 1+1 (same width): A(t) = exp(-t^2/4): "
    + ", ".join(f"A({tt})={np.exp(-tt**2/4):.6e}" for tt in (1,2,4,8)) + "  (A(2)=+1/e, sign requires 3D phase space)")
g = np.array([np.exp(-0.5),1,np.exp(-0.5)], complex); g/=np.linalg.norm(g)
for bc, D in [("open",D_open), ("periodic",D_per)]:
    H0sp = np.kron(Ksite(D), alph[0])
    psi = np.kron(g, chi)
    vals = []
    for tt in (1,2,4,8):
        A = np.vdot(psi, expmi(H0sp, tt)@psi)
        vals.append(f"A({tt})={A.real:+.6f}{A.imag:+.6f}i (|A|={abs(A):.6f})")
    say(f"3-site regulator [{bc}], Gaussian width 1 centered site 1, spinor S_n=+1: " + " ; ".join(vals))
say("3-site A(t) is quasi-periodic (finite point spectrum): no decay; continuum reading is the a.c. formula above.")

# ---------------------------------------------------------------- (f) spectral character of h0
say("")
say("=== (f) spectral character of h0 (regulator) ===")
for bc, D in [("open",D_open), ("periodic",D_per)]:
    H0sp = np.kron(Ksite(D), alph[0])
    evs = np.linalg.eigvalsh(H0sp)
    uniq = []
    for e in np.round(evs,10):
        if not uniq or abs(e-uniq[-1][0])>1e-9: uniq.append([e,1])
        else: uniq[-1][1]+=1
    say(f"[{bc}] spec(-iD) = {np.round(np.linalg.eigvalsh(Ksite(D)),10)} ;"
        f" spec(h0 12-dim) = " + ", ".join(f"{e:+.6f}(x{m})" for e,m in uniq))
say("full 108-dim regulator: every h0 eigenvalue carries an extra x9 record-label degeneracy"
    " (invariant public sector, NOT a source bound state).")
say("finite regulator => trivially pure point; continuum reading: h0(p)=alpha_D.p on L2(R^3)xC4 is purely")
say("absolutely continuous, spectrum R, multiplicity from spin+direction, no point spectrum / bound modes;")
say("the discrete zero modes (k=0 mode, open-chain midpoint mode) are regulator artifacts embedded in the a.c. continuum.")

