## PASTE 699 — CODEX 2 LANE = BUILDER A (5.6 SOL EXTRA HIGH) — [TASK 6 / TRANCHE] V010: THE GROUND-ATOM RESOLUTION STATEMENT

(Same Codex 2 session rules. CLEANROOM-ONLY writes; the registrar mirrors. THE FIRST-TIME-RIGHT RULES apply.)

CONTEXT (Q-614): RUN 031 — the chain executed END-TO-END for the first time. Census, root, argv, manifests, P0 all cleared; your producer emitted the seven-field carrier and 1 PASS / 55 FAIL / 10 NOT_RUN_GATE (the exact expected n=1 shape). ONE substantive verifier fault remains: `REPLAY: C-B-V009-06: evidence has no result 'r_ground'`. Adjudication of record: r_ground's operands are the member-payload digest (which the verifier computes ITSELF in P0) and the sealed spec constant. A producer-recorded r_ground carrier would hand the producer both operands of a passing comparison — BR-1 forbids it. Your producer's omission is CONFORMANT; the spec must say so.

TASK (bounded):
M1. AUTHOR SPEC V010: a finite delta from V009 (900a240d…), 66 rows unchanged, carrying ONE statement: ground atoms whose consumable operands are fully derivable from the verifier's own P0-verified evidence table plus sealed spec constants are replayed by R9 from those sources ALONE — no producer carrier exists for them, a producer-recorded result object for such an atom is a fault (BR-1), and the row's singular `invocation` carrier remains bound to structured-evidence consumption only. State the operand-derivation rule as a closed schema over the atom classes present in the descriptor language (which atoms qualify: exact criteria, not examples).
M2. Confirm from bytes that your producer and parent need ZERO code change under M1 (the omission is conformant); if anything does need change, that is a finding to display, not to silently fix. Re-pin package references V009→V010; full pin closure grep value AND name; regenerate inventory/manifests; dry-run touched paths.
OUTPUT: `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V010.md` + one sealed artifact `STAGE8_TASK6_V010_GROUND_ATOMS_CODEX2_V001.md`
with final lines: `SPEC_DELTA = one statement only / (+items)`, `ROWS_CHANGED = 0`, `CODE_CHANGED = none / (displayed findings)`, `PIN_CLOSURE = N hits, all resolved`, `DRY_RUN = executed`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If a name exists, STOP. Seal, report hashes, STOP (the registrar mirrors; B implements ground-atom resolution next; run 032 is the confirmation run). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
