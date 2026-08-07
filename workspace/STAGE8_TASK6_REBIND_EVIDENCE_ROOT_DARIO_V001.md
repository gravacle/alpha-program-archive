# STAGE 8 / TASK 6 / BUILD — THE EVIDENCE ROOT REBOUND FOR THE 12-PAYLOAD STATE — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 684 / Task 6 build — one field, recomputed not received
Authority: RD-22. **THIS ARTIFACT INVOKES NOTHING.**

```text
EVIDENCE_ROOT = independently recomputed (1fbb3c07…)
DELTA = 1 field (+sidecar)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 stale comment named and NOT repaired here, §4.1)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**The stop is the handshake working.** Run 023 halted at `VERIFIER_INPUT_ROOT`
because my instance attested the 10-payload root while the evidence set had moved
to 12. A stale attestation was **caught rather than silently accepted**, which is
what an independently computed root is for. The repair is one field.

## 1. THE COMPUTATION — mine, from bytes

[PROVABLE] The value below was computed from the **evidence files' own bytes**.
I did not read it from the parent's error display, from the manifest's
`declared_root`, or from my own 683 check. The manifest appears in §1.3 only as a
cross-check I observe *after* computing — never as a source. That is the 657
discipline, and it is the BR-1 direction: my instance attests what I derived, and
a producer-declared root is evidence about the producer, not about the evidence.

### 1.1 The recipe, as written in the spec

Spec V005 `:288-292`, applied literally — the definition is stated *"without path
trust"*, and `relative_path` is the filename, i.e. relative to the evidence
directory itself (the convention I fixed at 657 and used again here):

```text
content_root(M) := SHA256( "A35-CONTENT-ROOT-v1\0" ||
                           concat(sort( relative_path || NUL ||
                                        decimal_byte_length || NUL ||
                                        lowercase_sha256 || LF )) )
```

### 1.2 The twelve preimage lines

Every byte length and digest below was taken from the file, not from any
declaration. Payload names are content-addressed, so the leading 64 hex of each
line is also the digest I computed — a self-check the format gives for free, and
all twelve agree.

```text
EVIDENCE FILES = 12
sort(preimage bytes) == sort(filename) : True     (no reordering surprise)

[ 0] 0322763a…--BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md      8478 B
[ 1] 344fecdc…--C-B-V009-06-dag-args.json                                    1218 B   <- NEW
[ 2] 414067e2…--STAGE8_TASK6_A21_OPEN_LEG_DISPOSITION_LANE2_V001.md          6045 B
[ 3] 47e7c329…--C-B-V009-06-stage_dependencies.member                         932 B   <- NEW
[ 4] 5c679e37…--BID_SOURCE_PARENT_CLOSURE_GATE_V003.md                      10997 B
[ 5] 76589e94…--STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V005.md                78368 B
[ 6] 9d35f4ed…--STAGE7_PACKET_MANIFEST_V001.sha256                          13786 B
[ 7] a83289e6…--STAGE8_TASK6_LP_MATRIX_LEDGER_REVIEW_DARIO_V001.md          18647 B
[ 8] aa7c6d49…--BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md               78794 B
[ 9] bc6c3e49…--STAGE8_TASK6_LP_MATRIX_LEDGER_LANE3_V001.md                 51952 B
[10] c09f2c24…--BID_FULL_STACK_REVIEW_LEDGER_V003.md                        24108 B
[11] f8d1a7dc…--STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md              162641 B

PREFIX          = 'A35-CONTENT-ROOT-v1' + 0x00        20 bytes
PREIMAGE TOTAL  = 2175 bytes
content_root    = 1fbb3c0771e3c58dc87db6fcc5dad286331c25c051c98a1afeac3ec3fecb64a6
```

### 1.3 The control, and the cross-check

[PROVABLE] **The control is the load-bearing part of this section.** The *same*
function, over the *prior* ten payloads, reproduces the exact value my instance
was attesting before this relay:

```text
content_root(10 payloads) = e7820ca54197fad36d8d2dc4ecad92db9e75d9be0087918d55cb322a6abd1c9a
                            == the value the shipped instance carried            True
content_root(12 payloads) = 1fbb3c0771e3c58dc87db6fcc5dad286331c25c051c98a1afeac3ec3fecb64a6
```

So the recipe did not change; only the census did. Without that control I would
be asserting a new number with nothing to distinguish "the evidence moved" from
"my method drifted" — which is the whole reason the old value is worth
recomputing rather than remembering.

The two added members are exactly the envelope's, and nothing else moved:

```text
+ 1218 B  344fecdc…  C-B-V009-06-dag-args.json
+  932 B  47e7c329…  C-B-V009-06-stage_dependencies.member
  ten prior payloads: byte lengths and digests unchanged
```

Cross-check, observed after the fact and **not** used as a source:

```text
parent manifest payload_inventory == my byte-derived census : True
parent manifest declared_root                               : 1fbb3c07…
my independently computed root                              : 1fbb3c07…
AGREE                                                       : True
```

Two builders, two computations, one value. That agreement is the point of the
field; it is not what produced my value.

## 2. THE DELTA — one field

```text
CHANGED  rd22.verifier-manifest.v001.json
           input_roots.evidence_root_sha256
             e7820ca54197fad36d8d2dc4ecad92db9e75d9be0087918d55cb322a6abd1c9a
          -> 1fbb3c0771e3c58dc87db6fcc5dad286331c25c051c98a1afeac3ec3fecb64a6
           instance digest ddd340a4… -> a65cc1a5a277b6d08e8708cfcf4831dff022cd005752bfc52d0ce7e1b5fac63d
CHANGED  rd22.verifier-manifest.v001.json.seal.sha256   regenerated, verified OK
UNCHANGED  every verifier/*.py, run_verifier.py, both contracts, selfcheck
UNCHANGED  verifier_root_sha256                          dba5377d…
```

Asserted, not eyeballed:

```text
leaf paths in the instance : 32
leaf paths CHANGED         : 1   ['.input_roots.evidence_root_sha256']
key sets identical         : True    (nothing added, nothing dropped)
byte length                : 1139 -> 1139   (a hex digest replaced a hex digest)
```

The instance stayed the same size because one 64-hex value replaced another. That
is a coincidence of the delta, not a check — the leaf-path comparison is the check.

### 2.1 Canonical form

```text
single line, no trailing newline : True
sorted keys, tight separators    : True
round-trip identical             : True
top-level fields                 : 11
manifest_sha256(parsed)          : a65cc1a5…   == the file digest == the sidecar
sidecar `shasum -c`              : OK
```

`manifest_sha256()` runs the instance back through
`validate_verifier_manifest()`, so the digest I sealed is a digest of something my
own contract validator accepted, not merely of bytes I wrote.

## 3. WHY THE PACKAGE ROOT DID NOT MOVE — and a divergence that cannot happen

[PROVABLE] `verifier_root_sha256` covers the entry point, the ten `verifier/*.py`
modules and the verdict schema. The **instance is not a root member** — it is the
thing that *carries* the root — so rebinding it cannot move the root, and I
verified rather than assumed:

```text
package_root_digest(base)                      = dba5377d…   (recomputed from shipped code)
instance.verifier_root_sha256                  = dba5377d…   AGREE
```

[PROVABLE] I also checked the failure mode that would make this dangerous — a
root literal frozen into the code, where the instance and the code could drift
apart invisibly, because the code is inside the root digest and the instance is
not:

```text
grep for 'e7820ca5' or '1fbb3c07' in verifier/, run_verifier.py, selfcheck/, contracts/  ->  NONE
build_manifest(verifier_root_sha256, input_roots, output_path, receipt_path, optimize)
    takes input_roots as a PARAMETER; no root value is embedded anywhere
build_manifest(shipped inputs) == the shipped instance                        True
its canonical encoding == the shipped file bytes                              True
```

So the instance is the **sole carrier** of the evidence root, and code/instance
divergence is structurally impossible rather than merely absent today.

### 3.1 The ledger guard is untouched and still refuses

```text
require_roots_bound(instance) raises:
  "input roots ['ledger_sha256'] are still the UNBOUND sentinel;
   the parent must bind the run-scoped roots before launch"
```

`ledger_sha256` remains `0`×64 by design: the producer's ledger does not exist
when the launch manifest is authored, and a placeholder that passes unnoticed is
worse than one that fails closed. Binding the evidence root does not weaken that
— the guard is generic over all five roots and still fires on the one that is
genuinely unbindable in advance.

## 4. PIN CHECK

| Claim | Verified before sealing |
|---|---|
| root computed from file bytes, not received | twelve preimage lines displayed; content-addressed names cross-check every digest |
| the recipe did not drift | **control**: same function reproduces `e7820ca5…` over the prior ten |
| only the envelope's two payloads were added | ten prior lengths and digests unchanged |
| parent agreement is a cross-check, not a source | computed first, compared second |
| exactly one field changed | 1 of 32 leaf paths; key sets identical |
| instance canonical | single line, sorted, no trailing newline, 11 fields, round-trip identical |
| instance validates through my own contract | `manifest_sha256()` == file digest == sidecar `a65cc1a5…` |
| sidecar regenerated and verifies | `shasum -c` OK |
| package root unmoved | `package_root_digest()` recomputed = `dba5377d…`, equal to the instance's field |
| no root literal in shipped code | grep NONE; `build_manifest` reproduces the instance from parameters |
| ledger guard intact | fires, naming `ledger_sha256` alone |
| T-label contexts, output paths, exit contract, stdout discipline | unchanged |
| self-check CLEAN; 19 files; zero `assert` in runtime | executed |
| dry run, both cwds; stdout canon | exit 2; 372 bytes; last byte `0x7d`; `rstrip() == raw`; stderr 0 |

### 4.1 One observation named, not repaired here

[YOURS] `verifier/contracts.py:125-132` says both `RUN_SCOPED_ROOTS` — the ledger
digest and the evidence root — "cannot exist when the launch manifest is authored"
and that "the instance therefore carries this sentinel for them." Since relay 657
that is only true of `ledger_sha256`: the evidence set is sealed before launch, so
its root **can** be computed in advance, and this relay binds it for the second
time. The comment is stale; the code is not, because `require_roots_bound()` tests
the sentinel value rather than the field name.

I am not fixing it here. A delta with two causes cannot be checked, and the
commission is one field plus the sidecar — the same reason I left the verdict
schema outside the root at 674 and closed it as its own relay at 676. It costs one
line to record and one relay to repair.

### 4.2 `F_PLDEC` and coverage

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. **The chain was not invoked**; the demonstration is the
dry run, which opens no run input, and the hashing of sealed evidence bytes, which
starts no procedure. `alpha_computed = false`; `proof_authorized = false`;
`kappa_record_computed = false`; no member bound; no fixed point; no end test; no
numeric evaluation; no comparison to any measured constant.

**Coverage, stated exactly.** I rebound one attestation and reissued the instance.
I claim **no check or fixture outcome**, and I do **not** claim run 023 now
succeeds: `VERIFIER_INPUT_ROOT` was the point the run reached, not necessarily the
only thing standing in front of it, and what the next attempt reaches is what the
run tests. I also do not adjudicate the parent's report of the stop — I repaired
the attestation that caused it.

## 5. SELF VERB AUDIT

| My verb | Check |
|---|---|
| `independently recomputed` | From the twelve files' bytes, with the preimage recipe displayed and every line shown. The parent's manifest was read **after** the computation and used only as a cross-check. |
| The control, not just the result | The same function reproduces the value I was previously attesting. A new number with no control cannot distinguish "the evidence moved" from "my method drifted." |
| `DELTA = 1 field` | 1 of 32 leaf paths, key sets identical — asserted from the parsed objects, not inferred from equal byte lengths, which were equal by coincidence. |
| Root unmoved | Recomputed from the shipped code and compared, not presumed to have survived. |
| The dangerous case checked | A root literal in the code would let instance and code drift invisibly; I grepped for it and showed `build_manifest` takes the value as a parameter. |
| Observation deferred, not smuggled | The stale `RUN_SCOPED_ROOTS` comment is named and left; third time this discipline has applied. |
| `CHAIN_INVOKED = false` | Literally true. Builder B does not run what Builder B wrote. |
| No claim on run 023 | The stop is where the run reached; I do not promise what the next attempt reaches. |

---

```text
EVIDENCE_ROOT = independently recomputed (1fbb3c0771e3c58dc87db6fcc5dad286331c25c0
  51c98a1afeac3ec3fecb64a6, computed from the twelve evidence files' OWN BYTES under
  spec V005 :288-292 content_root with relative_path = the filename: twelve preimage
  lines displayed, 20-byte prefix, 2175-byte preimage total, and every line's leading
  content-addressed name agreeing with the digest I computed. THE CONTROL IS THE
  LOAD-BEARING PART: the same function over the prior TEN payloads reproduces
  e7820ca54197fad36d8d2dc4ecad92db9e75d9be0087918d55cb322a6abd1c9a, exactly the value
  the shipped instance was attesting -- so the recipe did not drift and only the census
  moved, the two added members being precisely the envelope's dag-args (1218 B) and
  relocated member (932 B) with the ten prior lengths and digests unchanged. NEVER
  SOURCED FROM THE PARENT: not from its error display, not from its declared_root, not
  from my own 683 check. The parent's manifest appears only as a cross-check observed
  AFTER computing -- payload_inventory matches my byte-derived census and declared_root
  agrees -- which is the BR-1 direction, since a producer-declared root is evidence
  about the producer. Two builders, two computations, one value.)
DELTA = 1 field (+sidecar) (input_roots.evidence_root_sha256 only: 1 of 32 leaf paths
  changed, key sets identical, nothing added or dropped -- asserted from the parsed
  objects, NOT inferred from the byte length, which stayed 1139 only because one 64-hex
  digest replaced another. Instance ddd340a4… -> a65cc1a5a277b6d08e8708cfcf4831dff022c
  d005752bfc52d0ce7e1b5fac63d; canonical single line, sorted keys, no trailing newline,
  11 fields, round-trip identical; manifest_sha256() runs it back through
  validate_verifier_manifest() and equals the file digest and the regenerated sidecar,
  which verifies OK. verifier_root_sha256 DID NOT MOVE (dba5377d…, recomputed from the
  shipped code and compared) because the instance is not a root member but the thing
  that carries the root -- and the failure mode that would make that dangerous is
  structurally absent: no root literal exists anywhere in the shipped code, and
  build_manifest takes input_roots as a PARAMETER and reproduces the shipped instance
  byte-for-byte from it, so instance/code divergence cannot occur rather than merely
  not having occurred. Ledger guard intact and still refusing, naming ledger_sha256
  alone; T-label contexts, output paths, exit contract and stdout discipline unchanged;
  19 files; zero asserts; self-check CLEAN; dry run exit 2 from both cwds under
  -I -S -B, 372 bytes ending 0x7d with rstrip() == raw and stderr 0.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. The demonstration
  is the dry run, which opens no run input, and the hashing of sealed evidence bytes,
  which starts no procedure. No check and no fixture has been run and NO OUTCOME IS
  CLAIMED. I do NOT claim run 023 now succeeds: VERIFIER_INPUT_ROOT is where the run
  REACHED, not necessarily the only thing in front of it, and what the next attempt
  reaches is what the run tests. Nor do I adjudicate the parent's report of the stop --
  I repaired the attestation that caused it. THE STOP IS THE HANDSHAKE WORKING: a stale
  attestation was caught rather than silently accepted, which is what an independently
  computed root is for.)
VERB_AUDIT_SELF = CLEAN (+1 observation NAMED AND NOT REPAIRED HERE: the comment at
  verifier/contracts.py:125-132 states that BOTH run-scoped roots "cannot exist when
  the launch manifest is authored" and that the instance carries the sentinel for both.
  Since 657 that is true only of ledger_sha256 -- the evidence set is sealed before
  launch, so its root CAN be computed in advance, and this relay binds it for the second
  time. The comment is stale; the code is not, because require_roots_bound() tests the
  sentinel VALUE rather than the field name. A delta with two causes cannot be checked,
  which is the same reason the verdict schema stayed outside the root at 674 and was
  closed as its own relay at 676.)
```

The useful part of this relay is not the new digest; it is the old one. Recomputing
the value I had already attested, and getting it back, is what makes the new value
a statement about the evidence rather than about me.
