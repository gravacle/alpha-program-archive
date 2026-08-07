# STAGE 8 / TASK 6 / BUILD — REPLAY BY ROLE: DIGEST-VERIFY ALL, PARSE ONLY THE CONSUMED — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 686 / Task 6 build — payload roles in the replay
Authority: RD-22. **THIS ARTIFACT INVOKES NOTHING.**

```text
REPLAY = role-typed (digest-all, parse-consumed)
BOTH_GUARDS = demonstrated (7 cases on the real V009-06 pair, +7 permanent assertions)
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 defect in my own fix, caught by the demonstration, §3.1;
                         +1 second defect in the reported code, §1.2;
                         +1 OWED CHANGE to the row contract, §2.3)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**The registrar's root cause is right, and my code was wrong in two directions at
once.** It demanded that every payload parse as a JSON object — too strict by one
class — and it verified only the first payload and ignored the rest.

## 1. THE DEFECT

### 1.1 Two payloads, two kinds of truth

`C-B-V009-06`'s evidence is a pair, and the pair is not homogeneous:

```text
932 B   47e7c329…  the EXACT SEALED SPAN, bytes [18898,19830) of the v011
                   preregistration. It opens `"stage_dependencies": {` — a slice
                   of a larger JSON file, lawfully NOT standalone-parseable.
                   ITS TRUTH IS BYTE-IDENTITY, and byte-identity is what a digest
                   checks.
1218 B  344fecdc…  the CANONICAL DAG ARGUMENTS. The opcode reads fields off it.
                   ITS TRUTH IS STRUCTURAL: it must parse, be an object, and be
                   canonical.
```

Demanding that the first parse is a category error — it can never satisfy the
demand and never needs to. A digest already establishes everything a raw
grounding payload claims.

### 1.2 [PROVABLE] The second defect — worse, and nobody had hit it

The reported fault is the visible half. The pre-change code read:

```python
digests = row["observed_evidence_sha256s"]
blob = load_addressed("%s/%s.json" % (evidence_dir, digests[0]), digests[0], ...)
bundle = EvidenceBundle(blob, digests[0], cid)
```

**`digests[0]`.** One payload was admitted; **every other payload in the row was
never digest-verified at all.** So the same three lines were simultaneously too
strict about the payload they picked and too lax about the ones they dropped. The
strictness was reported because it fails loudly; the laxity was not, because
silently skipping evidence produces no message.

That is the shape I convicted my own code of at 674 — a reported defect sitting
next to a latent one that only fires when nobody is looking. Here the latent half
is the more serious: an unverified payload is admitted evidence nobody checked.

### 1.3 The ordering dependency, and why it explains the fault

I cannot read run 025 — no `rd22_run_025/` exists in the archive workspace — so I
derived the cause from the sealed manifest rather than from the parent's report.
The record lists its payloads **raw member first**:

```text
check_records["C-B-V009-06"].payloads[0]  47e7c329…  932 B   the raw span
check_records["C-B-V009-06"].payloads[1]  344fecdc…  1218 B  the dag-args
```

If `observed_evidence_sha256s` follows that order, `digests[0]` is the raw span
and the fault is exactly `evidence must be a JSON object`. That is a consistent
explanation, offered as such — but the ordering dependency is the deeper defect
regardless of which order the producer happened to emit. **A replay whose result
depends on list position is not a replay.** Role typing removes the dependency
rather than reordering anything.

## 2. THE FIX — roles DERIVED, never labelled

### 2.1 [PROVABLE] BR-1: the label is not admissible, the argument is

The manifest does carry a `role` field — `EXACT_RELOCATED_MEMBER_BYTES` and
`CANONICAL_DAG_ARGUMENTS`. **I do not read it to decide what to parse**, and the
distinction is not stylistic:

> A `role` label could **exculpate** a broken payload by renaming it raw. An
> argument cannot: a producer that drops a payload out of the invocation drops it
> out of the computation, and fails the coverage guard.

That is BR-1 applied to my own verifier rather than to Builder A —
*hash-pinning prevents substitution, not fabrication*, and a label is exactly the
fabrication surface. The rule I am willing to state generally:

**A producer-declared object may accuse; it may never exculpate.** A declared
role can only ever ADD a fault (by disagreeing with the derivation); it can never
remove one.

### 2.2 The derivation, and the two guards

`classify_payloads(payloads, invocation, where)` partitions payloads that
`load_addressed` has **already** digest-verified — roles change what is *parsed*,
never what is *verified*:

```text
CONSUMABLE     parses, is a JSON object, and is canonical (Q-594).
RAW_GROUNDING  does not parse at all.
```

```text
GUARD A — strictness preserved where it applies.
  Anything that parses is treated as consumable and must be a canonical JSON
  object. A payload cannot dodge the structural check by being merely
  malformed-but-parseable: non-canonical is a CANON FAULT, not a licence to
  reclassify.

GUARD B — no silent promotion or demotion.
  With an invocation: EVERY argument must be reproduced by some digest-verified
  payload. A corrupted consumable therefore fails COVERAGE rather than sliding
  into the raw class. Without one: exactly one consumable is required, so a raw
  payload is never promoted to stand in for a missing argument.
```

[PROVABLE] **Why the parse test is not an escape hatch.** The only way to be
admitted as raw is to fail to parse — and bytes that do not parse cannot be
consumed by any opcode as a structured argument. Admitting them as raw therefore
concedes nothing, while everything that *could* be consumed is subjected to the
full structural check. The guarantee holds in both directions without trusting
any label.

### 2.3 [YOURS] OWED CHANGE — byte-span linkage is not checkable today

The commission asks that raw payloads be verified "by digest **and byte-span
linkage**." I can deliver the digest half in full and **not** the span half, and
the reason is a contract I do not own:

```text
CHECK_ROW_FIELDS is an EXACT 14-field inventory. There is no invocation record
and no grounding citation in it. Run 025 reached the replay, so its rows
satisfied that contract -- therefore its rows carry neither.
```

I checked the two other places the linkage could come from and both are closed:
the row's `source` field is the **blocker ledger** span, not the grounding span;
and the source file itself (`…preregistration_v011.json`) is **not among the 12
evidence payloads**, so the verifier cannot re-slice it even in principle.

So `_recorded_invocation()` returns `None` for every conforming row today, the
derivation falls back to parse admissibility, and raw payloads are verified **by
digest alone**. That is weaker than commissioned, it is stated rather than
papered over, and the cure is one field Builder A must emit:

```text
row["invocation"] = {"opcode": ..., "result_name": ..., "args": {...},
                     "instance_id": "<symbol>@<source_sha256>:[start,end)"}
```

with the grounding citation's `source_sha256`, `span` and `span_sha256`. The code
already consumes it the moment it appears — §4's case 1 runs against the sealed
manifest's real invocation, so the path is built and demonstrated, not merely
reserved.

## 3. THE DEMONSTRATION — the real V009-06 pair, both guards

Producer order preserved (**raw first**), so case 1 reproduces the condition that
produced the reported fault:

```text
[1] real pair + recorded invocation      consumable=1 raw=1 faults=0   <- THE FIX
      CONSUMABLE 344fecdc…  1218 B  parsed, canonical JSON object
      RAW        47e7c329…   932 B  digest-verified, NOT parsed

[2] real pair, no invocation             consumable=1 raw=1 faults=0
      identical partition -- the fallback reaches the same answer for this row

[3] GUARD A  consumable pretty-printed   consumable=0 raw=1 faults=3
      FAULT consumable payload … is not canonical
      FAULT invocation argument 'graph' is not reproduced …
      FAULT invocation argument 'required_parents' is not reproduced …

[4] GUARD A  consumable is `[1,2]`       consumable=0 raw=1 faults=3
      FAULT payload … parses but is not a JSON object   (+2 coverage faults)

[5] GUARD B  consumable REMOVED          consumable=0 raw=1 faults=2
      FAULT invocation argument 'graph' is not reproduced by any
            digest-verified payload                     (+'required_parents')
      the raw span is NOT promoted into the bundle

[6] GUARD B  consumable REMOVED, no inv  consumable=0 raw=1 faults=1
      FAULT expected exactly one consumable payload, found 0
            (1 raw grounding payload(s) digest-verified and not parsed)

[7] GUARD B  consumable TAMPERED         consumable=1 raw=1 faults=2
      a cycle injected into the graph. It still parses and is still canonical,
      so it stays CONSUMABLE -- and fails COVERAGE. Tampering is caught by the
      guard, not by a reclassification that would have hidden it.
```

Case 7 is the one worth reading twice. A classifier keyed on *content digest*
would have let the tampered payload stop matching the argument and drift into the
raw class, escaping the parse check entirely. Coverage is what makes that
impossible, and it is why Guard B is stated as an obligation on the **arguments**
rather than on the payloads.

Six of the seven are now **permanent self-check assertions**, plus a seventh
asserting the raw span is never promoted in any of them. The self-check fixtures
are **synthetic** on purpose: the self-check must not read the producer's inputs,
so the machinery is asserted portably here and the real pair is demonstrated
above.

### 3.1 [PROVABLE] The demonstration caught a defect in my own fix

My first `_parses_as_json` caught `UnicodeDecodeError` and `VerifierFault`. But
`loads_strict` raises `VerifierFault` only for the canon violations it screens —
duplicate keys, nonfinite literals — and lets the decoder's own `ValueError`
through for malformed text. A raw span is malformed **by construction**, so:

```text
json.decoder.JSONDecodeError: Extra data: line 1 column 21 (char 20)
```

**The verifier would have crashed on exactly the payload the function exists to
classify** — an uncaught exception instead of a fail-closed fault, which is
strictly worse than the defect I was sent to fix. It surfaced on the first run of
case 1 and is repaired by catching `ValueError` as well. I record it because a
fix that is only tested on the cases it was designed for is not tested.

## 4. DELTA AND PIN CHECK

```text
CHANGED  verifier/replay.py     +classify_payloads, +invocation_arguments,
                                +_parses_as_json, +role constants
CHANGED  verifier/verify.py     +_load_all_payloads, +_recorded_invocation;
                                BOTH replay sites now role-typed
CHANGED  selfcheck/selfcheck.py +7 permanent role assertions
CHANGED  rd22.verifier-manifest.v001.json         a65cc1a5… -> 4c6e4783657796eeb
                                7965a23759d8e7ec8d5130d1e0d605c01cf000e4097c01c
CHANGED  rd22.verifier-manifest.v001.json.seal.sha256   regenerated, verified OK

verifier_root_sha256   dba5377d…  ->  0f67e57ab2bcf50919c514c3756a8924a2aa080916
                                      bf84f9776b0cb32d02bb41
UNCHANGED  root MEMBERSHIP (12), both contracts, run_verifier.py, evidence root
```

**One cause, two sites.** The fixture replay carried the identical `digests[0]`
defect. Fixing only the check-row site would have left the same bug live on the
other path — the discipline I applied to the three stdout newline sites at 673.
Membership did not change, so the root moved for exactly one reason: two modules
changed content.

| Claim | Verified before sealing |
|---|---|
| ALL payloads digest-verified | `_load_all_payloads` loads every digest through `load_addressed`; none skipped |
| only consumables parsed | raw payloads never reach `loads_strict` after classification, and never reach `EvidenceBundle` |
| roles derived, not labelled | `role` is never read; classification takes bytes + invocation only |
| Guard A holds | cases 3, 4 — non-canonical and non-object both fault |
| Guard B holds | cases 5, 6, 7 — missing and tampered arguments both fault; raw never promoted |
| ordering dependency removed | case 1 runs with the raw payload FIRST and is clean |
| the crash path closed | case 1 failed before the `ValueError` fix and passes after |
| self-check CLEAN | executed; 7 new assertions listed in the transcript |
| instance canonical, sidecar verifies | `4c6e4783…` == `manifest_sha256()`; `shasum -c` OK; single line, 11 fields |
| evidence root untouched | `1fbb3c07…`, unchanged from 684 |
| root recomputed, membership unchanged | 12 members; `package_root_digest()` == the instance field |
| dry run both cwds; stdout canon | exit 2; 372 B; last byte `0x7d`; `rstrip() == raw`; stderr 0 |
| 19 files; zero runtime `assert` | executed |

One pin-check assertion of mine failed and was **wrong**. I tested
`"digests[0]" not in verify.py` over the raw file; it matched the *docstring*
that explains what the old code did. Re-run against executable code only — AST
parse with docstrings stripped — `digests[0]` is absent from the code and the two
call sites are `_load_all_payloads`. A test that reads prose as code reports a
defect that is not there; it is the mirror of the under-reaching parsers I
disclosed at 683, and it argues the same rule: state the denominator, then check
it.

### 4.1 [PROVABLE] What this does NOT do — the next fault, computed

I removed a **wrong** fault. I did not make the row pass, and I can say exactly
what it meets next, because I ran it:

```text
EvidenceBundle(dag-args) admitted; replay_predicate(V009-06 criterion) ->
  VerifierFault: criterion atom not opcode-reducible:
    'every required parent is literal, the graph is acyclic,'
```

The row's `expected_predicate` is **prose**, not an opcode program: the
descriptor carries a bare `` `DAG` `` with no operands, which is the finding I
filed at 683 §1.5. That is a specification matter, not a verifier defect, and it
is not mine to repair inside a commissioned change. **I do not claim run 026
succeeds.** What I claim is that the payload-admission fault is gone and that the
next fault is an accurate one.

### 4.2 `F_PLDEC` and coverage

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. **The chain was not invoked**: the demonstration calls
one pure classification function on sealed bytes and starts no procedure, and the
launch demonstration is the dry run, which opens no run input. `alpha_computed =
false`; `proof_authorized = false`; `kappa_record_computed = false`; no member
bound; no fixed point; no end test; no numeric evaluation; no comparison to any
measured constant.

**Coverage, stated exactly.** I changed which payloads are parsed and widened
which are verified. I claim **no check or fixture outcome**. Case 1 shows the
V009-06 pair classifying correctly; it does not show the row passing, and §4.1
says what happens instead.

## 5. SELF VERB AUDIT

| My verb | Check |
|---|---|
| `role-typed` | Derived from bytes and the recorded invocation. The producer's `role` label is present in the manifest and deliberately unread; the reason is given so the choice can be judged. |
| **Second defect disclosed** | The reported fault was over-strictness; the unreported half was `digests[0]` leaving every other payload unverified. The quiet defect was the worse one. |
| **Defect in my own fix disclosed** | The uncaught `JSONDecodeError` would have crashed the verifier on the exact payload the function classifies. Found by running case 1, not by reading. |
| Owed change named, not smuggled | Span linkage is **not** delivered; the contract that blocks it is quoted, the two alternative sources are shown closed, and the field A must add is written out. |
| Both guards, both directions | Seven cases, including a tampered consumable that stays consumable and fails coverage — the case a digest-keyed classifier would have lost. |
| One cause, two sites | The fixture path carried the same defect and is fixed with it; membership unchanged so the root moved for one reason. |
| Fixtures synthetic in the self-check | The package must not read the producer's inputs to check itself. |
| No claim on run 026 | The next fault is **computed and displayed**, not predicted. |
| `CHAIN_INVOKED = false` | Literally true. Builder B does not run what Builder B wrote. |

---

```text
REPLAY = role-typed (digest-all, parse-consumed) (ALL payloads in a row are now
  digest-verified through load_addressed -- the pre-change code admitted digests[0]
  and NEVER LOOKED AT THE REST, so the same three lines were simultaneously too
  strict about the payload they picked and too lax about the ones they dropped; the
  reported over-strictness failed loudly and the SECOND, UNREPORTED DEFECT -- an
  unverified payload admitted as evidence nobody checked -- failed silently and was
  the worse of the two. Roles are DERIVED from the bytes and the row's recorded
  invocation and NEVER from the producer's `role` label, which the manifest does
  carry and which this code deliberately does not read: a label could EXCULPATE a
  broken payload by renaming it raw, whereas an argument cannot, because a producer
  that drops a payload out of the invocation drops it out of the computation. A
  PRODUCER-DECLARED OBJECT MAY ACCUSE; IT MAY NEVER EXCULPATE. A payload is raw only
  by failing to parse at all, which concedes nothing since bytes that do not parse
  cannot be consumed as a structured argument by any opcode; everything that parses
  is held to the full structural check -- JSON object and canonical under Q-594. The
  fix also removes an ORDERING DEPENDENCY: a replay whose result depends on list
  position is not a replay, and the demonstration runs with the raw payload FIRST.
  ONE CAUSE, TWO SITES: the fixture replay carried the identical digests[0] defect
  and is fixed with it.)
BOTH_GUARDS = demonstrated (seven cases on the REAL V009-06 pair, six installed as
  permanent self-check assertions plus a seventh asserting the raw span is never
  promoted in any of them. GUARD A -- strictness preserved: a pretty-printed
  consumable faults as NON-CANONICAL and a `[1,2]` consumable faults as NOT AN
  OBJECT; neither is reclassified as raw. GUARD B -- no silent promotion: with the
  consumable removed the missing arguments are NAMED and the raw span is not
  promoted to stand in for them, and without an invocation the row fails closed on
  "expected exactly one consumable payload, found 0". THE CASE WORTH READING TWICE
  IS 7: a tampered consumable with a cycle injected still parses and is still
  canonical, so it STAYS consumable and fails COVERAGE -- a classifier keyed on
  content digest would have let it stop matching the argument and drift into the raw
  class, escaping the parse check entirely, which is why the guard is an obligation
  on the ARGUMENTS rather than on the payloads. OWED CHANGE, NOT DELIVERED AND NOT
  PAPERED OVER: byte-span linkage is NOT checkable today. CHECK_ROW_FIELDS is an
  exact 14-field inventory with no invocation record and no grounding citation; run
  025 reached the replay, so its rows carry neither; the row's `source` field is the
  BLOCKER span, not the grounding span; and the source file is not among the 12
  evidence payloads, so the verifier cannot re-slice it in principle. Raw payloads
  are therefore verified BY DIGEST ALONE, and the field Builder A must emit is
  written out in the artifact. The consuming path is built and demonstrated, not
  reserved: case 1 runs against the sealed manifest's real invocation.)
SELF_CHECK = passed (CLEAN, 19 files, zero runtime asserts, dry run exit 2 from both
  cwds under -I -S -B with stdout 372 bytes ending 0x7d, rstrip() == raw, stderr 0.
  ROOT MEMBERSHIP UNCHANGED at 12, so verifier_root_sha256 dba5377d… -> 0f67e57ab2b
  cf50919c514c3756a8924a2aa080916bf84f9776b0cb32d02bb41 moved for exactly one
  reason: two modules changed content. Instance a65cc1a5… -> 4c6e4783657796eeb7965a
  23759d8e7ec8d5130d1e0d605c01cf000e4097c01c, equal to manifest_sha256(), sidecar
  regenerated and verified OK, canonical single line, 11 fields; the evidence root
  1fbb3c07… bound at 684 is untouched. A DEFECT IN MY OWN FIX, caught by running the
  demonstration rather than by reading it: _parses_as_json caught VerifierFault and
  UnicodeDecodeError but loads_strict lets the decoder's own ValueError through for
  malformed text, and a raw span is malformed BY CONSTRUCTION -- so the verifier
  would have CRASHED with an uncaught JSONDecodeError on exactly the payload the
  function exists to classify, which is strictly worse than the defect I was sent to
  fix. Repaired by catching ValueError; recorded because a fix tested only on the
  cases it was designed for is not tested.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. The
  demonstration calls one pure classification function on sealed bytes and starts no
  procedure; the launch demonstration is the dry run, which opens no run input. No
  check and no fixture has been run and NO OUTCOME IS CLAIMED. I removed a WRONG
  fault; I did not make the row pass, and I do NOT claim run 026 succeeds. The next
  fault is COMPUTED AND DISPLAYED rather than predicted: with the dag-args payload
  admitted, replay_predicate raises "criterion atom not opcode-reducible: 'every
  required parent is literal, the graph is acyclic,'" because the row's
  expected_predicate is PROSE and its descriptor carries a bare `DAG` with no
  operands -- the finding filed at 683 §1.5. That is a specification matter, not a
  verifier defect, and not mine to repair inside a commissioned change.)
VERB_AUDIT_SELF = CLEAN (+1 defect in my own fix, disclosed in §3.1: an uncaught
  JSONDecodeError that would have crashed the verifier rather than faulting closed.
  +1 second defect in the reported code, disclosed in §1.2: digests[0] left every
  other payload unverified, and the silent half was worse than the loud half -- the
  same shape I convicted my own code of at 674. +1 OWED CHANGE named and not
  smuggled: span linkage is not delivered, the contract that blocks it is quoted,
  both alternative sources are shown closed, and the exact field is specified. +1
  root cause DERIVED rather than received: no rd22_run_025 exists in the archive
  workspace, so the ordering explanation comes from the sealed manifest's payload
  array and is offered as a consistent explanation, not as a reading of the run.
  +1 pin-check assertion OF MINE that was wrong and is displayed rather than
  quietly corrected: I tested for "digests[0]" over the raw file and matched the
  DOCSTRING explaining what the old code did. Re-run against executable code only,
  with docstrings stripped by AST parse, the token is absent and both replay sites
  call _load_all_payloads. A test that reads prose as code reports a defect that is
  not there -- the mirror of the under-reaching parsers disclosed at 683, arguing
  the same rule: state the denominator, then check it.)
```

The registrar's diagnosis was correct and incomplete in my favour: the code was
not merely too strict by one class, it was also skipping evidence. What the fix
buys is narrow and real — a raw sealed span is now true in the way a sealed span
is true, an argument is still true in the way an argument must be, and neither can
be mistaken for the other by a producer who would benefit from the confusion.
