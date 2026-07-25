# BID Distinguishable Record-Cell Composition Derivation v001

Date: 2026-07-23

## Scope

This derivation fixes the statistics and disjoint carrier of primitive pure
charged record cells. It does not select connected interactions or compute a
response.

## Local alternatives

After charged-source activation, one primitive causal record cell has the
handle-conditioned carrier

```text
H_c=span_C{|r_c>,|p_Q,c>,|e_Q,c>}.
```

These are mutually exclusive local alternatives: unresolved, completed
charged record, and the incidence intermediate. The causal cell label `c` is
physical spacetime-incidence data.

## Joint alternatives and Hilbert composition

For distinct labeled cells `c` and `d`, the joint alternatives are the
Cartesian product

```text
Omega_(c,d)=Omega_c x Omega_d.
```

The elementary-record Hilbertization gives

```text
l2(Omega_c x Omega_d)
  ~=l2(Omega_c) tensor l2(Omega_d)
```

by the canonical basis map

```text
|x,y> -> |x> tensor |y>.
```

The map is unitary and natural under cell relabeling. Iteration gives the
strong symmetric-monoidal Hilbert carrier for a finite family of disjoint
record cells.

This uses the standard quantum composition law for distinguishable local
systems as a disclosed kinematic input. It is not presented as a new
Gravacle prediction.

## Why Bose/Fermi statistics do not apply to the record cells

The labels `c,d` are physical causal-cell locations. The public configurations

```text
(p_Q at c, r at d)
and
(r at c, p_Q at d)
```

are different records. Symmetric or antisymmetric projection would identify
or discard part of this labeled configuration space. Therefore the record
cells themselves are distinguishable tensor factors.

This conclusion concerns record carriers. The charged source field retains
its separately derived fermionic statistics inside `Q_spec`.

## Disjoint generator and boundary

For independent cells with continuous evolutions, differentiation of the
factorized unitary gives

```text
B_(c disjoint d)=B_c tensor I+I tensor B_d.
```

The root and final record states are

```text
|R>=tensor_c |r_c>,
|P>=tensor_c |p_Q,c>.
```

The normalized transition amplitude factorizes exactly.

For adjacent or interacting cells, this derivation does not set all
cross-cell terms to zero. Shared `g,a,psi`, environmental degrees, and any
record coupling allowed by the complete parameter-free action must be derived
in `Q_spec`. The one-cell operator and disjoint composition do not determine
those terms.

## Status

```text
pure_charged_local_record_carrier_derived = true
record_cells_spacetime_labeled = true
joint_record_alternatives_are_cartesian_products = true
standard_distinguishable_quantum_composition_disclosed = true
strong_monoidal_Hilb_carrier_for_disjoint_cells_derived = true
record_cell_Bose_statistics_rejected = true
record_cell_Fermi_statistics_rejected = true
charged_source_field_fermionic_statistics_unchanged = true
disjoint_generator_sum_derived = true
disjoint_root_and_endpoint_products_derived = true
connected_cross_cell_terms_derived = false
connected_preparation_beyond_primitive_product_derived = false
connected_linked_cluster_density_proved = false
alpha_computed = false
proof_authorized = false
```
