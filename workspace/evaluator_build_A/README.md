# RD-22 evaluator — Builder A package

This directory contains Builder A's fresh parent and producer. It contains no
verifier implementation. `parent.py` is the direct R0 entry point and
`producer.py` is the normal/optimized child target.

The child check map is pinned to specification V009. All 66 descriptor rows are
byte-identical to V008. In the preceding V006-to-V007 delta, exactly one
descriptor changed: `C-B-V009-06` received the principal-ruled
single-authority DAG and byte-grounding criterion.
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
- The sealed Builder B verifier manifest is the sole root-membership carrier.
  The parent verifies its sorted `verifier_root_members` rows directly against
  Builder B's package bytes and has no private or generated membership copy.
- `manifests/normal.json` and `manifests/optimized.json`: closed child
  inventories differing only in mode, optimization, and writable paths.
- `manifests/pins.json`: the one generated, closed content-pin manifest from
  which parent, materializer, and static checker load sealed input digests.

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
supply a canonical, sidecar-pinned
`rd22.verifier-manifest.v001` with exactly twelve fields. Under V009, its
`argv` is an exact 22-item schema
and its `input_roots` is an exact seven-field schema, including subject- and
evidence-manifest digests. The parent validates those schemas, canonical-JSON
stdout discipline, three-way exit contract, output and receipt paths, and
`receipt_authoritative=false` before launch. It launches the declared direct
script with the pinned interpreter isolation flags. Exit 1 (`faults_found`) and
exit 2 (`fail_closed`) remain distinct terminal facts and both stop the chain;
only exit 0 (`verified`) can enter R10.

Custodian C supplies a freshly created empty run directory and is the only
actor who invokes the full chain. A signature custodian may sign only the
terminal ledger after R10 succeeds. The parent fails closed before verifier
launch if the required verifier manifest, its pin, or any of its contracts is
absent or malformed.

`inputs/evidence/` contains fourteen byte-identical, content-addressed copies
of sealed packet/workspace search and display sources (including the V009 spec
and integration addendum), the exact 932-byte
relocated `stage_dependencies` member, its tight canonical single-authority DAG
serialization, and the prior paired-argument bytes retained as a supersession
witness. The current member and single-authority serialization ground only
`C-B-V009-06`. The remaining
55 structural records and all three structural-fixture records remain
`ABSENT_OF_RECORD`. No Builder B verifier, Custodian invocation, board change,
seal change, or detached signature is silently bundled here.

Each produced check row carries `invocation:null` or the exact seven-field
object `{opcode, result_name, args, instance_id, source_sha256, span,
span_sha256}`. For `C-B-V009-06`, the three explicit linkage fields agree with
the source digest and half-open byte span packed into `instance_id`. Its observed evidence
is the two payloads the procedure consumes: the tight-canonical `graph` object
and the exact 932-byte raw grounding span. The opcode-result trace is excluded
from evidence; the child receipt's `output_sha256` retains custody of the result
row without misclassifying execution testimony as an evidentiary input.
Builder B's currently sealed verdict schema carries the V008 spec const; its
digest is generated into the pin manifest and verified before launch. Builder
B's separately owned V009 boundary confirmation and re-pin are therefore
required before a chain invocation, and this package does not claim that
parallel custody act.

For every digest placed in a produced row's `observed_evidence_sha256s`, the
producer materializes the exact tight canonical JSON it consumed or produced
at the run-scoped `evidence/<digest>.json`. Both modes declare the same logical
content-addressed materialization; the parent rehashes every carrier, requires
the observed/materialized digest sets to agree, and exposes only those verified
run-root bytes to the independent verifier for replay.
