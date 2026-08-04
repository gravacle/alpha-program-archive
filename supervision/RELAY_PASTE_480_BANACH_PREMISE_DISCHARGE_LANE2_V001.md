## PASTE 480 — CODEX LANE 2 (HIGH EFFORT) — [TASK 5] CROSS-VERIFICATION OF THE CONDITIONAL THEOREM + THE PREMISE-DISCHARGE SWEEP

PREFLIGHT (verify before starting; report any failure and STOP):
- Register head: Q-401.
- Artifact under review (Lane 1's theorem): `alpha-program-archive/workspace/STAGE8_TASK5_B_IND_ANALYTIC_STRUCTURE_LANE1_V001.md`
  SHA-256 `88854f08966c15e6afbcb300c6151f59a169e2725c3d5a8643b653abfe3ddcb3`. Verify before reading.
- Authorities: metric V005 `2a379098…`, the sensitivity audit `a434b1bb…`, the consumption chain `cacd3173…`/`041498bb…`, the ratified definitions of B_ind as cited, DoR-008, Q-399/400/401.
- Custody: adversarial verification + the forward sweep. p, ν symbolic.

TASK — PASS / KILL per item:
V1. **The not-a-self-map result.** Verify: DoR-019's Hilbert carrier genuinely fails to make scalar B_ind a self-map — recompute the typing; a repair (an obvious ratified carrier making it a self-map) = KILL of the negative and better than a pass.
V2. **The conditional Banach theorem.** Verify the proof under its four premises (completeness, closure, boundedness, q < 1) — each premise's exact statement, the theorem's chain, the DoR-008 compatibility.
V3. **THE DISCHARGE SWEEP, premise by premise:** (i) COMPLETENESS of the scalar carrier — does DoR-019's completion convention or any ratified structure supply it, or is the scalar carrier's completion a new object? (ii) CLOSURE — does B_ind map the candidate set into itself by ratified properties? (iii) BOUNDEDNESS — derivable from the ratified bounds (the trace/tower bounds, the metric)? (iv) q < 1 — is the contraction modulus computable symbolically on the minimal stages, and does its value depend on the freedoms (this doubles as the first sensitivity data)? For each: DERIVED (chain) / CONSTRUCTIBLE (what to build) / UNDETERMINED (the exact gap).
V4. **The sensitivity restatement.** Under the conditional theorem: the fixed point's freedom-dependence is controlled by the map's derivative in the freedom directions against q — state what the sensitivity computation consumes once the premises hold; run it on the minimal stages if the ingredients exist.
V5. **Falsifiers + one fresh attack.**

OUTPUT: one artifact, lane-tagged filename
`STAGE8_TASK5_BANACH_PREMISE_DISCHARGE_LANE2_V001.md`
with the verdict table V1–V5, a premise ledger (per premise: DERIVED/CONSTRUCTIBLE/UNDETERMINED), and final lines:
`CONDITIONAL_THEOREM = CONFIRMED / KILLED (+item)` and `PREMISES = n/4 DISCHARGED (+which)`.
Seal, mirror byte-identically to `alpha-program-archive/workspace/`, verify, report hashes, STOP. No register, plan, tracker, git, commit, or push action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No numeric evaluation; no registered verdict; no comparison to measured constants. If a fence blocks a structural result, flag MACHINERY-APPEAL and continue.
