# Stage-8 T7 Four-Axis Scope-Extension Adjudication Spec v001

Date: 2026-07-25

## Purpose

Adjudicate the four scope extensions required before any existing zero-free
or analytic result may be used for Stage-8 T7:

1. layer: the primitive completed-record amplitude;
2. carrier: a declared continuum-exhaustion member beyond the three-site
   regression fixture;
3. quantifier: the relayed causally sequential exhaustion and connected
   cellulations, rather than repeated time-supercells of one frozen chain;
4. object: exact reduction of the finite connected amplitude `Z_N` to the
   pinned one-handle ratio.

Each axis is either derived from the pinned authorities or assigned an
honest blocking scope restriction. No axis may pass by notation, by
substituting a complete-`Q_spec` CTP scalar for a primitive object, or by
selecting the branch that gives a preferred downstream value.

## Pinned authorities

```text
85d24996987278b285d63b8fe15a8732e55664e7c1b09063617b66cb4bc926b4  STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_V001.md
9410ee80ff89beed4e133f75fcdb952d059f3386df12069793b5d60895d15486  STAGE8_T7_CRITICAL_PATH_SCOPE_CORRECTION_V001.md
6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb  BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md
e12fffcc0f94d6896bc5607898db6b3a1ea343aeaf557b1f6f70e58db061fab6  STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md
0df721a170f4f4a1ec630775a3ae47b0d793c82e100b326e681030389eaf0694  STAGE8_T7_OPEN_EXHAUSTION_ATTACHMENT_AND_RELAY_NECESSITY_RESULT_V001.md
29c32f90e6a4f88a26e22c91504b6d92a1fc4083ad6368984a1e94858caa4365  STAGE8_T7_RELAY_DEPENDENCY_ORDER_AMENDMENT_V001.md
52401eefc3ff84e22f04bbc329a619b830058661db7f969d2d43d167d97d893d  STAGE8_T7_RELAYED_FAMILY_RESOLUTION_RESULT_V001.md
7aafba8667ac01f1c4326b0d714e838bf068eec7c8f4ce28ef03c8bef9d62098  STAGE8_T7_ACTUAL_PARENT_RECORD_AMPLITUDE_ADJUDICATION_RESULT_V001.md
6447eb80c9347e614a1ecfbfef6234e4acec5caadf829a8649fdb5282439aa09  STAGE8_T7_SOURCE_SCALARIZATION_NO_GO_RESULT_V001.md
f1dc38f8a08b9e21675dc35fc91ffbd5e0b94d3feb5113f850c09a19b89bbd38  STAGE8_T7_THREE_SITE_BASELINE_SCOPE_ERRATUM_V001.md
6e24ceb6b18e6e6da5a6d21e872f90f6d79a324df9f305d226ab6edec863831b  STAGE8_T7_COMPLETED_CONTINUUM_RESPONSE_PROVENANCE_SPEC_V001.md
a1258dcf40732f0e3fce358a68ffdbd34bc347d70283550440582a1129bec510  STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001.md
6a49a75669e61f74b2d1a6904c7bc1a4bb172842f4b01b84456c4cee65334676  COMPLETE_QSPEC_EXACT_SPIN2_SUPPORT_BRIDGE_RESULT_V001.md
ecca90cdb3ca81605da84b1a341d361127446df56cb9139e5a9efbc663919f5c  COMPLETE_QSPEC_CANONICAL_FULL_LOCAL_SOURCE_POLYDISC_RESULT_V001.md
```

The last two authorities close the exact reduced-to-full spin-2 bridge and a
periodic complete-`Q_spec` local-source theorem. They are included as
anti-substitution controls: neither may discharge a primitive T7 axis.

The continuum-Galerkin correction controls wherever it conflicts with the
earlier completed-continuum provenance specification or its
parent-state-regulator input. The withdrawn exact-reducing-family label may
not satisfy Axis 2.

## Frozen adjudication rule

For every axis, return exactly:

```text
status = DERIVED | SCOPE_RESTRICTED_BLOCKING
reason = AXISn_<specific reason>
```

`DERIVED` requires every positive obligation for that axis. If even one
positive obligation is absent, the axis is
`SCOPE_RESTRICTED_BLOCKING`. A restriction is a Stage-8 blocker, not a
conditional pass.

No choice between these verdicts may use a coupling value, `kappa_record`,
alpha, or the success or failure of any downstream numerical match.

Before adjudication, the executor must:

1. verify the hash of this sealed specification and every pinned authority;
2. verify every available authority sidecar seal;
3. apply correction and erratum authorities in preference to older
   conflicting claims;
4. reject every unpinned artifact as positive evidence; and
5. attest that it did not access a coupling value, `kappa_record`, alpha, or
   any downstream-match artifact.

Any failed hash, seal, precedence, provenance, or no-target check aborts the
adjudication.

## Axis 1 - Layer

To return `DERIVED`, establish all of:

1. the actual finite Lorentzian primitive parent, not a line-only,
   projector-chain, downstream/regulator-imported CAR/Fock, or
   complete-`Q_spec` substitute, supplies a normalized complex scalar
   completed-record amplitude;
2. the scalar functional is fixed by pre-existing primitive data, is
   gauge-covariant, natural under admitted carrier embeddings, and has a
   regulator-independent continuum meaning;
3. its flat baseline is nonzero on every admitted finite member;
4. it reduces exactly to the pinned one-handle amplitude at `N=1`.

A CAR/UHF or quasifree scalarization remains admissible if it is derived
from the primitive parent itself and proves naturality, continuum
compatibility, and exact one-handle reduction. It may not be imported from a
downstream complete-`Q_spec` result.

If the pinned current authorities derive only an operator-valued
completed-record map and do not derive a canonical primitive scalar
functional, return:

```text
status = SCOPE_RESTRICTED_BLOCKING
reason = AXIS1_PRIMITIVE_SCALAR_AMPLITUDE_SCOPE_RESTRICTED
```

The complete-`Q_spec` CTP scalar remains downstream and is not a repair.
This is an authority-relative scope restriction, not a theorem that no
physical primitive scalar amplitude can exist. An append-only successor may
discharge it by deriving the missing functional from upstream primitive
data.

## Axis 2 - Carrier

To return `DERIVED`, construct the Axis-1 object on at least one declared
member of the admissible continuum exhaustion beyond the three-site
regression fixture and prove that the member is obtained from the pinned
primitive parent without an inserted regulator state, trace, determinant,
counterterm, or endpoint ray.

If only the one-handle object, three-site regression, periodic fixture, or
an unexecuted continuum provenance specification exists, return:

```text
status = SCOPE_RESTRICTED_BLOCKING
reason = AXIS2_CARRIER_SCOPE_RESTRICTED
```

## Axis 3 - Quantifier

To return `DERIVED`, prove one common volume-uniform neighborhood over:

```text
all finite stages of the relayed causally sequential exhaustion;
the declared connected-cellulation class; and
the pinned common-refinement maps.
```

Repeating `N` time-supercells of one frozen periodic transfer does not
satisfy this quantifier.

If the available theorem is confined to a periodic chain or one
cellulation family, return:

```text
status = SCOPE_RESTRICTED_BLOCKING
reason = AXIS3_QUANTIFIER_SCOPE_RESTRICTED
```

## Axis 4 - Object

To return `DERIVED`, prove for the same Axis-1 object:

```text
Z_1(A)=a_h(A)/a_h(0)
```

with the root line, completed endpoint, connection return, and
normalization exactly those of the pinned one-handle derivation. The proof
must use the actual finite parent. An ideal projector-chain identity,
postselected source ray, or favorable finite wavepacket is insufficient.

Otherwise return:

```text
status = SCOPE_RESTRICTED_BLOCKING
reason = AXIS4_ONE_HANDLE_REDUCTION_SCOPE_RESTRICTED
```

## Aggregate verdict

Return:

```text
STAGE8_T7_FOUR_AXIS_SCOPE_EXTENSION_DERIVED
```

only if all four axes are `DERIVED`.

If any axis is restricted, return:

```text
STAGE8_T7_FOUR_AXIS_SCOPE_EXTENSION_BLOCKED
```

and list every restriction independently. Later linked-cluster,
Duhamel/Hessian, and ER-fork work may not convert that verdict without an
append-only successor that discharges the restricted axis.

## Protected status

The executor may set only these axis flags, and only when the corresponding
axis has `status = DERIVED`:

```text
axis1_primitive_layer_derived
axis2_continuum_carrier_member_derived
axis3_connected_exhaustion_uniformity_derived
axis4_one_handle_reduction_derived
```

Every restricted axis flag remains false. Regardless of the four-axis
verdict, all downstream and protected flags below remain false:

```text
primitive_source_scalarization_derived = false
connected_primitive_amplitude_derived = false
primitive_continuum_exhaustion_member_derived = false
primitive_connected_cellulation_uniformity_proved = false
primitive_ZN_one_handle_reduction_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
