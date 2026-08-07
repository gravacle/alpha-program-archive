# STAGE 8 / TASK 6 / BUILD — THE FORMAL RUN CERTIFICATION: RUN 022 vs THE PREREGISTRATION — DARIO V001

Lane: Dario (Claude Opus 5), cross-family reviewer
Task: PASTE 679 / Task 6 — certify run 022 against the Q-591 preregistration
Authority: DoR-020-A8 / RD-22. **THIS ARTIFACT AUTHORIZES NOTHING AND LIFTS NO GATE.**
**Custody note carried:** I built the verifier. This certifies **the run against the
preregistration** — a comparison of records. It is **not** a re-review of my own
code, and where a defect in my build is visible in the records I report it as a
finding rather than adjudicate it.

```text
REGISTER_HEAD = Q-603
ROWS = 66+6 compared, 0 deviations
VERIFIER_MAPPING = one-to-one
HONESTY = confirmed
CERTIFIES = the apparatus honestly reports the absent evidence layer under the pinned runtime
DOES_NOT_CERTIFY = no row verified, no seal moved, A35 not attained, aggregate cannot PASS
VERB_AUDIT_SELF = CLEAN (+2 build findings, both mine, neither affecting this certification)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**The preregistration is fulfilled exactly, and its value is that it was written
first.** Q-591 stated the expected outcome *before* execution and declared that
*"any PASS, any silent skip, any A/B disagreement is a FINDING against the build."*
Run 022 produced none of those.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-603 | verified (live-append tolerance) |
| Run artifacts | `rd22_run_022/` — both child outputs and receipts, producer ledger, bound manifest, verifier output |
| Standard of record | Q-591's expected-outcome statement, read in full |
| Output collision | none — clear to write |

---

## 1. Z1 — THE ROW-LEVEL COMPARISON

### 1.1 The 66 check rows — **0 deviations**

```text
                     PREREGISTERED        OBSERVED
STRUCTURAL x FAIL        56                 56      exact
GATED x NOT_RUN_GATE     10                 10      exact
PASS                      0                  0      exact
ERROR                     0                  0      exact
                                        ------------
class partition                      56 / 10        matches the sealed spec
```

[PROVABLE] Every one of the 56 failures carries the preregistered reason head:
`INPUT_INTEGRITY` — **56 of 56, no other reason present.** Q-591 predicted
`56 x FAIL(INPUT_INTEGRITY)` and that is precisely what the ledger contains.

The producer's own `summary` block agrees with my independent tally:
`{pass:0, fail:56, error:0, not_run_gate:10, structural:56, gated:10, total:66}`.

### 1.2 The 6 fixture rows — **0 deviations**

```text
FX-A35-03-C-FAMILY                      STRUCTURAL       FAIL
FX-A35-04-TAU-FAMILY                    STRUCTURAL       FAIL
FX-A35-05-PRIMITIVE-THOMSON-CONFLATION  STRUCTURAL       FAIL
FX-A35-01-V010-ZERO-STIFFNESS           GATED-EXECUTION  NOT_RUN_GATE
FX-A35-02-ROOT-SURVIVAL-ZERO            GATED-EXECUTION  NOT_RUN_GATE
FX-A35-06-NONZERO-INDEX-CONTROL         GATED-EXECUTION  NOT_RUN_GATE
```

3 STRUCTURAL failing on absent observations, 3 GATED not run — the 3/3 split, and
the class of each fixture matches the sealed §10 table.

### 1.3 Producer semantic agreement — re-verified by me

[PROVABLE] The ledger declares `equal_after_mask = True` with identical semantic
digests (`8a47be4f…` both). I did not take that on trust. I compared the two
children's own status maps directly: **66 rows, 0 disagreements.**

[PROVABLE] The two outputs are **not byte-identical** (86,062 vs 86,061 bytes), and
that is correct rather than a deviation. The differing top-level fields are
**exactly the three declared mask fields and no others**:

```text
mask = [monotonic_duration, process_id, python_optimize]
differing = [monotonic_duration, process_id, python_optimize]      set equality
   monotonic_duration  0.0034…  vs 0.0143…
   process_id          95406    vs 95409
   python_optimize     0        vs 1          <- MUST differ
```

[YOURS] `python_optimize` differing is not tolerated, it is **required**: if the
two children agreed on that field, one of them was not the optimized run. Q-591's
phrase "byte-agreeing" is satisfied in the only sense the apparatus can deliver —
semantic agreement under a mask declared in advance — and every byte that differs
is inside that mask and accounted for.

### 1.4 The verifier's 59 findings — **one-to-one, no absences, no extras**

```text
verifier findings            59      codes: EVIDENCE 56, FIXTURE_EVIDENCE 3
producer failing rows        59      56 checks + 3 fixtures

producer-failing NOT in verifier findings : NONE
verifier findings NOT producer-failing    : NONE
ids appearing more than once              : NONE
```

The 56 check findings carry their `C-B-…`/`C-D-…` identifiers. The 3 fixture
findings identify their rows **by index** (`fixtures[2]`, `[3]`, `[4]`), and I
resolved those indices against the ledger: they are exactly
`FX-A35-03`, `FX-A35-04`, `FX-A35-05` — the three failing structural fixtures. The
mapping is one-to-one and complete. **The positional identification is a finding
against the build (§4, B1), not a deviation in this run.**

---

## 2. Z2 — THE HONESTY PROPERTIES

```text
zero PASS                    0 of 66 check rows, 0 of 6 fixtures        CONFIRMED
zero ERROR                   0 of 66                                    CONFIRMED
gated procedure_started      false on all 10 gated check rows           CONFIRMED
   (and on ALL 66 checks and ALL 6 fixtures -- see below)
no terminal ledger           none present in the run root               CONFIRMED
authority firewall           identical across all four artifacts        CONFIRMED
trust snapshots              T0, T1, T2, T3 -- and no T4                CONFIRMED
```

[PROVABLE] **`procedure_started` is `false` on all 72 rows**, not merely the ten
gated ones. So the firewall's `executed: false` is **accurate, not conservative**:
no descriptor procedure ever started. The 56 structural rows failed at input
integrity *before* execution, and the 10 gated rows never opened. A firewall
reading `executed: false` after a chain that ran is the right answer here, because
what ran was the apparatus, not the checks.

[PROVABLE] **The firewall is byte-identical in all four artifacts** — producer
ledger, verifier output, and both child outputs — with only `implemented: true`,
and every physics and seal field false:

```text
alpha_computed=false  proof_authorized=false  kappa_record_computed=false
SPEC_SEAL=false  CORE_RESULT_SEAL=false  FINAL_CLAIM_SEAL=false
authorization_claimed=false  executed=false  implemented=true
```

[PROVABLE] **No terminal ledger exists, and that is correct.** Spec R10: *"Only
after the complete fresh chain exits successfully may the signature custodian
detached-sign the canonical machine-readable verdict ledger."* The verifier
returned `FAIL`; the chain did not exit successfully; therefore no terminal ledger
may exist. Its **absence is the lawful state**, and a terminal ledger here would
have been the fabrication this program barred at Q-601.

[PROVABLE] `trust_snapshots` carries `T0–T3` and no `T4` — the Q-601 adjudication
honoured in the artifact, not merely in the code.

---

## 3. Z3 — THE CERTIFICATION STATEMENT

### 3.1 What run 022 **does** certify

**That the apparatus honestly reports an absent evidence layer under the
authorized runtime pin.** Specifically, and only:

- the chain executes end to end under the v012 pin and the isolation flags;
- with the evidence layer absent, it returns **total honest failure** — 56 FAIL on
  input integrity, 10 NOT_RUN_GATE, 3 fixture failures, 3 fixture gates — and
  **not one PASS, not one ERROR, not one silent skip**;
- the two producer children agree semantically under a mask declared in advance;
- an **independently built verifier**, which imports no producer code and derives
  its census from the sealed spec bytes, reaches the same 59 conclusions from the
  same sealed inputs, with a one-to-one mapping and no absences in either
  direction;
- the gates hold: nothing gated started, and the authority firewall's physics and
  seal fields are false in every artifact.

[YOURS] The preregistration's deepest property is that it was **written before the
run and predicted failure**. An apparatus that reports total failure when its
inputs are absent has demonstrated something a passing run could not: that its
PASS means something, because its FAIL was not avoidable by construction.

### 3.2 What run 022 **does not** certify

- **No row is verified.** 56 checks failed; 10 never ran. Zero structural checks
  were discharged.
- **No seal moves.** `SPEC-SEAL`, `CORE-RESULT-SEAL`, `FINAL-CLAIM-SEAL` remain
  false; a runner PASS would confer no seal, and there was no PASS.
- **A35 is not attained.** The aggregate cannot be PASS while any row is
  `NOT_RUN_GATE` or FAIL, and 66 of 66 are one or the other.
- **No physics claim of any kind.** `alpha_computed = false`,
  `proof_authorized = false`, `kappa_record_computed = false`; no member bound, no
  fixed point, no end test, no numeric evaluation, no measured-constant comparison.
- **The 56 envelopes and 3 observations named at Q-591 remain unbuilt.** This run
  measured that absence precisely; it did not reduce it.

---

## 4. FINDINGS AGAINST THE BUILD — two, both mine

Neither affects this certification: in both cases the information reached the
record correctly through `findings`, and the one-to-one mapping holds.

**B1 — fixture findings identify rows positionally.** `fixtures[2]`, `[3]`, `[4]`
rather than `FX-A35-03/04/05`. A reader needs the ledger to resolve them, and if
row order ever changed the finding would silently point at a different fixture.
Check findings carry their IDs; fixtures should too.

**B2 — the replay ledgers record only the rows that did not run.** `checks_replayed`
carries **10 rows for 66 checks** and `fixtures_replayed` **3 rows for 6 fixtures** —
in both cases only the `NOT_RUN_GATE` entries. The failing rows appear solely in
`findings`, because the no-evidence branch emits a fault and moves on without
recording a replay row.

[YOURS] **B2 is the exact defect I argued against at 674.** I amended my own schema
that relay to give fixtures a first-class carrier, on the ground that a
`findings`-only encoding makes a discharged duty invisible and cannot distinguish
"nothing found" from "nothing done." My `checks_replayed` then drops 56 of 66 rows
for precisely that reason. The principle was right and I applied it one level too
shallow — to whether the *field* exists, not to whether every row *reaches* it.
Each check and fixture should have a replay row carrying an explicit status
(`PASS`/`FAIL`/`NOT_RUN_GATE`/`ERROR`), so absence and non-recording stay distinct.

---

## 5. Z4 — BATTERY

### 5.1 Pre-seal pin check

| Claim | Verified before sealing |
|---|---|
| 66 checks, 56/10 partition | counted from the ledger, cross-checked against the spec census |
| 56 FAIL all `INPUT_INTEGRITY` | reason heads tallied; one distinct value |
| 6 fixtures, 3 FAIL / 3 NOT_RUN_GATE | listed individually with class |
| A/B agreement | **status maps compared directly by me**, 0 disagreements; not taken from `equal_after_mask` |
| byte difference explained | differing fields set-equal to the declared mask |
| 59 ↔ 59 mapping | set difference computed both directions; duplicates checked |
| fixture indices resolve | 2,3,4 → the three failing structural fixtures |
| zero PASS / zero ERROR | direct scan |
| `procedure_started` false on all 72 | tallied by class |
| firewall identical, four artifacts | all nine fields printed per artifact |
| no terminal ledger | run-root listing |
| `T0–T3`, no `T4` | keys listed |
| verifier census independent | 66 / 56-10 / 35-13-8-10 present in its output |

### 5.2 `F_PLDEC`

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. This is a comparison of sealed records and digests. **No
descriptor, fixture, or chain was invoked by me.** All gates hold as displayed.

### 5.3 Coverage, stated exactly (VERDICT-LINE SCOPE RULE)

I compared 66 check rows and 6 fixture rows against the Q-591 preregistration,
re-verified the A/B agreement myself, mapped the verifier's findings both
directions, and confirmed the honesty properties. I did **not** re-review my own
verifier's code, and I do **not** certify that its logic is correct — only that
the **records** it produced agree with the producer's and with the preregistration.
Where its output revealed a defect, I filed it (§4) rather than adjudicate it.

### 5.4 Self verb audit

| My verb | Check |
|---|---|
| Custody line held | I built the verifier; I compared records and refused to certify my own code. §4 files the two defects it revealed instead of grading them. |
| `0 deviations` | Every preregistered quantity checked individually, not summarized. |
| A/B agreement | **Re-derived**, not read off `equal_after_mask`; and the 1-byte difference is explained rather than waved past. |
| `python_optimize` | Named as **required to differ** — a check that would have missed an unoptimized twin. |
| `executed: false` | Judged **accurate** on the evidence (`procedure_started` false on all 72), not excused as conservative. |
| No terminal ledger | Certified as the **lawful** state with the R10 clause quoted, not merely noted as missing. |
| **B2 recorded against myself** | The principle I argued at 674 applied one level too shallow, in my own code, found while certifying someone else's run. |
| Nothing over-certified | §3.2 is as specific as §3.1: no row verified, no seal moved, A35 not attained. |

---

```text
ROWS = 66+6 compared, 0 deviations (56 STRUCTURAL x FAIL all carrying the
  preregistered INPUT_INTEGRITY reason head -- 56 of 56, no other reason present;
  10 GATED x NOT_RUN_GATE; 3 structural fixtures FAIL on absent observations and
  3 gated fixtures NOT_RUN_GATE. Zero PASS, zero ERROR. The producer's own summary
  block agrees with my independent tally. A/B agreement RE-DERIVED BY ME from the
  two children's status maps -- 66 rows, 0 disagreements -- not read off
  equal_after_mask; the outputs are NOT byte-identical, 86,062 vs 86,061, and the
  differing top-level fields are set-equal to the three declared mask fields, with
  python_optimize 0 vs 1 REQUIRED to differ since otherwise one child was not the
  optimized run.)
VERIFIER_MAPPING = one-to-one (59 findings <-> 59 producer-failing rows; producer-
  failing NOT in findings = NONE, findings NOT producer-failing = NONE, duplicates
  = NONE. The 56 check findings carry their IDs; the 3 fixture findings identify
  positionally as fixtures[2],[3],[4], which I resolved against the ledger to
  FX-A35-03/04/05 -- exactly the three failing structural fixtures.)
HONESTY = confirmed (+display: zero PASS of 72 rows; zero ERROR; procedure_started
  FALSE on ALL 66 checks and ALL 6 fixtures, not merely the ten gated -- which makes
  the firewall's executed=false ACCURATE rather than conservative, since no
  descriptor procedure ever started; the authority firewall byte-identical across
  all four artifacts with only implemented=true and alpha_computed, proof_authorized,
  kappa_record_computed, SPEC_SEAL, CORE_RESULT_SEAL, FINAL_CLAIM_SEAL all false;
  trust_snapshots T0-T3 with NO T4, the Q-601 ruling honoured in the artifact and
  not only in the code; and NO TERMINAL LEDGER EXISTS, which is the LAWFUL state --
  R10 permits signing only after the chain exits successfully, the verifier
  returned FAIL, and a terminal ledger here would have been exactly the fabrication
  Q-601 barred.)
CERTIFIES = that the apparatus honestly reports the absent evidence layer under the
  authorized v012 pin: the chain executes end to end; with evidence absent it
  returns TOTAL HONEST FAILURE with not one PASS, not one ERROR and not one silent
  skip; the two producer children agree semantically under a mask declared in
  advance; and an INDEPENDENTLY BUILT verifier that imports no producer code and
  derives its census from the sealed spec bytes reaches the same 59 conclusions
  from the same sealed inputs. The preregistration's deepest property is that it
  was written BEFORE the run and predicted failure -- an apparatus whose FAIL was
  not avoidable by construction is one whose PASS would mean something.
DOES_NOT_CERTIFY = no row verified (56 failed, 10 never ran, zero structural checks
  discharged); no seal moved (SPEC-SEAL, CORE-RESULT-SEAL, FINAL-CLAIM-SEAL remain
  false, and a runner PASS would confer none anyway); A35 NOT ATTAINED (the
  aggregate cannot PASS while any row is FAIL or NOT_RUN_GATE, and 66 of 66 are one
  or the other); no physics claim of any kind; and the 56 envelopes plus 3
  observations named at Q-591 REMAIN UNBUILT -- this run measured that absence
  precisely, it did not reduce it.
VERB_AUDIT_SELF = CLEAN (+2 findings against the build, both MINE and neither
  affecting this certification since the information reached the record correctly
  through findings: B1 fixture findings identify rows POSITIONALLY rather than by
  fixture_id, so a row-order change would silently repoint them; B2 the replay
  ledgers record ONLY the rows that did not run -- checks_replayed carries 10 of 66
  and fixtures_replayed 3 of 6 -- which is the exact defect I argued against at 674,
  where I amended my own schema on the ground that a findings-only encoding cannot
  distinguish "nothing found" from "nothing done". I applied that principle one
  level too shallow: to whether the FIELD exists, not to whether every ROW reaches
  it. +custody line held: I built this verifier and did not certify my own code,
  only the agreement of the records.)
```

The run's correct output was total failure, and it delivered exactly that — which
is the only way an apparatus can earn the right to be believed when it later says
something passed. What it measured is the distance between a record that convinces
reviewers and a record that feeds a machine: 56 envelopes and 3 observations, named
at Q-591, unchanged by this run and now counted twice by two implementations that
never saw each other's code.
