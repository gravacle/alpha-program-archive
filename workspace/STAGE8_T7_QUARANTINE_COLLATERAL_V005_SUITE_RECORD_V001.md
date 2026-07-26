# Stage-8 T7 Quarantine Collateral — v005 Launcher Suite Record V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY_COLLATERAL_RECORD (previously unrecorded — disclosed, not backdated)
```

RECORD GAP DISCLOSED: this collateral was observed by the construction
lane during the v006 cycle and was NOT sealed at the time. It is recorded
now, on discovery of the omission, in the same class as the
evidence-in-scratchpad failure the reviewer previously named.

## The collateral

```text
scripts/test_stage8_t7_launcher_v005.py  now FAILS.
Reproduced this date:
  RuntimeError: regression-fence precondition:
  scripts/compare_stage8_t7_actual_parent_regulated_car_operator_
  response_v003.py should exist on disk
```

Cause: that suite's Blocking-2 regression fence asserts the superseded
comparator/controller files are PRESENT at their canonical paths, so that
a block by resolve_target proves the ALLOWLIST (not mere absence) does
the work. The Brian-authorized quarantine moved those files, so the
fence's precondition is now false. The fence's LOGIC was correct
pre-quarantine; it is its precondition that the disarm invalidated.

## What was and was not done

```text
NOT EDITED: test_stage8_t7_launcher_v005.py is a sealed-era file pinned by
  implementation manifest v004; it was deliberately left byte-frozen.
CARRIED FORWARD INSTEAD: test_stage8_t7_launcher_v006.py carries the
  quarantine-aware form of the same fence, which is STRICTLY STRONGER —
  it asserts (i) the superseded names are ABSENT at canonical paths, and
  (ii) their surviving quarantine copies, which DO exist on disk, are
  blocked by the allowlist. Both legs verified; suite 6/6.
```

## Consequence, stated plainly

```text
The CURRENT authority (implementation manifest v005) does not include the
v005 launcher test; it includes the v006 test. The current chain is
therefore unaffected by this failure.
BUT: manifest v004's sealed inventory contains a test that no longer
passes on this workspace. Any audit that re-runs the v004-era suite will
observe the failure, and must not read it as a defect of the disarm or of
the v006 work. It is the expected, disclosed cost of the authorized
quarantine.
```

## Protected status

```text
quarantine_collateral_v005_suite_recorded = true
alpha_computed = false
proof_authorized = false
```
