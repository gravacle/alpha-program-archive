# Stage 8 Standing-Premise Test Classification v001

Date: 2026-07-30

## 0. Controlling result

**Seventeen of twenty-six independently classified, status/test-bearing
value-path premise classes in the bounded, supersession-aware inventory are
UNTESTED. Nine are
TESTED in the Q-37 sense: a premise-specific falsifier, countermodel, gate, or
holdout can genuinely fail.**

The count is a conservative lower bound, not a claim that the corpus has
sealed an exhaustive premise universe. The current register-completeness audit
says:

`STAGE8_REGISTER_COMPLETENESS_AUDIT_CONTINUATION_V001.md:247-252`

```text
ledger_scope_decision_needed = true
```

Accordingly:

```text
COUNTING_UNIT =
  ONE_STATUS_AND_TEST_EQUIVALENT_PREMISE_CLASS
CLAUSES_WITH_THE_SAME_SEALED_STATUS_AND_THE_SAME_TEST_MAY_SHARE_ONE_CLASS = true
CLAUSES_WITH_DIFFERENT_EPISTEMIC_STATUS_SPLIT = true
MIRRORS_DUPLICATE_FLAGS_AND_DOWNSTREAM_CONSEQUENCES_COUNTED_AGAIN = false
LATER_SUPERSESSIONS_APPLIED = true
VALUE_PATH_PREMISE_CLASSES_CLASSIFIED_IN_BOUNDED_INVENTORY = 26
VALUE_PATH_TESTED = 9
VALUE_PATH_UNTESTED = 17
EXACT_CORPUS_WIDE_STANDING_PREMISE_COUNT_SEALED = false
```

This prevents arbitrary atomization of a compound adoption whose clauses carry
the same sealed status and the same test, while splitting a compound source
branch where its clauses have different epistemic status. In particular:

- primitive one-pair **minimality** is UNTESTED;
- exhaustive use of a one-source branch is separately TESTED by the complete
  charged-spectrum and threshold gate.

That distinction prevents a downstream spectrum gate from being misreported
as a test of primitive minimality.

The priority results are:

```text
C_R_EQUALS_1 = UNTESTED
K_BARE_EQUALS_0 = TESTED_PENDING
TRANSPORT_ONLY_MUTATION_EXCLUSION = TESTED_PENDING
ER_A = UNTESTED
A6_PURE_SELECTOR_SITES = 5_UNTESTED
A6_MIXED_PAIR_COUNT_COMPONENT = UNTESTED
DCC = UNTESTED_UNDEFINED_IN_BOUNDED_ROOTS
TAU_ORTH_EQUALS_T_R = UNTESTED_REGISTER_ONLY_CONDITIONALITY
```

No tested premise is reported as proved. `TESTED` means that a real
failure-capable test is attached. Its execution state is reported separately.

## 1. Classification rule and current authority

Q-37 states at
`/Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md:1571-1590`:

```text
one adopts a hypothesis in order to test it — the adoption is what makes the
thing falsifiable. A premise never stated is a premise never refutable.
...
EVERY ADOPTION CARRIES ITS TEST, OR IS MARKED UNTESTED.
```

Q-38 demonstrates the distinction at
`QUESTIONS_SETTLED_REGISTER_V001.md:1614-1638`:

```text
F-RP1 FIRED ON THE FIRST CONSTRUCTION TURN. THE ADOPTION LAPSES BY ITS OWN
TERMS.
```

Later-authority check: Q-40 does not revive that premise. The register says at
`QUESTIONS_SETTLED_REGISTER_V001.md:1738-1739`:

```text
DOES NOT: reinstate Q-37's lapsed adoption
```

Q-41 narrows the diagnosis but leaves the root flag false at `:1745-1757`:

```text
ROOT_DERIVED                 = false
PRODUCER_FLAG_FLIPPED        = false
F_RP1_STANDS_NARROWED        = true
```

Q-42 originally said at `:1792-1805`:

```text
SEALED TEXT DOES NOT SAY.
...
THE JOIN — NOT TYPED.
```

Q-43 later narrows that statement at `:1830-1858`:

```text
THE BASE COMPOSITION IS TYPED.
...
WHAT REMAINS — Q-42 NARROWED TO: the complete source-record-field CTP
producer
...
NO PRODUCER FLAG FLIPPED.
```

These later rulings derive and narrow construction status; they add no
standing adoption to this inventory and do not change the count. The Q-37
root premise remains lapsed and is excluded in Section 10.

This audit applies the following mechanical interpretation.

### TESTED

A premise is `TESTED` if sealed or frozen text attaches at least one of:

1. a falsifier whose occurrence rejects or lapses the premise or branch;
2. an executed countermodel that can reject it;
3. a named gate whose failure leaves the premise unusable or conditional; or
4. a holdout explicitly assigned to earn or reject that premise.

The test need not already have run. The table distinguishes `PENDING`,
`PARTIAL`, and `EXECUTED`.

### UNTESTED

The following do not count:

- a script that reuses the premise as an input and checks its algebra;
- a hard-coded status assertion;
- a generic downstream obligation with no premise-failure rule;
- a no-retuning rule without a named test;
- a statement that a reviewer may reject the premise;
- a control rejected only because the premise itself excludes it; or
- a check that cannot return evidence against the premise.

This implements the instruction that a test which cannot fail is UNTESTED.

## 2. Roots, exclusions, and bounded method

The roots were:

```text
C   = /Users/bgm/Documents/New project/gravity_emergence_evidence_program/
      alpha_fundamental_record_action_cleanroom_v003
S   = /Users/bgm/MB Work/alpha_supervision
A_W = /Users/bgm/MB Work/alpha-program-archive/workspace
A_S = /Users/bgm/MB Work/alpha-program-archive/supervision
P   = /Users/bgm/Documents/New project/gravity_emergence_evidence_program
```

`A_W` and `A_S` were inspected only to expose mirror duplication. `P` excluded
its nested `C` subtree.

Every search excluded before descent:

```text
all protected holdout and custodian subtrees;
.git;
.proof_deps;
.python_deps and versioned variants;
node_modules;
review_packets;
stage8_execution;
and, in P, papers, raw, extracted, data, runtime_snapshots, and nested C.
```

Lane-1 construction artifacts in the `Gamma_K`, joint-selector, CAR/GNS,
covariance-route, measure, and namespace families were excluded from
construction use. Historical CAR-named selector material was not read as
primary evidence; its status is quoted only through the sealed split
correction and V011 competitor classification. Standing-premise authority
files were read only where the present task explicitly required their status
and falsifiers. Nothing in Lane 1's write scope was edited.

Filename lists were emitted with NUL delimiters and converted only for display.
No path list was piped into a second search and no `xargs` was used.

The inventory spine was the union of:

```text
CURRENT_AUTHORITY_LEDGER_V010.json
CURRENT_AUTHORITY_LEDGER_V013.json
STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.md
STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.json
STAGE8_T7_BETA_ER_A_DISCLOSED_PREMISE_ADOPTION_V001.md
STAGE8_ALLOW_REQUIRE_MINIMALITY_SPLIT_CORRECTION_V001.md
STAGE1_PREMISE_DISPOSITION_V001.md
BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md
/Users/bgm/MB Work/alpha_supervision/AXIOM_SET_MAP_2026-07-29.md
/Users/bgm/MB Work/alpha_supervision/
  RECOVERY_STIFFNESS_AND_ALLOW_REQUIRE_2026-07-29.md
/Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md
```

`CURRENT_AUTHORITY_LEDGER_V013.json:9-17` explicitly inherits V010. V010 lists
four current Level-1 postulates at `:25-30`; V013 adds two at `:31-34`:

```text
"relative_record_onset_saturation"
"zero_flux_no_charged_write"
```

The cumulative register is not treated as automatically current because it
still lists items later retired or retyped. Those dispositions are reported in
Section 10.

## 3. Classification table — 26 value-path premise classes

`SEALED STATUS` in this table means an exact machine flag when the governing
source has one. For an older sealed source without a status block, the table
quotes the exact status heading or sentence as a `PROSE_STATUS`; no
machine-readable flag is inferred.

| # | Premise and sealed status | Q-37 class | Specific test or exposing route |
|---|---|---|---|
| 1 | **`C_R = 1`, marginal public closure.** `BID_MINIMAL_PUBLIC_CAUSAL_CELL_DERIVATION_V001.md:49-60`: “Marginal public-closure rule (adopted Level-1 Gravacle rule)” and “This fourth input is the selector.” Flags at `:162-167`: `marginal_public_closure_rule_adopted_Level_1 = true`, `absolute_record_interval_derived_in_declared_branch = false`, `strict_untrapped_inequality_alone_selects_unique_scale = false`. | **UNTESTED** | The producer takes the compactness threshold as an argument and the result says `"physical_premise_proved_by_script": false` (`results/bid_minimal_public_causal_cell_v001.json:59-64`). `DEPARTURE_2_RESCALING_EXCLUSION_FOUR_CHANNEL_AUDIT_V001.md:85-101` names a possible forcedness audit but says “NOT YET AUDITED AGAINST THIS REQUIREMENT.” No physical falsifier is frozen. |
| 2 | **`K_bare = 0`, induced-only.** `FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md:121-132`: “This is an adopted compositeness condition, not a result of compactness, projective geometry, or gauge covariance.” Flags at `:167-170`: adopted `true`; finite deformation excluded `false`. | **TESTED — PENDING** | Short of Slot 18, `:134-141` says the route fails if the completed specification admits an arbitrary finite deformation. `PRIMITIVE_ADDITIVE_RECORD_FIDELITY_ACTION_V002.md:135-159` makes finite deformation and unused-prediction failure hard branch failures; the gate remains false. Q-18 separately assigns Slot 18 to earn this premise (`QUESTIONS_SETTLED_REGISTER_V001.md:781-786`). Neither test has passed. |
| 3 | **Transport-only / Single-Operator Completeness.** `PRIMITIVE_TRANSPORT_ONLY_PHASE_COMPLETE_GENERATOR_PRINCIPLE_V001.md:5-7`: “new Level-1 Gravacle principle” and “not claimed as a theorem”; flags `:110-118` adopted `true`, derived `false`. | **TESTED — PENDING** | V011 `:1084-1092`: “If an additional primitive response coefficient is required, Single-Operator Completeness fails as a physical hypothesis.” Stop rules `:2134-2136` also fail if an independent magnitude survives or theorem exclusion merely restates the postulate. The theorem-exclusion flags remain false at `:2257-2263`. |
| 4 | **ER-A.** `STAGE8_T7_BETA_ER_A_DISCLOSED_PREMISE_ADOPTION_V001.md:18-27`: “NOT derived and NOT selected — assumed”; ER-B “remains UNEXCLUDED.” Flags `:103-108`: adopted `true`, ER-B excluded `false`, derived `false`, fork closed `false`. | **UNTESTED** | The prior kill-test “blocked on CONTROL DESIGN, not on physics” (`:11-14`). The finite-lane result selected nothing. The corpus identifies an exposing route—derive the write-rate from the record principle—but says it is “explicitly NOT opened” (`:88-98`). |
| 5 | **Minimal public carrier, `d = 4`.** `minimal_public_carrier_principle_v001.md:3-18,32-45`: `PROSE_STATUS = “Adopted principle”`; a derived lower bound is followed by “The Minimal Public Carrier Principle selects the lower bound.” | **UNTESTED** | The condition that any extra primitive state encode another independent public distinction is motivation, not a frozen test. No failure-capable dimension/carrier comparison is attached. |
| 6 | **Relative budget saturation.** `BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md:97-108`: “Saturation is adopted, not derived.” Flags at `:181-184`: `relative_onset_saturation_derived = false`, `relative_onset_saturation_adopted_Level_1 = true`. V013 `:31-33,55-58` records it as a Level-1 postulate and says `physical_dynamical_action_fixed = false`. | **UNTESTED** | Its “Exact next gate” at `:168-173` is a construction obligation, but it contains no premise-failure criterion. A derived durable onset which does not saturate would expose it; that test is not frozen. |
| 7 | **Proper-time floor `tau = 1`.** The split correction `STAGE8_ALLOW_REQUIRE_MINIMALITY_SPLIT_CORRECTION_V001.md:68-69` calls it a “frozen branch convention, not a theorem.” `STAGE8_OPERATOR_FLOOR_BOUNDARY_CHAIN_CANDIDATE_DERIVATION_V001.md:198-209` records `proper_time_floor_status = ADOPTED_BY_INDUCED_ONLY_FUNCTIONAL`. | **UNTESTED — COMPETITOR OPEN** | V011 `:1094-1105` admits the complete positive-`tau` competitor family and says neither the unit interval nor unit amplitude power follows. No premise-specific test selects the unit member. |
| 8 | **Primitive spin `1/2` minimality.** `primitive_durable_source_orientation_principle_v001.md:3-16`: `PROSE_STATUS = “Adopted principle”`; the central sign “does not by itself distinguish spin `1/2` from higher half-integer” representations and the principle “additionally adopts primitive minimality.” | **UNTESTED** | Construction of a physical comparison carrier remains separate (`:30-34`), but no failure rule tests minimality. A parent-derived higher primitive representation would expose it; none is frozen. |
| 9 | **Primitive one-vectorlike-pair minimality.** `PRIMITIVE_VECTORLIKE_CHARGED_SOURCE_BRANCH_V003.md:64-80`: pair count is frozen while “Additional vectorlike pairs are consistent and are not proved impossible.” | **UNTESTED** | The no-retuning clause at `:97-101` is not itself a test. This row concerns primitive minimality, not downstream spectral exhaustion. Unit charge is inherited from the compact character and is not counted again as an A6 selector. |
| 10 | **One-complete-`Q_spec` unity clause within FBRAP.** FBRAP's sealed status at `:22-30` is “an adopted microscopic theory premise, not a consequence”; the clause at `:83-95` says gravity, the charged field, sources, and record closure “belong to one complete quantum specification” and “No sector may receive an independent normalization after `Q_spec` is sealed.” | **UNTESTED** | The unused-prediction requirement at `:28-30` is theory-wide; unlike Q-18, no authority assigns that holdout specifically to earn the one-complete-`Q_spec` unity clause. A premise-specific non-alpha record/one-parent holdout is not frozen. |
| 11 | **Adopted relative-`U(1)` bundle and compact connection.** FBRAP `:47-60`: “adopted Level-1 field content”; flags `:164-166` say `smooth_principal_relative_U1_bundle_adopted = true`, `auxiliary_compact_connection_adopted = true`, and `physical_public_EM_connection_derived = false`. | **UNTESTED** | No premise-specific access/holonomy holdout or fail-capable comparator is frozen. The failed `Z_Q` shortcut does not test this field-content adoption. |
| 12 | **Pre-record link premises P1/P2.** `alpha_prerecord_independent_comparison_measure_principle_v001.md:3-19`: `PROSE_STATUS = “Frozen foundational premise”`; it adopts normalized invariant one-link marginals and statistically independent elementary links, and calls P2 “a foundational branch axiom.” | **TESTED — PENDING** | Explicit falsifier `:71-77`: “This premise is rejected” if a target-independent derivation or experiment shows nonfactorizing pre-record correlations, or if a required compact handle cannot use the product-Haar prior. |
| 13 | **Parent-State Covariance.** `PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md:7-13`: “adopted Level-1 Gravacle principle”; flags `:124-130` say adopted `true` and `same_parent_supplies_state_and_dynamics = true`. | **TESTED — ATTEMPTED/BLOCKED, NO PASS** | Explicit falsifiers `:93-107` say “The principle fails” for incompatible finite states, surviving cocycles, inequivalent exhaustion limits, or separately chosen state/generator. `R3_4_PARENT_STATE_COVARIANCE_ADJUDICATION_RESULT_V001.md:3-10,91-103` says “The current parent lineage does not yet pass it.” Q-41 later constructs the source-sector state but keeps `ROOT_DERIVED = false` and `PRODUCER_FLAG_FLIPPED = false` (`QUESTIONS_SETTLED_REGISTER_V001.md:1745-1757`); that narrows the block and still does not record a pass of this premise. |
| 14 | **Causal Incidence Support.** `CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md:7-14`: adopted Level-1 principle which “fixes the support and reuse law”; flags `:93-105` say adopted `true` and completed-incidence reuse `false`. | **TESTED — PARTIAL** | Explicit falsifiers `:62-79` say “This principle is rejected” for reuse of a completed incidence, noncovariant support, incompatible causal orders, separately selected switch-off, or destructive descendants. The primitive test exists; `EM_DEPENDENCY_ORDER_FREEZE_V001.md:45-47` retains the full generated-descendant test as mandatory. |
| 15 | **Global Boundary Descent / Quasi-Free Completeness.** `BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md:12-25` adopts the claim that the primitive action is “exactly the operator-valued functorial CAR lift” with no independent primitive higher/contact/overlap kernel; flags `:190-219` say both principles adopted `true`. | **UNTESTED** | Its quartic control is rejected by the adopted premise itself (`:139-149`) and therefore cannot refute the premise. No independently adjudicated countermodel with authority to fail this premise is attached in the permitted roots. |
| 16 | **Pre-split `SU(5)` parent.** `alpha_presplit_parent_connection_principle_v001.md:3-12`: `PROSE_STATUS = “Adopted Principle”`; one irreducible compact complex five-dimensional connection “is adopted as a Gravacle theory axiom.” | **UNTESTED** | No exhaustive target-independent parent-group/carrier competitor test or parent-sensitive non-alpha holdout is frozen. Such a comparison or a derivation selecting a different parent would expose it. |
| 17 | **Boundary spectral-semigroup / chiral-16 carrier rule.** `alpha_boundary_spectral_semigroup_principle_v001.md:3-13`: `PROSE_STATUS = “Adopted rule”`; the physical source carrier is the chiral half `Lambda^even(C5)=16`. | **TESTED — PENDING** | Its non-use gate at `:51-58` can fail: “If its consequences do not yield a complete positive fixed-point flow, the route fails; no sector weight or higher Casimir may be introduced to repair the result.” No pass is recorded here. |
| 18 | **Sector independence / multiplicative product functional.** `AXIOM_SET_MAP_2026-07-29.md:121` quotes the premise: it “declares” independent integration variables and “the independence is not derived.” | **UNTESTED** | The aggregate branch failure rule does not test the independence proposition specifically. A complete-parent derivation of an unavoidable correlated measure or cross-sector term would expose it; no such test is frozen. |
| 19 | **Residual disclosed ordinary-branch and standard-input package.** FBRAP `:97-101`: the ordinary spacetime properties “are disclosed inputs, not outputs.” `STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.md:42-56` additionally lists “flat source-free asymptotics,” “distinct even M3 record factors,” a “stationary quasifree in-state of h_0,” and the standard Dirac/CAR, CPT, spin-statistics, functional-analysis, and record-axiom inputs. The pair, compact connection, and ER-A are split into rows 9/25, 11, and 4. | **UNTESTED** | Internal Lorentz/CPT or algebra checks test constructions inside the package, not physical selection of the package. No preregistered branch comparison or failure rule for choosing a different asymptotic/state/record package is attached. |
| 20 | **Complex-vs-real selection.** `STAGE8_T7_BETA_ER_A_DISCLOSED_PREMISE_ADOPTION_V001.md:52-60`: `PROSE_STATUS = “standing; assumed, not derived.”` | **UNTESTED — UNDEFINED** | The bounded prior inventory records “no artifact stating this premise exists” (`AXIOM_SET_MAP_2026-07-29.md:127`). An unstated proposition cannot carry a falsifier; no test is identified. |
| 21 | **DCC / Durable-Record Closure Criterion.** The self-declared conditionality register at `STAGE8_T7_BETA_ER_A_DISCLOSED_PREMISE_ADOPTION_V001.md:62-75` carries `DCC` in the “Inherited historical Level-1 stack” and says the register is the authority for what the result is conditional on. `AXIOM_SET_MAP_2026-07-29.md:45-47` expands the label and says its defining artifact is outside the cleanroom; no machine flag exists in the permitted governing roots. | **UNTESTED — UNDEFINED IN BOUNDED ROOTS** | An undefined current-root premise cannot carry a current-root falsifier. No test is identified within `C`, `S`, `A_W`, `A_S`, or permitted `P`. Importing and pinning a defining artifact with a fail-capable criterion, or a current-root derivation that contradicts that defined criterion, would expose it. |
| 22 | **`tau_orth = T_R` cycle-6 identification.** The same register at `:62-75` carries `PROSE_STATUS = “tau_orth = T_R (cycle-6 conditionality)”` and declares itself authoritative. Current binary-gate text says `tau_orth is not yet tau_record` and `durable_record_condition_established = false` (`PRIMITIVE_BINARY_CLOSURE_GENERATOR_GATE_V002.md:59-76,78-90`). | **UNTESTED — REGISTER-ONLY/CONFLICT DISCLOSED** | The binary gate limits the identification but supplies no premise-failure rule. A derived durable-record generator and interval that fail the identification would expose it; no such test is frozen. |
| 23 | **Source-record odd-component identity.** `PRIMITIVE_SOURCE_RECORD_PAIRED_RETURN_IDENTIFICATION_PRINCIPLE_V002.md:14-25,42-76`: an “adopted hypothesis, not a theorem” that the same boundary closure field supplies the source's chiral-odd component; flags `:165-179` say adopted `true` and derived from older theorems `false`. | **TESTED — PENDING** | Failure rule `:145-163`: no durable record, no isolated stable background, nonunique closure magnitude, or no acceptable interacting source pole makes “this branch” fail. Required complete-generator flags remain false. |
| 24 | **Zero-flux/no-charged-write.** V013 `:31-34`; `SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.md:22-43` says “adopt” `Q_Sigma=0 => no charged-record write`; flag `:150` says `zero_flux_no_charged_write_adopted = true`. | **UNTESTED** | The executable checks the chosen representative conditional on the rule. Its “Exact next gate” `:140-144` tests whether `chi` is forbidden, fixed, or irrelevant—not zero-flux/no-write. Complete physical write-operator flags remain false at `:163-166`. |
| 25 | **Exhaustive-use clause of the disclosed one-source branch.** This is a distinct conditional branch clause, not a second primitive-pair adoption: `STAGE1_PREMISE_DISPOSITION_V001.md:60-75` says one pair is a “DISCLOSED_ORDINARY_PRIMITIVE_BRANCH_INPUT” and “Additional charged species cannot be silently discarded.” | **TESTED — PENDING** | The same lines require Stage 9 to “derive the complete charged spectrum and threshold map, or the final claim must remain explicitly conditional on the one-source branch.” That fail-capable gate tests exhaustive use; it does not test row 9's primitive-minimality clause. |
| 26 | **First-record capacity / `N_BR(k_R)=1`.** `alpha_first_durable_record_capacity_principle_v001.md:5-26`: `PROSE_STATUS = “Adopted Rule”`; at first opening, “there is exactly one independent public spectral record.” `AXIOM_SET_MAP_2026-07-29.md:110` expressly reports “No status flag block at all.” The split correction `:78-89` types it as onset plus trace-linearity/nondegeneracy, not A6 minimality. | **TESTED — PENDING** | Explicit failure conditions `:58-66` say “The principle does not close” if the quotient is underived, a trace is replaced by distinct-value counting, multiple inequivalent spectra satisfy the rule, or there is no finite isolated stationary point. |

## 4. Priority answer 1 — `C_R = 1`

### Premise and status

`BID_MINIMAL_PUBLIC_CAUSAL_CELL_DERIVATION_V001.md:49-67` says:

```text
Marginal public-closure rule (adopted Level-1 Gravacle rule)
...
C_R = 1.
...
This fourth input is the selector. Without it, public recoverability gives
a half-line of allowed durations and no absolute record scale.
...
A reviewer may reject that rule
```

The last sentence is permission to reject, not a frozen criterion for doing
so.

The producer cannot test the premise. Its result states at
`results/bid_minimal_public_causal_cell_v001.json:59-64`:

```text
"marginal_public_closure_rule_status": "ADOPTED_LEVEL_1"
"physical_premise_proved_by_script": false
```

The script accepts the compactness threshold as an input at
`scripts/derive_bid_minimal_public_causal_cell_v001.py:19-23`; its status
payload again sets `physical_premise_proved_by_script` false at `:101-106`.
This is an algebra/deformation check after premise injection. It cannot return
evidence against marginal self-gravitation.

### Classification

```text
C_R_EQUALS_1 = UNTESTED
MOST_CONSEQUENTIAL_UNTESTED_ABSOLUTE_SCALE_SELECTOR = true
```

The only corpus-named exposing audit is
`DEPARTURE_2_RESCALING_EXCLUSION_FOUR_CHANNEL_AUDIT_V001.md:85-101`, which asks
whether an admissible cell deformation preserves upstream principles while
moving the response and labels the requirement:

```text
NOT YET AUDITED AGAINST THIS REQUIREMENT.
```

That would test forcedness and uniqueness. It is not a physical falsifier of
the marginality condition and has not been frozen or executed as this
premise's Q-37 test.

## 5. Priority answer 2 — `K_bare = 0`

### Premise and status

FBRAP `:121-132` says:

```text
K_bare[Q_spec, regulator, causal-cell scale] = 0.
...
This is an adopted compositeness condition
```

### Tests

There is a real test short of Slot 18.

FBRAP `:134-141` says:

```text
The route fails to compute the coupling if the completed specification admits
an arbitrary finite deformation
```

`PRIMITIVE_ADDITIVE_RECORD_FIDELITY_ACTION_V002.md:135-145` makes the following
hard failures:

```text
the continuum limit permits an arbitrary finite c F^2 deformation;
...
or the unused prediction fails.
```

The current flag at `:149-159` is:

```text
finite_c_F2_deformation_excluded = false
```

The short gate tests whether the premise can yield an unambiguous coupling; it
does not demonstrate the isolated ontic truth of zero bare stiffness.

The independent premise-earning test remains Slot 18. Q-18 says at
`QUESTIONS_SETTLED_REGISTER_V001.md:781-786`:

```text
its conditionality equals the induced-only axiom's status
...
unless the postulate is independently earned by predicting something else
first — is slot 18.
```

The Slot-18 test is not currently executable:
`STAGE8_SLOT18_Q34_NATIVENESS_AND_HOLONOMY_BRIDGE_RESULT_V001.md:751-765`
says:

```text
It does not make Slot 18 reachable now.
```

This does not turn a failure-capable frozen test into a pass.

```text
K_BARE_EQUALS_0 = TESTED
FINITE_DEFORMATION_GATE_PASSED = false
SLOT18_EARNING_TEST_PASSED = false
```

## 6. Priority answer 3 — mutation exclusion / transport-only

The postulate is not theorem exclusion. V011 `:1084-1092` says:

```text
independent F_2 coefficients are excluded by the BID postulate, not proved
absent by restating that postulate.
...
If an additional primitive response coefficient is required,
Single-Operator Completeness fails as a physical hypothesis.
```

That last sentence is a direct frozen falsifier. It makes this premise
TESTED/PENDING even though:

```text
primitive_F2_theorem_excluded = false
primitive_Pauli_theorem_excluded = false
```

at V011 `:2257-2263`.

The status/test distinction is:

```text
TRANSPORT_ONLY_ADOPTED = true
TRANSPORT_ONLY_DERIVED = false
TRANSPORT_ONLY_TESTED = true
TRANSPORT_ONLY_TEST_PASSED = false
```

## 7. Priority answer 4 — ER-A

The adoption's own status block at
`STAGE8_T7_BETA_ER_A_DISCLOSED_PREMISE_ADOPTION_V001.md:103-108` says:

```text
ER_A_disclosed_premise_adopted = true
ER_A_selected = false
ER_B_selected = false
ER_B_excluded = false
envelope_realization_derived = false
ER_fork_closed = false
```

The prior kill-test cannot count because the same artifact says it blocked on
control design rather than physics. The later insensitivity result tests
finite-lane distinguishability, not whether ER-A is the physical realization.

The artifact itself names what would expose the premise at `:88-98`:

```text
the eventual route to discharging this premise is to DERIVE the write-rate
from the record principle itself
...
That route is explicitly NOT opened here
```

Therefore:

```text
ER_A = UNTESTED
ER_A_EXPOSING_ROUTE_IDENTIFIED = true
ER_A_EXPOSING_ROUTE_FROZEN_OR_EXECUTABLE = false
```

## 8. Priority answer 5 — corrected A6 site accounting

The governing split is
`STAGE8_ALLOW_REQUIRE_MINIMALITY_SPLIT_CORRECTION_V001.md:29-41`:

```text
The object called "allow/require" must be split into two differently typed
objects.
...
The allow/require constraint: real, argued, falsifiable, and already run
...
The local minimality or saturation adoptions named after allow/require
...
are not instances of the allow/require constraint
```

Its exact site list at `:57-76` gives five pure selector sites and one mixed
site:

```text
d = 4
C_R = 1
orthogonalization budget saturation
tau = 1
spin 1/2
one vectorlike pair plus inherited unit charge
```

The selector/minimality component at every one of those approximately five
and a half sites is UNTESTED under the strict premise-specific rule.

```text
A6_PURE_SELECTOR_SITES = 5
A6_MIXED_SITES = 1
A6_EFFECTIVE_SELECTOR_SITE_COUNT = APPROXIMATELY_5_5
A6_SELECTOR_COMPONENTS_TESTED = 0
A6_SELECTOR_COMPONENTS_UNTESTED = ALL
```

The complete-spectrum gate in table row 25 tests exhaustive one-source use.
It does not derive or falsify primitive one-pair minimality, so it does not
change this A6 result.

### Physical allow/require is separately TESTED

The split correction `:31-55` says the physical constraint is:

```text
real, argued, falsifiable, and already run
```

`ABSOLUTE_STIFFNESS_SELECTOR_ROUTE_LEDGER_V002.md:27-34` gives:

```text
status = CELL_CONSTRAINT_ONLY
```

The application at
`m3_e2_threshold2_application_test_v001.md:209-255` records that its required
threshold does not yet pass and freezes a consequence if the theorem fails.
This is a real executed, fail-capable test. It is not an A6 value selector and
is excluded from the 26 value-path-premise-class count rather than
used to launder the selectors as tested.

### Three misattributions

The split correction `:78-98` removes:

1. `N_BR(k_R)=1` from A6; it is separately TESTED in table row 26.
2. `p=1/2`; current authority
   `PRIMITIVE_BINARY_CLOSURE_GENERATOR_GATE_V002.md:3-9,50-90` rejects its
   promotion to a physical durable-record generator and records
   `balanced_calibration_derived = false`. It is conditional/diagnostic, not
   counted as a live standing premise.
3. `m_D/k_R=1`; V011 classifies its historical carrier branch as a competitor,
   not the assumed BID generator. The no-independent-row-renormalization
   bridge is reported as a missed terminus, but no current-authority adoption
   makes it a live value-path premise. It is not counted.

## 9. Two standing items outside the value-path count

### Physical allow/require constraint

```text
STATUS = CELL_CONSTRAINT_ONLY
CLASS = TESTED_EXECUTED
VALUE_SELECTOR = false
```

### C-L3 outcome typing

`STAGE8_T7_CL3_NONZERO_TYPING_PRINCIPAL_DECISION_V001.md:98-110` says the old
typing was:

```text
ADOPTED / SPEC-TYPED, NOT DERIVED
```

But its flags at `:213-239` include:

```text
no_value_could_discriminate = true
new_physical_principle_adopted = false
```

A test that no possible value can fail is UNTESTED under the user's rule.
Because the artifact says it adopts no physical principle and carries no
value discrimination, it is reported here rather than added to the physical
value-path denominator.

## 10. Retired, proposed, superseded, or register-only exclusions

These were found by the standing-premise sweep but are not counted:

| Item | Disposition and verbatim evidence |
|---|---|
| unit winding | `STAGE1_PREMISE_DISPOSITION_V001.md:112-118`: “unit winding: DERIVED from faithful U(1) character theory” |
| unit fidelity multiplicity | Same file `:77-99`: “retired from the load-bearing alpha path”; `information_multiplicity_enters_Q_spec = false` |
| source-record paired-return v001 | Rejected by v002, whose lines `5-13` state v001 equated differently typed objects and is not authority. |
| source-flux v001/v002 | V013 `:35-45` marks v001 rejected and v002 superseded. |
| Causal Direct-Limit Record Principle | `FORK_8_CAUSAL_DIRECT_LIMIT_PROMOTION_RESULT_V001.md:11-14,180-196` says all seven promotion conditions were discharged and “This is a derived scoped principle, not a newly adopted numerical premise”; it is derived, not a standing adoption counted here. |
| Q-37 root-producer premise | Q-38 says “THE ADOPTION LAPSES BY ITS OWN TERMS” (`QUESTIONS_SETTLED_REGISTER_V001.md:1614-1638`); Q-40 explicitly “DOES NOT: reinstate Q-37's lapsed adoption” (`:1738-1739`). |
| V011 declared but unsealed hypotheses | V011's own status block leaves `BID_v011_specification_sealed = false`; they are not inflated into the standing count. |
| process adoptions | Lane rules, runtime/pipeline features, reviewer procedures, and prediction weights are outside the physical value-path premise stack. |

## 11. Complete bounded file lists for the priority searches

Archive mirror lists are encoded elementwise, not by count:

```text
for every relative path x printed in a Complete C list:
  the corresponding complete archive-workspace path is A_W/x
for every relative path y printed in a Complete S list:
  the corresponding complete archive-supervision path is A_S/y
```

Existence of every such mapped path was checked. No additional `A_W` or `A_S`
hit was found for the corresponding query. Thus the printed relative-path
lists plus the explicit roots in Section 2 are complete file lists for both
the live roots and their archive mirrors.

### 11.1 `C_R = 1`

Query family:

```text
C_R = 1
C_R=1
marginal_public_closure_rule
marginal public-closure rule
physical_premise_proved_by_script
```

Complete `C` list:

```text
BID_MINIMAL_PUBLIC_CAUSAL_CELL_DERIVATION_V001.md
STAGE8_ALLOW_REQUIRE_MINIMALITY_SPLIT_CORRECTION_V001.md
STAGE8_G3_SLOT18_MODULUS_PROCESS_DEFECTS_REGISTER_RECORD_V001.md
results/bid_minimal_public_causal_cell_v001.json
scripts/derive_bid_minimal_public_causal_cell_v001.py
```

Complete `S` list:

```text
AXIOM_SET_MAP_2026-07-29.md
BOHM_CONSISTENCY_CONDITIONS_SWEEP_2026-07-28.md
BOHM_CTP_ABSOLUTE_RESPONSE_ROUTE_SWEEP_2026-07-28.md
BOHM_GR_EM_RELATION_REFUTED_2026-07-29.md
BOHM_RATIO_ROUTE_ADJUDICATION_RESULTS_2026-07-28.md
BOHM_TWO_STEPS_WORKFLOW_RESULTS_2026-07-28.md
CONTINUATION_STATE.md
DEPARTURE_2_RESCALING_EXCLUSION_FOUR_CHANNEL_AUDIT_V001.md
QUESTIONS_SETTLED_REGISTER_V001.md
RATIO_ROUTE_CROSS_CITATION_MAP_2026-07-28.md
RECOVERY_STIFFNESS_AND_ALLOW_REQUIRE_2026-07-29.md
RELAY_PASTE_126_ACTION_FORM_2026-07-29.md
RELAY_PASTE_129_GOVERNING_CHAIN_REGISTRATION_AND_CROSS_SECTOR_SPEC_2026-07-30.md
RELAY_PASTE_149_PREMISE_TEST_CLASSIFICATION_2026-07-30.md
RESULT_MODULUS_RADIUS_VS_RECORD_CELL_AND_THE_UNATTEMPTED_BRIDGE_2026-07-29.md
```

Complete `A_W` list: `A_W/x` for each of the five `C` paths printed above.
Complete `A_S` list: `A_S/y` for each of the fifteen `S` paths printed above.
`P = []` under the same exact query and exclusions.

### 11.2 `K_bare = 0`

Query family:

```text
K_bare[Q_spec, regulator, causal-cell scale] = 0
K_bare_zero_adopted_as_compositeness_condition
the induced-only premise sentence
```

Complete `C` list:

```text
FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md
PRIMITIVE_ADDITIVE_RECORD_FIDELITY_ACTION_V002.md
STAGE8_LANE_STATUS.md
STAGE8_Q2STOP_CL3_BULLET_DISARM_PRINCIPAL_DECISION_V001.md
STAGE8_Q2STOP_DIVERGENCE_STOP_STRUCK_PRINCIPAL_DECISION_V001.md
STAGE8_T7_CL3_NONZERO_TYPING_PRINCIPAL_DECISION_V001.md
```

Complete `S` list:

```text
AXIOM_SET_MAP_2026-07-29.md
BOHM_CONSISTENCY_CONDITIONS_SWEEP_2026-07-28.md
BOHM_DIVERGENCE_RETYPING_SWEEP_2026-07-27.md
BOHM_EM_ORDER_TRIAGE_2026-07-28.md
BOHM_GR_EM_RELATION_REFUTED_2026-07-29.md
BOHM_ROUTE_RUNNABILITY_WORKFLOW_RECOVERED_2026-07-28.md
BOHM_SWEEP_2026-07-27_derived_adopted_open.md
CONTINUATION_STATE.md
FOURTH_HORN_PRINCIPAL_DECISION_2026-07-29.md
PRINCIPAL_OBSERVATION_2026-07-27_divergence_is_the_coupling.md
RECOVERY_STIFFNESS_AND_ALLOW_REQUIRE_2026-07-29.md
TEST_RESULT_SURFACE_PREIMAGE_2026-07-29.md
TEST_SPEC_SURFACE_PREIMAGE_OF_COUNTERMODELS_2026-07-29.md
```

Complete `A_W` list: `A_W/x` for each of the six `C` paths printed above.
Complete `A_S` list: `A_S/y` for each of the thirteen `S` paths printed above.
Complete `P` list:

```text
alpha_induced_only_boundary_action_principle_v001.md
```

The exact holdout/failure-clause query list is:

```text
C/FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md
C/PRIMITIVE_ADDITIVE_RECORD_FIDELITY_ACTION_V002.md
A_W/FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md
A_W/PRIMITIVE_ADDITIVE_RECORD_FIDELITY_ACTION_V002.md
P/alpha_induced_only_boundary_action_principle_v001.md
```

### 11.3 Mutation exclusion / transport-only

Complete `C` status-query list:

```text
BID_PRIMITIVE_BOUNDARY_SUPERCONNECTION_CLASSIFICATION_V001.md
BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V002.md
BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V008.md
BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V009.md
BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V010.md
BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md
CURRENT_AUTHORITY_LEDGER_V008.json
CURRENT_AUTHORITY_LEDGER_V009.json
CURRENT_AUTHORITY_LEDGER_V010.json
PRIMITIVE_TRANSPORT_ONLY_PHASE_COMPLETE_GENERATOR_PRINCIPLE_V001.md
R3_4_OUTGOING_TAIL_GENERATOR_EXHAUSTION_PROVENANCE_V001.json
STAGE8_SCHUR_RATIO_PROTECTION_SCOPE_ATTACK_V001.md
provenance/boundary_incidence_dynamics_preregistration_v + 008 + .json
provenance/boundary_incidence_dynamics_preregistration_v + 009 + .json
provenance/boundary_incidence_dynamics_preregistration_v + 010 + .json
provenance/boundary_incidence_dynamics_preregistration_v011.json
results/r3_4_outgoing_tail_generator_exhaustion_v001.json
```

The three concatenated entries are exact legacy search-result paths: concatenate
the displayed stem, three-digit version field, and suffix without spaces. They
are structured this way to distinguish an enumerated historical hit from a
live hardwire to a superseded path.

Complete `S` list:

```text
AXIOM_SET_MAP_2026-07-29.md
BOHM_AUDIT_2026-07-27_stitching_rule_absent.md
BOHM_SWEEP_2026-07-27_derived_adopted_open.md
```

`P = []` under the exact status query. Complete `A_W` list: `A_W/x` for each
of the seventeen `C` paths printed above. Complete `A_S` list: `A_S/y` for
each of the three `S` paths printed above.

The assignment-to-true query for `excluded_by_theorem` or `theorem_excluded`
returned:

```text
C = []
P = []
S =
  BOHM_AUDIT_2026-07-27_stitching_rule_absent.md
A_S =
  A_S/BOHM_AUDIT_2026-07-27_stitching_rule_absent.md
```

The sole `S`/`A_S` carrier quotes a hypothetical true flag and itself reports
zero actual true assignments. It is not a semantic true assignment.

### 11.4 ER-A

The six sealed current `C` carriers are:

```text
STAGE8_T7_BETA_ER_A_DISCLOSED_PREMISE_ADOPTION_V001.md
STAGE8_T7_ER_FORK_KAPPA_INSENSITIVITY_RESULT_V001.md
STAGE8_T7_OPERATOR_VALUED_PRIMITIVE_RESPONSE_ARCHITECTURE_AMENDMENT_V001.md
STAGE8_T7_COMPLETED_CONDITIONED_DUHAMEL_IDENTITY_AND_INTERCHANGE_SCHEMA_SPEC_V001.md
STAGE8_T7_CONNECTED_LINKED_CLUSTER_MAJORANT_DERIVATION_SPEC_V001.md
STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md
```

There are six carriers total and five flag carriers: the adoption plus four
current downstream files report `ER_fork_closed = false` at the adoption
`:108`, operator architecture `:138`, Duhamel schema `:826`, connected
majorant `:551`, and E1 successor `:2222`. Within the bounded roots and
exclusions in Section 2, the insensitivity result is the sixth carrier and has
no such flag. The exact mandatory-headline phrase
`CONDITIONAL ON THE ER-A ENVELOPE PREMISE` occurs at the adoption `:46` and in
none of the five downstream carriers. Superseded E1 V001 and unsealed draft
material were excluded. The complete `A_W` carrier list is `A_W/x` for each
of the six `C` paths printed above; `S`, `A_S`, and `P` add no current carrier
under the same query and exclusions.

### 11.5 A6 split sources

Complete governing/source set:

```text
C:
  STAGE8_ALLOW_REQUIRE_MINIMALITY_SPLIT_CORRECTION_V001.md
  BID_MINIMAL_PUBLIC_CAUSAL_CELL_DERIVATION_V001.md
  BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md
  PRIMITIVE_VECTORLIKE_CHARGED_SOURCE_BRANCH_V003.md
  BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md
S:
  RECOVERY_STIFFNESS_AND_ALLOW_REQUIRE_2026-07-29.md
  AXIOM_SET_MAP_2026-07-29.md
P:
  minimal_public_carrier_principle_v001.md
  primitive_durable_source_orientation_principle_v001.md
A_W:
  A_W/STAGE8_ALLOW_REQUIRE_MINIMALITY_SPLIT_CORRECTION_V001.md
  A_W/BID_MINIMAL_PUBLIC_CAUSAL_CELL_DERIVATION_V001.md
  A_W/BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md
  A_W/PRIMITIVE_VECTORLIKE_CHARGED_SOURCE_BRANCH_V003.md
  A_W/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md
A_S:
  A_S/RECOVERY_STIFFNESS_AND_ALLOW_REQUIRE_2026-07-29.md
  A_S/AXIOM_SET_MAP_2026-07-29.md
```

The CAR-named historical floor/mass source was excluded from direct reading
under the lane fence. Its floor and bridge statuses are carried only through
the sealed split correction, the axiom-map secondary quotation, and V011's
competitor classification.

### 11.6 DCC and `tau_orth = T_R`

DCC query family:

```text
DCC
Durable-Record Closure Criterion
Durable Record Closure Criterion
DURABILITY_CLOSURE_PRINCIPLE
```

Complete governing-root DCC list, excluding this output-under-construction:

```text
C:
  STAGE8_T7_BETA_ER_A_DISCLOSED_PREMISE_ADOPTION_V001.md
S:
  AXIOM_SET_MAP_2026-07-29.md
  BOHM_LAMBDA_FILTER_AND_EXTERNAL_CHAIN_2026-07-29.md
  BOHM_REPLAN_AUDIT_RESULTS_2026-07-29.md
  BOHM_RESCOPE_REGISTER_2026-07-29.md
  BOHM_SWEEP_2026-07-27_derived_adopted_open.md
  CONTINUATION_STATE.md
  PLAN_TO_ALPHA_V005_ORDERED_2026-07-28.md
P:
  []
A_W:
  A_W/STAGE8_T7_BETA_ER_A_DISCLOSED_PREMISE_ADOPTION_V001.md
A_S:
  A_S/y for every S path printed above, and no other A_S path
```

The three expanded-name hits are
`S/AXIOM_SET_MAP_2026-07-29.md`,
`S/BOHM_LAMBDA_FILTER_AND_EXTERNAL_CHAIN_2026-07-29.md`, and
`S/BOHM_RESCOPE_REGISTER_2026-07-29.md`; each points outside the permitted
governing roots rather than supplying a current-root definition. The external
handoff trees were excluded before descent.

`tau_orth = T_R` query family:

```text
tau_orth = T_R
tau_orth=T_R
τ_orth = T_R
```

Complete governing-root list, excluding this output-under-construction:

```text
C:
  STAGE8_T7_BETA_ER_A_DISCLOSED_PREMISE_ADOPTION_V001.md
S:
  AXIOM_SET_MAP_2026-07-29.md
  BOHM_BLIND_DOF_COUNT_2026-07-28.md
  BOHM_LAMBDA_FILTER_AND_EXTERNAL_CHAIN_2026-07-29.md
  BOHM_SWEEP_2026-07-27_derived_adopted_open.md
  CONTINUATION_STATE.md
P:
  []
A_W:
  A_W/STAGE8_T7_BETA_ER_A_DISCLOSED_PREMISE_ADOPTION_V001.md
A_S:
  A_S/y for every S path printed above, and no other A_S path
```

The broader typed-status check additionally read
`C/PRIMITIVE_BINARY_CLOSURE_GENERATOR_GATE_V002.md:59-90`, which says
`tau_orth is not yet tau_record` and leaves
`durable_record_condition_established = false`.

## 12. Complete source list for the additional standing-class sweep

After deduplication and supersession, the additional classes in table rows
10-26 were sourced by:

```text
C:
  FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md
  PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md
  CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md
  BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md
  PRIMITIVE_SOURCE_RECORD_PAIRED_RETURN_IDENTIFICATION_PRINCIPLE_V002.md
  SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.md
  PRIMITIVE_VECTORLIKE_CHARGED_SOURCE_BRANCH_V003.md
  STAGE1_PREMISE_DISPOSITION_V001.md
  STAGE8_T7_BETA_ER_A_DISCLOSED_PREMISE_ADOPTION_V001.md
  STAGE8_T7_CL3_NONZERO_TYPING_PRINCIPAL_DECISION_V001.md
  PRIMITIVE_BINARY_CLOSURE_GENERATOR_GATE_V002.md
  CURRENT_AUTHORITY_LEDGER_V010.json
  CURRENT_AUTHORITY_LEDGER_V013.json
  STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.md
  STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.json
S:
  AXIOM_SET_MAP_2026-07-29.md
  QUESTIONS_SETTLED_REGISTER_V001.md
P:
  alpha_prerecord_independent_comparison_measure_principle_v001.md
  alpha_presplit_parent_connection_principle_v001.md
  alpha_boundary_spectral_semigroup_principle_v001.md
  alpha_first_durable_record_capacity_principle_v001.md
A_W:
  A_W/x for every C path printed above, and no other A_W path
A_S:
  A_S/y for every S path printed above, and no other A_S path
```

Fidelity multiplicity, unit winding, rejected predecessor gates, process
adoptions, and the unsealed V011 hypothesis expansion were inspected for
disposition but excluded from the standing value-path count for the reasons in
Section 10. DCC and `tau_orth = T_R` are retained explicitly in rows 21-22.

## 13. Protected status

```text
classification_only = true
premise_ruled_on = false
premise_adopted = false
premise_withdrawn = false
physical_value_computed = false
measured_constant_compared = false
coupling_computed = false
scale_computed = false
root_computed = false
eigenvalue_computed = false
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
