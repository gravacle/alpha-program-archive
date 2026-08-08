# STAGE8 TASK 6 / TRANCHE — Q-612 four-fix whole delta

**Artifact:** `STAGE8_TASK6_Q612_FIXES_CODEX2_V001.md`  
**Lane:** Codex 2 / Builder A  
**Date:** 2026-08-08  
**Register context:** Q-612  
**Custody:** specification V009 and Builder A package only; Builder B confirms the V009 boundary and re-pins independently  
**Execution scope:** generation, byte diffs, schema validation, and non-authoritative parent dry-run only; evaluator chain not invoked

## 1. Preflight and pinned inputs

The requested report and V009 filenames were absent in both the cleanroom and
archive workspace before creation. The immutable inputs were verified before
reading or use:

| Input | Verified SHA-256 | Use |
|---|---|---|
| `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V008.md` | `3b24fc39f47d4502b01c1f06faf9f02b7828f5ba0cf4b6a882a3b331ae9c0986` | immutable V009 base; all 66 descriptor rows |
| `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V007.md` | `d38d31719b64839744a98da5ee005fb50119f9a26b2b98b0e1a1de445b5d4973` | V008 carriage-count recomputation |
| `STAGE8_TASK6_SPEC_V005_INTEGRATION_ADDENDUM_DARIO_V001.md` | `d17c5e79986bea431dec0b572019096f9c059bcc43876fda9134abc96ce0f260` | event/fixture/verifier integration boundary and missing subject bytes |
| `STAGE8_TASK6_SCHEMA_IN_ROOT_DARIO_V001.md` | `de9139768c68371310e48245568472273fc19da96c48004ef7819ee6b0dbab79` | sealed 12-member root base list |
| `STAGE8_TASK6_V008_INTEGRATION_DARIO_V001.md` | `4b93a9acda84691ee4d32fd9f4ecc34dca49bdef882c898ebbe0f2f5f21c6a80` | sealed addition of `verifier/preconditions.py`; 13-member disclosure |
| `evaluator_build_B/rd22.verifier-manifest.v001.json` | `35b0ec6626c6648940304de78f313879de2f1599c4f6afbd6cf10fa5eba7f52e` | independently sealed V008 instance/root check |
| Builder A pre-delta package inventory | `1e89b685767239d52d62fdfa5adce632f794e822a6dd57b77cd17994f59662f5` | package-delta base |

No register, plan, tracker, git, commit, push, evaluator-chain, fixed-point,
end-test, member-binding, or physical-quantity action was performed.

## 2. J1 — generated fixture spans

The V008 generated fixture manifest was rechecked against the V008 source
bytes. Its spans and hashes are correct; the three V008 prose-table end offsets
were one byte low because they excluded each row's terminating newline.

| Fixture | V008 generated span | V008 generated SHA-256 | Prior prose end | Correct end |
|---|---:|---|---:|---:|
| `FX-A35-03-C-FAMILY` | `[133496,133685)` | `9f951cb11fbc7a199383b6914404e0fe1dc495a0d1c114190b125203f1971e07` | `133684` | `133685` |
| `FX-A35-04-TAU-FAMILY` | `[133685,133873)` | `a91920d88d567f0face3729e7ed8ae77716a35e6c94d42ffdb0be2819833223f` | `133872` | `133873` |
| `FX-A35-05-PRIMITIVE-THOMSON-CONFLATION` | `[133873,134126)` | `06ce18cbf270e5b497b7850a1ed497017df95cb8beab59086adb5896927b9a4e` | `134125` | `134126` |

V009's table was not hand-transcribed from those offsets. The materializer
located each final V009 row in the final bytes, included its newline, generated
the manifest and table, then the self-check recomputed all three:

```text
FX-A35-03-C-FAMILY                 [136130,136319)
FX-A35-04-TAU-FAMILY               [136319,136507)
FX-A35-05-PRIMITIVE-THOMSON-CONFLATION [136507,136760)
J1_GENERATED_FIXTURE_SPANS = 3/3 PASS
```

## 3. J2 — carriage recomputed from bytes

The declared convention is `/usr/bin/diff -U 3`: exclude only `---` and `+++`
file headers; count every other added/deleted line, including blank content
lines. Re-running that exact command over sealed V007 and V008 gives:

```text
V007 -> V008
HUNKS = 6
INSERTIONS = 155
DELETIONS = 21
```

The prior `160/26` figures came from Python `difflib.SequenceMatcher` using a
different alignment. It emitted five additional canceling replacement pairs:
five extra additions and the corresponding five extra deletions. Thus both
reported quantities were exactly +5 while the net line delta happened to
remain unchanged. V009 corrects the historical certificate to `155/21` and
states this cause.

The final V008-to-V009 diff independently recomputes as:

```text
HUNKS = 9
INSERTIONS = 120
DELETIONS = 23
UNASSIGNED_HUNKS = 0
MULTIPLY_ASSIGNED_HUNKS = 0
DESCRIPTOR_ROWS_CHANGED = 0
```

## 4. J3 — smallest lawful subject carrier

J3 required a specification boundary because the integration addendum was a
subject member but was not supplied as replayable bytes. V009 uses the
smallest already-authorized carrier: the existing content-addressed evidence
directory and evidence manifest. It does not add an argv position or an
`input_roots` key; the closed inventories remain 22 and 7.

V009 adds a closed five-field `rd22.subject-evidence-resolution.v001` record:

```text
{evidence_payload_path,evidence_payload_sha256,subject_byte_length,
 subject_relative_path,subject_sha256}
```

For each of the six `subject_manifest.files` rows, the verifier must find
exactly one evidence payload with the same digest and byte length and must
rehash the payload. Zero or multiple matches produces
`PRECONDITION_NOT_REPLAYABLE` naming the missing/ambiguous subject; it is not a
criterion FAIL. The addendum's sealed bytes now exist at
`inputs/evidence/d17c5e79...--STAGE8_TASK6_SPEC_V005_INTEGRATION_ADDENDUM_DARIO_V001.md`,
are inventoried by the evidence manifest, and resolved by the dry-run check.

```text
SUBJECT_RESOLUTION = 6/6
INTEGRATION_ADDENDUM_SUPPLIED = PASS
ARGV = 22 (unchanged)
INPUT_ROOTS = 7 (unchanged)
```

## 5. J4 — generated 13-member instance carrier

The parent-private 12-member tuple was deleted. V009 makes root membership a
closed manifest-instance field, `verifier_root_members`, whose rows are exact
`{byte_length,relative_path,sha256}` objects sorted by unique package-relative
path. The parent verifies every declared byte object and computes:

```text
verifier_root_sha256 = SHA256(concat(row.sha256 for rows sorted by relative_path))
```

The rows below were generated—not typed—from the sealed 12-member source, the
sealed V008 integration disclosure, and the current sealed Builder B package
bytes:

| # | Relative path | Bytes | SHA-256 |
|---:|---|---:|---|
| 1 | `contracts/verifier_verdict.schema.json` | `5154` | `8ff8b2cf9fe04d409965997d0a0c7ebe870a574ceeb84ab9547d554a5b672631` |
| 2 | `run_verifier.py` | `3793` | `c3d8fcd3bb0826d794a1ebaabca6475484b9d4de6e087c490c35acb160afcf9f` |
| 3 | `verifier/__init__.py` | `524` | `896bfc3837e7e68fbaab68d922df49f9d05ea69e0489d6a862b696e96d5c3e40` |
| 4 | `verifier/canonical_json.py` | `2596` | `b1424025b1f1f14fb31c5cdbfd42802229ef8c611677135b9f919e00283147b7` |
| 5 | `verifier/child_manifest.py` | `5571` | `755c7529cc6a10d4e9fa06dccf5e0648d0cc80100983da21a319c12d8dd19e6e` |
| 6 | `verifier/comparison.py` | `4786` | `dbce53e5f0a30c08f4d3a61d6201b97aeaf037e944f4ca27bdc54131cf2c7025` |
| 7 | `verifier/contracts.py` | `17610` | `29d904a1b722d0955524ce029319af07610d41436d88987b6055043f17b217f9` |
| 8 | `verifier/hashing.py` | `3364` | `8c69f599d8b5cc9a2a239a983143226347af29c4914651a3e7f2f205af1308e3` |
| 9 | `verifier/preconditions.py` | `7584` | `e71527e98c3b2332bf7e13843688d173acac79a8be4190c5cc9ea6b88b2260d9` |
| 10 | `verifier/replay.py` | `23620` | `b96cdca78830658cd523d23ea51ec50b2448aae8f722f916d78be2c71f8de2da` |
| 11 | `verifier/runtime_state.py` | `8100` | `3254664f33b017e0f21cea7578e8dab2da1c149d6a92ac8bb8e3b4b0281043f7` |
| 12 | `verifier/spec_census.py` | `7028` | `2fae7b80f5b595502915289ac2cf1f75e31d40e78631d8def7eb522db42fde40` |
| 13 | `verifier/verify.py` | `17867` | `553ae0f0c6e934b5703d48180c374e184082a28f66064bc83ed38b3ffb7687a5` |

```text
GENERATED_VERIFIER_ROOT = 43cff85d402a93753427f63607075d5c5ebff7d73e7b0ebe1090b2655c7f64db
SEALED_B_INSTANCE_ROOT = 43cff85d402a93753427f63607075d5c5ebff7d73e7b0ebe1090b2655c7f64db
ROOT_AGREEMENT = PASS
```

Future membership changes require a new sealed manifest instance, not another
Builder A code edit.

## 6. Specification V009 finite delta

The final V009 bytes are `182779` bytes with SHA-256
`900a240df2bfdee5867eb589ae88c7f282810a8c7718999ad5cdf2bfb3f80698`.
One V009 carries both schema boundary changes forced by J3/J4. The five named
delta items are:

| Item | Assignment |
|---|---|
| V9-01 | J1 generated fixture-table correction and final V009 span regeneration |
| V9-02 | J2 `155/21` correction plus the `difflib` +5/+5 cause |
| V9-03 | J3 closed subject-to-evidence resolution using the existing carrier |
| V9-04 | J4 closed `verifier_root_members` manifest field and parent transcription removal |
| V9-05 | Mechanical header/pin/certificate/terminal carriage |

The 66 descriptor row bodies are byte-identical to V008. No criterion,
predicate, opcode, physical value, authority, or seal status changed.

## 7. Builder A complete package delta

The package diff contains exactly 19 changed or added paths. Canonical
single-line JSON rewrites count as one physical diff hunk but are semantically
decomposed by the generated schemas/inventories and the checks below.

| Path | Before SHA-256 | After SHA-256 | Assignment |
|---|---|---|---|
| `README.md` | `2ef0f51e621cee2176a828400aff3a64b8b231f841a95ed1db4816245bdfbbda` | `f425dc89747f6bff74126868e75018735423638c5a9647bdd8d40635bc8f570a` | J3/J4 boundary documentation |
| `checks/check_map.json` | `65a2674dae7c75753b47324fb230393ef159c785d740de03e2a2aba026efe9c1` | `a5bf6148a37095e857c0ef4b1bb32bfe078874f9b89b7773f27f8c35109c0ba3` | V009 re-pin; descriptor bodies unchanged |
| `fixtures/fixture_manifest.json` | `dd3a70f3d9d00670a266c89f5ac9335ff7be977591b2e2ee815a7554434cad51` | `5548a26304351eaba0160d54d6ac1084d426413429a17fc8c3501f123869dd49` | J1 generated V009 spans and pin |
| `inputs/evidence/900a240d...--STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V009.md` | — | `900a240df2bfdee5867eb589ae88c7f282810a8c7718999ad5cdf2bfb3f80698` | V009 content-addressed carrier |
| `inputs/evidence/d17c5e79...--STAGE8_TASK6_SPEC_V005_INTEGRATION_ADDENDUM_DARIO_V001.md` | — | `d17c5e79986bea431dec0b572019096f9c059bcc43876fda9134abc96ce0f260` | J3 missing subject bytes supplied |
| `inputs/structural_evidence_manifest.json` | `142ce3b8b7eec841e3bdf6f95e0b9c74ad18d84bd377490540c132057787ffba` | `aabed7c27d2ee9baa905af5f6843c63bd6c5d8e8deb388de04c38055962a554a` | J3 payload inventory/root; V009 refs |
| `inputs/subject_lineage_manifest.json` | `34c84ac64d76e15a9d5ff876397b4b36a53f541cb25e8510d88cf1ad819a81cb` | `3ddd0530494a65456e5bc7f371b215d84591c34cd130dcb288c96d670831f8ee` | V009 subject/root regeneration |
| `inputs/verifier_root_members.generated.json` | — | `847055818c3e18414a43d092288abcfefa7def3d676ebea275499e1f5eb24846` | J4 13-member generated carrier |
| `manifests/normal.json` | `c06494a29156ee7cb257944536430d93657d0b3fe6d53e4959896d0b54b4fd35` | `cf462941f725466139fc7314c03ff3642f2bb5a165e5fb25bab271a0a2920911` | whole-state pin/inventory closure |
| `manifests/optimized.json` | `e73a8f5e78f6de526f5ac33f455a8b0c4d73c235d6995f199680f121d69dc238` | `b332023baeeb1ff79d60867bcbb2845e949c7484a519d1316b1a5cd862f1ab79` | whole-state pin/inventory closure |
| `manifests/package_inventory.json` | `1e89b685767239d52d62fdfa5adce632f794e822a6dd57b77cd17994f59662f5` | `37d7202bb407add3a56b5f5b2e64413012c079e1c494b61b9b74819dc94818dc` | complete 43-file inventory |
| `manifests/pins.json` | `9e2ff9fa3764178b816f2ee82dee56f7f777067c8f956c447d9263edcdf68a29` | `380c954a3d2f7557c6a9c5a58f4a10903378a29808c0aadc6a2a2376036ba2e2` | generated 25-pin closure |
| `parent.py` | `4e54dece3536e353a9eb01ddc0993fa16a80f95e40bad09abe4190df27acd53b` | `8710cc229e224820351612d647da8973951752793cd6bdba7e78968508cb1746` | J4 instance receiver; no private census |
| `schemas/subject-resolution.schema.json` | — | `f86d1b9d2a3beb2ea3be02d24a60096303ccae82ed2f4cc6df895e206dcafc6c` | J3 closed interface |
| `schemas/verifier-manifest.schema.json` | `748dc7b414738d8753be5ecfe0af9a722dfffd4273d2eca78617667f4cddeb98` | `de8ec7474b79a77042a22127553f2dc465dd9679fb04b813b922569c662a49a7` | J4 twelve-field closed instance |
| `schemas/verifier-root-members.schema.json` | — | `e51ef055d2a6875b822504513882b40b826a5413e2060a856b6babcb27af485b` | J4 closed member carrier |
| `tools/generate_pins.py` | `ec5e7608ef0668114b9113f9c230a572147a8005b6401cd7f68075712c0e39a2` | `0edd8098059671d208bc7cf873ad5e69379cd86d4d8e1e25610a97e02392fd5d` | V009/B-source pins generated |
| `tools/materialize.py` | `5c4d5efdfc62e66f21ffdc8bc694e45b7093164fd6b6b9a7a3df8a645f25b7d7` | `059c72d500d86fd6b6b14551a69d9b05bde9fc6689c3eccb10cfe836ade47489` | J1/J3/J4 whole-state generator |
| `tools/self_check.py` | `c60a3bde9029cdffbc10950ee56a300cdc26dbc14c79f30d91cdb9ef3db05cff` | `b19ae8ccdf4557de4ca77c6ef87d8757b96f2baeb90defc12a5bc25d1fafdb3c` | dry-run, span/count/root/pin closure guards |

## 8. Pin closure and dry-run transcript

The package sweep searched the superseded V008 name and full digest by both
name and value. Its 26 retained hits are only historical base/evidence/pin
records or the generated verifier itself; no live V008 pin remains. The five
superseded verifier-root prefixes named by the sealed B report have zero
package hits. Current generated pins are the sole live inputs.

```text
python3 evaluator_build_A/tools/generate_pins.py
  pins=25
  pin_manifest_sha256=380c954a3d2f7557c6a9c5a58f4a10903378a29808c0aadc6a2a2376036ba2e2

python3 evaluator_build_A/tools/materialize.py
  checks=66 structural=56 gated=10 fixtures=6
  normal=cf462941f725466139fc7314c03ff3642f2bb5a165e5fb25bab271a0a2920911
  optimized=b332023baeeb1ff79d60867bcbb2845e949c7484a519d1316b1a5cd862f1ab79

PYTHONDONTWRITEBYTECODE=1 python3 evaluator_build_A/tools/self_check.py
  SELF_CHECK_OK
  syntax=6 canonical_json=all local_schemas=11
  pin_closure=value:11,name:15,total:26:PASS
  superseded_roots=5 retained_historical_hits=0
  verifier_root_members=13 root=43cff85d402a93753427f63607075d5c5ebff7d73e7b0ebe1090b2655c7f64db
  subject_resolution=6/6 integration_addendum_supplied=PASS
  descriptor_delta=0:V008_to_V009 descriptor_terminators_excluded=66/66
  j1_fixture_spans=generated:3/3 j2_bsd_diff=6/155/21
  verifier_manifest_fields=12 verifier_input_roots=7 verifier_argv=22:closed
  parent_manifest_dry_run=PASS chain_invoked=false
```

The non-authoritative dry fixture copied all 13 sealed verifier members,
constructed the exact V009-shaped twelve-field manifest, ran the parent
pre-launch validator, bound a synthetic run-scoped ledger, ran post-production
carrier validation, and constructed the isolated direct-script command. It did
not launch the verifier or either producer child.

An attempted `python3 -m py_compile` was denied before writing because that
interpreter targeted a macOS cache outside the sandbox. The successful
bytecode-disabled self-check instead used `ast.parse()` and `compile()` over
all six Python files. Outputs and package pycache roots remain empty.

## 9. Battery and PIN CHECK

| Check | Result |
|---|---|
| F_PLDEC | CLEAN — no physical quantity, member, fixed point, end test, alpha, `kappa_record`, or measured constant was evaluated |
| anti-tuning | CLEAN — 66/66 descriptor rows byte-identical; predicates and opcodes unchanged |
| M-2 | CLEAN — fixed-string, whitespace-normalized, self-reference-scope, and hyphen/space/underscore modes retained; corpus-membership surface unchanged |
| authority/firewall | CLEAN — authorization not claimed; all seal/firewall values remain false |
| no unexecuted new path | CLEAN in Builder A custody — generators, both schema receivers, 13-member verification, subject resolution, pre/post validators, and command construction dry-executed |

```text
V009_SHA256 = 900a240df2bfdee5867eb589ae88c7f282810a8c7718999ad5cdf2bfb3f80698
PACKAGE_INVENTORY_SHA256 = 37d7202bb407add3a56b5f5b2e64413012c079e1c494b61b9b74819dc94818dc
PACKAGE_FILES = 43
NORMAL_MANIFEST_SHA256 = cf462941f725466139fc7314c03ff3642f2bb5a165e5fb25bab271a0a2920911
OPTIMIZED_MANIFEST_SHA256 = b332023baeeb1ff79d60867bcbb2845e949c7484a519d1316b1a5cd862f1ab79
EVIDENCE_MANIFEST_SHA256 = aabed7c27d2ee9baa905af5f6843c63bd6c5d8e8deb388de04c38055962a554a
CHAIN_OUTPUT_FILES = 0
```

The board, prior seals, and authorization state are untouched. Builder B's
V009 boundary confirmation and re-pin remain independent custody steps before
the registrar may invoke run 031.

J1 = corrected from generated values
J2 = recomputed from bytes, cause of +5/+5 stated
J3 = carrier named / V009 slot: existing evidence carrier, no new argv/root position
J4 = 13-member census, generated
SPEC_ISSUED = V009 (rows changed 0)
PIN_CLOSURE = 26 hits, all resolved
DRY_RUN = executed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN / +items: none
