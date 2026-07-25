# Stage-8 T7 Continuum-Galerkin Provenance Correction v001

Date: 2026-07-24

## Authority correction

The covariance algebra and numerical momentum-block checks in:

```text
STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_RESULT_V001.md
```

are correct. Its stronger label, `PARENT_STATE_REGULATOR_RESTRICTION_DERIVED`,
is withdrawn.

The sealed specification required a nonzero nested finite-rank family
`Q_n` on `L2(R^3;C^4)` satisfying:

```text
[Q_n,h_0]=0;
Q_n -> I strongly.
```

That family does not exist for the free massless Dirac multiplier. A
nonzero finite-dimensional reducing subspace would contain an `L2`
eigenvector of `h_0`, while `h_0` has purely continuous spectrum. The
executable's isolated momentum points are generalized-eigenvalue samples,
not finite-rank subspaces of the continuum Hilbert space.

Consequently:

```text
continuum_covariance_formula_derived = true
momentum_block_covariance_regression_valid = true
genuine_finite_rank_continuum_restriction_constructed = false
parent_state_regulator_restriction_derived = false
```

The three-site baseline scope erratum remains in force.

## Correct successor construction

A genuine Galerkin family must instead satisfy:

```text
Q_n is finite rank and nested;
Q_n -> I strongly;
Q_n h_0 Q_n converges to h_0 on a common core;
Q_n M_c(t) Q_n converges strongly to M_c(t);
and the finite propagators converge strongly, uniformly on compact times.
```

Exact commutation with `h_0` is neither required nor possible.

Two state restrictions are to be carried forward without selecting between
them by output:

1. the inherited mixed quasifree covariance

```text
C_n^(mix)=Q_n P_- Q_n,
0<=C_n^(mix)<=I;
```

2. the finite-Hamiltonian pure vacuum

```text
C_n^(pure)=1_(-infinity,0)(Q_n h_0 Q_n),
```

when the finite operator has no zero mode.

For the mixed state the finite quasifree formula is the general Klich
determinant, not a Slater-compression determinant. For the pure state the
Slater formula applies. The continuum response is admissible only if both
schemes converge to the same normalized result.

## Record-cancellation result

The forward-sealed continuum-response gate has completed C1 and C2:

```text
w_-= -1/4;
w_0= +1/2;
w_+= -1/4;

sum w_lambda lambda^0 = 0;
sum w_lambda lambda^1 = 0;
sum w_lambda lambda^2 = -1;
sum w_lambda lambda^(2m+1) = 0.
```

For a multivariate Duhamel monomial the history sum factorizes by cell.
Every surviving term therefore contains each completed cell at least twice,
and with even multiplicity.

An independent finite parent, unrelated to the three-site regression,
reproduces its direct fixed-particle Fock amplitude by the signed
determinant-history formula with absolute difference:

```text
3.209897674977742e-17.
```

This establishes the finite representation-theoretic identity. It does not
establish the continuum limit.

## Primitive/full-amplitude distinction

The full charged complex amplitude and the primitive Stage-8 attenuation
are not the same object.

For the full complex amplitude, a common-Fock lift, a determinant-line
trivialization, and finite local renormalization remain open. In particular,
a finite gauge-invariant `c F^2` deformation changes the physical phase and
the final Thomson coefficient. Record moment cancellation does not by
itself fix `c`.

For primitive T7:

```text
Gamma_K(A)=-log|Z_K(A)|.
```

One common overall implementer phase does not change `Gamma_K`. Therefore
the full charged `F^2` phase ambiguity is retained as a downstream Q_spec
blocker and is not misused as a reason to stop the primitive modulus gate.
What T7 still needs is stronger:

```text
a genuine continuum Galerkin parent;
one well-defined completed transition modulus;
agreement of the two state-restriction schemes;
all finite connected baselines nonzero;
a volume-uniform zero-free neighborhood;
and the connected cluster/Hessian limit.
```

History-dependent phase ambiguities or failure of sharp-cell
Shale-Stinespring/Schatten convergence would still block even the modulus.

## Current verdict

```text
C1_exact_record_cancellation = DERIVED
C2_finite_stage_identity = DERIVED_AND_INDEPENDENTLY_VERIFIED
C3_sharp_continuum_implementability = OPEN
C4_full_complex_finite_renormalization = BLOCKED
C4_primitive_modulus_response = OPEN
C5_regulator_independence = OPEN

physical_regulator_completed_record_baseline_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```

## Next executable target

Construct a target-free nested Galerkin family on the actual continuum
one-particle space, compress:

```text
h_0;
M_c(t);
h_K(t);
P_-;
```

and evaluate the completed transition under both state schemes at multiple
nested levels. The finite values are convergence diagnostics only. A pass
requires an analytic strong-propagator approximation theorem and a
Schatten/phase argument for the completed modulus; numerical convergence
alone cannot promote the result.
