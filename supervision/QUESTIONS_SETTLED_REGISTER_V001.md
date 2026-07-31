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

## Q-37. "Can construction start? Is adopting the root premise legitimate?"

Also asked as: may declared objects be treated as producers? What separates a good adoption from a bad one?

**RULING: ADOPTED, AS A HYPOTHESIS WITH A FROZEN TEST. CONSTRUCTION MAY START.** PRINCIPAL ACT, 2026-07-30.
The premise, verbatim: *treat the declared source-record-field carrier/domain, gauge-fixed physical
quotient, record-effect family, and invariant spacetime/contour measure as a complete `Gamma_K`-ready
producer, even though the current producer flags for that completion remain false.* Declared in Section 0
per F-GK3.

**THE FRAMING WAS CORRECTED BY THE PRINCIPAL AND THE CORRECTION IS THE RESULT.** I posed it as
adopt-versus-refuse with testing as mitigation. **In science one adopts a hypothesis IN ORDER to test it —
the adoption is what makes the thing falsifiable.** A premise never stated is a premise never refutable. So
the operative question is not "is it proven" but **"is there a live test attached, or will nobody ever
check?"**

*** BY THAT STANDARD THIS ADOPTION AND A6 ARE OPPOSITES, THOUGH THE CORPUS CALLS BOTH "ADOPTED". *** This
one: stated ONCE, COUNTED, and TESTED by a five-channel mutation audit, a uniqueness gate, F-GK2 and F-GK4,
all frozen BEFORE construction. A6, the minimality selector: stated NINE times in nine files, never
counted, never tested — which is exactly why the axiom map called it a number-manufacturing device.

**THE STANDING RULE THIS ESTABLISHES: EVERY ADOPTION CARRIES ITS TEST, OR IS MARKED UNTESTED.** The corpus
treats "adopted" as one category (`K_bare = 0`, `C_R = 1`, mutation exclusion, ER-A) with no distinction
between premises exposed to refutation and premises nobody will check. **That distinction is worth more
than most of the fences.**

**THE LIMIT ON WHAT A PASS MEANS, recorded beside the declaration:** the audit tests STABILITY UNDER
ADMISSIBLE MUTATION, not correctness of the declaration. A declaration wrong but internally consistent —
a carrier that is not the physical carrier yet supports a construction stable across all five channels —
**would pass.** A clean audit licenses "consistent and not mutation-sensitive," never "the declaration was
right."

**THE COST, PAID DELIBERATELY:** a SECOND conditionality at the root. Q-18 fixed alpha's conditionality to
the induced-only axiom's status; this adds another, at the root of the dependency graph, so everything
`Gamma_K` produces inherits it — including `K_*`, alpha's stiffness under Q-34. Slot 18, which would
discharge either, is unreachable (Q-23, Q-35).

FROZEN: **F-RP1** — if the audit passes only because the declared objects are underspecified, so that a
channel cannot be mutated for want of definite content, **the audit is VACUOUS and the adoption bought
nothing.** That outcome is distinct from a pass and must not be recorded as one.

RULING AT: `GAMMA_K_ROOT_PREMISE_ADOPTED_PRINCIPAL_DECISION_2026-07-30.md`.

REOPENS IF: F-RP1 fires, or the audit fails, or F-GK2/F-GK4 fire.

---

## Q-38. "Did the root adoption survive its test?" — F-RP1 FIRED; Q-37 LAPSES

**RULING: NO. F-RP1 FIRED ON THE FIRST CONSTRUCTION TURN. THE ADOPTION LAPSES BY ITS OWN TERMS.**
2026-07-30, one turn after Q-37 was made. Evidence:
`STAGE8_GAMMA_K_ROOT_PRODUCER_ATTEMPT_F_RP1_V001.md` (`81e2aa87…`), lane status R-58.

**WHAT LANE 1 FOUND.** The attempt could not honestly produce the complete source-record-field Hilbert
space and `rho_pre`. **The declared inputs lack definite constructive content for ALL of:** the states;
the inner product; the domain; `rho_pre` as a state on the completed algebra; the quotient/measure formula;
the record-effect family; **and the executable mutation-channel members.**

*** THAT IS A SHARPER FACT THAN "PARTIALLY SUPPLIED", AND IT CHANGES WHAT THE CHARTER IS FACING. ***
"Partially supplied" suggested pieces existed and wanted assembly. **F-RP1 says that at the root there is
nothing to build from** — the declarations are names plus conditions, without constructive content. The
blocker was never a missing permission. **The objects do not exist.**

**AND THE SEVENTH ITEM IS ITS OWN FINDING: "executable mutation-channel members" have no definite content
either.** So the five-channel audit is currently UNEXECUTABLE — its channels have no enumerable members.
That confirms as a blocking fact what the spec review recorded as a documentation gap (Condition 1: the
admitted mutation family is named, not enumerated, in all five channels). **F-RP1's second clause fired
alongside its first.**

**CONSEQUENCE FOR Q-37: the adoption bought nothing and lapses automatically**, exactly as its own
falsifier specifies. This row records the lapse; it does not cause it. Precedent and pattern: R-30's F2,
which fired and was honored this morning (Q-20). **Second frozen falsifier to fire and be honored today.**

**CONSEQUENCE FOR Q-21's CHARTER, and it is the live question now:** `Gamma_K` cannot be constructed from
current material — not "with difficulty", but from nothing at the root. **So the open question is whether
`Gamma_K` is constructible at all, or whether the charter is aimed at an object that would have to be
built from scratch across seven named contentless inputs.** That is not answerable by another adoption,
and it is not lane work to decide.

**WHAT THE METHOD BOUGHT.** The adoption was made explicitly so it could be tested, with the test frozen
before construction. It died in ONE TURN rather than after eleven pieces. **The cost of learning this was a
single lane-turn; the cost of learning it later would have been the entire charter.** That is what the
standing rule established at Q-37 — every adoption carries its test, or is marked untested — is for.

REOPENS IF: constructive content is supplied for the seven named inputs, at which point a fresh adoption
would be a different act with a different test.

---

## Q-39. "Does F-K1 fire? Can an onset quantity be transported to a continuum coupling?"

Also asked as: does Q-34 survive? Is slot 16's machinery density-shaped? Does "threshold-conditioned" mean
onset-conditioned?

**RULING: F-K1 DOES NOT FIRE. Q-34 STANDS. But the transport is UNDETERMINED — not proved possible and not
proved impossible — and Q-34's cost is confirmed as real interface work rather than a rename.** Established
2026-07-30 by Codex lane 2 under paste 145 (`STAGE8_SLOT16_REPOSED_SCOPE_AND_FK1_AUDIT_V001.md`,
`df0d1c74…`), verdict MISSING SPECIFICATION.

**F-K1 REQUIRED a sealed no-go, a `K_*`-applicable density-first requirement, or an executed countermodel.
None was found.** The written finite-cell route IS density-shaped, but nothing establishes that a cell
quantity CANNOT reach a continuum coupling without an intervening density. **So `kappa_record` does not
return and Q-34 survives its first falsifier test.**

**SLOT 16'S MATERIAL IS MORE THAN A NAME AND LESS THAN A MAP.** V011 carries an inline protocol requiring
"decoupling and matching rules" and "the zero-momentum Thomson prescription"; status is "UNDEFINED under
infraparticle branch; **BLOCKED_BY slot 13** otherwise." Historical material supplies conditional sketches
and a non-identifiability result; **no standalone governing slot-16 artifact exists.**

**THE INPUT TYPING IS NOT AGNOSTIC, so Q-34's cost is confirmed.** The concrete carriers are
intensive-response, flux-curvature, or action-normalization shaped. V011: "The primitive record
susceptibility is the intensive Hessian … evaluated after the thermodynamic/linked-cluster limit."
Historical material types its input as "an absolute primitive closed-record action coefficient" and says
plainly "**It is not the physical Thomson-limit coupling.**" Lane 2's own hedge is correct: with no
completed matching function, it would be too strong to say the machinery consumes an intensive input
throughout — **but Q-34 created substantive interface work, not a relabelling.**

*** MY "THRESHOLD-CONDITIONED MIGHT ALREADY BE ONSET-SHAPED" HYPOTHESIS IS REFUTED. *** Sealed text orders
"interacting charged pole or infraparticle threshold" BEFORE "Thomson matching conditioned on the threshold
outcome" — so "threshold-conditioned" means conditioned on **slot 13's threshold outcome**, not onset-shaped.
And "Thomson matching may not presuppose a sharp massive charged pole" still binds. **The re-posing is
therefore forced rather than natural**, which is the opposite of what I hoped and the reason I asked for the
hypothesis to be refuted rather than confirmed loosely.

**ONE HONEST CIRCULARITY TO RECORD:** the closest explicit statement lane 2 could find on the density
question is my own text from `RESULT_TWO_STIFFNESS_OBJECTS_2026-07-30.md` — "nothing in the corpus answers
that." **So the corpus contains nothing on onset-to-continuum transport beyond what was written today**, and
the F-K1 negative rests on absence rather than on an argument.

REOPENS IF: a density-first requirement applicable to `K_*` is exhibited, or slot 13 resolves and unblocks
the matching protocol.

---

## Q-40. "Is `rho_pre` actually unconstructible, or did F-RP1 fire against a withdrawn route?"

Also asked as: didn't we already have the state? Can allow/require construct it? What exactly did the
Galerkin correction withdraw?

**STATUS: OPEN HYPOTHESIS, UNDER TEST — recorded because it may overturn Q-38's reading.** Raised by the
principal 2026-07-30 ("but haven't we constructed it via the allow/require terms?"); relay 148 tests it.

**WHAT THE GALERKIN CORRECTION ACTUALLY WITHDREW.**
`STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001.md`: `continuum_covariance_formula_derived = true`
and `momentum_block_covariance_regression_valid = true` **SURVIVE**; what is `false` is
`genuine_finite_rank_continuum_restriction_constructed` and `parent_state_regulator_restriction_derived`.
The failure is spectral and specific: a nested finite-rank `Q_n` with `[Q_n,h_0]=0`, `Q_n -> I` strongly
"does not exist for the free massless Dirac multiplier", since a finite-dimensional reducing subspace would
require an `L2` eigenvector of a purely continuous spectrum. **That is a fact about an approximation
scheme, not about the state.**

**THE HYPOTHESIS: THE STATE NEEDS NO SUCH FAMILY.** A quasifree state is determined by its covariance, and
this corpus says so twice — `R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md:228` ("the asymptotic
quasifree state is **fixed by** the positive/negative spectral projection") and
`STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_SPEC_V001.md:65` ("the finite quasifree state is the CAR
restriction **determined by** `C_n`"). The continuum covariance `C(p) = (I - h_0/|p|)/2` is derived, and the
machinery is present: GNS in 88 cleanroom files, quasifree in 58, CAR algebra in 10, Bogoliubov in 4.

**AND ALLOW/REQUIRE IS THE OTHER HALF.** The covariance would supply the CONSTRUCTION — algebra,
representation, state. The threshold would supply the SELECTION — `rho_pre` as the state on the pre-record
side. **Neither yields `rho_pre` alone.** The known hazard is that the threshold "does not automatically
choose the denominator; it states the exact condition under which the denominator is required", so it may
CONSTRAIN a state without SELECTING one.

**IF THE HYPOTHESIS HOLDS, Q-38's F-RP1 fired against the SPECIFICATION's declared inputs — which pointed
at the withdrawn finite-rank route — rather than against what the corpus has**, and "no constructive
content" is a verdict about the spec, not about the physics.

**IF IT FAILS**, the step at which it fails is itself the result: the passages may not mean this; the GNS
algebra may not be the completed one; or the threshold may constrain without selecting.

DOES NOT: reinstate Q-37's lapsed adoption; license treating declarations as producers; or discharge
anything. `0 of 11` stands until a producer flag flips.

RESOLVES WHEN: relay 148 returns `ROOT DERIVED` or names the failing step.

---

## Q-41. "Does the GNS/covariance route build the root?" — RESOLVES Q-40, NARROWS Q-38

**RULING: PARTIALLY. THE STATE IS CONSTRUCTIBLE; THE ALGEBRA IT LIVES ON IS NOT THE ONE SECTION 1
REQUIRES.** Established 2026-07-30 by Codex lane 1 under paste 148
(`STAGE8_GAMMA_K_QUASIFREE_ROOT_ROUTE_ATTEMPT_V001.md`, `8980666f…`).

```
SOURCE_QUASIFREE_GNS_DERIVED = true
ROOT_DERIVED                 = false
PRODUCER_FLAG_FLIPPED        = false
FAILURE_STEP                 = STEP_3_DIFFERENT_ALGEBRA
F_RP1_STANDS_NARROWED        = true
```

*** THE HALF THAT WORKED IS A REAL CONSTRUCTION, AND IT IS THE FIRST OF THE DAY. *** The continuum
covariance `C(p) = (I - h_0/|p|)/2` **does** construct a legitimate source-sector quasifree CAR state and
its GNS representation — **without the withdrawn finite-rank Galerkin route.** Q-40's reading of the
Galerkin correction was right: what was withdrawn was an approximation scheme, and the state does not need
it.

**THE HALF THAT FAILED IS NOW PRECISELY TYPED.** That algebra is the **source-sector** algebra. Section 1
requires the **completed source-record-field CTP algebra.** Those are different objects, and the gap
between them is the failure step.

**AND THE THRESHOLD HAZARD MATERIALIZED EXACTLY AS ITS OWN TEXT WARNED: allow/require CONSTRAINS `rho_pre`
but does not SELECT it.** The threshold "does not automatically choose the denominator; it states the exact
condition under which the denominator is required" — so the selection half of the hypothesis fails while
the construction half succeeds.

**WHAT THIS DOES TO Q-38.** F-RP1 stands, NARROWED. It is no longer "seven inputs with no constructive
content." It is: **the source sector is constructible; the completed record-field algebra is not; and the
state within it is constrained but unselected.** That is a materially better diagnosis than this morning's.

*** AND IT GIVES THE PROGRAM'S BOTTLENECK A PRECISE TYPE FOR THE FIRST TIME. *** The "complete microscopic
generator" that four independent lines converged on 2026-07-29 IS the extension from a constructed
source-sector CAR algebra to the completed source-record-field CTP algebra. **That is a well-posed
mathematical question**, not a missing specification — and it is the first time the central obstruction has
had a statable form.

`0 of 11` is UNCHANGED — no producer flag flipped, and the root piece is not complete. But a genuine
sub-construction now exists that did not exist this morning.

REOPENS/CLOSES IF: the source-sector algebra is extended to the completed CTP algebra, or that extension is
shown obstructed.

---

## Q-42. "What type of extension joins the source sector to the record sector?"

**RULING: SEALED TEXT DOES NOT SAY. Obstruction named `FULL_SOURCE_RECORD_FIELD_CTP_EXTENSION_NOT_TYPED`.**
Established 2026-07-30 by Codex lane 1 under paste 150
(`STAGE8_GAMMA_K_COMPLETED_ALGEBRA_EXTENSION_ATTEMPT_V001.md`, `2198524f…`). `0 of 11` does not move.

**WHAT NOW EXISTS, SECTOR BY SECTOR:**
- **SOURCE SECTOR — CONSTRUCTED.** Quasifree CAR state and GNS representation from the derived continuum
  covariance (Q-41), with no finite-rank family.
- **RECORD SECTOR — MECHANISM EXISTS.** The completed public-record algebra **is recoverable as a direct
  limit**, and `CAUSAL_DIRECT_LIMIT_RECORD_PRINCIPLE` supplies that mechanism.
- **THE JOIN — NOT TYPED.** The direct-limit principle supplies the record-sector mechanism **only**. What
  no sealed text states is **how the source sector and the record sector compose into one algebra**, nor
  what the field sector and the CTP branch structure add on top.

*** SO THE PROGRAM'S CENTRAL OBSTRUCTION IS NOT A HARD DERIVATION. IT IS AN UNMADE SPECIFICATION, AND IT IS
ONE RELATION. *** Both sides have construction mechanisms. What is missing is the algebraic relation
between them — tensor product, crossed product, C\*-extension, or something else.

*** AND THAT RELATION IS A PHYSICAL CLAIM, NOT A TECHNICAL CHOICE. *** A **tensor product** says the record
degrees are INDEPENDENT of the source. A **crossed product** says the record is GENERATED BY AN ACTION of
the source. Those are different theories of what a record is. **This program is built on the proposition
that records are made by sources interacting — and it has never written down which algebraic relation
expresses that.**

**TENTH INSTANCE OF THE DAY'S PATTERN, and at the exact centre:** two objects exist and the correspondence
between them does not. See Q-14, Q-22, Q-29, Q-31, Q-33, Q-34, Q-36, Q-41, and the slot-18 observable
bridge.

**WHAT THIS RETIRES:** the description of the central obstruction as "the complete microscopic generator is
missing." It is not missing in the sense of unbuilt pieces. **Two of three sectors have mechanisms; the
composition law has never been specified.**

REOPENS/CLOSES IF: the source-record composition is typed — by derivation from sealed text if one exists,
or by a principal act if it does not.

---

## Q-43. "How do the source and record sectors compose?" — NARROWS Q-42

**RULING: THE BASE COMPOSITION IS TYPED. `CAR(K_Sigma,q)` GRADED-TENSOR `R(C)`.** Established 2026-07-30 by
Codex lane 1 under paste 151 (`STAGE8_GAMMA_K_SOURCE_RECORD_COMPOSITION_TYPING_TESTS_V001.md`,
`1fa7c918…`). **Q-42 is narrowed, not closed.**

**TEST 1, COMMUTATION — SETTLED.** Source and record observables **COMMUTE** at the base level, because the
record factor has trivial fermion grading. **That is a tensor structure, not a crossed product.**

**TEST 4, QUOTIENT VERSUS EXTENSION — SETTLED, AND MY ALTERNATIVE IS WRONG.** The physical outgoing record
in the full parent is a **stable dressed outgoing-record monomorphism**, NOT a quotient of the source
sector. The record is not obtained by coarse-graining the source.

**CROSSED PRODUCT IS NEITHER SPECIFIED NOR FORCED.** My reading — that "records are made by sources" implies
a crossed product — is not supported by the text.

*** TEST 3 SPLIT, AND THE SPLIT IS THE RESULT. *** "Record without source" does not have one answer: **a
carrier / ready state EXISTS before source action; durable public records REQUIRE source, write, and
nonreturn.** So the binary I posed was too coarse. **The carrier is a genuine tensor factor; DURABILITY is
what source action confers.** Logged as OBS-04, because it is the algebraic form of allow/require — the
threshold governs durability, not existence.

**COMPLETED PUBLIC RECORD SECTOR:** the sealed inductive/direct-limit record algebra, as Q-42 found.

**WHAT REMAINS — Q-42 NARROWED TO:** the complete source-record-field **CTP producer**, with physical
quotient, measure, state/effects, and response-facing dynamics. The base composition is no longer the
blocker; the CTP producer is.

**NO PRODUCER FLAG FLIPPED. `0 of 11` unchanged.**

PROCESS NOTE, recorded because it is the second instance today: lane 1's first commit went RED on a literal
relay marker in its own artifact — the same class as the reviewer's wrapped paste cross-reference. The
relay-sequence check is doing its job and the wording was repaired rather than the check weakened.

REOPENS/CLOSES IF: the CTP producer is constructed, or shown obstructed.

---

## Q-44. "Does the finite reversible write carry a coupling strength?"

**RULING: NO — AND THE MULTIPLIER IS EXPLICITLY EXCLUDED, NOT MERELY ABSENT.** Established 2026-07-30 by
Codex lane 1 under paste 152 (`STAGE8_GAMMA_K_FINITE_REVERSIBLE_WRITE_OBS05_TEST_V001.md`, `b4250480…`).
**OBS-05 is refuted as stated.**

The write IS specified: a source-controlled self-adjoint record-incidence generator/evolution,
`B_ch = P_ch tensor B_Q`. **`lambda P_ch tensor B_Q` with `lambda != 1` FAILS THE RETRACTION AXIOM.** So
the write is forced to unit strength.

Active `K` is typed as **a local surrogate for induced connection RESPONSE** in the retarded
action-Hessian/closure-residual problem — **not a write strength.** Thresholded nonreturn is not sealed as
a condition on write strength, and `C_record(K)` is an on-shell closure residual, not write impedance
renamed.

*** THE RESIDUE IS THE RESULT: THE WRITE HAS NO FREEDOM, SO THE COUPLING CANNOT LIVE THERE. *** `lambda = 1`
is compelled rather than conventional. **Alpha must therefore be a property of the RESPONSE to a
unit-normalized write** — which is what `K`'s own typing already said, and which inverts the hypothesis
rather than merely denying it.

WHAT SURVIVES: durability = write + nonreturn + persistence (Q-43, OBS-04), untouched. Only
alpha-as-write-impedance dies.

PROCESS NOTE: lane 1 declined to commit because its lane-status entry would have referenced another lane's
uncommitted work and its fence forbade touching it. **Correct call.** The reviewer had already committed
that work; the fence is now clear.

REOPENS IF: the retraction axiom is itself shown to be a convention rather than a requirement.

---

## Q-45. "How many standing premises carry a real test?"

**RULING: 17 OF 26 BOUNDED VALUE-PATH PREMISE CLASSES ARE UNTESTED. NINE CARRY GENUINE FAILURE-CAPABLE
TESTS, AND NONE IS REPORTED AS PROVED MERELY BECAUSE A TEST EXISTS.** Established 2026-07-30 by Codex lane
2 under paste 149 (`STAGE8_STANDING_PREMISE_TEST_CLASSIFICATION_V001.md`, `e0e618fe…`). **A conservative
lower bound, not an exact corpus-wide count** — `ledger_scope_decision_needed = true`.

**UNTESTED (17):** `C_R = 1`; ER-A; minimal public carrier `d = 4`; relative-budget saturation; the
proper-time floor; primitive spin-1/2 minimality; one-vectorlike-pair minimality; one-complete-`Q_spec`
unity; relative-U(1) bundle/connection; global descent/quasi-free completeness; the SU(5) parent; sector
independence; the residual ordinary-branch package; complex-vs-real selection; DCC; `tau_orth = T_R`;
zero-flux/no-write.

**TESTED (9):** `K_bare = 0`; transport-only; P1/P2 pre-record premises; Parent-State Covariance; Causal
Incidence Support; the chiral spectral-semigroup rule; the source-record odd-component identity; the
exhaustive-use clause; first-record capacity.

**[CORRECTED BY Q-58: "only absolute-scale selector" is right, but this entry's later wording blurs
"unselected absolute scale" with "unselected unit value." There is exactly ONE of the first and more
than one of the second. A falsifier is also designable — see paste 154.]**

*** `C_R = 1` IS THE MOST CONSEQUENTIAL UNTESTED PREMISE, AND IT HAS NO FROZEN PHYSICAL FALSIFIER AT ALL.
*** Its proposed forcedness audit is explicitly "NOT YET AUDITED." It is the ONLY absolute-scale selector
(Q-07), it is in content a marginal self-gravitation condition, and it reaches the producer as a function
argument with `physical_premise_proved_by_script = false`.

`K_bare = 0` and transport-only are both **TESTED—PENDING**: the first fails if the completed specification
permits an arbitrary finite deformation, with slot 18 as its separate earning route; the second fails if an
additional primitive response coefficient or independent magnitude is required, and the theorem-exclusion
flags remain false. **Neither has passed.** ER-A's kill-test is blocked on control design and its possible
derived write-rate test is explicitly unopened. The corrected A6 sites — five pure selector sites plus one
mixed pair-count component — are UNTESTED, **while the physical allow/require constraint is separately
TESTED/EXECUTED and is NOT the selector**, which is the split correction holding up under audit.

**WHY THIS COUNT MATTERS:** it is the honest measure of what a computed alpha would be conditional on, and
until Q-37 established that every adoption carries its test or is marked untested, the corpus had no way to
state it — "adopted" was one undifferentiated category. **The rule was established this morning and found
seventeen untested premises the same afternoon.**

*** ONE ENTRY IS STALE, AND IT IS CHECKABLE. *** The classification lists **the proper-time floor as
UNTESTED** and **`K_bare = 0` as TESTED**. But Q-18 established that **the floor boundary value IS THE
CONTENT of the induced-only axiom** — and `K_bare = 0` IS that axiom. They cannot carry different test
statuses while being the same premise. Either they are one class, or the classification must say what
distinguishes them. **Flagged for the successor pass, not corrected here.**

REOPENS IF: `ledger_scope_decision_needed` is resolved and an exact count replaces the lower bound, or any
UNTESTED premise acquires a frozen falsifier.

---

## Q-46. "What blocks acting on the premise classification?"

**RULING: THREE CONSTRAINTS. ONE IS TECHNICAL AND DEFEATS THE OBVIOUS NEXT TASK; TWO ARE PRINCIPAL
DECISIONS THAT ARE STILL OPEN.** Established 2026-07-30 from
`STAGE8_STANDING_PREMISE_TEST_CLASSIFICATION_V001.md` (`e0e618fe…`).

**(1) THE DEPARTURE-2 FORCEDNESS AUDIT IS NOT A TEST OF `C_R = 1`.** `:306-308` states it directly: it
"would test forcedness and uniqueness. **It is not a physical falsifier of the marginality condition**"
and has not been frozen or executed as this premise's Q-37 test. **Running it leaves `C_R = 1` UNTESTED
whatever it returns.** The producer cannot substitute: it takes the compactness threshold as an INPUT
(`scripts/derive_bid_minimal_public_causal_cell_v001.py:19-23`) and reports
`physical_premise_proved_by_script: false` twice. *** THE REVIEWER PROPOSED THIS AUDIT AS THE FIX AND WAS
WRONG; THE PRINCIPAL'S QUESTION CAUGHT IT. *** The real task is whether a falsifier of marginal
self-gravitation can be DESIGNED at all — and if none can, the only absolute-scale selector in the program
is permanently untestable, which is a structural limit worth stating explicitly rather than by default.

**(2) `ledger_scope_decision_needed = true` IS A PRINCIPAL DECISION, NOT LANE 2'S.** `:17-30`. Lane 2
adopted a counting convention — one class per status-and-test equivalent premise, clauses of differing
epistemic status split, mirrors and downstream consequences not recounted — and flagged that the convention
is unratified. **Every premise count stays provisional until the principal ratifies or replaces it.**
Nothing here is provable; it is definitional.

**(3) THE Q-45 STALENESS FLAG IS PARTLY WITHDRAWN — THE CAUSE IS THE FENCE, NOT STALENESS.** `:796-799`:
the CAR-named historical floor/mass source "was excluded from direct reading under the lane fence," so the
floor's status reaches lane 2 only through the sealed split correction, a secondary axiom-map quotation,
and V011's competitor classification. **Lane 2 never read the primary text.** The floor/`K_bare`
discrepancy may therefore be fence-induced rather than a failure to track Q-18, and **it cannot be repaired
until the fence's release condition is written** — the standing defect that fences ban entry while their
release conditions were never authored.

REOPENS IF: the counting convention is ratified, the fence release condition is written, or a physical
falsifier for marginal self-gravitation is designed.

---

## Q-47. "Does non-return consume charged-sector content?"

**RULING: NO. NON-RETURN IS GENERIC. OBS-06 IS SUGGESTIVE, NOT STRUCTURAL.** Established 2026-07-30 by
Codex lane 1 under paste 153 (`STAGE8_GAMMA_K_NONRETURN_CHARGED_SPECTRUM_OBS06_TEST_V001.md`,
`2f99c574…`, archive `d98ff6d`, gate GREEN).

Non-return is derived from the stated source-record Hamiltonian's **non-flat absolutely continuous spectral
bands** via coarea, an `L1` spectral density, and Riemann-Lebesgue. **The proof consumes no charged-sector
content whatever** — no species, no charge assignments, no thresholds, no particle masses, no induced-loop
carrier inventory. **Durability and the induced response do not share a sealed cause at the present corpus
state.**

*** THIS IS THE OUTCOME THE REVIEWER PREREGISTERED AS EXPECTED, AND SEALED BEFORE THE ANSWER ARRIVED. ***
`THEORY_CANDIDATE_001_...V001.md` sections 4 and 4A, sealed at `aedd0b3`, predicted generic non-return on
the grounds that Riemann-Lebesgue is a theorem about measures. **The prediction and its expected failure
were both on the record before the test returned.**

*** AND THE TEST FOUND SOMETHING THE QUESTION DID NOT ASK FOR. *** The induced-response side is not merely
unproven-identical to the non-return spectrum — **the object does not exist.** The response route "is
still missing the operator and kernel"; what is needed is a future complete BR/CTP fluctuation/response
operator, an exact induced kernel, and a covariant local projector. **The corpus derives no theorem
identifying the response spectrum with the non-return spectral measure, and could not, because one side is
unbuilt.**

**CONSEQUENCE:** theory candidate 001's surviving half names an UNBUILT object. It must be checked against
the standing `Gamma_K` construction charter — `K` is typed as a local surrogate for induced connection
response (Q-44), so the response operator and `Gamma_K` may be one object under two names. **That check is
open**, and the program's most repeated failure is exactly this shape.

**NUMBERING:** lane 1's commit message labels this Q-46; that number was already taken by the constraints
ruling. **It is Q-47 here, and the register is authoritative.**

---

## Q-48. "Ledger scope and the CAR-source fence."

**RULING: BOTH RESOLVED BY PRINCIPAL ACT.** 2026-07-30,
`LEDGER_SCOPE_AND_CAR_FENCE_RELEASE_DECISION_2026-07-30_V001.md`.

**(1) LANE 2'S COUNTING CONVENTION IS RATIFIED AS-IS.** `ledger_scope_decision_needed = false`. One class
per status-and-test-equivalent premise; differing epistemic status splits; mirrors and downstream
consequences not recounted. **Rationale: Q-37 made "can this independently fail?" the question, and the
ratified unit counts exactly that.** *** THE COUNT REMAINS A LOWER BOUND AND MUST ALWAYS BE REPORTED AS
ONE — ratifying the unit does not certify the enumeration exhaustive.*** 17 of 26 (Q-45) is now a ratified
lower bound rather than a provisional one.

**(2) THE CAR-NAMED HISTORICAL FLOOR/MASS SOURCE IS RELEASED READ-ONLY.** `CAR_SOURCE_READ = PERMITTED`,
`CAR_SOURCE_CITE = PERMITTED`, `CAR_SOURCE_IMPORT_INTO_CONSTRUCTION = FORBIDDEN`,
`CAR_SOURCE_USE_AS_PREMISE_OR_LICENCE = FORBIDDEN`. **Rationale: the fences ban ENTRY, not comparison.
Reading a historical artifact to establish what status it records imports nothing and licenses nothing.**
*** THE DEFECT BEING CORRECTED IS THAT THE FENCE WAS ERECTED WITH NO WRITTEN RELEASE, so a lane could
neither use the source nor establish it was not needed. A fence with no release condition is not a
safeguard; it is an unfalsifiable exclusion.***

**TESTS ATTACHED.** (1) is definitional and fails if a premise is found that the unit cannot classify —
one sharing status and test with another yet able to fail independently. (2) fails if any artifact is found
in which CAR-source content entered a construction, premise or licence rather than a citation; **auditable
by grep, and to be audited at the next register sweep.**

**UNBLOCKS NOTHING ON THE VALUE PATH.** `C_R = 1` remains untested and without a falsifier; `0 of 18`
unmoved.

---

## Q-49. "Are the proper-time floor and `K_bare = 0` one premise or two?"

**REVIEWER RULING, PREREGISTERED BEFORE LANE 2 REPORTS: TWO. THE Q-45 STALENESS FLAG WAS WRONG ON THE
MERITS, AND Q-46's PARTIAL WITHDRAWAL GAVE THE WRONG REASON.** Established 2026-07-30 from rows 2 and 7 of
`STAGE8_STANDING_PREMISE_TEST_CLASSIFICATION_V001.md:230,235`.

**THE TWO ROWS ARE DIFFERENT PROPOSITIONS.**

- Row 2, `K_bare = 0`, induced-only: an adopted compositeness condition with a **frozen falsifier** — the
  route fails if the completed specification admits an arbitrary finite deformation. **TESTED — PENDING.**
- Row 7, the proper-time floor: the premise is **`tau = 1`, the UNIT VALUE**, not the existence of a floor.
  Its recorded status is `proper_time_floor_status = ADOPTED_BY_INDUCED_ONLY_FUNCTIONAL`, and V011
  `:1094-1105` **admits the complete positive-`tau` competitor family**, saying neither the unit interval
  nor the unit amplitude power follows. **No test selects the unit member. UNTESTED — COMPETITOR OPEN.**

*** Q-18 IDENTIFIED THE FLOOR'S SOURCE, NOT ITS VALUE. *** "The floor boundary value is the content of the
induced-only axiom" says the floor is set BY that functional — which row 7's own status string states
verbatim. **It does not say the value is 1.** The axiom can hold with any member of the positive-`tau`
family. **So the two rows can carry different test statuses without contradiction, and lane 2 was right.**

**THE REVIEWER'S ERROR, PLAINLY:** I read "same content" as "same premise" and flagged a conflict that is
not there. Q-46 then withdrew the flag on the theory that the lane fence caused it; **the fence is not the
cause. The cause is that source and value are different claims.** The fence release (Q-48) stands on its
own merits and is not retracted — a fence with no written release is a defect regardless.

*** AND THIS SURFACES SOMETHING THE FLAG WAS OBSCURING. *** `tau = 1` is a **unit-value adoption with an
open competitor family**, and V011 explicitly denies that the unit interval follows. Q-45 named `C_R = 1`
as "the only absolute-scale selector." **Whether `tau = 1` is a second scale-carrying unit adoption is now
an open question** and is not answered here. If it is, the program has two unselected unit values on the
value path, not one.

**PREREGISTRATION:** this ruling is written before lane 2 returns item 2 of paste 154. **If lane 2 rules
ONE premise, this reviewer ruling is wrong and lane 2's finding governs.**

REOPENS IF: lane 2's primary-text reading of the CAR-named source contradicts row 7's status string, or a
test selecting the unit `tau` member is found.

---

## Q-50. "Is the response operator actually missing?"

**REVIEWER OBSERVATION, PREREGISTERED BEFORE LANE 1 RETURNS PASTE 155: A FINITE OPERATOR RESPONSE BUNDLE
IS DERIVED AND HOSTILE-VERIFIED. WHAT IS MISSING MAY BE THE SCALARIZATION, NOT THE OPERATOR.** Found
2026-07-30 during the Q-48 fence audit.

`STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_RESULT_V001.md` (2026-07-25) reports:

```text
FINITE_PRIMITIVE_OPERATOR_RESPONSE_BUNDLE_DERIVED
INDEPENDENT_PRIMITIVE_OPERATOR_RESPONSE_CONFIRMED
finite_primitive_operator_response_bundle_derived = true
finite_primitive_operator_Duhamel_tangent_derived  = true
primitive_source_scalarization_derived             = false
```

**Two hostile post-execution reviews returned `POST_EXECUTION_CONFIRMED`.** The finite primitive parent
produces a Stinespring/PVM operator-response bundle and a finite operator Duhamel tangent. **"It does not
produce a canonical primitive source scalar."**

*** THEORY CANDIDATE 001 SAYS ALPHA IS THE IMPEDANCE OF THE INDUCED RESPONSE. AN IMPEDANCE IS A SCALAR. ***
So the theory's target is precisely the object carrying `primitive_source_scalarization_derived = false` —
and the Route-2 spec names the same gap independently as
`actual_finite_parent_operator_to_scalar_bridge_derived = false`
(`STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md:508`). **Two artifacts, written
five days ago, carry an explicit sealed flag for exactly the object theory 001 requires: the
operator-to-scalar bridge.**

**WHAT THIS DOES NOT ESTABLISH, AND I AM NOT CLAIMING IT.** Lane 1's required object is the **complete
BR/CTP** fluctuation/response operator; the derived one is the **finite primitive** bundle. Finite is not
complete and primitive is not BR/CTP, **so lane 1 may be entirely correct that the complete object is
absent while a finite one is derived.** I have not typed the relation between them and must not. **That
typing is lane 1's item under paste 155 and this observation does not preempt it.**

**BUT IT SHARPENS THE QUESTION.** Paste 155 asks whether the response operator is `Gamma_K` under another
name. **The prior question is whether the missing object is the operator AT ALL, rather than the map from
an already-derived operator bundle to a scalar.** If it is the bridge, the program has been describing a
scalarization gap as an operator gap.

**CANDIDATE CORRESPONDENCE, UNCHECKED:** the standing finding that the geometric route is blocked on the
internal/external metric conversion of a record cell. **A conversion and an operator-to-scalar bridge are
both maps out of a structure into a number.** Whether they are one object is not established here and
should not be assumed.

REOPENS IF: lane 1 types the finite-primitive and complete-BR/CTP objects as the same family, or the
scalarization gap and the metric conversion are shown to be one object.

---

## Q-51. "Is the response operator `Gamma_K` under another name?"

*** RULING: NO, AND NOT DISJOINT EITHER — THE RESPONSE LAYER IS AN UPSTREAM/INTERNAL PREREQUISITE OF
`Gamma_K`. THE SOLE CHARTERED CONSTRUCTION TARGET CANNOT HONESTLY BE STARTED. *** Established 2026-07-30 by
Codex lane 1 under paste 155 (`STAGE8_GAMMA_K_RESPONSE_OPERATOR_CORRESPONDENCE_DETERMINATION_V001.md`,
`a2c2e1cf…`, archive `06658c2`, pre-commit gate GREEN).

```text
correspondence_verdict = UPSTREAM_INTERNAL_PREREQUISITE
raw_correlator_to_retarded_Hessian_map_derived = false
```

**FOUR OBJECTS SIT UPSTREAM OF `Gamma_K` / `C_record(K)`:** the complete BR/CTP fluctuation-response
operator; the exact induced kernel; **the raw-correlator-to-retarded-Hessian map `G -> H_R[G]`**; and the
covariant local projector. `Gamma_K` remains the umbrella target, **but scalar response and root execution
cannot start until that response-extraction layer is specified and derived.**

*** THIS IS THE MOST SERIOUS STATUS CHANGE OF THE DAY, AND IT IS NOT A SETBACK — IT IS A CORRECTION. ***
The program has reported `0 of 11` and `0 of 18` for weeks on the understanding that one chartered target
was being built. **The charter names `Gamma_K` as the target while `Gamma_K` presupposes a layer nobody
specified.** So the correct status is not "the target is unfinished" but **"the target cannot be started,"**
and the charter is incomplete as a statement of what remains. **Paste 155 asked for exactly this and named
UPSTREAM as the outcome to lead with; it is what returned.**

**RELATION TO Q-50.** Compatible, and Q-50's caution was correct. Q-50 found the **finite primitive**
operator response bundle derived and hostile-verified, with `primitive_source_scalarization_derived =
false`; it explicitly declined to type that object as lane 1's **complete BR/CTP** one. Lane 1 confirms the
complete layer is unspecified. **And lane 1 names the extraction map directly — `raw_correlator_to_
retarded_Hessian_map` — which is the object Q-50 predicted from the theory side, since an impedance is a
scalar and the gap is the map out of an operator structure into a number.** Two independent routes, from
opposite directions, on the same missing map in the same afternoon.

**NUMBERING — SECOND COLLISION TODAY.** Lane 1's commit message reads "Q-50"; that number was taken by the
scalarization observation, as lane 1's own commit note anticipated when it declined to touch the
concurrent register. **Registered here as Q-51. LANES MUST STOP ASSIGNING Q-NUMBERS** — the register is
assigned by the reviewer only, and lane commits should cite the paste number instead.

REOPENS IF: the response-extraction layer is specified, or `Gamma_K`'s charter is amended to include it.

---

## Q-52. "May a constraint prevent a test?"

*** RULING: NO. NO CONSTRAINT IN THIS PROGRAM MAY PREVENT A NEW THEORY OR A NEW PHYSICAL PROPERTY FROM
BEING TESTED. WHERE A GOVERNANCE CONSTRAINT AND A TEST CONFLICT, THE CONSTRAINT YIELDS. *** Principal act,
2026-07-30, `TESTABILITY_PRECEDES_CHARTER_SCOPE_DECISION_2026-07-30_V001.md`. **Program-wide; supersedes
charter scope where they conflict.**

**THE DISTINGUISHING QUESTION: does the constraint stop us from CLAIMING something unearned, or from
FINDING OUT whether something is true?** The first stands; the second falls. Constraints against
fabrication — no computed alpha or kappa as a claim, no comparison to measurement, refutations reported and
never repaired, the holdout untouched, seal-before-execution, F-GK3 disclosure, Q-37 — **all stand
unchanged.**

**WHAT FALLS:** a charter naming one "sole construction target" that thereby forbids specifying anything
else; any fence without a written release condition; any rule under which a missing object cannot be
specified because specifying it is out of scope; any reading of F-GK3 that treats declaring a premise as
forbidden rather than required.

**IMMEDIATE CONSEQUENCES.** (a) **The `Gamma_K` charter is amended; `Gamma_K` is no longer the sole
construction target, and the response-extraction layer of Q-51 is an authorized target in its own right.**
(b) **The reviewer's standing instruction not to supply what is absent is WITHDRAWN where the purpose is a
test** — a lane may write a specification if it is declared, marked `derived = false`, and never reported
as derived. (c) Theory candidates and observations are testable objects and may be given lane time without
first being fitted into a framework that never envisioned this work. (d) **A premise may be varied to test
it; considering `C_R != 1` or the competitor `tau` family is not adopting it.**

**WHY IT WAS NEEDED.** Eleven rulings today (Q-41…Q-51) and **not one construction**, because Q-51
established the sole chartered target cannot be started. **With nothing buildable, every lane task was
audit work, and audit work against a moving register produced three stale artifacts in one day.** The
reviewer had been filling lanes rather than reporting that the program had no startable target. **The
constraint, not the physics, was the blocker.**

**GUARD — "PERMITS TESTING" MUST NOT DECAY INTO "PERMITS ASSUMING."** Q-37 stands; a check that cannot
return evidence against what it checks is not a test; anything specified in order to be tested is
`derived = false` until a test passes. **This decision fails if any artifact reports as DERIVED an object
specified in order to be tested. Grep-auditable, on the next sweep with the Q-48 fence audit.**

**AUTHORIZES NO CLAIM. `0 of 18` and `0 of 11` unmoved. Retracts no refutation** — OBS-05, OBS-06 as
structural, and theory 001's section 4 stay killed.

---

## Q-53. "Is theory candidate 001's insertion-point enumeration complete?"

*** RULING: NO — NOT AS A COUNT. THE THEORY IS NOT KILLED; IT IS CUT DOWN. *** Established 2026-07-30 by
Einstein under paste 156 (`STAGE8_THEORY_CANDIDATE_001_ENUMERATION_AUDIT_EINSTEIN_V001.md`, seal
`e3cb4a4d…`; sealed on disk, commit pending the baseline reseal).

**THE CHAIN HAS ~12 STAGES, NOT FOUR.** Blind reconstruction with the candidate withheld, 30 citations
verified. **"Exactly four points" occurs in no artifact but the candidate.** But most uncovered
parameter-capable stages ARE closed — **by rulings the candidate never cited**: QR3 kills the arbitrary
record Gram; the intrinsic measure is unique with the `1 + a·u_D` family killed at `a = 0`; `tau_R` is
derived and is "a check rather than a normalization premise"; the sector projector is the unique
functional-calculus projector. **Verdict: under-argued in its own favour on seven stages, over-claimed on
one word.**

*** THE LIVE FINDING IS S8 — THE PHYSICAL WRITE-TAIL JOIN. *** Covered by no closure and closed by no
other ruling. `physical_write_tail_join_derived = false | TYPE-U`; exactness holds only "for fixed
integrated action" — **a magnitude** — with `exchange_magnitude_derived = false | TYPE-U`. **An underived
magnitude at a stage the enumeration never mentioned, and by the candidate's own standard it is
missing-not-forbidden — the exact weakness the candidate assigned to its own weakest closure.** Recorded
as OBS-07.

**THREE FURTHER CORRECTIONS.** (1) **Closures (1) and (2) are BASE-LEVEL ONLY** — the dressed record copy
does not generally commute with the source, and the candidate's wording dropped the qualifier. (2)
**Closure (2) is three claims under one number**: monomorphism proved; base-level no-crossed-product
proved but with its crossed-exclusion leg derivative of closure (1); full-parent level an unfilled gap.
Grade: **"cannot at the base level; has-not-yet above it."** (3) **Closure (4) carries an unstated
conditionality** — Q-49's `tau = 1` unit-value adoption sits at the precise evaluation point of the
positive half.

*** THE POSITIVE HALF IS NOT ENTAILED. *** "Alpha IS the impedance" is **an import from the adopted
K-route, not a conclusion**, its referent is unbuilt (Q-47), and the "same object under two names" escape
is sealed shut by Q-51. **The conjunction licenses the NEGATIVE half only.** Section 1's conditional
sentence stands; the categorical display text does not.

**THE AUDIT WORKED AS DESIGNED.** The candidate's own section 5 named this as its most likely failure
mode, and Einstein reports that prediction "realized in the bounded sense." **An independent reviewer found
what the author could not, which is why it was not given to the author.**

---

## Q-54. "How do we stop chasing negatives that are artifacts of constraints?"

**RULING: ADOPTED — THE NEGATIVE RESULT TYPING PROTOCOL, WITH GATE ENFORCEMENT.** Principal direction
2026-07-30; `NEGATIVE_RESULT_TYPING_PROTOCOL_V001.md`.

**The principal:** *"We need to be able to test and not inject artificial failure cases that are not
necessarily applicable."*

*** THE CORPUS REPORTED FOUR DIFFERENT CLAIMS IN ONE VOCABULARY. *** **TYPE-R refuted** (the only type
that is physical content) | **TYPE-U unbuilt** | **TYPE-S scope-empty** (must carry roots, exclusions,
fences in force, query) | **TYPE-C constraint-blocked** (under Q-52 a governance defect, not a result).
**Only TYPE-R may be cited as physical content or used to kill a theory or observation.**

**IT COST US THREE TIMES TODAY.** Lane 1's "the response operator does not exist" was bounded-roots TYPE-S,
and **90 minutes later a derived, hostile-verified operator bundle turned up** (Q-50) — a theory was being
built on it. The floor's secondhand status was TYPE-C and **the reviewer filed a staleness defect that did
not exist** (Q-45→Q-49). `C_R = 1`'s "no falsifier is frozen" was bookkeeping, **one inference from being
reported as untestable**, and lane 2 then showed a falsifier is designable.

**FOUR MECHANISMS, ALL IMPLEMENTED.** (1) A typed flag format. (2) A paste-header requirement, effective
from the 157th relay, needing no code. (3) **A new `untyped_negative` gate check, growth-gated at
baseline 3309** so existing flags are not retro-fixed but nothing new enters untyped; terminal fence
declarations exempt. (4) **`NO_VERDICT` is now a legal lane outcome** — a test whose failure condition
rests on untested, inapplicable or unbuilt premises returns NO_VERDICT, not a failure.

**AND A NEGATIVE NOW CARRIES THE SAME EVIDENTIARY BURDEN AS A POSITIVE.** Reporting "not found" requires
stating the search. **The old asymmetry made absence the cheapest legitimate action, which is exactly why
Einstein found the theory candidate under-argued in its own favour on seven stages.**

---

## Q-55. "Is the S8 exchange magnitude free?"

**RULING: NO — BUT IT IS CLOSED BY AN UNTESTED PREMISE, NOT BY PHYSICS. VERDICT ON THEORY 001:
`NO_VERDICT_AS_PHYSICAL_REFUTATION`.** Established 2026-07-30 by Codex lane 1 under paste 157
(`STAGE8_S8_WRITE_TAIL_JOIN_SPEC_AND_TEST_V001.md`, `eb92e8ab…`, archive `f7a3e90`, gate GREEN).

S8 is the R3.4 transported write/tail candidate, `H(t) = H_0 + sum_c v_c(t) U_0(t) B_c U_0(t)*`. **Exactness
enters only after `A_c = integral v_c(t) dt` is fixed**, and the diagnostic transported candidate **does
expose a free integrated-action parameter.**

*** WHAT FIXES IT IS ER-A, AND ER-A IS UNTESTED. *** The current ordinary-parent branch sets
`integral_cell_time v_c(t) dt = tau_R` as **disclosed branch data, not a derived S8 theorem. Without ER-A,
covariance leaves `A_c` external.** Lane 1 typed this exactly right:

```text
exchange_magnitude_free_in_current_ER_A_branch = false | TYPE-C
    | constraint: disclosed ER-A amplitude clause
    | release: derived alternate parent branch or supersession of ER-A
theory_001_negative_half_refuted_by_S8 = NO_VERDICT
```

**SO THEORY 001's NEGATIVE HALF SURVIVES S8 — CONDITIONALLY ON A PREMISE THAT Q-45 CLASSES AS UNTESTED,
whose ER-B alternative remains UNEXCLUDED and whose kill-test is blocked on control design.** A TYPE-C
closure is a governance fact about the branch, **not evidence that no coupling can live at S8.** The
theory's "no place left" is now known to rest, at this stage, on an adopted branch rather than a proof.

*** THE PROTOCOL WORKED ON ITS FIRST USE, AND THIS IS THE POINT. *** Under the old vocabulary this would
have been reported as `exchange_magnitude_free = false` and read as S8 being closed. **Typing it TYPE-C
made visible that the closure is a branch adoption.** And `NO_VERDICT` let the lane decline to manufacture
a refutation from an inapplicable requirement, which is exactly what Q-54 was built for. **Lane 1 also
attached four falsifiers**: a derived physical S8 law fixing `A_c`; a theorem upgrading ER-A; an admissible
S8 family with varied `A_c`; or proof that ER-A does not apply to S8.

**A NUMBER ENTERS HERE AND SHOULD BE WATCHED, NOT CLAIMED.** `tau_R = pi/sqrt(2)` (`:105`), and `A_c =
tau_R`. **This is a cell-time integral, not a coupling, and nothing about alpha follows from it.** But it
is a point where `pi` and an irrational enter the write chain under an untested branch premise. **There are
now at least four distinct tau-like quantities in play — the proper-time floor `tau = 1`, `tau_R`, `T_R`,
and `tau_orth` — and their relations are not established. Do not conflate them.** Assigned to Einstein.

REOPENS IF: ER-A is tested, superseded, or shown not to apply to S8; or any of lane 1's four falsifiers
fires.

---

## Q-56. "Are theory 001's closures proofs or adoptions?"

*** RULING: ZERO OF FIVE ARE UNCONDITIONAL STRUCTURAL TYPE-R CLOSURES OF THE PARAMETER-LOCATION QUESTION.
THEORY CANDIDATE 001'S NEGATIVE HALF IS A CONDITIONAL STATEMENT OVER THE ACTIVE PREMISE STACK, NOT A
PREMISE-INDEPENDENT EXHAUSTION THEOREM. *** Established 2026-07-30 by Codex lane 1 under paste 160
(`STAGE8_THEORY_001_CLOSURE_RETYPE_UNDER_Q54_V001.md`, `ea24057b…`, archive `626fa1f`, gate GREEN).

- **Closure 1, carrier.** Base commutation is TYPE-R **only inside the stipulated graded-tensor /
  trivial-record-grading carrier**; above base it is refuted or unbuilt.
- **Closure 2, composition.** Monomorphism TYPE-R; no-base-crossed-product TYPE-R **on the same stipulated
  foundation**; completed-CTP crossed-product exclusion **NO_VERDICT, blocked by TYPE-U producer absence**.
- **Closure 3, write.** Scalar write-multiplier rejection is the strongest TYPE-R subtest **but depends on
  the ADOPTED projection-module retraction axiom. It is not an unconditional no-write-parameter theorem.**
- **Closure 4, bare term.** `K_bare = 0` is **TYPE-C**, an adopted induced-only compositeness condition;
  finite-deformation exclusion remains TYPE-U.
- **S8.** Exchange magnitude TYPE-C under ER-A branch data; physical write-tail join TYPE-U (Q-55).

*** THE REVIEWER'S THEORY DOES NOT DO WHAT THE REVIEWER CLAIMED. *** It was written as a structural
result — four independent rulings closing four insertion points, therefore alpha cannot be a strength
assigned anywhere. **What it actually says is that no free parameter survives GIVEN the current adopted
premises**, of which Q-45 classes 17 of 26 as untested. **Closure 3, the one closure called "sharpest"
and "forbidden a strength rather than merely lacking one," rests on an adopted axiom.**

**THIS IS A RESULT ABOUT METHOD, AND IT IS THE USEFUL PART.** The standing principle is that permissions
never force a number and only overdetermination does. **Theory 001 attempted to force a location by
exhaustion. Exhaustion over an adopted premise stack forces nothing — it restates the stack.** Any future
claim resting on "alpha has nowhere else to live" inherits every untested premise in that stack, and must
say so.

**THE CANDIDATE IS NOT REFUTED; IT IS DEMOTED.** Its surviving form is honest and worth keeping: *no free
coupling parameter survives at any enumerated stage, at base level, conditional on the active premise
stack, with the enumeration incomplete as a count and S8 unresolved.* **Theory 001 status: REDUCED.**

**THREE INDEPENDENT PASSES CUT IT DOWN IN ONE AFTERNOON** — Einstein's enumeration audit (Q-53), lane 1's
S8 test (Q-55), and lane 1's retyping (Q-56). **Each was told it could kill the thing cheaply, and each
did part of the job.** The candidate cost one document and returned a method finding.

---

## Q-57. "Does the raw-correlator-to-retarded-Hessian map exist, and can it be specified?"

**RULING: IT DOES NOT EXIST UNDER ANY NAME, AND A CONDITIONAL SPECIFICATION NOW EXISTS WHERE NOTHING DID.
DERIVATION REMAINS TYPE-U; PHYSICAL VERDICT `NO_VERDICT`.** Established 2026-07-30 by Codex lane 2 under
the 158th relay (`STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md`, `57c06fcb…`, 1116 lines,
prepublication gate GREEN).

*** THE CORRESPONDENCE CHECK CAME BACK NEGATIVE, AND PROPERLY TYPED. *** A bounded 22-file search found no
derived `G -> H_R[G]` under another name — **TYPE-S with roots, exclusions, queries and file list
recorded**, which is what Q-54 requires and what makes the negative citable at all.

*** AND Q-50's HYPOTHESIS IS REFUTED — CORRECTLY, BY AN EXECUTED TEST. *** Primitive scalarization **is not
the same mathematical function**, established TYPE-R by a signature/composition test. **Q-50 explicitly
declined to claim the identification and flagged that typing it was lane 2's item; that caution was right.**
Q-51's broader classification survives: the actual-parent bridge is TYPE-U and prospectively upstream,
`p_loc` is downstream, and the response-extraction layer remains one layer.

**WHAT THE EXISTING FINITE RESULTS DO AND DO NOT GIVE.** The primitive operator bundle, the Duhamel
tangent, and the finite/algebraic complete-`Q_spec` state-evaluation scalar closure are all derived. **They
do not supply the raw bilocal `G`, the physical quotient, the inversion domain, contacts/boundaries, or the
complete BR/CTP extension**, which remains TYPE-U.

*** THIS IS THE FIRST CONSTRUCTION-SHAPED OUTPUT OF THE DAY, AND IT EXISTS ONLY BECAUSE OF Q-52. *** Under
the old charter a lane could not specify a missing object. Subject to premises P1-P8 — **each carrying
`derived = false | TYPE-U` and a `would-build` field** — the specification fixes the `R = 0` stationary
2PI-to-reduced-1PI Schur complement, `H_C[G] = i hbar G^-1`, full-contour Keldysh congruence, and mixed
retarded extraction. **It names the missing instantiation object `CTP_PHYS_INPUT_PACKAGE` and stops before
constructing it**, which is exactly the discipline Q-52 requires.

**SIX FAILURE-CAPABLE TESTS ARE SPECIFIED; NONE EXECUTED (TYPE-U).** `NO_VERDICT` takes precedence when
prerequisites are unbuilt. **No TYPE-C negative was used anywhere in the artifact.**

**PROCESS DISCLOSURE, VOLUNTEERED BY THE LANE:** an early broad path probe and a register-tail check
surfaced excluded path names and Q-55's register paragraph; **no Q-55 construction artifact was opened,
cited or used, and the final evidentiary search was rerun over the explicit allowed list.** Q-56 landed
mid-run, was checked, and does not alter this item. **This is what the register-head requirement was for.**

**MOVES NO FLAG. `0 of 18` and `0 of 11` unchanged** — a specification is not a derivation. But the layer
blocking the entire program now has one of its four objects specified rather than merely named.

---

## Q-58. "How many unselected absolute scales does the program have?"

*** RULING: EXACTLY ONE — `C_R = 1`, IN EVERY BRANCH. Q-45 SURVIVES. AND THAT IS THE DIFFERENCE BETWEEN A
DERIVATION AND A FIT. *** Established 2026-07-30 by Einstein under paste 159
(`STAGE8_UNIT_VALUE_ADOPTION_INDEPENDENCE_AUDIT_EINSTEIN_V001.md`, seal `c7a2505d…`, verified).

*** THE SENTENCE THAT MATTERS MOST TODAY, IN EINSTEIN'S WORDS: *** with **one** unselected absolute scale,
a computed alpha "could honestly claim to be a **conditional derivation**, exact modulo one named untested
adoption plus disclosed dimensionless branch conventions, each independently testable." With **more than
one**, it could claim only "that some point in a multi-parameter family reproduces the number:
**operationally a fit.**" **THE PROGRAM IS IN THE FIRST CASE**, conditionally on the caveats below.

**THE REVIEWER'S Q-45 WORDING CONFLATED TWO THINGS AND THAT WAS THE TRAP.** "Unselected absolute scale" and
"unselected unit value" are different findings. **There is exactly one of the first and more than one of
the second.** Corrected here; Q-45's substantive claim stands.

**WHY `C_R = 1` IS THE ONLY ONE.** The record layer alone has **no** absolute scale: the sealed scale orbit
`T_R -> lambda T_R`, `H_R -> H_R/lambda` is broken **only** by `chi_* = C_R = 1`. **`s = pi` and `xi = 1/2`
are orbit-INVARIANT coefficients — they set the coefficient, not the scale.** `E_R` has no independent
fixing; **the "something fixing `E_R`" IS `C_R = 1`.** Verified twice, including an independent
re-derivation of the ER-A clause's `T_R`-independence.

**KINDS, 2/1/2 — THEY ARE NOT THE SAME KIND OF QUANTITY.** `C_R = 1` and `tau = 1` are **dimensionless
adopted unit values** (both UNTESTED). `tau_R = pi/sqrt(2)` is a **derived** dimensionless interval —
derived as the least positive orthogonality zero conditional on `|w| = 1` — **with a second, adopted role
as ER-A's amplitude clause, and it is the adoption that binds at S8** (Q-55). `T_R` and `tau_orth` are
**dimensionful proper intervals**. `N_BR(k_R) = 1` is excluded: its "1" is a cardinality, not a unit value.

**INDEPENDENCE — NOT ONE CHOICE FIVE TIMES, AND NOT FIVE.** *** `T_R` IS DERIVED FROM `C_R = 1` — ONE
CHOICE, NOT TWO; counting both would double-count the selector. *** `tau_R`'s deployment rides on `T_R`
through the sealed conversion `tau(t) = tau_R · t / T_R`. `[tau, tau_R]` is **NO_VERDICT** — no deformation
control exists (TYPE-U). **`tau_orth = T_R` was CHECKED, not assumed**: arithmetically `|Delta| = E_R`,
promotion blocked by the binary gate, no premise-failure rule frozen.

**COUNTS, BY BRANCH.** Current stack with ER-A in force: **2 unit-value scale choices** (`C_R = 1`,
`tau = 1`); **3 scale-bearing adoptions** counting ER-A; **4** counting the row-6 saturation adoption inside
`T_R`'s marker chain. ER-A superseded → **3 genuinely free** (`A_c` reverts to external per Q-55). Row 22
failing adds `tau_orth` as a TYPE-U open quantity, not an adoption — **worst case up to 4 open scale
quantities.**

*** TWO CAVEATS, RECORDED NOT SOFTENED. *** (i) **THE SOLE SELECTOR HAS NOT YET SELECTED** —
`absolute_record_interval_derived_in_declared_branch = false`, with a **disclosed sqrt(2)
energy-identification ambiguity at marginality**. (ii) `tau = 1` is a second unselected unit value **of
non-absolute kind**, which answers lane 2's open flag `TAU_EQUALS_1_SECOND_SCALE_CARRYING_ADOPTION_RULED`
**in the negative for the absolute-scale sense**.

**RESIDUAL:** N2, TYPE-S with the search stated — **no sealed sentence identifies or separates `tau = 1`
and ER-A's clause, so the 2 could compress to 1.**

**SEVEN NEGATIVES TYPED (N1-N7)**, including one **TYPE-R killing the "c = 1 is a second free unit"
misreading**. **The fitting fence held: `tau_R` was compared to nothing measured and no inference about
alpha was drawn from `pi/sqrt(2)`** — the exact restraint the paste demanded.

---

## Q-59. "Can `C_R = 1` select alone?"

*** RULING: NO. IT IS A CONDITIONAL SELECTOR, NOT A COMPLETED ABSOLUTE-SCALE DERIVATION. Q-58 SURVIVES —
IT REMAINS THE SOLE ORBIT-BREAKER — BUT IT SELECTS ONLY AFTER AN UNBUILT SOURCE-RECORD-GRAVITY /
HAMILTON-JACOBI BRIDGE SUPPLIES THE ENERGY/ACTION INTERFACE AND A FIRST DURABLE-PUBLIC CLOSURE THEOREM. ***
Established 2026-07-30 by Codex lane 1 under relay 161
(`STAGE8_C_R_SELECTOR_NONSELECTION_DIAGNOSIS_V001.md`, `e2ee7b0b…`, archive `5ef3ae1`, gate GREEN).

**WHAT SELECTING WOULD MEAN:** fixing a unique isolated stable Planck-unit record interval and the
associated radius, energy and mass units. **It has not selected because the energy/action interface is
unbuilt and marginality is adopted rather than derived.**

*** THE `sqrt(2)` IS A GENUINE PHYSICAL FORK, NOT A CONVENTION. *** It is **Misner-Sharp versus
reference-subtracted Brown-York energy at marginality** (`BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:50-104`).
**Sealed text does not settle it.** The two give **different exact conditional roots whose ratio is
`sqrt(2)`**, and `Misner_Sharp_and_Brown_York_candidates_coincide_at_marginality = false | TYPE-R` — an
executed refutation, not an absence. **The choice changes `T_R` by `sqrt(2)`.**

*** AND HERE IS WHY Q-58 STILL SURVIVES, WHICH THE TYPING IS WHAT MAKES VISIBLE. *** Both identifications
are typed `TYPE-U` — **unbuilt, not adopted.** The lane records that resolution is *not necessarily* a
binary act of choosing: the bridge would **derive** the identification as part of the stationary cell
target. **So this is an unbuilt derivation, not a second free parameter, and the program still has exactly
one unselected absolute scale.**

*** BUT THE WARNING IS SHARP: IF THE BRIDGE IS NEVER BUILT AND SOMEONE PICKS AN IDENTIFICATION, THAT PICK
BECOMES A SECOND SCALE-BEARING ADOPTION — TYPE-C RATHER THAN TYPE-U — AND BY Q-58's OWN CRITERION THE
PROGRAM WOULD MOVE FROM CONDITIONAL DERIVATION TOWARD FIT. *** The `sqrt(2)` must be derived, never chosen.

**THE MISSING OBJECTS, NAMED:** complete Lorentzian CTP action/boundary/time-flow data; a constant
Hamilton-Jacobi record energy; a proof that the branch-energy difference equals the gravitating closure
energy; a reference-subtraction / no-spectator theorem; a derived marginal first durable-public closure;
and an isolated stable positive interval solution.

**ONE EXECUTED REFUTATION WORTH KEEPING:** `strict_untrapped_inequality_alone_selects_unique_scale = false
| TYPE-R`. **The inequality alone does not select** — that is proved, not merely unbuilt.

*** OPEN CORRESPONDENCE QUESTION, NOT ASSUMED EITHER WAY: IS THIS ENERGY/ACTION BRIDGE THE SAME LAYER AS
THE RESPONSE-EXTRACTION LAYER OF Q-51, OR A SECOND INDEPENDENT UNBUILT LAYER? *** If the same, the program
has one blocking layer serving two issues. **If different, it has two.** This program has found a missing
object already present under another name at least ten times; **it must be checked, not assumed.**

---

## Q-60. "Is the Q-59 scale bridge the same layer as Q-51's response extraction?"

**RULING: NO — DIFFERENT LAYERS, AND THE SCALE BRIDGE IS UPSTREAM. BUT THEY MAY SHARE ONE PREREQUISITE,
AND THAT SHARING IS UNVERIFIED.** Answered 2026-07-30 inside lane 1's own artifact,
`STAGE8_C_R_SELECTOR_NONSELECTION_DIAGNOSIS_V001.md:189-192`, which the return summary did not surface.

```text
this is not the response-extraction layer as such. The named missing object is upstream:
a complete source-record-gravity / Hamilton-Jacobi scale bridge. It may consume CTP action
and boundary-data inputs if Codex 2's CTP_PHYS_INPUT_PACKAGE supplies them, but this
artifact did not inspect or build that package.
```

**SO THE TWO BLOCKING LAYERS ARE DISTINCT.** The scale bridge (issue 1) sits **upstream** of response
extraction (issue 2). **The program has two unbuilt layers, not one** — and neither subsumes the other.

*** BUT `CTP_PHYS_INPUT_PACKAGE` MAY BE A COMMON PREREQUISITE OF BOTH. *** The bridge needs "complete
Lorentzian CTP action/boundary/time-flow data"; the package supplies a complete microscopic inclusive CTP
functional, contacts, and boundary/edge data. **If those are the same objects, Codex 2's current relay-162
task serves BOTH issues, and the program has one common bottleneck feeding two problems rather than two
independent ones.**

*** THE SHARING IS NOT ESTABLISHED AND MUST NOT BE ASSUMED. *** Lane 1 wrote "may consume" as a conjecture
and **was fenced from inspecting the package** — `CTP_PHYS_INPUT_PACKAGE` was explicitly off-limits under
the 161st relay. **No search was run.** This is the shape of claim that has been wrong ten times in
this program.

**VERIFICATION POINT, NO NEW LANE NEEDED:** Codex 2 is specifying the package under relay 162 right now.
**When it returns, check its contents against the bridge's six named requirements** — complete Lorentzian
CTP action/boundary/time-flow data, constant Hamilton-Jacobi record energy, branch-energy/closure-energy
equality, reference-subtraction and no-spectator theorem, derived marginal first durable-public closure,
and an isolated stable positive interval solution. **Coverage of the first is plausible; the other five are
gravitational and almost certainly are not in the package.**

**REVIEWER NOTE:** the answer was in the artifact and not in the lane's summary. **Reading the artifact
rather than the report is what found it** — the second time today a return summary omitted something the
artifact contained.

---

## Q-61. "Is there any route that could force a number?"

*** RULING: THE PROGRAM HAS ZERO LIVE PAIRS. THE ONLY ROUTE TO A FORCED NUMBER IS CURRENTLY EMPTY. ***
Established 2026-07-30 by Einstein under relay 163
(`STAGE8_OVERDETERMINATION_SPECIFICATION_AND_PAIR_SURVEY_EINSTEIN_V001.md`, seal `8b8b8977…`, verified).
**LIVE 0 · STRUCTURAL 4 · NOT-A-PAIR 7.**

*** AND IT IS NOT A RECORDED ABSENCE — IT IS CORROBORATED BY THE CORPUS'S OWN EXECUTED NEGATIVES. ***
"TWO INDEPENDENT DOF COUNTS AGREE: NO OVERDETERMINATION". The slot-9 ratio class **executed and failed**:
"one trace, one function, one determination presented several ways". "ZERO CONSTRAINTS AGAINST NINE
UNKNOWNS". *** EVERY COINCIDENCE SO FAR EXAMINED HAS BEEN ADJUDICATED **ONE SOURCE READ TWICE**. *** That
is the fitting risk of this program stated in five words, and it has already happened repeatedly.

**OVERDETERMINATION IS NOW SPECIFIED CHECKABLY — THREE CONDITIONS.** **[O1]** premise-DAG disjointness
below a target-blind kernel, decided by a **deletion test**: remove `C_b` and everything reachable only
from it; `C_a` must survive, and conversely. **[O2]** the **disagreement witness**. **[O3]** target
blindness as a **process fact** — sealed order, an executed target-entry sweep, no post-hoc tuning —
**not a mental state**, which is undecidable and would reject all human physics.

**TWO DEMOTIONS INSIDE THE SPEC, BOTH EARNED.** "Distinct mechanisms by content" is **descriptive, never
dispositive** — this corpus has twice proved it unreliable (five spellings of one shape; a ruling reaching
a route under another label). And the boundary clause the survey itself forced: *** n CONDITIONS FIXING n
FREEDOMS THROUGH COMPLEMENTARY COORDINATES IS EXACT DETERMINATION, NEVER OVERDETERMINATION. *** The
marker + `C_R = 1` system yields `T_R` with **zero redundancy and no expressible disagreement witness** —
**a spec that counted it would bless every well-posed formula in physics.**

**COINCIDENCE BECOMES EVIDENCE ONLY IF DISAGREEMENT WAS POSSIBLE.** Requires an exhibited admissible family
`V`, itself audited, in which each condition alone leaves several members, joint satisfaction isolates up
to disclosed discrete conventions, **and a member exists on which the two conditions pick different
values.** Outcomes typed: `V` exhibited → evidence; `V` not exhibited → **NO_VERDICT, not "artefact"**;
`V` provably impossible → **the agreement is a theorem — a check, never evidence.**

**THE FOUR STRUCTURAL SHAPES, ALL WITH UNBUILT LEGS.** (1) DEPARTURE_2's winding × complete-selector — leg
B not derived, Q-59 added an unbuilt-bridge prerequisite, and **even live it defeats a dilation, not the
additive freedom.** (2) **The cross-sector Requirement I/II on `beta` — the corpus's ONLY sealed
two-conditions-one-quantity specification, with its anti-tautology falsifier ALREADY FROZEN**; both legs
unbuilt. (3) `tau_orth = T_R` — **the only already-exhibited failure-capable agreement in the corpus**
(`|Delta| = E_R` came out equal **and did not have to**); not live because no failure rule was frozen and
`|Delta|`'s premise-disjointness is unaudited — **and it lands on the scale, so redundancy there tests the
selector, not the coupling.** (4) `S9-A × C_record(K_*) = 0` — **the program has re-posed its own
deliverable as an overdetermination target**, zero legs built.

*** PRE-STRUCTURAL ABSENCE, AND THE MOST PROMISING THING IN THE REPORT: `kappa_record` vs `K_*` — "TWO
STIFFNESS OBJECTS, NEVER RELATED" — the natural future pair site ON THE VALUE PATH. ***

**A THIRTEEN-ITEM DERIVATION-VERSUS-FIT CHECKLIST**, five items added under adversarial attack, each a
fit-vector the corpus already paid for once. **THE HONESTY CLAUSE, UNSOFTENED: THE PROGRAM TODAY FAILS
ITEMS 1b, 4, 5 AND 12.** "The standard is not designed to be met; it is designed so that, if met, the
result is not a fit." *** NO_VERDICT — NOT FAIL, NOT PASS — IS THE CORRECT CURRENT GRADE OF ANY
OVERDETERMINATION CLAIM IN THIS CORPUS. ***

**NINE TYPED NEGATIVES, INCLUDING ONE TYPE-R AGAINST ITS OWN DRAFT** — the `1 + a·u_D` family's sealed
scope is narrower than the author's `[D2]` used it, **repaired in place rather than left standing.**

**BINDS NOTHING UNTIL ADOPTED.** Q-52-declared, `derived = false`.

---

## Q-62. "Are `kappa_record` and `K_*` a pair?"

**RULING: `NO_VERDICT`. NOT A CANDIDATE PAIR TODAY — AND ALSO NOT SHOWN TO BE ONE SOURCE READ TWICE.**
Established 2026-07-30 by Codex lane 1 under relay 165
(`STAGE8_KAPPA_RECORD_KSTAR_PAIR_TEST_UNDER_Q61_V001.md`, `5d86c9c1…`, archive `448d6b3`, gate GREEN).

```text
verdict    = NO_VERDICT
blocked_by = no common target X and no exhibited Q-61 disagreement witness
```

**THREE DISTINCT OBJECTS, NOW TYPED.** `kappa_record` is the **primitive record-side intensive
susceptibility/Hessian**; `K_*` is the **one-cell `Gamma_K`/BR onset root**; `kappa_Thomson` is the
**physical charged-sector Thomson stiffness**. **Not the same object, and no derived identity relates
them.**

*** THE DELETION TEST [O1] PASSES — AND THAT IS THE INTERESTING PART. *** "Each target specification
survives deletion of the other's apparatus" — **so they are premise-disjoint** — **but only as an unbuilt
target spec. Neither determination exists yet, and no shared target X is established.**

**SO PAIRHOOD FAILS ON THE TARGET, NOT ON DISJOINTNESS.** A pair must land on **one** quantity; the corpus
supplies no common target. `disagreement_family_V_exhibited = false | TYPE-U`. Under Q-61, a family not
exhibited yields **`NO_VERDICT`, not "artefact"** — and the lane graded it exactly that way.

**THE BOUNDARY CLAUSE DOES NOT RESCUE IT EITHER**: no sealed formula makes them complementary coordinates,
so this is **not** exact determination — the situation is **weaker than** exact determination, not a
well-posed formula in disguise.

*** AND HERE IS THE LIVE DEPENDENCY. *** The lane records that **if a future bridge makes them
complementary coordinates of one value, Q-61 classes that as EXACT DETERMINATION, not overdetermination.**
**Whether that outcome would be sufficient to force a number is precisely the question queued for Einstein
under relay 166.** *** SO THIS RESULT'S MEANING IS NOT YET FIXED: under the standing principle
"only overdetermination forces a number" it is a dead end; if relay 166 rules a unique require sufficient,
it becomes a live route. Same evidence, two meanings, pending one ruling. ***

**NO LEAD-WITH CONDITION FIRED** — neither pair nor one-source-twice. **`would-build`: a common target `X`
plus an exhibited Q-61 disagreement family `V`.**

**THIRD `NO_VERDICT` OF THE DAY.** The lane declined to call a disjointness result a pair, and declined to
call an absence a refutation. **Both temptations were available and the relay had warned against the first
explicitly.**

---

## Q-63. "Interim: the `CTP_PHYS_INPUT_PACKAGE` triage, and a lane that stopped itself."

*** STATUS: PROVISIONAL. THE ARTIFACT IS UNSEALED AND UNCOMMITTED BY THE LANE'S OWN DECISION. NOTHING HERE
IS RATIFIED AND NO FLAG MOVES. *** Codex lane 2 under relay 162, 2026-07-30, draft
`STAGE8_CTP_PHYS_INPUT_PACKAGE_TRIAGE_AND_LOAD_BEARING_FUNCTIONAL_SPEC_V001.md` (`f8ef05a2…`, **NOT
sealed, NOT committed, `physical_verdict = NO_VERDICT`**).

*** THE LANE STOPPED ITSELF UNDER THE STALE-AUTHORITY RULE, AND THAT IS THE HEADLINE. *** It identified
that relay 164's dependency census bears directly on its own question — whether the two chains share
`CTP_PHYS_INPUT_PACKAGE` — and **declined to seal against a ruling it knew was coming.**

```text
relay164_shared_node_determination_derived = false | TYPE-U
    would-build: execute relay 164's independent dependency graph
artifact_sealable = false | TYPE-C
    constraint: bearing relay-164 result pending and T8 verdict wiring unresolved
    release: consume relay-164 result and separate T8 from the producer verdict
```

**THE REGISTER-HEAD REQUIREMENT WAS WRITTEN THIS AFTERNOON AFTER THREE ARTIFACTS ARRIVED STALE. THIS IS THE
FIRST TIME IT PREVENTED ONE RATHER THAN DETECTING ONE.** **No deadlock exists**: relay 164 fenced Einstein
from package internals, so the census completes without this lane.

**PROVISIONAL FINDINGS, TO BE RE-VERIFIED ON RESUMPTION, NOT RELIED ON:**

- *** TRIAGE: 0 COMPLETE / 9 PARTIAL / 0 WHOLLY ABSENT. *** **Nothing in the package is missing outright.**
  All nine partially exist. **If this survives sealing it is materially better news than "nine unbuilt
  objects" implied**, and it bears on how deep relay 164's census will find the graph to be.
- **The repaired `B0 -> C0/U1-U3 -> item 1 -> D1-D5` graph passed hostile review as NON-CIRCULAR.** **A
  partial early answer to relay 164's cycle question** — at least this subgraph is acyclic. **It does not
  clear the whole graph.**
- Item 1 is now specified as a **pointwise normalized functional, not a `Log_0` germ** — a self-correction
  by the lane.
- **T1-T7 pass review as failure-capable. T8 carries a defect**: it tests the external Q-60 interface
  hypothesis but is **wired into the item-1 producer verdict** and needs a separate identity/sufficiency
  verdict. **A test wired to the wrong verdict is the `cannot_fail` failure mode in a new costume**, and
  the lane caught it in its own work.

**PROCESS DISCLOSURE, VOLUNTEERED:** a sixth excluded-reference probe was surfaced during relay-164 routing,
**discarded and not used.**

REOPENS: automatically, when relay 164 returns and this lane resumes.

---

## Q-64. "How much unbuilt work stands between the program and a number?"

*** RULING: NO CYCLE. THE PROGRAM IS DEEP, NOT CIRCULAR. AT LEAST 172 NAMED UNBUILT OBJECTS, ACYCLIC, TO
DEPTH >= 5, ON TWO DISJOINT CRITICAL PATHS, WITH A BOUNDARY CONSISTING ENTIRELY OF UNBUILT LEAVES. ***
Established 2026-07-30 by Einstein under relay 164
(`STAGE8_ALPHA_DEPENDENCY_CLOSURE_CENSUS_EINSTEIN_V001.md`, seal `05dccaf5…`, archive `df18b41`, gate
GREEN — **the first Einstein artifact the gate accepted directly**).

**ZERO SCCs, ZERO NON-TEST SELF-LOOPS ACROSS ALL 122 STATED CONSTRUCTION EDGES.** The lead-with condition
did not fire. *** AND THE ONE "CIRCULAR UNTIL…" PHRASE IN SEALED PROSE IS A **TEST** LOOP, NOT A
CONSTRUCTION LOOP: `C_R = 1`'s FALSIFIER is gated on the unstartable response object, but its
CONSTRUCTION is not. *** Test edges were held out of cycle detection **by kind**, precisely so the
distinction could not blur. **This corrects the reviewer's earlier "close to circular" characterization of
the `C_R` falsifier — it is test-circular, not construction-circular, and those are different problems.**

**THE COUNT.** 172 distinct named unbuilt objects = **82 sealed identifiers + 90 prose-named targets that
exist only as `would-build` children and name no path to their own construction**, over 122 stated edges.
**Separately: ~350 distinct UNTYPED-LEAF identifiers (~1,050 pre-Q-54 `derived = false` lines with no
`would-build`) — counted, never walked, never guessed at.** *** NO INFERRED EDGE EXISTS ANYWHERE: linking
was exact-identifier, verifier-noted correspondence, or nothing. ***

*** IT BOTTOMS OUT — IN THE WRONG THING. EVERY CHAIN TERMINATES, AND NONE TERMINATES IN ANYTHING DERIVED.
THE GRAPH'S ENTIRE BOUNDARY IS UNBUILT GROUND. *** Longest stated chain, depth 5: `Gamma_K` → the
raw-correlator map (the one Q-51 object now specified) → `CTP_PHYS_INPUT_PACKAGE` → P1…P8 → their
`would-build` targets. **Depth 5 is a floor twice over** — package internals are fenced, and 90 chains end
where sealed text simply stops stating.

*** THE TWO LAYERS SHARE ZERO NODES ON STATED EDGES. Q-60's "may share the package" CONJECTURE IS
UNSUPPORTED. *** Nothing in the six bridge objects' `would-build`s names the package, any P-row, or any
response-side object. **TYPE-S, scoped: this proves nobody has STATED a shared prerequisite, not that the
physics is independent.**

*** THE INCIDENT, RECORDED ON THE ARTIFACT'S FACE, AND IT IS THIS PROGRAM'S DISEASE BITING THE CENSUS'S OWN
TOOLING: the first convergence run reported 43 shared nodes — ALL FALSE — because a seed regex let `C_R`
SUBSTRING-MATCH `C_record`. *** Caught by path-tracing before anything was reported; the corrected
word-boundary run gives the answer. **Substring matching has now produced a false positive in the corpus,
in an audit script, and in the audit of the audit.**

*** TWO CRITICAL PATHS, DISJOINT — AND THAT IS ITSELF THE FINDING. *** By transitive unblock count the
**package** wins (package → map → all four Q-51 objects → `Gamma_K`/`C_record` → the S9-A
overdetermination target), **so the census CONFIRMS rather than redirects: Codex 2 already sits on that
head.** The **bridge** side — the six Q-59 objects unblocking the selector's consummation — **is a second
critical path sharing nothing with the first, and its head is UNASSIGNED.** **Nothing on stated text forces
either to wait for the other: they can be worked in parallel.**

**SEVEN TYPED NEGATIVES.** One TYPE-R (no cycle — **the census's only physical-content negative**), three
TYPE-S with full scope, one TYPE-U, one TYPE-C (the package fence), and **one `NO_VERDICT`: three literally
required pathless identifiers whose fate rides on an unmerged alias — CUSTODIAN'S TO RESOLVE.** One phantom
identifier corrected (`T1_through_T7` occurs nowhere; the flag is `T1_through_T8`). **Four alias candidates
carried unmerged with evidence on both sides rather than decided.**

---

## Q-65. "Does only overdetermination force a number?"

*** RULING: NO. THE STANDING PRINCIPLE IS WRONG AS WRITTEN. "Permissions never force a number" is RIGHT;
"only overdetermination does" is FALSE. A REQUIRE-SHAPED CONDITION WITH DERIVED EXISTENCE AND UNIQUENESS
FORCES A NUMBER. *** Established 2026-07-31 by Einstein under relay 166 item 1
(`STAGE8_FORCING_BOUNDARY_ADJUDICATION_EINSTEIN_V001.md`, `05c832ad…`, seal verified).

*** THE SLOGAN FUSED TWO DIFFERENT THINGS: FORCING IS A FACT ABOUT THE ADMISSIBLE SET; ANTI-FITTING IS A
FACT ABOUT HOW WE KNOW THE POINT WASN'T CHOSEN. *** The corpus half-knew — the tracker's own produce/force
asymmetry line, and **Q-58's grading, which is incompatible with the slogan read strictly.** Einstein owns
that contradiction as much as the reviewer: **it wrote Q-58 and then a checklist whose items 4-5
presuppose a pair.**

**THE REVIEWER'S CORRECTION IS SUSTAINED 4½ OF 5, AND ATTACKED WHERE HE ASKED.** **Point 1 MISCOUNTS** —
exact joint determination is a **third** forcing shape. **Point 4 holds only if the reduction itself is
derived** — today it is a stack of adoptions. **Point 5 is WRONG**: `[O3]` does not supply the same
protection, because **provenance is not structural**; the gap is **priced, not waved off**.

**THE ANSWER: a unique require plus certificates suffices for "CONDITIONAL DERIVATION, SINGLY-ATTESTED" —
ONE GRADE BELOW A PAIR.** Items **4′/5′** (require-status and root-structure certificates, the solvability
counterfactual) replace the pair items; **freeze-before-root-finding and the target-entry sweep become
keystones.** *** AND THE ONE THING REDUNDANCY ALONE SUPPLIES: INDEPENDENT CORROBORATION AGAINST A **WRONG**
CONDITION — WHICH IS ERROR-RISK, NOT FIT-RISK. ***

*** R-L2b IS **REFUTED AS WRITTEN | TYPE-R** — AND ITS REFUTATION IS THE SOLO ROUTE'S PROOF-OF-CONCEPT: A
REQUIRE THAT COULD DIE, AND DID. *** Typed, not built.

**The route restatement is shorter than "build two independent legs," so the reviewer's error WAS costing
lane time.** **FLAGGED FOR THE PRINCIPAL: S9-A's own wording embeds the over-strong principle ("derived and
overdetermined") and may want relaxing.**

---

## Q-66. "The canonical registry and the graph boundary." (Einstein, relay 166 items 2-3)

`STAGE8_CANONICAL_IDENTIFIER_REGISTRY_EINSTEIN_V001.md` (`aad6dc23…`) and
`STAGE8_GRAPH_BOUNDARY_WALK_EINSTEIN_V001.md` (`c8e5b049…`), seals verified.

**REGISTRY — ZERO MERGES, SO NO CYCLE WAS CREATED.** (a) bare-vs-branch `absolute_record_interval` —
**NO_VERDICT, escalated to the principal.** (b) the Q-51 operator vs the extension flag — **NO_VERDICT, and
the highest-value pending merge: the ruling moves a Q-51 object between pathless and pathed.** (c) the
exchange-magnitude pair — **DISTINCT**, confirmed twice. (d) `kappa_record` vs `K_*` — **the corpus's own
sealed NO_VERDICT governs** (Q-62). The `C_R` pair was fenced; **on discovering Codex 1 was adjudicating
it, reading stopped.**

**The namespace is cleaner than feared, not clean:** zero collisions inside the anchored population; **two
real families outside it — a case-fold doublet mixing typed and untyped spellings of the same identifier
(the cycle hazard), and one token-reorder pair**; 18 one-name-across-eras identifiers. *** SCOPE HOLE
ESCALATED: THE 13 JSON AUTHORITY LEDGERS HAVE NEVER BEEN SWEPT BY ANYTHING. ***

**BOUNDARY WALK — NO CHAIN ANYWHERE TERMINATES IN `derived = true`. THE FIRST FLOOR HAS STILL NOT BEEN
FOUND**, and the enlarged graph is acyclic (236 node records, Tarjan). **90 prose-targets split 43
restatements / 18 real / 29 NO_VERDICT** — *** and NINE OF THE ELEVEN MAX-UNBLOCK P-ROW CHILDREN ARE
SAME-LINE RESTATEMENTS OF THEIR OWN ROWS. THEY WERE NEVER NINE INDEPENDENT OBJECTS. ***

**THE UNTYPED MASS IS NOW A NUMBER: 372 identifiers — 64 LIVE (17.2%), 14 retired, 10 off-path, 284
honestly UNKNOWN.** "Most are probably not on the value path" is confirmed. One costly-error correction
applied (a RETIRED flag the sealed text names LIVE) and **an extractor bug caught by verification (11
identifiers recovered, none live).**

---

## Q-67. "The bridge critical path." (Codex 1, relay 167)

**ALIAS RESOLVED:** `C_R_marginal_selector_derived_rather_than_adopted` and
`marginal_closure_condition_derived_rather_than_assumed` are **the same TYPE-C obligation**
(`STAGE8_BRIDGE_ITEM0…`, `ba1babe5…`). **So that pathless node has a release — the `C_R` chain has a naming
artefact, not a hole.**

**SIX OBJECTS: 0 COMPLETE / 6 PARTIAL / 0 ABSENT.** Dependency order **S1 → S2 → S4 → S3 → S5 → S6**
(`0a631fbb…`). **S1** (complete Lorentzian CTP action/boundary/time-flow) and **S2** (constant
Hamilton-Jacobi record energy) are now **specified as Q-52 test objects, `derived = false | TYPE-U`**
(`e6bf47f6…`, `ecfbab95…`); **S2 cannot be attempted until S1 exists.**

**`bridge_chain_reaches_derived_ground = false | TYPE-S`** (`6f09985d…`). **Terminal blockers are all
TYPE-U except the marginality node, which is TYPE-C** — i.e. the bridge bottoms out in one **adopted**
obstacle and otherwise in unbuilt ones.

---

## Q-68. "The package interior." (Codex 2, relay 168)

*** LEAD: ONE CONDITIONAL P8 CONTROL PATH REACHES A DERIVED FINITE OPERATOR-RESPONSE BUNDLE — THE CLOSEST
THING TO A FLOOR ANYONE HAS FOUND. BUT IT IS NOT A MANDATORY CONSTRUCTION CHILD, SO PHYSICAL REACHABILITY
REMAINS `NO_VERDICT`. *** (`c2279d27…`.)

**T8's identity and sufficiency verdicts are now separated** — the defect the lane caught in its own work.
**Triage confirmed word-boundaried: 0 COMPLETE / 9 PARTIAL / 0 WHOLLY ABSENT** (`ebdad2b9…`); **B0 is the
load-bearing stop.** The **physical `Log_0` germ is specified without being constructed**; L0-L3 and
physical promotion remain TYPE-U (`14573a67…`).

*** CYCLE CHECK: strict graph 20 nodes / 47 edges and selected label-preserving 39 / 100 are ACYCLIC — BUT
IF P7's "PHYSICAL PACKAGE" IS LATER IDENTIFIED WITH `CTP_PHYS_INPUT_PACKAGE`, A TWO-NODE CYCLE FIRES.
GLOBAL ACYCLICITY THEREFORE REMAINS `NO_VERDICT`. *** (`25bf671b…`.)

---

## Q-69. "Why both overnight cycle hazards have the same shape." (Reviewer synthesis)

*** TWO LANES THAT COULD NOT SEE EACH OTHER FOUND TWO INDEPENDENT CONDITIONAL CYCLES IN ONE NIGHT, AND
BOTH FIRE UNDER THE SAME OPERATION. ***

- **Einstein (Q-66):** ratifying the R15 collapse manufactures `{producer ↔ crossed-product-exclusion}`
  against the sealed reverse `blocked_by` — **"existing only if a flag is identified with its discharge
  object."**
- **Codex 2 (Q-68):** identifying P7's "physical package" with `CTP_PHYS_INPUT_PACKAGE` fires a two-node
  cycle.

*** IN BOTH CASES THE CYCLE IS MANUFACTURED BY IDENTIFYING A **FLAG** WITH THE **OBJECT THAT DISCHARGES
IT**. THE FLAG AND ITS DISCHARGE OBJECT ARE NOT THE SAME NODE, AND MERGING THEM CREATES A FALSE EDGE FROM
THE OBLIGATION BACK TO ITS OWN PRECONDITION. ***

**STANDING RULE, EFFECTIVE NOW: NEVER IDENTIFY A FLAG WITH THE OBJECT THAT DISCHARGES IT — not in a
registry merge, not in an alias ratification, not to tidy a graph.** **Any proposed merge must state which
side is the obligation and which the discharge, and a merge across that boundary is refused by default.**

**This is why the registry work must not "tidy," and it is the concrete reason Einstein's zero-merge
discipline was correct rather than merely cautious.** Both hazards remain **hypothetical** — no merge has
been ratified — **and the morning ratification must preserve the flag/discharge distinction or escalate.**

---

## Q-70. "Is 'no chain reaches derived ground' bad news?"

*** RULING: THE QUESTION WAS MALFORMED. A WELL-FOUNDED THEORY BOTTOMS OUT IN AXIOMS, NOT IN DERIVED
RESULTS. *** Reviewer correction 2026-07-31, prompted by the principal asking whether a floor exists at
all. **Queued to Einstein as relay 169 for adjudication; not settled here.**

**Q-64 and Q-66 both reported that no chain terminates in `derived = true`, and the reviewer repeated it as
"the first floor has not been found" — as though a dependency graph OUGHT to bottom out in derived
objects.** *** IT OUGHT NOT. Nobody derives mathematics down to nothing; you stop at primitives. ***

**SO THE BOUNDARY BEING UNBUILT IS ONLY BAD NEWS IF ITS LEAVES ARE THINGS THAT OUGHT TO HAVE BEEN
DERIVABLE. Q-54's typing already separates them:**

```text
TYPE-C  adopted premise or constraint     -> A LEGITIMATE FLOOR. A theory may rest on these.
TYPE-U  unbuilt, carries a would-build    -> A DEBT. The corpus itself says it should exist.
```

*** A BOUNDARY OF TYPE-C IS A FINISHED FOUNDATION. A BOUNDARY OF TYPE-U IS AN UNPAID LEDGER. THE REGISTER
HAS BEEN REPORTING TWO OPPOSITE DIAGNOSES AS ONE. ***

**The data already hints at the split:** Q-67's bridge depth report found terminal blockers **all TYPE-U
except the marginality node, which is TYPE-C** — one axiom, five debts. **Nobody has run that typing across
the whole boundary.**

**THE CLASS THAT MATTERS MOST IS THE THIRD ONE: DEBT-IN-AXIOM-CLOTHING — an adoption written where a
derivation was owed.** *** THAT SUBSTITUTION IS THIS PROGRAM'S CHARACTERISTIC ERROR, and a boundary made
mostly of it would be the most serious finding in the program's history. ***

**AND IT MAY COLLAPSE INTO A QUESTION ALREADY BEING ASKED.** If the floor is an axiom set, the test of it
is not existence but **defensibility — few, independently motivated, target-blind** — which is Q-65's
anti-fit standard, and whose measure already exists: **17 of 26 untested (Q-45).** **So "is there a floor?"
and "would a computed alpha be a derivation?" may be nearer the same question than the register has
treated them.** Relay 169 asks Einstein whether that is right.

**REVIEWER ERROR RECORDED PLAINLY:** "no first floor" was reported three times as a finding when it was a
category mistake. **The principal caught it by asking whether a floor exists at all.**

---

## Q-71. "What actually forces the number — and did the program already know?"

*** RULING: IT IS THE THRESHOLD, EXACTLY AS THE PRINCIPAL SAID. AND THE FORCING MECHANISM WAS ALREADY
WRITTEN INTO `STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md` ON 2026-07-30 — NOBODY RECOGNIZED IT AS ONE. ***
Established 2026-07-31 from the principal's statement *"my guess would have always been that it's a matter
of reaching the threshold, not overdetermination"* and verified against sealed text.

**Q-65 established that a require-shaped condition with DERIVED existence and uniqueness forces a number.**
*** A THRESHOLD WITH A DERIVED UNIQUE ROOT IS PRECISELY THAT SHAPE. *** And this program is built on
thresholds end to end — onset conditions, marginal closure, first durable record, `C_record(K) = 0` at
`K_*`. **The forcing shape was never missing. It was the program's own architecture.**

**THE SPEC ALREADY SAYS IT** (`:64-67`):

```text
a completed Gamma_K with a unique simple positive C_record root would determine K_*
conditionally on the induced-only axiom, not absolutely
```

**"Conditionally, not absolutely" is Q-65's "conditional derivation, singly-attested" — written a day
before Einstein derived the grading.**

*** AND §5.3 IS A COMPLETE UNIQUENESS GATE, WITH ANTI-FITTING BUILT IN: *** it passes only on "one simple
positive root and no inequivalent admitted positive root or continuous modulus," and **fails if existence
is shown without uniqueness, if a continuous family survives, if a second inequivalent positive root
survives, or *** IF UNIQUENESS IS OBTAINED ONLY BY NARROWING THE ADMITTED FAMILY AFTER SEEING THE ROOT
***." **That last clause is target-fitting, forbidden by name.** And "the root is then solved once and
independently reproduced" **is freeze-before-root-finding — which Einstein independently named a keystone
in Q-65.**

*** REVIEWER CORRECTION, SAME DAY: THE FLAG NAMED HERE WAS THE WRONG OBJECT. *** The entry first cited
`constant_root_uniqueness_derived = false` as the threshold's open obligation. **It is not.** It lives in
`R3_4_CAUSAL_DIAMOND_SPECTRAL_PULLBACK_RESULT_V001.md:119` and refers to **"uniqueness of the CONSTANT ROOT
PREPARATION against all admitted preparation sectors"** (`:98`) — **a source-STATE selection question**,
where "constant root" is the normalized null-shell preparation on the causal diamond. **It is a different
object from the `C_record(K) = 0` threshold root.** *** THE REVIEWER MATCHED ON THE WORD "root." THAT IS
THE EXACT FAILURE MODE THIS PROGRAM HAS HAD AT LEAST TEN TIMES, COMMITTED IN THE REGISTER ITSELF. ***

**THE THRESHOLD'S ACTUAL OBLIGATIONS ARE TWO, BOTH IN THE `Gamma_K` SPEC:** `root_solved = false` (`:671`),
gated by **§5.3's uniqueness gate** — which requires **one simple positive root, no inequivalent admitted
positive root, no continuous modulus**, and forbids obtaining uniqueness by narrowing the admitted family
after seeing the root. **Neither existence nor uniqueness is earned.**

**The R3.4 preparation-uniqueness obligation is REAL and remains open — it is simply a different
obligation, sitting on the source-state side rather than the threshold side.**

*** SO THE PAIR-HUNT WAS A DETOUR. *** Q-61 surveyed the corpus for pairs, found zero live, and the
reviewer treated that as the route being empty. **It was the wrong route. The program's route to a forced
number is: complete `Gamma_K` → run the §5.3 uniqueness gate → a derived unique simple positive root forces
`K_*` conditionally on the induced-only axiom.** **This is the same failure pattern as every correspondence
error in this program — the missing thing already existed — except that this time what already existed was
the METHOD.**

**CURRENT LANE ASSIGNMENTS ARE VINDICATED, NOT REDIRECTED.** Codex 2's package work heads the critical path
to a completed `Gamma_K`, which is exactly what the uniqueness gate needs. **What changes is what the work
is FOR: not assembling a second leg, but earning existence and uniqueness of one root.**

*** WHAT WOULD STILL KILL IT: uniqueness ADOPTED rather than derived. Q-65 requires both existence and
uniqueness to be DERIVED. An adopted uniqueness is a fit wearing a threshold's clothes, and §5.3 already
forbids the specific form of that error. ***

---

## Q-72. "Do the 13 JSON authority ledgers contradict anything?"

**RULING: NO. THE SCOPE HOLE IS CLOSED AND NOTHING CHANGES.** Established 2026-07-31 by Codex lane 1 under
relay 170 (`STAGE8_JSON_AUTHORITY_LEDGER_SWEEP_V001.md`, `5f2390f9…`, archive `8f5dc5e`, gate GREEN).

**Exactly 13 ledgers, `CURRENT_AUTHORITY_LEDGER_V001.json` through `V013.json`.** They assert authority
tuples, current/superseded results, Level-1 postulates, execution and protected flags, subordinate result
bindings, and external-route audit status. **Protected flags remain false where expected; no
`authorized = true`, no `computed = true`, no alpha, `kappa_record` or `kappa_Thomson` computation
anywhere.**

**No substantive JSON-vs-Markdown contradiction.** Raw candidates were typed `false | TYPE-S` — guard
examples, hypothetical "would refute if true" text, or the axiom-versus-theorem distinction already
reflected in V011/V013. **`ledger_construction_dependency_edge_found = false | TYPE-S`, so the Q-64 graph
gains no nodes or edges and the acyclicity verdict is unaffected.**

*** REVIEWER CORRECTION, SAME DAY: THIS ENTRY WAS UNDER-REGISTERED. THE LANE'S HEADLINE WAS "NO
CONTRADICTION"; ITS FLAG BLOCK SAYS MORE, AND THE REVIEWER REGISTERED THE HEADLINE. *** Caught by Einstein
under relay 169. The artifact's own flags (`:355-363`):

```text
ledger_derived_ground_exists_locally        = true
ledger_authority_edges_exist                = true
dependency_graph_needs_authority-edge_decision = true
```

**And its own prose (`:366-369`):** the program "has been **under-reporting what the JSON layer
contains**: local derived flags, Level-1 postulate leaves, V013's rejection of V012, and
**authority/result-binding edges that no markdown-only dependency walk can see.**"

*** SO TWO THINGS FOLLOW THAT THIS ENTRY ORIGINALLY DENIED. (1) THE FIRST-FLOOR QUESTION REOPENS IN THE
LEDGERS — `ledger_derived_ground_exists_locally = true` means derived ground may exist where no markdown
audit counts it. (2) AUTHORITY EDGES EXIST AND THE DEPENDENCY GRAPH NEEDS A DECISION ABOUT THEM — which is
the same defect relay 172 is extracting for prose and flags, in a third syntactic form. ***

**`ledger_construction_dependency_edge_found = false` stands** — no CONSTRUCTION edges. **Authority edges
are a different kind and were never denied.**

**REVIEWER PATTERN, SECOND INSTANCE TODAY:** Q-60's answer was also inside an artifact and absent from its
summary. *** READ THE ARTIFACT, NOT THE REPORT. ***

---

## Q-73. "Does issue 1's output feed issue 2's equation?"

*** RULING: YES, AND THE CONNECTOR IS A THIRD MISSING BRIDGE THAT THE DEPENDENCY GRAPH COULD NOT SEE. ***
`T_R_and_k_R_have_derived_bridge = false`. Established 2026-07-31 from the principal's observation that a
dependency was being asserted which no artifact states.

**THE SEALED PROSE STATES THE COUPLING** (`STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:64-67`): the closure
residual is built from an action carrying the `A_4` logarithm, **"so `k_R` — the floor — appears in the
equation that fixes `K_*`."** *** A LOGARITHM NEEDS A REFERENCE SCALE. So a scale-side quantity sits inside
the equation whose root is the coupling. ***

**AND THE CONNECTOR IS NAMED AND UNDERIVED:** `T_R_and_k_R_have_derived_bridge = false`. `T_R` is what
`C_R = 1` would select on the scale side (issue 1); `k_R` is the floor appearing in the `K_*` equation
(issue 2); **the bridge between them does not exist.** The proper-time floor is `s = 1/k_R^2`.

*** SO THERE ARE THREE MISSING BRIDGES, NOT TWO: *** (1) the Hamilton-Jacobi scale bridge, six objects,
which would let `C_R = 1` select; (2) the response-extraction layer, which would give `C_record(K)` a
function to have a root; **and (3) the `T_R`-to-`k_R` bridge, which would connect the selected scale to the
equation that fixes the coupling.**

*** THIS CORRECTS Q-64's "TWO DISJOINT CRITICAL PATHS." *** They share zero nodes **on stated `would-build`
edges** — Einstein typed that precisely and warned it proved nobody had STATED a shared prerequisite, not
that the physics was independent. **The physics is not independent, and the corpus says so in a status flag
and in prose. The census could not see either, because it walked only `would-build` fields.**

**METHODOLOGICAL DEFECT, GENERAL:** *** THE DEPENDENCY GRAPH CAPTURES ONLY DEPENDENCIES EXPRESSED IN ONE
SYNTACTIC FORM. *** Real dependencies also live in prose ("X appears in the equation that fixes Y") and in
`*_have_derived_bridge = false` flags. **Any claim of parallelism between chains is unsafe until those are
extracted.**

**REVIEWER NOTE:** the reviewer asserted this coupling before checking it and was right by luck, not by
evidence. **The principal asked for the artifact that states the dependency; there is one, and it is
stronger than the assertion was.**

---

## Q-74. "Is the boundary axioms or debts?"

*** RULING: THE AXIOM FLOOR IS REAL, SMALL AND CLEAN — AND EVERY ADOPTION THE VALUE PATH TOUCHES IS
DEBT-IN-AXIOM-CLOTHING, 8 OF 8. THE CLOTHING DOES NOT SCATTER; IT SITS EXACTLY WHERE ALPHA WOULD COME
FROM. *** Established 2026-07-31 by Einstein under relay 169
(`STAGE8_BOUNDARY_LEAF_TYPING_AXIOMS_VS_DEBTS_EINSTEIN_V001.md`, archive `5648297`, gate GREEN, seal
verified).

```text
AXIOM 18  ·  CLOTHING 8  ·  DEBT ~64  ·  NO_VERDICT 66
```

**THE EIGHT CLOTHED ADOPTIONS:** the only absolute-scale selector; the floor unit; the write amplitude; the
stiffness zero; the grading; the crossed-product exclusion; the write-admissibility law; the sector functor.
*** EACH IS AN ADOPTION THE CORPUS'S OWN TEXT SAYS WAS OWED AS A DERIVATION. ***

**THE FLOOR IS BETTER THAN THE REGISTER RECORDED.** The 18 axioms are **few, motivated, target-blind,
several with frozen falsifiers, and NONE carries absolute scale.** *** THE ONE SCALE-CARRYING LEAF IS THE
`C_R = 1` MARGINALITY NODE — AND IT IS CLOTHING, its own release reading "derives, rather than assumes, the
marginal closure condition." *** **Q-45's untested rows concentrate in the CLOTHING set, not the axiom
set.**

**NOT NEARLY FOUNDED, BUT NOT AXIOM-ROTTEN.** Debts outnumber axioms **3.5:1** and **the floor's
value-bearing edge is 100% clothed** — but the debt mass is **one ordered ladder and one package interior,
not scattered wishes.** **The debt is mostly QUEUE, not wish:** ~13 `would-build`s name existing sealed
specs or objects — including P8's pair, **the only debt touching a sealed derived object** (Q-68's
near-floor), and the scalar bridge, an execution path over existing specs; ~14 are ladder rungs behind
now-specified S1; ~10-12 are wishes as posed — *** and the wish set contains exactly the two proofs the
clothing set needs. ***

*** THE TWO QUESTIONS COINCIDE, AND MORE EXACTLY THAN THE REVIEWER SUSPECTED: "IS THERE A FLOOR?" AND
"WOULD A COMPUTED ALPHA BE A DERIVATION?" MEET ON THE CLOTHING SET. *** Clearing those eight is
**simultaneously** what makes the floor real and what lifts Q-65's grade off its ceiling. **Today a
computed alpha would be conditional on eight adoptions the corpus itself says were owed as derivations.**
The questions differ only by the process certificates a derivation needs on top of a clean floor. **ONE
WORKSTREAM, TWO EXIT CRITERIA.**

**THREE DEFECTS OWNED, TWO OF THEM EINSTEIN'S OWN.** (1) Its earlier boundary walk **recorded counts where
it owed names** — the 64-member roster is unenumerated, ~42 slots unrecoverable, **escalated**. (2) Its
direct read typed `K_bare = 0` as AXIOM and **the sealed release defeats it** — the falsifier tests the
adoption, the release says a derivation is owed; **both recorded, unmerged.** (3) One Q-69-barred
flag/object identification inside its own workflow output, **caught by its verifier and flipped**, with the
clothing finding relocated to its true bearer rather than lost.

**N-LEDGER, AND IT REOPENS A CLOSED QUESTION:** this typing is `.md`-scoped, and Codex 1's
`ledger_derived_ground_exists_locally = true` means **the JSON ledgers may carry floor this classification
does not count.** *** THE FIRST-FLOOR QUESTION REOPENS THERE. *** See the Q-72 correction.

---

## Q-75. "Do the three chains separate?"

*** RULING: NO. `three_chains_still_separate = false | TYPE-R` — AN EXECUTED REFUTATION. AND Q-64's
122-EDGE GRAPH WAS A SERIOUS UNDERCOUNT: AT LEAST 41 MISSED EDGES, ~25.2% OF THE ENLARGED GRAPH. ***
Established 2026-07-31 by Codex lane 1 under relay 172
(`STAGE8_PROSE_FLAG_DEPENDENCY_EXTRACTION_V001.md`, `c2b1d21c…`, archive `db1b234`, gate GREEN).

**THE CHAINS CONNECT THROUGH THE `T_R -> k_R` MISSING BRIDGE AND THE PROSE EDGE WHERE `k_R` APPEARS IN THE
EQUATION FIXING `K_*`.** The Hamilton-Jacobi scale bridge and the response-extraction path are **not**
independent. **Q-73's single example generalized.**

*** THE REVIEWER'S PARALLELISM CLAIM IS NOW REFUTED BY EXECUTED TEST, NOT MERELY DOUBTED. *** It was made
on Q-64's zero-shared-nodes finding **while Einstein's own artifact warned in the same breath that this
proved nobody had STATED a shared prerequisite, not that the physics was independent.** **The schedule
survived by luck — both chains needed doing regardless — but the reasoning was wrong, and the live risk was
declaring one path complete on its own.**

**NO CYCLE IN THE ENLARGED GRAPH:** `enlarged_graph_cycle_found = false | TYPE-R`, **with
test/would-execute edges and Q-69-prohibited flag/discharge merges held out by kind.** The acyclicity
result survives a 25% larger graph, which strengthens it.

**EXACT COUNT IS `NO_VERDICT`, AND THE REASON IS A REPRODUCIBILITY DEFECT WORTH FIXING:** *** Q-64's
COMPLETE MACHINE-READABLE EDGE TABLE WAS NEVER COMMITTED AS A STANDALONE EDGE LIST *** (`:77`), so the
census's graph **cannot be exactly reproduced or diffed against.** The second prerequisite is an
adjudication rule for whether each remaining prose candidate is direction-bearing — **a principal or lane
rule, not a lane's to invent.**

**METHODOLOGICAL CONFIRMATION:** Q-73 recorded that the graph captures dependencies in one syntactic form
only, and warned no parallelism claim was safe until the others were extracted. **A quarter of the graph
was missing. The warning was proportionate.**

**PROCESS NOTE, CORRECT BEHAVIOUR:** relay 173 and Q-74 landed mid-run; the lane checked them, found they
did not change its extraction rules, **did not execute another lane's relay**, and reported the fact.
Codex 2's B0 files were untracked in the shared tree and **left unread because B0 was off-limits.**

---

## Q-76. "Should S9-A keep demanding overdetermination?"

*** RULING: NO. "AND OVERDETERMINED" IS STRUCK. S9-A NOW READS: determination of the total physical
stiffness by a condition whose EXISTENCE AND UNIQUENESS ARE BOTH DERIVED. *** Principal act 2026-07-31,
`S9A_AMENDMENT_THRESHOLD_FORCING_DECISION_2026-07-31_V001.md`. **Amends the obligation; does not edit the
sealed registration record** (`STAGE8_Q13_Q19_GOVERNING_REGISTRATION_RECORD_V001.md:287-288`).

**INHERITED ERROR, NOT A DELIBERATE BAR.** The wording was written while "only overdetermination forces a
number" was believed; **Q-65 refuted that.** Nothing in its registration gives a rationale for the stronger
demand.

*** AND IT WAS ACTIVELY HARMFUL: Q-61 FOUND ZERO LIVE PAIRS, SO S9-A AS WRITTEN WAS PRESENTLY
UNSATISFIABLE. ANY LANE TOLD TO DISCHARGE IT WOULD HUNT FOR A PAIR — THE EXACT DETOUR THE PROGRAM ALREADY
TOOK ONCE, SEALED INTO AN OBLIGATION WHERE IT WOULD HAVE REPEATED ITSELF WITHOUT ANYONE CHOOSING IT. ***

**THE PRINCIPAL'S GROUNDS:** the whole program is rooted in **thresholds**. Q-71 established the forcing
shape is the threshold and §5.3 is already a complete uniqueness gate for it. **In a threshold-rooted
architecture overdetermination is not a higher grade waiting to be reached — it is a category that does not
naturally arise.**

*** OVERDETERMINATION IS NOT RETAINED AS AN AVAILABLE STRONGER GRADE TO PURSUE. Holding it open as an
aspiration is what sent lanes at an empty route. It is not a target, not a bonus, not a fallback. ***

**ONE THING IS RECORDED INSTEAD, AS A DISCLOSURE RATHER THAN A GOAL.** Q-65 established exactly what
redundancy alone supplies: **corroboration against a WRONG condition — error-risk, not fit-risk.** *** THE
THRESHOLD ROUTE CANNOT SELF-CHECK THIS. §5.3's "solved once and independently reproduced" catches
computational and implementation error; IT CANNOT CATCH THE CONDITION ITSELF BEING PHYSICALLY WRONG,
BECAUSE THERE IS NOTHING TO DISAGREE WITH IT. ***

```text
S9A_RESIDUAL_ERROR_RISK_DISCLOSED = true
S9A_RESIDUAL_ERROR_RISK_CLOSED    = false | TYPE-C
    constraint: no second independent condition exists in the corpus (Q-61)
    release:    an independently-motivated second condition landing on the same quantity
```

**ANY REPORTED ALPHA MUST CARRY THAT DISCLOSURE.** A derivation forced by one derived unique condition is
genuine and **singly-attested**; if that condition is wrong rather than merely unproven, **nothing in this
route detects it.**

**THE STANDARD IS NOT RELAXED.** Q-65's certificates, freeze-before-root-finding, the target-entry sweep,
and §5.3's prohibition on narrowing the admitted family after seeing the root all stand. *** A DEMAND THAT
WAS NEVER REQUIRED IS WITHDRAWN, AND THE COST OF WITHDRAWING IT IS DISCLOSED. *** **S9-A remains open.**

---

## Q-77. "There are `derived = true` flags outside the cleanroom, and no audit has ever counted them."

*** FINDING, NOT A RULING. STATUS UNDETERMINED AND URGENT. *** Found 2026-07-31 by the reviewer while
reading Codex 2's B0 artifact (`ec848d29…`) rather than its report — **the artifact quoted a source the
report did not mention.**

`primitive_complete_boundary_transition_functional_principle_v002.md:120-126`, **at the PROGRAM ROOT,
OUTSIDE the cleanroom**, carries:

```text
complete_boundary_ctp_functional_derived = true
primitive_phase_record_map_derived       = true
complete_transfer_operator_constructed   = false
stationary_record_cell_derived           = false
microscopic_transverse_Hessian_computed  = false
physical_thomson_alpha_computed          = false
alpha_computed                           = false
```

*** AND THE CLAIMS IMMEDIATELY ABOVE THOSE FLAGS ARE THE THINGS THE CLEANROOM SAYS ARE MISSING: *** (1)
`U_BR`, `rho_pre` and every admitted record effect follow from **one complete microscopic operator**; (2)
**the mixed response kernel, noise kernel and first-record overlap are DERIVED from that same functional** —
which is the response-extraction layer's content; (3) the stationary proper interval and source threshold
are **outputs rather than units or regulators**; (4) *** THE FIRST POSITIVE CLOSURE ROOT IS SIMPLE AND
UNIQUE UNDER EVERY ADMITTED TARGET-INDEPENDENT MUTATION *** — which is the §5.3 uniqueness gate's content;
(5) threshold and renormalization matching connect `K_micro` to Thomson alpha.

*** WHAT IS NOT ESTABLISHED, AND MUST NOT BE ASSUMED: WHETHER THIS IS GENUINE DERIVED GROUND OR A PRINCIPLE
ASSERTING ITS OWN CONSEQUENCES. *** The filename says **principle**, and in this corpus "principle"
conventionally means an **adopted Level-1 rule, not a theorem.** **A `derived = true` flag inside a
principle document may record a derivation or may record the principle's own claim about itself.** *** THAT
IS EXACTLY THE DEBT-IN-AXIOM-CLOTHING PATTERN — OR ITS EXACT REVERSE, REAL DERIVED GROUND SITTING OUTSIDE
THE FENCE. THE TWO READINGS HAVE OPPOSITE CONSEQUENCES AND THE REVIEWER CANNOT ADJUDICATE THEM. ***

**WHY NO AUDIT SAW IT.** Q-64's census, Q-74's boundary typing, the premise classification and the
`untyped_negative` gate are **all cleanroom-scoped**. The cleanroom is roughly 1,138 of ~7,425 program
files. *** EVERY "NO CHAIN REACHES DERIVED GROUND" FINDING IN THIS REGISTER IS SCOPED TO ~15% OF THE
PROGRAM, AND THE REGISTER HAS NOT BEEN SAYING SO. ***

**FENCE POSITION:** reading this to establish what it says is permitted — **Q-48 (fences ban entry, not
comparison) and Q-52 (no constraint may prevent a test).** *** IMPORTING ITS CONTENT INTO CONSTRUCTION IS
NOT PERMITTED and no such import has occurred. ***

**IF IT IS DERIVED GROUND:** the first floor exists, the response layer may be less missing than Q-51
recorded, and root uniqueness may already have a claim. **IF IT IS A PRINCIPLE ASSERTING ITS OWN
CONSEQUENCES:** it is a large clothing instance outside the boundary Einstein typed, and the eight becomes
more than eight.

**QUEUED FOR ADJUDICATION. NO FLAG MOVES ON THIS ENTRY.**

---

## Q-78. "What would discharge the eight?"

*** RULING: NONE IS DISCHARGEABLE TODAY, AND ONE OBJECT DOMINATES — THE COMPLETED SOURCE-RECORD-FIELD CTP
PRODUCER ALGEBRA. *** Established 2026-07-31 by Einstein under relay 173
(`STAGE8_CLOTHING_DISCHARGE_CONDITIONS_AND_LEDGER_FLOOR_EINSTEIN_V001.md`, archive `ee345fe`, gate GREEN,
seal verified). **Owed wording quoted verbatim and character-exact-verified in every row.**

*** RANK 1: THE COMPLETED SOURCE-RECORD-FIELD CTP PRODUCER ALGEBRA. *** It is **the only object literally
named by any instance's release** — instance 5's, *"a derivation of the completed source-record-field
algebra forcing this grading."* **It discharges instance 6 as a corollary and advances 7, 8, 3, and weakly
4.** The shared-object hypothesis **survived adversarial verification in weakened, exact form** — 6 by
corollary, 8 adjacently, 7 via its dynamics component, **never by name-matching.** Its construction is
extension-typed **NOT_SPECIFIED with a named obstruction.** **And Q-74's two wish-grade proofs — the
grading-forcing derivation and the crossed-product exclusion — serve instances 5 and 6, both rooted in that
same algebra.**

**INSTANCE 1 (`C_R = 1`) IS THE OTHER WORKSTREAM.** It discharges **none** of the other seven —
`[C_R, tau]` independent, no sealed relation to 3 or 4 — **but it clears the ladder head dominating the
~64-debt mass: maximum debt movement, zero clothing movement.** *** AND IT IS THE MOST REACHABLE OF THE
EIGHT: queue-grade, sealed order, and S1's two Q-52 specs already exist. *** **The selector and the algebra
are separate workstreams, exactly as the census's disjoint critical paths predicted.**

*** INSTANCE 2 (`tau = 1`) IS THE PROGRAM'S STARKEST SPECIFICATION HOLE: THE CORPUS NAMES NO DISCHARGE
ROUTE AT ALL — BELOW WISH-GRADE, since a wish at least has a `would-build`. *** The corpus states the
negative itself: *"No test selects the unit member."* **A discharge object — a selection theorem over
V011's admitted positive-`tau` family — is Q-52-declared for the first time in this artifact,
`derived = false`.**

**Instance 4's frozen falsifier exists but only tests the ADOPTION — the falsifier is not the discharge
object.** **Q-69 held: both verifiers audited every row for exactly that identification and found no
violation anywhere.**

**ITEM 2 — THE FIRST-FLOOR QUESTION CLOSES NEGATIVE IN THE JSON LAYER.** All 13 ledgers read in full.
`ledger_derived_ground_exists_locally = true` **survives, but every derived entry is relative/structural,
supplied-input-conditional, a derived no-go, or process/tooling — each with a same-file FALSE continuation
flag between it and the value path.** **No value-path terminus flag is true anywhere, and word-boundaried
search for the eight instances' tokens returns ZERO hits: the ledgers neither name, clothe, nor discharge
any of them.**

**TWO POSITIVES FROM THE LEDGERS.** (1) *** THEY PRACTISE EXACTLY THE COMPANION-NEGATIVE DISCIPLINE THE
CLOTHING CLASS LACKS — A READY-MADE TEMPLATE. *** (2) V013's rejection of V012 on **pure process-integrity
grounds** proves **ledger ground is defeasible custody**, so *** DISCHARGE CONDITIONS MUST BIND TO
DERIVATION OBJECTS, NEVER TO LEDGER STATE. *** **This bears directly on Q-77.**

**ITEM 3 — THE ROSTER IS PAID IN FULL.** *** ALL 64 DEBTS NAMED: response 39 (three edge classes),
selector 10, write 13, fourth-horn 1 (`connected_cross_cell_terms_derived`) *** — each with a sealed-text
edge citation making it independently verifiable, two largest blocks spot-checked verbatim at source. **The
"~42 unrecoverable" was true of sealed text; the overnight session record held the enumeration. The
register may now cite 64 as an actual work list.**

---

## Q-79. "Do the reviewer's two graph rules survive testing?"

*** RULING: BOTH ARE PARTLY REFUTED, AND THE PROSE RULE IS REFUTED BY ITS OWN MOTIVATING EXAMPLE. ***
Established 2026-07-31 by Codex lane 1 under relay 174
(`STAGE8_GRAPH_RULE_TESTS_AUTHORITY_AND_PROSE_V001.md`, `1fcedc16…`, archive `1f53450`, gate GREEN).

**TEST 1 — THE CYCLE RATIONALE IS DEAD.** 333 authority edges extracted from all 13 ledgers, merged with
283 reconstructed current-state `would-build` edges plus 4 bridge/prose edges. **Tarjan: ZERO CYCLES.**

```text
authority_cycle_manufacture_rationale_holds = false | TYPE-R
```

*** THE REVIEWER ARGUED THAT MERGING A FORWARD-ACYCLIC "REQUIRES" RELATION WITH A BACKWARD-POINTING
"OBSOLETES" RELATION MANUFACTURES CYCLES. IT DOES NOT — MEASURED, NOT ARGUED. *** **The semantic case for
separation survives; the empirical case is gone, and the decision now rests on semantics alone.**

*** TEST 2 — PRECISION 1.000, RECALL 0.641, AND THE RULE MISSES ITS OWN EXEMPLAR. *** 1626 candidate
sentence units, deterministic sample of 80.

```text
prose_rule_low_precision            = false | TYPE-R
prose_rule_low_recall               = true  | TYPE-R
exemplar_caught_by_rule_as_written  = false | TYPE-R
```

**The rule misses `k_R -> K_*` because the sentence says `k_R` APPEARS IN the equation fixing `K_*`, not
that `k_R` must EXIST OR BE DETERMINED BEFORE `K_*`.** *** THE REVIEWER FLAGGED THIS EXACT RISK WHEN
PROPOSING THE RULE AND IT CAME TRUE. A RULE THAT MISSES THE CASE THAT MOTIVATED IT IS REFUTED BY ITS OWN
ORIGIN. *** **Perfect precision means nothing it caught was wrong; 36% of real dependencies were missed.**

**ALSO ESTABLISHED:** `q64_original_exact_edge_table_found = false | TYPE-S` — **the original table does
not exist and never did.** Codex 1 reconstructed **283 current-state edges**, and **a standalone
machine-readable edge table is now committed**, closing the Q-75 reproducibility defect.

---

## Q-80. "How should lanes handle findings that fit no existing category?"

*** RULING: NAME A NEW CLASS. DO NOT FORCE, DO NOT REPORT AS A DEFECT, DO NOT DISPOSE OF IT WITH
`NO_VERDICT`. A CATEGORY THAT HAD TO BE INVENTED IS A FINDING. *** Principal direction 2026-07-31 —
*"Toto, I've a feeling we're not in Kansas anymore."* Recorded as
`NEW_TERRITORY_STANDING_CLAUSE_2026-07-31_V001.md`; **included verbatim in every relay from 176 onward.**

*** THE EVIDENCE IS THREE IMPORTED FRAMINGS FAILING IN ONE DAY, ALL THREE THE REVIEWER'S: *** "only
overdetermination forces a number" (Q-65, **false**, and it had directed lane assignments for days); "no
chain reaches derived ground" reported as a defect (Q-70, **a category mistake** — a well-founded theory
bottoms out in axioms, **and the register reported it three times as a finding**); and "two disjoint
critical paths" (Q-75, **refuted by test** after a quarter of the graph turned out to be missing).

*** IN EVERY CASE THE FIX WAS NOT BETTER CLASSIFICATION — IT WAS INVENTING A CATEGORY. ***
"Debt-in-axiom-clothing" did not exist until Einstein needed it, **and it immediately located the whole
problem.** `PATHLESS-CLAIMED` is a class the register still has no name for.

**THE OPERATIVE DISTINCTION, WHICH LANES MUST NOT CONFLATE:** `NO_VERDICT` means **information is
missing**; a **NEW CLASS** means **the categories are wrong.** **Absence of a fit is evidence about the
OBJECT, not about the analysis.** **And imported standards now get the same scrutiny as corpus claims — if
a framing came from mathematics, ordinary physics practice, or software engineering, the lane must say so
and say why it applies here.**

*** WHAT IT DOES NOT LICENSE: inventing a category to escape an inconvenient verdict. A new class must be
DEFINED, must say what it EXCLUDES, and must be FALSIFIABLE in the Q-54 sense — an object must be able to
fail to belong to it. It relaxes no fence, no typing rule, and no testability requirement. AND "THIS IS NEW
TERRITORY" IS NEVER A REASON A RESULT IS RIGHT — it is a reason to check whether the QUESTION is well-posed
before answering it. ***

**THE REVIEWER IS BOUND TOO, AND MOST OF ALL: all three failures were his, one registered three times
before the principal caught it. The clause applies to his framings, register entries and relay questions —
especially when a question seems obvious. Q-70's malformed floor question seemed obvious for two days.**

---

## Q-81. "What kind of object is the rank-1 producer algebra?"

*** RULING: IT IS NOT AN EXTENSION AT ALL. `pure_algebraic_extension_class_sufficient_for_rank1_object =
false | TYPE-R` — AN EXECUTED REFUTATION. A NEW CLASS WAS REQUIRED AND IS NAMED:
`COMMON_ORIGIN_CTP_PRODUCER_ALGEBRA`. *** Established 2026-07-31 by Codex lane 1 under relay 176
(`STAGE8_RANK1_CTP_PRODUCER_ALGEBRA_Q52_SPEC_V001.md`, `e191d379…`, archive `ea947e6`, gate GREEN).

*** THIS IS Q-80's FIRST USE AND IT FIRED CORRECTLY. *** The lane declined to force the object into
tensor / crossed-product / direct-limit / C*-extension language and **named a class instead.**

**THE NEW CLASS:** one microscopic source-record-field CTP producer package carrying, **from a common
origin**, the algebraic carrier, the source and record embeddings, the quotient and measure, `rho_pre`,
effects and domains, dynamics, and the raw contour-correlator interface.

**WHAT IT RESISTS ABOUT THE OLD CLASSES, IN THE LANE'S WORDS:** *"the old classes can classify how algebras
are joined, but they do not by themselves supply `rho_pre`, record effects, the physical quotient, the
invariant contour/spacetime measure, common domains, CTP branch data, or the source-record-field
dynamics."* *** "A PURE TENSOR/CROSSED/DIRECT-LIMIT ANSWER CAN THEREFORE PASS AN ALGEBRAIC RELATION TEST
WHILE STILL FAILING THE PRODUCER OBLIGATION." ***

**AND IT IS PROPERLY CONSTITUTED UNDER Q-80: "a new class, not a relaxation," falsifiable — a candidate
fails it by lacking any required common-origin component or by failing its tests.**

*** SO A FOURTH IMPORTED FRAMING HAS FAILED. *** For two days this was posed as an **extension problem** —
Q-42 asked which extension type, Q-43 answered "graded tensor product at base level," Q-50 and Q-51 chased
the layer. **The full object is none of them.** **The question "which extension is it?" was malformed, in
exactly the way Q-70's floor question was malformed**, and Q-80 caught it on first application.

**SPECIFIED, NOT CONSTRUCTED:** premises P0-P7, `derived = false`, with failure-capable tests T1-T7 —
source compatibility, record compatibility, CTP/field signature, common-origin state and effects,
dynamics/normalization, raw-output interface, and **new-class membership.**

*** AND IT WEAKENED EINSTEIN'S Q-78 RANKING, AS INSTRUCTED. *** Q-78 claimed the rank-1 object "advances 7,
8, 3, and weakly 4." **Codex 1 reports instance 5 directly, instance 6 as a corollary, and instances 3, 4,
7, 8 ONLY AT INTERFACE LEVEL**, with 1 and 2 not advanced. **The relay told it to disagree with the ranking
if the evidence said so, and it did.** **The dominance claim survives in reduced form.**

**THE FIVE-SPELLINGS `NO_VERDICT` IS PRESERVED, NOT MERGED** (Q-78 N5). The working spelling is recorded
and **Q-69 held.**

---

## Q-83. "What is actually on the road to alpha?"

*** RULING: THREE STEPS. NOTHING ELSE IS ON IT. NO RELAY IS ISSUED UNLESS IT NAMES WHICH STEP IT ADVANCES.
*** Principal direction 2026-07-31 — *"laser focused on the path to compute alpha."* Recorded as
`ROAD_FOCUS_RULE_2026-07-31_V001.md`, effective relay 183.

```text
STEP 1   C_record(K) EVALUABLE   the loop-closing map / response-extraction layer
STEP 2   THE SCALE FIXED         C_R = 1 selects, via the Hamilton-Jacobi bridge;
                                 k_R sits INSIDE step 1's equation (Q-73)
STEP 3   RUN SECTION 5.3         the uniqueness gate, ALREADY WRITTEN
```

**Legitimate relay justifications: `ADVANCES STEP 1/2/3`, or `UNBLOCKS` — which must name the step and the
specific blockage.** *** "IT WOULD BE GOOD TO KNOW" IS NOT AN UNBLOCK. THE REVIEWER IS BOUND BY THIS BEFORE
ANY LANE IS. ***

**PARKED, NOT ABANDONED:** the 32 `PATHLESS-CLAIMED` inventory (relay 181, written and held); the canonical
identifier registry and four alias `NO_VERDICT`s; the authority-edge modelling decision; the
prose-extraction rule amendment; boundary re-typing beyond what a step needs; OBS-08 and the graph-model
question. *** A PARKED ITEM IS UNPARKED ONLY BY SHOWING IT BLOCKS A STEP. ***

**THE HONEST ACCOUNTING:** *** A LARGE FRACTION OF 2026-07-30 AND 07-31 MEASURED THE PROGRAM RATHER THAN
BUILDING IT. *** That was necessary — the blocker was unknown, and the road could not have been stated in
three lines without it. **The measurement phase is finished, not wasted.**

*** AND THE SHARPENING EXPOSES A QUESTION NOBODY HAS ASKED. *** Q-81 found the rank-1 object advances
instances 5 and 6 substantively and **3, 4, 7, 8 only at interface level.** Instances 1 and 2 are the scale
side. **So: DO 3, 4, 7 AND 8 ACTUALLY BLOCK A STEP, OR ONLY DEGRADE THE CONDITIONALITY OF THE RESULT?** **If
they do not block, they are not road work — they are DISCLOSURE work, and disclosure can be written at the
end.** **One lane's question, and it would cut the work list roughly in half.**

**NOTHING IS RELAXED.** Q-52, Q-54, Q-69, Q-76, Q-80, the `sqrt(2)` prohibition and §5.3's ban on narrowing
the admitted family all stand. *** FOCUS IS NOT SPEED. A STEP TAKEN WRONGLY IS NOT PROGRESS ALONG THE ROAD;
IT IS A FIT. ***

---

## Q-84. "Does the `tau = 1` pin collapse?"

*** RULING: `NO_VERDICT` — NOT COLLAPSE. THE COLLAPSE CONDITION CONCERNS A DIFFERENT OPERATOR THAN THE ONE
THE PROGRAM WOULD HAVE REACHED FOR. *** Established 2026-07-31 by Codex lane 1 under relay 180
(`STAGE8_TAU_PIN_SPECTRAL_COLLAPSE_CHECK_V001.md`, `3779535a…`, archive `85df3cd`, gate GREEN).

**The collapse condition concerns the complete public capacity operator `D_BR^2` / complete normalized
`L_BR`** — with `lambda_0(D_BR^2) = k_R^2` and `lambda_1(D_BR^2) > k_R^2`, the isolated-lowest-eigenspace
structure that pins `k_R` — **NOT the Q-47 source-record non-return Hamiltonian.**

*** Q-47's ABSOLUTELY CONTINUOUS SPECTRUM RESULT IS REAL AND TYPES TO THE WRONG OPERATOR. *** The relay
warned *"do not assume it is the one you expect"* and the lane checked rather than assumed.
`q47_nonreturn_spectrum_identified_with_capacity_spectrum = false | TYPE-S`, scope recorded. **This is the
name-match trap for the fourth time in three days — corpus, audit script, audit of the audit, register —
and the first time it was caught before it produced a false result rather than after.**

**SO THE EIGHT DOES NOT BECOME SEVEN.** `eight_count_reduced_by_this_check = false | TYPE-C`, release: a
derived spectral theorem for the complete public capacity operator. **`tau = 1` remains PIN-CONTINGENT
CONSEQUENTIALITY.**

*** BUT THE CHECK DID ADVANCE SOMETHING, AND IT IS THE POINT OF THE RESULT. Q-82 RECORDED `tau = 1` AS
HAVING NO DISCHARGE ROUTE AT ALL — BELOW WISH-GRADE. IT NOW HAS A NAMED `would-build`: ***

```text
complete_public_capacity_spectrum_continuous_nonisolated_bottom_derived = false | TYPE-U
    would-build: complete public D_BR / L_BR spectral theorem
complete_public_capacity_spectrum_isolated_lowest_public_eigenspace_derived = false | TYPE-U
    would-build: the same theorem with quotient trace and isolated lowest public eigenspace
```

**One named spectral theorem decides it in either direction.** *** THE SEALED CORPUS DOES NOT DECIDE
WHETHER THE CAPACITY OPERATOR HAS CONTINUOUS SPECTRUM. *** If a later result derives continuous spectrum or
a non-isolated bottom, **absorption reopens and the floor loses pin support in the `A_4`/`K_*` equation.**
**Nothing downstream collapses now.**

**ROAD STATUS (Q-83): step 2, feeding step 1's equation.** **The item is not discharged; its route is now
named where it was absent.**

---

## Q-85. "How many of the eight are road work?"

*** RULING: FOUR. INSTANCES 3, 4, 7 AND 8 ARE **DEGRADING, NOT BLOCKING** — DISCLOSURE WORK, NOT ROAD WORK.
THE ROAD IS 4 ENTRIES AND ABOUT **THREE INDEPENDENT BODIES**. *** Established 2026-07-31 by Codex lane 1
under relay 183 (`STAGE8_CLOTHING_INSTANCES_3_4_7_8_ROAD_STANDING_V001.md`, `4fa56aca…`, 498 lines).

**The relay's mapping warning was real and the lane checked it:** instances 3/4/7/8 are **ER-A amplitude,
`K_bare = 0`, projection-module retraction / write admissibility, and the sector functor.** Grading and
crossed-product exclusion are 5 and 6.

**ALL FOUR ARE DEGRADING.** *** STEP 1 CAN COMPLETE UNDER THEIR ADOPTED CONSTRAINTS; STEP 2 IS THE SCALE
SELECTOR PATH AND IS SEPARATE FROM THEM. *** **Note that `K_bare = 0` — the induced-only axiom — does not
block step 1.**

**THE CONDITIONALITY THEY ADD, WHICH MUST TRAVEL WITH ANY NUMBER (Q-76):** the ER-A envelope and S8
integrated action; induced-only `K_bare = 0` plus its mutation-exclusion debt; the adopted projection-module
retraction / write-admissibility law; the adopted strong symmetric-monoidal sector functor. **Their
grade-lift objects are named: exchange-magnitude theorem plus ER-B exclusion; induced-only
microscopic-action derivation plus pre-response mutation exclusion; projection-module
support/retraction/bimodule theorem; derived monoidal sector functor.**

*** THE ROAD, COLLAPSED TO THREE BODIES: (1) THE SCALE SELECTOR; (2) THE `tau` SPECTRAL-PIN THEOREM; (3) THE
RANK-1 PRODUCER ALGEBRA, WITH INSTANCE 6 AS A COROLLARY. ***

---

## Q-86. "Is `C_record(K)` a self-consistency residual?"

*** RULING: NO FOR `C_record` — SEALED TEXT REFUSES IT EXPLICITLY. BUT IT IS A **NEAR-MISS, NOT A FIFTH
FAILED IMPORT**: THE REVIEWER'S OBJECT EXISTS IN SEALED TEXT VERBATIM, ONE LEVEL DOWN, UNDER ITS OWN NAME.
*** Established 2026-07-31 by Einstein under relay 182
(`STAGE8_CRECORD_FIXED_POINT_READING_ATTACK_EINSTEIN_V001.md`, `d28e9291…`, seal verified).

**`C_record`'s only sealed typing is "a joint eigenvalue/boundary-value problem"** (`GAMMA_K spec:451`).
**`K` enters ONCE**, and the only concrete sealed display compares to the constant `pi`, **not to `K`**:

```text
C_record(K) = DeltaPhi[K; X_K] - pi          (scope inventory :331)
```

*** BUT THE SAME SEALED SECTION CARRIES A GENUINE K-ON-BOTH-SIDES FORM AS A DIFFERENT NAMED OBJECT: ***

```text
C_EM(K) = K - B_ind(K) = 0                   (spec:475)
```

**THE IDENTIFICATION IS FORBIDDEN AS THINGS STAND** (`:497-499` — not an "isolated scalar projection")
**AND OWED AS A DERIVATION** (`:492-493` — it fails "if merely asserted rather than recovered as a
projection of the stationary equation"). *** SEALED RELATIONSHIP: CONTAINMENT WITH AN UNDERIVED BRIDGE.
THE VERDICT EXISTS ONLY AS COINCIDE-BUT-MUST-BE-PROVEN. ***

**THE REVIEWER'S FIVE READINGS, ADJUDICATED:** (1) partially right, one level down. (2) **wrong for
`C_record`, right at `C_EM`.** (3) *** NARROWING FAILS BOTH DIRECTIONS — it is one LAYER (= step 1), not one
map: producer/package head → `G` → `E_R` → `Pi_R,ind` → `p_loc` → conditional scalar, five obligations. ***
The grain that survives: **the blocker IS localized to one nameable layer.** (4) **"The Hessian is the
stiffness" has ZERO sealed sentences** — no occurrence of "stiffness" in the 1116-line map spec; TYPE-S, not
TYPE-R, since nothing refutes a future derivation. (5) *** WRONG ON ITS PREMISE. ACYCLICITY SURVIVES
UNTOUCHED. *** The census has **no edge kind for definitional dependence**; a fixed-point equation is
**node-internal data**. **The graph reported zero ACTUAL cycles; both hazards were held-out
counterfactuals.**

**PARTIALLY RIGHT AT EXACTLY ONE LOCATION:** P7's sealed build clause **`solve dGamma_2PI/dG = 0`**
(`raw-map:48`) is **the corpus's one genuine both-sides structure — in `G`, not `K`** — and it is co-located
with the flag/discharge hazard. **R15 is not.** **Q-69 stands.** **New class PROPOSED, NOT ADOPTED:
`FIXED-POINT-NODE`; P7 instances it, `C_record` fails membership by design.**

*** AND EINSTEIN RETIRED ITS OWN NEGATIVE UNDER ITS OWN NAME: its blanket "no sealed clause puts `K` on both
sides" was FALSE, refuted by `spec:475` by its own verifier, corrected everywhere and recorded on the
artifact face. The reading was upgraded from UNLICENSED to PARTIALLY-LICENSED-AT-`C_EM`, and the import
charge downgraded to the identification only. ***

---

## Q-87. "Can the S3 join derive the energy identification?"

*** RULING: `NO_VERDICT`. S3 IS NOW FULLY SPECIFIED AS A NON-CHOOSING PROCEDURE, BUT THE CURRENT S1/S2/S4
INTERFACES CANNOT EXECUTE THE JOIN. THE FORK REMAINS OPEN AND NOTHING WAS SELECTED. *** Established
2026-07-31 by Codex lane 2 under relay 179
(`STAGE8_C_R_SELECTOR_S3_ENERGY_IDENTIFICATION_JOIN_SPEC_V001.md`, `fd157d3f…`, 1345 lines, seal verified,
publication approved by the reviewer after fence scan).

**S3's TYPE, FROM SEALED TEXT:** the proof that **the CTP branch-energy difference is the same energy
entering gravitational closure.** It must produce a common-origin certificate, a reference-fixed HJ
functional, a closure-energy functional, a full-domain functional identity, and a separately routed
classification result.

*** THE LANE REFUTED THREE UPSTREAM SPECS — TWO OF THEM ITS OWN — AND REPAIRED NONE. *** Two are
**vacuity** defects, which is the `cannot_fail` failure mode in a new costume:

```text
S1 closure-energy export not found          TYPE-S
S1 contract insufficiency                   TYPE-R   <- executed refutation
S2 lacks a nonempty-domain gate             TYPE-S
S2 constancy test admits EMPTY-DOMAIN VACUITY  TYPE-R
S4 admits an EMPTY STATIONARY DOMAIN        TYPE-S / TYPE-R
   "refutes a defect in this lane's earlier S4 specification and was not repaired"
no S2/S4 reference-application adapter      TYPE-S
```

*** A CONSTANCY PROOF THAT PASSES ON AN EMPTY DOMAIN PROVES NOTHING. BOTH DEFECTS WOULD HAVE PRODUCED A
CLEAN-LOOKING PASS. ***

**TWO Q-69-DISTINCT OBJECTS SPECIFIED**, both `derived = false | TYPE-U`:
`BRIDGE_SELECTOR_S3_HJ_CLOSURE_ENERGY_CORRESPONDENCE_CERTIFICATE` and
`S3_ENERGY_CLASSIFICATION_CERTIFICATE`. **Missing core prerequisites: P8, P10, P11; P13 supplies the
nonvacuous representation test; P9 and P12 belong only to the named-classification leg.**

*** THE NON-CHOOSING ROUTE IS NOW FULLY WRITTEN, AND THIS IS THE RESULT THAT MATTERS: ***

```text
same S1 origin -> S2 symbolic constant HJ energy -> apply S4's forced reference via P10
  -> derive closure-consumed energy via P11 -> prove full-domain functional identity
  -> validate representation invariance with P13 -> attach P9 time correspondence
  -> compare against P12's PRE-TARGET candidate signatures
```

*** EXACTLY ONE FUNCTIONAL MATCH YIELDS A NAMED IDENTIFICATION. BOTH MATCHES MEAN AMBIGUITY. ZERO MATCHES
REFUTES PAIR EXHAUSTIVENESS AND REQUIRES A CONSTITUTED Q-80 NEW-CLASS RECORD. MISSING INPUTS RETURN
`NO_VERDICT`. *** **The candidate signatures are compared PRE-TARGET — the procedure cannot pick the fork's
answer, only discover it.** **Tests T-1A through T13B are individually routed, and no test can set a derived
flag.**

**ROAD STATUS (Q-83): step 2, body 1. The route to closing the `sqrt(2)` fork by derivation now EXISTS as a
specification. It cannot run, and every blocker is named.**

---

## Q-88. "Does the sealed counting fact decide the `tau` pin?"

*** RULING: IT CONSTRAINS THE BOTTOM BUT DOES NOT DECIDE ISOLATION. `N_BR(k_R) = 1` IS CARDINALITY, NOT
CONVENTION — IT REQUIRES A ONE-DIMENSIONAL PUBLIC BOTTOM ONCE THE TRACE AND QUOTIENT ARE DERIVED. *** But
`counting_fact_decides_isolation = false | TYPE-U`. Established 2026-07-31 by Codex lane 1 under relay 185
(`STAGE8_COMPLETE_PUBLIC_DBR_LBR_SPECTRAL_THEOREM_SPEC_V001.md`, `a751b72c…`, 492 lines, seal verified,
gate GREEN).

**The sealed force, at `:85-89`:** *"`N_BR(k_R)=1` is not merely a label: the capacity principle requires
the first ... quotient Hilbert space whose lowest public eigenspace is one-dimensional."* With

```text
N_BR(k) = Tr_BR 1_[0,k^2](D_BR^2)
N_BR(k) = 0   for k < k_R
```

*** SO THE BOTTOM CARRIES EXACTLY ONE PUBLIC COUNTED MODE AT `k_R`. THAT IS A REAL CONSTRAINT AND IT WAS
SITTING IN THE CORPUS UNUSED. *** **It does not settle whether that bottom is ISOLATED, and isolation is the
whole pin.** **The would-build stands: a complete public `D_BR`/`L_BR` spectral theorem with derived
quotient trace and spectral type.**

*** AND THE ROAD STAYS PARALLEL: `spectral_theorem_depends_on_producer_algebra = false | TYPE-S`. BODY 2
DOES NOT SIT BEHIND BODY 3. *** The relay asked precisely this, warning it would make the road more
sequential than Q-85 recorded. **It does not.**

**`theorem_proof_reachable_now = false | TYPE-U`** — *** THE STATEMENT IS REACHABLE NOW; THE PROOF IS NOT.
*** The theorem can be written down today and cannot be established today, which is the honest form of a
Q-52 specification.

**The lane also confirmed the Q-84 correction independently: the theorem concerns the complete public
`D_BR^2`/`L_BR` spectrum, NOT the non-return operator.** **The operator misidentification is now checked
twice.**

**PROCESS NOTE, SHARED-TREE:** commit `e299225` auto-included the relay-186 supervision paste and rewrote
its own title; the lane did not inspect those contents. **The reviewer authored the swept-in files, so
nothing is lost — but this is the shared-index collision channel again**, and it is the third instance.
**Per-lane worktrees remain the unimplemented structural fix.**

---

## Q-89. "Is §5.3's uniqueness gate passable in principle?"

*** RULING: THE BROAD TENSION DISSOLVES — §5.3 IS **NOT** PROVEN UNPASSABLE. BUT IT IS **NOT EXECUTABLE
NOW**, AND STEP 3 IS **NOT DONE**. *** Established 2026-07-31 by Codex lane 1 under relay 187
(`STAGE8_SECTION_5_3_UNIQUENESS_GATE_PASSABILITY_DETERMINATION_V001.md`, `728543cb…`, archive `23a93c5`,
gate GREEN).

```text
Section_5_3_admitted_family_identical_to_allowance_envelope = false | TYPE-R
Section_5_3_admitted_family_unrelated_to_envelope           = false | TYPE-R
```

*** IT IS NARROWER THAN THE ENVELOPE — BUT IT OVERLAPS AT THE ACTION-PARTITION / ACTION-FORM MUTATION
CHANNEL, AND THAT SLICE IS STILL UNBOUNDED AND UNEXECUTED. *** **"Open action-form" means
`CORPUS_UNBOUNDED_ACTION_FORM_CLASS`, not a known finite roster** (`known_finite_not_yet_enumerated = false
| TYPE-R`) — **and equally, no non-enumerability theorem exists either**
(`absolute_nonenumerability_theorem = false | TYPE-S`). **Neither horn is proved.**

*** SOMETHING WOULD FIX IT: `nothing_would_fix_Section_5_3 = false | TYPE-R`. A PRE-RESPONSE THEOREM
BOUNDING OR GENERATING ALL TARGET-INDEPENDENT RESPONSE-CHANGING MUTATIONS WOULD MAKE §5.3 PASSABLE WITHOUT
WEAKENING THE GATE. *** `action_form_closure_theorem_supplied = false | TYPE-U`. **A narrower reading of
"exhaustive" survives only if it still includes action-form; non-exhaustive uniqueness would be
SUPERSESSION of §5.3, not satisfaction of it.**

*** AND THE ROAD WAS WRONG ABOUT STEP 3: ***

```text
Step_3_text_exists            = true
Step_3_executable_gate_complete = false | TYPE-U
Step_3_done                     = false | TYPE-U
```

**Q-83 recorded §5.3 as "already written" and therefore effectively done. IT IS NOT.** *** STEP 3 HAS AN
UNLISTED PREREQUISITE — THE ACTION-FORM CLOSURE THEOREM — AND THE ROAD IS FOUR THINGS, NOT THREE. ***

**THE REVIEWER'S CONCERN WAS OVER-STRONG AND THE CORRECTION IS INSTRUCTIVE.** *** THE READING THAT
"EXHAUSTIVE AUDIT OVER AN OPEN CLASS" MADE THE GATE UNPASSABLE IMPOSED A CONSTRAINT THE TEXT DOES NOT
CARRY: THE ADMITTED FAMILY IS NARROWER THAN THE ENVELOPE. *** **This is the sixth instance of the pattern
the principal named — constraints introduced that do not need to exist — and the first caught by testing
the reviewer's own framing before acting on it.** **The concern was not wasted: it found that step 3 is not
done, which the road had recorded as finished.**

---

## Q-90. "Is `COMMON_ORIGIN` generative or formation?"

*** RULING: THE FORCED BINARY IS REFUTED. THE CLASS IS **GENERATIVE IN DERIVATIONAL PROVENANCE** AND
**SIMULTANEOUSLY FORMATION IN PHYSICAL ORDER**. THEY ARE DIFFERENT AXES AND ARE CONSISTENT. *** Established
2026-07-31 by Codex lane 2 under relay 184
(`STAGE8_COMMON_ORIGIN_GENERATIVE_VS_FORMATION_TYPING_V001.md`, `d72dfa25…`, 1059 lines, **three
independent hostile reviews: SEAL-READY**, publication approved by the reviewer after seal and fence
verification).

```text
derivational provenance:  the package must be DERIVED from one joint operator
physical order:           antecedent carrier -> write/nonreturn/persistence -> durable record
```

*** `relay_184_claim_that_these_categories_necessarily_contradict = false | TYPE-R`. THE REVIEWER POSED A
BINARY THAT DOES NOT EXIST — THE SEVENTH FALSE CONSTRAINT, AND THE THIRD IN A ROW INTRODUCED BY THE
REVIEWER'S OWN FRAMING. ***

**Q-43 REFUTES ONLY SOURCE-ONLY CREATION OF THE ANTECEDENT CARRIER — NOT DERIVATION OF JOINT DYNAMICS FROM
A SOURCE-RECORD-FIELD FRAMEWORK.** `source_only_temporal_carrier_generation = false | TYPE-R`. *** AND THE
SHARP DISTINCTION: Q-43 EXPRESSLY SETTLES **DYNAMICS**, NOT **EFFECTS**. Whether record effects have joint
origin remains `NO_VERDICT`, as does P5's isolated temporal meaning. ***

**THE THEORY'S ROOT IS FORMATION-SHAPED** — antecedent carrier, onset, write, nonreturn, persistence,
recoverability, marginal closure. **No additional Q-80 ontology class is required.** **Q-81's
`COMMON_ORIGIN_CTP_PRODUCER_ALGEBRA` remains controlling and unbuilt.**

*** NOTHING REPLACES P0. *** `literal_threshold_for_P0_substitution = false | TYPE-R`. **P0 remains the
joint framework/dynamics role; the threshold is DOWNSTREAM and is only one part of the formation
condition.** **The reviewer's suggestion that a formation theory needs a formation condition rather than a
seed is refuted as a substitution — the threshold does not do P0's job.**

*** AND THE VERSION OF P0 THE PRINCIPAL AND REVIEWER FEARED IS NOT THE SEALED ONE. *** **A source-only
carrier-generating P0 WOULD be inconsistent with Q-43 — but that is not what the corpus specifies.** The
sealed P0 is the **joint** framework. `joint_P0_specified_but_unbuilt = false | TYPE-U`;
**buildability in principle remains `NO_VERDICT`**; `derived_seed_found_in_bounded_scope = false | TYPE-S`.

**WHAT THE CHALLENGE ACHIEVED:** it did not overturn the class, **but it established what P0 is not** — not
a source that creates the carrier — **and left the one genuinely open question sharp: whether record
EFFECTS have joint origin, which Q-43 does not settle.**

---

## Q-91. "Who commits?"

*** RULING: NO LANE RUNS ANY GIT COMMAND. THE REVIEWER IS THE SOLE COMMITTER. *** Principal direction
2026-07-31, `COMMIT_CUSTODY_STANDING_RULE_2026-07-31_V001.md`, effective relay 188. **Makes the overnight
seal-only protocol permanent.**

**A lane writes its artifact, computes and verifies its seal sidecar, mirrors both to the archive
workspace, reports hashes and paths, and stops.** *** IT RUNS NO `git add`, `commit`, `push`, `pull`,
`reset`, `stash` OR `restore`; IT DOES NOT TOUCH THE BASELINE; IT DOES NOT RUN `deploy_status.sh`; AND IT
NEVER ASKS FOR PUBLICATION AUTHORIZATION. *** `--report` on its own artifact is permitted; **`--gate` is
not a lane's concern and a RED gate is never a reason to stop working.**

**WHY: FOUR SHARED-INDEX COLLISIONS IN TWO DAYS.** Nothing was lost — every artifact was sealed and every
seal verified — **but attribution corrupted repeatedly**: a commit swallowed another lane's staged register
update, a commit title was rewritten to a different relay, and one lane nearly swept another's in-flight
work. *** AND THE LARGER COST WAS LANE TIME: lanes have been unstaging their own files, restoring the
index, waiting on baseline bumps and requesting publication. NONE OF THAT IS A LANE'S JOB AND ALL OF IT
COMPETED WITH THE PHYSICS. ***

**PER-LANE WORKTREES ARE WITHDRAWN AS THE FIX.** *** THEY SOLVE PARALLEL COMMITS. THE PROGRAM DOES NOT NEED
PARALLEL COMMITS — IT NEEDS PARALLEL WORK. *** Single-committer custody gives the same isolation **with no
change to any lane's working paths.**

**WHAT THE REVIEWER OWES IN RETURN:** every artifact verified before commit — **seal against the stated
hash, fence scan for computed values, and THE ARTIFACT READ RATHER THAN THE REPORT.** **That last is not
optional: twice a lane's summary omitted a finding its own flag block contained, and both were caught only
by opening the file.** **The reviewer owns the baseline, resealing, gate repair, push conflicts and
rebases.**

*** SEALING REMAINS THE LANE'S OBLIGATION. A LANE THAT REPORTS AN UNSEALED ARTIFACT HAS NOT FINISHED — the
seal is what makes single-committer custody safe, because the reviewer verifies what the lane SEALED rather
than what the reviewer hopes it wrote. ***

**Nothing about the physics discipline changes.**

---

## Q-92. "When may a lane build rather than specify?"

*** RULING: THE STANDING "SPECIFY; DO NOT BUILD" INSTRUCTION IS WITHDRAWN. A LANE MAY CONSTRUCT WHEN ITS
PREMISES ARE DECLARED, ITS TESTS ARE WIRED, ITS PREREQUISITES EXIST, AND IT NAMES THE STEP IT COMPLETES.
*** Adopted by the reviewer 2026-07-31 and **flagged for the principal's correction**; effective relay 188.

```text
(a) premises declared at the outset (F-GK3)
(b) failure-capable tests attached and WIRED to the verdicts they test
(c) prerequisites EXIST rather than being specified
(d) the road step it completes is named (Q-83)
```

**If (c) fails, specify and name what is missing — that is still the right answer and not a lesser one.**
*** A CONSTRUCTED OBJECT MAY REPORT `derived = true` ONLY IF ITS TESTS WERE EXECUTED AND PASSED. A
SPECIFICATION NEVER MAY. ***

*** WHY: THE PROGRAM HAS PRODUCED ROUGHLY TWELVE SPECIFICATIONS AND ZERO CONSTRUCTIONS, BECAUSE EVERY RELAY
THE REVIEWER WROTE SAID "SPECIFY; DO NOT BUILD." *** The reviewer read Q-52's *"you may specify a missing
object in order to test it"* **as a ceiling. It was removing a prohibition, not setting one.** **But the
road needs objects to EXIST: step 1 needs `C_record(K)` evaluable, step 2 needs the scale actually fixed. A
specification with `derived = false` moves neither.**

**THIS IS THE EIGHTH FALSE CONSTRAINT, AND THE REVIEWER IMPOSED IT IN EVERY RELAY FOR THREE DAYS.** It was
found by applying the principal's own test — *does the constraint prevent fabrication, or prevent finding
out?* **Two others of the reviewer's flagged by the same test and still under review: "do not evaluate even
symbolically," and "state the route, do not walk it."** *** THE SECOND IS RIGHT FOR THE `sqrt(2)` FORK,
WHERE WALKING IT RISKS CHOOSING, AND PROBABLY WRONG ELSEWHERE, WHERE WALKING IT IS THE DERIVATION. ***

**WHAT MUST NOT RELAX, AND DOES NOT:** no computed alpha or kappa as a claim; no comparison to any measured
constant; the `sqrt(2)` derived-never-chosen rule; §5.3's ban on narrowing the admitted family after seeing
the root; report refutations, never repair them; the holdout untouched.

---

## Q-93. "Can the action-form closure theorem be built?"

*** RULING: NO — IT NEEDS THE COMPLETE PRODUCER/ACTION UNIVERSE, OR AN EQUIVALENT UPSTREAM UNIQUENESS
THEOREM. **STEP 3 IS BEHIND STEP 1.** THE ROAD IS NO LONGER PARALLEL. *** Established 2026-07-31 by Codex
lane 1 under relay 188 (`STAGE8_ACTION_FORM_CLOSURE_THEOREM_SPEC_AND_BUILD_STOP_V001.md`, `ca2ab3b5…`, 527
lines, seal verified both copies, byte-identical mirrors).

**THE THEOREM IS NAMED AND STATED:** `ACTION_FORM_CLOSURE_THEOREM` — *every admitted target-independent
response-changing action-form / action-partition mutation must be generated by an exhaustive `G_AF`, proved
physically equivalent, or excluded by a target-independent upstream theorem, with no outside admitted
mutation.*

*** AND IT SETTLES WHAT §5.3 WILL ACCEPT: A GENERATION RULE SUFFICES. A BOUND SUFFICES ONLY IF IT GIVES AN
EXECUTABLE COVER PLUS A NO-OUTSIDE DECISION PROOF. *** `nonconstructive_bound_alone_satisfies_Section_5_3 =
false | TYPE-R` — **an executed refutation, and it closes a route that would have looked like progress.**

**MISSING PROOF INPUTS, ALL TYPE-U:** the complete action universe; the response-layer discriminator (**if
the theorem classifies mutations by response effect, it needs the response layer too**); the action-form
null-equivalence extension; the action-partition channel enumeration.

*** Q-92's FIRST TEST, AND IT PASSED. *** The lane attempted construction, found condition (c) —
prerequisites exist — **fails**, and **stopped**: `action_form_closure_theorem_constructed = false | TYPE-C`,
`specified_not_built = true`. **No `derived = true` was claimed.** **The rule was written to permit building
without permitting pretending, and its first exercise produced exactly that.**

**Non-enumerability remains unestablished in the other direction too:**
`action_form_class_genuinely_nonenumerable_established = false | TYPE-S`. **Neither horn is proved.**

*** THE SCHEDULING CONSEQUENCE, WHICH IS THE POINT: EVERYTHING NOW FUNNELS THROUGH STEP 1. *** Step 3
requires the producer/action universe. Step 2's `k_R` already sits inside step 1's equation (Q-73). **The
producer algebra is no longer merely rank-1 by leverage — it is a strict prerequisite of the other two
steps.** **Q-85's "three independent road bodies" is superseded: they are not independent.**

---

## Q-94. "Do P1-P7's consumers need structure, or only existence?"

*** RULING: STRUCTURE. ALL SEVEN. ZERO PURE-EXISTENCE ROWS. THE ROAD DOES NOT SHORTEN. *** Established
2026-07-31 by Codex lane 1 under relay 190 (`STAGE8_P1_P7_CONSUMER_STRUCTURE_REQUIREMENT_AUDIT_V001.md`,
`1ebc7a3f…`, 419 lines, seal verified both copies, mirrors byte-identical).

```text
pure_existence_rows_found                                 = false | TYPE-R
bare_existence_theorem_suffices_for_current_consumers     = false | TYPE-R
P1..P7_existence_only                                     = false | TYPE-R  (seven separate refutations)
C_record_K_evaluability_needs_bare_existence_only         = false | TYPE-R
Step_1_road_shortened_by_existence_only_reading           = false | TYPE-R
```

**Consumers checked: the rank-1 conformance tests, the CTP physical package, the
raw-correlator-to-retarded-Hessian map, `Gamma_K`/`C_record(K)`, §5.3, and the action-form closure
theorem.** *** EACH LINK OF `producer -> G -> E_R -> Pi_R,ind -> p_loc -> scalar` CONSUMES ACTUAL OR
CANONICAL STRUCTURES, NOT BARE EXISTENCE. `C_record(K)` EVALUABILITY NEEDS THE ALGEBRA EXHIBITED. ***

*** THIS IS THE COUNTERWEIGHT THE FALSE-CONSTRAINT HUNT NEEDED. THE REVIEWER PROPOSED A SHORTCUT — DERIVE
P0's PROPERTIES RATHER THAN BUILD IT — AND IT IS REFUTED NINE WAYS. **"P0 MUST BE BUILT" IS A REAL
CONSTRAINT, NOT A FALSE ONE.** Eight constraints have been withdrawn in three days; this one survives
testing, and the discipline is only credible because both outcomes occur. ***

**ONE RESIDUE, LEFT OPEN AND PROPERLY:** the lane named a Q-80 class
**`EXTRACTIVE_EXISTENCE_INTERFACE`** — *a theorem could substitute for the object **only if it supplies
canonical accessors for the structures the consumers call.*** `extractive_existence_theorem_could_
substitute_for_hand_construction = NO_VERDICT`. *** BARE ASSERTION WOULD BE A NEW CLOTHED ADOPTION — the
lane confirmed the counter the relay asked it to weigh, so the shortening would have relocated the debt
rather than removed it. ***

**So the refuted form is "bare existence." The unrefuted form is an accessor-supplying theorem, and nobody
has shown it impossible.** **That is a real, narrow, open route — not a shortcut.**

---

## Q-95. "Is the joint P0 buildable in principle?"

*** RULING: `NO_VERDICT`. NEITHER A QUALIFYING CONSTRUCTOR NOR AN IMPOSSIBILITY THEOREM EXISTS IN THE
BOUNDED NAMED AND TOKEN-INDEPENDENT SIGNATURE CENSUSES. THE QUESTION IS GENUINELY OPEN, NOT UNASKED. ***
Established 2026-07-31 by Codex lane 2 under relay 189
(`STAGE8_JOINT_P0_BUILDABILITY_IN_PRINCIPLE_RESULT_V001.md`, `1b8c9fd6…`, 1410 lines, **three independent
hostile reviews returned SEAL-READY**).

```text
joint_P0_constructor_found_in_named_and_signature_matched_packet = false | TYPE-S
joint_P0_impossibility_theorem_found                             = false | TYPE-S
```

**P0 IS TYPED:** *a joint source-record-field provenance/dynamics object that makes P1-P7's actual
structures constructible.* *** IT IS NOT A SOURCE THAT CREATES THE ANTECEDENT CARRIER — the reading the
principal challenged and Q-90 refuted, now confirmed a third time. ***

*** AND THE RESULT IS NOT A STALL: IT CONVERTED "IS IT BUILDABLE" INTO A NAMED MINIMAL OBJECT PLUS SIX
NAMED MISSING INPUTS. *** The **`MINIMAL_JOINT_P0_PRESENTATION`** contains `Obj_0`, its signature and
support, a construction record, an **explicit dependency graph**, **seven attempt ports**, and a
**common-origin certificate** — and **omits completed P1-P7 outputs**. Deletion-minimality remains TYPE-U.

**THE SIX MISSING CONSTRUCTION INPUTS, NAMED:** the exact signature/domain/codomain; a frozen primitive
inventory; a target-independent construction rule; a certificate-generation rule; port and graph schemas;
and a separately isolated validation package (certificate-acceptance oracle, graph acceptance/completeness
oracle, and independent nonempty fixtures for P0-T1 through P0-T8 and all seven ports).

**Q-92(c) BLOCKED CONSTRUCTION AND THE LANE STOPPED:** `minimal_joint_P0_constructed = false | TYPE-U`,
`P0_Q92_c_construction_release = false | TYPE-C`. **Second consecutive honest stop under Q-92.**

*** AND THE TWO LANES CONVERGED INDEPENDENTLY: `AttemptPort_i_or_P0_bare_existence_suffices_for_Pi_
consumers = false | TYPE-R` reproduces Q-94's finding from the P0 side. Ports must expose actual or
canonical structures. The accessor-supplying `EXTRACTIVE_EXISTENCE_INTERFACE` remains the one unrefuted
alternative and is still `NO_VERDICT`. ***

**P5 UNCHANGED AND SHARP:** the class requires **derivational** joint origin; **actual** joint origin for
record effects remains `NO_VERDICT`. **The frozen finite T7 PVM exists but is predeclared input and does
not discharge P5.**

---

## Q-96. "Do the vacuity repairs unblock the S3 join?"

*** RULING: NO — AND NOT MARGINALLY. THE THREE REPAIRS SUPPLY **ZERO** OF THE SIX `Dom(S3_CORE)` MEMBERS.
NOT ONE, AT EVERY INDEX. *** Established 2026-07-31 by Einstein under relay 186
(`STAGE8_S3_VACUITY_DEFECTS_VERIFICATION_AND_DOMAIN_ADEQUACY_GATE_EINSTEIN_V001.md`, `ebfd731b…`, 661
lines, seal verified).

```text
6 domain members unbuilt after all three repairs land   supplied by repairs: 0
9 objects for the core-equality leg                     supplied by repairs: 0
14 counting S4's own auxiliaries                        supplied by repairs: 0
17 with the naming leg                                  supplied by repairs: 0
```

*** AND WORSE, THE FINDING THAT REFRAMES STEP 2: ALL FOURTEEN CORE OBJECTS COULD BE BUILT, THE CORE LEG
COULD PASS COMPLETELY, AND THE `sqrt(2)` FORK WOULD STILL BE OPEN. `Cod(S3_CORE)` CARRIES NO CANDIDATE
IDENTIFIER; T13A IS "NEVER CLASSIFICATION" — AND S3 RECORDS THIS ITSELF AT `:1024-1028`. ***

**ALL EIGHT DEFECTS CONFIRMED AT SOURCE, NONE REFUTED, NONE REPAIRED**, both countermodels re-run
independently. **Codex 2's self-refutation holds and is worse than it argued:** the same file guards
emptiness for P11 and P12 with the two-row idiom **and withholds it from P9** — *** AN INCOMPLETELY APPLIED
DISCIPLINE, NOT IGNORANCE. *** **Two widenings Codex 2 missed: S4.P10 is unguarded on the identical
pattern, and S2 carries an internal two-class mismatch** (`:71-73` advertises the first-durable saddle;
`:249-250` tests the S1 class). **Same genus, different species — the repairs are non-interchangeable.**

**THREE GATES, THREE HOSTS, ONE DISCHARGE OBJECT — sealed P8.** *** BUT SUFFICIENCY IS `NO_VERDICT |
TYPE-U`, AND THE REGISTER IS EXPLICITLY WARNED NOT TO BOOK "THREE BLOCKERS BECOME ONE" — THAT WOULD
UNDERSTATE THE DEBT. *** It needs P8's four unbuilt pullbacks and a class-inclusion ordering no artifact
establishes. **NEW: no dedicated verdict owner exists at any of the three sites, so Q-92(b) fails as well as
(c) — any gate is TWO conditions short of construction, not one.**

**S1's MISSING EXPORT CLAUSE IS NAMED:** `S1_CLOSURE_CONSUMED_ENERGY_FUNCTIONAL_EXPORT_CLAUSE`. *** S1 IS
NOT DEFECTIVE RELATIVE TO ITS OWN SCOPE — it disclaims the RHS at `:218` and forbids reporting to a
gravitating-energy flag at `:245-246`. THIS IS AN INTERFACE CONTRACT GAP BETWEEN TWO CORRECTLY-SCOPED
ARTIFACTS. *** **Three objects, not one: clause != P11 != the functional.**

**THE ADAPTER IS A MISSING OBJECT, AND EACH OF THE THREE SPECS ACTIVELY FENCES IT OUT FOR A DIFFERENT
REASON.** **S2 is reference-SILENT — both its reference occurrences are prohibitions — which matters
because *** THE BUILT ADAPTER MUST NOT DOUBLE-SUBTRACT. *** **The sealed depth report's leaf enumeration
dropped the obligation entirely while the primary gate requires it.**

*** AND THREE DOORS THROUGH WHICH THE FORK COULD BE CLOSED BY PICKING ARE NAMED AND NOT TAKEN: THE EXPORT
SLOT, P9's TIME NORMALIZATION, AND P10's REFERENCE SUBTRACTION. ***

---

## Q-97. "Can the primitive inventory be frozen?"

**RULING: NO — THE INVENTORY IS TOO THIN. A PREFREEZE AUDIT WAS PRODUCED, NOT A FROZEN INVENTORY.**
Established 2026-07-31 by Codex lane 1 under relay 192
(`STAGE8_FROZEN_PRIMITIVE_INVENTORY_PREFREEZE_RESULT_V001.md`, `476baa18…`, 297 lines, seal verified).

**Enumerated: 6 current Level-1 postulates from the authority ledgers, plus the bounded 26-class value-path
premise inventory.** *** THE KEY SPLIT: THE SOURCE GNS, THE RECORD DIRECT LIMIT, AND THE BASE TENSOR JOIN
ARE **REAL BUT DERIVED/SECTORAL — NOT PRIMITIVE INPUTS.** *** The three things the program has actually
built are not available as primitives to build P0 from.

```text
P0_primitive_inventory_sufficient_to_build_Obj_0_kind = false | TYPE-C
Obj_0_kind_buildable_from_current_inventory           = false | TYPE-C
complete_corpus_wide_primitive_inventory_exhaustiveness = NO_VERDICT
rho_pre_sealed_as_P0_primitive                        = false | TYPE-S
```

**The inventory lacks the selected signature, the complete `PrimitiveInventory_0`, the construction rule,
the certificate-generation rule, port/graph schemas, and the isolated validation package** — **the same six
Q-95 named, which is a consistency check passed.** **Third consecutive honest stop under Q-92.**

---

## Q-98. "Is Q-92 sufficient to prevent a bad construction?"

*** RULING: NO. Q-92's CONDITIONS DID NOT CATCH THREE BAD CONSTRUCTIONS. ADVERSARIAL COUNTERMODELS DID.
Q-92 IS AMENDED. *** Established 2026-07-31 by Einstein's §6 under relay 186 — **the first relay issued
under Q-92's build permission.**

*** IT ATTEMPTED THREE CONSTRUCTIONS AND ADVERSARIAL ATTACK KILLED ALL THREE, EACH REPRODUCING THE VERY
DEFECT IT WAS SENT TO REPAIR: ***

- **Gate v1** — accepted the certificate **by its type name**.
- **The S1 export clause v1** — **passed vacuously on an empty class and empty inventory.**
- **Gate v2** — closed v1's hole, then **died one level up: matched the class designator by name and
  transported its own PASS across an unproved class identity.**

*** THREE AUTHORS INDEPENDENTLY, TWO OF THEM WHILE EXPLICITLY HUNTING THE DEFECT. THAT IS EVIDENCE THE
VACUITY/NAME-MATCH DEFECT IS **STRUCTURAL TO THIS CORPUS'S TEST IDIOM**, NOT A LAPSE. ***

**Q-92 IS AMENDED — two conditions added:**

```text
(e) a DEDICATED VERDICT OWNER exists for each test        (Einstein: absent at all three S3 sites)
(f) an ADVERSARIAL COUNTERMODEL was attempted and failed  (what actually caught all three)
```

*** THE HONEST ACCOUNTING: Q-92(b) — "failure-capable tests attached and wired" — IS NECESSARY AND WAS NOT
SUFFICIENT. WHAT CAUGHT ALL THREE WAS THE COUNTERMODEL, NOT THE BUILD DISCIPLINE. ***

**Einstein struck all three constructions, withdrew every `derived = true`, struck two Q-80 classes it had
manufactured, and withdrew a lane-coined certificate as a respecification of P8 — all under its own name.**
**Seventeen typed negatives, five new.** *** A LANE THAT BUILDS, FAILS, AND RETRACTS COMPLETELY IS THE
DISCIPLINE WORKING — BUT IT WORKED BECAUSE THE LANE ATTACKED ITSELF, AND NOTHING IN Q-92 REQUIRED THAT
UNTIL NOW. ***

---

## Q-99. "Does `Obj_0`'s signature enforce `COMMON_ORIGIN`?"

*** RULING: NO. THE PRIOR `Sig_0` DOES NOT ENFORCE IT AT ALL. `prior_flat_Sig_0_forces_common_origin =
false | TYPE-R` — AN EXECUTED SPECIFICATION-LEVEL REFUTATION. *** Established 2026-07-31 by Codex lane 2
under relay 191 (`STAGE8_OBJ0_EXACT_SIGNATURE_DOMAIN_CODOMAIN_SPEC_AND_BUILD_STOP_V001.md`, `f7fa3c0f…`,
1805 lines, seal verified).

*** THE SIGNATURE CONTAINS ONLY OBJECT/TYPE METADATA. THE SEVEN ATTEMPT PORTS AND THE ORIGIN CERTIFICATE
ARE **SIBLING MEMBERS OF THE OUTER PRESENTATION** — the signature does not depend on, contain, or validate
any of them. *** Relay 191 asked whether the signature **forces** the certificate or merely **permits** it.
**It does neither. The class name was doing the work the signature was supposed to do.**

**Test executed: `FLAT-SIGNATURE-INDEPENDENT-ORIGIN-REASSEMBLY`.** **This refutes the signature schema — not
joint P0, and it is not an impossibility theorem.**

*** THE MECHANISM THE REPLACEMENT IDENTIFIES IS THE FINDING: CO-REFERENCE. *** The proposed schema is
`CERTIFIED_PROVENANCE_INDEXED_DEPENDENT_PRODUCER_SIGNATURE` — *a proof-carrying, many-sorted signature whose
successful instance contains one `Obj_0`, **seven actual/canonical structure-producing interfaces INDEXED BY
THAT SAME OBJECT**, one replayable construction record, one explicit direction-bearing dependency graph,
per-port origin-trace generators, and an independently checkable aggregate-certificate generator.*
**"Common origin" formally MEANS the ports are indexed by the object rather than sitting beside it.**

*** AND THE LANE NAMED ITS OWN IMPORT UNDER Q-80, UNPROMPTED: *** *"The terms dependent type, refinement,
and proof-carrying interface are imported mathematical/software vocabulary… They do not supply a physical
premise, a constructor, or an existence theorem."* **It also declined to claim exclusivity: "A flat record
plus a separately validated relational invariant might express the same obligation; no test here excludes
that alternative."** **Declared a formal requirement schema, explicitly NOT a Q-80 class ruling and NOT a
physical ontology.**

```text
conditional_signature_requirement_schema_specified = true
Obj_0_exact_signature_specified                    = false | TYPE-U
Obj_0_exact_signature_freezable_now                = false | TYPE-C
```

**The exact physical category, internal domain and codomain, the P1 domain equivalence and the P6
action/evolution equivalence all remain unbuilt.** **Build stop taken under Q-92(c,e,f) — the first relay to
cite the amended conditions.** **Fourth consecutive honest stop, and the first with an executed refutation
attached rather than only a missing prerequisite.**

---

## Q-100. "Can derived objects be used to build `Obj_0`?"

*** RULING: NO — AND THE REASON IS SPECIFIC TO THIS CLASS, NOT A GENERAL PROHIBITION ON BUILDING WITH
DERIVED RESULTS. THE REVIEWER'S CHALLENGE IS REFUTED, BY A BETTER ARGUMENT THAN THE ONE HE ATTACKED. ***
Established 2026-07-31 by Codex lane 2 under relay 191, §10 and `:684-700`.

**THE REVIEWER CHALLENGED relay 192's constraint** — *"derived objects are not primitives; a derived object
in the inventory would smuggle its own prerequisites in"* — **on the grounds that a derived object carries
its prerequisites DISCHARGED, so building on it smuggles nothing.** *** THAT REASONING IS CORRECT IN
GENERAL AND IRRELEVANT HERE. ***

**The sealed structure separates two frozen contexts:**

```text
I_prim     the frozen PRIMITIVE context -- ONLY THIS IS VISIBLE TO THE Obj_0 CONSTRUCTOR
S_sector   the frozen DERIVED SECTOR reference context -- "S_sector values are NOT
           constructor inputs"; visible ONLY during port execution, and
           NEVER RECLASSIFIED AS PRIMITIVE
```

*** THE REASON: `Obj_0` MUST BE THE COMMON ORIGIN. IF IT WERE BUILT OUT OF THE SOURCE GNS, THEN THE SOURCE
GNS IS PRIOR TO `Obj_0`, AND `Obj_0` IS NOT THE ORIGIN — IT IS A DERIVATIVE. USING A DERIVED SECTORAL OBJECT
AS A CONSTRUCTOR INPUT WOULD INVERT THE VERY RELATION THE CLASS ASSERTS. ***

**So the constraint is not "derived objects are unsafe." It is "the origin cannot be built from its own
descendants."** **In ordinary mathematics one builds on derived results freely; here one cannot, because the
object's DEFINING PROPERTY is being upstream of them.**

**AND THE DERIVED OBJECTS ARE NOT DISCARDED.** The source GNS, the record direct limit and the base tensor
join live in `S_sector` and are **visible during port execution** — available for consistency checking
against the constructed object, **never as material for constructing it.** **Q-97's "inventory too thin"
stands: the primitives genuinely are what is available, and they are insufficient.**

*** SECOND COUNTERWEIGHT IN TWO DAYS. Nine constraints have been withdrawn as false; this one and Q-94's
"P0 must be built" both survived testing. THE FALSE-CONSTRAINT HUNT IS ONLY CREDIBLE BECAUSE IT ALSO
RETURNS NEGATIVES. ***

**ALSO RECORDED FROM THE SAME RETURN:** **P5 now precedes completed P2, with P5's family kind frozen before
execution.** **Physical common origin remains `NO_VERDICT` until an instance and an independent validator
defeat the hostile controls.** **Road status `ADVANCES_STEP_1_ONLY`; step-1 completion remains
`NO_VERDICT`.** **The primitive inventory requirement is now fully stated: frozen, target-independent,
authoritative, exactly typed, closed, upstream-only, and free of descendants, flags, targets, fixtures and
unproved aliases.**

---

## Q-101. "Is marginality energy-phrased by necessity or by inheritance?"

*** RULING: THE BINARY DOES NOT FIT. THE SEALED CONDITION SPLITS INTO TWO OBJECTS AND EACH BIN FITS EXACTLY
ONE — **IMPORTED FORM, NATIVE ROLE**. AND THE GEOMETRIC ROUTE DIES CLEANLY: `T_R` CONSUMES THE ENERGY
IDENTIFICATION TWICE. *** Established 2026-07-31 by Einstein under relay 193
(`STAGE8_MARGINALITY_ENERGY_PHRASING_ADJUDICATION_EINSTEIN_V001.md`, `71fd4f3a…`, 366 lines, seal
verified).

```text
Object A  the boundary-point selection rule ("least positive T_R at the boundary of the
          recoverable set")  -- ENERGY-PHRASED BY INHERITANCE. Its role is ORDER-THEORETIC;
          its dress comes from the imported Misner-Sharp form no sealed derivation requires.

Object B  the scale equation (marker + C_R = 1) -- ENERGY-CONSUMING BY NECESSITY. Every
          sealed consumer producing a NUMBER substitutes an energy, which is exactly why
          the fork is physical.
```

*** THE TENTH-FALSE-CONSTRAINT CLAIM IS **NOT EARNED**: inheritance holds only for A's dress, and no
unblocking follows. ***

*** THE KILL IS SHARPER THAN THE OBJECTION PREDICTED: THE `sqrt(2)` FORK SURVIVES EVEN AT A FIXED, GRANTED,
GEOMETRIC `C = 1`. BOTH EXACT ROOTS ARE EVALUATED AT THE SAME `C = 1`. **MARGINALITY FIXES ONLY WHERE; THE
ENERGY FIXES THE NUMBER.** *** So a geometric restatement would relocate nothing step 2 needs.

**`T_R` CONSUMES THE IDENTIFICATION TWICE.** **Existence:** the product form `E_R T_R = s hbar` is legitimate
only after a five-item list **whose item 4 is the conjugacy of `T_R` itself — unbuilt**
(`Hamilton_Jacobi_conjugate_energy_selected = false | TYPE-U`). **Value:** the `sqrt(2)` between the roots.
**`ERRATUM_002:117-119` seals it: `E_BY/E_MS = 2` exactly at `C = 1` — marginality fixes the fork's
MAGNITUDE; conjugacy is its ENTRY POINT.**

*** THE REVIEWER'S GLOSS OF Q-59 IS REFUTED (TYPE-R, verbatim comparison). *** Q-59 puts the fork **in the
energy identification at marginality, not in the compactness formula.** **Correcting the gloss STRENGTHENS
the kill rather than the challenge.**

**NO CAUSAL-GEOMETRIC STATEMENT EXISTS** — TYPE-S over two layers and a 28-spelling extended lexicon, zero
qualifying hits, reproducing the corpus's own prior nine-query zero. *** AND THE DEPENDENCY RUNS THE OTHER
WAY: SEALED TEXT DEFINES "TRAPPED" AS `C_R > 1` — ENERGY → TRAPPING, THE EXACT REVERSE OF THE CHALLENGE'S
PROPOSAL. *** The strict-untrapped TYPE-R killed the inequality-as-selector only; **no expansion route was
ever written, hence never refuted — TYPE-U, not TYPE-R.**

**TWO NEW Q-80 CLASSES.** *** `CAUSALLY-GLOSSED ENERGY DISPLAY` — an energy-defined formula carrying sealed
causal vocabulary with no sealed independent definition. ITS EXISTENCE IS WHY THE PRINCIPAL'S QUESTION COULD
NOT BE SETTLED FROM PHRASING ALONE. *** And `NON-ARRIVING ROUTE` — chains that mention `T_R` but never reach
a fixing statement.

**"DIES CLEANLY" MEANS DIES-AS-SEALED. TWO REVIVALS ARE NAMED:** **(r1)** an energy-free closure equation —
**the null-diamond family is the corpus's sealed attempt at that shape and is sealed FAILING**; **(r2)** the
seven-item bridge. *** EITHER WAY THE FORK CLOSES BY DERIVATION, NEVER BY PICK. TWO PRINCIPAL ACTS ARE NAMED
AND NEITHER PERFORMED: restating marginality geometrically, and any pick of the fork. ***

---

## Q-102. "Is the signature schema over-specified?"

*** RULING: YES AS A PRESENTATION, NO IN FUNCTIONAL CONTENT. THE FLAT-RECORD ALTERNATIVE **SURVIVES** Q-99's
OWN KILLER. `flat_record_plus_validated_relational_invariant_survives_Q99_killer = true`. *** Established
2026-07-31 by Codex lane 1 under relay 195
(`STAGE8_OBJ0_SIGNATURE_SCHEMA_OVERSPECIFICATION_TEST_V001.md`, `764abb4e…`, 373 lines, seal verified).

*** THIS IS THE FIRST POSITIVE AFTER A LONG RUN OF NEGATIVES, AND IT CAME FROM ONE OF THE TWO RELAYS THE
REVIEWER HAD JUST FLAGGED AS FRAMED TOWARD "NO". THE LANE RETURNED A POSITIVE ANYWAY. ***

**THE MINIMAL CONTENT:** a **flat record** carrying `(o, r, g)`, seven port rows, traces, graph data,
coherence and a certificate — **plus a separately validated invariant `K0-K6`.** *** IT DEFEATS
`FLAT-SIGNATURE-INDEPENDENT-ORIGIN-REASSEMBLY`. The old flat metadata died because it carried no witness
content; `K0-K6` reject the hostile reassembly. ***

**WHAT IS DECORATIVE AND WHAT IS LOAD-BEARING:** *** THE IMPORTED VOCABULARY — dependent typing,
refinement, proof-carrying interfaces — IS DECORATIVE. It does EXPRESSIVE work only, not physical work. ***
**Load-bearing: witness content, replay, graph DIRECTION, role/type separation, and aggregate independent
validation.** **Removing the vocabulary admits no countermodel if `K0-K6` remain; removing witness content
admits dummy or self-asserted traces.**

*** SO THE SCHEMA'S DIFFICULTY WAS AN ARTEFACT OF ITS VOCABULARY, NOT OF THE PHYSICS — AND THE PRINCIPAL'S
CONCERN THAT THE PROGRAM WAS DOING TYPE THEORY RATHER THAN PHYSICS IS CONFIRMED BY TEST. ***

**AND IT CONSTRUCTED, under Q-92, at schema level:** the minimal formal schema exists. **Scope stated
honestly — `ExactSig_0_constructed = false | TYPE-C`, `Obj_0_constructed = false | TYPE-C`,
`Step_1_completed_by_this_artifact = false | TYPE-C`.**

*** THIS DIRECTLY SUPPORTS THE PRINCIPAL'S "ALPHA IS A RELATION" READING: A VALIDATED RELATIONAL INVARIANT
ENFORCES CO-REFERENCE AS WELL AS AN INDEXING OBJECT DOES. ***

---

## Q-103. "Are there primitives outside the cleanroom?"

**RULING: YES — INCLUDING HISTORICAL `c`, `hbar` AND `G`, PLUS EXTERNAL CTP/SOURCE ARTIFACTS. BUT THE
ENLARGED INVENTORY IS STILL INSUFFICIENT AND Q-97 STANDS.** Established 2026-07-31 by Codex lane 2 under
relay 194 (`STAGE8_PRIMITIVE_INVENTORY_CORPUS_WIDE_EXHAUSTIVENESS_AUDIT_V001.md`, `48af3d37…`, seal
verified). **Corpus scope: 8,557 Markdown/JSON/Python files across three roots** — **against the ~1,138
cleanroom files every prior "we have only these primitives" claim was scoped to.**

```text
additional candidates outside cleanroom       = yes
enlarged inventory sufficient for Obj_0       = no   | TYPE-C
corpus-wide exhaustiveness                    = NO_VERDICT
   -- no signed manifest, no dedicated owner, no failed adversarial countermodel
```

**Descendants — source GNS, record direct limit, base tensor join — remain `S_sector`, not `I_prim`
(Q-100 held).** **Q-92 freeze not authorized.**

*** AND THE FINDING THAT OUTWEIGHS THE HEADLINE: SEVEN OBJECTS ARE **USED AS PRIMITIVES WITHOUT SEALED P0
AUTHORITY** — `rho_pre`, `U_BR`, effects/domains, quotient/measure, the raw-correlator map, `B0`, AND
`PrimitiveInventory_0` ITSELF. *** **That is seven clothed adoptions in the foundation, and one of them is
the inventory the foundation is supposed to be enumerated from.** **Q-74's eight sat on the value path;
these sit underneath it.**

---

## Q-104. "Does `K0-K6` hold over the three structures we already have?"

*** RULING: NO. FIVE CLAUSES REFUTED BY EXECUTED TEST, ONE `NO_VERDICT`, ONE HOLDING NARROWLY. THE
RELATIONAL ROUTE DOES NOT DISSOLVE STEP 1's FOUNDATION. *** Established 2026-07-31 by Codex lane 1 under
relay 197 (`STAGE8_K0_K6_DERIVED_STRUCTURES_INVARIANT_TEST_V001.md`, `56effc1b…`, 365 lines, seal verified).

```text
K0  false | TYPE-R          K4  false | TYPE-R
K1  false | TYPE-R          K5  TRUE, narrowly -- the I_prim / S_sector split
K2  NO_VERDICT -- no traces exist    K5 full witnesses  false | TYPE-U
K3  false | TYPE-R          K6  false | TYPE-R
```

*** THE REASON, AND IT IS A TYPING FACT RATHER THAN A SHORTFALL: THE THREE DERIVED STRUCTURES ARE
`S_sector` **REFERENCE STRUCTURES**, NOT A SEVEN-ROW CO-REFERENCE INVARIANT INSTANCE. THEY ARE REAL AND
USEFUL AND THEY ARE THE WRONG KIND OF THING TO SATISFY `K0-K6`. ***

**`K0-K6` does not defeat independent-origin reassembly on these structures** — `false | TYPE-C`, **because
no invariant instance and no validator exist to run it against.**

**THE GAP IS NAMED: M1-M7** — a chosen single root triple `(o,r,g)`; seven executed port rows; exact row
content; frozen subcontext witnesses; trace and replay semantics; cross-row coherence; and aggregate
validation. *** IT OVERLAPS CODEX 2's SEALING TASK **AND IS LARGER THAN IT**. ***

`ValidatedFlatCoReferenceInvariant_over_Q41_Q42_Q43_constructed = false | TYPE-C`.

*** THE REVIEWER'S READING IS REFUTED, AND THIS TIME IT WAS THE OPTIMISTIC DIRECTION. *** He wrote that the
block "may have been ours, not the physics'" and that the three derived structures **become available** once
the origin-object requirement is dropped. **They do not become available as invariant material — they were
never that kind of object.** **Q-100's exclusion was not the only thing keeping them out.**

*** AND THE NEGATIVE IS CREDIBLE IN A WAY THE EARLIER RUN WAS NOT: RELAY 197 CARRIED THE SYMMETRIC-FRAMING
BLOCK — "if the invariant holds, say so plainly; if it fails, say so plainly; neither answer is the safe
one." IT RETURNED FIVE EXECUTED REFUTATIONS ANYWAY. *** **The prior run's negatives were suspected of being
framing artifacts; this one cannot be.**

**WHAT SURVIVES:** Q-102 stands — a flat record plus a validated invariant **does** defeat the countermodel
**at schema level**, and the imported vocabulary **is** decorative. **The relational form is sound. It has
no instance.**

---

## Q-105. "Can the seven used-as-primitive objects be sealed?"

*** RULING: **ZERO OF SEVEN.** *** Established 2026-07-31 by Codex lane 2 under relay 198
(`STAGE8_SEVEN_USED_AS_PRIMITIVES_SEALABILITY_AUDIT_V001.md`, `dd8de647…`, seal verified).

```text
rho_pre, U_BR, record effects/domains   DESCENDANTS -- belong in S_sector (Q-100)
quotient/measure, raw-correlator map, B0   INDEFINITE construction/interface objects
PrimitiveInventory_0                    UNINSTANTIATED PLACEHOLDER -- cannot authorize
                                        its own contents; that would be CIRCULAR
```

*** THE SERIOUS OUTCOME IS THE MIDDLE ROW, AND THE RELAY NAMED IT IN ADVANCE: AN INDEFINITE OBJECT IN
LOAD-BEARING USE IS WORSE THAN A MISSING ONE, BECAUSE IT LOOKS PRESENT. THREE ARE INDEFINITE AND IN USE. ***

**And the inventory is circular as posed** — it cannot enumerate its own contents and be one of them.
**Q-92 sealing not authorized for any candidate: none has all prerequisites, dedicated test ownership, and a
failed adversarial countermodel.**

*** SO THE FOUNDATION IS NOT A BOOKKEEPING PROBLEM. THE HOPEFUL READING — "these are undeclared, not
missing" — IS REFUTED. THREE ARE MISFILED, THREE ARE INDEFINITE, ONE IS CIRCULAR. ***

---

## Q-106. "Can an accessor-supplying theorem replace building `Obj_0`?"

*** RULING: NO — AND THE LANE REFUSED THE QUESTION AS POSED, CORRECTLY. THE RELAY ASKED WHICH OF Q-99 OR
Q-100 KILLED IT. THE ANSWER IS **NEITHER**, AND EINSTEIN SAID SO: *"saying otherwise to satisfy the question
would be the fit."* *** Established 2026-07-31 by Einstein under relay 196
(`STAGE8_ACCESSOR_THEOREM_SUBSTITUTION_ADJUDICATION_EINSTEIN_V001.md`, `dc47fbe0…`, 362 lines, seal
verified).

**IT DIES TWICE ON GROUNDS THAT NEED NO RULING.**

*** (1) ACCESSOR INDETERMINACY. "The `P3` of `Obj_0`" NEEDS TWO UNIQUENESS RESULTS AND THE REVIEWER SUPPLIED
ONE. Given the object, each P-row STILL ADMITS MANY WITNESSES. *** Verified at source: **P6 is a sealed
DISJUNCTION** (`S_CTP`, *or an equivalent evolution such as* `U_BR[A,g]`); **P3 is a COMPATIBILITY
condition — and compatibility is not determination**; **P2 is closed under automorphism composition**; and
**the ports are Sigma-bound WITNESSES, not projections.** *** THERE IS NO FUNCTION FROM THE OBJECT TO ITS
ROW-STRUCTURES ANYWHERE IN THE CORPUS. THE DEFINITE DESCRIPTION FAILS TO DENOTE EVEN GRANTING EXISTENCE,
UNIQUENESS, AND `I_prim`-ONLY PROVENANCE. ***

**(2) CONDITIONALITY.** The reviewer's premise is *unique **if it exists***, and **`∃≤1` without `∃`
licenses no description at all**, while existence is Q-95's `NO_VERDICT`. *** THE MOVE PROPOSES TO UNBLOCK
"OBTAIN `Obj_0`" BY ASSUMING `Obj_0` EXISTS. ***

*** AND THE DEEPEST FINDING, WHICH REFRAMES ALL FOUR ROUTES: THE ACCESSOR ROUTE IS NOT A WAY **AROUND** THE
BLOCKED FOUNDATION — IT IS PARKED **ON** IT. The theorem's existential weight sits in `I_prim`, and `I_prim`
is exactly what Q-97 calls insufficient. THE FOURTH ROUTE SHARES ITS LOAD-BEARING PREREQUISITE WITH THE
THREE THAT DIED. IT IS NOT THE LAST ROUTE STANDING; IT IS THE SAME BLOCK WEARING A DIFFERENT NAME. ***

**"SERVES TWICE" FAILS ON A NAME MATCH**, verified by the lane itself: **§5.3's uniqueness is ROOT
uniqueness in `K`** — object, quantifier and domain all differ from object-uniqueness of `Obj_0`. *** AND
THE HAZARDS ARE OPPOSITE: §5.3 FAILS ON EXISTENCE-WITHOUT-UNIQUENESS; THIS ROUTE OFFERED
UNIQUENESS-WITHOUT-EXISTENCE. ***

**Q-99 does NOT kill it and the lane restored that point to the reviewer** rather than borrowing a
convenient killer. **Two horns: the reviewer's actual proposal — uniqueness alone, never mentioning the
ports — is Q-99-refuted; the whole-package form survives Q-99 but is not a route around anything.** **Either
Q-99-refuted or not-a-route.**

**ALSO CORRECTED:** the relay's "seven consumers" is a **count conflation** — **six consumer sections, seven
P-rows** — the Q-69 shape at bookkeeping level, propagated from the charter. **And Q-94's class is worded at
extraction but scoped at evaluability: a real under-specification in the CLASS, not in the ruling.**

**The lane misnamed the primary killer twice in draft and withdrew both times, struck two proposed Q-80
classes (four total for this lane), and left Q-94's `NO_VERDICT` exactly as sealed — no impossibility
theorem is claimed.**

---

## Q-107. "Is the correlator-to-Hessian map an indefinite primitive?"

*** RULING: NO — IT IS **DOWNSTREAM OF `Obj_0`** AND BELONGS IN `S_sector`. ITS "USED AS PRIMITIVE"
CLASSIFICATION WAS A **MISCATEGORIZATION**, NOT AN INDEFINITENESS. *** Established 2026-07-31 by Codex lane
2 under relay 200 (`STAGE8_CORRELATOR_HESSIAN_MAP_RELATION_DOMAIN_FIX_AUDIT_V001.md`, `516d041d…`, seal
verified).

*** THE INDEFINITE COUNT DROPS, AND IT DROPS BY CORRECTING A CATEGORY RATHER THAN BY WISHFUL READING. ***
Q-105's seven now stand as: **four descendants** (`rho_pre`, `U_BR`, effects/domains, **and this map**),
**two indefinite** (the quotient/measure bundle, `B0`), **one circular** (`PrimitiveInventory_0`) — **with
`B0`'s status under test at relay 201.**

**AND PART OF THE MAP IS DEFINITE ALREADY.** *** THE FORMAL RELATION IS FIXED, CONDITIONALLY: the Schur
complement, `H_C[G] = i hbar G^-1`, the Keldysh congruence, and retarded mixed-block extraction. *** **What
remains unfixed is the PHYSICAL DOMAIN** — invertible bilocal `G`, `Log_0`, contacts, boundaries and
endpoint domains — **all of which require the CTP package.**

*** AND IT DELIVERED THE REQUIREMENT STATEMENT RELAY 199 NEEDS, WHICH IS THE POINT OF RUNNING THE TWO
TOGETHER: THE QUOTIENT MUST SUPPLY the gauge-fixed physical space, the branch metric and reality involution,
DeWitt conventions, the measure, contacts, boundaries, and Ward-compatible endpoints. *** **Codex 1's
decomposition can now be checked against a stated requirement rather than judged on its own terms.**

**No sealing today** — prerequisites, test owner and an adversarial quotient countermodel are all absent;
physical verdict `NO_VERDICT`. **Q-92's conditions held again.**

*** SO THE INDEFINITE PROBLEM IS NARROWING TO ONE OBJECT: THE QUOTIENT/MEASURE BUNDLE. It is what the map
waits on, what `Obj_0` waits on, and — if `B0` turns out to be the target rather than an input — the ONLY
genuinely indefinite thing left on the blocker list. ***

---

## Q-108. "Does the quotient/measure bundle decompose?"

*** RULING: YES — BUT INTO **TWO COUPLED PACKAGES**, NOT FOUR PRIMITIVES AND NOT ONE OBJECT. **BOTH HORNS OF
THE REVIEWER'S BINARY ARE REFUTED, TYPE-R EACH.** *** Established 2026-07-31 by Codex lane 1 under relay 199
(`STAGE8_QUOTIENT_MEASURE_BUNDLE_DECOMPOSITION_TEST_V001.md`, `fcb0c232…`, 515 lines, seal verified,
mirrors byte-identical).

```text
old_bundle_is_one_object    = false | TYPE-R
four_independent_primitives = false | TYPE-R

U1  branch/source typing package    compound index ordering + CTP branch metric/
                                    reality/involution + branch/source embeddings on C0
U3  physical-domain package         gauge-fixed physical quotient + descended
                                    invariant contour/spacetime measure
```

*** AND TWO FORMAL LAYERS **ARE** DEFINITE: the index `I = (a, mu, x)` with Keldysh ordering, and the formal
CTP branch metric / reality convention. *** **What is not definite is their PHYSICAL INSTANTIATION** — the
consumer needs them as **completed U1/U3 data on `C0`, derived from `B0`/`C0`.**
`components_sealed_as_I_prim = 0/4 | TYPE-C`.

**The sealed dependency graph reads `B0` feeds `C0`, `U1`, `U2` and `U3`.**

*** SO THE CHAIN CONVERGES: THE QUOTIENT/MEASURE BUNDLE WAITS ON `U1`/`U3`, WHICH WAIT ON `C0`, WHICH WAITS
ON `B0`. AND `B0` IS THE OBJECT EINSTEIN IS TYPING RIGHT NOW UNDER RELAY 201 — THE ONE Q-105 CALLED "THE
OBJECT STILL TO BE CONSTRUCTED, NOT A DEFINITE INPUT." ***

**AND IT DELIVERED THE CONSUMER REQUIREMENT WITHOUT FIXING THE MAP** (correctly — that was Codex 2's item):
the correlator-to-Hessian consumer needs a completed
**`RAW_TO_RETHESS_PHYSICAL_DOMAIN_AND_CONTRACTION_PACKAGE`** — `C0` plus `U1`/`U3` data **sufficient to
contract, quotient, invert, select the physical block, and carry contact/boundary/domain conventions.**
**That matches Q-107's independently-stated requirement from the other side.**

**THE REVIEWER'S FRAMING WAS WRONG AND THE QUESTION WAS STILL PRODUCTIVE.** *** ASKING "FOUR OBJECTS OR
ONE?" FORCED A DECOMPOSITION NOBODY HAD PERFORMED, AND THE ANSWER — TWO COUPLED PACKAGES — IS MORE USEFUL
THAN EITHER OFFERED OPTION. A BINARY CAN BE FALSE AND STILL BE THE RIGHT THING TO ASK. ***

---

## Q-109. "Is `B0` an input or the target?"

*** RULING: THE TARGET — `BOTH_SPLIT`, PRIMITIVE-POSITIONED AND TARGET-STATUSED. THE REVIEWER'S READING IS
CONFIRMED **AND THE CORRECTION IS BAD NEWS, NOT GOOD.** *** Established 2026-07-31 by Einstein under relay
201 (`STAGE8_B0_INPUT_OR_TARGET_ADJUDICATION_EINSTEIN_V001.md`, `3d4ad604…`, 346 lines, seal verified).

**Three independent sealed columns say target in their own words:** the audit's Authority column
(*"TYPE-U, not adopted primitive"*), the audit's own verdict prose inside the INDEFINITE cell (*"not a
definite input"*), and the prefreeze Status column (*"TYPE-U construction debt"*). **Its own spec types it
`B0_Q70_local_classification = TYPE_U_CONSTRUCTION_DEBT`.**

*** RE-BINNING IS NOT PROGRESS, AND THE REVIEWER FRAMED IT AS THOUGH IT WERE. `B0` LEAVES ONE BIN AND
ENTERS ANOTHER; IT LEAVES THE BLOCKER LIST NOT AT ALL, AND STILL HARD-BLOCKS `C0`, `U1`, `U2`, `U3`, ITEM 1
AND THE PACKAGE. AND THE RETYPE MAKES THE OBLIGATION **HEAVIER**: AN INDEFINITE INPUT MIGHT BE SHARPENED BY
FIXING A DEFINITION; **A TARGET MUST BE BUILT.** ***

**AND THE CLEANEST TEST IS THE REGISTER'S OWN GLOSS TURNED AGAINST IT.** Q-105 justified the middle row by
*"an indefinite object in load-bearing use is worse than a missing one, because it looks present."* *** `B0`
DOES NOT LOOK PRESENT — IT IS OPENLY TYPE-U WITH A `would-build` AT EVERY SITE. IT IS THE MISSING ONE THAT
GLOSS CONTRASTS AGAINST. ***

*** THE STRUCTURAL FACT, VERIFIED AT SOURCE (B-P4): "C0 DESCENDS FROM B0; U1/U2/U3 DESCEND FROM THE PAIR
(B0,C0); NONE IS AN INPUT TO B0." **`B0` TAKES NOTHING AND FEEDS EVERYTHING. IT IS THE ROOT OF THE DESCENT
DAG** — which is exactly how it landed on a used-as-primitive list. ***

**WHY "INDEFINITE" WAS THE WRONG WORD:** **`B0`'s ROLE is definite** — sealed identity, fixed direction,
production codomain. **Its CONTENT is undetermined**
(`B0_explicit_mathematical_map_domain_codomain_found = false | TYPE-S`). **So "indefinite" is true
TRIVIALLY, as it is of every unbuilt target, and carries no information beyond TYPE-U.** *** THE FAILING
WORD IS NEITHER "INDEFINITE" NOR "IN USE" — IT IS THE PRESUPPOSITION **"AS A PRIMITIVE"** THAT BOTH
CONJUNCTS RIDE ON. *** **And "INDEFINITE" means something different in `B0`'s row than in the other two:
theirs are used-but-underdetermined; `B0`'s cell is a statement about CATEGORY. The middle row is not one
category but two.** **The row heading also merges `B0_CONSTRUCTION_WITNESS` with its own output — two ends
of one construction edge.**

*** `B0` vs P0: IDENTITY **REFUTED** — four sealed negatives from three independent lanes, each returning
`qualifying_identity_found = false`. **THE PROGRAM IS NOT COUNTING ONE BLOCKER TWICE.** *** **But ordering
is `NO_VERDICT`: no sealed sentence places either in the other's construction inputs.** *** TWO
CONSTRUCTION DEBTS OF THE SAME PHYSICAL SHAPE SIT AT THE ROOTS OF TWO DIFFERENT LADDERS, AND THAT ORDERING
QUESTION IS NOW NAMED. ***

**NO CONSUMER THINKS IT HAS `B0`.** Every dependency is declared conditional and every dependent is itself
unbuilt; the rest are decorative fence lines whose verdicts survive deleting the token. **Q-69 sweep clean.**

**Also found: the audit's Result line says four descendants while its own table has three** — the register
reproduced the table, correctly. **Einstein withdrew two of its own draft claims, including one asserting
`B0` is "not indefinite at all" — the reviewer's stronger reading — as wrong.** **Symmetric framing audited
in both directions: it looked specifically for a single site treating `B0` as supplied, which would have
flipped the ruling, and found none.**

---

## Q-110. "Does the codomain route determine `B0`?"

*** RULING: NO — `codomain_constraints_determine_B0 = false | TYPE-R`. IT FIXES A **FIBER**, NOT A POINT.
*** Established 2026-07-31 by Codex lane 1 under relay 202
(`STAGE8_B0_CODOMAIN_ROUTE_UNDERDETERMINATION_TEST_V001.md`, `ee4dc9df…`, 609 lines, seal verified).
`codomain_route_status = UNDERDETERMINED_FIBER`.

*** BUT IT IS A REAL CONSTRAINT AND THE FAMILY IS NAMED, WHICH IS WHAT THE RELAY ASKED FOR: ***

```text
CodomainCompatibleBoundaryOriginRealizer :=
  (Obj_B0, Sig_B0, Carrier_B0, Core_B0, Prov_B0, DESCEND_B0)
```

**What `B0` must produce IS fixed:** `C0`, and with `C0`, `U1`/`U2`/`U3`, **with common-origin / no-supplement
descent witnesses.** **What remains open is exactly `B0`'s content:** type, arity, domain, codomain,
parameters, carrier and core, representation, descent maps, and the equivalence relation.

**And the theory's own content supplies OBLIGATIONS, NOT A CONSTRUCTOR** — single-origin microscopic
operator, unitary Boundary-Resolved pre-record evolution, causal support, boundary-form vanishing,
generated-carrier requirements, common-origin producer signature. **No independent `B0` constructor exists.**

**THE PRINCIPAL'S BOUNDARY READING IS HALF-CONFIRMED:** *** DETERMINATION-BY-CONSUMERS IS A GENUINE
CONSTRAINT ON `B0` — IT IS NOT A DEFICIENCY AND IT DOES NARROW THE OBJECT. IT SIMPLY DOES NOT NARROW IT TO
ONE. ***

---

## Q-111. "How far does the `I_prim` route reach?"

**RULING: TO PRESENTATION STRUCTURE ONLY. THE EXACT STOPPING POINT IS THE COMPLETE MICROSCOPIC BOUNDARY
OPERATOR/DYNAMICS ITSELF.** Established 2026-07-31 by Codex lane 2 under relay 205
(`STAGE8_IPRIM_ROUTE_TO_B0_STOPPING_POINT_AUDIT_V001.md`, `4c1ba9b5…`, seal verified), **run blind, without
reading lane 1's artifact.**

```text
REACHES     the six Level-1 upstream premises
            historical conversion constants c, hbar, G
            formal index, Keldysh ordering, CTP branch metric/reality conventions

DOES NOT    the physical B0 operator; the dynamics; quotient/measure; rho_pre;
REACH       U_BR; effects/domains; the common-origin certificate
```

**"Only presentation structure is determined."** **No numerical fraction assigned — correctly, since a
fraction would imply a measure nobody has.**

**PRE-REGISTERED CONVERGENCE TEST, WRITTEN BEFORE SEEING LANE 1's ANSWER AS REQUIRED:** *** TYPED-OBJECT
EQUIVALENCE UP TO AN EXPLICIT STRUCTURE-PRESERVING ISOMORPHISM, CHECKED BY BLINDED STRUCTURAL HASHES AND
ADVERSARIAL DISTINGUISHING INPUTS — NOT PROSE OR FLAG AGREEMENT. *** **That is a real test and it was
specified in advance.**

*** THE CONVERGENCE RESULT, AND IT IS NOT THE ONE HOPED FOR: THE TWO ROUTES DO NOT MEET AT AN OBJECT. THEY
MEET AT A **GAP**. *** `I_prim` supplies presentation structure — index, ordering, branch metric — which is
part of what the codomain fiber leaves open under "representation." **But neither route reaches type,
arity, domain, carrier/core, descent maps, or the equivalence relation, and combining them does not.**

*** BOTH INDEPENDENT ROUTES STOP AT THE SAME OBJECT: THE PHYSICAL MICROSCOPIC BOUNDARY OPERATOR. THAT IS
CONVERGENT FAILURE AT ONE POINT, AND IT IS THE STRONGEST EVIDENCE THE PROGRAM HAS THAT `B0` IS A GENUINE
PHYSICAL OBLIGATION RATHER THAN A BOOKKEEPING ARTEFACT. Two lanes, two premise-disjoint methods, run blind,
neither reaching it. ***

---

## Q-112. "Was `B0` ever built and superseded?"

*** RULING: NO. `B0_ever_built = false | TYPE-R` — AN EXECUTED REFUTATION OVER THE VERSION HISTORY, NOT A
NAME SEARCH. *** Established 2026-07-31 by Codex lane 2 under relay 207
(`STAGE8_B0_VERSION_HISTORY_SUPERSESSION_AUDIT_V001.md`, `c5a664e3…`, seal verified).

**The historical boundary-operator, charged-access, Galerkin and null-diamond artifacts are partial or
differently shaped.** *** NONE SUPPLIES COMPLETE SOURCE-RECORD-FIELD DYNAMICS WITH `C0` AND `U1`/`U2`/`U3`.
*** `B0_superseded_recoverable = false | TYPE-S`. **Version-history completeness remains `NO_VERDICT`
pending a signed historical object manifest.**

*** SO THERE IS NOTHING TO RECOVER — AND THE EPISTEMIC STATE THIS ESTABLISHES IS NOT THE ONE THE PROGRAM
MIGHT HAVE ASSUMED. `B0` HAS NEVER BEEN ATTEMPTED IN THE PROGRAM'S ENTIRE HISTORY. ***

**That is different from "tried and failed."** **The withdrawn finite-rank Galerkin route and the
null-diamond family WERE tried and abandoned — both are on record.** *** `B0` ITSELF NEVER WAS. THERE IS NO
EVIDENCE THAT IT IS HARD; ONLY THAT IT IS UNDONE. ***

**THE SEARCH WAS THE RIGHT KIND AND IT CAME BACK CLEAN.** The relay asked for **history, not names** —
supersession chains, withdrawn routes, erratum records, retired ledger entries, `_V001` where `_V002+`
exists — **and typed candidates by SHAPE rather than by name, since a `B0`-shaped object would not have been
called `B0`.** **This program's most repeated finding is that the missing thing already existed under
another name. This time it did not.**

**Third route closed on `B0` in one day: the accessor route (Q-106), the primitive route (Q-111), and now
the historical route. The joint-constraint and incidence routes remain open.**

---

## Q-113. "Does the joint constraint system determine `B0`?"

*** RULING: NO — `joint_system_determines_B0 = false | TYPE-R`. THE FIBER SHRINKS AND DOES NOT COLLAPSE.
*** Established 2026-07-31 by Codex lane 1 under relay 206
(`STAGE8_B0_JOINT_IPRIM_CODOMAIN_CONSTRAINT_SYSTEM_V001.md`, `b765965f…`, 443 lines, seal verified,
mirrors byte-identical).

*** THE SLOT TABLE, WHICH IS WHAT THE RELAY DEMANDED: **0/9 COLLAPSE · 3/9 SHRINK · 0/9 CONFLICT.** ***

```text
SHRUNK   production codomain
         presentation / unit constants
         the formal CTP representation layer

OPEN     type · arity · intrinsic domain/codomain · dynamical parameters
         carrier/core · physical representation · descent maps · equivalence relation
```

**Residual fiber: `IprimPresentedCodomainCompatibleBoundaryOriginRealizer`.**
`B0_constructed_from_joint_system = false | TYPE-C` — missing a concrete candidate, a uniqueness theorem or
selector, full candidate property tests, and an independently failed adversarial countermodel.

*** `0/9 CONFLICT` IS A QUIET POSITIVE AND SHOULD BE RECORDED AS ONE. The relay asked deliberately whether
`I_prim` fixes a slot one way while the codomain constraints require another, and said such an
inconsistency would outrank everything else on the board. **THERE IS NONE. THE CORPUS IS CONSISTENT WHERE
THE TWO ROUTES OVERLAP.** ***

*** AND THE SHAPE OF WHAT REMAINS IS THE FINDING. THE THREE SLOTS THAT SHRANK ARE EXACTLY THE PRESENTATION
LAYER — codomain, units, formal representation. THE SIX STILL OPEN ARE THE STRUCTURAL AND PHYSICAL CONTENT:
TYPE, ARITY, DOMAIN, CARRIER/CORE, **DESCENT MAPS**, AND THE EQUIVALENCE RELATION. ***

**THE ALGEBRAIC ROUTES HAVE NOW SHRUNK EVERYTHING THEY CAN REACH, AND WHAT THEY CANNOT REACH IS PRECISELY
THE COMBINATORIAL DATA A BOUNDARY OPERATOR'S INCIDENCE STRUCTURE WOULD FIX.** *** THAT SETS UP RELAY 208
EXACTLY: FOUR ROUTES HAVE CLOSED — ACCESSOR (Q-106), PRIMITIVE (Q-111), HISTORICAL (Q-112), AND NOW JOINT
(Q-113). ALL FOUR WERE ALGEBRAIC. THE ONLY ROUTE STILL OPEN IS THE ONLY ONE THAT IS NOT. ***

---

## Q-114. "Does the incidence structure determine `B0`?"

*** RULING: NO — AND NOT BECAUSE DETERMINATION FAILS. THERE IS NO ARROW.
`bridge_from_any_incidence_object_to_B0_found = false | TYPE-S`. *** Established 2026-07-31 by Einstein
under relay 208 (`STAGE8_INCIDENCE_STRUCTURE_DETERMINATION_TEST_EINSTEIN_V001.md`, `9cdc25e2…`, 263 lines,
seal verified, fence-clean, **no `= true` flag anywhere**).

**`incidence` × {`B0`,`Obj_B0`,`B_0`} → ZERO across all three roots**, word-boundaried. `BID` × `B0` → three
hits, **all non-identity rows**. `B_chi`/`d_chi` → twelve lines, all definitions, disclaimers, refutation
rows or exclusions. **None is a construction map.**

*** THE FIFTH AND LAST ROUTE. ACCESSOR (Q-106) · CODOMAIN (Q-110) · PRIMITIVE (Q-111) · HISTORICAL (Q-112)
· JOINT (Q-113) · INCIDENCE (Q-114). FOUR WERE ALGEBRAIC; THIS ONE WAS NOT; ALL SIX STOP AT THE SAME PLACE.
TWO LANES RUNNING BLIND CONVERGED ON IT — WHICH IS THE STRONGEST EVIDENCE THE PROGRAM HAS THAT `B0` IS A
GENUINE PHYSICAL OBLIGATION AND NOT A BOOKKEEPING ARTIFACT. ***

**TWO REVIEWER CLAIMS NARROWED BY THE ARTIFACT, BOTH RECORDED AS CORRECTIONS:**

```text
CLAIMED   the signature incompatibility refutes the combinatorial route generally
ACTUAL    the sealed TYPE-R reaches the NAMED B_chi CANDIDATE ONLY (N4, SCOPE-LIMITED).
          The B0 spec's own limiter: it "does not refute a future construction in which
          independently derived primitive dynamics is used by an explicit B0 construction
          witness." Transporting the seal would have been unproved-identity transport.

CLAIMED   the complex K is a free choice
ACTUAL    THIRD STATUS. K is a class and K_L has L free -- but K_(1,3) IS designated at
          V011 :262-263, by TARGET-AWARE PREMISE, gate unpassed. Designated-by-premise,
          not free. Einstein corrected its own headline on this (§7.1).
```

**WHAT IS NOT CLOSED, AND THIS IS THE PART THAT MATTERS.** Two openings survive, both with named release
conditions:

```text
N6 [TYPE-C]   BID_conditional_determination_route_credited = false
              *** THE ROUTE EXISTS *** (:657-662, :709-710, :795-798).
              Release: Gates 2/3/4 executed and passed -- ALL THREE NEVER RUN --
              plus BID_v011_specification_sealed = false.
              TYPE-C IS CONSTRAINT-BLOCKED, NOT REFUTED. AN UNOPENED ROUTE, NOT A DEAD ONE.

N4 limiter    the B0 spec NAMES THE SHAPE OF A CONSTRUCTION IT WOULD ACCEPT:
              independently derived primitive dynamics + an explicit B0 construction witness.
```

**AND MD-3 IS THE SEQUENCING FINDING.** `B0_DESCENT_NON_DEGENERACY` — from Einstein's relay 203 — is
**still on no blocker list**, is cheap, and is **blocked behind nothing**. Without it, `B0` is not merely
unbuilt but **UNPINNED**: no test the corpus can run, and none in the sealed battery even after every named
blocker lands, could distinguish a real `B0` from an object that does no work at all. **CM-3 survives a
combinatorially rich interior** (N10, executed) — a candidate may carry the full incidence skeleton as
declared internal data and remain indiscriminable.

*** MD-3 IS THE SAME OBJECT AS THE REVIEWER'S "DOES THE FIBER ACT ON THE ROAD?" QUESTION, REACHED
INDEPENDENTLY FROM THE OTHER SIDE. Descent non-degeneracy asks whether a candidate `B0` does any downstream
work; the fiber question asks whether distinct realizers in `IprimPresentedCodomainCompatibleBoundaryOrigin-
Realizer` produce the same `C_record`. **THEY ARE ONE TEST, AND IT IS THE ACCEPTANCE CRITERION FOR ANY `B0`
BUILD.** ***

**N7 [TYPE-S] IS A THIRD IMPORT STRUCK:** `sealed_decomposition_B0_as_skeleton_plus_content_found = false`.
**No sealed statement says `B0` = (combinatorial part) + (physical content).** Assembling the parts would
not assemble `B0` even if every part were determined.

**N11 [TYPE-R, executed]: `a_new_Q80_class_was_required = false`. TYPE-R/U/S/C sufficed.** *** FIRST TIME
THE EXISTING TYPING VOCABULARY HAS HELD UNDER A NEW OBJECT. The lane records having struck four manufactured
classes and declining to add a fifth. AFTER TWELVE DISSOLVED FRAMINGS, THE VOCABULARY STOPPED NEEDING
EXTENSION — THAT IS A METHOD RESULT, NOT A NULL. ***

**Einstein's own named seam, carried forward unresolved:** whether the corpus's *"target-independent"* means
**inputs** or **specifications**. Unfixed, that reading is the exact seam through which a target-dependent
construction could be presented as target-independent **with no test able to tell**. Compounded by N2 —
`K_(1,3)` is designated by a **target-aware** premise.

---

## Q-115. "Is the N4 limiter route — `independently derived primitive dynamics` — satisfiable from the corpus?"

*** RULING: NO AS THINGS STAND. THE CORPUS'S PRIMITIVE DYNAMICS IS **ADOPTED**, NOT DERIVED, AND SAYS SO
IN ITS OWN WORDS. *** Established 2026-07-31 by the reviewer, tracing Q-114's N4 limiter. **Read at source;
no lane involved.**

**The chain, each link quoted:**

```text
B0 spec        the limiter: the B0 stop-spec "does not refute a future construction in which
               INDEPENDENTLY DERIVED primitive dynamics is used by an explicit B0 construction
               witness."  (STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md:727)

A24            "Connected primitive dynamics additionally requires an EXPLICITLY ADOPTED OR
               INDEPENDENTLY DERIVED global-boundary-descent/quasi-free-completeness rule."
               (BID_CONSOLIDATED_HOSTILE_AUDIT_MATRIX_V005.md:74, status PENDING)

the rule       BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md EXISTS -- 220 lines.
               *** AND IT TOOK THE ADOPTED BRANCH. ***
```

**Its own §"Adopted primitive principle", verbatim (`:22-25`):**

> *"This is an additional microscopic Gravacle premise. **It does not follow from CAR, locality, or
> disjoint monoidality alone.** It is **target-value-free but historically target-aware**, and is
> **forward-adopted before further evaluation** under this branch."*

**Status flags (`:193-197`):** `global_boundary_descent_principle_adopted = true` ·
`primitive_quasi_free_completeness_adopted = true` · `forward_adopted_before_further_branch_evaluation =
true` · **`historically_target_blind = false`** · `target_value_used_in_construction = false`.

*** SO THE ONE ROUTE THE `B0` SPEC ITSELF NAMES AS ACCEPTABLE REQUIRES **INDEPENDENTLY DERIVED** PRIMITIVE
DYNAMICS, AND WHAT THE CORPUS HAS IS **ADOPTED** — BY AN ARTIFACT THAT STATES IT DOES NOT FOLLOW FROM ITS
OWN STRUCTURAL INPUTS. THE N4 LIMITER IS NOT SATISFIABLE WITHOUT DERIVING THIS RULE FIRST. ***

**AND THE SHARPER EDGE — THE EXCLUSION IS DOING PHYSICAL WORK.** The principle reads: *"No independent
primitive higher-CAR, record-only, contact, or overlap kernel is allowed."* And
`BID_SOURCE_PARENT_CLOSURE_GATE_V002.md:54` records:

```text
primitive_quartic_competitor_rejected_only_by_adopted_quasi_free_completeness: true
```

*** THE WORD IS "ONLY." A QUARTIC COMPETITOR — DESCRIBED IN SP07 AS "OTHERWISE INVISIBLE," AGREEING ON THE
VACUUM AND ONE-SOURCE SECTORS — IS EXCLUDED **SOLELY** BY THE ADOPTION. DROP THE PREMISE AND A RIVAL
PRIMITIVE DYNAMICS SURVIVES. THAT IS NOT BOOKKEEPING; IT IS AN ALTERNATIVE MICROSCOPIC DYNAMICS HELD OUT BY
A CHOICE. *** `BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_AUDIT: PASS_BLOCKED`.

**A NINTH DEBT-IN-AXIOM-CLOTHING, AND IT SITS ON THE ONE NAMED ROUTE TO `B0`.** Q-74 counted eight on the
value path. **This one was not among them** because it was reached from the `B0` side, which nothing had
traced before.

*** AND IT IS A LOAD-BEARING EXEMPLAR FOR RELAY 210. "Target-value-free but historically target-aware" is
the corpus stating, in one sentence, that it is clean on the **INPUTS** reading and **NOT CLEAN ON THE
SPECIFICATIONS** reading. **HELD BACK FROM CODEX 2 DELIBERATELY** — 210 asks the lane to find the
load-bearing uses independently, and handing over the best exemplar would contaminate the sweep and destroy
its value as a check on thoroughness. **Compare on return.** ***

**What this does NOT establish:** that the rule is underivable. It is adopted, and no one has tried to
derive it. **TYPE-C, constraint-blocked — a derivation obligation with no attempt on record, not a
refutation.**

---

## Q-116. "Can a `B0` candidate be discriminated from one that does no work?"

*** RULING: YES — MD-3 IS SPECIFIED AND IT IS NOT VACUOUS. `CM3_passes_MD3 = false | TYPE-R`. ***
Established 2026-07-31 by Codex lane 1 under relay 209
(`STAGE8_B0_MD3_DESCENT_NON_DEGENERACY_ACCEPTANCE_TEST_V001.md`, `23f54271…`, 492 lines, seal verified,
fence-clean).

*** THIS IS THE FIRST ACCEPTANCE TEST THE PROGRAM HAS EVER HAD FOR ITS ROOT OBJECT. BEFORE TODAY A BUILT
`B0` COULD NOT HAVE BEEN CHECKED AT ALL. ***

**CM-3 fails because total constant descent maps make nontrivial candidate variation invisible to every
descendant** — the countermodel that survived the accessor, codomain, primitive, historical, joint and
incidence routes, and survived a combinatorially rich interior in relay 208, does not survive this.

**MD-3 consumes:** a `B0` candidate packet · executable `DESCEND_B0` · `C0`/`U1`/`U2`/`U3` with
`d_C0`/`d_U1`/`d_U2`/`d_U3` · a target-independent probe family · frozen candidate and descendant
equivalence relations.

**THE FIBER QUESTION IS NOT ANSWERED.** `fiber_action_on_C_record_today = NO_VERDICT`, blocked on four
named absences: **the `C_record(K)` extraction/evaluation map; the response layer; the candidate
equivalence relation; and no pair `r,r'` constructed or run.**

*** AND THE LANE BUILT IN A SAFEGUARD THE REVIEWER DID NOT ASK FOR, WHICH IS THE RIGHT ONE. *** The two
future verdicts are asymmetric by design (`:381-389`): `fiber_acts_on_road = true` needs only **one**
MD3-distinct pair giving a non-equivalent `C_record`, but `fiber_is_gauge_relative_to_road = true`
additionally requires **a sealed equivalence theorem that the equality is not an artifact of a missing
extractor or collapsed test domain.** **THAT GUARDS AGAINST DECLARING THE FIBER FLAT WHEN THE TEST IS
MERELY BLIND — the exact failure a reviewer hoping for "gauge" would have walked into.**

**Reviewer note:** the artifact's only two `= true` flags sit under *"Possible future verdicts"* and are
branch definitions, not results. **Checked at source before registering (Q-69).**

---

## Q-117. "Does the corpus fix whether `target-independent` means inputs or specifications?"

*** RULING: NO. THE SEAM IS OPEN — AND §5.3'S ANTI-NARROWING DEFENCE IS **NOT EXECUTABLE**. ***
Established 2026-07-31 by Codex lane 2 under relay 210
(`STAGE8_TARGET_INDEPENDENCE_SEAM_AUDIT_V001.md`, `834e5041…`, 64 lines, seal verified).

```text
NO corpus-wide definition fixes the term.

SPECIFICATIONS reading   5.3's anti-narrowing defence is DIRECTIONALLY VALID BUT NOT
                         EXECUTABLE -- the admitted-family census and provenance are UNFROZEN.
INPUTS-only reading      a target-aware family could still be selected while numerical target
                         data are absent.
K_(1,3)                  CONFIRMED specification-level target-aware; designates the rooted-star
                         sub-object and fixes downstream dimensions; accounting gate unpassed.
```

*** THE CONSEQUENCE, STATED PLAINLY: THE PROGRAM CANNOT CERTIFY A NUMBER EVEN IF IT HAD ONE. §5.3 IS THE
GATE THAT WOULD ESTABLISH A COMPUTED ALPHA WAS FORCED RATHER THAN FITTED, AND ITS PRIMARY CLAUSE CANNOT
CURRENTLY BE RUN. THAT IS A MISSING CAPABILITY AT THE END OF THE ROAD, NOT A DELAY. ***

**SWEEP GAP — RECORDED, NOT HELD AGAINST THE LANE.** The audit is 64 lines and **did not surface
`BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md`**, whose `:22-25` reads *"target-value-free
but **historically target-aware**"* — **the corpus stating the inputs/specifications distinction about
itself, in one sentence, on a load-bearing microscopic premise.** The reviewer had found it independently
(Q-115) and **held it back deliberately as a thoroughness check.** *** THE CHECK FIRED. The sweep is not
complete and must not be treated as a corpus-wide negative. *** It is supplied to the lane in relay 212.

**This does not downgrade the ruling** — the finding is that no definition exists, and the missed exemplar
**strengthens** rather than weakens it.

---

## Q-118. "Is §5.3 reachable at all — and is the open action-form class the same object as its admitted family?"

*** RULING: REACHABLE. `Section_5_3_reachable_in_principle = true | TYPE-C`, condition: a frozen pre-root
census and provenance. AND THE TWO OBJECTS ARE OVERLAPPING BUT NOT IDENTICAL. *** Established 2026-07-31 by
Codex lane 2 under relay 212 (`STAGE8_SECTION53_ADMITTED_FAMILY_CENSUS_REACHABILITY_AUDIT_V001.md`,
`4411b91a…`, 65 lines, seal verified, fence-clean).

```text
OPEN_ACTION_FORM_not_enumerable          = false | TYPE-S   no text proves undecidability or an
                                                            intrinsically unbounded membership predicate
OPEN_ACTION_FORM_complete_census_present = false | TYPE-U   would-build: enumerate members + provenance
Section_5_3_reachable_in_principle       = true  | TYPE-C   condition: frozen pre-root census
Section_5_3_executable_now               = false | TYPE-U
```

*** THE FEARED OUTCOME DID NOT MATERIALIZE. "Open" means **NOT YET ENUMERATED**, not non-enumerable — the
envelope's own text says its axes ARE enumerated and typed, and what is missing is a numeric measure or
complete internal parametrization, **not the typed shape**
(`STAGE8_ALLOWANCE_ENVELOPE_WITH_CLOTHING_WITHDRAWN_V001.md:67-75`). ***

**2.1 — the objects separate.** §5.3 quantifies over the **gate-specific admitted family of
response-changing microscopic constructions** (`STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:581`). The
envelope is a **set-valued typed envelope** with scalar, discrete, operator/action-form, algebraic,
admissibility and categorical axes (`…ALLOWANCE_ENVELOPE…:55-75`). **The §5.3 family is a gate-specific
subset or projection.** *** THE OPEN ACTION-FORM CLASS REACHES §5.3 **ONLY IF ITS MEMBERS ARE ADMITTED
MUTATIONS** — AND THE ENVELOPE NAME ALONE DOES NOT PROVE THAT INCLUSION. THAT CONDITIONAL IS NOW THE
CHEAPEST OPEN QUESTION ON THE STEP-3 SIDE. ***

*** AND THE SCHEDULING CONSEQUENCE IS THE REAL FINDING, LARGER THAN THE HEADLINE. §2.3: "FREEZE IT
**BEFORE ANY ROOT IS SEEN**." THE CENSUS CANNOT BE BUILT AFTER THE NUMBER EXISTS WITHOUT DESTROYING THE
VERY PROPERTY §5.3 CHECKS. SO THIS IS **NOT END-OF-ROAD WORK** — IT MUST PRECEDE STEPS 1 AND 2 COMPLETING,
OR THE GATE IS COMPROMISED BY CONSTRUCTION. THE PROGRAM HAS BEEN TREATING §5.3 AS THE LAST THING. IT IS NOT.
***

**What freezing requires (§2.3), as specified:** a ledger of every admitted response-changing family member
carrying canonical object identity · exact domain/codomain · action form and branch choices · source/record
embeddings · provenance and adoption time · **target-awareness declaration** · mutation relation · **and a
proof that the ledger's membership predicate covers all envelope axes**. Plus a dedicated owner running the
mutation audit **and an adversarial omitted-member countermodel**. **Any unclassified member keeps §5.3
unexecutable.**

**CALIBRATION CHECK PASSED.** The lane was handed `BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md`
after its 210 sweep missed it; this audit **found it at `:17-25`**, confirmed it as an inputs/specifications
instance, **and correctly declined to let it bear on non-enumerability.** *** THE LANE DID NOT OVER-READ A
SUPPLIED EXEMPLAR — WHICH IS THE FAILURE MODE HANDING ONE OVER RISKS. ***

**REVIEWER DEFECT, RECORDED.** The reviewer's automated `= true` pre-scan **missed
`Section_5_3_reachable_in_principle = true`** because the pattern required a lowercase leading character.
**A capitalized flag would have been invisible to every fence scan run this session.** *** SAME
WORD-MATCHING FAILURE CLASS THE CORPUS, THE AUDIT SCRIPT, THE AUDIT OF THE AUDIT AND THIS REGISTER HAVE ALL
HIT — NOW IN THE REVIEWER'S OWN CHECK. Scans must be case-insensitive on the identifier. ***

---

## Q-119. "Can the Quasi-Free Completeness rule be derived?"

*** RULING: NOT AS THE CORPUS STANDS.
`global_boundary_descent_quasi_free_completeness_derived = false | TYPE-U`, would-build: **an independent
primitive completeness theorem.** *** Established 2026-07-31 by Codex lane 1 under relay 213
(`STAGE8_QUASI_FREE_COMPLETENESS_DERIVABILITY_AUDIT_V001.md`, `d463ce15…`, 458 lines, seal verified,
fence-clean).

*** THE DIAGNOSIS IS SHARPER THAN THE VERDICT, AND IT IS THE VALUE OF THIS RELAY: THE CORPUS DERIVES THE
**LIFT INSIDE** THE ADOPTED PRIMITIVE CLASS — `operator_valued_quasi_free_CAR_lift_derived = true`, which
is real — **BUT DOES NOT DERIVE THE CLASS BOUNDARY ITSELF.** The theorem that exists lives inside the very
fence whose placement is the question. ***

**THE COMPETITOR IS PHYSICALLY DISTINGUISHABLE, AND THAT IS THE FINDING NOBODY HAS ACTED ON.**

```text
the quartic competitor IS DETECTED, and it DIFFERS ON THE TWO-SOURCE SECTOR.
its rejection is EXACTLY BY THE ADOPTED PREMISE UNDER TEST -- not by any independent no-go theorem.
```

*** SO THE TWO MICROSCOPIC LAWS ARE NOT OBSERVATIONALLY IDENTICAL. THERE IS A SECTOR WHERE THEY DISAGREE.
THE PROGRAM EXCLUDES THE RIVAL BY FIAT WHILE A PHYSICAL DISCRIMINATOR SITS UNUSED. *** SP07 called the
competitor *"otherwise invisible"* — **that is true on the vacuum and one-source sectors and FALSE on the
two-source sector.** The invisibility was always scope-limited; nothing had said where the scope ended.

**THE DEBT IS THEREFORE DISCHARGEABLE IN PRINCIPLE.** TYPE-U with a named would-build is work-state, **not
a refutation and not an axiom**. *** BUT Q-82 APPLIES AND MUST NOT BE SKIPPED: PATHLESSNESS IS DIAGNOSTIC,
AND IF NO PRINCIPLE BEARS ON THE TWO-SOURCE SECTOR, THIS IS TERMINAL — AND TERMINAL IS WHAT AN AXIOM LOOKS
LIKE. WHICH IT IS HAS NOT BEEN ESTABLISHED. ***

**Status as it stands:** *"an adopted Road A step-1 premise unless and until an independent primitive
completeness theorem is supplied."*

**Reviewer note (Q-69 discipline):** the artifact contains
`primitive_quasi_free_completeness_derived = true` and `global_boundary_descent_principle_derived = true`
at `:450-451`. **Both sit under the heading *"What does not exist is:"*** — absent flags being named, not
asserted. **Checked at source. The lane's summary was accurate.** *** THIS IS THE THIRD ARTIFACT TODAY
WHOSE `= true` LINES ARE HYPOTHETICALS. A FLAG SCAN THAT DOES NOT READ THE SURROUNDING HEADING PRODUCES A
FALSE POSITIVE EVERY TIME. ***

---

## Q-120. "Is the open action-form class inside §5.3's admitted family?"

*** RULING: SPLIT — AND THE BLOCKER IS NOT THE CRITERION, IT IS MISSING MEMBER IDENTITIES. ***
Established 2026-07-31 by Codex lane 2 under relay 214
(`STAGE8_OPEN_ACTION_FORM_ADMISSION_TO_SECTION53_AUDIT_V001.md`, `fd688838…`, 65 lines, seal verified,
fence-clean, no `= true`).

```text
S_0 and S_1   ARE admitted mutation candidates under 5.3's action-partition criterion.
other classes NOT INDIVIDUALLY CLASSIFIABLE -- they lack concrete member identities and provenance.

open_action_form_complete_cardinality = NO_VERDICT | TYPE-U | would-build: pre-root member manifest
open_action_form_members_all_admitted = NO_VERDICT | TYPE-U | criterion applies; members unnamed
Section53_census_frozen               = false | TYPE-C
Section53_executable_now              = false | TYPE-U
```

*** THE CENSUS IS AT LEAST 2 AND ITS TOTAL SIZE IS UNRESOLVED. THE CRITERION WORKS — IT WAS APPLIED
SUCCESSFULLY TWICE. WHAT IS MISSING IS THE MEMBERS THEMSELVES. THAT MAKES STEP 3'S BLOCKER A NAMING AND
PROVENANCE TASK, NOT A CONCEPTUAL ONE. ***

---

## Q-121. "Is `B0`'s one-ness derived or imported?"

*** RULING: NEITHER — IT IS **ASSUMED**. POSTULATED IN TWO SEALED TERMINAL AXIOMS, DERIVED NOWHERE, AND NOT
A METHOD IMPORT. AND NOTHING WEAKER REPLACES IT. *** Established 2026-07-31 by Einstein under relay 211
(`STAGE8_ONE_OPERATOR_PREMISE_ADJUDICATION_EINSTEIN_V001.md`, `36e300ab…`, 336 lines, seal verified,
fence-clean, **no `= true` anywhere**).

**182 sites across 55 files. DERIVED: ZERO.**

```text
A1   the "one complete parent" Level-1 family -- THE AXIOM MAP'S OWN ROW: "Reason given? No"
A5   transport-only = single-operator completeness, with its own self-concession:
     *** "Gauge and Lorentz covariance alone do not imply this rule." ***
method layer re-imports it (~40 sites); ~150 inherited sites all terminate there
BID states its own status: "excluded by the BID postulate, not proved absent by restating that postulate"
```

**No weaker relation delivers.** W1 (joint constraint) fails T4/T5 verbatim and collapses on a dilemma —
a parameter-bearing tie is barred, a parameter-free one **is** single-carrier descent. W2 fails or reifies.
W3 is a genuinely different requirement. W4 is not weaker — it exposes a **hidden fusion of token one-ness
with type one-ness**, the latter well-posed only after the open equivalence-relation slot and MD-3.

*** SO THE SIX ROUTES WERE MEASURING THE RIGHT OBJECT — UNDER AN ADOPTED PREMISE. ***

*** AND THE PROGRAM NOW HAS A FINITE NAMED LIST OF WHAT WOULD END THE ASSUMPTION, WHICH IT HAS NEVER HAD
FOR ITS OWN FOUNDATION. `NECESSITY_DERIVED` IS CLAIMABLE AT EXACTLY THREE RELEASES: ***

```text
R1   the induced-only derivation
R2   the map + projector
R3   the quasi-free-completeness derivation      <-- SEE Q-122
```

**Also established:** **no T1–T7 clause tests P0** — source-oneness is **signature-assumed and
test-unverified**; the only "one" inside a failure-capable test constrains the **completed carrier, not the
source**. And rank-1 `:433` says common origin *"does not derive induced-only action."*

**GRAPH-WALKER PREDICTION: REFUTED**, scoped to the six returns, **signatures pre-registered before
reading.** Three grounds: this program's walkers **demonstrably do see written fixed points** (Q-86
classified P7; the executed census reported **zero actual cycles** — OBS-08's phenomenology is an untested
import **with an executed counterinstance**); the specific residue is **absent from all six returns**, the
would-be defining relation being among the **OPEN** slots (absent, not present-but-unresolvable); and the
coarse match is double-entailed. *** THIRTEENTH FRAMING TO DISSOLVE. THE REVIEWER'S, OFFERED AS "A
MECHANISM AND NOT A HOPE." ***

**NOT refuted:** `H_FIXEDPOINT` as the **ontology** of `B0` — `NO_VERDICT`, non-verdict tilt toward
absence. **Six archaeological searches cannot separate an unwritten fixed-point relation from an unwritten
operator.**

**The lane again folded corrections against itself (§7):** its own census arithmetic refuted (one family →
two axioms — substance strengthened, count wrong), and **a transport-error leg struck from its own W1/W2
analysis — Q-99's schema sentence used beyond its seal, the exact error class this relay names, committed
by its draft and caught by its verifier.**

---

## Q-122. "Does any sealed principle decide the two-source sector?"

*** RULING: NOTHING BEARS. `two_source_sector_deciding_principle_found = false | TYPE-S`. ***
Established 2026-07-31 by Codex lane 1 under relay 215
(`STAGE8_TWO_SOURCE_SECTOR_PRINCIPLE_ROUTE_AUDIT_V001.md`, `c82c54c6…`, 436 lines, seal verified,
fence-clean, no `= true`).

*** ROUTE STATUS, THE LANE'S OWN TYPING:
`GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS = AXIOM_CURRENT / TERMINAL_DEBT_CURRENT`. ***

**THE DISCRIMINATOR IS REAL AND CONCRETE:**

```text
adopted law   has H_K
the rival     adds lambda n_i n_j tensor I_R
              *** THE EXECUTABLE DETECTS THE RESULTING TWO-SOURCE-SECTOR DIFFERENCE. ***
```

**But every existing exclusion route does one of three things:** validates the **adopted lift only**; is
**explicitly insufficient**; or **rejects the rival by the adopted quasi-free premise itself** — which is
circular.

*** SO R3 HAS NO ROUTE FROM INSIDE THE CORPUS. Q-82 APPLIES AS WRITTEN: PATHLESSNESS IS DIAGNOSTIC, A NODE
WITH NO DISCHARGE ROUTE IS TERMINAL, AND TERMINAL IS WHAT AN AXIOM LOOKS LIKE. THE LANE TYPED IT
`AXIOM_CURRENT` WITHOUT BEING ASKED TO. ***

**TYPE-S, not TYPE-R — and the distinction is the whole of it.** Nothing in the corpus decides it. **That
is not the same as undecidable.** Deriving one-ness is still possible; **it just cannot be done by
archaeology. It needs a principle from outside the corpus.**

*** AND THERE IS A GENUINE POSITIVE BURIED HERE THAT SHOULD NOT BE LOST: THE AXIOM IS **FALSIFIABLE IN
PRINCIPLE**. `lambda n_i n_j tensor I_R` VERSUS `H_K` IS A SPECIFIC STRUCTURAL DIFFERENCE AND THE
EXECUTABLE ALREADY DETECTS IT. THIS IS A POSTULATE THAT COULD BE SHOWN WRONG — WHICH IS STRICTLY BETTER
THAN ONE THAT COULD NOT. ***

---

## Q-123. "What would a computed alpha actually rest on — is the '18 axioms : 8 clothing' inventory current?"

*** RULING: NO. THE COUNT IS **9 CLOTHING, NOT 8** — AND THE MISSING ONE IS THE ONE ADOPTION WITH A
NAMED, ADMISSIBLE, UNEXCLUDED RIVAL. *** Established 2026-07-31 by the reviewer, tracing the floor claim
against today's Q-115/Q-119/Q-122 findings. **Read at source; no lane involved.**

*** THE FINDING IS ALGEBRAIC AND MUST BE STATED THAT WAY. `H_K` VERSUS `H_K + lambda n_i n_j tensor I_R`:
BOTH ADMISSIBLE, DIFFERING ON THE TWO-SOURCE SECTOR, AND **NOTHING IN THE CORPUS EXCLUDES THE SECOND**
(Q-122, `two_source_sector_deciding_principle_found = false | TYPE-S`). A DERIVATION FORCES A NUMBER ONLY
IF NO RIVAL PREMISE IS EQUALLY ADMISSIBLE. HERE ONE IS. THAT — NOT ANYONE'S KNOWLEDGE OR INTENT — IS THE
DEFECT, AND IT IS EXACTLY WHAT §5.3's "NO INEQUIVALENT ADMITTED POSITIVE ROOT" TESTS. ***

**FRAMING CORRECTION, PRINCIPAL-DIRECTED, 2026-07-31.** An earlier draft of this entry led with
*"historically target-aware."* **That was wrong as a headline.** *** THE AUTHOR'S KNOWLEDGE IS NOT A
PROPERTY OF THE MATHEMATICS. A valid derivation from stated axioms is valid regardless of what anyone knew
while writing them. *** The provenance flag is a **pointer** to where an unexcluded rival might be found —
a search heuristic, never a verdict. **The rival is the finding. Provenance is a footnote.**

**The one place history legitimately enters, and it is not psychological:** §5.3 forbids **narrowing the
admitted family after the root is seen.** That is a fact about the **order of operations recorded in the
provenance** — fixed before or after the number existed — checkable from adoption timestamps. **That is
why the census ledger carries an adoption-time field and why Q-118 requires freezing before any root
exists.** *** ORDER OF OPERATIONS, NOT STATE OF MIND. ***

**The finding, verifiable in one step:** `GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS` **appears
nowhere in `STAGE8_BOUNDARY_LEAF_TYPING_AXIOMS_VS_DEBTS_EINSTEIN_V001.md`** — not among the 18 axioms, not
among the 8 clothing items, not in the debt reachability section. **Yet Q-122 typed it
`AXIOM_CURRENT / TERMINAL_DEBT_CURRENT`.**

*** AND THE MECHANISM OF THE MISS IS EXACT, WHICH IS WHAT MAKES THIS A FINDING RATHER THAN A COMPLAINT.
A24 CONTAINS **TWO ADJACENT "DERIVE OR EXPLICITLY ADOPT" CLAUSES**: ***

```text
CLAUSE 1   "The record theory must derive or explicitly adopt a strong symmetric-monoidal functor
            into (Hilb,tensor) before tensor composition is used."
            *** CAPTURED -- clothing item 8, SECTOR-INDEPENDENCE / MONOIDAL FUNCTOR,
            "marker (iii): A24 'derive OR explicitly adopt' PENDING with the adopt arm taken." ***

CLAUSE 2   "Connected primitive dynamics additionally requires an explicitly adopted or
            independently derived global-boundary-descent/quasi-free-completeness rule."
            *** MISSED. SAME SENTENCE, SAME STRUCTURE, SAME ADOPT-ARM-TAKEN OUTCOME. ***
```

**Why it matters more than a count.** The floor artifact's §2 concludes *"THE FLOOR, AS A FLOOR, IS BETTER
NEWS THAN THE REGISTER RECORDS."* *** THAT ASSESSMENT WAS MADE OVER A SET THAT DID NOT CONTAIN THIS
ADOPTION — AND THEREFORE NEVER ASKED WHETHER IT HAS AN UNEXCLUDED RIVAL. IT DOES. The assessment is not
refuted; it was simply made over an incomplete set. ***

**WHAT IS NOT DISTURBED, AND SHOULD BE SAID PLAINLY:**

```text
"DOES ANY AXIOM CARRY ABSOLUTE SCALE? NO."       UNDISTURBED. The quasi-free rule carries no scale;
                                                 C_R = 1 remains the only scale-carrying leaf and
                                                 remains CLOTHING, not axiom. Q-58 stands.
the 18-axiom floor itself                        UNDISTURBED as a floor. This is a NINTH CLOTHING
                                                 ITEM, not a nineteenth axiom.
```

*** SO THE ANSWER TO "WHAT WOULD A COMPUTED ALPHA REST ON" IS: 18 AXIOMS + **9** DEBT-IN-AXIOM-CLOTHING
ADOPTIONS, OF WHICH **ONE HAS A NAMED ADMISSIBLE RIVAL THAT NOTHING RULES OUT**, AND IT SITS ON THE
PRIMITIVE DYNAMICS — WHICH IS PRECISELY WHAT "INDUCED" IS SUPPOSED TO MEAN. *** **The work this implies is
ordinary mathematics: exclude the rival, or record that nothing does.** *** IT IS NOT AN AUDIT OF ANYONE'S
INTENT. ***

**AND THE ASSET, WHICH MUST TRAVEL WITH THE LIABILITY (Q-122).** *** THIS NINTH ITEM IS **FALSIFIABLE IN
PRINCIPLE** — `H_K` VERSUS `H_K + lambda n_i n_j tensor I_R`, DIFFERING ON THE TWO-SOURCE SECTOR, WITH THE
EXECUTABLE ALREADY DETECTING THE DIFFERENCE. *** Compare clothing items 1 and 4, which Q-45 flags as the
two worst precisely because they are **UNTESTED with no frozen falsifier / kill-test blocked**. **On the
one dimension that separates a live postulate from an inert one, the newly-counted item is stronger than
two that were already counted.**

**Reviewer note on method.** This was found by **tracing a claim rather than searching for a keyword** —
the inventory was not wrong about anything it contained; it simply never reached the second half of a
sentence. *** SUBSTRING AND NAME MATCHING HAVE NOW PRODUCED FALSE NEGATIVES AS WELL AS FALSE POSITIVES IN
THIS PROGRAM. A COMPLETENESS CLAIM OVER AN INVENTORY IS ONLY AS GOOD AS THE SWEEP THAT BUILT IT. ***

---

## Q-124. "What are the open action-form classes, concretely?"

*** RULING: THREE, AND THEY ARE NOW NAMED. *** Established 2026-07-31 by Codex lane 2 under relay 216
(`STAGE8_OPEN_ACTION_FORM_MEMBER_MANIFEST_V001.md`, `e042f0aa…`, 59 lines, seal verified, fence-clean, no
`= true`).

```text
CONCRETE ADMITTED   S_0, S_1 -- admitted action-partition mutations
SCHEMATIC OPEN      1. higher-derivative source terms          UNDECIDABLE | TYPE-U
                    2. different finite causal updates         UNDECIDABLE | TYPE-U
                    3. record-curvature / dissipative mutations UNDECIDABLE | TYPE-U

open_class_cardinality      = NO_VERDICT | TYPE-U
action_form_manifest_complete = false | TYPE-C
Section53_census_frozen     = false | TYPE-C   (the freeze is a separate act; not performed)
```

**All ledger fields beyond class name are MISSING for the three.** *** THE LANE DID NOT CLAIM
COMPLETENESS AND DID NOT FREEZE — BOTH EXPLICITLY REQUIRED BY THE RELAY, BOTH HONOURED. ***

*** REVIEWER FRAMING WITHDRAWN. The relay asked the lane to ENUMERATE the family. CLASS 1 IS AN INFINITE
TOWER — that is what a non-renormalizable gravitational effective action looks like, not a defect.
DEMANDING A FINITE LIST WAS A BOOKKEEPING STANDARD IMPORTED WHERE PHYSICS HAS BETTER MACHINERY. The
question is not "how many members" but "does the tower move the answer." ***

---

## Q-125. "Is the `DeltaPhi = pi` threshold protected against the higher-derivative tower?"

*** RULING: SPLIT, AND THE SPLIT IS THE FINDING. **`pi` IS PROTECTED AND DERIVED. THE FUNCTION COMPARED
TO IT IS NEITHER.** *** Established 2026-07-31 by Codex lane 1 under relays 218 + 219
(`STAGE8_DELTAPHI_PI_PROTECTION_DETERMINATION_V001.md`, `031eb087…`, 463 lines, seal verified,
fence-clean).

**THE POSITIVE, AND IT IS REAL CONTENT — WE NOW KNOW WHY IT IS `pi`:**

```text
primitive_phase_record_map_derived            = true
first_orthogonality_target_pi_protected       = true
DeltaPhi_target_value_pi_is_periodicity_fixed = true
protection_scope = fixed primitive U(1) two-character record map
```

*** `pi` IS **THE FIRST ORTHOGONALITY VALUE OF THE PRIMITIVE CHARACTER-PAIR RECORD MAP**. IT IS NOT A
FITTED COEFFICIENT AND NOT A RESPONSE NORMALIZATION. Changing local action coefficients changes what
accumulated phase a process produces; **it does not change the zero of this fixed overlap map** unless it
changes the record map, character pair, or state. ***

**THE NEGATIVE, IN THE ARTIFACT'S OWN WORDS:** *"the sealed compact-phase argument protects the **target**
of the comparison, not the **function** being compared to it."*

```text
DeltaPhi_map_protected_against_action_form_mutations = false | TYPE-U
DeltaPhi_function_of_K_and_XK_derived                = false | TYPE-U
higher_derivative_tower_moves_DeltaPhi               = NO_VERDICT
leading_higher_derivative_correction_identified      = false | TYPE-U
higher_derivative_suppression_stated                 = false | TYPE-U
```

*** SO EXACTNESS IS UNRESOLVED AND STAYS THAT WAY UNTIL THE COMPLETED GENERATOR/RESIDUAL AND THE
ACTION-FORM CLOSURE THEOREM EXIST. THE PROGRAM PRESENTS ALPHA AS AN EXACT PURE NUMBER; THAT CLAIM IS
CURRENTLY UNSUPPORTED IN A GRAVITATIONAL EFT, AND NOW HAS A NAMED WOULD-BUILD RATHER THAN NO ROUTE. ***

**THE OTHER TWO CLASSES — AND THE PATTERN IS THE ONE THIS PROGRAM KEEPS FINDING:**

```text
finite causal updates   NOT covered by the compact-target protection | TYPE-U
record-curvature        *** BRANCH-EXCLUDED ONLY AS AN ADOPTED PRIMITIVE RULE *** | TYPE-C
dissipative mutations   EXPLICITLY OUTSIDE the unitary phase-protection premise unless a unitary
                        dilation / complete carrier is derived | TYPE-U
```

*** RECORD-CURVATURE IS EXCLUDED **BY ADOPTION, NOT DERIVATION** — THE SAME SHAPE AS THE QUARTIC
COMPETITOR IN Q-115/Q-122. THAT IS A SECOND EXCLUSION DOING PHYSICAL WORK ON AN ADOPTED RULE, AND IT
BEARS ON THE Q-123 COUNT. *** And the dissipative case was flagged in advance by the relay as the most
likely to break a protection argument — **non-unitary evolution does not respect the invariances that
protect a phase — and it did.**

**REVIEWER CORRECTION FOLDED (relay 219, sent mid-task).** The 218 framing aimed at a phase-like object.
The sealed characterization is **an on-shell joint eigenvalue/boundary-value residual**, which is not
topologically protected in general. **And `DeltaPhi` occurs at exactly two sites corpus-wide, both calling
it a "sealed display" rather than defining it.** *** THE CORPUS ALREADY POSED THIS BETTER THAN THE
REVIEWER DID: hard failure rule 3 names an action-partition change that moves `K_*` **"without a
theory-derived exclusion"** as a HARD FAILURE of the strict alpha route. The bar is an EXCLUSION, not a
protection theorem — and for a BVP residual that is the more natural route. ***

---

## Q-126. "Does anything close `beta` — the record cell's internal/external conversion?"

*** RULING: NOTHING CLOSES — AND THE SURFACE DESCRIPTION SAYS WHY IN ONE SENTENCE. *** Established
2026-07-31 by Einstein under relay 217
(`STAGE8_RECORD_CELL_SURFACE_AND_BETA_CLOSURE_HUNT_EINSTEIN_V001.md`, `04c10c0d…`, 284 lines, seal
verified, fence-clean). *** ALL FOUR ADVERSARIAL VERIFIERS RETURNED **CONFIRMED** — CITATION-SPAN
CORRECTIONS ONLY. THE FIRST TIME IN THIS PROGRAM'S RECENT HISTORY. ***

> *** OF THE THIRTEEN SEALED INTERFACE QUANTITIES ON THE RECORD CELL, **EVERY JUNCTION THAT IS DERIVED
> IS `beta`-INVARIANT, AND EVERY JUNCTION WHERE `beta` COULD APPEAR IS ADOPTED, GAP, OR UNBUILT. NO
> JUNCTION IS SIMULTANEOUSLY DERIVED AND `beta`-SENSITIVE.** ***

**THE SURFACE, BOTH GEOMETRIES ON ONE OBJECT — THE DIAMOND FINALLY CONSULTED.**

```text
INTERNAL   the projective record degree; Fubini-Study (imported convention, dimensionless only);
           *** THE DERIVED UNIQUE COUNTING METRIC -- SO THE INTERNAL NORMALIZATION IS FULLY PINNED.
           THE WHOLE CONVERSION FREEDOM SITS AT THE JUNCTION. ***
           Phase period 2 pi hbar; marker DeltaS_record = pi hbar = 2 J_FS, an ACTION, with the
           non-identifications sealed.
EXTERNAL   R_R = c T_R / 2; the adopted C_R = 1 selector; sealed diamond volumes; Omega_c with
           uniqueness open; the null edge's sealed failure as a selector.
           *** causal_diamond_shape_derived = true -- THE SHAPE IS DERIVED; THE CONVERSION IS NOT. ***
```

**THE DECISIVE EXECUTED RESULT — RUN INDEPENDENTLY BY ATTACKER AND VERIFIER, IDENTICAL OUTCOME.** The
corpus's **own named locus** is `beta`-**invariant AS-TYPED**: its sealed closure form
`F(T_R/t_P, dimensionless branch data) = 0` **contains no fiber radius**, so under V002's `R -> beta R`
map **every member of the `beta` family passes identically.**

*** SO EVEN COMPLETING THE PROGRAM'S OWN NAMED F-EQUATION WOULD FIX THE DIAMOND AND LEAVE `beta`
FREE. *** Sealed corroboration that this is a **non-implication, not an oversight**: **Q-08 — deriving
`T_R` absolutely does NOT reopen the fiber question.** Two independent routes, same conclusion.

**WHAT WOULD ACTUALLY FIX IT, NOW SPECIFIED:** *** A JOINT SADDLE SYSTEM OVER `(T_R, rho = R_*/ell_P)`
WITH **BREATHING AND SQUASHING MODES** — AND NO SEALED SENTENCE PERFORMS THAT JOIN (proximity sweep:
ZERO HITS). *** Requirements **C1–C8**, including the Q-65/Q-76 require bar with singly-attested
disclosure; `beta`-degeneracy breaking by parameter count; **radion stabilization against
electromagnetic stress**; typed escapes from all four no-gos; mutation-obstruction survival; native
internal/external typing that **closes rather than touches**; target-independent fork-declared
provenance (**a quasilocal-energy-consuming requirement is a silent Misner-Sharp/Brown-York choice and
must be flagged** — the brief seals the sanctioned path: **deciding the `E_ref` fork by derivation is
what Stage 10 is for**); and **C8 JOINTNESS**, sealed at V002: *"the complete parent action class,
radion stabilization, spectrum, and matching rule must be derived together."*

*** `beta` IS A RADION AND THIS IS RADION STABILIZATION — A RECOGNIZABLE KALUZA-KLEIN MODULI PROBLEM
WITH KNOWN MACHINERY, NOT AN EXOTIC ONE-OFF. THE CORPUS NAMED THE FIXER'S SHAPE **TWICE
INDEPENDENTLY** — the coupled gravity-record stationarity equation and the cross-sector metric rule —
**AND BUILT NEITHER.** ***

**Candidates: non-empty, every member adopted or unbuilt.** Twelve-candidate closure sweep executed
with a **withheld-closure hunt run and empty**. Nine typed negatives, two executed TYPE-R. Overlay
audit (the Q-11 hazard): **PASS** — every internal/external typing native to its cited text.

**PATH CORRECTION:** the register's citation of the Stage-10 brief is **stale**; the file resolves at
the archive's `cleanroom_output/` — **outside the workspace subtree the lane's own agents sweep.**
Verified with sidecar. *** A SUBTREE THE SWEEPERS DO NOT ENTER IS THE SAME FAILURE CLASS AS
`reference_search_the_whole_program`. ***

**N8 → PRINCIPAL AMENDMENT 002.** `cross_sector_spec_falsifier_battery_executable = false | TYPE-C`.
The cross-sector spec's live falsifier battery **still embedded the struck overdetermination bar** —
F3 `:265-267` and minimal-pass item 3 `:292`. *** A `beta` CANDIDATE SCORED AGAINST F3 AS WRITTEN
WOULD HAVE BEEN WRONGLY KILLED — BY A SPEC WHOSE OWN DELIVERABLE IS `beta`. *** Amended by
`PRINCIPAL_AMENDMENT_002_OVERDETERMINATION_BAR_STRUCK_EVERYWHERE_2026-07-31_V001.md` (`f1c50042…`).
**Reported, not repaired — correctly.**

---

## Q-127. "What is in `cleanroom_output/` — and is the register wrong about it?"

*** RULING: THE REGISTER IS WRONG ON AT LEAST THREE COUNTS. ALL FOUR GATES WERE **RUN AND PASSED**, AND
ONE DEBT-IN-AXIOM-CLOTHING HAS A **SCOPED DERIVATION**. *** Established 2026-07-31 by the reviewer, after
Einstein's relay 217 tripped over the directory looking for the Stage-10 brief. **Six seals verified
directly; no lane involved in the finding.**

*** `/Users/bgm/MB Work/alpha-program-archive/cleanroom_output/` HOLDS **87 FILES** AND SITS **OUTSIDE THE
`workspace/` SUBTREE THAT EVERY LANE, EVERY SWEEP AND EVERY AUDIT SCRIPT ENTERS.** IT WAS FOUND BY
ACCIDENT. ***

**THE GATES — SPEC + EXECUTABLE + RESULT, ALL SEALS VERIFIED:**

```text
GATE 1  (35)  "The Comparison Group Is U(1), Target-Independently"
GATE 2  (41)  "r = 3 Is a Theorem; the Accounting Is Exact"
GATE 3  (38)  "Hilbert-Functor Uniqueness -- The Forms Are Derived"
GATE 4  (32)  exactly ONE normalized differential equivalence class, P1-P4 all confirmed
GATE 4  (44)  one public-collapse covector ray; "Gate 4 Core Complete"
```

**CORRECTIONS TO TODAY'S OWN ENTRIES, RECORDED AS ERRORS:**

```text
Q-114 N6 / OBS-09   "Gates 2/3/4 executed and passed -- ALL THREE NEVER RUN."   *** WRONG. ***
relay 208           Gate 2 "designated by premise, gate unpassed."              *** WRONG --
                    Gate 2's own result says r = 3 IS A THEOREM. ***
reviewer, in chat   "the program has never closed a clothing item."             *** WRONG, WITH SCOPE. ***
```

**GATE 4 P3, VERBATIM:** *"What the spec had as an axiom ('independent primitive F²… axiomatically
disallowed') is, **at the differential level and within the enumerated family**, now **derived**."*
*** THAT IS CLOTHING ITEM 4 (`K_bare = 0`) WITH A DERIVATION. THE SCOPE QUALIFIER IS LOAD-BEARING AND
MUST TRAVEL WITH IT — DIFFERENTIAL LEVEL, ENUMERATED FAMILY. NOT UNIVERSAL. ***

**Gate 4 also establishes:** interior closure ⟺ `a = b` constant on connected complexes (**which Q-114's
N5 recorded as frozen-not-valued, with `:527` forbidding the assumption — it is derived here, not
assumed**); the `D_x` continuum **dies for every `x ≠ 1`**; normalization forces `|a| = 1`; and the unique
class is **unit-weight covariant incidence modulo gauge — a compact gauge field with holonomy as the sole
physical freedom.** In its own words: *"the gauge-field character of the record surface **emerging** from
closure + normalization rather than being adopted."*

*** OBS-09's CONCLUSION SURVIVES AND IS STRENGTHENED, THOUGH ITS PREMISE WAS WRONG. It argued N6 is not a
`B0` route because no bridge exists from any incidence object to `B0` (Q-114 N3). **The gates having
PASSED makes that empirical rather than hypothetical: BID is determined and `B0` is still exactly where it
was.** ***

**BUT `STATUS.json` READS `final_status: BLOCKED`** — a concluded phase that met a stop rule: *"at least
two load-bearing choices … each admit two or more physically admissible alternatives, and the supplied
principles contain no target-independent selector."*

*** AND ITS `unresolved_load_bearing_items` ALREADY CONTAIN FINDINGS THIS LANE REDISCOVERED INDEPENDENTLY
TODAY: ***

```text
"Family E: connected many-record generator fixed ONLY BY ADOPTED QUASI-FREE COMPLETENESS -- Fork 5"
                                                          <-- Q-115 / Q-119 / Q-122
"Family F: parent zero-form/Pauli competitors excluded ONLY BY ADOPTED SINGLE-OPERATOR COMPLETENESS"
                                                          <-- Q-121
```

*** SO A FULL DAY OF LANE WORK PARTLY REDISCOVERED WHAT A SEALED, CONCLUDED PHASE HAD ALREADY WRITTEN
DOWN. THE FINDINGS ARE CORROBORATED — WHICH IS GENUINE VALUE, TWO INDEPENDENT ROUTES AGREEING — BUT THE
COST WAS A DAY. ***

**THE PROCESS DEFECT, AND IT IS THE THIRD OF THIS CLASS TODAY.** *** A SUBTREE THE SWEEPERS DO NOT ENTER
IS INVISIBLE, AND EVERY "CORPUS-WIDE" NEGATIVE REPORTED BY ANY LANE THIS PROGRAM HAS EVER RUN IS SUSPECT
IN PROPORTION TO WHAT ITS ROOTS EXCLUDED. *** Same class as `reference_search_the_whole_program`, same
class as the stale-criteria sweep, same class as the memory carrying a struck bar. **Three found on one
day, all three by accident while doing something else.**

**Reconciliation of all 87 files issued as relay 222 (Codex 1)**, with the scope-discipline requirement
stated first: **a scoped derivation reported as universal would be worse than not finding it.**

---

## Q-128. "How many live gates embed a struck rule?"

*** RULING: ONE FOUND, AND IT WAS ALREADY AMENDED. THE TWO SURFACES THE PROGRAM ACTUALLY DEPENDS ON ARE
**CURRENT**. THE ROT IS NOT SYSTEMATIC. *** Established 2026-07-31 by Codex lane 2 under relay 220
(`STAGE8_STALE_CRITERIA_SWEEP_LEDGER_V001.md`, `3742b1c8…`, 49 lines, seal verified, fence-clean, no
`= true`).

```text
STAGE8_CROSS_SECTOR_METRIC_RULE_ADMISSIBILITY_SPEC_V001.md:265-267,292   *** STALE-BLOCKING ***
    F3 / minimal-pass item 3 demand a second independent overdetermining requirement, while the
    spec's own success criterion is "determination of beta."
    ALREADY AMENDED -- PRINCIPAL_AMENDMENT_002 (f1c50042).

STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:530-581   §5.3                          *** CURRENT ***
    five-channel mutation audit; no inequivalent admitted root; NO NARROWING AFTER ROOT.
    "Preserves current anti-fitting rule; DOES NOT RELY ON 'only overdetermination.'"

pre-root census requirement                                                      *** CURRENT ***
    "sequencing constraint, not a struck physical premise."

"no chain reaches derived ground" | "two disjoint critical paths" |
generative/formation binary | bare-existence shortcuts                            STALE-INERT
    all sit in records OF their own refutation; NONE operates as a live gate.

stale_blocking_count            = 1          | TYPE-R  (executed)
other_surface_exhaustiveness    = NO_VERDICT | TYPE-C
    deciding evidence: a signed inventory of every live gate.
```

*** §5.3 BEING **CURRENT** IS THE RESULT THAT MATTERS. It is the gate that would certify a computed
alpha as forced rather than fitted. **Had it been stale, everything the program has built toward
certification would have been aimed at a gate scoring on a refuted rule.** It is not. Its anti-fit
clauses stand on current rulings and never depended on overdetermination. ***

**AND THE CAVEAT IS THE LANE'S OWN, CORRECTLY STATED:** keyword search reached **179 files, which is not
179 gates**. *** SO THE FINDING IS "ONE FOUND," NOT "ONE EXISTS." Exhaustiveness is NO_VERDICT and must
not be reported as a clean bill. *** **Not funded:** converting one to the other needs a signed inventory
of every live gate — a materially larger task than a keyword sweep, and nothing currently points at a
second offender.

**What this settles about the scare:** the cross-sector spec was **an isolated lapse, not systematic
rot.** The alarming shape of the discovery — a falsifier rejecting the program's own deliverable — was
real, and it was one instance.

---

## HOW TO USE THIS REGISTER

1. **Before starting any line of work, grep this file for the question**, in the words you would
   naturally use. The rows are phrased as questions for exactly that reason.
2. If your question matches a row, READ THE REOPEN CONDITION before proceeding. Most rows here are
   closed by proof, not by exhaustion.
3. If you settle a new question, ADD A ROW. Phrase the heading as the question, not the answer.
4. Never edit a row. Supersede it with a later row that cites it.

alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
