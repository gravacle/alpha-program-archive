## PASTE 674 — DARIO LANE = BUILDER B (OPUS 5 ULTRA, HIGH EFFORT) — [TASK 6 / BUILD] CONFORM THE VERDICT TO YOUR OWN SCHEMA

(Same Dario session rules. ARCHIVE-SIDE ONLY; the registrar mirrors.)

CONTEXT: run 019 — your stdout canon was accepted; the parent then rejected the verdict against the SCHEMA: extra field `fixtures_replayed`. Registrar-verified: your OWN sealed `contracts/verifier_verdict.schema.json` declares 13 fields with `additionalProperties: false` and no `fixtures_replayed` — the emission violates your own contract, and A enforced it faithfully.

TASK: choose deliberately and justify — (a) conform the emission: carry fixture-replay results inside the schema's existing carriers (`findings` / `checks_replayed` as their shapes allow), no schema change; or (b) amend the schema to declare `fixtures_replayed` as its own single-cause delta (schema + sidecar + instance if pinned), if fixture replay genuinely deserves a first-class field per the R9 duty ("replays every fixture's expected result"). State which and why; dry-run demonstrating a schema-valid verdict on both the success and fail-closed paths; disclosed delta; PIN CHECK.

OUTPUT: updated verifier (and schema, if (b)) + one sealed artifact
`STAGE8_TASK6_VERDICT_SCHEMA_CONFORM_DARIO_V001.md`
with final lines: `CHOICE = conform / amend (+reason)`, `VERDICT = schema-valid on all emission paths (demonstrated)`, `SELF_CHECK = passed`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal, report hashes, STOP (the registrar mirrors and re-invokes). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
