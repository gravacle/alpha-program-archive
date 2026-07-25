# Complete One-Cell CTP Kernel Gate v001

Date: 2026-07-23

## Purpose

This gate tests whether the squared reference fidelity used in
`PRIMITIVE_ADDITIVE_RECORD_FIDELITY_ACTION_V002.md` is the complete
trace-preserving influence kernel of the primitive two-outcome comparator.

No coupling or electromagnetic target value is used.

## Complete outcomes

Define

```text
|+> = (|0> + |1>)/sqrt(2),
|-> = (|0> - |1>)/sqrt(2),
U(theta) = diag(1, exp(i theta)).
```

The complete reference-basis outcome amplitudes are

```text
A_+(theta)
  = <+|U(theta)|+>
  = exp(i theta/2) cos(theta/2),

A_-(theta)
  = <-|U(theta)|+>
  = -i exp(i theta/2) sin(theta/2).
```

They obey

```text
|A_+(theta)|^2 + |A_-(theta)|^2 = 1.
```

The squared fidelity retained by the earlier candidate is only

```text
F_R(theta) = |A_+(theta)|^2.
```

It is the probability of one exclusive preserved-reference outcome.

## Doubled kernel

After summing the complete outcomes, the one-cell doubled influence kernel is

```text
I(theta_+,theta_-)
  = sum_(s in {+,-})
      A_s(theta_+) A_s(theta_-)^*

  = <+|U(theta_-)^dagger U(theta_+)|+>

  = [1 + exp(i(theta_+ - theta_-))]/2.
```

Therefore

```text
I(theta,theta) = 1,
I(theta_+,theta_-)^* = I(theta_-,theta_+).
```

The diagonal normalization is required for a trace-preserving CTP influence
functional. It is not equal to `F_R(theta)` except at response-null points.

## Consequence

The squared reference fidelity is a conditional, trace-decreasing component.
It cannot be the complete parent action of a closed unitary record theory.

Writing

```text
exp(-S_cell/hbar) = F_R
```

may define a postselected likelihood cost or a Euclidean lattice ansatz, but
it does not follow from the complete two-outcome CTP kernel.

The complete kernel contains a phase and a decoherence/noise structure as a
function of the branch difference. It does not generate a branchwise
Lorentzian Maxwell term by itself.

## Status

```text
complete_two_outcome_kernel_derived = true
trace_preserving_diagonal_normalization = true
ctp_hermiticity = true
squared_reference_fidelity_is_one_exclusive_component = true
fidelity_weight_is_complete_parent_CTP_action = false
primitive_fidelity_action_retained_as_diagnostic_only = true
complete_dynamical_record_kernel_derived = false
real_public_Maxwell_response_derived = false
finite_c_F2_deformation_excluded = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```

## Next admissible route

A parent action must generate nontrivial propagation before closure. It must
fix, in one specification:

```text
the record/source fields and state;
the unitary branch amplitudes;
the complete outcome/Kraus structure;
the CTP measure and contour;
the causal-cell boundary conditions;
and the real transverse response.
```

Only the complete kernel may then be reduced to an Euclidean transfer action
and tested for a Maxwell continuum limit.

