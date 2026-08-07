# STAGE 8 / TASK 6 / BUILD A — AUTHORIZATION SCOPE + T-LABEL FINDING — LANE 2 V001

Lane: Lane 2, Builder A  
Relay: PASTE 670  
Context: run 016 verifier diagnostic `authorization: missing 'scope'`  
Scope: authorization scope forwarding, exact authorization record, T0–T4 temporal audit, cross-builder finding, boundary schema, static self-check, recursive hashes, and disclosed delta  
Authority claimed: none

```text
SPEC_V005_SHA256 = f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b
INTEGRATION_ADDENDUM_SHA256 = d17c5e79986bea431dec0b572019096f9c059bcc43876fda9134abc96ce0f260
RD22_ARTIFACT_SHA256 = ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340
PRIOR_PARENT_SHA256 = 51b286a5e374cf7aee2e5f009d6cfc5486af333027c81392d5779b12870d637b
FINAL_PARENT_SHA256 = 776255fac3f533017e01a57931f8097d5eab033bc3ac5676df0847e1d6fb28bb
CHAIN_INVOKED = false
```

## 1. Preflight and scope disposition

| Check | Result |
|---|---|
| Output collision | This artifact and sidecar were absent in both the cleanroom and archive workspace immediately before creation. |
| Governing pins | V005 and the integration addendum verify at the exact hashes above. |
| RD-22 input | The principal decision verifies at `ff84c4a8…`; its structural-first-run scope and closed gates remain unchanged. |
| Builder A base | The archive mirror is the exact sealed PASTE 669 state: parent `51b286a5…`, normal/optimized manifests `a94ae441…` / `aee8a72f…`, package inventory `5549e558…`. |
| Prior sealed artifact | `STAGE8_TASK6_AUTH_DIGEST_FORWARD_LANE2_V001.md` and sidecar verify at `07ec125e…` / `930a88d7…`. |
| Run 016 record | The retained producer ledger contains `authorization={artifact_sha256,valid}`, its top-level run `scope`, and `trust_snapshots={T0..T4}`. |
| Chain state | No producer, verifier, check executor, fixture, launcher, or full chain was invoked in this relay. |

The corrected contract record is exactly:

```text
authorization = {
  artifact_sha256: <actual digest returned by R0 verification>,
  scope: <the same value as this ledger's top-level scope>
}
```

`verdict_ledger()` already receives the run-scope value that it places at top-level `scope`. It now places that same object at `authorization.scope`; no second scope constructor, summary, projection, or literal exists. Thus, for both producer and terminal ledgers:

```text
ledger.authorization.scope == ledger.scope
```

The previously inferred `valid` member is removed. The terminal-ledger schema closes authorization to the two required fields `artifact_sha256` and `scope`, with digest-form enforcement on the former and object-form enforcement on the latter.

The R0 digest path from PASTE 669 remains intact: `verify_bytes_with_digest()` returns the actual verified authorization digest, and that variable—not the expected-pin literal—is forwarded.

## 2. T-label question — audited finding

### 2.1 State order from sealed V005 and the parent

| Label/event | Sealed meaning | Parent order and carrier |
|---|---|---|
| T0 | Immediately before normal producer | `t0 = trust_snapshot(runtime)` before normal launch. |
| T1 | Immediately after normal producer | `t1 = trust_snapshot(runtime)` after normal returns. |
| T2 | Immediately after optimized producer | `t2 = trust_snapshot(runtime)` after optimized returns. |
| T3 | Immediately before verifier | `t3 = trust_snapshot(runtime)` before producer-ledger construction and verifier launch. |
| Producer ledger | Verifier input | Constructed after T3 and before `run_verifier_process(...)`. |
| T4 | Immediately after verifier | `t4 = trust_snapshot(runtime)` only after `run_verifier_process(...)` returns. |
| Terminal ledger | R10 record | Constructed after actual T4 and carries T0–T4. |

The exact parent maps are:

```text
producer ledger before verifier:
  {T0:t0, T1:t1, T2:t2, T3:t3, T4:t3}

terminal ledger after verifier:
  {T0:t0, T1:t1, T2:t2, T3:t3, T4:t4}
```

Run 016's producer-ledger bytes display five equal digest values. Value equality does not establish temporal identity: source/dataflow inspection proves its `T4` is an alias of T3, not a post-verifier observation.

### 2.2 Verdict on the question

`T4` structurally postdates the verifier launch. It cannot exist when the verifier reads its producer-ledger input. The current producer ledger silently fills the required T4 label with T3.

This is a cross-builder contract item, not a Builder A-local fact that can be repaired by renaming or copying:

- the current ledger schema requires exactly T0–T4;
- every label is required to carry a lowercase SHA-256 digest;
- the verifier contract described in the relay requires the exact same labels;
- no reserved/not-yet-observed T4 value or state is defined; and
- the actual T4 is available only to the post-verifier terminal ledger.

Therefore Builder A cannot lawfully supply `T0..T3` plus a reserved-and-labeled T4 under the current contract. A reserved record would require a registrar-ratified schema/verifier semantic for that state. Omitting T4 would violate the current exact-label/schema contract. Copying T3 into T4, as the current parent does, satisfies value shape but misstates the observation time.

Finding:

```text
CROSS_BUILDER_CONTRACT_ITEM = PRE_VERIFIER_T4_IMPOSSIBLE
CURRENT_PRODUCER_RECORD = T0,T1,T2,T3,T4 where T4 aliases T3
ACTUAL_POST_VERIFIER_RECORD = terminal ledger T0,T1,T2,T3,T4 where T4 is sampled after verifier
ADJUDICATION_REQUIRED = registrar must define a pre-verifier T0-T3 contract or an explicit reserved-T4 state before Builder A changes the protocol
```

No T-label or trust-protocol code was changed in this relay. The finding is displayed rather than silently absorbed.

## 3. Static self-check

The self-check now:

1. constructs distinct pre-verifier and post-verifier synthetic scope objects;
2. requires each authorization record to equal exactly `{artifact_sha256, scope: ledger.scope}`;
3. validates the closed two-field schema and confirms `valid` is absent;
4. verifies the parent source order `T3 -> producer ledger -> verifier launch -> T4 -> terminal ledger`;
5. requires the two exact producer/terminal label maps; and
6. reports the pre-verifier T4 alias as a structural finding while preserving the passing static package checks.

Transcript:

```text
$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/materialize.py
{"checks": 66, "fixtures": 6, "gated": 10, "normal_sha256": "70123e515cadd09c21db5b4e0e24554ae089a9bb9458082f37fffdeceed74ae1", "optimized_sha256": "68de7be02a0fe6bff1dd35b417b53a2f779f19856e2c63972b32a41ece98c875", "structural": 56, "subject_lineage_root": "d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688"}

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/self_check.py
SELF_CHECK_OK syntax=5 canonical_json=all schemas=9 inventory=31 evidence_payloads=10 evidence=0/56 absent=56 fixture_obs=0/3 checks=66 structural=56 gated=10 fixtures=6 producer_fields=13 receipt_fields=16 fixture_fields=16 child_fields=14 verifier_manifest_fields=11 authorization_fields=artifact_sha256,scope authorization_digest=ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340 authorization_scope=equals_ledger_scope authorization_forward=producer,terminal,verifier_receiver t_labels=producer:T0,T1,T2,T3,T4(alias_T3);terminal:T0,T1,T2,T3,T4(actual_T4) t_label_finding=STRUCTURAL_PRELAUNCH_T4_ALIAS trust_root=7a80a5d52fd35701d8da02239178f63ef80e4f80ce8557636db99a326cf4c73c trust_sites=10 trust_agreement=definition,manifests,main_receiver,T0_T4,child_rows,producer_runtime,producer_T0_T4_value_only,verifier_receiver,terminal_runtime,terminal_T0_T4 exits=0/1/2 chain_invoked=false
```

Materialization and the self-check were each run twice. All hashes and transcript values were identical. Both runtime manifests rehash all 25 package rows, the package inventory rehashes all 31 rows, and all Builder A output/pycache directories remain empty.

## 4. Disclosed finite delta — seven files

Method: recursive cleanroom-versus-archive comparison excluding empty runtime output/pycache directories, followed by per-file no-index diffs. Exactly seven files differ; none was added or removed. Canonical JSON files occupy one line, so their semantic changes are stated directly.

| File | Before bytes / SHA-256 | After bytes / SHA-256 | Diff / disclosed change |
|---|---|---|---|
| `evaluator_build_A/parent.py` | 56,673 / `51b286a5e374cf7aee2e5f009d6cfc5486af333027c81392d5779b12870d637b` | 56,674 / `776255fac3f533017e01a57931f8097d5eab033bc3ac5676df0847e1d6fb28bb` | 1 hunk; 1 insertion, 1 deletion. Replace authorization `valid:true` with the existing `scope` argument. No T-label line changed. |
| `evaluator_build_A/tools/materialize.py` | 32,218 / `068baefae75107cbba74cffd81259212f8b31053b1eb0743196a01781e03db1c` | 32,196 / `14c184ba422df2066c651d6c7e1d6a404752cccfa2a4302fd2930b1e903c7053` | 1 hunk; 1 insertion, 1 deletion. Replace the authorization `valid` schema member with object-valued `scope`. |
| `evaluator_build_A/tools/self_check.py` | 36,384 / `1902ea8add89d7fdeeb1b98069ce38478622339ff195448248a4f7eb031d001e` | 37,644 / `1f3b08fdf4662f3bb567fe1a9e511766aba8daece253ae17727d3b9efc10a51e` | 8 hunks; 22 insertions, 7 deletions. Exercise distinct scope forwarding; update exact schema/record tests; audit temporal source order and both T maps; report the structural T4 alias. |
| `evaluator_build_A/schemas/terminal-ledger.schema.json` | 4,701 / `c13524f661830677d42e2d126cc28cca1264ecbc226ce2190ce1b25a63bb139e` | 4,687 / `960bee5560b314297a5ae17606f95bcd5b7943f11803ddf78984d55d1ec9acd6` | 1 canonical line replaced. Close authorization to `{artifact_sha256,scope}`. Trust-snapshot schema remains exact T0–T4 digests. |
| `evaluator_build_A/manifests/normal.json` | 8,850 / `a94ae441a046ba9c24535a166439d4507ab9fbec92a83a732d8ae0666c0a6755` | 8,850 / `70123e515cadd09c21db5b4e0e24554ae089a9bb9458082f37fffdeceed74ae1` | 1 canonical line replaced. Rehash the parent and terminal-schema package rows. |
| `evaluator_build_A/manifests/optimized.json` | 8,859 / `aee8a72f54498c4d0406faa6c528e7ab264172701213fbcd7a1123a8439be505` | 8,859 / `68de7be02a0fe6bff1dd35b417b53a2f779f19856e2c63972b32a41ece98c875` | 1 canonical line replaced. Same two package-row updates in optimized mode. |
| `evaluator_build_A/manifests/package_inventory.json` | 5,512 / `5549e558887661190d07502f65b8821c8d679b5891ed68775666fba09ece8201` | 5,512 / `4675570ebc1758484ccf285f374610eae6626e3e09dceb31118bc60b7098ad06` | 1 canonical line replaced. Rehash the six other changed package files. |

Total no-index text diff: 14 hunks, 28 insertions, 13 deletions. `producer.py`, the other eight schemas, check map, fixture manifest, evidence manifest and payloads, subject lineage, Builder B package, verifier-manifest contract/instance, all T-label construction lines, and every other Builder A package file are byte-identical to the PASTE 669 archive base.

## 5. PRE-SEAL PIN CHECK, fences, and verb audit

### 5.1 PRE-SEAL PIN CHECK

| Pin or invariant | Final result |
|---|---|
| V005 / addendum | `f8d1a7dc…` / `d17c5e79…`, exact and unchanged. |
| RD-22 decision | Exact 2,921 bytes; digest `ff84c4a8…`; structural-first-run scope and all closed gates unchanged. |
| Authorization | Exact two-field schema; R0-returned digest; `authorization.scope` equals the containing ledger's top-level `scope` for producer and terminal records. |
| T-label dataflow | Statically ordered T3, producer ledger, verifier launch, T4, terminal ledger. Producer T4 aliases T3; terminal T4 is actual. |
| Cross-builder item | `PRE_VERIFIER_T4_IMPOSSIBLE` displayed; no guessed sentinel, omission, or protocol edit. |
| Parent | `776255fa…`; 56,674 bytes; syntax clean; zero load-bearing `assert` nodes. |
| Terminal schema | `960bee55…`; authorization scope fixed; existing T0–T4 digest contract unchanged. |
| Runtime manifests | `70123e51…` / `68de7be0…`; 25/25 package rows rehashed in both. |
| Package inventory | 31/31 rows rehashed; digest `4675570e…`. |
| Delta census | Exactly seven disclosed files differ from the PASTE 669 archive base; none added or removed. |
| Output collision | Artifact and sidecar absent in both required locations immediately before creation. |
| Chain products | Builder A `outputs/` and all package pycache directories contain no files. |

The artifact sidecar is created adjacent only after these final artifact bytes are fixed. Sealing this report grants no chain, result, authorization, adjudication, or proof authority.

### 5.2 Fences

No producer, verifier, fixture, check executor, launcher, or full chain ran. Static tests constructed only in-memory ledger/scope records and inspected source order. No member was bound; no fixed point or end test ran; no physical quantity was evaluated; and no measured constant was read or compared. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false`.

No fence blocked the scope repair. The T4 issue is a cross-builder contract mismatch, not a machinery appeal; it is left for registrar adjudication.

### 5.3 Self verb audit under the verdict-line scope rule

| Verb | Scoped meaning |
|---|---|
| `forward` / `carry` | Copies the existing ledger scope value and already-verified authorization digest into content-addressed metadata; it grants no authorization. |
| `sample` / `observe` | Describes the structural placement of trust-snapshot calls; no snapshot or chain was run in this relay. |
| `alias` | Means the producer-ledger T4 field is sourced from the `t3` variable; it is not a claim of trust drift. |
| `require` / `validate` | Means sealed-contract, source-order, schema, canonical form, pin, or in-memory record checks. |
| `adjudicate` | Names a future registrar action; Builder A neither performed nor inferred it. |
| `sealed` | Applies only after adjacent sidecar creation and grants no chain, result, authorization, adjudication, or proof authority. |

AUTH_RECORD = {artifact_sha256, scope} forwarded
T_LABELS = STRUCTURAL_MISMATCH reported: pre-verifier producer ledger T4 aliases T3; actual T4 exists only in the post-verifier terminal ledger; no lawful reserved T4 exists under the current exact digest schema; registrar adjudication required
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN / (+forward/carry metadata only; sample/observe structural placement only; alias variable provenance not trust drift; require/validate structural; adjudicate future registrar action only; no chain result, authorization grant, or proof claimed)
