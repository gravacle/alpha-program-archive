# Stage-8 T7 Cycle-7 Package Record, and Three Findings V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY. SEALED AND LEFT TO WAIT, NOT TRICKLED, per the principal's
packaging instruction. PRODUCTION REMAINS PROHIBITED: the gate verdict is
NO_GO and there is no recorded typed authorization.
THE PIPELINE ITSELF NOW HAS A BLOCKING FINDING OF ITS OWN (F-1).
```

## What cycle 7 delivered

Authored against Part A (A1–A5) and Part B of
`STAGE8_T7_PRODUCTION_GATE_NOGO_AND_PIPELINE_REPAIR_BINDING_V001.md`
(`aa8758a9…`). Sealed component record:
`STAGE8_T7_GENERATION_G7_COHERENCE_TABLE_V001.md` (`d77dda56…`).

```text
ONE COHERENT GENERATION, stage8_t7_generation_g7:
  controller v007 + launcher v007 + comparator v006 + manifest v006,
  twelve-row inventory; the byte-frozen v002 derive lanes are SHARED
  members reached ONLY through the v001-path bridge
  (stage8_t7_generation_bridge_v001).
A1  15-row pin table, ALL EXACT PINS, each read from the enforcement
    point as DATA (ast parse of the file's own bytes — no import, no
    exec; manifest pins from JSON). REQUIRED_MANIFEST_ROWS and
    REQUIRED_ALLOWLIST_ROWS are DERIVED from GENERATION_MEMBERS, not
    hand-typed, and verify_pin_table_is_total() blocks if a component
    family exists with no pin or a derived set stops matching its
    declared derivation — a future bump cannot silently orphan a row.
A2  REAL-CHAIN REHEARSAL, 184 s, no stubs, no monkeypatches, disposable
    copy from the canonical at-rest state. PREFLIGHT_OK was recorded and
    EXPLICITLY NOT OFFERED AS EVIDENCE, per A2.
A4  Receipt-before-check defect in v006 CONFIRMED by reading the source
    (atomic_sealed_json ran BEFORE the target_intact and returncode
    checks) and INVERTED in v007 — both checks first. Covered twice:
    behaviourally through the real chain to returncode 2 (no receipt, no
    seal) and by an AST source-order assertion.
SUITES at the final byte state: launcher v007 6/6, controller v007 10/10
    (8 one-pin skews each blocking by pin id; manifest-row skew; fence
    raise/drop; L3 self-heal; a REAL SIGTERM inside the raised window;
    A4 twice), comparator v006 5/5.
B1  FIX VERIFIED EMPIRICALLY BEFORE AUTHORING: real lanes under launcher
    v006 -> real comparator v005 sealed BLOCKED with reason "independent
    runtime-launcher provenance mismatch" at the canonical comparison
    path in 0.7 s, before touching a number. That is the six-cycle
    defect reproduced, not argued.
```

## FENCE ADOPTION PROBE — verdict recorded either way, as instructed

```text
VERDICT: YES, ON FUNCTION.
  every lane raised and dropped BOTH fenced directories;
  every lane WROTE THROUGH the raised fence (independent 84.6 s, primary
    11.2 s, comparison 2.6 s);
  the fence was verified CLOSED after every lane BY ATTEMPTING A WRITE,
    not by reading the mode;
  the superseded route (launcher v002 -> derive independent v002) with
    the fence at rest raised PermissionError, rc 1, and produced ZERO
    artifacts — B3 closed, and B4 closed by the same mechanism.
MATERIAL QUALIFICATION: see F-3. The fence works WHEN SET. Its at-rest
state does not hold itself in this environment.
```

## F-1 — BLOCKING. The real chain does not pass.

```text
Executed end to end for the first time in this program's history:
  VERDICT  ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_BLOCKED
           "34 component comparison(s) failed"
  34 of 157 component comparisons exceed TRANSPORTED_MATRIX_TOLERANCE
    = 3.0e-4: propagators 10, cross_operators 24; split ell0 28 / ell1 6.
  worst    8.411e-4 = 2.80x budget
  typical  4.206e-4 = 1.40x budget
  and the 104 PASSING transported rows have worst margin 2.941e-4 —
    i.e. THE WHOLE POPULATION SITS AT THE BUDGET SCALE, which is the
    part that matters and the part that is not explained by a few
    outliers.
  Bit-for-bit reproducible across two independently produced bundle
    pairs (one built under launcher v006, one under v007).
NOT FIXABLE BY THIS LANE, and that is the point: derive lanes are
byte-frozen; comparator v006's numerics are byte-identical to v005
(tested); no measured constant was introduced.
This is Part B item B2 CONFIRMED BY EXECUTION.

WHY IT IS BLOCKING RATHER THAN MERELY BAD: a content failure IS a
verdict, so the comparator seals it AT THE CANONICAL COMPARISON PATH by
design. The provenance prologue hoisted in cycle 7 covers PROVENANCE
ONLY — deliberately, and on the record. Therefore THE FIRST CANONICAL
PRODUCTION COMPARISON RUN WILL PERMANENTLY CONSUME THE CANONICAL
COMPARISON PATH WITH A BLOCKED VERDICT. The tolerance question must be
settled BEFORE that run, not after, and it is the principal's.
```

### The tolerance's freeze status — stated precisely, because it decides whether the failure can ever be argued away

```text
VERIFIED BY THIS LANE, not accepted on report:
  TRANSPORTED_MATRIX_TOLERANCE = 3.0e-4 is byte-identical in comparator
    v002, v005 and v006 — four generations, long predating any execution
    of the real chain.
  SEALED implementation manifest v001 (the EARLIEST, and the one the
    byte-frozen derive lanes verify row-by-row at canonical paths)
    HASHES COMPARATOR v002, which carries 3.0e-4. Manifests v004 and
    v005 hash comparator v005, also 3.0e-4.
  THEREFORE the freeze is REAL and it is OUTCOME-BLIND: the number was
    hash-pinned into a sealed manifest generations before anyone saw a
    comparison result.
  *** BUT, AND THIS IS THE CORRECTION TO THE STRONGER PHRASING: 3.0e-4
  IS NOT STATED IN ANY SEALED PROSE SPEC. It appears nowhere in the
  Phase-A execution binding and nowhere in any sealed .md except the
  cycle-7 coherence table written today. Its "preregistered" status
  rests on CODE PROVENANCE hashed into sealed manifests, NOT on a spec
  clause. ***
CONSEQUENCE, stated so no future lane can exploit the gap: revising
3.0e-4 after seeing 34 failures would be outcome-driven revision of a
frozen budget and is FORBIDDEN. The gap means a future lane could argue
the point more easily than it should be able to; it does not make the
argument legitimate. If the tolerance is ever to change it changes by a
recorded principal decision with the pre-revision numbers preserved.
```

## F-2 — procedural, and DELIBERATELY LEFT OPEN

```text
Manifest v006 is NOT sealed into canonical provenance/. Controller v007
therefore fails CLOSED at the implementation_manifest step, naming the
absent manifest. One authorized L4 raise closes it:
  <pinned python> -I -S scripts/launch_stage8_t7_content_addressed_runtime_v007.py \
    scripts/build_stage8_t7_actual_parent_car_implementation_manifest_v006.py \
    --l4-raise-and-record
THIS LANE DID NOT RUN IT, on purpose. Closing F-2 requires raising the
canonical fence, and the fence's own integrity is in question under F-3.
Two open questions must not be resolved by one unilateral write. The
builder was exercised for real in every disposable copy (12 rows, fence
dropped, verified). Fail-closed is the correct resting state.
```

## F-3 — NEW, and it lands on the principal's B3/B4 decision

```text
THE FACT, VERIFIED INDEPENDENTLY BY THIS LANE WITH stat:
  canonical stage8_execution/work  -> drwx------  (0700)
  canonical provenance             -> drwx------  (0700)
The AT-REST MODE OF RECORD IS 0555
(STAGE8_T7_DIRECTORY_PERMISSION_FENCE_EVALUATION_AND_PROBES_V001.md:
"stage8_execution/work and provenance are LEFT AT MODE 555").
THE CANONICAL FENCE IS PRESENTLY OPEN.

CAN THE PROGRAM HAVE DONE THIS TO ITSELF? Ruled out, with evidence:
  - the ONLY occurrence of 0o700 anywhere in scripts/ is
    test_stage8_t7_controller_v002.py:246, home.mkdir(mode=0o700) — a
    throwaway GPG keyring home under tempfile.mkdtemp, from the
    since-retired GPG era. mkdir CANNOT change the mode of an existing
    directory (it would raise FileExistsError), and both fenced
    directories already existed. Ruled out on mechanism, not on trust.
  - controller v007 and the manifest builder contain exactly two
    directory modes, 0o555 and 0o755. Never 0o700.
  - the mode changed with NO mtime change (chmod semantics) and no file
    inside either directory was created or modified: work 136 entries,
    provenance 22 entries, production outputs ZERO — all unchanged.
  - probes 9-18 verified writes were BLOCKED at the time of that record,
    which is only possible at 555. The directories genuinely WERE 555.
  THEREFORE an agency OUTSIDE the program's own routes altered the fence
  bits. Most likely a platform agent normalising modes under a synced
  ~/Documents tree. THAT ATTRIBUTION IS A HYPOTHESIS AND IS NOT CLAIMED
  AS ESTABLISHED; what is established is that no program route did it.

WHAT THIS COSTS — and this lane recommended the fence, so it says so
plainly:
  LIMITATION L2 MUST BE RESTATED. The fence bits can be reset with no
  human act and no program route involved. A permission fence in this
  environment is NOT A STANDING BARRIER; it is a barrier that holds only
  as long as nothing outside the program touches it.
  L3 PRE-FLIGHT BECOMES LOAD-BEARING RATHER THAN DEFENSIVE. It asserts
  the at-rest state, drops the fence if it finds it writable, and RECORDS
  the anomaly. That mechanism is now the thing standing between a
  superseded route and a live write — not the bits themselves.
  REVISED RECOMMENDATION ON B3/B4: the directory-permission fence remains
  the cheapest mechanism that closes B3 and B4 together, and the
  rehearsal proves it works when set — but it may be adopted ONLY with
  L3 re-assertion promoted to load-bearing and a re-assertion check that
  does not depend solely on a legitimate invocation happening. Adopting
  it as a passive at-rest barrier would be adopting something this
  environment has already been observed to undo.
TWO ACTS, NEITHER OF THEM THIS LANE'S:
  (1) restore the at-rest state (chmod 555, or one --preflight-only
      invocation once F-2 is closed, which self-heals and records it);
  (2) DECIDE whether an environment that resets these bits unprompted
      permits the fence to stand as the B3/B4 resolution at all.
```

## Rule-3 residual — recorded, not claimed away

```text
Launcher v007 REFUSES controllers v005/v006 and comparator v005, tested
in the strong form (the files exist and are still refused). But launchers
v005/v006 still launch them, and what stops those chains producing
artifacts is THE WRITE FENCE, not a launch fence — and per L1 they remain
executable, so a rogue invocation burns compute and produces nothing.
Under F-3 that reliance is weaker than it looked yesterday. Quarantining
the old launchers needs the principal.
```

## Protected status

```text
cycle7_package_sealed = true
generation_g7_coherent = true
A1_pin_table_rows = 15
A2_real_chain_rehearsal_executed = true      (no stubs, disposable copy)
A4_receipt_ordering_fixed_and_tested = true
B1_fix_verified_empirically = true
fence_adoption_probe = YES_ON_FUNCTION
fence_at_rest_state_self_holding = false     (F-3)
canonical_fence_currently_open = true        (F-3, awaiting restoration)
manifest_v006_sealed_into_provenance = false (F-2, deliberately open)
real_chain_passes = false                    (F-1, BLOCKING)
transported_tolerance_frozen_outcome_blind = true
transported_tolerance_stated_in_sealed_spec = false
production_gate_verdict = NO_GO
production_authorized = false
typed_authorization_recorded = false
alpha_computed = false
proof_authorized = false
```
