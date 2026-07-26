# R-L2b Over the Chartered Transport, and BLIND Route-Finding to kappa_record V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY. Part B's predictions are FROZEN BEFORE Part C is written, and
Part C is answered BLIND — the independent lane's answer to the same
question has not been seen and was not coordinated with.
Cites: plan 12f204c64f0c0fd9...; amendment 001 c59cc8337913b81b...;
transport charter f58007a0f982343e...; options memo 97149d0859d4f441...
NOTHING ADOPTED. R-L2b NOT closed. D3 NOT narrowed. PRODUCTION PROHIBITED.
alpha_computed = false.
```

## PART A — R-L2b STATED OVER THE CHARTERED TRANSPORT

```text
R-L2b, RESTATED, and the charter changes the OBJECTS but not the DIFFICULTY:
  CERTIFY:  || C (V_(mu lambda)(a) - V_(mu lambda)(0)) C ||_2
              <=  |D|_4^alpha * G_hs
  WHERE     D ranges over the DIAMONDS of the chartered decomposition, not
            over atoms of D3;
            |D|_4 is the sealed tetrad/Jacobian 4-volume of that diamond;
            alpha is DERIVED, not assumed to be 1/2;
            G_hs is finite UNIFORMLY over every admissible decomposition of
            every atom of the unrestricted D3 class, and CARRIER-BLIND.
  COMPANION: beta for G_cm, derived with alpha.
WHAT THE CHARTER BUYS, precisely:
  1. THE OBJECT IS NOW WELL-DEFINED. Before the charter, "the response on a
     sliver" named no quantity — the Phase-A construction existed only on
     the unit isotropic diamond. R-L2b was a bound on an undefined object.
     It is now a bound on a diamond, and every diamond IS an affine
     dilate/translate of the sealed construction.
  2. THE ANISOTROPY IS RELOCATED, NOT REMOVED. Each diamond is ISOTROPIC, so
     ON A SINGLE DIAMOND the isotropic scale orbit applies and the
     one-parameter covariance is available. The anisotropy of the atom now
     lives in the COMBINATORICS of the decomposition — how many diamonds,
     of what sizes — not in the geometry of any single insertion.
  *** THAT IS THE SUBSTANTIVE CONSEQUENCE, AND IT CHANGES THE SHAPE OF THE
  ESTIMATE. R-L2b over the charter is no longer "an anisotropic Schatten-2
  estimate". It is (i) the ISOTROPIC per-diamond estimate, where the sealed
  scale orbit is available and the exponent may be derivable from
  covariance; plus (ii) a SUMMATION over the decomposition, where the
  aspect-ratio dependence now sits. ***
WHAT THE CHARTER DOES NOT BUY: no estimate. The independent lane's report
that the bound class fails in the sliver direction is NOT answered by the
charter; it is re-localised from (i) to (ii). If the failure is genuinely in
the per-diamond isotropic estimate, the charter does not help. If it is in
the aspect-ratio summation, the charter converts an anisotropic operator
problem into a counting problem over isotropic pieces — which is a
different and plausibly easier object, and which is also exactly where
O-D1 (diamonds do not tile) and O-D3 (decomposition-independence) bite.
```

## PART B — FROZEN PREDICTIONS on the route-finding question

```text
Calibration, as Rule 6 requires: this lane's route-survival predictions run
optimistic across two eras; the independent family stands at FIVE
consecutive landings; this lane asserted past its evidence three times
today. Weight accordingly.
P-K1 The highest-value route is a RE-POSING OF WHAT MUST BE PROVED, not a
     new lemma: kappa_record needs only the SECOND DERIVATIVE AT a = 0,
     while T7(iii) clauses (2) and (3) prove analyticity on a whole
     polydisc and convergence of a whole differentiated series. The
     re-posing bypasses strictly more than it costs. Confidence:
     MODERATE-HIGH.
P-K2 A physical criterion fixing the cell scale is ABSENT from the corpus
     AND COLLIDES with sealed text; supplying one is a NEW PRINCIPLE.
     Confidence: HIGH.
P-K3 The independent lane independently identifies either the Hessian-only
     re-posing or the exact-monoidality reframing. Confidence: MODERATE.
P-K4 R-L2b ranks LEAST tractable of the three named missing objects and is
     the one worth a dedicated campaign. Confidence: HIGH.
P-K5 THE RISKY ONE, stated because a scored risk beats an unstated hunch:
     clause (4)(i)'s "the intensive limit EXISTS AND IS
     CELLULATION-INDEPENDENT" SPLITS, with EXISTENCE nearly free from the
     already-proved exact disjoint additivity and INDEPENDENCE carrying
     essentially all the content. Confidence: MODERATE. Most likely failure
     mode: exact additivity may not extend to the increasing-volume limit
     without the boundary-subextensivity of clause (4)(ii), which is itself
     unproved.
```

## PART C — THE ROUTE-FINDING ANSWER (blind)

### C.0 — The blockage, located precisely from T07 and the theorem text

```text
T7(iii)'s theorem has FOUR clauses. Their sealed status:
  (1) COMPOSITION, cell-local per Lemma 0.
      *** PASS. *** exact_disjoint_monoidal_additivity_proved = TRUE.
  (2) CLUSTER EXPANSION + MAJORANT on |a_c| <= eps_*, absolutely
      convergent, action-density form, UNIFORMLY IN K AND X INCLUDING
      COMMON REFINEMENTS.  BLOCKED. This is where R-L2b, A-L0 arm 2 and
      A-L5 live.
  (3) DIFFERENTIATED SERIES (O5): first and SECOND a-derivatives converge
      absolutely and uniformly on the same polydisc — and the text says
      explicitly "convergence of the undifferentiated series does not imply
      this and may not be cited for it."
      *** SEPARATELY UNSUPPLIED. O5 REMAINS UNSUPPLIED and may not be
      inferred from anything. ***
  (4) COROLLARIES: (i) intensive limit exists AND is cellulation-
      independent; (ii) boundary corrections subextensive at a certified
      rate; (iii) the first two a-derivatives converge to the derivatives
      of the limit — "the interchange used by T7(iv), stated here,
      consumed there".
AND SEPARATELY: T7(ii) volume_uniform_zero_free_neighborhood_proved =
FALSE, which gates thermodynamic_log_hessian_authorized = FALSE. The Log
must be defined before any Hessian of it exists.
THE CHAIN TO kappa_record IS THEREFORE:
  (2) -> (3)/O5 -> (4)(iii) -> T7(iv) -> kappa_record,  AND  T7(ii).
Corpus closure scan, from T07's own evidence: no_successor_closure_found =
TRUE, true_hit_count = 0. Nothing anywhere has closed any of it.
```

### C.1 — (a) IS D3-UNIFORMITY LOAD-BEARING FOR kappa_record, OR FOR THE STRATEGY?

```text
ANSWER: FOR CELLULATION-INDEPENDENCE, NOT FOR THE EXISTENCE OF THE DENSITY.
GROUND: clause (1) is PASS with EXACT disjoint monoidal additivity — not
subadditivity, EXACT additivity. On a region that is an exact disjoint union
of cells, -Log Z_hat_comp is EXACTLY additive, so the density is
(per-cell value)/(cell 4-volume) with NO limit, NO cluster expansion and NO
quantifier over refinements.
SO THE DENSITY EXISTS ON ANY FIXED CELLULATION. What the unrestricted D3
quantifier buys is that it is THE SAME DENSITY ON ALL OF THEM.
  LOAD-BEARING FOR: the CLAIM that kappa_record is a property of the theory
    rather than of the fixture.
  NOT LOAD-BEARING FOR: the ARITHMETIC that produces a number.
AND THE CORPUS ALREADY CONTEMPLATES THIS SPLIT: T13 calls the pinned
skeleton "a regression fixture, NOT PROOF OF UNIVERSALITY". A
kappa_record-on-the-fixture with universality carried as an open obligation
is a structure the sealed text already anticipates.
THE HONEST LIMIT OF THIS ROUTE, stated so it is not oversold: exact
additivity covers the DISCONNECTED part. connected_cross_cell_terms_derived
= FALSE. The cluster expansion exists precisely to handle the CONNECTED
corrections, so this route does not bypass A-L0 arm 2 — IT ISOLATES IT.
That is still a gain: it reframes the task from "prove a cluster expansion
converges uniformly over D3" to "bound the connected corrections to an
already-exact additive structure". One of those is a machine; the other is a
single estimate.
NARROWING TO C_ref REMAINS EXCLUDED, and not by preference: R-L0 and R-L2b
are word-for-word the same obligations inside the shape-regular class, and
the recorded alpha = 0 pathology arises under ISOTROPIC dilation, inside it.
```

### C.2 — (b) IS THERE A PHYSICAL CRITERION PICKING THE CELL SCALE?

```text
ANSWER: ABSENT, AND THE CORPUS APPEARS TO DENY IT.
  BID_MINIMAL_PUBLIC_CAUSAL_CELL, sealed: "a half-line of allowed durations
  and NO ABSOLUTE RECORD SCALE."
  "Absolute physical T_R" is a NAMED PART-C BLOCKER — an undischarged
  whole-program obligation, not a supplied criterion.
SO SUPPLYING ONE WOULD BE A NEW PRINCIPLE, and it would collide with a
sealed negative result rather than filling a gap. Under the transport
charter this branch is additionally CLOSED OFF for tau_R specifically.
BUT ONE PART OF THE PROBLEM DOES DISSOLVE, AND IT IS WORTH HAVING:
  The sealed ISOTROPIC SCALE ORBIT (T_R -> lambda T_R, 4-volume ->
  lambda^4, "dimensionless shape coefficients do not change") means a
  DIMENSIONLESS kappa_record is INVARIANT along it. So the ISOTROPIC
  refinement direction contributes NOTHING to the uniformity problem — it
  is fixed by covariance, not by estimate.
  *** THEREFORE THE ENTIRE REFINEMENT-UNIFORMITY PROBLEM LIVES IN THE
  ANISOTROPIC DIRECTIONS ONLY. *** That is not a route by itself, but it
  halves what R-L2b must cover and it explains why every failure this
  program has found is in the sliver direction and none in the dilation
  direction.
```

### C.3 — (c) TRACTABILITY RANKING, and where a campaign belongs

```text
RANKED BY TRACTABILITY, NOT IMPORTANCE:
 1. PER-CELL TRANSPORT RULE — NOW CHARTERED. Closest by far. Its three
    obligations are unequal: the D2 re-typing is nearly free (determined to
    be WORDING); O-D1 (diamonds do not tile) is a concrete geometric
    construction; O-D3 (decomposition-independence) is the hard one and the
    charter degrades to a new principle without it.
 2. D3 REFINEMENT-NATURAL WEIGHT — HALF DONE, EXACTLY. The weight side is
    closed unconditionally (measure additivity; shape is not among its
    hypotheses). The response side IS R-L2b. So this is not a third object;
    it is item 3 wearing a second label — same collapse already recorded for
    T11.
 3. R-L2b UNIFORM ANISOTROPIC SCHATTEN-2 ESTIMATE — LEAST TRACTABLE, and
    reported by the independent lane as failing as a bound class in the
    sliver direction.
DEDICATED CAMPAIGN: R-L2b, and it earns one on leverage rather than
difficulty. THREE ITEMS COLLAPSE ONTO IT — R-L2b, T11's response half, and
the D3 weight's response side are one obligation. One campaign, three
discharges, and it is the earliest unmet prerequisite. Under the charter it
splits into an ISOTROPIC per-diamond estimate plus a SUMMATION, which is
the first time it has had a natural decomposition.
NOT WORTH A CAMPAIGN: the transport obligations, which are in-line work now
that the definition is fixed.
```

### C.4 — (d) IS THERE A DIFFERENT DEFINITION OF THE INTENSIVE LIMIT? *** THIS IS THE ROUTE. ***

```text
THE SEALED REQUIREMENT IS NOT THE CLUSTER DENSITY. IT IS THE HESSIAN.
  T7(iv) is "Duhamel EQUALS INTENSIVE HESSIAN". Clause (4)(iii) supplies
  "the first two a-derivatives converge to the derivatives of the limit —
  the interchange used by T7(iv), STATED HERE, CONSUMED THERE."
  So what T7(iv) consumes is a SECOND DERIVATIVE AT a = 0.
WHAT CLAUSES (2) AND (3) PROVE INSTEAD: analyticity on an entire polydisc
|a_c| <= eps_*, plus absolute and uniform convergence of the entire
DIFFERENTIATED series. THAT IS STRICTLY MORE THAN A SECOND DERIVATIVE AT
ONE POINT.
*** THE RE-POSING: DEFINE THE INTENSIVE HESSIAN DIRECTLY AS THE
VOLUME-INTENSIVE LIMIT OF THE SECOND-ORDER DUHAMEL/DYSON TERM, AND REQUIRE
ONLY THAT ONE TERM BE VOLUME-INTENSIVE AND CELLULATION-INDEPENDENT. ***
WHAT THAT BYPASSES:
  - eps_star and the polydisc entirely. No radius of analyticity is needed
    for a second derivative at the origin. E1's whole
    epsilon_star-derivation apparatus, and its EPSILON_STAR_VACUOUS failure
    mode, drop out of the critical path.
  - O5 / clause (3) entirely. No differentiated SERIES is needed — one
    term. This matters because O5 is UNSUPPLIED and explicitly may not be
    inferred from clause (2).
  - A-L5 and recast Q6, which are obligations about ANCHORED SUMS over
    cluster size n. A single second-order term has n <= 2.
WHAT IT STILL NEEDS, and this is the honest cost:
  - T7(ii): the volume-uniform ZERO-FREE NEIGHBOURHOOD. Log must be defined
    near a = 0 before it has a Hessian there. NOT bypassed — but a
    neighbourhood of the origin is weaker than a polydisc of radius
    eps_star.
  - The SECOND-ORDER term's own volume-intensive limit and cellulation
    independence — which is where the connected cross term (A-L0 arm 2)
    reappears at n = 2, and where R-L2b is consumed.
  - Clause (4)(ii) boundary subextensivity, for the limit to be intensive
    at all.
ALREADY IN HAND FOR THIS ROUTE, and it is why the route is credible rather
than merely appealing: T7(iv)'s PIECES 1 AND 2 ARE DERIVED and its schema
and L-ADD are SEALED — the conditioned covariance normal form, the
attenuation with the -1/2 (log q)'' diagonal correction, the FS pullback,
and the q-weighted Hessian mixing, with SIX EXACT Route-1 anchors
(0, -1/2, 1/4, 1/4, 1/4, 1/4). The second-order machinery already exists
and is sealed; what has never been done is to make it the DEFINITION of the
intensive Hessian rather than a check against a cluster-derived one.
STATUS OF THIS ROUTE: A RE-POSING OF A SEALED REQUIREMENT, WHICH IS A
PRINCIPAL DECISION AND NOT A LANE'S. It changes what T7(iii) must deliver.
This lane does not adopt it and has not acted on it. IT IS THE ROUTE THIS
LANE WOULD PUT FIRST.
```

### C.5 — Summary of routes found, ranked by this lane

```text
 R1  HESSIAN-ONLY RE-POSING (C.4). Bypasses eps_star, O5/clause (3), A-L5
     and recast Q6. Needs T7(ii), the n = 2 connected term, and (4)(ii).
     Requires a principal re-posing of the battery requirement. FIRST.
 R2  EXACT-MONOIDALITY ISOLATION (C.1). Density exists on a fixed
     cellulation from already-proved exact additivity; the task reduces to
     bounding CONNECTED corrections rather than proving a uniform cluster
     expansion. Isolates A-L0 arm 2 instead of bypassing it. Composes with
     R1 — under R1 the connected correction needed is only n = 2.
 R3  ISOTROPIC-COVARIANCE REDUCTION (C.2). The dilation direction is fixed
     by the sealed scale orbit; only anisotropic directions need estimates.
     Not a route alone; halves R-L2b's burden and explains why every
     observed failure is in the sliver direction.
 R4  FIXTURE-FIRST WITH UNIVERSALITY DEFERRED (C.1). Compute
     kappa_record on the pinned skeleton, carry cellulation-independence as
     a named open obligation. The corpus already calls the fixture "not
     proof of universality", so this is a disclosure structure the sealed
     text anticipates rather than a weakening invented now. Weakest of the
     four in what it establishes; strongest in that it needs no new
     mathematics.
NONE OF THESE IS ADOPTED. R1 and R4 both require principal decisions; R2
and R3 are lane work that changes no requirement.
```

## Protected status

```text
RL2b_restated_over_charter = true
RL2b_closed = false
charter_relocates_anisotropy_to_the_summation = true
charter_supplies_no_estimate = true
P_K1..P_K5_frozen_before_part_C = true
blind = true                       (independent answer not seen)
T7iii_clause1 = PASS_exact_disjoint_monoidal_additivity
T7iii_clause2 = BLOCKED
T7iii_clause3_O5 = UNSUPPLIED_separately
T7ii_zero_free_neighbourhood = false
routes_found = 4
route_ranked_first = hessian_only_reposing
reposing_is_a_principal_decision = true
route_adopted = none
D3_narrowed = false
C_ref_narrowing_still_excluded = true
physical_scale_criterion = ABSENT_and_collides_with_sealed_text
dedicated_campaign_recommended_for = R_L2b (three items collapse onto it)
production_authorized = false
alpha_computed = false
proof_authorized = false
```
