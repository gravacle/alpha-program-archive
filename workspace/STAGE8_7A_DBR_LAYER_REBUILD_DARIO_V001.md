# STAGE 8 / 7A / [PLAN:A1-CORRECTIVE] — THE PUBLIC LAYER REBUILT ON THE SEALED OPERATOR

Lane: DARIO (Builder B, independent verifier). Relay 781.
Governing: **Q-685** — the cross-check refuted 775's trace form and positivity bound.
**The refutation is ADOPTED in full.** Adopt-and-rebuild.
All headline statements below enter as **CLAIMED** (alignment law 3; cross-check follows).

## Lead determination — CLAIMED

**775's `+1` was never a convention. It was the identification my own 768 had already
withdrawn, and I used it twice afterwards.**

```text
768 §1.1(c), span [6410,6885), span sha 4b6102e985b7a722…  — verified byte-exact this relay:

  "**(c) The `+1` is not `Phi^dagger Phi`. ADOPTED.** ... I hedged it as a convention but
   still made the identification. **Withdrawn.**"
```

I wrote that withdrawal at 768, then wrote `λ = p² + λ_S2² + 1 + C2_parent` at 775 and carried
it again through 777. **The refutation was mine, the violation was mine, and two relays passed
between them.** That is now DECLINE REGISTER **D1**, and the flattening check exists because of it.

**What the rebuild yields, on the operator as sealed:**

```text
H_0 := D_(Sigma,A)^2 + Phi^dagger Phi + C2_parent          [768 span S1, verified]

TRACE          no unconditional scalar form exists.  Displayed as a FUNCTIONAL of the
               Phi-sector, with two named conditions (F) and (S) under which — and only
               under which — it collapses to a sum.
POSITIVITY     lambda >= C2_parent, unconditional over the admissible Phi-sector, and
               TIGHT: 778's witness attains it.
U-ITEMS        three survive, three become conditional, three die.
```

**And a "+1" does legitimately survive — in a different place, from a different source.** Member
A's `S²` ladder starts at `ell = 1`, so `ell(ell + 2·0) = ell² ≥ 1`. The `+1` that belongs to the
record is the **sphere-sector gap of the uncharged member**, not `Φ†Φ`. 775 had the right number
in the wrong term.

**A further correction to my own 777, found by carrying the refutation properly rather than
patching around it:** 777 claimed *"B's bottom sits exactly ONE unit below A's, for every spin
structure."* With `Φ†Φ` a genuine unselected operator it need not commute with `D²`, and
`min spec(X+Y) ≠ min spec X + min spec Y` for non-commuting positive operators (verified on an
explicit 2×2 pair). **What separates by exactly 1 unconditionally is the two BOUNDS. The two
BOTTOMS separate by 1 only under condition (S).** 777 asserted the bottoms.

---

## 0. Preflight

### 0.1 Output name
Probed recursively before any write: artifact and sidecar **ABSENT**.

### 0.2 Seals verified before use (`shasum -c` run from each file's own directory)

```text
fb7e8bd774069221…  relay_inbox/RELAY_PASTE_781_LAYER_REBUILD_DARIO_V001.md      OK  [before reading]
8dd82679328b51ad…  supervision/LOCKED_PROCESS.md                                OK  [alignment laws]
9913262a8f9104ff…  supervision/DECLINE_REGISTER_V001.md                         OK  [D1–D10]
63549f639b751247…  supervision/PROGRAM_STATE_BRIEF_V003.md                      OK  [law 4]
118469418a3d8951…  supervision/QUESTIONS_SETTLED_REGISTER_V001.md               OK  [law 5(a) grep]
54d2af923f1b32a5…  workspace/STAGE8_7A_PUBLIC_LAYER_CROSSCHECK_CODEX2_V001.md   OK  [778, adopted]
03db8d3da273f42c…  workspace/STAGE8_7A_TOWER_CONTEST_DARIO_V001.md              OK  [768, the operator]
da8720a43a9b4eda…  workspace/STAGE8_7A_DBR_FAMILY_BUILD_DARIO_V001.md           OK  [777, salvage subject]
083e86e357a63e0a…  workspace/STAGE8_7A_DBR_PUBLIC_LAYER_CAMPAIGN_DARIO_V001.md  OK  [775, refuted subject]
```

**Spans re-derived, not trusted.** I recomputed 768's two decisive span digests from the file
bytes and they reproduce 778's independently stated values:

```text
768 [6410,6885)   span sha 4b6102e985b7a722…   the express withdrawal of +1 = Phi^dagger Phi
768 [10764,11705) span sha d08cccc778b13b44…   the corrected H_0, multiplicity, and flat-x16 condition
```

### 0.3 Alignment law 4 — discharged, and a disclosure

**The relay names no `PROGRAM_STATE_BRIEF` version or digest.** Law 4 requires *"every relay
names the current PROGRAM_STATE_BRIEF version and digest as a required preflight read."* I
discharged the law by loading the highest existing version, **V003 = `63549f639b751247…`, sealed
OK**, and record the relay's omission as a process disclosure, not a defect of the task.

V003 also corrects the relay's own count: LOCKED_PROCESS carries **SIX** alignment laws, not
three. The sixth is **PE-POINTER-ONLY** — *"never restate PE content in mandatory reads"* — which
is my 777 custody finding made into law. **The finding is discharged of record; I do not re-raise
it.** PE-1..PE-6: recorded, not consulted, not opened this relay.

### 0.4 Law 5(a) — register grep

`QUESTIONS_SETTLED_REGISTER_V001.md` (1,391,345 B) grepped before task work. Q-683 (carry both
kinds), Q-685 (this refutation) and Q-686 (my 777: *"the family is built and it is COUNTABLE; U7
falls out of the core; the discrimination rule cannot be closed lane-side"*) are all present and
their outcomes are already in V003's state block.

**One probe returned zero and I record it as an open item rather than a settled one:**
`N_lattice` — **0 hits in the whole register.** 778's lattice-counting objection (§2.1.2: the
source writes `N_lattice(p_t,p_q)`; 775 suppressed it into `Σ_{p∈Λ}` with no multiset convention)
**is settled nowhere.** It is carried explicitly below.

### 0.5 Gates

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
No determinant evaluated.  No member evaluated alone (FAMILY-BEFORE-DETERMINANT).
No bundle class adopted OR eliminated.  No member binding; no fixed-point execution; no end
test; no numeric evaluation of physical quantities; no comparison to measured constants; no
common cell formed; no junction map evaluated; no smooth data derived.
Phi, C2_parent, p^2_min, N_lattice, the radii and beta remain SYMBOLS throughout.
No register, plan, tracker, git action.
```

---

## 1. AS1 — THE TRACE, CONDITIONAL — CLAIMED

### 1.1 The two conditions, named and quoted

**(F) — the flat-parent condition.** Verbatim from 768, span `[10764,11705)`, span sha
`d08cccc778b13b44…`:

> *"the ×16 is flat ONLY IF the flux U(1) is external to Spin(10) with flat parent connection"*

**(S) — the scalar-Φ condition.** *Not* in the record; **stated here as a condition, never as a
fact:** `Phi^dagger Phi = mu^2 · Id` with `mu^2 >= 0` constant on `Σ_BR` and
`[Phi^dagger Phi, D_(Sigma,A)^2] = 0`.

### 1.2 The trace as a functional of the Φ-sector — the only unconditional form

```text
Tr f(H_0)  =  Tr_{H_BR}  f( D_(Sigma,A)^2  +  Phi^dagger Phi  +  C2_parent )
```

[YOURS] **This is a functional, not a sum, and it does not reduce.** `Phi^dagger Phi` is a
positive-semidefinite operator over `Σ_BR`, not a number; `D_(Sigma,A)^2` differentiates. Nothing
in the record makes them commute, so there is no joint eigenbasis to sum over. **768's own status
line says as much:** *"NOT a scalar tower … Second-order and higher: Phi-dependent, unbounded
while Phi is unselected."*

### 1.3 First specialization — under (F) alone

```text
Tr f(H_0)  =  16 · Tr_{L2(Sigma_BR, S_Sigma)}  f( D_(Sigma,A)^2 + Phi^dagger Phi + C2(16) )
```

[YOURS] (F) lets the parent factor come out as a flat multiplicity and makes `C2_parent` the
scalar `C2(16)` on the irreducible chiral **16**. **It does not scalarize `Φ†Φ`.** The `Σ`-trace
remains a functional of the Φ-sector.

### 1.4 Second specialization — under (F) **and** (S)

```text
Tr f(H_0)  =  SUM_(p_t,p_q)  2·N_lattice(p_t,p_q)  ·  SUM_(ell>=0)  d_S2(ell)  ·  16
                 ·  f( p_t^2 + p_q^2 + ell(ell+2|q|) + mu^2 + C2_parent )

   d_S2(0) = 2|q| = |deg L| ;   d_S2(ell>=1) = 4(ell+|q|)          [768, CONFIRMED by 778]
```

[YOURS] **`N_lattice(p_t,p_q)` is carried explicitly and NOT absorbed into the sum.** 775 wrote
`Σ_{p∈Λ}` and supplied no multiset convention; 778 objected; the register settles it nowhere. The
constant `2 × 16 = 32` is exact arithmetic **under (F)** and is not uniform over the open family
without it.

### 1.5 The declined case, displayed as declined

```text
mu^2 = 1  ==>  Tr f(H_0) = SUM 2 N_lattice · SUM d_S2(ell) · 16 ·
                            f( p_t^2 + p_q^2 + ell(ell+2|q|) + 1 + C2_parent )

*** THIS IS 775's TRACE.  It is DECLINE-REGISTER D1 and it is displayed here ONLY as the
*** mu^2 = 1 member of the (S)-family, CONDITIONED-ON and never substituted.  No step of
*** this artifact consumes it.  It appears so the refuted object is visible in its correct
*** position — as one point of a parameter family the record has expressly declined to fix.
```

```text
TRACE = rebuilt conditional (functional of the Phi-sector).  No unconditional scalar
   trace appears anywhere in this artifact.
```

---

## 2. AS2 — POSITIVITY, HONEST — CLAIMED

### 2.1 The unconditional bound, and it is tight

[YOURS] All three summands of `H_0` are positive semidefinite: `D_(Sigma,A)^2` is the square of a
self-adjoint operator; `Phi^dagger Phi >= 0` by construction; `C2_parent` is a compact-group
Casimir, `>= 0`. Hence

```text
lambda  >=  inf spec(C2_parent)  >=  0                      [no condition at all]
lambda  >=  C2_parent                                       [parent fiber = irreducible 16]
```

**TIGHT — attained, not merely bounded.** 778's witness (`q = 1/2` so `d_S2(0) = 1` is occupied;
`ell = 0`; `p_t = p_q = 0`; `Phi = 0`) gives `lambda = 0 + 0 + 0 + C2_parent = C2_parent`.
**Nothing stronger than `lambda >= C2_parent` holds over the admissible Φ-sector**, and I record
that as a ceiling on what this layer can deliver, not as a step toward one.

Note the scoping: the second line needs only that the parent fiber is the irreducible **16**
(sealed by PRIN's rank-16 chiral carrier), which is a fact about the *representation*. It does
**not** need (F). (F) governs whether `×16` is a *flat multiplicity*, which is a different claim.

### 2.2 The member-wise refinement — unconditional in Φ

[YOURS] On a Riemannian product with product spin structure the summands split and commute,
`D_(Sigma,A)^2 = D_(T^2)^2 + D_(S^2,A)^2`, so `H_0 >= D_(T^2)^2 + D_(S^2,A)^2 + C2_parent` as an
operator inequality — valid for **every** admissible `Φ`, since `Φ†Φ >= 0`:

```text
member A (n = 0):   lowest OCCUPIED S^2 level is ell = 1  ->  lambda_A >= p2min + 1 + C2_parent
kind   B (n >= 1):  ell = 0 is occupied, contributes 0    ->  lambda_B >= p2min + 0 + C2_parent
```

**The `+1` here is the sphere-sector gap of the uncharged member.** It has nothing to do with
`Φ†Φ`, and it is exactly the term 775 duplicated.

### 2.3 The correction to my own 777

[YOURS] 777 wrote: *"B's bottom sits exactly ONE unit below A's, for every spin structure."*

```text
min spec(X + Y)  !=  min spec X + min spec Y   for non-commuting positive semidefinite X, Y.
Verified on an explicit pair:  min spec X = min spec Y = 0, [X,Y] != 0, min spec(X+Y) = 0.2929.

=> UNCONDITIONAL:  the two BOUNDS of §2.2 separate by exactly 1.
=> The two BOTTOMS separate by exactly 1 only under (S).
777 asserted the BOTTOMS.  CORRECTED: the separation is a statement about bounds, not bottoms,
unless Phi is scalar/commuting.
```

### 2.4 The conditional strengthening, and its exact condition

```text
under (S):            lambda  >=  p2min + [S^2-min]  +  mu^2  +  C2_parent
under (S), mu^2 = 1:  lambda  >=  p2min + [S^2-min]  +  1     +  C2_parent    *** D1, CONDITIONED-ON
   S^2-min = 1 for member A ; = 0 for kind B
```

775's `U5` is the second line with `p2min` set to `0` and `S^2-min` folded in — i.e. **two**
un-warranted moves stacked, one of them D1. Both are now displayed as conditions.

### 2.5 The `U`-items: what survives, what becomes conditional, what dies

| | verdict | basis |
|---|---|---|
| `U1` carrier and rank `4 × 16 = 64` | **SURVIVES** | rank is pointwise and twist-independent; PRIN's rank-16 chiral carrier is sealed. (F) governs flat *multiplicity*, not rank. 777 §3.3's carrier-identity SPEC GAP stands unchanged. |
| `U2` eigenvalue FORM with `+ 1` | **DIES** | the `+1` is D1. Replaced by the sealed form `spec = {p_t²+p_q²+ell(ell+2|q|)} + [Φ†Φ] + C2_parent`. |
| `U3` multiplicity `32 · d_S2 · N_lattice` | **CONDITIONAL** | `32 = 2×16` exact **under (F)** only (778); and `N_lattice` may not be suppressed — unsettled in the register. |
| `U4` `\|q\|` in exactly two affine places | **CONDITIONAL (scoped)** | CONFIRMED for the displayed `S²` law (778). **UNVERIFIABLE for `H_0`**: the parent embedding and the `Φ` action lie outside the two-slot census. |
| `U5` `lambda >= 1 + C2_parent` | **DIES** | REFUTED by 778's witness. Replaced by `lambda >= C2_parent`, tight. |
| `U6` bigrading; `T` bidegree (1,1), zero diagonal | **SURVIVES** | restated in the same sealed span S1 that carries the correction. Caveat retained verbatim: second order and higher is Φ-dependent and *unbounded while Φ is unselected*. |
| `U7` branch boundary at `ell = 0` | **DIES** | already fallen at 777 → `C6`; registered Q-686. |
| `U8` three beta weights | **CONDITIONAL** | the `beta^0` sector now contains `Φ†Φ`, whose scaling is unselected. The three-weight statement needs Φ's scaling declared. |
| `U9` five open elements + TYPE-R closures | **SURVIVES** | class-independent obstructions, untouched by the operator correction. |

```text
survive: U1, U6, U9   |   conditional: U3, U4, U8   |   dead: U2, U5, U7
```

---

## 3. AS3 — THE FAMILY, REBUILT — CLAIMED

### 3.1 Salvage from 777 (`da8720a43a9b4eda…`, seal verified) — item by item, nothing carried silently

| 777 item | disposition | why |
|---|---|---|
| family = `A ∪ {B_n}_{n>=1}`, countable | **SURVIVES** | registered Q-686; independent of the operator correction |
| `n := 2\|q\| = \|deg L\|`, integer-affine | **SURVIVES** | a statement about the `S²` law, which 778 CONFIRMS |
| member A validated at `q = 0` | **SURVIVES** | 778 reproduced `(1,1,4)(2,4,8)(3,9,12)(4,16,16)` exactly and independently |
| `S²` branch partition Z / P | **SURVIVES** | 778: *"BRANCH = CONFIRMED"* |
| `C5` branch cardinality fork | **SURVIVES** | 778: *"FORK_STRUCTURAL = CONFIRMED"* — for the `S²` carrier |
| `C4` bottom locations `+0` / `+1` | **DEMOTED to bounds** | 778: *"asserted full-`H_0` bottom values are not established."* §2.2 gives the bounds; the bottoms are not established |
| A–B separation of exactly 1 | **SURVIVES as a BOUND separation** | §2.3; the BOTTOM offset needs (S). **My own correction, not 778's** |
| intra-B variation (`B_1` vs `B_2`) | **SURVIVES in the weight `d_S2(0) = n`; CONDITIONAL in `32nN`** | `n` vs `2n` is (F)-free; the factor `32` and `N_lattice` are not |
| `U7 → C6` | **SURVIVES** | registered |
| six free choices `FC-a … FC-f` | **SURVIVE unchanged** | none was operator-dependent; `Φ` was already inside FC-e |
| four gaps `DG-1 … DG-4` | **SURVIVE; DG-1 WORSENS** | §4 |
| 777's `U5` attainment withdrawal | **SUPERSEDED, in my favour and then past it** | 777 withdrew *attainment*; 778 killed the *bound* |

### 3.2 The family on the corrected layer

Uniform core factored once — now **eight** items (`U7 → C6`), of which **three survive
unconditionally, three are conditional, two are dead** (`U2`, `U5`). Per-member instantiation:

| | **member A** (`n = 0`) | **kind B** (`n >= 1`) |
|---|---|---|
| `d_S2(0) = n` | `0` — label present, fiber empty | `n` — occupied, unpaired, one chirality |
| `d_S2(ell>=1)` | `4ell` | `4ell + 2n` |
| `S²` term `ell(ell+n)` | `ell²`, `ell >= 1` | `ell² + n·ell`, `ell >= 0` |
| **bound** (unconditional in Φ) | `lambda_A >= p2min + 1 + C2_parent` | `lambda_B >= p2min + 0 + C2_parent` |
| bottom | **NOT ESTABLISHED** (778) | **NOT ESTABLISHED** (778) |
| `C5` cardinality | 1 | 2 |
| `C6` branch boundary | absent | present |
| index | `0` | `±n` |

### 3.3 Core invariance re-verified on the CORRECTED core

[YOURS] Re-run over the eight items:

```text
U1  identical from both  — rank is pointwise, twist-independent.
U3  identical from both  AS A CONDITIONAL — condition (F) is a statement about the parent arm
    and carries no n-dependence, so it is common-mode: equally load-bearing on A and on B.
    (This is the 777 U3 correction applied to the whole item rather than one conjunct.)
U4  identical from both within its S^2 scope.
U6  identical from both — no step mentions n; and ∇_A Φ does not degenerate at n = 0.
U8  identical from both — the unselected Φ scaling is a shared datum.
U9  identical from both.
CORE_INVARIANCE on the corrected core = VERIFIED.  No NEW member-dependence appeared.
```

**The one item that broke invariance, `U7`, is already out of the core.** Nothing that survived
the operator correction picked up member-dependence during re-instantiation.

---

## 4. AS4 — THE RULE DRAFT, RE-CHECKED — **AMENDED** — CLAIMED

[YOURS] The 777 schema's structure survives; **one step does not survive as written.**

```text
R1, R2, R5, R6, R7          UNCHANGED.
FC-a … FC-f                 UNCHANGED — none was operator-dependent, and Phi was already
                            named inside FC-e as one of PRIN's unquantified axes.
DG-2, DG-3, DG-4            UNCHANGED.

R3  AMENDED.  Was: "Form zeta_m(0) symbolically in n."
    Cannot stand: zeta_m(0) = a_2[m] − dim ker_m, and the heat coefficient a_2 depends on the
    potential term Phi^dagger Phi.  On the corrected operator zeta_m(0) is NOT a function of n
    alone.
    Now:  "Form zeta_m(0) symbolically in n AND as a functional of the Phi-sector."

R4  CONSEQUENTLY CONDITIONAL.  The scheme-freeness gate can be run only once the Phi-sector is
    fixed or conditioned; until then the gate has no argument to test.

DG-1 WORSENS.  777 recorded that log det is transcendental in n, so R6 admits no finite
    coefficient check, while the GATE quantity zeta_m(0) does reduce finitely.  That
    consolation is now withdrawn too: zeta_m(0) is a functional of Phi, so even the gate does
    not reduce finitely until Phi is conditioned.
```

```text
RULE_DRAFT = AMENDED (displayed).  R3 restated; R4 conditional; DG-1 worsened.  The rule is
   NOT undecidable — its structure is intact and its holes were already named — but the
   Phi-sector is now load-bearing at the gate, where 777 had it load-bearing only at R6.
```

---

## 5. AS5 — FREEDOMS CONSUMED, AND THE FLATTENING CHECK

### 5.1 `FREEDOMS_CONSUMED` (alignment law 2 — an empty block would itself be a claim)

| free datum | tag | where |
|---|---|---|
| odd vacuum profile `Phi` | **CARRIED-AS-PARAMETER** (§1.2, §2.1–2.3) and **CONDITIONED-ON** (§1.4 via (S)) | never substituted |
| parent bundle and characteristic class | **CONDITIONED-ON** — condition (F), quoted verbatim | §1.1, §1.3, §1.4 |
| `C2_parent` numerical value | **CARRIED-AS-PARAMETER** — convention-carrying per 764 | §2 throughout |
| spin structure on `T2_TQ` (hence `p2min`) | **CARRIED-AS-PARAMETER** — symbolic in every bound | §2.2, §3.2 |
| radii `R_T, R_flux, R_Q` (hence `beta`) | **CARRIED-AS-PARAMETER** — unit-radius convention displayed, not adopted | §2.5 `U8` |
| bundle class / chiral index `n` | **CARRIED-AS-PARAMETER** — the family index; neither adopted nor eliminated | §3 |
| `N_lattice(p_t,p_q)` | **CARRIED-AS-PARAMETER** — explicit, not absorbed | §1.4 |

**SUBSTITUTED: none.** No decision-of-record is cited because none is needed.

### 5.2 `FLATTENING_CHECK` against `DECLINE_REGISTER_V001` D1–D10

```text
D1  Phi^dagger Phi = 1 ; unconditional x16      CLEAN — Phi carried as parameter; x16
                                                CONDITIONED-ON (F) with the condition quoted;
                                                mu^2 = 1 displayed ONLY as a declined member of
                                                the (S)-family (§1.5), consumed by no step.
D2  authoring flux quantization                 CLEAN — not touched.
D3  parent-arm monopole correspondence          CLEAN — not touched.
D4  re-proposing flux quantization              CLEAN — not touched.
D5  character lattice read as flux lattice      CLEAN — not touched.
D6  the D_BR bundle class (a selector)          CLEAN — carried as family; neither adopted nor
                                                eliminated.
D7  the public equivalence relation             CLEAN — remains ABSENT; FC-a unchanged; nothing
                                                authored in its place.
D8  the 19 Step-11 objects                      CLEAN — not touched.
D9  the five D_BR free data                     CLEAN — all five appear in §5.1, each tagged.
D10 comparison to measured constants            CLEAN — none.

FLATTENING_CHECK = clean.
```

---

## 6. GROUNDING, JURISDICTION, VERB AUDIT

### 6.1 Jurisdiction

**On adopting a refutation of my own two most recent artifacts.** *What was the rule written to
protect?* Adopt-and-rebuild exists so a lane cannot defend a result past its refutation. The risk
was live: 775's trace was the campaign's headline deliverable and 777 was built on it. *Does the
outcome space distinguish adoption from capitulation?* Yes — §3.1 salvages nine 777 items
explicitly and demotes three, and §2.2 recovers a genuine `+1` that the refutation does not touch.
*Would the evidence appear if 775 were right?* It would: the withdrawal would not be in 768's own
bytes. It is, and I verified the span myself rather than accepting 778's citation.

**On the VOID CONDITION.** No class adopted, preferred, or eliminated. The witness that kills
`U5` is 778's, on kind B; I neither adopt it nor use it to prefer A. Condition (S) is displayed as
a condition and consumed by no bound in §2.1–2.3.

**On BR-1.** The relay authorises the rebuild; it does not authorise its result. §2.3 is a
correction I generated against my own 777 that 778 did not ask for.

**On builder independence.** 778 is Codex 2's sealed *artifact*, lawful stock. No file under
`evaluator_build_A/` or `checks/` was read. `~/.codex` untouched; `memory-bank` never searched.

### 6.2 Self verb audit — **NOT CLEAN: four disclosures**

1. **I violated a decline I myself registered.** 768 §1.1(c) withdrew `+1 = Φ†Φ`; 775 substituted
   it anyway and 777 carried it. **Two relays between the withdrawal and its second use.** The
   failure was not missing the source — the source was my own artifact, and I had already adopted
   the correction once. *An adopted refutation does not propagate itself; nothing in my process
   re-checked downstream formulas against corrections I had already made.* That is what the
   flattening check now enforces, and it exists because of this.
2. **777's bottom-offset claim was too strong** — the bounds separate by 1 unconditionally, the
   bottoms only under (S). Self-caught this relay by testing non-commuting positive operators
   instead of reasoning about them.
3. **The relay named no state-brief version**, which law 4 requires; I discharged it by loading
   V003 and disclose that the discharge was mine, not the relay's. V003 also shows the law count
   is six, not the three the relay states.
4. **`N_lattice` is settled nowhere** (0 hits across a 1.39 MB register). 775 suppressed it, 778
   objected, and I record it as open rather than quietly restoring it as though the objection had
   been answered.

*Direction check:* every one of these runs against my own prior work, and none creates a result.
The pattern of record holds — **my reasoning survives contact; my propagation discipline is the
weak part.** 775 was refuted on a term I had already withdrawn. That is not a reasoning failure
and it is worse than one: it is a bookkeeping failure in a program whose entire value is custody.

---

```text
TRACE = rebuilt conditional (functional of the Phi-sector).  Unconditional form:
   Tr f(H_0) = Tr_{H_BR} f(D_(Sigma,A)^2 + Phi^dagger Phi + C2_parent) — a FUNCTIONAL, which
   does not reduce: Phi^dagger Phi is an unselected positive-semidefinite operator and nothing
   in the record makes it commute with D_(Sigma,A)^2.  Under (F) alone ["the x16 is flat ONLY
   IF the flux U(1) is external to Spin(10) with flat parent connection", 768 span
   [10764,11705), span sha d08cccc778b13b44…]: Tr f(H_0) = 16 · Tr_{L2(Sigma,S_Sigma)}
   f(D^2 + Phi^dagger Phi + C2(16)).  Under (F) AND (S) [Phi^dagger Phi = mu^2 Id, commuting —
   STATED AS A CONDITION, NOT A FACT]: Tr f(H_0) = SUM_(p_t,p_q) 2 N_lattice(p_t,p_q) ·
   SUM_(ell>=0) d_S2(ell) · 16 · f(p_t^2+p_q^2+ell(ell+2|q|)+mu^2+C2_parent), with N_lattice
   CARRIED EXPLICITLY and not absorbed (778's objection; 0 hits in the settled register).
   NO UNCONDITIONAL SCALAR TRACE APPEARS IN THIS ARTIFACT.  The mu^2 = 1 case — 775's trace,
   DECLINE-REGISTER D1 — is displayed only as one declined member of the (S)-family and is
   consumed by no step.
POSITIVITY_UNCONDITIONAL = lambda >= C2_parent  CLAIMED.  All three summands of H_0 are
   positive semidefinite; the bound needs only that the parent fiber is the irreducible 16
   (sealed), NOT condition (F).  It is TIGHT: 778's witness (q=1/2, ell=0, p_t=p_q=0, Phi=0)
   attains lambda = C2_parent, so nothing stronger holds over the admissible Phi-sector.
   Member-wise and still unconditional in Phi: lambda_A >= p2min + 1 + C2_parent and
   lambda_B >= p2min + 0 + C2_parent — and THAT "+1" is the sphere-sector gap of the uncharged
   member (ell >= 1 for n = 0), not Phi^dagger Phi.  775 had the right number in the wrong term.
POSITIVITY_CONDITIONAL = lambda >= p2min + [S^2-min] + mu^2 + C2_parent under (S), with
   S^2-min = 1 for member A and 0 for kind B  CLAIMED.  At mu^2 = 1 this is 775's U5 — D1,
   CONDITIONED-ON, never substituted.  775's U5 stacked TWO unwarranted moves: p2min set to 0,
   and the declined mu^2 = 1.
U_ITEMS = survive: U1, U6, U9 / conditional: U3 (32 = 2x16 only under (F); N_lattice may not be
   suppressed), U4 (CONFIRMED for the displayed S^2 law; UNVERIFIABLE for H_0 — the parent
   embedding and the Phi action lie outside the two-slot census), U8 (the beta^0 sector now
   contains Phi^dagger Phi, whose scaling is unselected) / dead: U2 (carried the D1 +1),
   U5 (refuted by 778's witness), U7 (fell at 777 -> C6, registered Q-686).
FAMILY = rebuilt (salvage displayed, twelve 777 items dispositioned individually, nothing
   carried silently).  SURVIVE: the countable family A ∪ {B_n}, the integer-affine
   reparametrisation n = 2|q| = |deg L|, member A's exact untwisted validation (independently
   reproduced by 778), the Z/P branch partition, the C5 cardinality fork, U7 -> C6, all six
   free choices FC-a..FC-f, and all four gaps DG-1..DG-4.  DEMOTED: C4's bottom locations
   become BOUNDS — 778 established that the full-H_0 bottoms are not established; the intra-B
   variation survives in the weight d_S2(0) = n but is CONDITIONAL in 32nN.  CORRECTED BY ME:
   777's "B's bottom sits exactly ONE unit below A's" holds for the two BOUNDS unconditionally
   but for the two BOTTOMS only under (S), since min spec(X+Y) != min spec X + min spec Y for
   non-commuting positive operators (verified on an explicit pair).  CORE_INVARIANCE on the
   corrected eight-item core = VERIFIED; no NEW member-dependence appeared, and condition (F)
   is common-mode across members.
RULE_DRAFT = amended (displayed).  R1, R2, R5, R6, R7 and FC-a..FC-f and DG-2..DG-4 unchanged.
   R3 amended — zeta_m(0) = a_2[m] − dim ker_m depends on Phi^dagger Phi through a_2, so it is
   NOT a function of n alone; it must be formed as a functional of the Phi-sector.  R4 is
   consequently conditional: the scheme-freeness gate has no argument to test until Phi is
   conditioned.  DG-1 WORSENS — 777's consolation was that the gate quantity zeta_m(0) at least
   reduced finitely in n; that is withdrawn, since it too is a functional of Phi.  The rule is
   not undecidable: its structure is intact and its holes were already named.
FREEDOMS_CONSUMED = Phi CARRIED-AS-PARAMETER and CONDITIONED-ON (never substituted) ; parent
   bundle and characteristic class CONDITIONED-ON via (F), quoted verbatim ; C2_parent value
   CARRIED-AS-PARAMETER ; spin structure on T2_TQ (hence p2min) CARRIED-AS-PARAMETER ; radii
   R_T, R_flux, R_Q (hence beta) CARRIED-AS-PARAMETER ; bundle class / chiral index n
   CARRIED-AS-PARAMETER ; N_lattice CARRIED-AS-PARAMETER.  SUBSTITUTED: NONE.
FLATTENING_CHECK = clean (D1–D10 walked individually; D1 is the live one and is discharged by
   carrying Phi as a parameter, conditioning the x16 on (F) with the condition quoted, and
   displaying mu^2 = 1 only as a declined member of the (S)-family that no step consumes).
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+4): (1) I VIOLATED A DECLINE I MYSELF REGISTERED — 768 §1.1(c)
   withdrew "+1 = Phi^dagger Phi" and I verified that span byte-exact this relay; 775
   substituted it anyway and 777 carried it, two relays after my own withdrawal.  An adopted
   refutation does not propagate itself, and nothing in my process re-checked downstream
   formulas against corrections I had already made; (2) 777's bottom-offset claim was too
   strong — bounds, not bottoms — self-caught this relay by testing non-commuting operators
   rather than reasoning about them; (3) the relay named no PROGRAM_STATE_BRIEF version, which
   alignment law 4 requires, and I discharged it myself with V003 (which also shows the law
   count is SIX, not the three the relay states); (4) N_lattice is settled nowhere (0 hits in a
   1.39 MB register) and I record it open rather than quietly restoring it.
   Every one runs against my own prior work and none creates a result.
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
