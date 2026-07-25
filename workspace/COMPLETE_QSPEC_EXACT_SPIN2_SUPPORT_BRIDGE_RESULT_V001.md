# Complete-Qspec Exact Spin-2 Support Bridge Result v001

Date: 2026-07-25

## Verdict

```text
EXACT_ZERO_HISTORY_SPIN2_SUPPORT_BRIDGE_DERIVED
```

This result replaces the uncertified binary64 SVD/Krylov support bridge
identified in the overnight proof-chain adjudication. It proves the
reduced-to-full finite-amplitude identity for the exact frozen parent.
It does not revive the old numerical transfer certificate.

## Sealed inputs

```text
b92e69082d297b38700abcc9750e3b70899714133c290538a03885ebb90079c0  COMPLETE_QSPEC_EXACT_SPIN2_SUPPORT_BRIDGE_SPEC_V001.md
ad3286ee2961fc7569db7ed6572e1cb4bdc5ff5415226cd2b5b5e56625b2ab1e  COMPLETE_QSPEC_EXTERIOR_FRAME_AND_STINESPRING_LEMMAS_V001.md
5aeaf5f88f95f62b188d424e695ab3bc47c320a11fe89f5ef70497a0cef7f052  scripts/prove_complete_qspec_exact_spin2_support_bridge_v001.py
```

The executor verified every frozen authority named in its source before
loading the model and ran under isolated Python mode.

## Machine result

```text
093585374cc3cc1aafb4e500e7de032cec81809b6ee30800cc763b3c1d53fa3e  stage8_execution/work/QSPEC_exact_spin2_support_bridge_v001.json
```

The exact symbolic execution returned:

```text
cyclic Gram determinant = 34359738368/14348907 != 0
cyclic support rank      = 5
Lanczos diagonal         = (0,0,0,0,0)
Lanczos off-diagonal     = (4/3, 2 sqrt(6)/3,
                            2 sqrt(6)/3, 4/3)
H0 invariance residual   = exact zero
H1 invariance residual   = exact zero
H2 invariance residual   = exact zero
```

The resulting restricted generators are exactly

```text
Q^dagger H0 Q = sqrt(3) diag(-2,-1,0,1,2)

Q^dagger H1 Q
 =Q^dagger H2 Q
 =(4/3) J_x^(j=2).
```

The executor constructed the full `70 x 70` CAR lifts before forming the
cyclic space. The expected spin-2 entries were used only after the
target-independent Lanczos construction, as comparison values.

## Derived bridge

The exact source projector `P=Q Q^dagger` is an orthogonal reducing
projector for all three frozen source generators. With the normalized
record ready state, record-basis completeness, and exact Hermiticity:

```text
sum_q K_q^dagger K_q=I;
(I-P) K_q^- P=0.
```

For every `X=XP`,

```text
sum_q K_q^+ X K_q^(-dagger)
 =
[sum_q K_q^+ X K_q^(-dagger)] P.
```

Induction over fresh chronologically closed records therefore proves,
for every finite `N` and every admissible plus-history assignment in the
sealed sequential scope,

```text
Z_N^full[A_+,0]
 =Z_N^(left full x right S)[A_+,0].
```

The binary64 support-invariance residual is no longer load-bearing in
this exact model, and no accumulated leak term appears in this identity.

## Scope and successor

This result establishes the exact finite-stage support bridge only. The
following remain false:

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

The required successor is fixed by E6 of the sealed spec: construct the
canonical `left full x right S` transfer in the exact spin-2 basis,
ball-enclose that construction without a generic polar retraction, and
rerun the anchor, zero-free, and local-source-polydisc certificates. The
previously absorbed `(1+1e-11)` isometry factor must be itemized.

