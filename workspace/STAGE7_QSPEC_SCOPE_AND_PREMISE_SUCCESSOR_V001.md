# Stage-7 Q_spec Scope and Premise Successor v001

Date: 2026-07-24

## Purpose

This append-only authority implements review conditions C1, C3, C4, and C6.
It narrows or discloses statuses in the Stage-6/7 v001 artifacts without
altering those sealed files.

## Source-inclusive continuum completion

The completed-record quasi-local state does not supply a source-inclusive
continuum completion. The following remain separate open obligations:

```text
projective limit of source-inclusive states;
infinite-future source Moller limit;
and continuum-regulator independence of that source-inclusive limit.
```

No completed-record theorem may silently discharge these obligations.

## Envelope-realization fork

The classified intrinsic probability measure fixes normalized four-volume
on a flat primitive diamond and therefore fixes its normalized time marginal:

```text
w(s)=32 min(s,1-s)^3,  0<=s<=1.
```

It does not by itself select how that marginal enters the parent operator.
At least two readings are pinned-consistent:

```text
ER-A: use the time marginal as the temporal interaction amplitude;
ER-B: use uniform spacetime density at action level and derive the
      slice-level operator after spatial assembly.
```

The current ordinary parent adopts `ER-A` as a disclosed branch premise. It
is not relabeled as derived. Under `ER-A`:

```text
v_c(t)=(tau_R/T_R) w((t-t_c)/T_R)
```

inside the cell.

The old single "pushforward" check is replaced by two clauses:

```text
shape clause:
  w is the normalized time marginal of the intrinsic four-volume measure;

amplitude clause:
  integral_cell_time v_c(t) dt = tau_R.
```

The shape clause follows from the measure classification. The amplitude
realization follows from disclosed `ER-A` together with the independently
derived dimensionless opening interval `tau_R`. `ER-B` remains an unexcluded
alternate parent branch.

## Admitted finite-energy excitation class

For the ordinary flat massless source tail, define:

```text
E_fin = {
  psi in L2(R^3,C^4):
  ||psi||=1,
  psi is in the quadratic-form domain of |h_0|,
  and the spectral measure of psi for h_0 has an L1 density
}.
```

Boundary data may be finite mixtures of such normalized vector states.
No uniform decay time over the entire class is claimed.

The thresholded nonreturn quantifiers are fixed per state:

```text
for every psi in E_fin,
for every delta>0,
there exists T=T(psi,delta)<infinity
such that for every t>=T,
|<psi,exp(-i h_0 t)psi>|^2 < delta.
```

The order

```text
for every delta, there exists T, for every psi
```

is forbidden. Time-translated or increasingly narrow spectral packets rule
out that uniform reading.

## Admissible cell-complex and packing class

The currently proven durability branch uses locally finite,
future-directed, causally sequential exhaustions by finite primitive
diamonds. A stage addition is admissible only when every new cell opens
after all closure faces of the earlier stage.

The class requires:

```text
finite support for every local completed-record observable;
intrinsic per-cell measure assembly;
no reuse of a completed primitive incidence;
cofinal coverage of the declared outgoing region;
and bounded finite-stage operators.
```

Spacetime-overlapping concurrent cells are not in the proven compatibility
class. A future extension requires a derived spacelike
causal-factorization/light-cone lemma.

No Stage-10 or later normalization may depend on:

```text
cell count;
packing density;
triangulation valence;
arbitrary refinement rate;
or regulator-specific overlap multiplicity.
```

unless the dependence is first shown to survive a packing-independent
continuum limit derived from the parent action.

## Premise classes

The six adopted premise classes are:

```text
Fundamental Boundary Record Action;
Parent-State Covariance;
Causal Incidence Support;
Boundary Superconnection / Single-Operator Completeness;
Global Boundary Descent / Quasi-Free Completeness;
and zero independent bare F^2 compositeness.
```

They are target-value-free but historically target-aware.

The standard-theory or kinematic inputs are separately disclosed:

```text
the Dirac spinor and CAR framework;
standard CPT structure in the declared relativistic branch;
spin-statistics and ordinary functional-analysis conventions;
and the record axioms defining ready, pointer, completed, and recoverable
record sectors.
```

The stationary quasifree in-state of `h_0` is a disclosed ordinary-branch
state. The free CTP contour is derived from that disclosed state.

## Representation scope

`H_K(t)=dGamma_R(h_K(t))` and the finite `W_N` are
finite-regularization/algebraic Bogoliubov-automorphism objects. No unitary
implementability of the intermediate-time dynamics in the asymptotic
quasifree representation is claimed. The one-particle off-diagonal part
fails the Hilbert-Schmidt condition in that representation. Only the
completed maps identified in the scoped outgoing construction are claimed
to be implementable.

## Fixed statuses

```text
envelope_realization_ER_A = DISCLOSED_BRANCH_PREMISE
finite_energy_class_defined = true
threshold_quantifiers_per_state = true
causal_sequential_cell_class_fixed = true
packing_dependent_normalization_forbidden = true
free_in_state = DISCLOSED_BRANCH_STATE
free_CTP_contour = DERIVED_FROM_DISCLOSED_STATE

complete_parameter_free_Q_spec_frozen = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
