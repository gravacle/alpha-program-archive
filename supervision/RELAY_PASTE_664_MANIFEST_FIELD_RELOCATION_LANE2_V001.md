## PASTE 664 — CODEX LANE 2 = BUILDER A (GPT-5.6-SOL, EXTRA-HIGH) — [TASK 6 / BUILD] RELOCATE manifest_sha256 TO THE RECEIPT

(Same Lane 2 session rules: cleanroom writes; the registrar mirrors.)

CONTEXT: run 011 passed reclassification and reached R8, which flagged `PRODUCER_SEMANTIC_DRIFT`. Registrar diff of the two outputs: the ONLY non-masked difference is `manifest_sha256` — each child cites its own mode's manifest, so cross-equality is impossible BY CONSTRUCTION; every check row, fixture row, and summary field agrees exactly. The sealed mask (process_id, monotonic_duration, python_optimize) is not to be widened; the field is misplaced: per-child identity belongs in the per-child RECEIPT, which is not semantically compared.

TASK:
T1. Move `manifest_sha256` (and any other per-child-by-construction field, if your audit finds one) from the producer OUTPUT to the producer RECEIPT; the parent keeps verifying each child's manifest identity from the receipt + its own launch record. The semantic comparison then runs on outputs that can lawfully be byte-equal.
T2. Audit the output schema for any other field that differs by construction between modes; none may remain in the compared surface.
T3. Static self-check; disclosed delta; PIN CHECK.

OUTPUT: updated producer/parent/schemas + one sealed artifact
`STAGE8_TASK6_MANIFEST_FIELD_RELOCATION_LANE2_V001.md`
with final lines: `RELOCATED = manifest_sha256 -> receipt (+any others)`, `COMPARED_SURFACE = mode-invariant by construction`, `SELF_CHECK = passed`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal in the cleanroom, report hashes, STOP (the registrar mirrors and re-invokes). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
