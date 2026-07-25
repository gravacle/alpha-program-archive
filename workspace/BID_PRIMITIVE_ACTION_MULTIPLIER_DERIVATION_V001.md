# BID Primitive Action-Multiplier Derivation v001

Date: 2026-07-23

## Question

Can the primitive attenuation be replaced by

```text
Gamma_c(A)=-c log|Z(A)|, c>0,
```

without changing the physical record theory?

## Primitive action character

The additive comparison variable is action phase:

```text
theta=S/hbar mod 2 pi.
```

Every continuous one-dimensional unitary character of `U(1)` is

```text
chi_n(exp(i theta))=exp(i n theta),
n in Z.
```

The kernel has order `|n|` when `|n|>1`. Therefore the only faithful
nontrivial primitive characters are

```text
n=+1 and n=-1.
```

They differ by orientation/complex conjugation. On the chosen positive
orientation branch the primitive character is `n=+1`.

## Consequence for the amplitude power

Let `Z(A)` be the normalized completed-record transition amplitude derived
from the complete source-record theory. Replacing it by `Z(A)^c` defines a
single-valued continuous action character only when `c` is an integer.

```text
c=0:
  trivial response;

|c|>1:
  nonfaithful character with a finite kernel, or an actual multiplicity of
  independent copies;

c=-1:
  orientation-reversed complex conjugate;

c=+1:
  the chosen primitive faithful branch.
```

Thus the one-record amplitude is

```text
Gamma_record(A)=-log|Z(A)|.
```

No independent positive real multiplier survives.

The probability cost

```text
-log|Z|^2=-2 log|Z|
```

belongs to a doubled amplitude/conjugate construction or to a probability
description. It is not the primitive one-branch effective action. A genuine
integer multiplicity must be derived from the carrier and is counted by
monoidal composition rather than absorbed into `c`.

## Effective-action convention

For the quantum amplitude,

```text
W(A)=-i hbar Log Z(A),
```

so

```text
Im W(A)/hbar=-log|Z(A)|.
```

This is a consequence of the standard `exp(iS/hbar)` action character, not a
fit to an electromagnetic response.

## Boundary

This derivation fixes the primitive multiplier only after the physical
normalized completed-record amplitude exists. It does not select that
amplitude's state, CTP contour, outcome sum, causal cell, durability, or
connected thermodynamic limit.

## Status

```text
continuous_U1_character_lattice_classified = true
faithful_primitive_characters_plus_minus_one_only = true
positive_orientation_character_plus_one_selected = true
noninteger_amplitude_power_admissible = false
integer_power_greater_than_one_primitive_faithful = false
probability_square_identified_as_primitive_amplitude = false
independent_positive_action_multiplier_survives = false
primitive_attenuation_multiplier_equals_one = true
complete_Q_spec_amplitude_derived = false
unique_physical_record_duration_derived = false
physical_Thomson_stiffness_computed = false
alpha_computed = false
proof_authorized = false
```
