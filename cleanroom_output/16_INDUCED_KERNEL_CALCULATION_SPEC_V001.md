# 16 — Induced-Kernel Calculation Specification (Cycle 3) v001

Frozen before execution. Computes the named interface object of OUTPUT/15:
the effective record-only connected generator induced by eliminating the
source sector from a minimal faithful QFC-scoped primitive action, then
filtered by DCC (DC1–DC4). No measured constant may appear anywhere; all
scales are formal symbols of the model.

## The minimal faithful model (an H_K instance)

Carrier: two record cells (qubits R_1, R_2; registration observables
N_i = |1⟩⟨1|_i; writing quadratures X_i = |0⟩⟨1|_i + |1⟩⟨0|_i) and one
spinless fermionic source mode per cell site. One source particle (the
minimal mediator). H = H_K form Σ a_i†a_j ⊗ b_ij with:

- b_12 = b_21 = −h_s · I  (source-orbital hop; pure source, DC1-invisible)
- b_ii = g_N · N_i + g_X · X_i  (registration-side coupling of cell i:
  a phase-type component — source presence shifts the registered cell's
  action-phase rate — and a writing-type component — source presence drives
  the writing quadrature)

Both coupling types are included because the primitive registration-writing
dynamics must contain X-type terms (records cannot be written without
content-changing action — Q3's finding that even a single-cell quadrature
violates DC1 in the primitive scope), while phase-type terms are the
DC1-compatible class. Bare record rates are set to zero to isolate the
induced kernel. h_s > 0; source ground state is the bonding orbital.

## The calculation (both methods; agreement required)

1. **Second-order elimination (Schrieffer–Wolff / standard second-order
   perturbation theory)**: project onto the source ground state; compute
   the effective record-sector generator to O(g²).
2. **Exact cross-check**: full diagonalization of the 8-dimensional
   one-source-sector Hamiltonian at small g/h_s; compare the record-sector
   effective couplings extracted from exact spectra/eigenvectors with
   method 1 (agreement to the expected O(g⁴/h_s³) accuracy).

Then apply the **DC1 filter**: project the induced kernel onto the
DC1-admissible (registration-diagonal) algebra; the connected diagonal
component defines λ_c via the induced N_1N_2 coefficient.

## Sealed predictions

- **P1**: the elimination induces a nonzero connected record–record kernel
  for generic nonzero couplings (two-step, h_s-mediated).
- **P2 (the asymmetry)**: the g_X (writing-type) component induces only
  DC1-inadmissible connected terms (X_1X_2-type; filtered to zero); the
  g_N (phase-type) component induces the DC1-admissible connected term.
  Durable cross-talk is sourced exclusively by the phase-type coupling.
- **P3**: at leading order λ_c = c · g_N²/h_s with c a **pure structural
  number** independent of all model parameters. Hand-derivation during
  spec design suggests c = 1/4 (bonding/antibonding splitting 2h_s;
  matrix element (g_N/2)(N_1−N_2); (N_i)² = N_i); the script must verify
  or refute this independently by both methods.
- **P4**: λ_c is **scale-relative** (a ratio to model scales g_N, h_s that
  trace to the still-free Families A/C). No absolute magnitude appears —
  consistent with the angles-not-amplitudes finding. What the calculation
  fixes is the form, the selection asymmetry (P2), and the structural
  coefficient c.

## Failure conditions (fail-closed, declared in advance)

- **F1**: if all connected induced terms are DC1-filtered to zero even with
  g_N ≠ 0, the mediated route is dead at second order — report; no
  higher-order rescue may be added in this cycle.
- **F2**: if the two methods disagree on the surviving coefficient beyond
  their stated accuracy, the result is scheme-dependent — report as such;
  neither method may be preferred post hoc.
- No coefficient, term, or coupling may be added or re-scoped after
  results are seen. `alpha_computed = false` regardless of outcome: λ_c/E
  ratios are model-structural results, not couplings of nature.
