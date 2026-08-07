# STAGE 8 / TASK 6 / BUILD — THE PARENT'S ACTUAL OUTPUT NAME — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 661 / Task 6 build — one string
Authority: RD-22 + the addendum sealed at Q-588. **THIS ARTIFACT INVOKES NOTHING.**

```text
OUTPUT_PATH = verifier.output.json
DELTA = 1 string (+sidecar)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 note on what independence cost here, §3)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

## 1. THE CHANGE

[PROVABLE] Q-599 records that the 659 relay authored `verifier.verdict.json` from
the producer pattern rather than citing the parent's constant, which the
registrar has since read at source. Corrected:

```text
output_path    "verifier.verdict.json"  ->  "verifier.output.json"     CHANGED
receipt_path   "verifier.receipt.json"  ->  "verifier.receipt.json"    unchanged, was correct
```

Both remain flat and run-root-relative — verified: neither contains `/` or the
platform separator, so neither can resolve into a subdirectory under any run root.

## 2. DELTA AND PIN CHECK

```text
rd22.verifier-manifest.v001.json              373aff8c…  ->  08e6c05862f5e826b912dbcc512125098d494fbfa78d158e2079c34c5aa5bdd1
rd22.verifier-manifest.v001.json.seal.sha256  regenerated, verified OK
```

| Claim | Verified before sealing |
|---|---|
| exactly one string changed | `receipt_path`, all five `input_roots`, and the other eight fields byte-identical |
| **no code changed** | ten module digests re-compared against the prior relay — **all 10 match** |
| instance canonical | round-trip identical; sorted keys; single line; **no trailing newline** (Q-594 canon); 11 fields |
| sidecar verifies | `shasum -c` OK, and equals `manifest_sha256()` = `08e6c058…` |
| ledger guard intact | `require_roots_bound` still refuses, naming `ledger_sha256` alone |
| evidence root retained | `e7820ca5…` — the value run 008 accepted |
| package stable | 17 files; self-check CLEAN |

## 3. SELF VERB AUDIT

| My verb | Check |
|---|---|
| `OUTPUT_PATH` | Taken from the registrar's source citation, not re-derived by me — I have no lawful path to the parent's constant. |
| `DELTA = 1 string` | Checkable: ten code digests and every other manifest field re-compared unchanged. |
| **What independence cost here** | I wrote `verifier.verdict.json` in 659 because the relay specified it, and I could **not** have caught the error: the parent's constant lives in Builder A's code, which is off limits to me. This is the one class of defect the custody split cannot self-correct — a shared constant neither builder may read from the other — and the registrar, who may read both, is the right party to have caught it. I record that as a structural fact, **not** as an excuse: I could have flagged that the name had no source I was permitted to check, and I did not. |
| `CHAIN_INVOKED = false` | Literally true. |

---

```text
OUTPUT_PATH = verifier.output.json (the parent's actual constant per Q-599;
  receipt_path "verifier.receipt.json" was already correct and is unchanged.
  Both remain flat and run-root-relative -- neither contains "/" or the platform
  separator, so neither can resolve into a subdirectory under any run root.)
DELTA = 1 string (+sidecar) (instance 373aff8c… -> 08e6c05862f5e826b912dbcc51212
  5098d494fbfa78d158e2079c34c5aa5bdd1, sidecar regenerated and verified OK and
  equal to manifest_sha256(). NO CODE CHANGED -- ten module digests re-compared
  against the prior relay, all ten match -- and every other manifest field is
  byte-identical, including all five input_roots. Canonical tight form retained:
  sorted keys, single line, no trailing newline, 11 fields. The ledger guard
  still refuses naming ledger_sha256 alone; the evidence root e7820ca5… that run
  008 accepted is retained; 17 files; self-check CLEAN.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. No check and
  no fixture has been run; no outcome is claimed.)
VERB_AUDIT_SELF = CLEAN (+1 note recorded rather than excused: I could not have
  caught this myself, because the parent's constant lives in Builder A's code and
  is off limits to me -- this is the one defect class the two-builder split cannot
  self-correct, and the registrar who may read both sides is the right party to
  have caught it. But I could have flagged that the name I was given had no source
  I was permitted to verify, and I did not.)
```

The useful lesson is narrow and worth one sentence: independence buys convergence
on things both builders can compute, and buys nothing on constants only one of
them may read. `e7820ca5…` was the first kind. This was the second.
