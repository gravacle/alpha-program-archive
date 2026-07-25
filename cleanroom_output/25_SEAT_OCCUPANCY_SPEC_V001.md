# 25 — Cycle 6 Specification: g_N Seat-Occupancy Derivation v001

Frozen before adjudication. Decides the cycle-4 g_N fork (action marker πħ
vs FS budget πħ/2 as the phase-coupling normalization) by **type-matching
derivation**, not preference. Blindness: the adjudicating lane is not told
what either verdict implies for any downstream quantity or family.

## The question

In the elimination (cycles 3/5), g_N enters as the coefficient of the
registration projector in the connected generator: V = g_N·(n_a⊗N_1 +
n_b⊗N_2). The cycle-4 enumeration left two sealed candidates for its
normalization over the record interval, with no numeric selector:
πħ (marker) vs πħ/2 (budget). Question: **which sealed object has the same
TYPE as the seat, and does the package's own text fix the typing?**

## Proposed derivation (to be adversarially tested, not assumed)

1. **The seat's type is fixed by the elimination formalism itself**:
   second-order elimination consumes generator (Hamiltonian) matrix
   elements. The seat is therefore a *generator-coefficient* slot — the
   coefficient of N_i (≡ P₁) in a generator.
2. **The package seals exactly one generator-coefficient normalization for
   a registration projector**: the binary closure gate's H = Δ·P₁ with
   |Δ|·τ_orth/ħ = π at balanced calibration — i.e., generator coefficient ×
   interval = **πħ (the marker)**.
3. **The budget is sealed with a different type**: the onset gate defines
   J_FS,rel := ∫_cell dτ ΔH_W(τ) — an integrated *state-uncertainty/path-
   length functional*, not a generator coefficient. The bridge gate seals
   the factor-2 relation between the two as uncertainty = gap/2 at p = 1/2
   ("projective speed, set by the generator uncertainty, vs the gap
   between the two generator eigenvalues").
4. Therefore the marker occupies the generator seat; the budget occupies
   the path-length role, which the elimination does not consume.
   **Proposed verdict: MARKER_OCCUPIES — g_N·T_R = πħ.**

## Adjudication protocol

- A fresh-context lane reads ONLY: the binary closure gate, the onset
  gate, the bridge gate, and OUTPUT/16–18 (how the seat enters the
  elimination). It receives the proposed derivation and must first
  STRENGTHEN it, then attack it (is there a sealed reading in which the
  physical coupling seat is uncertainty-typed? does the marker→rate
  conversion over T_R hold, i.e., is τ_orth's physical realization the
  cell interval? is the typing itself an unsealed convention?).
- Allowed verdicts: MARKER_OCCUPIES | BUDGET_OCCUPIES |
  TYPE_UNDECIDABLE_IN_PACKAGE.
- The lane may not consider what any verdict implies downstream, and no
  measured constant may be used (standing G3).

## Consequence rule (mechanical, declared in advance)

- MARKER_OCCUPIES → g_N = πħ/T_R; the cycle-5 family reduces 4 → 2:
  ρ ∈ {3/16, 3√2/16}. (Noted here for the record; the LANE is not shown
  this section — enforced by giving the lane only the files listed above.)
- BUDGET_OCCUPIES → g_N = (πħ/2)/T_R; family reduces 4 → 2:
  ρ ∈ {3/64, 3√2/64}.
- TYPE_UNDECIDABLE → fork stands; family remains 4; the fork is added to
  NEEDS_THEORY_DECISION as a numbered entry.

## Failure conditions

- F1: verdict reached by downstream consequence → void, rerun blind.
- F2: any use of a measured constant → void.
- `alpha_computed = false` regardless of outcome.
