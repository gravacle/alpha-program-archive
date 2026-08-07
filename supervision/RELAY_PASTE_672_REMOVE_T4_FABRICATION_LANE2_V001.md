## PASTE 672 — CODEX LANE 2 = BUILDER A (GPT-5.6-SOL, EXTRA-HIGH) — [TASK 6 / BUILD] REMOVE THE T4 FABRICATION

(Same Lane 2 session rules: cleanroom writes; the registrar mirrors.)

CONTEXT (Q-601): your own audit found it; the registrar adjudicated it: the verifier-input ledger carries T0-T3 EXACTLY; T4 is sampled after the verifier and lives only in the terminal ledger; copying T3 into T4 is barred as fabrication.

TASK: the verifier-input record hands T0-T3 (no T4 key at all); the terminal ledger keeps T0-T4 with T4 sampled at its true time; the self-check gains a line failing on any T4-before-sample. Static self-check; disclosed delta; PIN CHECK.

OUTPUT: updated parent + one sealed artifact
`STAGE8_TASK6_REMOVE_T4_FABRICATION_LANE2_V001.md`
with final lines: `INPUT_RECORD = T0-T3 (no T4 key)`, `TERMINAL = T0-T4 at true sample time`, `SELF_CHECK = passed (+the new guard line)`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal in the cleanroom, report hashes, STOP (the registrar mirrors and re-invokes). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
