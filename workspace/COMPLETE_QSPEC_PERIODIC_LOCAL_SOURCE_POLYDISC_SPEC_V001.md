# Complete-Qspec Periodic Local-Source Polydisc Spec v001

Date: 2026-07-25

## Purpose

Prove or block a volume-uniform zero-free polydisc for independently
addressable connection sources on the frozen periodic regression regulator.
The proof must cover every volume `N>=1` and every source assignment

```text
(z_1,...,z_N),  |z_j|<=1/500.
```

It may not infer a multivariable result from the already-proved homogeneous
disk. It must instead prove a nonautonomous invariant splitting for arbitrary
ordered products of the locally sourced transfer maps.

No coupling or alpha target may be read or used.

## Frozen authorities

```text
24c8c7f5dc5ffa8be553de6a85899e7f0142347b378b0ca97c5252dadb573bb0  COMPLETE_QSPEC_PERIODIC_LOCAL_SOURCE_LIFT_DERIVATION_V001.md
506131686e97a27e90fb29d614ed1f74a33ea5ceec941a0805aa6dd7468ae178  COMPLETE_QSPEC_PERIODIC_ZERO_FREE_PROMOTION_RESULT_V001.md
8b47ff6af29537289675dd40d8095a2dc606147a93fb524a3ff659e0aabb6bb7  COMPLETE_QSPEC_PERIODIC_ZERO_FREE_PROMOTION_SPEC_V001.md
3a5c7a7d6b3ed2ae4d9c69feab78bdb34c2222149415e9fa0e8eb5b38f4670f1  COMPLETE_QSPEC_PERIODIC_ZERO_FREE_ZERO_ALIGNMENT_ADDENDUM_V001.md
2c193f34786c2eeff57a6ea611116448926076d676fd177b5f9c73980ec6496a  COMPLETE_QSPEC_ZERO_TRANSFER_DYADIC_BALL_CERTIFICATE_RESULT_V001.md
93a37fb83fe9b7264808a80b2f7bffb487af642180affb6918c5b98b65dbb74b  stage8_execution/work/QSPEC_zero_transfer_dyadic_ball_certificate_v001.json
1cd9528bc6872a3a28df828a452a165f8672cccc455a64323edab9e0905bf69d  scripts/verify_complete_qspec_periodic_analytic_continuation_v003.py
```

The exact emitted objects remain:

```text
transfer       69d6a95de251be3e3aa83d7344c7961b2023f41416399b760d3096fcde83718b
trace column   07506154f602a1fa17e32c81f4bc377e547868eb4bf540ed11248949afea0876
start vector   510205f86d4b068828d0a2ca0bfa4d6e43c62f44c555b7a627d25b20e0d4e4c7
analytic zero  5e59e660c1b0859e915f86258944972b0ecf5e939c4ca264158edc3eb95aec39
```

Any mismatch aborts execution.

## P0: exact anchor and local perturbation

Use the accepted orthogonal decomposition

```text
P=|p><p|,  Q=I-P,
A=P+R,
||R||_2<r,  r=203/250.
```

The physical trace row `l` obeys `lQ=0`. Let `x` be the frozen start vector.
Reconstruct their exact dyadic balls and retain the accepted analytic bound:

```text
||T_j(z_j)-A||_2<=eta
```

for every `|z_j|<=1/500`, where `eta` is recomputed with outward-rounded Arb
arithmetic from the frozen analytic formula and the `1e-10` zero-alignment
allowance. No sampled norm may carry this step.

## P1: block bounds

For an arbitrary finite source assignment, put

```text
M_j=T_j(z_j)=
  [a_j  b_j]
  [c_j  D_j]
```

relative to `P+Q`. The operator-ball bound must imply

```text
|a_j-1|<=eta,
||b_j||<=eta,
||c_j||<=eta,
||D_j||<=r+eta.
```

Extend the finite sequence by `A` outside its physical interval. This
extension is a proof device only and does not change the finite product.

Freeze

```text
X=1/20,
d=1-eta(1+X),
n=eta+(r+eta)X.
```

Require, with outward rounding,

```text
d>0,
n/d<X,
L_G=(r+eta)/d + eta*n/d^2 <1.
```

The same bounds apply to the adjoint sequence.

## P2: nonautonomous graph theorem

For each sequence satisfying P1, prove by pullback contraction that there
exist unique bounded right graph vectors `u_j` and bounded left graph
covectors `v_j`, both of norm at most `X`, such that the corresponding
rank-one projections

```text
Pi_j
 =(p+u_j)(p^dagger+v_j)/(1+v_j u_j)
```

obey

```text
M_j Pi_(j-1)=Pi_j M_j.
```

The proof must explicitly establish:

```text
||Pi_j-P|| <= delta_P
delta_P=(2X+2X^2)/(1-X^2);

|s_j|>=d
when M_j(p+u_(j-1))=s_j(p+u_j);

||M_N...M_1(I-Pi_0)||<=kappa B^N
on the stable bundle,

B=r+eta+eta X,
kappa=(1+X)/(1-X).
```

The stable estimate must come from the left-graph kernel coordinates
`w-p(v_j w)`, so the similarity loss is paid only at the two endpoints,
not once per cell.

## P3: finite-volume nonvanishing

Because `||A||=1` and `lQ=0`,

```text
l A^N x=l x
```

for every `N>=1`. For each `1<=N<=6`, use the nonautonomous telescoping
identity to certify

```text
|l M_N...M_1 x-1|
 <=|l x-1|
   +||l|| ||x|| N eta(1+eta)^(N-1)
 <1.
```

This is valid for arbitrary, independently chosen `M_j`; no homogeneous
power may be substituted.

## P4: all larger volumes

The invariant splitting gives a leading amplitude with lower bound

```text
coefficient_min d^N,

coefficient_min
 =|l x|-||l|| ||x|| delta_P.
```

The stable remainder has upper bound

```text
||l|| ||x|| kappa B^N.
```

Define

```text
q=B/d,
prefactor=||l|| ||x|| kappa/coefficient_min.
```

Require

```text
coefficient_min>0,
q<1,
prefactor q^7<1.
```

Then the leading amplitude cannot be cancelled for any `N>=7`.

## P5: analytic consequence

Only if P0-P4 pass, conclude:

```text
Z_N(z_1,...,z_N)!=0
```

for every integer `N>=1` on the closed local-source polydisc. Since the open
polydisc is simply connected, the origin fixes a unique holomorphic branch

```text
F_N(z_1,...,z_N)
 =Log[Z_N(z_1,...,z_N)/Z_N(0,...,0)].
```

This proves existence of the multivariable connected generator. It does not
prove decay or absolute summability of its cumulants.

## Execution discipline

The verifier must:

1. run under isolated Python;
2. verify this sealed spec, all authority hashes, and the full hashed
   `python-flint` runtime;
3. reconstruct all exact dyadic boundary scalars and every verdict-bearing
   inequality with outward-rounded Arb arithmetic;
4. emit every intermediate bound and pass boolean;
5. attest that no coupling or alpha target was read.

No threshold may be changed after execution.

## Pass rule and scope

Only if every obligation passes, return:

```text
FROZEN_PERIODIC_LOCAL_SOURCE_POLYDISC_PROVED
```

and set:

```text
frozen_periodic_local_source_polydisc_proved=true
finite_volume_multivariable_log_generator_proved=true
```

Even on pass:

```text
physical_continuum_local_source_addressability_derived=false
periodic_connected_linked_cluster_density_proved=false
all_stage8_regulators_zero_free_proved=false
all_connected_cellulations_linked_cluster_proved=false
kappa_record_computed=false
physical_Thomson_stiffness_computed=false
coupling_evaluation_authorized=false
alpha_computed=false
proof_authorized=false
```
