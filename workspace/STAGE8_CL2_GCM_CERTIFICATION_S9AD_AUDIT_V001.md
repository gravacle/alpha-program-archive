# STAGE 8 — ADVERSARIAL AUDIT OF THE C-L2/G_cm CERTIFICATION

## INDEPENDENT AUDITOR — CODENAME CL2-AUDIT — [SEALED]

Date: 2026-08-14
Commission: independent adversarial audit of
`STAGE8_CL2_GCM_CERTIFICATION_S9AD_V001.md` (seal e6838ffc, verified §2).
Default posture REFUTE; this verdict governs. The auditor did not write the
build and was not told its verdict before the pre-commit notes were hashed.

Gates, LIVE THROUGHOUT: `alpha_computed = false` ; `proof_authorized = false` ;
`kappa_record_computed = false`. EXACT SYMBOLIC ONLY (sympy 1.14.0, fresh venv
`cl2audit_venv`, scripts + output reproduced §7); no floats as ground, no
measured constants, no value frozen. No file matching register|road_|ledger|
lens|plan|tracker|THE_HANDOFF opened ("register" filename matches were listed
by sweep, never opened; fenced enumeration displayed §5.3). "Q-..." tokens
EXPECTED-UNLOCATABLE, noted not chased. No git; nothing registered/committed/
pushed; no existing file edited. Output path probed ABSENT at session start
AND re-probed immediately before write.

---

## 0. VERDICT IN ONE LINE

**CONFIRMED-WITH-CORRECTIONS. The certified core survives the full attack: the
anticommutator flip [h_0, M⊗S] = Σ_j {p_j, M} ⊗ α_j S is exact (re-derived
independently, entrywise, rep-independent); the form bound
|⟨ψ,[h_0,M(t)⊗S]ψ⟩| <= 2√3·||h_0ψ||·||ψ|| on D(h_0) with relative form bound
ZERO w.r.t. h_0² is correct with every constant exact and every quantifier
(state, t, cell, carrier, eps) honestly displayed; no operator-norm step is
smuggled (the only operator norms taken are of the BOUNDED vertex and the
unit spinor matrices — never of the commutator); sharp M(t) untouched; the
build's CAS re-ran verbatim 19/19 PASS byte-identically. The negative verdicts
are also correct and conservative at bytes: (o4)/G_cm NOT discharged
(beta symbolic u-1; form→HS grade gap real — B-L2* FAILS-AT confirmed at
6e81ae92 :32 / 2699af25 :23; F1 ceiling at WALL :401-407), wall F3 NOT
unblocked (held to the sealed conditional and no stronger), R-L0 untouched
(u-1/u-2/u-4 verbatim), witness E1_RECORD_KINK_COMMUTATOR_FORM_UNCERTIFIED
STANDS, retirement left to the registrar, V-clauses untouched. SIX CORRECTIONS,
none verdict-bearing, two substantive: (COR-1) the build consumed CL-ERROR
without its check — STAGE8_CL_ERROR_CHECK_V001.md (b4a55baa), invisible to the
build's too-narrow sweep pattern, REFUTED CL-ERROR's headline NET verdict while
CONFIRMING (OBJECT_FIDELITY) exactly the displays the build consumed; the
registrar must consume CL-ERROR at OBJECT_FIDELITY grade only; (COR-2) §3.4(i)
calls (α·n̂₀ ⊗ S) "the Hermitian unitary" — it is ANTI-Hermitian and squares
to −I (no +1 eigenspace exists; CAS A1a/A1b); the exhibit repairs in one line
with i(α·n̂₀)S (Hermitian unitary, CAS A1c) and the exclusion conclusion is
independently of record (E1 :1139-1141), so (o3) stands.**

---

## 1. INDEPENDENCE DISCLOSURE, WITH HASHES

Per the mandated protocol, sub-tasks (1)-(3) were worked and FIXED — including
the auditor's own verdict-grade answer and a conditional verdict map — in
hashed scratchpad notes BEFORE the build was opened. The build was then read
ONCE in full and attacked at bytes.

```text
PRE-COMMIT NOTES (written and hashed before the build was opened):
676b6adf8095885cf8549e9460c5f7f3e951312ad720f5eaa3b47dc860ab09fc  CL2_AUDIT_PRECOMMIT_NOTES.md
cb274009308335f830ca179434bf371b2625b6be9343e8d40c0b6a49a198e537  cl2_audit_independent_battery.py
59fa18d9b7af2a2c4fc6c2342b02633ee0ffef3ff748ff1cef5bef7a4bd306b2  cl2_audit_battery_fixes.py
(all under the session scratchpad
/private/tmp/claude-501/-Users-bgm/9ad117f3-207c-44de-9a15-f000de50d726/scratchpad/)

FIXED IN THE NOTES BEFORE OPENING, verbatim summary:
(1) my own certification pass: the commutator is the boundary form
    i∮ ψ†((α·n̂)S)ψ dS; certifiable as a quadratic form (trace/Besov endpoint
    B^{1/2}_{2,1}; H^{1/2} fails; exact algebraic constant); operator-norm and
    HS routes genuinely excluded; the DOMAIN EDGE fixed in advance: R.3's
    consuming site is HS-typed and a form bound does not deliver it — any
    "G_cm valued/consumable" claim must have smuggled a conversion; beta a
    symbol until R-L2b regardless.
(2) corpus pieces fixed: CL-ERROR (3b9730e0) symbol-level only; kappa_n
    (3b5e95b6) HS-divergent; no prior form certification exists; a refusal
    would be wrong.
(3) quantifier list fixed: form-domain, t (tips), D3 cell class, carrier
    n-uniformity, branch/CTP weights.
VERDICT MAP FIXED: scoped-form-certification claim -> CONFIRMED or
CONFIRMED-WITH-CORRECTIONS; G_cm-valued / F3-retired / witness-retired
claim -> REFUTED-AT; refusal -> REFUTED-AT; H^{1/2}-exact-domain claim ->
REFUTED-AT. THE BUILD LANDED IN THE FIRST BRANCH; the verdict above follows
the map as fixed, after the attack failed to break the certified core.
```

The auditor's independent route (Besov boundary-trace) and the build's route
(h_0-relative form via the anticommutator flip) differ; on D(h_0) the build's
is equivalent-or-stronger (H¹ ⊂ the Besov trace domain), and the C-L2 clause
assigns the WHICH-form naming act to the artifact (E1 :1141-1143). The build's
flip route avoids trace-constant machinery entirely and is r-independent —
cleaner than the pre-committed route at the tips. Judged admissible and
superior; no deduction.

---

## 2. SEAL TABLE — EVERY DIGEST RECOMPUTED FROM BYTES AT PATH THIS SESSION

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`. Method:
`shasum -a 256` at path; sidecar read and compared. None unverifiable.

```text
BUILD UNDER AUDIT:
e6838ffcc6f352b7a0cfaad1d51d98544717d3bbe04d413d8b356e752d400a3d  STAGE8_CL2_GCM_CERTIFICATION_S9AD_V001.md            MATCH sidecar
SEED STOCK (tasked prefixes all MATCH):
468467303a109dc825b015107897dacc107800fc981030377c3f006b384cccb5  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md           MATCH (46846730)
a903716c23c1a6969932e988f90d464abe9e8ee96624cd2dce3e32416de132e0  STAGE8_RL4_RL0_CERTIFICATION_V001.md                  MATCH (a903716c)
685afac8205b4ed2ed0a309a321f6eccc940882e89ec3dfbce70fd9b8d74af52  STAGE8_RL4_RL0_CHECK_V001.md                          MATCH (685afac8)
80db260fa1561d76296d5f54e1e52397b79009b8a0d12bc060c140818c38fdf7  STAGE8_WALL_BOUNDARY_CLOSURE_S9AD_V001.md             MATCH (80db260f)
46938251aeaa9af3541633691ecdd9f5939508e70bffbc43034b589c4945fa63  STAGE8_WALL_BOUNDARY_CLOSURE_S9AD_AUDIT_V001.md       MATCH (46938251)
LINEAGE/PINNED STOCK OPENED BY THIS AUDIT (sidecars all MATCH):
789338adb7d3d36da453113e98f371a4f92543cf2652b047f8481c407bed5bc3  STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md  MATCH (E1 :82 pin)
3b9730e0ce585c524a6ac27d3368f29535a0bbffe84e1ec8313cc861011acb7a  STAGE8_CL_ERROR_CERTIFICATION_V001.md                 MATCH
b4a55baa5cb46de474be6e03c7fbdea728118c38ebc24529c34ae4b77e184bad  STAGE8_CL_ERROR_CHECK_V001.md                         MATCH  [NOT in build's stock — COR-1]
6e81ae92b32fa34691396102ef79f1fdfcb8c15101a44d9206aeeded599a5027  STAGE8_BL2STAR_ATTEMPT_V001.md                        MATCH
2699af259750e2cae9afcb4d5a9487edd543c91a13db7c8f49a8fed1f3d9e24c  STAGE8_BL2STAR_CHECK_V001.md                          MATCH
3b5e95b6*                                                         STAGE8_R2_KAPPA_N_DETERMINATION_S9AD_V001.md          MATCH (wall CS-3 pin resolved)
efb08860b888e24acaa50fdafdbe4afdb868450f79ec23120c2bd3eb1d40ddbb  STAGE8_CL1_ATTEMPT_RESULT_REFUTED_V001.md             MATCH  [standing-stock probe, §4.6]
tau_R derivation (b786db3a): NO_SEAL_FILE carve-out B of record (E1 :88) —
consumed only through E1's sealed displays, same as the build. Not opened.
```

---

## 3. THE AUDITOR'S INDEPENDENT PASSES (fixed before the build was opened)

Full content in the hashed pre-commit notes (§1); results, all exact:

```text
P-1 OBJECT: [h_0, 1_B ⊗ S] = i((α·n̂)S)·delta_{∂B_r} as a form; pointwise
    contraction |ψ†((α·n̂)S)φ| <= |ψ||φ| ((α·n̂)² = I, S² = I, I2a/I3a);
    distributional ground verified on explicit radial f (I4a'-poly/exp).
P-2 CERTIFIABILITY: YES, as a quadratic form — trace endpoint B^{1/2}_{2,1}
    (H^{1/2} FAILS: matched-weight model mass 1/log2 finite vs trace mass
    +infinity, I8a'/I8b'); operator route excluded (concentration family,
    form value/||ψ||² = (3/2)/eps → ∞, I6b); HS route excluded (I7a; C6).
P-3 COLLAPSE BOOKKEEPING re-derived blind: coverage window [ρ, 1−ρ], phase
    = tau_R(1−16ρ⁴) (I5a), C4 second difference ⇒ deficit cos²(8πρ⁴) (I5b)
    — matching CL-ERROR's g EXACTLY, before either CL-ERROR's §2.2 details
    or the build were consulted on it.
P-4 THE DOMAIN EDGE, fixed in advance: form grade does not convert to R.3's
    HS-typed slot; beta symbolic until R-L2b; H-R and u-4 stand regardless;
    F3's consuming grade is trace/HS. (The build's §3.5/(d-1..3), §4, §5
    subsequently matched this point for point.)
P-5 Threshold/weight algebra re-verified: W(1/2) root unique (I9b'),
    S_± = ±1/2, kappa_bal = 1 arithmetic (I10), |C|_4 = π/24 (I11b),
    surface-pairing scaling weight L^{−1} exact (I11a).
```

---

## 4. THE ATTACK — EVERY CLAIMED STEP RE-DERIVED AT BYTES

### 4.1 The certified chain (build §3.2) — HOLDS

```text
a-1 FLIP: [h_0, M⊗S] = Σ_j (p_jM)⊗(α_jS) − (Mp_j)⊗(Sα_j); {S,α_j} = 0 ⇒
    Sα_j = −α_jS ⇒ = Σ_j {p_j,M}⊗α_jS. Re-derived by hand; build CAS B2
    verifies it entrywise over noncommutative symbols; rep-independent
    (needs only the algebra, not the C⁴ rep). EXACT. The sharp indicator's
    derivative never appears — no smoothing, no surface delta in the
    certified route. D6' respected.
a-2 FACTOR 2: ⟨φ,(p_jM⊗α_jS)ψ⟩ = ⟨p_jφ,(M⊗α_jS)ψ⟩ (p_j self-adjoint,
    φ ∈ H¹); ⟨φ,(Mp_j⊗α_jS)ψ⟩ bounded by ||φ||·||p_jψ|| (||M|| <= 1,
    ||α_jS|| = 1 unitary, B1e). Sum: |q_t(ψ)| <= 2Σ_j||p_jψ||·||ψ||. HOLDS.
a-3 √3 CONSOLIDATION: needs h_0² = Σ_j p_j²⊗I — cross terms cancel by
    {α_i,α_j} = 2δ_ij AND [p_i,p_j] = 0; verified entrywise with
    noncommuting momenta then symmetrized (audit A3); Cauchy-Schwarz
    (Σa_j)² <= 3Σa_j² (A2a'). CONTINUUM-EXACT — and the build correctly
    scopes it: at finite carrier only the primitive display stands (u-c),
    compressed momenta need not commute. Honest.
a-4 EPS-SPLIT: perfect-square witness exact (A2b = build B4). Relative form
    bound ZERO w.r.t. h_0² — correct KLMN-type statement.
a-5 CONSTANTS: ∫v = tau_R (B6a = my I1); Σ|w||λ| = √2/2 (B6d); the weighted
    one-insertion constant 2√3·tau_R·√2/2 = π√3 EXACT (audit A4); D(t)'s
    time factor t exact (A5); |C|_4 = π/24 cross-check (B6b = my I11b).
    All in the R.1 alphabet (E1 :684-687), no cellulation datum, no float.
a-6 SMUGGLE SCAN: the only ||·||_op taken anywhere in the certified chain
    are ||M|| <= 1 (bounded vertex) and ||α_jS|| = 1 (spinor matrix) —
    never the commutator. NO operator-norm step smuggled. NO equal-time HS
    object resurrected. NO domain quietly assumed (D(h_0) named; §4.4).
```

### 4.2 The build's CAS — verbatim re-run + audit battery

Build script extracted byte-for-byte (sha256 c9e930ec…) and re-run in the
fresh audit venv: **19/19 PASS, output byte-identical to §7.2 of the build.**
Audit's own batteries: pre-commit 21 PASS + 5 script-level FAILs each repaired
to PASS (6/6; sympy Abs/LambertW/unevaluated-integral handling, §7 note);
attack battery 8 PASS + 1 auditor-side witness-coefficient slip repaired to
PASS (A2a'). NO mathematical check of either side failed after script repair.

### 4.3 Quantifier honesty — VERIFIED

The five quantifiers fixed in the pre-commit notes are all displayed at the
build's certified statement (§3.2 u-a..u-d, §5): state ∀ψ ∈ D(h_0) (dense,
not L² — and the build says the form does NOT extend to L², §3.4(i)); t
uniform including tips (bound r-independent); cell ∀ admitted D3 cells (pure
number, no cellulation datum — E1 :679-687 order-of-quantification respected);
carrier honestly SPLIT (primitive display at every (n,ℓ); consolidation
continuum-only); eps ∀ > 0. The certified domain D(h_0) = H¹ is a proper
subset of the maximal Besov form domain — checked against every consuming
display cited tonight: none demands more than H¹ states. No gap.

### 4.4 The negative verdicts — VERIFIED AT BYTES, AND CONSERVATIVE

```text
n-1 (o4)/G_cm: R.3's consuming site is HS-typed at E1 :811-814 (verbatim
    re-read); u-1/u-2/u-3/u-4 verbatim at RL0 :377-391; R-L2b owns beta
    (E1 :826-832, "State the same for beta and G_cm"); B-L2* FAILS-AT
    stands at 6e81ae92 :32 with check CONFIRMED at 2699af25 :23 (both
    re-read at bytes); F1 = rank×op ceiling at WALL :401-407; kappa_n
    divergent at WALL :231-233. The form→HS distance (d-1)-(d-3) is real
    and exactly matches the auditor's pre-committed P-4. G_cm =
    NOT-DERIVABLE-TODAY is CORRECT, and b-3's both-directions guard
    (a certified G_cm still would not make x derivable) is exactly right.
n-2 WALL F3: the commission's consumable conditional ("certifying C-L2
    unblocks F3") is answered honestly: tonight's layer is form-grade, F3's
    consuming site (single-composite majorant, stay strata) is trace/HS-
    grade, the conversion is F1's own proved ceiling. NOT unblocked; the
    "tightens WHAT the modulo-layer is" claim is marked conditional on
    registration. NO STRONGER reading anywhere in the build. F1 and F2
    stops stand independently — the build never touches them.
n-3 WITNESS: stands; retirement/split explicitly the registrar's; nothing
    retired, nothing created (every failure point already carries its
    witness of record — verified: no new witness token in the build).
n-4 V-CLAUSES/GATES/FENCES: flag block re-checked line by line — gates
    false throughout, no n >= 2 claim, no threshold claim, sharp M(t)
    untouched, S3/G_bl untouched, kappa_bal display uncited, no Phase-1
    (K_sea, T_R, b_0) consumption. CLEAN.
```

### 4.5 S2b's type ambiguity (build ch-5) — CORRECTLY CARRIED

S2b's parenthetical is form-typed at its own bytes (E1 :702-708 names the
error AS "[h_0, M(t) ⊗ S]" and demands the bound "in the quadratic form C-L2
names"); R.3's derivation display consumes ||A(0)||_2 (E1 :811-814). The build
carries both readings without repairing the clause — the correct posture; the
ambiguity belongs to the spec author/registrar. Under the literal S2b reading
the ingredient now exists at the generator level; under the R.3 reading it
does not. The build says exactly this and no more.

### 4.6 Standing-stock probes beyond the build's stock

```text
s-1 STAGE8_CL_ERROR_CHECK_V001.md (b4a55baa): NET_VERDICT = REFUTED of
    CL-ERROR's headline (the SPLIT/no-opposite-component claim fails at
    insertion order n = 2 — E_int's phase-free S·S = I channel carries a
    degree-0 intraband part; correct verdict UNDECIDABLE-AT the E_int
    resummation). BUT OBJECT_FIDELITY = CONFIRMED: E = E_prof + E_int
    exact; E_prof = (g−1)1_ball⊗I with g = cos²(8π|x|⁴) re-derived by hand
    and CAS; the D-kernel exact; the flip re-derived by hand. THE BUILD
    CONSUMED ONLY THE CONFIRMED LAYER (§2.2 displays + the J3 flip ground,
    itself re-proved in-build as B2). No contamination — but see COR-1.
s-2 STAGE8_CL1_ATTEMPT_RESULT_REFUTED_V001.md (efb08860): "C-L1 FALSE AS
    WRITTEN — there is no ball where the collapse is exact" (the collapse
    holds only at ρ = 0; the deficit is exactly E_prof's g < 1 off-center,
    independently re-derived by this audit, P-3). CHECKED: the build never
    asserts the errorless collapse; it certifies the ERROR layer's
    generator, which this refutation makes MORE central, not less. No
    contamination.
s-3 Wider audit sweep (pattern C-L2|G_cm|KINK_COMMUTATOR, both roots, minus
    fenced classes) re-run: NO file outside the build's stock contains a
    certification display for the commutator form. The build's refusal
    hunt-space was complete in the material direction; the only relevant
    missed file is the CHECK in s-1 (COR-1/COR-3).
```

---

## 5. CORRECTIONS (none verdict-bearing; COR-1 and COR-2 substantive)

### 5.1 COR-1 — CONSUMED ARTIFACT'S CHECK NOT OPENED (provenance)

The build's sweep pattern `G_cm|RECORD_KINK_COMMUTATOR` cannot match
STAGE8_CL_ERROR_CHECK_V001.md, so the check of the very artifact the build
consumed never surfaced. The check REFUTES CL-ERROR's NET verdict while
CONFIRMING the consumed displays (§4.6 s-1). Consequences: (i) the build's
§2.2 phrase "the sealed CL-ERROR decomposition ... exact at the sealed-display
level" is TRUE but under-documented — the registrar must consume CL-ERROR at
OBJECT_FIDELITY grade only, never its headline; (ii) the §2.2 display
inherits, unacknowledged, the check's o4 bookkeeping note: the literal
E := U(0) − P accounting is phase-stripped (the free-factor (e^{−ih_0}−1)P
piece is a common unitary in the pairing — harmless, per the check, but it
should be carried). NOT verdict-bearing: the flip is independently proved
in-build (B2) and by this audit; E_prof/Theta re-derived three ways (build
B9, check by hand, audit I5 blind).

### 5.2 COR-2 — HERMITICITY SLIP IN THE EXCLUSION EXHIBIT (§3.4(i))

"(α·n̂₀ ⊗ S)" is called "the Hermitian unitary". FALSE: {S, α_j} = 0 makes
((α·n̂)S)† = −(α·n̂)S (anti-Hermitian) and ((α·n̂)S)² = −I — it has NO +1
eigenspace (CAS A1a/A1b, exact, symbolic unit n̂). REPAIR (one line): choose
the spinor in the +1 eigenspace of i(α·n̂₀)S, which IS Hermitian unitary
(squares to +I; CAS A1c); the cap pairing is then bounded below by c|ψ|² and
the divergence argument runs verbatim (the build's B1e proved unitarity only —
the Hermiticity claim was never CAS-covered; the gap in its own battery is the
detection surface). NOT verdict-bearing: (o3)'s conclusion is independently of
record (E1 :1139-1141), the L²-mass/trace-divergence arithmetic (B8a-c) is
correct, and the repaired exhibit is exact.

### 5.3 COR-3 — SWEEP COUNTS WRONG (material exhaustiveness HOLDS)

At the build's own timestamp the fenced class was SIX files, not four
(THE_HANDOFF ×2 created 05:06 same day, build written 18:57; plus REGISTER ×2,
ROAD ×2 — filenames listed by sweep only, never opened by either party), and
the non-fenced pattern-hit count is 41, not 43: PA and WALL-AUDIT, listed
under "CONSUMED AT BYTES (9)", do not contain the swept tokens. 41 + 6 = 47 ✓
(the build's total). This audit enumerated all 41 and confirmed every one is
classed in the build's scheme and none contains a certification display —
the EXHAUSTIVENESS CLAIM survives in the direction that matters; the printed
arithmetic does not.

### 5.4 COR-4 — SYSTEMATIC BYTE-PIN DRIFT (content attribution correct)

```text
build "F1 (WALL :408-413)"  -> actual F1 = :401-407 (:408-413 is F2's span)
build "F3 (WALL :414-419)"  -> actual :415-420 (quote drops F3's witness line)
build "E1 :810-813"          -> actual :811-814
build "RL0 ... :360-375"     -> actual ≈ :358-371
```
Every quoted text was re-read at bytes and is verbatim-correct; every
attribution (F1 = rank×op ceiling, F3 = error-term step) is to the right
object. Registrar should re-pin on splice.

### 5.5 COR-5 — DEFINITIONAL DISPLAY OF THE FORM (cosmetic)

§3.1's `q_t(ψ) := ⟨ψ, [h_0, M(t)⊗S]ψ⟩` on D(h_0) parses only in H¹–H^{−1}
duality (sharp M ⇒ (M⊗S)ψ ∉ D(h_0); the literal operator composition leaves
L²). The operative definition is Step 2's derivative-placed bilinear display —
which the build supplies and the bound is proved on — but it is not NAMED as
the definition; and Step 2's middle line garbles the tensor slots
("α_j S ⊗ p_j"). The inequality chain is unaffected (re-derived §4.1 a-2).

### 5.6 COR-6 — CARRIER TENSOR-FACTOR BYTE (u-c)

(u-c) writes the carrier as "H_(n,ell) ⊗ C⁴"; PA :69 gives spinor dimension 32
for the executed n = 2 member. The flip needs only {S, α_j} = 0 and the
spatial/spinor tensor split (PA :79-80), both rep-independent, so the
primitive display survives at every sealed carrier — but the C⁴ byte is not
PA's and should read "the carrier's spinor factor".

---

## 6. CHOICE LEDGER (auditor's)

```text
L-1 PRE-COMMIT PROTOCOL: answers + conditional verdict map fixed and hashed
    before the build was opened (hashes §1). Tag: PROVABLE (process,
    hash-attested).
L-2 VERDICT SELECTION: CONFIRMED-WITH-CORRECTIONS, not REFUTED-AT — because
    the certified inequality survived every attack lane (flip, factor 2,
    consolidation, eps-split, quantifiers, smuggle scan, CAS verbatim), and
    both substantive corrections leave their host claims standing on
    independent ground (COR-1: displays check-confirmed + re-proved;
    COR-2: conclusion of record + one-line repair). Under the pre-committed
    map this is the first branch. Tag: YOURS, grounds displayed.
L-3 STOCK BEYOND THE COMMISSION: CL_ERROR_CHECK, CL1_ATTEMPT_REFUTED,
    kappa_n determination opened (attack priorities 2 and 5; sidecars
    verified §2). Tag: YOURS (inclusion), each consumption displayed.
L-4 ROUTE COMPARISON: the pre-committed Besov-trace route vs the build's
    h_0-relative route judged equivalent-or-stronger on D(h_0); the clause
    assigns the naming act to the artifact. Tag: PROVABLE.
L-5 WIDER SWEEP PATTERN (C-L2|G_cm|KINK_COMMUTATOR) run against the build's
    narrower one; the diff (the CHECK file) is COR-1's detection. Tag:
    PROVABLE (displayed §4.6 s-3, §5.3).
L-6 MY OWN BATTERY SLIPS DISCLOSED: 5 pre-commit + 1 attack script-level
    FAILs, each repaired and re-run to PASS (I4a', I6a', I8a'/b', I9b',
    A2a'); all were sympy-handling issues, none mathematical. Tag: YOURS
    (disclosure), PROVABLE (repairs displayed in scripts).
```

## 7. TOY_SEPARATION (auditor's)

```text
T-1 1-D endpoint/trace models (I6 tent family, I8 matched-weight H^{1/2}
    failure) and the build's B7 1-D FTC check: MECHANISM DISPLAYS ONLY.
    No 3-D conclusion of this audit rests on them; the 3-D chain is §4.1
    (A1-A4, I2/I3, B1-B5), all exact and 3-D.
T-2 B9/I5 rational sample points inside piecewise reductions: consistency
    reproductions of closed forms, not grounds.
T-3 No numeric evaluation anywhere; every constant exact symbolic
    (2√3, π√3, √2/2, tau_R = π/√2, π/24, W(1/2), 1/log2).
T-4 Scripts and venv: cl2audit_venv (fresh, sympy 1.14.0); audit scripts
    hashed §1 and cl2_audit_attack_battery.py = 29d3e7de…,
    cl2_audit_attack_fix.py = 92bcb641…; build script extracted verbatim =
    c9e930ec…, re-run output byte-identical 19/19 PASS.
```

---

```text
FLAG BLOCK — STAGE8_CL2_GCM_CERTIFICATION_S9AD_AUDIT_V001
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
AUDIT_VERDICT = CONFIRMED-WITH-CORRECTIONS
INDEPENDENCE = pre-commit notes + own verdict map hashed BEFORE build opened
    (676b6adf…, cb274009…, 59fa18d9…); build read once in full afterward
BUILD_SEAL_VERIFIED = e6838ffc… MATCH at path
CERTIFIED_CORE = HOLDS( flip exact; 2√3 bound + zero relative form bound
    correct on D(h_0); quantifiers honest; constants exact and in-alphabet;
    no operator-norm smuggle; sharp M(t) untouched; build CAS verbatim re-run
    19/19 PASS byte-identical; audit batteries pass after disclosed
    script-level repairs )
NEGATIVE_VERDICTS = CORRECT-AND-CONSERVATIVE( (o4)/G_cm blocked at
    d-1/d-2/d-3 verified at bytes; G_cm NOT-DERIVABLE-TODAY; WALL F3 NOT
    unblocked, held to the sealed conditional and NO STRONGER; R-L0
    u-1/u-2/u-4 stand verbatim )
CORRECTIONS = 6( COR-1 CL-ERROR consumed without its check b4a55baa — check
    REFUTES its headline, CONFIRMS the consumed displays; consume at
    OBJECT_FIDELITY grade only; COR-2 §3.4(i) "(α·n̂₀⊗S) Hermitian" false —
    anti-Hermitian, squares to −I; repair = i(α·n̂₀)S; conclusion stands of
    record; COR-3 sweep counts 4/43 wrong, actual 6/41, material
    exhaustiveness holds; COR-4 byte-pin drift F1/F3/E1/RL0, content
    attribution correct; COR-5 form-definition display parses only as
    duality, operative definition unnamed; COR-6 carrier "C⁴" byte vs PA's
    spinor dimension 32 — flip rep-independent, display survives )
NONE_VERDICT_BEARING = true
WITNESS E1_RECORD_KINK_COMMUTATOR_FORM_UNCERTIFIED = STANDS (per the build;
    audit concurs; retirement/split is the REGISTRAR'S, and per COR-1 any
    split decision should also record CL-ERROR's check-status)
witnesses_retired_here = none ; witnesses_created_here = none
V_clauses_touched = none ; gates_moved = none ; fences_moved = none
new_numbers_frozen = none (all constants exact symbolic)
files_opened_beyond_build_and_seed = PA (789338ad), CL-ERROR (3b9730e0),
    CL-ERROR-CHECK (b4a55baa), BL2STAR (6e81ae92), BL2STAR-CHK (2699af25),
    KAPPA_N (3b5e95b6), CL1-REFUTED (efb08860) — all sidecar-verified
fenced_classes = matched filenames listed by sweep only, NEVER opened
Q_tokens = EXPECTED-UNLOCATABLE, noted not chased
CAS = sympy 1.14.0, fresh venv; build script verbatim re-run 19/19 PASS
    byte-identical; audit batteries 21+6+8+1 checks, all PASS after
    disclosed script repairs; scripts hashed (§1, §7 T-4)
output = ONE artifact + seal sidecar at the commission-distinct path,
    probed ABSENT at start and re-probed before write; no git, no register,
    no existing file edited
```
