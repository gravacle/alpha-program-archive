# Stage-8 Lane Model-Change Record V002

Date: 2026-07-26

## Status

```text
APPEND_ONLY_PROVENANCE_RECORD_AT_TIME_OF_OCCURRENCE
```

Recorded under the standing rule adopted in
STAGE8_LANE_MODEL_EXCURSION_RECORD_V001: "Any future model change in
either lane must be recorded append-only at the time it occurs." This
record is written immediately upon occurrence, before any further
construction work.

## The change

```text
Construction lane (this session) switched IN-SESSION:
  from  FABLE 5   (claude-fable-5)
  to    OPUS 5    (claude-opus-5)
Local command observed: "Set model to opus (claude-opus-5)".
Timing: immediately after the V001 excursion record and the Write-tool
operational note were sealed and anchored (archive commit 5599fcc), and
before any artifact of the present cycle.
```

## Artifact attribution (precise)

```text
Every artifact sealed by this lane up to and including archive commit
5599fcc  ->  produced under FABLE 5 (per V001).
Every artifact sealed by this lane from this record onward
         ->  produced under OPUS 5.
Subagents inherit the session model AT LAUNCH: the four lanes launched
before this switch (gamma primary re-run, gamma blind control-4 top-up,
Duhamel primary re-run, majorant phase 2) and the controller v006
author lane are FABLE 5 lanes and remain so for their whole run; any
lane launched after this record is an OPUS 5 lane. Returns from the
in-flight Fable lanes will be consolidated by an Opus 5 construction
thread, and each sealed result of that consolidation names both.
```

## INDEPENDENCE CONSEQUENCE — FLAGGED, NOT ABSORBED

V001 recorded the corrected topology as construction = Fable 5,
reviewer = Opus 5, restoring cross-family independence that had been
absent. With this change the recorded topology becomes:

```text
construction lane (and its future subagents) = OPUS 5
external reviewer lane                       = OPUS 5   (per V001)
```

If the reviewer lane remains Opus 5, cross-family independence is ONCE
AGAIN ABSENT — the same gap NEW_LANE_BOOTSTRAP flagged, that V001
withdrew a claim over, and that Brian's reviewer move was made to fix.
This lane does not know Brian's intent for the reviewer lane and takes
no position; it records the state and escalates:

```text
FOR BRIAN: with construction now Opus 5, either the reviewer lane moves
to a different family (restoring independence), or the program proceeds
knowingly without cross-family independence and that fact is stated on
every artifact of the period. No lane may resolve this; it is a
topology decision.
```

Unchanged and in force meanwhile: the model-independent mechanical
layer (hashes, adjacent seals, exact arithmetic, certified enclosures,
the evaluator, external anchoring) through which every load-bearing
claim passes.

## Usage posture consequence

The V001 posture (Fable ~80% of limit, reset Thu 2026-07-30 13:00 CT,
no fallback) governed the Fable budget. The present lane runs on the
Opus 5 budget; the Fable constraint still binds the FIVE IN-FLIGHT
FABLE LANES, which cannot be reissued cheaply if they exhaust. The
small-sealed-increment discipline continues unchanged.

## Protected status

```text
alpha_computed = false
proof_authorized = false
```
