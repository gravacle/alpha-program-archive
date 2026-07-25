# 29 — Cycle 7 Result: The Durable Interval Is Exact Only Where Cells Don't Interact

Sealing order: spec 27 (36f394f0…) → script 28 (6f142d46…) → this result.
`alpha_computed = false`. No comparison to anything (G3).

## Outcomes vs sealed predictions

- **P1 CONFIRMED (disjoint):** τ_R(L) = π/√2 exactly for every L; the
  certified L→∞ limit exists trivially. The spec's pass conditions are
  satisfiable in full — but only in the monoidal (non-interacting) regime.
- **P2 CONFIRMED (unbounded incidence):** τ_R(L) = π/√L → 0 — the interval
  degenerates. Unbounded incidence is excluded from durable cellulations:
  **DC3 (incidence locality) is load-bearing**, not decorative.
- **P3 resolved to declared outcome (ii):** for the bounded-degree chain,
  exact simultaneous orthogonality **fails to exist for every tested
  L ≥ 3** (positive spectra are incommensurate — the L = 3 chain carries
  the golden pair φ, 1/φ; L = 2 reproduces the sealed π/√2 exactly). The
  durable interval exists only in **thresholded form** τ_δ(L), and τ_δ
  grows as δ shrinks (L = 5: 8.1 → 22.3 → 78.3 across δ = 10⁻¹ → 10⁻³).

## The structural finding

Three independent results now converge on one statement:

1. Cycle 2's blind lane: DC1's *exact* commutation is adopted — primitives
   support only finite-(T, δ) near-diagonality.
2. Cycle 7 (this): even the *ideal* record dynamics cannot achieve exact
   many-cell orthogonality on incident complexes — thresholds are forced by
   spectral incommensurability, not by imperfection.
3. The sealed single-cell exactness (π/√2) is the degenerate
   single-frequency case — the exception, not the rule.

**Durability is intrinsically approximate for interacting records.** The
spec's Durable-Record Interval pass condition ("a certified L→∞ limit"),
as stated exactly, is **unsatisfiable for incident cellulations** and must
be reformulated in thresholded form with pre-frozen (T, δ) quantifiers —
precisely the fail-closed requirement the cycle-2 lane identified for any
asymptotic DC1. This is reported as a finding against the spec's current
wording, not repaired here (F1).

Physical resonance, stated cautiously: records in nature are
decoherence-stabilized — approximate and asymptotic, never exact. The
framework, pushed honestly, has now *derived* that character rather than
assumed it: exact record orthogonality is a measure-zero idealization that
interaction destroys.

## Consequences for the roadmap

- SP08's durability item and Stage 10's L→∞ constructions must carry
  (T, δ) quantifiers, frozen in advance, or restrict to disjoint
  composition. The relational chain (πħ marker, τ_R = π/√2, m_*T_R = π)
  is untouched — it lives in the sealed single-cell/disjoint regime.
- The two-member family {3/16, 3√2/16} is unaffected (built from
  single-cell and pairwise sealed objects), but any future many-cell
  response construction inherits the thresholded-durability structure.
