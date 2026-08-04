## PASTE 486 — CODEX LANE 2 (HIGH EFFORT) — [TASK 5 / R4] CROSS-VERIFY THE PARTIAL BUILD; CONSTRUCT THE KERNEL REALIZATION AND SYMBOL CALCULUS

PREFLIGHT (verify before starting; report any failure and STOP):
- Register head: Q-407.
- Artifact under review (Lane 1's partial build): `alpha-program-archive/workspace/STAGE8_TASK5_R4_LOCAL_SYMBOL_MAP_BUILD_LANE1_V001.md`
  SHA-256 `bae34116c4d6792b5e39b913addeeff1650989660d89ba01bf5de62ec2d9aa50`. Verify before reading.
- Authorities: the ledger `c35ef846…` (the R4 LM-1/LM-2 route), metric V005 `2a379098…`, DoR-016/V004 `69f4d93b…`, square V004 `abf6d366…`, Q-406/407.
- Custody: verify, then build; derivation-first; authored steps at the choice table; p, ν, χ_K, T symbolic; no member selected.

TASK:
B1. **Cross-verify the partial build:** the completed current seam; the profile Banach topology; the (χ_K,T) parameterization and its formula p_(χ,T)[H_x] = f(‖x‖²)χ_K + 2f₁(‖x‖²)⟨x,Tx⟩; the coordinate counts (1 loop / 2 S8-A pre-stabilizer) — recompute each; verify no member selection hides in the parameterization.
B2. **CONSTRUCT the blocked object:** COMPLETED_CONSERVED_CURRENT_TO_LOCAL_FIELD_KERNEL_REALIZATION_AND_SYMBOL_CALCULUS — the map from completed conserved currents to local field kernels with its symbol calculus (the physical long-wavelength Maxwell map), per the ledger's LM-2 clauses (spectral/long-wavelength symbol, Ward/contact split, kernel certificates, R4 units, covariance/reality/restriction/batching). Derivation-first; disclosed authored steps only where forced; a proven obstruction is a full success — do not force.
B3. **On whatever B2 yields:** compute p_loc on the rank-one profiles through the realized kernel — does the physical map CONSTRAIN the (χ_K, T) family (a derived relation among the coordinates, a normalization, a bound)? Any derived constraint shrinks the R2 ratification fiber — report exactly; select nothing.
B4. **Falsifiers:** finite restrictions; standing regressions; anti-tuning ledger.

OUTPUT: one artifact, lane-tagged filename
`STAGE8_TASK5_R4_KERNEL_REALIZATION_AND_SYMBOL_CALCULUS_LANE2_V001.md`
with a lead-result block (`PARTIAL_BUILD = CONFIRMED/KILLED (+item)`; `KERNEL_REALIZATION = BUILT / BUILT_WITH_AUTHORED (+items) / OBSTRUCTED (+exact)`; `FIBER_CONSTRAINT = <derived relations on (chi_K,T), if any>`), the register-sweep list, and the B1–B4 chain. Seal, mirror byte-identically to `alpha-program-archive/workspace/`, verify, report hashes, STOP. No register, plan, tracker, git, commit, or push action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No numeric evaluation; no registered verdict; no comparison to measured constants. If a fence blocks a structural result, flag MACHINERY-APPEAL and continue.
