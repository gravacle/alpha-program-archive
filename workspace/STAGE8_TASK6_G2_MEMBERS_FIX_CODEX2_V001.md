# STAGE8 TASK 6 / TRANCHE — G2 stale-members-copy disposition

**Artifact:** `STAGE8_TASK6_G2_MEMBERS_FIX_CODEX2_V001.md`  
**Lane:** Codex 2 / Builder A  
**Date:** 2026-08-08  
**Register context:** Q-613  
**Custody:** Builder A package only; Builder B's sealed V009 instance is read-only  
**Execution scope:** pin generation, package materialization, schema/static validation, and parent dry-run against Builder B's real sealed instance; evaluator chain not invoked

## 1. Preflight and sealed inputs

The requested output filename was absent in the cleanroom and archive
workspace. These inputs were verified before use:

| Input | Verified SHA-256 | Binding |
|---|---|---|
| `STAGE8_TASK6_V009_CONFIRMATION_DARIO_V001.md` | `79649121efe34247c4dd09eb5a1ee2e1ec48503ca635952f27f5eca8836d78ad` | B's V009 confirmation, P0 result, and G2 finding |
| `evaluator_build_B/rd22.verifier-manifest.v001.json` | `5bfe149f2395c406ce0d39b88e3d9b03aa2a3121a474da22ba5604f0a35f6f79` | real sealed twelve-field V009 instance |
| manifest sidecar | content binding verified | sidecar digest states the exact manifest digest above |
| `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V009.md` | `900a240df2bfdee5867eb589ae88c7f282810a8c7718999ad5cdf2bfb3f80698` | unchanged governing specification |
| Builder A pre-delta inventory | `37d7202bb407add3a56b5f5b2e64413012c079e1c494b61b9b74819dc94818dc` | bounded package-delta base |

B's sealed report confirms `P0.success = TRUE` on the real six-conjunct input
set. That fact is recorded here but was not recomputed as an evaluator outcome
and does not authorize or imply any criterion result.

No register, plan, tracker, git, chain, member-binding, fixed-point, end-test,
physical-quantity, alpha, `kappa_record`, or measured-constant action occurred.

## 2. Chosen fix — remove the copy

I chose option **(b)** because it is the smaller lawful surface. The parent
already validates `verifier_root_members` inside Builder B's canonical,
sidecar-pinned manifest and verifies each row against the package bytes before
deriving `verifier_root_sha256`. A second Builder A snapshot adds no authority
or integrity and necessarily acquires a time-of-copy race.

The following redundant surfaces were removed:

```text
inputs/verifier_root_members.generated.json
schemas/verifier-root-members.schema.json
```

The materializer no longer creates or inventories the copy. The parent no
longer requires it as a package file. The standalone schema was removed with
the object it typed; no replacement schema was added. The existing closed
`schemas/verifier-manifest.schema.json` continues to type the authoritative
nested key exactly as:

```text
verifier_root_members
```

The parent continues to require that field, require sorted unique
package-relative paths, verify `{byte_length,relative_path,sha256}` for every
row, and compute the root from the declared row digests. Thus a future Builder
B membership change requires only a newly sealed Builder B instance; Builder A
has no separate value that can go stale.

## 3. Real sealed-instance validation

The dry-run did not synthesize or copy a verifier manifest. It passed B's real
sealed `evaluator_build_B/rd22.verifier-manifest.v001.json` directly to
`parent.validate_verifier_manifest`, using Builder A's current real subject and
evidence manifest roots. The parent verified:

```text
MANIFEST_SHA256 = 5bfe149f2395c406ce0d39b88e3d9b03aa2a3121a474da22ba5604f0a35f6f79
SCHEMA_FIELDS = 12
ARGV_FIELDS = 22
INPUT_ROOTS = 7
VERIFIER_ROOT_MEMBERS = 13
COMPUTED_ROOT = 10622f170b979ae83ad8b496bafac41087b976512025669f5b38a97c028af488
DECLARED_ROOT = 10622f170b979ae83ad8b496bafac41087b976512025669f5b38a97c028af488
RESULT = PASS
```

It then bound a synthetic run-scoped ledger, executed the post-production
carrier validator, and constructed the isolated direct-script command. No
verifier or producer process was launched.

## 4. Stale-value and name closure

The superseded copy carried root
`43cff85d402a93753427f63607075d5c5ebff7d73e7b0ebe1090b2655c7f64db`.
Seven of its thirteen member rows were stale after B's 697 delta:

| Member | Superseded digest | Current sealed digest |
|---|---|---|
| `contracts/verifier_verdict.schema.json` | `8ff8b2cf9fe04d409965997d0a0c7ebe870a574ceeb84ab9547d554a5b672631` | `e2ce857eb5f3df9b07b129d104dc6e01e1c8e744b859942d6f48435e554575f0` |
| `verifier/child_manifest.py` | `755c7529cc6a10d4e9fa06dccf5e0648d0cc80100983da21a319c12d8dd19e6e` | `fe406b521d11ff5922c008a882a23d041627d1d0294f41ebb338feace7b181b0` |
| `verifier/contracts.py` | `29d904a1b722d0955524ce029319af07610d41436d88987b6055043f17b217f9` | `d2b9c6ce028a6612cfa6d9147eac434e7213ee5b1acf62e6392383c3dfac07ce` |
| `verifier/preconditions.py` | `e71527e98c3b2332bf7e13843688d173acac79a8be4190c5cc9ea6b88b2260d9` | `03c5eaad3c6d6c99d76f1f41c79c68a9efb2175072ceb4b95def11fd43ebafd4` |
| `verifier/replay.py` | `b96cdca78830658cd523d23ea51ec50b2448aae8f722f916d78be2c71f8de2da` | `a32bb0c43e4790e33a950a308fa7f8b31bf89fd8d4637f55b3b9f7e1a0234582` |
| `verifier/spec_census.py` | `2fae7b80f5b595502915289ac2cf1f75e31d40e78631d8def7eb522db42fde40` | `d0a472680ff500b4a997d9542fcd3861791d774c6832418961d2b8d342228189` |
| `verifier/verify.py` | `553ae0f0c6e934b5703d48180c374e184082a28f66064bc83ed38b3ffb7687a5` | `f1c1e31b826f19aff97b2b97157081ddb70a9c6802b36ed8999d576d2d7795b4` |

The final package was searched by full value for that root and all seven stale
digests, and by name for both removed files. Results:

```text
STALE_VALUE_HITS = 0
STALE_NAME_HITS = 0
PIN_CLOSURE_HITS = 0
```

The generated pin manifest now carries B's current instance, current V009
confirmation report, and current verdict schema. The prior V008 manifest/report
pin kinds and the historical root-membership-source pin were removed.

## 5. Bounded package delta

Exactly eleven package paths changed or were removed:

| Path | Before SHA-256 | After SHA-256 | Disposition |
|---|---|---|---|
| `README.md` | `f425dc89747f6bff74126868e75018735423638c5a9647bdd8d40635bc8f570a` | `b0e32d772a98abf52f65592d1fbe784ea3a06d280fccb498f6189d3bfc439327` | sole-carrier documentation |
| `inputs/verifier_root_members.generated.json` | `847055818c3e18414a43d092288abcfefa7def3d676ebea275499e1f5eb24846` | deleted | redundant stale copy removed |
| `manifests/normal.json` | `cf462941f725466139fc7314c03ff3642f2bb5a165e5fb25bab271a0a2920911` | `2b979384fa3fb2fc8b0add0e2e063831b81bf3786e69ca9c45cb1d371bd2f1d5` | regenerated package and B-schema pins |
| `manifests/optimized.json` | `b332023baeeb1ff79d60867bcbb2845e949c7484a519d1316b1a5cd862f1ab79` | `c06cce955351d6138171cd8c9a482e2debaeea931ca58b512d0e18352dc10cb9` | regenerated package and B-schema pins |
| `manifests/package_inventory.json` | `37d7202bb407add3a56b5f5b2e64413012c079e1c494b61b9b74819dc94818dc` | `fa394d58bc1799f2d0b6c4ec0b7a89d05f0ba22c2d79cffc030d41736b2744d4` | complete 41-file inventory |
| `manifests/pins.json` | `380c954a3d2f7557c6a9c5a58f4a10903378a29808c0aadc6a2a2376036ba2e2` | `92b80de0a57615fd2d9f2e9a337d62e314ca86608d9dc86a4e3d16b5ecdbce9b` | 24 current generated pins |
| `parent.py` | `8710cc229e224820351612d647da8973951752793cd6bdba7e78968508cb1746` | `a09f333a133deb28f57f4dda5b78fd54f708c553b0c5ec1df98d3682c79100cc` | removed redundant package-file requirement |
| `schemas/verifier-root-members.schema.json` | `e51ef055d2a6875b822504513882b40b826a5413e2060a856b6babcb27af485b` | deleted | copy-only standalone schema removed |
| `tools/generate_pins.py` | `0edd8098059671d208bc7cf873ad5e69379cd86d4d8e1e25610a97e02392fd5d` | `50f5afd8c865a4a904d3e0845b56a14aa35173c378a1cc13d89a652414a2a898` | current B instance/report pins |
| `tools/materialize.py` | `059c72d500d86fd6b6b14551a69d9b05bde9fc6689c3eccb10cfe836ade47489` | `3849138ccf51f18e647958820da13caf4336261ef762c4230d1dab59373b68b8` | copy generation and inventory removed |
| `tools/self_check.py` | `b19ae8ccdf4557de4ca77c6ef87d8757b96f2baeb90defc12a5bc25d1fafdb3c` | `246e0d5426f0f275c6a209c65fad9f61d5866c2cfb2f0288e45900513be5d436` | real-instance dry-run and zero-hit guard |

The governing specification, all 66 descriptor rows, `checks/check_map.json`,
fixtures, producer code, evidence bytes, criteria, and opcodes are unchanged.
No schema was added.

## 6. Static transcript and scope

```text
generate_pins.py
  pins=24
  sha256=92b80de0a57615fd2d9f2e9a337d62e314ca86608d9dc86a4e3d16b5ecdbce9b

materialize.py
  checks=66 structural=56 gated=10 fixtures=6
  normal=2b979384fa3fb2fc8b0add0e2e063831b81bf3786e69ca9c45cb1d371bd2f1d5
  optimized=c06cce955351d6138171cd8c9a482e2debaeea931ca58b512d0e18352dc10cb9

self_check.py
  SELF_CHECK_OK syntax=6 canonical_json=all local_schemas=10
  g2_pin_closure=value:0,name:0,total:0:PASS
  verifier_manifest=5bfe149f2395c406ce0d39b88e3d9b03aa2a3121a474da22ba5604f0a35f6f79
  verifier_root_members=13
  verifier_root=10622f170b979ae83ad8b496bafac41087b976512025669f5b38a97c028af488
  root_membership=sealed-B-instance-only
  b_spec_repin=ALIGNED
  parent_manifest_dry_run=PASS_REAL_SEALED_B_INSTANCE
  chain_invoked=false
```

Battery: F_PLDEC CLEAN; anti-tuning CLEAN; M-2 unchanged; authority not
claimed; 10 gated rows remain non-starting; package outputs remain empty.

The register's correction of the earlier J2 explanation is acknowledged
without a code or specification change: default `SequenceMatcher(autojunk=True)`
caused the `160/26` result; replace blocks decrease from 14 to 10 while
lines-per-side rise. The register is the correction of record.

```text
PACKAGE_FILES = 41
PACKAGE_INVENTORY_SHA256 = fa394d58bc1799f2d0b6c4ec0b7a89d05f0ba22c2d79cffc030d41736b2744d4
CHAIN_OUTPUT_FILES = 0
```

FIX = (b) copy removed
SCHEMA_KEY = verifier_root_members
PIN_CLOSURE = 0 hits, all resolved
DRY_RUN = executed against B's sealed instance
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN / +items: none
