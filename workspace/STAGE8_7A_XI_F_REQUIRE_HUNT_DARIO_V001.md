# STAGE 8 / 7A / STEP 8 — THE xi/F REQUIRE-HUNT

**Lane:** Dario (Opus 5, cross-family from the Codex build lanes)
**Date:** 2026-08-08
**Scope:** PASTE 733 only — RR1 enumerate, RR2 matrix, RR3 lambda, RR4 verdict
**Custody:** archive-side read and write; the registrar owns any mirror
**Governing:** 731 `5003d917…`; VOID condition; the C_ref smooth-coframe clause remains
**BARRED as a source**
**Charge:** re-derive, not trust. Nothing adopted under any verdict.

## Lead determination

```text
VERDICT = FORCED (Branch F).

  Sealed requires DO force the branch.  My draft verdict was UNDERDETERMINED and
  it was wrong, for a reason I must state before the result: my probe searched
  phrases the corpus never uses.  "refinement invariant" and "invariant under
  refinement" return zero because the corpus writes "invariant under EACH
  ELEMENTARY refinement", "refinement naturality", "a sealed class of regular-CW
  refinements".  A negative existential off an exact-phrase grep, again.

THE FORCING CHAIN, each link verified by me from bytes:

  L1  The ruled subject IS sum F^2, identically.  contribution / V_cell
      = sum_(mu<nu) [xi_(mu nu)/(ell_mu ell_nu)]^2 = sum F^2 -- checked exactly.
  L2  V011 REQUIRES that subject "invariant under each elementary refinement up
      to a boundary term whose ratio to four-volume tends to zero."
  L3  Branch xi's residual is BULK, not boundary: for bisection with shares
      s, 1-s the residual is V*F^2*(2s-1)^2, so residual/four-volume = F^2(2s-1)^2
      -- a CONSTANT, independent of V, unchanged under iteration.  It never tends
      to zero.  Only s = 1/2 survives, which IS Branch F's rule.
  L4  Independent lock: V011 -- "any residual shape-dependent scalar fails A27."
      Branch xi's surviving share factor is exactly such a scalar.
  L5  Second independent lock, ALREADY EXECUTED, and it is a sealed STAGE7 packet
      member bound to row A27 itself (lineage D038, e60aec3c…):
      "a subregion promoted to an elementary cell must be evaluated by that
      child's intrinsic cell measure.  It may not retain a weighting profile
      defined by an arbitrarily chosen parent."
      Branch xi is literally that retention; Branch F is literally the child's
      own ell'_mu ell'_nu.

LAMBDA_CONVERGENCE = DISTINCT-RHYMING -- and now demonstrably so: the refinement
  selector CLOSES here, the (D2-4) rescaling selector does not.  Same candidate
  pair, different group acting, and now different status.

NOTHING IS ADOPTED.  A forced branch is a derivation, not an adoption; but the
  ruling that books it is the principal's, and §4.3 states what still is not
  discharged.
```

---

## 0. Preflight

[PROVABLE] `relay_outbox/733_ACK.md` was written **before** source work. Lane guard:
the header names **DARIO**. Read only after its sidecar verified:

```text
relay_inbox/RELAY_PASTE_733_XI_F_REQUIRE_HUNT_DARIO_V001.md
  32294de8b84d60d9100cb4fdf8da0a6517358a45de54790cc1f091903b11ce46   shasum -c OK
```

[PROVABLE] `STAGE8_7A_XI_F_REQUIRE_HUNT_DARIO_V001.md` and its seal sidecar were probed
before the write and returned ABSENT.

### 0.1 The glob, stated — per my own 731 standing law

```text
GLOB: os.walk over "workspace" and "supervision", every subdirectory, files
      matching *.md, WRITER-EXCLUDED (no *_DARIO_V001.md).   1951 files.
```

[YOURS] Stating the glob is necessary and, this relay proves, **not sufficient**. The
glob was right. The *probes* were wrong — §2.5.

### 0.2 Sources verified before use

```text
V011  review_packets/.../BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md   aa7c6d49…
D007  BID_CONSOLIDATED_HOSTILE_AUDIT_MATRIX_V005.md                      78f6bb08…
R33R  R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_RESULT_V001.md              e60aec3c…
      (= lineage D038, a sealed STAGE7 packet member BOUND TO ROW A27)
R33S  R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_SPEC_V001.md                d9262ea2…  sealed
LED3  STAGE8_TASK6_LP_MATRIX_LEDGER_LANE3_V001.md                        bc6c3e49…
SUBJ  supervision/DECISION_REFINEMENT_LIMIT_SUBJECT_2026-08-08.md        112e6acb…
JREF  STAGE8_TASK5_JREF_AND_LOCAL_KERNEL_ESTIMATES_LANE2_V001.md         8dd59b35…
731   STAGE8_7A_FUNCTORIALITY_CHARACTERIZATION_DARIO_V001.md             5003d917…  (mine)
```

### 0.3 Gates

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

No common cell formed, no junction map evaluated, no member bound, **no physical
quantity evaluated numerically**, no measured constant. The arithmetic in §2 is exact
rational identity-checking on the displayed formula with dimensionless placeholders.
Nothing adopted. No register, plan, tracker, git action.

---

## 1. RR1 — THE REQUIRES, MODALITY-TAGGED

| # | Require | Source + span | Modality |
|---|---|---|---|
| **R1** | `F_phys = im(d_1)`; `Q_flux` the unique horizontal minimum-norm lift | `aa7c6d49…[44801,44955)` | REQUIRE (membership) |
| **R2** | A26: representative-independent lift; *"individual unit faces outside that image are not assigned a lift; surviving zero-flux additions fail"* | `78f6bb08…[11181,11366)` | REQUIRE + falsifier |
| **R3** | The min-norm determinacy proof: *"Every nonzero zero-flux addition raises the norm, proving uniqueness and representative independence"* | `bc6c3e49…[36444,36745)` | DERIVED mechanism |
| **R4** | `(d_0 lambda)_e = lambda_t − lambda_s`; `(d_1 a)_f = sum incidence(f,e) a_e`; `d_1 d_0 = 0` | `aa7c6d49…[44595,44690)` | REQUIRE (structural/gauge) |
| **R5** | The measure and the cell contribution: `V_cell sum F^2`, `xi = ell_mu ell_nu F + h.o.t.` | `aa7c6d49…[45718,46068)` | REQUIRE (definitional) |
| **R6** | **The invariance demand**: *"the intensive quadratic coefficient must be invariant under each elementary refinement up to a boundary term whose ratio to four-volume tends to zero"* | `aa7c6d49…[47025,47247)` | **REQUIRE ×2 ("must")** |
| **R7** | *"The inverse weight … an inserted compensator, or any residual shape-dependent scalar fails A27."* | `aa7c6d49…[46589,46710)` | **REQUIRE (bar)** |
| **R8** | The subject ruling: the limit's subject is the intensive quadratic coefficient | `112e6acb…[323,669)` | REQUIRE (principal) |
| **R9** | **The executed intrinsic-cell binding**: *"a subregion promoted to an elementary cell must be evaluated by that child's intrinsic cell measure. It may not retain a weighting profile defined by an arbitrarily chosen parent."* verdict `INHERITED_REFINEMENT_NATURALITY_FORCES_UNIFORM_MEASURE` | `e60aec3c…[551,740)`, `[69,123)` | **REQUIRE, already executed** |
| **A1** | (D2-4): *"Neither DoR-007 nor DoR-008 chooses `lambda` or supplies a scale law."* | `8dd59b35…[12383,12879)` | ALLOW / absence |

```text
REQUIRES = 9 enumerated (R1-R9) + 1 ALLOW.  R6, R7 and R9 are the eliminating three.
```

---

## 2. RR2 — THE MATRIX

`S` satisfies · `V` violates · `U` undetermined · `–` neutral

| | R1 | R2 | R3 | R4 | R5 | **R6 invariance** | **R7 shape-scalar bar** | R8 | **R9 intrinsic binding** |
|---|---|---|---|---|---|---|---|---|---|
| **Branch F** | S (with the side condition at §2.4) | S | – | S | S | **S, exactly** | **S** | S | **S** |
| **Branch xi** | S natively | S | – | S | S | **V** | **V** | U | **V** |

### 2.1 L1 — the ruled subject is literally `sum F^2`

[PROVABLE] From `R5` and `R8`. My own exact check, three generic placeholder triples:
`<xi,xi>`-term `= V/(ell_mu² ell_nu²)·xi²` with `xi = ell_mu ell_nu F` equals `V·F²` in
every case, and **contribution / V_cell = F²** exactly.

[PART-PROVABLE] So `R6`'s subject — *the intensive quadratic coefficient* — **is** `sum
F²`. A require that it be invariant under each elementary refinement is, term for term,
a require that `F` be the object refinement holds fixed.

### 2.2 L3 — Branch xi violates R6, and the residual is BULK

[PROVABLE] Take `C_ref`'s own named generator, cubical bisection: two sub-cells,
`A_i = A/2`, `V_i = V/2`, Branch-xi shares `s` and `1−s`. My exact check across generic
placeholders:

```text
refined total  = (V/2)(2sF)^2 + (V/2)(2(1-s)F)^2
parent         = V F^2
residual       = V F^2 (2s-1)^2                <- verified exactly, all cases
residual / four-volume = F^2 (2s-1)^2          <- INDEPENDENT OF V
```

[PROVABLE] The ratio is a **constant**. It does not tend to zero, and it is unchanged
under iteration — it is a **bulk** term, not *"a boundary term whose ratio to
four-volume tends to zero"*. **R6's tolerance does not admit it.** Only `s = 1/2`
gives residual zero, and `s = 1/2` is exactly `xi' = ell'_mu ell'_nu F` — Branch F.

[YOURS] This is an elimination certificate, not a preference: the require's own
tolerance clause is what kills the branch.

### 2.3 L4, L5 — two independent locks

[PROVABLE] **R7**, `aa7c6d49…[46589,46710)`: *"The inverse weight `ell_mu^2
ell_nu^2/V_cell`, an inserted compensator, or **any residual shape-dependent scalar**
fails A27."* Branch xi's surviving factor is a per-sub-cell scalar depending on the
sub-cell's share — a residual shape-dependent scalar by construction.

[PROVABLE] **R9**, `e60aec3c…[551,740)`, and this is the strongest of the three because
it is **already executed** and is a sealed STAGE7 packet member bound to row A27
(lineage `D038`):

```text
Therefore a subregion promoted to an elementary cell must be evaluated by
that child's intrinsic cell measure. It may not retain a weighting profile
defined by an arbitrarily chosen parent.
```

verdict `INHERITED_REFINEMENT_NATURALITY_FORCES_UNIFORM_MEASURE`, with
`intrinsic_per_cell_response_binding = true`.

[YOURS] Branch xi **is** retention of a parent-defined weighting profile with free
shares. Branch F **is** evaluation by the child's own `ell'_mu ell'_nu` and `V'_cell`.
The require does not merely disfavour one; it names the other's mechanism as its own
conclusion, and it has already been used to kill a nonuniform measure family.

### 2.4 The relay's three flagged questions, answered

**Does Branch F's per-face primitivity conflict with the no-lift-outside-`F_phys`
exclusion?** [PART-PROVABLE] **No — but it carries a side condition, and I state it.**
If `F` were a *free* per-face primitive, `xi = ell·ell·F` would generically leave
`im(d_1)`, which `R2` excludes. Branch F therefore carries: **`ell'·ell'·F` must remain
in `im(d_1')` on every refined complex.** That is not sealed, and it is the one place
Branch F is exposed. It is a burden on a forced branch, not a competing candidate — no
require prefers `xi` on its account, because Branch xi does not satisfy `R6`/`R7`/`R9`
whatever the membership question does.

**Does Branch xi's `k−1` freedom violate any invariance or determinacy require?**
[PROVABLE] **Yes — three: `R6` (bulk residual, §2.2), `R7` (shape-dependent scalar),
`R9` (parent-inherited weighting).** Any one suffices.

**Does the subject ruling's over-`N_4` structure bear?** [PART-PROVABLE] **Decisively.**
It is what makes `R6` a require *about `F`*: intensive = per four-volume = `sum F²`
(§2.1). Without the over-`N_4` structure the invariance demand would be about an
extensive quantity and would be satisfied by volume additivity on both branches.

### 2.5 Why my draft verdict was wrong — the probe, not the glob

[PROVABLE] I probed `"refinement invariant"` (0 files) and `"invariant under
refinement"` (0 files) and `"held fixed"` (36 files, none refinement-related), and drew
a negative existential. The counts are correct. **The corpus does not use those
phrases.** It uses *"invariant under each elementary refinement"* (`R6`), *"refinement
naturality"* (V011, twice), *"a sealed class of regular-CW refinements"* (A27), *"no
shape-dependent scalar"* (`R7`). Every one evades both patterns.

[YOURS] This is the **sixth consecutive relay** in which my search, not my reasoning,
produced the defect — and it is a *new kind again*: not the space (711, 713), not the
span (715), not the vocabulary of the object (716), not self-inclusion (725), not
recursion depth (731), but **the phrasing of the predicate**. I installed the
object-names rule at 716 for a neighbouring failure and it did not catch this one,
because I probed for a *name* and the corpus states a *condition*.

The rule this needs, stated plainly: **a negative existential must be probed by
meaning, not by phrase — enumerate the ways the corpus could say it, or do not claim
absence.** I record it because I have now needed six such rules and the pattern is
itself the finding: my reasoning has held up; my instruments keep being the weak part.

---

## 3. RR3 — THE LAMBDA CONVERGENCE, EXAMINED

```text
LAMBDA_CONVERGENCE = DISTINCT-RHYMING, and now demonstrably so.
```

**Locus A — the refinement selector.** V011's two readings: `F_phys = im(d_1)`
(`aa7c6d49…[44801,44955)`) and `xi = ell_mu ell_nu F + h.o.t.`
(`aa7c6d49…[45718,46068)`). **This locus CLOSES here**: `R6`/`R7`/`R9` force `F` (§2).

**Locus B — the rescaling selector.** `(D2-4)`, `8dd59b35…[12383,12879)`: `ell_e →
lambda·ell_e`, `V_cell → lambda^d·V_cell`, *"Neither DoR-007 nor DoR-008 chooses
`lambda` or supplies a scale law."* **This locus stays OPEN**: none of R6/R7/R9 is a
rescaling require. `R6` quantifies over *elementary refinements*; `R9` over *promotion
of a subregion to a cell*; `R7` bars a scalar that varies with *shape*, and a global
`lambda` is not shape-dependent — it rescales every cell alike.

[YOURS] **Same candidate pair, different group acting, and now different status.** A
ruling filling Locus B would not have been needed to fill Locus A, and Locus A's closure
does not touch Locus B. They rhyme; they are not one absence.

[YOURS] Two honest qualifications. First, **I withdraw the textual-disjointness argument
I had drafted** — that neither locus's text mentions the other's operation. A verifier
showed the `(D2-4)` passage sits inside a subsection about geometric refinement with
refinement language within a few lines on both sides. The distinctness holds on the
*status* argument above, not on textual isolation. Second, the RA27-2 adoptions decision
names *"the missing datum — which of `xi`/`F` is held fixed under (D2-4)'s rescaling"* in
the singular; that phrasing descends from my own 725 artifact, so it is a ruling of
record rather than independent corroboration, and I do not lean on it either way.

---

## 4. RR4 — VERDICT

```text
VERDICT = FORCED (Branch F)

  Forced by R6 (the invariance require, whose own tolerance clause excludes the
  bulk residual), independently by R7 (the shape-dependent-scalar bar), and
  independently again by R9 (the executed intrinsic-cell binding, a sealed packet
  member bound to row A27).  Any one is sufficient; all three point the same way.

  THE FORCED RULE:  xi' = ell'_mu ell'_nu F  on every sub-cell.
                    For cubical bisection this is the equal in-plane split.
```

### 4.1 Nothing is adopted

[PROVABLE] A forced branch is a **derivation**, not an adoption. This artifact adopts
nothing, and the ruling that books the result of record is the principal's.

### 4.2 The C_ref clause was not used

[YOURS] A tempting fifth argument was available and I refused it: `C_ref`'s
*"preserving the same smooth coframe and connection"* would give `F` directly as the
curvature of a preserved connection. **That clause is barred as a source** (TYPE-R), the
relay restates the bar, and the forcing above does not touch it. Branch F is forced
without it.

### 4.3 What this does and does not discharge

```text
DISCHARGED     the branch selector for REFINEMENT.  731's binary closes on the F
               side, so 731's Branch-F column becomes the operative one.
NOT DISCHARGED
  RA27-2       the index still needs its discharge booked against D012; this
               supplies the transport rule the 727 finding was missing, and 727's
               finding is now resolved on the forced branch rather than standing.
  J2           gains a truth condition on Branch F -- but the R9-JII carrier
               REMAINS PENDING on its common-cell quantifier.  Not runnable.
  T_ref        fields 2, 4-8 remain; the S5.3 convergence burden is untouched.
  Branch F's   side condition (§2.4): ell'*ell'*F in im(d_1') under refinement --
               NOT sealed, and now the sharpest open item on this thread.
  lambda/beta  untouched (§3).
```

---

## 5. LEDGER, VOID, GROUNDING, JURISDICTION, VERB AUDIT

### 5.1 Ledger (verdict weight = 0)

| # | Encountered at | Classical likeness | Weight |
|---|---|---|---|
| L1 | intensive = extensive / four-volume | a density as an intensive thermodynamic variable | 0 |
| L2 | the bulk-vs-boundary residual test | distinguishing a volume term from a surface term in a scaling argument | 0 |
| L3 | "may not retain a parent's weighting profile" | a coarse-graining that must forget its origin | 0 |

### 5.2 VOID attestation

```text
VOID = CLEAN.  No downstream numeric consulted, computed, or estimated.  §2's
arithmetic is exact rational identity-checking on the displayed formula with
dimensionless placeholders; no physical quantity was evaluated and nothing was
compared to a measured constant.  The branch was not chosen for its consequence:
I drafted UNDERDETERMINED and the requires overturned it.
```

### 5.3 Grounding

| # | Step | Source + span | Tag |
|---|---|---|---|
| 1 | R1 `F_phys = im(d_1)`, `Q_flux` | `aa7c6d49…[44801,44955)` | PROVABLE |
| 2 | R2 A26 lift/exclusion/falsifier | `78f6bb08…[11181,11366)` | PROVABLE |
| 3 | R3 min-norm determinacy proof | `bc6c3e49…[36444,36745)` | PROVABLE |
| 4 | R4 gauge structure | `aa7c6d49…[44595,44690)` | PROVABLE |
| 5 | R5 measure + `xi = ell ell F` | `aa7c6d49…[45718,46068)` | PROVABLE |
| 6 | R6 the invariance require | `aa7c6d49…[47025,47247)` | PROVABLE |
| 7 | R7 the shape-scalar bar | `aa7c6d49…[46589,46710)` | PROVABLE |
| 8 | R8 the subject ruling | `112e6acb…[323,669)` | PROVABLE |
| 9 | R9 the executed intrinsic binding + verdict | `e60aec3c…[551,740)`, `[69,123)` | PROVABLE |
| 10 | R9's source is packet member D038, bound to A27 | packet copy sha `e60aec3c44cfc5f1…` | PROVABLE |
| 11 | A1 no scale law | `8dd59b35…[12383,12879)` | PROVABLE |
| 12 | L1 subject `= sum F^2` | §2.1, exact check | PROVABLE |
| 13 | L3 residual `= V F^2 (2s−1)^2`, ratio constant | §2.2, exact check | PROVABLE |
| 14 | Branch xi violates R6 | from 6, 13 | PART-PROVABLE |
| 15 | Branch xi violates R7 | from 7 | PART-PROVABLE |
| 16 | Branch xi violates R9 | from 9 | PART-PROVABLE |
| 17 | Branch F's `im(d_1)` side condition | §2.4 | PART-PROVABLE |
| 18 | Loci A and B differ in status | §3 | PART-PROVABLE |
| 19 | The probe-phrasing failure | §2.5, counts displayed | PROVABLE |
| 20 | VERDICT FORCED(F) | §4, from 14–16 | PART-PROVABLE |

```text
GROUNDED_STEPS = 20 / 20 (no YOURS-only step is load-bearing; §2.5's rule and §4.2's
refusal are commentary, not premises)
```

### 5.4 Jurisdiction check

**R6.** Written so a coefficient that degrades under subdivision is caught. Present
exactly here. Its outcome space distinguishes false from cannot-see — it tolerates a
vanishing boundary term and refuses a bulk one, which is the discrimination it exists
to make. It permits the evidence: Branch F satisfies it with residual zero.

**R7 and R9.** Written against inserted weights and against inherited parent profiles.
Both squarely present; Branch xi's share factor is each one's named object.

**The barred C_ref clause.** §4.2 records that it would have given a fifth argument and
was not used.

**R9-JII.** §4.3 records the carrier still PENDING; a forced branch does not form a
common cell and does not make the junction test runnable.

### 5.5 Self verb audit

| Verb or status | Warrant |
|---|---|
| `FORCED` | three independent sealed requires, two of them bars and one already executed |
| `VIOLATES` | only where a require's own text and a checked consequence conflict |
| `bulk, not boundary` | my exact check: residual/four-volume independent of `V` |
| `side condition` | Branch F's `im(d_1)` exposure — named as open, not waved past |
| `distinct-rhyming` | on differing status, after withdrawing the textual argument |
| `nothing adopted` | a forced branch is derived; the booking ruling is the principal's |

[YOURS] Disclosures against myself:

1. **My draft verdict was UNDERDETERMINED and it was wrong.** The attack I commissioned
   overturned it, as at 731. Two consecutive relays where adversarial verification
   reversed my headline result — and both times the defect was in how I searched, not
   in how I reasoned.
2. **I probed a phrase, not a predicate.** `"refinement invariant"` returns zero because
   the corpus says *"invariant under each elementary refinement"*. A negative existential
   is only as good as the enumeration of ways the thing could be said, and mine was one
   guess wide.
3. **I withdraw 733's drafted textual-disjointness argument** for RR3. The `(D2-4)`
   passage is embedded in refinement discussion; distinctness holds on status, not
   isolation.
4. **I did not lean on the decision that would have helped.** The RA27-2 adoptions
   ruling names the missing datum in the singular, which reads as support for
   *same-absence*; its phrasing descends from my own 725 artifact, so I treated it as a
   ruling of record rather than corroboration and used neither direction.
5. **Branch F is the branch I had already found tidier at 731**, and it is now the
   forced one. I record that the order was: draft UNDERDETERMINED, get refuted, verify
   the refutation myself, book FORCED — not the reverse.
6. No verb here proves, authorizes, computes, binds a member, forms a common cell,
   evaluates a junction map, adopts anything, or grants a seal.

```text
REQUIRES = 9 enumerated (modality-tagged) + 1 ALLOW
MATRIX = 2 x 9 displayed at §2
VERDICT = FORCED (Branch F) — forced independently by R6 (invariance; Branch xi's
    residual is BULK, ratio to four-volume constant, never tending to zero), by R7
    (any residual shape-dependent scalar fails A27), and by R9 (the executed
    intrinsic-cell binding, sealed packet member D038 bound to row A27: a promoted
    subregion "may not retain a weighting profile defined by an arbitrarily chosen
    parent"). Forced rule: xi' = ell'_mu ell'_nu F. Branch F's one open exposure:
    the im(d_1) side condition at §2.4.
LAMBDA_CONVERGENCE = distinct-rhyming (loci displayed: A = V011's two readings,
    CLOSED here; B = (D2-4)'s rescaling, still OPEN — no rescaling require exists)
VOID = clean
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+6 disclosures at §5.5)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
