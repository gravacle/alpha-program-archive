# STAGE 8 — DOES THE BASE CARRY GEOMETRY? — DEFAULT-REFUTE AUDIT — O48SR AUDIT V001

Lane: **DEFAULT-REFUTE AUDIT.** Default verdict REFUTED. Adversarial by mandate.
Subject: `STAGE8_BASE_GEOMETRY_O48SR_V001.md` (`7a1c0da3…`), CLAIMED only.
Everything load-bearing re-derived at bytes from the corpus, not from the build's report.

Nothing authored, nothing adopted, nothing advocated. No numeric value of any coupling,
scale, root, eigenvalue, norm or constant computed or approached.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

---

## HEADLINE

```text
D1  THE SEPARATION (Q1)            = CONFIRMED-WITH-CORRECTIONS
D2  CURVATURE CENSUS BY SIDE (Q2)  = REFUTED
D3  BASE GEOMETRY (Q3)             = REFUTED
D4  PROVENANCE (Q4)                = REFUTED
D5  DEPENDENCY (Q5)                = CONFIRMED-WITH-CORRECTIONS
D6  IMPORTS AND BARS               = REFUTED

OVERALL                            = REFUTED
```

**What survives and what does not.** The subject's four *headline verdicts* — SEPARATION-REAL,
PARTIAL, mixed provenance, FIBER-DEPENDS-ON-BASE — all survive re-derivation at bytes, and its
best structural finding (four non-identified base-like objects, bridges open both ways) is not
only correct but **under**-supported: I found a third, more direct absence statement it missed.
What does not survive is the **census that supports those verdicts**. Two categorical absence
claims are false at bytes, an entire ADOPTED geometric rule on the record's own cell was missed,
one quotation presented as "whole" is a paraphrase that inverts its source's modality, and the
Q4 tally contradicts the Q4 table. The subject is right about the shape of the answer and wrong
about its contents.

---

## CHOICE LEDGER

| # | Choice | Disposition |
|---|---|---|
| 1 | "Base" read as `M_G` in `pi_G:P_G->M_G` — the object the adopted ruling's phrase `over the record surface` denotes | FORCED, same as the subject. `WHERE :243-248` introduces `pi_G:P_G->M_G` directly under the W4 heading |
| 2 | `supervision/` restricted to `DOR_*` only | FORCED by the commission. My first sweep pass wrongly included `BOHM_*` files there; I corrected the harness and re-ran. Their hits are excluded from every count below and named in SWEEP CUTOFFS |
| 3 | `.proof_deps/**` and `.pytest_cache/**` excluded, counted separately | Vendored third-party source, not record artifacts. Same disposition as the subject's row 3 |
| 4 | Workspace/cleanroom mirrors deduplicated by basename | Byte-identical mirrors |
| 5 | I did **not** identify `M_G`, `Sigma`, `K`, the `Ref_a` carrier, or the KK/record-bundle `M` with one another | The corpus refuses the merge in three places (Q3 §B below). Reported as distinct throughout |
| 6 | Objects typed IMPORTED or DECLARED are **counted in the census** and marked with their typing, not omitted | A census that silently drops imported objects cannot support a categorical absence claim. This is the disagreement that decides D2 |
| 7 | I did not reproduce any displayed numeric prefactor (`ell_P`, `G_4`, `hbar`, saturation values) when quoting action functionals | Fence. Structure quoted, magnitudes elided and marked `[prefactor elided — fence]` |
| 8 | Both the subject artifact and this audit self-excluded from all sweeps | REGISTER BAR, array glob, last two entries |

---

## IMPORT AUDIT

| # | Notion | Status | Does the finding survive without it? |
|---|---|---|---|
| I-1 | "base" / "fiber" as the two levels of `pi_G:P_G->M_G` | **CORPUS-DEFINED**, `WHERE :243-248, :259-277` | N/A — corpus vocabulary |
| I-2 | Any theorem about bundles, connections, curvature, metrics or complexes | **NOT USED.** No bundle-theoretic, cohomological or differential-geometric consequence is drawn anywhere in this artifact. Naming an object a curvature licensed no conclusion about it | YES — every finding below rests on a displayed corpus string |
| I-3 | That `sqrt(-g) R`, `R_4`, `R4[g]`, `K_ext` are curvature-shaped | **MINIMAL READING OF A DISPLAYED SYMBOL.** I read that the corpus *displays* these symbols inside objects it *itself* names "Einstein-Hilbert action" and "gravitational action functional". I assert nothing about what they satisfy | YES — COR-A is that the subject's claim "no such object exists anywhere" is false, which needs only that the strings are displayed |
| I-4 | That a shortest path / geodesic is a geometric structure | **COMMISSION VOCABULARY** — the commission names geodesics among the structures to sweep for | YES |
| I-5 | Ordinary audit English ("modality", "census", "provenance") | **COMMISSION VOCABULARY** | YES |

**FORBIDDEN IMPORTS: NONE USED.** No external literature. Where the *corpus itself* records an
import (`an imported Fubini-Study / Mandelstam-Tamm theorem`, `an imported KK ansatz`), I report
the corpus's own word and draw nothing from the imported theorem.

---

## SEALS

`shasum -a 256 -c` run from each artifact's own directory.

```text
SUBJECT
  STAGE8_BASE_GEOMETRY_O48SR_V001.md.seal.sha256 ................ OK
  STAGE8_BASE_GEOMETRY_O48SR_V001.md.sha256 ..................... OK
  (both sidecars carry 7a1c0da3…, matching the file on disk)

supervision/ — DOR_* , the permitted and REQUIRED set, ALL FOURTEEN
  DOR_016 … DOR_017 … DOR_018 … DOR_019 ......................... 4/4 OK
  DOR_020_A1 … A2 … A3 … A4 … A5 … A6 … A7 … A8 … A9 ............ 9/9 OK
  DOR_020_CONTINUUM_PACKAGE_CONDITIONAL_RATIFICATION ............ OK
                                                        subtotal  14/14 OK

workspace/ — sources I open and quote
  STAGE8_TASK5_EQ6_WHERE_CLAUSES_LANE2_V005.md .................. OK
  STAGE8_TASK5_EQ6_WHERE_CLAUSES_FINAL_CHECK_LANE1_V001.md ...... OK
  STAGE8_TASK5_EQ6_LOC_REVIEW_AND_HOL_PROVENANCE_DARIO_V001.md .. OK
  STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md ......... OK  (= 7ecf04e9…)
  STAGE8_AXN_SDN_SLICING_INSTANCE_DARIO_V003.md ................. OK
  STAGE8_B1A_CONNECTION_IDENTIFICATION_CODEX2_V001.md ........... OK
  STAGE8_B1C_DENSITY_LAYER_CODEX2_V001.md ....................... OK
  STAGE8_ETHER_CHECK_DARIO_V001.md .............................. OK
  STAGE8_B1A_LIFT_FORCING_CODEX2_V001.md ........................ OK   <- not in subject's list
  STAGE8_7A_MEASURE_ONELINER_CODEX2_V001.md ..................... OK   <- not in subject's list
  STAGE8_7A_MEASURE_DENOTATION_SPEC_ADDENDUM_CODEX2_V001.md ..... OK   <- not in subject's list
  STAGE8_TASK5_HUNT_CROSS_CHECK_AND_FRONTIER_LANE2_V001.md ...... OK   <- not in subject's list
  STAGE8_TASK5_COMMON_SEAMS_LANE3_V002.md ....................... OK
  STAGE8_C1_U_OMEGA_TYPED_CODEX2_V001.md ........................ OK
  STAGE8_ONSET_SATURATION_STEP3_FORCE_CHECK_V001.md ............. OK
  BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md .......... OK
  STAGE8_AXN_BUILD_BOX_GRAVITY_ROW_TYPING_DARIO_V001.md ......... OK
  STAGE8_KK_FRAMING_DERIVED_OR_IMPORTED_AUDIT_V001.md ........... OK
  STAGE8_PARENT_KK_ACTION_ELL_P_DEFINITION_AND_REDUCTION_V001.md  OK
  STAGE8_AXN_SLOT2_PATH_CROSSCHECK_DARIO_V001.md ................ OK
  STAGE8_GRAVITY_MATTER_SOURCE_SUMMANDS_LIVE_V004_STANDING_V001.md OK  (= 58208084…)
  R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_V001.seal.sha256 . 8/8 OK
                                                                       (EIGHT entries, not nine)
  review_packets/STAGE7_QSPEC_CANDIDATE_V001/
    BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md ............... OK  (aa7c6d49…)
    STAGE7_PACKET_MANIFEST_V001.sha256 .......................... OK

UNSEALED AT BYTES — no adjacent sidecar in either root, disclosed, no grade rests on either alone
  COUPLED_RECORD_BUNDLE_MODULUS_GATE_V001.md .................... NO SIDECAR
  STAGE8_CROSS_SECTOR_METRIC_RULE_ADMISSIBILITY_SPEC_V001.md .... NO SIDECAR
```

**Seal finding.** The subject reports `R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_* (9 entries)
..... 9/9 OK` and totals `26/26`. The seal file contains **eight** entries. All eight verify. The
subject's own list therefore totals **25/25 OK**, not 26/26. Separately, at least four artifacts
the subject **quotes** are absent from its seal list entirely (marked above). All four verify OK,
so no grade is endangered — but the claim "Cited-source seals 26/26 OK" does not describe what
was cited. See COR-H.

---

## SWEEP CUTOFFS

Exclusion globs as an **ARRAY**:
`[REGISTER, TRACKER, THE_PLAN*, ROAD_REMAINING*, THE_HANDOFF*, OBSERVATIONS_REGISTER*,
*DECISION_SHEET*, STAGE8_BASE_GEOMETRY_O48SR*]` — the last entry self-excludes both the subject
and this audit. `supervision/` restricted to `DOR_*`. `.proof_deps/**` counted separately.

| Pattern | Kept match lines | Kept basenames | BARRED leak counter | `.proof_deps` | Opened |
|---|---|---|---|---|---|
| `BUNDLE WITH CONNECTION` | 7 | 4 | 7 lines / 3 files | 0 | **ALL 4** — see note |
| `Ricci\|Riemann tensor\|scalar curvature\|sectional\|Gaussian\|intrinsic curvature\|Weyl` | 4 | 2 | 10 | 23 | **BOTH** |
| `S_grav\|S_EH\|sqrt(-g) R\|Einstein-Hilbert\|Einstein tensor` | 41 | 26 | 4 | 0 | **all 6 that display a curvature symbol** |
| `curvature` | 1721 | 269 | 128 | 9 | context-level, deduped |
| `shortest[- *]\|geodesic\|minimal path\|path length\|arc length` | 279 | **73** | 20 | 105 | all 24 `shortest-` contexts |
| *(subject's pattern)* `geodesic\|shortest path\|straight` | 196 | **51** | 19 | 140 | — run only for comparison |
| `distance function\|metric space\|d(x,y)\|dimensionless distance\|relative length` | 11 | 11 | 0 | 3 | **ALL 11** |
| `primitive causal diamond\|causal cell is a` | 17 | 9 | 0 | 0 | **ALL** |
| `MAXWELL_HODGE` | 20 | 12 | 0 | 0 | **the 1 row carrying the parenthetical** |
| `1/24\|det E_p\|cell weight` | 21 | 12 | 0 | 0 | **ALL** |
| `angle deficit\|deficit angle\|angular defect\|excess angle\|Regge\|vertex excess\|holonomy defect` | **0** | **0** | 8 | 8 | n/a — nothing to open |
| `defici\|defect` (broad control) | 4398 | 687 | 209 | 44 | top-20 basenames sampled; all algebraic/bookkeeping |

**OPEN WHAT YOU COUNT — the `BUNDLE WITH CONNECTION` set.** Raw file paths: 8 (7 excluding the
subject itself). Three are genuine BARRED exclusions — `QUESTIONSSETTLED_REGISTER_V001.md`
(cleanroom), `QUESTIONS_SETTLED_REGISTER_V001.md` (supervision), `RELAY_PASTE_570_…`
(supervision, outside the `DOR_*` permission). The surviving four basenames are
`DOR_020_A1_WHERE_CLAUSES_AMENDMENT_2026-08-04.md` (the ruling itself),
`STAGE8_TASK5_EQ6_LOC_REVIEW_AND_HOL_PROVENANCE_DARIO_V001.md` (workspace + cleanroom mirror),
and `STAGE8_THREE_ABSENCES_O41SR_AUDIT_V001.md` (the prior audit). **I opened all four.** The
subject reports "nine files"; that count is only reachable by counting its own artifact and both
mirror paths while simultaneously declaring the artifact self-excluded. Bookkeeping only — its
substantive claim (the ruling is inside the sweep) is correct.

**The decisive sweep-pattern defect.** The subject's declared pattern `geodesic|shortest path|
straight` uses a literal space. The corpus writes the object as `shortest-path` (hyphen) and as
`shortest **relative** projective path` (intervening markdown bold). **Neither form can match.**
The corrected pattern returns 73 basenames against the subject's 51 — 22 files it could not
reach, including the 24-hit cluster in `STAGE8_ONSET_SATURATION_STEP3_FORCE_CHECK_V001.md` and
the adopted rule that decides COR-B.

**Members I did not open.** For `curvature` (269 basenames) I opened every distinct match context
rather than every file, and traced to source every context naming a candidate structure. Contexts
consisting only of gate-board lines, negative ledgers, or relay custody headers were not opened
individually. That is the complete list of what I left closed.

---

# D1 — IS THE BASE/FIBER SEPARATION REAL AT BYTES?

## GRADE: **CONFIRMED-WITH-CORRECTIONS**

I attacked both directions and the separation holds.

**Attack 1 — is `M_G` merely a phrase?** No. `STAGE8_TASK5_EQ6_WHERE_CLAUSES_LANE2_V005.md
:243-248`, verified whole:

> "The base objects carry the ratified principal U(1) bundles
>
> ```text
> pi_G:P_G->M_G,
> pi_G':P_G'->M_G'.                                (B1-8)
> ```"

`M_G` carries a dimension and a smooth structure of its own, `:176-181` whole:

> "1. **Smooth actual support map.**
>
>    ```text
>    f_R:M_G->M_G' is a proper smooth map whose restriction to the old
>    physical image has full rank dim(M_G).         (B1-4)
>    ```"

and `:183-186` whole, adverse clause included:

> "In the equal-dimensional DoR-015 surface family it is a local
> diffeomorphism on that image; the embedded horn requires a proper
> embedding.  The same-carrier attachment horn is `f_R=id` on the old
> image, not a separate law."

**Attack 2 — is the fiber level nominal?** No. `:259-277` verified whole, including the
never-selects clause the subject also carried:

> "1. **Smooth full-rank bundle lift.**  `tilde_f_R` is smooth,
>    U(1)-equivariant, covers `f_R`, and has full rank on the old bundle
>    image:
>
>    ```text
>    tilde_f_R:P_G->P_G',
>    pi_G' compose tilde_f_R=f_R compose pi_G,
>    tilde_f_R(p z)=tilde_f_R(p) z,
>    rank(d tilde_f_R)=dim(P_G) on the old image.  (B1-10)
>    ```
>
>    Equivalently it supplies an equivariant bundle isomorphism
>
>    ```text
>    iota_R:P_G isomorphic_to f_R^*P_G'             (B1-11)
>    ```
>
>    over `id_(M_G)`.  The law retains the full gauge-covariant family of such
>    lifts/isomorphisms.  It never selects one."

**Attack 3 — could the two-level reading be read into a phrase?** No, and the subject identified
the right deciding byte. `WHERE :314-325`, whole (note the corrected range):

> "4. **Connection through the bundle lift.**  The source-bundle connection is
>    compared to the target connection only through `(B1-10)`/`(B1-11)`:
>
>    ```text
>    eta_conn,R(A_G')
>     :=tilde_f_R^*A_G'
>      =iota_R^*(f_R^*A_G'),
>    A_G=eta_conn,R(A_G') on the old image.         (B1-15)
>    ```
>
>    A bare base-map symbol `f_R^*A_G'` without `iota_R` is not a typed
>    connection on `P_G` and is forbidden."

Independently confirmed at `:655` — `| bare f_R^*A | forbidden; replaced by bundle
lift/pullback-bundle isomorphism |` — and by the two level-keyed rank tests, `SMOOTHNESS_TEST =
INSTALLED` / `FULL_RANK_TEST = INSTALLED` at `:442-443`, with the falsifier `:617-618` whole:

> "3. **Rank defect.**  If `df_R` or `d tilde_f_R` loses required rank, the
>    coframe/field pullback is degenerate and the tuple is rejected."

**Adverse clause, carried whole.** `:37-39`:

> "V005 is a clause artifact, not an inhabitant.  It defines two admissibility
> laws.  Each law may have no members.  DoR-020's certified joint `[EQ6]`
> witness remains the only object authorized to prove joint inhabitance."

with `:382-384` `W4_LOCAL_FIELD_LAW = LAW_ONLY / BUNDLE_TYPED`,
`W4_ADMISSIBLE_SET_MAY_BE_EMPTY = true`, `W4_PROPOSED_NOT_ADOPTED = true` — note the subject
quoted the first two of these three and omitted the third, which is the most adverse of them.

**Corrections at this dimension.** Four line ranges are off by one at the head, and one is off at
both ends: the subject's `:302-310` for the coframe clause is `:301-312`; `:315-325` for the
connection clause is `:314-325`; `:553-557` is `:554-557`; and `Cof_R` is the P4/X4 row at `:122`,
not `:123` (`:123` is `Dens_R`). Every quoted *string* is byte-accurate; only the ranges drift.
Recorded as COR-K.

---

# D2 — CURVATURE CENSUS BY SIDE

## GRADE: **REFUTED**

The commission named this dimension's likeliest error as assigning a fiber-side object to the
base side because geometric words appear near it. The subject did not make that error. It made
two others: it **omitted an entire class of base-side curvature objects**, and it tallied as
"BASE SIDE" two objects living on a carrier its own CHOICE LEDGER declares is not the base.

## §A — THE OMITTED CLASS: A CURVATURE SCALAR IS DISPLAYED IN THE CORPUS

The subject states, in Q2 and again as FL-3:

> "**No Riemann, Ricci, scalar or sectional curvature of the record surface exists anywhere in
> the corpus.**"

> "**NO CURVATURE OF THE RECORD SURFACE EXISTS.**"

**This is false at bytes.** `COUPLED_RECORD_BUNDLE_MODULUS_GATE_V001.md :17-18`, whole:

> "This realizes gravity and charged phase transport as different components of
> one record-bundle geometry. It uses no alpha target."

and `:22-28`, whole, prefactor elided under the fence:

> "For constant `r_Q`, the two-derivative Einstein-Hilbert action on the total
> space reduces schematically to
>
> ```text
> S_P
>   = [prefactor elided — fence] integral_M sqrt(-g)
>       [R_4 - [coefficient elided — fence] F_mu_nu F^mu_nu].
> ```"

`R_4` is a curvature scalar of the base metric `g` on `M`, displayed **in the same bracket as the
fiber curvature `F_mu_nu F^mu_nu`**, in an artifact the corpus titles `COUPLED RECORD BUNDLE` and
whose own sentence calls the pair "different components of one record-bundle geometry." A census
sorting curvature by side cannot omit the one displayed object that exhibits both sides at once.

It is not isolated. `STAGE8_PARENT_KK_ACTION_ELL_P_DEFINITION_AND_REDUCTION_V001.md :56`
(seal OK), whole:

> ```text
> S4 ⊃ [prefactor elided — fence] ∫ d^4x sqrt(-g) R4[g],
> ```

And a third artifact displays a full gravitational action functional carrying **both** an
intrinsic curvature scalar and an extrinsic curvature boundary term. I did not rest on the
quoting artifact: I resolved its hash pin `58208084e8da8d9d` to its home file,
`STAGE8_GRAVITY_MATTER_SOURCE_SUMMANDS_LIVE_V004_STANDING_V001.md` (seal OK), and read the
display there at `:159-165`. Prefactor elided under the fence:

> ```text
> S_grav,D
>   = [prefactor elided — fence]
>       { integral_M sqrt(-g) R d^4x
>         + 2 sum_B epsilon_B integral_B sqrt(|h|) K_ext d^3x
>         + 2 sum_J integral_J sqrt(sigma) eta_J d^2x }
>     + S_ref.
> ```

**How the subject missed it, and why that compounds the finding.** The subject's own sweep row
`scalar/Ricci/sectional/Gaussian/intrinsic curvature` returned exactly this file as one of its
two record hits, and the subject states it opened both and that "Neither supplies one." The
curvature display sits **six lines below** the line its pattern matched. The matched line
`:156` reads `` `Ricci` 0, `S_EH` 1, `S_grav` 1, `curvature scalar` 0 `` — a *count* of zero for
the word "Ricci" — and the subject appears to have read the zero as the answer. Four lines later
the same artifact writes, whole:

> "**The row's predicate "no such term or placeholder is present" is true at the build's control
> set and false archive-wide.** Neither lane disclosed the scope limit, and neither cited this
> display."

That sentence is a prior lane being corrected for **exactly the error the subject then repeated**:
declaring a categorical absence from a control set too narrow to see the display.

**The adverse clause, carried in full — and it is why the subject's headline is salvageable.**
These objects are typed IMPORTED and DECLARED, never derived or adopted.
`STAGE8_KK_FRAMING_DERIVED_OR_IMPORTED_AUDIT_V001.md :18-19` (seal OK), whole:

> "No sealed derivation identifies the projective direction with a spacetime dimension. The
> five-dimensional Einstein-Hilbert parent action is therefore an imported KK ansatz, not an
> emergent-gravity derivation."

and `STAGE8_AXN_SLOT2_PATH_CROSSCHECK_DARIO_V001.md :110` (seal OK): *"The displayed term-shaped
object `S_grav,D` remains **DECLARED** with its mixed domain"*.

**Corrected claim.** Not *"no curvature of the record surface exists anywhere in the corpus"* but:
*no curvature of the record surface is derived or adopted anywhere in the corpus; the ones the
corpus displays are typed IMPORTED (KK ansatz) or DECLARED, and no lane is authorized to install
them.* That is a weaker claim, it is true at bytes, and it is the one the record supports.

## §B — THE SIDE-ASSIGNMENT DEFECT

The subject's CHOICE LEDGER row 1 declares, FORCED, that "base" means `M_G`. Its BASE-SIDE tally
then consists entirely of two objects on `Sigma_s` — the Cauchy-slice family of the SD-N
spacetime, which its own Q3 §C lists as **BASE-4**, a *different* object it explicitly declines
to identify with `M_G`. Both entries verify at bytes as quoted (`SDN V003 :98-101`, `:103-104`,
`:110-114`, seal OK) and both are correctly *not* fiber objects. But a tally line reading
`BASE SIDE .... 2` on the strength of a carrier the same artifact says is not the base is a
category the subject created and then filled from elsewhere. Recorded as COR-J.

`K_ij := (1/2) d_s h_ij` is moreover the extrinsic curvature of a **3-dimensional slice inside a
4-dimensional spacetime**, not a curvature of a 4-dimensional record surface — a distinction the
subject never states.

## §C — WHAT THE CENSUS SHOULD READ

```text
FIBER / CONNECTION SIDE ...... 12   (F-1 … F-12 re-derived, all confirmed at bytes)
BASE SIDE, on M_G ............  0   (no curvature of M_G is defined anywhere)
BASE SIDE, on Sigma_s ........  2   (K_ij + H; the base affine transport) — ENTERED
BASE SIDE, on the KK /
  record-bundle carrier M .....  3   (R4[g]; R_4 beside F_munu F^munu; R with K_ext
                                      and eta_J in S_grav,D) — IMPORTED / DECLARED
CANNOT-DETERMINE .............  1   (the f = da identity question — confirmed as posed)
```

The subject's `12 | 2 | 1` becomes **`12 | 5 | 1`** once the omitted class is counted, and the
BASE column must be split by carrier because the corpus does not merge those carriers.

---

# D3 — DOES THE BASE CARRY GEOMETRY? — THE HEAVIEST

## GRADE: **REFUTED**

The headline **PARTIAL survives** — indeed I strengthen it below. The census beneath it does not.
The subject graded a mixed verdict, so per the commission I attacked both halves: I hunted for
structure it missed, and I attacked each structure it itemized. Both attacks landed.

## §A — STRUCTURE IT MISSED: THE RECORD CELL CARRIES A SHORTEST-PATH GEOMETRY, AND IT IS ADOPTED

The subject's §E concludes, flatly:

> "If the question is *"does the record's own cellular object carry more than incidence?"* the
> answer at bytes is: **orientation and a root, and otherwise no**"

**Refuted.** `BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md :97-108` (seal OK), whole,
including every adverse clause and with the saturation value elided under the fence:

> "## Adopted Gravacle onset rule
>
> The allow/require boundary is adopted to select first admissible record onset
> through a shortest **relative** projective path on the unique physical record
> cell. Conditional on this target-value-free, target-aware Level-1 rule,
>
> ```text
> J_FS,rel = [value elided — fence].
> ```
>
> The lower bound is derived from the imported theorem. Saturation is adopted,
> not derived. Historical target blindness is not claimed."

A **shortest path on the unique physical record cell** is a path-length structure with a
minimality notion on the record's own cell. The corpus makes the geodesic reading explicit at
`STAGE8_ONSET_SATURATION_STEP3_FORCE_CHECK_V001.md :38-40` (seal OK), whole:

> "  release: derive that the first physically admissible durable record onset
>            must use a shortest relative projective/geodesic path on the unique
>            physical record cell"

**Its adverse clauses, carried whole — the corpus is scrupulous that this is unforced.** Same
artifact, `:19-27`:

> "First orthogonality fixes the endpoint condition inside the declared two-level
> record-write geometry. Saturation asserts more: that the physical onset
> achieves that endpoint along the shortest relative projective path, so the
> Fubini-Study energy-uncertainty/path-length lower bound is attained.
>
> The corpus derives the lower bound from an imported Fubini-Study /
> Mandelstam-Tamm theorem and verifies one symmetric two-state representative
> that attains the endpoint. It does not derive that the physical process must
> choose that representative or any other shortest path."

with three separate negative flags: `:42` `shortest_path_physical_selection_theorem_found =
false | TYPE-S`; `:151` `physical_shortest_trajectory_forced_by_endpoint = false | TYPE-R`;
`:235` `physical_shortest_onset_selection_theorem_derived = false | TYPE-U`.

So the corrected reading is: **the record cell carries a relative projective path-length
structure with a shortest/geodesic selection rule, ADOPTED, expressly not derived.** That is
strictly more than "orientation and a root".

## §B — MORE STRUCTURE IT MISSED

**A flat Lorentzian geometry is SUPPLIED on the record's primitive cell.**
`STAGE8_C1_U_OMEGA_TYPED_CODEX2_V001.md :139` (seal OK), whole row:

> "| diamond class | ordinary flat Lorentzian primitive causal diamond (S04, S10, S11) |
> SUPPLIED IN DECLARED BRANCH |"

**A distance function `d(x,y)` exists.** The subject states: *"The sweep for `distance
function|metric space|d(x,y)` returned **zero line-level matches in the record corpus.** No
`d(x,y)` exists."* `STAGE8_TASK5_COMMON_SEAMS_LANE3_V002.md :613-614` (seal OK), whole:

> ```text
> d(g_D x,g_D y)=h_d(g)d(x,y),
> h_d(g)>0.                                           (C6)
> ```

with a Lipschitz-style quotient over it at `:619-624`,
`q = sup_(K!=K') d(g_D B_T(K),g_D B_T(K'))/d(K,K')`, on `D subset K_amb`. Whether `K_amb` is the
record's cell carrier is **INDETERMINATE-AT-BYTES** — the artifact does not say. But the flat
claim "no `d(x,y)` exists" is false, and the subject's §B row and §E absence line both rest on it.

**A metric fixing distances is live, not merely killed.** The subject's §B.1 cites BID V011 `:65`
to show an imported Fubini-Study metric was repaired away. That is true of *that* defect, but
`STAGE8_KK_FRAMING_DERIVED_OR_IMPORTED_AUDIT_V001.md :14-15, :29-30` (seal OK) records the object
as current: *"the Fubini–Study metric fixes dimensionless distances but not their dimensional
conversion"*, and *"The relevant internal object is the projective record degree with
Fubini–Study metric, not a derived circle length."*

## §C — STRUCTURE IT ITEMIZED THAT DOES NOT HOLD

**"an orthonormal frame (angle)" — the angle is an import.** The subject lists "an orthonormal
frame (angle)" among PRESENT structures in §E, on the strength of `SDN V003 :110` *"Choose any
orthonormal frame `(e_1,e_2,e_3)` on `Sigma_0`"*. That string verifies. But **no angle is defined
anywhere in the corpus**; "hence an angle" is the subject's inference from the word orthonormal,
and the commission's standing discipline says naming something does not license what the name
suggests. The structure to report is orthonormality. The angle is not there.

**"its inverse `h^(ij)`" and "a flatness-along-the-flow statement".** The corpus displays
`H := h^(ij) K_ij` and `nabla_n n = 0`; it nowhere says `h^(ij)` is the inverse of `h_ij`, nor
that `nabla_n n = 0` is a flatness statement. Both are imported readings. Neither changes a grade.

**"a weight that makes cells non-equivalent" — over-read.** The subject asserts: *"**Cells are
therefore not equivalent to one another.** … This is a genuine non-uniform weighting on the cell
set."* At bytes the weights are **uniform within a subdivision and volume-conserving**.
`STAGE8_7A_MEASURE_DENOTATION_SPEC_ADDENDUM_CODEX2_V001.md :31-39` (seal OK), whole:

> "  - On a d-simplex with edge-frame E:          Vol_4 = |det E| / d!.
>     For the sealed order-simplex subdivision of the unit 4-cube this gives
>     1/24 per cell, 24 cells, total 1 — MAJ 08b91543…[19632,19996), reproduced
>     exactly at 753 §1.3.
>
> ZERO PHYSICS CHOICE: no new measure, weight, normalization or convention is
> introduced.  The statement records which already-classified measure the
> general map's volume factor denotes, and evaluates it on the two cell types
> the working class produces."

Every one of the 24 simplices carries the *same* weight and the subdivision preserves the total.
The variation the subject reports is between a cell and its own children, and between two cell
*shapes* — a volume denotation carrying **ZERO PHYSICS CHOICE** by its author's own words, not a
weighting that distinguishes one record cell from another. (No value was computed here; `1/24`
is quoted from the source.)

**Two quotations in §A are uncited.** The cell-weight sentence is
`STAGE8_B1A_LIFT_FORCING_CODEX2_V001.md :176` — and it sits inside row **O4** of a table headed
`## 2. AS1 — the four obligations, stated as constraints — CLAIMED`, i.e. it is a *constraint on
a candidate lift* in a section its author marks CLAIMED, not a free-standing result. The
`1/24` exhibit is `STAGE8_7A_MEASURE_ONELINER_CODEX2_V001.md :77-81`. Neither is named; neither
appears in the subject's seal list. The claim that the cell-weight sentence is "the single match
in the whole corpus" is also false — it appears in workspace and cleanroom, and the weight family
`1/16`, `1/24`, `1/384` is displayed at `STAGE8_B1A_CORRECTED_JOINT_SOLVE_CODEX2_V001.md :301`.

## §D — WHAT SURVIVES, AND IS STRENGTHENED

The subject's §C — **four distinct base-like objects the corpus refuses to identify** — is
correct at bytes and is its best work. Both bridge citations verify:
`STAGE8_B1C_DENSITY_LAYER_CODEX2_V001.md :105` (`f_g` UNDECIDABLE; board `SUPPLIED = 0`,
`OPACITY-BOUND = 2` confirmed at `:161-166`), and
`STAGE8_PRPS_GATE4_LOCALIZATION_BRIDGE_ATTEMPT_V001.md :185-195`
(`reverse_discrete_to_smooth_bridge_canonical = false`).

**I found a third, more direct absence the subject missed**, in the same table as the diamond
class — `STAGE8_C1_U_OMEGA_TYPED_CODEX2_V001.md :148` (seal OK), whole row:

> "| incidence-to-diamond map | no map from primitive-incidence data to tip pair or equivalent
> diamond carrier is displayed | ABSENT |"

This is the cleanest statement in the corpus of the gap the subject's FL-1 registers, and it
names the two carriers directly. The PARTIAL grade is right; the record supports it better than
the subject knew.

## §E — CORRECTED GRADE STATEMENT

```text
Q3 = PARTIAL   (headline UNCHANGED; supporting census corrected)

ADD to PRESENT:  an adopted shortest/geodesic relative-projective path structure on the
                 unique physical record cell (ADOPTED, expressly not derived);
                 an ordinary flat Lorentzian primitive causal diamond class, SUPPLIED
                 IN DECLARED BRANCH;
                 a displayed distance function d(x,y) with a positive scaling law.

REMOVE from PRESENT: "angle" (no angle is defined in the corpus — orthonormality is);
                 "a weight making cells non-equivalent" (weights are uniform within a
                 subdivision and volume-conserving; ZERO PHYSICS CHOICE).

UNCHANGED ABSENT: any Riemann/Ricci/scalar/sectional curvature that is DERIVED or ADOPTED;
                 any angle deficit / vertex excess / face defect — I re-ran this sweep on a
                 pattern WIDER than the subject's (adding `vertex excess`, `holonomy defect`)
                 and CONFIRM 0 record hits; the broad `defici|defect` control returns 687
                 basenames dominated by "zero-defect section" and "rank defect", which are
                 algebraic/bookkeeping, not geometric — the subject's reading is correct;
                 an intrinsic length scale for the record.

AND:             the four-carrier finding stands, with a third absence statement added.
```

---

# D4 — PROVENANCE

## GRADE: **REFUTED**

The commission warned that a prior commission missed an entire adopted ruling, and that a wrong
DERIVED grade is the most consequential error available. **The DERIVED grades are sound. An
entire ADOPTED rule was missed.**

## §A — THE DERIVED GRADES SURVIVE

I checked the one item the subject grades DERIVED and it holds.
`R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md :5-19, :34-54, :103-109, :116`
all verify byte-accurate as quoted, seal OK. The subject's own qualifier — that this is
"**DERIVED from an ENTERED premise** (Poincaré covariance of a flat cell)" — is exactly right and
is the honest framing. The `Vol_4` denotation likewise survives: the addendum is explicit that it
is "classified uniquely" upstream and introduces "no new measure, weight, normalization or
convention", so grading it derived rather than authored is defensible.

One adverse clause the subject did not carry, from the same result at `:111-113`, whole:

> "This result fixes the primitive flat-cell integration measure. It does not
> derive the complete parent generator, its interacting spectral measure,
> durability, a coupling, or alpha."

It does not change the grade, but a whole-span discipline should have carried it.

**Content-dependence = NONE survives.** The R3.3 scope exclusion and the `ETHER_CHECK :176-183`
and `:110-116` spans all verify byte-accurate, seal OK.

## §B — THE MISSED ADOPTED RULE

Quoted in full at D3 §A: `BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md :97-100`,
`## Adopted Gravacle onset rule` — *"The allow/require boundary is **adopted** to select first
admissible record onset through a shortest **relative** projective path on the unique physical
record cell."* This is a geometric structure on the record's own cell, adopted, and it appears
nowhere in the subject's Q4 table, Q3 census, or Q2 census. It is the precise hazard the
commission named.

## §C — THE TALLY CONTRADICTS ITS OWN TABLE

The subject's Q4 table (`STAGE8_BASE_GEOMETRY_O48SR_V001.md :722-736`) has **thirteen** rows:

```text
ENTERED     rows 1,2,3,4,5,10  = 6   (subject's tally says 5 — its gloss omits row 5,
                                      "The orthonormal frame on Sigma_0", which its own
                                      table marks ENTERED)
ADOPTED     rows 6,7           = 2
DERIVED     rows 8,9           = 2   (subject's tally says 1, merging Vol_4 into the measure)
NAMED-ONLY  rows 11,12,13      = 3
                          TOTAL  13
```

The tally block at `:738-743` reads `1 + 2 + 5 + 3 = 11`. Two rows are lost between the table and
the tally.

## §D — TEN OF FOURTEEN REQUIRED RULINGS WERE NOT READ

The commission states the `DOR_*` rulings are **PERMITTED AND REQUIRED**. There are fourteen. The
subject's SEALS block lists four. I verified all fourteen (14/14 OK) and read all fourteen. Two of
the unread ones bear directly on the ruling the subject makes governing:

`DOR_020_A4_J12_CONTACT_GLUE_STRICT_PUSHOUT_2026-08-04.md :8`, whole:

> "THIS AMENDMENT EXPLICITLY SUPERSEDES DoR-020-A1's clause-layer-completeness statement."

`DOR_020_A5_CONTACT_LAPLACIAN_REDUCING_2026-08-04.md :7-8`, whole:

> "SUPERSEDES DoR-020-A1's clause-layer-
> completeness statement (as A4 did)."

The supersession reaches DoR-020-A1's *clause-layer-completeness* sentence, **not** its bundle
typing, so D1 is unaffected — but a commission that reads four of fourteen required rulings
cannot know that, and the subject asserts nothing about it. A third unread ruling,
`DOR_020_A9_XI_N_ADOPTED_2026-08-05.md :7-13`, adopts a further where-clause as "lawful
structure" with "the relative holonomy consumed per the derived display" — squarely inside this
commission's subject matter and uncensused.

## §E — CORRECTED TALLY

```text
Q4 (corrected) = DERIVED 2 · ADOPTED 3 · ENTERED 6 · NAMED-ONLY 3   [total 14]

  DERIVED     2  the uniform flat-cell measure (from an ENTERED premise on FLAT cells);
                 the Vol_4 denotation (zero-physics-choice recording of that classification)
  ADOPTED     3  Cof_R; Dens_R (both as possibly-empty membership laws);
                 + the Gravacle onset rule — shortest relative projective path on the
                   unique physical record cell  [NEW]
  ENTERED     6  smooth/3+1/signature/spin/CPT; the Lorentzian family; the frozen eta;
                 the SDN metric-and-slicing package; orientation/root;
                 + the orthonormal frame on Sigma_0  [restored from the subject's own table]
  NAMED-ONLY  3  M_p = I; delta_K'/d_g; the record's length scale

CONTENT-DEPENDENCE OF BASE STRUCTURE = NONE.  CONFIRMED at bytes, unchanged.
```

---

# D5 — DOES THE FIBER SIDE DEPEND ON THE BASE?

## GRADE: **CONFIRMED-WITH-CORRECTIONS**

The subject's grade FIBER-DEPENDS-ON-BASE, on admissibility only, survives. Two of its three
DEPENDS legs verify exactly. The third is a quotation defect serious enough to name separately.

## §A — THE TWO LEGS THAT HOLD

`STAGE8_B1A_CONNECTION_IDENTIFICATION_CODEX2_V001.md :122-123` (seal OK) verifies byte-accurate,
both rows whole, **including the adverse clause the subject correctly carried**:

> "| I8 | **Coframe compatibility.** On each child cell, the connection/curvature transport
> must be expressible with the sealed child coframe, including the derived simplicial frame.
> | D1 requires the fields in one `J_ref`; the coframe artifacts establish the per-cell
> frame but no connection relation. |
> | I9 | **`Vol_4` compatibility.** The transported curvature must make the child-cell
> quadratic `Vol_4(C) sum F^2` natural under refinement, with `Vol_4` evaluated
> intrinsically on boxes and simplices. | D4's exact linear/quadratic split; D5's forced
> `Vol_4(C)` rule. |"

`WHERE :621-622` verifies whole: *"5. **Coframe/density mismatch.**  Failure of nondegeneracy,
positivity, or duality rejects the tuple."* The tuple constituency at `:253-256` verifies. This is
a real admissibility dependence at bytes, and the subject's standing note — that every DEPENDS
item is a demand **not met** — is accurate and properly adverse to its own grade.

## §B — THE THIRD LEG IS A PARAPHRASE PRESENTED AS A QUOTATION

The subject writes: *"Of the six irreducible generators DoR-020 conditions the whole continuum
package on, one reads, **whole**:"* and displays:

> "B_C3_MAXWELL_HODGE (close d on the C1 carrier → spectral gap/closed range → the symbol
> from P4 coframes)"

Four defects, in ascending order of seriousness:

1. **No citation.** No file, no line.
2. **Mis-attributed.** `DOR_020_CONTINUUM_PACKAGE_CONDITIONAL_RATIFICATION_2026-08-04.md :12-13`
   lists the six generators **by bare name only** — `B_C3_MAXWELL_HODGE,` with no parenthetical
   at all. The ruling does not contain the quoted words.
3. **Not whole.** The actual source is
   `STAGE8_TASK5_HUNT_CROSS_CHECK_AND_FRONTIER_LANE2_V001.md :444` (seal OK), whose text reads,
   whole: *"close `d` on the C1 carrier, prove spectral-gap/closed-range estimates, run
   functional calculus, **derive symbol from P4 coframes**, then test normalization/refinement
   cubes"*. Commas became arrows, "run functional calculus" was dropped, "then test
   normalization/refinement cubes" was dropped, and "derive symbol from" became "the symbol from".
4. **Modality inverted — this is the one that matters.** The subject uses it affirmatively:
   *"The symbol of the Maxwell/Hodge operator … **is drawn** from the P4 coframes."* At bytes the
   sentence is the **would-build column** of a row whose verdict column reads
   **`CONSTRUCTIBLE_WITH_ROUTE`**, with the same row's requirement column listing *"completed
   local symbol, closed ranges/domains, Hodge/Maxwell projections, magnetic partner, nonzero
   normalization"* as **not yet supplied**. It is an instruction for a construction that has not
   been performed, reported as a present dependency.

The grade survives because legs one and two carry it alone. But the subject's SELF-AUDIT line
`QUOTES CHECKED FOR WRAPS = true (every displayed quote re-read against the source line range)`
cannot be true of a quote that has no source line range and does not match its source.

---

# D6 — IMPORTS AND BARS

## GRADE: **REFUTED**

**Imports asserted beyond the corpus** (all named in D3 §C): "hence an angle" from orthonormality;
"its inverse `h^(ij)`"; "a flatness-along-the-flow statement" for `nabla_n n = 0`; and, more
loosely, "Proper time along the normal geodesics **is a distance** on the base" — though this last
is well hedged by the subject's own next sentence. None is load-bearing for a headline grade, but
the subject's IMPORT AUDIT declares **"FORBIDDEN IMPORTS: NONE USED"** and **"Naming an object a
curvature licensed no conclusion about it anywhere in this artifact"**, and the angle is precisely
a conclusion drawn from a name. The declaration is broader than the artifact earns.

**A corpus-internal import the subject did not report.** `STAGE8_ONSET_SATURATION_STEP3_FORCE_
CHECK_V001.md :23-25`: *"The corpus derives the lower bound from an **imported** Fubini-Study /
Mandelstam-Tamm theorem"*. An audit of imports into base geometry should record that the corpus's
own path-length bound rests on an imported theorem. I draw nothing from that theorem.

**Seal discipline.** `26/26` overstates by one (the R3_3 seal file has eight entries, not nine;
8/8 OK; the subject's own list totals 25/25). At least four quoted sources are absent from the
seal list altogether — `STAGE8_B1A_LIFT_FORCING_CODEX2_V001.md`,
`STAGE8_7A_MEASURE_ONELINER_CODEX2_V001.md`,
`STAGE8_TASK5_HUNT_CROSS_CHECK_AND_FRONTIER_LANE2_V001.md`, and the unnamed beta-gap
specification. All four verify OK, so nothing is endangered; but "Cited-source seals 26/26 OK"
does not describe what was cited. The subject's two *disclosed* exceptions (the unsealed
`PRIMITIVE_RELATIVE_PHASE_CONNECTION_V001.md`, and the BID V011 packet-member substitution) I
re-checked and both disclosures are accurate — the packet member `aa7c6d49…` verifies against
`STAGE7_PACKET_MANIFEST_V001.sha256`, the top-level copy hashes `20a3a17d…`, and every BID span
the subject quotes verifies byte-identical in the packet member.

**Fences: INTACT.** `alpha_computed = false`, `proof_authorized = false`,
`kappa_record_computed = false` are present and correct in the subject. I found no computed
coupling, scale, root, eigenvalue, norm or constant. The `1/24` in the subject's Q3 is **quoted**
from `STAGE8_7A_MEASURE_ONELINER_CODEX2_V001.md :79` and the addendum `:33`, not computed — I
verified the string exists verbatim before assessing it. No breach.

**Authoring / advocacy / adoption: NONE FOUND** in the subject. Its lane discipline is clean; its
adverse clauses are, with the exceptions named above, carried whole; and it repeatedly reports
against its own interest (the LAW-ONLY emptiness, the SUPPLIED = 0 board, the "not met at bytes"
standing note on its own Q5 grade). That candour is real and I record it.

**Catalogued negatives used as authority: NONE FOUND.** The subject reads negative flags as
absences, which is their correct use.

---

## CORRECTIONS, IN SEVERITY ORDER

| # | Correction | Deciding file:line |
|---|---|---|
| **COR-A** | **A categorical absence claim is false at bytes.** Q2 and FL-3 assert no Riemann/Ricci/scalar/sectional curvature of the record surface "exists anywhere in the corpus". The corpus displays a curvature scalar beside the fiber curvature in an artifact it calls one record-bundle geometry, and a full gravitational action functional carrying intrinsic **and** extrinsic curvature. Corrected claim: none is **derived or adopted**; those displayed are typed IMPORTED / DECLARED. Aggravating: the artifact the subject says it opened contains, a few lines below its own match line, a prior lane being corrected for this exact error | `STAGE8_GRAVITY_MATTER_SOURCE_SUMMANDS_LIVE_V004_STANDING_V001.md:159-165`; `COUPLED_RECORD_BUNDLE_MODULUS_GATE_V001.md:22-28`; `STAGE8_AXN_BUILD_BOX_GRAVITY_ROW_TYPING_DARIO_V001.md:174-175` |
| **COR-B** | **An entire ADOPTED geometric rule on the record's own cell was missed** — the hazard the commission named. Refutes Q3 §E's "orientation and a root, and otherwise no"; adds one to Q4 ADOPTED; belongs in the Q2 census. Root cause: the sweep pattern `shortest path` (literal space) cannot match `shortest **relative** projective path` or `shortest-path`; corrected pattern returns 73 basenames against 51 | `BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md:99-101` |
| **COR-C** | **A quotation presented as "whole" is a paraphrase, uncited, mis-attributed to a ruling that does not contain it, with its modality inverted** — a `CONSTRUCTIBLE_WITH_ROUTE` would-build instruction reported as a present dependency | `STAGE8_TASK5_HUNT_CROSS_CHECK_AND_FRONTIER_LANE2_V001.md:444` (vs subject's attribution to `DOR_020_CONTINUUM…:12-13`) |
| **COR-D** | **"No `d(x,y)` exists / zero line-level hits" is false.** A distance function with a positive scaling law and a Lipschitz-style quotient is displayed. Whether its carrier is the record's cell carrier is INDETERMINATE-AT-BYTES | `STAGE8_TASK5_COMMON_SEAMS_LANE3_V002.md:613-614` |
| **COR-E** | **Ten of fourteen REQUIRED `DOR_*` rulings were not read.** Two of the unread declare they supersede the very ruling the subject makes governing (the supersession reaches only the clause-layer-completeness sentence, so D1 is unaffected — but the subject could not have known that); a third adopts a further where-clause as lawful structure, uncensused | `DOR_020_A4_J12_CONTACT_GLUE_STRICT_PUSHOUT_2026-08-04.md:8` |
| **COR-F** | **The Q4 tally contradicts the Q4 table** — thirteen rows tallied as eleven; ENTERED under-counted by one (the orthonormal frame), DERIVED by one (Vol_4 merged into the measure) | `STAGE8_BASE_GEOMETRY_O48SR_V001.md:722-743` |
| **COR-G** | **"A weight that makes cells non-equivalent" is an over-read.** Weights are uniform within a subdivision and volume-conserving; the source declares ZERO PHYSICS CHOICE. Also: the cell-weight sentence is lifted uncited from an **obligation row** in a section marked CLAIMED, and "the single match in the whole corpus" is false | `STAGE8_7A_MEASURE_DENOTATION_SPEC_ADDENDUM_CODEX2_V001.md:31-39`; source row `STAGE8_B1A_LIFT_FORCING_CODEX2_V001.md:176` |
| **COR-H** | **Structure missed that the subject would have welcomed** (it strengthens PARTIAL): a flat Lorentzian diamond class SUPPLIED on the record's primitive cell, and a third, more direct bridge-absence statement naming both carriers | `STAGE8_C1_U_OMEGA_TYPED_CODEX2_V001.md:139` and `:148` |
| **COR-I** | **Side-assignment category defect.** Both BASE-SIDE census entries live on `Sigma_s`, which the subject's own Q3 §C lists as a different carrier from the base its CHOICE LEDGER row 1 declares FORCED; and `K_ij` is the extrinsic curvature of a 3-slice inside a 4-spacetime, never stated | subject `:49` vs `:343-344` |
| **COR-J** | **Imports drawn from names.** "hence an angle" (no angle is defined in the corpus); "its inverse `h^(ij)`"; "a flatness-along-the-flow statement" — against a declared "FORBIDDEN IMPORTS: NONE USED" | subject `:420-422`, `:348-350` |
| **COR-K** | **Seal total overstated and four cited sources unlisted.** `26/26` should be `25/25` (the R3_3 seal file has eight entries, 8/8 OK); four quoted artifacts appear in no seal list. All verify OK — no grade endangered | `R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_V001.seal.sha256` |
| **COR-L** | **Line-range drift.** `:302-310`→`:301-312`; `:315-325`→`:314-325`; `:553-557`→`:554-557`; `Cof_R` is `:122` not `:123`. Every quoted string is byte-accurate; only the ranges drift | `STAGE8_TASK5_EQ6_WHERE_CLAUSES_LANE2_V005.md:301`, `:314`, `:122` |

---

## CORRECTED GRADES AND TALLIES, STATED EXPLICITLY

```text
Q1  BASE/FIBER SEPARATION   = SEPARATION-REAL              [UNCHANGED — re-derived at bytes]

Q2  CURVATURE CENSUS        = FIBER 12 | BASE 5 | CANNOT-DETERMINE 1
                              (was FIBER 12 | BASE 2 | CD 1)
                              BASE column must be split by carrier:
                                on M_G ............................. 0
                                on Sigma_s (ENTERED) ............... 2
                                on the KK / record-bundle M
                                  (IMPORTED / DECLARED) ............ 3

Q3  DOES THE BASE CARRY GEOMETRY = PARTIAL                 [HEADLINE UNCHANGED]
                              +3 structures added to PRESENT
                              -2 structures removed from PRESENT
                              "orientation and a root, and otherwise no" — REFUTED

Q4  PROVENANCE              = DERIVED 2 · ADOPTED 3 · ENTERED 6 · NAMED-ONLY 3   [total 14]
                              (was DERIVED 1 · ADOPTED 2 · ENTERED 5 · NAMED-ONLY 3, total 11)
    CONTENT-DEPENDENCE      = NONE                         [CONFIRMED at bytes]

Q5  FIBER DEPENDS ON BASE   = FIBER-DEPENDS-ON-BASE (admissibility)   [UNCHANGED]
                              supporting legs: 2 of 3 hold; the third is COR-C
```

---

## FLAG BLOCK

| # | Flag | Statement |
|---|---|---|
| **FL-1** | **THE SUBJECT'S HEADLINE VERDICTS ALL SURVIVE; ITS CENSUS DOES NOT.** Every one of Q1/Q3/Q4-shape/Q5 is right at bytes. The refutations are of the supporting counts, sweeps, quotations and absence claims. A reader who takes only the five headline lines is not misled; a reader who relies on "no curvature exists anywhere", "no `d(x,y)` exists", or "orientation and a root, and otherwise no" is. |
| **FL-2** | **THE REPEATED-ABSENCE PATTERN IS THE FINDING OF THIS AUDIT.** The artifact the subject swept for curvature contains, in the same section, a prior lane being corrected for declaring an absence true at a narrow control set and false archive-wide. The subject then declared such an absence. Categorical absence claims in this program have now failed the same way twice; the reachable discipline is to state absences as *"not derived / not adopted"* rather than *"does not exist anywhere"*. |
| **FL-3** | **ONE SWEEP PATTERN CAUSED THE MOST CONSEQUENTIAL MISS.** `shortest path` with a literal space cannot match `shortest-path` or `shortest **relative** projective path`. That single token cost an entire ADOPTED rule bearing a geodesic structure on the record's own cell. |
| **FL-4** | **THE RECORD'S OWN CELL CARRIES MORE THAN INCIDENCE — BUT EVERYTHING IT CARRIES IS ADOPTED, SUPPLIED-IN-BRANCH, OR IMPORTED.** Shortest/geodesic projective path: **adopted, three separate flags saying not derived**. Flat Lorentzian diamond class: **SUPPLIED IN DECLARED BRANCH**. The Fubini-Study path-length bound: **from an imported theorem**. Nothing here is derived from the record. |
| **FL-5** | **THE FOUR-CARRIER FINDING IS STRONGER THAN THE SUBJECT MADE IT.** A third absence statement — *"no map from primitive-incidence data to tip pair or equivalent diamond carrier is displayed \| ABSENT"* — names both carriers directly and sits in the same table as the diamond class the subject missed. |
| **FL-6** | **QUOTATION INTEGRITY FAILED ONCE, IN A LOAD-BEARING PLACE.** COR-C: a would-build instruction from a `CONSTRUCTIBLE_WITH_ROUTE` row, paraphrased, uncited, attributed to a ruling that does not contain it, and used affirmatively. The subject's SELF-AUDIT asserts every quote was re-read against its source line range; this one has no source line range. |
| **FL-7** | **TEN OF FOURTEEN REQUIRED RULINGS UNREAD.** The commission marks `DOR_*` PERMITTED AND **REQUIRED**. Four were read. Two unread ones declare supersession of the governing ruling; one adopts a further where-clause as lawful structure. I read and seal-verified all fourteen (14/14 OK). |
| **FL-8** | **FENCES INTACT IN BOTH ARTIFACTS.** No coupling, scale, root, eigenvalue, norm or constant computed or approached, here or in the subject. `1/24` in the subject is quoted, not computed — verified verbatim in source before assessment. I elided every displayed numeric prefactor and the saturation value when quoting action functionals. |
| **FL-9** | **INDETERMINATE-AT-BYTES, SAID PLAINLY.** Whether `K_amb` (carrier of the displayed `d(x,y)`) is the record's cell carrier: **the corpus does not say**. Whether the KK/record-bundle `M` is `M_G`: **the corpus does not say**. Whether the two `f = da` objects are one curvature or two: **the corpus does not say** — the subject's CANNOT-DETERMINE on this is correct and I confirm it. I identify none of them. |

---

## SELF-AUDIT

```text
REGISTER BAR OBSERVED        = true (array globs; per-pattern leak counter reported;
                                     both the subject and this audit self-excluded;
                                     supervision/ restricted to DOR_* )
DOR_* READ                   = true (ALL FOURTEEN opened and seal-verified, 14/14 OK)
SWEEP SETS OPENED            = true (BUNDLE WITH CONNECTION 4/4; intrinsic-curvature 2/2;
                                     distance 11/11; diamond 9/9; shortest- 24 contexts;
                                     EH-family 6/6 displays)
UNOPENED MEMBERS DECLARED    = true (SWEEP CUTOFFS, final paragraph)
QUOTES CHECKED FOR WRAPS     = true (every displayed quote re-read against its source
                                     line range; adverse clauses carried whole, including
                                     ones adverse to my own corrections)
SUBJECT SEALS RE-RUN         = true (both sidecars OK; subject's own cited-source seals
                                     independently re-verified, count corrected)
AUTHORING                    = none
ADVOCACY                     = none
ADOPTION                     = none
CATALOGUED NEGATIVES RE-READ = none
NUMERIC EVALUATION           = none
MAGNITUDE APPROACHED         = false
EXTERNAL LITERATURE          = none introduced
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
