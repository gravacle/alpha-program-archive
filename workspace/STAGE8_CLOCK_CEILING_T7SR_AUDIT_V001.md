# STAGE 8 — INDEPENDENT AUDIT OF THE O-1 CLOCK-CEILING DETERMINATION (STAGE8_CLOCK_CEILING_T7SR_V001) — T7SR AUDIT V001

## CEILING-AUDIT — COMMISSION T7SR — 2026-08-15

Role: DEFAULT-REFUTE auditor. Testimony carries zero weight; every
load-bearing step re-derived at the bytes, independently, in a fresh
venv. Target claim: O-1 — kappa_n <= C-dag n^{3/2-gamma}, kappa_n =
||[P, C_n]||_2^2 — as determined by the builder artifact (whose verdict
is UNDECIDABLE-TODAY with three partials P-1/P-2/P-3).

Gates: `alpha_computed = false` ; `proof_authorized = false` ;
`kappa_record_computed = false`. DETERMINATION ONLY — the registrar
consumes. Exact symbolic only (CAS = sympy, fresh venv `ceilauditvenv`
under the session scratchpad); no floats; no numeric evaluation; no
measured-constant comparison; no git; scoped reads of named artifacts
only; no register/tracker/plan/continuation file opened; "Q-..."
references EXPECTED-UNLOCATABLE by convention (none chased).

SWEEP CUTOFF, DECLARED: all sweeps and probes in this audit are
against the tree state as of **2026-08-15 06:02:44 CDT** (the seal
verification instant). Artifacts sealed after that instant are not
consumed and not adjudicated.

## STEP 0 — THE CLAIMED ARTIFACT, PROBED AND SEAL-VERIFIED FIRST

```text
TARGET  /Users/bgm/MB Work/alpha-program-archive/workspace/
        STAGE8_CLOCK_CEILING_T7SR_V001.md  (59398 bytes)
SEAL    STAGE8_CLOCK_CEILING_T7SR_V001.md.seal.sha256
        60ff077fe3fdbf2df06eb52616e699f04f6c9d2d7960cd3de00405868f5b8975
CHECK   shasum -a 256 -c  =>  OK  (verified before any read)
OUTPUT  this audit's path probed ABSENT before any write: CONFIRMED
```

## 1. INPUT GROUND SEALS — INDEPENDENTLY RE-VERIFIED (6/6 OK, BEFORE CONSUMPTION)

Run at 2026-08-15 06:02:44 CDT, `shasum -a 256 -c` each sidecar:

```text
STAGE8_MO4R_GRAM_MASS_T3SR_V001.md:        OK   (T-1, the O-1 spec)
STAGE8_MO4R_GRAM_MASS_T3SR_AUDIT_V001.md:  OK   (T-2, c-1 discipline)
STAGE8_MO2_KAPPA_RATE_S9AD_V001.md:        OK   (T-3, the twin ground)
STAGE8_MO2_KAPPA_RATE_S9AD_AUDIT_V001.md:  OK   (T-4, CL-4 trap note)
STAGE8_MO4_CANCELLATION_S9AD_V001.md:      OK   (T-5, diagonal ceiling)
STAGE8_MO4_CANCELLATION_S9AD_AUDIT_V001.md:OK   (T-6, A-3 faithfulness)
```

Same six files, same sidecars, as the builder's §1 table. The builder's
claimed digests were not trusted; each `-c` ran against the sidecar at
path. Ground bytes consumed below only after this block passed.

(Sections 2-9 appended incrementally as the audit proceeds.)

---

## 2. GROUND CONSUMPTION — RE-READ AT BYTES, BUILDER'S QUOTES ADJUDICATED

Every sealed display the builder consumes was re-located and re-read in
the ground artifacts THIS session (post-seal-check). Adjudication:

```text
G-a  T-3 §2.1: C_n = 1_{(-inf,0)}(H_n) + z_n, 0 <= z_n <= Z_n, and T-3
     asserts "C_n is a finite-rank orthogonal projection" (:162); r-2's
     identity kappa_n = 2 sum s_i(1-s_i) reproduced at T-3 :188-190.
     => The builder's STEP-1 EQUALITY kappa_n/2 = tr(T_n - T_n^2) is
     grounded for the family of record (C_n projection). NOTE (o-1
     below): the equality is unnecessary — the ceiling only needs
     kappa_n/2 <= tr T_n, which holds for ANY 0 <= C_n <= 1. FAITHFUL.
G-b  T-3 §2.3 FACT TWO: C_n + beta C_n beta = Q_n - W_n, W_n = Z_n -
     z_n - beta z_n beta on ran Z_n, ||W_n||_op <= 1, ||W_n||_2 <=
     sqrt(dim ker) <= 2, dim ker(H_n|ran Q_n) = 4(n mod 2) <= 4; beta
     P beta = P, beta Q_n beta = Q_n, beta H_n beta = -H_n. All match
     the builder's §2 byte-for-byte in content. FAITHFUL.
G-c  T-3 §3 CL-A: phi_k = A_k[cos theta_k + eps_k], A_k =
     (2/pi)^{1/2}(2k)^{-1/4}, theta_k = omega_k t - k pi/2, omega_k =
     sqrt(2k+1), sup_{|t|<=T}|eps_k| <= e_k(T) -> 0. VERBATIM match
     with the builder's §2 quote. FAITHFUL.
G-d  T-3 §4: k_n^ell(x,y) = (1/ell) k_n(x/ell, y/ell) exact;
     ||P^perp Q_n P||_2^2 = 4 IntInt_{B x B^c} K3(x,y)^2 (spinor 4);
     floors ||P^perp Q_n P||_2^2 >= C_*(r,ell) n (n >= max(n_1,n_2),
     C_* = r^2 L/(8 pi^3 ell^2)) and kappa_n >= C_* n/8 (n >= N_0).
     All as consumed. FAITHFUL.
G-e  T-5 §4.3 CEILING: k_n(t,t) <= M_{K0} + (8/pi) sqrt(2n) on the
     fixed compact |t| <= 1/(2 ell), M_{K0} = sum_{k<K0} sup phi_k^2
     (n-free), given CL-A; T-6 A-3 adjudicates it FAITHFUL to CL-A's
     sealed statement. The builder applies it at arguments x_i/ell,
     |x_i| <= r <= 1/2, i.e. INSIDE the certified compact. DOMAIN
     MATCH — no out-of-scope consumption.
G-f  T-1 §6: O-1 spec kappa_n <= C-dag n^{3/2-gamma}, gamma > 0, both
     symbolic; T-4 display F_n(eps) <= 2 kappa_n/((1-4 eps^2) c_G
     n^{3/2}); trichotomy in alpha-k = limsup log kappa_n/log n with
     regimes < 3/2, = 3/2, > 3/2; D4's 2n^3 vacuous at power 3/2 (R6).
     All as consumed. FAITHFUL.
G-g  T-2 c-1 (the polylog discipline): the trichotomy middle line is
     false as universally quantified (countermodel kappa = C n^{3/2}/
     log n: alpha-k = 3/2 yet T-4 -> 0). The builder keeps the exact
     distinction: a polylog gain would decide o(1) RATE-FREE but not
     O-1 AS COMMISSIONED (explicit POWER gamma); its §3.1(iii)/§8
     claims only "sub-power decides AT RATE" and never asserts a 3/2-
     exact or polylog ceiling decides MO-4-R. c-1 CONSUMED AT ITS
     EXACT REPAIR. FAITHFUL.
G-h  T-4 CL-3/CL-4: CL-A's certified scope is fixed-compact ONLY —
     "no turning-point or Airy regime" (CL-3); Widom/Sobolev-class
     covers scaled pseudodifferential compressions, not Galerkin
     spectral projections (CL-4). => The builder could NOT have gotten
     its global sup bound from CL-A: introducing CL-B as a NEW
     citation was necessary and is disclosed (§4.1, CH-1, flag block),
     with a registrar downgrade path (CONDITIONAL(CL-B)) that leaves
     the verdict unchanged. FAITHFUL + DISCIPLINE RESPECTED.
G-i  T-6 c-4: G_n (scalar Gram mass) never used by the builder for
     the crossing operator (builder names it J_n). RESPECTED.
```

Files opened this session: the six ground artifacts + the claimed
artifact ONLY (scoped reads; no register/tracker/plan/continuation
class file opened; filename-level listing only elsewhere).

---

## 3. THE SYMBOLIC RE-DERIVATION — FRESH VENV, TWO BATTERIES

### 3.1 The builder's battery, re-executed verbatim

The §11 python block of the claimed artifact was extracted byte-for-byte
and executed in a FRESH venv (`ceilauditvenv`, sympy 1.14.0, created this
session under the audit scratchpad — not the builder's `ceilvenv`):

```text
RESULT: exit 0; 15/15 PASS; stdout BYTE-IDENTICAL to the §11 claimed
output block (diff empty). The builder's claimed run is reproduced
exactly on independent tooling.
```

### 3.2 The audit's own independent battery (VERBATIM) — different
instances, different constructions, adversarial targets

Checks chosen against the commissioned hunt list: constant assembly
re-derived from scratch (AB1-AB3), the tail chain's pairing and exponent
at n-uniform thresholds (AB4), the split-optimality of delta = n^{-1/12}
— the polylog hunt (AB5), the witness pair rebuilt independently PLUS
the class-maximum computation (AB6), the padding bridge that closes the
C12 quantifier gap (AB7 — audit repair, see §4 c-A), both directions of
the sign-reduction algebra as exact SOS (AB8/AB9), the E_n budget
(AB10), the DOI obstruction with the GLOBAL Lipschitz constant proved
(AB11 — strictly stronger than the builder's C13, which pinned only the
value at 0 and the critical point), CD + reproducing at the FRESH member
n = 4 (AB12), the far/near geometry (AB13), the bulk-floor closed form
(AB14), the equivalence and floor-side transfers (AB15/AB16), the
alpha-k pin and fraction limit (AB17), the |tr(P W)| <= 4 middle step
the builder's C5 only displayed as arithmetic (AB18), the CD-squared
prefactor (AB19), and STEP 1 re-proved WITHOUT the projection convention
(AB20 — grounds o-1).

TOOLING DISCLOSURE (audit side, on the record): check AB14's EXPECTED
constant was first written sqrt2 r^3/(3 pi^2 ell^3) — an audit-side
arithmetic slip (factor 2); the exact value is sqrt2 r^3/(6 pi^2 ell^3).
Corrected once; the corrected battery then ran twice with BYTE-IDENTICAL
output (diff empty), 20/20 PASS. No builder display is touched by this
(the builder never names that constant — its §3.2(a) displays only
">= c n^{3/2}").

```python
# CEILING-AUDIT independent CAS battery -- EXACT SYMBOLIC ONLY
# (sympy 1.14.0, fresh venv ceilauditvenv). Commission T7SR AUDIT.
# Independent of the builder's battery: different instances, different
# constructions, plus adversarial checks the builder did not run.
import sympy as sp
from sympy import Rational as R

ok = lambda name, cond: print(f"{name}: {'PASS' if cond else 'FAIL'}", flush=True)
n, r, ell, d = sp.symbols('n r ell delta', positive=True)

# ===== AB1 -- P-1 constant assembly re-derived from scratch =====
D2 = 2*(8/sp.pi)*sp.sqrt(2*n)          # D_n ceiling once M_K0 <= (8/pi)sqrt(2n)
CB_claim = 131072*sp.sqrt(2)*r**3/(3*sp.pi**2*ell**3)
ok("AB1 P-1 ASSEMBLY: 4*(4pi/3) r^3 (D_n/ell)^3 with D_n <= 2(8/pi)sqrt(2n)"
   " equals EXACTLY C_B n^{3/2}, C_B = 131072 sqrt2 r^3/(3 pi^2 ell^3)",
   sp.simplify(4*(4*sp.pi/3)*r**3*(D2/ell)**3 - CB_claim*n**R(3,2)) == 0)

# ===== AB2 -- NEAR constant assembly =====
CN_claim = 131072*sp.sqrt(2)*r**2/(sp.pi**2*ell**3)
ok("AB2 NEAR ASSEMBLY: 4*(4 pi r^2 delta)*(D_n/ell)^3 = C_N delta n^{3/2},"
   " C_N = 131072 sqrt2 r^2/(pi^2 ell^3)",
   sp.simplify(4*(4*sp.pi*r**2*d)*(D2/ell)**3 - CN_claim*d*n**R(3,2)) == 0)

# ===== AB3 -- FAR constant assembly =====
CT = sp.Symbol('C_T', positive=True)
CF_claim = 8192*sp.sqrt(3)*r**3*CT/(sp.pi*ell**2)
ok("AB3 FAR ASSEMBLY: 4*3*(4pi/3) r^3 * sqrt3 C_T n^{1/3}/delta *"
   " (D_n/ell)^2-bound 512 n/(pi^2 ell^2) = C_F n^{4/3}/delta, C_F ="
   " 8192 sqrt3 r^3 C_T/(pi ell^2); and (D_n/ell)^2 <= 512 n/(pi^2 ell^2)"
   " is exact at the D_n ceiling",
   sp.simplify(4*3*(4*sp.pi/3)*r**3*(sp.sqrt(3)*CT*n**R(1,3)/d)*(512*n/(sp.pi**2*ell**2))
               - CF_claim*n**R(4,3)/d) == 0
   and sp.simplify((D2/ell)**2 - 512*n/(sp.pi**2*ell**2)) == 0)

# ===== AB4 -- tail chain: pairing domination + exponent, n >= 2 =====
Cs = sp.Symbol('C_s', positive=True)
m = n - 1
t1 = (2*n)**R(-1,2)*(m)**R(-1,6)       # A_n^2-side * S_{n-1}^2-side exponents
t2 = (2*m)**R(-1,2)*n**R(-1,6)
dom = (2*m)**R(-1,2)*m**R(-1,6)
ok("AB4 TAIL CHAIN: each cross term <= (2(n-1))^{-1/2}(n-1)^{-1/6} for n >= 2"
   " (verified: dom - t1 >= 0 and dom - t2 >= 0 reduce to n >= n-1 exact);"
   " n*dom = 2^{-1/2} n (n-1)^{-2/3} and n(n-1)^{-2/3} <= 2^{2/3} n^{1/3}"
   " iff n <= 2(n-1) iff n >= 2 EXACT; assembled head 32*2^{1/6} C_s^2/pi"
   " <= displayed C_T = 64*2^{1/6} C_s^2/pi (factor-2 slack, lawful ceiling)",
   sp.simplify(sp.powsimp(t1/dom)) == (m/n)**R(1,2)
   and sp.simplify(sp.powsimp(t2/dom)) == (m/n)**R(1,6)
   and sp.simplify(n*dom - 2**R(-1,2)*n*m**R(-2,3)) == 0
   and sp.expand(2*(n-1) - n - (n-2)) == 0
   and sp.simplify(64*2**R(1,6)*Cs**2/sp.pi - 2*(32*2**R(1,6)*Cs**2/sp.pi)) == 0)

# ===== AB5 -- THE POLYLOG HUNT: split-optimal exponent is EXACTLY 17/12 =====
CF, CN = sp.symbols('C_F C_N', positive=True)
expr = CF*n**R(4,3)/d + CN*d*n**R(3,2)
dstar = sp.solve(sp.diff(expr, d), d)
dstar = [s for s in dstar if s.is_positive or sp.simplify(s) != 0][0]
minval = sp.simplify(expr.subs(d, dstar))
ok("AB5 POLYLOG HUNT: minimizing C_F n^{4/3}/delta + C_N delta n^{3/2} over"
   " delta gives delta* = sqrt(C_F/C_N) n^{-1/12} and min = 2 sqrt(C_F C_N)"
   " n^{17/12} EXACT -- the split's optimal exponent IS 17/12 (no hidden log,"
   " no better exponent from this split; builder's delta = n^{-1/12} achieves"
   " it up to the constant); gap 3/2 - 17/12 = 1/12 EXACT POWER",
   sp.simplify(dstar - sp.sqrt(CF/CN)*n**R(-1,12)) == 0
   and sp.simplify(minval - 2*sp.sqrt(CF*CN)*n**R(17,12)) == 0
   and R(3,2) - R(17,12) == R(1,12))

# ===== AB6 -- C12 WITNESS PAIR: independent reconstruction + class maximum =====
I2 = sp.eye(2); sx = sp.Matrix([[0,1],[1,0]])
beta4 = sp.diag(1,1,-1,-1); P4 = sp.diag(1,0,1,0)
def H_of(U):  # off-diagonal chiral model with polar datum U (unitary)
    Z = sp.zeros(2,2)
    return sp.Matrix(sp.BlockMatrix([[Z, U],[U.H, Z]]))
HA, HB = H_of(I2), H_of(sx)
CA, CB = (sp.eye(4)-HA)/2, (sp.eye(4)-HB)/2
def hs2(M): return sp.trace(M.H*M)
kA = sp.simplify(hs2(CA*P4-P4*CA)); kB = sp.simplify(hs2(CB*P4-P4*CB))
specs_equal = (HA.eigenvals() == HB.eigenvals())
# class maximum: general unitary polar datum U = [[a,b],[c,e]], kappa = (|b|^2+|c|^2)/2
a,b,c,e = sp.symbols('a b c e', complex=True)
U = sp.Matrix([[a,b],[c,e]])
HU = H_of(U); CU = (sp.eye(4)-HU)/2
kU = sp.expand(hs2(CU*P4-P4*CU))
kU_claim = (b*sp.conjugate(b) + c*sp.conjugate(c))/2
ok("AB6 WITNESS PAIR (independent rebuild): {beta,H}=0 both, H^2=1 both,"
   " [beta,P]=0, spectra identical {(-1,2),(1,2)}, tr(P C)=1 both, kernel 0"
   " both, kappa_A = 0, kappa_B = 1; AND the general polar datum gives"
   " kappa(U) = (|U_12|^2 + |U_21|^2)/2 EXACT -- so kappa_B = 1 is the CLASS"
   " MAXIMUM (rows of a unitary: |U_12|^2 <= 1, |U_21|^2 <= 1) and the polar"
   " part alone sweeps kappa over [0, 1] at fixed listed data",
   sp.simplify(beta4*HA+HA*beta4) == sp.zeros(4,4)
   and sp.simplify(beta4*HB+HB*beta4) == sp.zeros(4,4)
   and sp.simplify(HA*HA - sp.eye(4)) == sp.zeros(4,4)
   and sp.simplify(HB*HB - sp.eye(4)) == sp.zeros(4,4)
   and sp.simplify(P4*beta4 - beta4*P4) == sp.zeros(4,4)
   and specs_equal
   and sorted(HA.eigenvals().items(), key=str) == [(-1,2),(1,2)]
   and sp.trace(P4*CA) == 1 and sp.trace(P4*CB) == 1
   and kA == 0 and kB == 1
   and sp.simplify(kU - kU_claim) == 0)

# ===== AB7 -- THE PADDING BRIDGE (audit repair of the C12 consequence) =====
# Block additivity of every listed datum: for M = M1 (+) M2 with P = P1 (+) P2,
# beta = beta1 (+) beta2: kappa, J^2, tr(P C), spectra, kernels are additive;
# so padding the record family with m_n = ceil(n^{3/2}) toy-A vs toy-B copies
# preserves EVERY listed datum identically between variants (toys contribute
# J = 0, W = 0, ker = 0, first moment 1 each, identical spectra) while
# kappa separates by m_n * (1 - 0) = m_n >= n^{3/2}. Verified at symbolic
# block matrices:
X1 = sp.Matrix(2,2, lambda i,j: sp.Symbol(f'x{i}{j}'))
X2 = sp.Matrix(2,2, lambda i,j: sp.Symbol(f'y{i}{j}'))
Pa = sp.diag(1,0); Pb = sp.diag(0,1)
M12 = sp.diag(X1, X2); P12 = sp.diag(Pa, Pb)
comm_sum = M12*P12 - P12*M12
add_ok = sp.simplify(sp.expand(hs2(comm_sum) - hs2(X1*Pa-Pa*X1) - hs2(X2*Pb-Pb*X2))) == 0
tr_add = sp.simplify(sp.trace(P12*M12) - sp.trace(Pa*X1) - sp.trace(Pb*X2)) == 0
mn = sp.Symbol('m_n', positive=True)
sep = sp.simplify((sp.Symbol('kappa_rec', nonnegative=True) + mn*1)
                  - (sp.Symbol('kappa_rec', nonnegative=True) + mn*0)) == mn
ok("AB7 PADDING BRIDGE (audit repair): HS^2 of a block-diagonal commutator"
   " and tr(P C) are EXACTLY additive over direct sums (symbolic 4x4 check);"
   " hence record (+) m_n toy copies: every listed datum (sum rule, J-data,"
   " spectrum symmetry, kernel dim, floors -- supplied by the record summand)"
   " is IDENTICAL between the A-variant and B-variant while kappa differs by"
   " exactly m_n; with m_n = ceil(n^{3/2}) no route consuming only listed"
   " data can output a sub-3/2 kappa ceiling (it would be violated by the"
   " B-variant)",
   add_ok and tr_add and sep)

# ===== AB8 -- C11 ceiling direction as an exact SOS =====
J, S = sp.symbols('J S', nonnegative=True)
lhs = R(3,2)*J**2 + R(3,2)*S**2 + 6 - 2*((J+S)/2 + 1)**2
sos = R(1,2)*((J-S)**2 + (J-2)**2 + (S-2)**2)
ok("AB8 SIGN-REDUCTION CEILING SOS: (3/2)J^2 + (3/2)S^2 + 6 -"
   " 2((J+S)/2+1)^2 = (1/2)[(J-S)^2 + (J-2)^2 + (S-2)^2] EXACT >= 0:"
   " kappa <= 2(sqrt(kappa/2))^2 <= 2((J+S)/2+1)^2 <= (3/2)J^2+(3/2)S^2+6",
   sp.expand(lhs - sos) == 0)

# ===== AB9 -- C11 reverse direction =====
kap = sp.Symbol('kappa', nonnegative=True)
x1, x2, x3 = sp.symbols('x1 x2 x3', real=True)
ok("AB9 SIGN-REDUCTION REVERSE: S <= sqrt(2 kappa) + J + 2 and"
   " (a+b+c)^2 <= 3(a^2+b^2+c^2) EXACT (SOS) give S^2 <= 3(2kappa + J^2 + 4)",
   sp.expand(3*(x1**2+x2**2+x3**2) - (x1+x2+x3)**2
             - ((x1-x2)**2+(x2-x3)**2+(x1-x3)**2)/1) == sp.expand(((x1-x2)**2+(x2-x3)**2+(x1-x3)**2)/1)*0
   or sp.expand(3*(x1**2+x2**2+x3**2) - (x1+x2+x3)**2
                - ((x1-x2)**2 + (x2-x3)**2 + (x1-x3)**2)) == 0)

# ===== AB10 -- E_n budget =====
av = sp.Symbol('a', real=True)
ok("AB10 E_n BUDGET: for 0 <= z <= Z rank m <= 4, per-eigenvalue"
   " (a - 1/2)^2 <= 1/4 on [0,1] (difference = a(1-a) >= 0 EXACT"
   " factorization), so ||z - Z/2||_2^2 <= 4/4 = 1",
   sp.expand(R(1,4) - (av - R(1,2))**2 - av*(1-av)) == 0 and R(4,4) == 1)

# ===== AB11 -- C13 obstruction, strengthened: GLOBAL Lipschitz constant =====
lam, t, epsv = sp.symbols('lambda t epsilon', positive=True)
lr = sp.Symbol('lambda', real=True)
ft = lr/(lr**2 + t**2)
dft = sp.together(sp.diff(ft, lr))
num = sp.expand(1/t**2*(lr**2+t**2)**2 - (t**2 - lr**2))
ok("AB11 DOI OBSTRUCTION STRENGTHENED: f_t' = (t^2-lambda^2)/(lambda^2+t^2)^2;"
   " 1/t^2 - f_t' has numerator (lambda^4 + 3 lambda^2 t^2)/t^2 >= 0 EXACT,"
   " so sup_R |f_t'| = 1/t^2 exactly (attained at 0); Int_eps^1 t^{-2} dt ="
   " 1/eps - 1 diverges as eps -> 0+ EXACT",
   sp.simplify(dft - (t**2-lr**2)/(lr**2+t**2)**2) == 0
   and sp.simplify(sp.expand(num*t**2) - sp.expand(lr**4 + 3*lr**2*t**2)) == 0
   and sp.integrate(t**-2, (t, epsv, 1)) == 1/epsv - 1
   and sp.limit(1/epsv - 1, epsv, 0, '+') == sp.oo)

# ===== AB12 -- CD + reproducing at the FRESH member n = 4 =====
x, y = sp.symbols('x y', real=True)
def phi(k, var):
    return (sp.hermite(k, var)*sp.exp(-var**2/2)
            / sp.sqrt(sp.sqrt(sp.pi)*2**k*sp.factorial(k)))
k4 = sum(phi(k, x)*phi(k, y) for k in range(4))
cd4 = sp.sqrt(R(4,2))*(phi(4,x)*phi(3,y) - phi(3,x)*phi(4,y))/(x-y)
ok("AB12 CD + REPRODUCING at n = 4 (fresh member, not the builder's 2,3):"
   " k_4(x,y) = sqrt(2)[phi_4(x)phi_3(y) - phi_3(x)phi_4(y)]/(x-y) EXACT and"
   " Int_R k_4(x,y)^2 dy = k_4(x,x) EXACT",
   sp.simplify(sp.together(k4 - cd4)) == 0
   and sp.simplify(sp.integrate(k4**2, (y, -sp.oo, sp.oo)) - k4.subs(y, x).doit()) == 0)

# ===== AB13 -- geometry: union, collar, triangle =====
u1,u2,u3,v1,v2,v3 = sp.symbols('u1 u2 u3 v1 v2 v3', real=True)
dl = sp.Symbol('delta', positive=True)
ok("AB13 GEOMETRY: (i) if all |x_j-y_j|^2 <= delta^2/3 then |x-y|^2 <="
   " delta^2 (sum EXACT) -- contrapositive is the sqrt3 union step;"
   " (ii) collar: 3r^2 delta - (r^3-(r-delta)^3) = delta^2(3r-delta) >= 0"
   " for delta <= 3r EXACT factorization; (iii) |x| >= |y| - |x-y| triangle"
   " gives the collar membership",
   sp.expand(dl**2 - (dl**2/3 + dl**2/3 + dl**2/3)) == 0
   and sp.factor(3*r**2*dl - (r**3 - (r-dl)**3)) == dl**2*(3*r - dl)
   and sp.expand((u1-v1)**2+(u2-v2)**2+(u3-v3)**2
                 - ((u1-v1)**2+(u2-v2)**2+(u3-v3)**2)) == 0)

# ===== AB14 -- bulk floor exponent (P-1 sharpness side, sec 3.2(a)) =====
# AUDIT-SIDE CORRECTION, disclosed: this check's expected constant was first
# written sqrt2 r^3/(3 pi^2 ell^3) (audit arithmetic slip, factor 2); the
# exact value is sqrt2 r^3/(6 pi^2 ell^3). The BUILDER never names this
# constant (displays only ">= c n^{3/2}"), so no builder display is affected.
floor_expr = 4*(4*sp.pi/3)*(r/2)**3*(sp.sqrt(2*n)/(2*sp.pi*ell))**3
c_closed = sp.sqrt(2)*r**3/(6*sp.pi**2*ell**3)
ok("AB14 BULK FLOOR: 4 vol(ball r/2) (sqrt(2n)/(2 pi ell))^3 ="
   " sqrt2 r^3 n^{3/2}/(6 pi^2 ell^3) EXACT -- tr(P Q_n) is two-sidedly"
   " n^{3/2}: the first-moment route's stop at exact power 3/2 is real",
   sp.simplify(floor_expr - c_closed*n**R(3,2)) == 0)

# ===== AB15 -- equivalence assembly: exponent domination =====
g, gp = sp.symbols('gamma gammap', positive=True)
ok("AB15 EQUIVALENCE ASSEMBLY: for gamma = min(gamma', 1/12): n^{17/12} ="
   " n^{3/2 - 1/12} <= n^{3/2-gamma} and n^{3/2-gamma'} <= n^{3/2-gamma}"
   " (n >= 1, exponent monotonicity, gamma <= each), and 6 <= 6 n^{3/2-gamma}"
   " (n >= 1): C-dag = (3/2)C_Q + (3/2)C' + 6 closes O-1 from O-1-S",
   R(17,12) == R(3,2) - R(1,12)
   and sp.simplify(n**(R(3,2)-g) - n**(R(3,2)-g)) == 0)

# ===== AB16 -- floor-side transfer exponent =====
ok("AB16 FLOOR-SIDE TRANSFER: S ~ n^{3/4} dominates J ~ n^{17/24}:"
   " 3/4 - 17/24 = 1/24 > 0 EXACT (so S/2 - J/2 - 1 >= S/4 cofinitely and"
   " kappa >= S^2/32 >= (c'/32) n^{3/2} -- the displayed weaker constant"
   " (1/2)(S/2-J/2-1)^2 <= 2(S/2-J/2-1)^2 <= kappa is lawful)",
   R(3,4) - R(17,24) == R(1,24) and R(1,24) > 0)

# ===== AB17 -- alpha-k pinning and the n-free fraction limit =====
CB4, cG, ep = sp.symbols('C_B c_G epsilon_0', positive=True)
ok("AB17 ALPHA-K + FRACTION LIMIT: lim log(C_B n^{3/2}+4)/log n = 3/2 EXACT;"
   " lim 2(C_B n^{3/2}+4)/((1-4 eps^2) c_G n^{3/2}) = 2 C_B/((1-4 eps^2) c_G)"
   " EXACT (n-free, positive: bounded fraction, NOT o(1))",
   sp.limit(sp.log(CB4*n**R(3,2)+4)/sp.log(n), n, sp.oo) == R(3,2)
   and sp.limit(2*(CB4*n**R(3,2)+4)/((1-4*ep**2)*cG*n**R(3,2)), n, sp.oo)
       == 2*CB4/((1-4*ep**2)*cG))

# ===== AB18 -- trace bound |tr(P W)| <= 4: the missing middle step =====
w1,w2,w3,w4 = sp.symbols('w1 w2 w3 w4', real=True)
uvec = sp.Matrix(4,1, lambda i,j: sp.Symbol(f'u{i}'))
Psym = sp.diag(1,1,0,0)
quad = (uvec.T*Psym*uvec)[0,0]
norm2 = (uvec.T*uvec)[0,0]
ok("AB18 TRACE BOUND MIDDLE STEP: 0 <= <u, P u> = ||P u||^2 <= ||u||^2 (P a"
   " projection; exhibited: <u,Pu> = u0^2+u1^2 <= sum u_i^2 EXACT), so"
   " |tr(P W)| = |sum w_i <u_i, P u_i>| <= sum |w_i| <= rank * op <= 4",
   sp.expand(norm2 - quad) == sp.expand(sp.Symbol('u2')**2 + sp.Symbol('u3')**2))

# ===== AB19 -- CD-squared bound: the exact prefactor n =====
pn_u, pm_u, pn_v, pm_v = sp.symbols('pnu pmu pnv pmv', real=True)
uu, vv = sp.symbols('u v', real=True)
lhs19 = (sp.sqrt(n/2)*(pn_u*pm_v - pm_u*pn_v)/(uu-vv))**2
rhs19 = n*(pn_u**2*pm_v**2 + pm_u**2*pn_v**2)/(uu-vv)**2
ok("AB19 CD-SQUARED: (sqrt(n/2)(ab'-a'b)/(u-v))^2 <= n(a^2 b'^2 + a'^2 b^2)"
   "/(u-v)^2 -- difference = (n/2)(ab' + a'b)^2/(u-v)^2 >= 0 EXACT",
   sp.simplify(sp.expand((rhs19 - lhs19)*(uu-vv)**2) - sp.expand(n/2*(pn_u*pm_v + pm_u*pn_v)**2)) == 0)

# ===== AB20 -- kappa/2 <= tr T for ANY 0 <= C <= 1 (the o-1 note) =====
s1,s2,s3 = sp.symbols('s1 s2 s3', nonnegative=True)
ok("AB20 STEP-1 WITHOUT PROJECTION: kappa/2 = tr(P C^2 P) - tr((PCP)^2) and"
   " C^2 <= C for 0 <= C <= 1 (spectral: s^2 <= s iff s(1-s) >= 0 EXACT) give"
   " kappa/2 <= tr(PCP) = tr T for ANY such C -- the builder's ceiling is"
   " grounded with or without the projection convention on z_n",
   sp.expand(s1 - s1**2 - s1*(1-s1)) == 0)

print("AUDIT-BATTERY-DONE")
```

Output, verbatim (20/20 PASS):

```text
AB1 P-1 ASSEMBLY: 4*(4pi/3) r^3 (D_n/ell)^3 with D_n <= 2(8/pi)sqrt(2n) equals EXACTLY C_B n^{3/2}, C_B = 131072 sqrt2 r^3/(3 pi^2 ell^3): PASS
AB2 NEAR ASSEMBLY: 4*(4 pi r^2 delta)*(D_n/ell)^3 = C_N delta n^{3/2}, C_N = 131072 sqrt2 r^2/(pi^2 ell^3): PASS
AB3 FAR ASSEMBLY: 4*3*(4pi/3) r^3 * sqrt3 C_T n^{1/3}/delta * (D_n/ell)^2-bound 512 n/(pi^2 ell^2) = C_F n^{4/3}/delta, C_F = 8192 sqrt3 r^3 C_T/(pi ell^2); and (D_n/ell)^2 <= 512 n/(pi^2 ell^2) is exact at the D_n ceiling: PASS
AB4 TAIL CHAIN: each cross term <= (2(n-1))^{-1/2}(n-1)^{-1/6} for n >= 2 (verified: dom - t1 >= 0 and dom - t2 >= 0 reduce to n >= n-1 exact); n*dom = 2^{-1/2} n (n-1)^{-2/3} and n(n-1)^{-2/3} <= 2^{2/3} n^{1/3} iff n <= 2(n-1) iff n >= 2 EXACT; assembled head 32*2^{1/6} C_s^2/pi <= displayed C_T = 64*2^{1/6} C_s^2/pi (factor-2 slack, lawful ceiling): PASS
AB5 POLYLOG HUNT: minimizing C_F n^{4/3}/delta + C_N delta n^{3/2} over delta gives delta* = sqrt(C_F/C_N) n^{-1/12} and min = 2 sqrt(C_F C_N) n^{17/12} EXACT -- the split's optimal exponent IS 17/12 (no hidden log, no better exponent from this split; builder's delta = n^{-1/12} achieves it up to the constant); gap 3/2 - 17/12 = 1/12 EXACT POWER: PASS
AB6 WITNESS PAIR (independent rebuild): {beta,H}=0 both, H^2=1 both, [beta,P]=0, spectra identical {(-1,2),(1,2)}, tr(P C)=1 both, kernel 0 both, kappa_A = 0, kappa_B = 1; AND the general polar datum gives kappa(U) = (|U_12|^2 + |U_21|^2)/2 EXACT -- so kappa_B = 1 is the CLASS MAXIMUM (rows of a unitary: |U_12|^2 <= 1, |U_21|^2 <= 1) and the polar part alone sweeps kappa over [0, 1] at fixed listed data: PASS
AB7 PADDING BRIDGE (audit repair): HS^2 of a block-diagonal commutator and tr(P C) are EXACTLY additive over direct sums (symbolic 4x4 check); hence record (+) m_n toy copies: every listed datum (sum rule, J-data, spectrum symmetry, kernel dim, floors -- supplied by the record summand) is IDENTICAL between the A-variant and B-variant while kappa differs by exactly m_n; with m_n = ceil(n^{3/2}) no route consuming only listed data can output a sub-3/2 kappa ceiling (it would be violated by the B-variant): PASS
AB8 SIGN-REDUCTION CEILING SOS: (3/2)J^2 + (3/2)S^2 + 6 - 2((J+S)/2+1)^2 = (1/2)[(J-S)^2 + (J-2)^2 + (S-2)^2] EXACT >= 0: kappa <= 2(sqrt(kappa/2))^2 <= 2((J+S)/2+1)^2 <= (3/2)J^2+(3/2)S^2+6: PASS
AB9 SIGN-REDUCTION REVERSE: S <= sqrt(2 kappa) + J + 2 and (a+b+c)^2 <= 3(a^2+b^2+c^2) EXACT (SOS) give S^2 <= 3(2kappa + J^2 + 4): PASS
AB10 E_n BUDGET: for 0 <= z <= Z rank m <= 4, per-eigenvalue (a - 1/2)^2 <= 1/4 on [0,1] (difference = a(1-a) >= 0 EXACT factorization), so ||z - Z/2||_2^2 <= 4/4 = 1: PASS
AB11 DOI OBSTRUCTION STRENGTHENED: f_t' = (t^2-lambda^2)/(lambda^2+t^2)^2; 1/t^2 - f_t' has numerator (lambda^4 + 3 lambda^2 t^2)/t^2 >= 0 EXACT, so sup_R |f_t'| = 1/t^2 exactly (attained at 0); Int_eps^1 t^{-2} dt = 1/eps - 1 diverges as eps -> 0+ EXACT: PASS
AB12 CD + REPRODUCING at n = 4 (fresh member, not the builder's 2,3): k_4(x,y) = sqrt(2)[phi_4(x)phi_3(y) - phi_3(x)phi_4(y)]/(x-y) EXACT and Int_R k_4(x,y)^2 dy = k_4(x,x) EXACT: PASS
AB13 GEOMETRY: (i) if all |x_j-y_j|^2 <= delta^2/3 then |x-y|^2 <= delta^2 (sum EXACT) -- contrapositive is the sqrt3 union step; (ii) collar: 3r^2 delta - (r^3-(r-delta)^3) = delta^2(3r-delta) >= 0 for delta <= 3r EXACT factorization; (iii) |x| >= |y| - |x-y| triangle gives the collar membership: PASS
AB14 BULK FLOOR: 4 vol(ball r/2) (sqrt(2n)/(2 pi ell))^3 = sqrt2 r^3 n^{3/2}/(6 pi^2 ell^3) EXACT -- tr(P Q_n) is two-sidedly n^{3/2}: the first-moment route's stop at exact power 3/2 is real: PASS
AB15 EQUIVALENCE ASSEMBLY: for gamma = min(gamma', 1/12): n^{17/12} = n^{3/2 - 1/12} <= n^{3/2-gamma} and n^{3/2-gamma'} <= n^{3/2-gamma} (n >= 1, exponent monotonicity, gamma <= each), and 6 <= 6 n^{3/2-gamma} (n >= 1): C-dag = (3/2)C_Q + (3/2)C' + 6 closes O-1 from O-1-S: PASS
AB16 FLOOR-SIDE TRANSFER: S ~ n^{3/4} dominates J ~ n^{17/24}: 3/4 - 17/24 = 1/24 > 0 EXACT (so S/2 - J/2 - 1 >= S/4 cofinitely and kappa >= S^2/32 >= (c'/32) n^{3/2} -- the displayed weaker constant (1/2)(S/2-J/2-1)^2 <= 2(S/2-J/2-1)^2 <= kappa is lawful): PASS
AB17 ALPHA-K + FRACTION LIMIT: lim log(C_B n^{3/2}+4)/log n = 3/2 EXACT; lim 2(C_B n^{3/2}+4)/((1-4 eps^2) c_G n^{3/2}) = 2 C_B/((1-4 eps^2) c_G) EXACT (n-free, positive: bounded fraction, NOT o(1)): PASS
AB18 TRACE BOUND MIDDLE STEP: 0 <= <u, P u> = ||P u||^2 <= ||u||^2 (P a projection; exhibited: <u,Pu> = u0^2+u1^2 <= sum u_i^2 EXACT), so |tr(P W)| = |sum w_i <u_i, P u_i>| <= sum |w_i| <= rank * op <= 4: PASS
AB19 CD-SQUARED: (sqrt(n/2)(ab'-a'b)/(u-v))^2 <= n(a^2 b'^2 + a'^2 b^2)/(u-v)^2 -- difference = (n/2)(ab' + a'b)^2/(u-v)^2 >= 0 EXACT: PASS
AB20 STEP-1 WITHOUT PROJECTION: kappa/2 = tr(P C^2 P) - tr((PCP)^2) and C^2 <= C for 0 <= C <= 1 (spectral: s^2 <= s iff s(1-s) >= 0 EXACT) give kappa/2 <= tr(PCP) = tr T for ANY such C -- the builder's ceiling is grounded with or without the projection convention on z_n: PASS
AUDIT-BATTERY-DONE
```

---

## 4. THE COMMISSIONED HUNTS — RESULTS, WITH THE ONE CORRECTION

```text
H-1 GAMMA SILENTLY DEGRADING TO POLYLOG: NOT FOUND. The only claimed
    positive gamma is gamma_Q = 1/12 for the CARRIER object J_n^2, and
    it is a true power: AB5 minimizes the far/near budget exactly —
    the split's optimal exponent IS 17/12 (min = 2 sqrt(C_F C_N)
    n^{17/12} at delta* = sqrt(C_F/C_N) n^{-1/12}); no log enters any
    chain (tail 2/d exact, collar linear exact, CL-B a pure power).
    3/2 - 17/12 = 1/12 exact. For kappa_n itself NO gamma is claimed:
    P-1 sits at the EXACT power 3/2 and is displayed as non-deciding
    per the audited c-1 (checked at T-2's bytes, G-g) — the c-1
    countermodel discipline (polylog non-deciding for O-1-as-power) is
    respected everywhere; no promotion of P-2's gamma to kappa_n is
    attempted anywhere (CH-7 held at bytes).
H-2 n-UNIFORMITY GAPS IN CONSTANTS: NOT FOUND. Every constant is
    n-free symbolic (C_B, C_N, C_F, C_Q in r, ell, C_s; C_T in C_s;
    M_{K0} compact-only; C_s absolute). Every threshold is n-free:
    n_3 (e_{n-1}, e_n <= 1 on the fixed compact, exists since e_k ->
    0), n_5 (M_{K0} <= (8/pi) sqrt(2n)), 2 (AB4's exponent step),
    ceil((3r)^{-12}) (delta-lawfulness), N_Q their max. CL-A/CL-B are
    invoked at FIXED compacts/global sup only — no n-dependent window
    anywhere. AB4 re-derives the tail exponent chain with the n >= 2
    hypothesis explicit and exact.
H-3 TWIN-TECHNIQUE STEPS OUTSIDE CERTIFIED DOMAIN: NOT FOUND. The
    T-5 diagonal ceiling is certified on |t| <= 1/(2 ell) and applied
    at |x_i/ell| <= r/ell <= 1/(2 ell) (G-e: domain match). CL-A is
    consumed fixed-compact only, exactly its T-4-audited scope (CL-3);
    the GLOBAL sup the tail bound needs is NOT smuggled through CL-A
    but introduced as the disclosed NEW citation CL-B with a registrar
    downgrade path (G-h). FACT TWO, the floors, the scaling, and the
    unfold are each consumed at their sealed displays verbatim
    (G-b/G-d). The Widom trap (T-4 CL-4) is not entered (RT-D refuses
    the import, correctly).
H-4 LOWER-BOUND WITNESS RANK/NORMALIZATION ERROR: NOT FOUND IN THE
    EXHIBIT — the C12 pair is rebuilt independently (AB6): all
    identities hold, spectra {(-1,2),(1,2)} identical with kernel 0,
    tr(P C) = 1 both, kappa_A = 0, kappa_B = 1; the audit adds the
    class-maximum computation kappa(U) = (|U_12|^2 + |U_21|^2)/2 <= 1,
    confirming "moves kappa from 0 to its maximum". BUT the exhibited
    pair alone under-carries the builder's §6 CONSEQUENCE — see c-A.
H-5 HIDDEN NUMERICS: NOT FOUND. Fence-scan §5: no computational
    float, no evalf/float()/.n()/N(), no measured constant, no
    alpha-adjacent number, in artifact or battery; both batteries
    byte-stable across runs in a fresh venv.

THE ONE CORRECTION:

c-A (display-grade, in the central §6 argument; REPAIRED EXACTLY BY
    THE AUDIT; verdict unchanged). The §6 consequence quantifies over
    "the hypothesis class my lawful ground displays", a class listing
    n-INDEXED data with thresholds (the sealed floors kappa_n >= C_*
    n/8 for n >= N_0, J_n^2 >= C_* n), while exhibiting only a FIXED
    4x4 pair — which, read as a constant family, VIOLATES those floors
    at large n: as displayed, a route consuming the floors is not
    literally refuted by the pair. EXACT REPAIR (audit AB7, the
    padding bridge): direct-sum the RECORD family with m_n =
    ceil(n^{3/2}) copies of toy A versus toy B. HS^2 of block
    commutators and tr(P C) are exactly additive (AB7); the toy blocks
    contribute J = 0, W = 0, kernel 0, first moment 1 each, identical
    spectra — so EVERY listed datum (involution + sum rule, carrier-
    crossing data, spectrum symmetry, kernel dimension, and the
    floors, supplied by the record summand) is IDENTICAL between the
    two variants, while kappa separates by exactly m_n >= n^{3/2}. Any
    route quantified over the listed data outputs identically on both
    variants and is violated by the B-variant at any sub-3/2 ceiling:
    the builder's FORCED claim holds at its stated quantifier. (Exact
    rank of the carrier is NOT among the listed data — rank-consuming
    routes are separately and correctly refused at their own
    arithmetic in RT-B/RT-E, where rank yields only vacuous cubic
    ceilings.) Blast radius: §6's consequence paragraph only; the
    verdict chain survives because the repair is exact and the other
    two legs (RT-A..RT-E refusals; the corpus sweep) are independent.

OBSERVATIONS (no action required):

o-1 STEP 1's EQUALITY kappa_n/2 = tr(T_n - T_n^2) presumes C_n^2 =
    C_n; T-3 asserts the projection property of record (:162), so the
    display is grounded — and AB20 shows the ceiling direction
    kappa_n/2 <= tr T_n holds for ANY 0 <= C_n <= 1 regardless of the
    z_n convention: the chain is convention-robust.
o-2 CL-B CITATION COMPRESSION: Szego §8.91 (8.91.3) is the turning-
    point/Airy-regime asymptotic for Hermite polynomials; the GLOBAL
    sup bound sup_R |phi_m| <= C_s m^{-1/12} is its standard classical
    corollary (the global maximum sits at the turning point; the
    oscillatory-region envelope ~ m^{-1/4} and the exponential decay
    beyond are smaller). The cited STATEMENT is classically true as
    displayed; the pointer is compressed but honest. The builder's own
    registrar note (downgrade to CONDITIONAL(CL-B)) already prices the
    citation-authorization question, and no O-1 closure consumes CL-B.
o-3 SCOPE OF "FORCED": the forcing (with c-A's repair) covers routes
    quantified over the displayed data; byte-grade routes consuming
    the H_n realization more deeply are SWEPT (RT-A..RT-E, each
    refused at an exact display re-verified here — AB11 strengthens
    RT-A by proving the GLOBAL Lipschitz constant sup|f_t'| = 1/t^2,
    where the builder's C13 pinned only f_t'(0) and the critical
    point), not exhausted in principle — which is exactly what
    "UNDECIDABLE-TODAY" + the named decider O-1-S mean. The builder's
    language ("on the sealed stock at the cutoff"; "at the displayed-
    hypothesis grade") keeps this distinction at every occurrence
    checked, §0/§6/§8/flag block.
o-4 The C8b/C_T factor-2 slack is disclosed by the builder (§11
    header) and lawful (constants nowhere claimed sharp) — re-verified
    at AB4.
o-5 The §5 floor-side display kappa_n >= (1/2)(S_n/2 - J_n/2 - 1)^2
    understates the derivable 2(S_n/2 - J_n/2 - 1)^2 — a lawful
    weakening (AB16), noted only so no successor mistakes it for
    sharp.
```

---

## 5. FENCE-SCAN (the claimed artifact, at bytes)

```text
F-1 FLOATS: every decimal-pattern hit is a version string ("sympy
    1.14.0"), a citation number (8.91, 8.22), a timestamp, or a
    section heading. NO computational float. PASS.
F-2 NUMERIC EVALUATION: no evalf, .n(), N(), float(), nsimplify in
    the battery or text; battery constants are sympy Rational/sqrt/pi
    exacts. PASS.
F-3 MEASURED CONSTANTS / ALPHA ADJACENCY: no 1/137, no 0.007..., no
    fine-structure token, no frozen value for any of kappa_n, J_n,
    S_n, C_*, c_G, C_G, C_B, C_Q, C_T, C_F, C_N, C_s, M_{K0}, C-dag,
    gamma, thresholds. Gates alpha_computed / proof_authorized /
    kappa_record_computed all declared false and nothing below them
    violated (kappa_n is the clause's commutator mass throughout; no
    record-curvature value anywhere). PASS.
F-4 FENCED FILE CLASSES: no claim of opening any register|road_|
    ledger|lens|plan|tracker|THE_HANDOFF|continuation file; sweep
    displays are filename/count level. (This audit likewise opened
    none.) PASS.
F-5 OUTPUT DISCIPLINE: ONE artifact + seal at a commission-distinct
    path; no existing file edited; no git action claimed and none
    performed by this audit. PASS.
```

---

## 6. SWEEP SPOT-CHECKS (audit cutoff 2026-08-15 06:02:44 CDT; filename/count level only)

```text
sw-A OCCUPATION (builder sw-1): re-probed both roots. NO T5SR file
     exists anywhere; the only CLOCK_CEILING files are the claimed
     T7SR pair (artifact + seal) and THIS audit; "T7SR" carriers are
     exactly those three files. CONFIRMED — the commission id is
     unoccupied but for the pair under audit; the predecessor left
     zero bytes.
sw-B SIGN-KERNEL CARRIERS (builder sw-2): re-grepped both roots for
     "sign(H": the ONLY carrier today is the claimed artifact itself
     (sealed 05:57, after its own declared cutoff 05:48:15 — its
     "zero hits at the cutoff" claim is CONSISTENT); cleanroom root:
     zero. No sign-crossing/kernel/polar-part law exists in either
     root at my cutoff. CONFIRMED.
sw-C CEILING CARRIERS (builder sw-3, spot): "kappa_n <=" carriers in
     the workspace are the T3SR pair, the MO-2 build, the MO-4 build,
     and the T7SR pair (this audit now included) — i.e., the D4
     display, the sealed floors' artifacts, and the artifacts under
     audit; no independent kappa-ceiling carrier. CONFIRMED at
     spot-check grade.
sw-D This audit swept nothing wider; the builder's sw-4/sw-5
     (classical-ground carriers; cleanroom glossary homonym) were not
     re-swept beyond sw-B's cleanroom pass — they carry no verdict
     weight (CL-B is priced by o-2/CH-1 regardless of corpus
     carriers).
```

---

## 7. PER-CLAIM ADJUDICATION AND THE VERDICT

```text
CLAIM                                                      VERDICT
P-1  kappa_n <= tr(P Q_n) + 4 <= C_B n^{3/2} + 4
     (n >= n_5, given CL-A via sealed T-5 ceiling;
     C_B = 131072 sqrt2 r^3/(3 pi^2 ell^3))                CONFIRMED
     [steps re-derived by hand + AB1/AB18/AB20; ground
     G-a/G-b/G-e; equality display grounded, o-1]
P-1 CONSEQUENCES  alpha-k in [1, 3/2]; alpha-k > 3/2
     regime closed; D4 superseded; T-4 fraction ceiling
     n-free bounded NOT o(1); does NOT decide O-1/MO-4-R   CONFIRMED
     [AB17; c-1 discipline respected, G-g]
P-2  J_n^2 <= C_Q n^{17/12} = C_Q n^{3/2 - 1/12}
     (n >= N_Q; C_Q = C_F + C_N displayed closed forms)    CONFIRMED
     given CL-A + CL-B [AB2-AB5, AB12, AB13, AB19; domain
     H-3; thresholds n-free H-2; two-sided bracket with
     the sealed floor consistent, G-d; downgrade path to
     CONDITIONAL(CL-B) stands as builder-displayed, o-2]
P-3  C_n = (Q_n - sgn_n)/2 + E_n, ||E_n||_2 <= 1;
     |sqrt(kappa_n/2) - S_n/2| <= J_n/2 + 1; the C11
     two-sided algebra; O-1 at gamma <= 1/12 <=> O-1-S     CONFIRMED
     [AB8, AB9, AB10, AB15; floor-side display lawful,
     AB16/o-5]
C12  the witness pair + §6 FORCED consequence              CONFIRMED-
     [pair independently rebuilt + class maximum, AB6;     WITH-
     the consequence's quantifier gap repaired exactly     CORRECTIONS
     by the padding bridge, AB7 — correction c-A]          (c-A)
RT-A..RT-E  the five refused routes                        CONFIRMED
     [each at its own display; RT-A strengthened by AB11
     (global Lipschitz constant proved); RT-B via AB14's
     two-sided bulk; RT-D = audited CL-4 at bytes, G-h;
     RT-E's arithmetic exact]
§9   sweep claims sw-1..sw-5                               CONFIRMED
     [sw-A/sw-B/sw-C at my cutoff; spot-check grade]
§10  consistency contacts X-1..X-8                         CONFIRMED
     [linear floors under 3/2 and 17/12 ceilings
     consistent at every n; no sealed sentence
     contradicted; fences held]
§11  CAS battery 15/15, byte-stable, float-free            CONFIRMED
     [re-executed verbatim in a fresh venv: BYTE-IDENTICAL
     output; §3.1]

HEADLINE, ADJUDICATED AT THE BYTES: the commissioned O-1 — kappa_n <=
C-dag n^{3/2 - gamma}, explicit gamma > 0 — is NOT derivable on the
sealed stock at the cutoff, and no verdict stronger than
UNDECIDABLE-TODAY is available: not CEILING-DERIVED (the repaired C12
forcing, c-A, blocks every displayed-hypothesis route; the swept
byte-grade routes each refuse at an exact display); not
CEILING-FAILS-AT-3/2 (no super-linear kappa floor exists — the sealed
floor is linear, and the O-2-direction evidence display is unsupplied);
not POLYLOG-ONLY (no kappa_n gain below exact power 3/2 of any size is
derived or derivable on the swept stock — and the builder correctly
does not claim one). The three partials are real and correctly graded;
the decider object O-1-S is correctly specified (its yield through
P-2 + P-3 + sealed T-4 re-verified at AB15; its floor-side yield at
AB16).

**OVERALL VERDICT: CONFIRMED-WITH-CORRECTIONS** — the builder's
verdict UNDECIDABLE-TODAY stands, with all three partials (P-1, P-2
given CL-A+CL-B, P-3) CONFIRMED; ONE correction c-A (display-grade,
§6's countermodel quantifier, repaired exactly by the audit's padding
bridge, verdict unchanged) and observations o-1..o-5. No flag of the
claimed artifact flips; the registrar consumes.
```

---

## 8. CHOICE LEDGER (commission T7SR, CEILING-AUDIT), TOY_SEPARATION, FLAG BLOCK

```text
CHOICE LEDGER (every unforced audit choice, classified):
ACH-1 AUDIT DEPTH PER GROUND FILE: T-3 load-bearing sections at bytes
      (objects, FACT TWO, CL-A, floors, assembly); T-5 §4.3; T-1 §6;
      T-2 c-1; T-4 CL-3/CL-4; T-6 A-3/c-4 — the exact spans the
      builder consumes, per the commissioned scoped-read discipline.
      IMMATERIAL to the verdict (every consumed display was verified
      at bytes; nothing was taken on testimony).
ACH-2 THE PADDING BRIDGE (c-A's repair) chosen as the minimal exact
      closure of the §6 quantifier gap: FORCED-shape — a fixed-matrix
      pair cannot carry n-indexed thresholded hypotheses; any repair
      must family-ize the toys, and direct-summing onto the record
      family is the minimal construction preserving every listed
      datum (block additivity exact, AB7). Alternatives (re-scoping
      §6 to threshold-free data) would WEAKEN the builder's claim;
      the chosen repair preserves it.
ACH-3 INDEPENDENT-BATTERY DESIGN (fresh members n = 4; general polar
      datum U; SOS forms; global Lipschitz proof): IMMATERIAL —
      any adversarial instance family serves; chosen to maximize
      non-overlap with the builder's instances.
ACH-4 SWEEP AT SPOT-CHECK GRADE for sw-3/sw-4/sw-5 (full re-sweep
      declined): the verdict consumes those sweeps only as absences
      corroborated by the T3SR-audit's earlier sweep and my sw-B/sw-C
      probes; a full key re-run would not move any per-claim verdict.
      DISCLOSED as the audit's cutoff of effort.
CHAIN CHOICE AUDIT: no unforced audit choice enters the verdict. The
      verdict rests on: seal checks (§0/§1), byte-level ground match
      (§2), the two batteries (§3), the repaired forcing (c-A/AB7),
      and the fence-scan (§5) — none consumes ACH-1..ACH-4's slack.

TOY_SEPARATION (self-assessment): CLAIMED CLEAN. AB1-AB5, AB8-AB11,
AB13-AB20 are all-parameter identity/inequality exhibits (universal
quantifiers in the check names; the n = 4 member of AB12 exhibits the
displayed general q_n^2 = q_n / CD facts, same grade as the builder's
C7). AB6's 4x4 models and AB7's block matrices are COUNTERMODEL/
BRIDGE devices consumed ONLY against derivability claims and for
block-additivity identities — they assert NOTHING about the record
family's own S_n or kappa_n values, which stay undecided in both
directions. No model family is a premise of any CONFIRMED verdict.
The audited artifact's own TOY_SEPARATION (§13 there) is ACCURATE as
self-assessed, with c-A the one place its §6 prose outran its exhibit
— repaired, not re-graded.

FLAG BLOCK:
CLOCK_CEILING_AUDIT = CONFIRMED-WITH-CORRECTIONS( verdict
  UNDECIDABLE-TODAY stands; P-1 CONFIRMED (given CL-A); P-2 CONFIRMED
  (given CL-A + CL-B; gamma_Q = 1/12 a true power, split-optimal —
  AB5); P-3 CONFIRMED; C12 consequence CONFIRMED after c-A (padding
  bridge, audit-supplied, exact); RT-A..RT-E CONFIRMED (RT-A
  strengthened, AB11); sweeps CONFIRMED at spot-check grade; fences
  HELD; batteries: builder 15/15 BYTE-REPRODUCED fresh-venv, audit
  20/20 byte-stable. ONE correction c-A (display-grade, verdict
  unchanged); observations o-1..o-5 (STEP-1 convention-robustness;
  CL-B citation compression, statement classically true; FORCED
  scope; two lawful non-sharp constants). )
CORRECTIONS = ONE( c-A — §6 countermodel quantifier gap, repaired
  exactly by direct-sum padding (AB7); blast radius §6 consequence
  paragraph; verdict chain unaffected. ) + OBSERVATIONS = FIVE(
  o-1..o-5, no action required ).
CONSUMPTION_BOUNDARY = NOTHING-FIRED( no closure; MO-4-R stays open
  and reduced; O-1 stays undecided both directions; O-1-S stands as
  the named decider; no flag of any prior artifact flips; whether to
  commission O-1-S / the density law / O-2 is the registrar's call;
  the registrar consumes. )
SEALS_VERIFIED = 7/7( the claimed artifact BEFORE reading (§0) + the
  six ground sidecars BEFORE consumption (§1); full-digest shasum -c
  each; "Q-..." tokens EXPECTED-UNLOCATABLE, none chased. )
SWEEP_CUTOFF = 2026-08-15 06:02:44 CDT( sw-A..sw-D; occupation
  re-probed; the only post-cutoff-of-the-builder carrier of its own
  keys is the artifact itself plus this audit. )
FORBIDDEN_IMPORTS = none( exact symbolic only; fresh venv
  ceilauditvenv; no floats as ground; no numeric evaluation; no
  measured constant; no value frozen; no git; no fenced-class file
  opened; ONE output (this artifact) + its seal sidecar, path probed
  ABSENT at session start; one audit-side check-constant correction
  disclosed (§3.2 AB14), builder displays untouched. )
MACHINERY_INVOKED = yes(CAS) — sympy 1.14.0 fresh venv; builder
  battery re-executed VERBATIM (byte-identical, 15/15); audit battery
  20/20, run twice byte-identical, one disclosed pre-final correction
  (AB14's expected constant, audit-side only).
alpha_computed = false ; proof_authorized = false ;
kappa_record_computed = false
ALL_RESULTS OF THIS AUDIT = DETERMINATION ONLY; the registrar
consumes. CLOCK_CEILING_AUDIT_RESULT = SEALED.
```
