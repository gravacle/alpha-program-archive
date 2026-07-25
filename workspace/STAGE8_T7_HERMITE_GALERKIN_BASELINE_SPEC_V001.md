# Stage-8 T7 Hermite-Galerkin Baseline Spec v001

Date: 2026-07-24

## Purpose

Construct the first genuine nested finite-rank restrictions of the continuum
causal-cell parent and evaluate the one-cell completed-record baseline under
two predeclared quasifree state restrictions.

This is a convergence diagnostic. No finite value is a coupling or a proof
of the continuum limit.

## Pinned authorities

```text
6e24ceb6b18e6e6da5a6d21e872f90f6d79a324df9f305d226ab6edec863831b  STAGE8_T7_COMPLETED_CONTINUUM_RESPONSE_PROVENANCE_SPEC_V001.md
40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9  R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md
6f6b822ac8ccf9ea19659f4ccf811268f60a27a361f817ee6513479d63b62546  BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md
1fd82d0d42c7d7b1369adfa0e0061c80044afc847f7dae2f066bdfb89165e56f  STAGE8_T7_GAUSSIAN_PATH_SUM_REDUCTION_RESULT_V001.md
```

The authority correction is:

```text
STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001.md
```

Its hash is recorded by the execution script after this specification is
sealed.

## Galerkin family

Use normalized one-dimensional Hermite functions with oscillator length
`ell`. In three dimensions:

```text
Q_(n,ell) L2(R3)
 =span{phi_a(x/ell)phi_b(y/ell)phi_c(z/ell):
       0<=a,b,c<n}.
```

The spinor carrier is the tensor product with `C4`. The spaces are nested
in `n` and their union is a core for the free Dirac operator.

Freeze:

```text
n in {2,4};
ell in {1,sqrt(2)};
T_R=1 as the dimensionless cell coordinate unit;
tau_R=pi/sqrt(2).
```

The second scale is a regulator-scheme stress test, not an adjustable
physical length.

## Compressed parent

Construct the exact truncated momentum matrices from Hermite ladder
relations and:

```text
h_(0,n)=sum_j p_(j,n) tensor alpha_j.
```

For local cell time `s in [0,1]`, set:

```text
r(s)=min(s,1-s);
M_n(s)=Q_n 1_(|x|<=r(s)) Q_n;
v(s)=tau_R * 32 r(s)^3;
h_(lambda,n)(s)=h_(0,n)+lambda v(s)M_n(s) tensor S_n.
```

No periodic derivative, finite lattice Hamiltonian, fitted pulse, or
post-write operator is admitted.

Use second-order Strang propagation at:

```text
N_t in {12,24,48}.
```

## Cell-multiplication quadrature

Compute `M_n(s)` in spherical coordinates using:

```text
10 radial Gauss-Legendre nodes;
10 polar-cosine Gauss-Legendre nodes;
20 uniform azimuthal nodes.
```

At the primary `N_t=48` result, independently recompute the cell matrices
with:

```text
12 radial nodes;
12 polar-cosine nodes;
24 azimuthal nodes.
```

The quadrature comparison is an error diagnostic. It may not be used to
reshape the cell.

## State schemes

Compute both:

```text
C_n^(mix)=Q_n P_- Q_n;
C_n^(pure)=1_(-infinity,0)(h_(0,n)).
```

For `C_n^(mix)`, project the exact continuum symbol:

```text
P_-(p)=[I-alpha dot p/|p|]/2
```

with a `20^3` tensor Gauss-Hermite quadrature. Use no value at `p=0`;
the even quadrature contains no zero node.

The finite gauge-invariant quasifree expectation is:

```text
D_C(U)=det(I-C+C U).
```

The completed amplitude is:

```text
a_n=sum_lambda w_lambda D_C(U_lambda);
(w_-,w_0,w_+)=(-1/4,1/2,-1/4).
```

No amplitude or state scheme may be dropped.

## Mandatory checks

Report:

```text
Hermiticity of h_0 and M_n;
Clifford relations;
spectrum and contraction bounds of C_n^(mix);
projector error and rank of C_n^(pure);
absence or presence of finite zero modes;
unitarity of every propagated U_lambda;
time-step convergence for every scheme;
quadrature sensitivity at N_t=48;
n=2 to n=4 movement;
ell=1 to ell=sqrt(2) movement;
and all completed amplitudes.
```

## Predeclared interpretation

```text
if the construction checks pass:
  GENUINE_HERMITE_GALERKIN_BASELINES_COMPUTED

if either state scheme is not mathematically defined:
  HERMITE_GALERKIN_STATE_SCHEME_BLOCKED

if time or quadrature convergence fails:
  HERMITE_GALERKIN_NUMERICS_BLOCKED
```

Even the positive verdict does not prove continuum convergence or T7.

```text
physical_regulator_completed_record_baseline_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
