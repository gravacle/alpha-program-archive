# Stage 8 Bridge Item 3 Constant HJ Record Energy Spec v001

CODEX 1 artifact for Paste 167, Item 3.

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

This artifact specifies the second load-bearing bridge object in order to make
a later test possible. It does not certify constancy and does not report the
object as derived.

## Declared Premises At Outset

P0. Item 1 ranks the first two load-bearing objects as:

```text
S1 complete Lorentzian CTP action / boundary / time-flow data
S2 constant Hamilton-Jacobi record energy on stationary cell
```

P1. Item 2 specifies S1 as a Q-52 test object only:

```text
BRIDGE_S1_COMPLETE_LORENTZIAN_CTP_ACTION_BOUNDARY_TIME_FLOW_DATA_derived =
  false | TYPE-U
```

P2. `BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:16-31` says the
Hamilton-Jacobi relation is conditional on a completely specified Lorentzian
CTP action, state, boundary conditions, and time-flow vector.

P3. `BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:33-48` says the product
form follows only if the same microscopic theory proves a constant energy on
the stationary record trajectory.

P4. `BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:175-177` requires
deriving the CTP Hamilton-Jacobi energy and proving it constant on the first
durable-record saddle.

P5. `BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:192` records
`record_energy_constant_on_stationary_cell_derived = false`.

P6. `STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:314-380` states that the
required HJ conjugate energy does not yet exist and must be specified and
derived as part of the stationary cell target.

No premise beyond P0-P6 is used.

## Object Name

```text
BRIDGE_S2_CONSTANT_HAMILTON_JACOBI_RECORD_ENERGY_CERTIFICATE
```

Typed status:

```text
record_energy_constant_on_stationary_cell_derived = false | TYPE-U
would-build: proof that the Hamilton-Jacobi energy obtained from the complete
             stationary record-cell CTP action is constant on the first
             durable-record saddle
```

## Input

The input is one completed S1 package:

```text
BRIDGE_S1_COMPLETE_LORENTZIAN_CTP_ACTION_BOUNDARY_TIME_FLOW_DATA
```

If S1 is absent, the S2 constancy test must return:

```text
NO_VERDICT | prerequisite S1 package absent | TYPE-U
```

It must not infer a Hamilton-Jacobi energy from a partial action, from a
finite-cell diagnostic, or from the already adopted marginal public-closure
rule.

## Type

`BRIDGE_S2_CONSTANT_HAMILTON_JACOBI_RECORD_ENERGY_CERTIFICATE` is a proof
certificate over the S1 stationary problem.

It must define the symbolic Hamilton-Jacobi record energy as the conjugate of
the on-shell CTP action difference with respect to the S1-declared time-flow
parameter. This is a typing equation, not an evaluation:

```text
HJ_record_energy := conjugate derivative of the on-shell CTP branch-action
                    difference with respect to the S1-declared time-flow
                    parameter
```

The certificate then proves that this symbolic energy is constant on the
declared stationary record-cell solution class.

## Required Fields

### F1. S1 Provenance

The certificate must cite the exact S1 package it consumes.

Failure condition:

```text
S1_input_identified = false | TYPE-R
test: the certificate claims HJ constancy without naming a complete S1 package
```

### F2. Conjugate Variable

The certificate must identify the S1-declared time-flow parameter and the
on-shell action difference being differentiated.

Failure condition:

```text
HJ_conjugate_variable_defined = false | TYPE-R
test: the derivative is taken with respect to an unstated, floating, or
      downstream-selected parameter
```

### F3. Differentiability Domain

The certificate must state the domain on which the on-shell action difference
is differentiable in the S1-declared time-flow parameter.

Failure condition:

```text
HJ_differentiability_domain_declared = false | TYPE-R
test: constancy is claimed where the HJ derivative is not defined or where
      differentiability is only asserted after the target is known
```

### F4. Stationary Solution Class

The certificate must state the stationary record-cell solution class inherited
from S1 and prove constancy on that class, not on a selected example.

Failure condition:

```text
stationary_solution_class_declared = false | TYPE-R
test: constancy is proved only for an example or endpoint rather than the
      declared stationary class
```

### F5. Constancy Identity

The certificate must prove that the HJ record energy is independent of the
S1-declared time-flow parameter throughout the declared domain. Endpoint
matching is insufficient.

Failure condition:

```text
HJ_record_energy_constant = false | TYPE-R
test: the symbolic derivative has residual time-parameter dependence, or the
      proof establishes equality only at a selected endpoint
```

### F6. Boundary And Reparametrization Guard

The certificate must show that the constancy statement is stable under the
boundary and time-flow choices fixed by S1. This does not license changing
those choices.

Failure condition:

```text
HJ_constancy_boundary_stable = false | TYPE-R
test: the claimed constant changes when the fixed S1 boundary/time-flow data
      are represented in an equivalent allowed way
```

### F7. Downstream Isolation

The certificate must not claim equality to the gravitating closure energy, a
reference-subtraction theorem, a derived marginal closure, or an interval
solution.

Failure condition:

```text
downstream_bridge_flag_silently_flipped = false | TYPE-R
test: an S2 pass is recorded as a pass for S3, S4, S5, or S6 without the
      corresponding downstream certificate
```

## What The Spec Does Not Deliver

The S2 certificate does not prove:

```text
complete_CTP_action_and_boundary_data_derived = false | TYPE-U
record_energy_equals_total_gravitating_energy_derived = false | TYPE-U
reference_subtraction_and_no_spectator_theorem_derived = false | TYPE-U
marginal_closure_condition_derived_rather_than_assumed = false | TYPE-C
isolated_stable_positive_interval_solution_derived = false | TYPE-U
```

It also does not resolve the energy-identification fork in
`BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:50-104`.

## Test Wiring

### T1. Input Availability

If S1 is not supplied, return:

```text
NO_VERDICT | prerequisite S1 package absent | TYPE-U
```

Reports to:

```text
S2_input_availability
```

### T2. HJ Typing

Given S1, verify that the HJ conjugate energy is a well-defined symbolic object.

Reports to:

```text
HJ_record_energy_well_typed
```

### T3. Constancy

Given a well-typed HJ record energy, test whether it is constant on the S1
stationary record-cell solution class.

Reports to:

```text
record_energy_constant_on_stationary_cell
```

Failure is TYPE-R only against a supplied S1 package and a supplied constancy
certificate. Absence of either prerequisite is TYPE-U / NO_VERDICT.

### T4. Downstream Isolation

Check that an S2 pass is not used as evidence for S3-S6.

Reports to:

```text
S2_downstream_isolation_preserved
```

## Re-Rank

The dependency order from Item 1 remains unchanged:

```text
S1 -> S2 -> S4 -> S3 -> S5 -> S6
```

The only refinement is that S2 cannot be attempted as a proof until S1 exists.
Its current contribution is a test specification only.

## Verdict

The second load-bearing object is now specified as a test object, not derived.

```text
BRIDGE_S2_CONSTANT_HAMILTON_JACOBI_RECORD_ENERGY_CERTIFICATE_specified_for_test = true
BRIDGE_S2_CONSTANT_HAMILTON_JACOBI_RECORD_ENERGY_CERTIFICATE_derived = false | TYPE-U
would-build: a certificate, over one complete S1 package, proving that the
             Hamilton-Jacobi record energy is constant on the first
             durable-record stationary solution class
```

