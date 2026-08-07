## PASTE 678 — CODEX LANE 2 = BUILDER A (GPT-5.6-SOL, EXTRA-HIGH) — [TASK 6 / BUILD] THE THIRD NEWLINE RULING + THE EVENT PAYLOADS

(Same Lane 2 session rules: cleanroom writes; the registrar mirrors.)

CONTEXT (Q-602): run 021 ran END TO END — the fault list is substantially the preregistered honest outcome. Two fault classes remain, both yours:
1. DESCRIPTOR_DIGEST x66: your `check_spec_sha256` hashes each sealed row INCLUDING the line terminator; B hashes it without. Registrar-reproduced both. The adjudication follows the two prior newline rulings: the terminator is excluded. Recompute all 66 against the sealed spec rows sans terminator (B's values are the expected result — but derive yours from the spec bytes, never copy B's list).
2. EVENT_LEDGER: a child row declares an event-class payload by digest at a run-root path where no file exists. Materialize the six event-class ledgers as files at the exact declared locations (empty classes as the canonical empty-list bytes whose digest is declared — the Q-601 absent-vs-empty law), so B's digest-fetch finds real bytes for every declared digest.

TASK: both fixes; check_map regenerated with the new digests; static self-check incl. a line asserting no digest in the map covers a terminator byte; disclosed delta; PIN CHECK.

OUTPUT: updated package + one sealed artifact
`STAGE8_TASK6_DESCRIPTOR_NEWLINE_EVENTS_LANE2_V001.md`
with final lines: `DESCRIPTORS = 66 recomputed sans terminator (derived from spec bytes)`, `EVENT_PAYLOADS = 6 classes materialized at declared paths`, `SELF_CHECK = passed`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal in the cleanroom, report hashes, STOP (the registrar mirrors and re-invokes). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
