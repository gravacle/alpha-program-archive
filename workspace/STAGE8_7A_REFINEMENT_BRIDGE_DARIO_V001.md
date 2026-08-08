# STAGE 8 / 7A / STEP 8 — THE REFINEMENT BRIDGE: `F` UNDER SUBDIVISION

**Lane:** Dario (Opus 5, cross-family from the Codex build lanes)
**Date:** 2026-08-08
**Scope:** PASTE 729 only — NN1 assemble, NN2 derive, NN3 lens, NN4 attest
**Custody:** archive-side read and write; the registrar owns any mirror
**Governing:** built index `66f078ba…`; `DECISION_CORRECTION_FC1_TRANSPORT_2026-08-08.md`
`72894c1c…`; frozen prereg `9f0d12b4…`; PE-1 of record at zero weight
**Charge:** re-derive, not trust. Nothing adopted.

## Lead determination

```text
SUBDIVISION = UNDERDETERMINED, and the free datum is NOT where the relay's own
              framing (or my 727 framing) put it.

F's definition DOES say what F is on a sub-face -- F = d_1 a, and d_1's formula
applies verbatim to any face of any complex.  So the gap is not "the definition
is silent about sub-faces."  It is one level DOWN and on a different object:

  THE FREE DATUM: the 1-cochain `a` on the NEW INTERIOR EDGES a subdivision
  creates -- edges with no parent, whose values `a` does not constrain and
  which are not pure gauge.

AND THE SHAPE OF THE FREEDOM IS EXACT.  For a face subdivided into k sub-faces:
  * the SUM of the sub-face fluxes is fixed by the parent (interior edges cancel
    by opposite incidence);
  * the INDIVIDUAL sub-face fluxes carry k-1 free parameters.
The measure is V_cell * sum F^2 -- QUADRATIC.  A quadratic form is not
determined by the linear total.  So the linear functional transports and the
measure does not, on the same k-1 parameters.

THAT IS WHY T11's GAP IS REAL AND WHY IT LOOKED CLOSED.  Flux adds; the measure
squares.

CORRECTION I MADE MID-DERIVATION: I first located the freedom in the SPLIT of
the parent's boundary edges.  That split is PURE GAUGE -- d_1 d_0 = 0 kills it,
sealed at [44595,44690) -- so it cannot move any flux.  The real freedom is on
interior edges.  §2.4 records the correction rather than the tidy first answer.

DIVERGENCE_NOTE = none.  No scale-dependent structure surfaced; an
underdetermination is not a divergence, and typing it as one would be the
fitter's move Requirement 5 explicitly warns against.
```

---

## 0. Preflight

[PROVABLE] `relay_outbox/729_ACK.md` was written **before** source work. Lane guard:
the header names **DARIO**. Read only after its sidecar verified:

```text
relay_inbox/RELAY_PASTE_729_REFINEMENT_BRIDGE_DARIO_V001.md
  587aae713f8295fd9e0d8ce3c0fc36549c09db5234f02ef76067ff89609bfbd2   shasum -c OK
```

[PROVABLE] `STAGE8_7A_REFINEMENT_BRIDGE_DARIO_V001.md` and its seal sidecar were probed
before the write and returned ABSENT.

### 0.1 Sources verified before use

```text
CORR   supervision/DECISION_CORRECTION_FC1_TRANSPORT_2026-08-08.md  72894c1c…  sidecar OK
V011   review_packets/.../BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md aa7c6d49…
D007   BID_CONSOLIDATED_HOSTILE_AUDIT_MATRIX_V005.md                78f6bb08…
BATT   STAGE8_T7_CODEX_BATTERY_TIER2_RETURNS_V001.md                14ddfc15…
4d     STAGE8_TASK4D_STITCHING_THEOREM_GERM_INDEPENDENT_HALF_V001.md 430f0971…
727    STAGE8_7A_RA27_2_INDEX_BUILT_DARIO_V001.md                   66f078ba…  (mine)
PREREG STAGE8_7A_OBS22_RECOGNITION_PREREG_V002_FROZEN.md            9f0d12b4…  unchanged
```

[PROVABLE] The **writer-exclusion rule** was applied to every census: searches exclude
`*_DARIO_V001.md`.

### 0.2 Gates

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

No common cell formed, no junction map evaluated, no member bound, no fixed point, no
end test, **no numeric evaluation of any physical quantity**, no measured constant.
Nothing adopted. No register, plan, tracker, git action.

---

## 1. NN1 — `F`'s DEFINITION, ASSEMBLED

### 1.1 The five sealed statements

**N1 — the differentials, and the gauge identity.** `V011` `aa7c6d49…[44595,44690)`:

```text
(d_0 lambda)_e=lambda_t-lambda_s,
(d_1 a)_f=sum_(e in boundary f) incidence(f,e)a_e,
d_1 d_0=0.
```

**N2 — the physical flux space.** `V011` `aa7c6d49…[44801,44955)`:

```text
ker(d_0)=span{constant function on K^(j)}_j,
P_h=I-d_0(d_0^dagger d_0)^+d_0^dagger,
F_phys=im(d_1),
Q_flux=P_h d_1^dagger(d_1 P_h d_1^dagger)^+|_(F_phys).
```

**N3 — uniqueness of the lift, and the exclusion.** `V011` `aa7c6d49…[44961,45186)`:

```text
For every `xi in F_phys`, `Q_flux xi` is the unique horizontal,
minimum-norm lift orthogonal to
`ker(d_1) intersect im(d_0)^perp`. It obeys
`d_1 Q_flux xi=xi`. Individual unit faces outside `F_phys` are never assigned
a lift.
```

**N4 — the response is a functional on `F_phys`.** `V011` `aa7c6d49…[45361,45440)`:

```text
mathcal_K_L(xi,zeta)
  = R_record,L(Q_flux xi,Q_flux zeta),  xi,zeta in F_phys.
```

**N5 — the coordinate-flux / frame relation, with its remainder.** `V011`
`aa7c6d49…[45848,45901)`:

```text
xi_(mu nu)=ell_mu ell_nu F_(mu nu)+higher-order terms
```

[PROVABLE] Corroborated independently in the criteria: `D007` `78f6bb08…[11161,11438)`,
A26, states `F_phys=im(d1)` and that *"individual unit faces outside that image are not
assigned a lift."*

```text
F_DEFINITION = 5 statements assembled (N1-N5), all block-covered,
               plus the independent A26 corroboration.
```

### 1.2 What `F` IS — the question NN1 asks

```text
F is a DERIVED FUNCTIONAL.

  NOT a primitive per-face datum:  N2/N3 restrict the physical fluxes to
  im(d_1), and N3 says faces outside that image are never assigned a lift.
  A free per-face value would make F_phys the whole 2-cochain space.

  NOT the restriction of something global:  N1 builds it upward from edge
  data, face by face, through a local incidence sum.

  IT IS:  xi_f = (d_1 a)_f = sum_(e in boundary f) incidence(f,e) a_e,
  the coboundary of a 1-cochain `a` on EDGES, and gauge-invariant because
  d_1 d_0 = 0.  `F_(mu nu)` is its orthonormal-frame expression, N5, to
  leading order.
```

[YOURS] This already answers half of NN2's preamble. The relay says *"F's SEALED
DEFINITION must SAY what F is on a sub-face, or say nothing."* **It says.** `d_1`'s
formula is stated for a general face of a general complex; applied to a sub-face it
gives that sub-face's flux without ambiguity. The definition is not silent. What is
silent is what `a` equals on the edges the subdivision creates — and that is a
different object.

---

## 2. NN2 — THE SUBDIVISION QUESTION, DERIVED

### 2.1 The question, restated precisely

For a licensed move (cubical bisection; oriented simplicial/barycentric subdivision)
taking face `f` to sub-faces `f_1 … f_k`:

```text
xi'_(f_i) = sum_(e' in boundary f_i) incidence(f_i,e') a'_(e')      [N1, verbatim]
```

So `xi'` on every sub-face is **determined by `a'`**. The whole question is therefore:
**what is `a'` on the refined edges?**

### 2.2 The boundary-edge split is pure gauge — it moves nothing

[PART-PROVABLE] Subdividing a parent edge `e` at a new vertex `v` produces `e'_1, e'_2`
with the configuration constrained by `a'_(e'_1) + a'_(e'_2) = a_e`. The residual
one-parameter freedom is exactly a gauge transformation at `v`: by N1,
`(d_0 lambda)_e = lambda_t − lambda_s`, so `lambda_v` shifts the two sub-edge values
oppositely and leaves every other edge alone.

[PROVABLE] And `d_1 d_0 = 0` (N1) makes `xi' = d_1 a'` invariant under it.

[YOURS] **So this freedom cannot move any flux.** It is the tidy answer and it is the
wrong one; §2.4 records that I reached for it first.

### 2.3 The interior edges are the free datum — and the count is exact

[YOURS] A subdivision that produces `k` sub-faces from one face necessarily creates
**interior edges** — edges lying inside `f`, with no parent edge in `K`. `a` says
nothing about them; N1 constrains `a'` only through the incidence sums, and no parent
value bounds an interior edge. Their values are not pure gauge either: gauge at the new
interior vertices absorbs only part of the freedom, because gauge is one parameter per
vertex while the interior edges are more numerous.

[PART-PROVABLE] The exact shape of what survives:

```text
CONSTRAINED   sum_(i=1..k) xi'_(f_i)  =  xi_f
              Every interior edge is shared by exactly two sub-faces and enters
              their incidence sums with opposite sign (N1's incidence(f,e)), so
              interior contributions cancel and only the parent's boundary
              survives.  THE TOTAL FLUX TRANSPORTS.

FREE          k - 1 independent parameters, distributing xi_f among the k
              sub-faces.  One linear constraint on k values leaves k-1 free,
              and the interior-edge degrees of freedom modulo gauge supply
              exactly that many.
```

[YOURS] I mark the cancellation PART-PROVABLE and not PROVABLE: it follows from N1's
incidence sum applied to a subdivided face **given that the subdivision carries the
standard incidence data**, which is the defining property of a subdivision but is not
separately sealed in the bytes I have. If the registrar wants it airtight, that is the
one line to seal.

### 2.4 Why this defeats the measure — and only the measure

[PROVABLE] The object that must transport is `V_cell · sum_(mu<nu) F_(mu nu)^2`
(`BATT`/`V011`, and 727 §2). It is **quadratic** in `F`.

[YOURS] The derivation's whole content is the mismatch between the two functionals:

```text
LINEAR      sum_i xi'_(f_i)          determined by the parent.        TRANSPORTS.
QUADRATIC   sum_i (xi'_(f_i))^2      NOT determined -- it varies over the
                                     k-1 free parameters at fixed total.
```

A quadratic form is not a function of the sum of its arguments. So the same `k−1`
parameters that leave the flux alone move the measure. **The measure's refinement
functoriality is therefore not derivable from `F`'s definition — not because the
definition is silent, but because it fixes a linear total and the measure asks a
quadratic question.**

[YOURS] This is also why the gap looked closed for so long, including to me at 725:
*"flux adds"* is true and is the thing everyone checks. The measure squares.

[YOURS] **The correction I made mid-derivation, recorded rather than smoothed away.**
My first location for the free datum was the boundary-edge split — the natural reading,
and the one my 727 framing (*"a rule assigning `F` on sub-faces"*) points at. §2.2 shows
it is pure gauge and moves nothing. Had I stopped there I would have reported a free
datum that cannot affect the answer, which would have sent a repair at the wrong object.
The interior edges are the real locus.

### 2.5 Nothing supplies the missing datum

[PROVABLE] SEARCHED SPACE: `workspace/` + `supervision/`, `*.md`, recursive,
**writer-excluded**. Probes: `sub-edge` **0 files**; `subdivided edge` **0**;
`holonomy split` **0**; `splits the holonomy` **0**; `subedge` 2; `edge subdivision` 1;
`connection cochain` 1. Every non-zero carrier was opened; none assigns the 1-cochain on
edges a subdivision creates. `D007`'s A24 does say the source-decorated incidence family
must *include* `edge refinements` — a demand that a competitor family be exhaustive, not
a rule assigning `a'`.

### 2.6 The verdict

```text
SUBDIVISION = UNDERDETERMINED

FREE DATUM, named exactly:
  the 1-cochain `a` on the interior edges created by a licensed move --
  equivalently, the distribution of the parent face's flux among its k
  sub-faces, k-1 parameters, at fixed total.

SMALLEST SEALED ADDITION THAT WOULD DETERMINE IT:
  a connection-refinement rule -- an assignment of `a'` on interior edges from
  `a` and the cell data.  Once `a'` is fixed, xi' is FORCED by N1 with no
  further freedom, and the functoriality of V_cell * sum F^2 becomes a
  decidable question rather than an open one.
  NOTHING IS ADOPTED HERE.  I do not propose a rule, and I note that the
  obvious candidates (equidistribution; proportional-to-area) are exactly the
  kind of choice the R4-kernel void condition governs.

NOT OBSTRUCTED:  nothing in sealed text makes the assignment impossible or
  inconsistent.  The definition admits many extensions; it selects none.
```

---

## 3. NN3 — THE K-1/K-3 LENS, AT ZERO ADOPTION

[PROVABLE] Requirement 5, frozen at `9f0d12b4…` §5A, binds two halves: *"MEASURE, DON'T
HALT"* and *"AND A PRE-STATED WAY TO LOSE"*, the second because *"'the divergence is the
signal' is ALSO THE FITTER'S MOVE."* K-1 is the coefficient class; K-2 is the
**named-open slot, not in the frozen kill set**; K-3 is the locus.

```text
DIVERGENCE_NOTE = none.
```

[YOURS] Applying the lens honestly means saying when it does not fit. **No
scale-dependent structure surfaced here.** What §2 produces is an *underdetermination* —
a `k−1`-parameter family of admissible values — not a divergence: no quantity was
computed, nothing runs in a variable, and there is no coefficient to place in a class.
Recording an underdetermination under K-1/K-3 would be typing a missing datum as a
physical signal, which is precisely the fitter's move the requirement's second half
exists to bar.

[YOURS] One adjacency recorded and explicitly **not promoted**: because the freedom sits
at each refinement step, a *chosen* subdivision scheme iterated could in principle make
`sum F^2` scheme-dependent in the limit — which is the refinement-dependence `BATT`
names as the failure mode. That is a **conditional** about an object nobody has built,
on a rule nobody has adopted. It is not a measurement, it does not enter the K-axes, and
I decline to compute it — doing so would require both an adopted rule and a downstream
evaluation the void condition bars.

### 3.1 Correspondence ledger (verdict weight = 0)

| # | Encountered at | Classical likeness | Weight |
|---|---|---|---|
| L1 | `F = d_1 a` with `d_1 d_0 = 0`; boundary splits pure gauge | a lattice gauge field: plaquette curvature from link variables, link splits absorbed by gauge at the new site | 0 |
| L2 | total flux transports, the quadratic does not | a conserved charge surviving coarse-graining while its variance does not | 0 |
| L3 | `k−1` free parameters at fixed sum | the standard defect of reconstructing a distribution from its total | 0 |
| L4 | scheme-dependence of a quadratic under iterated refinement | anomaly/running structures, where a regularization choice survives in the limit | 0 |

[YOURS] L4 is the seductive one and is the reason §3 says `none` rather than reaching
for the K-axes. The resemblance is to a *computed* running structure; what I have is an
*uncomputed* freedom. Logging it is where it belongs; promoting it would be the move
Requirement 5 pre-names.

---

## 4. NN4 — VOID ATTESTATION

```text
VOID = CLEAN

No downstream numeric was consulted, computed, or estimated at any point.
Specifically:
  -- no coefficient, response value, or alpha-facing quantity was read;
  -- the k-1 freedom is reported as a COUNT of parameters, never evaluated;
  -- no subdivision scheme was chosen, and §2.6 names the obvious candidates
     only to flag them as governed by the void condition, not to weigh them;
  -- §3's adjacency is left as a conditional and expressly not computed.
No candidate rule was preferred, and the derivation's direction was fixed by
F's definition before any consequence was considered.
```

---

## 5. GROUNDING, JURISDICTION, VERB AUDIT

### 5.1 Grounding

| # | Step | Source + span | Tag |
|---|---|---|---|
| 1 | The correction's content | `72894c1c…` (sidecar OK) | PROVABLE |
| 2 | N1 differentials; `d_1 d_0 = 0` | `aa7c6d49…[44595,44690)` | PROVABLE |
| 3 | N2 `F_phys = im(d_1)`; `Q_flux` | `aa7c6d49…[44801,44955)` | PROVABLE |
| 4 | N3 unique lift; faces outside get none | `aa7c6d49…[44961,45186)` | PROVABLE |
| 5 | N4 response is a functional on `F_phys` | `aa7c6d49…[45361,45440)` | PROVABLE |
| 6 | N5 `xi`↔`F` with remainder | `aa7c6d49…[45848,45901)` | PROVABLE |
| 7 | A26 corroborates `F_phys=im(d1)` | `78f6bb08…[11161,11438)` | PROVABLE |
| 8 | `F` is a derived functional, not a face primitive | §1.2, from 2–4, 7 | PART-PROVABLE |
| 9 | `xi'` on a sub-face is determined by `a'` | §2.1, N1 applied verbatim | PROVABLE |
| 10 | Boundary-edge split is pure gauge | §2.2, from 2 | PART-PROVABLE |
| 11 | Interior-edge values are unconstrained by `a` | §2.3 | PART-PROVABLE |
| 12 | Total flux transports (interior cancellation) | §2.3 — proviso stated | PART-PROVABLE |
| 13 | `k−1` free parameters at fixed total | §2.3 | PART-PROVABLE |
| 14 | The measure is quadratic; quadratic ≠ function of the sum | §2.4 | PART-PROVABLE |
| 15 | Nothing supplies the sub-edge rule | §2.5, writer-excluded counts | PROVABLE |
| 16 | Verdict UNDERDETERMINED, not OBSTRUCTED | §2.6 | PART-PROVABLE |
| 17 | The smallest sealed addition | §2.6 | **YOURS** |
| 18 | `DIVERGENCE_NOTE = none` | §3 | **YOURS** |
| 19 | The mid-derivation correction | §2.4 | **YOURS** |

```text
GROUNDED_STEPS = 16 / 19
YOURS, NAMED: 17, 18, 19.  None is a premise for any PROVABLE row.
```

### 5.2 Jurisdiction check

**Requirement 5.** Written so a divergence is measured rather than halted on, *and* so
"the divergence is the signal" cannot become unfalsifiable. Present in the sense that
the relay invited the lens; §3 declines it because an underdetermination is not a
divergence. The requirement's outcome space distinguishes false from cannot-see, and I
used it in the direction it was written — as a bar on promotion, not as licence.

**The R4-kernel void condition.** Present the moment a subdivision rule is contemplated.
§2.6 names candidate rules only to mark them as governed by it, and adopts none. §4
attests.

**`d_1 d_0 = 0`.** Applied strictly inside its jurisdiction — it kills the boundary
split (§2.2) and is *not* stretched to cover the interior edges, which is exactly the
over-reach that would have produced a false DETERMINED.

**DoR-007 and the TYPE-R bars.** Untouched. Nothing smooth imported; no formal generator
substituted; no refinement bridge authored.

**R9 / R9-JII.** Unchanged and not advanced. This artifact derives a property of `F`; it
forms no common cell and does not touch the carrier's PENDING quantifier.

### 5.3 Self verb audit

| Verb or status | Warrant |
|---|---|
| `derived functional` | N1–N4 and A26; the two alternatives excluded by N3's own words |
| `pure gauge` | `d_0`'s formula and `d_1 d_0 = 0`, N1 |
| `UNDERDETERMINED` | the free datum named as an object, with its parameter count |
| `NOT OBSTRUCTED` | nothing in sealed text forbids an extension; many exist, none selected |
| `none` (divergence) | the lens applied and declined, with the reason stated |
| PART-PROVABLE on §2.3 | the incidence-cancellation proviso is stated, not hidden |

[YOURS] Disclosures against myself:

1. **My first answer was the tidy one and it was wrong.** I located the free datum in
   the split of the parent's boundary edges. That split is pure gauge and moves no flux.
   Reporting it would have aimed a repair at an object that cannot affect the result.
   §2.2/§2.4 record the correction; the interior edges are the locus.
2. **My 727 framing pointed at the wrong object too**, and the relay inherited it: *"a
   rule assigning `F` on sub-faces"*. `F` on a sub-face is forced by `d_1` once `a'` is
   known. The missing rule is about `a` on interior edges — one level down, and on
   edges rather than faces.
3. **§2.3's cancellation is PART-PROVABLE, not PROVABLE.** It needs the subdivision to
   carry the standard incidence data. That is what a subdivision *is*, but I did not
   find it sealed, and I would rather flag one line than let a structural convenience
   pass as a citation.
4. **I declined the K-axes on a result that would have looked stronger inside them.**
   "Refinement-dependence surfaced, measured under K-1/K-3" is a more impressive
   sentence than "no divergence surfaced". It would also have typed a missing datum as
   a physical signal, which Requirement 5 pre-names as the fitter's move.
5. No verb here proves, authorizes, computes, binds a member, forms a common cell,
   evaluates a junction map, adopts a rule, or grants a seal.

```text
F_DEFINITION = assembled (5 statements N1-N5, block-covered; A26 corroboration)
SUBDIVISION = UNDERDETERMINED — free datum named: the 1-cochain on the INTERIOR
    edges a licensed move creates (equivalently, the distribution of the parent
    face's flux among k sub-faces, k-1 parameters at fixed total). The boundary-edge
    split is pure gauge and moves nothing (d_1 d_0 = 0). The total flux TRANSPORTS;
    the measure V_cell*sum F^2 is QUADRATIC and does not. Smallest sealed addition:
    a connection-refinement rule on interior edges — NOT adopted. Not OBSTRUCTED.
DIVERGENCE_NOTE = none (lens applied and declined; adjacency logged at L4, not promoted)
LEDGER_ENTRIES = 4
VOID = clean
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+5 disclosures at §5.3)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
