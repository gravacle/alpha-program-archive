# Stage 8 PRPS Cover Nerve K1,3 Realization Test v001

Date: 2026-08-01

## Scope and fences

This artifact responds to Paste 263. It tests whether a PRPS
endpoint-comparison cover can realize Gate 2's rooted star `K_1,3` as its
nerve, and whether the good-cover nerve theorem can be applied to the PRPS
domain.

No coupling, scale, root value, eigenvalue, beta function, `E_R`, `T_R`,
`k_R`, `kappa_record`, `kappa_Thomson`, or `alpha` is computed or compared to
any measured constant. No phase, holonomy value, or angle is evaluated. The
Misner-Sharp / Brown-York fork is not resolved. `a32_holdout/custodian_private/`
was not opened.

## Lead verdict

The nerve route is **not refuted** by this test, but it is also **not
realized** by sealed PRPS text.

The corpus does not define an actual PRPS cover whose nerve can be checked
against `K_1,3`; it defines local patches and overlap transitions
schematically. Therefore the answer to "is the PRPS cover's nerve `K_1,3`?"
is not a physical no-go. It is unbuilt.

The good-cover / contractibility chain is presently void: the corpus does not
establish that the PRPS cover is good, that its nerve is `K_1,3`, or that the
underlying endpoint-comparison domain is covered by such a good cover.

```text
PRPS_COVER_NERVE_REALIZES_GATE2_K13 = false | TYPE-U |
would-build: an actual PRPS endpoint-comparison cover with four patches,
one distinguished central patch meeting three leaf patches, leaf patches
pairwise disjoint, and a proof that this cover is selected by PRPS/record
structure rather than drawn to match Gate 2.

K13_NERVE_ROUTE_REFUTED = false | NO_VERDICT |
reason: no sealed PRPS cover/domain is specified strongly enough to prove
non-realizability.

GOOD_COVER_HOMOTOPY_CONCLUSION_AVAILABLE = false | TYPE-U |
would-build: good-cover hypotheses for the PRPS endpoint-comparison domain
plus a proof that the selected cover's nerve is `K_1,3`.
```

## Source: PRPS/LPRB cover data

`PRIMITIVE_RELATIVE_PHASE_STABILIZER_V002.md:93-115` says the pointwise result
does not imply that the relative active stabilizer may vary independently at
every surface point. It requires a later target-independent theorem to
establish:

```text
the endpoint comparison frame is local;
independent smooth relative-frame changes are physically redundant;
comparison data must be transported between overlapping patches;
```

Only then is a connection with `D = d - i a` and `a -> a + d theta` required.
The same block says those premises are not established by current sealed
sources and that PRPS neither introduces `a` as a physical field nor
identifies it with electromagnetism. Its executable-role block at
`PRIMITIVE_RELATIVE_PHASE_STABILIZER_V002.md:143-147` says the companion audit
does not certify the physical premises needed for localization.

`LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md:16-43` supplies the closest cover
data. It says that on a local patch `U_i` one chooses a normalized lift
`z_i : U_i -> C^2`; on overlaps, `z_j = g_ij z_i` with
`g_ij = exp(i theta_ij) in U(1)`; and on triple overlaps,
`g_ij g_jk g_ki = 1`. The local lifts and transition functions define a
complex line bundle / principal `U(1)` comparison bundle.

`LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md:45-79` supplies a patching calculation
for local one-forms `a_i`: derivatives patch covariantly when
`a_j = a_i + d theta_ij`.

Those lines do **not** specify:

```text
the number of patches;
the endpoint-comparison domain being covered;
which intersections are nonempty;
whether leaf-leaf intersections are empty;
whether all nonempty finite intersections are contractible;
a distinguished central patch;
a root/leaf assignment;
or an orientation on the cover nerve.
```

`FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md:5-20` also says LPRB
remains provenance but not authority for a physical charged connection, and
`FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md:47-60` types the smooth
principal `U(1)_rel` bundle and auxiliary compact connection as adopted
Level-1 field content, not derived from the common phase of a projective lift,
passive basis rephasing, electromagnetism, or measured alpha.

## Source: Gate 2 / Gate 4 target graph

`MB Work/alpha-program-archive/cleanroom_output/39_GATE2_FIRST_OPENING_SPEC_V001.md:12-23`
sets the Gate-2 problem over connected simple rooted `1`-complexes with
three independent root-incident comparison directions. Lines 24-48 predict
that, among all connected simple rooted `1`-complexes hosting those
directions, the minimal one is `K_1,3`, uniquely up to isomorphism, with
three root-incident edges.

`MB Work/alpha-program-archive/cleanroom_output/41_GATE2_FIRST_OPENING_RESULT_V001.md:6-19`
confirms the result: exhaustive enumeration finds the minimal complex hosting
three independent root-incident comparison directions is `K_1,3`, uniquely
up to isomorphism, with exact accounting.

`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:248-274` states the first-
opening premise directly: three independent public action handles, one
unresolved pre-record alternative, all primitive first-opening arrows begin
at the unresolved root, and no endpoint, arrow, loop, or composite cell
exists at first order without an additional public distinction or
composition. It says this fixes the minimal first-opening `1`-complex to the
rooted star `K_(1,r)` with `r=3`.

`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:276-330` then types the
record-complex object as a finite oriented regular CW complex with a
distinguished root, one-dimensional Hermitian fibers on vertices, and unitary
transport on oriented edges. It also states that one chooses orientation
representatives for unoriented edges and faces.

`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:515-552` gives the local
first-incidence family and orientation-extension law. It explicitly says
orientation is bookkeeping, not an additional physical handle.

Thus the target graph is rooted and directed/incidence-oriented. A plain
cover nerve is not.

## Combinatorial condition

For a cover's nerve `1`-skeleton to be isomorphic as an **unrooted
undirected graph** to `K_1,3`, it must have four patches:

```text
U_0 intersects U_1, U_2, U_3;
U_1 cap U_2 = empty;
U_1 cap U_3 = empty;
U_2 cap U_3 = empty.
```

If the cover is also good, every nonempty patch and nonempty central-leaf
intersection must be contractible; there are no nonempty leaf-leaf or triple
intersections under the star pattern.

This condition is satisfiable by some covers of some spaces in imported
topology. That is not the question here. The question is whether PRPS/LPRB
itself supplies such a cover on its own endpoint-comparison domain.

It does not.

```text
K13_STAR_PATTERN_SATISFIABLE_BY_SOME_COVER = true | IMPORTED_GENERAL_TOPOLOGY

K13_STAR_PATTERN_SUPPLIED_BY_PRPS_COVER = false | TYPE-U |
would-build: a PRPS theorem specifying four endpoint-comparison patches with
exactly the star overlap pattern.
```

## Root and leaf assignment

The centre of a star-shaped nerve would be combinatorially unique **after**
one has already supplied a cover whose nerve is a star. That does not make
the assignment to the unresolved root canonical in the sealed PRPS cover
data.

PRPS/LPRB have patch labels `U_i`, local lifts, and overlap transitions. They
do not mark a patch as "unresolved root", and they do not assign the three
other patches to public endpoint alternatives. Gate 2 has a distinguished
root and three root-incident directions, but that is Gate-side structure, not
a PRPS cover selector.

```text
root_patch_assignment_forced_by_PRPS = false | TYPE-U |
would-build: a theorem identifying one PRPS endpoint-comparison patch with
the unresolved root and the remaining three patches with first-public
endpoint alternatives before looking at the Gate-2 graph.

root_patch_assignment_available_after_chosen_star_cover = true |
IMPORTED_CONDITIONAL |
condition: if a chosen cover already has star nerve, the degree-three vertex
of the nerve is graph-theoretically distinguished; this is not a PRPS-derived
cover selector.
```

## Orientation

A nerve `1`-skeleton is undirected. It can be turned into a directed graph by
passing to ordered pairs or oriented `1`-simplices, and transition functions
come with an ordered notation `g_ij`. But that is imported nerve/Cech
bookkeeping, not the Gate-2 first-opening orientation.

Gate-side orientation is stronger: all primitive first-opening arrows begin
at the unresolved root (`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:254-260`),
and Gate 4 has an orientation-extension law for reversed representatives
(`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:529-552`).

No sealed text derives that root-to-leaf orientation from PRPS cover data.

```text
nerve_orientation_supplied_by_PRPS = false | TYPE-U |
would-build: an orientation theorem assigning ordered overlaps to the Gate
root-to-leaf incidence directions, with orientation reversal matching the
Gate-4 extension law.

orientation_can_be_added_to_a_chosen_nerve = true | IMPORTED_CONDITIONAL |
condition: choose an ordering or orient edges away from the chosen central
patch; this is construction data unless PRPS supplies it.
```

## Good-cover and homotopy chain

The standard imported theorem is conditional:

```text
If a cover is good, then the nerve is homotopy equivalent to the covered
space.
```

Applying it here would require all of:

```text
1. a PRPS endpoint-comparison domain;
2. a selected cover of that domain;
3. proof that the cover is good;
4. proof that its nerve is `K_1,3`;
5. proof that this is the cover used by the localization bridge.
```

The sealed corpus supplies none of those in sufficient form.

```text
PRPS_good_cover_hypothesis_established = false | TYPE-U |
would-build: proof that the selected PRPS endpoint-comparison cover has
contractible nonempty finite intersections.

PRPS_domain_contractible_from_nerve = false | TYPE-U |
would-build: PRPS good-cover theorem application with selected nerve
`K_1,3`.

if_good_PRPS_cover_has_nerve_K13_then_domain_contractible = true |
IMPORTED_CONDITIONAL |
condition: standard nerve theorem plus the fact that `K_1,3` is a tree and
hence contractible.
```

If that imported conditional were eventually discharged, the topological
principal-bundle consequence would also be conditional/imported:

```text
if_contractible_smooth_domain_then_principal_U1_bundle_topologically_trivial
  = true | IMPORTED_CONDITIONAL |
condition: ordinary smooth/paracompact principal-bundle classification.
```

But the consequence must be stated narrowly. Topological triviality of a
principal `U(1)` bundle does **not** by itself prove that a connection is
flat, that a local one-form vanishes, or that no later curvature/plaquette
carrier can exist. It says there is no nontrivial topological classifying
data on that contractible first-opening domain. That matches the Gate-side
tree intuition only at the first-opening transport/topology level.

```text
contractible_domain_would_force_connection_flat = false | TYPE-R |
test: imported differential geometry distinguishes topological triviality of
a principal bundle from flatness or vanishing curvature of a chosen connection.

contractible_domain_would_remove_topological_bundle_class = true |
IMPORTED_CONDITIONAL
```

## The three possible chain breaks

### 1. Cover not good

This is not established as a positive failure. The corpus does not define the
cover enough to decide goodness.

```text
PRPS_cover_is_not_good = NO_VERDICT |
reason: no selected PRPS cover is sealed.

PRPS_cover_good = false | TYPE-U |
would-build: selected cover plus contractibility of every nonempty finite
intersection.
```

### 2. Nerve not `K_1,3`

This is also not established as a positive failure. The corpus does not
define an actual PRPS cover nerve to compare to `K_1,3`.

```text
PRPS_cover_nerve_not_K13 = NO_VERDICT |
reason: no selected PRPS cover nerve is sealed.

PRPS_cover_nerve_K13 = false | TYPE-U |
would-build: selected cover plus proof of the four-patch star intersection
pattern.
```

### 3. Contractible but not trivial

At the level of topological principal `U(1)` bundles, the imported theorem
does not leave this as the live break, assuming the ordinary smooth-domain
hypotheses. The live caveat is different: trivial topological bundle does not
erase differential connection data.

```text
contractible_but_topologically_nontrivial_principal_U1_bundle =
  false | IMPORTED_CONDITIONAL |
condition: ordinary smooth/paracompact principal-bundle classification.

contractible_but_connection_data_still_possible =
  true | IMPORTED_CONDITIONAL |
condition: topological triviality does not imply flatness of a chosen
connection.
```

## Result for the nerve route

This relay does not kill the nerve route. It blocks its payoff.

The cheap-kill condition would have been:

```text
no PRPS endpoint-comparison cover can have nerve `K_1,3`.
```

The sealed corpus does not support that. It also does not support the
opposite.

The named remaining object is therefore:

```text
PRPS_GOOD_STAR_COVER_REALIZATION_THEOREM = missing | TYPE-U |
would-build: a target-independent theorem specifying the PRPS
endpoint-comparison domain and a good four-patch cover whose nerve is
canonically the Gate-2 rooted star `K_1,3`, with root/leaf assignment and
orientation derived rather than chosen.
```

Until that theorem is supplied, the cover selector and Cech transition map
remain premature. They are not refuted; they are blocked behind the
realization/goodness theorem.

## Status block

```text
K13_PRPS_NERVE_REALIZATION_PROVED = false | TYPE-U
K13_PRPS_NERVE_REALIZATION_REFUTED = false | NO_VERDICT
PRPS_GOOD_COVER_PROVED = false | TYPE-U
GOOD_COVER_HOMOTOPY_CHAIN_APPLIES = false | TYPE-U
ROOT_LEAF_ASSIGNMENT_FORCED_BY_PRPS = false | TYPE-U
ORIENTATION_FROM_PRPS_NERVE_DERIVED = false | TYPE-U
NERVE_ROUTE_CHEAPLY_KILLED = false | NO_VERDICT
TARGET_2_STATUS = BLOCKED_BY_TYPE_U_PRPS_GOOD_STAR_COVER_REALIZATION
physical_public_EM_connection_derived = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```

## Search record

Roots entered:

```text
/Users/bgm/.codex/attachments/eeceb67f-ed68-4956-a656-02959de90e70/pasted-text.txt
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha-program-archive/cleanroom_output
/Users/bgm/Documents/New project/_external_handoffs/fable_alpha_cleanroom
```

The archive `cleanroom_output/` root was entered directly. `a32_holdout/custodian_private/`
was not entered. No git command was run.

Queries and methods:

```text
rg over cleanroom, archive cleanroom_output, and external handoff roots for:
  good cover, nerve theorem, homotopy equivalent, contractible,
  trivial principal, principal U(1) trivial, paracompact;
  cover, patch, overlap, U_i, g_ij, K_1,3, K₁,₃, rooted star,
  first-opening, root-incident, directed, orientation.

targeted reads of:
  PRIMITIVE_RELATIVE_PHASE_STABILIZER_V002.md;
  LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md;
  FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md;
  BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md;
  cleanroom_output Gate-2 spec/result;
  the prior Target-2 functor attempt.
```

The search found no sealed good-cover hypothesis, no sealed nerve theorem
application, no sealed claim that a PRPS cover has nerve `K_1,3`, and no
sealed claim that Gate 2's rooted directed star is a cover nerve.

