## PASTE 659 — DARIO LANE = BUILDER B (OPUS 5 ULTRA, HIGH EFFORT) — [TASK 6 / BUILD] FLAT RUN-ROOT OUTPUT PATHS

(Same Dario session rules. ARCHIVE-SIDE ONLY; the registrar mirrors.)

CONTEXT: run 008 PASSED the evidence-root gate — your independently computed `e7820ca5…` and A's declared_root agree exactly; the two-builder convergence worked. The stop is now `VERIFIER_OUTPUT_CONTRACT`: your `output_path`/`receipt_path` (`verifier/verdict.json`, `verifier/receipt.json`) resolve into your own PACKAGE directory, while outputs belong in the custodian's fresh RUN ROOT, flat, per the producer-child pattern the parent enforces: `verifier.verdict.json` and `verifier.receipt.json`.

TASK:
Q1. Update the instance: `output_path` = `verifier.verdict.json`, `receipt_path` = `verifier.receipt.json` (run-root-relative, flat); confirm your verifier writes to the argv-substituted paths at run time (the parent fills the tokens) and never into its package. Update the sidecar; canonical tight form.
Q2. Confirm the run-isolation principle in one line of the artifact: a verifier that writes inside its own immutable package would corrupt its next run's integrity baseline — the run root is the only writable surface.
Q3. Disclosed delta; PIN CHECK.

OUTPUT: updated instance + sidecar + one sealed artifact
`STAGE8_TASK6_OUTPUT_PATHS_FIX_DARIO_V001.md`
with final lines: `PATHS = flat run-root (+both names)`, `WRITE_SURFACE = run root only (confirmed)`, `INSTANCE = canonical, sidecar-pinned`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal, report hashes, STOP (the registrar mirrors and re-invokes). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
