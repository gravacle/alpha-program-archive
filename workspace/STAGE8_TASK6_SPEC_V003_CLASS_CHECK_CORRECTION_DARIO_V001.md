# STAGE 8 / TASK 6 / SUBGATE — THE CORRECTION OF RECORD + THE CARRIED FINDINGS VERIFIED — DARIO V001

Lane: Dario (Claude Opus 5), cross-family custody reviewer
Task: PASTE 637 / Task 6 subgate — correction of my sealed class-check, and personal
verification of the carried findings
Authority: DoR-020-A8. **THIS ARTIFACT AUTHORIZES NOTHING AND LIFTS NO GATE.**
Corrects: `STAGE8_TASK6_SPEC_V003_CLASS_CHECK_DARIO_V001.md` =
`01adfa83043bf1e01ffa965a7f955ebcce6b74b27e4e6728b71c375df7976063`, which **stands
sealed and is not overwritten**. This artifact is the correction; that one is the
record of what I sealed.

```text
REGISTER_HEAD = Q-573
WITHDRAWAL = stated
V009_04 = FATAL_CONFIRMED
SP1_05 = UNBOUND_CONFIRMED
TEN_FINDINGS = 6 confirmed / 2 refuted (8 findings across 7 rows)
V004_SCOPE = closed_list (+11 repairs, +2 rules = 13)
CLASS_RULE = proposed (BR-1, BR-2 — text at §3.3)
VERB_AUDIT_SELF = CLEAN (+1 self-caught severity error, recorded at §4.4)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**The single most useful sentence in this artifact:** hash-pinning prevents
*substitution*, not *fabrication*. The spec already requires every indexed manifest
to be content-addressed and `P0`-verified (`:340-342`). That stops a producer
swapping a manifest after the fact. It does nothing to constrain **what was pinned
in the first place** — and six rows route their blocker's directional demand
through exactly such an object. That is one gap, not six, and §3.3 proposes closing
it as law.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-573 | verified |
| My sealed check = `01adfa83043bf1e01ffa965a7f955ebcce6b74b27e4e6728b71c375df7976063` | **verified** — stands sealed, not overwritten |
| Spec under finding = `f910815c84fd29d3dc6ca55f43ebe5d4c7015f457ddcde7bd7a69afdf81658dc` | **verified before reading** |
| Census source = `c09f2c246c48ddfd0df127da26a22f08ba9ffd44f5c2118c178a0a5eba5d00e8` | verified |
| Output name collision | none — clear to write |

Archive-side only. Declared conventions for this artifact: all row/blocker citations
are line numbers in the fixed byte subjects above; all searches are `grep -F`
fixed-string unless stated.

---

## 1. N1 — THE CORRECTION OF RECORD

### 1.1 `RE_RENDERS = 28/28 CONFIRMED` — **WITHDRAWN**

[PROVABLE] My sealed check's final line reads `RE_RENDERS = 28/28 CONFIRMED`. It is
withdrawn. At least two of the twenty-eight are defective — `C-B-V009-04` (§1.2)
and `C-B-V011-MR-07` (§2.6) — and four more carry confirmed material defects
(§§2.3–2.5, 2.7). The corrected value is **22/28 confirmed, 6 defective.**

[YOURS] **The verdict-line/scope mismatch, named plainly.** My §2.4 stated the
coverage boundary correctly and in advance: mechanical on all 28, semantic in full
on 7, and *"I do not claim row-by-row semantic verification of all 28."* The
boundary was accurate and the defects landed exactly inside it. **The failure was
not the analysis; it was the headline.** `28/28 CONFIRMED` is the line a reader
quotes, registers, and builds on, and it asserted more than the paragraph beneath
it conceded. A caveat in the body does not license an over-claim in the verdict
line — the verdict line must be no stronger than the weakest thing it summarizes.
Had I written `22/28 CONFIRMED / 21 NOT SEMANTICALLY VERIFIED`, the register would
have carried the truth and this relay would be routine rather than corrective.

That is the VERDICT-LINE SCOPE RULE, and it is now process law because I broke it.

### 1.2 `C-B-V009-04` — **FATAL, confirmed at source**

[PROVABLE] **The sealed blocker** (ledger `:113-114`):

> *"4. The formal I-adic logarithm, holomorphic principal logarithm, and
> norm-convergent Taylor series were not assigned their **distinct domains**."*

[PROVABLE] **The deleted directional predicate.** V002's row (`:420`) required:

> *"**exactly one licensed dispatch occurs at every admitted input**, out-of-domain
> points fail, and Taylor use includes its norm bound"*

V003's row (`:434`) retains only the third atom as `r_bound:=EXACT(taylor_norm_bound)`
and replaces the first two with a single per-input comparison. **The directional
predicate was deleted and no receiver was supplied in its place.**

[PROVABLE] **The producer-declared object with no content-forcing opcode.** The only
per-input conjunct is

```text
r_dispatch_x := COMPARE({r_formal_x.status, r_principal_x.status, r_taylor_x.status},
                        E_log[x], empty)
```

`COMPARE` is defined at `:338` as *"Canonicalize only the predeclared process-local
fields in `mask`, then require byte equality of all other fields."* It is a
**symmetric byte equality** between a computed triple and the producer's own
declaration of that triple. It has no directional force.

[PROVABLE] **The `.success` bits are absent from PASS.** The criterion is

```text
P0 and r_enum.success and r_ids.success and r_bound.success
    and (for every x in r_enum.items: r_dispatch_x.success)
```

`r_formal_x.success`, `r_principal_x.success` and `r_taylor_x.success` **do not
appear**. Only their `.status` fields feed the comparison, so even a `DOMAIN`
failure is absorbable by declaring that status in `E_log[x]`.

[PROVABLE] **The distinctness identifiers occur once.** `D_formal`, `D_principal`,
`D_taylor`, `E_log`, `G_log_domain`, `log_formal`, `log_principal`, `log_taylor`
and `taylor_norm_bound` occur in the entire 1,490-line spec **only at line 434**.
No schema, `EXACT`, `KERNEL`, fixture, second row or global rule constrains them.
`DOMAIN(f,D)` is defined as *"Prove from the typed graph that `f` is used exactly
on `D`"* — it pins each map to its own domain and says nothing about the three
domains relative to one another.

[PROVABLE] **The failure scenario.** A producer sets
`D_formal[x] = D_principal[x] = D_taylor[x] = D` for every enumerated `x` — the
three logarithms sharing one domain, which is the literal pre-fix defect the
blocker names — and declares `E_log[x] = {IN_DOMAIN, IN_DOMAIN, IN_DOMAIN}`. Then
every `DOMAIN` call reports in-domain, `r_dispatch_x.success` holds for every `x`,
`r_enum`/`r_ids` hold over the producer's own grammar/ledger pair, and `r_bound`
holds independently. **The row PASSES with all three domains identical.**

[YOURS] The row cannot fail for the blocker's stated reason. Distinctness — the
whole demand — has no receiver. The spec's own audit note at `:690` concedes it
without noticing: it claims the re-render bound *"the domain partition's
completeness and dispatch comparison"* and never claims distinctness was bound,
yet `:1485` counts the row inside `BINDING_SWEEP = 66/66`.

**Class: producer-suppliable object + missing receiver. This is the SP1-07 class
recurring in a different row.**

### 1.3 `C-B-V011-SP1-05` — the ordering atom re-graded **UNBOUND**

[PROVABLE] The row (`:486`) is graded **BOUND**. Its criterion is

> *"the family is **exhaustive** in the declared class and **selection occurs only
> after enumeration**"*

with procedure *"`ENUM` grammar with independent completeness certificate; `TYPE`
every candidate."*

[YOURS] **I re-grade my own finding upward.** In my sealed check I charged this row
at MATERIAL on the word `exhaustive`, reasoning that `ENUM(grammar,cert)` receives
completeness — which is true. **I under-graded it, because I audited the adjective
and not the second atom.** *"Selection occurs only after enumeration"* is an
**ordering** claim. `ENUM` establishes completeness; `TYPE` validates candidate
structure. Neither establishes that no selection preceded the enumeration — that
would need an `M2` query over the selection sources, or a `DAG` ordering, and the
row has neither.

So the row carries one atom that is under-notated (`exhaustive`, receiver present)
and one that is **UNBOUND** (ordering, no receiver at all). **Class: missing
receiver.**

---

## 2. N2 — THE CARRIED FINDINGS, VERIFIED PERSONALLY AT SOURCE

I verified each at source against its sealed blocker and the opcode definitions at
`:305-340`. **I relay nothing as mine that I did not display.** Two are refuted.

### 2.1 The definitional facts that decide four of these

[PROVABLE] Three opcode definitions, quoted from `:305-340`, do most of the work:

```text
COMPARE(x,y,mask)  Canonicalize only the predeclared process-local fields in mask,
                   then require byte equality of all other fields.
SYMBOLIC(e)        Reduce a declared symbolic expression/limit exactly; permitted
                   only in a GATED-EXECUTION row after its gate opens.
EXACT(e)           Normalize ... and compare canonical normal forms.
```

[PROVABLE] Two consequences, both load-bearing below:

1. **`COMPARE` is symmetric.** Compared against a producer-declared expectation it
   is a self-consistency check and carries no direction.
2. **`SYMBOLIC(e).success` is not a truth value.** It means the reduction
   succeeded, not that `e` holds. `EXACT` differs — it *compares normal forms*, so
   its success does carry an equality outcome.

### 2.2 `C-B-V010-05` — alleged FATAL — **REFUTED**

[PROVABLE] The row is **byte-identical in V002 (`:439`) and V003 (`:453`)**. Its
criterion is *"coordinate-shape factors cancel from the local coefficient without
an inserted compensator and covariance holds for every sealed fixture"*, with
procedure *"`EXACT; UNITS` transform every fixture"* over *"anisotropic symbolic
fixtures."*

[YOURS] **The receiver exists, so I refute the FATAL.** `EXACT` compares canonical
normal forms across the transformed fixtures. An inserted compensator changes the
normal form, so `EXACT` fails — the absence claim is received, not floating. The
blocker (`:158`) asks to *"Prove anisotropic scale cancellation from an exact
tetrad/Hodge face measure"*, and `EXACT` + `UNITS` over every sealed anisotropic
fixture is a genuine receiver for exactly that.

**Downgraded to MINOR**, and only this: unlike its sibling `C-B-V010-01`, the row
enumerates no compensator-mutation grammar, so its coverage rests on the sealed
fixture set being adequate. That is a completeness question about fixtures, not an
unbound obligation. **Class: none (refuted); residual MINOR = fixture coverage.**

### 2.3 `C-B-V011-SP2-05` — alleged FATAL — **REFUTED**

[PROVABLE] Also **byte-identical in V002 (`:486`) and V003 (`:500`)**. Its criterion
is a pure conjunction of eleven opcode success bits. The blocker (`:205`) demands
one global carrier from cell pushouts, covariance/associativity proved, SP17
recovered, primitive overlap kept distinct from `h_K^2`, and the quartic competitor
rejected. Each has a receiver:

```text
r_enum_pushout / r_enum_orientation      ENUM with independent completeness certificates
r_compare_pushout_index                  COMPARE(r_enum_pushout.ids, p_pushout.index, empty)
r_compare_orientation_index              COMPARE(r_enum_orientation.ids, p_orientation.index, empty)
r_kernel_covariance                      KERNEL replay of the covariance/associativity bundle
r_kernel_quartic                         KERNEL replay of the quartic rejection
r_compare_axioms                         COMPARE(used_axiom_hashes, allowed_axiom_hashes, empty)
```

[YOURS] The prose quantifier *"over every associativity/relabeling and orientation
square"* is not loose: the two index comparisons force the proof index to equal the
**complete** enumeration with empty difference, so the replayed bundle covers
exactly the enumerated squares. This is also the row I verified personally at
Q-567 as a model repair, and nothing has changed in it since. **Refuted. Class:
none.**

### 2.4 `C-B-V010-01` — alleged MATERIAL — **CONFIRMED**

[PROVABLE] Blocker (`:154`): *"Reproduce the nonextensive direct-sum response with
zero thermodynamic stiffness and **reject every after-the-fact extensive factor**."*
V002's criterion (`:435`) carried the direction: *"every inserted `L^2`, `L^4`,
cell-volume, or equivalent post-hoc factor **fails**."* V003 (`:449`) replaces it
with

```text
for every m: r_m := SYMBOLIC(m(V010_canonical_response))
             r_cmp_m := COMPARE(r_m.classification, E_factor[m], empty)
```

`E_factor` occurs **once in the spec, at line 449**, and no opcode forces its
content. A producer declaring `E_factor[m] = ACCEPTED` for a post-hoc factor that
should be rejected passes the row. The ledger is *named* an "expected rejection
ledger", but a name is not an opcode — which is the standard this whole review
exists to apply. **Class: producer-suppliable object. MATERIAL.**

[YOURS] I note in fairness that this row is **better built than V009-04**: its
per-item `.success` bits *are* conjoined, and `r_domain` pins the limit domain. Only
the direction is unforced.

### 2.5 `C-B-V010-13` — alleged MATERIAL — **CONFIRMED (two defects)**

[PROVABLE] Blocker (`:166`): *"Make the holdout universe exhaustive, canonical,
**independently committed**, externally beaconed, and structure-sensitive."*

**(a) Independence has no receiver.** The row (`:461`) discharges the custodian with
`r_custodian := TYPE(G_custodian)`. `TYPE(g)` is defined as *"Validate every object,
domain, codomain, decoration, identity, and composable edge in graph `g`"* — it
validates a graph's internal well-formedness. **Independence is a relational
property between custodian and producer**, and no opcode in the row establishes it.

**(b) The failure direction is producer-declared.** *"Any contamination or drift
fails"* is discharged by `r_cmp_m := COMPARE(r_m.normal_form, E_holdout[m], empty)`.
`E_holdout` appears only in descriptor rows (`:443`, `:461`) and in no constraining
rule, so a producer declaring the contaminated normal form as expected passes.

[YOURS] The row's outcome-access leg *is* properly bound —
`r_access := M2(q_outcome, preseal_sources)` with `r_access.hits = empty` is a real
directional predicate, and it shows the author knew how to write one. **Class: (a)
missing receiver; (b) producer-suppliable object. MATERIAL.**

### 2.6 `C-B-V011-MR-07` — alleged FATAL + MATERIAL — **BOTH CONFIRMED**

[PROVABLE] Blocker (`:179`): *"Prove the certified zero-free domain **contains** the
independently derived record interval."* The row (`:474`) ends:

```text
for every f in r_enum.items:
    r_f := SYMBOLIC(containment(E_zero_free.tau_R, E_zero_free.domain, f))
PASS iff  P0 and ... and (for every f in r_enum.items: r_f.success)
```

[PROVABLE] **`r_f` is an unpaired reduction, and it carries the blocker's verb.**
`SYMBOLIC(e).success` means the reduction succeeded, not that the containment
holds, and **no `COMPARE` pairs `r_f`**. A containment that reduces cleanly to FALSE
yields `r_f.success = true` and the row passes.

[PROVABLE] **Displayed contrast, one line away.** I swept every row for a bare
`SYMBOLIC(...).success` conjoined without a companion `COMPARE`. **Exactly two
exist:**

```text
C-B-V010-01   r_response.success   (a reduction of the response — asserts nothing)
C-B-V011-MR-07 r_f.success         (THE ASSERTION — containment)
```

and `C-B-V010-01` shows the correct pattern in the same file:
`r_m := SYMBOLIC(...)` **paired with** `r_cmp_m := COMPARE(r_m.classification, …)`.
MR-07 omits exactly that pairing on exactly the atom that matters.

[PROVABLE] **The MATERIAL half also holds.** `r_domain := DOMAIN(response,
E_zero_free.domain)` and both `COMPARE`s route through `E_zero_free`, which occurs
**once, at line 474**, unconstrained. So even the domain the containment is tested
against is producer-declared.

[YOURS] `r_zero` and `r_tau` *are* genuine `KERNEL` replays with their conclusions
compared — the proofs are properly bound. What is missing is the truth of the
relation between them. **FATAL. Class: missing receiver (primary) + producer-
suppliable object (secondary).**

### 2.7 `C-B-V011-MR-05` — alleged MATERIAL — **CONFIRMED**

[PROVABLE] Blocker (`:177`): *"**Resolve** continuous-sum, ordered, sequential,
Trotter, and circuit evolutions."* V002 (`:458`) carried the direction:
*"inequivalent forms **remain distinct** on the fixture."* V003 (`:472`) replaces it
with `r_cmp_e := COMPARE(r_e.normal_form, E_evolution[e], empty)`.

`E_evolution` occurs **once, at line 472**. **Nothing requires the five declared
normal forms to differ from one another.** A producer declaring identical normal
forms for all five evolutions passes the row while the forms are unresolved — which
is the blocker's defect.

[YOURS] This is **the same distinctness gap as `C-B-V009-04`**, in a different
family. Two independent rows losing the identical property in the identical way is
what makes this a class rather than two bugs. The row's other half — *"exactly one
adopted/derived rule"* — **is** bound, by `r_selected := COMPARE(M_rule.rule_id,
E_evolution.selected_rule_id, empty)` plus the `KERNEL` provenance replay.
**Class: missing receiver (distinctness). MATERIAL.**

### 2.8 `C-B-V011-SP1-02` — alleged MATERIAL — **CONFIRMED**

[PROVABLE] Blocker (`:188`): *"**Derive** the chiral-odd boundary map as a
Lorentz-covariant **intertwiner**."* V003 (`:483`) binds the derivation properly —
`r_selected := KERNEL(p_selected_map, proof_axioms)` with
`r_selected_cmp := COMPARE(r_selected.conclusion, E_map.selected_map, empty)`.

The **intertwining** half is not: `r_g := EXACT(Lorentz_square(E_map.selected_map,
g))` with `r_cmp_g := COMPARE(r_g.normal_form, E_map[g], empty)`. The intertwining
relation should be an identity (the Lorentz square vanishing or matching a fixed
form); instead the computed normal form is compared to a **producer-declared**
`E_map[g]`. `E_map` occurs **once, at line 483**.

[YOURS] So "derive" is bound and "intertwiner" is not — the row half-lands. **Class:
producer-suppliable object. MATERIAL.**

### 2.9 Tally

```text
CONFIRMED (5 rows, 6 findings): C-B-V010-01, C-B-V010-13 (x2), C-B-V011-MR-05,
                                C-B-V011-MR-07 (FATAL), C-B-V011-SP1-02
REFUTED   (2 rows, 2 findings): C-B-V010-05 (downgraded MINOR), C-B-V011-SP2-05
TEN_FINDINGS = 6 confirmed / 2 refuted
```

---

## 3. N3 — THE CONSOLIDATED V004 SCOPE

### 3.1 The closed repair list — eleven items

| # | Subject | Defect | Exact repair | Sev |
|---|---|---|---|---|
| 1 | `C-B-V009-04` `:434` | distinctness unbound; direction deleted | Add a spec-fixed disjointness receiver, e.g. `r_distinct := EXACT(pairwise_disjoint(D_formal[x],D_principal[x],D_taylor[x]))` **and** `r_one := EXACT(exactly_one_in_domain(r_formal_x.status,r_principal_x.status,r_taylor_x.status))`; conjoin both, and conjoin the three `DOMAIN` `.success` bits | **FATAL** |
| 2 | `C-B-V011-MR-07` `:474` | containment truth unreceived | Pair the reduction: add `r_cmp_f := COMPARE(r_f.result, CONTAINED, empty)` against a **spec-fixed** constant, or replace `SYMBOLIC` with `EXACT`/`KERNEL`; conjoin it | **FATAL** |
| 3 | `C-B-V011-SP1-05` `:486` | ordering atom unbound; `exhaustive` under-notated | Add `r_order := M2(q_selection_before_enum, selection_sources)` with `r_order.hits = empty`; rewrite the criterion to name `r_enum.success` for completeness | **UNBOUND** |
| 4 | `C-B-V010-01` `:449` | `E_factor` direction unforced | Fix the expected classification to the spec-level constant `REJECTED` for every enumerated post-hoc factor, or add a closed schema fixing `E_factor[m].classification` | MATERIAL |
| 5 | `C-B-V010-13` `:461` (a) | custodian independence has no receiver | Add a relational receiver: `r_indep := COMPARE(G_custodian.principal, M_holdout.producer_principal, empty)` **required to differ**, or a `KERNEL` independence proof | MATERIAL |
| 6 | `C-B-V010-13` `:461` (b) | contamination/drift direction unforced | Fix `E_holdout[m]` to the spec-level constant `FAILS` for every enumerated contamination/drift mutation | MATERIAL |
| 7 | `C-B-V011-MR-05` `:472` | distinctness of five evolutions unbound | Add `r_distinct := EXACT(pairwise_distinct({r_e.normal_form}))` and conjoin | MATERIAL |
| 8 | `C-B-V011-SP1-02` `:483` | intertwining direction unforced | Compare each Lorentz square to the **spec-fixed** intertwiner identity rather than to `E_map[g]` | MATERIAL |
| 9 | `C-B-V010-14` | `silently inserted` does not name its receiver | Rewrite the atom as `r_m2.hits = empty` | MINOR |
| 10 | §12.7A `:1427` | `FINAL_INSERTIONS = 248` is false | Set to **261**. Arithmetic: `1392 − 163 + 261 = 1490`, the true V003 length; 248 implies 1477. Cause: counting with `grep '^+[^+]'` drops 13 inserted **blank** lines | MINOR |
| 11 | §3 `:207` | `B-V011-SP2-07` requirement-of-record carries the convicted parse | Restore the blocker's grammar: *"Every **load-bearing audit** must be free of Python `assert`…"* — the modifier belongs on *audit* | MINOR |

*(Optional, not charged: `C-B-V010-05` `:453` — add an enumerated compensator-mutation
grammar so its coverage does not rest on fixture adequacy.)*

### 3.2 The closed verification list for the check of V004

For each row 1–8: (i) the named receiver exists in the **procedure**; (ii) its
`.success` (or comparison) is a **conjunct of the PASS criterion**; (iii) the
expected side is a **spec-fixed constant or schema-fixed value**, not a
producer-declared ledger entry; (iv) the class is unchanged; (v) `diff -U 3` hunk
count and **insertions and deletions** all reconcile against the file's own length.
For 9–11: fixed-string presence/absence, and the arithmetic in item 10 recomputed
from the file rather than from the certificate.

### 3.3 `CLASS_RULE = proposed` — make the class structurally impossible

[YOURS] Eight of the eleven repairs above are the **same defect**. Patching them
instance-by-instance leaves the next re-render free to reintroduce it — which is
precisely what happened between Q-567 and now: SP1-07 was repaired and the class
reappeared in V009-04, MR-05, MR-07, SP1-02, V010-01 and V010-13. The spec should
install law, not patches. I propose two rules for the builder to install in §2.2
beside the existing binding-class rule:

```text
(BR-1) NO PRODUCER-DECLARED OBJECT MAY CARRY A CRITERION'S DIRECTION.

If the truth of a PASS-criterion atom depends on the CONTENT of a producer-supplied
object E -- an expected ledger, status record, or manifest VALUE -- then the row
must also contain an opcode result that forces that content independently of the
producer. Admissible forcers, exhaustively:
  (a) a content-addressed CLOSED SCHEMA that fixes the required VALUES, not merely
      the field shape;
  (b) a KERNEL replay whose conclusion is COMPAREd to E; or
  (c) a SPEC-FIXED constant or constant set that E is COMPAREd against.
A COMPARE between a computed object and a producer-declared expectation is a
SELF-CONSISTENCY check and carries NO directional force by itself.

Rationale of record: hash-pinning prevents SUBSTITUTION, not FABRICATION. The
existing manifest rule at 12.2 forces every indexed manifest to be content-addressed
and P0-verified, which stops post-hoc swapping and does not constrain what was
pinned.

(BR-2) A REDUCTION OPCODE'S .success IS NOT A TRUTH VALUE.

SYMBOLIC(e).success and SPECTRAL(e).success mean the reduction or formation
succeeded, not that e holds. Any criterion atom asserting that a RELATION HOLDS must
either pair the reduction with a COMPARE against a spec-fixed expected value, or use
EXACT (which compares canonical normal forms) or KERNEL (which replays a proof).
A bare SYMBOLIC/SPECTRAL success bit may be conjoined only where the row asserts
nothing about the reduced expression's value.
```

[YOURS] **A mechanical conformance test comes free with each rule**, which is why I
propose them in this form rather than as prose guidance:

- **BR-1**: for every row, every identifier of the form `E_*` or `M_*` appearing in a
  criterion-bearing comparison must also appear in a closed schema, a `KERNEL`
  conclusion comparison, or against a spec-fixed constant. Today **six rows fail
  this test**, and the failing identifiers each occur exactly once in the file —
  which is itself the signature of the defect and makes the test cheap.
- **BR-2**: no row may conjoin `r_x.success` where `r_x := SYMBOLIC(...)` or
  `SPECTRAL(...)` unless a `COMPARE(r_x.…)` also appears. Today **one row fails**
  (`MR-07`); `C-B-V010-01`'s `r_response` passes because it asserts nothing.

I ran both tests to produce §2, so they are known to be executable against the spec
as it stands, not merely well-formed.

---

## 4. N4 — BATTERY

### 4.1 `F_PLDEC`

[PROVABLE] Nothing here consumed a reader output, a desired outcome, a measured
value, or any physical quantity. This is criterion-language auditing, opcode-
definition reading, and line arithmetic. No descriptor was executed. Document line
counts and SHA-256 digests are not physical quantities. `F_PLDEC = CLEAN`.

### 4.2 M-2, four modes, conventions declared

| Mode | Execution | Result |
|---|---|---|
| regex / metacharacter | `grep -F` fixed-string for every identifier (`E_log`, `E_factor`, `E_evolution`, `E_map`, `E_zero_free`, `E_holdout`, `D_formal`, `D_principal`, `D_taylor`) | each confined to its own row |
| line-wrap / whitespace | rows read as whole lines from the byte subject, not by visual span | wrap-independent |
| self-reference / scope | board rows, descriptor rows and §12.7/§12.7A hunk tables distinguished before counting; a hit inside a delta table cannot certify an operative occurrence | `E_holdout`'s two hits both located and classified |
| hyphenation / identifier | `[-_ ]` variants for the scope/coverage family carried from the prior relay | zero |

Declared convention: diffs cited under `-U 3`, the convention the spec itself
declares at `:1425` — **not** the `-U 0` I habitually use. That distinction cost me
a near-miss last relay and is now stated up front.

### 4.3 Pre-seal pin check on **this** artifact

| Claim in this artifact | Where displayed | Verified before sealing |
|---|---|---|
| V009-04's identifiers occur once | §1.2 | fixed-string count over the 1,490-line subject |
| `.success` bits absent from V009-04's PASS | §1.2 | criterion quoted in full from `:434` |
| Exactly two bare-`SYMBOLIC` rows | §2.6 | mechanical sweep of all 66 descriptor rows |
| `COMPARE`/`SYMBOLIC`/`EXACT`/`TYPE`/`DOMAIN` definitions | §2.1, §2.5 | quoted verbatim from `:305-340` |
| V010-05 and SP2-05 byte-identical V002→V003 | §2.2, §2.3 | both rows pulled from both files and compared |
| `1392 − 163 + 261 = 1490` | §3.1 item 10 | recomputed from both files' lengths |
| Final-line counts (6/2; 11+2=13) | §5 | recounted against §2.9 and §3.1 |

Every final-line value is no stronger than the body item it summarizes — the rule
whose breach caused this relay, applied to the artifact that reports it.

### 4.4 Self verb audit

| My verb | Check |
|---|---|
| `WITHDRAWAL = stated` | Stated in the first substantive line, not buried. The mismatch is named as a **headline** failure, not excused by the accurate caveat beneath it. |
| `V009_04 = FATAL_CONFIRMED` | Verified by me at source before this relay was written, with the deleted predicate, the once-occurring identifiers, the absent `.success` bits and a concrete passing input all displayed. |
| `SP1_05 = UNBOUND_CONFIRMED` | **A severity error of my own, self-caught and corrected upward.** I graded it MATERIAL on the adjective and missed that the ordering atom has no receiver at all. I audited a word instead of the row — the exact failure I charge in others. |
| `TEN_FINDINGS = 6/2` | Each verified independently at source. **I refused two**, including one FATAL, and one of the refusals (`SP2-05`) protects a row I had previously praised — so the refusals are not reflexive deference in either direction. |
| `C-B-V010-05` refuted | Refuted on the `EXACT` definition, which compares normal forms — an inserted compensator perturbs them. Downgraded, not dismissed. |
| Agent findings | **Not relayed.** Every confirmation rests on my own reading of the row, the blocker and the opcode table; where I agree with the carried claim I say why in my own display, and where I disagree I refute it. |
| `CLASS_RULE = proposed` | Proposed as **law with a mechanical conformance test**, and both tests were actually run against V003 to produce §2 — so I am not proposing an untested rule. |
| `V004_SCOPE = closed_list` | Closed in both directions: a work list for the builder and a verification list for the checker, so the check of V004 is not another open-ended sweep. |
| Scope | I re-adjudicate no grade of record, open no appeal, and do not touch my sealed check, which stands as the record of what I sealed. |

---

```text
WITHDRAWAL = stated (RE_RENDERS = 28/28 CONFIRMED is withdrawn; corrected value
  22/28 confirmed, 6 defective. The verdict-line/scope mismatch named plainly: my
  sealed §2.4 stated the coverage boundary correctly IN ADVANCE -- mechanical on all
  28, semantic in full on 7 -- and the defects landed exactly inside it. The failure
  was the headline, not the analysis: a caveat in the body does not license an
  over-claim in the line a reader quotes and the register carries. A verdict line
  must be no stronger than the weakest thing it summarizes.)
V009_04 = FATAL_CONFIRMED (blocker demands DISTINCT domains; V002's directional
  predicate "exactly one licensed dispatch occurs at every admitted input" was
  DELETED with no receiver supplied; the sole per-input conjunct is a SYMMETRIC
  COMPARE against the producer-declared E_log[x]; r_formal_x/r_principal_x/
  r_taylor_x .success are ABSENT from PASS; D_formal, D_principal, D_taylor, E_log
  and taylor_norm_bound occur at line 434 and NOWHERE ELSE; a producer setting all
  three domains equal and declaring {IN_DOMAIN,IN_DOMAIN,IN_DOMAIN} PASSES the row
  in the literal pre-fix state. The spec's own audit note at :690 claims only
  completeness and dispatch comparison were bound -- never distinctness -- yet
  :1485 counts the row inside BINDING_SWEEP = 66/66.)
SP1_05 = UNBOUND_CONFIRMED (re-graded UPWARD from my own MATERIAL: "selection occurs
  only after enumeration" is an ORDERING claim and ENUM/TYPE receive completeness
  and typing, not order -- no M2 query, no DAG. I audited the adjective and missed
  the atom.)
TEN_FINDINGS = 6 confirmed / 2 refuted (CONFIRMED: C-B-V010-01 producer-suppliable
  E_factor replacing V002's "every post-hoc factor FAILS"; C-B-V010-13 TWICE --
  custodian independence has no receiver, TYPE validates a graph not a relation,
  and the contamination/drift direction is producer-declared; C-B-V011-MR-05 the
  SAME distinctness gap as V009-04 in another family; C-B-V011-MR-07 FATAL -- the
  blocker's verb "contains" is carried by an UNPAIRED SYMBOLIC whose .success means
  the reduction succeeded, not that containment holds, and a sweep of all 66 rows
  finds EXACTLY TWO bare-SYMBOLIC conjuncts, the other being C-B-V010-01's
  assertion-free r_response, which pairs its real assertion with a COMPARE one line
  away; C-B-V011-SP1-02 "derive" bound by KERNEL but "intertwiner" compared to a
  producer-declared E_map[g].
  REFUTED: C-B-V010-05 -- EXACT compares canonical normal forms, so an inserted
  compensator perturbs them and the receiver exists; downgraded to MINOR fixture
  coverage. C-B-V011-SP2-05 -- criterion is a pure conjunction of eleven success
  bits with both ENUM completeness certificates COMPAREd to the proof indexes with
  empty difference, so the replayed bundle covers exactly the enumerated squares;
  byte-identical to the row I verified as a model repair at Q-567.)
V004_SCOPE = closed_list (+11 repairs with exact edits and +2 rules = 13; each with
  a verification criterion so the check of V004 is a closed list rather than another
  open-ended sweep)
CLASS_RULE = proposed (BR-1: no producer-declared object may carry a criterion's
  direction -- if an atom's truth depends on the CONTENT of a producer-supplied
  object, the row must also force that content by a value-fixing closed schema, a
  KERNEL conclusion comparison, or a spec-fixed constant; a COMPARE against a
  producer-declared expectation is SELF-CONSISTENCY and carries NO direction.
  BR-2: a reduction opcode's .success is not a truth value -- SYMBOLIC/SPECTRAL
  success means the reduction succeeded, not that the relation holds; an atom
  asserting a relation must pair it with COMPARE against a spec-fixed value, or use
  EXACT or KERNEL. Rationale of record: HASH-PINNING PREVENTS SUBSTITUTION, NOT
  FABRICATION -- the existing manifest rule at :340-342 stops post-hoc swapping and
  does not constrain what was pinned. Both rules carry mechanical conformance tests,
  and both were RUN against V003 to produce this artifact: BR-1 fails on six rows,
  BR-2 on one.)
VERB_AUDIT_SELF = CLEAN (+1 self-caught severity error: I had graded SP1-05 MATERIAL
  by auditing its adjective and missing that its ordering atom has no receiver at
  all; corrected upward here. Two carried FATAL claims REFUSED, including one on a
  row I had previously praised, so the verifications are not deference in either
  direction; nothing is relayed that I did not read at source.)
```

Eight of the eleven repairs are one defect wearing eight faces. The spec already
forbids the adjectives that used to carry criteria unaided, and that repair held —
no re-rendered row smuggles a word back in. What replaced the adjective was a
*shape*: compute a thing, compare it to what the producer said the thing would be,
and call the agreement a check. It reads as rigor and is a mirror. The eight
instances should be repaired, but the reason to install BR-1 and BR-2 as law is
that this class has already survived one repair cycle by moving rooms, and a rule
that can be run over the file is the only thing that will notice when it moves again.
