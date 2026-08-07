## PASTE 675 — CODEX LANE 2 = BUILDER A (GPT-5.6-SOL, EXTRA-HIGH) — [TASK 6 / BUILD] VALIDATE THE VERDICT AGAINST THE SEALED SCHEMA, NOT A TRANSCRIBED LIST

(Same Lane 2 session rules: cleanroom writes; the registrar mirrors.)

CONTEXT: run 019's stop and B's 674 response — B amended its own output contract deliberately (oneOf: a 14-field full verdict / a 3-field fault document, each closed; the reasoning is the program's absent-vs-empty law). Your `verifier_stdout` hard-codes a 13-field list — an AUTHORED TRANSCRIPTION of B's contract, the same class your authorization prose-lines were (Q-592). It will reject the lawful amended verdict.

TASK:
X1. Validate the verifier's stdout against B's SEALED schema file (`evaluator_build_B/contracts/verifier_verdict.schema.json`) as a content-addressed input: pin its digest in your external-inputs/manifest (new kind, e.g. `verifier_verdict_schema`, hash-verified at R0 like every input), implement the schema check (the subset you need: type/required/additionalProperties/oneOf/const — state your supported keyword list as B did), and accept BOTH document kinds with the semantic checks (schema name, expected verdict, spec/auth digests) applied per kind.
X2. Remove the transcribed field list; audit for any OTHER transcription of B's contract (the entry_point regex, exit map, stdout discipline are addendum-contract items — those are lawful; B's OUTPUT shape is B's schema's).
X3. Static self-check; disclosed delta; PIN CHECK.

OUTPUT: updated parent + one sealed artifact
`STAGE8_TASK6_VALIDATE_AGAINST_SCHEMA_LANE2_V001.md`
with final lines: `VERDICT_VALIDATION = against B's sealed schema (pinned; +supported keywords)`, `TRANSCRIPTIONS = removed (+audit)`, `SELF_CHECK = passed`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal in the cleanroom, report hashes, STOP (the registrar mirrors and re-invokes). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
