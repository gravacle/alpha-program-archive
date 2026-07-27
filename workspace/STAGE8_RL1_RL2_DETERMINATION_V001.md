# R-L1 and R-L2 — Determination V001

Date: 2026-07-27

## Status — the answer

```text
**BOTH ARE BLOCKED. NEITHER IS DISCHARGEABLE FROM SEALED TEXT. THE BLOCKERS ARE NAMED AS OBJECTS.**
**THEY ARE NOT INDEPENDENT** — they share one precondition, and R-L2 additionally depends on R-L2b,
which is a DEPENDENCY INSIDE a block headed "must close first".

*** R-L1's BLOCKER IS A DEFECT IN THE SEALED SPEC, FOUND ON THE CORPUS'S OWN MEASUREMENT: the
identity is asserted "Per admitted state (M-3)", M-3 admits TWO pinned schemes, and it is
structural for only ONE of them. ***

AND THE HAZARD CONVERGENCE IS STRONGER THAN PRE-REGISTERED: the EM forward constraint does not
arrive early — IT ALREADY BINDS STAGE 8, sealed.
NOTHING WAS CONSTRUCTED. No Carleman constant, no enclosure, no reduction lemma.
PRODUCTION PROHIBITED. alpha_computed = false. proof_authorized = false.
```

## 1. BOTH OBLIGATIONS, AS v002 CARRIES THEM

```text
§O.R — Architecture obligations (common; MUST CLOSE FIRST), v002:1010-1017, VERBATIM:
  R-L1   Block-triangular reduction on the sealed forms, adjoint-continued pair
         (M-2).  SCAD_BLOCK_TRIANGULAR_REDUCTION_UNCERTIFIED
  R-L2   Certified Carleman machinery: det(1+A) = det_2(1+A) e^{tr A};
         |det_2(1+A)| <= exp(||A||_2^2/2); the differentiated identity
         d/ds Log det_2(1+A_s) = tr[((1+A_s)^{-1} - 1) Delta]; the
         trace-of-product estimate. Every constant explicit and outward-enclosed;
         NO textbook constant by citation alone.  SCAD_CARLEMAN_CONSTANTS_UNCERTIFIED

AND THE FUNCTIONAL RELATION THEY SERVE, v002:657-666, VERBATIM:
  Block-triangular identity (obligation R-L1):
      1 + C(V-1) = [[ C V C , C V (1-C) ] , [ 0 , I ]]
    => det(1 + C(V-1)) = det_{ran C}(C V C).
      A_{mu lambda}(a)     := C(V_{mu lambda}(a) - 1)C
      Delta_{mu lambda}(a) := A(a) - A(0) = C(V(a) - V(0))C
      A_{mu lambda,s}(a)   := A(0) + s Delta(a),  s in [0,1]
  Carleman: det(1+A) = det_2(1+A) e^{tr A}, Log det_2(1+A) = tr[Log(1+A) - A],
      Log rho(a) := Log[ det(1+A(a))/det(1+A(0)) ]
                  = tr[Delta] - int_0^1 tr[(1+A_s)^{-1} A_s Delta] ds
      — VALID ONLY ON THE SURVIVING SECTOR (R.2), where det(1+A(0)) != 0.

NEITHER HAS EVER BEEN ATTEMPTED. The two witness strings occur in exactly 3 .md files and 0 .py,
0 .json; "Carleman" occurs in exactly two files; "det_2" in two. EVERY occurrence is the obligation
being LISTED, never worked. Bounded negative over .md/.py/.json/.txt, vendored sympy excluded.
```

## 2. R-L1 — THE STRUCTURAL HALF IS A PROPERTY. THE BLOCKER IS ELSEWHERE.

```text
THE BLOCK FORM IS A CONSEQUENCE OF C BEING IDEMPOTENT, AND OF NOTHING ELSE.
CHECKED, AND THE CHECK IS THIS LANE'S, NOT CORPUS CONTENT: with C = C^2 = C^dagger, in
H = ran C (+) ker C, the (2,1) block is (1-C)C(V-1)C = 0 identically, and the four blocks match
v002:658 exactly. Verified in exact rational arithmetic over 50 trials at n=6, rank(C)=3, with V
GENERIC — non-unitary and non-normal — in a scratchpad fixture outside the canonical root.
*** SO THE "ADJOINT-CONTINUED PAIR (M-2)" CLAUSE IN R-L1's OWN TITLE DOES NOT BEAR ON THE ALGEBRA
AT ALL. *** It assumes nothing about V: not unitarity, not invertibility. An executor reading R-L1
as an algebra obligation would discharge the algebra and inherit an uncertified premise upstream.
```

### 2a. THE BLOCKER — M-3 ADMITS TWO SCHEMES AND THE IDENTITY HOLDS FOR ONE

```text
R.0 QUANTIFIES THE IDENTITY OVER M-3, v002:652, VERBATIM:
  "Per admitted state (M-3), per admitted cell `C` of D3, per record-color pair `(mu, lambda)`,
   per CTP pair on the closed pair polydisc (M-2)"
AND M-3 ADMITS TWO, v002:402, VERBATIM:
  "**M-3** (the two pinned finite schemes `C_mix`, `C_pure`; per-state, reported separately,
   never promoted)"

*** AND THE CORPUS MEASURED THEM. VERIFIED AT SOURCE BY THIS LANE,
stage8_execution/work/T07_control4_v3_blind_commit_v001.json: ***
    C_pure_rank                = 16
    C_pure_projector_residual  = 2.220446049250313e-16     <- MACHINE ZERO. IT IS A PROJECTOR.
    C_mix_hermiticity          = 2.77555756156794e-17      <- Hermitian
    C_mix_spectrum_min         = 0.03905128961944969
    C_mix_spectrum_max         = 0.9609487103805515        <- SPECTRUM STRICTLY INSIDE (0,1)
    C_mix_trace                = 16.000000000000014
NO EIGENVALUE AT 0 OR 1 ⇒ C_mix IS NOT IDEMPOTENT. The corpus's own word for these objects is
"Hermitian contractions", typed 0 <= C <= I.
AND WORSE FOR THE REDUCTION: with no zero eigenvalue, ker C_mix = {0}, so ran C_mix is the whole
space AND THERE IS NO COMPLEMENT TO TRIANGULARIZE AGAINST AT ALL. The decomposition the display
presumes does not exist for that scheme.

=> THE SEALED IDENTITY IS ASSERTED ACROSS BOTH ADMITTED SCHEMES AND IS STRUCTURAL FOR ONLY ONE.
THAT IS THE BLOCKER, AND IT IS A DEFECT IN THE SPEC, NOT MERELY AN UNDONE OBLIGATION.
MISSING OBJECT: a reduction lemma valid for a NON-IDEMPOTENT Hermitian contraction 0 <= C <= I —
or a certificate that C_mix is idempotent, which the corpus's own measurement contradicts.
NEITHER IS SUPPLIED. NEITHER IS CONSTRUCTED HERE. And note a gap in the register itself: NO WITNESS
NAME EXISTS for this failure mode.
```

### 2b. R-L1 AND R-L4a ARE THE SAME QUESTION AT TWO POINTS — and R-L4a is answered NEGATIVE

```text
R-L1's RIGHT-HAND SIDE, EVALUATED AT THE SEALED OPPOSITE-PHASE BASELINE V(0) = 1 - 2P, IS
    det_{ran C}(C(1-2P)C) = det_{ran C}(1 - 2CPC)
WHICH IS VERBATIM R-L4a's OBJECT D. So R-L4a is the a = 0, opposite-phase INSTANCE of R-L1's
existence precondition — and the corpus has already answered it: D "DOES NOT EXIST AS A FREDHOLM
DETERMINANT", and 1 + A(0) = 1 - 2CPC "is not a trace-class perturbation of the identity".
AND THE DISPLAY IS UNSCOPED: the "VALID ONLY ON THE SURVIVING SECTOR" clause at v002:666 attaches
to Log rho, NOT to the block-triangular display two lines above it. SO R-L1 AS WRITTEN IS
QUANTIFIED OVER A SECTOR WHERE ITS OWN RIGHT-HAND SIDE HAS NO UNREGULARIZED MEANING.
```

## 3. R-L2 — BLOCKED, AND MORE SIMPLY. And it depends on R-L2b.

```text
(i) NO CONSTANT IS SUPPLIED, ANYWHERE. All four required statements exist ONLY as obligation text
    (v001:561-566; v002:663, :1013-1017) plus one uncertified assembly use (v002:814). No proof, no
    derivation, no constant, no outward enclosure. A sweep of all 36 "outward.enclos" occurrences
    found NONE attaching to any R-L2 item. §N (Frozen Numerics) names pi, e, exp, log and zeta —
    AND NO CARLEMAN CONSTANT. R-L2's own text forbids "textbook constant by citation alone", so the
    absence cannot be repaired by citation.
    MISSING OBJECT: the §N outward enclosures for the det_2 estimate, the differentiated identity,
    and the trace-of-product estimate.

(ii) *** R-L2 DEPENDS ON R-L2b, AND BOTH SIT IN THE "MUST CLOSE FIRST" BLOCK. ***
    R-L2's second required item is |det_2(1+A)| <= exp(||A||_2^2/2). The corpus's own assembly,
    v002:811-813 VERBATIM, bounds that norm as
        ||A_s||_2 <= ||A(0)||_2 + ||Delta||_2 <= |C|_4^{beta} G_cm + |C|_4^{alpha} G_hs
    and alpha is SCAD_HS_SCALING_EXPONENT_UNDERIVED — "a symbol, not 1/2" — with beta "derived with
    alpha under R-L2b". Sealed elsewhere: subtracted_response_scaling_in_|C|_4 =
    NOT_DERIVED_IN_EITHER_DIRECTION; p_of_the_actual_object = UNKNOWN.
    R-L2 CANNOT BE CERTIFIED PAST THE POINT WHERE ITS OWN DISPLAYED BOUND IS A FUNCTION OF A
    QUANTITY THE PROGRAM HAS NOT BOUNDED. This is an ordering defect inside §O.R, and it is not
    recorded there.

(iii) ARE THEY INDEPENDENT? NO. R-L1 and R-L2 share one precondition — a named trace-ideal class
    for A on the closed pair polydisc. Beyond that their content differs.
```

## 4. WHAT DISCHARGING THEM BUYS — ONE FACTOR, NOT THE EXTRACTION STEP

```text
Log rho IS PER-COLOUR-PAIR ONLY. v002:668-671 corrects exactly this: the per-pair display is NOT
valid for the colour-summed object, "the log of a sum is not a sum of logs".
AND A PRECISION CORRECTION TO MY OWN ERRATUM (da4cf7e6): I wrote that v002:838 "sums it into
Z_hat_comp^{(C)}(a)", with "it" being Log rho. VERIFIED: :838 sums c_{mu lambda} rho_{mu lambda}(a)
— RHO, NOT LOG RHO. Log rho enters at :842 only as the bounded quantity. Corrected here.
SO R-L3 (colour-sum handling on the surviving sector, SCAD_COLOR_SUM_LOG_MISUSE) is required
between R-L1/R-L2 and any statement about the summed object.

RESIDUE BETWEEN A DISCHARGED R-L1/R-L2 AND A COMPUTED kappa_record: **40 NAMED LINES (53 EXPANDED)**,
including at minimum R-L0, R-L0b, R-L2b, R-L3, R-L4a, R-L4b, R-L4, R-L5; the five conditions of BID
Theorem 3, of which ZERO are established; T7(ii) BLOCKED; T7(iii) BLOCKED; T7(iv) NOT_EXECUTABLE;
A-L0 arm 2 with U1/U2/U3 and the undeclared projection-tail conditional; the parent's unselected
preparation; the source-scalarization no-go and omega_in; the nine-step EM dependency order with
zero items closed; and the arithmetic firewall on kappa_record.
AND THE SURVIVING-SECTOR RESTRICTION LIMITS EVEN THAT: Log rho is valid only where
det(1+A(0)) != 0, and R-L4b — that the opposite-phase sector vanishes identically — is UNCERTIFIED.
```

## 5. THE HAZARD CONVERGENCE — STRONGER THAN PRE-REGISTERED. IT ALREADY BINDS.

```text
R-L2's BLOCKER SITS ON THE CELL-SCALE (REFINEMENT) AXIS: the scaling of ||Delta||_2 in |C|_4.
NOT the coincidence axis (r -> 0) and NOT the separation axis (large R). This program has confused
those three repeatedly; they are kept apart here.

AND THE EM FORWARD CONSTRAINT DOES NOT MERELY PRE-REGISTER THIS HAZARD — IT ALREADY BINDS STAGE 8.
Sealed, battery spec :152-161, and it is stronger than the step-list's lane judgement that
"solving it once may serve both": the packing fence text was "DELIBERATELY EXTENDED to bind this
battery", and "T7/T13's cellulation-independent limit IS the required packing-independence
demonstration."
=> SO THE CORRECT STATEMENT IS NOT "THE DOWNSTREAM HAZARD ARRIVES EARLY". IT IS THAT THE SAME
FENCE IS ALREADY IN FORCE HERE, BY A SEALED EXTENSION, AND R-L2b IS THE OBLIGATION THAT MUST
SATISFY IT. Failing it does not merely block Stage 8 and threaten EM step 4 — it fails a fence that
is already binding on both.
```

## 6. WHAT THE SPEC PREDICTED, AND WHAT IS ACTUALLY THE CASE

```text
v002:1935-1937, PA-1, VERBATIM: "R-L1, R-L2, R-L3 discharge at the structural level. Confidence:
high. Ground: the block-triangular reduction and the Carleman identities are structural."
THAT IS A PREDICTION, NOT A DISCHARGE. On this determination it is RIGHT about the block form's
structural character and WRONG about its sufficiency: the structural half IS a property, and R-L1
is blocked anyway — by scheme admissibility (§2a) and by its own right-hand side's existence (§2b).
Recorded under Rule 6 as a frozen prediction now bearing against the spec's authoring lane.
```

## 7. INVENTION CHECK

```text
NOTHING CONSTRUCTED. No Carleman constant, no value, no interval, no outward enclosure, no Schatten
or trace-norm bound, no exponent, no reduction lemma for the non-idempotent case, and no
"this would follow from" sketch toward any of them.
THE ONE DERIVATION PERFORMED IS A CHECK ON A DISPLAYED IDENTITY — the block decomposition of
1 + C(V-1) — declared throughout as this lane's verification and never as corpus content, in exact
rational arithmetic, in a scratchpad fixture outside the canonical root. Its result is used to ADD
an obligation, not to discharge one.
GENERAL MATHEMATICS NOT USED AS EVIDENCE: Carleman's inequality, Fredholm theory and Seiler-Simon
bounds are true and are not evidence about what this corpus supplies. R-L2's own text forbids
exactly that route ("NO textbook constant by citation alone").
```

## Protected status

```text
R_L1 = BLOCKED_BLOCKER_NAMED ; R_L2 = BLOCKED_BLOCKER_NAMED
independent = false (shared precondition: a named trace-ideal class for A on the polydisc)
R_L1_structural_half = A PROPERTY of C's idempotence, verified by this lane, generic V
R_L1_blocker = M-3 ADMITS TWO SCHEMES; C_mix IS NOT IDEMPOTENT (sealed measurement)
  C_mix_spectrum = [0.03905128961944969, 0.9609487103805515]; C_pure_projector_residual = 2.22e-16
  ker C_mix = {0} => no complement to triangularize against
  missing_object = a reduction lemma for a non-idempotent Hermitian contraction 0 <= C <= I
  witness_name_for_this_failure_mode = DOES NOT EXIST (gap in the witness register)
R_L1_equals_R_L4a_at_a_eq_0 = true; R-L4a already answered NEGATIVE (no Fredholm determinant)
R_L1_display_is_unscoped = true (the surviving-sector clause attaches to Log rho, not to the display)
R_L2_blocker_1 = NO certified outward enclosure for any Carleman constant anywhere; §N names none
R_L2_blocker_2 = R-L2 DEPENDS ON R-L2b (||A_s||_2 <= |C|_4^beta G_cm + |C|_4^alpha G_hs, alpha
  underived) — A DEPENDENCY INSIDE THE "MUST CLOSE FIRST" BLOCK, NOT RECORDED THERE
what_discharging_buys = ONE FACTOR, per-colour-pair only; R-L3 required before the summed object
residue_to_a_computed_kappa_record = 40 named lines (53 expanded)
own_correction = v002:838 sums RHO, not Log rho; corrects erratum da4cf7e6
hazard_class = SAME FENCE, AND IT ALREADY BINDS STAGE 8 by sealed extension (battery spec :152-161)
  axis = CELL-SCALE (refinement), not coincidence, not separation
PA_1_prediction = right on structural character, wrong on sufficiency (Rule 6, frozen)
constructed_anything = NONE
production_authorized = false
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
