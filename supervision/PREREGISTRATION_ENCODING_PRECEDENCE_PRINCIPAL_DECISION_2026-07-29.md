# PREREGISTRATION STAGE-ENCODING PRECEDENCE — PRINCIPAL DECISION (2026-07-29)

PROVENANCE: A PRINCIPAL ACT, ruled 2026-07-29, session e268883f, on decision-queue item Q1.
THE ACT IS AUTHORITY AND IS DISCLOSED AS AUTHORITY. It is a SCOPING ruling in the R-14 form
("applied, not amended") — no immutable artifact is edited, weakened, or superseded.

## THE SITUATION RULED ON, AS VERIFIED (not as first reported)

`provenance/boundary_incidence_dynamics_preregistration_v011.json`, inside
`review_stage_semantics`, carries TWO stage encodings:

  `stage_dag` — 10 nodes, snake_case keys. Its dependency lists MIX seal names with
  NON-SEAL PROSE PRECONDITIONS: "passed A01-A29 and A35", "executed Gates 1-5",
  "composition-loop result", "external randomness-beacon rule", "complete target-free
  Q_spec", "three unanimous final-claim reports", "A33 independent end-to-end
  reconstruction".

  `stage_dependencies` — 11 nodes, UPPER-CASE seal names. Its dependency lists contain ONLY
  seal-to-seal edges. This is the encoding the evaluator consumes.

CORRECTION OF RECORD: the completeness critic reported these as "six internal
contradictions" such that "freezing this file freezes a self-contradiction." Direct
verification shows that framing OVERSTATES. Most of the six differences are not disagreements
but LEVEL differences — `stage_dag` carries non-seal preconditions that `stage_dependencies`
omits by design. FOUR differences are genuine graph-structure differences, AND IN EVERY ONE
OF THEM `stage_dependencies` IS THE STRICTER ENCODING:
  1. `stage_dependencies` contains END-TO-END-RECONSTRUCTION-SEAL; `stage_dag` has no such
     node (11 vs 10).
  2. `stage_dependencies` gives PREDICTION-MAP-SEAL an additional parent QSPEC-SPEC-SEAL.
  3. `stage_dependencies` gives HOLDOUT-UNIVERSE-SEAL the parent SPEC-SEAL.
  4. `stage_dependencies` gives QSPEC-SPEC-SEAL the parent SPEC-SEAL.
No case was found in which `stage_dag` is stricter. The pair is UNRANKED, not contradictory.

## THE RULING

1. `stage_dependencies` IS AUTHORITATIVE FOR GRAPH STRUCTURE — the node set, the edges, and
   therefore the fail-closed descendant computation. Where the two encodings differ on
   structure, `stage_dependencies` governs.
2. `stage_dag` IS DESCRIPTIVE AND REMAINS BINDING FOR THE NON-SEAL PRECONDITIONS IT CARRIES.
   Those preconditions (A-matrix rows passed, Gates 1-5 executed, the composition-loop
   result, the beacon rule, the complete target-free Q_spec, the unanimous report counts, the
   A33 reconstruction) ARE NOT DISCARDED by this ruling. They are obligations stated at a
   different level and every one of them still binds.
3. NO EDIT IS MADE to the preregistration. Its immutability claim survives intact, and
   SPEC-SEAL's "immutable V011 specification artifacts" precondition is not disturbed by this
   act. The ruling RANKS two encodings that were already both present; it changes no bytes.
4. THE STRICTER READING IS ADOPTED DELIBERATELY. Where the encodings differ, the ruling takes
   the encoding with MORE nodes and MORE required parents. This act cannot loosen any gate.
5. IT RATIFIES WHAT THE MACHINE ALREADY DOES. The evaluator consumes `stage_dependencies`;
   this ruling makes that consumption authorized rather than incidental.

PRECEDENT: R-14, in which F'-5 was APPLIED, SCOPED, AND NOT AMENDED
(`E1_CELL_4VOLUME_ADMITTED_ONLY_ON_PINNED_SKELETON`). That is the form used here. This is
NOT the first weakening act on an immutable artifact — nothing is weakened, and the corpus
still contains NO procedure for weakening a fence, which remains true after this ruling.

## SCOPE — WHAT THIS DOES NOT DO

Does NOT amend, edit, supersede, or reopen the preregistration. Does NOT discharge any
A-matrix row (all 35 remain PENDING). Does NOT seal anything or advance the ladder. Does NOT
resolve the report field-name mismatch — that is a separate, LANE-EXECUTABLE repair on the
EVALUATOR (which is unsealed and named in no immutability clause), already queued. Does NOT
address the missing `--subjects` file, also lane work. Does NOT authorize any computation.

## EXECUTION

Construction lane: record this precedence in the cleanroom authority chain citing this
decision by path and hash, and index it in `STAGE8_LANE_STATUS.md` in the same act. State on
the face of the recording artifact that `stage_dag`'s non-seal preconditions remain binding —
the most likely misreading of this ruling is that ranking the encodings discarded them.

alpha_computed = false; proof_authorized = false.
