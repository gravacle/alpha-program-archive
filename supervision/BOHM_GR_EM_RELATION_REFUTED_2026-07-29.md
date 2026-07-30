# GR-EM PARAMETER-FREE RELATION — REFUTED (2026-07-29)

Adversarial check of a reviewer synthesis, run with the default set to refute. VERDICT: the
parameter-free relation DOES NOT EXIST. The argument dissolves at step S4, exactly where the
reviewer flagged it as most likely to break.

REVIEWER ERROR, RECORDED: the argument assumed the record interval T_R is the inverse of the BR
record scale k_R, so that k_R cancels in T_R/t_P. That identification is the specific move the
corpus PROHIBITS ("Adoption by dimensional analogy is foreclosed; only derivation can reopen
it"). T_R is a pure scale-orbit parameter under which ALL dimensionless data are invariant, so
it cannot be a function of x at all. This is the sixth reviewer over-reading corrected today by
a check the reviewer ordered.

TWO FINDINGS THAT MATTER INDEPENDENTLY OF THE ERROR — see the body:
 1. A SYMBOL COLLISION ON C_R between the two trees (cleanroom: a compactness ratio set to 1 at
    marginality, which is what fixes T_R; parent: the induced Einstein coefficient C_R(x)).
    Same symbol, unrelated objects. This is what made the error easy and it will bite anyone.
 2. THE OFFSET IS NOT THE BINDING OBSTRUCTION; THE ACTION FORM IS. Two parameter-free
    completions of the parent action exist (differing by a Pauli term), BOTH with K_bare = 0,
    giving DIFFERENT finite responses — and the gate says so explicitly: "This is not the
    ordinary finite-c_R F^2 counterterm objection. It survives even after an independent bare
    Maxwell term is forbidden."

## Verdicts

**S1. POWER COUNTING — SURVIVES (with an audit caveat).**

Verified verbatim at `/Users/bgm/Documents/New project/gravity_emergence_evidence_program/reports/alpha_br_common_induced_coefficients_v001.md` (lines 12–20) and at the producer `/Users/bgm/Documents/New project/gravity_emergence_evidence_program/scripts/derive_alpha_br_common_induced_coefficients_v001.py` (lines 326–336, where the same text is emitted as literal strings):

```
k_R^4 C_V(x)  -  k_R^2 C_R(x) R  +  (1/4) K_Q(x) F_Q^2
```

The gauge coefficient carries no explicit `k_R` factor. Confirmed. In the producer, `coefficient_data(x)` takes only `x`; `k_R` appears nowhere in the numerics, and the CSV values are genuinely computed from `i_n()` integrals, not hardcoded.

Caveat that matters: the PASS flag `PASS_COMMON_BR_LOCAL_COEFFICIENT_FUNCTIONS_DEPTH_OPEN` certifies only the trace inventory (dim 16, TrQ²=16/3), positivity, derivative recurrences, and monotonicity (producer lines 197–297). **No assertion in the script tests the `k_R` power assignments** — they are hand-written prose in the markdown writer. The power counting is correct standard heat-kernel dimensional analysis, but it is not executed content, and the report's PASS does not certify it.

**S2. INFORMATION ASYMMETRY — SURVIVES on the narrow claim, REFUTED as the argument uses it.**

The narrow claim survives, and I found the mechanism that makes it true. `alpha_induced_only_boundary_action_principle_v001.md`, "Record-floor normalization": *"The common spectral scale is absorbed into dimensionless proper time `tau=s k_R^2`."* The floor sits at `s = 1/k_R^2` by definition, so no independent cutoff scale enters; the `k_R^{4,2,0}` prefactors are just the dimensions of `I_{3,2,1}`. The normalization report confirms the same: *"the explicit massless check uses `integral ds/s=log(k_R^2/k^2)`."* Nothing hides in the measure or in `F_Q` (the ledger types `[F_mu_nu]=L^-2`, `[K]=1`).

But the corollary the argument needs — that `K_Q` is a function of `x` **alone** — is false. Strict ledger row 125: *"the induced parent coupling depends only on `W_ch=N_g[(1/3)E1(x_5bar)+E1(x_10)]` but current BR rules do not output its mass determinant or `N_g`"* (status BLOCKED). The gauge coefficient is `N_g` × function of `x`, and the ledger keeps **two** thresholds where the reviewer assumes one.

**S3. PLANCK SCALE AS OUTPUT — REFUTED.**

The corpus's Einstein normalization is non-reduced and treats `l_P` as an input: `alpha_complete_dimension_convention_ledger_v004.md` writes `S_grav,D = -hbar/(16 pi l_P^2) { integral_M sqrt(-g) R ... }`. Nowhere does any artifact match this against `k_R^2 C_R(x)`. I grepped the whole tree for `C_R` co-occurring with G/Newton/Planck: zero hits of any such identification.

Decisive status flag, `results/joint_matter_em_gravity_hessian_identifiability_v001.json`: `"gravitational_normalization_computed": false`, with `"common_induced_coefficients_are_not_derived": true` and blocker *"the common induced supertrace coefficients and global saddle remain open."*

On the earlier finding: it does **not** contradict S3, but it is **not merely a diagnostic artifact** either — it is the universal pattern. The prior verified adjudication records: *"the Newtonian-limit family is 75 versions (not 67) and never computes G from any spectral object — G is a primitive calibration constant in every version."* The artifact in question is `results/alpha_br_replacement_einstein_maxwell_covariant_hessian_v001.json`: `"ordinary_action": "sqrt(g)[-2 R + 4 Lambda + (K/4) F_mu_nu F^mu_nu] with kappa=1 canonical gravity coordinates"` — gravity normalized away by coordinate choice while `K` stays symbolic (sampled 0.8, 1.4, 2.0). Additionally `reports/alpha_eh_subspace_invariance_v001.md` returns `NO_GO_EINSTEIN_HILBERT_SUBSPACE_NOT_HEAT_FLOW_INVARIANT`: *"the exponential Einstein-Hilbert fixed point is a diagnostic truncation, not an exact Boundary-Resolved gravity product."* The truncation required to read a Planck scale off the two-derivative coefficient is itself flagged non-invariant. S3 is an available structural reading of one artifact; it is not the corpus's state.

**S4. THE T_R ≈ 1/k_R BRIDGE — REFUTED. Ruling: DIFFERENT OBJECTS, NO BRIDGE.**

This is where the argument dies. The decisive file is `/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/BID_ABSOLUTE_RECORD_SCALE_IDENTIFIABILITY_GATE_V001.md`, lines 54–61:

> *"The current record kinematics do not identify one SI value of `T_R`. The allow/require rule fixes the first completed action interval, not an absolute clock duration, unless an additional dimensionful part of the same parameter-free dynamics breaks this scale orbit. The existence of the Planck time does not by itself select `T_R=t_P`. Such an identification must follow from the coupled gravity-source-record saddle or another target-independent stationary condition."*

with flags `positive_scale_orbit_exists = true`, `first_opening_data_break_scale_orbit = false`, `absolute_SI_record_duration_derived = false`. `T_R` is a pure scale-orbit parameter: under `T_R' = lambda T_R, H_R' = H_R/lambda` **all dimensionless data are invariant** (lines 24–50). An object whose defining construction leaves every dimensionless quantity invariant cannot be a function of `x`. Setting `T_R = const/k_R` is precisely the "additional dimensionful part... breaks this scale orbit" that the gate flags as absent.

The two objects are constructed in disjoint namespaces. `k_R` is fixed (conditionally) in the parent tree by `N_BR(k_R)=1`, `lambda_0(D_BR^2)=k_R^2` (`alpha_first_durable_record_capacity_principle_v001.md`). `T_R` is fixed in the cleanroom by the compactness marginality `C=1, R=c T_R/2, |Delta S_record|=s hbar`. Confirming the earlier check: `k_R` has exactly one substantive occurrence in the entire cleanroom (a citation to the parent report in the STAGE8 binding) plus one sympy hash substring; the `_external_handoffs` tree has **zero** `k_R` files and many `T_R` files.

I also found the likely root of the error — a **namespace collision on `C_R`**. In the cleanroom, `BID_MINIMAL_PUBLIC_CAUSAL_CELL_DERIVATION_V001.md` line 43 defines `C_R = 2 G E_R / (c^4 R_R) <= 1` — a *compactness ratio* set to 1 at marginality. In the parent, `C_R(x) = sum_a d_a I_2(x+C2_a)/(192 pi^2)` — the *induced Einstein coefficient*. Same symbol, unrelated objects, and it is the cleanroom `C_R=1` that fixes `T_R`.

Three further independent bars. The STAGE8 binding: *"The following are three independent scale obligations and must not be collapsed: x ... rho ... T_R"*, with `x_computed = false`, `T_R_computed = false`. The same binding's S4 authority mechanism: *"Adoption by dimensional analogy is foreclosed; only derivation can reopen it"* — `T_R ~ 1/k_R` is exactly a dimensional analogy. And the binding admits the parent report *"as citation surface only... Its premise set is not imported"* — so S1–S3 rest on an artifact the cleanroom has deliberately not imported.

Finally, the corpus's own only attempt at this ratio goes through `t_P`, not `k_R`: `T_R=2 sqrt(pi) t_P` vs `T_R=sqrt(2pi) t_P`, split by an unresolved Misner-Sharp/Brown-York energy choice (`energy_choice_changes_T_R_by_sqrt_2 = true`). The prior verified adjudication: *"F(T_R/t_P)=0 has exactly one construction attempt (conditional T_R = 2*sqrt(pi)*t_P, blocked by a sealed sqrt(2) energy ambiguity)"* and *"the specific two-log-coefficients-cancel-in-the-ratio mechanism is engaged NOWHERE (bounded zero across all three roots)."*

**S5. THE RELATION — REFUTED (moot after S4, and independently false).**

Even granting S4, elimination does not give a parameter-free relation. Three hidden parameters, each corpus-flagged:

- `N_index`/`N_g`. `reports/alpha_superconnection_finite_mass_spectrum_v001.md`: `W_ch = N_index (4/3) E1(r^2/k_R^2)`, and *"Neither `r/k_R` nor `N_index` may be selected from the measured fine-structure constant."* Row 125 is BLOCKED on exactly this. It enters the gauge coefficient multiplicatively, so it survives elimination of `x` as a second unknown.
- The whole functional form, not just a constant. `COMPLETE_PARENT_ACTION_UNDERDETERMINATION_GATE_V001.md` exhibits two parameter-free completions `S_0` and `S_1` (Pauli term `hbar ell_* bar(psi) sigma^(mu nu) psi F_(mu nu)`), both with `K_bare=0`, giving different finite responses: *"This is not the ordinary finite-`c_R F^2` counterterm objection. It survives even after an independent bare Maxwell term is forbidden."* Flags: `complete_parent_action_uniquely_derived = false`, `finite_response_evaluation_authorized = false`.
- Thomson matching. Row 515 BLOCKED; the coupled-bundle gate lists *"threshold matching to the Thomson limit"* as an open condition.

Note also that the corpus's other cross-sector ratio is a function of a *different* scale entirely — `alpha_tree = 4 ell_P^2/R^2` awaiting `rho = R_*/ell_P` — one of the three obligations that must not be collapsed with `x`.

**S6. THE OFFSET — REFUTED as reasoning, though its asymmetry premise is CONFIRMED.**

The asymmetry is real and I confirmed it at source. `alpha_strict_route_decision_ledger_v001.csv` row 429:

> *"fresh_gravity_em_normalization_identifiability_v001,BLOCKED,gravity_match_does_not_remove_additive_K0,"hostile review confirms the replacement 45-Weyl carrier gives the proper-time Einstein coefficient N_W/(192 pi-squared) and EM logarithmic slope TrQ-squared/(12 pi-squared), but countermodels with the same gravity coefficient regulator and EM slope retain different additive Maxwell stiffness","do not infer absolute EM normalization from G..."*

So an admissible deformation does touch `F^2` while holding the Einstein coefficient fixed. The "both sectors carry an offset, so two free constants" worry is **not** what the corpus admits — the exhibited countermodel class holds gravity fixed. To that extent the reviewer's premise is right and my instructed suspicion is wrong.

But the conclusion does not follow. `CURRENT_AUTHORITY_LEDGER_V010.json` lines 115–116: `"finite_c_F2_deformation_excluded_inside_adopted_primitive_branch": true`, `"finite_c_F2_deformation_excluded_as_universal_theorem": false`. Inside the adopted branch the offset is **excluded**, so there is no offset to make the relation a test; outside it, there is no derived relation to test. Either way S6's dichotomy has no referent. And `alpha_induced_only_boundary_action_principle_v001.md` forecloses the framing at the premise level: *"Before durable public record formation there is no independent bare metric or gauge stiffness"* — both sectors — and *"No independent local counterterm may be selected to repair a coupling."*

**THE CRUX — the reviewer is WRONG; the corpus's accounting is RIGHT.**

The reviewer equivocates between two different statements. The corpus's *compositeness* premise is `K_bare = 0`, a statement about the microscopic Lagrangian. The statement equivalent to `c_R = 0` is the *stronger* boundary-normalization condition `K_R(Lambda_R)=0` at a derived physical boundary. The corpus separates these deliberately and executes a discriminator on each:

- Independence direction, `alpha_step5_absolute_response_identifiability_v001.md`: *"`K_bare=0` forbids inserting a microscopic trial Maxwell term. It does not by itself choose the finite part of a divergent induced determinant."*
- Linkage direction, `alpha_step5_zero_bare_compositeness_boundary_v002.md`: *"Any additive finite mutation `Pi_T(k) -> Pi_T(k)+c_R` cancels in this difference. This removes the additive ambiguity algebraically **once the physical boundary construction exists; it does not derive that construction**."* — with `physical_boundary_assumptions_derived = false`, `zero_bare_compositeness_condition_derived = false`.

So the linkage the reviewer asserts exists only as conditional algebra downstream of an underived construction. Two further quotes kill the identification outright. The strict-route ledger on the very principle that imposes the condition at `k_R`: *"the historical K(k_R)=0 sentence was not derived by that file"* (status CLOSED_BUT_INSUFFICIENT, with *"derive the non-Abelian and continuum realization before using the boundary condition in a coupling computation"*). And decisively, row 429's countermodels share *"the same gravity coefficient **regulator** and EM slope"* while differing in `K0` — the offset freedom survives at **fixed** regulator. That refutes "the offset and the depth are linked through where the boundary sits" directly: the corpus exhibits offset freedom with the boundary held fixed, so the offset is not the floor-location freedom. Corroborating, `induced_only_boundary_provenance_v001` is **BLOCKED** with decision `additive_K0_not_selected`: *"two synthetic K0 witnesses with identical compact U1 character lattice one-loop selector and local Delta-K but different absolute K."*

There is also a structural point in the corpus's favour that the reviewer's own framing misses: the floor location is a *single* object. Moving it off `1/k_R^2` perturbs `I_1` and `I_2` together, so if the offset really were the floor freedom it would move both sectors and could not produce the S6 asymmetry at all. The asymmetry that does exist (row 429) is a different, regulator-independent freedom.

## Overall verdict

**The parameter-free relation does not exist.** The argument dissolves, and it dissolves at S4, exactly where flagged.

The chain fails structurally, not just evidentially. S1 survives. S2 survives only in its narrow routing claim. S3 is an unexecuted structural reading. S4 is false: `T_R` and `k_R` are objects in disjoint constructions with disjoint namespaces, joined by no derived bridge, and the corpus explicitly forecloses joining them by dimensional analogy while flagging them as two of three obligations that must not be collapsed. Without the bridge, `k_R` does not cancel, `T_R/t_P` is not a function of `x`, and there is no second equation to eliminate `x` against. S5 and S6 are then moot, and both fail on their own terms anyway.

This has the shape the brief predicted. The hopeful direction here was supplied by an assumed identity (`T_R ~ 1/k_R`) that the corpus names as a specific prohibited move, and it was made easy by a real symbol collision on `C_R` between the two trees.

## What would have to be true

Precisely the closure condition the corpus already writes down, `BID_ABSOLUTE_RECORD_SCALE_IDENTIFIABILITY_GATE_V001.md` line 72: a Lorentz-scalar equation `F(T_R/t_P, dimensionless branch data)=0` with one isolated positive stable solution, derived from *"the complete parameter-free parent."* Note that the reviewer proposed the right *shape* and then supplied it by assumption instead of derivation. Specifically it would take, in order:

1. One action containing both sectors, so that `T_R`'s scale orbit is broken by the same dynamics that generates `C_R` — i.e. `first_opening_data_break_scale_orbit` flipped true by derivation, not by identifying `T_R` with `1/k_R`.
2. An executed match of the induced Einstein coefficient to the gravitational normalization, flipping `gravitational_normalization_computed`, and a decoupling theorem answering the `NO_GO_EINSTEIN_HILBERT_SUBSPACE` result — without which no Planck scale is an output.
3. An index theorem fixing `N_index`/`N_g`, else the eliminated relation carries a second unknown.
4. Exclusion of the Pauli completion and equivalent mutations *before* response evaluation (`COMPLETE_PARENT_ACTION_UNDERDETERMINATION_GATE_V001.md` reopen conditions) — the offset is not the binding obstruction; the action form is.
5. Resolution of the `sqrt(2)` Misner-Sharp/Brown-York energy ambiguity, which currently splits `T_R/t_P` two ways before any `x` enters.

One route-class warning worth carrying forward: ledger row 517 records `primitive_boundary_native_alpha_postfreeze_comparison_v001` as **REJECTED**, a prior instance of this same shape — a parameter-free coupling produced from a proper-time floor convention plus a matching choice — preserved as a negative result with no residual repair authorized. The corpus has run this route class before.