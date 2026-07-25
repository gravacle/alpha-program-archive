# Stage-8 Required Return Completion v001

Date: 2026-07-24

## Authority artifacts

Fable-authored theorem-battery authority mirror:

`STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_AUTHORITY_FABLE_V002.md`

SHA-256:

`ddb36cbfe4edfc2a0520e9ae58063295214c64afed5cad5a64e9f311826358f5`

Fable-authored independent evaluator:

`stage8_battery_evaluator_v001.py`

SHA-256:

`b053b4b16fb1dd858430a9898bf983894b610d353a5840c50e7a430e2affeba9`

The byte-exact authority mirror is the evaluator's `--spec` input. The
custody-wrapped in-workspace specification remains
`STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_V001.md`, SHA-256
`85d24996987278b285d63b8fe15a8732e55664e7c1b09063617b66cb4bc926b4`.
The files have different hashes only because the in-workspace copy carries
the required custody header; its external authoring body is byte-identical.

## Evaluator self-test

Command:

`python3 stage8_battery_evaluator_v001.py --selftest`

Recorded output:

`SELFTEST PASS: transform fence, commitment check, and prediction fence all fire on synthetic violations.`

The self-test was first run against the externally supplied evaluator after
its hash was verified, and repeated against the byte-exact workspace copy.

## Authorization state

`stage8_theorem_battery_authored = true`

`stage8_independent_evaluator_received = true`

`stage8_test_harness_received = true`

`stage8_cross_execution_authorized = true`

`stage8_cross_execution_completed = false`

`T0_first_cross_execution_obligation = true`

The evaluator is the sole authority for the battery verdict. Execution-lane
PASS strings have no verdict authority.

## Protected state

`primitive_output = "kappa_record only"`

`BID_core_result_sealed = false`

`spectral_evaluation_authorized = false`

`complete_Q_spec_sealed = false`

`physical_charged_amplitude_computed = false`

`physical_Thomson_stiffness_computed = false`

`coupling_evaluation_authorized = false`

`alpha_computed = false`

`proof_authorized = false`
