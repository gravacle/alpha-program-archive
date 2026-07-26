# Stage-8 T7 Controller v006 Repair Binding — Supplement V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY_SCOPE_SUPPLEMENT_SEALED_BEFORE_AUTHORING
```

The controller v006 authoring lane raised two flags under the sealed
discipline's rule-1 corollary (name the gap, do not work around it),
recorded verbatim in CONTROLLER_V006_AUTHOR_RETURN_SEALED_TRANSCRIPT_V001:

```text
Flag 1: launcher v005 allowlists test_stage8_t7_controller_v005.py, not
        the v006 test.
Flag 2: launcher v005 carries NO row for controller v006, so canonical
        PREFLIGHT_OK is mechanically unreachable (the B1 defect class).
```

The v006 binding's clause 3 authored no launcher v006; that clause is
superseded here. This is the correct handling of the class: the gap was
detected pre-production by the lane that created it, and is closed
mechanically rather than by disposition-in-prose.

## Authorized additions (nothing else)

```text
1. scripts/launch_stage8_t7_content_addressed_runtime_v006.py — base
   launcher v005; SOLE change: ALLOWED_TARGETS gains exactly two rows
   (run_stage8_t7_actual_parent_car_pipeline_v006.py and
   test_stage8_t7_controller_v006.py), every existing row retained and
   NO superseded-generation row introduced (the quarantine stands).
2. scripts/test_stage8_t7_launcher_v006.py — base v005 launcher test
   repointed (self-echo target and pass-line label), retaining the
   allowlist regression fence and extending its exact set-equality to
   the v006 row set.
3. controller v006 and its test are repointed to launcher v006 (runtime
   path + manifest row + fixture references); the comparator v005
   RUNTIME_LAUNCHER_PATH is NOT changed (comparator v006 is out of
   scope; the controller's bridge pre-flight verifies the launcher row
   against disk either way, and the manifest v005 inventory pins both).
4. provenance/..._implementation_v005.json (+ seal) over the v006
   inventory, built AFTER the real-chain verification below.
```

## Mandatory verification (discipline rules 1 and 2)

Before manifest v005 seals: the REAL launcher v006 must drive the REAL
controller v006 `--preflight-only --lane independent` against the
canonical workspace, read-only, and the recorded outcome (PREFLIGHT_OK
with the full ten-step enumeration, or the precise block reason) plus a
zero-write verification must be part of the cycle's sealed evidence.

## Protected status

```text
alpha_computed = false
proof_authorized = false
```
