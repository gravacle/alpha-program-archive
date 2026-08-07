## PASTE 660 — CODEX LANE 2 = BUILDER A (GPT-5.6-SOL, EXTRA-HIGH) — [TASK 6 / BUILD] THE LEDGER IS RUN-SCOPED: BIND POST-PRODUCTION

(Same Lane 2 session rules: cleanroom writes; the registrar mirrors.)

CONTEXT (Q-597's machine adjudication, now applied to your own parent): your `validate_verifier_manifest` requires, PRE-LAUNCH, an argv token naming an existing file whose digest equals `input_roots.ledger_sha256`. But the ledger is a PRODUCER OUTPUT — it cannot exist, and its digest cannot be known, before the producer children run. B's manifest lawfully carries the self-detecting all-zero sentinel there. Your parent currently demands the impossible.

TASK:
R1. **Split the validation per the 4/1 semantics:** pre-launch, the four pinned roots (spec, snapshot, gate, evidence) are value-checked as now, and `ledger_sha256` is checked only for FORM (64-hex) with the all-zero sentinel expressly lawful; POST-PRODUCTION and pre-verifier-launch, the parent (a) computes the produced ledger's digest, (b) BINDS it — substituting the real value into the verifier's launch context (the argv token fill and the environment the verifier reads), and (c) records both the sentinel-then-bound transition and the bound value in the run ledger and the verifier child row. The verifier's own `require_roots_bound()` then sees a bound root, which is exactly the handshake B built for.
R2. The argv ledger-file check moves to post-production (the file exists then); keep it exact.
R3. Static self-check; disclosed delta; PIN CHECK; one audit line confirming no OTHER pre-launch check demands a run-scoped object.

OUTPUT: updated parent + one sealed artifact
`STAGE8_TASK6_LEDGER_RUNTIME_BIND_LANE2_V001.md`
with final lines: `SPLIT = 4 pinned pre-run / 1 bound post-production`, `SENTINEL = lawful pre-run, bound before verifier launch (+recorded)`, `AUDIT = no other run-scoped pre-launch demand / (+items)`, `SELF_CHECK = passed`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal in the cleanroom, report hashes, STOP (the registrar mirrors and re-invokes). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
