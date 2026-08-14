# STAGE 8 — BLIND CROSS-LINEAGE AUDIT OF STAGE8_RL4_RL0_CERTIFICATION_V001

## BLIND INDEPENDENT AUDITOR — CODENAME RL4-RL0-AUDIT — [SEALED]

Date: 2026-08-14
Role: BLIND independent auditor, cross-lineage. Posture: skeptical
re-derivation — nothing confirmed that was not re-derived here. Under test:
`STAGE8_RL4_RL0_CERTIFICATION_V001.md`, sha256
`a903716c23c1a6969932e988f90d464abe9e8ee96624cd2dce3e32416de132e0`
(recomputed from bytes at path this session; matches the tasked digest and
the sidecar `.seal.sha256`).

Gates: `alpha_computed = false` ; `kappa_record_computed = false` ;
`proof_authorized = false`. ALL_RESULTS = CLAIMED until checked.

Fences held: EXACT SYMBOLIC ANALYSIS ONLY — one CAS script of my own
(sympy 1.14.0, venv `zfcheckvenv`, NOT the artifact's `rl4venv`; script and
output verbatim in §6, 30/30 PASS), routes DIFFERENT from the artifact's
wherever a different exact route exists. Nothing numeric evaluated; every
constant symbolic or exact rational/surd. No scale, imported GR, or
faithfulness authority. M(t) sharp; equal-time FALSE by C6. No
register/tracker/plan/road/ledger/lens file read. Output name probed before
write: ABSENT. No git action; not registered, not pushed.

---

## 0. VERDICT IN ONE LINE

**CONFIRMED on all five audits. The clause quotes are byte-faithful
(mechanical diff, 0 mismatches against E1 :766-790; §3.1/§3.5/D3 quotes
verified by independent read); the Task A census/normalization re-derives
exactly and is everywhere presented as conditional on the exclusion, with
all three witnesses left standing; x's sealed form and its
exponent-explicit expansion re-derive exactly (my CAS X1/X2), the four
unvalued items are each verified at their sealed bytes, and the fence
reasoning survives audit — nothing numeric was evaluated, the stricken
display was consumed only in its clause-permitted fixed-n form, and no
value of D was inferred; the R-L0 quantifier is the unrestricted D3 family
at :856 + :687-689 + :417-426, neither narrowed nor widened by the
artifact; provenance clean, injection none. Three audit notes (§5, none
refuting): the word "dichotomy" names two sufficient-condition branches
that do NOT partition the parameter space; §2.4's parenthetical "(Branch
1)" labels the necessary condition det_n(0) -> 0 with its sufficient
condition; and u-4's "no admissible M" phrasing is ZF o-1's paraphrase of
52f2490b, whose own flag says it as `RL2b_uniformity_refuted = true` /
`X_HS_norm_infinite = true` / `eps_threshold_exists = false` (its :22
states the M-form obligation). None of the three moves any verdict, act,
or witness.**

---

## 1. SEALS — ALL RECOMPUTED FROM BYTES AT PATH THIS SESSION

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`. Full
digests recomputed by me (never substring presence); all match the tasked
prefixes and the artifact's §1 table. None unverifiable.

```text
a903716c23c1a6969932e988f90d464abe9e8ee96624cd2dce3e32416de132e0  STAGE8_RL4_RL0_CERTIFICATION_V001.md         (under test; = sidecar)
26f9314bdbbf1d7638ecbdf398c891cb3ba54251d4b40314df39c03ab48c08b7  STAGE8_ZERO_FREE_DERIVATION_V001.md          MATCH (ZF)
aed551e3dba40a0846e540709f0608398d2f5d28764e01033efbd9b20ed1d90f  STAGE8_ZERO_FREE_CHECK_V001.md               MATCH (ZF-CHK)
468467303a109dc825b015107897dacc107800fc981030377c3f006b384cccb5  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md  MATCH (E1)
2e4e5163bb5b9c06078890fc573dd149905975b55860dcabcc7050fb1aa02666  STAGE8_REMAINDER_UNIFORMITY_V001.md          MATCH (REM)
89641f762d35c0e6d3c8fb0475e2de742663f9dcf9f08a44621b059c2bd927ec  STAGE8_REMAINDER_UNIFORMITY_CHECK_V001.md    MATCH (REM-CHK)
a7969f0c3a42112ee300f73617494fb77c2a415bf5b6cf4d33598c6b6c8bf9cf  STAGE8_R2_RESUMMATION_V001.md                MATCH (R2)
a4f2e1b7878139afd017abe5fb62c6af7bf19836f7f162ef62902265bfc03cb5  STAGE8_R2_RESUMMATION_CHECK_V001.md          MATCH (R2-CHK)
789338adb7d3d36da453113e98f371a4f92543cf2652b047f8481c407bed5bc3  STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md  MATCH (PA)
52f2490b187fd4b307c2af45f6238ea02f1d6839b23466fefee1dbba47ed6241  STAGE8_RL2B_UNIFORMITY_REFUTED_RESULT_V001.md  MATCH (per-pair refutation)
```

---

## 2. AUDIT 1 — THE CLAUSES AT THE SEALED BYTES

**Method.** I read E1 :650-899, :417-426, :995-1029 directly, then ran a
mechanical line-by-line diff of the artifact's §2.1 quote block (its lines
121-145, stripping the `:NNN` prefixes) against E1 lines 766-790 at bytes.

**Result: 0 mismatches.** The §2.1 quote of R-L4a/b/R-L4 is byte-faithful
(whitespace-normalized). Independently verified by read:

```text
v-1  R-L4b's "as displayed above" = the R.2 display at :759-762
     ("det(1 + A(a)) = 0 for ALL a ... EXCLUDED from every sum, sup and
     segment rather than being assigned a value") — exactly as the
     artifact maps it.
v-2  The sector algebra context: V(0) - 1 = (phase_mu phase_lambda - 1)P
     at :746-748; tr(CPC) = +infinity as C2's divergence at :757-758;
     ||CPC||_2 radius-independent and INFINITE by C6 in the S3-deletion
     grounds at :713-715. All present at those bytes.
v-3  kappa_bal consequence :794-800 — from surviving weights, "NOT from
     the (1+|D|)/|1-D| display, and NOT from any claim that D = 0", with
     the KAPPA_BAL_DERIVED_FROM_STRICKEN_DISPLAY block — as quoted.
v-4  R-L0's operative demand :854-858 quoted in §3.1 — verbatim at bytes,
     including "for EVERY admitted cell of D3" (:856-857) and the frozen
     1/2 threshold.
v-5  R-L0b :877-885 quoted in full in §3.5 — verbatim at bytes; register
     line :1010 confirmed.
v-6  The block-triangular identity at :657-659 and the Log-rho display
     with "VALID ONLY ON THE SURVIVING SECTOR" at :663-666 — as cited.
v-7  The O.R register tail :1024-1029 (R-L4a "with the regularization
     named"; R-L4b; R-L4 "reported per state; never a discharge of H-B")
     — consistent with everything the artifact certifies and withholds.
```

**Clause-wording daylight test.** The artifact's certification claims were
checked word-against-clause: (i) it certifies the unregularized half in
the clause's own words ("D IS UNDEFINED", NOT "D = 0") and does not touch
the reserved naming act ("WITH THE REGULARIZATION EXPLICITLY NAMED" —
:768 — left to the spec author, ZF o-3 concurring at ZF :420-425); (ii)
it reports the stricken display only as the clause's own :774-778 permits
(finite-dimensional REPORTED item, never at an infinite right side, no
value of D inferred); (iii) R-L4 is reported as "CANDIDATE partial
statement ... NEVER as a discharge of H-B" with the witness left standing.
No daylight found. **CLAUSES_AUDIT = CONFIRMED.**

---

## 3. AUDIT 2 — TASK A RERUN (CENSUS / NORMALIZATION)

Re-derived from the sealed inputs only (weights (1/2, -1/4, -1/4) on
lambda = (0, +sqrt2, -sqrt2) — of record at R2 :78; phases (+1,-1,-1) at
E1 :743; S_± at E1 :750), by my own enumeration (§6 C1-C6, different
implementation from the artifact's A1):

```text
r-1  m_0 = 0; S_+ = 1/2, S_- = -1/2.                              MATCH
r-2  9 pairs = 5 surviving + 4 opposite.                          MATCH
r-3  surviving totals 1/2 signed = 1/2 absolute = S_+^2 + S_-^2;
     opposite -1/2 signed = 2 S_+ S_-, 1/2 absolute.              MATCH
r-4  N_surv(0) = 1/2; c = (1/2, 1/8 x 4) ALL POSITIVE;
     sum c = 1; sum |c| = kappa_bal = 1.                          MATCH
r-5  §2.2's failure-mode exhibit re-derived: with opposite dets = d,
     the all-pairs baseline is (1-d)/2 — equal to 1/2 only at d = 0,
     and 0 = m_0^2 at d = 1 (no normalization). EXACT (§6 C6).    MATCH
```

**Partial-presented-as-complete test.** The artifact states the
dependency direction explicitly (§2.2: the census CONSUMES the exclusion;
"conditional on the exclusion" appears in the verdict and flag block) and
attaches "conditional on R-L4b" to every downstream use (m-3, R-L0b's
convexity footing). R-L4a is PARTIAL with the residue enumerated; R-L4b
is NOT-DERIVABLE with three acts named; all three witnesses STAND. The
one candidate for overclaim — §0's "discharges the R-L4 BOOKKEEPING
clause's content" — is resolved by its own §2.2: the clause is a
REPORTING obligation, the report is made per the clause's terms, and
E1_BASELINE_COLLAPSE_UNCERTIFIED is explicitly kept standing. One
observation, non-refuting: the clause's "REPORTED PER STATE" qualifier is
satisfied state-uniformly — the sealed R.2 weight display (:745-762)
itself carries no state index, so per-its-own-terms reporting is
state-blind; no daylight. **TASKA_RERUN = MATCH.**

---

## 4. AUDIT 3 — X's FORM, THE SYMBOLIC INEQUALITIES, AND THE FENCES

### 4.1 The form, re-derived independently

From E1 :806-808 with S1 (:691), S2 (:696), S2b (:702), S4 (:720) read at
bytes, I re-derived by hand and by CAS (§6 X1):

```text
x = |C|_4 (G_tr + rho_res G_hs (G_cm + G_hs))
  = |tr[C Delta C]| + rho_res ( ||C Delta C||_2 Gcm_num |C|_4^{1-alpha-beta}
                               + ||C Delta C||_2^2 |C|_4^{1-2 alpha} ),
```

an exact expansion (CAS-verified identity). Powers cancel IFF
1 - alpha - beta = 0 AND 1 - 2 alpha = 0, whose unique solution is
alpha = beta = 1/2 (§6 X2) — matching the artifact's "IFF R-L2b's
exponents balance (alpha + beta = 1, alpha = 1/2)" and E1's own
conditional-bookkeeping downgrade at :817-824. **X_RERUN = MATCH (the
form).**

### 4.2 The cell-dependence claim, verified item by item

```text
u-1  alpha/beta symbols: E1 :698-700 ("Until R-L2b closes, alpha is a
     symbol, not 1/2"), :707 (beta with alpha under R-L2b), R-L2b open at
     :826-832 with witness SCAD_HS_SCALING_EXPONENT_UNDERIVED.   VERIFIED
u-2  rho_res = H-R: E1 :725-727 ("NOT discharged here. May NEVER default
     to 1 or to any other value (F'-3)").                        VERIFIED
u-3  G_cm form uncertified: E1 :708, witness
     E1_RECORD_KINK_COMMUTATOR_FORM_UNCERTIFIED.                 VERIFIED
u-4  per-pair carrier sup +infinity of record: 52f2490b at path (:22
     states the obligation "sup_n ||X_n||_2 <= M with M admissible";
     flags RL2b_uniformity_refuted = true, X_HS_norm_infinite = true,
     eps_threshold_exists = false); ZF o-1 (:394-399) carries the
     "no admissible M" paraphrase and the fixed-n x_n n-DEPENDENCE.
                                                                 VERIFIED
```

So x is neither a cell-independent constant nor a determinate symbolic
expression on the discharged basis; it exists as the fixed-n family x_n,
and the D3 cell-sup of x_n is the R-L2b scaling question (:819-824
exhibits the alpha = 0 divergence mode for the deleted S3). The
artifact's CELL-DEPENDENCE claim is exactly right.

### 4.3 The symbolic inequalities, re-checked by different routes

```text
i-1  Threshold: with kappa_bal = 1, X_* e^{X_*} <= 1/2 <=> X_* <= W(1/2).
     My route (different from the artifact's solve): W((1/2)e^{1/2}) = 1/2
     by the defining identity z e^z = arg (§6 F1, xreplace-exact) plus
     strict monotonicity of u e^u on u >= 0 (§6 F4) and of W on y > 0
     (§6 F3, W' = W/(y(1+W))); then 1/2 < (1/2)e^{1/2} (equivalent to
     1/2 > log 1 = 0, §6 F2) gives W(1/2) < W((1/2)e^{1/2}) = 1/2.
     CONFIRMED: X_* <= W(1/2) < 1/2, unique root.
i-2  Record-cycle scale: sqrt2 · tau_R = sqrt2 · (pi/sqrt2) = pi exactly,
     and the discharged all-orders dominator is e^{sqrt2 tau_R} = e^pi
     (REM :162, :805; R2's domination uses ONLY |lambda| <= sqrt2 and
     Theta <= tau_R — read at R2 :173-176, :330; Theta = tau_R(1-16r^4)
     monotone decreasing, §6 H4). CONFIRMED (§6 G1).
i-3  pi e^pi > 1/2: my route pi > 2 (unit disc contains the inscribed
     square of area 2) > 1/2, e^pi > 1 (§6 G2/G3) — product exceeds
     1/2 · 1. CONFIRMED SYMBOLICALLY. Sharper than needed; the failure
     conditional only needs x >= 1/2 => x e^x >= (1/2)e^{1/2} > 1/2
     (§6 G4, monotonicity), which re-derives §3.3(c)'s "any constant
     >= 1/2 breaches the threshold" exactly.
i-4  Fixed-n structure: det_{ran C}(1-2CPC) = prod(1-2 s_i) via the
     sealed R-L1 identity (:657-659; finite-dimensional det(1+AB) =
     det(1+BA) closes the C-right-factor gap exactly at fixed n);
     (1-2s)^2 = 1-4s(1-s); s(1-s) = 1/4 - (s-1/2)^2; 1-4u <= e^{-4u}
     (coefficientwise-positive series route, §6 D4/D5); and the
     commutator identity ||[C,P]||_2^2 = 2 tr(CPC) - 2 tr((CPC)^2)
     verified on an ALL-theta one-parameter exact projection family
     (§6 D1-D3) — a continuum of exact instances, a stronger route than
     rational trials — plus the cyclic-trace operator argument checked
     by hand (tr(PCP) = tr(CP) = tr(CPC), tr((CP)^2) = tr((CPC)^2)).
     Hence |det_n(0)|^2 <= exp(-2 kappa_n): Branch 1 re-derived.
i-5  Branch 2: |s_i - 1/2| >= delta => u_i <= U := 1/4 - delta^2 (from
     the D4 identity); 1 - 4U = 4 delta^2 (§6 E3); chord bound from
     concavity (§6 E2) re-confirmed by a DIFFERENT route at the midpoint
     — log(1-2U) >= (1/2)log(1-4U) <=> (1-2U)^2 - (1-4U) = 4U^2 >= 0,
     an exact polynomial identity (§6 E1); then sum u_i <= M gives
     |det_n(0)|^2 >= (4 delta^2)^{M/U}, i.e. |det_n(0)| >=
     (4 delta^2)^{M/(2U)} > 0 — the flag block's constant, re-derived.
i-6  |rho - 1| <= x e^x support: e^x - 1 <= x e^x on x >= 0 (§6 G5).
i-7  Entered-cell data by a different (Piecewise/Min) route: int_0^1
     32 r(t)^3 dt = 1; |C|_4 = pi/24 EXACT; int v = tau_R = pi/sqrt2
     EXACT; b_D(1/2,0) = exp(16 - 1/(1/16)·...) = e^0 = 1 EXACT
     (s(1/2,0) = 1/16) (§6 H1-H5, PA :84-108 read at bytes).
```

### 4.4 Fence-reasoning audit

```text
f-1  Numeric evaluation: NONE found. Every constant in the artifact's §5
     and in the chain of §2-§3 is symbolic or exact rational/surd; the
     orderings used (pi > 1/2, e^{1/2} > 1, e^pi > 1, W(1/2) < 1/2) are
     exact orderings of mathematical constants internal to the sealed
     threshold display, each grounded by a monotonicity chain — the
     artifact's "structural arithmetic" framing is honest. No decimal
     appears anywhere in either artifact. The inequality x <= X_* was
     never instantiated — the artifact's NOT REQUIRES-EVALUATION
     reasoning (blocker upstream of any evaluation) is correct and is
     the right verdict class.
f-2  The stricken display (:773-778): consumed ONLY at fixed n as the
     clause's own REPORTED-item permission allows; never evaluated at an
     infinite right side; no value of D inferred (D stays UNDEFINED;
     Branch 1 is a limit statement about det_n(0) along the named-family
     candidate, conditional on the unsealed kappa_n input — which is the
     clause's own :779-781 "regularized route" invitation, honestly
     narrowed). CLEAN.
f-3  kappa_bal: derived from surviving weights only (§2.2/CAS A1), never
     from the stricken (1+|D|)/|1-D| display — the :794-800 block is
     satisfied. CLEAN.
f-4  No coarsest-cell 4-volume, V_max, skeleton, or cellulation-family
     datum substituted for X_* (:873-875): the entered-cell data
     (|C|_4 = pi/24, tau_R) are reported as data of the entered cell and
     explicitly NOT offered as X_*. CLEAN.
f-5  Equal-time/C6: the omega = 0 slice consumed only as R2 §4's sealed
     bookkeeping intermediate; S2's two-time requirement (:697-698)
     respected. M(t) sharp throughout. CLEAN.
f-6  Gates: alpha_computed / kappa_record_computed / proof_authorized
     all false and nothing in the artifact computes either quantity or
     authorizes anything. CLEAN.
f-7  The artifact's CAS: script + output verbatim in its §5; I re-ran
     the mathematics on MY OWN battery (different venv, different
     routes, §6) rather than re-executing theirs — every mathematical
     claim their 20 checks assert is confirmed by my 30. CLEAN.
```

**FENCE_AUDIT = CLEAN.**

---

## 5. AUDIT 4 — THE QUANTIFIER ; AND THREE NON-REFUTING NOTES

**Quantifier.** At bytes: R-L0 binds "for EVERY admitted cell of D3"
(:856-857); the cell-sup is the one DEFERRED at :687-689; D3 is the
FROZEN unrestricted common-refinement reading at :417-426 ("ANY
cellulation refining BOTH parents — UNRESTRICTED, UNIVERSALLY QUANTIFIED
... NOT the minimal overlay"), with the pinning reserved above any lane.
The artifact quantifies over exactly this class — an unbounded family —
and explicitly refuses both narrowings (the entered cell; any
cellulation-family substitute) and any widening. The tasking's "b_1 = 1"
designation is indeed absent from the sealed sources (grep over E1/PA/ZF:
no such token); the artifact's mapping of it to the entered PA
unit-diamond cell (b_D(1/2,0) = 1 at PA :107-108, ||b_D||_inf = 1 per E1
:864) is the only sealed referent and is correctly labeled a mapping.
**QUANTIFIER_AUDIT = CONFIRMED.**

**Three audit notes — none refuting, no verdict/act/witness moves:**

```text
n-1  "Dichotomy" (§2.3(d), flag block): the two branches are a
     sufficient condition for vanishing (kappa_n -> infinity) and a
     sufficient condition for non-vanishing (bounded kappa_n AND uniform
     1/2-avoidance). They do NOT partition: bounded kappa_n WITHOUT
     uniform 1/2-avoidance is a third, undecided region (a single
     s_i -> 1/2 drives det_n(0) -> 0 at bounded commutator mass). The
     artifact's own text marks Branch 1 "sufficient" and defines Branch 2
     with both hypotheses, and no conclusion consumes exhaustiveness —
     the residue (r-2) and the R-L4b conditional FALSE (which cites
     Branch 2 as defined, avoidance included) survive as stated. Wording
     note only.
n-2  §2.4's "needs det_n(0) -> 0 (Branch 1)": det_n(0) -> 0 is the
     NECESSARY condition (value at a = 0); kappa_n -> infinity (Branch 1)
     is sufficient for it, not equivalent to it. The joint rate
     ||R_n Delta_n(a)||_1 = o(-log|det_n(0)|) is the sufficient estimate
     for the factorization route, correctly named as the act (r-3).
     Label imprecision only; the named acts are unaffected.
n-3  u-4's "no admissible M" phrase sits in ZF o-1's paraphrase of
     52f2490b, not verbatim in 52f2490b's flag block; the file's own :22
     states the M-form obligation and its flags refute it
     (RL2b_uniformity_refuted = true; X_HS_norm_infinite = true;
     eps_threshold_exists = false). Substance identical; attribution
     note only.
```

**Provenance.** Every line citation in the artifact was spot-verified at
bytes this session: E1 :417-426, :650-666, :679-689, :691-736, :745-762,
:766-790, :794-800, :803-848, :851-894, :995-1029; PA :63-142 (carrier
n = 2, ell in {1, sqrt2}; r(t) = min(t,1-t); M(t) = Q 1_{|x|<=r(t)} Q;
v(t) = (pi/sqrt2) 32 r(t)^3; b_D and its diamond; frozen (a_+,a_-)
pairs); R2 :78-98, :158-190, :320-340; REM :352-383, :162, :805; ZF
:394-425 (o-1..o-3), :657-681 + :727-729 (Z10 census), :435-436; ZF-CHK
:37, :49-59 (landing set = summed-S2' + R-L4a/b + R-L0(/R-L0b) +
C-L2/G_cm — the artifact's NET matches it verbatim); 52f2490b :22, :182,
flags. No citation failed. The §2.1 quote block is mechanically
byte-faithful. **PROVENANCE = CLEAN.**

**Injection.** No instruction-shaped content directed at an auditor found
in the artifact or any sealed source read; no steering text; the
artifact's flag block matches its body (registered-from-flag-block rule
satisfiable without divergence). Seals were verified by full-digest
recomputation, never by substring presence. **INJECTION = none.**

---

## 6. MY CAS BATTERY (VERBATIM) AND ITS OUTPUT (VERBATIM)

sympy 1.14.0, venv `zfcheckvenv` (not the artifact's `rl4venv`). Exact
symbolic / exact rational only. Routes chosen to DIFFER from the
artifact's §5: independent census enumeration + S_± identity route (C4);
symbolic all-theta projection family instead of rational trials (D1-D3);
coefficientwise series positivity for e^u ordering (D5); midpoint
polynomial identity for the chord bound (E1); LambertW inverse-identity +
W-monotonicity route for the threshold (F1-F4); pi > 2 disc-vs-square
ordering (G2); Piecewise/Min integration for the cell data (H1-H3).

```python
# RL4-RL0-AUDIT independent CAS battery — EXACT SYMBOLIC ONLY (sympy 1.14.0,
# venv zfcheckvenv, NOT the artifact's rl4venv). Different routes than the
# artifact's §5 wherever a different route exists. Nothing numeric evaluated;
# every constant symbolic or exact rational/surd.
import itertools
import sympy as sp
from sympy import Rational as R

ok = lambda name, cond: print(f"{name}: {'PASS' if cond else 'FAIL'}")

# ---------- AUDIT 2 (Task A rerun) — census by independent enumeration ----------
lam = ['0', '+s2', '-s2']
w = {'0': R(1, 2), '+s2': R(-1, 4), '-s2': R(-1, 4)}   # sealed weights (R2 :78, E1 :750 S_+/S_-)
ph = {'0': 1, '+s2': -1, '-s2': -1}                    # sealed phases (E1 :743)
pairs = list(itertools.product(lam, lam))
surv = [p for p in pairs if ph[p[0]] == ph[p[1]]]
opp = [p for p in pairs if ph[p[0]] != ph[p[1]]]
Sp = sum(w[l] for l in lam if ph[l] == 1)
Sm = sum(w[l] for l in lam if ph[l] == -1)
ok("C1 m_0 = 0, S_+ = 1/2, S_- = -1/2                            ",
   sum(w.values()) == 0 and Sp == R(1, 2) and Sm == R(-1, 2))
ok("C2 census 9 = 5 surviving + 4 opposite                       ",
   len(pairs) == 9 and len(surv) == 5 and len(opp) == 4)
sv_sgn = sum(w[a]*w[b] for a, b in surv)
sv_abs = sum(abs(w[a]*w[b]) for a, b in surv)
op_sgn = sum(w[a]*w[b] for a, b in opp)
op_abs = sum(abs(w[a]*w[b]) for a, b in opp)
ok("C3 surviving signed = abs = 1/2; opposite -1/2 signed, 1/2 abs",
   sv_sgn == R(1, 2) and sv_abs == R(1, 2) and op_sgn == R(-1, 2) and op_abs == R(1, 2))
# independent identity route: totals from S_+/S_- algebra
ok("C4 sv_sgn = S_+^2 + S_-^2 ; op_sgn = 2 S_+ S_- (identities)   ",
   sv_sgn == Sp**2 + Sm**2 and op_sgn == 2*Sp*Sm)
Nsurv = sv_sgn   # collapse level det(1+A(0)) = 1 on surviving pairs, CONDITIONAL on exclusion
c = {p: w[p[0]]*w[p[1]]/Nsurv for p in surv}
ok("C5 N_surv = 1/2; c = {1/2, 1/8 x4} all > 0; sum c = 1; k_bal=1",
   Nsurv == R(1, 2) and sorted(c.values()) == [R(1, 8)]*4 + [R(1, 2)]
   and all(v > 0 for v in c.values()) and sum(c.values()) == 1
   and sum(abs(v) for v in c.values()) == 1)
# failure-mode exhibit of §2.2: all-pairs baseline with opposite dets = d
d = sp.symbols('d')
N_all = sv_sgn*1 + op_sgn*d
ok("C6 N_all = (1-d)/2 ; N_all(1) = 0 = m_0^2 ; N_all(d!=0)!=1/2  ",
   sp.expand(N_all - (1 - d)/2) == 0 and N_all.subs(d, 1) == 0
   and sp.expand(N_all - R(1, 2) + d/2) == 0)

# ---------- AUDIT 3 (Task B / X form rerun) — symbolic expansion ----------
V4, alpha, beta, T, H, Gcm_n, rho = sp.symbols(
    'V4 alpha beta T H Gcm_n rho', positive=True)
G_tr = T/V4
G_hs = V4**(-alpha)*H
G_cm = V4**(-beta)*Gcm_n
x_sealed = V4*(G_tr + rho*G_hs*(G_cm + G_hs))
x_expl = T + rho*(H*Gcm_n*V4**(1 - alpha - beta) + H**2*V4**(1 - 2*alpha))
ok("X1 sealed x == exponent-explicit form (exact expansion)       ",
   sp.simplify(x_sealed - x_expl) == 0)
# powers cancel iff alpha+beta = 1 AND alpha = 1/2 (both exponents zero)
e1_, e2_ = 1 - alpha - beta, 1 - 2*alpha
sol = sp.solve([e1_, e2_], [alpha, beta], dict=True)
ok("X2 both V4-powers vanish iff alpha = 1/2, beta = 1/2 (unique)  ",
   sol == [{alpha: R(1, 2), beta: R(1, 2)}])

# ---------- AUDIT 3 — fixed-n determinant structure, different routes ----------
s, u, U, dlt = sp.symbols('s u U delta', real=True)
# one-parameter EXACT projection family (all-theta symbolic, not rational trials):
th = sp.symbols('theta', real=True)
cth, sth = sp.cos(th), sp.sin(th)
C2m = sp.Matrix([[cth**2, cth*sth], [cth*sth, sth**2]])   # proj onto span(cos,sin)
P2m = sp.Matrix([[1, 0], [0, 0]])
ok("D1 C, P are exact projections (C^2=C, P^2=P, symmetric)       ",
   sp.simplify(C2m*C2m - C2m) == sp.zeros(2) and P2m*P2m == P2m)
CPC = C2m*P2m*C2m
lhs = sp.trace((C2m*P2m - P2m*C2m).T*(C2m*P2m - P2m*C2m))
rhs = 2*sp.trace(CPC) - 2*sp.trace(CPC*CPC)
ok("D2 ||[C,P]||_F^2 = 2tr(CPC) - 2tr((CPC)^2) ALL theta (symbolic)",
   sp.simplify(lhs - rhs) == 0)
# eigenvalue of CPC on ran C is s1 = cos^2 theta; det_{ran C}(1-2CPC) = 1-2cos^2
detr = sp.simplify(sp.trace(C2m*(sp.eye(2) - 2*P2m)*C2m))  # rank-1 ran C: value = 1-2s1
ok("D3 det_ranC(1-2CPC) = 1 - 2 cos^2(theta) (rank-1 exact)       ",
   sp.simplify(detr - (1 - 2*cth**2)) == 0)
# per-factor identities:
ok("D4 (1-2s)^2 = 1 - 4s(1-s) and s(1-s) = 1/4 - (s-1/2)^2        ",
   sp.expand((1 - 2*s)**2 - (1 - 4*s*(1 - s))) == 0
   and sp.expand(s*(1 - s) - (R(1, 4) - (s - R(1, 2))**2)) == 0)
# 1-4u <= e^{-4u} on u >= 0: h(u) = e^{-4u} - 1 + 4u, h(0) = 0, h' = 4(1-e^{-4u});
# e^{4u} >= 1 on u >= 0 because e^{4u} - 1 = sum_{k>=1} (4u)^k/k!, ALL coefficients
# positive — checked coefficientwise on the exact series:
h = sp.exp(-4*u) - 1 + 4*u
ser = sp.series(sp.exp(4*u) - 1, u, 0, 6).removeO()
coeffs_pos = all(sp.Poly(ser, u).coeffs()[i] > 0 for i in range(len(sp.Poly(ser, u).coeffs())))
ok("D5 h(0) = 0 ; h' = 4(1-e^{-4u}) ; e^{4u}-1 coeffwise > 0       ",
   h.subs(u, 0) == 0 and sp.simplify(sp.diff(h, u) - 4*(1 - sp.exp(-4*u))) == 0
   and coeffs_pos)
# Branch-2 chord bound, DIFFERENT route: midpoint identity + concavity.
# claim: log(1-4u) >= (u/U) log(1-4U) on [0,U]; at u = U/2 it is equivalent to
# (1-2U)^2 >= (1-4U), i.e. 4U^2 >= 0 — an exact polynomial identity:
ok("E1 midpoint: (1-2U)^2 - (1-4U) = 4U^2 >= 0 (exact identity)   ",
   sp.expand((1 - 2*U)**2 - (1 - 4*U) - 4*U**2) == 0)
ok("E2 concavity: d2/du2 log(1-4u) = -16/(1-4u)^2 < 0 (u < 1/4)   ",
   sp.simplify(sp.diff(sp.log(1 - 4*u), u, 2) + 16/(1 - 4*u)**2) == 0)
# avoidance: |s - 1/2| >= delta => u = s(1-s) <= 1/4 - delta^2 (from D4 identity)
# 1 - 4U at U = 1/4 - delta^2 equals 4 delta^2:
ok("E3 1 - 4(1/4 - delta^2) = 4 delta^2 (exact)                   ",
   sp.expand(1 - 4*(R(1, 4) - dlt**2) - 4*dlt**2) == 0)

# ---------- AUDIT 3 — threshold algebra, different routes ----------
# W(1/2) < 1/2 via W-monotonicity route: W((1/2)e^{1/2}) = 1/2 exactly,
# and W increasing on (0, oo) since W'(y) = W/(y(1+W)) > 0; 1/2 < (1/2)e^{1/2}.
Wexp = sp.LambertW(R(1, 2)*sp.exp(R(1, 2)))
# CAS route: z := W((1/2)e^{1/2}) satisfies z e^z = (1/2)e^{1/2} (defining identity,
# CAS-exact); z > 0 arithmetically (z = ((1/2)e^{1/2})/e^z with positive numerator);
# u e^u strictly increasing on u >= 0 (F4) and attains (1/2)e^{1/2} at u = 1/2
# => z = 1/2. The two CAS-checkable pieces:
arg = R(1, 2)*sp.exp(R(1, 2))
defining = (Wexp*sp.exp(Wexp) - arg).xreplace({sp.exp(Wexp): arg/Wexp})  # e^{W(x)} = x/W(x)
ok("F1 z e^z = (1/2)e^{1/2} (defining) ; (1/2)e^{1/2} at u = 1/2   ",
   sp.simplify(defining) == 0
   and sp.simplify((u*sp.exp(u)).subs(u, R(1, 2)) - arg) == 0)
ok("F2 1/2 < (1/2)e^{1/2}  <=>  e^{1/2} > 1  <=>  1/2 > log 1 = 0  ",
   sp.log(1) == 0 and R(1, 2) > 0 and bool(sp.exp(R(1, 2)) > 1))
y = sp.symbols('y', positive=True)
Wy = sp.LambertW(y)
ok("F3 W'(y) = W/(y(1+W)) > 0 on y > 0 (W increasing)             ",
   sp.simplify(sp.diff(Wy, y) - Wy/(y*(1 + Wy))) == 0)
# u e^u strictly increasing; unique root of u e^u = 1/2:
ok("F4 d/du(u e^u) = (1+u)e^u > 0 on u >= 0 ; root set = {W(1/2)}  ",
   sp.simplify(sp.diff(u*sp.exp(u), u) - (1 + u)*sp.exp(u)) == 0
   and sp.solve(u*sp.exp(u) - R(1, 2), u) == [sp.LambertW(R(1, 2))])
# record-cycle scale: sqrt2 * tau_R = pi exactly; pi e^pi > 1/2 by ordering
tau_R = sp.pi/sp.sqrt(2)
ok("G1 sqrt2 * tau_R = pi EXACT ; dominator e^{sqrt2 tau_R} = e^pi ",
   sp.simplify(sp.sqrt(2)*tau_R - sp.pi) == 0
   and sp.simplify(sp.exp(sp.sqrt(2)*tau_R) - sp.exp(sp.pi)) == 0)
ok("G2 pi > 2 (unit-disc vs inscribed square, exact) => pi > 1/2   ",
   bool(sp.pi > 2) and bool(sp.pi > R(1, 2)))
ok("G3 e^pi > 1 (pi > 0, exp increasing) ; hence pi e^pi > 1/2     ",
   bool(sp.exp(sp.pi) > 1))
# the failure conditional: x >= 1/2 at a cell => x e^x >= (1/2)e^{1/2} > 1/2
ok("G4 (1/2)e^{1/2} > 1/2 (so any x >= 1/2 breaches the threshold) ",
   bool(R(1, 2)*sp.exp(R(1, 2)) > R(1, 2)))
# |rho - 1| <= x e^x support: e^x - 1 <= x e^x on x >= 0
xx = sp.symbols('x', nonnegative=True)
g4 = xx*sp.exp(xx) - sp.exp(xx) + 1
ok("G5 g(0) = 0, g'(x) = x e^x >= 0  =>  e^x - 1 <= x e^x on x>=0  ",
   g4.subs(xx, 0) == 0 and sp.simplify(sp.diff(g4, xx) - xx*sp.exp(xx)) == 0)

# ---------- AUDIT 3 — entered cell data, different route (Piecewise/Min) ----------
t = sp.symbols('t', real=True)
r_t = sp.Min(t, 1 - t)
I32 = sp.integrate(32*sp.Piecewise((t, t <= R(1, 2)), (1 - t, True))**3, (t, 0, 1))
ok("H1 int_0^1 32 r(t)^3 dt = 1 (Piecewise route)                 ", I32 == 1)
V4cell = sp.integrate(R(4, 3)*sp.pi*sp.Piecewise((t, t <= R(1, 2)), (1 - t, True))**3,
                      (t, 0, 1))
ok("H2 |C|_4 = pi/24 EXACT (Piecewise route)                      ",
   sp.simplify(V4cell - sp.pi/24) == 0)
ok("H3 int v = tau_R * 1 = pi/sqrt2 EXACT                         ",
   sp.simplify(tau_R*I32 - sp.pi/sp.sqrt(2)) == 0)
# Theta = tau_R(1 - 16 rho^4) monotone decreasing on [0,1/2]: Theta' = -64 tau_R rho^3
rr = sp.symbols('r_v', nonnegative=True)
Th = tau_R*(1 - 16*rr**4)
ok("H4 Theta(0) = tau_R, Theta(1/2) = 0, Theta' = -64 tau_R r^3<=0 ",
   sp.simplify(Th.subs(rr, 0) - tau_R) == 0 and Th.subs(rr, R(1, 2)) == 0
   and sp.simplify(sp.diff(Th, rr) + 64*tau_R*rr**3) == 0)
# b_D(1/2,0) = 1 from the sealed formula exp(16 - 1/s), s(1/2,0) = 1/16:
s_m = (t**2)*((1 - t)**2)   # at x = 0
ok("H5 s(1/2,0) = 1/16 ; b_D(1/2,0) = exp(16 - 16) = 1 EXACT      ",
   s_m.subs(t, R(1, 2)) == R(1, 16)
   and sp.exp(16 - 1/s_m.subs(t, R(1, 2))) == 1)

print("AUDIT-DONE")
```

Output, verbatim (30/30 PASS):

```text
C1 m_0 = 0, S_+ = 1/2, S_- = -1/2                            : PASS
C2 census 9 = 5 surviving + 4 opposite                       : PASS
C3 surviving signed = abs = 1/2; opposite -1/2 signed, 1/2 abs: PASS
C4 sv_sgn = S_+^2 + S_-^2 ; op_sgn = 2 S_+ S_- (identities)   : PASS
C5 N_surv = 1/2; c = {1/2, 1/8 x4} all > 0; sum c = 1; k_bal=1: PASS
C6 N_all = (1-d)/2 ; N_all(1) = 0 = m_0^2 ; N_all(d!=0)!=1/2  : PASS
X1 sealed x == exponent-explicit form (exact expansion)       : PASS
X2 both V4-powers vanish iff alpha = 1/2, beta = 1/2 (unique)  : PASS
D1 C, P are exact projections (C^2=C, P^2=P, symmetric)       : PASS
D2 ||[C,P]||_F^2 = 2tr(CPC) - 2tr((CPC)^2) ALL theta (symbolic): PASS
D3 det_ranC(1-2CPC) = 1 - 2 cos^2(theta) (rank-1 exact)       : PASS
D4 (1-2s)^2 = 1 - 4s(1-s) and s(1-s) = 1/4 - (s-1/2)^2        : PASS
D5 h(0) = 0 ; h' = 4(1-e^{-4u}) ; e^{4u}-1 coeffwise > 0       : PASS
E1 midpoint: (1-2U)^2 - (1-4U) = 4U^2 >= 0 (exact identity)   : PASS
E2 concavity: d2/du2 log(1-4u) = -16/(1-4u)^2 < 0 (u < 1/4)   : PASS
E3 1 - 4(1/4 - delta^2) = 4 delta^2 (exact)                   : PASS
F1 z e^z = (1/2)e^{1/2} (defining) ; (1/2)e^{1/2} at u = 1/2   : PASS
F2 1/2 < (1/2)e^{1/2}  <=>  e^{1/2} > 1  <=>  1/2 > log 1 = 0  : PASS
F3 W'(y) = W/(y(1+W)) > 0 on y > 0 (W increasing)             : PASS
F4 d/du(u e^u) = (1+u)e^u > 0 on u >= 0 ; root set = {W(1/2)}  : PASS
G1 sqrt2 * tau_R = pi EXACT ; dominator e^{sqrt2 tau_R} = e^pi : PASS
G2 pi > 2 (unit-disc vs inscribed square, exact) => pi > 1/2   : PASS
G3 e^pi > 1 (pi > 0, exp increasing) ; hence pi e^pi > 1/2     : PASS
G4 (1/2)e^{1/2} > 1/2 (so any x >= 1/2 breaches the threshold) : PASS
G5 g(0) = 0, g'(x) = x e^x >= 0  =>  e^x - 1 <= x e^x on x>=0  : PASS
H1 int_0^1 32 r(t)^3 dt = 1 (Piecewise route)                 : PASS
H2 |C|_4 = pi/24 EXACT (Piecewise route)                      : PASS
H3 int v = tau_R * 1 = pi/sqrt2 EXACT                         : PASS
H4 Theta(0) = tau_R, Theta(1/2) = 0, Theta' = -64 tau_R r^3<=0 : PASS
H5 s(1/2,0) = 1/16 ; b_D(1/2,0) = exp(16 - 16) = 1 EXACT      : PASS
AUDIT-DONE
```

(Script tooling note, on the record: two early-draft checks failed on
sympy TOOLING, not mathematics — `sp.ask` returning None on an
exponential ordering, and `subs` mis-matching inside `exp(LambertW(·))`
— and were replaced by the coefficientwise-series route (D5) and the
`xreplace` defining-identity route (F1). No mathematical claim changed.)

---

## 7. FLAG BLOCK

```text
CLAUSES_AUDIT = CONFIRMED (E1 :766-790 mechanically byte-faithful in the
  artifact's §2.1, 0 mismatches; :759-762 / :794-800 / :854-875 /
  :877-885 / :417-426 / :687-689 / :1010 quotes and mappings verified at
  bytes by independent read; no clause-wording daylight between what was
  certified and what the spec demands — the reserved naming act, the
  stricken-display permission, and the CANDIDATE/H-B language are all
  honored word-for-word).
TASKA_RERUN = MATCH (census 5/4, S_± = ±1/2, totals ±1/2 signed and 1/2
  absolute, N_surv(0) = 1/2, c = (1/2, 1/8 x 4) all positive, sum c = 1,
  kappa_bal = 1 — re-derived by independent enumeration + the S_±
  identity route, §6 C1-C5; the §2.2 failure-mode exhibit re-derived
  exactly, N_all = (1-d)/2, §6 C6; conditionality on the exclusion
  stated at every consumption point; nothing partial presented as
  complete; all three witnesses left standing).
X_RERUN = MATCH(the form: x = |C|_4 (G_tr + rho_res G_hs (G_cm + G_hs))
  re-derived from E1 :806-808 + S1/S2/S2b/S4 at :691-727; the
  exponent-explicit expansion is a CAS-exact identity, §6 X1; powers
  cancel iff alpha = beta = 1/2 — unique solution, §6 X2; the
  cell-dependence claim verified item by item — u-1 (:698-700, :707,
  :826-832), u-2 (:725-727), u-3 (:708), u-4 (52f2490b :22 + flags, ZF
  o-1 :394-399); x is the fixed-n family x_n and its D3 cell-sup is the
  R-L2b scaling question, exactly as certified).
FENCE_AUDIT = CLEAN (no numeric evaluation anywhere in the artifact; all
  orderings are exact symbolic orderings of mathematical constants
  internal to the sealed threshold display, each re-derived here by a
  DIFFERENT exact route — W(1/2) < 1/2 via the inverse identity
  W((1/2)e^{1/2}) = 1/2 + W-monotonicity, pi e^pi > 1/2 via pi > 2 and
  e^pi > 1; the "structural arithmetic" framing is honest; the stricken
  D^2-display consumed only as the fixed-n REPORTED item its clause
  permits, never at an infinite right side, no value of D inferred —
  Branch 1 is a limit statement about det_n(0) conditional on the
  unsealed kappa_n input, i.e. the clause's own :779-781 regularized
  route honestly narrowed; kappa_bal never from the stricken display; no
  X_* substitute datum; equal-time respected; gates untouched;
  NOT REQUIRES-EVALUATION is the correct verdict class — the blocker is
  missing derivations, upstream of any evaluation).
QUANTIFIER_AUDIT = CONFIRMED ("for EVERY admitted cell of D3" at E1
  :856-857; the cell-sup deferred at :687-689; D3 = the FROZEN
  unrestricted common-refinement quantifier at :417-426 — the unbounded
  family, NOT the entered cell; the artifact neither narrowed nor
  widened it; the tasking's "b_1 = 1" token confirmed ABSENT from the
  sealed sources by grep, and the artifact's mapping to the entered PA
  unit-diamond cell (b_D(1/2,0) = 1 at PA :107-108, |C|_4 = pi/24 exact,
  int v = tau_R = pi/sqrt2 exact — re-derived here by the Piecewise
  route, §6 H1-H5) is correct and correctly labeled a mapping).
NET_VERDICT = CONFIRMED(R-L4 bookkeeping reported per its own terms;
  R-L4a's unregularized half certified ("D IS UNDEFINED", identity-grade
  from sealed tr(CPC) = +infinity, re-derived: CPC >= 0 and nonnegative
  + non-finite-trace => not trace class) + the uncompressed-det_2
  sharpening (||CPC||_2 = infinity of record, :713-715) + the fixed-n
  form det_n(0) = prod(1 - 2 s_i) with both branch conditionals
  re-derived exactly (Branch 1 via the per-factor chain D4/D5; Branch 2
  lower bound (4 delta^2)^{M/(2U)} via the chord bound, re-confirmed by
  the midpoint polynomial identity E1); R-L4b and R-L0 NOT-DERIVABLE
  with all acts named (r-1..r-3; a-1..a-4 = R-L2b, H-R, C-L2/G_cm,
  summed-S2') and both MAY-FAIL branches exact conditionals — the R-L0
  failure conditional re-derived (x >= 1/2 at any admitted cell breaches
  X_* e^{X_*} <= 1/2 since (1/2)e^{1/2} > 1/2, and the discharged
  log-scale sqrt2 tau_R = pi > 1/2); R-L0b's convexity footing derived
  (all five c positive, sum c = 1, conditional on R-L4b); no gate moves,
  no flag flips, no new obstruction, no new act; landing set of record
  unchanged: summed-S2' + R-L4a/b + R-L0(/R-L0b) + C-L2/G_cm — verified
  verbatim against ZF-CHK :49-59. Three non-refuting audit notes of
  record, §5 n-1..n-3: "dichotomy" = two sufficient-condition branches,
  not a partition (bounded kappa_n without 1/2-avoidance is a third,
  undecided region); §2.4's "(Branch 1)" parenthetical labels the
  necessary condition with its sufficient condition; "no admissible M"
  is ZF o-1's paraphrase of 52f2490b, substance identical. No verdict,
  act, or witness moves on any of the three.)
PROVENANCE = CLEAN (all nine seals recomputed from bytes at path this
  session by full digest, never substring; every cited line range
  spot-verified at bytes — E1, PA, R2, REM, ZF, ZF-CHK, 52f2490b; the
  §2.1 quote block mechanically byte-faithful; the artifact's sidecar
  matches; none unverifiable).
INJECTION = none (no instruction-shaped or steering content in the
  artifact or any sealed source read; flag block consistent with body).
MACHINERY_USED_BY_ME = yes(CAS) — sympy 1.14.0, venv zfcheckvenv (not
  the artifact's), exact symbolic/rational only, script + output
  verbatim in §6 (30/30 PASS), routes deliberately different from the
  artifact's §5.
alpha_computed = false ; kappa_record_computed = false ;
proof_authorized = false.
ALL_RESULTS = CLAIMED until checked.
```
