# Transport-Functor Charter — Diamond Decomposition V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY CHARTER, authored by the construction lane ON THE PRINCIPAL'S
DECISION of 2026-07-26. This is an ADOPTION artifact: the definition below
is in force. Nothing in it is this lane's choice; the choice was made by the
principal from the four costed candidates.
Cites: plan 12f204c64f0c0fd9...; amendment 001 c59cc8337913b81b...;
options-with-costs 97149d0859d4f441...; step-1 determination
83fe2fade220a92c...
NO SEALED ARTIFACT IS EDITED. D3 IS NOT NARROWED. R-L2b IS NOT UNBLOCKED.
PRODUCTION PROHIBITED. alpha_computed = false.
```

## §1 — THE DECISION

```text
ADOPTED: OPTION 4 — DIAMOND DECOMPOSITION.
REJECTED, with the principal's reasons recorded so the rejection is citable:
  INSCRIBED DIAMOND — breaks extensivity and the cellulation-independent
    thermodynamic limit. The atom is not covered; the covered fraction goes
    to zero under sliver refinement.
  CIRCUMSCRIBED DIAMOND — breaks D5's action-density form. Activity per unit
    |C|_4 diverges with aspect ratio, which D5 itself declares a spec
    violation.
  ATOM INDICATOR M_C = Q 1_C Q — severs the light-cone tie that A-L0 arm 2
    requires, destroying the Huygens structure; and it is a NEW PRINCIPLE
    rather than a definition, since dropping causality from the construction
    is a physics posit.
GROUND FOR THE ADOPTION: Option 4 breaks NOTHING SEALED. Its costs are
obligations rather than contradictions, and they are accepted as honest work.
```

## §2 — THE DEFINITION IN FORCE

```text
THE TRANSPORT FUNCTOR. For an admitted atom C of the frozen D3 class:
  1. C is covered by a family of DISJOINT CAUSAL DIAMONDS
     {D_1, ..., D_N(C)}, each an affine dilate/translate of the Phase-A
     unit diamond — i.e. each of the sealed form
        0 < t < 1 in its own local time,  |x| < min(t, 1-t),
        r(t) = min(t, 1-t),  M(t) = Q 1_{|x| <= r(t)} Q,
        v(t) = tau_R * 32 r(t)^3,  b_D = exp(16 - 1/s).
  2. EACH DIAMOND IS AN EXHAUSTION UNIT in D2's sense: it carries its own
     cell closure U(tau_R) and typed relay isometry, at FULL tau_R.
  3. THE RESPONSE WEIGHT is the sealed tetrad/Jacobian 4-volume, summed over
     the decomposition:
        weight(C) = sum_i |D_i|_4 ,  and the decomposition is required to
        satisfy  sum_i |D_i|_4 = |C|_4  exactly.
     This is what makes the response VOLUME-TYPED, as required if D5, T11
     naturality, A-L5 and recast Q6 are to be well-posed over D3.
  4. tau_R REMAINS DIMENSIONLESS — the full record interval in each
     diamond's own local time on [0,1], with int_0^1 v(t) dt = tau_R by
     construction. It is NOT a physical duration. See §5.
  5. SEPARATION: A-L1's R = dist(D_1, D_2) is the distance BETWEEN
     DIAMONDS, which is now well-defined because the diamonds are the
     objects the bound quantifies over.
  6. REDUCTION REQUIREMENT, binding: on family A the decomposition must
     reduce to A-L4's |C|_4 scaling. Any decomposition that does not is
     inadmissible.
CONSEQUENCE, and it is the point of the charter: the five pins identified in
the options memo (cell time extent; the volume symbol; minimum separation;
tau_R's units; the diamond on a non-diamond atom) are ALL FIXED by items
1-5. The charter is one definition, as predicted.
```

## §3 — CONDITION 1 DISCHARGED: THE ~A^3 CONFLICT WITH D2 IS WITH ITS **WORDING**

```text
D2's SEALED TEXT, verbatim (majorant spec lines 136-149): admitted
exhaustions are relayed causal exhaustions — cell closure
U_c(tau_R): L_(r_c) -> L_(p_c) followed by the typed relay isometry
R_c |p_(c,h)> = |e_(c,h)> tensor |r_(c+1)> (record preserved, ready root
supplied), causal order per the relayed-family resolution, THEN:
    "Every cell runs at FULL tau_R = pi/sqrt(2). No
     small-record-coupling hypothesis exists anywhere in this spec."

DETERMINATION: WORDING, NOT SUBSTANCE. Four grounds, in increasing force.

 G1 D2's STRUCTURAL CONTENT IS PER-EXHAUSTION-UNIT, NOT PER-REGION. The
    sentence fixes the DURATION PARAMETER OF U_c as tau_R rather than some
    fraction of it. It is a statement about the COMPLETENESS OF EACH
    CLOSURE. Under this charter each diamond is an exhaustion unit carrying
    its own U(tau_R) at full tau_R, so the claim holds per unit EXACTLY AS
    WRITTEN, with the unit re-identified from "cell" to "diamond of the
    decomposition".
 G2 THE PURPOSE CLAUSE IS EXPLICIT AND UNTOUCHED. "No small-record-coupling
    hypothesis exists anywhere in this spec", reinforced by D4's "the
    expansion parameter is the connection difference; the record coupling is
    never expanded in." D2 exists to DENY A SMALL PARAMETER in the record
    coupling. N diamonds each at full tau_R contains no small parameter —
    it is further from one, not closer.
 G3 NOTHING IN THE CORPUS CONSUMES THE COUNT. Searched: "one cycle per",
    "cycles per cell", "record cycle count", "number of record" — NO
    OCCURRENCES. No bound, constant, estimate or control treats record
    cycles per cell as a quantity. A number nothing consumes cannot be a
    substantive commitment.
 G4 DECISIVE: THE COUNT CANNOT REACH THE RESPONSE AT ALL. Record content is
    a-INDEPENDENT, and Z_hat_comp(a) := Z_comp(a)/Z_comp(0) annihilates
    every a-independent per-unit factor before any activity is formed —
    the same structure that refuted this lane's own P-S1. So the response is
    not merely compatible with an A^3 count; it is PROVABLY INDIFFERENT to
    it.

REMEDY, and it is the smaller of the two available: an APPEND-ONLY
AMENDMENT RE-TYPING D2's UNIT — "every EXHAUSTION UNIT of the decomposition
runs at FULL tau_R" — carrying the no-small-record-coupling clause VERBATIM
AND UNCHANGED. That is a RE-TYPING, of the same class as the L2 typing
freeze (which re-typed which chain an object lives on), NOT a scope
narrowing and NOT a weakening. D2 is not edited; the amendment is a
successor.
```

## §4 — A FOURTH ITEM, FOUND WHILE DISCHARGING CONDITION 1. NOT ADOPTED.

```text
THE PRINCIPAL ACCEPTED THREE OBLIGATIONS. THIS IS A FOURTH, AND THIS LANE'S
OPTION ANALYSIS MISSED IT. Recorded as an addition rather than folded in.

D4 / H-IND, sealed: "Per-cell INDEPENDENT source assignments (tensor-form
ready-root supply; no cross-cell record-color correlation — this
independence is hypothesis H-IND, discharged structurally by Lemma 0, and is
the GHZ-discriminating hypothesis of NC1)."
THE QUESTION THE CHARTER CANNOT AVOID: IS THE SOURCE-INDEPENDENCE UNIT THE
ATOM OR THE DIAMOND?
  IF PER-ATOM: the N(C) diamonds inside one atom SHARE a source assignment,
    hence are correlated with each other. H-IND as WORDED survives, because
    it forbids CROSS-CELL correlation and this correlation is INTRA-cell.
    But the decomposition then introduces correlated sub-units that Lemma 0's
    structural discharge was not written to cover.
  IF PER-DIAMOND: there are N(C) times more independent sources per atom.
    H-IND is satisfied more easily, but the DENSITY of independent
    degrees of freedom per unit 4-volume changes with aspect ratio — and
    NC1 is the GHZ-DISCRIMINATING control that rests on H-IND.
EITHER ANSWER GENERATES AN OBLIGATION: show that NC1's GHZ discrimination
survives the chosen reading, and that Lemma 0's structural discharge of
H-IND still applies to the decomposition's units.
*** THIS LANE DOES NOT CHOOSE. It is flagged because the principal accepted
three obligations on the strength of an analysis that had four. ***
```

## §5 — CONDITION 2 DISCHARGED: THE tau_R-AS-PHYSICAL-DURATION BRANCH IS CLOSED

```text
CLOSED OFF EXPLICITLY AND PERMANENTLY WITHIN THIS CHARTER:
  tau_R IS DIMENSIONLESS. It is the full record interval in each diamond's
  OWN LOCAL TIME on [0, 1], normalized by int_0^1 v(t) dt = tau_R, where
  v(t) = tau_R * 32 r(t)^3 and int_0^1 32 min(t,1-t)^3 dt = 1 exactly.
  *** NO ARTIFACT UNDER THIS CHARTER MAY READ tau_R AS A PHYSICAL DURATION
  OF ANY ATOM OR DIAMOND. ***
GROUND, and it is why the branch is inadmissible rather than merely
disfavoured: reading tau_R as a physical duration PRESUPPOSES AN ABSOLUTE
PHYSICAL T_R — a NAMED PART-C BLOCKER, listed as an undischarged
whole-program obligation, and contradicted by the sealed
BID_MINIMAL_PUBLIC_CAUSAL_CELL result: "a half-line of allowed durations and
no absolute record scale." That branch would DISCHARGE A NAMED BLOCKER BY
FIAT.
STANDING RULE FROM THIS CHARTER: any artifact that treats tau_R as a
physical duration is a DEFECT, and the correct response is to report it
rather than to reason from it. If the absolute physical T_R blocker is ever
discharged on its own merits, this clause is revisited by principal decision
and not before.
```

## §6 — THE THREE ACCEPTED OBLIGATIONS, stated precisely

```text
O-D1  DIAMONDS DO NOT TILE. A general atom is not a finite disjoint union of
      causal diamonds. The obligation: exhibit a decomposition scheme whose
      diamonds are disjoint, whose 4-volumes sum EXACTLY to |C|_4 (item 3),
      and whose residual set is null — or, if countably many diamonds are
      needed, prove the sum converges and the tail is controlled.
O-D2  COUNT GROWTH AND THE D2 RE-TYPING. N(C) grows with aspect ratio
      (~A^3 for aspect ratio A). Per §3 this is a WORDING conflict; the
      obligation is to author the append-only D2 re-typing amendment, and
      to carry §3's G4 explicitly so no future lane mistakes the count for a
      response-bearing quantity.
O-D3  DECOMPOSITION-INDEPENDENCE. The decomposition is NOT UNIQUE. The
      obligation: prove the completed response is independent of which
      admissible decomposition is chosen — or exhibit a CANONICAL scheme and
      prove canonicity, which converts the obligation into a definition.
      NOTE: if the scheme is non-canonical AND independence is unproved,
      §4-Q4 of the options memo applies and the charter degrades into a NEW
      PRINCIPLE. Keeping this a definition depends on discharging O-D3.
PLUS O-D4, NOT YET ACCEPTED BY THE PRINCIPAL: the source-independence unit
      question of §4, with its consequent NC1/Lemma-0 obligation.
```

## §7 — WHAT THIS CHARTER DOES NOT DO

```text
IT DOES NOT UNBLOCK R-L2b. The exponent is still underived. The charter
fixes WHAT R-L2b MAY BE STATED OVER — diamonds of the decomposition, with
the tetrad 4-volume as weight — and supplies NO ESTIMATE. Under this
charter the estimate's difficulty is roughly unchanged from its present
state.
IT DOES NOT CLOSE A-L0 ARM 2. It PRESERVES the Huygens structure arm 2
needs, which is why the atom-indicator candidate was rejected; preserving a
mechanism is not supplying a bound.
IT DOES NOT NARROW D3 and adopts no shape condition.
IT DOES NOT RESOLVE C_ref/D3, which remains the principal's and remains
devalued on the restriction side.
IT DOES NOT DISCHARGE T11, A-L5 or recast Q6. It makes their "weighted"
quantifier WELL-POSED over D3, which was the prerequisite; the obligations
themselves stand.
```

## Protected status

```text
charter_in_force = true
charter_option = 4_diamond_decomposition
rejected_options = inscribed, circumscribed, atom_indicator
five_pins_fixed_by_charter = true
D2_conflict_class = WORDING_not_substance
D2_determination_grounds = 4      (decisive one: a-independent content
                                   cancels in Z_comp(a)/Z_comp(0))
D2_remedy = append_only_retyping_of_the_exhaustion_unit
D2_edited = false
tau_R_typing = DIMENSIONLESS_local_time
tau_R_as_physical_duration = CLOSED_OFF_PERMANENTLY
tau_R_physical_would_discharge = absolute_physical_T_R (named Part-C blocker)
accepted_obligations = O-D1 O-D2 O-D3
new_obligation_flagged_not_accepted = O-D4 (source-independence unit; NC1 /
                                     Lemma-0 consequent)
option_analysis_was_incomplete = true      (this lane's; O-D4 missed)
charter_remains_a_definition_iff = O-D3_discharged
R_L2b_unblocked = false
A_L0_arm2_closed = false
D3_narrowed = false
production_authorized = false
alpha_computed = false
proof_authorized = false
```
