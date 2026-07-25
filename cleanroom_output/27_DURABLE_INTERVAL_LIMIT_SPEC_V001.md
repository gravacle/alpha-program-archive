# 27 — Cycle 7 Specification: The L→∞ Durable-Interval Limit v001

Frozen before execution. Tests the spec's own Durable-Record Interval pass
conditions (existence of τ_R(L); uniqueness of least positive solution;
nondegeneracy; certified L→∞ limit) at the dimensionless level, in the
three incidence regimes the sealed structure admits. Definition declared
here (a spec choice, disclosed): **τ_R(L) = the first time at which every
cell's ready-state overlap vanishes simultaneously** — the natural L-cell
lift of the sealed single-cell first-orthogonality definition, with each
cell's overlap o_j(t) = [(1 + cos(ω_j t))/2]² and frequencies ω_j the
distinct positive eigenvalues of the regime's incidence operator (hop μ = 1
units).

## The three regimes

- **R1 (disjoint cells):** monoidal composition; every cell carries the
  sealed conditioned spectrum {−√2, 0, +√2}.
- **R2 (unbounded incidence):** all L cells on one shared root — star
  K_{1,L}; conditioned spectrum {−√L, 0, +√L}.
- **R3 (bounded-degree chain):** L cells with nearest-neighbor incidence —
  path P_{L+1} adjacency; eigenvalues 2·cos(kπ/(L+2)). Note P₃ (L = 2)
  reproduces the sealed star exactly ({−√2, 0, √2}) — the chain regime
  *contains* the sealed case.

## Sealed predictions

- **P1 (R1):** τ_R(L) = π/√2 exactly, for every L — all cells share one
  frequency, so simultaneous orthogonality occurs at the single-cell
  interval. Certified limit exists trivially: τ_R(∞) = π/√2.
- **P2 (R2):** τ_R(L) = π/√L → 0: the interval degenerates. **Unbounded
  incidence is excluded from durable cellulations** — the DC3 locality
  clause is load-bearing, not decorative.
- **P3 (R3) — declared TEST, no confident prediction** (cycle-5 lesson):
  for L ≥ 3 the chain's positive frequencies are generically
  incommensurate (e.g., P₅: golden-ratio pair φ, 1/φ), so **exact**
  simultaneous orthogonality may fail to exist at all. Sealed possible
  outcomes: (i) exact common zero exists (commensurate structure) — report
  it and its limit; (ii) exact common orthogonality fails for L ≥ 3 —
  then the durable interval exists only in **thresholded form**
  τ_δ(L) = first t with max_j o_j(t) < δ, and its (L, δ) behavior must be
  measured and reported. Outcome (ii) would echo the cycle-6-adjacent Q1
  finding (exactness is adopted, not derived) at the many-cell level.

## Failure conditions

- F1: no repair, re-scoping, or definitional change after results.
- F2: no comparison to any measured constant; `alpha_computed = false`.
