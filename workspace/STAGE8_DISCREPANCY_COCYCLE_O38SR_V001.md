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
`beta_f :=` returns exactly ONE file in ROOT1 and exactly ONE in ROOT2 — this
artifact, this line.

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
`:206-224`, quoted WHOLE:

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
