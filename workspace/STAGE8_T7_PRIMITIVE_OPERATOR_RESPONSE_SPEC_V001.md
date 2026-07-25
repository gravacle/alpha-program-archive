# Stage-8 T7 Primitive Operator Response Specification v001

Date: 2026-07-25

## Status

```text
SPECIFICATION_SEALED_BEFORE_EXECUTION
```

This specification is target-free. It is written before its executor and
before the Route-2 Stage-8 architecture amendment. It derives only the
operator-valued response forced by the finite causal parent. It does not
select a source state, evaluate a scalar logarithm, compute a response
coefficient, or authorize a coupling calculation.

## Frozen authorities

| Classification | Artifact | SHA-256 |
|---|---|---|
| Frozen parent specification | `R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md` | `40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9` |
| Positive finite-parent result | `R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md` | `345d447eaf6d730caa6fa655b92a7b0cd93a68b5f86e0c8929cf969f40aeb7cb` |
| Adopted primitive-class boundary and positive CAR lift | `BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md` | `949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd` |
| Sealed actual-parent regression bundle | `stage8_execution/t7_actual_parent_record_amplitude/T07_ACTUAL_PARENT_RECORD_AMPLITUDE_V001.seal.sha256` | `322510075e1f8f6616eb47b1325f47963d90e8adaf20e83f7209c8be5f048b40` |
| Negative scalarization result bundle | `STAGE8_T7_SOURCE_SCALARIZATION_NO_GO_RESULT_V001.seal.sha256` | `199987876a3c7a6b9ed6bfda123256daddf0f5dd96cfdf929e3e155ddb32fc35` |
| Positive one-handle amplitude derivation | `BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md` | `6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb` |
| Positive one-cell complete-kernel control | `COMPLETE_ONE_CELL_CTP_KERNEL_GATE_V001.md` | `e30f2e631204df2416b9aa38e55c2710db1d676749fcd2fbdb6604388f3ea391` |
| Positive one-line closure classification | `STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md` | `e12fffcc0f94d6896bc5607898db6b3a1ea343aeaf557b1f6f70e58db061fab6` |
| Four-axis scope restriction | `STAGE8_T7_FOUR_AXIS_SCOPE_EXTENSION_ADJUDICATION_RESULT_V001.md` | `94d035231df7908f9fdde62b1a6aae7d791fa74c8f32c1a95b2511d346fd54c2` |

The executor must verify each bundle's internal entries as well as the
bundle hash. Any mismatch blocks execution. No authority may be replaced by
an unhashed equivalent.

## O1 - Primitive parent and record resolution

For each finite Galerkin causal parent `K` and external compact connection
history `A`, let

```text
W_K[A]: H_S tensor H_R -> H_S tensor H_R
```

be the unique unitary propagator derived from the sealed parent. Let

```text
i_r: H_S -> H_S tensor H_R
```

be the single history-independent isometric injection of the predeclared
tensor product of ready record states.

Let the final record algebra carry the history-independent orthogonal PVM

```text
P_xi=P_xi^dagger=P_xi^2;
P_xi P_zeta=0, xi!=zeta;
sum_(all xi) P_xi=I_R.
```

The index set contains every final record sector, including ready,
intermediate, and unresolved sectors. Let `C` be the predeclared subset of
completed public alternatives and define

```text
Q_comp=sum_(xi in C) P_xi.
```

In the finite regression:

```text
H_R=(C^3) tensor (C^3);
xi in {0,1,2}^2;
P_xi=|xi><xi|;
C={(1,1)}.
```

Thus all nine final qutrit outcomes are retained, while `11` is separately
reported as the completed two-record sector. No POVM or post hoc instrument
choice is admitted by this gate. A later POVM extension would require its
own sealed instrument theorem.

## O2 - Forced Stinespring map and record-resolved family

The object forced directly by the parent and ready injection is the
Stinespring isometry

```text
V_K[A]=W_K[A] i_r:H_S->H_S tensor H_R.
```

For each projection choose an orthonormal basis of its range,

```text
P_xi=sum_mu |xi,mu><xi,mu|.
```

The PVM resolves the Stinespring map into the complete operator family

```text
M_(xi,mu)[A]=(I_S tensor <xi,mu|)V_K[A] in End(H_S).
```

The primary primitive output is the pair `(V_K,{P_xi})`; the Kraus family
and the kernels in O3 are derived from it. No claim is made that one kernel
is the unique possible summary of the instrument.

Each `M_(xi,mu)` is not assumed to be scalar, proportional to the identity,
invertible, or the second quantization of one contraction.

The executor must reconstruct the sealed finite-parent witness and verify
that its completed `11` member is non-scalar. Reproducing that negative
witness is a required type check, not a failed response calculation.

## O3 - Full and completed-sector relative-history kernels

For two histories define the full-record kernel

```text
R_all,K[A_+,A_-]
 =sum_(all xi,mu) M_(xi,mu)[A_-]^dagger M_(xi,mu)[A_+]
 =i_r^dagger W_K[A_-]^dagger W_K[A_+] i_r.
```

The equality of the two forms must be proved from completeness of the
record resolution and checked independently in the finite-parent
execution.

Separately define the completed-sector kernel

```text
R_comp,K[A_+,A_-]
 =sum_(xi in C,mu) M_(xi,mu)[A_-]^dagger M_(xi,mu)[A_+]
 =i_r^dagger W_K[A_-]^dagger
    (I_S tensor Q_comp)
   W_K[A_+] i_r.
```

The kernels are derived summaries of the forced Stinespring/PVM response
bundle. This gate does not select either kernel as a scalar physical action.
The complete-`Q_spec` CTP authority uses the all-outcome identity; that
downstream binding is not made until the state is separately hash-pinned.

Neither kernel applies a source state. They are therefore distinct from:

```text
a postselected record amplitude;
an inclusive probability;
a finite normalized source trace;
a determinant;
a final source ray or covector;
and the complete-Q_spec scalar CTP functional.
```

## O4 - Exact structural identities

The finite theorem must prove:

```text
R_all,K[A,A]=I_S;
R_all,K[A_+,A_-]^dagger=R_all,K[A_-,A_+];
||R_all,K[A_+,A_-]||<=1;

R_comp,K[A,A]>=0;
R_comp,K[A,A]<=I_S;
R_comp,K[A_+,A_-]^dagger=R_comp,K[A_-,A_+];
||R_comp,K[A_+,A_-]||<=1.
```

Passive source-basis covariance and gauge covariance are separate claims.
For a passive source basis change `G_S`, conjugate the parent and transform
the ready injection functorially. Then:

```text
R_all,K^G=G_S R_all,K G_S^dagger;
R_comp,K^G=G_S R_comp,K G_S^dagger.
```

The finite executor verifies this passive covariance identity.

For a future simultaneous gauge transformation on both histories, the
required endpoint
intertwiners

```text
W_K[A^g]=(G_T tensor G_R,T) W_K[A]
          (G_0 tensor G_R,0)^dagger;
i_r^g=(G_0 tensor G_R,0)i_r G_0^dagger;
P_xi^g=G_R,T P_(pi_g(xi)) G_R,T^dagger,
```

where `pi_g` preserves the complete index set and the completed subset.
Only after a separately sealed successor derives these relations may gauge
covariance of both kernels be reported, with conjugation by `G_0`.

Future disjoint monoidality is restricted to genuinely independent parent systems
with orthogonal source supports, no shared source incidence or interaction,
factorized histories/PVMs/ready injections, and the canonical graded-Fock
identification. Because the response kernels are even:

```text
R_all,(K1 disjoint K2)=R_all,K1 tensor R_all,K2.
```

No factorization is claimed for disjoint cell subsets that still share the
global source carrier. Gauge covariance and graded monoidality are successor
obligations and are not pass conditions of this finite gate.

## O5 - Operator Duhamel response

On the finite Galerkin parent, let `A_s=A+s a`. The map
`s -> H_K[A_s](t)` is norm-`C^1`; let

```text
J_a(t)=d H_K[A_s](t)/ds |_(s=0)
```

be its bounded, norm-integrable derivative. The ready injection and final
PVM are frozen history-independent boundary data in this gate. If either
varies with `A`, its derivative must be added and this specification blocks.

For `Q` equal to either `I_R` or `Q_comp`, write

```text
R_Q[A_+,A_-]
 =i_r^dagger W_K[A_-]^dagger (I_S tensor Q) W_K[A_+] i_r.
```

The first-history variation is

```text
delta_+ R_Q[A_+,A_-;a]
 =-i i_r^dagger W_K[A_-]^dagger
    (I_S tensor Q)
    integral_0^T
      W_K[A_+](T,t) J_a(t) W_K[A_+](t,0) dt
    i_r.
```

The second-history variation is the adjoint-exchanged companion:

```text
delta_- R_Q[A_+,A_-;a]
 =[delta_+ R_Q[A_-,A_+;a]]^dagger.
```

The formula follows exactly from finite-dimensional Duhamel
differentiability. The numerical execution verifies the discretized
propagator derivative by an independently accumulated Fréchet/product-rule
path and central finite differences. Numerical agreement verifies the
implementation only; it is not the proof of the identity and does not prove
the continuum Hessian or an intensive limit.

## O6 - Route-1 special-case consistency falsifier

This gate may not retire, weaken, or declare passed the primitive scalar
Route 1. The following special-case consistency falsifier is frozen before
execution.

On the exact one-cell comparator:

```text
|+>=(|0>+|1>)/sqrt(2);
|->=(|0>-|1>)/sqrt(2);
U(theta)=diag(1,exp(i theta));

A_+(theta)=<+|U(theta)|+>;
A_-(theta)=<-|U(theta)|+>.
```

Route 1 retains the complex completed component `A_+`. Route 2 must preserve
that component and satisfy:

```text
R_comp(theta_+,theta_-)
 =A_+(theta_-)^* A_+(theta_+);

R_all(theta_+,theta_-)
 =A_+(theta_-)^* A_+(theta_+)
  +A_-(theta_-)^* A_-(theta_+)
 =[1+exp(i(theta_+-theta_-))]/2.
```

The frozen comparison pairs are:

```text
(theta_+,theta_-)=(7/100,-11/100);
(theta_+,theta_-)=(13/100,4/100).
```

A mismatch in either component is
`ROUTE1_SPECIAL_CASE_CONSISTENCY_FALSIFIER_FAILED`
and blocks Route 2. The all-outcome sum may not be substituted for the
Route-1 completed component. Agreement is only a consistency control and
cannot select a source state, physical scalar functional, or response
coefficient.

This is a mandatory architecture special-case falsifier: Route 2 must reduce
to the already sealed Route-1/complete-outcome comparator when its carrier is
the comparator's one-dimensional source line. It is not evidence that the
actual finite parent occupies that special case.

For the actual finite Lorentzian parent, the sealed result has not derived
the one-dimensional root-to-endpoint restriction. This control therefore
does not claim that the actual parent has passed Route 1. Any future claim
of a common physical domain must prove the line restriction before using
this control as positive support.

## O7 - Execution obligations

The finite regression is frozen as follows:

```text
source sites                  = 3;
Dirac spin dimension          = 4;
record factors                = 2;
record dimension per factor   = 3;
midpoint steps per pulse      = 96;
integrated write action       = pi/sqrt(2);
full final PVM                = {|xi><xi|:xi in {0,1,2}^2};
completed subset              = {(1,1)};

D_theta[j,j+1 mod 3] = (1/2) exp(i theta/3);
D_theta[j,j-1 mod 3] =-(1/2) exp(-i theta/3);
h_source(theta)=-i D_theta tensor alpha_x;

history pairs = {(0,0),(7/100,-11/100),(13/100,4/100)};

G_S=diag(1,exp(i pi/7),exp(-i pi/5)) tensor I_4;

Duhamel plus-family           = theta_+(s)=s, theta_-=0;
Duhamel minus-family          = theta_+=0, theta_-(s)=s;
dD/dtheta[j,j+1 mod 3] at 0  = i/6;
dD/dtheta[j,j-1 mod 3] at 0  = i/6;
dh_source/dtheta at 0         =-i (dD/dtheta) tensor alpha_x;
J_a(t)                        =dh_source/dtheta tensor I_R;
central-difference epsilons   = {2^-8,2^-9,2^-10};
matrix arithmetic             = IEEE-754 binary64 / complex128.
```

The structural tolerance is `1e-10` in operator 2-norm unless a stricter
exact Boolean is stated. The completed `11` scalar-distance and Frobenius
norm must reproduce the sealed witness within `1e-10`. The finest Duhamel
relative error must be at most `2e-5`, decrease strictly across the three
epsilons, and each halving after the first must reduce the error by a factor
of at least `2`. This requirement applies separately to the plus and minus
derivatives of both `Q=I_R` and `Q=Q_comp`. For each derivative:

```text
relative_error
 =||D_central-D_Duhamel||_2 / ||D_Duhamel||_2.
```

Any zero Duhamel derivative norm blocks that comparison. The plus derivative
is accumulated directly by the product rule. The minus derivative is
accumulated independently through the differentiated adjoint branch and
must also satisfy the exact adjoint-exchange identity.

The executor must:

1. hash-verify every frozen authority and this sealed specification;
2. reconstruct the actual finite Lorentzian parent rather than an ideal
   projector chain;
3. construct every record-output Kraus operator, including every rank
   component;
4. compute both `R_all,K` and `R_comp,K` by the Kraus sum and by direct
   unitary compression;
5. verify the finite O4 identities for the frozen histories;
6. verify the frozen passive source-basis covariance witness;
7. verify the O5 derivative by two independently coded paths;
8. reproduce the non-scalar completed-record witness;
9. execute the frozen Route-1 control without using it to alter the
   operator construction;
10. emit exact-theorem fields separately from numerical-regression fields,
   including every tolerance, residual, and decision;
11. read only this specification and the frozen authority allowlist;
12. emit an atomic `BLOCKED` result on an authority mismatch, startup
   exception, or failed check; and
13. attest that no coupling or alpha target was read.

The independent verifier must recompute the decisive identities without
importing the executor as a module.

## Verdict rule

Return

```text
FINITE_PRIMITIVE_OPERATOR_RESPONSE_BUNDLE_DERIVED
```

only if O1-O7 pass. Otherwise return

```text
FINITE_PRIMITIVE_OPERATOR_RESPONSE_BUNDLE_BLOCKED
```

Passing derives only the finite-Galerkin Stinespring/PVM response bundle,
its full/completed relative kernels, and its finite Duhamel tangent. It does
not derive a primitive scalar amplitude, a continuum response, or universal
arbitrary-history closure.

## Protected status

```text
finite_primitive_operator_response_bundle_derived = false
finite_primitive_operator_Duhamel_tangent_derived = false
primitive_source_scalarization_derived = false
complete_Qspec_state_hash_pinned_for_route2 = false
route1_special_case_consistency_falsifier_frozen = true
route1_special_case_consistency_falsifier_passed = false
actual_parent_route1_line_restriction_derived = false
finite_primitive_operator_gauge_covariance_derived = false
finite_primitive_operator_graded_monoidality_derived = false
stage8_route2_architecture_amended = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
