# STAGE 8 / 7A / STEP 8 — THE FUNCTORIALITY CHARACTERIZATION

**Lane:** Dario (Opus 5, cross-family from the Codex build lanes)
**Date:** 2026-08-08
**Scope:** PASTE 731 only — PP1 incidence, PP2 characterization, PP3 consequences
**Custody:** archive-side read and write; the registrar owns any mirror
**Governing:** 729 `972eae9a…`; built index `66f078ba…`; FC-2 shape-regular class;
VOID condition in full force
**Charge:** re-derive, not trust. Nothing adopted.

## Lead determination

```text
PP1 = DERIVED, PROVABLE.  My 729 flag closes.  Both licensed moves ARE constructed
      in sealed text, with exact cell counts and the four-volume identity:
      "family-A member = one bisection of the unit 4-cube (16 subcubes,
       |C|_4 = 1/16); family-B member = the oriented order-simplex (Freudenthal)
       subdivision (24 simplices, |C|_4 = 1/24 each)".
      My 729 search missed it, and my first census this relay missed it again --
      that census was NON-RECURSIVE.  §1.3.

PP2 = THE CHARACTERIZATION I FIRST DERIVED IS REFUTED, BY MY OWN CHECK.

      I built a trichotomy on the constrained minimum of sum_i c_i xi_i^2.  The
      algebra is right and the conclusion is wrong: I summed over the IN-PLANE
      sub-faces only and omitted the TRANSVERSE cells the same refinement
      creates.  Restoring them, the refined total equals the parent EXACTLY --
      in every case I tested, isotropic and anisotropic, and short by exactly the
      transverse multiplicity m in my version.

      THE CORRECT RESULT IS SIMPLER AND STRONGER.  The sealed quantity is a sum
      over CELLS of V_cell * sum F^2.  If F is the same field on the sub-cells,
      functoriality is FOUR-VOLUME ADDITIVITY and is exact, with no boundary term
      and no freedom.  The sealed construction states that additivity outright.

      SO THE QUESTION WAS NEVER THE MEASURE.  It is: WHICH OF xi AND F IS HELD
      FIXED UNDER REFINEMENT?  On the F branch the rule is UNIQUE and forced by
      xi' = ell'_mu ell'_nu F.  On the xi branch 729's k-1 freedom is real.
      THE CORPUS DOES NOT SAY -- and it is the SAME unsealed datum I named at
      725 §2.4 for the lambda question.  One binary, two open threads.

CHARACTERIZATION = UNIQUE on one branch of a named unsealed binary; FAMILY on the
      other.  Adoption-free, and the binary is the principal's.
```

---

## 0. Preflight

[PROVABLE] `relay_outbox/731_ACK.md` was written **before** source work. Lane guard:
the header names **DARIO**. Read only after its sidecar verified:

```text
relay_inbox/RELAY_PASTE_731_FUNCTORIALITY_CHARACTERIZATION_DARIO_V001.md
  6f9e99c777f36f5fea3f8bc6e9e4664939f92c4f26ab600c04a597e38f279ea8   shasum -c OK
```

[PROVABLE] `STAGE8_7A_FUNCTORIALITY_CHARACTERIZATION_DARIO_V001.md` and its seal
sidecar were probed before the write and returned ABSENT.

### 0.1 Sources verified before use

```text
V011  review_packets/.../BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md  aa7c6d49…
MAJ   workspace/stage8_execution/work/MAJORANT_PHASE2_O3_O7_PROOF_DRAFT_V001.md
                                                                        08b91543…  sealed
729   STAGE8_7A_REFINEMENT_BRIDGE_DARIO_V001.md                         972eae9a…  (mine)
727   STAGE8_7A_RA27_2_INDEX_BUILT_DARIO_V001.md                        66f078ba…  (mine)
725   STAGE8_7A_RA27_2_ADOPTION_PACKAGE_DARIO_V001.md                   2acac49a…  (mine)
PREREG STAGE8_7A_OBS22_RECOGNITION_PREREG_V002_FROZEN.md                9f0d12b4…  unchanged
```

[PROVABLE] Writer-exclusion applied to every census: `*_DARIO_V001.md` excluded.

### 0.2 Method note — I commissioned attacks on my own derivation

[YOURS] Before writing, I ran five independent adversarial verifiers against the five
load-bearing claims of my draft characterization, each blind to my artifacts and
instructed to refute. **Two returned REFUTED and three NEEDS_QUALIFICATION.** I then
re-derived each contested point myself rather than adopting a verifier's word — §2.2's
arithmetic is my own check, not theirs. The process caught a real error in my
mathematics, which is what it is for and which §2.2 records at full weight.

### 0.3 Gates

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

No common cell formed, no junction map evaluated, no member bound, **no physical
quantity evaluated numerically**, no measured constant. The algebra below is symbolic
and structural, run on dimensionless generic rationals as an identity check. Nothing
adopted. No register, plan, tracker, git action.

---

## 1. PP1 — THE INCIDENCE LINE

### 1.1 The flag, from 729

At 729 §2.3 I marked the interior-edge cancellation `PART-PROVABLE`, needing *"the
subdivision to carry the standard incidence data"*, and wrote that if the registrar
wanted it airtight, that was the one line to seal. PP1 asks me to close it or spec it.

### 1.2 It closes — the construction is sealed

[PROVABLE] `MAJ` `08b91543…[19632,19996)`, sealed (sidecar present):

```text
Construction (exact): family-A member = one bisection of the unit
4-cube (16 subcubes, `|C|_4 = 1/16`); family-B member = the
oriented order-simplex (Freudenthal) subdivision (24 simplices,
`|C|_4 = 1/24` each — re-derived exactly by iterated polynomial
integration). Common refinement Z = Freudenthal subdivision of each
subcube: 384 cells of volume 1/384 each.
```

[PROVABLE] This supplies exactly what the flag needed and more: **both** licensed
moves constructed, with cell counts, and with the four-volume identity exact in each
case — `16 × 1/16 = 24 × 1/24 = 384 × 1/384 = 1`. A subdivision with exact volume
additivity and a stated cell count carries the standard incidence data; the interior
cancellation of 729 §2.3 follows.

```text
INCIDENCE = DERIVED, PROVABLE.  729 §2.3's PART-PROVABLE flag is closed, not specced.
```

### 1.3 How I missed it twice — the disclosure this relay owes first

[YOURS] At 729 I searched for a sub-edge/subdivision rule and reported absence. This
relay, asked whether the moves were *defined*, I ran a census that returned *"35
occurrences, zero with definitional markers"* and was about to book **spec it**.

**Both were wrong, and the second was wrong for a mechanical reason I can name.** My
census used `glob.glob("*.md")` from `workspace/` plus `../supervision/*.md` — **not
recursive**. It never entered `workspace/stage8_execution/work/`, where the sealed
construction lives. Re-run recursively the count is **50**, not 35, and one sealed file
carries the construction.

[YOURS] This is the fifth consecutive relay in which my *search*, not my reasoning, was
the defect — archive boundary (711), workspace-only (713), span coverage (715),
vocabulary (716), self-inclusion (725), and now **recursion depth**. The standing laws
cover the first five. The missing one is blunt: **state the glob, not just the
directory** — a searched-space declaration that says "workspace + supervision" while
the code says top-level-only is a false declaration, and mine was.

---

## 2. PP2 — THE CHARACTERIZATION

### 2.1 What I first derived, displayed because it was wrong

Let `c := V_cell/(ell_mu^2 ell_nu^2)` from `V011` `aa7c6d49…[45718,46068)`. Subdividing
one face into `k` sub-faces with the 729 constraint `sum_i xi_i = xi`, and writing
linear rules `xi_i = w_i xi` with `sum w_i = 1`, the refined contribution is
`(sum_i c_i w_i^2) xi^2`. That map is strictly convex on the affine set, so it has a
unique minimiser `w_i ∝ 1/c_i` with value `1/(sum_i 1/c_i)`. I concluded a trichotomy:
functoriality impossible / unique / a family, according as `c` is below, at, or above
that minimum — and computed that cubical bisection sits **exactly at** the minimum,
forcing the equal split.

**The algebra is correct. The conclusion is false.**

### 2.2 The refutation, re-derived by me

[PROVABLE] The sealed quantity is a sum over **cells**: `V011` `aa7c6d49…[46074,46387)`
— *"Therefore each cell contributes `V_cell sum_(mu<nu) F_(mu nu)^2`"*.

[YOURS] Refining a 4-cell does not merely subdivide one 2-face in its own plane. It
also produces **parallel translates of that plane in the two transverse directions**,
each a face of a distinct sub-cell, each carrying its own flux — and those translates
are **not** constrained to sum to `xi`. My constraint set omitted them entirely.

[PROVABLE] My own check, exact rational arithmetic on the displayed formula, with
`n_rho` cuts per direction, in-plane count `k = n_mu n_nu` and transverse multiplicity
`m = prod_{rho != mu,nu} n_rho`:

| extents | cuts | k | m | cells | my in-plane sum | all-cells sum | parent |
|---|---|---|---|---|---|---|---|
| 1,1,1,1 | 2,2,2,2 | 4 | 4 | 16 | 1/4 | **1** | 1 |
| 2,3,5,7 | 2,2,2,2 | 4 | 4 | 16 | 35/24 | **35/6** | 35/6 |
| 2,3,5,7 | 2,1,1,1 | 2 | 1 | 2 | 35/6 | **35/6** | 35/6 |
| 1,1,1,1 | 3,2,4,5 | 6 | 20 | 120 | 1/20 | **1** | 1 |

[PROVABLE] The all-cells sum equals the parent **exactly in every case**, and my
in-plane sum is short by exactly `m`. The third row is why the error survived my
first check: there `m = 1`, and the two agree — the single case I happened to compute
by hand at 731's opening.

[YOURS] **So functoriality is not delicate; it is automatic.** With `F` the same field
on the sub-cells, `sum_cells V_cell · sum F^2 = (sum_cells V_cell) · sum F^2 =
V · sum F^2` — four-volume additivity, which `MAJ` states exactly for both moves
(§1.2). No boundary term is needed; the subextensivity clause is satisfied with a
boundary term of zero.

### 2.3 The characterization, corrected

```text
THE CONDITION IS NOT A CONSTRAINT ON RULES.  It is a question about which object
the refinement holds fixed.

BRANCH F  (F is the primitive; xi is derived per cell by xi = ell_mu ell_nu F)
  Then xi' on a sub-cell is FORCED: xi'_i = ell'_mu ell'_nu F.
  The measure transports EXACTLY, by four-volume additivity, for BOTH licensed
  moves, with zero boundary term and for arbitrary anisotropy.
  CHARACTERIZATION ON THIS BRANCH: UNIQUE.  The rule is xi' = ell'_mu ell'_nu F,
  which for cubical bisection is the equal in-plane split -- the same rule my
  refuted trichotomy reached for the wrong reason.

BRANCH xi (xi is the primitive cochain in F_phys = im(d_1); F is its density)
  Then 729's analysis stands: d_1 constrains only the sum over sub-faces of a
  subdivided face, leaving k-1 free parameters per face, and the QUADRATIC
  measure moves with them while the linear total does not.
  CHARACTERIZATION ON THIS BRANCH: FAMILY, of dimension k-1 per subdivided face.

THE BINARY IS UNSEALED.  V011 carries BOTH readings: `F_phys = im(d_1)` makes the
xi's the cochains, and `xi_(mu nu) = ell_mu ell_nu F_(mu nu) + higher-order terms`
reads F as the primitive and xi as derived.  Neither is marked as the refinement
invariant.
```

[YOURS] **And it is the same missing datum I named at 725.** For the `lambda` question
I recorded the absent datum as *"a rule fixing which of `xi` / `F` is invariant under
(D2-4)'s rescaling"*. It is the identical binary here, under refinement rather than
rescaling. **One unsealed line governs two open threads** — `lambda`/`beta` and the
refinement bridge. I record the convergence and do not assert the two are the same
question; the corpus does not say that either.

### 2.4 What I do not claim

[YOURS] Four limits, stated because the corrected result is strong and a reader will
want to know its edges.

1. **`F` constant across a parent cell is a modelling reading**, not a sealed statement.
   The sealed relation carries `+ higher-order terms`, and on Branch F those terms are
   exactly what a subextensivity bound would have to control. My "zero boundary term"
   holds for the leading relation as displayed.
2. **The `xi`-branch family is per-face, not global**; whether it survives the
   shape-regular class over a refinement *sequence* is a separate question I did not
   answer, and one verifier argued the shape-regular clause bites on anisotropic
   sequences.
3. **I withdraw 729's suggestion that the answer is a "connection-refinement rule".**
   On Branch F no rule is needed; on Branch xi what is needed is the primitivity
   ruling, not a rule. 729 located the freedom correctly and mis-described the repair.
4. **The barycentric branch is expressible after all.** I had drafted that the formula's
   *"orthogonal physical cell"* quantifier makes it inexpressible for simplices; the
   next sentence of the same paragraph generalises through
   `wedge^2(e^(-1))` and `|det e|` and demotes the diagonal formula to *"a mandatory
   exact check"*. A verifier caught this and it is right; `MAJ` then constructs the
   simplicial move with exact volumes anyway.

---

## 3. PP3 — CONSEQUENCES, LEDGER, ATTESTATION

### 3.1 J2's truth condition

[PART-PROVABLE] On **Branch F**, J2 acquires a truth condition: the intensive
coefficient is invariant under the licensed re-presentations by exact additivity, so
*"invariant under cell re-presentation"* has a determinate value and it is satisfied
for these moves. On **Branch xi** it does not: the value moves with the `k−1`
parameters and the predicate has no determinate truth value.

[PROVABLE] Either way the **R9-JII carrier remains PENDING on its common-cell
quantifier** — the ruling and FC-1 both record it and this artifact does not touch it.
Nothing here makes the junction test runnable.

### 3.2 The sealed density instance's transport

[PART-PROVABLE] On Branch F the obstruction I reported at 727 dissolves: the measure
transports along the refinement arrows, so the exhaustion-indexed instance can in
principle be re-indexed on `Ref_a` — leaving the S5.3 burden untouched and undischarged,
and leaving `T_ref`'s fields 2, 4–8 exactly where they were. On Branch xi the 727
finding stands as written.

[YOURS] So the 727 finding is **branch-conditional**, not withdrawn. I state that
precisely rather than let a correction of my trichotomy read as a retraction of the
finding it was built on top of.

### 3.3 Ledger (verdict weight = 0)

| # | Encountered at | Classical likeness | Weight |
|---|---|---|---|
| L1 | the constrained-minimum trichotomy | parallel-resistance / harmonic composition | 0 |
| L2 | the `xi` vs `F` primitivity binary | choosing whether the field or its flux is the fundamental variable — a scheme choice | 0 |
| L3 | Branch F's exactness by volume additivity | an extensive quantity coarse-graining trivially | 0 |
| L4 | Branch xi's per-face freedom | a renormalization-scheme ambiguity surviving into the limit | 0 |

[YOURS] L4 is the rhyme the relay anticipated. It is a rhyme only: nothing runs, no
coefficient exists, and §2.3 records an unsealed binary rather than a measured scheme
dependence.

### 3.4 VOID attestation

```text
VOID = CLEAN

The characterization is structural.  No downstream numeric was consulted,
computed, or estimated.  The tables in §2.2 are EXACT RATIONAL IDENTITY CHECKS on
the displayed formula using dimensionless generic placeholders; no physical
quantity was evaluated and nothing was compared to a measured constant.  No rule
was adopted, no branch preferred, and the binary at §2.3 is left to the principal.
```

---

## 4. GROUNDING, JURISDICTION, VERB AUDIT

### 4.1 Grounding

| # | Step | Source + span | Tag |
|---|---|---|---|
| 1 | The measure formula and its quantifier | `aa7c6d49…[45718,46068)` | PROVABLE |
| 2 | The per-**cell** contribution; general-coframe map | `aa7c6d49…[46074,46387)` | PROVABLE |
| 3 | Both moves constructed; exact volume additivity | `08b91543…[19632,19996)` (sealed) | PROVABLE |
| 4 | PP1 closes: incidence data carried | §1.2, from 3 | PART-PROVABLE |
| 5 | The convexity lemma (correct in isolation) | §2.1, elementary | PROVABLE |
| 6 | The trichotomy's conclusion is false | §2.2, my exact-rational table | PROVABLE |
| 7 | All-cells sum = parent, exactly, 4/4 cases | §2.2 | PROVABLE |
| 8 | Branch F: UNIQUE, exact, zero boundary term | §2.3, from 2, 3, 7 | PART-PROVABLE |
| 9 | Branch xi: FAMILY of dimension k−1 | §2.3, from 729 | PART-PROVABLE |
| 10 | The binary is unsealed; V011 carries both readings | §2.3, from 1 and `F_phys=im(d_1)` | PART-PROVABLE |
| 11 | Same datum as 725's `lambda` gap | §2.3 | **YOURS** |
| 12 | J2 branch-conditional | §3.1 | PART-PROVABLE |
| 13 | 727's finding is branch-conditional, not withdrawn | §3.2 | **YOURS** |
| 14 | The four limits at §2.4 | §2.4 | **YOURS** |
| 15 | My census was non-recursive | §1.3, re-run displayed | PROVABLE |

```text
GROUNDED_STEPS = 12 / 15
YOURS, NAMED: 11, 13, 14.
```

### 4.2 Jurisdiction check

**The void condition.** Present throughout — a characterization is where a rule would
be chosen by its consequence. §3.4 attests; no branch is preferred and the binary is
left open even though Branch F is the tidier result.

**V011's quantifiers.** §2.4(4) records that I nearly over-read *"orthogonal physical
cell"* as a bar, and that the same paragraph's general-coframe sentence removes it. I
was applying a quantifier past its own text — the failure mode I have twice charged
elsewhere.

**R9 / R9-JII.** §3.1 records the carrier PENDING regardless of branch; no domain is
read as a truth condition and no common cell is formed.

**DoR-007 and the TYPE-R bars.** Untouched. Note the one place they bite here: a
verifier argued that C_ref's *"preserving the same smooth coframe and connection"*
clause pins the fine cochain and so kills Branch xi's freedom. That clause is exactly
the one **barred as a source** (TYPE-R, `4d` §6.3). It cannot be used to settle the
binary, and I decline to use it.

### 4.3 Self verb audit

| Verb or status | Warrant |
|---|---|
| `REFUTED` | applied to my own trichotomy, on my own exact-rational check |
| `UNIQUE` / `FAMILY` | each scoped to a named branch, never to the corpus as a whole |
| `DERIVED, PROVABLE` | PP1 only, on the sealed construction with volume additivity |
| `branch-conditional` | J2 and the 727 finding — neither withdrawn, both scoped |
| `I withdraw` | 729's "connection-refinement rule" phrasing, §2.4(3) |

[YOURS] Disclosures against myself:

1. **My characterization was wrong and the attack I commissioned found it.** I omitted
   the transverse cells a refinement creates and summed over the in-plane sub-faces
   only. The error survived my first check because the one case I computed by hand had
   transverse multiplicity 1 — the single configuration in which the wrong sum and the
   right sum agree.
2. **Twice in this relay I was about to book a wrong result.** `spec it` for PP1, and
   the trichotomy for PP2. Both were caught before sealing — one by a recursive re-run,
   one by adversarial verification — and neither by my first pass.
3. **My census declared a searched space it did not search.** *"workspace + supervision,
   recursive"* was the declaration; `glob.glob("*.md")` was the code. That is a false
   declaration, not a narrow one, and the searched-space clause exists precisely to
   stop it.
4. **729's repair phrasing was wrong** and I withdraw it: what is missing is not a rule
   assigning the connection on interior edges but a ruling on which object refinement
   holds fixed. 729 located the freedom correctly; it mis-named the fix.
5. **Branch F is the tidier, more publishable answer** and I have not preferred it. The
   binary is unsealed, the corpus carries both readings, and choosing here would be the
   move the void condition names.
6. No verb here proves, authorizes, computes, binds a member, forms a common cell,
   evaluates a junction map, adopts a rule or a branch, or grants a seal.

```text
INCIDENCE = derived PROVABLE (sealed construction 08b91543…[19632,19996): both moves
    constructed with exact cell counts and four-volume additivity; 729 §2.3's flag
    closes — and §1.3 discloses that my own census missed it by being non-recursive)
CHARACTERIZATION = UNIQUE (rule displayed: xi' = ell'_mu ell'_nu F, the equal in-plane
    split) ON BRANCH F; FAMILY of dimension k−1 per subdivided face ON BRANCH xi.
    The branch selector — which of xi / F refinement holds fixed — is UNSEALED and is
    the same datum named at 725 §2.4 for lambda. My first trichotomy is REFUTED by my
    own exact check (§2.2): it omitted the transverse cells and was short by exactly
    the transverse multiplicity m.
CONSEQUENCES = J2 gains a truth condition on Branch F and none on Branch xi; the
    density instance's transport dissolves on Branch F and 727's finding stands on
    Branch xi — branch-conditional, not withdrawn; R9-JII stays PENDING either way;
    RA27-2's discharge waits on the branch ruling, not on a new rule
LEDGER_ENTRIES = 4
VOID = clean
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+6 disclosures at §4.3)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
