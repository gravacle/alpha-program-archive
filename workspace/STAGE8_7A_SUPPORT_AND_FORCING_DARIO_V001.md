# STAGE 8 / 7A / STEP 8 — THE SUPPORT TRANSPORT, AND THE RECONCILIATION FORCING CHECK

Lane: DARIO (Builder B, independent verifier). Relay 755.
Governing: my 751 board `4d072e76…`; my 753 result `d6f490b8…`.

## Lead determination

**AG2 is FORCED — and the reason corrects my own 753. There was never a conflict.**

753 reported *"a conflict between two sealed authorities"* — `V011`'s clause giving `|det e| =
1` on an `A2` child against `R33` + `MAJ` giving `1/24`. **That framing is wrong on both
halves.**

- **`V011` is silent, not opposed.** Its sentence reads *"For a **general coframe** `theta^a =
  e^a_mu dx^mu`, the same map is defined by…"*. That generalizes the **coframe**, not the cell
  shape. The cells it governs are parallelepipeds throughout — and for a parallelepiped
  `|det e| = V_cell` **exactly**, arbitrary frame included. The clause never quantified over
  simplices, so it never asserted `1` was their volume.
- **The measure is already classified, uniquely, and I had never opened the file.**
  `R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001` `e4cfaef1…`, packet-sealed, verdict
  `GLOBAL_INTRINSIC_FLAT_CELL_MEASURE_CLASSIFIED`: *"the intrinsic probability measure on a flat
  primitive causal diamond is **uniquely** `mu_D(A) = Vol_4(A)/Vol_4(D)`"* — with an executed
  exact audit behind it.

So `|det e|` and `1/24` are **two evaluations of the same sealed measure** `Vol_4`, on a
parallelepiped and on an order-simplex. The `4!` is the simplex-to-parallelepiped ratio, not a
disagreement. **The one-line statement is FORCED, with zero physics choice**, and its exact
content is displayed at §2.5 for A to author.

**AG1 names the unsealed element precisely — and it is not what I guessed at 751.** I called
support *"structurally immediate, unsealed"*, thinking of set-theoretic cochain support. Its
sealed definition is nothing of the kind: the **Causal Incidence Support Principle**
(`b0c636f3…`, adopted Level-1, sealed, packet member) fixes `support(L_c) is contained in
Omega_c` — the support of an **interaction density** inside a **Lorentz-covariant causal
cell** — and its transport law is **indexed by the exhaustion**, not by refinement: *"Once the
**future boundary** has crossed the closure face of `Omega_c`…"*. Growing volume, not
subdivision.

**So support is not "immediate and unsealed"; it is indexed to a different index** — the same
exhaustion-vs-refinement gap carried since `IDX` §3.3.

---

## 0. Preflight

### 0.1 Output name

Probed **before any write**, recursively: **absent**, artifact and sidecar both.

### 0.2 Sources verified before use

```text
CIS    workspace/CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md              b0c636f3…  SEALED-OK
R33G   workspace/R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md  e4cfaef1…
R33    workspace/R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_RESULT_V001.md   e60aec3c…
V011   workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/
         BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md                   aa7c6d49…
MAJ    workspace/stage8_execution/work/MAJORANT_PHASE2_O3_O7_PROOF_DRAFT_V001.md  08b91543…
D012   workspace/STAGE8_TASK6_A25_A27_SCOPING_LANE2_V003.md              74bbb7aa…
C1B    workspace/STAGE8_TASK5_EQ6_C1_COMPLETION_BUILD_LANE1_V001.md      5203347c…
751    workspace/STAGE8_7A_RA27_3_FRONTIER_DARIO_V001.md                 4d072e76…
753    workspace/STAGE8_7A_SIMPLICIAL_COFRAME_DARIO_V001.md              d6f490b8…
```

**Seal provenance, stated precisely.** `CIS` carries an adjacent sidecar (`shasum -c` OK, run
from its own directory). `R33G`, `R33` and `V011` carry **no adjacent sidecar**; all three are
sealed by membership in `review_packets/STAGE7_QSPEC_CANDIDATE_V001/STAGE7_PACKET_MANIFEST_V001.sha256`
— I grepped the manifest for `e4cfaef1`, `e60aec3c` and `aa7c6d49` and each is listed, rather
than assuming a sidecar.

**Searched space for every negative claim:** recursive glob `./workspace/**/*.md` +
`./supervision/**/*.md` — **1,978 files** — `*_DARIO_V001.md` excluded, `evaluator_build_A/`
code excluded. **Run from the archive root**, with known-positive controls — see §3.3
disclosure 1.

### 0.3 Gates

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
No member binding.  No fixed-point execution.  No end test.  No numeric evaluation of
physical quantities.  No comparison to measured constants.  No common cell formed.
No junction map evaluated.  No smooth data derived.  Nothing adopted.
No register, plan, tracker, or git action.
```

---

## 1. AG1 — THE SUPPORT FIELD

### 1.1 Support's sealed definition

[PROVABLE] `CIS` `b0c636f3…[527,755)` — *"an adopted Level-1 Gravacle microscopic-action
principle … frozen before construction or evaluation of the causal parent that uses it"*:

```text
For every primitive record-forming incidence `c`, the complete microscopic
parent assigns one Lorentz-covariant causal cell `Omega_c` and one interaction
density `L_c` such that

support(L_c) is contained in Omega_c.
```

**Support is the support of an interaction density, and the law is a containment in a causal
cell.** It is not the set-theoretic support of a cochain, which is what I assumed at 751
without opening this file.

### 1.2 Its sealed law is indexed by the exhaustion, not by refinement

[PROVABLE] `CIS` `b0c636f3…[818,1091)`:

```text
Once the future boundary has crossed the closure face of `Omega_c`, the same
primitive incidence is absent from the active generator. A physical exhaustion
adds new future incidences on new record factors; it does not reapply a
completed incidence to its old record factor.
```

[YOURS] **That is a growing-volume law.** The quantity that moves is the **future boundary**;
the operation is a **physical exhaustion** adding new incidences on new record factors. Nothing
in it concerns subdividing an existing `Omega_c` and asking where `support(L_c)` goes. The
principle governs the support field along the *exhaustion* index. RA27-3 demands transports
along the *refinement* index.

### 1.3 The negative, probed by meaning

[PROVABLE] Over the 1,978-file searched space, pairing support with refinement in both
orderings within 60 characters yields **37 distinct contexts**. I read them. **None is a
transport law.** They are audit checklist items (*"support/restriction square +
common-refinement diamond"*), demands (*"the antecedent and restriction maps use actual …
supports, bundles, and surface refinements"*), and register entries.

[PROVABLE] **The closest thing to the object is inside a STOPPED residue.** `C1B`
`5203347c…[13728,14058)`:

```text
EXACT_RESIDUE =
  a target-blind bounded-geometry certificate controlling path length,
  mesh scale/shape, cell volume/coframe condition, support overlap,
  distribution order, and refinement density across every primitive orbit;
  plus a positive covariant W5 proved to generate that same topology.
```

immediately preceded in that file by `S2_GLOBAL_ATTAINMENT = STOPPED` and `S2_W5 = STOPPED`.
So **support-behaviour-under-refinement is named of record — as content of a certificate the
corpus records as not built.**

### 1.4 The unsealed element, named precisely

```text
UNSEALED: the behaviour of `support(L_c) ⊆ Omega_c` when `Omega_c` is
SUBDIVIDED.  The sealed principle supplies containment plus a reuse law
indexed by the FUTURE BOUNDARY (exhaustion).  It supplies no rule for the
refinement index, and the object that would — a bounded-geometry certificate
controlling support overlap and refinement density — is recorded STOPPED.
```

[YOURS] **Not derivable here, and the reason is not shyness.** A transport would require
knowing whether `Omega_c` is a cell of the cellulation being refined at all — the principle
never identifies the causal cell `Omega_c` with a cell of the record complex, and I found no
sealed text that does. Deriving the transport would first require *authoring* that
identification, which is a typing act, not a verification.

```text
SUPPORT = unsealed element named.
```

### 1.5 The correction to 751

[YOURS] 751 §2.3 said support is *"structurally immediate, unsealed"* and offered a one-line
set-theoretic argument I declined to write into the record. **The first half was wrong.**
Support is an interaction-density support in a causal cell under an exhaustion-indexed reuse
law; the one-liner I had in mind was about a different object. Declining to write it was right
for the wrong reason — and had I written it, it would have been a false transport for a field
whose sealed definition I had not read.

---

## 2. AG2 — THE RECONCILIATION FORCING CHECK

### 2.1 (i) Is `V011`'s clause limited to boxes — silent, or in conflict?

[PROVABLE] The full passage, `V011` `aa7c6d49…[45718,46387)`, in its own order:

```text
For an orthogonal physical cell with edge lengths `ell_mu`, volume
    V_cell = product_mu ell_mu, …
Therefore each cell contributes  V_cell sum_(mu<nu) F_(mu nu)^2  in the local
orthonormal frame. For a general coframe `theta^a=e^a_mu dx^mu`, the same map
is defined by pulling the bivector through `wedge^2(e^(-1))` and multiplying
by `|det e|`.
```

[YOURS] **The generalization is over the COFRAME, not over the cell shape.** The sentence's own
quantifier is *"For a general coframe `theta^a = e^a_mu dx^mu`"* — it relaxes `e = diag(ell)` to
a general `e^a_mu`, i.e. it admits **non-orthogonal frames**. It does not admit non-parallelepiped
**cells**. And on the class it does quantify over — a cell that is the frame's parallelepiped —
`|det e| = V_cell` remains **exact**, arbitrary frame included.

[PROVABLE] **Corroborating the silence:** across the 1,978-file space, `simplicial cell`
returns **1** and `parallelepiped` returns **1**, both in the register and both downstream of
my own 753. The corpus does not discuss simplicial cell volumes anywhere else.

```text
(i) VERDICT: the clause is SILENT on simplices.  It is not in conflict with
    anything, because it never quantified over them.
```

### 2.2 (ii) Do `R33` + `MAJ` force intrinsic four-volume — and is it already classified?

[PROVABLE] `R33` `e60aec3c…[551,740)`, executed, packet-sealed, bound to row A27: *"a subregion
promoted to an elementary cell must be evaluated by **that child's intrinsic cell measure**. It
may not retain a weighting profile defined by an arbitrarily chosen parent."*

[PROVABLE] `D012` itself types `R33` in its own manifest row: *"intrinsic cell measure | packet
`R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_RESULT_V001.md` | `e60aec3c…` | **flat-cell measure
selector; naturality inherited**."* A simplex is a flat cell; the selector applies.

[PROVABLE] **And the measure itself is classified — uniquely.** `R33G` `e4cfaef1…[98,309)`:

```text
GLOBAL_INTRINSIC_FLAT_CELL_MEASURE_CLASSIFIED

Within the predeclared class A1-A4, the intrinsic probability measure on a
flat primitive causal diamond is uniquely

    mu_D(A) = Vol_4(A) / Vol_4(D).
```

with an **executed** audit behind it — Lorentz generator count 6, fixed-covector constraint
rank 4, nullity 0, generator span rank 6, commutator span rank 6 — i.e. the uniqueness is
proved by exhausting the covariance characters, not asserted.

[YOURS] **So the intrinsic cell measure IS four-volume, uniquely, of record.** `R33` says use
the child's intrinsic measure; `R33G` says that measure is uniquely `Vol_4`; `MAJ` evaluates it
on the order-simplex at `1/24`; `V011` evaluates it on a parallelepiped at `|det e|`. **One
measure, several evaluations. No choice anywhere.**

```text
(ii) VERDICT: FORCED — and stronger than forced, since the general volume
     factor is already CLASSIFIED, not merely determined.
```

### 2.3 (iii) Any other sealed require bearing

[PROVABLE] Probed by meaning across the searched space. The one require that could cut against
is `V011`'s bar — *"The inverse weight `ell_mu^2 ell_nu^2/V_cell`, an inserted compensator, or
any residual shape-dependent scalar fails A27."*

[YOURS] **It does not bite.** The bar is on **inserted compensators** and **residual
shape-dependent scalars** *in the coefficient*. Evaluating `Vol_4` on the actual cell is not an
inserted anything — it is the sealed measure applied to the cell that exists. `R33`'s own
verdict name says which way this cuts:
`INHERITED_REFINEMENT_NATURALITY_FORCES_UNIFORM_MEASURE`. The compensator the bar forbids would
be a factor introduced *to fix up* a measure; `1/d!` is not introduced, it is what `Vol_4` *is*
on a simplex.

### 2.4 VERDICT, and the correction to 753

```text
RECONCILIATION = FORCED (statement displayed).
```

[YOURS] **753 called this a conflict between two sealed authorities. It is not, and I withdraw
that framing.** `V011` is silent where I said it disagreed (§2.1), and the measure the
"reconciliation" would supply is already classified uniquely (§2.2). What 753 correctly
established is the **arithmetic** — 24 exact frames, `det E_p = sgn(p)`, `|det E| = 1`,
`V_cell = 1/24`, the ratio `4!`. What it mis-typed is the **status** of that ratio: not a
divergence between authorities, but the value of one sealed measure on a cell type the box
formula does not cover.

[YOURS] The generalizable lesson, and it is the same one three relays running: **a clause's
quantifier decides its scope, and "general X" generalizes X and nothing else.** 751 was decided
by *"For an orthogonal physical cell"*; 755 is decided by *"For a general coframe"* — the same
sentence pair, read once for what it restricts and once for what it extends.

### 2.5 The forced statement, exact content, for A to author

```text
The general map's volume factor is the cell's intrinsic four-volume Vol_4(C),
classified uniquely at R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001
(e4cfaef1…) as mu_D(A) = Vol_4(A)/Vol_4(D), and selected per cell by
R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_RESULT_V001 (e60aec3c…).

  - On a parallelepiped cell with coframe e:   Vol_4 = |det e|.
    This is V011 aa7c6d49…[46074,46387) unchanged; the box case is recovered
    exactly and nothing in V011 is amended.
  - On a d-simplex with edge-frame E:          Vol_4 = |det E| / d!.
    For the sealed order-simplex subdivision of the unit 4-cube this gives
    1/24 per cell, 24 cells, total 1 — MAJ 08b91543…[19632,19996), reproduced
    exactly at 753 §1.3.

ZERO PHYSICS CHOICE: no new measure, weight, normalization or convention is
introduced.  The statement records which already-classified measure the
general map's volume factor denotes, and evaluates it on the two cell types
the working class produces.
```

[YOURS] **This is a restatement, not a ruling — but it is still not mine to write into the
record.** Authoring it is A's, and booking it is the registrar's; my charge was to establish
whether its content is forced, and it is.

---

## 3. GROUNDING, JURISDICTION, VERB AUDIT

### 3.1 Grounding

| # | Claim | Pin | Tag |
|---|---|---|---|
| 1 | Support's sealed definition: `support(L_c) ⊆ Omega_c` | `b0c636f3…[527,755)` | PROVABLE |
| 2 | Its reuse law is future-boundary / exhaustion indexed | `b0c636f3…[818,1091)` | PROVABLE |
| 3 | 37 support-near-refinement contexts, none a transport law | §1.3, 1,978 files | PROVABLE |
| 4 | Support-under-refinement named inside a STOPPED residue | `5203347c…[13728,14058)` | PROVABLE |
| 5 | The clause generalizes the coframe, not the cell | `aa7c6d49…[45718,46387)` | PROVABLE |
| 6 | `simplicial cell` = 1, `parallelepiped` = 1, both downstream of 753 | §2.1 census | PROVABLE |
| 7 | `R33`'s child-intrinsic universal | `e60aec3c…[551,740)` | PROVABLE |
| 8 | D012 types `R33` as the flat-cell measure selector | `74bbb7aa…` manifest row | PROVABLE |
| 9 | The intrinsic measure is uniquely `Vol_4`, with an executed audit | `e4cfaef1…[98,309)` | PROVABLE |
| 10 | The compensator bar does not bite | §2.3 | YOURS |
| 11 | The forced statement's content | §2.5 | YOURS |

**Pin check: 11/11.** All spans read from bytes this relay; seal provenance checked per file,
including manifest membership where no sidecar exists.

### 3.2 Jurisdiction check

**On hunting before authoring, which is what this relay was for.** Both halves paid: AG1 found
a sealed definition I had guessed wrong, and AG2 found a classification result that dissolved a
conflict I had reported. *Does the outcome space distinguish false from cannot-see?* Yes — AG1
returns a **named unsealed element** with its index identified, AG2 returns **FORCED** with the
content displayed. *Would the evidence appear if the theory is right?* Yes: §2.5's statement is
checkable against four sealed sources at once.

**On the VOID CONDITION.** No coefficient consulted. §2.5 introduces no measure, weight or
normalization — the whole point of the verdict is that none is needed.

**On the authoring line.** §2.5 is displayed as content and explicitly left for A to author and
the registrar to book. §1.4's transport is refused for a stated reason: it would require first
authoring an identification of `Omega_c` with a cellulation cell that no sealed text makes.

**On R9 / R9-JII.** Untouched.

### 3.3 Self verb audit — **CLEAN, with four disclosures**

1. **An instrument failure, caught by controls.** My first AG1/AG2(iii) probe ran `os.walk` on
   relative roots `workspace`/`supervision` **from inside `workspace/`**, so the file list was
   empty and four probes returned `0` — including `Omega_c` and `causal cell`, which I had just
   read on screen. Those two were **known-positive controls**, and they are the only reason I
   caught it. Every negative in this artifact comes from the re-run at the archive root, with
   the file count (**1,978**) printed as a control. **New practice worth keeping: put a
   known-positive in every negative-existential probe and print the corpus size.**
2. **753's "conflict between two sealed authorities" is withdrawn** (§2.4). The arithmetic in
   753 stands exactly; the status I assigned the `4!` does not.
3. **751's "structurally immediate" for support is withdrawn** (§1.5). I characterized a field
   without reading its defining principle, which was sealed, adjacent, and named after the
   thing I was describing.
4. **I had never opened `R33G`**, the file that decides AG2, despite having cited its sibling
   `R33` at 733, 751 and 753. It sits in the same packet, one row from `R33` in `D012`'s own
   manifest table. Seventh occurrence on this thread of the deciding material sitting beside
   something I had already used.

---

```text
SUPPORT = unsealed element named.  Support's SEALED DEFINITION is the Causal
    Incidence Support Principle b0c636f3...[527,755) — an adopted Level-1 principle:
    "support(L_c) is contained in Omega_c", the support of an INTERACTION DENSITY
    inside a Lorentz-covariant CAUSAL CELL.  Its sealed transport law is indexed by
    the EXHAUSTION, not by refinement — [818,1091): "Once the FUTURE BOUNDARY has
    crossed the closure face of Omega_c … A physical exhaustion adds new future
    incidences on new record factors."  Across 1,978 files, 37 distinct
    support-near-refinement contexts, NONE a transport law; the closest is inside a
    STOPPED residue (5203347c...[13728,14058), a bounded-geometry certificate
    "controlling … support overlap … and refinement density", preceded by
    S2_GLOBAL_ATTAINMENT = STOPPED).  THE UNSEALED ELEMENT: the behaviour of
    support(L_c) ⊆ Omega_c when Omega_c is SUBDIVIDED — and deriving it would first
    require AUTHORING an identification of the causal cell Omega_c with a cell of the
    record complex, which no sealed text makes.  751's "structurally immediate" is
    WITHDRAWN: support is not a cochain support and is not immediate.
RECONCILIATION = FORCED (statement displayed at section 2.5).  (i) V011's clause is
    SILENT on simplices, not in conflict: "For a GENERAL COFRAME theta^a = e^a_mu
    dx^mu" generalizes the COFRAME, not the cell shape, and on the parallelepiped
    cells it does govern, |det e| = V_cell remains EXACT for arbitrary frames.
    (ii) FORCED, and stronger — the measure is already CLASSIFIED: R33G
    e4cfaef1...[98,309), packet-sealed, verdict GLOBAL_INTRINSIC_FLAT_CELL_MEASURE
    _CLASSIFIED, "the intrinsic probability measure on a flat primitive causal
    diamond is UNIQUELY mu_D(A) = Vol_4(A)/Vol_4(D)", with an executed covariance
    audit (Lorentz generators 6, fixed-covector rank 4, nullity 0).  R33 selects the
    child's intrinsic measure; D012's own manifest types R33 "flat-cell measure
    selector"; MAJ evaluates it at 1/24 on the order-simplex; V011 evaluates it at
    |det e| on a parallelepiped.  ONE MEASURE, SEVERAL EVALUATIONS.
    (iii) V011's inserted-compensator / shape-dependent-scalar bar does NOT bite:
    1/d! is not introduced to fix up a measure, it is what Vol_4 IS on a simplex.
    753's "CONFLICT between two sealed authorities" is WITHDRAWN — its arithmetic
    stands exactly; the status I assigned the 4! does not.
VOID = clean
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+4 disclosures at section 3.3, including a probe run from
    the wrong directory that returned four false zeros and was caught only by
    known-positive controls)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
