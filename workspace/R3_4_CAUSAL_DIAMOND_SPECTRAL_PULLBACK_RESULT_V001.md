# R3.4 Causal-Diamond Spectral Pullback Result

## Verdict

```text
CONDITIONAL_DIAMOND_PULLBACK_OPERATOR_OR_ROOT_OPEN
```

The causal-diamond calculation succeeds exactly. Its physical provenance gate
does not yet pass, so the result is retained as a target-independent
conditional density rather than promoted to the unique Gravacle spectral law.

No measured coupling, mass, endpoint, cosmological value, or alpha entered.

## Exact conditional result

For the unit-tip-separation `3+1` causal diamond,

```text
D = {x: -1/2 <= t <= 1/2, |x_spatial| <= 1/2-|t|},
Vol(D) = pi/24,
d mu_D = d^4x/Vol(D).
```

The normalized null-shell Fourier transform of the constant root is

```text
F_D(E)
 = 24/E^3 [sin(E/2)-(E/2)cos(E/2)].
```

This is the full four-dimensional diamond integral, not the transform of a
fixed spatial ball. A separate Gauss-Legendre calculation integrated the
shrinking spatial three-ball at each time. Across the sealed energy points,
its maximum disagreement with the closed form was `7.76e-12`.

Using the positive-energy `3+1` massless phase-space weight gives

```text
N_D
 = integral_0^infinity E^2 |F_D(E)|^2 dE
 = 12 pi,

rho_D(E)
 = [48/pi]
   [sin(E/2)-(E/2)cos(E/2)]^2/E^4.
```

The normalization follows from

```text
integral_0^infinity j_1(z)^2 dz = pi/6.
```

An independent interval quadrature through `z=5000`, followed by the leading
analytic tail, returned `0.999999994157` for the normalized integral.

## Decay and durability

The density is nonnegative, normalized, absolutely continuous, and in `L1`.
Near threshold,

```text
rho_D(E)=E^2/(12 pi)+O(E^4).
```

Its first three derivatives have the regularity needed for three integrations
by parts. Therefore

```text
A_D(t)
 = integral_0^infinity rho_D(E) exp(-iEt) dE
 = i/(6 pi t^3)+o(t^-3),

|A_D(t)|^2 = O(t^-6).
```

In particular, the Riemann-Lebesgue theorem supplies the required thresholded
statement: for every `delta>0`, some finite `T_delta` makes the local return
probability smaller than `delta` for all later times.

The amplitude result reproduces the `t^-6` **probability** class of the
sealed covariant representative. It does not reproduce the three discrete
regulators, whose interval-averaged return probabilities scale as `t^-3`
and whose amplitudes therefore have envelope class `t^-3/2`. That mismatch
remains an unresolved scheme-equivalence test; it may not be erased by
calling all four rows one decay class.

## Why this is not yet the physical spectral theorem

The current corpus has derived the uniform flat-cell measure and the
quasi-local outgoing-record algebra. It has not yet derived all of the
following:

1. that the physical outgoing-record generator is the positive-energy
   `3+1` massless incidence/Hodge-Dirac continuation;
2. its self-adjoint outgoing-sector domain;
3. uniqueness of the constant root preparation against all admitted
   preparation sectors; and
4. why this continuum sector, rather than a gapped source mode or a distinct
   boundary/environment sector, carries durability.

This distinction is load-bearing. The finite BID generator is defined on the
oriented two-skeleton of a four-dimensional cell complex and evolves in its
record parameter. Replacing it with a positive-energy `3+1` shell requires a
derived Hamiltonian/continuation map; it cannot be inferred merely because the
resulting density is clean.

## Status

```text
uniform_flat_cell_measure_derived = true
outgoing_record_algebra_subobligation_closed = true
conditional_density_computed = true
conditional_density_absolutely_continuous = true
conditional_thresholded_durability = true
massless_positive_energy_outgoing_operator_derived = false
self_adjoint_outgoing_domain_derived = false
constant_root_uniqueness_derived = false
physical_durability_carrier_identified = false
unique_covariant_spectral_measure_derived = false
hypothesis_promoted_to_principle = false
spectral_evaluation_authorized = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
