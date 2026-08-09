# STAGE 8 / 7A / [PLAN:B1a-8] — THE NO-GO IS REFUTED BY EXHIBIT: THE IDENTITY LAW SOLVES THE SYSTEM

Lane: DARIO (Builder B, independent verifier). Relay 804.
State brief pinned: `PROGRAM_STATE_BRIEF_V005.md` = `e26f0d16055f3e83…` — digest matches, seal OK.
Subject: **STAGE8_B1A_FULL_SPACE_SOLVE_CODEX2_V001.md** = `520a3fa2391be887…`, `.md.seal` **OK**
(law 8: both spellings probed). Sealed packet V011 `aa7c6d49…` used exclusively.
**This relay is the last gate before a parked principal ruling.**

## Lead determination — CLAIMED

```text
CERTIFICATE = REFUTED, by an explicit exact exhibit.
```

**The system the no-go declares UNSATISFIABLE has a solution, and it is the most ordinary point in
the 864-parameter space: the identity law on every child, with the constant-form lift.**

Verified by me, in exact rationals, from a receiver I built myself:

```text
S   = the lift of a constant coordinate 2-form F        (curvature-NONZERO: verified)
M_p = I_6  for all 24 Freudenthal children

(1)  the constant-form refined curvature IS globally integrable — I solved d_1' a = xi exactly
     and re-verified d_1' a == xi entry by entry;
(2)  for ALL 24 children, 2 x (frame-face flux) = (E_p F E_p^T)_(ab) EXACTLY, so pulling the
     bivector through wedge^2(E_p)^-1 per V011's own rule returns the coordinate components,
     i.e. M_p = I_6;
(3)  (III) (1/24) sum_p M_p^T M_p = (1/24)(24 I_6) = I_6                        EXACT;
(4)  (II) C S = I_6 — the constant form aggregates back to itself on all six components  EXACT;
(5)  (I) M - L S = 0 holds by the construction of M_p in (2).
```

**A single exact solution refutes UNSATISFIABLE regardless of how the certificate was computed.**
I do not need to locate the subject's error to report this, and I do not claim to have located it.

**And the exhibit is not new to the record.** It is candidate `(a2)` component-inheritance from my
own sealed **795**, where I verified it preserves the intrinsic-`Vol_4` quadratic exactly —
`children/parent = 1.000000` on every trial. **The no-go contradicts a cross-checked prior result
of record**, and the structural reason is elementary:

> A subdivision carrying a **constant** form preserves an **additive** quadratic, because `Vol_4`
> is additive over the partition and the form is unchanged. Any posing that forbids this has
> mis-stated one of its maps.

**What IS faithful in the subject.** All **nine** structural counts reproduce exactly under my
independent rebuild, and its displayed rationals are internally consistent to the last digit:

```text
dim H 50 | rank(L on H) 50 | rank C 6 | dim ker C 44 | section dim 264
law params 864 | lift entries 300 | variables 1164 | equations 921        9/9 MATCH
G_0 displayed matrix -> F_*^T G_0 F_* = 1058658/368613 = 352886/122871    self-consistent
352886/122871 - 2 = 107144/122871                                        self-consistent
```

**The defect is localized to `L`.** My rebuild gives `F_*^T G_0 F_* = 11/56`, excess `−101/56 < 0`.
The two `G_0` matrices share the sign pattern and the exact zero positions `(0,5),(1,4),(2,3)`, but
the diagonal and off-diagonal ratios differ (≈8.69 vs ≈30.43), so **it is not a normalization**. A
commissioned sweep of ~100 exact convention combinations — `L` scaled, `L` through
`wedge^2(E_p)^{±1}`, all-10-faces, `|det E_p|` weighting, `C` as sum / average / single square,
both orientations — **reproduced the subject's number under none of them.**

```text
CONSEQUENCE FOR THE PARKED RULING: its premise is false.  The ruling asks whether to accept a
no-go or authorize a revision; there is no no-go to accept.  IT MUST NOT PROCEED AS POSED.
```

---

## 1. AS1 — SYSTEM AUDIT

### 1.1 Counts: faithful, 9 of 9

Rebuilt from scratch — vertices `{0,1}^4`, edges = comparable pairs, triangles = chains,
`d_1' a(u,v,w) = a(u,v)+a(v,w)−a(u,w)`, `H = im(d_1')` via the pivot **columns of `d_1'`**:

| quantity | subject | mine | |
|---|---:|---:|:--:|
| curvature quotient `dim H` | 50 | 50 | ✓ |
| `rank(L on H)` (full column rank) | 50 | 50 | ✓ |
| `rank C` | 6 | 6 | ✓ |
| `dim ker C` | 44 | 44 | ✓ |
| linear section dimension `6·44` | 264 | 264 | ✓ |
| law parameters `24·36` | 864 | 864 | ✓ |
| lift entries `50·6` | 300 | 300 | ✓ |
| variables | 1164 | 1164 | ✓ |
| equations `864+36+21` | 921 | 921 | ✓ |

**The gauge quotient at 300 is confirmed**: the 50 coordinates are already the quotient of the
65-edge presentation by the 15-dimensional vertex-gauge kernel, `65 − 15 = 50`, and `50 × 6 = 300`.

### 1.2 The intrinsic quadratic's sealed form — the "killer" — is faithfully transcribed

`(III) (1/24) M^T M = I_6` is exactly the sealed requirement as I derived it independently at
**795**: with `Vol_4(C'_i) = 1/24` and `Vol_4(C) = 1`, preservation for all `F` is
`(1/24) Σ_i M_i^T M_i = I_6`. **Nothing is added, dropped, or strengthened here.** The subject
transcribes the constraint correctly.

**And that is what makes the verdict impossible**: `M_i = I_6` satisfies it identically.

### 1.3 The defect — `L` is underspecified in the text, and cannot be any lawful reading

The subject describes `L` only as *"the derived frames give an exact rational, full-column-rank map
`L : H → Q^(24·6)` which converts a global compatible refined curvature to its six local components
on every child."* It never states the normalization: raw flux, doubled flux, or bivector pulled
through `wedge^2(e^{-1})`, and with or without `|det e|`.

```text
DEFECT, DISPLAYED:
   (a) the certificate is NOT REPRODUCIBLE from the artifact's own text — L and C are prose,
       and different lawful readings give different G_0;
   (b) whatever L was used, it is NOT a lawful reading, because under EVERY lawful reading the
       identity law M_p = I_6 is a solution (section 0), and the subject's system forbids it.
```

---

## 2. AS2 — CERTIFICATE CHECK

### 2.1 The linear block: confirmed

The 264-dimensional curvature-nonzero affine section space is confirmed exactly from my own basis:
`dim ker C = 44`, `6 × 44 = 264`, and the sections are curvature-nonzero.

### 2.2 The Gram completion: NOT reproduced

```text
mine     F_*^T G_0 F_* = 11/56          excess = -101/56  < 0   (would be FEASIBLE)
subject  F_*^T G_0 F_* = 352886/122871  excess = +107144/122871 > 0
```

Both `G_0` lie in the `S_4`-invariant family `a·I + b·K` forced by the Freudenthal symmetry, with
the same `K` and the same zeros. The **scale-invariant fingerprint** — the ratio of the two block
eigenvalues, invariant under every rescaling of `L` or `C` — is `7/12` for mine and `40957/1677 ≈
24.42` for the subject. **No scaling, orientation, frame-conversion or aggregation convention
bridges them**; the connecting factor is not a rational square.

### 2.3 The exhibit — which settles it without needing their `L`

Section 0's five exact checks. **Refuting a universal negative requires one witness, and the
witness is verified.** I state plainly that this does **not** identify the subject's error.

---

## 3. AS3 — SCOPE AUDIT

```text
SCOPE = corrected (displayed).
   The subject's scope — "the declared full linear law class on these generators" — is the right
   class to have quantified over, and it does cover all 864 parameters.  But the VERDICT on that
   class is wrong: the class is NON-EMPTY, and the identity law is in it.
   So "closed as UNSATISFIABLE on the declared full linear coframe-law class" is withdrawn, and
   with it "JOINT_A1_A2_FIELD_EXT_MEMBER is impossible" and "B2 is not runnable", both of which
   are inferences from the empty verdict.
NONLINEAR_BEARING = none sealed.
   Nothing in the seven atomic constraints restricts or excludes nonlinear law classes; the
   quadratic (III) constrains the law's Gram, not its linearity.  The question is now MOOT for the
   parked ruling's option (ii): no broader class need be authorized to escape an obstruction that
   is not there.
```

---

## 4. AS4 — THE OBSTRUCTION READING

```text
EXCESS_STABILITY = not lawfully computable — and moot.
   The positive excess 107144/122871 is an artifact of the L actually used, not a property of the
   record's constraints: under lawful readings the excess is NEGATIVE (mine: -101/56) and the
   system is satisfiable.  Testing whether an artifact is "stable across generators" would grant
   it the status of a structure.  I decline to compute it and say why, rather than return a number
   that would read as obstruction-shaped evidence.
   Zero-weight note, structure only: an obstruction that vanishes under the identity law was never
   obstruction-shaped to begin with.
```

---

## 5. FREEDOMS CONSUMED, FLATTENING CHECK

| datum | tag |
|---|---|
| the `F'/F` law / all 864 `M_p` entries | **NOT ADOPTED** — the exhibit displays one point to refute a universal negative; it is not proposed as the law |
| the lift `S` | **CARRIED AS VARIABLE**; the constant-form lift is exhibited, not selected |
| parent two-form `F` | **CARRIED SYMBOLICALLY** — the exhibit holds for a generic rational `F`, not one value |
| child frames `E_p`, orientations | **CARRIED AS DERIVED** (753) |
| intrinsic `Vol_4` | **CARRIED AS FORCED/CLASSIFIED** — no compensator |
| vertex gauge | **QUOTIENTED**, not fixed |
| `C`'s aggregation convention | **CARRIED AS A STATED CHOICE** — the `1/4` average, pinned by requiring `C ∘ (constant-form lift) = I_6`; disclosed, not hidden |
| `L`'s normalization | **CARRIED AS A STATED CHOICE** — `2 ×` flux through `wedge^2(E_p)^{-1}`, per V011's own general-coframe rule |
| A2 representative | Freudenthal, as the subject's own generator; **no cellulation adopted or eliminated** |
| metric / counting inner product | **NOT ADOPTED** — `G` is the sealed quadratic pulled through derived frames |
| scaling weights (law 2a) | **NONE CONSUMED** |
| smooth constituent | **NOT CONSUMED; BARRED (S26)** |

**SUBSTITUTED: none.**

```text
FLATTENING_CHECK = clean (37 rows walked).  S26 clean — no smooth C_ref import; the packet clause
is a constraint only.  S08 clean — finite cochains and bivector coordinates are not identified
with electromagnetism or a smooth public field.  S28 clean — nothing selected by desired outcome;
the exhibit is a refutation witness, not a chosen member.  S01-S07, S09-S27, S29-S37 untouched.
```

---

## 6. JURISDICTION AND VERB AUDIT

**Jurisdiction.** *What was the rule written to protect?* Builder-never-verifies, with a principal
ruling parked behind it. The risk was live in **both** directions: confirming a false no-go would
terminate a route wrongly; refuting a true one on my own bug would block a sound ruling. *Does the
outcome space distinguish?* Yes — I confirmed 9/9 counts and the subject's internal arithmetic
before dissenting, and the dissent rests on an **exhibit** rather than on reproducing their number.
*Would evidence look different if the no-go were right?* Yes: the identity law would fail one of
the three constraints. It fails none.

**VOID CONDITION.** No law adopted. The exhibit is displayed to refute a universal claim, which is
the one use of a specific point that is not a selection.

### 6.1 Self verb audit — **NOT CLEAN: three disclosures**

1. **My first rebuild carried an instrument bug and I nearly reported a false divergence on it.**
   I extracted the basis of `im(d_1')` from the pivots of the *transpose*, using triangle indices
   as edge indices; that gave `rank(L on H) = 42` and a singular `G`, and I was one step from
   reporting the subject's "full column rank 50" as a defect. **A sanity check I had built in —
   reading the identity on all 110 triangles, which must return `dim H` — caught it.** Without
   that control the relay would have blocked a ruling on my own error.
2. **I did not locate the subject's error and do not claim to.** The refutation is by exhibit. The
   fingerprint analysis narrows where the difference lives (`L`'s anisotropy between the two
   isotypic blocks, ~24:1 where lawful readings give ~0.5–2.3) but naming a mechanism would be
   speculation, and I leave it to the subject's own lane.
3. **The exhibit was already in the record, in my own sealed 795, and I did not connect it when I
   read the no-go.** 795 displayed `(a2)` component-inheritance as surviving the quadratic exactly.
   The no-go's conclusion contradicts it directly. **I read the subject's argument on its own terms
   for a full pass before recalling that I had already verified its negation.** That is the same
   under-reading of my own corpus that Q-704 made a standing lesson, and this is its third
   appearance in the arc.

*Direction check:* 1 and 3 run against me. The finding that most flatters this relay — refuting the
other lane — is delivered only after confirming 9/9 of their counts and their arithmetic, and with
an explicit statement that I have not found their bug.

---

```text
SYSTEM_AUDIT = DEFECT (displayed).  All NINE structural counts are faithful and reproduce exactly
   (dim H 50; rank(L on H) 50; rank C 6; dim ker C 44; section dim 264; law params 864; lift
   entries 300; variables 1164; equations 921), the gauge quotient at 300 is confirmed (65 - 15 =
   50, times 6), and the intrinsic quadratic (III) (1/24) M^T M = I_6 is transcribed exactly as
   795 derived it — nothing added, dropped, or strengthened.  THE DEFECT IS IN L: the artifact
   specifies it only in prose ("converts a global compatible refined curvature to its six local
   components"), never stating the normalization, so (a) THE CERTIFICATE IS NOT REPRODUCIBLE FROM
   THE ARTIFACT'S OWN TEXT, and (b) whatever L was used cannot be a lawful reading, because under
   every lawful reading the identity law is a solution.
CERTIFICATE = REFUTED (exhibit).  S = the lift of a constant coordinate 2-form F, M_p = I_6 on all
   24 Freudenthal children, verified by me in exact rationals: the constant-form refined curvature
   IS globally integrable (d_1' a = xi solved and re-verified entrywise); for ALL 24 children
   2 x (frame-face flux) = (E_p F E_p^T)_(ab) exactly, so pulling through wedge^2(E_p)^-1 per
   V011's own rule gives M_p = I_6; (III) (1/24) sum_p M_p^T M_p = I_6 EXACT; (II) C S = I_6 EXACT
   on all six components; (I) holds by construction; and S is curvature-NONZERO.  A single exact
   solution refutes UNSATISFIABLE however the certificate was computed.  THE EXHIBIT IS NOT NEW:
   it is candidate (a2) component-inheritance from my own sealed 795, where it preserved the
   intrinsic-Vol_4 quadratic exactly (children/parent = 1.000000 every trial), so the no-go
   contradicts a cross-checked prior result of record.  Structural reason: a subdivision carrying a
   CONSTANT form preserves an ADDITIVE quadratic, because Vol_4 is additive over the partition and
   the form is unchanged.
   NOT CLAIMED: I did not locate the subject's error.  Its displayed matrix, certificate value and
   excess are internally consistent to the last digit (1058658/368613 = 352886/122871; minus 2 =
   107144/122871).  My rebuild gives 11/56 with excess -101/56 < 0; the two G_0 share the sign
   pattern and the zeros (0,5),(1,4),(2,3) but differ in the diagonal/off-diagonal ratio (8.69 vs
   30.43), so it is NOT a normalization, and a commissioned sweep of ~100 exact convention
   combinations (L scaled, L through wedge^2(E_p)^{+/-1}, all-10-faces, |det E_p| weighting, C as
   sum / average / single square, both orientations) reproduced the subject's number under NONE.
SCOPE = corrected (displayed).  The declared full linear law class is the right class and does
   cover all 864 parameters, but the verdict on it is wrong: THE CLASS IS NON-EMPTY.  Withdrawn
   with it: "B1a closed as UNSATISFIABLE", "JOINT_A1_A2_FIELD_EXT_MEMBER impossible", and "B2 not
   runnable" — all inferences from the empty verdict.
NONLINEAR_BEARING = none sealed.  Nothing in the seven atomic constraints restricts or excludes
   nonlinear law classes; (III) constrains the law's Gram, not its linearity.  MOOT for the parked
   ruling's option (ii): no broader class need be authorized to escape an obstruction that is not
   there.
EXCESS_STABILITY = not lawfully computable — and moot.  The positive excess 107144/122871 is an
   artifact of the L actually used, not a property of the record's constraints; under lawful
   readings the excess is NEGATIVE.  Computing its "stability across generators" would grant an
   artifact the status of a structure, so I decline and say why.  Zero-weight note, structure only:
   an obstruction that vanishes under the identity law was never obstruction-shaped.
CONSEQUENCE FOR THE PARKED RULING: its premise is false.  It asks whether to accept a finite no-go
   or authorize a revision; THERE IS NO NO-GO TO ACCEPT.  The ruling must not proceed as posed.
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+3): (1) MY FIRST REBUILD CARRIED AN INSTRUMENT BUG and I was one step
   from reporting a false divergence — I extracted the basis of im(d_1') from the pivots of the
   TRANSPOSE, using triangle indices as edge indices, giving rank(L on H) = 42 and a singular G;
   a built-in sanity control (the identity reading on all 110 triangles, which must return dim H)
   caught it, and without that control this relay would have blocked a ruling on my own error;
   (2) I DID NOT LOCATE THE SUBJECT'S ERROR and do not claim to — the refutation is by exhibit, and
   naming a mechanism would be speculation; (3) THE EXHIBIT WAS ALREADY IN THE RECORD, in my own
   sealed 795, and I read the no-go on its own terms for a full pass before recalling that I had
   already verified its negation — the same under-reading of my own corpus that Q-704 made a
   standing lesson, third appearance in this arc.
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
