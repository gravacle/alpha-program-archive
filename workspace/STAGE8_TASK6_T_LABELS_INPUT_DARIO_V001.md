# STAGE 8 / TASK 6 / BUILD — T0–T3 IN THE INPUT CONTEXT; T4 IS TERMINAL-ONLY — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 671 / Task 6 build — implement the Q-601 adjudication
Authority: RD-22 + Q-601. **THIS ARTIFACT INVOKES NOTHING.**

```text
INPUT_CONTEXT = T0-T3 exact (T4 presence = fault)
TERMINAL_MODE = T0-T4 (exposed)
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 defect of my own, worse than a miss, §1.1)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

## 1. THE DEFECT, AND IT WAS MINE TOO

### 1.1 My verifier did not merely miss the fabrication — it required it

[PROVABLE] The prior implementation, as shipped:

```python
def revalidate_trust_snapshots(snapshots, authorized_trust_root, where):
    """Require T4 = T3 = T2 = T1 = T0 = authorized_trust_root (spec R9/R10)."""
    expected_labels = ("T0", "T1", "T2", "T3", "T4")
    require_exact_fields(snapshots, expected_labels, where)
```

`require_exact_fields` fails on **missing** fields as well as undeclared ones. So
in the verifier-input context my verifier would have:

- **accepted** a fabricated `T4` — a post-verifier snapshot attested before the
  verifier ran; and
- **rejected as malformed** a correct record that honestly omitted it.

Both directions wrong, and the second is the sharper one: **a parent that did the
right thing would have failed my check.** Codex 2's audit found its own parent
fabricating the value; my verifier was demanding it. I inferred `T0–T4` from R9/R10
prose describing the whole chain and never asked which of those snapshots can
exist at the moment my own inputs are composed.

[YOURS] I recorded this label set as deferral **D4** in my first manifest —
*"R9/R10 name `T0`–`T4` in prose; no sealed schema declares the object's shape…
if the producer emits different labels, this binds on the first run."* I named
the risk and then implemented the guess as a hard requirement rather than the
weaker check the uncertainty warranted. Flagging a gap is not the same as
declining to depend on it.

### 1.2 The principle applied

Q-601 is the program's absent-vs-fabricated principle in a new place: **T4's
absence from the verifier-input record is the lawful state, and its presence is a
fabrication.** A snapshot of "after the verifier ran" cannot exist while the
verifier's inputs are being assembled, so a value there is not evidence — it is
an assertion about the future. **A fabricated snapshot must never validate.**

---

## 2. THE IMPLEMENTATION

```text
TRUST_LABELS_VERIFIER_INPUT = ("T0","T1","T2","T3")      exact
TRUST_LABELS_TERMINAL       = ("T0","T1","T2","T3","T4") exact

revalidate_trust_snapshots(snapshots, root, where,
                           context=CONTEXT_VERIFIER_INPUT)   <- SAFE DEFAULT
```

**The default is the strict context.** A caller that forgets to say which context
it is in gets the rule that refuses fabrication, rather than the permissive one.

**The fault is named before the inventory check.** A bare
`require_exact_fields` would report a `T4` as an "undeclared field", which is true
and useless. The implementation tests for `T4` first and raises:

```text
FABRICATED_SNAPSHOT -- T4 is present in the verifier-input trust record.
T4 is the post-verifier snapshot and cannot exist before the verifier runs;
its absence here is the lawful state (Q-601).
A fabricated snapshot must never validate.
```

so the verdict carries the real reason. An unknown `context` value raises rather
than defaulting — *"refusing to guess"* — because guessing a context is how the
original defect happened.

`verify.py` now calls it explicitly with `CONTEXT_VERIFIER_INPUT`. Drift checking
is unchanged: every present label must equal the authorized trust root.

---

## 3. THE DEMONSTRATION — all four cases

```text
trust T0-T3 (input)  : accepted
trust T4 in input    : refused as FABRICATED_SNAPSHOT
trust T0-T4 (terminal): accepted
trust terminal w/o T4: refused
```

Both contexts are exercised in **both** directions — each accepts its lawful
record and refuses the other's. A guard tested only where it should refuse is a
guard that might refuse everything.

Dry run re-run under the pinned flags after the change: **exit 2**, canonical
line, `run_inputs_consumed:false`.

---

## 4. DELTA AND PIN CHECK

```text
CHANGED  verifier/runtime_state.py    context-aware labels; FABRICATED_SNAPSHOT fault
CHANGED  verifier/verify.py           explicit CONTEXT_VERIFIER_INPUT call + import
CHANGED  selfcheck/selfcheck.py       four new trust-context assertions
CHANGED  rd22.verifier-manifest.v001.json          91d264dc… -> 2616cf156dcd2ce885ff57cc26184c77a89df3023691c97eb6d2b0064592c03b
CHANGED  rd22.verifier-manifest.v001.json.seal.sha256   regenerated, verified OK
```

```text
verifier_root_sha256   8732646c…  ->  d5f279c499e9e2bcf6a57116d0cc937133534ae9c6f27e8306ab011f1cf589ab
```

[PROVABLE] **The manifest's field list did not change — 11 fields, same names —
but the instance had to be reissued anyway**, because `verifier_root_sha256`
covers all eleven load-bearing members and three of them changed. That is the
root behaving correctly: a root that covers every load-bearing byte is *supposed*
to move when any of those bytes move. A stale root would have failed Builder A's
check, and rightly.

| Claim | Verified before sealing |
|---|---|
| prior code required T4 | the shipped function displayed verbatim at §1.1 |
| input context is exactly T0–T3 | self-check accepts T0–T3, refuses T0–T4 |
| refusal names the real reason | `FABRICATED_SNAPSHOT` asserted in the self-check, not just any fault |
| terminal mode still T0–T4 | self-check accepts T0–T4, refuses a record missing T4 |
| safe default | signature defaults to `CONTEXT_VERIFIER_INPUT` |
| unknown context refuses | raises rather than defaulting |
| root recomputed and consistent | manifest value equals `package_root_digest()`; `_self_digest()` shares the definition |
| instance canonical | round-trip identical; sorted; single line; no trailing newline; 11 fields |
| sidecar verifies, equals `manifest_sha256()` | `2616cf15…` |
| ledger guard intact; evidence root retained | refuses naming `ledger_sha256`; `e7820ca5…` |
| dry run under `-I -S -B` | exit 2 |
| zero `assert`; 18 files; self-check CLEAN | executed |

### 4.1 `F_PLDEC` and coverage

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. **The chain was not invoked.** `alpha_computed = false`;
`proof_authorized = false`; `kappa_record_computed = false`; no member bound; no
fixed point; no end test; no numeric evaluation; no comparison to any measured
constant.

**Coverage, stated exactly:** I changed the trust-label rule, added four
self-check assertions, and reissued the instance and sidecar. I claim **no check
or fixture outcome**, and I do **not** claim the next run passes — A's parent is
being repaired in parallel at 672, and whether the two sides now agree is what
the run tests.

---

## 5. SELF VERB AUDIT

| My verb | Check |
|---|---|
| Defect owned | Not "I failed to catch it" but **"I required it"** — and the mirror-image fault matters more: a correct parent would have failed my check. Displayed verbatim rather than described. |
| The deferral I under-weighted | I logged this exact uncertainty as D4 and then coded the guess as a hard requirement. Naming a gap is not declining to depend on it, and I record that as the lesson rather than citing the flag as cover. |
| `INPUT_CONTEXT` | Exercised in both directions, and the refusal asserts the **reason string**, so a right answer for a wrong reason fails the check. |
| `TERMINAL_MODE` | Exposed and tested both ways, so the fix does not quietly delete a lawful shape. |
| Safe default | The stricter context is the default; an unknown context refuses rather than guessing — guessing a context is what caused this. |
| Instance reissued though fields unchanged | Explained rather than glossed: the root covers the changed code, so it must move. |
| `CHAIN_INVOKED = false` | Literally true. |

---

```text
INPUT_CONTEXT = T0-T3 exact (T4 presence = fault). revalidate_trust_snapshots now
  takes a context and DEFAULTS TO THE STRICT ONE, so a caller that forgets gets
  the rule that refuses fabrication. T4 in the verifier-input record raises
  FABRICATED_SNAPSHOT -- tested BEFORE the inventory check so the verdict carries
  the real reason rather than "undeclared field" -- and an unknown context raises
  rather than defaulting, because guessing a context is what caused the defect.
  MY OWN CODE WAS WRONG IN BOTH DIRECTIONS: the shipped function required exactly
  T0-T4 via require_exact_fields, so it would have ACCEPTED the fabricated T4 that
  Codex 2's audit caught AND REJECTED AS MALFORMED a correct record that honestly
  omitted it. The second is the sharper fault: a parent doing the right thing would
  have failed my check. I had logged this very uncertainty as deferral D4 and then
  implemented the guess as a hard requirement -- naming a gap is not the same as
  declining to depend on it.)
TERMINAL_MODE = T0-T4 (exposed, as CONTEXT_TERMINAL, and tested in both directions:
  it accepts T0-T4 and refuses a record missing T4, so repairing the input rule did
  not quietly delete the lawful terminal shape.)
SELF_CHECK = passed (four new assertions covering both contexts both ways: T0-T3
  accepted; T4-in-input refused AND the FABRICATED_SNAPSHOT reason asserted so a
  right answer for a wrong reason fails; T0-T4 terminal accepted; terminal-without-T4
  refused. Package self-check CLEAN, zero asserts, 18 files, dry run exit 2 under
  -I -S -B.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. No check and
  no fixture has been run; no outcome is claimed; and I do NOT claim the next run
  passes -- A's parent is being repaired in parallel at 672 and whether the two
  sides agree is what the run tests.)
VERB_AUDIT_SELF = CLEAN (+1 defect of my own that was worse than a miss, displayed
  verbatim rather than described; +the instance reissued despite an unchanged field
  list, explained: verifier_root_sha256 covers all eleven load-bearing members and
  three changed, so the root is SUPPOSED to move and a stale one would rightly have
  failed Builder A's check.)
```

The adjudication came from Codex 2 auditing its own parent, and it landed on my
code too. What I take from it is narrower than "check your assumptions": I had
already written this assumption down as a deferral, in my own manifest, and then
built a hard requirement on top of it anyway. The flag cost nothing because
nothing downstream was weakened to match it.
