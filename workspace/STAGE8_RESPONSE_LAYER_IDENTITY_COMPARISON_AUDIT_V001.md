# CODEX 2 — Response-layer identity comparison

`alpha_computed = false; proof_authorized = false; kappa_record_computed = false.`

## Separate characterizations

**Route B (Step 1.3).** The raw-correlator response layer consumes a bilocal physical correlator `G` and
the completed CTP package; it produces the retarded Hessian `H_R[G]`, the exact induced kernel, and a
covariant local projector. Its formal relation and Keldysh extraction are specified at
`STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:730-821`; the physical package remains TYPE-U
(`:1077-1094`). It is a response of the complete microscopic source-record-field action to source/field
variations.

**Route A (E_ref / Stage 10).** The geometric matching layer consumes the canonical skeleton embedded in the
causal diamond, cell boundary conditions, and the public transverse response; it produces the normalization
that selects the reference rate `E_ref` for the Thomson map. The Stage-10 brief names the causal-diamond and
skeleton-to-cell embedding and says the response normalization is the deciding task
(`45_STAGE10_HANDOFF_GEOMETRIC_BRIEF_V001.md:34-45`). The ratio result states that E_ref is selected only by
derived Stage-10 response/matching (`21_DIMENSIONLESS_RATIO_RESULT_V001.md:20-39`).

## Feature comparison

| Feature | Route B | Route A | Relation |
|---|---|---|---|
| carrier | complete BR/CTP source-record-field package | canonical skeleton + causal-diamond cell | different stated carriers |
| source/probe | correlator `G`, source/field variations | public transverse response / matching probe | different probes |
| output | retarded Hessian/kernel/projector | reference-rate normalization and E_ref identification | different output types |
| domain | physical quotient, bilocal inverse, contacts/Ward data | Stage-10 geometric embedding and boundary conditions | neither contains the other on sealed text |
| purpose | construct response operator for C_record path | select the energy normalization in Thomson matching | complementary roles |
| sealed identity | none | none | no identity theorem |

## Rule

**DIFFERENT OBJECTS** is the supported classification: they share the word “response” but not a sealed
referent. The Route-A matching may consume a response supplied by Route B in a future completed pipeline,
but no sealed text states that it is the same object or a restriction/projection/completion. Treating them as
one would be unproved-identity transport.

`response_layers_same_object = false | TYPE-R | test: feature comparison above; no identity or inclusion
statement in the cited specifications.`
`response_layer_pipeline_composition = NO_VERDICT | TYPE-U | would-build: completed Route-B response plus
Stage-10 matching map and a typed composition theorem.`

## If a future union were attempted

The union would require the CTP physical quotient/measure, raw-correlator-to-retarded map, exact induced
kernel, covariant projector, causal-diamond/skeleton embedding, boundary conditions, Ward/causal tests, and
a derived matching theorem selecting E_ref. These are absent or adopted, not sealed as one object. No fork
was chosen and no build was attempted.

No git, commit, push, gate, or deploy action was performed.
