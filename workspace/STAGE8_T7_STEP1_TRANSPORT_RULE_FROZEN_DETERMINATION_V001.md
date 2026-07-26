# Stage-8 Part A Step 1 — Transport Rule: FROZEN DETERMINATION (pre-cross-check) V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY. THIS LANE'S DETERMINATION, FROZEN BEFORE THE INDEPENDENT
CROSS-CHECK RETURNS, per Part G's assignment of step 1 to "Einstein +
Codex check" and per this lane's own record of asserting past its evidence
three times today.
NOT A CONCLUSION. Cross-check commissioned. D3 NOT narrowed. No modelling
choice adopted. PRODUCTION PROHIBITED. alpha_computed = false.
Cites: canonical plan 12f204c64f0c0fd9...; amendment 001 c59cc8337913b81b...
```

## THE DETERMINATION: case (b), NOT DERIVABLE — but CONSTRAINED, not free

```text
VERBATIM, A-L4 (E1 successor spec v002, lines 1086-1091), the ONE place in
the corpus where a |C|_4 factor is derived rather than imposed:
  "shell count R^3 dR / L^4; pair activity s^2 L^8/R^6; in-cell strength
   s <= eps ||b_D||_inf x (cell time extent) ~ eps L;
   int_L^inf R^-3 dR = 1/(2L^2); total eps^2 L^4/2 = |C|_4 (eps^2/2), so
   eta^2 is L-INDEPENDENT. Stated for the TWO-LINE SECTOR on family A, and
   NOT extended to n = 1, NOT extended to the one-line sector, NOT extended
   beyond family A."

THE FINDING: THE SINGLE SYMBOL L CARRIES THREE GEOMETRICALLY DISTINCT
ROLES IN ONE CHAIN.
  ROLE 1  L = CELL TEMPORAL EXTENT, in "in-cell strength <= eps
          ||b_D||_inf x (cell time extent) ~ eps L".
  ROLE 2  L^4 = CELL 4-VOLUME, in the shell-count normalization R^3 dR/L^4
          and in the L^8 of the pair activity (two cells' volumes).
  ROLE 3  L = MINIMUM SPATIAL SEPARATION, as the lower cutoff of
          int_L^inf R^-3 dR.
ON A CUBE OF SIDE L THESE ARE THE SAME NUMBER. ON A SLIVER THEY ARE THREE
DIFFERENT NUMBERS. The identification L^4 = |C|_4 is therefore a STRUCTURAL
ISOTROPY IDENTITY, and A-L4's "NOT extended beyond family A" is a
CONSEQUENCE of that, not a precaution attached to an otherwise general
derivation.

CONSEQUENCE FOR THE PLAN'S BINARY: the plan poses one binary, |C|_4 versus
tau_R x |C|_3. THAT IS UNDER-SPECIFIED. At least THREE candidate readings
exist on an anisotropic cell, one per role above: (cell time extent)^4; the
literal |C|_4; and a reading set by the R = L spatial cutoff. The binary
should be a trichotomy at least.

WHY (b) RATHER THAN (a): to transport A-L4 off cubes, each of the three
occurrences of L must be independently assigned a geometric meaning. The
sealed corpus assigns them nowhere, because on family A it never had to.
Assigning them is a MODELLING ACT.

WHY "CONSTRAINED, NOT FREE" — AND THIS IS THE USEFUL HALF:
  ROLE 1 IS DETERMINED. "in-cell strength <= coupling x (cell time extent)"
  has an actual mechanism behind it — strength = coupling x duration, the
  Duhamel/Dyson form — and duration is unambiguously TEMPORAL. No decision
  is needed there, and any transport rule that makes role 1 anything other
  than the cell's time extent contradicts the mechanism.
  ROLES 2 AND 3 ARE THE DECISIONS. What normalizes the shell count on an
  anisotropic cell, and what sets the minimum separation cutoff when a cell
  has different extents in different directions.
SO WHAT GOES TO THE PRINCIPAL IS NOT "CHOOSE A MODEL". IT IS: "TWO SPECIFIC
SYMBOLS NEED A GEOMETRIC ROLE ASSIGNED; HERE IS WHAT EACH ASSIGNMENT
COMMITS YOU TO." That is a smaller and better-posed decision than the plan
anticipated.

A SEPARATE STRUCTURAL POINT, offered and NOT relied on: A1/A2's support is
|x| < min(t, 1-t), which IS the causal diamond of the unit time interval —
the spatial extent is FIXED BY the temporal extent at the light cone. A cell
whose spatial extent exceeds its temporal extent cannot BE a causal diamond.
So "the cell's causal diamond" and "the cell" are different objects on any
anisotropic cell, and a transport rule must say which one carries the
insertion. If it is the diamond, the natural volume is (time extent)^4 and
role 2 follows role 1. THIS IS NOT ASSERTED as the answer; it is flagged
because it would make roles 1 and 2 agree and leave only role 3 open.
```

## FROZEN PREDICTIONS, before the cross-check

```text
CALIBRATION, as Rule 6 requires: this lane's route-survival predictions run
optimistic across two eras; the independent family stands at FOUR
consecutive landings (P-C5..P-C8); and this lane has asserted past its
evidence THREE times today, twice from mis-scoped searches and once from a
measurement it never took. Weight all of the following accordingly.
P-T1 The independent lane CONFIRMS that the sealed corpus does not
     determine the transport rule (case (b)). Confidence: moderate-high.
P-T2 The independent lane INDEPENDENTLY IDENTIFIES the multiple-roles-of-L
     structure, or something equivalent to it, rather than treating the
     ambiguity as a single binary. Confidence: moderate. This is the
     prediction most likely to fail, because it asks another lane to arrive
     at a specific decomposition rather than a verdict.
P-T3 ROLE 1 (time extent) is confirmed as mechanism-determined and NOT a
     free choice. Confidence: high.
P-T4 The causal-diamond point is judged CORRECT BUT NOT DECISIVE — i.e. it
     narrows the decision without closing it. Confidence: low-moderate;
     stated because a low-confidence prediction that is scored is worth
     more than an unstated intuition.
REFUTATION: if the independent lane exhibits a sealed rule assigning the
three roles, or shows that one assignment is forced by an authority this
lane has not read, then (b) is wrong, step 1 is lane work after all, and
this determination is withdrawn.
```

## Protected status

```text
step1_determination = case_b_NOT_DERIVABLE_BUT_CONSTRAINED
cross_check_returned = false
determination_is_final = false
roles_of_L_identified = 3
role1_time_extent_mechanism_determined = true
roles_2_and_3_require_principal_decision = true
plan_binary_is_underspecified = true          (trichotomy at least)
causal_diamond_point_relied_on = false
modelling_choice_adopted_by_this_lane = none
D3_narrowed = false
P_T1..P_T4_frozen_before_cross_check = true
production_authorized = false
alpha_computed = false
proof_authorized = false
```
