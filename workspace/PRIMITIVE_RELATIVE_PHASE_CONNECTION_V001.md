# Primitive Relative-Phase Connection v001

## Scope

This result uses the hash-locked primitive two-alternative record carrier,
boundary recoverability, and the disclosed local `3+1` Lorentzian surface
branch. It derives a compact record-comparison connection. It uses no
electromagnetic coupling, particle mass, endpoint value, or candidate alpha
equation.

## Two local phase conventions

Let `|0>` and `|1>` be the two alternatives of one primitive comparison
record. A change of local basis representatives acts by

```text
(u_0,u_1) in U(1) x U(1),
|0> -> u_0 |0>,
|1> -> u_1 |1>.
```

The diagonal subgroup

```text
U(1)_diag = {(u,u)}
```

changes only the common representative phase. It changes no projective state
or public record statistic and is removed by the physical null quotient.

The surviving comparison group is therefore

```text
[U(1) x U(1)] / U(1)_diag
  isomorphic to U(1)_rel,

(u_0,u_1) -> u_1 u_0^(-1).
```

The displayed map is onto and its kernel is exactly `U(1)_diag`, so the
quotient contains one compact relative-phase handle and no second independent
phase handle.

## Primitive generator and characters

Choose the representative in which the reference alternative is fixed:

```text
U_rel(theta) = diag(1, exp(i theta)).
```

Its uncentered generator is

```text
Q = |1><1| = diag(0,1).
```

Adding a multiple of the identity changes only the removed common phase. The
centered representative is

```text
Q_0 = Q - (1/2) I = diag(-1/2,1/2).
```

Endpoint exchange sends `Q_0 -> -Q_0`; it does not produce a second physical
generator.

Continuous characters of `U(1)_rel` are

```text
chi_n(theta) = exp(i n theta),  n in Z.
```

The primitive faithful character has `|n|=1`. `n=0` is unfaithful and
`|n|>1` repeats the primitive winding. Orientation relates `n=1` and `n=-1`.
This yields stable integral charge units for the primitive record handle
without using the observed electromagnetic coupling.

## Localization

On overlapping local patches of the disclosed surface, let the relative basis
coordinate transform as

```text
z_1 -> exp(i theta(x)) z_1.
```

Ordinary differentiation of local representatives is not invariant under
this patch change. A comparison connection `a` is therefore required:

```text
D z_1 = (d - i a) z_1,
a -> a + d theta,
f = da.
```

Its Wilson character

```text
W_n(gamma) = exp[i n integral_gamma a]
```

is the compact parallel comparison of the primitive action phase. This is the
local connection implied by the record's relative-phase bundle.

## What is and is not derived

Derived:

```text
one compact relative-phase comparison group;
one generator modulo the common-phase identity;
integer character lattice;
primitive unit winding;
the need for a local comparison connection and curvature.
```

Not yet derived:

```text
that this record connection is the unique exterior electromagnetic field;
the source matter action and complete CTP specification;
the parity-even Maxwell stiffness;
the physical measure and ultraviolet completion;
the scale-dependent response K_R(mu);
alpha.
```

The next result must derive the physical identification and dynamics of this
connection. Compactness and charge units do not select the curvature-action
coefficient.

## Executable role

The companion audit verifies the quotient, generator, character composition,
source hashes, and fail-closed status. It is a regression guard, not evidence
beyond the group-theoretic derivation above.

## Status

```text
primitive_relative_phase_group_derived = true
primitive_relative_generator_rank = 1
primitive_character_lattice = Z
primitive_unit_winding_derived = true
local_record_comparison_connection_derived = true
identification_with_unique_exterior_EM_connection_derived = false
absolute_Maxwell_stiffness_selected = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
