# 30 — Cycle 8 Specification: Gate-4 Differential Uniqueness Theorem v001

Frozen before execution. Executes the mathematical core of BID v011 Gate 4
("exactly one normalized differential equivalence class"), as the spec
itself demands: "Gate 4 must verify each step rather than recording this
paragraph as a passed result." **Scope declared**: the differential half
only (the public-collapse covector ray is deferred); this discharges the
theorem over the enumerated family — full Gate-4 *authority* additionally
requires Gates 1–3 and the spec's three-review seal process, not supplied
here.

## The admissible (hostile) family — the spec's own enumeration

Per-edge operators D_{a_e,b_e}: x ↦ i_t(a_e·U_e x) − i_s(b_e·x) with
independent complex coefficients (a_e, b_e) per edge; arbitrary
positive-definite Hilbert forms M_0, M_1; the continuum counterfamily
D_x = i_t(√(2−x)·U_e·) − i_s(√x·), 0 < x < 2 (which satisfies the
one-record norm for every x); residual phases; the sealed
orientation-extension involution (a_ē, b_ē) = (b_e, a_e).

## The sealed constraints (each from the spec's own text/sketch)

- **C1 (naturality/universality)** over universal-edge isomorphisms:
  coefficients cannot depend on which isomorphic copy of the universal
  edge carries them.
- **C2 (interior closure / chain property)**: the boundary of a composite
  path is supported on its endpoints only (the sealed cellular boundary
  ∂(e⊗ψ) = t⊗U_eψ − s⊗ψ and chain maps J₀/J₁/J₂; the elimination
  sketch's "closure a=b" step).
- **C3 (one-record normalization)**: ‖D_E e‖²_{M₀}/‖e‖²_{M₁} = 2.
- **C4 (equivalence group)**: per-vertex U(1) rephasing; form congruence
  (M₀, M₁ changes with matching adjoint redefinition); orientation
  bookkeeping via the sealed involution.

## Sealed predictions (hand-derived; script must verify or refute)

- **P1 (closure kills the continuum):** composing two edges leaves an
  interior residue (a − b)·m⊗U₁ψ; C2 ⟺ a_e = b_{e'} on every composable
  pair ⟹ on a connected complex all coefficients equal one constant
  a = b. The D_x family violates C2 for every x ≠ 1 (residue magnitude
  |√(2−x) − √x| > 0), and dies. x = 1 is the unique survivor of the
  continuum.
- **P2 (normalization + rephasing):** C3 then gives 2|a|² = 2 ⟹ |a| = 1;
  vertex rephasing removes edge phases on trees, so the equivalence class
  is **unit-modulus transport with residual phases only on loops** —
  i.e., the surviving class is exactly a compact gauge field (physical
  holonomy survives; magnitudes do not). Wilson-loop phases must be
  invariant under the equivalence group (verified), and gauge freedom must
  NOT be able to remove them.
- **P3 (forbidding lemma, incidence level):** no per-edge magnitude
  deformation survives C1–C3 — independent primitive edge/handle
  magnitudes are theorem-excluded *within this family*, converting the
  spec's axiomatic exclusion into a derived one at the differential level.
- **P4 (forms do not reopen the family):** the C3 ratio is invariant under
  form congruence, so M₀/M₁ freedom cannot restore any killed
  deformation.

Conclusion if P1–P4 hold: **exactly one normalized differential
equivalence class** — unit-weight covariant incidence (∂ with a = b = 1)
modulo gauge, with holonomy as the sole surviving (physical) freedom.

## Failure conditions

- F1: any surviving deformation not equivalent to a = b = 1 ⟹ Gate-4
  differential uniqueness FAILS over this family; report (stop-rule
  material), no repair.
- F2: no comparison to any measured constant; `alpha_computed = false`.
