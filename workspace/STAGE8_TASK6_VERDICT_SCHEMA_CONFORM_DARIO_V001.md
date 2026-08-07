# STAGE 8 / TASK 6 / BUILD — THE VERDICT CONFORMED TO ITS OWN SCHEMA — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 674 / Task 6 build — the verdict against `verifier_verdict.schema.json`
Authority: RD-22. **THIS ARTIFACT INVOKES NOTHING.**

```text
CHOICE = amend (+reason at §1)
VERDICT = schema-valid on all emission paths (demonstrated)
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 second defect found, latent and worse, §2)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**A enforced my contract against me correctly, and the contract was mine.** I
wrote `additionalProperties: false` over 13 fields and then emitted 14.

## 1. THE CHOICE: **(b) AMEND** — and why it is not the easy road

[YOURS] **(a) was the cheaper option** — delete one field and ship. I chose the
one that costs a schema amendment, and here is the reasoning, so it can be
overruled on its merits.

**1. R9 lists fixture replay as a distinct duty.** Its duty list carries
*"replays each pass predicate from evidence bytes"* **and** *"replays every
fixture's expected result"* as separate lines. `checks_replayed` already gives the
first a first-class carrier. The second has an equal claim.

**2. `findings` carries only faults, so folding fixtures there erases a
discharged duty.** If every fixture replays correctly, a `findings`-only encoding
leaves **no trace that fixture replay happened at all** — and "no fixture
findings" becomes indistinguishable from "no fixture replay performed."

That is the absent-vs-fabricated principle this program has now ruled on twice —
Q-591's `ABSENT_OF_RECORD` and Q-601's `T4`. A verdict must be able to show that a
duty was **discharged**, not merely that it produced no complaints.

**3. Checks and fixtures are different universes with different row shapes.** 66
checks against 6 fixtures; the integration addendum §2.3 gives fixtures their own
16-field row precisely because they are not checks. Pushing fixture outcomes into
`checks_replayed` would undo a distinction I drew two relays ago and that Builder A
now conforms to.

**4. This schema is my own package's output contract**, not the shared
`rd22.verifier-manifest.v001`. Amending it is within my lane, as a disclosed
delta — not a unilateral change to something we jointly depend on.

## 2. THE SECOND DEFECT — latent, worse, and nobody had hit it

[PROVABLE] While conforming the success path I checked the other one. **The
fail-closed path has never satisfied the schema:**

```text
fail-closed emission = {schema, verdict, fault}      3 fields
schema required      = 13 fields, additionalProperties:false
  -> `fault` is UNDECLARED
  -> 11 required fields are MISSING
```

It was invisible because it only fires when no verdict can be formed, and run 019
got far enough to produce a full verdict. Had the run stopped earlier, the
verifier would have emitted a document its own contract forbids — and reported a
schema violation *about itself* while trying to report the real fault.

**I did not fabricate fields to fix it.** Filling `runtime_subject` or
`authorization_sha256` with placeholders on a path that by definition could not
read them is exactly the fabrication Q-601 barred. Instead the schema now declares
**two closed document kinds**:

```text
oneOf:
  FULL  verdict  14 fields, all required, additionalProperties:false
                 emitted whenever a verdict could be formed (exit 0 or 1)
  FAULT verdict   3 fields {schema, verdict:"FAIL", fault}, additionalProperties:false
                 emitted only when no verdict could be formed (exit 2);
                 its fields are exactly those knowable without a verdict
```

Each is closed on its own terms, and neither invents a value it cannot hold.

## 3. THE DEMONSTRATION — both paths, and four negatives

```text
SUCCESS path (full verdict)                    errors=0   OK
FAIL-CLOSED path (fault verdict)               errors=0   OK
OLD 13-field emission (no fixtures_replayed)   errors=1   OK  (correctly refused)
full + undeclared field                        errors=1   OK  (correctly refused)
fault + undeclared field                       errors=1   OK  (correctly refused)
wrong spec_sha256 const                        errors=1   OK  (correctly refused)
```

Positive **and** negative cases: a schema that accepts everything would also
"validate" both paths.

[YOURS] One incident worth recording. My first validation run reported the full
verdict matching **zero** branches, and my instinct was that the amendment was
wrong. It was not — **the schema caught my test sample.** `spec_sha256` is a
`const` pinned to the governing spec digest and I had fed it `"0"*64`. The
contract refused a fake before it refused anything real, which is the behaviour I
want and did not expect to have demonstrated on myself.

Four of these cases are now permanent self-check assertions, so a regression bites
rather than waits for a run.

## 4. DELTA AND PIN CHECK

```text
CHANGED  contracts/verifier_verdict.schema.json          9a50ce5b… -> 300a475ead3c17cd5b759ffcc3733418029030404af262632583fff077f2907f
CHANGED  contracts/verifier_verdict.schema.json.seal.sha256   -> 4973bb2da031f9e4e8152ce1584f3648334b96e70ac5224fdef66c65d8446c53
CHANGED  selfcheck/selfcheck.py                          -> 9d9ffc2a0817c9674a939c96e7f4797434ecb7922d62d8e8e3d689298b678ea7
UNCHANGED  every verifier/*.py and run_verifier.py
UNCHANGED  rd22.verifier-manifest.v001.json              83b68846… (and its sidecar verifies)
UNCHANGED  verifier_root_sha256                          eb246168…
```

[PROVABLE] **No runtime code changed**, because none needed to: the emission was
already correct and the *contract* was wrong about it. The root therefore did not
move, and the instance did not need reissuing — I verified the root before and
after and it is identical. Package: 19 files (the schema sidecar is new).

| Claim | Verified before sealing |
|---|---|
| schema declares 14 + 3 in two closed kinds | counted from the amended file |
| both emission paths validate | executed, errors=0 each |
| four tamper cases refused | executed, errors>0 each |
| the const pin bites | wrong `spec_sha256` refused |
| no runtime `.py` changed | root recomputed before/after, identical |
| instance and its sidecar untouched | digest unchanged; `shasum -c` OK |
| schema sidecar regenerated | `shasum -c` OK |
| self-check CLEAN, 19 files, zero `assert` | executed |

### 4.1 One observation, not repaired here

[YOURS] `verifier_root_sha256` covers `run_verifier.py` and `verifier/*.py`. It
does **not** cover `contracts/verifier_verdict.schema.json` — yet that file is
load-bearing for the handshake, since it is the contract A validates my verdict
against. It is pinned by its own sidecar, so it is not unpinned; but it is not
inside the one root either. Whether the output contract belongs in the package
root is a contract question, not a bug I should settle mid-delta, so I record it
rather than expand this change. It is the same shape as the launcher question A
raised at 667.

### 4.2 `F_PLDEC` and coverage

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. **The chain was not invoked.** `alpha_computed = false`;
`proof_authorized = false`; `kappa_record_computed = false`; no member bound; no
fixed point; no end test; no numeric evaluation; no comparison to any measured
constant.

**Coverage, stated exactly:** I amended my own output schema and added four
self-check assertions. I claim **no check or fixture outcome**. Whether the next
run's verdict validates against A's reading of this schema is what the run tests.

## 5. SELF VERB AUDIT

| My verb | Check |
|---|---|
| `CHOICE = amend` | The **more** expensive option; the cheaper one (delete the field) is named so the choice can be judged on its reasoning rather than assumed convenient. |
| Reason 2 is the program's own principle | Not invented for this relay: Q-591 and Q-601 both turned on absent-vs-empty, and a `findings`-only encoding makes a discharged duty invisible. |
| **Second defect found** | The fail-closed path had *never* validated — undeclared `fault`, 11 required fields missing. Latent because it only fires when no verdict forms. Disclosed as its own named cause rather than folded silently into the amendment. |
| No fabrication | I refused to pad the fault document with placeholder digests it cannot know — the exact move Q-601 barred one relay ago. |
| Negatives tested | Four refusals as well as two acceptances; and the const-pin refusal was demonstrated **on my own fake sample**, which I record because it was not the outcome I expected. |
| Root not moved | Verified, not assumed — recomputed before and after. |
| Observation deferred, not smuggled | The schema sits outside `verifier_root_sha256`; named, not fixed mid-delta. |

---

```text
CHOICE = amend (+reason: R9 lists "replays every fixture's expected result" as a
  DISTINCT duty from replaying pass predicates, and checks_replayed already gives
  the latter a first-class carrier; `findings` carries only FAULTS, so folding
  fixture results there would leave a fully-passing fixture replay with NO TRACE
  and make "no fixture findings" indistinguishable from "no fixture replay
  performed" -- the absent-vs-empty principle this program ruled on at Q-591 and
  Q-601; checks and fixtures are different universes with different row shapes,
  and addendum §2.3 gives fixtures their own 16-field row precisely because they
  are not checks; and this schema is my OWN package's output contract, not the
  shared manifest contract, so amending it is within my lane. NOTE: option (a),
  deleting the field, was the CHEAPER road and is named so the choice can be
  judged on its reasoning.)
VERDICT = schema-valid on all emission paths (demonstrated: SUCCESS full verdict
  errors=0 and FAIL-CLOSED fault verdict errors=0, plus FOUR negative cases each
  correctly refused -- the old 13-field emission, full+undeclared, fault+undeclared,
  and a wrong spec_sha256 const. A SECOND DEFECT was found and fixed here: the
  fail-closed path had NEVER satisfied the schema -- `fault` undeclared and 11
  required fields missing -- latent because it fires only when no verdict can form,
  and run 019 got far enough to produce a full one. It is repaired WITHOUT
  FABRICATION: rather than padding the fault document with placeholder digests it
  cannot know -- the exact move Q-601 barred -- the schema now declares TWO CLOSED
  DOCUMENT KINDS via oneOf, full(14) and fault(3), each closed on its own terms.)
SELF_CHECK = passed (four of the six validation cases are now permanent assertions
  so a regression bites rather than waits for a run; package CLEAN, 19 files, zero
  asserts. NO RUNTIME CODE CHANGED -- the emission was already right and the
  CONTRACT was wrong about it -- so verifier_root_sha256 stayed eb246168… and the
  instance 83b68846… and its sidecar are untouched; root recomputed before and
  after to verify rather than assume. Observation recorded, not repaired mid-delta:
  the schema is pinned by its own sidecar but sits OUTSIDE verifier_root_sha256,
  the same shape as the launcher question A raised at 667.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. No check and
  no fixture has been run; no outcome is claimed; whether the next run's verdict
  validates against A's reading of this schema is what the run tests.)
VERB_AUDIT_SELF = CLEAN (+1 second defect found while conforming the first, worse
  than the reported one because it was latent, disclosed as its own named cause;
  +the const pin caught my own fake test sample before it caught anything real,
  recorded because it was not the outcome I expected.)
```

The reported defect was one extra field. Fixing it properly meant asking what the
schema is *for* — and the answer surfaced a path that had never conformed and
would have failed while trying to report something else. The contract also caught
my test data before it caught any real document, which is the first time in this
build that one of my own guards refused me rather than someone else.
