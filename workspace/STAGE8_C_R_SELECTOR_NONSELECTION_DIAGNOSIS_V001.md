# Stage 8 C_R Selector Nonselection Diagnosis v001

Date: 2026-07-30
Lane: CODEX 1
Register head used: Q-58
Status: DIAGNOSTIC / APPEND-ONLY / DOES NOT SELECT A SCALE

This artifact answers Paste 161: why `C_R = 1`, the sole absolute-scale selector identified by
Q-58, has not yet selected an absolute record interval, and what would make it select.

F-GK3 declaration: no premise beyond the current sealed stack is introduced. This artifact does
not specify a new missing object under Q-52 because the relevant missing objects are already named
by the scale-bridge and falsifier-design artifacts.

Fences observed: `a32_holdout/custodian_private/` was not read. The correlator-to-Hessian map,
`CTP_PHYS_INPUT_PACKAGE`, the response-extraction layer, and `Gamma_K` were not opened as objects
of analysis. No alpha, kappa_record, kappa_Thomson, coupling, radius, scale, root, eigenvalue,
beta function, `E_R`, `T_R`, or absolute interval was computed or evaluated. No comparison to any
measured constant was made.

Later-ruling check: the archive head at start included relays 161-163 and Q-58. No later ruling
bearing on this item was consulted.

Search scope for TYPE-S statements: cleanroom root
`/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003`,
archive workspace root `/Users/bgm/MB Work/alpha-program-archive/workspace`, and supervision root
`/Users/bgm/MB Work/alpha_supervision`. Exclusions: `a32_holdout/custodian_private/` and the
Codex-2-owned response-extraction / correlator-to-Hessian / `CTP_PHYS_INPUT_PACKAGE` object layer.
Queries used included `C_R = 1`, `C_R=1`, `chi_*`, `absolute_record_interval`,
`marginal public-closure`, `Misner-Sharp`, `Brown-York`, `energy_choice_changes_T_R_by_sqrt_2`,
`Delta S_record`, `Hamilton-Jacobi`, `first durable`, and `physical_premise_proved_by_script`.

## Lead Finding

`C_R = 1` cannot select alone.

Q-58 remains correct that `C_R = 1` is the only absolute-scale selector in every branch, but being
the only orbit-breaking condition is not the same as being sufficient. In the sealed chain it is a
dimensionless marginal self-gravitation condition. It can select only after a partner derivation
supplies:

1. the physical identification of the record action marker with the complete stationary boundary
   Hamiltonian action;
2. the Hamilton-Jacobi energy that is conjugate to the local tip-to-tip proper interval;
3. equality between that CTP branch-energy difference and the gravitating energy used in the
   closure condition, including fixed reference subtraction and no-spectator control;
4. independent first durable/public closure, without marginality supplied as an input; and
5. one isolated stable positive solution in Planck units, before any endpoint or alpha-facing
   value is evaluated.

Therefore the present state is not `C_R = 1` refuted. It is:

```text
C_R_equals_1_truth_status = NO_VERDICT
blocked_by:
  absolute_record_interval_derived_in_declared_branch = false | TYPE-U
  relative_marker_equals_complete_stationary_Hamiltonian_action_derived = false | TYPE-U
  C_R_marginal_selector_derived_rather_than_adopted = false | TYPE-C
```

## 1. What `C_R = 1` Asserts, And What Selecting Would Mean

`BID_MINIMAL_PUBLIC_CAUSAL_CELL_DERIVATION_V001.md:38-47` defines the public recoverability
condition on the maximal spherical section:

```text
C_R = 2 G E_R / (c^4 R_R) <= 1.
```

The same lines say that `C_R > 1` is trapped and cannot be the outwardly recoverable primitive
comparison cell of the declared branch. Lines 49-60 state the marginal public-closure rule as an
adopted Level-1 rule: the least positive `T_R` is attained at the boundary of the recoverable set,
`C_R = 1`, and "This fourth input is the selector." Lines 62-67 add the control: the rule may not
be hidden or replaced by numerical agreement downstream, and the active theory must derive the
map `Delta S_record = E_R T_R`.

Selecting would mean producing a unique physical member of the scale orbit: a Lorentz-scalar
proper interval in Planck-time units, with associated record radius, energy, and mass in the
corresponding Planck units, inside the declared ordinary isotropic branch. This artifact does not
restate or evaluate the displayed conditional numeric root in `BID_MINIMAL_PUBLIC_CAUSAL_CELL`
lines 83-98.

The source itself marks why this has not selected. Lines 144-152 say the algebra fixes the
primitive cell scale and local source threshold **if** complete source-parent dynamics derives
`Delta S_record = E_R T_R`; until that interface is closed, the result is a conditional candidate.
Lines 156-170 flag the current state:

```text
relative_marker_equals_complete_stationary_Hamiltonian_action_derived = false | TYPE-U
absolute_record_interval_derived_in_declared_branch = false | TYPE-U
primitive_record_radius_derived_in_declared_branch = false | TYPE-U
primitive_record_energy_scale_derived_in_declared_branch = false | TYPE-U
strict_untrapped_inequality_alone_selects_unique_scale = false | TYPE-R
```

The failure-to-select type is therefore **missing input / unbuilt interface**, not a refutation of
the marginality premise.

## 2. The `sqrt(2)` Energy-Identification Ambiguity

`BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:33-48` states that the product form
`|Delta S_record| = E_R T_R` follows only after the same microscopic theory proves a constant
Hamilton-Jacobi energy on the stationary record trajectory, equality between the CTP branch-energy
difference and complete gravitating cell energy after reference subtraction, no spectator/vacuum/
binding/edge/environment mismatch, conjugacy of the time parameter to `T_R`, and use of the same
energy in the chosen gravitational closure condition.

The explicit ambiguity is at `BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:50-104`. The two
standard candidates are:

- Misner-Sharp energy, entering the compactness formula in lines 52-56.
- Reference-subtracted Brown-York energy on a round timelike boundary, given in lines 58-65.

Lines 67-79 say they are both geometrically meaningful but conjugate to different boundary/time
choices, and that the present causal diamond is the support of a CTP history difference rather than
a material timelike boundary. Therefore neither candidate is automatically the Hamiltonian
conjugate to the local tip-to-tip proper interval.

At the adopted marginal selector, lines 81-104 show that the two energy identifications give
different exact conditional roots whose ratio is `sqrt(2)`. This artifact does not reproduce or
evaluate either root. The typed status is:

```text
Misner_Sharp_and_Brown_York_candidates_coincide_at_marginality = false | TYPE-R
energy_choice_changes_interval_by_sqrt_2 = true | TYPE-R
Misner_Sharp_selected = false | TYPE-U
Brown_York_selected = false | TYPE-U
Hamilton_Jacobi_conjugate_energy_selected = false | TYPE-U
```

This is a genuine physical/typing fork, not a convention already settled by a sealed rule. It is
also not necessarily a binary "choose Misner-Sharp or Brown-York" act: the scale bridge requires
the complete target-independent microscopic theory to derive the relevant Hamilton-Jacobi energy.
The sealed text explicitly refuses automatic selection by either named energy.

Later sealed material preserves that refusal. `STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:314-380`
states that the required Hamilton-Jacobi conjugate energy does not yet exist and must be specified
and derived as part of the stationary cell target; it does not choose Misner-Sharp or Brown-York.
`STAGE8_GAMMA_K_CONSTRUCTION_SPEC_AMENDMENT_001.md:234-236` preserves that energy refusal.
`STAGE8_MODULAR_CONJUGATE_ENERGY_LIMIT1_APPLICABILITY_RESULT_V001.md:281-289` says the modular
proposal is not applicable to the active target and leaves the Hamilton-Jacobi conjugate energy
unspecified.

## 3. What Is Missing Between `C_R = 1` And A Derived Absolute Interval

The missing objects are already named by the sealed chain:

```text
complete_CTP_action_and_boundary_data_derived = false | TYPE-U
would-build: a completely specified Lorentzian CTP action, state, boundary conditions, and
             time-flow vector for the stationary record-cell problem.
source: BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:16-31, 169-185, 187-203

record_energy_constant_on_stationary_cell_derived = false | TYPE-U
would-build: proof that the Hamilton-Jacobi energy is constant on the first durable-record saddle.
source: BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:33-48, 169-185

record_energy_equals_total_gravitating_energy_derived = false | TYPE-U
would-build: proof that the CTP branch-energy difference equals the complete gravitating cell
             energy used by closure, after fixed reference subtraction.
source: BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:33-48, 155-167, 169-185

reference_subtraction_and_no_spectator_theorem_derived = false | TYPE-U
would-build: state/reference-subtraction theorem excluding spectator, vacuum, binding, edge, or
             environment energy from compactness unless it also enters the record action
             difference.
source: BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:33-48, 155-167, 169-185

marginal_closure_condition_derived_rather_than_assumed = false | TYPE-C
constraint: `C_R = 1` is currently an adopted Level-1 marginal public-closure rule.
release: target-independent complete source-record-gravity action derives first durable/public
         closure at the marginal boundary without receiving marginality as an input.
source: BID_MINIMAL_PUBLIC_CAUSAL_CELL_DERIVATION_V001.md:49-67;
        STAGE8_C_R_FALSIFIER_DESIGN_AND_FLOOR_SOURCE_VALUE_RECONCILIATION_V001.md:487-520

isolated_stable_positive_scale_solution_derived = false | TYPE-U
would-build: Lorentz-scalar equation in the dimensionless interval with one isolated positive
             stable solution, before alpha or endpoint evaluation.
source: BID_ABSOLUTE_RECORD_SCALE_IDENTIFIABILITY_GATE_V001.md:66-79;
        BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:169-185

first_durable_public_closure_independently_derived = false | TYPE-U
would-build: derivation that the selected configuration is the first durable, outwardly
             recoverable public record configuration, with physical durability/publicity not
             inserted through the marginality premise.
source: STAGE8_C_R_FALSIFIER_DESIGN_AND_FLOOR_SOURCE_VALUE_RECONCILIATION_V001.md:487-520
```

Relation to Codex 2 fences: this is not the response-extraction layer as such. The named missing
object is upstream: a complete source-record-gravity / Hamilton-Jacobi scale bridge. It may
consume CTP action and boundary-data inputs if Codex 2's `CTP_PHYS_INPUT_PACKAGE` supplies them,
but this artifact did not inspect or build that package.

## 4. Is `C_R = 1` Capable Of Selecting Alone?

No.

`BID_ABSOLUTE_RECORD_SCALE_IDENTIFIABILITY_GATE_V001.md:10-50` proves the record kinematics have a
positive scale orbit: rescaling `T_R` and inversely rescaling the physical generator leaves
first-opening probabilities, orthogonality, endpoint transfer, incidence normalization, and
projective path lengths unchanged. Lines 52-64 conclude that current record kinematics do not
identify one physical duration; the selection must come from a dimensionful part of the same
parameter-free dynamics, not an endpoint or measured target. Lines 66-79 give the exact closure
condition: a Lorentz-scalar equation in the dimensionless interval with one isolated positive
stable solution.

`C_R = 1` is the only known orbit-breaking condition, but as a standalone equation it relates an
energy to a radius. It becomes a selector only when paired with the record-action product, the
causal-diamond support relation, and the still-unbuilt proof that the action energy is the same
energy as the closure energy. In the minimal public-cell algebra, this pairing produces a
conditional formula. In the full program, the pairing is not yet derived.

Typed conclusion:

```text
C_R_can_select_alone = false | TYPE-U
would-build: no standalone construction; selection requires the named source-record-gravity /
             Hamilton-Jacobi bridge and first durable/public closure theorem.

C_R_can_select_conditionally_with_declared_inputs = true
condition: action marker, causal-diamond support, chosen/conjugate closure energy, and marginal
           public-closure rule are all accepted as inputs.

C_R_has_selected_in_declared_branch = false | TYPE-U
would-build: the missing bridge plus one isolated stable positive physical interval.
```

Q-58 is therefore not refuted. Its "one unselected absolute scale" result stands, but its honest
use requires saying that the one selector is not yet an executed selector. The partner is not
unnamed: it is the complete target-independent source-record-gravity Hamilton-Jacobi scale bridge
already specified by the scale-bridge gate.

## 5. Current Test Status

`STAGE8_C_R_FALSIFIER_DESIGN_AND_FLOOR_SOURCE_VALUE_RECONCILIATION_V001.md:7-27` states that a
physical falsifier for `C_R = 1` can be designed. The test asks a target-independent complete
source-record-gravity action to select the first durable, outwardly recoverable public record
configuration without receiving marginality as an input. A strictly interior first configuration
or a complete derivation excluding marginal first closure would count against `C_R = 1`; equality
would make the premise survive; an incomplete construction would be inconclusive.

Its status remains:

```text
C_R_physical_falsifier_designable = true
C_R_falsifier_candidate_frozen = false | TYPE-C
constraint: freezing this falsifier is a principal act.
release: principal freezes a C_R-specific physical falsifier.

C_R_test_executed = false | TYPE-C
constraint: the candidate falsifier is not frozen.
release: frozen falsifier plus complete source-record-gravity action sufficient to run it.

existing_minimal_cell_producer_tests_C_R_premise = false | TYPE-R
test: STAGE8_C_R_FALSIFIER... lines 304-333 show that the producer receives the compactness
      threshold as an input and therefore cannot produce physical evidence against that input.
```

`STAGE8_C_R_FALSIFIER_DESIGN_AND_FLOOR_SOURCE_VALUE_RECONCILIATION_V001.md:367-485` finds no
current sealed antagonist requiring strict submarginality; mere interior membership in the
already acknowledged recoverable half-line is not enough. That bounded negative is carried here as:

```text
current_separately_sealed_strict_submarginality_antagonist_found = false | TYPE-S
roots: cleanroom root; archive workspace root; supervision root.
excl: a32_holdout/custodian_private/; Codex-2-owned response and CTP package objects.
fences: no scale, interval, energy, alpha, kappa_record, or kappa_Thomson evaluation.
query: "strict submarginal", "submarginal first closure", "C_R < 1", "forbids marginal closure",
       "first durable public", "marginal public-closure".
```

## 6. Four Direct Answers

1. `C_R = 1` asserts marginal self-gravitation of the first admissible public primitive record
   cell. Selecting would mean fixing the physical record-cell interval as a unique isolated stable
   Planck-unit solution and thereby fixing the associated cell radius/energy/mass units. It has
   not selected because the energy/action interface and firstness/durability derivation are
   unbuilt, and because marginality is adopted rather than derived.

2. The `sqrt(2)` ambiguity is the gap between using Misner-Sharp energy and using
   reference-subtracted Brown-York energy as the Hamiltonian-conjugate closure energy at
   marginality. The two candidates do not coincide, and sealed text says neither is automatically
   conjugate to the local tip-to-tip interval. This is an unresolved physical/typing fork, not a
   convention settled by the corpus.

3. Missing between `C_R = 1` and `absolute_record_interval_derived = true`: complete Lorentzian
   CTP action/boundary/time-flow data; constant Hamilton-Jacobi energy on the stationary cell;
   equality between branch-energy difference and gravitating closure energy; reference subtraction
   and no-spectator theorem; derived marginal first durable/public closure; one isolated stable
   positive interval solution. This is upstream of response extraction, though it may later
   consume CTP input-package material.

4. `C_R = 1` is not capable of selecting alone. It is the only known scale-orbit breaker, but it
   is not sufficient without the source-record-gravity Hamilton-Jacobi bridge. The present status
   is a conditional formula plus a designed-but-unfrozen falsifier, not a completed selection.

## Protected Status

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
