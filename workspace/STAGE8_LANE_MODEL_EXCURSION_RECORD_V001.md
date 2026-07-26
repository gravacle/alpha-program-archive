# Stage-8 Lane Model-Excursion Record V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY_PROVENANCE_CORRECTION
```

The sealed custody note LANE_CHANGE_CUSTODY_CLAUDE_CONSTRUCTION_V001.md
(seal fc585326…) states: "The incoming lane is a FRESH CLAUDE ACCOUNT
(model Opus 4.8)". That assertion is corrected of record here; the
custody note itself is not altered. No verdict, threshold, or sealed
result changes; this is provenance accuracy of exactly the class this
program records rather than leaves implicit.

## What is establishable from this lane's own transcript

1. The session was LAUNCHED with model flags reading claude-opus-4-8;
   the system context asserted Opus 4.8.
2. The model was switched IN-SESSION to Fable 5 (local command "Set
   model to claude-fable-5") IMMEDIATELY after this lane's very first
   action (the NEW_LANE_BOOTSTRAP read) and BEFORE any other read or
   any write.
3. Therefore: EVERY artifact this lane produced — beginning with the
   custody note itself, and including every sealed spec, binding,
   amendment, record, review transcript, and script cycle of
   2026-07-25/26 — was produced under FABLE 5. The custody note's
   "(model Opus 4.8)" was already inaccurate at its own sealing. The
   only pre-switch action was the single bootstrap read.
4. Subagents inherit the session model: every supervision, hostile-
   review, blind, verification, and execution subagent launched by this
   lane also ran FABLE 5.

## Independence consequence (stated plainly)

The external reviewer lane's v002/v003/v004-era audits described their
own independence as "different model family (Fable, not Opus)" —
premised on this lane being Opus. Under the actual state, reviewer and
construction were BOTH Fable: during those audits the program had NO
cross-family independence at all — precisely the gap NEW_LANE_BOOTSTRAP
flagged and the falsification erratum's calibration note named. The
audits' FINDINGS stand on their verified content (each confirmed
finding was independently reproduced in code or algebra by lanes whose
work is sealed), but the cross-family-independence CLAIM attached to
them was not true at the time and is withdrawn of record.

Compensation that WAS in force throughout, per the bootstrap's own
design: the mechanical layer — hashes, adjacent seals, exact
arithmetic, certified enclosures, the evaluator, external anchoring —
is model-independent, and every load-bearing claim of the period passed
through it.

## Topology going forward (Brian's correction)

```text
construction lane (this lane, incl. its subagents) = FABLE 5
external reviewer lane                             = OPUS 5
```

Cross-family independence is thereby restored. Any future model change
in either lane must be recorded append-only at the time it occurs.

## Usage posture recorded

Fable 5 usage stands at ~80% of limit, resetting Thursday 2026-07-30
13:00 CT, with NO configured fallback: work seals in small complete
increments; CONTINUATION_STATE updates after each completed item; near
the limit, remaining budget goes to RECORDING state, not new
computation.

## Protected status

```text
alpha_computed = false
proof_authorized = false
```
