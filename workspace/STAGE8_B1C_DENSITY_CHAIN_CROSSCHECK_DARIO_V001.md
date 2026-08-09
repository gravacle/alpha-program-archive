# STAGE 8 / 7A / [PLAN:B1c-6] — THE DENSITY CHAIN SURVIVES; ONE SCOPE CORRECTION AND ONE CUSTODY OBSERVATION

Lane: DARIO (Builder B, independent verifier). Relay 813.
State brief pinned: `PROGRAM_STATE_BRIEF_V005.md` = `e26f0d16055f3e83…`, seal OK. Law 8 throughout.
Subjects (builder-never-verifies): **810** `STAGE8_B1C_DENSITY_LAYER_CODEX2_V001.md` =
`00e2654a3b48bd8a…` and **811** `STAGE8_B1C_RECEIVER_RETYPE_CODEX2_V001.md` = `8d57b8d7df82342f…`
— both `.md.seal` **OK**, digests matching the relay's pins.
All headline items **CLAIMED**. PE-1..PE-9 pointer-only, not opened, not consulted.

## Lead determination — CLAIMED

**I attempted to refute the chain on its most vulnerable point and the refutation failed on the
record's own sentence. The chain stands, with one scope correction and one custody observation.**

```text
RETYPE          = CONFIRMED (license verified span by span)
IDENTIFICATION  = CONFIRMED identity (no variance, normalization or basis shift)
D_G             = CONFIRMED forced — WITH A SCOPE CORRECTION on WHY it is forced
CLASSIFICATION  = confirmed, one precision; all three undecidables REAL, not reading artifacts
```

**The attack I ran, and why it failed.** 793 types the density with
`CurrentDomain(delta_K) = Curr(K)`. A **current** density has units of current-per-four-volume; a
**volume** is four-volume. If `delta_K` were a current density, `delta_K = Vol_4` would be a
unit-class error — precisely the normalization trap this arc keeps producing. I hunted for the
licensing sentence expecting to find it absent.

It is present, and it is decisive. `WHERE` `[11067,11566)` sha `f1236e38f976dc01…`:

> *"`e_G = f_R^* e_G'` on the old image, **`mu_G = f_R^* mu_G'` on the old image, (B1-14)** and
> `mu_G'` is positive. **`Cof_R` and `Dens_R` are the induced operators in the already declared R4
> unit classes.** Their duality square commutes; no scale or frame is selected."*

**`Dens_R` is the operator induced by `mu` — the measure — and WHERE pairs it with the coframe in
one law and one declared unit class.** `delta` is what currents are normalized *against*, not a
current density. The identification is licensed by the sentence 811 cites, and my attack dies on
it.

**The scope correction.** `d_g` is forced — but **forced by singleton-ness, not by a derivation.**
The sharp type makes `R4Dens_sharp(K)` a one-element set (the uniquely classified `Vol_4`), and a
map between one-element sets is unique. "DERIVABLE-FORCED" is true and reads as though a derivation
produced the arrow; what produced it is that the re-type left exactly one candidate. **The real
content is the aggregation check**, which I re-derived exactly and which could have failed.

**The custody observation.** 811 retires **DS2**, a scope wall another lane declared deliberately.
The mathematics is licensed; **retiring another lane's declared scope is registrar-shaped**, and
811 performs it in its own final lines. Flagged, not adjudicated.

---

## 1. AS1 — THE RE-TYPE: **CONFIRMED**

### 1.1 The license, span by span

| source | span / sha | what it licenses |
|---|---|---|
| `WHERE` `19b2060392b6e044…` | `[11067,11566)` sha `f1236e38f976dc01…` | **the decisive one** — `mu_G = f_R^* mu_G'` in the same law as the coframe; *"`Cof_R` and `Dens_R` are the induced operators in the already declared R4 unit classes"*; *"no scale or frame is selected"* |
| `MEAS-ADD` `9ae682eb7834304d…` | `[1517,2544)` sha `9bffbe45a47285c2…` | `Vol_4` uniquely classified; `|det e|` on a box, `|det E|/4!` on a simplex; **"ZERO PHYSICS CHOICE: no new measure, weight, normalization or convention is introduced"** |
| `R33G` (packet, mode 3) | — | `mu_D(A) = Vol_4(A)/Vol_4(D)` unique |

**The `VolNorm` question, answered.** 811 claims the cellwise equation `delta_K(C) = Vol_4(C)` is
the old `VolNorm` predicate *expanded*, "not an extra condition." Against it: `VolNorm` could have
meant a *normalized* density (`1/Vol_4`), which is a different object. **WHERE settles it** — the
predicate pairs `mu` with the coframe under a commuting duality square, and `MEAS-ADD` fixes `mu`'s
evaluation as `|det e|` / `|det E|/4!`. Those are volumes, not reciprocals. **No excess.**

### 1.2 The hunt for a sentence the re-type exceeds

I ran the relay's demand — find any sealed sentence the re-type contradicts. **The strongest
candidate is 793's own declaration**: *"`R4Dens(K)` is deliberately opaque … Refining that sort
here would author the very object the build is meant to locate."*

**Does 811 author it? NO.** It identifies the density with an already-classified, uniquely-forced
measure whose own spec says *no new measure, weight, normalization or convention is introduced*.
Authoring would mean supplying a density the record lacks; 811 supplies none — it removes a name.

```text
RETYPE = CONFIRMED (license verified).  No sealed sentence is exceeded or contradicted.
```

### 1.3 Custody observation — flagged, not adjudicated

793 declared the opacity **deliberately**, as a lane act. 811 declares `DS2 = DISSOLVED` and
retires it. **The substance is licensed; the act of retiring another lane's declared scope wall is
registrar-shaped**, and 811 performs it in its own final lines rather than routing it. I record
this because it is a custody question the mathematics does not settle, and because a scope wall
that a lane can retire is a weaker instrument than one that only the registrar can.

---

## 2. AS2 — THE IDENTIFICATION `delta_K' = mu_K'`: **CONFIRMED IDENTITY**

### 2.1 811's citation of my own 806 is accurate

`806` = `3151fd1a38ab30a5…` (matches 811's pin). Span `[727,2831)` sha `d1f9f3157beb1105…`
re-derived by me: it **does** display `mu_K'` among the four supplied components and **does** list
`delta_K'` and `d_g` among the six absent — exactly as 811 represents it. **No misquotation.**

### 2.2 The three trap classes, checked individually

```text
NORMALIZATION — CLEAN.  MEAS-ADD: "no new measure, weight, normalization or convention is
   introduced."  delta_K(C) = Vol_4(C) is an evaluation of the classified measure, not a rescaling.
BASIS         — CLEAN.  The density is cellwise on Cell_4(K); no basis of a cochain space is
   chosen, so there is no basis to shift.  (This is the trap that cost me 804; it does not arise
   here because nothing is expressed in a chosen basis.)
VARIANCE      — REAL, AND 811 NAMES IT.  WHERE's law is a PULLBACK, mu_G = f_R^* mu_G'
   (contravariant); 793's receiver arrow d_g : R4Dens(K) -> R4Dens(K') is FORWARD (covariant).
   811 reconciles WITHOUT inventing an inverse, by defining d_g on the canonical admissible slice.
   LEGITIMATE — but see section 3: the reconciliation consumes the singleton-ness, so it inherits
   the re-type as a precondition rather than standing on its own.
```

```text
IDENTIFICATION = CONFIRMED identity.  No hidden conversion.
```

---

## 3. AS3 — `d_g`: **CONFIRMED FORCED, WITH A SCOPE CORRECTION**

### 3.1 Re-derived independently, exact rationals

```text
d_g(delta_K)(C') := Vol_4(C');   check:  sum_(C' over C) Vol_4(C') = Vol_4(C)

  A0 identity/relabeling                     1 x 1      = 1    aggregates ✓
  A1 cubical bisection                      16 x 1/16   = 1    aggregates ✓
  A2 order-simplex subdivision               24 x 1/24   = 1    aggregates ✓
  A1 then A2 (384-cell common refinement)   384 x 1/384  = 1    aggregates ✓
  A2 then A1                                384 x 1/384  = 1    aggregates ✓        both paths agree
```

**All five exact.** This is the part of 811's claim that carries real content: it could have
failed, and had it failed the sharp type would have been refuted.

### 3.2 The scope correction — **why** it is forced

```text
811 types d_g as DERIVABLE-FORCED.  That is TRUE.  But the forcing mechanism is:
   R4Dens_sharp(K) = { delta : delta(C) = Vol_4(C) } and Vol_4 is UNIQUELY CLASSIFIED,
   so the admissible slice is a SINGLETON, and a map between one-element sets is unique.

*** d_g IS FORCED BY SINGLETON-NESS, NOT BY A DERIVATION. ***

Consequences, stated so downstream work does not over-read the label:
 (i)  the forcing is INHERITED from AS1's re-type — if the re-type were ever narrowed, the
      forcing would go with it; it is not an independent result;
 (ii) "DERIVABLE-FORCED" reads as though an argument produced the arrow.  What produced it is
      that exactly one candidate remained.  811 did NOT select among options — there were none —
      so the answer to the relay's question ("is it pinned, or did 811 select?") is PINNED;
 (iii) the AGGREGATION CHECK is the substantive content and it is confirmed.
```

```text
D_G = CONFIRMED forced (re-derived) — with the forcing mechanism corrected to singleton-ness.
```

---

## 4. AS4 — THE 810 CLASSIFICATION SPOT-CHECK

### 4.1 `s_g` / `S_g` — the forced-once-`f_g` pinning argument: **CONFIRMED**, one precision

810: *"once `f_g` and the named child decomposition exist, the image of every chain basis element
and hence the linear boundary-intertwining map are fixed"*, and `S_g` *"is definitionally
`s_g|Curr(K)`"*.

**Sound.** A linear map is determined by its values on a basis; given `f_g` and the child
decomposition, those values are determined, and boundary intertwining is then a *constraint* on the
determined map, not a further choice. A restriction of a determined map is determined.

**Precision, offered because it matters downstream:** *determined* is not *admissible*. 793's
bridge type requires `S_g` to be **injective and current-preserving**. Those are **checks that can
fail**. 810 is honest here — it says the lineage *"fixes the carrier and conservation/injectivity
checks"*, i.e. fixes the checks, not that they pass. **`DERIVABLE-FORCED` must not be read
downstream as `will-succeed`.**

### 4.2 The three undecidables — record's absences, or reading artifacts?

Applying the false-boundary standard (**record-voiced AND survives a dedicated hunt**), and
corroborating from **my own independent prior hunts** rather than by re-reading 810:

| | 810's reason | record-voiced? | survived a hunt? | verdict |
|---|---|---|---|---|
| **`f_g`** | physical-path realization unsealed; *"a cellular map cannot be relabeled as the physical map under S26"* | **YES** — S26 is a decline row | **YES** — my 773 magnetic-sector hunt (2,952 files) and 792's sweep returned no bridge | **REAL** |
| **`F_g`** | CIS/CDL support is exhaustion-indexed; the subdivision/support functor is absent | **YES** — 755, IDX §3.3 | **YES** — **this is my own 792/798 finding**: the exhaustion-vs-refinement index gap, and my 798 hunt found no object relating the two index categories | **REAL** |
| **`eta_resp`** | *"ERR/GNS is a strict precursor, not a conversion"* | **YES** | **YES** — **my own 800 Møller hunt found exactly this**: a derived precursor (the stable dressed outgoing-record monomorphism + GNS completion) and an absent target, with the same files saying so unprompted | **REAL** |

**All three are real boundaries. None is a reading artifact.** Notably, two of the three I
independently established in earlier relays without reference to 810 — which is the strongest form
of corroboration available here, since it is not a re-reading of the subject.

```text
CLASSIFICATION_SPOTCHECK = confirmed (one precision: DERIVABLE-FORCED is determinacy, not
   guaranteed admissibility; all three undecidables REAL and independently corroborated).
```

---

## 5. FREEDOMS CONSUMED, FLATTENING CHECK

### 5.1 `FREEDOMS_CONSUMED` (law 2a)

| datum | tag |
|---|---|
| intrinsic `Vol_4` | **CARRIED AS UNIQUELY CLASSIFIED** — no alternate measure, no rescaling |
| `delta_K'` / `mu_K'` | **VERIFIED AS IDENTITY, NOT ADOPTED** — I check a conversion; I bind no member |
| `d_g` | **VERIFIED AS FORCED, NOT CONSTRUCTED** — the aggregation is re-derived, the arrow not authored |
| `f_g`, `F_g`, `eta_resp` | **CARRIED AS ABSENT** — no substitute proposed |
| `s_g`, `S_g` | **CARRIED AS 810's FORCED RECIPES**, not executed |
| the B1a family | **CARRIED WHOLE** — nothing here selects a point in it |
| the parent frame / cell shapes | **CARRIED AS THE SEALED INSTANCES** (unit 4-cube, its bisection, its order-simplex subdivision) |
| scaling weights (law 2a) | **NONE CONSUMED** |
| smooth constituent | **NOT CONSUMED; BARRED (S26)** |

**SUBSTITUTED: none.**

### 5.2 `FLATTENING_CHECK` — `DECLINE_REGISTER_V002` (S01–S37)

```text
S26  C_ref barred as a source        CLEAN — and LOAD-BEARING in 810's f_g reason, correctly used:
     a cellular map may not be relabelled as the physical map.  I import nothing smooth.
S08  no EM / Maxwell / smooth-field  CLEAN — the density is finite, cell-intrinsic, record-side.
S28  the free data unselected        CLEAN — the unique measure denotation is not a selector on
     the B1a family, and I select nothing.
S24  clustering axiom BARRED         CLEAN — no undecidable is rescued by reaching for an axiom;
     all three are confirmed absent rather than bridged.
Remaining rows untouched.  FLATTENING_CHECK = clean (37 walked; 4 live, all discharged).
```

---

## 6. JURISDICTION AND VERB AUDIT

**Jurisdiction.** *What was the rule written to protect?* Builder-never-verifies, with downstream
work about to consume these claims. *Does the outcome space distinguish confirmation from
rubber-stamping?* Yes — I mounted a specific refutation (the unit-class attack), reported that it
failed and on which sentence, and returned one scope correction plus one custody observation rather
than a bare CONFIRMED. *Would evidence look different if the re-type were unlicensed?* Yes:
`WHERE` would not put `Dens_R` and `Cof_R` in one declared unit class.

**VOID CONDITION.** Nothing adopted, no member bound, no diagnostic run.

**Builder independence.** No `evaluator_build_A/` or `checks/` file read. `~/.codex` untouched;
`memory-bank` never searched.

### 6.1 Self verb audit — **NOT CLEAN: two disclosures**

1. **My refutation attempt failed, and I report the attempt as well as the failure.** The
   unit-class attack was the strongest available and I expected it to land: `CurrentDomain(delta_K)
   = Curr(K)` genuinely looks like a current density. It failed on `WHERE`'s pairing of `mu` with
   the coframe in one declared unit class. **A cross-check that only reports its successes is not a
   cross-check**, so the dead attack is on the page.
2. **Two of my three AS4 corroborations are my own prior findings**, and that cuts both ways. It is
   the strongest corroboration available — independently established before 810 existed, without
   reference to it. It is also **not independent of me**: if my 798 index-gap finding or my 800
   Møller finding were wrong, `F_g` and `eta_resp` would inherit the error. I state the dependency
   rather than present three unrelated confirmations.

*Direction check:* neither disclosure flatters the verdict. The chain is confirmed, and the two
things I add — a forcing mechanism weaker than its label, and a scope wall retired by the wrong
authority — both cut against the subject rather than for it.

---

```text
RETYPE = CONFIRMED (license verified).  The decisive licence is WHERE [11067,11566) sha
   f1236e38f976dc01…: "e_G = f_R^* e_G' on the old image, mu_G = f_R^* mu_G' on the old image,
   (B1-14) and mu_G' is positive.  Cof_R and Dens_R are the induced operators in the already
   declared R4 unit classes.  Their duality square commutes; no scale or frame is selected."
   Dens_R's carrier IS mu — the measure — so delta is what currents are normalized AGAINST, not a
   current density.  MY UNIT-CLASS REFUTATION ATTEMPT (a current density cannot equal a volume)
   THEREFORE FAILED, on that sentence.  MEAS-ADD [1517,2544) sha 9bffbe45a47285c2… adds "ZERO
   PHYSICS CHOICE: no new measure, weight, normalization or convention is introduced", which
   settles the VolNorm reading against the reciprocal-density alternative.  NO SEALED SENTENCE IS
   EXCEEDED: 793's "refining that sort would author the very object the build is meant to locate"
   is not violated, because 811 authors nothing — it identifies the slot with an already-classified
   measure and removes a name.
   CUSTODY OBSERVATION, flagged not adjudicated: 811 retires DS2, a scope wall 793 declared
   deliberately, in its own final lines.  The substance is licensed; RETIRING ANOTHER LANE'S
   DECLARED SCOPE IS REGISTRAR-SHAPED, and a wall a lane can retire is a weaker instrument than one
   only the registrar can.
IDENTIFICATION = CONFIRMED identity.  811's citation of my own 806 verified: file sha matches its
   pin, span [727,2831) sha d1f9f3157beb1105… does display mu_K' among the four supplied and
   delta_K'/d_g among the six absent — no misquotation.  The three trap classes checked
   individually: NORMALIZATION clean (MEAS-ADD's zero-choice clause); BASIS clean (nothing is
   expressed in a chosen basis, so the 804 trap cannot arise); VARIANCE REAL AND NAMED BY 811 —
   WHERE's law is a pullback, 793's arrow is forward, and 811 reconciles by restricting to the
   canonical slice rather than inventing an inverse, which is legitimate but consumes the
   singleton-ness and so inherits the re-type as a precondition.
D_G = CONFIRMED forced (re-derived), WITH A SCOPE CORRECTION.  Re-derived independently in exact
   rationals on A0 (1 x 1), A1 (16 x 1/16), A2 (24 x 1/24) and BOTH composite orders
   (384 x 1/384) — all five aggregate to the parent exactly, and both composite paths agree.
   CORRECTION: d_g is FORCED BY SINGLETON-NESS, NOT BY A DERIVATION — the sharp type makes
   R4Dens_sharp(K) a one-element set and a map between one-element sets is unique.  Answer to the
   relay's question: PINNED, not selected — 811 chose among nothing, because nothing remained.  But
   "DERIVABLE-FORCED" reads as though an argument produced the arrow; the forcing is INHERITED from
   AS1 and would narrow with it.  The substantive content is the aggregation check, which could
   have failed and did not.
CLASSIFICATION_SPOTCHECK = confirmed, with one precision.  s_g/S_g's pinning argument is SOUND: a
   linear map is determined by its values on a basis, boundary intertwining is then a constraint
   rather than a choice, and a restriction of a determined map is determined.  PRECISION:
   DETERMINED IS NOT ADMISSIBLE — 793 requires S_g injective and current-preserving, which are
   checks that can FAIL; 810 is honest ("fixes the ... checks"), but DERIVABLE-FORCED must not be
   read downstream as WILL-SUCCEED.  THE THREE UNDECIDABLES ARE ALL REAL, none a reading artifact,
   each record-voiced AND hunt-surviving: f_g (S26-voiced; my 773 hunt over 2,952 files and 792's
   sweep found no bridge); F_g (my OWN 792/798 exhaustion-vs-refinement index gap, and my 798 hunt
   found no object relating the two index categories); eta_resp (my OWN 800 Moller hunt found
   exactly this shape — a derived precursor and an absent target, the sealed files saying so
   unprompted).
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+2): (1) MY REFUTATION ATTEMPT FAILED AND I REPORT THE ATTEMPT AS WELL
   AS THE FAILURE — the unit-class attack was the strongest available and I expected it to land,
   since CurrentDomain(delta_K) = Curr(K) genuinely reads as a current density; a cross-check that
   reports only its successes is not a cross-check; (2) TWO OF MY THREE AS4 CORROBORATIONS ARE MY
   OWN PRIOR FINDINGS (798's index gap for F_g, 800's Moller hunt for eta_resp) — the strongest
   corroboration available, established before 810 existed and without reference to it, but NOT
   INDEPENDENT OF ME: if those findings were wrong, F_g and eta_resp inherit the error.  Stated
   rather than presented as three unrelated confirmations.
   Neither disclosure flatters the verdict; the two things I add — a forcing mechanism weaker than
   its label, and a scope wall retired by the wrong authority — both cut against the subject.
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
