# Coupled Record-Bundle Modulus Gate v002

## Authority correction

This file supersedes v001. The canonical Hopf fiber of a normalized qubit is
its common phase. The active endpoint-preserving relative-phase `U(1)_rel`
used by the charged branch is not automatically that canonical principal
fiber: its action on the Bloch sphere has fixed record poles. A free
relative-phase lift and its physical metric therefore require additional
structure.

Accordingly, a coupled record-bundle metric is constructible as a candidate;
it has not been derived from projective kinematics.

## Strongest granted candidate

Grant a principal circle with primitive period

```text
theta equivalent to theta + 2 pi
```

and the strict metric-only five-dimensional ansatz

```text
ds_5^2
  = g_mu_nu dx^mu dx^nu
    + R^2 (d theta + A_mu dx^mu)^2.
```

Grant also that the complete primitive action is the two-derivative
five-dimensional Einstein-Hilbert action and that no independent connection
term is present.

For constant `R`, dimensional reduction gives

```text
S_4/hbar
  = [1/(16 pi ell_P^2)] integral sqrt(-g)
      [R_4 - (R^2/4) F_mu_nu F^mu_nu],

K_KK = R^2/(16 pi ell_P^2),
alpha_tree = 4 ell_P^2/R^2.
```

This is a genuine conditional transfer of gravitational normalization to the
electromagnetic kinetic term. It does not use alpha.

## Exact obstruction

The action-phase period fixes the coordinate period and integer character
lattice. It does not fix the proper radius `R`.

Even if one unique base record interval `Delta tau` is granted, every

```text
R = beta c Delta tau,  beta > 0
```

preserves the base interval, phase periodicity, topology, gauge covariance,
and unit character while changing `K_KK` by `beta^2`.

The Fubini-Study metric fixes dimensionless distances in projective state
space. It does not fix their dimensional conversion relative to the
spacetime metric or `ell_P`.

The radius is also a dynamical radion. Pure circle Einstein-Hilbert reduction
does not generate a potential that selects one constant value. Freezing it
without stabilization is not a complete reduction when electromagnetic
stress sources that mode.

## Mutation obstruction

The metric-only two-derivative parent forbids a separate tree-level `F^2`
term only under full higher-dimensional diffeomorphism invariance. The
ambiguity returns if:

- the connection is distinguished independently of the metric;
- higher-curvature or localized boundary terms are allowed;
- the record section carries its own curvature action; or
- quantum matching introduces an undetermined finite local term.

Thus the complete parent action class, radion stabilization, spectrum, and
matching rule must be derived together.

## Exact reopen conditions

The coupled route computes alpha only after a target-independent derivation
supplies:

1. the physical free `U(1)_rel` lift and its total-space metric;
2. a unique action class excluding independent connection and localized
   `F^2` terms;
3. a parameter-free saddle selecting
   `rho = R_*/ell_P`, including breathing and squashing modes;
4. the full Kaluza-Klein/record spectrum and unitary Lorentzian measure; and
5. threshold matching to the Thomson limit.

Declaring `R` equal to a record interval by dimensional analogy does not pass.
A derived metric-gluing or stabilization law is required.

## Status

```text
canonical_Hopf_fiber_identified_with_active_relative_U1 = false
coupled_record_bundle_candidate_constructible = true
coupled_record_bundle_physically_derived = false
conditional_tree_level_K_relation_derived = true
charge_fiber_radius_derived = false
radion_stabilization_derived = false
parent_action_class_unique = false
quantum_threshold_map_derived = false
coupled_bundle_computes_alpha = false
alpha_computed = false
proof_authorized = false
```
