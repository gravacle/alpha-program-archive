# STAGE 8 / TASK 6 / SUBGATE — THE BR-1 ADJUDICATION: CORRECTION + THE SIXTEEN CANDIDATES — DARIO V001

Lane: Dario (Claude Opus 5), cross-family custody reviewer and author of BR-1/BR-2
Task: PASTE 642 / Task 6 subgate — correction of record, the row-by-row adjudication,
and the ruling on BR-1's conformance regime
Authority: DoR-020-A8. **THIS ARTIFACT AUTHORIZES NOTHING AND LIFTS NO GATE.**
Corrects: `STAGE8_TASK6_SPEC_V004_CHECK_DARIO_V001.md` =
`502e3b3b14bb0d55c42efef7e0c950d15af25171a1036e12a22e98d5ac52ba67`, which **stands
sealed and is not overwritten.**

```text
REGISTER_HEAD = Q-578
WITHDRAWAL = stated
ADJUDICATION = 16/16 (+10 defective / 6 lawful)
NEW_CLOSED_LIST = 10
BR1_REGIME = adjudicated (+text at §3.2)
VERB_AUDIT_SELF = CLEAN (+1 systematic detector bias, recorded at §4.4)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**I am ruling against my own claim.** I told the program that BR-1 "carries a
mechanical conformance test" and that I had run it. That was wrong, and the
adjudication below is the demonstration: deciding whether a row is lawful required
knowing **which clause of the blocker each receiver serves**, and no pattern match
can do that. BR-1 is sound law and an **adjudicated** check. The mechanical part
survives only as a candidate generator — useful for bounding the work, fatal if
mistaken for the verdict.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-578 | verified |
| My sealed check = `502e3b3b14bb0d55c42efef7e0c950d15af25171a1036e12a22e98d5ac52ba67` | verified — stands sealed |
| Spec = `2c767bfc953c7efeeaf4a33542974b10e0a674a161a5f1a651f3486ac36fad8b` | **verified before reading** |
| Census source = `c09f2c246c48ddfd0df127da26a22f08ba9ffd44f5c2118c178a0a5eba5d00e8` | verified |
| Output name collision | none — clear to write |

Declared conventions: rows cited by line number in the fixed spec; blocker demands
quoted from the spec's §1.3 requirement-of-record table, which I verified against the
sealed ledger for the rows where the demand decides the verdict.

---

## 1. J1 — CORRECTION OF RECORD

### 1.1 `BR_SWEEPS_RERUN = +5` — **withdrawn as an undercount**

[PROVABLE] My sealed check reported five BR-1 failures. The number is withdrawn.
The true count under adjudication is **ten** (§2). The verdict direction is
unchanged and strengthened; only the count was wrong.

### 1.2 The detector bias, displayed

[PROVABLE] My BR-1 implementation credited a forcer **per row**: if a row contained
any `COMPARE(r_x.conclusion, …)` anywhere, I treated every producer object in that
row as forced. BR-1 requires the forcer in the **same slice** — that is, forcing
**the field the atom actually consumes.** The two rows this concealed:

```text
C-B-V009-13 (:528)
  atom     r_cmp_m := COMPARE(r_m.normal_form, E_holdout[m], empty)
  my test  saw  COMPARE(r_select.conclusion, E_holdout.selection, empty)  -> "forced"
  truth    that forces E_holdout.SELECTION, a DIFFERENT FIELD of the same ledger;
           SCHEMA(S_registry, M_registry) validates the MANIFEST, not the ledger.
           E_holdout[m] is unforced.

C-B-V011-MR-02 (:554)
  atom     r_cmp_s := COMPARE(r_s.normal_form, E_stats[s], empty)
  my test  saw  COMPARE(r_selector.conclusion, M_stats_status, empty)  -> "forced"
  truth    that forces M_stats_status, a DIFFERENT OBJECT ENTIRELY.
           E_stats[s] is unforced.
```

[YOURS] Both were verified by me at source before this artifact was written. The
bias was **systematic, not incidental** — it would mis-clear any row whose ledger
carries one proof-forced field beside unforced ones, which is a common shape here.

### 1.3 And the opposite error, which I did not commit but nearly did

[PROVABLE] Re-running per-**field** yields **sixteen** candidates. Reporting sixteen
would have been the mirror-image over-claim: `C-B-V011-MR-05` appears in that list,
yet MR-05 is correctly repaired — its per-item `E_evolution[e]` comparison is indeed
unforced, but the blocker's demand is that the five evolutions be **distinct**, and
`EXACT(pairwise_distinct(…))` forces exactly that.

[YOURS] So I have now written two BR-1 implementations that are wrong in opposite
directions. That is not two mistakes; it is one finding about the law, and §3 rules
on it.

---

## 2. J2 — THE ADJUDICATION, ALL SIXTEEN

**The standard, restated:** a row is **DEFECTIVE** iff the blocker's *directional
demand* lacks a receiver. It is **LAWFUL** if that demand is received, even where a
subsidiary ledger field is unforced. Producer-declared bookkeeping beside a forced
demand is a weakness to note, not a defect to charge.

### 2.1 The six LAWFUL

| Row | Blocker's demand | The receiver that carries it | Note |
|---|---|---|---|
| `C-B-V008-08` | *"Restrict the flux lift to `im(d_1)`."* | `r_exact_im:=EXACT(F_phys=im(d1))` **and** `r_domain:=DOMAIN(Q_flux,im(d1))`; both KERNEL conclusions compared to `E_flux` fields (BR-1(b)) | the outside-fixture rejection field is unforced — a supporting control, not the demand |
| `C-B-V011-MR-04` | *"Detect overlap interactions invisible on vacuum and one-record sectors."* | `r_low:=EXACT(B_λ0\|_(vac+one)=B_λ1\|_(vac+one))` **and** `r_high:=KERNEL(p_high_distinct)` **with spec-stated goal** `B_λ0\|_higher != B_λ1\|_higher` | the flagged `M_unique.claim_spans` is uniqueness-claim bookkeeping; the row also discloses that its last conjunction is vacuously true on the empty claim set |
| `C-B-V011-MR-05` | *"Resolve continuous-sum, ordered, sequential, Trotter, and circuit evolutions."* | `r_distinct:=EXACT(pairwise_distinct({r_e.normal_form : e in r_enum.items}))`, conjoined | **the archetype**: unforced per-item field, forced demand |
| `C-B-V011-SP1-08` | *"Derive a complete physical two-point function before assigning mass meaning."* | `r_proof_cmp:=COMPARE(r_proof.conclusion,E_2pt.two_point,empty)` for the derivation; `r_mass:=DAG(G_mass,P_mass)` for the ordering | `E_2pt.classification` is a subsidiary cross-check |
| `C-B-V011-SP2-04` | *"…solve the complete projection-module control family **uniquely as `PBP`**."* | `r_unique:=COMPARE(E_control.solution_ids,{PBP},empty)` — a **spec-fixed literal**, BR-1(c) | my sealed refutation of this row stands |
| `C-B-V011-SP2-06` | *"Derive Lorentzian pole/threshold status, sign, …"* | `r_kernel_sign:=KERNEL(p_reality_sign_class,…)` — an exact-goal bundle for reality/sign/**classification** — with `r_compare_sign` comparing its conclusion to `E_SP08` (BR-1(b)) | `r_compare_class` against `E_SP08.classification` is a redundant cross-check of the SPECTRAL output, not the carrier of the demand |

### 2.2 The ten DEFECTIVE

| # | Row | Blocker's demand | Why the demand is unreceived |
|---|---|---|---|
| 1 | `C-B-V008-09` | *"Make physical-interval and Maxwell-completion obligations executable **without later choices**."* | Per-branch outcomes rest on `COMPARE(r_schema_b.normalized, E_branch[b], empty)`. `SCHEMA(S_branch,b)` validates the **enumerated item**, not the ledger's values; no KERNEL; no spec constant. A producer declaring the favourable outcome per branch **is** the "later choice" the blocker forbids. |
| 2 | `C-B-V008-11` | *"…require a genuinely **forward** external holdout."* | Contamination transitions rest on `COMPARE(r_m.normal_form, E_contam[m], empty)`. The row **has** `r_protocol:=KERNEL(p_holdout,…)`, but its conclusion is never compared to `E_contam` — a proof present and not doing this work. |
| 3 | `C-B-V009-02` | *"**Remove** the undefined common positive dimensionful-scale equivalence."* | `COMPARE(r_units_e.classification, E_equiv[e], empty)` with **no KERNEL anywhere in the row**. The rejection exists only as prose in the inputs column. Declaring the dimensionful-scale equivalence `ALLOWED` passes every conjunct. **The cleanest instance in the set.** |
| 4 | `C-B-V009-07` | *"**Freeze** the response complex, background connection, root preparation, and finite-to-continuum sequence."* | `r_frozen:=COMPARE(M_config,E_config,empty)` compares the manifest to a producer-declared *"frozen expected manifest"* — the freeze certifies itself. Mutation rejections rest on `E_config_mut[m]`, also producer-declared. |
| 5 | `C-B-V009-10` | *"Supply a **deterministic** local-Maxwell reconstruction from the global response."* | `r_null:=EXACT(reconstruct(T_top)=0)` is genuinely spec-fixed and receives the topological-null control — but the per-basis and per-parity reconstruction outcomes rest on `E_reconstruct[u]`/`[p]`. **Narrow**: one real receiver present, the determinism of the reconstruction itself unforced. |
| 6 | `C-B-V009-13` | *"…**fail-closed** under contamination."* | `COMPARE(r_m.normal_form, E_holdout[m], empty)`. The KERNEL forces `E_holdout.selection`; the fail-closed direction is a different field and unforced. **Byte-identical in shape to my closed-list item 6, which V004 repaired at `V010-13` with spec-fixed `FAILS`.** |
| 7 | `C-B-V011-MR-02` | *"**Resolve or carry** the bosonic/fermionic/hard-core/distinguishable statistics family."* | `COMPARE(r_s.normal_form, E_stats[s], empty)`; the KERNEL forces `M_stats_status`, a different object. `r_query:=M2(...)` with `hits=empty` guards silent selection — a real guard, but not the resolution demand. |
| 8 | `C-B-V011-MR-09` | *"Derive charged access for the full star or a complete composite-handle operator; **one handle is insufficient**."* | The access half **is** forced — `KERNEL(p_full_star_access)` carries the canonical disjunctive goal and its conclusion is compared to `E_star`. But *"one handle is insufficient"* is a **separate explicit clause**, and it rests on `COMPARE(r_one.normal_form, E_star.one_handle_insufficient, empty)` — producer-declared. |
| 9 | `C-B-V011-SP2-03` | *"…and account for … a **nonzero-index control**."* | Most clauses are exemplary — `r_kernel_pair` carries a spec-stated exact goal, and `r_compare_pair` compares SPECTRAL to a **KERNEL conclusion** rather than to a ledger, which is the right pattern. But the index-one control rests on `COMPARE(r_spectral.control, E_SP04.expected_index_one_control, empty)`; a producer declaring a zero-index control as expected passes. **Narrow.** |
| 10 | `C-D-A35-03-PHYSICAL-RESIDUE` | the board's own charge: *"`derived`, positivity, covariance, branch completeness, and **finite-`z` exclusion** were unbound"* | Positivity/covariance **are** now bound by `r_proof_cmp:=COMPARE(r_proof.conclusion,E_residue.positivity_covariance,empty)`. The finite-`z` exclusion is not: `r_z:=COMPARE(M_residue.finite_cell_z,E_residue.z_not_sufficient,empty)` is producer-declared on both sides of the intent. **Narrow.** |

```text
ADJUDICATION = 16/16
DEFECTIVE = 10  (V008-09, V008-11, V009-02, V009-07, V009-10, V009-13,
                 MR-02, MR-09, SP2-03, A35-03-PHYSICAL-RESIDUE)
LAWFUL    =  6  (V008-08, MR-04, MR-05, SP1-08, SP2-04, SP2-06)
```

[YOURS] Four of the ten are **narrow** — V009-10, MR-09, SP2-03, A35-03 each carry a
real receiver for part of their blocker and fail on one clause. I grade them
defective anyway, because a blocker clause is a demand and not a preference; but the
repair for each is one comparison, and the record should not read as though these
rows are in the state V009-02 is in.

### 2.3 The new closed list — ten repairs

| # | Row | Exact repair | Verification criterion |
|---|---|---|---|
| 1 | `C-B-V008-09` | fix each branch outcome to a spec-fixed token set (`ADMITTED`/`REJECTED`) compared per branch, or add a `KERNEL` per branch whose conclusion is compared to `E_branch[b]` | the expected side of the per-branch `COMPARE` is a spec constant or a `KERNEL` conclusion |
| 2 | `C-B-V008-11` | compare `r_m.normal_form` to spec-fixed `FAILS`, **or** compare `r_protocol.conclusion` to `E_contam` | `E_contam[m]` no longer appears as a bare expected side |
| 3 | `C-B-V009-02` | compare `r_units_e.classification` to a spec-fixed `{ALLOWED, REJECTED_DIMENSIONFUL}` token, with the dimensionful case required present in the enumeration | the rejection is an opcode-received value, not inputs-column prose |
| 4 | `C-B-V009-07` | make `E_config` a **spec-pinned** frozen manifest digest (not a producer field), and fix mutation outcomes to `REJECTED` | `r_frozen`'s expected side is content-addressed to a spec pin; `r_cmp_m` targets a spec constant |
| 5 | `C-B-V009-10` | add `r_det := KERNEL(p_deterministic_reconstruction)` with its conclusion compared to `E_reconstruct`, or fix per-basis outcomes to spec tokens | determinism has a proof receiver; `r_null` retained |
| 6 | `C-B-V009-13` | compare `r_m.normal_form` to spec-fixed `FAILS` — the identical repair V004 already applied at `C-B-V010-13` | `E_holdout[m]` no longer a bare expected side |
| 7 | `C-B-V011-MR-02` | add `r_resolve := EXACT(pairwise_distinct({r_s.normal_form}))` if the demand is *resolve*, or a `KERNEL` carry-proof if the demand is *carry*; the row must declare which | the chosen arm is spec-forced and the declaration is a closed record |
| 8 | `C-B-V011-MR-09` | compare `r_one.normal_form` to spec-fixed `INSUFFICIENT`, or add a `KERNEL` goal `one_handle_action != full_star_action` | the insufficiency clause has its own receiver |
| 9 | `C-B-V011-SP2-03` | compare `r_spectral.control` to a spec-fixed `INDEX_ONE` token, or add a `KERNEL` with an exact nonzero-index goal | the control's index is spec-forced |
| 10 | `C-D-A35-03-PHYSICAL-RESIDUE` | compare `M_residue.finite_cell_z` to a spec-fixed `Z_NOT_SUFFICIENT` token, or carry the exclusion in `p_residue`'s goal | the finite-`z` exclusion is opcode-received |

[YOURS] Every repair is one comparison or one proof goal. **The spec already contains
the pattern for all ten** — V004's own `REJECTED`, `FAILS`, `CONTAINED`,
`INTERTWINER_IDENTITY` repairs are exactly this move. Nothing here needs invention.

---

## 3. J3 — THE BR-1 CONFORMANCE REGIME, RULED

### 3.1 The ruling: **ADJUDICATED**, not mechanical

[YOURS] I choose the option that is **true**, not the one that is stronger. BR-1
conformance is an **adjudicated check**: a per-row reading performed and displayed by
a reviewer. It is not, and cannot be made, a swept pattern.

The demonstration is §2 itself, on the two rows my implementations disagreed about:

```text
C-B-V011-MR-05   per-row test  -> LAWFUL   (a KERNEL exists in the row)
                 per-field test -> DEFECTIVE (E_evolution[e] unforced)
                 ADJUDICATION   -> LAWFUL, because the blocker's demand is
                                   "resolve", and pairwise_distinct receives it.

C-B-V011-MR-09   per-row test  -> LAWFUL   (a KERNEL conclusion is compared to E_star)
                 per-field test -> DEFECTIVE (E_star.one_handle_insufficient unforced)
                 ADJUDICATION   -> DEFECTIVE, because "one handle is insufficient"
                                   is a SEPARATE CLAUSE of the blocker and the
                                   forced KERNEL serves the OTHER clause.
```

Both rows have a KERNEL, a conclusion comparison, and one unforced ledger field.
**They are syntactically indistinguishable and adjudicate oppositely.** The
difference lies entirely in the blocker's clause structure — whether the unforced
field carries a demand of its own. No slice definition over the spec's bytes can
see that, because the deciding fact is not in the spec: **it is in the blocker.**

### 3.2 The text for V005 to install as the law's own

```text
(BR-1/A) BR-1 CONFORMANCE IS ADJUDICATED, NOT SWEPT.

A BR-1 verdict is a per-row reading, performed by a reviewer and DISPLAYED. It has
three ordered steps, all of which must appear in the artifact that claims the verdict:

  1. CANDIDATE GENERATION (mechanical, over-generating).
     Emit every PASS-criterion atom whose expected side is a field of a producer
     supplied E_*/M_* object, EXCLUDING (i) pure ID-set comparisons paired with a
     proof-index or enumeration comparison, and (ii) comparisons whose expected side
     is a spec-fixed constant. The generator MUST over-generate: a candidate is not
     a finding, and a zero-candidate row still requires step 3's one-line note.

  2. CLAUSE DECOMPOSITION (from the SEALED BLOCKER, not from the spec).
     Split the blocker at its span into its separate directional demands. A clause
     joined by "and", or introduced by a semicolon, is a separate demand.

  3. ADJUDICATION (per candidate).
     For each candidate, name which blocker clause its field carries.
       - If that clause is received elsewhere in the row by a spec-fixed constant,
         a KERNEL conclusion comparison, or a value-fixing closed schema, the
         candidate is LAWFUL and the receiver MUST BE NAMED.
       - If the field carries a clause with no other receiver, the row is DEFECTIVE.
     A candidate dismissed without naming its receiver is not adjudicated.

A BR-1 report states: candidates generated, clauses decomposed, and a verdict with a
named receiver for every candidate. A report of "zero failures" without those three
displays is NOT a BR-1 result and may not be registered as one.

(BR-2 is unaffected: it IS mechanical, and two independent implementations agreed
at zero. The distinction is that BR-2 asks a question about the SPEC's own syntax --
is this success bit paired -- while BR-1 asks a question whose answer lives in the
BLOCKER.)
```

[YOURS] This also states the **SWEEP COVERAGE RULE** in its proper place: the defect
in V004's transcript was not the arithmetic but the missing display. It listed six
repaired slices and emitted `failures = []` for sixty-six rows. Under (BR-1/A) that
report is inadmissible on its face, without anyone needing to re-derive it.

---

## 4. J4 — BATTERY

### 4.1 `F_PLDEC`

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value, or
any physical quantity. This is criterion-language adjudication against sealed blocker
text. No descriptor was executed. `F_PLDEC = CLEAN`.

### 4.2 M-2

Fixed-string extraction of all 66 descriptor rows and all `E_*`/`M_*` identifiers;
rows parsed one logical row per stable ID (wrap-independent); the transcript and
repair tables **excluded** when testing whether a row's own procedure contains a
receiver; hyphen/underscore variants checked on the spec-fixed token names. Bounded
negatives are scoped to the fixed spec byte subject.

### 4.3 Pre-seal pin check

| Claim | Verified before sealing |
|---|---|
| 16 candidates, 10 defective / 6 lawful | recounted against §2.1 + §2.2; 6 + 10 = 16 |
| V009-13 and MR-02 forcers target other fields | both rows read at source and the target fields displayed |
| MR-05 vs MR-09 adjudicate oppositely | both rows read; both contain a KERNEL, a conclusion comparison, and one unforced field |
| SP2-04's `{PBP}` forcer | re-read; the sealed refutation stands |
| new closed list = 10 items | one per defective row, counted |
| every repair uses a pattern already in V004 | `REJECTED`/`FAILS`/`CONTAINED`/`INTERTWINER_IDENTITY` all present in the spec |

### 4.4 Coverage, stated exactly, and the self verb audit

[YOURS] **Coverage:** I adjudicated the sixteen rows the per-field generator emitted,
each against its blocker's demand. I did **not** re-adjudicate the fifty carried rows
the generator did not flag, and I do not claim they are BR-1 clean — I claim only
that the generator, which over-generates by construction within BR-1's scope, did not
flag them. That is weaker than a clean bill and is the strongest thing I can say.

| My verb | Check |
|---|---|
| `WITHDRAWAL = stated` | The undercount is withdrawn in the first substantive line, with the bias displayed as **systematic**, not incidental. |
| `ADJUDICATION = 16/16` | Every row read at source against its blocker; both verdicts carry a named receiver or a named absence. |
| `10 defective / 6 lawful` | I refused six, including four rows the mechanical test condemned. Four of the ten are graded **narrow** so the record does not flatten them into V009-02's condition. |
| `BR1_REGIME = adjudicated` | **Ruled against my own prior claim.** I said BR-1 carried a mechanical test and that I had run it; that was false, and MR-05 vs MR-09 is the proof — syntactically identical, oppositely adjudicated. |
| **The bias, owned** | My per-row credit was not a slip: it would mis-clear any row whose ledger has one proof-forced field beside unforced ones. I found it only because another reading caught two rows I had cleared. |
| Not over-correcting | I did **not** report the sixteen. The mirror-image over-claim was available and refused, and MR-05 is displayed as the reason. |
| Scope | No grade, appeal, ruling or freeze text is touched; my sealed check stands as the record of what I sealed. |

---

```text
WITHDRAWAL = stated (the sealed BR_SWEEPS_RERUN = +5 is withdrawn as an UNDERCOUNT;
  true count under adjudication is TEN. The bias was systematic: my implementation
  credited a forcer PER ROW, while BR-1 requires it in the SAME SLICE -- forcing the
  FIELD the atom consumes. C-B-V009-13's KERNEL forces E_holdout.SELECTION while the
  fail-closed atom consumes E_holdout[m]; C-B-V011-MR-02's forces M_stats_status, a
  different object entirely. Both verified by me at source.)
ADJUDICATION = 16/16 (+10 DEFECTIVE: C-B-V008-09 branch outcomes producer-declared,
  which IS the "later choice" the blocker forbids; C-B-V008-11 contamination
  transitions unforced though the row HAS a KERNEL doing other work; C-B-V009-02 the
  cleanest -- no KERNEL anywhere and the dimensionful-scale rejection surviving only
  as inputs-column PROSE; C-B-V009-07 a freeze that certifies itself against a
  producer-declared "frozen expected manifest"; C-B-V009-10 (narrow) determinism
  unforced though r_null is genuinely spec-fixed; C-B-V009-13 the fail-closed
  direction, byte-identical in shape to the item V004 already repaired at V010-13;
  C-B-V011-MR-02 resolution unforced; C-B-V011-MR-09 (narrow) the explicit clause
  "one handle is insufficient" producer-declared while the access clause IS forced;
  C-B-V011-SP2-03 (narrow) the nonzero-index control; C-D-A35-03 (narrow) the
  finite-z exclusion, positivity and covariance having been genuinely bound.
  +6 LAWFUL: C-B-V008-08, C-B-V011-MR-04, C-B-V011-MR-05, C-B-V011-SP1-08,
  C-B-V011-SP2-04, C-B-V011-SP2-06 -- each with an unforced subsidiary field beside
  a demand that IS received, and the receiver named.)
NEW_CLOSED_LIST = 10 (one repair per defective row, each a single comparison or proof
  goal, and EVERY ONE uses a pattern already present in V004 -- the spec's own
  REJECTED / FAILS / CONTAINED / INTERTWINER_IDENTITY constants. Verification
  criterion stated per item so the check of V005 is closed.)
BR1_REGIME = adjudicated (+(BR-1/A) text at §3.2 for V005 to install as the law's own:
  candidate generation is mechanical and MUST over-generate; clause decomposition
  comes from the SEALED BLOCKER, not the spec; adjudication names, per candidate,
  which blocker clause the field carries and which receiver serves it. A "zero
  failures" report without candidates, clauses and named receivers is NOT a BR-1
  result and may not be registered as one. The proof that no slice definition can
  replace this: C-B-V011-MR-05 and C-B-V011-MR-09 are SYNTACTICALLY
  INDISTINGUISHABLE -- each has a KERNEL, a conclusion comparison, and one unforced
  ledger field -- and they adjudicate OPPOSITELY, because the deciding fact is not in
  the spec at all. It is in the blocker's clause structure. BR-2 is unaffected and
  remains genuinely mechanical.)
VERB_AUDIT_SELF = CLEAN (+1 systematic detector bias, owned rather than minimised: my
  per-row forcer credit would mis-clear any row whose ledger carries one proof-forced
  field beside unforced ones, and I found it only because another reading caught two
  rows I had cleared. I also refused the mirror-image over-claim -- the sixteen
  candidates are NOT sixteen findings, and MR-05 is displayed as the reason.)
```

I told the program that BR-1 came with a runnable test, and that was the part of my
own law I had not tested. The law is right: a producer's expectation cannot supply a
direction, and ten rows still violate it. What was wrong is the idea that a machine
could tell you so. The deciding fact — whether an unforced field carries a demand of
its own — lives in the blocker, not in the spec, and MR-05 and MR-09 differ in
nothing a parser can see. A generator can bound the work and a reviewer must do it,
which is slower than a sweep and is the only version of this check that has ever
returned a true answer.
