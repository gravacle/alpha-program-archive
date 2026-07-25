# Coupled Record-Bundle Modulus Gate v001

## Candidate mechanism

The active relative phase defines a principal `U(1)_rel` bundle over the
public `3+1` record surface. A natural coupled gravity-EM candidate is an
invariant total-space metric

```text
ds_P^2
  = g_mu_nu dx^mu dx^nu
    + r_Q^2 (d theta + A_mu dx^mu)^2,

theta equivalent to theta + 2 pi.
```

This realizes gravity and charged phase transport as different components of
one record-bundle geometry. It uses no alpha target.

## Reduction

For constant `r_Q`, the two-derivative Einstein-Hilbert action on the total
space reduces schematically to

```text
S_P
  = [1/(16 pi G_4)] integral_M sqrt(-g)
      [R_4 - (r_Q^2/4) F_mu_nu F^mu_nu].
```

In the primitive unit-character convention,

```text
1/e_tree^2 = r_Q^2/(16 pi G_4),
alpha_tree = e_tree^2/(4 pi) = 4 G_4/r_Q^2.
```

The formula shows that a genuine total-space derivation could transfer the
known gravitational normalization into the electromagnetic sector.

## Surviving modulus

The action-phase period fixes the coordinate identification
`theta ~ theta+2 pi`. It does not fix the physical fiber radius `r_Q`.

For every positive `lambda`,

```text
r_Q -> lambda r_Q
```

preserves:

```text
the compact group;
the unit character and charge lattice;
the principal-bundle topology;
gauge covariance;
the action-phase period;
Lorentz covariance on the base;
and the existence of a unique base causal-record interval.
```

It changes `alpha_tree` by `lambda^(-2)`.

The canonical Hilbert/Fubini-Study metric of the two-state comparator fixes
relative lengths inside the comparator geometry. It does not, without an
additional cross-sector metric rule, fix that internal length relative to
the public spacetime metric and `G_4`.

## Higher-action ambiguity

Even after `r_Q` is fixed, higher-dimensional curvature invariants or an
independent horizontal curvature term can modify the reduced `F^2`
coefficient unless the complete microscopic action excludes them. Thus a
two-derivative total-space branch and its mutation rule must be derived, not
selected after comparison.

## Exact reopen conditions

The coupled record-bundle route can close Step 5 only if Gravacle derives,
before evaluating a coupling:

1. why the physical parent is the total-space geometric action;
2. why its primitive action is uniquely the declared two-derivative action;
3. the dimensionless ratio `r_Q/sqrt(G_4)`, or an isolated saddle that fixes
   it; and
4. the complete quantum/threshold correction to the Thomson limit.

Possible physical mechanisms are:

```text
a derived isometry between the proper-time return and charge-phase return;
a record-capacity saddle that stabilizes r_Q;
or a complete spectral parent whose normalized operator fixes both metrics.
```

Choosing the relation because it reproduces alpha is forbidden.

## Status

```text
shared_record_bundle_geometry_constructed = true
tree_level_alpha_relation_derived = true
charge_fiber_radius_derived = false
two_derivative_parent_action_uniquely_derived = false
quantum_threshold_map_derived = false
coupled_bundle_computes_alpha = false
alpha_computed = false
proof_authorized = false
```
