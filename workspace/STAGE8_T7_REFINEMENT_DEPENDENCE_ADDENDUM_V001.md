# Stage-8 T7 — Refinement-Dependence Addendum: the Principal's Question Answered V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY ADDENDUM to STAGE8_T7_SLIVER_NATURALITY_ATTEMPT_RESULT_V001.
Answers the principal's question: does the result indicate the completed
response is refinement-DEPENDENT BY CONSTRUCTION — that refining a cell
CREATES record content that did not exist before, because tau_R is
scale-invariant? And: "this proof route fails" vs "the invariance being
sought does not hold"?
THE ANSWER IS NEITHER OF THOSE TWO. There is a THIRD, LOGICALLY PRIOR
ANSWER, and it is the finding.
D3 NOT NARROWED. NO SHAPE CONDITION ADOPTED. PRODUCTION PROHIBITED.
```

## §1 — THE DIRECT ANSWER: refinement creates record content, and that content cannot reach the response

```text
YES, REFINEMENT CREATES RECORD CONTENT. Every admitted cell runs at FULL
tau_R = pi/sqrt(2), with no small-record-coupling hypothesis anywhere. Cut
one cell into N and there are N full record cycles where there was one.
That is a real change in the BASELINE.
NO, THAT DOES NOT MAKE THE RESPONSE REFINEMENT-DEPENDENT, and the reason
is structural and sealed:
    D1 line 116:  Z_hat_comp(a) := Z_comp(a) / Z_comp(0)
    Phase-A A1:   record tier enters as  +lambda v(t) M(t) tensor S   (no a)
    Phase-A A2:   history enters ONLY as +a J(t) tensor I_R
  => Z_hat_comp(0) = 1 IDENTICALLY on every admitted complex, hence
     Phi_gamma(0) = 0 for every cluster, every depth, EVERY CELL SHAPE;
     and any a-INDEPENDENT per-cell content multiplies numerator and
     denominator alike and is annihilated BEFORE any activity is formed.
THE PRECISE ERROR THIS CORRECTS — this lane's own P-S1, and two of five
lanes made it too: IT CONFLATES A BASELINE FACT WITH A RESPONSE FACT. The
record content per cell is a baseline quantity. The completed response is a
DIFFERENCE in a. Creating baseline content does not create response
content. tau_R's scale-invariance is a genuine, sealed obstruction — for
the ACTIVITY g(C,eps) under R-L0 ground (i), where no normalizing ratio
exists — and it does not cross into the normalized response.
SO: the tau_R mechanism the question names is REFUTED as a source of
refinement-dependence in the response.
```

## §2 — THE THIRD ANSWER, and it is prior to the dichotomy

```text
THE QUESTION ASSUMES THE RESPONSE ON A SLIVER CELL IS A DEFINED QUANTITY
WHOSE INVARIANCE ONE MAY THEN AFFIRM OR DENY. IT IS NOT.

VERIFIED AT SOURCE BY THIS LANE, with multiple spellings deliberately,
because a negative existential from a single grep pattern is exactly the
error that produced this lane's P-X4 miss:
    "shape parameter"    0 occurrences in the corpus
    "arbitrary cell"     0
    "general cell"       0
    "aspect ratio"       0
    "unit diamond"       0
    "reference diamond"  0
  and Phase-A A1/A2 (789338ad…, lines 86-88 and 111) fix the construction
  RIGIDLY AND ISOTROPICALLY:
      r(t) = min(t, 1-t);   v(t) = (pi/sqrt2) 32 r(t)^3;
      support: 0 < t < 1, |x| < min(t, 1-t);   b_D = exp(16 - 1/s)
  There is NO shape parameter and NO sealed rule transporting this unit
  isotropic diamond to a general admitted cell of D3. The two places the
  corpus speaks of "per-cell scale covariance" (E1 v001:447-451,
  v002:861-865) are items in R-L0's list of AVAILABLE INPUTS to an
  obligation that may fail, and they cite an UNSEALED phase-1 draft.

THEREFORE: "the completed response on a sliver cell" NAMES NO QUANTITY in
the sealed corpus. One cannot score a scaling law — or an invariance — for
an object that has not been written down.
  IT IS NOT "THIS PROOF ROUTE FAILS": no route was reached.
  IT IS NOT "THE INVARIANCE DOES NOT HOLD": nothing was shown to fail.
  IT IS: THE OBJECT WHOSE INVARIANCE IS SOUGHT IS NOT DEFINED OVER THE
  CLASS THE INVARIANCE IS QUANTIFIED OVER.
THAT IS THE FINDING, and it is logically prior to the principal's
dichotomy rather than a third position within it.
```

## §3 — WHAT THE DAY'S OBSTRUCTIONS ACTUALLY CONVERGED ON

The principal is right that they converge. They converge here, and it is
not the tau_R question:

```text
*** IS THE PER-CELL INSERTION DOMAIN |C|_4, OR IS IT tau_R x |C|_3 ? ***

  IF |C|_4        : the insertion scales with the cell's own 4-volume;
                    slivers contribute proportionally; volume-natural.
  IF tau_R x |C|_3: a sliver with small |C|_4 but O(1) 3-volume receives a
                    FULL tau_R insertion; refinement then genuinely
                    multiplies response content and the invariance FAILS.
THE SEALED CORPUS PULLS BOTH WAYS AND RESOLVES IT NOWHERE:
  - D2 ("every cell runs at FULL tau_R", no small-coupling hypothesis)
    reads naturally toward the second.
  - A-L4 (E1 v002 ~1086) states the strength scaling tracking CELL TIME
    EXTENT and reaches "total eps^2 L^4 / 2 = |C|_4 (eps^2/2)" — the first
    — but is immediately scoped: "Stated for the TWO-LINE SECTOR on family
    A, and NOT extended to n = 1, NOT extended to the one-line sector, NOT
    EXTENDED BEYOND FAMILY A."
  - The |C|_4 factor is DERIVED exactly ONCE in the corpus, in that
    family-A two-line statement, via the ISOTROPY identity
    (cell time extent) = L, which holds ON CUBES. Everywhere else |C|_4 is
    either D5's TARGET SHAPE or a definitional divisor
    (S1: G_tr := |C|_4^-1 |tr[...]|; the tautology x := |C|_4 g).
  - The one architecture that ever derived a per-unit-volume functional is
    the phase-1 K_sea functional, RETIRED by R.5; consuming it BLOCKS with
    witness PHASE1_KSEA_ARCHITECTURE_REANIMATED.
SO THE ANSWER TO "BETTER BOUND OR DIFFERENT FRAME" IS: NEITHER YET. What
is missing is not an estimate and not a frame — it is a DEFINITION, and
the definition is upstream of both. A better bound cannot be sought for an
undefined object, and a different frame cannot be chosen before knowing
which of the two readings the construction actually has.
```

## §4 — THE FINDING THAT BEARS ON THE HELD DECISION: shape is not the deciding axis

```text
RESTRICTING TO V011's SHAPE-REGULAR C_ref WOULD NOT RESCUE THE OBJECT.
Three grounds, the third decisive:
  1. No failure was established, so the antecedent of V011's
     restrict-or-block clause is not triggered.
  2. R-L2b and R-L0 are WORD-FOR-WORD THE SAME OBLIGATIONS on C_ref. The
     restriction removes no obligation.
  3. THE ONE RECORDED INSTANCE OF THE PATHOLOGY ARISES INSIDE C_ref. The
     deleted S3/G_bl case — the alpha = 0 failure the corpus actually has
     on record — arises under ISOTROPIC DILATION, which is inside the
     shape-regular class. THE SHAPE AXIS IS NOT THE DECIDING AXIS.
CONSEQUENCE, stated so it cannot be misread as advocacy: anyone reading
this as ammunition for narrowing D3 would be taking a decision that is not
theirs AND would not obtain the thing they took it for. This lane neither
narrows D3 nor recommends narrowing it. The C_ref/D3 conflict remains the
principal's, unresolved and unprejudiced.
```

## §5 — THE TWO MISSING OBJECTS, STRICTLY ORDERED

```text
(1) PRIOR / DEFINITIONAL — does not exist under any name; named here:
    E1_PER_CELL_CONSTRUCTION_TRANSPORT_RULE_ON_ANISOTROPIC_AND_NON_DIAMOND_D3_ATOMS
    A sealed rule carrying A1/A2 — local cell time t in [0,1];
    r(t) = min(t,1-t); M(t) = Q 1_{|x|<=r(t)} Q; v(t) = (pi/sqrt2) 32 r(t)^3;
    b_D = exp(16 - 1/s) — from the unit isotropic diamond to an ARBITRARY
    admitted cell of full D3, including anisotropic slivers and
    star-refined atoms of unbounded facet count. It must state how tau_R,
    v, M and b_D^(c) are defined there; what "the cell's causal diamond"
    means for an atom that is not an affine image of the reference
    diamond; whether ||b_D^(c)||_inf = 1 survives ANISOTROPIC rescaling;
    and DECISIVELY whether the record cycle's extent is tied to the cell's
    PHYSICAL TIME EXTENT or normalized in LOCAL cell time — which is §3's
    dichotomy.
(2) CONSEQUENT / ANALYTIC — already named in the corpus:
    SCAD_HS_SCALING_EXPONENT_UNDERIVED (R-L2b): alpha in
    ||C(V(a)-V(0))C||_2 <= |C|_4^alpha G_hs DERIVED, not assumed 1/2, with
    G_hs uniform over the FULL unrestricted D3 quantifier including
    unbounded aspect ratio; companion beta for G_cm. Downstream: the common
    wall B-L2*, in a form blind to ASPECT RATIO as well as to carrier —
    B-L2* as sealed contains NO anisotropy clause.
DISCHARGING (2) WITHOUT (1) WOULD BE DISCHARGING A BOUND ON AN UNDEFINED
OBJECT. The ordering is part of the finding.
```

## §6 — Recast Q6's status, in a third category rather than collapsed into a neighbour

```text
RECAST Q6 IS NEITHER ILL-POSED NOR WELL-POSED ON SEALED INPUTS.
Its "weighted" quantifier ranges over full D3. On that class the WEIGHT
side is settled exactly (measure additivity, shape-blind — P-S2 landed),
but the RESPONSE side is not merely unproved: over part of the quantifier
IT IS NOT YET DEFINED. So recast Q6 is currently quantified over a class
on which its own weight is HALF-CONSTRUCTED. That is weaker than
"ill-posed" and strictly stronger than "merely unproved", and it is
recorded in that third category.
AND A CAUTION AGAINST A TEMPTING INFERENCE: exact reaggregation and
volume-suppression are LOGICALLY INDEPENDENT — a Dirac mass reaggregates
exactly yet assigns full weight to a vanishing sliver. So P-S2's landing is
not even weak evidence for the response half, and the object may NOT be
sealed as validated on the strength of the weight half.
```

## Protected status

```text
refinement_creates_record_content = true            (baseline)
refinement_dependence_of_response_via_tau_R = REFUTED
baseline_vs_response_conflation_recorded = true
proof_route_failed = false
invariance_shown_not_to_hold = false
response_on_sliver_cells_defined_in_corpus = false  (THE FINDING)
insertion_domain_reading = UNRESOLVED_ON_SEALED_TEXT (|C|_4 vs tau_R x |C|_3)
volume_factor_derived_instances_in_corpus = 1        (family A, two-line
                                                     sector, via isotropy)
needs_better_bound = false
needs_different_frame = false
needs_a_DEFINITION_first = true
restricting_to_C_ref_would_rescue_object = false
shape_is_the_deciding_axis = false
alpha_zero_pathology_arises_inside_C_ref = true
recast_Q6_status = third_category_half_constructed_weight
weight_half_evidence_for_response_half = none
D3_narrowed = false
D3_object_spec_status = HELD_PENDING_PRINCIPAL
production_authorized = false
alpha_computed = false
proof_authorized = false
```
