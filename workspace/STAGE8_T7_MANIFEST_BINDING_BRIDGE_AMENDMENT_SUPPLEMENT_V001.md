# Stage-8 T7 Manifest-Binding Bridge Amendment — Supplement V001

Date: 2026-07-25 (night)

## Status

```text
APPEND_ONLY_SCOPE_SUPPLEMENT_SEALED_BEFORE_AUTHORING
```

The v004 hostile verification returned NOT_READY with a SOLE blocker
outside the bridge amendment's enumeration: the pinned launcher v003's
frozen ALLOWED_TARGETS cannot launch the v004 comparator or v004 test
files (wedge class caught PRE-production; all four authored v004 files
otherwise verify defect-free). The bridge amendment (A2) enumerated no
launcher change; this supplement adds the minimal rows.

## Authorized additions (nothing else)

1. `scripts/launch_stage8_t7_content_addressed_runtime_v004.py` — base
   launcher v003 (read-once, registered __main__); SOLE change:
   ALLOWED_TARGETS gains three rows (compare v004, test_compare v004,
   test_controller v004), retaining every existing row.
2. `scripts/test_stage8_t7_launcher_v004.py` — base v003 launcher test
   pointing at launcher v004 (all fences re-run incl. read-once A/B/A).
3. The UNSEALED controller v004 and test_controller v004 drafts are
   repointed to launcher v004 (runtime path + manifest row + fixture
   references). Both are pre-seal working drafts; the bridge
   amendment's enumeration is amended accordingly.
4. Manifest v003 inventory (bridge amendment A2 item 5) updated:
   launcher v004 and test_launcher v004 replace the v003 rows;
   otherwise unchanged (controller v004, comparator v004, derive v002
   x2, test_compare v004, test_controller v004, derive-lane v002
   tests).

The comparator v004 author's interpretive decision (executor rows
cross-checked between manifests; launcher authority resting on the
comparator's own manifest + read-once attestation, because the sealed
v001-path manifest pins the v002 launcher and a path-keyed launcher
cross-check would reintroduce the wedge) is RATIFIED by this supplement
and flagged for the external reviewer's sign-off in the re-audit.

## Protected status

```text
actual_parent_regulated_CAR_operator_response_derived = false
kappa_record_computed = false
alpha_computed = false
proof_authorized = false
```
