# 42 — Cycle 12 Specification: Gate-4 Public-Collapse Covector Ray v001

Frozen before execution. Executes the second half of BID Gate 4's pass
condition ("…and one public-collapse covector ray"): over ALL nonzero
readout functionals on the first-opening record complex, do the sealed
constraints force a **unique ray** (direction up to positive scale)?
**Scope**: theorem over the enumerated family on the canonical structure
forced by cycles 8–11; full Gate-4 authority requires the spec's reviews.

## Setting

The canonical first-opening object (forced in cycles 8–11): rooted star
K₁,₃, per-leaf record fibers with identity forms, U(1) transport, unit
weights. A public-collapse functional is represented per leaf by a
Hermitian weight matrix W_j, acting as φ(ρ) = Σ_j Tr(W_j ρ_j).

## Sealed constraints

- **V1 (publicness / gauge invariance):** φ is invariant under the
  cycle-8/9 gauge group (per-fiber U(1) rephasing) — W_j must commute with
  the transport action.
- **V2 (no output without a record):** the sealed conditional-write
  structure (public record change is Q_Σ-conditioned; the unwritten branch
  is public-silent) requires φ to vanish on every unwritten (charge-0
  sector) state: (W_j)₀₀ = 0.
- **V3 (naturality under complex automorphisms):** the star's S₃ leaf
  permutations are structure automorphisms; φ must be
  automorphism-covariant — the same W on every leaf.
- **V4 (positivity, nontriviality):** φ is a readout weight: W ⪰ 0, φ ≠ 0.
- **V5 (monoidal additivity):** on disjoint cells, φ adds (counting
  registrations across independent cells) — to be verified consistent for
  the survivor, not used as a selector.

## Sealed predictions

- **P1:** V1 forces W diagonal in the registration basis (Schur, as in
  cycle 10).
- **P2:** V2 forces the unwritten-sector weight to zero exactly.
- **P3:** V3 forces equal weights across leaves; with V4, the survivor set
  is {c·Σ_j |1⟩⟨1|_j : c > 0} — **exactly one ray**: the registration-
  counting functional.
- **P4:** the survivor is monoidally additive across disjoint cells
  (consistency check), and any deformation (off-diagonal element,
  unwritten-sector weight, unequal leaf weights) violates a named
  constraint — each exhibited numerically.

Together with cycle 8, P1–P4 complete both halves of Gate 4's pass
condition at the theorem-core level: one normalized differential
equivalence class (cycle 8) and one public-collapse covector ray (this
cycle).

## Failure conditions

- F1: any second surviving ray ⟹ report; no repair.
- F2: no comparison to any measured constant; `alpha_computed = false`.
