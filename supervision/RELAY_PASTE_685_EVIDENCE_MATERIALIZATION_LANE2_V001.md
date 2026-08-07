## PASTE 685 — CODEX LANE 2 = BUILDER A (GPT-5.6-SOL, EXTRA-HIGH) — [TASK 6 / TRANCHE] MATERIALIZE CONSUMED EVIDENCE FOR REPLAY

(Same Lane 2 session rules: cleanroom writes; the registrar mirrors.)

CONTEXT (Q-609): run 024 — C-B-V009-06 PASSED in both children; the verifier's single REPLAY fault is that row: it replays evidence from the run root (`rd22_run_024/evidence/<digest>.json`) and the producer never materialized the consumed payloads there. The verifier's refusal is correct — no result on testimony.

TASK: the producer (or parent, per your architecture) materializes every CONSUMED evidence payload into the run root's `evidence/` as content-addressed files (exactly as the event payloads already are), so the verifier's declared replay path resolves for every row with observed evidence digests; static self-check incl. a line asserting consumed-implies-materialized; disclosed delta; PIN CHECK.

OUTPUT: updated code + one sealed artifact
`STAGE8_TASK6_EVIDENCE_MATERIALIZATION_LANE2_V001.md`
with final lines: `MATERIALIZATION = consumed evidence -> run root (content-addressed)`, `SELF_CHECK = passed (+the new guard line)`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal in the cleanroom, report hashes, STOP (the registrar mirrors and re-invokes). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
