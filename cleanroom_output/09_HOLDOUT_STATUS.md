# 09 — Holdout Status

**HOLDOUT_NEEDED.** No valid holdout exists in this package, and none can be
constructed inside it.

Per HOLDOUT_POLICY.md, a valid holdout requires an exhaustive eligible
registry, canonical serialization/deduplication, outcome masking, selection
via external future randomness or an independent custodian commitment,
prediction frozen before outcome access, and fail-closed contamination
handling. None of that infrastructure is present (WORK_PLAN Stage 11:
"no valid holdout supplied in this package"; the BID spec's own admission:
"The exact registry/query/cutoff fields are not yet set in this working
draft; V011 cannot receive SPEC-SEAL until they are").

Candidate inventory reviewed and rejected:

- **Composition-loop prediction** (K_square at Φ=π: characteristic
  polynomial, eight eigenvalues, kernel multiplicity, Tr[B²], Tr[B⁴],
  R_square): a genuinely preregistered forward *mathematical* consequence,
  fully specified and internally consistent — but unexecuted
  (`composition_loop_prediction_sealed = false`), self-described as
  target-aware, and in any case a mathematical consistency output, not the
  structure-sensitive *physical* observable the policy requires.
- **Transport-only "independent consequences"** (no intrinsic Pauli term,
  Dirac magnetic structure): permanently disqualified — known at adoption;
  same-pass reuse (Gate H).
- **τ_R/causal-cell relations**: conditional and already used in
  construction; not holdout-eligible.

No same-pass consistency check has been substituted. Stage 11 cannot be
reached in this run regardless, because Stages 3–5 exit BLOCKED.
