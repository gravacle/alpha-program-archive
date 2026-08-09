# STAGE 8 / 7A / [PLAN:B1a-5] — THE COFRAME HALF: THE RECORD CAN POSE THE SQUARE, AND CAN ELIMINATE — BUT NOT DECIDE

Lane: DARIO (Builder B, independent verifier). Relay 795.
State brief pinned by the relay: `PROGRAM_STATE_BRIEF_V005.md` = `e26f0d16055f3e83…` — digest
matches, seal OK, read before task work. Drift check: V005 current.
Governing: my own **788** (`97f073c101d8cf4a…`, SEALED-OK) — the incidence half delivered, the
coframe half and O1 named as not delivered. **794 judges the incidence half lane-opposite; nothing
of it is re-derived here.** All headline items **CLAIMED**.

## Lead determination — CLAIMED

**788's `ABSENT` worry was mine and it is refuted. The record-side stock can pose the coframe
square without the barred smooth constituent — and it can eliminate a candidate. It cannot decide.**

At 788 I wrote that V011's only two `coframe` occurrences are both on the **S26-barred** smooth
side and named the `F'/F` square as not deliverable. That was true of **V011** and I let it stand
for **the record**. It is not: the record-side coframe stock is my own sealed 753 — twenty-four
child frames `E_p`, derived, with `det E_p = sgn(p)`, `|det E_p| = 1`, `Vol_4 = 1/24` each — and
that stock poses the square perfectly well.

```text
THE SEALED QUADRATIC DISCRIMINATES.  V011 D10 + the classified intrinsic Vol_4:

  (a1) FORM-inheritance      F' is the same 2-form; child-frame components = wedge^2(E^-1) F
       ->  sum_children / parent  =  1.81, 1.83, 3.04, 4.01, 1.68, 4.69   *** ELIMINATED ***
           an O(1), F-DEPENDENT failure — not a boundary term with vanishing ratio.

  (a2) COMPONENT-inheritance  F'_{ab} = F_{ab} in the child's own frame
       ->  sum_children / parent  =  1.000000 every trial            *** SURVIVES EXACTLY ***
```

**That is a real record-side elimination, derived from sealed stock, with no smooth import.** It
is also the answer to whether the square can be posed at all: it can, and it has teeth.

**But it does not force a law.** The constraint is `(1/24) Σ_i M_i^T M_i = I_6` — one symmetric
`6×6` identity, **21 conditions on 864 parameters**:

```text
RESIDUAL = 864 - 21 = 843 dimensions.   The quadratic eliminates; it does not single out.
```

And a **second** complete record-side candidate survives it exactly — orientation-weighted
component inheritance `F'_i = sgn(p_i)·F`, built from 753's *derived* orientation, differing from
`(a2)` on **12 of 24** children.

```text
COFRAME_SQUARE = FREE (two candidates displayed, neither adopted; one candidate ELIMINATED).
```

**O1 is proved, with A0 constructed rather than typed** — the clause 788 left standing.

---

## 0. Preflight

```text
OUTPUT NAME  probed recursively before any write: artifact and sidecar ABSENT.
LAW 8 APPLIED (my own 792 finding, now binding): every seal probe tested ALL THREE modes —
   <name>.md.seal.sha256, <name>.seal.sha256, and packet-manifest membership.
   Relay 795 sidecar: .md.seal.sha256 OK ; .seal.sha256 absent.  753: .md.seal.sha256 OK.
753  STAGE8_7A_SIMPLICIAL_COFRAME_DARIO_V001.md   d6f490b80e8d8775…  SEALED-OK
     span [4420,6672) re-derived this relay, span sha 01a0c8dbf7dcdd37…  MATCH
788  STAGE8_B1A_REFINEMENT_CARRIER_DARIO_V001.md  97f073c101d8cf4a…  SEALED-OK
755  STAGE8_7A_SUPPORT_AND_FORCING_DARIO_V001.md  9685af44cc48f01f…  SEALED-OK
V011 sealed packet copy aa7c6d4904706276… (78,794 B) — D10 [46074,46387) sha dffd13b31d56c212…
     The workspace ROOT copy 20a3a17d… (84,987 B) is UNSEALED; offsets NOT interchangeable; unused.

GATES: alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false.
No member binding; no fixed-point execution; no end test; no numeric evaluation of physical
quantities; no comparison to measured constants.  NO SMOOTH IMPORT (S26).  NO EM IDENTIFICATION
(S08).  NO METRIC ADOPTED.  NOTHING SELECTED BY OUTCOME.  No common cell formed; no junction map
evaluated.  PE-1..PE-7 pointer-known, zero weight, not opened, not consulted.
```

---

## 1. AS1 — THE COFRAME HALF

### 1.1 The record-side stock, re-derived

753's span `[4420,6672)` (verified) gives the child frames from the coordinates alone:
`E_p` has rows `v_k − v_0` along the monotone chain in permutation order `p`; entries `0/1`;
**`det E_p = sgn(p)`, `|det E_p| = 1`, `Vol_4 = |det E_p|/4! = 1/24`, summing to `1`.**
I rebuilt all 24 independently: count, determinants, orientations and volume sum all reproduce.

V011 D10 supplies the integration map, verbatim: each cell contributes
`V_cell Σ_{μ<ν} F_{μν}²` in the local orthonormal frame; *"For a general coframe `θ^a = e^a_μ dx^μ`,
the same map is defined by pulling the bivector through `∧²(e^{-1})` and multiplying by
`|det e|`."*

**Nothing smooth is used.** `E_p` is combinatorial; `Vol_4` is the classified intrinsic measure;
`D_e` is V011's own map. S26 is untouched.

### 1.2 The square's two readings — and they are not the same thing

The square `J_2^g(D_e F) = D_{e'} F'` needs `F'` **declared**. "Inherit `F`" has two inequivalent
readings, because the child frame differs from the parent's:

```text
(a1) FORM-inheritance      : F' is the SAME 2-form.  Its child-frame components are
                             wedge^2(E_p^{-1}) F.
(a2) COMPONENT-inheritance : F'_{ab} = F_{ab} — the same numbers, read in the child's own frame.
```

Verified inequivalent on **24 of 24** children (they coincide on **0**).

### 1.3 The sealed quadratic eliminates (a1)

Displayed on the **sealed** A2 instance — the unit 4-cube with its 24 order-simplices, which is
753's own object, not a frame I chose:

| law | `Σ_i Vol_4(C'_i)‖F'_i‖² / Vol_4(C)‖F‖²` over six random `F` |
|---|---|
| **(a1)** form-inheritance | `1.813, 1.825, 3.041, 4.014, 1.682, 4.691` — **F-dependent, O(1)** |
| **(a2)** component-inheritance | `1.000000` × 6 — **exact** |

**(a1) is eliminated.** Its deviation is not a boundary term whose ratio to four-volume tends to
zero (788 §3.1's conjunct 2); it is a multiplicative O(1) error on the leading term, varying with
`F`. **A sealed requirement kills it. That is a derivation, not a preference.**

### 1.4 But the quadratic does not force a law

Writing `F'_i = M_i F`, the constraint *for all `F`* is

```text
sum_i Vol_4(C'_i) ||M_i F||^2 = Vol_4(C) ||F||^2   <=>   (1/24) sum_i M_i^T M_i = I_6
```

— one symmetric `6×6` identity, **21 independent conditions**, on `24 × 36 = 864` parameters.

```text
RESIDUAL = 843 dimensions.
```

### 1.5 A second surviving record-side candidate

```text
(b2) ORIENTATION-WEIGHTED component inheritance:  F'_i = sgn(p_i) · F
     built from 753's DERIVED orientation det E_p = sgn(p) — record-side, not authored.
     sum_children / parent = 1.000000 every trial  -> SURVIVES the quadratic EXACTLY.
     Differs from (a2) on 12 of 24 children (the odd permutations) -> INEQUIVALENT.
```

**Two complete candidates, both surviving the coframe square's own sealed constraint, neither
adopted.**

### 1.6 Scope of the FREE verdict, stated rather than assumed

```text
FREE is asserted at the level of the COFRAME SQUARE'S OWN CONSTRAINT SET (the sealed quadratic).
NOT tested here: whether (b2) survives flux conservation or naturality.  Naturality is 794's
lane by the relay's own instruction, and I do not pre-empt it.  If (b2) later fails an obligation
I have not run, the verdict narrows toward a single surviving candidate — and I say so now rather
than let a later narrowing look like a discovery.
```

---

## 2. AS2 — O1's CLAUSES, WITH A0 CONSTRUCTED

**A0 = identities + certified relabelings + ratified W3 restrictions**, and it carries **no
refinement by type**. Constructed concretely, not asserted:

```text
INSTANCE: the coordinate relabeling sigma = (1,0,3,2) of the 4-cube.
   induced edge map is a bijection of the 32 parent edges : TRUE
   sd*_1 for this generator is the permutation matrix P, |det P| = 1 : INVERTIBLE
   unique section J_1 = P^{-1};  sd*_1 J_1 = I : TRUE
   a closed parent cochain stays closed under it : TRUE
```

**Clause 1 — `L_id = id`. PROVED.** By 788's direction theorem, `sd*_1` is injective **iff** the
refinement adds no new edge **iff** `g ∈ A0`. A section of an injective surjection is **unique**,
and `I ∘ J = I` forces `J = I`. So `L_id = id` is *derived from the section structure*, not
assumed — which is what 788 left standing "by type".

**Clause 2 — per-generator existence. PROVED**, in two steps:

```text
(i)  sd*_1 is SURJECTIVE for every generator (assign a parent edge's whole value to one child),
     so a linear section exists over a field — no obstruction.
(ii) 788's corrected forcing lemma (i): sd*_1 maps ker d_1' ONTO ker d_1.  So the section can be
     chosen to satisfy the intertwining criterion J_1(ker d_1) subseteq ker d_1' — exactly the
     condition for J_2 to exist.
=>   a lift WITH its J_2 exists on every A0 / A1 / A2 generator.
```

**Composition on A0**: relabelings compose and `L_{ψ∘φ} = ψ_* φ_* = L_ψ L_φ`, by the permutation
action itself.

```text
O1 = PROVED (A0 constructed).
```

---

## 3. AS3 — THE MIN-NORM LEAD

AS3 is conditional on AS1 landing **DERIVED**. It landed **FREE**.

```text
MINNORM_BEARING = n-a.
```

[YOURS] One statement, offered as a statement and not a test: each surviving candidate induces a
**different** `J_2` via `D_{e'}F'`, hence a different `J_1` on `im(d_1)`. So the coframe half
**adds** a freedom rather than removing one, and cannot by itself pin 788 §3.3's min-norm
combination. **Whether either candidate coincides with the min-norm one is a naturality question,
and the relay assigns that test to 794. I do not run it.**

---

## 4. AS4 — FREEDOMS CONSUMED, FLATTENING CHECK

### 4.1 `FREEDOMS_CONSUMED` — item by item against the text above (law 2a in force)

| datum | tag | where |
|---|---|---|
| **the `F'/F` law** | **NOT ADOPTED** — two candidates displayed, one eliminated | §1.2–1.5 |
| child coframes `E_p` | **CARRIED AS DERIVED** (753, re-derived here) | §1.1 |
| intrinsic `Vol_4` | **CARRIED AS FORCED/CLASSIFIED** — no alternate measure | §1.3–1.4 |
| **the parent frame `e = I`** | **CARRIED AS THE SEALED INSTANCE, disclosed** — the unit 4-cube is 753's own object, not a frame I selected; the elimination in §1.3 is displayed **on that instance** and is **not claimed for every parent frame** | §1.3 |
| the orientation `det E_p = sgn(p)` | **CARRIED AS DERIVED** (753) — used to *build* candidate (b2), not to prefer it | §1.5 |
| `J_1` / the section freedom | **CARRIED AS PARAMETER** — 788's residual, untouched here | §2 |
| scaling weights (law 2a) | **NONE CONSUMED** — no `beta`-graded statement appears | — |
| a metric | **NOT ADOPTED** — the quadratic used is the sealed `Vol_4`-weighted one, not a chosen inner product | §1.3 |
| the smooth `C_ref` constituent | **NOT CONSUMED; BARRED (S26)** | not invoked |

**SUBSTITUTED: none** — audited line-by-line against §1–§2, and the one instance choice that could
have been invisible (`e = I`) is disclosed above with its scope.

### 4.2 `FLATTENING_CHECK` — against `DECLINE_REGISTER_V002` (S01–S37)

```text
S26  C_ref barred as a source                                        LIVE, CLEAN.
     The entire coframe half is built from 753's combinatorial child frames, V011's D10 map and
     the classified Vol_4.  The smooth same-coframe-and-connection clause supplies NO step, and
     is mentioned only to record that 788's ABSENT worry rested on V011's smooth-side occurrences
     rather than on the record-side stock.
S08  no EM / smooth-field / Maxwell / response identification        CLEAN — F is treated as a
     local frame two-form in V011's own sense; no physical field reading.
S27, S28, S01 and the remaining rows: not touched.
FLATTENING_CHECK = clean (37 rows walked; 2 live, both discharged).
```

---

## 5. JURISDICTION AND VERB AUDIT

**Jurisdiction.** *What was the rule written to protect?* AS1's three-way option exists so a lane
cannot report ABSENT when the stock is merely elsewhere. The risk was live — **I had already
reported it at 788**. *Does the outcome space distinguish a real result from a preference?* Yes:
(a1) is eliminated by a sealed requirement with numbers on the page, and (a2)/(b2) are left
undecided with the residual dimension stated. *Would evidence look different if ABSENT were right?*
Yes: 753's frames would not suffice to evaluate the quadratic. They do.

**VOID CONDITION.** No `F'/F` law adopted. (b2) is built from derived orientation data
specifically so that the second candidate is record-side rather than authored; it is displayed to
demonstrate freedom, not because it is attractive.

**BR-1.** The relay authorises finishing the remainder; it does not authorise the result. §1 runs
against my own 788.

**Builder independence.** No `evaluator_build_A/` or `checks/` file read. 794 runs lane-opposite
on the incidence half and **nothing of it is re-derived here**. `~/.codex` untouched;
`memory-bank` never searched.

### 5.1 Self verb audit — **NOT CLEAN: three disclosures**

1. **788's ABSENT worry was mine, and it was a search failure, not a record fact.** I checked
   V011, found both `coframe` occurrences on the barred smooth side, and let that stand for the
   record — when the record-side coframe stock is **my own sealed 753**, cited in the same
   artifact. *I under-searched a question I had the answer to, in a file I wrote.*
2. **"FREE" is scoped and I state the scope before it can be mistaken.** Two candidates survive the
   **coframe square's own** constraint; neither has been run against flux conservation or
   naturality. If (b2) later fails, the verdict narrows — and I record that now so a later
   narrowing is not read as a new discovery.
3. **I nearly made an invisible instance substitution.** §1.3's elimination is computed on the unit
   4-cube with `e = I`. That is 753's sealed object rather than a choice of mine — but the
   distinction is exactly the one 781/784/789 got wrong, so it is disclosed in the freedoms block
   with its scope, and the elimination is **not** claimed for every parent frame.

*Direction check:* all three run against my own work. The one result that flatters this relay — a
genuine record-side elimination — is immediately bounded by §1.4's 843-dimensional residual, which
is the number that stops it from being a closure.

---

```text
COFRAME_SQUARE = FREE (two candidates displayed, neither adopted).
   788's ABSENT worry is REFUTED: the record-side stock POSES the square without the S26-barred
   smooth constituent, using 753's derived child frames (E_p, det E_p = sgn(p), |det E_p| = 1,
   Vol_4 = 1/24 each — span [4420,6672) re-derived, sha 01a0c8dbf7dcdd37 MATCH), V011 D10's
   integration map, and the classified intrinsic Vol_4.
   ELIMINATED BY SEALED STOCK: (a1) FORM-inheritance (F' the same 2-form; child-frame components
   wedge^2(E_p^{-1})F) fails the intrinsic-Vol_4 quadratic by an O(1), F-DEPENDENT factor
   (children/parent = 1.813, 1.825, 3.041, 4.014, 1.682, 4.691) — not a boundary term with
   vanishing ratio.  A sealed requirement kills it; this is a derivation, not a preference.
   SURVIVING, DISPLAYED, NEITHER ADOPTED: (a2) COMPONENT-inheritance F'_{ab} = F_{ab} (ratio
   1.000000 every trial) and (b2) ORIENTATION-WEIGHTED component inheritance F'_i = sgn(p_i)F,
   built from 753's derived orientation (ratio 1.000000 every trial), differing from (a2) on 12
   of 24 children.  The two readings of "inherit F" are inequivalent on 24 of 24 children.
   NOT FORCED: the constraint is (1/24) sum_i M_i^T M_i = I_6 — one symmetric 6x6 identity, 21
   conditions on 864 parameters, RESIDUAL 843 DIMENSIONS.  The quadratic eliminates; it does not
   single out.
   SCOPE STATED: FREE is asserted at the level of the coframe square's OWN constraint set.
   Whether (b2) survives flux conservation or naturality is NOT tested here — naturality is 794's
   lane by the relay's instruction — and if (b2) later fails, the verdict narrows.
O1 = PROVED (A0 constructed).  A0 built concretely as the coordinate relabeling sigma = (1,0,3,2):
   induced edge map a bijection of the 32 parent edges; sd*_1 the permutation matrix P with
   |det P| = 1; unique section J_1 = P^{-1} verified; closed cochains stay closed.
   CLAUSE 1, L_id = id: by 788's direction theorem sd*_1 is injective iff no new edge iff g in A0;
   a section of an injective surjection is UNIQUE and I.J = I forces J = I.  DERIVED from the
   section structure, not assumed by type.
   CLAUSE 2, per-generator existence: (i) sd*_1 is surjective for every generator so a linear
   section exists over a field; (ii) 788's corrected forcing lemma (i) gives sd*_1(ker d_1') =
   ker d_1, so the section can be chosen to satisfy J_1(ker d_1) subseteq ker d_1' — exactly the
   condition for J_2 to exist.  A lift WITH its J_2 exists on every A0/A1/A2 generator.
   COMPOSITION on A0 holds by the permutation action: L_(psi.phi) = psi_* phi_* = L_psi L_phi.
MINNORM_BEARING = n-a (AS3 is conditional on DERIVED; AS1 landed FREE).  Statement only, no test:
   each surviving candidate induces a DIFFERENT J_2 via D_(e')F', hence a different J_1 on
   im(d_1), so the coframe half ADDS a freedom rather than removing one and cannot by itself pin
   788 section 3.3's min-norm combination.  Whether either candidate coincides with it is a
   naturality question assigned to 794; I do not run it.
FREEDOMS_CONSUMED = the F'/F law NOT ADOPTED (two candidates displayed, one eliminated) ; child
   coframes E_p CARRIED AS DERIVED ; intrinsic Vol_4 CARRIED AS FORCED/CLASSIFIED ; THE PARENT
   FRAME e = I CARRIED AS THE SEALED INSTANCE AND DISCLOSED (753's own object, not a frame I
   selected; the elimination is displayed ON THAT INSTANCE and NOT claimed for every parent
   frame) ; the orientation det E_p = sgn(p) CARRIED AS DERIVED and used to BUILD (b2), not to
   prefer it ; J_1 / the section freedom CARRIED AS PARAMETER (788's residual, untouched) ;
   scaling weights NONE CONSUMED (law 2a) ; a metric NOT ADOPTED (the quadratic is the sealed
   Vol_4-weighted one) ; the smooth C_ref constituent NOT CONSUMED and BARRED (S26).
   SUBSTITUTED: NONE — audited line-by-line, with the one instance choice that could have been
   invisible disclosed above.
FLATTENING_CHECK = clean (37 rows walked; S26 and S08 live and both discharged).
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+3): (1) 788's ABSENT worry was MINE and was a SEARCH FAILURE, not a
   record fact — I checked V011, found both coframe occurrences on the barred smooth side, and let
   that stand for the record, when the record-side stock is my own sealed 753 cited in the same
   artifact; I under-searched a question I had the answer to, in a file I wrote; (2) "FREE" is
   SCOPED — two candidates survive the coframe square's own constraint and neither has been run
   against flux conservation or naturality, so a later narrowing must not read as a discovery;
   (3) I nearly made an invisible INSTANCE substitution — the elimination is computed at e = I,
   which is 753's sealed object rather than my choice, but that is exactly the distinction
   781/784/789 got wrong, so it is disclosed with its scope and not generalised.
   All three run against my own work; the one flattering result is bounded immediately by the
   843-dimensional residual.
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
