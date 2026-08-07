## PASTE 653 — CODEX LANE 2 = BUILDER A (GPT-5.6-SOL, EXTRA-HIGH) — [TASK 6 / BUILD] THE AUTHORIZATION-CHECK FIX + THE AUTHORED-EXPECTATION AUDIT

(Same Lane 2 session rules: cleanroom writes; the registrar mirrors. Register head Q-592 — satisfiable via the cleanroom snapshot mechanism if the supervision tree is unreachable: the registrar will have placed `REGISTER_HEAD_SNAPSHOT_Q592_2026-08-07.md` in the cleanroom; verify its seal and proceed.)

CONTEXT: the first invocation stopped at `RD22_PARENT_FAIL AUTHORIZATION_CONTENT`. Your hash pin on the sealed decision PASSED; your prose-line check requires `"Builder A               = Codex Lane 2 (parent + producer)"` — a column-aligned paraphrase that appears nowhere in the sealed decision (`DECISION_RD22_BUILD_AUTHORIZED_2026-08-07.md`, SHA-256 `ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340`; its actual line: `Builder A (producer + parent)  = Codex Lane 2   (GPT family)`). An expectation authored rather than cited — the BR-1 class in your own preflight.

TASK:
H1. **Fix `validate_authorization`:** every required content line must be a VERBATIM QUOTE of the sealed decision's bytes (or drop prose-line checks entirely in favor of the already-enforced hash pin + the three hash strings — state which you chose and why; the hash-pin-only form is the BR-1-clean choice).
H2. **The authored-expectation audit:** sweep parent.py and producer.py for EVERY expected-content literal (strings compared against external sealed inputs) and verify each is a verbatim quote of its sealed source at its pinned hash — a table: literal, source, verbatim yes/no. Any non-verbatim literal is fixed the same way.
H3. Re-run the static self-check; update inventories/hashes; disclosed delta table; PIN CHECK.

OUTPUT: updated code + one sealed artifact
`STAGE8_TASK6_AUTH_CHECK_FIX_LANE2_V001.md`
with final lines: `FIX = verbatim / hash_pin_only (+reason)`, `AUDIT = N literals checked (+non-verbatim count, all fixed)`, `SELF_CHECK = passed`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal in the cleanroom, report hashes, STOP (the registrar mirrors and re-invokes). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
