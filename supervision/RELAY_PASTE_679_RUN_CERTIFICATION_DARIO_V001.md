## PASTE 679 — DARIO LANE (OPUS 5 ULTRA, HIGH EFFORT) — [TASK 6 / BUILD] THE FORMAL RUN CERTIFICATION: RUN 022 VS THE PREREGISTRATION

(Same Dario session rules. ARCHIVE-SIDE ONLY; the registrar mirrors. NOTE: run 022's artifacts live in the cleanroom run root — the registrar has mirrored them to archive `rd22_run_022/` for your reading.)

PREFLIGHT (verify before starting; report any failure and STOP; live-append tolerance applies):
- Register head: Q-603.
- The preregistration of record: Q-591's expected-outcome statement. The run artifacts: `rd22_run_022/` (normal/optimized outputs + receipts, producer ledger, bound manifest, verifier output).
- Custody note: you built the verifier; this review certifies THE RUN against THE PREREGISTRATION — a comparison of records, not a re-review of your own code.

TASK — bounded:
Z1. **The row-level comparison:** every one of the 66 check rows and 6 fixture rows against the preregistered expectation (56 FAIL / 10 NOT_RUN_GATE; 3/3); any deviation is a finding. The producer semantic agreement re-verified under the declared mask. The verifier's 59 findings mapped one-to-one onto the producer's failing rows (an absence the verifier missed, or reported that the producer lacks, is a finding).
Z2. **The honesty properties:** zero PASS (display); zero ERROR; the ten gated rows procedure_started=false; no terminal ledger exists (and why that is correct); the authority firewall fields all false in every artifact.
Z3. **The certification statement**, under the VERDICT-LINE SCOPE RULE: state exactly what this run certifies (the apparatus honestly reports the absent evidence layer under the pinned runtime) and what it does NOT (no row verified, no seal moved, A35 not attained, the aggregate cannot PASS).
Z4. Battery: PIN CHECK; self verb audit.

OUTPUT: one sealed artifact IN THE ARCHIVE WORKSPACE
`STAGE8_TASK6_RUN022_CERTIFICATION_DARIO_V001.md`
with final lines: `ROWS = 66+6 compared, N deviations`, `VERIFIER_MAPPING = one-to-one / (+items)`, `HONESTY = confirmed (+the display list)`, `CERTIFIES = (statement)`, `DOES_NOT_CERTIFY = (statement)`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal, report hashes, STOP (the registrar mirrors). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
