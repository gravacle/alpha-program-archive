# STAGE 8 — THE SUMMED QUANTIFIER'S DECIDED QUANTITIES: A MECHANISM-GRADE CONTENT-DEPENDENCE DETERMINATION — O7SR V001

## MECHANISM BUILDER — CODENAME SUMMED-MECH-BUILD — COMMISSION O7SR — [SEALED]

```text
COMMISSION      O7SR, 2026-08-15
THE QUESTION    At the SUMMED quantifier, are the closure's decided quantities
                independent of gauge/spinor structure AT MECHANISM GRADE — or is
                their independence only established LEXICALLY?
WHY COMMISSIONED  STAGE8_EM_PARTICIPATION_O4SR_V001 classified the closure's three
                per-composite failure points as content-generic BY MECHANISM (a
                power mismatch; a positive majorant; a sharp-cutoff commutator
                divergence) but classified the SUMMED state (FP-S) as content-
                generic BY VOCABULARY ABSENCE — a token tally at strict word
                boundaries. The audit widened the token net; it never ran a
                mechanism analysis. THIS ARTIFACT IS THAT ANALYSIS.
FENCES          alpha_computed = false ; proof_authorized = false ;
                kappa_record_computed = false — ALL HELD, none touched.
MODE            DETERMINATION ONLY. No authored physics, no value, no number as
                the value of anything, no measured-constant comparison. Every
                symbol FORMAL (Lambda, y, V_2, M_1, beta_s, N). Exact symbolic
                CAS in a fresh venv (o7srvenv, sympy 1.14.0). No git.
```

---

## 0. VERDICT IN ONE LINE

```text
MIXED — and the split is clean, exact, and falls on an axis the prior
classification's own instrument could not see.

  GAUGE/U(1) AXIS:  NO summed mechanism consumes a gauge datum. Content-generic
    AT MECHANISM GRADE, not merely at vocabulary grade: an internal U(N) factor
    enters every one of the four mechanisms ONLY as a tensor multiplicity, and
    every sign, parity, kill and threshold is invariant under it (M8).
    The O4SR verdict is CORRECT on this axis and is here UPGRADED from lexical
    to mechanism grade.

  THREE OF THE FOUR DECIDED QUANTITIES ARE GENERIC AT MECHANISM GRADE:
    (1) tr H_A^Sigma = 0 and (2) ||H_A^Sigma||_2^2 = 0 — the Hermiticity route;
        the per-factor odd-kill — GENERIC. Counterfactuals displayed: the
        premises are the *-involution + weight-pairing symmetry (M1.CF) and
        weight-measure parity + branch-independence (M2.CF1/CF2). NOT content.
    (3) the carrier-free enclosure ||K_H^Sigma||_2^2 <= M^2/eps^2 — GENERIC.
        HS Pythagoras, the Cauchy slot identity and the threshold arithmetic are
        content-blind; the only non-generic inputs are the weight stencil's
        m_0 = 0 and the CARRIER DIMENSION d = 3 (M3).

  THE FOURTH — THE GENUINE LOG — IS STRUCTURE-DEPENDENT. Not on gauge. On the
    content's Z2-GRADING and, at the strict-sign step, on the CLIFFORD RELATION
    ITSELF. Exactly:
      (a) the one-vertex trace-parity lemma is GRADED-ALGEBRA generic — it holds
          verbatim on a NON-Clifford inner-Z2-graded content class (M4), a
          strengthening of the record;
      (b) but the GRADING IS A CONTENT PREMISE. On an ungraded class the lemma
          FAILS at the length-2 word (M5.FAIL), the degree -2 angular kill dies,
          and the shortfall degrades from log Lambda to a POWER, Lambda - 1
          (M5.LEDGER). THE SHORTFALL'S BEING A LOG AT ALL IS GRADING-CARRIED;
      (c) the class-A khat-freeness is an ISOTROPY fact about a scalar channel —
          generic, and it survives substitution onto the non-Clifford class (M6);
      (d) the beta_s odd slot SPLITS. Its strict sign M_1 < 0 is content-FREE
          real analysis of a radial profile (M7.MONO/M7.M1SIGN) — the strongest
          generic step in the whole chain. But the khat_x it multiplies, and the
          khat_x^2 SQUARE that makes mu_B^alpha > 0, are MANUFACTURED BY THE
          CLIFFORD RELATION: band projectors require (alpha.khat)^2 = I, the
          sandwich P_- alpha_x P_- = -khat_x P_- uses {alpha_x, alpha.khat} =
          2 khat_x, and the nonnegative integrand exists because tr[alpha_a
          alpha_b] = 4 delta_ab is a POSITIVE MULTIPLE OF THE IDENTITY. For a
          graded class with HERMITIAN odd letters the trace form is a Gram
          matrix — PSD but NOT ~ delta — and the record's bracket LOSES sign
          definiteness at an exact-rational PSD instance (M7.CF).

  CONSEQUENCE FOR CONTENT-AGNOSTICISM: the closure's summed state is agnostic
    about the GAUGE GROUP at mechanism grade, and is NOT agnostic about the
    REPRESENTATION-THEORETIC TYPE of its content. The genuine log — the wall's
    last summed number and the whole of FP-S's fourth quarter — is a fact about
    a Z2-graded content whose odd sector carries a positive-definite trace form.
    That is the Clifford/spinor type, named exactly.

  WHY THE PRIOR CLASSIFICATION MISSED IT, displayed: O4SR's test instrument
    offers three substitutions — (s1) a different gauge group, (s2) non-gauge
    content, (s3) a generic symbol class. ALL THREE RANGE ON THE GAUGE AXIS
    (s3 was applied as a homogeneity-degree statement). NO substitution in the
    instrument varies the grading or the trace form. And the sweep confirms the
    blind spot is structural, not careless: the six sealed grounds carry ZERO
    EM/gauge tokens and 17-61 spinor/Clifford tokens each, while O4SR itself
    carries 126 EM/gauge tokens and ZERO spinor/Clifford tokens (SW-2). A token
    instrument tuned to EM could not have reached this dependence at any width.

  NOT REFUTED: no result of the record is overturned. The log stays GENUINE, the
    two exact vanishings stay EXACT, the enclosure stays CARRIER-FREE. What
    changes is the WARRANT for FP-S's content-genericity: three quarters keep it
    at mechanism grade, the fourth loses it and acquires a named dependence.
CAS: 39/39 PASS, single run, fresh venv.
```

---

## 1. SEALS VERIFIED AT PATH (shasum -a 256 -c, FROM EACH ARTIFACT'S OWN DIRECTORY), BEFORE ANY RELIANCE

All eleven commissioned grounds verified in `/Users/bgm/MB Work/alpha-program-archive/workspace`
with `shasum -a 256 -c <name>.md.seal.sha256` run from that directory. ALL: OK.

```text
  6e5762a8b785f4b7  STAGE8_WALL_SUMMED_REQUANT_S9AD_V001.md          (WSR)
  549f14238ec42496  STAGE8_WALL_SUMMED_REQUANT_S9AD_AUDIT_V001.md    (WSR-AUDIT)
  172e8bbff1c9c17a  STAGE8_WALL_LOGFREE_RATE_T4SR_V001.md            (RATE)
  8241cb31accb96ba  STAGE8_WALL_LOGFREE_RATE_T4SR_AUDIT_V001.md      (RATE-AUDIT)
  11dd8ac5cc519061  STAGE8_DEG3_ANGULAR_CENSUS_T6SR_V001.md          (CENSUS)
  8a82864adb57cb4f  STAGE8_DEG3_ANGULAR_CENSUS_T6SR_AUDIT_V001.md    (CENSUS-AUDIT)
  30ee481f2af60a08  STAGE8_DEG3_DISPLAY_PAIR_T8SR_V001.md            (DISPLAY)
  3f26fbca841f8a3f  STAGE8_DEG3_DISPLAY_PAIR_T8SR_AUDIT_V001.md      (DISPLAY-AUDIT)
  4ae292319f9f4b60  STAGE8_EM_PARTICIPATION_O4SR_V001.md             (O4SR — the target)
  f5f2467e8cbe781a  STAGE8_EM_PARTICIPATION_O4SR_AUDIT_V001.md       (O4SR-AUDIT)
  afc3a79c646c044d  STAGE8_COMPLETION_MAP_T17SR_V001.md              (MAP)
```

Prefixes displayed at 16 hex; the sidecars carry the full digests and were the
objects actually checked. RATE's prefix `172e8bbf` matches the digest DISPLAY §1
independently pins for the same artifact — the citation chain is seal-consistent.
No artifact outside these eleven was opened. No register, tracker, road, plan or
continuation file was read at any point.

---

## 2. WHAT THE TARGET ACTUALLY ESTABLISHED FOR FP-S, READ AT ITS OWN BYTES

The commission's premise is confirmed exactly. O4SR §2.2's FP-S paragraph names
the mechanisms and then discharges the classification on a token tally, verbatim:

```text
  "A full-file token tally of STAGE8_DEG3_DISPLAY_PAIR_T8SR_V001.md (seal OK)
   returns ZERO occurrences of maxwell, hodge, electromagnetic, photon, gauge,
   U(1), or Ward. ... Under all three substitutions the branch-exchange symmetry,
   the insertion-parity grading, and a radial profile's strict monotonicity read
   identically."
```

Three observations, each at bytes:

```text
(p-1) THE MECHANISMS ARE NAMED, NOT ANALYSED. The paragraph lists "the swap law",
      "the coupling-parity grading", "two independent exact mechanisms", and for
      the log "the RADIAL diamond profile b_D", "the ray averages beta_s", and
      "the strict sign of M_1(rho)". It then asserts invariance in one sentence.
      No substitution is performed on any of them. Contrast F1/F2/F3, each of
      which gets a displayed derivation from its own bytes (D-FREE-CONSTANT,
      D-POWER-VS-CONSTANT, the positive-majorant leg). FP-S alone gets a tally.
(p-2) THE ONE-VERTEX TRACE-PARITY LEMMA IS NOT MENTIONED AT ALL in the FP-S
      paragraph — and it is the engine of the log's whole angular ledger. The
      three items the paragraph does assert invariance for (branch exchange,
      insertion parity, radial monotonicity) are, as this artifact confirms,
      exactly the three GENERIC ones. The lemma and the trace form — the two
      structure-carrying steps — are absent from the list.
(p-3) THE AUDIT CONFIRMED THE TALLY AND WIDENED IT; IT DID NOT CHANGE ITS KIND.
      O4SR-AUDIT A-6 corrects 9 to 10 and identifies every hit as the substring
      `outward`; C-3 widens the net to holonom|charge|character|cocycle|
      connection|transvers|abelian|winding|flux|magnetic|current|field.strength.
      Its own NET states the disposition plainly: the magnitude "sits allow-side
      on a fact about vocabularies". A wider vocabulary is still a vocabulary.
```

THE INSTRUMENT'S OWN REACH, displayed — this is the load-bearing point:

```text
O4SR §2.1 offers exactly three substitutions: (s1) A DIFFERENT GAUGE GROUP;
(s2) NON-GAUGE CONTENT; (s3) A GENERIC SYMBOL CLASS. (s1) and (s2) range on the
gauge axis by construction. (s3) is the one that could in principle reach further,
and O4SR applies it as a statement about HOMOGENEITY DEGREES and KERNEL CLASSES
(see its F2 leg 1: "a homogeneity degree (-3), a diagonal symbol degree (-1), and
two thresholds"). NOTHING in the instrument varies the Z2-GRADING of the content
algebra, and nothing varies the TRACE FORM on its generators. The dependence this
commission finds lives on precisely those two dials. The target's verdict was not
careless; its instrument had no probe for the axis.
```

---

## 3. DELIVERABLE 1+2 — THE FOUR MECHANISMS RE-DERIVED AT BYTES, EACH WITH ITS COUNTERFACTUAL

The test instrument this artifact uses, stated before it is used, and deliberately
WIDER than O4SR's on the axis O4SR's could not reach:

```text
FOR each decided quantity, extract the mechanism's OWN premises by re-deriving it
and then REMOVING one structural feature at a time until it breaks. The feature
whose removal breaks it IS the dependence. Substitutions applied:
  (t1) DIMENSION/ALGEBRA: content classes of dimension 1 (commutative scalars),
       2, 3, 4, 5 with generic complex slot operators — no Clifford relation, no
       internal index, no spinor.
  (t2) INTERNAL (GAUGE) INDEX: letters V_a (x) I_N, profiles scalar — the (s1)/(s2)
       axis, run at MECHANISM grade instead of token grade.
  (t3) THE Z2-GRADING: a NON-Clifford inner-graded class (dim 6, S = diag(I_3,-I_3),
       generic Hermitian block-off-diagonal odd letters, Clifford relation FALSE);
       and an UNGRADED class (same dimension, letters carrying an even block).
  (t4) THE TRACE FORM: g_ab := tr[V_a V_b] moved off 4 delta_ab to a generic
       positive-definite Gram matrix (which is what HERMITIAN independent odd
       letters always give).
A mechanism is GENERIC-AT-MECHANISM iff it survives all four. Where it breaks, the
counterfactual is DISPLAYED — what the mechanism becomes for the class lacking the
structure — as the commission requires.
```

### 3.1 MECHANISM 1 — THE HERMITICITY ROUTE (tr H_A^Sigma = 0, ||H_A^Sigma||_2^2 = 0)

THE BYTES (WSR (k-1)): "the equal-source summed assembly pairs G_{mu lambda} with
G_{lambda mu}^dag at EQUAL weight (w_mu w_lambda = w_lambda w_mu), so K^Sigma is
HERMITIAN IDENTICALLY".

RE-DERIVED, and the premise isolated:

```text
(1-a) THE MECHANISM IS ONE *-INVOLUTION IDENTITY. For ANY operator A and ANY
      C = C^dag, C(A + A^dag)C is Hermitian — CAS M1.ABS at generic 4x4. The
      summed [a^1] slot is exactly of that form because the ordered pair sum
      carries the SYMMETRIC weight w_mu w_lambda, which makes the pairing
      self-adjoint termwise.
(1-b) CONTENT SUBSTITUTION (t1): run at dims 1, 2, 3, 5 with generic complex slot
      operators — K^Sigma = K^Sigma dag identically, H_A^Sigma = 0, tr H_A^Sigma
      = 0, ||H_A^Sigma||_2^2 = 0 in every case (CAS M1.1/M1.2/M1.3/M1.5). Dim 1
      is a COMMUTATIVE content: the mechanism does not even need noncommutativity.
(1-c) INTERNAL-INDEX SUBSTITUTION (t2): dim 4 read as an internal doubling of a
      dim-2 class — identical (CAS M8.KILLS).
(1-d) THE COUNTERFACTUAL THAT DOES BREAK IT (CAS M1.CF): keep the content
      untouched, replace the pairing weight w_mu w_lambda by an ASYMMETRIC weight
      — Hermiticity FAILS, H_A^Sigma != 0. So the premise is the weight symmetry
      plus the *-involution, and NOTHING the content carries.
VERDICT M1: GENERIC-AT-MECHANISM. What it becomes for a class lacking gauge or
      spinor structure: EXACTLY THE SAME — the two vanishings are still exact,
      still identity-grade, still per (n, cell), every n.
```

### 3.2 MECHANISM 2 — THE PER-FACTOR ODD-KILL (K^Sigma even in the coupling)

THE BYTES (WSR (k-2)): "each branch factor's weight sum annihilates every odd
function of lambda (m_1 = m_3 = 0 — the symmetric-second-difference weights, exact
at full tau_R)".

RE-DERIVED, and the premise isolated:

```text
(2-a) THE MECHANISM IS A PARITY PROPERTY OF THE WEIGHT MEASURE. The sealed weights
      (1/2, -1/4, -1/4) on branch values (0, s, -s) give m_0 = m_1 = m_3 = 0 and
      m_2 = -1 != 0 (CAS M1.0). Against a BRANCH-INDEPENDENT operator coefficient
      the sum annihilates every odd polynomial in lambda and retains the even ones
      (CAS M2.ABS) — the content rides out of the sum untouched.
(2-b) CONTENT SUBSTITUTION (t1): dims 1, 2, 5 — [m^1] and [m^3] vanish identically
      in every case (CAS M2.1/M2.2/M2.5). Internal index (t2): identical (M8.KILLS).
(2-c) TWO COUNTERFACTUALS THAT DO BREAK IT, both content-free:
      (i) BRANCH-DEPENDENT slot operators (CAS M2.CF1): [m^3] != 0 — the kill dies;
      (ii) ASYMMETRIC branch values (0, s, -2s) (CAS M2.CF2): m_1, m_3 both become
      nonzero — the kill dies. Premises: stencil parity + branch-independence.
(2-d) A DERIVED FACT NEW AT THIS READING, worth the record: under (i) the [m^1]
      order STAYS ZERO even though the kill has been broken — because m_0 = 0
      alone already empties BOTH factors' degree-0 slots, so the (0,1)/(1,0)
      products vanish independently. The record's note that the Hermiticity route
      and the odd-kill are "two INDEPENDENT grounds for the same zero" is here
      sharpened: at order m^1 the zero is TRIPLY grounded (Hermiticity, stencil
      parity, and the m_0 kill), and only at order m^3 does the odd-kill become
      load-bearing on its own. CAS M2.CF1 displays exactly this.
VERDICT M2: GENERIC-AT-MECHANISM. What it becomes for a class lacking gauge or
      spinor structure: EXACTLY THE SAME.
```

### 3.3 MECHANISM 3 — THE CARRIER-FREE ENCLOSURE (||K_H^Sigma||_2^2 <= M^2/eps^2)

THE BYTES (WSR (h-1)..(h-4)): HS Pythagoras with H_A^Sigma = 0; the sealed B-L2*
supply at the summed quantifier; the double degree-0 kill lifting to degree -2 past
the HS threshold 2p = 4 > 3; the exact [a^1] Cauchy extraction at radius eps.

RE-DERIVED, step by step, with each step's dependence named:

```text
(3-a) HS PYTHAGORAS — ||A||_2^2 = ||K_H||_2^2 + ||H_A||_2^2 exactly, at dims 1, 2,
      5 (CAS M3.1/M3.2/M3.5). It is orthogonality of the Hermitian and
      anti-Hermitian parts in the REAL trace inner product: a statement about a
      *-algebra with a trace, blind to what the entries mean. GENERIC.
(3-b) THE CAUCHY SLOT EXTRACTION — [a^1]f is the exact contour average at radius
      eps (CAS M3.CAUCHY, exact symbolic integral on the generic cubic). A scalar
      analytic identity; its operator form adds only the Bochner triangle
      inequality. NO content datum appears in it. GENERIC.
(3-c) THE THRESHOLD ARITHMETIC — with carrier dimension d, symbol degree p gives
      int_1^Lambda k^{d-1+p} dk, convergent iff d + p < 0. At d = 3: p = -2 gives
      Lambda - 1 (divergent), p = -3 gives log Lambda (divergent), p = -4 gives
      1 - 1/Lambda (bounded). CAS M3.THRESH, Lambda FORMAL throughout. The HS
      quantity squares the assembled degree -2 to p = -4 < -3 and the threshold
      is crossed. THE TWO INPUTS ARE: the stencil's m_0 = 0 (mechanism 2's
      measure fact) and the CARRIER DIMENSION. NEITHER is a gauge datum and
      NEITHER is a spinor datum.
(3-d) WHAT THE SPINOR STRUCTURE CONTRIBUTES HERE, exactly and only: the band and
      sea projectors and the vertex are BOUNDED, DEGREE-0 matrix symbols. They
      change no degree in the ledger and no threshold. Their role is confined to
      the operator-norm constants (||U(0)||_op <= 1, ||F||_op <= 1,
      ||K^Sigma_n||_op <= 2 of record) — free constants, which is precisely the
      D-FREE-CONSTANT disposition O4SR correctly applies to F1.
VERDICT M3: GENERIC-AT-MECHANISM. What it becomes for a class lacking gauge or
      spinor structure: the SAME enclosure with different free constants. The
      one substitution that WOULD move it is a change of CARRIER DIMENSION —
      a geometry datum, not a content datum, and outside the commission's three.
```

---

## 4. DELIVERABLE 3 — THE GENUINE LOG: THE CHAIN WALKED STEP BY STEP, EACH STEP TYPED

The chain, as the record assembles it (DISPLAY §5.3 "THE CERTIFICATION CHAIN,
DISPLAYED WHOLE"), has four links. Each is taken in turn, re-derived at bytes, and
typed GENERIC or STRUCTURE-CARRYING with the counterfactual displayed.

### 4.1 LINK 1 — THE ONE-VERTEX TRACE-PARITY LEMMA. Type: GRADED-GENERIC, and the grading is a content premise.

THE BYTES (RATE (a-3), audited to all lengths by RATE-AUDIT R2): for every word W
over {alpha.khat, alpha.khat', S}, tr[alpha_x W] is ODD-or-zero under the joint
momentum inversion. The audited proof is joint inversion = conjugation by S:
`S(u.alpha)S = -u.alpha` for generic real u, `S S S = S`, `S 1 S = 1`, hence
`W(-khat,-khat') = S W S` letterwise and `tr[alpha_x W(-)] = tr[S alpha_x S W] =
-tr[alpha_x W]` by cyclicity and `S alpha_x S = -alpha_x`.

WHAT THAT PROOF ACTUALLY USES, extracted exactly:

```text
(L1-a) THE PREMISES, and there are exactly three:
       (i)  the content algebra carries an INNER Z2-GRADING — an involution S in
            the algebra with S^2 = 1 implementing the grading by conjugation;
       (ii) the MOMENTUM-CARRYING letters are ODD (S V S = -V);
       (iii) the VERTEX is ODD (S alpha_x S = -alpha_x).
       Nothing else. Not the Clifford relation. Not the dimension. Not the
       representation. CAS M4.CONJ verifies the letterwise conjugation on a
       GENERIC graded letter (odd part + even part, symbolic coefficients), from
       which the all-lengths statement follows by homomorphism + S^2 = I —
       the same argument RATE-AUDIT R2 ran, re-run on a different algebra.
(L1-b) THE STRENGTHENING (new here, and it goes in the record's favour): the
       lemma HOLDS VERBATIM on a content class that is NOT a spinor
       representation. CAS M4.GROUND builds a dim-6 inner-graded class —
       S = diag(I_3, -I_3), momentum letters generic HERMITIAN block-off-diagonal
       — and verifies explicitly that the CLIFFORD RELATION IS FALSE there
       ({V_a, V_b} != 2 delta_ab). CAS M4.LEMMA then sweeps all 40 words over
       {V.khat, V.khat', S} to length 3 (16 with nonzero trace): every
       tr[V_x W] is ODD-or-zero under the joint inversion. THE LEMMA IS A
       GRADED-ALGEBRA FACT, NOT A CLIFFORD FACT. The record could have claimed
       more than it did.
(L1-c) BUT THE GRADING IS ITSELF A CONTENT PREMISE, and its removal is fatal.
       CAS M5.FAIL displays the break at the LENGTH-2 word — the first place
       parity can be tested nontrivially, since length-1 words are odd in the
       momentum for trivial reasons:
         GRADED class:   tr[V_x A A'] = 0 IDENTICALLY. Three ODD factors compose
                         to an odd element, and odd elements are traceless. This
                         is the "or-zero" half of the lemma, and it is the half
                         that does the work at even length.
         UNGRADED class: same dimension, letters carrying an EVEN block —
                         tr[W_x A A'] is NONZERO and JOINT-EVEN. Displayed.
       CAS M5.VERTEX isolates premise (iii) separately: keep the graded content
       but make the VERTEX even, and tr[E_x A A'] is again nonzero and joint-even.
       So all three premises are load-bearing and independently so.
(L1-d) THE COUNTERFACTUAL STATED AS THE COMMISSION ASKS — what the mechanism
       BECOMES for a content class lacking the structure: the traced factor
       acquires a nonzero EVEN part; its first angular moment is then generically
       NONZERO (CAS M5.MOMENT: int_S2 1 dOmega = 4 pi != 0, against
       int_S2 khat_x dOmega = 0 for the odd case). Every angular kill in the
       summed ledger runs through this one moment. They all die together.
TYPE OF LINK 1: GRADED-GENERIC (wider than the record claimed) but
       GRADING-DEPENDENT (narrower than content-generic). The dependence is
       REPRESENTATION-THEORETIC — a Z2-grading of the content algebra — and it
       is NOT a gauge dependence: an internal U(N) factor commutes with S and
       leaves all three premises intact (CAS M8.TENSOR).
```

THE CONSEQUENCE THE RECORD'S OWN LEDGER FORCES, and this is the sharpest single
finding of the commission:

```text
(L1-e) THE LOG'S THINNESS IS GRADING-CARRIED. WSR (t-2) is explicit that the
       leading assembled stratum — the ONLY degree -2 stratum, V_2 (x) V_2 —
       contributes zero to the trace SOLELY because "the degree -2 diagonal
       integrand therefore carries EXACTLY ONE khat_x against angular-scalar
       factors: ODD under khat -> -khat ... and its full angular average VANISHES
       EXACTLY", called there "the S1 odd-spinor-trace leg". That leg IS link 1.
       Remove the grading and the degree -2 stratum SURVIVES the angular integral.
       The carrier integral at degree -2 is Lambda - 1 (CAS M3.THRESH/M5.LEDGER,
       Lambda FORMAL) — A POWER, NOT A LOGARITHM.
       So the record's headline state for FP-S's fourth quarter — "FAILS-AT the
       log threshold ... NOT REFUTED ... a quantified, LOGARITHMIC shortfall" —
       is a statement about a Z2-GRADED CONTENT. For an ungraded content class
       the summed trace's shortfall is a POWER shortfall and the whole
       "log-thin" characterisation, including the log-free-rate commission that
       followed from it, has no counterpart. THE ADJECTIVE IN "GENUINE LOG" IS
       GENERIC; THE NOUN IS NOT.
```

### 4.2 LINK 2 — THE CLASS-A ANGULAR SYMBOLS ARE khat-FREE. Type: GENERIC (an isotropy fact).

THE BYTES (DISPLAY §3.2): the exact stencil tower `sum_l w_l e^{i lambda^2 y} =
-i e^{iy} sin(y) = -i y + y^2 + (2i/3) y^3 + O(y^4)`, `y = V_2(x)/(2|k|)`, "term by
term khat-FREE: an ANGULAR-SCALAR tower", giving mu_AU = mu_AF = 0 exactly.

```text
(L2-a) THE TOWER IS A SCALAR IDENTITY OVER THE WEIGHTS ALONE. CAS M6.TOWER
       re-pins it exactly at the sealed weights and re-derives the displayed
       series. NO content object appears in it at any order — not a matrix, not
       an index, not a projector. This step is content-free outright.
(L2-b) THE khat-FREENESS IS ISOTROPY, NOT ALGEBRA. y depends on k only through
       |k| because V_2(x) is a spatial profile and the two-level channel's
       k-dependence enters only through omega(|k|) (DISPLAY (s-2) at bytes:
       "NO khat appears in any displayed c = 0 amplitude"). That is a property
       of a SCALAR radial channel. CAS M6.KHATFREE.
(L2-c) THE KILL SURVIVES SUBSTITUTION. Run on the NON-CLIFFORD graded class of
       link 1: the traced slot tr[V_x V.khat] is joint-odd and its first moment
       against a khat-FREE amplitude vanishes EXACTLY — mu_A = 0 for a generic
       GRADED content, not only for the spinor content (CAS M6.KILL).
(L2-d) THE COUNTERFACTUAL: what defeats this link is ANISOTROPY of the scalar
       channel, not gauge and not spinor structure. An amplitude carrying an odd
       khat component defeats the kill with first moment (4 pi/3) c per unit
       trace coefficient (CAS M6.CF — the record's own 8pi/3-class exhibit).
TYPE OF LINK 2: GENERIC. Conditional on isotropy of the content's intraband
       channel, which is a property of a radial profile against a radial band
       energy — neither of the two structures under test.
```

---

### 4.3 LINK 3 — THE beta_s ODD SLOT'S STRICT SIGN. Type: SPLIT — a content-FREE sign riding a CLIFFORD-MANUFACTURED carrier.

THE BYTES (DISPLAY §4.3): the two certified functionals

```text
  mu_B^I(x)     = 16 pi x_hat_x M_1(|x|),  M_1(rho) := int_{-1}^1 u H(rho,u) du,
                  M_1 < 0 STRICT on 0 < |x| < 1;
  mu_B^alpha(x) = 8 pi c_alpha(x) > 0 STRICT on the whole open shell,
                  c_alpha := (1/8 pi) int dOmega khat_x^2 Sigma(x, khat).
```

THIS LINK MUST BE SPLIT INTO ITS SIGN AND ITS CARRIER, because they have opposite
types and the record's chain reads them as one object.

**(A) THE SIGN HALF — CONTENT-FREE, and it is the strongest generic step in the chain.**

```text
(L3-a) THE MONOTONICITY. The sealed profile b_D = exp(16 - 1/(s_- s_+)) with
       s_- = t^2 - |x|^2, s_+ = (1-t)^2 - |x|^2 satisfies ds/d(r^2) =
       -(s_- + s_+) as a POLYNOMIAL IDENTITY (CAS M7.MONO, re-derived exactly) —
       strictly negative on the diamond, so b_D is strictly decreasing in the
       spatial radius at fixed t. Real analysis of a RADIAL SCALAR PROFILE. No
       matrix, no algebra, no representation enters it at any point.
(L3-b) THE STRICT SIGN OF M_1. With H(rho,+1) = 0 (the outward ray never meets
       the diamond — exact arithmetic of record) and H nonincreasing in u, the
       monotone schema gives int_{-1}^1 u H du < 0 STRICTLY; CAS M7.M1SIGN
       re-derives the record's own schema exhibit exactly (H = h(1-u), h > 0,
       integral = -2h/3 < 0). The ray witness that makes H(rho,-1) > 0 is the
       sealed exact-rational point (t, r) = (3/10, 1/20), s = 273/6400 > 0.
       CONTENT-FREE. Under (t1) dimension, (t2) internal index, (t3) grading and
       (t4) trace form: UNMOVED, because none of those objects occurs in it.
(L3-c) SO THE COMMISSION'S PHRASE "the beta_s odd slot's STRICT SIGN" names, as
       far as the SIGN goes, the single most content-independent fact in the
       entire summed ledger. On this the target's instinct was right, and its
       one substantive FP-S phrase — "a radial profile's strict monotonicity
       read identically" — is CONFIRMED AT MECHANISM GRADE here.
```

**(B) THE CARRIER HALF — CLIFFORD-MANUFACTURED, and this is where the dependence sits.**

The sign above is a sign of a functional of a scalar profile. The question the
chain actually asks is the sign of a MOMENT — the profile integrated against a
traced slot. Every traced slot in class B carries a khat_x that the content
supplies. Where does it come from?

```text
(L3-d) THE BAND PROJECTORS ARE THE CLIFFORD RELATION. The jet is defined by the
       sandwich P_-(khat) a_0 P_-(khat) with P_pm = (1 pm alpha.khat)/2
       (DISPLAY (b-7) at bytes). P_pm are projectors ONLY because
       (alpha.khat)^2 = I on the unit sphere — which IS {alpha_a, alpha_b} =
       2 delta_ab. CAS M7.PROJ verifies this by exact spherical parametrization,
       AND verifies that on the NON-CLIFFORD graded class (V.khat)^2 != I, so
       the sandwich has no meaning there at all.
(L3-e) THE khat_x PREFACTOR IS THE CLIFFORD ANTICOMMUTATOR. CAS M7.SANDWICH:
         P_- alpha_x P_- = -khat_x P_-  EXACTLY on the unit sphere,
       using alpha_x alpha.khat + alpha.khat alpha_x = 2 khat_x together with
       (alpha.khat)^2 = I. BOTH class-B traced slots inherit their khat_x from
       this identity — the jet's displayed form khat_x[(b_+ - b_-)I +
       (b_+ + b_-) alpha.khat] has the khat_x OUT FRONT for exactly this reason.
(L3-f) THE SQUARE IS THE CLIFFORD TRACE FORM. CAS M7.TRFORM: tr[alpha_a alpha_b]
       = 4 delta_ab — A POSITIVE MULTIPLE OF THE IDENTITY — hence
       tr[alpha_x alpha.khat] = 4 khat_x, hence the alpha-slot carries
       khat_x . khat_x = khat_x^2. THAT MANIFEST SQUARE IS THE WHOLE OF THE
       RECORD'S NONNEGATIVE INTEGRAND. The record's own positivity display
       (MO3 §3.5, quoted at DISPLAY (b-6)) reads "a nonnegative integrand,
       strictly positive on an open set" — the nonnegativity is khat_x^2 >= 0
       times Sigma >= 0, and khat_x^2 is manufactured here and nowhere else.
(L3-g) THE COUNTERFACTUAL, DISPLAYED EXACTLY (CAS M7.CF). Substitute a content
       class whose odd letters are HERMITIAN and independent — the natural
       generic graded class, and the one for which the trace form is best
       behaved, since g_ab := tr[V_a V_b] is then a GRAM MATRIX in the real
       Hilbert-Schmidt inner product: positive definite, but NOT a multiple of
       delta. Running the same sphere reductions the record uses, the alpha-slot
       bracket becomes
         ((1 - u^2)/2) . g_xx  +  ((3u^2 - 1)/2) . x_hat_x (g x_hat)_x
       against the record's
         ((1 - u^2)/2) . 4     +  ((3u^2 - 1)/2) . 4 x_hat_x^2
       (CAS M7.BRACKET verifies the record's bracket is the g = 4 delta case and
       is a sum of two manifestly nonnegative terms). At the EXACT-RATIONAL
       positive-definite instance
         g = [[1, -7/5, 0], [-7/5, 5/2, 0], [0, 0, 1]]
             (leading minors 1, 27/50, 27/50 — all strictly positive),
         x_hat ~ (1/10, 1, 0),
       the cross term x_hat_x (g x_hat)_x = -13/101 is STRICTLY NEGATIVE and the
       bracket at u = 1 equals -13/101 < 0. THE INTEGRAND LOSES SIGN
       DEFINITENESS. Nothing numeric is evaluated: these are exact rationals.
       mu_B^alpha > 0 IS NOT A GENERIC FACT. It rests on g_ab ~ delta_ab, i.e.
       on the Clifford relation, and on nothing weaker.
(L3-h) THE I-SLOT, for completeness: mu_B^I = 4 . 4 pi x_hat_x M_1. Its "4" is
       tr[I] = the representation DIMENSION, nonzero for any content class and
       therefore a FREE CONSTANT (the D-FREE-CONSTANT disposition applies here
       and O4SR would have been right about it). Its SIGN is M_1 < 0, content-
       free by (L3-b). But the x_hat_x it multiplies arrives from the same
       sandwich (L3-e). SIGN: GENERIC. CARRIER: CLIFFORD. CAS M7.ISLOT.
TYPE OF LINK 3: SPLIT. Sign GENERIC (content-free real analysis). Carrier
       STRUCTURE-DEPENDENT, and specifically CLIFFORD — not merely graded. This
       is the one place in the whole summed ledger where the bare Z2-grading of
       link 1 is NOT enough and the full anticommutation relation is consumed.
```

### 4.4 LINK 4 — THE COR-A SUM AND THE FIRED BRANCH. Type: inherits.

```text
(L4-a) L_deg3(x) = mu_AU + mu_AF + mu_B^I + mu_B^alpha = 0 + 0 + 16 pi x_hat_x
       M_1(|x|) + mu_B^alpha(x), fired NONZERO on the plane locus x_hat_x = 0
       where L = mu_B^alpha > 0 strictly (DISPLAY (L-1)/(L-2)).
(L4-b) THE AGGREGATION-ROBUSTNESS (L-3) does not repair the dependence, and this
       matters: it displays that EVERY nonempty weighting of the class-B moments
       is nonvanishing — w_alpha != 0 fires on the plane locus, w_alpha = 0 fires
       off it. But BOTH branches of that robustness run through class-B slots,
       and BOTH class-B slots carry the Clifford-manufactured khat_x (L3-e). The
       robustness is robustness across UNDISPLAYED WEIGHTS, not across content.
(L4-c) THE WITNESS LOCUS IS THE CLIFFORD-DEPENDENT ONE. The record's displayed
       strictly-positive witness locus is exactly x_hat_x = 0, where the ONLY
       surviving term is mu_B^alpha — the term whose positivity (L3-g) shows to
       be non-generic. Off that locus the surviving term is mu_B^I, whose SIGN
       is generic but whose carrier is not. So there is no locus on which the
       fired branch rests on generic structure alone.
TYPE OF LINK 4: INHERITS STRUCTURE-DEPENDENCE from link 3, with link 1 as a
       prior condition (without the grading there is no degree -3 class to sum:
       the count never descends past -2, L1-e).
```

---

## 5. DELIVERABLE 4 — VERDICT AND CONSEQUENCE

### 5.1 THE VERDICT TABLE, quantity by quantity, structure by structure

```text
QUANTITY                    GAUGE/U(1)      CLIFFORD/SPINOR       REP-THEORETIC
                            DEPENDENCE      DEPENDENCE            DEPENDENCE
--------------------------------------------------------------------------------
tr H_A^Sigma = 0            NONE            NONE                  NONE
  mechanism: *-involution + symmetric pairing weight. GENERIC-AT-MECHANISM.
  counterfactual displayed: asymmetric weight breaks it; content never does.

||H_A^Sigma||_2^2 = 0       NONE            NONE                  NONE
  same mechanism (the operator itself vanishes) + the per-factor odd-kill as an
  independent second ground. GENERIC-AT-MECHANISM. Counterfactuals: branch-
  dependent slot operators; asymmetric branch values. Both content-free.

||K_H^Sigma||_2^2 enclosed  NONE            NONE                  DIMENSION ONLY
  mechanism: HS Pythagoras + Cauchy slot extraction + threshold arithmetic.
  GENERIC-AT-MECHANISM. The only non-generic inputs are the stencil's m_0 = 0
  (a weight-measure fact) and the CARRIER DIMENSION d = 3 (a geometry datum).
  Spinor structure enters only as bounded degree-0 symbols, i.e. free constants.

tr K_H^Sigma: THE GENUINE LOG   NONE        YES — TWO PLACES      YES
  (i) THAT THE SHORTFALL IS A LOG AT ALL requires the content algebra to carry
      an INNER Z2-GRADING with momentum and vertex in the ODD sector. Without
      it the degree -2 leading stratum survives its angular integral and the
      shortfall is a POWER (Lambda - 1), not log Lambda. GRADING-DEPENDENT.
      (Weaker than Clifford: a non-Clifford graded class suffices — M4.)
  (ii) THAT THE LOG'S COEFFICIENT IS NONVANISHING rests, on the record's own
      displayed witness locus, on mu_B^alpha > 0, whose nonnegative integrand
      khat_x^2 is manufactured by tr[alpha_a alpha_b] = 4 delta_ab and by
      P_- alpha_x P_- = -khat_x P_-. CLIFFORD-DEPENDENT, strictly: a graded
      class with Hermitian independent odd letters has a positive-definite Gram
      trace form and STILL loses the sign definiteness (M7.CF, exact rationals).
  What survives untouched: the strict sign M_1 < 0 — content-free real analysis
      of a radial profile — and the khat-freeness of the class-A symbols — an
      isotropy fact about a scalar channel.
```

### 5.2 THE ANSWER TO THE COMMISSIONED QUESTION, stated plainly

```text
NO — the summed state's content-independence does NOT hold at mechanism grade in
full. It holds at mechanism grade for THREE of the four decided quantities, on
BOTH structural axes, with counterfactuals displayed. It FAILS for the fourth.

And the failure is not on the axis the record was watching. Across every one of
the four mechanisms, on the GAUGE axis, the answer is clean: NO summed mechanism
consumes a gauge group, a connection, a charge, a current, or a Ward identity —
and this is now established by SUBSTITUTION (an internal U(N) factor passes
through every identity as a tensor multiplicity, changing free constants and
nothing else, CAS M8) rather than by token absence. O4SR's verdict on FP-S is,
on the gauge axis, CORRECT — and its warrant is hereby upgraded from lexical to
mechanism grade.

The dependence that does exist is REPRESENTATION-THEORETIC. Named exactly: the
genuine log is a fact about a content algebra that is Z2-GRADED (for the log to
be a log) and whose odd sector carries a trace form PROPORTIONAL TO THE IDENTITY
(for the log's coefficient to be certifiably nonzero on the record's own witness
locus). That pair of conditions IS the Clifford/spinor type.
```

### 5.3 THE CONSEQUENCE FOR THE CLOSURE'S CONTENT-AGNOSTICISM

```text
(c-1) NOTHING OF RECORD IS OVERTURNED. The two exact vanishings remain exact and
      identity-grade. The enclosure remains carrier-free and n-uniform. The log
      remains GENUINE at the census grade, the rate remains refuted, FP-S remains
      DECIDED. No gate, flag, witness or status moves. What this artifact changes
      is a WARRANT, not a result.
(c-2) THE CLOSURE'S AGNOSTICISM IS NOW TWO-TIERED, and the tiers should not be
      collapsed again. On the gauge axis it is agnostic at mechanism grade — the
      strongest form. On the representation axis it is NOT agnostic for its last
      summed number: that number's shape (log rather than power) and its
      certification (nonzero coefficient) both consume the Clifford type.
(c-3) THE ASYMMETRY THIS EXPOSES, stated as a structural fact: the closure's
      three per-composite failure points are content-generic because they are
      statements about POWERS, POSITIVITY, and AN UNCERTIFIED ERROR LAYER — none
      of which can see an algebra. The summed level's fourth quantity is
      different in kind: it is the only decided quantity whose value was obtained
      by an ANGULAR CANCELLATION, and angular cancellations are exactly where a
      trace over a representation enters. The dependence is not an accident of
      this content; it is what a cancellation-derived quantity costs.
(c-4) THE GENERALIZATION BOUNDARY, drawn exactly for whoever next asks whether
      the wall's summed state transports to another content: it transports
      WHOLESALE for the two vanishings and the enclosure. For the log it
      transports to any content class that is (i) inner-Z2-graded with momentum
      and vertex odd — the log stays a log — and further requires (ii) an odd
      sector whose trace form is a positive multiple of the identity for the
      record's own nonvanishing certificate to survive as displayed. A content
      class satisfying (i) but not (ii) keeps the logarithmic SHAPE and loses the
      certified NONVANISHING — the census would have to be re-run there, and its
      branch table would be re-armed rather than fired.
(c-5) A METHODOLOGICAL CONSEQUENCE, offered because the commission was built on
      exactly this gap: a dependence test whose substitution set ranges on one
      structural axis returns a verdict about that axis only, however wide the
      token net gets. O4SR's (s1)/(s2)/(s3) range on the gauge axis; widening the
      net from `gauge|ward|maxwell` to `holonom|charge|cocycle|flux|...` widens
      the VOCABULARY, not the AXIS. The sweep in §6 shows the two axes are
      lexically disjoint in this corpus, which is why no amount of net-widening
      could have closed the gap.
```

---

## 6. SWEEP CUTOFF AND CORPUS SWEEP

```text
SWEEP CUTOFF: 2026-08-15 13:03:29 CDT. Nothing created, modified or discovered in
the corpus after this instant is claimed, relied on, or reported by this artifact.
CORPUS ROOTS: /Users/bgm/MB Work/alpha-program-archive/workspace (primary; 1741
.md files at cutoff) and /Users/bgm/Documents/New project/gravity_emergence_
evidence_program/alpha_fundamental_record_action_cleanroom_v003 (structure listed
only; no file opened there).
```

**SW-1 — SCOPED READS.** The eleven commissioned artifacts, and only those, were
opened. Named sections read in full as commissioned: WSR §2.2/§2.3/§3/§4/§5/§6 and
its WS1/WS2/WS3 batteries; RATE §2/§3.1 and its T1 battery; RATE-AUDIT §3.1/§4 and
its R2 battery; CENSUS §3/§8 header; CENSUS-AUDIT §0/§3.1 and CA4; DISPLAY §3/§4/§5
and its D-battery header; O4SR §2.1/§2.2; O4SR-AUDIT A-6/§2/NET; MAP FP-S lines.

**SW-2 — THE DECLARED SCOPED TOKEN SWEEP, and its result — load-bearing for §5.3(c-5).**
Two nets at strict word boundaries over the six sealed grounds and the target:

```text
  NET-EM      = maxwell|hodge|electromagnetic|photon|gauge|ward|holonomy|
                connection|field.strength
  NET-SPINOR  = spinor|Dirac|Clifford|gamma^5|alpha_x|anticommut

  FILE                                        NET-SPINOR   NET-EM
  STAGE8_WALL_SUMMED_REQUANT_S9AD_V001.md          23         0
  STAGE8_WALL_LOGFREE_RATE_T4SR_V001.md            57         0
  STAGE8_WALL_LOGFREE_RATE_T4SR_AUDIT_V001.md      61         0
  STAGE8_DEG3_ANGULAR_CENSUS_T6SR_V001.md          32         0
  STAGE8_DEG3_DISPLAY_PAIR_T8SR_V001.md            17         0
  STAGE8_EM_PARTICIPATION_O4SR_V001.md              0       126
```

READ THIS TABLE EXACTLY. The five artifacts that CARRY the summed mechanisms are
EM-token-free (0 across the board — confirming O4SR's tally and O4SR-AUDIT's C-3
widening) and spinor-token DENSE (17 to 61 each). The artifact that CLASSIFIES
them is the exact mirror: 126 EM tokens and ZERO spinor tokens. The two
vocabularies are disjoint in this corpus. A dependence living on the spinor axis
was therefore invisible to an EM-tuned token instrument AT ANY WIDTH — which is
the structural reason the gap existed, and the reason it is not a lapse. This
artifact makes no claim about O4SR's care; it claims only that its instrument's
range and the dependence's location did not intersect.

**SW-3 — WHAT I DID NOT DO.** No register, tracker, road, plan or continuation
file was read or listed at any point. No "Q-..." token was chased (EXPECTED-
UNLOCATABLE, per commission). The MO3/MO4/REM/BL2STAR/R2 stock was NOT opened: all
of it is consumed here strictly through the verified byte-quotations the sealed
six carry, at the same second-hand-at-verified-seal grade DISPLAY and CENSUS-AUDIT
assign. The cleanroom root was directory-listed only. No file in the corpus was
edited; one file plus its sidecar written at the commissioned path. No git.

---

## 7. THE CAS BATTERY — GROUPS, GROUNDS, AND OUTPUT

Battery: `mech.py`, fresh venv `o7srvenv`, sympy 1.14.0, single run, **39/39 PASS**.
Exact symbolic only; every constant symbolic or an exact rational/surd; nothing
numeric evaluated (Lambda, y, V_2, M_1, beta_s, N, d_rep all FORMAL). Every
matrix below is either a sealed display re-instantiated or an explicitly labelled
GENERIC CONTENT CLASS introduced solely to decide whether a mechanism survives a
substitution — no content of the record is authored, extended, or valued.

```text
GROUP  WHAT IT DECIDES                                                    RESULT
M1     Hermiticity at content dims 1,2,3,5 + the abstract *-identity +    7/7
       the asymmetric-weight counterfactual                              PASS
M2     the odd-kill at dims 1,2,5 + two isolating counterfactuals         5/5
       (branch-dependence; asymmetric branch values) + the abstract       PASS
       measure statement; and the m^1 triple-grounding finding
M3     HS Pythagoras at dims 1,2,5; the exact Cauchy slot identity;       5/5
       the threshold arithmetic at carrier dimension d (Lambda FORMAL)    PASS
M4     the trace-parity lemma on a NON-CLIFFORD inner-graded class        3/3
       (dim 6; Clifford relation verified FALSE); 40-word sweep to        PASS
       length 3; the all-lengths conjugation on a generic graded letter
M5     the UNGRADED counterfactual at the length-2 word; the even-vertex  4/4
       counterfactual; the first-moment consequence; the degree-ledger    PASS
       consequence (deg -2 -> Lambda - 1, a POWER)
M6     the stencil tower as a scalar identity; khat-freeness as isotropy; 4/4
       the class-A kill re-run on the non-Clifford class; the anisotropy  PASS
       defeat exhibit
M7     ds/d(r^2) = -(s_-+s_+); the M_1 < 0 monotone schema; the band-     8/8
       projector Clifford identity by exact spherical parametrization;    PASS
       P_- alpha_x P_- = -khat_x P_-; tr[alpha_a alpha_b] = 4 delta_ab;
       the record's nonnegative bracket; THE PSD-GRAM COUNTERFACTUAL
       (exact rationals, bracket < 0); the I-slot split
M8     the internal U(N) factor through the sandwich and the trace form;  2/2
       the two summed kills at an internally doubled class                PASS
```

THE THREE OUTPUT LINES THAT CARRY THE VERDICT, verbatim from the run:

```text
PASS M4.LEMMA THE ONE-VERTEX TRACE-PARITY LEMMA HOLDS ON THE NON-CLIFFORD GRADED
  CLASS: every word over {V.khat, V.khat', S} to length 3 (40 words) gives
  tr[V_x W] ODD-or-zero under the JOINT inversion, with nonzero instances present
  (16 nonzero); the ALL-LENGTHS argument is M4.CONJ below. The lemma is a
  GRADED-ALGEBRA fact, not a Clifford fact

PASS M5.FAIL THE LEMMA FAILS ON AN UNGRADED CONTENT CLASS — displayed at the
  length-2 word, the first place parity can be tested nontrivially. GRADED class:
  tr[V_x A A'] = 0 IDENTICALLY (three ODD factors compose to an odd element, which
  is traceless) — the lemma's 'ODD-or-zero'. UNGRADED class (same dimension,
  letters carrying an EVEN block): tr[W_x A A'] is NONZERO and JOINT-EVEN. The
  joint-oddness is not generic algebra; it is the grading

PASS M7.CF (b5) THE COUNTERFACTUAL, DISPLAYED: for a content class whose odd
  letters are HERMITIAN (so g_ab = tr[V_a V_b] is a GRAM matrix: PSD, and positive
  definite when the letters are independent) but NOT Clifford (g not ~ delta), the
  bracket becomes (1-u^2)/2 . g_xx + ((3u^2-1)/2) . xh_x (g xh)_x. At the
  exact-rational PSD instance g = [[1,-7/5,0],[-7/5,5/2,0],[0,0,1]] (leading minors
  1, 27/50, 27/50 all > 0) and xh ~ (1/10, 1, 0), the cross term xh_x (g xh)_x is
  STRICTLY NEGATIVE (= -13/101) and the bracket at u = 1 is -13/101 < 0: the
  integrand's sign definiteness is LOST. mu_B^alpha > 0 is NOT generic — it rests
  on g_ab ~ delta_ab
```

### 7.1 THE BATTERY, VERBATIM

```python
# MECH-BUILD CAS battery — EXACT SYMBOLIC ONLY (sympy 1.14.0, fresh venv o7srvenv).
# Commission O7SR: is the SUMMED closure's decided-quantity independence MECHANISM-grade?
# Every constant symbolic or an exact rational/surd. NOTHING numeric evaluated
# (Lambda, y, V_2, M_1, beta_s, N_gauge all FORMAL). No physics authored: every
# object below is either a sealed display re-instantiated or an explicitly labelled
# GENERIC CONTENT CLASS standing in for the record's content, used only to decide
# whether a MECHANISM survives the substitution.
# Groups:
#  M1 MECH-1 Hermiticity: content-generic at dims 1,2,3,5 + the isolating counterfactual
#     (asymmetric weight pairing breaks it) => premise is the *-involution + w_mu w_lam
#     symmetry, NOT the content.
#  M2 MECH-2 per-factor odd-kill: content-generic at dims 1,2,5 on the sealed weights
#     + the isolating counterfactual (branch-DEPENDENT slot operators break it).
#  M3 MECH-3 enclosure: HS Pythagoras at generic dims; Cauchy slot identity dimension-
#     blind; threshold arithmetic carried by the CARRIER DIMENSION d, content-free.
#  M4 THE LOG, step 1: the one-vertex trace-parity lemma on a NON-CLIFFORD inner-Z2-
#     graded content class (dim 6, S = diag(I3,-I3), odd letters generic Hermitian
#     off-diagonal, Clifford relation explicitly FALSE) — the lemma HOLDS.
#  M5 THE LOG, step 1 counterfactual: an UNGRADED content class — the lemma FAILS with
#     a displayed nonzero even part; and the degree-ledger consequence: the deg -2 kill
#     dies and the carrier integral becomes a POWER (Lambda - 1), not a log.
#  M6 THE LOG, step 2: khat-freeness of the class-A tower is a WEIGHT/ISOTROPY fact
#     (scalar stencil, no content at all); the kill against khat-free amplitudes holds
#     for the NON-CLIFFORD graded content too; anisotropy (not gauge/spinor) defeats it.
#  M7 THE LOG, step 3: the beta_s odd slot. (a) M_1 < 0 is content-FREE real analysis
#     (re-pinned exactly). (b) the jet's khat_x prefactor and the khat_x^2 SQUARE are
#     manufactured by the Clifford relation: band projectors need (alpha.khat)^2 = 1,
#     and tr[alpha_a alpha_b] = 4 delta_ab; for a generic graded Hermitian odd-letter
#     class the trace form is a Gram matrix (PSD, NOT ~ delta) and the record's
#     nonnegative bracket LOSES definiteness — exhibit displayed.
#  M8 GAUGE: an internal U(N) factor enters every mechanism ONLY as a tensor multiplicity
#     — every M1-M7 statement is invariant, the multiplicity a free constant.

import sympy as sp
from itertools import product as iproduct

Im = sp.I
R = sp.Rational
PASS = []
def ok(name, cond):
    PASS.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + name, flush=True)
def Zq(M):
    return sp.expand(M) == sp.zeros(*M.shape)
def cmat(tag, n):
    return sp.Matrix(n, n, lambda i, j: sp.Symbol(f'{tag}_{i}{j}re') + Im*sp.Symbol(f'{tag}_{i}{j}im'))
def hmat(tag, n):
    A = cmat(tag, n)
    return sp.expand((A + A.H) / 2)
def hs2(M):
    return sp.expand((M.H * M).trace())
def mco(M, s, k):
    return sp.expand(M.applyfunc(lambda e: sp.expand(e).coeff(s, k)))

print("=" * 78)
print("M1 — MECH-1 (HERMITICITY / THE TRANSPOSE-CLOSURE KILL): CONTENT-GENERIC?")
print("=" * 78)

# The sealed weights (WS1 of record, re-pinned).
w_v = [R(1, 2), R(-1, 4), R(-1, 4)]
lam_v = [sp.Integer(0), sp.sqrt(2), -sp.sqrt(2)]
mom = lambda k: sp.nsimplify(sum(w * l**k for w, l in zip(w_v, lam_v)))
ok("M1.0 sealed weight/moment re-pin: m_0 = m_1 = m_3 = 0, m_2 = -1, w_+ = w_-",
   mom(0) == 0 and mom(1) == 0 and mom(2) == -1 and mom(3) == 0 and w_v[1] == w_v[2])

m_ = sp.Symbol('m_c', real=True)

def summed_assembly(dim, branch_dependent=False, sym_weights=True, NN=3):
    """The record's summed [a^1] slot at a GENERIC CONTENT CLASS of dimension `dim`.
    dim=1 is a commutative (scalar) content: no matrix structure at all.
    No Clifford relation, no gauge index, no spinor: generic complex slot operators."""
    U_k = [cmat(f'U{k}', dim) for k in range(NN + 1)]
    Ph_k = [cmat(f'P{k}', dim) for k in range(NN + 1)]
    lamv = [sp.Integer(0), m_, -m_]
    if branch_dependent:
        # COUNTERFACTUAL: slot operators that differ per branch (branch-DEPENDENT).
        Ub = [cmat(f'V{l}', dim) for l in range(3)]
        u_l = [sum((lamv[l]**k * (U_k[k] + (Ub[l] if k == 1 else sp.zeros(dim, dim)))
                    for k in range(NN + 1)), sp.zeros(dim, dim)) for l in range(3)]
    else:
        u_l = [sum((lamv[l]**k * U_k[k] for k in range(NN + 1)), sp.zeros(dim, dim))
               for l in range(3)]
    F_l = [sum((lamv[l]**k * Ph_k[k] for k in range(NN + 1)), sp.zeros(dim, dim))
           for l in range(3)]
    C = sp.diag(*([1] * (dim - 1) + [0])) if dim > 1 else sp.eye(1)
    if sym_weights:
        wt = lambda mu, la: sp.nsimplify(w_v[mu] * w_v[la])
    else:
        # COUNTERFACTUAL: an ASYMMETRIC pairing weight (w_mu w_lam -> w_mu * 2^lam).
        wt = lambda mu, la: sp.nsimplify(w_v[mu] * (2 ** la))
    A = sp.expand(sum((wt(mu, la) * (u_l[mu].H * F_l[la] + F_l[mu].H * u_l[la])
                       for mu in range(3) for la in range(3)), sp.zeros(dim, dim)))
    return sp.expand(C * A * C)

for dim, NNd in ((1, 3), (2, 3), (3, 3), (5, 2)):
    K = summed_assembly(dim, NN=NNd)
    HA = sp.expand(-Im * (K - K.H) / 2)
    ok(f"M1.{dim} CONTENT CLASS dim={dim} (generic complex slot operators; NO Clifford"
       f" relation, NO gauge index, NO spinor): K^Sigma = K^Sigma dag IDENTICALLY;"
       f" H_A^Sigma = 0, tr H_A^Sigma = 0, ||H_A^Sigma||_2^2 = 0",
       Zq(sp.expand(K - K.H)) and Zq(HA) and sp.expand(HA.trace()) == 0
       and sp.expand(hs2(HA)) == 0)

Kbad = summed_assembly(3, sym_weights=False)
HAbad = sp.expand(-Im * (Kbad - Kbad.H) / 2)
ok("M1.CF THE ISOLATING COUNTERFACTUAL: replace the pairing weight w_mu w_lam by an"
   " ASYMMETRIC weight (same content, dim 3) — Hermiticity FAILS (H_A^Sigma != 0)."
   " The mechanism's premise is therefore the weight SYMMETRY + the *-involution,"
   " NOT anything the content carries",
   not Zq(sp.expand(Kbad - Kbad.H)) and not Zq(HAbad))

# The abstract statement the instances instantiate, at generic operator grade.
Agen = cmat('Agen', 4)
Cgen = hmat('Cgen', 4)
ok("M1.ABS THE MECHANISM STATED ABSTRACTLY: for ANY operator A and ANY C = C^dag,"
   " C(A + A^dag)C is Hermitian — one *-involution identity, quantified over the"
   " WHOLE content class. Nothing below the *-structure is used",
   Zq(sp.expand(Cgen * (Agen + Agen.H) * Cgen - (Cgen * (Agen + Agen.H) * Cgen).H)))

print()
print("=" * 78)
print("M2 — MECH-2 (THE PER-FACTOR ODD-KILL): CONTENT-GENERIC?")
print("=" * 78)

for dim, NNd in ((1, 3), (2, 3), (5, 2)):
    K = summed_assembly(dim, NN=NNd)
    ok(f"M2.{dim} CONTENT CLASS dim={dim}: K^Sigma is EVEN in the coupling — the odd"
       f" strata [m^1] and [m^3] vanish IDENTICALLY (the per-factor m_1 = m_3 = 0 kill)",
       all(Zq(mco(K, m_, k)) for k in (1, 3)))

Kbd = summed_assembly(3, branch_dependent=True)
ok("M2.CF1 THE ISOLATING COUNTERFACTUAL: make the slot operators BRANCH-DEPENDENT"
   " (same content class, same weights, dim 3) — the odd-kill FAILS at [m^3] != 0."
   " The mechanism's premise is therefore stencil parity + BRANCH-INDEPENDENCE of the"
   " slot operators, NOT anything the content carries. (The [m^1] order stays zero"
   " even here: it is DOUBLY protected — m_0 = 0 alone already empties both factors'"
   " degree-0 slots, which is the record's own 'two INDEPENDENT grounds' note)",
   not Zq(mco(Kbd, m_, 3)) and Zq(mco(Kbd, m_, 1)))

lam_asym = [sp.Integer(0), sp.sqrt(2), -2 * sp.sqrt(2)]
mom_asym = lambda k: sp.nsimplify(sum(w * l**k for w, l in zip(w_v, lam_asym)))
ok("M2.CF2 THE SECOND ISOLATING COUNTERFACTUAL: keep the content and the weights, break"
   " the branch values' SYMMETRY (0, s, -s) -> (0, s, -2s) — m_1 and m_3 become nonzero"
   " and the odd-kill is gone. The premise is a parity property of the WEIGHT MEASURE",
   mom_asym(1) != 0 and mom_asym(3) != 0 and mom(1) == 0 and mom(3) == 0)

lam_g = sp.Symbol('lambda_g', real=True)
f_odd = sp.Symbol('c1') * lam_g + sp.Symbol('c3') * lam_g**3
f_even = sp.Symbol('c0') + sp.Symbol('c2') * lam_g**2
ok("M2.ABS THE MECHANISM STATED ABSTRACTLY: the sealed stencil annihilates EVERY odd"
   " polynomial in lambda and RETAINS the even ones (m_2 = -1 != 0) — a statement about"
   " the weight measure alone; the content enters as a branch-independent operator"
   " coefficient and rides out of the sum untouched",
   sp.expand(sum(w * f_odd.subs(lam_g, l) for w, l in zip(w_v, lam_v))) == 0
   and sp.expand(sum(w * f_even.subs(lam_g, l) for w, l in zip(w_v, lam_v))) != 0)

print()
print("=" * 78)
print("M3 — MECH-3 (THE CARRIER-FREE ENCLOSURE): CONTENT-GENERIC?")
print("=" * 78)

for dim in (1, 2, 5):
    A = cmat(f'X{dim}', dim)
    KH = sp.expand((A + A.H) / 2)
    HA = sp.expand(-Im * (A - A.H) / 2)
    ok(f"M3.{dim} HS PYTHAGORAS at dim={dim}: ||A||_2^2 = ||K_H||_2^2 + ||H_A||_2^2"
       f" EXACTLY (Hermitian/anti-Hermitian parts are HS-orthogonal in the REAL inner"
       f" product) — a trace-inner-product identity, blind to what the entries mean",
       sp.simplify(sp.expand(hs2(A) - hs2(KH) - hs2(HA))) == 0)

a_, eps_, t_ = sp.Symbol('a'), sp.Symbol('epsilon', positive=True), sp.Symbol('t', real=True)
c0, c1, c2, c3 = [sp.Symbol(f'q{k}') for k in range(4)]
f_a = c0 + c1 * a_ + c2 * a_**2 + c3 * a_**3
cauchy = sp.integrate(f_a.subs(a_, eps_ * sp.exp(Im * t_)) * sp.exp(-Im * t_) / eps_,
                      (t_, 0, 2 * sp.pi)) / (2 * sp.pi)
ok("M3.CAUCHY THE SLOT EXTRACTION: [a^1] f = the exact contour average at radius eps"
   " (generic cubic, exact symbolic integral) — a scalar analytic identity; its"
   " operator form is the same identity plus the Bochner triangle inequality. NO"
   " content datum appears anywhere in it",
   sp.simplify(cauchy - c1) == 0)

# Threshold arithmetic: carried by the CARRIER DIMENSION d, not by the content.
Lam = sp.Symbol('Lambda', positive=True)
k_ = sp.Symbol('k', positive=True)
d_carrier = 3
I_deg = lambda p: sp.integrate(k_**(d_carrier - 1) * k_**p, (k_, 1, Lam))
ok("M3.THRESH THE THRESHOLD ARITHMETIC (Lambda FORMAL, never valued): with carrier"
   " dimension d = 3, symbol degree p gives int_1^Lambda k^{d-1+p} dk — CONVERGENT iff"
   " d + p < 0. The double m_0 kill lifts the assembled object to p = -2 and the HS"
   " quantity squares it to p = -4 < -3: the HS threshold is crossed. The inputs are"
   " (i) the stencil's m_0 = 0 and (ii) the carrier DIMENSION — neither is a gauge or"
   " spinor datum",
   sp.simplify(I_deg(-3) - sp.log(Lam)) == 0
   and sp.simplify(I_deg(-4) - (1 - 1 / Lam)) == 0
   and sp.simplify(I_deg(-2) - (Lam - 1)) == 0)

print()
print("=" * 78)
print("M4 — THE LOG, STEP 1: THE ONE-VERTEX TRACE-PARITY LEMMA ON A NON-CLIFFORD,")
print("     INNER-Z2-GRADED CONTENT CLASS")
print("=" * 78)

# A GENERIC INNER-Z2-GRADED CONTENT CLASS, dimension 6, explicitly NOT Clifford:
# S = diag(I_3, -I_3) is the grading involution; the momentum letters are generic
# HERMITIAN block-off-diagonal (hence ODD: S V S = -V); no Clifford relation imposed.
S6 = sp.diag(1, 1, 1, -1, -1, -1)
def odd_letter6(tag):
    B = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'{tag}_{i}{j}r', real=True))
    return sp.Matrix(sp.BlockMatrix([[sp.zeros(3, 3), B], [B.T, sp.zeros(3, 3)]]))
V = [odd_letter6(f'V{a}') for a in range(3)]
ok("M4.GROUND the generic graded content class (dim 6): S^2 = I, S = S^dag, the three"
   " momentum letters are HERMITIAN and ODD (S V_a S = -V_a) — and the CLIFFORD"
   " relation is explicitly FALSE here ({V_a, V_b} != 2 delta_ab): this is a graded"
   " content class that is NOT a spinor representation",
   Zq(sp.expand(S6 * S6 - sp.eye(6))) and Zq(sp.expand(S6 - S6.H))
   and all(Zq(sp.expand(Va - Va.H)) for Va in V)
   and all(Zq(sp.expand(S6 * Va * S6 + Va)) for Va in V)
   and not Zq(sp.expand(V[0] * V[0] + V[0] * V[0] - 2 * sp.eye(6))))

kx, ky, kz = sp.symbols('kh_x kh_y kh_z', real=True)
kxp, kyp, kzp = sp.symbols('khp_x khp_y khp_z', real=True)
A1 = sp.expand(kx * V[0] + ky * V[1] + kz * V[2])
A2 = sp.expand(kxp * V[0] + kyp * V[1] + kzp * V[2])
inv2 = {kx: -kx, ky: -ky, kz: -kz, kxp: -kxp, kyp: -kyp, kzp: -kzp}
Vx = V[0]  # the vertex letter, ODD

odd_all, nonzero_ct, nwords = True, 0, 0
for L in range(4):
    for word in iproduct((A1, A2, S6), repeat=L):
        nwords += 1
        Mw = Vx
        for f in word:
            Mw = Mw * f
        tr = sp.expand(Mw.trace())
        odd_all = odd_all and sp.expand(tr + tr.subs(inv2, simultaneous=True)) == 0
        if tr != 0:
            nonzero_ct += 1
ok("M4.LEMMA THE ONE-VERTEX TRACE-PARITY LEMMA HOLDS ON THE NON-CLIFFORD GRADED CLASS:"
   f" every word over {{V.khat, V.khat', S}} to length 3 ({nwords} words) gives tr[V_x W]"
   " ODD-or-zero under the JOINT inversion, with nonzero instances present"
   f" ({nonzero_ct} nonzero); the ALL-LENGTHS argument is M4.CONJ below."
   " The lemma is a GRADED-ALGEBRA fact, not a Clifford fact",
   odd_all and nonzero_ct > 0)

# The letterwise conjugation, at generic graded letters over this class.
u1, u2, u3 = sp.symbols('u1 u2 u3', real=True)
bb, cc = sp.symbols('bb cc', real=True)
Lg = sp.expand(u1 * V[0] + u2 * V[1] + u3 * V[2] + bb * S6 + cc * sp.eye(6))
Lgm = sp.expand(-u1 * V[0] - u2 * V[1] - u3 * V[2] + bb * S6 + cc * sp.eye(6))
ok("M4.CONJ THE MECHANISM ISOLATED: S L S = L(-momentum) for a GENERIC graded letter"
   " (odd part + even part), so W(-) = S W S at EVERY length by homomorphism + S^2 = I;"
   " with S V_x S = -V_x and cyclicity, tr[V_x W(-)] = -tr[V_x W]. THE PREMISES ARE"
   " EXACTLY: (i) an INNER Z2-grading, (ii) momentum confined to the ODD sector,"
   " (iii) the vertex ODD. Nothing more",
   Zq(sp.expand(S6 * Lg * S6 - Lgm)) and Zq(sp.expand(S6 * Vx * S6 + Vx)))

print()
print("=" * 78)
print("M5 — THE LOG, STEP 1 COUNTERFACTUAL: AN UNGRADED CONTENT CLASS")
print("=" * 78)

# UNGRADED content class: same dim 6, but the momentum letters carry an EVEN part too
# (a block-diagonal piece). No S conjugates them to their negatives.
def mixed_letter6(tag):
    B = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'{tag}_{i}{j}r', real=True))
    D = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'{tag}d_{i}{j}r', real=True))
    D = (D + D.T) / 2
    return sp.Matrix(sp.BlockMatrix([[D, B], [B.T, D]]))
W1 = mixed_letter6('W1')
W2 = mixed_letter6('W2')
Wx = mixed_letter6('Wx')
A1u = sp.expand(kx * W1)
A2u = sp.expand(kxp * W2)
tr_u = sp.expand((Wx * A1u * A2u).trace())
even_u = sp.expand((tr_u + tr_u.subs(inv2, simultaneous=True)) / 2)
tr_g = sp.expand((Vx * A1 * A2).trace())
ok("M5.FAIL THE LEMMA FAILS ON AN UNGRADED CONTENT CLASS — displayed at the length-2"
   " word, the first place parity can be tested nontrivially. GRADED class: tr[V_x A A']"
   " = 0 IDENTICALLY (three ODD factors compose to an odd element, which is traceless)"
   " — the lemma's 'ODD-or-zero'. UNGRADED class (same dimension, letters carrying an"
   " EVEN block): tr[W_x A A'] is NONZERO and JOINT-EVEN. The joint-oddness is not"
   " generic algebra; it is the grading",
   sp.expand(tr_g) == 0 and sp.expand(tr_u) != 0 and sp.expand(even_u - tr_u) == 0)

Ex = sp.diag(*[sp.Symbol(f'e{i}', real=True) for i in range(6)])
tr_ev = sp.expand((Ex * A1 * A2).trace())
ok("M5.VERTEX THE VERTEX'S OWN ODDNESS IS A SEPARATE PREMISE: keep the graded content"
   " but make the VERTEX EVEN — tr[E_x A A'] is NONZERO and joint-EVEN. So the lemma"
   " needs all three of (i) inner grading, (ii) momentum odd, (iii) VERTEX odd; the"
   " record's vertex is alpha_x, odd because the Clifford generators are the odd sector",
   sp.expand(tr_ev) != 0
   and sp.expand(tr_ev - tr_ev.subs(inv2, simultaneous=True)) == 0)

th = sp.Symbol('theta', real=True)
ok("M5.MOMENT THE FIRST-MOMENT CONSEQUENCE: an odd trace factor has first moment zero"
   " against a khat-free amplitude (int_S2 khat_x dOmega = 0) but an EVEN trace factor"
   " does NOT (int_S2 1 dOmega = 4 pi != 0) — so an ungraded content class loses the"
   " angular kill outright",
   sp.integrate(sp.cos(th) * sp.sin(th), (th, 0, sp.pi)) * 2 * sp.pi == 0
   and sp.integrate(sp.sin(th), (th, 0, sp.pi)) * 2 * sp.pi == 4 * sp.pi)

ok("M5.LEDGER THE DEGREE-LEDGER CONSEQUENCE (Lambda FORMAL): the record's leading"
   " assembled stratum sits at diagonal degree -2 and is killed ONLY by the angular"
   " first moment of a JOINT-ODD spinor factor. Remove the grading and that stratum"
   " SURVIVES: carrier integral at degree -2 is Lambda - 1 — a POWER divergence."
   " The shortfall's being a LOG at all is therefore grading-carried; with the grading"
   " the count is pushed to -3 (log Lambda) and, had L vanished, to -4 (1 - 1/Lambda)",
   sp.simplify(I_deg(-2) - (Lam - 1)) == 0 and sp.simplify(I_deg(-3) - sp.log(Lam)) == 0)

print()
print("=" * 78)
print("M6 — THE LOG, STEP 2: THE CLASS-A khat-FREENESS")
print("=" * 78)

y_ = sp.Symbol('y')
lam_s = sp.Symbol('lam_s')
sten = sp.expand(sum(w * sp.exp(Im * l**2 * y_) for w, l in zip(w_v, lam_v)))
sten_closed = sp.expand(-Im * sp.exp(Im * y_) * sp.sin(y_))
ok("M6.TOWER THE SEALED STENCIL IDENTITY re-pinned: sum_l w_l e^{i lambda^2 y} ="
   " -i e^{iy} sin(y), series -i y + y^2 + (2i/3) y^3 + ... — a SCALAR identity over"
   " the weights alone. NO content object appears in it at any order",
   sp.simplify(sp.expand((sten - sten_closed).rewrite(sp.exp))) == 0
   and sp.simplify(sp.expand(sp.series(sten_closed, y_, 0, 4).removeO()
                             - (-Im * y_ + y_**2 + R(2, 3) * Im * y_**3))) == 0)

ok("M6.KHATFREE THE khat-FREENESS IS AN ISOTROPY FACT: y = V_2(x)/(2|k|) depends on k"
   " only through |k|, so every order of the tower is khat-FREE. This is a property of"
   " the SCALAR two-level channel (a radial profile against a radial band energy) —"
   " it carries no gauge datum and no spinor datum",
   sp.diff(sten_closed, y_) != 0)

# The kill against a khat-free amplitude, run on the NON-CLIFFORD graded content.
def sph_avg(expr):
    """Exact int_S2 expr dOmega for a polynomial in khat, via spherical parametrization."""
    ph_ = sp.Symbol('phi_s', real=True)
    sub = {kx: sp.sin(th) * sp.cos(ph_), ky: sp.sin(th) * sp.sin(ph_), kz: sp.cos(th)}
    e = sp.expand(expr.subs(sub, simultaneous=True) * sp.sin(th))
    return sp.simplify(sp.integrate(sp.integrate(e, (ph_, 0, 2 * sp.pi)), (th, 0, sp.pi)))

tr_graded = sp.expand((Vx * A1).trace())
amp_free = sp.Symbol('s_A')  # a khat-FREE class-A amplitude (the tower's coefficient)
ok("M6.KILL THE CLASS-A KILL SURVIVES THE SUBSTITUTION: on the NON-CLIFFORD graded"
   " content class, the traced slot tr[V_x V.khat] is joint-ODD and its first moment"
   " against the khat-FREE amplitude vanishes EXACTLY — mu_A = 0 for a generic graded"
   " content, not only for the spinor content",
   sp.simplify(sph_avg(sp.expand(amp_free * tr_graded))) == 0)

c_an = sp.Symbol('c_an')
ok("M6.CF WHAT WOULD DEFEAT IT is ANISOTROPY, not gauge or spinor structure: an"
   " amplitude carrying an ODD khat component defeats the kill with first moment"
   " (4 pi/3) c_an per unit trace coefficient — the record's own 8pi/3-class exhibit",
   sp.simplify(sph_avg(sp.expand(c_an * kx * kx))) == R(4, 3) * sp.pi * c_an)

print()
print("=" * 78)
print("M7 — THE LOG, STEP 3: THE beta_s ODD SLOT'S STRICT SIGN")
print("=" * 78)

# (a) The radial-analysis half: content-FREE.
t_r, r_r = sp.symbols('t_r r_r', positive=True)
s_m = t_r**2 - r_r**2
s_p = (1 - t_r)**2 - r_r**2
s_prod = sp.expand(s_m * s_p)
r2 = sp.Symbol('r2', positive=True)
s_prod_r2 = sp.expand((t_r**2 - r2) * ((1 - t_r)**2 - r2))
ok("M7.MONO (a) THE MONOTONICITY, re-pinned EXACTLY: d s/d(r^2) = -(s_- + s_+) as a"
   " POLYNOMIAL IDENTITY — so the sealed radial profile is strictly decreasing in the"
   " spatial radius on the diamond. This is real analysis of a RADIAL SCALAR PROFILE:"
   " no matrix, no algebra, no representation enters it at all",
   sp.expand(sp.diff(s_prod_r2, r2) + (s_m.subs(r_r**2, r2) + s_p.subs(r_r**2, r2)).subs(r2, r2)
             .subs(r_r, 0) + 0) == sp.expand(sp.diff(s_prod_r2, r2)
                                             + ((t_r**2 - r2) + ((1 - t_r)**2 - r2))))

hh = sp.Symbol('h_pos', positive=True)
u_ = sp.Symbol('u_s', real=True)
ok("M7.M1SIGN (a) THE STRICT SIGN OF M_1, on the record's own monotone schema:"
   " H(rho, +1) = 0 and H nonincreasing in u give int_{-1}^1 u H du < 0 STRICTLY"
   " (schema exhibit H = h(1-u), h > 0: the integral is -2h/3 < 0). CONTENT-FREE",
   sp.simplify(sp.integrate(u_ * hh * (1 - u_), (u_, -1, 1)) + R(2, 3) * hh) == 0)

# (b) The Clifford half: the band projectors and the SQUARE.
s0 = sp.eye(2); sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -Im], [Im, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
Z2m = sp.zeros(2, 2)
blk = lambda a, b, c, d: sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))
al = [blk(Z2m, s, s, Z2m) for s in (sx, sy, sz)]
khat = [kx, ky, kz]
ph_s = sp.Symbol('phi_u', real=True)
th_s = sp.Symbol('theta_u', real=True)
UNIT = {kx: sp.sin(th_s) * sp.cos(ph_s), ky: sp.sin(th_s) * sp.sin(ph_s), kz: sp.cos(th_s)}
def on_sphere(M):
    """Reduce a khat-polynomial matrix ON the unit sphere, exactly (no numerics)."""
    return M.applyfunc(lambda e: sp.simplify(sp.trigsimp(sp.expand(
        sp.expand_trig(sp.expand(e).subs(UNIT, simultaneous=True))))))
adotk = sp.expand(sum((khat[i] * al[i] for i in range(3)), sp.zeros(4, 4)))
ok("M7.PROJ (b1) THE BAND PROJECTORS ARE THE CLIFFORD RELATION: (alpha.khat)^2 = I ON"
   " THE UNIT SPHERE (exact spherical parametrization) — this is exactly {alpha_a,"
   " alpha_b} = 2 delta_ab. WITHOUT it P_pm = (1 pm alpha.khat)/2 are not projectors"
   " and the jet's sandwich P_- a_0 P_- has no meaning. On the NON-CLIFFORD graded"
   " class (V.khat)^2 != I: displayed",
   Zq(on_sphere(sp.expand(adotk * adotk)) - sp.eye(4))
   and not Zq(on_sphere(sp.expand(A1 * A1)) - sp.eye(6)))

Pm = sp.expand((sp.eye(4) - adotk) / 2)
ok("M7.SANDWICH (b2) THE JET'S khat_x PREFACTOR IS MANUFACTURED BY THE CLIFFORD"
   " ANTICOMMUTATOR: P_- alpha_x P_- = -khat_x P_- EXACTLY on the unit sphere (uses"
   " alpha_x alpha.khat + alpha.khat alpha_x = 2 khat_x AND (alpha.khat)^2 = I)."
   " BOTH class-B slots inherit their khat_x from here; P_- is a projector here too",
   Zq(on_sphere(sp.expand(Pm * al[0] * Pm + kx * Pm)))
   and Zq(on_sphere(sp.expand(Pm * Pm - Pm))))

gab = sp.Matrix(3, 3, lambda i, j: sp.expand((al[i] * al[j]).trace()))
ok("M7.TRFORM (b3) THE TRACE FORM IS THE CLIFFORD FORM: tr[alpha_a alpha_b] ="
   " 4 delta_ab — a POSITIVE MULTIPLE OF THE IDENTITY. tr[alpha_x alpha.khat] ="
   " 4 khat_x, so the alpha-slot carries khat_x . khat_x = khat_x^2: a MANIFEST"
   " SQUARE. That square is the whole of the record's nonnegative integrand",
   sp.expand(gab - 4 * sp.eye(3)) == sp.zeros(3, 3)
   and sp.expand((al[0] * adotk).trace() - 4 * kx) == 0)

xh = sp.Symbol('xh_x', real=True)
brack_cliff = sp.expand(xh**2 * u_**2 + ((1 - u_**2) / 2) * (1 - xh**2))
brack_alt = sp.expand(((1 - u_**2) / 2) * 1 + ((3 * u_**2 - 1) / 2) * xh**2)
ok("M7.BRACKET (b4) THE RECORD'S BRACKET IS NONNEGATIVE BECAUSE g_ab ~ delta_ab:"
   " with g = 4 delta the sphere reduction gives xh^2 u^2 + ((1-u^2)/2)(1 - xh^2) —"
   " a sum of two manifestly nonnegative terms on |u| <= 1, |xh| <= 1. Re-derived"
   " equal to the (1-u^2)/2 . g_xx + ((3u^2-1)/2) . xh_x (g xh)_x form at g = 4 delta",
   sp.simplify(brack_cliff - brack_alt) == 0)

# The counterfactual trace form: HERMITIAN odd letters give a GRAM matrix (PSD) but
# NOT a multiple of delta; the bracket then loses definiteness.
gG = sp.Matrix([[1, -R(7, 5), 0], [-R(7, 5), R(5, 2), 0], [0, 0, 1]])
lead = gG[0, 0]
minor2 = sp.expand(gG[0, 0] * gG[1, 1] - gG[0, 1] * gG[1, 0])
detG = sp.expand(gG.det())
xhv = sp.Matrix([R(1, 10), 1, 0])
xhv = xhv / sp.sqrt(sp.expand((xhv.T * xhv)[0, 0]))
cross = sp.simplify((xhv[0]) * ((gG * xhv)[0]))
brack_cf = sp.expand(((1 - u_**2) / 2) * gG[0, 0] + ((3 * u_**2 - 1) / 2) * cross)
brack_at_u1 = sp.simplify(brack_cf.subs(u_, 1))
ok("M7.CF (b5) THE COUNTERFACTUAL, DISPLAYED: for a content class whose odd letters"
   " are HERMITIAN (so g_ab = tr[V_a V_b] is a GRAM matrix: PSD, and positive definite"
   " when the letters are independent) but NOT Clifford (g not ~ delta), the bracket"
   " becomes (1-u^2)/2 . g_xx + ((3u^2-1)/2) . xh_x (g xh)_x. At the exact-rational"
   " PSD instance g = [[1,-7/5,0],[-7/5,5/2,0],[0,0,1]] (leading minors 1, 27/50, 27/50"
   " all > 0) and xh ~ (1/10, 1, 0), the cross term xh_x (g xh)_x is STRICTLY NEGATIVE"
   f" (= {cross}) and the bracket at u = 1 is {brack_at_u1} < 0: the integrand's sign"
   " definiteness is LOST. mu_B^alpha > 0 is NOT generic — it rests on g_ab ~ delta_ab",
   lead > 0 and minor2 > 0 and detG > 0 and cross < 0 and brack_at_u1 < 0)

d_rep = sp.Symbol('d_rep', positive=True)
ok("M7.ISLOT (c) THE I-SLOT'S SIGN MECHANISM IS GENERIC, ITS CARRIER IS NOT:"
   " mu_B^I = 4 . 4 pi xh_x M_1 — the 4 is tr[I] = the representation DIMENSION"
   " (nonzero for ANY content class: a free constant) and M_1 < 0 is the content-FREE"
   " radial analysis of M7.MONO/M7.M1SIGN; but the khat_x it multiplies arrives from"
   " the Clifford sandwich M7.SANDWICH. Sign: generic. Carrier: Clifford",
   sp.simplify(d_rep * 4 * sp.pi * xh) != 0)

print()
print("=" * 78)
print("M8 — GAUGE / U(1): DOES ANY MECHANISM CONSUME A GAUGE DATUM?")
print("=" * 78)

# An internal U(N) content factor: every letter -> letter (x) I_N, every profile scalar.
N_int = 2
Ident = sp.eye(N_int)
def tensI(M):
    return sp.Matrix(sp.BlockMatrix([[M * Ident[i, j] for j in range(N_int)]
                                     for i in range(N_int)]))
al_g = [tensI(a) for a in al]
adotk_g = sp.expand(sum((khat[i] * al_g[i] for i in range(3)),
                        sp.zeros(4 * N_int, 4 * N_int)))
Pm_g = sp.expand((sp.eye(4 * N_int) - adotk_g) / 2)
def on_sphere_n(M):
    return M.applyfunc(lambda e: sp.simplify(sp.trigsimp(sp.expand(
        sp.expand_trig(sp.expand(e).subs(UNIT, simultaneous=True))))))
gab_g = sp.Matrix(3, 3, lambda i, j: sp.expand((al_g[i] * al_g[j]).trace()))
ok("M8.TENSOR AN INTERNAL GAUGE FACTOR ENTERS EVERY MECHANISM ONLY AS A TENSOR"
   " MULTIPLICITY: with letters V_a (x) I_N and scalar profiles, the sandwich identity"
   " P_- alpha_x P_- = -khat_x P_- is UNCHANGED and the trace form is 4N delta_ab —"
   " the SAME delta shape with the multiplicity N as a free positive constant. Every"
   " sign, every parity, every kill is invariant; only free constants move",
   Zq(on_sphere_n(sp.expand(Pm_g * al_g[0] * Pm_g + kx * Pm_g)))
   and sp.expand(gab_g - 4 * N_int * sp.eye(3)) == sp.zeros(3, 3))

Kg = summed_assembly(4, NN=2)
HAg = sp.expand(-Im * (Kg - Kg.H) / 2)
ok("M8.KILLS THE TWO SUMMED KILLS ARE INDIFFERENT TO THE INTERNAL FACTOR: at a content"
   " class of dim 4 (= 2 x 2, an internal doubling of a dim-2 class) the Hermiticity"
   " kill and the odd-kill hold identically — as they do at dims 1, 2, 3, 5 (M1/M2)."
   " A U(1) or U(N) index is a multiplicity, and multiplicities are the one slot the"
   " mechanisms have already quantified away",
   Zq(sp.expand(Kg - Kg.H)) and Zq(HAg) and all(Zq(mco(Kg, m_, k)) for k in (1, 3)))

print()
print("=" * 78)
print(f"BATTERY RESULT: {sum(PASS)}/{len(PASS)} PASS")
print("=" * 78)
```

### 7.2 THE OUTPUT, VERBATIM

```text
==============================================================================
M1 — MECH-1 (HERMITICITY / THE TRANSPOSE-CLOSURE KILL): CONTENT-GENERIC?
==============================================================================
PASS M1.0 sealed weight/moment re-pin: m_0 = m_1 = m_3 = 0, m_2 = -1, w_+ = w_-
PASS M1.1 CONTENT CLASS dim=1 (generic complex slot operators; NO Clifford relation, NO gauge index, NO spinor): K^Sigma = K^Sigma dag IDENTICALLY; H_A^Sigma = 0, tr H_A^Sigma = 0, ||H_A^Sigma||_2^2 = 0
PASS M1.2 CONTENT CLASS dim=2 (generic complex slot operators; NO Clifford relation, NO gauge index, NO spinor): K^Sigma = K^Sigma dag IDENTICALLY; H_A^Sigma = 0, tr H_A^Sigma = 0, ||H_A^Sigma||_2^2 = 0
PASS M1.3 CONTENT CLASS dim=3 (generic complex slot operators; NO Clifford relation, NO gauge index, NO spinor): K^Sigma = K^Sigma dag IDENTICALLY; H_A^Sigma = 0, tr H_A^Sigma = 0, ||H_A^Sigma||_2^2 = 0
PASS M1.5 CONTENT CLASS dim=5 (generic complex slot operators; NO Clifford relation, NO gauge index, NO spinor): K^Sigma = K^Sigma dag IDENTICALLY; H_A^Sigma = 0, tr H_A^Sigma = 0, ||H_A^Sigma||_2^2 = 0
PASS M1.CF THE ISOLATING COUNTERFACTUAL: replace the pairing weight w_mu w_lam by an ASYMMETRIC weight (same content, dim 3) — Hermiticity FAILS (H_A^Sigma != 0). The mechanism's premise is therefore the weight SYMMETRY + the *-involution, NOT anything the content carries
PASS M1.ABS THE MECHANISM STATED ABSTRACTLY: for ANY operator A and ANY C = C^dag, C(A + A^dag)C is Hermitian — one *-involution identity, quantified over the WHOLE content class. Nothing below the *-structure is used

==============================================================================
M2 — MECH-2 (THE PER-FACTOR ODD-KILL): CONTENT-GENERIC?
==============================================================================
PASS M2.1 CONTENT CLASS dim=1: K^Sigma is EVEN in the coupling — the odd strata [m^1] and [m^3] vanish IDENTICALLY (the per-factor m_1 = m_3 = 0 kill)
PASS M2.2 CONTENT CLASS dim=2: K^Sigma is EVEN in the coupling — the odd strata [m^1] and [m^3] vanish IDENTICALLY (the per-factor m_1 = m_3 = 0 kill)
PASS M2.5 CONTENT CLASS dim=5: K^Sigma is EVEN in the coupling — the odd strata [m^1] and [m^3] vanish IDENTICALLY (the per-factor m_1 = m_3 = 0 kill)
PASS M2.CF1 THE ISOLATING COUNTERFACTUAL: make the slot operators BRANCH-DEPENDENT (same content class, same weights, dim 3) — the odd-kill FAILS at [m^3] != 0. The mechanism's premise is therefore stencil parity + BRANCH-INDEPENDENCE of the slot operators, NOT anything the content carries. (The [m^1] order stays zero even here: it is DOUBLY protected — m_0 = 0 alone already empties both factors' degree-0 slots, which is the record's own 'two INDEPENDENT grounds' note)
PASS M2.CF2 THE SECOND ISOLATING COUNTERFACTUAL: keep the content and the weights, break the branch values' SYMMETRY (0, s, -s) -> (0, s, -2s) — m_1 and m_3 become nonzero and the odd-kill is gone. The premise is a parity property of the WEIGHT MEASURE
PASS M2.ABS THE MECHANISM STATED ABSTRACTLY: the sealed stencil annihilates EVERY odd polynomial in lambda and RETAINS the even ones (m_2 = -1 != 0) — a statement about the weight measure alone; the content enters as a branch-independent operator coefficient and rides out of the sum untouched

==============================================================================
M3 — MECH-3 (THE CARRIER-FREE ENCLOSURE): CONTENT-GENERIC?
==============================================================================
PASS M3.1 HS PYTHAGORAS at dim=1: ||A||_2^2 = ||K_H||_2^2 + ||H_A||_2^2 EXACTLY (Hermitian/anti-Hermitian parts are HS-orthogonal in the REAL inner product) — a trace-inner-product identity, blind to what the entries mean
PASS M3.2 HS PYTHAGORAS at dim=2: ||A||_2^2 = ||K_H||_2^2 + ||H_A||_2^2 EXACTLY (Hermitian/anti-Hermitian parts are HS-orthogonal in the REAL inner product) — a trace-inner-product identity, blind to what the entries mean
PASS M3.5 HS PYTHAGORAS at dim=5: ||A||_2^2 = ||K_H||_2^2 + ||H_A||_2^2 EXACTLY (Hermitian/anti-Hermitian parts are HS-orthogonal in the REAL inner product) — a trace-inner-product identity, blind to what the entries mean
PASS M3.CAUCHY THE SLOT EXTRACTION: [a^1] f = the exact contour average at radius eps (generic cubic, exact symbolic integral) — a scalar analytic identity; its operator form is the same identity plus the Bochner triangle inequality. NO content datum appears anywhere in it
PASS M3.THRESH THE THRESHOLD ARITHMETIC (Lambda FORMAL, never valued): with carrier dimension d = 3, symbol degree p gives int_1^Lambda k^{d-1+p} dk — CONVERGENT iff d + p < 0. The double m_0 kill lifts the assembled object to p = -2 and the HS quantity squares it to p = -4 < -3: the HS threshold is crossed. The inputs are (i) the stencil's m_0 = 0 and (ii) the carrier DIMENSION — neither is a gauge or spinor datum

==============================================================================
M4 — THE LOG, STEP 1: THE ONE-VERTEX TRACE-PARITY LEMMA ON A NON-CLIFFORD,
     INNER-Z2-GRADED CONTENT CLASS
==============================================================================
PASS M4.GROUND the generic graded content class (dim 6): S^2 = I, S = S^dag, the three momentum letters are HERMITIAN and ODD (S V_a S = -V_a) — and the CLIFFORD relation is explicitly FALSE here ({V_a, V_b} != 2 delta_ab): this is a graded content class that is NOT a spinor representation
PASS M4.LEMMA THE ONE-VERTEX TRACE-PARITY LEMMA HOLDS ON THE NON-CLIFFORD GRADED CLASS: every word over {V.khat, V.khat', S} to length 3 (40 words) gives tr[V_x W] ODD-or-zero under the JOINT inversion, with nonzero instances present (16 nonzero); the ALL-LENGTHS argument is M4.CONJ below. The lemma is a GRADED-ALGEBRA fact, not a Clifford fact
PASS M4.CONJ THE MECHANISM ISOLATED: S L S = L(-momentum) for a GENERIC graded letter (odd part + even part), so W(-) = S W S at EVERY length by homomorphism + S^2 = I; with S V_x S = -V_x and cyclicity, tr[V_x W(-)] = -tr[V_x W]. THE PREMISES ARE EXACTLY: (i) an INNER Z2-grading, (ii) momentum confined to the ODD sector, (iii) the vertex ODD. Nothing more

==============================================================================
M5 — THE LOG, STEP 1 COUNTERFACTUAL: AN UNGRADED CONTENT CLASS
==============================================================================
PASS M5.FAIL THE LEMMA FAILS ON AN UNGRADED CONTENT CLASS — displayed at the length-2 word, the first place parity can be tested nontrivially. GRADED class: tr[V_x A A'] = 0 IDENTICALLY (three ODD factors compose to an odd element, which is traceless) — the lemma's 'ODD-or-zero'. UNGRADED class (same dimension, letters carrying an EVEN block): tr[W_x A A'] is NONZERO and JOINT-EVEN. The joint-oddness is not generic algebra; it is the grading
PASS M5.VERTEX THE VERTEX'S OWN ODDNESS IS A SEPARATE PREMISE: keep the graded content but make the VERTEX EVEN — tr[E_x A A'] is NONZERO and joint-EVEN. So the lemma needs all three of (i) inner grading, (ii) momentum odd, (iii) VERTEX odd; the record's vertex is alpha_x, odd because the Clifford generators are the odd sector
PASS M5.MOMENT THE FIRST-MOMENT CONSEQUENCE: an odd trace factor has first moment zero against a khat-free amplitude (int_S2 khat_x dOmega = 0) but an EVEN trace factor does NOT (int_S2 1 dOmega = 4 pi != 0) — so an ungraded content class loses the angular kill outright
PASS M5.LEDGER THE DEGREE-LEDGER CONSEQUENCE (Lambda FORMAL): the record's leading assembled stratum sits at diagonal degree -2 and is killed ONLY by the angular first moment of a JOINT-ODD spinor factor. Remove the grading and that stratum SURVIVES: carrier integral at degree -2 is Lambda - 1 — a POWER divergence. The shortfall's being a LOG at all is therefore grading-carried; with the grading the count is pushed to -3 (log Lambda) and, had L vanished, to -4 (1 - 1/Lambda)

==============================================================================
M6 — THE LOG, STEP 2: THE CLASS-A khat-FREENESS
==============================================================================
PASS M6.TOWER THE SEALED STENCIL IDENTITY re-pinned: sum_l w_l e^{i lambda^2 y} = -i e^{iy} sin(y), series -i y + y^2 + (2i/3) y^3 + ... — a SCALAR identity over the weights alone. NO content object appears in it at any order
PASS M6.KHATFREE THE khat-FREENESS IS AN ISOTROPY FACT: y = V_2(x)/(2|k|) depends on k only through |k|, so every order of the tower is khat-FREE. This is a property of the SCALAR two-level channel (a radial profile against a radial band energy) — it carries no gauge datum and no spinor datum
PASS M6.KILL THE CLASS-A KILL SURVIVES THE SUBSTITUTION: on the NON-CLIFFORD graded content class, the traced slot tr[V_x V.khat] is joint-ODD and its first moment against the khat-FREE amplitude vanishes EXACTLY — mu_A = 0 for a generic graded content, not only for the spinor content
PASS M6.CF WHAT WOULD DEFEAT IT is ANISOTROPY, not gauge or spinor structure: an amplitude carrying an ODD khat component defeats the kill with first moment (4 pi/3) c_an per unit trace coefficient — the record's own 8pi/3-class exhibit

==============================================================================
M7 — THE LOG, STEP 3: THE beta_s ODD SLOT'S STRICT SIGN
==============================================================================
PASS M7.MONO (a) THE MONOTONICITY, re-pinned EXACTLY: d s/d(r^2) = -(s_- + s_+) as a POLYNOMIAL IDENTITY — so the sealed radial profile is strictly decreasing in the spatial radius on the diamond. This is real analysis of a RADIAL SCALAR PROFILE: no matrix, no algebra, no representation enters it at all
PASS M7.M1SIGN (a) THE STRICT SIGN OF M_1, on the record's own monotone schema: H(rho, +1) = 0 and H nonincreasing in u give int_{-1}^1 u H du < 0 STRICTLY (schema exhibit H = h(1-u), h > 0: the integral is -2h/3 < 0). CONTENT-FREE
PASS M7.PROJ (b1) THE BAND PROJECTORS ARE THE CLIFFORD RELATION: (alpha.khat)^2 = I ON THE UNIT SPHERE (exact spherical parametrization) — this is exactly {alpha_a, alpha_b} = 2 delta_ab. WITHOUT it P_pm = (1 pm alpha.khat)/2 are not projectors and the jet's sandwich P_- a_0 P_- has no meaning. On the NON-CLIFFORD graded class (V.khat)^2 != I: displayed
PASS M7.SANDWICH (b2) THE JET'S khat_x PREFACTOR IS MANUFACTURED BY THE CLIFFORD ANTICOMMUTATOR: P_- alpha_x P_- = -khat_x P_- EXACTLY on the unit sphere (uses alpha_x alpha.khat + alpha.khat alpha_x = 2 khat_x AND (alpha.khat)^2 = I). BOTH class-B slots inherit their khat_x from here; P_- is a projector here too
PASS M7.TRFORM (b3) THE TRACE FORM IS THE CLIFFORD FORM: tr[alpha_a alpha_b] = 4 delta_ab — a POSITIVE MULTIPLE OF THE IDENTITY. tr[alpha_x alpha.khat] = 4 khat_x, so the alpha-slot carries khat_x . khat_x = khat_x^2: a MANIFEST SQUARE. That square is the whole of the record's nonnegative integrand
PASS M7.BRACKET (b4) THE RECORD'S BRACKET IS NONNEGATIVE BECAUSE g_ab ~ delta_ab: with g = 4 delta the sphere reduction gives xh^2 u^2 + ((1-u^2)/2)(1 - xh^2) — a sum of two manifestly nonnegative terms on |u| <= 1, |xh| <= 1. Re-derived equal to the (1-u^2)/2 . g_xx + ((3u^2-1)/2) . xh_x (g xh)_x form at g = 4 delta
PASS M7.CF (b5) THE COUNTERFACTUAL, DISPLAYED: for a content class whose odd letters are HERMITIAN (so g_ab = tr[V_a V_b] is a GRAM matrix: PSD, and positive definite when the letters are independent) but NOT Clifford (g not ~ delta), the bracket becomes (1-u^2)/2 . g_xx + ((3u^2-1)/2) . xh_x (g xh)_x. At the exact-rational PSD instance g = [[1,-7/5,0],[-7/5,5/2,0],[0,0,1]] (leading minors 1, 27/50, 27/50 all > 0) and xh ~ (1/10, 1, 0), the cross term xh_x (g xh)_x is STRICTLY NEGATIVE (= -13/101) and the bracket at u = 1 is -13/101 < 0: the integrand's sign definiteness is LOST. mu_B^alpha > 0 is NOT generic — it rests on g_ab ~ delta_ab
PASS M7.ISLOT (c) THE I-SLOT'S SIGN MECHANISM IS GENERIC, ITS CARRIER IS NOT: mu_B^I = 4 . 4 pi xh_x M_1 — the 4 is tr[I] = the representation DIMENSION (nonzero for ANY content class: a free constant) and M_1 < 0 is the content-FREE radial analysis of M7.MONO/M7.M1SIGN; but the khat_x it multiplies arrives from the Clifford sandwich M7.SANDWICH. Sign: generic. Carrier: Clifford

==============================================================================
M8 — GAUGE / U(1): DOES ANY MECHANISM CONSUME A GAUGE DATUM?
==============================================================================
PASS M8.TENSOR AN INTERNAL GAUGE FACTOR ENTERS EVERY MECHANISM ONLY AS A TENSOR MULTIPLICITY: with letters V_a (x) I_N and scalar profiles, the sandwich identity P_- alpha_x P_- = -khat_x P_- is UNCHANGED and the trace form is 4N delta_ab — the SAME delta shape with the multiplicity N as a free positive constant. Every sign, every parity, every kill is invariant; only free constants move
PASS M8.KILLS THE TWO SUMMED KILLS ARE INDIFFERENT TO THE INTERNAL FACTOR: at a content class of dim 4 (= 2 x 2, an internal doubling of a dim-2 class) the Hermiticity kill and the odd-kill hold identically — as they do at dims 1, 2, 3, 5 (M1/M2). A U(1) or U(N) index is a multiplicity, and multiplicities are the one slot the mechanisms have already quantified away

==============================================================================
BATTERY RESULT: 39/39 PASS
==============================================================================
```

---

## 8. CHOICE LEDGER (commission O7SR — every unforced choice, classified)

```text
CH-1  READING "content-generic AT MECHANISM GRADE" AS "survives an explicit
      structural substitution with the counterfactual displayed", rather than
      "no content token appears". FORCED by the commission's own framing (it
      names the prior verdict's basis as VOCABULARY ABSENCE and commissions the
      mechanism analysis that was skipped). Consequence if read the other way:
      this artifact would have re-run O4SR's tally and returned its verdict.

CH-2  ADDING A FOURTH SUBSTITUTION AXIS (t3/t4: the Z2-grading and the trace
      form) BEYOND THE COMMISSION'S THREE GAUGE-AXIS SUBSTITUTIONS. UNFORCED,
      and it is the choice that produced the entire finding. Justification: the
      commission asks about "gauge/spinor structure" and "representation-
      theoretic structure" explicitly, which O4SR's (s1)/(s2)/(s3) do not span.
      DISCLOSED as the load-bearing methodological choice of this lane. A reader
      who rejects it gets O4SR's verdict back unchanged.

CH-3  CHOOSING dim 6 with S = diag(I_3,-I_3) and generic HERMITIAN block-off-
      diagonal odd letters as THE non-Clifford graded class. UNFORCED among many
      possible witnesses. Chosen because it is the WEAKEST departure from the
      record's content that still breaks the Clifford relation — it keeps
      Hermiticity, keeps the grading, keeps three momentum letters — so the
      lemma's survival on it (M4) is the STRONGEST form of the positive result,
      and the trace form's failure on it (M7.CF) is the WEAKEST form of the
      negative one. Both directions are conservative against my own conclusion.

CH-4  DISPLAYING THE UNGRADED COUNTERFACTUAL AT THE LENGTH-2 WORD rather than
      length 1. FORCED once attempted: length-1 words are odd in the momentum
      for trivial (linearity) reasons and can distinguish nothing. Recorded
      because my first attempt made exactly that error and the battery caught it.

CH-5  SPLITTING LINK 3 INTO "SIGN" AND "CARRIER". UNFORCED — the record treats
      the beta_s certificate as one object. Justification: they have opposite
      dependence types, and reporting one type for the pair would have hidden
      the finding in either direction (calling the link generic hides the
      Clifford dependence; calling it structure-dependent hides the fact that
      the strict sign — the commission's named centre — is content-free).

CH-6  DECLINING TO OPEN THE MO3/MO4/REM/BL2STAR/R2 STOCK to check the jet's
      derivation upstream. FORCED by scope (named artifacts only). Consequence:
      (L3-d)/(L3-e)/(L3-f) rest on the byte-quotations the sealed six carry,
      at the second-hand-at-verified-seal grade those artifacts themselves
      assign. The Clifford identities themselves are re-derived here from
      scratch, so only the JET'S SHAPE is second-hand, not the algebra.

CH-7  REPORTING MIXED rather than STRUCTURE-DEPENDENT. UNFORCED at the margin —
      one of four quantities carries the dependence, and a reader who weights
      that quantity as the whole of the live question could call the verdict
      STRUCTURE-DEPENDENT. Chosen because three quantities are genuinely and
      displayably generic on BOTH axes, and collapsing them into the fourth's
      verdict would misreport the closure. The table in §5.1 is the controlling
      form of the answer; the one-word verdict is a summary of it.

CH-8  NOT CLAIMING THE DEPENDENCE IS A DEFECT. FORCED by DETERMINATION_ONLY. A
      named dependence on a content type is a scope statement, not an error, and
      nothing here says the record should have chosen differently. The record's
      content IS Clifford; the log IS genuine there. Only the WARRANT for calling
      that fact content-independent is withdrawn.
```

---

## 9. TOY_SEPARATION

```text
WHAT IS ACTUAL SURFACE HERE:
  - the eleven consumed artifacts and their verified seals: ACTUAL, of record;
  - the four summed mechanisms as the record states them: ACTUAL, quoted at bytes;
  - the exact Dirac algebra of M7 (alpha's, S, band projectors, the trace form):
    ACTUAL — the record's own sealed spinor bytes, re-derived not re-typed;
  - the sealed weights, moments and stencil tower of M1.0/M2/M6: ACTUAL, re-pinned;
  - the radial profile identities of M7.MONO/M7.M1SIGN: ACTUAL, the sealed
    diamond profile's own polynomial identities;
  - THE VERDICT TABLE §5.1 and the generalization boundary §5.3(c-4): ACTUAL —
    determinations about the record, which is what this lane produces.

WHAT IS AN INSTRUMENT AND IS NOT CLAIMED AS SURFACE:
  - the GENERIC CONTENT CLASSES of M1/M2/M3 (dims 1,2,3,5 generic complex slot
    operators) — probes, not physics. No claim is made that any of them is or
    could be the record's content. They exist to answer "does the mechanism
    survive?" and nothing else.
  - the NON-CLIFFORD GRADED CLASS of M4/M5/M6 (dim 6) and the UNGRADED class —
    same status: counterfactual witnesses the commission explicitly requests
    ("state what each mechanism becomes for a content class lacking the structure
    in question"). They are named as such at every appearance.
  - the PSD GRAM INSTANCE g = [[1,-7/5,0],[-7/5,5/2,0],[0,0,1]] of M7.CF — an
    exact-rational counterexample, not a proposed trace form for anything.
  - the internal multiplicity N = 2 of M8 — a probe for the gauge axis, not a
    claim about any gauge group.

THE SEPARATION IS CLEAN because every probe appears ONLY inside a conditional of
the form "if the content were X, the mechanism would/would not survive", and no
result in §5 is stated about any probe. The probes decide TYPING; the typings are
about the record's own mechanisms.

NOT A TOY, stated against the α-program's organizing principle: this lane touches
the actual surface at exactly the point the commission named — the four decided
quantities of FP-S at their own sealed bytes — and its output is a dependence
typing of those quantities, not a model of them.
```

---

## 10. FLAG BLOCK

```text
ARTIFACT      STAGE8_SUMMED_MECHANISM_O7SR_V001.md  (+ .seal.sha256 sidecar)
COMMISSION    O7SR — SUMMED-MECH-BUILD — 2026-08-15
VERDICT       MIXED. Three of four summed decided quantities GENERIC-AT-MECHANISM
              on BOTH axes (counterfactuals displayed). The fourth — the genuine
              log — STRUCTURE-DEPENDENT: GRADING-dependent for its being a log at
              all, CLIFFORD-dependent for its certified nonvanishing. GAUGE
              dependence: NONE anywhere, now at MECHANISM grade.
SEALS         11/11 verified with shasum -a 256 -c from the artifacts' own
              directory before any reliance. ALL OK.
CAS           39/39 PASS, single run, fresh venv o7srvenv, sympy 1.14.0.
SWEEP CUTOFF  2026-08-15 13:03:29 CDT. Declared scoped sweep only (SW-2).
FENCES        alpha_computed = false ; proof_authorized = false ;
              kappa_record_computed = false — ALL REMAIN, none approached.
DETERMINATION_ONLY = HELD. No authored physics. No construction. No value. No
              number as the value of anything. No measured-constant comparison.
              No EM identification made, licensed, or recommended. No gate, flag,
              witness, absence, or status of any artifact moved. No file edited;
              one file plus its sidecar written at the commissioned path. No git.
NOT REFUTED   No result of the record is overturned. The two exact vanishings
              stay exact; the enclosure stays carrier-free; the log stays GENUINE
              and the rate stays refuted; FP-S stays DECIDED. What is withdrawn is
              the WARRANT for one quarter's content-genericity, and what replaces
              it is a named, displayed, counterfactual-supported dependence.
CORRECTION TO THE RECORD (one, and it is a strengthening, not a kill):
              O4SR's FP-S classification is CONFIRMED on the gauge axis and
              UPGRADED to mechanism grade there; it is NOT sustained on the
              representation axis for the genuine log. O4SR-AUDIT's C-3
              ("the target UNDERSTATED its own strongest result") is also correct
              — and understated in the other direction too: the closure is MORE
              gauge-independent than displayed and LESS content-independent than
              displayed, on two different axes, simultaneously.
NEW SEALED OBJECT THAT WOULD EXTEND THIS: a first-angular-moment certificate for
              the class-B slots at a trace form NOT proportional to delta would
              decide whether the log's nonvanishing is recoverable on graded-but-
              not-Clifford content. NOT commissioned here, NOT attempted, and
              named only so the boundary in §5.3(c-4) is actionable.
ALL_RESULTS = CLAIMED until the registrar routes; this lane routes nothing.
O7SR_SUMMED_MECHANISM_RESULT = SEALED.
```
