# R3.4 Causal-Diamond Spectral Pullback

## Status

Forward calculation plus provenance adjudication.

R3.3 derived the normalized flat-cell volume measure. This gate asks what
root spectral measure follows when that cell is continued by the massless
positive-energy continuum symbol of the unit incidence/Hodge-Dirac operator.
It also checks whether that operator and root embedding are already derived
for the outgoing-record sector.

No measured coupling, mass, endpoint, cosmological value, or alpha may enter.

## Fixed geometric input

For unit tip separation, let

```text
D={x: -1/2 <= t <= 1/2, |x_spatial| <= 1/2-|t|},
Vol(D)=pi/24,
d mu_D=d^4x/Vol(D).
```

The constant normalized cell root is

```text
r_D(x)=1/sqrt(Vol(D)).
```

This is the continuum analogue of the path-independent, covariantly constant
root representative declared in BID V011. The audit must separately report
whether its preparation uniqueness is proved.

## Conditional continuum operator

Under the massless positive-energy incidence/Hodge-Dirac continuation,

```text
E=|k|,
d phase space proportional to E^2 dE.
```

This gate computes the resulting measure. It may not mark that operator as
derived unless the current corpus derives it as the physical outgoing-record
generator, including domain and root embedding.

## Required derivation

On the positive-energy shell `k^0=|k|=E`, derive the normalized diamond form
factor

```text
F_D(E)
 = [1/Vol(D)] integral_D exp[i(E t-k dot x)] d^4x
 = 24/E^3 [sin(E/2)-(E/2)cos(E/2)].
```

Then define and normalize

```text
rho_D(E)=E^2 |F_D(E)|^2/N_D, E>=0.
```

The calculation must derive `N_D`, verify positivity and normalization,
classify absolute continuity, and apply the Riemann-Lebesgue theorem to the
return amplitude

```text
A_D(t)=integral_0^infinity rho_D(E) exp(-iEt) dE.
```

## Provenance gate

The final verdict is:

```text
DERIVED_COVARIANT_ROOT_SPECTRAL_MEASURE
```

only if all of the following are already derived:

1. the massless positive-energy continuum incidence/Hodge-Dirac operator;
2. its self-adjoint outgoing-sector domain;
3. the constant root embedding and its uniqueness; and
4. the identification of that sector, rather than a gapped source or another
   boundary/environment sector, as the carrier of record durability.

If the calculation succeeds but any item remains open, return:

```text
CONDITIONAL_DIAMOND_PULLBACK_OPERATOR_OR_ROOT_OPEN.
```

## Non-promotion rule

A conditional density may be retained as a target-independent candidate but
does not promote the direct-limit hypothesis.

```text
alpha_used = false
alpha_computed = false
hypothesis_promoted_to_principle = false
```
