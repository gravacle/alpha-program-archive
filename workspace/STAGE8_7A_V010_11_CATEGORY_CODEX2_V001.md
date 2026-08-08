# Stage 8 / 7A Step 11 — V010-11 Decorated Category — Codex 2 v001

Date: 2026-08-08  
Lane: CODEX 2  
Scope: bounded derive-or-gap construction for `C-B-V010-11`

## 0. Pickup, custody, and pins

The relay input
`relay_inbox/RELAY_PASTE_745_V010_11_CATEGORY_CODEX2_V001.md` rehashed to
`ce08f6ba8b944054e534d524e189c6151a03a8801731f5917b85492aa9ca2818`;
its sidecar and CODEX 2 lane guard matched. `relay_outbox/745_ACK.md` was
written before task work. The requested report, package directory, and DONE
name were absent from the cleanroom, and the report and DONE names were absent
from the archive workspace. Only cleanroom bytes were written.

The builder verified these sealed inputs before reading their content:

| ID | Sealed input | SHA-256 | Use |
|---|---|---|---|
| `PACKET-V011` | `review_packets/STAGE7_QSPEC_CANDIDATE_V001/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` | `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` | category-bearing source |
| `BX-DELTA` | `STAGE8_7A_BOX_SCHEMA_DELTA_CODEX2_V001.json` | `b52e66b79787a55bad1553c05dfa8df52e7b11153879589d9627073a8e06bba9` | sealed BX13 schema |
| `SPEC-V012` | `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V012.md` | `382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504` | `C-B-V010-11` descriptor |
| `PRIOR-ENVELOPE` | `STAGE8_7A_ENVELOPE_C_B_V010_11_CODEX2_V001.json` | `06a1fb27cff9dc57639312f587bb13598a547de0c2ebb08b11256a9cdb28dd96` | prior `UNSTATEABLE` record |
| `CONSUMER` | `step11_tooling_family1/compile_carriers.py` | `e5ac5f578ae82bb0e89590bf7dc4528c599502e5e9f9a6c7597b5d6416f8fbac` | actual sealed BX13 consumer |
| `CONSUMER-CONTRACT` | `step11_tooling_family1/contracts/tooling_family1.schema.json` | `055e05ca59d04e6e4c3876dde50ac580b9033a11b9555cad81d2056fa1beaca7` | consumer manifest/result schemas |
| `TARGETS` | `step11_tooling_family1/targets.generated.json` | `477d038935d69ada049e570a693a3218e4c7bf2706330f8ae3888fe0cc56cdf6` | sealed target census |
| `PRIOR-SOURCES` | `step11_tooling_family1/sources.generated.json` | `7de7613410f9fec54223bec291f5b51a40071bc65975aac56c83c37fd534ccf2` | predecessor source manifest |

The V012 descriptor row is pinned at bytes `[57063,57309)` with digest
`9345948b5e6fb0d40e2e737f61d19b199b54926fb8121ec11790cf3ac8446a57`.
It requires a decorated-category schema and generator list, then types the
objects, first-opening subsets, M/Q/G labels, morphisms, identities, and
composition.

Jurisdiction is structural only. No member, physical quantity, target value,
fixed point, end test, proof authorization, or measured constant is selected
or evaluated.

## 1. Meaning probe and sealed derivation

The prior envelope searched a provenance serialization and correctly found no
closed instance there. The category-bearing packet itself contains the missing
constructive bytes. The builder consumed these exact half-open spans:

| Block | Packet span | Span SHA-256 | Structural content consumed |
|---|---:|---|---|
| `ENDPOINT_NAMES` | `[7823,8532)` | `748dea6a96a1349c1874dc02b4d6b99c8a941679bbd8398dcb128aba964f391d` | separates the endpoint carrier and names `p_h`, `h in {M,Q,G}` |
| `FIRST_OPENING_STAR` | `[12070,13010)` | `039d0392eaeee955b254f839a95fb6ab8174df54350dfcd5d5505e3c038a83f0` | fixes the minimal first-opening complex to the rooted three-arm star |
| `BARE_CATEGORY_LAWS` | `[13010,15548)` | `1ee369d497db0cb16c9e63ed60ab24f519ff537362ce30fdd49c1f3920b8588e` | types morphisms, identity, composition, and structural associativity |
| `DECORATED_CATEGORY_LAWS` | `[15667,16969)` | `6980c6747a4c198402af41ec5010a0f322036a7cc5e5327b7e9191143a66af88` | defines `FO`, `lambda:FO->{M,Q,G}`, reflection, and label preservation |
| `CANONICAL_CELL_INCLUSIONS` | `[16969,18374)` | `558f381349919ab28a3bdb0418d1abba69a65182d0afff62b522e29ff4fd62e1` | gives inherited decoration on `bar(c)` and canonical `j_c:bar(c)->K` |

These spans determine a canonical bounded carrier: the subcategory generated
by **all three** first-opening closed-edge inclusions of the sealed minimal
star. It is not an identities-only or hand-selected favorable subcategory.
The three labeled first-opening edges are the entire label-bearing first-order
cell census of that star. Closing those generators under identities and every
defined composition gives a finite, non-vacuous BX13 instance.

## 2. Closed instance elements

### 2.1 Objects

| Object ID | First-opening edges | M/Q/G labels | Sealed construction |
|---|---|---|---|
| `K_STAR_MQG` | `e_M,e_Q,e_G` | `M,Q,G` | minimal rooted three-arm first-opening star |
| `BAR_E_M` | `e_M` | `M` | inherited closed-cell object `bar(e_M)` |
| `BAR_E_Q` | `e_Q` | `Q` | inherited closed-cell object `bar(e_Q)` |
| `BAR_E_G` | `e_G` | `G` | inherited closed-cell object `bar(e_G)` |

The ordered edge/label arrays encode the sealed map
`lambda(e_M)=M`, `lambda(e_Q)=Q`, `lambda(e_G)=G`. No unlabeled vertex cell
was given a fabricated label.

### 2.2 Morphisms and generators

| Morphism ID | Source | Target | First-opening/label carrier | Role |
|---|---|---|---|---|
| `id_K_STAR_MQG` | `K_STAR_MQG` | `K_STAR_MQG` | `e_M/M,e_Q/Q,e_G/G` | identity |
| `id_BAR_E_M` | `BAR_E_M` | `BAR_E_M` | `e_M/M` | identity |
| `id_BAR_E_Q` | `BAR_E_Q` | `BAR_E_Q` | `e_Q/Q` | identity |
| `id_BAR_E_G` | `BAR_E_G` | `BAR_E_G` | `e_G/G` | identity |
| `j_M` | `BAR_E_M` | `K_STAR_MQG` | `e_M/M` | canonical cell inclusion; generator |
| `j_Q` | `BAR_E_Q` | `K_STAR_MQG` | `e_Q/Q` | canonical cell inclusion; generator |
| `j_G` | `BAR_E_G` | `K_STAR_MQG` | `e_G/G` | canonical cell inclusion; generator |

The exact generator list is `[j_M,j_Q,j_G]`. It is all and only the
non-identity morphism census. Every morphism reproduces its domain's complete
first-opening/label pairs, and each pair occurs in its target. Thus the
sealed first-opening reflection and label-preservation conditions both type.

### 2.3 Complete composition table

The convention is `left compose right = result`.

| Left | Right | Result |
|---|---|---|
| `id_BAR_E_G` | `id_BAR_E_G` | `id_BAR_E_G` |
| `id_BAR_E_M` | `id_BAR_E_M` | `id_BAR_E_M` |
| `id_BAR_E_Q` | `id_BAR_E_Q` | `id_BAR_E_Q` |
| `id_K_STAR_MQG` | `id_K_STAR_MQG` | `id_K_STAR_MQG` |
| `id_K_STAR_MQG` | `j_G` | `j_G` |
| `id_K_STAR_MQG` | `j_M` | `j_M` |
| `id_K_STAR_MQG` | `j_Q` | `j_Q` |
| `j_G` | `id_BAR_E_G` | `j_G` |
| `j_M` | `id_BAR_E_M` | `j_M` |
| `j_Q` | `id_BAR_E_Q` | `j_Q` |

There are exactly ten composable ordered pairs among the seven morphisms; the
table has ten entries. The compiler generated the pair census from domains
and codomains and required exact equality with the supplied table, so no
defined composite is omitted.

## 3. Exact category-law proofs

### 3.1 Both identity laws

For each `f`, the second and third columns are respectively
`id_target compose f` and `f compose id_source`.

| `f` | Left-identity result | Right-identity result | Check |
|---|---|---|---|
| `id_K_STAR_MQG` | `id_K_STAR_MQG` | `id_K_STAR_MQG` | PASS |
| `id_BAR_E_M` | `id_BAR_E_M` | `id_BAR_E_M` | PASS |
| `id_BAR_E_Q` | `id_BAR_E_Q` | `id_BAR_E_Q` | PASS |
| `id_BAR_E_G` | `id_BAR_E_G` | `id_BAR_E_G` | PASS |
| `j_M` | `j_M` | `j_M` | PASS |
| `j_Q` | `j_Q` | `j_Q` | PASS |
| `j_G` | `j_G` | `j_G` | PASS |

### 3.2 Exhaustive associativity

For each composable triple `(left,middle,right)`, the fourth column is
`left compose (middle compose right)` and the fifth is
`(left compose middle) compose right`.

| Left | Middle | Right | Left-associated result | Right-associated result | Check |
|---|---|---|---|---|---|
| `id_K_STAR_MQG` | `id_K_STAR_MQG` | `id_K_STAR_MQG` | `id_K_STAR_MQG` | `id_K_STAR_MQG` | PASS |
| `id_K_STAR_MQG` | `id_K_STAR_MQG` | `j_M` | `j_M` | `j_M` | PASS |
| `id_K_STAR_MQG` | `id_K_STAR_MQG` | `j_Q` | `j_Q` | `j_Q` | PASS |
| `id_K_STAR_MQG` | `id_K_STAR_MQG` | `j_G` | `j_G` | `j_G` | PASS |
| `id_K_STAR_MQG` | `j_M` | `id_BAR_E_M` | `j_M` | `j_M` | PASS |
| `id_K_STAR_MQG` | `j_Q` | `id_BAR_E_Q` | `j_Q` | `j_Q` | PASS |
| `id_K_STAR_MQG` | `j_G` | `id_BAR_E_G` | `j_G` | `j_G` | PASS |
| `id_BAR_E_M` | `id_BAR_E_M` | `id_BAR_E_M` | `id_BAR_E_M` | `id_BAR_E_M` | PASS |
| `id_BAR_E_Q` | `id_BAR_E_Q` | `id_BAR_E_Q` | `id_BAR_E_Q` | `id_BAR_E_Q` | PASS |
| `id_BAR_E_G` | `id_BAR_E_G` | `id_BAR_E_G` | `id_BAR_E_G` | `id_BAR_E_G` | PASS |
| `j_M` | `id_BAR_E_M` | `id_BAR_E_M` | `j_M` | `j_M` | PASS |
| `j_Q` | `id_BAR_E_Q` | `id_BAR_E_Q` | `j_Q` | `j_Q` | PASS |
| `j_G` | `id_BAR_E_G` | `id_BAR_E_G` | `j_G` | `j_G` | PASS |

The domain/codomain census contains exactly 13 composable triples. All 13 are
displayed above and rechecked from the ten-entry composition table. This is
an exact finite proof, consistent with the packet's structural proof that the
same laws follow from ordinary cellular/fiber-map composition.

## 4. Content addressing and actual-consumer compile

The package is `step11_v010_11_category/`. Its five element collections and
two principal generated objects are independently content-addressed:

| Generated object | SHA-256 |
|---|---|
| objects collection | `a9a7d758f1c3445c24944297ab27402adac09fe6df85735c5501430b5c00c138` |
| morphisms collection | `76a4cfb704e3222b75f7cd686318970916a80e729445c5945083f88928feb38d` |
| identities collection | `f99d902b98c62dae0cce694b323dc225ab4218f1c811cbad4b81136e0ee2a95f` |
| composition collection | `6a42f2d6a043fcc1222dbdf133099ff63ae2cf72bd4d3757ad4d47227ffbf397` |
| generator-ID collection | `28b7c99a38c0a2578a84d080ef9a19afb33e8aafffe07afad9faa60481533cc5` |
| complete BX13 instance | `664059f4b10f1b78b1e04f111b77adc556644378a741622603bfbba957aa2b2d` |
| exact law proof | `b5eaf8a24b3749784fb61a7c5d93153a0f639c12fba5311baef5e6dddb09e12f` |

The element manifest hashes to
`6ba68dcd88aff329e29e5ea7ca649b7d1d9f7c075414a23819e80cfc7c09c719`
and byte-compares each collection with its corresponding array in the BX13
instance. The BX13 schema was extracted directly from the sealed delta and
hashes to
`d7c283070669c546b87ff5185b2432cbfb641c917de618108c0fcddc2d0e1e58`.

The existing sealed `compile_carriers.py` consumer was executed with exactly
one source-manifest delta: `CS:C-B-V010-11:decorated-category` became available
at the content-addressed instance path. It independently:

1. validated the instance against the sealed BX13 schema;
2. rehashed every source and half-open span binding;
3. canonicalized the component;
4. reproduced the same component digest; and
5. returned target status `PRODUCED` and bounded row state
   `STATEABLE_COMPONENTS_PRESENT_ADMISSION_BARRED`.

The consumer compilation result hashes to
`f3ad4bc38c35fde773be59bfdccf98ef8456e5ea8387abe8b0802f8fa280bb22`.
The local combined outcome is
`PASS_INSTANCE_BUILT_AND_CONSUMER_COMPILED`, with law result
`PASS_EXACT_STRUCTURAL_CATEGORY_LAWS`. Neither string is an evaluator row
PASS or an admission claim.

## 5. Determination boundary

All seven fields required by BX13 are determined for the bounded carrier:
four objects, seven morphisms, four identities, ten composition entries, and
three generator IDs. There is no required-field gap in this carrier.

The sealed packet also defines an ambient `DecRec_2` category containing
arbitrary finite oriented regular CW complexes, Hermitian lines, and discrete
unitary connections. It does **not** select a finite census of those ambient
objects, concrete unit frames, coordinate scalars, connection representatives,
later composite cells, or two-cells. Those ambient extensions remain
underdetermined and are not claimed by this bounded instance. They are not
silently labeled or added:

- root and endpoint vertex closed-cell objects are not first-opening and do
  not inherit M/Q/G labels; BX13 requires a nonempty label array, so no label
  was fabricated for them;
- the minimal first-order star has no face object;
- concrete Hermitian-line coordinates and unitary scalars are deliberately
  absent from BX13 and from the emitted bytes.

Thus the determination claim is exact: the maximal sealed label-bearing
first-opening generator subcategory of the minimal star is built; exhaustion
of the ambient `DecRec_2` universe is neither asserted nor needed for this
bounded component status.

## 6. Self-check, refusal controls, and limits

The isolated command
`python3 -I -S -B step11_v010_11_category/build_v010_11_category.py`
completed. Independent replay rehashed all 33 inventory members, confirmed
tight canonical JSON for every JSON member, and parsed the builder AST. The
package inventory hashes to
`96647f334c8ce31e04e1bdbc9226cdc4294ea6e43941f7c70f165406057b406d`.
The self-check hashes to
`55e190ecb4565b653b04dc7320e10cecbe3f798718fbeda9911d25870e030a18`.

Six negative controls bit:

| Control | Required refusal |
|---|---|
| empty object labels | BX13 `minItems` schema refusal |
| wrong inclusion target | decoration-preservation refusal |
| missing identity | identity-census refusal |
| wrong composite result | composition-result typing refusal |
| missing generator | generator-coverage refusal |
| wrong source span digest | span-hash refusal |

A second isolated build refused the occupied `contracts/` output before
changing any generated byte.

`F_PLDEC`: CLEAN. Only category incidence, decorations, identities, and
composition were serialized. No physical quantity was evaluated.

M-2: the prior envelope's narrow provenance finding was checked against the
packet by fixed-string, whitespace-normalized, scope/self-reference, and
hyphen/space/underscore probes. The object names `BareRec_2`, `OpenRec_2`,
`DecRec_2`, `K_(1,r)`, `bar(c)`, and `j_c` located the sealed carrier. Exact
file and span digests, not path spelling or search testimony, bind the result.

Anti-tuning: all three labeled first-opening arms and all their canonical
inclusions are present; all identities, composable pairs, and composable
triples are exhausted. No favorable label, morphism, composite, or failed
control was omitted.

Admission remains barred by the Step-11 subgate. The emitted row status is a
component-state transition only. The evaluator chain, board, register, plan,
tracker, and git state were untouched.

Verb audit under the verdict-line scope rule: CLEAN. “Built” means canonical
instance bytes exist. “Compiled” means the sealed bounded BX13 consumer
returned `PRODUCED`. “Stateable” is the consumer's admission-barred component
state, not a row verdict, proof authorization, board change, or admission.

ELEMENTS = 28 built / 0 required underdetermined (4 objects; 7 morphisms; 4 identities; 10 composition entries; 3 generator IDs; ambient DecRec_2 extensions named but not claimed)
COMPILE = PASS_INSTANCE_BUILT_AND_CONSUMER_COMPILED; category laws PASS_EXACT_STRUCTURAL_CATEGORY_LAWS
ROW = STATEABLE_COMPONENTS_PRESENT_ADMISSION_BARRED
ADMISSION = barred, stated
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
