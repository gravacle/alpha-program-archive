# 22 — Cycle 5 Specification: Full-Kernel Elimination (h_s Fork Decider) v001

Frozen before execution. Decides the cycle-4 mediator fork (hop μ vs gap
m_* = √2·μ) by computation, per the declared decider in OUTPUT/21: repeat
the cycle-3 elimination with the mediator carrying the **sealed full-kernel
record structure** instead of the minimal two-site structure.

## Model (the sealed conditioned structure)

Mediator: one source particle on the sealed conditioned star operator —
3-dimensional, characteristic polynomial λ(λ²−2), hop coefficient μ —
i.e., H_med = μ·B with B = [[0,1,1],[1,0,0],[1,0,0]] in the (root, leaf-a,
leaf-b) basis. Sealed spectrum μ·{−√2, 0, +√2}; ground state
(−√2, 1, 1)/2. This is the structure whose sealed consequences are
τ_R = π/√2 and the Schur pole gap m_* = √2·μ. Carried caveat (disclosed,
not repaired): the conditioning premise (A24) is itself unexecuted in the
package; this cycle inherits that scope.

Records: two cells at the two leaf sites (the incident pair), phase-type
coupling only (per the sealed cycle-3 selection rule):
V = g_N·(n_a ⊗ N_1 + n_b ⊗ N_2), with n_a, n_b the leaf occupations.
Bare record rates zero. No writing-type coupling is included: cycle 3
proved it contributes nothing durable, and this cycle tests the mediator
scale, not the selection rule.

## Method

1. Second-order elimination onto the mediator ground state (SW), summing
   over BOTH sealed intermediate levels (0 and +√2, denominators √2μ and
   2√2μ).
2. Exact cross-check: the full Hamiltonian is block-diagonal in the record
   pattern (phase coupling commutes with N_i); per pattern (r₁, r₂) the
   3×3 source block is μB + g_N·diag(0, r₁, r₂); λ_c^exact =
   E(11) − E(01) − E(10) + E(00) from exact ground energies; must converge
   to the SW result at O(g_N²/μ²).

## Sealed predictions (hand-derived during spec design; script must
independently verify or refute)

- **P1 (fork resolution):** both intermediate denominators are multiples of
  √2·μ, so the induced λ_c carries the **gap m_* = √2μ** as its exact
  denominator scale — the hop μ appears only through m_*. The h_s fork
  resolves to the GAP, by computation.
- **P2 (new structural coefficient):** λ_c = **(3/16)·g_N²/m_***.
  Hand-derivation: level-0 channel gives +[(1/(2√2))²·2]·g_N²/(√2μ)
  = +(1/4)·g_N²/(√2μ) connected; level-+√2 channel gives
  −(1/16)·2·g_N²/(2·2√2μ)… net (1/4 − 1/16) = 3/16 on 1/(√2μ) = 1/m_*.
  The two sealed intermediate levels contribute with opposite connected
  signs; both must appear in the script's decomposition.
- **P3:** exact diagonalization converges to SW within O(g_N²/μ²).
- **P4 (table update, mechanical):** with (c, h_s) → (3/16, m_*) decided,
  the cycle-4 surviving family reduces 6 → 4:
  ρ = (3/16)·g_N²/(m_*·E_ref) over the two remaining forks
  (g_N ∈ {πħ, πħ/2}/T_R; E_ref ∈ {π, π/√2}/T_R), giving
  **{3/64, 3√2/64, 3/16, 3√2/16}** unflagged. No member may be compared to
  anything (G3 of spec 19 continues to bind).

## Failure conditions

- F1: SW vs exact disagreement beyond declared accuracy → scheme
  dependence; report, do not prefer.
- F2: if the level sum does not factor onto a single m_*-proportional
  denominator, report the actual two-scale form; no forcing into the fork.
- F3: no comparison of any number to any measured constant;
  `alpha_computed = false` regardless of outcome.
