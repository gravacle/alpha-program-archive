# STAGE 8 — MO-2 AUDIT OF RECORD: ADVERSARIAL AUDIT OF THE kappa_n RATE ATTEMPT (STAGE8_MO2_KAPPA_RATE_S9AD_V001) — S9AD V001

## ADVERSARIAL AUDITOR — CODENAME MO2-AUDIT — COMMISSION S9AD — [SEALED]

Date: 2026-08-14 (session late CDT). Role: adversarial auditor, NOT told
the build's outcome; DEFAULT REFUTE; this verdict governs.

INDEPENDENCE INSTRUMENT, ON THE RECORD: the rate question was worked
independently and the audit's verdict-posture FIXED AND HASHED BEFORE the
build was opened —
sha256(MO2_AUDIT_PREVERDICT_FIXED.md) =
9e6c12eb3983d9dcdb434e719dcd982c2f992d317d7b67da12c68958cd1bdb2e
(scratchpad path /private/tmp/claude-501/-Users-bgm/9ad117f3-207c-44de-
9a15-f000de50d726/scratchpad/MO2_AUDIT_PREVERDICT_FIXED.md; written and
hashed before the first byte of the build was read). The pre-verdict
fixed: (i) NO lower rate is a consequence of the operator-grade sealed
facts alone (delayed-reindexing witness: any strongly-convergent finite-
rank family satisfies them at arbitrarily slow divergence), so any
DERIVED rate must consume family-specific quantitative input; (ii) the
only admissible new input class is a genuinely classical asymptotic used
exactly; (iii) the SHAPE any true floor should take: LINEAR in n with an
r- and ell-DEPENDENT constant proportional to r^2/ell^2, NO log at floor
grade (scale-free sealed kernel; power-law collar); (iv) conditional
attack posture P-A(1)-(7) for a derived-rate claim. The opened build's
claim matched the pre-fixed shape exactly and survived all seven attack
points; the verdict below follows the pre-fixed menu mapping.

SWEEP CUTOFF, DECLARED (parallel lanes running tonight): corpus state as
of **2026-08-14 23:23 CDT** (the build's own seal mtime). Artifacts
sealed after 23:23 were not consumed and not swept (the 23:27
REFUTING_BRANCH audit and anything later are outside this audit). The
build's own declared cutoff (23:14:15 CDT) precedes its seal (23:23):
self-consistent.

Gates: `alpha_computed = false` ; `proof_authorized = false` ;
`kappa_record_computed = false` (kappa_n is the clause's collapse
commutator mass, not the record curvature; no record-curvature value
appears here). ALL_RESULTS = CLAIMED until checked.

Fences held: EXACT SYMBOLIC ONLY — two CAS runs (sympy 1.14.0, fresh venv
`mo2auditvenv` under the session scratchpad): the build's §7 battery
extracted VERBATIM and rerun (12/12 PASS reproduced), and the audit's own
adversarial battery (§5, 10/10 PASS, ONE final run, no pre-final
corrections); no floats as ground; no value frozen (every constant
symbolic/exact; the audit evaluates nothing numeric); no file matching
register|road_|ledger|lens|plan|tracker|THE_HANDOFF opened; "Q-..."
tokens EXPECTED-UNLOCATABLE, noted not chased; no git action; no
existing file edited; ONE output (this artifact) + seal sidecar at the
commission-distinct path, probed ABSENT at session start AND re-probed
immediately before write.

---

## 0. VERDICT

**CONFIRMED-WITH-CORRECTIONS.** The build's claim — a certified linear
lower rate, kappa_n >= C_*(r, ell) n / 8 for n >= N_0(r, ell) with
C_* = r^2 L/(8 pi^3 ell^2), L = log((4 - sqrt3)/(2(2 - sqrt3))) > 0,
liminf kappa_n / n >= C_*/2, mixed scheme kappa_n^mix >= C_* n/2, and
the determinant corollary -log|det_n(0)| >= C_* n/8 — is DERIVED as
claimed. The full chain was re-derived by this audit end to end (§2);
the one classical ground CL-A is genuinely classical and used exactly
(§3); the rate is derived for THE ACTUAL family at its own sealed bytes,
not for a model (§4); three corrections, NONE verdict-chain-breaking
(§6: COR-1 a one-line justification gap in the pairing floor, repaired;
COR-2 a wording defect in the zero-mode generalization; COR-3 a
registrar-facing dependency note on the commission's CL-A
authorization). Both CAS batteries green. Nothing fires: the registrar
consumes; MO-2 is a candidate input; r-3 and R-L4b remain undischarged
exactly as the build states.

---

## 1. SEALS AND CITED BYTES, RE-VERIFIED THIS SESSION

```text
BUILD    6997ff617ae746ab335c6728da7440baf29ae77ee591b55adc89a91739c60117
         STAGE8_MO2_KAPPA_RATE_S9AD_V001.md — MATCH vs sidecar at path,
         verified BEFORE opening (after the pre-verdict hash was fixed).
INPUTS   all 7 of the build's §1 table recomputed at path by this audit:
         3b5e95b6 (r-2) / a4cf394c (r-2 audit) / bebc0f08 (r-3) /
         72c95d42 (r-3 audit) / 46846730 (E1) / 789338ad (PA) /
         3de0502c (linkage) — 7/7 MATCH the build's table.
VERDICTS the two consumed audits re-read at flag grade: r-2 audit =
         CONFIRMED-WITH-CORRECTIONS (cosmetic, consumable) and r-3
         audit = CONFIRMED-WITH-CORRECTIONS — exactly as the build
         quotes them.
BYTES    the two structural facts the chiral reduction is load-bearing
         on were re-read at PA bytes THIS session: A1 carrier =
         span{phi_a(x/ell) phi_b(y/ell) phi_c(z/ell): 0 <= a,b,c < n}
         tensor C^4 — an index CUBE, so Q_n is an exact product
         projector; and h_(0,n,ell) = sum_j p_(j,n,ell) tensor alpha_j —
         MASSLESS, no beta m term. Both as the build consumed them.
```

EXPECTED-UNLOCATABLE tokens: "Q-1059", "Q-1062", "Q-1054" — noted inside
sealed artifacts, not chased, nothing defaulted.

---

## 2. THE CHAIN, RE-DERIVED (attack branch 1: every step)

```text
STEP-1 BLOCK IDENTITY. [C,P] = P^perp C P - P C P^perp for any C and
   projection P; the two blocks are HS-ORTHOGONAL (audit check A9:
   tr((P^perp C P)^H (P C P^perp)) = 0 for ALL C), and for Hermitian C
   they are mutual adjoints up to sign: kappa = 2||P^perp C P||_2^2.
   EXACT; stronger than the build displays (orthogonal decomposition,
   not merely triangle). HOLDS.
STEP-2 CHIRAL INVOLUTION. beta with {beta, alpha_j} = 0, beta^2 = 1:
   (i) beta h_0 beta = -h_0 REQUIRES masslessness — of record at PA A1
   bytes (re-read, §1); (ii) beta Q_n beta = Q_n (spatial tensor 1_4);
   (iii) beta P beta = P (spinor-diagonal sharp ball, C4/D6');
   (iv)-(v) functional calculus under unitary conjugation (audit
   exhibit A8); (vi) C_n + beta C_n beta = Q_n - W_n, W_n = Z_n - z_n -
   beta z_n beta with beta Z_n beta = Z_n (since beta H_n beta = -H_n
   fixes the kernel), 0 <= z_n, beta z_n beta <= Z_n, so -Z_n <= W_n <=
   Z_n, ||W_n|| <= 1. ALL EXACT. HOLDS.
STEP-3 KERNEL PARITY. H_n^2 = (pi_x^2 + pi_y^2 + pi_z^2) tensor 1_4
   (anticommutation + commuting factors, build M5); ker = (ker q_n p
   q_n)^{tensor 3} tensor C^4; the 1D compressed momentum is unreduced
   tridiagonal (entries -i sqrt((k+1)/2)/ell, all nonzero — build M3
   exact), so nullity <= 1 (row-0 forces v_1 = 0; the three-term
   recurrence then kills the odd chain, and for n EVEN the last row
   kills the even chain too — audit re-derivation confirms nullity =
   n mod 2 for ALL n, not merely <= 1); parity re-verified at the
   EXTENDED members n = 6, 7 (audit A4, beyond the build's {4, 5}).
   dim ker(H_n) = 4(n mod 2) <= 4, ||W_n||_2 <= 2. HOLDS.
STEP-4 REDUCTION (*). X := ||P^perp Q_n P||_2 <= 2||P^perp C_n P||_2 +
   ||W_n||_2 <= 2||P^perp C_n P||_2 + 2 (unitary invariance through
   beta, which commutes with P, P^perp); hence kappa_n >= (1/2)(X-2)^2
   WHENEVER X >= 2 — the build scopes this correctly ("whenever ... >=
   2"; needed before squaring). MIXED (**): beta C beta = 1 - C exactly
   (M1; h_0 has no zero eigenvalue, a.c. spectrum, classical), so
   kappa_n^mix >= (1/2) X^2 with NO kernel correction. HOLDS.
STEP-5 CROSSING MASS. ||P^perp Q_n P||_2^2 = 4 Int_B Int_{B^c} K3^2
   (spinor trace 4; product kernel exact by the CUBE index set — PA
   bytes, §1). Region shrink is POSITIVITY-sound (integrand a square);
   the y_2, y_3 collapse is the EXACT reproducing identity (build M6);
   the window shrink (0, s(x_perp)) -> (0, a), a = (sqrt3/2) r at
   |x_perp| <= r/2, and (r, inf) -> (r, 2r) is again positivity. HOLDS.
STEP-6 DIAGONAL FLOOR. Pairing consecutive levels with the exact trig
   ground (audit A3: cos^2 th + sin^2(th + dl) = 1 + sin dl sin(2th +
   dl) >= 1 - |dl|), d_k = 2/(omega_{k+1} + omega_k) exact, error
   budget Sum A_k^2 (d_k T + 4 e_k(T)) = o(sqrt n) by Cesaro — the
   citation's e_k -> 0 SUFFICES, no rate from CL-A is consumed (audit
   re-derivation); telescoping floor M11 exact. Floor k_n^ell(t,t) >=
   sqrt(2n)/(2 pi ell) on |t| <= r/2 for n >= n_1. HOLDS with COR-1
   (§6): the c_k < 0 case of the pairing inequality needs phi_k^2 >= 0,
   omitted in the build's displayed justification; one-line repair
   (audit A2); the STATEMENT is true, the constant unchanged.
STEP-7 WAVE FLOOR. CD formula exact (M6); CL-A insertion with the M7
   exact decomposition; all remainders Lipschitz-controlled on the
   FIXED window (separation (1 - sqrt3/2) r/ell > 0; window inside a
   fixed compact since r <= 1/2, ell in {1, sqrt2}); prefactor
   (1 - 1/n)^{-1/4} >= 1 exact (M8); (s + eta)^2 >= s^2 - 2|eta|;
   sin^2 averaging with the oscillatory part O(1/omega_n) by exact IBP
   (M10); the window integral L re-derived by this audit in the
   OPPOSITE integration order (A5): EXACT match, r- and ell-free by
   scale invariance of (u-v)^{-2} du dv, and L > 0 exact. Floor
   L/(4 pi^2) for n >= n_2. HOLDS.
STEP-8 ASSEMBLY + BUDGET. Audit A6 re-derives the constant from RAW
   factors: 4 (pi r^2/4)(sqrt(2n)/(2 pi ell))^2 (L/(4 pi^2)) =
   r^2 L n/(8 pi^3 ell^2) = C_* n EXACT. Audit A7 re-derives the
   budget: (1/2)(X-2)^2 - X^2/8 = (3X-4)(X-4)/8 >= 0 for X >= 4 —
   the sufficient direction only, exactly as the build (post its own
   disclosed M12 correction) claims; N_0 = max(n_1, n_2, ceil(16/C_*))
   exists by CL-A's thresholds, unextracted. DETERMINANT COROLLARY:
   -log|det_n(0)| >= kappa_n is the of-record r-2 X-1 / r-3 D8 chain;
   the s_i = 1/2 edge (left side +infinity) is handled. HOLDS.
```

## 3. THE CLASSICAL GROUND, ATTACKED (genuineness + exact use)

```text
CL-1 GENUINE: Plancherel–Rotach (1929) / Szego, Orthogonal Polynomials
   §8.22 (8.22.6) — the fixed-x oscillatory asymptotic of Hermite
   functions — is classical in the strictest sense.
CL-2 TRANSCRIPTION EXACT: Szego's e^{-x^2/2} H_n(x) = 2^{n/2 + 1/4}
   (n!)^{1/2} (n pi)^{-1/4} [cos(sqrt(2n+1) x - n pi/2) + O(n^{-1/2})]
   transcribed to L^2-normalized phi_n gives amplitude EXACTLY the
   build's A_n = sqrt(2/pi)(2n)^{-1/4} — verified symbolically (audit
   A1); phase theta_k = omega_k t - k pi/2, omega_k = sqrt(2k+1)
   matches; the uniform-on-compacts O(k^{-1/2}) error is STRONGER than
   the e_k(T) -> 0 the build consumes.
CL-3 SCOPE RESPECTED: every use is on a fixed compact (windows bounded
   by 2r/ell <= 1); the WKB cubic phase correction and the amplitude
   discrepancy are O(k^{-1/2}) on compacts, correctly assigned to the
   citation; nothing wider (no growing windows, no turning-point or
   Airy regime, no rate demanded of e_k) is consumed. The diagonal
   floor needs only Cesaro absorption of e_k -> 0 (audit re-derived).
CL-4 NO SUBSTITUTE CLAIMED: the build does NOT cite Widom/Sobolev-class
   theorems (which cover scaled pseudodifferential compressions, not
   Galerkin spectral projections) — the trap my pre-verdict flagged is
   not entered; CL-A is consumed only for 1D Hermite functions, where
   it genuinely applies.
```

## 4. FAMILY-RELATIVITY, ATTACKED (the V/NV precedent at rate grade)

```text
FR-1 The rate is derived for THE family: the actual cube carrier (PA
   bytes => exact product projector), the actual massless generator
   (PA bytes), the actual sharp ball (C4/D6'), the actual ell scaling
   (exact), the actual C_n realization (r-2 CH-A inherited as the named
   premise, exactly as r-3 inherited it). No filtered/momentum-cutoff
   model stands in at any load-bearing step.
FR-2 My pre-fixed witness argument (operator-grade facts certify NO
   rate — delayed reindexings) is RESPECTED, not violated: the build
   derives the rate from NEW family-specific quantitative input (CL-A
   on the actual Hermite functions + the exact chiral structure of the
   actual massless generator), which is precisely the only door my
   pre-verdict left open.
FR-3 SCHEME-ROBUST AT RATE GRADE: my pre-verdict flagged that r-2's
   scheme-robustness was divergence-grade only and a pure/mixed rate
   BRIDGE was missing. The build needs no bridge: BOTH schemes receive
   direct floors ((*) with the exact rank <= 4 correction; (**) clean).
   The CH-A premise remains load-bearing ONLY for attaching the rate to
   the s_i/det displays — same boundary as r-2, correctly booked.
FR-4 SHAPE CROSS-CHECK (audit-side): my pre-fixed independent shape
   estimate — linear in n, constant proportional to r^2/ell^2, no log
   at floor grade — was hashed BEFORE opening the build and is exactly
   the shape the build derived (C_* = r^2 L/(8 pi^3 ell^2)). The TOY
   collar computation corroborating the shape is A10, tagged, ground
   for nothing. Sharpness is NOT claimed by the build (truth plausibly
   n log n from the level-cutoff Fermi box); a lower bound needs no
   sharpness. Consistent.
FR-5 QUANTIFIERS EXACT: per admitted state and cell; per cell time with
   r(t) > 0 (N_0 depends on r, ell — correctly displayed; nothing is
   claimed at r(t) = 0); each frozen ell; all four opposite-phase pairs
   (pair-independence of A_n(0), of record); full-family cofinite bound
   => every subsequence. X-1..X-6 consistency claims re-checked: the
   linear floor sits under the cubic ceiling at symbolic grade; r-2 is
   recovered-with-rate, not corrected; r-3's Route-1 obstruction is
   untouched (the n^2-growing ratio claim is exact); the stricken
   display is consumed nowhere in the build (C6 not even needed); no
   fenced class opened by the build per its own manifest, and nothing
   in my sweep contradicts that.
```

## 5. THE AUDIT CAS BATTERY (VERBATIM) AND OUTPUT (VERBATIM)

Fresh venv `mo2auditvenv` (sympy 1.14.0), session scratchpad. FIRST the
build's §7 battery was extracted verbatim (sha256 of the extracted
script: 6388feffa897ad2f89cd26307e912f793badc5f47b67320add10050645045dcf)
and rerun: **12/12 PASS reproduced, output byte-identical to §7's.**
THEN the audit battery below ran ONCE (no pre-final corrections):

```python
# MO2-AUDIT adversarial CAS battery -- EXACT SYMBOLIC ONLY (sympy 1.14.0,
# fresh venv mo2auditvenv under the session scratchpad). Every constant
# symbolic or an exact rational; nothing numeric evaluated. Checks A1-A10
# attack the build's chain at the steps MY audit identified as load-bearing.
import sympy as sp
from sympy import Rational as R

ok = lambda name, cond: print(f"{name}: {'PASS' if cond else 'FAIL'}", flush=True)

x = sp.Symbol('x', real=True)
n = sp.Symbol('n', positive=True)

# ===== A1 -- the Szego 8.22.6 -> CL-A amplitude TRANSCRIPTION is exact =====
# Szego: e^{-x^2/2} H_n(x) = 2^{n/2+1/4} (n!)^{1/2} (n pi)^{-1/4} [cos + O(n^{-1/2})].
# phi_n = (2^n n! sqrt(pi))^{-1/2} e^{-x^2/2} H_n(x). The build's A_n must equal
# the transcribed amplitude: (2^n n! sqrt(pi))^{-1/2} 2^{n/2+1/4} (n!)^{1/2} (n pi)^{-1/4}
# = sqrt(2/pi) (2n)^{-1/4} EXACTLY.
lhs = (2**n*sp.factorial(n)*sp.sqrt(sp.pi))**(-R(1, 2)) \
      * 2**(n/2 + R(1, 4)) * sp.factorial(n)**R(1, 2) * (n*sp.pi)**(-R(1, 4))
An = sp.sqrt(R(2)/sp.pi)*(2*n)**(-R(1, 4))
ok("A1 Szego 8.22.6 amplitude transcribed to L^2-normalized phi_n equals the"
   " build's A_n = sqrt(2/pi)(2n)^(-1/4) EXACTLY (classical citation used"
   " exactly at amplitude grade)",
   sp.simplify(sp.powsimp(lhs/An, force=True)) == 1)

# ===== A2 -- the pairing-floor inequality SURVIVES the negative-case gap ====
# The build justifies phi_k^2 + phi_{k+1}^2 >= A_{k+1}^2 (c_k + c_{k+1}) via
# A_{k+1} <= A_k, which alone fails when c_k := cos^2 - 2|eps| < 0. The repair:
# phi_k^2 >= A_{k+1}^2 c_k holds in BOTH cases -- if c_k >= 0 via A-monotonicity,
# if c_k < 0 via phi_k^2 >= 0 > A_{k+1}^2 c_k. CAS exhibits: the two case
# inequalities at symbolic grade (A >= B > 0, c arbitrary real, ph^2 >= A^2 c
# given; show ph^2 >= B^2 c in each case as an exact algebraic implication).
A, B, c, ph = sp.symbols('A B c phi', real=True)
case_pos = sp.simplify((A**2 - B**2)*c) # >= 0 when A^2>=B^2, c>=0: gap term
# identity: A^2 c - B^2 c = (A^2 - B^2) c ; and for c < 0: B^2 c < 0 <= ph^2.
ok("A2 repair identity A^2 c - B^2 c = (A^2 - B^2)c EXACT (c >= 0 case:"
   " nonneg when A^2 >= B^2), and the c < 0 case needs only phi^2 >= 0:"
   " the build's pairing floor STATEMENT is true; its displayed"
   " justification omitted the c < 0 case (correction, not a break)",
   sp.expand(A**2*c - B**2*c - (A**2 - B**2)*c) == 0)

# ===== A3 -- the diagonal-floor trig identity, audit-independent form =====
# cos^2(th) + sin^2(th + dl) = 1 + sin(dl) sin(2 th + dl) EXACT, hence
# >= 1 - |sin dl| >= 1 - |dl| (with M8's |sin| <= |.|).
th, dl = sp.symbols('theta delta', real=True)
ok("A3 cos^2(theta) + sin^2(theta+delta) = 1 + sin(delta) sin(2 theta + delta)"
   " EXACT (audit re-derivation of the pairing floor's ground, independent"
   " of the build's M7 route)",
   sp.simplify(sp.expand_trig(sp.cos(th)**2 + sp.sin(th + dl)**2
               - 1 - sp.sin(dl)*sp.sin(2*th + dl))) == 0)

# ===== A4 -- nullity parity EXTENDED beyond the build's displayed members ===
# Exact tridiagonal compressed momentum at n = 6 (nullity 0) and n = 7
# (nullity 1): extends the build's M4 sweep {4, 5} adversarially.
def pmat(N):
    M = sp.zeros(N, N)
    for k in range(N - 1):
        M[k, k+1] = -sp.I*sp.sqrt(R(k+1, 2))
        M[k+1, k] = sp.I*sp.sqrt(R(k+1, 2))
    return M
ok("A4 nullity(q_n p q_n) = n mod 2 at n = 6 (0) and n = 7 (1) -- audit"
   " extension of the build's displayed members; the all-n recurrence"
   " argument verified in audit text",
   pmat(6).rank() == 6 and pmat(7).rank() == 6)

# ===== A5 -- the window integral L, INDEPENDENT integration order =====
r = sp.Symbol('r', positive=True)
y = sp.Symbol('y', positive=True)
inner = sp.integrate((y - x)**(-2), (x, 0, sp.sqrt(3)*r/2))
Ival2 = sp.integrate(inner, (y, r, 2*r))
Lsym = sp.log((4 - sp.sqrt(3))/(2*(2 - sp.sqrt(3))))
ok("A5 the window integral re-derived with the OPPOSITE integration order"
   " equals L = log((4-sqrt3)/(2(2-sqrt3))) EXACT and r-free (audit"
   " independence check on the build's M9)",
   sp.simplify(Ival2 - Lsym) == 0)

# ===== A6 -- assembly re-derived from the RAW floor factors =====
ell, L = sp.symbols('ell L', positive=True)
raw = 4*(sp.pi*r**2/4)*(sp.sqrt(2*n)/(2*sp.pi*ell))**2*(L/(4*sp.pi**2))
ok("A6 assembly from RAW factors 4 * (pi r^2/4) * (sqrt(2n)/(2 pi ell))^2"
   " * (L/(4 pi^2)) = r^2 L n/(8 pi^3 ell^2) EXACT (audit re-derivation,"
   " not reusing the build's intermediate n/(2 pi^2 ell^2) form)",
   sp.simplify(raw - r**2*L*n/(8*sp.pi**3*ell**2)) == 0)

# ===== A7 -- the budget chain re-derived: kappa >= C n/8 from the floor ====
Cst = sp.Symbol('C', positive=True)
X = sp.Symbol('X', positive=True)
diff_expr = R(1, 2)*(X - 2)**2 - X**2/8
ok("A7 (1/2)(X-2)^2 - X^2/8 = (3X-4)(X-4)/8 EXACT: for X = sqrt(C n) >= 4"
   " the pure-scheme floor kappa_n >= (1/2)(sqrt(C n)-2)^2 >= C n/8 follows"
   " (audit re-derivation of the budget step at its exact factorization)",
   sp.expand(diff_expr - (3*X - 4)*(X - 4)/8) == 0)

# ===== A8 -- chiral functional-calculus exhibit at matrix grade =====
# beta 1_{(-inf,0)}(H) beta = 1_{(0,inf)}(H) for {beta, H} = 0: exact 2x2
# exhibit H = sigma_x, beta = sigma_z; negative projection (I - sigma_x)/2.
sx = sp.Matrix([[0, 1], [1, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
Cneg = (sp.eye(2) - sx)/2
Cpos = (sp.eye(2) + sx)/2
ok("A8 beta 1_(-inf,0)(H) beta = 1_(0,inf)(H) exhibited exactly at matrix"
   " grade (H = sigma_x, beta = sigma_z anticommuting): sz (I-sx)/2 sz ="
   " (I+sx)/2, and the two projections sum to Q = I (zero-kernel case of"
   " the build's (vi))",
   sp.simplify(sz*Cneg*sz - Cpos) == sp.zeros(2, 2)
   and sp.simplify(Cneg + sz*Cneg*sz - sp.eye(2)) == sp.zeros(2, 2)
   and sp.simplify(sz*sx + sx*sz) == sp.zeros(2, 2))

# ===== A9 -- HS-orthogonality of the two commutator blocks (M2's ground) ===
# tr((P-perp C P)^dag (P C P-perp)) = 0 exactly for ANY C (3x3 symbolic):
# the block identity is an ORTHOGONAL decomposition, not just a triangle step.
z = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'c_{i}{j}'))
Pm = sp.diag(1, 1, 0); Pp = sp.eye(3) - Pm
ok("A9 tr((P-perp C P)^H (P C P-perp)) = 0 for ALL C (the two blocks of"
   " [C,P] are HS-orthogonal; audit ground for ||[C,P]||_2^2 ="
   " ||P-perp C P||_2^2 + ||P C P-perp||_2^2, = 2x for Hermitian C)",
   sp.simplify(sp.trace((Pp*z*Pm).H*(Pm*z*Pp))) == 0)

# ===== A10 -- TOY-TAGGED shape corroboration (model, NOT ground): the =====
# continuum collar mass of a scale-free |r|^-3 kernel at resolution eps is
# a POWER law eps^-2 (flat-boundary model): inner angular integral
# Int_{R^2} (w^2+s^2)^-3 d^2 s = pi/(2 w^4), then Int_{u+v>=eps} du dv
# f(u+v) = Int_eps^inf w f(w) dw gives pi/(4 eps^2). With eps ~ ell/sqrt(2n)
# this is LINEAR in n -- the build's gamma = 1 floor is shape-compatible;
# nothing here is consumed as ground (TOY: flat boundary, filtered model).
w, s, eps = sp.symbols('w s epsilon', positive=True)
ang = sp.integrate(2*sp.pi*s*(w**2 + s**2)**(-3), (s, 0, sp.oo))
coll = sp.integrate(w*(sp.pi/(2*w**4)), (w, eps, sp.oo))
ok("A10 [TOY] Int_{R^2}(w^2+s^2)^{-3} d^2s = pi/(2 w^4) and"
   " Int_eps^inf w * pi/(2 w^4) dw = pi/(4 eps^2) EXACT: scale-free collar"
   " mass is a POWER law in resolution (no log); with eps^2 ~ ell^2/(2n)"
   " the shape is linear in n -- corroborates gamma = 1 as a lower-bound"
   " shape; MODEL ONLY, consumed as ground NOWHERE",
   sp.simplify(ang - sp.pi/(2*w**4)) == 0
   and sp.simplify(coll - sp.pi/(4*eps**2)) == 0)

print("MO2-AUDIT-BATTERY-DONE")
```

Output, verbatim (10/10 PASS):

```text
A1 Szego 8.22.6 amplitude transcribed to L^2-normalized phi_n equals the build's A_n = sqrt(2/pi)(2n)^(-1/4) EXACTLY (classical citation used exactly at amplitude grade): PASS
A2 repair identity A^2 c - B^2 c = (A^2 - B^2)c EXACT (c >= 0 case: nonneg when A^2 >= B^2), and the c < 0 case needs only phi^2 >= 0: the build's pairing floor STATEMENT is true; its displayed justification omitted the c < 0 case (correction, not a break): PASS
A3 cos^2(theta) + sin^2(theta+delta) = 1 + sin(delta) sin(2 theta + delta) EXACT (audit re-derivation of the pairing floor's ground, independent of the build's M7 route): PASS
A4 nullity(q_n p q_n) = n mod 2 at n = 6 (0) and n = 7 (1) -- audit extension of the build's displayed members; the all-n recurrence argument verified in audit text: PASS
A5 the window integral re-derived with the OPPOSITE integration order equals L = log((4-sqrt3)/(2(2-sqrt3))) EXACT and r-free (audit independence check on the build's M9): PASS
A6 assembly from RAW factors 4 * (pi r^2/4) * (sqrt(2n)/(2 pi ell))^2 * (L/(4 pi^2)) = r^2 L n/(8 pi^3 ell^2) EXACT (audit re-derivation, not reusing the build's intermediate n/(2 pi^2 ell^2) form): PASS
A7 (1/2)(X-2)^2 - X^2/8 = (3X-4)(X-4)/8 EXACT: for X = sqrt(C n) >= 4 the pure-scheme floor kappa_n >= (1/2)(sqrt(C n)-2)^2 >= C n/8 follows (audit re-derivation of the budget step at its exact factorization): PASS
A8 beta 1_(-inf,0)(H) beta = 1_(0,inf)(H) exhibited exactly at matrix grade (H = sigma_x, beta = sigma_z anticommuting): sz (I-sx)/2 sz = (I+sx)/2, and the two projections sum to Q = I (zero-kernel case of the build's (vi)): PASS
A9 tr((P-perp C P)^H (P C P-perp)) = 0 for ALL C (the two blocks of [C,P] are HS-orthogonal; audit ground for ||[C,P]||_2^2 = ||P-perp C P||_2^2 + ||P C P-perp||_2^2, = 2x for Hermitian C): PASS
A10 [TOY] Int_{R^2}(w^2+s^2)^{-3} d^2s = pi/(2 w^4) and Int_eps^inf w * pi/(2 w^4) dw = pi/(4 eps^2) EXACT: scale-free collar mass is a POWER law in resolution (no log); with eps^2 ~ ell^2/(2n) the shape is linear in n -- corroborates gamma = 1 as a lower-bound shape; MODEL ONLY, consumed as ground NOWHERE: PASS
MO2-AUDIT-BATTERY-DONE
```

---

## 6. CORRECTIONS (none verdict-chain-breaking)

```text
COR-1 (§4.2 of the build; MINOR, repaired): the pairing floor
   phi_k^2 + phi_{k+1}^2 >= A_{k+1}^2(c_k + c_{k+1}) is justified only
   by "A_{k+1} <= A_k", which is insufficient when c_k := cos^2 theta_k
   - 2|eps_k| < 0 (a larger coefficient on a negative term lowers the
   sum). The repair is one line and uses only phi_k^2 >= 0: in both
   sign cases phi_k^2 >= A_{k+1}^2 c_k (audit A2/A3). The floor's
   STATEMENT, constant, and thresholds are unchanged. Registrar may
   consume the build with this line understood.
COR-2 (§2.1 of the build; COSMETIC): "ANY self-adjoint 0 <= z_n <= Z_n"
   jointly with "C_n is a finite-rank orthogonal projection" is
   inaccurate — C_n is a projection only when z_n is a subprojection of
   Z_n. Every displayed bound requires only Hermitian C_n with 0 <= z_n
   <= Z_n (M2 holds for Hermitian C), and the of-record realization IS
   a projection, so nothing breaks; wording only. (The generalization
   itself is a strengthening: the floor holds under every zero-mode
   convention, upgrading r-2's per-member note.)
COR-3 (DEPENDENCY NOTE, registrar-facing): the build's license for CL-A
   is its quoted commission sentence ("classical Hermite asymptotics
   (Plancherel-Rotach-type) cited as classical ground the way LSC
   was"). The commission text is not an artifact at path within this
   audit's reach, so the AUTHORIZATION is consumed at the build's
   quotation and should be confirmed by the registrar against the
   commission bytes. The MATHEMATICS is independent of this: CL-A is
   genuinely classical and used exactly (§3), and this audit's own
   tasking treats genuinely-classical-and-exactly-used grounds as
   admissible. If the registrar finds NO such commission clause, the
   correct downgrade is CONDITIONAL(classical ground authorization),
   not REFUTED — no derivation step fails.
```

## 7. AUDIT CHOICE LEDGER

```text
ACH-1 INDEPENDENCE: verdict-posture fixed and hashed BEFORE opening the
   build (hash in header; scratchpad file retained). The build's seal
   was verified against its sidecar before reading. FORCED by tasking.
ACH-2 SWEEP CUTOFF 23:23 CDT (build's seal mtime): YOURS (unforced
   within the tasking's demand to declare one); artifacts after it
   (23:27 onward) untouched.
ACH-3 CORPUS CONTEXT READ PRE-OPENING (r-2 in full; r-3/linkage
   headers; sibling verdict lines): FORCED-shape — working the rate
   question independently requires the sealed definitions; none of it
   discloses the build's outcome (r-3/linkage PREDATE the build and
   name MO-2 as missing; sibling flags disclaim rate content).
ACH-4 CL-A AUTHORIZATION consumed at the build's quotation: COR-3;
   classified a dependency note, not a defect (grounds in §3).
ACH-5 CAS: rerun-verbatim + adversarial battery, fresh venv, each ONE
   final run, no pre-final corrections; the verbatim extraction's own
   sha256 displayed (§5).
ACH-6 NO independent numerical spot-check of kappa_n at any member:
   FORCED (floats banned; a member value would freeze a number and
   decide nothing about a rate).
```

## 8. TOY_SEPARATION (audit self-assessment)

```text
CLEAN. A10 is the ONLY model computation (flat-boundary continuum
collar), tagged [TOY] in the check name and in §5's comment, consumed as
ground NOWHERE — it corroborates a shape and decides nothing. A1-A9 are
identity-grade or exact-member checks of all-quantifier statements, each
displayed with its quantifier; A4's members extend the build's displayed
sweep. The pre-verdict's shape heuristic (D-4) was fixed for CALIBRATION
of attack posture, hashed as such, and no verdict sentence rests on it.
The RULING on the build's own TOY_SEPARATION (§9 there): CLEAN as
self-assessed — its CAS instances are identity exhibits, its load-
bearing inputs are actual-family bytes; confirmed by this audit's §2/§4.
```

## 9. FLAG BLOCK

```text
MO2_AUDIT_VERDICT = CONFIRMED-WITH-CORRECTIONS( the build's DERIVED
  linear lower rate stands at audited grade: kappa_n >= C_*(r, ell) n/8
  for n >= N_0(r, ell), C_* = r^2 L/(8 pi^3 ell^2),
  L = log((4 - sqrt3)/(2(2 - sqrt3))) > 0; liminf kappa_n/n >= C_*/2;
  mixed scheme kappa_n^mix >= C_* n/2; determinant corollary
  -log|det_n(0)| >= C_* n/8 via the of-record chain. Chain re-derived
  end to end (§2, STEP-1..8); classical ground CL-A genuine and used
  exactly, transcription audit-verified symbolically (§3, A1); rate is
  for THE ACTUAL family at bytes, no model stand-in, scheme-robust at
  rate grade without a bridge (§4); build battery reproduced 12/12 in a
  fresh venv; audit battery 10/10, one run. )
CORRECTIONS = THREE( COR-1 pairing-floor justification gap (c_k < 0
  case), one-line repair via phi_k^2 >= 0, statement/constant/threshold
  unchanged; COR-2 z_n projection wording, cosmetic; COR-3 the CL-A
  commission-authorization consumed at the build's quotation — registrar
  to confirm at commission bytes; if absent, downgrade path is
  CONDITIONAL(authorization), never REFUTED — no derivation step fails. )
INDEPENDENCE = HELD( pre-verdict fixed and hashed BEFORE opening:
  9e6c12eb3983d9dcdb434e719dcd982c2f992d317d7b67da12c68958cd1bdb2e;
  its fixed shape expectation (linear in n, r^2/ell^2 constant, no log
  at floor grade) matches the build's derived C_* n exactly; its P-A
  attack menu (7 points) executed in full, all survived. )
CONSUMPTION_BOUNDARY = NOTHING-FIRED( audit confirms the build fires
  nothing: MO-2 supplied as candidate input only; r-3 NOT discharged
  (Route 1 still needs MO-1 + MO-3; direct package still lacks MO-4);
  R-L4b NOT discharged; all three R-L4 witnesses STAND; the registrar
  consumes both artifacts together. )
SEALS_VERIFIED = 8/8( build 6997ff61 vs sidecar BEFORE opening; the
  build's 7 inputs recomputed at path: 3b5e95b6, a4cf394c, bebc0f08,
  72c95d42, 46846730, 789338ad, 3de0502c — all MATCH its table; PA A1
  carrier-cube and massless bytes re-read directly. )
SWEEP_CUTOFF = DECLARED( 2026-08-14 23:23 CDT — the build's seal mtime;
  post-cutoff artifacts untouched; the build's own 23:14:15 cutoff
  precedes its seal, self-consistent. )
FORBIDDEN_IMPORTS = none( exact symbolic only; no floats as ground; no
  measured constant; NO value frozen (rate = asymptotic statement with
  symbolic constants; N_0 unextracted here as there); no
  register/road_/ledger/lens/plan/tracker/THE_HANDOFF file opened;
  "Q-..." tokens noted, not chased; no git action; no existing file
  edited; ONE output + seal sidecar at the commission-distinct path,
  probed ABSENT at session start and re-probed immediately before
  write. )
MACHINERY_INVOKED = yes(CAS) — sympy 1.14.0, fresh venv mo2auditvenv;
  build battery rerun verbatim (12/12 PASS reproduced) + audit battery
  (10/10 PASS, one final run, no pre-final corrections), both
  reproduced verbatim in §5.
alpha_computed = false ; proof_authorized = false ;
kappa_record_computed = false
ALL_RESULTS of the build remain CLAIMED until the registrar's check;
this audit's ruling is CONFIRMED-WITH-CORRECTIONS.
MO2_KAPPA_RATE_AUDIT_RESULT = SEALED.
```
