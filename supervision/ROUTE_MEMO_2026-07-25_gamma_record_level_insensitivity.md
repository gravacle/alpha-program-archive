# Route Memo — Option Gamma Scoping: Record-Level ER Insensitivity (VERDICT: DEAD, pending kill-test)
Claude lane · 2026-07-25 (night) · fresh-context theory lane return, recorded verbatim below.
Bottom line: gamma in its exact form is DEAD on the available structure — with a proven
mechanism explanation and one cheap predeclared symbolic kill-test remaining (predicted
to confirm refutation). Two NEW exact parity lemmas proven and verified against sealed
artifacts survive as unconditional yield.

All checks are in. The λ-parity lemma holds at machine epsilon on the actual sealed carrier machinery (5.6e-14 at a = 0.07, both envelopes), the a-parity lemma is confirmed inside the sealed primary JSON itself (1e-15 to 1e-17), the record moments are exact, and the toy counterexample matches its closed form to four digits. The memo follows.

---

# ROUTE MEMO — Option γ scoping: "record-level ER insensitivity" as an operator theorem

Theory scoping lane, fresh context, 2026-07-25 (night). Read-only; scratch only under `scratchpad/gamma_scope/`. Chartered by `DECISION_2026-07-25_er_fork_option_gamma.md` (read first, discipline applied: numerical cancellation is not the theorem; only an exact operator-level algebraic identity counts; formulation is against what reaches kappa_record, not the finite-lane proxy).

**BOTTOM LINE (stated up front per charter): γ in its exact form is dead on the structure available to prove it, and I recommend saying so: gamma dead, beta — subject to exactly one cheap, named, symbolic kill-test (Section 6) that the derived structure predicts will fail. What survives of γ is a pair of new exact parity lemmas (proven here, verified against sealed artifacts) plus an honest-partial-discharge bound route, which is not γ under the principal's rule.**

---

## 1. The candidate theorem, typed exactly

### 1.1 Objects (amended architecture, battery chain)

Per `STAGE8_T7_OPERATOR_VALUED_PRIMITIVE_RESPONSE_ARCHITECTURE_AMENDMENT_V001.md` (A1/A2) and battery T7 of `STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_AUTHORITY_FABLE_V002.md`: the object that feeds kappa_record is the **completed-record amplitude** of T7(i), Z_h(A) = a_h(A)/a_h(0) (per `BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md`), whose volume-uniform zero-free neighborhood (T7(ii)), linked-cluster thermodynamic density (T7(iii)), and Duhamel/intensive-Hessian equality H_K = g_{D,K} (T7(iv), typed in `ROUTE_MEMO_2026-07-25_duhamel_intensive_hessian.md`) produce the intensive limit that is the kappa_record source. The finite realization of the completed amplitude on a carrier member is (Phase-A spec `STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md`, A3/A4):

```
Z_ER(a) = sum_lambda w_lambda · omega( Gamma( u_{lambda,ER}(a) ) ),
lambda in {-sqrt2, 0, +sqrt2},  w_lambda = <pointer|P_lambda|ready> = (-1/4, 1/2, -1/4),
u_{lambda,ER}(a) = T-exp[ -i ∫_0^1 ( h_0 + lambda·v_ER(t)·M(t)⊗S + a·J(t) ) dt ],
S = -i γ^0 γ^5,   J(t) = -B_D(t)⊗α_x.
```

The completed/exhaustive distinction is binding: the amendment's A2 scalar closure Z_K = ω_in(R_all) is the **exhaustive** kernel; T7(i) is the **completed** one; `STAGE8_T7_CRITICAL_PATH_SCOPE_CORRECTION_V001.md` forbids substituting either for the other. This memo's statement is typed on the completed object, matching T7(i) and matching what the executed gate (`STAGE8_T7_ER_FORK_KAPPA_INSENSITIVITY_RESULT_V001.md`) measured. Note the T7(i) normalization a_h(A)/a_h(0) restores the log anchor Ẑ(0) = 1 for the completed chain (the exhaustive chain's anchor Z[A,A] = 1 does not apply to the completed object, whose witnessed raw moduli are ~5.9e-4 … 6.8e-2).

### 1.2 The ER-difference operator D_ER

From `STAGE8_T7_CRITICAL_PATH_SCOPE_CORRECTION_V001.md` section 1 (w_T(t) = ρ₄V₃(t), ρ₄ = 24/(πT_R⁴); the proposed ER-B slice generator τ_R ρ₄ M(t)) as executed in `STAGE8_T7_ENVELOPE_REALIZATION_COMPARISON_SPEC_V001.md` (frozen branches, unit cell):

```
V_A(t) = v_A(t)·M(t)⊗S,  v_A(t) = tau_R·32·r(t)^3 = tau_R·V_3(t)/V_4(D)     (ER-A)
V_B(t) = v_B(t)·M(t)⊗S,  v_B(t) = tau_R/V_4(D) = 24·tau_R/pi               (ER-B)

D_ER(t) := V_A(t) - V_B(t) = (tau_R/V_4(D))·[ V_3(t) - 1 ]·M(t)⊗S
         = tau_R·[ 32·r(t)^3 - 24/pi ]·M(t)⊗S,
```

with r(t) = min(t, 1−t), V₃(t) = (4π/3)r(t)³, V₄(D) = π/24, τ_R = π/√2. The envelope enters the generator **only** as the scalar time-profile multiplying the record coupling λ; h₀ and J are envelope-free. Note ∫v_A dt = τ_R (time-marginal normalized) while ∫v_B dt = τ_R/V₄(D): the two branches normalize different marginals; no reparametrization maps one flow to the other while fixing h₀ and J (checked; see 5.1).

### 1.3 The Hessian functional and the identity to prove

Per-cell (and per exhaustion member K) define, on the T7(ii) zero-free neighborhood:

```
kappa_K(ER) := - d^2/da^2 log| Z_{K,ER}(a) |  at a = 0
```

(normalization-insensitive: the a_h(0) normalization and any constant rescaling drop out of the Hessian — same fact the V002 stencil used).

**CANDIDATE THEOREM (record-level ER insensitivity, strong form).** For every cell and every member K of the relayed causally-sequential exhaustion (`STAGE8_T7_RELAYED_FAMILY_RESOLUTION_RESULT_V001.md`, `STAGE8_T7_OPEN_EXHAUSTION_ATTACHMENT_AND_RELAY_NECESSITY_RESULT_V001.md`):

```
kappa_K(ER-A) = kappa_K(ER-B)   exactly,
```

equivalently: the derived functional D_K[v] := ∂²_a log Z_{K,v}(a)|_{a=0} has vanishing Gâteaux derivative in the direction D_ER along the segment {v_B + ε(v_A − v_B), ε ∈ [0,1]} — "the Hessian functional annihilates D_ER."

**Quantifier scope needed to discharge the fork for kappa_record purposes:**

- **Second order in a, exact — and that SUFFICES.** Justified, not merely assumed: kappa_record is by definition (battery T7(iv); V011 kappa_record semantics; the typed H_K = g_{D,K} of `ROUTE_MEMO_2026-07-25_duhamel_intensive_hessian.md`) the intensive limit of the a = 0 Hessian. No a³-or-higher data feeds it. The physical leverage a ≤ 0.13 is a proxy-lane (stencil-error) concern only. Caveat: the discharge is kappa_record-scoped; any downstream consumer evaluating at finite a (Q_spec, EM order steps) reopens the fork there. The dischargeable flag is "ER fork closed **for kappa_record**", not ER_fork_closed globally.
- **All orders in the record coupling.** λ·v is O(1) (τ_R ≈ 2.22, v_B ≈ 17); there is no small parameter. A leading-order-in-record-coupling identity discharges nothing exactly.
- **Per exhaustion member K, not merely per cell.** Per-cell exactness does not automatically kill multi-cell connected clusters in the T7(iii) linked-cluster expansion of log Z_K: connected terms spanning several cells carry products of per-cell record-dressed correlators, and their envelope dependence is not a sum of per-cell Hessian differences. The theorem must be typed at K-level (or a separate multi-cell lemma supplied).
- **Uniformly in K**, so the identity survives the intensive limit through the same (H1)/(H2) Vitali–Cauchy interchange already required by the Duhamel route memo, applied to the difference sequence κ_{A,K} − κ_{B,K}. If the identity is exact per-K, no new interchange machinery is needed — the limit of the zero sequence is zero. (What IS new: the ER-B side has no sealed T7(ii)/(iii) inputs at all — see 5.2.)

Sharp distinction as demanded: exact-all-orders-in-a is NOT needed; second-order-in-a exact IS needed and suffices for kappa_record; leading-order-in-record-coupling does NOT suffice.

---

## 2. Derivation — how far the proof goes, and where it dies

### 2.1 Starting identities, verified

From the A3 c-matrix of the Phase-A spec: eigenvalues {−√2, 0, +√2}; λ = 0 eigenvector (|ready⟩+|pointer⟩)/√2; p_λ = (1/4, 1/2, 1/4), w_λ = (−1/4, 1/2, −1/4). Verified exactly (scratch check): m0 = Σw_λ = 0, m1 = Σw_λλ = c[1][0] = 0, m2 = Σw_λλ² = −1. Consequence, sharpened: for ANY per-history functional f(λ),

```
sum_lambda w_lambda f(lambda) = -(1/4)·[ f(sqrt2) + f(-sqrt2) - 2 f(0) ]
```

— the pointer sum is exactly **(−1/4) times the second symmetric λ-difference**. It annihilates λ-constant and λ-linear parts and nothing else. On the 3-point spectrum all higher moments follow: m_{2k+1} = 0, m_{2k} = −2^{k−1}. The theorem's entire content is the λ-even, record-coupling-dependent part, as the charter says.

### 2.2 Two NEW exact operator lemmas (proven, and verified against sealed artifacts)

**Lemma 1 (λ-parity / chiral conjugation).** T := I_spatial ⊗ γ⁵ satisfies [T, h₀] = 0, T(M⊗S)T = −M⊗S (γ⁵ anticommutes with S = −iγ⁰γ⁵), TJT = +J (γ⁵ commutes with α_x). Hence T h_λ(t;a) T = h_{−λ}(t;a) and u_{−λ}(a) = T u_λ(a) T. Both pinned states are T-invariant (the mixed covariance C = ½(1 − Σ p̂_j⊗α_j) commutes with γ⁵; the pure Dirac-sea projection commutes with h₀ hence with T). Therefore

```
D_{-lambda}(a) = D_lambda(a)   exactly — both states, both envelopes, all a, all orders.
```

This survives Galerkin compression and the sealed quadratures exactly (T acts on the spinor factor only). **Verified on the actual sealed machinery** (executor functions of `scripts/derive_stage8_t7_er_fork_kappa_insensitivity_primary_v001.py`, n=2, ℓ=1, a = 0.07): ‖u_{−√2} − T u_{+√2} T‖₂ = 5.6e-14; |D₊ − D₋| ≤ 2e-15 for both states and both envelopes.

**Lemma 2 (a-parity).** T′ := P_x ⊗ γ¹ (x-parity on the Hermite carrier times γ¹) satisfies [T′, h₀] = 0 (γ¹ anticommutes with α_x, commutes with α_y, α_z; P_x flips p_x), T′(M⊗S)T′ = M⊗S (M, B_D radial; γ¹ commutes with S), T′JT′ = −J. Hence u_λ(−a) = T′u_λ(a)T′⁻¹, both states T′-invariant, so

```
D_lambda(-a) = D_lambda(a)   exactly;  hence Z(-a) = Z(a),  Z'(0) = 0.
```

The sealed quadrature grids (even azimuthal counts) are P_x-closed, so this too is machine-exact. **Verified inside the sealed artifact** `stage8_execution/work/T07_er_fork_kappa_insensitivity_primary_v001.json`: |Z(+7/100) − Z(−7/100)| = 6e-17 … 2.8e-15 across all four (envelope, state) pairs — two to three orders below the a-movement itself. (This also proves the symmetric stencil of `STAGE8_T7_ER_FORK_KAPPA_INSENSITIVITY_BOUND_SPEC_V002.md` is exactly odd-order-free, retroactively strengthening that gate.)

### 2.3 Exact reduction of the theorem

Lemma 1 + m0 = 0 give, exactly:

```
Z(a) = -(1/2)·[ D_{sqrt2}(a) - D_0(a) ]
```

— the completed-record amplitude is the dressed-minus-free history difference; and the λ = 0 history is **exactly envelope-independent** (v multiplies λ). Lemma 2 gives Z′(0) = 0, so

```
kappa(ER) = -Re[ Z''(0) / Z(0) ]
          = -Re{ [ F_v(sqrt2)·H_v(sqrt2) - F(0)·H(0) ] / [ F_v(sqrt2) - F(0) ] },
```

where F(λ) := D_λ(0), H(λ) := ∂²_a log D_λ|_{a=0} (per-history connection log-Hessian; well-defined since D′_λ(0) = 0 by Lemma 2), and F(0), H(0) are envelope-independent exactly. So the theorem is EXACTLY equivalent to:

```
Xi(v) := F_v(sqrt2)·[ H_v(sqrt2) - H(0) ] / [ F_v(sqrt2) - F(0) ]   equal for v = v_A, v_B.
```

Sufficient (and the only natural) exact mechanism: **H_v(√2) = H(0)** — the per-history connection log-Hessian is invariant under record-dressing. Then κ = −Re H(0) for every envelope. This is precisely the "per-cell connection Hessian independent of the record-coupling magnitude" formulation the charter asked me to assess.

### 2.4 The mechanism fails: exact counterexample with the identical algebra

Duhamel around the record-dressed flow U_λ(t): u_λ(a) = U_λ(1)·[1 − iaG_λ − a²K_λ + O(a³)], G_λ = ∫J^λ, K_λ = ∫∫_{t>s}J^λ(t)J^λ(s), J^λ(t) = U_λ(t)†J(t)U_λ(t). The λ- and envelope-dependence of H(λ) rides entirely on this dressing. Take the zero-dimensional chiral model that keeps every recorded structural fact — S² = 1, α_x² = 1, **{S, α_x} = 0** (verified: this anticommutation is exact for the actual S = −iγ⁰γ⁵), the exact pointer weights, unitarity, a quasifree (here rank-one) functional — and drops only the spatial structure (h₀ = 0, M = B_D = 1). Then, with σ(t) = ∫₀ᵗ v and a state with Sψ = ψ, everything closes exactly:

```
D_lambda(0) = e^{-i·lambda·sigma(1)},
d^2_a D_lambda|_0 = -2·Jbar^2·e^{-i·lambda·sigma(1)}·Phi(lambda),
Phi(lambda) = ∫_0^1 dt ∫_0^t ds  e^{ 2·i·lambda·( sigma(t) - sigma(s) ) },
kappa = Jbar^2 · [ 1 - 2·Re( e^{-i·sqrt2·sigma(1)} Phi(sqrt2) ) ] / [ 1 - cos( sqrt2·sigma(1) ) ].
```

κ depends on the **full cumulative profile σ(·)**, not on any endpoint datum. Small-coupling expansion: κ ≈ J̄²·[1 − 8V̄A + 8B]/V̄² with A = ∫∫Δσ, B = ∫∫Δσ² — at EQUAL total action V̄ the shape coefficients are 1/3 (flat), 5/9 (the actual r(t)³ bump), 1 (concentrated). Verified by direct unitary propagation (scratch, matches to 3–4 digits): flat +0.3339, r³-bump +0.5561, near-delta +0.9736; with the actual sealed magnitudes (v_A vs v_B) the toy gives κ_A = 0.707 vs κ_B = 1.802 — an **O(1) envelope difference at order ‖J‖², all record orders**.

**Findings, stated precisely as the charter demands:**

1. H(λ) = H(0) is FALSE as a consequence of the recorded structure. In the counterexample H(λ) − H(0) = −2J̄²[Φ(λ) − ½] ≠ 0 already at order λ² (record coupling squared), and it is NOT suppressed: the resulting κ envelope-difference has an O(1) shape coefficient at the leading order ‖J‖².
2. The property the charter asked me to identify: **none** of {commutation, λ-parity, ±√2 spectral symmetry with equal weights, second-quantized structure} makes the λ-even part envelope-independent. λ-parity (γ⁵) and the equal-weight ±√2 pair produce exactly the odd-part cancellations of Lemma 1 — and nothing more. Worse: the chiral anticommutation {S, α_x} = 0 that generates those cancellations is the very channel that transmits the envelope's cumulative profile into the λ-even Hessian (it makes the record term and the connection maximally non-commuting, so J^λ(t) acquires the profile-dependent phase e^{2iλσ(t)S}). The structure that produces the observed three-history cancellation **obstructs** the γ identity.
3. **The executed gate's "mechanism candidate" is fully deflated.** The observed 1e-10 → 1e-13 suppression in `STAGE8_T7_ER_FORK_KAPPA_INSENSITIVITY_RESULT_V001.md` is quantitatively explained by m0 = 0 + Lemma 1 alone: Δ²_a D_λ ≈ D_λH_λh² ~ O(‖J‖²h²) ~ 1e-9–1e-10 per history, while Δ²_a Z ≈ h²·Z(0)·H-scale picks up the extra factor |Z(0)|/|D_λ| ≈ 6e-4 — three orders — with **no** envelope-insensitivity required. The structural observation is real but it evidences the (now proven) parity lemmas, not γ.
4. Numerical posture of the sealed data: the uncertified point values κ_A − κ_B = 4.6e-9 (mixed) / 5.8e-9 (pure) sit at ~1.4–1.7% of ‖J‖² = 3.39e-7 (‖J‖ = 5.82e-4 from the sealed JSON) — exactly where a **suppressed-but-nonzero** difference (toy O(1) coefficient shrunk by h₀-flow averaging over the 32-dim carrier) would sit. Certified bounds (floors 6.98–82.3) cannot distinguish this from exact zero; the point values weakly favor nonzero.
5. Could the actual h₀/M(t)/B_D structure rescue exactness where the toy fails? No mechanism is visible, and any rescue would have to hold uniformly along the exhaustion (varying carriers), which a delicately h₀-tuned cancellation would not. The burden is now on exhibiting a carrier-specific identity, and Section 6 names the cheap decisive test.

**Per the principal's rule (`DECISION_2026-07-25_er_fork_option_gamma.md`: only an exact algebraic identity counts; the scoping lane is chartered not to assume exactness): gamma dead, beta** — unless the single kill-test below returns exact symbolic zero, which the derived structure predicts it will not. What remains honest and available: (i) the two parity lemmas as sealed exact theorems (they harden the stencil and the blind lanes for free); (ii) an α-flavored certified BOUND |κ_A,K − κ_B,K| ≤ C‖J_K‖²·ε_K with ε_K a computable dressed-overlap factor — the decision memo's "honest partial discharge", which still leaves the fork as disclosed conditionality, i.e., β with a quantitative rider.

---

## 3. The four refutation conditions as testable predictions

**(1) Carrier-dependence.** The decisive sealed test bed is the retained 12-dimensional periodic three-site regression fixture (Phase-A spec A1: "remains only a separate operator regression"; `STAGE8_T7_THREE_SITE_BASELINE_SCOPE_ERRATUM_V001.md`), with the Route-1 one-dimensional comparator (`STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_RESULT_V001.md`, `STAGE8_ROUTE1_SPECIAL_CASE_CONSISTENCY_BINDING_V001.md`) as the even cheaper degenerate case. Prediction: Ξ_A − Ξ_B ≠ 0 on both, computable in exact symbolic arithmetic, with magnitude ~‖J‖² times a carrier-dependent dressing factor; on the sealed ℓ = √2 Hermite carrier the difference should rescale with that carrier's ‖J‖². If γ were true, Ξ_A − Ξ_B = 0 exactly on every carrier of the family — a single symbolic nonzero anywhere kills it.

**(2) a ≠ 0 degradation.** The theorem candidate is a statement about the a²-coefficient only. Prediction: the a⁴-coefficient of −log|Z| is envelope-DEPENDENT even in any world where γ holds (the toy's Φ-structure shows all-orders-in-a insensitivity is impossible). So at physical leverage a ≤ 0.13 the two envelopes' amplitudes must separate at O(a⁴); a spec must predeclare that this separation is expected and is not evidence against (or for) the a²-identity — and conversely, any claimed all-orders-in-a version of γ is already refuted here.

**(3) Thermodynamic/continuum survival.** Per-cell exactness + volume-uniformity would suffice via the Route-A (Vitali–Cauchy) interchange of `ROUTE_MEMO_2026-07-25_duhamel_intensive_hessian.md` applied to the difference sequence — no new interchange principle. What could break it, in order of severity: (a) the per-cell-to-K gap — multi-cell connected clusters in T7(iii) are NOT controlled by per-cell Hessian identities (the theorem must be K-level); (b) the ER-B chain has no zero-free neighborhood, no linked-cluster density, no (H1)/(H2) — κ_B,K is not even battery-defined yet (see 5.2); (c) the completed amplitude's modulus is small (witnessed 5.9e-4 on the sealed carrier) and nothing sealed prevents it from approaching zero along the exhaustion, where log-derivatives blow up (the V002 division-safety fence is the finite shadow of this); (d) the C2 hypothesis of the Duhamel memo (history-independence of ready injections, PVM, relay isometries) must additionally be envelope-independent — plausible but must be stated as a named hypothesis.

**(4) Proxy vs kappa_record.** Confirmed: the typed statement of Section 1 is against the battery-chain object — the T7(i) completed-record amplitude Z_h(A) = a_h(A)/a_h(0) and its intensive Hessian per T7(iv)/H_K = g_{D,K} — NOT the N=96 Strang/stencil proxy of the executed gate. Additional lemmas the link needs beyond the majorant/interchange machinery already on the books: **(L1)** the per-cell-to-K linked-cluster extension (genuinely new — flagged above); **(L2)** the completed-vs-exhaustive typing: the Duhamel memo's H_K = g_{D,K} as recorded is anchored on the A2 exhaustive closure (Z[A,A] = 1), while kappa_record's Γ is built on the completed amplitude; the γ statement must ride the completed chain end-to-end with the T7(i) normalization supplying the log anchor, and may never substitute the exhaustive object (forbidden by the scope correction and the amendment). So yes — MORE is needed than the majorant machinery, and I flag it loudly: L1 is a new obligation, and L2 is a typing decision that belongs in any spec's frozen definitions.

---

## 4. Negative controls a derivation/refutation spec must include

1. **Envelope-sensitive functional that must NOT be annihilated (teeth):** the single-history amplitude D_{√2}(a) — sealed facts already witness its envelope sensitivity (|ΔZ| = 6.1e-2 pure / 5.7e-3 mixed at a = 0, recorded as context in the V002 gate; per-history a-movement ~1e-10). Any pipeline that "proves" insensitivity for D_{√2} is broken.
2. **Exhaustive/all-outcome kernel:** at coincident histories R_all(a,a) = I is trivially envelope-blind — the control must use the split-history exhaustive kernel Z_all(a,0) = Σ_λ p_λ ω(Γ(u_λ(0)†u_λ(a))): p-weights have m0 = 1 ≠ 0, no cancellation, must show envelope sensitivity. This simultaneously polices the completed/exhaustive substitution fence.
3. **λ-odd positive control:** replace w by first-moment weights (0, −1/(2√2), +1/(2√2)): Lemma 1 predicts EXACT zero at all a, both envelopes — machine-verifiable; failure indicates a broken carrier symmetry, not physics.
4. **a-parity control with teeth:** Z′(0) = 0 must hold at machine exactness (Lemma 2); a predeclared broken variant (b_D center displaced off x = 0, breaking P_x) must produce Z′(0) ≠ 0.
5. **The toy closed form as an executable exact-arithmetic control:** the Section 2.4 model must show κ_A ≠ κ_B symbolically — proving the apparatus can SEE envelope differences (analogue of the V002 review's contact-term-omission control).
6. **Correlated-record (GHZ-style) variant:** only if the battery chain ever uses correlated record factors; the pointer sum then involves w_μ*w_λ products and the second-difference structure changes — out of scope for the current single-qutrit A3 chain; include only as a labeled non-blocking observation.

---

## 5. Adoption watch (Brian-level items, flagged loudly)

1. **Any reparametrization/equal-action/covariance principle** relating the ER-A and ER-B flows would be a NEW principle — and would effectively re-adjudicate the intrinsic-measure selector that `STAGE8_T7_CRITICAL_PATH_SCOPE_CORRECTION_V001.md` section 1 explicitly demoted. Do not let γ resurrect ER selection through the back door. → Brian.
2. **ER-B battery obligations do not exist.** T7(ii)/(iii)/(iv) are sealed on the ER-A disclosed premise; the γ statement needs the ER-B completed amplitude to be zero-free and linked-cluster-dense too. Adding those is a battery-spec change (`STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_AUTHORITY_FABLE_V002.md` pins "ER-B not used and not silently excluded"). → Brian.
3. **Per-cell-to-K multi-cell lemma (L1)** is a new named obligation, not covered by any sealed artifact. → Brian before any spec claims per-cell suffices.
4. **Completed-vs-exhaustive typing of the kappa_record chain (L2):** T7(i) (completed) vs amendment A2 (exhaustive) — the γ spec must freeze which object carries the intensive Hessian, and that freeze is spec-level. → Brian.

---

## 6. Disposition and the single kill-test

Recommended next artifact is NOT a derivation spec for γ. It is a small sealed **refutation gate**: exact symbolic computation of Ξ_A − Ξ_B (equivalently κ_A − κ_B at a = 0, second-order-in-a, all record orders) on the sealed three-site regression fixture, with the Route-1 comparator as cross-check, the Section 4 controls, and the predeclared verdict rule: nonzero ⇒ **gamma dead, beta** (record it and route back to the β conditionality clause); exact zero ⇒ a carrier-specific mechanism exists that this memo did not find, and a mechanism-identification lane must run before any derivation spec is written. Prediction, frozen here per the calibration discipline: **nonzero**. Independent of that outcome, the two parity lemmas (Section 2.2) are exact, cheap to seal, verified against `T07_er_fork_kappa_insensitivity_primary_v001.json` and the executor machinery, and worth sealing regardless — they retroactively harden the executed gate and delete half the stencil error budget in any successor.

---

*Artifacts consumed (all at the canonical cleanroom root unless pathed): DECISION_2026-07-25_er_fork_option_gamma.md; STAGE8_T7_ER_FORK_KAPPA_INSENSITIVITY_RESULT_V001.md; STAGE8_T7_ER_FORK_KAPPA_INSENSITIVITY_BOUND_SPEC_V002.md; stage8_execution/work/T07_er_fork_kappa_insensitivity_{primary,blind_commit}_v001.json; scripts/derive_stage8_t7_er_fork_kappa_insensitivity_primary_v001.py; STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md (A1–A4); STAGE8_T7_CRITICAL_PATH_SCOPE_CORRECTION_V001.md; STAGE8_T7_ENVELOPE_REALIZATION_COMPARISON_SPEC_V001.md; STAGE8_T7_OPERATOR_VALUED_PRIMITIVE_RESPONSE_ARCHITECTURE_AMENDMENT_V001.md; STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_AUTHORITY_FABLE_V002.md (T7/T14, frozen numerics, inherited scope); ROUTE_MEMO_2026-07-25_duhamel_intensive_hessian.md; stage8_execution/work/T07_envelope_realization_comparison_v002.json (structure only). Scratch verification scripts live under scratchpad/gamma_scope/ and touch nothing in the repository.*
