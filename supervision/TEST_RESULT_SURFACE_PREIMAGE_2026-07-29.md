# TEST RESULT — SURFACE PREIMAGE OF THE c_R COUNTERMODELS (2026-07-29)

EXECUTED AGAINST THE PRE-SEALED SPECIFICATION

(sha256 f33e77f156c40c5fc6204a48af6a87d85d49a0b90c1b8ca05c96223b6e35f674), sealed BEFORE launch.
Executed by a DIFFERENT MODEL (Opus) from the reviewer lane, for architectural independence.

VERDICT: UNDECIDABLE FROM THE TEXT — but NOT for the reason the frozen prediction gave.

PREDICTION CHECK, as required by the spec:
 - Main prediction (UNDECIDABLE most likely): RIGHT.
 - Sub-prediction (at least one countermodel bulk/lattice-constructed with no stated surface
   preimage): RIGHT, twice over — the S_0/S_1 Pauli completion and the independent-F^2 cochain
   witness.
 - THE PREDICTION'S STATED REASON WAS WRONG. The spec asserted undecidability would mean the
   countermodels' admissibility was never checked. It WAS checked, repeatedly and deliberately,
   with the result recorded in the authority ledger; and the corpus DOES state an image, twice.
   Undecidability comes from those statements' POSTULATE status and the undelivered L_BR/Q_spec,
   not from silence.

*** THE PRINCIPAL WAS RIGHT THAT PRIOR WORK EXISTS AND REACHED A RESULT. *** It is
PRIMITIVE_TRANSPORT_ONLY_PHASE_COMPLETE_GENERATOR_PRINCIPLE_V001.md (cleanroom, 2026-07-23) —
his reframing already executed: it restricts the admissible class of primitive record
generators so the deformations fall OUTSIDE the class, rather than excluding a bulk term.
Recorded result, CURRENT_AUTHORITY_LEDGER_V010.json:115-116 —
  finite_c_F2_deformation_excluded_inside_adopted_primitive_branch = TRUE
  finite_c_F2_deformation_excluded_as_universal_theorem = FALSE
THIS TEST IS THEREFORE A PARTIAL RE-DERIVATION and is disclosed as such.

Search complete. Writing the report.

---

## STEP 1 — PRIOR WORK: IT EXISTS, AND ITS RESULT GOVERNS. THIS TEST IS A PARTIAL RE-DERIVATION.

The principal was right that a version of this was done before. It was done on **2026-07-23**, it reached a **scoped successful result**, and that result is recorded in the cleanroom's authority ledger. Disclosed as a re-derivation.

**The prior work is `PRIMITIVE_TRANSPORT_ONLY_PHASE_COMPLETE_GENERATOR_PRINCIPLE_V001.md`** (cleanroom). It is exactly the principal's reframing, executed: instead of excluding a bulk term, it restricts the admissible class of primitive record generators, and the deformations then fall outside that class. Lines 43–54:

> `## Excluded primitive mutations` / `The following are not independent terms in the primitive generator:` / `c[A] I                       gauge-history-dependent scalar phases;` / `c_F integral F^2             a bare Maxwell action;` / `ell_* bar(psi) sigma.F psi   a primitive Pauli insertion;` / `higher-covariant-derivative charged vertices;` / `independent Lindblad/dephasing rates;` / `an independently normalized record-curvature term.`

Line 15–18 gives the image-side rule: `At the primitive pre-record level, the compact charged handle enters the microscopic generator only through unit-character parallel transport. Curvature is the failure of composed transports to close; it is not an independent primitive vertex.` Lines 56–58: `Such structures may arise as calculated composite terms of the exact closed transport dynamics. They may not be inserted as microscopic inputs`. Lines 72–75: `It therefore removes the explicit countermodels in COMPLETE_PARENT_ACTION_UNDERDETERMINATION_GATE_V001.md only inside this adopted branch.`

**Its recorded result** — `alpha_fundamental_record_action_cleanroom_v003/CURRENT_AUTHORITY_LEDGER_V010.json:115-116` (latest full execution_state; V011–V013 are deltas naming V010 as `parent_authority`, do not mention transport-only, and do not retire it):

> `"finite_c_F2_deformation_excluded_inside_adopted_primitive_branch": true,` / `"finite_c_F2_deformation_excluded_as_universal_theorem": false,`

That pair is the governing prior answer. It is precisely the structure the spec's second bullet describes — excluded inside the theory, not excluded universally — and the corpus already declines to call it a theorem: `PRIMITIVE_TRANSPORT_ONLY...V001.md:112` `principle_derived_from_older_record_theorems = false`.

**A second, independent prior instance, with a genuinely stated image.** `alpha_prerecord_independent_comparison_measure_principle_v001.md:36-53` excludes the *bare* plaquette weight not by symmetry but by non-membership in the admissible pre-record measure class:

> `A Wilson or plaquette factor` / `exp[beta_0 Re Tr(U_p)]` / `correlates the links around the closed loop p. It is gauge invariant, but for beta_0 != 0 it does not factorize into independent one-link Haar measures. It is therefore absent from the pre-record microscopic measure in this branch:` / `beta_0 = 0.` … `The conclusion follows from pre-record link independence, not from gauge symmetry alone; gauge symmetry by itself permits the term.`

This is a real non-surjectivity argument with a stated image (measures that factorize into one-link Haar marginals). **But it does not reach slot 9.** The corpus says so at `results/alpha_current_gravacle_nonidentifiability_v001.json:62`: `P1+P2 conditionally remove an independent bare plaquette stiffness, but the induced effective Maxwell stiffness remains unidentified.` Slot 9 is the finite counterterm *given* no bare term, which is the residue this argument leaves.

**A third: the criterion itself, stated as a theorem, in the external chain.** `_external_handoffs/fable_alpha_phase_a_construction/SAFE_INPUTS/upstream_results/gravacle_v251_boundary_recoverability_master_theorem.md:406-409`:

> `The same recoverability rule governs the single-handle theorem, the local tomography frontier, and quantum-materials certification: a formal degree of freedom is physical in a declared context only when an admissible boundary can recover it as a record.`

Applied to `c_R`, this cuts against the principal. `c_R` **is** boundary-recoverable: `scripts/audit_alpha_charged_stiffness_counterfamily_v001.py:211` (producer-verified, members hardcoded at `:101` as `Fraction(1), Fraction(2)`) says `Two physically distinct Coulomb coefficients under the same fixed compact` structure, with `Coulomb coefficient 1/(4 pi K)` at `:200`. A changed Coulomb response is recoverable as a record. Under the corpus's own criterion `c_R` is therefore a physical, not merely formal, degree of freedom.

**A fourth, from yesterday and today:** `/Users/bgm/MB Work/alpha_supervision/BOHM_SLOT9_THEORY_ATTACK_2026-07-29.md`, and `.../BOHM_CTP_ABSOLUTE_RESPONSE_ROUTE_SWEEP_2026-07-28.md`. The theory attack already argues the surjectivity-relevant point at `:103`: `the space of admissible local gauge-invariant operators does not shrink to a point when the Hilbert space does` … `Enumeration of admissible local terms in a finite model yields a finite basis with continuous coefficients, which is exactly the wrong kind of finiteness.` And at `:87`: `K_bare = 0 is not a derived property of a complete spectrum; it is the statement that the boundary condition is imposed at the lower endpoint. The floor *is* the subtraction.`

**Bounded negative.** The vocabulary the spec suggested is essentially absent as a description of this question. Searched: (A) cleanroom and (B) parent tree — `rg` over `*.md *.py *.json *.txt *.csv *.tex`, excluding `.proof_deps`, `site-packages`, `sympy`, `.git`, and for the vocabulary sweeps also `external/`, `third_party/`, `sources/` and the duplicated `gravity_em_surface_unification_review_packet_*/`, `gravacle_alpha_cleanroom_review_packet_*/` subtrees (12,608 text files of 47,360 total); (C) `/Users/bgm/MB Work/alpha_supervision` (176 files, all types); (D) `/Users/bgm/Documents/New project/_external_handoffs` (229 files). `/Users/bgm/Documents/New project` was resolved to `Documents - Brian's MacBook Pro/New project` and searched once. Results: **"surjective/surjectivity": zero hits** outside the sealed spec and its relay paste. **"not representable", "ill-formed", "no preimage", "not realizable", "realizability", "outside the admissible": zero relevant hits** — the only "ill-formed" hits concern the CTP `prod_c` display-index (`STAGE8_T7_F8_FIRST_HALF_RESULT_AND_TWO_NEW_FINDINGS_V001.md:41`, `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:411`), and the only "not representable" hit concerns quarter-turn phases (`34_gate1_comparison_group_v001.py:49`). "preimage" appears twice, both mathematically unrelated (Moore–Penrose lift, `stage8_execution/t_reports/T10.json:10`; modular squares, `34_gate1_comparison_group_v001.py:27`). "deformation class" appears once, in today's `STAGE8_SCHUR_RATIO_PROTECTION_SCOPE_ATTACK_V001.md`.

## STEP 2 — THE MAP, AND WHETHER THE IMAGE IS STATED

The corpus specifies M in two legs, and **states an image for each**. The reviewer's expectation that no image is stated was wrong.

**Induced leg.** `alpha_induced_only_boundary_action_principle_v001.md:5-14`: `Before durable public record formation there is no independent bare metric or gauge stiffness. The public action below the first record-forming spectral scale k_R is induced by the same Boundary-Resolved fluctuation operator that supplies the spectral semigroup:` `Gamma_BR,k = -(1/2) integral_(1/k_R^2)^(1/k^2) ds/s STr'_BR exp(-s L_BR).` The image statement is `:21-23`: **`No independent local counterterm may be selected to repair a coupling. A term may appear only as a heat coefficient of the frozen complete BR operator or as a renormalization required by a separately derived public threshold.`** Corroborated at `alpha_coupled_gravity_em_surface_saddle_principle_v001.md:38-41`: `The electromagnetic and gravitational coefficients must be generated by the same target-independent BR operator and supertrace.`

**Primitive leg.** Two independent gradings. Transport-only (quoted above). And `BID_PRIMITIVE_BOUNDARY_SUPERCONNECTION_CLASSIFICATION_V001.md:95-98`: the Pauli term `is therefore degree two in the BID incidence filtration. Adding it as an independent component of D_BR would count a generated two-incidence return as a second primitive operator. It violates the declared degree-one superconnection completeness rule.`

**But the same file says F² is IN the image**, `:112-114`: `Effective Pauli and F^2 terms may then arise from the complete quantum response, but their coefficients are outputs rather than independent primitive inputs.` Independently: `reports/alpha_br_local_u1_induced_continuum_universality_v001.md:11` `The plaquette expansion also matches K_bare=beta`.

So the corpus's own position is: **the F² operator is generated (in the image); what is not in the image is a freely chosen additive shift of its coefficient.** That is a coefficient claim, not a well-formedness claim.

**Why the image is nonetheless not computable from the text.** The image is defined as the heat coefficients of `L_BR` under a proper-time floor, and neither is delivered. `alpha_step5_zero_bare_compositeness_boundary_v001.md:84-87`: `complete_microscopic_record_operator_derived = false` / `physical_record_boundary_scale_derived = false` / `physical_regulator_measure_derived = false`. `CURRENT_AUTHORITY_LEDGER_V010.json:111-112`: `"complete_parameter_free_Q_spec_frozen": false, "unique_causal_record_cell_derived": false`.

And the domain of M is not record data alone. `FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md:88-95`: `Q_spec[g, a, psi, R]` … **`Q_spec must fix fields, action, state, contour, domain, boundaries, gauge/ghost structure, edge modes, measure, regulator, record operator, closure map, branch enumeration, and matching rule.`** The action, measure and regulator are *inputs* to Q_spec. The additive freedom lives exactly in those undelivered slots — which is the theory attack's "the floor *is* the subtraction."

Decisively, the same sealed Level-1 principle **writes the deformation in bulk form and types it as admissible-or-not, never as ill-formed** — `:134-141`: `The route fails to compute the coupling if the completed specification admits an arbitrary finite deformation` / `delta S = -(hbar c/4) integral F wedge *F` / `at the matching scale.` And `:170` `finite_c_F2_deformation_excluded = false`.

## STEP 3 — PER COUNTERMODEL

**(1) Dilation scalar-phase family, `K_c = K_0 + c`** — `alpha_finite_cptp_ctp_record_cell_hostile_analysis_v001.md` §4, `:234-303`.
(a) **Record-side carrier, bulk-local label.** The deformation is attached to the record cell's Stinespring dilation: `U_c[A]=e^{-icX[A]}U[A]` (`:257-259`), where `X[A]=\frac14\int_C d^4x\,\sqrt{-g}\,F_{\mu\nu}F^{\mu\nu}` (`:250-252`).
(b) **A preimage IS stated** — the dilation phase itself, a record-structure datum. The artifact's point is that the channel-level record data *forget* it: `no channel tomography, Kraus normalization, complete positivity, or trace-preservation test can distinguish the family` (`:267-269`), while the CTP functional does.
(c) **Checked, and the check is by postulate.** The artifact states this itself, `:319-321`: **`If K_bare=0 is imposed, the scalar phase family is forbidden only because an additional compositeness/action postulate forbids it. It is not forbidden by the CPTP channel or its kinematic normalization.`** The postulate that names it is transport-only `:48`, `:113` `primitive_F_dependent_identity_phase_allowed = false`. Caveat recorded at `:157-158`: `a curvature scalar requires the full cell support and measure, not only its proper duration` — the preimage needs the cell measure Q_spec has not delivered.

**(2) Pauli-vertex action / S_0–S_1** — `COMPLETE_PARENT_ACTION_UNDERDETERMINATION_GATE_V001.md:38-44`, restated at hostile analysis `:386-399`.
(a) **BULK.** `S_1 = S_0 + hbar ell_* integral d^4x sqrt(-g) bar(psi) sigma^(mu nu) psi F_(mu nu)` — a local Lagrangian density.
(b) **No record-structure preimage is stated.** `ell_*` is a record datum (`gate:16-19`), but the vertex is postulated, not generated. The gate's reopen condition asks for the generating structure it lacks (`:82-88`): `a derived total-space geometric action in which all charged vertices are fixed components of one connection`.
(c) **Checked twice, both adopted.** Transport-only `:50`, `:114` `primitive_Pauli_vertex_allowed = false`; and the degree-two filtration above. The corpus records the type distinction explicitly at `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:2258-2261`: `independent_primitive_F2_axiomatically_disallowed = true` / `independent_primitive_Pauli_axiomatically_disallowed = true` / `primitive_F2_theorem_excluded = false` / `primitive_Pauli_theorem_excluded = false`. Also `STAGE8_LANE_STATUS.md:322`: `The two-completion claim is carried by displayed action/prose algebra and authority flags, not by an executable finite-response producer.`

**(3) Two-channel comparator** — hostile analysis §5, `:323-378`.
(a) **Record-side.** Two distinct comparator channels, `U_{\rm tot}^{(c)}[A]=U_D[A]\otimes e^{-icX[A]Q}` (`:331-336`), `supported on the same unique causal cell; equipped with the same one-Dirac source and no extra species` (`:346-347`).
(b) **Preimage stated** — a comparator channel is a record datum. Again labelled by the bulk-local `X[A]`.
(c) **No admissibility check as a Q_spec.** The separation is stipulated: `The difference is a theoretical countermodel coefficient from Q, the balanced state, and the fixed integer choice c=1` (`:372-374`). Transport-only excludes the carrier by postulate.

**(4) Two synthetic K0 witnesses** — `scripts/audit_alpha_br_induced_only_boundary_provenance_v001.py:298`, verified at producer: `k0_witnesses = (0.0, 1.0)`, stipulated literals, not derived.
(a) **Neither.** Two numbers, with `slope` and `log_interval = 2.0` held fixed.
(b) **No preimage, and the artifact says so** — `reports/alpha_br_induced_only_boundary_provenance_v001.md:17`: **`Physical absolute K: not derived or selected; displayed K values are synthetic countermodels only.`**
(c) No admissibility check. This is a non-identifiability statement about the corpus's principles (`:9` `Nothing in the current record-publicity or Gaussian selector rules eliminates that family`), not a claim about a theory space.

**(5) The independent-F² admissibility countermodel** (not on the spec's list but load-bearing, cited by the slot-9 inventory) — `scripts/audit_alpha_br_independent_f2_counterterm_admissibility_v001.py`.
(a) **LATTICE.** `# Minimal cochain realization of A -> A+d chi and F=dA` (`:50`), integer `d0`/`d1` matrices, `coefficient_a = 0.0` / `coefficient_b = 1.0` hardcoded at `:76-77`.
(b) No preimage; its own scope disclaims one (`:174-179`): `The finite cochain is an executable gauge-invariance witness, not a complete continuum worldtube regulator, a standalone diffeomorphism proof, or a derivation of the physical coefficient.`
(c) Its verdict is the openness: `BLOCKED_INDEPENDENT_F2_COUNTERTERM_ALLOWED_MICROSCOPIC_SELECTOR_REQUIRED`, and `:166-172` `Excluding that term requires a microscopic action, a boundary variational law, or an ultraviolet fixed-point condition beyond the current derived branch structure.` Its ledger status is `CLOSED_BUT_INSUFFICIENT` (`reports/alpha_strict_route_ledger_audit_v001.md:436`).

**The corpus's own general answer to 3(c)**, and it is unambiguous — `SOURCE_RECORD_CLOSURE_ACTION_UNDERDETERMINATION_GATE_V001.md:100-103`: **`This is a local symmetry-level nonselection witness. It is not a pair of complete authority-admissible record theories and therefore is not a full model-theoretic proof that two completed Q_spec constructions survive every later gate.`** With `:123-124`: `two_complete_authority_admissible_closure_actions_constructed = false` / `full_Q_spec_nonuniqueness_proved_by_countermodel_pair = false`.

## STEP 4 — VERDICT: **UNDECIDABLE FROM THE TEXT**

Not for the reason predicted. The corpus states an image twice; it does check admissibility, repeatedly; and it records its answer. What blocks the decision is that **both image statements are self-classified as adopted postulates whose theorem versions are explicitly flagged false, and the operator whose heat coefficients define the image is undelivered.** The corpus's own bar for slot 9 rejects the postulate route as a discharge — `STAGE8_QSPEC_SLOT_DEEP_INVENTORY_V001.md:57`: `Universal exclusion over the open class of response-changing mutations, **by theorem rather than postulate relabeling**.` And its own failure list fires on exactly this move — `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:2135-2136`: `an F^2 or Pauli term is declared theorem-excluded only because completeness postulated it away`.

**What would have to be written.** (i) The frozen `L_BR` / the Q_spec entries `measure, regulator, record operator, cell support` — the image is their heat coefficients and nothing else. (ii) The theorem versions: `primitive_F2_theorem_excluded` and `primitive_Pauli_theorem_excluded` (`V011:2260-2261`) turned true over the open class. (iii) The corpus's own named test, which *is* the surjectivity question — `alpha_step5_absolute_response_identifiability_v001.md:79-81`: `To upgrade the argument to a regulator-realization theorem would require two explicit admissible regulator/measure constructions and their full boundary Ward and symplectic reductions`, currently `:102` `explicit_regulator_pair_realizing_arbitrary_c_R_constructed = false`. Note the asymmetry: discharging (iii) positively proves SURJECTIVE; failing to construct such a pair proves nothing. (iv) The Phase-A obligation, which is non-surjectivity in the corpus's own words, posed as a thing to be proved — `_external_handoffs/.../PREREGISTRATION_V002.md:137-139`: `every admitted regulator/measure/boundary realization gives the same value; no independent polynomial, contact, Jacobian, reference, or local F^2 term is admissible.`

**Per countermodel — freedom in the surface theory, or only in a larger theory?**

| Countermodel | Verdict |
|---|---|
| Dilation scalar-phase family | **Survives in the surface theory.** Its carrier — the phase of the record cell's unitary dilation — is a record-formalism object, and the text exhibits it. Inside the transport-only branch it is excluded, by a postulate that names it. Restriction by adoption, not non-representability. |
| Two-channel comparator | **Survives in the surface theory**, same ground: comparator channels are record data. Its numerical separation is stipulated. |
| Pauli vertex / S_0–S_1 | **Only in a larger theory.** Bulk Lagrangian density, no stated record preimage. But the corpus says the *operator* is generated (`BID...:112-114`), so the exclusion is of the independent input, not of the term. |
| Two synthetic K0 witnesses | **Neither.** Stipulated literals. They demonstrate non-identifiability of the corpus's principles, not freedom in any theory — the producing artifact says so. |
| Independent-F² cochain witness | **Only in a larger theory** — a lattice construction, self-disclaimed as not a continuum or surface object. |

## STEP 5 — GUARD

**My verdict does distinguish "ill-posed in my preferred language" from a refusal to face the problem, and the test that distinguishes them is concrete:** for each countermodel, ask whether the object that *carries* the deformation is a datum the record formalism can hold. For the dilation-phase family and the two-channel comparator it plainly is — a Stinespring dilation and a comparator channel are record objects, and the deformation is a phase on exactly those, exhibited in the corpus's own text at `alpha_finite_cptp_ctp_record_cell_hostile_analysis_v001.md:257-259` and `:331-336`. The counterterm is therefore **a well-formed object of the record formalism in at least two of the five countermodels.** It is removed by a rule that names it and declines to call itself a theorem. That is exclusion-by-postulate — the refusal shape — not ill-formedness.

I did not infer NOT SURJECTIVE from any absence of a translation, and I report the one place where a genuine image characterization with a real argument does exist (product-Haar factorization) together with the corpus's own statement that it does not reach this object.

Two further checks against the refusal shape. First, the corpus's own recoverability criterion (`gravacle_v251...:406-409`) makes `c_R` physical, because the K=1/K=2 witnesses `chang[e] the Coulomb response` (`reports/alpha_strict_route_ledger_audit_v001.md:473`) — a boundary-recoverable difference. Second, the theory attack's finite-model argument (`BOHM_SLOT9_THEORY_ATTACK_2026-07-29.md:103`) with the corpus's spin-ice witness (`reports/alpha_target_free_finite_u1_route_audit_v001.md:152-184`, an external lattice model, so an analogy rather than a Gravacle preimage) says a finite record structure still yields a finite operator basis with continuous coefficients.

## PREDICTION CHECK

**Main prediction: RIGHT.** UNDECIDABLE FROM THE TEXT, as the reviewer expected was most likely.

**Sub-prediction: RIGHT, twice over.** The S_0/S_1 Pauli completion is a bulk `integral d^4x sqrt(-g)` Lagrangian density with no stated surface preimage; the independent-F² admissibility witness is an explicit lattice cochain construction, self-disclaimed.

**The prediction's stated *reason* was wrong.** The spec's third bullet asserted that undecidability `would mean the countermodels' admissibility as Gravacle theories was never checked`. It was checked — repeatedly, deliberately, and with the result recorded at `CURRENT_AUTHORITY_LEDGER_V010.json:115-116`. The corpus also states an image, twice. Undecidability comes from the postulate status of those statements and the undelivered `L_BR`/`Q_spec`, not from silence.

**Fences honored.** Read-only; no file written, edited, or created anywhere. No computation of alpha, `kappa_record`, `kappa_Thomson`, `c_R`, `x`, `rho`, `T_R`, any coupling, root, or scale; no comparison to any measured constant. Vendored directories `.proof_deps`, `site-packages`, `sympy` excluded from every sweep, as were `external/`, `third_party/`, `sources/` and duplicated review-packet subtrees for the vocabulary sweeps. On the `C_R` collision: I relied on no `C_R` claim in either sense, and note that the only `C_R` I encountered — `BOHM_SLOT9_THEORY_ATTACK_2026-07-29.md:69` — is the parent-tree induced Einstein coefficient, not the cleanroom compactness ratio.