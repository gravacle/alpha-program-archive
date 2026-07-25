# 24 — Cycle 5 Result: The Mediator Fork Is Decided; One Sealed Prediction Refuted

Sealing order: spec 22 (9fdceb82…) → script 23 (9814fb31…; an earlier
sealed hash of the same script with a misleading terminal summary line was
superseded before manifest entry — the P3 detail block was always honest;
the summary line was corrected to match it) → this result.
`alpha_computed = false`. No value compared to anything (G3).

## Fork resolution (P1 — CONFIRMED)

In the sealed conditioned-star mediator (spectrum μ·{−√2, 0, +√2}), both
second-order channels carry denominators that are integer multiples of the
**gap m_* = √2·μ** (√2μ and 2√2μ). The hop coefficient μ enters only
through m_*. **The cycle-4 h_s fork resolves to the GAP — by computation,
not choice.**

## New structural coefficient (P2 — CONFIRMED)

**λ_c = (3/16) · g_N²/m_*** — the two sealed intermediate levels contribute
with opposite connected signs (+1/4 and −1/16 on 1/m_*), both required.
The minimal model's 1/4 was the two-site artifact; the full sealed record
structure gives 3/16.

## Honest failure (P3 — REFUTED AS SEALED)

The sealed spec predicted exact-vs-SW convergence at O(g²/μ²). **Measured
convergence is cleanly O(g)** (orders 0.994, 0.997, 0.999): the three-level
mediator's ground state has asymmetric occupations (root 1/2, leaves 1/4),
so no odd-order cancellation occurs and a genuine third-order channel
exists. The spec is sealed and stands refuted on this point; no repair.
**Substance preserved by measurement**: Richardson extrapolation of the
exact data gives c(g→0) = 0.187498 → the leading coefficient **3/16
stands**, and with it P1. Consequence for the record: any future use of
λ_c at finite coupling must carry the O(g³) correction term; the
"structural coefficient" is a leading-order object.

## Reduced surviving family (P4 — CONFIRMED, mechanical)

With (c, h_s) → (3/16, m_*) decided by computation, the cycle-4 family
reduces **6 → 4**:

ρ = (3/16)·g_N²/(m_*·E_ref) ∈ **{3/64, 3√2/64, 3/16, 3√2/16}**
(numerically 0.046875, 0.066291, 0.187500, 0.265165).

Remaining forks, unchanged in character:
- **g_N** (marker πħ vs budget πħ/2, factor 2) — decider: seat-occupancy
  derivation from the full action's phase-coupling term.
- **E_ref** (E_* vs μ, factor √2) — decider: Stage-10 Thomson/matching
  rule; cannot be legitimately decided before the response object exists.

Per the standing guardrails, no member of the family is compared to any
measured value, and none may be preferred for its numerical consequence.
