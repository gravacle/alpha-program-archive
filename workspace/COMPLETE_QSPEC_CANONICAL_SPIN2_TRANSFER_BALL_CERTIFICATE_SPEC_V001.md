# Complete-Qspec Canonical Spin-2 Transfer Ball Certificate Spec v001

Date: 2026-07-25

## Purpose

Construct and certify the physical zero-history

```text
left full x right exact-spin-2
```

periodic transfer. This is the required E6 successor to the exact support
bridge. It replaces the old binary64 SVD support and generic polar
retraction with the exact invariant support and the unretracted unitary
cell.

No response coefficient, coupling, or alpha value may be read or used.

## Frozen authorities

```text
b92e69082d297b38700abcc9750e3b70899714133c290538a03885ebb90079c0  COMPLETE_QSPEC_EXACT_SPIN2_SUPPORT_BRIDGE_SPEC_V001.md
ad3286ee2961fc7569db7ed6572e1cb4bdc5ff5415226cd2b5b5e56625b2ab1e  COMPLETE_QSPEC_EXTERIOR_FRAME_AND_STINESPRING_LEMMAS_V001.md
5aeaf5f88f95f62b188d424e695ab3bc47c320a11fe89f5ef70497a0cef7f052  scripts/prove_complete_qspec_exact_spin2_support_bridge_v001.py
093585374cc3cc1aafb4e500e7de032cec81809b6ee30800cc763b3c1d53fa3e  stage8_execution/work/QSPEC_exact_spin2_support_bridge_v001.json
6a49a75669e61f74b2d1a6904c7bc1a4bb172842f4b01b84456c4cee65334676  COMPLETE_QSPEC_EXACT_SPIN2_SUPPORT_BRIDGE_RESULT_V001.md
e0b477ac3fa2a8cdb48523465739d695e46076c141356229eed249789e26fdf2  COMPLETE_QSPEC_GAUSSIAN_CELL_REDUCTION_LEMMA_V001.md
83a59120eb09e4d058602234d89aacfe6aeedaa792d4983f3ae8e3389f6efcf2  /Users/bgm/MB Work/alpha_supervision/OVERNIGHT_PROOF_ADJUDICATION_RETURN_V001.md
54c972914b180d694517ed7598ac3344fd4dde3aa953d139a7a1572ddb281690  COMPLETE_QSPEC_PERIODIC_UNIFORM_ZERO_FREE_THEOREM_SPEC_V001.md
ada56f525f4a5a9708545e29e62e7e5f0e2dd762d37f168429284194c7babd95  COMPLETE_QSPEC_ZERO_TRANSFER_DYADIC_BALL_CERTIFICATE_SPEC_V001.md
```

The executor must verify all hashes and all local seals before loading the
model.

## C0: exact carrier and support

Reconstruct the exact parent and exact Lanczos support from the sealed
spin-2 executor. The executor must not load a floating eigensystem or SVD.
It must independently recheck:

```text
Q^dagger Q=I_5;
(I-QQ^dagger) H_a Q=0, a=0,1,2;
Q^dagger H0 Q=sqrt(3) diag(-2,-1,0,1,2);
Q^dagger H1 Q=Q^dagger H2 Q=(4/3)J_x^(j=2).
```

## C1: Gaussian cell identity

For the exterior-power representation `Gamma_4`, derive and use

```text
exp[dGamma(b)] = Gamma_4(exp b).
```

The proof must come from differentiating
`Gamma_4(exp(t b))` and uniqueness of the finite-dimensional linear ODE.
It may not be introduced as a numerical shortcut.

For the exact one-body interactions `b_1,b_2`, verify before propagation:

```text
b_a^dagger=b_a;
(b_a^2-I)(b_a^2-I/9)=0;
spec(b_a)={-1,-1/3,1/3,1};
rank P_(a,lambda)=2 for each lambda.
```

Construct the projectors by the target-independent Lagrange formula

```text
P_(a,lambda)
 =product_(mu != lambda) (b_a-mu I)/(lambda-mu).
```

Verify exactly:

```text
P_(a,lambda)^dagger=P_(a,lambda);
P_(a,lambda)P_(a,mu)=delta_(lambda,mu)P_(a,lambda);
sum_lambda P_(a,lambda)=I;
sum_lambda lambda P_(a,lambda)=b_a.
```

For the record generator `R`, verify:

```text
R^dagger=R;
R(R^2-2I)=0;
spec(R)={-sqrt(2),0,sqrt(2)};
rank Q_mu=1.
```

Construct its projectors by the same formula.
Verify exactly:

```text
Q_mu^dagger=Q_mu;
Q_mu Q_nu=delta_(mu,nu)Q_mu;
sum_mu Q_mu=I_R;
sum_mu mu Q_mu=R.
```

## C2: exact conditional-record reduction

The record generator is fixed throughout one cell and the free factor acts
only on the source. Therefore the joint cell is block diagonal in the
record spectral basis. For each record eigenvalue `mu`, construct the
source evolution with the frozen parameters

```text
STEPS=96;
action=pi/sqrt(2);
diamond_weight(t)=32 min(t,1-t)^3;
```

and midpoint times `(j+1/2)/STEPS`:

```text
F_half=Gamma_4(exp[-i h0/(2 STEPS)]);

U_(a,mu)
 =ordered_product_j [
    F_half
    Gamma_4(exp[-i action diamond_weight(t_j) mu b_a/STEPS])
    F_half
  ].
```

Chronological order is fixed: the `j=0` factor acts first and is the
rightmost factor in the final matrix product.

Recover the unretracted Kraus operators from the exact record projectors:

```text
K_(a,q)
 =sum_mu <q|Q_mu|0_R> U_(a,mu).
```

The record ready state and outcome basis are pinned to the frozen parent:

```text
|0_R>=(1,0,0)^T;
|q> in {(1,0,0)^T,(0,1,0)^T,(0,0,1)^T}.
```

Verify their exact normalization and completeness before propagation.

Do this once on the full `70`-dimensional source carrier. On the exact
spin-2 support, construct the same conditional evolution directly from

```text
H0_S=Q_S^dagger H0 Q_S;
Ha_S=Q_S^dagger Ha Q_S
```

using rigorous `5 x 5` matrix exponentials (or their verified spectral
projectors), with exactly the same times and ordering. Verify that the
support cell is the exact compression of the full cell.

The two-cell chronological composite is fixed:

```text
K_(q1,q2)=K_(2,q2) K_(1,q1).
```

No `G^(-1/2)`, SVD, QR support finder, or generic polar retraction is
admissible.

## C3: rigorous arithmetic

All algebraic inputs must enter as exact integers, rationals, `i`, and
certified square-root balls. All transcendental factors and all matrix
operations must be enclosed with `python-flint` complex-ball arithmetic at
no less than `192` bits.

The executor must verify the complete installed wheel record and every
loaded `flint` module origin before assigning any verdict.

The old binary64 transfer may be compared only as a non-verdict diagnostic.
No binary64 entry may be treated as the exact physical transfer.

## C4: transfer and anchor

Chronologically compose the two frozen cells and construct

```text
T0=sum_(q1=0)^2 sum_(q2=0)^2
     K_(q1,q2)^(left full)
     tensor conjugate(K_(q1,q2)^(right S)),
```

with dimension `350 x 350`.

The vectorization convention is frozen as row-major:

```text
[vec_r(X)]_(5 i+j)=X_(i,j),
0<=i<70, 0<=j<5.
```

Thus, without an implicit transpose or factor swap,

```text
vec_r(A X B^dagger)
 =[A tensor conjugate(B)] vec_r(X).
```

Construct the exact-basis start and trace vectors:

```text
start=vec(rho_in Q_S);
trace=vec(Q_S)^dagger,
```

where `Q_S` is the exact `70 x 5` spin-2 basis. First derive algebraically,
with

```text
|psi_0>=|0,1,2,3>;
rho_in=|psi_0><psi_0|;
P_S=Q_S Q_S^dagger,
```

and verify exactly:

```text
<psi_0|psi_0>=1;
rho_in=P_S rho_in P_S;
Tr(rho_in)=1;
Q_S^dagger Q_S=I_5.
```

Then derive algebraically, from exact support reduction and Stinespring
completeness:

```text
trace start=1;
trace T0=trace;
```

The ball calculation must independently enclose the corresponding
residuals, but a ball containing zero is not by itself accepted as an
equality proof.

With

```text
P=|trace_column><trace_column|/<trace_column|trace_column>,
Q0=I-P,
R0=Q0 T0 Q0,
A0=P+R0,
```

prove by a ball-certified singular-value or positive-congruence argument:

```text
||R0||_2 < 0.812.
||T0-A0||_2 < 1e-10.
```

Both thresholds are inherited from the already sealed zero-free theorem
and are fixed before this computation.

The norm proof is fail-closed and fixed as follows:

1. use the midpoint of the ball matrix only to compute an approximate
   eigenvector preconditioner `V` for
   `H_mid=0.812^2 I-R0_mid^dagger R0_mid`;
2. convert every binary64 entry of `V` to its exact dyadic ball;
3. prove `V^dagger V>0` by interval Gershgorin with a strictly positive
   reported lower margin;
4. prove

   ```text
   0.812^2 V^dagger V-(R0 V)^dagger(R0 V)>0
   ```

   by interval Gershgorin with a strictly positive reported lower margin.

Only the two interval positivity certificates carry the norm verdict.
The midpoint eigensystem is a non-authoritative preconditioner. Failure to
obtain either positive margin returns `BLOCKED`; an interval or floating
SVD is not an admissible substitute.

For the anchor defect, compute outward-rounded `1`- and infinity-norm
upper bounds and use

```text
||T0-A0||_2<=sqrt(||T0-A0||_1 ||T0-A0||_infinity).
```

## C5: isometry accounting

The exact Stinespring theorem gives `G=I` for the physical cell. This
successor must itemize the prior factor:

```text
old numerical allowance: 1+1e-11;
canonical exact-cell factor: 1;
inherited polar correction: none.
```

The old factor may not be silently absorbed into `eta`. If a numerical
stabilizer is applied anywhere, this certificate returns `BLOCKED`.

## Pass rule

Only if C0-C5 all pass, return:

```text
CANONICAL_EXACT_SPIN2_TRANSFER_AND_R0_BALL_CERTIFIED
```

and set:

```text
canonical_spin2_transfer_ball_certified=true
exact_physical_R0_norm_below_0_812=true
```

Even on pass:

```text
full_completed_record_amplitude_zero_free_for_all_volumes=false
physical_continuum_local_source_addressability_derived=false
periodic_connected_linked_cluster_density_proved=false
kappa_record_computed=false
physical_Thomson_stiffness_computed=false
coupling_evaluation_authorized=false
alpha_computed=false
proof_authorized=false
```

The all-volume zero-free promotion and the local-source polydisc remain
separate successor gates.
