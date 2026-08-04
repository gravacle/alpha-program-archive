## PASTE 533 — CODEX LANE 1 (HIGH EFFORT) — [TASK 5] THE HELD CROSS-CHECK: LICENSED CONDITIONAL CHAIN V002

PREFLIGHT (verify before starting; report any failure and STOP):
- Register head: Q-456.
- Artifact under review (Lane 2's build; its cross-verification was HELD for a Sol-grade lane and is now due):
  `alpha-program-archive/workspace/STAGE8_TASK5_LICENSED_CONDITIONAL_CHAIN_LANE2_V002.md`
  SHA-256 `1069e4f442ebfd083944c7cf6df8ba04058c531846fa61e1b6452d7ba551a269`. Verify before reading.
- Authorities: the C_ret commissioning record (the disconnected-domain counterexample: reported A_loop = 0 while the true two-point modulus is 1), DoR-020 + A1, the threshold theorem (strict contraction iff |p_loc[R_hat_K]| < A_loop^-1), Q-448/Q-450 (EQ6 and C_ret independent), Q-455/Q-456 (the finite-package absences — the chain must NOT presuppose the unbuilt objects).
- Custody: builder never verifies own work; this is the review of record for chain V002.

TASK — verdict-grade, PASS/KILL per item:
K1. **C_ret's statement:** the stationary-return certificate exactly separates what the Q-448 counterexample broke — domain connectivity/interval-convexity or the absolute-continuity branch — and is nowhere implied by, or folded into, EQ6 (the M16/N7 layer discipline applies here too).
K2. **The twelve-step witness-to-number map:** each step's inputs, outputs, and authorization gates typed correctly; Steps 1–2 consistent with the Q-455/Q-456 state (Step 1 needs the finite package cert + adopted axiom; Step 2's regressions are its inputs, not its substitutes); Steps 8–12 escrowed exactly per DoR-020.
K3. **The conditional structure:** boundedness (Step 5) and return closure (Step 6) correctly tagged [EQ6]+C_ret; branch completeness (Step 7) correctly C_ret_SCOPE-conditional; no step consumes a certificate before the step that produces it.
K4. **Anti-tuning:** no clause of the chain chosen from a response, threshold, fixed-point, or end-test consequence; the counterexample regressions installed as permanent.
K5. **Two fresh attacks:** (a) a hidden-uniformity attack — does any step silently need a uniform-in-stage bound never certified? (b) a gate-bypass attack — construct a reading of the map that reaches Step 8 without C_ret_SCOPE; if one exists the typing is defective.

OUTPUT: one artifact, lane-tagged filename
`STAGE8_TASK5_CHAIN_V002_CROSS_CHECK_LANE1_V001.md`
with the per-step verdict table and final lines:
`CHAIN_V002 = CONFIRMED / DEFECTIVE (+items)` and `HELD_CROSS_CHECK = DISCHARGED`.
If the output filename already exists in the workspace, STOP and report — do not overwrite. Seal, mirror byte-identically to `alpha-program-archive/workspace/`, verify, report hashes, STOP. No register, plan, tracker, git, commit, or push action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants. If a fence blocks a structural result, flag MACHINERY-APPEAL and continue.
