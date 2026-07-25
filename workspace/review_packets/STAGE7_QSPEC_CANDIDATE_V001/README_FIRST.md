# Stage-7 Q_spec Candidate Review Packet v001

Date: 2026-07-24

## Read first

1. `STAGE7_REVIEW_REQUEST_V001.md`
2. `STAGE7_QSPEC_REVIEW_CANDIDATE_V001.md`
3. `STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V001.md`
4. `STAGE1_PREMISE_DISPOSITION_V001.md`
5. `STAGE7_CONSTRUCTION_LANE_SELF_REVIEW_V001.md`

Then inspect the four sealed result bundles:

```text
R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION;
R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT;
R3_4_OUTGOING_RECORD_GNS_COMPLETION;
FORK_8_CAUSAL_DIRECT_LIMIT_PROMOTION.
```

## Required independence

The three required reviews are not present in this packet and must be run in
fresh Fable contexts:

```text
R1 mathematical/operator;
R2 physical/QED;
R3 provenance/target-blindness/implementation.
```

The included construction-lane self-review is a fourth, explicitly
non-independent voice.

## Current status

```text
durability_parent_derived_in_declared_branch = true
fork_8_closed_at_scoped_durability_level = true
stage6_ledger_frozen = true
stage7_candidate_frozen = true

complete_parameter_free_Q_spec_frozen = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```

The packet asks whether the frozen candidate and ledger are correct. It does
not ask reviewers to accept alpha or a complete electromagnetic theory.

## Integrity

Run:

```text
shasum -a 256 -c STAGE7_PACKET_MANIFEST_V001.sha256
```

from this directory. The zip hash is recorded beside the zip in the parent
`review_packets` directory.
