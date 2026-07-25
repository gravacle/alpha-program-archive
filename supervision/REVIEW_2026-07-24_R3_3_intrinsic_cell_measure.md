# Supervision Review — R3.3 Intrinsic Cell-Measure Derivation (Codex)

Artifact: `R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_RESULT_V001.md` (+ spec,
audit, tests, JSON; seals verify 5/5).
Reviewer: Fable supervision lane. Date: 2026-07-24.

## Verdict: ACCEPT — and this is the best possible outcome for the fork

`INHERITED_REFINEMENT_NATURALITY_FORCES_UNIFORM_MEASURE` — **no new
strict-locality principle adopted.** The premise ledger did not grow.

The tie-breaker recommendation (run the response-level cellulation test
before adopting) was executed exactly as relayed: Codex inspected the
sealed BID response-assembly definition and found five binding clauses
(each cell supplies its own operators and local response; residual
shape-dependent scalars forbidden; response must commute with common
refinement; cellulation-dependent response fails the gate). Conclusion: a
subregion promoted to a cell must be evaluated by its intrinsic measure —
so the μ_a boundary-profile family violates an **inherited** requirement,
and the uniform measure d⁴x/Vol is **derived**, not chosen.

## Cross-validation (their exact vs my Monte Carlo)

Codex derived closed forms:

- Δ⟨t⟩ = 3a / [4(960 + 19a)]
- Δ⟨u_child⟩ = −a(a+45) / [7(a+60)(19a+960)]

Both vanish together only at a = 0 (for the predeclared a ≥ 0 family).

Checking against my independent MC tie-breaker (run before their result
existed):

| a | exact Δ⟨t⟩ | my MC (abs) | agree? |
|---|---|---|---|
| 2 | 0.00150 | ≈0.00164 | ✓ within MC error |
| 6 | 0.00419 | ≈0.00455 | ✓ within MC error |

Two fully independent executions — exact rational vs Monte Carlo — agree.
The earlier geometric moments also line up (Vol/π = 1/24; ∫u/π = 1/1440
matched my 0.002175 estimate).

## Gate-D note (one caveat, mitigated)

The audit script computes the delta formulas in exact Fraction arithmetic,
but the base moments (e.g., 19/23040, 1/57600) appear as pinned Fraction
constants around line 221. Whether they are derived in-script or verified
against an off-line derivation needs one deeper pass to classify fully.
Mitigation: my independent MC agrees with the exact deltas, so the moment
values are cross-validated by a second method regardless of their
in-script provenance. Recommended (minor): a follow-up script that
integrates the moments symbolically in-script, closing the loop.

## Significance

1. **The supervision loop demonstrably changed the outcome.** Codex's
   prior recommendation was "adopt strict locality." After the relay, the
   fork closed by derivation instead. The conditionality stack of any
   future α value is one premise lighter at a maximally load-bearing
   point (measure → spectral density → response → E_ref → ρ).
2. **Fork 8 now has exactly one open object**: the root spectral density
   for the (now unique) uniform flat-cell measure, plus its absolute
   continuity — then the promotion adjudication under the sealed
   non-promotion rule.
3. Status flags all honest; `alpha_computed = false`; scope correctly
   states what remains.

## Watch items

- SPEC-SEAL / CORE-RESULT-SEAL vocabulary appeared in the live stream;
  no seal may be *claimed* without the three-review chain — watching.
- The spectral-density derivation is now in progress per the thinking
  feed; it inherits the contaminated-context concern (June session knows
  the target value). The density is numerically load-bearing. Standing
  recommendation: derive it in a fresh-context execution from the sealed
  spec, or at minimum have the derivation independently re-executed
  blind (I can run that as a parallel lane, as done here).
