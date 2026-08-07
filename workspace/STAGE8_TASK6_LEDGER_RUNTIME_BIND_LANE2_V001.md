# STAGE 8 / TASK 6 / BUILD A — LEDGER RUNTIME BIND — LANE 2 V001

Lane: Lane 2, Builder A  
Relay: PASTE 660  
Context: Q-597 machine adjudication, applied to Builder A's parent  
Scope: verifier-manifest 4/1 timing split, post-production ledger construction/binding, exact launch substitution, run-ledger carriage, and recursive package hashes  
Authority claimed: none

```text
SPEC_V005_SHA256 = f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b
INTEGRATION_ADDENDUM_SHA256 = d17c5e79986bea431dec0b572019096f9c059bcc43876fda9134abc96ce0f260
PRIOR_PARENT_SHA256 = a3833419dcf08b522f9005762b14f9960ed1267a849b44115cfd91edd66f2040
FINAL_PARENT_SHA256 = e98e9644459ce56ead6aa22235aa339fa790466b3173d5463ab1abf997ed90da
UNBOUND_ROOT_SENTINEL = 0000000000000000000000000000000000000000000000000000000000000000
CHAIN_INVOKED = false
```

## 1. Preflight and defect disposition

| Check | Result |
|---|---|
| Output collision | Artifact and sidecar were absent in the cleanroom and archive workspace immediately before creation. |
| Governing spec | V005 remains `f8d1a7dc…`; R3–R8 produce and compare the two producer branches before R9. |
| Verifier contract | The sealed addendum remains `d17c5e79…`; the eleven/five/three/three field inventories remain unchanged. |
| B manifest behavior | Its authored `ledger_sha256` is the 64-zero sentinel and its argv carries exactly six named substitution tokens. |
| Prior Builder A state | `parent.py` was 39,480 bytes, `a3833419…`; both child manifests and package inventory matched the sealed PASTE 658 state. |
| Chain state | The evaluator chain was not invoked; `outputs/` and all three package pycache directories contain no files. |

The former `validate_verifier_manifest` mixed two time domains. It checked four immutable inputs and also searched the authored argv for an already-existing file whose digest equaled `input_roots.ledger_sha256`. That last condition was impossible when the lawful authored value was the sentinel and the ledger was not created until after the producer children.

The repaired joint is input versus output:

```text
PRE-LAUNCH, VALUE-CHECKED (4):
  spec_sha256
  runtime_snapshot_sha256
  runtime_gate_sha256
  evidence_root_sha256

PRE-LAUNCH, FORM-CHECKED ONLY (1):
  ledger_sha256
  rule: lowercase 64-hex; the all-zero UNBOUND sentinel is expressly lawful

POST-PRODUCTION, VALUE-BOUND (1):
  ledger_sha256 := SHA256(exact canonical producer-ledger bytes)
```

## 2. R1 — the 4/1 split and binding handshake

### 2.1 Pre-launch validation

`validate_verifier_manifest` still verifies the sealed manifest sidecar, manifest bytes, tight canonical form, exact 11-field inventory, schema, verifier root form, entry point, argv type, declared optimization, the closed stdout and exit contracts, nonauthoritative receipt, and declared output/receipt paths.

Its root treatment is now split:

- the expected-root map contains exactly spec, snapshot, gate, and evidence, each compared for value;
- `ledger_sha256` is required to match `[0-9a-f]{64}` and is not compared to a nonexistent output;
- no argv token is opened or hashed in this phase.

The all-zero sentinel therefore passes only as a syntactically valid pre-run placeholder. It cannot reach the verifier launch because the post-production gate rejects either a mismatched root or the sentinel itself.

### 2.2 Post-production ledger and bound launch context

After both producer processes, R7 receipt reclassification, R8 semantic comparison, and trust snapshot T3, the parent now:

1. Constructs `producer.ledger.json` from the two producer children, the canonical checks/fixtures/summary/scope, comparison record, authority firewall, pins, and T0–T3. Its pre-verifier T4 carrier is T3; the parent still requires the actual post-verifier T4 to equal T3/T2 before final carriage.
2. Exclusively writes the tight canonical producer-ledger bytes.
3. Computes `produced_ledger_sha = SHA256(producer_ledger_bytes)`.
4. Copies the authored verifier manifest in memory, replaces `input_roots.ledger_sha256` with the produced digest, and substitutes exactly once each of `${SPEC_PATH}`, `${LEDGER_PATH}`, `${LEDGER_SHA256}`, `${EVIDENCE_DIR}`, `${RUNTIME_SNAPSHOT_PATH}`, and `${RUNTIME_GATE_PATH}`.
5. Rejects a missing, duplicate, or undeclared unresolved `${...}` token.
6. Requires exactly one `--ledger` and one `--ledger-sha256`; requires their adjacent values to be the produced ledger's resolved path and digest; then opens that now-existing file and rehashes its exact bytes.
7. Tight-canonicalizes and exclusively writes `verifier.manifest.bound.json` and content-addresses that bound launch context.
8. Derives the verifier command from the bound argv while retaining the pinned Python executable and `-I -S -B` isolation flags.

The same bound object was supplied to Builder B's sealed `require_roots_bound()` in the static handshake test. The guard released only after the real digest replaced the sentinel.

### 2.3 Run-ledger and verifier-child carriage

The pre-verifier producer ledger records the authored root and the phase `POST_PRODUCTION_HASH_THEN_BIND`. It cannot contain its own final SHA-256 as a field: doing so would demand a forbidden self-hash fixed point. The digest is therefore carried in the content-addressed bound launch manifest and then recorded directly in the final terminal run ledger after R9.

The final terminal ledger's `scope.verifier_ledger_binding` records:

```text
authored_ledger_sha256
authored_manifest_sha256
bound_ledger_sha256
bound_manifest_sha256
producer_ledger_relative_path
sentinel_lawful
transition = UNBOUND_SENTINEL_TO_BOUND_POST_PRODUCTION
verifier_child_manifest_sha256
```

The verifier child row remains the addendum's exact fourteen-field row. Its existing `manifest_sha256` carrier now contains `bound_manifest_sha256`, not the authored sentinel manifest's digest. The content-addressed bound manifest contains both the real `input_roots.ledger_sha256` and the concrete `--ledger-sha256` argv value. Thus the child row records the bound launch context without silently adding a fifteenth field or weakening the closed child-row schema.

The authored manifest digest and sentinel remain separately visible in the terminal binding record, so the transition is not collapsed into its endpoint.

## 3. R2 — exact argv ledger-file check moved

The former pre-launch scan over all argv tokens was removed. The exact post-production check is stronger and later:

```text
producer ledger exclusive write
  < compute SHA-256
  < bind input_roots + six argv tokens
  < require one --ledger and one --ledger-sha256
  < resolve exact adjacent ledger path
  < rehash exact existing file and compare bound digest
  < verifier launch
```

The source-order audit verified the same strict ordering mechanically.

## 4. Disclosed finite delta — four files

| File | Before bytes / SHA-256 | After bytes / SHA-256 | Disclosed change |
|---|---|---|---|
| `evaluator_build_A/parent.py` | 39,480 / `a3833419dcf08b522f9005762b14f9960ed1267a849b44115cfd91edd66f2040` | 45,424 / `e98e9644459ce56ead6aa22235aa339fa790466b3173d5463ab1abf997ed90da` | Add sentinel/token constants; split pre/post verifier-manifest validation; create and hash the post-production producer ledger; bind roots and six argv tokens; add exact post-production ledger-file gate; content-address the bound manifest in the verifier child row; record transition in terminal scope; factor common ledger construction; carry trust snapshots as their existing content hashes. |
| `evaluator_build_A/manifests/normal.json` | 9,172 / `25d9495ff04d0f7f849b79c3e614468f1ff8d9b1f3379ea87cb49c74795dab12` | 9,172 / `2b0ee3aeb4c1634b5522fa878d79a920a2412e80d285e57acb2601b1d960ee9c` | Update only the parent package-row SHA-256/byte length and recursive manifest digest. |
| `evaluator_build_A/manifests/optimized.json` | 9,181 / `29592726fd7f099211e4c6a6a882d006e7b93a58bd8a8e6eed7ae3c2afbc33fd` | 9,181 / `713177580acaacaab1229f2681ca1e5c984d5fd58dc5ddee3a1937b3e93b2739` | Same parent package-row update for optimized mode. |
| `evaluator_build_A/manifests/package_inventory.json` | 5,512 / `041a9c7de586469cc6eb18cbaf6ec2ed7e7bed381e4fbfbae3801c5c474ff498` | 5,512 / `cf5db3ba818aba39f013b98538a7988a6b21e09942fa63c93db61d32b7ab6910` | Recursively update the parent, normal-manifest, and optimized-manifest rows. |

No producer, generator, self-check source, schema, evidence manifest, payload, check map, fixture manifest, subject-lineage manifest, or README byte changed. In particular:

```text
producer.py              = 14a679f75a15b96f93e70685ff422fbc74465038f8ae68b95ca3df16b8d76b45
tools/materialize.py     = 94f63527cdbc5b2ad8235806bc4ee23495d89c78efddf16fcbf95268909507e7
tools/self_check.py      = fc0d9f4ef64a770d5f0bafadaaaff569e547844fc9f7cbe828473ab8a7ec8117
evidence manifest       = 3da1ab07c3d3c5d3a87064cbfe758f8227bf6e0dca553c37b38329d5342b71e8
```

## 5. Static self-check and handshake transcript

Only source compilation, synthetic manifest/ledger binding, Builder B contract-guard invocation on synthetic non-subject bytes, deterministic package materialization, and canonical/schema/hash checks ran. No producer, check executor, fixture, verifier replay, or full chain ran.

```text
$ /usr/bin/python3 -I -S -B -c '<compile parent.py>'
parent_compile=PASS

$ /usr/bin/python3 -I -S -B - '<synthetic split/binding test>'
SPLIT_TEST_OK pre_pins=4 authored_ledger=sentinel post_ledger=bound argv_file=exact require_roots_bound=PASS
GUARD_BIDIRECTIONAL_OK sentinel=REFUSED bound=PASS

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/materialize.py
{"checks": 66, "fixtures": 6, "gated": 10, "normal_sha256": "2b0ee3aeb4c1634b5522fa878d79a920a2412e80d285e57acb2601b1d960ee9c", "optimized_sha256": "713177580acaacaab1229f2681ca1e5c984d5fd58dc5ddee3a1937b3e93b2739", "structural": 56, "subject_lineage_root": "d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688"}

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/self_check.py
SELF_CHECK_OK syntax=5 canonical_json=all schemas=9 inventory=31 evidence_payloads=10 evidence=0/56 absent=56 fixture_obs=0/3 checks=66 structural=56 gated=10 fixtures=6 fixture_fields=16 child_fields=14 verifier_manifest_fields=11 exits=0/1/2 chain_invoked=false

$ /usr/bin/python3 -I -S -B - '<pre-launch AST/source-order audit>'
PRELAUNCH_AUDIT_OK is_file_demands=1 pinned_sidecar=1 run_scoped_demands=0
ORDER_AUDIT_OK producer_ledger_write < post_production_argv_check < verifier_launch

ASSERT_AUDIT_OK parent=0
```

## 6. Audit of pre-launch object demands

`validate_verifier_manifest` contains one `.is_file()` demand: the sealed verifier-manifest sidecar. Its manifest bytes are then verified against that pin. These are authored immutable inputs.

No other pre-launch check asks for a run-scoped object:

- the four immutable roots are compared to already verified input values;
- the ledger root is checked for 64-hex form only;
- output and receipt declarations are compared as paths but are not required to exist;
- the ledger path and digest are opened/rehashed only in `post_production_verifier_validation`, after `exclusive_write(producer_ledger_path, ...)`;
- the preexisting-output check requires run outputs to be absent, not present.

Audit line:

```text
AUDIT = no other run-scoped pre-launch demand
```

## 7. PIN CHECK, fences, and verb audit

### 7.1 PRE-SEAL PIN CHECK

| Pin or invariant | Final result |
|---|---|
| V005 | `f8d1a7dc…`, exact and unchanged. |
| Integration addendum | `d17c5e79…`, exact and unchanged. |
| Evidence root | `e7820ca5…`, still value-checked pre-run. |
| Root split | Four named immutable roots value-checked; ledger root form-only pre-run and non-sentinel value-bound post-production. |
| Sentinel behavior | Authored B instance accepted pre-run; unchanged B `require_roots_bound()` rejects the sentinel and released on the synthetic bound manifest. |
| Argv binding | Six/six named tokens required exactly once; no unresolved token admitted; exact ledger path/file/digest gate ordered after ledger write. |
| Run carriage | Direct sentinel/bound values recorded in final terminal scope; verifier child `manifest_sha256` addresses the bound manifest while the exact 14-field schema is preserved. |
| Parent source | `e98e9644…`; syntax clean; zero Python `assert` nodes. |
| Runtime manifests | `2b0ee3ae…` / `71317758…`; 25/25 package rows independently rehashed in each. |
| Package inventory | 31/31 rows rehashed; inventory digest `cf5db3ba…`. |
| Output collision | Artifact and sidecar absent in both required locations immediately before creation. |
| Chain products | No files under Builder A `outputs/` or any package pycache directory. |

### 7.2 Fences

The synthetic ledger was non-subject `{}` bytes in a temporary directory and exercised only form, binding, and hash order. No evaluator component ran. No member was bound; no fixed point or end test ran; no physical quantity was evaluated; and no measured constant was read or compared. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false`.

No self-hash fixed point was attempted. The produced ledger's own digest is carried by the later bound manifest and final terminal record, which is why no MACHINERY-APPEAL is required.

### 7.3 Self verb audit under the verdict-line scope rule

| Verb | Scoped meaning |
|---|---|
| `bind` / `bound` | Replace the authored ledger sentinel with the SHA-256 of exact post-production producer-ledger bytes in the in-memory/root/argv launch context, then content-address that bound manifest. |
| `records` | The final terminal scope displays both values and transition; the exact verifier child row addresses the bound manifest through its existing `manifest_sha256` carrier. |
| `passes` / `released` | Static synthetic contract-handshake or static syntax/schema/hash validation only. |
| `audit` | AST/source-order inspection of Builder A parent code; no chain behavior inferred. |
| `sealed` | Applies only after adjacent sidecar creation and grants no chain, result, authorization, or proof authority. |

SPLIT = 4 pinned pre-run / 1 bound post-production
SENTINEL = lawful pre-run, bound before verifier launch (+recorded)
AUDIT = no other run-scoped pre-launch demand
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN / (+bind/record/pass/audit scopes; exact 14-field child schema preserved; no self-hash fixed point, chain result, authorization, or proof claimed)
