# Stage-8 T7 Quarantine / Bridge-Row Conflict — Finding and Escalation V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY_FINDING — RESOLUTION REQUIRES THE PRINCIPAL
```

## What happened (verified, fail-closed, zero writes)

The Brian-authorized quarantine disarm works as intended: seven
invocation attempts against superseded chains all fail closed with zero
artifacts (quarantine manifest dc41d278…).

The mandatory post-disarm real-chain verification then found a SIDE
EFFECT of the disarm, before any production run:

```text
launcher v006 -> controller v006 --lane independent --preflight-only
  status  PREFLIGHT_BLOCKED
  reason  "bridge pre-flight: v001-path implementation input is absent:
           scripts/compare_stage8_t7_actual_parent_regulated_car_
           operator_response_v002.py"
  zero-write CONFIRMED
```

Cause: the sealed v001-path implementation manifest — the bridge
manifest that the BYTE-FROZEN v002 derive lanes verify at runtime, and
that the bridge pre-flight re-verifies row-by-row — pins v002-era files
(launcher v002, controller v002, comparator v002 and their tests) that
the quarantine moved to `scripts/superseded_quarantine/`. Every row is
byte-preserved and recorded in the quarantine manifest; none is lost.

This is exactly the conflict the sealed disarm disposition anticipated
("quarantine (move) breaks the sealed manifests' path+hash row
verification"), and its proposed mechanism named the remedy in the same
breath ("PLUS an amendment to the immutability-sweep expectation: rows
of sealed manifests whose paths are quarantined verify at the quarantine
path via the quarantine manifest"). The conflict surfaced here in the
bridge pre-flight rather than in a sweep.

## Why this lane stops rather than repairs

Both candidate resolutions cross a boundary this lane may not cross
alone:

```text
(A) QUARANTINE-AWARE ROW RESOLUTION (the disposition's own remedy):
    a path absent at its canonical location but present in the sealed
    quarantine manifest resolves to its quarantine path and verifies
    against the recorded hash. Clean and append-only for the CURRENT
    chain — but the BYTE-FROZEN v002 derive lanes perform the same
    full-manifest verification internally, so they would still fail at
    runtime. Making them quarantine-aware means editing components
    whose byte-frozen, twice-audited pedigree is itself an audited
    property.
(B) SELECTIVE RESTORATION: return only the v002-era files that the
    v001-path bridge manifest pins, keeping v003/v004 quarantined.
    This restores the bridge and the frozen lanes untouched — but
    launcher v002 returns to a canonical path and allowlists controller
    v002, so the v002 chain (which carries the live GPG defect class the
    reviewer named) becomes launchable again: a partial reopening of
    B2, i.e. a narrowing of the disarm the principal authorized.
```

A third option — quarantining only the sealed manifests that the
superseded controllers verify — disarms v003/v004 but not v002, and
touches the bridge manifest the current chain needs.

## State of the pipeline meanwhile

```text
Manifest v005 sealed (v006 inventory) — the chain's authority exists.
Pre-flight reaches step 4 (bridge_binding): runtime attestation,
  implementation manifest, and all authority digests PASS; the block is
  precisely and only the quarantined bridge row.
Suites: launcher v006 6/6; controller v006 27/27 (fixture-root real-
  launcher/real-controller assertions included).
Production remains PROHIBITED independently of this finding (reviewer
  verdict and recorded typed authorization both absent).
```

## Recommendation (stated, not taken)

(A) with its frozen-lane consequence made explicit: implement
quarantine-aware resolution in the current chain, and treat the frozen
derive lanes' internal full-manifest verification as a separately
dispositioned item — either an authorized narrow amendment to those two
files (with fresh hostile review of exactly that diff), or a scoped
acceptance that the bridge manifest's quarantined rows are verified by
the controller pre-flight on their behalf. This preserves the full
disarm the principal authorized; (B) does not.

## Protected status

```text
superseded_chains_mechanically_disarmed = true
production_chain_startable = false
alpha_computed = false
proof_authorized = false
```
