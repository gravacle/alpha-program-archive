# STAGE 8 / TASK 6 / BUILD — V008 ENVELOPE CHECK AND INDEPENDENT INTEGRATION — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 695 / Task 6 — envelope-check V008, then integrate it, as one whole delta
Authority: RD-22. **THIS ARTIFACT INVOKES NOTHING.**

```text
ENVELOPE = three statements only (+2 carriage findings, +1 statement short of its own claim)
ROWS_CHANGED_CONFIRMED = 0
P0_REPLAY = implemented, executed (six conjuncts; three outcomes, all three exercised)
MANIFEST_INSTANCE = authored, sealed (argv 22, input_roots 7, pins generated)
VERIFIER_ROOT = 43cff85d402a93753427f63607075d5c5ebff7d73e7b0ebe1090b2655c7f64db
PIN_CLOSURE = 12 hits, all resolved (+1 historical citation retained, stated)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 malformed check of my own, §5.2)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**All three preflight digests were generated, not transcribed.** V008 =
`3b24fc39…` (177,979 B); A's report `STAGE8_TASK6_V008_SEVEN_FIELD_CODEX2_V001.md`
= `c597153e…`; `evaluator_build_A/manifests/package_inventory.json` = `1e89b685…`.
The values in the commission were used only as cross-checks.

## 1. I1 — THE ENVELOPE

### 1.1 The three statements are exactly three, and they are schemas

```text
V008-R9-1  R9 computes all six §2.1 P0 conjuncts itself; a producer-emitted P0
           result object is a contract fault; no exemption.
V008-R9-2  the two manifests are closed launch inputs -- an exact ordered argv
           JSON Schema (minItems 22, maxItems 22, prefixItems, items:false) and
           an exact closed eleven-field manifest object with a closed
           SEVEN-field input_roots.
V008-R9-3  a closed four-field refusal value, schema
           `rd22.r9-precondition-refusal.v001`, status
           PRECONDITION_NOT_REPLAYABLE, `criterion_evaluated:false`, and a
           nonempty `missing_carrier`.
```

Checked as commissioned, and each check computed:

```text
66 descriptor rows                     BYTE-IDENTICAL 66/66     rows changed = 0
criterion drift (column 5)             none
procedure drift (column 4)             none
class partition                        56 STRUCTURAL / 10 GATED, both versions
M2 registry                            17 rows, identical list
protected anchors 712a861a / a9e7e50a / bfad4441   byte-identical V007/V008
my census re-derived from V008 bytes   66 / 63+3 / 56-10 / board  REPRODUCE
closed schemas, not prose              argv, manifest, input_roots, refusal: all JSON Schema
PRECONDITION_NOT_REPLAYABLE            distinct from FAIL in the sealed text, and
                                       §2.3's status alphabet is still the closed four
missing carrier named                  `missing_carrier` is a required field
```

V008 also writes into law the sentence relay 693 argued for: *"A criterion `FAIL`
may be recorded only after P0 was independently computed and the criterion was
actually evaluated; a FAIL that was never evaluated is not a verdict."*

### 1.2 [PROVABLE] FINDING F1 — the fixture-span migration is off by one, three times

V008 migrates the three structural-fixture source spans (delta item V8-05,
"whole-state carriage"). The migration was performed — which is the repair my 683
§3.3 asked for — **and every end offset is one byte low.**

```text
                                V007 declared        V008 declared      true V008 span
FX-A35-03-C-FAMILY              [129056,129245)      [133496,133684)    [133496,133685)
FX-A35-04-TAU-FAMILY            [129245,129433)      [133685,133872)    [133685,133873)
FX-A35-05-…-CONFLATION          [129433,129686)      [133873,134125)    [133873,134126)

V007 spans are CONTIGUOUS.  V008's leave 1-byte gaps -- exactly the newlines.
Every start offset is correct; only the ends are short.
```

Decided by computation, not by eye. The convention of record is
**newline-inclusive**, and run 030's own declared `fixture_spec_sha256` values
prove it:

```text
FX-A35-03  declared 9f951cb1…   V008 span as written -> a87e4613…  NO
                                V008 span +1 byte    -> 9f951cb1…  MATCH
FX-A35-04  declared a91920d8…   as written a23682b6… NO   +1 a91920d8… MATCH
FX-A35-05  declared 06ce18cb…   as written 24c18686… NO   +1 06ce18cb… MATCH
```

So this is a defect, not a convention change: a consumer slicing per V008 gets a
digest the fixture manifest does not declare, and the rows would fail their own
spec binding. **Cure: `[133496,133685)`, `[133685,133873)`, `[133873,134126)`,
which also restores contiguity.**

### 1.3 [PROVABLE] FINDING F2 — the carriage certificate's figures

```text
§12.7E declares   FINAL_HUNKS = 6   FINAL_INSERTIONS = 160   FINAL_DELETIONS = 26
computed          FINAL_HUNKS = 6   FINAL_INSERTIONS = 155   FINAL_DELETIONS = 21
```

Four independent algorithms agree on 155/21: `/usr/bin/diff -U 3` (the command
the certificate declares), `git diff --no-index -U3`, `--histogram`, `--minimal`.
Hunk count and assignment are correct — six hunks, all assigned once to
V8-01…V8-06, none unassigned or multiply assigned.

**The error cancels, which is why the certificate cannot self-detect it:** both
figures are +5, so `160−26 = 134 = 155−21`, and the net matches the true line
delta `2119 → 2253`. That is the same shape as the arithmetic slip I disclosed in
my own work at relay 643 — an equation that balances because the error appears on
both sides.

### 1.4 [PROVABLE] FINDING F3 — V008-R9-2 is one carrier short of its own claim

V008-R9-2 states: *"With those supplied inputs, every §2.1 P0 conjunct is
replayable by R9; there is no missing-manifest exception."*

The manifests are supplied and two conjuncts become computable — that part holds.
But conjunct 2, `every_declared_sha256_matches_the_supplied_bytes`, ranges over
the **subject files**, and one of the six is not supplied to R9 in any form:

```text
subject files resolvable by content address in the evidence dir:
   YES  c09f2c24…   BID_FULL_STACK_REVIEW_LEDGER_V003.md
   YES  3b24fc39…   STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V008.md
   NO   d17c5e79…   STAGE8_TASK6_SPEC_V005_INTEGRATION_ADDENDUM_DARIO_V001.md
   YES  5c679e37…   BID_SOURCE_PARENT_CLOSURE_GATE_V003.md
   YES  aa7c6d49…   BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md
   YES  9d35f4ed…   STAGE7_PACKET_MANIFEST_V001.sha256
```

So on the real inputs my implementation returns
`PRECONDITION_NOT_REPLAYABLE` — **V008's own third statement, exercised on its
first real run, for a genuine reason** (§2.2, PATH 2). The claim is not wrong
about the manifests; it is wrong that no carrier is missing. **Cure: one input
action — add the addendum's bytes to the evidence set — after which P0 computes
true (§2.2, PATH 3 proves it). Or state the exemption in §2.1 and say why.** I do
not choose between them.

I record it as a finding rather than accommodate it: I did not weaken conjunct 2
to range only over files that happen to be supplied, because "no mismatch found"
and "never compared" are different facts and only one is a discharged duty.

## 2. I2 — THE INDEPENDENT INTEGRATION

### 2.1 P0 computed, with three outcomes because there are three

`verifier/preconditions.py` (new module) implements all six §2.1 conjuncts. The
design point is the outcome set:

```text
P0 = true                     every conjunct evaluated and satisfied
P0 = false                    every conjunct evaluated, one is false
PRECONDITION_NOT_REPLAYABLE   a conjunct could not be evaluated at all
```

Relay 693's defect was collapsing the third into the second. This module never
does, and the self-check now asserts all three permanently.

`content_root` was **absent from my package entirely** and is added to
`hashing.py`, implemented from §2.1.5 and **controlled against two roots I
already hold** before being used: it reproduces the subject manifest's declared
root and the evidence manifest's declared root exactly.

### 2.2 [PROVABLE] Every new path RUN, not read (FIRST-TIME-RIGHT rule 3)

```text
PATH 1  load_manifest with a wrong digest      REFUSED, content-address mismatch
PATH 2  compute_p0 on the REAL inputs          PRECONDITION_NOT_REPLAYABLE
          missing_carrier = "subject_files[…STAGE8_TASK6_SPEC_V005_INTEGRATION_
          ADDENDUM_DARIO_V001.md] bytes (sha256 d17c5e79…) are declared but not
          supplied to R9"
PATH 3  same, with that one carrier supplied   P0.success = TRUE, 6/6 conjuncts,
                                               evidence_files table = 15 entries
PATH 4  a declared byte_length corrupted       P0.success = FALSE (not a refusal):
                                               content_root(subject) false AND
                                               declared-vs-bytes false
PATH 5  a duplicate declared path              no_duplicate_path_or_key false,
                                               P0.success = FALSE
PATH 6  no bytes supplied at all               closed 4-field refusal, fields
                                               exactly {schema,status,
                                               criterion_evaluated,missing_carrier}
PATH 7  the 22-token argv                      all 22 parsed; fail-closed verdict
                                               emitted; exit 2
PATH 8  producer-emitted P0 in a payload       contract fault (V008-R9-1)
PATH 9  uncomputed P0 reaching the atom        faults; never returns False
```

PATHS 4 and 5 matter as much as 3: they prove `false` is reachable and is *not*
the same object as a refusal. A design with three outcomes that only ever
produces two has two outcomes.

### 2.3 The real manifest instance — pins generated, never transcribed

Every digest below was computed here from the bytes:

```text
spec_sha256               3b24fc39f47d4502b01c1f06faf9f02b7828f5ba0cf4b6a882a3b331ae9c0986
ledger_sha256             0…0   RUN-SCOPED sentinel; the parent binds it, and the
                                verifier refuses the sentinel at run time
evidence_root_sha256      8caa0f7c4e10c9cb8a076a6a719ebbb9093c2daee55e2da375e5a47b12a561bd
subject_manifest_sha256   34c84ac64d76e15a9d5ff876397b4b36a53f541cb25e8510d88cf1ad819a81cb
evidence_manifest_sha256  142ce3b8b7eec841e3bdf6f95e0b9c74ad18d84bd377490540c132057787ffba
runtime_snapshot_sha256   50a6fc14…      runtime_gate_sha256   2ad7f72a…

CONTROL: the evidence root I computed over 15 payloads EQUALS the evidence
manifest's own declared_root -- two derivations, one value.

argv items 22   input_roots 7   top-level fields 11
instance   35b0ec6626c6648940304de78f313879de2f1599c4f6afbd6cf10fa5eba7f52e
           == manifest_sha256(), sidecar regenerated and verified OK
```

**Interfaces are schemas (rule 2):** the self-check now parses the sealed V008
`input_roots` schema out of the spec bytes and requires set equality with my
inventory, and requires `len(argv) == 22`. The inventories are checked against
the sealed text, not against my memory of it.

## 3. I3 — PIN CLOSURE

Swept by **value and by name**, the 688 lesson: a pin carried by filename is
invisible to a digest grep.

```text
superseded roots, by value
  fd59672a (693)  0 files      e3abd168 (690)  0 files
  02da5c8e (688)  0 files      0f67e57a (686)  0 files
  dba5377d (676)  0 files
  -> roots are carried ONLY by the instance, which is reissued every relay

V007 by VALUE  (d38d3171…)   3 hits -> README, verdict-schema const, spec_census const
V007 by NAME   (LANE2_V007)  2 hits -> README path, self-check lookup hint
V007 in prose  (governing)   7 hits -> spec_census "Governing spec:", replay ×2,
                                       contracts §9.4 quote, verify.py R9 cite
TOTAL 12 hits, ALL RESOLVED. Final sweep: 0 by value, 0 by filename.
```

**One retained, deliberately.** `selfcheck/selfcheck.py:526` still reads *"When
the pin moved to V007 and this string still said V005…"* — that is a record of
**when** an incident happened, not a claim about **which bytes govern**. The rule
I applied: *a reference that tells a reader which bytes govern must move; a
reference that records when a decision was taken stays.* Rewriting it would erase
provenance to satisfy a grep.

Before moving the four prose citations I checked that each cited passage carries
forward byte-identically into V008 — the R9 duty sentence, the DAG
single-authority row, and both §9.4 sentences all do — so the citations point at
live text, not at a version that no longer says it.

## 4. DELTA — one whole state change (rule 4)

```text
NEW      verifier/preconditions.py       P0's six conjuncts and the closed refusal
CHANGED  verifier/hashing.py             +content_root (§2.1.5), absent until now
CHANGED  verifier/contracts.py           input_roots 5 -> 7; +refusal and manifest
                                         inventories; V008 citation
CHANGED  verifier/child_manifest.py      argv 14 -> 22 tokens
CHANGED  verifier/verify.py              +4 CLI args, +_index_evidence, P0 computed
                                         before any criterion, refusal recorded
                                         instead of FAIL, producer-P0 fault
CHANGED  verifier/replay.py              the P0 atom consumes the COMPUTED object
CHANGED  verifier/spec_census.py         SPEC_SHA256 -> V008; governing-spec line
CHANGED  contracts/verifier_verdict.schema.json   spec_sha256 const -> V008
CHANGED  contracts/verifier_verdict.schema.json.seal.sha256   -> 8ff8b2cf…
CHANGED  selfcheck/selfcheck.py          +14 permanent assertions; V008 lookup
CHANGED  README.md                       governing spec name and digest
CHANGED  rd22.verifier-manifest.v001.json   authored fresh; +sidecar

verifier_root_sha256  fd59672a…  ->  43cff85d402a93753427f63607075d5c5ebff7d73e7b0e
                                     be1090b2655c7f64db
root MEMBERSHIP 12 -> 13   (preconditions.py; disclosed, not incidental)
package 20 files
```

The four pin sites of relay 688 were all re-pinned together, and the schema's
`spec_sha256` const among them — the site that, left behind, makes every verdict
fail its own contract.

## 5. PIN CHECK

| Claim | Verified before sealing |
|---|---|
| three preflight digests generated | hashed from bytes; commission values used as cross-check |
| 66 rows byte-identical, 0 drift | computed on both files |
| partition, board, M2 registry, anchors | computed |
| F1 spans off by one | declared digests reproduce only from span+1 |
| F2 counts 155/21 | four independent diff algorithms |
| F3 one carrier absent | evidence dir indexed by observed digest |
| content_root correct | controlled against two roots already held |
| P0 three outcomes | PATHS 2–6 executed |
| argv 22 accepted end-to-end | executed; fail-closed verdict emitted |
| producer-P0 is a fault | asserted permanently |
| inventories match sealed bytes | parsed out of the spec and compared |
| instance canonical, sidecar OK | `35b0ec66…` == `manifest_sha256()`; 11 fields |
| evidence root double-derived | mine == the manifest's declared_root |
| root recomputed, membership 13 | `43cff85d…`; equals the instance field |
| pin closure | 0 by value, 0 by filename, 1 historical retained and stated |
| self-check CLEAN, 20 files, 0 asserts | executed |
| dry run both cwds; stdout canon | exit 2; 372 B; `0x7d`; `rstrip() == raw`; stderr 0 |

### 5.1 What I did NOT do

I did not implement the twelve unimplemented opcodes, and an unimplemented
opcode still faults explicitly. I did not add the missing addendum bytes to the
evidence set — that is an input action and A's to take. I did not adjust F1's
spans in my own code; nothing of mine consumes them, and silently compensating
for a spec defect is how a defect survives.

### 5.2 [YOURS] A malformed check of my own

One of my pin-closure commands passed an empty file list to `grep -rc`, which
expanded to the whole package and hung the shell for two minutes. It produced no
wrong finding — the re-run gave the same zeros — but it is worth recording that
the check I wrote to prove closure was the one thing in this relay that failed to
execute cleanly. Re-run as a simple per-pattern loop.

### 5.3 `F_PLDEC` and coverage

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. **The chain was not invoked**: the envelope check reads
sealed bytes, the P0 paths call pure functions on mirrored inputs, and the launch
demonstration is the dry run, which opens no run input. `alpha_computed = false`;
`proof_authorized = false`; `kappa_record_computed = false`; no member bound; no
fixed point; no end test; no numeric evaluation; no comparison to any measured
constant.

**Coverage, stated exactly.** I checked an envelope and integrated an interface.
I claim **no check or fixture outcome**. `P0.success = true` in PATH 3 is a
counterfactual I constructed by supplying a carrier that is not currently
supplied; on the inputs as they stand, P0 is **not replayable**. **I do not claim
run 031 passes** — on today's inputs it will record `PRECONDITION_NOT_REPLAYABLE`
naming the addendum, which is the correct and intended behaviour of V008-R9-3,
and is a refusal rather than a criterion failure.

## 6. SELF VERB AUDIT

| My verb | Check |
|---|---|
| Pins generated, never transcribed | All three preflight digests and all seven input roots computed from bytes. |
| `ROWS_CHANGED_CONFIRMED = 0` | Computed on both files, columns 4 and 5 separately. |
| Findings, not accommodations | F1, F2 and F3 are reported; none is worked around, and I did not weaken conjunct 2 to make F3 disappear. |
| F1 decided by evidence | The declared fixture digests, not my reading of intent, settle newline-inclusive. |
| F2 stated with four algorithms | And with the reason the certificate cannot self-detect it. |
| Three outcomes, all exercised | `false` and `not replayable` are separately demonstrated; a design with three outcomes that produces two has two. |
| `content_root` controlled first | Reproduced two roots I already held before anything depended on it. |
| Pin closure by value AND name | 12 hits; the one retained is stated with the rule that retained it. |
| Membership change disclosed | 12 → 13; a new root member is not an incidental. |
| Own malformed check disclosed | §5.2. |
| No claim on run 031 | The expected outcome is named, and it is a refusal, not a pass. |

---

```text
ENVELOPE = three statements only (+3 findings) (V008-R9-1 independent P0
  computation, V008-R9-2 the closed two-manifest launch interface with an exact
  ordered 22-item argv schema and closed eleven-field/seven-field manifest
  schemas, and V008-R9-3 the closed four-field PRECONDITION_NOT_REPLAYABLE
  refusal naming the missing carrier -- all three are SCHEMAS, NOT PROSE, the
  refusal is textually distinct from criterion-FAIL, and §2.3's status alphabet is
  still the closed four. Verified alongside: M2 registry identical at 17, the three
  protected anchors byte-identical, and my census re-derived from V008 bytes
  reproducing 66 / 63+3 / 56-10 / board. F1: THE FIXTURE-SPAN MIGRATION IS OFF BY
  ONE, THREE TIMES -- every end offset is one byte low, leaving 1-byte gaps exactly
  where the newlines are, where V007's spans were contiguous. Decided by evidence,
  not by eye: run 030's own declared fixture_spec_sha256 values reproduce ONLY from
  the span plus one byte, so the convention of record is newline-inclusive and this
  is a defect rather than a convention change; cure [133496,133685), [133685,133873),
  [133873,134126). F2: the §12.7E certificate declares 160 insertions and 26
  deletions; four independent algorithms -- /usr/bin/diff -U 3 as declared, git diff,
  --histogram, --minimal -- all give 155 and 21. The error is +5 on BOTH sides so it
  cancels and the net still matches the true line delta, which is why the certificate
  cannot self-detect it, the same shape as the slip I disclosed in my own work at 643.
  Hunk count and assignment are correct. F3: V008-R9-2 CLAIMS "every §2.1 P0 conjunct
  is replayable by R9; there is no missing-manifest exception" -- but one of the six
  SUBJECT FILES, the integration addendum d17c5e79…, is not supplied to R9 in any
  form, so conjunct 2 remains unevaluable and the real inputs return
  PRECONDITION_NOT_REPLAYABLE. The claim is right about the manifests and wrong that
  no carrier is missing; cure is one input action, proven sufficient by PATH 3.)
ROWS_CHANGED_CONFIRMED = 0 (66/66 descriptor rows BYTE-IDENTICAL V007 -> V008, ID
  sets equal, zero criterion drift in column 5 and zero procedure drift in column 4,
  partition 56 STRUCTURAL / 10 GATED-EXECUTION unchanged. Computed on both files
  rather than read from the certificate that asserts it.)
P0_REPLAY = implemented, executed (verifier/preconditions.py computes all six §2.1
  conjuncts, with THREE outcomes because there are three: true, false, and
  PRECONDITION_NOT_REPLAYABLE. Relay 693's defect was collapsing the third into the
  second; this module never does. content_root was ABSENT FROM MY PACKAGE ENTIRELY
  and is added from §2.1.5, CONTROLLED FIRST against two roots I already held. NINE
  PATHS RUN, NOT READ: wrong-digest manifest refused; the real inputs returning the
  refusal with the carrier named; the same inputs with that carrier supplied giving
  P0.success TRUE at 6/6; a corrupted declared length giving P0 FALSE; a duplicate
  path giving P0 FALSE; no bytes at all giving the closed four-field refusal; the
  22-token argv parsed end-to-end with a fail-closed verdict at exit 2; a
  producer-emitted P0 faulting; and an uncomputed P0 faulting rather than returning
  False. The false cases matter as much as the true one -- a design with three
  outcomes that only ever produces two has two.)
MANIFEST_INSTANCE = authored, sealed (argv 22 items, input_roots 7 fields, 11
  top-level fields; instance 35b0ec6626c6648940304de78f313879de2f1599c4f6afbd6cf10fa
  5eba7f52e == manifest_sha256(), sidecar regenerated and verified OK. EVERY PIN
  GENERATED FROM BYTES, NONE TRANSCRIBED, including the three preflight digests, and
  the evidence root DOUBLE-DERIVED: my computation over 15 payloads equals the
  evidence manifest's own declared_root. ledger_sha256 stays the run-scoped sentinel
  the parent binds and the verifier refuses at run time. INTERFACES ARE SCHEMAS: the
  self-check parses the sealed V008 input_roots schema out of the spec bytes and
  requires set equality with my inventory, and requires argv length 22 -- checked
  against the sealed text, not against my memory of it.)
VERIFIER_ROOT = 43cff85d402a93753427f63607075d5c5ebff7d73e7b0ebe1090b2655c7f64db
  (membership 12 -> 13, preconditions.py, DISCLOSED rather than incidental; package
  20 files; self-check CLEAN with 14 new permanent assertions; dry run exit 2 from
  both cwds under -I -S -B, 372 bytes ending 0x7d with rstrip() == raw and stderr 0.)
PIN_CLOSURE = 12 hits, all resolved (+1 historical citation retained. Swept BY VALUE
  AND BY NAME per the 688 lesson that a pin carried by filename is invisible to a
  digest grep: V007 by value 3 -- README, the verdict-schema const, the spec_census
  const -- V007 by filename 2, and 7 governing prose citations. All twelve moved;
  the final sweep is 0 by value and 0 by filename. ALL FIVE SUPERSEDED ROOTS --
  fd59672a, e3abd168, 02da5c8e, 0f67e57a, dba5377d -- return ZERO files, because a
  root is carried only by the instance and the instance is reissued every relay. ONE
  RETAINED DELIBERATELY: the self-check comment recording WHEN the V005->V007 pin
  incident happened, under the rule that a reference telling a reader WHICH BYTES
  GOVERN must move while a reference recording WHEN A DECISION WAS TAKEN stays --
  rewriting it would erase provenance to satisfy a grep. Before moving the four prose
  citations I checked that each cited passage carries forward byte-identically into
  V008, so they point at live text.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. The envelope
  check reads sealed bytes, the P0 paths call pure functions on mirrored inputs, and
  the launch demonstration is the dry run, which opens no run input. NO OUTCOME IS
  CLAIMED: PATH 3's P0.success = true is a COUNTERFACTUAL built by supplying a
  carrier that is not currently supplied, and on the inputs as they stand P0 is NOT
  REPLAYABLE. I do NOT claim run 031 passes -- it will record
  PRECONDITION_NOT_REPLAYABLE naming the addendum, which is V008-R9-3 working, and a
  refusal is not a criterion failure.)
VERB_AUDIT_SELF = CLEAN (+1 malformed check of my own, §5.2: a pin-closure command
  passed an empty file list to grep -rc, expanded to the whole package and hung the
  shell for two minutes. It produced no wrong finding -- the re-run gave the same
  zeros -- but the check I wrote to prove closure was the one thing in this relay
  that failed to execute cleanly, and a closure claim resting on a command that did
  not complete would not be a closure claim. +NOTE: I declined to weaken conjunct 2
  to range only over files that happen to be supplied, which would have made F3
  disappear; "no mismatch found" and "never compared" are different facts and only
  one of them is a discharged duty.)
```

The envelope is clean where it matters: three statements, sixty-six rows
untouched, schemas rather than prose. The two carriage defects are arithmetic and
one byte. The interesting one is F3 — V008 built the machinery for a refusal it
believed would never fire, and the first real run fires it, on a file nobody had
noticed was never handed to the verifier at all.
