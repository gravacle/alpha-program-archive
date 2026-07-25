# Reduced Source-Record Generator Structure Gate v002

Date: 2026-07-23

## Why v002 exists

Version 001 listed four operators and reported dimensions without computing
the full linear kernels. It also described the reduced product carrier too
broadly and called positive exchange magnitude compulsory.

Version 002 computes both kernel dimensions over the full 16-element
Hermitian Pauli-product basis and narrows every physical claim. Version 001 is
rejected as authority.

## Reduced-factor ansatz

For this structure calculation only, declare

```text
H_reduced = C^2_source-grading tensor C^2_record-endpoint.
```

All suppressed spin and multiplicity factors are assumed to carry the
identity. This reduced factorization is not derived from the complete closure
carrier. Consequently the computed dimensions are not dimensions of the full
`G_closure` operator space.

Let

```text
Z_S = source left/right grading,
Z_R = record endpoint grading.
```

## Exact odd/odd kernel

On the real vector space of all 16 Hermitian Pauli products, impose

```text
{G,Z_S tensor I}=0,
{G,I tensor Z_R}=0.
```

The combined real linear map has rank `12`, hence nullity `4`. Its kernel is

```text
span_R {
  X_S tensor X_R,
  X_S tensor Y_R,
  Y_S tensor X_R,
  Y_S tensor Y_R
}.
```

This is complete on the declared reduced factor only.

## Conditional combined-grading reduction

Restrict the commutator map

```text
G -> [G,Z_S tensor I + I tensor Z_R]
```

to that four-dimensional kernel. Its exact rank is `2`, hence its nullity is
`2`, with kernel

```text
E_1 = X_S tensor X_R + Y_S tensor Y_R,
E_2 = X_S tensor Y_R - Y_S tensor X_R.
```

Thus a generator satisfying the additional commutator condition has

```text
G = a E_1 + b E_2
  = lambda |01><10| + lambda^* |10><01|,

lambda = 2(a+i b).
```

The condition expresses conserved combined grading in this reduced ansatz.
It is not yet derived from closed boundary accounting.

## Passive record-basis phase

A consistent passive record rephasing

```text
U_R(theta)=exp(-i theta Z_R/2)
```

rotates `E_1` and `E_2`. For this isolated exchange coefficient it can make a
nonzero `lambda` real and nonnegative, provided every record object is
transformed consistently. Zero exchange remains allowed.

This rephasing does not set the sealed closure background component `b_R` to
zero and does not remove any axial Jacobian or topological term in the full
field theory.

## Conditional coherent transfer

In the phase convention

```text
G_ex = (g/2) E_1,
g >= 0,
```

the one-excitation sector evolves as

```text
|1_S,0_R>
  -> cos(g tau/hbar)|1_S,0_R>
     - i sin(g tau/hbar)|0_S,1_R>.
```

Exact coherent state transfer occurs for

```text
g tau/hbar = (2n+1) pi/2,
n = 0,1,2,...
```

The first positive transfer is at `pi/2`. This is an iSWAP-like reversible
state transfer, not by itself a measurement or durable record.

## Relation to the source mass block

`G_ex` is a joint reduced source-record operator, not the supplied c-number
background of the free chiral-block gate. A source-only mass parameter still
requires a dynamically derived record background, an exact reduction of the
joint propagator, or a derived self-energy after integrating out the record
sector.

## What is established

```text
on the declared reduced factor:
  odd/odd Hermitian kernel dimension = 4;
  conditional conserved-exchange kernel dimension = 2.

not established:
  reduced factorization of the complete closure carrier;
  combined-grading conservation as physical law;
  nonzero exchange;
  exchange magnitude or physical interval;
  durability;
  source mass or alpha.
```

## Exact next gate

Determine whether closed source-record boundary accounting independently
requires the combined-grading conservation law, including all spin,
environment, edge, and multiplicity factors. Only then may the exchange
operator be promoted into the complete closure-generator construction.

## Status

```text
reduced_source_record_product_factor_declared = true
minimal_product_carrier_derived = false
complete_closure_operator_space_dimension_derived = false
reduced_odd_odd_linear_map_rank = 12
reduced_odd_odd_kernel_dimension = 4
combined_grading_conservation_derived = false
conditional_restricted_commutator_rank = 2
conditional_exchange_kernel_dimension = 2
nonzero_exchange_derived = false
exchange_magnitude_derived = false
physical_record_interval_derived = false
durable_record_dynamics_derived = false
source_mass_derived = false
spectral_evaluation_authorized = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
