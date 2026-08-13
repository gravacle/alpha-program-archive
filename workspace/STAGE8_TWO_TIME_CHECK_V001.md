# STAGE 8 — TWO-TIME CHECK: BLIND ADVERSARIAL VERIFICATION OF THE TWO-TIME RE-ANALYSIS

## BLIND VERIFIER — CODENAME TWO-TIME-CHECK — CROSS-LINEAGE — [SEALED]

Date: 2026-08-13
Role: BLIND adversarial verifier, DEFAULT = REFUTE. Under test:
`STAGE8_TWO_TIME_REANALYSIS_V001.md`, sha256
`18af3dee8e3e5b17fe624d1b0547f4713359473a373df1562ff584647244ccf1` — recomputed at
path this session, MATCH (and matching its sidecar).

Gates: `alpha_computed = false` ; `kappa_record_computed = false` ;
`proof_authorized = false` ; `coupling_evaluation_authorized = false`
ALL_RESULTS = CLAIMED until checked.

Fences held: EXACT SYMBOLIC ALGEBRA ONLY. The one script used is exact symbolic CAS
(sympy 1.14.0) verifying polynomial/trig Clifford identities and one symbolic
large-|k| series over symbols — nothing numeric; reproduced in full in §6. No value
of n, kappa_record, alpha, any exponent, norm, scale, or spectrum computed, bounded,
or evaluated. No scale, imported GR, or faithfulness authority; scale-bearing sealed
text read SUSPECT-ONLY to fix structure. No register/tracker/plan/road/ledger/lens
file read. Output name probed before write: ABSENT. No git action.

---

## 0. VERDICT IN ONE LINE

**TT_VERDICT = CONFIRMED(NET = FAILS(the term)). Every load-bearing claim of the
re-analysis re-derived independently and found exact: the first-order two-time term
is the sealed object's own (not an idealization); the principal symbol
i a_Delta k_hat_x b_tilde(x,k_hat) alpha.k_hat is real and correctly interleaved; the
sandwich survivor -i a_Delta k_hat_x b_tilde(x,k_hat) C(k) is degree 0, intraband,
carrier-scaling in HS, at the sealed per-pair S2 quantifier. My independent route
STRENGTHENS the finding: the sandwich isolates the survivor pointwise at every
intermediate time t' — P_-(e^{iKt'} alpha_x e^{-iKt'})P_- = -k_hat_x P_- identically
in t' (§6 V7) — so the survivor does not even depend on the Gevrey time-integration
argument; that argument is needed only for the un-sandwiched interband remnant. No
dropped scalar, no dropped longitudinal term, no wrong interleaving found. Scope
honest; two strengthening notes, zero corrections.**

---

## 1. SEALS VERIFIED AT PATH (shasum -a 256), BEFORE ANY RELIANCE

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`. Every digest
recomputed from bytes at path THIS session; every one matches both its sidecar
`.seal.sha256` and the tasked digest. None unverifiable.

```text
18af3dee8e3e5b17fe624d1b0547f4713359473a373df1562ff584647244ccf1  STAGE8_TWO_TIME_REANALYSIS_V001.md                                   MATCH (UNDER TEST)
48e0c76fc3c8bb2f2c288e8d5be91240a7383181585f7315ef2b9b7e8f46f0f2  STAGE8_ANNIH_ANCHOR_CODEX2_V001.md                                   MATCH (ANCHOR)
7cf16a3c9cb829b3c4d5a9ac2c8996897b1268e7d1e4f18d510e0ba4ce0b9c95  STAGE8_ANNIHILATION_CHECK_V001.md                                    MATCH (CHECK)
564b7040bf51da4e7aec5b00d940b5e0215a9327ebbb2cd04947c568f8c9ae50  STAGE8_CANC_PANEL_SYMHUNT_V001.md                                    MATCH (SYMHUNT)
468467303a109dc825b015107897dacc107800fc981030377c3f006b384cccb5  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md                          MATCH (E1)
789338adb7d3d36da453113e98f371a4f92543cf2652b047f8481c407bed5bc3  STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md MATCH (PA)
5e49d2093d4ee17b840cc096d5caf3a6edafda4e37abbd175a7a371c34658f37  STAGE8_R_RECORD_L_FORM_FABLE_V001.md                                 MATCH (FORM)
f1881511c8a93cca3d8eb45f71b3be901cf337c9ce9321da0004901bfded6647  STAGE8_MIN_CARRIER_CANDIDATE_V001.md                                 MATCH (MIN-CARRIER)
```

The four anchor-certified E1 byte spans were recomputed by me from bytes and match
the anchor's span digests exactly:

```text
[24271,27553) 3215cca855623a09ef3a575d4c5ca716fa25c7f02ce00d3eb4f7fcf6eb228542  (C1/C2/C4/C6)
[33912,35504) 74568815cf886f2fe3285bde090ba8644d45222693407dad40292b4c6520fc49  (Dyson-dressed clause)
[44552,45695) b0281063f7ca4758ed38ac9f17990de8f5172febc73a7ab791fa718c9f4e61a6  (S1/S2)
[57212,58506) 162e30a6ccb77ae53fb9026ef6d4a675fb74cb899b1e21c6fbc4926225ae5fcf  (B-L2*)
```

Every line citation the re-analysis relies on was independently read at path and
matched: E1 :653-654 (V), :660-661 (Delta), :693-694/:1107-1108 (S1 trace),
:696-698 (two-time mandate; alpha exponent not asserted), :510-513 (Dyson-dressed),
:465-470 (sharp M(t), not softenable), :343-350 (C4 saturation; the summed
a-linear tadpole kill), :356-358 (C6 cell-time-integration clause), :565-569
(cancellation inventory), :672 (F'-14 log-of-sum), :687-689 (S2 sup over color
pairs on the surviving sector and the closed pair polydisc), :754 (V(0) = I
same-phase), :1056-1058/:1111-1116 (b_D Gevrey; B-L2 a-vertex "plausible"; record
vertex volume-diagonal locus); PA :79-80 (h_0, S_n), :86-88 (r, M, v), :100-113
(b_D, vanishing to all orders), :121-127 (J = -(Q b_D Q) tensor alpha_x; h_lambda),
:130-135 (fixed gauge, no covariance claimed), :140-141 (frozen pairs), :181-182
(u_lambda generated by h_lambda), :212-214 (R_pointer weight sum), :371-372
(Trotter interleaving); FORM :168-186 (D3 two-branch; diagonal flat), :277-281
(G3 ell unsupplied); CHECK :219-229, :352-360 (the longitudinal converse);
SYMHUNT §3.3-3.4 within anchor-certified span [5488,14492) (the surrogate symbol);
ANCHOR §5/§7 ("longitudinal terms not controlled by the B1 calculation"; "the
two-time re-analysis is owed"); MIN-CARRIER header ("CONDITIONAL THROUGHOUT:
candidate, NOT a physical carrier of record").

---

## 2. ATTACK 1 — EXPANSION FIDELITY: RE-DERIVED FROM THE SEALED SPANS. CONFIRMED.

I re-derived the first-order term from the sealed definitions alone, by hand, twice
(once directly, once through the cocycle refactoring), before comparing.

```text
Sealed inputs (verified at spans above):
  V_{mu lambda}(a) = u_mu(a_-)^dag u_lambda(a_+);  u_lambda(a) generated by
  h_lambda(t;a) = h_0 + lambda v(t) M(t) tensor S + a J(t), t in [0,1];
  J(t) = -(Q b_D(t,x) Q) tensor alpha_x, Hermitian (b_D real, Q and alpha_x
  Hermitian) — the a-dependence of h is LINEAR in a, so Duhamel in a is a clean
  power expansion.
Duhamel, exact:  u_lambda(a) = W_lambda(1,0)
  - i a int_0^1 W_lambda(1,t') J(t') W_lambda(t',0) dt' + O(a^2),
  W_lambda = the a = 0 propagator (unitary, cocycle W(1,0) = W(1,t')W(t',0)).
Zeroth order of V(a) is W_mu(1,0)^dag W_lambda(1,0) = V(0) exactly — so
  V(a) - V(0) starts at the first-order term. First order, my derivation:
  T_1 = -i a_+ int W_mu(1,0)^dag W_lambda(1,t') J(t') W_lambda(t',0) dt'
        + i a_- int W_mu(t',0)^dag J(t') W_mu(1,t')^dag W_lambda(1,0) dt'
  (the a_- term is the dagger of the a_- Duhamel correction; sign +i from (-i)^dag;
  J^dag = J). Cocycle refactoring: W_mu(1,0)^dag = W_mu(t',0)^dag W_mu(1,t')^dag
  and W_lambda(1,0) = W_lambda(1,t') W_lambda(t',0) give
  T_1 = -i int W_mu(t',0)^dag [a_+ G J - a_- J G] W_lambda(t',0) dt',
  G = G_{mu lambda}(t') = W_mu(1,t')^dag W_lambda(1,t').
IDENTICAL to the artifact's FIRST_ORDER_TERM, term by term, sign by sign.
Branch diagonal (mu = lambda, a_+ = a_-): G = I and the bracket collapses to
  (a_+ - a_-) W^dag J W = 0 — FORM D3's flatness reproduced; the response rides
  a_Delta = a_+ - a_-. CONFIRMED.
Record-stratum zero (all W -> e^{-i h_0 t}; G = I, hence pair-independent):
  T_1^{(0)} = -i a_Delta int e^{i h_0 t'} J(t') e^{-i h_0 t'} dt'
            = +i a_Delta int e^{i h_0 t'} b_D(t',x) alpha_x e^{-i h_0 t'} dt'
  (sign flip from J = -b_D alpha_x; Q transparent at principal symbol in the
  carrier interior). IDENTICAL to the artifact's display, including sign.
```

**Is it another idealization one level up?** NO. The lineage's twice-produced
failure mode was OBJECT-CLASS SUBSTITUTION (equal-time multiplication surrogate for
the two-time Dyson object). Here the two-time Dyson structure is the derivation's
own skeleton; the interleaving matches the sealed Trotter factorization [PA
:371-372] and the sealed Dyson-dressed clause [E1 :510-513]. The single
idealization-shaped step — Galerkin Q treated as transparent at principal-symbol
level in the carrier interior — is DECLARED in the artifact (§2 carrier note, §7
Galerkin caveat) and its quantitative consequence is precisely what
CARRIER_DEPENDENCE types carrier-sensitive. The record-stratum grading is a second
exact Dyson expansion in a bounded sealed vertex (v M tensor S bounded, S^2 = I);
strata are additive and the sharp strata are scoped, not smoothed.

**EXPANSION_FIDELITY = CONFIRMED.**

---

## 3. ATTACK 2 — THE CLIFFORD ALGEBRA, RE-DERIVED MY OWN WAY. MATCH (AND STRONGER).

By hand (each verified by CAS in §6, 22 checks, all True, my own construction — not
a re-run; the artifact's own §8 script was ALSO re-run verbatim and reproduces its
claimed nine-True output exactly):

```text
BAND TYPING (V2-V4): with M = alpha.k_hat, {alpha_x, alpha.k} = 2 k_x I gives
  (I-M)alpha_x(I-M) = alpha_x - 2k_hat_x I + (2k_hat_x M - alpha_x) = -2k_hat_x(I-M),
  i.e. P_- alpha_x P_- = -k_hat_x P_-, P_+ alpha_x P_+ = +k_hat_x P_+ — the
  longitudinal part k_hat_x M is EXACTLY the band-diagonal part; the transverse
  part alpha_x^perp ({M, alpha_x^perp} = 0) is EXACTLY the interband part.
  The claimed LONGITUDINAL_GENERATED is therefore real and honestly glossed by the
  artifact itself: the component is PRESENT in the sealed vertex from the start.
CONJUGATION (V5-V6): e^{iKt} = cos(|k|t)I + i sin(|k|t)M;
  e^{iKt} alpha_x e^{-iKt} = alpha_x^par + cos(2|k|t) alpha_x^perp
  + i sin(2|k|t) M alpha_x^perp — my expansion of (c+isM)A(c-isM) with MA = -AM
  reproduces it exactly; the interband pair {alpha^perp, M alpha^perp} is CLOSED
  under the conjugation (V5d) and tr = 0 for all t (V6a: NO scalar ever forms);
  the M-coefficient is k_hat_x independent of t (V6b: the longitudinal part rides
  through unrotated, nothing leaks).
THE DECISIVE POINTWISE CHECK (V7), my own and stronger than the artifact needs:
  P_- (e^{iKt'} alpha_x e^{-iKt'}) P_- = -k_hat_x P_-  IDENTICALLY IN t'.
  The sandwich isolates the intraband survivor at EVERY intermediate time; the
  oscillatory sector drops from the sandwiched object exactly, before any
  integration. Consequence: the survivor is independent of the Gevrey mechanism —
  the artifact's route (integrate, then sandwich) and mine (sandwich, then
  integrate) agree exactly, and the cell-time integration then multiplies the
  survivor by the transported profile int_0^1 b_D(t', x -+ t'k_hat) dt' =
  b_tilde(x,k_hat): degree 0, k-dependence through k_hat only, not identically
  zero (b_D > 0 on the open diamond — structural positivity, nothing evaluated).
ON-SHELL KINEMATICS (V12, symbolic series, no numbers): at fixed transfer q,
  |k+q| - |k| -> k_hat.q (bounded — intraband: Gevrey joint decay never engages);
  |k+q| + |k| -> infinity (interband: faster-than-any-power decay engages). The
  root-cause diagnosis (massless on-shell marginality) is exact.
WRONG-INTERLEAVING HUNT: negative. Both CTP branch terms contribute the SAME
  stratum-zero conjugation integral (G = I), combining to a_Delta; the a_- dagger
  chain was re-derived independently; the matrix-element form
  <k',-|T_1^{(0)}|k,-> = i a_Delta B_hat_D(|k'|-|k|, k'-k) u_-(k')^dag alpha_x u_-(k)
  re-derived (band eigenvalue -|k| gives phases e^{-i(|k'|-|k|)t'}; b_D supported
  in t' in (0,1) makes the [0,1] integral the full time transform), with
  u_-^dag alpha_x u_- -> -k_hat_x on the band (= V2). The survivor is not an
  artifact of ordering.
```

**SYMBOL_RERUN = MATCH** — sigma(T_1^{(0)}) = i a_Delta k_hat_x b_tilde(x,k_hat) M
+ O(|k|^{-infinity}), no scalar, no dropped term, correctly interleaved.

---

## 4. ATTACK 3 — SANDWICH AND DEGREE BOOKKEEPING, RE-RUN ON MY TERM. MATCH.

```text
SANDWICH: P_- M P_- = -P_- (V10, = CHECK's converse realized), so on my version of
  the term: sigma(C T_1^{(0)} C) = -i a_Delta k_hat_x b_tilde(x,k_hat) C(k)
  + O(|k|^{-infinity}) — sign chain re-derived and matching the artifact's.
INTERBAND: annihilated pointwise (V4b) AND O(|k|^{-infinity}) after integration —
  the surrogate mechanism survives STRENGTHENED on its own sector; correct.
INTERBAND IDENTITY: [P_-,[P_-, alpha^perp]] = alpha^perp (V9a) holds; on the
  survivor [P_-, k_hat_x M] = 0 (V9b) so A = [C,[C,A]] FAILS on it; correct.
DEGREES: k_hat_x b_tilde is homogeneous degree 0 in k — NOT degree <= -1; symbol
  composition corrections (commuting the smooth degree-0 factor through C(k))
  drop one degree, subleading — the verdict is stable against them.
HS: degree-0 symbol, x-support compact (b_tilde inherits b_D's compact support)
  => ||.||_2^2 integrates an O(1)-in-k density over the carrier's momentum range:
  finite ONLY on a fixed carrier, scaling with carrier momentum volume — the
  sealed C2 shape verbatim ("finite only on a fixed carrier, which spec-header
  scoping clause 1 forbids"). Carrier-uniformity failure shape: correct, and
  correctly NOT evaluated.
TRACE: tr[C(k) alpha_x] = -2 k_hat_x re-derived by hand and CAS (V8) — the sealed
  S1 identity; tr of the survivor = -2 i a_Delta k_hat_x b_tilde; S1's rescue
  re-derived: int d^3x b_tilde(x,k_hat) = int b_D dt d^3x is k_hat-independent by
  translation invariance, and the angular integral of the odd k_hat_x kills the
  trace — while the HS norm squares to the even |k_hat_x|^2 and nothing cancels.
  The sealed S1-fine / S2-wall split is reproduced exactly as the artifact says.
```

**SANDWICH_RERUN = MATCH.**

---

## 5. ATTACK 4 — SCOPE, AND ATTACK 5 — PROVENANCE/INJECTION

```text
SECOND ORDER: separability claim TRUE and in fact UNDER-ARGUED: the sealed S2
  quantifier includes the sup over the CLOSED PAIR POLYDISC [E1 :687-689], so the
  first-order coefficient in a is separated identically over a continuum of pairs,
  not merely at the two frozen nonzero-a_Delta pairs (whose a_Delta values are
  distinct and nonzero — structural, not evaluated). Strengthening note, not a
  correction: the FAILS verdict is decided at first order.
SHARP FACTOR: honestly scoped. Additive strata, sealed sharp [E1 :465-470], B-L2*
  volume-diagonal locus verified at bytes. My reinforcement: the record strata
  live OUTSIDE the smooth symbol class (power-law-tailed sharp-locus kernels), so
  an exact cancellation of the smooth degree-0 principal symbol would require the
  sharp strata to carry a matching smooth degree-0 component — nothing sealed
  supplies one, and C4's saturation runs the other way. Second strengthening note.
WEIGHT-SUMMED CAVEAT: correct and honest, and it RECONCILES the artifact with E1
  C4's own clause ("the bare a-linear tadpole vanishes identically" [:343-345]):
  that kill lives in the WEIGHT-SUMMED object (|sum_lambda w_lambda|^2 = |m_0|^2
  = 0), which is R_pointer's assembly [PA :212-214] — NOT the sealed S2 per-pair
  sup [E1 :687-689 verified at bytes: "sups over states, color pairs on the
  SURVIVING sector, and the closed pair polydisc"]. Per-pair, the pair-independent
  stratum-zero survivor stands for every surviving-sector pair; under summation
  the wall relocates to the sharp strata (B-L2*) and F'-14 [:672]. Exactly as the
  artifact states, at the claimed strength and no more.
NOT-COVERED LIST: verified real. No ell in the per-cell vertex (PA A2: J carries
  b_D only; FORM G3 :277-281: ell unsupplied, multi-cell datum); IR/boundary and
  post-limit genuinely untouched; gauge non-move correct (PA :130-135 claims no
  covariance; the survivor's non-pure-gauge parenthetical is structural
  positivity only).
CARRIER_DEPENDENCE: split verified line by line: everything in §3-§5 above is
  continuum symbol algebra (carrier-light, unchanged on K_dd); the HS meaning of
  the survivor and multi-cell assembly are carrier-sensitive; MIN-CARRIER's
  "CONDITIONAL THROUGHOUT" status preserved, not upgraded.
NET FOLLOWS: the annihilation does not extend, the failure is exhibited as a
  term, the mechanism's survival on its own sector is stated, and nothing
  stronger is claimed (no R-L2b death claim, no evaluated magnitude). The verdict
  follows from the algebra shown, at the claimed strength.

PROVENANCE: 7/7 source seals + the artifact's own digest recomputed at path and
  matching sidecars and tasked digests; the anchor's four E1 span digests
  recomputed byte-exactly (§1); every cited line span read at path. CLEAN.
INJECTION: scanned the artifact and all sources for directive-shaped content
  aimed at a verifier (ignore/disregard/skip-verification/report-X patterns):
  NONE found. The sealed files' BLOCKS/witness clauses are program governance,
  not injection. The tasked flag block is an ASCII-normalized transcription of
  the artifact's §10 flag block with no material discrepancy (checked field by
  field against the sealed bytes; the sealed bytes are the authority).
FORBIDDEN-IMPORT AUDIT OF THE ARTIFACT: no number computed, bounded, or
  evaluated anywhere in it; the two borderline-looking items (b_D positivity;
  frozen-pair distinctness) are structural parities/distinctness facts, not
  evaluations. Its §8 script re-run verbatim: output matches its in-artifact
  transcript exactly, and contains nothing numeric. Its disclosed first-run
  C4/C8 process note is consistent with the corrected script's content. CLEAN.
```

---

## 6. MY SCRIPT (exact symbolic; reproduced in full) AND ITS OUTPUT

Run with sympy 1.14.0 in a fresh venv. My own construction (normalized projectors,
sector closure, pointwise sandwich, trace, kinematic limits) — not a re-run of the
artifact's script. The artifact's §8 script was additionally extracted from the
sealed bytes and run verbatim: its output reproduced its in-artifact transcript
exactly (nine True).

```python
# TWO-TIME-CHECK: independent adversarial re-derivation (my own construction,
# NOT a re-run of the artifact's script). EXACT SYMBOLIC ONLY: polynomial/trig
# identities over symbols and one symbolic large-|k| series; nothing numeric,
# no physical quantity evaluated.
import sympy as sp

I2 = sp.eye(2); Z2 = sp.zeros(2, 2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])

def alpha(s):  # Dirac alpha_j in the chiral-block form [[0,s],[s,0]]
    return sp.Matrix(sp.BlockMatrix([[Z2, s], [s, Z2]]).as_explicit())

ax, ay, az = alpha(sx), alpha(sy), alpha(sz)
I4 = sp.eye(4)

kx, ky, kz, lx, ly, t = sp.symbols('kx ky kz lx ly t', real=True)
w = sp.symbols('w', positive=True)     # |k|; relation w^2 = kx^2+ky^2+kz^2 by substitution
n2 = kx**2 + ky**2 + kz**2

K  = kx*ax + ky*ay + kz*az             # symbol of h_0
M  = K/w                               # alpha.k_hat
Pm = (I4 - M)/2                        # sea-band projector C(k)  (E1 C1)
Pp = (I4 + M)/2

def Z(Mx):
    Mx = sp.expand(Mx)
    for _ in range(3):
        Mx = sp.expand(Mx.subs(w**2, n2))
    Mx = sp.simplify(sp.expand(sp.expand_trig(Mx)))
    for _ in range(3):
        Mx = sp.expand(Mx.subs(w**2, n2))
    Mx = sp.simplify(Mx)
    return Mx == sp.zeros(*Mx.shape)

def Zs(e):  # scalar zero test
    e = sp.expand(sp.expand_trig(sp.expand(e)))
    for _ in range(3):
        e = sp.expand(e.subs(w**2, n2))
    return sp.simplify(e) == 0

apar  = (kx/w) * M                     # longitudinal part k_hat_x (alpha.k_hat)
aperp = ax - apar                      # transverse part

# V1 projector algebra (normalized, my own path)
print("V1a P_-^2 = P_-                              :", Z(Pm*Pm - Pm))
print("V1b P_- P_+ = 0                              :", Z(Pm*Pp))
print("V1c P_- Hermitian                            :", Z(Pm - Pm.H))
# V2/V3 band typing (normalized)
print("V2  P_- ax P_- = -(kx/w) P_-                 :", Z(Pm*ax*Pm + (kx/w)*Pm))
print("V3  P_+ ax P_+ = +(kx/w) P_+                 :", Z(Pp*ax*Pp - (kx/w)*Pp))
# V4 exact sector typing: longitudinal = band-diagonal, transverse = interband
print("V4a P_+ apar P_- = 0 and P_- apar P_+ = 0    :", Z(Pp*apar*Pm) and Z(Pm*apar*Pp))
print("V4b P_- aperp P_- = 0 and P_+ aperp P_+ = 0  :", Z(Pm*aperp*Pm) and Z(Pp*aperp*Pp))
# V5 Heisenberg conjugation, derived my way: U = e^{iKt} = cos(wt) + i sin(wt) M
c, s = sp.cos(w*t), sp.sin(w*t)
U  = c*I4 + sp.I*s*M
Ud = c*I4 - sp.I*s*M
print("V5a U unitary (U Ud = I)                     :", Z(U*Ud - I4))
conj = U*ax*Ud
print("V5b U apar Ud = apar (rides through)          :", Z(U*apar*Ud - apar))
print("V5c U aperp Ud = cos(2wt) aperp + i sin(2wt) M aperp :",
      Z(U*aperp*Ud - (sp.cos(2*w*t)*aperp + sp.I*sp.sin(2*w*t)*M*aperp)))
print("V5d interband sector closes (U (M aperp) Ud = cos(2wt) M aperp + i sin(2wt) aperp) :",
      Z(U*(M*aperp)*Ud - (sp.cos(2*w*t)*(M*aperp) + sp.I*sp.sin(2*w*t)*aperp)))
# V6 no scalar, longitudinal coefficient constant in t
print("V6a tr[U ax Ud] = 0 for all t (no scalar)    :", Zs(conj.trace()))
print("V6b (1/4) tr[M U ax Ud] = kx/w for all t     :", Zs(sp.Rational(1,4)*(M*conj).trace() - kx/w))
# V7 THE DECISIVE SANDWICH: pointwise in t, the whole conjugated vertex sandwiches
#    to the longitudinal survivor alone — the oscillatory sector drops for ALL t.
print("V7  P_- (U ax Ud) P_- = -(kx/w) P_-  ALL t   :", Z(Pm*conj*Pm + (kx/w)*Pm))
# V8 the sealed S1 trace identity re-derived
print("V8  tr[C(k) ax] = -2 kx/w                    :", Zs((Pm*ax).trace() + 2*kx/w))
print("V8b tr[P_-] = 2                              :", Zs(Pm.trace() - 2))
# V9 interband double-commutator identity holds on aperp, FAILS on the survivor
print("V9a [P_-,[P_-, aperp]] = aperp               :", Z(Pm*(Pm*aperp - aperp*Pm) - (Pm*aperp - aperp*Pm)*Pm - aperp))
print("V9b [P_-, kx/w M] = 0 (so [C,[C,A_par]] = 0 != A_par) :", Z(Pm*((kx/w)*M) - ((kx/w)*M)*Pm))
# V10 the check-file converse, normalized: P_- M P_- = -P_-
print("V10 P_- M P_- = -P_-                         :", Z(Pm*M*Pm + Pm))
# V11 surrogate contrast: transverse ell sandwiches to zero (k.l = 0 imposed)
lz = -(kx*lx + ky*ly)/kz
L = lx*ax + ly*ay + lz*az
print("V11 P_- (alpha.l_perp) P_- = 0               :", Z(Pm*L*Pm))
# V12 on-shell kinematics (symbolic series; no numbers): k = K e3, transfer q
Ksym, qx, qy, qz = sp.symbols('Ksym qx qy qz', positive=True)
om_intra = sp.sqrt((Ksym+qz)**2 + qx**2 + qy**2) - Ksym       # |k+q| - |k|
om_inter = sp.sqrt((Ksym+qz)**2 + qx**2 + qy**2) + Ksym       # |k+q| + |k|
lim_intra = sp.limit(om_intra, Ksym, sp.oo)
lim_inter = sp.limit(om_inter, Ksym, sp.oo)
print("V12a intraband omega -> k_hat.q (= qz), BOUNDED :", sp.simplify(lim_intra - qz) == 0)
print("V12b interband omega -> infinity               :", lim_inter == sp.oo)
```

Output, verbatim:

```text
V1a P_-^2 = P_-                              : True
V1b P_- P_+ = 0                              : True
V1c P_- Hermitian                            : True
V2  P_- ax P_- = -(kx/w) P_-                 : True
V3  P_+ ax P_+ = +(kx/w) P_+                 : True
V4a P_+ apar P_- = 0 and P_- apar P_+ = 0    : True
V4b P_- aperp P_- = 0 and P_+ aperp P_+ = 0  : True
V5a U unitary (U Ud = I)                     : True
V5b U apar Ud = apar (rides through)          : True
V5c U aperp Ud = cos(2wt) aperp + i sin(2wt) M aperp : True
V5d interband sector closes (U (M aperp) Ud = cos(2wt) M aperp + i sin(2wt) aperp) : True
V6a tr[U ax Ud] = 0 for all t (no scalar)    : True
V6b (1/4) tr[M U ax Ud] = kx/w for all t     : True
V7  P_- (U ax Ud) P_- = -(kx/w) P_-  ALL t   : True
V8  tr[C(k) ax] = -2 kx/w                    : True
V8b tr[P_-] = 2                              : True
V9a [P_-,[P_-, aperp]] = aperp               : True
V9b [P_-, kx/w M] = 0 (so [C,[C,A_par]] = 0 != A_par) : True
V10 P_- M P_- = -P_-                         : True
V11 P_- (alpha.l_perp) P_- = 0               : True
V12a intraband omega -> k_hat.q (= qz), BOUNDED : True
V12b interband omega -> infinity               : True
```

---

## 7. FLAG BLOCK

```text
EXPANSION_FIDELITY = CONFIRMED(the first-order term is the sealed object's own,
  re-derived independently from E1 :653-654/:510-513 and PA :121-127/:181-182/
  :371-372: T_1 = -i int W_mu(t',0)^dag [a_+ G J - a_- J G] W_lambda(t',0) dt'
  exactly, branch-diagonal flat (FORM D3), stratum zero pair-independent with the
  artifact's sign; NOT the lineage's object-class substitution — the two-time
  Dyson structure is the derivation's skeleton; the single idealization-shaped
  step (Galerkin Q transparent at principal symbol, carrier interior) is declared
  in the artifact and correctly typed carrier-sensitive.)

SYMBOL_RERUN = MATCH(sigma(T_1^{(0)}) = i a_Delta k_hat_x b_tilde(x,k_hat)
  alpha.k_hat + O(|k|^{-infinity}) — re-derived by hand and by my own 22-check CAS
  construction (all True; artifact's own nine-identity script also re-run verbatim,
  output reproduced exactly). LONGITUDINAL_GENERATED verified real, not a wrong
  interleaving: both CTP branches feed the same stratum-zero conjugation; no
  scalar forms at any t (tr = 0 identically); the longitudinal coefficient is
  t-independent; STRENGTHENED: P_-(e^{iKt'} alpha_x e^{-iKt'})P_- = -k_hat_x P_-
  POINTWISE in t' — the survivor is isolated by the sandwich before any Gevrey
  argument, which is needed only for the un-sandwiched interband remnant.)

SANDWICH_RERUN = MATCH(sigma(C T_1^{(0)} C) = -i a_Delta k_hat_x b_tilde(x,k_hat)
  C(k) + O(|k|^{-infinity}); degree 0, intraband, scalar on the sea band; the
  CHECK converse (I-M)M(I-M) = -2(I-M) realized; A = [C,[C,A]] fails on the
  survivor ([C, A_par] = 0); trace = -2 i a_Delta k_hat_x b_tilde consistent with
  the sealed S1 identity tr_spinor[C(p) alpha_x] = -2 p_hat_x, re-derived; S1's
  oddness rescue and its non-transfer to the squared HS both re-derived; HS-norm^2
  carrier-momentum-volume scaling shape (C2 Lambda^3) verified as shape only;
  interband remnant faster than any power — degree bookkeeping matches.)

SCOPE = EXACT(no corrections; two strengthening notes: (i) order separability is
  grounded even more strongly by the sealed closed-pair-polydisc quantifier
  [E1 :687-689] than by the frozen pair family; (ii) the sharp record strata lie
  outside the smooth symbol class, so cancelling the smooth degree-0 survivor
  would require a sealed smooth degree-0 record component — none exists. The
  weight-summed caveat correctly reconciles E1 C4's summed a-linear tadpole kill
  (|m_0|^2 = 0, R_pointer assembly) with the sealed PER-PAIR S2 sup where the
  survivor stands; carrier split correct; MIN-CARRIER conditionality preserved;
  NET follows from the algebra shown at the claimed strength and no more.)

TT_VERDICT = CONFIRMED(NET = FAILS(the term -i a_Delta k_hat_x b_tilde(x,k_hat)
  C(k), degree 0, carrier-scaling HS, at the sealed per-pair S2 quantifier): the
  equal-time annihilation does not extend to the sealed two-time vertex; the
  annihilation mechanism survives strengthened on the interband sector; the
  failure is the band-diagonal sector of alpha_x, deleted by the surrogate's
  object class; root cause massless on-shell marginality — my V12 symbolic limits
  confirm bounded intraband vs divergent interband energy transfer.)

PROVENANCE = CLEAN(7/7 source seals + the artifact digest 18af3dee recomputed at
  path, all matching sidecars and tasked digests; the anchor's four E1 byte-span
  digests recomputed byte-exactly; every relied-on line span read at path; none
  unverifiable.)

INJECTION = none(directive-pattern scan of the artifact and all six sources:
  clean; sealed BLOCKS/witness clauses are program governance, not injection;
  tasked flag block is a faithful ASCII normalization of the artifact's sealed
  flag block — no material discrepancy, sealed bytes taken as authority.)

MACHINERY_USED_BY_ME = yes(exact symbolic CAS only — sympy 1.14.0 in a fresh
  venv: my own 22-check script (§6, reproduced verbatim with output) plus a
  verbatim re-run of the artifact's §8 script (output matches its transcript
  exactly); shasum/sed/grep/python byte-extraction otherwise; NOTHING numeric —
  no value of n, kappa_record, alpha, any exponent, norm, scale, or spectrum
  computed, bounded, estimated, or evaluated.)

alpha_computed = false ; kappa_record_computed = false ; proof_authorized = false ;
coupling_evaluation_authorized = false
ALL_RESULTS = CLAIMED until checked.
TWO_TIME_CHECK_RESULT = SEALED.
```
