# Stage-8 T7 Relayed-Family Resolution Spec v001

Date: 2026-07-24

## Status

```text
SPECIFICATION_SEALED_BEFORE_EXECUTION
```

This gate tests whether the pulled-forward primitive Q_spec lineage fixes the
residual family `F(S,chi,beta,sigma,I)` inside the already-declared
causally-sequential, pure-charge, single-incidence branch. It does not choose
a family member, compute a response, or enlarge the branch.

## Hash-pinned authorities

```text
29c32f90e6a4f88a26e22c91504b6d92a1fc4083ad6368984a1e94858caa4365  STAGE8_T7_RELAY_DEPENDENCY_ORDER_AMENDMENT_V001.md
781608f2fe4c8753a0c06b1d87407b2a6c88caa0ab45329e1200160e56292a24  R3_4_SHARED_SOURCE_CAUSAL_PARENT_RESULT_V001.md
b786db3adec8cc335967d49ec13b59923d67f424644f72c535b27b579dd1489f  BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md
6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb  BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md
7471988138233218430c6b6dd07b39f33508a75907557723654dbc712c0c4476  BID_FIRST_OPENING_INTERVAL_DERIVATION_V001.md
1d114e71c29c3a39b7afd1b7a80b47afb52fe77e8ee1e4e19b604defe3c69305  R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_RESULT_V001.md
10909b5c21e73ecf655462339a27bd645b8d35e3ad11fb6f8cb204c601992995  R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md
edb0ba6d25a8a4c4182189b4f5b2b2f0cb3b7e916ad959ee87a51c6d3a43c915  BID_SOURCE_DECORATED_FIRST_OPENING_CLASSIFICATION_V001.md
e12fffcc0f94d6896bc5607898db6b3a1ea343aeaf557b1f6f70e58db061fab6  STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md
```

Any mismatch aborts execution.

## Declared scope

The admissible branch is fixed before the tests:

```text
one global source carrier;
pure compact-vector-U(1) access;
one normalized primitive incidence line per active cell;
causally sequential cell additions;
one fresh record factor per primitive event;
and the branch-resolved complex transition amplitude.
```

Spacetime-concurrent cells, multi-handle public outputs, charge-changing
sources, gravity-plus-charge composite handles, and the complete
source-inclusive CTP amplitude are not silently added to this branch.

## F1 - Transport/cell assignment S

Rebuild the three-cell incidence chain:

```text
d_j=e_(j+1)-e_j,
P_j=|d_j><d_j|/2.
```

Verify exactly:

```text
Tr(P_0P_1)=Tr(P_1P_2)=1/4;
Tr(P_0P_2)=0.
```

Construct the corresponding record-write unitaries at `tau_R`. Confirm:

```text
adjacent overlapping cells do not commute;
nonadjacent cells commute;
reversing an adjacent pair changes the parent;
and every later cell is the identity on prior completed record factors.
```

Within a declared causal order, `S` passes as fixed only if every overlapping
pair is ordered by that causal order and permutations of disjoint cells give
the same map. A second inequivalent assignment satisfying these same
conditions returns `FAMILY_SURVIVES`.

## F2 - Active handle chi

Verify that the authority derives:

```text
P_ch=1_(R\{0})(Q),
B_ch=P_ch tensor B_Q,
(a_0,a_+,a_-)=(0,1,1).
```

Test the rescaled competitor `lambda P_ch tensor B_Q`. It must fail the
projection-module retraction for every `lambda != 1`. A neutral charged
write and a second primitive charged line must remain inadmissible in the
declared branch.

## F3 - Endpoint beta

Verify that the minimal pure-charged first-opening object has exactly one
public endpoint `p_Q` for its active handle and that:

```text
root survival is unresolved, not completed;
parallel paths or multiple endpoints are enlarged branches;
and a later endpoint cannot be selected after response evaluation.
```

For a causally sequential history, `beta` is the endpoint attached to the
already-fixed active cell. If two completed endpoints remain in the declared
one-arrow branch, return `FAMILY_SURVIVES`.

## F4 - Conditioning sigma

The response-closure result must select the normalized complex-linear,
branch-resolved return:

```text
Z_h(A)=a_h(A)/a_h(0).
```

Recompute the exact relative-holonomy witness:

```text
FS curvature                         = 1/4;
linear-amplitude attenuation         = 1/4;
endpoint-probability attenuation     = 1/2;
inclusive-sandwich attenuation       = 0.
```

Only the linear branch-resolved amplitude is admissible as the primitive
response closure. Equal scalar components may not identify a component
amplitude, endpoint vector, normalized symmetric amplitude, and inclusive
probability.

## F5 - Interval I

Verify:

```text
tau_R=pi/sqrt(2)
```

as the least positive exact-transfer interval on the normalized one-arm
block. For every mixed star `m>1`, use:

```text
|q_m(t)|<=2/(m+1)<1;
|q_sym,m(t)|<=2 sqrt(m)/(m+1)<1.
```

Therefore no mixed replacement interval exists. A searched or target-chosen
interval is forbidden.

## Verdicts

```text
RELAYED_FAMILY_RESOLVED_IN_DECLARED_BRANCH
  iff F1-F5 each leave exactly one admissible operation in the declared
  branch and every listed negative control fails;

RELAYED_FAMILY_SURVIVES
  iff any F coordinate retains two inequivalent admissible operations;

RELAYED_FAMILY_GATE_BLOCKED
  iff an authority drifts or an exact regression fails.
```

Passing this gate authorizes only construction of the relayed finite
primitive amplitude. It does not pass T7(ii)-(iv), compute `kappa_record`,
or authorize a coupling calculation.

## No-target attestation

No measured coupling, alpha, endpoint, cosmological value, or
response-selected coefficient may be read or used.

## Fixed status

```text
relayed_family_resolved = false
connected_primitive_amplitude_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
