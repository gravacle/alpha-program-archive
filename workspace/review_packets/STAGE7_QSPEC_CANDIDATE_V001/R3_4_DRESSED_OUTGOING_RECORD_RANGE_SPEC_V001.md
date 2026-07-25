# R3.4 Dressed Outgoing-Record Range Correction Specification v001

Date: 2026-07-24

## Status

Result-aware correction gate. A hostile internal review found that the
stabilized Heisenberg image of a bare record observable can contain source
projectors. The earlier phrase "public-record endomorphism" is therefore
under direct test.

No alpha or measured target enters this correction.

## Hash-pinned historical results

```text
R3_4_SHARED_SOURCE_CAUSAL_PARENT_V001.seal.sha256
  1f710cb0e865e359988ba4fe1800f1c8e025f5eee9185ce5521371ef5a8d42ef

R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_V001.seal.sha256
  56d257cd0d9218a37277850a9dff987a54757153d49ade4a232d0a4684cd276d

R3_4_SHARED_SOURCE_CAUSAL_PARENT_RESULT_V001.md
  781608f2fe4c8753a0c06b1d87407b2a6c88caa0ab45329e1200160e56292a24

R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_RESULT_V001.md
  1d114e71c29c3a39b7afd1b7a80b47afb52fe77e8ee1e4e19b604defe3c69305

CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md
  b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30

PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md
  532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb
```

## Required calculation

On two shared-source causal cells, let

```text
W_1=U_0;
W_2=U_1U_0.
```

For every matrix unit `E_ab` of the first record factor, define

```text
Phi_N(E_ab)
 =W_N^* (I_source tensor E_ab tensor I) W_N.
```

The gate must test:

1. stabilization: `Phi_2(E_ab)=Phi_1(E_ab)` for all nine matrix units;
2. range: whether `Phi_1(E_ab)` lies in
   `I_source tensor A_records`;
3. star preservation, multiplication, unitality, and norm preservation;
4. noncommutation of a nontrivial image with at least one source observable;
5. compatibility of the already computed bare output-record state
   restrictions.

The conditional expectation onto the bare record-only algebra is

```text
E_R(X)
 =I_source tensor Tr_source(X)/dim(H_source).
```

A nonzero norm of `X-E_R(X)` proves that the image is not record-only.

## Predeclared adjudication

```text
if the images stabilize but leave the record-only algebra:
  STABLE_DRESSED_RECORD_MONOMORPHISM_DERIVED;
  outgoing_public_record_Moller_endomorphism_derived = false;

if the images remain in the record-only algebra:
  BARE_RECORD_ENDOMORPHISM_CONFIRMED;

otherwise:
  OUTGOING_RECORD_RANGE_BLOCKED.
```

Under the first verdict, the correct outgoing object is an isomorphic
dressed copy of the record algebra embedded in the full source-record
algebra. It is not an endomorphism of the bare record-only algebra.

## Fixed scope

```text
same_GNS_unitary_Moller_implementer_derived = false
complete_parent_to_outgoing_GNS_map_derived = false
generated_descendant_action_derived = false
complete_physical_durability_derived = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
