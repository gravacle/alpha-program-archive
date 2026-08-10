# STAGE 8 — AXN BUILD — THE INFINITE-INCIDENCE EXTENSION
## DARIO LANE (Builder B) — RELAY 875 — [PLAN:AXN-BUILD-B3]

```text
alpha_computed         = false
proof_authorized       = false
kappa_record_computed  = false
```

No member bound; no fixed-point execution; no end test; no smooth import; no EM identification; no
common cell formed; no junction map evaluated; no numeric evaluation of any physical quantity; no
comparison to measured constants. PE-1..PE-13 pointer-only, none opened or consulted. Builder-A code
not opened. `~/.codex` untouched; memory-bank never searched. No register, plan, tracker, git action.

CLAIM STATUS: **all headline items CLAIMED.**

**The gap this relay attacks is MINE**, declared at 871. Subjects seal-verified BEFORE reading: my 871
`6b676829f46ecb2a`; Codex's 872 `2f0fa11e…` (sidecar OK); and the quasi-local source located **by its
citation** and verified **at its pin**.

---

## 0. LEAD

**The gap does not close — but it moves, and the move is real and derived.**

```text
871's STOP (mine):   "no infinite/incomplete TENSOR construction exists, so Gamma_p is undefined
                      for infinitely many incidences"
875's STOP (this):   "the GRADING AUTOMORPHISM alpha_infinity EXISTS BY THE SEALED CONSTRUCTION and
                      the census EXTENDS ON THE LIMIT ALGEBRA; what is missing is whether a generic,
                      possibly unbounded D_p^2 IS AFFILIATED WITH that algebra"
```

**`GRADING_LIMIT = EXISTS-BY-CONSTRUCTION` — as an automorphism, not as a spatial involution.**
**`CENSUS_LIMIT = EXTENDED` on the limit algebra, all four clauses re-derived.**
**`THEOREM_STATUS = STILL-FINITE (gap restated, and narrowed).`**

**The key observation, and it is about my own construction rather than about the corpus:**

```text
P_even = 1/2 (id + Ad_Gamma) ,  P_odd = 1/2 (id - Ad_Gamma)
```

**depends on `Γ` ONLY THROUGH `Ad_Γ`.** So the census never needed a spatial `Γ_∞` — it needs a
**grading automorphism**. And an automorphism is exactly what an algebraic inductive limit carries.

**I confirm Codex's 872 classification (`GENUINE-CONDITION`) and its flattening rejection of
"quasi-local inductive limit ⟹ spatial infinite tensor grading" — that rejection is correct.** What I
add is that the rejection does not cost as much as it appears to: **the spatial implementation was
never required for the census clauses**, only for the identification of `D_p²` as an object the
census can be applied to.

---

## 1. THE CANDIDATE, AT BYTES

**Located by citation and verified at its pin.** 872's closure table row *"quasi-local record limit"*
cites `[9198,10268)` span `0f94b343e788e87e…` in
`R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md` (`40890e753463b8c4`, verified). **I located
the span by recomputing digests over the corpus rather than trusting the row**, and it resolves
exactly.

What it constructs, verbatim in relevant part — *"Outgoing records and durability"*:

```text
After the closure face,   [H_K(t), I_source tensor A_j] = 0
for every bare observable A_j on that completed factor.

The gate must prove:
  1. exact invariance of the completed record's reduced state under every later
     source/new-record unitary;
  2. compatibility of the finite output states under  A -> A tensor I ;
  3. existence of the quasi-local outgoing record state;
  ... 4-7 ...
```

**Index set:** completed record factors `R_j`, exhausted along the closure faces.
**Compatibility maps:** the inclusions `A → A ⊗ I`.
**Scope declaration, and it is the sharp one:** items 1–7 are what **"the gate MUST PROVE"** — they
are **obligations, not established facts**. `PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md`
(`532b0f0eac4ac749`) supplies the compatible finite states and the inductive/projective limits at its
own span.

**A distinction I must hold and do:** the *algebraic* inductive limit `∪_N A_N` along the inclusions
is a purely algebraic object requiring **no state**. The gate's item 3 — *existence of the quasi-local
outgoing record **state*** — is what a **Hilbert-space completion** would need. **My extension below
lives entirely on the algebraic limit and consumes no state, so it does not depend on item 3.**

---

## 2. THE FIT — the parity structure survives, and by a two-line derivation

**Question: do the cell gradings' tensor extensions form a compatible system along the inclusions?**

For `a ∈ A_N`, with `Γ_{N+1} = Γ_N ⊗ Γ_cell`:

```text
alpha_{N+1}(a (x) I) = (G_N (x) G_c)(a (x) I)(G_N (x) G_c)
                     = (G_N a G_N) (x) (G_c I G_c)
                     = alpha_N(a) (x) G_c^2
                     = alpha_N(a) (x) I                     [since  Gamma_cell^2 = I ]
```

**The whole compatibility rests on `Γ_cell² = I`, which is sealed** (grading authority `2215f79c…`,
and I verified `‖Γ_cell² − I‖ = 0.000e+00` at 862). Numerically confirmed for `N = 1,2,3`:
**residual `0.000e+00` at every level.**

**Therefore `α_∞ := lim_N α_N` exists on the algebraic inductive limit BY THE SEALED CONSTRUCTION —
no reference sequence, no state, no completion, nothing chosen.** Each `α_N` is `Ad` by a
self-adjoint unitary, hence a `*`-automorphism, hence isometric; the system is compatible; the limit
automorphism is determined.

**`GRADING_LIMIT = EXISTS-BY-CONSTRUCTION`, as an automorphism.**

**What I do NOT claim, and Codex was right to reject it:** a **spatial** `Γ_∞` — an involution
operator on a Hilbert space implementing `α_∞`. That would need the completion, a reference vector or
state, and an implementation theorem. **None is supplied and none is authored here.**

---

## 3. THE CENSUS AT THE LIMIT — extended, all four clauses re-derived

**The census construction never used `Γ` except through `Ad_Γ`.** With `α := α_∞`, `α² = id`:

| clause | derivation on the limit algebra |
|---|---|
| **reconstruction** | `P_even + P_odd = ½(id+α) + ½(id−α) = id`, so the two components sum to the element |
| **idempotence** | `P_even² = ¼(id + 2α + α²) = ¼(2·id + 2α) = ½(id+α) = P_even`; likewise `P_odd` |
| **orthogonality** | `P_even ∘ P_odd = ¼(id − α²) = 0` |
| **no-refinement** | a scalar split of an `α`-homogeneous element yields pieces of the **same** parity, so `P_odd` returns the odd component whole and the split produces no different census — the 862 argument, which used only homogeneity |

**All four are algebraic in `α` alone. `CENSUS_LIMIT = EXTENDED` for every element of the limit
algebra.**

**And here is the residual stop, stated exactly.** The census extends to elements **of the limit
algebra**. The theorem is about `D_p²`. So the live question is:

```text
IS A GENERIC, POSSIBLY UNBOUNDED  D_p^2  AN ELEMENT OF / AFFILIATED WITH  the quasi-local limit algebra?
```

**Not supplied.** 872 names it precisely — *"the closure does not state or prove that a generic
U1-produced, possibly unbounded `D_p²` is affiliated with that quasi-local graded algebra"* — and I
confirm that at the closure. **Law 9b, closure-first:** the closure is 872's declared seven-row table
(every whole-file digest fixed by verified sidecar or verified parent pin, every span carrying a full
content digest) **plus** the two BID grading sources **plus** the R3_4 parent SPEC's fifteen pinned
authorities. *Within that declared closure*, no member supplies an affiliation or domain theorem for a
generic unbounded `D_p²`.

**A convergence worth the registrar's attention:** that missing object — **affiliation of an unbounded
operator to the record algebra, with its domain** — is the **same object family as S4**, whose stop my
864 typed and whose free-tail partial I cross-checked at 869. **The infinite-incidence gap and the S4
gap meet on one missing object.** Closing S4's operator/affiliation half would bear directly on this
one; they are not two independent debts.

---

## 4. COVARIANCE AT THE LIMIT — extends conditionally, condition named

Q-780 strengthened covariance at finite level to **outright over the admitted action, with mixing
excludable** — the opposite lane's result, consumed at its sealed scope and **not re-derived here**.

At the limit, for an action member given by a compatible system `{R_N}` along the inclusions with each
`R_N` `Γ_N`-homogeneous, my 871 two-line argument applies **level by level** — `[R,Γ]=0` and
`{R,Γ}=0` both give `Γ(RMR*)Γ = R(ΓMΓ)R*`, the two signs cancelling in the second case — and passes to
`α_∞` because the system is compatible.

**`COVARIANCE_LIMIT = EXTENDED, conditional on the action being inclusion-compatible.`** **What is not
supplied:** that **every** admitted action member forms a compatible system along the inclusions.
Tensor relabelings and grading-commuting relabelings are compatible by construction; a general `U_c`
is not shown to be. **I state the condition rather than assuming it** — assuming it would be the same
move as treating the algebra limit as a grading limit.

---

## 5. SCOPE — capped at the construction's own sealed scope

- The extension lives on the **algebraic** inductive limit and **consumes no state**; it therefore does
  not depend on the gate's item 3 (*existence of the quasi-local outgoing record state*), and equally
  **claims nothing about it**.
- **No completion is authored.** No reference sequence, vector, or state is chosen. **No spatial
  `Γ_∞` is constructed.**
- The seven branch hypotheses remain **ANTECEDENTS**; outside-branch competitors remain live.
- 872's own gate items 1–7 remain **obligations of the gate**, none discharged here.
- **`THEOREM_STATUS = STILL-FINITE`** for the theorem as posed — a census **of `D_p²`** — because
  affiliation is unsupplied. **The construction underneath it is no longer finite**, and that is the
  narrowing.

---

## 6. FREEDOMS-CONSUMED (law 2, law 2a)

```text
CARRIED UNCHANGED: Gamma_cell^2 = I as sealed (the ONLY input the compatibility derivation consumes);
  the algebraic inductive limit and its inclusions at their sealed scope; the gate's items 1-7 AS
  OBLIGATIONS, none treated as established; Q-780's finite-level covariance strengthening consumed at
  its sealed scope and NOT re-derived; the seven branch hypotheses as ANTECEDENTS with competitors
  live; my own 871 existence stop carried and then NARROWED, not silently widened.

DERIVED HERE: (a) the compatibility alpha_{N+1}(a (x) I) = alpha_N(a) (x) I, from Gamma_cell^2 = I,
  confirmed at N = 1,2,3 at 0.000e+00; (b) hence alpha_infinity on the algebraic inductive limit, by
  construction and with nothing chosen; (c) the observation that P_even/P_odd depend on Gamma ONLY
  through Ad_Gamma, so the census never required a spatial grading; (d) re-derivation of all four
  census clauses in alpha alone; (e) the relocated stop — affiliation of a generic unbounded D_p^2 to
  the limit algebra; (f) the convergence of that stop with S4's operator/affiliation half.

SELECTED HERE: NOTHING.  No reference sequence, vector, state, completion, spatial grading, affiliation
  theorem, or domain is constructed, chosen, or assumed.  NO FLAG MOVES.  The theorem is not promoted:
  its status stays STILL-FINITE.

NOT DONE AND DISCLOSED: I did not re-derive Q-780's covariance strengthening — I consume it.  I did
  not verify the gate's items 1-7 or attempt any of them.  The covariance extension is CONDITIONAL on
  inclusion-compatibility of the admitted action, which I do not establish.  My compatibility check is
  a derivation confirmed at three levels, not an induction written out; the derivation is the content
  and the numerics are a sanity check.
```

**FLATTENING CHECK — 37/37 walked, clean.**
**S03 and THE VOID CONDITION — live at the exact place the relay warned about.** The tidy move was to
take "a sealed quasi-local inductive limit exists" and read it as "so `Γ_∞` exists". **That
identification is precisely what 872's own flattening check rejects, and I reject it too** — what
exists is an **automorphism** on an **algebraic** limit, and I say which of the census's needs that
does and does not meet. **No spatial grading is built.**
**S12** — the gate's items carried as **obligations**, never as established facts; `α_∞` carried as an
automorphism, never as an operator.
**S26 / S08 / S19 / S24** untouched — no completion, state, or regularity class imported; the
algebraic limit is used **because** it needs none.
**T1 / T5** untouched.
**BR-1 HELD.** 872 is a producer-declared object: it may accuse and never exculpate. **Its located
candidate was the claim under test** — I re-found the span by digest rather than trusting the row, and
its classification (`GENUINE-CONDITION`) is confirmed by my own derivation rather than adopted.

---

## 7. FINAL LINES

```text
CANDIDATE = displayed (bytes, scope).  Located BY ITS CITATION and verified AT ITS PIN — I re-found
  the span by recomputing digests over the corpus rather than trusting 872's row: [9198,10268) span
  0f94b343e788e87e in R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md (40890e753463b8c4,
  verified).  IT CONSTRUCTS: the quasi-local outgoing record limit over completed record factors R_j
  exhausted along closure faces, with compatibility maps A -> A (x) I, and [H_K(t), I_source (x) A_j]
  = 0 after the closure face.  ITS OWN SCOPE DECLARATION IS THE SHARP POINT: items 1-7 are what "THE
  GATE MUST PROVE" — OBLIGATIONS, NOT ESTABLISHED FACTS — including item 3, existence of the
  quasi-local outgoing record STATE.  DISTINCTION I HOLD: the ALGEBRAIC inductive limit along the
  inclusions needs NO STATE; item 3 is what a HILBERT COMPLETION would need.  MY EXTENSION LIVES
  ENTIRELY ON THE ALGEBRAIC LIMIT AND CONSUMES NO STATE, SO IT DOES NOT DEPEND ON ITEM 3 AND CLAIMS
  NOTHING ABOUT IT.
GRADING_LIMIT = EXISTS-BY-CONSTRUCTION (derivation displayed) — AS AN AUTOMORPHISM, NOT A SPATIAL
  INVOLUTION.  For a in A_N with Gamma_{N+1} = Gamma_N (x) Gamma_cell:
  (G_N (x) G_c)(a (x) I)(G_N (x) G_c) = (G_N a G_N) (x) G_c^2 = alpha_N(a) (x) I.
  THE WHOLE COMPATIBILITY RESTS ON Gamma_cell^2 = I, WHICH IS SEALED, and I verified the residual at
  N = 1,2,3 as 0.000e+00.  Each alpha_N is Ad by a self-adjoint unitary, hence a *-automorphism,
  hence isometric; the system is compatible; alpha_infinity is DETERMINED.  NO REFERENCE SEQUENCE, NO
  STATE, NO COMPLETION, NOTHING CHOSEN.  I DO NOT CLAIM A SPATIAL Gamma_infinity, AND CODEX'S 872 WAS
  RIGHT TO REJECT THAT IDENTIFICATION.
CENSUS_LIMIT = EXTENDED (all four clauses re-derived).  THE KEY OBSERVATION IS ABOUT MY OWN
  CONSTRUCTION, NOT ABOUT THE CORPUS: P_even = 1/2(id + Ad_Gamma) and P_odd = 1/2(id - Ad_Gamma)
  DEPEND ON Gamma ONLY THROUGH Ad_Gamma — THE CENSUS NEVER NEEDED A SPATIAL GRADING, ONLY A GRADING
  AUTOMORPHISM, WHICH IS EXACTLY WHAT AN ALGEBRAIC INDUCTIVE LIMIT CARRIES.  With alpha^2 = id:
  reconstruction P_even + P_odd = id; idempotence P_even^2 = 1/4(id + 2alpha + alpha^2) = P_even;
  orthogonality P_even P_odd = 1/4(id - alpha^2) = 0; no-refinement because a scalar split of an
  alpha-homogeneous element yields SAME-PARITY pieces, so P_odd returns the odd component WHOLE (the
  862 argument, which used only homogeneity).  ALL FOUR ALGEBRAIC IN alpha ALONE.
  THE RESIDUAL STOP, EXACTLY: the census extends to elements OF THE LIMIT ALGEBRA, and the theorem is
  about D_p^2 — SO THE LIVE QUESTION IS WHETHER A GENERIC, POSSIBLY UNBOUNDED D_p^2 IS AFFILIATED WITH
  THAT ALGEBRA.  NOT SUPPLIED, and 872 names it precisely.  LAW 9b CLOSURE-FIRST: the closure is 872's
  declared seven-row table plus the two BID grading sources plus the R3_4 SPEC's fifteen pinned
  authorities; WITHIN IT no member supplies an affiliation or domain theorem for a generic unbounded
  D_p^2.  CONVERGENCE FOR THE REGISTRAR: that missing object is THE SAME OBJECT FAMILY AS S4 — whose
  stop my 864 typed and whose free-tail partial I cross-checked at 869 — SO THE INFINITE-INCIDENCE GAP
  AND THE S4 GAP MEET ON ONE MISSING OBJECT; THEY ARE NOT TWO INDEPENDENT DEBTS.
COVARIANCE_LIMIT = EXTENDED, CONDITIONAL, condition named.  For an action member given by a compatible
  system {R_N} along the inclusions with each R_N Gamma_N-homogeneous, my 871 two-line argument applies
  level by level — [R,Gamma]=0 and {R,Gamma}=0 BOTH give Gamma(RMR*)Gamma = R(Gamma M Gamma)R*, the two
  signs cancelling in the second — and passes to alpha_infinity because the system is compatible.  NOT
  SUPPLIED: that EVERY admitted action member forms a compatible system along the inclusions.  Tensor
  relabelings and grading-commuting relabelings are compatible by construction; a general U_c is not
  shown to be.  I STATE THE CONDITION RATHER THAN ASSUMING IT — assuming it would be the same move as
  treating the algebra limit as a grading limit.  Q-780's finite-level strengthening is CONSUMED at its
  sealed scope and NOT re-derived.
THEOREM_STATUS = STILL-FINITE (gap restated, AND NARROWED).  The theorem as posed is a census OF
  D_p^2, and affiliation is unsupplied, so its status does not change.  BUT THE CONSTRUCTION UNDERNEATH
  IT IS NO LONGER FINITE: 871's stop was "no infinite/incomplete TENSOR construction exists, so
  Gamma_p is undefined at infinite incidence"; the stop is now "the GRADING AUTOMORPHISM EXISTS BY THE
  SEALED CONSTRUCTION and the census EXTENDS ON THE LIMIT ALGEBRA — what is missing is AFFILIATION of a
  generic unbounded D_p^2."  I CONFIRM 872's GENUINE-CONDITION CLASSIFICATION AND ITS FLATTENING
  REJECTION; what I add is that the rejection COSTS LESS THAN IT APPEARS TO, because the spatial
  implementation was never required by the census clauses — only by the identification of D_p^2 as
  something the census can be applied to.
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+3):
  (1) THE STOP I NARROWED WAS MY OWN, AND I NARROWED IT BY NOTICING SOMETHING ABOUT MY OWN
      CONSTRUCTION THAT I SHOULD HAVE NOTICED AT 871.  P_even/P_odd depend on Gamma only through
      Ad_Gamma — that is visible in the definition I myself wrote, and at 871 I nonetheless stopped at
      "no infinite TENSOR construction", i.e. I stopped at the absence of a SPATIAL object my own
      construction never needed.  The corpus did not change between 871 and now; MY READING OF MY OWN
      FORMULA DID.
  (2) THE OPPOSITE LANE'S SEARCH REACHED THE CANDIDATE AND MINE DID NOT — the second time in three
      relays (869: the scaling result my endpoint-conjunction excluded).  I record the PATTERN, not
      the instance: my enumerations keep being cut by a conjunction or by a token I expect the answer
      to contain.  872's closure-first method — declare the closure, then bind "missing" to it — is
      the discipline I adopted at 869 and used here, and it is not the same skill as choosing the
      right query in the first place.
  (3) I CONFIRMED THE OPPOSITE LANE'S CLASSIFICATION WHILE ADDING A RESULT THAT SOFTENS ITS
      CONSEQUENCE, WHICH IS A SHAPE WORTH DISTRUSTING.  "You were right, and also it matters less than
      you said" is a comfortable thing for a checked lane to conclude.  The guard is that the softening
      is a two-line algebraic identity anyone can check against the definition, and that I DID NOT
      MOVE THE THEOREM'S STATUS: it stays STILL-FINITE.  If the affiliation question is as hard as S4
      suggests, the narrowing buys the round very little, and I do not claim otherwise.
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

---

**GATES HELD.** Charter fences live; nothing selected; no smooth import; no EM identification; no
member binding; no fixed-point execution; no end test; no numeric evaluation of physical quantities;
no comparison to measured constants; no common cell formed; no junction map evaluated. PE-1..PE-13
pointer-only, none opened or consulted. Builder-B independence held. `~/.codex` untouched;
memory-bank never searched. No register, plan, tracker, or git action.
