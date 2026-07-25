# BID Physical Record-Amplitude Zero-Free Gate v001

Date: 2026-07-23

## Purpose

This gate identifies a necessary correction before any many-record logarithm,
linked-cluster expansion, response Hessian, or coupling evaluation. It uses no
alpha, endpoint, mass, or measured response value.

## Exact obstruction

For the sealed handle-conditioned first-opening operator,

```text
<r|U_h(tau)|r> = [1+cos(sqrt(2) tau)]/2
                = cos^2(tau/sqrt(2)).
```

At the independently derived first-opening interval

```text
tau_R=pi/sqrt(2),
```

the root is mapped to the public endpoint:

```text
U_h(tau_R)|r>=|p_h>.
```

Therefore

```text
<r|U_h(tau_R)|r>=0,
-log|<r|U_h(tau_R)|r>|=+infinity.
```

The root survival amplitude cannot be the baseline amplitude for the V011
response. It has no nonzero reference value, no logarithm branch through
`A=0`, and no finite local Hessian. Tensoring this zero over cells does not
repair it.

## Candidate physical objects

The same exact calculation gives

```text
<p_h|U_h(tau_R)|r>=1.
```

This makes the branch-conditioned completed-record transition amplitude a
plausible candidate. Other mathematically possible objects include:

```text
the inclusive completed-record probability;
a vector of branch transition amplitudes;
a determinant or trace over a derived public endpoint carrier;
and the complete CTP amplitude Z_Q[A]/Z_Q[0].
```

The transition amplitude was not selected by this negative gate. It is
subsequently selected from the completed-record endpoint semantics in
`BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md`, not because the
survival amplitude vanishes.

## Selection and zero-free obligations

Before an amplitude enters `Gamma=-log|A|`, the complete record semantics must:

1. derive the final bra, effect, projector, trace, or CTP boundary condition
   from public closure and durability;
2. show gauge and handle covariance;
3. prove exact composition on disjoint record systems;
4. prove its unperturbed value is nonzero;
5. normalize only by that derived value;
6. prove a volume-uniform zero-free neighborhood containing the response
   point; and
7. prove that the first two connection derivatives survive the
   thermodynamic limit.

For a branch-conditioned amplitude the candidate normalization is

```text
Z_h[A]
  = <p_h|U_h(A;tau_R)|r>
    / <p_h|U_h(0;tau_R)|r>.
```

The public-record derivation now independently selects `p_h` as the primitive
final boundary condition and authorizes this one-handle formula. The complete
`Q_spec` may replace this primitive object with a CTP amplitude; the two must
not be identified by notation alone.

## Status

```text
root_survival_amplitude_at_tau_R_zero = true
root_survival_log_response_rejected = true
completed_record_transition_baseline_nonzero = true
primitive_response_amplitude_selected = true
public_final_boundary_condition_derived = true
volume_uniform_zero_free_neighborhood_proved = false
thermodynamic_log_hessian_authorized = false
primitive_record_stiffness_computed = false
alpha_computed = false
proof_authorized = false
```

## Next gate

Derive the physical final boundary condition from the public-closure and
durability rules before comparing candidate amplitudes. Then test the selected
object for zero-freeness and connected-cluster control at `tau_R`.
