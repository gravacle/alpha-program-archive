# STAGE 8 / TASK 6 / SUBGATE — A35 SPEC REVIEW COMPLETION: THE MAP, THE RUNNER, THE RUNTIME PIN — DARIO V001

Lane: Dario (Claude Opus 5), cross-family custody reviewer
Task: PASTE 624 / Task 6 subgate — completing the scope Q-559 left unreviewed
Authority: DoR-020-A8. **THIS ARTIFACT AUTHORIZES NOTHING AND LIFTS NO GATE.**
Custody: Codex 3 specified; I verify. I verify nothing of my own construction.

```text
REGISTER_HEAD = Q-559
MAP = CONFIRMED (+4 sampled rows carry PARTIAL blocker coverage and non-Boolean criteria)
CLASS_OVERRIDES = none
RUNNER = CONFIRMED
RUNTIME_PIN = CONFIRMED
SPEC_OVERALL = CONFIRMED (+the map items above; combining Q-559's census and firewall)
VERB_AUDIT_SELF = CLEAN (+1 method note, §5.2)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none of my own
```

## 0. STEP 0 — access checks

| Check | Result |
|---|---|
| Cleanroom + archive workspace listed | both readable and **writable** |
| Register head | **Q-559** — and its entry records this lane's own prior review, the expected live-append state; verify-and-proceed |
| `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE3_V001.md` = `eb2073eb…` | **verified before reading** |
| `STAGE8_TASK6_A35_EVALUATOR_SPEC_REVIEW_DARIO_V001.md` = `a1f5b4c3…` | verified (E1/E4 already CONFIRMED there — **not redone**) |
| `BID_FULL_STACK_REVIEW_LEDGER_V003.md` = `c09f2c24…` | verified |
| `BID_SOURCE_PARENT_CLOSURE_GATE_V003.md` = `5c679e37…` | verified |
| Output filename in both locations | absent — clear to write |

**Structural corroboration of Q-559, obtained incidentally.** I re-tallied the
row table independently: **10 GATED-EXECUTION + 56 STRUCTURAL = 66**, with family
counts V008 11, V009 13, V010 14, V011-MR 9, V011-SP1 9, V011-SP2 7 = 63, plus 3
A35-only = 66. That reproduces the census I confirmed at Q-559 from a different
direction.

---

## 1. E2 — THE 66-ROW MAP — **CONFIRMED, with four sampled-row items**

### 1.1 Sample stated

**All 10 GATED-EXECUTION rows:** `C-B-V010-01`, `C-B-V011-MR-07`, `-MR-08`,
`-MR-09`, `-SP1-04`, `-SP1-08`, `-SP2-03`, `-SP2-06`, `C-D-A35-01-ZERO-INDEX`,
`C-D-A35-03-PHYSICAL-RESIDUE`.

**13 STRUCTURAL rows across all six families plus the A35-only structural row:**
`C-B-V008-01`, `-V008-08`; `C-B-V009-05`, `-V009-13`; `C-B-V010-06`, `-V010-11`;
`C-B-V011-MR-02`, `-MR-05`; `C-B-V011-SP1-02`, `-SP1-07`; `C-B-V011-SP2-01`,
`-SP2-05`; `C-D-A35-02-QUASIFREE-CAR-LIFT`. **23 of 66 rows.**

Every proposed defect was put to an adversarial attacker instructed to default to
refutation. I report the **post-attack** state.

### 1.2 Class correctness — **clean in both directions; `CLASS_OVERRIDES = none`**

[PROVABLE] **The dangerous direction is clean.** No STRUCTURAL row in the sample
secretly forms a fenced physical quantity. A fixed-string scan of the sampled
structural row lines returns **zero** hits for `tau_R`, `alpha`, `kappa`,
`response`, `amplitude`, `residue`, `pole`, `determinant`, `anomaly` — and the
spec enforces this structurally rather than by care: the gated-only opcodes
`SYMBOLIC` and `SPECTRAL` are *"permitted only in a `GATED-EXECUTION` row"*, so a
structural row cannot reach a fenced object through the language at all.

[PROVABLE] **The conservative direction is also clean.** One override to
STRUCTURAL was proposed (`C-B-V011-MR-09`, on the ground that it carries no
gated-only opcode) and was **refuted** on attack: the gated-opcode implication
runs one way only, and the row's object falls inside the spec's own gating
enumeration. It **stands as GATED-EXECUTION**.

The fence definitions do the work, and they are exact:

> `STRUCTURAL := the procedure checks types, exact symbolic identities, finite
> enumerations, schemas, provenance, or protocols without forming a fenced
> physical quantity.`
> `GATED-EXECUTION := running the procedure would form/evaluate a physical
> response, survival amplitude, determinant/anomaly, record-interval containment,
> two-point/pole, or residue.`

**`CLASS_ASSIGNMENTS` = CONFIRMED; `CLASS_OVERRIDES = none`.**

### 1.3 The four items that survived attack

[PART-PROVABLE] Four sampled rows — `C-B-V011-SP1-07`, `-SP2-03`, `-SP2-05`,
`-SP2-06` — carry the same two-part defect, and it survived adversarial attack in
each case:

1. **PARTIAL blocker coverage.** Each tests the *negative/regression* half of its
   blocker exactly, and drops or weakens the *positive* half, substituting a
   typing or presence check where the sealed blocker demands a derivation. The
   clearest instance: `C-B-V011-SP2-05`'s blocker demands *"full source-record
   orientation covariance"*, and M-2 across all three guards returns **zero** for
   any source-record orientation-covariance predicate in the executable row —
   while the spec's own census gloss for the same ID **retains** "covariance."
   The requirement is stated in the gloss and absent from the executable.
2. **Criteria that are not Boolean.** Each carries a term no opcode decides —
   *"certified"*, *"derived"*, *"proven"*, *"silently set"*, and in `-SP2-05` the
   phrase *"all structural laws hold"*, where **"structural laws" is defined
   nowhere in the spec**. A criterion whose terms are not reducible to the closed
   opcode language is not Boolean, and the spec demonstrably knows the right
   instruments — it uses `KERNEL` proof-replay and `ENUM(grammar,cert)`
   completeness certificates elsewhere for exactly this predicate shape.

[YOURS] **I grade this CONFIRMED-with-items rather than REFUTED, and the reason
matters.** The defect is *under-specification of four criteria*, not a false
verdict: no row claims to test something it does not, no class is wrong, and
nothing here could let a fenced quantity be formed. But an evaluator's PASS
criterion that contains an undefined adjective is not executable as written, and
the spec's own §2.2 promises a closed language. **These four rows should be
re-rendered against the opcode set before an implementation is built.**

Nine other proposed defects were **refuted** on attack, several because the
objection was already answered by a column the auditor had not quoted, or by the
spec's rule that *"Every criterion is implicitly conjoined with `P0`."*

**Sampling limit, stated honestly:** 23 of 66 rows. The four items are the
sampled instances of a pattern; whether it recurs in the unsampled 43 is
**not established** by this review.

---

## 2. E3 — THE RUNNER — **CONFIRMED**

### 2.1 SP14's eleven demands, walked one by one

I extracted SP14's demands from the sealed gate and mapped each to a state.

| # | SP14 demand (sealed) | State | Verdict |
|---|---|---|---|
| 1 | load-bearing `assert` removed | **R0** — `parent_source_contains_no_load_bearing_assert`; *"Python `assert` is never load-bearing"* | mapped, not weakened |
| 2 | exact subordinate verdicts frozen | **R1** — manifests carry the exact check-ID and fixture-ID sets; *"Changing one byte changes the manifest root and invalidates the run"* | mapped |
| 3 | a fresh direct parent | **R0** — invoked as a direct script under `-I -S -B`, no `-c`, no `-m`, no undeclared `PYTHONPATH`/`PYTHONHOME`/`DYLD_*`/`LD_*` | mapped, **hardened beyond the demand** |
| 4 | separate content-addressed normal and real `python -O` children | **R3** normal producer child; **R5** optimized producer child; **R1** fixes optimization level 0 / 1 / verifier-declared | mapped |
| 5 | an independent verifier | **R9** independent verifier child; custody §9.2 forbids B importing A's check functions, expected-verdict generator, comparison function, or mutable receipt | mapped |
| 6 | re-derive every module/native/open-event classification against runtime v012 | **R7** — *"reclassifies every module, native image, open event, process/network event, environment mutation, and write"* | mapped, **exceeded** |
| 7 | compare the producer outputs | **R8** producer comparison | mapped |
| 8 | revalidate the mutable macOS trust record **before and after every child** | **R2** `T0`, **R4** `T1`, **R6** `T2` | mapped — see §2.2 |
| 9 | detached-sign one terminal local-assurance record | **R10** terminal ledger and local assurance | mapped |
| 10 | child receipts remain non-authoritative | **R7** — *"Child receipts are evidence. They are never terminal authority and never supply expected row counts or verdicts"*; recurs three times in the spec | mapped |
| 11 | alpha remains false | lead + fences | mapped |

**Eleven of eleven mapped; none weakened.**

### 2.2 Three points where the runner is stronger than the demand

[PROVABLE] **(a) T0/T1/T2 is exactly right, and economical.** SP14 demands trust
revalidation *"before and after every child."* With two producer children (R3,
R5), three snapshots give before-and-after coverage for each — T1 serves as
"after the first" and "before the second." Four would be redundant; two would be
insufficient. The spec picked the minimum that satisfies the demand.

[PROVABLE] **(b) R7 is parent-side, which is what the demand actually requires.**
*"The parent does not trust child labels. From the raw ledgers it
independently…"* SP14 says *re-derive*, and a child's self-report is not a
re-derivation. The spec places the reclassification where the authority is.

[PROVABLE] **(c) The parent hashes its own compiled byte buffer** — along with
both producer/verifier sources, launchers, manifests, the check map, the 66
descriptors, fixtures, subject lineage, runtime, schemas and proof axioms —
*"before any child receives control."* Self-hashing closes the swapped-parent
attack, which SP14 does not name.

### 2.3 Custody separation and the terminal signature

[PROVABLE] The custody graph separates specification (Lane 3), review (this
lane), producer implementation (Builder A), **independent** verifier
implementation (Builder B), invocation (Custodian C, who authored neither), the
principal's content-addressed authorization, and the signature custodian. The
non-sharing rule is explicit and closes the obvious leak: B may share only sealed
schemas, the specification, immutable inputs and output contracts. Custodian C
*"may not patch code, manifests, fixtures, or expected results."*

The bounding sentence is the one that matters: *"Neither builder, child, parent,
verifier, nor signature infers authorization."* The terminal signature therefore
attests **a validated fresh chain exited**, not that any physics claim holds —
which is the correct bound, and consistent with the authority firewall I
confirmed at Q-559.

---

## 3. E4b — THE RUNTIME PIN — **CONFIRMED**

### 3.1 Both digests resolve to real artifacts — verified by direct hashing

[PROVABLE] The digests are cited **only** in the spec within the archive, and the
named files are absent under `workspace/`. Under M-2 that is a bounded no-member
finding in one root, not an absence — so I searched the parent tree and hashed the
artifacts directly:

```text
provenance/primitive_step6_runtime_snapshot_v012.json
  50a6fc141a45451678aa7543e4f267ce26beb6e53182170b478acb6fb0e0f5bb   MATCH
provenance/primitive_step6_runtime_snapshot_v014.json
  fb74b7566b5c7ae8da64096754b16570dc613c8afdd140abd7a0100d5fcc1a08   MATCH
primitive_step6_content_addressed_runtime_gate_v012.md
  34faecbfc0f0a741fbd93ed2698b7ba5a1f3262d4b7cb83c37a375c3c3abe63b   MATCH
primitive_step6_content_addressed_runtime_gate_v010.md
  2ad7f72a88184c11e1253f2c47598fca11e60d05e8e71a26db4e19b16bf98d42   MATCH
```

**All four reproduce exactly.** They are real artifacts of record.

### 3.2 The ambiguity is genuine — and subtler than "two candidates"

[PROVABLE] The name "v012" attaches to **two distinct real artifacts on opposite
sides of the snapshot/gate distinction**, and the spec's display shows why that
bites:

```text
runtime_snapshot_v012   schema v012   but its GATE is v010   (2ad7f72a...)
logical_gate_v012                     is the GATE of the v014 snapshot
runtime_snapshot_v014   schema v014   gate = logical_gate_v012
```

So *"against runtime v012"* selects the v012 **snapshot** under one reading and
the v014 **snapshot** under the other. The name does not determine the
`(snapshot, gate)` pair. **The ambiguity is real, not manufactured.**

### 3.3 The fail-closed handling is lawful and sufficient

[PROVABLE] The remedy is exactly matched to the defect: the manifest must carry
one authorized `runtime_subject={snapshot_sha256, gate_sha256, trust_root}` — a
**content triple**, which is precisely what a *name* cannot supply. Absent it the
parent returns `FAIL(RUNTIME_SUBJECT_AMBIGUOUS)` **before launching a child**, and
`runtime_subject_is_unique` is an R0 precondition, so the check sits at the
earliest state.

[YOURS] Two further points make it sufficient rather than merely present. The
spec *"does **not** silently replace v012 by v014"* — it declines to resolve the
ambiguity by convenience, which is the disposition a reviewer-facing spec owes.
And `FAIL(...)` is a status in the closed four-value alphabet whose aggregate
consequence I confirmed at Q-559, so an ambiguous subject cannot pass through as a
PASS. The closing judgment is right: *"The ambiguity does not prevent
architectural specification; it prevents an implementation from choosing its
runtime by name or convenience."*

---

## 4. E5 — FRESH ATTACK

[YOURS] **My attack: SP14 demands re-deriving "module/native/open-event"
classification, and a three-part demand is where one part quietly goes missing.**
A fixed-string search for `open-event` in the spec returned **zero**.

**It fails.** M-2 guard 3 caught my own false negative: the spec writes "open
event" unhyphenated, and R7 covers *"every module, native image, open event,
process/network event, environment mutation, and write."* The demand is met and
exceeded by three additional classes.

I report the failure because the attack was correctly aimed — a hyphenation
difference between a demand and its implementation is exactly how a conjunct
disappears — and because the way it failed is this relay's method note.

## 5. BATTERY

### 5.1 `F_PLDEC`, anti-tuning, surface anchor

[PROVABLE] Nothing in my verified scope consumes a reader output, a desired
outcome, a measured value, or any physical quantity. The map is a comparison of
procedures against blocker text; the runner is a state machine over hashes and
manifests; the runtime pin is four SHA-256 computations over files.

**Anti-tuning:** the spec's own structural guarantee is the gated-opcode
restriction — a structural row *cannot* reach a fenced object through the
language, so class discipline is enforced by construction rather than by
vigilance.

**Surface anchor.** *Verified by me:* the 66-row partition and six family counts;
the four runtime digests against real files; SP14's eleven demands against R0–R10;
R7's classification list; the custody graph. *Verified by attacked agents:* 23
rows against their blockers. *Not verified:* the remaining 43 rows; the six
fixtures; R8/R10 internals.

### 5.2 Method note — a third false-negative mode, in my own probing

```text
This session's false negatives, all mine, all caught before reaching a finding:
  regex metacharacter   'd^per'      -> '^' is an anchor          (Q-546)
  line wrap             a wrapped phrase across two lines          (Q-551)
  self-reference/scope  an addendum matching its own anchor        (Q-551)
  HYPHENATION           'open-event' vs 'open event'               (HERE)
M-2's three guards catch all four ONLY if guard 3 is actually run in context.
Guards 1 and 2 would have passed this one straight through.        (M-3)
```

### 5.3 Self verb audit

| My verb | Check |
|---|---|
| `MAP = CONFIRMED (+4 items)` | Confirms class correctness and blocker-testing **on a 23-of-66 sample**, which I state. The four items are under-specified criteria, not false verdicts. Not a claim about the unsampled 43. |
| `CLASS_OVERRIDES = none` | Verified in **both** directions; the one proposed override was refuted on attack. This is the safety-critical result and it is clean. |
| `RUNNER = CONFIRMED` | Eleven SP14 demands extracted from sealed text by me and mapped one by one; three points where the runner exceeds the demand recorded as such, not as compliance. |
| `RUNTIME_PIN = CONFIRMED` | Four digests hashed by me against real files; the ambiguity independently characterized; the fail-closed remedy judged sufficient because it demands a content triple where a name is ambiguous. |
| `SPEC_OVERALL = CONFIRMED` | Combines Q-559's census and firewall with this relay's map, runner and pin. Q-559's `PARTIALLY VERIFIED` is now superseded **by coverage, not by revision** — nothing in Q-559 is retracted. |
| "not verified" items | Stated explicitly (43 rows, fixtures, R8/R10 internals) rather than absorbed into the confirmation. |
| Fresh attack | **Fired and failed**, reported as failed, with the reason recorded as (M-3). |
| Agent reliance | 16 agents; every proposed defect was adversarially attacked and I report the post-attack state. Nine were refuted. I verified the runner, the runtime pin and the partition myself. |

---

```text
MAP = CONFIRMED (+4 sampled rows -- C-B-V011-SP1-07, -SP2-03, -SP2-05, -SP2-06 --
  carry PARTIAL blocker coverage and NON-BOOLEAN criteria that survived
  adversarial attack: each tests its blocker's negative/regression half exactly
  and weakens the positive "must be derived" half, and each criterion contains a
  term no opcode decides ("certified", "derived", "proven", "silently set", and
  in SP2-05 "all structural laws hold", where "structural laws" is defined
  nowhere in the spec). Clearest instance: SP2-05's blocker demands "full
  source-record orientation covariance", M-2 returns zero for that predicate in
  the executable row, and the spec's own census gloss for the same ID retains
  "covariance". These four should be re-rendered against the closed opcode set
  before implementation. Nine other proposed defects were REFUTED on attack.
  Sample = 23 of 66 rows; the pattern's recurrence in the unsampled 43 is NOT
  established.)
CLASS_OVERRIDES = none (both directions clean: no STRUCTURAL row secretly forms a
  fenced physical quantity -- enforced structurally, since SYMBOLIC and SPECTRAL
  are permitted only in gated rows -- and the one proposed OVERRIDE_TO_STRUCTURAL,
  C-B-V011-MR-09, was REFUTED on attack and stands as GATED-EXECUTION)
RUNNER = CONFIRMED (all eleven SP14 demands mapped to states, none weakened;
  T0/T1/T2 is the minimum satisfying "before and after every child" for two
  producer children; R7 is PARENT-SIDE re-derivation, which is what "re-derive"
  requires, and it exceeds the demand by three classes; the parent hashes its own
  compiled byte buffer before any child receives control, closing a swapped-parent
  attack SP14 does not name; custody separates A/B/C/principal/signature with
  explicit non-sharing; child receipts non-authoritative at every appearance; the
  terminal signature attests a validated fresh chain exited, not any physics claim)
RUNTIME_PIN = CONFIRMED (all four digests reproduce EXACTLY against real artifacts
  in the parent tree; the ambiguity is genuine and subtler than two candidates --
  "v012" names both a snapshot, whose gate is v010, and a logical gate, which is
  the v014 snapshot's gate, so the two readings select DIFFERENT snapshots; the
  fail-closed remedy demands a content triple {snapshot_sha256, gate_sha256,
  trust_root}, which is exactly what a name cannot supply, fails BEFORE launching
  a child as an R0 precondition, and declines to silently substitute v014)
SPEC_OVERALL = CONFIRMED (+the four map items; combining Q-559's CENSUS and
  AGGREGATE_FIREWALL, both CONFIRMED there and neither retracted, with this
  relay's MAP, RUNNER and RUNTIME_PIN. Q-559's PARTIALLY VERIFIED is superseded
  by COVERAGE, not by revision. Not verified anywhere: the 43 unsampled rows, the
  six fixtures, and R8/R10 internals.)
VERB_AUDIT_SELF = CLEAN (+1 method note (M-3): my "open-event" probe was a
  HYPHENATION false negative -- a fourth mode after regex-metacharacter, line-wrap
  and self-reference. Guards 1 and 2 would have passed it through; only M-2's
  guard 3, read in context, caught it.)
```

The specification survives the scope Q-559 left open. Its class discipline is
enforced by the language rather than by care, its runner meets every SP14 demand
and exceeds three, and its runtime pin answers a real ambiguity with the one
remedy that fits it — a content triple where a name cannot decide. What remains is
four criteria written in words the spec's own opcode set does not decide, and
forty-three rows nobody has yet read.
