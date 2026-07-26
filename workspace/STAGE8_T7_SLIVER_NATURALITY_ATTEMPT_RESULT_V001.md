# Stage-8 T7 Sliver Naturality Attempt — Result V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY RESULT.
VERDICT: UNDETERMINED_ON_SEALED_INPUTS. The sealed corpus does NOT settle
whether the completed response is volume-natural under sliver refinement.
THIS LANE'S FROZEN P-S1 IS SCORED: ITS GROUND IS REFUTED. The conclusion
is neither established nor refuted, and this lane claims NO credit for it
under any later outcome, because the stated mechanism was wrong.
D3 IS NOT NARROWED. NO SHAPE CONDITION IS ADOPTED. The C_ref/D3 conflict
is NOT resolved by this attempt and remains the principal's.
RECAST Q6 IS **NOT** SHOWN ILL-POSED. PRODUCTION PROHIBITED.
```

Predictions frozen before the attempt at
STAGE8_T7_RULE8_COST_SUPPLEMENT_AND_FROZEN_SLIVER_PREDICTIONS_V001.md
(bdf72fa85d7d97eb…). Five independent lanes plus an adjudicator; the
decisive claim was then re-verified at source by this lane rather than
adopted.

## §1 — P-S1'S GROUND IS REFUTED, and this lane verified it against itself

```text
WHAT THIS LANE PREDICTED, and why it felt safe: "the response pullback
FAILS to be volume-natural under sliver refinement ... GROUND: every cell
runs at FULL tau_R = pi/sqrt(2); the record cycle is a PER-CELL quantity
that does NOT scale with cell 4-volume; refining one cell into N cells
multiplies per-cell record content by N at unchanged volume." It was
offered as structural rather than a guess, and as the O7 root already
sealed for R-L0.

THE REFUTATION, verified by this lane at source, three legs:
 1. THE COMPLETED RESPONSE IS A RATIO. Majorant spec D1, line 116:
        Z_hat_comp(a) := Z_comp(a) / Z_comp(0)
    so Z_hat_comp(0) = 1 IDENTICALLY on every admitted complex, whence
    Gamma(0) = 0 and, by the theorem clause at line 249
    (-Log Z_hat_comp = sum over anchored connected gamma of Phi_gamma),
    Phi_gamma(0) = 0 identically — every cluster, every refinement depth,
    EVERY CELL SHAPE.
 2. THE RECORD TERM IS a-INDEPENDENT. Phase-A spec: the generator carries
    the record tier as "+lambda v(t) M_(n,ell)(t) tensor S_n" (line 126)
    while the history enters ONLY as "+a J(t) tensor I_R" (line 245).
    The full-tau_R record cycle contains no a.
 3. THEREFORE IT CANCELS. An a-independent per-cell factor multiplies
    Z_comp(a) and Z_comp(0) ALIKE and is annihilated by the ratio BEFORE
    any activity is formed. The mechanism P-S1 named cannot inject
    un-suppressed per-cell content into the response, because the quantity
    it acts on is normalized away by the very ratio that DEFINES the
    completed response.

THIS LANE'S ERROR, named precisely rather than softened: IT IMPORTED THE
O7 ROOT FROM THE SETTING WHERE IT BITES INTO ONE WHERE IT DOES NOT. The
tau_R scale-invariance obstruction is real and sealed — for the ACTIVITY /
MAJORANT quantity g(C,eps) under R-L0 ground (i), where there is no
normalizing ratio. The COMPLETED RESPONSE is a different object with a
different typing (the L2 freeze: Z_hat_comp = Z_comp/Z_comp(0), no
unitality anchor), and the ratio is exactly what makes the two settings
different. Reusing a sealed obstruction across a typing boundary is the
same class of error as universal-vs-represented and operator-vs-scalar —
the tripwire this lane named ONE ARTIFACT EARLIER and then walked into.

SCORING, and the scoring rule is the one this lane has applied to others:
A PREDICTION WHOSE STATED GROUND IS REFUTED EARNS NO CREDIT IF THE
CONCLUSION LATER LANDS. P-S1 is recorded as GROUND-REFUTED / CONCLUSION-
OPEN, and this lane will not claim it if the response is later shown
non-natural for some other reason.

NOTE ON THE FALSIFIER: P-S5 said P-S1 dies if |C|_4 is found multiplying
the per-cell record content in the completed chain. The refutation came
through a DIFFERENT DOOR — not by supplying a volume factor, but by the
ratio deleting the record tier from the response altogether. The falsifier
was well-formed and still did not anticipate the actual failure mode.
Recorded because naming a falsifier is not the same as naming the right
one.
```

## §2 — WHY THE QUESTION IS NEVERTHELESS UNDETERMINED

```text
REFUTING P-S1's GROUND IS NOT ESTABLISHING VOLUME-NATURALITY, and the
adjudicator was right to stop short of it.
The response is Delta = C(V(a) - V(0))C, and how ||Delta|| scales with
|C|_4 is obligation R-L2b — whose exponent is UNDERIVED BY SEALED
STATEMENT. E1 v002, R.3 and its repair note:
    "v001 wrote 1/2 without derivation; R-L2b must DERIVE it. Until R-L2b
     closes, alpha is a symbol, not 1/2."
    witness SCAD_HS_SCALING_EXPONENT_UNDERIVED; R.3's half-power
    bookkeeping downgraded to "consistent with D5 CONDITIONAL on R-L2b".
So the sealed corpus contains NO derived statement of how the response
scales with cell 4-volume, in EITHER direction. It does not say
volume-natural and it does not say otherwise.

THE PRECISELY NAMED MISSING SEALED OBJECT, which is the useful output:
    R-L2b — THE HS SCALING EXPONENT OF Delta = C(V(a)-V(0))C IN |C|_4,
    DERIVED RATHER THAN ASSUMED, AND VALID IN THE SLIVER DIRECTION
    (4-volume -> 0 at diameter O(1)), NOT ONLY ALONG THE ISOTROPIC SCALE
    ORBIT.
The sliver direction matters and one lane made the point sharply: the
sealed construction possesses exactly ONE scaling covariance, the
isotropic orbit of BID_ABSOLUTE_RECORD_SCALE_IDENTIFIABILITY_GATE_V001
(4-volume -> lambda^4 with diameter -> lambda*diam). A SLIVER IS
TRANSVERSE TO THAT ORBIT — diameter stays O(1) while 4-volume -> 0 — so
no one-parameter isotropic covariance can supply a weight in the sliver
direction. That observation does not decide the question, but it says
exactly why R-L2b must be derived transversally and not merely on the
orbit.
```

## §3 — the other frozen predictions, scored

```text
P-S2  THE VOLUME WEIGHT SURVIVES SLIVERS EXACTLY.            *** HIT ***
      Ground confirmed and sharpened: mu_e(S) := integral_S |det e| d^4x
      is a countably additive positive Borel measure absolutely continuous
      w.r.t. Lebesgue, because |det e| is nonnegative and measurable.
      Reaggregation of |C|_4 is then LITERALLY THE ADDITIVITY AXIOM OF A
      MEASURE evaluated on sets, whose only hypotheses are measurability
      and a.e.-disjointness. Shape is not among them. This holds on FULL
      D3 — slivers, needles, star-refined atoms of unbounded facet count —
      with no regularity hypothesis whatever.
      NOT claimed as independent credit: it agrees with the independent
      family's already-landed P-C8 first clause.
P-S3  NEGATIVE CONTROLS BITE. NOT INDEPENDENTLY CONFIRMED HERE and
      recorded as such rather than assumed. The weight-half lane's
      decisive finding was the additivity argument; it did not return an
      explicit failing construction for w = 1 and w = diam^4 that this
      lane has verified. P-S3 remains OPEN and the controls must still be
      exhibited before the object could be validated.
P-S4  CONSEQUENCE IF P-S1 HELD.                          NOT TRIGGERED.
      Its antecedent did not establish. *** RECAST Q6 IS NOT SHOWN
      ILL-POSED. *** Nothing here licenses that conclusion, and nothing
      here licenses narrowing D3.
P-S5  See §1. Well-formed, and still did not anticipate the actual
      failure mode.
```

## §4 — what this changes, and what it does not

```text
DOES NOT RESOLVE THE C_ref/D3 CONFLICT. The conflict was that D3's class
is strictly larger than C_ref's with no sealed text recording the
broadening. This attempt was the principal's third path — decide it by
proof rather than preference — and the proof attempt returned
UNDETERMINED. So the conflict is still live and still the principal's.
NEITHER OF THE PRINCIPAL'S TWO BRANCHES IS EARNED. The broad class is not
vindicated (naturality is not shown to survive slivers) and the
restriction is not earned either (no counterexample was produced). The
honest position is that the corpus cannot yet tell.
THE OBJECT SPEC REMAINS HELD. Sealing it still requires choosing an
admissible class, and the attempt did not remove that requirement.
WHAT WOULD SETTLE IT: R-L2b derived in the sliver direction, per §2. That
is now a NAMED, SCOPED obligation rather than an open question, which is
the most this attempt could honestly produce.
```

## Protected status

```text
sliver_naturality_verdict = UNDETERMINED_ON_SEALED_INPUTS
P_S1_ground = REFUTED
P_S1_conclusion = OPEN
P_S1_credit_claimable_later = false
P_S2 = HIT            (not claimed as independent credit)
P_S3 = OPEN           (controls not exhibited)
P_S4 = NOT_TRIGGERED
recast_Q6_shown_ill_posed = false
volume_weight_natural_on_full_D3 = true      (measure additivity, exact)
response_pullback_natural_on_full_D3 = UNDETERMINED
missing_sealed_object = R_L2b_HS_scaling_exponent_derived_in_the_sliver_direction
sliver_transverse_to_isotropic_scale_orbit = true
cref_vs_D3_conflict_resolved = false
D3_narrowed = false
shape_condition_adopted = false
D3_object_spec_status = HELD_PENDING_PRINCIPAL
cross_typing_obstruction_reuse_recorded_as_defect = true
v003_started = false
production_authorized = false
alpha_computed = false
proof_authorized = false
```
