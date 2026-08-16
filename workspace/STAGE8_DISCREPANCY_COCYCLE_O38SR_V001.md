# DISCREPANCY-COCYCLE DETERMINATION — COMMISSION O38SR — READ AND CLASSIFIED AT BYTES

COMMISSION O38SR — BUILD LANE OF A COMMISSIONED PAIR — 2026-08-15
READ AND CLASSIFY ONLY. NOTHING IS DERIVED, EXTENDED, ADOPTED, ADVOCATED,
RECOMMENDED, OR SUPPLIED. NO MISSING OBJECT, PRINCIPLE, OR CLAUSE IS AUTHORED
ANYWHERE BELOW — NOT IN A TOY, A FOOTNOTE, OR AN ASIDE. GAPS ARE DESCRIBED,
NEVER FILLED.

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

OUTPUT-PATH PROBE, BEFORE ANY WRITE:
`/Users/bgm/MB Work/alpha-program-archive/workspace/STAGE8_DISCREPANCY_COCYCLE_O38SR_V001.md`
— ABSENT (`ls` exit 1); sidecars `...V001.md.sha256` / `...V001.md.seal.sha256` — ABSENT.
Probed at commission start, before the first byte was written.

CORPUS (only readable surface, both roots swept):
```text
ROOT1 = /Users/bgm/MB Work/alpha-program-archive/workspace
ROOT2 = /Users/bgm/Documents/New project/gravity_emergence_evidence_program/
        alpha_fundamental_record_action_cleanroom_v003
```

---

## §0 — IMPORT AUDIT, STATED FIRST

```text
*** THE WORDS "COCYCLE", "CROSSED HOMOMORPHISM", "COBOUNDARY", "SUPPORT",
    "DEFECT TERM", "RESIDUE" AND "GAUGE" ARE USED BELOW ONLY TO *DESCRIBE* WHAT
    THE CORPUS DISPLAYS. NO THEOREM ABOUT ANY OF THEM IS IMPORTED, AND NOTHING
    IS CONCLUDED FROM A NAME. ***
```

| Import | Source | Where used | Does the finding survive without it? |
|---|---|---|---|
| "crossed homomorphism" / "cocycle" as descriptive vocabulary | standard homological algebra, outside this corpus | §2 type discussion only | **YES.** Every grade rests on quoted corpus bytes. The word is never load-bearing. Note the corpus itself uses "cocycle" of its own accord (`(C1-7)` "Its discrepancy cocycle is", `(R1-7)`), so even the *name* is record-native at these sites. |
| "defect term", "residue" as shape names | supplied by this commission's sweep vocabulary | §0, SWEEP CUTOFFS only | **YES.** Used only as search strings. `defect term` as a *shape name* is flagged by `STAGE8_BOUNDARY_SHAPES_O32SR_AUDIT_V001.md:§0` as commission vocabulary, not the record's; this artifact adopts that same discipline. |
| "domain", "type", "source/target" | standard mathematical usage | §2 | **YES.** Descriptive only; every type claim is quoted. |

NO OTHER IMPORT IS MADE. In particular, no theorem about cocycles, no
vanishing criterion, no cohomological interpretation, and no consequence of any
composition law is imported or applied. Where the corpus states a law, this
artifact reports the law and stops.

---

## §1 — Q1: IS `beta` EVER NONZERO?

### GRADE: **PROVEN-ZERO**, at every site in the corpus where `beta` is evaluated at all.

Three independent sites evaluate it. All three give zero. No site anywhere in
either root exhibits a nonzero `beta`, bounds one below, or asserts one exists.

### §1.1 SITE ONE — the definition itself, and it carries `= 0` in the defining line

`STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V001.md` (seal verified OK
from its own directory), `:242-254`, quoted WHOLE, including every clause that
cuts against a finding of emptiness, and to the end of its span:

```text
Define the response/contact transport `rho_f^C2` by the same test/current
pullback, including the endpoint and bundle data supplied by DoR-020-A1.
Its discrepancy cocycle is

beta_f := rho_f^C2(C2_m^fin) - C2_n^fin = 0       (C1-7)

on the old image. For a cycle-creating arrow, `(C1-7)` says the old response
restricts exactly; it says nothing false about the target-only new-cycle
component. The latter remains visible in `C2_m^fin`. The local orthogonal
excision certificate ensures contact and disjoint support pieces do not leak
into the old response coordinate.
```

**This is the only definition of `beta_f` in either root.** The sweep
`beta_f :=` returns **2 files / 3 hits in ROOT1** and **1 file / 1 hit in
ROOT2**. Stated exactly, so the count is not mistaken for more than it is: in
ROOT2 the single hit is this artifact, this line. In ROOT1 the same line appears
here, and the two further hits are both in
`STAGE8_BOUNDARY_SHAPES_O32SR_AUDIT_V001.md` (`:366` and `:910`), which
**quotes** this definition rather than issuing another one. **One definition,
one defining artifact, one prior audit quoting it.**

Read at bytes, the equality `= 0` is *part of the defining display*, on the same
line as the `:=`. The scope is stated in the immediately following prose and is
**"on the old image"**. Two clauses cutting against a blanket zero are quoted
above and are repeated here so they are not lost: the artifact expressly says
`(C1-7)` "says nothing false about the target-only new-cycle component", and
that component "remains visible in `C2_m^fin`". So the corpus is explicit that
`(C1-7)` is a statement about the old-image restriction and is **not** a claim
that nothing differs anywhere.

The next paragraph, `:256-259`, quoted whole:

```text
The definition extends the pass-1 `Ref_path` zero cocycle to every generator
of `I_F`: W3 restrictions use the sealed response square; flips use OLD_FID,
exclusive-region RNL, and LR; common refinements use the already-proved
path/current and bundle diamonds.
```

The corpus's own word for the object being extended is **"zero cocycle"**.

### §1.2 SITE TWO — the pass-1 `Ref_path` evaluation, also zero

`STAGE8_TASK5_HUNT_CROSS_CHECK_AND_FRONTIER_LANE2_V001.md` (seal verified OK),
`:208-226`, quoted WHOLE:

```text
### 2.3 Zero kernel-discrepancy cocycle

On `Ref_path`, define the actual discrepancy—not an authored response—by

beta_nm(H)
 :=Kern_m^fin(j_nm^H H)-Pull_nm Kern_n^fin(H).     (R1-6)

Equation `(R1-2)` gives `beta_nm=0`.  For composable subdivisions,

beta_nl=0=beta_ml+eta_ml(beta_nm).                 (R1-7)

The generated contact ideal is `{0}`, so no visible cycle is deleted.  This
is neither circular nor a blanket declaration about future new-edge
discrepancies.  The expression `beta/Vol` remains undefined until a positive
P4 volume exists; the hunt correctly leaves subextensivity conditional.
```

Note three things at bytes. First, the section *heading itself* is "Zero
kernel-discrepancy cocycle". Second, `(R1-7)` writes the composition law with a
literal `0` substituted on the left: `beta_nl=0=beta_ml+eta_ml(beta_nm)` — the
cocycle law is displayed *already collapsed*. Third, the artifact's own caveat
is quoted whole and cuts against over-reading the zero: it is "neither circular
nor a blanket declaration about future new-edge discrepancies."

### §1.3 SITE THREE — the typed form, with `beta_nn=0` displayed

`STAGE8_TASK5_HOSTILE_WITNESS_CROSS_CHECK_LANE1_V001.md` (seal verified OK),
`:179-195`, quoted WHOLE:

```text
### 2.3 J13

The headline equation is shorthand, but W-13 supplies the typed form:

beta_nk
 =beta_mk compose S_nm + eta_mk compose beta_nm,
beta_nn=0.

This is the direct/two-step discrepancy cocycle, including the necessary
precomposition.  The rule meets the Q-413 repair.  F_PLDEC's `beta=0`
claim still depends on an actually constructed response transport, which is
not supplied.
```

The final sentence is the corpus's own hostile qualification and is reported
here in full: the `beta=0` claim is said to depend on "an actually constructed
response transport, which is not supplied." **This does not exhibit a nonzero
`beta`.** It states that the *zero claim* rests on an object that is absent. An
unsupplied premise for a vanishing claim is not a nonvanishing witness, and this
artifact does not read it as one.

### §1.4 THE SEARCH FOR A NONZERO WITNESS — RUN, AND NEGATIVE

The corpus states, in its own words and at two seal-verified sites, that no
family for `beta` to range over exists.

`STAGE8_TASK5_CONTINUUM_PACKAGE_ADOPTION_PROPOSAL_LANE2_V005.md:482`, quoted
whole (the full table row):

```text
| J13 | boundary/contact cocycle and safe ideal | **CONDITIONAL THEOREM ONLY** | closure hull `(O1-13)` preserves a supplied cocycle; no actual P7 discrepancy family exists to close |
```

`STAGE8_GAUGE_AS_CONTENT_O34SR_V001.md:564-570`, from its TOY_SEPARATION block,
quoted whole across the boundary between its two halves so no clause is lost:

```text
  beta_nk, the direct/two-step discrepancy cocycle, and the J13 status rows;
  H_source tensor H_record tensor H_boundary/environment;
  O6SR's COUNTERFACTUAL B (O6-1d);
  M-1 unmatched carriers / M-2 overlapping-not-identical cells / M-3 adjacency.

NOT SURFACE — NOT TOUCHED, NOT BUILT, NOT SUPPLIED:
  no patch family, cover, nerve, or topology was constructed for U_i;
  no transfer of the Cech/nerve construction to the Gate-4 incidence graph;
  no discrepancy family was supplied for beta to range over;
```

**"no discrepancy family was supplied for beta to range over"** is the corpus's
own sentence, in a sealed artifact, and it is dispositive for Q1.

Correspondingly, `STAGE8_TASK5_PACKAGE_ADJUDICATION_AND_WITNESS_LANE1_V001.md`
(seal OK) `:137`, quoted whole:

```text
| P7 response/boundary naturality | **KILL / J13** | J9, J12-J13, J15 | naturality and subextensivity are stated, but no boundary discrepancy cocycle under refinement composition is required |
```

### §1.5 WHAT V003 ITSELF DOES WITH `beta` — NOTHING BEYOND RESTATING A LAW

In the commissioned artifact `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md`,
`beta` occurs at exactly **three** lines (`:391`, `:395`, `:412`) plus one
bare mention in a regression table (`:458`). It is **never defined there**,
never evaluated there, never given a type there, and never bounded there. V003
states laws about an object whose definition lives in a different artifact —
the one identified in §1.1, whose standing is reported in §4.

### §1.6 Q1 GRADE, STATED WITHOUT SOFTENING

```text
Q1_GRADE = PROVEN-ZERO
```

- **Cited:** `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V001.md:247`
  — `beta_f := rho_f^C2(C2_m^fin) - C2_n^fin = 0   (C1-7)`.
- **Scope of that proof, in the corpus's own words:** **"on the old image."**
  The corpus explicitly declines to extend it to "the target-only new-cycle
  component", which "remains visible in `C2_m^fin`", and explicitly declines a
  "blanket declaration about future new-edge discrepancies"
  (`...HUNT_CROSS_CHECK...:219-220`).
- **Second and third sites** (`beta_nm=0` on `Ref_path`, `(R1-6)/(R1-7)`;
  `beta_nn=0`, typed form) agree.
- **Nonzero exhibition:** NONE, in either root. No worked instance, no example,
  no lower bound, no nonvanishing proof, no statement that it is nonzero in any
  case. The corpus instead states that **no family for it to range over exists**.

This grade is not softened to MIXED. The three sites do not disagree with one
another; they agree on zero and differ only in which generator class they cover.
The one qualification the corpus raises — that the zero claim depends on an
unsupplied response transport (§1.3) — makes the zero claim *less* supported,
not the object nonzero.

**Consequence, stated plainly and not hedged:** a defect term that is zero
wherever the corpus evaluates it, and that has no supplied family to range over,
carries no exhibited content at bytes. Everything below is read in that light.

---

## §2 — Q2: TYPE AND DOMAIN

### §2.1 The morphism-indexed usage — the only one that is defined

From the single definition (`...LANE1_LANE2_V001.md:247`, quoted whole in §1.1):

```text
beta_f := rho_f^C2(C2_m^fin) - C2_n^fin = 0       (C1-7)
```

The constituents are typed by that artifact's own symbol ledger, `:126-132`,
quoted whole:

```text
| Symbol | Meaning |
|---|---|
| `Adm_fin(n)` | the entire retained finite R1 action family at stage `n`, never a selected member |
| `Gamma_m` | a variable member of `Adm_fin(m)` |
| `Kern_n^fin` | actual Q-408 finite current/kernel map |
| `C2_n^fin` | finite response/contact/Ward boundary datum |
| `C3_n^fin` | finite Ward and finite Maxwell-symbol datum, not a completed Hodge object |
| `Bot_n` | the one sealed finite-shadow package at stage `n` |
| `v_f` | target vertical/new-cycle coordinate relative to `i_f^Y(Y_n)` |
```

and `rho_f^C2` is declared among the **backward physical/restriction legs** of a
`FinPackage_020` morphism, `:85-110`, quoted whole:

```text
### 2.2 A morphism in `FinPackage_020`

The apparent variance is resolved at the type, not by reversing an arrow.
For an actual refinement arrow `f:n -> m`, a finite-package morphism is a
structured pair:

forward geometric legs:
  i_f^Y       : Y_n -> Y_m              old physical carrier inclusion,
  j_f^H       : H_n -> H_m              test/profile transport,
  S_f^J       : J_n -> J_m              conserved-current transport,
  f_base      : M_n -> M_m              actual surface map,
  tilde_f     : P_n -> P_m              U(1)-bundle lift;

backward physical/restriction legs:
  r_f^Y       := (i_f^Y)^dagger          W3 old-sector restriction,
  rho_f^Gamma : Adm_fin(m) -> Adm_fin(n),
  rho_f^Hess  : Hess_fin(m) -> Hess_fin(n),
  rho_f^C2, rho_f^C3, rho_f^R2, rho_f^A,
  rho_f^bot   : finite shadows at m -> finite shadows at n.
```

**TYPE, READ OFF THE BYTES:**

```text
INDEXED BY   an actual refinement arrow f : n -> m of I_F
SOURCE       (implicitly) the C2 datum at the TARGET stage m — rho_f^C2 is a
             backward leg, so it carries C2_m^fin down to stage n
TARGET       an element of the C2 finite response/contact/Ward boundary datum
             at the SOURCE stage n — beta_f is a DIFFERENCE of two objects of
             that one type: rho_f^C2(C2_m^fin) and C2_n^fin
VALUE        stated equal to 0 on the old image
```

`beta_f` is therefore **not** a map with its own source and target. At bytes it
is an **element** of the stage-`n` C2 datum type, indexed by the arrow `f`. The
composition law `beta_gf = beta_g + Eta_g(beta_f)` adds such elements after
pushing one forward along `Eta_g`; the corpus never types `beta` as a function
of a variable in the morphism-indexed usage.

### §2.2 The element-applied usage — undefined, and never related to the above

`STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md:412`:

```text
||beta_N([r,b])|| <= a_N ||r|| + b_N ||b||,
```

Here the subscript is a **stage** `N`, not a morphism, and the object is
**applied to an element** `[r,b]` of the signed pushout carrier `P_N`.

```text
*** THE CORPUS NEVER RELATES THE TWO USAGES. ***
```

This is a determination at bytes, not an inference:

- `beta_N` in this sense occurs **exactly once in either root** — at this line.
  Every other `beta_N`/`beta_NM` in the corpus is a different object in a
  different artifact (a CTP stage map `beta_NM := alpha_NM,+ tensor_min
  (alpha_NM,-)^op : B_N -> B_M`; a profile map `beta_N : O_prof,N -> I_N^q`; a
  functional `beta_N : Bot_N -> R` which its own artifact says is "not part of
  the sealed stock"). These are homonyms, not the same object.
- No artifact writes `beta_N` in terms of `beta_f`, or vice versa. No artifact
  states that `beta_N` is the map whose value at `f` is `beta_f`, or that
  `beta_f = beta_N(...)` for any argument.
- `beta_N` is **never defined anywhere**. `beta_f` is defined once. The line
  above is the whole of `beta_N`'s existence in the corpus.

Reported plainly: **the corpus does not relate them.** The V003 §4.3 display
therefore moves, inside one section, between a morphism-indexed element that is
defined elsewhere and a stage-indexed operator that is defined nowhere, without
a bridging statement.

### §2.3 WHAT DATA IS `beta` DEFINED ON? — (i), the record's own structure

**ANSWER: (i) the record's own structure.** Every constituent of `(C1-7)` is
record-native:

- `f` ranges over the arrows of `I_F`, which the same artifact defines at
  `:68-79`, quoted whole:

```text
`I_F` is exactly the exhibition's full actual finite consumer/refinement
category. Its objects include all sealed active stages and every covariance,
reality, frame, bundle-gauge, orientation, Ref_path, flip, common-refinement,
and finite-consumer image. Its arrows are generated by:

(i)   identities and admitted surface isomorphisms;
(ii)  W3/DoR-008 finite restrictions;
(iii) rank-preserving physical path subdivisions;
(iv)  cycle-creating flip attachments;
(v)   actual disjoint/contact common refinements;
(vi)  every finite-bottom arrow used by a sealed consumer.
```

- `C2_n^fin` is the record's "finite response/contact/Ward boundary datum" at an
  actual sealed stage.
- `rho_f^C2` is a declared backward leg of the package morphism, built from "the
  same test/current pullback, including the endpoint and bundle data supplied by
  DoR-020-A1".

None of this is an auxiliary construction erected alongside the record. It is
the record's own stage/arrow structure and its own response datum. **This is the
single most important structural fact about `beta` in this artifact**, and it is
what makes the Q2 comparison below decide the way it does.

The carrier that V003's element-applied usage names, `P_N`, is likewise
record-native — V003 `:305-312`, quoted whole:

```text
Define the signed pushout carrier in the additive response category by

R_N^phys = P_N
 := (R_N^rep direct_sum I_N^contact) / Delta_N,

Delta_N
 := { (c,-c) : c in C_N }.                                   (J12-2)
```

```text
NAME COLLISION, FLAGGED SO IT CANNOT PROPAGATE:
  `P_N` in V003:307 is the signed pushout response carrier.
  `P_n` in LANE2_V001:97 is the U(1)-BUNDLE, the source of `tilde_f`.
  These are DIFFERENT objects sharing a letter across two artifacts.
  Nothing below rests on conflating them, and this artifact does not.
```

### §2.4 THE LOAD-BEARING COMPARISON — `beta`'s domain vs. the patch family

The corpus's U(1)-valued transition functions are defined in
`LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md` (see §4 for its seal standing —
**it has no sidecar in either root**), `:19-38`, quoted WHOLE:

```text
The new principle places one primitive record degree on every admissible
causal record cell. Its physical state is a ray in the primitive complex
two-dimensional carrier. On a local patch `U_i`, choose a normalized lift

z_i : U_i -> C^2,
z_i^dagger z_i = 1.

Two lifts represent the same local ray exactly when, on an overlap,

z_j = g_ij z_i,
g_ij = exp(i theta_ij) in U(1).

On triple overlaps, equality of the represented ray requires

g_ij g_jk g_ki = 1.

The local lifts and transition functions therefore define a complex line
bundle, equivalently a principal `U(1)` comparison bundle. This `U(1)` is a
local representative redundancy of the adopted projective record field. It
is not obtained by mistaking a passive basis change for a new physical force.
```

**THE TWO DOMAINS, SIDE BY SIDE, FROM THEIR OWN DEFINITIONS:**

```text
                    beta_f                          g_ij
                    ──────                          ────
DEFINING SITE       ...LANE1_LANE2_V001.md:247      LOCAL_PROJECTIVE_RECORD_
                    (C1-7)                          BUNDLE_V001.md:19-38

INDEXED BY          ONE arrow f : n -> m of I_F     an ORDERED PAIR (i,j) of
                                                    patches with nonempty
                                                    overlap U_i ∩ U_j

THE INDEXING        Obj/Arr(I_F) — sealed active    {U_i}, "a local patch",
OBJECT IS           record stages and their         patches of the space
                    actual refinement/consumer      carrying the projective
                    arrows: identities, W3          record field; overlaps and
                    restrictions, path              triple overlaps
                    subdivisions, flip
                    attachments, common
                    refinements, finite-bottom
                    consumer arrows

VALUED IN           C2_n^fin — the record's finite  U(1), as exp(i theta_ij)
                    response/contact/Ward
                    boundary datum (a DIFFERENCE
                    of two objects of that type)

CONSISTENCY LAW     beta_gf = beta_g + Eta_g(beta_f) g_ij g_jk g_ki = 1
                    (composition of arrows)         (triple overlap)

IS THE INDEXING     YES — I_F is the record's own   *** NO ***
OBJECT CONSTRUCTED  stage/arrow category, sealed
IN THE CORPUS?      and active
```

**ANSWER: A DIFFERENT OBJECT. NOT THE SAME PATCH FAMILY. NOT ANY PATCH FAMILY.**

This is not answered from names. The two indexing objects are displayed above
from their own defining bytes and they are not the same: one is a category of
record stages and refinement arrows; the other is a family of local patches of a
space with overlaps and triple overlaps. There is no map between them in the
corpus, and the corpus says so of its own accord.

`STAGE8_GAUGE_AS_CONTENT_O34SR_V001.md:505-509`, quoted whole:

```text
**HALF TWO HOLDS AS A TYPING STATEMENT, AND ONLY AS THAT.** The gauge structure
is the only structure in the corpus whose values *could* be a mismatch's content
rather than its verdict, because it is the only one that is group-valued on
non-agreeing pieces. It is a **could**, not a **does**: §1.3 establishes that the
one such object is defined on a patch family the corpus never constructs.
```

and `:644-645`:

```text
    triple-overlap cocycle g_ij g_jk g_ki = 1, quoted inside two sealed
    artifacts. It is defined on a patch family the corpus never constructs, and
```

and `STAGE8_RECORD_SIDE_PATCH_DEFINITION_SWEEP_V001.md:42-45` (seal OK):

```text
It does not have the missing object: a definition of what the patch family
```

**The asymmetry is total and it runs the opposite way from what a name-based
reading would suggest.** `beta_f` is defined on data the corpus HAS — actual
sealed stages and actual arrows — but is zero there and has no family to range
over (§1.4). `g_ij` is defined on data the corpus does NOT have — a patch family
it never constructs — but is group-valued where it is defined. The two objects
fail in opposite directions and they do not meet.

---

## §3 — Q3: THE SUPPORT LAW

### §3.1 (J13-1) QUOTED WHOLE, IN CONTEXT, WITH THE LINE-WRAP CHECK RUN

`STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md:386-401`, quoted
WHOLE — the introducing sentence, the entire fenced display, and the paragraph
that follows it, so that no clause bearing on the law's scope is elided:

```text
More explicitly, with `q_N` the quotient map and with all expressions on their
declared scopes, the induced data satisfy

Eta_g Eta_f q_N = Eta_gf q_N,
beta_gf          = beta_g + Eta_g(beta_f),
Res_f Eta_f       = id on each licensed old-image scope,
Theta_M Eta_f    = Eta_f Theta_N,
Ward_M Eta_f     = Ward_N,
supp(Eta_f x)    subset f(supp x) union supp(beta_f).          (J13-1)

The first equality was proved in (J12-4).  For each remaining equality, both
sides agree after precomposition with the represented injection and with the
contact injection.  They also agree on `C_N` by (J12-1).  The pushout universal
property therefore makes the equality hold on all of `P_N`.
```

**LINE-WRAP CHECK — RUN AT BYTES, NOT ASSUMED.** Physical line lengths in the
display, measured directly:

```text
LINE 389  ```text                                                       len 7
LINE 390  Eta_g Eta_f q_N = Eta_gf q_N,                                 len 29
LINE 391  beta_gf          = beta_g + Eta_g(beta_f),                    len 42
LINE 392  Res_f Eta_f       = id on each licensed old-image scope,      len 56
LINE 393  Theta_M Eta_f    = Eta_f Theta_N,                             len 33
LINE 394  Ward_M Eta_f     = Ward_N,                                    len 26
LINE 395  supp(Eta_f x)    subset f(supp x) union supp(beta_f).   (J13-1)  len 70
LINE 396  ```                                                           len 3
```

Line 395 terminates in a period before the label and line 396 is the closing
fence. **(J13-1) is COMPLETE ON ONE PHYSICAL LINE. There is no continuation.**
No line in the block approaches a wrap width. This artifact makes no fabrication
finding and no truncation finding here.

```text
ONE AMBIGUITY, REPORTED RATHER THAN RESOLVED:
  The label `(J13-1)` is placed at the end of a SIX-LINE display. The bytes do
  not disambiguate whether it labels the whole display or only its last line.
  This artifact does not decide it, and nothing below depends on which reading
  is correct.
```

### §3.2 WHAT (J13-1) BOUNDS, STATED PLAINLY

```text
supp(Eta_f x)  subset  f(supp x)  union  supp(beta_f)
└─ where the ─┘        └─ the ──┘        └─ PLUS AN ALLOWANCE ─┘
   transported            image of
   object lives           the original
                          support
```

`supp(beta_f)` is the **additive allowance** in a support-containment law. It
bounds how far the support of a transported object may extend beyond the direct
image of the support it started with. It controls the permitted *spreading* of
support under `Eta_f`, and nothing else in this display.

**IF `supp(beta_f)` WERE EMPTY**, the law would read `supp(Eta_f x) subset
f(supp x)` — exact support transport with no spreading whatever. That is the
structural content of the question, and the answer is: the allowance term is the
entire difference between "support may spread" and "support may not spread."

This artifact stops there. It does not evaluate whether the allowance is empty,
does not derive the emptiness from `(C1-7)`, and does not author the missing
statement. **The corpus nowhere writes `supp(beta_f) = empty`, and nowhere draws
the inference from `beta_f = 0` to the support law collapsing.** Whether such an
inference is available is not decided at bytes and is not decided here.

### §3.3 IS `supp(beta_f)` EVER COMPUTED, BOUNDED, LOCALIZED, OR PLACED?

Swept in both roots: `supp\(beta` returns **2 files / 8 hits in ROOT1** and
**1 file / 1 hit in ROOT2**. In ROOT1 those are V003 (one hit, line 395 — the
law itself) and `STAGE8_BOUNDARY_SHAPES_O32SR_AUDIT_V001.md` (seven hits, all of
which quote or discuss V003's line 395 and none of which compute anything). In
ROOT2 the single hit is V003's line 395.

**There is no other occurrence of `supp(beta_f)` in the corpus.** It is never
computed, never bounded above or below, never localized to any region, and never
placed on any boundary, interface, seam, overlap, or carrier edge.

The nearest-adjacent text is a table row in the same section, V003 `:380`,
quoted whole — and it must not be mistaken for a constraint on `supp(beta_f)`:

```text
| support | support is the union of the represented and contact supports modulo their actual overlap |
```

This row describes the support of the **glued data on the pushout carrier** —
the union of the two legs' supports modulo overlap. It is a statement about
`P_N`'s support structure, **not** about `supp(beta_f)`. The prior audit
`STAGE8_BOUNDARY_SHAPES_O32SR_AUDIT_V001.md:403-408` reads this row alongside
`supp(beta_f)` when typing the record against a shape template; this artifact
records that the two are different objects and declines to merge them.

### §3.4 Q3 GRADE

```text
Q3_GRADE = NEVER-CONSTRAINED
```

`supp(beta_f)` is written, and used as a term inside a sealed inclusion, at
exactly one line in the corpus. It is never given an extent, a bound, a
locus, or a relation to any boundary, interface, seam, overlap, or carrier edge.
It is a named term with a place in one expression and no determination anywhere.

---

## §4 — Q4: ADOPTION STATUS OF EVERY ARTIFACT CONSUMED

**V003 IS NOT ASSUMED CURRENT. IT IS NOT CURRENT, AND IT IS DEFECTIVE OF RECORD.**

### §4.1 The supersession chain, traced

```text
STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md   ← the commissioned site
   a46beae26048a0d093de339363fb8597d362a0101d103cfc06305edabac53f4c
   reviewed by → STAGE8_TASK5_EQ6_STAGE1_V003_REVIEW_LANE2_V001.md
                    verdict: STAGE1_V003 = DEFECTIVE (H1,H5,H6)
   succeeded by → STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V004.md
                    9bf34e27da9aca51966feb2b41f34b0060e2121bd85d783d35a81685bbb63514
                    ARTIFACT_TYPE = STAGE1_REPAIR_BUILD
                    *** V004 CONTAINS ZERO OCCURRENCES OF `beta` AND ZERO OF `J13` ***
```

`STAGE8_TASK5_EQ6_STAGE1_V003_REVIEW_LANE2_V001.md` (seal OK), header block,
quoted whole:

```text
ARTIFACT_TYPE = ADVERSARIAL_REVIEW_OF_RECORD
LANE = CODEX_LANE_2
ARTIFACT_UNDER_REVIEW = STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md
ARTIFACT_UNDER_REVIEW_SHA256 = a46beae26048a0d093de339363fb8597d362a0101d103cfc06305edabac53f4c
REGISTER_HEAD_STATED = Q-467
REGISTER_HEAD_VERIFIED = Q-468
Q468_EFFECT_ON_REVIEW = NONSUPERSEDING; relay 544 remains queued

STAGE1_V003 = DEFECTIVE (H1,H5,H6)
FC_SUPPLIED = FC2, FC4, FC13; FC1/FC7/FC8/FC9 carried; FC3 and FC5 not confirmed; FC10 partial; FC11 open; FC12 struck
```

**That review nowhere examines `beta`.** Swept: `J13|beta|subextensiv` returns
exactly one line in it — `:290`, quoted whole with its enclosing item so the
sense is not clipped:

```text
3. Composition, reality, units, Ward, restriction, support, OLD_FID, RNL, LR,
   and subextensivity descend only when their two legs agree on `C_N`; V003
   states and uses that premise rather than deriving it from the quotient.
```

So the review's one contact with this material records that V003 **states and
uses** the descent premise **rather than deriving it**.

V004's own scope statement, `:43`, quoted whole:

```text
The stage-1 V003 artifact is byte-different from V004 by design; this repair only replaces the J4 face's A3-family implementation and functoriality ledger.
```

**CONSEQUENCE, STATED EXACTLY:** V004 repairs the J4 face only. It does not
restate, repair, confirm, or withdraw the §4.3 J13 material. The `beta` display
therefore stands where V003 left it, in an artifact its own review of record
graded **DEFECTIVE**, with the successor silent on the point.

### §4.2 The artifact that DEFINES `beta_f` is killed

The single definition of `beta_f` (§1.1) lives in
`STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V001.md`
(`e21cee3081da06417109697352abe570c58dc6dda7d46e78f690d666bed128f5`).

Its review of record, `STAGE8_TASK5_EQ6_ASSEMBLY_STAGE1_REVIEW_LANE1_V001.md`
(seal OK), header, quoted whole:

```text
ARTIFACT_TYPE = ADVERSARIAL_CROSS_REVIEW_OF_RECORD
REGISTER_HEAD_CHECKED = Q-458
ARTIFACT_UNDER_REVIEW = STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V001.md
ARTIFACT_UNDER_REVIEW_SHA256 = e21cee3081da06417109697352abe570c58dc6dda7d46e78f690d666bed128f5

STAGE1_ASSEMBLY = DEFECTIVE (V1,V2,V3,V4,V5,V6)
STAGE2_REMAINDER = INCOMPLETE (all-arrow J4 + forward J12 + package J15 remain before the joint diamonds)
```

And the corpus calls it **killed**, twice, in a later lane artifact.
`STAGE8_TASK5_EQ6_MEMBERSHIP_THEOREM_LANE3_V001.md` (seal OK) `:49` and `:382`,
each quoted whole:

```text
| Q-486 finding 1 is honored. | PROVABLE | Every assembly citation below names the confirmed `...LANE1_V003.md` / `...LANE1_V004.md` chain, never the killed `...LANE2_V001.md` look-alike. |
```

```text
[PROVABLE] The citation correction is substantive and explicit: the five-face input is consumed through confirmed `H_ASM3=a46beae2…` plus repaired `H_ASM4=9bf34e27…` and their reviews `H_R3/H_R4`. The killed `...JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V001.md` is not an authority for this proof.
```

```text
*** THE ONLY DEFINITION OF beta_f IN THE CORPUS LIVES IN AN ARTIFACT THE CORPUS
    ITSELF CALLS "KILLED" AND "NOT AN AUTHORITY". ***
```

This artifact does not thereby conclude the definition is wrong. It reports the
standing: the object's one definition has no adopted carrier.

### §4.3 ARE THE J13 LAWS SEALED OF RECORD, OR ASSERTED WITHIN A SINGLE LANE?

V003 names its authority for the J12/J13 material. V003 `:48-49`, quoted whole:

```text
| `DOR_020_A3_J4_RELATIONAL_INCREMENT_GROUPOID_2026-08-04.md` | adopted J4 law | SHA-256 `07e0e50145314fe5c30b7f7b5637d4c8add0834c631ad9c2e16209bf3b5a9d6f` |
| `DOR_020_A4_J12_CONTACT_GLUE_STRICT_PUSHOUT_2026-08-04.md` | adopted J12 law | SHA-256 `5fd95472bd6f0507a371779505fe91e2c3c4657ee3afc664ca563a3743d668a4` |
```

and a second lane confirms A4 is where the J13 laws are supposed to live —
`STAGE8_TASK5_EQ6_PROJECTOR_LOCALITY_REDUCING_CERT_V002_LANE1_V001.md:87` and
`:110-112`, each quoted whole:

```text
| DoR-020-A4 strict pushout | `5fd95472bd6f0507a371779505fe91e2c3c4657ee3afc664ca563a3743d668a4` | contact gluing and J13 laws |
```

```text
5. A4 requires contact gluing plus J13 support/Ward/restriction laws, but says
   nothing about the contact orthogonal projection commuting with a Riesz
   adjoint, Laplacian, or spectral projector.
```

```text
*** THE DoR-020-A3 AND DoR-020-A4 FILES ARE NOT PRESENT IN EITHER ROOT. ***
  find -iname "*DOR_020*"  →  0 files, ROOT1
  find -iname "*DOR_020*"  →  0 files, ROOT2
  find -iname "*dor*020*"  →  0 files, ROOT2
The SHA 5fd95472… appears in 8 ROOT1 artifacts, always as a CITATION.
The bytes of the decision of record carrying the J13 laws CANNOT BE READ IN THE
CORPUS. This artifact therefore CANNOT VERIFY at bytes that the J13 laws are
sealed of record, and does not assert that they are.
```

What CAN be read at bytes is how other lanes grade J13. All four are quoted
whole:

```text
| J13 | boundary/contact cocycle and safe ideal | **CONDITIONAL THEOREM ONLY** | closure hull `(O1-13)` preserves a supplied cocycle; no actual P7 discrepancy family exists to close |
      — STAGE8_TASK5_CONTINUUM_PACKAGE_ADOPTION_PROPOSAL_LANE2_V005.md:482
        (that artifact's own header: "Standing: **PROPOSED_NOT_ADOPTED**; DoR-020 reserved")

| P7 response/boundary naturality | **KILL / J13** | J9, J12-J13, J15 | naturality and subextensivity are stated, but no boundary discrepancy cocycle under refinement composition is required |
      — STAGE8_TASK5_PACKAGE_ADJUDICATION_AND_WITNESS_LANE1_V001.md:137

| J13 boundary cocycle | **KILL ON WITNESS** | rule installed, but zero discrepancy uses the incomplete J12 map |
      — STAGE8_TASK5_HOSTILE_WITNESS_CROSS_CHECK_LANE1_V001.md:412

| J13 | `beta=0` obeys the cocycle and safe-ideal requirements on `Ref_path` |
      — STAGE8_TASK5_THE_WITNESS_HUNT_LANE1_V001.md:604
```

The one affirmative grade in that set is scoped to `Ref_path` and states the
object as `beta=0`.

### §4.4 STANDING TABLE — EVERY ARTIFACT CONSUMED FOR THIS FINDING

| # | Artifact | Seal | Standing, QUOTED from its own bytes |
|---|---|---|---|
| 1 | `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md` | OK | `ARTIFACT_TYPE = CONDITIONAL_FINITE_ASSEMBLY_BUILD` / `LANE = CODEX_LANE_1` / `CONDITION_TAG = [EQ6]`. **Lane build, condition-tagged.** Graded `STAGE1_V003 = DEFECTIVE (H1,H5,H6)` by its review of record. Superseded on the J4 face only by V004. |
| 2 | `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V004.md` | content hash matches sidecar; **sidecar malformed** (see FLAG BLOCK) | `ARTIFACT_TYPE = STAGE1_REPAIR_BUILD` / `REGISTER_HEAD = Q-469`. Repairs the J4 face only; **silent on `beta` and `J13`** (0 occurrences of each). |
| 3 | `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V001.md` | OK | `ARTIFACT_TYPE = FINITE_CONSTRUCTIVE_BUILD`. Graded `STAGE1_ASSEMBLY = DEFECTIVE (V1,V2,V3,V4,V5,V6)`; called **"killed"** and **"not an authority for this proof"** by LANE3. **Carries the only definition of `beta_f`.** |
| 4 | `STAGE8_TASK5_EQ6_STAGE1_V003_REVIEW_LANE2_V001.md` | OK | `ARTIFACT_TYPE = ADVERSARIAL_REVIEW_OF_RECORD`. A lane review. Does not examine `beta`. |
| 5 | `STAGE8_TASK5_EQ6_ASSEMBLY_STAGE1_REVIEW_LANE1_V001.md` | OK | `ARTIFACT_TYPE = ADVERSARIAL_CROSS_REVIEW_OF_RECORD`. A lane review. |
| 6 | `STAGE8_TASK5_HUNT_CROSS_CHECK_AND_FRONTIER_LANE2_V001.md` | OK | Lane cross-check. Source of `(R1-6)/(R1-7)` and of the `beta/Vol` undefinedness statement. |
| 7 | `STAGE8_TASK5_HOSTILE_WITNESS_CROSS_CHECK_LANE1_V001.md` | OK | Lane hostile cross-check. Grades J13 `KILL ON WITNESS`. |
| 8 | `STAGE8_TASK5_CONTINUUM_PACKAGE_ADOPTION_PROPOSAL_LANE2_V005.md` | OK | **`Standing: PROPOSED_NOT_ADOPTED; DoR-020 reserved`** — quoted from its own header. Not of record. |
| 9 | `STAGE8_TASK5_PACKAGE_ADJUDICATION_AND_WITNESS_LANE1_V001.md` | OK | Lane adjudication. |
| 10 | `STAGE8_TASK5_EQ6_MEMBERSHIP_THEOREM_LANE3_V001.md` | OK | Lane theorem build; every claim tagged `[PROVABLE]`, not adopted. Source of the "killed" statements. |
| 11 | `STAGE8_TASK5_EQ6_DETERMINATION_MAP_LANE1_V001.md` | OK | Lane determination map. Its `(D2-4)` block is labelled **PROVABLE**, and it states the local-excision artifact "expressly leaves the positive-source physical contact term and coherent all-rank section unproved." |
| 12 | `STAGE8_GAUGE_AS_CONTENT_O34SR_V001.md` | OK | Prior commission determination (O34SR). Determination only. |
| 13 | `STAGE8_BOUNDARY_SHAPES_O32SR_AUDIT_V001.md` | OK | Prior commission audit (O32SR). `DETERMINATION ONLY. Nothing is constructed, proposed, adopted or supplied.` |
| 14 | `STAGE8_DEMAND_REGISTER_O25SR_V001.md` | OK | Prior commission determination; source of the W-1/W-2/W-3 text. |
| 15 | `STAGE8_RECORD_SIDE_PATCH_DEFINITION_SWEEP_V001.md` | OK (sidecar names a ROOT2 absolute path) | Sweep artifact; records the patch family as the missing object. |
| 16 | `STAGE8_CANONICAL_PATCH_COVER_TO_INCIDENCE_GRAPH_FUNCTOR_ATTEMPT_V001.md` | OK (sidecar names a ROOT2 absolute path) | Named an **ATTEMPT** in its own filename. |
| 17 | `LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md` | **NO SIDECAR IN EITHER ROOT — UNVERIFIABLE** | Carries the `g_ij` definition. Its own text: "It is therefore a Level-1 result under the newly adopted microscopic principle." **This artifact could not seal-verify it and flags the quotation in §2.4 accordingly.** |
| 18 | `STAGE8_TASK5_EQ6_AXIOM_CONSTRAINT_ARM_LANE1_V001.md` | OK | Lane constraint arm; `Custody: derivation only`. |
| 19 | `STAGE8_TASK5_THE_WITNESS_HUNT_LANE1_V001.md` | OK | Lane witness hunt. |
| 20 | `STAGE8_TASK5_EQ6_PROJECTOR_LOCALITY_REDUCING_CERT_V002_LANE1_V001.md` | OK | Lane certificate. |
| — | `DOR_020_A4_J12_CONTACT_GLUE_STRICT_PUSHOUT_2026-08-04.md` | **ABSENT FROM BOTH ROOTS** | The claimed adopted authority for the J13 laws. **Not readable. Not verified. Cited by SHA only.** |

### §4.5 Q4 ANSWER, STATED WITHOUT CONFLATION

```text
*** NOTHING IN THIS FINDING IS OF RECORD. ***

The beta display sits in a CONDITION-TAGGED LANE BUILD graded DEFECTIVE by its
own review. Its one definition sits in a lane build the corpus calls KILLED. The
J13 grades available at bytes are CONDITIONAL THEOREM ONLY (in an artifact whose
own header reads PROPOSED_NOT_ADOPTED), KILL / J13, and KILL ON WITNESS. The
decision of record that would carry the J13 laws is ABSENT FROM THE CORPUS and
could not be read.

A structure that is real but unadopted is a different finding from one of
record. THIS ONE IS UNADOPTED, AND IN PART KILLED.
```

---

## §5 — Q5: REACH

### §5.1 THE THREE DEMANDS — W-1 / W-2 / W-3

Their text, from `STAGE8_DEMAND_REGISTER_O25SR_V001.md:142-157` (seal OK),
quoted WHOLE as one operative block:

```text
W-1 (discharges FP-1): the certified sub-volume trace/HS rate for the dressed
    composite class — "verbatim MO-3, open of record"; carrier named CN-1 (R5):
    "member-named topologies with continuity proofs for Loc_N^phys, iotatilde_N^H,
    iota_N^H, Loc_N^C — no member exists in the scored corpus to name them";
    "the F1 escape is a certified sub-volume rate, i.e. a TOPOLOGY in which the
    dressed composites are controlled uniformly."
W-2 (discharges FP-2): the member-supplied sealed prequotient rule — CN-2 (R1):
    "a member-supplied sealed prequotient rule (JD-3/JD-3a) with one displayed
    evaluation on a named oriented k-cell — absent from the scored corpus";
    "a sealed member evaluation on a named cell would replace the diagonal-majorant
    accounting (F2's blocked side) with the junction object's own symbol-side value."
W-3 (discharges FP-3): the C-L2 certification at its consuming type — G_cm derived
    at the consuming (HS) type; "its only permitted certification (C-L2 quadratic
    form)" with "the operator-norm route excluded (||[h_0, 1_B]|| = +infinity)";
    retirement of witness E1_RECORD_KINK_COMMUTATOR_FORM_UNCERTIFIED is the
    registrar's upon its landing.
```

**TOKEN-PRESENCE TEST, RUN FILE BY FILE OVER EVERY ARTIFACT THAT CARRIES THE
`beta` OBJECT:**

```text
ARTIFACT                                   W-1 W-2 W-3 FP-1 FP-2 FP-3 G_cm prequot
────────────────────────────────────────────────────────────────────────────────
...JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003   0   0   0    0    0    0    0     0
...JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V001   0   0   0    0    0    0    0     0
...EQ6_DETERMINATION_MAP_LANE1_V001          0   0   0    0    0    0    0     0
...EQ6_MEMBERSHIP_THEOREM_LANE3_V001         0   0   0    0    0    0    0     0
...HUNT_CROSS_CHECK_AND_FRONTIER_LANE2_V001  0   0   0    0    0    0    0     0
...HOSTILE_WITNESS_CROSS_CHECK_LANE1_V001   20   0   1    0    0    0    0     0
```

The two nonzero cells are **a different namespace and are not the three
demands.** `STAGE8_TASK5_HOSTILE_WITNESS_CROSS_CHECK_LANE1_V001.md` labels its
witnesses `W-1 … W-19`; its hits read, quoted whole:

```text
    W-9 and W-16a make Loc the identity on
    the S_1 complement.  W-17 instead defines pi_Mx from the previously
    blocked on LM2-20.  W-1 cites the opposite statement as a premise.
```

```text
Density weights can change both matrices, but W-3/W-4 do not specify the
```

`W-1` there is a **witness index** in a list running to `W-19` (`W-13` supplies
the typed `beta` form quoted in §1.3), not "the certified sub-volume trace/HS
rate". Likewise the `W3` appearing in the assembly artifacts ("W3 restrictions
use the sealed response square", `...LANE2_V001.md:257`) is the **W3/DoR-008
finite restriction** generator class of `I_F`, quoted from that artifact's own
arrow list in §2.3 — again not W-3.

```text
Q5_W1 = DOES-NOT-TOUCH
Q5_W2 = DOES-NOT-TOUCH
Q5_W3 = DOES-NOT-TOUCH
```

No artifact carrying `beta` mentions a certified sub-volume rate, a
member-supplied prequotient rule, or `G_cm` at a consuming HS type. The
name-coincidence on the string `W-1`/`W-3` is displayed above precisely so that
it cannot be mistaken for reach.

### §5.2 THE NAMED FAILURE POINTS — FP-1 / FP-2 / FP-3

`FP-1`, `FP-2`, `FP-3` occur **0 times** in every artifact carrying `beta`
(table above). Corpus-wide they are substantial (`FP-1` 30 files/313 hits,
`FP-2` 27/310, `FP-3` 30/353 in ROOT1) — so this is not an absence of the
vocabulary from the corpus; it is an absence of contact between that vocabulary
and this object.

```text
Q5_FAILURE_POINTS = DOES-NOT-TOUCH
```

### §5.3 THE RECORD'S NAMED MISMATCHES — M-1 / M-2 / M-3

Named in `STAGE8_GAUGE_AS_CONTENT_O34SR_V001.md:564-567`, quoted whole in §1.4
above: `M-1 unmatched carriers / M-2 overlapping-not-identical cells / M-3
adjacency`. That artifact's VERDICT block, `:641-652`, quoted WHOLE from the
start of the entry to the end of its grade line — **begun at line 641 and not at
645, because the sentence running through 644-645 wraps mid-phrase ("quoted
inside two sealed / artifacts") and starting at 645 would have clipped it**:

```text
Q1  GAUGE STRUCTURE CARRIES RESIDUE IN EXACTLY ONE OBJECT AND ON NO RECORD DATA.
    The corpus contains one object of gauge type whose value on a
    failure-to-agree is a quantity: g_ij = exp(i theta_ij) in U(1), with
    triple-overlap cocycle g_ij g_jk g_ki = 1, quoted inside two sealed
    artifacts. It is defined on a patch family the corpus never constructs, and
    its transfer to the record's own incidence structure is flagged false in the
    corpus's own status block. It is defined on NONE of the record's three
    mismatches — the unmatched carriers, the overlapping-not-identical cells, or
    the demanded-never-held adjacency. AN OBJECT OF THE RIGHT TYPE ON THE WRONG
    DATA, AND SAYING SO IS THE COMPLETE ANSWER.
    GRADE: GAUGE-CARRYING. Not EM-carrying — the source is quoted as neither
    introducing `a` as a physical field nor identifying it with electromagnetism.
```

That passage is about `g_ij`, not about `beta`. For `beta` itself, the mismatch
tokens are absent from every `beta`-bearing artifact.

```text
Q5_NAMED_MISMATCHES = DOES-NOT-TOUCH
```

### §5.4 DOES ANYTHING RELATE `beta` TO THE U(1) TRANSITION FUNCTIONS, OR TO GAUGE STRUCTURE OF ANY KIND?

**CO-OCCURRENCE TEST, RUN OVER BOTH ROOTS.** Files containing both a `beta`
token (`beta_f|beta_nm|beta_nk|beta_gf`) and `g_ij`, and separately both a
`beta` token and `transition function|triple-overlap|triple overlap`:

```text
ROOT1, both tests, identical result — THREE corpus files:
  STAGE8_BOUNDARY_SHAPES_O32SR_AUDIT_V001.md
  STAGE8_GAUGE_AS_CONTENT_O34SR_V001.md
  STAGE8_GAUGE_AS_CONTENT_O34SR_AUDIT_V001.md
ROOT2, both tests: ZERO corpus files.
```

**All three are prior commission audits/determinations. NOT ONE is a
construction artifact. And all three place the two objects side by side only in
order to TYPE THEM APART.**

`STAGE8_GAUGE_AS_CONTENT_O34SR_V001.md:269-297`, quoted WHOLE — including the
clause that grants `beta` its strongest property, and carried past line 292's
wrap ("It fails a second time / on data:") to the end of the evidence it
introduces, so no sentence is cut at a line break:

```text
**NEAR-HIT A — the direct/two-step discrepancy cocycle `beta`.** This is the
corpus's one object whose *value on a disagreement is a quantity*.
`STAGE8_TASK5_HOSTILE_WITNESS_CROSS_CHECK_LANE1_V001.md:184-189` (seal OK):

```text
beta_nk
 =beta_mk compose S_nm + eta_mk compose beta_nm,
beta_nn=0.
```
```text
This is the direct/two-step discrepancy cocycle, including the necessary
precomposition.
```

```text
TAKES    a pair of routes (direct vs. two-step) between record stages that do
         not agree
YIELDS   a map, composed with S_nm and eta_mk — valued in the RESPONSE/
         TRANSPORT MORPHISM CLASS
```

**TYPED OUT: NOT AN OBJECT OF GAUGE TYPE.** It carries no U(1), no connection,
no group value. It is therefore not graded on the gauge/EM distinction — it is
not a hit under Question One's typing requirement at all. It fails a second time
on data: `STAGE8_TASK5_CONTINUUM_PACKAGE_ADOPTION_PROPOSAL_LANE2_V005.md:482`
(seal OK):

```text
| J13 | boundary/contact cocycle and safe ideal | **CONDITIONAL THEOREM ONLY** | closure hull `(O1-13)` preserves a supplied cocycle; no actual P7 discrepancy family exists to close |
```
```

(The inner ```` ```text ```` markers above are the SOURCE artifact's own fence
delimiters, reproduced rather than stripped. No word is elided.)

and its independent audit, `STAGE8_GAUGE_AS_CONTENT_O34SR_AUDIT_V001.md:348-354`
(seal OK), quoted WHOLE from the start of the finding — **begun at 348, not at
the eye-catching line 353, because the sentence wraps 352→353 ("for the same /
reason") and a shorter cut would have clipped it**:

```text
E-A returned **zero**. E-B returned exactly one hit, and it is the build's own
sentence. E-C returned four distinct corpus files, all in the T7 numeric lane
("cross-lane Strang-vs-RK4 transported comparison", "operator 2-norm, transported
comparisons") — quantities, but carrying no group value, no U(1), no connection.
They fail Question One's typing requirement in the same way, and for the same
reason, as the build's typed-out `beta_nk`. **No object of gauge type valued on a
real mismatch of record was found by any pattern.** Question One is not inverted.
```

```text
*** STATED EXACTLY, AS THE COMMISSION REQUIRES: ***

NOTHING IN THE CORPUS RELATES beta TO THE U(1)-VALUED TRANSITION FUNCTIONS.
No artifact writes beta in terms of g_ij, or g_ij in terms of beta; none maps
one domain to the other; none asserts a correspondence, an analogy, or a shared
class. The only three artifacts that mention both are prior AUDITS, and each
mentions both solely to record that beta is NOT of gauge type.
```

**ONE ADJACENCY, REPORTED SO THAT IT IS NOT MISTAKEN FOR A RELATION.** `beta_f`'s
defining transport `rho_f^C2` is built "including the endpoint and bundle data
supplied by DoR-020-A1" (§1.1), and a `U(1)`-bundle lift `tilde_f : P_n -> P_m`
sits among the forward legs of the same package morphism (§2.1), while the
sibling `C3` leg uses `j_f^fld`, "the support-local field/test transport derived
from the adopted U(1)-bundle lift" (`...LANE2_V001.md:280-281`). So a `U(1)`
**bundle** is present in the same structured tuple.

That is proximity in one morphism's data, **not** a relation between `beta` and
the transition functions. The corpus draws no such relation, and this artifact
authors none. The `U(1)`-bundle lift of `...LANE2_V001.md:97` and the transition
functions `g_ij` of `LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md` are not identified
with each other anywhere in the corpus either; that too is left as it lies.

```text
Q5_GAUGE_RELATION = DOES-NOT-TOUCH
  (with the adjacency above disclosed in full, and named as adjacency, not reach)
```

### §5.5 Q5 GRADE TABLE

| Target | Grade |
|---|---|
| named failure points (FP-1 / FP-2 / FP-3) | **DOES-NOT-TOUCH** |
| W-1, certified sub-volume rate | **DOES-NOT-TOUCH** |
| W-2, member-supplied prequotient rule | **DOES-NOT-TOUCH** |
| W-3, `G_cm` at a consuming HS type | **DOES-NOT-TOUCH** |
| the record's named mismatches (M-1 / M-2 / M-3) | **DOES-NOT-TOUCH** |
| U(1) transition functions / gauge structure of any kind | **DOES-NOT-TOUCH** — and three prior audits say so explicitly |

---

## §6 — Q6: THE SUBEXTENSIVE BOUND

### §6.1 THE CITING PASSAGE, QUOTED WHOLE

`STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md:408-419`, quoted
WHOLE — the set-up, the display, and the closing unit clause:

```text
For subextensivity, equip the finite pushout with its quotient norm.  If the
component bounds are `a_N` and `b_N`, then

||beta_N([r,b])|| <= a_N ||r|| + b_N ||b||,

and taking the infimum over all representatives of `[r,b]` gives the induced
quotient bound.  The sealed `a_N/Vol_N -> 0` and `b_N/Vol_N -> 0` estimates
therefore imply the glued subextensive estimate.  The R4 unit maps commute on
both injections and on `C_N`, so this argument supplies no undeclared unit
conversion.
```

### §6.2 WHAT THE "SEALED" ESTIMATES ACTUALLY SAY — THE SOURCES WERE SOUGHT AND ARE NOT THERE

The commission asks for these estimates "quoted from their own sources with
their hypotheses." **Their own sources do not exist in the corpus.**

```text
AUTHORITATIVE SWEEP, BOTH ROOTS, BARRED FILES EXCLUDED, LEAK-CHECKED:

TOKEN        ROOT1 files/hits   ROOT2 files/hits   WHERE
a_N/Vol_N        1 / 1              1 / 1          V003:416 — the citing sentence itself
b_N/Vol_N        1 / 1              1 / 1          V003:416 — the citing sentence itself
Vol_N            1 / 1              1 / 1          V003:416 — the citing sentence itself
```

**`Vol_N` occurs exactly once in the entire readable corpus, and that occurrence
is inside the sentence that calls the estimates "sealed."** There is no artifact
in either root that states `a_N/Vol_N -> 0`, states `b_N/Vol_N -> 0`, defines
`Vol_N`, defines `a_N` or `b_N` in this sense, or carries any hypothesis for
them. The other `a_N` tokens in the corpus belong to unrelated objects in
unrelated artifacts (an action coordinate `a_N in Act_N^quot`; `a_N(A)` in a
connection-lift spec; `b_N^m - a_N^m` in a square re-adjudication).

**THEREFORE: THE HYPOTHESES CANNOT BE REPORTED, BECAUSE THE ESTIMATES CANNOT BE
LOCATED.** This artifact does not reconstruct them, does not infer what they
would have to say, and does not supply them.

### §6.3 WHAT THE CORPUS DOES SAY ABOUT `beta` AND VOLUME

Two located statements exist, and both go the other way.

`STAGE8_TASK5_HUNT_CROSS_CHECK_AND_FRONTIER_LANE2_V001.md:223-232`, quoted whole
(overlapping §1.2 and repeated here because it is the operative Q6 text):

```text
The generated contact ideal is `{0}`, so no visible cycle is deleted.  This
is neither circular nor a blanket declaration about future new-edge
discrepancies.  The expression `beta/Vol` remains undefined until a positive
P4 volume exists; the hunt correctly leaves subextensivity conditional.

REF_PATH_KERNEL_TRANSPORT = CONFIRMED
REF_PATH_ZERO_COCYCLE = CONFIRMED
REF_PATH_SUBEXTENSIVITY = conditional_on_P4_density
```

```text
*** "The expression `beta/Vol` remains undefined until a positive P4 volume
    exists." — THE CORPUS'S OWN SENTENCE. `beta/Vol` occurs exactly ONCE in
    each root, and it occurs there to say the ratio IS NOT DEFINED. ***
```

`STAGE8_TASK5_EQ6_DETERMINATION_MAP_LANE1_V001.md:311-324`, quoted WHOLE
including the paragraph that qualifies the whole block:

```text
The stock proves, conditionally on an actual physical contact term:

I_contact is closed, invariant, restriction-natural, and bulk-cycle safe;
beta_(gf)=beta_g+Eta_g(beta_f);
beta_f/Vol_f -> 0 on admitted cofinal families;
OLD_FID + exclusive-region RNL + LR + Ward/bundle compatibility;
contact and disjoint diamonds compose when a coherent physical section exists.
                                                               (D2-4)

These facts are **PROVABLE**. The local-excision artifact expressly leaves
the positive-source physical contact term and coherent all-rank section
unproved. None of `(D2-4)` identifies the two maps on `C_N`.
```

This is the nearest thing in the corpus to the estimate V003 invokes, and its
hypotheses are stated on its own face:

```text
HYPOTHESES CARRIED BY beta_f/Vol_f -> 0, QUOTED FROM ITS OWN SITE:
  (H-a) "conditionally on an actual physical contact term"   ← governs the block
  (H-b) "on admitted cofinal families"                       ← in the line itself
  (H-c) graded "PROVABLE", not proved
  (H-d) same artifact: "The local-excision artifact expressly leaves the
        positive-source physical contact term and coherent all-rank section
        unproved."
```

Note also that the token differs: the determination map writes `beta_f/Vol_f`
(morphism-indexed), V003 writes `a_N/Vol_N` and `b_N/Vol_N` (stage-indexed
component bounds). The corpus does not connect these two notations, and this
artifact does not connect them.

### §6.4 WHAT THE BOUND DOES TO `beta`, STRUCTURALLY — COMPUTING NOTHING

Structurally, and computing no value of anything:

- `||beta_N([r,b])|| <= a_N ||r|| + b_N ||b||` is a **linear majorant** of the
  displayed quantity by the two component bounds. It is an upper bound only. It
  carries no lower bound and therefore, on its own face, permits the bounded
  quantity to be anything at or below the majorant — including zero.
- Dividing the component bounds by a volume and sending the ratios to zero is a
  **relative-smallness statement about the majorant**, not a statement about the
  bounded object's content. A quantity whose upper bound is subextensive relative
  to volume is thereby constrained from above and not at all from below.
- Whether that leaves room for content is therefore **not settled by these
  estimates as stated**, and in this corpus the question does not even reach that
  point, because (i) the estimates are not located at all (§6.2), (ii) the one
  located relative is explicitly conditional and "PROVABLE"-graded (§6.3), and
  (iii) the object being bounded is stated `= 0` at every site where it is
  evaluated (§1).

```text
*** THE BOUND CANNOT DRIVE beta TOWARD IRRELEVANCE RELATIVE TO VOLUME, BECAUSE
    THE CORPUS ALREADY PLACES beta AT ZERO WHEREVER IT EVALUATES IT. AN UPPER
    BOUND ON A QUANTITY STATED TO BE ZERO ADDS NOTHING TO ITS STANDING. AND THE
    ESTIMATES THAT WOULD SUPPLY THE BOUND ARE NOT IN THE CORPUS. ***
```

### §6.5 Q6 GRADE

```text
Q6_GRADE = INDETERMINATE-AT-BYTES
```

**Explicitly, which hypotheses each estimate carries:**

| Estimate | Hypotheses, at bytes |
|---|---|
| `a_N/Vol_N -> 0` | **NONE STATABLE — the estimate has no source in either root.** Called "sealed" at V003:416; `Vol_N` appears nowhere else in the corpus. Hypotheses unknown and unrecoverable at bytes. |
| `b_N/Vol_N -> 0` | **NONE STATABLE — same.** |
| `beta_f/Vol_f -> 0` (the located relative, different notation, in a different artifact) | "conditionally on an actual physical contact term"; "on admitted cofinal families"; graded **PROVABLE**; same artifact records the physical contact term as **unproved**. |
| `beta/Vol` generally | Stated **undefined**: "remains undefined until a positive P4 volume exists"; `REF_PATH_SUBEXTENSIVITY = conditional_on_P4_density`. |

The grade is INDETERMINATE-AT-BYTES and not SMALLNESS-STATEMENT, because a
smallness statement would require the estimates to say something, and they are
not present to say it. It is not GENUINE-BOUND-WITH-ROOM, because nothing at
bytes exhibits room and the bounded object is stated `= 0`.

---

## CHOICE LEDGER

| # | Choice | Alternatives considered | Why this one | Status |
|---|---|---|---|---|
| CH-1 | Grade Q1 **PROVEN-ZERO** rather than NEVER-EVALUATED | NEVER-EVALUATED (V003 itself never evaluates it); MIXED (three sites) | The corpus *does* evaluate it — three times, all zero, one of them inside the defining line. NEVER-EVALUATED would be false of `(C1-7)`, `(R1-6)/(R1-7)` and `beta_nn=0`. MIXED would be false because the sites agree. | **CLOSED** |
| CH-2 | Do **not** soften Q1 to VANISHES-UNDER-STATED-HYPOTHESES | That grade, on the strength of "on the old image" and the hostile qualification | The scope clause narrows *where the proof reaches*, it does not make the vanishing hypothetical. Both the scope ("on the old image") and the hostile qualification are quoted in full in §1.1/§1.3 so a reader can regrade on the same bytes. | **CLOSED** |
| CH-3 | Treat `beta_f` (morphism-indexed) and `beta_N([r,b])` (element-applied) as **not related by the corpus** | Assume `beta_N` is the operator whose value at `f` is `beta_f` | The corpus writes no such statement. `beta_N` in this sense occurs exactly once and is never defined. Assuming the relation would author a missing bridge. | **CLOSED** |
| CH-4 | Answer Q2's comparison from displayed **domains**, not names | Answer from the shared word "cocycle" | The commission forbids answering from names. Both indexing objects are displayed side by side from their own defining bytes in §2.4. | **CLOSED** |
| CH-5 | Grade Q3 **NEVER-CONSTRAINED**, not BOUNDED-ONLY | BOUNDED-ONLY, reading V003's `support` table row as a bound on `supp(beta_f)` | That row bounds the *glued carrier's* support, not `supp(beta_f)`. Merging them would be a misattribution; §3.3 quotes the row and separates them. | **CLOSED** |
| CH-6 | Do **not** infer `supp(beta_f) = empty` from `beta_f = 0` | Draw the inference and grade Q3 LOCALIZED | That inference is nowhere in the corpus. Drawing it would be authoring a missing clause — barred. §3.2 states the structural stake and stops. | **CLOSED** |
| CH-7 | Report DoR-020-A3/A4 as **absent from the corpus** rather than as sealed authority | Accept V003's citation-by-SHA as establishing the J13 laws of record | The files are not in either root (`find` returns 0 both times). A SHA citation to an unreadable file cannot be verified at bytes, and the commission requires seal verification of consumed artifacts. | **CLOSED** |
| CH-8 | Grade Q6 **INDETERMINATE-AT-BYTES** | SMALLNESS-STATEMENT (reading V003's sentence as the estimate) | V003's sentence *cites* estimates; it does not state them. `Vol_N` occurs once in the whole corpus — in that citation. A statement with no source cannot be graded as saying something. | **CLOSED** |
| CH-9 | Report the `beta_f/Vol_f` line as a **different-notation relative**, not as the cited estimate | Treat it as the source of `a_N/Vol_N -> 0` | Different tokens, different indexing (morphism vs. stage), different artifact, and the corpus never connects them. §6.3 displays both and declines the identification. | **CLOSED** |
| CH-10 | Disclose the `U(1)`-bundle **adjacency** in §5.4 rather than omit it | Omit it, since it is not a relation and the grade is DOES-NOT-TOUCH | Quotation-integrity discipline requires surfacing material that cuts against the grade. It is disclosed and explicitly named adjacency, not reach. | **CLOSED** |
| CH-11 | Re-run every sweep with **array-passed** globs after discovering the string-passed globs failed | Keep the original counts | The original method silently failed to exclude a barred file. All reported counts are from the corrected harness and are leak-checked. See FLAG BLOCK. | **CLOSED** |
| CH-12 | Read the prior audits O32SR / O34SR as **corpus artifacts**, and re-derive their claims at bytes rather than carry them | Treat them as catalogued negatives and decline to read | They are sealed determinations in the readable corpus, not declined paths. Every claim of theirs used here was re-verified against the primary source's own bytes (§1.1, §1.3, §2.4, §5.4). | **CLOSED** |

```text
OPEN CHOICES AT SEAL = 0
```

---

## TOY_SEPARATION

```text
ACTUAL SURFACE OF THE RECORD (what this determination touched, all seal-verified
except as flagged):
  beta_f := rho_f^C2(C2_m^fin) - C2_n^fin = 0   (C1-7), and its scope clause;
  beta_nm(H) := Kern_m^fin(j_nm^H H) - Pull_nm Kern_n^fin(H)  (R1-6), and
    beta_nl = 0 = beta_ml + eta_ml(beta_nm)  (R1-7);
  beta_nk = beta_mk compose S_nm + eta_mk compose beta_nm, beta_nn = 0;
  beta_gf = beta_g + Eta_g(beta_f) and (J13-1) on the glued carrier;
  ||beta_N([r,b])|| <= a_N ||r|| + b_N ||b||, and its citing sentence;
  P_N := (R_N^rep direct_sum I_N^contact)/Delta_N   (J12-2);
  I_F, its objects and its six generator classes;
  the FinPackage_020 morphism's forward and backward legs, and the symbol ledger;
  g_ij = exp(i theta_ij) in U(1) and g_ij g_jk g_ki = 1, with z_i : U_i -> C^2;
  the J13 status rows (CONDITIONAL THEOREM ONLY / KILL / KILL ON WITNESS / Ref_path);
  W-1, W-2, W-3 as the completion map displays them; FP-1/FP-2/FP-3; M-1/M-2/M-3.

*** NO ILLUSTRATIVE, TOY, MODEL, OR HYPOTHETICAL OBJECT WAS CONSTRUCTED BY THIS
    ARTIFACT — NOT ONE, ANYWHERE, INCLUDING IN FOOTNOTES AND ASIDES. THERE IS
    THEREFORE NO NON-CORPUS OBJECT TO DECLARE, AND NO FINDING RESTS ON ONE. ***

The one schematic device used is the annotated re-display of (J13-1) in §3.2
(the under-brace labelling "where the transported object lives" / "the image of
the original support" / "PLUS AN ALLOWANCE"). It is a TYPOGRAPHIC GLOSS ON A
QUOTED CORPUS LINE, introduces no symbol, asserts nothing the line does not, and
is declared here as non-corpus presentation. The Q3 grade rests on the sweep in
§3.3, not on this gloss.

NOT SURFACE — NOT TOUCHED, NOT BUILT, NOT SUPPLIED BY THIS ARTIFACT:
  no value, extent, bound, or locus for supp(beta_f);
  no inference from beta_f = 0 to supp(beta_f) = empty;
  no bridge between beta_f and beta_N([r,b]);
  no reconstruction of the a_N/Vol_N or b_N/Vol_N estimates or their hypotheses;
  no definition of Vol_N, a_N, or b_N;
  no relation between beta and g_ij, and no gauge typing of beta;
  no patch family, cover, or nerve;
  no restatement, repair, or withdrawal of any J13 law;
  no adoption, advocacy, or recommendation of anything.
```

---

## SWEEP CUTOFFS

**HARNESS.** All counts below were produced by a single leak-checked harness run
separately over each root, with the bar globs passed as a **zsh array** (one
argv word per glob). Every row was additionally tested for barred-file leakage;
the leak column was **0 on every pattern in both roots**. Corpus files only;
this artifact's own file excluded from ROOT1 counts.

```text
BAR GLOBS APPLIED TO EVERY PATTERN BELOW:
  !*REGISTER*  !*EXECUTION_TRACKER*  !*THE_PLAN*  !*ROAD_REMAINING*
  !*THE_HANDOFF*  !*OBSERVATIONS_REGISTER*  !*DECISION_SHEET*  !*_ADDENDUM*
  !alpha_supervision/**  !STAGE8_DISCREPANCY_COCYCLE_O38SR*
```

| # | Pattern | ROOT1 files/hits | ROOT2 files/hits | Where this sweep was stopped, and why |
|---|---|---|---|---|
| S-1 | `beta_f` | 30 / 52 | 27 / 30 | All 30 ROOT1 files opened at the hit line. **Only 6 carry the object**; the rest are the fence token `beta_function_computed`, the guard `beta_family_survives`, or a JSON path `sympy/functions/special/beta_functions.py`. Stopped after typing every hit. |
| S-2 | `beta_gf` | 2 / 5 | 1 / 1 | All opened. |
| S-3 | `beta_nm` | 6 / 12 | 5 / 11 | Opened at the two defining sites (`(R1-6)/(R1-7)`, typed form); remainder are citations of those. |
| S-4 | `beta_nk` | 4 / 10 | 2 / 2 | All opened. |
| S-5 | `beta_N` | 15 / 47 | 15 / 48 | All 15 ROOT1 files opened. **Exactly one is the V003 usage**; the other 14 are unrelated homonyms in other artifacts (`beta_NM` CTP stage maps, `beta_N : O_prof,N -> I_N^q`, `beta_N : Bot_N -> R`). Enumerated in §2.2. |
| S-6 | `beta_R` | 10 / 20 | 8 / 17 | Sampled at the V005 proposal site (`"The cocycle is the actual discrepancy beta_R"`). Not pursued further: V005 is `PROPOSED_NOT_ADOPTED` and this is a fourth naming variant, recorded but not load-bearing. **Stopped deliberately.** |
| S-7 | `supp\(beta` | 2 / 8 | 1 / 1 | **Exhaustive — all 9 hits opened.** ROOT1: V003 `:395` (1) and the O32SR audit (7, all quoting/discussing `:395`). ROOT2: V003 `:395`. Basis of the Q3 grade. |
| S-8 | `beta_f :=` | 2 / 3 | 1 / 1 | **Exhaustive.** One defining artifact; the other ROOT1 file is the O32SR audit quoting it at `:366` and `:910`. |
| S-9 | `discrepanc` | 139 / 602 | 127 / 611 | **NOT exhausted — 139 files is beyond byte-level reading in this commission.** Narrowed by the two sub-patterns S-10 and S-11, which localise the object. Stopped there, and the residue is disclosed as unread. |
| S-10 | `discrepancy cocycle` | 6 / 25 | 4 / 5 | **Exhaustive — all 6 ROOT1 files opened.** This is the pattern that locates the object. |
| S-11 | `defect term` | 10 / 30 | 7 / 12 | Sampled; the phrase is a *shape name* supplied by prior commissions, not the record's vocabulary (per O32SR §0). Stopped after confirming it names no additional corpus object. |
| S-12 | `J13` | 35 / 126 | 32 / 107 | Narrowed to law-statement and status contexts; the four status rows quoted in §4.3 were opened at bytes. Remaining hits are citations. **Stopped at the status rows.** |
| S-13 | `a_N/Vol_N` | 1 / 1 | 1 / 1 | **Exhaustive.** Q6 basis. |
| S-14 | `b_N/Vol_N` | 1 / 1 | 1 / 1 | **Exhaustive.** Q6 basis. |
| S-15 | `Vol_N` | 1 / 1 | 1 / 1 | **Exhaustive.** The single occurrence is the citing sentence itself. |
| S-16 | `Vol_f` | 1 / 1 | 1 / 1 | **Exhaustive.** The determination map's `beta_f/Vol_f` line. |
| S-17 | `beta/Vol` | 1 / 1 | 1 / 1 | **Exhaustive.** The "remains undefined" sentence. |
| S-18 | `subextensiv` | 91 / 177 | 85 / 153 | **NOT exhausted.** Read only where it co-occurs with `beta` (V003 §4.3, the hunt cross-check, the determination map, the adjudication row). Residue disclosed as unread. |
| S-19 | `g_ij` | 26 / 83 | 9 / 25 | Read at the defining artifact and at the three audits that also carry `beta`. Basis of §2.4 and §5.4. |
| S-20 | `triple-overlap` | 11 / 22 | 4 / 4 | Read at the defining artifact and the co-occurrence files. |
| S-21 | `transition function` | 20 / 46 | 13 / 26 | Same; used for the co-occurrence test in §5.4. |
| S-22 | `patch famil` | 6 / 16 | 1 / 5 | **Exhaustive — all opened.** Basis of the "never constructs" finding. |
| S-23 | `W-1` | 81 / 524 | 8 / 62 | **NOT exhausted corpus-wide.** Exhaustively tested on the 6 `beta`-bearing artifacts (the only thing Q5 needs); the one hit-set found there was opened and shown to be a different namespace. |
| S-24 | `W-2` | 66 / 517 | 2 / 7 | Same method, same cutoff. Zero hits in `beta`-bearing artifacts. |
| S-25 | `W-3` | 69 / 504 | 3 / 7 | Same method, same cutoff. One hit in a `beta`-bearing artifact, opened, different namespace. |
| S-26 | `G_cm` | 46 / 198 | 6 / 12 | Same method. **Zero** in `beta`-bearing artifacts. |
| S-27 | `prequotient` | 47 / 108 | 25 / 48 | Same method. **Zero** in `beta`-bearing artifacts. |
| S-28 | `sub-volume rate` | 20 / 41 | 0 / 0 | Read at the demand register for the W-1 text. |
| S-29 | `FP-1` | 30 / 313 | 0 / 0 | Same method. **Zero** in `beta`-bearing artifacts. |
| S-30 | `FP-2` | 27 / 310 | 0 / 0 | Same method. **Zero** in `beta`-bearing artifacts. |
| S-31 | `FP-3` | 30 / 353 | 0 / 0 | Same method. **Zero** in `beta`-bearing artifacts. |
| S-32 | `DOR_020` | 31 / 63 | 28 / 60 | All are citations. Paired with `find -iname "*DOR_020*"` → **0 files in both roots**. Basis of §4.3. |
| S-33 | `nonzero` (and `nonzero.*beta`, `beta.*nonzero`, `beta != 0`, `beta_f != 0`) | 7+4+1+0 hits on the beta-adjacent forms | comparable | **Exhaustive on the beta-adjacent forms — all opened.** Every hit belongs to an unrelated object (a chiral involution `beta`, ray averages `beta_s`, `beta_G`, a sympy symbol). **No nonzero discrepancy cocycle anywhere.** Q1 basis. |
| S-34 | co-occurrence: `beta_f\|beta_nm\|beta_nk\|beta_gf` × `g_ij` | 3 corpus files | 0 corpus files | **Exhaustive — all 3 opened.** All are prior audits; all type the two apart. |
| S-35 | co-occurrence: same × `transition function\|triple-overlap\|triple overlap` | 3 corpus files | 0 corpus files | **Exhaustive.** Identical file set to S-34. |
| S-36 | `find -iname "*DOR_020*"` / `"*dor*020*"` | 0 | 0 | **Exhaustive.** |

---

## FLAG BLOCK

### Fence line

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

No numeric value of any coupling, scale, root, eigenvalue, norm, or constant was
computed. No comparison to any measured value was made. Every statement in this
artifact is symbolic or structural. Fence tokens appear only inside quotation and
in this declaration.

### Seal tally

```text
ARTIFACTS CONSUMED = 23
  shasum -a 256 -c OK, run from each artifact's own directory   = 21
  sidecar malformed but content hash MATCHES exactly            =  1
  no sidecar in either root — UNVERIFIABLE                      =  1
  MISMATCH                                                      =  0
```

**No seal mismatch was found, so no STOP condition fired.** Two disclosures:

1. `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V004.md.seal.sha256` uses
   a **single space** between digest and filename where `shasum -c` requires two.
   `shasum -a 256 -c` therefore reports "no properly formatted SHA checksum lines
   found" rather than OK. The content was verified by direct comparison:
   computed `9bf34e27da9aca51966feb2b41f34b0060e2121bd85d783d35a81685bbb63514`,
   sidecar records the identical digest. **The artifact is intact; the sidecar's
   formatting is defective.** Reported, not repaired — repair is not this lane's
   authority.
2. `LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md` has **no sidecar in either root**. It
   is the source of the `g_ij` definition quoted in §2.4. That quotation is
   flagged at its point of use and in the §4.4 standing table as **unverifiable
   at seal**. The Q2 comparison does not depend on it alone: the same `g_ij`
   text is carried inside two independently seal-verified artifacts
   (`STAGE8_CANONICAL_PATCH_COVER_TO_INCIDENCE_GRAPH_FUNCTOR_ATTEMPT_V001.md`
   and `STAGE8_RECORD_SIDE_PATCH_DEFINITION_SWEEP_V001.md`), both OK.

Additionally, two sidecars (`STAGE8_RECORD_SIDE_PATCH_DEFINITION_SWEEP_V001.md`,
`STAGE8_CANONICAL_PATCH_COVER_TO_INCIDENCE_GRAPH_FUNCTOR_ATTEMPT_V001.md`) name
**absolute ROOT2 paths** rather than basenames. They verify OK from the ROOT1
directory because the absolute path resolves. Noted, not a defect of content.

### Register-bar incidents

```text
INCIDENTS = 1  (detected, contained, and corrected before any use)
```

**INCIDENT R-1.** During an intermediate co-occurrence sweep over ROOT2, the
result listing included one line naming a barred file:
`./QUESTIONSSETTLED_REGISTER_V001.md`. Actions taken:

- The file was **never opened, never grepped for content, and never quoted.**
  Only its name appeared, in a `-l` (names-only) listing.
- The line was **discarded** and plays no part in any finding.
- **Root cause, diagnosed rather than guessed:** the bar globs were being passed
  as a single space-joined **string** variable. With one glob the exclusion
  fired; with two or more it silently stopped firing. Bisection confirmed the
  behaviour (`leak=0` with one glob, `leak=1` with any second glob added), and
  literal quoted arguments never leaked.
- **Correction:** every sweep was **re-run from scratch** with the globs held in
  a **zsh array**, one argv word per glob, plus an explicit per-pattern
  barred-leak counter. **All 36 rows in SWEEP CUTOFFS report leak = 0.** The
  counts in this artifact are the corrected ones; the pre-correction counts were
  discarded.
- No barred file's *contents* entered this artifact at any stage.

### Defects found in this artifact's own draft on self-check

```text
DEFECTS FOUND AND FIXED BEFORE SEAL = 6
```

| # | Defect in the draft | Fix |
|---|---|---|
| D-1 | §1.1 asserted the sweep `beta_f :=` "returns exactly ONE file in ROOT1". The corrected harness returns **2 files / 3 hits** in ROOT1 — a **false count**, and exactly the class of error this program's sweep discipline exists to catch. | Rewritten to report 2/3 and 1/1 with both extra hits attributed to the O32SR audit *quoting* the definition. The substantive claim (one definition, one defining artifact) survives and is now stated precisely. |
| D-2 | §5.3 quoted `STAGE8_GAUGE_AS_CONTENT_O34SR_V001.md` beginning at line 645, which **starts mid-sentence** — the sentence wraps across 644→645 ("quoted inside two sealed / artifacts"). This is the exact line-wrap trap the commission warns about. | Quote re-cut to begin at line 641 (start of the entry) and extended through 652 (end of the grade line). |
| D-3 | §5.4 quoted O34SR `:269-290` ending at "…typing requirement at all", one physical line before the wrap "It fails a second time / on data:", and had **flattened the source's internal code-fence delimiters**. | Quote extended to `:269-297` so the following sentence and the evidence it introduces are included; the source's own inner fences are now reproduced, with a note that no word was elided. |
| D-4 | The sweep counts in the first draft were produced by the defective string-glob harness (see R-1) and were therefore untrustworthy — several differed from the corrected values (e.g. `subextensiv` 92→91 files, `g_ij` 25→26, `triple-overlap` 10→11, `W-1` 516→524 hits). | All counts replaced with corrected, leak-checked values. |
| D-5 | **Four line-range citations were wrong**, each off by a few lines because the draft cited the span it had *read* rather than the span it had *quoted*: the hunt cross-check cited `:206-224` (actual `:208-226`) and again `:219-224` (actual `:223-232`); the determination map cited `:310-321` (actual `:311-324`); the demand register cited `:142-158` (actual `:142-157`, 158 being the closing fence). The quoted *text* was correct in every case. | All four re-checked line by line against `awk`-numbered output and corrected. |
| D-6 | §5.4's quote of the O34SR **audit** began at line 353, **mid-sentence** — the sentence wraps 352→353 ("for the same / reason"). Same trap as D-2, caught on a second pass. | Quote re-cut to begin at line 348, the start of the finding, and carried through 354. |

### Standing of this artifact

```text
ARTIFACT_TYPE = READ_AND_CLASSIFY_DETERMINATION
DETERMINATION ONLY. Nothing is constructed, proposed, adopted, advocated,
recommended, or supplied. No object, principle, or clause is authored.
NO GIT ACTION TAKEN. NO REGISTER, TRACKER, PLAN, OR ROAD FILE TOUCHED OR READ.
```

### Grades at a glance

```text
Q1  IS beta EVER NONZERO?      PROVEN-ZERO   (C1-7, scope: "on the old image";
                                              corroborated at (R1-6)/(R1-7) and
                                              beta_nn=0; NO nonzero exhibit anywhere)
Q2  TYPE AND DOMAIN            record's own structure (I_F arrows, C2^fin datum);
                               domain is a DIFFERENT OBJECT from the patch family
Q3  THE SUPPORT LAW            NEVER-CONSTRAINED
Q4  ADOPTION STATUS            NOTHING OF RECORD; V003 DEFECTIVE, LANE2_V001 KILLED,
                               DoR-020-A4 ABSENT FROM THE CORPUS
Q5  REACH                      DOES-NOT-TOUCH on every target, including gauge
Q6  THE SUBEXTENSIVE BOUND     INDETERMINATE-AT-BYTES (cited estimates have no source)
```

**END OF DETERMINATION.**
