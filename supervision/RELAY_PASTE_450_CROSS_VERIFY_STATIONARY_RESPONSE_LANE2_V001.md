## PASTE 450 — CODEX LANE 2 (HIGH EFFORT) — [TASK 4b] CROSS-VERIFICATION: THE STATIONARY RESPONSE COMPUTATION

PREFLIGHT (verify before starting; report any failure and STOP):
- Register head: Q-368.
- Artifact under review (Lane 1's computation): `alpha-program-archive/workspace/STAGE8_TASK4B_STATIONARY_RESPONSE_COMPUTATION_LANE1_V001.md`
  SHA-256 `be570c182ef875b557395b62c382ee875420ac0462e2efb5774e9600f794b27a`. Verify before reading.
- You built the ratified square (V004 `abf6d366…`) — you are the natural auditor of how it was loaded. Authorities: DoR-017 (decision file), the derive standard `a9b733c7…`, descent V003 `a03e8363…`, DoR-016/V004 `69f4d93b…`, Q-367/368.
- Custody: adversarial cross-verification. The p-verdict will be computed against this structure — an error here propagates into the program's deciding question.

TASK — PASS / KILL per item:

X1. **The stationary system assembly (W1).** Recompute the stationary blocks, the complement inverse, the Schur reduction, and the retarded extraction with the N-member installed; verify each member certificate genuinely passes at each stage (covariance, reality, batching, restriction) — re-run, don't trust the ledger.
X2. **The finite stages (W2).** Recompute the reciprocal-loop and S8-A computations and the general-stage statement; verify the finite-shadow reproduction (Q-243/Q-279 tables) exactly.
X3. **The zero theorem.** Verify FINITE_ACTIVE_REFERENCE_RETARDED_BLOCK = 0, p-free and ν-free, at every finite stage with probes — attack it: find any stage/probe combination where the member's presence makes it nonzero.
X4. **The p/ν appearance map (W3).** Verify: p enters only through the base restrictions; the member carries no declared p/rank dependence; the homogeneity statement about ν and the jets. Attack the LOCALIZED_NOT_DECIDED typing in both directions — is anything already decidable that the artifact left open, or anything claimed localized that actually spreads?
X5. **The instantiation boundary.** Verify EXACT_COMPONENT_EVALUATION = TYPE-U is correctly typed: sweep the ratified stack (the R1 Gen structure, the divergence datum δ_div, the draft) — does anything ratified ALREADY generate the member's stationary jets? A found generator would collapse the boundary and is the most valuable possible finding.
X6. **The tag ledger.** Every member-sensitive/member-independent tag audited; any untagged result = KILL.
X7. **One fresh attack** of your own on the computed structure.

OUTPUT: one artifact, lane-tagged filename
`STAGE8_TASK4B_STATIONARY_RESPONSE_CROSS_VERIFICATION_LANE2_V001.md`
with the verdict table X1–X7 and final lines:
`RESPONSE_STRUCTURE = CONFIRMED / KILLED (+item)` and `JET_BOUNDARY = CONFIRMED_TYPE_U / GENERATOR_FOUND (+where)`.
Seal (.seal.sha256 sidecar), mirror both files byte-identically to `alpha-program-archive/workspace/`, verify, report hashes, then STOP. No register, plan, tracker, git, commit, or push action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No evaluation of alpha, K_*, roots, or any response value; no p-verdict; no comparison to measured constants. Structural/symbolic mathematics of declared objects is permitted; if a fence blocks a structural result, flag MACHINERY-APPEAL and continue.
