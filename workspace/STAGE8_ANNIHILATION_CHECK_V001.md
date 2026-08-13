# STAGE 8 — ANNIHILATION-CHECK: ADVERSARIAL VERIFICATION OF THE PROJECTOR-SANDWICH ANNIHILATION CLAIM

## BLIND ADVERSARIAL VERIFIER — CROSS-LINEAGE — [SEALED]

Date: 2026-08-13
Role: BLIND adversarial verifier (ANNIHILATION-CHECK), cross-lineage. DEFAULT = REFUTE.
Target: the single new positive structural claim of STAGE8_CANC_PANEL_SYMHUNT_V001.md —
that the projector sandwich X = C(V(a)-V(0))C annihilates the difference's leading
survivor EXACTLY at principal-symbol level, leaving only degree <= -1 locally. Five
attacks executed at byte spans: (1) the projector identification, (2) the transversality
of the leading symbol, (3) the anticommutation step and the longitudinal fate, (4) the
post-annihilation degree count, (5) provenance. Every algebraic step was RE-DERIVED
independently here, not accepted from the claim.

Gates: `alpha_computed = false` ; `kappa_record_computed = false` ;
`proof_authorized = false` ; `coupling_evaluation_authorized = false`

Fences held: connection-only, symbolic. NO value of n, kappa_record, alpha (coupling),
any exponent, norm, scale, length, or spectrum computed, bounded, or evaluated — the work
below is exact symbolic Fourier/Clifford algebra on sealed forms and degree/parity
bookkeeping; sealed constants (1/2, 2 pi^2) carried verbatim, never evaluated. No
scale/GR/faithfulness used as authority; scale-bearing sealed text (ECO/RFA) read
SUSPECT-ONLY, to verify the claim's grounding at its cited bytes. No register/tracker/
plan/road/ledger/lens read. STAGE8_CANC_PANEL_STRUCTURE_V001.md and
STAGE8_CANC_PANEL_CLASSIFICATION_V001.md NOT OPENED (blind to co-panelists; their
existence at path noted from directory listing only). Output name probed before write:
ABSENT. No git action.

---

## 0. VERDICT IN ONE LINE

**ALL FIVE ATTACKS FAIL. The claim survives at exactly the level it asserts and no
further: C of record IS the exact sea projector (FT of the sealed kernel recomputed:
C_hat(k) = (1/2)(I - alpha.k_hat), spectrum {0,1}); the leading survivor's symbol IS
purely transverse with ZERO scalar and ZERO longitudinal component (the longitudinal
candidate cancels inside the exact k-derivative of the unit vector, upstream of the
sandwich, by algebra — not by definition, not by Ward); the annihilation
(I-M)(alpha.ell_perp)(I-M) = 0 is exact and its load-bearing dependence on
transversality was adversarially confirmed (a surviving scalar or longitudinal part
would NOT be killed — and there is none); the post-annihilation local degree is <= -1
at frozen write current, with the derivative-of-ell corrections correctly and
explicitly scoped to FORM's G3 NOT-SUPPLIED datum, not silently assumed smooth.
ANNIHILATION_VERDICT = CONFIRMED at principal-symbol level, conditional (as the claim
itself declares) on the CANC build's B1 survivor form. PROVENANCE = CLEAN.**

---

## 1. SEALS RECOMPUTED AT PATH (shasum -a 256), BEFORE READING

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`. Full digests recomputed
at path this session; first 16 hex shown.

```text
CLAIM UNDER ATTACK:
  STAGE8_CANC_PANEL_SYMHUNT_V001.md
    564b7040bf51da4e7aec5b00d940b5e0215a9327ebbb2cd04947c568f8c9ae50  MATCHES-TASKED
TASKED SECONDARY:
  STAGE8_REQUIRE_BUILD_CANCELLATION_V001.md
    4971e2739666bd95917163763f42cadf427442a7c710f8b22353d65ead9fe5fe  MATCHES-TASKED (CANC)
  STAGE8_R_RECORD_L_FORM_FABLE_V001.md
    5e49d2093d4ee17b840cc096d5caf3a6edafda4e37abbd175a7a371c34658f37  MATCHES-TASKED (FORM)
FROM THE CLAIM'S/BUILD'S REFERENCES, recomputed at path:
  STAGE8_EXTENSIVITY_VERDICT_AND_RL2B_CAMPAIGN_OPENING_V001.md (ECO)
    0f3082cab910f2eb6769698fc03cdb0201830c2551ecd8201fa6748b24e07505  MATCHES claim-recorded
  STAGE8_RL2B_FRAME_ANSWER_AND_CAMPAIGN_TARGET_V001.md (RFA)
    2ede02aea415157ada9edd6f685aabcc824acf2716777f4aa2dc98467fe92840  MATCHES claim-recorded
```

Five seals verified, all matching. Citation-accuracy spot-checks at the bytes, all
verified against the actual line numbers: ECO :153-155 (kernel + EXACT modulus + op
norm), :158-159 (HS integrand), :174 (the sandwich), :192 (two-projection identity),
:195-201 (commutator route, ROUTE_NOT_LEMMA), :222 (sea_projector flag); RFA :33
(diagonal internal to every diamond), :66-67 (HS norm spatial), :119-121, :126-128,
:137-138 (UNKNOWN); CANC :183-214 (mechanisms A-D), :234-242 (the declined
composition); FORM :96-113 (B5/B6), :168 (D2), :180-199 (D3), :208-209/:230 (D4),
:241-242 (D5), :277-281 (G3 NOT SUPPLIED), :348-357 (4.4), :384-385 (5.1 pt 4). One
citation is off by one line (claim cites D4 :231 for "scales as n^2 and as nothing else
in n", actual :230) — immaterial.

---

## 2. ATTACK 1 — THE PROJECTOR IDENTIFICATION: FAILS (C IS THE PROJECTOR OF RECORD)

The question: is the C in the sealed HS object the exact sea projector, or a different
object (cutoff/endcap, smeared projector, density matrix with sigma in (0,1)) — in
which case (I-M)A(I-M) = 0 fails?

**2.1 The Fourier transform, recomputed independently from the sealed kernel.** ECO
:153, verbatim: `C(r) = (1/2) delta^3(r) I - i alpha.r / (2 pi^2 |r|^4)`. With
convention `f_hat(k) = int e^(-ik.r) f(r) d^3r`:

```text
FT[|r|^-2]      = 2 pi^2/|k|         (exact 3D identity: 2^(3-a) pi^(3/2)
                                      Gamma((3-a)/2)/Gamma(a/2) |k|^(a-3) at a = 2)
r/|r|^4         = -(1/2) grad(|r|^-2)          (grad|r|^-2 = -2r/|r|^4, exact)
FT[d_m f]       = i k_m f_hat                  (this convention, exact)
FT[r/|r|^4]     = -(1/2)(ik)(2 pi^2/|k|) = -i pi^2 k_hat
FT[C_off]       = (-i/(2 pi^2)) alpha.(-i pi^2 k_hat) = -(1/2) alpha.k_hat
C_hat(k)        = (1/2)(I - alpha.k_hat)                                    [RECOMPUTED]
```

This MATCHES the claim's §3.2 exactly. Step independent of the claim's text.

**2.2 Idempotency: grounded, and the alternatives excluded at the bytes.**
`C_hat^2 = C_hat` iff `(alpha.k_hat)^2 = I`. The Clifford relation is not a verbatim
sealed line; it is FORCED by four independent sealed facts, jointly:

```text
(i)   ECO :154: "off-diagonal modulus EXACTLY 1/(2 pi^2 |r|^3)" — a single scalar
      modulus for a matrix-valued kernel means C_off(r)^dagger C_off(r) =
      (modulus)^2 I, i.e. ALL singular values of alpha.r_hat equal 1 (corroborated by
      :158-159: the HS integrand is the single scalar 1/(4 pi^4 |r|^6), no spread).
(ii)  Hermiticity: the kernel is the SEA COVARIANCE (ECO :151; FORM D5 :246-248 types
      the Gate-5 kernel "symmetric and positive-semidefinite ... covariance").
      C(x,y) = C(y,x)^dagger requires C(-r) = C(r)^dagger, which on the sealed form
      holds iff alpha^dagger = alpha. Hermitian + all singular values 1 forces
      (alpha.r_hat)^2 = I for every direction — the Clifford relation.
(iii) ECO :192: ||[C,P]||_2^2 = 2 sum_i sigma_i(1 - sigma_i), "verified on 50 exact
      trials" — the exact two-projection formula, EXACT only when C is an orthogonal
      projection. The corpus's own worked case treats C as an exact projector.
(iv)  ECO :222: `sea_projector_restricted_to_a_diamond_is_HS = false` — the corpus's
      own name for C is PROJECTOR.
```

**2.3 The adversarial alternatives, each excluded.**
- *Density matrix with sigma in (0,1)?* The recomputed FT has eigenvalues
  (1 -/+ 1)/2 = {0, 1} exactly — NOT in (0,1). The sigma_i in ECO :192 are eigenvalues
  of the COMPRESSION of one projector by the other (that is what the two-projection
  formula sums over); they measure [C,P] != 0, not any non-idempotency of C. A genuine
  density-matrix C would deform the sealed kernel's radial profile away from EXACTLY
  1/(2 pi^2 |r|^3) — contradicting ECO :154's "EXACTLY".
- *Cutoff/endcap/smeared C_n?* NO competing sealed definition exists anywhere in the
  reference chain: RFA contains no "C_n", no smearing, no mollification, not even the
  word "projector" (grepped); the wall (STAGE8_REQUIRE_BUILD_CLUSTER_SUMMABILITY :8)
  names only "the Gate-5 connected cluster covariance kernel C"; CANC :7's "C_n" is the
  CANC builder's own subscript notation for that same object at winding n. The ONLY
  kernel of record is ECO :153. A smeared variant would again break :154's "EXACTLY".
- *Diamond restriction spoiling idempotency?* The restriction sits at the diamond
  boundary; the singularity under test is at the INTERIOR diagonal (RFA :33: "r -> 0 IS
  INTERNAL TO WHATEVER DIAMOND ONE IS IN"), where the restriction indicator is locally
  identically 1 — the local symbol algebra at the interior diagonal is that of the
  unrestricted C. The claim's §3.1 says exactly this; verified against RFA :33.

**ATTACK 1 FAILS. PROJECTOR_OF_RECORD = CONFIRMED** (ECO :153-155, :158-159, :192,
:222; FORM :246-248). Honest residue, stated for future lenses: the Clifford relation
is an inference forced by (i)+(ii), not a verbatim sealed anticommutator line; it is,
however, the UNIQUE matrix structure compatible with the sealed EXACT modulus, the
covariance typing, and the exact two-projection identity of record.

---

## 3. ATTACK 2 — TRANSVERSALITY OF THE LEADING SYMBOL: FAILS (NO SCALAR, NO LONGITUDINAL PART)

The highest-value attack: does a scalar (identity-component) or longitudinal
(alpha.k_hat-parallel) piece survive in the leading symbol — which the sandwich would
NOT kill? Worked honestly, independently, from the B1 survivor form
`D_lead(r) = i n <ell,r> C_off(r) = n <ell,r> alpha.r/(2 pi^2 |r|^4)` (real, even,
degree -2 — recomputed: odd x odd = even, +1 + (-3) = -2):

```text
FT[r_m f]  = i d/dk_m f_hat        (this convention, exact)
D_hat(k)   = i n ell_m . i d/dk_m [ -(1/2) alpha_j k_hat_j ]
           = (n/2) ell_m alpha_j . d/dk_m ( k_j/|k| )
d/dk_m (k_j/|k|) = delta_mj/|k| - k_j k_m/|k|^3 = (delta_mj - k_hat_m k_hat_j)/|k|
D_hat(k)   = (n/(2|k|)) [ alpha.ell - (alpha.k_hat)(k_hat.ell) ]
           = (n/(2|k|)) alpha.ell_perp                                      [RECOMPUTED]
```

MATCHES the claim's §3.3 exactly. Now the two dangerous components, checked one by one:

```text
SCALAR (identity) part:  ZERO, by construction of the algebra. The FT of C_off is
  purely a Clifford VECTOR (-(1/2) alpha.k_hat — no identity component; the identity
  component of C sits entirely in the delta term). Multiplication by <ell,r> is scalar;
  the k-derivative keeps the symbol in span{alpha_j} with scalar coefficients. NO
  product of two alpha matrices is ever formed — the only way an identity component
  could arise (alpha_m alpha_j = delta_mj I + ...) — so the identity component of
  D_hat is EXACTLY 0. And the delta term contributes nothing to D_lead at any phase
  order: r_m delta^3(r) = 0 exactly as a distribution, so
  i n <ell,r> . (1/2) delta^3(r) I = 0 EXACTLY.
LONGITUDINAL part:  ZERO, cancelled INSIDE the exact algebra. The delta_mj/|k| term
  alone would contribute the full alpha.ell (including its longitudinal component
  (alpha.k_hat)(k_hat.ell)); the -k_hat_m k_hat_j/|k| term of the unit-vector
  derivative cancels that longitudinal component IDENTICALLY, at every k. Nothing was
  "projected out and discarded" — ell_perp is the RESULT of the algebra, not a
  definition imposed on it.
Consistency checks: D_lead real+even => D_hat real+even: (n/(2|k|)) alpha.ell_perp is
  real, and even in k (ell_perp(-k) = ell_perp(k), 1/|k| even). Kernel degree -2 in
  3D => symbol degree -1: matches. Convention flip e^(+ik.r): k -> -k, still
  transverse. Overall sign flip of the sealed kernel: C_hat -> (1/2)(I + alpha.k_hat),
  still a projector; (I+M)A(I+M) = A(I-M)(I+M) = A(I - M^2) = 0 — annihilation
  survives every convention.
```

**ATTACK 2 FAILS. LEADING_SYMBOL_TRANSVERSE = CONFIRMED** — the leading symbol is
exactly `(n/(2|k|)) alpha.ell_perp`; the scalar part is exactly zero and the
longitudinal part is exactly zero, both by recomputed algebra, not by assumption.

---

## 4. ATTACK 3 — THE ANTICOMMUTATION STEP AND THE LONGITUDINAL FATE: FAILS

**4.1 The anticommutator, pointwise.** `{alpha.k_hat, alpha.ell_perp} =
2 (k_hat.ell_perp) I` by the Clifford relation (§2), and `k_hat.ell_perp =
k_hat.ell - (k_hat.k_hat)(k_hat.ell) = 0` IDENTICALLY for every k and every ell — an
algebraic identity of the decomposition, pointwise in k-space, requiring no property
of ell whatsoever. The anticommutation step is exact.

**4.2 Is "ell_perp" a definition hiding a discarded longitudinal remainder?** NO —
this is the decisive point, established in §3: the full leading symbol IS
`(n/(2|k|)) alpha.ell_perp` with nothing left over. The longitudinal component of
`alpha.ell` is cancelled inside the exact k-derivative of the unit vector
(`d k_hat_j/dk_m` is itself the transverse projector divided by |k|), UPSTREAM of the
sandwich, at the same degree (-1). There is no longitudinal remainder whose "fate"
needs a second mechanism. No Ward identity, no gauge move, no d ell = 0 input is used
or needed at this step (the claim likewise never invokes one here — checked).

**4.3 The load-bearing converse, adversarially confirmed.** Had a longitudinal or
scalar piece survived at degree -1, the sandwich would NOT kill it — computed exactly,
with M = alpha.k_hat, M^2 = I:

```text
scalar:        (I-M)(I)(I-M)  =  (I-M)^2  =  2(I-M)          != 0
longitudinal:  (I-M)(M)(I-M)  =  -(I-M)^2 =  -2(I-M)         != 0
transverse:    (I-M)(alpha.ell_perp)(I-M)
               = (alpha.ell_perp)(I+M)(I-M)    [anticommutation]
               = (alpha.ell_perp)(I - M^2) = 0                EXACTLY
```

The annihilation genuinely stands or falls on exact transversality — and transversality
holds exactly (§3). The claim's four-term convolution display (§3.4) also re-derived:
with C_hat = (1/2)I - (1/2)M and A = alpha.ell_perp: the delta-delta term (1/4)A, the
cross terms -(1/4)(MA + AM) = 0 by anticommutation, and the off-off term
(1/4)MAM = -(1/4)M^2 A = -(1/4)A, cancelling the delta-delta term exactly — the
claim's term-by-term reading is verbatim correct. The interband identity of §3.5 also
re-derived: for PAP = (I-P)A(I-P) = 0, [P,[P,A]] = PA + AP - 2PAP = PA(I-P) +
(I-P)AP = A exactly — so the difference's leading part IS commutator-shaped, and the
claim's statement that ECO :195-197's structural premise is proved AT PRINCIPAL-SYMBOL
LEVEL is accurate as scoped (no bound, no exponent claimed — none is).

**ATTACK 3 FAILS. LONGITUDINAL_FATE = CANCELS_BY(exact Fourier algebra upstream of the
sandwich — the unit-vector derivative is itself the transverse projector; no Ward/gauge
mechanism used or needed; nothing discarded).**

---

## 5. ATTACK 4 — THE DEGREE COUNT AFTER ANNIHILATION: FAILS (SCOPE VERIFIED HONEST)

Is "everything remaining locally is degree <= -1, HS-integrable" true — and are the
frozen-coefficient corrections silently assumed smooth?

**5.1 At frozen write current (exact, term by term).** The full difference kernel at
frozen ell is `[exp(i n<ell,r>) - 1] C(r)` plus O(r^2)-phase corrections:

```text
(a) all phase orders x delta part:  r_m^p delta^3(r) = 0 for p >= 1 — EXACTLY ZERO,
    every order. (And [exp(i.0)-1] kills the p = 0 term.)
(b) second-and-higher phase orders x C_off:  |exp(ix) - 1 - ix| <= x^2/2, so the
    remainder beyond D_lead is kernel degree >= (+2) + (-3) = -1. Its square is
    degree >= -2; int d^3r r^2 . r^-2 ~ int dr converges at 0 — locally HS at the
    diagonal, by symbolic order alone.
(c) the annihilated leading term:  at frozen ell all three factors are convolution
    operators; composition = symbol product in order; C_hat D_hat C_hat = 0 at EVERY k
    means C D_lead C is the ZERO OPERATOR at frozen coefficients — stronger than
    "lower degree". (Noted: the claim asserts only the symbol-level zero; the
    frozen-coefficient statement is in fact exact.)
(d) O(r^2) phase term x C_off:  kernel degree -1 — same count as (b) — but its
    coefficient carries DERIVATIVES OF ell. See 5.2.
(e) sandwich stability: C_hat is a bounded matrix symbol (projector, op norm 1), so
    sandwiching the locally-HS remainder by C preserves local HS-ness.
```

**5.2 The derivative-of-ell corrections — exactly the G3-unsupplied data, and NOT
silently assumed smooth.** Symbol-calculus corrections to the frozen-coefficient
approximation carry one derivative of ell per order and drop one degree in k per
derivative (symbol degree -2 <-> kernel degree -1) — the count is right IF ell is
smooth. Of record, ell_j is the cell-history write chain whose support/current-density
realization is NOT SUPPLIED: FORM B7 :117-118 ("RA27-3's support and current density
fields: NOT SUPPLIED"), FORM G3 :277-281, FORM 4.4 :348-357. If ell is cell-piecewise,
its derivative is face-localized and distributional, and smooth-symbol degree
bookkeeping does NOT cover the faces. The claim does NOT hide this — verified at its
bytes: §3.6 "The subleading terms carry derivatives of ell(x) — ... exactly FORM's G3,
'NOT SUPPLIED' of record ... If ell is cell-piecewise, the corrections are
face-localized, and their HS fate is a genuine metric/analytic computation, not
symmetry", repeated in the flag block, with RFA :137-138's UNKNOWN kept standing,
relocated one order down. The degree <= -1 statement is therefore CONFIRMED as what it
claims to be: a LOCAL statement at the diagonal, at frozen write current, with the
ell-derivative corrections explicitly fenced out as the open non-symmetry remainder.
The IR/boundary (diamond-restriction) side is likewise explicitly left open. No silent
smoothness import found.

**ATTACK 4 FAILS. POST_ANNIHILATION_DEGREE = CONFIRMED(<= -1 locally at frozen ell;
the ell-derivative corrections are exactly the declared G3-unsupplied remainder).**

---

## 6. ATTACK 5 — PROVENANCE: CLEAN

```text
The claim's algebra audit (§7) verified at its bytes and against my own re-derivation:
  every Fourier identity used is exact and standard; sealed constants carried
  symbolically; no numeric evaluation anywhere in the claim's §3 (the only numerics in
  the chain are ECO :162-165's sealed cutoff table, quoted by CANC, used by the claim
  only as sealed classification text, never as authority for the algebra).
My own machinery: shasum -a 256, file reads, grep for definition-existence probes, and
  exact symbolic re-derivation by hand. Nothing computed, bounded, estimated, or
  evaluated; no scale used as authority; no register/tracker/plan/road/ledger/lens
  read; co-panelist artifacts not opened.
Observation, recorded without verdict weight: directory mtimes show
  STAGE8_CANC_PANEL_CLASSIFICATION_V001.md written 11:44, the claim written 11:46. The
  claim's "no panel file existed at path when probed" cannot be confirmed or refuted
  from bytes (a pre-11:44 probe at session start is fully consistent); no content
  dependency on any panel artifact is detectable in the claim, and every load-bearing
  step re-derives here independently — so this cannot break the verdict.
Conditionality, re-stated as the claim states it: the whole finding is conditional on
  CANC B1's survivor form (i n<ell,r> x C_off). If B1 falls, the annihilation is moot
  in the same stroke. This check did not re-verify B1 (other lenses' remit) and adds
  no authority to it.
```

---

## 7. FLAG BLOCK

```text
PROJECTOR_OF_RECORD = CONFIRMED(ECO :153 kernel's Fourier transform recomputed
  independently: C_hat(k) = (1/2)(I - alpha.k_hat), spectrum {0,1} — exact idempotent;
  the Clifford relation (alpha.k_hat)^2 = I is forced jointly by the sealed EXACT
  scalar modulus + op norm (ECO :154-155), the single-scalar HS integrand (:158-159),
  and the Hermitian covariance typing (ECO :151; FORM D5 :246-248); corroborated by
  the exact two-projection identity (ECO :192, exact only for orthogonal projections,
  verified of record on 50 exact trials) and the sea_projector flag (:222). The
  adversarial alternatives fail at the bytes: a density matrix with sigma in (0,1)
  contradicts the {0,1} FT spectrum and :154's "EXACTLY" (the sigma_i in :192 are
  compression eigenvalues, not C's); no sealed cutoff/endcap/smeared C_n exists
  anywhere in the reference chain — CANC :7's "C_n" is the builder's notation for the
  one kernel of record; diamond restriction is boundary-localized while the tested
  singularity is at the interior diagonal (RFA :33).)

LEADING_SYMBOL_TRANSVERSE = CONFIRMED(recomputed independently from the B1 form:
  D_hat(k) = (n/2) ell_m alpha_j (delta_mj - k_hat_m k_hat_j)/|k| =
  (n/(2|k|)) alpha.ell_perp — real, even, degree -1. SCALAR part EXACTLY ZERO: the
  algebra never forms a product of two alpha matrices (the only source of an identity
  component), and the delta term contributes nothing at any phase order
  (r^p delta^3(r) = 0, p >= 1, exact). LONGITUDINAL part EXACTLY ZERO: the unit-vector
  derivative d k_hat_j/dk_m = (delta_mj - k_hat_m k_hat_j)/|k| is itself the
  transverse projector — the longitudinal component of alpha.ell is cancelled
  identically inside the exact Fourier algebra. Convention-robust (FT sign, kernel
  sign both checked).)

LONGITUDINAL_FATE = CANCELS_BY(exact Fourier algebra UPSTREAM of the sandwich: the
  would-be longitudinal piece (alpha.k_hat)(k_hat.ell)/|k| from the delta_mj term is
  annihilated identically by the -k_hat_m k_hat_j term of the unit-vector derivative,
  at the same degree (-1), at every k — an algebraic identity, not a definition that
  discards a remainder, and NOT a Ward/gauge mechanism (d ell = 0 is neither used nor
  needed at this step). Adversarially confirmed load-bearing: had a longitudinal
  (resp. scalar) piece survived, the sandwich would NOT kill it —
  (I-M)M(I-M) = -2(I-M) != 0, (I-M)I(I-M) = 2(I-M) != 0 — so the annihilation
  genuinely rests on exact transversality, which holds.)

POST_ANNIHILATION_DEGREE = CONFIRMED(<= -1 locally at the diagonal, at frozen write
  current — verified term by term: all phase orders x delta part = 0 exactly
  (r^p delta^3(r) = 0); phase remainder beyond first order x C_off is kernel degree
  >= -1 (|exp(ix)-1-ix| <= x^2/2, symbolic), |.|^2 degree >= -2, int r^2 r^-2 dr
  converges — locally HS; at frozen coefficients the annihilated leading sandwich is
  in fact the ZERO OPERATOR (convolution composition = ordered symbol product),
  stronger than the claim needs; sandwiching by the bounded projector preserves local
  HS-ness. The frozen-coefficient corrections carry derivatives of ell, one degree
  down per derivative — and the claim does NOT silently assume ell smooth: it names
  these corrections as exactly FORM's G3 NOT-SUPPLIED write-chain realization
  (FORM B7 :117-118, G3 :277-281), face-localized if ell is cell-piecewise, a genuine
  non-symmetry computation left open, with RFA :137-138's UNKNOWN standing relocated.
  Scope declaration verified honest and necessary.)

ANNIHILATION_VERDICT = CONFIRMED(at exactly the claimed level and no further: the
  principal symbol of C(V(a)-V(0))C vanishes IDENTICALLY —
  (I-M)(alpha.ell_perp)(I-M) = (alpha.ell_perp)(I - M^2) = 0 exactly, every k, every
  cell, every n; the four-term display re-derived exactly ((1/4)D killed by
  C_off*D*C_off = -(1/4)D, cross terms zero by anticommutation); the survivor is
  purely INTERBAND and the identity A = [C,[C,A]] re-derived exactly, so ECO
  :195-197's commutator-route structural premise IS proved at principal-symbol level
  as claimed. CONDITIONAL, as the claim itself declares, on CANC B1's survivor form
  (not re-verified here — other lenses' remit); NOT full cancellation, NOT alpha
  forced, NOT alpha = 1 — the G3 ell-derivative remainder and the IR/boundary side
  remain open of record, exactly as the claim scopes them.)

PROVENANCE = CLEAN(five seals recomputed at path before reading, all matching; every
  load-bearing algebraic step re-derived independently and exactly — no step accepted
  on the claim's authority; sealed constants carried symbolically, nothing evaluated;
  scale-bearing ECO/RFA read suspect-only at the claim's cited bytes; no
  register/tracker/plan/road/ledger/lens read; co-panelist artifacts NOT opened; the
  mtime observation on the claim's blindness probe is recorded in §6 without verdict
  weight — no content dependency exists and all algebra re-derives. No git action.)

MACHINERY_USED_BY_ME = no(shasum -a 256, file reads, and existence-probe greps only;
  all algebra exact symbolic by hand; no value of n, kappa_record, alpha, any
  exponent, norm, scale, or spectrum computed, bounded, estimated, or evaluated.)

alpha_computed = false ; kappa_record_computed = false ; proof_authorized = false ;
coupling_evaluation_authorized = false
ANNIHILATION_CHECK_RESULT = SEALED.
```
