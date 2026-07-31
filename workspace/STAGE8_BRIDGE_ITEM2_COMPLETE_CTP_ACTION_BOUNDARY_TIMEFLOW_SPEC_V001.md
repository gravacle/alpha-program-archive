# Stage 8 Bridge Item 2 Complete CTP Action Boundary Time-Flow Spec v001

CODEX 1 artifact for Paste 167, Item 2.

Status: Q-52 TEST SPECIFICATION ONLY.

```text
derived = false
adopted = false
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No computation or evaluation of alpha, `kappa_record`, `kappa_Thomson`, a
coupling, a radius, a scale, a root, an eigenvalue, a beta function, `E_R`,
`T_R`, or any absolute interval was performed. No measured constant comparison
was performed. `a32_holdout/custodian_private/` was not opened.

This artifact specifies a missing object in order to make a test possible. It
does not report the object as derived.

## Declared Premises At Outset

P0. Q-59 identifies the bridge from `C_R = 1` to an absolute record interval
as unclosed, and Q-64 reports the bridge as an unbuilt path with no cycle.

P1. `BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:16-31` states that
the Hamilton-Jacobi relation is conditional on a completely specified
Lorentzian CTP action, state, boundary conditions, and time-flow vector.

P2. `BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:169-175` requires one
target-independent complete source-record-gravity action fixing the
global/subregion boundary terms and the time-flow vector.

P3. `STAGE8_C_R_SELECTOR_NONSELECTION_DIAGNOSIS_V001.md:145-153` states the
same would-build object and keeps
`complete_CTP_action_and_boundary_data_derived = false`.

P4. `BID_MINIMAL_PUBLIC_CAUSAL_CELL_DERIVATION_V001.md:49-67` supplies an
adopted Level-1 marginal public-closure rule. It is not treated here as a
derived marginality theorem.

P5. The rank-6 conditionality stands: this bridge remains conditional on the
disclosed induced-only branch and does not upgrade that branch to a theorem.

No premise beyond P0-P5 is used.

## Object Name

```text
BRIDGE_S1_COMPLETE_LORENTZIAN_CTP_ACTION_BOUNDARY_TIME_FLOW_DATA
```

Typed status:

```text
complete_CTP_action_and_boundary_data_derived = false | TYPE-U
would-build: one target-independent source-record-gravity Lorentzian CTP
             action, state, boundary conditions, and time-flow vector for the
             stationary record-cell problem
```

## Type

`BRIDGE_S1_COMPLETE_LORENTZIAN_CTP_ACTION_BOUNDARY_TIME_FLOW_DATA` is a finite
specification package, not a scalar:

```text
S1 =
  (
    cell_domain,
    source_record_gravity_field_content,
    CTP_branch_data,
    Lorentzian_CTP_action_with_boundary_terms,
    admissible_state_or_preparation,
    global_boundary_data,
    subregion_boundary_data,
    time_flow_vector,
    stationary_problem,
    provenance_and_fences
  )
```

Domain: the stationary record-cell problem named by the bridge gate.

Output: enough data to define an on-shell CTP action difference and its
Hamilton-Jacobi conjugate energy. It does not output a value, an interval, a
response, or any stiffness.

## Required Fields

### F1. Cell Domain

The package must specify the Lorentzian cell domain to which the stationary
record-cell problem applies, including the boundary hypersurfaces on which the
action principle is posed.

Failure condition:

```text
cell_domain_specified = false | TYPE-R
test: the package contains no Lorentzian domain with boundary data on which
      the CTP variational problem can be stated
```

### F2. Source-Record-Gravity Field Content

The package must name every dynamical and background field in the
source-record-gravity action. The bridge source requires the same microscopic
theory to carry the action, state, boundary, time-flow, record phase, and
closure energy identifications
(`BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:33-48`).

Failure condition:

```text
field_content_complete = false | TYPE-R
test: a field or sector used by the stationary action, boundary term, or
      closure-energy comparison is absent from the declared field list
```

### F3. CTP Branch Data

The package must specify the two CTP branches, their index ordering, and their
branch-reality relation strongly enough that a branch-energy difference is a
well-typed object. It must also state which branch data are held fixed in the
stationary variation.

Failure condition:

```text
CTP_branch_structure_well_typed = false | TYPE-R
test: the branch action difference or branch-energy difference is undefined,
      branch-order dependent without a rule, or lacks a stated reality relation
```

### F4. Lorentzian CTP Action With Boundary Terms

The package must specify the Lorentzian CTP action including all global and
subregion boundary terms. The boundary terms cannot be left to later choice,
because the bridge gate says the HJ relation is conditional on the action,
state, boundary conditions, and time-flow vector as a package
(`BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:16-31`).

Failure condition:

```text
boundary_action_complete = false | TYPE-R
test: the action lacks a boundary term required to make the variation
      well-posed, or leaves a boundary/reference term selectable after
      response-facing quantities are inspected
```

### F5. Admissible State Or Preparation

The package must specify the state or preparation on which the stationary
record-cell problem is evaluated. This is a typing requirement only; it is not
a no-spectator theorem.

Failure condition:

```text
state_or_preparation_specified = false | TYPE-R
test: the stationary action is evaluated without a declared state/preparation
      or with a state/preparation chosen after a downstream target is known
```

### F6. Time-Flow Vector

The package must specify a time-flow vector and the parameter with respect to
which the Hamilton-Jacobi conjugate is taken. It must be target-independent.

Failure condition:

```text
time_flow_vector_specified = false | TYPE-R
test: the HJ derivative is taken with respect to an unstated time parameter,
      a freely reparametrizable parameter, or a parameter selected by a
      downstream target
```

### F7. Stationary Problem

The package must specify the stationary variational problem and the class of
stationary solutions/saddles it admits. This field only makes the next bridge
object attemptable; it does not prove that the HJ energy is constant.

Failure condition:

```text
stationary_problem_specified = false | TYPE-R
test: the package gives an action but no stationary equations, boundary
      variation rule, or admissible solution class
```

### F8. Provenance And Fences

The package must declare that it is target-independent and must carry the
standing fences forward: no measured endpoint, no alpha or stiffness target,
no post-hoc finite counterterm, no concealed marginality input.

Failure condition:

```text
target_blindness_preserved = false | TYPE-R
test: any field, boundary term, time-flow normalization, state/preparation, or
      reference term is selected by a downstream response value, measured
      endpoint, or desired closure result
```

## What The Spec Does Not Deliver

This S1 package does not prove:

```text
record_energy_constant_on_stationary_cell_derived = false | TYPE-U
record_energy_equals_total_gravitating_energy_derived = false | TYPE-U
reference_subtraction_and_no_spectator_theorem_derived = false | TYPE-U
marginal_closure_condition_derived_rather_than_assumed = false | TYPE-C
isolated_stable_positive_interval_solution_derived = false | TYPE-U
```

It also does not resolve the Misner-Sharp / Brown-York energy-identification
fork identified in `BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:50-104`.
It only creates the typed input that later bridge tests would consume.

## Test Wiring

The following tests are the only tests this specification authorizes.

### T1. Package Completeness

Input: a proposed S1 package.

Method: check that F1-F8 are present and cite their authorities or declared
Q-52 test premises.

Reports to:

```text
complete_CTP_action_and_boundary_data_specified_for_test
```

It must not report to any downstream constant-energy, gravitating-energy,
reference-subtraction, marginality, or interval-solution flag.

### T2. CTP / Boundary Well-Formedness

Input: a proposed S1 package.

Method: verify that the CTP branch difference, boundary variational principle,
and stationary equations are all well typed.

Reports to:

```text
CTP_boundary_stationary_problem_well_typed
```

Failure is TYPE-R only if a concrete package is supplied and fails. If no
package is supplied, the result is:

```text
NO_VERDICT | prerequisite package absent | TYPE-U
```

### T3. Time-Flow Conjugacy

Input: a proposed S1 package.

Method: verify that the time-flow vector and conjugate parameter are specified
before any response-facing quantity is inspected.

Reports to:

```text
time_flow_conjugacy_well_typed
```

It does not prove that the conjugate energy is constant.

### T4. Boundary / Reference Non-Floating Check

Input: a proposed S1 package.

Method: verify that boundary and reference slots are either fixed in the
package or explicitly declared missing. A floating slot fails the S1 package;
an explicitly missing slot returns TYPE-U rather than a fabricated pass.

Reports to:

```text
boundary_reference_slots_not_floating
```

### T5. Downstream Isolation

Input: a proposed S1 package and this artifact.

Method: check that no S1 pass is treated as a pass for S2-S6.

Reports to:

```text
downstream_isolation_preserved
```

Failure condition:

```text
downstream_flag_silently_flipped = false | TYPE-R
test: an S1 package pass causes any S2-S6 bridge flag to be recorded as true
      without the corresponding downstream test
```

## Verdict

The first load-bearing object is now specified as a test object, not derived.

```text
BRIDGE_S1_COMPLETE_LORENTZIAN_CTP_ACTION_BOUNDARY_TIME_FLOW_DATA_specified_for_test = true
BRIDGE_S1_COMPLETE_LORENTZIAN_CTP_ACTION_BOUNDARY_TIME_FLOW_DATA_derived = false | TYPE-U
would-build: a target-independent complete source-record-gravity Lorentzian
             CTP action package with boundary data, state/preparation, and
             time-flow vector
```

