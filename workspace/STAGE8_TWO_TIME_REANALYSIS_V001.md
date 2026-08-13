# STAGE 8 — TWO-TIME RE-ANALYSIS: DOES THE PROJECTOR-SANDWICH ANNIHILATION SURVIVE ON THE SEALED TWO-TIME DYSON-DRESSED VERTEX?

## BLIND ANALYST — CODENAME TWO-TIME — [SEALED]

Date: 2026-08-13
Role: BLIND analyst (TWO-TIME). This artifact is the load-bearing re-analysis the
external anchor demanded (anchor §5/§7: "the two-time re-analysis is owed"). Road
step 3: determine whether the CONFIRMED equal-time-surrogate annihilation
((I-M)(alpha.ell_perp)(I-M) = 0 at principal symbol; post-annihilation degree <= -1)
SURVIVES on the sealed two-time object V_{mu lambda}(a) = u_mu(a_-)^dagger u_lambda(a_+)
with Dyson-dressed vertex J = -(Q b_D Q) tensor alpha_x interleaved with free h_0
propagation.

Gates: `alpha_computed = false` ; `kappa_record_computed = false` ;
`proof_authorized = false` ; `coupling_evaluation_authorized = false`
ALL_RESULTS = CLAIMED until checked.

Fences held: EXACT SYMBOLIC ALGEBRA ONLY — operator/Clifford/Fourier symbol algebra
on sealed forms; Dyson/Duhamel expansions kept symbolic; the one script used is exact
symbolic CAS verification of Clifford identities (polynomial/trig identities over
symbols — nothing numeric), reproduced in full in §8. NO value of n, kappa_record,
alpha (coupling), any exponent, norm, scale, length, or spectrum computed, bounded,
or evaluated; sealed constants carried verbatim. No scale, imported GR, or
faithfulness used as authority; scale-bearing sealed text read SUSPECT-ONLY to fix
structure (the sea kernel's form read to analyze structure, never evaluated). No
register/tracker/plan/road/ledger/lens file read. Output name probed before write:
ABSENT. No git action.

---

## 0. VERDICT IN ONE LINE

**NET = FAILS(the term). The annihilation does NOT survive on the sealed two-time
object. The annihilation MECHANISM (interband => sandwich-zero) survives — in fact it
is STRENGTHENED on the two-time object: the Gevrey cell-time integration suppresses
the entire interband (transverse + bivector) sector faster than any power of |k|. But
the sealed vertex alpha_x possesses, at every k with k_x != 0, a LONGITUDINAL =
BAND-DIAGONAL component k_hat_x (alpha.k_hat) that the frozen equal-time surrogate
did not contain at all. That component commutes with the h_0 symbol, rides through
the free propagators unrotated, receives NO decay from the cell-time integration (its
phase is non-oscillatory), and survives the sandwich as an INTRABAND scalar on the
sea band: at principal-symbol level, at first order in a_Delta = a_+ - a_-,**

```text
sigma( C[V(a) - V(0)]C )(x,k) = -i a_Delta k_hat_x b_tilde(x, k_hat) C(k)
                                 + O(|k|^{-infinity}) interband remnants
                                 + record-dressed strata (scoped, §6)
                                 + one-degree-down symbol corrections,
b_tilde(x, k_hat) = int_0^1 b_D(t', x - t' k_hat) dt'   (diamond profile averaged
                                                         along the sea-band ray),
```

**degree 0 in k — NOT annihilated, NOT degree <= -1, NOT locally HS at any negative
order carrier-blindly. Its spinor trace is the sealed S1 identity
tr_spinor[C(p) alpha_x] = -2 p_hat_x (E1 :693-694, :1107-1108): the sealed record
itself already carries the nonvanishing of C alpha_x C — the trace is saved only by
oddness under the angular k-integration, never by the sandwich being zero. The
surrogate's transversality was an artifact of its object class (covariance
conjugation manufactures the unit-vector derivative ell_perp), not a feature of the
sealed vertex.**

---

## 1. SEALS VERIFIED AT PATH (shasum -a 256), BEFORE ANY RELIANCE

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`. Every digest below
recomputed from bytes at path THIS session and matched both the sidecar seal and the
tasked digest. None unverifiable.

```text
48e0c76fc3c8bb2f2c288e8d5be91240a7383181585f7315ef2b9b7e8f46f0f2  STAGE8_ANNIH_ANCHOR_CODEX2_V001.md                                  MATCH (ANCHOR)
7cf16a3c9cb829b3c4d5a9ac2c8996897b1268e7d1e4f18d510e0ba4ce0b9c95  STAGE8_ANNIHILATION_CHECK_V001.md                                   MATCH (CHECK)
564b7040bf51da4e7aec5b00d940b5e0215a9327ebbb2cd04947c568f8c9ae50  STAGE8_CANC_PANEL_SYMHUNT_V001.md                                   MATCH (SYMHUNT)
468467303a109dc825b015107897dacc107800fc981030377c3f006b384cccb5  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md                         MATCH (E1)
789338adb7d3d36da453113e98f371a4f92543cf2652b047f8481c407bed5bc3  STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md MATCH (PA)
5e49d2093d4ee17b840cc096d5caf3a6edafda4e37abbd175a7a371c34658f37  STAGE8_R_RECORD_L_FORM_FABLE_V001.md                                MATCH (FORM)
f1881511c8a93cca3d8eb45f71b3be901cf337c9ce9321da0004901bfded6647  STAGE8_MIN_CARRIER_CANDIDATE_V001.md                                MATCH (MIN-CARRIER)
```

The four E1 byte spans the anchor certified ([24271,27553) C1/C6; [33912,35504)
Dyson-dressed clause; [44552,45695) S1/S2; [57212,58506) B-L2*) were re-extracted
from bytes this session; content quoted below is from those extractions and from
line-addressed reads of the same sealed file.

---

## 2. THE SEALED TWO-TIME OBJECT, ASSEMBLED AT SPANS (every structural ingredient)

```text
(i)    THE OBJECT. Per admitted cell C, per record-color pair (mu, lambda), per CTP
       pair on the closed pair polydisc:
           V_{mu lambda}(a) := u_mu^{(c)}(a_-)^dagger u_lambda^{(c)}(a_+)      [E1 :653-654]
           Delta_{mu lambda}(a) := C(V(a) - V(0))C                              [E1 :660-661]
(ii)   THE GENERATOR. u_lambda(a) is "the one-particle propagator generated by
       h_lambda(t;a)" [PA :181-182], with
           h_lambda(t;a) = h_0 + lambda v(t) M(t) tensor S + a J(t)            [PA :124-127]
           h_0 = sum_j p_j tensor alpha_j            (massless Dirac)          [PA :79]
           S = S_n = -i slash(n) gamma^5, S^2 = I                              [PA :80; E1 :347]
(iii)  THE a-VERTEX (smooth factor). J(t) = -(Q b_D(t,x) Q) tensor alpha_x
       [PA :121-122; E1 :1111], with b_D(t,x) = exp(16 - 1/s(t,x)) on the open unit
       causal diamond, zero outside; C-infinity, compactly supported in the closed
       diamond, "vanishes to all orders at its boundary and tips" [PA :100-113];
       "b_D = exp(16 - 1/s) (vanishing to all orders at the diamond boundary and
       both tips, ||b_D||_inf = 1 exactly)" [E1 :1056-1058]; "b_D Gevrey, all
       derivatives vanishing at boundary and tips, so its spacetime transform decays
       faster than any power" [E1 :1111-1113].
(iv)   THE RECORD VERTEX (sharp factor). M(t) = Q 1_{|x| <= r(t)} Q,
       r(t) = min(t, 1-t), v(t) = tau_R 32 r(t)^3 — SEALED SHARP, not softenable
       [E1 :465-470; PA :86-88]. "M(t) is a SHARP indicator and by C4 the pointer
       weights put it in the LEAD at full tau_R (sum_lambda w_lambda u_lambda = P).
       The locus is the VOLUME DIAGONAL (C6 refinement)" [E1 :1114-1116].
(v)    THE SEA PROJECTOR. C = 1_(-inf,0)(h_0), C(p) = (I - alpha.p_hat)/2,
       C(r) = (1/2)delta^3(r) I - i alpha.r/(2 pi^2 |r|^4) [E1 C1, bytes
       [24271,...)]. Exact projector: CONFIRMED of record (anchor §2; check §2).
(vi)   THE TWO-TIME MANDATE. "MUST be a TWO-TIME (cell-S-matrix) object; the
       equal-time version is FALSE by C6" [E1 :696-698]; "Y_2 Y_1 = 0 holds only in
       the strict equal-time multiplication-operator idealization with disjoint
       supports; the actual V_i - 1 are Dyson-dressed by free h_0 propagation over
       the whole interval" [E1 :510-513].
(vii)  THE BRANCH STRUCTURE. The connection response is carried by the
       difference-branch combination a_Delta = a_+ - a_- of the two-branch CTP
       algebra; the response is FLAT on the branch diagonal [FORM D3, :168-186].
       Frozen pairs (a_+, a_-) in {(0,0), (7/100,-11/100), (13/100,4/100)} [PA :140-141].
       Same-phase sector baseline: V(0) = I exactly [E1 :754].
(viii) THE SEALED CANCELLATION INVENTORY. "CTP/Moebius kills DISCONNECTED terms
       ONLY; the spinor-odd trace and m_0 = m_1 = 0 are SATURATED at full tau_R
       (C4); TIME-INTEGRATION SMOOTHING IS THE ONLY REMAINING SUMMABILITY SOURCE"
       [E1 :565-569]. S1's trace kill: "odd spinor trace
       tr_spinor[C(p) alpha_x] = -2 p_hat_x, and |m_0|^2 = 0" [E1 :693-694, :1107-1108].
(ix)   THE SURROGATE OF RECORD (for contrast only; REFUTED as an anchor for this
       object): leading symbol D_hat(k) = (n/(2|k|)) alpha.ell_perp, purely
       transverse, sandwiched to zero exactly [SYMHUNT §3.3-3.4, within
       anchor-certified span [5488,14492); CHECK §3-4; ANCHOR §3-4]. The check's own
       converse, load-bearing here: "longitudinal: (I-M)(M)(I-M) = -2(I-M) != 0"
       [CHECK :219-229, :352-360].
```

Carrier note, used throughout: at principal-symbol level the Galerkin compression Q
is transparent in the interior of the carrier's momentum range; h_0's symbol is
alpha.k. Where the carrier matters it is said explicitly (§7).

---

## 3. STEP 1 — THE EXACT FIRST-ORDER TWO-TIME TERM

Write W_lambda(t,s) for the a = 0 propagator of h_lambda(t;0) = h_0 +
lambda v(t) M(t) tensor S from time s to time t (unitary; cocycle
W(1,0) = W(1,t')W(t',0)). Duhamel/Dyson to first order in the vertex J on each CTP
branch, exactly:

```text
u_lambda(a) = W_lambda(1,0) - i a int_0^1 W_lambda(1,t') J(t') W_lambda(t',0) dt' + O(a^2).
```

Substituting into V_{mu lambda}(a) = u_mu(a_-)^dagger u_lambda(a_+) and using
J(t')^dagger = J(t') (b_D real, Q and alpha_x Hermitian):

```text
FIRST-ORDER TERM, EXACT (the leading a-dependent term):

T_1 = -i a_+ int_0^1 W_mu(1,0)^dagger W_lambda(1,t') J(t') W_lambda(t',0) dt'
      +i a_- int_0^1 W_mu(t',0)^dagger J(t') W_mu(1,t')^dagger W_lambda(1,0) dt'

    = -i int_0^1 W_mu(t',0)^dagger [ a_+ G_{mu lambda}(t') J(t')
                                    - a_- J(t') G_{mu lambda}(t') ] W_lambda(t',0) dt',

G_{mu lambda}(t') := W_mu(1,t')^dagger W_lambda(1,t')   (unitary future-mismatch
                                                         factor; = I when mu = lambda).
```

This is free-plus-record propagation interleaving the smooth vertex at the
intermediate time t', integrated over the cell interval — exactly the structure the
sealed bytes demand [E1 :510-513, :696-698; PA :371-372's Trotter factors
F = exp[-i h_0 dt/2], A = exp[-i a J(t_k) dt/2] are the same interleaving].

**Exact structural checks.**

```text
(a) BRANCH-DIAGONAL FLATNESS (FORM D3 reproduced). At mu = lambda, a_+ = a_- = a:
    both integrands collapse by unitarity+cocycle to W(t',0)^dagger J(t') W(t',0),
    so T_1 = 0 EXACTLY — the response is flat on the branch diagonal and is carried
    by a_Delta = a_+ - a_-, exactly FORM D3's derived structure. At mu = lambda:
        T_1 = -i a_Delta int_0^1 W_lambda(t',0)^dagger J(t') W_lambda(t',0) dt'.
(b) RECORD-STRATUM GRADING. Expanding each W in the record vertex
    lambda v(t)M(t) tensor S grades T_1 by the number of sharp-record insertions.
    The stratum with ZERO record insertions (W -> e^{-i h_0 t}) is
        T_1^{(0)} = +i a_Delta int_0^1 e^{+i h_0 t'} b_D(t',x) alpha_x e^{-i h_0 t'} dt'
    (sign: J = -b_D alpha_x), and is the SAME for every color pair (mu, lambda),
    since the mu/lambda-dependence enters ONLY through the record vertex
    (G_{mu lambda} = I at stratum zero). The record-dressed strata are additive
    separate terms carrying at least one sharp M(t) insertion; they are scoped in
    §6, not silently smoothed — M(t) is sealed sharp [E1 :465-470].
```

`T_1^{(0)}` is the two-time analogue of the surrogate's leading term: it is where
the annihilation question lives in the smooth symbol category.

---

## 4. STEP 2 — THE PRINCIPAL SYMBOL: THE CLIFFORD ALGEBRA, WORKED EXACTLY

Let K = alpha.k (the h_0 symbol), |k| = w, M = alpha.k_hat = K/w, band projectors
P_± = (I ± M)/2, C(k) = P_-. Decompose the vertex Clifford generator at each k:

```text
alpha_x = alpha_x^par + alpha_x^perp,
alpha_x^par  := k_hat_x (alpha.k_hat) = k_x K/|k|^2    (LONGITUDINAL part),
alpha_x^perp := alpha_x - alpha_x^par = alpha.(e_x - k_hat k_hat_x)  (TRANSVERSE part).
```

**4.1 The band-typing identity (the crux, and the reversal of the surrogate).**
By {alpha_x, K} = 2 k_x I (verified exactly, §8 C2):

```text
P_- alpha_x P_- = -k_hat_x P_-,   P_+ alpha_x P_+ = +k_hat_x P_+,
P_+ alpha_x P_- + P_- alpha_x P_+ = alpha_x^perp.

=> THE LONGITUDINAL PART OF alpha_x IS EXACTLY ITS BAND-DIAGONAL (INTRABAND) PART;
   THE TRANSVERSE PART IS EXACTLY ITS INTERBAND PART.
```

(Verified exactly at the unnormalized level: (wI-K) alpha_x (wI-K) = -2 k_x (wI-K),
§8 C3 — equivalently C alpha_x C = -k_hat_x C, an exact operator identity pointwise
in k.) The surrogate's symbol alpha.ell_perp was purely transverse = purely
interband, hence sandwiched to zero. The sealed vertex alpha_x is NOT transverse: at
every k with k_x != 0 it carries the intraband component k_hat_x M. Nothing in the
two-time structure removes it — the question is only what the propagators and the
time integration do to each part.

**4.2 The Heisenberg conjugation — exact.** Since K^2 = |k|^2 I (§8 C1),
e^{iKt} = cos(|k|t) I + i sin(|k|t) M, and (verified exactly, §8 C5):

```text
e^{+iKt'} alpha_x e^{-iKt'} = alpha_x^par                              (NO rotation)
                              + cos(2|k|t') alpha_x^perp               (interband,
                              + i sin(2|k|t') M alpha_x^perp            oscillating
                                                                        at 2|k|).
```

The longitudinal/intraband part COMMUTES through the propagators unchanged. The
transverse part is rotated at frequency 2|k| into the vector+bivector interband pair
(both anticommute with M — verified, §8 C7a/C7b — hence both are interband and both
are killed by the sandwich pointwise). NO SCALAR (identity) component is generated
at any t': the conjugated symbol stays in span{alpha-vector, M.alpha^perp-bivector}
— the anticommutator {alpha_x, K} = 2 k_x I enters not as a scalar term in the
symbol but as the coefficient of the longitudinal projection.

**4.3 The cell-time integration — where two-time-ness acts, and where it does not.**
The stratum-zero symbol requires int_0^1 dt' b_D(t', x_transported) x (the above).
Band-block by band-block (Egorov: intraband blocks transport x along the band ray at
speed 1; the corrections drop one symbol degree per order — b_D is Gevrey-smooth, so
the smooth calculus applies on this stratum):

```text
INTERBAND BLOCKS (the transverse+bivector sector): time phase e^{±2i|k|t'} with
  d(phase)/dt' = ±2|k| != 0 — no stationary point; amplitude b_D(., x_transported)
  smooth, compactly supported in t', ALL t'-derivatives vanishing at the endpoints
  of its support [PA :110-113; E1 :1056-1058]. Repeated integration by parts:
  O(|k|^{-N}) for every N — the interband sector decays FASTER THAN ANY POWER of
  |k| after the cell-time integration. This is E1 B-L2's Gevrey clause [:1111-1113]
  made precise — and it is the two-time mechanism (C6: "the cell time integration
  supplies the missing decay") WORKING, on this sector.
INTRABAND BLOCKS (the longitudinal sector): time phase identically 1 — the
  integrand is NON-OSCILLATORY. The integration supplies NO decay in |k|:
      int_0^1 b_D(t', x - t' k_hat) dt' =: b_tilde(x, k_hat)
  (transport sign per band-flow convention; the choice moves x along ±k_hat and
  does not affect any conclusion), a smooth function, bounded, compactly supported
  in x, homogeneous of degree 0 in k (depends on k through k_hat only), and NOT
  identically zero: b_D > 0 on the open diamond, so b_tilde > 0 wherever the ray
  crosses the diamond.
```

**Equivalent exact matrix-element form (no symbol calculus needed).** On sea-band
plane-wave states |k,-> (h_0 eigenvalue -|k|):

```text
<k',-| (V(a)-V(0)) |k,-> = i a_Delta B_hat_D(|k'|-|k|, k'-k) u_-(k')^dagger alpha_x u_-(k)
                           + (record strata) + O(a^2),
```

with B_hat_D the spacetime Fourier transform of b_D and u_-(k')^dagger alpha_x u_-(k)
-> -k_hat_x I_2 as k' -> k (the band-typing identity, 4.1). The ON-SHELL kinematics
of the MASSLESS dispersion is the decisive fact: at fixed transfer q = k' - k, the
energy transfer is omega = |k'| - |k| = k_hat.q + O(|q|^2/|k|) — BOUNDED, |omega| <=
|q|, as |k| -> infinity. So the faster-than-any-power decay of B_hat_D in (omega, q)
JOINTLY never engages along the energy shell: B_hat_D(k_hat.q, q) is O(1) in |k| at
fixed q. (Contrast a quadratic dispersion, where omega ~ |k||q| grows and the smooth
vertex is harmless: the failure below is strictly a massless/relativistic on-shell
marginality — both bands move at speed 1.) The interband element carries
omega = |k'| + |k| -> infinity instead, which is why IT decays faster than any power.

**4.4 Answer to the crux question.** The propagators commute through ONLY on the
longitudinal sector — which the surrogate did not possess — and rotate-and-kill the
transverse sector that the surrogate consisted of. Principal symbol of the
stratum-zero first-order term after the cell-time integration:

```text
sigma(T_1^{(0)})(x,k) = i a_Delta k_hat_x b_tilde(x,k_hat) M(k) + O(|k|^{-infinity}),
```

purely LONGITUDINAL (band-diagonal), degree 0. No scalar component. PRINCIPAL_SYMBOL
= LONGITUDINAL_GENERATED — with the precise statement: the longitudinal component is
present in the sealed vertex alpha_x from the start (the surrogate's ell_perp
structure never forms on this object class), is preserved exactly by the free
propagation ({alpha_x, alpha.k} = 2k_x: the anticommutator IS twice the longitudinal
projection coefficient), and is made DOMINANT by the cell-time integration, which
suppresses everything else faster than any power.

---

## 5. STEP 3 — THE SANDWICH: WHAT SURVIVES, WITH EXACT DEGREE BOOKKEEPING

Apply C(.)C = P_-(.)P_- at principal-symbol level (b_tilde is a smooth scalar
factor; commuting it through C(k) costs one symbol degree, subleading):

```text
INTERBAND SECTOR: annihilated pointwise by the sandwich — (I-M)alpha_x^perp(I-M) = 0
  and (I-M)(M alpha_x^perp)(I-M) = 0 (both anticommute with M; §8 C6/C7) — AND
  already suppressed to O(|k|^{-infinity}) by §4.3. On this sector the surrogate's
  annihilation SURVIVES AND IS STRENGTHENED (surrogate: one-degree drop; two-time:
  faster than any power).
INTRABAND SECTOR: NOT annihilated. P_- M P_- = -P_-, so

  sigma( C T_1^{(0)} C )(x,k) = -i a_Delta k_hat_x b_tilde(x,k_hat) P_-(k)
                                + O(|k|^{-infinity}) + lower-order corrections.

  This is the check file's own adversarial converse, realized: "longitudinal:
  (I-M)(M)(I-M) = -2(I-M) != 0" [CHECK :219-229] — verified exactly here as
  (wI-K)K(wI-K) = -2|k|^2 (wI-K) (§8 C8). The survivor is INTRABAND — a SCALAR on
  the sea band (coefficient -i a_Delta k_hat_x b_tilde times the band identity).
  The interband-only structure A = [C,[C,A]] FAILS for this term: for the intraband
  A_par = k_hat_x M, [C, A_par] = 0 identically, so [C,[C,A_par]] = 0 != A_par.
```

**Degree bookkeeping, plain.**

```text
Surviving symbol degree in k:            0        (k_hat_x b_tilde: bounded, degree-0
                                                   homogeneous, NO decay)
Surrogate's post-annihilation degree:    <= -1    (CHECK §5; not comparable object
                                                   class — the surrogate's middle
                                                   factor was covariance-conjugated,
                                                   symbol degree -1 BEFORE the
                                                   sandwich; the sealed middle factor
                                                   is a difference of unitaries,
                                                   degree 0)
Local HS-integrability of the survivor:  AT NO NEGATIVE ORDER carrier-blindly. The
  HS integrand of the surviving term is O(1) in k: ||C T_1^{(0)} C||_2^2 has the
  shape |a_Delta|^2 int d^3x d^3q |B_hat_D(k_hat.q, q)|^2-type (finite) times
  int d^3k O(1) — DIVERGENT proportionally to the carrier's momentum volume
  (the Lambda^3 shape of E1 C2: "finite only on a fixed carrier"). On the sealed
  Galerkin carrier it is finite and scales with the carrier — a carrier-UNIFORMITY
  failure shape, which is exactly what S2/B-L2* demands be excluded.
Local HS-integrability of the interband remnant: at EVERY order (faster than any
  power) — this sector is better than the surrogate's.
```

**The trace cross-check — the sealed record already contains this survivor.** The
spinor trace of the surviving symbol is tr_spinor[-i a_Delta k_hat_x b_tilde P_-] =
-2 i a_Delta k_hat_x b_tilde — and indeed tr_spinor[C(p) alpha_x] = -2 p_hat_x is
SEALED TEXT [E1 :693-694, :1107-1108] (re-derived exactly: tr[(wI-K)alpha_x(wI-K)] =
-8 k_x w, §8 C4, i.e. tr[C alpha_x C] = -2 k_hat_x). The sealed S1 mechanism — the
trace is finite because the ODD (p_hat_x) integrand cancels under the angular
k-integration (and |m_0|^2 = 0), NOT because the sandwich vanishes — PRESUPPOSES
C alpha_x C != 0. This re-analysis recovers S1's cancellation on the two-time object
(x-integration makes b_tilde's k_hat-dependence drop from the trace:
int d^3x b_tilde(x,k_hat) = int b_D dt d^3x, k_hat-independent; the k_hat_x angular
integral then vanishes exactly), and shows why it does NOT transfer to S2: the HS
norm squares the symbol, |k_hat_x|^2 is even, and nothing cancels. The sealed
S1-fine / S2-wall division is exactly reproduced.

**Why the surrogate missed this.** The surrogate's middle factor was
[phase difference] x C(r) — the equal-time idealization conjugates the sea
COVARIANCE, so its Fourier symbol is the k-DERIVATIVE of alpha.k_hat, and the
unit-vector derivative is automatically transverse (that is where ell_perp came
from). The sealed middle factor is a difference of UNITARIES whose first-order
symbol is the conjugated vertex itself — no covariance factor, no unit-vector
derivative, no manufactured transversality. The anchor's "wrong object class"
[ANCHOR §5, §7] is hereby given its exact content: the object-class substitution did
not merely risk corrections — it deleted the entire surviving sector.

---

## 6. STEP 4 — HIGHER ORDERS AND THE SHARP FACTOR, SCOPED HONESTLY

```text
SECOND ORDER IN THE VERTEX (O(a^2)). Two J insertions with free/record propagation
  between: symbol degree <= 0 with at least the first order's transfer decay;
  intraband x intraband chains are degree 0 at O(a_+^2, a_+a_-, a_-^2); interband x
  interband products entering intraband blocks carry the O(|k|^{-infinity})
  suppression twice. NO identical cancellation against the first-order survivor is
  possible: the orders are separable in a_Delta over the frozen pair family
  [PA :140-141] (distinct nonzero a_Delta values), and no sealed identity relates
  them. The FAILS verdict is decided at first order.
THE SHARP RECORD FACTOR M(t). Record-dressed strata (>= 1 insertion of
  v(t) M(t) tensor S) are OUTSIDE the smooth symbol category: 1_{|x| <= r(t)} is a
  sealed SHARP indicator [E1 :465-470] whose transfer decay is power-law only
  (boundary-surface tails), the named B-L2* locus (volume diagonal) [E1 bytes
  [57212,58506)]. These strata are ADDITIVE separate terms; they cannot cancel the
  stratum-zero survivor absent an exact certified identity — none is sealed, and
  C4's saturation ("the zero-sum weights buy NO decay" at full tau_R, E1 :343-350)
  runs the other way. NOT resolved here; explicitly not this task's target.
THE WEIGHT-SUMMED CAVEAT (honest, load-bearing for interpretation). The FAILS
  verdict is stated at the SEALED S2 QUANTIFIER: per record-color pair, sup over
  pairs on the surviving sector [E1 :653-654, :686-690, :696-698]. In the fully
  weight-summed assembly (R_pointer = sum_{mu,lambda} w_mu^* w_lambda ...,
  PA :212-214), the stratum-zero term is pair-independent and its coefficient is
  |sum_lambda w_lambda|^2 = |<pointer|ready>|^2 = 0 — C4's own |m_0|^2 = 0 kill
  annihilates exactly this stratum THERE. But that summation (i) is not the sealed
  S2 target (R.1 takes the sup over color pairs), and (ii) relocates the leading
  survivor into the record-dressed strata — i.e., onto the sharp M(t) at the volume
  diagonal, exactly B-L2*'s named wall — and meets the F'-14 log-of-sum obstruction
  [E1 :669-674] at the determinant level. The finding therefore RELOCATES, not
  removes, the wall under re-quantification; per-pair, it stands as stated.
NOT COVERED BY THIS ANALYSIS (honest scope): the G3-derivative remainder — the
  write chains ell_j [FORM :277-281] do not enter the per-cell E1 vertex at all
  (J carries b_D, not ell); they re-enter only at multi-cell assembly (§7). The
  IR/diamond-boundary side of the sandwich (the a-vertex has no boundary issue —
  b_D vanishes to all orders there; the record M(t) boundary is B-L2*'s). The
  post-limit (continuum/carrier limit) — the finding is stated as carrier-scaling
  SHAPE, no limit taken, nothing evaluated. Gauge: no licensed gauge move exists
  (PA: fixed-gauge diagnostic, "Phase A claims no local gauge covariance",
  PA :130-135), and the survivor is not pure gauge regardless
  (int b_D dt d^3x != 0 since b_D > 0 on the open diamond).
```

---

## 7. CARRIER DEPENDENCE, STEP BY STEP

```text
PER-CELL ONLY (carrier-light; unchanged on K_dd or any multi-cell family):
  - the Dyson expansion and the exact first-order form (§3): any cell, any carrier;
  - the band-typing identity P_± alpha_x P_± = ±k_hat_x P_± and every Clifford
    identity of §4/§8: continuum symbol algebra, carrier-free;
  - the conjugation/oscillation dichotomy and the cell-time integration kinematics
    (§4.3): per-cell, using only the sealed diamond profile and h_0's symbol;
  - the sandwich algebra and the trace/HS split (§5): pointwise in k.
  Galerkin caveat: Q-compression distorts these only at the carrier's UV edge; the
  principal-symbol statements live in the carrier interior.
CARRIER-SENSITIVE:
  - the QUANTITATIVE meaning of the degree-0 survivor: its HS norm is finite only
    through the carrier's UV truncation and scales with the carrier momentum volume
    (the C2 Lambda^3 shape) — the carrier-uniform S2/R-L2b demand is what it
    breaks; on any FIXED carrier nothing diverges;
  - multi-cell families / K_dd [MIN-CARRIER, conditional candidate of record]: the
    first-order survivors are cell-local (each cell's own b_D) and ADD over cells;
    no cross-cell cancellation exists at first order without a certified mechanism
    (none sealed); which cells/pairs enter, and the G3 write-chain realization,
    are family data that first appear at assembly — the per-cell verdict is
    unchanged on K_dd, whose per-cell structure this analysis never used beyond
    the sealed cell definitions.
```

---

## 8. THE SCRIPT (exact symbolic verification; reproduced in full) AND ITS OUTPUT

Run with sympy 1.14.0 (fresh venv; CAS used for exact polynomial/trig matrix
identities ONLY — no numeric evaluation of any physical quantity).

```python
# TWO-TIME re-analysis: exact symbolic verification of the load-bearing Clifford identities.
# EXACT SYMBOLIC ONLY: polynomial/trig identities over symbols; nothing evaluated numerically.
import sympy as sp

I2 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
Z2 = sp.zeros(2, 2)

def alpha(s):  # Dirac alpha_j = [[0, sigma_j], [sigma_j, 0]]
    return sp.Matrix(sp.BlockMatrix([[Z2, s], [s, Z2]]).as_explicit())

ax, ay, az = alpha(sx), alpha(sy), alpha(sz)
I4 = sp.eye(4)

kx, ky, kz, lx, ly, t = sp.symbols('kx ky kz lx ly t', real=True)
w = sp.symbols('w', positive=True)  # w stands for |k|; the relation w^2 = kx^2+ky^2+kz^2 is imposed by substitution
s2 = kx**2 + ky**2 + kz**2

K = kx*ax + ky*ay + kz*az   # symbol of h_0 = alpha.p at momentum k (PA :79)
KM = w*I4 - K               # 2|k| * C(k): the sea-band projector numerator (E1 C1)

def zero(M):
    M = sp.expand(M)
    M = M.subs(w**2, s2)
    M = sp.expand(M)
    M = M.subs(w**2, s2)
    M = sp.simplify(sp.expand(M))
    return M == sp.zeros(*M.shape)

print("C1  K^2 = |k|^2 I                          :", zero(K*K - s2*I4))
print("C2  {alpha_x, K} = 2 kx I                  :", zero(ax*K + K*ax - 2*kx*I4))
print("C3  (wI-K) ax (wI-K) = -2 kx (wI-K)        :", zero(KM*ax*KM + 2*kx*KM))
print("C4  tr[(wI-K) ax (wI-K)] = -8 kx w         :", sp.simplify(sp.expand((KM*ax*KM).trace()) + 8*kx*w) == 0)
# C3/C4 give C ax C = -(kx/w) C and tr_spinor[C(p) alpha_x] = -2 p-hat_x  (the sealed S1 identity, E1 :693-694, :1107-1108)

# C5: Heisenberg conjugation. e^{iKt} = cos(wt) I + i sin(wt) K/w  (since K^2 = w^2 I).
c, s = sp.cos(w*t), sp.sin(w*t)
U  = c*I4 + sp.I*s*K/w
Ud = c*I4 - sp.I*s*K/w
a_par  = kx*K/w**2          # longitudinal (band-diagonal) part of alpha_x
a_perp = ax - a_par         # transverse (interband) part
target = a_par + sp.cos(2*w*t)*a_perp + sp.I*sp.sin(2*w*t)*(K/w)*a_perp
D = sp.expand_trig(sp.expand(U*ax*Ud - target))
D = sp.expand(D.subs(w**2, s2)); D = D.subs(w**2, s2)
D = sp.simplify(sp.expand_trig(sp.expand(D)))
print("C5  e^{iKt} ax e^{-iKt} = kx K/w^2 + cos(2wt) a_perp + i sin(2wt) (K/w) a_perp :", D == sp.zeros(4, 4))

# C6: the surrogate contrast — for l with k.l = 0, (wI-K)(alpha.l)(wI-K) = 0 (the CONFIRMED equal-time annihilation)
lz_sol = -(kx*lx + ky*ly)/kz   # impose k.l = 0
L = lx*ax + ly*ay + lz_sol*az
print("C6  (wI-K)(alpha.l_perp)(wI-K) = 0          :", zero(KM*L*KM))

# C7: interband typing of the rotated parts: {K/w, a_perp} = 0 and {K/w, (K/w) a_perp} = 0 (both anticommute with M => interband)
M4 = K/w
print("C7a {M, a_perp} = 0                         :", zero(M4*a_perp + a_perp*M4))
print("C7b {M, M a_perp} = 0                       :", zero(M4*(M4*a_perp) + (M4*a_perp)*M4))

# C8: the check-file converse used as the FAILS detector: (wI-K) K (wI-K) = -2|k|^2 (wI-K);
#     dividing by w^3 with M = K/w, I-M = (wI-K)/w this is exactly (I-M)M(I-M) = -2(I-M).
print("C8  (wI-K) K (wI-K) = -2|k|^2 (wI-K)  [<=> (I-M)M(I-M) = -2(I-M)] :", zero(KM*K*KM + 2*s2*KM))
```

Output, verbatim:

```text
C1  K^2 = |k|^2 I                          : True
C2  {alpha_x, K} = 2 kx I                  : True
C3  (wI-K) ax (wI-K) = -2 kx (wI-K)        : True
C4  tr[(wI-K) ax (wI-K)] = -8 kx w         : True
C5  e^{iKt} ax e^{-iKt} = kx K/w^2 + cos(2wt) a_perp + i sin(2wt) (K/w) a_perp : True
C6  (wI-K)(alpha.l_perp)(wI-K) = 0          : True
C7a {M, a_perp} = 0                         : True
C7b {M, M a_perp} = 0                       : True
C8  (wI-K) K (wI-K) = -2|k|^2 (wI-K)  [<=> (I-M)M(I-M) = -2(I-M)] : True
```

(Process note of record: the first run reported C4/C8 False — C4 from an unevaluated
`sp.trace` wrapper, C8 from THIS analyst's mis-normalized expected constant
(-2w instead of -2|k|^2 at the unnormalized level). Both were re-derived by hand,
the script corrected, and all nine identities verify. The by-hand derivation in
§4-§5 was unaffected.)

---

## 9. RECONCILIATION WITH THE SEALED RECORD, STATED PLAINLY

```text
1. E1 C6 / B-L2* ("only two-time objects can work; the cell time integration
   supplies the missing decay") — REFINED, not contradicted: the time integration
   supplies decay EXACTLY on the sector the sandwich already annihilates
   (interband), and supplies NOTHING on the sector the sandwich keeps (intraband).
   Two-time-ness is necessary (C6) but its decay mechanism is sector-blind to the
   survivor found here.
2. E1 B-L2 "a-VERTEX SECTOR: plausible" [:1111-1113] — CONTRADICTED at
   principal-symbol level AT THE SEALED PER-PAIR S2 QUANTIFIER. The Gevrey premise
   is TRUE (and used here), but fast joint (omega,q)-decay does not reach the
   intraband energy shell, where omega = |k'|-|k| stays bounded at fixed transfer
   (massless dispersion). Under the weight sum the |m_0|^2 = 0 kill rescues this
   stratum and confines the block to the record vertex — B-L2's typing is
   defensible ONLY under that re-quantification (§6).
3. E1 S1 [:693-694] — INDEPENDENTLY RE-DERIVED on the two-time object: the sealed
   odd spinor trace -2 p_hat_x IS the trace of the surviving intraband symbol; the
   trace-level cancellation survives two-time, and its mechanism (oddness) is
   exactly what the HS norm squares away.
4. THE CHECK's converse [CHECK :219-229] — REALIZED: the check proved a
   longitudinal survivor would not be killed and confirmed none existed ON THE
   SURROGATE; the sealed vertex supplies precisely that survivor.
5. THE ANCHOR's refutation [ANCHOR §5-§7] — COMPLETED as demanded: the owed
   two-time re-analysis finds the annihilation does NOT extend; the anchor's "its
   leading symbol could contain ... longitudinal terms not controlled by the B1
   calculation" is answered: it does, and the term is exhibited.
6. E1's CANCELLATION INVENTORY [:565-569] — RESPECTED: no fourth summability
   source is claimed; the third source (time-integration smoothing) is shown to
   have an exact intraband blind spot.
```

---

## 10. FLAG BLOCK

```text
FIRST_ORDER_TERM = EXACT(
  T_1 = -i a_+ int_0^1 W_mu(1,0)^dag W_lambda(1,t') J(t') W_lambda(t',0) dt'
        + i a_- int_0^1 W_mu(t',0)^dag J(t') W_mu(1,t')^dag W_lambda(1,0) dt'
      = -i int_0^1 W_mu(t',0)^dag [a_+ G_{mu lambda}(t') J(t')
                                   - a_- J(t') G_{mu lambda}(t')] W_lambda(t',0) dt',
  G_{mu lambda}(t') = W_mu(1,t')^dag W_lambda(1,t'); J(t) = -(Q b_D(t) Q) tensor
  alpha_x [PA :121-122; E1 :1111]; V_{mu lambda}(a) = u_mu(a_-)^dag u_lambda(a_+)
  [E1 :653-654]; W generated by h_0 + lambda v(t)M(t) tensor S [PA :124-127,
  :181-182; E1 :465-470]; branch-diagonal flatness exact (FORM D3 [:168-186]
  reproduced); record-stratum zero: T_1^{(0)} = +i a_Delta int_0^1 e^{i h_0 t'}
  b_D(t',x) alpha_x e^{-i h_0 t'} dt', pair-independent; smooth tensor sharp
  factor structure per E1 :1056-1058, :1111-1116, :510-513, :696-698.)

PRINCIPAL_SYMBOL = LONGITUDINAL_GENERATED(
  the algebra: alpha_x = k_hat_x(alpha.k_hat) + alpha_x^perp with the longitudinal
  part EXACTLY the band-diagonal part (P_± alpha_x P_± = ±k_hat_x P_±; C alpha_x C
  = -k_hat_x C, exact, §8 C3) — present in the sealed vertex from the start, NOT
  generated from a transverse seed: the surrogate's ell_perp structure never forms
  on this object class. The propagators commute through the longitudinal part
  unrotated ({alpha_x, alpha.k} = 2k_x I) and rotate the transverse part at 2|k|
  (e^{iKt}alpha_x e^{-iKt} = alpha_x^par + cos(2|k|t)alpha_x^perp
  + i sin(2|k|t) M alpha_x^perp, exact, §8 C5); the Gevrey cell-time integration
  kills the rotated (interband) sector faster than any power and leaves the
  longitudinal sector at full strength (non-oscillatory phase). NO scalar
  component at any order of the conjugation. Net principal symbol:
  sigma(T_1^{(0)}) = i a_Delta k_hat_x b_tilde(x,k_hat) alpha.k_hat
  + O(|k|^{-infinity}), b_tilde(x,k_hat) = int_0^1 b_D(t', x - t'k_hat) dt'.)

SANDWICH_RESULT = INTRABAND_SURVIVES(
  the term: sigma(C T_1^{(0)} C) = -i a_Delta k_hat_x b_tilde(x,k_hat) C(k)
  + O(|k|^{-infinity}) — first order in a_Delta, symbol degree 0, a scalar on the
  sea band; (I-M)M(I-M) = -2(I-M) != 0 (the check's own converse, §8 C8); the
  interband identity A = [C,[C,A]] fails on it ([C, A_par] = 0). Its spinor trace
  is the SEALED identity tr_spinor[C(p)alpha_x] = -2 p_hat_x [E1 :693-694,
  :1107-1108] — the record itself already carries C alpha_x C != 0; S1's trace
  kill (oddness + |m_0|^2 = 0) survives two-time, the HS norm squares it away.
  Local HS-integrability: NEVER at symbol level carrier-blindly for the survivor
  (degree-0 symbol; HS-norm^2 scales as the carrier momentum volume — the C2
  Lambda^3 shape); at ALL orders for the interband remnant (faster than any
  power — STRONGER than the surrogate's degree <= -1).)

HIGHER_ORDERS = SCOPED(
  second order: degree <= 0, O(a^2), separable from O(a_Delta) over the frozen
  pair family [PA :140-141] — no identical cancellation; verdict decided at first
  order. Sharp record factor M(t): record-dressed strata carry the sealed sharp
  indicator [E1 :465-470], power-law transfer tails only, outside the smooth
  symbol category — the B-L2* volume-diagonal locus, additive, unable to cancel
  the smooth-sector survivor absent a sealed exact identity (none; C4 saturation
  runs the other way). Weight-summed caveat: |sum_lambda w_lambda|^2 = 0 kills
  stratum zero in the fully summed assembly, relocating the wall onto the sharp
  record strata (B-L2*) and the F'-14 log-of-sum obstruction — NOT available at
  the sealed per-pair S2 quantifier. NOT COVERED: G3 remainder (no ell in the
  per-cell E1 vertex; re-enters at multi-cell assembly), IR/diamond boundary,
  post-limit.)

NET = FAILS(
  the term above: the sealed two-time first-order intraband survivor
  -i a_Delta k_hat_x b_tilde(x,k_hat) C(k), degree 0, carrier-scaling HS. The
  equal-time annihilation does NOT extend to the sealed vertex AT THE SEALED
  PER-PAIR S2 QUANTIFIER. Honest structure of the failure: the annihilation
  mechanism itself (interband => sandwich-zero) survives STRENGTHENED on the
  sector where it operated; the failure comes entirely from the band-diagonal
  sector of alpha_x, which the surrogate's object class had deleted (covariance
  conjugation manufactures transversality via the unit-vector derivative; the
  difference of unitaries has no such factor). Root kinematic cause: massless
  on-shell marginality — energy transfer |omega| <= |q| stays bounded along the
  sea shell, so Gevrey joint decay never engages intraband.)

CARRIER_DEPENDENCE = SPLIT(
  per-cell only: Dyson expansion, band-typing and all Clifford identities,
  conjugation/oscillation dichotomy, cell-time integration kinematics, sandwich
  algebra, trace/HS split — continuum symbol algebra, unchanged on K_dd or any
  multi-cell family; carrier-sensitive: the HS-norm meaning of the degree-0
  survivor (finite only on a fixed carrier, scales with carrier momentum volume —
  the exact C2 shape; this IS the carrier-uniformity failure), and multi-cell
  assembly (cell-local survivors add; no cross-cell cancellation at first order
  without a certificate; G3 write-chain and family data first enter there).)

SEALS_VERIFIED = 7/7(48e0c76f ANCHOR; 7cf16a3c CHECK; 564b7040 SYMHUNT; 46846730
  E1; 789338ad PA; 5e49d209 FORM; f1881511 MIN-CARRIER — all recomputed at path
  this session, all matching sidecars and tasked digests; none unverifiable; the
  four anchor-certified E1 byte spans re-extracted from bytes.)

FORBIDDEN_IMPORTS = none(no scale, no imported GR, no faithfulness authority; the
  sea kernel's sealed form read to fix structure only, never evaluated; no
  register/tracker/plan/road/ledger/lens read; no physical quantity computed,
  bounded, or evaluated — degrees, orders, and parities only.)

MACHINERY_INVOKED = yes(exact symbolic CAS only — sympy 1.14.0 verifying nine
  polynomial/trig Clifford identities over symbols, script and output reproduced
  verbatim in §8; shasum/file reads/greps otherwise; NOTHING numeric: no value of
  n, kappa_record, alpha, any exponent, norm, scale, or spectrum computed,
  bounded, estimated, or evaluated.)

alpha_computed = false ; kappa_record_computed = false ; proof_authorized = false ;
coupling_evaluation_authorized = false
ALL_RESULTS = CLAIMED until checked.
TWO_TIME_REANALYSIS_RESULT = SEALED.
```
