# STAGE 8 — THE ZERO-FREE / NONVANISHING CONTROL ON THE DISCHARGED BASIS: DERIVED CORE, EXACT ZERO LOCATED, GATES REDUCED NOT CLOSED

## BLIND ANALYST — CODENAME ZERO-FREE — [SEALED]

Date: 2026-08-14
Role: BLIND analyst (ZERO-FREE). Derivation attempted BEFORE any authored act:
(1) the volume-uniform zero-free neighborhood demanded at V011 :1232-1233
(flag :2184 false) — worked from the discharged chain's unitarity-pinned rate
and the exact slab closed forms, with the simultaneous-vanishing condition
worked exactly and the small-omega marginality region handled honestly;
(2) F'-14 Route B's analytic content — analyticity and nonvanishing of the
N_surv-normalized summed determinant on the closed pair polydisc, with the
normalization derived exactly. Honest outcomes equal citizens; if content is
derivable no spec act is needed for it (the Q-1041 lesson), and what is not
derivable is named exactly with the act that remains.

Gates: `alpha_computed = false` ; `kappa_record_computed = false` ;
`proof_authorized = false`. ALL_RESULTS = CLAIMED until checked.

Fences held: EXACT SYMBOLIC ANALYSIS ONLY — the one script is exact symbolic
CAS identity verification (sympy 1.14.0, fresh venv `zfvenv`), reproduced in
full in §7 with output verbatim; NOTHING numeric evaluated, every constant
symbolic or an exact rational/surd. No physical quantity computed, bounded
numerically, or evaluated. No scale, imported GR, or faithfulness authority.
M(t) sharp (jumps retained exactly); equal-time FALSE by C6 (the omega = 0
slice used below is the sealed bookkeeping intermediate of record, R2 §4, not
a certification). No register/tracker/plan/road/ledger/lens file read. Output
name probed before write: ABSENT. No git action.

---

## 0. VERDICT IN ONE LINE

**The zero-free demand's analytic MECHANISM is now derived on the discharged
basis, its one genuine zero located EXACTLY, and the demand REDUCED — but not
discharged. Per slab the amplitude vanishes iff omega = 0 AND cos(Om T) = 0
(the exact identity Om^2|A|^2 = omega^2 + mu^2 cos^2(Om T)); for the full
sealed profile the omega = 0 slice has exactly ONE zero per non-trivial
branch, at lambda = ±sqrt2, |x| = 2^(-5/4) — interior, genuine. That zero
NEVER enters the objects the existence path consumes: the lambda-weighted sum
equals 1/2 EXACTLY at the zero, and on the surviving sector the CTP pair
cancels the in-cell dressing at a = 0 (V(0) = I exact), so the baseline
determinant never sees it — NO neighborhood choice and NO new act is needed
for the marginality region. The normalized summed determinant's nonvanishing
region has the exact form |Z_hat| >= 1 - kappa_bal·x·e^x > 0 on
{x e^x < 1}, with the normalization derived exactly (N_surv(0) = 1/2, c
weights (1/2, 1/8, 1/8, 1/8, 1/8), kappa_bal = 1; the ALL-pairs weight total
is |m_0|^2 = 0 — the sum vanishes at leading order BY DESIGN, which is what
makes normalization mandatory). What is NOT derivable from the discharged
basis: the carrier/volume-uniform finiteness of the input x — per-pair it is
REFUTED (52f2490b), and the discharged summed HS bound canNOT be substituted,
for two exact reasons: the determinant sum is per-pair-first (weights outside
the dets), and the surviving-sector restriction BREAKS the m_0 product
factorization the discharged kill runs on. The zero-free gate and Route B's
nonvanishing therefore collapse onto the ALREADY-NAMED gates (summed-S2' spec
act + R-L4a/b + the F'-14 passage): no new obstruction, no new act.**

---

## 1. SEALS VERIFIED AT PATH (shasum -a 256), BEFORE ANY RELIANCE

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`. Every digest
recomputed from bytes at path THIS session; all match sidecars and tasked
prefixes.

```text
df4514a5b807cbc903465505ad896ffb6e72c7ab9f891a4541226d18398a7034  STAGE8_G1_KERNEL_CERTIFICATE_V001.md         MATCH (G1; tasked df4514a5)
3534ca534709a3c8ac591994a9ae650224a8594b3f1a8b2a96494a69ab9653e6  STAGE8_G1_KERNEL_CERTIFICATE_CHECK_V001.md   MATCH (G1-CHK; tasked 3534ca53)
2e4e5163bb5b9c06078890fc573dd149905975b55860dcabcc7050fb1aa02666  STAGE8_REMAINDER_UNIFORMITY_V001.md          MATCH (REM; tasked 2e4e5163)
89641f762d35c0e6d3c8fb0475e2de742663f9dcf9f08a44621b059c2bd927ec  STAGE8_REMAINDER_UNIFORMITY_CHECK_V001.md    MATCH (REM-CHK; tasked 89641f76)
a7969f0c3a42112ee300f73617494fb77c2a415bf5b6cf4d33598c6b6c8bf9cf  STAGE8_R2_RESUMMATION_V001.md                MATCH (R2; tasked a7969f0c)
a4f2e1b7878139afd017abe5fb62c6af7bf19836f7f162ef62902265bfc03cb5  STAGE8_R2_RESUMMATION_CHECK_V001.md          MATCH (R2-CHK; tasked a4f2e1b7)
468467303a109dc825b015107897dacc107800fc981030377c3f006b384cccb5  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md  MATCH (E1; tasked 46846730)
0a10c0305d4cde8b226d844ed0fb9289f393b670e02b144bf762dd49c853c9c4  STAGE8_ASSEMBLY_QUANTIFIER_V001.md           MATCH (AQ; tasked 0a10c030)
331035d393695519eaa061a343abb67129a8ea48fcc47a765daaef1883b0aa22  STAGE8_ASSEMBLY_QUANTIFIER_CHECK_V001.md     MATCH (AQ-CHK; tasked 331035d3)
aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a  evaluator_build_A/inputs/evidence/aa7c6d49...--BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md  MATCH (V011 sealed member)
```

UNVERIFIABLE-AT-PATH NOTE (bookkeeping, consistent with G1 §1): the
working-tree `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` has NO
`.seal.sha256` sidecar and recomputes to 20a3a17d... — DRIFTED from the
manifest digest. Every V011 citation below is read from the SEALED evidence
member aa7c6d49 (where the tasked line numbers land exactly: the zero-free
clause at :1232-1233, the flag at :2184). The drifted working-tree copy is
not relied on.

Sealed content read at path this session and relied on below:
V011(aa7c6d49) :1217-1233 (the derived amplitude Z_h(A) = a_h(A)/a_h(0),
Z_h(0) = 1; "The remaining connected theory must prove a volume-uniform
zero-free neighborhood for the derived amplitude"), :1253-1258 (Gamma
monoidal additivity), :2184 (volume_uniform_zero_free_neighborhood_proved =
false); E1 :660-674 (the Carleman displays; F'-14: the log of a sum is not a
sum of logs, witness SCAD_COLOR_SUM_LOG_MISUSE), :687-689 (the polydisc
quantifier: sups over states, colour pairs on the surviving sector, the
closed pair polydisc at radius eps), :745-762 (R.2 sector algebra: V(0) - 1
= (phase_mu phase_lambda - 1)P; same-phase V(0) = I exactly; weight
bookkeeping S_+ = 1/2, S_- = -1/2), :766-790 (R-L4a/R-L4b uncertified),
:794-800 (kappa_bal = 1 from surviving weights), :835-848 (R.3 colour-sum
closure: Z_hat = sum c rho, c = w*w det(1+A(0))/N_surv(0), sum c = 1,
sum|c| = kappa_bal; R.3.a/R.3.b); R2 §3-§4 + flag block (the slab closed
form A = cos(Om T) + i omega sin(Om T)/Om, |A|^2+|B|^2 = 1, V4a-V4h; the
omega = 0 slice A_lambda = cos(lambda Theta), Theta = tau_R(1-16 rho^4);
the weighted sum c(th) = (1-cos(sqrt2 th))/2, g = cos^2(8 pi rho^4); m_0 =
m_1 = 0); REM :266-311 (the rate chain: |A_lambda - 1| <= C_rate(x)
lambda^2/omega, all-orders Volterra-IBP, unitarity-pinned; the trivial l1
bound |sigma^rem| <= 2 for small omega), :445-519 (estimate-grade typing
e-i/e-ii, overturn conditions), :352-383 (dominated a-series on the closed
polydisc, carrier-uniformity = ||Pi X Pi||_2 <= ||X||_2); AQ §2.3 (the
summed-S2' is the spec author's act), §4 (F'-14 Route A closed / Route B
unsealed: "certified analyticity/nonvanishing of the N_surv-normalized
summed determinant on the closed pair polydisc"), §5 (the three-item gate);
G1 §2-§5 (the gate list of record; B-L2* discharged; F'-14 + summed-S2' +
OBL-D open).

---

## 2. THE SEALED DEMANDS, LOCATED EXACTLY

```text
D-1  V011(aa7c6d49) :1232-1233: "The remaining connected theory must prove a
     volume-uniform zero-free neighborhood for the derived amplitude."
     Context :1217-1231: the derived amplitude is the NORMALIZED primitive
     completed-record amplitude Z_h(A) = a_h(A)/a_h(0), Z_h(0) = 1 — the
     neighborhood is in SOURCE space around A = 0, its radius uniform in
     volume (the existence path needs Gamma = -log|A| finite; for disjoint
     cells Gamma is additive, :1253-1258, so a volume-shrinking neighborhood
     fails the many-cell object). Flag :2184:
     volume_uniform_zero_free_neighborhood_proved = false.
D-2  F'-14 ROUTE B (AQ §4.3, sealed shape): "a NEW derivation controlling
     Log Z_comp directly — certified analyticity/nonvanishing of the
     N_surv-normalized summed determinant on the closed pair polydisc,
     bounds obtained on the SUM without per-pair logs."
     The object (E1 :835-845): Z_hat_comp(a) = sum_surv c_{mu lambda}
     rho_{mu lambda}(a), c = w_mu^* w_lambda det(1+A(0))/N_surv(0),
     N_surv(0) = sum_surv w_mu^* w_lambda det(1+A_{mu lambda}(0)).
     Polydisc quantifier E1 :687-689: closed pair polydisc at radius eps,
     sups over states and surviving colour pairs.
```

---

## 3. ITEM 1 — THE ZERO-FREE NEIGHBORHOOD, DERIVED AS FAR AS THE BASIS REACHES

### 3.1 The simultaneous-vanishing condition, exact (the slab)

The sealed slab closed form (R2 V4a, re-verified §7 Z1): on any interval of
length T with constant coupling mu,

```text
  A = cos(Om T) + i omega sin(Om T)/Om ,   Om = sqrt(omega^2 + mu^2),
  |A|^2 + |B|^2 = 1  exactly (Z1a).
```

THE MODULUS IDENTITY (new, exact, CAS Z1b):

```text
  Om^2 |A|^2 = omega^2 + mu^2 cos^2(Om T).
```

The right side is a sum of squares of REAL quantities. Therefore, exactly:

```text
  A = 0   <=>   omega = 0   AND   cos(Om T) = cos(mu T) = 0
          <=>   omega = 0   AND   mu T in pi/2 + pi Z.
```

(The task's two conditions cos(Om T) = 0 and omega sin(Om T)/Om = 0 collapse
to this: cos = 0 forces |sin| = 1, so the second condition forces omega = 0.)
Equivalently the UNITARITY FLOOR (Z1c):

```text
  |A|^2 = omega^2/Om^2 + mu^2 cos^2(Om T)/Om^2  >=  omega^2/(omega^2 + mu^2),
```

so EVERY slab of the sealed profile is zero-free on {omega > 0} with the
explicit x-free, carrier-free, volume-free lower bound |A| >= omega/Om. With
the sealed coupling cap mu <= sqrt2 sup_t v = sqrt2 · 4 tau_R = 4 pi (Z13),
the floor is |A| >= omega/sqrt(omega^2 + 16 pi^2) uniformly over every slab,
every cell, every carrier — a volume-uniform zero-free statement, DERIVED,
for the slab amplitudes. The candidate zeros are EXACTLY the points
{omega = 0, mu T in pi/2 + pi Z}.

### 3.2 The full profile at omega = 0: the genuine zero, located exactly

At omega = 0 the two-level Hamiltonian commutes at different times and the
amplitude is exact (R2 §2.4(c1)/V4e, the sealed omega = 0 slice):

```text
  A_lambda(x, 0) = cos(lambda Theta(rho)),   Theta = tau_R (1 - 16 rho^4),
  rho = |x| in [0, 1/2],  tau_R = pi/sqrt2.
```

For lambda = ±sqrt2: lambda Theta = ±pi (1 - 16 rho^4) (Z3b). Zeros on the
closed ball (Z4a/Z4b, exact solve on u = 1 - 16 rho^4 in (0, 1]):

```text
  cos(pi u) = 0 on (0,1]  <=>  u = 1/2  <=>  16 rho^4 = 1/2
  <=>  rho = rho* = 2^(-5/4)   — INTERIOR (2^(-5/4) < 2^(-1), Z4c).
```

**THE CANDIDATE ZERO IS REALIZED**: the per-lambda amplitude A_{±sqrt2} has a
genuine zero in the closed symbol domain, at the single interior radius
rho* = 2^(-5/4), on the omega = 0 edge (the massless marginality region of
record, exactly where the rate bound C lambda^2/omega is empty). The
lambda = 0 branch is A = 1 identically (Z4d). This is the honest answer to
the small-omega question: unitarity + the closed form do NOT exclude zeros
there — they LOCATE one, exactly.

Transversality at the zero (exact, §7 Z7-Z9): the first-order-in-omega
formula, verified against the closed form on the slab (Z8a = Z8b),

```text
  dA/d omega |_{omega=0} = i [ sin(Phi) int_0^1 sin(2 phi(t)) dt
                             + cos(Phi) int_0^1 cos(2 phi(t)) dt ] ,
  phi(t) = lambda int_0^t v~,  Phi = lambda Theta.
```

At the zero cos(Phi) = 0, sin(Phi) = ±1 and 2 phi runs monotonically over
[0, ±pi] (Z5b: sqrt2 Theta(rho*) = pi/2 exactly), so sin(2 phi) is
single-signed and not identically zero (Z8c): Im dA/d omega is STRICTLY
one-signed (positive for both lambda = +sqrt2 and -sqrt2). Together with
dA/d rho |_(rho*,0) = 2^(9/4) pi != 0 (Z9) and Im A(rho, 0) = 0 identically,
the Jacobian of (rho, omega) -> (Re A, Im A) at the zero is nondegenerate:
the zero is ISOLATED — it does not propagate into omega > 0 locally. (A
quantitative neighborhood radius is not extracted here; none is needed, by
§3.4.)

### 3.3 Where the rate bound bites (the large-omega region), volume-uniform

The discharged chain's unitarity-pinned rate (REM :277-296, estimate-grade
e-i, overturn conditions as sealed): |A_lambda(x, omega) - 1| <=
C_rate(x) lambda^2/omega with C_rate a functional of the frozen profile only
— no volume, no carrier, no cellulation datum. Hence

```text
  |A_lambda| >= 1 - C_rate(x) lambda^2/omega > 0   on omega > C_rate(x) lambda^2,
```

a volume-uniform zero-free region for every branch (lambda^2 <= 2). The slab
instance carries the whole chain in closed form: |A_int - 1| <=
(mu^2/omega)(T/2 + 1/2) (REM R5, standing on Z1e). DERIVED. The gap between
this region and §3.2's exact slice — the finite-omega interior — is where
nothing on the discharged basis bounds the PER-LAMBDA amplitude below, and
where a per-lambda zero-free claim would be an overreach; §3.4 shows the
consumed objects never need one.

### 3.4 Why the genuine zero never reaches the derived amplitude

Two exact cancellations stand between the per-lambda zero and every object
the existence path (Gamma = -log|A|) consumes:

```text
(i)  THE WEIGHTED SUM DOES NOT VANISH THERE. At the zero (rho*, omega = 0):
       sum_l w_l cos(lambda_l Theta(rho*)) = (1/2)·1 + (-1/4)·0 + (-1/4)·0
                                           = 1/2  EXACTLY (Z5c; = g(rho*) =
       cos^2(8 pi rho*^4) = cos^2(pi/4) = 1/2, Z5d).
     The lambda = ±sqrt2 branches vanish TOGETHER at rho*, and the weight
     mass transfers entirely to the lambda = 0 branch. The weighted sum's
     own omega = 0 zeros are ONLY at the ball boundary rho = 1/2 (Z6a: no
     interior root of cos(pi u) = 1 on u in (0,1]; Z6b: Theta(1/2) = 0),
     where it vanishes because m_0 = 0 — the BY-DESIGN vanishing (Z6c: off
     the record support the weighted sum is m_0 · (free phase) = 0
     identically). The weight-summed amplitude is therefore NOT the
     zero-free object and was never going to be: the object that can be
     zero-free is the NORMALIZED one — exactly the object V011 :1225-1226
     already names (Z_h(0) = 1) and Route B normalizes (§4).
(ii) THE CTP PAIR CANCELS THE DRESSING AT BASELINE. On the surviving sector
     the sealed R.2 algebra gives V_{mu lambda}(0) = I EXACTLY (E1 :745-756;
     phase_mu phase_lambda = 1, Z10d): the in-cell record dressings of the
     two CTP branches cancel at a = 0, BEFORE any norm or determinant. The
     per-lambda zero at (rho*, 0) is a zero of the SINGLE-BRANCH dressed
     symbol; it never appears in the baseline pair object — the baseline
     determinant is det(1 + A(0)) with A(0) the C-L2 commutator error only,
     = 1 up to that error. The zero can re-enter only through the source
     difference Delta(a) on the polydisc — i.e., through the SAME majorant
     x(C, eps) that gates everything else (§4.3).
```

CONSEQUENCE: the omega = 0 marginality region creates NO independent
zero-free obstruction and requires NO neighborhood choice — the zero's
location is exactly known and exactly cancelled in every consumed object.
The opposite-phase sector is the opposite case: 1 + A(0) = 1 - 2 CPC has
eigenvalues 1 - 2 sigma_i which HIT ZERO at sigma = 1/2 (Z12) — that sector
is handled by EXCLUSION (R-L4b, uncertified obligation), never by a
zero-free bound; nothing here touches it.

### 3.5 Verdict on item 1

```text
DERIVED (exact, on the discharged basis):
  (a) the simultaneous-vanishing condition and the modulus identity
      Om^2|A|^2 = omega^2 + mu^2 cos^2(Om T); slab zero-freeness on
      {omega > 0} with the volume/carrier-free floor |A| >= omega/Om,
      mu <= 4 pi;
  (b) the complete omega = 0 zero set of the full profile: the single
      interior zero per non-trivial branch at rho* = 2^(-5/4), lambda =
      ±sqrt2; its transversality (isolated, nondegenerate Jacobian);
  (c) the rate-bound zero-free region omega > C_rate(x) lambda^2,
      volume-uniform;
  (d) the two exact cancellations (weighted sum = 1/2 at the zero; V(0) = I
      pair cancellation) that keep the zero out of the derived amplitude;
  (e) the REDUCTION: the volume-uniform zero-free neighborhood for the
      NORMALIZED derived amplitude is implied by the polydisc perturbation
      bound |Z_hat(a) - 1| <= kappa_bal x e^x < 1 (§4.2) — i.e., the
      zero-free demand REDUCES EXACTLY to the carrier/volume-uniform
      finiteness of x(C, eps). No new act, no neighborhood choice.
NOT DERIVED (the sealed demand as a whole): the demand's quantitative input
  x carrier/volume-uniform is NOT on the discharged basis — per-pair it is
  REFUTED (52f2490b: no admissible M), and §4.3 shows exactly why the
  discharged summed bound cannot be substituted without the spec act.
VERDICT: NOT-DERIVABLE as a discharge — REDUCED to the already-named gates
  (the summed-S2'/Route B spec act + R-L4a/b + the C-L2/G_cm input), with
  the analytic mechanism, the exact zero, and the no-new-act determination
  DERIVED. Flag :2184 stands false; flipping is the Gate-6 evaluator's.
```

---

## 4. ITEM 2 — ROUTE B'S ANALYTIC CONTENT: WHAT IS DERIVED, WHAT OBSTRUCTS

### 4.1 Analyticity, stated exactly

```text
(a) SYMBOL LEVEL (the discharged chain's own level): each per-lambda
    amplitude A_lambda(x, omega) is ENTIRE in omega — every Dyson term
    A^(n) is a finite integral of e^{-2 i omega (excursion duration)} over
    a compact simplex (entire in omega), and the series is dominated
    termwise by (sqrt2 Theta)^n/n! UNIFORMLY in omega (sealed, R2 §2.3), so
    the sum converges locally uniformly. Slab amplitudes are entire in
    closed form; finite slab products and the finite lambda-weighted sum
    are entire. EXACT.
(b) SOURCE LEVEL, FIXED CARRIER n: the entries of V_{mu lambda, n}(a) are
    entire in (a_+, a_-) (time-ordered exponential, source entering
    linearly in the generator; finite carrier), A_{mu lambda, n}(a) =
    C_n(V(a) - 1)C_n is finite-rank analytic, det(1 + A_{mu lambda, n}(a))
    is entire on C^2, and Z_comp,n(a) = sum_{mu lambda} w_mu^* w_lambda
    det(1 + A_{mu lambda, n}(a)) is a FINITE sum (9 pairs; 5 surviving) of
    entire functions: ENTIRE. On the closed pair polydisc the a-series of
    the assembled object is dominated (REM §3.5, sealed). EXACT at fixed n.
(c) THE CARRIER LIMIT, PER PAIR: NOT available — per-pair
    sup_n ||Delta_n(a)||_2 = +infinity of record (52f2490b), so the
    per-pair determinants have NO uncompressed limit object on the sealed
    basis; only the n-indexed family exists. Any Route B statement is
    therefore about the FIXED-n family with n-uniform bounds — and the
    n-uniform input is exactly the missing x (§4.3).
```

### 4.2 The normalization and the nonvanishing region, derived exactly

THE BY-DESIGN VANISHING, made exact (Z10b): if every pair determinant took
its record-free value 1, the summed object would be

```text
  sum_{mu,lambda} w_mu^* w_lambda · 1 = |sum_l w_l|^2 = |m_0|^2 = 0
```

— the UNNORMALIZED all-pairs sum vanishes at leading order BY DESIGN (the C4
kill). The sum survives ONLY through the sector split: on same-phase pairs
V(0) = I exactly (det = 1, up to the C-L2 error); on opposite-phase pairs
R-L4b demands det = 0 identically. Hence, at the C-L1 collapse level and
conditional on R-L4a/b:

```text
  Z_comp(0) = sum_surv w_mu^* w_lambda = S_+^2 + S_-^2 = 1/2 = N_surv(0)
  (Z10c/Z10f; the excluded sector's weight total is the missing -1/2, Z10c),
  c_{mu lambda} = w_mu^* w_lambda / N_surv(0):
      c_{00} = 1/2,  c at the four (±sqrt2, ±sqrt2) pairs = 1/8 each (Z10f),
  sum_surv c = 1,   sum_surv |c| = kappa_bal = 1  (all c > 0; Z10g),
  Z_hat(0) = 1 EXACTLY.
```

THE NONVANISHING REGION (the perturbation-of-1 mechanism, exact):
wherever the per-pair majorant chain holds — |Log rho_{mu lambda}(a)| <=
x(C, eps) on the surviving sector (R.3.a) — the elementary coefficientwise
inequality |e^z - 1| <= e^{|z|} - 1 <= |z| e^{|z|} (Z11a: u e^u - (e^u - 1)
has series coefficients (n-1)/n! >= 0) gives |rho(a) - 1| <= x e^x, and the
triangle inequality gives, on the closed pair polydisc:

```text
  |Z_hat(a) - 1| <= sum_surv |c| · sup |rho - 1| <= kappa_bal · x e^x ,
  |Z_hat(a)|     >= 1 - kappa_bal · x e^x  > 0    on  { kappa_bal x e^x < 1 },
```

with kappa_bal = 1. On that region Log Z_hat is defined and analytic (Z_hat
entire at fixed n, zero-free), and Gamma = -Log Z_hat obeys the sealed R.3.b
form. THE ZERO-FREE NEIGHBORHOOD OF THE NORMALIZED SUMMED DETERMINANT IS
EXACTLY {x(C, eps) e^{x(C, eps)} < 1} — derived, with x the one named input.
Note this is per-pair-INPUT but sum-level-OUTPUT: no per-pair log is applied
to the sum; F'-14 is honored by construction (the assembly is of rho's).

### 4.3 The exact obstruction

```text
(o-1) THE INPUT x IS NOT ON THE DISCHARGED BASIS. x(C, eps) is built from
      the PER-PAIR S2/G_hs majorants; carrier-uniformly these are REFUTED
      (52f2490b: no admissible M; the two-time survivor's HS norm scales
      with the carrier volume). At fixed carrier n the chain closes with
      x_n finite but n-DEPENDENT — the volume/carrier-uniform neighborhood
      {x e^x < 1} then shrinks with n, which is exactly what D-1 forbids.
(o-2) THE DISCHARGED SUMMED BOUND CANNOT BE SUBSTITUTED, for two exact
      structural reasons:
      (i) PER-PAIR-FIRST: Z_comp is a sum of per-pair DETERMINANTS — the
          weights stand OUTSIDE the nonlinear det. The discharged chain
          controls the weight-summed OPERATOR (the sum inside the HS norm).
          No sealed display, and no identity derivable here, converts
          control of || sum w^* w Delta ||_2 into control of
          sum w^* w det(1 + A) without per-pair inputs.
      (ii) THE SECTOR RESTRICTION BREAKS THE m_0 FACTORIZATION: the
          discharged kill runs on the FULL product sum
          sum_{mu,lambda} w_mu^* w_lambda f(mu) g(lambda)
          = (sum w f)(sum w g) — with m_0 = 0 annihilating the low strata.
          The surviving-sector sum restricts to phase_mu = phase_lambda,
          and sum_{same-phase} w_mu^* w_lambda f(mu) g(lambda) does NOT
          factor (the restriction couples mu to lambda). The c-weighted
          object of §4.2 therefore does not inherit the discharged
          carrier-uniform bound. This is the same one wall in a second
          dress: the summed-S2' act (colour sum inside the norm, C4 kill
          before the norm, R.3 re-derived compatibly with F'-14) is the
          named repair — AQ §2.3(iii), the spec author's, not a lane's.
(o-3) R-L4a/R-L4b remain uncertified obligations that DEFINE the surviving
      sum (which pairs are in it, and that the excluded sector's
      determinants vanish identically rather than take values). Both are
      consumed by §4.2's "conditional on" and are not dischargeable here
      (they need the named regularization act at the divergent trace).
```

### 4.4 Verdict on item 2

```text
ROUTE_B_ANALYTIC = PARTIAL.
DERIVED (exact): analyticity at the symbol level and at fixed carrier
  (finite sums/products of entire functions, dominated a-series on the
  closed polydisc); the by-design leading vanishing |m_0|^2 = 0 of the
  all-pairs sum (normalization mandatory, not optional); the normalization
  EXACTLY (N_surv(0) = 1/2 at the collapse level; c = (1/2, 1/8 x 4);
  kappa_bal = 1); the nonvanishing region in exact form:
  |Z_hat| >= 1 - x e^x > 0 on {x e^x < 1}, F'-14-compliant by construction.
NOT DERIVED: the carrier/volume-uniformity of the input x — per-pair
  refuted, summed substitute structurally blocked (o-2), the one named act
  the summed-S2' spec amendment; and R-L4a/b (the sector-defining
  obligations, a regularization act at the divergent trace).
```

---

## 5. WHAT OF F'-14 ROUTE B REMAINS AFTER THIS DERIVATION — THE QUANTIFIER, SEPARATED HONESTLY

Even with §4.2's analytic content in hand, Route B is NOT thereby passed.
The separation, exactly:

```text
ANALYTIC CONTENT (derivable, and here derived in mechanism): entirety at
  fixed carrier; Z_hat(0) = 1; the perturbation-of-1 nonvanishing on
  {kappa_bal x e^x < 1}; Gamma = -Log Z_hat analytic there. What remains
  analytic-side is ONE input: x carrier/volume-uniform at the summed-
  compatible quantifier (o-1/o-2) — content-shaped, but sitting behind an
  unsealed estimate that no lane may write.
QUANTIFIER CONTENT (the spec author's act, irreducibly):
  (q-1) WHICH OBJECT the Route B statement quantifies over — the per-pair
        determinants exist only as the fixed-n family (§4.1(c)); the spec
        must say whether Route B's nonvanishing is claimed for the
        n-indexed family with n-uniform constants, or for a summed limit
        object it must first DEFINE (sum-then-limit vs limit-then-sum; the
        per-pair limit does not exist of record).
  (q-2) THE SUMMED-S2' ESTIMATE ITSELF — placing the colour sum inside the
        Schatten-2 norm with the C4 kill before the norm, and re-deriving
        the R.3 chain around it compatibly with F'-14 (AQ §2.3(iii) names
        this an E1-successor spec amendment in so many words).
  (q-3) THE RETIREMENT of witness SCAD_COLOR_SUM_LOG_MISUSE: F'-14 is a
        validity bar, "passed or violated" — adopting §4.2's construction
        as THE compliant passage (and its eps, its sup order, its sector
        exclusion citing R-L4a/b) is adoption into the spec, not a lane
        derivation. This artifact exhibits the candidate; it does not and
        may not adopt it.
```

The Q-1041 custody line, applied honestly: the MECHANISM proved derivable
here needs no spec act (and none is requested for it); the INPUT x at the
right quantifier and the QUANTIFIER itself were already the named spec-act
debts (DEBT 2 / DEBT 3 of record) — this derivation narrows what the act
must contain (only the estimate and the adoption; the analytic scaffolding
around it is now on paper), it does not remove the act.

---

## 6. NET — WHICH GATES MOVE

```text
GATE (V011 :1232-1233 / flag :2184, volume-uniform zero-free neighborhood):
  NOT closed. REDUCED: mechanism derived, the one genuine zero located at
  (lambda = ±sqrt2, rho* = 2^(-5/4), omega = 0) and shown cancelled in
  every consumed object (weighted sum = 1/2 there; V(0) = I at baseline on
  the surviving sector); NO neighborhood choice needed; remaining content
  IDENTICAL to the already-named gates (x carrier-uniform at the summed-
  compatible quantifier + R-L4a/b). No new obstruction found; no new act
  created.
GATE (F'-14 Route B): NOT closed. Its analytic content is now PARTIAL-
  derived (§4); its remaining content is the summed-S2' estimate + the
  quantifier adoption (§5, q-1..q-3) + R-L4a/b. Route A stays closed as
  architected; the witness stands.
UNMOVED: B-L2* stays DISCHARGED as certified (G1); the per-pair refutation
  (52f2490b) stays untouched; OBL-D rides the transport package; all V011
  flags stay as sealed — no flag is flipped by this artifact (GOV-F).
STRENGTH: everything above at identity-grade where CAS-verified (35/35),
  estimate-grade-with-declared-conditions where it consumes the sealed rate
  chain (e-i/e-ii, overturn conditions as sealed in REM §5), and
  conditional-as-marked where it consumes R-L4a/b or the C-L2 error input.
```

---

## 7. THE SCRIPT (exact symbolic verification; reproduced in full) AND OUTPUT

Run with sympy 1.14.0 (fresh venv `zfvenv`). Exact symbolic identity
verification only; nothing numeric evaluated; all constants symbolic or
exact rationals/surds.

```python
# ZERO-FREE: exact symbolic verification of the load-bearing identities.
# EXACT SYMBOLIC ONLY: matrix/trig/integral/series identities over symbols;
# nothing numeric evaluated; all constants symbolic or exact rationals/surds.
import sympy as sp

ok = lambda name, cond: print(f"{name}: {'PASS' if cond else 'FAIL'}")

om = sp.symbols('omega', nonnegative=True)
mu, T = sp.symbols('mu T', positive=True)
rho = sp.symbols('rho', nonnegative=True)
th = sp.symbols('theta', real=True)
tt = sp.Symbol('tt', real=True)
u_ = sp.symbols('u_', real=True)
nn = sp.symbols('nn', integer=True, positive=True)
lam_v = [sp.Integer(0), sp.sqrt(2), -sp.sqrt(2)]
w_v = [sp.Rational(1, 2), sp.Rational(-1, 4), sp.Rational(-1, 4)]
tauR = sp.pi/sp.sqrt(2)
rho_star = 2**sp.Rational(-5, 4)

# ---------- Z1: slab closed form, unitarity, the exact modulus identity ----------
Om = sp.sqrt(om**2 + mu**2)
A = sp.cos(Om*T) + sp.I*om*sp.sin(Om*T)/Om     # sea-sea (sealed R2 V4a)
B = -sp.I*mu*sp.sin(Om*T)/Om                   # interband (only |B| enters)
ok("Z1a |A|^2 + |B|^2 = 1 exactly (unitarity, re-run)              ",
   sp.simplify(sp.expand_trig(A*sp.conjugate(A) + B*sp.conjugate(B) - 1)) == 0)
ok("Z1b Om^2 |A|^2 = omega^2 + mu^2 cos^2(Om T)  (modulus identity) ",
   sp.simplify(Om**2*A*sp.conjugate(A) - (om**2 + mu**2*sp.cos(Om*T)**2)) == 0)
ok("Z1c |A|^2 - om^2/Om^2 = mu^2 cos^2(Om T)/Om^2  (unitarity floor)",
   sp.simplify(A*sp.conjugate(A) - om**2/Om**2 - mu**2*sp.cos(Om*T)**2/Om**2) == 0)
ok("Z1d om = 0 slice of the slab: A = cos(mu T)                     ",
   sp.simplify(A.subs(om, 0) - sp.cos(mu*T)) == 0)
ok("Z1e Om - om = mu^2/(Om + om)  (the rate chain's pin, re-run)    ",
   sp.simplify(Om - om - mu**2/(Om + om)) == 0)

# ---------- Z2: the simultaneous-vanishing condition (sum of real squares) ----------
# From Z1b: Om^2|A|^2 = omega^2 + (mu cos(Om T))^2, a sum of squares of REAL
# quantities: A = 0 iff omega = 0 AND cos(Om T) = 0 (mu > 0). Witness both parts:
ok("Z2a at omega = 0 and mu T = pi/2: A = cos(pi/2) = 0 (zero realized)",
   sp.simplify(A.subs({om: 0, T: sp.pi/(2*mu)})) == 0)
ok("Z2b for omega > 0: |A|^2 >= om^2/Om^2 > 0 (difference is a square) ",
   sp.simplify(A*sp.conjugate(A) - om**2/Om**2
               - (mu*sp.cos(Om*T)/Om)**2) == 0)

# ---------- Z3: the sealed profile and the per-lambda phase ----------
prof = sp.integrate(32*tt**3, (tt, rho, sp.Rational(1, 2))) \
     + sp.integrate(32*(1-tt)**3, (tt, sp.Rational(1, 2), 1-rho))
ok("Z3a Theta(rho)/tau_R = int_rho^{1-rho} 32 min(t,1-t)^3 dt = 1-16 rho^4",
   sp.simplify(prof - (1 - 16*rho**4)) == 0)
ok("Z3b lambda Theta = pi (1-16 rho^4) at lambda = sqrt2               ",
   sp.simplify(sp.sqrt(2)*tauR*(1 - 16*rho**4) - sp.pi*(1 - 16*rho**4)) == 0)

# ---------- Z4: the genuine zero of the per-lambda amplitude at omega = 0 ----------
zs_perlam = sp.solveset(sp.cos(sp.pi*u_), u_, domain=sp.Interval.Lopen(0, 1))
ok("Z4a cos(pi u) = 0 on u in (0,1] iff u = 1/2                        ",
   zs_perlam == sp.FiniteSet(sp.Rational(1, 2)))
zs_rho = sp.solveset(sp.Eq(1 - 16*rho**4, sp.Rational(1, 2)), rho,
                     domain=sp.Interval.Ropen(0, sp.Rational(1, 2)))
elems = list(zs_rho)
ok("Z4b u = 1 - 16 rho^4 = 1/2 on [0,1/2) iff rho = 2^(-5/4) (interior)",
   len(elems) == 1 and sp.simplify(elems[0] - rho_star) == 0)
ok("Z4c 16 rho*^4 = 1/2 exactly; rho* < 1/2 (exponent -5/4 < -1)       ",
   sp.simplify(16*rho_star**4 - sp.Rational(1, 2)) == 0
   and sp.Rational(-5, 4) < -1)
ok("Z4d lambda = 0 branch: A = 1 identically (never zero)              ",
   sp.cos(sp.Integer(0)*th) == 1)

# ---------- Z5: the lambda-weighted sum at the candidate zero ----------
c_th = (1 - sp.cos(sp.sqrt(2)*th))/2
wsum = sum(w*sp.cos(l*th) for w, l in zip(w_v, lam_v))
Theta_star = tauR*(1 - 16*rho_star**4)
ok("Z5a sum_l w_l cos(l th) = c(th) = (1-cos(sqrt2 th))/2 (re-run)     ",
   sp.simplify(wsum - c_th) == 0)
ok("Z5b Theta(rho*) = tau_R/2 ; sqrt2 Theta(rho*) = pi/2               ",
   sp.simplify(Theta_star - tauR/2) == 0
   and sp.simplify(sp.sqrt(2)*Theta_star - sp.pi/2) == 0)
ok("Z5c THE WEIGHTED SUM AT THE PER-LAMBDA ZERO = 1/2 EXACTLY (not 0)  ",
   sp.simplify(wsum.subs(th, Theta_star) - sp.Rational(1, 2)) == 0)
ok("Z5d g(rho*) = cos^2(8 pi rho*^4) = 1/2 (same point via the g-form) ",
   sp.simplify(sp.cos(8*sp.pi*rho_star**4)**2 - sp.Rational(1, 2)) == 0)

# ---------- Z6: the weighted sum's own omega = 0 zeros ----------
zs_wsum = sp.solveset(sp.cos(sp.pi*u_) - 1, u_, domain=sp.Interval.Lopen(0, 1))
ok("Z6a weighted sum zero at om=0 iff cos(pi u)=1: NO root, u in (0,1] ",
   zs_wsum == sp.EmptySet)
ok("Z6b boundary rho = 1/2: Theta = 0 and g(1/2) = cos^2(pi/2) = 0     ",
   sp.simplify(tauR*(1 - 16*sp.Rational(1, 2)**4)) == 0
   and sp.simplify(sp.cos(8*sp.pi*sp.Rational(1, 2)**4)**2) == 0)
ok("Z6c off-support the weighted sum = m_0 = 0 identically (by design) ",
   sp.nsimplify(sum(w_v)) == 0)

# ---------- Z7: the conjugation identity behind the omega-derivative ----------
I2 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
phi_s = sp.symbols('phi_s', real=True)
Urot = sp.cos(phi_s)*I2 + sp.I*sp.sin(phi_s)*sx     # e^{+i phi sigma_1}
Urot_m = sp.cos(phi_s)*I2 - sp.I*sp.sin(phi_s)*sx   # e^{-i phi sigma_1}
conj_id = sp.simplify(sp.expand_trig(
    Urot*sz*Urot_m - (sp.cos(2*phi_s)*sz + sp.sin(2*phi_s)*sy)))
ok("Z7  e^{i phi s1} s3 e^{-i phi s1} = cos(2phi) s3 + sin(2phi) s2   ",
   conj_id == sp.zeros(2, 2))

# ---------- Z8: the first-order-in-omega formula (transversality engine) ----------
dA = sp.simplify(sp.diff(A, om).subs(om, 0))
ok("Z8a dA/dom|_{om=0} = i sin(mu T)/mu  (from the closed form)        ",
   sp.simplify(dA - sp.I*sp.sin(mu*T)/mu) == 0)
first = sp.I*(sp.sin(mu*T)*sp.integrate(sp.sin(2*mu*tt), (tt, 0, T))
              + sp.cos(mu*T)*sp.integrate(sp.cos(2*mu*tt), (tt, 0, T)))
ok("Z8b i[sin(Phi) int sin(2phi) + cos(Phi) int cos(2phi)] = same      ",
   sp.simplify(first - sp.I*sp.sin(mu*T)/mu) == 0)
# at the zero cos(Phi) = 0, sin(Phi) = +1 (lambda = +sqrt2): dA/dom =
# i int_0^1 sin(2 phi(t)) dt with 2 phi in [0, pi] monotone: integrand >= 0,
# > 0 on the open support: STRICTLY POSITIVE imaginary part. (Z5b gives
# phi_total = pi/2 exactly.) sin >= 0 on [0, pi]:
ok("Z8c sin(u) >= 0 on [0, pi]: no root of sin in (0, pi) (interior)   ",
   sp.solveset(sp.sin(u_), u_, domain=sp.Interval.open(0, sp.pi)) == sp.EmptySet
   and sp.sin(sp.pi/2) == 1)

# ---------- Z9: the rho-transversality component at the zero ----------
Az0 = sp.cos(sp.pi*(1 - 16*rho**4))          # A_{sqrt2}(rho, 0)
dAr = sp.simplify(sp.diff(Az0, rho).subs(rho, rho_star))
ok("Z9  dA/drho at (rho*, 0) = 2^(9/4) pi (nonzero; Jacobian nondegen.)",
   sp.simplify(dAr - 2**sp.Rational(9, 4)*sp.pi) == 0)

# ---------- Z10: sector algebra and the exact normalization ----------
phase = [sp.Integer(1), sp.Integer(-1), sp.Integer(-1)]   # phases on (0, +sqrt2, -sqrt2)
m0 = sum(w_v)
m1 = sum(w*l for w, l in zip(w_v, lam_v))
allpairs = sp.nsimplify(sum(w_v[i]*w_v[j] for i in range(3) for j in range(3)))
surv = [(i, j) for i in range(3) for j in range(3) if phase[i] == phase[j]]
opp = [(i, j) for i in range(3) for j in range(3) if phase[i] != phase[j]]
S_surv = sp.nsimplify(sum(w_v[i]*w_v[j] for i, j in surv))
S_opp = sp.nsimplify(sum(w_v[i]*w_v[j] for i, j in opp))
ok("Z10a m_0 = 0, m_1 = 0 (the C4 kill; re-run)                        ",
   sp.nsimplify(m0) == 0 and sp.nsimplify(m1) == 0)
ok("Z10b ALL-PAIRS weight total = |m_0|^2 = 0 (vanishes BY DESIGN)     ",
   allpairs == 0)
ok("Z10c surviving (same-phase) total = 1/2 ; opposite total = -1/2    ",
   S_surv == sp.Rational(1, 2) and S_opp == sp.Rational(-1, 2))
ok("Z10d (phase_mu phase_lambda - 1) = 0 same-phase / -2 opposite      ",
   all(phase[i]*phase[j] - 1 == 0 for i, j in surv)
   and all(phase[i]*phase[j] - 1 == -2 for i, j in opp))
ok("Z10e 5 surviving pairs, 4 opposite pairs (exhaustive)              ",
   len(surv) == 5 and len(opp) == 4)
# The normalization, exactly (C-L1 collapse level: det = 1 per surviving pair):
N_surv = S_surv
c_wts = {p: sp.nsimplify(w_v[p[0]]*w_v[p[1]]/N_surv) for p in surv}
ok("Z10f N_surv(0) = 1/2 EXACTLY; c_{00} = 1/2, four c_{ss'} = 1/8     ",
   N_surv == sp.Rational(1, 2) and c_wts[(0, 0)] == sp.Rational(1, 2)
   and all(c_wts[p] == sp.Rational(1, 8) for p in surv if p != (0, 0)))
ok("Z10g sum c = 1 ; sum |c| = kappa_bal = 1 (all c > 0)               ",
   sum(c_wts.values()) == 1 and sum(abs(v) for v in c_wts.values()) == 1)

# ---------- Z11: the nonvanishing-region inequality chain, coefficientwise ----------
# |rho(a) - 1| = |e^{Log rho} - 1| <= e^{|Log rho|} - 1 <= |Log rho| e^{|Log rho|}:
# coefficientwise, u e^u - (e^u - 1) = sum_{n>=1} u^n (n-1)/n! with (n-1)/n! >= 0.
coeff_id = sp.simplify(1/sp.factorial(nn - 1) - 1/sp.factorial(nn)
                       - (nn - 1)/sp.factorial(nn))
ok("Z11a 1/(n-1)! - 1/n! = (n-1)/n! (>= 0 for n >= 1): coefficientwise ",
   coeff_id == 0)
# hence |Zhat - 1| <= sum|c| sup|rho - 1| <= kappa_bal x e^x, and
# |Zhat| >= 1 - kappa_bal x e^x > 0 on { kappa_bal x e^x < 1 } (triangle ineq.)

# ---------- Z12: opposite-phase determinant CAN vanish (exclusion, not bound) ----------
sig = sp.symbols('sigma', nonnegative=True)
ok("Z12 eigenvalues of 1 + A(0) = 1 - 2 sigma vanish at sigma = 1/2    ",
   sp.solveset(1 - 2*sig, sig, domain=sp.Interval(0, 1)) == sp.FiniteSet(sp.Rational(1, 2)))

# ---------- Z13: the slab coupling cap (volume-uniform constants) ----------
vfun = tauR*32*sp.Min(tt, 1 - tt)**3
ok("Z13 sup_t v = v(1/2) = 4 tau_R ; mu_max = sqrt2 * 4 tau_R = 4 pi   ",
   sp.simplify(vfun.subs(tt, sp.Rational(1, 2)) - 4*tauR) == 0
   and sp.simplify(sp.sqrt(2)*4*tauR - 4*sp.pi) == 0)
```

Output, verbatim:

```text
Z1a |A|^2 + |B|^2 = 1 exactly (unitarity, re-run)              : PASS
Z1b Om^2 |A|^2 = omega^2 + mu^2 cos^2(Om T)  (modulus identity) : PASS
Z1c |A|^2 - om^2/Om^2 = mu^2 cos^2(Om T)/Om^2  (unitarity floor): PASS
Z1d om = 0 slice of the slab: A = cos(mu T)                     : PASS
Z1e Om - om = mu^2/(Om + om)  (the rate chain's pin, re-run)    : PASS
Z2a at omega = 0 and mu T = pi/2: A = cos(pi/2) = 0 (zero realized): PASS
Z2b for omega > 0: |A|^2 >= om^2/Om^2 > 0 (difference is a square) : PASS
Z3a Theta(rho)/tau_R = int_rho^{1-rho} 32 min(t,1-t)^3 dt = 1-16 rho^4: PASS
Z3b lambda Theta = pi (1-16 rho^4) at lambda = sqrt2               : PASS
Z4a cos(pi u) = 0 on u in (0,1] iff u = 1/2                        : PASS
Z4b u = 1 - 16 rho^4 = 1/2 on [0,1/2) iff rho = 2^(-5/4) (interior): PASS
Z4c 16 rho*^4 = 1/2 exactly; rho* < 1/2 (exponent -5/4 < -1)       : PASS
Z4d lambda = 0 branch: A = 1 identically (never zero)              : PASS
Z5a sum_l w_l cos(l th) = c(th) = (1-cos(sqrt2 th))/2 (re-run)     : PASS
Z5b Theta(rho*) = tau_R/2 ; sqrt2 Theta(rho*) = pi/2               : PASS
Z5c THE WEIGHTED SUM AT THE PER-LAMBDA ZERO = 1/2 EXACTLY (not 0)  : PASS
Z5d g(rho*) = cos^2(8 pi rho*^4) = 1/2 (same point via the g-form) : PASS
Z6a weighted sum zero at om=0 iff cos(pi u)=1: NO root, u in (0,1] : PASS
Z6b boundary rho = 1/2: Theta = 0 and g(1/2) = cos^2(pi/2) = 0     : PASS
Z6c off-support the weighted sum = m_0 = 0 identically (by design) : PASS
Z7  e^{i phi s1} s3 e^{-i phi s1} = cos(2phi) s3 + sin(2phi) s2   : PASS
Z8a dA/dom|_{om=0} = i sin(mu T)/mu  (from the closed form)        : PASS
Z8b i[sin(Phi) int sin(2phi) + cos(Phi) int cos(2phi)] = same      : PASS
Z8c sin(u) >= 0 on [0, pi]: no root of sin in (0, pi) (interior)   : PASS
Z9  dA/drho at (rho*, 0) = 2^(9/4) pi (nonzero; Jacobian nondegen.): PASS
Z10a m_0 = 0, m_1 = 0 (the C4 kill; re-run)                        : PASS
Z10b ALL-PAIRS weight total = |m_0|^2 = 0 (vanishes BY DESIGN)     : PASS
Z10c surviving (same-phase) total = 1/2 ; opposite total = -1/2    : PASS
Z10d (phase_mu phase_lambda - 1) = 0 same-phase / -2 opposite      : PASS
Z10e 5 surviving pairs, 4 opposite pairs (exhaustive)              : PASS
Z10f N_surv(0) = 1/2 EXACTLY; c_{00} = 1/2, four c_{ss'} = 1/8     : PASS
Z10g sum c = 1 ; sum |c| = kappa_bal = 1 (all c > 0)               : PASS
Z11a 1/(n-1)! - 1/n! = (n-1)/n! (>= 0 for n >= 1): coefficientwise : PASS
Z12 eigenvalues of 1 + A(0) = 1 - 2 sigma vanish at sigma = 1/2    : PASS
Z13 sup_t v = v(1/2) = 4 tau_R ; mu_max = sqrt2 * 4 tau_R = 4 pi   : PASS
```

(35/35 PASS. The dominated-convergence/entirety statements of §4.1(a) and
the Riemann-Lebesgue-free rate chain are the sealed R2/REM steps of record,
cited not re-proved; every algebraic/trig/solve step introduced HERE is in
the battery above.)

---

## 8. FLAG BLOCK

```text
ZERO_FREE_NEIGHBORHOOD = NOT-DERIVABLE-AS-DISCHARGE, REDUCED(
  DERIVED exactly: the modulus identity Om^2|A|^2 = omega^2 +
  mu^2 cos^2(Om T) making every slab zero-free on {omega > 0} with the
  volume/carrier-free floor |A| >= omega/sqrt(omega^2 + mu^2), mu <= 4 pi;
  the rate-bound region omega > C_rate(x) lambda^2 zero-free
  volume-uniformly; the complete omega = 0 zero set of the full profile
  (one interior zero per non-trivial branch, rho* = 2^(-5/4), lambda =
  ±sqrt2), its transversality (nondegenerate Jacobian: d rho-component
  2^(9/4) pi, d omega-component strictly imaginary-positive); the two exact
  cancellations keeping the zero out of every consumed object (weighted sum
  = 1/2 at the zero; V(0) = I CTP pair cancellation at baseline on the
  surviving sector); and the REDUCTION of the sealed demand to
  {kappa_bal x e^x < 1} with kappa_bal = 1 — the zero-free gate collapses
  onto the already-named gates. NOT DERIVED: the carrier/volume-uniform
  finiteness of x — per-pair REFUTED (52f2490b), summed substitution
  structurally blocked (per-pair-first determinants + the surviving-sector
  restriction breaks the m_0 factorization). ACT REMAINING: none NEW — the
  already-named summed-S2'/Route B spec act + R-L4a/b. No neighborhood
  choice is needed; flag :2184 stands false, the Gate-6 evaluator's to flip.)
SIMULTANEOUS_VANISHING = EXACT(
  slab: A = 0 <=> omega = 0 AND cos(mu T) = 0 (from Om^2|A|^2 = omega^2 +
  mu^2 cos^2(Om T), a sum of real squares); full profile at omega = 0:
  A_lambda = cos(lambda Theta), zero iff lambda Theta in pi/2 + pi Z,
  realized ONLY at lambda = ±sqrt2, rho* = 2^(-5/4) — interior, genuine, on
  the omega = 0 marginality edge of the closed symbol domain. POLYDISC
  STATUS: the zero sits at a = 0 (baseline) in source space — the CENTER of
  the closed pair polydisc — but it is a SINGLE-BRANCH dressed-symbol zero:
  on the surviving sector V_{mu lambda}(0) = I exactly (CTP pair
  cancellation), so it never enters the baseline determinant, and the
  lambda-weighted sum equals 1/2 exactly at it. It obstructs NOTHING the
  existence path consumes; the weighted sum's own zeros (ball boundary,
  off-support, large-omega) are the BY-DESIGN m_0 = 0 vanishing that the
  N_surv normalization divides out.)
ROUTE_B_ANALYTIC = PARTIAL(
  DERIVED: analyticity exactly stated — per-lambda amplitudes entire in
  omega (dominated Dyson series), slab closed forms entire, finite
  products/sums entire; at fixed carrier n, det(1 + A_{mu lambda,n}(a))
  entire on C^2 and Z_comp,n(a) a finite (5-pair surviving) sum of entire
  functions, a-series dominated on the closed polydisc; the by-design
  leading vanishing of the sum: all-pairs weight total = |m_0|^2 = 0, so
  normalization is mandatory; the normalization EXACTLY: N_surv(0) = 1/2 at
  the C-L1 collapse level (conditional on R-L4a/b), c = (1/2, 1/8, 1/8,
  1/8, 1/8), sum c = 1, kappa_bal = sum|c| = 1; the nonvanishing region in
  exact form: |Z_hat(a) - 1| <= kappa_bal x e^x, |Z_hat| >= 1 - x e^x > 0
  on {x e^x < 1}, F'-14-compliant by construction (rho's assembled, no
  per-pair log of a sum). NOT DERIVED — the exact obstruction: (o-1) the
  input x carrier/volume-uniform does not exist on the sealed basis
  (per-pair refuted; fixed-n gives an n-shrinking neighborhood, exactly
  what D-1 forbids); (o-2) the discharged summed HS bound cannot be
  substituted — the determinant sum is per-pair-first AND the
  surviving-sector restriction breaks the m_0 product factorization the
  discharged kill runs on; (o-3) R-L4a/R-L4b uncertified and
  sector-defining.)
ROUTE_B_QUANTIFIER = SPEC-ACT-REMAINS(
  exactly three things, none a lane's: (q-1) WHICH OBJECT — Route B must be
  quantified over the fixed-n family with n-uniform constants or over a
  summed limit object the spec must first define (the per-pair limit does
  not exist of record); (q-2) the summed-S2' estimate itself (colour sum
  inside the Schatten-2 norm, C4 kill before the norm, R.3 re-derived
  compatibly with F'-14) — AQ §2.3(iii), the E1-successor author's act;
  (q-3) adoption of the compliant passage and retirement of witness
  SCAD_COLOR_SUM_LOG_MISUSE — a validity bar is passed by spec adoption,
  not by a lane exhibit. This derivation NARROWS the act (the analytic
  scaffolding is now on paper) but does not perform it.)
NET = GATES-REDUCED-NONE-CLOSED(
  V011 zero-free gate: reduced to the named gates, no new act, no
  neighborhood choice, one exact zero located and cancelled; F'-14 Route B:
  analytic content partial-derived, remaining = summed-S2' + quantifier
  adoption + R-L4a/b; B-L2* discharge unmoved; per-pair refutation unmoved;
  OBL-D unmoved; all flags stand as sealed — none flipped here (GOV-F).
  Strength: identity-grade where CAS-verified (35/35); estimate-grade-with-
  declared-conditions where the sealed rate chain is consumed; conditional-
  as-marked on R-L4a/b and the C-L2 error input.)
SEALS_VERIFIED = 10/10(
  df4514a5 G1; 3534ca53 G1-CHK; 2e4e5163 REM; 89641f76 REM-CHK; a7969f0c
  R2; a4f2e1b7 R2-CHK; 46846730 E1; 0a10c030 AQ; 331035d3 AQ-CHK; aa7c6d49
  V011 SEALED EVIDENCE MEMBER at evaluator_build_A/inputs/evidence/ (the
  tasked line numbers :1232-1233 and :2184 land exactly there) — all
  recomputed from bytes at path this session. UNVERIFIABLE NOTE: the
  working-tree BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md has no
  sidecar and recomputes to 20a3a17d (drifted, consistent with G1 §1's
  bookkeeping finding) — not relied on.)
FORBIDDEN_IMPORTS = none(
  no physical quantity computed, bounded numerically, or evaluated — every
  constant symbolic or an exact rational/surd; no scale, imported GR, or
  faithfulness authority; M(t) sharp, nothing mollified; equal-time not
  resurrected (the omega = 0 slice is the sealed bookkeeping intermediate
  of record); no register/tracker/plan/road/ledger/lens file read.)
MACHINERY_INVOKED = yes(CAS identity checks only — sympy 1.14.0, fresh venv
  zfvenv, 35 exact identity/solve groups Z1-Z13 over symbols, script and
  output reproduced verbatim in §7; shasum/file reads otherwise; NOTHING
  numeric evaluated.)
alpha_computed = false ; kappa_record_computed = false ;
proof_authorized = false
ALL_RESULTS = CLAIMED until checked.
ZERO_FREE_DERIVATION_RESULT = SEALED.
```
