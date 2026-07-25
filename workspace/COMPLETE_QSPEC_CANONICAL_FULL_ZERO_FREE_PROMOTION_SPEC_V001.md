# Complete-Qspec Canonical Full Zero-Free Promotion Spec v001

Date: 2026-07-25

## Purpose

Decide whether the exact spin-2 support bridge and the canonical physical
transfer certificate prove a volume-uniform zero-free disk and a uniform
thermodynamic logarithm for the **full completed-record amplitude** of the
frozen period-two regulator.

This is a fresh composition gate. It does not inherit the old
SVD-supported transfer, a polar-retraction factor, a binary64 leakage
estimate, or any prior PASS boolean. It must recompute every
verdict-bearing scalar inequality with outward-rounded Arb arithmetic.

No coupling or alpha target may be read or used.

## Frozen authorities

```text
b92e69082d297b38700abcc9750e3b70899714133c290538a03885ebb90079c0  COMPLETE_QSPEC_EXACT_SPIN2_SUPPORT_BRIDGE_SPEC_V001.md
093585374cc3cc1aafb4e500e7de032cec81809b6ee30800cc763b3c1d53fa3e  stage8_execution/work/QSPEC_exact_spin2_support_bridge_v001.json
6a49a75669e61f74b2d1a6904c7bc1a4bb172842f4b01b84456c4cee65334676  COMPLETE_QSPEC_EXACT_SPIN2_SUPPORT_BRIDGE_RESULT_V001.md
e0b477ac3fa2a8cdb48523465739d695e46076c141356229eed249789e26fdf2  COMPLETE_QSPEC_GAUSSIAN_CELL_REDUCTION_LEMMA_V001.md
80c21c579518bb28878b0468615e3d03a02654356964074a50e3684820f43f06  COMPLETE_QSPEC_CANONICAL_SPIN2_TRANSFER_BALL_CERTIFICATE_SPEC_V001.md
00da930b54722791552434252a9cbe6b26a43494d4f7d78eae365bb7938481ce  scripts/certify_complete_qspec_canonical_spin2_transfer_v001.py
46dd8f18dc7e9bfcdda7b90278f8cc71bd1e80aa157c29ba39433057d74be807  stage8_execution/work/QSPEC_canonical_spin2_transfer_ball_certificate_v001.json
12dc40274aa431e08245573963cf2f47de6f7ed4aa9803ae38b71539f538d261  COMPLETE_QSPEC_CANONICAL_SPIN2_TRANSFER_BALL_CERTIFICATE_RESULT_V001.md
54c972914b180d694517ed7598ac3344fd4dde3aa953d139a7a1572ddb281690  COMPLETE_QSPEC_PERIODIC_UNIFORM_ZERO_FREE_THEOREM_SPEC_V001.md
40e5fdac17bd61616b34fcd401a0019b8889e0df38aa0d0b06bd4aec2b1e9e59  COMPLETE_QSPEC_PERIODIC_REDUCED_TO_FULL_BRIDGE_CORRECTION_V001.md
83a59120eb09e4d058602234d89aacfe6aeedaa792d4983f3ae8e3389f6efcf2  /Users/bgm/MB Work/alpha_supervision/OVERNIGHT_PROOF_ADJUDICATION_RETURN_V001.md
```

Every local authority that has a seal must pass its sidecar seal check.
Any missing file, hash mismatch, or seal mismatch is `BLOCKED`.

## C0: exact physical amplitude representation

Let `S` be the exact rank-five spin-2 sector and let `Q_S` be its exact
isometry into the full 70-dimensional four-fermion source carrier. The
sealed bridge proves, for every finite volume and every admissible
plus-history connection-source assignment,

```text
Z_N^full[A_+,0]
 = Z_N^(left full x right S)[A_+,0].
```

The right zero-history evolution reduces exactly on `S`; there is no
finite-precision leakage term and no volume-dependent bridge error.

For the homogeneous source `z`, define the canonical physical transfer
`T(z)` on the row-major operator carrier

```text
Hom(S,left full) ~= C^(70 x 5) ~= C^350
```

using the unretracted Gaussian cell construction, all three completed
record outcomes per cell, and all nine chronological outcomes per
period-two supercell. Then

```text
Z_N^full(z)=l T(z)^N x
```

for every finite `N`, where `l` is the physical trace row and `x` is the
incoming pure-state operator.

This exact representation, not a reduced numerical approximation, carries
the promotion.

## C1: canonical zero-source anchor

Use only the certified canonical `T0=T(0)`. Put

```text
P=|t><t|/<t,t>,
Q=I-P,
R0=Q T0 Q,
A=P+R0,
```

where `t` is the column adjoint of the trace row. The exact physical
identities are

```text
l T0=l,
l x=1,
||l||_2=sqrt(5),
||x||_2=1,
l Q=0.
```

The canonical ball certificate supplies

```text
||R0||_2<r,                 r=203/250=0.812;
||T0-A||_2<delta0,          delta0=1/10^10.
```

The actual enclosed anchor defect is much smaller than `delta0`, but the
gate must use the preregistered ceiling `delta0`. Orthogonality gives
`||A||_2=1`, and

```text
l A^N x=l x=1
```

for every integer `N>=1`.

## C2: analytic physical-transfer perturbation

Freeze the closed complex disk

```text
|z|<=rho,                   rho=1/500.
```

The plus-history connection is the holomorphic family

```text
[D(z)]_(k,k+1)= exp(i z/3)/2,
[D(z)]_(k,k-1)=-exp(-i z/3)/2
```

on the three-site ring. The minus history remains at the exact zero
reference. The four-particle lift of the active Fourier-sector bound gives

```text
L_free
 =(2/3)[1+(2 rho/3) exp(rho/3)],

delta_free=L_free rho.
```

There are two chronological cells per supercell. Duhamel comparison of
their unretracted exact Gaussian evolutions gives

```text
||V_pair(z)-V_pair(0)||_2
 <=exp(2 delta_free)-1.
```

The completed-record environment has nine outcomes. The
Hilbert-Schmidt partial-trace bound therefore gives

```text
epsilon
 =3[exp(2 delta_free)-1],

||T(z)-T0||_2<=epsilon.
```

Consequently,

```text
||T(z)-A||_2<=eta,
eta=epsilon+delta0.
```

The executor must recompute `L_free`, `delta_free`, `epsilon`, and `eta`
with outward rounding. A sampled transfer norm may be emitted only as a
negative control and cannot carry the verdict.

The exact cell isometry factor is `1`. The former numerical factor
`1+1e-11` and every generic polar correction are forbidden.

## C3: explicit invariant-graph contraction

Relative to `P+Q`, write

```text
T(z)=[a(z) b(z); c(z) D(z)].
```

The perturbation bound implies

```text
|a-1|<=eta,
||b||<=eta,
||c||<=eta,
||D||<=r+eta.
```

Freeze

```text
X=1/20,
d=1-eta(1+X),
n=eta+(r+eta)X.
```

For the right graph transform

```text
G(u)=(c+D u)/(a+b u)
```

on `||u||<=X`, and for the adjoint left graph transform, prove with
outward-rounded bounds

```text
d>0,
n/d<X,
L_G=(r+eta)/d + eta*n/d^2 <1.
```

These inequalities give unique analytic right and left invariant graph
lines throughout the disk. Their normalized rank-one spectral projector
`Pi(z)` obeys

```text
||Pi(z)-P||<=delta_P,
delta_P=(2X+2X^2)/(1-X^2).
```

The leading eigenvalue `lambda(z)` and stable block obey

```text
|lambda(z)|>=d,
B<=r+eta+eta X,
kappa=(1+X)/(1-X),
||T(z)^N[I-Pi(z)]||<=kappa B^N.
```

The proof must not charge a similarity factor once per cell.

## C4: finite-volume nonvanishing

Define

```text
coefficient_min
 =1-sqrt(5) delta_P.
```

Require `coefficient_min>0`.

For every `1<=N<=6`, use the telescoping identity around `A` to certify

```text
|Z_N^full(z)-1|
 <=sqrt(5) N eta (1+eta)^(N-1)
 <1.
```

These six inequalities must be recomputed independently. No homogeneous
power sampled at selected values of `z` may replace them.

## C5: all larger volumes

Define

```text
q=B/d,
prefactor=sqrt(5) kappa/coefficient_min.
```

Require

```text
q<1,
prefactor q^7<1.
```

Then for every integer `N>=7`,

```text
|stable remainder|/|leading contribution|
 <=prefactor q^N
 <=prefactor q^7
 <1.
```

Together with C4, this proves

```text
Z_N^full(z)!=0
```

for every integer `N>=1` and every `|z|<=1/500`.

## C6: thermodynamic logarithm

The disk is simply connected, `Z_N^full(0)=1`, and C3-C5 give the uniform
decomposition

```text
Z_N^full(z)
 =c(z) lambda(z)^N [1+O(q^N)],
|c(z)|>=coefficient_min>0.
```

Fix logarithm branches continuously from `z=0`. The executor's scalar
certificate, together with the analytic graph theorem, must establish

```text
lim_(N->infinity) (1/N) Log Z_N^full(z)
 =Log lambda(z)
```

uniformly on the disk.

This is a homogeneous periodic thermodynamic logarithm. It is not yet an
explicit connected-cluster expansion or an absolute cumulant majorant.

## Execution discipline

The executor must:

1. run as `python3 -I -S`;
2. verify this sealed spec, all frozen authority hashes, all available
   local sidecar seals, and the complete pinned `python-flint` wheel
   record;
3. verify the exact-bridge and canonical-transfer machine verdicts and
   every prerequisite boolean used here;
4. recompute every C2-C5 scalar using at least 192-bit Arb arithmetic;
5. emit both interval values and individual pass booleans;
6. audit all loaded Flint module origins immediately before verdict
   assignment;
7. attest that no coupling or alpha target was read.

No threshold may be widened or formula changed after execution. Any
failure is `BLOCKED`; there is no conditional PASS.

## Pass rule and scope

Only if C0-C6 and every execution-discipline obligation pass, return

```text
CANONICAL_FULL_PERIODIC_ZERO_FREE_AND_LOG_DENSITY_PROVED
```

and set

```text
canonical_full_periodic_zero_free_neighborhood_proved=true
full_completed_record_amplitude_zero_free_for_all_volumes=true
canonical_full_periodic_thermodynamic_log_density_proved=true
full_completed_record_amplitude_thermodynamic_log_density_proved=true
```

Even on PASS:

```text
frozen_periodic_local_source_polydisc_proved=false
physical_continuum_local_source_addressability_derived=false
periodic_connected_linked_cluster_density_proved=false
connected_cumulant_absolute_majorant_proved=false
all_stage8_regulators_zero_free_proved=false
all_connected_cellulations_linked_cluster_proved=false
kappa_record_computed=false
physical_Thomson_stiffness_computed=false
coupling_evaluation_authorized=false
alpha_computed=false
proof_authorized=false
```
