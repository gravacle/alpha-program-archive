# RD-22 evaluator — Builder A package

This directory contains Builder A's fresh parent and producer. It contains no
verifier implementation. `parent.py` is the direct R0 entry point and
`producer.py` is the normal/optimized child target.

The child check map is derived byte-for-byte from the 66 V005 descriptor rows.
Each structural row is bound to its descriptor SHA-256 and an ordered opcode
contract. A structural record that is absent, has the wrong descriptor hash,
has the wrong content root, omits an invocation, adds an invocation, or returns
a false opcode success bit fails closed. The ten gated rows return
`NOT_RUN_GATE` with `procedure_started=false` before dispatch.

## Sealed build inputs and runtime data

- `checks/check_map.json`: 66 IDs, 56 structural and 10 gated, plus exact row
  hashes, blocker byte spans, procedure text, predicates, and opcode contracts.
- `fixtures/fixture_manifest.json`: six exact regression descriptors.
- `inputs/subject_lineage_manifest.json`: the closed sealed-document subject
  root used by these manifests.
- `inputs/structural_evidence_manifest.json`: records the present evidence
  state. The governing input set contains no separately sealed per-check proof
  payloads or structural fixture observations, so those entries are explicitly
  unavailable; a run returns input-integrity failures rather than inventing
  evidence or expected verdicts.
- `manifests/normal.json` and `manifests/optimized.json`: closed child
  inventories differing only in mode, optimization, and writable paths.

`BRANCH_OUTCOME` is a build-time specification constant, never a producer
field:

| Branch ID | Outcome |
|---|---|
| `BRANCH-CANDIDATE-TYPED-COMPLETE` | `ADMITTED` |
| `BRANCH-FAILURE-UNRESOLVED` | `REJECTED` |
| `BRANCH-TIE-UNRESOLVED` | `REJECTED` |

The three IDs are the sealed descriptor's candidate/tie/failure partition.
The outcomes encode the blocker's directional demand: only a typed, completed
branch is admitted; unresolved ties and failures cannot become later choices.

## Integration boundary

Builder B supplies one sealed `rd22.verifier-manifest.v001` and exactly one
`verifier_source` inventory row. The verifier uses the CLI contract emitted by
the parent. Custodian C supplies a freshly created empty run directory and is
the only actor who invokes the full chain. A signature custodian may sign only
the terminal ledger after R10 succeeds.

After this package was independently built, Builder B's sealed public contract
became visible in the archive mirror. It emits
`gravacle.a35.verifier-verdict.v1` on stdout, declares a `python3 -m` launch,
and emits no §9.4 child receipt. Those public choices do not satisfy this
parent's isolated direct-child, verifier-manifest, and receipt contract. No A
code was changed to pretend otherwise: Custodian C must not invoke the chain
until a separately sealed integration adapter/contract resolves the launch,
output-schema, and receipt differences. The parent fails closed before R9 if
the required `rd22.verifier-manifest.v001` is absent.

No structural proof/evidence payload, Builder B verifier/integration adapter,
Custodian invocation, or detached signature is silently bundled here. These
are external custody or run inputs, not producer defaults.
