## PASTE 619 — CODEX LANE 3 (SOL, HIGH EFFORT) — [TASK 6 / SUBGATE] A35/RD-22: THE EVALUATOR SPECIFICATION

(Same Lane 3 session rules.)

PREFLIGHT (verify before starting; report any failure and STOP; live-append tolerance applies):
- Register head: Q-553 (your ledger, registered).
- THE TARGET (your `missing_A35`, independently attested by the source-parent gate SP14 and `independent_seal_evaluator_implemented=false`): the SPECIFICATION of the content-addressed optimization-safe regression evaluator — the complete blocker-to-executable-check map plus the runner architecture. SPEC ONLY: no code is run, no check is executed, no authorization is claimed (RD-22 authorization is a principal act, reserved). This supplies the missing object's DEFINITION so its build becomes mechanical and reviewable.
- Authorities: `BID_FULL_STACK_REVIEW_LEDGER_V003.md` (`c09f2c246c48ddfd0df127da26a22f08ba9ffd44f5c2118c178a0a5eba5d00e8` — the blocker census), the A35 row text in the audit matrix (`78f6bb08…`), the source-parent gate's runner demands (fresh optimization-safe parent, separate normal and `python -O` children, independent verifier, runtime reclassification, trust-record validation), your ledger (`bc6c3e49…`) for the missing-object statement, the M-2 three-guard protocol.
- Custody: you specify; Dario reviews. Tag every design decision PROVABLE / PART-PROVABLE / YOURS.

TASK:
S1. **The blocker census:** every blocker in V003 enumerated with a stable ID; the count stated; any blocker that A35's row text names but V003 lacks (or vice versa) flagged as a census discrepancy, not silently reconciled.
S2. **The blocker-to-check map:** one row per blocker — the check's inputs (content-addressed), its executable form (deterministic procedure, pass/fail criterion), and its EXECUTION CLASS: `STRUCTURAL` (runnable under the fences now) vs `GATED-EXECUTION` (running it would evaluate a physical quantity — the check is specified in full but marked as fence-gated until its gate opens). No check may be left as prose intent.
S3. **The runner architecture:** the optimization-safe parent, the separate normal and `python -O` children, the independent verifier's separation (who builds it vs who runs it — state the custody demand), runtime reclassification, trust-record validation, content-addressing of the runner itself, and the output form (a sealed machine-readable verdict ledger).
S4. **The regression fixtures:** the mandatory rejected competitors (the V010 zero-stiffness route, the zero survival amplitude, the `c`/`tau` families, primitive/Thomson conflation, the nonzero-index control) each mapped to a named fixture with its expected verdict.
S5. **Battery:** F_PLDEC; anti-tuning; surface anchor; M-2 searches; self verb audit. State plainly what this spec does NOT do: it does not implement, run, or authorize.

OUTPUT: one artifact, lane-tagged filename
`STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE3_V001.md`
with final lines: `BLOCKERS = N enumerated (+census discrepancies)`, `CHECKS = N mapped (+STRUCTURAL/GATED-EXECUTION counts)`, `RUNNER = specified`, `FIXTURES = N named`, `AUTHORIZATION = not_claimed`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the output filename already exists in the workspace, STOP and report — do not overwrite. Seal, mirror byte-identically to `alpha-program-archive/workspace/`, verify, report hashes, STOP. No register, plan, tracker, git, commit, or push action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation of any physical quantity; no comparison to measured constants. If a fence blocks a structural result, flag MACHINERY-APPEAL and continue.
