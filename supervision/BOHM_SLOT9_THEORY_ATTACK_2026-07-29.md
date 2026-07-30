# SLOT 9 THEORY ATTACK — verbatim agent return (2026-07-29)

The first genuine theory work in the program this week. Single agent, three mechanism classes
(topological/index; boundary/completeness; ratio/overdetermination), plus a judgement.

STATUS: SINGLE-SOURCE, NOT ADVERSARIALLY VERIFIED as a whole. The reviewer independently
verified the load-bearing ARITHMETIC (see below); the physics arguments and the E1-E4
exhaustion are unverified and must be attacked before any of them is relied on.

REVIEWER'S INDEPENDENT VERIFICATION OF THE TRACE-COLLAPSE CLAIM (exact rational arithmetic,
weights of Lambda^k over 5-subsets, Q = diag(-1/3,-1/3,-1/3,1,0), H = diag(0,0,-1,1,0)):
  Tr_Lambda0 = 0 for all pairs.
  Tr_Lambda2 = 3 * Tr_5 for all pairs (Q,Q), (H,H), (Q,H).
  Tr_Lambda4 = 1 * Tr_5 for all pairs.
  Tr_5(Q,Q) = 4/3 · Tr_5(H,H) = 2 · Tr_5(Q,H) = 4/3.
  Tr_5(H,H)/Tr_5(Q,Q) = 3/2  == the corpus's K_H = (3/2) K_Q.
  Tr_5(Q,H)/Tr_5(Q,Q) = 1    == the corpus's K_QH = K_Q.
CONFIRMED: the trace factor is COMMON to every pair, so it cancels in ratios. The two "forced
ratios" ARE the Cartan inner-product ratios of two fixed lattice vectors. They carry no
dependence on the depth x, on the I_n integrals, or on anything the heat kernel computed.

I have what I need. Here is the analysis.

---

# Slot 9: What excludes a finite local `c·F²` counterterm in a theory with no bare `F²`?

## 0. The object, stated exactly

Before any mechanism can be judged, the object it must act on has to be pinned down, because this is where match-by-name failures live. From `alpha_br_frozen_primitives_v001.py`, `derive_alpha_br_common_induced_coefficients_v001.py`, and `reports/alpha_br_common_induced_coefficients_v001.md`:

- The carrier is `Λ^even(C⁵)` = Λ⁰ ⊕ Λ² ⊕ Λ⁴ = **1 + 10 + 5̄**, with SU(5) Casimirs `C2 = deg(5−deg)·6/10 ∈ {0, 18/5, 12/5}` and multiplicities `{1, 10, 5}`.
- `Q = diag(−1/3, −1/3, −1/3, 1, 0)` and `H = diag(0, 0, −1, 1, 0)` are **traceless diagonal 5×5 matrices** — genuine su(5) Cartan elements (`SEAT_Q = SEAT_Y + SEAT_T3`, `SEAT_H = SEAT_Q + SEAT_C`).
- `K_Q(x) = Σ_a Tr_a(Q²) I_1(x + C2_a)/(24π²)`, with `I_n(c) = ∫_1^∞ τ^{−n} e^{−cτ} dτ` — the record-floor-regulated exponential integral. The floor `τ ≥ 1` is the lower proper-time limit of `Γ_BR,k` in `alpha_induced_only_boundary_action_principle_v001.md`.
- The deformation at issue, in the corpus's own normalization (`reports/alpha_target_free_finite_u1_route_audit_v001.md`): `ΔΓ_c[A] = (ħ c_R/4)∫F_{μν}F^{μν}`, i.e. `K ↦ K + c_R`.

**A structural fact that has not been stated in the corpus and is load-bearing for everything below.** For any traceless X, Y ∈ su(5) Cartan:

- `Tr_{Λ⁰}(XY) = 0`
- `Tr_{Λ⁴}(XY) = Tr_5(XY)` (since Λ⁴C⁵ ≅ 5̄, and squares/products of Cartan elements are conjugation-invariant)
- `Tr_{Λ²}(XY) = (N−2)Tr_5(XY) + (Tr_5 X)(Tr_5 Y) = 3·Tr_5(XY)` for N = 5, the second term vanishing by tracelessness.

Therefore the whole induced gauge kinetic matrix collapses:

```
K_XY(x) = Tr_5(XY) · S(x),     S(x) = [ I_1(x + 12/5) + 3 I_1(x + 18/5) ] / (24 π²)
```

Check against the executable grouping in the report: `Tr_5(Q²) = 3·(1/9) + 1 = 4/3` (report: `TrQ2=1.33333` on the dim-5 block, `4` on the dim-10 block = 3×4/3 ✓); `Tr_5(H²) = 1 + 1 = 2` (report: `2` and `6 = 3×2` ✓); `Tr_5(QH) = 1/3 + 1 = 4/3` (report: `4/3` and `4` ✓).

**Consequence.** `K_H = (3/2)K_Q` and `K_QH = K_Q` are *not* two derived dynamical relations. They are `Tr_5(H²)/Tr_5(Q²) = 3/2` and `Tr_5(QH)/Tr_5(Q²) = 1` — two Cartan inner products of two fixed lattice vectors. They carry **no dependence on `x`, on `I_n`, on the carrier's spectral structure, or on anything the heat kernel computed**. The gauge sector of this construction contains exactly **one unknown scalar function `S(x)`**, projected three ways.

I also note that the script's `projection_error` gate (`em_stiffness` vs `(8/3)·su5_stiffness`) is `q2/(24π²)` vs `(8/3)·q2/(64π²)`, i.e. it verifies `8/3 = 64/24`. It is arithmetic, not a cross-check. Likewise the `derivative_error` gates verify `I_n′ = −I_{n−1}`, a property of the integral. The gate's PASS content is representation theory plus identities about exponential integrals. That is fine as far as it goes, but it must not be read as physical overdetermination. (No coefficient is evaluated anywhere in this report.)

---

## Class 1 — Topological / index-theoretic: a category error, cleanly

**The general mechanism and what it requires.** Every member of this class — Atiyah–Singer, the local index theorem, anomaly coefficients, θ-periodicity, Chern–Simons level quantization, Chern numbers — quantizes a coefficient by making it the coefficient of a **characteristic form**: a wedge polynomial in curvature 2-forms, whose integral over a closed manifold is a topological integer. The quantization argument in each case requires that the density be metric-independent and configuration-independent (depending only on the bundle class), so that the coefficient multiplies an integer and single-valuedness or integrality forces it.

**`F ∧ *F` is not of that type, and the obstruction is not technical.** The Hodge star is a metric-dependent, configuration-dependent operation. `F ∧ *F` is a wedge of `F` with an object built from `F` *and* `g` by index contraction; it is not a polynomial in curvature 2-forms. There is therefore no invariant whose density it can be. In 4d the complete list of relevant densities makes this concrete: `F ∧ F` is the second Chern density (parity-odd, integral), `tr R ∧ R` is the signature density (parity-odd, integral), `E_4` is the Euler density (parity-even, integral — but purely gravitational, since the "εεRR" construction closes only for the frame bundle whose fiber ε is the spacetime ε). There is no parity-even gauge characteristic class in four dimensions, because contracting two epsilons against two `F`'s requires the metric, which is exactly what disqualifies it. The corpus's own counterterm gate states the type marker without drawing the inference: "`F wedge *F` is local, **parity even**, and gauge invariant." Every Class 1 mechanism produces a parity-odd density (or the gravitational Euler density). The classes do not intersect.

**Specific mechanisms, individually.**

- *Anomaly coefficients* are unrenormalizable because they are the local index density. The prompt's suspicion is correct and the category error is exactly this: the `F²` kinetic term is not an anomaly. Its 4d cousin is the *beta function*, which is the coefficient of the **log**, and that is universal — but "universal log coefficient" constrains `dK/d ln k`, not `K`. Adding `c_R` changes the constant of integration and leaves every log coefficient untouched.
- *Local index theorem.* `str(γ₅ e^{−tD²})` is `t`-independent and equals the index; all `t`-dependent `a_n` cancel in that supertrace. The `F²` kinetic term lives in `tr(e^{−tD²})` — the log-determinant, no `γ₅`. **Explicit match-by-name warning:** `STr′_BR` in `alpha_induced_only_boundary_action_principle_v001.md` "carries the statistics and ghost signs." It is a statistics supertrace, not the `γ₅` index supertrace. The local index theorem never engages this object.
- *η invariants* are metric-dependent and not quantized (only `η mod Z` / `exp(2πiη)` is topological); they contribute to phases and to odd-dimensional or boundary CS terms, never to a 4d parity-even modulus.
- *CS level quantization* is 3d and topological. The corpus's own audit already kills the dimensional-reduction version: `1/g₄² = β/e₅²` leaves the extent `β` continuous. Level quantization plus a compactification extent is still one continuous parameter.
- *`a_2` / heat kernel.* `a_2 = (4π)^{−2} tr(E + R/6)` is not quantized; it is the corpus's `C_R`, continuous in `x`. And the corpus itself already identifies the only topological piece it has: "The Euler integral is topological at fixed topology; the Weyl-squared term supplies the non-topological fourth-derivative local coefficient."

**Is there an index-like factor inside `K_Q`?** Yes, and the factorization above says exactly where. Write `K_Q = Tr_5(Q²) · S(x)`.

- **Quantized / discrete:** `Tr_5(Q²)`, fixed by `Q` being a coweight paired integrally with the weight lattice of the 16 (this *is* charge quantization); the Dynkin index ratios `{0, 1, 3}`; the multiplicities `{1, 5, 10}`; the Casimir rationals `{0, 12/5, 18/5}`. `reports/alpha_br_source_clutching_chern_map_v001.md` supplies a genuine integer: `H` has unbroken-U(1) magnetic Chern number 1. But that integer multiplies `∫F` (flux), never `∫F ∧ *F`.
- **Continuous:** `x`, hence `S(x)`.
- **`c_R` enters neither.** It is an additive offset *outside* the product.

This is the crisp reason Class 1 is impotent, and it generalizes: quantization arguments constrain **multiplicative factors and arguments**; they cannot constrain an **additive offset** unless the offset itself is the coefficient of a characteristic form. The quantized data fix *which curve* in the (`x`, `K`) plane; `x` fixes *where on the curve*; `c_R` translates the whole curve vertically, and no discrete invariant of the su(5) data is a function of a vertical translation. This is consistent with, and explains, given fact (a): compactness and charge quantization kill the *multiplicative* freedom in `A`'s normalization and say nothing about the additive one.

**One genuine loophole, and it is the only place Class 1 touches the problem.** On a self-dual or anti-self-dual configuration, `F ∧ *F = ±F ∧ F`. There, and only there, the parity-even action evaluated on a configuration equals `K` times a topological integer. That does not *exclude* `c_R` — it makes the **total** `K = K_induced + c_R` the thing that multiplies an integer. I return to this in Class 3 as the only viable anchor shape.

**Class 1 verdict: category error. No mechanism in this class reaches a kinetic coefficient at all.** This is a clean negative and I am confident in it.

---

## Class 2 — Boundary / completeness

**(i) Complete spectrum, finite response, no subtraction freedom.** The finiteness in this corpus is real: `I_1(c)` is finite for `c > 0`. But the finiteness is *produced by the proper-time floor* `τ ≥ 1`, i.e. `s ≥ 1/k_R²`. In `Γ_BR,k = −(1/2)∫_{1/k_R²}^{1/k²} (ds/s) STr′ exp(−sL)`, `Γ_BR,k_R = 0` holds because the integration range is empty. **`K_bare = 0` is not a derived property of a complete spectrum; it is the statement that the boundary condition is imposed at the lower endpoint.** The floor *is* the subtraction. The corpus's own route audit says this: `K_R(Λ_R[X];X)=0` "becomes absolute only if `X` derives the physical boundary scale, the complete spectrum, the regulator or measure, and the finite response. Choosing `Λ_R` is not itself a derivation."

**(ii) UV-softness / superconvergence.** This is the strongest candidate in the class and the corpus ranks it #2 (`PASS-CONDITIONAL / BLOCK-CURRENT`). I want to state a structural incompatibility that I do not find made explicit anywhere, because it explains the "PASS-for-running, BLOCK-for-absolute" split as a dichotomy rather than a gap.

An unsubtracted dispersion relation for `Π_T` requires the spectral superconvergence sum rule. A nonzero `β_K` is exactly the failure of that sum rule: the corpus's own benchmark `K_1D(Q;Λ,m)` has `dK/d ln Q → −1/(6π²)` and the corresponding gauge-handle coefficients (`b_fermion = 20/3, 4, 4`) are nonzero. So: **superconvergence and a nonzero beta function are mutually exclusive statements about the same spectrum.** The program's closed result is "running is thresholded Boundary Resolution" (`f_charged_step24c`), which requires `β_K ≠ 0`. Its best absolute route requires superconvergence. Those cannot both hold at all scales. If the softness holds only above `k_R` while the log holds below, that is not superconvergence — that is a cutoff, i.e. option (iii).

There is a further nuance worth recording. Superconvergence would not *derive* `K_bare = 0`; it would make `K_bare = 0` **well-posed and scheme-free**, whereas without it the phrase requires a scale and a subtraction scheme to even have a referent. That is a real upgrade, and it is why this route is worth ranking highly. It is not a mechanism of exclusion.

**(iii) Boundary condition at a derived scale.** The prompt asks me not to dodge, and there is no need to: **the corpus has already executed the refutation of the most attractive version of this.** From `reports/alpha_strict_route_ledger_audit_v001.md`, entry `fresh_gravity_em_normalization_identifiability_v001`, status `BLOCKED`: "countermodels with the same gravity coefficient regulator and EM slope retain different additive Maxwell stiffness; reopen/next: **do not infer absolute EM normalization from G**."

That kills the idea I judged most promising on structural grounds before finding it. The idea was: the relocation `c_R → k_R` is not freedom-preserving, because `k_R` is *over-used* — it multiplies `C_V` as `k_R⁴`, `C_R` as `k_R²`, and sets the thresholds through `x = r²/k_R²`. So fixing `k_R` gravitationally should determine `K_Q`. The countermodel says no: one can hold the Einstein coefficient *and* the EM slope fixed and still move the additive stiffness. The reason is visible in the structure: `c_R` is `x`-independent, so it is invisible to any condition that acts through `x` — including a stationarity/saddle condition on the depth. **The saddle that selects `x` cannot select `c_R`, because `∂c_R/∂x = 0`.**

So: no version of (iii) avoids relocation. Say it plainly — that is a result.

**(iv) Finite-dimensionality.** If the carrier were finite in *spacetime* as well as internally, `log det` would be a finite sum, absolutely defined, no subtraction. The corpus's rank-1 candidate is exactly this ("fully finite **total** record-cell triple"), blocked because "current carrier is only internally finite; spacetime spectral support, cell density, and CTP construction are missing" — which is the known stitching gap.

But finite-dimensionality fails for a *categorical* reason too, not just the missing stitching theorem: **the space of admissible local gauge-invariant operators does not shrink to a point when the Hilbert space does.** The audit's own counterexample is decisive and physical — quantum spin ice, a spin-1/2 model with exact emergent U(1), admits gauge-preserving perturbations `ζ` and `μ` that demonstrably move the emergent coupling. "Fixed local dimension and Gauss law coexist with continuously variable electric, magnetic, and symmetry-preserving perturbation coefficients." Enumeration of admissible local terms in a finite model yields a *finite basis with continuous coefficients*, which is exactly the wrong kind of finiteness.

What finiteness *does* buy, and this is the one non-trivial gain in the whole landscape: if the microscopic rule's entries are required to be integral or algebraic and fixed by antecedent premises (audit §11.1), then the relocation lands in a **discrete menu of rules** rather than a continuum of coefficients. Discrete relocation of a continuous freedom is a genuine reduction in kind. But the corpus's own uniqueness test has already returned `FAIL_ADOPTED_STRUCTURE_UNIQUENESS`: the SU(5) parent is an adopted axiom (observed unbroken algebra has dimension 12, the parent adds 12 undetermined broken directions), `exp(−tC2)` and `exp(−tC2²)` both pass, and both one-loop and two-loop `T²` readings survive. So the menu is populated and unselected. "A finite menu of unexplained discrete models is not yet an absolute prediction."

**Class 2 verdict: (i) is the floor in disguise; (ii) is incompatible with the program's own running result; (iii) provably relocates and the relocation has been executed as a countermodel; (iv) is refuted categorically, with a partial gain (discrete relocation) that is itself currently unselected.**

---

## Class 3 — Ratio and overdetermination

**Is a ratio invariant under an additive deformation?** Only if the deformation is proportional to the same bilinear form. With `K_XY = Tr_5(XY)·S(x)`, the question becomes: must an admissible local counterterm `c_XY F^X F^Y` satisfy `c_XY ∝ Tr_5(XY)`?

**The answer is a conditional theorem, and it is real.** If the gauge symmetry at the induction scale is the *simple* algebra su(5), then by Schur's lemma the invariant symmetric 2-tensor on the adjoint is unique up to scale, so any su(5)-invariant local dimension-4 kinetic counterterm is `c·Tr(F_{μν}F^{μν})` with **one** `c`, and `K_XY ↦ (S(x) + c)Tr_5(XY)`. The ratios `K_H/K_Q` and `K_QH/K_Q` are then **exactly invariant**. This is not a relocation — it is a genuine invariance, and it survives operator-level deformations too: a Pauli vertex `κ σ^{μν}F^A_{μν}T_A` contributes to `a_4` through `tr(E²)` a term `∝ κ² Tr_a(T_A T_B)`, again proportional to `Tr_5`, and its linear contribution to `a_2` vanishes because `tr(σ·F) = 0`. So an su(5)-covariant Pauli deformation moves `K` while leaving `C_R` untouched — it is transverse in the sector direction and *parallel* in the Cartan direction.

**So the structure requires the counterterm to respect the trace structure, not to be sector-diagonal — conditional on su(5) being the symmetry.** And the condition is load-bearing: the corpus's own countermodel audit says the observed unbroken algebra has dimension 12 (not simple), and the su(5) parent is an *adopted axiom*. If the counterterm need only respect the unbroken 12-dimensional algebra, `c_XY` has three independent pieces, `Q` is a combination across factors, and the ratios move. Furthermore, even granting su(5) at `k_R`, the protection lives at `k_R`: below the breaking scale, independent threshold corrections for each surviving factor are allowed. **The protection is real but sits at the wrong scale for a low-energy statement** — this is the standard GUT threshold problem and it is not evaded here.

**What the ratios buy and do not buy.** They buy that the gauge sector has one unknown function, not three, and that this reduction is immune to the counterterm. They do **not** buy `α`, and the reason is sharper than "ratios don't fix normalization": these particular ratios are `x`-independent constants. **A quantity independent of the unknown cannot determine the unknown.** They are invariant under `c_R` precisely because they are empty of the content needed. The anchor would have to be one equation for the *absolute* value `S(x*) + c_R` at a specified scale. Candidates: (1) a topological-sector weight (the self-dual loophole from Class 1 — `K_total` multiplying an integer, anchored by an independently normalized sector weight); (2) a UV fixed-point value; (3) the gravitational sector — **explicitly closed** by the executed countermodel above.

**Overdetermination: one determination twice, not two.** Rigorously:

1. `C_V`, `C_R`, `K_Q`, `K_H`, `K_QH` and the `a_4` gravitational coefficients are all moments of the *same* heat kernel of the *same* frozen operator over the *same* inventory, differing only in the weight (`d_a` vs `Tr_a(Q²)`) and the `I_n` order. Within the gauge sector the collapse is total: three coefficients, one function.
2. Decisively, the map is **not injective in the relevant direction**: the executed countermodel holds `C_R` and `β_K` fixed and moves the additive stiffness. Two determinations force a number only if both constrain the same unknowns and are functionally independent. Here the EM "determination" carries a free direction (`c_R`) that the gravitational one does not touch.
3. The parameter count makes this exact. With all bare local coefficients set to zero by postulate, the unknowns are `(k_R, x)` — two — and the sectors supply more than two coefficients, so there is genuine overdetermination *of the postulate*. Allow bare `F²` and the unknowns become three; allow the whole dimension-≤4 basis (`√g`, `√g R`, `√g F²`, `√g C²`) and the count becomes five. **The induced-only postulate is doing precisely as much work as the number of coefficients the program wants to explain, no more and no less.** It is not a convenience. It is the load-bearing input.

**Class 3 verdict: the ratio-protection theorem survives (conditionally); the overdetermination claim does not. It is one trace, one scalar function, one determination presented several ways.** This is exactly where a match-by-name error would have hidden, and the `(8/3)` "projection agreement" gate is a live instance: it is presented as agreement with an independent parent computation and it is the arithmetic identity `8/3 = 64/24`.

---

## The reframing that makes the negative decisive

`c_R` is not a symmetry-violating object that a cleverer symmetry might catch. **`c_R` is the integration constant of the RG flow of a marginal coupling.** `K(Q) = ∫_Q^{Λ} β_K d ln k` is a first-order flow equation; a first-order equation has exactly one boundary datum per coupling. The corpus states this in its own words at `alpha_spectral_ncg_absolute_stiffness_research_v001.md`: the exact determinant "does not fix the additive integration constant defining the stiffness at one reference scale."

Given fact (b) — the condition class (local, causal, Lorentz-covariant, gauge-invariant, finite, regulator-independent, packing-independent) is *closed* under `K ↦ K + c` — the conclusion is immediate and needs no further search: **no condition in that class can supply the boundary datum, because no condition in that class distinguishes the two theories.** Slot 9 has no solution *inside* the class. Any solution must come from outside it. Exhaustively, the ways to fix an integration constant of a marginal coupling are:

- **E1. A UV fixed point at which the `F²` direction is irrelevant.** The only exit that *replaces* the boundary datum rather than relocating it: the fixed point is a property of the flow, not a chosen scale, and adding `c_R` moves you off the critical surface, so UV completeness excludes it. Residual freedom relocates into *discrete* data (which fixed point; the integer number of relevant directions). This is the only mechanism I can construct that passes the relocation test. **But it cannot be applied to this object as currently posed:** `K_bare = 0` means `g = ∞` at `k_R`, and the corpus's own gauge-handle test states that the perturbative gauge/ghost calculation "cannot be extrapolated back to `K=0`, where `g` is infinite and the perturbative gauge/ghost calculation is not defined." The corpus has imported the relevant gravitational ingredient (Toms' `β_e^gravity = −3κ²Λe/(64π²)` in `alpha_br_orbit_space_quantization_corollary_v001.md`) and its own non-use rule correctly says what is missing: a derived trajectory and a derived `G_k Λ_k`.
- **E2. Superconvergence.** Incompatible with `β_K ≠ 0` at all scales, as argued. Collapses into E3 if the softness is only above `k_R`.
- **E3. Boundary condition at a derived scale.** Provably relocates; countermodel executed.
- **E4. `K` appearing only multiplied by an integer** (self-dual / topological-sector pairing). Dissolves the question rather than closing it: the anchor fixes the *sum*, so the counterterm becomes moot instead of excluded. Not present in the corpus, and my prior is against it: the coarea measure rule's discrete data enter `Γ_orbit` **additively** (`+ log Vol_h(Stab) + log|Stab_discrete|`), i.e. `K`-independently, which is the wrong form to anchor `K`.

That is the exhaustion, and it is what makes the negative decisive rather than merely unproven.

---

# The five judgements

**1. What survives my own attempt to refute it, and what would still have to be proved.**

Two things, neither of which closes slot 9.

*(a) The ratio-protection theorem (Class 3).* If the local counterterm must be su(5)-invariant, then `K_XY ↦ (S(x)+c)Tr_5(XY)` and `K_H/K_Q = 3/2`, `K_QH/K_Q = 1` are exactly invariant under every additive deformation, action-level or operator-level. I could not break this. Still to be proved: (i) that su(5), not the 12-dimensional unbroken algebra, is the symmetry constraining counterterms at `k_R` — currently an *adopted axiom* per `alpha_br_structure_provenance_countermodels_v001.md`; (ii) that the protection survives transport below the breaking scale, where independent per-factor threshold corrections are allowed. Without (ii) the theorem is a statement at `k_R` only.

*(b) UV-fixed-point irrelevance (E1).* The only mechanism whose residual freedom is discrete rather than continuous. Still to be proved: that the coupled (gravity + BR carrier) flow has a fixed point; that `F²` is irrelevant there; and — prior to all of that — that the flow is even definable from an initial condition at `g = ∞`, which the corpus's own gate says it is not.

**2. Category errors, bluntly.**

*Class 1 in its entirety is a category error for this object.* Index densities are wedge polynomials in curvature 2-forms; `F ∧ *F` is not one, because `*` is metric- and configuration-dependent. There is no theorem to find. Sub-errors named: an anomaly coefficient is not a kinetic coefficient (the 4d analogue of anomaly-rigidity is beta-function universality, which constrains `dK/d ln k`, not `K`); `STr′_BR` is a statistics supertrace, not the `γ₅` index supertrace, so the local index theorem never engages; the quantized data in `K_Q` (coweight norm, Dynkin indices `{0,1,3}`, multiplicities `{1,5,10}`, Casimirs `{0,12/5,18/5}`, the unit Chern number of `H`) are all multiplicative factors and arguments, and quantizing a factor cannot constrain an additive offset. *Class 2(iv), finite-dimensionality, is also a category error:* a finite Hilbert space gives a finite operator basis with continuous coefficients, which is the wrong kind of finiteness — the corpus's own quantum-spin-ice counterexample settles it.

**3. The bottom line.**

**No credible mechanism is known, and slot 9 is unclosable as posed.** `c_R` is not a symmetry-violating deformation; it is the integration constant of a first-order RG flow for a marginal coupling. Given the already-proved fact that the corpus's condition class is *closed* under `K ↦ K + c`, no condition in that class can exclude it — the question has no solution inside the class it is asked in. The exits are outside the class and number four; three are already blocked in this corpus (superconvergence contradicts the program's own running result; the derived-boundary-scale route has an executed countermodel; the topological-anchor route has no candidate normalization and the corpus's discrete measure data enter additively); the fourth, fixed-point irrelevance, cannot be evaluated from a `g = ∞` initial condition. **Slot 9 should be retired as posed and replaced by the exit question: which of E1–E4 obtains.**

**4. What the program then is.**

A theory with an unfixed additive marginal coupling can legitimately claim: (i) the *running* of that coupling, which is universal — the program's `β_K` results are genuine; (ii) *ratios* invariant under the deformation, which here means the su(5)-protected relative gauge normalizations, conditional on the parent axiom; (iii) *one relation* among the coefficients it generates from a shared `(k_R, x)`, valid only if every bare local coefficient of dimension ≤4 is zero. It **cannot** claim `α` as an unconditioned output. The parameter accounting is exact and unforgiving: with the whole bare basis allowed there are five unknowns; with induced-only adopted there are two. The postulate supplies precisely the missing constraints. **Predicting a dimensionless number from a postulate that contains exactly one free dimensionless number per predicted coefficient is a reparametrization, not a prediction** — unless the postulate is independently earned by predicting something else first. The honest label is: `α` is a *consequence of the induced-only axiom*, with the axiom flagged as carrying the same dimensional weight as the output. This is stronger than the corpus's current framing and it is the fact that should govern how the result is described.

**5. The one next theory step, and its falsifier.**

**Promote the ratio-protection result to a stated theorem and make it — not `α` — the program's primary deliverable.** Concretely: (i) prove `K_XY(x) = Tr_5(XY)·S(x)` from the three-line trace identity above (`Tr_{Λ⁴} = Tr_5`, `Tr_{Λ²} = 3Tr_5`, `Tr_{Λ⁰} = 0` for traceless Cartan arguments), thereby retiring the "two forced ratios" as independent determinations and correcting the `(8/3)` gate's status; (ii) prove that su(5)-invariance of the counterterm implies exact invariance of `K_H/K_Q` and `K_QH/K_Q` under every additive deformation including Pauli-type operator deformations; (iii) state the resulting relative-normalization prediction as an `α`-free, counterterm-immune output; (iv) carry it below the breaking scale and quantify what independent threshold corrections do to it.

This is executable now from primitives already frozen in the corpus, it requires no scale, no depth, and no coupling value, and it converts a blocked `α` claim into a live falsifiable one.

*Falsifiers, any one of which kills it:* (a) a demonstration that the admissible counterterm need only respect the 12-dimensional unbroken algebra rather than su(5), in which case `c_XY` has three independent pieces and the ratios are not protected; (b) an observed relative normalization of the two U(1) directions inconsistent with `Tr_5(H²)/Tr_5(Q²)` and `Tr_5(QH)/Tr_5(Q²)` after honest threshold transport; (c) a demonstration that threshold corrections below the breaking scale can shift the ratio by an amount comparable to the prediction, which would show the protection lives only at `k_R` and is untestable.

Companion negative to record alongside it: the E1–E4 exhaustion in §"The reframing", whose own falsifier is the exhibition of a fifth exit — a condition that fixes the integration constant of a marginal coupling without a scale-boundary condition, a fixed point, compositeness, or a topological pairing. If no one can name a fifth, slot 9 is closed as unclosable, which is itself a result the program can bank.