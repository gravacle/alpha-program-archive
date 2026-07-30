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

## HOW TO USE THIS REGISTER

1. **Before starting any line of work, grep this file for the question**, in the words you would
   naturally use. The rows are phrased as questions for exactly that reason.
2. If your question matches a row, READ THE REOPEN CONDITION before proceeding. Most rows here are
   closed by proof, not by exhaustion.
3. If you settle a new question, ADD A ROW. Phrase the heading as the question, not the answer.
4. Never edit a row. Supersede it with a later row that cites it.

alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
