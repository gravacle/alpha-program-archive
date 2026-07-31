# STAGE8 K0-K6 DERIVED STRUCTURES INVARIANT TEST V001

Lane: CODEX 1
Date: 2026-07-31
Relay: PASTE 197
Register head consulted: Q-103
Road justification: Q-83, advances Step 1.

Status: APPEND-ONLY TEST RESULT. This artifact tests whether the exact K0-K6
relational invariant from
`STAGE8_OBJ0_SIGNATURE_SCHEMA_OVERSPECIFICATION_TEST_V001.md` already holds over
the three derived structures named by Q-41, Q-42, and Q-43:

1. source-sector quasifree CAR algebra and GNS representation;
2. completed public-record direct limit;
3. base source-record graded-tensor join / stable dressed outgoing-record
   monomorphism.

Q-91 status: no git, no baseline, no deploy_status, no gate. Seal sidecar and
mirror only.

Fences honored: no computation of alpha, `kappa_record`, `kappa_Thomson`, any
coupling, scale, root, eigenvalue, beta function, `E_R`, `T_R`, `k_R`, or any
absolute interval; no comparison to a measured constant; no resolution of the
Misner-Sharp / Brown-York fork; no read of `a32_holdout/custodian_private/`.

## 0. Scope And Premises

Search/read scope:

```text
roots searched/read:
  /Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md
  /Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/

queries:
  "Q-41", "Q-42", "Q-43", "SOURCE_QUASIFREE_GNS_DERIVED",
  "COMPLETED_RECORD_DIRECT_LIMIT_DERIVED", "SOURCE_RECORD_BASE_COMPOSITION",
  "FlatObj0CoReferenceRecord_0", "VALIDATED_COREFERENCE_INVARIANT_0",
  "OriginTrace_", "CommonOriginCertificate_0", "CrossRowCoherence_0",
  "S_sector", "AttemptPort"

exclusions:
  **/a32_holdout/custodian_private/**
  Codex 2's authority/sealing adjudication for the seven used-as-primitive objects
  Einstein's marginality workstream
```

F-GK3 declared inputs:

1. K0-K6 is fixed by
   `STAGE8_OBJ0_SIGNATURE_SCHEMA_OVERSPECIFICATION_TEST_V001.md:128-159`.
   It is not weakened here.
2. Q-41 constructs the source-sector CAR/quasifree/GNS object and expressly
   withholds the full completed source-record-field algebra
   (`QUESTIONS_SETTLED_REGISTER_V001.md:1745-1767`;
   `STAGE8_GAMMA_K_QUASIFREE_ROOT_ROUTE_ATTEMPT_V001.md:185-214`).
3. Q-42 records that the source sector and record sector exist, but the
   source-record-field CTP extension remains untyped
   (`QUESTIONS_SETTLED_REGISTER_V001.md:1792-1826`;
   `STAGE8_GAMMA_K_COMPLETED_ALGEBRA_EXTENSION_ATTEMPT_V001.md:318-327`).
4. Q-43 types the base source-record join and stable outgoing-record monomorphism,
   but still withholds the full source-record-field CTP producer
   (`QUESTIONS_SETTLED_REGISTER_V001.md:1830-1858`;
   `STAGE8_GAMMA_K_SOURCE_RECORD_COMPOSITION_TYPING_TESTS_V001.md:444-467`).
5. Q-100 classifies the source GNS, record direct limit, and base tensor join as
   `S_sector` descendants visible during port execution, not as `I_prim`
   constructor inputs (`QUESTIONS_SETTLED_REGISTER_V001.md:4082-4102`).

No premise beyond that stack is introduced here.

## 1. Lead Determination

K0-K6 does **not** hold over the three derived structures as they currently
exist. The reason is not that the structures are useless or false. The reason is
typed: they are `S_sector` reference structures, while K0-K6 is an invariant over
an executed seven-row co-reference record.

The only clause that holds in the relevant direction is K5's context split:
Q-100 already says these three objects remain derived sector references visible
during port execution, never constructor inputs. The other clauses require an
input record that does not exist: one `(o,r,g)` root, seven `c_i/t_i` rows,
replayable construction record, direction-bearing P-port graph, cross-row
coherence, and independently validated aggregate certificate.

```text
K0_K6_holds_over_Q41_Q42_Q43_structures = false | TYPE-R |
  test: DOMAIN-AND-FIELD-INSPECTION; Q-41/Q-42/Q-43 provide three S_sector
  reference structures, not a FlatObj0CoReferenceRecord_0 with seven port rows,
  traces, graph, replay record, cross-row coherence and certificate

three_structures_are_available_as_S_sector_references = true [STRUCTURAL FACT]
three_structures_are_a_K0_K6_invariant_instance = false | TYPE-R |
  test: REQUIRED-FIELDS-PRESENT; required K0-K6 record fields are absent
```

This is a structural negative, not an anti-fit precaution. If the invariant had
held, this artifact would report it.

## 2. K0-K6 Stated Exactly

The invariant's input record is stated at
`STAGE8_OBJ0_SIGNATURE_SCHEMA_OVERSPECIFICATION_TEST_V001.md:103-120`:

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

The clauses are:

```text
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

## 3. Clause-By-Clause Test Over The Three Structures

The three structures are:

```text
Q41 source-sector object:
  source one-particle Hilbert space;
  source CAR algebra;
  source quasifree state;
  source-sector GNS representation.
  Source: STAGE8_GAMMA_K_QUASIFREE_ROOT_ROUTE_ATTEMPT_V001.md:185-196.

Q42 completed record object:
  completed public-record direct limit.
  Source: STAGE8_GAMMA_K_COMPLETED_ALGEBRA_EXTENSION_ATTEMPT_V001.md:318-327.

Q43 base source-record join:
  SOURCE_RECORD_BASE_COMPOSITION_TYPE = TENSOR_PRODUCT;
  OUTPUT_RECORD_IN_FULL_PARENT_TYPE = STABLE_DRESSED_RECORD_MONOMORPHISM.
  Source: STAGE8_GAMMA_K_SOURCE_RECORD_COMPOSITION_TYPING_TESTS_V001.md:444-467.
```

| Clause | Status over Q41/Q42/Q43 | Reason |
|---|---|---|
| K0 single-root identity | FAILS | No single `(o,r,g)` root record binds the three structures together as one `FlatObj0CoReferenceRecord_0`; Q43 depends on Q41/Q42, but that is not the same as a frozen object/construction/graph triple for seven rows. |
| K1 per-port pairing | FAILS | There are no seven port rows `(c1,t1)...(c7,t7)` over these structures. |
| K2 trace validation | NO_VERDICT after K1 failure | There are no `t_i` traces to validate. Absence of traces blocks validation; it is not a failed trace. |
| K3 replay | FAILS | Q41/Q42/Q43 are provenance-bearing artifacts, but no `r : ConstructionRecord_0` exists that replays seven port outputs and traces. |
| K4 direction-bearing graph | FAILS | Q43 supplies a typed source-record relation, but no `g : PortDependencyGraph_0` with edges from `Obj_0` to all seven accepted port operations and from each port to P_i candidate roles. |
| K5 context split | HOLDS NARROWLY | Q100 and the primitive audit classify these structures as `S_sector`, not `I_prim`. This preserves the constructor/execution split. The per-port `S_i,d_i` witnesses are still absent. |
| K6 aggregate validation | FAILS | No `CommonOriginCertificate_0`, cross-row `q`, or independent validator over all seven rows exists. |

Typed clause ledger:

```text
K0_over_Q41_Q42_Q43_holds = false | TYPE-R |
  test: SINGLE-ROOT-FIELD-INSPECTION; no shared (o,r,g) record root exists

K1_over_Q41_Q42_Q43_holds = false | TYPE-R |
  test: SEVEN-ROW-FIELD-INSPECTION; no c1/t1 through c7/t7 rows exist

K2_over_Q41_Q42_Q43_holds = NO_VERDICT |
  blocker: no t_i traces exist to validate under frozen trace semantics

K3_over_Q41_Q42_Q43_holds = false | TYPE-R |
  test: REPLAY-RECORD-FIELD-INSPECTION; no replayable seven-port construction
  record r exists

K4_over_Q41_Q42_Q43_holds = false | TYPE-R |
  test: PORT-GRAPH-FIELD-INSPECTION; no direction-bearing seven-port graph g
  exists

K5_context_split_over_Q41_Q42_Q43_holds = true [STRUCTURAL FACT]

K5_full_port_subcontext_witnesses_present = false | TYPE-U |
  would-build: bind I_i,p_i,S_i,d_i witnesses for each of the seven port rows

K6_over_Q41_Q42_Q43_holds = false | TYPE-R |
  test: AGGREGATE-CERTIFICATE-FIELD-INSPECTION; no q, C, or independent
  seven-row verdict owner exists
```

The positive K5 result is not enough to make the total invariant hold. K5 says
the three structures are in the right *place* for later port execution. It does
not supply the executed ports or common-origin certificate.

## 4. Independent-Origin Reassembly On These Structures

Q-102 showed at schema level that a flat record plus K0-K6 rejects
`FLAT-SIGNATURE-INDEPENDENT-ORIGIN-REASSEMBLY`. That result does not transfer
to Q41/Q42/Q43 as currently recorded, because the K0-K6 record and validator are
not instantiated over them.

Run the hostile substitution against the actual state:

1. Substitute a same-typed source-sector GNS object for Q41 while leaving Q42
   and Q43 textually identified.
2. Substitute a same-typed completed record direct-limit object for Q42 while
   leaving Q41 and Q43 textually identified.
3. Substitute a same-typed base source-record tensor join for Q43 while leaving
   Q41 and Q42 textually identified.

There is no K0-K6 validator present that can inspect `(o,r,g)`, port rows,
traces, replay record, graph, or aggregate certificate and reject the reassembly.
Existing file seals can protect the bytes of particular artifacts, but byte
integrity is not the K0-K6 common-origin invariant.

```text
K0_K6_defeats_independent_origin_reassembly_on_Q41_Q42_Q43 = false | TYPE-C |
  constraint: no FlatObj0CoReferenceRecord_0 instance or independent validator
  exists over the three structures
  release: instantiate the seven-row record and validator, then submit same-typed
  independent-origin replacements for each row/reference and verify rejection

schema_level_countermodel_result_transfers_to_actual_three_structures = false | TYPE-R |
  test: INSTANCE-PRESENCE-CHECK; Q-102's countermodel was run against a formal
  schema, while no actual K0-K6 instance exists here
```

This does not refute the schema-level K0-K6 result. It refutes the stronger
claim that the existing three structures already instantiate that result.

## 5. What The Invariant Still Needs

The missing object is larger than the sealing status of the seven
used-as-primitive objects. Sealing those objects may supply authority for some
inputs, but K0-K6 still needs an actual co-reference record and validator.

Required missing objects:

```text
M1. A chosen single root triple (o,r,g):
    o : object identity token;
    r : replayable ConstructionRecord_0;
    g : direction-bearing PortDependencyGraph_0.

M2. Seven executed port rows:
    c1/t1 through c7/t7, not only Q41/Q42/Q43 reference artifacts.

M3. Exact row content:
    P1 completed carrier/domain;
    P2 source embedding/restricted-state coherence using Q41 as S_sector;
    P3 record embedding/monomorphism coherence using Q42/Q43 as S_sector;
    P4 physical field/CTP package;
    P5 rho_pre/effects/domains;
    P6 dynamics/normalization interface;
    P7 contact/source/raw-correlator interface.

M4. Frozen subcontext witnesses:
    I_i,p_i,S_i,d_i for each row, with S_i only execution-visible.

M5. Trace semantics and replay:
    every t_i must validate and replay from (o,r,g,I_i,p_i,S_i,d_i) to c_i.

M6. Cross-row coherence:
    q linking P2/P5, P2/P4, P3/Q42/Q43, P4/P5/P6/P7 domains, and P7's use of
    P5/P6, as sketched in
    STAGE8_OBJ0_EXACT_SIGNATURE_DOMAIN_CODOMAIN_SPEC_AND_BUILD_STOP_V001.md:1145-1182.

M7. Independent aggregate validation:
    CommonOriginCertificate_0 plus dedicated verdict owners and hostile fixtures.
```

Overlap with Codex 2's seven-object sealing task: the sealing task may address
authority for inputs such as `rho_pre`, effects/domains, quotient/measure,
raw-map, B0, and primitive inventory. It does not by itself create M1-M7.
Therefore the two workstreams meet, but they are not identical.

```text
what_invariant_needs_is_nothing = false | TYPE-R |
  test: MISSING-REQUIRED-FIELDS; M1-M7 are absent

missing_objects_equal_only_the_seven_used_as_primitive_seals = false | TYPE-R |
  test: REQUIREMENT-COMPARISON; the seven seals can support authority, but K0-K6
  also requires executed rows, traces, replay, graph, coherence, certificate,
  verdict owners, and hostile fixtures
```

## 6. Q-92 Construction Status

Under Q-92, the invariant cannot be constructed over Q41/Q42/Q43 in this relay.
Condition (c) fails: the prerequisites for a concrete invariant instance do not
exist. Conditions (e) and (f) also cannot be satisfied for the actual instance
because no dedicated instance validator or submitted hostile fixtures exist.

```text
ValidatedFlatCoReferenceInvariant_over_Q41_Q42_Q43_constructed = false | TYPE-C |
  constraint: prerequisite FlatObj0CoReferenceRecord_0 instance, port rows,
  traces, replay record, graph, certificate, validator, and hostile fixtures do
  not exist
  release: M1-M7 exist and Q-92(e,f) are satisfied by dedicated owners and
  failed adversarial reassembly controls

road_step_completed = false | TYPE-C |
  constraint: no concrete K0-K6 invariant instance exists over the three
  structures
  release: construct and validate the K0-K6 record over actual P1-P7 rows

road_step_advanced = true [PROCESS RESULT]
```

## 7. Five Answers

1. K0-K6 requires exactly the clauses quoted in Section 2: one `(o,r,g)` root,
   seven port/result trace pairs, trace validation, replay, direction-bearing
   graph, context split, and aggregate independent validation.
2. Clause-by-clause over Q41/Q42/Q43: K0 fails, K1 fails, K2 is `NO_VERDICT`
   because no traces exist, K3 fails, K4 fails, K5 holds narrowly as an
   `S_sector`/`I_prim` split, and K6 fails. The total invariant does not hold.
3. The invariant does not defeat independent-origin reassembly on these
   structures because the invariant instance is absent.
4. The invariant still needs M1-M7 above. This overlaps Codex 2's sealing task
   but is larger than it.
5. No Q-92 construction of the concrete invariant is authorized by prerequisites:
   condition (c) fails, and instance-level (e)/(f) are unavailable.

Protected status:

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

