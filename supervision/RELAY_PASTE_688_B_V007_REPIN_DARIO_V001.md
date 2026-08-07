## PASTE 688 — DARIO LANE = BUILDER B (OPUS 5 ULTRA, HIGH EFFORT) — [TASK 6 / TRANCHE] B'S V007 RE-PIN

(Same Dario session rules. ARCHIVE-SIDE ONLY; the registrar mirrors.)

CONTEXT: spec V007 is sealed (`STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V007.md` = `d38d31719b64839744a98da5ee005fb50119f9a26b2b98b0e1a1de445b5d4973`; the coordinated A-side re-pin is done). Your verifier pins the governing spec by const and attests `spec_sha256` in the instance's input roots.

TASK: re-pin to V007 — the const, the instance's `spec_sha256` root (independently computed from the V007 bytes you verify, per your own discipline), the sidecar; verify your parse-expectations derive cleanly from V007 (the census, partition, and board must reproduce; V007's V009-06 row now states the single-authority identity explicitly — confirm your replay consumes it as reducible); disclosed delta; PIN CHECK.

OUTPUT: updated verifier/instance/sidecar + one sealed artifact
`STAGE8_TASK6_B_V007_REPIN_DARIO_V001.md`
with final lines: `SPEC_PIN = V007 (+value, independently computed)`, `PARSE = census/partition/board reproduce (+V009-06 row reducible)`, `DELTA = disclosed`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal, report hashes, STOP (the registrar mirrors and invokes run 026). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
