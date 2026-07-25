# Stage-8 T7 Causal-Line Connection-Return Lift Spec v001

Date: 2026-07-24

## Status

```text
SPECIFICATION_SEALED_BEFORE_EXECUTION
```

This gate tests whether the already-derived one-handle
connection-returned amplitude extends functorially to the relayed causal
source lines. It adopts no source state, in/out prescription, response
coefficient, or new closure principle.

The full-source state-expectation route has already failed and remains
sealed. This gate may pass only if the linear in/out functional is forced by
the same line-valued boundary data and the same connection-return theorem
that predate that failure.

## Hash-pinned authorities

```text
21b782b50e9b0ddf1785727ff625a2b933d370aaf539c9fea74982025279b729  STAGE8_T7_RELAYED_CONNECTED_PREPARATION_RETEST_RESULT_V001.md
b2e8cd624bb7ee5c946762d423e8dcee5a4527dcc92d9724064d8ffb3e5beaf1  stage8_execution/t7_relayed_connected_preparation_retest/T07_RELAYED_CONNECTED_PREPARATION_RETEST_V001.seal.sha256
e12fffcc0f94d6896bc5607898db6b3a1ea343aeaf557b1f6f70e58db061fab6  STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md
6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb  BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md
52187f8174b203d3cf2acb641d800f45ae733331cc0f3d56658898ed7daec244  BID_BOUNDARY_METRIC_TRANSPORT_DERIVATION_V001.md
52401eefc3ff84e22f04bbc329a619b830058661db7f969d2d43d167d97d893d  STAGE8_T7_RELAYED_FAMILY_RESOLUTION_RESULT_V001.md
2be95d5b58ea000df9a30b717a809374a90693f78a893d87b73a12e4be97fa21  R3_4_CHARGED_INCIDENCE_OUTGOING_STATE_RESULT_V002.md
1d114e71c29c3a39b7afd1b7a80b47afb52fe77e8ee1e4e19b604defe3c69305  R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_RESULT_V001.md
```

## Q1 - Typed causal source lines

For a fixed completed causal history with source supports `P_j`, define:

```text
L_j=im(P_j).
```

This gate is restricted to the already-declared rank-one source-incidence
history. Each `L_j` is therefore a one-dimensional Hermitian line. The
completed record factors are retained in their durable output labels, while
the next ready root is supplied by the sealed relay.

Histories with rank-greater-than-one active supports or multiple unresolved
future endpoints are enlarged branches and fail this gate rather than being
reduced by a trace.

## Q2 - Connection transport

For every adjacent pair with nonzero causal attachment, derive the oriented,
metric-compatible isometry:

```text
V_(j,j-1):L_(j-1)->L_j.
```

Its phase is fixed by the existing oriented source transport. A local
rephasing must transform `V` and the physical transition together and cancel
in `V^dagger T`.

For a history of length `N`, define:

```text
V_N=V_(N-1,N-2)...V_(1,0):L_0->L_(N-1).
```

No isometry may be defined from the perturbed response being evaluated.

## Q3 - Relayed physical transition

Compress the exact primitive controlled-write product onto the already-fixed
completed record labels. Restrict the remaining source operator to the typed
boundary lines:

```text
T_N(A)
 =P_(N-1) K_N(A) i_0
 :L_0->L_(N-1).
```

The relayed connection-return is:

```text
V_N^dagger T_N(A):L_0->L_0.
```

Since `L_0` is one-dimensional, the sealed D3 closure theorem requires:

```text
V_N^dagger T_N(A)=a_N(A) I_(L_0).
```

The normalized branch amplitude is:

```text
Z_N(A)=a_N(A)/a_N(0).
```

## Q4 - Exact chain execution

On the exact incidence chain:

```text
<e_j,e_(j-1)>=-1/2,
K_N(0)=P_(N-1)...P_0,
V_N |e_0>=|e_(N-1)>.
```

Derive:

```text
a_N(0)=(-1/2)^(N-1)
```

for arbitrary finite `N>=1`, and execute `N=1,...,8` as a regression.
Every finite baseline must be nonzero.

The one-cell restriction must return `a_1(0)=1` and the pinned public
record-transition amplitude.

## Q5 - Uniqueness and negative controls

Prove the linear source-line closure is fixed before the failed
state-expectation table by:

```text
the already-selected complex-linear response closure;
the fixed initial and final causal source lines;
the metric-compatible connection return;
and End_C(L_0)=C.
```

Explicitly retain:

```text
full-source state expectation: rejected for the primitive line amplitude;
inclusive probability/sandwich: rejected by the FS witness;
response-dependent final line: rejected;
polar return computed from K_N(A): rejected;
branch sum: not substituted for the branch amplitude.
```

The source line boundary functional is primitive and branch resolved. It is
not the finite Lorentzian wavepacket parent, and it is not the normalized
interacting CTP amplitude of the complete Q_spec.

## Verdicts

```text
FINITE_RELAYED_CONNECTION_RETURN_AMPLITUDE_DERIVED
```

requires Q1-Q5, nonzero arbitrary-finite-`N` baseline, and exact one-handle
reduction.

```text
CAUSAL_LINE_CONNECTION_RETURN_LIFT_BLOCKED
```

is required if the source lines, return isometry, phase covariance, or
arbitrary-`N` nonzero baseline is not derived.

Passing this gate closes only the finite branch-resolved amplitude. It does
not prove a volume-uniform zero-free neighborhood, linked-cluster density,
or thermodynamic Duhamel equality.

## No-target and fixed status

```text
finite_relayed_connection_return_amplitude_derived = false
connected_primitive_amplitude_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
