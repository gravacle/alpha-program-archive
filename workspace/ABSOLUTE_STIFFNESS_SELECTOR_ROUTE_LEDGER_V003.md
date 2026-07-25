# Absolute Stiffness Selector Route Ledger v003

## Purpose

This ledger records the target-independent route comparison completed after
the one-cell CTP and BCC Weyl-walk gates. It prevents a blocked mechanism from
returning under different notation.

No measured value of alpha, no endpoint radius, and no earlier alpha
coefficient is used to select a route.

## Common obstruction

For every ordinary local `3+1` compact-`U(1)` continuum construction reviewed,
the parity-even action admits

```text
S_M[A]       = (hbar K/4) integral F wedge *F,
Delta S_c[A] = (hbar c_R/4) integral F wedge *F,
K            -> K + c_R.
```

Gauge invariance, Lorentz covariance, compactness, charge quantization, Ward
identities, anomalies, and the charge-character lattice do not forbid the
finite second term. They can fix charge ratios, topological data, beta-function
slopes, or relative kinetic coefficients, but not the absolute Thomson
stiffness.

Therefore alpha is not computed unless one complete microscopic
specification both:

1. calculates the absolute parity-even response; and
2. makes an additional independent `c_R F^2` mutation inadmissible.

## Independently audited routes

### Continuum determinant and finite internal geometry

A finite internal carrier fixes factors such as `Tr(Q^2)` but leaves the
continuous spacetime spectrum. The exact determinant has the standard local
`F^2` divergence and requires a subtraction condition. Cutoff and zeta
spectral actions retain an action normalization, cutoff profile, matching
condition, or equivalent finite prescription.

Status: `BLOCK_ABSOLUTE`.

### Induced gauge theory and compositeness

`K_bare=0` is a valid declared branch condition, but the induced response
still depends on the complete spectrum, masses, compositeness scale, boundary
prescription, and finite matching rule.

Status: `BLOCK_CURRENT_SPECIFICATION`.

### BCC Weyl walk and causal/QCA routes

The minimal isotropic BCC walk is a real target-free parent-propagator
candidate, but its full Brillouin zone contains four Weyl cones. Existing
gauge-covariant QCA constructions retain a continuous gauge coupling and
additional branch choices. Removing or lifting doublers changes the response
and is forbidden after evaluation.

Status: `BLOCK_CURRENT_SPECIFICATION`.

### Quantum links and finite gauge Hilbert spaces

Finite link representations quantize flux. Gauge-preserving deformations can
still vary the emergent parity-even stiffness continuously.

Status: `BLOCK_ABSOLUTE`.

### Exact RG and self-dual routes

No accepted pure-`U(1)` interacting fixed point fixes the observed weak
coupling. Matter fixed-point and self-dual constructions require additional
parent dynamics and generally select order-one couplings or retain relevant
directions.

Status: `BLOCK_CURRENT_BRANCH`.

### Boundary CFT / holographic current normalization

An exact boundary CFT can fix a bulk kinetic coefficient through its current
central charge. That would be a complete parent theory, not a consequence of
the currently sealed flat `3+1` record axioms. No such target-independent
Gravacle boundary CFT has been derived.

Status: `CONDITIONAL_PARENT_ROUTE_NOT_DERIVED`.

## Only surviving strict route

The smallest route not excluded in principle is a complete finite
spacetime-plus-internal record cell:

```text
Q_cell = {
  finite carrier,
  gauge-covariant operator,
  state and CTP contour,
  boundary and edge data,
  measure,
  exact record map,
  exact normalized partition functional
}.
```

Every entry must be derived and sealed before response evaluation. The full
finite spectrum, including all doublers and zero modes, must be retained.

The first authorized response test, once `Q_cell` exists, is the exact
electric/magnetic flux-curvature protocol in
`FINITE_RECORD_CELL_FLUX_RESPONSE_PROTOCOL_V001.md`.

## Failure rule

The route fails if:

- the finite cell, carrier, operator, mass, multiplicity, or boundary is
  selected after seeing alpha;
- a coupling is already present in the gauged microscopic update;
- a finite `c_R F^2` term can be added without violating the complete
  microscopic specification;
- the full finite spectrum is replaced by a preferred low-energy cone;
- a finite-cell answer is called physical without a derived stitching or
  continuum rule; or
- the Thomson limit is asserted without a derived massive charged sector.

## Current state

```text
ordinary_continuum_absolute_selector_exists = false
finite_internal_geometry_fixes_absolute_stiffness = false
bcc_parent_propagator_candidate_exists = true
bcc_complete_gauged_Q_cell_derived = false
complete_finite_record_cell_Q_spec_derived = false
finite_flux_response_protocol_frozen = true
finite_flux_response_evaluated = false
finite_c_F2_deformation_excluded = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
