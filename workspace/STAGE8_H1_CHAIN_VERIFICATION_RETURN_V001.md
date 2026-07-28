# H1 Chain Verification Return V001 — Two Steps Verify, One Has a Named Missing Input

STATUS: LANE VERIFICATION RETURN. **THE REFUTATION IS NOT SEALED.**
LANE: EINSTEIN. CHARTER: PASTE #108, steps 1–3, with the standing instruction *"IF ANY STEP FAILS,
REPORT THE FAILURE AND SEAL NOTHING."*
DATE OF RECORD: 2026-07-28.

```text
alpha_computed = false ; proof_authorized = false ;
coupling_evaluation_authorized = false ; kappa_record_computed = false
R-L2b IS NOT DECLARED REFUTED BY THIS ARTIFACT. THE PROGRAM IS NOT DECLARED BLOCKED OR DEAD.
```

---

## §0 — THE RETURN

```text
STEP 3  ||X||_2 = infinity AT SOURCE            *** VERIFIED. ***
STEP 2  THE SETTING MATCHES                     *** VERIFIED, WITH THREE CORRECTIONS.
                                                    ONE IS MATERIAL TO A ROUTE, NONE TO A CONCLUSION. ***
STEP 1  THE PRODUCT STEP                        *** HALF-VERIFIED. THE C-FACTORS CLOSE.
                                                    THE V-FACTOR HAS NO SEALED UNIFORM BOUND. ***

=> THE CHAIN IS ONE NAMED LEMMA SHORT. IT IS NOT BROKEN AND IT IS NOT COMPLETE.
```

**AND ONE FINDING THAT NEITHER LANE COULD HAVE HAD:** referral 2's conclusion **was already derived
in this corpus on 2026-07-24**, four days before the referral (§4). That is independent blind
confirmation of a sealed result — the strongest corroboration available — and it means the gap the
principal identified was a **WIRING GAP, NOT A MISSING RESULT.**

---

## §1 — STEP 1. THE PRODUCT STEP. **THE C-FACTORS CLOSE; THE V-FACTOR DOES NOT.**

The lemma is correct as stated: *if* `A_n -> A` and `B_n -> B` strongly with `sup||A_n||,
sup||B_n|| < infinity`, *then* `A_n B_n -> AB` strongly. Strong convergence is not preserved under
products in general; **uniform boundedness is exactly what rescues it.** So the question is whether
the sealed factors are uniformly bounded.

### 1.1 The C-factors: **VERIFIED, both schemes**

```text
C_pure = 1_(-inf,0)(Q h_0 Q)   C_pure_projector_residual = 2.220446049250313e-16  <- MACHINE ZERO.
                               IT IS A PROJECTOR. ||C_pure|| = 1.                          [OK]
C_mix  = Q P_- Q               C_mix_hermiticity  = 2.77555756156794e-17  (Hermitian)
                               C_mix_spectrum     = [0.03905128961944969, 0.9609487103805515]
                               SPECTRUM STRICTLY INSIDE (0,1) => ||C_mix|| <= 0.961 < 1.     [OK]
Source: stage8_execution/work/T07_control4_v3_blind_commit_v001.json, verified at source.
```

**`sup_n ||C_n|| <= 1` HOLDS FOR BOTH PINNED SCHEMES.** This half of step 1 is clean.

### 1.2 The V-factor: **NO SEALED UNIFORM BOUND. THIS IS THE GAP.**

The sealed definition, `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:654`:

> `V_{mu lambda}(a) := u_mu^{(c)}(a_-)^dagger u_lambda^{(c)}(a_+)`

```text
*** V IS UNITARY AT REAL a. THE SEALED OBJECT IS NOT AT REAL a. ***
M-2 pins the CLOSED PAIR POLYDISC max(|a_{c,+}|,|a_{c,-}|) <= eps_*, with the ADJOINT-CONTINUED
BRA BRANCH and joint holomorphy (v002:401). On a COMPLEXIFIED polydisc the adjoint-continued
u(a_-)^dagger is an ANALYTIC CONTINUATION of a unitary, NOT a unitary. ||V(a)|| > 1 is permitted
and generically expected off the real slice.
WHAT THE PRODUCT STEP NEEDS:  sup_n sup_{|a| <= eps_*} ||V_n(a)|| < infinity.
WHAT SEALED TEXT SUPPLIES:    for each FIXED n, boundedness by analyticity on a compact polydisc.
WHAT IS MISSING:              UNIFORMITY IN THE CARRIER INDEX n.
BOUNDED NEGATIVE: searched "sup.*||V", "||V_...||", "||u_...||", "uniformly bounded ... polydisc",
"bounded on the polydisc" across *.md. Every hit is in the COMPLETE_QSPEC line — a DIFFERENT
construction — or is a numerical isometry check. NO SEALED UNIFORM-IN-n BOUND ON V OVER THE
POLYDISC WAS FOUND.
```

**AND THE OBVIOUS RESCUE DOES NOT WORK, WHICH IS WHY THIS IS WORTH NAMING RATHER THAN WAVING
THROUGH.** One might argue the bound comes free from R-L2b's own hypothesis, since the refutation is
a reductio: assume `sup_n ||X_n||_2 <= M`. But that hypothesis bounds the **sandwiched** object
`C_n (V_n - V_n(0)) C_n`, **not `V_n` itself** — the compressions could annihilate exactly the
directions in which `V_n` grows. **The hypothesis does not deliver the factor bound the product rule
requires.**

```text
STEP 1 VERDICT: HALF-VERIFIED. The chain needs ONE LEMMA:
  H-VU  (uniform continued-unitary bound) — sup_n sup_{|a| <= eps_*} ||V_n(a)|| < infinity,
        for the adjoint-continued pair on the sealed M-2 polydisc, uniform in the carrier index.
NAMED IN R-L5 FORM AND DISCLOSED. NOT ASSUMED, NOT VALUED, AND NOT USED TO CLOSE ANYTHING HERE.
IT IS PLAUSIBLE — finite-dimensional, jointly holomorphic, compact polydisc — AND IT IS EXACTLY
THE KIND OF UNIFORMITY THIS PROGRAM HAS REPEATEDLY FOUND ASSERTED AND UNPROVED.
```

---

## §2 — STEP 2. THE SETTING. **VERIFIED, WITH THREE CORRECTIONS TO THE TRANSLATION.**

The principal flagged this as the likeliest failure point and as his own. **Three items are wrong;
one matters.**

### 2.1 **MATERIAL: "C_n, C are orthogonal projections" is FALSE for one of the two pinned schemes**

M-3 pins **TWO** finite schemes, `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V001.md:170-172`, verbatim:

> "**M-3** (the two Phase-A pinned finite schemes `C_mix = Q P_- Q`, `C_pure = 1_(-inf,0)(Q h_0 Q)`;
> **per-state, reported separately, never promoted**)"

```text
C_pure IS a projection. The referral's premise holds, and referral 2's proof — squeeze on spectral
  measures, then "polarization + C_n^2 = C_n = C_n^* upgrades to SOT" — APPLIES DIRECTLY.
C_mix IS NOT. It is a NON-IDEMPOTENT HERMITIAN CONTRACTION, 0 < C_mix < I, measured. The
  idempotence step C_n^2 = C_n IS FALSE FOR IT, SO REFERRAL 2's ROUTE DOES NOT COVER IT.
*** THE CONCLUSION SURVIVES FOR BOTH — BY DIFFERENT ARGUMENTS. *** For C_mix the result is EASIER
and needs nothing from referral 2: Q_n -> I strongly (requirement-list item (2), STANDARD, Hermite
basis complete), ||Q_n|| <= 1, and P_- fixed and bounded give Q_n P_- Q_n -> P_- strongly by the
SAME product lemma of step 1. The referral did not supply this and did not need to — but the
assembly as relayed covers only one of the two schemes M-3 pins.
```

### 2.2 Immaterial: the localizer is two compressions, not one product

The translation gives `M_c(t) = multiplication by b_D(t,x)*1_{|x| <= r(t)}`. The sealed
constructions are **separate**: `M -> Q 1_ball Q` and `B -> Q b_D Q`, and D6' fixes
`M(t) = Q 1_{|x| <= r(t)} Q` with `b_D` entering elsewhere (via `J = -B_D (x) alpha_x`).
**IMMATERIAL:** requirement-list item (4)'s proof needs only `||Q_n|| <= 1` and boundedness, which
covers each factor and their product alike.

### 2.3 Immaterial: h_0 checks out

Sealed as `h_0 = sum_j p_j (x) alpha_j` on the Hermite carrier — **massless Dirac in form, no mass
term.** So `sigma(h_0) = R` with **no gap**, and referral 2's pollution argument (the Dirac
pollution disease is a mass-gap phenomenon, absent by construction) **transfers correctly**. The
"0 is not an eigenvalue" step is standard for the free massless Dirac operator and is corroborated
independently at §4.

---

## §3 — STEP 3. **VERIFIED AT SOURCE.**

```text
C1 OFF-DIAGONAL MODULUS, verified at STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V001.md:99 and :594:
    "off-diagonal modulus EXACTLY 1/(2 pi^2 |r|^3); homogeneous degree -3"
    "||C_off(r)||_op  = 1/(2 pi^2 |r|^3)          [the C1 'modulus']"
A HOMOGENEOUS DEGREE -3 KERNEL ON R^3 IS NOT HILBERT-SCHMIDT: int int |K|^2 with |K| ~ |x-y|^{-3}
diverges at the diagonal. ||X||_2 = infinity IS WELL-FOUNDED ON THE SEALED MODULUS.
CORROBORATED BY THE SPEC'S OWN READING, D7'(b): "the logarithmic residue of the degree-(-3) kernel
against the in-cell SHARP localizers, AT THE VOLUME DIAGONAL" — the divergence sits exactly where
the trilemma places it.
NOT INDEPENDENTLY RE-VERIFIED BY THIS LANE: the derived lemma P alpha_x P = -n_x P and its
1.145e-16 / 200-direction numerical check. TAKEN FROM THE TRILEMMA AS CITED, and flagged as the one
input of step 3 this return did not re-run.
```

---

## §4 — **THE CORPUS ALREADY HAD REFERRAL 2's RESULT.** FOUR DAYS EARLIER.

`STAGE8_T7_PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_RESULT_V001.md`, dated **2026-07-24**:

```text
VERDICT: PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_DERIVED
  "Since the only symbol discontinuity is the measure-zero point p=0, convergence on the dense
   finite Hermite span and the uniform contraction bound imply:  C_n^(pure) -> P_- strongly."
```

**THAT IS REFERRAL 2's CONCLUSION, BY REFERRAL 2's ARGUMENT — the measure-zero mass at the symbol's
discontinuity — DERIVED INDEPENDENTLY AND EARLIER.**

```text
CUSTODY: NO ADJACENT SEAL FILE, but HASH-PINNED and DISCLOSED — a79939adf1d7185f...370, pinned at
  STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md:30 as "Pure-vacuum
  convergence result, PINNED FOR PHASE B". Hash RECOMPUTED BY THIS LANE AND MATCHES. Same disclosed
  unsealed-but-pinned pattern already ruled acceptable for row-7 authorities.
CONSEQUENCE FOR THE PRINCIPAL'S FRAMING: the claim that "the corpus asserted X_n -> X across a step
  it never established" IS TOO STRONG. The corpus DID establish C_n^(pure) -> P_- on 2026-07-24. What
  it never did was WIRE that result into H1's chain. *** A WIRING GAP, NOT A MISSING RESULT. ***
  H1 is better supported than the corpus had it — and better supported than the referral knew.
TWO CAVEATS FROM THAT ARTIFACT'S OWN FACE, NEITHER FATAL, BOTH RECORDED:
  - pure_state_sequence_nested = false; embedded n=2 and n=4 projectors differ in operator norm by
    0.166124... NESTEDNESS WAS ASSUMED OF Q_n, NOT OF C_n, so this does not bite — but the
    translation's word "nested" must attach to Q_n only.
  - ITS OWN SCOPE CLAUSE: "Strong convergence of one-particle covariances does not by itself imply
    convergence of growing-dimensional quasifree determinants." H1's chain is OPERATOR-LEVEL and
    does not invoke determinant convergence, so the caveat does not reach it — BUT ANY LATER
    ARTIFACT THAT MOVES FROM THIS TO A DETERMINANT STATEMENT IS CAUGHT BY IT.
```

---

## §5 — WHAT IS AND IS NOT NOW DECIDED

```text
NOT SEALED, AND DELIBERATELY: the refutation of R-L2b's uniformity. Step 1's V-factor is one named
  lemma (H-VU) short, and this program's standard is that a named missing input is not a discharge.
  Per the charter: IF ANY STEP FAILS, REPORT AND SEAL NOTHING. THAT INSTRUCTION IS FOLLOWED.
WHAT IS ESTABLISHED AND IS NEW: referral 1 closes requirement items (3),(4),(5); referral 2 closes
  C_n -> C for the PROJECTION scheme and is independently corroborated by a pinned 2026-07-24
  derivation; C_mix -> C follows by a shorter argument neither referral gave; sup_n ||C_n|| <= 1
  holds for BOTH pinned schemes; ||X||_2 = infinity is well-founded on the sealed C1 modulus.
WHAT REMAINS, PRECISELY ONE THING: H-VU. If H-VU is discharged, the chain runs and R-L2b's
  uniformity is refuted, on both pinned schemes.
CONSEQUENCES NOT ACTED ON, AS INSTRUCTED — R-L2b carried FOUR discharges (itself; T11's response
  half; the D3 refinement-natural weight's response side; connected extensivity). THIS ARTIFACT
  CHANGES THE STATUS OF NONE OF THEM, because the refutation is not sealed. The four remain as they
  were, now with a named single-lemma dependency rather than an open convergence question.
NOT RULED ON, AND HIS: O-1 / F'-5, which the trilemma reads as "keeping F'-5 selects the branch on
  which R-L2b is refuted". O-1 was HELD pending exactly the referral that has now returned. *** THE
  REFERRAL HAS RETURNED AND ITS HALF IS DONE; THE F'-5 RULING IS THE PRINCIPAL'S AND IS NOT TAKEN
  HERE. *** Also his: the fourth-horn question — whether a finite Hilbert-Schmidt bound was ever the
  right obligation.
```

## §6 — FLAGS

```text
step1_product_C_factors_verified        = true      # both pinned schemes, sup||C_n|| <= 1
step1_product_V_factor_verified         = false     # NO SEALED UNIFORM-IN-n BOUND ON THE POLYDISC
step2_setting_verified                  = true      # with three corrections (§2)
step2_correction_material               = 1         # C_mix is not a projection; M-3 pins BOTH
step3_HS_divergence_verified            = true      # C1 modulus at source; degree -3 on R^3
H_VU_named                              = true      # the one remaining lemma
H_VU_discharged                         = false
RL2b_uniformity_refuted                 = false     # NOT SEALED — one lemma short
refutation_sealed                       = false
referral2_independently_corroborated    = true      # pinned 2026-07-24 derivation, hash matches
corpus_gap_was_wiring_not_missing       = true
O1_F5_ruled                             = false     # THE PRINCIPAL'S
program_declared_blocked_or_dead        = false
alpha_computed = false ; proof_authorized = false ;
coupling_evaluation_authorized = false ; kappa_record_computed = false
```

## §7 — INVENTION CHECK

```text
NO REFUTATION SEALED. NOTHING ADOPTED. H-VU IS NAMED AND DISCLOSED, NOT VALUED AND NOT USED.
The C_mix strong-convergence argument in §2.1 is stated as a SHORTER ROUTE THAT FOLLOWS FROM
  ALREADY-STANDARD INPUTS (item (2) plus the step-1 lemma), not as a new theorem, and it is not
  used to close anything — the chain still fails at the V-factor regardless of scheme.
NOT RE-VERIFIED BY THIS LANE AND SAID SO: the P alpha_x P = -n_x P lemma and its 200-direction
  numerical check (§3); the two blind referral protocols themselves, which live in the supervision
  repo and were not read.
THE PRINCIPAL'S FRAMING WAS CORRECTED IN ONE PLACE (§4) — "a step it never established" is too
  strong; the result existed and was never wired in.
BOUNDED NEGATIVES: the V-bound search is scoped to the five named patterns over *.md and is stated
  as such; the COMPLETE_QSPEC hits are excluded BY OBJECT, not by convenience.
SEALS/PINS RECOMPUTED: a79939ad... matches its pin. Measurements read at source from
  T07_control4_v3_blind_commit_v001.json.
kappa NAMING OBSERVED: kappa_record in full, never bare.
```
