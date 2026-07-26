# Stage-8 T7 Directory-Permission Fence — Evaluation and Probe Record V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY_EVALUATION + SEALED PROBE RECORD (probes 9-18)
VERDICT: THE FENCE WORKS. RECOMMENDED FOR ADOPTION IN THE CYCLE-7 PACKAGE.
```

Evaluates the principal's third option for B3/B4: canonical output
directories read-only at rest; controller v006 (current generation,
freely editable) raises write permission as its first gated action after
all pre-flight passes and drops it on exit and on every failure path.

Why it is the right shape: it touches NO frozen file, and directory
permission bits are not hashed by any seal or manifest row — so it is
fully compatible with the byte-freeze whose preservation was the reason
fix (A) was rejected, and with append-only discipline.

## Probe record (all with before/after artifact fingerprints; ZERO WRITES throughout)

At-rest state applied for probing: `stage8_execution/work` and
`provenance` set to mode 555. Fingerprint 29484af48175b353 IDENTICAL
before and after every probe below.

```text
LAUNCHER v002 — ALL NINE ALLOWLISTED TARGETS (the B3 route set):
 9  derive primary v002      PermissionError on
                             '…/T07_…_primary_v001.json.tmp'  BLOCKED
10  derive independent v002  PermissionError on
                             '…_independent_precomparison_v001.json
                              .blocked.tmp'                   BLOCKED
11  compare v002             argparse: required bundle args absent
                             (no write attempted)             no route
12  run_pipeline v002        RuntimeError: implementation signature
                             is absent (.asc gate, probe 8a) BLOCKED
13  test_launcher v002       4/4 PASS (temp dirs only)        no canonical write
14  test_controller v002     6/6 PASS (fixture dirs only)     no canonical write
15  test derive primary v002 PASS                             no canonical write
16  test derive indep. v002  OK                                no canonical write
17  test_compare v002        OK                                no canonical write
V001 ROUTES (B4), invoked directly at their quarantine paths:
18a run_pipeline v001        RuntimeError: pipeline requires the sealed
                             runtime launcher                 BLOCKED
18b compare v001             ComparisonBlocked: comparison requires the
                             sealed Stage-8 runtime launcher  BLOCKED
```

### The finding that matters most

Probe 10 caught the derive lane failing while writing its OWN BLOCKED
artifact (`.blocked.tmp`). That is precisely the B4 defect class — a
chain that "self-blocks" only after a write-capable step — and the fence
stops it before any file exists. **The fence closes B3 and B4 with one
mechanism.**

## Mechanism test (raise / write / drop / verify)

```text
at rest        mode 555
raised         mode 755   -> write succeeds
dropped        mode 555   -> write raises PermissionError
```

The raise/drop cycle behaves exactly as the design requires, and the
post-drop state is verifiably closed rather than merely intended.

## Honest limitations — recorded, not minimised

```text
L1 IT IS A WRITE FENCE, NOT AN EXECUTION FENCE. Probes 9 and 10 show the
   derive lanes RUN their numerics and fail only at the write. No
   artifact is produced, which is what the discipline requires, but a
   rogue invocation still burns compute. Acceptable; recorded.
L2 IT STOPS ROUTES, NOT A HUMAN WITH chmod. Any operator can raise the
   bits by hand. This is the same accepted class as "an operator could
   delete a seal file"; the fence's claim is about ROUTES and must never
   be written up as more.
L3 HARD-KILL WINDOW. If the controller is SIGKILLed between raise and
   drop, the directories stay writable. REQUIRED MITIGATION, to be
   authored with the fence: every controller invocation asserts the
   at-rest read-only state as a PRE-FLIGHT CONDITION and, if it finds
   the directories writable, DROPS them and RECORDS the anomaly before
   proceeding. That makes the invariant self-healing on the next
   invocation, and any legitimate run leaves an auditable trace of why
   the state was open.
L4 CONSTRUCTION-LANE FRICTION. This lane seals manifests into
   provenance/. Under the fence it must raise and drop deliberately,
   with the same discipline as the controller, and record each such
   raise. That friction is a feature, not a defect: it makes every
   canonical write an explicit, logged act.
```

## Required work if adopted (cycle-7 package)

```text
1. Controller v006: raise as the FIRST gated action after ALL pre-flight
   passes; drop in a finally-path AND on every failure path; assert the
   at-rest state in pre-flight per L3 with anomaly recording.
2. The A2 no-stubs rehearsal must exercise the raise/drop cycle end to
   end in a DISPOSABLE workspace copy, and must include a probe that
   LEGITIMATE production still completes through it — the fence is not
   adopted until that probe passes.
3. The fence is recorded as a row in the A1 GENERATION-COHERENCE TABLE
   (at-rest mode; which component may raise; where the drop is
   enforced), so a future generation bump cannot silently orphan it.
4. Probes 9-18 above are sealed here alongside probes 1-8; the
   re-audit consumes them as the B3/B4 evidence.
```

## Recommendation

```text
ADOPT, as the resolution of B3 and B4, subject to the item-2 probe that
legitimate production still works. On the evidence above the fence
converts the live write route into a verified non-route by mechanism
rather than by discipline, satisfies rule 3, touches no frozen file, and
needs no manifest supersession — so the four costly options escalated
earlier (including ending the byte-freeze by decision) can all be
declined.
IF the item-2 probe fails, this lane will report exactly why and the
choice reverts to the principal between time-boxed exposure and holding
production.
```

## At-rest state as of this record

`stage8_execution/work` and `provenance` are LEFT AT MODE 555. Production
is prohibited, so nothing legitimate requires them open; the construction
lane raises/drops explicitly per L4 and records each raise.

## Protected status

```text
directory_permission_fence_probed = true
directory_permission_fence_adopted = false   (pending item-2 probe)
live_write_route_open = false   (mechanically fenced; B3/B4 both closed
                                 by probes 9-18, adoption pending)
production_authorized = false
alpha_computed = false
proof_authorized = false
```
