# Corpus Check Report

Overall gate verdict: `RED`
Baseline loaded: `True`

This checker reports and blocks process defects only. It never rules, adopts, retires, repairs, seals, or computes physical values.

## Gate Failures

- RED seal_integrity: 20 issue(s)
- RED deploy_state: 1 issue(s)
- RED authority_currency: 2 issue(s)

## Checks

### seal_integrity

- severity: `RED`
- status: `RED`
- issue_count: `20`
- metric: `20`
- summary: 588 sidecars checked; 2676 unsealed artifacts listed by class
- details: `{"unsealed_by_class": {"json": 214, "jsonl": 5, "md": 410, "py": 2040, "txt": 7}, "unsealed_samples": {"json": ["workspace/R3_4_REGULATOR_SCHEME_AND_RAY_SUFFICIENCY_PROVENANCE_V001.json", "workspace/CURRENT_AUTHORITY_LEDGER_V006.json", "workspace/CURRENT_AUTHORITY_LEDGER_V010.json", "workspace/LEVEL1_MICROSCOPIC_ACTION_PREMISE_LEDGER_V001.json", "workspace/CURRENT_AUTHORITY_LEDGER_V011.json", "workspace/R3_4_INCIDENCE_CONTINUUM_SCALING_PROVENANCE_V001.json", "workspace/R3_4_CAUSAL_DIAMOND_SPECTRAL_PULLBACK_PROVENANCE_V002.json", "workspace/CURRENT_AUTHORITY_LEDGER_V007.json", "workspace/R3_4_PARENT_TO_OUTGOING_GNS_COMPATIBILITY_PROVENANCE_V001.json", "workspace/provenance_inputs_v003.json", "workspace/CURRENT_AUTHORITY_LEDGER_V001.json", "workspace/BID_SOURCE_PARENT_SUBORDINATE_OUTPUT_CONTRACT_V001.json", "workspace/STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V001.json", "workspace/STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.json", "workspace/contract_v003.json", "workspace/CURRENT_AUTHORITY_`

Sample findings:
- `workspace/STAGE8_LANE_STATUS.md.seal.sha256` — seal mismatch expected=9b1133f5067dd71bb4f931548705788b06e35e0fe8fda62aed2c0bf7403ef4a4 actual=a5f1823e2496c86182beb4e3fb4f011f426cfb0bf5ef7925f8b3b1000dc90a49
- `workspace/stage8_execution/execution_authority.seal.sha256` — target missing: execution_authority
- `workspace/stage8_execution/t7_relayed_connected_preparation_retest/T07_RELAYED_CONNECTED_PREPARATION_RETEST_V001.seal.sha256` — target missing: T07_RELAYED_CONNECTED_PREPARATION_RETEST_V001
- `workspace/stage8_execution/t7_connected_analytic_closure/T07_CONNECTED_ANALYTIC_CLOSURE_V001.seal.sha256` — target missing: T07_CONNECTED_ANALYTIC_CLOSURE_V001
- `workspace/stage8_execution/t7_response_closure_selection/T07_RESPONSE_CLOSURE_SELECTION_V001.seal.sha256` — target missing: T07_RESPONSE_CLOSURE_SELECTION_V001
- `workspace/stage8_execution/t7_response_lift/T07_RESPONSE_LIFT_AUDIT_V001.seal.sha256` — target missing: T07_RESPONSE_LIFT_AUDIT_V001
- `workspace/stage8_execution/t7_primitive_connected_scalarization_dichotomy/T07_PRIMITIVE_CONNECTED_SCALARIZATION_DICHOTOMY_V001.seal.sha256` — target missing: T07_PRIMITIVE_CONNECTED_SCALARIZATION_DICHOTOMY_V001
- `workspace/stage8_execution/t0_lineage/T00_LINEAGE_REEXECUTION_V001.seal.sha256` — target missing: T00_LINEAGE_REEXECUTION_V001
- `workspace/stage8_execution/t7_parent_state_regulator_restriction/T07_PARENT_STATE_REGULATOR_RESTRICTION_V001.seal.sha256` — target missing: T07_PARENT_STATE_REGULATOR_RESTRICTION_V001
- `workspace/stage8_execution/t7_finite_fock_completed_record_amplitude/T07_FINITE_FOCK_COMPLETED_RECORD_AMPLITUDE_V001.seal.sha256` — target missing: T07_FINITE_FOCK_COMPLETED_RECORD_AMPLITUDE_V001
- `workspace/stage8_execution/t7_primitive_connected_lift/T07_COMPLETED_EFFECT_ZERO_BASELINE_V001.seal.sha256` — target missing: T07_COMPLETED_EFFECT_ZERO_BASELINE_V001
- `workspace/stage8_execution/t7_primitive_connected_lift/T07_PRIMITIVE_CONNECTED_LIFT_VERIFIER_V002.seal.sha256` — target missing: T07_PRIMITIVE_CONNECTED_LIFT_VERIFIER_V002
- `workspace/stage8_execution/t7_primitive_connected_lift/T07_PRIMITIVE_CONNECTED_LIFT_V001.seal.sha256` — target missing: T07_PRIMITIVE_CONNECTED_LIFT_V001
- `workspace/stage8_execution/t7_gaussian_path_sum_reduction/T07_GAUSSIAN_PATH_SUM_REDUCTION_V001.seal.sha256` — target missing: T07_GAUSSIAN_PATH_SUM_REDUCTION_V001
- `workspace/stage8_execution/t7_connected_response/T07_CONNECTED_RESPONSE_GATE_V001.seal.sha256` — target missing: T07_CONNECTED_RESPONSE_GATE_V001
- `workspace/stage8_execution/t7_actual_parent_record_amplitude/T07_ACTUAL_PARENT_RECORD_AMPLITUDE_V001.seal.sha256` — target missing: T07_ACTUAL_PARENT_RECORD_AMPLITUDE_V001
- `workspace/stage8_execution/t7_open_exhaustion_relay_necessity/T07_OPEN_EXHAUSTION_RELAY_NECESSITY_V001.seal.sha256` — target missing: T07_OPEN_EXHAUSTION_RELAY_NECESSITY_V001
- `workspace/stage8_execution/structural_core/STRUCTURAL_CORE_V001.seal.sha256` — target missing: STRUCTURAL_CORE_V001
- `workspace/stage8_execution/t7_relayed_family_resolution/T07_RELAYED_FAMILY_RESOLUTION_V001.seal.sha256` — target missing: T07_RELAYED_FAMILY_RESOLUTION_V001
- `workspace/stage8_execution/t7_causal_line_connection_return_lift/T07_CAUSAL_LINE_CONNECTION_RETURN_LIFT_V001.seal.sha256` — target missing: T07_CAUSAL_LINE_CONNECTION_RETURN_LIFT_V001

### deploy_state

- severity: `RED`
- status: `RED`
- issue_count: `1`
- metric: `1`
- summary: archive deploy state not clean/current
- details: `{"ahead_count": 0, "porcelain": ["?? CORPUS_CHECK_REPORT_2026-07-29.md", "?? CORPUS_CHECK_REPORT_2026-07-29.md.seal.sha256", "?? CORPUS_CHECK_USAGE.md", "?? CORPUS_CHECK_USAGE.md.seal.sha256", "?? corpus_check.py", "?? corpus_check.py.seal.sha256", "?? corpus_check_baseline_v001.json", "?? corpus_check_baseline_v001.json.seal.sha256"]}`

Sample findings:
- `.` — working tree not clean

### substring_certification

- severity: `YELLOW`
- status: `YELLOW`
- issue_count: `6`
- metric: `6`
- summary: 6 substring-certification comparisons over checker-shaped scripts
- details: `{"scripts_scanned": 224}`

Sample findings:
- `workspace/scripts/audit_stage7_condition_implementation_v001.py:43` — substring certification over file text
- `workspace/scripts/audit_r3_4_causal_diamond_spectral_pullback_v001.py:102` — substring certification over file text
- `workspace/scripts/audit_stage8_t7_connected_analytic_closure_v001.py:87` — substring certification over file text
- `workspace/scripts/run_stage8_t7_connected_response_gate_v001.py:181` — substring certification over file text
- `workspace/scripts/run_stage8_t7_connected_response_gate_v001.py:183` — substring certification over file text
- `workspace/scripts/audit_stage8_t7_response_lift_v001.py:101` — substring certification over file text

### hardcoded_claim_flags

- severity: `YELLOW`
- status: `YELLOW`
- issue_count: `2927`
- metric: `2927`
- summary: 2927 literal boolean claim-shaped payload entries or assignments

Sample findings:
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/verify_r3_4_complete_causal_superconnection_parent_v001.py:188` — literal False for claim key alpha_computed
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/verify_r3_4_complete_causal_superconnection_parent_v001.py:189` — literal False for claim key proof_authorized
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/audit_r3_4_complete_causal_superconnection_parent_v001.py:533` — literal True for claim key finite_causal_source_record_parent_derived
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/audit_r3_4_complete_causal_superconnection_parent_v001.py:534` — literal False for claim key complete_causal_source_record_parent_flat_branch
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/audit_r3_4_complete_causal_superconnection_parent_v001.py:535` — literal False for claim key complete_parent_to_outgoing_GNS_map_derived
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/audit_r3_4_complete_causal_superconnection_parent_v001.py:536` — literal False for claim key absolute_record_interval_derived
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/audit_r3_4_complete_causal_superconnection_parent_v001.py:537` — literal False for claim key curved_nonstationary_parent_derived
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/audit_r3_4_complete_causal_superconnection_parent_v001.py:538` — literal False for claim key interacting_gauge_infraparticle_spectrum_derived
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/audit_r3_4_complete_causal_superconnection_parent_v001.py:539` — literal False for claim key complete_parameter_free_Q_spec_frozen
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/audit_r3_4_complete_causal_superconnection_parent_v001.py:540` — literal False for claim key physical_Thomson_stiffness_computed
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/audit_r3_4_complete_causal_superconnection_parent_v001.py:541` — literal False for claim key coupling_evaluation_authorized
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/audit_r3_4_complete_causal_superconnection_parent_v001.py:542` — literal False for claim key alpha_computed
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/audit_r3_4_complete_causal_superconnection_parent_v001.py:543` — literal False for claim key proof_authorized
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/audit_r3_4_complete_causal_superconnection_parent_v001.py:523` — literal True for claim key quasilocal_output_record_state_exists
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/audit_r3_4_complete_causal_superconnection_parent_v001.py:527` — literal False for claim key source_inclusive_state_projective_limit_derived
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/audit_r3_4_complete_causal_superconnection_parent_v001.py:528` — literal False for claim key infinite_future_Moller_limit_derived
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/audit_r3_4_complete_causal_superconnection_parent_v001.py:529` — literal False for claim key continuum_regulator_independence_derived
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/audit_r3_3_global_intrinsic_measure_classification_v001.py:331` — literal False for claim key spectral_density_derived
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/audit_r3_3_global_intrinsic_measure_classification_v001.py:332` — literal False for claim key complete_parent_generator_derived
- `workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/scripts/audit_r3_3_global_intrinsic_measure_classification_v001.py:335` — literal False for claim key alpha_computed
- ... 2907 more not shown

### voided_pass

- severity: `RED`
- status: `GREEN`
- issue_count: `0`
- metric: `0`
- summary: 54 PASS result hashes checked against 4 failure-shaped provenance files

### marker_prefix_collision

- severity: `RED`
- status: `GREEN`
- issue_count: `0`
- metric: `0`
- summary: 6 substring-matched PASS markers checked for strict-prefix collisions

### superseded_path_hardwire

- severity: `YELLOW`
- status: `YELLOW`
- issue_count: `546`
- metric: `546`
- summary: 546 vNNN hardwires with vNNN+1 present

Sample findings:
- `workspace/CURRENT_AUTHORITY_LEDGER_V006.json:40` — references results/microscopic_exhaustion_v001.json while successor microscopic_exhaustion_v002.json exists
- `workspace/CURRENT_AUTHORITY_LEDGER_V006.json:41` — references results/public_charged_action_uniqueness_v001.json while successor public_charged_action_uniqueness_v002.json exists
- `workspace/CURRENT_AUTHORITY_LEDGER_V010.json:63` — references results/microscopic_exhaustion_v001.json while successor microscopic_exhaustion_v002.json exists
- `workspace/CURRENT_AUTHORITY_LEDGER_V010.json:64` — references results/public_charged_action_uniqueness_v001.json while successor public_charged_action_uniqueness_v002.json exists
- `workspace/STAGE8_T7_CYCLE7_PACKAGE_RECORD_AND_THREE_FINDINGS_V001.md:156` — references test_stage8_t7_controller_v002.py while successor test_stage8_t7_controller_v003.py exists
- `workspace/COMPLETE_QSPEC_ANALYTIC_CONTINUATION_INDEPENDENT_ISOMETRY_STABILIZATION_ADDENDUM_V001.md:15` — references scripts/verify_complete_qspec_periodic_analytic_continuation_v002.py while successor verify_complete_qspec_periodic_analytic_continuation_v003.py exists
- `workspace/COMPLETE_QSPEC_ANALYTIC_CONTINUATION_INDEPENDENT_ISOMETRY_STABILIZATION_ADDENDUM_V001.md:16` — references stage8_execution/work/QSPEC_periodic_analytic_continuation_verification_v002.json while successor QSPEC_periodic_analytic_continuation_verification_v003.json exists
- `workspace/CURRENT_AUTHORITY_LEDGER_V011.json:6` — references scripts/audit_current_authority_v010.py while successor audit_current_authority_v011.py exists
- `workspace/CURRENT_AUTHORITY_LEDGER_V011.json:8` — references tests/test_current_authority_v010.py while successor test_current_authority_v011.py exists
- `workspace/CURRENT_AUTHORITY_LEDGER_V011.json:10` — references results/current_authority_v010.json while successor current_authority_v011.json exists
- `workspace/STAGE8_T7_QUARANTINE_COLLATERAL_V005_SUITE_RECORD_V001.md:19` — references scripts/test_stage8_t7_launcher_v005.py while successor test_stage8_t7_launcher_v006.py exists
- `workspace/STAGE8_T7_QUARANTINE_COLLATERAL_V005_SUITE_RECORD_V001.md:36` — references test_stage8_t7_launcher_v005.py while successor test_stage8_t7_launcher_v006.py exists
- `workspace/STAGE8_T7_QUARANTINE_COLLATERAL_V005_SUITE_RECORD_V001.md:38` — references test_stage8_t7_launcher_v006.py while successor test_stage8_t7_launcher_v007.py exists
- `workspace/CURRENT_AUTHORITY_LEDGER_V007.json:44` — references results/microscopic_exhaustion_v001.json while successor microscopic_exhaustion_v002.json exists
- `workspace/CURRENT_AUTHORITY_LEDGER_V007.json:45` — references results/public_charged_action_uniqueness_v001.json while successor public_charged_action_uniqueness_v002.json exists
- `workspace/COMPLETE_QSPEC_ANALYTIC_CONTINUATION_INDEPENDENT_PREFLIGHT_FAILURE_V001.md:60` — references scripts/verify_complete_qspec_periodic_analytic_continuation_v001.py while successor verify_complete_qspec_periodic_analytic_continuation_v002.py exists
- `workspace/COMPLETE_QSPEC_ANALYTIC_CONTINUATION_INDEPENDENT_PREFLIGHT_FAILURE_V001.md:61` — references stage8_execution/work/QSPEC_periodic_analytic_continuation_verification_v001.json while successor QSPEC_periodic_analytic_continuation_verification_v002.json exists
- `workspace/STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_EXECUTION_BINDING_V001.md:17` — references scripts/verify_stage8_t7_primitive_operator_response_v001.py while successor verify_stage8_t7_primitive_operator_response_v002.py exists
- `workspace/STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_EXECUTION_BINDING_V001.md:18` — references scripts/run_stage8_t7_primitive_operator_response_v001.sh while successor run_stage8_t7_primitive_operator_response_v002.sh exists
- `workspace/COMPLETE_QSPEC_ANALYTIC_CONTINUATION_PREFLIGHT_FAILURE_V001.md:63` — references scripts/derive_complete_qspec_periodic_analytic_continuation_v003.py while successor derive_complete_qspec_periodic_analytic_continuation_v004.py exists
- ... 526 more not shown

### fingerprint_currency

- severity: `RED`
- status: `GREEN`
- issue_count: `0`
- metric: `0`
- summary: 1 tracked-hash manifests recomputed

### scope_declaration

- severity: `YELLOW`
- status: `YELLOW`
- issue_count: `107`
- metric: `107`
- summary: 107 negative assertions without nearby scope declaration

Sample findings:
- `workspace/COMPLETE_QSPEC_ABSOLUTE_SCALE_AND_CONTINUUM_PREREQUISITE_AUDIT_V001.md:132` — negative assertion lacks nearby search-root/scope declaration
- `workspace/SOURCE_RECORD_GENERATOR_STRUCTURE_GATE_V001.md:116` — negative assertion lacks nearby search-root/scope declaration
- `workspace/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V009.md:1450` — negative assertion lacks nearby search-root/scope declaration
- `workspace/STAGE8_NINE_ITEM_PLAN_REVIEW_AND_EXTRACTION_ERRATUM_V001.md:156` — negative assertion lacks nearby search-root/scope declaration
- `workspace/STAGE8_NINE_ITEM_PLAN_REVIEW_AND_EXTRACTION_ERRATUM_V001.md:161` — negative assertion lacks nearby search-root/scope declaration
- `workspace/STAGE8_T7_CYCLE7_PACKAGE_RECORD_AND_THREE_FINDINGS_V001.md:114` — negative assertion lacks nearby search-root/scope declaration
- `workspace/STAGE8_T7_CYCLE7_PACKAGE_RECORD_AND_THREE_FINDINGS_V001.md:115` — negative assertion lacks nearby search-root/scope declaration
- `workspace/STAGE8_F5_PROVENANCE_ERRATUM_AND_FORCING_GROUND_CORRECTION_V001.md:47` — negative assertion lacks nearby search-root/scope declaration
- `workspace/STAGE8_F5_PROVENANCE_ERRATUM_AND_FORCING_GROUND_CORRECTION_V001.md:84` — negative assertion lacks nearby search-root/scope declaration
- `workspace/STAGE8_T7_COMPLETED_CONDITIONED_DUHAMEL_IDENTITY_AND_INTERCHANGE_SCHEMA_SPEC_V001.md:360` — negative assertion lacks nearby search-root/scope declaration
- `workspace/STAGE8_STAGE_LABEL_RETIREMENT_9_10_11_V001.md:27` — negative assertion lacks nearby search-root/scope declaration
- `workspace/STAGE8_STAGE_LABEL_RETIREMENT_9_10_11_V001.md:114` — negative assertion lacks nearby search-root/scope declaration
- `workspace/STAGE8_T7_REFINEMENT_DEPENDENCE_ADDENDUM_V001.md:141` — negative assertion lacks nearby search-root/scope declaration
- `workspace/STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001.md:24` — negative assertion lacks nearby search-root/scope declaration
- `workspace/STAGE8_COLLAR_CONJUNCTION_CHARTER_RESULT_V001.md:81` — negative assertion lacks nearby search-root/scope declaration
- `workspace/STAGE8_COLLAR_CONJUNCTION_CHARTER_RESULT_V001.md:225` — negative assertion lacks nearby search-root/scope declaration
- `workspace/STAGE8_T7II_ATTEMPT_RESULT_OBSTRUCTION_NAMED_V001.md:76` — negative assertion lacks nearby search-root/scope declaration
- `workspace/STAGE8_T7II_ATTEMPT_RESULT_OBSTRUCTION_NAMED_V001.md:110` — negative assertion lacks nearby search-root/scope declaration
- `workspace/STAGE8_STEP_LIST_AND_DOWNSTREAM_STAGE_FINDING_V001.md:11` — negative assertion lacks nearby search-root/scope declaration
- `workspace/STAGE8_STEP_LIST_AND_DOWNSTREAM_STAGE_FINDING_V001.md:89` — negative assertion lacks nearby search-root/scope declaration
- ... 87 more not shown

### relay_sequence_head

- severity: `YELLOW`
- status: `YELLOW`
- issue_count: `17`
- metric: `17`
- summary: max paste number 124; 17 duplicate-number classes
- details: `{"duplicate_numbers_sample": [86, 90, 98, 100, 104, 105, 106, 111, 113, 114, 115, 116, 119, 120, 121, 122, 123], "max_paste_number": 124}`

Sample findings:
- `workspace/STAGE8_T7II_ATTEMPT_RESULT_OBSTRUCTION_NAMED_V001.md:4` — PASTE 106
- `workspace/STAGE8_RL2B_UNIFORMITY_REFUTED_RESULT_V001.md:6` — PASTE 113
- `workspace/STAGE8_R2_DETERMINATION_ERRATUM_001_R1_RULING_REACH.md:6` — PASTE 90
- `workspace/STAGE8_R2_DETERMINATION_ERRATUM_001_R1_RULING_REACH.md:343` — PASTE 90
- `workspace/STAGE8_R2_WELL_POSEDNESS_AND_INPUT_SEAL_DETERMINATION_V001.md:5` — PASTE 86
- `workspace/STAGE8_R2_WELL_POSEDNESS_AND_INPUT_SEAL_DETERMINATION_V001.md:304` — PASTE 86
- `workspace/STAGE8_Q2STOP_DISARM_GROUND_VERIFICATION_STOP_V001.md:4` — PASTE 96
- `workspace/STAGE8_CL1_ATTEMPT_RESULT_REFUTED_V001.md:4` — PASTE 116
- `workspace/STAGE8_REGISTER_COMPLETENESS_AUDIT_GAP_REPORT_V001.md:5` — PASTE 91
- `workspace/STAGE8_H1_CHAIN_VERIFICATION_RETURN_V001.md:4` — PASTE 108
- `workspace/STAGE8_REGISTER_COMPLETENESS_AUDIT_ADDENDUM_001_SECTION_LEVEL_SWEEP.md:6` — PASTE 106
- `workspace/STAGE8_V010_SATURATION_IDENTIFICATION_BLIND_ANSWER_V001.md:129` — PASTE 35
- `/Users/bgm/MB Work/alpha_supervision/A32_FREEZE_V002_RATIFIED_2026-07-28.md:94` — PASTE 114
- `/Users/bgm/MB Work/alpha_supervision/LANE_CHANGE_CUSTODY_CLAUDE_CONSTRUCTION_V002.md:27` — PASTE 115
- `/Users/bgm/MB Work/alpha_supervision/LANE_CHANGE_CUSTODY_CLAUDE_CONSTRUCTION_V002.md:36` — PASTE 115
- `/Users/bgm/MB Work/alpha_supervision/RELAY_PASTE_115_EINSTEIN_HANDOFF_REQUEST_2026-07-28.md:1` — PASTE 115
- `/Users/bgm/MB Work/alpha_supervision/RELAY_PASTE_123_CORPUS_CHECK_2026-07-29.md:1` — PASTE 123
- `/Users/bgm/MB Work/alpha_supervision/A32_FREEZE_DRAFT_V000_2026-07-28.md:3` — PASTE 105
- `/Users/bgm/MB Work/alpha_supervision/RELAY_PASTE_121_A32_ARTIFACTS_DEPLOY_2026-07-29.md:1` — PASTE 121
- `/Users/bgm/MB Work/alpha_supervision/PRINCIPAL_DECISION_QUEUE.md:53` — PASTE 122
- ... 30 more not shown

### authority_currency

- severity: `RED`
- status: `RED`
- issue_count: `2`
- metric: `2`
- summary: 6 principal ruling files checked against governing chain citations
- details: `{"governing_root": "/Users/bgm/MB Work/alpha-program-archive/workspace", "supervision_root": "/Users/bgm/MB Work/alpha_supervision"}`

Sample findings:
- `/Users/bgm/MB Work/alpha_supervision/A32_FREEZE_V001_PREPARED_2026-07-28.md` — principal ruling not cited by governing chain; sha256=13a3b8b28e3ccdceb7c3d19559985a1c4f4678e11b70e3deaf5e9b482ff32e08
- `/Users/bgm/MB Work/alpha_supervision/PREREGISTRATION_ENCODING_PRECEDENCE_PRINCIPAL_DECISION_2026-07-29.md` — principal ruling not cited by governing chain; sha256=70c4080eae018bd644a3f0694557f1c0e854d621aa61097c775737887fec528f
