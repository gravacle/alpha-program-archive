# Full98 Background Quadratic-Jet Continuum Closure Target v001

Status: `PROPOSED_NOT_CLOSED`. The scalar tail shape is known, but the actual
operator-level partial sums and their constants have not yet passed the gate
below.

## Fixed scope

This target concerns derivatives at the adopted record-forming background
`u=0` for one fixed periodic spin structure and one fixed external full98 mode
`L=2`, `M=0`, `q=(+/-1,0)`. It does not assert a nonlinear operator family on
an open neighborhood. Metric variations are represented on the fixed
reference spinor Hilbert space by the already adopted oriented
Bourguignon-Gauduchon identification.

The background source operator is

```text
K0 = A0^dagger A0 + C2_parent,
Gamma(0) = (1/2) Tr E1(K0),
E1(x) = integral_1^infinity exp(-t x) dt/t.
```

Its locked spectrum is reconstructed exactly as

```text
lambda_a = p_t^2 + p_q^2 + lambda_S2(flux,ell)^2 + 1 + C2_parent,
lambda_a >= 1 + p_t^2 + p_q^2 + ell(ell+1).
```

## Source and return windows

Let `S(N_T,N_S)` contain source eigenstates with

```text
|p_t|,|p_q| <= N_T,  ell <= N_S.
```

The return guard is independently defined by

```text
G(N_T,N_S): |p_t|,|p_q| <= N_T+2,  ell <= N_S+4.
```

The source trace is taken only over `S`; `G` is used only to evaluate every
first- and second-insertion path before contraction. No path is discarded
merely because an intermediate return leaves `S`.

## Explicit quadratic-jet partial sums

In the eigenbasis of `K0`, construct from the guarded superconnection jets

```text
K_i  = A0^dagger V_i + V_i^dagger A0,
K_ij = V_i^dagger V_j + V_j^dagger V_i
       + A0^dagger W_ij + W_ij^dagger A0.
```

Define the finite partial sums, rather than an ambiguous compressed nonlinear
functional,

```text
Gamma_N = (1/2) sum_{a in S} E1(lambda_a),

G_i,N = (1/2) sum_{a in S} E1'(lambda_a) (K_i)_aa,

H_ij,N = (1/2) sum_{a in S} E1'(lambda_a) (K_ij)_aa
       + (1/2) sum_{a,b in S} phi(lambda_a,lambda_b)
                    (K_i)_ab (K_j)_ba,
```

where

```text
phi(x,y) = [E1'(x)-E1'(y)]/(x-y), x != y,
phi(x,x) = E1''(x).
```

This is the spectral double-operator-integral kernel written as an explicit
matrix-element sum; it is not ordinary multiplication by a symbolic divided
difference. Equivalently, it is the finite spectral form of the Duhamel
two-insertion integral.

## Complete jets and support certificate

The exact inventory must certify all fields and unordered pairs:

```text
metric: 20 V_i of order <=1,
connection: 72 V_i of order 0,
odd paired return: 6 V_i of order 0,

metric-metric W_ij: 210 order <=1,
metric-connection W_ij: 1440 order 0,
all other W_ij: 3201 exact zeros.
```

For every source level, not merely sampled levels, Fourier addition and the
Wigner-3j triangle rule must emit a symbolic support certificate

```text
V_i:  |Delta p_t|<=1, Delta p_q=0, |Delta ell|<=2,
W_ij: |Delta p_t|<=2, Delta p_q=0, |Delta ell|<=4.
```

Flux-changing spin-c intertwiners and every intermediate return are included.
For the background Hessian, the required second-jet datum is the diagonal
spectral contraction `(K_ij)_aa`.  The neutral metric and neutral
metric-connection direct traces must be evaluated.  A nonzero off-diagonal
`W_ij` may be omitted from this contraction only after a cutoff-independent
selection rule proves `Tr[K0^dagger W_ij]=0`; it must not be relabeled as a
zero operator.  The complete nonzero `W_ij` dispatcher remains mandatory for
the later differentiated-Ward gate, where off-diagonal operator support is
load-bearing.  Class counting alone satisfies neither requirement.

The current pointwise spin-weighted quadrature is certified only for numerical
checkpoints with `N_S<=2`.  No higher angular checkpoint may enter the proof
until the quadrature is independently extended and calibrated.  Angular modes
above that certified window must instead be controlled by exact Wigner
intertwiners and the analytic remainder below.

## Convergence bar

For the background gap `lambda>=1`,

```text
|E1'(x)| <= exp(-x),
|phi(x,y)| <= 2 exp[-min(x,y)].
```

Actual field-specific and pair-specific operator bounds `C_i` and `C_ij`,
including finite-neighbor multiplicities, must be computed from the guarded
operators. Their resulting action, gradient, and Hessian majorants may use the
conservative polynomial powers `p=0,2,4`, but no unit-normalized placeholder is
accepted as a certified remainder.

Convergence is a two-parameter net: for every tolerance there must be
independent `N_T*` and `N_S*` such that the actual partial sums are Cauchy for
all larger `(N_T,N_S)`, including asymmetric cutoff sequences. The analytic
incomplete-gamma inequalities certify the infinite remainder; floating-point
samples are regressions only.

The final gate also requires real `Gamma_N` and `G_N`, symmetric real `H_N`,
the locked `(1,1)` regression, and explicit failure when either cutoff is held
fixed while the other is enlarged.

## What this earns

Passing establishes the continuum background action, gradient, and Hessian for
this fixed external mode and fixed spin structure. It does not yet establish
the nonlinear homogeneous family required for the coupled saddle, the full
differentiated Ward term `D2 Gamma R + D Gamma DR`, an absolute parameter
measure, a Picard-Lefschetz cycle, a field/ghost determinant, threshold flow,
or alpha.
