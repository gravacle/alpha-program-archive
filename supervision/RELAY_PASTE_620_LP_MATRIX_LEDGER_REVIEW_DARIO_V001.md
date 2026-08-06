## PASTE 620 — DARIO LANE (OPUS 5 ULTRA, HIGH EFFORT) — [TASK 6 / SUBGATE] CUSTODY REVIEW: THE LP-MATRIX THIRTY-ROW LEDGER

(Same Dario session rules.)

PREFLIGHT (verify before starting; report any failure and STOP; live-append tolerance applies):
- Register head: Q-554 (your assembly, registered; the ledger under review is Q-553).
- Artifact under review: `alpha-program-archive/workspace/STAGE8_TASK6_LP_MATRIX_LEDGER_LANE3_V001.md`
  SHA-256 `bc6c3e496ffd6e8d06cc3237e47a6a02b76faaa88b63b0ffb38684971c2d1362`. Verify before reading.
- Its claim: the immutable V011 lineage (five-row canonical root manifest, SHA-256 `4c04e4aa…`) executes as 24 PASS / 2 FAIL (A25, A27) / 4 BLOCKED (A23, A24, A28, A35) / 0 FENCE-ADJACENT, hence `passed_A01_A29_and_A35 = false` and SPEC-SEAL = false at root.
- Custody: Codex 3 executed; you verify. Adversarial posture: over-claiming is worse than an honest kill. M-2 three-guard searches throughout.

TASK — bounded, verdict per item:
V1. **The lineage:** recompute the five-row root manifest hash; re-run or re-verify the 113/113 packet manifest claim; rule whether the five members are the lawful lineage (and the audit matrix/blocker ledger correctly kept as protocol authorities, not lineage members).
V2. **PASS verification:** re-derive in full the load-bearing displays — A10 (Gram), A13 (colimit collapse), A14 (frozen reduction incl. the D_x hostile family), A17 (adjoint), A21 (the CPT/CP-axial branch audit and its branch scoping), A26 (Moore-Penrose lift), A29 (loop preregistration columns) — and spot-check the remaining PASS rows against their cited V011 line ranges. Each: CONFIRMED / REFUTED (+the display's defect).
V3. **FAIL/BLOCKED verification:** A25 and A27 — are the false conjuncts genuinely false of record at the cited pins? A23/A24/A28/A35 — are the missing objects genuinely absent under M-2 (scope-limited honesty preserved)? And rule explicitly: is any of the six correctly FENCE-ADJACENT rather than FAIL/BLOCKED, or vice versa?
V4. **The consequence:** the SPEC-SEAL propagation chain and the invalidation rule (any repair increments the lineage; full thirty-row rerun; no delta-only carry) verified against the authoritative machine graph.
V5. **Battery + one fresh attack** of your choosing on the ledger's weakest point.

OUTPUT: one artifact, lane-tagged filename
`STAGE8_TASK6_LP_MATRIX_LEDGER_REVIEW_DARIO_V001.md`
with final lines: `LEDGER = CONFIRMED / REFUTED (+items)`, `ROW_OVERRIDES = none / (list)`, `LINEAGE = CONFIRMED / REFUTED`, `CONSEQUENCE = CONFIRMED / REFUTED`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the output filename already exists in the workspace, STOP and report — do not overwrite. Seal, mirror byte-identically to `alpha-program-archive/workspace/`, verify, report hashes, STOP. No register, plan, tracker, git, commit, or push action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation of any physical quantity; no comparison to measured constants. If a fence blocks a structural result, flag MACHINERY-APPEAL and continue.
