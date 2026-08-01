# Stage 8 Canonical Patch-Cover to Incidence-Graph Functor Attempt v001

Date: 2026-08-01

## Scope and fences

This artifact responds to Paste 261. It attempts the named obstruction under
Target 2:

```text
CANONICAL_PATCH_COVER_TO_INCIDENCE_GRAPH_FUNCTOR
```

No coupling, scale, root, eigenvalue, beta function, `E_R`, `T_R`, `k_R`,
`kappa_record`, `kappa_Thomson`, or `alpha` is computed or compared to any
measured constant. The Misner-Sharp / Brown-York fork is not resolved.
`a32_holdout/custodian_private/` was not opened.

## Lead verdict

The nerve construction gives a **candidate data map per chosen cover**, but it
does **not** build the canonical functor the program needs.

The obstruction is the cover selector and refinement law:

```text
CANONICAL_PATCH_COVER_TO_INCIDENCE_GRAPH_FUNCTOR_BUILT = false | TYPE-U |
would-build: a target-independent distinguished-cover selector, or an
equivalent theorem proving that the PRPS/LPRB cover nerve is canonically the
Gate-2/Gate-4 rooted incidence graph, independent of cover, lift, path
representative, ordering, and refinement.

NERVE_ONE_SKELETON_CANDIDATE_PER_COVER = true | IMPORTED_GENERAL_TOPOLOGY |
scope: given a fixed indexed cover, its Cech nerve has vertices = patches and
edges = nonempty pairwise overlaps; transition functions form U(1)-valued
1-cochain data.

NERVE_CANDIDATE_TRANSFERS_CANONICALLY_TO_THIS_STRUCTURE = false | TYPE-U |
would-build: a proof that the imported Cech/nerve construction applies to
the PRPS endpoint-comparison patches and lands in the fixed Gate-4 incidence
graph without introducing a nonsealed choice of cover, lift, path
representative, ordering, or refinement.
```

This is not a refutation of localization or of Cech/nerve mathematics. It is
an unbuilt realization theorem. Under the anti-deflation clause, this remains
`TYPE-U`, not `TYPE-R`.

## Domain from sealed text

The PRPS side is a smooth record-side localization problem.

`PRIMITIVE_RELATIVE_PHASE_STABILIZER_V002.md:93-115` states that its result is
pointwise and does not imply that the relative active stabilizer may vary
independently at every surface point. It requires a later target-independent
theorem to establish:

```text
the endpoint comparison frame is local;
independent smooth relative-frame changes are physically redundant;
comparison data must be transported between overlapping patches;
```

Only then is a connection with `D = d - i a` and `a -> a + d theta` required.
The same block says those premises are not established by the current sealed
sources and that the document neither introduces `a` as a physical field nor
identifies it with electromagnetism. Its executable-role block at
`PRIMITIVE_RELATIVE_PHASE_STABILIZER_V002.md:143-147` says the companion audit
does not test or certify the physical premises needed for localization.

`LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md:16-43` supplies local patches `U_i`,
normalized lifts `z_i : U_i -> C^2`, overlap transition functions
`z_j = g_ij z_i`, `g_ij = exp(i theta_ij) in U(1)`, and the triple-overlap
cocycle `g_ij g_jk g_ki = 1`. It says the local lifts and transition
functions define a complex line bundle / principal `U(1)` comparison bundle,
as local representative redundancy of the adopted projective record field.

`LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md:45-79` supplies the local patching
calculation for a connection: ordinary derivatives do not patch, while local
one-forms `a_i` make `D_i = d - i a_i` patch covariantly exactly when
`a_j = a_i + d theta_ij`.

This smooth side is record-side but not derived physical public
electromagnetism. `FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md:5-20`
says v001 mixed a derived pointwise stabilizer with a smooth local charged
connection, and that `LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md` remains
provenance but not authority for a physical charged connection.
`FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md:47-60` says the smooth
principal `U(1)_rel` bundle and auxiliary compact connection are adopted
Level-1 field content, not derived from the common phase of a projective lift,
passive basis rephasing, the demand to reproduce electromagnetism, or the
measured value of alpha. Its authorization block at
`FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md:159-174` records
`physical_public_EM_connection_derived = false`.

The sector typing has already been separated from the external response
sector. `STAGE8_ONE_SEAM_OR_THREE_SEAMS_ADJUDICATION_V001.md:171-203` records
this as:

```text
SMOOTH_RECORD_SIDE_NONEXTERNAL
```

because LPRB's patches, overlap transitions, and connection one-forms are
record-side smooth machinery, not the external source-field CTP response
sector.

## Codomain from sealed text

The Gate side is a discrete incidence-gauge structure.

`MB Work/alpha-program-archive/cleanroom_output/39_GATE2_FIRST_OPENING_SPEC_V001.md:12-23`
sets the Gate-2 first-opening problem over connected simple rooted
1-complexes with three independent root-incident comparison directions.
Its predictions at lines 24-48 say the minimal complex is `K_1,3`, with
`dim C_0 = 4`, `dim C_1 = 3`, rank-three incidence, and tree kernel zero,
while carrying the conditionality of the three-axis layer, first-minimal
reading, and root-incidence premise.

`MB Work/alpha-program-archive/cleanroom_output/41_GATE2_FIRST_OPENING_RESULT_V001.md:6-19`
records the result: the minimal complex hosting three independent
root-incident comparison directions is `K_1,3`, uniquely up to isomorphism,
with the exact first-opening accounting. Its status block at lines 27-47 says
that, within the declared conditionality stack, Gate 1 forces `U(1)`, Gate 2
forces `K_1,3`, Gate 3 forces identity fibers and canonical `B_rho`, and
Gate 4 forces unit-weight covariant transport with holonomy the sole freedom.

`MB Work/alpha-program-archive/cleanroom_output/30_GATE4_DIFFERENTIAL_UNIQUENESS_SPEC_V001.md:12-33`
specifies Gate 4's differential family: per-edge operators
`D_(a_e,b_e)`, positive-definite forms, residual phases, orientation
bookkeeping, and per-vertex `U(1)` rephasing. Lines 35-60 predict that
interior closure and one-record normalization force the unique class:
unit-weight covariant incidence modulo gauge, with residual phases only on
loops.

`MB Work/alpha-program-archive/cleanroom_output/32_GATE4_DIFFERENTIAL_UNIQUENESS_RESULT_V001.md:9-31`
confirms the theorem over the enumerated family: closure forces constant
`a=b`, normalization forces unit modulus, vertex rephasing removes tree
phases, loop holonomy survives, and forms cannot reopen the family.
Its scope block at lines 46-55 says the theorem reaches only the enumerated
differential family.

`MB Work/alpha-program-archive/cleanroom_output/44_GATE4_COVECTOR_RAY_RESULT_V001.md:6-17`
confirms the other Gate-4 half: over the canonical first-opening object,
gauge invariance, no-output-without-record, leaf naturality, and positivity
force exactly one registration-counting covector ray. Lines 30-35 summarize
the net kinematic result as a canonical compact `U(1)` gauge structure on the
rooted three-star with unique registration-counting readout.

## Is it a functor as sealed?

As sealed, the word "functor" is stronger than the specified data.

On the PRPS/LPRB side, the text supplies patches, overlaps, transition
functions, and a cocycle. It does not define a cover category, Cech groupoid,
nerve category, morphisms of covers, or refinement category. Those structures
can be imported from standard topology, but they are not themselves sealed
objects in PRPS or LPRB.

On the Gate side, the text supplies a rooted graph / chain complex, edge
operators, composable-path closure, universal-edge isomorphisms, and vertex
gauge maps. A path category can be imported from a directed graph, but the
Gate artifacts do not state the missing object as a functor from a Cech
category to a path category. They classify incidence data over the enumerated
Gate family.

Therefore the current build target is, as sealed, a candidate **data map**.
It becomes a functor only after additional category data are declared:

```text
PATCH_COVER_TO_INCIDENCE_GRAPH_FUNCTOR_AS_SEALED = false | TYPE-U |
would-build: a sealed source category of PRPS/LPRB covers, overlaps, frame
changes, and refinements; a sealed target category of Gate incidence graphs,
oriented edges, vertex-gauge maps, and graph/refinement morphisms; and a
mapping preserving objects, morphisms, composition, and identities.

PATCH_COVER_TO_INCIDENCE_GRAPH_DATA_MAP_PER_FIXED_COVER = true |
IMPORTED_CONDITIONAL |
condition: a fixed indexed cover and chosen overlap-to-edge realization are
supplied before the map is formed.
```

This is not a vocabulary objection. A functor would carry morphisms and
composition; a data map only assigns one chosen cover to one graph-like
object.

## Candidate: the 1-skeleton of the nerve

The imported candidate is standard:

```text
Given an indexed cover {U_i}:
  vertices: one vertex v_i for each patch U_i;
  edges: one edge e_ij for each nonempty pairwise overlap U_i cap U_j;
  opposite edge: e_ji for the reverse orientation;
  edge data: transition function g_ij on U_i cap U_j;
  vertex-gauge data: lift changes h_i on U_i act by
       g_ij -> h_j g_ij h_i^(-1)
  cocycle: g_ij g_jk g_ki = 1 on triple overlaps.
```

This has the same **shape** as Gate 4's vertex/edge/gauge data. It does not
yet have the same **type**:

```text
LPRB edge data: smooth transition functions on overlaps.
Gate-4 edge data: incidence-edge transports/fiber maps in a finite rooted
                  graph / chain complex.
```

To make them equal, the corpus would have to supply a way to reduce overlap
functions to the Gate edge transports or to prove that Gate-4 edge transports
are precisely the Cech transition functions. The current sealed corpus does
not supply that theorem.

## Does the record structure select a distinguished cover?

### Record cell as selector

The record cell does not select the needed cover in the current sealed text.

LPRB says one primitive record degree is placed on every admissible causal
record cell and then works on local patches `U_i`. It does not define a
distinguished cover of the endpoint-comparison domain, a good-cover
condition, a nerve, or a canonical overlap graph.

```text
record_cell_selects_distinguished_PRPS_cover = false | TYPE-U |
would-build: a theorem assigning to each admissible causal record cell a
canonical endpoint-comparison cover with specified overlaps and transition
domains, independent of nonsealed patch choices.
```

### First-opening incidence structure as selector

The first-opening incidence structure selects the Gate-side graph, not a
PRPS-side cover.

Gate 2 derives `K_1,3` from minimality and root-incidence over rooted
1-complexes. It does not identify the root and leaves with local patches of a
smooth endpoint-comparison cover, and it does not state that `K_1,3` is the
nerve of any such cover.

```text
first_opening_graph_selects_PRPS_cover = false | TYPE-R |
test: Gate-2 cleanroom_output specs/results quantify over rooted graphs and
incidence directions; their variables are vertices, edges, root choice and
graph isomorphism, not patches, open sets, cover morphisms or overlaps.

Gate4_graph_is_sealed_as_nerve_of_PRPS_cover = false | TYPE-S |
roots: listed in Search record |
query: nerve, Cech, cover, patch, overlap, patch-incidence, incidence-cover |
reason: no sealed artifact states that the Gate-2/Gate-4 graph is the nerve
of a PRPS/LPRB cover.
```

The first-opening graph and the nerve graph may be isomorphic after choosing
a cover with one central patch overlapping three leaves and no leaf-leaf
overlaps. That construction is not canonical unless the cover is selected
beforehand by sealed structure.

## Five independence checks

### 1. Cover

The cover check fails as a canonical construction.

A nerve is one graph per cover. LPRB does not select a cover, and Gate 2
selects a graph without selecting any cover whose nerve realizes it. Different
covers of the same local domain can have different nerves, and the standard
way to compare them is a refinement or Cech-colimit construction, not a
single fixed finite Gate graph.

```text
cover_independence_proved = false | TYPE-U |
would-build: either a distinguished-cover selector, or a proof that all
admissible PRPS/LPRB covers produce canonically equivalent Gate-4 incidence
data without changing the fixed `K_1,3` target.
```

### 2. Lift

The lift check has a formal match but not a sealed discharge.

At the Cech level, changing local lifts by `h_i` changes transitions by
`g_ij -> h_j g_ij h_i^(-1)`, which is formally the same law as Gate-4 vertex
rephasing. But LPRB's `h_i` are smooth patch functions, while Gate 4's vertex
gauge maps act on finite vertex fibers. The corpus does not seal the
reduction from smooth patch functions to Gate vertex maps, nor prove that all
smooth relative-frame changes are exhausted by Gate-4 vertex rephasing.

```text
lift_independence_formally_matches_vertex_gauge = true | IMPORTED_CONDITIONAL

lift_independence_proved_for_PRPS_to_Gate4 = false | TYPE-U |
would-build: a smooth-frame-to-vertex-gauge theorem proving that lift changes
on PRPS patches descend exactly to Gate-4 vertex gauge maps and leave no
additional physical comparison data.
```

### 3. Path representative

The path-representative check fails as a sealed construction.

The nerve of a cover gives overlaps. Gate 4 classifies incidence-edge
transports. If one reads the overlap transition functions as edge data, then
the data are still functions on overlaps, not selected finite edge transports.
If one instead uses parallel transport, then a path representative or
equivalent edge realization must be selected. The current corpus supplies
neither.

```text
path_representative_independence_proved = false | TYPE-U |
would-build: an overlap-to-edge-transport theorem proving either that no path
choice is needed because Gate-4 edge data are literally the transition
functions, or that path choices inside overlaps give canonically equivalent
Gate-4 edge transports.
```

### 4. Ordering

The ordering check fails as a canonical construction.

The Cech nerve of an indexed cover can be oriented by ordered pairs or by a
chosen total order on indices. Gate 4 has orientation bookkeeping and can
handle opposite edges, but it does not choose an ordering of patches, nor a
canonical assignment of PRPS patches to the rooted-star root and leaves. A
chosen ordering may be harmless after a proof of label-preserving
isomorphism/gauge invariance, but that proof is not sealed for the PRPS cover
realization.

```text
ordering_independence_proved = false | TYPE-U |
would-build: a theorem proving that every admissible indexing/orientation of
the PRPS cover nerve lands in the same Gate-4 equivalence class, including a
canonical rooted-star isomorphism or an explicit proof that the root/leaf
assignment is physically redundant.
```

### 5. Refinement

The refinement check fails for the fixed finite Gate graph.

Standard cover theory obtains cover independence by passing through
refinements or a Cech colimit over good covers. Gate 4's object is a fixed
finite first-opening graph, and Gate 2 derives `K_1,3` as a minimal rooted
1-complex, not as a refinement colimit. A refinement of a cover generally
changes the nerve's vertex/edge count and can introduce additional
intersections. That does not canonically remain the same fixed Gate graph
without a refinement-collapse theorem.

```text
refinement_independence_proved = false | TYPE-U |
would-build: a refinement-collapse theorem from PRPS cover nerves to the
fixed Gate-2/Gate-4 rooted-star incidence class, or a revised target in which
Gate-4 is lifted from a fixed finite graph to a refinement-colimit object.
```

## What would build it

The smallest sufficient route is not a new connection theorem. It is a cover
realization theorem:

```text
DISTINGUISHED_PRPS_COVER_SELECTOR = missing | TYPE-U |
would-build: canonical patches for the endpoint-comparison frame on each
admissible record cell.

NERVE_REALIZES_GATE4_K13 = missing | TYPE-U |
would-build: proof that the selected cover's 1-nerve is canonically the
rooted `K_1,3` first-opening incidence graph, with root/leaf assignment and
orientation handled without hidden choices.

CECH_TRANSITION_TO_GATE4_EDGE_DATA = missing | TYPE-U |
would-build: proof that LPRB transition functions / overlap comparison data
map to Gate-4 edge transports, and that smooth lift changes map exactly to
Gate-4 vertex gauge maps.

REFINEMENT_INDEPENDENCE_OR_COLLAPSE = missing | TYPE-U |
would-build: proof that changing cover, lift, path representative, ordering,
or refinement does not change the resulting Gate-4 equivalence class.
```

If all four were supplied, the imported nerve construction would become
available to Target 2. Without them, the candidate depends on a nonsealed
choice of cover and does not discharge PRPS.

## Status block

```text
canonical_patch_cover_to_incidence_graph_functor_built = false | TYPE-U
nerve_candidate_per_chosen_cover_available = true | IMPORTED_CONDITIONAL
functor_name_as_sealed_object = aspirational | TYPE-U
record_cell_selects_distinguished_cover = false | TYPE-U
first_opening_graph_selects_cover = false | TYPE-R
cover_independence_proved = false | TYPE-U
lift_independence_proved = false | TYPE-U
path_representative_independence_proved = false | TYPE-U
ordering_independence_proved = false | TYPE-U
refinement_independence_proved = false | TYPE-U
TARGET_2_STATUS = BLOCKED_BY_TYPE_U_COVER_REALIZATION_THEOREM
physical_public_EM_connection_derived = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```

## Search record

Roots entered:

```text
/Users/bgm/.codex/attachments/0b196f6b-1dcf-457b-ac00-d880490c1f06/pasted-text.txt
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/stage8_execution/t0_lineage/core_scripts
/Users/bgm/MB Work/alpha-program-archive/cleanroom_output
/Users/bgm/Documents/New project/_external_handoffs/fable_alpha_cleanroom
```

The archive `cleanroom_output/` root contained 87 files at read time and was
entered directly. `a32_holdout/custodian_private/` was not entered. No git
command was run.

Queries and methods:

```text
find /Users/bgm/MB Work/alpha-program-archive/cleanroom_output -maxdepth 2 -type f
rg over cleanroom_output for Gate 1/2/3/4, comparison group, first-opening,
  differential uniqueness, covector, vertex, edge, gauge, nerve, Cech, cover,
  patch, overlap, functor, incidence
rg over cleanroom, archive cleanroom_output, and external handoff roots for:
  nerve, Cech, good cover, cover independence, refinement colimit,
  patch-incidence, incidence-cover, patch-Gate, Gate-patch, overlap-Gate,
  Gate-overlap
targeted reads of PRPS, LPRB, FBRAP v002, Gate 1-4 cleanroom_output files,
  and prior Target-2 / one-seam artifacts
```

The search found the Gate-2/Gate-4 fixed finite rooted-star / incidence-gauge
structure and the LPRB local-patch / overlap-transition structure. It found no
sealed cover selector, no sealed claim that the Gate graph is the nerve of the
PRPS cover, and no sealed refinement-collapse theorem from cover nerves to
the fixed Gate-4 incidence class.

