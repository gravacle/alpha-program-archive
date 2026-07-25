# BID Public-Record Hilbertization Derivation v001

Date: 2026-07-23

## Purpose

Derive the elementary record-label metric and its composition law from the
declared meaning of a public quantum record, without using alpha or any
downstream response.

## Disclosed kinematic inputs

This derivation uses ordinary quantum probability kinematics:

```text
QR1. A finite elementary public record register is a finite set X of
     durably distinguishable labels.

QR2. Perfectly distinguishable labels are the mutually orthogonal spectral
     projections P_x of one public pointer observable.

QR3. The conditioned elementary state in ran(P_x) is normalized, and its
     singleton inclusion into any larger register is probability preserving.

QR4. Amplitudes add linearly and probabilities obey the Born norm.

QR5. Relabeling X acts by a probability-preserving map.

QR6. Independent registers X and Y have joint labels X cross Y, and product
     record probabilities factor.

QR7. Products of record-preserving maps act componentwise on X cross Y.
```

These are kinematic record axioms. They are not inferred from alpha, an
endpoint value, or the desired incidence coefficient.

## Objectwise metric

Let the label carrier be the free complex vector space on `X`, and begin with
an arbitrary positive Hermitian Gram form. Write the label vectors as
`delta_x`.

Orthogonality of the pointer projections gives

```text
P_x P_y=0
and
<delta_x,delta_y>=0
for x != y.
```

QR3 fixes the norm of every label vector inside every register, not merely
inside the one-label object. Hence

```text
H_record(X)=ell^2(X),
<delta_x,delta_y>=delta_(x,y).
```

Probabilistic weights belong to the state amplitudes, not to a hidden
label-dependent Gram weight.

## Maps and composition

An injective record-preserving map with unit line phases sends

```text
delta_x -> u_x delta_(f(x)), |u_x|=1,
```

and is an isometry. Identities and compositions follow from those of `f` and
the line phases.

Disjoint alternatives obey

```text
ell^2(X disjoint-union Y)
  is canonically ell^2(X) direct-sum ell^2(Y).
```

QR6 and QR7 give the independent-register law

```text
ell^2(X cross Y)
  is canonically ell^2(X) tensor ell^2(Y),
delta_(x,y) <-> delta_x tensor delta_y.
```

The canonical maps satisfy the unit, associativity, and swap coherence
relations on the label basis. Thus the public-record assignment has the
direct-sum structure for exclusive alternatives and, given the disclosed
independent-system composition rule QR6-QR7, the strong symmetric monoidal
tensor structure for independent registers.

## Source-decorated consequence

If source transport is compatible with the positive hypersurface metric, each
source-labeled sector carries that same `h_n` metric, and its singleton
inclusion is isometric, the source-record product metric is fixed:

```text
h_source-record=h_n tensor I_record.
```

This does not copy the source algebra per record. It supplies only the local
metric; the global source remains the one CAR algebra constructed separately.

## Earned result and boundary

Given QR1-QR7 and standard Born kinematics, public record labels carry the
unique counting Hilbert metric, and independent record registers compose
canonically by tensor product. This discharges the earlier arbitrary-Gram
freedom.

The result does not derive Born kinematics from a deeper action, the global
connected source-record action, durability dynamics, a source pole, or
alpha.

## Status

```text
record_axioms_QR1_through_QR7_disclosed = true
arbitrary_positive_Hermitian_competitor_admitted = true
pointer_projection_orthogonality_forces_offdiagonal_zero = true
probability_preserving_singleton_inclusions_force_unit_diagonal = true
without_QR3_common_scale_freedom_reproduced = true
public_record_counting_metric_derived_from_disclosed_quantum_record_axioms = true
disjoint_union_direct_sum_coherence_derived = true
independent_register_tensor_coherence_derived_given_QR6_QR7 = true
strong_symmetric_monoidal_record_functor_derived_given_QR6_QR7 = true
source_record_product_metric_given_compatible_transport = true
Born_kinematics_derived_from_deeper_action = false
global_connected_source_record_action_derived = false
alpha_computed = false
proof_authorized = false
```
