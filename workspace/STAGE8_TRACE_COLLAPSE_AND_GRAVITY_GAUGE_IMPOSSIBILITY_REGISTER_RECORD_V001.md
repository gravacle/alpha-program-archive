# Stage 8 Trace-Collapse and Gravity/Gauge Impossibility Register Record v001

## Status

```text
registration_record = true
source_layer = supervision
source_has_no_procedural_authority = true
principal_or_lane_adoption = false
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## Source

Source: `/Users/bgm/MB Work/alpha_supervision/RESULT_TRACE_COLLAPSE_THEOREM_AND_GRAVITY_GAUGE_IMPOSSIBILITY_2026-07-29.md`

Source SHA-256:

```text
a7b82f9a180945844b95dc3931a649591e7c7ad7449e26f035ce7f270cb50d5e
```

This artifact records the result into the governing cleanroom chain by path
and hash. It does not recompute the arithmetic.

## Theorem Recorded

The source states, at lines 9-14:

```text
Let `X, Y in gl(N,C)` with AT LEAST ONE traceless.
Tr_{Lambda^k}(XY) = C(N-2, k-1) * Tr_fund(XY)          [one traceless]
Tr_{Lambda^k}(XY) = C(N-2, k-1) * Tr_fund(XY) + C(N-2, k-2) * (Tr X)(Tr Y)     [general]
```

It further records at lines 20-26 that Cartan is not required: the bilinear
form is `GL(N)` invariant, `gl(N) = sl(N) + center`, and exact-rational checks
were run for generic non-commuting rational traceless generators at `N = 3,4,5,6`,
every `k`.

At lines 33-34 the source specializes this to `N = 5`, `k in {0,2,4}`,
giving `C(3,-1)=0`, `C(3,1)=3`, `C(3,3)=1`, and
`K_XY(x) = Tr_fund(XY) * S(x)`.

## Consequence for Gauge Ratios

The exact gauge ratios are retained as exact representation facts, not as
dynamical outputs. The source records at lines 44-48:

```text
With `H = Q + C`, `C = diag(1/3,1/3,-2/3,0,0)` the color-center cocharacter:
- `Tr(QC) = 0`, so **`K_QH = K_Q` IS EXACTLY THE TRACE-ORTHOGONALITY OF `C` TO `Q`**.
- `Tr(C^2)/Tr(Q^2) = 1/2`, so **`K_H/K_Q = 1 + Tr(C^2)/Tr(Q^2) = 3/2`**.
```

## Impossibility Proof Recorded

The source records the coefficient families at lines 137-145:

```text
C_V           : (d, 3)
C_R (Einstein): (d, 2)
a_4 layer     : (d, 1)
K_Q, K_H, K_QH: (t, 1)
```

and the criterion at lines 147-149:

```text
TWO COEFFICIENTS ARE EXACTLY PROPORTIONAL IFF THEY SHARE BOTH `w` AND `n`.
```

The sharp contradiction is at lines 151-163. Assuming
`a_4^grav(x) = lambda K_Q(x)` on an open interval leaves an `I_1(x)` coefficient
that must vanish:

```text
1/23040 = 0
```

The source states the structural reason at lines 165-170:

```text
THE CONTRADICTION LOCALISES ENTIRELY ON `Lambda^0`, AND THAT IS THE STRUCTURAL CONTENT:
THE SINGLET HAS DIMENSION 1 BUT INDEX 0.
```

Operational consequence, source lines 177-185: depth selection is provably
unavoidable on this carrier. There is no depth-cancels-in-the-ratio escape.
The ratio route is not killed; its existing `DEPTH_OPEN` condition becomes a
proven necessity.

## Sharper Admissibility Criterion

The source records at lines 94-102 that the collapse does not require Casimir
grouping as such. It requires the second-moment tensor

```text
sum_s w_s mu_s (x) mu_s
```

to be proportional to the Cartan metric. The same paragraph records that the
admissible weightings form a 7-dimensional subspace of the 16-dimensional
weighting space, and that enumerating all `2^16` level sets gives 27 nonempty
admissible subsets, only 7 of which are unions of whole `Lambda^k` blocks.

This is the governing-chain phrasing:

```text
admissibility_condition = SECOND_MOMENT_CONDITION
casimir_class_functionhood = sufficient_not_necessary
```

## Live Counterexample Inside the Parent Code

The source records at lines 104-123 that
`derive_alpha_br_homogeneous_operator_pullback_v001.py` builds on
`internal_abs_h_block(flux_degree)`, decomposed by `|H|` rather than by Casimir.
Lines 111-116 give exact restricted traces:

```text
| `|H|=0` | 8 | 4/3 | 0 | 0 | 0 | 0 |
| `|H|=1` | 8 | 4 | 8 | 16/3 | 2 | 4/3 |
```

The source conclusion at lines 116-119 is recorded verbatim for planning:

```text
NEITHER SECTOR GIVES `(3/2, 1)`. In the `|H|=0` sector `K_H` and `K_QH` VANISH OUTRIGHT.
Both indicator vectors are INADMISSIBLE under the second-moment criterion.
```

The surviving hypothesis is also recorded. Lines 129-133 state that
`MASS_CHEVALLEY` survives because `mass^dag mass = 1` per block, so the mass
enters as a uniform shift absorbed into `x`, not as a splitting.

## Register Payload

```text
trace_collapse_theorem_registered = true
gravity_to_gauge_x_independent_ratio_impossible_on_lambda_even_c5 = true
depth_selection_unavoidable_on_this_carrier = true
ratio_route_killed = false
ratio_route_depth_open_converted_to_proven_necessity = true
admissibility_condition_recorded_as_second_moment_condition = true
live_flux_sector_counterexample_recorded = true
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

