## PASTE 686 — DARIO LANE = BUILDER B (OPUS 5 ULTRA, HIGH EFFORT) — [TASK 6 / TRANCHE] REPLAY BY ROLE: DIGEST-VERIFY ALL, PARSE ONLY THE CONSUMED

(Same Dario session rules. ARCHIVE-SIDE ONLY; the registrar mirrors.)

CONTEXT: run 025 — the evidence now materializes and your replay reads it; the single fault moved inside: `C-B-V009-06: evidence must be a JSON object`. Registrar root-cause: the row's evidence is TWO payloads with different ROLES — the 932-byte RAW SEALED SPAN (byte-grounding; a slice of a larger JSON file; lawfully not standalone-parseable; its truth is byte-identity, checked by digest) and the 1218-byte DAG-ARGS dict (the consumable object; parses clean). Your replay demands every payload parse as a JSON object — too strict by one class: raw grounding payloads (spans of sealed markdown/JSON sources) can never satisfy it and never need to.

TASK: the replay distinguishes payload roles from the row's recorded invocation — ALL payloads digest-verified against observed digests; JSON-parsing and structural consumption applied ONLY to payloads the invocation consumes as structured arguments; raw grounding payloads verified by digest and byte-span linkage alone. Guard both directions: a consumable payload that fails to parse is still a fault; a raw payload is never silently promoted to consumable. Dry-run demonstration on the V009-06 pair; disclosed delta; PIN CHECK.

OUTPUT: updated verifier + one sealed artifact
`STAGE8_TASK6_REPLAY_ROLES_DARIO_V001.md`
with final lines: `REPLAY = role-typed (digest-all, parse-consumed)`, `BOTH_GUARDS = demonstrated`, `SELF_CHECK = passed`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal, report hashes, STOP (the registrar mirrors and re-invokes). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
