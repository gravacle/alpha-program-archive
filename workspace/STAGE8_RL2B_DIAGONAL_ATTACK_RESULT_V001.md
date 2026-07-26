# R-L2b Diagonal Attack — RESULT: the Framing is Refuted, and the Missing Ingredient is Named V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY. Deliverable for DIAGONAL_SECOND_ORDER_COINCIDENCE_CANCELLATION_
THEOREM_FOR_C(V(a)-V(0))C.
*** OUTCOME: A REFUTATION OF THE FRAMING, PLUS ONE DERIVED IDENTITY, PLUS
THE MINIMAL MISSING INGREDIENT. THE p > 3/2 QUESTION IS NOT A QUESTION ABOUT
THE SEALED OBJECT. The sealed object is FINITE-RANK and has NO COINCIDENCE
SINGULARITY AT ALL. ***
CONTAINS A MAJOR SELF-CORRECTION: this lane's divergence computation, and
several artifacts built on it today, applied a CONTINUUM computation to a
GALERKIN object. Seventh instance of the day's error class.
kappa_record/kappa_Thomson rule observed. PRODUCTION PROHIBITED.
alpha_computed = false. proof_authorized = false.
```

## §1 — THE SEALED OBJECT IS FINITE-RANK. THERE IS NO DIAGONAL SINGULARITY.

```text
SEALED, Phase-A A1/A2 (789338ad...), every operator carrying the SAME
Galerkin projector:
    M_(n,ell)(t)   = Q_(n,ell) 1_(|x|<=r(t)) Q_(n,ell)
    B_(D,n,ell)(t) = Q_(n,ell) b_D(t,x) Q_(n,ell)
    J_(n,ell)(t)   = -B_(D,n,ell)(t) tensor alpha_x
    h_(lambda,n,ell)(t;a) = h_(0,n,ell) + lambda v(t) M_(n,ell)(t) tensor S_n
                            + a J_(n,ell)(t)
    -- note even the FREE term is h_(0,n,ell), Galerkin-projected.
SEALED, Hermite-Galerkin baseline spec (80aa4e17...), line 7 verbatim:
    "Construct the first genuine FINITE-RANK RESTRICTIONS of the continuum"
  with the carrier the span of finitely many Hermite products
    span{phi_a(x/ell) phi_b(y/ell) phi_c(z/ell) : ...}, spinor dimension 32.
*** Q_(n,ell) IS A FINITE-RANK PROJECTOR. ***

THE CONSEQUENCE, IN THREE LINES:
  1. J_(n,ell) = Q(...)Q is FINITE-RANK.
  2. Every term of the Dyson series for V(a) - V(0) contains AT LEAST ONE
     J (that is what makes it the DIFFERENCE), so V(a) - V(0) IS
     FINITE-RANK -- at every order in a, not merely the first.
  3. rank(C X C) <= rank(X), so X = C(V(a)-V(0))C IS FINITE-RANK, hence
     trace-class, hence HILBERT-SCHMIDT, WITH A FINITE-SUM-OF-PRODUCTS
     KERNEL AND NO SINGULARITY ANYWHERE.
*** THEREFORE p IS NOT A PROPERTY OF THE SEALED OBJECT. AT FINITE (n,ell)
THE OBJECT IS SMOOTH AND ||X||_2 < infinity TRIVIALLY. THE DIAGONAL
COINCIDENCE-CANCELLATION THEOREM HAS NOTHING TO ACT ON. ***
```

## §2 — SELF-CORRECTION: A CONTINUUM COMPUTATION APPLIED TO A GALERKIN OBJECT

```text
THIS LANE COMPUTED, and several of today's artifacts rest on it:
    || 1_D C 1_D ||_2^2 = int int |C|^2 ~ int d^3r r^-6, divergent as eps^-3,
    "so R-L2b's finiteness is purchased entirely by CANCELLATION, not by
     support volume."
THAT COMPUTATION USED THE CONTINUUM SEA KERNEL
C(r) = (1/2)delta^3(r) - i alpha.r/(2 pi^2 |r|^4) ACTING ON CONTINUUM
FUNCTIONS. THE SEALED OBJECT IS A FINITE-RANK GALERKIN OBJECT. The
computation is correct about the continuum and IS NOT ABOUT THE SEALED
OBJECT.
PROPAGATION, stated so the record is repairable: the following inherited the
error and are affected as claims about the SEALED object, while remaining
correct as claims about the CONTINUUM limit --
  the "finiteness is cancellation-purchased" statement;
  the alpha = 1 <=> bounded-difference-kernel equivalence;
  the p > 3/2 threshold and the A^(3(1-alpha)) aggregate growth;
  the framing of the three blind questions that followed from it.
NONE OF THEM IS WITHDRAWN AS CONTINUUM MATHEMATICS. ALL OF THEM ARE
RE-TYPED: they describe the n -> infinity LIMIT, not the object at finite n.
SEVENTH INSTANCE TODAY of match-by-name / fail-by-type, and the largest in
propagation. The class is now: universal-vs-represented; operator-vs-scalar;
object-vs-bound; formula-vs-response-naturality; insertion-grading-vs-
coincidence-grading; dilution-vs-cancellation (caught before adoption); and
CONTINUUM-vs-GALERKIN (this one, caught after propagation).
```

## §3 — WHAT IS ACTUALLY DERIVED: THE LEADING SYMBOL SURVIVES

The continuum analysis is not wasted; it is the limit analysis. Here is the
one new derived result, and it is exact.

```text
LEMMA (derived here; verified numerically to 1.1e-16 over 200 random
directions in the Dirac representation, Clifford relations checked first).
  Let P = (1 - alpha.nhat)/2 be the negative-energy projector for direction
  nhat. Then for every spatial index x:
        *** P alpha_x P  =  - nhat_x P . ***
PROOF: {alpha_i, alpha_j} = 2 delta_ij gives alpha_x(alpha.nhat) =
  2 nhat_x - (alpha.nhat) alpha_x, and (alpha.nhat)^2 = 1. Expanding
  4 P alpha_x P = alpha_x - alpha_x(alpha.nhat) - (alpha.nhat)alpha_x
  + (alpha.nhat)alpha_x(alpha.nhat) and substituting twice gives
  -2 nhat_x + 2 nhat_x (alpha.nhat) = -4 nhat_x P.  QED.

WHAT IT SAYS, AND IT IS THE ANSWER TO THE COINCIDENCE QUESTION IN THE LIMIT:
  The sea projector's symbol C(p) = (1 - alpha.phat)/2 is homogeneous of
  DEGREE 0. Sandwiching the insertion's Dirac structure gives
        C(p) alpha_x C(p)  =  - phat_x C(p) ,
  i.e. THE SANDWICH REDUCES THE MATRIX INSERTION TO A SCALAR TIMES THE
  PROJECTOR, and the result is STILL DEGREE 0 in p -- hence a DEGREE -3
  kernel in r, hence NO VANISHING AT COINCIDENCE.
*** THE LEADING TERM IS NOT CANCELLED BY THE SANDWICH. IT SURVIVES, WITH AN
EXPLICIT COEFFICIENT -phat_x. So in the CONTINUUM LIMIT the object is NOT
Hilbert-Schmidt, and this is now DERIVED rather than merely unproven. ***
```

## §4 — THE SHARP CONSEQUENCE, AND IT IS A CONDITIONAL REFUTATION

```text
HS BALLS ARE WEAKLY CLOSED. If X_n -> X in the strong sense with
||X_n||_2 <= M uniformly, then X is Hilbert-Schmidt with ||X||_2 <= M.
CONTRAPOSITIVE: IF THE LIMIT X IS NOT HILBERT-SCHMIDT, THEN ||X_n||_2 ->
infinity. NO UNIFORM BOUND CAN EXIST.
COMBINING WITH §3: the continuum limit's leading symbol survives (derived),
so the continuum X is not HS, so
    *** ||X_(n,ell)||_2 -> infinity AS THE GALERKIN CARRIER EXHAUSTS THE
    CONTINUUM, AND R-L2b'S UNIFORM BOUND CANNOT HOLD. ***
CONDITIONAL ON EXACTLY ONE HYPOTHESIS, NAMED AND NOT ASSUMED: that the
Galerkin scheme CONVERGES to the continuum object in the sense required for
the weak-closedness argument. The baseline spec calls itself "a convergence
diagnostic", which is suggestive but is NOT the convergence statement the
argument needs. THIS LANE HAS NOT ESTABLISHED IT.
SO THE RESULT IS: R-L2b's uniform bound FAILS IF the Galerkin exhaustion
converges to the continuum object; and HOLDS TRIVIALLY, at every finite
(n,ell), if it does not.
```

## §5 — THE MINIMAL MISSING INGREDIENT

```text
NOT a cancellation, NOT a Ward identity, NOT a smoothing estimate. It is a
TYPING DECISION WITH AN ANALYTIC CONSEQUENCE:
  *** DOES R-L2b QUANTIFY OVER FINITE CARRIERS, OR OVER THE CONTINUUM
  LIMIT? ***
    FINITE CARRIER, uniform in the diamond but at FIXED (n,ell): R-L2b is
      TRUE and nearly trivial -- finite rank, smooth kernel, finite HS norm.
      But then kappa_record is a finite-carrier quantity and the continuum
      claim is not made.
    CONTINUUM LIMIT, uniform in (n,ell) as the carrier exhausts: §3 and §4
      say the bound FAILS, because the limiting symbol survives.
THE MINIMAL MISSING SEALED OBJECT IS THEREFORE THE ONE ALREADY NAMED THIS
MORNING, BEFORE ANY OF THIS:
    *** U3 -- THE PROJECTION-TAIL / GALERKIN-LIMIT OBLIGATION, and its
    verdict-language requirement to state which of UNIFORM-IN-Q or
    LIMIT-WITH-CERTIFIED-TAILS the route relies on. ***
It was bound into STAGE8_T7_ARM2_SHARPENING_AND_PROJECTION_TAIL_BINDING_V001
this morning, carried into the transport charter, and it is the item this
lane failed to propagate into the E1 v002 spec -- the defect recorded in the
three-defect erratum. THE DAY CLOSES ON THE ITEM IT OPENED ON.
```

## §6 — WHAT THIS DOES AND DOES NOT SETTLE

```text
SETTLED: the coincidence-cancellation theorem as posed does not exist,
  because its object does not have the singularity it would cancel. The
  seven closed mechanisms were all aimed at the continuum limit, correctly
  as limit analysis and incorrectly as analysis of the sealed object.
DERIVED AND NEW: P alpha_x P = -nhat_x P, exact, and with it the fact that
  the continuum leading term SURVIVES the sea sandwich. That converts "no
  identified mechanism supplies p > 3/2" into "the leading term is derivably
  nonzero in the limit" -- a stronger and more useful negative.
NOT SETTLED: whether the Galerkin exhaustion converges in the required
  sense. That single hypothesis decides between "R-L2b fails in the limit"
  and "R-L2b holds at finite carrier and the continuum claim was never
  available". THIS LANE DOES NOT DECIDE IT AND DOES NOT ADOPT EITHER.
NOT CLAIMED: no bound, no exponent, no closure of R-L2b. And the
  object-vs-bound line holds -- §4 is a statement about the SEQUENCE of HS
  norms under a named hypothesis, not an unconditional statement about the
  object.
FOR THE PRINCIPAL: the question "does R-L2b close" has become the question
  "at what carrier is kappa_record defined", which is a typing decision he
  holds and which U3 was written to force.
```

## Protected status

```text
sealed_object_is_finite_rank = true      (Q_(n,ell) finite-rank, SEALED)
coincidence_singularity_in_sealed_object = NONE
p_is_a_property_of_the_sealed_object = false
framing_refuted = true
self_correction = continuum computation applied to a Galerkin object
error_class_instance = 7th (largest in propagation)
affected_claims_retyped_not_withdrawn = true (correct as CONTINUUM claims)
derived_lemma = P alpha_x P = -nhat_x P   (exact; verified to 1.1e-16)
leading_symbol_survives_the_sandwich = true (DERIVED, not merely unproven)
continuum_object_is_HS = false
conditional_refutation = ||X_n||_2 -> infinity IF Galerkin converges
convergence_hypothesis_established = false      (named, NOT assumed)
minimal_missing_ingredient = U3 projection-tail / Galerkin-limit obligation
U3_was_named_this_morning = true; and not propagated into E1 v002 (recorded
                            defect)
R_L2b_closed = false
bound_claimed = false
exponent_derived = false
typing_decision_belongs_to = principal
production_authorized = false
alpha_computed = false
proof_authorized = false
```
