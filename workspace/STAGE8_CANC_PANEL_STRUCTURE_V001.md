# STAGE 8 — CANC-PANEL-STRUCTURE: ADVERSARIAL VERIFICATION OF B1 (DIFFERENCE_STRUCTURE) AND B3 (LEADING_DEGREE_3) OF STAGE8_REQUIRE_BUILD_CANCELLATION_V001

## BLIND ADVERSARIAL VERIFIER — STRUCTURE LENS — [CLAIMED]

Date: 2026-08-13
Role: one lens of a three-lens panel; cross-lineage to the builder; DEFAULT = REFUTE.
Blind to co-panelists: no STAGE8_CANC_PANEL_* artifact opened or listed-into.

Gates: `alpha_computed = false` ; `kappa_record_computed = false` ;
`proof_authorized = false`

Fences held: connection-only, symbolic. No value of n, kappa_record, alpha, any
exponent, norm, scale, or spectrum computed, bounded, or evaluated; only symbolic
order/parity/degree/quantifier bookkeeping. Scale-bearing sealed text (ECO, RFA, the
E1 successor spec) read SUSPECT-ONLY to classify and attack — never as a positive
certifier. No register/tracker/plan/road/ledger/lens file read. Every seal verified
at path by `shasum -a 256` BEFORE reliance. Output name probed ABSENT before write.

---

## 1. SEALS VERIFIED AT PATH

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`.

```text
BUILD UNDER TEST:
  STAGE8_REQUIRE_BUILD_CANCELLATION_V001.md
    4971e2739666bd95917163763f42cadf427442a7c710f8b22353d65ead9fe5fe  MATCHES-TASKED
TASKED SOURCES:
  STAGE8_REQUIRE_BUILD_CLUSTER_SUMMABILITY_V001.md
    5cdd5dafccd1dfd5075426cce384cb84136a21df1cecad56576da3799cea9455  MATCHES-TASKED  CONN
  STAGE8_REQUIRE_CLUSTER_CHECK_V001.md
    a7f75d0f2c4ed9604be78a9024461d93ff097c77fbf9b46e0207c4e7eea93c13  MATCHES-TASKED  CONN
  STAGE8_R_RECORD_L_FORM_FABLE_V001.md (FORM)
    5e49d2093d4ee17b840cc096d5caf3a6edafda4e37abbd175a7a371c34658f37  MATCHES-TASKED  CONN
BUILD'S SEA-COVARIANCE SOURCES:
  STAGE8_EXTENSIVITY_VERDICT_AND_RL2B_CAMPAIGN_OPENING_V001.md (ECO)
    0f3082cab910f2eb6769698fc03cdb0201830c2551ecd8201fa6748b24e07505  MATCHES build-recorded  SCALE
  STAGE8_RL2B_FRAME_ANSWER_AND_CAMPAIGN_TARGET_V001.md (RFA)
    2ede02aea415157ada9edd6f685aabcc824acf2716777f4aa2dc98467fe92840  MATCHES build-recorded  SCALE
PROVENANCE ONE LEVEL DOWN (the FORM's own bedrock, recomputed at path;
first-8 all match the FORM §1 table):
  STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md (M03)
    2cd1ffcefd68ac03c6c09a4eca0dc9fe8d1adc8ac564cc0d050dfd41d79e6d0f  CONN
  STAGE8_BARE_SURFACE_ALPHA_DETERMINATION_FABLE_V001.md (W)
    82e81f6e659108c05872d30d4c5ad00bf66cad3c272c4aa8240aa89fc5a62010  CONN
  STAGE8_SADDLE_FOUNDATION_PARENT_ACTION_DARIO_V001.md (T3)
    1d11f15040f8b85b7e081fccfeddb995c41941c55464d759a2fa91a8feffc775  CONN
THE OBJECT'S OWN SEALED DEFINITION (found by this lens; NOT in the build's source
list; sidecar verified):
  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md (E1v2)
    468467303a109dc825b015107897dacc107800fc981030377c3f006b384cccb5
    sidecar STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md.seal.sha256: MATCH  SCALE
  STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md (Phase-A)
    789338adb7d3d36da453113e98f371a4f92543cf2652b047f8481c407bed5bc3
    matches E1v2 :82 recorded seal                                        SCALE
```

E1v2 is the "E1 spec v002" that ECO's own kernel quotation cites (ECO :151-152
"E1 spec v001:98-99 and v002:322"); its C1 block at E1v2 :319-325 carries verbatim
the same `C(r)` display ECO :153-155 quotes. It is therefore inside the build's own
citation closure — the build quoted 4 lines of it (via ECO) and did not open it.

---

## 2. WHAT B1 AND B3 CLAIM, AT THE BYTES

Build :139-145: because "a enters only through the abelian unit-modulus character
(S4/B5)", the a-dependence of the kernel is a pure phase dressing with a POINT
function `Theta_a(x) = n <ell(x), a>`:
`V_n(a)(x,y) = exp(i[Theta_a(x) - Theta_a(y)]) · V_n(0)(x,y)`, hence
`V_n(a) - V_n(0) = [exp(i[Theta_a(x)-Theta_a(y)]) - 1] · V_n(0)(x,y)`
("the connection-only content permits nothing else", build :147-148).
Build :156-159: the difference "vanishes to EXACTLY FIRST ORDER" with prefactor
`i Delta`, `Delta = n<ell,r> + O(|r|^2)`. Build :166-179 (B3): one-power softening,
degree -3 -> degree -2, still HS-singular; full cancellation would need third-order
vanishing = trivial write, contradicting n != 0.

---

## 3. ATTACK 1 — IS THE PHASE-DRESSING IDENTITY OF RECORD? NO. THE a-DEPENDENCE ESCAPES THE POINTWISE PHASE THROUGH THE TRANSPORTED GENERATORS

**3.1 No sealed source states the identity.** ECO :174 and RFA :119-121 use
`V(a)` / `V_(mu lambda)(a)` WITHOUT defining its kernel law. The FORM never mentions
`V_n(a)(x,y)` as a kernel. The identity at build :144-145 is the build's own
construction, nowhere quoted.

**3.2 The object HAS a sealed definition, and the build never opened it.** The
R-L2b object the build claims for itself (build :7-9 = ECO :174 = RFA :119) is
defined of record at E1v2 §R.0:

```text
E1v2 :653-654  V_{mu lambda}(a) := u_mu^{(c)}(a_-)^dagger u_lambda^{(c)}(a_+)
E1v2 :660-661  A_{mu lambda}(a) := C(V_{mu lambda}(a) - 1)C ;
               Delta_{mu lambda}(a) := A(a) - A(0) = C(V(a) - V(0))C
```

The a-dependence sits inside the dressed one-particle evolutions `u^{(c)}(a_±)`.
Three sealed clauses type that dependence as NOT a pointwise-phase multiplication:

```text
E1v2 :510-512  "Y_2 Y_1 = 0 holds only in the strict equal-time
   multiplication-operator idealization with disjoint supports; the actual
   V_i - 1 are Dyson-dressed by free h_0 propagation over the whole interval."
E1v2 :696-698  (S2, the HS object itself) "MUST be a TWO-TIME (cell-S-matrix)
   object; the equal-time version is FALSE by C6."
E1v2 :1111     the a-vertex is  J = -(Q b_D Q) ⊗ alpha_x  — the connection
   insertion carries the Dirac matrix alpha_x, i.e. it is SPINOR-MATRIX-VALUED,
   with a profile b_D supported inside the diamond (E1v2 :1057-1058).
```

Consequences, purely structural: (i) the build's identity IS the equal-time
multiplication-operator idealization — a scalar endpoint phase acting on the kernel
— and the sealed spec types exactly that idealization FALSE for this object;
(ii) a scalar endpoint factorization `exp(i[Theta(x)-Theta(y)])` can reproduce an
a-insertion only when the insertion is the pure-gauge (curvature-free) part — it
commutes with the spinor structure and with propagation, while the sealed vertex
`(Q b_D Q) ⊗ alpha_x` does neither (the same commutator class the spec names as its
central nonzero obstruction, `[h_0, M(t) ⊗ S]`, E1v2 :703, :1138); (iii) the sealed
cancellation bookkeeping that DOES exist for the subtracted object runs through the
alpha_x vertex algebra — "the leading residue is killed TWICE — odd spinor trace
tr_spinor[C(p) alpha_x] = -2 p-hat_x, and |m_0|^2 = 0" (E1v2 :692-694) — a
spinor-parity mechanism the build's scalar-phase picture erases entirely.

**3.3 The FORM does not close the gap.** FORM B5 governs the ratified INFLUENCE
FUNCTIONAL `F_N = P_0 + Z_N P_ch` (FORM :96-105) — a different level from the sea
kernel. In the sealed law the characters are INTERLEAVED with the a-independent step
operators (`W_{1,j} = D_{n,j} S_j`, ordered product, FORM :99-100); they collect
into a single product phase only ON THE READY VECTOR: `W_N^(n)[a]|R_N> =
(product_j z_j)|P_N>` (FORM :101) — a one-vector identity, not an operator/kernel
identity. Pulling every `D_j` to the endpoints of a general matrix element requires
commutation through the `S_j` that no sealed span supplies; the E1-lineage seal
(:510-512) says the actual objects do NOT so commute (Dyson dressing). D3's
invariance clause (FORM :197-199) makes the write phase a GLOBAL functional of the
doubled history — again not a per-point function on the diamond.

**3.4 What survives this attack (recorded for fairness).** Within the sealed text I
find NO a-dependence in: the HS measure (flat double integral, RFA :66-68), the C
endcaps (fixed sea covariance, ECO :174; E1v2 :660), the pointer weights `w_lambda`
(Phase-A data, E1v2 :82, a-independent), or the contour bookkeeping (the doubled
pair enters as `(a_-, a_+)` arguments only, E1v2 :654; FORM :197-199). So the
build's WEAK claim — subtraction removes an a-independent baseline; the connection
enters the LAW only through the character/vertex insertions — stands. What is
refuted is the STRONG claim that the kernel-level a-dependence is a pointwise
endpoint phase: it escapes into the TRANSPORTED GENERATORS (the h_0-interleaved,
matrix-valued a-vertex of the two-time object).

---

## 4. ATTACK 2 — IS "VANISHES TO EXACTLY FIRST ORDER" FORCED? NO — THE ORDER IS NOT OF RECORD, IN BOTH TASKED DIRECTIONS

**4.1 The coefficient consumes an unsupplied sealed datum.** The build's
`Delta = n<ell,r> + O(|r|^2)` (build :158-159, :276-277) reads `ell` as a pointwise
current density with `grad Theta_a = n ell`. The FORM itself flags, at the exact
line the build cites for its derivative law: `ell_j` is "an incidence datum of the
write, NOT sealed as an object — see D6" (FORM :164-165); and D6/G3: "the write
chains ell_j — the support/current-density realization of the per-cell write ...
RA27-3's support and current density fields are NOT SUPPLIED of record" (FORM
:277-281; B7 :115-119). The build's Taylor step is built on the one object its own
bedrock seals as unsupplied.

**4.2 Direction one — HIGHER order is open.** If the G3 realization concentrates
the write current on a lower-dimensional support (the literal reading of a CHAIN in
`R^(K_1^+)`, FORM B4 :89-94), then at every diagonal point off the support the
accumulated character phase is locally CONSTANT and the difference kernel vanishes
to ALL orders there — not first order. The one-power softening is then not a
uniform property of the diagonal at all; the residual relocates to the support.

**4.3 Direction two — ZEROTH order is open.** Near or around a concentrated write
current no single-valued `Theta_a` exists (the accumulated phase between two
spatially coincident approaches is path-dependent; abelian curvature concentrated
on the support), so `[exp(i Delta)-1]` need not vanish as `|r| -> 0` there: the
degree -3 singularity passes through UNSOFTENED at such points. Independently, at
the sealed definition the difference is a TWO-TIME Dyson-dressed object
(E1v2 :653-654, :696-698); no sealed span certifies that ITS kernel vanishes at
spatial coincidence at any order. The build's diagonal-triviality step rests on
`chi_n(identity) = 1` (FORM :168) — a statement about the holonomy argument of the
character, i.e. coincidence ALONG THE RECORD ORDER; its transfer to SPATIAL
coincidence of the 3d kernel is exactly the unsealed chain-to-diamond bridge.

**4.4 What survives.** At any point where a pointwise current density EXISTS and is
nonzero, first-order vanishing with coefficient `n<ell,r>` is the correct Taylor
statement, and the build's remark that conservation (divergence-free) does not
raise the order is sound: transversality kills `<ell(x),r>` only on a plane of
directions, never for all `r`; `<ell(x),r> = 0` for all `r` iff `ell(x) = 0`. The
refutation is of "EXACTLY", as an of-record, realization-independent claim.

---

## 5. ATTACK 3 — "FULL CANCELLATION IFF TRIVIAL WRITE": THE STATED BICONDITIONAL HAS A LOCALITY GAP AND A THRESHOLD CONFLATION

**5.1 Locality gap (the tasked conflation, confirmed present).** The nonzero write
forced by `n != 0` is GLOBAL-EXISTENTIAL: "nonzero variation is Phi != 0" (FORM
B6 :111-113; FORM :337-339) — nonzero SOMEWHERE. Full cancellation of the R-L2b
kernel is asked ON A DIAMOND (RFA :119-121). In the build's own phase picture, full
cancellation on a given diamond requires only that the write current vanish ON THAT
DIAMOND (phase locally constant THERE) — which is compatible with a nonzero write
elsewhere. With G3's support NOT SUPPLIED, no sealed object places the write current
inside every diamond; a support-avoiding diamond fully cancels with `n != 0`
intact. The build's single-diamond statement (build :175-179, :282-284) therefore
does NOT follow as written. The biconditional is RESTORED at every-diamond
strength — cancellation on EVERY diamond forces zero current density everywhere,
i.e. zero chains, i.e. `Phi = 0`, contradicting `n != 0` — and the campaign's
per-diamond-uniform exponent (RFA :122-128) does live at every-diamond strength;
but the build never states the quantifier, and the quantified version changes B3's
content: the residual and its location become support-realization-dependent rather
than a uniform degree -2 on every diamond.

**5.2 Threshold conflation.** "To reach FULL cancellation (bounded kernel) the
phase difference would have to vanish to THIRD order" (build :175-177) imports
RFA's bounded-kernel criterion (RFA :119-121). The OBJECT is Hilbert-Schmidt
(ECO :174; RFA :66-68), for which full cancellation needs only coincidence degree
strictly better than -3/2 — i.e. `Delta = O(|r|^s)` with `s > 3/2`; order-2
vanishing suffices. Both thresholds hinge on the same first-order coefficient, so
the build's conclusion is unaffected — but the two sealed criteria are distinct and
the build fuses them. Minor bookkeeping slip in the same lines: third-order
vanishing of `Delta` requires `ell` and its FIRST derivative to vanish (killing the
`r^1` and `r^2` terms), not "its next two derivatives" (build :177-178).

**5.3 Conditionality.** The whole biconditional is posed inside the phase-dressing
identity refuted in §3; at the sealed two-time definition, "full cancellation would
require a trivial write" is not derived by any sealed span. Status of record:
UNDETERMINED, not CONFIRMED — while noting no sealed span exhibits full
cancellation either, and this lens found no exact symmetry that would produce it
(the matrix-vertex/Dyson structure adds no candidate symmetry; it removes the
scalar-phase one).

---

## 6. ATTACK 4 — THE SYMBOLIC DEGREE BOOKKEEPING: VERIFIED

```text
(i)  O(|r|) prefactor on a homogeneous degree -3 kernel: degree (+1) + (-3) = -2.
     CORRECT as symbolic order arithmetic (conditional on the O(|r|) prefactor,
     which is B1's refuted premise, not an arithmetic error).
(ii) HS threshold in three dimensions: ||X||_2^2 integrates |kernel|^2 against
     d^3r near coincidence; int_{|r|<eps} |r|^(-2s) d^3r converges iff 2s < 3,
     i.e. a coincidence degree strictly better than -3/2 is required. CORRECT.
(iii) degree -2 residual: |kernel|^2 ~ |r|^(-4); the radial integrand ~ |r|^(-2);
     divergent at coincidence. So degree -2 IS still HS-singular. CORRECT.
(iv) sealed inputs to the count verified verbatim: degree -3 homogeneity and odd
     imaginary off-diagonal part, ECO :151-155 (= E1v2 :319-325); "L^2-BOUNDED BUT
     NOT HILBERT-SCHMIDT", ECO :168-171. Parity fact |odd|^2 = even: elementary.
```

No numeric evaluation performed by this lens; degrees and parities only.

---

## 7. CITATION-SPAN AUDIT OF THE BUILD

```text
ECO :151-155, :162-165, :168-171, :174, :176-179, :189-201  — all VERIFIED at the
  quoted lines.
RFA :66 (HS integrand; actually :66-68), :119-131, :122-125, :126-128, :137-138
  — VERIFIED (off-by-lines within tolerance).
FORM B6 :107-113, D2 :167-168, D3 :198-199 — VERIFIED.
FORM "B5 :96-98" for "no other a-dependence exists anywhere in the law" — SPAN
  SLIP: the phrase is D2's gloss of B5 at FORM :162-163, not text inside :96-98;
  and the FORM is itself CLAIMED (pre-panel), so the build's bedrock premise is a
  co-lineage CLAIMED assembly's paraphrase of M03/T3. Not a provenance break
  (M03/W/T3 seals verified here, §1), but the citation is imprecise and the
  crucial adjacent caveat — ell_j "NOT sealed as an object" (FORM :164-165) — is
  never carried into the build.
Build's consistency claim with the wall's "short one power" (build :299-301; wall
  §3.4 :264-284): the wall's clause "The difference-cancellation supplies at most
  ONE power" is itself a carried claim of the same CLAIMED lineage, not a sealed
  derivation; consistency with it is noted, certifying nothing.
OMISSION, the decisive one: the sealed definition of the very object B1 factors —
  E1v2 :653-654 with its :510-512 / :696-698 / :1111 typing — is absent from the
  build's source list although ECO's kernel quote points into the same sealed file.
```

---

## 8. WHAT THIS REFUTATION DOES AND DOES NOT DO

```text
DOES: refute B1's factorized identity as an of-record fact; refute "EXACTLY FIRST
  ORDER" as forced; refute the single-diamond form of "full cancellation iff
  trivial write"; reduce B3-as-stated ("softened to degree -2") to a conditional
  of an unsealed idealization plus an unsupplied datum (G3). The residual's DEGREE
  is not of record.
DOES NOT: exhibit or reopen a full-cancellation symmetry. No sealed span provides
  one; the sealed vertex structure (matrix-valued, two-time) removes the build's
  scalar-phase mechanism without supplying any exact cancellation in its place;
  the sealed S1 spinor-trace kill (E1v2 :692-694) is a TRACE-sector mechanism, not
  an HS one. B2's norm-sense classification and B4's horn filing are other lenses'
  territory and are not adjudicated here.
DOES NOT: evaluate anything. Whether the ACTUAL two-time difference kernel is
  better or worse than degree -2 at coincidence is left exactly where the sealed
  record leaves it: UNDETERMINED.
```

---

## 9. IMPORT / MACHINERY AUDIT (MINE)

```text
No value of n, kappa_record, alpha, any exponent, coupling, norm, length, scale,
or spectrum computed, bounded, estimated, evaluated, or compared. Degrees (+1, -3,
-2, -3/2 threshold), parities, and quantifier order are symbolic bookkeeping.
Scale-bearing text (ECO, RFA, E1v2, Phase-A) read SUSPECT-ONLY to classify and to
attack; no clause of it used as a positive certifier of any structural claim of
mine — every refutation above stands on: what the sealed text DEFINES (E1v2
:653-654), what it TYPES (:510-512, :696-698, :1111), and what the FORM itself
flags as unsealed (:164-165, :277-281). No GR, no faithfulness premise, no scale
consumed as authority. No register/tracker/plan/road/ledger/lens read. No
STAGE8_CANC_PANEL_* artifact opened. No git action.
```

---

## 10. FLAG BLOCK

```text
DRESSING_OF_RECORD = REFUTED(the a-dependence escapes the pointwise phase through
  the TRANSPORTED GENERATORS: of record the object is V_{mu lambda}(a) :=
  u_mu^{(c)}(a_-)^dagger u_lambda^{(c)}(a_+) (E1 spec v002 :653-654, seal
  46846730..., sidecar MATCH — the same sealed file ECO's kernel quote cites), a
  TWO-TIME Dyson-dressed object whose a-vertex is J = -(Q b_D Q) ⊗ alpha_x
  (:1111): spinor-matrix-valued and interleaved with free h_0 propagation
  (:510-512 "the actual V_i - 1 are Dyson-dressed"; :696-698 "MUST be a TWO-TIME
  (cell-S-matrix) object; the equal-time version is FALSE by C6"). The build's
  identity V_n(a)(x,y) = exp(i[Theta_a(x)-Theta_a(y)]) V_n(0)(x,y) is exactly the
  equal-time scalar-multiplication idealization the seal types FALSE; FORM B5's
  character-only law collects to an endpoint product only on the ready vector
  (FORM :101), not at kernel level. CONFIRMED sub-findings, for fairness: the HS
  measure, the C endcaps, the pointer weights, and the contour carry no
  a-dependence anywhere in the sealed text; the subtraction does remove an
  a-independent baseline.)

FIRST_ORDER_EXACT = REFUTED(actual order NOT OF RECORD. The coefficient
  n<ell,r> consumes a pointwise write-current density that the build's own bedrock
  seals as unsupplied: ell_j is "an incidence datum of the write, NOT sealed as an
  object" (FORM :164-165) and G3's support/current-density realization is NOT
  SUPPLIED (FORM :277-281, B7 :115-119). Higher order is open: a
  singular-support realization makes the phase locally constant a.e. — all-orders
  vanishing off the support. Zeroth order is open: no single-valued Theta_a exists
  around a concentrated current, and at the sealed two-time definition no span
  certifies diagonal vanishing at any order; chi_n(identity)=1 (FORM :168) pins
  coincidence along the RECORD ORDER, not spatial coincidence of the 3d kernel.
  Kept for fairness: where a pointwise nonzero density exists, first order with
  that coefficient is correct, and conservation/transversality cannot raise it.)

FULL_CANCEL_IFF_TRIVIAL_WRITE = REFUTED(the gap: LOCALITY CONFLATION — n != 0
  forces Phi != 0 GLOBALLY (FORM :111-113, :337-339), while full cancellation is
  posed PER DIAMOND (RFA :119-121); in the build's own picture a diamond avoiding
  the (G3-unsupplied) write support fully cancels with the nonzero write intact.
  The biconditional is restored only at every-diamond strength — a quantifier the
  build never states. Secondary: the "THIRD order" threshold is RFA's
  bounded-kernel criterion; the HS object needs only order > 3/2 (order-2)
  vanishing — two sealed criteria fused; and third-order vanishing needs ell and
  its FIRST derivative, not "next two". The whole biconditional is in any case
  conditional on the refuted phase identity: of record it is UNDETERMINED, with
  no sealed span exhibiting full cancellation either.)

DEGREE_BOOKKEEPING = CONFIRMED(as conditional symbolic arithmetic: (+1) + (-3) =
  -2; HS in 3d requires coincidence degree strictly better than -3/2, and degree
  -2 gives |kernel|^2 ~ |r|^-4, radially ~ |r|^-2, HS-divergent — the build's
  threshold claim is right. The error in B3 is not the arithmetic but its PREMISE
  (the uniform O(|r|) prefactor), charged above to B1.)

STRUCTURE_VERDICT = REFUTED(B1: the factorized phase-difference identity is not
  of record, is contradicted in type by the object's sealed definition (two-time,
  Dyson-dressed, matrix-valued a-vertex — E1v2 :510-512, :653-654, :696-698,
  :1111), and its "EXACTLY FIRST ORDER" consumes the unsupplied G3 datum. B3 as
  stated falls with it: "softened to degree -2, still HS-singular" is the
  smooth-density branch of an unsealed trichotomy (order 0 / 1 / all — location-
  dependent), so the surviving residual's DEGREE is not of record. NOT reopened:
  full cancellation by an exact connection-only symmetry — this lens hunted for
  one in the sealed structure and found none; the refutation removes B1's
  mechanism, it does not supply the cancellation the build denies.)

PROVENANCE = CLEAN(all seals verified at path before reliance: build + three
  tasked sources exact; ECO/RFA match the build-recorded digests; FORM's own
  bedrock M03/W/T3 recomputed and matching its recorded first-8; E1v2 sidecar
  MATCH; Phase-A matches E1v2's recorded seal. One citation slip in the build,
  noted not escalated: "no other a-dependence exists anywhere in the law" is FORM
  :162-163 (D2's gloss), not B5 :96-98, and the FORM is itself CLAIMED. The
  material omission — the object's sealed definition (E1v2) absent from the
  build's source list — is charged to B1's verdict above, not to provenance.)

MACHINERY_USED_BY_ME = no(symbolic order/parity/degree/quantifier bookkeeping
  only; nothing computed, bounded, estimated, evaluated, or compared; scale-
  bearing text read SUSPECT-ONLY to classify and attack, never as a positive
  certifier; no register/tracker/plan/road/ledger/lens read; no co-panel artifact
  opened; no git action.)

alpha_computed = false ; kappa_record_computed = false ; proof_authorized = false
ALL_RESULTS = CLAIMED until panel consolidation.
```
