## PASTE 623 — DARIO LANE (OPUS 5 ULTRA, HIGH EFFORT) — [TASK 6 / SUBGATE] CROSS-FAMILY REVIEW: THE A35 EVALUATOR SPECIFICATION

(Same Dario session rules.)

PREFLIGHT (verify before starting; report any failure and STOP; live-append tolerance applies):
- Register head: Q-558 (your ledger review, registered; the spec under review is Q-555).
- Artifact under review: `alpha-program-archive/workspace/STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE3_V001.md`
  SHA-256 `eb2073ebb4f23cbc0c0bfa20a36c482e24c59dc6b6e1ccbcd1ef1bd1150d0ecb`. Verify before reading.
- Its claims: 63 numbered V003 blockers enumerated with byte-span anchors; 66 checks mapped (56 STRUCTURAL / 10 GATED-EXECUTION) over a closed 14-opcode language; the R0-R10 runner state machine per SP14; 6 regression fixtures; 3 A35-only sharpenings given their own check IDs; 2 unnumbered V003 pre-seal regressions carried as conjuncts; a displayed runtime-pin ambiguity (v012 name resolves to two snapshot candidates); AUTHORIZATION not claimed.
- Custody: Codex 3 specified; you verify. Adversarial posture; over-claiming worse than an honest kill. M-2 three-guard searches; APPEAL PREFLIGHT rule (check supersession before citing any conflict).

TASK — bounded, verdict per item:
E1. **The census:** re-derive the 63-blocker count from `BID_FULL_STACK_REVIEW_LEDGER_V003.md` (`c09f2c24…`) at the cited spans — every numbered blocker present, none invented, none double-counted; the A35 title-vs-operative-sentence scope judgment (all of V003 in scope) correct; the three A35-only sharpenings genuinely absent from V003 as standalone blockers; the two unnumbered regressions correctly carried as conjuncts rather than promoted.
E2. **The map:** for each of the 66 rows spot-checked in depth (at minimum: all 10 GATED-EXECUTION rows plus a sample of at least 12 STRUCTURAL rows across all six families) — does the executable procedure actually test the blocker's requirement of record? Is the PASS criterion exact and Boolean? Is the STRUCTURAL vs GATED-EXECUTION class assignment right — in particular, is any STRUCTURAL row secretly forming a fenced physical quantity, and is any GATED row actually runnable now?
E3. **The runner:** the R0-R10 state machine against SP14's demands (`5c679e37…`) — every SP14 demand mapped to a state, none weakened; the custody separation (Builder A / Builder B / Custodian C / principal / signature custodian) sufficient for the independent-verifier demand; child receipts non-authoritative throughout; the runtime-pin ambiguity display correct (both snapshot digests real, the fail-closed handling lawful).
E4. **The aggregate rule and firewall:** verify the aggregate cannot return PASS while the fences stand (the 10 NOT_RUN_GATE rows force it); the authority firewall complete (no path from a runner PASS to any seal or physics claim); the fixture quarantine sound.
E5. **Battery + one fresh attack** on the spec's weakest point.

OUTPUT: one artifact, lane-tagged filename
`STAGE8_TASK6_A35_EVALUATOR_SPEC_REVIEW_DARIO_V001.md`
with final lines: `SPEC = CONFIRMED / REFUTED (+items)`, `CENSUS = CONFIRMED / REFUTED`, `CLASS_ASSIGNMENTS = CONFIRMED / (+overrides)`, `RUNNER = CONFIRMED / REFUTED`, `AGGREGATE_FIREWALL = CONFIRMED / REFUTED`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the output filename already exists in the workspace, STOP and report — do not overwrite. Seal, mirror byte-identically to `alpha-program-archive/workspace/`, verify, report hashes, STOP. No register, plan, tracker, git, commit, or push action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation of any physical quantity; no comparison to measured constants. If a fence blocks a structural result, flag MACHINERY-APPEAL and continue.
