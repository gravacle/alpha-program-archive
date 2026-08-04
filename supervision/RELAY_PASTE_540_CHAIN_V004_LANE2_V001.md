## PASTE 540 — CODEX LANE 2 (HIGH EFFORT) — [TASK 5] CHAIN V004: THE DEGENERATE BRANCH AND THE MODULUS-COMPATIBILITY CERTIFICATE

PREFLIGHT (verify before starting; report any failure and STOP):
- Register head: Q-462 (or current — recheck).
- Your chain V003 (`f2b0b786…`): the entrance gate and D_w certificate PASSED; two localized kills remain. Read the cross-check first:
  `alpha-program-archive/workspace/STAGE8_TASK5_CHAIN_V003_CROSS_CHECK_LANE1_V001.md`
  SHA-256 `c40cdb05fd45ae78c449fd0e77b0ecd6f9f6abd590cec2f0df24dae278146588`. Verify before reading — especially (X3-2) and the alternate-complete-metric attack.
- Custody: builder repairs; V004 returns to Lane 1. Bounded delta only — exactly two items.

TASK — produce chain V004:
P1. **The degenerate threshold branch (X3):** add to Step 10 the explicit pointwise branch for `A_loop = infinity` and `chi_K = 0` (and any other unlicensed edge of the case split — enumerate the FULL case lattice: A_loop in {0, (0,inf), inf} x chi_K in {0, nonzero} — every cell licensed or explicitly excluded with its reason). No numeric evaluation; symbolic typing only.
P2. **The modulus-compatibility certificate (X4):** a separate falsifiable certificate that Step 8's coordinate derivative computes Step 9's d_w Lipschitz modulus — state the exact condition (equivalence of d_w with the coordinate metric on D_w, or the chain rule that transports the derivative bound), its witness form, and the failure mode it forecloses (the alternate-complete-metric attack becomes a permanent regression).
P3. **Delta table vs V003 bounded to P1–P2; everything else verbatim.** Rerun: gate-bypass, hidden-uniformity, pending-cert laundering, disconnected-domain; one fresh attack of your choosing.

OUTPUT: one artifact, lane-tagged filename
`STAGE8_TASK5_LICENSED_CONDITIONAL_CHAIN_LANE2_V004.md`
with final lines: `CHAIN_V004 = READY_FOR_CROSS_CHECK`, `CASE_LATTICE = COMPLETE`, `MODULUS_CERT = ADDED`.
If the output filename already exists in the workspace, STOP and report — do not overwrite. Seal, mirror byte-identically to `alpha-program-archive/workspace/`, verify, report hashes, STOP. No register, plan, tracker, git, commit, or push action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants. If a fence blocks a structural result, flag MACHINERY-APPEAL and continue.
