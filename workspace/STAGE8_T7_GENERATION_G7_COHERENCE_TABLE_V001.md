# Stage-8 T7 Generation G7 — A1 Coherence Table and Cycle-7 Change Record V001

Date: 2026-07-26

## Status

```text
SEALED GENERATION TABLE (one per generation, per A1)
+ CYCLE-7 CHANGE ENUMERATION
+ THREE FINDINGS THIS LANE COULD NOT CLOSE (F-1, F-2, F-3)
PRODUCTION REMAINS PROHIBITED: verdict NO_GO, no typed authorization.
```

Authority: STAGE8_T7_PRODUCTION_GATE_NOGO_AND_PIPELINE_REPAIR_BINDING_V001
(Part A A1-A5, Part B B1/B2/B5 and the MAJORs, Part B' errata),
STAGE8_T7_DIRECTORY_PERMISSION_FENCE_EVALUATION_AND_PROBES_V001 (the fence,
limitations L1-L4, required-work items 1-4), and the standing discipline
STAGE8_REAL_COMPONENT_PRECONDITION_DISCIPLINE_V001 with its rule-4
supplement. All eight of those seals were verified from disk before this
file was authored; none had drifted.

## THE GENERATION TAG

```text
frontier generation tag : stage8_t7_generation_g7
bridge generation tag   : stage8_t7_generation_bridge_v001
```

The file-version numbers differ per component, as they always have. The
GENERATION is the coherence unit, and the mechanical check keys on the tag,
not on a version digit.

```text
G7 MEMBERSHIP (twelve manifest rows + the manifest itself)
  controller              scripts/run_stage8_t7_actual_parent_car_pipeline_v007.py
  launcher                scripts/launch_stage8_t7_content_addressed_runtime_v007.py
  comparator              scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_v006.py
  manifest                provenance/stage8_t7_actual_parent_regulated_car_operator_response_implementation_v006.json
  controller_test         scripts/test_stage8_t7_controller_v007.py
  launcher_test           scripts/test_stage8_t7_launcher_v007.py
  comparator_test         scripts/test_compare_stage8_t7_actual_parent_regulated_car_operator_response_v006.py
  rehearsal_test          scripts/test_stage8_t7_real_chain_rehearsal_v001.py
  manifest_builder        scripts/build_stage8_t7_actual_parent_car_implementation_manifest_v006.py
  derive_primary          scripts/derive_..._primary_v002.py          (byte-frozen, SHARED)
  derive_independent      scripts/derive_..._independent_v002.py      (byte-frozen, SHARED)
  derive_primary_test     scripts/test_..._primary_v002.py            (byte-frozen, SHARED)
  derive_independent_test scripts/test_..._independent_v002.py        (byte-frozen, SHARED)

BRIDGE MEMBERSHIP (the sealed v001-path manifest's own row set; frozen
forever, and the ONLY generation the byte-frozen derive lanes may name)
  manifest    provenance/..._implementation_v001.json  f573ae21…
  controller  scripts/run_..._pipeline_v002.py
  launcher    scripts/launch_..._runtime_v002.py
  comparator  scripts/compare_..._v002.py
  + the v002 test rows and the four SHARED byte-frozen rows above
```

## THE A1 COHERENCE TABLE — every generation pin that exists today

Built by READING THE ENFORCEMENT POINTS on disk, never by re-deriving
intent (A3). "read as" is how the mechanical check obtains the pin: source
pins are parsed with `ast` out of the file's own bytes (no import, no exec),
manifest pins are read out of the manifest JSON.

```text
ID   PIN                              LIVES IN            READ AS                       GENERATION  MUST NAME
P01  controller launcher pin          controller v007     RUNTIME_LAUNCHER              frontier    launcher v007
P02  controller manifest pin          controller v007     IMPLEMENTATION_MANIFEST       frontier    manifest v006
P03  controller bridge manifest pin   controller v007     BRIDGE_MANIFEST               bridge      manifest v001
P04  controller lane targets          controller v007     TARGETS                       frontier    derive v002 x2 + comparator v006
P05  controller generation membership controller v007     GENERATION_MEMBERS            frontier    all thirteen G7 members
P06  launcher allowlist               launcher v007       ALLOWED_TARGETS               frontier    the eleven launchable G7 rows
P07  comparator manifest pin          comparator v006     IMPLEMENTATION_MANIFEST       frontier    manifest v006
P08  comparator launcher pin          comparator v006     RUNTIME_LAUNCHER_PATH         frontier    launcher v007
P09  comparator bundle-binding pin    comparator v006     BUNDLE_BINDING_MANIFEST       bridge      manifest v001
P10  comparator executor paths        comparator v006     EXECUTOR_PATHS                frontier    derive v002 x2
P11  frontier manifest row set        manifest v006       @rows                         frontier    the twelve G7 rows exactly
P12  bridge manifest row set          manifest v001       @rows                         bridge      the ten v002-era rows exactly
P13  derive primary manifest pin      derive primary v002 IMPLEMENTATION_MANIFEST       bridge      manifest v001
P14  derive independent manifest pin  derive indep. v002  IMPLEMENTATION_MANIFEST       bridge      manifest v001
P15  DIRECTORY-PERMISSION WRITE FENCE (not a path pin; see its own row below)
```

Every pin is an EXACT pin: the set of component paths it names, restricted
to the classified component families, must EQUAL that generation's members
of the families the pin declares. Three failure modes therefore block:
a pin naming a foreign generation's member (the lagging pin), a pin naming
an extra generation's member (a cross-generation pin — the B1 wedge), and
a pin that has stopped naming a required family (an orphaned row).

### P15 — the fence row (fence record required-work item 3)

```text
at-rest mode        0555 on stage8_execution/work AND provenance
raised mode         0755, and only inside a controller-v007 lane invocation
who may raise       scripts/run_stage8_t7_actual_parent_car_pipeline_v007.py
                    scripts/build_stage8_t7_actual_parent_car_implementation_manifest_v006.py
                      (construction lane, ONLY under --l4-raise-and-record,
                       which records the raise; it can create the manifest
                       and its seal at one fixed path and nothing else)
where the drop is   main(): the finally path around every lane invocation
enforced            main(): SIGINT / SIGTERM / SIGHUP handlers
                    preflight_fence_at_rest(): the L3 self-heal
limitations kept    L1 write fence not execution fence; L2 an operator with
                    chmod defeats it; L3 SIGKILL leaves it open until the
                    next invocation self-heals; L4 construction-lane friction
```

## THE SIX-CYCLE DEFECT, AS FOUND ON DISK BEFORE THIS CYCLE

Recorded as data, because it is the reason the table exists:

```text
controller v006 : launcher v006 (2b7bd64a…)  manifest v005 (9f80aa63…)
comparator v005 : launcher v005 (7e7b9179…)  manifest v004 (187a0435…)
                  ^^^^^^^^^^^^^ ONE PIN, ONE BUMP BEHIND
manifest v005 has NO launcher-v005 row  (erratum E-1 confirmed from disk)
manifest v004 launcher row = launcher v005
```

Reproduced empirically in a disposable workspace copy before any repair was
authored: the two real derive lanes under launcher v006 produced valid
bundles, and the real comparator v005 sealed
`ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_BLOCKED` with reason
`independent runtime-launcher provenance mismatch` at the canonical
comparison path, in 0.7 s, before touching a single number. That is the
wedge, observed rather than argued.

## CYCLE-7 CHANGES, ENUMERATED (no "sole change" claims)

```text
launcher v007  ALLOWLIST REPOINT — A FUNCTIONAL CHANGE.
  added   controller v007, comparator v006, test_controller v007,
          test_launcher v007, test_compare v006, the rehearsal suite,
          the manifest builder
  removed controller v005, controller v006, comparator v005,
          test_controller v005/v006, test_launcher v005/v006,
          test_compare v005
  consequence, stated plainly: launcher v007 CANNOT launch controller v005
  or v006 or comparator v005. Those remain launchable under launcher v005
  and v006, which are untouched. The docstring says exactly that and
  repeats no disarm claim (erratum E-3).
comparator v006  four changes: manifest pin -> v006; launcher pin -> v007
  (functional); the PROVENANCE PROLOGUE hoisted out of the try that seals a
  BLOCKED verdict; the stale v005-era launcher-authority comment corrected.
  Byte-identity outside those four is asserted AND tested.
controller v007  five changes: the G7 repoints (three pins + the row set);
  the A1 coherence check; the write fence (raise / drop / L3 self-heal /
  signal handlers); the A4 receipt-order fix; the comparator-authority
  hoist. Preconditions grow from ten to thirteen.
manifest v006 + its builder  the builder READS the row set out of
  controller v007's frozen table rather than carrying a hand-typed list,
  because a hand-typed list in a builder is exactly the shape that produced
  six one-pin lags.
```

## SUITE RESULTS (all run at the sealed byte state of this cycle)

```text
test_stage8_t7_launcher_v007.py                     6/6   PASS
test_stage8_t7_controller_v007.py                  10/10  PASS
test_compare_..._v006.py                            5/5   PASS
test_stage8_t7_real_chain_rehearsal_v001.py         see below
```

## A2 REHEARSAL — the only accepted startability evidence

No stubs, no monkeypatches, no source substitution: the real launcher v007
driving the real controller v007 driving the real byte-frozen v002 derive
lanes and the real comparator v006, end to end, in a disposable workspace
copy that starts at the canonical at-rest fence state. 184 s.

```text
L4 construction-lane manifest build   OK, raise recorded, fence dropped
superseded-route probe (B3's route):
  launcher v002 -> derive independent v002, fence at rest
  -> PermissionError on '…independent_precomparison_v001.json.blocked.tmp'
  -> returncode 1, ZERO artifacts                        BLOCKED BY MECHANISM
--preflight-only                       PREFLIGHT_OK (recorded, NOT evidence)
lane independent   84.6 s  SUCCEEDED   fence raised, wrote 2 outputs +
                                       receipt, dropped, verified closed
lane primary       11.2 s  SUCCEEDED   fence raised, wrote 2 outputs +
                                       receipt, dropped, verified closed
lane comparison     2.6 s  BLOCKED     fence raised, comparator wrote its
                                       sealed verdict, dropped, verified
                                       closed; NO RECEIPT SEALED (A4 held
                                       in the real chain)

FENCE ADOPTION PROBE (fence record item 2)            ANSWER: YES
  every lane raised and dropped both directories        true
  every lane wrote its artifacts through the raised fence true (all three)
  fence verified closed after every lane, by ATTEMPTING A WRITE  true
  superseded route wrote nothing                        true

PIPELINE VERDICT                                       NOT A PASS
  ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_BLOCKED
  reason: "34 component comparison(s) failed"
```

The two are reported separately on purpose. The fence, the generation
coherence, the launcher, both manifests, the receipt ordering and both
derive lanes all behaved as designed. The pipeline verdict is a COMPARATOR
RESULT, and it is finding F-1.

## F-1 — THE FIRST FINDING THIS LANE CANNOT CLOSE (BLOCKING for production)

```text
The real chain, executed end to end for the FIRST time in this program,
does NOT produce the Phase-A PASS verdict. 34 of 157 component comparisons
exceed their preregistered budget.

  failing categories   propagators (10), cross_operators (24)
  budget               TRANSPORTED_MATRIX_TOLERANCE = 3.0e-4
                       (operator 2-norm, transported comparisons)
  worst failure        8.411e-4   = 2.80 x budget
  typical failure      4.206e-4   = 1.40 x budget
  by oscillator length ell0: 28 failures, worst 8.411e-4
                       ell1:  6 failures, worst 3.281e-4
  passing transported rows: 104, worst margin 2.941e-4 — i.e. the whole
  transported population sits AT the budget scale, not comfortably inside it
  reproducible         bit-for-bit identical failure set across two
                       independently produced bundle pairs (one built under
                       launcher v006, one under launcher v007)

WHY THIS IS NOT A PLUMBING DEFECT AND NOT MINE TO FIX
  - the derive lanes are byte-frozen; the comparator's numerics in v006 are
    byte-identical to v005 (tested); the budgets are v002-era constants,
    frozen outcome-blind and explicitly "not revisable after any production
    value exists"; I introduced no measured constant.
  - the same failure would occur under ANY coherent generation. It was
    invisible until now for exactly the reason Part B item B2 names: the
    production combination executed in NO test on disk. B2 is hereby
    confirmed with teeth, by execution rather than by inspection.

WHY IT IS BLOCKING FOR PRODUCTION, not merely open
  A comparator content failure IS a verdict, so the comparator seals it at
  the canonical comparison path by design — and my prologue hoist covers
  PROVENANCE conditions only, deliberately and on the record. Therefore:
  THE FIRST CANONICAL PRODUCTION COMPARISON RUN WILL PERMANENTLY CONSUME
  THE CANONICAL COMPARISON PATH WITH A BLOCKED VERDICT, and we now know
  this in advance rather than discovering it afterwards. Production must
  not be authorized until the transported-budget question is adjudicated by
  the principal. The disposition is a scientific one — is 3.0e-4 the right
  budget for a 48-step / 10-10-20-quadrature lane against a 384-step /
  12-12-24 lane, or is the discrepancy real? — and it is NOT a disposition
  this lane may make by editing a tolerance.
```

## F-2 — THE SECOND FINDING THIS LANE CANNOT CLOSE (procedural)

```text
manifest v006 IS NOT SEALED INTO THE CANONICAL provenance/ DIRECTORY.
The fence is live: provenance is mode 555 at rest, and this lane's
instructions forbid chmod of any canonical directory. Sealing the manifest
therefore requires ONE explicit authorized L4 raise:

  <pinned python> -I -S \
    scripts/launch_stage8_t7_content_addressed_runtime_v007.py \
    scripts/build_stage8_t7_actual_parent_car_implementation_manifest_v006.py \
    --l4-raise-and-record

The builder raises provenance, writes the manifest and its seal, drops the
fence, and prints the L4 raise record. Until that is run, controller v007
blocks precisely at the implementation_manifest precondition naming the
absent manifest — fail-closed, by design, and the same shape controller
v006 documented for manifest v005. The builder was exercised for real in
every disposable copy used by the suites and by the rehearsal (twelve rows,
fence dropped afterwards, verified).

Row hashes as of this seal (what the manifest will contain):
  4269de1aa6f7e92a  scripts/build_..._implementation_manifest_v006.py
  d0d5f5cdb2690a7a  scripts/compare_..._v006.py
  1098168c47e59ae7  scripts/derive_..._independent_v002.py
  402d3e988037fa47  scripts/derive_..._primary_v002.py
  316ed7433e88b08b  scripts/launch_..._runtime_v007.py
  a2fc4fe43a326f73  scripts/run_..._pipeline_v007.py
  c9c0c5b28b34e067  scripts/test_compare_..._v006.py
  aa04ff9a8f783da2  scripts/test_..._independent_v002.py
  73534e5a34571dc7  scripts/test_..._primary_v002.py
  d170b042aeb36cb9  scripts/test_stage8_t7_controller_v007.py
  c7128b79ca6d5d13  scripts/test_stage8_t7_launcher_v007.py
  767eaa81111b2695  scripts/test_stage8_t7_real_chain_rehearsal_v001.py
```

## F-3 — THE FENCE'S AT-REST STATE WAS ALTERED FROM OUTSIDE THE PIPELINE

```text
OBSERVED, at the end of this cycle, at the CANONICAL root:

  stage8_execution/work   mode 0700 (drwx------)  ctime 2026-07-26 09:07:04
  provenance              mode 0700 (drwx------)  ctime 2026-07-26 09:07:04

The at-rest mode of record is 0555. Mode 0700 is OWNER-WRITABLE, so the
canonical fence is presently OPEN. Both directories changed in the SAME
SECOND, and no other directory in the tree changed.

THIS LANE DID NOT DO IT, and the evidence is mechanical rather than an
assurance:
  - controller v007 and the manifest builder contain exactly two directory
    modes, 0o555 and 0o755. Neither is 0o700. Nothing in this cycle can
    produce 0700.
  - every chmod in every cycle-7 test is workspace-COPY relative, and each
    loader asserts `module.ROOT == workspace` before any fence call, so a
    test cannot have addressed the canonical directories.
  - the fenced directories contain NO file created or modified after
    2026-07-26 08:45 and no stray .tmp or probe file; the artifact counts
    are unchanged (provenance 22, work 136) and production outputs remain
    ZERO. Nothing was written through the open fence.

WHAT IT MEANS. Fence limitation L2 was recorded as "it stops routes, not a
human with chmod". This is a strictly wider case: a PLATFORM AGENT (the
tree lives under a synced ~/Documents hierarchy, where 0555 directories are
routinely normalised) can reset the bits with no human and no route
involved. L2 must be restated in those terms; the fence's claim is about
ROUTES and about nothing else, and its at-rest state is NOT self-holding in
this environment.

WHY THIS MAKES L3 LOAD-BEARING RATHER THAN DEFENSIVE. The required L3
mitigation — assert the at-rest state in pre-flight, drop it, and RECORD
the anomaly — is now known to fire against a real, recurring, non-hostile
cause, not only against a hard kill. Controller v007's
preflight_fence_at_rest will drop 0700 to 0555 and record the anomaly in
its pre-flight JSON and in the lane receipt on the next invocation.

NOT CLOSED BY THIS LANE, and deliberately so: restoring the bits is a
chmod of a canonical directory, which is outside this lane's authority.
Two actions are needed and neither is mine:
  (a) restore the at-rest state (`chmod 555` on both, or one
      --preflight-only invocation of controller v007, which self-heals and
      records it — but that requires manifest v006, i.e. F-2 first); and
  (b) decide whether an environment that resets these bits on its own
      permits the fence to be adopted as the B3/B4 resolution at all, or
      whether the fence needs a periodic re-assertion rather than a
      per-invocation one.
```

## RULE-3 DISPOSITION FOR THE SUPERSEDED v005/v006 CHAINS

Discipline rule 3 requires a superseded chain's launch route to be removed
mechanically in the same change. This lane may not quarantine v005/v006
(no authorization, and new files only), so the disposition is recorded
honestly rather than claimed away:

```text
launcher v007 refuses them          (allowlist; tested, strong form: the
                                     files EXIST and are still refused)
launcher v005 / v006 still launch them  (unchanged; not claimed otherwise)
they cannot WRITE anything          (the fence: work and provenance are 555
                                     at rest and only controller v007
                                     raises them — tested end to end by the
                                     rehearsal's superseded-route probe)
RESIDUAL, on the record             they remain EXECUTABLE (fence L1), so a
                                     rogue invocation burns compute and
                                     produces nothing. Closing that needs a
                                     quarantine decision from the principal.
```

## PROTECTED STATUS

```text
production_gate_verdict = NO_GO
production_authorized = false
generation_coherence_invariant_adopted = true
generation_coherence_check_authored = true
real_chain_rehearsal_authored = true
real_chain_rehearsal_pipeline_verdict = BLOCKED   (F-1)
directory_permission_fence_adopted = true         (item-2 probe: YES)
live_write_route_open = false                     (mechanically fenced WHEN
                                                   the fence is at rest; see
                                                   F-3 — it is NOT at rest
                                                   right now)
canonical_fence_at_rest = false                   (F-3, mode 0700 observed)
manifest_v006_sealed = false                      (F-2, awaiting one L4 raise)
alpha_computed = false
proof_authorized = false
```
