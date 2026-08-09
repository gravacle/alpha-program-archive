# STAGE 8 / 7A / Q-126 ROUTE — THE D_BR SPECTRUM: THE DEMAND ASSEMBLED, THE STRUCTURE DERIVED, THE SPECTRUM NOT BUILDABLE

Lane: DARIO (Builder B, independent verifier). Relay 760.
Governing: `DECISION_DBR_ROUTE_2026-08-08` `2cbe0c0c…` (SEALED-OK); the sealed beta closure
hunt `04c10c0d…`. Nothing adopted; the frozen prereg and R9-JII untouched.

## Lead determination

**The spectrum is PARTIAL, and the sealed record said the proof was out of reach before this
relay opened.** `STAGE8_COMPLETE_PUBLIC_DBR_LBR_SPECTRAL_THEOREM_SPEC_V001` `a751b72c…`,
sealed:

```text
complete_public_D_BR_L_BR_spectral_theorem_specified = true
complete_public_D_BR_L_BR_spectral_theorem_derived   = false | TYPE-U
theorem_proof_reachable_now                          = false | TYPE-U
```

**What I can build, and did.** The object's geometry is quoted archive-side and is completely
explicit — `Sigma_BR = S1_T x S2_flux x S1_Q`, compact; `H_BR = L2(Sigma_BR, S_Sigma tensor
E_parent)`; `D_BR = D_(Sigma,A) + Gamma_Sigma Phi`. From that alone the **raw spectrum's
structure is determined**: discrete, of product sums-of-squares form, with the `S2` tower
contributing `(k+1)^2/r_F^2` and each circle `(n + a)^2/R^2` with `a ∈ {0, 1/2}` fixed by its
spin structure — and, if `Phi` is a constant odd term, a uniform shift `D_BR^2 = D_(Sigma,A)^2 +
Phi^dagger Phi`.

**What blocks the rest is not effort.** Five prerequisites are TYPE-U; four shortcuts to the
public bottom are already TYPE-R **refuted** of record — including the one my own derivation
most invites, `Phi_dagger_Phi_forces_uniform_positive_public_gap = false | TYPE-R`. And the
**multiplicities cannot be pinned at all**, because the bundle class and `E_parent`'s rank are
*unselected* of record, along with the three radii, both spin structures, the odd profile, and
the index.

**A custody finding the route runs into immediately.** The two primary sources — the object's
defining principle (`ae1d0492…`) and the report that already carries *"an exact discrete
product-spectrum family for the untwisted adopted skeleton"* — are **absent archive-side**.
Under ARCHIVE-SIDE ONLY this lane reaches the *demand spec* and the *sealed quotations of the
object*, but not the defining principle and not the existing spectrum family. **I derived the
structure from the quoted geometry rather than reproducing a report I cannot read.**

**AL3 lands, and it cross-checks the census.** Every eigenvalue scales as an **inverse proper
length**, so `D_BR^2 ∝ 1/R^2`. The census's ground for its sibling candidate is *"`K_KK` changes
by `beta^2`"* — the same mechanism on a proper radius, with the reciprocal power. **`beta` enters
the D_BR spectrum through the radii and through the normalized transfer to `L_BR`'s proper-time
consumer**, which the corpus classifies VALUE/CONSUMER-CRITICAL and unbuilt.

`Q126_STATUS`: **unchanged.** `D_BR` is still UNBUILT for the complete normalized spectrum, so
no junction is yet simultaneously derived and beta-sensitive. The route is open; it is not
closed by this relay.

---

## 0. Preflight

### 0.1 Output name

Probed **before any write**, recursively: **absent**, artifact and sidecar both.

### 0.2 Sources verified before use

```text
DEC760 supervision/DECISION_DBR_ROUTE_2026-08-08.md                        2cbe0c0c…  SEALED-OK
SPEC   workspace/STAGE8_COMPLETE_PUBLIC_DBR_LBR_SPECTRAL_THEOREM_SPEC_V001.md  a751b72c…  SEALED-OK
SPEC1  workspace/STAGE8_BR_CLOSURE_OPERATOR_SPECTRUM_AND_SEAM10_IDENTITY_DETERMINATION_V001.md
                                                                            de88ba68…  SEALED-OK
GAP    workspace/STAGE8_BR_CLOSURE_OPERATOR_STRUCTURAL_SPECTRAL_GAP_DETERMINATION_V001.md
                                                                            e2fc00d2…  SEALED-OK
BETA   workspace/STAGE8_RECORD_CELL_SURFACE_AND_BETA_CLOSURE_HUNT_EINSTEIN_V001.md  04c10c0d…  SEALED-OK
REG    supervision/QUESTIONS_SETTLED_REGISTER_V001.md                       1ad7f0bd…  SEALED-OK
758    workspace/STAGE8_7A_THOMSON_SCOPING_DARIO_V001.md                    ebed567b…
```

**ABSENT ARCHIVE-SIDE, and load-bearing** — searched by name across the whole archive:

```text
alpha_global_record_surface_superconnection_principle_v001.md   ae1d0492…   NOT PRESENT
   — the object's DEFINING principle.  Reached only through GAP's sealed quotation of
     its lines :5-43 (the carrier and operator) and :45-68 (the unselected moduli).
reports/alpha_global_surface_dirac_superconnection_v001.md                  NOT PRESENT
   — the report GAP characterizes as giving "an exact discrete product-spectrum family
     for the untwisted adopted skeleton", moduli open.  NOT READ.  Nothing below is
     taken from it.
```

**Searched space:** recursive glob `./workspace/**/*.md` + `./supervision/**/*.md`, run from the
archive root, **all `_DARIO_` files excluded** (the corrected filter from 758 — the old
`*_DARIO_V001.md` pattern missed 199 artifacts' other versions), corpus **1,970 files**, with
`D_BR` (71) and `U_BR` (50) as known-positive controls.

### 0.3 Gates

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
No member binding.  No fixed-point execution.  No end test.  NO NUMERIC EVALUATION OF
PHYSICAL QUANTITIES — no eigenvalue, gap value, radius, scale or root is evaluated; §2
derives STRUCTURE in symbols only.  No comparison to measured constants.  No common cell
formed.  No junction map evaluated.  No smooth data derived.  Nothing adopted.
No register, plan, tracker, or git action.
```

---

## 1. AL1 — THE DEMAND, ASSEMBLED

### 1.1 The object

[PROVABLE] `GAP` `e2fc00d2…` §1.1, quoting the defining principle at `:5-43`:

```text
Sigma_BR = S1_T x S2_flux x S1_Q,
H_BR = L2(Sigma_BR, S_Sigma tensor E_parent),
D_BR = D_Sigma,A + Gamma_Sigma Phi.
```

with `Sigma_BR` **compact** (`:5-18`) and `D_BR` a **Dirac superconnection** (`:24-43`).

[PROVABLE] And, in the same quotation, what is **not** fixed (`:45-68`): *"metric radii, spin
structure, bundle class, odd profile, and index unselected."*

### 1.2 What the spectrum is the spectrum *of*

[PROVABLE] The gap the program wants is stated at `SPEC1` `de88ba68…` §0:

```text
carrier  H_BR = L2(Sigma_BR, S_Sigma tensor E_parent)
gap      isolation between the lowest public spectral points of D_BR^2
         on a derived public quotient under Tr_BR
```

**So the demanded object is not `spec(D_BR)` on `H_BR`. It is the spectrum of `D_BR^2` on a
derived *public quotient*, counted under a derived linear trace `Tr_BR`.** That distinction is
the whole of §3.

### 1.3 The normalization, and what "complete" requires

[PROVABLE] `SPEC` `a751b72c…` carries the `L_BR` relation:

```text
L_BR = Delta_BR,public tensor I_E + I_public tensor C2,parent
P_BR = C_candidate^dagger P_public C_candidate = P_public
```

[PROVABLE] The eight-item package, `SPEC1` `de88ba68…`: *"1. a domain; 2. a
spectral-calculus-admissible realization; 3. derived public equivalence relation/quotient
Hilbert space; 4. derived linear `Tr_BR`; 5. null/private-mode removal rule; 6. statistics/ghost
sign assignment; 7. a sufficient relation between `D_BR^2` and normalized `L_BR`; 8. target-blind
moduli, boundary, spin, bundle, and odd-profile selection or a predeclared parametrized
theorem."*

[PROVABLE] `GAP` `e2fc00d2…` §2 sorts them — and the three-way split is finer than the relay's
binary, which `GAP` says explicitly (*"The requested binary split is not quite exhaustive"*):

```text
EXISTENCE-CRITICAL:
  complete closed domain; symmetric/self-adjoint realization; elliptic
  principal symbol; compactness preserved by the physical quotient
PUBLIC-IDENTITY-CRITICAL:
  public quotient; Tr_BR; null/private removal; selected admissible branch;
  proof of bottom positivity and one-dimensional public multiplicity
VALUE/CONSUMER-CRITICAL ONLY:
  exact moduli after branch selection; statistics/ghost signs for supertrace;
  normalized transfer from D_BR^2 to the L_BR proper-time consumer
```

[YOURS] **"Complete normalized" therefore names two distinct things at once**: *complete* = the
public-identity layer (quotient, trace, null/private rule, branch, bottom simplicity);
*normalized* = the last item, the **transfer from `D_BR^2` to `L_BR`'s proper-time consumer**.
The census's phrase packs both, and only the second is where `beta` lives (§3).

### 1.4 The status of record, before this relay

[PROVABLE] Every flag below is sealed, from `SPEC`, `SPEC1` and `GAP`:

```text
complete_public_D_BR_L_BR_spectral_theorem_specified = true
complete_public_D_BR_L_BR_spectral_theorem_derived   = false | TYPE-U
theorem_proof_reachable_now                          = false | TYPE-U
complete_public_D_BR_L_BR_object_derived             = false | TYPE-U
BR_operator_domain_derived                           = false | TYPE-U
symbolic_spectrum_available                          = false | TYPE-U
complete_public_BR_ellipticity_derived               = false | TYPE-U
complete_public_BR_self_adjoint_on_named_domain      = false | TYPE-U
complete_public_BR_gap_exists_by_structure           = NO_VERDICT
```

**and four shortcuts already refuted:**

```text
Phi_dagger_Phi_forces_uniform_positive_public_gap    = false | TYPE-R
parent_Casimir_forces_uniform_positive_public_gap    = false | TYPE-R
unquotiented_skeleton_satisfies_public_cardinality_one = false | TYPE-R
compact_topology_forces_simple_public_bottom         = false | TYPE-R
```

**and one positive theorem, conditional:**

```text
raw_BR_skeleton_compact_resolvent_theorem = true | TYPE-C |
  condition: smooth compact Riemannian record surface, finite-rank Hermitian
  carrier, unitary connection, smooth self-adjoint odd term, and standard
  self-adjoint Sobolev realization
raw_BR_skeleton_has_isolated_spectral_clusters = true | TYPE-C
```

---

## 2. AL2 — THE BUILD

### 2.1 What the quoted geometry determines

[YOURS] `Sigma_BR = S1_T x S2_flux x S1_Q` is a product of two circles and a two-sphere, all
compact. For a product spin manifold with the product spin structure, the Dirac Laplacian is the
sum of the factors' Dirac Laplacians, so **the spectrum of `D_(Sigma,A)^2` is a sum of the three
towers**:

```text
spec(D_(Sigma,A)^2)  =  { (n_T + a_T)^2 / R_T^2
                       + (k + 1)^2   / r_F^2
                       + (n_Q + a_Q)^2 / R_Q^2 }

   n_T, n_Q in Z ;  k = 0, 1, 2, ...
   a_T, a_Q in {0, 1/2}, fixed by each circle's SPIN STRUCTURE
   R_T, r_F, R_Q  the three metric radii
```

The `S^2` tower's `(k+1)/r_F` form and the circles' `(n+a)/R` form are the standard Dirac spectra
of those factors; the shift `a` is `0` for the periodic and `1/2` for the antiperiodic spin
structure. **This is discrete with finite multiplicities and accumulates only at infinity** —
which is `GAP`'s `raw_BR_skeleton_has_isolated_spectral_clusters`, reproduced here from the
geometry rather than assumed.

### 2.2 The odd term

[YOURS] `D_BR = D_(Sigma,A) + Gamma_Sigma Phi`. If `Phi` is a **constant** odd term and
`Gamma_Sigma` anticommutes with `D_(Sigma,A)`, the cross terms cancel and

```text
D_BR^2 = D_(Sigma,A)^2 + Phi^dagger Phi,
```

a **uniform non-negative shift** of the whole tower.

[PROVABLE] **And the inference this most invites is already refuted of record.** `GAP`:
`Phi_dagger_Phi_forces_uniform_positive_public_gap = false | TYPE-R`. The shift is real on the
**raw** operator; it does **not** deliver a positive **public** gap, because the public quotient
can remove exactly the modes the shift was protecting. I derive the shift and stop at the line
the corpus already drew.

### 2.3 What is NOT determined — and why multiplicities in particular are not

[PROVABLE] The moduli are **unselected**: the three radii `R_T, r_F, R_Q`; both circles' spin
structures (`a_T, a_Q`); the bundle class; the odd profile `Phi`; the index.

[YOURS] **So multiplicities cannot be pinned even in principle here.** The multiplicity of an
eigenvalue is the product of the factor multiplicities **times `rank(E_parent)`** and the
spinor-bundle bookkeeping of the product — and `E_parent`'s bundle class is one of the unselected
items. **I decline to display a multiplicity table.** This is exactly the bookkeeping where my
731 trichotomy failed by summing the wrong index set, and here the corpus has not even fixed the
index set.

### 2.4 The public layer — where the spectrum actually lives, and it is unbuilt

[PROVABLE] Per §1.2 the demanded spectrum is on the **public quotient under `Tr_BR`**, and per
§1.4 the quotient, the trace, the null/private-mode rule, the branch selection, and the proofs of
bottom positivity and simplicity are all unbuilt, with `compact_topology_forces_simple_public_bottom
= false | TYPE-R` closing the obvious route.

[YOURS] **So §2.1's tower is not the demanded object.** It is the raw skeleton's spectrum; the
demanded object is its image under a quotient that does not exist. Reporting §2.1 as "the D_BR
spectrum" would be the error `SPEC1` warns against when it refuses to *"calculate an unbuilt
operator."*

```text
SPECTRUM = PARTIAL (gaps named).
  DERIVED here: the raw product tower's exact FORM (sums of squares over two
    circle towers and one S^2 tower), its discreteness, and the uniform Phi^2
    shift — all in symbols, no value evaluated.
  NOT DERIVED: multiplicities (bundle class and rank(E_parent) unselected);
    the three radii, both spin structures, odd profile, index (unselected);
    the public quotient, Tr_BR, null/private rule, branch, bottom positivity
    and simplicity (TYPE-U, with four TYPE-R refutations closing the shortcuts);
    the normalized transfer to L_BR (VALUE/CONSUMER-CRITICAL, unbuilt).
```

---

## 3. AL3 — HOW `beta` ENTERS, AND THE CENSUS RE-VERIFIED

[PROVABLE] The census's ground, `BETA` `04c10c0d…`: *"beta-SENSITIVE junctions — none derived:
the fiber proper radius `R` in `K_KK` (**ADOPTED** ansatz; `K_KK` changes by `beta^2`); the
complete normalized `D_BR` spectrum (**UNBUILT**); the skeleton-to-cell embedding … (**GAP**)."*

[YOURS] **Re-verified against the built structure, and the mechanism is now visible rather than
asserted.** Every entry of §2.1's tower is an inverse proper length squared:

```text
eigenvalues of D_BR^2  ~  1/R_T^2 ,  1/r_F^2 ,  1/R_Q^2
```

`beta` is the record cell's internal/external conversion — `R = beta c Delta tau` — i.e. exactly
what turns a record-internal interval into a **proper length**. Rescaling `beta` rescales the
radii and therefore rescales **every eigenvalue**, as `beta^(-2)` on `D_BR^2`.

[YOURS] **Two independent confirmations that this is the census's own mechanism.**

1. **Its sibling candidate scales the same way.** `K_KK` *"changes by `beta^2`"* through *"the
   fiber proper radius `R`"* — the same object type, the same conversion, the reciprocal power.
   The census's two named candidates are beta-sensitive **for one reason**, and §2.1 exhibits it.
2. **The normalization is named as the transfer to a proper-time consumer.** `GAP`'s
   VALUE/CONSUMER-CRITICAL item is the *"normalized transfer from `D_BR^2` to the `L_BR`
   **proper-time** consumer."* Proper time is the external side of `beta`'s conversion. **So the
   word "normalized" in "the complete normalized `D_BR` spectrum" is precisely the beta-carrying
   step**, and the census's classification is not incidental to the phrase — it *is* the phrase.

```text
BETA_ENTRY = displayed.  Through the metric radii (eigenvalues ~ 1/R, so
  D_BR^2 ~ beta^(-2)) and through the normalized transfer to L_BR's PROPER-TIME
  consumer.  The census's grounds re-verified against the built structure, and
  its sibling candidate's beta^2 scaling shown to be the same mechanism.
```

### 3.1 Q-126, re-posed honestly

[YOURS] **Unchanged.** Q-126 holds that every junction where `beta` could appear is ADOPTED, GAP,
or UNBUILT. `D_BR` remains **UNBUILT** for the complete normalized spectrum: §2 derived the raw
tower's form and nothing on the public layer. **No junction is yet simultaneously derived and
beta-sensitive**, and I do not report the census as moved.

[YOURS] What *has* changed is smaller and worth stating exactly: the census's `D_BR` entry was a
one-line status. It now has a **displayed mechanism** — which is what a later derivation would
have to make good on, and which lets a reader check the claim instead of taking it.

---

## 4. AL4 — CORRESPONDENCE LEDGER, ZERO VERDICT WEIGHT

Recorded because they are familiar and therefore dangerous; **none is used above.**

| # | Rhyme | Zero-weight note |
|---|---|---|
| 1 | `D_BR^2 = D^2 + Phi^dagger Phi` ↔ a mass gap from a Yukawa-type term | The corpus **already refuted** the inference to a public gap (TYPE-R). The rhyme is why it needed refuting. |
| 2 | `S1 x S2 x S1` towers ↔ a Kaluza-Klein mode tower | Close enough to be hazardous: the census's sibling candidate is literally `K_KK`. Ledgered, not used. |
| 3 | The public quotient ↔ BRST / physical-state cohomology | Suggestive of a route to `Tr_BR`; **not** taken. |
| 4 | *"isolated lowest eigenspace"* ↔ a spectral-gap/mass-gap theorem | The demanded statement is about a **quotient**, not the raw operator; the rhyme drops exactly that. |

```text
LEDGER = 4 (all at zero verdict weight; none consumed)
```

---

## 5. GROUNDING, JURISDICTION, VERB AUDIT

### 5.1 Grounding

| # | Claim | Pin | Tag |
|---|---|---|---|
| 1 | The route is ruled; a construction, not an adoption or gap | `2cbe0c0c…` | PROVABLE |
| 2 | `Sigma_BR`, `H_BR`, `D_BR`; compact; moduli unselected | `e2fc00d2…` §1.1, quoting `:5-43`, `:45-68` | PROVABLE |
| 3 | The gap is on a **public quotient** under `Tr_BR` | `de88ba68…` §0 | PROVABLE |
| 4 | The eight-item package | `de88ba68…` | PROVABLE |
| 5 | The three-way EXISTENCE / PUBLIC-IDENTITY / VALUE split | `e2fc00d2…` §2 | PROVABLE |
| 6 | `L_BR` relation; theorem specified, derived-false, proof not reachable now | `a751b72c…` | PROVABLE |
| 7 | Four TYPE-R shortcut refusals; one TYPE-C conditional theorem | `e2fc00d2…` | PROVABLE |
| 8 | The census's three candidates and `K_KK`'s `beta^2` ground | `04c10c0d…` | PROVABLE |
| 9 | The product tower's exact form and discreteness | §2.1 | YOURS |
| 10 | The uniform `Phi^dagger Phi` shift | §2.2 | YOURS, and stopped at the TYPE-R line |
| 11 | Multiplicities not determinable (bundle class, `rank(E_parent)` unselected) | §2.3 | YOURS |
| 12 | `beta` enters via the radii and the proper-time transfer | §3 | YOURS |
| 13 | Two primaries absent archive-side | §0.2, by name-search of the whole archive | PROVABLE |

**Pin check: 13/13.**

### 5.2 Jurisdiction check

**On building at all, as Builder B.** The distinction I used at 753 governs again: deriving what
sealed coordinates already determine is verification; authoring new content is not. §2.1 takes a
**quoted, sealed geometry** and reads off the structure it forces. Where authorship would have
begun — selecting a radius, a spin structure, a bundle class, or a normalization — I stopped and
listed the item as unselected.

**On the VOID CONDITION.** No coefficient consulted, no value evaluated, no modulus chosen. The
one place a choice would have produced a result — picking spin structures to make a bottom mode
appear or vanish — is exactly what §2.3 refuses.

**On the four TYPE-R refutations.** My §2.2 derivation lands one step short of a refuted claim.
I display the derivation and the refutation together rather than presenting the shift as progress
toward a gap.

**On ARCHIVE-SIDE ONLY.** Two load-bearing primaries are outside. I did not read them, did not
route around them, and did not reproduce the spectrum family one of them is said to contain.
§0.2 records both by name and digest so the registrar can decide whether to mirror them.

**On R9 / R9-JII and the frozen prereg.** Untouched.

### 5.3 Self verb audit — **CLEAN, with three disclosures**

1. **The headline is weaker than the commission's title.** The relay is titled *"THE D_BR
   SPECTRUM: BUILT"*. It is not built, and the sealed record carried
   `theorem_proof_reachable_now = false | TYPE-U` before this relay opened. A commission's title
   may direct the work; it may not settle its outcome.
2. **I derived one step short of a refuted claim and say so in place.** §2.2's `Phi^dagger Phi`
   shift is the natural read and its extension to a public gap is TYPE-R of record. Presenting the
   shift without the refutation beside it would have read as progress toward the gap.
3. **I declined a multiplicity table** (§2.3) that would have looked like the most concrete part
   of a spectrum build. The index set it would sum over is unselected of record, and this is the
   precise failure mode of my 731 trichotomy.

---

```text
DEMAND = assembled (block-covered).  The demanded object is NOT spec(D_BR) on H_BR but
  the spectrum of D_BR^2 on a DERIVED PUBLIC QUOTIENT under a derived linear Tr_BR
  (de88ba68... section 0).  Eight-item package displayed; GAP's three-way split
  (EXISTENCE / PUBLIC-IDENTITY / VALUE-CONSUMER) displayed and preferred to the relay's
  binary, as GAP itself states.  "Complete normalized" names two things: the
  public-identity layer, and the normalized transfer from D_BR^2 to L_BR's PROPER-TIME
  consumer.
SPECTRUM = PARTIAL (gaps named).  DERIVED from the sealed quoted geometry
  Sigma_BR = S1_T x S2_flux x S1_Q, D_BR = D_(Sigma,A) + Gamma_Sigma Phi:
  the raw tower's exact FORM — spec(D^2) = { (n_T+a_T)^2/R_T^2 + (k+1)^2/r_F^2 +
  (n_Q+a_Q)^2/R_Q^2 }, k >= 0, a in {0,1/2} by spin structure — its discreteness, and
  the uniform shift D_BR^2 = D^2 + Phi^dagger Phi for constant odd Phi.  All symbolic;
  no value evaluated.  NOT DERIVED: multiplicities (bundle class and rank(E_parent)
  UNSELECTED — no table displayed, deliberately); the three radii, both spin structures,
  odd profile, index (UNSELECTED); the public quotient, Tr_BR, null/private rule, branch
  selection, bottom positivity and simplicity (TYPE-U, with FOUR TYPE-R refutations
  already closing the shortcuts, including Phi_dagger_Phi_forces_uniform_positive_
  public_gap = false); the normalized transfer to L_BR.  The corpus already carried
  theorem_proof_reachable_now = false | TYPE-U.
  CUSTODY: the object's DEFINING principle (ae1d0492...) and the report said to hold an
  exact discrete product-spectrum family are BOTH ABSENT ARCHIVE-SIDE.  Neither was read;
  the structure above is derived from the sealed QUOTATION of the geometry instead.
BETA_ENTRY = displayed (census grounds re-verified).  Eigenvalues go as inverse proper
  lengths, so D_BR^2 ~ beta^(-2); and the normalization is named of record as the
  transfer to L_BR's PROPER-TIME consumer — the external side of beta's conversion.
  The census's sibling candidate K_KK "changes by beta^2" through a fiber PROPER RADIUS:
  the same mechanism, reciprocal power.  So "complete NORMALIZED D_BR spectrum" is not
  incidentally beta-sensitive — the normalizing step IS the beta-carrying step.
Q126_STATUS = re-posed honestly: UNCHANGED.  D_BR remains UNBUILT for the complete
  normalized spectrum; no junction is yet simultaneously derived and beta-sensitive.
  What changed is smaller and stated as such: the census's one-line status now has a
  displayed mechanism a later derivation must make good on.
LEDGER = 4 (zero verdict weight, none consumed)
VOID = clean
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+3 disclosures at section 5.3, including that the commission's
  title says BUILT and the sealed record said the proof was unreachable beforehand)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
