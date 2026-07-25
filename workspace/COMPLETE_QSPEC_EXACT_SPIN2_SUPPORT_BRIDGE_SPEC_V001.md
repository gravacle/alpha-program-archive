# Complete-Qspec Exact Spin-2 Support Bridge Spec v001

Date: 2026-07-25

## Purpose

Replace the uncertified binary64 SVD/Krylov support bridge with a
target-independent exact invariant-support derivation from the frozen
three-site ring and Dirac generators.

The gate asks one question:

```text
Does the exact zero-history source-record evolution preserve a
five-dimensional source sector containing the disclosed incoming state?
```

No response coefficient, coupling, or alpha value may be read or used.

## Authorities

```text
1cd9528bc6872a3a28df828a452a165f8672cccc455a64323edab9e0905bf69d  scripts/verify_complete_qspec_periodic_analytic_continuation_v003.py
273e1473a1a8bf0be0467634411cec1b7daeee0c9f24c330fad5d288d191dcbb  COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_AMPLITUDE_RESULT_V001.md
5fc923b9ecca5ee6e63fe8faa50047d72747ebaf09646b14b03affc48a6e84a3  COMPLETE_QSPEC_SEQUENTIAL_TRANSFER_INDUCTION_PROOF_V001.md
40e5fdac17bd61616b34fcd401a0019b8889e0df38aa0d0b06bd4aec2b1e9e59  COMPLETE_QSPEC_PERIODIC_REDUCED_TO_FULL_BRIDGE_CORRECTION_V001.md
83a59120eb09e4d058602234d89aacfe6aeedaa792d4983f3ae8e3389f6efcf2  /Users/bgm/MB Work/alpha_supervision/OVERNIGHT_PROOF_ADJUDICATION_RETURN_V001.md
```

## E0: exact one-body carrier

Work over the exact algebraic field

```text
Q(i,sqrt(2),sqrt(3))
```

which also contains `sqrt(6)`.
Construct, without numerical eigensolvers:

```text
D_0(k,k+1)= 1/2,
D_0(k,k-1)=-1/2
```

on the three-site ring;

```text
alpha_x =
[[0,0,0,1],
 [0,0,1,0],
 [0,1,0,0],
 [1,0,0,0]];

I_BR =
[[0,0,-i,0],
 [0,0,0,-i],
 [i,0,0,0],
 [0,i,0,0]];
```

and

```text
h_0=-i D_0 tensor alpha_x.
```

Use the exact Fourier vectors with `omega=exp(2 pi i/3)` and the exact
`alpha_x` eigenvectors to build an explicit orthonormal basis of the eight
nonzero modes. Verify exactly that the active one-body free generator is

```text
diag(-sqrt(3)/2 I_4, +sqrt(3)/2 I_4).
```

The parent carrier must also be defined without choosing a degenerate
eigenbasis. With `s=sqrt(3)/2`, construct the exact spectral projectors

```text
P_active=(4/3) h_0^2,
P_minus=(P_active-h_0/s)/2,
P_plus =(P_active+h_0/s)/2.
```

Prove:

```text
P_active^2=P_active, rank(P_active)=8;
P_minus^2=P_minus, rank(P_minus)=4;
P_plus^2=P_plus, rank(P_plus)=4;
V_exact V_exact^dagger=P_active;
V_exact,- V_exact,-^dagger=P_minus.
```

This basis-independent projector definition is the frozen physical parent.
The numerical degenerate eigensystem in the prior verifier is an
implementation frame, not an additional physical choice.

For the two frozen masks

```text
M_1=diag(1,1,0),
M_2=diag(0,1,1),
```

construct exactly

```text
b_a=V_active^dagger (M_a tensor I_BR) V_active.
```

For every other orthonormal active frame `V_f`, require the explicit
intertwiner

```text
U=V_exact^dagger V_f,
V_f=V_exact U,
```

and prove the one-particle and exterior-power covariance identities

```text
h_f=U^dagger h_exact U;
b_(a,f)=U^dagger b_(a,exact) U;
dGamma(U^dagger b U)
 =Gamma_4(U)^dagger dGamma(b) Gamma_4(U).
```

For a frame respecting the negative/positive spectral split, prove that the
filled negative sea is carried to `psi_0` up to the determinant phase of the
negative block. Hence the CTP scalar and support dimension are frame
independent. The old binary64 matrix is not declared exact; it is superseded
by the exact-frame numerical successor in E6.

## E1: exact four-fermion lift

On the lexicographically ordered basis of `Lambda^4 C^8`, construct the
number-preserving second-quantized matrices

```text
H_0=dGamma(h_0|active),
H_1=dGamma(b_1),
H_2=dGamma(b_2).
```

The executor must use the complete CAR matrix-element rule

```text
dGamma(b)=sum_(p,q) b_(p,q) a_p^dagger a_q,
```

including the fermionic removal and insertion parity in the lexicographic
occupation basis. It must build the full `70 x 70` matrices before the
spin-2 comparison. The expected spin-2 matrices in E3 may be used only as
comparison outputs, never as inputs to `H_a`, `S`, or `Q`.

Let

```text
psi_0=|0,1,2,3>
```

be the filled negative-energy state. No SVD, rank threshold, floating
projector, or response quantity is admissible.

## E2: cyclic support and exact rank

Define the cyclic span

```text
S=span{psi_0,H_1 psi_0,H_1^2 psi_0,H_1^3 psi_0,H_1^4 psi_0}.
```

Prove exactly:

```text
dim S=5;
H_0 S subset S;
H_1 S subset S;
H_2 S subset S.
```

The execution must emit a nonzero exact `5 x 5` Gram determinant and exact
zero residual matrices for all three invariance tests.

## E3: spin-2 identification

Construct the exact orthonormal Lanczos basis

```text
q_-2,...,q_2
```

from `psi_0` and `H_1`. Verify exactly:

```text
Q^dagger Q=I_5;

Q^dagger H_0 Q
 =sqrt(3) diag(-2,-1,0,1,2);

Q^dagger H_1 Q
 =Q^dagger H_2 Q
 =(4/3) J_x^(j=2),
```

where the nonzero upper/lower off-diagonal entries are

```text
4/3, 2 sqrt(6)/3, 2 sqrt(6)/3, 4/3.
```

Also prove

```text
(I-QQ^dagger) H_a Q=0,  a=0,1,2.
```

These identities, not a numerical rank gap, carry the verdict.

## E4: exact cell and Kraus invariance

The exact, unretracted zero-history cell Hamiltonian is assembled only from

```text
H_0 tensor I_record
```

and

```text
H_a tensor R_record,  a=1 or 2,
```

with scalar time weights. From E2-E3 prove that every factor in the exact
time-ordered product preserves `S tensor H_record`. Therefore:

```text
every exact zero-history cell unitary preserves S tensor H_record;
every exact zero-history Kraus operator maps S into S;
every exact zero-history two-cell composite maps S into S.
```

Exact time-ordered factors are unitary, so the exact stacked Stinespring
map obeys

```text
G=sum_q K_q^dagger K_q=I
```

and its polar factor `G^(-1/2)` is exactly `I`. No polar retraction or
finite-precision leakage estimate may be used in this logical step. E4-E5
concern the exact unretracted parent, not the old repaired binary64 transfer.

## E5: reduced-to-full amplitude equality

The disclosed incoming source state lies in `S`. Put `P=QQ^dagger`. For
every exact minus-history Kraus block, E4 must first give

```text
(I-P) K_q^- P=0.
```

For every operator `X=XP`, prove directly:

```text
sum_q K_q^+ X K_q^(-dagger)
 =
[sum_q K_q^+ X K_q^(-dagger)] P.
```

Starting from `rho_in=rho_in P`, induct over cells and then apply the full
source trace. This must establish:

```text
Z_N^full[A_+,0]
 =Z_N^(left full x right S)[A_+,0]
```

for every finite `N` and every admissible plus-history source assignment.
The equality follows from exact right-history invariance; no accumulated
leak term exists in the exact model.

Here `admissible` has exactly the scope of the sealed sequential theorem:

```text
the same source and fresh-record spaces;
the same ready states and completed outcome closure;
chronological completed-record composition;
identity action on every previously closed record; and
no later interaction with a previously closed record.
```

No broader overlapping-open-record history is included.

## E6: required numerical successor

A pass here does not revive the old binary64 transfer certificate as a
full-amplitude theorem. After this exact gate passes, a successor must:

1. build the canonical `left full x right S` transfer using the exact
   spin-2 basis rather than the SVD support;
2. enclose the analytic matrix construction with ball arithmetic;
3. rerun the anchor, zero-free, and local-source-polydisc certificates;
4. itemize the previously absorbed `(1+1e-11)` isometry factor.

The successor may not apply a generic numerical polar retraction. It must
either enclose the unretracted exact unitary construction directly or first
prove that any numerical stabilizer is block diagonal with respect to
`S direct-sum S^perp` and does not change the exact physical object.

Until that successor passes:

```text
full_completed_record_amplitude_zero_free_for_all_volumes=false
```

## Execution and pass rule

The symbolic executor must verify this sealed spec and every local authority
hash before loading the model. It must use exact symbolic arithmetic for all
E0-E5 verdicts and emit machine-readable forms of every restricted matrix,
Gram determinant, and zero residual.

Only if E0-E5 all pass, return:

```text
EXACT_ZERO_HISTORY_SPIN2_SUPPORT_BRIDGE_DERIVED
```

and set:

```text
exact_zero_history_spin2_support_derived=true
exact_reduced_to_full_finite_amplitude_identity_derived=true
```

Even on pass:

```text
canonical_spin2_transfer_ball_certified=false
full_completed_record_amplitude_zero_free_for_all_volumes=false
physical_continuum_local_source_addressability_derived=false
periodic_connected_linked_cluster_density_proved=false
kappa_record_computed=false
physical_Thomson_stiffness_computed=false
coupling_evaluation_authorized=false
alpha_computed=false
proof_authorized=false
```
