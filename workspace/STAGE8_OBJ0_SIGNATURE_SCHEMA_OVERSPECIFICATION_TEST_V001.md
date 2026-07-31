# STAGE8 OBJ0 SIGNATURE SCHEMA OVERSPECIFICATION TEST V001

Lane: CODEX 1
Date: 2026-07-31
Relay: PASTE 195
Register head consulted: Q-100
Road justification: Q-83, advances Step 1 only.

Status: APPEND-ONLY RESULT. This artifact tests whether the heavy
`CERTIFIED_PROVENANCE_INDEXED_DEPENDENT_PRODUCER_SIGNATURE` presentation is
strictly required to enforce co-reference, or whether a flat record plus a
separately validated relational invariant can enforce the same obligation.

Fences honored: no computation of alpha, `kappa_record`, `kappa_Thomson`, any
coupling, scale, root, eigenvalue, beta function, `E_R`, `T_R`, `k_R`, or any
absolute interval; no comparison to a measured constant; no resolution of the
Misner-Sharp / Brown-York fork; no read of `a32_holdout/custodian_private/`.

Q-91 status: no git, no baseline, no deploy_status, no gate. Seal sidecar and
mirror only.

## 0. Source Scope And Declared Premises

Search/read scope:

```text
roots searched/read:
  /Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md
  /Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/

queries:
  "Q-98", "Q-99", "Q-100",
  "FLAT-SIGNATURE-INDEPENDENT-ORIGIN-REASSEMBLY",
  "CERTIFIED_PROVENANCE_INDEXED_DEPENDENT_PRODUCER_SIGNATURE",
  "common origin", "co-reference", "Obj_0_exact_signature"

exclusions:
  /Users/bgm/MB Work/a32_holdout/custodian_private/
  /Users/bgm/Documents/New project/**/a32_holdout/custodian_private/
```

F-GK3 declared inputs:

1. Q-98 amends Q-92 with two conditions: a dedicated verdict owner for each
   test and an adversarial countermodel attempted and failed
   (`QUESTIONS_SETTLED_REGISTER_V001.md:4011-4016`).
2. Q-99 refutes the inherited flat `Sig_0`: it contains only object/type
   metadata while the seven ports and origin certificate are siblings
   (`QUESTIONS_SETTLED_REGISTER_V001.md:4031-4042`).
3. Q-99 identifies the mechanism as co-reference: seven interfaces indexed by
   the same `Obj_0`, one replayable construction record, one direction-bearing
   graph, per-port traces, and an independently checkable aggregate certificate
   (`QUESTIONS_SETTLED_REGISTER_V001.md:4044-4049`).
4. Q-99 explicitly declines exclusivity: a flat record plus a separately
   validated relational invariant might express the same obligation, and no
   test there excludes it (`QUESTIONS_SETTLED_REGISTER_V001.md:4051-4056`).
5. Q-100 separates the primitive constructor context `I_prim` from the derived
   sector reference context `S_sector`; derived sector objects can be visible
   during port execution but cannot be constructor inputs for `Obj_0`
   (`QUESTIONS_SETTLED_REGISTER_V001.md:4082-4102`).
6. The Q-95 presentation supplies the old flat members and shows why the old
   `Sig_0` was too weak: `Obj_0`, `Sig_0`, `ConstructionRecord_0`,
   `PortDependencyGraph_0`, seven attempt ports, and
   `CommonOriginCertificate_0` were listed as sibling fields, while `Sig_0`
   contained only metadata
   (`STAGE8_JOINT_P0_BUILDABILITY_IN_PRINCIPLE_RESULT_V001.md:849-918`).
7. Relay 191's schema artifact states that dependent/refinement notation can
   force carriage of a witness, but physical truth still requires origin
   semantics, replayable trace, hostile controls, and an independent acceptance
   oracle
   (`STAGE8_OBJ0_EXACT_SIGNATURE_DOMAIN_CODOMAIN_SPEC_AND_BUILD_STOP_V001.md:568-587`).

No premise beyond that stack is introduced here.

## 1. Lead Determination

The flat-record alternative survives Q-99's own killer when the record carries a
separately validated co-reference invariant. Therefore the heavy dependent /
proof-carrying presentation is over-specified as a presentation. It is not
over-specified in functional content: origin traces, replay, direction-bearing
graph data, and aggregate validation remain load-bearing.

```text
flat_record_plus_validated_relational_invariant_survives_Q99_killer = true
  [SCHEMA-LEVEL TEST RESULT]

exclusive_need_for_dependent_proof_carrying_signature = false | TYPE-R |
  test: SAME-ATTACK-AGAINST-VALIDATED-FLAT-INVARIANT;
  the independent-origin substitution that broke the old flat metadata is
  rejected by the separately validated invariant, so the dependent/proof-
  carrying vocabulary is not exclusively required to enforce co-reference
```

This does not construct a physical `ExactSig_0`, does not construct `Obj_0`,
and does not prove physical common origin for P1-P7.

## 2. Minimal Formal Content Enforcing Co-Reference

The weakest checkable content is not "flat metadata". Q-99 already refuted that.
The weakest content found here is a flat record plus a separately validated
relational invariant over the record.

```text
FlatObj0CoReferenceRecord_0 :=
  (
    o        : Obj_0 identity token,
    r        : ConstructionRecord_0 identity token,
    g        : PortDependencyGraph_0 identity token,
    sig_meta : flat physical/presentation metadata, if frozen,

    rows     : (
      row_1 := (c1, t1, I_1, p_1, S_1, d_1),
      ...,
      row_7 := (c7, t7, I_7, p_7, S_7, d_7)
    ),

    q        : CrossRowCoherence_0(c1,...,c7),
    C        : CommonOriginCertificate_0,
    owner    : dedicated verdict-owner package for each invariant test
  )
```

The checkable invariant is:

```text
VALIDATED_COREFERENCE_INVARIANT_0(FlatObj0CoReferenceRecord_0) holds iff:

  K0. Single-root identity:
      the same ordered triple (o,r,g) is bound once and all port rows, traces,
      graph references, and certificate references use exactly that triple.

  K1. Per-port pairing:
      each port result c_i has exactly one trace t_i in the same row, and no
      port result may be accepted without its trace.

  K2. Trace validation:
      t_i is not a label, name, or self-assertion. It must validate as an
      origin trace from (o,r,g,I_i,p_i,S_i,d_i) to c_i under the frozen trace
      semantics.

  K3. Replay:
      r must contain the replayable construction record needed by K2, and each
      accepted t_i must be replayable against r rather than merely type-correct.

  K4. Direction-bearing graph:
      g must contain explicit direction-bearing edges from the Obj_0 role to
      every accepted port operation and from each port operation to its produced
      P_i candidate role; hidden upstream descendants, flags, validation
      fixtures, or cycles invalidate the invariant.

  K5. Context split:
      I_prim remains the constructor-visible primitive context. S_sector and
      its S_i subcontexts may be visible only during port execution and may not
      be smuggled into Obj_0 construction.

  K6. Aggregate validation:
      C is accepted only if an independent verdict owner checks all seven
      rows, traces, graph edges, context witnesses, and q jointly. A certificate
      name or generator name is not itself a verdict.
```

This schema is "flat" only in storage shape. The invariant is relational and
global. That is enough to make co-reference checkable rather than asserted:
the seven interfaces are accepted only as rows of one record whose invariant
binds every row to the same `(o,r,g)`.

```text
minimal_co_reference_content_identified = true [SCHEMA FACT]
minimal_content_is_flat_metadata_only = false | TYPE-R |
  test: Q-99 FLAT-SIGNATURE-INDEPENDENT-ORIGIN-REASSEMBLY
ValidatedFlatCoReferenceSchema_0_specified = true [FORMAL SCHEMA RESULT]
ValidatedFlatCoReferenceSchema_0_physical_derived = false | TYPE-C |
  constraint: this artifact specifies a formal schema and runs a schema-level
  countermodel; it does not construct or execute a physical Obj_0 instance
  release: construct a physical ExactSig_0 and Obj_0 instance, execute all
  seven ports, and pass the independent validator against the hostile roster
```

## 3. Q-99 Killer Against The Flat-Invariant Alternative

Q-99's killer is the same-typed independent-origin reassembly: replace one port
output with an externally originated constant while holding the old flat
metadata tuple fixed. Against the old `Sig_0`, the attack succeeds because the
metadata tuple does not depend on, contain, or validate the seven port witnesses
or aggregate certificate
(`STAGE8_OBJ0_EXACT_SIGNATURE_DOMAIN_CODOMAIN_SPEC_AND_BUILD_STOP_V001.md:503-532`).

Run against `FlatObj0CoReferenceRecord_0 + VALIDATED_COREFERENCE_INVARIANT_0`:

1. Replace `c_j` while keeping old `t_j`.
   Result: rejected by K2/K3, because `t_j` no longer validates or replays to
   the substituted `c_j`.
2. Replace both `c_j` and `t_j` with a pair from a different origin.
   Result: rejected by K0/K2, because the trace root is not the same `(o,r,g)`.
3. Replace both and forge `t_j` to name the same `(o,r,g)`.
   Result: rejected by K2/K3/K6, because a self-asserted or non-replayable trace
   is not accepted by the independent verdict owner.
4. Hide the foreign origin in `I_j`, `p_j`, `S_j`, or `d_j`.
   Result: rejected by K5/K6, because unlisted or forged subcontexts and hidden
   port inputs are disallowed.
5. Alter the graph so the substituted result appears connected.
   Result: rejected by K4/K6 unless the changed graph is itself the frozen `g`;
   a same-typed different graph is a different construction record/graph root,
   not co-reference with the original object.

Therefore the alternative survives the old killer. The old flat metadata died
because it had no relational invariant. A flat record with that invariant does
not die the same way.

```text
FLAT_SIGNATURE_INDEPENDENT_ORIGIN_REASSEMBLY_rejects_validated_flat_invariant = true
  [SCHEMA-LEVEL TEST RESULT]

old_flat_Sig_0_failure_generalizes_to_all_flat_records = false | TYPE-R |
  test: SAME-ATTACK-AGAINST-VALIDATED-FLAT-INVARIANT;
  the attack breaks a flat metadata tuple, not a flat record whose separately
  validated invariant binds every port row to the same root

flat_record_plus_validated_relational_invariant_common_origin = NO_VERDICT |
  deciding evidence: an actual physical instance and independent validator
  executing the invariant over all seven ports
```

## 4. Heavy Schema Components

| Component | Load-bearing? | Removal countermodel |
|---|---:|---|
| Proof-carrying vocabulary | No, as vocabulary. Yes, as validated witness content. | Removing the vocabulary alone does not admit a countermodel if K0-K6 remain. Removing witness/proof content admits dummy or self-asserted traces. |
| Many-sorted vocabulary | No, as full formal presentation. Yes, as role/type separation. | Removing all role/sort separation admits name-match substitutions among object, flag, trace, graph, certificate, and verdict roles. |
| Per-port origin traces | Yes. | A same-typed independently originated port result can be inserted with no row-level origin evidence. This is the Q-99 failure shape. |
| Replayable construction record | Yes. | A trace can be self-asserted or non-replayable while carrying the right labels. Relay 191 already states witness carriage alone does not prove truth. |
| Direction-bearing graph | Yes. | Hidden upstream inputs, descendant/flag consumption, or graph cycles can be disguised as undirected adjacency or sibling membership. |
| Aggregate certificate | Yes, as a global independently checked invariant. Not necessarily as a dependent generator. | Local traces can be mutually inconsistent, rooted in different records/graphs, or accepted piecemeal without a joint common-origin check. |

Result:

```text
proof_carrying_vocabulary_load_bearing_as_vocabulary = false | TYPE-R |
  test: VALIDATED-FLAT-INVARIANT-EQUIVALENCE; K0-K6 reject the Q-99 hostile
  substitution without dependent/proof-carrying notation

validated_witness_content_load_bearing = true [SCHEMA FACT]

many_sorted_vocabulary_load_bearing_as_vocabulary = false | TYPE-R |
  test: VALIDATED-FLAT-INVARIANT-EQUIVALENCE; explicit role fields and
  invariant checks can perform the same separation without imported many-sorted
  presentation machinery

role_and_type_separation_load_bearing = true [SCHEMA FACT]
per_port_origin_traces_load_bearing = true [SCHEMA FACT]
replayable_construction_record_load_bearing = true [SCHEMA FACT]
direction_bearing_dependency_graph_load_bearing = true [SCHEMA FACT]
aggregate_independent_certificate_load_bearing = true [SCHEMA FACT]

aggregate_certificate_generator_name_load_bearing = false | TYPE-R |
  test: VALIDATED-FLAT-INVARIANT-EQUIVALENCE; an independently validated
  relational invariant can perform the same aggregate check
```

The difficulty is real for the functional content. It is not real for the
specific imported presentation vocabulary.

## 5. Imported Vocabulary

Codex 2's reading is confirmed: dependent type, refinement, and proof-carrying
interface vocabulary is doing expressive work only. It makes the required
co-reference hard to omit syntactically, but it does not supply a physical
premise, constructor, or existence theorem. A flat record with K0-K6 expresses
the same schema-level obligation.

```text
dependent_refinement_proof_carrying_vocabulary_physical_work = false | TYPE-R |
  test: SOURCE-CITATION-AND-VALIDATED-FLAT-INVARIANT;
  source says the vocabulary supplies no physical premise/constructor/existence
  theorem, and the flat invariant rejects the same independent-origin attack

dependent_refinement_proof_carrying_vocabulary_expressive_work = true
  [SCHEMA FACT]

schema_difficulty_due_to_imported_vocabulary = true [SCHEMA FACT]
physical_common_origin_difficulty_due_to_imported_vocabulary = false | TYPE-R |
  test: WITNESS-TRUTH-SEPARATION; physical common origin still requires origin
  semantics, replay, hostile controls, and an independent validator regardless
  of presentation vocabulary
```

Q-80 status: no new formal class is required. The existing categories are not
wrong; the issue was an over-strong presentation choice for a co-reference
invariant.

```text
Q80_new_class_required_for_signature_schema_result = false | TYPE-R |
  test: FLAT-RECORD-PLUS-RELATIONAL-INVARIANT-FITS-EXISTING-SCHEMA-CATEGORIES
```

## 6. Q-92 Construction Status

Constructed here under Q-92: a minimal formal schema,
`ValidatedFlatCoReferenceSchema_0`, and its schema-level countermodel result.

Not constructed here: a physical `ExactSig_0`, a physical `Obj_0`, any port
object, any response object, or any value.

Q-92(a): premises declared in Section 0.

Q-92(b): failure-capable tests attached:

```text
T195-1 SAME-ATTACK-AGAINST-VALIDATED-FLAT-INVARIANT
T195-2 WITNESS-TRUTH-SEPARATION
T195-3 VALIDATED-FLAT-INVARIANT-EQUIVALENCE
T195-4 FLAT-RECORD-PLUS-RELATIONAL-INVARIANT-FITS-EXISTING-SCHEMA-CATEGORIES
```

Q-92(c): prerequisites exist for the formal schema test: Q-95's flat
presentation, Q-99's executed killer, Q-99's explicit alternative, Q-100's
context split, and Relay 191's trace/graph/certificate semantics. Physical
prerequisites for `ExactSig_0` and `Obj_0` do not exist.

Q-92(d): road step: `UNBLOCKS STEP 1` / `ADVANCES_STEP_1_ONLY` by reducing the
formal signature burden. It does not complete Step 1.

Q-92(e): dedicated schema-level verdict owner for T195-1 through T195-4 is this
Relay 195 Codex 1 artifact. This is not a physical instance validator and is
not carried into an Obj_0 build.

Q-92(f): adversarial countermodel attempted: the Q-99 independent-origin
reassembly, with the five cases in Section 3. It failed against the validated
flat invariant and had previously succeeded against old flat metadata.

```text
ValidatedFlatCoReferenceSchema_0_constructed = true [FORMAL SCHEMA CONSTRUCTION]
ValidatedFlatCoReferenceSchema_0_countermodel_attempted = true [SCHEMA FACT]
ValidatedFlatCoReferenceSchema_0_countermodel_failed = true [SCHEMA FACT]

ExactSig_0_constructed = false | TYPE-C |
  constraint: Q-99/Q-100 physical prerequisites remain unbuilt; this artifact
  constructs only a formal co-reference schema
  release: freeze exact physical category/domain/codomain, primitive bindings,
  sector reference bindings, port schemas, trace semantics, graph schema,
  validator owners, and hostile instance fixtures

Obj_0_constructed = false | TYPE-C |
  constraint: ExactSig_0 and the physical constructor inputs do not exist
  release: construct an ExactSig_0 and a target-independent Obj_0 construction
  rule from an adequate primitive inventory, then execute and validate ports

Step_1_completed_by_this_artifact = false | TYPE-C |
  constraint: this is a schema-over-specification result only
  release: every Step 1 physical prerequisite and validation route exists and
  passes its dedicated tests

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 7. Five Answers

1. Minimal formal content: a single flat record carrying `(o,r,g)`, seven
   port rows, seven traces, graph data, cross-row coherence, and an aggregate
   certificate, plus a separately validated invariant K0-K6. Metadata alone is
   refuted.
2. Author's alternative: survives Q-99's killer. The old attack rejects old flat
   metadata, not flat storage plus an actual validated co-reference invariant.
3. Load-bearing components: per-port traces, replayable construction record,
   direction-bearing graph, role/type separation, and aggregate independent
   validation are load-bearing. Dependent/proof-carrying/many-sorted vocabulary
   is not load-bearing as vocabulary.
4. Imported vocabulary: expressive work only, not physical work.
5. Q-92 construction: the minimal formal schema is constructed and tested here.
   The physical exact signature and `Obj_0` remain constraint-blocked.

