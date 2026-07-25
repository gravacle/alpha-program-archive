# Stage-8 T7 Relayed-Family Resolution Result v001

Date: 2026-07-24

## Verdict

```text
RELAYED_FAMILY_RESOLVED_IN_DECLARED_BRANCH
```

After the primitive relay is pulled ahead of T7, the existing sealed
authorities fix all five coordinates of `F(S,chi,beta,sigma,I)` inside the
causally sequential, pure-charge, single-incidence branch.

This is a branch-scoped provenance result. It does not derive a physical
connected preparation, a connected amplitude, a thermodynamic response, or
an enlarged-branch uniqueness theorem.

## S - Transport and causal assignment

For the three-cell regression, exact incidence projectors give:

```text
Tr(P_0P_1)=Tr(P_1P_2)=1/4;
Tr(P_0P_2)=0.
```

With the full pinned spin/source normalization:

```text
||[B_0,B_1]||_F^2=||[B_1,B_2]||_F^2=72;
||[B_0,B_2]||_F^2=0;

||U_1U_0-U_0U_1||_F^2
 =||U_2U_1-U_1U_2||_F^2
 =288;
||U_2U_0-U_0U_2||_F^2=0.
```

Every later cell commutes exactly with prior pointer observables. Thus
overlapping cells retain the declared causal order, while disjoint cells may
be swapped without changing the map.

The general step is the standard linear-extension theorem: any two linear
extensions of a finite causal order differ by adjacent swaps of incomparable
elements. In the declared branch, incomparable cells are disjoint and their
operators commute. The resulting finite causal product is consequently
independent of the chosen linear extension.

## chi - Active charged handle

The pinned projection-module derivation fixes:

```text
P_ch=1_(R\{0})(Q),
B_ch=P_ch tensor B_Q,
(a_0,a_+,a_-)=(0,1,1).
```

A rescaling `lambda P_ch tensor B_Q` fails the retraction condition unless
`lambda=1`. A neutral charged write and a second primitive charged line are
outside the declared pure-charge branch.

## beta - Completed endpoint

The minimal source-decorated first-opening object contains:

```text
one root;
one active public endpoint p_Q;
one primitive arrow.
```

Root survival is unresolved, while parallel paths and multiple public
endpoints are enlarged branches. The completed endpoint is fixed before
response evaluation.

## sigma - Response conditioning

The response-closure derivation fixes the normalized complex-linear,
branch-resolved return. The exact witness is:

```text
Fubini-Study curvature                    = 1/4
linear-amplitude attenuation curvature   = 1/4
endpoint-probability curvature            = 1/2
inclusive-sandwich curvature              = 0
```

Neither a probability nor an inclusive sandwich may replace the complex
branch amplitude.

## I - Interval

The one-arm block has the least positive exact-transfer interval:

```text
tau_R=pi/sqrt(2).
```

For every mixed star `m>1`:

```text
|q_m(t)|<=2/(m+1)<1;
|q_sym,m(t)|<=2 sqrt(m)/(m+1)<1.
```

No mixed replacement interval exists and no interval search is authorized.

## Independent verification

The verifier imported no construction code. It recomputed the projector
overlaps and both order witnesses in exact rational arithmetic:

```text
source-projector commutator norm squared = 3/8;
full generator commutator norm squared   = 72;
full unitary-order norm squared          = 288.
```

It also checked every branch-scope and protected-status assertion. Result:

```text
pass = true
```

## What remains

The positive verdict removes the residual `F` choice only after the declared
branch has been fixed. It does not select the physical connected in-state.
The next gate must construct that preparation and the relayed finite
completed-record amplitude.

The mandatory hostile control remains:

```text
Z_N(s)=cos(Ns/2),
```

which shows that finite analyticity and a correct one-cell curvature do not
imply a volume-uniform zero-free neighborhood. Any later T7(ii)-(iv) result
must exclude that coherent shared-source mechanism using the actual parent,
not by assumption.

## Artifact hashes

```text
b99c41a1744f3b252c32b484ec0ce49832fc5f95dc64a6dab2c855afd078892e  STAGE8_T7_RELAYED_FAMILY_RESOLUTION_SPEC_V001.md
4d1510130287f0d8576f8491122742dbd535ab0050dc7ea773341327452dade1  scripts/derive_stage8_t7_relayed_family_resolution_v001.py
58ea19373342116f6b386862df3f729dec10eedb7f329c5f113183ef44c89800  stage8_execution/work/T07_relayed_family_resolution.json
6e1d40e8542b459daae859fcfd9f11d315a07874dc0d2740d34a4edefdb9d14a  scripts/verify_stage8_t7_relayed_family_resolution_v001.py
180d0524b6d2b171019464a4228b2184b76956ee4c3881401d5e917957e23617  stage8_execution/work/T07_relayed_family_resolution_verification.json
```

## Fixed status

```text
relayed_family_resolved = true
physical_connected_preparation_derived = false
connected_primitive_amplitude_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
