# Stage-8 Real-Component and Precondition Discipline — Supplement V001 (Rule 4)

Date: 2026-07-26

## Status

```text
STANDING_DISCIPLINE_SUPPLEMENT_SEALED
```

Adopted on the reviewer's batch-audit finding (fifth repetition of the
defect class, sharpest form: a production docstring ASSERTING a
mechanism that did not exist). Appends to the sealed discipline
(STAGE8_REAL_COMPONENT_PRECONDITION_DISCIPLINE_V001):

```text
RULE 4: no production file may assert in prose that a mechanism exists
unless a test drives that mechanism. Docstring claims are checkable
claims, and every mechanism claim in a production file must name (in
the verification artifact of its cycle) the test that drives it.
```

DOCSTRING-TRUTH DISPOSITION OF RECORD: launcher v005's docstring claim
("the superseded chains are made unlaunchable on the canonical paths
mechanically") was FALSE when sealed and is TRUE as of the authorized
quarantine disarm executed this date (quarantine manifest dc41d278…,
seven fail-closed invocation attempts recorded, zero artifacts). Per
the reviewer's instruction the statement now stands; the mechanism that
makes it true is the quarantine, driven by the recorded invocation
attempts and the launcher suite's allowlist regression fence.

## Protected status

```text
alpha_computed = false
proof_authorized = false
```
