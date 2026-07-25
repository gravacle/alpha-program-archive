# Stage-8 T7 Relayed Connected-Preparation Retest Spec v001

Date: 2026-07-24

## Status

```text
SPECIFICATION_SEALED_BEFORE_EXECUTION
```

This gate retests C1 after the relay dependency has been pulled forward and
the residual family has been resolved in the declared branch. It asks whether
the same sealed parent now supplies a unique scalar source functional and a
nonzero completed baseline for every admitted finite causal history.

No state, final source boundary, response, or coefficient may be selected by
the execution.

## Hash-pinned authorities

```text
52401eefc3ff84e22f04bbc329a619b830058661db7f969d2d43d167d97d893d  STAGE8_T7_RELAYED_FAMILY_RESOLUTION_RESULT_V001.md
53c499da21ba2387d1cb235e573bc67c2974331b873d9b93ad2baece467107e4  stage8_execution/t7_relayed_family_resolution/T07_RELAYED_FAMILY_RESOLUTION_V001.seal.sha256
dced9d9ed95601d8524bfbe68ec870a620bfe1cbee5b7c07230a5a9658de945c  STAGE8_T7_CONNECTED_ANALYTIC_CLOSURE_SPEC_V001.md
f891d3afc58e695529d8d569b5d2ba4b853e30c9cfa4296817cb17b60f38b054  STAGE8_T7_CONNECTED_ANALYTIC_CLOSURE_RESULT_V001.md
40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9  R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md
345d447eaf6d730caa6fa655b92a7b0cd93a68b5f86e0c8929cf969f40aeb7cb  R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md
532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb  PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md
202f8d8db60046a8069b1cd8fcc38f505eb95fa29578e094e005f56e967c3a35  STAGE7_QSPEC_SCOPE_AND_PREMISE_SUCCESSOR_V001.md
1d114e71c29c3a39b7afd1b7a80b47afb52fe77e8ee1e4e19b604defe3c69305  R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_RESULT_V001.md
```

## P1 - Type of the relayed completed boundary

For a causal sequence of exact controlled writes with source projectors
`P_0,...,P_(N-1)`, compress every record factor from its ready root to its
completed pointer. Derive the remaining map on the source:

```text
K_N(0)
 =(I_source tensor <p|^N)
   U_(N-1)...U_0
   (I_source tensor |r>^N)
 =P_(N-1)...P_0
```

up to the already-fixed spin identity and incidence orientation.

The relay preserves completed record labels and supplies new ready roots. It
does not, by itself, turn `K_N` into a scalar.

## P2 - Baseline state dependence

Use the exact three-cell incidence chain:

```text
e_0=(-1,1,0,0)/sqrt(2),
e_1=(0,-1,1,0)/sqrt(2),
e_2=(0,0,-1,1)/sqrt(2),
P_j=|e_j><e_j|.
```

Evaluate:

```text
a_N(rho)=Tr(rho K_N)
```

for `N=1,2,3` and the predeclared source states:

```text
rho=P_0;
rho=P_1;
rho=P_2;
rho=I/4.
```

Report every complex value. Any zero baseline or state-dependent value is a
failure of a state-independent C1 closure, not a reason to remove the state.

Also report the off-diagonal source transition

```text
<e_(N-1)|K_N|e_0>.
```

It is a separate in/out functional, not an expectation state, and may not be
substituted after the expectation test.

## P3 - State-selection audit

Classify the current source-state status from the sealed authorities:

```text
Parent-State Covariance requires a parent-selected state;
the Stage-7 ordinary-branch quasifree in-state is disclosed;
finite-energy incoming charged excitations are boundary data;
and the current complete-parent result does not derive a unique physical
charged in-state.
```

Then prove the minimal nonuniqueness statement: charge superselection and
stationarity alone admit more than one density operator whenever the charged
source sector has dimension greater than one. No target comparison is
permitted.

## P4 - Dispositions

```text
T7_CONNECTED_PREPARATION_DERIVED_AFTER_RELAY
```

requires one source functional derived by the sealed parent, a nonzero
baseline for every admitted finite history, and reduction to the pinned
one-handle amplitude.

```text
T7_CONNECTED_PREPARATION_BLOCKED_AFTER_RELAY
```

is required if the completed compression remains source-operator-valued,
the authorities leave the charged in-state as boundary data, or two
admissible states give different/zero baselines.

No adoption verdict exists in this execution.

## Mandatory downstream negative control

Even if P1-P4 pass, later T7 work must retain:

```text
Z_N(s)=cos(Ns/2)
```

as the volume-uniform-zero-free countermechanism. This gate cannot discharge
T7(ii)-(iv).

## No-target attestation and fixed status

```text
connected_preparation_derived = false
all_finite_connected_baselines_nonzero_proved = false
connected_primitive_amplitude_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
