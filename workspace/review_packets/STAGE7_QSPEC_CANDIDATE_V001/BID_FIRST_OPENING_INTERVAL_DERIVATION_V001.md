# BID First-Opening Interval Derivation v001

Date: 2026-07-23

## Purpose

This derives the dimensionless action interval and causal-cell shape used by
the V011 response. It contains no coupling target and computes no alpha.

## Canonical handle-conditioned operator

For each first-opening edge `h:r->p_h`, the closed-cell inclusion gives the
three-dimensional carrier

```text
H_h=span{|r>,|p_h>,|e_h>}.
```

Gate 4's unit incidence column is

```text
D_h|e_h>=|p_h>-|r>.
```

In the ordered basis `(|r>,|p_h>,|e_h>)`, the self-adjoint incidence operator
is

```text
B_h =
[[ 0, 0,-1],
 [ 0, 0, 1],
 [-1, 1, 0]].
```

Its characteristic polynomial and minimal polynomial are

```text
det(lambda I-B_h)=lambda(lambda^2-2),
B_h^3=2 B_h.
```

Hence

```text
spec(B_h)={-sqrt(2),0,+sqrt(2)}
```

and

```text
exp(-i tau B_h)
 =I-i sin(sqrt(2)tau) B_h/sqrt(2)
   +[cos(sqrt(2)tau)-1]B_h^2/2.
```

Applied to the unresolved root,

```text
U_h(tau)|r>
 =[(1+cos(sqrt(2)tau))/2]|r>
  +[(1-cos(sqrt(2)tau))/2]|p_h>
  +i[sin(sqrt(2)tau)/sqrt(2)]|e_h>.
```

## Least common record interval

For distinct handles `h!=k`, the endpoint and edge supports are disjoint.
Their conditional-state overlap is therefore

```text
<r|U_h(tau)^dagger U_k(tau)|r>
 =[(1+cos(sqrt(2)tau))/2]^2.
```

The least positive common zero is

```text
tau_R=pi/sqrt(2).
```

At this interval,

```text
U_h(tau_R)|r>=|p_h>
```

for every handle. Thus the unresolved root plus the three first-opening
outputs are one orthonormal four-alternative set. The result is unchanged by
edge orientation reversal or endpoint rephasing.

For a surviving incidence magnitude `w`, the result would be

```text
tau_R(w)=pi/(sqrt(2)|w|).
```

Therefore the interval is absolute only after Gate 4 derives `|w|=1`.
This makes the dependence visible rather than hiding it.

## Causal-cell realization

Adopt the previously declared causal-cell domain

```text
Omega(p,q)=J^+(p) intersect J^-(q),
```

where the endpoint proper-time separation is `T_R`. The action coordinate
along the cell is fixed by

```text
tau(t)=tau_R t/T_R,
H_h,physical=(hbar tau_R/T_R) B_h.
```

Consequently

```text
exp(-i H_h,physical T_R/hbar)=exp(-i tau_R B_h).
```

The absolute SI value of `T_R` is not inserted. The dimensionless action
interval is fixed, and `T_R` is the invariant scale of the physical causal
diamond. In the flat local `3+1`-dimensional branch,

```text
maximum spatial radius=T_R/2,
maximum spatial volume=pi T_R^3/6,
four-volume of Omega=pi T_R^4/24.
```

These coefficients follow from the Lorentzian causal diamond rather than a
hypercubic cell choice. The overall `T_R^4` cancels from a four-dimensional
quadratic gauge action only through the separately audited tetrad map; the
dimensionless geometric coefficients do not disappear.

## Durability boundary

The calculation establishes first mutually orthogonal public alternatives.
Physical durability additionally requires the complete record/environment
action to preserve or redundantly encode the endpoint label after closure.
That obligation belongs to `Q_spec`. V011 must not rename orthogonality as
durability before that map is derived.

## Status

```text
handle_conditioned_incidence_operator_derived = true
incidence_magnitude_one_required_from_Gate_4 = true
least_positive_common_orthogonality_interval_derived = true
dimensionless_tau_R_fixed = true
causal_diamond_shape_and_volume_coefficients_derived = true
absolute_SI_record_duration_computed = false
physical_durability_derived = false
primitive_record_stiffness_computed = false
alpha_computed = false
```
