# 36 — Cycle 10 Specification: Gate-3 Hilbert-Functor Uniqueness v001

Frozen before execution. Executes the mathematical core of BID Gate 3: over
the family of ALL positive-definite Hilbert forms (M₀ on the vertex space,
M₁ on the edge space), do the sealed constraints force a unique pair modulo
the declared overall-congruence equivalence? **Scope**: theorem over the
enumerated constraint set; full Gate-3 authority requires the spec's review
process. Cycle 8 showed forms *cannot reopen* killed deformations; this
cycle asks whether the forms are themselves *selected*.

## Sealed constraints

- **H1 (monoidal orthogonality):** disjoint cells/edges are orthogonal —
  forms are block-diagonal over fibers. (Carried conditionality: the
  monoidal-extensivity proof file is absent from the package — spec flag
  false; H1 is the spec's own declared monoidal requirement, adopted.)
- **H2 (naturality):** universal-edge isomorphisms force the same fiber
  form on every fiber.
- **H3 (transport invariance):** U_e is unitary for the fiber form; the
  per-axis transport group is U(1) acting with charges (0, 1) on the
  two-endpoint comparison fiber (cycle-9 result). Schur: the invariant
  positive forms are exactly diag(s₀, s₁) — one scale per charge sector.
- **H4 (the sealed calibration as form selector):** the bridge gate seals
  "exact orthogonality if and only if p = 1/2, θ = π." With form
  diag(s₀, s₁), the weighted overlap s₀p + s₁(1−p)e^{iθ} vanishes iff
  θ = π and p = s₁/(s₀+s₁). The sealed p = 1/2 therefore **forces
  s₀ = s₁**: the fiber form is proportional to the identity.
- **H5 (scale anchoring):** the sealed one-record norm ratio
  ‖D_E e‖²/‖e‖² = 2 pins the relative C₀/C₁ scale (a rescale M₀ → cM₀
  gives 2c); the overall scale is the declared congruence equivalence.

## Sealed predictions

- **P1:** invariant-form computation confirms Schur: the commutant of the
  transport set is diagonal — the admissible fiber forms are exactly
  diag(s₀, s₁); nothing off-diagonal survives.
- **P2:** the weighted-overlap zero condition is exactly
  p = s₁/(s₀+s₁), θ = π (exact algebra); hence sealed p = 1/2 ⟺ s₀ = s₁.
- **P3:** H1–H5 jointly force the **unique canonical pair** (fiber forms ∝
  identity, repeated; relative scale fixed by the ratio 2) modulo overall
  congruence. Consequence: the adjoint D^♯ = M₁⁻¹D†M₀ and the normalized
  transition operator B_ρ are canonical — cycle 8's conventions are
  *derived*, not chosen.
- **P4:** a deliberately skewed form (s₀ ≠ s₁) shifts the sealed
  orthogonality population away from 1/2 (numerically exhibited),
  demonstrating the selector has teeth.

## Failure conditions

- F1: any surviving form freedom beyond overall congruence ⟹ Gate-3
  uniqueness fails over this constraint set; report, no repair.
- F2: no comparison to any measured constant; `alpha_computed = false`.
