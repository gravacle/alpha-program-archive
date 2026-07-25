# 38 — Cycle 10 Result: Gate-3 Hilbert-Functor Uniqueness — The Forms Are Derived

Sealing order: spec 36 (953e875b…) → script 37 (a32a4812…; one instrument
repair before sealing — a double-conjugation bug in the invariance
sandwich; disclosed, claim untouched) → this result.
`alpha_computed = false`. No comparison (G3).

## Theorem (P1–P4 confirmed)

Over the family of ALL positive-definite Hilbert-form pairs (M₀, M₁), the
sealed constraints force a **unique canonical pair modulo overall
congruence**:

1. **Schur (P1):** transport invariance under the cycle-9 U(1) action
   leaves exactly the sector-diagonal forms diag(s₀, s₁); nothing
   off-diagonal survives.
2. **The sealed calibration is a form selector (P2 — the load-bearing
   step):** the weighted overlap s₀p + s₁(1−p)e^{iθ} vanishes exactly at
   θ = π, p = s₁/(s₀+s₁). The bridge gate's sealed "orthogonality iff
   p = 1/2" therefore forces **s₀ = s₁** — the fiber form is proportional
   to the identity. A skewed form has visible consequences (P4: diag(3,1)
   moves the orthogonality population to p = 1/4, contradicting the sealed
   identity) — the selector has teeth.
3. **Assembly (P3):** monoidal orthogonality (block-diagonality) +
   naturality (one repeated fiber form) + P2 (∝ identity) + the sealed
   one-record ratio 2 (pinning the relative C₀/C₁ scale) leave **no form
   freedom** beyond overall congruence.

**Consequence:** the adjoint D^♯ = M₁⁻¹D†M₀ and the normalized transition
operator B_ρ are **canonical** — the conventions cycle 8 worked in are now
derived, not chosen. Gates 1, 3, and 4 interlock: group forced (U(1)),
forms forced (identity fibers), differential class forced (unit-weight
transport, holonomy free).

## Conditionality (carried)

H1 rests on the spec's monoidal requirement whose extensivity proof file
is absent from the package (flag false — inherited); the calibration
selector inherits the bridge gate's conditional base (V156/H1–H6,
imported character and winding); the fiber typing inherits the cycle-9
carrier layers. Full Gate-3 authority requires the spec's review process.
Within the declared bounds: theorem.
