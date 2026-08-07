## PASTE 683 — DARIO LANE (OPUS 5 ULTRA, HIGH EFFORT) — [TASK 6 / TRANCHE] BOUNDED CHECK: THE ENVELOPE + SPEC V006

(Same Dario session rules. ARCHIVE-SIDE ONLY; the registrar mirrors.)

PREFLIGHT (verify before starting; report any failure and STOP; live-append tolerance applies):
- Register head: Q-607.
- Under review: the envelope work (`STAGE8_TASK6_V009_06_ENVELOPE_SPEC_V006_LANE2_V001.md` = `832a3c10e92c5503c2c466fd53872bb89f1c37ff7bae6fc705608247156c6271`) and spec V006 (`STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V006.md` = `1b8b03e4b2688acb30d8c3f5afea3529be8322f8541406adae520aa51e654995`) vs base V005 `f8d1a7dc…`. Your relocation (`69334875…`) is the grounding authority.

TASK — bounded:
D1. **The envelope:** the payload bytes byte-identical to the relocated member span; the DAG-argument serialization faithful (the dict as adjacency, value arrays as required parents — your own grounding); the barred encoding and status field absent from both payloads; the manifest row and declared_root correct.
D2. **Spec V006:** the corpus rule faithful to the Q-606 finding (S must name a sealed corpus definition; SPEC-INCOMPLETE rows cannot be populated); the 17-row registry complete against your own sweep expectations (you found 4 and warned of recurrence — verify the 17 by re-derivation); zero descriptor-row changes (diff scope); carriage complete.
D3. **The run-pin note:** the artifact states the authorized runtime pin remains V005 for the chain — confirm that is lawful for run 023 (V006 changes no consumed row) and state what lineage V2 must carry.
D4. Verdict under the VERDICT-LINE SCOPE RULE.

OUTPUT: one sealed artifact IN THE ARCHIVE WORKSPACE
`STAGE8_TASK6_ENVELOPE_V006_CHECK_DARIO_V001.md`
with final lines: `ENVELOPE = CONFIRMED / (+items)`, `SPEC_V006 = CONFIRMED (+17-row registry verdict)`, `RUN_PIN = lawful for 023 / (+finding)`, `READY_FOR_RUN_023 = yes/no`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal, report hashes, STOP (the registrar mirrors and invokes run 023). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
