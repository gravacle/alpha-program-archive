# STAGE 8 / TASK 6 / BUILD — THE VERIFIER-MANIFEST INSTANCE — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 654 / Task 6 build — the filled-in launch manifest the parent demands
Authority: RD-22 + the integration addendum sealed at Q-588 (`d17c5e79…`).
**THIS ARTIFACT INVOKES NOTHING.**

```text
REGISTER_HEAD = Q-593
INSTANCE = 11/11 fields, canonical, sidecar-pinned
SCHEMA_VALIDATION = passed
ENTRY_POINT = executable as declared
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 contract defect found in my own addendum, §2.2)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**The parent was right and I was wrong.** I shipped the *contract schema* where
the chain needed the *instance*. Both files now exist with distinct roles, and the
instance is canonical and sidecar-pinned.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-593 | verified (live-append tolerance) |
| Sealed addendum = `d17c5e79986bea431dec0b572019096f9c059bcc43876fda9134abc96ce0f260` | verified |
| Output artifact collision | none — clear to write |
| Instance path collision | none — `evaluator_build_B/rd22.verifier-manifest.v001.json` did not exist |
| `evaluator_build_A/` | **never listed, opened, or searched** |

---

## 1. THE TWO FILES AND THEIR DISTINCT ROLES

[PROVABLE] The name collision was mine, and it is resolved by location, not by
renaming:

| File | Role |
|---|---|
| `contracts/rd22.verifier-manifest.v001.json` | **THE CONTRACT.** A JSON-Schema draft-07 document describing the shape any conforming launch manifest must take. It is a *schema*: it has `$schema`, `properties`, `required`. Builder A conforms to the same contract. |
| `rd22.verifier-manifest.v001.json` *(package root)* | **THE INSTANCE.** Builder B's actual filled-in launch facts — the 11 fields with real values. This is what a parent reads to launch the verifier. |

Both carry a `.seal.sha256` protocol sidecar. The contract lives under
`contracts/` because that is where the shape declarations live; the instance
lives at the package root because that is where a parent looks for *this
package's* launch facts. **Nothing was renamed.**

---

## 2. THE INSTANCE

### 2.1 Displayed in full (indented for reading; the file is canonical single-line)

```json
{
  "argv": [
    "python3", "-m", "verifier.verify",
    "--spec", "${SPEC_PATH}",
    "--ledger", "${LEDGER_PATH}",
    "--ledger-sha256", "${LEDGER_SHA256}",
    "--evidence-dir", "${EVIDENCE_DIR}",
    "--runtime-snapshot", "${RUNTIME_SNAPSHOT_PATH}",
    "--runtime-gate", "${RUNTIME_GATE_PATH}"
  ],
  "entry_point": "verifier.verify",
  "exit_contract": { "fail_closed": 2, "faults_found": 1, "verified": 0 },
  "input_roots": {
    "evidence_root_sha256":    "0000000000000000000000000000000000000000000000000000000000000000",
    "ledger_sha256":           "0000000000000000000000000000000000000000000000000000000000000000",
    "runtime_gate_sha256":     "2ad7f72a88184c11e1253f2c47598fca11e60d05e8e71a26db4e19b16bf98d42",
    "runtime_snapshot_sha256": "50a6fc141a45451678aa7543e4f267ce26beb6e53182170b478acb6fb0e0f5bb",
    "spec_sha256":             "f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b"
  },
  "optimize": false,
  "output_path": "verifier/verdict.json",
  "receipt_authoritative": false,
  "receipt_path": "verifier/receipt.json",
  "schema": "rd22.verifier-manifest.v001",
  "stdout_discipline": {
    "format": "canonical-json", "lines": 1, "other_output_permitted": false
  },
  "verifier_root_sha256": "a8494992fdd5c631ec9df76ac394f9558a0253a2cf008de2be5116ae3e4e50ed"
}
```

```text
FILE   = evaluator_build_B/rd22.verifier-manifest.v001.json
BYTES  = 1145 (canonical: sorted keys, no insignificant whitespace, single line)
SHA256 = 897b4b148af7b180a03e1ad0d451c78a7ebb7012177ba260c8a328404826fac8
SIDECAR= rd22.verifier-manifest.v001.json.seal.sha256   (verified OK)
```

[PROVABLE] Because the manifest's canonical encoding *is* the file's bytes, its
content address and its file digest coincide:
`child_manifest.manifest_sha256(instance)` returns
`897b4b14…`, the same value as the sidecar. The parent's child row can carry that
digest directly.

### 2.2 The two unbound roots — and the contract defect in my own addendum

[PROVABLE] `ledger_sha256` and `evidence_root_sha256` carry the all-zero
**UNBOUND sentinel**, because they are **run-scoped**: they are digests of the
producer's outputs, and a launch manifest authored before that run cannot know
them. Q-591 records that the evidence layer has never been built (0/56 populated,
56 `ABSENT_OF_RECORD`), so they are not merely unknown to me — they do not yet
exist.

[YOURS] **This is a defect in the addendum I myself drafted.** §3.2's
`input_roots` conflates two different kinds of thing:

```text
run-INVARIANT pins (knowable at authoring time):
    spec_sha256, runtime_snapshot_sha256, runtime_gate_sha256
run-SCOPED digests (exist only after the producer runs):
    ledger_sha256, evidence_root_sha256
```

and requires all five to be 64-hex. A conforming instance therefore *cannot* be
authored honestly before the run. **I did not notice this when drafting, because
my verifier never had to emit an instance — the contract passed my own review
precisely because I only ever validated shapes, never produced one.**

**The mitigation, so the placeholder cannot pass unnoticed.** A sentinel that is
a syntactically valid digest is dangerous: it satisfies the schema and could sail
through. So the sentinel is made **self-detecting** —
`contracts.require_roots_bound()` raises `VerifierFault` if any input root is
still the sentinel at run time. Demonstrated at §3.2 below: the verifier refuses
its own manifest until the parent binds the two run-scoped roots.

**The repair I propose for a V002 addendum** (not made here — I do not amend a
sealed document by fiat): split the field into `pinned_roots` (3, authored) and
`run_roots` (2, bound at launch), so the distinction is structural rather than
enforced by a sentinel.

### 2.3 The other fields

- **`argv`** is concrete except for **six named substitution tokens**
  (`${SPEC_PATH}`, `${LEDGER_PATH}`, `${LEDGER_SHA256}`, `${EVIDENCE_DIR}`,
  `${RUNTIME_SNAPSHOT_PATH}`, `${RUNTIME_GATE_PATH}`). A parent that knows
  nothing of this package's internals launches it by substituting exactly those
  and nothing else. The prior code emitted prose like `<spec path>`, which is not
  mechanically substitutable; that is fixed.
- **`optimize: false`** is the normal-run manifest. The `-O` twin is the same
  document with `optimize: true`, which inserts `-O` into `argv` after `python3`
  — declared, never inferred, so R9's normal/optimized pair can be placed at the
  same `common_member_key`.
- **`output_path` / `receipt_path`** are **relative** (`verifier/verdict.json`,
  `verifier/receipt.json`), resolved by the parent against its own run root. I do
  not invent an absolute path into a run root I have never seen.
- **`verifier_root_sha256`** is the digest over the package's source buffers,
  computed exactly as `verify._self_digest()` computes it, and **re-verified
  current after the last edit** (§3.4).

---

## 3. K2 — VALIDATION TRANSCRIPT

### 3.1 Against the contract schema

`jsonschema` is not installed in this environment, so validation uses a
self-contained draft-07 subset checker (`const`, `type`, `pattern`, `required`,
`properties`, `additionalProperties:false`, `items`) written for this purpose:

```text
  properties in schema : 11
  required in schema   : 11
  fields in instance   : 11
  VALIDATION ERRORS    : 0
```

### 3.2 Against the verifier's own closed validator

```text
  validate_verifier_manifest: PASS
  manifest_sha256           : 897b4b148af7b180a03e1ad0d451c78a7ebb7012177ba260c8a328404826fac8
  require_roots_bound       : REFUSES (fail-closed) —
      "input roots ['evidence_root_sha256', 'ledger_sha256'] are still the
       UNBOUND sentinel; the parent must bind the run-scoped roots before launch"
```

[YOURS] The third line is the one that matters. **My verifier refuses my own
manifest**, by design, until the parent supplies what only the parent can know.

### 3.3 Entry point executable as declared

```text
$ python3 -m verifier.verify --help
usage: verify.py [-h] --spec SPEC --ledger LEDGER --ledger-sha256 LEDGER_SHA256
                 --evidence-dir EVIDENCE_DIR --runtime-snapshot RUNTIME_SNAPSHOT
                 --runtime-gate RUNTIME_GATE

  --spec              accepted
  --ledger            accepted
  --ledger-sha256     accepted
  --evidence-dir      accepted
  --runtime-snapshot  accepted
  --runtime-gate      accepted
```

Every flag the instance's `argv` declares is accepted by the real entry point.
`--help` exercises the CLI without invoking the chain.

### 3.4 Package state

```text
self-check          : CLEAN (census live-parsed at 66 ids, 56/10, board 35/13/8/10)
python -O parity    : output BYTE-IDENTICAL to normal
assert statements   : 0
verifier_root_sha256: declared == recomputed  (a8494992…)   CURRENT
```

---

## 4. UPDATED INVENTORY — 17 files

```text
cbbe6583fe829dc0318f814010fdd50b94727b3c8c8538d03f3d9e05f0da915f  README.md
1fdaa0f6181bea11cd264c088dd054499d71bcc0569f3ed3678f5cff20199f29  contracts/rd22.verifier-manifest.v001.json           CONTRACT (schema)
3c28c59c16da0048b0a41a0ba2794f8de59c1c25e7feeca777922ed4372cbb2f  contracts/rd22.verifier-manifest.v001.json.seal.sha256
9a50ce5bd83d0e58c493f64f5a181de963a88ebfd041f72545894909a5d76296  contracts/verifier_verdict.schema.json
897b4b148af7b180a03e1ad0d451c78a7ebb7012177ba260c8a328404826fac8  rd22.verifier-manifest.v001.json                     INSTANCE  NEW
ba848297cd65328c880b58e30002b0aa3447f88044f3a3a417745418e0857af3  rd22.verifier-manifest.v001.json.seal.sha256         NEW
48bfc493edfa39508513393c8a872782cc5a04d5da5f54f1e7b709ba88d40604  selfcheck/selfcheck.py
896bfc3837e7e68fbaab68d922df49f9d05ea69e0489d6a862b696e96d5c3e40  verifier/__init__.py
b1424025b1f1f14fb31c5cdbfd42802229ef8c611677135b9f919e00283147b7  verifier/canonical_json.py
a4ad4b3873695d9a00139ee29380a97215e841b63864edbf181398ab3e74e65f  verifier/child_manifest.py                           CHANGED
dbce53e5f0a30c08f4d3a61d6201b97aeaf037e944f4ca27bdc54131cf2c7025  verifier/comparison.py
b743e0a2814e570fb25f45f400523fce2a65d894c1359f7016188ddf51cfc9c7  verifier/contracts.py                                CHANGED
aee8826ceeed26ec1da7b7859d2c08b7d3d67be3dc873ccdae715a067ebf0632  verifier/hashing.py
eeefe1424559ff31ebdde7803fdf417190536c39c16bdb641fb8da1b559980b2  verifier/replay.py
081c6b41f7c00ffdd6d586e8afb74e5a70a857911cde2b94c294579c0a67bde9  verifier/runtime_state.py
d38a66cdaa029addf342fe571fd6c212ed09f522df14e24f46bfc1331f307048  verifier/spec_census.py
e342a381e6d3d913138469e8c2b59517858a66ae557d8ce3a6d99934c107c480  verifier/verify.py
```

**Changed:** `child_manifest.py` (real substitution tokens replacing prose
placeholders), `contracts.py` (`UNBOUND_ROOT_SENTINEL`, `RUN_SCOPED_ROOTS`,
`require_roots_bound`). **New:** the instance and its sidecar. Everything else
byte-unchanged, including the independence core `spec_census.py`.

*(The `contracts/…seal.sha256` file pins the contract schema; its digest matches
that file exactly. I did not author it in this relay and record that rather than
present it as deliberate — it is correct, and pinning the contract is right, but
I did not intend it here.)*

---

## 5. BATTERY

### 5.1 Pre-seal pin check

| Claim | Verified before sealing |
|---|---|
| instance is canonical | round-trip `dumps_canonical(loads_strict(raw)) == raw`; keys sorted; no trailing whitespace |
| 11 fields | counted from the parsed instance |
| sidecar verifies | `shasum -c` OK |
| content address == file digest | `manifest_sha256()` equals the sidecar value |
| schema validation 0 errors | 11 properties / 11 required / 11 fields |
| sentinel is self-detecting | `require_roots_bound` raises on this very instance |
| entry point executable | all six declared flags accepted by `--help` |
| `verifier_root_sha256` current | recomputed after the last edit and compared |
| 17 files, digests as listed | `find` + `shasum` after `__pycache__` removal |

### 5.2 `F_PLDEC` and fences

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. `--help` was executed; **the chain was not**. No
descriptor or fixture ran. `alpha_computed = false`; `proof_authorized = false`;
`kappa_record_computed = false`; no member bound; no fixed point; no end test; no
numeric evaluation; no comparison to any measured constant.

### 5.3 Coverage, stated exactly (VERDICT-LINE SCOPE RULE)

I produced **the instance, its sidecar, and two supporting code changes**, and
validated the instance against its schema, against the verifier's own closed
validator, and against the real entry point's CLI. I did **not** invoke the
chain, and I claim **no check or fixture outcome**. I did **not** read Builder A's
code, so I claim **no agreement between the implementations**. The two unbound
roots mean this manifest is **not yet launchable as it stands** — the parent must
bind them, and my verifier will refuse until it does. My verdict lines claim a
canonical sidecar-pinned 11-field instance, a passing schema validation, and an
executable entry point — **and nothing else.**

---

## 6. SELF VERB AUDIT

| My verb | Check |
|---|---|
| `INSTANCE = 11/11, canonical, sidecar-pinned` | Displayed in full; canonicality proved by round-trip; sidecar verified; content address equals file digest. |
| `SCHEMA_VALIDATION = passed` | 0 errors against the draft-07 contract, with the validator's limits stated (`jsonschema` unavailable; a subset checker was written and its supported keywords named). |
| `ENTRY_POINT = executable as declared` | All six declared flags accepted by the real CLI. `--help` only — no chain invocation. |
| The parent's finding | Accepted without argument. I shipped a schema where an instance was needed, and the reason is worth recording: **my package only ever validated manifest shapes and never produced one**, so the gap could not surface in my own self-check. |
| **Contract defect, found in my own addendum** | §3.2 conflates run-invariant pins with run-scoped digests. I name it, mitigate it with a self-detecting sentinel, and **propose** rather than perform the V002 split — a sealed document is not amended by the lane that noticed. |
| Sentinel honesty | A schema-valid placeholder that passes silently would be the worst of both worlds. `require_roots_bound` makes the verifier refuse its own manifest until the parent binds. |
| Stray sidecar | The `contracts/` pin is correct but not authored by me in this relay; recorded as such rather than presented as intentional. |
| `CHAIN_INVOKED = false` | Literally true. Builder B does not run what Builder B wrote. |

---

```text
INSTANCE = 11/11 fields, canonical, sidecar-pinned
  (evaluator_build_B/rd22.verifier-manifest.v001.json, 1145 bytes, sorted keys,
   no insignificant whitespace, single line;
   sha256 897b4b148af7b180a03e1ad0d451c78a7ebb7012177ba260c8a328404826fac8 with
   its .seal.sha256 protocol sidecar verified OK. The manifest's canonical
   encoding IS the file's bytes, so manifest_sha256() and the sidecar coincide
   and the parent's child row can carry that digest directly.
   The CONTRACT SCHEMA stays at contracts/rd22.verifier-manifest.v001.json --
   two files, distinct roles, nothing renamed.
   TWO ROOTS ARE THE UNBOUND SENTINEL and this manifest is NOT YET LAUNCHABLE as
   it stands: ledger_sha256 and evidence_root_sha256 are RUN-SCOPED digests of
   producer outputs that Q-591 records do not yet exist. This is a defect in the
   addendum I MYSELF DRAFTED -- §3.2 conflates run-invariant pins with run-scoped
   digests and demands 64-hex for both -- which I missed because my package only
   ever validated shapes and never emitted an instance. Mitigated so it cannot
   pass unnoticed: require_roots_bound() makes the verifier REFUSE ITS OWN
   MANIFEST until the parent binds them. A V002 split into pinned_roots(3) and
   run_roots(2) is PROPOSED, not performed.)
SCHEMA_VALIDATION = passed (0 errors; 11 properties / 11 required / 11 fields.
  jsonschema is not installed here, so a self-contained draft-07 SUBSET checker
  was written -- const, type, pattern, required, properties,
  additionalProperties:false, items -- and its limits are stated rather than left
  implied. The instance also passes the verifier's own closed
  validate_verifier_manifest.)
ENTRY_POINT = executable as declared (all six flags of the declared argv accepted
  by the real CLI; argv is concrete except for six NAMED substitution tokens a
  parent fills mechanically, replacing the prose placeholders like "<spec path>"
  that were not substitutable. --help only; the chain was not invoked.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. No check and
  no fixture has been run; no outcome is claimed; Builder A's code was not read,
  so no agreement between implementations is claimed either.)
VERB_AUDIT_SELF = CLEAN (+1 contract defect found in my own sealed addendum and
  named rather than worked around; +the parent's finding accepted without
  argument, with the reason it escaped my self-check recorded -- I validated
  manifest shapes and never produced one; +1 stray sidecar disclosed as correct
  but not deliberately authored in this relay.)
```

The gate caught something my own self-check structurally could not: a package
that validates a shape will never notice that it has not produced one. The
instance is written and the contract defect behind the delay is named — including
that I wrote the contract. What is not fixed is that two of its five roots cannot
exist until the producer has run, so the manifest is not launchable until the
parent binds them, and the verifier now says so out loud rather than proceeding
against a zero digest.
