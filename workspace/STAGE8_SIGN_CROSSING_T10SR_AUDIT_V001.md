# STAGE 8 — AUDIT OF THE O-1-S SIGN-CROSSING ARTIFACT (T10SR) — DEFAULT-REFUTE, RE-DERIVED AT THE BYTES — T10SR AUDIT V001

## SN-AUDIT — COMMISSION T10SR — 2026-08-15

Date: 2026-08-15 (session CDT). Role: AUDITOR (SN-AUDIT), DEFAULT-REFUTE;
testimony carries zero weight; every load-bearing step re-derived at the
bytes in a fresh venv.

THE CLAIMED ARTIFACT:
`/Users/bgm/MB Work/alpha-program-archive/workspace/STAGE8_SIGN_CROSSING_T10SR_V001.md`
(+ `.seal.sha256`). Its question: O-1-S (the S_n ceiling or floor), as
specified at the sealed T7SR §8 display.

Gates: `alpha_computed = false` ; `proof_authorized = false` ;
`kappa_record_computed = false`. DETERMINATION ONLY — no adoption, no
authored physics; the registrar consumes. Fences held: exact symbolic
only (CAS = sympy, fresh venv `auditvenv_t10sr` under the session
scratchpad; batteries sourced into this artifact by file-append); no
floats as ground; no numeric evaluation; no measured-constant
comparison; every rational-vs-pi comparison routed through the CLASSICAL
bound pi < 22/7 (Archimedes), rational arithmetic only; no git; no
fenced-class file opened (register|road_|ledger|lens|plan|tracker|
THE_HANDOFF|continuation — filename-level listing only); "Q-..." tokens
EXPECTED-UNLOCATABLE by design, none chased; scoped reads of named
artifacts only; ONE output (this artifact) plus its seal sidecar, output
path probed ABSENT at session start and re-probed immediately before
seal. Marks: DERIVED / CONFIRMED / CLAIMED / CLASSICAL(cited) /
CONDITIONAL(premise named) span by span.

SWEEP CUTOFF, DECLARED: the audit sweep of §8 was executed against the
tree state as of **2026-08-15 07:19:00 CDT** (tree unchanged since the
claimed artifact's 06:56 seal except this audit's own output file).
Artifacts sealed after that instant are not consumed and not swept.

---

## 0. VERDICT IN ONE LINE

**CONFIRMED-WITH-CORRECTIONS — the headline (UNDECIDABLE-TODAY for
O-1-S as commissioned, neither direction derivable on the sealed stock
at the cutoff) is CONFIRMED at the bytes; the three derived partials
SP-1 / SP-2 (given CL-C) / SP-3 are CONFIRMED by independent
re-derivation (operator forms exact; every CAS conjunct re-run
byte-identical, builder's battery 10/10 PASS twice, audit's own
independent battery 10/10 PASS twice, both byte-stable); the
corrections are
display/scope-grade and none flips the verdict: (F-1) the §5.2/§8
grid-coordinate displays of the excess and of A_n leave the
zero-momentum column unpinned for n odd — the exact excess carries an
additional kernel-column term 4 sum_{p != 0} |B_p0|^2 in [0, 4] that
the displayed angular sum omits (angle(p, 0) undefined); bounded slack,
every power-law yield survives with constants folded; (F-2) the §6
padding-bridge display "S^2 separates by m_n * 8/49 >= n^{3/2}" is
false as written at m_n = ceil(n^{3/2}) (the separation is
(8/49) n^{3/2}-grade); the forcing survives (any Theta(n^{3/2})
separation refutes a sub-3/2 ceiling); (F-3) the c-A-pattern n-indexing
check the artifact's own discipline demands was not run on its OWN
padded countermodel: the W12' toys carry J_toy^2 = 45/49 per copy, so
the padded variants' J-datum exits the record's sealed P-2 bracket
(J^2 <= C_Q n^{17/12}) at rate n^{3/2} — routes whose hypothesis class
includes the sealed P-2 ceiling are NOT covered by the displayed
forcing (unlike the audited AB7 original, whose C12 toys carried J = 0
exactly); repaired exactly here (audit AT-5/AT-7: an idempotent-B toy
with J_toy = 0, per-copy separation 2, and an n-indexed toy radius
above the record band that verifies every thresholded listed datum
including the count-law inequality); (F-4) the §6 sentence "no
super-linear floor quantified over the listed class survives the pair"
overclaims the pair's reach — both padded variants have S^2 >=
(8/49) n^{3/2}, so the pair refutes NO floor; the floor-direction
class-level refutation needs a different witness (audit AT-6: the
all-parallel model — same listed data shape, excess = 0) or rests, as
the artifact separately and correctly displays at RT-F', on the
sweep-absence of any anti-localization carrier; with either repair the
floor-side refusal stands. Nothing fires; no flag of any prior
artifact flips; the registrar consumes.**

---

## 1. STEP 0 + INPUT SEALS — ALL VERIFIED AT PATH (shasum -a 256 -c) BEFORE ANY RELIANCE

```text
STEP 0 — THE CLAIMED ARTIFACT:
  STAGE8_SIGN_CROSSING_T10SR_V001.md            PRESENT (63740 bytes)
  sidecar digest c66f948ef33b126e1d709428f291e29dde16db9cf13ce944
  edfae1f2e10e8639 — shasum -a 256 -c: OK. Read IN FULL after
  verification. Output path STAGE8_SIGN_CROSSING_T10SR_AUDIT_V001.md
  probed ABSENT at session start (before any other action).

INPUT GROUND (the same sealed ground the builder names in its §1),
independently re-verified, 8/8 OK, each BEFORE consumption:
  T-1 STAGE8_CLOCK_CEILING_T7SR_V001.md          OK
  T-2 STAGE8_CLOCK_CEILING_T7SR_AUDIT_V001.md    OK
  T-3 STAGE8_MO4R_GRAM_MASS_T3SR_V001.md         OK
  T-4 STAGE8_MO4R_GRAM_MASS_T3SR_AUDIT_V001.md   OK
  T-5 STAGE8_MO2_KAPPA_RATE_S9AD_V001.md         OK
  T-6 STAGE8_MO2_KAPPA_RATE_S9AD_AUDIT_V001.md   OK
  T-7 STAGE8_MO4_CANCELLATION_S9AD_V001.md       OK
  T-8 STAGE8_MO4_CANCELLATION_S9AD_AUDIT_V001.md OK
Scoped reads only; no fenced-class file opened; no other file opened
at content level.
```

---
## 2. GROUND CONSUMPTION — THE BUILDER'S QUOTES ADJUDICATED AT BYTES

Each load-bearing quote in the claimed artifact was re-read at its
sealed source. Scoped reads only.

```text
G-1 T-1 §2/§5/§8 (the T7SR ground): sgn_n and S_n definitions; P-3
    (C_n = (Q_n - sgn_n)/2 + E_n, ||E_n||_2 <= 1); the C11 two-sided
    algebra kappa_n <= (3/2) J_n^2 + (3/2) S_n^2 + 6 and S_n^2 <=
    3(2 kappa_n + J_n^2 + 4); the O-1-S spec (ceiling => O-1 at
    gamma = min(gamma', 1/12); floor => CEILING-FAILS-AT-3/2 via the
    §5 floor-side display); P-1 (kappa_n <= C_B n^{3/2} + 4, §3.1);
    P-2 (J_n^2 <= C_Q n^{17/12}, §4, given CL-A + CL-B); BLOCKER-1/
    BLOCKER-2; C12 and its §6 consequence; sw-2 at cutoff 05:48:15
    CDT. ALL FAITHFULLY QUOTED by the claimed artifact.        MATCH
G-2 T-2 (T7SR audit): c-A at bytes — the AB7 padding bridge's toys
    "contribute J = 0, W = 0, kernel 0 ... kappa separates by exactly
    m_n >= n^{3/2}" (NOTE: J = 0 toys and per-copy separation exactly
    1 — the two properties the claimed artifact's W12' padding does
    NOT inherit; see F-2/F-3); o-3 scope note verbatim ("byte-grade
    routes consuming the H_n realization more deeply are SWEPT ...
    not exhausted in principle") — the door SP-1 walks through is
    real and correctly quoted.                                 MATCH
G-3 T-3 (T3SR): the T-4 display F_n(eps) <= 2 kappa_n/((1 - 4 eps^2)
    c_G n^{3/2}) at :224; the O-1 spec §6.                     MATCH
G-4 T-4 (T3SR audit): c-1 at bytes (:251-268). OBSERVATION o-A: c-1's
    own content is that a polylog-only kappa gain (e.g. C n^{3/2}/
    log n) DOES decide MO-4-R's o(1) via T-4 — the correction was
    against "localization ALONE decides" prose. The claimed
    artifact's paraphrase ("a polylog-only gain does NOT decide —
    POWER gamma demanded", §1/T-4 line) is faithful to the O-1-S
    COMMISSION (explicit gamma' > 0 demanded) and to T-1 §8's
    NOT-POLYLOG-ONLY category, but it is NOT what the c-1 byte
    establishes; nothing consumes the paraphrase (the artifact
    derives no polylog gain at all — CO-2 returns exact 3/2), so
    verdict-immaterial. Quote-fidelity observation only.  MATCH(o-A)
G-5 T-5 (MO2): the tensor bytes §2.1-2.3 — H_n = sum_j pi_j alpha_j,
    pi_x = (q_n p q_n) tensor q_n tensor q_n, DIFFERENT factors,
    commute exactly; <k|p|k+1> = -i sqrt((k+1)/2)/ell, zero
    diagonal; Q_n = q_n^{x3} tensor 1_4 rank 4n^3; dim ker = 4(n mod
    2) <= 4; C_*(r, ell) = r^2 L/(8 pi^3 ell^2); floors ||P^perp Q_n
    P||_2^2 >= C_* n (n >= max(n_1, n_2)), kappa_n >= C_* n/8; CL-A
    verbatim (§3).                                             MATCH
G-6 T-6 (MO2 audit): CL-2 (8.22.6 transcription exact); CL-3 (CL-A
    fixed-compact ONLY — "no growing windows, no turning-point or
    Airy regime"); CL-4 (Widom covers scaled pseudodifferential
    compressions, not Galerkin spectral projections).          MATCH
G-7 T-7 (MO4_CANCELLATION): diagonal ceiling k_n(t,t) <= M_{K0} +
    (8/pi) sqrt(2n) on the fixed compact (:361-364); G_n two-sided
    c_G n^{3/2} <= G_n <= C_G n^{3/2} (:367); the crossing identity
    and MO-4-R naming (§4.5).                                  MATCH
G-8 T-8 (MO4 audit): A-3 adjudicates the diagonal ceiling FAITHFUL;
    c-4 names the G_n notational collision — the claimed artifact's
    X-7 respects it (B_pp' is a NEW name, no collision).       MATCH
```

No quote failure found. The one paraphrase stretch is o-A above
(display-grade, consumed nowhere).

---

## 3. THE RE-DERIVATION — EVERY LOAD-BEARING STEP, INDEPENDENTLY

```text
R-1 SP-1 STEP 1 (simplicity). Deleting the LAST ROW and FIRST COLUMN
    of (q_n p q_n - lambda) leaves a triangular matrix with diagonal
    (-i a_0/ell, ..., -i a_{n-2}/ell), det != 0, rank >= n-1: every
    eigenvalue simple. CONFIRMED — with one COSMETIC correction
    (F-7): that submatrix is LOWER-triangular (nonzero entries at
    submatrix j in {i-2, i-1, i}), not "upper-triangular" as the
    display says; the determinant, the rank bound, and the
    conclusion are unchanged (the upper-triangular variant arises
    from deleting FIRST row and LAST column).
R-2 SP-1 STEP 2 (spectrum = zeros). (D M D^{-1})_{k,k+1} =
    i^{-1}(-i a_k/ell) = -a_k/ell and (D M D^{-1})_{k+1,k} =
    i (i a_k/ell) = -a_k/ell: D M D^{-1} = -(1/ell) J_x EXACT; the
    three-term recurrence row identity J_x v(lambda) = lambda
    v(lambda) - a_{n-1} phi_n(lambda) e_{n-1} re-derived; phi_0
    never vanishes; n simple eigenvalues vs n zeros of phi_n:
    spec = Z_n^{(1)}/ell (symmetric set). CONFIRMED. Audit pushes
    the member exhibits PAST the builder's n = 3: char poly of J_n
    = the MONIC Hermite polynomial H_n(x)/2^n exactly at n = 4 AND
    n = 5 (AT-3), D-conjugation and simplicity minors there too,
    and nullity (0 at n = 4, > 0 at n = 5) reproducing 4(n mod 2).
R-3 SP-1 STEP 3 + resolution. Commuting tensor factors => joint grid
    G_n = (Z_n^{(1)}/ell)^3, |G_n| = n^3, product eigenvectors;
    blockwise functional calculus on H_n = sum_p Pi_p tensor
    (p.alpha): (1 -+ U(p))/2 are EXACTLY the spectral projections at
    -+|p| (AT-1 verifies BOTH signs, projection property, and
    completeness — one conjunct more than the builder's SN2);
    sgn_n = sum_{p != 0} Pi_p tensor (p.alpha)/|p|; kernel = the
    p = 0 block, present iff n odd, dim 4(n mod 2) — matches the
    sealed FACT TWO independently; rank sum 4n^3 = rank Q_n; beta
    sgn_n beta = -sgn_n termwise. CONFIRMED (32-dim member rebuilt
    from scratch, AT-2). SP-1 IS A DERIVATION FROM SEALED BYTES —
    no crossing law is imported anywhere in it (the hunt's central
    question; see H-2).
R-4 SP-2. CL-C as cited is the classical Sturm statement; the
    Hermite ODE is CAS-exact at members (builder k = 0..4; audit
    adds k = 5, 6); the zero-gap consequence >= pi/sqrt(2n+1) is
    exhibited EXACTLY at the members n = 3, 4 by pure-rational
    chains through the CLASSICAL bound pi < 22/7 (AT-10; no
    numerics); the count assembly (m-1)s <= 2a, the per-axis
    product bound, the factor 4, and n-uniformity re-derived
    (AT-9); |p| <= E => every |p_j| <= E is exact. CONFIRMED given
    CL-C, exactly as scoped by the builder's own registrar note
    (blast radius SP-2 only; verdict consumes it nowhere).
R-5 SP-3 operator form. The three trace reductions of §5.1 were
    re-derived by hand and verified on a HARDER instance class than
    the builder's (rank-2 kernel, dim 8, exact-rational random-ish
    projection, AT-4a): S_n^2 = J_n^2 + (1/2)||Q_n [P, sgn_n]
    Q_n||_2^2 - ||Q_n^perp P Z_n||_2^2 EXACT; corr in [0, rank Z];
    the CO-4 hidden step corr <= J_n^2 (from Z <= Q and X = P
    Q^perp P >= 0: tr(ZXZ) <= tr(QXQ)) made explicit and verified;
    ||[P, u]||_2^2 = 2 S_n^2 block identity verified. CONFIRMED.
R-6 SP-3 grid form. In the SP-1 basis Q_n P Q_n = B tensor 1_4;
    J_n^2 = 4(tr B - tr B^2); K_{pp'} = B_pp'(u(p') - u(p)) with
    ||U(p') - U(p)||_HS^2 = 8(1 - cos angle). For n EVEN the §5.2
    display is EXACT. For n ODD the p = 0 column contributes
    ||0 - U(p)||_HS^2 = 4 per entry, giving the EXACT excess
      (1/2)||K||_2^2 = 4 sum_{p != p', both != 0} |B_pp'|^2
        (1 - cos angle(p, p'))  +  4 sum_{p != 0} |B_p0|^2 ,
    second term in [0, 4] (sum_p |B_p0|^2 = (B^2)_{00} <= 1) — the
    displayed angular sum OMITS it, and angle(p, 0) is undefined in
    the A_n display. FINDING F-1 (exhibited exactly on a 16-dim
    n-odd-form model, AT-4b: displayed sum 288/1521 vs true excess
    340/1521). All power-law yields survive: the slack folds into
    the constant (4 <= 4 n^{3/2 - gamma'} for n >= 1, AT-9).
R-7 CO-1..CO-4. CO-1's arithmetic (C_* n - 4 >= (C_*/2) n for
    n >= 8/C_*) exact; CO-2's chain re-derived (off-mass <= tr B^2
    <= tr B = tr(P Q_n)/4; the n-odd kernel column is covered by
    the "+4" already displayed there — CO-2 is CORRECT as written);
    CO-3 re-verified on the resolved n = 2 member with a generic
    rational ball (AT-8); CO-4 confirmed with its hidden step now
    displayed (R-5). CONFIRMED.
R-8 The DOI tightness display (RT-A'): the entry integral =
    (pi/2)(sgn l_i - sgn l_j) re-verified both signs (AT-9);
    entrywise tightness argument sound; the W12' leg it leans on is
    sound for CEILING-shaped totals-only assemblies (see F-4 for
    the floor side). CONFIRMED at its stated scope.
```

---
## 4. THE TWO CAS BATTERIES — FRESH VENV, RE-RUN AND INDEPENDENT

Fresh venv `auditvenv_t10sr` (session scratchpad); sympy 1.14.0 — the
SAME version the builder pins, so version drift is excluded as an
explanation for any divergence (none arose).

### 4.1 The builder's battery, re-executed VERBATIM

```text
Extracted from the sealed artifact between its ```python fences
(227 lines; extraction sha256
59e20b6941c4106df2158a4c95c786374ef6df5697e5e0bf33538d851d7fc751);
run TWICE: exit 0 both, 10/10 PASS both, run1 == run2 BYTE-IDENTICAL,
and run1 == THE DISPLAYED §11 OUTPUT BYTE-IDENTICAL (diff empty).
The builder's disclosed SN2 check-form note (Hermiticity tested on
the numerator) is visible in the source and is mathematically
harmless as disclosed: the audit's AT-1 additionally verifies BOTH
spectral projections and completeness with no such workaround needed.
```

### 4.2 The audit's own independent battery (VERBATIM SOURCE)

Different constructions, harder instances (rank-2 kernel; n-odd grid
form with a zero momentum point; n = 4, 5 Jacobi members; k = 5, 6
ODE members; the repair witnesses; the padded-countermodel n-indexing
checks). Run TWICE: exit 0 both, 10/10 PASS both, byte-identical
across runs. Source, by file-append:

```python
# SN-AUDIT independent battery -- EXACT SYMBOLIC ONLY (sympy, fresh venv
# auditvenv_t10sr). Commission T10SR AUDIT. DEFAULT-REFUTE: every check is the
# auditor's own construction; no builder code reused. No floats, no numeric
# evaluation, no measured constants; every pi comparison routed through the
# CLASSICAL rational bound pi < 22/7 (Archimedes) and pure rational arithmetic.
import itertools
import sympy as sp
from sympy import Rational as R, I, sqrt, kronecker_product as kron

ok = lambda name, cond: print(f"{name}: {'PASS' if cond else 'FAIL'}", flush=True)

ell = sp.Symbol('ell', positive=True)
rho = sp.Symbol('rho', positive=True)
nn = sp.Symbol('n', positive=True)

# my own Dirac construction (standard rep, independent assembly)
sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -I], [I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]]); Z2 = sp.zeros(2, 2)
def offblock(s):
    m = sp.zeros(4, 4)
    m[0:2, 2:4] = s; m[2:4, 0:2] = s
    return m
AL = [offblock(s) for s in (sx, sy, sz)]
BETA = sp.diag(1, 1, -1, -1)

# ===== AT-1 -- Dirac + polar ground, both spectral projections =====
ax, ay, az = sp.symbols('a_x a_y a_z', real=True)
pa = ax*AL[0] + ay*AL[1] + az*AL[2]
mod = sp.sqrt(ax**2 + ay**2 + az**2)
c1 = all(sp.expand(AL[i]*AL[j] + AL[j]*AL[i] - 2*(1 if i == j else 0)*sp.eye(4))
         == sp.zeros(4, 4) for i in range(3) for j in range(3))
c2 = all(sp.trace(AL[i]*AL[j]) == (4 if i == j else 0) for i in range(3) for j in range(3))
c3 = all(sp.expand(BETA*a + a*BETA) == sp.zeros(4, 4) for a in AL) and sp.expand(BETA*BETA) == sp.eye(4)
c4 = sp.expand(pa*pa - (ax**2 + ay**2 + az**2)*sp.eye(4)) == sp.zeros(4, 4)
c5 = sp.trace(pa) == 0 and sp.expand(pa.H - pa) == sp.zeros(4, 4)
Pp = (sp.eye(4) + pa/mod)/2; Pm = (sp.eye(4) - pa/mod)/2
c6 = (sp.simplify(sp.expand(pa*Pp - mod*Pp)) == sp.zeros(4, 4)
      and sp.simplify(sp.expand(pa*Pm + mod*Pm)) == sp.zeros(4, 4)
      and sp.simplify(sp.expand(Pp*Pp - Pp)) == sp.zeros(4, 4)
      and sp.simplify(sp.expand(Pm*Pm - Pm)) == sp.zeros(4, 4)
      and sp.simplify(sp.expand(Pp + Pm)) == sp.eye(4))
bx, by, bz = sp.symbols('b_x b_y b_z', real=True)
qa = bx*AL[0] + by*AL[1] + bz*AL[2]
modq = sp.sqrt(bx**2 + by**2 + bz**2)
c7 = sp.simplify(sp.trace((pa/mod)*(qa/modq)) - 4*(ax*bx + ay*by + az*bz)/(mod*modq)) == 0
ok("AT-1 DIRAC+POLAR GROUND (independent): CAR, traces, beta, (p.a)^2 = |p|^2,"
   " tr(p.a) = 0, Hermitian; BOTH spectral projections (1 +- U)/2 verified as"
   " projections summing to 1 with p.a (1+-U)/2 = +-|p| (1+-U)/2; tr(U_p U_q) ="
   " 4 cos angle -- all symbolic EXACT", c1 and c2 and c3 and c4 and c5 and c6 and c7)

# ===== AT-2 -- SP-1 rebuilt independently at n = 2; zeros of H_2 =====
m2 = sp.Matrix([[0, -I*sqrt(R(1, 2))/ell], [I*sqrt(R(1, 2))/ell, 0]])  # sealed bytes
lam = sp.Symbol('lambda', real=True)
cp2 = sp.expand((m2 - lam*sp.eye(2)).det())
c_cp = sp.expand(cp2 - (lam**2 - R(1, 2)/ell**2)) == 0   # zeros of H_2 = +-1/sqrt2, /ell
D2 = sp.diag(1, I)
J2 = sp.Matrix([[0, sqrt(R(1, 2))], [sqrt(R(1, 2)), 0]])
c_conj2 = sp.expand(D2*m2*D2**-1 + (1/ell)*J2) == sp.zeros(2, 2)
wP = sp.Matrix([1, I])/sqrt(2); wM = sp.Matrix([1, -I])/sqrt(2)
c_ev = (sp.expand(m2*wP - (1/(sqrt(2)*ell))*wP) == sp.zeros(2, 1)
        and sp.expand(m2*wM + (1/(sqrt(2)*ell))*wM) == sp.zeros(2, 1))
PI3 = [kron(kron(m2, sp.eye(2)), sp.eye(2)), kron(kron(sp.eye(2), m2), sp.eye(2)),
       kron(kron(sp.eye(2), sp.eye(2)), m2)]
c_comm = all(sp.expand(PI3[a]*PI3[b] - PI3[b]*PI3[a]) == sp.zeros(8, 8)
             for a in range(3) for b in range(3))
H32 = sp.zeros(32, 32)
for j in range(3):
    H32 += kron(PI3[j], AL[j])
sgn32 = sp.zeros(32, 32)
wv = {1: wP, -1: wM}
for s3 in itertools.product((1, -1), repeat=3):
    proj = kron(kron(wv[s3[0]]*wv[s3[0]].H, wv[s3[1]]*wv[s3[1]].H), wv[s3[2]]*wv[s3[2]].H)
    unit = (s3[0]*AL[0] + s3[1]*AL[1] + s3[2]*AL[2])/sqrt(3)
    sgn32 += kron(proj, unit)
b32 = kron(sp.eye(8), BETA)
c_all = (sp.expand(sgn32.H - sgn32) == sp.zeros(32, 32)
         and sp.expand(sgn32*sgn32 - sp.eye(32)) == sp.zeros(32, 32)
         and sp.expand(sgn32*H32 - H32*sgn32) == sp.zeros(32, 32)
         and sp.expand(sgn32*H32 - (sqrt(3)/(sqrt(2)*ell))*sp.eye(32)) == sp.zeros(32, 32)
         and sp.expand(H32*H32 - (R(3, 2)/ell**2)*sp.eye(32)) == sp.zeros(32, 32)
         and sp.expand(b32*sgn32 + sgn32*b32) == sp.zeros(32, 32))
ok("AT-2 SP-1 AT n = 2, REBUILT (32-dim): sealed tridiagonal's char poly ="
   " lam^2 - 1/(2 ell^2) (zeros of H_2 scaled), D-conjugation to -(1/ell)J,"
   " commuting momenta, sgn built blockwise: Hermitian, square 1, commutes"
   " with H, sgn*H = sqrt(3/2)/ell > 0, H^2 = (3/2)/ell^2, beta-odd -- EXACT",
   c_cp and c_conj2 and c_ev and c_comm and c_all)

# ===== AT-3 -- Jacobi identification PAST the builder's exhibit: n = 4, 5 =====
aof = lambda k: sqrt(R(k + 1, 2))
def Jn(n):
    M = sp.zeros(n, n)
    for k in range(n - 1):
        M[k, k + 1] = aof(k); M[k + 1, k] = aof(k)
    return M
def herm_monic(n):
    x = sp.Symbol('x')
    return sp.expand(sp.hermite(n, x)/2**n), x
c_j = True
for n_ in (4, 5):
    Jm = Jn(n_)
    x = sp.Symbol('x')
    cp = sp.expand((x*sp.eye(n_) - Jm).det())
    hm, xv = herm_monic(n_)
    c_j = c_j and sp.expand(cp - hm.subs(xv, x)) == 0
    # sealed-byte tridiagonal, D-conjugation, simplicity minor
    Pm_ = sp.zeros(n_, n_)
    for k in range(n_ - 1):
        Pm_[k, k + 1] = -I*aof(k)/ell; Pm_[k + 1, k] = I*aof(k)/ell
    Dn = sp.diag(*[I**k for k in range(n_)])
    c_j = c_j and sp.expand(Dn*Pm_*Dn**-1 + (1/ell)*Jm) == sp.zeros(n_, n_)
    minor_det = sp.prod([aof(k) for k in range(n_ - 1)])
    c_j = c_j and sp.simplify(minor_det) != 0
c_nul = (Jn(4).det() != 0) and (sp.expand(Jn(5).det()) == 0)
ok("AT-3 JACOBI IDENTIFICATION AT n = 4 AND n = 5 (past the builder's n = 3"
   " exhibit): char poly of J_n = the MONIC Hermite polynomial H_n/2^n exactly"
   " (spectrum = zeros of phi_n); sealed tridiagonal conjugates by D = diag(i^k)"
   " to -(1/ell)J_n; simplicity minor prod a_k != 0; nullity 0 at n = 4 and"
   " > 0 at n = 5 (det J_5 = 0): the 4(n mod 2) kernel law at members -- EXACT",
   c_j and c_nul)

# ===== AT-4 -- SP-3 identity: rank-2 kernel instance + THE n-ODD GRID FORM (F-1) =====
# (a) dim-8 exact-rational instance, kernel rank 2
A8 = sp.Matrix([[1, 0, 1], [1, 1, 0], [0, 1, 1], [1, 1, 1], [1, 0, 0],
                [0, 1, 0], [0, 0, 1], [1, 2, 1]])
P8 = A8*(A8.T*A8)**-1*A8.T
Q8 = sp.diag(1, 1, 1, 1, 1, 1, 0, 0)
u8 = sp.zeros(8, 8); u8[0, 1] = u8[1, 0] = 1; u8[2, 2] = 1; u8[3, 3] = -1
Z8 = sp.diag(0, 0, 0, 0, 1, 1, 0, 0)
pre = (sp.expand(P8*P8 - P8) == sp.zeros(8, 8) and sp.expand(u8*u8 - (Q8 - Z8)) == sp.zeros(8, 8)
       and u8*Q8 == u8 and Q8*u8 == u8 and Z8*Q8 == Z8)
S2 = sp.trace(((sp.eye(8) - P8)*u8*P8).T*((sp.eye(8) - P8)*u8*P8))
J2i = sp.trace(((sp.eye(8) - P8)*Q8*P8).T*((sp.eye(8) - P8)*Q8*P8))
K8 = Q8*(P8*u8 - u8*P8)*Q8
corr8 = sp.trace(((sp.eye(8) - Q8)*P8*Z8).T*((sp.eye(8) - Q8)*P8*Z8))
c_a = sp.simplify(S2 - J2i - R(1, 2)*sp.trace(K8.T*K8) + corr8) == 0
c_a2 = (0 <= corr8) and (corr8 <= 2)   # rank Z = 2 instance: corr in [0, rank Z]
c_a3 = corr8 <= J2i                     # the CO-4 hidden step, instance-verified
c_a4 = sp.simplify(sp.trace((P8*u8 - u8*P8).T*(P8*u8 - u8*P8)) - 2*S2) == 0  # ||[P,u]||^2 = 2 S^2
# (b) THE n-ODD GRID FORM: resolved model WITH a zero momentum point
v4 = sp.Matrix([1, 2, 3, 5])
Psp = v4*v4.T/39
PF = kron(Psp, sp.eye(4))
QF = kron(sp.diag(1, 1, 1, 0), sp.eye(4))
ZF = kron(sp.diag(1, 0, 0, 0), sp.eye(4))          # p0 = 0 IN the carrier
e11 = sp.diag(0, 1, 0, 0); e22 = sp.diag(0, 0, 1, 0)
uG = kron(e11, AL[0]) + kron(e22, AL[1])           # p1 = rho e_x, p2 = rho e_y, angle pi/2
HG = rho*(kron(e11, AL[0]) + kron(e22, AL[1]))
pre_b = (sp.expand(uG*uG - (QF - ZF)) == sp.zeros(16, 16)
         and sp.expand(HG*HG - rho**2*(QF - ZF)) == sp.zeros(16, 16))
S2g = sp.trace(((sp.eye(16) - PF)*uG*PF).H*((sp.eye(16) - PF)*uG*PF))
J2g = sp.trace(((sp.eye(16) - PF)*QF*PF).H*((sp.eye(16) - PF)*QF*PF))
KG = QF*(PF*uG - uG*PF)*QF
corrG = sp.trace(((sp.eye(16) - QF)*PF*ZF).H*((sp.eye(16) - QF)*PF*ZF))
c_b1 = sp.simplify(S2g - J2g - R(1, 2)*sp.trace(KG.H*KG) + corrG) == 0
# B matrix on carrier slots {0,1,2}: B_ij = v_i v_j / 39, v = (1,2,3)
B01, B02, B12 = R(2, 39), R(3, 39), R(6, 39)
disp_sum = 4*(2*B12**2*(1 - 0))                       # displayed: nonzero pairs only
kercol = 4*(B01**2 + B02**2)                          # the OMITTED kernel-column term
c_b2 = sp.simplify(R(1, 2)*sp.trace(KG.H*KG) - (disp_sum + kercol)) == 0
c_b3 = sp.simplify(disp_sum - R(288, 1521)) == 0 and sp.simplify(kercol - R(52, 1521)) == 0
c_b4 = kercol > 0                                     # the omission is REAL on the instance
c_b5 = kercol <= 4                                    # and bounded as the audit states
ok("AT-4 SP-3 IDENTITY: (a) rank-2-kernel dim-8 exact-rational instance:"
   " S^2 = J^2 + (1/2)||Q[P,u]Q||_2^2 - ||Q^perp P Z||_2^2 EXACT, corr in"
   " [0, rank Z], corr <= J^2 (CO-4's hidden step), ||[P,u]||_2^2 = 2 S^2;"
   " (b) F-1 EXHIBIT, n-ODD grid form with p0 = 0: the exact excess ="
   " [4 sum_{p != p' != 0} |B|^2 (1 - cos)] + [4 sum_{p != 0} |B_p0|^2] ="
   " 288/1521 + 52/1521 -- the displayed angular sum OMITS the kernel-column"
   " term 52/1521 > 0 (bounded by 4): the SS5.2/SS8 displays are inexact for"
   " n odd exactly as the audit states", pre and c_a and c_a2 and c_a3 and c_a4
   and pre_b and c_b1 and c_b2 and c_b3 and c_b4 and c_b5)

# ===== AT-5 -- W12' REBUILT + the F-2/F-3 exhibits =====
v3 = sp.Matrix([1, 2, 3])
Pw = kron(v3*v3.T/14, sp.eye(4))
Qw = kron(sp.diag(1, 1, 0), sp.eye(4))
f11 = sp.diag(1, 0, 0); f22 = sp.diag(0, 1, 0)
uA = kron(f11, AL[0]) + kron(f22, AL[1])
uB = kron(f11, AL[0]) - kron(f22, AL[0])
HA = rho*uA
HB = rho*kron(f11, AL[0]) + kron(f22, -rho*AL[0])
bw = kron(sp.eye(3), BETA)
CA = (Qw - uA)/2; CB = (Qw - uB)/2
listed = (sp.expand(HA*HA - rho**2*Qw) == sp.zeros(12, 12)
          and sp.expand(HB*HB - rho**2*Qw) == sp.zeros(12, 12)
          and sp.trace(HA) == 0 and sp.trace(HB) == 0
          and sp.expand(bw*HA + HA*bw) == sp.zeros(12, 12)
          and sp.expand(bw*HB + HB*bw) == sp.zeros(12, 12)
          and sp.expand(bw*Pw - Pw*bw) == sp.zeros(12, 12)
          and sp.expand(CA*CA - CA) == sp.zeros(12, 12)
          and sp.expand(CB*CB - CB) == sp.zeros(12, 12)
          and sp.trace(Pw*CA) == sp.trace(Pw*CB))
S2A = sp.trace(((sp.eye(12) - Pw)*uA*Pw).H*((sp.eye(12) - Pw)*uA*Pw))
S2B = sp.trace(((sp.eye(12) - Pw)*uB*Pw).H*((sp.eye(12) - Pw)*uB*Pw))
J2w = sp.trace(((sp.eye(12) - Pw)*Qw*Pw).H*((sp.eye(12) - Pw)*Qw*Pw))
c_sep = (sp.simplify(S2A - J2w - R(8, 49)) == 0 and sp.simplify(S2B - J2w - R(16, 49)) == 0)
# F-3: the toys' own J^2 is NOT zero -- it is 45/49 per copy
c_f3 = sp.simplify(J2w - R(45, 49)) == 0
# padded J-datum exits ANY n^{17/12} bracket: (45/49) n^{3/2} / n^{17/12} = (45/49) n^{1/12}
c_f3b = sp.simplify(nn**R(3, 2)/nn**R(17, 12) - nn**R(1, 12)) == 0
# F-2: the displayed separation constant is 8/49 < 1 (so m_n = ceil(n^{3/2})
# gives separation (8/49) n^{3/2}-grade, NOT >= n^{3/2} as displayed)
c_f2 = R(8, 49) < 1
ok("AT-5 W12' REBUILT (independent): all listed-data identities hold and"
   " S_A^2 = J^2 + 8/49, S_B^2 = J^2 + 16/49 (separation 8/49) EXACT --"
   " builder's SN6 CONFIRMED; AND the audit exhibits: J_toy^2 = 45/49 != 0"
   " per copy (F-3: padded variants' J-datum grows at (45/49) n^{3/2}, and"
   " n^{3/2}/n^{17/12} = n^{1/12} cofinally exits ANY sealed C_Q n^{17/12}"
   " bracket -- P-2-consuming routes are NOT covered by the displayed"
   " forcing); 8/49 < 1 (F-2: the displayed 'm_n * 8/49 >= n^{3/2}' is false"
   " at m_n = ceil(n^{3/2}))", listed and c_sep and c_f3 and c_f3b and c_f2)

# ===== AT-6 -- THE TWO AUDIT REPAIR WITNESSES =====
# (a) idempotent-B toy: J_toy = 0, separation 2 per copy (F-3 repair)
w2 = sp.Matrix([1, 1, 0])
Pi_ = kron(w2*w2.T/2, sp.eye(4))
c_r1 = sp.expand(Pi_*Pi_ - Pi_) == sp.zeros(12, 12)
S2Ai = sp.trace(((sp.eye(12) - Pi_)*uA*Pi_).H*((sp.eye(12) - Pi_)*uA*Pi_))
S2Bi = sp.trace(((sp.eye(12) - Pi_)*uB*Pi_).H*((sp.eye(12) - Pi_)*uB*Pi_))
J2i_ = sp.trace(((sp.eye(12) - Pi_)*Qw*Pi_).H*((sp.eye(12) - Pi_)*Qw*Pi_))
c_r2 = (sp.simplify(J2i_) == 0 and sp.simplify(S2Ai - 2) == 0
        and sp.simplify(S2Bi - 4) == 0)
c_r3 = (sp.expand(bw*Pi_ - Pi_*bw) == sp.zeros(12, 12)
        and sp.trace(Pi_*CA) == sp.trace(Pi_*CB))
# (b) all-parallel witness: excess = 0, S^2 = J^2 exactly (F-4 repair)
g11 = sp.diag(1, 0, 0, 0); g22 = sp.diag(0, 1, 0, 0); g33 = sp.diag(0, 0, 1, 0)
uPar = kron(g11 + g22 + g33, AL[0])
HPar = kron(rho*g11 + 2*rho*g22 + 3*rho*g33, AL[0])
QPar = kron(sp.diag(1, 1, 1, 0), sp.eye(4))
vP = sp.Matrix([1, 2, 3, 5]); PPar = kron(vP*vP.T/39, sp.eye(4))
bP = kron(sp.eye(4), BETA)
c_p1 = (sp.expand(uPar*uPar - QPar) == sp.zeros(16, 16)
        and sp.expand(HPar*uPar - (kron(rho*g11 + 2*rho*g22 + 3*rho*g33, sp.eye(4))))
        == sp.zeros(16, 16)
        and sp.expand(bP*HPar + HPar*bP) == sp.zeros(16, 16)
        and sp.expand(bP*PPar - PPar*bP) == sp.zeros(16, 16))
S2P = sp.trace(((sp.eye(16) - PPar)*uPar*PPar).H*((sp.eye(16) - PPar)*uPar*PPar))
J2P = sp.trace(((sp.eye(16) - PPar)*QPar*PPar).H*((sp.eye(16) - PPar)*QPar*PPar))
c_p2 = sp.simplify(S2P - J2P) == 0
ok("AT-6 AUDIT REPAIR WITNESSES: (a) idempotent-B toy (P from w = (e1+e2)/"
   "sqrt2): J_toy^2 = 0 EXACTLY while S_A^2 = 2, S_B^2 = 4 (separation 2 per"
   " copy, J-datum untouched by padding: the F-3 repair -- the forcing now"
   " covers P-2-consuming routes); (b) ALL-PARALLEL witness (three collinear"
   " momenta rho, 2rho, 3rho): resolved form, chirality, u^2 = Q, H u = |H|,"
   " and S^2 = J^2 EXACTLY (excess = 0): a listed-class member with the sign"
   " crossing equal to the carrier crossing -- the F-4 floor-side witness",
   c_r1 and c_r2 and c_r3 and c_p1 and c_p2)

# ===== AT-7 -- n-INDEXING OF THE PADDED COUNTERMODEL (the c-A-pattern check) =====
# (i) Gershgorin: ||J_n||_op <= max row sum <= 2 a_{n-1} = sqrt(2n) => every
#     record radius <= sqrt(3) sqrt(2n)/ell =: R_n. Exhibit at n = 5 exactly.
J5 = Jn(5)
rowmax_sq_bound = (2*aof(4))**2         # (2 sqrt(5/2))^2 = 10 = 2n at n = 5
c_g1 = sp.simplify(rowmax_sq_bound - 10) == 0
gersh = all(sum(sp.Abs(J5[i, j]) for j in range(5) if j != i)**2 <= 10 for i in range(5))
# (ii) toy radius rho_n := 2 sqrt(6 n)/ell = 2 R_n sits above the record band:
#     (2 sqrt(6n)/ell)^2 = 24 n / ell^2 > 3 * 2n / ell^2 = R_n^2 iff 24 > 6.
c_g2 = R(24, 1) > R(6, 1)
# (iii) count-law headroom at E >= rho_n, EXACT RATIONAL CHAIN via pi < 22/7
#     and sqrt3 >= 3/2 ((3/2)^2 = 9/4 <= 3):
#     ceiling >= 4 (2 rho_n ell sqrt(2n+1)/pi)^3 >= 4 (2*2*sqrt(6n)*sqrt(2n)/pi)^3
#     = 6144 sqrt(3) n^3 / pi^3 >= 6144*(3/2)*343/10648 n^3 = 296.87...*n^3
#     >= 4 n^3 + 8 m_n + [4 n^3 slack]  for n >= 1  (padded total states).
c_g3 = R(9, 4) <= 3                                    # sqrt3 >= 3/2, squared
c_g4 = R(6144*3*343, 2*10648) >= R(20, 1)              # 6322176/21296 >= 20
c_g5 = R(20, 1)*1 >= R(4, 1) + R(8, 1) + R(8, 1)       # 4n^3+8n^{3/2}+8 <= 20 n^3, n >= 1
ok("AT-7 c-A-PATTERN n-INDEXING CHECK ON THE PADDED COUNTERMODEL: Gershgorin"
   " ||J_n||_op^2 <= 2n at the n = 5 member (record radii <= sqrt(6n)/ell,"
   " DERIVED, no new citation); n-indexed toy radius rho_n = 2 sqrt(6n)/ell"
   " sits strictly above the record band (24 > 6); and the SP-2 count-law"
   " inequality HOLDS for the padded variants at every E, by the exact"
   " rational chain via CLASSICAL pi < 22/7: 6144*sqrt3/pi^3 >="
   " 6322176/21296 >= 20 >= (4 n^3 + 8 m_n + 8)/n^3 at n >= 1 -- the"
   " padding bridge closes at the stated quantifier ONCE the J-preserving"
   " toy (AT-6a) is used; the artifact's own variant fails only the P-2"
   " bracket (F-3)", c_g1 and gersh and c_g2 and c_g3 and c_g4 and c_g5)

# ===== AT-8 -- CO-3 first moment; CO-2 totals chain on the resolved member =====
Pgen = kron(vP[0:3, 0]*vP[0:3, 0].T/14, sp.eye(4))    # generic rational spatial P, 12-dim
c_m1 = sp.trace(Pgen*uA) == 0 and sp.trace(Pgen*uB) == 0
Psp32 = sp.zeros(8, 8)
vv8 = sp.Matrix([1, 1, 2, 3, 5, 8, 13, 21]); Psp32 = vv8*vv8.T/sum(x**2 for x in vv8)
P32g = kron(Psp32, sp.eye(4))
c_m2 = sp.simplify(sp.trace(P32g*sgn32)) == 0          # tr(P sgn) = 0 at the n = 2 member
Bm = v3*v3.T/14
offmass = sum(Bm[i, j]**2 for i in range(3) for j in range(3) if i != j)
c_m3 = offmass <= sp.trace(Bm*Bm) and sp.trace(Bm*Bm) <= sp.trace(Bm)
ok("AT-8 CO-3/CO-2: tr(P sgn) = 0 EXACT on both W12' models AND on the full"
   " n = 2 resolved member with a generic rational spatial ball (beta-odd"
   " first moment vanishes -- the sign question is second-moment); the CO-2"
   " totals chain off-mass <= tr B^2 <= tr B verified exact", c_m1 and c_m2 and c_m3)

# ===== AT-9 -- count/DOI/yield arithmetic, independent =====
m_, s_, a_ = sp.symbols('m s a', positive=True)
c_c1 = sp.expand((m_ - 1)*s_ - (2*a_) - ((m_ - (1 + 2*a_/s_))*s_)) == 0
M0, u1, u2, u3 = sp.symbols('M u1 u2 u3', nonnegative=True)
c_c2 = sp.expand(M0**3 - u1*u2*u3 - ((M0 - u1)*M0**2 + u1*(M0 - u2)*M0 + u1*u2*(M0 - u3))) == 0
lamP = sp.Symbol('lambda_p', positive=True)
t = sp.Symbol('t', positive=True)
c_c3 = sp.integrate(lamP/(lamP**2 + t**2), (t, 0, sp.oo)) == sp.pi/2
c_c4 = sp.integrate(-lamP/(lamP**2 + t**2), (t, 0, sp.oo)) == -sp.pi/2
c_c5 = R(3, 2) - R(17, 12) == R(1, 12)
Cst = sp.Symbol('C_star', positive=True)
c_c6 = sp.expand((Cst*nn - 4) - (Cst*nn/2) - (Cst*nn/2 - 4)) == 0
gp = sp.Symbol('gamma_p', positive=True)
c_c7 = sp.simplify(nn**(R(3, 2) - gp)*nn**(gp - R(3, 2))) == 1  # fold sanity
ok("AT-9 COUNT/DOI/YIELD ARITHMETIC (independent): gap-count rearrangement"
   " exact; 3-factor telescoping exact; DOI entry integral = (pi/2) sgn"
   " both signs; 3/2 - 17/12 = 1/12; floor transfer; exponent fold -- EXACT"
   " (so F-1's +4 kernel-column slack folds into the ceiling constant:"
   " 4 <= 4 n^{3/2 - gamma'} for n >= 1, every power-law yield survives)",
   c_c1 and c_c2 and c_c3 and c_c4 and c_c5 and c_c6 and c_c7)

# ===== AT-10 -- Hermite ODE past the builder's members; CL-C gaps at members =====
xx = sp.Symbol('x', real=True)
def phi(k):
    return sp.hermite(k, xx)*sp.exp(-xx**2/2)/sp.sqrt(sp.sqrt(sp.pi)*2**k*sp.factorial(k))
ode_ok = all(sp.simplify(sp.diff(phi(k), xx, 2) + (2*k + 1 - xx**2)*phi(k)) == 0
             for k in (5, 6))
# zeros of H_3: {0, +-sqrt(3/2)}; gap^2 = 3/2 >= pi^2/7 via pi^2 < 484/49:
c_z3 = R(484, 49) < R(21, 2) or R(968, 1) <= R(1029, 1)   # 968 <= 1029 exact
c_z3b = R(968, 1) <= R(1029, 1)
# zeros of H_4: inner gap^2 = 6 - 2 sqrt6 >= 484/441 iff 6*441^2 <= 1081^2;
# outer gap^2 = 3 - sqrt3 >= 484/441 iff 3*441^2 <= 839^2 (sqrt3 <= 839/441):
c_z4 = (R(6)*441**2 <= R(1081)**2) and (R(3)*441**2 <= R(839)**2)
# symbolic identities for the gap algebra at n = 4:
s6 = sp.sqrt(6)
c_z4b = (sp.expand((2*sp.sqrt((3 - s6)/2))**2 - (6 - 2*s6)) == 0
         and sp.expand((sp.sqrt((3 + s6)/2) - sp.sqrt((3 - s6)/2))**2
                       - (3 - sp.sqrt(3))).simplify() == 0)
ok("AT-10 HERMITE ODE AT k = 5, 6 (past the builder's 0..4) and CL-C's"
   " consequence at members: zero gaps of phi_3 and phi_4 are >= pi/sqrt(2n+1)"
   " by EXACT RATIONAL chains through CLASSICAL pi < 22/7 (968 <= 1029;"
   " 6*441^2 <= 1081^2; 3*441^2 <= 839^2) -- no numerics, no evalf",
   ode_ok and c_z3 and c_z3b and c_z4 and c_z4b)

print("AT-BATTERY-DONE")
```

Output, verbatim (both runs byte-identical):

```text
AT-1 DIRAC+POLAR GROUND (independent): CAR, traces, beta, (p.a)^2 = |p|^2, tr(p.a) = 0, Hermitian; BOTH spectral projections (1 +- U)/2 verified as projections summing to 1 with p.a (1+-U)/2 = +-|p| (1+-U)/2; tr(U_p U_q) = 4 cos angle -- all symbolic EXACT: PASS
AT-2 SP-1 AT n = 2, REBUILT (32-dim): sealed tridiagonal's char poly = lam^2 - 1/(2 ell^2) (zeros of H_2 scaled), D-conjugation to -(1/ell)J, commuting momenta, sgn built blockwise: Hermitian, square 1, commutes with H, sgn*H = sqrt(3/2)/ell > 0, H^2 = (3/2)/ell^2, beta-odd -- EXACT: PASS
AT-3 JACOBI IDENTIFICATION AT n = 4 AND n = 5 (past the builder's n = 3 exhibit): char poly of J_n = the MONIC Hermite polynomial H_n/2^n exactly (spectrum = zeros of phi_n); sealed tridiagonal conjugates by D = diag(i^k) to -(1/ell)J_n; simplicity minor prod a_k != 0; nullity 0 at n = 4 and > 0 at n = 5 (det J_5 = 0): the 4(n mod 2) kernel law at members -- EXACT: PASS
AT-4 SP-3 IDENTITY: (a) rank-2-kernel dim-8 exact-rational instance: S^2 = J^2 + (1/2)||Q[P,u]Q||_2^2 - ||Q^perp P Z||_2^2 EXACT, corr in [0, rank Z], corr <= J^2 (CO-4's hidden step), ||[P,u]||_2^2 = 2 S^2; (b) F-1 EXHIBIT, n-ODD grid form with p0 = 0: the exact excess = [4 sum_{p != p' != 0} |B|^2 (1 - cos)] + [4 sum_{p != 0} |B_p0|^2] = 288/1521 + 52/1521 -- the displayed angular sum OMITS the kernel-column term 52/1521 > 0 (bounded by 4): the SS5.2/SS8 displays are inexact for n odd exactly as the audit states: PASS
AT-5 W12' REBUILT (independent): all listed-data identities hold and S_A^2 = J^2 + 8/49, S_B^2 = J^2 + 16/49 (separation 8/49) EXACT -- builder's SN6 CONFIRMED; AND the audit exhibits: J_toy^2 = 45/49 != 0 per copy (F-3: padded variants' J-datum grows at (45/49) n^{3/2}, and n^{3/2}/n^{17/12} = n^{1/12} cofinally exits ANY sealed C_Q n^{17/12} bracket -- P-2-consuming routes are NOT covered by the displayed forcing); 8/49 < 1 (F-2: the displayed 'm_n * 8/49 >= n^{3/2}' is false at m_n = ceil(n^{3/2})): PASS
AT-6 AUDIT REPAIR WITNESSES: (a) idempotent-B toy (P from w = (e1+e2)/sqrt2): J_toy^2 = 0 EXACTLY while S_A^2 = 2, S_B^2 = 4 (separation 2 per copy, J-datum untouched by padding: the F-3 repair -- the forcing now covers P-2-consuming routes); (b) ALL-PARALLEL witness (three collinear momenta rho, 2rho, 3rho): resolved form, chirality, u^2 = Q, H u = |H|, and S^2 = J^2 EXACTLY (excess = 0): a listed-class member with the sign crossing equal to the carrier crossing -- the F-4 floor-side witness: PASS
AT-7 c-A-PATTERN n-INDEXING CHECK ON THE PADDED COUNTERMODEL: Gershgorin ||J_n||_op^2 <= 2n at the n = 5 member (record radii <= sqrt(6n)/ell, DERIVED, no new citation); n-indexed toy radius rho_n = 2 sqrt(6n)/ell sits strictly above the record band (24 > 6); and the SP-2 count-law inequality HOLDS for the padded variants at every E, by the exact rational chain via CLASSICAL pi < 22/7: 6144*sqrt3/pi^3 >= 6322176/21296 >= 20 >= (4 n^3 + 8 m_n + 8)/n^3 at n >= 1 -- the padding bridge closes at the stated quantifier ONCE the J-preserving toy (AT-6a) is used; the artifact's own variant fails only the P-2 bracket (F-3): PASS
AT-8 CO-3/CO-2: tr(P sgn) = 0 EXACT on both W12' models AND on the full n = 2 resolved member with a generic rational spatial ball (beta-odd first moment vanishes -- the sign question is second-moment); the CO-2 totals chain off-mass <= tr B^2 <= tr B verified exact: PASS
AT-9 COUNT/DOI/YIELD ARITHMETIC (independent): gap-count rearrangement exact; 3-factor telescoping exact; DOI entry integral = (pi/2) sgn both signs; 3/2 - 17/12 = 1/12; floor transfer; exponent fold -- EXACT (so F-1's +4 kernel-column slack folds into the ceiling constant: 4 <= 4 n^{3/2 - gamma'} for n >= 1, every power-law yield survives): PASS
AT-10 HERMITE ODE AT k = 5, 6 (past the builder's 0..4) and CL-C's consequence at members: zero gaps of phi_3 and phi_4 are >= pi/sqrt(2n+1) by EXACT RATIONAL chains through CLASSICAL pi < 22/7 (968 <= 1029; 6*441^2 <= 1081^2; 3*441^2 <= 839^2) -- no numerics, no evalf: PASS
AT-BATTERY-DONE
```

---
## 5. FINDINGS — THE CORRECTION SET (none flips the verdict)

```text
F-1 (correction, display-grade; §5.2 and §8/O-1-S-B; REPAIRED HERE).
  THE ZERO-MOMENTUM COLUMN OF THE GRID DISPLAYS IS UNPINNED FOR n
  ODD. The exact excess in grid coordinates is
    S_n^2 - J_n^2 + ||Q_n^perp P Z_n||_2^2
      = 4 sum_{p != p', p, p' != 0} |B_pp'|^2 (1 - cos angle(p, p'))
        + 4 sum_{p != 0} |B_p0|^2            [n odd; second term
        absent n even; in [0, 4] since sum_p |B_p0|^2 = (B^2)_{00}
        <= 1],
  while the §5.2 display and the §8 definition of A_n write the
  angular sum over ALL pairs p != p' in G_n with weight (1 - cos
  angle(p, p')) — undefined at p' = 0 and, under any convention,
  off the exact excess by a bounded term (<= 8). AT-4b exhibits the
  omission exactly (displayed sum 288/1521 vs true excess 340/1521
  on a 16-dim n-odd-form model). BLAST RADIUS: none at power grade —
  the §8 yield "S_n^2 <= J_n^2 + 4 A_n + 0" becomes S_n^2 <= J_n^2 +
  4 A_n + 4 with A_n read over nonzero pairs, and 4 <= 4 n^{3/2 -
  gamma_B} for n >= 1 folds into C_B'' (AT-9); the floor-side yield
  likewise survives with c shifted by an O(1) term. EXACT REPAIR:
  define A_n over pairs of NONZERO grid points and add the displayed
  kernel-column term, or restrict the O-1-S-B object to n even and
  carry n odd by the [0, 4] bracket.
F-2 (correction, display-grade; §6 QUANTIFIER NOTE). "S^2 separates
  by m_n * 8/49 >= n^{3/2}" is FALSE as written at m_n =
  ceil(n^{3/2}): the separation is (8/49) m_n >= (8/49) n^{3/2}, and
  8/49 < 1 (AT-5). The audited AB7 original had per-copy separation
  EXACTLY 1, so its ">= n^{3/2}" was true; the W12' toys' per-copy
  separation is 8/49 and the display was carried over unadjusted.
  IMMATERIAL to the forcing (any Theta(n^{3/2}) separation kills a
  sub-3/2 ceiling: variant B alone has S^2 >= (8/49) n^{3/2} >
  C n^{3/2 - gamma} cofinally); the display should read ">=
  (8/49) n^{3/2}" or take m_n = ceil((49/8) n^{3/2}).
F-3 (correction, scope-grade; §6 QUANTIFIER NOTE + BLOCKER-2'; the
  c-A PATTERN AT ONE REMOVE — the commissioned hunt's exact target).
  THE PADDED COUNTERMODEL'S OWN n-INDEXED DATA WERE NOT RE-CHECKED
  AGAINST THE RECORD'S SEALED BRACKETS. The W12' toys are NOT
  J-silent: J_toy^2 = 45/49 per copy EXACTLY (AT-5; the artifact
  never displays this value). Under the displayed padding m_n =
  ceil(n^{3/2}), the variants' J-datum grows by (45/49) m_n ~
  (45/49) n^{3/2}, which cofinally exits the record's sealed P-2
  bracket J_n^2 <= C_Q n^{17/12} (n^{3/2}/n^{17/12} = n^{1/12} ->
  inf, symbolically, AT-5). CONSEQUENCE: the §6 forcing, as
  displayed, does NOT refute ceiling routes whose hypothesis class
  includes the sealed P-2 ceiling as an n-indexed threshold — and
  the artifact's own contemplated route (O-1-S-B => yield through
  SP-3 + P-2) consumes exactly P-2. The audited AB7 original does
  not have this leak (its C12 toys carry J = 0 exactly, T-2 c-A
  bytes). EXACT REPAIR (AT-6a + AT-7, audit's): replace the toy
  ball by the IDEMPOTENT-B ball P = w w^T tensor 1_4, w = (e1 +
  e2)/sqrt2: then J_toy^2 = 0 EXACTLY, per-copy separation 2 (also
  repairing F-2: 2 m_n >= n^{3/2}), the padded variants' J-datum is
  UNTOUCHED (every sealed J-bracket preserved), kernel + chirality
  + first-moment data identical, and with the n-indexed toy radius
  rho_n = 2 sqrt(6n)/ell — sitting strictly above the record band,
  since Gershgorin gives ||J_n||_op <= sqrt(2n), hence record radii
  <= sqrt(6n)/ell, DERIVED with no new citation — the SP-2
  count-law inequality also HOLDS for the padded variants at every
  E (exact rational chain via CLASSICAL pi < 22/7: AT-7). With the
  repair, the §6 forcing covers the n-indexed thresholded class
  INCLUDING the sealed P-2 ceiling and the count law: the
  ceiling-direction forcing claim stands at (better than) its
  stated quantifier.
F-4 (correction, scope-grade; §6 last sentence). "NO SUPER-LINEAR
  FLOOR QUANTIFIED OVER THE LISTED CLASS SURVIVES THE PAIR"
  OVERCLAIMS THE PAIR'S REACH: both padded variants have S^2 >=
  (8/49) m_n ~ (8/49) n^{3/2}; a floor claim is violated by NEITHER
  variant, so the pair (padded or not) refutes NO floor. What the
  pair refutes is two-sided DETERMINATION and every sub-3/2
  CEILING over the class. The floor-direction class-level
  refutation requires a witness with SMALL S^2 at record-shaped
  listed data — supplied here (AT-6b): the ALL-PARALLEL model (all
  grid momenta collinear, distinct radii) is a resolved-form class
  member with excess = 0, i.e. S^2 = J^2 EXACTLY, hence sub-3/2
  whenever the J-datum is (as the record's sealed P-2 bracket
  makes it); scaled direct sums of it inhabit the listed class at
  any n with S^2 = J^2 <= C_Q n^{17/12} < c' n^{3/2} cofinally: no
  class-quantified super-linear floor exists. ALTERNATIVELY the
  artifact's OWN RT-F' leg (sweep-absence of any anti-localization
  carrier) independently carries the floor-side refusal, as it
  correctly displays. Either way the floor-side verdict stands;
  the §6 sentence should attribute the floor-side refutation to
  RT-F'/the parallel witness, not to the pair.
F-5 (observation, reading-guard; §6 class display). The listed class
  names "the ball-overlap Gram MODULI (B diagonal, |B_pp'|, ...)".
  Read as moduli INDEXED BY THE RECORD'S OWN GRID PAIRS (the grid
  being KNOWN after SP-1 — the zeros cubed — with all angles
  computable), the class would DETERMINE the excess exactly and the
  forcing would be false; the witness pair inhabits the class only
  because its two models carry DIFFERENT grids, i.e. the class must
  be read GRID-ABSTRACT (moduli as data not tied to the known
  angular geometry). The artifact's undecidability verdict is safe
  regardless — the indexed-moduli route is blocked TODAY by
  BLOCKER-1' (the moduli values are unlocated at any indexing;
  sw-3 re-confirmed here) — but the class display should pin the
  grid-abstract reading. No repair needed beyond the reading guard;
  successor commissions on O-1-S-B should note that angular
  geometry is KNOWN and it is the MODULI that are missing.
F-6 (observation, quote-fidelity; §1 T-4 line). The c-1 paraphrase —
  see §2 G-4/o-A. Consumed nowhere; the artifact derives no polylog
  gain (CO-2 returns exact 3/2), and the commission demands power
  gamma' in any case. No repair needed in this artifact's chain.
F-7 (cosmetic; §3.1 STEP 1). "upper-triangular" should read
  "lower-triangular" for the displayed deletion (last row + first
  column); determinant, rank bound, and conclusion unchanged.
```

---

## 6. THE COMMISSIONED HUNTS — RESULTS

```text
H-1 A GAMMA-PRIME DEGRADING TO POLYLOG AT THE EXACT EXPONENT:
    NOT FOUND. No gamma' is claimed anywhere (verdict is
    UNDECIDABLE-TODAY, no ceiling sealed); CO-2 returns the EXACT
    power 3/2 bulk with no hidden log (re-derived, AT-8/AT-9); the
    NOT-POLYLOG-ONLY verdict line is accurate — no sub-3/2 gain of
    any size, polylog or power, is derived for S_n^2.
H-2 AN IMPORTED CROSSING LAW THAT EXISTS NOWHERE SEALED: NOT FOUND.
    SP-1 is a DERIVATION from the sealed T-5 tensor bytes (re-built
    independently, R-1..R-3, AT-1..AT-3); the polar closed form is
    therefore lawful ground, not an import. The OVERLAP law the
    ceiling/floor would need (full-range Plancherel-Rotach at the
    zeros / any B_pp' angular law) is DISPLAYED AS THE ABSENT
    DECIDER (O-1-S-B), never consumed: RT-B' correctly refuses the
    kernel route for exactly this reason, and the audit's sweep
    (§8) re-confirms ZERO carriers of "8.22.9"/full-range-PR/
    angular-excess/B_pp content in either root outside the T10SR
    pair itself. The one NEW citation, CL-C (Sturm), is disclosed,
    classical in the strictest sense, member-verified here at
    exact rational grade (AT-10), correctly scoped (blast radius
    SP-2 only), and consumed by no verdict leg.
H-3 A FLOOR WITNESS WITH A RANK, NORMALIZATION, OR QUANTIFIER ERROR
    (THE c-A PATTERN — n-INDEXING OF COUNTERMODELS): FOUND, THREE,
    ALL AT THE DISPLAY/SCOPE GRADE, ALL REPAIRED EXACTLY HERE —
    F-2 (the 8/49 separation constant vs the displayed >= n^{3/2}),
    F-3 (the padded variants' J-datum exits the sealed P-2 bracket;
    J-preserving toy supplied), F-4 (the pair refutes no floor; the
    all-parallel witness supplied; RT-F' independently carries the
    floor side). The witness pair's INTERNAL claims (identities,
    spectra, separation 8/49) are all CONFIRMED (AT-5); the W12'
    rank/normalization bookkeeping itself is exact.
H-4 CONSTANTS THAT ARE NOT n-UNIFORM: NOT FOUND. The SP-2 count law
    is n-uniform with every constant displayed (4, 2, pi, ell);
    CO-1's threshold n >= max(n_1, n_2, 8/C_*) is symbolic and
    cofinite; the SP-3 identity is threshold-free; the O-1-S-B
    yield arithmetic holds for all n >= 1 with constants folded
    (AT-9). The F-1 kernel-column term is bounded by an absolute 4.
H-5 HIDDEN NUMERICS: NOT FOUND. Fence-scan at bytes (§8): every
    decimal-literal hit in the claimed artifact is a section
    reference, a date/time, the sympy version pin, or a sealed
    exponent label (17/12, -1/12); the single "N(" hit is the count
    function N(E), a symbol, not an evaluation call; zero
    evalf/.n()/float( occurrences; zero alpha-adjacent numerics
    (no 137, no 0.007...). The witness rationals (8/49, 16/49,
    45/49, 2, 4) are TOY constants, toy-separated by the builder
    and by this audit; the builder's battery is float-free and its
    displayed output reproduces byte-identically.
```

---
## 7. PER-CLAIM ADJUDICATION AND THE VERDICT

```text
K-1  SP-1 (the polar resolution; sgn_n closed form at the bytes):
     CONFIRMED (R-1..R-3; AT-1/AT-2/AT-3; one cosmetic F-7). The
     of-record blocker sw-2 genuinely MOVES: the artifact's X-2
     cutoff bookkeeping (T-1's absence claim stands at 05:48:15;
     SP-1 is later derivation from bytes the sweep never denied) is
     correct at bytes.
K-2  SP-2 (spectral law + count ceiling, given CL-C): CONFIRMED at
     its conditional grade (R-4; AT-3/AT-9/AT-10). BLOCKER-2's named
     object is genuinely supplied; the builder's own display that it
     does NOT decide (RT-A' tightness + witness) is sound.
K-3  SP-3 (the angular-excess identity, operator form + corollaries
     CO-1..CO-4): CONFIRMED (R-5, R-7; AT-4a/AT-8). The linear
     S_n^2 floor (CO-1) is exact and is correctly NOT claimed as
     the commissioned 3/2 floor.
K-4  SP-3 grid form + the A_n object: CONFIRMED-WITH-CORRECTIONS
     (F-1 — the n-odd zero-momentum column; exact repair displayed;
     all yields survive at power grade).
K-5  W12' (the deeper witness pair, internal claims): CONFIRMED
     (AT-5 independent rebuild — identities, identical listed data,
     S_A^2 = J^2 + 8/49, S_B^2 = J^2 + 16/49).
K-6  The §6 FORCING (undecidability at the resolved byte grade,
     ceiling direction): CONFIRMED-WITH-CORRECTIONS (F-2 constant;
     F-3 the P-2-bracket leak, repaired by the J-preserving toy +
     n-indexed radius, AT-6a/AT-7; F-5 reading guard). With the
     repairs the forcing holds at (better than) the stated
     quantifier.
K-7  The §6 FORCING (floor direction): CONFIRMED-WITH-CORRECTIONS
     (F-4 — the pair carries nothing here; the refusal stands on
     RT-F' sweep-absence, as the artifact itself displays, and now
     also on the audit's all-parallel witness AT-6b).
K-8  RT-A'..RT-F' (the route sweep): CONFIRMED (R-8; each refusal
     display re-derived or re-verified at bytes; RT-C' re-checked
     against the audited CL-4 trap note; RT-E' arithmetic vacuity
     unchanged by SP-1..SP-3).
K-9  §8 O-1-S-B (the decider object + yield chains): CONFIRMED-WITH-
     CORRECTIONS (F-1's "+0" -> "+4" with constants folded, AT-9;
     the double yield through sealed P-2/P-3/T-4 re-checked against
     the sealed displays at bytes, G-1/G-3).
K-10 §9 sweep claims (sw-1..sw-4): CONFIRMED at the audit's own
     later cutoff (§8 below) — occupation, carriers, homonym
     count-probes all reproduce.
K-11 §10 consistency ledger X-1..X-9: CONFIRMED (each contact point
     re-checked at the sealed bytes; X-5's independent kernel
     cross-check reproduced independently at members by AT-3).
K-12 §11 CAS battery: CONFIRMED (verbatim re-run, 10/10 PASS, twice,
     byte-identical to each other AND to the displayed output; the
     disclosed SN2 check-form correction is as described and
     harmless — AT-1 verifies the full Hermiticity content with no
     workaround).
K-13 Gates/fences (§ header, §14): CONFIRMED — no closure claimed,
     no flag flipped, alpha/proof/kappa_record gates false, no
     value frozen, no fenced-class file opened, one output + seal,
     occupation was genuinely empty at its cutoff (sw-1 reproduced).
K-14 TOY_SEPARATION (§13): CONFIRMED CLEAN at the stated
     quantifiers; the witness rationals are toy constants and no
     derived partial consumes a toy premise. (The audit's own toys
     are likewise countermodel/repair-status only.)

VERDICT, PER THE COMMISSION'S MENU, ADJUDICATING THE HEADLINE AT THE
BYTES:

  OVERALL: **CONFIRMED-WITH-CORRECTIONS.**
  THE HEADLINE — UNDECIDABLE-TODAY for O-1-S as commissioned
  (neither the ceiling S_n^2 <= C' n^{3/2 - gamma'}, explicit
  gamma' > 0, nor the floor S_n^2 >= c' n^{3/2} is derivable on the
  sealed stock at the cutoff), with three exact partials SP-1/SP-2/
  SP-3 and the deciding object reduced to the named overlap law
  O-1-S-B — STANDS. The corrections F-1..F-4 (+ observations F-5..
  F-7) are display/scope-grade; every one is repaired exactly
  within this audit; no repair touches the verdict chain, which
  after repair rests on: the W12' pair + the J-PRESERVING padding
  (ceiling direction, now covering P-2-consuming routes); the
  all-parallel witness AND the RT-F' sweep-absence (floor
  direction); the RT-A'..RT-F' refusal displays; and the corpus
  absences (sw-3, re-confirmed at this audit's cutoff). NOT
  REFUTED; not clean CONFIRMED (four real corrections, one of them
  — F-3 — exactly the commissioned c-A-pattern hunt target).
```

---
## 8. THE AUDIT SWEEP AND FENCE-SCAN (cutoff in header; filename/count level for everything unopened)

```text
ROOTS (as commissioned): /Users/bgm/MB Work/alpha-program-archive/
workspace (primary) and /Users/bgm/Documents/New project/
gravity_emergence_evidence_program/
alpha_fundamental_record_action_cleanroom_v003 (cleanroom). Fenced
name classes (register|road_|ledger|lens|plan|tracker|THE_HANDOFF|
continuation) excluded from every opening; no fenced-class file
opened at any point.
KEYS RUN: "T10SR"; "SIGN_CROSSING"; "O-1-S"; "8.22.9" (fixed-string);
"elliptic regime"; "full-range Plancherel"; "overlap law"; "B_pp";
"angular excess".
FINDINGS:
 asw-1 OCCUPATION: T10SR/SIGN_CROSSING carriers in the workspace are
       EXACTLY the claimed artifact, its seal, and this audit file;
       ZERO in the cleanroom. The builder's sw-1 (unoccupied at its
       06:47:00 cutoff) is consistent: the only carriers postdate
       it. Output path was ABSENT at session start (STEP 0) and
       claimed only by this audit.
 asw-2 O-1-S CARRIERS: exactly the T7SR pair + the T10SR pair (the
       claimed artifact and this audit). Reproduces the builder's
       sw-2 with the expected two additions.
 asw-3 OVERLAP/ELLIPTIC CARRIERS: "8.22.9", "elliptic regime",
       "full-range Plancherel", "angular excess", "B_pp": ZERO
       carriers in both roots outside the T10SR pair itself —
       BLOCKER-1' / sw-3 RE-CONFIRMED at this later cutoff: the
       deciding overlap law exists nowhere sealed.
 asw-4 HOMONYMS: "overlap law" hits exactly five workspace artifacts
       (PRIMITIVE_ADDITIVE_RECORD_FIDELITY_ACTION_V001,
       STAGE8_GC2_H1_H2_CAMPAIGN_CODEX2_V001, and three
       STAGE8_TASK5_EQ6_* artifacts) plus their cleanroom mirrors —
       the same five families the builder's sw-4 names. Probed at
       MATCH-COUNT level only (never opened): kappa_n 0, "sgn(" 0,
       "sign(H" 0, "B_pp" 0 in every one — different objects,
       different lanes, exactly as the builder typed them out.
FENCE-SCAN OF THE CLAIMED ARTIFACT (bytes): every decimal-literal
hit inspected: section references (§4.3, §5.1, §8.91, 8.22.6/8.22.9
citation labels), the sympy version pin 1.14.0, dates/times, sealed
exponent labels (17/12, -1/12) — no computational float anywhere;
zero evalf/.n()/float( hits; the single "N(" hit is the spectral
count symbol N(E) at :453, not an evaluation call (inspected at
bytes — a symbolic class label, not a constant); zero alpha-adjacent
numerics (no 137, no 0.007...). The embedded battery is float-free.
FENCE-SCAN OF THIS AUDIT's OWN BATTERY: exact rationals and symbols
only; the two pi-contacts are sp.pi/2 SYMBOLIC (DOI integral, exact)
and the CLASSICAL rational bound pi < 22/7 consumed as pure rational
arithmetic (968 <= 1029 etc.); no floats, no evalf, no .n().
```

Each sentence claims only this displayed sweep at the declared
cutoff.

---

## 9. CHOICE LEDGER, TOY_SEPARATION, FLAG BLOCK (commission T10SR AUDIT)

```text
ACH-1 REPAIR WITNESSES CHOSEN MINIMAL (idempotent-B toy for F-3;
      all-parallel model for F-4): IMMATERIAL(derived) — any
      J-silent separating toy and any zero-angle class member
      serve; minimality is display economy (AT-6). The repairs
      ADD to the builder's forcing; they replace nothing sealed.
ACH-2 THE n-INDEXED TOY RADIUS rho_n = 2 sqrt(6n)/ell (AT-7): one
      unforced constant (any factor > 1 above the derived record
      band sqrt(6n)/ell works); chosen for the cleanest rational
      chain via pi < 22/7. Blast radius: the F-3 repair display
      only; the verdict consumes it nowhere.
ACH-3 pi < 22/7 (Archimedes) AS THE ONE CLASSICAL CONTACT OF THE
      AUDIT'S OWN CHAINS: strictest-sense classical; consumed as
      pure rational arithmetic; used only in AT-7/AT-10 member
      exhibits, never in a verdict leg.
ACH-4 F-1 GRADED CORRECTION (not refutation): FORCED by the
      commission's own standard — the error is bounded (<= 8),
      absent for n even, and every power-law yield survives with
      constants folded; grading it REFUTED would misstate the
      power-grade content.
ACH-5 K-6/K-7 GRADED CONFIRMED-WITH-CORRECTIONS (not REFUTED):
      FORCED by the same standard — the ceiling-direction forcing
      is TRUE over its displayed class as written (variant B alone
      kills any class-quantified sub-3/2 ceiling) and the repairs
      extend it to the thresholded classes; the floor-direction
      REFUSAL is true and independently carried by RT-F'; only the
      ATTRIBUTION sentences err.
CHAIN CHOICE AUDIT: no unforced audit choice enters the adjudication
      chain. CONFIRMED-WITH-CORRECTIONS rests on: the byte-identical
      battery re-runs, the independent battery (10/10 twice), the
      re-derivations R-1..R-8, the findings F-1..F-4 with exact
      repairs, and the sweep — none consumes ACH-1..ACH-3 choices
      beyond exhibit role.

TOY_SEPARATION (self-assessment): CLAIMED CLEAN. AT-1/AT-9 are
all-parameter symbolic; AT-2/AT-3/AT-8/AT-10 are member/instance
exhibits of displayed general facts; AT-4's instances verify an
identity whose general operator proof is displayed (R-5/R-6);
AT-5/AT-6 toys are COUNTERMODEL/REPAIR-status only and assert
NOTHING about the record family's own angular distribution (which
stays undecided in both directions); AT-7's radius is a
construction parameter of a countermodel, ground for nothing. No
value frozen: kappa_n, J_n, S_n, A_n, B_pp', C_*, C_Q, C', c',
C_B'', gamma', gamma_B and all thresholds stay symbols; the audit
rationals (8/49, 16/49, 45/49, 2, 4, 288/1521, 52/1521) are toy
constants. The RULING on this audit is the registrar's.

FLAG BLOCK:
AUDIT_VERDICT = CONFIRMED-WITH-CORRECTIONS( headline
  UNDECIDABLE-TODAY for O-1-S STANDS at the bytes; SP-1 CONFIRMED;
  SP-2 CONFIRMED given CL-C; SP-3 CONFIRMED with F-1 on its grid
  displays; W12' internal claims CONFIRMED; §6 forcing
  CONFIRMED-WITH-CORRECTIONS (F-2/F-3/F-4/F-5, all repaired
  exactly here); RT-A'..RT-F' CONFIRMED; O-1-S-B decider
  CONFIRMED-WITH-CORRECTIONS (F-1 fold); sweeps CONFIRMED and
  re-confirmed at this audit's cutoff; batteries: builder 10/10
  PASS twice byte-identical to display; audit 10/10 PASS twice
  byte-identical. )
CORRECTIONS = FOUR + THREE OBSERVATIONS( F-1 n-odd zero-momentum
  column of §5.2/A_n (bounded <= 8; yields survive; repair
  displayed); F-2 padding separation constant (8/49-grade, not
  >= n^{3/2}); F-3 the c-A-pattern leak — W12' toys' J_toy^2 =
  45/49 exits the sealed P-2 bracket under padding; J-preserving
  repair + count-law verification displayed (AT-6a/AT-7); F-4 the
  pair refutes no floor — all-parallel witness + RT-F' carry the
  floor side; o: F-5 grid-abstract reading guard, F-6 c-1
  paraphrase, F-7 upper/lower-triangular. NONE touches the
  verdict. )
CONSUMPTION_BOUNDARY = NOTHING-FIRED( O-1, O-1-S, MO-4-R all stay
  open; no flag of any prior artifact flips; the claimed artifact's
  own flags stand as sealed with the corrections noted for the
  registrar; whether to commission O-1-S-B (with F-1's convention
  pinned and F-5's reading guard) is the registrar's call. )
SEALS_VERIFIED = 9/9( the claimed artifact + the 8 ground files,
  full-digest sidecar checks before any reliance; §1. )
SWEEP_CUTOFF = 2026-08-15 07:19:00 CDT( §8; occupation = the T10SR
  pair only; overlap-law/elliptic carriers ZERO outside it;
  homonyms count-probed, never opened. )
FORBIDDEN_IMPORTS = none( exact symbolic only; no floats; no
  numeric evaluation; no measured constant; no crossing/overlap law
  imported by builder OR auditor (H-2); no fenced-class file
  opened; no git action; no existing file edited (this artifact
  appended only, plus its seal sidecar); output path probed ABSENT
  at session start and re-probed before seal. )
MACHINERY_INVOKED = yes(CAS) — sympy 1.14.0, fresh venv
  auditvenv_t10sr under the session scratchpad; builder's battery
  extracted verbatim (extraction sha256 59e20b6941c4106df2158a...
  full digest in §4.1), run twice, byte-identical to the displayed
  output; audit battery run twice, byte-identical; both sources
  and outputs in §4 by file-append.
alpha_computed = false ; proof_authorized = false ;
kappa_record_computed = false
ALL_RESULTS = DETERMINED (audit adjudication); the registrar
consumes.
SIGN_CROSSING_AUDIT = SEALED.
```
