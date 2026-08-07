## PASTE 693 — DARIO LANE = BUILDER B (OPUS 5 ULTRA, HIGH EFFORT) — [TASK 6 / TRANCHE] THE REPLAY DISAGREEMENT: DIAGNOSE AT SOURCE

(Same Dario session rules. ARCHIVE-SIDE ONLY; the registrar mirrors. Run 030's artifacts are mirrored to archive `rd22_run_030/`.)

CONTEXT: run 030 — `REPLAY_DISAGREE: producer says PASS, independent replay says FAIL` on C-B-V009-06. Registrar forensics: A's payloads are CORRECT — the 594-byte graph payload is byte-perfect canonical of the authoritative 11-node stage_dependencies (registrar re-derived from the provenance source; zero missing, zero diffs), and the 932-byte raw span is the true grounding bytes. But the raw span is a KEY-PREFIXED FRAGMENT (`"stage_dependencies": {…}` — it does not parse standalone). The candidate root cause: your replay's r_ground derivation from raw span to comparable value (the wrap/strip recipe) differs from A's.

TASK:
G1. Reproduce your replay's FAIL locally on the run-030 evidence; name the exact failing step and its inputs (display, not summary).
G2. Adjudicate at the spec: does V007's row text DETERMINE the raw-span-to-value recipe? If yes — fix your replay to the spec's recipe (disclosed delta; the fix must make the FAIL/PASS verdict follow the spec, not follow A). If no — the recipe is a SPEC GAP: report it precisely (what the row must state), do not guess, and your replay's refusal stands as lawful until the spec states it.
G3. Either way: the disagreement's resolution must be grounded in sealed text, and your artifact says which side's computation matched it. Dry-run; PIN CHECK.

OUTPUT: updated verifier (if G2-yes) + one sealed artifact
`STAGE8_TASK6_REPLAY_DISAGREE_DARIO_V001.md`
with final lines: `FAILING_STEP = (named, displayed)`, `SPEC_DETERMINES = yes (fixed to spec) / no (gap stated)`, `VERDICT_FOLLOWS = the spec / pending spec`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal, report hashes, STOP (the registrar mirrors and re-invokes or routes the spec item). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
