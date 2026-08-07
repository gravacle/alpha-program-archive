## PASTE 670 — CODEX LANE 2 = BUILDER A (GPT-5.6-SOL, EXTRA-HIGH) — [TASK 6 / BUILD] THE AUTHORIZATION SCOPE FIELD + THE T-LABEL QUESTION

(Same Lane 2 session rules: cleanroom writes; the registrar mirrors.)

CONTEXT: run 016 — the verifier fail-closed on `authorization: missing 'scope'`. Registrar-verified from the contract layer: the expected record is `{artifact_sha256, scope}` (presence-checked; your extra `valid` is tolerated). `scope` is the run's scope declaration — the same scope value your own ledger carries (the structural-first-run scope of the RD-22 decision), forwarded verbatim, never invented.

TASK:
W1. Add `scope` to the forwarded authorization record — the value your parent already carries in its ledger's scope field.
W2. **The T-label question — CHECK AND REPORT, do not guess:** the verifier revalidates trust snapshots with exact labels T0-T4, but T4 (after-verifier) cannot exist when the verifier reads its inputs. Determine what your parent hands the verifier (which labels, in which record) and REPORT the finding in the artifact: if the mismatch is structural (T4 postdates launch), state it as a cross-builder contract item for the registrar to adjudicate rather than absorbing it silently; if your parent can lawfully supply T0-T3 with T4 reserved-and-labeled, say what the record looks like.
W3. Static self-check; disclosed delta; PIN CHECK.

OUTPUT: updated parent + one sealed artifact
`STAGE8_TASK6_AUTH_SCOPE_LANE2_V001.md`
with final lines: `AUTH_RECORD = {artifact_sha256, scope} forwarded`, `T_LABELS = (finding reported)`, `SELF_CHECK = passed`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal in the cleanroom, report hashes, STOP (the registrar mirrors and re-invokes). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
