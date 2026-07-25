# Causal Direct-Limit Architecture Test Specification v001

Date: 2026-07-24

Frozen before execution. No measured coupling, mass, endpoint, or cosmological
value is an input.

## Common observable

Every model uses a unit-normalized local generator in record units and begins
at a distinguished root state. The computed observable is

```text
P_root(t) = |<r|exp(-i t B)|r>|^2.
```

`P_root(t) -> 0` is evidence for loss of local recurrence in the infinite
model. It is not by itself evidence that a recoverable public record exists.

The decay exponent is estimated from interval-averaged probabilities on
logarithmically separated late-time windows. All five rows are emitted in
the declared order. The program has no winner, ranking, or target field.

## Frozen architectures

### A1: causal half-line

The limit is the endpoint-rooted unit-weight path. Its root spectral
representation is

```text
A_1(t) = integral_0^pi (2/pi) sin(k)^2 exp[-i 2t cos(k)] dk.
```

Finite path truncations are regulators.

### A2: three-branch causal tree

The root-radial sector of the unit-weight rooted three-branch tree is a
half-line with radial hopping `sqrt(3)`:

```text
A_2(t) = A_1(sqrt(3) t).
```

Finite-depth trees are regulators.

### A3: three-dimensional spatial lattice

The unit-weight cubic lattice return amplitude factorizes:

```text
A_3(t) =
  [integral_0^(2pi) exp[-i 2t cos(k)] dk/(2pi)]^3.
```

Finite periodic tori are regulators.

### A4: Lorentz-covariant causal-complex continuum representative

The representative uses the normalized positive-energy `3+1` phase-space
spectral density in record units,

```text
rho_4(E) = E^2 exp(-E)/2,
A_4(t) = integral_0^infinity rho_4(E) exp(-iEt) dE
       = (1 + i t)^(-3).
```

The exponential smearing is a declared unit-scale preparation regulator.
This row represents a covariant continuum class; covariance does not
automatically prove this spectral density unique.

### A5: effective continuum environment

The normalized one-sided continuum representative is

```text
rho_5(E) = exp(-E),
A_5(t) = (1 + i t)^(-1).
```

Its spectral density is an effective-model choice and must not be promoted
to a microscopic law.

## Blind covariance-selector criteria

The selector sees only:

```text
exact or reconstructed proper-orthochronous Lorentz covariance;
absence of a physical preferred foliation;
local causal composition;
compatibility with the disclosed 3+1 ordinary branch;
and preservation of the unit incidence law.
```

Allowed classifications:

```text
PHYSICAL_CLASS;
REGULATOR_OR_RADIAL_REDUCTION;
EFFECTIVE_DESCRIPTION;
INADMISSIBLE.
```

If more than one inequivalent `PHYSICAL_CLASS` survives, covariance does not
close Fork 8.

## Direct-limit theorem attempted

For an exhaustion of a locally finite, uniformly bounded-degree causal
complex:

```text
H_n = l2(V_n);
P_n -> I strongly;
B_n = P_n B_infinity P_n;
sup_n ||B_n|| < infinity.
```

The proof target is:

```text
B_n -> B_infinity strongly;
exp(-it B_n)P_n -> exp(-it B_infinity) strongly,
uniformly for t in compact intervals.
```

For the root spectral measure `mu_r`, an absolutely continuous `L1` density
implies `A_infinity(t) -> 0` by the Riemann-Lebesgue lemma. The thresholded
condition is then:

```text
for every delta > 0, exists T_delta:
sup_(t >= T_delta) P_root,infinity(t) < delta.
```

The proof must report separately whether covariance and the existing record
principles force the bounded-degree exhaustion, absolute continuity, and
recoverable outgoing record algebra. Conditional hypotheses may not be
reported as derived facts.

## Sealed outcome rules

```text
unique covariance survivor plus complete direct-limit proof:
  Fork 8 may advance to outgoing-record recoverability;

multiple covariant survivors or free spectral measures:
  Fork 8 remains open;

no direct limit or no thresholded durability:
  causal direct-limit hypothesis fails in the tested class.
```

Regardless of outcome:

```text
coupling_evaluated = false
alpha_computed = false
```
