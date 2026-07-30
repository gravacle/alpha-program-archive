# Stage 8 Gamma_K Construction Spec Amendment 001

Status: APPEND-ONLY AMENDMENT / NO EXECUTION.

Subject: `STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md`

Subject SHA-256:
`2d63dfadbb741c467b812f21e14f9e0e66015f1d86e2aa8307d8ae77acfe3d69`

This amendment discharges the two hostile-review conditions on V001 by
recording their bounded determinations. It does not rewrite V001, construct
`Gamma_K`, run a mutation audit, solve a root, evaluate a response, choose
Misner-Sharp energy, choose Brown-York energy, or compute any physical
constant.

## Condition 2 First: Live Equivalence Is Weaker Than V001's Teeth Clause

Scope for this version-lineage statement: searched
`primitive_record_cell_selection_principle_v001.md` through
`primitive_record_cell_selection_principle_v004.md` for the literal phrases
`physically null` and `null transformation`.

The continuous-modulus exclusion in
`primitive_record_cell_selection_principle_v001.md:38-42` is not carried
verbatim into live v002. V001 states:

```text
Selection is unique only up to transformations already proved physically
null: gauge, public isometry, orientation paired with charge conjugation, and
Boundary-Resolved equivalence. A continuous modulus that changes any action
integral or response coefficient is not a null transformation and fails the
principle.
```

The live equivalence relation available in
`primitive_record_cell_selection_principle_v002.md:48-57` is:

```text
For each `K`, the complete BR boundary conditions and stationarity equations
select, when it exists,

X_K = [Omega_K, g_K, Delta tau_K, A_K, Psi_K]

modulo gauge, public isometry, charge-conjugate orientation, and
Boundary-Resolved equivalence. `Delta tau_K` is varied in the stationary
problem; it is not fixed by units.
```

This amendment therefore uses the live v002 relation as the only equivalence
relation for V001 Section 5.2. It does not silently reimport the v001 sentence
"A continuous modulus that changes any action integral or response coefficient
is not a null transformation and fails the principle" as part of the live
equivalence arm.

The live continuous-modulus catch is instead the uniqueness gate at
`primitive_record_cell_selection_principle_v002.md:73-83`, whose required
conditions include:

```text
no second inequivalent positive root or continuous modulus.
```

Determination: the equivalence arm may identify only gauge, public isometry,
charge-conjugate orientation, and Boundary-Resolved equivalence, as derived or
otherwise supplied by the completed problem. It may not by itself exclude an
action-changing or response-changing continuous modulus. Such a modulus is
caught, if at all, by the uniqueness gate. Therefore a later audit pass must
state whether any continuous modulus survives under the uniqueness gate; it may
not pass by calling that modulus "null" unless the completed derivation supplies
that null transformation in the live chain.

## Condition 1: Five Mutation Channels Are Named, Not Enumerated

### Bounded Search Scope

Roots searched for this condition:

- `/Users/bgm/Documents/New project/gravity_emergence_evidence_program`
- `/Users/bgm/MB Work/alpha_supervision`

Excluded paths:

- `third_party/**`
- `external/**`
- `**/venv/**`
- `**/a32_holdout/custodian_private/**`

Search terms:

- `mutation audit`
- `admitted.*mutation`
- `admitted.*geometry`
- `admitted.*clock`
- `admitted.*measure`
- `admitted.*regulator`
- `action[- ]partition`
- `boundary condition, measure, regulator, or action partition`
- `geometry, clock, measure, regulator`
- `physically null`
- `null transformation`
- `continuous modulus`
- `Boundary-Resolved equivalence`

Hit-file list:

```text
/Users/bgm/MB Work/alpha_supervision/EXECUTION_TRACKER.md
/Users/bgm/MB Work/alpha_supervision/BOHM_ROUTE_RUNNABILITY_WORKFLOW_RECOVERED_2026-07-28.md
/Users/bgm/MB Work/alpha_supervision/F8_SECOND_HALF_REVIEW_SEALED_TRANSCRIPT_V001.md
/Users/bgm/MB Work/alpha_supervision/REVIEW_2026-07-30_gamma_k_construction_spec_hostile.md
/Users/bgm/MB Work/alpha_supervision/CONTINUATION_STATE.md
/Users/bgm/MB Work/alpha_supervision/BOHM_LAMBDA_FILTER_AND_EXTERNAL_CHAIN_2026-07-29.md
/Users/bgm/MB Work/alpha_supervision/RELAY_PASTE_135_SPEC_CONDITIONS_2026-07-30.md
/Users/bgm/MB Work/alpha_supervision/RELAY_PASTE_130_TWO_RULINGS_AND_OSC1_2026-07-30.md
/Users/bgm/MB Work/alpha_supervision/RELAY_PASTE_131_GAMMA_K_CHARTER_AND_ERRATUM_2026-07-30.md
/Users/bgm/MB Work/alpha_supervision/GAMMA_K_SOLE_CONSTRUCTION_TARGET_CHARTER_2026-07-30.md
/Users/bgm/MB Work/alpha_supervision/DEPARTURE_2_RESCALING_EXCLUSION_FOUR_CHANNEL_AUDIT_V002.md
/Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md
/Users/bgm/MB Work/alpha_supervision/RECOVERY_STIFFNESS_AND_ALLOW_REQUIRE_2026-07-29.md
/Users/bgm/MB Work/alpha_supervision/TEST_RESULT_SURFACE_PREIMAGE_2026-07-29.md
/Users/bgm/MB Work/alpha_supervision/RELAY_PASTE_133_GAMMA_K_SPEC_2026-07-30.md
/Users/bgm/MB Work/alpha_supervision/BOHM_RESCOPE_REGISTER_2026-07-29.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/primitive_record_cell_selection_principle_v002.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_cleanroom_f_charged_operator_plan_v001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/reports/alpha_br_induced_only_boundary_provenance_mutations_v001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/gravacle_alpha_cleanroom_review_packet_v003_2026-07-14/alpha_cleanroom_f_charged_operator_plan_v001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/R3_4_OUTGOING_TAIL_GENERATOR_EXHAUSTION_SPEC_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/BID_CONSOLIDATED_HOSTILE_AUDIT_MATRIX_V005.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/STAGE8_LANE_STATUS.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/STAGE8_GAMMA_K_SCOPE_INVENTORY_AND_Q21_REGISTRATION_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/BID_AXIAL_PHASE_CP_REDUCTION_DERIVATION_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/STAGE8_RESCALING_EXCLUSION_RECOVERY_ERRATUM_V002.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/STAGE8_Q13_Q19_GOVERNING_REGISTRATION_RECORD_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/STAGE8_RESCALING_EXCLUSION_RECOVERY_ERRATUM_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_strict_route_decision_ledger_v001.csv
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/stage8_execution/work/MAJORANT_LEMMA0_PROOF_DRAFT_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/gravacle_alpha_cleanroom_review_packet_v004_2026-07-14/alpha_cleanroom_f_charged_operator_plan_v001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v002/PREREGISTRATION_V002.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/reports/alpha_br_exact_public_source_traceclass_v001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/reports/alpha_strict_route_ledger_audit_v001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/primitive_record_cell_selection_principle_v001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/gravacle_alpha_cleanroom_review_packet_v005_2026-07-14/alpha_cleanroom_f_charged_operator_plan_v001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/primitive_same_cell_opening_normalization_principle_v001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/gravacle_alpha_cleanroom_review_packet_v002_2026-07-13/alpha_cleanroom_f_charged_operator_plan_v001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/gravacle_alpha_cleanroom_review_packet_v002_2026-07-13/rules/alpha_cleanroom_f_charged_operator_plan_v001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/alpha_strict_route_decision_ledger_step6_carrier_v002_snapshot.csv
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/alpha_strict_route_decision_ledger_cartesian_authorization_v001_snapshot.csv
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/alpha_strict_route_decision_ledger_step7_cartesian_v001_snapshot.csv
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/alpha_strict_route_decision_ledger_step6_carrier_crossgrid_v001_snapshot.csv
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/alpha_strict_route_decision_ledger_step4_authorization_v005_snapshot.csv
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/primitive_record_cell_selection_preregistration_v001.json
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/alpha_strict_route_decision_ledger_two_endpoint_carrier_v003_snapshot.csv
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/alpha_strict_route_decision_ledger_step4_authorization_v002_snapshot.csv
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/alpha_strict_route_decision_ledger_step4_authorization_v003_snapshot.csv
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/alpha_strict_route_decision_ledger_step4_authorization_v004_snapshot.csv
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/alpha_strict_route_decision_ledger_v008_prerun.csv
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/primitive_unitary_prerecord_transfer_preregistration_v001.json
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/alpha_strict_route_decision_ledger_v007_prerun.csv
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/alpha_strict_route_decision_ledger_step6_carrier_v001_snapshot.csv
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/primitive_complete_boundary_transition_functional_preregistration_v001.json
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/alpha_strict_route_decision_ledger_symplectic_pullback_v006_snapshot.csv
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/primitive_record_cell_selection_preregistration_v002.json
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/alpha_strict_route_decision_ledger_step7_cartesian_v002_snapshot.csv
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/alpha_strict_route_decision_ledger_step4_authorization_v001_snapshot.csv
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/provenance/alpha_strict_route_decision_ledger_step6_carrier_v003_snapshot.csv
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/results/primitive_boundary_ctp_record_map_v001.json
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/results/alpha_strict_route_effective_state_v002.json
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/gravacle_alpha_cleanroom_review_packet_v001_2026-07-12_current/alpha_cleanroom_f_charged_operator_plan_v001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/primitive_generated_sector_step9_admission_gate_v001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v001/PREREGISTRATION.md
```

Bounded-search finding: the corpus names the five live mutation channels but
does not supply an enumerated member set for any of them in a form an audit can
execute. The deepest existing channel ledger is
`DEPARTURE_2_RESCALING_EXCLUSION_FOUR_CHANNEL_AUDIT_V002.md:241-250`, and it
records every live channel as gated rather than enumerated.

### Governing Anchors

`primitive_record_cell_selection_preregistration_v002.json:15-23` requires:

```text
"a mutation audit over admitted geometry, clock, measure, regulator, and
action-partition alternatives"
```

`primitive_record_cell_selection_principle_v002.md:126-133` blocks the
construction if:

```text
1. the cell interval, geometry, field norm, or source depth is inserted rather
   than obtained from the joint stationarity problem;
...
3. changing an admitted boundary condition, measure, regulator, or action
   partition changes `K_*` without a theory-derived exclusion;
```

`DEPARTURE_2_RESCALING_EXCLUSION_FOUR_CHANNEL_AUDIT_V002.md:125-144`
identifies the live channel set as five:

```text
geometry, clock, measure, regulator, and action-partition alternatives
```

and explains that the older four-channel framing missed regulator and folded
measure into another channel.

### Per-Channel Determination

| Channel | Corpus status | Reason enumeration cannot be supplied in this amendment |
|---|---|---|
| geometry | NAMED / NOT ENUMERATED | The live gate says geometry must come from the joint stationarity problem, not insertion (`primitive_record_cell_selection_principle_v002.md:126-129`). The channel ledger says geometry is gated behind the joint operator because no `C_record(K)` exists to mutate (`DEPARTURE_2_RESCALING_EXCLUSION_FOUR_CHANNEL_AUDIT_V002.md:243-246`). |
| clock | NAMED / NOT ENUMERATED | The preregistration names clock alternatives, and v002 says `Delta tau_K` is varied in the stationary problem and fixed by neither units nor insertion (`primitive_record_cell_selection_principle_v002.md:48-57`). The channel ledger says clock is gated behind the same joint operator and the `sqrt(2)` energy convention is also open (`DEPARTURE_2_RESCALING_EXCLUSION_FOUR_CHANNEL_AUDIT_V002.md:245-247`). |
| measure | NAMED / NOT ENUMERATED | V001's still-relevant selector content says the microscopic measure, gauge quotient, zero-mode prescription, and field domains are part of the selector (`primitive_record_cell_selection_principle_v001.md:56-60`). The live channel ledger says measure is gated and has never been separately examined (`DEPARTURE_2_RESCALING_EXCLUSION_FOUR_CHANNEL_AUDIT_V002.md:247-248`). |
| regulator | NAMED / NOT ENUMERATED | Regulator appears in the live v002/preregistration channel list but was absent from the old four-channel tracker. The channel ledger says regulator is gated and identifies it with slot 6 (`DEPARTURE_2_RESCALING_EXCLUSION_FOUR_CHANNEL_AUDIT_V002.md:248-249`). |
| action-partition | NAMED / NOT ENUMERATED | V002 blocks if changing an admitted action partition changes `K_*` without a theory-derived exclusion (`primitive_record_cell_selection_principle_v002.md:131-132`). The channel ledger says action-partition is gated because `Gamma_rest,*` has never been constructed (`DEPARTURE_2_RESCALING_EXCLUSION_FOUR_CHANNEL_AUDIT_V002.md:249-250`). |

Determination: V001 Section 5.2 is not executable yet. A later executable
mutation-audit spec must enumerate these five channel families, or expressly
carry the same per-channel non-enumerability finding as a BLOCK, before any
root value exists.

## Preservation Of V001 Conditions

This amendment preserves the following V001 requirements without weakening or
replacing them:

1. Complementary residual: V001 Section 4 requires that the implementation
   derive `C_record(K)` from the full on-shell problem and demonstrate that
   every complementary residual required by the same operator vanishes before a
   scalar root is used (`STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:497-504`).
2. Energy refusal: V001 Section 2.2 refuses to choose Misner-Sharp or
   Brown-York energy and states that the Hamilton-Jacobi conjugate energy must
   be derived as part of the stationary cell target
   (`STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:314-380`).
3. Added falsifiers: F-GK6, F-GK7, and F-GK8 remain frozen in V001 Section 6
   (`STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:640-663`).

## Section 5 Gate Status

V001 Section 5 remains acceptance criteria, not a complete executable gate.
V001 already states that no numerical tolerance is set because no numerical
representation has been constructed, and that any later executable spec must
freeze exact arithmetic, certified enclosure, or reproducibility tolerances
before execution and before any root value exists
(`STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:592-595`).

This amendment restates that requirement as binding on successor executable
work: tolerances are not frozen by V001 or by this amendment. They must be
frozen in a later executable spec before the root value exists, not merely
before the root-solver text is written.

## Gate Verdict

Verdict: READY_WITH_CONDITIONS_DISCHARGED_AS_SPECIFICATION.

Meaning: V001 plus this amendment is a specification target with the two review
conditions discharged by bounded determinations. It remains non-executable until
the completed `Gamma_K` object, stationary problem, residual, channel
enumeration or explicit BLOCK, uniqueness gate, and pre-value tolerance scheme
exist in a successor executable spec.

## Protected Status

```text
artifact_type = APPEND_ONLY_SPECIFICATION_AMENDMENT
subject_artifact = STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md
subject_sha256 = 2d63dfadbb741c467b812f21e14f9e0e66015f1d86e2aa8307d8ae77acfe3d69
construction_executed = false
mutation_audit_executed = false
root_solved = false
response_evaluated = false
Misner_Sharp_selected = false
Brown_York_selected = false
equivalence_relation_source = primitive_record_cell_selection_principle_v002.md:48-57
v001_null_transformation_teeth_imported = false
continuous_modulus_caught_by_uniqueness_gate = true
five_mutation_channels_named = true
five_mutation_channels_enumerated = false
Section_5_executable_gate_complete = false
tolerances_frozen = false
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
