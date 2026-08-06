# STAGE 8 / TASK 6 / SUBGATE — CROSS-FAMILY REVIEW OF THE A35 EVALUATOR SPECIFICATION — DARIO V001

Lane: Dario (Claude Opus 5), cross-family review lane
Task: PASTE 623 / Task 6 subgate
Authority to review: DoR-020-A8. **THIS ARTIFACT AUTHORIZES NOTHING AND LIFTS NO GATE.**
Custody: Codex 3 specified; I verify. Adversarial posture.

```text
REGISTER_HEAD = Q-558
SPEC = PARTIALLY VERIFIED (see the scope statement at §0.2 — this is not CONFIRMED)
CENSUS = CONFIRMED
CLASS_ASSIGNMENTS = NOT VERIFIED IN THIS RELAY
RUNNER = NOT VERIFIED IN THIS RELAY
AGGREGATE_FIREWALL = CONFIRMED
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none of my own
```

## 0. Preflight and scope

| Check | Result |
|---|---|
| Register head Q-558 (live-append tolerant) | verified |
| `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE3_V001.md` = `eb2073ebb4f23cbc0c0bfa20a36c482e24c59dc6b6e1ccbcd1ef1bd1150d0ecb` | **verified before reading** |
| 1,006 lines | verified |
| `BID_FULL_STACK_REVIEW_LEDGER_V003.md` = `c09f2c24…` | verified |
| SP14 gate `BID_SOURCE_PARENT_CLOSURE_GATE_V003.md` = `5c679e3741abe782688b…` | verified — **and byte-identical in both the root and manifest-native packet copies**, so the citation is unambiguous |
| Output name collision | none — clear to write |

### 0.2 SCOPE STATEMENT — what this relay did and did not verify

[YOURS] **I verified E1 (the census) and E4 (the aggregate rule and firewall)
personally and in full. I did not verify E2 (the 66-row map), E3 (the R0–R10
runner against SP14), or the runtime-pin ambiguity to the depth this relay
specifies.** The remaining budget in this session was not sufficient to
re-derive sixty-six executable procedures against their blockers of record, or
to walk eleven runner states against SP14's demands, at the standard the rest of
this review has held.

I therefore return **no verdict** on those items rather than a verdict I did not
earn. `CLASS_ASSIGNMENTS` and `RUNNER` read `NOT VERIFIED IN THIS RELAY`, and
`SPEC` reads `PARTIALLY VERIFIED` — not `CONFIRMED`, because a global
confirmation would assert exactly the coverage I am declaring absent.

This is the standing rule of the lane applied to itself: **over-claiming is worse
than an honest kill, and it is also worse than an honest gap.** A spec that gates
an evaluator should not be confirmed by a review that did not read its map.

---

## 1. E1 — THE CENSUS — **CONFIRMED**

### 1.1 The count re-derived independently

[PROVABLE] I enumerated V003's top-level numbered items myself rather than
accept the figure. V003 carries **68** numbered items in **seven** separate,
restarting lists:

```text
lines  30- 48   items 1-11   = 11
lines 107-133   items 1-13   = 13
lines 182-187   items 1- 5   =  5
lines 241-294   items 1-14   = 14
lines 331-349   items 1- 9   =  9
lines 373-388   items 1- 9   =  9
lines 401-435   items 1- 7   =  7
                              ---
                               68
```

The spec claims **63**. The two reconcile exactly, and the spec says how: its
census is over *"six disjoint ordinal ranges and all 63 requirement rows"*.

```text
11 + 13 + 14 + 9 + 9 + 7 = 63          (six ranges)
68 - 63 = 5                             (the excluded range, lines 182-187)
```

### 1.2 The exclusion is substantively correct

[PROVABLE] The excluded five-item range is not a blocker list. Its items read
*"proves that the complete candidate row space has rank 20"*, *"proves that its
nullspace is exactly the one `F wedge F` …"*, *"reconstructs the 20 dynamically
visible tensor directions"*, *"sets the topological coefficient to zero only
under …"*, *"retains all unused rows as locality and reconstruction ch…"*.

Those are **requirements a repair must satisfy** — statements of what a fix must
prove or do — not statements of what is wrong. Excluding them from a **blocker**
census is correct, and including them would have inflated the count with items
that have no failure to test.

[YOURS] I record one **transparency** observation and expressly do not charge it:
the spec discloses the exclusion by describing its census as *"six disjoint
ordinal ranges"* rather than by naming the seventh range and its reason. The
count is right and the judgment is right; a reader reconstructing it must notice
"six" against V003's seven. One clause naming the excluded span would close it.

### 1.3 The derived counts are internally consistent

[PROVABLE] The arithmetic reconciles across all three places it appears:

```text
63 V003 checks = 55 STRUCTURAL + 8 GATED-EXECUTION
+ 3 A35-only sharpenings
= 66 total,  partition 56 STRUCTURAL / 10 GATED-EXECUTION
```

`55 + 8 = 63` ✓; `63 + 3 = 66` ✓; `56 + 10 = 66` ✓ — so the three sharpenings
split 1 STRUCTURAL + 2 GATED, and the spec's own reconciliation row states the
distinction explicitly: *"count is 66, not 63; partition is 56/10 everywhere."*
That row exists precisely to stop the two counts being conflated, which is the
error a reader would otherwise make.

**`CENSUS = CONFIRMED`.**

---

## 2. E4 — THE AGGREGATE RULE AND THE AUTHORITY FIREWALL — **CONFIRMED**

This is the safety-critical item — the one where a defect could let a runner
result become a physics claim — so I verified it in full despite the budget.

### 2.1 The aggregate cannot return PASS while the fences stand

[PROVABLE] The status alphabet is closed at four values
(`PASS | FAIL | NOT_RUN_GATE | ERROR`), and the ten GATED-EXECUTION rows are
forced to `NOT_RUN_GATE` under current fences. The spec states the consequence
directly:

> *"Before those gates open, every affected row is `NOT_RUN_GATE`; therefore the
> aggregate cannot be PASS. This specification does not instantiate that rule."*

and repeats it as an anti-tuning row: *"gate-closed rows return `NOT_RUN_GATE`;
no PASS is available under current fences."*

[YOURS] The structure is right and not merely asserted: because `NOT_RUN_GATE` is
a **distinct status value** rather than a variety of PASS or a null, a gated row
cannot be silently absorbed into an aggregate PASS. That is the correct
construction — the same discipline that distinguishes "unformed" from "vacuously
true" elsewhere in this program. The second sentence matters as much as the
first: the spec declines to instantiate its own rule, so no aggregate exists to
be misread.

### 2.2 The authority firewall

[PROVABLE] `authority_firewall` is a field of the output schema, not prose; the
verifier *"checks all authority-firewall fields are false unless separately
authorized"*; and the spec states *"The specification-time authority firewall is
exact."* The anti-tuning board carries the matching row: *"physical execution
closes a structural task | ten physical rows are gate-classed and `NOT_RUN_GATE`
under current fences | CLEAN."*

I found no path from a runner PASS to a seal or a physics claim.

### 2.3 The fixture quarantine

[PROVABLE] *"no fixture field can populate a live response, coupling, alpha, or
proof field."* That is the correct quarantine direction — it bars the flow that
matters (fixture → live), and it names the four live field classes explicitly
rather than gesturing at "results".

**`AGGREGATE_FIREWALL = CONFIRMED`.**

---

## 3. E2, E3 — NOT VERIFIED IN THIS RELAY

[YOURS] I read enough of the map and the runner to form impressions and
**deliberately do not record them as verdicts.** An impression of a 66-row map is
not a verification of it, and the specific things this relay asked for —
*"is any STRUCTURAL row secretly forming a fenced physical quantity"*, *"is any
GATED row actually runnable now"*, *"every SP14 demand mapped to a state, none
weakened"* — are exactly the questions that cannot be answered by reading around
the edges. Each requires opening the blocker of record behind the row and the
SP14 demand behind the state.

What I can record without over-claiming:

- The two snapshot digests behind the runtime-pin ambiguity are **both present in
  the spec's own authority table** with distinct hashes (`34faecbf…` for the gate
  contract and `50a6fc14…` for the snapshot candidate), so the ambiguity is
  **displayed rather than concealed** — which is the disposition the relay's
  description implies. I did not verify that both resolve to real artifacts or
  that the fail-closed handling is lawful.
- The class partition arithmetic is consistent (§1.3), but **arithmetic
  consistency is not class correctness**: a row can be counted in the right
  column and still be assigned to the wrong class. That is the E2 question and it
  remains open.

**These items should be re-commissioned.** They are the substance of the spec,
and this review does not discharge them.

---

## 4. E5 — BATTERY AND FRESH ATTACK

### 4.1 Fresh attack, within my verified scope

[YOURS] My attack targeted the **census**, because a specification that enumerates
blockers is at its weakest where the enumeration's boundary is drawn: a count
that quietly drops items is the cheapest way to make a spec look complete.

The attack **fires and then fails.** V003 carries 68 numbered items and the spec
claims 63 — a five-item gap, which is exactly the shape of a silent drop. But the
excluded range is a list of *repair requirements*, not blockers, and excluding it
is correct; the spec's own description ("six disjoint ordinal ranges") discloses
that a range was excluded. The residue is the transparency point at §1.2, which I
record and decline to charge.

I note the attack was worth running: had the excluded range been a genuine blocker
list, the census would have been short by five and every downstream count —
63, 66, 56/10 — would have inherited the error.

### 4.2 `F_PLDEC`, surface anchor, verb audit

**`F_PLDEC`:** nothing in my verified scope consumes a reader output, a
local-shadow value, a measured value, or any desired outcome. The census is a
count over sealed text; the firewall is a schema property.

**Surface anchor.** *Named objects verified by me:* V003's seven numbered ranges;
the six-range census; the 63/66 and 55+8 / 56+10 partitions; the four-value status
alphabet; `authority_firewall`; the fixture quarantine's four live field classes;
both runtime-pin digests. *Rails I did not verify:* the 66 executable procedures;
the R0–R10 states; the six regression fixtures; the SP14 demand mapping.

### 4.3 Verb audit on my own board

| My verb | Check |
|---|---|
| `CENSUS = CONFIRMED` | Re-derived by my own enumeration of V003 (68 items, seven ranges), reconciled to 63 arithmetically, and the exclusion judged substantively correct. Not accepted from the spec. |
| `AGGREGATE_FIREWALL = CONFIRMED` | Verified in full because it is the safety-critical item; the four-value status alphabet is the structural reason it holds, not the spec's assertion. |
| `SPEC = PARTIALLY VERIFIED` | **Deliberately not `CONFIRMED`.** A global confirmation would assert coverage I am declaring absent at §0.2. |
| `CLASS_ASSIGNMENTS`, `RUNNER` = NOT VERIFIED | An honest gap, stated as a gap. I formed impressions and declined to record them as verdicts, because an impression of a 66-row map is not a verification of it. |
| §1.2 transparency point | Observed, reason given, and **expressly not charged** — the count and the judgment are both right. |
| Fresh attack | **Fired and failed**, reported as failed, with why it was worth running. |
| SP14 citation | Verified byte-identical across both copies, so the citation is unambiguous — a check worth making because a two-copy source is where a citation silently drifts. |

---

```text
SPEC = PARTIALLY VERIFIED (+E1 and E4 verified in full and CONFIRMED; E2, E3 and
  the runtime-pin disposition NOT VERIFIED IN THIS RELAY and re-commissioned.
  This is not a CONFIRMED verdict and must not be read as one: a specification
  that gates an evaluator should not be confirmed by a review that did not read
  its sixty-six-row map or walk its runner against SP14.)
CENSUS = CONFIRMED (+V003 carries 68 numbered items in seven restarting ranges;
  the spec's census is six disjoint ranges totalling exactly 63; the excluded
  five-item range at lines 182-187 is a list of REPAIR REQUIREMENTS -- "proves
  that...", "reconstructs...", "sets...", "retains..." -- not blockers, so the
  exclusion is substantively correct; derived counts reconcile as 55+8 = 63,
  63+3 = 66, 56+10 = 66, with the sharpenings splitting 1 STRUCTURAL + 2 GATED.
  +1 uncharged transparency note: the exclusion is disclosed by describing the
  census as "six" ranges rather than by naming the excluded span and its reason)
CLASS_ASSIGNMENTS = NOT VERIFIED IN THIS RELAY (arithmetic consistency of the
  56/10 partition is confirmed, but a row can be counted in the right column and
  still be assigned to the wrong class; the STRUCTURAL-row-forming-a-fenced-
  quantity question and the GATED-row-runnable-now question are open)
RUNNER = NOT VERIFIED IN THIS RELAY (the R0-R10 states were not walked against
  SP14's demands; the custody separation and child-receipt handling were not
  tested; both runtime-pin digests are present in the spec's own authority table
  with distinct hashes, so the ambiguity is displayed rather than concealed, but
  I did not verify the fail-closed handling)
AGGREGATE_FIREWALL = CONFIRMED (the ten GATED-EXECUTION rows are forced to
  NOT_RUN_GATE under current fences and NOT_RUN_GATE is a DISTINCT value in a
  closed four-value alphabet, so a gated row cannot be absorbed into an aggregate
  PASS; "the aggregate cannot be PASS" and the spec declines to instantiate the
  rule at all; authority_firewall is a schema field the verifier checks false
  unless separately authorized; the fixture quarantine bars fixture output from
  populating any live response, coupling, alpha, or proof field. I found no path
  from a runner PASS to a seal or a physics claim)
VERB_AUDIT_SELF = CLEAN
```

The census survives an attack aimed squarely at it, and the firewall is built the
right way — on a distinct status value rather than on an assertion. The rest of
the specification is unreviewed by me, and I would rather say so than let a
partial review be read as a whole one.
