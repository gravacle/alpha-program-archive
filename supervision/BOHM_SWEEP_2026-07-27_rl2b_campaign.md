> Source: Bohm reviewer-lane ruled-state sweep, 2026-07-27. RAW SWEEP OUTPUT.
> The compile step truncated; these source sweeps are the complete record.
> Verification: the `rulings`, `derived-vs-adopted` and `rl2b-campaign` sweeps were
> adversarially refuted and survived. The `traps`, `route-graveyard` and `conditionals`
> refuters FAILED on API errors — those three are SINGLE-PASS, UNVERIFIED. Treat as leads.

# THE R-L2b CAMPAIGN: STANDING BRIEFING ON STRUCTURE AND STATE (as of 2026-07-27 16:39, corpus alpha_fundamental_record_action_cleanroom_v003)

## [SEALED SPEC DEFINITION — the exponent is explicitly NOT ASSERTED; R-L2b is the obligation to derive it] S2 / G_hs — THE OBJECT R-L2b IS ABOUT (defining text)
- **Statement:** The object is the SCAD constant S2, a per-cell functional G_hs(C,eps) := |C|_4^{-alpha} * || C(V(a)-V(0))C ||_2. The form in the sweep prompt is CONFIRMED VERBATIM. It is the SUBTRACTED Hilbert-Schmidt density. The norm is the Schatten-2 (Hilbert-Schmidt) norm. The exponent alpha is an exponent OF |C|_4, the cell 4-volume — NOT of a separation, not of a norm, not the fine-structure constant. The spec explicitly refuses to assert its value.
- **Source:** `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:696` (SEALED (STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md.seal.sha256))
- **Quote:** S2. G_hs(C, eps)  := |C|_4^{-alpha} · || C(V(a) - V(0))C ||_2
      [SUBTRACTED HILBERT-SCHMIDT DENSITY. MUST be a TWO-TIME (cell-S-matrix)
       object; the equal-time version is FALSE by C6. *** THE EXPONENT alpha
       IS NOT ASSERTED. *** v001 wrote 1/2 without derivation; R-L2b must
       DERIVE it. Until R-L2b closes, alpha is a symbol, not 1/2.]
- **Why it matters:** This is the single object the whole campaign is about. Any lane restating R-L2b must restate THIS. Note the two-time requirement: computations on the instantaneous/equal-time generator insertion are NOT about the sealed object (see INSTANCE-9 item).

## [SEALED DEFINITION (Carleman setup)] THE VARIABLE, THE DOMAIN, AND THE OPERATOR — Delta and A (defining text)
- **Statement:** The operator inside the norm is Delta_{mu lambda}(a) := A(a) - A(0) = C(V(a)-V(0))C, with A_{mu lambda}(a) := C(V_{mu lambda}(a) - 1)C. The variable is the per-cell complexified history a (per-cell a_c); the domain used elsewhere in the architecture is the closed pair polydisc |a_c| <= eps_star. C is the sea projector C = 1_{(-inf,0)}(h_0). mu,lambda are colour-pair indices, and the sups are taken over states and over colour pairs ON THE SURVIVING SECTOR ONLY.
- **Source:** `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:660` (SEALED (X.md.seal.sha256))
- **Quote:**     A_{mu lambda}(a)     := C(V_{mu lambda}(a) - 1)C
    Delta_{mu lambda}(a) := A(a) - A(0) = C(V(a) - V(0))C
    A_{mu lambda,s}(a)   := A(0) + s Delta(a),  s in [0,1]
- **Why it matters:** Names the variable (a), the sandwich (C ... C), and fixes that R-L2b's object is a DIFFERENCE, not a bare operator. The difference structure is load-bearing for every subsequent argument.

## [SEALED DEFINITION] |C|_4 IS THE CELL 4-VOLUME — what the exponent is an exponent OF
- **Statement:** |C|_4 is defined by the spec as the cell 4-volume, and by the transport charter as the sealed tetrad/Jacobian 4-volume summed over the diamond decomposition. alpha is therefore an exponent on CELL SIZE, not on inter-cell separation.
- **Source:** `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:436` (SEALED (X.md.seal.sha256))
- **Quote:** with `|C|_4` the cell 4-volume and both `eta_1`, `eta_{>=2}` functionals of
`(||b_D||, tau_R, sea-kernel decay data, |w_lambda|)` only, carrier-index-blind,
stated over the envelope-profile class.
- **Why it matters:** This is the axis distinction that the corpus repeatedly says lanes get wrong: |C|_4 (cell size) versus R (inter-cell separation). See the D-1 item.

## [OPEN — named obligation with a named failure witness] R-L2b — THE OBLIGATION AS CHARTERED IN THE SPEC
- **Statement:** R-L2b is the scaling-exponent derivation. It must certify ||C(V(a)-V(0))C||_2 <= |C|_4^{alpha} G_hs with G_hs finite UNIFORMLY over the D3 refinement quantifier, EXHIBITING THE MECHANISM that supplies the powers. Same for beta and G_cm. Witness on failure: SCAD_HS_SCALING_EXPONENT_UNDERIVED.
- **Source:** `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:826` (SEALED (X.md.seal.sha256))
- **Quote:** R-L2b SCALING-EXPONENT DERIVATION (new; C-13). DERIVE alpha (and beta):
      certify || C(V(a) - V(0)) C ||_2 <= |C|_4^{alpha} G_hs with G_hs finite
      uniformly over the D3 refinement quantifier, EXHIBITING THE MECHANISM
      that supplies the powers — cell time extent from the Duhamel bound, and
      the Gevrey b_D. State the same for beta and G_cm. alpha = 1/2 may be the
      answer; it may not be the assumption.
      Witness: SCAD_HS_SCALING_EXPONENT_UNDERIVED.
- **Why it matters:** The authoritative statement of what must be delivered. Note 'EXHIBITING THE MECHANISM' — a bound without a mechanism does not discharge it.

## [OPEN — part of R-L2b's deliverable, routinely omitted when the campaign is summarised] THE COMPANION EXPONENT beta (S2b / G_cm) — derived WITH alpha under R-L2b
- **Statement:** S2b defines G_cm(C,eps) := |C|_4^{-beta} * (certified bound on the C-L2 commutator error [h_0, M(t) tensor S]). beta is explicitly to be derived WITH alpha under R-L2b. S2b replaces the DELETED S3/G_bl. Witness: E1_RECORD_KINK_COMMUTATOR_FORM_UNCERTIFIED.
- **Source:** `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:702` (SEALED (X.md.seal.sha256))
- **Quote:** S2b. G_cm(C, eps) := |C|_4^{-beta} · (certified bound on the C-L2 commutator
       error [h_0, M(t) ⊗ S] in the quadratic form C-L2 names)
      [*** REPLACES THE DELETED S3/G_bl. *** ... beta is derived with alpha under R-L2b.
- **Why it matters:** R-L2b is TWO exponents, not one. Every campaign summary that says 'derive alpha' is under-stating the obligation by half.

## [DELETED OBJECT — but the alpha = 0 mechanism's transfer to the LIVE S2 is OPEN in both directions] S3 / G_bl IS DELETED — and its alpha = 0 pathology is deployed as a LIVE WARNING ABOUT S2
- **Statement:** S3 (the equal-time baseline HS density G_bl) is REMOVED FROM THE ARCHITECTURE; any reappearance of G_bl or of any norm of the baseline BLOCKS with witness SCAD_BASELINE_NORMED. Its recorded pathology is 'the true scaling is alpha = 0', arising by dilation covariance (||CPC||_2 radius-independent, infinite by C6) — a scale-invariant numerator over |C|_4^{alpha} -> 0.
- **Source:** `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:710` (SEALED (X.md.seal.sha256))
- **Quote:** S3. *** DELETED. *** G_bl (the equal-time baseline HS density) is REMOVED FROM
      THE ARCHITECTURE. ... ANY REAPPEARANCE OF G_bl OR OF ANY NORM OF
      THE BASELINE BLOCKS with witness SCAD_BASELINE_NORMED.
- **Why it matters:** DO NOT re-propose bounding a baseline norm — it BLOCKS by name. And do NOT treat the alpha = 0 pathology as safely quarantined in a deleted object; see the next item.

## [OPEN — named, well-posed, narrower than R-L2b, NOT BEGUN] THE alpha = 0 TRANSFER QUESTION — the one place a forcing result could still come from
- **Statement:** Whether divergence MECHANISM 2 — the |C|_4-scaling exponent, the thing 'alpha = 0' names — transfers from the deleted S3 to the live S2 is OPEN. Sealed text is silent in BOTH directions: no sentence transfers it, and no sentence protects S2 from it. The corpus deploys the alpha = 0 fact INSIDE the S2 bookkeeping-downgrade block, i.e. as a live warning about S2. An earlier assertion that S2 escapes it 'in the corpus's own words' was CAUGHT AS A SMUGGLE and removed.
- **Source:** `STAGE8_IS_RL2B_FAILURE_FORCED_BY_F5_DETERMINATION_V001.md:136` (SEALED (X.md.seal.sha256))
- **Quote:** HONEST STATEMENT: whether mechanism 2 transfers from the deleted S3 to the live S2 IS OPEN, and
the corpus treats it as a live warning rather than a settled non-issue. That does not establish
forcing — an unresolved warning is not a proof — but it forbids the comfortable reading that the
pathology is safely confined to a deleted object.
- **Why it matters:** Named twice as THE live successor test (also at STAGE8_DISCRIMINATOR_CLAIM_WITHDRAWAL_V001.md:132-135). Do not re-derive the question; it is already posed and un-attempted.

## [SEALED / FROZEN INPUT (C1). Contradicting it without a new exact witness BLOCKS.] THE SEALED SEA COVARIANCE C1 — the kernel every attempt is run against
- **Statement:** C = 1_{(-inf,0)}(h_0); C(p) = (I - alpha.p-hat)/2; C(r) = (1/2)delta^3(r) I - i alpha·r/(2 pi^2 |r|^4); off-diagonal operator modulus EXACTLY 1/(2 pi^2 |r|^3); homogeneous degree -3; odd, Calderon-Zygmund; int_{a<|r|<R} |C_off| d^3r = (2/pi) log(R/a) EXACTLY, divergence at the UV/coincidence end. 'E1 is a LEMMA UNPROVEN ABOUT A FULLY KNOWN OBJECT.'
- **Source:** `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:320` (SEALED (X.md.seal.sha256))
- **Quote:** C1  SEA COVARIANCE PINNED EXACTLY, NOT BY CLASS. C = 1_(-inf,0)(h_0),
    C(p) = (I - alpha·p-hat)/2,
    C(r) = (1/2) delta^3(r) I - i alpha·r/(2 pi^2 |r|^4);
    off-diagonal operator modulus EXACTLY 1/(2 pi^2 |r|^3); homogeneous
    degree -3; odd (zero spherical mean; Calderon-Zygmund).
- **Why it matters:** The object is fully known; the difficulty is not ignorance of the kernel. The 'alpha' in C(p) = (I - alpha.p-hat)/2 is the DIRAC ALPHA MATRIX — a third distinct 'alpha' in this campaign alongside the S2 exponent and the fine-structure constant.

## [SEALED / FROZEN INPUT (C6), with an adopted locus refinement] C6 — TWO-TIME REQUIRED, AND ITS LOCUS IS THE VOLUME DIAGONAL
- **Statement:** Equal-time localization of the 3-D massless Dirac sea fails Shale-Stinespring: ||[C,1_B]||_2 = +infinity; a Lipschitz cutoff still gives int dr/r^2, divergent. Only two-time / scattering-type objects, where the cell time integration supplies the missing decay, CAN work. Locus refined of record: the fatal local integral is the VOLUME DIAGONAL x = y, NOT the sharp boundary; smoothing only the boundary will not remove a |x-y|^-3 positive majorant.
- **Source:** `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:353` (SEALED (X.md.seal.sha256))
- **Quote:** C6  THE BLOCK IS CONFINED TO n = 1 — AND ITS LOCUS IS THE VOLUME DIAGONAL.
    Equal-time localization of the 3-D massless Dirac sea fails
    Shale-Stinespring: ||[C, 1_B]||_2 = +infinity; a Lipschitz cutoff still
    gives int d^3 r · r^2/r^6 = int dr/r^2, divergent. Only TWO-TIME /
    scattering-type objects, where the cell time integration supplies the
    missing decay, can work.
- **Why it matters:** DEAD ROUTE FENCE: a smoothed-localizer successor MAY NOT FIX THE OBSTRUCTION AT ALL. And C6's 'supplies the missing decay' is a MODAL clause carrying NO EXPONENT — citing it for a quantity is 'citing a modal for a quantity' (see the modal-hazard item).

## [NAMESPACE HAZARD — ACTIVE. Three distinct 'alpha's: the S2 exponent, the Dirac alpha matrices in C(p), and the fine-structure constant.] 'alpha' IN R-L2b IS A SCHATTEN-2 SCALING EXPONENT — NOT THE FINE-STRUCTURE CONSTANT
- **Statement:** The campaign charter names obligation 1 as 'R-L2b itself — the Schatten-2 scaling exponent'. All artifacts in the campaign carry alpha_computed = false in the same status blocks in which they discuss alpha the exponent.
- **Source:** `STAGE8_EXTENSIVITY_VERDICT_AND_RL2B_CAMPAIGN_OPENING_V001.md:87` (SEALED (X.md.seal.sha256))
- **Quote:**   1. R-L2b itself — the Schatten-2 scaling exponent.
- **Why it matters:** Conflation here would be catastrophic and is easy: every artifact says both 'alpha' and 'alpha_computed = false' within twenty lines of each other.

## [ADOPTED CAMPAIGN STRUCTURE (this lane's charter, recorded explicitly at the principal's direction)] THE FOUR CONSUMERS — 'FOUR OBLIGATIONS ARE ONE ESTIMATE' (the charter text)
- **Statement:** The campaign charter declares four obligations to be one estimate: (1) R-L2b itself; (2) T11's response half — response-map pullback commutation and boundary-subextensive invariance; (3) the D3 refinement-natural weight's RESPONSE side (its weight side is closed exactly and unconditionally); (4) CONNECTED EXTENSIVITY, via convergence of sum_n tau_R^n <B_K(A)^n>_connected / n! uniformly as cells shrink at FIXED tau_R.
- **Source:** `STAGE8_EXTENSIVITY_VERDICT_AND_RL2B_CAMPAIGN_OPENING_V001.md:86` (SEALED (X.md.seal.sha256))
- **Quote:** FOUR OBLIGATIONS ARE ONE ESTIMATE:
  1. R-L2b itself — the Schatten-2 scaling exponent.
  2. T11's response half — response-map pullback commutation and
     boundary-subextensive invariance.
  3. The D3 refinement-natural weight's RESPONSE side (its weight side is
     closed exactly and unconditionally).
  4. *** CONNECTED EXTENSIVITY *** — via §1.2: convergence of
     sum_n tau_R^n <B_K(A)^n>_connected / n! uniformly as cells shrink,
     with tau_R FIXED, depends entirely on the shrink rate of the connected
     cumulants, which IS R-L2b's exponent.
ONE CAMPAIGN, FOUR DISCHARGES.
- **Why it matters:** This is why R-L2b is 'the program's single target'. It also fixes the accounting on failure: 'IF R-L2b FAILS, THE REASON EXTENSIVITY IS UNRESOLVED IS R-L2b's NAMED FAILURE AND NOT A GENERAL MALAISE.'

## [MEASURE DERIVED; NATURALITY OPEN. Battery routing RULED BLOCKED (register R-15).] CONSUMER 2 — T11: local face measure DERIVED, refinement naturality NOT proved
- **Statement:** T11's measure is derived and forced (no inverse weight, no ad hoc weight, no residual shape scalar). Its TWO missing sealed objects are the sealed RESPONSE-MAP PULLBACK on common refinements and BOUNDARY-SUBEXTENSIVE INVARIANCE over C_ref. V011 flags cellulation_independence_proved = false. Separately, T11 routes BLOCKED (not CONDITIONAL) in the battery.
- **Source:** `STAGE8_T7_CODEX_BATTERY_TIER2_RETURNS_V001.md:94` (SEALED (X.md.seal.sha256))
- **Quote:** MISSING SEALED OBJECTS (obligation, named, two of them):
    the sealed RESPONSE-MAP PULLBACK on common refinements; and
    BOUNDARY-SUBEXTENSIVE INVARIANCE over C_ref.
V011 flags cellulation_independence_proved = false.
- **Why it matters:** Consumer 2's independent status: half-derived. Also: T11's naturality gap is judged (uncertified lane judgement) a PREREQUISITE of recast Q6, not a synonym for it.

## [DERIVED / CLOSED (the weight half only). The RESPONSE half is R-L2b.] CONSUMER 3 — the D3 refinement-natural weight: WEIGHT SIDE CLOSED EXACTLY AND UNCONDITIONALLY
- **Statement:** The volume weight survives slivers exactly. mu_e(S) := integral_S |det e| d^4x is a countably additive positive Borel measure absolutely continuous w.r.t. Lebesgue; reaggregation of |C|_4 is LITERALLY THE ADDITIVITY AXIOM OF A MEASURE, whose only hypotheses are measurability and a.e.-disjointness. Shape is not among them. Holds on FULL D3 — slivers, needles, star-refined atoms of unbounded facet count.
- **Source:** `STAGE8_T7_SLIVER_NATURALITY_ATTEMPT_RESULT_V001.md:116` (SEALED (X.md.seal.sha256))
- **Quote:** P-S2  THE VOLUME WEIGHT SURVIVES SLIVERS EXACTLY.            *** HIT ***
      Ground confirmed and sharpened: mu_e(S) := integral_S |det e| d^4x
      is a countably additive positive Borel measure absolutely continuous
      w.r.t. Lebesgue ... This holds on FULL
      D3 — slivers, needles, star-refined atoms of unbounded facet count —
      with no regularity hypothesis whatever.
- **Why it matters:** DO NOT RE-OPEN. The weight half is closed by measure additivity, unconditionally, on full D3. Only the RESPONSE side is open, and it is R-L2b wearing a second label. NOTE: P-S3 (the negative controls for w=1 and w=diam^4) is recorded OPEN — controls not exhibited.

## [DERIVED REDUCTION (this lane); adopted as the fourth campaign obligation] CONSUMER 4 — CONNECTED EXTENSIVITY: the reduction to R-L2b, exactly
- **Statement:** From Theorem 3's own expansion Log A_K(A) = sum_{n>=1} (-i tau_R)^n / n! <B_K(A)^n>_connected, tau_R appears raised to n multiplying a-DEPENDENT connected cumulants, so it does NOT cancel in the Z_comp(a)/Z_comp(0) ratio. Under refinement cells shrink but tau_R does not (it is sealed scale-invariant), so the entire burden of convergence falls on how fast the connected cumulants shrink with cell size — and that rate IS R-L2b's exponent.
- **Source:** `STAGE8_EXTENSIVITY_QUESTION_BLIND_ANSWER_V001.md:149` (SEALED (X.md.seal.sha256))
- **Quote:** IS A SCALE-INVARIANT PER-CELL tau_R COMPATIBLE WITH EXTENSIVE RECORD
CONTENT? *** THE QUESTION REDUCES, EXACTLY, TO R-L2b. ***
  Convergence of the series needs tau_R^n <B_K(A)^n>_connected / n! to be
  summable UNIFORMLY as cells shrink. Under refinement the cells shrink but
  TAU_R DOES NOT — it is sealed scale-invariant.
- **Why it matters:** This is the reduction that makes R-L2b carry extensivity. It also identifies where the tau_R obstruction genuinely lives (inside the a-dependent connected series), correcting P-S1, which put it in the response pullback where the ratio annihilates it.

## [RULED — verdict of record; the withdrawn hypothesis is on the record as withdrawn] EXTENSIVITY VERDICT OF RECORD — RECORDS DO COMPOSE; GAP, NOT SIGNAL
- **Statement:** Both lanes independently and blind: A_K = product_i A_Ki and Gamma_K = sum_i Gamma_Ki — EXACT DISJOINT ADDITIVITY, DERIVED AND NOT ASSUMED. CONNECTED extensivity is REQUIRED BUT NOT DERIVED, AND NOT CONTRADICTED. Therefore connected_cross_cell_terms_derived = false is a GAP, not a physical no-go signal. The principal's working hypothesis (that records do not compose the way continuum field theory assumes) was TESTED AND WITHDRAWN.
- **Source:** `STAGE8_EXTENSIVITY_VERDICT_AND_RL2B_CAMPAIGN_OPENING_V001.md:22` (SEALED (X.md.seal.sha256))
- **Quote:**   A_K = product_i A_Ki  and  Gamma_K = sum_i Gamma_Ki  — EXACT DISJOINT
  ADDITIVITY, DERIVED AND NOT ASSUMED (BID_MONOIDAL_EXTENSIVITY_DERIVATION_
  V001, 451550c3..., Theorem 1).
  CONNECTED EXTENSIVITY IS REQUIRED BUT NOT DERIVED, AND NOT CONTRADICTED
  (Theorem 3, five named conditions).
THEREFORE connected_cross_cell_terms_derived = false IS A GAP, NOT A
PHYSICAL NO-GO SIGNAL.
- **Why it matters:** DO NOT RE-OPEN 'do records compose'. Answered, twice, blind. And do NOT re-derive the illicit inference: the three-failure-mode coincidence is 'EVIDENCE OF DIFFICULTY LOCALISATION AND OF NOTHING ELSE' (§1.1).

## [CHARTERED DIVISION OF LABOUR] DIVISION OF LABOUR AS CHARTERED — who holds what
- **Statement:** This lane (construction / Einstein) holds R-L2b over the chartered diamond transport as PRIMARY WORK. The independent lane holds A-L0 arm 2 — 'the other half of the same estimate problem, and the item with no known route.'
- **Source:** `STAGE8_EXTENSIVITY_VERDICT_AND_RL2B_CAMPAIGN_OPENING_V001.md:101` (SEALED (X.md.seal.sha256))
- **Quote:** DIVISION OF LABOUR: this lane holds R-L2b over the chartered diamond
transport as PRIMARY WORK. The independent lane holds A-L0 arm 2 — the
other half of the same estimate problem, and the item with no known route.
- **Why it matters:** Sets which lane owns which item. The phrase 'other half of the same estimate problem' is loose and is CORRECTED by the D-1 determination and by the R2 determination — see the next two items.

## [RULED (register R-6, AMENDMENT_001 §B): 'Neither gates the other'] D-1 RULED: R-L2b AND A-L0 ARM 2 ARE ON DIFFERENT VARIABLES — |C|_4 versus R
- **Statement:** R-L2b controls scaling in CELL SIZE: alpha in ||C(V(a)-V(0))C||_2 <= |C|_4^alpha G_hs, a per-cell statement about how one cell's response scales as its 4-volume shrinks. A-L0 arm 2 controls decay in INTER-CELL SEPARATION: the one-line connected cross term at separation R, needing the Huygens collar (R^3 -> R^2) AND >= R^-1 after cell-time integration, giving a summable R^-2. A bound in one does not supply a bound in the other. The coupling runs ONE DIRECTION ONLY: arm 2 may CONSUME R-L2b, never the reverse. R-L2b is EARLIER in dependency order; arm 2 is the item with no known route.
- **Source:** `STAGE8_KAPPA_RULE_ADOPTION_STAGE12_ERRATUM_AND_D1_D2_D3_RETURNS_V001.md:110` (SEALED (X.md.seal.sha256))
- **Quote:**   DIFFERENT VARIABLES: |C|_4 versus R. A bound in one does not supply a
  bound in the other.
THE ONE-WAY COUPLING: arm 2's obligation U2 requires light-cone
  transversality over ALL common refinements in the RATIFIED unrestricted
  D3 quantifier. A D3-UNIFORM statement needs the per-cell constants to be
  controlled uniformly as cells shrink — which is what R-L2b supplies.
- **Why it matters:** THE SINGLE MOST RE-COMMITTED ERROR ON THIS AXIS. 'Single point of failure' was doing two jobs — earliest-unmet-prerequisite (R-L2b) and highest-probability-of-never-closing (arm 2) — and they are different items. Do not conflate them again.

## [SEALED TARGET — a requirement ('MUST SUPPLY'), not an achievement] THE ARM-2 TARGET, VERBATIM: R^2 · R^-3 · R^-1 = R^-2, BOTH FACTORS REQUIRED
- **Statement:** A-L0 arm 2 must supply BOTH (i) light-cone / Huygens collar support reducing the shell count from R^3 to R^2, AND (ii) amplitude decay of at least R^-1 after the cell-time integrations. Then the anchored sum carries R^2 · R^-3 · R^-1 = R^-2, summable. Neither factor alone suffices: (i) without (ii) leaves R^-1, divergent; (ii) without (i) leaves R^-1, divergent. Certifying one and asserting the bound BLOCKS with witness A_L0_HUYGENS_BOUND_ONE_FACTOR_ONLY.
- **Source:** `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:533` (SEALED (X.md.seal.sha256))
- **Quote:** The free/Dyson propagation bridge must supply BOTH:
      (i)  LIGHT-CONE / HUYGENS COLLAR SUPPORT, reducing the shell count from
           R^3 to R^2; AND
      (ii) AMPLITUDE DECAY of at least R^-1 after the cell-time integrations.
Then the anchored sum carries R^2 · R^-3 · R^-1 = R^-2, which is summable.
- **Why it matters:** The other lane's target, stated so this lane does not misremember it. Note the arithmetic block is labelled 'EXACT ARITHMETIC OF THE TARGET' — it transforms an ASSUMED exponent into a convergent number.

## [BOUND_CLASS_NOT_OBJECT_THEOREM. NOT DETERMINED BY THE SEALED STRUCTURE.] ARM 2's INDEPENDENT STATUS: BOTH FACTORS BOUND-CLASS, NEITHER AN OBJECT THEOREM; U1/U2/U3 UNCERTIFIED
- **Statement:** Both factors of the arm-2 target carry as CONTINUUM BOUND-CLASS statements and NEITHER YET as an object theorem uniformly over D3. Three uncertified components: U1 uniform control of time-profile W^{1,1}/BV norms; U2 light-cone transversality over ALL common A/B refinements in D3 (the unrestricted quantifier — the harder statement); U3 the finite-Q PROJECTION-TAIL issue. A separate determination counts the whole corpus's quantitative content on R^-1 at TWO LINES, with ZERO ACHIEVEMENT CLAIMS.
- **Source:** `STAGE8_T7_ARM2_SHARPENING_AND_PROJECTION_TAIL_BINDING_V001.md:17` (SEALED (X.md.seal.sha256))
- **Quote:** Both factors of the arm-2 target now carry as CONTINUUM BOUND-CLASS
statements — and NEITHER YET as an object theorem uniformly over D3.
- **Why it matters:** Arm 2 is not 'nearly done'. And scripts/verify_v002.py DOES NOT EXIST — the collar sums were never computed; the corpus had already sealed this as finding H-3 and FORBIDS citing the file.

## [DETERMINED (lane determination, sealed). 'R2 DOES NOT REACH R-L2b. NOT PARTIALLY, NOT WEAKLY, NOT VIA ARM 2.'] R2 (EXACT-MONOIDALITY ISOLATION) DOES NOT REACH R-L2b — hardened
- **Statement:** R2 closes at most a pinned-skeleton, order-restricted slice of A-L0 arm 2. It leaves open (i) the D3 quantifier, (ii) ALL OF R-L2b — R2 does not touch the separation variable R, and its |C|_4 side CONSUMES R-L2b's underived alpha rather than supplying it — and (iii) n >= 3 absent R1. Flag r2_reaches_RL2b = false, HARDENED by the erratum.
- **Source:** `STAGE8_R2_WELL_POSEDNESS_AND_INPUT_SEAL_DETERMINATION_V001.md:227` (SEALED (X.md.seal.sha256))
- **Quote:** R2 LEAVES OPEN: (i)  the D3 quantifier — the whole of what F-2 says no lane may pin;
                (ii) ALL OF R-L2b. R2 does not touch the separation variable R, and its
                     |C|_4 side CONSUMES R-L2b's underived alpha rather than supplying it.
                (iii) n >= 3, absent R1.
- **Why it matters:** DEAD ROUTE INTO R-L2b. Do not re-propose R2 as a way past R-L2b. Note also r2_tractable_form_available = false: the n=2 reduction required R1, and R1 is NOT CHARTERED.

## [ADOPTED AND IN FORCE (register R-10). Three accepted obligations O-D1, O-D2, O-D3; a fourth O-D4 flagged and NOT accepted.] THE CHARTER IN FORCE — Option 4, disjoint causal-diamond decomposition
- **Statement:** ADOPTED by the principal: each admitted atom C of the frozen D3 class is covered by a family of DISJOINT CAUSAL DIAMONDS, each an affine dilate/translate of the sealed Phase-A unit diamond (0<t<1, |x|<min(t,1-t), r(t)=min(t,1-t), M(t)=Q 1_{|x|<=r(t)} Q, v(t)=tau_R*32 r(t)^3, b_D=exp(16-1/s)); each diamond is an exhaustion unit at FULL tau_R; the response weight is sum_i |D_i|_4, required to equal |C|_4 exactly; tau_R REMAINS DIMENSIONLESS. Rejected: inscribed diamond, circumscribed diamond, atom indicator M_C = Q 1_C Q.
- **Source:** `STAGE8_TRANSPORT_FUNCTOR_CHARTER_V001.md:41` (SEALED (X.md.seal.sha256))
- **Quote:** THE TRANSPORT FUNCTOR. For an admitted atom C of the frozen D3 class:
  1. C is covered by a family of DISJOINT CAUSAL DIAMONDS
     {D_1, ..., D_N(C)}, each an affine dilate/translate of the Phase-A
     unit diamond
- **Why it matters:** DO NOT RE-PROPOSE the three rejected options; their rejection reasons are recorded and citable. And DO NOT read tau_R as a physical duration — that is a standing DEFECT under this charter, because it would discharge a named Part-C blocker (absolute physical T_R) by fiat.

## [SEALED SELF-DISCLAIMER, INDEPENDENTLY CONFIRMED. moves_R_L2b = NOT ONE STEP.] THE CHARTER DOES NOT UNBLOCK R-L2b — the charter says so itself, and four independent grounds confirm
- **Statement:** 'IT DOES NOT UNBLOCK R-L2b. The exponent is still underived. The charter fixes WHAT R-L2b MAY BE STATED OVER ... and supplies NO ESTIMATE.' Independently confirmed on four grounds, the decisive one being that role 3 (the pair-separation lower cutoff) is not even a variable of G_hs, which is a SINGLE-CELL quantity with no R-integral in it.
- **Source:** `STAGE8_TRANSPORT_ROLE_GRID_SECOND_DIMENSION_V001.md:141` (SEALED (X.md.seal.sha256))
- **Quote:**  B1  *** ROLE 3 CANNOT TOUCH alpha EVEN IN PRINCIPLE — IT IS NOT IN THE OBJECT. *** G_hs(C,eps) :=
     |C|_4^{-alpha} ||C(V(a)-V(0))C||_2 is a SINGLE-CELL quantity in §R.3. Role 3 is the lower
     cutoff of a PAIR-SEPARATION integral at n >= 2. THERE IS NO R-INTEGRAL IN G_hs.
- **Why it matters:** STANDING PRIOR, recorded in the corpus: 'THIS IS THE THIRD TIME AN ANALYSIS OF THE TRANSPORT/CHARTER AXIS HAS PRODUCED A RESULT THAT READS LIKE PROGRESS TOWARD ALPHA. IT IS NOT.' A fourth was then logged (REMAINING_CONTENT §7). Charter-axis work is not R-L2b work.

## [RESTATEMENT OF RECORD (append-only successor). E1 v002 itself is UNAMENDED — S2 and R-L2b still read |C|_4 there.] R-L2b RESTATED OVER THE CHARTER — the current form of the obligation
- **Statement:** CERTIFY || C (V_{mu lambda}(a) - V_{mu lambda}(0)) C ||_2 <= |D|_4^alpha * G_hs, where D ranges over the DIAMONDS of the chartered decomposition, not over atoms of D3; |D|_4 is the sealed tetrad/Jacobian 4-volume of that diamond; alpha is DERIVED, not assumed 1/2; and G_hs is finite UNIFORMLY over every admissible decomposition of every atom of the unrestricted D3 class, and CARRIER-BLIND. Companion beta for G_cm derived with alpha.
- **Source:** `STAGE8_RL2B_OVER_CHARTER_AND_BLIND_ROUTE_FINDING_V001.md:21` (SEALED (X.md.seal.sha256))
- **Quote:**   CERTIFY:  || C (V_(mu lambda)(a) - V_(mu lambda)(0)) C ||_2
              <=  |D|_4^alpha * G_hs
  WHERE     D ranges over the DIAMONDS of the chartered decomposition, not
            over atoms of D3;
            ... G_hs is finite UNIFORMLY over every admissible decomposition of
            every atom of the unrestricted D3 class, and CARRIER-BLIND.
- **Why it matters:** Note the NESTED, DISTINCT quantifiers: decomposition axis inside, atom/cellulation axis outside. The corpus does not conflate them (OD3_LEVER:90-92). Note also flag E1_v002_unamended = true — the chartered reading lives ONLY in append-only successors.

## [OBSERVATION OF RECORD, expressly NOT decisive ('That observation does not decide the question'). Source is a relayed independent-lane point, re-recorded by this lane.] THE SLIVER DIRECTION — what it is, and why the isotropic covariance cannot reach it
- **Statement:** A sliver is a cell whose 4-volume goes to 0 while its DIAMETER stays O(1). The sealed construction possesses exactly ONE scaling covariance, the isotropic orbit (4-volume -> lambda^4 with diameter -> lambda*diam). A SLIVER IS TRANSVERSE TO THAT ORBIT, so no one-parameter isotropic covariance can supply a weight in the sliver direction. Hence R-L2b must be derived transversally and not merely on the orbit.
- **Source:** `STAGE8_T7_SLIVER_NATURALITY_ATTEMPT_RESULT_V001.md:102` (SEALED (X.md.seal.sha256))
- **Quote:** The sliver direction matters and one lane made the point sharply: the
sealed construction possesses exactly ONE scaling covariance, the
isotropic orbit of BID_ABSOLUTE_RECORD_SCALE_IDENTIFIABILITY_GATE_V001
(4-volume -> lambda^4 with diameter -> lambda*diam). A SLIVER IS
TRANSVERSE TO THAT ORBIT — diameter stays O(1) while 4-volume -> 0 — so
no one-parameter isotropic covariance can supply a weight in the sliver
direction.
- **Why it matters:** This is the sharpest statement of WHY the sliver is the failing direction. It is an observation about available covariance, not a proof that the bound fails.

## [NAMED, SCOPED OBLIGATION. Verdict of the artifact itself: sliver_naturality_verdict = UNDETERMINED_ON_SEALED_INPUTS.] THE SLIVER ARTIFACT'S NAMED MISSING OBJECT (its central deliverable)
- **Statement:** The pre-charter sliver artifact names the missing sealed object as: R-L2b — the HS scaling exponent of Delta = C(V(a)-V(0))C in |C|_4, DERIVED rather than assumed, AND VALID IN THE SLIVER DIRECTION (4-volume -> 0 at diameter O(1)), NOT ONLY ALONG THE ISOTROPIC SCALE ORBIT. Flag: missing_sealed_object = R_L2b_HS_scaling_exponent_derived_in_the_sliver_direction.
- **Source:** `STAGE8_T7_SLIVER_NATURALITY_ATTEMPT_RESULT_V001.md:97` (SEALED (X.md.seal.sha256))
- **Quote:** THE PRECISELY NAMED MISSING SEALED OBJECT, which is the useful output:
    R-L2b — THE HS SCALING EXPONENT OF Delta = C(V(a)-V(0))C IN |C|_4,
    DERIVED RATHER THAN ASSUMED, AND VALID IN THE SLIVER DIRECTION
    (4-volume -> 0 at diameter O(1)), NOT ONLY ALONG THE ISOTROPIC SCALE
    ORBIT.
- **Why it matters:** This is the text the supersession dispute is ABOUT. Its other results — P-S1 ground REFUTED, P-S2 HIT, recast_Q6_shown_ill_posed = false, D3 NOT narrowed — are untouched by any charter and stand.

## [ADJUDICATED: OBJECT SUPERSEDED (R-L2b-over-atoms -> R-L2b-over-diamonds). SUBSTANCE NOT SUPERSEDED (the sliver difficulty is relocated to leg (ii) aggregation and to the surviving D3 quantifier in leg (i), and is unanswered).] *** ADJUDICATION OF THE CONTESTED SUPERSESSION: SUPERSEDED IN OBJECT, NOT IN SUBSTANCE ***
- **Statement:** The corpus's ONLY supersession adjudication is a single clause in REMAINING_CONTENT §7, on timestamps: the sliver artifact is PRE-CHARTER (verified: 2026-07-26 13:42:41 vs charter 15:32:20) and states R-L2b over ATOMS, the formulation the charter replaced. There is NO separate supersession artifact and no other text supersedes it. BUT the same artifact records, verbatim, that the anisotropy is RELOCATED, NOT REMOVED, that the sliver failure is 'RE-LOCALISED from (i) to (ii)' rather than answered, and that a D3 uniformity quantifier reaching unbounded aspect ratio SURVIVES into leg (i). A search for any artifact saying the anisotropy is removed, dropped, or beside the point returned ZERO HITS.
- **Source:** `STAGE8_RL2B_REMAINING_CONTENT_UNDER_THE_CHARTER_V001.md:149` (SEALED (X.md.seal.sha256); timestamps independently re-verified by this sweep)
- **Quote:** ADJUDICATED SUPERSEDED IN OBJECT on timestamps — it is PRE-CHARTER (07-26 13:42; charter 15:32)
and states R-L2b over ATOMS, the formulation the charter replaced. So the relocation finding stands.
BUT AN INVESTIGATION DELIVERING A COSTLY CORRECTION ON THE SLIVER QUESTION THAT NEVER OPENED THE
CORPUS'S SHARPEST SLIVER ARTIFACT HAS COMMITTED THE OMISSION IT CHARGES TO THE SWEEP. Recorded.
- **Why it matters:** THIS IS THE CONTESTED ITEM. Both halves must travel together or the record misleads. Citing 'superseded' alone would license the false inference that the sliver problem is gone. It is not — it has moved.

## [DERIVED CONSEQUENCE OF THE CHARTER (structural, not an estimate)] THE RELOCATION TEXT ITSELF — 'THE ANISOTROPY IS RELOCATED, NOT REMOVED'
- **Statement:** Under the charter each diamond is ISOTROPIC, so on a single diamond the isotropic scale orbit applies and the one-parameter covariance is available; the anisotropy of the atom now lives in the COMBINATORICS of the decomposition. R-L2b over the charter is no longer 'an anisotropic Schatten-2 estimate': it is (i) the ISOTROPIC per-diamond estimate plus (ii) a SUMMATION over the decomposition, where the aspect-ratio dependence sits. The independent lane's report that the bound class fails in the sliver direction is NOT answered by the charter; it is RE-LOCALISED from (i) to (ii).
- **Source:** `STAGE8_RL2B_OVER_CHARTER_AND_BLIND_ROUTE_FINDING_V001.md:36` (SEALED (X.md.seal.sha256))
- **Quote:**   2. THE ANISOTROPY IS RELOCATED, NOT REMOVED. Each diamond is ISOTROPIC, so
     ON A SINGLE DIAMOND the isotropic scale orbit applies and the
     one-parameter covariance is available. The anisotropy of the atom now
     lives in the COMBINATORICS of the decomposition
- **Why it matters:** The exact text that both halves of the supersession question rest on. Also records the branch structure: 'If the failure is genuinely in the per-diamond isotropic estimate, the charter does not help.'

## [DERIVED ARITHMETIC (aggregation only). The artifact's own caveat: 'They do not say what alpha is.'] THE SLIVER FAILURE IS WHAT alpha < 1 LOOKS LIKE UNDER AGGREGATION — with a predicted rate
- **Statement:** With N diamonds of 4-volume V/N each, sum_i |D_i|_4^alpha = N^(1-alpha) V^alpha. D5 requires (V/N)^(alpha-1) bounded as N -> infinity at fixed V, which holds iff alpha >= 1. A sliver of aspect ratio A needs N ~ A^3 diamonds, so the aggregate grows as A^(3(1-alpha)): alpha=1/2 -> A^1.50; alpha=3/4 -> A^0.75; alpha=1 -> A^0. So the reported sliver failure is not a separate fact — it is what alpha<1 looks like under aggregation, at a PREDICTED rate.
- **Source:** `STAGE8_RL2B_FRAME_ANSWER_AND_CAMPAIGN_TARGET_V001.md:58` (SEALED (X.md.seal.sha256))
- **Quote:** *** SO THE INDEPENDENT LANE'S REPORTED SLIVER FAILURE OF THE BOUND CLASS IS
NOT A SEPARATE FACT. IT IS WHAT alpha < 1 LOOKS LIKE UNDER AGGREGATION, AND
ITS RATE IS PREDICTED: A^(3(1-alpha)). ***
- **Why it matters:** Converts a vague uniformity demand into the single inequality alpha >= 1. But the diagonal attack later RE-TYPED this and the alpha>=1 <=> full-cancellation equivalence as claims about the CONTINUUM LIMIT, not about the sealed (Galerkin) object.

## [DEAD ROUTE — refuted by this lane one turn after proposing it. Do not re-propose.] MECHANISM 1 — COMMUTATOR ALGEBRA. REFUTED, on two independent grounds.
- **Statement:** GROUND 1 (quantitative): finiteness needs the difference kernel to vanish like |r|^p with p > 3/2; a single commutator's Lipschitz gain gives p = 1, which diverges. GROUND 2 (structural, decisive): C is a projection, so C[C,Y]C = 0 IDENTICALLY — commutator structure controls the OFF-DIAGONAL blocks C X (1-C), while the object R-L2b bounds, C X C, is the DIAGONAL block. Exhibiting the object 'in commutator form' would make it VANISH, not make it finite.
- **Source:** `STAGE8_RL2B_COMMUTATOR_ROUTE_REFUTED_AND_TARGET_SHARPENED_V001.md:63` (SEALED (X.md.seal.sha256))
- **Quote:** C is a projection, C^2 = C. So for ANY Y,
    C [C, Y] C  =  C (CY - YC) C  =  C Y C  -  C Y C  =  0   IDENTICALLY.
*** THEREFORE COMMUTATOR STRUCTURE CONTROLS THE OFF-DIAGONAL BLOCKS
C X (1-C), WHILE THE OBJECT R-L2b BOUNDS — C X C — IS THE DIAGONAL BLOCK.
- **Why it matters:** Also records an INVITATION DEFECT: the corpus's worked identity ||[C,P]||_2^2 = 2 sum_i sigma_i(1-sigma_i) is FINITE-RANK ONLY and establishes nothing about continuum commutators with C, where the analogous statement FAILS at degree -3.

## [DEAD ROUTE — 'The ideal bound is TRUE AND USELESS. ... Recorded so the rescue is not attempted again.'] MECHANISM 2 — THE HS IDEAL BOUND. TRUE AND VACUOUS.
- **Statement:** Since C is a projection, ||C||_op = 1 and HS is an ideal, so ||C X C||_2 <= ||X||_2. But at first order X = V(a)-V(0) = -i a int dt U_0^* J U_0 with J = -Q b_D(t,x) Q tensor alpha_x a bounded multiplication-type operator whose kernel is a delta times a bump, so ||J||_2 = INFINITY and ||X||_2 = INFINITY. Finiteness must come from how the two C's act, not from X alone.
- **Source:** `STAGE8_RL2B_COMMUTATOR_ROUTE_REFUTED_AND_TARGET_SHARPENED_V001.md:80` (SEALED (X.md.seal.sha256))
- **Quote:** whose kernel is a delta times a bump — so ||J||_2 = INFINITY and hence
||X||_2 = INFINITY. The ideal bound is TRUE AND USELESS. Finiteness must come
from how the two C's act, not from X alone. Recorded so the rescue is not
attempted again.
- **Why it matters:** The most obvious rescue. Explicitly fenced so it is not re-attempted.

## [DERIVED FOR THE CONTINUUM; RE-TYPED (not withdrawn) as a limit statement, NOT a statement about the sealed Galerkin object. Flag HS_volume_supplies_R_minus_1 = DEAD.] MECHANISM 3 — HS VOLUME SCALING. DEAD (and later self-corrected as a continuum statement).
- **Statement:** || 1_D C 1_D ||_2 = INFINITY on every diamond at every scale (~eps^-3 divergence, computed at four cutoffs); a Calderon-Zygmund kernel of degree -3 in 3D is L^2-bounded but NOT Hilbert-Schmidt. Hence R-L2b's finiteness is not a property of the support volume — it is purchased entirely by cancellation in the difference, so alpha is set by the CANCELLATION RATE, not by |D|_4. Also closes 'any hope that HS volume scaling secretly supplies the missing R^-1. It does not.'
- **Source:** `STAGE8_EXTENSIVITY_VERDICT_AND_RL2B_CAMPAIGN_OPENING_V001.md:168` (SEALED (X.md.seal.sha256))
- **Quote:**     *** THEREFORE || 1_D C 1_D ||_2 = INFINITY, ON EVERY DIAMOND, AT EVERY
    SCALE. This is consistent with and explained by the sealed degree -3
    homogeneity: a Calderon-Zygmund kernel of degree -3 in three dimensions
    is L^2-BOUNDED BUT NOT HILBERT-SCHMIDT. ***
- **Why it matters:** This mechanism is ALSO the one whose closure artifact carries explains_sliver_direction_failure = true — so it is a CELL-SCALE mechanism, not a coincidence-axis one. A reviewer claim that 'all five argue about p on the coincidence axis' was refuted on exactly this ground.

## [NOT A CLOSURE. time_integration_has_a_closure_artifact = false. Route is PARTLY SPENT, PARTLY MODAL, AXIS-BLOCKED, and gated before it starts.] MECHANISM 4 — TIME INTEGRATION. HAS NO CLOSURE ARTIFACT; partly spent, modal, axis-blocked.
- **Statement:** Time integration was named in COMM (17:08) as 'the candidate this lane would attack next' and listed as CLOSED in WARD (17:32); no artifact exists in that 24-minute window (verified by find over the whole tree, all filetypes). It is the corpus's DESIGNATED SOLE REMAINING SUMMABILITY SOURCE, with two sealed statements on two axes (separation: arm-2 factor (ii); coincidence: C6, locus the volume diagonal), BOTH MODAL AND CARRYING NO EXPONENT. And its CELL-SCALE role is ALREADY SPENT — booked as exactly one power of L in M·L·L^3 = M·|D|_4.
- **Source:** `STAGE8_TWO_UNTRIED_MECHANISMS_ATTACK_RESULT_V001.md:63` (SEALED (X.md.seal.sha256))
- **Quote:** *** AND THE DECISIVE FINDING: THE CELL-SCALE ROLE OF THE SAME int dt IS ALREADY SPENT. ***
FRAME_ANSWER:70-72 books the time integration as EXACTLY ONE POWER OF L, in M · L · L^3 = M · |D|_4
— and does so by reusing A-L4's strength mechanism OUTSIDE ITS SEALED SCOPE, self-labelled a
non-derivation. THERE IS NO SECOND alpha TO EXTRACT FROM IT.
- **Why it matters:** Do not restart this as a 'virgin' candidate. And do NOT cite C6's 'supplies the missing decay' for a quantity: all four such sentences are 'RESTRICTIVE RELATIVE CLAUSES INSIDE MODAL CLAIMS ... NONE CARRIES AN EXPONENT.'

## [NOT A MECHANISM. Q_support_structure_has_a_closure_artifact = false; it collapses into the blocker itself.] MECHANISM 5 — Q SUPPORT STRUCTURE. DEGENERATE: IT IS U3 WEARING A DIFFERENT NAME.
- **Statement:** At finite carrier, Q_(n,ell) is finite-rank so X is finite-rank with a finite-sum-of-products kernel and NO SINGULARITY ANYWHERE — there is nothing for Q's support to supply additional vanishing against. In the limit Q -> I and Q's support structure is gone. So the candidate exists only at intermediate carrier, which IS U3. Sealed inputs on Q's support: ZERO, both directions, both axes; '[Q, 1_{|x|<=r(t)}]' does not exist anywhere in the corpus under any pattern run.
- **Source:** `STAGE8_TWO_UNTRIED_MECHANISMS_ATTACK_RESULT_V001.md:96` (SEALED (X.md.seal.sha256))
- **Quote:** IN THE LIMIT: Q -> I and Q's support structure is gone.
=> THE CANDIDATE EXISTS ONLY AT INTERMEDIATE CARRIER — WHICH IS EXACTLY U3, THE ALREADY-NAMED LIVE
BLOCKER, WEARING A DIFFERENT NAME. It was never a separate mechanism.
- **Why it matters:** Q is not even a determinate object: the sealed spec's required family ([Q_n,h_0]=0, Q_n -> I) 'does not exist for the free massless Dirac multiplier', and the replacement's conditions (3),(4),(5) are NOT DISCHARGED.

## [CLOSED BY PHYSICS. p_supplied_by_the_identity = 0; threshold p > 3/2.] MECHANISM 6 — THE WARD / POINTER-WEIGHT IDENTITY. CLOSED, two independent reasons.
- **Statement:** Reason 1: wrong grading — C4 gives two orders in the RECORD-INSERTION grading, not the coincidence grading; in the coincidence grading it supplies p = 0. Reason 2: exactly saturated at full tau_R (sum w·phase = sum |w| = 1, exact in Q(sqrt2)). Supplying such an identity would be a NEW PRINCIPLE, because the corpus's sole candidate has been MEASURED and REFUTED. The obvious escape (small record coupling) is FORECLOSED by sealed D2.
- **Source:** `STAGE8_WARD_IDENTITY_QUESTION_BLIND_ANSWER_V001.md:138` (SEALED (X.md.seal.sha256))
- **Quote:** BEING QUANTITATIVE AS ASKED: the threshold is p > 3/2. The identity supplies
0. The five closed mechanisms supply at most 1. THE SHORTFALL IS NOT
CLOSED AND IS NOT NARROWED BY THIS ANSWER.
- **Why it matters:** The 'at most 1' numeral is a CEILING OVER A SET, and it traces to exactly ONE member. It is not a statement that the object's p is 1. Object-vs-bound: 'The difference kernel's actual p REMAINS UNKNOWN.'

## [DETERMINED: STRUCTURAL. R-L2b's Ward route is closed by physics, not by exhausted search.] MECHANISM 7 — IS C4's SATURATION SOFT? NO: IT IS STRUCTURAL.
- **Statement:** The closure/orthogonality record criterion and the saturation condition are THE SAME EQUATION, not two equations with a shared root: three phases e^{-i lambda tau} with lambda in {-sqrt2, 0, +sqrt2} are mutually orthogonal exactly at sqrt2 tau = pi, which is what defines tau_R. Verified closed form S(tau) = sin^2(sqrt2 tau/2), first max at pi/sqrt2. An independent ground (scale-protection) holds even for a reader who rejects the identification.
- **Source:** `STAGE8_C4_SATURATION_STRUCTURAL_BLIND_ANSWER_V001.md:172` (SEALED (X.md.seal.sha256))
- **Quote:** *** C4's SATURATION IS STRUCTURAL. R-L2b's WARD ROUTE IS CLOSED BY PHYSICS,
NOT BY EXHAUSTED SEARCH. ***
- **Why it matters:** 'the day's arc closed on itself. The transport charter was chosen because the sealed construction lives on causal diamonds; the saturation that blocks R-L2b is fixed by the same derivation that fixes those diamonds. The obstruction and the frame have one root.'

## [LEDGER STATE OF RECORD. seven_closed_mechanisms_with_primary_sources = 5.] THE HONEST COUNT OF THE MECHANISM LEDGER — 7 entries, 5 sourced, 0 suppliers
- **Statement:** Seven classes; five carry analysis and ALL FIVE ARE NEGATIVES, not suppliers; of the remaining two, one is partly spent and axis-blocked, one is degenerate and is the blocker itself. 'SO THE SEARCH IS NOT FIVE CLOSED AND TWO OPEN. IT IS SEVEN ITEMS OF WHICH NONE SUPPLIES ANYTHING TOWARD alpha, AND TWO WERE NEVER ROUTES.' AND: 'DO NOT READ THIS AS THE SEARCH IS EXHAUSTED.' search_exhausted = FALSE.
- **Source:** `STAGE8_TWO_UNTRIED_MECHANISMS_ATTACK_RESULT_V001.md:144` (SEALED (X.md.seal.sha256))
- **Quote:** SO THE SEARCH IS NOT "FIVE CLOSED AND TWO OPEN". IT IS SEVEN ITEMS OF WHICH NONE SUPPLIES ANYTHING
TOWARD alpha, AND TWO WERE NEVER ROUTES.
DO NOT READ THIS AS "THE SEARCH IS EXHAUSTED". It is not a proof that no mechanism exists
- **Why it matters:** NEW HAZARD, RECORDED: '"FIVE" NOW DENOTES TWO DIFFERENT SETS.' WARD's five INCLUDES time integration and Q support; the later 'five sourced mechanisms' EXCLUDES them and includes the Ward identity and C4-saturation. Any future citation of 'the five' is ambiguous.

## [POWER COUNTING, NOT A DERIVATION. A_L4_mechanism_reused_outside_sealed_scope = true (DISCLOSED). Does not discharge R-L2b.] §4 OF THE FRAME ANSWER IS POWER COUNTING, NOT A DERIVATION — self-labelled
- **Statement:** The alpha = 1 <=> full-cancellation equivalence is obtained by power counting: bounded difference kernel M gives ||X||_2 <= M*|D|_3, the a-insertion carries one further power of temporal extent L via A-L4's strength mechanism, so for an isotropic diamond ||C(V(a)-V(0))C||_2 <~ M*L*L^3 = M*|D|_4. The step reuses A-L4 OUTSIDE ITS SEALED SCOPE (A-L4 is sealed only for the two-line sector on family A), and the artifact labels itself accordingly.
- **Source:** `STAGE8_RL2B_FRAME_ANSWER_AND_CAMPAIGN_TARGET_V001.md:82` (SEALED (X.md.seal.sha256))
- **Quote:** DISCLOSURE, REQUIRED: the time-integral step reuses A-L4's strength
mechanism, and A-L4 is sealed ONLY for the two-line sector on family A. The
reuse is more defensible here than on a general atom, because UNDER THE
CHARTER EVERY DIAMOND IS ISOTROPIC ... IT IS STILL A REUSE OUTSIDE ITS SEALED SCOPE and
is labelled as such: §4 is POWER COUNTING, NOT A DERIVATION, and it does not
discharge R-L2b.
- **Why it matters:** THE label-vs-proof-category discipline in action. Anyone citing 'alpha = 1 iff full cancellation' must carry this label with it.

## [DERIVED. framing_refuted = true. p_is_a_property_of_the_sealed_object = false.] THE DIAGONAL ATTACK — FRAMING REFUTED: the sealed object is FINITE-RANK, with no coincidence singularity
- **Statement:** Q_(n,ell) is a finite-rank Hermite-Galerkin projector (sealed). J = Q(...)Q is finite-rank; every Dyson term for V(a)-V(0) contains at least one J, so V(a)-V(0) is finite-rank at every order in a; rank(CXC) <= rank(X); so X = C(V(a)-V(0))C is finite-rank, trace-class, HILBERT-SCHMIDT, with a finite-sum-of-products kernel and NO SINGULARITY ANYWHERE. Therefore p is NOT a property of the sealed object, and the coincidence-cancellation theorem as posed has nothing to act on.
- **Source:** `STAGE8_RL2B_DIAGONAL_ATTACK_RESULT_V001.md:46` (SEALED (X.md.seal.sha256))
- **Quote:** *** THEREFORE p IS NOT A PROPERTY OF THE SEALED OBJECT. AT FINITE (n,ell)
THE OBJECT IS SMOOTH AND ||X||_2 < infinity TRIVIALLY. THE DIAGONAL
COINCIDENCE-CANCELLATION THEOREM HAS NOTHING TO ACT ON. ***
- **Why it matters:** THE PIVOT OF THE WHOLE CAMPAIGN. It carries a MAJOR SELF-CORRECTION: the divergence computation, and several artifacts built on it, applied a CONTINUUM computation to a GALERKIN object — the SEVENTH instance of match-by-name/fail-by-type, and the largest in propagation. The affected claims are RE-TYPED, not withdrawn: they describe the n -> infinity limit.

## [DERIVED AND EXACT. leading_symbol_survives_the_sandwich = true (DERIVED, not merely unproven). Survives all subsequent corrections.] THE ONE NEW DERIVED LEMMA OF THE CAMPAIGN: P alpha_x P = -nhat_x P
- **Statement:** For P = (1 - alpha.nhat)/2 the negative-energy projector for direction nhat, and every spatial index x: P alpha_x P = -nhat_x P. Proved from {alpha_i,alpha_j} = 2 delta_ij and (alpha.nhat)^2 = 1; verified numerically to 1.1e-16 over 200 random directions in the Dirac representation, Clifford relations checked first. Consequence: C(p) alpha_x C(p) = -phat_x C(p) — the sandwich reduces the matrix insertion to a scalar times the projector, and the result is STILL DEGREE 0 in p, hence a degree -3 kernel in r, hence NO VANISHING AT COINCIDENCE.
- **Source:** `STAGE8_RL2B_DIAGONAL_ATTACK_RESULT_V001.md:88` (SEALED (X.md.seal.sha256))
- **Quote:**   Let P = (1 - alpha.nhat)/2 be the negative-energy projector for direction
  nhat. Then for every spatial index x:
        *** P alpha_x P  =  - nhat_x P . ***
- **Why it matters:** The campaign's only positive derived mathematics. It converts 'no identified mechanism supplies p > 3/2' into 'the leading term is derivably nonzero IN THE LIMIT' — a stronger negative. Note the 'alpha' here is the DIRAC MATRIX.

## [CONDITIONAL REFUTATION. RL2b_uniform_bound_refuted = CONDITIONAL_ON_H1. RL2b_declared_dead = false.] THE CONDITIONAL REFUTATION — and it is conditional on ONE named hypothesis
- **Statement:** HS balls are weakly closed, so if the limit X is not Hilbert-Schmidt then ||X_n||_2 -> infinity and no uniform bound can exist. Combined with the surviving leading symbol: ||X_(n,ell)||_2 -> infinity as the Galerkin carrier exhausts the continuum, and R-L2b's uniform bound cannot hold — CONDITIONAL ON EXACTLY ONE HYPOTHESIS: that the Galerkin scheme CONVERGES in the sense the weak-closedness argument needs. THIS LANE HAS NOT ESTABLISHED IT.
- **Source:** `STAGE8_RL2B_DIAGONAL_ATTACK_RESULT_V001.md:124` (SEALED (X.md.seal.sha256))
- **Quote:** SO THE RESULT IS: R-L2b's uniform bound FAILS IF the Galerkin exhaustion
converges to the continuum object; and HOLDS TRIVIALLY, at every finite
(n,ell), if it does not.
- **Why it matters:** R-L2b IS NOT REFUTED. The ratification artifact insists on this precision: '"Refutation" overstates that ... what is decoupled is a body of NEGATIVE RESULTS AND A CONDITIONAL REFUTATION, not a completed one.'

## [PROOF OF IMPOSSIBILITY, not a gap. The label PARENT_STATE_REGULATOR_RESTRICTION_DERIVED was WITHDRAWN.] THE SEALED GALERKIN IMPOSSIBILITY — the required family DOES NOT EXIST
- **Statement:** The sealed specification required a nonzero nested finite-rank family Q_n with [Q_n,h_0]=0 and Q_n -> I strongly. That family does not exist for the free massless Dirac multiplier: a nonzero finite-dimensional reducing subspace would contain an L2 eigenvector of h_0, while h_0 has purely continuous spectrum. Flag genuine_finite_rank_continuum_restriction_constructed = false. 'Exact commutation with h_0 is neither required nor possible.'
- **Source:** `STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001.md:24` (HASH-PINNED, NOT SEAL-FILE-SEALED. No X.seal.sha256, no X.md.seal.sha256, and no membership in any *.sha256 manifest; but its current sha256 a1258dcf40732f0e… is pinned in STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md:26 and in five scripts, and MATCHES current bytes.)
- **Quote:** That family does not exist for the free massless Dirac multiplier. A
nonzero finite-dimensional reducing subspace would contain an `L2`
eigenvector of `h_0`, while `h_0` has purely continuous spectrum.
- **Why it matters:** Cited as 'SEALED' by the trilemma (§2 heading). It is HASH-PINNED, which is a different and weaker status. The finding stands; the label should be corrected when cited.

## [SEALED REQUIREMENT LIST, 3 of 5 NOT DISCHARGED. requirement_list_items_discharged = 2 of 5.] THE REPLACEMENT GALERKIN REQUIREMENT LIST — 2 of 5 discharged, and item (5) is what the refutation needs
- **Statement:** A genuine Galerkin family must satisfy: (1) finite rank and nested; (2) Q_n -> I strongly; (3) Q_n h_0 Q_n converges to h_0 on a common core; (4) Q_n M_c(t) Q_n converges strongly to M_c(t); (5) the finite propagators converge strongly, uniformly on compact times. Status: (1) and (2) STANDARD; (3), (4), (5) NOT DISCHARGED. Item (5) is exactly what the conditional refutation needs. What (5) actually needs is Trotter-Kato, and 'it is not proved anywhere in this corpus.'
- **Source:** `STAGE8_RL2B_CONVERGENCE_HYPOTHESIS_RESOLUTION_AND_F5_TRILEMMA_V001.md:83` (SEALED (X.md.seal.sha256))
- **Quote:** (1) finite rank and nested          STANDARD, holds for Hermite projectors
(2) Q_n -> I strongly               STANDARD (Hermite basis is complete)
(3) Q_n h_0 Q_n -> h_0 on a core    NOT DISCHARGED
(4) Q_n M_c Q_n -> M_c strongly     NOT DISCHARGED
(5) finite propagators converge     NOT DISCHARGED  <-- what my argument needs
- **Why it matters:** The corpus WROTE THE HYPOTHESIS DOWN BEFORE THE CAMPAIGN DID, as a requirement on future work. Do not re-invent it. CAUTION: STAGE8_T7_PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_RESULT_V001:45 carries pure_state_sequence_nested = false — a different object (C_n^pure, not Q_n), but a reason to check item (1) rather than assume it.

## [DERIVED NEGATIVE. smooth_to_sharp_theorem_covers_galerkin_truncation = false.] THE SMOOTH-TO-SHARP THEOREM DOES NOT DISCHARGE ITEM (5) — DERIVED, and the reason is that V is not compact
- **Statement:** FINITE_PARENT_ANALYTIC_AUTHORITY_V001's stability theorem concludes 'Thus the propagators converge in operator norm, hence strongly', but its hypothesis is an L1 OPERATOR-NORM condition and it excludes families failing it. The Galerkin family fails it provably: ||Q_n - I|| = 1 for every n; ||Q_n V Q_n - V|| -> 0 would require V COMPACT; V contains multiplication by b_D(t,x) and by 1_{|x|<=r(t)}, and a multiplication operator on L2(R^3) is compact only if the multiplier vanishes a.e.
- **Source:** `STAGE8_RL2B_CONVERGENCE_HYPOTHESIS_RESOLUTION_AND_F5_TRILEMMA_V001.md:111` (SEALED (X.md.seal.sha256))
- **Quote:** Q_n -> I STRONGLY but NEVER IN NORM: ||Q_n - I|| = 1 for every n, since a
finite-rank projection cannot norm-approximate the identity in infinite
dimensions.
||Q_n V Q_n - V|| -> 0 would therefore require V COMPACT.
V IS NOT COMPACT
- **Why it matters:** DEAD ROUTE, explicitly fenced: 'That theorem is about smooth-to-sharp regularization of the interaction (V_eps -> V), an entirely different limit from Galerkin truncation of the carrier (Q_n V Q_n -> V). Reading it as covering the second is the program's characteristic failure mode again.'

## [THE GOVERNING TRILEMMA. Register row O-1: 'Does F\'-5 stand as written? HELD — pending Trotter-Kato'. F5_ruled_on = false.] *** THE F'-5 TRILEMMA — no horn delivers R-L2b as written ***
- **Statement:** With X_n = C_n(V_n(a)-V_n(0))C_n and R-L2b requiring sup_n ||X_n||_2 <= M with M admissible under F'-5: H1 the requirement list IS discharged -> weak lower semicontinuity plus the derived degree-0 symbol gives ||X||_2 = infinity, so NO SUCH M EXISTS and R-L2b's UNIFORMITY IS REFUTED. H2 the list is NOT discharged -> the finite objects do not approximate the parent, any bound on X_n is a bound on something that is not the parent's object, and its constant carries n, violating F'-5. H3 deny the continuum target -> kappa_record acquires a carrier index and F'-5 must be weakened, which is the principal's alone.
- **Source:** `STAGE8_RL2B_CONVERGENCE_HYPOTHESIS_RESOLUTION_AND_F5_TRILEMMA_V001.md:181` (SEALED (X.md.seal.sha256))
- **Quote:** **Every horn costs something, and no horn delivers R-L2b as written.** H1
refutes it. H2 disqualifies the bound as evidence about the parent. H3
requires amending a sealed scoping clause.
- **Why it matters:** THE central open decision. Note the self-executing clause: if H1 holds, R-L2b under F'-5 is a provably unsatisfiable obligation, and E1 v002's own text says the spec may not execute on it. AND note the correction: the decision is NOT 'which carrier' but 'does F'-5 stand as written'.

## [SELF-CORRECTION, INSTANCE 8. trilemma_withdrawn = false; target re-typed.] INSTANCE 8 — THE TRILEMMA CARRIED THE WRONG OBJECT: ||X||_2 instead of |C|_4^{-alpha}||X||_2
- **Statement:** The trilemma argued about ||X||_2 BARE. The sealed obligation is about G_hs = |C|_4^{-alpha} * ||X||_2, with a prefactor the trilemma was not carrying. That prefactor is not cosmetic: a divergent ||X||_2 with a compensating alpha can still give a finite G_hs as cells shrink. So H1's 'no uniform M exists' was stated about an object that is NOT the one R-L2b bounds. The trilemma is NOT withdrawn — its lemma, its refutation of the finite-rank framing, and its identification of U3 all stand; its TARGET is re-typed.
- **Source:** `STAGE8_X_TO_KAPPA_RECORD_EXTRACTION_DETERMINATION_V001.md:134` (SEALED (X.md.seal.sha256))
- **Quote:** THE F'-5 TRILEMMA ARGUED ABOUT ||X||_2 BARE. THE SEALED OBLIGATION IS ABOUT
      G_hs = |C|_4^{-alpha} · ||X||_2 ,
WITH A PREFACTOR I WAS NOT CARRYING. That prefactor is not cosmetic: a divergent ||X||_2 with
a compensating alpha can still give a finite G_hs as cells shrink.
- **Why it matters:** CRITICAL: anyone re-arguing the trilemma must argue about the PREFACTORED object. Also: |C|_4 is a cellulation geometric datum forbidden by F'-5 in general, and ADMITTED only under the E-Q1 Option-3 scoped grant (witness E1_CELL_4VOLUME_ADMITTED_ONLY_ON_PINNED_SKELETON), so S2 is well-formed ON THE PINNED SKELETON and may not be claimed over D3.

## [DISSOLVED TENSION — INSTANCE 9. conversion_step_exists_in_corpus = false (scoped to the sandwiched-vs-unsandwiched grading of p).] INSTANCE 9 — THE SYMBOL COLLISION ON 'X': p IS DEFINED ON THE UNSANDWICHED DIFFERENCE
- **Statement:** p is defined in exactly two sealed loci as an exponent on the kernel of the UNSANDWICHED difference V(a)-V(0), measured in r = |x-y|, entering as |X_diff(r)|^2 ~ r^{2p} inside the pair integral WITH |C(r)|^2 ~ r^{-6} CARRIED SEPARATELY. The degree-0/degree--3 result is about the SANDWICHED object C(V(a)-V(0))C. Both artifacts write 'X'. Converting the first into 'p = 0' requires a grading step the corpus NEVER PERFORMS.
- **Source:** `STAGE8_P_COINCIDENCE_EXPONENT_DETERMINATION_V001.md:51` (SEALED (X.md.seal.sha256))
- **Quote:** THE COLLISION, EXHIBITED: the symbol "X" denotes V(a) - V(0) in the two artifacts that DEFINE p,
and denotes C(V(a) - V(0))C in the three that REASON ABOUT THE SANDWICHED OBJECT. One letter,
two objects, and the question inherited the ambiguity from this lane's own artifacts.
- **Why it matters:** NAMESPACE HAZARD, ACTIVE. Also: the flag conversion_step_exists_in_corpus = false is scoped to THIS conversion (both sides on the coincidence axis) and was later MIS-CITED for the coincidence-to-cell-scale conversion. Do not repeat that mis-citation.

## [UNDETERMINED_BY_SEALED_TEXT. Four verifiers, four times, under a standard asymmetric AGAINST any definite p.] p IS UNDETERMINED BY SEALED TEXT — and even p = 0 does not close the program
- **Statement:** Answer: NEITHER 0 NOR 1. p is undetermined by sealed text for the object. p is a single exponent, not a spectrum ('p_effective' returns zero occurrences). None of the seven mechanisms claims the object's p; three say so in their own flags. And the p = 0 branch does not close the program: the counting does not exclude a region-level route at p = 0, because the region-level target (Gamma_K = -log|A_K|) is built from a log and derivatives of a NORMALIZED amplitude, a connected/cumulant object with cancellations available.
- **Source:** `STAGE8_P_COINCIDENCE_EXPONENT_DETERMINATION_V001.md:106` (SEALED (X.md.seal.sha256))
- **Quote:** CONSEQUENCE FOR THE FRAMING: the premise "p = 0 closes the program with a determinate negative"
DOES NOT HOLD ON SEALED TEXT. Even the unfavourable branch leaves a route undetermined.
- **Why it matters:** Do not treat any p value as established, in either direction. The well-posed successor is narrower: does the connected region object have to pass through D5's ABSOLUTE anchored sum, or does a cancellation-preserving route exist? NEITHER IS BEGUN.

## [DETERMINED: NOT_FORCED. answer_upgraded_to_theorem = false. 'R-L2b remains open in the ordinary way — hard, unrouted, and not shown impossible.'] IS R-L2b's FAILURE FORCED BY F'-5? NOT FORCED — on affirmative grounds
- **Statement:** Answer NOT FORCED, typed as a BOUNDED NEGATIVE EXISTENTIAL, defeated on affirmative grounds by two counterexamples: (1) R-L2b is TRUE at fixed carrier, uniform in the diamond, which KEEPS the cellulation quantifier and escapes on the CARRIER axis; (2) Route T / O3+O7 in the parent majorant spec, which contains no F'-5 at all and failed for O7's refuted intertwiner. Where F'-5 bites it is the CARRIER-INDEX clause, not the CELLULATION-GEOMETRIC-DATUM clause. Zero of the closed mechanisms are attributable to F'-5. Searched *.md, *.json AND *.py (2,037 .py, 250 .json) — zero hits.
- **Source:** `STAGE8_IS_RL2B_FAILURE_FORCED_BY_F5_DETERMINATION_V001.md:202` (SEALED (X.md.seal.sha256))
- **Quote:** THE DIFFICULTY IS RELOCATED, WHICH IS THE USEFUL RESIDUE. R-L2b's live obstruction is on the
CARRIER axis and in the seven algebraic/physical closures, NOT in F'-5's cellulation-blindness.
So the question that governs it is still the one already held: at what carrier is the object
defined. F'-5's cellulation clause is not the executioner.
- **Why it matters:** CAUTION: this determination's Ground (A) was later CORRECTED (see next item), and its seven-count was corrected to five. The ANSWER survives both corrections unchanged.

## [ERRATUM RAISED, NOT ACTED ON. F5_edited = false; F5_weakened = false; F'-5 still binds as sealed. Ground (A) of the forcing determination corrected; the answer strengthened.] F'-5 PROVENANCE ERRATUM — F'-5 claims verbatim binding of a clause it STRENGTHENS
- **Statement:** F'-5 opens 'SPEC-HEADER SCOPING CLAUSE 1 BINDS VERBATIM', but the parent clause says materially less. Three differences: (i) 'AND NO CELLULATION GEOMETRIC DATUM' IS NOT IN THE PARENT — the parent forbids a cellulation-family INDEX, a label; F'-5 forbids any GEOMETRIC datum (|C|_4, diameter, aspect ratio); (ii) the enforcement-mechanism sentence is not in the parent; (iii) the tuple's fourth entry differs (parent p_lambda vs F'-5 |w_lambda|). The parent clause is titled 'CONSTANTS ARE CARRIER-INDEX-BLIND'.
- **Source:** `STAGE8_F5_PROVENANCE_ERRATUM_AND_FORCING_GROUND_CORRECTION_V001.md:42` (SEALED (X.md.seal.sha256))
- **Quote:**   (i)  *** "AND NO CELLULATION GEOMETRIC DATUM" IS NOT IN THE PARENT. ***
       The parent forbids a cellulation-family INDEX — a label. F'-5 forbids any cellulation
       GEOMETRIC DATUM — |C|_4, diameter, aspect ratio. THESE ARE DIFFERENT PROHIBITIONS, and
       the second is the one the forcing question is entirely about.
- **Why it matters:** A lane reading F'-5 would believe the cellulation-geometric-datum prohibition carries PARENTAL authority. It does not. Also raises a SECOND erratum: STAGE8_T7_REFINEMENT_DEPENDENCE_ADDENDUM_V001:58's sealed count '"aspect ratio" 0' is contradicted three times by its own file.

## [SELF-CORRECTION, INSTANCE 12. 'What was wrong was the reason, not the result.'] INSTANCE 12 — the p-determination's 'wrong axis' claim about time integration is FALSE
- **Statement:** The p-determination stated that the live time-integration smoothing statement is on the wrong axis (large separation, not coincidence). That is wrong: there are TWO statements on TWO axes, and the coincidence one exists — it is C6, whose locus is stated as the volume diagonal x = y. Error class: FALSE NEGATIVE EXISTENTIAL FROM AN UNDER-SEARCHED FILE, third occurrence. The p-determination's CONCLUSION is unaffected and if anything strengthened, because C6's statement is modal and carries no exponent.
- **Source:** `STAGE8_TWO_UNTRIED_MECHANISMS_ATTACK_RESULT_V001.md:78` (SEALED (X.md.seal.sha256))
- **Quote:** *** THAT IS WRONG. THERE ARE TWO STATEMENTS ON TWO AXES, AND THE COINCIDENCE ONE EXISTS: IT IS C6,
whose locus is stated as the volume diagonal x = y. My sweep found the separation statement and
concluded the coincidence one did not exist. ***
- **Why it matters:** Directly relevant to this briefing's own method: narrow greps produce false negative existentials in this corpus, repeatedly.

## [WITHDRAWN. discriminator = UNDETERMINED. Fifth withdrawal of the day; INSTANCE 13.] INSTANCE 13 — THE 'ASSUMPTION PROBLEM' DIAGNOSIS IS WITHDRAWN
- **Statement:** The claim that the seven-item ledger discriminates an assumption problem from a hard, unrouted obligation is WITHDRAWN to a suspicion. Re-classified from each closure's own artifact: exactly ONE limb fits 'wrong axis'; ZERO fit 'carrier-gated'; FOUR carry self-standing, carrier-invariant grounds. Commutator Ground 1 (p=1 against a p>3/2 threshold, right axis, right object, not enough) is POSITIVE EVIDENCE FOR THE HARD-PROBLEM READING. No undisclosed load-bearing premise is nameable; every candidate is a DISCLOSED gap.
- **Source:** `STAGE8_DISCRIMINATOR_CLAIM_WITHDRAWAL_V001.md:43` (SEALED (X.md.seal.sha256))
- **Quote:** TALLY OVER THE FIVE MY CLAIM GENERALISED ACROSS: exactly ONE limb fits "wrong axis"; ZERO fit
"carrier-gated"; FOUR carry SELF-STANDING, CARRIER-INVARIANT grounds.
*** MY CLAUSE "RATHER THAN FOR REASONS OF THEIR OWN" IS FALSE FOR FOUR OF THE FIVE. ***
- **Why it matters:** DO NOT re-propose 'R-L2b is mis-typed' as a finding. It was proposed, tested against the corpus, and withdrawn — with the note that 'EVEN THE UNDECLARED IS DECLARED AS UNDECLARED. THIS CORPUS'S FAILURE MODE IS NOT CONCEALMENT.'

## [THE PROPOSITION TO BE PROVED. Not begun. GATED ON U3.] *** WHAT WOULD DISCHARGE R-L2b — the named object, in one sentence ***
- **Statement:** THE CELL-SCALE SCALING OF || C (V(a) - V(0)) C ||_2 RESTRICTED TO A SINGLE CHARTERED DIAMOND, AS THAT DIAMOND'S ONE PARAMETER GOES TO ZERO — DERIVED, NOT POWER-COUNTED. What counts as deriving it: an exponent for that norm on the one-parameter isotropic family, established for the SUBTRACTED TWO-TIME object (not the unsubtracted sea kernel, and not the deleted S3), AT A STATED CARRIER, with the p -> alpha step performed as a derivation rather than power counting.
- **Source:** `STAGE8_RL2B_REMAINING_CONTENT_UNDER_THE_CHARTER_V001.md:128` (SEALED (X.md.seal.sha256))
- **Quote:** *** THE OBJECT WHOSE DERIVATION WOULD DISCHARGE R-L2b:
    THE CELL-SCALE SCALING OF  || C (V(a) - V(0)) C ||_2  RESTRICTED TO A SINGLE CHARTERED DIAMOND,
    AS THAT DIAMOND'S ONE PARAMETER GOES TO ZERO — DERIVED, NOT POWER-COUNTED. ***
- **Why it matters:** THE ANSWER TO SWEEP QUESTION (6). Four qualifiers are all load-bearing: single chartered diamond; one parameter -> 0; subtracted two-time object; stated carrier; derivation not power counting.

## [BEGUN (as the successor framing). The prior diagonal-attack lemma and the trilemma feed it directly once re-typed onto the prefactored object.] THE SAME PROPOSITION WITH THE NORMALIZATION VISIBLE — the successor question actually begun
- **Statement:** Does there exist alpha such that |C|_4^{-alpha} * ||C(V(a)-V(0))C||_2 is finite and uniform as cells shrink, ON THE PINNED SKELETON? This is R-L2b stated with the normalization visible: it is what S2 needs, what the per-cell majorant needs, and the exponent the corpus marks NOT ASSERTED.
- **Source:** `STAGE8_X_TO_KAPPA_RECORD_EXTRACTION_DETERMINATION_V001.md:246` (SEALED (X.md.seal.sha256))
- **Quote:** THE SUCCESSOR QUESTION IS NOW WELL-POSED AND IT IS NOT THE ONE THIS LANE WAS ATTACKING:
      does there exist alpha such that   |C|_4^{-alpha} · ||C(V(a)-V(0))C||_2
      is finite and uniform as cells shrink, ON THE PINNED SKELETON?
- **Why it matters:** The 'ON THE PINNED SKELETON' scoping comes from the E-Q1 Option-3 grant and is MANDATORY in verdict language: every relying verdict must say 'on the pinned skeleton' and may NOT say 'over D3'.

## [DETERMINED. deriving_p_would_discharge_RL2b = FALSE — leaves p -> alpha owed as a derivation, gated on U3.] DERIVING p WOULD NOT DISCHARGE R-L2b — the p -> alpha step is owed as a DERIVATION
- **Statement:** A stated conditional linking p to alpha EXISTS in the corpus and was written for S2 (three places: 'alpha IS SET BY THE CANCELLATION RATE'; alpha_eq_1_iff = degree_minus_3_singularity_fully_cancels_in_the_difference; 'p > 3/2 -> C X C is Hilbert-Schmidt; combined with the aggregation arithmetic, alpha = 1'). But ALL THREE ARE SELF-LABELLED NON-DERIVATIONAL, and a DERIVED cell-scale scaling statement for S2's numerator does not exist. The gap changes shape: from 'no conversion exists' to 'the conversion exists at power-counting grade and has never been upgraded to a derivation.'
- **Source:** `STAGE8_RL2B_REMAINING_CONTENT_UNDER_THE_CHARTER_V001.md:96` (SEALED (X.md.seal.sha256))
- **Quote:** CONSEQUENCE: deriving p would NOT discharge R-L2b unaided. It would leave the p -> alpha step owed
AS A DERIVATION, and leave it gated on U3.
- **Why it matters:** Anyone who sets out to derive p must know in advance that success does not close R-L2b. Two axes: coincidence (p) and cell-scale (alpha); the bridge between them is power-counted only.

## [ADJUDICATED — NOT A CONFLICT. R-L2b's derivation is not currently well-posed (U3-gated); the connected-correction object is defined and sealed at two orders; they are different objects and the second does not make the first well-posed.] *** ADJUDICATION OF THE WELL-POSEDNESS CONTEST: THE TWO TEXTS ARE ABOUT DIFFERENT OBJECTS ***
- **Statement:** Text A: 'SO THE OBJECT IS NAMED AND ITS DERIVATION IS NOT CURRENTLY WELL-POSED' — this is about R-L2b's named object (the cell-scale scaling of ||C(V(a)-V(0))C||_2 on a diamond), and its ground is that U3 has not typed the carrier, so 'p is not a property of the sealed object' at finite rank and the continuum reading is the one U3 decides. Text B: R2's object IS 'DEFINED AND SEALED at two orders' — but the object there is the Möbius/Ursell activity Phi_gamma (general n, sealed) and W1 (n = 2, sealed, frozen history a = (7/100, -11/100)), which is a CLUSTER-EXPANSION object on the Z_K side, not G_hs's numerator. The SAME artifact that supplies Text B states r2_reaches_RL2b = false and 'R2 DOES NOT REACH R-L2b. NOT PARTIALLY, NOT WEAKLY, NOT VIA ARM 2.' NO CONTRADICTION: both stand.
- **Source:** `STAGE8_RL2B_REMAINING_CONTENT_UNDER_THE_CHARTER_V001.md:135` (SEALED (X.md.seal.sha256))
- **Quote:** IT IS GATED ON U3: until the carrier is typed, the object does not have a determinate scaling —
"p is not a property of the sealed object" at finite rank, and the continuum reading is the one U3
decides. SO THE OBJECT IS NAMED AND ITS DERIVATION IS NOT CURRENTLY WELL-POSED.
- **Why it matters:** THE ANSWER TO SWEEP QUESTION (7). Do not cite R2's 'well-posed at two orders' as evidence that R-L2b is well-posed. The corresponding counter-text is at STAGE8_R2_WELL_POSEDNESS_AND_INPUT_SEAL_DETERMINATION_V001.md:149-165 and :218-234.

## [OBJECT GATE PASSED for R2 — first of four obligations to clear it that day (U1, the IBP, and Q_cell all died at it).] THE COUNTER-TEXT IN FULL: R2's object IS defined and sealed at two orders
- **Statement:** General n: Phi_gamma(a) := -sum_{0!=gamma' subseteq gamma} (-1)^{|gamma|-|gamma'|} Log Z_hat_comp^(K,gamma')(a), sealed at MAJORANT_LEMMA0_PROOF_DRAFT_V001.md:329-331 with SEAL_MATCH; variable per-cell complexified history a_c; domain closed polydisc |a_c| <= eps_star. n = 2: W1 := -Log Z_hat_comp^(12)(a) + Log Z_hat_comp^(1)(a) + Log Z_hat_comp^(2)(a), sealed, frozen history, carrier pinned by M-9, comparator |C|_4 eta^2/(1-eta), refutation criterion written. And connected_cross_cell_terms_derived = false means DEFINED-BUT-UNPROVED, not undefined.
- **Source:** `STAGE8_R2_WELL_POSEDNESS_AND_INPUT_SEAL_DETERMINATION_V001.md:149` (SEALED (X.md.seal.sha256))
- **Quote:** Three obligations died today at the same gate — U1's norm object (no referent for "the smooth
cell profiles"), the IBP's seven inputs (zero sealed), Q_cell (a slot list with no slots filled).
**The gate was applied to R2 first, and R2 clears it, on sealed referents at two orders:**
- **Why it matters:** The 'defined connected correction at two orders' the contest refers to. Its qualification: 'The pass is complete at n = 2 and partial at general n' — and the n = 2 form is available ONLY under R1, which is NOT CHARTERED.

## [RULED: hessian_first_supersession = NOT_CHARTERED. TRIGGER HAS NOT FIRED (RL2b_closed=false; RL2b_refuted=false; search_exhausted=FALSE). R1 as stated does not carry F2 or F5.] THE HESSIAN-FIRST SUPERSESSION (route-list R1) — NOT CHARTERED, with five fallback terms fixed in advance
- **Statement:** Not chartered because both lanes agree it would CONCEAL the extensivity question — nothing at second order can test ALL-ORDER record-action extensivity. Available as fallback ONLY IF R-L2b FAILS, on five terms recorded in advance so they are not renegotiated later: F1 it must state that it SUPERSEDES T7(iii) and does NOT prove the linked-cluster density object; F2 it carries the V010-style zero-stiffness control; F3 it proves cellulation-independence of the second-order term; F4 it is sourced Hessian-first, explicitly; F5 Theorem 3's five conditions listed VERBATIM as an open register.
- **Source:** `STAGE8_EXTENSIVITY_VERDICT_AND_RL2B_CAMPAIGN_OPENING_V001.md:115` (SEALED (X.md.seal.sha256))
- **Quote:** AVAILABLE AS FALLBACK IF R-L2b FAILS, on five terms, all recorded now so
they are not renegotiated later:
  F1 it must state that it SUPERSEDES T7(iii) and does NOT satisfy or prove
     the linked-cluster density object;
- **Why it matters:** *** THE REGISTER HAS NO ROW FOR THIS RULING. *** STAGE8_LANE_STATUS.md carries R-1..R-15 and none of them is hessian_first_supersession = NOT_CHARTERED; the gap is separately recorded as needing a row (STAGE8_R2_DETERMINATION_ERRATUM_001_R1_RULING_REACH.md:347, :333). Do not treat the register as the authority on what has been ruled.

## [A CONTINGENCY. NOT PURSUED. Register R-5: 'Extensivity contingency (would be a new principle) — DEFERRED, unadopted'.] THE NAMED FALLBACK SHAPE IF CONNECTED EXTENSIVITY FAILS — a RUNNING kappa_record. NAMED, NOT PURSUED.
- **Statement:** If connected extensivity does fail, NO SEALED REPLACEMENT CONSTRUCTION EXISTS — both lanes confirm independently. The nearest shape, named and not pursued: a RUNNING kappa_record — a response depending on the cellulation scale rather than converging to an intensive constant, i.e. a renormalization-group structure rather than a thermodynamic-limit one. It would be a NEW PRINCIPLE, is the principal's to charter, and would collide with Theorem 1's derived intensivity for the disjoint part unless reconciled.
- **Source:** `STAGE8_EXTENSIVITY_VERDICT_AND_RL2B_CAMPAIGN_OPENING_V001.md:135` (SEALED (X.md.seal.sha256))
- **Quote:** THE NEAREST SHAPE, named and NOT pursued: a RUNNING kappa_record — a
response that depends on the cellulation scale rather than converging to an
intensive constant, i.e. a RENORMALIZATION-GROUP structure rather than a
thermodynamic-limit one.
- **Why it matters:** Recorded so it is not rediscovered. Do not propose it as a lane route; it is a principal-only new principle.

## [RULED 2026-07-27 by the principal (Route 2 ratified). RL2b_is_a_Z_K_side_obligation = true. RL2b_refuted = false.] R-L2b IS A Z_K-SIDE OBLIGATION, DOWNSTREAM OF THE A2 STATE EVALUATION (Route 2 ratified)
- **Statement:** Under the ratified Route 2 architecture, A4(3) places the zero-free neighborhood, logarithm branch, connected linked-cluster density and intensive Hessian on Z_K — 'not on a nonexistent primitive scalar.' R-L2b serves the linked-cluster density, therefore R-L2b is a Z_K-side obligation, and this campaign's negative results on per-cell majorization land THERE rather than on Stage 8's primitive obligations. This decoupling is a CONSEQUENCE of the ruling and is EXPRESSLY NOT A GROUND FOR IT.
- **Source:** `STAGE8_ROUTE2_RATIFICATION_AND_FRAMING_CORRECTION_V001.md:117` (SEALED (X.md.seal.sha256))
- **Quote:** UNDER ROUTE 2, A4(3) PLACES THE ZERO-FREE NEIGHBORHOOD, LOGARITHM BRANCH, CONNECTED
LINKED-CLUSTER DENSITY AND INTENSIVE HESSIAN ON Z_K — VERBATIM, "not on a nonexistent primitive
scalar." R-L2b serves the linked-cluster density. THEREFORE R-L2b IS A Z_K-SIDE OBLIGATION,
DOWNSTREAM OF THE A2 STATE EVALUATION
- **Why it matters:** THE MOST RECENT RE-LOCATION OF R-L2b IN THE ARCHITECTURE, and the most likely to be missed. The ruling 'falls with' ground §4(a) if the source-scalarization no-go's independent confirmation is ever overturned.

## [DETERMINED. ratio_makes_HS_irrelevant = FALSE — DENIED BY SEALED TEXT. F5_is_moot = false; F'-5 IS LIVE.] X IS THE S2 OPERATOR — the normalization RELOCATES the HS question, it does not cancel it
- **Statement:** The amplitude IS a normalized ratio (five sealed spellings). The corpus ADOPTS half the principal's hypothesis — the ratio kills the BASELINE divergence, and S3/G_bl was deleted on exactly that ground — and DENIES the other half: the replacement constant is still a Hilbert-Schmidt norm and its operator is X. 'The ratio does not cancel the HS question. It RELOCATES it from the baseline operator to the a-difference operator, and the a-difference operator IS X.' Whether the singularity fully cancels in the a-difference is explicitly UNKNOWN in sealed text.
- **Source:** `STAGE8_X_TO_KAPPA_RECORD_EXTRACTION_DETERMINATION_V001.md:14` (SEALED (X.md.seal.sha256))
- **Quote:** SO THE PRINCIPAL'S HYPOTHESIS (b) SPLITS: the amplitude IS a normalized ratio, CONFIRMED
in five sealed spellings; but the corollary — that the ratio makes Hilbert-Schmidt
behaviour IRRELEVANT to kappa_record — IS DENIED BY SEALED TEXT.
- **Why it matters:** THE HOLD ON F'-5 WAS PREMISED ON THE OPPOSITE. Register flag F5_hold_premise = CHECKED_AND_FAILED — F'-5 IS LIVE, not moot. Do not re-propose 'the ratio makes it moot'.

## [BRIDGE_ABSENT (bounded negative existential) + SEALED NO-GO. kappa_record = kappa_Thomson is ASSUMED, NOT DERIVED (V011:2077).] THE DIRECT EXTRACTION FROM X TO kappa_record IS ABSENT — and carries a sealed no-go
- **Statement:** No artifact defines an extraction, formula, map or derivation taking X to kappa_record. Bounded search over .md, .json AND .py including scripts/ and stage8_execution/, across a long enumerated pattern list; three PARTIAL fragments could be mistaken for a bridge; none connects the two ends. Both flags actual_finite_parent_operator_to_scalar_bridge_derived = false and kappa_record_computed = false are FALSE everywhere, always, never true. And the step carries a sealed, independently confirmed no-go: PRIMITIVE_SOURCE_SCALARIZATION_BLOCKED.
- **Source:** `STAGE8_X_TO_KAPPA_RECORD_EXTRACTION_DETERMINATION_V001.md:153` (SEALED (X.md.seal.sha256))
- **Quote:** BRIDGE_ABSENT. No artifact defines an extraction, formula, map or derivation taking X to
kappa_record.
- **Why it matters:** Even a closed R-L2b does not by itself produce kappa_record. And O-13 is open: two sealed authorities conflict on whether Stage 8 emits kappa_record at all.

## [FROZEN PREDICTION, NOT REVISABLE, IN TENSION WITH THE CAMPAIGN'S AGGREGATION ARITHMETIC. Neither is a derivation.] PA-2b — A LIVE FROZEN PREDICTION THAT R-L2b RETURNS alpha = 1/2
- **Statement:** The spec's frozen prediction PA-2b states: 'R-L2b returns alpha = 1/2 for the SUBTRACTED HS density (via cell time extent + Gevrey b_D) but the derivation is not trivial. Confidence: low-moderate.' It sits alongside C-13's striking of the asserted 1/2 and alongside the campaign's later finding that D5 requires alpha >= 1 and that alpha = 1/2 would be an AREA LAW, the signature of a support-drawn bound.
- **Source:** `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:1945` (SEALED (X.md.seal.sha256))
- **Quote:** PA-2b OUTCOME-CLASS. R-L2b returns alpha = 1/2 for the SUBTRACTED HS density
      (via cell time extent + Gevrey b_D) but the derivation is not
      trivial. Confidence: low-moderate. Stated because v001 asserted 1/2 with
      no derivation and was caught.
- **Why it matters:** A lane finding alpha = 1/2 must know this prediction exists and was frozen in advance; a lane finding alpha >= 1 must know it CONTRADICTS a frozen prediction and say so. Do not silently resolve the tension.

## [PREDECLARED VERDICT, FROZEN AND NOT REVISABLE] WHERE R-L2b SITS IN THE VERDICT CHAIN — the certification clause
- **Statement:** E1S_REPLACEMENT_ARCHITECTURE_CERTIFIED holds iff R-L0 (or R-L0b) and R-L1, R-L2, R-L2b, R-L3, R-L4a, R-L4b, R-L4, R-L5 discharge; AND A-L0 (arm 2, BOTH Huygens factors) closes; AND A-L5 closes; AND at least one of {IR-B, IR-C} closes; AND eta_1, eta_{>=2} are certified with Gamma_star^split <= 1; AND all controls NC1-NC11 behave; AND W1 is computed and inside its comparator; AND §Q2-STOP is not triggered.
- **Source:** `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:1787` (SEALED (X.md.seal.sha256))
- **Quote:** E1S_REPLACEMENT_ARCHITECTURE_CERTIFIED
    iff R-L0 (or R-L0b) and R-L1, R-L2, R-L2b, R-L3, R-L4a, R-L4b, R-L4, R-L5
    discharge; AND A-L0 (arm 2, BOTH Huygens factors) closes; AND A-L5 closes;
- **Why it matters:** R-L2b is necessary but very far from sufficient. Closing it does not certify the architecture; roughly a dozen other conjuncts remain.

## [OPEN OBLIGATION with a named witness (E1_CELL_SCALE_NORMALIZATION_UNCERTIFIED) and a named failure hazard] R-L0 IS THE ENFORCEMENT MECHANISM AND MAY FAIL — the tau_R hazard, stated
- **Statement:** R-L0 requires exhibiting X_*(eps) with x(C,eps) = |C|_4 g(C,eps) <= X_*(eps) for EVERY admitted cell of D3. Two admissible grounds only: (i) scale covariance, (ii) uniform smallness. THE HAZARD, STATED: tau_R is scale-INVARIANT — every refined cell inserts a FULL record cycle at every refinement depth, at exact phase e^{+-i pi} = -1. This is the structural root of the O7 obstruction and the same fact that saturates C4. It is therefore NOT a priori true that g carries the compensating weight, and R-L0 MAY FAIL.
- **Source:** `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:867` (SEALED (X.md.seal.sha256))
- **Quote:**       THE HAZARD, STATED: tau_R is scale-INVARIANT — every refined cell
      inserts a FULL record cycle at every refinement depth, at exact phase
      e^{+-i pi} = -1. This is the structural root of the O7 obstruction
      (3c81647e…) and the same fact that saturates C4. It is therefore NOT a
      priori true that g carries the compensating weight, and R-L0 MAY FAIL.
- **Why it matters:** R-L0 consumes G_hs and is F'-5's enforcement mechanism. R-L0 and R-L2b are word-for-word the same obligations inside the shape-regular class C_ref, which is why narrowing to C_ref would NOT rescue the object (AMENDMENT_001 F-2).

## [DERIVED, verified at source; refutes P-S1's ground and supplies the transport charter's decisive G4] THE COMPLETED RESPONSE IS A RATIO — and a-independent per-cell factors CANCEL BEFORE ANY ACTIVITY FORMS
- **Statement:** Z_hat_comp(a) := Z_comp(a)/Z_comp(0), so Z_hat_comp(0) = 1 identically on every admitted complex, Gamma(0) = 0, and Phi_gamma(0) = 0 identically — every cluster, every refinement depth, EVERY CELL SHAPE. The record term is a-INDEPENDENT (generator carries the record tier as +lambda v(t) M(t) tensor S_n while the history enters ONLY as +a J(t) tensor I_R). Therefore an a-independent per-cell factor is annihilated by the ratio.
- **Source:** `STAGE8_T7_SLIVER_NATURALITY_ATTEMPT_RESULT_V001.md:37` (SEALED (X.md.seal.sha256))
- **Quote:**  1. THE COMPLETED RESPONSE IS A RATIO. Majorant spec D1, line 116:
        Z_hat_comp(a) := Z_comp(a) / Z_comp(0)
    so Z_hat_comp(0) = 1 IDENTICALLY on every admitted complex, whence
    Gamma(0) = 0
- **Why it matters:** DEAD ARGUMENT, twice refuted: 'refining a cell multiplies per-cell record content by N at unchanged volume' does NOT reach the response. Do not re-propose it. The tau_R obstruction's CORRECT home is inside the a-dependent connected series.

## [CONFIRMED ABSENT in .py and .json under the three named patterns. (Independently matches the report in the F'-5 forcing determination.)] NO CODE, NO JSON, NO WITNESS ANYWHERE FOR R-L2b
- **Statement:** BOUNDED NEGATIVE EXISTENTIAL, this sweep: grep for the literal strings 'L2b', 'G_hs' and 'SCAD_HS' across all .py and .json files in the corpus, excluding the vendored sympy tree — 2,037 .py files and 250 .json files — returns ZERO files. R-L2b has no audit script, no witness code, no result JSON, and no machine-readable flag outside the .md artifacts.
- **Source:** `STAGE8_IS_RL2B_FAILURE_FORCED_BY_F5_DETERMINATION_V001.md:13` (SEALED (X.md.seal.sha256); re-measured independently by this sweep)
- **Quote:** Searched
across *.md, *.json AND *.py (2,037 .py, 250 .json), zero hits.
- **Why it matters:** R-L2b lives entirely in prose. There is nothing executable to run, extend, or re-run. Any lane looking for a script to modify will not find one, and should not create one without a charter.

## [ACTIVE HAZARD, RE-CHECKED AND CLEARED for the R1/R2/F5 cases; no namespace register exists] ACTIVE NAMESPACE COLLISIONS ON THIS CAMPAIGN — enumerated by the corpus itself
- **Statement:** 'Route 2' in the ratification artifact is the ARCHITECTURE route, not the route list's R2. 'F5' in the R-L2b-forcing determination is the spec constraint F'-5, not the ruling's fifth fallback term. 'THE CORPUS NOW CARRIES AT LEAST FOUR R1 NAMESPACES, TWO F5 NAMESPACES AND TWO ROUTE-2 NAMESPACES. A NAMESPACE REGISTER WOULD BE WORTH MORE THAN ANY SINGLE ERRATUM.' Additionally: 'alpha' denotes the S2 exponent, the Dirac alpha matrices, and the fine-structure constant; 'X' denoted both V(a)-V(0) and C(V(a)-V(0))C (INSTANCE 9); 'the five' denotes two different mechanism sets.
- **Source:** `STAGE8_R2_DETERMINATION_ERRATUM_001_R1_RULING_REACH.md:354` (SEALED (X.md.seal.sha256))
- **Quote:** (d) NAMESPACE COLLISIONS, RE-CHECKED AND CLEARED so no one re-trips: "Route 2" in the RATIFICATION
    artifact is the architecture route, not the route list's R2; "F5" in the RL2b-forcing
    determination is the spec constraint F'-5, not the ruling's fifth fallback term. THE CORPUS
    NOW CARRIES AT LEAST FOUR R1 NAMESPACES, TWO F5 NAMESPACES AND TWO ROUTE-2 NAMESPACES.
- **Why it matters:** ALWAYS DISAMBIGUATE BY QUOTING THE DEFINING TEXT. The two F5s specifically: F5 = the fifth Hessian-fallback term (Theorem 3's five conditions as an open register), at CAMPAIGN_OPENING:124-127; F'-5 = the spec scoping clause forbidding carrier indices and cellulation geometric data, at SPEC_V002:1671-1677.

## [route_adopted = none. R1 NOT CHARTERED; R2 startable but discharges nothing; R3 not a route alone; R4 unadopted.] THE FOUR ROUTES FOUND (route-list R1-R4), and their present status
- **Statement:** R1 HESSIAN-ONLY RE-POSING — bypasses eps_star, O5/clause (3), A-L5, recast Q6; needs T7(ii), the n=2 connected term, and (4)(ii); a principal re-posing. RULED NOT CHARTERED. R2 EXACT-MONOIDALITY ISOLATION — isolates arm 2 rather than bypassing it; determined not to reach R-L2b; its tractable (n=2) form is available ONLY under R1 and is therefore unavailable. R3 ISOTROPIC-COVARIANCE REDUCTION — the dilation direction is fixed by the sealed scale orbit; not a route alone. R4 FIXTURE-FIRST WITH UNIVERSALITY DEFERRED — needs no new mathematics, establishes least. NONE ADOPTED.
- **Source:** `STAGE8_RL2B_OVER_CHARTER_AND_BLIND_ROUTE_FINDING_V001.md:253` (SEALED (X.md.seal.sha256))
- **Quote:**  R1  HESSIAN-ONLY RE-POSING (C.4). Bypasses eps_star, O5/clause (3), A-L5
     and recast Q6. Needs T7(ii), the n = 2 connected term, and (4)(ii).
     Requires a principal re-posing of the battery requirement. FIRST.
- **Why it matters:** THE ROUTE LIST'S R1/R2 ARE TWO OF THE SEVEN 'R1' NAMESPACES. This list predates the NOT-CHARTERED ruling by 72 minutes and 'DOES NOT DEFY IT'. Do not re-propose R1 as available: the fallback trigger has not fired.

## [CLAUSE-BY-CLAUSE STATUS OF RECORD. Corpus closure scan: no_successor_closure_found = TRUE, true_hit_count = 0.] T7(iii)'s FOUR CLAUSES — where R-L2b lives in the theorem, and what else is unsupplied
- **Statement:** (1) COMPOSITION, cell-local per Lemma 0: PASS, exact_disjoint_monoidal_additivity_proved = TRUE. (2) CLUSTER EXPANSION + MAJORANT uniformly in K and X including common refinements: BLOCKED — this is where R-L2b, A-L0 arm 2 and A-L5 live. (3) DIFFERENTIATED SERIES (O5): SEPARATELY UNSUPPLIED, and 'convergence of the undifferentiated series does not imply this and may not be cited for it.' (4) COROLLARIES (i)(ii)(iii). Separately, T7(ii) volume_uniform_zero_free_neighborhood_proved = FALSE, gating thermodynamic_log_hessian_authorized = FALSE.
- **Source:** `STAGE8_RL2B_OVER_CHARTER_AND_BLIND_ROUTE_FINDING_V001.md:96` (SEALED (X.md.seal.sha256))
- **Quote:**   (2) CLUSTER EXPANSION + MAJORANT on |a_c| <= eps_*, absolutely
      convergent, action-density form, UNIFORMLY IN K AND X INCLUDING
      COMMON REFINEMENTS.  BLOCKED. This is where R-L2b, A-L0 arm 2 and
      A-L5 live.
- **Why it matters:** O5 is SEPARATELY UNSUPPLIED and may not be inferred from clause (2). A lane that closes R-L2b has closed part of clause (2) only. The chain to kappa_record is (2) -> (3)/O5 -> (4)(iii) -> T7(iv), AND T7(ii).

## [THREE ACCEPTED AND OPEN; O-D3 is the hard one and the charter degrades into a NEW PRINCIPLE without it. O-D4 flagged, not accepted. O-D3 is UNTOUCHED.] THE CHARTER'S THREE ACCEPTED OBLIGATIONS (O-D1/O-D2/O-D3) AND THE FOURTH FLAGGED (O-D4)
- **Statement:** O-D1 DIAMONDS DO NOT TILE — exhibit a decomposition scheme with disjoint diamonds whose 4-volumes sum EXACTLY to |C|_4 and whose residual is null, or prove convergence and tail control for countably many. O-D2 COUNT GROWTH AND THE D2 RE-TYPING (N(C) ~ A^3). O-D3 DECOMPOSITION-INDEPENDENCE — prove the completed response is independent of which admissible decomposition is chosen, or exhibit a canonical scheme and prove canonicity; charter_remains_a_definition_iff = O-D3_discharged. O-D4 the source-independence unit (atom or diamond?) — flagged, NOT accepted (register O-6).
- **Source:** `STAGE8_TRANSPORT_FUNCTOR_CHARTER_V001.md:182` (SEALED (X.md.seal.sha256))
- **Quote:** O-D3  DECOMPOSITION-INDEPENDENCE. The decomposition is NOT UNIQUE. The
      obligation: prove the completed response is independent of which
      admissible decomposition is chosen — or exhibit a CANONICAL scheme and
      prove canonicity, which converts the obligation into a definition.
- **Why it matters:** The combinatorial residue of the sliver relocation lives HERE, not in R-L2b: 'THE COMBINATORIAL WORK IS REAL BUT IT IS NOT R-L2b: it is O-D1 and O-D3, the charter's own undischarged obligations.' They are separately open.

## [SETTLED (hostility of the class) / NOT SETTLED (any scaling statement). subtracted_response_scaling_in_|C|_4 = NOT_DERIVED_IN_EITHER_DIRECTION.] THE ADMITTED CLASS IS AS HOSTILE AS ASSUMED — arbitrarily small cells, unbounded aspect ratio, unbounded facet count
- **Statement:** Under the ratified D3 reading (register R-11: ALL common refinements), the admitted class includes cells of ARBITRARILY SMALL 4-VOLUME, UNBOUNDED ASPECT RATIO (slivers/needles), and UNBOUNDED FACET COUNT. So R-L0 is a real obligation and not a formality. AND: the corpus does NOT state or entail a value for sup over admitted cells of G_hs — its finiteness IS R-L2b's obligation. The corpus has NO derived statement of how the subtracted response scales with |C|_4 'in either direction'. Not an obstruction — an absence.
- **Source:** `STAGE8_IS_RL2B_FAILURE_FORCED_BY_F5_DETERMINATION_V001.md:97` (SEALED (X.md.seal.sha256))
- **Quote:**   THE CORPUS HAS NO DERIVED STATEMENT OF HOW THE SUBTRACTED RESPONSE SCALES WITH |C|_4
  "IN EITHER DIRECTION." Not an obstruction — an absence.
- **Why it matters:** Bounds the whole campaign: there is nothing to build on, in either direction. The nearest sealed thing (||1_D C 1_D||_2 infinite) is about the UNSUBTRACTED sea kernel; no sealed statement of any restriction of the SUBTRACTED response to a cell was found.

## [DISQUALIFICATION OF RECORD, flagged in two separate determinations] THE SHELL-COUNT LOGARITHMS ARE NOT EVIDENCE ABOUT G_hs — flagged twice so no one assembles them
- **Statement:** The logarithmic divergences (24 H_K + 2 zeta(3); 64 H_K + 16 zeta(3)) are sums over k = LATTICE DISTANCE BETWEEN CELLS. They belong to arm-2's two single-factor failure modes and to NC3's detector role — CROSS-CELL SEPARATION, not the per-cell coincidence object. They are NOT evidence about G_hs at all. The n=1 line carries a different logarithm, coefficient exactly 2/pi at the coincidence end (C1).
- **Source:** `STAGE8_IS_RL2B_FAILURE_FORCED_BY_F5_DETERMINATION_V001.md:165` (SEALED (X.md.seal.sha256))
- **Quote:** THE LOGARITHMIC DIVERGENCES (24 H_K + 2 zeta(3); 64 H_K + 16 zeta(3)) ARE SUMS OVER k =
LATTICE DISTANCE BETWEEN CELLS. They belong to arm-2's two single-factor failure modes and to
NC3's detector role — CROSS-CELL SEPARATION, not the per-cell coincidence object. THEY ARE NOT
EVIDENCE ABOUT G_hs AT ALL.
- **Why it matters:** 'Anyone assembling the shell counts into a forcing argument would be committing the program's characteristic error on the separation-versus-coincidence axis. Flagged so no one does.' It has now been flagged three times.

## [CORRECTION OF RECORD (nothing substantive turns on it)] THE COMMENTARY-VOCABULARY CORRECTION: 'isotropic dilation' is not primary-source language
- **Statement:** 'ISOTROPIC DILATION' occurs ZERO times in the primary source and zero times in E1 v002. The phrase enters via STAGE8_MASTER_PLAN_AMENDMENT_001 §F-2 and the refinement-dependence addendum §4, both downstream commentary. The primary mechanism is stated as DILATION COVARIANCE and RADIUS-INDEPENDENCE.
- **Source:** `STAGE8_IS_RL2B_FAILURE_FORCED_BY_F5_DETERMINATION_V001.md:145` (SEALED (X.md.seal.sha256))
- **Quote:** "ISOTROPIC DILATION" OCCURS ZERO TIMES IN THE PRIMARY SOURCE, AND ZERO TIMES IN E1 v002.
The phrase enters via STAGE8_MASTER_PLAN_AMENDMENT_001 §F-2 and the refinement-dependence
addendum §4, both of which are downstream commentary.
- **Why it matters:** Prevents a lane from searching the primary spec for 'isotropic dilation', finding nothing, and concluding the mechanism is absent — a false-negative-existential trap of exactly the class logged three times.

## [SEALED FINDING, and it is what the transport charter was authored to fix ('THE OBJECT IS NOW WELL-DEFINED').] 'THE COMPLETED RESPONSE ON A SLIVER CELL' NAMED NO QUANTITY BEFORE THE CHARTER
- **Statement:** Pre-charter finding: there is NO shape parameter and NO sealed rule transporting the unit isotropic diamond to a general admitted cell of D3. 'the completed response on a sliver cell' NAMES NO QUANTITY in the sealed corpus. 'IT IS NOT THIS PROOF ROUTE FAILS ... IT IS: THE OBJECT WHOSE INVARIANCE IS SOUGHT IS NOT DEFINED OVER THE CLASS THE INVARIANCE IS QUANTIFIED OVER.' Flag response_on_sliver_cells_defined_in_corpus = false.
- **Source:** `STAGE8_T7_REFINEMENT_DEPENDENCE_ADDENDUM_V001.md:71` (SEALED (X.md.seal.sha256))
- **Quote:** THEREFORE: "the completed response on a sliver cell" NAMES NO QUANTITY in
the sealed corpus. One cannot score a scaling law — or an invariance — for
an object that has not been written down.
- **Why it matters:** Explains WHY the charter was needed and what precisely it bought: definedness, not an estimate. NOTE this file's :58 count ('aspect ratio 0') is a sealed negative existential CONTRADICTED BY ITS OWN DOCUMENT; the §4 conclusion survives on a different ground.

## [NON-CITABLE INDEX. Sealed (STAGE8_LANE_STATUS.md.seal.sha256) but self-declared non-evidence, and known incomplete.] THE REGISTER IS NOT THE AUTHORITY, AND IS ITSELF NON-CITABLE
- **Statement:** STAGE8_LANE_STATUS.md declares itself LIVING and NON-CITABLE: 'No artifact may cite this file as a source.' 'THIS FILE IS NOT EVIDENCE. It is an index. If it and a sealed artifact disagree, THE SEALED ARTIFACT GOVERNS and this file is wrong and must be corrected.' It carries rows R-1..R-15 and has NO ROW for hessian_first_supersession = NOT_CHARTERED. Its snapshot date is 2026-07-26 while it was last modified 2026-07-27 00:27.
- **Source:** `STAGE8_LANE_STATUS.md:21` (SEALED (X.md.seal.sha256) — but self-declared NON-CITABLE)
- **Quote:** THIS FILE IS NOT EVIDENCE. It is an index. If it and a sealed artifact disagree, THE
SEALED ARTIFACT GOVERNS and this file is wrong and must be corrected.
- **Why it matters:** A file can be SEALED and still not be authority. Sealing certifies bytes, not standing. Search the artifacts for what has been ruled.

## [PENDING — bounded negative existential: case-insensitive grep for 'trotter' across all *.md returns 17 hits in 7 files, all pending/naming; no return recorded.] THE TROTTER-KATO REFERRAL HAS NOT RETURNED
- **Statement:** The blind referral — 'Does the sealed successor Galerkin requirement list admit a Trotter-Kato discharge for a nested Hermite family on a Schwartz core?' — is to be sent WITHOUT the conclusion. Every occurrence of 'trotter' in the corpus records it as pending, named, or not-attempted; none records a return, a result, or an answer. F5_ruled_on = false in both the register and the spec amendment.
- **Source:** `STAGE8_RL2B_CONVERGENCE_HYPOTHESIS_RESOLUTION_AND_F5_TRILEMMA_V001.md:222` (SEALED (X.md.seal.sha256))
- **Quote:** 1. REFER TO CODEX BLIND: "Does the sealed successor Galerkin requirement
   list admit a Trotter-Kato discharge for a nested Hermite family on a
   Schwartz core?" A YES makes H1 live and refutes R-L2b's uniformity. Do
   not send this artifact's conclusion with the question.
- **Why it matters:** The single most consequential open item (register: most_consequential_open = O-1). It gates the F'-5 ruling, which gates the trilemma horn, which gates whether R-L2b is satisfiable at all.

## [NUMBERED OBLIGATION, GRANTED into the governing chain; U3_projection_tail_uncertified = true. The declaration it demands has NEVER BEEN MADE anywhere.] U3 IS THE NAMED MINIMAL MISSING INGREDIENT, AND IT IS NOW LOAD-BEARING THREE TIMES
- **Statement:** U3 — the projection-tail / Galerkin-limit obligation — is a TYPING DECISION WITH AN ANALYTIC CONSEQUENCE, and its verdict language must state which of UNIFORM-IN-Q or LIMIT-WITH-CERTIFIED-TAILS the route relies on. It was named as an arm-2 factor-(i) dependency, and two later sealed artifacts find the same finite-carrier-versus-limit typing question to be the pivot of R-L2b as well. It was GRANTED into E1 v002's governing chain (register R-1), which now MAY NOT EXECUTE until each of U1, U2, U3 is either discharged with a witness or explicitly BLOCKED with a witness of blockage.
- **Source:** `STAGE8_RL2B_DIAGONAL_ATTACK_RESULT_V001.md:144` (SEALED (X.md.seal.sha256))
- **Quote:**     *** U3 -- THE PROJECTION-TAIL / GALERKIN-LIMIT OBLIGATION, and its
    verdict-language requirement to state which of UNIFORM-IN-Q or
    LIMIT-WITH-CERTIFIED-TAILS the route relies on. ***
- **Why it matters:** THE SINGLE ITEM THAT UNIFIES THE CAMPAIGN'S BLOCKAGE. It is what Q-support collapses into, what p -> alpha is gated on, and what F'-5's trilemma turns on. The typing decision belongs to the principal.

## [DERIVED (covariance) / NOT DERIVED (determinants). The corpus stops explicitly at the boundary of the extrapolation.] ONE-PARTICLE COVARIANCE CONVERGENCE IS DERIVED — determinant convergence IS NOT
- **Statement:** C_n^(pure) -> P_- STRONGLY, with direct diagonalization agreeing to 1.56e-15 (n=2) and 3.68e-15 (n=4); pure_state_strong_convergence_derived = true. And its own limiting clause: 'Strong convergence of one-particle covariances does not by itself imply convergence of growing-dimensional quasifree determinants'; global_determinant_convergence_derived = false. Also pure_state_sequence_nested = false.
- **Source:** `STAGE8_T7_PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_RESULT_V001.md:41` (HASH-PINNED, NOT SEAL-FILE-SEALED. No adjacent .seal.sha256 in either form and no membership in any *.sha256 manifest; its current sha256 a79939adf1d7185f… is pinned in STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md:30 and in five scripts, and MATCHES current bytes.)
- **Quote:** Strong convergence of one-particle covariances does not by itself imply
convergence of growing-dimensional quasifree determinants.
- **Why it matters:** Cited as 'SEALED' by the trilemma at :34. It is HASH-PINNED. The finding is unaffected; the label should be corrected when cited, and the nested = false flag should be checked against requirement-list item (1) rather than assumed.

## [OPEN. NO IDENTIFIED ROUTE. NOT SHOWN IMPOSSIBLE. NEXT STEP IS THE PRINCIPAL'S.] CAMPAIGN BOTTOM LINE, AS THE CORPUS STATES IT
- **Statement:** R-L2b as posed has NO REMAINING IDENTIFIED ROUTE; the last candidate mechanism is structurally protected; either the object changes or the campaign does; and that is the principal's, not a lane's. But this is NOT a proof that no mechanism exists: 'R-L2b remains open in the ordinary way — hard, unrouted, and not shown impossible.' All campaign gates remain: R_L2b_closed = false; alpha_derived = false; p_known = false; bound_claimed = false; production_authorized = false; alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
- **Source:** `STAGE8_C4_SATURATION_STRUCTURAL_BLIND_ANSWER_V001.md:184` (SEALED (X.md.seal.sha256))
- **Quote:** WHAT FOLLOWS IS THE PRINCIPAL'S. R-L2b as posed has no identified route and
the last candidate mechanism is now known to be structurally protected. Either
the object changes or the campaign does. This lane adopts nothing, proposes
nothing, and notes that the honest form of today's outcome is: THE CAMPAIGN
FOUND WHY IT CANNOT PROCEED, WHICH IS A RESULT AND NOT A FAILURE.
- **Why it matters:** The state to carry forward. Two things must travel together: 'no identified route' and 'not shown impossible'. Reporting either alone misstates the record.


## SEARCHED
CORPUS: /Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003 (3,899 files total; 2,037 .py; 250 .json). READ-ONLY throughout; no writes anywhere.

FILE DISCOVERY. `grep -ril "R-L2b"` -> 39 files, all STAGE8_*.md, all read or targeted-read. `grep -rln "L2b"` -> 40 files. `grep -rln "G_hs"` -> 13 files. `grep -rn "Schatten"` -> 6 files. `grep -rln "arm 2|arm-2|arm_2"` -> 32 files. `grep -rln "sliver"` -> 21 files (70 occurrences). `find -maxdepth 1 -name "*.md" -newermt "2026-07-27 00:00"` -> 24 files, enumerated with timestamps and the four post-12:16 ones read (DISCRIMINATOR_CLAIM_WITHDRAWAL, IBP_SCALAR_WEIGHT, OD3_LEVER, R2_WELL_POSEDNESS + R2_ERRATUM).

READ IN FULL: STAGE8_EXTENSIVITY_VERDICT_AND_RL2B_CAMPAIGN_OPENING_V001.md; STAGE8_RL2B_FRAME_ANSWER_AND_CAMPAIGN_TARGET_V001.md; STAGE8_RL2B_COMMUTATOR_ROUTE_REFUTED_AND_TARGET_SHARPENED_V001.md; STAGE8_RL2B_DIAGONAL_ATTACK_RESULT_V001.md; STAGE8_RL2B_CONVERGENCE_HYPOTHESIS_RESOLUTION_AND_F5_TRILEMMA_V001.md; STAGE8_RL2B_OVER_CHARTER_AND_BLIND_ROUTE_FINDING_V001.md; STAGE8_RL2B_REMAINING_CONTENT_UNDER_THE_CHARTER_V001.md; STAGE8_IS_RL2B_FAILURE_FORCED_BY_F5_DETERMINATION_V001.md; STAGE8_TWO_UNTRIED_MECHANISMS_ATTACK_RESULT_V001.md; STAGE8_P_COINCIDENCE_EXPONENT_DETERMINATION_V001.md; STAGE8_X_TO_KAPPA_RECORD_EXTRACTION_DETERMINATION_V001.md; STAGE8_DISCRIMINATOR_CLAIM_WITHDRAWAL_V001.md; STAGE8_F5_PROVENANCE_ERRATUM_AND_FORCING_GROUND_CORRECTION_V001.md; STAGE8_T7_SLIVER_NATURALITY_ATTEMPT_RESULT_V001.md; STAGE8_TRANSPORT_FUNCTOR_CHARTER_V001.md; STAGE8_T7_ARM2_SHARPENING_AND_PROJECTION_TAIL_BINDING_V001.md; STAGE8_LANE_STATUS.md.

READ IN PART (targeted, with line-numbered extraction): STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md (§R.1 S1-S5 660-730; §R.3 800-900; C1/C2/C4/C6 315-365; D5' 425-445; §O.A0 491-575; obligations 1010-1025; §V 1782-1795; missing-object table 1858-1876; PA-2b 1940-1955); STAGE8_WARD_IDENTITY_QUESTION_BLIND_ANSWER_V001.md (120-211); STAGE8_C4_SATURATION_STRUCTURAL_BLIND_ANSWER_V001.md (150-220); STAGE8_EXTENSIVITY_QUESTION_BLIND_ANSWER_V001.md (80-175); STAGE8_T7_CODEX_BATTERY_TIER2_RETURNS_V001.md (84-135); STAGE8_KAPPA_RULE_ADOPTION_STAGE12_ERRATUM_AND_D1_D2_D3_RETURNS_V001.md (85-130); STAGE8_BRIDGE_DECAY_DETERMINATION_V001.md (1-140); STAGE8_TRANSPORT_ROLE_GRID_SECOND_DIMENSION_V001.md (130-200); STAGE8_R2_WELL_POSEDNESS_AND_INPUT_SEAL_DETERMINATION_V001.md (1-60, 140-180, 210-270); STAGE8_R2_DETERMINATION_ERRATUM_001_R1_RULING_REACH.md (100-135, 236-300, 340-370); STAGE8_OD3_LEVER_DETERMINATION_V001.md (70-120); STAGE8_ROUTE2_RATIFICATION_AND_FRAMING_CORRECTION_V001.md (100-185); STAGE8_TRANSPORT_CHARTER_OPTIONS_WITH_COSTS_V001.md (218-250); STAGE8_T7_REFINEMENT_DEPENDENCE_ADDENDUM_V001.md (55-100); STAGE8_MASTER_PLAN_AMENDMENT_001.md (48-76); STAGE8_T7_E1_SPEC_V002_AMENDMENT_001.md (118-200); STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001.md (14-60); STAGE8_T7_PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_RESULT_V001.md (25-58); STAGE8_T7_CONNECTED_LINKED_CLUSTER_MAJORANT_DERIVATION_SPEC_V001.md (D5 188-198); STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V001.md (grep only).

SEAL VERIFICATION (all three forms tested per the discipline, plus manifest membership). For 34 named artifacts I tested X.seal.sha256, X.md.seal.sha256, AND `grep -rl <basename> --include="*.sha256"`. 351 *.seal.sha256 files exist at corpus root; multi-line seal manifests confirmed present (e.g. FORK_8_CAUSAL_DIRECT_LIMIT_PROMOTION_V001.seal.sha256, 10 lines). All 32 R-L2b-campaign artifacts carry the X.md.seal.sha256 form. One seal hash recomputed and matched byte-for-byte (STAGE8_RL2B_REMAINING_CONTENT_UNDER_THE_CHARTER_V001.md -> 99da8628c1f6ef1d…). Two cited artifacts carry NO seal in any of the three forms and were traced to hash pins instead (see items 40 and 62).

NEGATIVE EXISTENTIALS I RAN MYSELF, stated narrowly: (a) literal 'L2b' OR 'G_hs' OR 'SCAD_HS' across all *.py and *.json excluding vendored/sympy -> ZERO files; (b) case-insensitive 'trotter' across all *.md -> 17 hits in 7 files, none recording a return; (c) 'supersed*' co-occurring with 'sliver' or 'naturality' -> only the single adjudication clause in REMAINING_CONTENT and its flag; (d) 'two orders' / 'orders 1 and 2' / 'first two orders' across *.md -> 3 hits, 2 of them the R2 well-posedness artifact; (e) 'LARGELY INDEPENDENT' -> 3 hits, primary at KAPPA_RULE:98.

TIMESTAMPS recomputed with `stat -f %Sm` for the 15 campaign-relevant artifacts to adjudicate the pre/post-charter supersession claim (sliver 2026-07-26 13:42:41; charter 15:32:20 — confirms the corpus's own figures).

## SELF-DECLARED GAPS
WHAT THIS SWEEP COULD NOT ESTABLISH, and why.

1. THE INDEPENDENT LANE'S PRIMARY R-L2b SLIVER RETURN IS NOT IN THIS CORPUS. Three artifacts refer to "the independent lane's report that the bound class fails in the sliver direction" and "the independent lane's R-L2b return stands", but every occurrence is a RELAY — a re-statement inside a construction-lane artifact. I found no artifact authored by the independent lane stating that return, and the sliver observation as recorded (SLIVER_NATURALITY:102-110) is attributed to "one lane made the point sharply". So the sliver failure's PROVENANCE is a relay, not a sealed derivation available for inspection. I did not search outside the cleanroom directory.

2. I DID NOT VERIFY THE PARENT AND PHASE-A ARTIFACTS AT SOURCE. Statements attributed by hash to BID_MONOIDAL_EXTENSIVITY_DERIVATION_V001 (451550c3, Theorems 1/2/3 and the five conditions), Phase-A A1/A2 (789338ad), the Hermite-Galerkin baseline spec (80aa4e17), MAJORANT_LEMMA0_PROOF_DRAFT_V001 (679ba036), V011, and FINITE_PARENT_ANALYTIC_AUTHORITY_V001 were taken from the quoting artifacts. I verified the parent majorant spec's D5 and scoping clause 1 directly, and the E1 v002 spec throughout, but not the rest. A lane relying on Theorem 3's five conditions verbatim should open 451550c3 itself.

3. SEAL-STATUS OF THE TWO HASH-PINNED FILES IS REPORTED, NOT ADJUDICATED. STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001.md and STAGE8_T7_PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_RESULT_V001.md carry no seal file in any of the three forms and no manifest membership; their content hashes are pinned in a sealed spec and in five scripts and MATCH current bytes. Whether "hash-pinned in a sealed authority table" counts as sealed in this program's convention is a question the corpus answers inconsistently — the R2 determination coins "UNSEALED-ADJACENT but HASH-PINNED, DISCLOSED AS SUCH, and EXPRESSLY CLEARED for pinned use by a sealed carve-out" for a different file. I report the measurement and decline the adjudication. This is NOT a claim that those artifacts are unsealed in the sense that would invalidate them.

4. I DID NOT ADJUDICATE THE PA-2b TENSION. The spec carries a frozen, non-revisable prediction that R-L2b returns alpha = 1/2; the campaign's aggregation arithmetic says D5 requires alpha >= 1 and that alpha = 1/2 would be an area law. No artifact reconciles them. Both are recorded; neither is a derivation; I have not decided which the record favours, and doing so would require the exponent the whole campaign is missing.

5. THE "THIRD ERRATUM" HAZARD: I did not re-verify the sealed counts inside the artifacts I quote. The F'-5 provenance erratum found one sealed negative existential ("aspect ratio: 0") contradicted three times by its own file, and the p-determination found "seven closed mechanisms" to be a count of list entries rather than closures. Other counts inside these artifacts may be similarly wrong. Where a count is load-bearing in this briefing I have flagged it (the seven-vs-five ledger; the "at most 1" ceiling; "the five" denoting two sets).

6. NOTHING WAS COMPUTED. No value of alpha (the S2 exponent), no p, no kappa_record, no kappa_Thomson, no function of them, and no 1/(4*pi*kappa). No route was constructed and no gap was filled. Where a text supplies a conditional (p > 3/2 -> alpha = 1), I report the conditional and its self-applied POWER-COUNTING label; I did not evaluate either side.

7. SIX ARTIFACTS THAT MENTION R-L2b OR ARM 2 WERE NOT OPENED and could carry material this briefing misses: STAGE8_APPARATUS_PROVENANCE_DETERMINATION_V001.md, STAGE8_APPARATUS_PROVENANCE_ERRATUM_001.md, STAGE8_COMPLETION_PLAN_PROPOSAL_V001.md, STAGE8_MASTER_PLAN_FINDINGS_V001.md, STAGE8_STEP_LIST_AND_DOWNSTREAM_STAGE_FINDING_V001.md, STAGE8_V010_SATURATION_IDENTIFICATION_BLIND_ANSWER_V001.md. They were grepped for R-L2b/G_hs and their hits were incidental or already covered, but I did not read them end to end. The corpus's own logged error class is precisely the false negative from an under-searched file — logged three times — so this is stated as an unclosed gap and not as an absence.

8. O-D1 AND O-D3 WERE NOT SWEPT. The combinatorial residue of the sliver relocation lives in the charter's own obligations, and the OD3 lever determination records "O-D3 ... UNTOUCHED". I confirmed the obligations exist and are open; I did not assemble their state.
