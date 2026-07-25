# BCC Weyl-Walk Parent Candidate Gate v001

Date: 2026-07-23

## Purpose

This gate asks whether a finite homogeneous, local, isotropic, unitary
two-component walk can supply the missing record/source parent propagator.
No gauge response or coupling is evaluated.

Primary classification sources:

```text
https://arxiv.org/abs/1708.00826
https://arxiv.org/abs/1703.05890
https://arxiv.org/abs/1707.08455
```

## Candidate selected by the declared constraints

Within walks on `Z^3` with:

```text
homogeneity;
finite-neighbor locality;
unitarity;
spatial isotropy;
and minimal internal dimension two,
```

the cited classification selects the body-centered-cubic Cayley graph and two
inequivalent Weyl-walk orientations.

One representative factorizes as

```text
A(k)
  = exp(-i k_x sigma_x)
    exp(-i k_y sigma_y)
    exp(-i k_z sigma_z).
```

Its small-wave-vector branch recovers a Weyl propagator. This is a credible
target-free parent-propagator candidate, not yet a Gravacle causal-cell
theorem.

## Species result

Across the full Brillouin zone, the same walk has Weyl neighborhoods at

```text
k_0 = (0,0,0),
k_1 = (pi/2,pi/2,pi/2),
k_2 = (-pi/2,-pi/2,-pi/2),
k_3 = (pi,0,0),
```

with two cones of each chirality. Thus one minimal two-component walk is not
one isolated Weyl species. Its net chirality cancels.

This is a target-free prediction of the candidate regulator and a species
gate:

```text
minimal_BCC_two_component_walk_Weyl_cones = 4
positive_chirality_cones = 2
negative_chirality_cones = 2
```

The previously frozen one-Dirac source inventory cannot be combined with this
regulator unchanged. No determinant may be evaluated until the all-zone
species are incorporated or a separately derived doubler-removal mechanism
is sealed.

## Why the parent kernel is not yet frozen

The classification does not yet derive:

```text
the BCC graph from the Gravacle causal-cell postulate;
the spatial-step to time-step ratio;
one physical choice between the two walk orientations;
the finite spacetime domain and record boundaries;
the Fock vacuum and doubled CTP state;
or the gauge-covariant interacting update.
```

Minimal insertion of link phases is not enough. The free walk's cancellations
need not preserve exact unitarity in an arbitrary link background. A
factorized gauging preserves stepwise unitarity, but the ordering of the three
conditional shifts and admissible gauge-covariant local dressings must then be
derived. Those choices alter finite curvature response.

## Status

```text
free_BCC_walk_classification_imported = true
free_BCC_walk_unitarity_reproduced = true
four_Weyl_cones_reproduced = true
one_Dirac_source_inventory_survives = false
BCC_graph_derived_from_Gravacle_cell = false
unique_gauge_covariant_walk_derived = false
complete_Fock_CTP_parent_kernel_frozen = false
finite_response_authorized = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```

## Next hard gate

Before adopting this route, Gravacle must derive one gauge-covariant causal
update and either:

```text
accept the complete forced all-zone species content before evaluation;
or derive a local gauge-covariant doubler-removal rule without target input.
```

If neither follows from the boundary principles, the BCC walk is a useful
analogy and regulator candidate, not the unique `Q_spec`.

