## PASTE 673 — DARIO LANE = BUILDER B (OPUS 5 ULTRA, HIGH EFFORT) — [TASK 6 / BUILD] THE STDOUT NEWLINE

(Same Dario session rules. ARCHIVE-SIDE ONLY; the registrar mirrors.)

CONTEXT: run 018 — your verifier RAN COMPLETE and emitted its full canonical verdict (24,555 bytes, one tight JSON value, exit 1 = faults found, exactly the preregistered honest behavior). The parent rejects the stdout shape: your `print` appends a trailing newline, and the Q-594 canon adjudication — which convicted A's file canon of the same byte — reads "no insignificant whitespace" against it. Symmetric justice: the newline loses on both sides.

TASK: emit the verdict via `sys.stdout.write` (or equivalent) with NO trailing newline; confirm stderr stays empty in the success path; dry-run demonstration showing byte-exact stdout; disclosed delta; PIN CHECK.

OUTPUT: updated verifier + one sealed artifact
`STAGE8_TASK6_STDOUT_NEWLINE_DARIO_V001.md`
with final lines: `STDOUT = tight canonical value, no trailing newline (demonstrated)`, `SELF_CHECK = passed`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal, report hashes, STOP (the registrar mirrors and re-invokes). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
