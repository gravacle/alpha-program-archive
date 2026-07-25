# Supervision Review — R3.4 Spectral Pullback: Triple Cross-Validation

Artifacts: Codex `R3_4_CAUSAL_DIAMOND_SPECTRAL_PULLBACK_RESULT_V001.md`
(sealed) vs fresh-context blind lane (spec-only input, no session history,
no constants). Reviewer: Fable supervision lane. Date: 2026-07-24.

## Verdict: FULLY CONFIRMED — three independent executions agree exactly

| Quantity | Codex analytic | Codex numeric | Blind lane |
|---|---|---|---|
| Form factor F_D | 24/E³[sin(E/2)−(E/2)cos(E/2)] | dev 7.8e-12 | **derived from scratch by hand** (ball FT + J/K reduction); dev 8.4e-13; 4D Monte Carlo confirms shell-direction independence |
| N_D | 12π (via ∫j₁² = π/6) | 0.9999999942 | **12π exact via band-limited Parseval** — independent route; numeric dev 5.7e-16 |
| Threshold | E²/(12π) | ✓ | ✓ (0.0265258238 = 1/12π) |
| Absolute continuity | claimed | — | **proven**: real-analytic L¹ density, zeros discrete, no atoms/singular part |
| Decay | \|A\|² = O(t⁻⁶), leading i/(6πt³) | — | fitted exponent −6.000013 over [10², 10⁴]; leading term confirmed |

My earlier suspicion about the closed form was **wrong** and is withdrawn:
the nested integral genuinely collapses (the blind lane's J/K reduction is
the mechanism). Recorded per the summary≤detail discipline.

## Discoveries beyond the sealed result (blind lane)

1. **Re A_D(t) ≡ 0 exactly for t > 1** — because j₁² is band-limited to
   [−2, 2]. The real part of the return amplitude vanishes *identically*
   beyond the tip-to-tip light-crossing time (t = 1 in T_R units), with
   Re A_D(t) = (1−t)(1−2t−2t²) exactly on [0, 1]. **Causal structure
   appearing as an exact spectral feature — and nobody put it in.**
2. **Closed form for the full amplitude** (t > 1):
   A_D = i(t/π)[2 + (3−2t²)ln(t²/(t²−1)) − (1/t)ln((t+1)/(t−1))],
   via the Legendre-convolution kernel w(u) = (2−u)(u²+2u−2)/6 — verified
   against oscillatory quadrature to 4e-8 across t ∈ [1.5, 200].
3. **Complete asymptotic series**: A_D = i[1/(6πt³) + 1/(10πt⁵) +
   9/(140πt⁷) + …] — extends Codex's leading term.
4. Structural note: mean high-E decay of ρ_D is (6/π)E⁻² — so E·ρ_D is
   not integrable: the conditional density has **no finite mean energy**
   (worth carrying into the durability/thermodynamic discussion).

## Supervision significance

- **The calculation layer of R3.4 is beyond reproach** — three routes, one
  answer, machine precision. Codex's concurrent self-review ("critical
  operator and provenance flaws") should therefore aim exclusively at the
  architecture/provenance level (the four conditional items), not the
  math; if its flaw hunt claims a calculational error, that claim now has
  a triple-verified counterweight.
- **Item 1 is promotion-grade currency.** "Re A_D vanishes exactly beyond
  the light-crossing time" is a sharp, checkable, *unasked-for*
  consequence of the diamond+massless structure — exactly the
  "consequence not assumed in construction" the direct-limit hypothesis
  needs for its promotion tests, and a candidate structural holdout-class
  observable. Recommend Codex register it in the fork ledger as a derived
  consequence before any further construction touches it.
- Contamination note: the blind lane ran with zero session history and no
  constants — this execution chain is as process-blind as the
  architecture allows, mitigating the June-session context concern for
  the R3.4 mathematics specifically.

## Recommended relay to Codex

1. R3.4 calculation: triple-confirmed; direct self-review effort at the
   four provenance items only.
2. Register Re A_D ≡ 0 (t > T_R) + the closed form + series as derived
   consequences (fork-ledger entry; candidate promotion-test evidence).
3. The no-finite-mean-energy property should be stated in the density's
   scope block before downstream thermodynamic use.
