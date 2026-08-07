# STAGE 8 / TASK 6 / BUILD — RECEIVING THE FIELD I SPECIFIED — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 690 / Task 6 build — the row contract gains `invocation`
Authority: RD-22. **THIS ARTIFACT INVOKES NOTHING.**

```text
ROW_CONTRACT = 15 fields (invocation typed + validated)
SPAN_LINKAGE = now consumed (digest + declared span arithmetic; re-slicing still not possible)
BOTH_DIRECTIONS = demonstrated (16 contract cases + 5 linkage cases; 15 made permanent)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 refutation of mine that was itself too narrow, §3.2;
                         +1 near-miss on the opcode inventory, §1.2;
                         +1 dead helper removed, §4.1; +2 reporting gaps deferred, §4.2)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**I wrote the field at 686, Builder A emitted it at 687, and my own exact
inventory then refused it.** `checks[0]: field inventory mismatch
(undeclared=['invocation'])` is the correct behaviour of a closed contract meeting
something it does not declare — and the reason the contract exists. Receiving a
specification is part of issuing one.

## 1. THE CONTRACT — 15 fields, and the field is TYPED

### 1.1 What "typed" means here

Admitting the field would have cleared the fault in one line. That is not what a
contract is for. `invocation` is validated on six axes, every one of them derived:

```text
SHAPE       exact 4-field inventory {opcode, result_name, args, instance_id}
VOCABULARY  opcode ∈ the CLOSED 14-opcode set of the sealed spec's §2.2 table
SYMBOL      result_name matches ^r_[A-Za-z0-9_]+$
STRUCTURE   args is a JSON object
LINKAGE     instance_id is null, or parses as
              <symbol>@<source_sha256(64 hex)>:[start,end)  with end > start
PROGRAM     the recorded (result_name, opcode) pair must be DECLARED BY THE
            SEALED DESCRIPTOR's own procedure text
```

The last axis is the one that makes this more than a shape check. `declared_opcodes()`
already parsed the descriptor's program for the replay; the contract now uses the
same parse to refuse an invocation the spec does not declare, and to refuse a
declared result recorded under the wrong opcode. **A producer cannot introduce an
opcode invocation the specification never authorised**, and it cannot rename one.

Cardinality: `null`, one object, or a list of objects, each validated identically.
The list form is not laxity — see §2.2 for why it is necessary and what it exposes
about my own write-out.

### 1.2 [PROVABLE] The opcode inventory — a near-miss disclosed

My first pass read the closed set off the sealed §2.2 table with
`^\| \`([A-Z][A-Z0-9_]*)\(` and returned **13**. The set is 14. `STRICT` is the one
row written **without a parenthesised operand**, so a pattern requiring `(` drops it
silently. Had I shipped that, `STRICT` would have been "outside the closed opcode
set" and every row invoking it would have faulted.

I found it because the count contradicted the number I already knew, and I checked
the table by eye rather than trusting the regex. That is the fourth relay in which
an under-reaching parser nearly produced a false charge, and the rule stands:
**publish the denominator, and stop when the denominator is wrong.**

## 2. BOTH DIRECTIONS — demonstrated

### 2.1 Sixteen cases against a synthetic row built on the sealed V009-06 descriptor

```text
ACCEPT
  null (a row with nothing to record -- what an evidence-absent row carries)
  a list of two, matching the descriptor's declared program
  a singular object (my own 686 write-out form)
  an empty list

REFUSE, each with the fault named
  undeclared field inside the invocation      field inventory mismatch (undeclared=['extra'])
  missing field inside the invocation         field inventory mismatch (missing=['instance_id'])
  opcode outside the closed 14                opcode 'GREP' is outside the closed opcode set
  result_name not an r_ symbol                result_name 'dag' is not an r_<name> result symbol
  args not an object                          args must be an object
  instance_id malformed                       does not parse as <symbol>@<source_sha256>:[start,end)
  instance_id span inverted [19830,18898)     span is empty or inverted
  instance_id span empty    [18898,18898)     span is empty or inverted
  result the descriptor does not declare      result 'r_bogus' is not declared by the sealed descriptor
  declared result, WRONG opcode               result 'r_dag' is declared as DAG, recorded as COMPARE
  invocation is a string                      must be null, an object, or a list of objects
  list containing a non-object                expected object

16/16
```

The refusals are as important as the acceptances: a contract that accepted
everything would also "accept" the valid cases.

### 2.2 [YOURS] A gap in my own 686 write-out, named rather than papered over

I wrote the field as a **singular object**. V007's `C-B-V009-06` declares **two**
assignments — `r_ground := COMPARE(…)` and `r_dag := DAG(…)` — so one object cannot
record the row's program. Hence the list form.

The direction I did **not** make a fault: *declared but not recorded*. A producer
that records only `r_dag` leaves `r_ground` uncovered, and the coverage guard is
correspondingly weaker for it. That is the exculpation direction and I would
normally close it. I did not, for a stated reason: **my own write-out specified a
singular field, and faulting Builder A for conforming to my specification would be
unjust.** The cure is an amendment to the write-out — *the recorded invocations must
cover every assignment the descriptor declares* — which belongs in a relay that
amends it, not in one that receives it. Recorded here so the next relay has it.

## 3. SPAN LINKAGE — now consumed

At 686 §2.3 I recorded byte-span linkage as **undelivered** and named the field
needed. It is here, and it is consumed:

```text
declared spans from A's recorded invocation pair:
    (932, 'stage_dependencies@13cf1e17…:[18898,19830)')

[real payloads + the recorded invocation pair]   consumable=1 raw=1 faults=0
    RAW 47e7c329…  932 B  linkage=digest+span  stage_dependencies@13cf1e17…:[18898,19830)
    unrequired_args = ['authority', 'left', 'mask', 'right']

[COMPARE only -- null instance_id, nothing span-grounded]   faults=0
    RAW 47e7c329…  932 B  linkage=digest          <- legitimately unlinked, not a defect

[raw payload 932 -> 933 bytes, span still declares 932]   faults=1
    FAULT raw payload 20b35aef… is 933 bytes but no recorded instance_id
          declares a span of that length (932)

[object-valued argument tampered]   faults=1
    FAULT invocation argument 'graph' is not reproduced by any digest-verified payload
```

**What the linkage is, exactly.** The payload's identity is its independently
verified digest; the declared span must agree on its **length**. The verifier still
**cannot re-slice the source** — `…preregistration_v011.json` is not a run input —
so this is arithmetic against a declaration, not a re-derivation, and the code and
the verdict both label it `digest+span` rather than `verified`. That is stronger
than 686's digest-only and weaker than full re-slicing, and it is named as such.

A null `instance_id` is lawful and stays `linkage: digest`: `r_ground` is a COMPARE
over two digests and grounds no span. An empty span set is a fact about the row.

### 3.1 The exemption that does not weaken the guard

Guard B still bites on object-valued arguments — the tampered-`graph` case above
proves it. What changed is that **non-object arguments are reported, not required**.

### 3.2 [PROVABLE] This convicts a refutation of mine

At 688 §4.2 I predicted my coverage guard would false-fault on
`authority: "PRINCIPAL_SINGLE_AUTHORITY"`, tested it, got zero faults, and
**withdrew the hazard**. That withdrawal was wrong, and wrong in a way I should
have caught: **I tested one of the row's two recorded invocations.** With the pair,
the guard demanded a digest-verified payload for `left`, `right` and `mask` — a
P0-derived digest, a spec-fixed constant, and an empty mask. Three false faults on
the one row that matters.

The rule now implemented: **coverage applies only to object-valued arguments.** A
payload is admitted as consumable only if it parses to a JSON *object*, so only an
object-valued argument can ever be reproduced by one. Demanding a payload for a
spec-fixed constant is the same category error the registrar identified for raw
payloads at 686 — *too strict by one class* — moved into the argument dimension.
Nothing is conceded: a scalar cannot slide into the raw class, because it is not a
payload.

I withdrew a real hazard on a test with the wrong denominator, and the denominator
was two. That is the same failure as §1.2 and as the 683 parser near-misses, in a
third costume.

## 4. DELTA AND PIN CHECK

```text
CHANGED  verifier/contracts.py   CHECK_ROW_FIELDS 14 -> 15; +OPCODES(14),
                                 +INVOCATION_FIELDS, +parse_instance_id,
                                 +validate_invocation, +recorded_invocations;
                                 validate_check_row cross-checks the descriptor
CHANGED  verifier/replay.py      invocation_arguments accepts a list and carries
                                 is_object; +declared_spans; span linkage and the
                                 non-object exemption in classify_payloads
CHANGED  verifier/verify.py      _recorded_invocation docstring: owed change DISCHARGED
CHANGED  selfcheck/selfcheck.py  +15 permanent assertions
CHANGED  rd22.verifier-manifest.v001.json    2b1d195b… -> 433d208e927c61504ad83b077cb
                                 19ffefa0bad320520cee7742524ecb5558e26
CHANGED  rd22.verifier-manifest.v001.json.seal.sha256   regenerated, verified OK

verifier_root_sha256  02da5c8e…  ->  e3abd168dfdaacd16c29ee1bd7eb857409a1dd7c9749916
                                     e5957fe9b6b1a9314
UNCHANGED  root MEMBERSHIP (12); run_verifier.py; spec_census; both contracts files;
           all five input roots -- spec d38d3171… and evidence fcaa97a0… untouched
```

`contracts.py` imports `declared_opcodes` from `replay`. I checked the direction:
`replay` imports only `canonical_json` and `hashing`, so there is no cycle. For the
same reason the `instance_id` pattern is written in both modules rather than shared
— **two lines that agree beat one import across a cycle** — and the self-check
asserts both behave identically by exercising each.

| Claim | Verified before sealing |
|---|---|
| 15 fields, 14 opcodes | asserted from the shipped inventories, permanently |
| invocation typed on six axes | 12 refusal cases, each naming its fault |
| descriptor cross-check | `r_bogus` refused; `r_dag` as COMPARE refused |
| span linkage consumed | `digest+span` with the instance_id carried; length mismatch faults |
| null instance_id lawful | `linkage: digest`, no fault |
| Guard B unweakened | tampered object-valued argument still faults |
| no import cycle | `replay` imports neither `contracts` nor `verify` |
| root recomputed, membership 12 | `e3abd168…`; equals the instance field |
| instance canonical, sidecar OK | `433d208e…` == `manifest_sha256()`; single line; 11 fields |
| input roots untouched | spec `d38d3171…`, evidence `fcaa97a0…`, ledger sentinel |
| self-check CLEAN, 19 files, 0 asserts | executed |
| dry run both cwds; stdout canon | exit 2; 372 B; `0x7d`; `rstrip() == raw`; stderr 0 |

### 4.1 A helper written and then removed

I wrote `undeclared_invocation_coverage()` to report the declared-but-not-recorded
direction, then found it had **zero callers**: it could not be surfaced without a
verdict field, which is §4.2's deferred change. Dead code in a shipped package is
worse than a documented gap, so I removed it rather than leave a function that
looks like a check and performs none.

### 4.2 Two reporting gaps, deferred with a reason

`classify_payloads` now returns `unrequired_args`, and the coverage direction of
§2.2 has no carrier. **Neither is emitted in the verdict**, because emitting them
means amending `verifier_verdict.schema.json` — a second cause. That is the same
call I made at 674 and closed as its own relay at 676. By my own absent-vs-empty
argument these deserve carriers; they do not deserve to ride inside a delta about
the row contract.

### 4.3 `F_PLDEC` and coverage

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. **The chain was not invoked**: the contract cases run
against a synthetic row I constructed on the sealed descriptor's real procedure
text, the linkage cases call one pure classification function on sealed bytes, and
the launch demonstration is the dry run, which opens no run input.
`alpha_computed = false`; `proof_authorized = false`; `kappa_record_computed = false`;
no member bound; no fixed point; no end test; no numeric evaluation; no comparison
to any measured constant.

**Coverage, stated exactly.** I extended a contract and consumed a field. I claim
**no check or fixture outcome**, and **I do not claim run 028 passes** — what the
next run reaches is what it tests. The three false faults of §3.2 would have been
reported against `C-B-V009-06`; removing them removes wrong faults, not real ones.

## 5. SELF VERB AUDIT

| My verb | Check |
|---|---|
| `typed + validated` | Six axes, twelve refusals; the descriptor cross-check makes it a program check, not a shape check. |
| The refusal was correct | My exact inventory meeting an undeclared field is the contract working; the fault text named exactly what to fix. |
| **My own write-out was incomplete** | It specified a singular field for a row declaring two assignments. Named, with the amendment written out, rather than silently generalised. |
| **A refutation of mine overturned** | 688's withdrawal of the coverage hazard was tested on ONE of TWO invocations. The hazard was real; the fix is stated and the guard is shown still to bite. |
| Near-miss disclosed | The opcode regex returned 13; `STRICT` carries no parentheses. Shipping it would have faulted every `STRICT` row. |
| `SPAN_LINKAGE = now consumed` | Scoped in the code and the verdict: `digest+span`, not `verified`. Re-slicing is still impossible and still said so. |
| Dead code removed, not left | A helper with no callers looks like a check and performs none. |
| Deferrals reasoned | Two reporting gaps need a verdict carrier; that is a schema amendment and a separate cause. |
| No claim on run 028 | Removing wrong faults is not producing a pass. |

---

```text
ROW_CONTRACT = 15 fields (invocation typed + validated) (I specified this field at
  686 §2.3, Builder A emitted it at 687, and my own EXACT inventory then refused it
  as undeclared -- which is the contract working, not failing. Admitting it would
  have been one line; instead `invocation` is validated on SIX DERIVED AXES: exact
  4-field shape {opcode, result_name, args, instance_id}; opcode within the CLOSED
  14-opcode set of the sealed §2.2 table; result_name an r_<name> symbol; args a JSON
  object; instance_id null or parsing as <symbol>@<source_sha256>:[start,end) with
  end > start; and -- the axis that makes it a PROGRAM check rather than a shape
  check -- the recorded (result_name, opcode) pair MUST BE DECLARED BY THE SEALED
  DESCRIPTOR's own procedure, so a producer can neither introduce an invocation the
  specification never authorised nor rename a declared one. Cardinality is null, one
  object, or a list, each element validated identically. NEAR-MISS DISCLOSED: my
  first read of the closed opcode set returned THIRTEEN because `STRICT` is the only
  table row written without a parenthesised operand and my pattern required "(";
  shipping it would have faulted every STRICT row. Fourth relay in which an
  under-reaching parser nearly produced a false charge.)
SPAN_LINKAGE = now consumed (+status: DIGEST + DECLARED SPAN ARITHMETIC, NOT
  re-derivation. A raw grounding payload's independently verified digest is its
  identity and the recorded instance_id must agree on its LENGTH -- the real V009-06
  member links as digest+span at stage_dependencies@13cf1e17…:[18898,19830), 932
  bytes, and a payload lengthened to 933 FAULTS naming the declared 932. The verifier
  still CANNOT RE-SLICE the source, because …preregistration_v011.json is not a run
  input, so the code and the verdict label it `digest+span` and not `verified`. A
  null instance_id is lawful and stays digest-only: r_ground is a COMPARE over two
  digests and grounds no span. THE FIX THIS EXPOSED: coverage now applies only to
  OBJECT-VALUED arguments, because a payload is admitted as consumable only if it
  parses to a JSON object, so only an object argument can ever be reproduced by one;
  demanding a payload for a spec-fixed constant, a P0-derived digest or an empty mask
  is the same "too strict by one class" category error the registrar identified for
  raw payloads at 686, moved into the argument dimension. Guard B is UNWEAKENED --
  a tampered object-valued argument still faults.)
BOTH_DIRECTIONS = demonstrated (SIXTEEN contract cases -- four accepted, twelve
  refused with the fault named: undeclared field, missing field, opcode outside the
  closed 14, result_name not an r_ symbol, args not an object, malformed
  instance_id, inverted span, empty span, a result the descriptor does not declare, a
  declared result under the wrong opcode, a string instead of an object, and a list
  containing a non-object -- plus FIVE linkage cases. FIFTEEN are now permanent
  self-check assertions, so a regression bites rather than waits for a run. A GAP IN
  MY OWN 686 WRITE-OUT is named rather than papered over: I specified a SINGULAR
  field, but V007's C-B-V009-06 declares TWO assignments, so one object cannot record
  the row's program -- hence the list form. The declared-but-not-recorded direction is
  reported and NOT faulted, deliberately: it is the exculpation direction and I would
  normally close it, but my own write-out specified the singular form and faulting
  Builder A for conforming to my specification would be unjust. The amendment -- the
  recorded invocations must cover every assignment the descriptor declares -- belongs
  in a relay that amends the write-out, not in one that receives it.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. The contract
  cases run against a SYNTHETIC row built on the sealed descriptor's real procedure
  text, the linkage cases call one pure classification function on sealed bytes, and
  the launch demonstration is the dry run, which opens no run input. No check and no
  fixture has been run and NO OUTCOME IS CLAIMED. I do NOT claim run 028 passes: the
  three false faults removed here would have been reported against C-B-V009-06, and
  removing WRONG faults is not producing a pass.)
VERB_AUDIT_SELF = CLEAN (+1 REFUTATION OF MINE OVERTURNED, §3.2: at 688 I predicted
  my coverage guard would false-fault on the spec-fixed PRINCIPAL_SINGLE_AUTHORITY,
  tested it, got zero faults and WITHDREW the hazard -- but I tested ONE of the row's
  TWO recorded invocations. With the pair the guard demanded digest-verified payloads
  for `left`, `right` and `mask`: a P0-derived digest, a spec-fixed constant and an
  empty mask, three false faults on the one row that matters. I withdrew a real hazard
  on a test with the wrong denominator, and the denominator was two -- the same
  failure as the opcode regex above and as the 683 parser near-misses, in a third
  costume. +1 near-miss on the opcode inventory, §1.2. +1 DEAD HELPER REMOVED, §4.1:
  I wrote undeclared_invocation_coverage(), found it had zero callers because it
  cannot be surfaced without a verdict field, and removed it -- a function that looks
  like a check and performs none is worse than a documented gap. +2 REPORTING GAPS
  DEFERRED with a reason, §4.2: unrequired_args and the coverage direction have no
  verdict carrier, and adding one means amending verifier_verdict.schema.json -- a
  second cause, the same call I made at 674 and closed as its own relay at 676.)
```

The commissioned change was one field. The work was refusing to merely admit it —
and then discovering, while typing it, that the guard it feeds had been demanding
evidence for a spec-fixed constant, which I had tested for two relays ago and
cleared on half the data.
