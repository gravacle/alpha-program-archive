# Stage 8 Construction Conventions C1-C5 - Proposed Rules V001

Date: 2026-07-28

Status: PROPOSED / AWAITING PRINCIPAL RATIFICATION. This artifact records five
construction conventions from
`EINSTEIN_HANDOFF_2026-07-28.md`
(`2c4eb207872cfb7d497a83ea134cee5cd1bb8fe244f8c5b5798d8841186d0398`)
as proposed rules. It does not adopt them and does not change any verdict,
register row, seal, or evaluator rule.

```text
rules_adopted = false
principal_ratification_required = true
alpha_computed = false
proof_authorized = false
```

## C1 - Lane Findings Do Not Get Part 2 Rows

Proposed rule:

```text
A lane finding does not receive a Part 2 row in STAGE8_LANE_STATUS.md merely
because it is a finding. Part 2 is reserved for ruled items. Lane findings may
be sealed, cited, mirrored, committed, and used as authorities within their
scope, but they are not indexed as principal rulings unless a principal ruling
exists.
```

Rationale:

```text
The handoff identifies a recurring defect: lane determinations were previously
filed under "RULED", blurring lane output with principal-held decisions. This
rule preserves the register as a decision index rather than a general finding
ledger.
```

## C2 - Named Obstruction At A Line Is A Sealable Result Class

Proposed rule:

```text
A failed attempt is sealable as a result when it names the obstruction at a
specific file and line, states the attempted route, and records what was not
proved, repaired, adopted, or computed.
```

Rationale:

```text
The program needs failed attempts to retire false routes without converting
them into impossibility claims. A named obstruction at a line makes the failure
auditable and distinguishes "not closed" from "not attempted".
```

## C3 - If A Sealed Clause Says A Register Row Exists, Write The Row

Proposed rule:

```text
When a sealed clause asserts that the status register carries a row and the row
does not exist, the construction lane should write the missing index row rather
than edit the sealed clause, provided the row faithfully indexes an existing
authority and does not manufacture a ruling.
```

Rationale:

```text
This makes the sealed clause true by completing the index, while preserving the
append-only record. If no existing authority supports the row, the lane must
stop and report the conflict rather than inventing one.
```

## C4 - Declined Referral Is Provenance

Proposed rule:

```text
A declined or contaminated referral is provenance and should appear on the face
of the relevant result when it materially affects independence, timing, or the
usable authority of the result.
```

Rationale:

```text
The blind-wall discipline depends on knowing which independent checks occurred,
which were declined, and why. Omitting a declined referral can make a result
look cleaner or more independent than it is.
```

## C5 - Carrier-Indexed Numbers May Be Used Refutationally

Proposed rule:

```text
Carrier-indexed numbers may be used refutationally to decide a negative
existential or exhibit a finite-carrier counterexample, while remaining
inadmissible as constants in any F'-5-governed bound.
```

Rationale:

```text
F'-5 forbids carrier-indexed constants in certified bounds. That fence does not
forbid exact finite-carrier evidence from refuting a universal claim or a
purported identity. The proposed rule preserves the object-vs-bound
distinction.
```

## Flags

```text
C1_proposed = true
C2_proposed = true
C3_proposed = true
C4_proposed = true
C5_proposed = true
rules_adopted = false
awaiting_principal_ratification = true
alpha_computed = false
proof_authorized = false
```
