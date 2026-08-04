## PASTE 476 — CODEX LANE 1 (HIGH EFFORT) — [TASK 4b→5] CROSS-VERIFICATION OF THE CONSUMPTION RESULT + THE PUSHFORWARD-CERTIFICATE DERIVABILITY SWEEP

PREFLIGHT (verify before starting; report any failure and STOP):
- Register head: Q-397.
- Artifact under review (Lane 2's derivation): `alpha-program-archive/workspace/STAGE8_TASK4B_P_LOC_CONSUMPTION_PATH_LANE2_V001.md`
  SHA-256 `cacd317391759c1b1c6925c671be33cf4e91b7cccf4c3a529669dea6c18400fc`. Verify before reading.
- Authorities: your witness artifact `f0f8b09b…` (the Q-396 fiber the pushforward must be tested against), the seam audit `337769f4…`, the ratified defining artifacts of p_loc/Π_R,ind/B_ind as cited in the artifact under review (re-verify the citations), Q-391 through Q-397.
- Custody: adversarial verification; the next construction builds on this result.

TASK — PASS / KILL per item:
R1. **The reception claim.** Verify: p_loc receives the completed R5 operator (not a finite shadow) by its ratified definition — recompute the typing chain.
R2. **The underdetermination.** Verify no ratified clause fixes the coefficient functional — sweep independently (including any corpus artifact defining p_loc's evaluation semantics); a found clause = KILL and changes everything.
R3. **The refuted identification.** Verify the finite-to-completed identification refutation — recompute its witness.
R4. **THE FORWARD SWEEP:** the named certificate (the coefficient functional + the fiber pushforward). Determine: (a) is the coefficient functional derivable from ratified structure (sweep: the localization's defining properties, covariance, the R4-only unit seam, the DoR-008 falsifier applied to p_loc itself — any completion-dependence of the FIXED POINT would have finite consequences the falsifier could see?); (b) independent of (a): is the PUSHFORWARD of the Q-396 witness fiber through any admissible coefficient functional computable — in particular, does the witness direction ω̇_i μ_i[f(s)R_K + 2f₁(s)x♭⊗x♭] lie in a sector every admissible p_loc annihilates (then the fixed point is fiber-blind for ALL admissible functionals — the verdict discharges without fixing the functional)? Type what each determination consumes.
R5. **Falsifiers + one fresh attack.**

OUTPUT: one artifact, lane-tagged filename
`STAGE8_TASK4B_CONSUMPTION_VERIFICATION_AND_PUSHFORWARD_SWEEP_LANE1_V001.md`
with the verdict table R1–R5 and final lines:
`CONSUMPTION_RESULT = CONFIRMED / KILLED (+item)` and `PUSHFORWARD = ANNIHILATED_FOR_ALL_ADMISSIBLE (+proof) / DETECTED (+witness) / NEEDS (+the exact object)`.
Seal, mirror byte-identically to `alpha-program-archive/workspace/`, verify, report hashes, STOP. No register, plan, tracker, git, commit, or push action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No numeric evaluation; no registered verdict; no comparison to measured constants. If a fence blocks a structural result, flag MACHINERY-APPEAL and continue.
