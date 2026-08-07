# STAGE 8 / TASK 6 / BUILD — THE VERDICT SCHEMA BROUGHT INTO THE ROOT — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 676 / Task 6 build — commission of my own 674 observation
Authority: RD-22. **THIS ARTIFACT INVOKES NOTHING.**

```text
ROOT = covers schema (12 members; eb246168… -> dba5377d…)
DRY_RUN = passes
INSTANCE = canonical, sidecar-pinned
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 sibling case named and NOT expanded into, §3.1)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**This closes an observation I made and deliberately did not act on.** At 674 I
recorded that `contracts/verifier_verdict.schema.json` was sidecar-pinned but sat
outside `verifier_root_sha256`, and declined to fix it mid-delta because changing
two things at once makes a delta unattributable. Commissioned as its own relay, it
is now one change with one cause.

## 1. THE CHANGE

### 1.1 Why the schema is load-bearing

[PROVABLE] The verdict schema is the contract **Builder A validates my verdict
against**. A verdict that conforms to a schema A holds a different copy of would
pass locally and fail the handshake — or worse, pass both while meaning different
things. It is not documentation; it participates in the run.

It was already pinned by its own sidecar, so it was never *unpinned*. But it was
not inside the one root, which is exactly the shape A raised about
`run_verifier.py` at 667 and which was resolved there by root inclusion. **Same
question, same answer**: one root over every load-bearing byte, and a file outside
it is not load-bearing.

### 1.2 The member list — 12, package-relative, sorted

```text
contracts/verifier_verdict.schema.json    <- NEWLY COVERED
run_verifier.py                              (covered at 667)
verifier/__init__.py
verifier/canonical_json.py
verifier/child_manifest.py
verifier/comparison.py
verifier/contracts.py
verifier/hashing.py
verifier/replay.py
verifier/runtime_state.py
verifier/spec_census.py
verifier/verify.py
```

### 1.3 The computation — scheme unchanged again

```text
verifier_root_sha256 := SHA256( concat( sha256_hex(member_bytes)
                                        for member in sorted(members) ) )

OLD root   eb246168d86e945df78900903232314293bae382b11ecf1e3d5074caa3e62b92   (11 members)
NEW root   dba5377d5ca1e7eebf2932da10e043e96c33f642cf06c8dd81cf26dff3bd3ac0   (12 members)
```

Membership changed; **the algorithm did not** — the same discipline as 667, so the
old→new delta has a single attributable cause. The scheme hashes bytes, so a JSON
member is covered exactly as a Python member is; nothing about it is Python-specific.

[PROVABLE] The manifest and the verdict still agree on the root, because both
still call one definition:

```text
package_root_digest(base) = dba5377d5ca1e7eebf2932da10e043e96c33f642cf06c8dd81cf26dff3bd3ac0
_self_digest()            = dba5377d5ca1e7eebf2932da10e043e96c33f642cf06c8dd81cf26dff3bd3ac0
AGREE = True
```

## 2. DRY RUN

```text
$ python3 -I -S -B run_verifier.py --dry-run-launch
exit = 2 ; stdout 372 bytes ; last byte 0x7d ('}') ; stderr 0 bytes

$ cd /tmp && python3 -I -S -B "<abs>/evaluator_build_B/run_verifier.py" --dry-run-launch
exit = 2
```

Both cwds; canon holds (no trailing newline); stderr silent on the success path.

## 3. DELTA AND PIN CHECK

```text
CHANGED  verifier/child_manifest.py                  ROOT_MEMBERS gains the schema
CHANGED  rd22.verifier-manifest.v001.json            83b68846… -> ddd340a4652b70a3cab2a1ab5c888ecda4fc0def5cda03e39672a5d50818e983
CHANGED  rd22.verifier-manifest.v001.json.seal.sha256    regenerated, verified OK
UNCHANGED  the schema itself, run_verifier.py, and every other verifier/*.py
```

**One module, one cause.** The schema file is not edited by being covered — only
the definition of what the root spans changed. Package: 19 files.

| Claim | Verified before sealing |
|---|---|
| old root reproduced first | `eb246168…` computed before any edit |
| 12 members, sorted, schema included | list printed from the shipped code; membership test on the schema path |
| new root | `dba5377d…`, recomputed from the instance and compared |
| manifest and verdict agree | `package_root_digest()` == `_self_digest()` |
| instance canonical | round-trip identical; sorted; single line; no trailing newline; 11 fields |
| manifest sidecar verifies, equals `manifest_sha256()` | `ddd340a4…` |
| schema sidecar still verifies | `shasum -c` OK — the schema is now pinned twice, consistently |
| ledger guard intact | refuses, naming `ledger_sha256` alone |
| evidence root, output paths, T-labels | unchanged |
| dry run both cwds; stdout canon | exit 2; last byte `}`; stderr 0 |
| self-check CLEAN; 19 files; zero `assert` | executed |

### 3.1 The sibling case — named, not expanded into

[YOURS] `contracts/rd22.verifier-manifest.v001.json` — the launch **contract
schema** — is likewise sidecar-pinned and outside the root. I did **not** include
it, and the distinction is real rather than convenient: the verdict schema is
consumed **during the run**, as the thing A validates my output against, whereas
the manifest schema is a shape declaration that both builders conform to and which
neither reads at run time; what A actually reads is the manifest **instance**,
which the root does cover via its own digest field.

That may still be the wrong line, and it is one relay's work to move it. I record
it as an open question rather than settle it inside a commissioned change — the
same reason I did not fix the verdict schema inside 674.

### 3.2 `F_PLDEC` and coverage

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. **The chain was not invoked**; the demonstration is the
dry run, which opens no run input. `alpha_computed = false`;
`proof_authorized = false`; `kappa_record_computed = false`; no member bound; no
fixed point; no end test; no numeric evaluation; no comparison to any measured
constant.

**Coverage, stated exactly:** I changed the root's membership and reissued the
instance. I claim **no check or fixture outcome**, and I do not claim the next run
passes — A is being repaired in parallel to validate against this schema as a
pinned input, and whether the two sides now agree is what the run tests.

## 4. SELF VERB AUDIT

| My verb | Check |
|---|---|
| Observation closed, not re-argued | I raised this at 674 and declined to act; commissioned, I implement it without relitigating whether it was worth doing. |
| `ROOT = covers schema` | Member list printed **from the shipped code**; old value reproduced first as a control; schema membership asserted, not assumed. |
| Scheme unchanged | Third time this discipline has applied: membership and algorithm never move in the same relay. |
| Single-source root preserved | The 667 fix still holds — one definition, and the agreement re-demonstrated rather than presumed to have survived. |
| **Sibling case named, not taken** | The manifest contract schema is in the same position; I give the distinction I am drawing and admit it may be wrong, rather than silently including it or silently omitting it. |
| `CHAIN_INVOKED = false` | Literally true. |

---

```text
ROOT = covers schema (+12 members, eb246168d86e945df78900903232314293bae382b11ecf
  1e3d5074caa3e62b92 -> dba5377d5ca1e7eebf2932da10e043e96c33f642cf06c8dd81cf26dff
  3bd3ac0. Newly covered: contracts/verifier_verdict.schema.json, joining
  run_verifier.py and the ten verifier/*.py modules. It is load-bearing because it
  is the contract Builder A validates this verifier's verdict against -- it
  participates in the run rather than describing it -- and it was pinned by its own
  sidecar but outside the one root, exactly the shape A raised about the launcher
  at 667 and resolved there the same way. THE ALGORITHM DID NOT CHANGE, only
  membership, so the delta has a single attributable cause; the scheme hashes
  bytes, so a JSON member is covered exactly as a Python one is. Manifest and
  verdict still agree on the root -- package_root_digest() == _self_digest() ==
  dba5377d… -- because the 667 single-source definition still holds.)
DRY_RUN = passes (exit 2 from the package directory and from a foreign cwd by
  absolute path under -I -S -B; stdout 372 bytes ending on 0x7d with no trailing
  newline; stderr 0 bytes on the success path.)
INSTANCE = canonical, sidecar-pinned (83b68846… -> ddd340a4652b70a3cab2a1ab5c888ec
  da4fc0def5cda03e39672a5d50818e983, equal to manifest_sha256(), sidecar
  regenerated and verified OK; sorted keys, single line, no trailing newline,
  11 fields. DELTA: ONE MODULE, ONE CAUSE -- verifier/child_manifest.py gains the
  schema in ROOT_MEMBERS; the schema file itself is untouched, being covered is not
  being edited. Ledger guard, evidence root, output paths and the Q-601 T-label
  contexts all unchanged; the schema's own sidecar still verifies, so it is now
  pinned twice and consistently; 19 files; self-check CLEAN; zero asserts.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. No check and
  no fixture has been run; no outcome is claimed; and I do not claim the next run
  passes -- A is being repaired in parallel to validate against this schema as a
  pinned input, and whether the two sides agree is what the run tests.)
VERB_AUDIT_SELF = CLEAN (+1 sibling case NAMED AND NOT EXPANDED INTO:
  contracts/rd22.verifier-manifest.v001.json is likewise sidecar-pinned and outside
  the root. I give the distinction I am drawing -- the verdict schema is consumed
  DURING the run as the thing A validates my output against, while the manifest
  schema is a shape declaration neither builder reads at run time, what A reads
  being the instance, which the root covers via its digest field -- and I admit the
  line may be wrong. Recording it beats settling it inside a commissioned change,
  which is the same reason I did not fix the verdict schema inside 674.)
```

The observation I filed two relays ago is closed, and the discipline that made it
worth filing is the one that kept it out of 674: a delta with two causes cannot be
checked, and a note costs one line. What the closure buys is narrow and real —
Builder A can now pin my verdict schema as an input and know its digest is inside
the same root that covers the code which emits against it.
