# STAGE 8 / 7A / [PLAN:B1c-3] — NOT THIS CANDIDATE: THE EXHIBIT CLOSES THE COFRAME SIDE AND LEAVES THE DENSITY SIDE UNTOUCHED

Lane: DARIO (Builder B, independent verifier). Relay 806.
State brief pinned: `PROGRAM_STATE_BRIEF_V005.md` = `e26f0d16055f3e83…`, seal OK. Drift check:
V005 and `DECLINE_REGISTER_V002` current.
Receiver: **793** `STAGE8_B1C_DENSITY_RECEIVER_BUILD_CODEX2_V001.md` = `0c53549766730513…`,
`.md.seal` **OK** (law 8, both spellings probed).
Candidate: my own **804** exhibit (identity-law transport + constant-form lift).
**The exhibit is TESTED, never adopted.** All headline items **CLAIMED**.
Per the relay: 805 runs lane-opposite on the divergence; **802's `L` question is not touched here.**

## Lead determination — CLAIMED

```text
VERDICT = NOT-THIS-CANDIDATE.
   Rejecting predicate: I1, receiver acceptance — the candidate has no delta_K, so it is not
   even an OBJECT ROW of CDensRecv(Ref_a).  Second, independent rejection: I5, conserved-current
   transport — the exhibit says nothing about Curr(K) or J_K.
```

**But the residual gap is now sharply typed, and that is the relay's real product.** 793 named the
missing object as `JOINT_A1_A2_FIELD_EXT_MEMBER`, a ten-component tuple, and named its blocker
precisely:

> *"What is absent is `a'` on the new interior edges — equivalently the `k−1`-parameter distribution
> of parent flux among `k` children — and the density member compatible with that choice."*

**The exhibit supplies the `a'`.** Verified by me on **both** generators, exactly:

```text
A2 Freudenthal : d_1' a' = xi solved and re-verified entrywise; a' assigned on all 65 edges,
                 including the 33 new diagonal interior edges.
A1 bisection   : d_1' a' = xi solved and re-verified entrywise; a' on all 216 edges, with 116
                 nonzero values on non-parent edges.
```

So the `k−1`-parameter distribution is fixed — by the constant form — and it is exactly the choice
that makes the quadratic exact. **793's I8 build failure is discharged on the coframe side**, and
its I2 build failure is partially discharged.

```text
JOINT_A1_A2_FIELD_EXT_MEMBER = (f_g, F_g, s_g, S_g; e_K', mu_K', a_K', F_K', delta_K', d_g)

SUPPLIED by the exhibit (4/10):  e_K'  mu_K'  a_K'  F_K'
   plus the properties: exact intrinsic-Vol_4 quadratic transport; incidence preservation;
   identity and composition.
STILL ABSENT (6/10):            f_g  F_g  s_g  S_g  delta_K'  d_g
   i.e. exactly the CURRENT side (s_g, S_g), the DENSITY side (delta_K', d_g), and SUPPORT
   (f_g, F_g).
```

**The gap moved from "the coframe/curvature datum is missing" to "only the density and current
data are missing."** That is a different and better-posed remainder, and it is not one this lane
can close: `R4Dens(K)` is *deliberately opaque* in 793 by design.

---

## 1. AS1 — THE CANDIDATE, ASSEMBLED IN RECEIVER TYPES

### 1.1 What the exhibit is

From my 804, verified there in exact rationals: `S` = the lift of a constant coordinate 2-form `F`;
`M_p = I_6` on every child; `(1/24) Σ_p M_p^T M_p = I_6`; `C S = I_6`; `S` curvature-nonzero.

### 1.2 The conversions — named, because this arc's failures were conversions

**This mapping is itself a step, and I state it rather than assume it.** Two convention traps have
already cost this arc a relay each: `L`'s normalization (804) and a transpose-pivot basis
extraction (804, my own bug).

| 793's type | what the exhibit supplies | conversion, stated |
|---|---|---|
| `Cof(K)` — derived A0/A1/A2 coframe carrier (G6) | the derived child frames `E_p` from **753** | **identity** — 793's G6 and my 753 cite the same derived frames; no conversion needed |
| `Vol(K,C) = Vol_4(C)` (G6/G7) | `Vol_4 = |det E|/4!` on simplices, `(1/2)^4` per bisection child | **identity** — the same forced intrinsic measure; no alternate measure introduced |
| `a_K'`, `F_K' = d_1' a_K'` (bridge, §2.1) | solved exactly on both generators (§0) | **identity in the coordinate reading.** The quadratic is evaluated in V011 D10's **local orthonormal frame** — `V_cell · Σ_{μ<ν} F_{μν}²` — which is the reading my 804 exhibit used. **I do not convert to the general-coframe form; that is 802's `L` question and the relay bars touching it.** |
| `Curr(K) = ker(B_K^T)` (G3) | **nothing** | no conversion possible — the exhibit is a curvature/coframe object, not a current object |
| `R4Dens(K)` (G5) | **nothing** | `R4Dens` is deliberately opaque; the exhibit has no density slot to convert |

```text
CANDIDATE = assembled (conversions displayed), and it is a PARTIAL member by construction:
   it populates the coframe/curvature/measure fields and leaves the current and density fields
   empty.  I state that before running the predicates rather than discovering it in the tally.
```

---

## 2. AS2 — THE NINE PREDICATES

| # | predicate | verdict | computation or named element |
|---|---|---|---|
| **I1** | receiver acceptance (one field in the full realization) | **FAIL — REJECTING** | `CDensRecv`'s object row requires `delta_K ∈ R4Dens(K)` with `Pos`, `Dual`, `VolNorm`, `CurrentDomain`. The candidate has **no `delta_K`**. It is not an object row, so it is not a member. |
| **I2** | `Ref_a` totality on every generator and composite | **PARTIAL** | **Coframe side TOTAL, verified:** the identity law is defined and quadratic-exact on A0 (1 cell, `Vol_4 = 1`), A1 (16 × 1/16), A2 (24 × 1/24), and composites (A1∘A2 and A2∘A1: 384 × 1/384 = 1). Receiver arrow data `S_R`, `d_R` absent, so receiver-level totality is not evaluable. |
| **I3** | positive coframe-dual `Vol_4` density type | **UNPOSEABLE** | `R4Dens(K)` opaque by design; no `delta_K` supplied. Unchanged from 793. |
| **I4** | functoriality | **PASS (coframe side)** | `M^{h∘g} = M^h M^g = I_6 · I_6 = I_6`, the identity law on the composite; `L_id = id` **PROVED** at 795 (`sd*_1` injective on A0 ⟹ unique section). Composition closes. `d_R`/`S_R` functoriality: absent. |
| **I5** | conserved-current transport `J_{K'}(S_R c) = R_* J_K(c)` | **FAIL — REJECTING** | The exhibit supplies no `S_R : Curr(K) → Curr(K')`. It is a statement about curvature and the coframe, not about `ker(B_K^T)` or `J_K`. **Independent of I1.** |
| **I6** | incidence intertwining | **PASS** | `C S = I_6` verified exactly on all six components (804). The incidence half is **PROVED** of record (Q-702: builder 788 + independent 794, exact integer matrix identity plus 771 random-cochain trials). |
| **I7** | coframe duality `DualitySquare(R, d_R, Cof_R)` | **UNPOSEABLE** | Coframe transports are derived (G6) and the predicate is typed, but it quantifies over `d_R`, which is absent. |
| **I8** | exact-energy / intrinsic `Vol_4` compatibility | **PASS on the coframe side — 793's build failure DISCHARGED** | 793 failed this because *"fixed total flux leaves `k−1` child-flux parameters, while the measure is quadratic."* The exhibit **fixes those parameters** via `a'` and the result is exact: children/parent `= 1` on A0, A1, A2 and composites. The single fact used is `Σ_i Vol_4(C'_i) = Vol_4(C)`. The receiver's own `ExactVol4Quadratic(R, d_R)` quantifies over `d_R` and remains unevaluable. |
| **I9** | covariance / common carrier / support / anti-tuning | **UNPOSEABLE** | Support map `F_g` and a common instantiated `tau_ker` absent (G7). This is the exhaustion-vs-refinement index gap my 792/798 typed; unchanged here. |

```text
PREDICATES = 3/9 pass (I4, I6, I8 — on the components the candidate supplies)
             1/9 partial (I2, coframe-side total)
             2/9 fail    (I1 receiver acceptance; I5 conserved-current transport)
             3/9 unposeable (I3, I7, I9 — all quantify over the absent delta_K / d_R / tau_ker)
```

**Every unposeable quantifies over the density or support data. Every pass is on the
coframe/curvature/measure data. The split is clean and it is the finding.**

---

## 3. AS3 — VERDICT

```text
VERDICT = NOT-THIS-CANDIDATE.
   REJECTING PREDICATE: I1 (receiver acceptance).  REASON, exactly: CDensRecv(Ref_a)'s object row
   demands delta_K in R4Dens(K); the exhibit is a coframe/curvature object and supplies no density
   slot, so it cannot be an object row, let alone an inhabitant.
   SECOND, INDEPENDENT REJECTION: I5 (conserved-current transport) — no S_R on Curr(K).
   The relay anticipated exactly this shape: "the identity law may fail density-side predicates
   even while solving the coframe system."  It does, and that types the residual gap sharply.

RESIDUAL GAP, NEWLY TYPED:
   BEFORE (793): JOINT_A1_A2_FIELD_EXT_MEMBER absent as a whole; blocker named as a' on the new
                 interior edges plus a compatible density member.
   AFTER  (this relay): a' IS SUPPLIED on both A1 and A2, verified entrywise; with it e_K', mu_K',
                 F_K', the exact quadratic transport, incidence preservation, and
                 identity/composition.  4 of 10 components, and the named blocker among them.
   WHAT REMAINS: f_g, F_g (support), s_g, S_g (current), delta_K', d_g (density) — 6 of 10, and
                 they are ALL on the density/current/support side, which R4Dens's deliberate
                 opacity makes a typing question, not a computation this lane can run.

B1C INHABITANCE: still open, but no longer open at the coframe layer.
FORCING: still gated, and the gate has narrowed from JOINT_A1_A2_FIELD_EXT_MEMBER entire to its
   density/current/support half.
```

### 3.1 B2 runnability

```text
B2_RUNNABLE = NO — with the reason changed, and the change matters.
   793: not runnable because "its required B1 transport input does not exist under those
        constraints."  My 804 withdrew the stronger "impossible" as an inference from a refuted
        empty verdict.
   NOW: a B1 coframe transport EXISTS (the identity law, total on A0/A1/A2 and composites).  B2
        remains not runnable because its input is a receiver MEMBER, and the receiver is still
        uninhabited on its density and current rows.
   So B2's blocker is no longer "no transport exists"; it is "the transport that exists is not yet
   a receiver member."  Whether B2 in fact needs the density row, or could run on the coframe
   transport alone, is a scope question for the receiver's own lane — I do not decide it.
```

---

## 4. AS4 — FREEDOMS CONSUMED, FLATTENING CHECK

### 4.1 `FREEDOMS_CONSUMED` (law 2a) — item by item against §1–§3

| datum | tag |
|---|---|
| **the identity law / the exhibit** | **TESTED, NOT ADOPTED** — displayed as one candidate against a typed receiver; it is not proposed as the law, and the verdict is that it is *not* the member |
| the constant form `F` | **CARRIED SYMBOLICALLY** — a generic rational `F`; no value adopted |
| `a'` on new interior edges | **DISPLAYED AS A CONSEQUENCE of the constant form**, not chosen as a split rule — no equal-split or area-proportional rule is adopted, and 793's bar on both is respected |
| child frames `E_p`, orientations | **CARRIED AS DERIVED** (753 = 793's G6) |
| intrinsic `Vol_4` | **CARRIED AS FORCED/CLASSIFIED** — no alternate measure |
| the quadratic's frame reading | **CARRIED AS THE ORTHONORMAL READING** of V011 D10, disclosed; the general-coframe form is **802's question and is not touched** |
| `delta_K`, `d_g` (density) | **NOT SUPPLIED, NOT AUTHORED** — `R4Dens` left opaque as 793 designed it |
| `S_g`, `s_g` (current) | **NOT SUPPLIED** |
| `F_g`, `tau_ker` (support) | **NOT SUPPLIED** — G7's gap preserved |
| scaling weights (law 2a) | **NONE CONSUMED** — no `beta`-graded statement here |
| smooth constituent | **NOT CONSUMED; BARRED (S26)** |

**SUBSTITUTED: none.**

### 4.2 `FLATTENING_CHECK` — `DECLINE_REGISTER_V002` (S01–S37)

```text
S26  C_ref barred as a source        CLEAN — not invoked; all objects are finite cochains, derived
     frames, and the classified Vol_4.
S08  no EM / Maxwell / smooth-field / response identification   CLEAN — the curvature, coframe and
     (absent) density are not identified with electromagnetism or a public field.
S28  the free data unselected        CLEAN — nothing selected by desired outcome; the exhibit is
     tested and REJECTED, which is the opposite of selection.
S01-S07, S09-S27, S29-S37: untouched.
FLATTENING_CHECK = clean (37 rows walked; 3 live, all discharged).
```

---

## 5. JURISDICTION AND VERB AUDIT

**Jurisdiction.** *What was the rule written to protect?* The relay hands me my own exhibit and asks
me to test it — the standing risk being that a lane grades its own construction generously. *Does
the outcome space distinguish?* Yes: the verdict is **NOT-THIS-CANDIDATE**, against my own object,
with two independent rejecting predicates named. *Would evidence look different if it were an
inhabitant?* Yes: `delta_K` and `S_R` would exist. They do not.

**VOID CONDITION.** Nothing adopted. `a'` is displayed as a consequence of the constant form, not
chosen as a split rule — 793 expressly bars equal-split and area-proportional choices, and I make
neither.

**BR-1.** The relay authorises the test; it does not authorise a pass. The result is a rejection of
my own candidate.

**Builder independence.** No `evaluator_build_A/` or `checks/` file read. 802's `L` question
untouched per the relay. `~/.codex` untouched; `memory-bank` never searched.

### 5.1 Self verb audit — **NOT CLEAN: two disclosures**

1. **I stated the candidate was partial before running the predicates, and I should say why that
   is not a hedge.** Reading 793's object row makes the absence of `delta_K` immediate; a tally
   that "discovered" it at predicate 9 would have dressed a foreseeable rejection as a finding. The
   honest structure is to name it at §1.2 and let the predicates measure *how much* of the member
   the exhibit does supply — which is the part that was not foreseeable and is the result.
2. **The quadratic reading is a disclosed choice, and the relay's bar is why it is not defended
   here.** I evaluate V011 D10 in its **local orthonormal frame**, which is the reading my 804
   exhibit used. The general-coframe form could give a different answer, and that difference is
   precisely 805/802's live question. **My I8 pass is therefore scoped to the orthonormal reading**
   and would need re-testing if 802 resolves the other way — stated now, so a later re-scoping is
   not read as a retraction.

*Direction check:* both bound my own result. The relay's positive product — that `a'`, 793's named
blocker, is supplied on both generators — is delivered inside a verdict that rejects my candidate.

---

```text
CANDIDATE = assembled (conversions displayed).  Cof(K) <- 753's derived frames (identity, same
   objects as 793's G6); Vol(K,C) <- the forced intrinsic Vol_4 (identity); a_K' and F_K' = d_1'a_K'
   <- solved exactly on BOTH generators and re-verified entrywise (A2: all 65 edges incl. the 33
   new diagonals; A1: all 216 edges, 116 nonzero on non-parent edges); Curr(K) <- NOTHING;
   R4Dens(K) <- NOTHING.  The candidate is a PARTIAL member by construction and is stated so before
   the predicates run.  Quadratic evaluated in V011 D10's LOCAL ORTHONORMAL frame — the 804 reading;
   802's general-coframe L question is NOT touched, per the relay.
PREDICATES = 3/9 pass (I4 functoriality: M^(h.g) = I_6 . I_6 = I_6, L_id = id proved at 795;
   I6 incidence intertwining: C S = I_6 exact, and the incidence half PROVED of record at Q-702;
   I8 exact-energy: children/parent = 1 exactly on A0, A1, A2 and composites, discharging 793's
   I8 BUILD FAILURE on the coframe side — the single fact used is sum_i Vol_4(C'_i) = Vol_4(C)).
   1/9 partial (I2 totality: coframe side TOTAL on A0 (1 x 1), A1 (16 x 1/16), A2 (24 x 1/24) and
   composites (384 x 1/384 = 1); receiver arrow data S_R, d_R absent).
   2/9 FAIL (I1 receiver acceptance; I5 conserved-current transport).
   3/9 unposeable (I3 density type, I7 coframe duality, I9 support/tau) — EVERY unposeable
   quantifies over the absent delta_K / d_R / tau_ker, and EVERY pass is on the
   coframe/curvature/measure data.  The split is clean and it is the finding.
VERDICT = NOT-THIS-CANDIDATE (rejecting predicate + reason).  I1 RECEIVER ACCEPTANCE: CDensRecv's
   object row demands delta_K in R4Dens(K) with Pos, Dual, VolNorm, CurrentDomain; the exhibit is a
   coframe/curvature object and supplies no density slot, so it is not an object row, let alone an
   inhabitant.  SECOND, INDEPENDENT REJECTION: I5, no S_R on Curr(K).
   RESIDUAL GAP NEWLY TYPED: 793 named JOINT_A1_A2_FIELD_EXT_MEMBER absent as a whole, with its
   blocker "a' on the new interior edges ... and the density member compatible with that choice".
   THE EXHIBIT SUPPLIES THE a', on both generators, verified.  Components now supplied: e_K',
   mu_K', a_K', F_K' (4 of 10), plus exact quadratic transport, incidence preservation, and
   identity/composition.  STILL ABSENT: f_g, F_g, s_g, S_g, delta_K', d_g (6 of 10) — ALL on the
   current / density / support side, which R4Dens's deliberate opacity makes a typing question
   rather than a computation this lane can run.  B1c inhabitance is still open but NO LONGER OPEN
   AT THE COFRAME LAYER; forcing is still gated, on a narrower gate.
B2_RUNNABLE = NO, with the reason CHANGED.  793: not runnable because the required B1 transport
   input does not exist.  NOW: a B1 coframe transport EXISTS (the identity law, total on A0/A1/A2
   and composites); B2 remains not runnable because its input is a receiver MEMBER and the receiver
   is uninhabited on its density and current rows.  Whether B2 in fact needs the density row is a
   scope question for the receiver's own lane; I do not decide it.
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+2): (1) I stated the candidate was PARTIAL before running the
   predicates — reading 793's object row makes the absence of delta_K immediate, and a tally that
   "discovered" it at predicate 9 would have dressed a foreseeable rejection as a finding; the
   predicates are there to measure HOW MUCH of the member the exhibit supplies, which is the part
   that was not foreseeable; (2) the quadratic reading is a DISCLOSED CHOICE — V011 D10's local
   orthonormal frame, the 804 reading — so my I8 pass is SCOPED to that reading and would need
   re-testing if 805/802 resolves the general-coframe question the other way; stated now so a later
   re-scoping is not read as a retraction.  Both bound my own result, and the positive product is
   delivered inside a verdict that rejects my own candidate.
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
