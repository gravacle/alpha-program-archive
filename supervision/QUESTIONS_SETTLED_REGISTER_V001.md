# QUESTIONS SETTLED — REGISTER V001

PURPOSE, AND WHY THIS FORMAT. This program retraces ground constantly. The reviewer lane
rediscovered its own result from the previous day on 2026-07-29; 718 of 821 pre-cleanroom root
artifacts are cited nowhere; a rescaling-exclusion section was deleted with no supersession note;
the same file-count figure propagated through fourteen artifacts without anyone opening the
directories it counted.

(The "718 of 821" figure is a machine count recomputed by the sweep recorded in
`RECOVERY_STIFFNESS_AND_ALLOW_REQUIRE_2026-07-29.md`; the file-count figures are a machine count
whose exact command and exclusion list are recorded in `ERRATUM_001_PROGRAM_FILE_COUNT_2026-07-29.md`
under COMPUTATION PROVENANCE. Both are exclusion-dependent. Citing either without its exclusions is
the exact defect this program has already made twice.)

The cause is that findings are indexed BY ANSWER. A future session searching for the QUESTION
never reaches them, because the artifact is named after what was concluded.

**THIS REGISTER IS INDEXED BY QUESTION, PHRASED THE WAY SOMEONE WOULD RE-ASK IT.** Before opening
any new line of work, search this file for the question first. Every row carries: the question as
it would naturally be re-asked, the ruling, WHERE THE PROOF IS, and THE EXACT CONDITION UNDER
WHICH THE ROW REOPENS. A row with no reopen condition is closed permanently.

APPEND-ONLY. Rows are never edited, only superseded by a later row citing the earlier one.
This register ADOPTS NOTHING and DERIVES NOTHING. It records where rulings live.

---

## Q-01. "Can the gravity/gauge coefficient ratio give a depth-free number, so we don't have to select the depth?"

Also asked as: does the depth cancel in the ratio? Can one operator give both couplings so their
ratio is forced? Is the EM-GR ratio parameter-free?

**RULING: NO. PROVED, not merely unestablished.** On the `Lambda^even(C^5)` carrier no
x-independent gravity-to-gauge ratio exists, for any arrangement of thresholds.

WHY: gauge coefficients are weighted by the Dynkin index `t = (0,3,1)`, gravitational coefficients
by the dimension `d = (1,10,5)`. These are linearly independent functionals on the representation
ring. Assuming proportionality on an open interval and using linear independence of `E_1(x+c)` at
distinct branch points forces `1/23040 = 0`.

**THE STRUCTURAL CONTENT, WHICH IS THE THING TO REMEMBER: the singlet has dimension 1 but index 0.**
Gravity sees `Lambda^0`; the gauge sector is blind to it.

PROOF AT: `RESULT_TRACE_COLLAPSE_THEOREM_AND_GRAVITY_GAUGE_IMPOSSIBILITY_2026-07-29.md` §6
(sealed `a7b82f9a1809458 44b95dc3931a64959 1e7c7ad7449e26f035ce7f270cb50d5e`, sidecar in this
directory). Exact rational arithmetic; no depth evaluated.

REOPENS ONLY IF: the carrier changes to one whose blocks are not a direct sum of `su(5)`
representations, or the gravitational coefficients stop being dimension-weighted. Changing
thresholds, offsets, regulator or depth DOES NOT reopen it.

CONSEQUENCE: depth selection is PROVABLY unavoidable on this carrier. It is not a gap a cleverer
assembly might route around.

---

## Q-02. "Are the relative gauge normalizations 3/2 and 1 a real dynamical result we can lean on?"

Also asked as: is the forced-ratio mechanism executed in-tree? Is `K_H = (3/2) K_Q` evidence?

**RULING: THE RATIOS ARE EXACT AND CORRECT. THEY ARE NOT DYNAMICAL.** They are identities of the
construction — pure Cartan representation theory, carrying no dependence on the heat kernel, the
depth, the regulator, or the Casimir offsets.

The producer's `2e-14` PASS/FAIL gates at
`derive_alpha_br_common_induced_coefficients_v001.py:264-273` and `:242-244` **CANNOT FAIL** —
they are identities over the same inventory that defines them. `K_Q = (8/3) K_5` is not
representation theory at all; it asserts `1/24 = 8/192`.

THEOREM: `Tr_{Lambda^k}(XY) = C(N-2,k-1) Tr_fund(XY)` when at least one generator is traceless;
otherwise a `C(N-2,k-2)(Tr X)(Tr Y)` term survives. Cartan is NOT required. Verified exactly for
`N = 3..6`, every `k`, non-commuting generators included.

ALSO TRUE AND WORTH KEEPING: `K_QH = K_Q` IS exactly the trace-orthogonality `Tr(QC) = 0` of the
colour-centre cocharacter to `Q`; and `K_H/K_Q = 1 + Tr(C^2)/Tr(Q^2) = 3/2`.

RECORDED AT: same artifact, §§1-3 and §8. Erratum pointer 002 appended to
`GRAVITY_EVIDENCE_REGISTER_V001_2026-07-29.md`, which had called the mechanism "EXECUTED in-tree".

**TWO EXHIBITED WAYS THE PREDICTION FAILS — carry these with any use of the ratios:**
1. The corpus's OWN operator is built on `|H|` flux-degree blocks, which are inadmissible under
   the second-moment condition and give `(0,0)` and `(2, 4/3)` instead of `(3/2, 1)`.
2. A `U(1)` normalised inside `u(5)` rather than `su(5)` revives the trace term and makes the
   ratios depth-dependent.

REOPENS IF: someone derives that all admissible deformations are full `su(5)`-invariant symmetric
2-tensors on the transported carrier (the antecedent
`STAGE8_SCHUR_RATIO_PROTECTION_SCOPE_ATTACK_V001.md:137-142` records as unestablished), AND
supplies a threshold-transport rule below the breaking scale.

---

## Q-03. "Was the trace collapse a new discovery?"

**RULING: NO. It already existed in three places** — as executable code
(`derive_alpha_boundary_chiral_spectrum_v001.py:25-27`, `dynkin_index = comb(n-2,k-1)`, the only
occurrence of that binomial in the trees), in the reviewer's own memo of the previous day
(`BOHM_SLOT9_THEORY_ATTACK_2026-07-29.md:38-52`), and in collapsed form in the parent ledger
(`alpha_strict_route_decision_ledger_v001.csv:125`).

KEEP THIS ROW. It is the cheapest available reminder that **searching before deriving is not
optional in this corpus**, at a one-day timescale, inside the supervision layer itself.

---

## Q-04. "Do the fences forbid comparing anything to external data before alpha exists?"

Also asked as: can we test anything now? Is the program untestable until the eighteen slots close?

**RULING: NO. Ten of eleven fence instruments ban measured values ENTERING a derivation, not
comparison.** The one genuine comparison ban (G3) is NOT a cleanroom authority — zero cleanroom
citations of either carrier, and the battery spec explicitly replaced the rule it belongs to with
a version containing **no comparison clause**.

**AND G3'S RELEASE CONDITION DOES NOT EXIST.** `stage12_exists_in_corpus = false`. Read literally,
G3 never opens — the corpus contains no procedure for weakening a fence. That is a structural
defect in the fence, not a finding about physics.

THE STANDING PERMISSION NOBODY CARRIED FORWARD: `PREREGISTRATION_V002.md:190-196` types public and
previously-viewed data `diagnostic_only = true`. Blocked: candidate response evaluation, target
reveal, the confirmatory CLAIM. Not comparison.

RECORDED AT: `RESULT_FENCE_INVENTORY_AND_WHAT_IS_TESTABLE_TODAY_2026-07-29.md`.

REOPENS IF: a cleanroom artifact pins a G3 carrier by hash, or a Stage-12 authorization is
written.

---

## Q-05. "Is slot 18 last, so it can only be worked after the other seventeen?"

**RULING: NO. That was an inference from list position, not sealed text.** The eighteen-slot
enumeration carries no ordering language; the corpus's only frozen order is a NINE-item
electromagnetic sequence that does not contain slot 18; the machine-readable form encodes the
slots as an unordered dictionary.

THE REAL CONSTRAINT, which is different and narrower: A32 custodian unmasking sits behind
ALPHA-RESULT-SEAL (`V011:1816-1819`), so an A32-grade holdout cannot COMPLETE before alpha. The
PREDICTION can be derived at any time from a sealed theory output record.

ERRATA APPENDED TO: `THE_MAP.md`, `PLAN_TO_ALPHA_V007_2026-07-29.md`, `TASK_LIST.md` (all
re-sealed).

---

## Q-06. "Has this program ever confronted external evidence?"

**RULING: YES, MORE THAN ONCE, and the claim that it did so exactly once is FALSE.** A completed
freeze-then-score external comparison chain ran 2026-07-12: `f_charged_step9c` froze the
prediction before comparison, `f_charged_step9d` scored it, `step10c` typed the mode, plus
`step12a/12c` and `step13a/13c` (an electron-anomaly non-alpha gate).

**THE OPERATIONAL POINT: THE FREEZE-THEN-COMPARE WORKFLOW EXISTS AND WAS ABANDONED.** Rebuilding it
is a RESUMPTION, not a new capability.

CAVEAT: step 9c's frozen quantity is the textbook one-loop slope, so no same-alpha comparator
differs from it — it was never structure-sensitive, and would not satisfy A32 eligibility.

---

## Q-07. "Did we already project a curvature term for the modulus radius, when we computed an event-horizon size?"

**RULING: NO CURVATURE TERM WAS PROJECTED.** `C_R = 1` is an ADOPTED Level-1 rule; the threshold is
passed into the producer as a function argument
(`derive_bid_minimal_public_causal_cell_v001.py:18-22`,
`scale_ratios(action_marker, causal_radius_fraction, compactness_threshold)`), with
`"physical_premise_proved_by_script": false` on the result.

BOUNDED NEGATIVE (all four roots, exclusions stated in the source artifact): `marginally trapped`
0 files · `apparent horizon` 0 · `Schwarzschild radius` 0 · `gravitational radius` 0 ·
`quasi-local mass` 0 · `Hawking mass` 0 · `Raychaudhuri` 0 · `hoop conjecture` 0 ·
`null expansion` 0. **THE CORPUS NEVER WRITES "HORIZON" ABOUT THE CELL.**

THE HORIZON WORK THAT DOES EXIST RUNS THE OTHER WAY: the parent EDM family computes
Reissner-Nordström outer horizon radii whose result key is literally named `"no_horizon"`, inside a
pass-conjunction with `MIN_EXTERIOR_HORIZON_MARGIN = 1.0`. **Horizon sizes were computed to certify
that horizons are ABSENT.**

WHAT IS TRUE: `C_R = 1` IS, in content, a marginal self-gravitation condition, and it IS the
corpus's only absolute-scale selector — "This fourth input is the selector. Without it, public
recoverability gives a half-line of allowed durations and no absolute record scale."

RECORDED AT: `RESULT_MODULUS_RADIUS_VS_RECORD_CELL_AND_THE_UNATTEMPTED_BRIDGE_2026-07-29.md`.

---

## Q-08. "Is the bundle fiber radius the same object as the record cell radius? If we fix the cell scale, does that fix the coupling?"

Also asked as: can the record cell size supply the compactification radius? Does the geometric
route reduce to the BID scale?

**RULING: TWO OBJECTS, NO BRIDGE — AND THE GATE CONTAINS A PROOF, NOT A PREFERENCE.**

THE PROOF, which is the thing to remember:
> every `R = beta c Delta tau`, `beta > 0`, preserves the base interval, phase periodicity,
> topology, gauge covariance, and unit character while changing `K_KK` by `beta^2`.

**HANDING THE GATE A FULLY DERIVED RECORD INTERVAL STILL LEAVES A ONE-PARAMETER FAMILY FREE.** This
is not "we have not shown they are the same". It is "they cannot be, because beta survives."

SUPPORTING: zero token overlap between the two artifacts; no third artifact carries both
(`radion` occurs in ONE artifact program-wide);
`STAGE8_GRAVITY_EVIDENCE_ADMISSION_AND_FIVE_STRATA_BINDING_V001.md:138-143` explicitly forbids
collapsing the three scale obligations `x`, `rho`, `T_R`; and they are different KINDS of length —
`R` is transverse to spacetime, `R_R` is an areal radius inside it.

ALSO: the modulus stratum S3 is MEMO-ONLY. No audit script, no result JSON, no test.

REOPENS ONLY IF: a derived cross-sector metric rule appears (see Q-09). Nothing else reopens it —
in particular, deriving `T_R` absolutely does NOT.

---

## Q-09. "Can the bundle be built FROM the record structure instead of granted alongside it?"

**RULING: IT ALREADY WAS, AND IT STOPS ONE STRUCTURE SHORT BY CONSTRUCTION.**

`LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md` places one primitive record degree on every admissible
causal record cell and derives the line bundle, the cocycle condition, a connection forced by
covariant comparison, a globally defined curvature, and the unit character. It has a producer, a
result, and a test — **more machinery than the modulus gate has.**

WHY IT CANNOT REACH THE RADIUS, and this is structural rather than a lapse:
> "Connections on a fixed line bundle form an affine space. Bundle geometry does not choose one
> `a`, one curvature, or one kinetic coefficient."

A bundle derived from record combinatorics is TOPOLOGICAL AND HOLONOMIC. **It has no fiber metric,
and a radius is a metric datum.** It was subsequently demoted to provenance-only
(`CONDITIONAL_PROJECTIVE_LIFT_BUNDLE_NOT_PHYSICAL_CONNECTION`).

DO NOT RE-ATTEMPT "derive the bundle from the record structure" EXPECTING A RADIUS. The bundle is
derivable; the metric on it is not, by the affine-space argument above.

---

## Q-10. **THE OPEN QUESTION. "What fixes the conversion between a record cell's internal and external geometry?"**

This is the live one. Everything above is settled; this is not.

THE GAP, named by the corpus in two independent places:
- `COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:63-66` — "The Fubini-Study metric fixes dimensionless
  distances in projective state space. **It does not fix their dimensional conversion relative to
  the spacetime metric or `ell_P`.**"
- `_external_handoffs/fable_alpha_cleanroom/OUTPUT/45_STAGE10_HANDOFF_GEOMETRIC_BRIEF_V001.md:36-42`
  — "**The causal diamond is present but unconsulted.** ... the cell's Lorentzian geometry never
  entered." And `:58-62` — "the ratio of internal (Fubini-Study/phase) geometry to external
  (Lorentzian/diamond) geometry of one record cell. **This is the first point in the program where
  the gravity-facing geometry becomes load-bearing for the coupling.**"

That conversion IS `beta` from Q-08. The free parameter and the missing metric rule are one gap
seen from two sides.

WHY THIS TARGET IS UNLIKE EVERY FAILED IDENTIFICATION: it needs NO bridge between disjoint
constructions. ONE record cell already carries both structures — it is a causal diamond bearing a
primitive projective record degree. Both constructions already agree that object exists.

STATUS 2026-07-30: THE FIRST-OPENING CANDIDATE IS REFUTED — SEE Q-11. The question itself remains OPEN.
SUPERSEDED TEXT (kept for provenance): A structured multi-agent run is asking whether the recovered
first-opening-root principle
(`primitive_same_cell_opening_normalization_principle_v001.md`, 2026-07-21) constrains the internal
phase budget and the external causal geometry SIMULTANEOUSLY. If it does, it fixes `beta`. If it
only touches one side, the geometric route needs an object nobody in this program has.

THE TEST THAT DECIDES IT, and it is the program's own: **permissions compose and never force a
number; only overdetermination does.** Touching both sides is NOT sufficient. The condition must
CLOSE — two independent requirements meeting on one quantity such that only one value satisfies
both. Note the precedent: `boundary_access_closure_threshold_principle_v001.md` was typed
`CELL_CONSTRAINT_ONLY` and "RETIRED AS A STANDALONE K_R SELECTOR" for exactly this reason.

STANDING CAUTIONS ON THIS TARGET:
- `BID_ABSOLUTE_RECORD_SCALE_IDENTIFIABILITY_GATE_V001.md:59-61` (2026-07-23) already located the
  fix in this saddle and recorded it absent: `:90`
  `coupled_gravity_record_stationarity_equation_derived = false`.
- The record interval itself is conditional on a `sqrt(2)` energy-convention choice
  (`BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:89-104`).
- Four independent no-gos already killed radius selection by other means
  (`alpha_first_durable_capacity_moduli_v001`, `alpha_capacity_constrained_induced_action_v001`,
  `alpha_coupled_flux_logdet_modulus_selection_v001`,
  `alpha_coupled_flux_first_capacity_moduli_v001`). Any new attempt must say why it escapes these.

---

## Q-11. "Does the first-opening-root principle fix the internal/external metric conversion?"

Also asked as: is the recovered stiffness principle the missing datum for the geometric route?
Does the opening condition constrain both geometries at once?

**RULING: NO, AND THE ROUTE WAS ALREADY RETIRED BEFORE THE QUESTION WAS ASKED.** Adjudicated by a
nine-agent run 2026-07-30: four independent reads, one adjudication, three hostile verifiers
(2-1 to sustain; the dissent argued the ruling was too GENEROUS).

WHAT THE PRINCIPLE ACTUALLY CONTAINS. `primitive_same_cell_opening_normalization_principle_v001.md`
is 83 lines and defines four objects — `H_energy(K)` (constrained second variation of the canonical
energy), `T_K` (stationary proper record interval), `H_cell(K) = (T_K/hbar) H_energy(K)`, and
`R_BR(K)` (inclusive same-carrier record-fidelity curvature) — joined by ONE equation,
`L_open(K) = H_cell(K) - R_BR(K)`.

**BOUNDED NEGATIVE, search root = that single file, no exclusions, case-insensitive:**
`fubini|beta|metric|diamond|radius|length|ell_P|planck|conversion|internal|external` returns **ZERO**.
The file contains no length, no metric, no radius, no `ell_P`, no `c`, no `G`, and no causal
diamond, and it never uses the words "internal" or "external". **THE INTERNAL/EXTERNAL TYPING WAS
THE REVIEWER'S OVERLAY.** The corpus does not type `T_K` as external geometry or `R_BR` as internal
geometry anywhere. `T_K` is a TIME, not a length; it is defined once in the entire program, with no
defining equation, and the file itself flags `physical_record_interval_derived = false`.

WHY IT DOES NOT CLOSE — parameter count, which is the decisive test. The selection rule contains
exactly ONE equality, `lambda_min[L_open(K_*)] = 0`; the other clauses are an inequality, a rank
condition, a transversality condition and a sign condition, which choose WHICH ROOT rather than
adding a second quantity. **`beta` does not appear in `L_open` at all, so every member of the
family `R = beta c Delta tau` satisfies the condition trivially. The parameter count before and
after is UNCHANGED.** Verdict: ALLOW, not REQUIRE.

THE CORPUS ALREADY SAID THIS, TWICE:
- `primitive_dressed_interval_stationarity_no_selector_gate_v001.md:72-75` — "The unique physical
  interval remains required to place source cost and record gain in one dimensionless cell. **It
  does not, by itself, add a second equation that selects the stiffness.**"
- `ABSOLUTE_STIFFNESS_SELECTOR_ROUTE_LEDGER_V002.md:27-34`, under the heading "Allow/require
  threshold alone" — "It constrains when declared support can become a record. It does not alone
  fix state preparation, complete species, measure, or curvature weight. / `status = CELL_CONSTRAINT_ONLY`"

**AND THE ROUTE IS FORMALLY RETIRED.** `STAGE8_FIRST_OPENING_ROOT_PRINCIPLE_RECOVERY_INDEX_V001.md:76-79`
— `L_open_route_retired = true`, `first_opening_root_route_restored = false`,
`first_opening_root_computable_from_current_working_set = false`; and `:73`, which anticipates
exactly the move that was attempted: **"the retired `L_open` subtraction may not be reused by
renaming its terms."**

TWO FURTHER DEFECTS IN THE OBJECT ITSELF:
- The subtraction is UNAUTHORIZED. `primitive_native_ctp_opening_adjudication_v001.md:5-8` — the ADM
  quadratic form and the fidelity curvature "are different components of a closed-time-path
  functional. They are not two positive metrics whose numerical equality is implied by sharing a
  coordinate basis." `:20` — "The positive-cost version of the rule is not authorized for this branch."
- `R_BR` is NOT the modulus gate's Fubini-Study object. Same index `:63-65`: it "does not descend
  from `PRIMITIVE_ADDITIVE_RECORD_FIDELITY_ACTION_V002`; the association is a cross-tree name
  resemblance."

REVIEWER FINDING ON PROCESS, RECORDED BECAUSE IT IS THE POINT OF THIS REGISTER: the reviewer lane
proposed this route on 2026-07-30 **without finding the retirement index that already closed it**,
on the same day it built this register to stop exactly that. Search before proposing is not
optional. See Q-03.

WHAT DIES WITH IT: any claim that recovering the first-opening principle advances the geometric
route; any use of `L_open` to steer active work; the line that the recovered principle is the
missing datum.
WHAT DOES NOT: the principle remains valid evidence for the earlier stiffness frame, and the
allow/require typing stands.

**ONE LIVE THING SURVIVED THE VERIFIERS, AND NO ARTIFACT NAMES IT.** Both constructions write the
coupling in the same convention — `alpha_micro = 1/(4 pi K_*)` at the principle `:71-73`, and
`alpha_tree = 4 ell_P^2/R^2`, i.e. `1/(4 pi K_KK)`, at the gate. Composing them gives
`beta^2 = 16 pi ell_P^2 K_* / (c^2 Delta_tau^2)`. It fails today for three stated reasons: it needs
`Delta_tau = T_K`, which is dimensional analogy and is the spec's own falsifier F2; `K_*` is a
function of `T_K`, so the result is a CURVE indexed by `T_K` rather than a point; and the radion is
untouched. **But it is the live route if `T_K` ever becomes an output.** PART-PROVABLE.

REOPENS IF: `T_K` is derived as the output of a stated variational problem with a metric and a
region attached. Nothing else reopens it, and renaming the terms of `L_open` explicitly does not.

CORRECTLY-TYPED LIVE HOME FOR THIS QUESTION:
`STAGE8_CROSS_SECTOR_METRIC_RULE_ADMISSIBILITY_SPEC_V001.md`, whose status reads
`cross_sector_metric_rule_specified_as_target = true`, `cross_sector_metric_rule_derived = false`,
`candidate_test_executed = false`, with a six-item minimal pass condition in its section 6.
**Work the spec, not `L_open`.**

---

## Q-12. "Can getting the surface geometry right fix the coupling? Does removing the rescaling freedom exclude the counterterm?"

Also asked as: is slot 9 malformed because it is posed in bulk language? Will a better geometric
picture of the record surface determine the normalization?

**RULING ON THE RESCALING ARGUMENT: NO, IN BOTH DIRECTIONS, AND THE CORPUS ALREADY RAN THE AUDIT.**
The reviewer proposed on 2026-07-30 that adding `c F^2` to `K F^2` is a rescaling, that Gravacle
removed the rescaling freedom, and that slot 9 is therefore already excluded. Then proposed the
inverse — that removing the freedom makes the counterterm physical and slot 9 WORSE. **BOTH FAIL.**
`alpha_strict_route_decision_ledger_v001.csv:469` records under
`joint_matter_em_gravity_hessian_selector_v001`: "a congruence audit excludes field-coordinate
rescaling as the cause". And the K=1 / K=2 witnesses "preserve compact normalization while changing
the Coulomb response" (`strict_current_audited_alpha_underdetermination_v001`, same ledger). **THE
AMBIGUITY WAS NEVER A RESCALING.** Rescaling is orthogonal to slot 9. Someone ran that audit and
nobody carried the result forward.

**THE LARGER RULING, AND IT IS THE MOST CONSEQUENTIAL STRUCTURAL FINDING OF THE SESSION:
THE OBSTRUCTION IS A SCALING SYMMETRY, AND GEOMETRY CANNOT BREAK IT.**

Eight independent `BLOCKED` rows in `reports/alpha_strict_route_ledger_audit_v001.md` and
`alpha_strict_route_decision_ledger_v001.csv` carry the SAME failure reason — a continuous positive
family survives a scale-covariant condition:

- `strict_charged_causal_closure_alpha_origin_v001` — "even granting a cycle compact U(1) locality
  causality positivity and public records admit a continuous positive Maxwell-stiffness family with
  distinct couplings"
- `strict_charged_record_stiffness_selection_v001` — "its standard flux Hessian is positive for
  every finite K"
- `strict_compact_holonomy_flux_record_cell_v001` — "H_K=(K/2)P^2+X^2/(2K) has one
  minimum-uncertainty ground record for every K>0; canonical X-to-sX and P-to-P-over-s rescaling
  preserves the algebra and uncertainty product while changing widths"
- `strict_public_record_influence_kernel_v001` — "under natural Maxwell scaling both decoherence and
  dressed self-flux scale as 1/K and cannot select a finite K"
- `prerecord_boundary_transfer_kernel_v001` — "exact positive transfer kernels with different
  diffusion constants or tensors preserve those requirements while changing first-mode cost"
- `strict_first_record_capacity_alpha_selector_v001` — "K_star=A, which moves under exact admissible
  changes of coupling duration or environment covariance"
- `joint_record_state_qfi_metric_v001` — "exact same-generator witnesses with different normalized
  states give QFI 1, 3/4, and 0"
- `minimal_public_carrier_dimension_v001` — "exact four-state unit-charge counterassignments with and
  without neutral occupancy give different matter-gravity-reduced EM responses"

**EVERY CONDITION THE PROGRAM HAS IMPOSED IS SCALE-COVARIANT** — positivity, locality, causality,
gauge invariance, compactness, uncertainty saturation, marginality, the allow/require onset, the
first-opening root. So the entire family satisfies all of them simultaneously. **YOU CANNOT BREAK A
SYMMETRY WITH CONDITIONS THAT RESPECT IT.**

This is the same object as: `beta` surviving in the modulus gate (Q-08); the four capacity no-gos;
slot 9; and falsifier F1 (`beta_family_survives`) in
`STAGE8_CROSS_SECTOR_METRIC_RULE_ADMISSIBILITY_SPEC_V001.md`. **ONE OBSTRUCTION, NOT FIVE.**

**CONSEQUENCE FOR THE GEOMETRY QUESTION, WHICH IS WHAT THE PRINCIPAL ASKED.** The four adopted
departures — `K_bare = 0`; removal of the rescaling freedom; the record surface being PRIOR to the
connection; records as fundamental boundary degrees of freedom — are all STRUCTURAL, TOPOLOGICAL OR
ORDERING statements. **NONE OF THEM BREAKS A SCALING SYMMETRY.** Therefore no amount of getting the
surface geometry right can fix a normalization. Shape does not determine scale. This is why every
geometric insight of 2026-07-29/30 sharpened the question and none moved the number.

**WHAT THE CORPUS SAYS WOULD BREAK IT**, in its own words, from the reopen condition on
`strict_compact_holonomy_flux_record_cell_v001`: "reopen only if an independently derived public
metric or **NON-SELF-SIMILAR** microscopic term breaks canonical squeezing before alpha evaluation;
equal-width balance may not be adopted as a unit convention."

**WHY THE ONE SUCCESSFUL DERIVATION SUCCEEDED.** The minimal-cell derivation pairs an internal
action quantum with an external self-gravitation condition, and it works because `G` supplies a
DIMENSIONFUL, INDEPENDENTLY FIXED scale. `G` is the scale-breaking ingredient. That is the entire
trick, and it is the only place in the program where it has been performed.

**WHY THE CHARGE SECTOR HAS NO ANALOGUE.** Charge is quantized in INTEGERS; integers are scale-free;
and the modulus gate states that the phase period "fixes the coordinate period and integer character
lattice. It does not fix the proper radius `R`." So `beta` is free for a STRUCTURAL reason, not for
want of cleverness.

**UNTESTED CONSEQUENCE, TAGGED AS REVIEWER INFERENCE AND NOT ESTABLISHED.** In known physics the
objects tying charge to a length involve a MASS (Compton wavelength, classical radius). If a mass is
the only scale-breaking ingredient available to the charge sector, then slot 9 and the fiber radius
are blocked on slot 14 (charged-species and threshold map) and slot 13 (charged pole / infraparticle
threshold), and **no artifact draws that arrow.** This is an inference from outside the corpus and
has the same shape as six claims refuted on 2026-07-29. UNDER TEST as of 2026-07-30.

REOPENS IF: a condition is exhibited that is NOT invariant under the positive scaling family. That
is the only thing that reopens it. Better geometric pictures, additional structural axioms, and
further ordering statements do not.

---

## Q-13. "Which of the eighteen slots can ever fix the number?" — AND THE CORRECTION OF Q-12

SUPERSEDES THE OVERREACH IN Q-12. Q-12 is not withdrawn; its core survives. Six specific claims in
it are corrected below. Established 2026-07-30 by a hostile audit of Q-12 against the primary
ledger (170 blocked/rejected rows classified; `alpha_strict_route_decision_ledger_v001.csv`, 795
rows total, exclusions as stated in the source artifact).

### PART A — THE SLOT CLASSIFICATION. THIS IS THE ACTIONABLE RESULT.

Test applied: does discharging the slot introduce a NEW DIMENSIONFUL, INDEPENDENTLY FIXED quantity
(scale-breaking, could select), or only an invariance / limit / exhaustion / matching / protocol
requirement (scale-covariant, cannot select)?

**FOUR SLOTS CAN BREAK A SCALE: 1 (absolute `T_R`), 2 (full gravitational action), 6 (functional
regulator + finite renormalization), 13 (charged pole / infraparticle threshold — POLE BRANCH ONLY).**

**TWO ACT ON OTHER FREEDOMS: slot 9** (the ADDITIVE shift — translation-breaking, NOT
scale-breaking) **and slot 14** (supplies dimensionless mass RATIOS, so it attacks the already
scale-invariant depth `x`, not the scaling orbit).

**TWELVE CANNOT FIX A NORMALIZATION UNDER ANY CIRCUMSTANCES: 3, 4, 5, 7, 8, 10, 11, 12, 15, 16, 17,
18.** They are invariance, limit, exhaustion, matching-identification or protocol obligations.
Slot 8 is actively anti-selective — it DEMANDS invariance under cell count, packing density, valence
and refinement rate, and a condition that requires invariance cannot select. Slot 16 transports a
scale supplied by slot 13 and cannot originate one. **DISCHARGING ALL TWELVE PERFECTLY CHANGES
NOTHING ABOUT THE NUMBER.**

**THREE CONSEQUENCES:**

1. **SLOT 6 IS THE MOST UNDER-PRIORITISED ITEM IN THE PROGRAM.** It is the only scale-breaking slot
   the corpus itself names as the ORIGIN of response normalization —
   `EM_DEPENDENCY_ORDER_FREEZE_V001.md:32-34`: "Because zero bare `F^2` is adopted, **the
   functional-regulator and finite renormalization step is where response normalization can
   originate**." It sits at position 4 of 9 in the frozen order, UPSTREAM of the pole (7) and Thomson
   (8). Both of the corpus's independent enumerations of scale-breakers terminate at a local anomaly
   or renormalization condition, which is slot 6's content. Its status is merely "OPEN,
   PRINCIPAL-GUARDED."

2. **SLOTS 6 AND 12 DIRECTLY CONTRADICT EACH OTHER AND NOBODY HAS ADJUDICATED IT.** Slot 6 is where a
   scale MAY ORIGINATE; slot 12 demands continuum-regulator independence with "no hidden finite
   selector." **If slot 12 is discharged as written, slot 6 CANNOT supply a scale.** One of the two
   obligations must be re-posed. This is a live contradiction inside the eighteen and it is
   unrecorded anywhere else.

3. **SLOT 9 IS NOT DOWNSTREAM OF ANY SCALE-BREAKER.** It cannot be discharged by slot 1, 2, 6 or 13.
   `BOHM_SLOT9_THEORY_ATTACK_2026-07-29.md:97-99`: "`c_R` is `x`-independent, so it is invisible to
   any condition that acts through `x` ... **The saddle that selects `x` cannot select `c_R`, because
   `partial c_R / partial x = 0`.**" Anyone sequencing slot 9 behind an absolute scale is sequencing
   it behind something that provably does not reach it.

### PART B — SIX CORRECTIONS TO Q-12

1. **"ONE OBSTRUCTION" IS WRONG. THERE ARE THREE INDEPENDENT FREEDOMS.**
   - **F-scale**, a multiplicative normalization — the scaling orbit. **21 ledger rows.**
   - **F-shift**, an ADDITIVE offset (`c_R` / `K0`). **10 rows.** `alpha_strict_route_decision_ledger_v001.csv:429`,
     decision `gravity_match_does_not_remove_additive_K0` — "countermodels with the same gravity
     coefficient regulator and EM slope retain different additive Maxwell stiffness ... **do not infer
     absolute EM normalization from `G`**." **A SHIFT IS NOT A DILATION. NO SCALE-BREAKING INGREDIENT
     DISCHARGES IT.**
   - **F-ratio**, the dimensionless depth `x`, which is ALREADY scale-invariant, so a scale-breaker
     cannot fix it either (`STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V001.md:455`: "THE HAZARD, STATED:
     `tau_R` is scale-INVARIANT").
   Q-12 also contradicted itself 35 lines apart — ruling "the ambiguity was never a rescaling" and
   then folding slot 9 back in as "one obstruction, not five." Both cannot stand. **The second is
   struck.** And `STAGE8_GRAVITY_EVIDENCE_ADMISSION_AND_FIVE_STRATA_BINDING_V001.md:138,150` forbids
   collapsing `x`, `rho` and `T_R` — `routes_merged = false`.

2. **THE COUNT: NOT EIGHT ROWS, AND NOT ALL OF THEM.** The true scaling-orbit population is **21**,
   2.6x Q-12's list. But of Q-12's own eight, TWO ARE NOT INSTANCES: `joint_record_state_qfi_metric_v001`
   (QFI 1, 3/4, 0 — three discrete states, one degenerate, not a continuous family) and
   `minimal_public_carrier_dimension_v001` (a discrete occupancy choice, and its status is
   `CLOSED_BUT_INSUFFICIENT`, not `BLOCKED`). Honest share: **21 of 170 blocked/rejected rows
   (12.4%); 21 of the 50 UNDERDETERMINATION rows (42%)** — the largest single mechanism, and a
   minority.

3. **"EVERY CONDITION THE PROGRAM HAS IMPOSED IS SCALE-COVARIANT" IS FALSE.** At least EIGHT imposed
   conditions DO break the scaling, and they failed differently — **by MONOTONICITY, with no interior
   root**: ledger:138 `monotone_no_finite_scale`, "under common homothety every positive heat-kernel
   term is strictly monotone and the one-carrier induced determinant selects only an endpoint"; also
   ledger:130, 142, 156, 164, 263. And TWICE a condition selected a definite number and was rejected
   for being WRONG (ledger:149; ledger:517, rejected against its declared holdout). **So breaking the
   symmetry is necessary and nowhere near sufficient — a scale-breaker must also survive the
   monotonicity failure mode.**

4. **PAIRING `beta` WITH `c_R` WAS WRONG, AND IT IS THE OVERREACH IN MINIATURE.** Three registered
   senses: `beta` = the cross-sector FIBER-RADIUS conversion (a metric datum); `c_R` = the ADDITIVE
   finite `F^2` coefficient (slot 9); `C_R` = the COMPACTNESS RATIO (the gravity-side selector that
   worked). Welding a metric-datum freedom to an affine-shift freedom and naming the pair after the
   third object is exactly how "one obstruction" was manufactured.

5. **"THE ONE SUCCESSFUL ABSOLUTE-SCALE DERIVATION" IS NOT ONE.**
   `BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:184-185`: "the causal-cell formulas are exact
   conditional algebra, **not an absolute scale derivation**." The cell file contradicts itself —
   `:7` claims it derives the absolute scale, while `:164-165` flag
   `absolute_record_interval_derived_in_declared_branch = false` and
   `primitive_record_radius_derived_in_declared_branch = false`. Corpus-accurate word: **SELECTOR**.
   And **`G` is necessary and NEVER SUFFICIENT** — the file names its FOURTH input as the selector
   (`:59-60` "This fourth input is the selector"), and that input is the ADOPTED Level-1 rule
   `C_R = 1`, not `G`.

6. **"NO ARTIFACT DRAWS THE MASS ARROW" IS FALSE AND IS STRUCK.** Seven artifacts in four lineages
   draw it, including a titled no-go: `reports/alpha_parent_mass_threshold_no_go_v001.md:9` — "the
   current parent operator cannot provide the logarithmic decoupling spectrum **needed by the induced
   gauge stiffness** ... Representation Casimirs are diffusion eigenvalues, **not a substitute for the
   missing symmetry-breaking mass operator**"; and in the LIVE cleanroom as a failure rule,
   `ABSOLUTE_STIFFNESS_SELECTOR_ROUTE_LEDGER_V003.md:116-126` — "The route fails if ... the Thomson
   limit is asserted without a derived massive charged sector." **BUT THE ARROW POINTS FROM SLOT 13
   TO SLOT 16, NOT TO SLOT 9.** A mass is NECESSARY for the Thomson/induced-stiffness step,
   NOT SUFFICIENT for slot 9 (a scale does not move a shift), and NOT the only scale-breaker — 39 of
   41 catalogued ingredients are not masses, and `EM_DEPENDENCY_ORDER_FREEZE_V001.md:32-34` names
   SLOT 6, not slot 14, as the origin of normalization. Also
   `EM_DEPENDENCY_ORDER_FREEZE_V001.md:28-30`: "**Thomson matching may not presuppose a sharp massive
   charged pole.**"

### PART C — WHAT THE CORPUS ASKS FOR, COUNTED

**41 distinct scale-breaking ingredients** are named across reopen/release/closure clauses. Full
catalogue in the source audit. Two independent in-corpus enumerations exist and BOTH terminate at a
local anomaly / renormalization condition or an empirical calibration:
`field_access_allow_require_unification_v001.md:7633-7671` ("There are only three clean ways") and
`f_charged_step18c_local_chiral_scale_breaking_attempt_v001.md:120-134`. **That is the corpus telling
you twice, independently, that its own shortlist for the charge sector is a RENORMALIZATION
CONDITION — slot 6, not slot 14.**

BOUNDED NEGATIVES WORTH KEEPING: `conformal anomaly` ZERO hits anywhere. `trace anomaly` ZERO.
`scale breaking` ZERO. `anomalous dimension` ONE hit total. `Planck` in a reopen condition appears
ALWAYS as a prohibition, never as a permitted input.

REOPENS IF: the slot classification is challenged at a specific slot with the obligation text quoted,
or a thirteenth slot is shown to carry a dimensionful independently-fixed quantity.

**ACTIVE WORK ARISING:** `DEPARTURE_2_RESCALING_EXCLUSION_FOUR_CHANNEL_AUDIT_V001.md` — the one
departure aimed at the scaling family, recovered and undischarged, reduced to a four-item checklist.

---

## Q-14. "Was the rescaling exclusion deleted without a supersession note, and is the four-channel audit the way to discharge it?"

Also asked as: is Departure 2 a live lever we can work now? What does the corpus say about the
field-energy integral? Did an unversioned tree lose a necessary condition?

**RULING: THE DELETION WAS SUPERSEDED, NOT SILENT; THE REQUIREMENT IS LIVE AND STRONGER; THE CHANNEL
LIST IS FIVE, NOT FOUR; AND THE AUDIT IS AN ACCEPTANCE CHECK ON AN OPERATOR THAT WAS NEVER BUILT.**
Established 2026-07-30 by executing the channel-4 scoping step V001 of the tracker asked for.

The supersession note is `primitive_record_cell_selection_principle_v002.md:3-16`, headed "## Correction
to v001", three minutes after v001 (mtimes 15:10 -> 15:13, 2026-07-20), restated the same minute in
`provenance/primitive_record_cell_selection_preregistration_v002.json`. Reason given: the division rule
`K_R = 4(Phi_* - Gamma_rest,*)/I_F,*` "is valid only if the selected field configuration and the action
partition are already independent of `K_R`. A coupled matter-electromagnetic-gravitational saddle need
not have that property." Plus: "No numerical cell or alpha value was evaluated between the two versions."

THE REQUIREMENT SURVIVES AS A BLOCKING RULE, not a remark: `v002:131-133` failure rule 3 — the
construction blocks if "changing an admitted boundary condition, measure, regulator, or action partition
changes `K_*` without a theory-derived exclusion" — and rule 4 on rescaling `A`. Preregistration v002
requires "a mutation audit over admitted geometry, clock, measure, **regulator**, and action-partition
alternatives."

**THE FOUR CHANNELS WERE THE FOUR INGREDIENTS OF THE SUPERSEDED DIVISION RULE.** The live list is five:
geometry, clock, measure, regulator, action-partition. `field-energy integral` is not among them —
`I_F` survives only in the envelope identity at `v002:111-120`, which `:121-123` disposes of: "This
identity checks the implementation. **It does not select `K_*`**." Bounded negative, roots parent tree
+ external handoffs + supervision, types md/json/csv/py, exclusions node_modules + `external/` +
custodian_private, case-insensitive: `field-energy integral|energy integral` = 6 hits in 6 files, **every
one the exclusion sentence or a restatement of it. Zero independent occurrences.**

**AND IT CANNOT BE RUN.** `results/primitive_record_cell_joint_selector_readiness_v001.json` lists five
failed authorization checks, the fifth being `joint_operator_passes_mutation_audit` — a check ON the
operator. There is no `C_record(K)`, so no `K_*`, so nothing for a channel audit to move. `next_gate`:
"derive one complete target-independent `Gamma_K` and BR closure operator whose joint stationary problem
outputs `Delta_tau(K)` and a scalar `C_record(K)`." The adjudication is worth keeping: the principle
"would turn alpha into a surface-selected eigenvalue if its joint operator were constructed."

WHAT DIES: the four-channel audit as the next work item; "channel 4 is the least-examined place where
the freedom probably lives"; "no supersession note"; and the V001 argument that the 07-24 minimal-cell
derivation could not have known the requirement existed (it was live and stronger from 07-20 15:13).
WHAT DOES NOT: Departure 2 is still the only departure that demands the scaling family be defeated, and
v002 rule 3 makes that demand blocking. The ceiling also stands — discharging it is necessary for a
selector and is not a number.

FULL WORKING: `DEPARTURE_2_RESCALING_EXCLUSION_FOUR_CHANNEL_AUDIT_V002.md` (this directory).

REOPENS IF: `Gamma_K` and `C_record(K)` are constructed, at which point the five-channel mutation audit
becomes the acceptance criterion and should be run in full. Nothing else reopens the four-channel form.

CAUTION CARRIED FORWARD: `Gamma_K` is a NEW UNREGISTERED COLLISION. In `v002` it is the complete
microscopic CTP functional indexed by the coupling; in the live cleanroom it is a BID amplitude
functional indexed by a cell set (`BID_MONOIDAL_EXTENSIVITY_DERIVATION_V001.md:34`,
`Gamma_K(A) = -log|A_K(A)|`, 12 files). Third instance after `C_R` and `K_H`.

---

## Q-15. "Does Q-11's refutation also kill the first-positive-root determination of the stiffness?"

Also asked as: is the root-condition route dead? Did the L_open refutation close K_*?

**RULING: NO. TWO DIFFERENT TARGETS, TWO DIFFERENT VERDICTS. The `beta` arm is refuted; the `K_*` arm is
unbuilt.** Established 2026-07-30 alongside Q-14.

Q-11's argument is a parameter count: `beta` does not appear in `L_open`, so every member of
`R = beta c Delta tau` satisfies `lambda_min[L_open(K_*)] = 0` trivially, and the count is unchanged.
**That argument is silent on `K_*`, which is the quantity `L_open` was built to select.**

And the retirement is by non-computability, not refutation.
`STAGE8_FIRST_OPENING_ROOT_PRINCIPLE_RECOVERY_INDEX_V001.md:70-79`:
`first_opening_root_computable_from_current_working_set = false`, `L_open_route_retired = true`, and in
its own words "Whether a first-opening root can be formed from one microscopic CTP functional is open."

The same shape is posed one day EARLIER by
`primitive_record_cell_selection_principle_v002.md:95-97,:104` — `C_record(K_*) = 0`,
`dC_record/dK != 0` at `K_*`, `K_* > 0`, `alpha_micro = 1/(4 pi K_*)`. Whether the 07-21 principle is
its operator realization is a plausible lineage and is NOT asserted.

WHAT THIS PERMITS: treating `C_record(K)` as a live target. WHAT IT DOES NOT PERMIT: reusing `L_open`.
The prohibition is explicit and unchanged — "the retired `L_open` subtraction may not be reused by
renaming its terms" — and the two defects in the object itself (unauthorized subtraction; `R_BR` is not
the modulus gate's Fubini-Study object) stand as Q-11 recorded them.

REOPENS/CLOSES IF: `C_record(K)` is constructed and either yields a unique simple positive root or is
shown to admit a surviving stiffness-changing family under the five-channel audit of Q-14.

---

## Q-16. "Can the regulator step fix the coupling, or must the answer be regulator-independent?"

Also asked as: does slot 12 kill slot 6? Is a finite renormalization condition a hidden selector?
Where does the response normalization originate?

**RULING: SLOT 12 IS RE-POSED AS SCHEME-COVARIANCE. THE REGULATOR STEP MAY ORIGINATE THE
NORMALIZATION.** PRINCIPAL ACT, 2026-07-30. Physical outputs must be independent of the regulator
FAMILY; exactly ONE finite renormalization condition is permitted, admissible only if DERIVED from
the parent rather than chosen. A condition forced by the theory is not a hidden finite selector; a
condition selected by its outcome is, and remains forbidden.

THE CONTRADICTION IT RESOLVES: `EM_DEPENDENCY_ORDER_FREEZE_V001.md:32-34` makes slot 6 the only
named origin of response normalization ("Because zero bare `F^2` is adopted, the functional-regulator
and finite renormalization step is where response normalization can originate"), while slot 12
demanded regulator independence with no hidden finite selector. Discharging 12 as written closed 6.
Raised at Q-13 consequence 2 and independently at Q-14 §5.

WHY: with `K_bare = 0` there is no counterterm to absorb anything, so the induced coefficient IS what
the regulated calculation produces — total regulator-independence would require the coupling not to
depend on what generates it. Scheme-independence never meant condition-freeness. And the absolute
form of slot 12 is a machinery-shaped requirement standing in front of a physical mechanism, which
the principal's binding rule of 2026-07-29 forbids.

**IT DOES NOT MAKE SLOT 6 EASIER.** Two new obligations: O-SC1, derive the finite renormalization
condition from the parent, target-blind and sealed before any response is evaluated — if it is
adopted instead, slot 6's originating role LAPSES and this row reopens; O-SC2, exhibit covariance
across a regulator family whose membership is defined in advance.

RULING AT: `SLOT12_SCHEME_COVARIANCE_PRINCIPAL_DECISION_2026-07-30.md` (this directory), with
falsifiers F-SC1/F-SC2/F-SC3 frozen. Not in force in the governing chain until registered — owed via
paste 130.

REOPENS IF: F-SC1 fires (the condition is chosen, not derived), or F-SC2 fires (outputs vary across
the stated family), or the permitted condition fixes a PRODUCT rather than a magnitude.

DOES NOT REACH: slot 9. `d c_R / d x = 0`, and a shift is not a dilation.

---

## Q-17. "Who may work slot 6, and in what order?"

Also asked as: is the regulator slot still principal-guarded? Can the lane touch the functional
regulator? What has to happen before a response is evaluated?

**RULING: THE GUARD IS LIFTED. THE LANE IS CHARTERED, AND O-SC1 COMES FIRST.** PRINCIPAL ACT,
2026-07-30, paired with Q-16.

O-SC1 — derive the finite renormalization condition from the parent, target-blind, stated and sealed
BEFORE evaluation — must be attempted before any response is evaluated. No coefficient, no coupling,
no response evaluation until that condition exists as a sealed artifact or is honestly reported
underivable.

WHY THE GUARD COULD GO: its protective function is now carried by Q-16's F-SC1, which makes an
ADOPTED condition an automatic LAPSE of slot 6's originating role. A lane that chooses rather than
derives gets a recorded lapse, not a number. The prohibition is redundant; the falsifier is not.

WHY THE ORDER IS THE SUBSTANCE: evaluate a response first and then find a condition reproducing it,
and the condition was selected by its outcome. That is the move that produced ledger row 516's
`K = 3/16 + E1(1)/(12 pi^2)` and got it rejected at row 517. Deriving first is what makes a value
forced rather than fitted.

ACCEPTABLE OUTCOMES: DERIVED; UNDERIVABLE-AND-REPORTED (F-SC1 lapse, honest); or
BLOCKED-BY-ORDERING, since slot 6 sits at position 4 of 9 in the frozen EM order and slots 3-5 are
open. All three are informative. A fourth outcome — condition adopted, response evaluated — voids
the release under F-S6 and the guard returns by default.

RULING AT: `SLOT6_RELEASE_PRINCIPAL_DECISION_2026-07-30.md` (this directory). Not in force in the
governing chain until registered — owed via paste 130, same relay as Q-16.

REOPENS IF: F-S6 fires.

---

## Q-18. "Is the zero stiffness at the record floor a derived spectral fact or a chosen subtraction?"

Also asked as: does the operator fix the floor? Is `K_bare = 0` derived? Can the capacity principle
close slot 9? Is the floor the subtraction?

**RULING: NEITHER. IT IS THE CONTENT OF THE INDUCED-ONLY AXIOM.** Settled 2026-07-30 at the
principal's instruction.

**THE DECISIVE POINT, WHICH IS NEW: the capacity condition and the proper-time floor act on OPPOSITE
ENDS of the same integral.** `lambda_0(D_BR^2) = k_R^2` is a bottom-of-spectrum statement, and the
bottom of the spectrum governs LARGE `s` in `STr' exp(-s L)` — it gives infrared decay
`exp(-s lambda_0)`. The floor `s >= 1/k_R^2` cuts SMALL `s`, which is where the `F^2` logarithm lives.
`exp(-s L)` is well defined and nonvanishing for every `s > 0` regardless of where the spectrum
starts, so **no value of `lambda_0` can empty the small-`s` range.** The step OPERATOR -> FLOOR is a
type mismatch, not an unfinished proof.

**CONSEQUENCE: the operator-floor chain cannot be completed by discharging its own named gaps.** It
names its obstructions at step 1 (complete normalized `L_BR`) and step 2 (lowest eigenvalue for the
complete public operator); closing both still leaves the lower limit unfixed. Its own flag was already
honest: `proper_time_floor_status = ADOPTED_BY_INDUCED_ONLY_FUNCTIONAL`,
`gamma_at_floor_zero = DERIVED_GIVEN_FLOOR`.

BOUNDED NEGATIVE, roots parent tree + supervision, types md/json, exclusions node_modules + `external/`
+ custodian_private: files mentioning a lower endpoint/limit = **12**; files mentioning `lambda_0` =
**16**; files mentioning **BOTH = 0**. The two objects have never appeared in the same file in either
direction. And no artifact anywhere distinguishes the small-`s` from the large-`s` end of this integral.

THE AXIOM SAYS SO ITSELF, and the verb is the evidence —
`alpha_induced_only_boundary_action_principle_v001.md:16-19`: "The lower proper-time boundary is the
first durable record scale; `Gamma_BR,k_R=0` **states** that no separate public stiffness is installed
before the record branch opens." A claim about public field content, adopted, carrying real physical
consequence. Not a spectral consequence and not a subtraction convention.

**WHAT IT SETTLES ABOUT alpha:** its conditionality equals the induced-only axiom's status, exactly and
no more. The attack's own escape clause — a postulate with one free number per predicted coefficient is
a reparametrization "unless the postulate is independently earned by predicting something else first" —
**is slot 18.** So slot 18 is load-bearing for alpha's EPISTEMIC STATUS while remaining irrelevant to
alpha's VALUE. It cannot fix a normalization (Q-13) and it can retire the postulate's freeness; both
hold without tension, and it explains why FINAL-CLAIM was correctly placed on slot 18 rather than alpha.

WHAT DIES: "the geometry closes the additive freedom"; the operator-floor chain as a route to slot 9;
and the reading of F-shift as merely unattempted. WHAT SURVIVES: leg 1 — `Gamma_BR,k_R = 0` given the
floor is exact arithmetic; and the induced-only axiom as a physical proposition rather than a
convention.

FULL WORKING: `RESULT_FLOOR_BOUNDARY_VALUE_SETTLED_2026-07-30.md` (this directory), with F-FL1/2/3
frozen.

**ERRATUM (appended 2026-07-30, append-only): THE BOUNDED NEGATIVE IN THIS ROW IS RETRACTED.** Stated
12 / 16 / BOTH 0 with the claim the two objects "have never appeared in the same file"; correct null-safe
figures are **16 / 19 / BOTH 7**, the seven including the operator-floor chain itself, relay paste 127 and
the 07-29 operator-chain test. Cause: an `xargs` path pipeline split on the spaces in the root paths and
reported zero silently. **THE RULING IS UNAFFECTED — it rests on the opposite-ends mathematics, not on the
count — and the corrected reading makes it sharper: the type mismatch sits inside an actively-cited chain
rather than in unexamined ground.** The second bounded negative (nothing distinguishes the two ends)
stands at 3 files. See `ERRATUM_002_BOUNDED_NEGATIVE_METHOD_DEFECT_2026-07-30.md`.

**REOPENS IF F-FL1 FIRES: exhibit a condition that fixes the SMALL-`s` end of the proper-time
integral.** A bottom-of-spectrum condition cannot; a statement about the domain, the measure, or the
admissible mode content might. That is the one repair worth attempting and it is well posed.

CARRIED FORWARD, NOT SETTLED: `Gamma_K` + `C_record(K)` is a candidate FIFTH exit for F-shift — an
existence/onset condition, none of E1-E4 in kind. But an onset condition fixes the TOTAL `K`, which is
sufficient for alpha's value and NOT sufficient for slot 9 as posed, since it makes the deformation
moot rather than excluded. Whether that is acceptable is a principal question. It counts as an exit only
if the onset condition is itself DERIVED and OVERDETERMINED; an adopted onset condition is the same
defect one level up.

---

## Q-19. "Must we EXCLUDE the finite `c F^2` deformation, or is DETERMINING the total enough?"

Also asked as: is slot 9 the right obligation? Is "moot" acceptable where the slot says "excluded"?
Can we retire slot 9?

**RULING: SLOT 9 IS RETIRED AS POSED AND REPLACED BY TWO OBLIGATIONS.** PRINCIPAL ACT, 2026-07-30.
Slot 9 is not deleted; the count stays eighteen; its content is re-posed.

**S9-A (DETERMINATION).** Determine the TOTAL physical stiffness by a DERIVED and OVERDETERMINED
condition. The split into induced part and counterterm is bookkeeping and need not be separated —
`alpha_micro = 1/(4 pi K_*)` consumes the total.
**S9-B (THE EXIT QUESTION).** State which exit obtains: E1 fixed point, E2 superconvergence, E3
derived-scale boundary condition, E4 integer pairing, a NAMED FIFTH, or NONE. "NONE" is permitted and
informative.

WHY: the attack's own recommendation ("Slot 9 should be retired as posed and replaced by the exit
question"), on the ground that "the question has no solution inside the class it is asked in" — the
condition class is closed under `K -> K + c`. Q-18 removed the last apparent fifth exit. And the
asymmetry is decisive: **"excluded" and "determined" are different demands and only the second is what
alpha needs.** Requiring exclusion of a term that cannot be separately observed, when the observable
consumes only the sum, is a demand on bookkeeping rather than on physics.

PRECEDENT: R-31, the fourth-horn ruling — "R-L2b as written is SUPERSEDED / RE-POSED, NOT SOLVED and NOT
MERELY REFUTED." Same shape, same authority level, append-only.

FIVE GUARDS, and they are the substance: no ADOPTED determining condition (that is the same defect one
level up); no selection by outcome, and Q-16's O-SC1 ordering applies; **"moot" is NOT discharge of the
epistemic obligation** — alpha's conditionality still equals the induced-only axiom's status and earning
it is slot 18's job; no claim that a scale-breaker now reaches the additive freedom (`d c_R/d x = 0`
stands); and S9-B may not be answered with silence.

*** CARRIES AN UNRULED CONSEQUENCE: R-30's FALSIFIER F2. *** The primary-route declaration's F2 fires if
slot 9 "being underivable on this route except by adopted postulate." Q-18 established exactly that, so
**on its face F2 has fired and the primary-route declaration lapses by its own terms.** Two readings:
(a) F2 fires and the BR/EM-GR route loses declared primacy without being refuted; (b) F2 is explicitly
RESTATED against S9-A, in which case it has not fired because S9-A has not been attempted. Reading (b)
is defensible only if made explicitly and recorded. **A declared label may not survive on a
technicality.** Queued as the next principal decision.

RULING AT: `SLOT9_RETIRED_AS_POSED_PRINCIPAL_DECISION_2026-07-30.md`, falsifiers F-S9A/B/C frozen.
Not in force in the governing chain until registered — paste 130.

REOPENS IF: F-S9A fires (S9-A discharged by adoption — then the program carries two postulates where it
carried one), or F-S9C fires (the observable turns out not to consume only the sum, which would reinstate
slot 9's original form).

---

## Q-20. "Is there a declared primary route?"

Also asked as: did F2 fire? Is the BR / EM-GR ratio route still primary? What is the target of record?

**RULING: NO. F2 FIRED AND R-30's PRIMARY-ROUTE DECLARATION LAPSED ON 2026-07-30.** PRINCIPAL ACT. The
program has no declared primary route.

R-30 froze F2 as firing if slot 9 is "underivable on this route except by adopted postulate." Q-18
established precisely that, as a proved negative. The trigger is met, and the declaration lapses by its
own terms — the ruling records the lapse rather than causing it.

**LAPSES:** the primacy label, "target of record" status, its claim on focused lane effort.
**DOES NOT LAPSE:** the route is NOT refuted; its executed coefficient results stand; **slot 2 remains a
required obligation** (its requirement comes from the ledger, and R-30's own scope said it "does not make
slot 2 newly required"); **F1 is untouched, unfired and still live** (the coupled-Hessian P2 branch); and
work on the route is un-privileged, not prohibited.

RE-DECLARATION IS A FRESH DECISION ON EVIDENCE: S9-A must be attempted on the route and S9-B answered for
it. Re-declaring on a restatement of the falsifier rather than on evidence is forbidden.

THE REJECTED READING, recorded so the choice is attackable: F2 could have been restated against S9-A,
on which reading it has not fired. Rejected because of the ORDER the facts arrived in — the retirement of
slot 9 came AFTER the finding that fires F2, so restating now would let a declared label survive because
a retirement moved its referent. **A declared label may not survive on a technicality.** Honor the
falsifier, then re-earn the label.

*** PROCESS FACT: THIS IS THE FIRST FROZEN FALSIFIER IN THE PROGRAM TO FIRE AND BE HONORED. *** Cite it
whenever "are the frozen falsifiers real?" is asked. It is worth more than the label was.

RULING AT: `R30_F2_FIRED_PRIMARY_ROUTE_LAPSED_PRINCIPAL_DECISION_2026-07-30.md`. Not in force in the
governing chain until registered.

REOPENS IF: primacy is re-declared on evidence after S9-A is attempted on the route.

---

## Q-21. "What is the program building, and what does everything else wait on?"

Also asked as: is there a primary route now? What is the sole construction target? Why Gamma_K?

**RULING: `Gamma_K` + `C_record(K)` IS THE SOLE CONSTRUCTION TARGET, CHARTERED 2026-07-30. IT IS
EXPLICITLY NOT A PRIMARY-ROUTE DECLARATION.**

THE OBJECT, from the readiness record's own `next_gate`: "derive one complete target-independent
`Gamma_K` and BR closure operator whose joint stationary problem outputs `Delta_tau(K)` and a scalar
`C_record(K)`", with `C_record(K_*) = 0`, `dC_record/dK != 0`, `K_* > 0`,
`alpha_micro = 1/(4 pi K_*)`.

**FORCED BY FOUR CONVERGENCES REACHED SEPARATELY:** F-scale directly (Q-14); F-scale via slot 6 —
Codex's O-SC1 step zero returned `BLOCKED_BY_ORDERING` behind this exact object, unprompted; slot 1's
closure items 1-2, which require "one target-independent complete source-record-gravity action"; and
S9-A, whose derived overdetermined determination of the total is what a `C_record` root would be.
**AND IT IS THE ROOT OF THE DEPENDENCY GRAPH WITH NOTHING UPSTREAM** — slot 3 is blocked on the
action-form class which IS this object, slots 4-8 sit behind slot 3, slot 6 behind both, and the
readiness record lists its inputs as already available. Everything waits on it; it waits on nothing.

**SCOPE FIRST IS MANDATORY.** Construction does not start until a bounded inventory returns MISSING
SPECIFICATION / HARD PROOF / DERIVABLE NOW, with roots and exclusions stated. Justification: scoping
has paid twice in one day — Departure 2's framing collapsed under it, and O-SC1's step zero produced
this charter.

**NOT A PRIMARY ROUTE, and the distinction is the substance.** R-30 declared primacy on 07-29 and its
F2 fired on 07-30; declaring primacy on an unattempted construction hours later would repeat the error
with a different noun. A construction target says what is being built and what waits on it; a primary
route says which path is privileged and citable. This does the first and refuses the second. Primacy
is re-earned on evidence (Q-20).

**SLOT 18 RUNS IN PARALLEL AND IT IS NOT A HEDGE.** Two live workstreams, not competing: `Gamma_K` for
alpha's VALUE, slot 18 for its STANDING (Q-18). A number without slot 18 is a conditional consequence
of an adopted axiom; slot 18 without a number is still a falsifiable prediction.

CHARTER AT: `GAMMA_K_SOLE_CONSTRUCTION_TARGET_CHARTER_2026-07-30.md`, falsifiers F-GK1..F-GK5 frozen.
F-GK1 is the one to watch: if scoping returns HARD PROOF behind another object, `Gamma_K` is not the
root and the charter's premise is false.

WHAT SUCCESS WOULD DISCHARGE: S9-A; S9-B answered with a named fifth exit; O-SC1 and slot 6 unblocked;
slot 1's closure items 1-2 supplied; and `alpha_micro`. It would NOT make alpha unconditional.

REOPENS IF: any of F-GK1..F-GK5 fires.

---

## Q-22. "What could fix the small-`s` end of the proper-time integral?"

Also asked as: is there a fifth exit? Can the floor be derived after all? What makes the induced
coefficient absolute rather than running?

**RULING: A CONDITION CLASS EXISTS AND IS ALREADY RANKED, AND IT IS BLOCKED BY THE STITCHING RULE.
NOT REFUTED, NOT AVAILABLE. NOT A FIFTH EXIT TODAY.** Settled 2026-07-30; F-FL1 discharged as a
question, not as a repair.

**THE ANSWER IS RANK 1 OF AN EXISTING TABLE.** `alpha_spectral_ncg_absolute_stiffness_research_v001.md:349`
— "Fully finite **total** record-cell triple plus exact normalized determinant/CTP trace ... Finite
matrix determinant gives an absolute cell Hessian once `D[A]`, state, measure, and unit character are
fixed", blocked by "Current carrier is only internally finite; spacetime spectral support, cell density,
and CTP construction are missing." **On a total finite triple there is no small-`s` divergence to cut and
no floor is needed at all.** Its blocking fact is the STITCHING GAP, whose absence is a sealed failure
rule (`ABSOLUTE_STIFFNESS_SELECTOR_ROUTE_LEDGER_V003.md:116-126`: the route fails if "a finite-cell
answer is called physical without a derived stitching or continuum rule").

**THE CANCELLATION CLASS IS DEAD STRUCTURALLY.** A vanishing primed supertrace cannot help: the `F^2`
divergence is LOGARITHMIC, coming from `A_4`, and a log cannot be cancelled by mode counting. A vanishing
`F^2` part of `A_4` would BE superconvergence, which contradicts the program's own nonzero running,
`alpha_step5_zero_bare_compositeness_boundary_v002.md:53`: `lim d K_1D/d ln Q = -1/(6 pi^2)`. This is
rank 2 and E2, blocked twice over.

The other rows close the space: ranks 3-4 buy the small-`s` end by reintroducing a bare action, which
`K_bare = 0` forbids; rank 5 fixes ratios only; rank 6 — the CURRENT carrier — is PASS-RUNNING /
BLOCK-ABSOLUTE because "`A_4` logarithm and finite local `F^2` mutation require subtraction/matching";
rank 7 is kinematics only.

*** THE REFRAMING, AND IT IS THE RESULT: THE PROPER-TIME FLOOR IS THE PRICE OF AN INCOMPLETE CARRIER. ***
Q-18 typed the floor as the induced-only axiom's content; Q-22 sharpens it — **the axiom stands in for a
finiteness property the carrier does not have.** So the floor and the stitching gap are ONE problem seen
from two sides, tracked separately until now. Same shape as `beta` in Q-10.

**CONSEQUENCE FOR THE `Gamma_K` CHARTER, to be stated before construction rather than after:**
`Gamma_K` on the current carrier lands at RANK 6, not rank 1 — it supplies the CTP construction and the
measure, not spacetime finiteness. So a completed `Gamma_K` with a unique simple positive `C_record` root
determines `K_*` **conditionally on the induced-only axiom, not absolutely**; the closure residual is
built from an action carrying the `A_4` log, so `k_R` appears in the equation fixing `K_*`. This does NOT
fire F-GK1 and does not weaken the charter — it is what F-GK3 exists to force into the open.

WHAT WOULD LIFT IT: a derived stitching or continuum rule, which moves the construction from rank 6 to
rank 1 and makes the coefficient absolute. **That object now has two independent consumers** — the floor
(this row) and any finite-cell stiffness route (the 2026-07-27 finding).

RESULT AT: `RESULT_FFL1_SMALL_S_END_2026-07-30.md`.

REOPENS IF: a derived stitching/continuum rule appears, or someone exhibits a small-`s` condition outside
the seven ranked rows. Work on the cancellation class does NOT reopen it.

---

## Q-23. "Is slot 18 well-posed? What does 'unused' mean?"

Also asked as: can we produce the non-alpha prediction? Is the A32 admissibility condition defined?

**RULING: NO — SLOT 18 IS HALF-POSED. "STRUCTURE-SENSITIVE" IS DEFINED; "UNUSED" IS NOT.** Established
2026-07-30 by Codex lane 2's bounded two-root inventory, reviewer-verified.

The obligation (`STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.md:119-139`) says "one **unused**
structure-sensitive prediction." `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:2080-2089` defines
structure-sensitive operationally — "BID and at least one preregistered comparator calibrated to the same
alpha must make distinct predictions" — and offers "be absent as an outcome or target from the complete
historical lineage", but **nothing equates that with "unused" or supplies a machine-testable predicate.**

**CONSEQUENCE FOR Q-18/Q-22:** slot 18 is the mechanism that would EARN the induced-only axiom that
alpha's conditionality equals. **An earning mechanism with an undefined admissibility condition cannot be
relied on to earn anything.** Q-18 and Q-22 assumed slot 18 was well-posed; it is not yet.

Defining it is a PRINCIPAL ACT — a lane choosing the predicate that decides which predictions are
admissible would be selecting the test after seeing the candidate space.

ALSO ESTABLISHED, and each matters: the 355 collected rows are NOT the eligible universe ("Lineage
exclusion is executed later at the eligibility stage… No row was dropped for content"; and "No sealed
HOLDOUT-UNIVERSE-SEAL immutable subject exists"); A32 is "RATIFIED" but "SPEC-SEAL becomes ATTAINABLE,
not attained"; **no concrete same-alpha comparator exists** — the term names a CLASS with no publication,
expression, order or payload found; the eligible set cannot be shown non-empty before predictions exist;
and **`D` is NOT a comparison to a measured central value** — measurement enters only through
uncertainty/covariance, so computing `D` does not breach the no-comparison fences.

NO IMPOSSIBILITY: six typed non-alpha output families exist with their required derivations listed.

RESULT AT: `RESULT_A32_MASKING_AND_UNUSED_UNDEFINED_2026-07-30.md`; lane report
`STAGE8_SLOT18_BOUNDED_SCOPE_INVENTORY_V001.md` (`3a1a9d98…`).

REOPENS/CLOSES IF: the principal defines "unused", or rules that the "absent from the complete historical
lineage" condition IS the definition and records that identification.

---

## Q-24. "Is A32's masking discipline compliant with its own spec?"

Also asked as: is the holdout sound? Was there an independent custodian? Can we trust the commitments?

**RULING: COMPLIANCE IS NOT ESTABLISHED ON TWO SPECIFIC POINTS. THE HOLDOUT IS NOT SHOWN COMPROMISED.**
Established 2026-07-30; the second point is a reviewer finding lane 2 did not name.

Rule 9, `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:2008-2011`, requires an "**independent
custodian**", a 256-bit salt per candidate, "Payload = RFC-8785 JSON of canonical outcome value,
uncertainty, **covariance**, units, source identifier", and "**Custodian attests that no payload was
disclosed.**"

**(a) NO INDEPENDENT CUSTODIAN.** `a32_holdout/collector_v001.py:301-326`: one program, one run, reads
`/dev/urandom` for salts, writes `custodian_private/custodian.jsonl` containing BOTH payload and salt, and
writes the public `commitments.jsonl`. **"Custodian attests that no payload was disclosed" cannot be
satisfied by self-attestation** — an attestation by the party that generated the payloads is not what
rule 9 asks for.

**(b) THE SALT SOURCE IS ARGUABLY COMPLIANT — recorded so nobody later claims otherwise.** Rule 9 permits
"auditable external randomness OR hardware entropy." `/dev/urandom`, 32 bytes, fail-closed on short read,
plausibly satisfies the second disjunct. It leaves no audit trail, so it fails the first. Disjunctive
requirement, so NOT a violation.

**(c) NEW — THE COMMITTED PAYLOAD OMITS COVARIANCE, AND THIS ONE HAS TEETH.** The code commits four
fields (`source_id`, `uncertainty`, `units`, `value`); rule 9 requires five. **Covariance is not bound by
the commitment.** And `V011:2052-2058` defines `D` "after unit conversion and **covariance projection**"
— so an unbound covariance can be supplied AFTER the prediction exists. *** That is a post-hoc freedom
inside the one mechanism whose entire purpose is to remove post-hoc freedom. *** Two innocent readings
exist — all observables scalar, or covariance carried elsewhere — and **neither is recorded.**

**TIME-SENSITIVE, NOT MERELY IMPORTANT: a holdout committed late is VOID, not weaker.** If re-collection
under an independent custodian is required, it must happen BEFORE any prediction exists, and both
construction lanes are now working toward predictions. The same defect found after alpha exists cannot be
repaired at all.

Also recorded: lane 2's structure-only probe detected a numeric-looking candidate-definition suffix and
stopped, reproducing and inferring nothing. Correct behavior, and a second independent reason to inspect
masking.

REOPENS/CLOSES IF: the principal accepts the arrangement with the limitation recorded; or requires
re-collection under an independent custodian; or rules on whether covariance must be committed (which
likely forces re-commitment). An innocent reading of (c), once recorded with evidence, closes (c) alone.

---

## Q-25. "How was A32's masking disposed?" — SUPERSEDES Q-24's OPEN DISPOSITION

**RULING, TWO PARTS. PRINCIPAL ACT, 2026-07-30.**

**CUSTODIAN: THE ARRANGEMENT STANDS, LIMITATION RECORDED PERMANENTLY.** Commitments are not withdrawn and
the holdout is not re-collected. The concealment is cryptographically sound — `SHA256(salt || payload)`,
256-bit salts, fail-closed on short entropy reads — but **process independence between collector and
custodian was never established and no independent attestation exists.** That discount travels with every
A32 headline and is inherited by FINAL-CLAIM. Re-collection was available in this window only and was
declined as disproportionate; the cost is stated so it cannot later be discovered.

**COVARIANCE: CLOSED BY EVIDENCE — VACUOUS BY CONSTRUCTION.** Check run on the collector source only, no
candidate content read: `covar|corr_matrix|correlation` returns **ZERO occurrences** in
`collector_v001.py`, and the parser's fields at `:231-258` are **name | value | uncertainty | units**. The
source format is a fixed-column table with no covariance to commit. **The payload omits covariance because
the universe has none, not because the collector dropped it** — the commitment binds everything the source
supplies. The spec over-specifies relative to this universe; the collector does not under-bind it. No
re-commitment required.

*** FORWARD CONDITION, BINDING: THIS COLLECTOR CANNOT COMMIT A MULTI-COMPONENT OBSERVABLE. *** No
covariance field, no code path for one. If the eligible universe is ever extended to vector or
multi-component observables, the collector must be revised and those candidates re-committed BEFORE any
prediction exists. Live rather than hypothetical, because the universe is not yet sealed ("No sealed
HOLDOUT-UNIVERSE-SEAL immutable subject exists").

RULING AT: `A32_MASKING_DISPOSITION_PRINCIPAL_DECISION_2026-07-30.md`.

REOPENS IF: the eligible universe is extended to covariance-bearing candidates, or an external review
rejects the recorded custodian limitation as insufficient for a published claim.

---

## Q-26. "What energy is conjugate to a causal diamond's proper time?"

Also asked as: how do we settle the sqrt(2)? Misner-Sharp or Brown-York? What fixes the record interval's
energy?

**RULING: NEITHER — AND THE DICHOTOMY IS THE WRONG SHAPE.** Both are BOUNDARY energies, and the gate
rejects both because the diamond "is the support of a CTP history difference, not a material timelike
boundary." **That rejection generalizes: no quasilocal boundary energy can be right for a region with no
boundary.** The `sqrt(2)` is the residue of asking a boundary construction to do a non-boundary job.

**A THIRD CLASS EXISTS AND WAS NEVER CONSIDERED: the diamond's MODULAR HAMILTONIAN** — the generator of
the modular automorphism group of the diamond algebra in the given state. Built from (region, state);
needs no boundary, no boundary conditions, no reference spacetime. No competing member of its class.

NOT A FREE CHOICE — two theorems: for a FREE MASSLESS field the modular flow of a double cone is
GEOMETRIC, the flow of the conformal Killing vector preserving the diamond with the tips as fixed points
(Hislop-Longo); and its normalization is fixed by KMS, not by a subtraction convention. The conversion to
proper time is exact and derived, `tau = R tanh(s/2)` on the central worldline, mapping the full modular
parameter onto the tip-to-tip interval.

**BOUNDED NEGATIVE — modular theory is absent from this program.** Roots parent tree + supervision, types
md/json/py, exclusions node_modules + external/ + custodian_private: modular Hamiltonian 0, modular flow
0, modular automorphism 0, conformal Killing 0, double cone 0, Hislop 0, Casini 0, Bisognano 0,
Wichmann 0, entanglement Hamiltonian 0; Tomita 2 (incidental, GNS), Unruh 1.

GATE'S FIVE CONDITIONS, SCORED: 1 plausible (K generates its own flow); 2 hard, with a named candidate
bridge (the causal-diamond first law relating area variation to `delta<K>`, NOT in this corpus); 3 partial
(relative entropy makes vacuum subtraction intrinsic); **4 FAILS NAIVELY** — the conjugate parameter is
MODULAR time, not proper time, **but with an exact derived conversion rather than an ambiguity**; 5 open.

WHAT IT WOULD BUY: the corpus asserts `|Delta S_record| = E_R T_R` as a product rule; modular theory's
exact statement for a region is the entanglement first law `delta S = delta<K>`, an identity. The relation
the program asserts would become a theorem.

**STATUS: PROPOSAL, PART-PROVABLE, NOT ADOPTED, DOES NOT DISCHARGE SLOT 1.** Four limits attached, the
binding one being that geometric modular flow is a free/conformal result — **whether the sealed
stationary quasifree in-state is in the applicable class must be CHECKED, not assumed.** Also flagged and
deliberately NOT pursued: the modular periodicity is `2 pi` and the corpus marker is `pi hbar`; selection
by numerical resemblance is the numerology fence.

PROPOSAL AT: `PROPOSAL_MODULAR_CONJUGATE_ENERGY_2026-07-30.md`.

REOPENS/CLOSES IF: the in-state check fails (candidate does not reach the applicable stage), or the
gravity bridge is imported by principal act, or a fourth class of conjugate object is named.

---

## Q-27. "What does 'unused' mean in slot 18?"

**RULING: `unused` IS the sealed clause at `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:2080-2089` —
"be absent as an outcome or target from the complete historical lineage" — with "complete historical
lineage" operationalized by the scope V011 rule 11 already defines for the contamination audit (all
accessible repository history, attachments, logs, prompts, tickets, browser-history exports).**
PRINCIPAL ACT, 2026-07-30. Supersedes Q-23's open state.

**THIS IS AN IDENTIFICATION, NOT A DEFINITION.** Both halves are sealed text that was in the corpus
throughout; what was missing was the statement that they are the same condition. The weaker act was the
one available: a lane may not define its own admissibility predicate, and a principal should not invent
one when the clause already exists.

TEST LICENSED: a bounded search over the rule-11 scope returning zero occurrences of the candidate
observable as an outcome or target; roots and exclusions stated, FILE LISTS reported.

F-U1: if the rule-11 scope proves unbounded or unsearchable in practice, the identification fails and
`unused` returns to undefined — report that rather than substituting a narrower scope.
F-U2: the stronger reading (never CONSUMED by the derivation, whether or not it appears in the record) was
considered and NOT adopted. A candidate that passes the lineage test but is later shown to have shaped the
construction is not protected by this ruling and must be escalated.

RULING AT: `SLOT18_ADMISSIBILITY_PRINCIPAL_DECISION_2026-07-30.md`.

REOPENS IF: F-U1 or F-U2 fires.

---

## Q-28. "Can a precision observable be a slot-18 candidate?"

Also asked as: is `D >= 5` meaningful on the electron anomaly? Why did the eligible set collapse?

**RULING: NO — A THIRD ADMISSIBILITY CLAUSE IS ADDED.** PRINCIPAL ACT, 2026-07-30.

> An observable is admissible only if the comparator's own predictive uncertainty is not so far below any
> plausible BID deviation that a `D >= 5` difference would be automatically in conflict with established
> measurement.

**WHY: on the electron magnetic anomaly — the ONLY family with an available comparator payload
(`formula_available_families = 1`) — the test inverts.** QED and experiment agree to ~10 figures, so
`sigma_comp` and `sigma_meas` are minute; any BID prediction differing by more than a whisker gives `D`
far above 5, and any difference that large is already excluded by measurement. **`D >= 5` is therefore
passed by a refuted theory and failed by a correct one.** The apparent escape via a large `sigma_BID` cuts
the other way: a prediction too uncertain to conflict with QED is too uncertain to make the distinctive
claim FINAL-CLAIM requires.

**FENCE POSTURE: it is a condition on comparator PRECISION, never on a measured central value.** `D`
already admits `sigma_meas` into its denominator, so admitting uncertainties into an admissibility test is
the posture the protocol already takes. No measured central value enters.

APPLIED AT THE ELIGIBILITY STAGE, before the beacon selects — not at collection (so no re-collection) and
not after selection (which would be selection-by-outcome).

**EXPECTED IMMEDIATE CONSEQUENCE, stated rather than discovered: applying clause 3 today most likely
leaves ZERO admissible families**, and "an empty eligible set fails closed." That is an honest outcome,
not a defect. The correct response is to look for observables satisfying all three clauses, **not to relax
the third.**

F-C3: if clause 3 cannot be applied without consulting a measured central value, it breaches the
comparison fence and must be WITHDRAWN — report the breach, do not soften the clause to fit.

FINDING AT: `FINDING_D_TEST_DEGENERATE_ON_PRECISION_OBSERVABLES_2026-07-30.md`; ruling at
`SLOT18_ADMISSIBILITY_PRINCIPAL_DECISION_2026-07-30.md`.

REOPENS IF: F-C3 fires, or a formulation is found that preserves the intent without a precision condition.

---

## Q-29. "What exactly is the missing stitching / continuum rule?"

Also asked as: why can't a finite-cell answer be called physical? What blocks the continuum limit? Is
there a stitching principle anywhere?

**RULING: IT IS NOT A MISSING CONTINUUM PRINCIPLE. IT IS TWO NAMED COHERENCE CONDITIONS, AND THE MEASURE
THEY ACT ON IS ALREADY DERIVED AND FORCED.** Established 2026-07-30 by re-typing, not by derivation.

**THE MEASURE IS DONE.** `STAGE8_T7_CODEX_BATTERY_TIER2_RETURNS_V001.md:86-97`, DERIVED:
`<xi,xi>_(2,ell) = sum_(mu<nu) V_cell/(ell_mu^2 ell_nu^2) xi_(mu nu)^2` with
`xi_(mu nu) = ell_mu ell_nu F_(mu nu)`; "each cell contributes `V_cell sum F^2`"; "general coframe =
pullback by `wedge^2(e^-1)` times `|det e|`"; and its own summary — "**NO inverse weight, NO ad hoc
weight, NO residual shape scalar ... the measure is forced, not chosen.**" The per-cell contribution is
already in additive extensive form, and its coframe transformation is already a pullback.

**WHAT IS MISSING IS TWO OBJECTS, NAMED IN THE SAME PLACE:** "the sealed RESPONSE-MAP PULLBACK on common
refinements; and BOUNDARY-SUBEXTENSIVE INVARIANCE over `C_ref`", with
`cellulation_independence_proved = false`. Corroborated at
`STAGE8_CORRECTED_STATUS_MECHANISM_OPTIONS_WITH_COSTS_V001.md:27`.

*** AND ONE OF THE TWO IS ALREADY CHARTERED. *** Boundary-subextensivity IS the extensivity obligation —
`STAGE8_RL2B_OVER_CHARTER_AND_BLIND_ROUTE_FINDING_V001.md:106` states it as "(ii) boundary corrections
subextensive at a certified...", and `STAGE8_RL2B_UNIFORMITY_REFUTED_RESULT_V001.md:161` lists CONNECTED
EXTENSIVITY as the fourth of R-L2b's four obligations. **So the genuinely unattacked half is (i), the
response-map pullback on common refinements.**

**FOUR CONSUMERS FOR ONE PAIR OF CONDITIONS:** Q-22's rank 1 (a total finite triple, which would make the
coefficient absolute and the floor unnecessary); every finite-cell stiffness route (the 07-27 sealed
failure rule); and lane 2's tier-1 slot-18 families, whose stated requirements — "regulator/refinement and
packing independence", "the many-cell limit, long-wavelength locality, frequency convergence, packing
independence" — ARE these two conditions.

WHY THE FRAMING MATTERED: "no derived stitching rule exists" is true and was read as *a continuum
principle is missing*. An obligation described as a missing principle attracts no work; "prove the
response map commutes with refinement" is a stated target with a known shape.

DOES NOT ESTABLISH: that (i) or (ii) is provable. F-2 still forbids pinning the cellulation, and R-L2b
carries a refuted-uniformity result whose bearing on (ii) is not assessed here.

RESULT AT: `RESULT_STITCHING_RULE_DECOMPOSED_2026-07-30.md`.

REOPENS IF: (i) or (ii) is proved or refuted, or a third missing condition is named.

---

## Q-30. "Does the modular-Hamiltonian candidate apply to this construction?" — CLOSES Q-26

**RULING: NO. NOT_APPLICABLE.** Established 2026-07-30 by Codex lane 1 under paste 136
(`STAGE8_MODULAR_CONJUGATE_ENERGY_LIMIT1_APPLICABILITY_RESULT_V001.md`,
`73a5a36c9de72a476fcb5f8dacd1615383c05a6dc4d9407c8e7406265a9fcd94`, `spec_amended = false`).

Q-26's limit 1 was the binding one and it fired: **the free/quasifree state is only the free SUBGATE.**
`Gamma_K` requires the completed **interacting** source-record-gravity CTP object, not the flat free-field
local algebra of a standard double cone. Hislop-Longo's geometric modular flow is a free-field theorem
about the local algebra of a double cone; neither the state nor the algebra at the applicable stage is in
that class.

**WHAT DIES:** the modular Hamiltonian as a candidate for the conjugate energy in this construction; any
use of `tau = R tanh(s/2)` as the record's modular-to-proper-time conversion; and the suggestion that the
`sqrt(2)` dissolves by better typing. No spec amendment was made and none should be.

**WHAT SURVIVES, and it is only the negative half of Q-26:** both Misner-Sharp and Brown-York remain
rejected by the gate's own reasoning, and that rejection still generalizes to every quasilocal BOUNDARY
energy, since the diamond is a CTP history-difference support. **So the conjugate energy remains
unidentified and the candidate class is now one narrower.** Q-26's bounded negative (modular theory absent
from the corpus) also stands as a fact about the corpus.

Section 2.2 of `STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001` is unchanged and correct as written: the required
conjugate energy does not exist yet, and the spec does not choose.

REOPENS ONLY IF: a modular characterization is derived for the interacting completed object rather than
imported from the free case. **Do not reopen it by locating a free subgate and arguing from there** — that
is the move this ruling refuses.

---

## Q-31. "Is the response-map pullback already obstructed by O7?"

Also asked as: does the refinement-intertwiner failure close the finite-cell route class? Is the stitching
rule refuted rather than unproved?

**RULING: NO. DOES_NOT_TRANSFER.** Established 2026-07-30 by Codex lane 1 under paste 139
(`STAGE8_O7_RESPONSE_PULLBACK_TRANSFER_CHECK_V001.md`,
`dcf29eeae27c25ee17c93671acb32336c5e227d97a2280a3fa8668f17610c57d`).

**O7's obstruction is REAL and stays real — but it is typed to ROUTE T's transfer-operator refinement
mechanism, not to T11's response-map pullback.** The refuting witness (`(3/8)^k` vs `3/8`, every refined
cell inserting an `O(1)` record cycle) acts on the transfer operator and record-tier tensor data, not on
the response map. Anchors: majorant spec `:313` and `:378` (O7 as a Route-T/O3 transfer mechanism); proof
draft `:489` and phase result `:27` (what the witness acts on); T11 return `:84` and `V011:1407` (T11's
missing object is response-map pullback + boundary-subextensive invariance).

**AND THE RESCOPE READING IS CONFIRMED AND NARROWED:** `refinement_intertwiner_derived = false (unchanged;
now not required)` means not required for the **Route-Q derived arm**, and it kills **Route T's transport
mechanism only** — `STAGE8_T7_MAJORANT_ARM_RESCOPE_PRINCIPAL_DECISION_V001.md:18` and `:75`. It does NOT
discharge the stitching rule's requirement.

**CONSEQUENCE: THE FINITE-CELL ROUTE CLASS IS NOT CLOSED, AND (i) THE RESPONSE-MAP PULLBACK REMAINS OPEN
— unproved, unattacked, and NOT refuted.** With Q-29's four consumers (Q-22's rank 1, every finite-cell
stiffness route, and lane 2's three tier-1 slot-18 families) it is the highest-leverage single open object
in the program.

METHOD NOTE WORTH KEEPING: this was a pure typing check and it turned on refusing to infer sameness from
the shared word "refinement." Two objects, one word, opposite verdicts. Q-11's match-by-name/fail-by-type
is now the second most-cited discipline in this register after search-before-deriving.

RESULT AT: as above; question posed in `RELAY_PASTE_139_O7_TRANSFER_2026-07-30.md`.

REOPENS IF: a witness is exhibited that acts on the response map itself rather than on the transfer
operator.

---

## Q-32. "Can the response-map pullback (i) be settled from the existing corpus?"

Also asked as: is (i) provable? Is it refutable by an O7-analogue? Why is it stuck?

**RULING: NO — IN EITHER DIRECTION. AND THE REASON IS THE RESULT: (i) IS NOT AN OPEN THEOREM, IT IS AN
UNDEFINED STATEMENT.** Established 2026-07-30 by Codex lane 1 under paste 140
(`STAGE8_RESPONSE_MAP_O7_ANALOGUE_WITNESS_CHECK_V001.md`,
`6f8f0dd3209e3bf10ba6c1e1ab766cdccafc226f507486b216a0d33d2b2cb3ad`). Verdict `UNDETERMINED`.

**THE RESPONSE MAP IS NOT MEASURE-ONLY, so it is NOT insulated by the forced face-measure pullback.** It
consumes amplitude / record-cycle / Duhamel structure: V011 routes response through `H_c/r_c/U_c/A_c/
Gamma_c` (`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:1249`), `G_L(a;tau_R)` and the intensive Hessian
(`:1283`), and the generated face response (`:1348`). **The "inherits the measure's pullback and (i) is
close to immediate" branch is DEAD.**

**BUT THE O7-ANALOGUE WITNESS IS ALSO NOT CONSTRUCTIBLE FROM SEALED TEXT — and the reason is circular in
an informative way.** To turn O7's transfer-operator witness into a RESPONSE witness, **the missing
response-map pullback would have to already define how coarse and refined completed amplitudes, full-`tau_R`
cycles, connected terms and Hessians compare.** *** YOU CANNOT REFUTE THE PULLBACK WITHOUT THE PULLBACK.
The object needed to build the refutation is the object being refuted. ***

The cheap raw-cycle argument is separately blocked by the sealed extensivity record: **"`tau_R` makes the
estimate hard. It does not make extensivity false."**

**THE CONSEQUENCE, AND IT IS ACTIONABLE: (i) NEEDS A DEFINITION BEFORE IT NEEDS A PROOF.** One cannot prove
or refute a commutation until the comparison is defined — what it MEANS for a response on a coarse
cellulation and a response on a refined one to be the same. That definition is the missing object, and its
ingredients exist: the measure's pullback is derived and forced, and V011 routes the response through
named objects.

**SIXTH INSTANCE OF THE DAY'S PATTERN.** The missing object is a CORRESPONDENCE — how two things compare —
not a calculation. See Q-14, Q-22, Q-29, Q-31, and the slot-18 observable bridge.

REOPENS/CLOSES IF: the comparison map is defined, at which point (i) becomes answerable in the ordinary
way and this row is superseded by the answer.

---

## Q-33. "Is the response-map comparison really undefined?" — CORRECTS Q-32's INFERENCE

**RULING: NO. THE COMPARISON IS DEFINED, AND (i) AND (ii) ARE TWO CONDITIONS IN ONE THEOREM'S HYPOTHESIS
LIST.** Found 2026-07-30 in `BID_MONOIDAL_EXTENSIVITY_DERIVATION_V001.md`, Theorem 3, "Connected-cellulation
obligation" — an artifact lane 1 did not consult because paste 140 pointed it at V011's response routing.

**Q-32's LANE FINDINGS STAND**: the response map is not measure-only (V011 routes it through
`H_c/r_c/U_c/A_c/Gamma_c`, `G_L(a;tau_R)`, the intensive Hessian, the generated face response), and the
O7-analogue witness is not constructible from sealed text. **WHAT IS CORRECTED IS MY INFERENCE** that no
comparison exists to make the statement well-posed.

**THE DEFINITION, verbatim from Theorem 3:** "Disjoint additivity alone does not prove a thermodynamic
response on a connected cellulation." The volume-density limit is
`gamma(A) = lim_(K exhausts R^4) -Log|A_K(A)| / N_4(K)`, and "its Hessian is the connected local record
susceptibility." **So "the response map commutes with refinement" means "this limit does not depend on
cellulation" — and Theorem 3 names that failure explicitly: "or the limit depends on cellulation, the
connected response gate fails."**

**FIVE CONDITIONS ARE STATED FOR THE LIMIT TO EXIST:** uniform finite-range/bounded local terms; uniform
preparation clustering; a volume-independent open neighborhood of `A=0` in which `A_K(A)` is nonzero;
uniform absolute convergence of the differentiated connected-cluster sum; **and subextensive boundary
corrections across the sealed refinement class.**

*** THE LAST OF THE FIVE IS (ii). CELLULATION-INDEPENDENCE OF THE LIMIT IS (i). SO THE STITCHING RULE IS
NOT TWO SEPARATE OBJECTS — IT IS THE HYPOTHESIS LIST OF ONE THEOREM, TRACKED AS
`connected_linked_cluster_density_proved = false`. ***

**AND THAT IS THE LINKED-CLUSTER MAJORANT PROGRAM, WHICH IS R-L2b's TERRITORY** — already chartered,
already attacked, and carrying a refuted-uniformity result. **(i) is therefore NOT a fresh unattacked
object.** My description of it as "the one unattacked half" (Q-29) and "the highest-leverage open object"
was wrong twice: it is one hypothesis of a theorem whose proof is an existing campaign.

ALSO ESTABLISHED IN THE SAME ARTIFACT, worth keeping: exact disjoint additivity IS proved
(`exact_disjoint_monoidal_additivity_proved = true`) — `Gamma_K(A) = sum_i Gamma_(K_i)(A_i)` on any
connected logarithm branch containing the unperturbed point. **Additivity over DISJOINT cells is derived;
consistency under SUBDIVISION is what Theorem 3 governs.** Those are different operations and the corpus
distinguishes them correctly.

And Theorem 2 records a rejected route: the V010 normalized global ray gives `kappa_L -> 0`, "incompatible
with a nonzero extensive local stiffness ... No factor of `L^2`, `L^4`, cell count, or volume may be
supplied afterward."

**SEVENTH INSTANCE OF THE DAY'S PATTERN, and the first to correct a same-day register row.**

REOPENS IF: the five conditions are proved or one is refuted, at which point the connected response gate
resolves and this row is superseded by that outcome.

---

## Q-34. "Which stiffness is alpha's — `K_*` or `kappa_record`?"

Also asked as: what does slot 16 transport? Is the extensivity campaign on the value path? Onset or
intensive?

**RULING: `K_*`, THE ONSET ROOT. SLOT 16 IS RE-POSED TO CARRY `K_* -> kappa_Thomson`.** PRINCIPAL ACT,
2026-07-30. Basis: `RESULT_TWO_STIFFNESS_OBJECTS_2026-07-30.md` (`f3eb0c84…`); ruling at
`ALPHA_STIFFNESS_IS_K_STAR_PRINCIPAL_DECISION_2026-07-30.md`.

THE GAP RULED ON: `kappa_record` is an INTENSIVE HESSIAN, a density on the completed chain requiring the
volume-density limit and Theorem 3's five hypotheses. `K_*` is an ONSET ROOT on ONE cell,
`alpha_micro = 1/(4 pi K_*)`. Bounded negative: 20 files carry `K_*`, 263 carry `kappa_record`, **7 carry
both and all seven were created 2026-07-30.** No pre-existing artifact relates them, and the typing freeze
warns that "the two Hessians are generically DIFFERENT physical quantities."

**GROUNDS — THE PROGRAM'S OWN COMMITMENTS.** Couplings are IMPEDANCES OF ACCESS CONDITIONS, `Z_F =
1/kappa_F`, explicitly "not Lagrangian normalizations" — an impedance of an access condition is
threshold-shaped, not a volume density. Allow/require is the central mechanism and `K_*` is it made
quantitative. The record cell is primitive. The stiffness departure (`K_bare = 0` PLUS removal of the
rescaling freedom) makes stiffness physical rather than conventional. **`kappa_record` is the construction
one builds when the coupling IS a Lagrangian normalization — the premise these foundations deny** — and
that route already carries a refutation (V010 ray, `kappa_L -> 0`).

**WHY THE THRESHOLD OBSERVATION MATTERS (the principal's):** a threshold tells you WHEN, not HOW MUCH —
"the threshold rule does not automatically choose the denominator", `status = CELL_CONSTRAINT_ONLY`. The
onset route gets a magnitude by applying the condition to a `K`-INDEXED FAMILY, converting a *when* into a
*which*. **That works only if everything else is fixed independently — which is exactly what `Gamma_K`'s
eleven Section-1 pieces are.** They are the data the threshold cannot supply.

*** THE COST, STATED NOT HIDDEN: SLOT 16 MUST NOW TRANSPORT A CELL QUANTITY TO A CONTINUUM COUPLING. ***
Under the old reading the continuum step was already taken (a density matched to a scale). Under this
ruling it has not been, and slot 16 must take it. The ruling relocates a hard problem; it does not remove
one.

*** OPERATIONAL CONSEQUENCE: THE LINKED-CLUSTER / EXTENSIVITY / R-L2b CAMPAIGN IS NO LONGER ON ALPHA'S
VALUE PATH. *** Not retired, not refuted — it serves `kappa_record`, which keeps its other sealed roles.
But proving Theorem 3's five hypotheses does not produce alpha under this ruling, and that campaign should
not be resumed as value-path work without a further ruling. **`Gamma_K`'s eleven Section-1 pieces are now
the critical path.**

DOES NOT: retire `kappa_record`; claim the two are different; discharge slot 16 or any slot; lift F-GK3
(11 of 11 pieces partially supplied, none complete, root blocked on an undeclared premise); authorize any
computation.

FROZEN: **F-K1** — if a cell quantity is shown untransportable to a continuum coupling without first
constructing a density, this ruling FAILS and `kappa_record` returns. **F-K2** — if completed `Gamma_K`
produces an intensive object, the premise is false. **F-K3** — if re-posed slot 16 needs Theorem 3's
conditions anyway, the routes were never distinct and the ruling bought nothing; say so.

REOPENS IF: any of F-K1/F-K2/F-K3 fires.

---

## Q-35. "Does a dimensionless observable shorten slot 18's bridge?"

Also asked as: is finite holonomy the native family? Can `Z_Q` be the non-alpha prediction?

**RULING: NO, AND THE REASON MATTERS MORE THAN THE ANSWER — THE THEORY'S MOST NATIVE OBSERVABLE IS ALPHA
ITSELF.** Established 2026-07-30 by Codex lane 2 under paste 143
(`STAGE8_SLOT18_Q34_NATIVENESS_AND_HOLONOMY_BRIDGE_RESULT_V001.md`, `8abb4089…`), verdict
MISSING_SPECIFICATION.

**NATIVENESS RANKING under Q-34's lens (onset/access-shaped above density-shaped):** finite global
holonomy -> causal-record durability -> temporal plaquette/kernel. As predicted, and the density-shaped
kernel ranks last.

**THE SHORTCUT IS DEAD. Dimensionlessness removes ZERO of the four required bridge components** — it could
only make unit conversion trivial *after* a common convention is frozen. My hypothesis that a dimensionless
quantity dodges the unit map was wrong.

*** AND THE KILL IS STRUCTURAL, NOT INCIDENTAL: `Z_Q` IS DIMENSIONLESS BECAUSE HISTORICAL TEXT DEFINES IT
AS ALPHA'S RECIPROCAL. *** V011 therefore excludes it as a deterministic re-expression of alpha; it cannot
be the non-alpha slot-18 observable. The separately named `H_CTP` scalar is not sealed as a dimensionless
physical observable and has not been identified with `Z_Q`.

**THE TENSION THIS EXPOSES, and it is worth carrying:** the impedance framing says couplings ARE impedances
of access conditions (`Z_F = 1/kappa_F`). So the access-condition observable of the compact U(1) sector IS
the coupling — necessarily, not accidentally. **The theory's most native, most access-shaped, dimensionless
quantity turns out to be alpha itself.** Slot 18 demands a NON-alpha observable, so it pushes the program
away from exactly the quantity its foundations are best at expressing. That is a structural tension between
what this theory says well and what its terminal claim requires, and nothing in the corpus records it.

**THE NEW `unused` PREDICATE IS ALREADY DOING WORK:** Q-27's identification REFUTES the exact `H_CTP`
identity, because it already occurs as both target and outcome. First candidate excluded by the predicate,
on the day it was defined.

REMAINING FOR THE TOP FAMILY: all four interfaces — public physical observable, canonical A32 candidate,
candidate-compatible published comparator, sealed uncertainties. Admissibility: structure-sensitive NOT
established (no comparator exists); clause 3 not executable without comparator uncertainty.

REOPENS IF: a dimensionless observable is found that is NOT a re-expression of alpha, or `H_CTP` is sealed
as a physical observable distinct from `Z_Q`.

---

## Q-36. "Does the EM/GR surface body supply what `Gamma_K` needs?"

Also asked as: is the coupled gravity-EM surface saddle the same object as `Gamma_K`? What is the
Gravity-EM Surface Unification Theorem? Does the surface body shrink the root adoption?

**RULING: NO. ZERO COMPLETE SECTION-1 PIECES. THE ROOT ADOPTION IS UNCHANGED IN SCOPE.** Established
2026-07-30 by Codex lane 1 under paste 144 (`STAGE8_EM_GR_SURFACE_BODY_SCOPE_FOR_GAMMA_K_V001.md`,
`6b9ee31f…`).

CONTEXT: the body is large and essentially uncited — 490 entries matching
`gravity_electromagnetism|gravity_em|em_surface|surface_unification` over the parent tree (machine count,
2026-07-30), of which the cleanroom cited three, two written the same day.

**IT SUPPLIES USEFUL ADJACENT BR / ACTION-REGISTRATION STRUCTURE AND ZERO COMPLETE `Gamma_K` SECTION-1
PIECES.** The MIXED verdict on the root premise stands exactly as stated: the root is not recoverable as a
completed object, and using the declared subcomponents now would be a NEW ADOPTION.

**`Gamma_BR[g, A_Q, h]` IS A DIFFERENT OBJECT.** Typed as a distinct Boundary-Resolved effective-action
object — not `Gamma_K`, and not currently a sealed specialization of it. **Answered by type, not by name**,
which is the third time today that discipline changed an answer (O7; the two stiffnesses; this).

**THE GRAVITY-EM SURFACE UNIFICATION THEOREM IS LOCATED AND CLASSIFIED: a closed ordinary-branch capstone.**
It joins ordinary EM and gravity access at a record-forming surface. **It does NOT derive the complete
microscopic source-record-gravity CTP functional, nor any of the eleven `Gamma_K` producer objects.**

**THE ORDERING CONVERGENCE IS REAL BUT NARROWER THAN I CLAIMED.** Both the surface saddle and `Gamma_K`
forbid target/root/capacity closure before the target-independent object is derived — **but they are not
the same object-ordering.** My earlier reading, that two formulations had converged on one admissible
order, is corrected: they converge on the PRINCIPLE, not the ordering.

WHAT SURVIVES FROM THE SURFACE PRINCIPLE REGARDLESS: its statement of the forbidden circular construction
`k_R -> Gamma_BR,k_R -> H_phys -> K_pub -> k_R`, and the discipline that "a failed test rejects the branch;
it does not supply a Lagrange multiplier that repairs it." That is the allow/require onset stated
correctly, and it is not in the working set.

CONSEQUENCE: **the root-premise adoption is now a clean decision at its stated size.** Nothing shrinks it,
and the principal rules on the sentence lane 1 extracted.

REOPENS IF: a surface-body object is later sealed as a specialization of a `Gamma_K` producer.

---

## HOW TO USE THIS REGISTER

1. **Before starting any line of work, grep this file for the question**, in the words you would
   naturally use. The rows are phrased as questions for exactly that reason.
2. If your question matches a row, READ THE REOPEN CONDITION before proceeding. Most rows here are
   closed by proof, not by exhaustion.
3. If you settle a new question, ADD A ROW. Phrase the heading as the question, not the answer.
4. Never edit a row. Supersede it with a later row that cites it.

alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
