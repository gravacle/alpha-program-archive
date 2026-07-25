# BID Absolute Record-Scale Identifiability Gate v001

Date: 2026-07-23

## Question

Do the completed first-opening kinematics fix the physical SI duration `T_R`,
or only the dimensionless action interval?

## Exact scale orbit

The first-opening calculation fixes

```text
tau_R=pi/sqrt(2)
```

and represents the physical generator as

```text
H_R(T_R)=(hbar tau_R/T_R) B.
```

For every positive scale factor `lambda`, define

```text
T_R' =lambda T_R,
H_R' =H_R/lambda.
```

Then

```text
exp(-i H_R' T_R'/hbar)
  =exp(-i H_R T_R/hbar)
  =exp(-i tau_R B).
```

All first-opening probabilities, orthogonality, endpoint transfer, incidence
normalization, and projective path lengths are identical on this scale orbit.

The causal-diamond geometry changes dimensionfully:

```text
radius -> lambda radius,
three-volume -> lambda^3 three-volume,
four-volume -> lambda^4 four-volume,
```

but its dimensionless shape coefficients do not.

## Consequence

The current record kinematics do not identify one SI value of `T_R`. The
allow/require rule fixes the first completed action interval, not an absolute
clock duration, unless an additional dimensionful part of the same
parameter-free dynamics breaks this scale orbit.

The existence of the Planck time does not by itself select `T_R=t_P`. Such an
identification must follow from the coupled gravity-source-record saddle or
another target-independent stationary condition.

No electromagnetic coupling, particle mass, cosmological endpoint, or
observed radius may be used to select a member of the orbit.

## Exact closure condition

Absolute scale closes only if the complete parameter-free parent supplies a
Lorentz-scalar equation

```text
F(T_R/t_P, dimensionless branch data)=0
```

with one isolated positive stable solution, before alpha or any endpoint is
evaluated.

If the equation is scale-free, has a continuum of roots, or is selected by a
measured target, the SI interval remains open.

## Status

```text
dimensionless_tau_R_derived = true
causal_diamond_shape_derived = true
positive_scale_orbit_exists = true
first_opening_data_break_scale_orbit = false
absolute_SI_record_duration_derived = false
Planck_time_identified_with_record_duration = false
coupled_gravity_record_stationarity_equation_derived = false
alpha_computed = false
proof_authorized = false
```
