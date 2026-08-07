# RD-22 evaluator — Builder A package

This directory contains Builder A's fresh parent and producer. It contains no
verifier implementation. `parent.py` is the direct R0 entry point and
`producer.py` is the normal/optimized child target.

The child check map is pinned to specification V007. Exactly one descriptor
changes from V006: `C-B-V009-06` now carries the principal-ruled
single-authority DAG and byte-grounding criterion; the other 65 rows are
byte-identical to V006.
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
  state. `C-B-V009-06` alone has the C77-authorized, content-addressed
  `stage_dependencies` envelope; the other 55 structural checks and all three
  structural fixture observations remain explicitly unavailable and fail
  input integrity rather than inventing evidence or expected verdicts.
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

The sealed integration addendum supplies the boundary contract. Builder B must
supply a canonical, sidecar-pinned `rd22.verifier-manifest.v001` with exactly
the addendum's eleven fields. The parent validates its five input roots,
canonical-JSON stdout discipline, three-way exit contract, output and receipt
paths, and `receipt_authoritative=false` before launch. It launches the declared
module with the pinned interpreter isolation flags. Exit 1 (`faults_found`) and
exit 2 (`fail_closed`) remain distinct terminal facts and both stop the chain;
only exit 0 (`verified`) can enter R10.

Custodian C supplies a freshly created empty run directory and is the only
actor who invokes the full chain. A signature custodian may sign only the
terminal ledger after R10 succeeds. The parent fails closed before verifier
launch if the required verifier manifest, its pin, or any of its contracts is
absent or malformed.

`inputs/evidence/` contains eleven byte-identical, content-addressed copies of
sealed packet/workspace search and display sources, the exact 932-byte
relocated `stage_dependencies` member, its tight canonical single-authority DAG
serialization, and the prior paired-argument bytes retained as a supersession
witness. The current member and single-authority serialization ground only
`C-B-V009-06`. The remaining
55 structural records and all three structural-fixture records remain
`ABSENT_OF_RECORD`. No Builder B verifier, Custodian invocation, board change,
seal change, or detached signature is silently bundled here.

Each produced check row carries `invocation:null` or the exact four-field object
`{args, instance_id, opcode, result_name}`. For `C-B-V009-06`, `instance_id`
packs the grounding source digest and half-open byte span. Its observed evidence
is the two payloads the procedure consumes: the tight-canonical `graph` object
and the exact 932-byte raw grounding span. The opcode-result trace is excluded
from evidence; the child receipt's `output_sha256` retains custody of the result
row without misclassifying execution testimony as an evidentiary input.
Builder B's sealed verdict schema carries the V007 spec const and is pinned at
`5acf066a01eec3762de6364766424be57ce6a1a19a4a34f0e15edc081b0cc1a2`;
the external-input manifest verifies those bytes before launch.

For every digest placed in a produced row's `observed_evidence_sha256s`, the
producer materializes the exact tight canonical JSON it consumed or produced
at the run-scoped `evidence/<digest>.json`. Both modes declare the same logical
content-addressed materialization; the parent rehashes every carrier, requires
the observed/materialized digest sets to agree, and exposes only those verified
run-root bytes to the independent verifier for replay.
