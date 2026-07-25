# R3.4 Parent-to-Outgoing GNS Compatibility Specification v001

## Purpose

This target-independent gate tests whether the existing microscopic parent
lineage derives the state and dynamics of the outgoing record limit together.
It may not select a continuum generator, root profile, or spectral density
independently of that parent.

No alpha, measured coupling, mass, endpoint, or cosmological value may enter.

## Exhaustion, not subdivision

Invisible bivalent subdivisions are first reduced by the existing graph
refinement quotient. The direct system then exhausts the future causal
record complex by adding physical cells:

```text
K_1 subset K_2 subset ...
```

For the record algebra,

```text
iota_nm(A)=A tensor I
```

on newly added distinguishable record factors. Source CAR inclusions use the
already typed local Cauchy-data net. This gate does not shrink a primitive
cell to zero or replace its unit counting metric by an unproved refinement
metric.

## Required parent data

For every finite `K_n`, one and the same parent construction must provide:

1. a finite algebra `A_n`;
2. a normalized state `omega_n`;
3. a self-adjoint generator or derivation `delta_n`;
4. the finite first-opening root/public-label observables;
5. every boundary or overlap term.

The following must then be derived:

```text
omega_m o iota_nm = omega_n;
delta_m o iota_nm = iota_nm o delta_n
```

on each fixed interior local observable once the exhaustion contains its
interaction neighborhood. A nonzero derived boundary cocycle may replace the
second equality only if its support and limit are computed from the parent.

## Static-parent negative control

The finite one-cell incidence generator is

```text
c_partial =
  [[0,0,-i],
   [0,0,+i],
   [+i,-i,0]]
```

in the basis `(|r>,|p>,|e>)`.

The completed-label state `omega_p(A)=<p|A|p>` is invariant only if

```text
omega_p(exp(i t c_partial) A exp(-i t c_partial))=omega_p(A)
```

for all `A,t`. The evaluator must test this rather than infer invariance from
the existence of a public label. It must also retain the exact finite result

```text
exp(-i tau_R c_partial)|p>=|r>,
tau_R=pi/sqrt(2).
```

If the static parent fails this test, a successful outgoing construction
must derive from the parent one of:

```text
causal post-write decoupling;
an invariant pointer/superselection algebra;
or a parent-derived scattering/outgoing state.
```

It may not simply declare the product-label state stationary.

## GNS/scaling closure bar

Return `PARENT_TO_OUTGOING_LIMIT_DERIVED` only if all of the following are
present in one lineage:

1. compatible finite parent-selected states;
2. compatible finite parent derivations;
3. an inductive-limit state and GNS triple;
4. a strongly continuous implemented automorphism group;
5. a nonzero root/public-label limit;
6. a derived generator form domain containing that root;
7. the compact write region or its causal switch-off;
8. a computed absence or controlled inventory of bound/point spectrum; and
9. a root spectral measure derived from those objects.

Return `STATIC_PARENT_STATE_DYNAMICS_MISMATCH` if the existing static parent
fails the completed-label invariance test and no parent-derived alternative
is present.

Return `PARENT_LIMIT_UNDERDETERMINED` if multiple response-inequivalent
parent actions, states, derivations, or outgoing limits survive.

## Fixed interpretation

The quasi-local covector-ray lift closes the public outgoing-algebra
sub-obligation. It does not supply a generator.

The free-flat continuum multiplier is a conditional mathematical model until
this gate derives its parent-to-limit map.

## Fixed statuses

Regardless of outcome:

```text
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
