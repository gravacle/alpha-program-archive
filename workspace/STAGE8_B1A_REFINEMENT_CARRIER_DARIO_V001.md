# STAGE 8 / 7A / [PLAN:B1a-3] — THE REFINEMENT CARRIER: HALF DERIVED, THE OTHER HALF NAMED, AND A FORCING CANDIDATE THE RECORD ALREADY OWNS

Lane: DARIO (Builder B, independent verifier). Relay 788.
State brief pinned by the relay: `PROGRAM_STATE_BRIEF_V005.md` = `e26f0d16055f3e83…` — digest matches
the pin, seal OK, read before task work.
Governing: 786 `STAGE8_B1A_LIFT_FORCING_CODEX2_V001.md` = `3966fdb124c6fed8…` SEALED-OK.
Declines in force: **S08**, **S26**. All headline items **CLAIMED**.

## Lead determination — CLAIMED

**The carrier splits cleanly in two, and only one half is derivable. I derived that half, and I
did not deliver the other — I name it rather than paper over it.**

```text
INCIDENCE HALF  (J_1 / J_2 / d_1'J_1 = J_2 d_1)   DERIVED, typed, and machine-verified.
COFRAME HALF    (the declared F'/F square, O3)     NOT DELIVERED.  Named as the stop.
```

**The structural result — why the carrier was missing rather than merely unwritten:**

> The two sealed constraint displays (`Ext_g`'s parent-edge sum, `Flux_g`'s child-flux sum) *are*
> the **aggregation** maps `sd*_1`, `sd*_2`, which run **K' → K**. The canonical structure a
> subdivision supplies has the **opposite variance** to the wanted lift. `J_1` is therefore a
> **SECTION** of `sd*_1`, and sections of a non-injective surjection are never unique. That is
> also why V011's own `J_1,J_2` — induced by an **injective** cellular map, one face to one face
> — are of a different type and cannot be reused (786's D12 item 3).

**And the record already owns a forcing candidate that 786 did not use and my own first pass
missed.** V011 seals `Q_flux`, *"the unique horizontal, minimum-norm lift"* with `d_1 Q_flux ξ = ξ`.
I validated my implementation against all three defining properties, then tested it:

```text
Q_flux is NOT sd*-equivariant.        max | sd*_1 Q'_flux - Q_flux sd*_2 | = 1.82  (scale 2.80)
sd*_1 Q'_flux VARIES over the flux fibre.                     max deviation = 0.894
BUT, at the MINIMUM-NORM fibre point:
        sd*_1 o Q'_flux o (min-norm flux section)  =  Q_flux        on im(d_1)
        300 trials, ZERO failures, worst deviation 8.9e-15.
```

**That is a candidate canonical carrier, and it cuts against the direction I was leaning.** It is
canonical only *relative to the counting inner product* — a Gate-3 metric input, not a metric-free
structure — so it does not settle forcing. It is handed to the principal as the sharpest live lead,
not adopted.

**Two of my own claims were refuted by commissioned check and I adopt both.** The forcing lemma was
stated at cochain level using "same vertex set", which is true of the **Freudenthal instance** and
false of the licensed generator (V011 licenses A2 as *"oriented simplicial/barycentric
subdivision"*; barycentric adds 65 vertices). And I read the sealed invariance clause as wholly
asymptotic when it is a **conjunction** whose first conjunct — *"The response map must commute with
pullback to a common refinement"* — carries **no tolerance at all**. That second error is the 742
shape again: **collapsing a conjunctive clause**.

**The correction is worth more than the claim it replaced:** that exact conjunct is stated over a
**common refinement**, so it *is* a coherence condition on spans of generators. The record does not
leave the relation set open — **it supplies a relation**, and that relation is exactly what cannot
be evaluated while the carrier is missing.

---

## 0. Preflight

```text
OUTPUT NAME   probed recursively before any write: artifact and sidecar ABSENT.
STATE BRIEF   PROGRAM_STATE_BRIEF_V005.md  e26f0d16055f3e83…  seal OK, digest matches the pin.
DRIFT CHECK   brief V005, plan V003, declines V002 all still current (the 782 lesson). No drift.
786           STAGE8_B1A_LIFT_FORCING_CODEX2_V001.md   3966fdb124c6fed8…  SEALED-OK
785           STAGE8_B1A_CONNECTION_IDENTIFICATION_CODEX2_V001.md  1b45d5a657fff30b…  SEALED-OK
mine, verified: RA27_3 frontier 4d072e7671113357… ; simplicial coframe d6f490b80e8d8775… ;
              support-and-forcing 9685af44cc48f01f… ; identification family 487cc63f5dfc1c8d…

V011 HAZARD, handled: TWO byte-versions exist.  Sealed packet copy
   workspace/mirrored_sources/corpus_members/…V011.md = aa7c6d4904706276… (78,794 B) — USED.
   workspace root copy = 20a3a17d44e15841… (84,987 B), UNSEALED — offsets NOT interchangeable.
SPANS RE-DERIVED BY ME (all MATCH): D4 [13822,16181) 9809578b… ; D12 [10842,13138) c0461282… ;
   V011 D9 [44595,44690) c6cd568b… ; D10 [46074,46387) dffd13b3… ; D11 [47025,47247) 9ff68526…

GATES: alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false.
No member binding; no fixed-point execution; no end test; no numeric evaluation of physical
quantities; no comparison to measured constants; no common cell formed; no junction map evaluated.
NO SMOOTH DATA IMPORTED (S26).  NO EM IDENTIFICATION (S08).  NOTHING SELECTED BY OUTCOME.
PE-1..PE-7: pointer-known, ZERO WEIGHT, not opened, not consulted.
```

---

## 1. AS1 — THE CARRIER: INCIDENCE HALF DERIVED, COFRAME HALF NAMED

### 1.1 The direction theorem — [YOURS]

786 §1.1 displays two sealed constraints. Read as maps they are:

```text
sd*_1 : C^1(K') -> C^1(K),   (sd*_1 a')_e  = sum_(e' subdividing e) orientation(e',e) a'_(e')
sd*_2 : C^2(K') -> C^2(K),   (sd*_2 xi')_f = sum_(f_i subset f) xi'_(f_i)
```

`Ext_g(a)` is exactly the fibre `(sd*_1)^{-1}(a)` modulo new-vertex gauge; `Flux_g(ξ_f)` is exactly
the fibre of `sd*_2`. **The canonical structure runs refined → coarse.** Hence:

```text
J_1 is a SECTION of sd*_1  (sd*_1 J_1 = id),  not a pullback.
sd*_1 is INJECTIVE  <=>  g adds no new edge  <=>  g in A0.
=> for every non-trivial generator the section space is a positive-dimensional affine space.
```

This is why V011's own `J_1,J_2` cannot be reused: they are induced by an **injective cellular map
sending one face to one face** (786 D12 item 3) — the opposite type from a subdivision.

### 1.2 The cochain-map property — DERIVED, then MACHINE-VERIFIED

Interior edges of a subdivided parent face are shared by exactly two subfaces with opposite induced
incidence, so they cancel; boundary edges survive with the parent sign. Hence
`sd*_2 d_1' = d_1 sd*_1`.

**I did not rest on the argument.** I built both complexes from scratch and tested:

```text
A1 (cubical bisection)  24 parent squares x 200 random rational cochains -> 0 mismatches
A2 (Freudenthal)        24 parent squares x 200 random rational cochains -> 0 mismatches
TRANSVERSE-MULTIPLICITY PROBE (my own D4 §3.4 pre-registered this as the live failure mode:
   "I summed over in-plane sub-faces only and was short by exactly the transverse multiplicity"):
   perturb one off-plane edge at a time -> 0 off-plane edges move any parent-square value.
```

**Independent census reproduction (all six of 786's numbers, from my own construction):**

| | 786 | mine |
|---|---|---|
| A2 edges / parent / free | 65 / 32 / 33 | 65 (= 3⁴−2⁴) / 32 / 33 ✓ |
| A1 affine / gauge / physical | 184 / 65 / 119 | 216−32=184 / 81−16=65 / 119 ✓ |

### 1.3 The intertwining criterion — DERIVED

```text
J_2 with d_1' J_1 = J_2 d_1 EXISTS  <=>  J_1(ker d_1) subseteq ker d_1'   [J_1 linear]
and then J_2 is UNIQUE on im(d_1) and unconstrained off it.
```
*Proof.* Define `J_2(d_1 a) := d_1' J_1 a`; well-defined iff `d_1(a−b)=0 ⇒ d_1' J_1(a−b)=0`. ∎

### 1.4 Flux conservation is a CONSEQUENCE, not an obligation — with its disclosure

Given §1.2 and `sd*_1 J_1 = id`: `sd*_2(d_1' J_1 a) = d_1 sd*_1 J_1 a = d_1 a`. So every section
automatically satisfies `Σ_i ξ'_i = ξ_f`.

[YOURS] **Disclosed, because it flatters the result otherwise:** this is the *linear* half, and my
own sealed D5 (`REFINEMENT_BRIDGE`) already conceded it — *"LINEAR `Σ_i ξ'_(f_i)` determined by the
parent. TRANSPORTS. QUADRATIC `Σ_i (ξ'_(f_i))²` NOT determined — it varies over the k−1 free
parameters at fixed total."* **I proved the half the record had already granted.** The half that
does not transport is O4's, and §3 is where it bites.

### 1.5 The forcing lemma — CORRECTED to carrier level, per generator

**My first statement was wrong and I adopt the refutation.** I argued at *cochain* level from "K'
has the same vertex set", which is a property of the **Freudenthal instance**, not of the licensed
generator: V011 `[46772,47023)` licenses A2 as *"oriented simplicial/barycentric subdivision"*, and
**barycentric subdivision of the 4-cube adds 65 vertices** (V′=81, E′=544, T′=1232). For that
licensed member the cochain-level uniqueness is **false**.

**Corrected, and now general.** Let `n_new = |V(K')| − |V(K)|`.

```text
(i)   SOLVABILITY. sd*_1 maps ker d_1' ONTO ker d_1, so every closed parent cochain lifts closed.
(ii)  FIBRE.  For a in ker d_1, { a' : d_1'a' = 0, sd*_1 a' = a } is affine of dimension EXACTLY
      n_new — a single point iff n_new = 0.
(iii) THE AMBIGUITY IS PURE GAUGE.  That fibre is a coset of im(d_0') cap ker(sd*_1), of dimension
      exactly n_new; since ker d_1' = im d_0' (H^1 = 0 verified), it collapses in Conn(K').
(iv)  FORCING, CORRECTLY LEVELLED.  On the DECLARED carrier Conn = C^1/im(d_0) — which is V011's
      own carrier, and which Ext_g already quotients by new-vertex gauge — J_1 is FORCED on the
      ker d_1 sector for EVERY generator.
```

**Residual, instance-indexed** (`rank d_1 = 17` on the 4-cube; the second factor is the physical
refined quotient):

| instance | `dim ker sd*_1` | gauge | physical | residual = `17 × physical` |
|---|---|---|---|---|
| A2 Freudenthal | 33 | 0 | 33 | **561** |
| A1 bisection | 184 | 65 | **119** ← = 786's own census | **2023** |
| A2 barycentric | 512 | 65 | 447 | **7599** |

[YOURS] The A1 column lands on 786's independently sealed "119-dimensional physical quotient" —
which is a check on the corrected lemma, not a coincidence I arranged.

### 1.6 What is NOT delivered — the named stop

```text
STOP.  THE COFRAME HALF OF THE CARRIER IS NOT DERIVED.
   O3 requires  J_2^g(D_e F) = D_(e') F'  "with the relation between F' and F DECLARED rather
   than guessed" (786 §2).  AS1 names "the declared F'/F coframe square" as a required output.
   NOTHING ABOVE SUPPLIES IT.
   And the word "coframe" occurs in the sealed V011 exactly twice (46197, 46996) — BOTH on the
   SMOOTH tetrad side, which S26 bars as a source.  So the discrete coframe half cannot be taken
   from V011 either.
   I considered defining F' := D_(e')^{-1} xi' and declining to: it would make O3 VACUOUS by
   construction, which is a sign the constraint has been misread, not discharged.
```

Also not delivered: **O1's non-composition clauses** — `L_id = id` and "a lift exists on every
generator" are stated, not proved, and **A0 was exercised only by type, never constructed.**

---

## 2. AS2 — THE SQUARES, INSTANTIATED

| obligation | on A0 | on A1 | on A2 | status |
|---|---|---|---|---|
| O2 incidence intertwining | `sd*_1 = id`, section unique | verified, 24 squares × 200 | verified, 24 squares × 200 | **RUNNABLE, instantiated** |
| O1 `Ref_a` naturality | `L_id = id` by type | not instantiated | not instantiated | **NOT RUNNABLE** (needs the relation set) |
| O3 child-coframe | — | — | — | **NOT RUNNABLE** (F′/F undeclared, §1.6) |
| O4 quadratic | — | — | — | **SPLITS — see §3** |

```text
SQUARES = incidence square INSTANTIATED on A0/A1/A2; coframe square NOT instantiated. STOPPED.
```

---

## 3. AS3 — THE SOLUTION-SET TEST

### 3.1 O4 splits, and my reading of it was wrong — adopted

V011 `[47025,47247)` is a **CONJUNCTION**, and only the second conjunct carries a tolerance:

```text
[47025,47092)  "The response map must commute with pullback to a common refinement,"
               *** NO qualifier, NO tolerance, NO limit.  EXACT. ***
[47106,47247)  "...the intensive quadratic coefficient must be invariant under each elementary
               refinement up to a boundary term whose ratio to four-volume tends to zero."
```

Scope probe on the sealed file: `boundary term` occurs **once** (47192), `tends to zero` **once**,
`commute` **once** (47047, this sentence; the other `commut` hits are "commutator"). **No clause
anywhere extends a tolerance over conjunct 1.**

```text
SURVIVES  : demanding EXACT equality of Q on ONE object is stronger than CONJUNCT 2 requires;
            adopting it in the objectwise diagnostics would author a constraint the record does
            not impose.
WITHDRAWN : "O4 has no finite bite."  FALSE.  Conjunct 1 is exact, finite and decidable.
STATUS    : conjunct 1 cannot be EVALUATED, because the coarse-to-fine carrier does not exist.
            UNDECIDABLE_FROM_STOCK — not vacuous.  O4 does not clear away; it RE-INSTANTIATES the
            missing-carrier defect at the level of the response map.
```

[YOURS] **This is the 742 failure shape again — collapsing a conjunctive clause** — and it is the
second time this session a conjunction has cost me a headline. I record it as a repeat, not a
novelty.

### 3.2 The consequence, which is worth more than the claim it replaced

Conjunct 1 is stated over a **common refinement** — i.e. over a *span* of generators. **It is
itself a coherence condition.** Therefore:

```text
The residue is NOT "does the working category have relations?"  THE RECORD SUPPLIES ONE.
A natural family may be DEFINED on composites by L_(h o g) := L_h o L_g, so composition holds by
construction; coherence on relations is the only condition — and conjunct 1 IS such a relation.
=> "with no relations, FREE follows immediately" is DEAD.  Freedom cannot be reached by
   discharging O4, because O4 is where the relation lives.
```

### 3.3 The forcing candidate the record already owns — [YOURS]

V011 seals a distinguished lift (span verified; **note:** the span digest cited to me as
`d79393f5…` does **not** reproduce — I compute `1d25eb77…` at those bounds; the object is real, the
citation drifted, and I report the drift rather than repeat it):

```text
P_h = I - d_0(d_0^† d_0)^+ d_0^† ,   F_phys = im(d_1) ,
Q_flux = P_h d_1^†(d_1 P_h d_1^†)^+ |_(F_phys)
"For every xi in F_phys, Q_flux xi is the unique horizontal, minimum-norm lift ...
 It obeys d_1 Q_flux xi = xi."
```

**Implementation validated first** (all three defining properties, 50 random trials): `d_1 Q ξ = ξ`
✓, horizontal (`⊥ im d_0`) ✓, minimum norm in its coset ✓. Then:

```text
NOT sd*-EQUIVARIANT.   max | sd*_1 Q'_flux xi' - Q_flux sd*_2 xi' | = 1.82   (scale 2.80, 200 trials)
sd*_1 Q'_flux VARIES over the flux fibre at fixed parent xi.   max deviation 0.894 over 31 samples
   => the one distinguished lift the record supplies does NOT induce a canonical J_1.

*** BUT, AT THE MINIMUM-NORM FIBRE POINT ***
        sd*_1 o Q'_flux o (min-norm flux section)  =  Q_flux    on im(d_1)
        300 independent trials, ZERO failures, worst deviation 8.9e-15.
```

[YOURS] **I report this against my own leaning.** Everything above pointed toward freedom; this
points the other way. It is a **candidate**, not a result, for one exact reason: *both* sides are
minimum-norm, so the combination is canonical only **relative to the counting inner product** — a
Gate-3 metric input, not a metric-free structure. Adopting it would select. **Handed to the
principal as the sharpest live lead, unadopted, with its metric dependence on its face.**

### 3.4 Verdict

```text
FORCED_UNIQUE : NOT ESTABLISHED.  sd*_1 is injective only on A0; O2 forces J_1 only on the
   ker d_1 sector; the residual is 17 x (physical quotient) per instance.  A metric-relative
   candidate exists (§3.3) and is not adopted.
FREE          : NOT ESTABLISHED.  Two COMPLETE natural families would need the coframe half
   (§1.6, absent) and coherence against the sealed relation of §3.2 (unevaluable).  Two fibre
   points are not two families — 786 §3.2 is unchanged by anything here.
SOLUTION_SET  = stopped (element named).
```

---

## 4. AS4 — COMPOSITION

My own sealed D4 §3.2 settles the easy direction: *"a composition of chain maps is a chain map,
and functoriality on composites follows by induction on composite length"* — and that applies to
`sd*` as derived in §1.2. Defining `L_(h∘g) := L_h ∘ L_g` makes composition hold by construction.

```text
COMPOSITION = failing item displayed.
   The failure is NOT the composite step and NOT identity; it is COHERENCE on the sealed relation
   of §3.2 — O4 conjunct 1's exact commutation with pullback to a COMMON REFINEMENT.  That
   predicate is well-formed and finite, and it CANNOT BE EVALUATED because the coarse-to-fine
   carrier it quantifies over is the very object under construction.
```

---

## 5. AS5 — MICROSTATE COMPARISON, FREEDOMS, FLATTENING

```text
MICROSTATE_COMPARISON = n-a.  AS5 is conditional on AS3 landing FREE; it did not.  Comparing the
   sealed 32/118-dimensional fibres against a four-obligation residual space that has not been
   formed would compare a finite fibre with an undefined set.  786 §4's disposition is unchanged.
```

### 5.1 `FREEDOMS_CONSUMED` — item by item (the 784 lesson)

| datum | tag | where consumed |
|---|---|---|
| per-object Gate-4 connection | **CARRIED AS DERIVED** | §1.1; not re-derived |
| connection representative | **QUOTIENTED BY VERTEX GAUGE**, never fixed | §1.5 (iii)–(iv) |
| refined interior-edge values | **UNSUBSTITUTED; free fibre displayed** | §1.5; no equidistribution, area rule, or minimiser adopted |
| **the counting inner product (Gate-3 metric)** | **CONSUMED — and flagged** | §3.3 only. `Q_flux` and "min-norm" are metric-dependent; this is why §3.3 is a candidate, not a result |
| child coframes | **NOT CONSUMED** | the coframe half is not delivered (§1.6) |
| intrinsic `Vol_4` | **NOT CONSUMED** | O4 was split, not evaluated |
| the F′/F relation | **ABSENT OF SEALED STOCK, NOT AUTHORED** | §1.6; I declined the vacuous definition |
| relation set of `Ref_a` | **NOT AUTHORED** | §3.2; the record supplies conjunct 1 |
| A2's representative | **NOT NARROWED** | §1.5 treats Freudenthal as one instance of a licensed generator |
| smooth coframe/connection constituent | **NOT CONSUMED; BARRED (S26)** | mentioned only to explain why it cannot fill the gap |
| 32/118-dim fibres | **DIAGNOSTIC ONLY** | not promoted to natural families |

**SUBSTITUTED: none.**

### 5.2 `FLATTENING_CHECK` — against `DECLINE_REGISTER_V002` (S01–S37)

```text
S08  no EM / smooth-public-field / Maxwell / response identification    CLEAN — the discrete
     incidence connection is treated purely as C^1(K)/im(d_0); no physical reading anywhere.
S26  C_ref barred as a source (audit/target interface only)             CLEAN — the smooth
     same-coframe-and-connection clause is named ONLY to record that it cannot fill the carrier;
     it supplies no step.  §1.6 notes V011's two "coframe" hits are both on the barred side.
S27, S28, S13, S01 and the remaining rows: not touched by this artifact.
FLATTENING_CHECK = clean (37 rows walked; 2 live, both discharged above).
```

---

## 6. JURISDICTION AND VERB AUDIT

**Jurisdiction.** *What was the rule written to protect?* AS1 says "stopping honestly wherever
sealed stock ends". The risk was live: half a carrier presented as a carrier would have unblocked
B1a on paper. *Does the outcome space distinguish a real derivation from a gesture?* Yes — §1.2 and
§1.5 are machine-verified against 786's independently sealed censuses, and §1.6 names what is
missing. *Would evidence look different if the coframe half were derivable?* Yes: V011's "coframe"
occurrences would not both be on the S26-barred side.

**VOID CONDITION.** Nothing selected by outcome. §3.3 is the test: it points *against* my leaning
and is reported at full strength and left unadopted, with its metric dependence stated.

**BR-1 / builder independence.** No `evaluator_build_A/` or `checks/` file read, by me or by any
commissioned checker. The sealed V011 packet copy was used throughout; the unsealed root copy was
not. `~/.codex` untouched; `memory-bank` never searched.

### 6.1 Self verb audit — **NOT CLEAN: five disclosures**

1. **The forcing lemma was instance-specific and I stated it as the generator's.** "Same vertex
   set" is Freudenthal, not licensed A2 — which V011 licenses as *"oriented simplicial/**barycentric**
   subdivision"*, adding 65 vertices. My headline "exact dimensions for A2" were Freudenthal-only
   numbers. Corrected to carrier level, per generator, instance-indexed.
2. **I collapsed a conjunctive clause.** D11 is two requirements; only the second is asymptotic. I
   applied "asymptotic" to both and concluded O4 had no finite bite. **This is the 742 failure
   shape, and its second appearance this session** — at 784 the failure was conditioning, at 742
   and here it is reading a conjunction as a single claim.
3. **§1.4 proves the half the record already granted.** My own sealed D5 states the linear half
   transports and the quadratic half does not. Presenting "flux conservation is a consequence" as a
   reduction, without that sentence beside it, would have overstated the reduction.
4. **O1 and O3 are not delivered at all** — half the named carrier. No amount of O2 structure
   substitutes for the coframe square, and A0 was exercised only by type.
5. **A cited span digest did not reproduce** (`d79393f5…` vs my `1d25eb77…` for the `Q_flux`
   block). The object is real; the citation drifted. Recorded because I would rather report a
   provenance mismatch than quietly re-cite it.

*Direction check:* 1, 2, 3 and 4 run against my own work; 5 against a source handed to me. The one
finding that could have flattered me — §3.3 — points **against** the freedom direction the rest of
the artifact leans toward, and I state it that way. *Instrument note:* 1 and 2 were surfaced by
commissioned adversarial check run **before** the seal; 18 of 20 attacks failed, so §1.1–§1.4 and
§1.3's criterion survived scrutiny. §3.3 came from the completeness critic asking what no lens had
tested.

---

```text
CARRIER = stopped (element named).  DERIVED AND TYPED — the INCIDENCE half:
   sd*_1 : C^1(K')->C^1(K) and sd*_2 : C^2(K')->C^2(K), read off the sealed Ext_g/Flux_g
   constraints;  the DIRECTION THEOREM (the canonical map runs K'->K, so J_1 is a SECTION of
   sd*_1, and sd*_1 is injective iff g in A0 — which is why V011's injective-cellular J_1,J_2 are
   the wrong type and the carrier was missing rather than unwritten);  the COCHAIN-MAP PROPERTY
   sd*_2 d_1' = d_1 sd*_1, derived combinatorially and MACHINE-VERIFIED on all 24 parent squares
   of BOTH A1 and A2 over 200 random cochains each with ZERO mismatches, and with the
   transverse-multiplicity hazard my own D4 pre-registered probed explicitly (0 off-plane edges
   contribute);  the INTERTWINING CRITERION (J_2 exists iff J_1(ker d_1) subseteq ker d_1', then
   unique on im d_1);  FLUX CONSERVATION as a CONSEQUENCE of any section (disclosed: this is the
   linear half my own sealed D5 already granted);  and the FORCING LEMMA, corrected to carrier
   level and per generator — J_1 forced on the ker d_1 sector for EVERY generator, residual
   17 x (physical refined quotient): 561 Freudenthal, 2023 A1 (whose 119 reproduces 786's own
   sealed census), 7599 barycentric.
   NOT DELIVERED, NAMED: the COFRAME HALF — O3's declared F'/F square.  Nothing above supplies it,
   and V011's only two "coframe" occurrences are both on the S26-barred smooth side.  I declined
   to define F' := D_(e')^{-1} xi', which would make O3 vacuous by construction.  Also not
   delivered: O1's L_id = id and per-generator existence clauses; A0 exercised only by type.
SQUARES = incidence square INSTANTIATED and runnable on A0/A1/A2; coframe square NOT instantiated.
   STOPPED.
SOLUTION_SET = stopped (element named).  FORCED_UNIQUE not established: sd*_1 is injective only on
   A0 and O2 forces J_1 only on the ker d_1 sector.  FREE not established: two COMPLETE natural
   families need the absent coframe half and coherence against a sealed relation that cannot be
   evaluated; two fibre points are not two families.
   NEW, AND AGAINST MY OWN LEANING — A FORCING CANDIDATE THE RECORD ALREADY OWNS: V011's sealed
   Q_flux, "the unique horizontal, minimum-norm lift", d_1 Q_flux xi = xi.  Implementation
   validated on all three defining properties, then tested: NOT sd*-equivariant (max deviation
   1.82 at scale 2.80 over 200 trials) and sd*_1 Q'_flux VARIES over the flux fibre (0.894), so it
   induces no canonical J_1 — BUT at the MINIMUM-NORM fibre point
   sd*_1 o Q'_flux o (min-norm flux section) = Q_flux on im(d_1), over 300 trials with ZERO
   failures and worst deviation 8.9e-15.  Canonical only RELATIVE to the counting inner product, a
   Gate-3 metric input; handed to the principal as the sharpest live lead, UNADOPTED.
COMPOSITION = failing item displayed.  The composite step and identity are free (my own sealed D4:
   a composition of chain maps is a chain map); defining L_(h o g) := L_h o L_g makes composition
   hold by construction.  THE FAILURE IS COHERENCE ON A SEALED RELATION: V011 [47025,47247) is a
   CONJUNCTION whose FIRST conjunct — "The response map must commute with pullback to a common
   refinement" — carries NO tolerance (scope probe: "boundary term" once, "tends to zero" once,
   "commute" once, in the whole sealed file).  Stated over a COMMON REFINEMENT, that conjunct IS a
   coherence condition on spans of generators.  So the record does not leave the relation set open
   — IT SUPPLIES A RELATION — and that relation is exactly what cannot be evaluated while the
   carrier is missing.  My earlier reading ("O4 has no finite bite") is WITHDRAWN; what survives is
   only that exact equality of Q on ONE object is stronger than conjunct 2 requires.
MICROSTATE_COMPARISON = n-a (AS3 did not land FREE; 786 section 4's disposition unchanged).
B1A_STATUS = remaining stated.  Remaining: (1) the coframe half — declare/derive the F'/F square
   without importing the S26-barred smooth constituent; (2) O1's identity and per-generator
   existence clauses, with A0 actually constructed; (3) test whether the section 3.3 min-norm
   combination is NATURAL (identity + composition) across generators — if it is, B1a closes
   FORCED relative to the counting metric, and the metric itself becomes the principal's decision;
   (4) evaluate O4 conjunct 1 once a carrier exists.  The per-object Gate-4 connection remains
   derived; no prior closure is reversed.
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+5): (1) the forcing lemma was Freudenthal-specific and I stated it as
   the licensed generator's — V011 licenses A2 as "oriented simplicial/BARYCENTRIC subdivision",
   which adds 65 vertices and makes my cochain-level uniqueness FALSE; corrected to carrier level;
   (2) I COLLAPSED A CONJUNCTIVE CLAUSE, reading D11's two requirements as one asymptotic claim —
   THE 742 FAILURE SHAPE, and its second appearance this session; (3) section 1.4 proves the linear
   half my own sealed D5 had already granted, and would have overstated the reduction without that
   sentence beside it; (4) O1 and O3 are not delivered at all — half the named carrier; (5) a span
   digest cited to me did not reproduce (d79393f5… vs my 1d25eb77…) and I report the drift rather
   than re-cite it.  1-4 run against my own work; the one finding that could have flattered me
   (section 3.3) points AGAINST my leaning and is stated that way.
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
