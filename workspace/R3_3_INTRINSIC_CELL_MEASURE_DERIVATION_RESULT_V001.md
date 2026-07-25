# R3.3 Intrinsic Cell-Measure Derivation Result

## Verdict

```text
INHERITED_REFINEMENT_NATURALITY_FORCES_UNIFORM_MEASURE
```

No new strict-locality principle is adopted.

The sealed BID response definition binds response assembly to intrinsic
per-cell data:

1. every disjoint cell supplies its own `H_c`, `r_c`, `U_c`, and `A_c`;
2. every cell contributes its own `V_cell` local response;
3. residual shape-dependent scalars are forbidden;
4. response must commute with common refinement; and
5. a cellulation-dependent response fails the gate.

Therefore a subregion promoted to an elementary cell must be evaluated by
that child's intrinsic cell measure. It may not retain a weighting profile
defined by an arbitrarily chosen parent.

## Exact nested-diamond result

For the unit parent diamond and its past half-diamond child, the exact raw
moments, after mapping the child to unit-diamond coordinates, are:

```text
Vol/pi                         = 1/24
integral u_child/pi            = 1/1440
integral u_parent/pi           = 19/23040
integral t/pi                  = -1/96
integral t u_child/pi          = -1/5760
integral t u_parent/pi         = -1/5760
integral u_child^2/pi          = 1/50400
integral u_child u_parent/pi   = 1/57600
```

For

```text
d mu_a proportional to [1+a u_cell(x)] d^4x,
```

the parent-restricted minus child-intrinsic response means are:

```text
Delta <t>
  = 3a/[4(960+19a)],

Delta <u_child>
  = -a(a+45)/[7(a+60)(19a+960)].
```

For the predeclared family `a>=0`, both vanish together only at `a=0`.
Every `a>0` gives different response physics to the same child region
depending on whether it is treated as a cell or as part of its parent.

Hence all nonuniform members of the exhibited Lorentz-covariant family
violate BID's inherited refinement-naturality rule. The surviving measure is

```text
d mu_D(x)=d^4x/Vol(D)
```

on a flat primitive causal diamond.

## Scope

This closes the primitive flat-cell measure selector and removes one
candidate premise. It does not yet derive the generator's root spectral
density, prove its absolute continuity, or promote the complete
direct-limit hypothesis.

```text
intrinsic_per_cell_response_binding = true
uniform_flat_cell_measure_derived = true
new_strict_locality_principle_adopted = false
spectral_density_derived = false
hypothesis_promoted_to_principle = false
alpha_computed = false
```
