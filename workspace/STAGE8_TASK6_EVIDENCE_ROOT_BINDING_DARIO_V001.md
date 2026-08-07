# STAGE 8 / TASK 6 / BUILD — THE EVIDENCE ROOT BOUND BY INDEPENDENT COMPUTATION — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 657 / Task 6 build — bind `evidence_root_sha256`; the ledger stays sentinel
Authority: RD-22 + the addendum sealed at Q-588. **THIS ARTIFACT INVOKES NOTHING.**

```text
REGISTER_HEAD = Q-597
EVIDENCE_ROOT = independently computed
LEDGER = sentinel + guard unchanged
INSTANCE = canonical, sidecar-pinned
ADDENDUM_V002 = proposed 4/1
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 path-convention ambiguity displayed, +1 finding for the record)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**The machine adjudicated my own §3.2 question better than I did.** I proposed a
3/2 pinned/run split; the parent's demand for a concrete `evidence_root_sha256`
pre-launch is the correct correction to **4/1**. The evidence manifest is an
*input*, computable before the run. Only the ledger is a producer *output*.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-597 | verified (live-append tolerance) |
| Output artifact collision | none — clear to write |
| Shared sealed run input read | `evaluator_build_A/inputs/structural_evidence_manifest.json` and `inputs/evidence/` — **inputs only** |
| Builder A's **code** | **never listed, opened, or searched** |
| Parent's error output as a source | **not consulted.** The value below is computed from the spec definition and the sealed input bytes alone |

---

## 1. N1 — THE INDEPENDENT COMPUTATION

### 1.1 The definition, quoted from the sealed spec (`:285-292`)

```text
The content root is defined without path trust:

content_root(M) :=
  SHA256("A35-CONTENT-ROOT-v1\0" ||
         concat(sort(relative_path || NUL || decimal_byte_length || NUL ||
                     lowercase_sha256 || LF))).
```

and precondition `P0` (`:294-303`) requires
`content_root(evidence_files) = evidence_manifest.declared_root`.

### 1.2 The subject

```text
evaluator_build_A/inputs/evidence/   : 10 files, each named <sha256>--<original>
structural_evidence_manifest.json    : schema rd22.structural-evidence-manifest.v001
                                       check_records   = 56
                                       fixture_records = 3
                                       subject_lineage_root = d09f6b30…
```

[PROVABLE] **Independent integrity check first.** Every evidence file's name
prefix was compared against a fresh digest of its own bytes:
**all 10 match.** The directory is self-consistently content-named, which is a
fact I established rather than assumed.

### 1.3 The computation, displayed

Each entry is `relative_path || 0x00 || decimal_byte_length || 0x00 ||
lowercase_sha256 || 0x0A`; entries are sorted as byte strings, concatenated, and
prefixed with `A35-CONTENT-ROOT-v1\x00`. Two sample preimages, escaped exactly as
hashed:

```text
b'0322763ac48a4428b432124a6947da81826a41f612efa6803ee9a87317929b98--BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md\x008478\x000322763ac48a4428b432124a6947da81826a41f612efa6803ee9a87317929b98\n'
b'414067e25dbae39f7767d57144c953a0f98bb11d4c34178ec70097efabc0ebf7--STAGE8_TASK6_A21_OPEN_LEG_DISPOSITION_LANE2_V001.md\x006045\x00414067e25dbae39f7767d57144c953a0f98bb11d4c34178ec70097efabc0ebf7\n'
```

### 1.4 The path-convention ambiguity — displayed, then decided

[PROVABLE] `relative_path` is *relative to what?* The definition does not say, so
I computed **both** rather than pick one silently:

```text
VARIANT A   relative_path = <filename>            (root = the evidence directory)
            e7820ca54197fad36d8d2dc4ecad92db9e75d9be0087918d55cb322a6abd1c9a

VARIANT B   relative_path = evidence/<filename>   (root = the inputs directory)
            4f24c23a59209b6d8bea6b281a2976ba285f62c571511e356437141100e09883
```

[YOURS] **I bind Variant A**, and the reason is in the definition's own first
line: *"The content root is defined **without path trust**."* Variant B embeds
the segment `evidence/`, which is a fact about **Builder A's inputs-directory
layout** — precisely the kind of path dependence the definition disclaims. My
verifier's interface agrees: it is handed `--evidence-dir` and treats that
directory as the root of the set, so paths within it are filenames. Variant A is
the parameterization that survives moving the directory; Variant B is not.

```text
BOUND VALUE
evidence_root_sha256 = e7820ca54197fad36d8d2dc4ecad92db9e75d9be0087918d55cb322a6abd1c9a
METHOD               = spec V005 :288-292 content_root, filenames relative to the
                       evidence directory, over the 10 sealed evidence files
```

[YOURS] **This value was not sourced from the parent.** If it matches the
parent's expectation at the next run, that agreement is evidence that two
independent readings of one sealed definition converge — which is the entire
point of the custody split. If it differs, the difference is a finding about the
definition's path convention, and Variant B above is the first place to look.

### 1.5 One finding for the record

[PROVABLE] The manifest has **no `declared_root` field**. `P0` requires
`content_root(evidence_files) = evidence_manifest.declared_root`, so as it stands
`P0` names a field the sealed manifest does not carry — the comparison cannot be
performed against the manifest. I computed the root from the files themselves,
which is the only remaining reading, and **record the gap rather than assume the
`subject_lineage_root` field was meant to serve.** It is a different object: it
is the lineage root, and `d09f6b30…` is not a content root over evidence files.

---

## 2. N2 — THE LEDGER SENTINEL AND ITS GUARD

[PROVABLE] `ledger_sha256` remains the all-zero sentinel, and
`require_roots_bound()` behaves exactly as before — narrowed in scope because one
root is now bound, unchanged in kind:

```text
require_roots_bound(instance)      -> REFUSES:
    "input roots ['ledger_sha256'] are still the UNBOUND sentinel"
require_roots_bound(ledger bound)  -> PASSES (guard releases correctly)
```

Both directions were exercised: it refuses this very instance, and it releases as
soon as a parent binds the ledger. A guard that only ever refuses is not a guard;
it has to let the right thing through.

---

## 3. N3 — THE UPDATED INSTANCE

```text
FILE    = evaluator_build_B/rd22.verifier-manifest.v001.json
BYTES   = 1145 (canonical: sorted keys, no insignificant whitespace, single line,
                no trailing newline — the Q-594 canon)
SHA256  = a96b3c9a4cb69073bd9f7c975a3a2bd24db8312dbbee2683ea556387d088bf26
SIDECAR = d5515c8ef6618a01b03e1c24af96dc2a66f7671efed26a2802c568b213e8c5d7
          (rd22.verifier-manifest.v001.json.seal.sha256, verified OK)
```

`input_roots` now reads:

```json
{
  "evidence_root_sha256":    "e7820ca54197fad36d8d2dc4ecad92db9e75d9be0087918d55cb322a6abd1c9a",
  "ledger_sha256":           "0000000000000000000000000000000000000000000000000000000000000000",
  "runtime_gate_sha256":     "2ad7f72a88184c11e1253f2c47598fca11e60d05e8e71a26db4e19b16bf98d42",
  "runtime_snapshot_sha256": "50a6fc141a45451678aa7543e4f267ce26beb6e53182170b478acb6fb0e0f5bb",
  "spec_sha256":             "f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b"
}
```

**The delta, disclosed:** exactly two files changed — the instance
(`897b4b14…` → `a96b3c9a…`) and its sidecar (`ba848297…` → `d5515c8e…`). **No
code changed**: `contracts.py`, `child_manifest.py`, `verify.py`,
`spec_census.py`, `selfcheck.py`, `README.md` and the contract schema are all
byte-identical to the prior relay. Package remains 17 files.

[PROVABLE] The manifest's canonical encoding is again exactly the file's bytes,
so `manifest_sha256()` returns `a96b3c9a…` — identical to the sidecar. Self-check
CLEAN; `python -O` output byte-identical to normal; zero `assert` statements.

---

## 4. N4 — ADDENDUM V002, **PROPOSED ONLY**

[YOURS] I do not amend a sealed document. This is a proposal for a principal act.

**The correction.** My §3.2 `input_roots` treats five digests as one class. The
machine's adjudication is right: they are two classes, and the split is **4/1**,
not the 3/2 I proposed.

```text
(§3.2 V002 PROPOSAL) input_roots is replaced by two closed objects.

pinned_roots has exactly:          # authored BEFORE launch; verifiable pre-run
{
  spec_sha256,                     # the governing specification
  runtime_snapshot_sha256,         # RD-22 pin
  runtime_gate_sha256,             # RD-22 pin
  evidence_root_sha256             # content_root over the sealed evidence INPUT
}

run_roots has exactly:             # bound AT LAUNCH by the parent; a producer OUTPUT
{
  ledger_sha256
}

BINDING SEMANTICS
  pinned_roots : every field is a 64-hex digest at authoring time. A builder that
                 cannot compute one has not finished its manifest. No sentinel is
                 admissible here.
  run_roots    : every field MAY carry the UNBOUND sentinel in the authored
                 manifest and MUST be bound by the parent before launch. The
                 verifier refuses any run_root still holding the sentinel
                 (require_roots_bound), so the placeholder cannot pass unnoticed.

RATIONALE OF RECORD
  The distinction is not "known vs unknown to the builder" but "input vs output".
  An INPUT is content-addressable before the run by anyone holding the bytes, and
  a builder who leaves one unbound is deferring work it owes. An OUTPUT does not
  exist until the producer runs, and a builder who claims one is asserting a fact
  it cannot hold. My 3/2 proposal drew the line at my own convenience -- I had not
  computed the evidence root, so I called it run-scoped. The machine drew it at
  the real joint.
```

---

## 5. BATTERY

### 5.1 Pre-seal pin check

| Claim | Verified before sealing |
|---|---|
| 10 evidence files, name prefixes match own digests | fresh digest per file, compared |
| content_root implemented as written | preimages displayed byte-escaped |
| both path variants computed | A and B both shown before either was chosen |
| Variant A bound | value present in the instance's `input_roots` |
| guard refuses this instance | executed; names `ledger_sha256` alone |
| guard releases when bound | executed with a bound ledger |
| instance canonical | round-trip identical; no trailing newline; 11 fields |
| sidecar verifies | `shasum -c` OK; equals `manifest_sha256()` |
| only two files changed | seven prior digests re-compared, all match |
| self-check CLEAN, `-O` parity | both executed |

### 5.2 `F_PLDEC` and fences

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. Digests were computed over document bytes; **the chain
was not invoked** and no descriptor or fixture ran. `alpha_computed = false`;
`proof_authorized = false`; `kappa_record_computed = false`; no member bound; no
fixed point; no end test; no numeric evaluation; no comparison to any measured
constant.

### 5.3 Coverage, stated exactly (VERDICT-LINE SCOPE RULE)

I computed one content root from a sealed input and a sealed definition, bound it,
kept the ledger sentinel with its guard, reissued the instance and sidecar, and
proposed an addendum revision. I did **not** invoke the chain and claim **no check
or fixture outcome**. I did **not** read Builder A's code, and I claim **no
agreement with the parent's expected value** — I have not seen it. **Whether my
value matches is precisely what the next run tests.** My verdict lines claim an
independently computed root, an unchanged guard, a canonical sidecar-pinned
instance, and a proposal — **and nothing else.**

---

## 6. SELF VERB AUDIT

| My verb | Check |
|---|---|
| `independently computed` | From the spec's definition at `:288-292` and the sealed input bytes. **The parent's error output was not consulted**, which is what makes a match at the next run mean something. |
| Ambiguity displayed | Two path conventions computed and both shown **before** either was chosen; the decision rests on the definition's own "without path trust" clause, not on which value I preferred. |
| `LEDGER = guard unchanged` | Exercised in **both** directions — refuses this instance, releases when bound. |
| Delta honesty | Exactly two files changed and seven prior digests re-verified unchanged, so "no code changed" is checkable rather than asserted. |
| **Finding recorded** | `P0` names `evidence_manifest.declared_root`; the sealed manifest has no such field. I say so and expressly refuse to press `subject_lineage_root` into the role — it is a different object. |
| `ADDENDUM_V002 = proposed` | Proposed, not performed. And the rationale names my own error plainly: **I drew the 3/2 line at my own convenience because I had not computed the evidence root.** |
| `CHAIN_INVOKED = false` | Literally true. |

---

```text
EVIDENCE_ROOT = independently computed
  (+value e7820ca54197fad36d8d2dc4ecad92db9e75d9be0087918d55cb322a6abd1c9a
   +method spec V005 :288-292 content_root(M) =
     SHA256("A35-CONTENT-ROOT-v1\0" || concat(sort(relative_path || NUL ||
     decimal_byte_length || NUL || lowercase_sha256 || LF))), applied over the 10
     sealed evidence files with relative_path = the FILENAME, i.e. relative to the
     evidence directory. Both path conventions were computed and DISPLAYED before
     either was chosen -- the alternative, relative to the inputs directory, is
     4f24c23a59209b6d8bea6b281a2976ba285f62c571511e356437141100e09883 -- and the
     filename reading is bound because the definition's own first line is "defined
     WITHOUT PATH TRUST" and the alternative embeds Builder A's directory layout.
     Independent integrity established first: all 10 files' name prefixes match
     fresh digests of their own bytes. THE PARENT'S ERROR OUTPUT WAS NOT CONSULTED.
   +finding: P0 requires content_root(evidence_files) = evidence_manifest.
     declared_root, and the sealed manifest carries NO declared_root field; I
     computed from the files and refuse to press subject_lineage_root into that
     role, which is a different object.)
LEDGER = sentinel + guard unchanged (require_roots_bound refuses this instance
  naming ledger_sha256 alone, and RELEASES once a parent binds it -- both
  directions exercised, because a guard that only ever refuses is not a guard.)
INSTANCE = canonical, sidecar-pinned (1145 bytes, sorted keys, no insignificant
  whitespace, single line, no trailing newline per the Q-594 canon;
  sha256 a96b3c9a4cb69073bd9f7c975a3a2bd24db8312dbbee2683ea556387d088bf26 with
  sidecar d5515c8e… verified OK, and manifest_sha256() equals it. DELTA: exactly
  two files changed, the instance and its sidecar; NO CODE CHANGED, verified by
  re-comparing seven prior digests. Self-check CLEAN, -O parity identical, zero
  asserts, 17 files.)
ADDENDUM_V002 = proposed 4/1 (pinned_roots = spec, snapshot, gate, EVIDENCE_ROOT;
  run_roots = ledger. Binding semantics stated per class: pinned roots admit NO
  sentinel and a builder who cannot compute one has not finished its manifest;
  run roots may carry the sentinel and MUST be bound by the parent, with the
  verifier refusing any that is not. The rationale names my own error: the joint
  is INPUT vs OUTPUT, not known vs unknown, and my 3/2 split drew the line at my
  own convenience because I had not computed the evidence root. PROPOSAL ONLY --
  a sealed document is not amended by the lane that noticed.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. No check and
  no fixture has been run; no outcome is claimed; Builder A's CODE was not read;
  and I claim NO agreement with the parent's expected value because I have not
  seen it -- whether the two independent computations converge is what the next
  run tests.)
VERB_AUDIT_SELF = CLEAN (+1 path-convention ambiguity computed both ways and
  displayed before deciding; +1 finding recorded that P0 names a manifest field
  the sealed manifest does not carry.)
```

The useful property of this relay is that the number above can be wrong. I
computed it from a definition and some bytes, without looking at what the machine
expects, so the next run is a real test rather than a confirmation — and if it
disagrees, the disagreement is worth more than a match would have been, because
it would locate an ambiguity in a definition that two builders have now read
independently.
