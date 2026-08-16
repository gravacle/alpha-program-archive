# STAGE 8 — DOES THE BASE CARRY GEOMETRY? — BUILD LANE — O48SR V001

Commission: read-and-classify audit at bytes. Two-level question: the sealed ADOPTED
ruling types local field members as a U(1) BUNDLE WITH CONNECTION **over the record
surface**. `f = da` is the curvature of the connection — the fiber side. This audit asks
whether the BASE carries geometric structure of its own.

Lane: BUILD. Nothing authored, nothing adopted, nothing advocated. No numeric value of any
coupling, scale, root, eigenvalue, norm or constant computed or approached.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

---

## HEADLINE

```text
Q1  BASE/FIBER SEPARATION            = SEPARATION-REAL
Q2  CURVATURE CENSUS                 = FIBER/CONNECTION 12 | BASE 2 | CANNOT-DETERMINE 1
Q3  DOES THE BASE CARRY GEOMETRY     = PARTIAL
Q4  PROVENANCE                       = mixed: 1 DERIVED, 2 ADOPTED, 5 ENTERED, 3 NAMED-ONLY
      CONTENT-DEPENDENCE OF BASE STRUCTURE = NONE. Fixed independently of what the
      record contains, and one sealed theorem excludes state-dependence by name.
Q5  FIBER DEPENDS ON BASE            = FIBER-DEPENDS-ON-BASE (admissibility), with the
      primitive fiber-side objects (`f = da`, `W_n(gamma)`, `c_1`) defined without any
      base structure beyond smooth/differentiable structure and incidence.
```

**The one-sentence answer to the core question.** The base is **not** bare incidence — it
carries a coframe, a positive density, a forced intrinsic cell volume, an orientation, a
dimension, and (in the disclosed ordinary branch) a full Lorentzian metric with proper
time, normal geodesics, parallel transport into itself, and an extrinsic curvature. But
the base that carries all of that is a **smooth carrier** (`M_G` / `M_K` / `Sigma`), and
the corpus does **not** connect it at bytes to the record's own cellular incidence object
(`K`, `BareRec_2`), which carries cells, faces, incidence, orientation and a root and
nothing more. **The geometry and the record sit on two different bases, and the arrow
between them is an open gap of record in both directions.**

---

## CHOICE LEDGER

| # | Choice | Disposition |
|---|---|---|
| 1 | "Base" read as the object the ruling's phrase `over the record surface` denotes — i.e. `M_G` in `pi_G:P_G->M_G` | FORCED by `WHERE :243-248`, which introduces `pi_G:P_G->M_G` immediately under the heading of the adopted field law |
| 2 | `M_G` identified with the DoR-015 surface family | AT BYTES: `WHERE :186` `"In the equal-dimensional DoR-015 surface family"`, and `WHERE :82` pins that object by hash `7ecf04e9…`, which I verified equals `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md` |
| 3 | The vendored `.proof_deps/sympy` tree excluded from all sweeps | Third-party library source, not sealed record artifacts. It was the sole source of hits for `geodesic`, `shortest path`, `Regge`, `Ricci`, `straight line` on the first pass. Excluded and counted separately in SWEEP CUTOFFS |
| 4 | Workspace/cleanroom mirror pairs deduplicated by basename | Byte-identical mirrors; counting both would double every tally |
| 5 | BID V011 quoted from the **sealed packet member** `aa7c6d49…`, not the top-level workspace copy `20a3a17d…` | The two differ (123 diff lines). I verified every span I quote is byte-identical between them; the divergence is confined to the §A32 holdout-freeze subsection, which I do not quote |
| 6 | I did NOT identify the DoR-020-A1 bundle with [LPRB]'s bundle or with the BID discrete connection | Neither names the other. Same disposition as the prior O41SR audit. Reported as separate objects throughout |
| 7 | `s_G(c,d)=g_A4(u_c,u_d)` (DoR-019 "carrier metric") classified as CARRIER, not BASE | Its arguments are cycles `c,d in ker(B_G^T)`, not points or cells of the surface. Stated explicitly in Q3 rather than silently dropped |
| 8 | Four distinct base-like objects reported separately rather than merged | The corpus itself refuses the merge (Q3 §C). Merging them would manufacture the very identification the record leaves open |

---

## IMPORT AUDIT

Every notion I rely on is defined in the corpus. Nothing external is introduced.

| # | Notion | Status | Does the finding survive without it? |
|---|---|---|---|
| I-1 | "base" / "fiber" as the two levels of `pi_G:P_G->M_G` | **CORPUS-DEFINED** — `WHERE :243-248, :259-278` displays both objects and the projection | N/A — corpus vocabulary |
| I-2 | That a U(1) bundle has a rank-1 fiber, that `c_1` is an integral class, that `d^2=0`, that a connection determines holonomy | **NOT USED.** Named here only to say no bundle-theoretic, cohomological or differential-geometric theorem is invoked | YES. Every grade rests on displayed corpus words only |
| I-3 | That a coframe/density/metric "is geometry" | **COMMISSION VOCABULARY.** The commission enumerates the structures to sweep for; I report only objects the corpus defines and quote each | YES |
| I-4 | Reading `|det e|`, `|det E|/d!`, `h^(ij)K_ij`, `-ds^2+h_s` as displayed forms | **MINIMAL READING OF A DISPLAYED FORM.** Nothing evaluated; no value computed; no identity applied | YES |
| I-5 | Ordinary English audit vocabulary ("stratum", "provenance", "admissibility") | **COMMISSION VOCABULARY** | YES |

**FORBIDDEN IMPORTS: NONE USED.** No external literature. No theorem about bundles,
connections, curvature, metrics or complexes. Naming an object a curvature licensed no
conclusion about it anywhere in this artifact. No `ell_P`, no fiber proper radius, no
scale object, no measured constant, no comparison to any observed value. No numeric value
of any coupling, scale, root, eigenvalue, norm or constant was computed or approached.

---

## SEALS

`shasum -a 256 -c` run from each artifact's own directory.

```text
supervision/  (DOR_* only — the permitted set)
  DOR_020_A1_WHERE_CLAUSES_AMENDMENT_2026-08-04.md ............... OK
  DOR_019_CARRIER_METRIC_AND_UNITS_RATIFICATION_2026-08-03.md .... OK
  DOR_020_CONTINUUM_PACKAGE_CONDITIONAL_RATIFICATION_2026-08-04.md OK
  DOR_018_N_MEMBER_JETS_SHAPE_K_RATIFICATION_2026-08-03.md ....... OK

workspace/
  STAGE8_TASK5_EQ6_WHERE_CLAUSES_LANE2_V005.md ................... OK
  STAGE8_TASK5_EQ6_WHERE_CLAUSES_FINAL_CHECK_LANE1_V001.md ....... OK
  LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md ......................... OK
  STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md .......... OK
  STAGE8_AXN_SDN_SLICING_INSTANCE_DARIO_V003.md .................. OK
  STAGE8_B1A_CONNECTION_IDENTIFICATION_CODEX2_V001.md ............ OK
  STAGE8_B1C_DENSITY_LAYER_CODEX2_V001.md ........................ OK
  STAGE8_ETHER_CHECK_DARIO_V001.md ............................... OK
  STAGE8_7A_SIMPLICIAL_COFRAME_DARIO_V001.md ..................... OK
  STAGE8_B1A_COFRAME_HALF_DARIO_V001.md .......................... OK
  STAGE8_TASK4B_CARRIER_METRIC_AND_UNITS_PROPOSAL_LANE2_V005.md .. OK
  R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_* (9 entries) ..... 9/9 OK
  review_packets/STAGE7_QSPEC_CANDIDATE_V001/
    BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md ................ OK  (aa7c6d49…)

cleanroom/
  STAGE8_PRPS_GATE4_LOCALIZATION_BRIDGE_ATTEMPT_V001.md .......... OK

TOTAL = 26/26 OK
```

**One seal exception, disclosed.** `PRIMITIVE_RELATIVE_PHASE_CONNECTION_V001.md` — one of
the two `f = da` sources — has **no adjacent sidecar** in either root. I read it and quote
it; it is reported as UNSEALED-AT-BYTES and no grade turns on it alone (its `f = da` and
`W_n(gamma)` are duplicated in the sealed `LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md`).

**Second exception, disclosed.** `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` has no
adjacent sidecar at the top level of either root; the top-level copy hashes `20a3a17d…`.
The sealed copy is the packet member `aa7c6d49…`, which verifies OK against
`review_packets/STAGE7_QSPEC_CANDIDATE_V001/STAGE7_PACKET_MANIFEST_V001.sha256`. All five
spans I quote were checked byte-identical between the two.

---

## SWEEP CUTOFFS

Exclusion globs as an **ARRAY**: `[REGISTER, TRACKER, THE_PLAN*, ROAD_REMAINING*,
THE_HANDOFF*, OBSERVATIONS_REGISTER*, *DECISION_SHEET*, STAGE8_BASE_GEOMETRY_O48SR*]`.
The last entry is the **self-exclusion** of this artifact. Per-pattern leak counter below.
`.proof_deps/**` excluded per CHOICE LEDGER row 3 and counted separately.

| Pattern | Unique basenames | BARRED-excluded (leak counter) | `.proof_deps` excluded | Opened |
|---|---|---|---|---|
| `BUNDLE WITH CONNECTION` | 9 raw | 3 | 0 | **ALL 9** — see note below |
| `f *= *da` | 10 | 0 | 0 | all distinct definitional sites (2) |
| `metric` | 964 | 10 | 0 | line-level: every distinct 220-char match context, deduped |
| `densit(y|ies)|volume|Vol_4` | 1070 | 14 | 0 | line-level, deduped |
| `angle|inner product|orthonormal|orthogonal` | 620 | 5 | 0 | line-level, deduped |
| `curvature` | 280 | 3 | 0 | line-level, deduped |
| `parallel transport|nabla_n|Levi-Civita` | 45 | 0 | 0 | line-level, deduped |
| `geodesic|shortest path|straight` | 56 | 1 | 9 | line-level, deduped — **all 8 surviving contexts opened** |
| `angle deficit|deficit angle|angular defect|excess angle|Regge` | **0** | 0 | 2 | n/a |
| `deficit|excess at a vertex|around a face` | 27 | 1 | 0 | **all 3 match lines opened** |
| `scalar/Ricci/sectional/Gaussian/intrinsic curvature` | 2 | 0 | 4 | **both opened** |
| `distance function|metric space|d(x,y)` | 4 basenames, **0 match lines** | 0 | 3 | n/a — zero line-level hits |
| `cell weight|weights on cells|non-equivalent cells` | 10 | 0 | 0 | **all — 1 match line** |
| `no metric|metric-free|without a metric` | 18 | 0 | 0 | line-level, all opened |

**OPEN WHAT YOU COUNT — the nine-file set.** The `BUNDLE WITH CONNECTION` sweep returns
exactly nine files. A prior build is on record as having reported its size and opened none
of it. I opened all nine. Three are genuine BARRED exclusions —
`QUESTIONSSETTLED_REGISTER_V001.md` (cleanroom), `QUESTIONS_SETTLED_REGISTER_V001.md`
(supervision), and `RELAY_PASTE_570_…` (supervision, outside the `DOR_*` permission). The
remaining six are three workspace artifacts, their two cleanroom mirrors, and
`DOR_020_A1_WHERE_CLAUSES_AMENDMENT_2026-08-04.md` — **the ruling itself, inside the
sweep**. That is the exclusion the earlier build would have missed.

**Members I did NOT open, declared.** For the four large patterns (`metric` 964,
`density/volume` 1070, `angle/orthogonal` 620, `curvature` 280) I did not open every file.
I opened, instead, **every distinct match context** — each hit rendered as a 220-character
window and deduplicated across the whole corpus — which is a strictly finer instrument than
opening files, since two files sharing a sentence collapse to one context but a file with
three distinct uses yields three. Every context that named a candidate base structure was
then traced to its defining artifact and that artifact opened in full. Files whose only
match contexts were (a) gate-board lines `alpha_computed = false … no metric adopted`, (b)
negative ledgers `no metric or fiber metric`, or (c) relay custody headers, were not opened
individually. That is the complete list of what I left closed.

---

# Q1 — IS THE BASE/FIBER SEPARATION REAL AT BYTES?

## GRADE: **SEPARATION-REAL**

Both levels have distinct defining text. Quoted whole.

### The ruling

`/Users/bgm/MB Work/alpha-program-archive/supervision/DOR_020_A1_WHERE_CLAUSES_AMENDMENT_2026-08-04.md`
— seal **OK** this session — title line `:1`
`# DECISION OF RECORD 020 — AMENDMENT 1: THE WHERE-CLAUSES (ADOPTED)`, ruling line `:3`
`Principal: Brian (ruling: "Adopt the amendment")`. At `:10-15`, whole:

> "1. THE PATH/CURRENT SUPPORT CORRESPONDENCE — the law assigning currents to the
>    paths that carry them (what lives where), law-only.
> 2. THE LOCAL FIELD MEMBERS — typed as a U(1) BUNDLE WITH CONNECTION over the
>    record surface, with the bundle lift/pullback-bundle isomorphism, smooth
>    full-rank, and characteristic-class compatibility; transport derived from
>    the declared members. Law-only."

Its adopted text is pinned at `:17-19`: `STAGE8_TASK5_EQ6_WHERE_CLAUSES_LANE2_V005.md`
(`19b20603…`), verified by `STAGE8_TASK5_EQ6_WHERE_CLAUSES_FINAL_CHECK_LANE1_V001.md`.
Both seal **OK**.

### THE BASE — defined

`STAGE8_TASK5_EQ6_WHERE_CLAUSES_LANE2_V005.md :243-248`, whole:

> "The base objects carry the ratified principal U(1) bundles
>
> ```text
> pi_G:P_G->M_G,
> pi_G':P_G'->M_G'.                                (B1-8)
> ```"

The base object is `M_G`. It is not a bare index set. At `:176-181`, whole:

> "1. **Smooth actual support map.**
>
>    ```text
>    f_R:M_G->M_G' is a proper smooth map whose restriction to the old
>    physical image has full rank dim(M_G).         (B1-4)
>    ```"

and at `:183-186`, whole, including its adverse clause:

> "In the equal-dimensional DoR-015 surface family it is a local
> diffeomorphism on that image; the embedded horn requires a proper
> embedding.  The same-carrier attachment horn is `f_R=id` on the old
> image, not a separate law."

So `M_G` carries: a **dimension** (`dim(M_G)`), a **smooth structure** (`proper smooth
map`, `local diffeomorphism`, `d f_R` has a rank), and membership in a named **surface
family**. `WHERE :82` pins that family by hash — `field signature V005 / DoR-015 object |
7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12 | U(1)-bundle surface
family, paths, currents, fields`. I verified that hash: it is
`STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md`, whose A1 row `:431` reads, whole:

> "| A1 | unchanged full globally hyperbolic oriented Lorentzian U(1)-bundle family |
> nonsmooth causal locale; fixed member; Euclidean family | preserves the V003 external
> family without selecting it | family empty or raw-G signature mismatch |"

### THE FIBER — defined

`WHERE :259-277`, whole:

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

`P_G` is a distinct object with its own dimension `dim(P_G)`, carrying a right U(1) action
`p -> p z`, and mapping onto `M_G` by `pi_G`.

### THE CONNECTION — defined

`WHERE :315-325`, whole:

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

### Why this is SEPARATION-REAL and not a form of words

The final sentence of `(B1-15)` is the decisive byte. The ruling does not merely *name* two
levels; it makes the distinction **failure-capable**. A symbol that lives only on the base
(`f_R^*A_G'`) is expressly declared **not** a connection and **forbidden**. `WHERE :655`
records this as the delta against the prior version: `| bare f_R^*A | forbidden; replaced
by bundle lift/pullback-bundle isomorphism |`. A nominal two-level structure cannot forbid
a base-only symbol, because it has no base-only symbol to forbid.

The separation is further enforced by two independent tests keyed to different levels:
`(B1-4)` `rank(df_R) = dim(M_G)` on the base, `(B1-10)` `rank(d tilde_f_R) = dim(P_G)` on
the total space. `WHERE :433-444` installs both — `SMOOTHNESS_TEST = INSTALLED`,
`FULL_RANK_TEST = INSTALLED` — and the falsifier `:616-618` reads, whole:

> "3. **Rank defect.**  If `df_R` or `d tilde_f_R` loses required rank, the
>    coframe/field pullback is degenerate and the tuple is rejected."

**The adverse clause, carried whole.** The separation is real *as typing*; it is not
inhabited. `WHERE :37-39`:

> "V005 is a clause artifact, not an inhabitant.  It defines two admissibility
> laws.  Each law may have no members.  DoR-020's certified joint `[EQ6]`
> witness remains the only object authorized to prove joint inhabitance."

and `:381-385`: `W4_LOCAL_FIELD_LAW = LAW_ONLY / BUNDLE_TYPED`,
`W4_ADMISSIBLE_SET_MAY_BE_EMPTY = true`. And DoR-020 itself
(`DOR_020_CONTINUUM_PACKAGE…:26-27`) is `RATIFIED CONDITIONALLY`, `CONDITIONAL on
nonemptiness of the joint J1-J15 equalizer`.

`SEPARATION-REAL` therefore means: **two distinct objects with distinct defining text,
distinct dimensions, distinct rank tests, and an enforced prohibition against collapsing
them — inside a law that may be empty.**

---

# Q2 — CURVATURE CENSUS, SORTED BY SIDE

Every curvature-shaped object found: derivative of a connection, field strength, two-form,
holonomy around a closed loop, defect around a cycle, or failure of a transport to return
what it started with.

## FIBER / CONNECTION SIDE — 12

| # | Object | Definition, quoted | Source |
|---|---|---|---|
| F-1 | `f` | `f\|U_i = d a_i` — "Thus a connection on the projective record bundle is required by the adopted local covariant-comparison clause. Its curvature … is globally defined because `d^2 theta_ij = 0`." | `LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md :72-79` |
| F-2 | `f` | `f = da`, displayed inside `D z_1 = (d - i a) z_1, a -> a + d theta, f = da` — "A comparison connection `a` is therefore required" | `PRIMITIVE_RELATIVE_PHASE_CONNECTION_V001.md :89-95` (UNSEALED) |
| F-3 | `W_n(gamma)` | "For a closed comparison path `gamma`, the primitive integer character gives `W_n(gamma) = exp(i n integral_gamma a), n in Z.`" | `LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md :83-88` |
| F-4 | `W_n(gamma)` | "Its Wilson character `W_n(gamma) = exp[i n integral_gamma a]` is the compact parallel comparison of the primitive action phase." | `PRIMITIVE_RELATIVE_PHASE_CONNECTION_V001.md :97-104` (UNSEALED) |
| F-5 | `F_G' = Curv(A_G')` and `eta_curv,R` | "5. **Curvature and characteristic form.**  With `F_G'=Curv(A_G')`, define `eta_curv,R(F_G'):=tilde_f_R^*F_G'.   (B1-16)`" | `WHERE :327-331` |
| F-6 | curvature naturality | "Naturality gives `eta_curv,R(Curv(A_G')) =Curv(eta_conn,R(A_G')).   (B1-17)`" | `WHERE :333-338` |
| F-7 | `c_1(P_G)` | "2. **Characteristic-class discipline.**  Membership requires `c_1(P_G)=f_R^*c_1(P_G') in H^2(M_G;Z).  (B1-12)`" — a class **of the bundle**, valued in base cohomology | `WHERE :279-283` |
| F-8 | Chern–Weil form | "At the de Rham level, the sealed U(1) Chern--Weil class of `F` represents the real image of `c_1`" | `WHERE :340-343` |
| F-9 | `F_BR(mu,nu)` | "The oriented base-point holonomy and its traceable curvature are then …" — face holonomy of the discrete unitary connection `U_e`; "Reversing the face orientation sends `F_BR(mu,nu)` to …" | `BID V011 (aa7c6d49…) :891-902` |
| F-10 | face holonomy admissibility | "No flatness around a filled two-cell is imposed. … it is deliberately called a discrete unitary connection, because nontrivial face holonomy must remain admissible." | `BID V011 :301-304` |
| F-11 | `xi' = d_1 a'` | "I7 \| **Incidence compatibility.** The lifted connection must remain compatible with `d_1`, incidence signs, and the subdivision chain/cochain relation, so refined curvature is `xi'=d_1 a'` and total flux commutes with refinement." | `STAGE8_B1A_CONNECTION_IDENTIFICATION_CODEX2_V001.md :121` |
| F-12 | `PT_A(gamma_e)` | "`PT_A(gamma_e) I_(s,p) = I_(t,p) multiplication_by(h_e(A,p)).`" — transport along an edge path, failure to close measured by `h_e` | `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md §8` |

Every one of these twelve is built from `a`, `A`, `U_e`, or `P_G` — connection data on the
fiber. None consumes a base metric, distance, angle or volume in its **definition**.

## BASE SIDE — 2

| # | Object | Definition, quoted whole | Source |
|---|---|---|---|
| **B-1** | **extrinsic curvature `K_ij`** and **mean curvature `H`** | "**Convention adopted as part of the entered authorship** (SD-N's route field explicitly asks the entry to author it, so this consumes no freedom beyond the entry): signature `(-,+,+,+)`; `n` future-directed with `<n,n> = -1`, so `slash(n)^2 = -1`; extrinsic curvature `K_ij := (1/2) d_s h_ij` with mean curvature `H := h^(ij) K_ij`." | `STAGE8_AXN_SDN_SLICING_INSTANCE_DARIO_V003.md :98-101` |
| **B-2** | **the base's own affine transport and its flatness along `n`** | "With `N = 1` and `beta = 0` the metric on the scope takes Gaussian normal form `g = -ds^2 + h_s`, and `d/ds = n` exactly. The normal curves are geodesics, `nabla_n n = 0`." / "2. Extend along the flow by parallel transport: `nabla_n e_a = 0`. 3. Parallel transport preserves the metric, so the frame stays orthonormal on every `Sigma_s`; and because `nabla_n n = 0`, the transported `e_0` **remains the unit normal** of `Sigma_s`." | `STAGE8_AXN_SDN_SLICING_INSTANCE_DARIO_V003.md :103-104, :110-114` |

B-1 is a genuine base-side curvature: it is a comparison of the induced metric `h_ij` at
nearby slices, defined from base data only, with no fiber and no `a` anywhere in it. B-2 is
a connection **of the base into itself** — `nabla` acting on frame vectors `e_a`, not on a
U(1) fiber — and its statement `nabla_n n = 0` is a flatness-along-the-flow statement about
the base.

**No Riemann, Ricci, scalar or sectional curvature of the record surface exists anywhere in
the corpus.** The sweep for those terms returned exactly two record artifacts, and both
were opened. Neither supplies one. The only substantive hit reads, whole:

> "he fiber itself | Principal circle / pure circle EH branch | no term; one-dimensional
> circle has no intrinsic curvature potential in the sealed reduction |
> `pure_circle_curvature_potential = false | TYPE-R | test: pure circle EH generates …"

— which is a **negative** about the *fiber*, not a base curvature.

**No angle deficit, vertex excess, or face defect exists.** The pattern
`angle deficit|deficit angle|angular defect|excess angle|Regge` returned **0** record hits
(2 hits, both in the excluded vendored library). The broader `deficit|excess at a vertex|
around a face` returned 27 files whose 3 distinct match lines I opened in full: all three
are bookkeeping deficits ("collapsed line 6's remaining deficit to ONE NAMED DATUM: the
slicing"; "a false merge here understates the deficit"; "the honest deficit for line 6's
source third is TWO obstructions"). **None is geometric.**

## CANNOT-DETERMINE — 1

| # | Object | Why undecided |
|---|---|---|
| X-1 | `f = da` in `PRIMITIVE_RELATIVE_PHASE_CONNECTION_V001.md`, whether it is the same object as F-1 | The two artifacts derive the same displayed form on different carriers (one from the projective record carrier, one from the two-alternative comparison record) and **neither names the other**. Whether they are one curvature or two is INDETERMINATE-AT-BYTES. Counted once on the fiber side in both cases, so the side-tally is unaffected |

## TALLY BY SIDE

```text
FIBER / CONNECTION SIDE .... 12
BASE SIDE ..................  2   (B-1 extrinsic + mean curvature; B-2 base affine transport)
CANNOT-DETERMINE ...........  1   (an identity question, not a side question)
```

**Both BASE-side objects live in the same artifact, on the disclosed ordinary-branch
spacetime, and both are marked ENTERED by that artifact's own words.** Neither is a
curvature of the record's cellular object. See Q3 §C.

---

# Q3 — DOES THE BASE HAVE GEOMETRIC STRUCTURE? — THE CORE

## GRADE: **PARTIAL**

Stated flatly and without softening: **the base is not bare incidence.** It carries a
coframe, a positive density, a forced intrinsic cell volume, an orientation, a dimension,
and — in the disclosed ordinary branch — a full Lorentzian metric with an inner product, a
proper-time distance, normal geodesics, parallel transport of the base into itself, and an
extrinsic curvature. Each is quoted below.

But the grade is PARTIAL, not BASE-CARRIES-GEOMETRY, for a reason the corpus states itself:
**the object carrying the geometry and the object carrying the record are not the same
object, and the arrow between them is missing in both directions.**

## §A — WHAT IS PRESENT, ITEMIZED WITH DEFINITIONS QUOTED

### A metric, an inner product, and an angle

`STAGE8_AXN_SDN_SLICING_INSTANCE_DARIO_V003.md :98-104`, whole:

> "**Convention adopted as part of the entered authorship** (SD-N's route field explicitly
> asks the entry to author it, so this consumes no freedom beyond the entry): signature
> `(-,+,+,+)`; `n` future-directed with `<n,n> = -1`, so `slash(n)^2 = -1`; extrinsic
> curvature `K_ij := (1/2) d_s h_ij` with mean curvature `H := h^(ij) K_ij`.
>
> With `N = 1` and `beta = 0` the metric on the scope takes Gaussian normal form
> `g = -ds^2 + h_s`, and `d/ds = n` exactly. The normal curves are geodesics,
> `nabla_n n = 0`."

An inner product with signature; an induced slice metric `h_s`; its inverse `h^(ij)`. And
at `:110-113`, an **orthonormal frame** — hence an angle:

> "1. Choose any orthonormal frame `(e_1,e_2,e_3)` on `Sigma_0` and set `e_0 := n`."

At the microscopic principle, `BID V011 :813-819`, whole:

> "```text
> S = C^4,
> {gamma^mu,gamma^nu} = 2 eta^(mu nu) I,
> eta = diag(+1,-1,-1,-1),
> sigma^(mu nu) = (i/2)[gamma^mu,gamma^nu],
> Tr_S(I) = 4.
> ```"

and `:1029-1034`, whole:

> "Raise indices only with
>
> ```text
> eta = diag(+1,-1,-1,-1),
> F_BR^(mu nu) = eta^(mu rho) eta^(nu sigma) F_BR(rho,sigma).
> ```"

A **flat** Lorentzian metric, used to raise indices.

### A distance

`SDN V003 :94-95`, whole:

> "FIELD 6  normal-parameter    : s is proper time along the normal geodesics,
>          normalization         s|_(Sigma_0) = 0, d/ds = n, <n,n> = -1 in the signature
>                                convention adopted below"

**Proper time along the normal geodesics** is a distance on the base. Note the exact shape
of this: it is a distance *along a distinguished flow*, not a metric-space distance
function between arbitrary points. The sweep for `distance function|metric space|d(x,y)`
returned **zero line-level matches in the record corpus.** No `d(x,y)` exists.

### A geodesic and a notion of straightness

`SDN V003 :88-89`, whole:

> "FIELD 2  hypersurface family : Sigma_s := exp_perp(Sigma_0 x {s}), the image of Sigma_0
>                                under normal geodesic flow at parameter s, on the scope of
>                                field 8"

and `:104`: `The normal curves are geodesics, nabla_n n = 0.`

### Parallel transport of the base into itself

`SDN V003 :111-113`, whole:

> "2. Extend along the flow by parallel transport: `nabla_n e_a = 0`.
> 3. Parallel transport preserves the metric, so the frame stays orthonormal on every
>    `Sigma_s`; and because `nabla_n n = 0`, the transported `e_0` **remains the unit
>    normal** of `Sigma_s`. The frame is therefore adapted at every `s` without a second
>    choice."

This is transport of **base** frame vectors by a **base** connection `nabla`. It is not the
U(1) connection and does not mention `a`, `A` or `P_G`.

### A curvature of the surface

`K_ij := (1/2) d_s h_ij`, `H := h^(ij) K_ij` — quoted in full above and as Q2 B-1.

### A coframe

`WHERE :302-310`, whole:

> "3. **Coframe and density.**  `f_R` has full rank on the old image, so
>    pullback of the target coframe is nondegenerate there.  With the admitted
>    frame-torsor intertwiner carried family-wide,
>
>    ```text
>    e_G = f_R^* e_G' on the old image,
>    mu_G=f_R^*mu_G' on the old image,              (B1-14)
>    ```
>
>    and `mu_G'` is positive.  `Cof_R` and `Dens_R` are the induced operators
>    in the already declared R4 unit classes.  Their duality square commutes;
>    no scale or frame is selected."

`e_G` is a coframe field on `M_G`, pulled back along a **base** map `f_R` with no `iota_R`
in sight — the one place the where-law permits a bare base pullback, precisely because it
is a base object.

### A volume, a measure, and a weight that makes cells non-equivalent

`STAGE8_B1A_CONNECTION_IDENTIFICATION_CODEX2_V001.md :123`, whole:

> "| I9 | **`Vol_4` compatibility.** The transported curvature must make the child-cell
> quadratic `Vol_4(C) sum F^2` natural under refinement, with `Vol_4` evaluated
> intrinsically on boxes and simplices. | D4's exact linear/quadratic split; D5's forced
> `Vol_4(C)` rule. |"

and the cell weight itself, the single match in the whole corpus for a per-cell weighting:

> "The cell weight is the forced intrinsic `Vol_4(C)`: `|det e|` on parallelepipeds and
> `|det E|/d!` on simplices."

**Cells are therefore not equivalent to one another.** A parallelepiped cell weighs
`|det e|`; a simplex cell weighs `|det E|/d!`. In the sealed exhibit, `Vol_4(C_p) =
|det E_p|/4! = 1/24` while an A0 cell has `Vol_4 = 1`. This is a genuine non-uniform
weighting on the cell set, and it is derived, not stipulated per cell.

The measure itself is a sealed theorem.
`R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md :5-19`, whole:

> "## Verdict
>
> ```text
> GLOBAL_INTRINSIC_FLAT_CELL_MEASURE_CLASSIFIED
> ```
>
> Within the predeclared class A1-A4, the intrinsic probability measure on a
> flat primitive causal diamond is uniquely
>
> ```text
> mu_D(A) = Vol_4(A) / Vol_4(D).
> ```
>
> This is a global classification under the stated assumptions, not merely a
> test of the earlier `1+a u_D` family."

with `:116` `uniform_flat_cell_measure_derived = true`.

### An orientation

`BID V011 :287-292`, whole:

> "where `K` is a finite oriented regular CW complex of dimension at most two,
> each connected component carries zero or one distinguished root `r`, `L`
> assigns a one-dimensional Hermitian fiber to every vertex, and `U` is the
> discrete unitary connection below. The first-opening object has exactly one
> root. Rootless objects are retained so every elementary cell has a test
> inclusion."

and `BID V011 :1556` `epsilon_0123=+1`.

## §B — WHAT IS ABSENT

| Swept-for structure | Result |
|---|---|
| a metric-space **distance function** on the record's own points/cells | **ABSENT.** `distance function|metric space|d(x,y)` → 0 line-level record hits |
| **angle deficit / vertex excess / face defect** (discrete curvature) | **ABSENT.** 0 record hits on the specific pattern; all 3 lines of the broad pattern opened and all are bookkeeping deficits |
| **Riemann / Ricci / scalar / sectional / Gaussian curvature of the record surface** | **ABSENT.** 2 record hits, both opened; the substantive one is a *negative about the fiber* |
| a **curvature of the base** beyond the extrinsic `K_ij` of a slice | **ABSENT.** No intrinsic curvature of `M_G`, of `K`, or of `Sigma` is defined anywhere |
| **curved cells** | **EXPRESSLY OUT OF SCOPE.** `R3.3 :107-109`, whole: *"Singular measures, curved cells, and state-dependent measures with a supplied preferred covector remain outside this theorem."* |
| an **intrinsic length scale for the record** | **ABSENT — and it is the program's registered blocker.** The conversion from internal record geometry to external length is the beta gap: *"The spec defines the target as a same-cell map from internal/projective record geometry to external/Lorentzian length normalization, equivalently a determination of `beta`"* — status PRE-CANDIDATE SPECIFICATION AUTHORED, i.e. not built |
| a **non-uniform weighting on the microscopic cells** | **ABSENT AT THAT STRATUM, AND ONLY HYPOTHESISED.** See §B.1 |

### §B.1 — the microscopic stratum weights all cells alike, and even that is a hypothesis

`BID V011 :483-505`, whole, including its adverse clauses:

> "1. `C_0`, `C_1`, and `C_2` are pairwise orthogonal grading sectors;
> 2. distinct elementary cells of the same degree are orthogonal;
> 3. disjoint union maps to orthogonal Hilbert direct sum;
> 4. every closed-cell map `j_c` is an isometry on its top-cell generator;
> 5. the unique top-cell generator of every `bar(c)` has norm one in
>    dimensionless record-counting units; and
> 6. every bare incidence-preserving cell relabeling is unitary.
>
> These conditions include roots, undecorated/decorated edges after applying
> `U`, and two-cells through their elementary-cell maps. A root-specific norm,
> a handle-specific edge norm, and a face-specific counting weight are not left
> free. If consistent, they force:
>
> ```text
> M_0(K) = I,
> M_1(K) = I,
> M_2(K) = I
> ```
>
> in the elementary cell bases. This is a new physical hypothesis, not a
> result inherited from the action character. Gate 3 must classify coherent
> Hilbert functors starting from all positive-definite forms and prove whether
> one unitary equivalence class survives."

Read this exactly. At the microscopic stratum the inner product on the cell carriers is
forced to the **identity**: every cell has norm one, distinct cells are orthogonal. That is
a counting structure — it distinguishes **no** cell from any other. And it is explicitly
**"a new physical hypothesis, not a result"**, with Gate 3 open. `:509-513` adds, whole:

> "A compensating positive basis/measure rescaling is
> not an equivalence; it changes the physical Hilbert operator and remains in
> the competitor audit. The sole nonunitary exception is rescaling the
> public-closure **constraint covector** by a nonzero scalar, which leaves its
> kernel unchanged and is never used to normalize a Hilbert operator."

The corpus also records that imported metrics at this stratum have been actively **killed**
— `BID V011 :65` lists among the defects repaired: *"an imported Fubini-Study metric
described with an invalid passive-symmetry"*, and `:21-23`: *"a rooted-star and equal-weight
assumption hidden in the inputs; an incomplete weighted family; an undefined naturality
condition and Hilbert metric"*.

`STAGE8_TASK5_EQ6_WHERE_CLAUSES_LANE2_V005.md :607` records the same discipline as a
permanent regression: *"| Hodge from isometry | **PASS** — no Hodge or bundle existence
inferred from the metric |"*.

## §C — THE DECISIVE STRUCTURAL FACT: FOUR BASES, NOT ONE

This is why the grade is PARTIAL and not BASE-CARRIES-GEOMETRY. The corpus carries **four
distinct base-like objects**, and does not identify them with one another.

| | Object | What it carries | Status |
|---|---|---|---|
| **BASE-1** | `M_G` in `pi_G:P_G->M_G` — the DoR-015 "globally hyperbolic oriented Lorentzian U(1)-bundle family" | dimension, smooth structure, orientation, Lorentzian typing, coframe `e_G`, positive density `mu_G` | **LAW-ONLY. `W4_ADMISSIBLE_SET_MAY_BE_EMPTY = true`. No member exhibited.** |
| **BASE-2** | the `Ref_a` finite cell carrier (A0/A1/A2 and composites) | derived child coframes, `\|det E_p\| = 1`, forced intrinsic `Vol_4(C)` cell weight, the uniform flat-cell measure | coframe half **derived**; density receiver `R4Dens` **OPACITY-BOUND**, `SUPPLIED = 0` |
| **BASE-3** | `K` in `BareRec_2 = (K,r,L,U)` | *"a finite oriented regular CW complex of dimension at most two"*, roots, incidence, orientation — **and nothing else** | cell weights `M_p = I` are a **hypothesis**, Gate 3 open |
| **BASE-4** | `Sigma` / `Sigma_s` in the disclosed globally hyperbolic spin spacetime | metric `g = -ds^2 + h_s`, `h^(ij)`, orthonormal frame, proper time, normal geodesics, `nabla`, parallel transport, `K_ij`, `H` | **ENTERED** — see Q4 |

**BASE-3 is bare incidence plus orientation and a root.** If the question is asked of the
record's own cellular object, the answer is: cells, faces, adjacency, ordering, orientation,
one root — and a cell inner product that is hypothesised to be the identity and therefore
distinguishes nothing.

**The bridges between these are open of record, in both directions.**

Forward (cells → smooth carrier), `STAGE8_B1C_DENSITY_LAYER_CODEX2_V001.md :105`, whole:

> "The record displays two nearby but non-identical things: the target-independent `Ref_a`
> cellular generator grammar, and the older `PathRel_adm` **law** for a physical local map.
> It does not display the conversion between them. WHERE `[6510,9332)` expressly allows the
> admissible physical-path set to be empty and records the law as proposed/not adopted. INC
> `[3953,7622)` supplies coordinate incidence/aggregation data for A0/A1/A2, but a
> coordinate cellular refinement is not by itself a map of the physical path carriers
> `M_K`. Treating the barred same-smooth-coframe constituent as that map would violate S26.
> The missing sealed object is:
>
> ```text
> one nonempty, content-addressed PathRel_adm(g) realization for every licensed
> Ref_a generator, or a sealed functor converting the Ref_a cellular arrow to
> the older actual-path arrow.
> ```"

— classified `f_g` **UNDECIDABLE**, and the layer's board reads `SUPPLIED = 0`.

Reverse (smooth carrier → cells),
`STAGE8_PRPS_GATE4_LOCALIZATION_BRIDGE_ATTEMPT_V001.md :185-195`, whole:

> "The reverse direction is worse typed for the present task. A Gate-4 finite
> edge-transport assignment does not canonically reconstruct a smooth principal
> bundle with connection on a patch cover. Many smooth connections and covers
> can restrict to the same finite edge data, and a tree has no loop holonomy or
> plaquette carrier with which to constrain curvature.
>
> ```text
> reverse_discrete_to_smooth_bridge_canonical = false | TYPE-U |
> would-build: a canonical reconstruction theorem from the BID incidence graph
> and Gate-4 transport class to a smooth PRPS endpoint-comparison bundle with
> patch overlaps, including uniqueness modulo the PRPS smooth redundancy.
> ```"

## §D — THE STRUCTURE THE COMMISSION NAMED THAT IS *NOT* BASE GEOMETRY

DoR-019 is titled **THE CARRIER METRIC AND UNITS (RATIFIED)** and its derived core opens
with `the forced pullback semiform s_G(c,d) = g_A4(u_c, u_d)`. The word "metric" in a
ratified ruling title is exactly the seduction this commission warned about, so I state
what it is at bytes: `c` and `d` are **cycles**, `c,d in ker(B_G^T)`, and `u_c` is the
conserved current attached to the cycle. It is an inner product on the **current/cycle
carrier**, not on points or cells of the surface. DoR-019's own ruling text calls its
positive-definiteness a statement about *"the FULL carrier"*, and lists among its four
**AUTHORED** items *"the A4 automorphism isometry (beyond W3's reach)"*.

**This is a carrier structure, not a base structure, and it is not counted in §A.**

## §E — GRADE STATEMENT

```text
Q3 = PARTIAL

PRESENT on a base:  dimension; smooth structure; orientation; coframe; positive density;
                    forced intrinsic cell volume Vol_4 (a weight making cells
                    non-equivalent); a uniquely classified uniform flat-cell measure;
                    a Lorentzian metric and inner product; an orthonormal frame (angle);
                    proper-time distance along a distinguished flow; normal geodesics;
                    parallel transport of the base into itself; extrinsic and mean
                    curvature of a slice.

ABSENT everywhere:  a distance function d(x,y); any angle deficit / vertex excess /
                    face defect; any Riemann, Ricci, scalar or sectional curvature of
                    the record surface; curved cells (expressly out of scope); an
                    intrinsic length scale for the record (the beta gap).

AND:                the base carrying the geometry (BASE-1/2/4) is not the base carrying
                    the record's incidence (BASE-3), the corpus does not identify them,
                    the forward bridge is UNDECIDABLE with SUPPLIED = 0, and the reverse
                    bridge is sealed false.
```

If the question is *"does the record's own cellular object carry more than incidence?"* the
answer at bytes is: **orientation and a root, and otherwise no** — its cell weights are the
identity by hypothesis, and Gate 3 has not classified them. If the question is *"does the
smooth carrier the ruling names as the base carry geometry?"* the answer is: **yes, a great
deal, and almost all of it entered rather than derived.**

---

# Q4 — WHAT FIXES EACH STRUCTURE?

| Structure (Q3 §A) | Provenance | What decides it, quoted |
|---|---|---|
| Smooth structure, `dim`, `3+1`, Lorentz signature, spin, CPT | **ENTERED** | `BID V011 :821-824`, whole: *"The `3+1` spacetime dimension, Lorentz signature, spin structure, CPT framework, and resulting four-component complex Dirac module are disclosed ordinary-branch inputs. BID does not derive them, and the number four in this spinor trace is not counted as target-blind evidence for alpha."* |
| The Lorentzian surface family (BASE-1's typing) | **ENTERED / AUTHORED** | `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md :431`: *"A1 \| unchanged full globally hyperbolic oriented Lorentzian U(1)-bundle family"* — **"unchanged"**, i.e. carried in. The lineage's own self-description: *"FIELD_SIGNATURE_PHYS V001 complete — nine fields, openly authored (a smooth locally covariant 3+1 Lorentzian background family + incidence realization, claiming NO derivation)"* |
| `eta = diag(+1,-1,-1,-1)`, `epsilon_0123 = +1` | **ENTERED (frozen)** | `BID V011 :1553-1557`, whole: *"Freeze the ordinary-branch inputs `eta=diag(+1,-1,-1,-1),  epsilon_0123=+1, (*F)_(mu nu)=(1/2)epsilon_(mu nu rho sigma)F^(rho sigma).`"* |
| Metric `g = -ds^2 + h_s`; `N=1`; `beta=0`; proper time; normal geodesics; `nabla_n e_a = 0`; `K_ij`; `H` | **ENTERED** | `SDN V003 :92-101`: `FIELD 4  N = 1 : entered`, `FIELD 5  beta = 0 : entered`, and *"**Convention adopted as part of the entered authorship** (SD-N's route field explicitly asks the entry to author it, so this consumes no freedom beyond the entry)"*. Its own board `:213`: *"All three steps are determined by the entered SD-N data plus sealed `g`, `a` and 916; none selects."* |
| The orthonormal frame on `Sigma_0` | **ENTERED (free choice, no selection)** | `SDN V003 :110`: *"Choose any orthonormal frame `(e_1,e_2,e_3)` on `Sigma_0`"* — and `:114` *"The frame is therefore adapted at every `s` without a second choice."* |
| Coframe `Cof_R` (`e_G = f_R^* e_G'`) | **ADOPTED** | `DOR_020_A1 :12-15` adopts the field law; `WHERE :302-310` is its clause 3. Its status is **membership law**, not a member: `W4_ADMISSIBLE_SET_MAY_BE_EMPTY = true` (`WHERE :383`) |
| Density `Dens_R` (`mu_G = f_R^* mu_G'`, `mu_G'` positive) | **ADOPTED** | same ruling, same clause; *"and `mu_G'` is positive.  `Cof_R` and `Dens_R` are the induced operators in the already declared R4 unit classes.  Their duality square commutes; no scale or frame is selected."* |
| Forced intrinsic `Vol_4(C)` cell weight | **DERIVED** (on entered flat cells) | *"The cell weight is the forced intrinsic `Vol_4(C)`: `\|det e\|` on parallelepipeds and `\|det E\|/d!` on simplices."* |
| The uniform flat-cell measure `mu_D(A) = Vol_4(A)/Vol_4(D)` | **DERIVED** | `R3.3 :34-54`, whole: *"Poincare covariance sends this ray to itself: `rho(gx) = c(g) rho(x)`, where `c` is a continuous positive character. … Semidirect-product compatibility requires `k` to be fixed by every Lorentz transformation. The exact generator calculation has rank four on the four-dimensional covector space, so the fixed space is `{0}`. The Lorentz commutators also span the full six-dimensional Lorentz algebra, excluding a separate continuous positive Lorentz character. Thus `c=1`; `rho` is translation invariant and hence constant almost everywhere. Normalizing on each diamond gives the displayed uniform measure."* — **DERIVED from an ENTERED premise** (Poincaré covariance of a flat cell) |
| Orientation of `K`; root `r` | **ENTERED (definitional)** | `BID V011 :287-292`, quoted in Q3 §A |
| Cell inner products `M_0=M_1=M_2=I` | **NAMED-ONLY** | `BID V011 :502-505`, whole: *"This is a new physical hypothesis, not a result inherited from the action character. Gate 3 must classify coherent Hilbert functors starting from all positive-definite forms and prove whether one unitary equivalence class survives."* |
| Density members `delta_K' in R4Dens(K')`, transport `d_g` | **NAMED-ONLY** | `STAGE8_B1C_DENSITY_LAYER_CODEX2_V001.md :139`: *"The stock displays `Dens_R` as a positive current/volume-density operator dual to `Cof_R`, and 793 packages the exact predicates above. It deliberately declines to say what an element of `R4Dens(K)` is."* Board `:162-167`: `SUPPLIED = 0`, `OPACITY-BOUND = 2`. Freedoms row `:205`: *"density normalization/scale \| **NONE SELECTED**; `VolNorm` remains a predicate"* |
| Any intrinsic length scale for the record | **NAMED-ONLY (the beta gap)** | *"The spec defines the target as a same-cell map from internal/projective record geometry to external/Lorentzian length normalization, equivalently a determination of `beta`"* — status: PRE-CANDIDATE SPECIFICATION AUTHORED |

```text
DERIVED     = 1   (the uniform flat-cell measure; and Vol_4 as its evaluation rule)
ADOPTED     = 2   (Cof_R, Dens_R — as membership laws that may be empty)
ENTERED     = 5   (smooth/3+1/signature/spin/CPT; the Lorentzian family; the frozen eta;
                   the SDN metric-and-slicing package; orientation/root)
NAMED-ONLY  = 3   (M_p = I; delta_K'/d_g; the record's length scale)
```

## Does anything make the base's structure depend on the record's content?

**No. Nothing in the corpus does, and one sealed theorem excludes it by name.**

`R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md :103-109`, whole:

> "## Scope
>
> The result applies to positive absolutely-continuous intrinsic measures on
> flat primitive causal diamonds, with continuous density ray and full
> proper-orthochronous Poincare covariance. Singular measures, curved cells,
> and state-dependent measures with a supplied preferred covector remain
> outside this theorem."

**State-dependent measures are outside the theorem.** The measure it does classify is
`translation invariant and hence constant almost everywhere` — fixed by the entered
Poincaré covariance alone, with no argument slot for what the record contains.

The same holds at every other site:

- `eta = diag(+1,-1,-1,-1)` is **frozen**, not a function of anything.
- `M_0 = M_1 = M_2 = I` is **uniform across all cells** and forced (if consistent) by
  functoriality conditions that quantify over *all* objects — no cell's weight can respond
  to what that cell records.
- `Cof_R` and `Dens_R` are pullbacks along the base map `f_R`: `e_G = f_R^* e_G'`,
  `mu_G = f_R^* mu_G'`. Their values are fixed by the target's coframe and density and the
  map, with no record-content argument.
- The SDN package is `entered` field-by-field with `FREEDOM FOUND = none` (`SDN V003 :198`).

The independent hostile check reaches the same place from the other direction.
`STAGE8_ETHER_CHECK_DARIO_V001.md :176-183`, whole:

> "**(P3) `n_ch` never consumes the metric argument — CONFIRMED, and established without the
> party.** The subject rests this on member 08's assurance that the machinery import is
> *confined to the metric argument `n_ch` does not consume*. Member 08 is this lane's own prior
> output and carries a standing IMPORT-FOUND, so I did not accept that assurance. I settled it
> instead from member 02's own regression ledger, which certifies that no parent, curvature,
> distributed, source-contact, metric/continuum, state, effect, or domain datum is added to the
> construction. `n_ch` is defined from characters, C7 and C4 over that construction; there is
> no metric argument in it to consume, at any depth reachable from member 02."

and `:112-116`, whole, on what the record's own object is missing:

> "member 02 names the missing supply by name, twice — *"without an
> additional source state"* the scalarization is unlicensed, and the negative ledger records
> `State/effects/domains/contacts/metric/common-origin fields remain` as outstanding. The
> regression check in the same member confirms that no *"effect, or domain datum is added"* to
> the construction — the state is not merely unfixed, it is expressly outside the object."

**The base's geometry is fixed independently of what the record contains — completely and
without exception at bytes.**

---

# Q5 — DOES ANYTHING ON THE FIBER SIDE DEPEND ON THE BASE'S STRUCTURE?

## GRADE: **FIBER-DEPENDS-ON-BASE**

The dependency is on **admissibility**, not on value or primitive definition. Both halves
are stated precisely, and the dependencies are quoted whole.

## §A — WHERE THE DEPENDENCY IS REAL

### Two sealed interface demands bind fiber-side transport to base-side structures

`STAGE8_B1A_CONNECTION_IDENTIFICATION_CODEX2_V001.md :122-123`, both rows whole,
**including their adverse clauses**:

> "| I8 | **Coframe compatibility.** On each child cell, the connection/curvature transport
> must be expressible with the sealed child coframe, including the derived simplicial frame.
> | D1 requires the fields in one `J_ref`; the coframe artifacts establish the per-cell
> frame but no connection relation. |
> | I9 | **`Vol_4` compatibility.** The transported curvature must make the child-cell
> quadratic `Vol_4(C) sum F^2` natural under refinement, with `Vol_4` evaluated
> intrinsically on boxes and simplices. | D4's exact linear/quadratic split; D5's forced
> `Vol_4(C)` rule. |"

I8 makes a **base coframe** a condition on the expressibility of the **connection and
curvature** transport. I9 makes the **base volume** a weight on the **curvature** in the
quantity that must be natural under refinement: `Vol_4(C) sum F^2` is literally a fiber-side
curvature multiplied by a base-side cell volume. The adverse clause in I8's own right-hand
column is carried: the coframe artifacts *"establish the per-cell frame but no connection
relation"* — the demand is stated and **not met**.

### The adopted where-law makes a bundle member's admissibility turn on base coframe and density

A `FieldExt_adm(R)` member is the tuple `E_R=(e_G',mu_G',A_G',F_G',tilde_f_R,iota_R)`
(`WHERE :253-256`) — the coframe `e_G'` and density `mu_G'` are **constituents of the same
tuple** as the connection `A_G'` and curvature `F_G'`, and membership requires **all** of
clauses 1–8. Clause 3 is the coframe/density clause quoted in Q3 §A. Its failure is
failure-capable, `WHERE :621-622`, whole:

> "5. **Coframe/density mismatch.**  Failure of nondegeneracy, positivity, or
>    duality rejects the tuple."

A tuple whose base-side coframe is degenerate or whose base-side density is non-positive is
**not an admissible member**, and therefore its connection and curvature are not admitted.
That is an admissibility dependence of fiber-side objects on base-side structure, at bytes.

`WHERE :553-557` states the same in the affirmative, whole:

> "The smooth full-rank condition makes the coframe pullback nondegenerate;
> orientation compatibility preserves density positivity.  The class
> condition ensures the source and pullback target bundles lie in the same
> U(1) topological sector.  Common-refinement transport follows from
> `(B1-18)` and the clause's diamond equality."

### The Maxwell/Hodge generator takes its symbol from the base coframes

Of the six irreducible generators DoR-020 conditions the whole continuum package on, one
reads, whole:

> "B_C3_MAXWELL_HODGE (close d on the C1 carrier → spectral gap/closed range → the symbol
> from P4 coframes)"

The symbol of the Maxwell/Hodge operator — the object that would give the curvature its
quadratic form — is drawn **from the P4 coframes**, which are base-side (`Cof_R` is a P4/X4
field, `WHERE :123`).

## §B — WHERE THERE IS NO DEPENDENCY

The **primitive** fiber-side objects are defined with no base structure beyond smooth /
differentiable structure and incidence. Reading their definitions exactly:

- `f|U_i = d a_i` (`LPRB :76`) — the exterior derivative of a local one-form. No metric,
  distance, angle or volume appears in it.
- `f = da` (`PRPS :94`) — same.
- `W_n(gamma) = exp(i n integral_gamma a)` (`LPRB :86-87`) — a line integral of a one-form
  along a path. Its arguments are `gamma` (a path — incidence data) and `a`. No base
  metric enters.
- `a_j = a_i + d theta_ij` (`LPRB :69`) and `g_ij g_jk g_ki = 1` (`LPRB :37`) — patching
  and cocycle conditions. Overlap combinatorics only.
- `c_1(P_G)=f_R^*c_1(P_G') in H^2(M_G;Z)` (`WHERE :282`) — valued in the base's cohomology,
  but cohomology is not one of the structures this commission swept for, and no metric,
  volume, coframe or distance appears in the condition.
- `eta_conn,R(A_G') := tilde_f_R^*A_G'` (`WHERE :318-321`) — pullback along the **bundle**
  map, expressly *not* along the base map.
- `U_e:L_s->L_t, U_(bar e)=U_e^(-1)` (`BID V011 :297-298`) — the discrete unitary
  connection. Defined edge by edge on bare incidence.

And the charge-type quantity is settled the same way. `LPRB :90-92`, whole:

> "The primitive faithful winding is inherited conditionally as `|n|=1`. This
> establishes the normalization of the comparison character. It does not
> establish a spectrum of elementary matter particles."

`|n| = 1` follows from faithfulness of a `U(1)` character — a group-theoretic fact about
the fiber. `PRPS :74-77`, whole: *"The primitive faithful character has `|n|=1`. `n=0` is
unfaithful and `|n|>1` repeats the primitive winding. Orientation relates `n=1` and `n=-1`.
This yields stable integral charge units for the primitive record handle without using the
observed electromagnetic coupling."* No base structure is consulted.

The independent hostile check confirms this at depth: `ETHER_CHECK :149-153`, whole:

> "I checked whether any machinery object was needed even to POSE `n_ch`. It was not. The posing
> consumes unit-modulus characters, the two-sector controlled transition, refinement/composition
> and cycle/gauge single-valuedness — all present in member 02 without a metric argument. The
> subject's citation of member 08 is for span custody (which member pins member 02's bytes),
> not for content, so the posing does not route through member 08's contested promotion."

## §C — GRADE STATEMENT

```text
Q5 = FIBER-DEPENDS-ON-BASE

DEPENDS (admissibility):  a W4 member's connection and curvature are inadmissible if the
                          base coframe is degenerate or the base density non-positive
                          (WHERE :621-622); the transported connection/curvature must be
                          expressible with the child coframe (I8) and must make
                          Vol_4(C) sum F^2 natural under refinement (I9); the Maxwell/Hodge
                          symbol comes from the P4 coframes (B_C3_MAXWELL_HODGE).

DOES NOT DEPEND (definition and value):  f = da, W_n(gamma) = exp(i n integral_gamma a),
                          a_j = a_i + d theta_ij, the cocycle g_ij g_jk g_ki = 1, U_e,
                          and |n| = 1 are each defined and valued with no base metric,
                          distance, angle, volume or coframe anywhere in them.

STANDING NOTE: every one of the DEPENDS items is a demand that is NOT MET at bytes —
I8's own column says the coframe artifacts supply "no connection relation"; I9 sits in an
interface whose I6 binding is expressly "the missing binding"; and the W4 member set may
be empty. The dependency is real in the law and uninhabited in the record.
```

---

## FLAG BLOCK

| # | Flag | Statement |
|---|---|---|
| **FL-1** | **THE GEOMETRY AND THE RECORD SIT ON DIFFERENT BASES.** | Every substantive base-side geometric structure (metric, geodesic, parallel transport, extrinsic curvature, coframe, density, `Vol_4`) lives on a smooth carrier — `M_G`, `M_K`, `Sigma`. The record's own cellular object `K` is *"a finite oriented regular CW complex of dimension at most two"* with a root, and carries incidence, faces, orientation, and cell weights hypothesised to be the identity. **The corpus does not identify these objects.** Forward bridge `f_g` = **UNDECIDABLE**, `SUPPLIED = 0`. Reverse bridge = `reverse_discrete_to_smooth_bridge_canonical = false`. Registered here as the load-bearing structural fact of this audit. |
| **FL-2** | **THE BASE'S GEOMETRY IS ALMOST ENTIRELY ENTERED, NOT DERIVED.** | Provenance count: 1 DERIVED, 2 ADOPTED (as possibly-empty membership laws), 5 ENTERED, 3 NAMED-ONLY. The one derived item — the uniform flat-cell measure — is derived **from** an entered Poincaré covariance on **flat** cells. The corpus is candid about this: *"disclosed ordinary-branch inputs. BID does not derive them."* |
| **FL-3** | **NO CURVATURE OF THE RECORD SURFACE EXISTS.** | Sweeps for Riemann, Ricci, scalar, sectional, Gaussian and intrinsic curvature of the surface returned two record artifacts, both opened; neither supplies one, and the substantive hit is a *negative about the fiber*. Sweeps for angle deficit / vertex excess / face defect returned **zero**. Curved cells are expressly outside the one classification theorem. The only base-side curvature at bytes is the **extrinsic** `K_ij := (1/2) d_s h_ij` of a slice, and it is entered as a convention. |
| **FL-4** | **THE BASE HAS NO LENGTH OF ITS OWN.** | The conversion from internal record geometry to external Lorentzian length — `beta` — is the program's registered long-standing blocker and is a specification, not a construction. The base's *shape* structures (coframe, `Vol_4`) are ratios and determinants in an unfixed unit class: *"density normalization/scale \| NONE SELECTED; `VolNorm` remains a predicate"*. |
| **FL-5** | **THE ADOPTED BASE GEOMETRY MAY BE EMPTY.** | `Cof_R` and `Dens_R` are adopted as **membership conditions**, and `W4_ADMISSIBLE_SET_MAY_BE_EMPTY = true`. The density receiver `R4Dens` is **OPACITY-BOUND** by its own author's declaration: *"It deliberately declines to say what an element of `R4Dens(K)` is."* No coframe member and no density member is bound anywhere in the corpus. |
| **FL-6** | **THE MICROSCOPIC CELL WEIGHTS ARE A HYPOTHESIS, AND THEIR ALTERNATIVE IS A LIVE COMPETITOR.** | `M_0=M_1=M_2=I` is *"a new physical hypothesis, not a result"*, with Gate 3 open; and *"A compensating positive basis/measure rescaling is not an equivalence; it changes the physical Hilbert operator and remains in the competitor audit."* Whether the record's cells are equally weighted is therefore **open**, not settled. |
| **FL-7** | **A RATIFIED RULING IS TITLED "THE CARRIER METRIC" AND IS NOT A METRIC ON THE BASE.** | DoR-019's `s_G(c,d)=g_A4(u_c,u_d)` takes **cycles** as arguments. Reported so that the ruling's title is not read forward as base geometry. |
| **FL-8** | **TWO SEAL EXCEPTIONS, DISCLOSED.** | `PRIMITIVE_RELATIVE_PHASE_CONNECTION_V001.md` — one of the two `f = da` sources — has **no sidecar in either root**; it is UNSEALED-AT-BYTES and no grade rests on it alone. `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` has no top-level sidecar and the top-level copy (`20a3a17d…`) differs from the sealed packet member (`aa7c6d49…`) by 123 diff lines in the §A32 holdout subsection; all five quoted spans verified byte-identical. |
| **FL-9** | **BUNDLE IDENTITY LEFT OPEN, AS BEFORE.** | Whether DoR-020-A1's bundle, [LPRB]'s *"principal `U(1)` comparison bundle"*, and BID's discrete unitary connection are one object or three is **INDETERMINATE-AT-BYTES**. Neither names another. **This audit does not identify them**, and no grade above depends on identifying them. |

---

## SELF-AUDIT

```text
REGISTER BAR OBSERVED       = true (array globs; per-pattern leak counter reported;
                                    this artifact self-excluded)
DOR_* READ                  = true (4 opened and seal-verified; nothing else read from
                                    supervision/)
NINE-FILE SET OPENED        = true (all 9; 3 genuine BARRED exclusions inside, one of
                                    which is the ruling itself)
UNOPENED MEMBERS DECLARED   = true (SWEEP CUTOFFS, final paragraph)
QUOTES CHECKED FOR WRAPS    = true (every displayed quote re-read against the source
                                    line range; adverse clauses carried whole)
AUTHORING                   = none
ADVOCACY                    = none
ADOPTION                    = none
CATALOGUED NEGATIVES RE-READ = none
NUMERIC EVALUATION          = none
MAGNITUDE APPROACHED        = false
EXTERNAL LITERATURE         = none introduced
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
