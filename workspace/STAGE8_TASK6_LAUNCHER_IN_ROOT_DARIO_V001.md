# STAGE 8 / TASK 6 / BUILD — THE LAUNCHER BROUGHT INSIDE THE PINNED ROOT — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 667 / Task 6 build — close the unpinned-entry-script hole
Authority: RD-22 + the addendum sealed at Q-588. **THIS ARTIFACT INVOKES NOTHING.**

```text
ROOT = covers launcher (11 members; b32b700f… -> 8732646c…)
DRY_RUN = passes under -I -S -B
INSTANCE = canonical, sidecar-pinned
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 duplication hazard removed, +1 improvement proposed not taken)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**Builder A's stop was correct and I adopt it without argument.** I shipped a
launcher that dispatches the entire verifier and left it outside the root that
pins the verifier's bytes. An entry script that can change behaviour and is not
covered by the integrity root is exactly the hole a content-addressed custody
graph exists to prevent — and A caught it before the run rather than after.

## 0. Preflight

| Check | Result |
|---|---|
| Output artifact collision | none — clear to write |
| A's cited old root `b32b700f…` | **reproduced exactly** before changing anything — confirms A read my manifest correctly |
| `run_verifier.py` digest `2c8caad0…` | the file A named as uncovered |
| Builder A's **code** | never listed, opened, or searched |

---

## 1. V1 — THE CHOICE, AND WHY

[YOURS] A offered two remedies. **I take root inclusion**, for the reason A
implied: *one root is one thing to check.* A separately pinned entry digest adds
a second value that can drift out of step with the first — two facts to keep
true, and a failure mode where each is individually correct and the pair is not.
Root inclusion has no such state: every load-bearing byte is inside one digest,
and a file that is not inside it is not load-bearing.

### 1.1 The exact member list — 11, package-relative, sorted

```text
run_verifier.py                 <- NEWLY COVERED (was outside the root)
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

### 1.2 The computation — scheme unchanged, membership extended

```text
verifier_root_sha256 := SHA256( concat( sha256_hex(member_bytes)
                                        for member in sorted(members) ) )
```

The scheme is **exactly the one already in use**; only the member set changed.
I deliberately did not alter the algorithm in the same relay as the membership,
so the delta has one cause and A can attribute any difference to the added file
alone.

```text
OLD root   b32b700f70922a9c7a4678ccb172e8ee5484811cae6948a732c4de69569937c9   (10 members)
NEW root   8732646c2bfec9b0e98dbb2ae4ab4733d0348b20bc09a6792805f97104a36275   (11 members)
```

### 1.3 The duplication hazard I found while doing it — removed

[PROVABLE] The root was being computed in **two places**: `verify._self_digest()`
(which stamps the verdict) and the manifest generator. Two implementations of one
root is a latent disagreement — the manifest could pin one value while the
verdict reported another, and both would look correct in isolation.

Both now call a single definition, `child_manifest.package_root_digest()`, and I
verified they agree:

```text
package_root_digest(base) = 8732646c2bfec9b0e98dbb2ae4ab4733d0348b20bc09a6792805f97104a36275
_self_digest()            = 8732646c2bfec9b0e98dbb2ae4ab4733d0348b20bc09a6792805f97104a36275
AGREE = True
```

The member list and computation are stated **in the code**, not only here, so the
next reader finds the definition where the value is produced.

### 1.4 An improvement I judged out of scope, proposed not taken

[YOURS] The concatenated-hex scheme binds each member's **content** but not its
**name or length**: two members with swapped filenames would produce the same
root. The spec's own `content_root` (`:288-292`) binds path, byte length and
digest, and is already proven interoperable — run 008 converged on it between two
builders.

**I did not switch.** Changing the root's *definition* in the same relay that
changes its *membership* would make the old→new delta unattributable, and A may
be verifying my root under the current scheme. I record it as a proposal for a
contract revision, to be taken deliberately or not at all.

---

## 2. V2 — THE DRY RUN STILL PASSES

```text
$ python3 -I -S -B run_verifier.py --dry-run-launch
{"chain_invoked":false,"dont_write_bytecode":true,"entry_point":"run_verifier.py",
 "governing_spec_sha256":"f8d1a7dc…","isolated":true,"no_site":true,
 "package_root_resolved":true,"run_inputs_consumed":false,
 "schema":"rd22.verifier-launch-dryrun.v001","verdict":"NO_VERDICT_DRY_RUN",
 "verifier_module":"verifier.verify"}
exit=2

$ cd /tmp && python3 -I -S -B "<abs>/evaluator_build_B/run_verifier.py" --dry-run-launch
exit=2        # foreign cwd, absolute path — as the parent invokes
```

`isolated:true`, `no_site:true` and `dont_write_bytecode:true` are read from
`sys.flags` at run time, so the flags are proved **in effect**. No run input is
opened; the chain is not invoked.

---

## 3. V3 — DELTA AND PIN CHECK

```text
CHANGED  verifier/child_manifest.py            single-source root: ROOT_MEMBERS,
                                               package_root_members, package_root_digest
CHANGED  verifier/verify.py                    _self_digest delegates to that definition
CHANGED  rd22.verifier-manifest.v001.json      7a5ee8ce… -> 91d264dcbc2da49ccb4e28e19eb0e775dd654eb1d16b60bfef5a132f0f3a4d7d
CHANGED  rd22.verifier-manifest.v001.json.seal.sha256   regenerated, verified OK
UNCHANGED run_verifier.py                      the covered file itself did not move
```

Package: **18 files**, unchanged in count.

| Claim | Verified before sealing |
|---|---|
| A's cited old root reproduced | `b32b700f…` computed before any edit |
| 11 members, sorted, package-relative | list printed from the shipped code |
| new root | `8732646c…`, recomputed from the instance and compared |
| manifest and verdict agree on the root | `package_root_digest()` == `_self_digest()` |
| launcher genuinely covered | `run_verifier.py` is member 1 of 11 |
| dry run under `-I -S -B` | executed twice, exit 2, flags echoed |
| instance canonical | round-trip identical; sorted; single line; no trailing newline; 11 fields |
| sidecar verifies and equals `manifest_sha256()` | `91d264dc…` |
| ledger guard intact | refuses, naming `ledger_sha256` alone |
| evidence root retained | `e7820ca5…` |
| zero `assert`; self-check CLEAN | executed |

### 3.1 `F_PLDEC` and coverage

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. **The chain was not invoked**; the dry run opens no run
input. `alpha_computed = false`; `proof_authorized = false`;
`kappa_record_computed = false`; no member bound; no fixed point; no end test; no
numeric evaluation; no comparison to any measured constant.

**Coverage, stated exactly:** I changed the root's membership, removed a
duplicate implementation of it, and reissued the instance and sidecar. I claim
**no check or fixture outcome**, and I do **not** claim run 013 will pass — I have
closed the custody hole A named, which is a precondition, not a verdict.

---

## 4. SELF VERB AUDIT

| My verb | Check |
|---|---|
| A's stop adopted | Without argument. The hole was real and mine: I pinned ten files and shipped an eleventh that dispatches all ten. |
| `ROOT = covers launcher` | Member list printed **from the shipped code**, not transcribed; old and new both displayed; A's cited old value reproduced first as a control. |
| Scheme unchanged | Deliberate: membership and algorithm are not changed in one relay, so the delta has a single attributable cause. |
| **Duplication hazard removed** | Found while implementing, not asked for: the root had two implementations that could disagree while each looked right. Now one definition, and the agreement is demonstrated rather than assumed. |
| **Improvement proposed, not taken** | The concatenated-hex scheme does not bind names or lengths; `content_root` does. Switching mid-delta would have made the change unattributable, so I propose it and leave it. |
| `DRY_RUN` | Re-executed after the pinning change, from two cwds, with `sys.flags` echoed. |
| `CHAIN_INVOKED = false` | Literally true. |

---

```text
ROOT = covers launcher (+11 members, b32b700f70922a9c7a4678ccb172e8ee5484811cae
  6948a732c4de69569937c9 -> 8732646c2bfec9b0e98dbb2ae4ab4733d0348b20bc09a679280
  5f97104a36275. Member list, package-relative and sorted: run_verifier.py --
  NEWLY COVERED -- plus the ten verifier/*.py modules. Computation is the SCHEME
  ALREADY IN USE, membership extended only: SHA256(concat(sha256_hex(member_bytes)
  for member in sorted(members))). I deliberately did NOT change the algorithm in
  the same relay as the membership, so the delta has one attributable cause and A
  can verify the difference is the added file alone. Root inclusion was chosen over
  a separate entry digest because one root is one thing to check and cannot drift
  out of step with a companion value.
  DUPLICATION HAZARD REMOVED en route: the root was computed in TWO places --
  verify._self_digest(), which stamps the verdict, and the manifest generator --
  so the manifest could pin one value while the verdict reported another and both
  look correct alone. Both now call child_manifest.package_root_digest(), and the
  agreement is DEMONSTRATED: package_root_digest() == _self_digest() == 8732646c….
  PROPOSED NOT TAKEN: the concatenated-hex scheme binds member CONTENT but not
  NAME or LENGTH, where the spec's own content_root at :288-292 binds all three
  and is already proven interoperable by run 008's convergence. Switching mid-delta
  would make old->new unattributable, so it is recorded for a deliberate contract
  revision.)
DRY_RUN = passes under -I -S -B (re-executed after the pinning change, from the
  package directory and from a foreign cwd by absolute path as the parent invokes;
  both exit 2 with one canonical JSON line, run_inputs_consumed:false and
  chain_invoked:false, and sys.flags echoed as isolated:true / no_site:true /
  dont_write_bytecode:true so the flags are proved IN EFFECT.)
INSTANCE = canonical, sidecar-pinned (7a5ee8ce… -> 91d264dcbc2da49ccb4e28e19eb0e7
  75dd654eb1d16b60bfef5a132f0f3a4d7d, equal to manifest_sha256(), sidecar
  regenerated and verified OK; sorted keys, single line, no trailing newline,
  11 fields. entry_point and argv unchanged at run_verifier.py; output_path,
  receipt_path and all five input_roots unchanged; the ledger guard still refuses
  naming ledger_sha256 alone; evidence root e7820ca5… retained. DELTA: two modules
  and the instance+sidecar; run_verifier.py itself did not move; 18 files;
  self-check CLEAN; zero asserts.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. No check and
  no fixture has been run; no outcome is claimed; and I do NOT claim run 013 will
  pass -- closing the custody hole A named is a precondition, not a verdict.)
VERB_AUDIT_SELF = CLEAN (+1 duplication hazard found while implementing and
  removed, with the agreement demonstrated rather than assumed; +1 improvement to
  the root's algorithm proposed and expressly NOT taken, because changing a
  definition and its membership in one relay makes the delta unattributable.)
```

A stopped on a hole I made: I pinned ten files and shipped an eleventh that
dispatches all ten. Fixing it turned up a second one nobody had asked about — the
root had two implementations that could disagree while each looked right on its
own. Both are closed, and the third thing I found is written down and left alone,
because the discipline that makes a delta checkable is not doing two things at
once.
