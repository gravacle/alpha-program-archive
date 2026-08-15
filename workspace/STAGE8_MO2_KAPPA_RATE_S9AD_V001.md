# STAGE 8 — MO-2 OF RECORD: A CERTIFIED LOWER RATE FOR kappa_n ALONG THE HERMITE CARRIER COMPRESSION FAMILY — S9AD V001

## BLIND BUILDER — CODENAME MO2-BUILD — COMMISSION S9AD — [SEALED]

Date: 2026-08-14 (session CDT 2026-08-14 late / UTC 2026-08-15)
Role: BLIND builder (MO2-BUILD). Task: MO-2 of record — a certified LOWER
RATE for kappa_n := ||[C_n, P]||_2^2 (or directly for -log|det_n(0)|) along
the actual Hermite carrier compression family, at the baseline point a = 0.
r-2 (3b5e95b6, audited a4cf394c) proved kappa_n -> +infinity by lower
semicontinuity — rate-free BY CONSTRUCTION; the commission authorizes NEW
spectral input: the sealed constructions worked exactly, plus classical
Hermite asymptotics (Plancherel–Rotach-type) cited as classical ground the
way LSC was, deriving exactly what is used. "Q-..." tokens inside sealed
artifacts are EXPECTED-UNLOCATABLE by design; noted, never chased.

Gates: `alpha_computed = false` ; `proof_authorized = false` ;
`kappa_record_computed = false`. (kappa_n here is the collapse commutator
mass of the adopted clause's dichotomy — NOT kappa_record; no record
curvature value appears anywhere below.) ALL_RESULTS = CLAIMED until
checked.

Fences held: EXACT SYMBOLIC DERIVATION ONLY — one CAS battery (sympy
1.14.0, fresh venv `mo2venv` under the session scratchpad), reproduced
verbatim in §7 (12/12 PASS on the final run; ONE pre-final check-form
correction disclosed in §7's header: check M12 originally CLAIMED an "iff"
for the budget inequality (X-2)^2 >= X^2/4 whose true solution set is
(0, 4/3] U [4, inf); the claim was corrected to the X >= 4 sufficient
direction — the ONLY direction the derivation ever used — and the exact
factorization (3X-4)(X-4)/4 is displayed; no derivation step changed);
every constant symbolic or an exact closed form (pi, sqrt(3), logs of exact
ratios); NOTHING numeric evaluated; no floats as ground; no measured
constant; NO value frozen (the result is an asymptotic growth law with
symbolic constants — an exponent statement, never a number); M(t)/1_{D_t}
sharp (D6'); the stricken display (E1 :773-778) consumed NOWHERE as ground;
no file matching register|road_|ledger|lens|plan|tracker|THE_HANDOFF
opened; no git action; no existing file edited; ONE output (this artifact)
plus its seal sidecar at the commission-distinct path, probed ABSENT at
session start AND re-probed immediately before write. Every
enumeration/uniqueness sentence claims only its own displayed sweep.
Marks: DERIVED / CLAIMED / CLASSICAL(cited) / CONDITIONAL(premise named)
span by span.

SWEEP CUTOFF, DECLARED (parallel lanes running tonight): the corpus sweep
of §5 was executed against the workspace/supervision state as of
**2026-08-14 23:14:15 CDT**; artifacts sealed after that instant are not
consumed and not swept. Parallel S9AD lanes were checked at the cutoff for
MO-2 occupation: NONE claims it (REFUTING_BRANCH flag
`does_not_derive_any_rate = true`; WALL_BOUNDARY_CLOSURE: "MO-1/MO-2 never
enter"; the MO3 lane occupies MO-3 only).

---

## 0. VERDICT IN ONE LINE

**DERIVED — a certified LINEAR lower growth law (gamma = 1, constants
symbolic): for the carrier compression family of record, per admitted state
and cell, at every collapse-bearing cell time (r = r(t) > 0), for each
frozen ell in {1, sqrt2}, uniformly for all four opposite-phase pairs at
once,**

```text
  liminf_{n -> inf}  kappa_n / n  >=  C_*(r, ell) / 2  >  0,
  and explicitly:  kappa_n >= C_*(r, ell) n / 8  for all n >= N_0(r, ell),

  C_*(r, ell) = r^2 L / (8 pi^3 ell^2),
  L = log( (4 - sqrt3) / (2 (2 - sqrt3)) )  > 0   (exact, r- and ell-free),
```

**hence, by the of-record chain -log|det_n(0)| >= kappa_n (r-2 X-1 / r-3
D8), the SAME lower rate for -log|det_n(0)|, i.e. |det_n(0)| <=
exp(-C_* n/8) for n >= N_0: the baseline determinant collapses at least
EXPONENTIALLY IN THE CARRIER LEVEL n. The derivation is scheme-robust (the
mixed family Q_n P_- Q_n obeys the cleaner bound kappa_n^mix >= C_* n / 2
with no kernel correction). The NEW spectral input the rate needed is
named: (i) the EXACT chiral involution of the compressed family — the
Dirac beta (beta^2 = 1, {beta, alpha_j} = 0) anticommutes with the sealed
massless generator h_0 = sum_j p_j alpha_j and commutes with the Hermite
carrier projector Q_n and with the ball projector P, so beta C_n beta =
Q_n - C_n - (kernel correction of rank <= 4, computed exactly), which
converts the un-diagonalizable pure sea projection C_n into the EXPLICIT
Hermite projector Q_n at the price of a factor 2 and an O(1) additive term:
kappa_n >= (1/2)(||P^perp Q_n P||_2 - 2)^2; and (ii) ONE classical ground,
CL-A (Plancherel–Rotach fixed-compact asymptotics of Hermite functions,
cited as classical, commission-authorized), from which the boundary-
crossing Hilbert–Schmidt mass of Q_n across the ball surface is bounded
below by C_* n exactly (region-shrink positivity + the exact reproducing
identity + a diagonal density floor + a separated-window wave floor).
Sharpness is NOT claimed (the true rate is plausibly faster; not needed —
the commission requires a certified lower rate, any gamma). N_0 exists by
CL-A's thresholds and is not numerically extracted (no value frozen).
Nothing fires: the registrar consumes; MO-2 is supplied as a candidate
input only; r-3 and R-L4b are NOT discharged here (MO-1/MO-3 or MO-4 still
missing, of record). CAS battery 12/12 PASS.**

---

## 1. SEALS VERIFIED AT PATH (shasum -a 256), BEFORE ANY RELIANCE

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`. Every
digest recomputed from bytes at path THIS session by FULL digest and
matched against its sidecar (and the commission's pinned digests 3b5e95b6,
bebc0f08 reproduced exactly). 7/7 MATCH.

```text
G-1  3b5e95b6da98a99e510515deab518b25554feb74145f6e754944262a17e7ab9f
     STAGE8_R2_KAPPA_N_DETERMINATION_S9AD_V001.md   MATCH (sidecar, tasked)
     — r-2 OF RECORD: kappa_n definition and identity frame (§2.2(b)
     :169-174); C_n^(pure) = 1_(-inf,0)(Q_n h_0 Q_n) with CH-A premise
     (:511-526); zero-mode convention note (§3 step 3); X-1 chain
     |det_n(0)|^2 <= exp(-2 kappa_n) (:371-379); read in full.
G-2  a4cf394c7c94feab39bf9437e3112ceb719f07a251ff772dcca1661e044521fb
     STAGE8_R2_KAPPA_N_DETERMINATION_S9AD_AUDIT_V001.md  MATCH (sidecar)
     — CONFIRMED-WITH-CORRECTIONS, all cosmetic, none verdict-chain: r-2
     consumable at audited grade.
G-3  bebc0f085d10082e1229e2638637e12681687356daf86fbe652179514230c6a9
     STAGE8_R3_JOINT_RATE_S9AD_V001.md              MATCH (sidecar,
     tasked) — MO-2 definition (:74-76, :478-479, flag :809-811); the
     denominator chain -log|det_n(0)| >= kappa_n (D8); the kappa ceiling
     kappa_n <= 2n^3 (D4); rank C_n <= 4n^3 (K-2/CH-f); read in full.
G-4  72c95d42308921ad7e64bb9fee127752cb7256ff8b8c9f57949d508636d4c407
     STAGE8_R3_JOINT_RATE_S9AD_AUDIT_V001.md        MATCH (sidecar) —
     CONFIRMED-WITH-CORRECTIONS, cosmetic: r-3 consumable at audited
     grade; blocker list (incl. MO-2) confirmed GENUINE.
G-5  468467303a109dc825b015107897dacc107800fc981030377c3f006b384cccb5
     STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md    MATCH (sidecar) — C1
     sea symbol pinned exactly (:320-329); C4 the sharp causal-ball
     projector promotion (:339-352); C6 + locus refinement (:353-370);
     R.2 baseline display (:739-762); the stricken display (:773-778,
     consumed nowhere).
G-6  789338adb7d3d36da453113e98f371a4f92543cf2652b047f8481c407bed5bc3
     STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md
     MATCH (sidecar) — PA A1 (:48-92): the Hermite-triple carrier
     H_(n,ell) = span{phi_a(x/ell)phi_b(y/ell)phi_c(z/ell): 0 <= a,b,c
     < n} tensor C^4 (an index CUBE, hence a product projector);
     h_(0,n,ell) = sum_j p_(j,n,ell) tensor alpha_j (MASSLESS — no beta m
     term); the causal ball r(t) = min(t, 1-t).
G-7  3de0502c46d3f837166106206303c3e17dcda074d00f46dad7aa647154305522
     STAGE8_RATE_GAP_LINKAGE_S9AD_V001.md           MATCH (sidecar) —
     GAP-C typing (§2.3): MO-2 unoccupied of record; B-C/A-C cousinship
     (no rate chain elsewhere); consumed as sweep corroboration only.
```

EXPECTED-UNLOCATABLE tokens this session: "Q-1059", "Q-1062", "Q-1054"
(register pointers inside sealed artifacts) — noted per standing design;
not chased; nothing defaulted. The adopted clause (72d5343e) was NOT
opened; its content enters only through r-2/r-3's sealed-and-audited
quotes (ledger CH-7).

---

## 2. THE OBJECTS OF RECORD, AND THE THREE EXACT STRUCTURAL FACTS

### 2.1 The pair, at bytes

```text
C_n  (the family of record, pure scheme, r-2 CH-A premise inherited):
     C_n = 1_(-inf,0)(H_n) + z_n,  H_n := Q_n h_0 Q_n restricted to
     ran Q_n,  z_n = the per-member zero-mode convention: ANY self-adjoint
     0 <= z_n <= Z_n, Z_n := 1_({0})(H_n|ran Q_n)  [G-1 §2.3, §3 step 3;
     G-12-of-r-2's "when the finite operator has no zero mode"]. C_n is a
     finite-rank orthogonal projection supported in ran Q_n.
P    the sharp causal-ball projector: multiplication by 1_(|x| <= r),
     spinor-diagonal, r = r(t) = min(t, 1-t) > 0 at every collapse-bearing
     cell time  [G-5 C4 :339-352, R.2; D6' sharp].
Q_n  the carrier projector: Q_n = q_n tensor q_n tensor q_n tensor 1_4,
     q_n = the 1D Hermite-level-< n projector at oscillator length ell
     (the index set 0 <= a,b,c < n is a CUBE: the product form is exact)
     [G-6 A1 :53-57]. rank Q_n = 4n^3.
h_0  = sum_j p_j alpha_j, MASSLESS  [G-6 A1 :79]. Hence
     H_n = sum_j pi_j alpha_j with pi_x = (q_n p q_n) tensor q_n tensor
     q_n etc. — the three compressed momenta act in DIFFERENT tensor
     factors and therefore commute exactly.
kappa_n := ||[C_n, P]||_2^2  (of record, G-1 §2.2(b)); at the baseline on
     opposite-phase pairs A_n(0) = -2 C_n P C_n is PAIR-INDEPENDENT (G-5
     R.2): every statement below covers all four pairs at once.
```

### 2.2 FACT ONE (DERIVED, exact) — the block identity

For ANY Hermitian C and any orthogonal projection P: in the P-block
decomposition, [C, P] = P^perp C P - P C P^perp, the two blocks are
mutually adjoint up to sign, so

```text
  ||[C, P]||_2^2 = 2 ||P^perp C P||_2^2.                       (CAS M2)
```

For C = C_n (projection) this reproduces r-2's identity kappa_n =
2 sum_i s_i(1 - s_i) exactly (tr(P C_n P^perp C_n P) = tr(C_n P C_n) -
tr((C_n P C_n)^2)); consistency, not new.

### 2.3 FACT TWO (DERIVED, exact) — the chiral involution and its kernel bookkeeping

In the 4x4 Dirac algebra there exists beta with beta = beta^dag,
beta^2 = 1, {beta, alpha_j} = 0 for j = x, y, z (existence displayed at
the standard representation, CAS M1; ANY such beta serves — CH-4). Then:

```text
(i)   beta h_0 beta = -h_0        (massless; termwise sign flip, M1);
(ii)  beta Q_n beta = Q_n         (Q_n = spatial tensor 1_4);
(iii) beta P beta = P,  beta P^perp beta = P^perp   (P spinor-diagonal);
(iv)  beta H_n beta = -H_n        ((i)+(ii));
(v)   beta 1_(-inf,0)(H_n) beta = 1_(-inf,0)(-H_n) = 1_(0,inf)(H_n)
      (unitary conjugation of the functional calculus, exact);
(vi)  therefore  C_n + beta C_n beta = Q_n - Z_n + z_n + beta z_n beta
      = Q_n - W_n,   W_n := Z_n - z_n - beta z_n beta,  an operator on
      ran Z_n with ||W_n|| <= 1  (Z_n acts as the identity there and
      z_n, beta z_n beta are positive contractions of it).
```

KERNEL DIMENSION, EXACT: H_n^2 = (pi_x^2 + pi_y^2 + pi_z^2) tensor 1_4
(the alpha cross terms cancel by exact anticommutation; the pi_j commute —
CAS M5), so ker(H_n|ran Q_n) = ker(pi_x) ∩ ker(pi_y) ∩ ker(pi_z) =
(ker q_n p q_n)^{tensor 3} tensor C^4. The 1D compressed momentum q_n p
q_n is the Hermitian tridiagonal matrix with <k|p|k+1> = -i sqrt((k+1)/2)
/ ell and zero diagonal (exact Gaussian integrals, CAS M3). An unreduced
Hermitian tridiagonal matrix has nullity <= 1 (three-term recurrence: a
kernel vector is determined by its first component — row 0 forces v_1 = 0,
row k forces v_{k+2} from v_k); factoring i it is real antisymmetric, so
for n odd it IS singular (det A = (-1)^n det A) and for the displayed even
member it is not (CAS M4: nullity 0 at n = 4, 1 at n = 5). Hence

```text
  dim ker(H_n | ran Q_n) = 4 (n mod 2) <= 4,
  ||W_n||_2 <= sqrt(dim ker) <= 2.                             (CAS M3/M4/M5)
```

### 2.4 FACT THREE (DERIVED, exact) — the chiral reduction to the explicit projector

From (vi), P^perp Q_n P = P^perp C_n P + P^perp (beta C_n beta) P +
P^perp W_n P, and ||P^perp (beta C_n beta) P||_2 = ||beta (P^perp C_n P)
beta||_2 = ||P^perp C_n P||_2 (unitary invariance + (iii)). Triangle
inequality and ||P^perp W_n P||_2 <= ||W_n||_2 <= 2:

```text
  ||P^perp Q_n P||_2  <=  2 ||P^perp C_n P||_2 + 2,

  i.e.  kappa_n = 2 ||P^perp C_n P||_2^2
              >=  (1/2) ( ||P^perp Q_n P||_2 - 2 )^2            (*)
        whenever ||P^perp Q_n P||_2 >= 2.
```

THE POINT: (*) eliminates the spectral projection of the compressed Dirac
operator — the object with no closed form, the reason r-2's method was
rate-free — in favor of the EXPLICIT Hermite projector Q_n, at the price
of a factor 2 and an O(1) additive term. This is the new spectral input's
structural half. MIXED SCHEME, CLEANER: beta C beta = 1 - C for the
continuum sea (symbol conjugation, M1; h_0 has no zero eigenvalue —
absolutely continuous spectrum, classical), so beta (Q_n C Q_n) beta =
Q_n - Q_n C Q_n EXACTLY, no kernel correction:

```text
  kappa_n^mix := ||[Q_n C Q_n, P]||_2^2 = 2 ||P^perp Q_n C Q_n P||_2^2
             >=  (1/2) ||P^perp Q_n P||_2^2.                    (**)
```

---

## 3. THE CLASSICAL GROUND CL-A (cited as classical; commission-authorized; everything used derived from it)

```text
CL-A (Plancherel–Rotach fixed-compact asymptotics; classical: Plancherel &
Rotach 1929; Szegő, Orthogonal Polynomials, §8.22 (8.22.6), transcribed to
the L^2-normalized oscillator eigenfunctions phi_k at ell = 1): for every
fixed T > 0 there are e_k(T) -> 0 with

  phi_k(t) = A_k [ cos(theta_k(t)) + eps_k(t) ],
  A_k = (2/pi)^(1/2) (2k)^(-1/4),   theta_k(t) = omega_k t - k pi/2,
  omega_k = sqrt(2k+1),   sup_{|t| <= T} |eps_k(t)| <= e_k(T) -> 0.
```

Consumed EXACTLY the way r-2 consumed lower semicontinuity: cited as
classical, never re-derived, with every consequence below derived exactly
from the statement (the WKB phase's cubic correction and the amplitude's
(2k+1-t^2)^(-1/4)-vs-(2k)^(-1/4) discrepancy are O(k^(-1/2)) on compacts
and absorbed into eps_k — part of the citation, not of my derivation).
Everything else in §4 is exact algebra on top of CL-A: the CD formula and
the reproducing identity are exact (CAS M6), the trig assembly is exact
(M7), the Lipschitz grounds are exact (M7/M8), the integrals are exact
(M9-M11). No other classical analytic input is consumed anywhere.

---

## 4. THE HERMITE CROSSING-MASS LOWER BOUND (DERIVED, exact given CL-A)

Write k_n for the 1D Christoffel–Darboux kernel at ell = 1, k_n(x, y) =
sum_{k<n} phi_k(x) phi_k(y); at oscillator length ell, k_n^ell(x, y) =
(1/ell) k_n(x/ell, y/ell) (exact scaling). The 3D spatial kernel of Q_n is
the product K3(x, y) = prod_j k_n^ell(x_j, y_j), spinor factor 1_4, so

```text
  ||P^perp Q_n P||_2^2 = 4 Int_{x in B} Int_{y in B^c} K3(x,y)^2 dx dy .
```

### 4.1 Region shrink (positivity) and exact tensor factorization

Let D := { x : |x_perp| <= r/2, 0 < x_1 < s(x_perp) }, s(x_perp) =
sqrt(r^2 - |x_perp|^2) >= a := (sqrt3/2) r; D is inside B, and
{ y : y_1 > r } is inside B^c. The integrand is a square, so restricting
both domains only lowers the value; the y_2, y_3 integrals then run over
ALL of R and collapse by the EXACT reproducing identity Int_R
k_n^ell(x_j, y_j)^2 dy_j = k_n^ell(x_j, x_j) (orthonormality; CAS M6):

```text
  ||P^perp Q_n P||_2^2
    >= 4 Int_{|x_perp| <= r/2} k_n^ell(x_2,x_2) k_n^ell(x_3,x_3)
         [ Int_0^a dx_1 Int_r^R dy_1  k_n^ell(x_1, y_1)^2 ]  dx_perp
```

(with the inner x_1-window shrunk from (0, s(x_perp)) to (0, a) and the
y_1-window from (r, inf) to (r, R), R := 2r — positivity again).

### 4.2 The diagonal floor (from CL-A)

Pairing consecutive levels: theta_{k+1}(t) = theta_k(t) - pi/2 + d_k t,
d_k = omega_{k+1} - omega_k = 2/(omega_{k+1} + omega_k) (exact
rationalization, M11 shape), so cos^2 theta_{k+1} = sin^2(theta_k + d_k t)
and, by the exact identity sin^2 theta - sin^2(theta - delta) =
sin(delta) sin(2 theta - delta) (M7) with |sin| <= |.| (M8):

```text
  cos^2 theta_k + cos^2 theta_{k+1} >= 1 - d_k |t| ,
```

while (cos + eps)^2 >= cos^2 - 2|eps| and A_{k+1} <= A_k (M8). Dropping
the head k < m (each term >= 0) and telescoping the tail with the exact
integral-test floor sum_{k=m}^{n-1} (2k)^(-1/2) >= sqrt(2n) - sqrt(2m)
(M11):

```text
  k_n(t, t) >= (1/pi)(sqrt(2n) - sqrt(2m+2))(1 - eta_{m,n}),
  eta_{m,n} -> 0 (m fixed, n -> inf), uniformly on |t| <= T.
```

Hence for each fixed compact and any theta in (0,1) there is n_1 with
k_n(t,t) >= theta sqrt(2n)/pi there; take theta = 1/2 (CH-6):

```text
  k_n^ell(t, t) >= sqrt(2n) / (2 pi ell)   for |t| <= r/2, n >= n_1.
```

### 4.3 The separated-window wave floor (from CL-A)

On the scaled window u in [0, a/ell], v in [r/ell, 2r/ell] (separation
(r - a)/ell > 0, all inside a fixed compact), the exact CD formula
k_n = sqrt(n/2)[phi_n(x)phi_{n-1}(y) - phi_{n-1}(x)phi_n(y)]/(x - y)
(CAS M6) with CL-A inserted and the EXACT trig decomposition M7 gives

```text
  k_n(u, v) = pref_n [ sin(omega_n (u - v)) + eta_n(u, v) ] / (pi (u - v)),
  pref_n = (1 - 1/n)^(-1/4) >= 1   (exact, M8),
  sup |eta_n| -> 0 on the window
```

(the remainders are Lipschitz-controlled by d_n·(compact diameter) and by
e_n, e_{n-1} — M7/M8 grounds, all displayed). Squaring with
(s + eta)^2 >= s^2 - 2|eta| and averaging the oscillation exactly —
sin^2 = 1/2 - cos(2 omega_n .)/2, the cos(2 omega_n .) integral O(1/
omega_n) by the exact integration-by-parts identity M10 — against the
EXACT window integral (M9)

```text
  Int_0^{a/ell} du Int_{r/ell}^{2r/ell} dv (u - v)^(-2)
      = L := log( (4 - sqrt3) / (2 (2 - sqrt3)) ) > 0
  (r-free and ell-free: proportional windows; positivity is exact:
   (4 - sqrt3) - 2(2 - sqrt3) = sqrt3 > 0),
```

gives: liminf_n Int Int k_n^ell(x_1,y_1)^2 >= L/(2 pi^2) over the window,
hence a threshold n_2 with

```text
  Int_0^a dx_1 Int_r^{2r} dy_1 k_n^ell(x_1, y_1)^2  >=  L / (4 pi^2),
  n >= n_2.
```

### 4.4 Assembly (exact algebra, CAS M12)

For n >= max(n_1, n_2), using |x_2|, |x_3| <= |x_perp| <= r/2 and the
disk area pi r^2/4:

```text
  ||P^perp Q_n P||_2^2
    >= 4 · (pi r^2/4) · ( sqrt(2n)/(2 pi ell) )^2 · ( L/(4 pi^2) )
    =  r^2 L n / (8 pi^3 ell^2)  =:  C_*(r, ell) · n .           (M12)
```

---

## 5. THE RATE, THE SWEEP, AND CONSISTENCY

### 5.1 The certified rate (the MO-2 object)

Combining §4.4 with the chiral reduction (*) and the budget algebra
(X - 2)^2 >= X^2/4 for X >= 4 (exact factorization (3X-4)(X-4)/4, M12):

```text
  PURE SCHEME (the family of record, CH-1 premise inherited):
    kappa_n >= (1/2)( sqrt(C_* n) - 2 )^2          for n >= max(n_1, n_2),
    kappa_n >= C_* n / 8                            for n >= N_0,
    liminf_n kappa_n / n >= C_* / 2,
    N_0 := max( n_1, n_2, ceil(16 / C_*) )  — N_0 EXISTS by CL-A's
    thresholds; its value is not extracted (no value frozen).

  MIXED SCHEME (scheme-robustness, r-2 pattern):
    kappa_n^mix >= C_* n / 2                        for n >= max(n_1, n_2).

  DETERMINANT COROLLARY (of-record chain -log|det_n(0)| >= kappa_n,
  r-2 X-1 / r-3 D8; at a member with some s_i = 1/2 the left side is
  +infinity and the bound is trivially true):
    -log|det_n(0)| >= C_* n / 8,  i.e.  |det_n(0)| <= exp(-C_* n / 8),
    for n >= N_0.

  QUANTIFIERS: per admitted state (M-3) and admitted cell, at every cell
  time with r(t) > 0, per frozen ell in {1, sqrt2} (C_* displayed as a
  symbolic function of r and ell), all four opposite-phase pairs at once
  (pair-independence of A_n(0), G-5 R.2). GAMMA = 1; SHARPNESS NOT
  CLAIMED (the truncation's own Fermi-box surface plausibly adds a log n;
  not derived, not needed — a lower bound at a certified rate suffices,
  per the commission).
```

### 5.2 The sweep (exhaustive at this displayed sweep only; cutoff §header)

```text
ROOTS: /Users/bgm/MB Work/alpha-program-archive and /Users/bgm/MB Work/
alpha_supervision, minus the fenced name classes (register|road_|ledger|
lens|plan|tracker|THE_HANDOFF, case-insensitive).
KEYS RUN: Plancherel; Christoffel; "chiral symmetr"; particle-hole;
anticommut; Widom; "commutator-mass growth"; "kappa_n >="; "kappa_n rate";
"beta H beta"; "MO-2".
FINDINGS:
 s-1 NO kappa_n rate exists anywhere (re-confirming r-3 s-4 and the
     linkage GAP-C typing at my cutoff): the only "commutator-mass
     growth" carriers are r-3 and the linkage (the MO-2 DEFINITION, not a
     supply); the parallel S9AD lanes at the cutoff disclaim it
     (REFUTING_BRANCH `does_not_derive_any_rate = true`;
     WALL_BOUNDARY_CLOSURE "MO-1/MO-2 never enter"; MO3 lane = MO-3).
 s-2 NO "chiral symmetr" carrier exists in either root: the beta
     involution of the compressed family is NEW input, nowhere sealed,
     and NOTHING sealed contradicts it (the only requirement is h_0
     massless of record — G-6 A1 bytes — and the spinor-diagonality of P
     and Q_n, G-5/G-6 bytes).
 s-3 "Plancherel"/"Christoffel" hits are sympy vendored files and
     unrelated lanes (FORM_TO_HS_BRIDGE consumes Christoffel-Darboux
     vocabulary for the C-L2 form bound at other sites; no kappa_n
     content); one supervision filename ("Widom") surfaced by name only,
     NEVER OPENED (narrative root; not needed).
 s-4 No sealed display supplies or refutes any n_1/n_2-type Hermite
     threshold: CL-A has no sealed substitute; classical citation is the
     commission's own authorized route.
```

### 5.3 Consistency with the sealed stock (exact, never numeric)

```text
X-1 vs THE CEILING (r-3 D4): C_* n / 8 <= kappa_n <= 2 n^3 — a linear
    floor under a cubic ceiling; no conflict at any n; the ratio
    (2n^3)/(C_* n/8) grows, as it must (the floor is not claimed sharp).
X-2 vs r-2 (B1-DERIVED): kappa_n >= C_* n/8 -> +infinity RECOVERS r-2's
    divergence WITH a rate, at the same full-family quantifier (the bound
    holds cofinitely, hence on every subsequence). No r-2 sentence is
    contradicted; r-2's method (LSC) is bypassed, not corrected.
X-3 vs r-3's Route-1 obstruction (D10): supplying MO-2 does NOT revive
    the rank x op budget: (4n^3 c(eps_*)) / (C_* n/8) grows like n^2 —
    Route 1 still requires MO-3 exactly as r-3 proved structurally; and
    the MO-2+MO-4 package (the REFUTING_BRANCH-preferred closure) now
    lacks only MO-4. Nothing in r-3's verdict is disturbed; one of its
    four named missing objects is supplied as a candidate.
X-4 vs the check's n-1 shape / FRAME-N3: a single s_i -> 1/2 carries
    bounded kappa mass — consistent: my bound is a SUM statement over the
    whole spectrum, forced by the crossing mass of Q_n, not by any single
    eigenvalue; near-1/2 eigenvalues maximizing per-eigenvalue kappa mass
    (r-3 CAS D2) is consistent with, and explains, the mechanism: the
    truncation accumulates near-1/2 spectrum at the coincidence locus.
X-5 THE STRICKEN DISPLAY (E1 :773-778): consumed nowhere. No continuum
    inequality is evaluated; no value of D inferred; C6 itself is not
    even needed here (the divergence input of r-2 is REPLACED by the
    finite-n crossing mass of Q_n; C6's locus — the volume diagonal at
    the ball surface — is exactly where the mass in §4 accumulates,
    displayed as consistency, not consumed as ground).
X-6 FENCE CHECK: kappa_record_computed = false is untouched — kappa_n is
    the clause's collapse commutator mass, not the record curvature; no
    alpha-adjacent number appears; every constant is a displayed symbolic
    expression (C_*, L, pi, sqrt3).
```

---

## 6. WHAT THIS SUPPLIES AND WHAT IT DOES NOT (consumption boundary)

```text
- Once sealed and checked, this is the MO-2 CANDIDATE INPUT of r-3's
  missing-object list (bebc0f08 :74-76, :478-479, :807-815): a certified
  lower RATE for kappa_n AND for -log|det_n(0)| at the baseline. THE
  REGISTRAR CONSUMES; this artifact fires nothing, flips no flag,
  retires no witness.
- r-3 is NOT discharged: Route 1 still needs MO-1 + MO-3; the direct
  package still needs MO-4. R-L4b is NOT discharged. All three R-L4
  witnesses STAND.
- B2/F-a interactions: none new — r-2 already refuted bounded kappa_n;
  a RATE only strengthens the same branch. F-d untouched (a != 0
  territory).
- The rate feeds the r-3 denominator: any future numerator rate must now
  beat C_* n/8 (a named, displayed target instead of an unquantified
  divergence) — the race of two divergences has one lane clocked.
```

---

## 7. THE CAS BATTERY (VERBATIM) AND ITS OUTPUT (VERBATIM)

sympy 1.14.0, fresh venv `mo2venv` under the session scratchpad; nothing
written to the workspace but this artifact and its seal. Tooling
disclosure, on the record: ONE pre-final check-form correction — check M12
originally claimed "(X-2)^2 >= X^2/4 iff X >= 4", but the inequality's
true solution set on X > 0 is (0, 4/3] U [4, inf); the check was corrected
to display the exact factorization (3X-4)(X-4)/4 and claim only the X >= 4
SUFFICIENT direction, which is the only direction the derivation uses (§5.1
applies it at X = sqrt(C_* n) >= 4). No derivation step changed. The final
battery then ran ONCE: 12/12 PASS.

```python
# MO2-BUILD CAS battery -- EXACT SYMBOLIC ONLY (sympy 1.14.0, fresh venv
# mo2venv under the session scratchpad). Every constant symbolic or an exact
# rational. Nothing numeric evaluated. All checks are exact-identity
# consistency checks of steps whose operator-theoretic content is derived in
# the artifact text.
import sympy as sp
from sympy import Rational as R

ok = lambda name, cond: print(f"{name}: {'PASS' if cond else 'FAIL'}", flush=True)

# ===== M1 -- the Dirac beta exists and does what the reduction needs =====
# Standard Dirac representation: alpha_j = offdiag(sigma_j, sigma_j),
# beta = diag(I2, -I2). Checks: beta Hermitian unitary; {beta, alpha_j} = 0
# for all j; hence beta(alpha.v)beta = -alpha.v for every real vector v, and
# beta conjugates the sealed sea symbol C(p) = (I - alpha.p-hat)/2 to
# I - C(p) EXACTLY.
sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]]); I2 = sp.eye(2); Z2 = sp.zeros(2, 2)
def blk(a, b, c, d):
    return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))
alx = blk(Z2, sx, sx, Z2); aly = blk(Z2, sy, sy, Z2); alz = blk(Z2, sz, sz, Z2)
beta = blk(I2, Z2, Z2, -I2)
px, py, pz = sp.symbols('p_x p_y p_z', real=True)
nrm = sp.sqrt(px**2 + py**2 + pz**2)
alp = (px*alx + py*aly + pz*alz)/nrm
Csym = (sp.eye(4) - alp)/2
ok("M1 beta^2 = I, beta = beta^dag, {beta, alpha_j} = 0 (j = x,y,z), and"
   " beta C(p) beta = I - C(p) EXACTLY for the sealed symbol C(p) ="
   " (I - alpha.p-hat)/2",
   beta*beta == sp.eye(4) and beta == beta.H
   and all(sp.simplify(beta*a + a*beta) == sp.zeros(4, 4)
           for a in (alx, aly, alz))
   and sp.simplify(beta*Csym*beta - (sp.eye(4) - Csym)) == sp.zeros(4, 4))

# ===== M2 -- the block identity ||[C,P]||_F^2 = 2 ||P-perp C P||_F^2 =====
# For ANY Hermitian C and any diagonal 0/1 projection P (3x3 symbolic
# Hermitian instance; the argument in the text is the all-dimensions block
# decomposition [C,P] = P-perp C P - P C P-perp).
a11, a22, a33 = sp.symbols('a11 a22 a33', real=True)
z12, z13, z23 = sp.symbols('z12 z13 z23')
Cm = sp.Matrix([[a11, z12, z13],
                [sp.conjugate(z12), a22, z23],
                [sp.conjugate(z13), sp.conjugate(z23), a33]])
Pm = sp.diag(1, 1, 0); Pp = sp.eye(3) - Pm
comm = Cm*Pm - Pm*Cm
lhs = sp.trace(comm.H*comm)
rhs = 2*sp.trace((Pp*Cm*Pm).H*(Pp*Cm*Pm))
ok("M2 ||[C,P]||_F^2 = 2||P-perp C P||_F^2 for Hermitian C, projection P"
   " (block decomposition [C,P] = P-perp C P - P C P-perp, exact)",
   sp.simplify(sp.expand(lhs - rhs)) == 0)

# ===== M3 -- exact Hermite ladder: the compressed momentum is tridiagonal ==
# phi_k = (2^k k! sqrt(pi))^(-1/2) H_k(x) e^{-x^2/2} (ell = 1);
# <j| p |k> = Int phi_j (-i phi_k') dx, exact Gaussian integrals.
x = sp.Symbol('x', real=True)
def phi(k):
    return (sp.hermite(k, x)*sp.exp(-x**2/2)
            / sp.sqrt(sp.sqrt(sp.pi)*2**k*sp.factorial(k)))
Pmat = sp.zeros(5, 5)
for j in range(5):
    for k in range(5):
        Pmat[j, k] = sp.integrate(phi(j)*(-sp.I)*sp.diff(phi(k), x),
                                  (x, -sp.oo, sp.oo))
target = sp.zeros(5, 5)
for k in range(4):
    target[k, k+1] = -sp.I*sp.sqrt(R(k+1, 2))
    target[k+1, k] = sp.I*sp.sqrt(R(k+1, 2))
ok("M3 <j|p|k> tridiagonal EXACT on levels 0..4: <k|p|k+1> = -i sqrt((k+1)/2)"
   " (ell = 1; general ell divides by ell), all other entries 0",
   sp.simplify(Pmat - target) == sp.zeros(5, 5))

# ===== M4 -- kernel-dimension parity of the compressed 1D momentum =====
# n = 4: invertible (nullity 0); n = 5: nullity exactly 1; and every real
# antisymmetric odd-dimensional matrix is singular (3x3 symbolic witness).
M4 = target[0:4, 0:4]; M5 = Pmat[0:5, 0:5]
b12, b13, b23 = sp.symbols('b12 b13 b23', real=True)
A3 = sp.Matrix([[0, b12, b13], [-b12, 0, b23], [-b13, -b23, 0]])
ok("M4 nullity(q_n p q_n) = n mod 2 at the displayed members (n = 4: 0;"
   " n = 5: 1) and det(antisymmetric odd) = 0 identically (3x3 symbolic);"
   " with the three-term-recurrence simplicity argument (text): <= 1 all n",
   M4.rank() == 4 and M5.rank() == 4
   and sp.expand(A3.det()) == 0)

# ===== M5 -- the tensor-square identity (Sum pi_j alpha_j)^2 = Sum pi_j^2 ==
# pi_j mutually commuting (they act in different tensor factors of record);
# commuting-scalar instance at identity grade, alphas explicit.
q1, q2, q3 = sp.symbols('pi_x pi_y pi_z', commutative=True)
H = q1*alx + q2*aly + q3*alz
ok("M5 (pi_x alpha_x + pi_y alpha_y + pi_z alpha_z)^2 ="
   " (pi_x^2 + pi_y^2 + pi_z^2) I_4 EXACT for commuting pi_j (of record:"
   " the three compressed momenta act in different Hermite tensor factors)",
   sp.expand(H*H - (q1**2 + q2**2 + q3**2)*sp.eye(4)) == sp.zeros(4, 4))

# ===== M6 -- Christoffel-Darboux + reproducing property, exact members =====
def kker(n, xx, yy):
    return sum((phi(k)*phi(k).subs(x, yy)).subs(x, xx) for k in range(n))
y = sp.Symbol('y', real=True)
cd_ok = True
for n in (2, 3):
    kn = kker(n, x, y)
    cd = sp.sqrt(R(n, 2))*(phi(n)*phi(n-1).subs(x, y)
                           - phi(n-1)*phi(n).subs(x, y))/(x - y)
    cd_ok = cd_ok and sp.simplify(sp.together(kn - cd)) == 0
rep_ok = True
for n in (2, 3):
    kn = kker(n, x, y)
    rep_ok = rep_ok and sp.simplify(sp.integrate(kn**2, (y, -sp.oo, sp.oo))
                                    - kker(n, x, x)) == 0
ok("M6 CD formula k_n(x,y) = sqrt(n/2)[phi_n(x)phi_(n-1)(y) -"
   " phi_(n-1)(x)phi_n(y)]/(x-y) EXACT at n = 2,3; reproducing property"
   " Int_R k_n(x,y)^2 dy = k_n(x,x) EXACT at n = 2,3",
   cd_ok and rep_ok)

# ===== M7 -- the trig assembly of the off-diagonal wave (exact identities) ==
u, v, aph, bph = sp.symbols('u v a b', real=True)
expr = sp.sin(u - aph)*sp.cos(v) - sp.cos(u)*sp.sin(v - bph)
decomp = (R(1, 2)*(sp.sin(u + v - aph) - sp.sin(u + v - bph))
          + sp.sin(u - v + (bph - aph)/2)*sp.cos((aph + bph)/2))
th, dl = sp.symbols('theta delta', real=True)
ok("M7 sin(u-a)cos(v) - cos(u)sin(v-b) = (1/2)[sin(u+v-a) - sin(u+v-b)]"
   " + sin(u-v+(b-a)/2)cos((a+b)/2) EXACT (the CD numerator = sin(u-v) +"
   " Lipschitz-small remainders); and sin^2(theta) - sin^2(theta-delta) ="
   " sin(delta) sin(2 theta - delta) EXACT (the pairing floor's Lipschitz"
   " ground)",
   sp.simplify(sp.expand_trig(expr - decomp)) == 0
   and sp.simplify(sp.expand_trig(sp.sin(th)**2 - sp.sin(th - dl)**2
                                  - sp.sin(dl)*sp.sin(2*th - dl))) == 0)

# ===== M8 -- |sin t| <= |t| and the amplitude/prefactor limits =====
t = sp.Symbol('t', nonnegative=True)
n = sp.Symbol('n', positive=True)
pref = sp.sqrt(n/2)*(2/sp.pi)*(2*n)**(-R(1, 4))*(2*n - 2)**(-R(1, 4))
ok("M8 t - sin t >= 0 on t >= 0 (h(0) = 0, h' = 1 - cos t >= 0): |sin t|"
   " <= |t|; prefactor sqrt(n/2)(2/pi)(2n)^(-1/4)(2n-2)^(-1/4) ="
   " (1/pi)(1 - 1/n)^(-1/4) EXACT, limit 1/pi; A_k = (2/pi)^(1/2)(2k)^(-1/4)"
   " decreasing in k",
   (t - sp.sin(t)).subs(t, 0) == 0
   and sp.simplify(sp.diff(t - sp.sin(t), t) - (1 - sp.cos(t))) == 0
   and sp.simplify(pref - (1/sp.pi)*(1 - 1/n)**(-R(1, 4))) == 0
   and sp.limit(pref, n, sp.oo) == 1/sp.pi
   and sp.simplify(sp.diff((2/sp.pi)**R(1, 2)*(2*n)**(-R(1, 4)), n)
                   + R(1, 2)*(2/sp.pi)**R(1, 2)*(2*n)**(-R(5, 4))) == 0)

# ===== M9 -- the separated-window integral L, exact and positive =====
r = sp.Symbol('r', positive=True)
aa = sp.sqrt(3)*r/2
Ival = sp.integrate(sp.integrate((y - x)**(-2), (y, r, 2*r)), (x, 0, aa))
Lsym = sp.log((4 - sp.sqrt(3))/(2*(2 - sp.sqrt(3))))
ok("M9 Int_0^(sqrt3 r/2) dx Int_r^(2r) dy (x-y)^(-2) ="
   " log((4-sqrt3)/(2(2-sqrt3))) EXACT, r-free and ell-free (proportional"
   " windows), and POSITIVE: (4-sqrt3) - 2(2-sqrt3) = sqrt3 > 0",
   sp.simplify(Ival - Lsym) == 0
   and sp.simplify((4 - sp.sqrt(3)) - 2*(2 - sp.sqrt(3)) - sp.sqrt(3)) == 0)

# ===== M10 -- the oscillatory remainder vanishes at rate 1/omega (IBP) =====
w, d1, d2 = sp.symbols('omega d1 d2', positive=True)
uu = sp.Symbol('u', positive=True)
ibp = sp.diff(sp.sin(2*w*uu)/(2*w)*uu**(-2), uu)
ok("M10 d/du[ sin(2 omega u)/(2 omega u^2) ] = cos(2 omega u)/u^2"
   " - sin(2 omega u)/(omega u^3) EXACT: Int cos(2 omega u)/u^2 du ="
   " boundary/(2 omega) + (1/omega) Int sin(2 omega u)/u^3 du -- every term"
   " O(1/omega) on u >= d > 0",
   sp.simplify(ibp - (sp.cos(2*w*uu)/uu**2 - sp.sin(2*w*uu)/(w*uu**3))) == 0)

# ===== M11 -- integral-test floor for the diagonal density sum =====
k = sp.Symbol('k', positive=True)
gap = sp.sqrt(2*(k + 1)) - sp.sqrt(2*k)
ok("M11 sqrt(2(k+1)) - sqrt(2k) = 2/(sqrt(2k+2) + sqrt(2k)) <= 2/(2 sqrt(2k))"
   " = (2k)^(-1/2) EXACT (rationalization identity + sqrt(2k+2) >= sqrt(2k)"
   " from (2k+2) - (2k) = 2 > 0): the telescoping floor"
   " Sum_(k=m)^(n-1) (2k)^(-1/2) >= sqrt(2n) - sqrt(2m)",
   sp.simplify(gap*(sp.sqrt(2*k + 2) + sp.sqrt(2*k)) - 2) == 0
   and sp.simplify((sp.sqrt(2*k + 2))**2 - (sp.sqrt(2*k))**2 - 2) == 0)

# ===== M12 -- the final budget algebra and constant assembly =====
X, Cst, ell = sp.symbols('X C ell', positive=True)
L = sp.Symbol('L', positive=True)
assembled = 4*(sp.pi*r**2/4)*(n/(2*sp.pi**2*ell**2))*(L/(4*sp.pi**2))
ok("M12 (X-2)^2 - X^2/4 = (3X-4)(X-4)/4 EXACT, so (X-2)^2 >= X^2/4 for all"
   " X >= 4 (both factors nonnegative there; sufficient direction, the only"
   " one used); (1/2)(sqrt(C n) - 2)^2 / n -> C/2; assembly 4 (pi r^2/4)"
   " (n/(2 pi^2 ell^2)) (L/(4 pi^2)) = r^2 L n/(8 pi^3 ell^2) EXACT",
   sp.expand((X - 2)**2 - X**2/4 - (3*X - 4)*(X - 4)/4) == 0
   and sp.limit(R(1, 2)*(sp.sqrt(Cst*n) - 2)**2/n, n, sp.oo) == Cst/2
   and sp.simplify(assembled - r**2*L*n/(8*sp.pi**3*ell**2)) == 0)

print("MO2-BATTERY-DONE")
```

Output, verbatim (12/12 PASS):

```text
M1 beta^2 = I, beta = beta^dag, {beta, alpha_j} = 0 (j = x,y,z), and beta C(p) beta = I - C(p) EXACTLY for the sealed symbol C(p) = (I - alpha.p-hat)/2: PASS
M2 ||[C,P]||_F^2 = 2||P-perp C P||_F^2 for Hermitian C, projection P (block decomposition [C,P] = P-perp C P - P C P-perp, exact): PASS
M3 <j|p|k> tridiagonal EXACT on levels 0..4: <k|p|k+1> = -i sqrt((k+1)/2) (ell = 1; general ell divides by ell), all other entries 0: PASS
M4 nullity(q_n p q_n) = n mod 2 at the displayed members (n = 4: 0; n = 5: 1) and det(antisymmetric odd) = 0 identically (3x3 symbolic); with the three-term-recurrence simplicity argument (text): <= 1 all n: PASS
M5 (pi_x alpha_x + pi_y alpha_y + pi_z alpha_z)^2 = (pi_x^2 + pi_y^2 + pi_z^2) I_4 EXACT for commuting pi_j (of record: the three compressed momenta act in different Hermite tensor factors): PASS
M6 CD formula k_n(x,y) = sqrt(n/2)[phi_n(x)phi_(n-1)(y) - phi_(n-1)(x)phi_n(y)]/(x-y) EXACT at n = 2,3; reproducing property Int_R k_n(x,y)^2 dy = k_n(x,x) EXACT at n = 2,3: PASS
M7 sin(u-a)cos(v) - cos(u)sin(v-b) = (1/2)[sin(u+v-a) - sin(u+v-b)] + sin(u-v+(b-a)/2)cos((a+b)/2) EXACT (the CD numerator = sin(u-v) + Lipschitz-small remainders); and sin^2(theta) - sin^2(theta-delta) = sin(delta) sin(2 theta - delta) EXACT (the pairing floor's Lipschitz ground): PASS
M8 t - sin t >= 0 on t >= 0 (h(0) = 0, h' = 1 - cos t >= 0): |sin t| <= |t|; prefactor sqrt(n/2)(2/pi)(2n)^(-1/4)(2n-2)^(-1/4) = (1/pi)(1 - 1/n)^(-1/4) EXACT, limit 1/pi; A_k = (2/pi)^(1/2)(2k)^(-1/4) decreasing in k: PASS
M9 Int_0^(sqrt3 r/2) dx Int_r^(2r) dy (x-y)^(-2) = log((4-sqrt3)/(2(2-sqrt3))) EXACT, r-free and ell-free (proportional windows), and POSITIVE: (4-sqrt3) - 2(2-sqrt3) = sqrt3 > 0: PASS
M10 d/du[ sin(2 omega u)/(2 omega u^2) ] = cos(2 omega u)/u^2 - sin(2 omega u)/(omega u^3) EXACT: Int cos(2 omega u)/u^2 du = boundary/(2 omega) + (1/omega) Int sin(2 omega u)/u^3 du -- every term O(1/omega) on u >= d > 0: PASS
M11 sqrt(2(k+1)) - sqrt(2k) = 2/(sqrt(2k+2) + sqrt(2k)) <= 2/(2 sqrt(2k)) = (2k)^(-1/2) EXACT (rationalization identity + sqrt(2k+2) >= sqrt(2k) from (2k+2) - (2k) = 2 > 0): the telescoping floor Sum_(k=m)^(n-1) (2k)^(-1/2) >= sqrt(2n) - sqrt(2m): PASS
M12 (X-2)^2 - X^2/4 = (3X-4)(X-4)/4 EXACT, so (X-2)^2 >= X^2/4 for all X >= 4 (both factors nonnegative there; sufficient direction, the only one used); (1/2)(sqrt(C n) - 2)^2 / n -> C/2; assembly 4 (pi r^2/4) (n/(2 pi^2 ell^2)) (L/(4 pi^2)) = r^2 L n/(8 pi^3 ell^2) EXACT: PASS
MO2-BATTERY-DONE
```

---

## 8. CHOICE LEDGER (Actual-Surface Guard discipline; every unforced choice, classified)

```text
CH-1 INHERITED PREMISE (r-2 CH-A: C_n = the pure Hermite vacuum
     projection): PREMISE(named), inherited at the clause's own display,
     exactly as r-3 CH-g inherited it — AND made IMMATERIAL(derived) for
     the rate itself by scheme-robustness: the mixed family Q_n P_- Q_n
     obeys the cleaner bound kappa_n^mix >= C_* n/2 (§2.4 (**), no kernel
     correction), so the linear growth law holds under BOTH sealed
     realizations. Load-bearing only for attaching the rate to the s_i /
     det_n(0) displays (V-N3-protected, as of record).
CH-2 THE WINDOW CONSTANTS a = (sqrt3/2) r, R = 2r, transverse radius r/2:
     YOURS (unforced). Any 0 < a < r, R > r, transverse radius < r yields
     the same GAMMA = 1 with a different symbolic constant; these values
     are chosen for exact closed forms (s(x_perp) >= a is exact at
     |x_perp| = r/2; L is r- and ell-free). The rate statement is
     window-independent; only C_* moves.
CH-3 ZERO-MODE CONVENTION: IMMATERIAL(derived) — the bound holds for ANY
     self-adjoint 0 <= z_n <= Z_n (the correction W_n has rank <= 4 by
     the EXACT kernel computation §2.3, contributing the O(1) additive
     term only). This upgrades r-2's per-member convention note to an
     exact all-convention statement.
CH-4 THE beta REPRESENTATION: IMMATERIAL(derived) — any Hermitian unitary
     anticommuting with the three alphas gives the identical conjugation
     algebra; one explicit witness displayed (M1); no representation-
     dependent quantity survives into any displayed bound.
CH-5 CLASSICAL GROUND CL-A: the commission's own authorized ground
     (PR-type asymptotics "admissible classical ground the way LSC was");
     consumed cited-not-rederived with every used consequence derived
     exactly (§3-§4); the sweep (s-4) shows no sealed substitute exists.
     Classification: FORCED-shape given the commission text; the SCOPE of
     the citation (fixed-compact wave form with uniform o(1) error) is
     the minimal statement sufficient, and nothing wider is consumed.
CH-6 THE FLOOR FRACTIONS (theta = 1/2 in the diagonal floor; L/(4 pi^2)
     as half the limit; X >= 4 as the budget threshold): IMMATERIAL
     (derived) — any fractions in (0,1) work; they trade the constant
     against N_0, and neither is claimed sharp or extracted.
CH-7 THE ADOPTED CLAUSE NOT OPENED: its content enters only via r-2/r-3's
     sealed-and-audited quotes (as in the linkage lane's CH-5).
     IMMATERIAL(derived) for every displayed bound.
MACHINERY/RELEVANCE (guard append honored): the machinery is classical
     spectral algebra (an exact involution, functional calculus, block
     decompositions) plus ONE cited classical asymptotic, applied to the
     SEALED constructions with booked surface traces (G-1, G-5, G-6);
     SURFACE-DERIVED, not surface-native; no surface verdict is anchored
     beyond the named inherited premise (CH-1).
```

## 9. TOY_SEPARATION (self-assessment)

```text
CLAIMED CLEAN at the stated quantifiers. Every load-bearing input is the
ACTUAL sealed family's structure: the actual carrier (PA A1 cube => exact
product projector), the actual massless generator (PA A1 bytes), the
actual sharp ball (C4/D6'), the actual C_n realization (r-2 CH-A,
inherited and scheme-robustified). The CAS instances are IDENTITY-GRADE
exhibits of all-matrix/all-scalar identities, each displayed with its
universal quantifier in the check name (M1/M2/M5 explicit-matrix or
symbolic-Hermitian identities; M3/M6 exact Gaussian-integral evaluations
of the actual 1D objects at displayed members, with the general-n
statements derived in text from the exact ladder algebra and CD theory;
M4's parity displayed at members PLUS the all-n recurrence argument in
text; M7-M12 exact identities/inequalities with exact solution sets or
factorizations). The classical ground CL-A is cited at its own classical
quantifier and consumed no wider than stated. No toy family stands in for
the actual family anywhere; no instance is promoted beyond its display;
no spectral datum of the actual family is valued numerically. The RULING
is the checker's/audit's, not this artifact's.
```

---

## 10. FLAG BLOCK

```text
MO2_KAPPA_RATE = DERIVED( certified lower growth law, gamma = 1: for the
  carrier compression family of record, per admitted state and cell, at
  every collapse-bearing cell time r = r(t) > 0, each frozen ell in
  {1, sqrt2}, all four opposite-phase pairs at once:
    liminf_n kappa_n / n >= C_*(r, ell)/2 > 0,  and
    kappa_n >= C_*(r, ell) n / 8 for all n >= N_0(r, ell),
    C_* = r^2 L/(8 pi^3 ell^2),  L = log((4 - sqrt3)/(2(2 - sqrt3))) > 0
  (all constants symbolic exact; N_0 exists by the classical thresholds,
  not extracted; sharpness NOT claimed). Scheme-robust: mixed family
  kappa_n^mix >= C_* n/2. DETERMINANT FORM: -log|det_n(0)| >= C_* n/8,
  i.e. |det_n(0)| <= exp(-C_* n/8), n >= N_0 (of-record chain
  -log|det| >= kappa_n). )
NEW_INPUT_NAMED = TWO( (i) the EXACT chiral involution: beta with
  {beta, alpha_j} = 0 anticommutes with the massless h_0 of record,
  commutes with Q_n and P, gives beta C_n beta = Q_n - C_n - (rank <= 4
  correction, kernel dimension computed EXACTLY = 4(n mod 2) via the
  commuting compressed momenta and the unreduced-tridiagonal nullity
  bound) => kappa_n >= (1/2)(||P^perp Q_n P||_2 - 2)^2: the
  un-diagonalizable spectral projection is eliminated for the EXPLICIT
  Hermite projector; (ii) ONE classical ground CL-A (Plancherel-Rotach
  fixed-compact asymptotics, commission-authorized, cited as classical,
  everything used derived exactly from it): crossing mass
  ||P^perp Q_n P||_2^2 >= C_* n via region-shrink positivity + the exact
  reproducing identity + the diagonal density floor + the separated-
  window wave floor. Sweep s-2: no chiral carrier exists anywhere in the
  corpus — the involution is genuinely new input, contradicted by
  nothing sealed. )
CONSUMPTION_BOUNDARY = NOTHING-FIRED( this is the MO-2 candidate input of
  r-3's missing-object list, supplied; the registrar consumes. r-3 NOT
  discharged (Route 1 still needs MO-1 + MO-3; the direct package still
  needs MO-4 — with this input the direct package lacks ONLY MO-4);
  R-L4b NOT discharged; all three R-L4 witnesses STAND; no flag flipped,
  no witness retired, no gate moved. Route-1's rank x op obstruction is
  NOT revived: (4n^3 c(eps_*))/(C_* n/8) grows like n^2 (consistent with
  r-3 D10). )
CONSISTENCY = CHECKED-EXACT( X-1 linear floor under the exact cubic
  ceiling kappa_n <= 2n^3; X-2 r-2's B1-DERIVED divergence RECOVERED
  with a rate at the full-family quantifier, method bypassed not
  corrected; X-3 r-3's Route-1 obstruction intact, MO-2 slot filled as
  candidate; X-4 the check's n-1 single-eigenvalue shape consistent (sum
  statement vs member statement); X-5 stricken display consumed nowhere,
  C6 not even needed as ground (its locus appears only as displayed
  consistency); X-6 kappa_record untouched — kappa_n is the clause's
  collapse mass, no record-curvature value appears. )
SWEEP_CUTOFF = DECLARED( 2026-08-14 23:14:15 CDT; both corpus roots,
  fenced name classes excluded; keys displayed §5.2; artifacts sealed
  after cutoff not consumed; MO-2 unoccupied at cutoff by all parallel
  S9AD lanes (their own flags quoted); no kappa_n rate carrier exists;
  no chiral carrier exists; CL-A has no sealed substitute. )
SEALS_VERIFIED = 7/7( 3b5e95b6 r-2; a4cf394c r-2 audit; bebc0f08 r-3;
  72c95d42 r-3 audit; 46846730 E1; 789338ad PA; 3de0502c rate-gap
  linkage — all sidecar-matched at path this session; commission pins
  reproduced. EXPECTED-UNLOCATABLE register tokens noted, not chased. )
FORBIDDEN_IMPORTS = none( exact symbolic only; no floating-point numerics
  as ground; no measured constant; NO value frozen — the result is an
  exponent/asymptotic statement with symbolic constants (C_*, L, N_0
  displayed as symbols/closed forms, N_0 not extracted); M(t)/1_{D_t}
  sharp; the stricken display consumed nowhere; no register/road_/
  ledger/lens/plan/tracker/THE_HANDOFF file opened; no git action; no
  existing file edited; ONE file written plus its seal;
  commission-distinct path S9AD probed ABSENT at start and re-probed
  before write. )
MACHINERY_INVOKED = yes(CAS) — sympy 1.14.0, fresh venv mo2venv under the
  session scratchpad; final run ONCE, 12/12 PASS, script and output
  reproduced verbatim in §7; one pre-final check-form correction (M12
  "iff" narrowed to the sufficient direction actually used) disclosed,
  no derivation step changed.
alpha_computed = false ; proof_authorized = false ;
kappa_record_computed = false
ALL_RESULTS = CLAIMED until checked.
MO2_KAPPA_RATE_RESULT = SEALED.
```
