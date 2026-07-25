# Stage-8 T7 Actual-Parent Regulated CAR Operator Response Spec v001

Date: 2026-07-25

## Status

```text
SPECIFICATION_SEALED_BEFORE_EXECUTION
```

This is Phase A of the approved Route-2 repair. It constructs and seals the
operator-valued CAR response on a genuine member of the inherited
Hermite-Galerkin continuum exhaustion. It does not evaluate an incoming
state. State evaluation is a separately sealed Phase-B gate that may begin
only after the Phase-A result and its independent verification are sealed.

No coupling target, alpha value, endpoint value, or prior candidate response
coefficient may be read or used.

## Frozen authorities

| Role | Path | SHA-256 |
|---|---|---|
| Complete parent specification | `R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md` | `40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9` |
| Complete Q-spec and disclosed state | `STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md` | `5026afb89b52ead9f309168cb2fa4f06b81039f8dd01b8940f40e64aad679a7e` |
| Continuum-Galerkin provenance correction | `STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001.md` | `a1258dcf40732f0e3fce358a68ffdbd34bc347d70283550440582a1129bec510` |
| Hermite-Galerkin construction spec | `STAGE8_T7_HERMITE_GALERKIN_BASELINE_SPEC_V001.md` | `80aa4e1722c117e8195ce0fb2ae3fc37262bc8fc2ba5d79a6dd38cd1029bc26d` |
| Hermite numerical protocol | `STAGE8_T7_HERMITE_GALERKIN_NUMERICS_PROTOCOL_V001.md` | `950e957ec2aa1022509b57df48f4f701e717e5dcbb18731332abbf55bf57dadd` |
| Exact mixed-covariance result, pinned for Phase B | `STAGE8_T7_EXACT_HERMITE_MIXED_COVARIANCE_RESULT_V001.md` | `235246abd1c4df69c80bda8f79494c342e30178504dadec411612c18d6f8685b` |
| Pure-vacuum convergence result, pinned for Phase B | `STAGE8_T7_PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_RESULT_V001.md` | `a79939adf1d7185fdf4d6ec5ccb929de2e4f5997bee2ed085c0d63164dc8e370` |
| Gaussian path-sum theorem | `STAGE8_T7_GAUSSIAN_PATH_SUM_REDUCTION_RESULT_V001.md` | `1fd82d0d42c7d7b1369adfa0e0061c80044afc847f7dae2f066bdfb89165e56f` |
| Existing Hermite primary result | `stage8_execution/work/T07_hermite_galerkin_baseline.json` | `87593740c5f35f68ea1c484c7ab304fbd12ee7b54f62f48f38417c80a2e33f7c` |
| Existing Hermite independent result | `stage8_execution/work/T07_hermite_galerkin_baseline_verification.json` | `fc55cdedb059d31843b2490a9af2a74902c20acaed08793d64ff5c1e2a7f32f8` |
| Three-site scope correction | `STAGE8_ROUTE2_CAR_STATE_BRIDGE_SCOPE_CORRECTION_V001.md` | `4e1282bc800c47441d255e9d9d576958608d955dce15f02969261cd6e601e268` |
| Route-2 architecture amendment | `STAGE8_T7_OPERATOR_VALUED_PRIMITIVE_RESPONSE_ARCHITECTURE_AMENDMENT_V001.md` | `8a7f52ffa2500d20ad834b11e3762ed114ee1a201f2fec18bcb119e3c7ead860` |
| Complete-Q-spec state binding | `STAGE8_ROUTE2_COMPLETE_QSPEC_STATE_BINDING_V001.md` | `5cbcd28ee493ba43e3d36158d80c4202230f056808caf2b36420f08c38fbd0d7` |
| Route-1 special-case falsifier binding | `STAGE8_ROUTE1_SPECIAL_CASE_CONSISTENCY_BINDING_V001.md` | `460e87522884e703968025081cceccc0153af3cda27410c397fc2a09a0b367e3` |
| Route-1 frozen specification | `STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_SPEC_V001.md` | `2f2aa7f7397b70616fa5c9e8ed628ca1d1e819bb698133a169c6d544086b3cde` |
| Route-1 sealed result | `STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_RESULT_V001.md` | `76f5505e3aa1fdc11102f782ed8ee40e49787bb38e3a2524e17b92fd8de46740` |
| Route-1 executor | `scripts/derive_stage8_t7_primitive_operator_response_v001.py` | `3d8aea1a4779b0bfe7a472dca1fab0642750e8e010e339b9e3b100197b75a18c` |
| Route-1 content-addressed runtime | `provenance/stage8_t7_numpy_runtime_manifest_v001.json` | `f2e820d5d7a53335f1a6aacdbc03331d18e6afa350f99b7d2f2abd59d77bc46b` |
| Primitive transition-amplitude authority | `BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md` | `6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb` |

Every hash is verified before construction. A mismatch returns `BLOCKED`.
The two finite state schemes are pinned here but neither covariance is
applied during Phase A.

## A1 - Genuine Galerkin carrier

Use normalized three-dimensional Hermite functions with oscillator length
`ell`. The finite one-particle carrier is

```text
H_(n,ell)
 =span{phi_a(x/ell) phi_b(y/ell) phi_c(z/ell):
        0<=a,b,c<n} tensor C^4.
```

The spaces are nested in `n`, converge strongly to the continuum carrier,
and are the already-declared replacement for the invalid isolated-momentum
and periodic-three-site state regulators.

Phase A uses the first nontrivial member

```text
n=2;
ell in {1,sqrt(2)};
spatial dimension=8;
spinor dimension=32.
```

Both `ell` values are executed and retained. Neither may be selected by its
output. The old 12-dimensional periodic fixture remains only a separate
operator regression and is not compared as the same carrier.

Construct:

```text
h_(0,n,ell)=sum_j p_(j,n,ell) tensor alpha_j;
S_n=-i slash(n) gamma^5.
```

For local cell time `t in [0,1]`, use the already-sealed causal ball:

```text
r(t)=min(t,1-t);
M_(n,ell)(t)=Q_(n,ell) 1_(|x|<=r(t)) Q_(n,ell);
v(t)=(pi/sqrt(2)) 32 r(t)^3.
```

No periodic derivative, isolated momentum point, finite zero-mode filling,
fitted pulse, or post-write operator is admitted.

## A2 - Forward-sealed smooth connection direction

The finite type bridge requires a nontrivial relative history. Define the
smooth causal-diamond function

```text
s_-(t,x)=t^2-|x|^2;
s_+(t,x)=(1-t)^2-|x|^2;
s(t,x)=s_-(t,x)s_+(t,x);

b_D(t,x)
 =exp(16-1/s(t,x)),
    0<t<1 and s_-(t,x)>0 and s_+(t,x)>0;
 =0,                 otherwise.
```

The time-oriented joint positivity region is exactly the open unit causal
diamond `0<t<1`, `|x|<min(t,1-t)`. The zero extension is `C-infinity`,
compactly supported in the closed diamond, vanishes to all orders at its
boundary and tips, and satisfies `b_D(1/2,0)=1`.

Use the fixed-gauge, unit-charge spatial connection:

```text
A_x^(a)(t,x)=a b_D(t,x);
A_y=A_z=A_0=0;

B_(D,n,ell)(t)=Q_(n,ell) b_D(t,x) Q_(n,ell);
J_(n,ell)(t)=-B_(D,n,ell)(t) tensor alpha_x;

h_(lambda,n,ell)(t;a)
 =h_(0,n,ell)
  +lambda v(t) M_(n,ell)(t) tensor S_n
  +a J_(n,ell)(t).
```

The sign and unit coefficient are the minimal-coupling convention for the
already-declared unit charge. The profile is fixed by the same causal
diamond but is not a physical field-normalization claim. This is explicitly
a fixed-gauge finite response diagnostic. Phase A claims no local gauge
covariance: a future covariance theorem must transport the Galerkin carrier
by `exp(i chi)` while transforming `A -> A+d chi`.

Frozen history values and pairs:

```text
a in {0,7/100,-11/100,13/100,4/100};
(a_+,a_-) in {(0,0),(7/100,-11/100),(13/100,4/100)}.
```

Changing the connection direction after execution requires a successor
specification. It may not be changed because of the response value.

## A3 - Record spectral resolution

Use one qutrit record factor:

```text
H_R=C^3;
|ready>=|0>;
|pointer>=|1>;
c=
  [[0,0,-i],
   [0,0,+i],
   [+i,-i,0]].
```

Construct its spectral projectors `P_lambda` without inserting their known
weights:

```text
lambda in {-sqrt(2),0,+sqrt(2)};
p_lambda=<ready|P_lambda|ready>;
w_lambda=<pointer|P_lambda|ready>.
```

The executor must recover

```text
p_lambda>=0;
sum_lambda p_lambda=1;
sum_lambda P_lambda=I_3;
```

and independently verify the already-derived pointer weights. It may not
type those weights into the response.

For every `lambda` and history `a`, let `u_lambda(a)` be the one-particle
propagator generated by `h_lambda(t;a)`.

## A4 - Full CAR response as a Gaussian sum

The number-preserving quasifree lift and the spectral resolution imply the
complete source-record propagator

```text
W(a)=sum_lambda Gamma(u_lambda(a)) tensor P_lambda.
```

With ready injection `i_r`, the complete and pointer-record Kraus operators
are

```text
K_x(a)
 =sum_lambda <x|P_lambda|ready> Gamma(u_lambda(a));

K_pointer(a)
 =sum_lambda w_lambda Gamma(u_lambda(a)).
```

For each frozen pair, derive and construct:

```text
R_all(a_+,a_-)
 =sum_x K_x(a_-)^dagger K_x(a_+)
 =sum_lambda p_lambda
    Gamma(u_lambda(a_-)^dagger u_lambda(a_+));

R_pointer(a_+,a_-)
 =sum_(mu,lambda) w_mu^* w_lambda
    Gamma(u_mu(a_-)^dagger u_lambda(a_+)).
```

These are finite sums of legitimate Gaussian second quantizations, not one
postselected determinant and not a replacement by one `Gamma(k)`.

The sealed Phase-A operator artifact is the complete Gaussian-sum
representation:

```text
{coefficients, one-particle cross operators,
 record projectors, history labels, carrier metadata}.
```

Every matrix in that representation must be written as a content-addressed
binary artifact and included in the result seal.

## A5 - Direct one-source comparison

Independently construct the direct one-source source-record propagator on

```text
H_(n,ell) tensor H_R
```

from:

```text
H_direct(t;a)
 =h_0 tensor I_R
  +v(t) M(t) tensor S_n tensor c
  +a J(t) tensor I_R.
```

Resolve all three final record outcomes and form `R_all^(1)` and
`R_pointer^(1)` by both Kraus sums and direct unitary compression.

Evaluate the Phase-A Gaussian-sum representation in the one-particle sector,
where `Gamma_1(U)=U`, and require equality to the independently propagated
direct response, outcome by outcome and for both response kernels. This is
the same-carrier one-source restriction required by the scope correction.

No equality or intertwiner with the old periodic three-site response is
claimed.

The sealed one-dimensional Route-1 comparator is also re-executed unchanged.
Its completed component and exhaustive kernel must match the Route-2
special-case formulas at both frozen comparator history pairs. Failure blocks
Phase A. Passing remains only a consistency falsifier and does not imply
that the Hermite parent has a one-dimensional source restriction.

Before re-execution, verify the nested hashes in the frozen binding,
specification, result, executor, and runtime manifest. Use the original
comparator formulas, history pairs, generic compression path, and `1e-10`
acceptance threshold. Any mismatch blocks Phase A.

The canonical sealed Route-1 tree and result are read-only. Re-execute the
unchanged executor only inside a content-addressed isolated snapshot that
contains its complete verified authority allowlist and a fresh output path.
Hash the snapshot result, import only that new hash into the Phase-A report,
and verify before and after execution that the canonical result hash remains
`6dbda44a0f21a28b57f114654a6df79fc091ccfd601c38518fd5cf5f21697dcc`.

## A6 - Exact identities and frozen numerics

For both `ell` values and every frozen history pair verify:

```text
R_all^(1)(a,a)=I;
R_all^(1)(a_+,a_-)^dagger=R_all^(1)(a_-,a_+);
||R_all^(1)(a_+,a_-)||_2<=1;

0<=R_pointer^(1)(a,a)<=I;
R_pointer^(1)(a_+,a_-)^dagger=R_pointer^(1)(a_-,a_+);
||R_pointer^(1)(a_+,a_-)||_2<=1.
```

Frozen execution:

```text
n                              =2;
ell                            ={1,sqrt(2)};
time-step resolutions          ={12,24,48};
independent RK4 resolutions    ={192,384};
primary cell quadrature        =(10 radial,10 polar,20 azimuthal);
independent cell quadrature    =(12 radial,12 polar,24 azimuthal);
matrix arithmetic              =IEEE-754 binary64 / complex128.
```

The canonical primary basis order is lexicographic `(a,b,c,s)`, with the
Dirac spin index `s` fastest, then `c`, `b`, and `a`. The independent
verifier may use a different ordering or phase convention, but it must
compute, before any propagation, the basis-overlap matrix

```text
S_ij=<e_i^primary,e_j^independent>
```

solely from the sealed Hermite basis metadata and an independent overlap
quadrature. Response matrices may not enter the construction of `S`;
Procrustes, SVD, eigenvector, or other response-dependent alignment is
forbidden. Require `||S^dagger S-I||_2<=2e-11` and compare transported
matrices:

```text
R_primary versus S R_independent S^dagger.
```

The independent source, its test harness, the third comparison program and
its test harness, both strict read allowlists, the comparison norms and
component thresholds below, and the shared content-addressed runtime
manifest are all sealed before either numerical lane runs. Neither the
independent executor nor comparator may import the primary executor or any
primary construction helper.

The independent lane executes first, while the future primary output paths
are absent from its read allowlist. It atomically writes and hashes an
immutable precomparison bundle containing:

```text
carrier and basis metadata;
record eigenvalues, projectors, p_lambda, and w_lambda;
every u_lambda(a);
every one-particle cross operator;
every direct one-source Kraus member and response;
every all-outcome and pointer aggregate kernel;
all residuals and RK4 tails.
```

Only after that bundle and its manifest are sealed may the primary lane run.
A third, separately hashed comparison program then consumes both bundles.
The comparison must check, under the precomputed `S`, every corresponding
projector, coefficient, propagator, cross operator, and aggregate kernel.
It may not compare only the two final aggregate responses.

The comparator uses absolute value for scalar coefficients and operator
2-norm for matrices. Every component passes separately:

```text
carrier dimensions and discrete labels             exact equality;
record eigenvalue/coefficient absolute difference  <=2e-11;
record-projector operator-2-norm difference         <=2e-11;
basis-overlap unitarity residual                    <=2e-11;
transported propagator difference                   <=3e-4;
transported one-particle cross-operator difference  <=3e-4;
transported direct Kraus-member difference          <=3e-4;
transported direct response difference              <=3e-4;
transported aggregate-kernel difference             <=3e-4.
```

No aggregation can hide a component failure. Any one failed comparison
returns `ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_BLOCKED`.

At each midpoint `t_k=(k+1/2)/N_t`, the primary chronological Strang step is
fixed:

```text
F=exp[-i h_0 dt/2];
A=exp[-i a J(t_k) dt/2];
G_lambda=exp[-i lambda v(t_k) M(t_k) tensor S_n dt];

Step_lambda=F A G_lambda A F;
U_(k+1)=Step_lambda U_k.
```

The direct source-record path uses the same order with

```text
G_direct
 =exp[-i v(t_k) M(t_k) tensor S_n tensor c dt].
```

All exponentials of Hermitian matrices are computed by an explicitly
Hermitian eigendecomposition. No factor order may change after execution.
The independent verifier rebuilds the same time-ordered exponential with the
classical fourth-order Runge-Kutta method applied to

```text
dU/dt=-i h(t) U;
U(0)=I;

k1=f(t,U);
k2=f(t+dt/2,U+dt k1/2);
k3=f(t+dt/2,U+dt k2/2);
k4=f(t+dt,U+dt k3);
U_next=U+dt(k1+2k2+2k3+k4)/6.
```

The Hamiltonian and both Galerkin multiplication matrices are independently
evaluated at each displayed RK4 stage time. No midpoint cache is substituted
at the half or endpoint stages.

For each `ell`, each nontrivial history pair, and each kernel
`q in {all,pointer}`, define in operator 2-norm:

```text
d_12_24(q)=||R_q^(24)-R_q^(12)||_2;
d_24_48(q)=||R_q^(48)-R_q^(24)||_2;
rho(q)=d_12_24(q)/d_24_48(q).
```

If `d_24_48<=10^-15`, the tail is unresolved and the gate blocks rather than
forming `0/0`. Every nontrivial `rho(q)` must pass separately; no averaging
or favorable-case selection is allowed.

The primary/independent response difference is the maximum transported
operator-2-norm difference over both `ell` values, both nontrivial history
pairs, and both kernels, comparing the primary `N_t=48` result with the
independent `N_t=384` result. The independent `192`-to-`384` tail is emitted
separately for every `ell`, nontrivial history pair, and kernel. Every case
must be no larger than one quarter of the frozen primary/independent
tolerance; no averaging or favorable-case selection is allowed.

Connection sensitivity is a preregistered non-vacuity gate. Define:

```text
S_conn(ell)
 =||R_all^(48)(7/100,-11/100)-I||_2;

E_conn(ell)
 =max {
    d_24_48(all),
    ||R_all,primary_quadrature^(48)
      -R_all,independent_quadrature^(48)||_2,
    ||R_all,primary^(48)-S R_all,independent^(384) S^dagger||_2,
    ||S R_all,independent^(384) S^dagger
      -S R_all,independent^(192) S^dagger||_2
   }.
```

Require:

```text
max_(t_k) ||J_(n,ell)(t_k)||_2 > 10^-6, separately for each ell;
S_conn(ell) > 20 E_conn(ell), separately for each ell.
```

This blocks an implementation that omits the connection term or produces
only numerical-noise sensitivity. Failure is retained; the multiplier `20`
may not be revised in this version.

Frozen pass thresholds:

```text
Hermiticity/projector residual                <=2e-11;
record spectral completeness residual         <=2e-12;
Gaussian-sum/direct one-source residual        <=3e-9;
Kraus-sum/direct-compression residual          <=3e-9;
same-history identity residual                 <=3e-9;
adjoint-exchange residual                      <=3e-9;
contraction/positivity spectral allowance      <=3e-9;
each nontrivial split-step convergence ratio   >=3.2;
every primary/independent component difference <=its preregistered bound.
```

The independent tolerance is fixed above the previously sealed Hermite
second-order tail scale and is not a precision claim. Every raw residual,
time-step difference, and quadrature difference must be emitted.

Any runtime exception, authority mismatch, failed identity, failed
one-source restriction, missing matrix artifact, or independent-verifier
failure returns an atomic blocked result. Thresholds may not be changed
after execution; a successor specification is required.

## A7 - Ordering and verdict

Phase A may return

```text
ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_DERIVED
```

only if A1-A6 pass and the primary and independent bundles are sealed.

Only then may a separately forward-sealed Phase-B specification evaluate
both predeclared finite state schemes on the exact Phase-A Gaussian-sum
hashes. Phase B may not recompute, replace, or select the response after
seeing either scalar.

Passing Phase A establishes a finite operator-to-CAR representation on one
genuine continuum-exhaustion member. It does not establish a continuum
limit, regulator independence, zero-free neighborhood, linked-cluster
density, physical connection normalization, coupling, or alpha.

## Protected status

```text
actual_parent_regulated_CAR_operator_response_derived = false
actual_parent_same_carrier_one_source_restriction_derived = false
route1_special_case_consistency_falsifier_frozen = true
route1_special_case_consistency_falsifier_passed = true
route1_special_case_reexecution_passed = false
actual_parent_route1_line_restriction_derived = false
actual_finite_parent_state_evaluation_derived = false
actual_finite_parent_operator_to_scalar_bridge_derived = false
interacting_continuum_CTP_amplitude_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
ER_fork_closed = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
