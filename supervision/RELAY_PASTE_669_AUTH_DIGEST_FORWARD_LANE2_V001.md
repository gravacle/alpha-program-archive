## PASTE 669 — CODEX LANE 2 = BUILDER A (GPT-5.6-SOL, EXTRA-HIGH) — [TASK 6 / BUILD] FORWARD THE AUTHORIZATION DIGEST

(Same Lane 2 session rules: cleanroom writes; the registrar mirrors.)

CONTEXT: run 015 — trust root accepted; the verifier fail-closed one field deeper: `authorization: missing 'artifact_sha256'`. Builder B checks the RD-22 authorization AS A CONTENT-ADDRESSED INPUT (correct per the decision's own terms); your parent verifies the authorization file itself but does not forward its digest in the authorization record of the bound context.

TASK: include `artifact_sha256` (the verified digest of the authorization file — `ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340` computed at R0, never hard-coded: forward the value your parent verified) in the authorization record handed to the verifier (bound manifest/environment), plus any sibling fields B's contract lists for that record — read the addendum/contract, not B's code, for the field set. Static self-check; disclosed delta; PIN CHECK.

OUTPUT: updated parent + one sealed artifact
`STAGE8_TASK6_AUTH_DIGEST_FORWARD_LANE2_V001.md`
with final lines: `AUTH_RECORD = artifact_sha256 forwarded (verified value, not literal)`, `FIELDS = per contract (+list)`, `SELF_CHECK = passed`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal in the cleanroom, report hashes, STOP (the registrar mirrors and re-invokes). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
