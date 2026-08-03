## PASTE 430 — CODEX LANE 2 (HIGH EFFORT) — [TASK 4a] CROSS-REVIEW: THE MAP-1 EXTENSION THEOREM (Q-347)

PREFLIGHT (verify before starting; report any failure and STOP):
- Register head: Q-348.
- Artifact under review (Lane 1's build): `alpha-program-archive/workspace/STAGE8_TASK4A_MAP1_FULL_FAMILY_EXTENSION_LANE1_V001.md`
  SHA-256 `04002fb49fcf91a544544a798519cfe56017f42659a1eb6d6947f9defbc76a5a`. Verify before reading.
- Authorities: Q-313 build `ea8f4e9a…`, Q-315 squares `f886284c…`, DoR-015/V005 `7ecf04e9…`, DoR-016/V004 `69f4d93b…`, your own sufficiency arm `d9a507fc…` (Q-348).
- Custody: adversarial cross-review of the parallel arm. The comparison-square commission will be built ON this theorem — attack both the extension and the obstruction.

TASK — PASS / KILL per item:

Y1. **The rank-0/1 extension.** Verify uniqueness and each certificate (quotient compatibility, restriction naturality on rank-preserving arrows, reality, batching, zero-extension, agreement with Q-313 on Q_square and with Q-315's square).
Y2. **The classification (E3.1).** Verify that every no-selection scalar-character lift at a fixed stage is of the classified form s_G^λ, λ ∈ Hom(C_G, Z) — hunt for an unclassified construction (a lift NOT of this form would break the obstruction's generality).
Y3. **The automorphism obstruction.** Recompute: σ (a↔d) fixes Z_N; σ-action on the cycle lattice (c₁↔c₂, c₃→−c₃); naturality forcing λ(c₃) = 0; c₃ record-visible by V005's separation theorem. Verify the proof does NOT assume the unbuilt relative-label-to-edge functor (as claimed).
Y4. **The kernel/image disclosure (E4).** Verify the target-side witness (Ann(image) = ker(λ), rank ≥ rank(C_G)−1) and the dimension count (image ≤ 1 vs quotient rank ≥ 2).
Y5. **The escape hatch audit.** The obstruction binds maps depending only on the SINGLE consumed scalar Z_N. Your own Q-348 theorem shows the every-prefix trace FAMILY carries strictly more (all cellwise characters). Determine: does the obstruction survive against prefix-family-consuming constructions, or is the boundary an artifact of the single-scalar restriction? State exactly what the obstruction does and does not forbid for a prefix-family-domain descent — this is the load-bearing item for the next commission.
Y6. **Regression + selection scan.** One-edge, S8-A triple, reality, zero-extension rerun; no member/orientation/edge selection anywhere; the residual Hom(C_G,Z) family honestly retained.
Y7. **One fresh attack** of your own on either the extension or the obstruction.

OUTPUT: one artifact, lane-tagged filename
`STAGE8_TASK4A_MAP1_EXTENSION_CROSS_REVIEW_LANE2_V001.md`
with the verdict table Y1–Y7, computations, and final lines:
`EXTENSION_RANK01 = CONFIRMED / KILLED`, `RANK2_OBSTRUCTION = CONFIRMED / KILLED`, `PREFIX_FAMILY_ESCAPE = OPEN / CLOSED (+why)`.
Seal (.seal.sha256 sidecar), mirror both files byte-identically to `alpha-program-archive/workspace/`, verify, report hashes, then STOP. No register, plan, tracker, git, commit, or push action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No evaluation of alpha, K_*, or roots; no comparison to measured constants. Structural mathematics of declared objects is permitted; if a fence blocks a structural result, flag MACHINERY-APPEAL and continue.
