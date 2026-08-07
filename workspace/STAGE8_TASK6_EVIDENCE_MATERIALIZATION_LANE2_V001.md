# STAGE 8 / TASK 6 / TRANCHE — consumed-evidence materialization for replay

**Artifact:** `STAGE8_TASK6_EVIDENCE_MATERIALIZATION_LANE2_V001.md`  
**Lane:** Codex Lane 2 / Builder A  
**Date:** 2026-08-07  
**Custody:** bounded Builder A repair under Q-609; the registrar mirrors and re-invokes  
**Status:** STATIC BUILD REPAIR ONLY; the evaluator chain is not invoked here

## 1. Preflight and diagnosed contract

| Item | Verified result |
|---|---|
| register head | Q-609 is the final live register entry and records run 024's single replay fault |
| no-clobber | `STAGE8_TASK6_EVIDENCE_MATERIALIZATION_LANE2_V001.md` was absent in both commissioned locations before creation |
| run-024 producer result | `C-B-V009-06` is `PASS` in normal and optimized outputs; both cite observed digest `87fa71f271b3b1471da2a9b882c79c749b03e5f0f666ba9acba8d6ef3d0fa43a` |
| run-024 verifier finding | `REPLAY`: missing `rd22_run_024/evidence/87fa71f2….json`; the refusal is correct |
| existing evidence root | `1fbb3c0771e3c58dc87db6fcc5dad286331c25c051c98a1afeac3ec3fecb64a6`, unchanged |
| existing evidence manifest | `007b01f7bd35da47e6b7cdcd16f69630f3766e5f4123bbd135fb4129a4840adc`, unchanged |
| existing check map | `1197e8b8ebaef433bf5c96f83d4324e3f48e66fb6d4425c830c953b13317e7d0`, unchanged |

The observed digest is not the digest of either input file. It is the SHA-256
of the exact tight canonical JSON array returned by the producer's opcode
execution. Renaming an input payload would therefore be false evidence. The
lawful carrier is the exact 441-byte canonical array whose hash the row emits.

The gates remain:

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 2. Implemented materialization contract

### 2.1 Producer: bytes and digest stay joined

`execute_structural` now forms the canonical opcode-output bytes once, hashes
those exact bytes, emits the digest in `observed_evidence_sha256s`, and sends
the same byte object to a materialization sink. This applies to successful,
failed, and structural-error executions that emit an observed digest.

For the current row, the exact replay carrier is:

```json
[{"instance_id":"stage_dependencies@13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd:[18898,19830)","opcode":"DAG","result":{"nodes":["ALPHA-RESULT-SEAL","CORE-RESULT-SEAL","END-TO-END-RECONSTRUCTION-SEAL","FINAL-CLAIM-SEAL","HOLDOUT-RESULT-SEAL","HOLDOUT-UNIVERSE-SEAL","PARENT-COMPARISON","PREDICTION-MAP-SEAL","QSPEC-SPEC-SEAL","SPEC-SEAL","THOMSON-RESULT-SEAL"],"reason":"","success":true},"result_name":"r_auto_01_dag"}]
```

```text
byte length = 441
SHA-256    = 87fa71f271b3b1471da2a9b882c79c749b03e5f0f666ba9acba8d6ef3d0fa43a
run path   = evidence/87fa71f271b3b1471da2a9b882c79c749b03e5f0f666ba9acba8d6ef3d0fa43a.json
```

Materialization is fail-closed:

1. the claimed digest must be lowercase 64-hex;
2. the bytes must rehash to that digest;
3. the bytes must be one tight canonical JSON value;
4. the destination must be the supplied run-root evidence directory;
5. an absent target is exclusively created;
6. an existing target is lawful only when it is a regular non-symlink file
   with byte-identical contents;
7. the stored file is rehashed after create-or-verify.

The producer also enforces the universal guard after all check and fixture
rows are formed:

```text
set(all emitted observed_evidence_sha256s)
  == set(all content-addressed materializations)
```

If a future fixture carries an observed digest already present in the sealed
evidence inventory, the producer verifies and materializes those existing
canonical JSON bytes. A digest with neither an execution-produced byte object
nor one exact sealed-inventory source fails `CONSUMED_EVIDENCE_SOURCE`.

### 2.2 Parent: independent run-root rehash and receipt classification

Both children receive only the run-scoped `--consumed-evidence-dir`. After
each child returns, the parent independently collects every observed digest
from its check and fixture rows, requires
`run_root/evidence/<digest>.json`, parses it as tight canonical JSON, and
rehashes it to the row's digest. Those exact verified paths are then:

- added to that child's read/open allowlist;
- required in the child's write and mutation ledgers under the explicit
  operation `content_addressed_materialize`;
- available to the verifier only through `${EVIDENCE_DIR}` at the run root;
- included in the parent-side verifier allowlist as generic run-evidence JSON,
  alongside but not confused with the six event-ledger payload classes.

Normal and optimized children declare the same logical content-addressed
materialization. The first exclusive creation and the second byte-identical
verification are both bound to the same digest. A filename match without a
content match remains a terminal failure.

No field was added to the compared producer output or the closed receipt:

```text
producer output fields = 13 (unchanged)
child receipt fields   = 16 (unchanged)
comparison mask        = process_id, monotonic_duration, python_optimize (unchanged)
```

The manifests now declare `consumed_evidence` in their permitted write and
mutation classes and declare `evidence/<observed_sha256>.json` as a run-scoped
writable path.

## 3. Static self-check and new guard

Commands run:

```text
python3 evaluator_build_A/tools/materialize.py
python3 evaluator_build_A/tools/self_check.py
```

Materialization regenerated 66 checks, 56 structural rows, 10 gated rows, and
six fixtures. The static self-check:

1. executed only the already-authorized structural DAG fixture in a temporary
   directory;
2. captured the exact bytes paired with its observed digest;
3. materialized them through the producer's new function;
4. rediscovered and rehashed them through the parent's independent function;
5. checked the exact `content_addressed_materialize` receipt row;
6. required equality of the observed, producer-materialized, and
   parent-discovered digest sets.

The relevant transcript is:

```text
SELF_CHECK_OK
evidence=1/56 absent=55
v009_06_opcode=DAG:PASS
v009_06_observed=87fa71f271b3b1471da2a9b882c79c749b03e5f0f666ba9acba8d6ef3d0fa43a
consumed_implies_materialized=PASS
consumed_path=run_root/evidence/<digest>.json
producer_fields=13
receipt_fields=16
chain_invoked=false
```

The static test uses a temporary directory and does not invoke the parent
state machine, producer subprocesses, verifier, terminal ledger, or any
physical/gated opcode.

## 4. Complete disclosed delta

The pre-relay package was copied to a fresh temporary baseline before edits.
`diff -qr` finds exactly these eight changed files and no others:

| File | Old SHA-256 | New SHA-256 | Disclosed reason |
|---|---|---|---|
| `README.md` | `40ee650ab0b3b2fb90fe7dabb84003ca11cd46c785b16d02a452603e4c31913d` | `20302996db734eedfb358d72708c768bace325d7534db17178a10a47e14c388c` | document replay-carrier custody |
| `parent.py` | `061a2a303bcdf3fae23100e79a3f03c182029f448bdad4cd18cfc3d10d91a509` | `78d99947447e6688202f3071cce37980d944bf747a8ee3379eba88afa65c953b` | collect, rehash, classify, and expose consumed carriers |
| `producer.py` | `d565221e701cadea3d75dc21003b322d097decb2f1913a868901064bc81cde9e` | `8bbd11e4289bf8da5c5b589daf971054eb6c8f5efe3d789f70777f0a59a7523b` | retain and materialize exact canonical opcode-output bytes |
| `tools/materialize.py` | `c5ed9995aa30435d6d2fb995b29ed173fddac40b9536a544c5410b79ad974861` | `8c4d370f65b00b15ec5b49630187f54f6aa35aac9a82c0ffee76a313f56d1e86` | declare the new run-scoped write/mutation class |
| `tools/self_check.py` | `b36dcfb1640db1f83398a7b1f620de8b9dcaeaa4be9ab3b894c6f92599e6301d` | `adfddf6fe89e8e0d4ca2240e6a1c7e928bf69e1ec6abd359538668a1ac19299a` | add consumed-implies-materialized guard and receiver audit |
| `manifests/normal.json` | `ed1d184e0abb9e8780f8247638e41579d2d708d7fd3adeb2c731ffe2d3397bb1` | `16534f20ba096ae0a3ea78638d744f3bae2ffae1633940db59b8fa765f55b104` | refreshed code inventory and declared write class |
| `manifests/optimized.json` | `58763ead5db1b6c33aabd1e7a735b0b57966a756b4328b2353395e7eb149a209` | `dd9d72229a903834b60dba68b11b8904f28291ee08cba591a0f8a573fe153094` | refreshed code inventory and declared write class |
| `manifests/package_inventory.json` | `3c791abc5e13b5fc8c51a855048f396ccacba574816fa33a26c751f6811f43cd` | `1dcb3517db383fadfdbb1bbad4fd6c7f314ce62c91e19cc323887a78f0789b46` | refreshed complete package hashes |

The check map, structural evidence manifest, evidence payloads, declared
evidence root, subject lineage, schemas, fixtures, runtime pin, authorization
pin, gates, and Builder B package are byte-unchanged.

## 5. PIN CHECK, battery, and non-actions

| Pin/check | Result |
|---|---|
| package inventory | 32/32 declared package members rehashed |
| normal manifest | `16534f20ba096ae0a3ea78638d744f3bae2ffae1633940db59b8fa765f55b104` |
| optimized manifest | `dd9d72229a903834b60dba68b11b8904f28291ee08cba591a0f8a573fe153094` |
| evidence manifest/root | unchanged and verified |
| canonical replay payload | 441 bytes; `87fa71f2…`; tight JSON; no trailing newline |
| consumed/materialized quantification | exact set equality over every check and fixture observed digest |
| F_PLDEC | clean; no symbolic/spectral or physical path reached |
| authority firewall | unchanged; no authorization, board, or seal claim |

No member was bound. No fixed point or end test ran. No physical quantity was
evaluated and no measured constant was compared. The row's prior PASS is not
re-issued here, and the verifier's next verdict is not predicted. The registrar
alone mirrors and re-invokes.

MATERIALIZATION = consumed evidence -> run root (content-addressed)
SELF_CHECK = passed (+the new guard line)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
