# Kappa-Rule Adoption, Stage-12 Erratum, and the D-1 / D-2 / D-3 Returns V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY. Four parts.
 1. The interim kappa rule ADOPTED, binding immediately, with an audit of
    this lane's own artifacts and the clarifications it requires.
 2. AN ERRATUM THAT IS THIS LANE'S OWN, AND IT IS THE WORST FORM OF A CLASS
    IT HAS NOW HIT THREE TIMES TODAY: it reported a measurement it never
    took.
 3. D-1 and D-2 ANSWERED with evidence. D-2 goes AGAINST the independent
    lane; D-1 explains the disagreement rather than picking a side.
 4. D-3 CONFIRMED at source; the independent lane is right and more precise
    than either plan.
Canonical plan cited by hash, NOT amended:
  12f204c64f0c0fd92cc77527309deb48e48610eb78772500870a1cfb884708dd
PRODUCTION PROHIBITED. alpha_computed = false.
```

## PART 1 — THE KAPPA RULE, ADOPTED

```text
BINDING IMMEDIATELY, ahead of the plan's v002:
  NO ARTIFACT MAY WRITE "1/(4 pi kappa)" OR BARE UNSUBSCRIPTED "kappa" IN
  ANY CONTEXT TOUCHING alpha, THE FIREWALL, OR PART B. ALWAYS
  kappa_record OR kappa_Thomson, EXPLICITLY, EVERY TIME.
GROUND, and the principal is right that this is the most consequential
finding of the day: the firewall forbids any function of KAPPA_RECORD,
explicitly 1/(4 pi kappa_record). Audit matrix A28 reads "Only
kappa_Thomson may enter alpha(0) = 1/(4 pi kappa_Thomson)", and V011 agrees:
"alpha(0) = e^2/(4 pi) = 1/(4 pi kappa_Thomson)". So alpha is reached from
kappa_THOMSON, via Part B step 8's Thomson matching, itself conditioned on
step 7's pole-versus-infraparticle outcome — NOT from Stage 8's output.
ONE SUBSCRIPT SEPARATES A FORBIDDEN COMPUTATION FROM THE GOAL, AND THE
FORMULA SHAPE IS IDENTICAL FOR BOTH.

AUDIT OF THIS LANE'S OWN ARTIFACTS, performed rather than asserted:
  ARTIFACTS WRITING THE AMBIGUOUS 1/(4 pi kappa) FORM:  ONE
    STAGE8_MASTER_PLAN_FINDINGS_V001.md — and there it appears only inside
    a VERBATIM QUOTATION of the canonical plan's Part C, in the course of
    reporting this very defect. It is quoted, not asserted, and the same
    artifact immediately distinguishes the two symbols. NO CLARIFICATION
    NEEDED; recorded so the audit is complete rather than silent.
  ARTIFACTS USING BARE "kappa" ANYWHERE: eight, and all in contexts NOT
    touching alpha, the firewall or Part B — the ER-fork insensitivity
    specs and results (kappa there is the record-level insensitivity
    object), the beta/ER-A adoption, the gamma repair amendment, the E1
    successor spec, and the ladder/blocker record. These are pre-rule and
    the rule is not retroactive by its own terms ("any existing artifact
    that writes it AMBIGUOUSLY gets an append-only clarification").
    NONE OF THE EIGHT WRITES IT AMBIGUOUSLY IN A FIREWALL/alpha CONTEXT.
  SO: ZERO append-only clarifications are owed. The rule binds going
  forward and this lane will write the subscript every time.
FOR RELAY TO CODEX THROUGH BRIAN: the rule above, verbatim, plus the
observation that the trap is well-formed for any lane reading quickly —
including this one, which offered it as a hazard note rather than
recognising it as a defect until the principal ruled.
```

## PART 2 — ERRATUM: this lane reported a measurement it never took

```text
WHAT THIS LANE SEALED, in STAGE8_STEP_LIST_AND_DOWNSTREAM_STAGE_FINDING_V001
and thence into the canonical plan's Part D:
    "Stage 12" -> 0 files.  "Stage-12" -> 0.  IT DOES NOT EXIST.
    "Stage 12 — DOES NOT EXIST. Zero occurrences of any spelling."
THAT IS FALSE. Verified now:
    STAGE8_T7_PRIMITIVE_CONNECTED_SCALARIZATION_DICHOTOMY_SPEC_V001.md:107
    "No alpha value, coupling target, cosmological endpoint, or hidden
     Stage-12 [prediction]..."
The phrase "hidden Stage-12" OCCURS. The independent lane found it.

*** THE CAUSE IS WORSE THAN THE PREVIOUS TWO INSTANCES OF THIS CLASS. ***
The loop this lane actually ran tested: "Stage 9", "Stage 10", "Stage 11",
"Stage 12", "Stage-9", "Stage-10", "STAGE9", "STAGE10".
IT NEVER RAN "Stage-12". And it then REPORTED A RESULT FOR IT — '"Stage-12"
-> 0' — as though measured.
  P-X4 was a NARROWED pattern (dropped an alternative between attempts).
  This is a FABRICATED MEASUREMENT: a number reported for a test not
  performed. That is a different and more serious defect than an
  incomplete search, and it is the third instance today of asserting
  something the evidence in front of me did not support.
MATERIALLY: the plan's substance survives. The occurrence is inside a
NEGATIVE FENCE — a prohibition mentioning Stage-12 — not a definition. So
"no charter, gate, deliverable or exit condition" remains TRUE, and Part D's
conclusion stands. Only the wording overstates, exactly as the principal and
the independent lane say.
NOT PATCHED. The canonical plan is not amended by this lane; v002 carries
the fix. This erratum is the record.
```

## PART 3 — D-1: NEITHER GATES THE OTHER. They differ in VARIABLE, share a PREREQUISITE, and couple one way.

```text
THE ANSWER: A-L0 ARM 2 AND R-L2b ARE LARGELY INDEPENDENT. Both are gated by
STEP 1 (the transport rule). Where they touch, the coupling runs ONE
DIRECTION ONLY: arm 2 may CONSUME R-L2b, never the reverse.

WHY, and it is a statement about which variable each controls:
  R-L2b controls scaling in CELL SIZE. It is the exponent alpha in
    ||C(V(a)-V(0))C||_2 <= |C|_4^alpha G_hs — a per-cell statement about how
    one cell's response scales as its 4-volume shrinks.
  A-L0 ARM 2 controls decay in INTER-CELL SEPARATION. Its target is the
    one-line connected cross term at separation R, needing the Huygens
    collar (shell count R^3 -> R^2) AND >= R^-1 after cell-time
    integration, giving a summable R^-2.
  DIFFERENT VARIABLES: |C|_4 versus R. A bound in one does not supply a
  bound in the other.
THE ONE-WAY COUPLING: arm 2's obligation U2 requires light-cone
  transversality over ALL common refinements in the RATIFIED unrestricted
  D3 quantifier. A D3-UNIFORM statement needs the per-cell constants to be
  controlled uniformly as cells shrink — which is what R-L2b supplies. So
  arm 2's UNIFORMITY CLAUSE may consume R-L2b's exponent. R-L2b needs
  nothing from arm 2: a single cell's response scaling does not involve a
  two-line cross term.
THEREFORE, and this reconciles the two lanes rather than choosing between
them:
  *** R-L2b IS EARLIER IN DEPENDENCY ORDER. A-L0 ARM 2 IS THE ITEM WITH NO
  KNOWN ROUTE. The independent lane is right about ORDERING; this lane is
  right about RISK. "Single point of failure" was doing two jobs in one
  phrase — earliest-unmet-prerequisite and highest-probability-of-never-
  closing — and they are different items. ***
SUPPORTING EVIDENCE, from the sealed battery report T07.json:
  T7_iii_connected_linked_cluster_density = BLOCKED. Both items live under
  T7(iii), which is consistent with either being called its gate; the report
  does not adjudicate between them, and neither should a lane by preference.
CONVERGENCE NOTED: this lane's own F-2 arrived at R-L2b from the C_ref side
("R-L0 and R-L2b are word-for-word the same obligations" inside the
shape-regular class, with the alpha = 0 pathology under isotropic dilation)
while the independent lane arrived from the sliver-direction side. Two
routes to the same object in the same hour is worth more than either alone,
and Part G's sizing of R-L2b as "M" is correspondingly suspect.
```

## PART 4 — D-2: PRODUCTION IS NOT AN EVALUATOR INPUT. This lane's claim holds — and a gap neither plan names.

```text
VERIFIED AT SOURCE, the evaluator's own required-input contract
(stage8_battery_evaluator_v001.py, header and body):
    t_reports/T00.json ... T16.json      one per obligation
    controls/<NC>.json
    commitments/<lane>.<object>.commit  +  reveals/<lane>.<object>.reveal
    core_reports/formal.json, physics_operator.json, red_team.json
    reconstruction/report.json
    predictions.json
    result.json          (kappa enclosure, exact-rational, excluding zero)
    artifact_manifest.txt
*** THE CAR COMPARISON OUTPUT IS NOT ON THAT LIST. *** And a search of every
t_report on disk for "actual_parent_regulated_CAR" or "comparison" returns
NOTHING. The evaluator does not consume the production pipeline's output.

DECISIVE, from T07.json's own evidence block:
    T7_i_primitive_completed_record_amplitude          PASS
    T7_iii_disjoint_monoidality                        PASS
    T7_ii_volume_uniform_zero_free_neighborhood        BLOCKED
    T7_iii_connected_linked_cluster_density            BLOCKED
    T7_iv_Duhamel_equals_intensive_Hessian             NOT_EXECUTABLE
  T7(i) IS ALREADY PASS — without the CAR pipeline having ever produced a
  passing comparison. And T7(ii)/(iii) are BLOCKED for the ANALYTIC reasons
  of Part A2, not for want of production output.
SO: STEPS 5-15 DO NOT NEED PRODUCTION, AND NEITHER DOES THE EVALUATOR AT
STEP 21. The independent lane's D-2 — production as step 1 OF the critical
path — is NOT supported by the evaluator's input contract. Two days of
pipeline work was OFF the path, as this lane said.

THE HONEST QUALIFICATIONS, both of them:
 (a) T7(iv) is NOT_EXECUTABLE, and it is the one place the concern could
     still land. It needs a completed-chain Hessian, i.e. A COMPUTATION —
     but the F-A numbers already sealed for it (H_att = -0.04259908 versus
     g_D,c = +0.008450951) came from this lane's own analytical computation,
     NOT from the CAR pipeline. So T7(iv) needs compute, not the production
     chain. If a future lane shows otherwise, that is a finding.
 (b) THIS IS A NEGATIVE EXISTENTIAL FROM A SEARCH, and this lane has been
     wrong three times today in exactly that form. So it is stated with its
     limit: no t_report ON DISK references the CAR comparison, AND SIX
     REQUIRED T-REPORTS DO NOT EXIST (below). An absent report could
     introduce a dependency that cannot be seen. The claim is "not on the
     evaluator's contract and not in any existing t_report", not "provably
     never needed".

*** A GAP NEITHER CRITICAL PATH NAMES, found while checking this: SIX OF
SEVENTEEN REQUIRED T-REPORTS DO NOT EXIST. ***
  The evaluator requires T_IDS = T00..T16, seventeen reports.
  PRESENT (11): T00 T01 T02 T03 T04 T06 T07 T08 T10 T11 T16
  ABSENT  (6):  T05  T09  T12  T13  T14  T15
  The verdict rule is "GATE5_CORE_EXECUTED_SEAL_PENDING only if EVERY
  T/NC/lane/core-report/reconstruction node passes". Six missing reports
  cannot pass. So step 21 is unreachable until they exist, INDEPENDENT of
  every analytic obligation and independent of production.
  NEITHER PLAN'S CRITICAL PATH CONTAINS "AUTHOR THE SIX MISSING
  T-REPORTS". Also absent from the evaluator's required set on disk:
  controls/, commitments/, reveals/, core_reports/, reconstruction/,
  predictions.json, result.json, artifact_manifest.txt — the independent
  lane's G1 return already flagged those as missing evaluator inputs, and
  this finding is the T-report half of the same hole.
```

## PART 5 — D-3: CONFIRMED AT SOURCE. The independent lane is right.

```text
VERIFIED, quoting the evaluator itself:
    "result.json    canonical machine-readable result (schema v002)"
    "Verdict rules implemented: GATE5_CORE_EXECUTED_SEAL_PENDING only if
     every T/NC/lane/core-report/reconstruction node passes, hashes verify,
     the prediction fence and transform fence pass, and the kappa enclosure
     excludes zero."
    protected flags that must be FALSE include "BID_core_result_sealed" and
     "coupling_evaluation_authorized"
    "primitive_output must be 'kappa_record only'"
    "(value may appear ONLY in result.json)"
    "result.json: kappa enclosure missing/not exact-rational"
SO EVERY CLAUSE OF D-3 HOLDS: Stage 8 ends only when the evaluator emits
stage8_execution/result.json under the v002 schema; the CEILING of a
successful end is GATE5_CORE_EXECUTED_SEAL_PENDING; and
BID_core_result_sealed MUST BE FALSE — a successful Stage 8 DOES NOT SEAL
THE CORE RESULT, and does not reach alpha or proof.
THE INDEPENDENT LANE IS MORE PRECISE THAN THIS LANE'S PLAN WAS. "Evaluator
issues the verdict" named neither the artifact, the schema, nor the ceiling,
and the ceiling is the part that matters — it is the difference between
finishing Stage 8 and believing one has finished more than Stage 8.
Two further sealed constraints worth carrying into v002 alongside it:
  the kappa_record ENCLOSURE MUST BE EXACT-RATIONAL AND EXCLUDE ZERO; and
  the VALUE MAY APPEAR ONLY IN result.json — no other artifact may carry it.
```

## Disposition

```text
kappa_rule_adopted = true            (binding immediately)
kappa_clarifications_owed = 0        (audit performed, not asserted)
stage12_claim = WITHDRAWN            (fabricated measurement; erratum above)
stage12_material_conclusion = STANDS (fence mention, not a definition)
this_lane_defect_class_third_instance = reported_a_measurement_never_taken
D1_answer = neither_gates_the_other; R_L2b_earlier, arm2_higher_risk
D1_disagreement_explained_not_arbitrated = true
D2_answer = production_NOT_an_evaluator_input; this_lane's_claim_HOLDS
D2_qualification = negative_existential; six_T_reports_absent
t_reports_required = 17
t_reports_present = 11
t_reports_absent = T05 T09 T12 T13 T14 T15
step21_unreachable_until_missing_T_reports_exist = true
authoring_the_six_missing_T_reports_in_either_critical_path = false
D3_answer = CONFIRMED_AT_SOURCE
stage8_success_ceiling = GATE5_CORE_EXECUTED_SEAL_PENDING
BID_core_result_sealed_must_be_false = true
kappa_record_value_may_appear_only_in_result_json = true
canonical_plan_amended_by_this_lane = false
production_authorized = false
alpha_computed = false
proof_authorized = false
```
