# Complete-Q_spec Relative-History CTP Amplitude Specification v001

Date: 2026-07-25

## Purpose

Derive the scalar connected amplitude at the complete-`Q_spec` level from
the already-disclosed incoming state and the complete unitary
source-record parent. This gate follows the primitive source-scalarization
no-go and does not alter the pending Stage-8 verdict.

No coupling target may be read or used.

## Frozen authorities

```text
5026afb89b52ead9f309168cb2fa4f06b81039f8dd01b8940f40e64aad679a7e  STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md
6f6b822ac8ccf9ea19659f4ccf811268f60a27a361f817ee6513479d63b62546  BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md
345d447eaf6d730caa6fa655b92a7b0cd93a68b5f86e0c8929cf969f40aeb7cb  R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md
e30f2e631204df2416b9aa38e55c2710db1d676749fcd2fbdb6604388f3ea391  COMPLETE_ONE_CELL_CTP_KERNEL_GATE_V001.md
451550c3825288d699db35c7289e408e8314ad042450253b58f32722c4ead46b  BID_MONOIDAL_EXTENSIVITY_DERIVATION_V001.md
10909b5c21e73ecf655462339a27bd645b8d35e3ad11fb6f8cb204c601992995  R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md
6447eb80c9347e614a1ecfbfef6234e4acec5caadf829a8649fdb5282439aa09  STAGE8_T7_SOURCE_SCALARIZATION_NO_GO_RESULT_V001.md
```

Any mismatch aborts execution.

## Q1 - Complete relative-history functional

Let `omega_in` be the disclosed incoming source state tensored with all
ready record states. For a finite causal parent `K`, let `W_K[A]` be its
complete unitary source-record evolution in the external connection
history `A`.

Define:

```text
Z_K[A_+,A_-]
 =omega_in(W_K[A_-]^dagger W_K[A_+]).
```

The record sum is complete because the identity on every final record
factor is retained. No public outcome is postselected. No source ray,
finite normalized trace, determinant, or final source covector is added.

This is the algebraic Schwinger-Keldysh/influence functional for two
external histories. The state supplies the scalar functional at complete
`Q_spec`, exactly where the primitive no-go says it must enter.

## Q2 - Required exact identities

Derive:

```text
Z_K[A,A]=1;
Z_K[A_+,A_-]^*=Z_K[A_-,A_+];
|Z_K[A_+,A_-]|<=1;
```

and simultaneous gauge covariance/invariance under a common gauge
transformation of both histories, state, and parent.

For disjoint parents with factorized incoming states:

```text
Z_(K1 disjoint K2)=Z_K1 Z_K2;
-log|Z_(K1 disjoint K2)|
 =-log|Z_K1|-log|Z_K2|.
```

Connected cellulations still require a linked-cluster theorem.

## Q3 - Exact one-cell comparator

Recompute the complete two-outcome comparator:

```text
|+>=(|0>+|1>)/sqrt(2);
U(theta)=diag(1,exp(i theta));

Z(theta_+,theta_-)
 =<+|U(theta_-)^dagger U(theta_+)|+>
 =[1+exp(i(theta_+-theta_-))]/2.
```

Verify:

```text
Z(theta,theta)=1;
Z(theta_+,theta_-)^*=Z(theta_-,theta_+);
[-log|Z(delta,0)|]''_(delta=0)=1/4.
```

The exclusive preserved-reference probability `|A_+|^2` is not substituted
for this complete kernel.

## Q4 - Relation to the primitive no-go

The primitive connected compression remains operator-valued. Q1 does not
contradict that result: `omega_in` is complete-`Q_spec` state content, not a
canonical primitive trace.

The execution must report:

```text
primitive_source_scalarization_derived = false;
complete_Qspec_CTP_scalar_closure_derived = true
```

only if Q1-Q3 pass.

## Q5 - Scope ceiling

This gate may derive the finite/algebraic scalar closure and its exact
one-cell regression. It may not claim:

```text
the interacting continuum CTP measure;
gauge fixing, ghosts, or edge completion;
a volume-uniform zero-free neighborhood;
the connected linked-cluster density;
the Maxwell tensor form;
the Thomson stiffness;
or alpha.
```

Those remain successor obligations.

## Verdict rule

Return:

```text
COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_CLOSURE_DERIVED
```

only if all authority hashes and Q1-Q4 pass. Otherwise return:

```text
COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_CLOSURE_BLOCKED
```

## Fixed status

```text
primitive_source_scalarization_derived = false
complete_Qspec_CTP_scalar_closure_derived = false
interacting_continuum_CTP_amplitude_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
