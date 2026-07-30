# THE STITCHING RULE IS NOT MISSING — IT IS TWO NAMED COHERENCE CONDITIONS ON AN ALREADY-FORCED MEASURE

Reviewer lane, 2026-07-30. Nothing derived here; this is a re-typing of an obligation the corpus has
carried as "absent" since 2026-07-27. No value computed.

## 1. WHAT THE PROHIBITION SAYS

`ABSOLUTE_STIFFNESS_SELECTOR_ROUTE_LEDGER_V003.md:116-126`, failure rule, sealed — the route fails if
"**a finite-cell answer is called physical without a derived stitching or continuum rule.**"

That has been carried as a missing continuum principle, and Q-22 named it as the blocker on the one
condition class that could fix the small-`s` end (a total finite triple, rank 1). It is the object I said
this morning had "two independent consumers."

**IT HAS A THIRD, AND THE THIRD ONE SHOWS WHAT IT ACTUALLY IS.**

## 2. THE MEASURE IS ALREADY DERIVED, AND THE CORPUS SAYS IT IS FORCED

`STAGE8_T7_CODEX_BATTERY_TIER2_RETURNS_V001.md:86-97`, DERIVED, verbatim:

```
<xi, xi>_(2,ell) = sum_(mu<nu) V_cell / (ell_mu^2 ell_nu^2) xi_(mu nu)^2
xi_(mu nu) = ell_mu ell_nu F_(mu nu)
each cell contributes  V_cell sum F^2
general coframe = pullback by wedge^2(e^-1) times |det e|
NO inverse weight, NO ad hoc weight, NO residual shape scalar — which is
the substantive content: the measure is forced, not chosen.
```

**Two things follow that the "no stitching rule" framing hides.** The per-cell contribution is already in
additive, extensive form — `V_cell sum F^2` — which is what a density looks like. And the transformation
under a general coframe is already a **pullback**, `wedge^2(e^-1) |det e|`, which is exactly the
naturality law a measure needs. **The measure's own stitching is done.**

## 3. WHAT IS ACTUALLY MISSING, AND IT IS TWO NAMED OBJECTS

Same artifact, immediately after, verbatim:

```
MISSING SEALED OBJECTS (obligation, named, two of them):
    the sealed RESPONSE-MAP PULLBACK on common refinements; and
    BOUNDARY-SUBEXTENSIVE INVARIANCE over C_ref.
V011 flags cellulation_independence_proved = false.
```

Corroborated at `STAGE8_CORRECTED_STATUS_MECHANISM_OPTIONS_WITH_COSTS_V001.md:27` — "T11 needs
response-map pullback commutation + boundary-subextensive."

**So the stitching rule decomposes exactly:**

| Component | What it asserts | Status |
|---|---|---|
| the per-cell measure | `V_cell sum F^2`, coframe pullback `wedge^2(e^-1)\|det e\|` | **DERIVED AND FORCED** |
| **(i) response-map pullback on common refinements** | the RESPONSE map commutes with refinement — two cellulations with a common refinement give the same response | **MISSING, named** |
| **(ii) boundary-subextensive invariance over `C_ref`** | boundary contributions are subleading, so a bulk density exists | **MISSING, named** |

Those two are precisely the conditions under which a per-cell quantity possesses a
cellulation-independent continuum limit. **They are coherence conditions, not a new continuum
principle.**

## 4. AND ONE OF THE TWO IS ALREADY A CHARTERED OBLIGATION

**(ii) IS THE EXTENSIVITY OBLIGATION.** `STAGE8_RL2B_OVER_CHARTER_AND_BLIND_ROUTE_FINDING_V001.md:106`
states the requirement as "(ii) boundary corrections subextensive at a certified..." — the same clause,
in the R-L2b campaign's own language. And `STAGE8_RL2B_UNIFORMITY_REFUTED_RESULT_V001.md:161` lists
**CONNECTED EXTENSIVITY as the fourth of the campaign's four obligations**, which the campaign's binding
declared to be one estimate discharging four consumers.

**So boundary-subextensivity is not new work. It is R-L2b's fourth discharge, already chartered, already
attacked, and already the subject of a refuted-uniformity result.** Whatever its status, it is not an
unexamined gap.

That leaves **(i), the response-map pullback on common refinements, as the one genuinely unattacked half
of the stitching rule.**

## 5. WHY THE FRAMING MATTERED

"No derived stitching or continuum rule exists" is TRUE and has been read as *a continuum principle is
missing*. What is missing is narrower and better-posed: **the response map's naturality under refinement,
plus a subextensivity condition that is already chartered elsewhere.** The measure they would act on is
derived and forced.

This is the same defect the day has produced repeatedly — a named structure with no stated correspondence
to the quantity it governs. Here the correspondence exists for the *measure* and is missing for the
*response*. `cellulation_independence_proved = false` is the flag that says so, and it appears in only
four places.

**AND IT CONVERGES WITH BOTH LANES.** Lane 2 reports that its tier-1 families each require "regulator/
refinement and packing independence" (finite holonomy) and "the many-cell limit, long-wavelength locality,
frequency convergence, packing independence" (temporal plaquette). **Those are (i) and (ii).** So the
stitching rule is not only the blocker on Q-22's rank 1 and on every finite-cell stiffness route — it is
also the common blocker under lane 2's three tier-1 slot-18 families.

**THAT IS FOUR CONSUMERS FOR ONE PAIR OF CONDITIONS**, and the pair is half-chartered.

## 6. WHAT THIS DOES NOT ESTABLISH

- It does not prove (i) or (ii). Both remain unproved and `cellulation_independence_proved = false`.
- It does not show they are provable. F-2's prohibition on pinning the quantifier still forbids the cheap
  route of fixing a cellulation, and the R-L2b campaign already carries a refuted-uniformity result whose
  bearing on (ii) I have not assessed here.
- It does not touch the `Gamma_K` construction, which is a different object at a different stage.
- It computes nothing and adopts nothing.

## 7. WHAT I RECOMMEND

**Re-type the obligation in the tracker and the register from "no stitching rule exists" to the two named
conditions, with the measure marked DERIVED.** An obligation described as a missing principle attracts no
work; an obligation described as "prove the response map commutes with refinement" is a stated
mathematical target with a known shape.

**And check (ii)'s status against the R-L2b record before anyone attacks it fresh** — that campaign has
been over this ground, and re-deriving it would be the retracing this program keeps paying for.

`alpha_computed = false`; `proof_authorized = false`; `kappa_record_computed = false`.
