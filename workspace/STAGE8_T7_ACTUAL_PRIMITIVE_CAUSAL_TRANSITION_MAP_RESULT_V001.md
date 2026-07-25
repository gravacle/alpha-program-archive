# Stage-8 T7 Actual Primitive Causal Transition-Map Result v001

Date: 2026-07-24

## Verdict

```text
ACTUAL_PRIMITIVE_CAUSAL_TRANSITION_MAP_BLOCKED
```

The candidate execution derived an exact result for the stripped incidence
zero-form, but it did not execute the sealed Lorentzian parent and therefore
does not derive the physical `A`-dependent connected amplitude.

The candidate JSON verdict
`ACTUAL_PRIMITIVE_CAUSAL_TRANSITION_MAP_DERIVED` is superseded by this
adjudication.

## Result retained

For the isolated incidence zero-form, endpoint compression at
`tau_R=pi/sqrt(2)` gives:

```text
E_j=P_j tensor I_spin.
```

Consequently, on the finite path fixture:

```text
P_(N-1)...P_0
 =(-1/2)^(N-1)|u_(N-1)><u_0|,
```

with nonzero finite baselines for every `N`. The primary and independent
Gram-recurrence verifier reproduce this exact identity through `N=8`.

The strongest positive status is:

```text
BASELINE_ZERO_FORM_PROJECTOR_CHAIN_IDENTITY_DERIVED
```

## Why the physical transition remains blocked

The sealed Lorentzian parent is:

```text
h_K(t)
 =h_0[g,A]
  +sum_c v_c(t) M_c(t) tensor S_n tensor iota_c(c_c).
```

It contains the free source generator, causal envelope, spatial support, and
time ordering. The candidate replaced this parent by the integrated
zero-form pulse:

```text
exp(-i tau_R P_j tensor gamma^5 tensor c_j).
```

Those objects are not equivalent. In the existing complete-parent
regression, the first pointer probability is approximately
`0.9252683055811919`, not exact unit transfer. Therefore the candidate
identity cannot be promoted to the actual Lorentzian transition.

The candidate also:

```text
contains no nonzero connection variable A;
constructs the final source-line range map directly;
uses transpose rather than an A-dependent adjoint connection transport;
and verifies stored algebraic identities rather than independently evolving
the Lorentzian parent.
```

The actual outgoing record object is source-dressed, not a bare record line.

There is also an exact geometric obstruction. The tested incidence carrier
is a tree. Every `U(1)` connection on a tree is gauge-equivalent to the
trivial connection, so a gauge-invariant returned scalar on this carrier
cannot detect physical holonomy. Nonzero electromagnetic stiffness requires
a derived causal carrier containing a closed comparison route, such as a
face or loop, rather than a phase decoration of the open line.

## Hostile response audit

Even within the stripped zero-form fixture, the covariant incidence overlap
is:

```text
<u_j(A_j),u_(j-1)(A_(j-1))>
 =-(1/2) exp(i A_(j-1)).
```

Hence:

```text
|Z_N(A)|=1,
-log|Z_N(A)|=0,
Hessian[-log|Z_N(A)|]=0.
```

The exact verdict is:

```text
OPEN_LINE_HOLONOMY_ZERO_STIFFNESS
```

The Stage-8 boundary routes exact-zero stiffness to `BLOCKED`; it cannot be
repaired by a branch sum, source state, trace, determinant, envelope change,
or added residual term.

## Verification limitation

The candidate verifier independently checks the local three-state endpoint
unitary, but it does not independently reconstruct the full chain or evolve
the Lorentzian parent. It also treats the candidate verdict string as an
expected value. It therefore verifies the retained local algebra only and
cannot support the superseded physical-map verdict.

## Remaining physical obligation

The next admissible object must use the actual Lorentzian parent and derive,
without postselection:

```text
the fixed completed public output in its source-dressed range;
the normalized A-dependent complex amplitude;
a nonzero volume-uniform zero-free response;
and its connection to the periodic F1 Duhamel tensor.
```

If no such primitive object exists, the amplitude/cluster/Hessian step must
move downstream to complete `Q_spec` rather than being forced into primitive
T7.

The sealed authority chain for any successor must also hash-pin the causal
direct-limit/relay authority and the shared-source causal-parent authority;
the candidate specification did not pin both.

## Response-audit artifacts

```text
8b53704d5ba0f49bec6c385984ea8d68d00a04f218c0db47092e5890bdbe127d  STAGE8_T7_ACTUAL_PRIMITIVE_TRANSITION_RESPONSE_AUDIT_SPEC_V001.md
05343c45d4096f90605326d796de3476717900739f6483c54fd50c9b146f3c69  scripts/audit_stage8_t7_actual_primitive_transition_response_v001.py
20493c399cb5b1d6e0d282c05625f5008242e7728f342f200681fa34ed459b59  stage8_execution/work/T07_actual_primitive_transition_response_audit.json
6abc9c00bc628dfe94e244b43f090449bb17b0459403853b9d93f321ae861c94  scripts/verify_stage8_t7_actual_primitive_transition_response_v001.py
e56372ba30ee2ec60424b138a724a2778b9d8a7cb4b62faa33afc585b8c2c90c  stage8_execution/work/T07_actual_primitive_transition_response_audit_verification.json
```

## Fixed status

```text
actual_A_dependent_connected_amplitude_derived = false
physical_final_source_line_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
