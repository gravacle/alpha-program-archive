## PASTE 656 — CODEX LANE 2 = BUILDER A (GPT-5.6-SOL, EXTRA-HIGH) — [TASK 6 / BUILD] THE CANON FIX: DROP THE TRAILING NEWLINE

(Same Lane 2 session rules: cleanroom writes; the registrar mirrors.)

CONTEXT (Q-594): run 005 stopped at `VERIFIER_MANIFEST_NOT_CANONICAL` over ONE BYTE — your `canonical_bytes` appends a trailing newline; the sealed spec §9.4 demands "no insignificant whitespace"; the adjudication is against the newline. Builder B's tight form is the lawful canon.

TASK:
M1. Remove the `+ "\\n"` from `canonical_bytes` (and any counterpart in producer.py/tools); regenerate every canonical artifact in your package under the corrected form (manifests, check_map, fixture manifest, schemas where canonical); update all internal hash references and the package inventory.
M2. Re-run the static self-check; disclosed delta table; PIN CHECK.
M3. One audit line: confirm no OTHER canon deviation from §9.4's words exists in your encoder (key order, separators, unicode, number forms).

OUTPUT: updated code + one sealed artifact
`STAGE8_TASK6_CANON_NEWLINE_FIX_LANE2_V001.md`
with final lines: `CANON = tight, no trailing newline (spec-grounded)`, `REGENERATED = N files (+hashes)`, `AUDIT = no other deviation / (+items)`, `SELF_CHECK = passed`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal in the cleanroom, report hashes, STOP (the registrar mirrors and re-invokes). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
