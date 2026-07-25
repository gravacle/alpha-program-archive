# Stage-8 Route-2 Complete-Q_spec State Binding v001

## Purpose

Pin the already-disclosed complete-`Q_spec` incoming state before it is
used to evaluate the newly derived primitive all-outcome operator kernel.
This is a provenance binding, not a new state choice and not a primitive
scalarization.

## Frozen authorities

| Role | Path | SHA-256 |
|---|---|---|
| Stage-7 declared branch and state content | `STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md` | `5026afb89b52ead9f309168cb2fa4f06b81039f8dd01b8940f40e64aad679a7e` |
| Free quasifree state and CTP contour derivation | `BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md` | `6f6b822ac8ccf9ea19659f4ccf811268f60a27a361f817ee6513479d63b62546` |
| Complete-Q_spec CTP closure specification | `COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_AMPLITUDE_SPEC_V001.md` | `ddb51c32e1ec45e6145be4c688f2af5fa87823ab20b4f523fc4657823165e544` |
| Complete-Q_spec CTP closure result | `COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_AMPLITUDE_RESULT_V001.md` | `273e1473a1a8bf0be0467634411cec1b7daeee0c9f24c330fad5d288d191dcbb` |
| Complete causal parent result | `R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md` | `345d447eaf6d730caa6fa655b92a7b0cd93a68b5f86e0c8929cf969f40aeb7cb` |
| Primitive operator-response result | `STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_RESULT_V001.md` | `76f5505e3aa1fdc11102f782ed8ee40e49787bb38e3a2524e17b92fd8de46740` |

## Bound state and evaluation

The declared ordinary branch supplies:

1. the stationary quasifree incoming source state of the frozen free
   Hamiltonian `h_0`;
2. its derived positive/negative spectral projectors and complete free CTP
   contour; and
3. the predeclared ready state on every record factor.

Their product is the already-disclosed incoming state functional
`omega_in` on the complete source-record algebra.

The primitive result supplies the all-outcome relative-history operator

```text
R_all,K[A_+,A_-]
 =i_r^dagger W_K[A_-]^dagger W_K[A_+] i_r.
```

Only at complete `Q_spec`, after the state is present, is the scalar
functional evaluated:

```text
Z_K[A_+,A_-]
 =omega_in(W_K[A_-]^dagger W_K[A_+])
 =omega_source(R_all,K[A_+,A_-]).
```

This is the same scalar closure already derived and independently checked
in the pinned complete-`Q_spec` CTP result. The current binding prevents a
different state, postselection, determinant, normalized trace, or
record-conditioned scalar from being selected after seeing the primitive
operator response.

## Scope ceiling

The binding closes the state identity and the finite/algebraic
operator-to-scalar type transition. It does not establish:

```text
complete parameter-free Q_spec;
interacting continuum CTP amplitude;
source-inclusive projective-limit state;
continuum regulator independence;
volume-uniform zero-free neighborhood;
linked-cluster density;
intensive Hessian equality;
response coefficient;
coupling;
alpha.
```

In particular, the stationary quasifree in-state is disclosed
ordinary-branch content. Its use here must not be relabeled as a unique
interacting-vacuum derivation.

## Protected status

```text
complete_Qspec_state_hash_pinned_for_route2 = true
complete_Qspec_CTP_scalar_closure_derived = true
primitive_source_scalarization_derived = false
complete_parameter_free_Qspec_frozen = false
interacting_continuum_CTP_amplitude_derived = false
source_inclusive_state_projective_limit_derived = false
continuum_regulator_independence_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
