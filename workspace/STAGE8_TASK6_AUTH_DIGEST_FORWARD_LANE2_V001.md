# STAGE 8 / TASK 6 / BUILD A — AUTHORIZATION DIGEST FORWARDING — LANE 2 V001

Lane: Lane 2, Builder A  
Relay: PASTE 669  
Context: run 015 verifier diagnostic `authorization: missing 'artifact_sha256'`  
Scope: sealed authorization-record contract, R0 digest forwarding, producer/terminal ledger transport, verifier-output receiver, boundary schema, static self-check, recursive hashes, and disclosed delta  
Authority claimed: none

```text
SPEC_V005_SHA256 = f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b
INTEGRATION_ADDENDUM_SHA256 = d17c5e79986bea431dec0b572019096f9c059bcc43876fda9134abc96ce0f260
RD22_ARTIFACT_SHA256 = ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340
PRIOR_PARENT_SHA256 = 175068a311feaf90711874a502dda68b9ef561e92121dda0f9fb5f588c5dcce4
FINAL_PARENT_SHA256 = 51b286a5e374cf7aee2e5f009d6cfc5486af333027c81392d5779b12870d637b
CHAIN_INVOKED = false
```

## 1. Preflight and finding

| Check | Result |
|---|---|
| Output collision | This artifact and sidecar were absent in both the cleanroom and archive workspace immediately before creation. |
| Governing pins | V005 and the integration addendum verify at the exact hashes above. |
| RD-22 input | The principal decision verifies before use at `ff84c4a8…`; its bytes state that the decision artifact is the content-addressed RD-22 input. |
| Builder A base | The archive mirror is the exact sealed PASTE 668 state: parent `175068a3…`, normal/optimized manifests `b74b50aa…` / `2d7cc8dc…`, package inventory `02c74ac7…`. |
| Prior sealed artifact | `STAGE8_TASK6_TRUST_ROOT_DIGEST_LANE2_V001.md` and sidecar verify at `a6cda506…` / `228416b7…`. |
| Run 015 record | The retained producer ledger contains `authorization={rd22_sha256,valid}`. The digest value is correct but the digest key is not the contract key. |
| Chain state | No producer, verifier, check executor, fixture, launcher, or full chain was invoked in this relay. |

The old parent verified the authorization file at R0, discarded the computed digest, then separately authored this ledger object from the constant used as the expected pin:

```text
{"rd22_sha256": AUTHORIZATION_SHA256, "valid": true}
```

That is a two-places hazard: the expected value was correct, but the record was neither named by the contract nor derived from the value actually returned by R0 verification.

## 2. Field set derived from sealed contracts, not Builder B code

No Builder B source was consulted to select the authorization fields.

The sealed sources establish:

1. V005 §1 `BASE.authorization` is the RD-22 artifact plus its SHA-256.
2. V005 R0 requires the RD-22 hash to be present and valid.
3. V005 R10 carries one top-level `authorization` record and requires authorization validity.
4. The relay fixes the digest member name as `artifact_sha256`.
5. The integration addendum closes `rd22.verifier-manifest.v001` to exactly 11 fields and its `input_roots` to exactly five. It contains no direct authorization member, so adding one would violate that contract.

The resulting closed record is exactly:

```text
authorization = {
  artifact_sha256: lowercase 64-hex digest,
  valid: true
}
```

`valid` is the single sibling required by the sealed validity clauses. The invented `rd22_sha256` alias is removed, and no third alias or status field is added.

The terminal-ledger schema now closes this object to those two required members, requires `artifact_sha256` to be lowercase 64-hex, and fixes `valid` to `true`.

## 3. R0 value forwarding and verifier transport

### 3.1 Verified value, not literal

`verify_bytes_with_digest(path, expected)` now reads the bytes once, computes their actual SHA-256, fails if it differs from the expected pin, and returns both the verified bytes and the computed actual digest.

R0 consumes it as:

```text
authorization_data, authorization_artifact_sha256 =
    verify_bytes_with_digest(args.authorization, AUTHORIZATION_SHA256)
```

The constant remains solely the expected pin. Ledger construction never substitutes that constant. `verdict_ledger()` receives `authorization_artifact_sha256` as an argument, validates its form, and emits:

```text
{"artifact_sha256": authorization_artifact_sha256, "valid": true}
```

Both the post-production producer ledger and final terminal ledger receive the same R0-returned variable. The verifier-output receiver also compares `authorization_sha256` with that variable rather than with the expected-pin constant.

### 3.2 Bound launch context

The exact 11-field verifier manifest remains byte-contract compatible: no unauthorized top-level or `input_roots` field was invented. Post-production, the parent hashes the producer ledger and binds its path and digest into the verifier manifest's existing ledger argv/root carriers. The verifier therefore receives the two-field authorization record inside a content-addressed ledger.

The verifier child environment remains the required empty object. Authorization is not duplicated into an environment variable, where it would become an uncontracted second carrier.

Transport is therefore:

```text
verified RD-22 bytes at R0
  -> actual digest returned by verify_bytes_with_digest
  -> producer ledger authorization.artifact_sha256
  -> produced ledger SHA-256
  -> bound verifier manifest ledger path/digest
  -> verifier
```

The final terminal ledger independently carries the same two-field record.

## 4. Static self-check

The self-check reads the sealed authorization artifact identified by the normal manifest's authorization input row, calls the same parent verifier, checks the byte length, and uses the returned actual digest to construct synthetic producer and terminal ledgers. It requires both records to equal exactly:

```text
{"artifact_sha256":"ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340","valid":true}
```

It also requires the verifier-output receiver to accept that same runtime-derived value, verifies the closed two-field schema, requires all forwarding source receivers, and rejects either of these authored-literal forms:

```text
{"rd22_sha256": AUTHORIZATION_SHA256, "valid": true}
{"artifact_sha256": AUTHORIZATION_SHA256, "valid": true}
```

Transcript:

```text
$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/materialize.py
{"checks": 66, "fixtures": 6, "gated": 10, "normal_sha256": "a94ae441a046ba9c24535a166439d4507ab9fbec92a83a732d8ae0666c0a6755", "optimized_sha256": "aee8a72f54498c4d0406faa6c528e7ab264172701213fbcd7a1123a8439be505", "structural": 56, "subject_lineage_root": "d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688"}

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/self_check.py
SELF_CHECK_OK syntax=5 canonical_json=all schemas=9 inventory=31 evidence_payloads=10 evidence=0/56 absent=56 fixture_obs=0/3 checks=66 structural=56 gated=10 fixtures=6 producer_fields=13 receipt_fields=16 fixture_fields=16 child_fields=14 verifier_manifest_fields=11 authorization_fields=artifact_sha256,valid authorization_digest=ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340 authorization_forward=producer,terminal,verifier_receiver trust_root=7a80a5d52fd35701d8da02239178f63ef80e4f80ce8557636db99a326cf4c73c trust_sites=10 trust_agreement=definition,manifests,main_receiver,T0_T4,child_rows,producer_runtime,producer_T0_T4,verifier_receiver,terminal_runtime,terminal_T0_T4 exits=0/1/2 chain_invoked=false
```

Materialization and the self-check were each run twice. All hashes and transcript values were identical. Both runtime manifests rehash all 25 package rows, the package inventory rehashes all 31 rows, and all Builder A output/pycache directories remain empty.

## 5. Disclosed finite delta — seven files

Method: recursive cleanroom-versus-archive comparison excluding empty runtime output/pycache directories, followed by per-file no-index diffs. Exactly seven files differ; none was added or removed. Canonical JSON files occupy one line, so their semantic changes are stated directly.

| File | Before bytes / SHA-256 | After bytes / SHA-256 | Diff / disclosed change |
|---|---|---|---|
| `evaluator_build_A/parent.py` | 56,101 / `175068a311feaf90711874a502dda68b9ef561e92121dda0f9fb5f588c5dcce4` | 56,673 / `51b286a5e374cf7aee2e5f009d6cfc5486af333027c81392d5779b12870d637b` | 10 hunks; 16 insertions, 8 deletions. Return the actual verified digest; thread it into ledger construction and verifier-output validation; replace `rd22_sha256` with `artifact_sha256`; form-check the forwarded value. |
| `evaluator_build_A/tools/materialize.py` | 32,102 / `8c9f3737e556812c4cf5185b23d45d01e6bf0eeb195a510e98a4c44efffd617e` | 32,218 / `068baefae75107cbba74cffd81259212f8b31053b1eb0743196a01781e03db1c` | 2 hunks; 2 insertions, 1 deletion. Define the closed two-field authorization schema and install it in the terminal contract. |
| `evaluator_build_A/tools/self_check.py` | 33,940 / `e094446aa67f5aff2f42542407b52e7a174f2ec1ac3576c27e0617a7facb9747` | 36,384 / `1902ea8add89d7fdeeb1b98069ce38478622339ff195448248a4f7eb031d001e` | 6 hunks; 31 insertions, 7 deletions. Verify the sealed artifact, exercise the exact producer/terminal/verifier carriers, validate the field set/schema, and reject literal-backed record construction. |
| `evaluator_build_A/schemas/terminal-ledger.schema.json` | 4,517 / `b005c8ed00966fe3ee79c3f1fa0e0990fc9df94af5eed99f3a71dc687a9c9b03` | 4,701 / `c13524f661830677d42e2d126cc28cca1264ecbc226ce2190ce1b25a63bb139e` | 1 canonical line replaced. Close authorization to required `{artifact_sha256,valid}` with digest/true constraints. |
| `evaluator_build_A/manifests/normal.json` | 8,850 / `b74b50aaffc6ab52c9003cdea83a4f5dc1b3549e797a5b0dfa595c7e458ffb04` | 8,850 / `a94ae441a046ba9c24535a166439d4507ab9fbec92a83a732d8ae0666c0a6755` | 1 canonical line replaced. Rehash the parent and terminal-schema package rows. |
| `evaluator_build_A/manifests/optimized.json` | 8,859 / `2d7cc8dc19248e05b0bad56efa2feb6b935e35f4758e06c4e16970ec98f55d9f` | 8,859 / `aee8a72f54498c4d0406faa6c528e7ab264172701213fbcd7a1123a8439be505` | 1 canonical line replaced. Same two package-row updates in optimized mode. |
| `evaluator_build_A/manifests/package_inventory.json` | 5,512 / `02c74ac76f94c86fe70dee37c01e747cd947fd4302926b65480652bae293d0b3` | 5,512 / `5549e558887661190d07502f65b8821c8d679b5891ed68775666fba09ece8201` | 1 canonical line replaced. Rehash the six other changed package files. |

Total no-index text diff: 22 hunks, 53 insertions, 20 deletions. `producer.py`, the other eight schemas, check map, fixture manifest, evidence manifest and payloads, subject lineage, Builder B package, verifier-manifest contract/instance, and every other Builder A package file are byte-identical to the PASTE 668 archive base.

## 6. PRE-SEAL PIN CHECK, fences, and verb audit

### 6.1 PRE-SEAL PIN CHECK

| Pin or invariant | Final result |
|---|---|
| V005 / addendum | `f8d1a7dc…` / `d17c5e79…`, exact and unchanged. |
| RD-22 decision | Exact 2,921 bytes; R0/static verifier returns actual digest `ff84c4a8…` only after matching that pin. |
| Field derivation | Sealed V005/addendum/decision plus the relay; no Builder B code used. Exact fields are `artifact_sha256` and `valid`. |
| Runtime forwarding | Producer ledger, terminal ledger, and verifier-output receiver all consume the returned actual digest variable. |
| Manifest transport | Exact 11-field verifier contract unchanged; existing post-production ledger path/digest binding carries the record; child environment remains empty. |
| Parent | `51b286a5…`; 56,673 bytes; syntax clean; zero load-bearing `assert` nodes. |
| Terminal schema | `c13524f6…`; closed two-field authorization record verifies. |
| Runtime manifests | `a94ae441…` / `aee8a72f…`; 25/25 package rows rehashed in both. |
| Package inventory | 31/31 rows rehashed; digest `5549e558…`. |
| Delta census | Exactly seven disclosed files differ from the PASTE 668 archive base; none added or removed. |
| Output collision | Artifact and sidecar absent in both required locations immediately before creation. |
| Chain products | Builder A `outputs/` and all package pycache directories contain no files. |

The artifact sidecar is created adjacent only after these final artifact bytes are fixed. Sealing this report grants no chain, result, authorization, or proof authority.

### 6.2 Fences

No producer, verifier, fixture, check executor, launcher, or full chain ran. Static tests read and hashed the sealed authorization bytes and constructed only in-memory ledger records. No member was bound; no fixed point or end test ran; no physical quantity was evaluated; and no measured constant was read or compared. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false`.

No fence blocked this structural transport repair; no MACHINERY-APPEAL is required.

### 6.3 Self verb audit under the verdict-line scope rule

| Verb | Scoped meaning |
|---|---|
| `verify` / `return` | The static/R0 byte receiver hashes the sealed artifact, checks it against the expected pin, and returns that actual digest. |
| `forward` / `carry` | Copies the already-verified digest variable through content-addressed metadata; it does not infer or grant authorization. |
| `bind` | Refers only to the verifier manifest's run-scoped producer-ledger path/digest handshake, not member binding. |
| `validate` | Means source, schema, canonical form, pin, or in-memory record checks; no evaluator verdict was formed. |
| `sealed` | Applies only after adjacent sidecar creation and grants no chain, result, authorization, or proof authority. |

AUTH_RECORD = artifact_sha256 forwarded (verified value, not literal)
FIELDS = per contract (+artifact_sha256, valid)
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN / (+verify/return limited to RD-22 file SHA-256; forward/carry metadata only; bind run-scoped ledger metadata only; validate structural; no chain result, authorization grant, or proof claimed)
