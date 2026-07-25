# Complete-Qspec Canonical Full Local-Source Polydisc Spec v001

Date: 2026-07-25

## Purpose

Prove or block a volume-uniform zero-free polydisc for independently
addressable connection sources on the canonical full completed-record
amplitude of the frozen period-two regulator:

```text
(z_1,...,z_N),              |z_j|<=1/500.
```

The result must hold for every finite integer volume `N>=1` and every
admissible assignment in the polydisc. It may not infer a multivariable
claim from homogeneous powers.

This specification supersedes the unsealed
`COMPLETE_QSPEC_PERIODIC_LOCAL_SOURCE_POLYDISC_SPEC_V001.md`. No coupling or
alpha target may be read or used.

## Frozen authorities

```text
273e1473a1a8bf0be0467634411cec1b7daeee0c9f24c330fad5d288d191dcbb  COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_AMPLITUDE_RESULT_V001.md
5fc923b9ecca5ee6e63fe8faa50047d72747ebaf09646b14b03affc48a6e84a3  COMPLETE_QSPEC_SEQUENTIAL_TRANSFER_INDUCTION_PROOF_V001.md
ade49876242ffc4ce6c90942f8b63261f3cc1c463103110ff1e2e60fee232e84  COMPLETE_QSPEC_SEQUENTIAL_RELATIVE_HISTORY_TRANSFER_MAP_RESULT_V001.md
24c8c7f5dc5ffa8be553de6a85899e7f0142347b378b0ca97c5252dadb573bb0  COMPLETE_QSPEC_PERIODIC_LOCAL_SOURCE_LIFT_DERIVATION_V001.md
6a49a75669e61f74b2d1a6904c7bc1a4bb172842f4b01b84456c4cee65334676  COMPLETE_QSPEC_EXACT_SPIN2_SUPPORT_BRIDGE_RESULT_V001.md
12dc40274aa431e08245573963cf2f47de6f7ed4aa9803ae38b71539f538d261  COMPLETE_QSPEC_CANONICAL_SPIN2_TRANSFER_BALL_CERTIFICATE_RESULT_V001.md
61d3822f78b1b48c690951e4ffb710ca798ee2b8cbc7986d5c1b6164c7e52e83  COMPLETE_QSPEC_CANONICAL_FULL_ZERO_FREE_PROMOTION_SPEC_V001.md
3cde9448454d95ede29b904a353b72b56f8f21bc746918f794ed527430ac2aef  scripts/certify_complete_qspec_canonical_full_zero_free_v001.py
bf693cea0ad011d4d7fa020cc9f74ead93a9054c967ccd3878438e1312562473  stage8_execution/work/QSPEC_canonical_full_zero_free_promotion_v001.json
083e63e2516e1f319e4dd1edbb17f97d3e58a9eec683739c95310cb1dedb6640  COMPLETE_QSPEC_CANONICAL_FULL_ZERO_FREE_PROMOTION_RESULT_V001.md
a6c2124626701e79a78a40923fe09cd8e9c93bbd2eec741c22344dbe10709c16  COMPLETE_QSPEC_BOUNDARY_ADAPTED_NONAUTONOMOUS_FACTORIZATION_LEMMA_V001.md
```

Every local authority that has a seal must pass its sidecar seal check.
Any missing file, hash mismatch, or seal mismatch is `BLOCKED`.

## L0: exact locally sourced physical amplitude

For supercell `j`, put the plus-history connection source `z_j` on the
same three-site compact loop used by the homogeneous family:

```text
[D(z_j)]_(k,k+1)= exp(i z_j/3)/2,
[D(z_j)]_(k,k-1)=-exp(-i z_j/3)/2.
```

The minus history remains at the exact zero reference. The sealed
sequential induction and local-source lift give

```text
Z_N^full(z_1,...,z_N)
 =l T_N(z_N)...T_1(z_1)x.
```

The exact spin-2 bridge applies independently at each stage because the
right zero-history support is exact and arbitrary left multiplication
preserves the right-support identity. Therefore the displayed transfer
product is the full completed-record amplitude for every finite admissible
assignment, not a reduced approximation.

Real `z_j` are independent compact connection holonomies. Complex `z_j`
are their holomorphic complexification for the zero-free theorem.

## L1: common anchor and per-cell perturbation

Use the same canonical anchor as the sealed homogeneous result:

```text
P=|t><t|/<t,t>,
Q=I-P,
A=P+Q T0 Q,

||Q T0 Q||_2<r,             r=203/250;
||T0-A||_2<delta0,          delta0=1/10^10;

l=sqrt(5) p^dagger,
||x||_2=1,
l x=1.
```

For every individual `|z_j|<=rho`, `rho=1/500`, recompute with
outward-rounded Arb arithmetic:

```text
L_free
 =(2/3)[1+(2 rho/3) exp(rho/3)],

delta_free=L_free rho,
epsilon=3[exp(2 delta_free)-1],
eta=epsilon+delta0.
```

The exact physical cell factor is `1`; no old `1+1e-11` isometry allowance
or polar correction is admissible. The analytic Duhamel and
completed-record bounds give, independently for every cell,

```text
||T_j(z_j)-A||_2<=eta.
```

No sampled matrix norm may carry this obligation.

## L2: boundary-adapted graph hypotheses

Freeze

```text
X=1/20,
d=1-eta(1+X),
n=eta+(r+eta)X,

L_G=(r+eta)/d + eta*n/d^2.
```

Require, with outward-rounded intervals and separate pass booleans:

```text
d>0,
n/d<X,
L_G<1,
1-sqrt(5)X>0.
```

Any failure is `BLOCKED`; no threshold may be widened after execution.

## L3: exact nonautonomous factorization

Apply the sealed boundary-adapted nonautonomous factorization lemma to the
arbitrary ordered sequence

```text
M_j=T_j(z_j).
```

The right recursion starts at the physical incoming anchor `u_0=0`; the
complex-linear dual recursion, with no parameter conjugation, ends at the
physical trace boundary `v_N=0`. The lemma gives exact factors

```text
Z_N^full(z_1,...,z_N)
 =sqrt(5)
  [product_(j=1)^N s_j]
  (p^dagger+v_0)x
```

with

```text
|s_j|>=d,

|sqrt(5)(p^dagger+v_0)x|
 >=1-sqrt(5)X.
```

Therefore

```text
|Z_N^full(z_1,...,z_N)|
 >=[1-sqrt(5)X] d^N
 >0
```

for every finite `N>=1` and every source assignment in the closed
polydisc. The stable component is eliminated exactly by the physical
terminal trace; no finite/large-volume split or sampled source grid is
used.

## L4: holomorphic generator

The open polydisc is simply connected, and

```text
Z_N^full(0,...,0)=1.
```

Fix

```text
F_N(0,...,0)=Log Z_N^full(0,...,0)=0.
```

The zero-free theorem then gives a unique holomorphic branch

```text
F_N(z_1,...,z_N)
 =Log Z_N^full(z_1,...,z_N).
```

Its mixed derivatives are the finite-volume connected cumulants of the
ordered local insertions by the standard moment-cumulant identity.

This establishes the multivariable generator. It does not yet prove an
absolute cumulant majorant, thermodynamic convergence of those cumulants,
or physical continuum local addressability.

## L5: contraction datum for the next gate

The same complex-linear graph maps have Lipschitz constant at most `L_G`.
The executor must emit this certified value and the strict margin
`1-L_G`. This supplies a target-independent decay datum for the next
connected-cumulant-majorant gate.

No connected-density status is promoted here.

## Execution discipline

The executor must:

1. run as `python3 -I -S`;
2. atomically invalidate any prior result before validating inputs;
3. verify this sealed spec, every authority hash, every available local
   sidecar seal, and the complete pinned `python-flint` wheel record;
4. verify the exact-bridge, canonical-transfer, and homogeneous
   full-amplitude prerequisite verdicts and protected statuses;
5. recompute every L1-L2 scalar using at least 192-bit Arb arithmetic;
6. emit each interval, each individual pass boolean, the exact
   factorization status, and the resulting symbolic lower bound;
7. audit all loaded Flint module origins before verdict assignment;
8. attest that no coupling or alpha target was read.

On any exception or failed obligation, the executor must leave an atomic
`BLOCKED` artifact with every protected flag false. There is no conditional
PASS.

## Pass rule and scope

Only if L0-L5 and every execution-discipline obligation pass, return

```text
CANONICAL_FULL_PERIODIC_LOCAL_SOURCE_POLYDISC_PROVED
```

and set

```text
canonical_full_periodic_local_source_polydisc_proved=true
full_completed_record_amplitude_local_source_zero_free_for_all_volumes=true
finite_volume_multivariable_log_generator_proved=true
periodic_boundary_graph_contraction_proved=true
```

Even on PASS:

```text
physical_continuum_local_source_addressability_derived=false
periodic_connected_linked_cluster_density_proved=false
connected_cumulant_absolute_majorant_proved=false
periodic_connected_cumulant_thermodynamic_limit_proved=false
all_stage8_regulators_zero_free_proved=false
all_connected_cellulations_linked_cluster_proved=false
kappa_record_computed=false
physical_Thomson_stiffness_computed=false
coupling_evaluation_authorized=false
alpha_computed=false
proof_authorized=false
```
