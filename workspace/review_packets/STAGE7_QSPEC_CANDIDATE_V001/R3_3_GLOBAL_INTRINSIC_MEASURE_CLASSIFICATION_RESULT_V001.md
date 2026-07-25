# R3.3 Global Intrinsic Cell-Measure Classification Result

Date: 2026-07-24

## Verdict

```text
GLOBAL_INTRINSIC_FLAT_CELL_MEASURE_CLASSIFIED
```

Within the predeclared class A1-A4, the intrinsic probability measure on a
flat primitive causal diamond is uniquely

```text
mu_D(A) = Vol_4(A) / Vol_4(D).
```

This is a global classification under the stated assumptions, not merely a
test of the earlier `1+a u_D` family.

## Analytic result

Restriction naturality gives, for every nested `C subset D`,

```text
f_C = f_D / mu_D(C)
```

almost everywhere. The density rays therefore agree on subdiamonds. Since
causal diamonds form a basis and overlapping regions are linked by
subdiamond chains, these local rays patch to one positive global density
ray `[rho]`.

Poincare covariance sends this ray to itself:

```text
rho(gx) = c(g) rho(x),
```

where `c` is a continuous positive character. Its restriction to
translations has the form

```text
c(I,a)=exp(k_mu a^mu).
```

Semidirect-product compatibility requires `k` to be fixed by every Lorentz
transformation. The exact generator calculation has rank four on the
four-dimensional covector space, so the fixed space is `{0}`. The Lorentz
commutators also span the full six-dimensional Lorentz algebra, excluding a
separate continuous positive Lorentz character. Thus `c=1`; `rho` is
translation invariant and hence constant almost everywhere.

Normalizing on each diamond gives the displayed uniform measure.

## Executable results

The primary exact audit obtained:

```text
Lorentz generator count                 = 6
fixed-covector constraint rank          = 4
fixed-covector nullity                  = 0
Lorentz generator span rank             = 6
Lorentz commutator span rank            = 6
```

Each standard-basis nonzero covector violates three generator constraints.

The independent verifier used a separately selected four-equation witness
from `J12`, `J13`, and `K01`. Its exact determinant is:

```text
det(witness) = 1.
```

It therefore independently confirms that the Lorentz-invariant covector
space is zero-dimensional.

## Negative controls

### Translations alone

A nonzero real covector `k` defines a continuous positive translation
character through `exp(k.a)`. Its exponent is exactly additive. The audit
confirms that this construction survives translation covariance but violates
the Lorentz constraints. Uniformity is therefore not being inferred from
translation covariance alone.

### Earlier nested-diamond family

The exact response differences were retained:

```text
Delta <t>       = 3a/[4(960+19a)]
Delta <u_child> = -a(a+45)/[7(a+60)(19a+960)].
```

Their common nonnegative zero set is `{0}`. This reproduces the earlier
family-level result while the global density-ray proof closes the larger
class.

## Scope

The result applies to positive absolutely-continuous intrinsic measures on
flat primitive causal diamonds, with continuous density ray and full
proper-orthochronous Poincare covariance. Singular measures, curved cells,
and state-dependent measures with a supplied preferred covector remain
outside this theorem.

This result fixes the primitive flat-cell integration measure. It does not
derive the complete parent generator, its interacting spectral measure,
durability, a coupling, or alpha.

```text
uniform_flat_cell_measure_derived = true
spectral_density_derived = false
complete_parent_generator_derived = false
hypothesis_promoted_to_principle = false
construction_uses_alpha = false
alpha_computed = false
proof_authorized = false
```
