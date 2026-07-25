# Primitive Relative-Phase Stabilizer v002

## Correction of v001

Version 001 incorrectly promoted passive basis rephasing into a physical local
gauge freedom. It also described the matrix rank of one chosen generator
representative as though rank were invariant after quotienting by the
identity. Those claims are retired.

This version preserves only the group-theoretic result supported by the
hash-locked primitive carrier. It evaluates no electromagnetic response or
coupling.

## Ordered endpoint structure

The primitive record carrier contains two declared durable endpoint
alternatives. Let their projectors be

```text
P_0 = |0><0|,
P_1 = |1><1|.
```

Their existence is inherited. The order is a declared comparison convention:
it records which endpoint is the reference and which is the compared
alternative. If that convention were removed, endpoint exchange would add a
discrete `Z_2` factor. Transformations that mix the two rays continuously
change the declared endpoint alternatives and are not stabilizers of this
fixed ordered comparison context.

The unitary stabilizer that preserves each endpoint ray separately is

```text
Stab(P_0,P_1) = U(1) x U(1).
```

This is an active stabilizer statement. A passive change of basis, accompanied
by the inverse coordinate change, is only a description change and supplies no
physical gauge field.

## Projective quotient

The center

```text
U(1)_diag = {(u,u)}
```

acts as a common phase and is null on projective record statistics. The
effective active stabilizer is therefore

```text
Stab(P_0,P_1) / U(1)_diag
  isomorphic to U(1)_rel,

(u_0,u_1) -> u_1 u_0^(-1).
```

The map is onto and its kernel is exactly `U(1)_diag`. Consequently the
relative Lie algebra is one-dimensional: there is one independent generator
modulo the identity.

One may use either

```text
Q = diag(0,1)
```

or the centered representative

```text
Q_0 = diag(-1/2,1/2).
```

Their matrix ranks differ, so no rank claim is attached to the quotient
generator.

## Characters

Once the effective stabilizer is established as `U(1)`, its continuous
characters are

```text
chi_n(theta) = exp(i n theta),  n in Z.
```

This derives the character lattice as a mathematical property of the
stabilizer. The primitive unit winding used by the comparator is inherited
from the separately sealed primitive additive-action representation, where
faithfulness after quotienting response-null kernels is an explicit premise.
It is not newly derived here as an electromagnetic charge spectrum.

## Localization gate

The result above is pointwise. It does not imply that the relative active
stabilizer may vary independently at every surface point.

If a later target-independent theorem establishes all of the following:

```text
the endpoint comparison frame is local;
independent smooth relative-frame changes are physically redundant;
comparison data must be transported between overlapping patches;
```

then a connection with

```text
D = d - i a,
a -> a + d theta
```

is required for covariant comparison. Those premises are not established by
the current sealed sources. Accordingly, this document neither introduces
`a` as a physical field nor identifies it with electromagnetism.

## What is established

```text
endpoint_projectors_inherited = true
reference_comparison_order_declared = true
endpoint_ray_stabilizer_derived = true
effective_projective_stabilizer = U(1)
relative_lie_algebra_dimension = 1
relative_character_lattice = Z
primitive_unit_winding_inherited_conditionally = true
```

## What remains open

```text
passive_basis_freedom_is_physical_symmetry = false
local_relative_frame_redundancy_derived = false
physical_comparison_connection_derived = false
unique_dynamical_connection_derived = false
identification_with_unique_exterior_EM_connection_derived = false
absolute_Maxwell_stiffness_selected = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```

## Executable role

The companion audit checks the endpoint stabilizer, common-phase quotient,
character composition, provenance hashes, and fail-closed status. It does not
test or certify the physical premises needed for localization.

## Status

```text
PASS_ORDERED_ENDPOINT_PROJECTIVE_STABILIZER_ONLY
LOCAL_CONNECTION_OPEN
EM_IDENTIFICATION_OPEN
ALPHA_FALSE
```
