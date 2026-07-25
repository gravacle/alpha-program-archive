# Complete-Qspec Periodic Local-Source Lift Derivation v001

Date: 2026-07-25

## Authorities

```text
5fc923b9ecca5ee6e63fe8faa50047d72747ebaf09646b14b03affc48a6e84a3  COMPLETE_QSPEC_SEQUENTIAL_TRANSFER_INDUCTION_PROOF_V001.md
ade49876242ffc4ce6c90942f8b63261f3cc1c463103110ff1e2e60fee232e84  COMPLETE_QSPEC_SEQUENTIAL_RELATIVE_HISTORY_TRANSFER_MAP_RESULT_V001.md
273e1473a1a8bf0be0467634411cec1b7daeee0c9f24c330fad5d288d191dcbb  COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_AMPLITUDE_RESULT_V001.md
6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb  BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md
506131686e97a27e90fb29d614ed1f74a33ea5ceec941a0805aa6dd7468ae178  COMPLETE_QSPEC_PERIODIC_ZERO_FREE_PROMOTION_RESULT_V001.md
1cd9528bc6872a3a28df828a452a165f8672cccc455a64323edab9e0905bf69d  scripts/verify_complete_qspec_periodic_analytic_continuation_v003.py
f39103452e214c8e0ef29ebeddd884074140a35316c486fadabb12c4b160bf65  stage8_execution/work/QSPEC_periodic_analytic_continuation_verification_v003.json
```

## Statement

Let the frozen sequential regulator contain `N` period-two supercells. Give
supercell `j` its own complex connection source `z_j`, applied to the same
local plus-history handle used by the homogeneous continuation. Keep the
minus history at the repaired zero reference.

Let `T_j(z_j)` be the resulting source-space cross-history transfer map for
that supercell. Fresh records and completed-stage closure give, exactly:

```text
Z_N(z_1,...,z_N)
 = trace [
     T_N(z_N) ... T_2(z_2) T_1(z_1) (rho_in)
   ].
```

This is the complete-Qspec CTP scalar with independently addressable local
sources. It is not a new scalarization.

## Derivation

The sequential induction theorem allows each stage operator `U_j` to differ
from every other stage operator. Its proof uses only:

```text
one shared source;
one fresh ready record at each stage;
identity action on every previously closed record; and
chronological composition.
```

Replacing the homogeneous stage label `z` by the labelled family `z_j`
does not alter any induction step. Applying the theorem to the two-cell
supercell maps yields the displayed ordered product.

The source assignment is local: differentiating in `z_j` changes only
`T_j`. Mixed derivatives preserve the same chronological order as the full
source-record evolution.

## Admissible local connection history

The labelled family is not obtained by assigning unrelated matrix
parameters. The frozen source carrier is a three-site oriented ring. On
supercell `j`, assign the plus-history spatial links

```text
U_j(k -> k+1)=exp(i z_j/3),  k=0,1,2 mod 3,
```

and the inverse phase to the reversed links. For real `z_j`, these are
unitary `U(1)` transports and their oriented loop product is
`exp(i z_j)`. Substitution in the frozen central-difference convention gives
exactly the accepted analytic family:

```text
[D(z_j)]_(k,k+1)= exp(i z_j/3)/2,
[D(z_j)]_(k,k-1)=-exp(-i z_j/3)/2.
```

A finite list `(z_1,...,z_N)` therefore specifies one piecewise-constant
compact connection history on the shared source ring, with one
gauge-invariant loop flux on each chronological supercell. The spatial
gauge is fixed once for the full history; changing one loop flux changes
only that supercell's free source operator. Chronological propagation still
uses the same source Hilbert space and the same fresh-record interactions.

Under a common vertex gauge transformation, every `D(z_j)` is conjugated
and the endpoint conjugations cancel in the complete CTP scalar. Thus the
real labelled family is an admissible gauge-covariant connection history on
the frozen periodic regression regulator. Complex `z_j` are only its
holomorphic complexification for the zero-free and Cauchy estimates; they
are not asserted to be physical nonunitary connections.

This construction does not promote the three-site ring to the physical
continuum carrier. A separate lift to the nested continuum carriers
`Q_n L^2(R^3;C^4)`, preserving local support and gauge covariance as
`Q_n -> I`, remains required before physical continuum local addressability
can be claimed.

## Generating-function normalization

Define:

```text
Z_N^norm(z_1,...,z_N)
 = Z_N(z_1,...,z_N) / Z_N(0,...,0).
```

The numerator and denominator are values of the same complete-Qspec CTP
amplitude, and the accepted periodic zero-free theorem proves that the
denominator is nonzero. The division is therefore a mathematically
authorized global generating-function normalization. It is not itself an
additional physical CTP normalization and is not inherited from the
primitive ratio `a_h(A)/a_h(0)`. No per-cell renormalization, postselection,
stationary state, or determinant is inserted.

This constant division changes neither the zero set nor any positive-order
derivative of the logarithm. The unnormalized `Z_N` remains the exact
complete-Qspec CTP scalar; `Z_N^norm` is only the convenient origin-normalized
generator.

Where a zero-free local-source domain is proved, fix the branch from the
origin and define:

```text
F_N(z_1,...,z_N) = Log Z_N^norm(z_1,...,z_N).
```

Then `F_N(0)=0`, and its labelled derivatives are the connected cumulants
of the ordered local insertions by the standard moment-cumulant identity.
This statement identifies the object; it does not yet prove their spatial
decay or summability.

## Disjoint systems

For tensor-disjoint source-record systems with factorized incoming states,
the complete CTP theorem gives:

```text
Z_(K1 disjoint K2)=Z_K1 Z_K2,
F_(K1 disjoint K2)=F_K1+F_K2.
```

Therefore a mixed cumulant whose insertions lie in genuinely
tensor-disconnected components vanishes exactly.

## Earned status

```text
periodic_real_connection_history_local_addressability_derived = true
periodic_complex_local_source_lift_is_holomorphic_complexification = true
physical_continuum_local_source_addressability_derived = false
unnormalized_local_source_lift_equals_complete_Qspec_CTP_amplitude = true
global_generating_normalization_mathematically_authorized = true
global_generating_normalization_inherited_as_physical_CTP_rule = false
chronological_mixed_derivative_order_fixed = true
tensor_disjoint_factorized_component_mixed_cumulants_vanish = true
volume_uniform_local_source_polydisc_proved = false
periodic_connected_linked_cluster_density_proved = false
all_connected_cellulations_linked_cluster_proved = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
