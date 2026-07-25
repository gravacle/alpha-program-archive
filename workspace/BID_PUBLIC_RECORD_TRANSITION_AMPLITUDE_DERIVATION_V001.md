# BID Public Record-Transition Amplitude Derivation v001

Date: 2026-07-23

## Purpose

This derivation selects the primitive branch amplitude from the already
declared first-opening and public-closure semantics. It is performed before
any response or coupling value is evaluated.

## Boundary data

For a completed first-opening branch `h`, the source and public endpoint are
Hermitian lines

```text
L_r --U_h--> L_p_h.
```

Let

```text
i_r:L_r->H_h,
P_p_h:H_h->L_p_h
```

be the canonical root injection and endpoint projection. For physical
evolution `W_h(A;tau_R)` on the handle-conditioned carrier, the branch
transition is

```text
T_h(A)=P_p_h W_h(A;tau_R) i_r:L_r->L_p_h.
```

The connection supplies the canonical return comparison

```text
U_h^dagger T_h(A):L_r->L_r.
```

Because `L_r` is one-dimensional, this endomorphism is one complex scalar:

```text
a_h(A) I_(L_r)=U_h^dagger T_h(A).
```

The normalized primitive branch amplitude is

```text
Z_h(A)=a_h(A)/a_h(0).
```

## Why this object is selected

The first-opening object declares `p_h`, not `r`, to be the completed public
record alternative for branch `h`. Therefore the final support is fixed by
the endpoint summand and its canonical projector. The root survival amplitude
has the wrong final boundary condition: it asks whether the system remains
unresolved.

No endpoint basis is required. Under connection-preserving fiber maps

```text
eta_p U_h=U'_h eta_r,
eta_p T_h=T'_h eta_r,
```

and hence

```text
eta_r (U_h^dagger T_h)
  =(U'_h^dagger T'_h) eta_r.
```

The scalar `a_h` is natural and gauge invariant. Endpoint rephasing changes
`U_h` and `T_h` by the same phase and cancels in `U_h^dagger T_h`.

The branch probability is `|Z_h|^2` after normalization. The complex scalar
is retained because its phase is needed for action/holonomy comparison. The
inclusive completed-record probability is the sum of branch probabilities;
it is not substituted for the complex amplitude.

## Exact first-opening value

For the unit-incidence operator and

```text
tau_R=pi/sqrt(2),
```

the exact evolution is

```text
W_h(0;tau_R)i_r=U_h i_r
```

as a map into the endpoint line. Therefore

```text
a_h(0)=1,
Z_h(0)=1.
```

The normalization is thus nonzero and derived from completed-record transport.
It is not introduced to avoid the zero of the rejected survival amplitude.

## Scope boundary

This closes the primitive one-handle final-boundary and amplitude-selection
question. It does not prove:

```text
a volume-uniform zero-free neighborhood;
the connected many-record carrier or generator;
the physical durability/environment map;
the complete CTP amplitude;
or the Thomson coupling.
```

## Status

```text
completed_branch_final_support_derived = true
canonical_endpoint_projection_derived = true
connection_return_comparison_derived = true
primitive_complex_transition_amplitude_unique = true
primitive_transition_amplitude_gauge_invariant = true
primitive_transition_baseline_equals_one = true
root_survival_amplitude_excluded_by_record_semantics = true
volume_uniform_zero_free_neighborhood_proved = false
connected_many_record_amplitude_derived = false
complete_Q_spec_amplitude_derived = false
alpha_computed = false
proof_authorized = false
```
