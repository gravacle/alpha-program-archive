# STAGE 8 — B-L2* ATTEMPTED: THE CARRIER-UNIFORM TWO-TIME HS CERTIFICATION OF THE >= 2-INSERTION STRATA AT THE VOLUME DIAGONAL

## BLIND ANALYST — CODENAME BL2STAR — [SEALED]

Date: 2026-08-13
Role: BLIND analyst (BL2STAR). One hard structural estimate attempted and reported
honestly: B-L2* — the carrier-uniform TWO-TIME Hilbert-Schmidt certification of the
record-vertex pairing at the VOLUME DIAGONAL x = y, taken at the summed-assembly
quantifier where C4's identities have already killed every stratum with fewer than
two record insertions per CTP branch.

Gates: `alpha_computed = false` ; `kappa_record_computed = false` ;
`proof_authorized = false` ; `coupling_evaluation_authorized = false`
ALL_RESULTS = CLAIMED until checked.

Fences held: EXACT SYMBOLIC ANALYSIS ONLY — operator/Clifford/symbol algebra, exact
degree/order/parity/coincidence-order bookkeeping on sealed forms; the one script
used is exact symbolic CAS verification of matrix/trig identities over symbols
(sympy 1.14.0, fresh venv), reproduced in full in §9, NOTHING numeric. No physical
quantity computed, bounded numerically, or evaluated; every constant carried
symbolic. The sealed sharp localizer M(t) was NOT softened, mollified, or replaced
(E1 :465-470, :1123-1124 respected as written). The equal-time route was NOT
resurrected (C6 respected as FALSE). No scale, imported GR, or faithfulness
authority; scale-bearing sealed text read SUSPECT-ONLY to fix structure. No
register/tracker/plan/road/ledger/lens file read. Output name probed before write:
ABSENT. No git action.

---

## 0. VERDICT IN ONE LINE

**NET = FAILS-AT(the stratum-resummation step, at the sealed saturation clause).
Per FIXED stratum the certification mechanism exists and is exact — each record
insertion's band-diagonal element vanishes linearly at momentum coincidence
(P_s(k')·S·P_s(k) = ±(1/2)·S·(alpha·(k-hat' − k-hat))·P_s(k), new exact identity,
§4), so every >= 2-per-branch stratum has volume-diagonal amplitude degree <= −2 at
fixed transfer, strictly past the HS threshold −3/2. But the sealed C4 saturation
clause (E1 :346-351) is itself the exact statement that this per-stratum gain does
NOT survive the stratum sum: at full tau_R the weight-summed branch propagator
resums to the sharp, spinor-trivial causal-ball projector P (plus the UNCERTIFIED
C-L1 error), P's band-diagonal transfer elements are O(1), and the leading summed
response then contains the P-restricted longitudinal intraband term
−i a_Delta k-hat_x b-tilde_P(x, k-hat) C(k) — degree 0, the C2 Lambda^3
carrier-volume HS shape at the volume diagonal, with no sealed identity to cancel
it. The exhibition is exact AT the sealed C4 operator-level display; its only
in-spec escape is a certified C-L1 error structure supplying an exact cancellation
(nothing sealed supplies one; witness E1_RECORD_PHASE_OPERATOR_COLLAPSE_UNCERTIFIED),
the only other named repair — softening M(t) — being sealed away.**

---

## 1. SEALS VERIFIED AT PATH (shasum -a 256), BEFORE ANY RELIANCE

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`. Every digest below
recomputed from bytes at path THIS session and matched both the sidecar
`.seal.sha256` and the tasked digest (where tasked). None unverifiable.

```text
468467303a109dc825b015107897dacc107800fc981030377c3f006b384cccb5  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md                          MATCH (E1; tasked + sidecar)
789338adb7d3d36da453113e98f371a4f92543cf2652b047f8481c407bed5bc3  STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md MATCH (PA; tasked + sidecar)
18af3dee8e3e5b17fe624d1b0547f4713359473a373df1562ff584647244ccf1  STAGE8_TWO_TIME_REANALYSIS_V001.md                                   MATCH (TWO-TIME; tasked + sidecar)
6a2aa0fd18b9a0ea4f370dfbea278563ba02552e64b48ac0a7d91fbd7f90bc9e  STAGE8_TWO_TIME_CHECK_V001.md                                        MATCH (TT-CHECK; tasked + sidecar)
0a10c0305d4cde8b226d844ed0fb9289f393b670e02b144bf762dd49c853c9c4  STAGE8_ASSEMBLY_QUANTIFIER_V001.md                                   MATCH (AQ; tasked + sidecar)
331035d393695519eaa061a343abb67129a8ea48fcc47a765daaef1883b0aa22  STAGE8_ASSEMBLY_QUANTIFIER_CHECK_V001.md                             MATCH (AQ-CHECK; tasked + sidecar)
3d8aea1a4779b0bfe7a472dca1fab0642750e8e010e339b9e3b100197b75a18c  scripts/derive_stage8_t7_primitive_operator_response_v001.py         MATCH (PA-pinned executor; digest pinned in PA's own hash table, recomputed at path)
```

The tasked E1 byte span was re-extracted from bytes this session:
`[57212,58506)` recomputes to
`162e30a6ccb77ae53fb9026ef6d4a675fb74cb899b1e21c6fbc4926225ae5fcf` — MATCH to the
tasked span digest. All line-cited sealed content below was read at path this
session: E1 :339-352 (C4), :353-364 (C6 + locus refinement), :465-470 (D6' sharp
localizers, no-mollify clause), :652-700 (R.0/R.1/S2), :740-800 (R.2 sector algebra,
kappa_bal), :806-845 (R.3, R-L2b, colour-sum closure), :1110-1116 and :1123-1124
(B-L2 typing; only-repair clause), :2183-2196 (certification ledger,
`record_vertex_two_time_HS_certified = false` at :2191); PA :55-141 (carrier, A1
ball/localizer, A2 diamond b_D and J, frozen pairs), :155-214 (pointer weights,
u_lambda, R_pointer), :360-380 (Strang interleaving); the PA-pinned executor's
`dirac_data()` (the concrete sealed realization S = −i gamma^0 gamma^5,
slash(n) = gamma^0, alpha_j = gamma^0 gamma^j, Dirac representation).

---

## 2. STEP 1 — THE OBJECT, SET UP EXACTLY FROM THE SEALED DISPLAYS

### 2.1 The >= 2-insertion stratum object

```text
PER PAIR [E1 :652-661]:  V_{mu lambda}(a) = u_mu(a_-)^dagger u_lambda(a_+),
                         Delta_{mu lambda}(a) = C(V(a) - V(0))C,
   u_lambda(a) generated by h_lambda(t;a) = h_0 + lambda v(t) M(t) tensor S + a J(t)
   [PA :124-127, :181-182], h_0 = sum_j p_j tensor alpha_j [PA :79],
   S = S_n = -i slash(n) gamma^5, slash(n) = gamma^0 (PA-pinned executor,
   dirac_data(), digest 3d8aea1a MATCH), S^2 = I, S^dagger = S (§9 I1-I2),
   M(t) = Q 1_{|x|<=r(t)} Q, r(t) = min(t,1-t), v(t) = tau_R 32 r(t)^3, SEALED
   SHARP [E1 :465-470], int_0^1 v = tau_R = pi/sqrt2 EXACTLY,
   J(t) = -(Q b_D(t,x) Q) tensor alpha_x, b_D Gevrey [PA :100-122; E1 :1111-1113],
   C = 1_{(-inf,0)}(h_0), C(k) = (I - alpha.k_hat)/2, off-diagonal kernel EXACTLY
   degree -3, log-marginal at coincidence [E1 C1 :320-329].

SUMMED ASSEMBLY (the defined objects' own sealed quantifier; AQ Det.1 CONFIRMED):
   the weights enter as sum_{mu,lambda} w_mu^* w_lambda (...) [PA :212-214;
   E1 :669-674]. The weights are REAL: w_lambda = <pointer|P_lambda|ready> with
   the C4 stencil values (w_0, w_{+sqrt2}, w_{-sqrt2}) = (1/2, -1/4, -1/4)
   [E1 :340-342: sum_lambda w_lambda f(lambda) = -(1/4)[f(+sqrt2) - 2f(0)
   + f(-sqrt2)], read off at f = indicator], so w^* = w. The double sum
   FACTORIZES EXACTLY over the two CTP branches:

     X(a_+, a_-) := sum_{mu,lambda} w_mu w_lambda Delta_{mu lambda}(a)
                  = C[ U(a_-)^dagger U(a_+) - U(0)^dagger U(0) ]C,

     U(a) := sum_lambda w_lambda u_lambda(a)
           = -(1/4)[ u_{+sqrt2}(a) - 2 u_0(a) + u_{-sqrt2}(a) ]

   — each branch factor is the SYMMETRIC SECOND DIFFERENCE of three UNITARIES
   over the record-coupling stencil {0, +-sqrt2} (the sealed second-difference
   Kraus structure, operator form). ||U(a)|| <= 1/4 + 1/2 + 1/4 = 1: the sealed
   l1-tight mass, exactly.

RECORD-STRATUM GRADING. Expanding each u in powers of the record vertex
   lambda v(t) M(t) tensor S (Dyson-interleaved with h_0- and J-propagation:
   two-time, insertions at independent ordered times — the PA :371-380 Strang
   factors are the same interleaving), a branch term with n insertions carries
   lambda^n; the branch weight sum inserts the moment m_n = sum w_lambda
   lambda^n. SEALED + re-verified exactly (§9 I10): m_0 = m_1 = 0, all odd
   moments 0, m_{2j} = -2^{j-1} (m_2 = -1, m_4 = -2). Hence [E1 :343-345]
   every Dyson term with FEWER THAN TWO record insertions PER CTP BRANCH is
   annihilated in X: the summed survivors begin at n_- >= 2 AND n_+ >= 2
   insertions (even each). THE >= 2-INSERTION STRATUM OBJECT IS X ITSELF,
   graded: X = sum_{n_-, n_+ >= 2, even} X^{(n_-, n_+)}, plus the a-grading
   (every term of X carries >= 1 J insertion — the a-difference).

CARRIER-UNIFORM quantifies over: the Hermite-Galerkin refinement family
   H_{n,ell} [PA A1 :55-70], i.e. the D3 refinement quantifier of the sealed
   require-clause (R-L2b, E1 :826-832: G_hs finite UNIFORMLY over the D3
   refinement quantifier; TRILEMMA form of record: sup_n ||X_n||_2 <= M). A
   bound that grows with the carrier's momentum volume (the C2 shape:
   "~ Lambda^3 under carrier-blindness; finite only on a fixed carrier",
   E1 :330-333) is NOT carrier-uniform.

THE LOCUS AND THE THRESHOLD. B-L2* [E1 bytes [57212,58506), digest 162e30a6]:
   the bound must be TWO-TIME (equal-time is FALSE by C6, Shale-Stinespring,
   ||[C,1_B]||_2 = +infinity); the locus is the VOLUME DIAGONAL x = y
   ("A bound that controls only the boundary region does not discharge
   B-L2*"). Threshold arithmetic, exact: C's off-diagonal kernel is degree -3
   (E1 C1); a kernel of coincidence degree -p on a 3-D volume is locally HS
   iff 2p < 3, i.e. DEGREE > -3/2. Equivalently in momentum space: the HS
   integrand at bounded transfer must decay in |k| strictly faster than
   |k|^{-3/2} in amplitude (|amplitude|^2 integrable against d^3k); an
   amplitude that is O(1) in |k| at bounded transfer gives HS^2 ~ carrier
   momentum volume — the C2 Lambda^3 failure shape. TWO orders of
   coincidence-vanishing on a degree -3 kernel land at degree -1 > -3/2:
   past the threshold. This is the exact sense of "a discrete second
   derivative kills two orders at coincidence" — IF the second-difference
   structure acts at spatial coincidence.
```

### 2.2 What is being attempted, precisely

Certify (or refute, or locate the exact wall of):
`|| X(a_+, a_-) ||_2 <= |C|_4^{alpha} G` with `G` finite uniformly over the
refinement family, `alpha` symbolic, on the closed pair polydisc — the summed
two-time HS certification of the >= 2-insertion strata at the volume diagonal.
(Noted of record, per AQ Det.1(iii): no sealed display places the colour sum inside
a Schatten-2 norm; the summed-quantifier statement S2' is an unsealed spec act.
This attempt analyzes the summed object structurally; it does not and cannot
create the sealed target — that residue is debt 3 regardless of the outcome here.)

---

## 3. STEP 2(a) — THE SECOND-DIFFERENCE MECHANISM, WORKED EXACTLY

The second difference acts in the COUPLING variable lambda over the stencil
{0, +-sqrt2}. Its exact effects, separated:

```text
(a1) STRATUM KILL (sealed, re-verified §9 I10): m_0 = m_1 = 0 — strata with
     < 2 insertions on either branch vanish identically in X. In particular
     the smooth stratum zero — whose per-pair intraband survivor
     -i a_Delta k_hat_x b_tilde C(k) is the sealed per-pair FAILS term
     (18af3dee, confirmed 6a2aa0fd) — is DEAD here. This kill is the entire
     reason B-L2* lives on the record vertex.
(a2) COINCIDENCE ORDER AT THE DIAGONAL (new, exact, §4): the surviving
     insertions' spinor factor S is EXACTLY interband; each record insertion's
     band-diagonal channel carries an exact factor alpha.(k_hat' - k_hat)/2 —
     ONE order of coincidence-vanishing per insertion. With >= 2 insertions
     per branch this is the "second derivative kills two orders" mechanism
     REALIZED PER BRANCH: >= 2 coincidence orders per branch, >= 4 total on
     the all-intraband channel of the leading stratum. Effect on the
     volume-diagonal degree, exact: the fixed-stratum intraband amplitude at
     bounded transfer is O(|k|^{-4}) — the degree moves from 0 (the C2 shape)
     to <= -4, and even the worst band-flip configuration nets <= -2 (§4.3):
     STRICTLY past the -3/2 threshold, stratum by stratum.
(a3) THE LIMIT OF THE MECHANISM (sealed, re-verified §9 I11-I12): at full
     tau_R the stencil sees the record phase FULLY WRAPPED: cos(lambda tau_R)
     = (+1, -1, -1) on lambda = (0, +sqrt2, -sqrt2), sin(lambda tau_R) = 0,
     so the second difference of the phases is -(1/4)[(-1) - 2(+1) + (-1)]
     = 1 = sum|w_lambda|: l1-TIGHT. A second difference is small only on a
     slowly-varying integrand; at full tau_R the integrand is maximally
     varying over the stencil and the second difference SATURATES. The
     coupling-space second difference therefore supplies coincidence orders
     ONLY stratum-by-stratum (through (a2)); summed over strata it buys
     nothing — that is the sealed clause "the zero-sum weights buy NO decay"
     [E1 :346-351], reproduced here as exact stencil arithmetic.
```

---

## 4. STEP 2(b) — THE INTERBAND/INTRABAND SPLIT ON THE STRATUM: THE EXACT ALGEBRA

### 4.1 The record vertex's spinor factor is exactly interband (new identity)

With the PA-pinned realization S = -i gamma^0 gamma^5 (slash(n) = gamma^0,
verified at the sealed executor bytes, digest MATCH), alpha_j = gamma^0 gamma^j:

```text
S alpha_j = -i gamma^0 gamma^5 gamma^0 gamma^j = +i gamma^5 gamma^j
alpha_j S = -i gamma^0 gamma^j gamma^0 gamma^5 = -i gamma^5 gamma^j
=>  {S, alpha_j} = 0  for j = x, y, z            (§9 I3-I5, exact)
=>  {S, M(k)} = 0,  M(k) := alpha.k_hat  (the h_0 band operator at every k)
=>  P_s(k) S P_s(k) = 0  for both bands s = +-    (§9 I9a/I9b, exact):
    the record vertex's spinor factor has ZERO band-diagonal part at every
    momentum — it is a PURE interband generator.
```

Contrast of record: the smooth vertex alpha_x has the O(1) band-diagonal
(longitudinal) part -k_hat_x C(k) (TWO-TIME §4.1; re-verified §9 I15) — that O(1)
intraband mass is what killed the per-pair estimate. The record vertex HAS NO
ANALOGUE of it.

### 4.2 The exact coincidence factor at unequal momenta

The insertion transfers momentum (the sharp localizer), so the band-diagonal
elements sit between projectors at different momenta. Exactly (u = k_hat,
v = k_hat', both unit; §9 I7-I8, verified as unnormalized 4x4 identities under
u^2 = v^2 = 1):

```text
(I - alpha.v) S (I - alpha.u) =  S (alpha.(v-u)) (I - alpha.u)
(I + alpha.v) S (I + alpha.u) = -S (alpha.(v-u)) (I + alpha.u)
=>  P_s(k') S P_s(k) = (+-1/2) S (alpha.(k_hat' - k_hat)) P_s(k)

Derivation (minus band; two lines, no expansion): {S, alpha.v} = 0 gives
(I - alpha.v)S = S(I + alpha.v); then (I + alpha.v)(I - alpha.u)
= I - alpha.u + alpha.v - (alpha.v)(alpha.u), and writing alpha.v = alpha.u
+ alpha.(v-u) with (alpha.u)^2 = I collapses it to (alpha.(v-u))(I - alpha.u).
```

So EVERY band-diagonal (intraband, sea-sea or plus-plus) matrix element of a
record insertion vanishes LINEARLY in the unit-momentum increment
|k_hat' - k_hat| <= 2|q|/max(|k|,|k'|): one exact power of coincidence-vanishing
(equivalently one power of |k|^{-1} at bounded transfer) per insertion. The
band-FLIP element is O(1) and full: P_+(k) S P_-(k) = S P_-(k) (§9 I9c).

### 4.3 Per-stratum degree bookkeeping (exact orders, all band configurations)

Fixed stratum X^{(n_-, n_+)}, n_-, n_+ >= 2, with one Gevrey J insertion (the
a-difference's leading order; higher a-orders only add Gevrey factors). The
pairing kernel is a single chain from y to x: external lines C-projected (sea);
each internal line sea or plus; N = n_- + n_+ >= 4 record insertions.

```text
Per record insertion:  band-diagonal channel  -> exact factor |k_hat'-k_hat|
                                                 ~ |q_i|/|k| at bounded transfer
                       band-flip channel      -> O(1), but opens/closes a
                                                 plus-band segment
Per plus-band segment: the segment's free phase oscillates at
                       omega = |k|+|k'| ~ 2|k| (the interband on-shell
                       kinematics of record, TWO-TIME §4.3); the insertion
                       amplitudes' t-dependence is BV/Lipschitz-with-corner
                       (v(t) corner at t = 1/2; chi_hat_{r(t)}(q) entire in
                       r(t); simplex boundaries), so one integration by parts
                       is licit and gains >= one power |k|^{-1} PER SEGMENT —
                       and only power-law is claimed, matching the sealed
                       typing (record strata: POWER-LAW transfer tails only,
                       outside the smooth symbol category; AQ S-2, TT-CHECK §5).
The J insertion:       O(1) in every channel (its longitudinal part -k_hat_x
                       is O(1) intraband — the per-pair killer); Gevrey in its
                       own transfer; never impairs the counting.
Count (2f record flips => >= f plus segments; J may add one flip):
    amplitude degree <= -(N - 2f) - f = -(N - f) <= -(N - floor(N/2)),
    worst case N = 4, f = 2:  degree <= -2.
Mixed transfer regimes do not evade it: a large internal transfer |q_i| ~
|k|^gamma (0 < gamma <= 1) trades the coincidence factor |q_i|/|k| =
|k|^{gamma-1} against the localizer tail chi_hat ~ |q_i|^{-2} = |k|^{-2 gamma}:
the insertion's combined weight |k|^{gamma-1-2 gamma} = |k|^{-1-gamma} <=
|k|^{-1} — never better for the adversary than the coincidence count; escaping
to small internal momentum and returning costs two tails ~ |k|^{-4}.

=>  EVERY fixed >= 2-per-branch stratum has volume-diagonal amplitude degree
    <= -2 at bounded transfer: |amplitude|^2 <= O(|k|^{-4}), integrable
    against d^3k. THE PER-STRATUM VOLUME-DIAGONAL OBSTRUCTION IS STRUCTURALLY
    ABSENT — no fixed stratum carries the C2 Lambda^3 shape.
SCOPE, honest: this is a DEGREE (coincidence-order/amplitude) certification,
    exact at the level of orders and parities. It is NOT a completed
    per-stratum HS NORM: a completed norm would additionally require the
    joint multi-scale composition estimate over all transfer regimes
    simultaneously (chi_hat is L^2 but not L^1 — no absolutely convergent
    transfer bound exists factor-wise), which no exact identity supplies and
    which is not performed here. It does not matter for the verdict: the wall
    below is upstream of it.
```

### 4.4 The answer to the (b)-question — and the resummation reversal

Per stratum: NO intraband survivor persists. The second difference (m_1 = 0
twice over) plus the S-algebra kill the band-diagonal component TWICE PER BRANCH
at coincidence — the record strata are pointwise-in-k intraband-suppressed in a
way the single-insertion stratum's smooth partner (alpha_x, O(1) longitudinal)
never was.

BUT the stratum sum reverses it. The sealed C4 saturation [E1 :346-351],
re-verified as exact arithmetic (§9 I11-I12): at full tau_R,
`exp(-i lambda tau_R S) = (+1,-1,-1)·I` on the stencil (spinor-TRIVIAL scalars,
since e^{-+i pi S} = -I by S^2 = I), and at the operator level

```text
    U(0) = sum_lambda w_lambda u_lambda(0) = m_0 (I - P) + 1·P = P + E ,
```

P the SHARP causal-ball record projector — spinor-trivial, hence with O(1)
band-diagonal transfer elements and sharp (power-law, q^{-2}) tails — and E the
C-L1 operator-collapse error, sealed as an OBLIGATION, NOT a result
(E1 C-L1: "extend to u_lambda = (I-P) + phase_lambda P + [error]"; witness
E1_RECORD_PHASE_OPERATOR_COLLAPSE_UNCERTIFIED; the interleaving corrections have
a sealed name: the C-L2 commutator error [h_0, M(t) tensor S], the S2b/G_cm
obligation — also uncertified). The resummed branch factor is NOT
coincidence-suppressed: the per-stratum |k|^{-n} gains, weighted by the GROWING
moments m_{2j} = -2^{j-1} and fed through the mixed transfer regimes, sum to an
O(1)-band-diagonal sharp object. That is not an estimate — it is the sealed
identity: "the weights PROMOTE the sharp causal-ball projector to the leading
in-cell object."

Exhibit the consequence exactly. First order in the histories on the polydisc:

```text
X = a_+ C U(0)^dagger F C + a_- C F~^dagger U(0) C + O(a^2),
F := -i int_0^1 sum_lambda w_lambda W_lambda(1,t') J(t') W_lambda(t',0) dt'
```

(W_lambda the a = 0 record-dressed propagators; both W-factors belong to the
lambda branch, so the weight sum requires >= 2 insertions ACROSS them — the
counting of §2 unchanged). At the sealed collapse display (C-L1's leading
structure, phases accumulated theta_0(t') = int_0^{t'} v, theta_1(t') =
int_{t'}^1 v, theta_0 + theta_1 = tau_R exactly), the lambda weight sum
collapses BY EXACT STENCIL TRIGONOMETRY (§9 I13, verified as a 4x4 matrix
identity over symbolic theta_0):

```text
sum_lambda w_lambda e^{-i lambda theta_1 S} J e^{-i lambda theta_0 S}
    = c(theta_1 - theta_0) · J ,      c(theta) = (1 - cos(sqrt2 theta))/2 ,
```

because the cross terms vanish by odd moments and, decisively, S J S = -J
(S anticommutes with alpha_x; §9 I6): the (J + SJS) channel — the only channel
the wrapped phases could have cancelled — is IDENTICALLY ZERO, and the (J - SJS)
= 2J channel comes through with the STRICTLY POSITIVE weight c. c(Delta-theta)
= sin^2(sqrt2 Delta-theta / 2) >= 0 vanishes only quadratically at t' = 1/2 and
equals 1 at the endpoints (§9 I14): no kill — a reweighted profile. Therefore,
at the collapse display,

```text
F  =  -i int_0^1 c(Delta-theta(t')) [ball-dressed](t') J(t') [ball-dressed](t') dt' + [E-type errors]
X  ⊃  a_Delta · C P [ -i int c J~ ] P C - type terms + [E-type errors]:
INTRABAND PRINCIPAL PART, exact in structure:
    sigma_intra(X) = -i a_Delta k_hat_x b~_P(x, k_hat) C(k) + (coincidence-
                     suppressed and interband-power-suppressed remainders),
b~_P := the c(Delta-theta)-weighted, sharp-ball-restricted diamond-profile ray
        average — NOT identically zero (c >= 0 with isolated zeros, b_D > 0 on
        the open diamond, ball-diamond overlap nonempty: structural
        positivity, nothing evaluated).
```

Degree 0 in k. Intraband. The chain C·P·[longitudinal J]·P·C has NO
coincidence factor anywhere: P is spinor-trivial (O(1) band-diagonal), J's
longitudinal part is O(1) band-diagonal, the intraband time phases are slow
(massless on-shell marginality: |omega| <= |q| along the sea shell — the
two-time integration is powerless exactly there, TWO-TIME §4.3, sealed). Its
HS^2 at bounded transfer is ~ int d^3k O(1): the C2 Lambda^3 carrier-volume
shape. CARRIER-UNIFORMITY FAILS on this term. The spinor trace of the term is
the sealed S1 identity tr_spinor[C(p) alpha_x] = -2 p_hat_x — killed in the
TRACE by oddness (S1 fine, as of record), squared to no kill in the HS norm
(S2 wall): the sealed S1/S2 division reproduced a third time, now at the summed
quantifier.

---

## 5. STEP 2(c) — THE SHARP LOCALIZER'S TAILS AGAINST THE HS THRESHOLD

```text
The ball indicator's transfer kernel: chi_hat_r(q) = (4 pi / q^3)[sin(qr)
- qr cos(qr)]; leading tail -4 pi r cos(qr)/q^2: DEGREE -2 (surface tail —
power-law only, the sealed typing; no Gevrey mechanism, M(t) not softenable
and NOT softened here).
Against the HS threshold: |chi_hat|^2 ~ q^{-4} is INTEGRABLE (int d^3 q q^{-4}
converges at the UV end): the tails, per insertion, are square-summable — the
transfer directions CLEAR the HS threshold. chi_hat is L^2 but NOT L^1
(int d^3 q |chi_hat| ~ int dq diverges): no absolutely-convergent factor-wise
transfer bound exists — compositions must be estimated jointly (the honest
scope limit of §4.3) — but no DIVERGENCE lives in the tails.
=> THE TAILS ARE NOT THE WALL. The failing direction is the momentum-volume
   direction at bounded transfer — the VOLUME DIAGONAL x = y — exactly as the
   sealed C6 refinement adopted of record ("the fatal local integral is the
   volume diagonal, not the sharp boundary; smoothing only the boundary will
   not remove a |x-y|^{-3} positive majorant", E1 :359-364). This attempt's
   failure term (§4.4) lives exactly there and would survive any boundary
   smoothing: consistent with the seal in both content and locus.
```

---

## 6. STEP 2(d) — WHAT THE SATURATION CLAUSE FORBIDS

```text
Sigma w_lambda u_lambda = P [E1 :346-351], l1-tight, exact. It forbids:
(F1) any route that obtains summed decay from weight cancellation on the
     >= 2-insertion strata — the l1 mass is saturated; the stencil sees the
     fully wrapped phases; "the zero-sum weights buy NO decay";
(F2) any route that certifies the RESUMMED object by per-stratum coincidence
     orders — the clause IS the statement that those orders do not survive
     the sum: the resummed branch factor is the SHARP PROJECTOR, the least
     HS-compatible object in the cell (tr(CPC) = +infinity is C2's own
     divergence, E1 :757-758);
(F3) treating the record dressing as a perturbative decoration: at full tau_R
     it is the LEADING in-cell object, and every summed estimate must pass
     through C P (...) P C - type chains.
It does NOT forbid the per-stratum degree certification of §4.3 (which this
artifact delivers) — it confines its use.
```

---

## 7. STEP 3 — VERDICT

```text
NET = FAILS-AT( THE STRATUM-RESUMMATION STEP, AT THE SEALED SATURATION CLAUSE.
  The exact term: sigma_intra(X) = -i a_Delta k_hat_x b~_P(x,k_hat) C(k) —
  the P-restricted longitudinal intraband survivor of the summed leading
  response (§4.4) — degree 0 at the volume diagonal, HS^2 ~ carrier momentum
  volume (the C2 Lambda^3 shape): carrier-uniformity fails. The chain that
  exhibits it: (i) branch factorization of the summed assembly into second
  differences of unitaries (exact, §2); (ii) C4 kill of all < 2-per-branch
  strata (sealed + §9 I10); (iii) per-stratum coincidence suppression of all
  surviving strata (new exact identities, §4.1-4.3) — the mechanism WORKS
  stratum-wise; (iv) sealed C4 saturation resums the branch strata to the
  sharp spinor-trivial projector P (+ uncertified C-L1 error), restoring an
  O(1) band-diagonal channel; (v) the exact stencil-trig collapse (§9 I13,
  S J S = -J) shows the wrapped weights CANNOT kill the longitudinal J
  channel — the candidate cancelling channel (J + SJS) is identically zero
  and the surviving channel carries strictly positive weight c(Delta-theta);
  (vi) the composite C P J_long P C is degree-0 intraband, immune to two-time
  decay (slow intraband phases, sealed massless marginality) and to boundary
  smoothing (volume locus).
  HONEST CONDITIONALITY, stated plainly: steps (iv)-(v) are exact AT the
  sealed C4 operator-level display; its error term is the UNCERTIFIED C-L1
  object (witness E1_RECORD_PHASE_OPERATOR_COLLAPSE_UNCERTIFIED; interleaving
  corrections = the uncertified C-L2/S2b commutator error). The failure
  exhibited is the failure of the LEADING sealed structure; overturning it
  would require certifying that the error term carries an EXACTLY opposite
  degree-0 intraband component — an exact-conspiracy identity of which
  nothing sealed shows a trace (and which would itself be a major new
  certified identity, not a repair of this analysis). The only other named
  repair — softening M(t) — is sealed away [E1 :1123-1124] and was not
  touched. )

SUBSIDIARY POSITIVE (REFORMULATED-grade, delivered, not claimed as B-L2*):
  PER-STRATUM VOLUME-DIAGONAL DEGREE CERTIFICATION — every fixed
  >= 2-per-branch stratum of the summed assembly has intraband coincidence
  order >= 2 per branch (exact identity P_s(k')SP_s(k) =
  (+-1/2)S(alpha.(k_hat'-k_hat))P_s(k)) and worst-configuration amplitude
  degree <= -2 at bounded transfer: past the -3/2 HS threshold stratum-wise.
  The first symbol-level analysis of the sharp strata (none existed sealed:
  AQ §3.2 UNBUILT clause). Residual named exactly: (r1) the resummation
  across strata — blocked by saturation, the FAILS-AT above; (r2) the
  completed per-stratum HS NORM (joint multi-scale transfer composition;
  chi_hat not L^1) — not performed; (r3) the summed-S2' sealed target —
  a spec-author act, not a lane's.

WHY NOT THE OTHER VERDICTS: not PROVED — (r1) is fatal at the leading sealed
  display and (r2)/(r3) are open even stratum-wise. Not UNDECIDABLE-AT — the
  missing object (certified C-L1 error) is needed to OVERTURN the failure,
  not to exhibit it: the leading term is exhibited from sealed displays plus
  exact new identities, the sealed lineage's standard for a FAILS report
  (TWO-TIME NET = FAILS at the per-pair quantifier, confirmed of record).
  Not bare REFORMULATED — the reformulated content is delivered above but
  the tasked certification itself FAILS at a located step, and the honest
  report names that step.
```

---

## 8. STEP 4 — EFFECT ON THE SUMMED-FIXED HORN (stated at sealed strength, no more)

Per the sealed blocked-chain (AQ Det.4, CONFIRMED): the summed-assembly FIXED
horn is blocked on exactly three debts — (1) B-L2* (this attempt), (2) the F'-14
log-of-sum passage, (3) the unsealed summed-S2' re-quantification act.

```text
THIS RESULT (CLAIMED, single-lane, conditional as stated in §7): debt (1)
moves from UNBUILT to ATTEMPTED-AND-FAILING-AT-A-NAMED-STEP: the >= 2-insertion
strata do NOT certify carrier-uniformly at the volume diagonal at the sealed
leading collapse; the failure relocates INSIDE B-L2* to a single named object —
the uncertified C-L1/C-L2 error structure of the record-phase operator collapse.
If this stands under check, the summed-FIXED horn's remaining life is confined
to an exact-cancellation property of that error term (nothing sealed suggests
one), OR to a successor spec that lawfully re-forms the object. DO NOT
OVERSTATE: debts (2) F'-14 and (3) the summed-S2' spec act REMAIN REGARDLESS —
even a rescued B-L2* would still face both; a failed B-L2* makes them moot for
the FIXED horn but they stand as sealed obligations of the architecture.
Per-pair, nothing moves: the FIXED horn stays dead as architected (52f2490b of
record); RUNNING stays a lean, unforced, no sealed target — none created here.
The equal-time route stays FALSE (C6); M(t) stays sharp; no repair was
attempted through it.
```

---

## 9. THE SCRIPT (exact symbolic verification; reproduced in full) AND ITS OUTPUT

Run with sympy 1.14.0 (fresh venv; CAS used for exact matrix/trig identities over
symbols ONLY — no numeric evaluation of any physical quantity).

```python
# BL2STAR: exact symbolic verification of the load-bearing identities.
# EXACT SYMBOLIC ONLY: polynomial/trig matrix identities over symbols; nothing numeric evaluated.
import sympy as sp

I2 = sp.eye(2); Z2 = sp.zeros(2, 2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])

# Dirac representation, exactly as the PA-pinned executor (3d8aea1a..., dirac_data()):
g0 = sp.Matrix(sp.BlockMatrix([[I2, Z2], [Z2, -I2]]).as_explicit())
def gj(s):  # gamma^j = [[0, sigma],[-sigma, 0]]
    return sp.Matrix(sp.BlockMatrix([[Z2, s], [-s, Z2]]).as_explicit())
g1, g2, g3 = gj(sx), gj(sy), gj(sz)
g5 = sp.I * g0 * g1 * g2 * g3
S  = -sp.I * g0 * g5                      # S = -i slash(n) gamma^5, slash(n) = gamma^0
ax, ay, az = g0*g1, g0*g2, g0*g3          # alpha_j = gamma^0 gamma^j
I4 = sp.eye(4)

ux, uy, uz, vx, vy, vz = sp.symbols('ux uy uz vx vy vz', real=True)
t0, t1 = sp.symbols('theta0 theta1', real=True)

def unit_reduce(M, subs_pairs):
    M = sp.expand(M)
    for lhs, rhs in subs_pairs:
        M = sp.expand(M.subs(lhs, rhs)); M = sp.expand(M.subs(lhs, rhs))
    return sp.simplify(sp.expand(M))

def zero(M, subs_pairs=()):
    return unit_reduce(M, subs_pairs) == sp.zeros(*M.shape)

Mu = ux*ax + uy*ay + uz*az               # alpha.u  (u = k_hat, unit)
Mv = vx*ax + vy*ay + vz*az               # alpha.v  (v = k_hat', unit)
Du = (vx-ux)*ax + (vy-uy)*ay + (vz-uz)*az  # alpha.(v - u)
u2 = [(ux**2, 1 - uy**2 - uz**2)]
v2 = [(vx**2, 1 - vy**2 - vz**2)]

print("I1  S^2 = I                                :", zero(S*S - I4))
print("I2  S dagger = S                           :", zero(S.H - S))
print("I3  {S, alpha_x} = 0                       :", zero(S*ax + ax*S))
print("I4  {S, alpha_y} = 0                       :", zero(S*ay + ay*S))
print("I5  {S, alpha_z} = 0                       :", zero(S*az + az*S))
print("I6  S alpha_x S = -alpha_x  [=> J+SJS=0]   :", zero(S*ax*S + ax))
# I7: band-diagonal coincidence factor, minus band (sea):
#     (I - alpha.v) S (I - alpha.u) = S (alpha.(v-u)) (I - alpha.u),  u,v unit.
print("I7  (I-Mv) S (I-Mu) = S Du (I-Mu)          :",
      zero((I4-Mv)*S*(I4-Mu) - S*Du*(I4-Mu), u2+v2))
# I8: plus band: (I + alpha.v) S (I + alpha.u) = -S (alpha.(v-u)) (I + alpha.u).
print("I8  (I+Mv) S (I+Mu) = -S Du (I+Mu)         :",
      zero((I4+Mv)*S*(I4+Mu) + S*Du*(I4+Mu), u2+v2))
# I9: equal-momentum band-diagonal parts vanish exactly; interband is full:
print("I9a (I-Mu) S (I-Mu) = 0                    :", zero((I4-Mu)*S*(I4-Mu), u2))
print("I9b (I+Mu) S (I+Mu) = 0                    :", zero((I4+Mu)*S*(I4+Mu), u2))
print("I9c (I+Mu) S (I-Mu) = 2 S (I-Mu)  (flip O(1)):", zero((I4+Mu)*S*(I4-Mu) - 2*S*(I4-Mu), u2))
# I10: the C4 stencil moments: w = (-1/4, 1/2, -1/4) on lambda = (sqrt2, 0, -sqrt2).
lam = [sp.sqrt(2), sp.Integer(0), -sp.sqrt(2)]
w   = [sp.Rational(-1,4), sp.Rational(1,2), sp.Rational(-1,4)]
mom = lambda n: sp.simplify(sum(wi*li**n for wi, li in zip(w, lam)))
print("I10 m_0,m_1,m_2,m_3,m_4 = 0,0,-1,0,-2      :",
      [mom(0), mom(1), mom(2), mom(3), mom(4)] == [0, 0, -1, 0, -2])
# I11: saturation at full tau_R = pi/sqrt2: phases on the stencil:
tauR = sp.pi/sp.sqrt(2)
phases = [sp.simplify(sp.cos(li*tauR)) for li in lam]     # exp(-i li tauR S) = cos(li tauR) I - i sin(li tauR) S
sins   = [sp.simplify(sp.sin(li*tauR)) for li in lam]
print("I11 phases cos(lam tauR) = (-1, 1, -1); sin = 0:",
      phases == [-1, 1, -1] and sins == [0, 0, 0])
sat  = sp.simplify(sum(wi*ci for wi, ci in zip(w, phases)))
l1   = sum(abs(wi) for wi in w)
print("I12 sum w_l phase_l = 1 = sum |w_l| (l1-tight):", sat == 1 and l1 == 1)
# I13: the collapsed two-time weight-sum identity:
#      sum_l w_l e^{-i l theta1 S} alpha_x e^{-i l theta0 S} = c(theta1-theta0) alpha_x
#      with c(t) = (1 - cos(sqrt2 t))/2, on the constraint theta0 + theta1 = tau_R = pi/sqrt2.
def erec(li, th):  # exp(-i li th S) exactly via S^2 = I
    return sp.cos(li*th)*I4 - sp.I*sp.sin(li*th)*S
lhs = sp.zeros(4, 4)
for wi, li in zip(w, lam):
    lhs = lhs + wi * erec(li, t1) * ax * erec(li, t0)
lhs = lhs.subs(t1, tauR - t0)
c_delta = (1 - sp.cos(sp.sqrt(2)*((tauR - t0) - t0)))/2
D = sp.simplify(sp.expand_trig(sp.expand(lhs - c_delta*ax)))
print("I13 sum_l w_l e^{-il th1 S} ax e^{-il th0 S} = c(th1-th0) ax  (th0+th1=tauR):",
      D == sp.zeros(4, 4))
# I14: c vanishes only quadratically at Delta=0 and c(+-tauR) = 1 (stencil sees full wrap):
cfun = lambda th: (1 - sp.cos(sp.sqrt(2)*th))/2
print("I14 c(0)=0, c'(0)=0, c''(0)=1, c(tauR)=1     :",
      [cfun(0), sp.diff(cfun(sp.Symbol('q')), 'q').subs('q', 0),
       sp.simplify(sp.diff(cfun(sp.Symbol('q')), 'q', 2).subs('q', 0)),
       sp.simplify(cfun(tauR))] == [0, 0, 1, 1])
# I15: sea-projector sandwich of the smooth vertex (TWO-TIME C3 reused): C ax C = -u_x C at u:
KM = I4 - Mu   # 2*C(k) at unit u
print("I15 (I-Mu) ax (I-Mu) = -2 ux (I-Mu)        :", zero(KM*ax*KM + 2*ux*KM, u2))
```

Output, verbatim:

```text
I1  S^2 = I                                : True
I2  S dagger = S                           : True
I3  {S, alpha_x} = 0                       : True
I4  {S, alpha_y} = 0                       : True
I5  {S, alpha_z} = 0                       : True
I6  S alpha_x S = -alpha_x  [=> J+SJS=0]   : True
I7  (I-Mv) S (I-Mu) = S Du (I-Mu)          : True
I8  (I+Mv) S (I+Mu) = -S Du (I+Mu)         : True
I9a (I-Mu) S (I-Mu) = 0                    : True
I9b (I+Mu) S (I+Mu) = 0                    : True
I9c (I+Mu) S (I-Mu) = 2 S (I-Mu)  (flip O(1)): True
I10 m_0,m_1,m_2,m_3,m_4 = 0,0,-1,0,-2      : True
I11 phases cos(lam tauR) = (-1, 1, -1); sin = 0: True
I12 sum w_l phase_l = 1 = sum |w_l| (l1-tight): True
I13 sum_l w_l e^{-il th1 S} ax e^{-il th0 S} = c(th1-th0) ax  (th0+th1=tauR): True
I14 c(0)=0, c'(0)=0, c''(0)=1, c(tauR)=1     : True
I15 (I-Mu) ax (I-Mu) = -2 ux (I-Mu)        : True
```

(Stencil ordering note: I11 lists lambda = (+sqrt2, 0, -sqrt2), so (-1, +1, -1)
is the sealed "(+1, -1, -1) on lambda = (0, +sqrt2, -sqrt2)" in this artifact's
ordering — same content.)

---

## 10. FLAG BLOCK

```text
STRATUM_OBJECT = EXACT(
  X(a_+,a_-) = sum_{mu,lambda} w_mu w_lambda C(V_{mu lambda}(a) -
  V_{mu lambda}(0))C = C[U(a_-)^dag U(a_+) - U(0)^dag U(0)]C with U(a) =
  -(1/4)[u_{+sqrt2}(a) - 2 u_0(a) + u_{-sqrt2}(a)] — the branch-factorized
  second difference of unitaries (weights real, (1/2,-1/4,-1/4), E1 :340-342;
  V per pair E1 :652-661 [42492,42704); assembly PA :212-214 [8096,8192);
  Z_comp E1 :669-674 [43297,43698)). Record grading: m_0 = m_1 = 0 kills all
  < 2-insertion-per-branch strata (E1 :343-345, in C4 :339-352); survivors
  n_-, n_+ >= 2 even, moments m_{2j} = -2^{j-1}; two-time: insertions at
  independent Dyson-ordered times interleaved with h_0 (E1 :510-513; PA
  :371-380). Sharp M(t) = Q 1_{|x|<=r(t)} Q sealed (E1 :465-470); B-L2*
  obligation at E1 bytes [57212,58506), span digest 162e30a6 MATCH; locus =
  VOLUME diagonal; record_vertex_two_time_HS_certified = false (E1 :2191).
  Carrier-uniform = uniform over the Hermite-Galerkin D3 refinement family
  (PA A1; E1 :826-832). HS threshold at the volume diagonal: coincidence
  degree > -3/2 (C degree -3 exact, E1 C1).)

SECOND_DIFFERENCE_GAIN = TWO-ORDERS-PER-BRANCH-STRATUMWISE-ZERO-SUMMED(
  exact order effect at the diagonal: (i) m_0 = m_1 = 0 forces >= 2 record
  insertions per branch; (ii) NEW EXACT IDENTITY: the record spinor factor
  S = -i gamma^0 gamma^5 anticommutes with every alpha_j (§9 I3-I5), so
  P_s(k')SP_s(k) = (+-1/2) S (alpha.(k_hat'-k_hat)) P_s(k) (§9 I7-I8) — ONE
  exact coincidence order per insertion, hence >= TWO per branch, >= FOUR on
  the all-intraband channel: fixed-stratum volume-diagonal amplitude degree
  drops from 0 (the C2 Lambda^3 shape) to <= -2 worst-configuration
  (<= -4 all-intraband), strictly past the -3/2 HS threshold; (iii) the gain
  is PER-STRATUM ONLY: at full tau_R the stencil sees the fully wrapped
  phases (+1,-1,-1), the second difference saturates (l1-tight, §9 I11-I12)
  and the summed gain is ZERO — the sealed "zero-sum weights buy NO decay"
  (E1 :346-351) reproduced as exact stencil arithmetic.)

BAND_SPLIT_ON_STRATUM = NO-SURVIVOR-PER-STRATUM-SURVIVOR-BY-RESUMMATION(
  the algebra: per fixed stratum the intraband part does NOT inherit a
  survivor — every band-diagonal record element vanishes linearly at
  coincidence (P_s S P_s = 0 at every k, §9 I9a/I9b; flip channel full,
  P_+SP_- = SP_-, §9 I9c); the second difference (m_1 = 0 twice over) plus
  the S-algebra kill the band-diagonal component the smooth single-insertion
  object could not lose. BUT the stratum SUM reverses it: C4 saturation
  resums the branch to the sharp spinor-trivial ball projector,
  U(0) = P + E (E = the UNCERTIFIED C-L1 error, witness
  E1_RECORD_PHASE_OPERATOR_COLLAPSE_UNCERTIFIED; interleaving = the
  uncertified C-L2/S2b commutator error), P's band-diagonal elements O(1);
  the exact stencil-trig collapse sum_l w_l e^{-il th1 S} J e^{-il th0 S} =
  c(th1-th0) J (§9 I13; decisive: SJS = -J so the cancellable channel
  J + SJS is IDENTICALLY zero, §9 I6) carries the longitudinal J through
  with strictly positive weight c = sin^2(sqrt2 Delta-theta/2): the summed
  leading response contains sigma_intra(X) = -i a_Delta k_hat_x
  b~_P(x,k_hat) C(k) — degree 0, intraband, carrier-volume HS.)

TAIL_DEGREE = MINUS-2-PER-INSERTION-CLEARS-THRESHOLD(
  chi_hat_r(q) leading tail -4 pi r cos(qr)/q^2: degree -2, power-law only
  (sealed typing; M(t) untouched); |chi_hat|^2 ~ q^{-4} integrable — the
  transfer directions clear the HS threshold; chi_hat is L^2 not L^1, so
  factor-wise absolute transfer bounds do not exist (joint estimates
  required — named residual r2); the tails are NOT the wall: the failing
  direction is the momentum volume at bounded transfer = the VOLUME diagonal,
  exactly the sealed C6 refinement (E1 :359-364), and the exhibited failure
  term survives any boundary smoothing — locus consistent with seal.)

NET = FAILS-AT(
  the stratum-resummation step at the sealed saturation clause (E1 :346-351)
  — the term: the P-restricted longitudinal intraband survivor
  -i a_Delta k_hat_x b~_P(x,k_hat) C(k), degree 0 at the volume diagonal,
  HS^2 ~ carrier momentum volume (C2 Lambda^3 shape): the carrier-uniform
  two-time HS certification of the >= 2-insertion strata FAILS at the sealed
  leading collapse. Chain: branch factorization (exact) -> C4 kill (sealed)
  -> per-stratum coincidence suppression (new exact identities — the
  mechanism works stratum-wise) -> C4 saturation resums to P + E ->
  stencil-trig collapse passes the longitudinal J channel (J + SJS = 0
  identically; c > 0 a.e.) -> C P J_long P C degree-0 intraband, immune to
  two-time decay (slow intraband phases; massless on-shell marginality,
  sealed) and to boundary smoothing. CONDITIONALITY, honest: exhibited AT
  the sealed C4 operator-level display; overturning it requires certifying
  an exactly-opposite degree-0 intraband component in the UNCERTIFIED C-L1/
  C-L2 error — nothing sealed supplies one; the only other named repair,
  softening M(t), is sealed away (E1 :1123-1124) and was not touched.
  SUBSIDIARY DELIVERED (reformulated-grade, not B-L2*): per-stratum
  volume-diagonal degree certification of ALL fixed >= 2-per-branch strata
  (first symbol-level analysis of the sharp strata; residuals named: the
  resummation wall r1, the joint multi-scale norm completion r2, the
  unsealed summed-S2' target r3).)

EFFECT_ON_SUMMED_FIXED = DEBT-1-ATTEMPTED-FAILING(
  debt 1 of 3 moves from unbuilt to failing-at-a-named-step (CLAIMED,
  conditional at the sealed leading collapse); the summed-FIXED horn's
  remaining life confines to an exact-cancellation property of the
  uncertified C-L1/C-L2 error (nothing sealed suggests one) or a successor
  spec act; debts 2 (F'-14) and 3 (summed-S2') REMAIN REGARDLESS; per-pair
  nothing moves (FIXED dead as architected, 52f2490b of record; RUNNING
  stays an unforced lean, no target created).)

SEALS_VERIFIED = 7/7(
  46846730 E1; 789338ad PA; 18af3dee TWO-TIME; 6a2aa0fd TT-CHECK; 0a10c030
  AQ; 331035d3 AQ-CHECK; 3d8aea1a PA-pinned executor (digest pinned inside
  the sealed PA hash table, recomputed at path) — all recomputed at path
  this session, all matching sidecars and tasked digests; the E1 B-L2* byte
  span [57212,58506) recomputed to 162e30a6 MATCH; every cited line span
  read at path; none unverifiable.)

FORBIDDEN_IMPORTS = none(
  no scale, no imported GR, no faithfulness authority; scale-bearing sealed
  text read SUSPECT-ONLY to fix structure; M(t) not softened, equal-time not
  resurrected; no register/tracker/plan/road/ledger/lens file read; no
  physical quantity computed, bounded numerically, or evaluated — degrees,
  orders, parities, coincidence orders, and exact stencil arithmetic only;
  all constants symbolic.)

MACHINERY_INVOKED = yes(CAS identity checks only — sympy 1.14.0 verifying
  seventeen exact matrix/trig/stencil identities over symbols, script and
  output reproduced verbatim in §9; shasum/file reads/byte extractions
  otherwise; NOTHING numeric evaluated.)

alpha_computed = false ; kappa_record_computed = false ;
proof_authorized = false ; coupling_evaluation_authorized = false
ALL_RESULTS = CLAIMED until checked.
BL2STAR_ATTEMPT_RESULT = SEALED.
```
