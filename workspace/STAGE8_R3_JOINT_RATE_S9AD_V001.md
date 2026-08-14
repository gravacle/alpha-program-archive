# STAGE 8 — r-3 OF RECORD: THE JOINT POLYDISC RATE ||R_n Delta_n(a)||_1 = o(-log|det_n(0)|) FOR THE CARRIER COMPRESSION FAMILY OF RECORD

## BLIND BUILDER — CODENAME R3-BUILD — COMMISSION S9AD — [SEALED]

Date: 2026-08-14
Role: BLIND builder (R3-BUILD). Task: establish or refuse, from the sealed
stock only, the r-3 joint-rate input of the adopted clause R-L4a-N —
||R_n Delta_n(a)||_1 = o(-log|det_n(0)|) UNIFORMLY on the closed pair
polydisc, in the exact factorization frame det(1 + A_n(a)) =
det(1 + A_n(0)) det(1 + R_n Delta_n(a)) with 1 + A_n(0) invertible — the
ONLY remaining input for R-L4b's discharge at the adopted naming, r-2
having landed B1-DERIVED, sealed and checked. "Q-..." tokens inside sealed
artifacts are EXPECTED-UNLOCATABLE by design; noted, never chased.

Gates: `alpha_computed = false` ; `proof_authorized = false` ;
`kappa_record_computed = false`. ALL_RESULTS = CLAIMED until checked.

Fences held: EXACT SYMBOLIC DERIVATION ONLY — one CAS battery (sympy
1.14.0, fresh venv `r3venv` under the session scratchpad), reproduced
verbatim in §7 (10/10 PASS on the final run; ONE pre-final harness-form
correction disclosed in §7's header: sympy returns the D5 scalar Duhamel
integral as a Piecewise over the aJ != 0 / aJ = 0 branches and the check
was made branch-aware — the identity itself is unconditional and no
mathematical claim changed); every constant symbolic or an exact rational;
NOTHING numeric evaluated; no measured constant; NO value frozen (no
numeric kappa, M, delta, D, or rate constant; eps_* and every profile norm
stay symbols; every conclusion is a limit/o(.) statement or a named
refusal); M(t) and 1_{D_t} consumed SHARP (D6'); the stricken display
(E1 :773-778) consumed NOWHERE as ground; no
register/road_/ledger/lens/plan/tracker/THE_HANDOFF file opened; no git
action; no existing file edited; ONE output file (this artifact) plus its
seal sidecar at the commission-distinct path, probed ABSENT before write.
Every enumeration/uniqueness sentence below claims only its own displayed
sweep. Marks: DERIVED / CLAIMED / CONDITIONAL(premise named) span by span.

---

## 0. VERDICT IN ONE LINE

**(NOT-DERIVABLE-TODAY), with five named partial results DERIVED and the
missing objects named exactly: the r-3 joint rate is a RACE OF TWO
DIVERGENCES on which the sealed stock certifies divergence on both sides
but a RATE on neither. Derived here: (P-1) the frame re-derived at bytes
division-free (CAS D1), with its own hazard confronted — invertibility of
1 + A_n(0) is GENERIC-ONLY per member (eigenvalues 1 - 2 s_i; no sealed
input excludes s_i = 1/2), ||1 + A_n(0)||_op <= 1 EXACT, and
||R_n||_op = 1/min_i|1 - 2 s_i| >= 1 with NO n-uniform bound on any sealed
artifact — the resolvent factor is exactly the S4/H-R shape the record
restricts to the surviving sector and forbids defaulting (E1 :720-727,
F'-3), and r-2's kappa_n -> infinity is CONSISTENT with ||R_n||_op ->
infinity at any speed, since s_i near 1/2 MAXIMIZES per-eigenvalue kappa
mass (CAS D2); (P-2) constructibility — Delta_n(a) is finite-rank
(<= 4n^3) entire in (a_+, a_-), and a NEW n-free polydisc-uniform
OPERATOR-norm bound ||Delta_n(a)||_op <= c(eps_*) = eps_* e^{eps_*}
(1 + e^{eps_*}) is DERIVED by Duhamel from the PA generator (a multiplies
J alone, ||J_n(t)|| <= ||b_D||_inf = 1 derived exactly, CAS D5/D6/D7),
consistent with the sealed n-free V-factor bound (52f2490b LINK 2); (P-3)
the reduction o(kappa_n) => o(-log|det_n(0)|) via the sealed chain
-log|det_n(0)| >= kappa_n (CAS D8) — SUFFICIENT-ONLY, the reverse bound
refuted at the check's n-1 shape (single s_i -> 1/2: -log|det| unbounded
at bounded kappa mass, CAS D9); (P-4) at a = 0 the numerator is EXACTLY 0
(Delta_n(0) = 0): the statement is entirely about a != 0; (P-5, negative,
the obstruction made exact) Delta_n(a) = (1 + A_n(0)) R_n Delta_n(a)
exactly, so ||R_n Delta_n(a)||_1 >= ||R_n Delta_n(a)||_2 >=
||Delta_n(a)||_2 (CAS D3), and OF RECORD sup_n ||Delta_n(a)||_2 =
+infinity per pair (52f2490b; ZF §4.1(c)): THE NUMERATOR DIVERGES ALONG
THE FAMILY — no bounded-numerator shortcut exists — while the rank x
op-norm budget PROVABLY CANNOT close the estimate: the numerator budget
4n^3 c(eps) and the kappa ceiling kappa_n <= 2n^3 carry the SAME carrier
power, the ratio is n-free and never o(1) (CAS D4/D10), so ANY
product-of-norms discharge REQUIRES a sub-volume trace-norm rate for
Delta_n(a) — precisely the OPEN R-L2b sharpened target (p unknown, alpha
underived, of record). Missing objects, exactly: MO-1 an n-uniform (or
rate-quantified) resolvent bound on R_n; MO-2 a certified lower RATE for
kappa_n or for -log|det_n(0)| (r-2's lower-semicontinuity route is
rate-free by construction); MO-3 a certified sub-volume trace-norm rate
for Delta_n(a) (uniform constant REFUTED of record; only a rate remains
possible); MO-4 (alternative) a product-level cancellation identity for
R_n Delta_n(a) — none exists in the corpus (sweep displayed, §4.4). F-d is
NOT exhibited: nothing here bounds det(1 + A_n(a*)) away from 0 along the
family; the F-d hazard needs exactly the uniform control that is missing.
R-L4b is NOT discharged and NOT refuted here; nothing fires; all three
R-L4 witnesses STAND. CAS battery 10/10 PASS.**

---

## 1. SEALS VERIFIED AT PATH (shasum -a 256), BEFORE ANY RELIANCE

Workspace files under `/Users/bgm/MB Work/alpha-program-archive/workspace/`;
the clause under `/Users/bgm/MB Work/alpha_supervision/`. Every digest
recomputed from bytes at path THIS session by FULL digest and compared
against sidecar and/or the tasked/citing pinned digest. 10/10 MATCH.

```text
G-1  72d5343ea2961e16733b01a90e517f92171be7f603eb95bf1999efdfc4839aa7
     R_L4A_N_CLAUSE_V002_ADOPTED_2026-08-14.md      MATCH (path, sidecar,
     tasked) — THE ADOPTED CLAUSE; N.2 domain; N.3 dichotomy + the r-3
     frame (:84-89); N.4; N.5 F-a..F-d (:101-131); read in full.
G-2  e1da7446242de98a4997b778eaad5e791e192084852d4a8e4024e4b87c690ed6
     STAGE8_R1_NAMING_CANDIDATE_V001.md             MATCH (sidecar, tasked)
     — the candidate; CAS C3 frame (:486-503, output :525); S2 stock
     enumeration; read in full.
G-3  3b5e95b6da98a99e510515deab518b25554feb74145f6e754944262a17e7ab9f
     STAGE8_R2_KAPPA_N_DETERMINATION_S9AD_V001.md   MATCH (sidecar, tasked)
     — r-2 OF RECORD, sealed AND checked: kappa_n -> +infinity full-family
     (:33-55); the exact chain |det_n(0)|^2 <= exp(-2 kappa_n) (X-1,
     :371-379); CH-A realization premise (:511-526); read in full.
G-4  a4cf394c7c94feab39bf9437e3112ceb719f07a251ff772dcca1661e044521fb
     STAGE8_R2_KAPPA_N_DETERMINATION_S9AD_AUDIT_V001.md  MATCH (sidecar,
     tasked) — CONFIRMED-WITH-CORRECTIONS, all cosmetic, none verdict-chain
     (:34-68): r-2 consumable at audited grade.
G-5  468467303a109dc825b015107897dacc107800fc981030377c3f006b384cccb5
     STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md    MATCH (sidecar, tasked)
     — C1 :320-329; C4 :339-352; C6 :353-370; M-2/D4 :400-402; R.0
     :650-666; S2 :696-700; S4 :720-727; R.2 :739-762; clauses :766-790;
     stricken display :773-778.
G-6  a903716c23c1a6969932e988f90d464abe9e8ee96624cd2dce3e32416de132e0
     STAGE8_RL4_RL0_CERTIFICATION_V001.md           MATCH (sidecar, tasked)
     — §2.3(c) :228-249; §2.3(d) :251-273; §2.4 :287-314 (the frame
     :296-300; the joint rate :302-304; the S4-resolvent identification
     :304-306).
G-7  26f9314bdbbf1d7638ecbdf398c891cb3ba54251d4b40314df39c03ab48c08b7
     STAGE8_ZERO_FREE_DERIVATION_V001.md            MATCH (sidecar, tasked)
     — §4.1(b) :332-339 (fixed-n analyticity); §4.1(c) :340-346 (per-pair
     sup_n ||Delta_n(a)||_2 = +infinity of record); o-1 :394-399.
G-8  789338adb7d3d36da453113e98f371a4f92543cf2652b047f8481c407bed5bc3
     STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md
     MATCH (sidecar, tasked) — A1 :48-92 (carrier dim n^3 x C^4, nested,
     strong); A2 :94-142 (b_D :99-113; J = -B_D tensor alpha_x :117-127;
     h_lambda(t;a) = h_0 + lambda v M tensor S + a J :124-128); A3
     :181-182 (u_lambda(a) = the propagator generated by h_lambda(t;a)).
G-9  52f2490b187fd4b307c2af45f6238ea02f1d6839b23466fefee1dbba47ed6241
     STAGE8_RL2B_UNIFORMITY_REFUTED_RESULT_V001.md  MATCH (sidecar; pinned
     at r-2's G-7, ZF §4.1(c), CERT) — chased citation, read in full: §0
     the refutation chain :17-26; LINK 1 :78-82 (sup_n ||C_n|| <= 1, both
     schemes); LINK 2 :83-98 (SEALED n-free polydisc V-factor bound +
     adjoint-continuation closure); LINK 6 :116-119 (||X||_2 = infinity,
     C1 degree -3); LINK 7 :120 (weak LSC); flags :179-203
     (V_factor_uniform_bound = true; X_HS_norm_infinite = true).
G-10 685afac8205b4ed2ed0a309a321f6eccc940882e89ec3dfbce70fd9b8d74af52
     STAGE8_RL4_RL0_CHECK_V001.md                   MATCH (sidecar; pinned
     at r-2's G-5) — chased citation: n-1 :310-317 (a single s_i -> 1/2
     drives det_n(0) -> 0 at bounded commutator mass); n-2 :318-323 (the
     joint rate is the SUFFICIENT estimate for the factorization route);
     n-3 :324-329 (ZF o-1's "carrier volume" phrase is a paraphrase —
     attribution note; the refutation's own chain is LSC-based).
SWEEP-LOCATED, seal verified before citation:
G-11 d1807b967ad94c915f67c5fe004eed7c972f03589648128d76c9a8cc42068f86
     STAGE8_RL2B_COMMUTATOR_ROUTE_REFUTED_AND_TARGET_SHARPENED_V001.md
     MATCH (sidecar) — §4 :110-137: the R-L2b sharpened target OPEN
     ("p unknown", "alpha not derived"); consumed ONLY as status evidence
     for MO-3's openness (E1 S2 :696-700 already states alpha unasserted).
```

EXPECTED-UNLOCATABLE tokens this session: "Q-1059", "Q-1062", "Q-1054"
(register pointers inside sealed artifacts) — noted per standing design;
not chased; nothing defaulted.

---

## 2. SUB-TASK 1 — THE FRAME, AT BYTES (invertibility and the resolvent hazard confronted FIRST)

### 2.1 The frame re-derived (DERIVED, exact)

The sealed displays: A_{mu lambda, n}(a) = C_n(V_{mu lambda}(a) - 1)C_n
(ZF §4.1(b) :332-339; clause N.1 :41); Delta_{mu lambda}(a) = A(a) - A(0)
= C(V(a) - V(0))C (E1 R.0 :661, at the family member C = C_n); baseline
A_n(0) = -2 C_n P C_n on ran C_n on opposite-phase pairs (E1 R.2
:746-748; clause N.1 :44-45); the frame (CERT §2.4 :296-300; clause N.3
:84-89):

```text
  det(1 + A_n(a)) = det(1 + A_n(0)) · det(1 + R_n Delta_n(a)),
  R_n = (1 + A_n(0))^{-1},   valid WHERE 1 + A_n(0) is invertible.
```

Re-derivation, division-free, at the displayed sweep (CAS D1, matching
the candidate's CAS C3 at e1da7446 :486-503): for any square A_0, A,

```text
  (1 + A_0)(D_0 I + adj(1 + A_0)(A - A_0)) = D_0 (1 + A),  D_0 = det(1+A_0),
```

with det multiplicativity; where D_0 != 0 divide by D_0 and take
determinants. DERIVED. All finite-dimensional objects here live on
ran C_n (R-L1 block-triangular identity, E1 :657-659), rank <= 4n^3.

### 2.2 Invertibility per member: GENERIC-ONLY, not certified (the frame's first hazard)

On ran C_n the baseline 1 + A_n(0) = 1 - 2 C_n P C_n has eigenvalues
1 - 2 s_i, s_i in [0, 1] (CERT §2.3(c) :232-235). It is invertible iff NO
s_i = 1/2 exactly. The sealed stock's exact position (CERT §2.4 :289-292):
det(1 + A_n(a)) "equals prod(1 - 2 s_i) != 0 at a = 0 UNLESS some s_i =
1/2 exactly ... a spectral coincidence no sealed input supplies." That is:
no sealed input FORCES a coincidence, and no sealed input EXCLUDES one.
The frame is therefore PER-MEMBER CONDITIONAL of record — exactly as both
CERT (:294-295 "where 1 + A_n(0) is invertible") and the clause (:87-89)
write it. At a member with some s_i = 1/2: det_n(0) = 0 (that member's
baseline vanishing is automatic), R_n is undefined, and BOTH sides of the
r-3 statement degenerate (-log|det_n(0)| = +infinity). No repair is
available or attempted here; the derivation below quantifies over the
members where the frame is defined, as the frame itself does. [DERIVED at
the sealed bytes; nothing new asserted.]

### 2.3 The two exact norm facts, and what R_n does as n grows (the second hazard)

```text
FRAME-N1 (DERIVED, exact):  ||1 + A_n(0)||_op = max_i |1 - 2 s_i| <= 1.
  Ground: s_i in [0, 1] => (1 - 2s_i)^2 <= 1, an exact inequality whose
  solution set IS [0,1] (CAS D2). The baseline direction of the frame is
  a CONTRACTION — this is the load-bearing half of §4.3's lower bound.
FRAME-N2 (DERIVED, exact):  ||R_n||_op = 1/min_i |1 - 2 s_i| >= 1,
  and NO n-uniform bound on ||R_n||_op exists on any sealed artifact:
  (i)  a uniform bound is EXACTLY a uniform 1/2-avoidance statement
       (exists delta: |s_i - 1/2| >= delta all i, n <=> sup_n ||R_n||_op
       <= 1/(2 delta)) — one of the two B2 hypotheses, UNSEALED ON BOTH
       SIDES of record (clause N.3(B2)/(B3) :76-82; r-2 refutes only the
       OTHER B2 hypothesis, bounded kappa — r-2 §4 :349-353);
  (ii) the resolvent is the S4 object as recorded: "On the opposite-phase
       sector the segment starts at 1 + A(0) = 1 - 2CPC ... an
       unrestricted sup is +infinity as written" (E1 S4 :720-727); the
       named hypothesis H-R "May NEVER default to 1 or to any other
       value (F'-3)" (E1 :725-727). CERT §2.4 :304-306 identifies the
       frame's R_n with exactly this recorded blow-up shape.
FRAME-N3 (DERIVED — the r-2 input does NOT tame R_n): kappa_n ->
  +infinity is CONSISTENT with ||R_n||_op -> infinity at ANY speed:
  s(1-s) = 1/4 - (s - 1/2)^2 is MAXIMAL at s = 1/2 (CAS D2), so
  eigenvalues approaching 1/2 — the ones that blow up R_n — are the most
  efficient carriers of the kappa mass r-2 certifies divergent. The
  check's n-1 (:310-317) seals the same shape from the other side: "a
  single s_i -> 1/2 drives det_n(0) -> 0 at bounded commutator mass."
FRAME VERDICT: the frame is EXACT and per-member conditional; its
  resolvent factor carries an of-record refusal-to-default (H-R shape)
  and no sealed control. Confronted first, as tasked: every route in §4
  that consumes ||R_n||_op must name it as missing (MO-1).
```

---

## 3. SUB-TASK 2 — CONSTRUCTIBILITY: WHAT THE SEALED CONSTRUCTIONS FIX ABOUT Delta_n(a), WHAT IS FREE

### 3.1 Fixed exactly by the sealed stock (DERIVED, byte-cited)

```text
K-1 ANALYTICITY. Entries of V_{mu lambda, n}(a) are entire in (a_+, a_-)
    (time-ordered exponential, source entering LINEARLY in the generator,
    finite carrier); Delta_n(a) = C_n(V(a) - V(0))C_n is finite-rank
    analytic; det(1 + A_n(a)) entire on C^2 per fixed n. [ZF §4.1(b)
    :332-339, EXACT at fixed n.]
K-2 RANK. rank Delta_n(a) <= rank C_n <= dim H_(n,ell) = 4 n^3 (n^3
    Hermite triples tensor C^4, PA A1 :53-57). Trace class per member;
    ||Delta_n(a)||_1 <= 4 n^3 ||Delta_n(a)||_op exact per member (singular
    values: N-term sum <= N x max, CAS D4). [DERIVED.]
K-3 THE a-COUPLING IS A BOUNDED COEFFICIENT, OF RECORD. a multiplies J
    alone; J = -B_D tensor alpha_x with B_D = Q_n b_D Q_n; the profile is
    a-free (D6' sharp objects untouched). [52f2490b CHECK 1/CHECK 2
    :39-71, sealed; PA A2 :117-128.] And ||J_n(t)||_op <= ||b_D||_inf = 1
    with the sup ATTAINED at the diamond center: on the open diamond
    s = s_- s_+ <= t^2 (1-t)^2 <= 1/16 (drop |x|^2 >= 0; t(1-t) <= 1/4
    exactly), so b_D = e^{16 - 1/s} <= e^0 = 1 = b_D(1/2, 0). [DERIVED
    exactly, CAS D6; b_D bytes at PA :99-113.]
K-4 SEALED n-FREE POLYDISC BOUND ON THE V FACTOR. sup_n sup_polydisc
    ||V_n(a)|| <= exp((|Im a_-| + |Im a_+|) C_J), n APPEARING NOWHERE in
    the constant; returns exactly 1 on the real slice; adjoint-
    continuation convention closed (both conventions obey the same
    bound). [52f2490b LINK 2 :83-98, flag V_factor_uniform_bound = true
    :189 — SEALED.]
K-5 NEW, DERIVED HERE — n-FREE, POLYDISC-UNIFORM OPERATOR-NORM BOUND ON
    THE DIFFERENCE. By variation of constants on the PA generator
    h_lambda(t; a) = h_lambda(t; 0) + a J_n(t) (PA A2 :124-128; A3
    :181-182), with u^0 the a = 0 propagator (UNITARY: Hermitian
    generator) and u^a the polydisc member:
      u_lambda(a; 1, 0) - u_lambda(0; 1, 0)
        = -i a int_0^1 u_lambda(0; 1, s) J_n(s) u_lambda(a; s, 0) ds
    (the operator identity behind CAS D5's exact scalar instance; a
    enters ONLY through aJ, K-3). Norms: ||u_lambda(0; 1, s)|| = 1;
    ||u_lambda(a; s, 0)|| <= e^{|Im a| C_b} with C_b := int_0^1
    ||J_n(t)|| dt <= 1 (K-3) — the same logarithmic-norm mechanism LINK 2
    seals (a self-adjoint generator part makes the flow oscillate, not
    grow). Hence, on the closed pair polydisc max(|a_+|, |a_-|) <= eps_*:
      ||u_lambda(a_+) - u_lambda(0)||_op <= eps_* C_b e^{eps_* C_b}
                                         <= eps_* e^{eps_*}   (CAS D7),
    and by the two-factor splitting V(a) - V(0) =
    u_mu(a_-)^dag [u_lambda(a_+) - u_lambda(0)]
    + [u_mu(a_-) - u_mu(0)]^dag u_lambda(0):
      ||V_n(a) - V_n(0)||_op <= eps_* e^{eps_*} (1 + e^{eps_*}) =: c(eps_*)
    UNIFORMLY in n, lambda, mu, both frozen ell, and a on the closed
    polydisc (CAS D7 assembly; the adjoint-continued bra branch obeys the
    same bound, |a_-bar| = |a_-|, of record K-4). With ||C_n|| <= 1 both
    schemes (52f2490b LINK 1 :78-82):
      ||Delta_n(a)||_op <= c(eps_*),  n-free, polydisc-uniform. [DERIVED;
    eps_* SYMBOLIC throughout — no value frozen.]
```

### 3.2 What the stock leaves FREE (named exactly)

```text
F-1 NO n-uniform HS/trace-norm bound: REFUTED of record — sup_n
    ||Delta_n(a)||_2 = +infinity per pair (52f2490b §0 :17-26 via strong
    convergence + ||X||_2 = infinity + weak LSC; consumed at ZF §4.1(c)
    :340-346's display). A fortiori no n-uniform trace-norm bound
    (||.||_1 >= ||.||_2, CAS D3).
F-2 NO trace-norm (or HS) RATE below rank x op: the R-L2b sharpened
    target — coincidence-vanishing exponent p of the difference kernel —
    is OPEN of record ("p unknown", "alpha not derived", G-11 §4
    :110-137; E1 S2 :696-700 "THE EXPONENT alpha IS NOT ASSERTED").
    NOTE OF RECORD (check n-3 :324-329): ZF o-1's phrase "scales with
    the carrier volume" is a PARAPHRASE, not a certified rate display —
    the refutation's own chain is lower-semicontinuity-based and
    therefore RATE-FREE. Consumed here at that grade: divergence yes,
    rate no.
F-3 NO closed-form spectrum {s_i} (r-2 CONSTRUCTIBILITY, G-3), no
    1/2-avoidance or approach law (§2.3), no kappa_n rate (r-2's step L
    is lower semicontinuity — divergence without speed, BY CONSTRUCTION
    of the method).
```

---

## 4. SUB-TASK 3 — THE ESTIMATE, AS FAR AS THE STOCK REACHES

### 4.1 The reduction of record, and its one-way-ness (DERIVED)

r-2's sealed chain (X-1, G-3 :371-379): |det_n(0)|^2 <= exp(-2 kappa_n),
hence EXACTLY -log|det_n(0)| >= kappa_n (CAS D8; the tasked form
kappa_n/2 is the same chain weakened, also displayed). Therefore

```text
  ||R_n Delta_n(a)||_1 = o(kappa_n) uniformly  ==>  the r-3 target
  ||R_n Delta_n(a)||_1 = o(-log|det_n(0)|) uniformly.       [SUFFICIENT]
```

SUFFICIENT-ONLY, not equivalent: no sealed display bounds -log|det_n(0)|
ABOVE by any function of kappa_n, and none can — the check's n-1 shape,
made exact (CAS D9): a single eigenvalue s = (1 - delta)/2 contributes
-log delta -> +infinity to -log|det_n(0)| while its kappa mass
2s(1-s) = (1 - delta^2)/2 <= 1/2 stays bounded. The o(kappa_n) route is
the consumable one; its failure would NOT refute the target. [DERIVED.]

### 4.2 Route 1 — rank x operator-norm budget: PROVABLY CANNOT CLOSE (DERIVED)

```text
  ||R_n Delta_n(a)||_1 <= ||R_n||_op ||Delta_n(a)||_1
                       <= ||R_n||_op · 4 n^3 · c(eps_*)      [§3.1 K-2/K-5]
```

Against the denominator: the ONLY sealed lower control is kappa_n ->
+infinity WITH NO RATE (F-3), and kappa_n carries the EXACT a priori
ceiling kappa_n = 2 sum_i s_i(1 - s_i) <= 2 · 4n^3 · (1/4) = 2 n^3
(CAS D4). The budget ratio is therefore

```text
  (||R_n||_op · 4 n^3 · c(eps_*)) / (2 n^3) = 2 ||R_n||_op c(eps_*),
```

n-FREE (CAS D10): the carrier power CANCELS EXACTLY. Even granted MO-1
(||R_n||_op uniformly bounded) the budget yields a BOUNDED ratio, never
o(1) — and kappa_n may sit anywhere below its ceiling. CONSEQUENCE
(derived, structural): NO product-of-norms discharge of r-3 can succeed
without a certified SUB-VOLUME trace-norm rate for Delta_n(a) (MO-3) —
r-3 INHERITS THE OPEN R-L2b SHARPENED TARGET on this route. Route 1
FAILS-AT the same-power ceiling; displayed, closed. [DERIVED.]

### 4.3 Route 2 — HS route: STRICTLY WORSE (DERIVED)

||R_n Delta||_1 <= sqrt(4n^3) ||R_n Delta||_2 <= sqrt(4n^3) ||R_n||_op
||Delta_n(a)||_2 consumes ||Delta_n(a)||_2, which is n-UNBOUNDED of
record (F-1), times a half-power of the rank: dominated by Route 1 in
every factor. Closed. [DERIVED.]

### 4.4 Route 3 — sealed uniformity already certified: SWEPT, NONE REACHES TRACE GRADE

The tasked sweep was run over both corpus roots (recursive, minus the
fenced name classes), keyed on: joint rate / R_n Delta_n; o(-log / o(kappa;
kappa_n rates, resolvent bounds, 1/2-avoidance; Delta_n; trace-norm and
carrier-volume rate content. Findings, exhaustive at this sweep:

```text
(s-1) The only o(-log carriers are the r-3-DEFINING artifacts themselves
      (clause, candidate, CERT, CHECK, r-2) — no supplier.
(s-2) The only sealed polydisc-uniform bound is LINK 2's V-factor
      OPERATOR-norm bound (K-4) — operator grade; compression to trace
      grade reintroduces the rank 4n^3 (Route 1).
(s-3) H-R is undischarged EVERYWHERE it appears (E1 :720-727 and its
      lineage); no artifact bounds ||R_n||_op or min_i |1 - 2 s_i|.
(s-4) No kappa_n rate exists anywhere (r-2 is the only kappa_n
      determination; its method is rate-free).
(s-5) The remaining grep hits are DIFFERENT OBJECTS: the AXN/S2 files'
      resolvent is the lattice free-Hamiltonian resolvent (its own
      display ||(h_a - z)^{-1}|| <= 1/|Im z|); TASK5's "Delta_n" is a
      cellular Hodge Laplacian; SUMMED_S2 cites the same 52f2490b
      refutation; the 2026-07-24 continuum-scaling review is the
      strong-resolvent limit of h_a — none carries V(a)/Delta_n/R_n
      trace-norm or polydisc-rate content for THIS frame.
(s-6) No product-level cancellation identity for R_n Delta_n(a) exists
      in the corpus (no display couples the near-kernel of 1 + A_n(0)
      to the range or kernel structure of Delta_n(a)).
```

Each sentence claims only this displayed sweep. Route 3: EMPTY. [DERIVED
at sweep grade.]

### 4.5 The obstruction made exact: the numerator DIVERGES (DERIVED — P-5)

Exactly, in the baseline eigenbasis on ran C_n: Delta_n(a) =
(1 + A_n(0)) · R_n Delta_n(a) (row scaling, CAS D3), and with FRAME-N1
(||1 + A_n(0)||_op <= 1):

```text
  ||R_n Delta_n(a)||_1 >= ||R_n Delta_n(a)||_2 >= ||Delta_n(a)||_2
```

(trace >= HS and the row-scaling inequality, CAS D3). Of record (F-1),
per pair, sup_n ||Delta_n(a)||_2 = +infinity at the refutation's own
locus on the polydisc (52f2490b §0: Delta_n(a) -> X strongly, ||X||_2 =
+infinity by C1's degree -3 kernel, weak lower semicontinuity — the same
LSC mechanism r-2 used for kappa_n, here running AGAINST the numerator).
CONSEQUENCES: (i) no bounded-numerator shortcut to the o(.) exists — the
target is a genuine race of two certified divergences; (ii) the uniform
(sup over the polydisc) numerator is a fortiori n-unbounded; (iii) at
a = 0 by contrast Delta_n(0) = C_n(V(0) - V(0))C_n = 0 EXACTLY — the
numerator vanishes identically at the baseline point (P-4), so the entire
content of r-3 lives at a != 0, where the divergence race is live.
[DERIVED.]

### 4.6 Where the race stands (the exact state of the question)

```text
  NUMERATOR:    >= ||Delta_n(a)||_2 -> infinity of record; <= 4n^3 c(eps_*)
                derived. NO RATE sealed in between (F-2).
  DENOMINATOR:  -log|det_n(0)| >= kappa_n -> infinity of record; kappa_n
                <= 2n^3 exact; -log|det_n(0)| itself admits NO sealed
                upper bound at all (D9). NO RATE sealed (F-3).
  THE o(.) IS UNDECIDED IN BOTH DIRECTIONS: a discharge needs
  numerator-upper-rate / denominator-lower-rate -> 0; a refutation needs
  numerator-lower-rate >= const x denominator-UPPER-rate at some polydisc
  point — and the denominator has no sealed upper rate (n-1's shape kills
  kappa_n as an upper proxy). Neither package exists (§4.4).
```

---

## 5. SUB-TASK 4 — THE VERDICT

```text
VERDICT: NOT-DERIVABLE-TODAY.

DERIVED PARTIALS (each at its own displayed quantifier):
 P-1 the frame at bytes, division-free, per-member conditional;
     ||1 + A_n(0)||_op <= 1 exact; ||R_n||_op = 1/min|1 - 2 s_i|
     uncontrolled of record (H-R/S4 shape; never defaults, F'-3).
 P-2 ||Delta_n(a)||_op <= c(eps_*) = eps_* e^{eps_*}(1 + e^{eps_*}),
     n-free, polydisc-uniform, derived (Duhamel; a multiplies J alone;
     ||J|| <= ||b_D||_inf = 1 exact); ||Delta_n(a)||_1 <= 4n^3 c(eps_*)
     per member.
 P-3 o(kappa_n) => o(-log|det_n(0)|) via -log|det_n(0)| >= kappa_n
     (sufficient-only; non-reversibility witnessed exactly).
 P-4 at a = 0 the numerator is exactly 0: r-3 is entirely an a != 0
     statement.
 P-5 (negative) the numerator diverges along the family of record
     (||R_n Delta_n(a)||_1 >= ||Delta_n(a)||_2, sup_n = +infinity per
     pair), and the rank x op budget provably cannot close (same-power
     ceiling, ratio n-free) — any product-of-norms discharge REQUIRES a
     sub-volume trace-norm rate: r-3 inherits the open R-L2b sharpened
     target on that route.

MISSING OBJECTS — what each would unblock:
 MO-1 an n-uniform (or rate-quantified) bound on ||R_n||_op — equivalently
      a quantified 1/2-approach/avoidance law for {s_i} — the compressed
      opposite-sector H-R shape. Unblocks the resolvent factor of every
      product route. (Uniform avoidance ALONE, with kappa_n -> infinity,
      is consistent and consumable; it is only TOGETHER WITH bounded
      kappa_n that F-a would fire — r-2 refutes bounded kappa_n, so MO-1
      cannot trigger N.5 on any artifact consistent with r-2.)
 MO-2 a certified LOWER rate for kappa_n (or directly for
      -log|det_n(0)|): r-2's lower-semicontinuity method is rate-free BY
      CONSTRUCTION; a rate needs new spectral input (e.g. a certified
      commutator-mass growth law for the Hermite family). Unblocks the
      denominator side of any route.
 MO-3 a certified n-uniform trace-norm RATE for Delta_n(a) strictly below
      the carrier volume (the uniform CONSTANT is refuted of record;
      only a rate remains possible). This is the R-L2b sharpened-target
      shape (coincidence-vanishing exponent p of the difference kernel,
      OPEN of record). Unblocks Route 1 together with MO-1 + MO-2.
 MO-4 (alternative to MO-1+MO-3) a product-level cancellation identity
      controlling ||R_n Delta_n(a)||_1 directly — none exists in the
      corpus (sweep §4.4 s-6). With MO-2 it would close the target alone.

NOT (DERIVED): the uniform o(.) is not established.
NOT (FAILS-AT) as a whole: no step of the TARGET provably fails — what
     provably fails is the rank x op BUDGET ROUTE (§4.2), displayed.
NOT (REFUTES-VANISHING)/F-d: nothing here exhibits failure of the
     full-family vanishing at any polydisc point — that would need a
     lower bound on |det(1 + A_n(a*))| along the family, i.e. exactly
     the uniform control that is missing. The F-d hazard is NOT
     exhibited; N.5 does not fire; reported plainly per the tasking.
CONSUMPTION BOUNDARY: R-L4b remains NOT discharged (its N.3 discharge
     condition = the sealed-and-checked B1 input PLUS this r-3 input;
     the r-3 slot stays open). Nothing fires, no flag flips, no witness
     retires; all three R-L4 witnesses STAND; the registrar consumes.
```

---

## 6. SUB-TASK 5 — CONSISTENCY WITH THE SEALED DICHOTOMY AND r-2's CHAIN (EXACT, NEVER NUMERIC)

```text
Y-1 FRAME vs CANDIDATE C3: §2.1's division-free identity is byte-content
    identical to e1da7446 :486-503 (CAS D1 re-run PASS; same sweep, same
    conclusion). No divergence.
Y-2 THE DENOMINATOR CHAIN: -log|det_n(0)| >= kappa_n re-derived from
    r-2's X-1 display |det_n(0)|^2 <= exp(-2 kappa_n) EXACTLY (CAS D8);
    the tasked kappa_n/2 form is implied (kappa_n >= kappa_n/2, exact).
    With r-2's kappa_n -> +infinity: -log|det_n(0)| -> +infinity, i.e.
    det_n(0) -> 0 — CONSISTENT with (B1) exactly; no numeric touch.
Y-3 P-5 vs (B1): numerator divergence and denominator divergence are
    jointly consistent; NOTHING here constrains their ratio — exactly the
    verdict's content. No sealed display is contradicted.
Y-4 FRAME-N1/N3 vs the dichotomy displays: (1-2s)^2 <= 1 on [0,1] and
    s(1-s) maximal at 1/2 (CAS D2) are the same per-factor facts as CERT
    §2.3(c)/§5 and the check's n-1 third-region shape — consistent, and
    they REPRODUCE n-1's exhibit exactly (CAS D9).
Y-5 K-5 vs LINK 2: on the real slice my Duhamel bound gives
    ||u(a) - u(0)|| <= eps_* C_b (the e-factor is 1 when Im a = 0), hence
    ||V(a) - V(0)|| <= 2 eps_* there — consistent with LINK 2's bound
    returning EXACTLY 1 for ||V|| on the real slice (difference of two
    norm-<= 1 operators <= 2). Off the real slice both carry the same
    log-norm mechanism. No conflict, and K-5 is the DIFFERENCE-level
    statement LINK 2 does not itself display.
Y-6 THE STRICKEN DISPLAY (E1 :773-778): consumed nowhere above. The only
    continuum input used (||X||_2 = infinity) enters via 52f2490b's own
    sealed chain about the REGULARIZED family's numerator, not via any
    valuation of D. No value of D, kappa, delta, M, or any rate constant
    appears anywhere in this artifact.
```

---

## 7. THE CAS BATTERY (VERBATIM) AND ITS OUTPUT (VERBATIM)

sympy 1.14.0, fresh venv `r3venv` under the session scratchpad; nothing
written to the workspace but this artifact and its seal. Tooling
disclosure, on the record: ONE pre-final harness-form correction — sympy
returns the D5 scalar integral as a Piecewise over aJ != 0 / aJ = 0 and
the check was made branch-aware (both branches verified exactly; the
identity is unconditional) — no mathematical claim changed. The final
battery then ran ONCE: 10/10 PASS.

```python
# R3-BUILD CAS battery -- EXACT SYMBOLIC ONLY (sympy 1.14.0, fresh venv r3venv
# under the session scratchpad). Every constant symbolic or an exact rational.
# Nothing numeric evaluated. All checks are exact-identity consistency checks
# of steps whose operator-theoretic content is derived in the artifact text.
import sympy as sp
from sympy import Rational as R

ok = lambda name, cond: print(f"{name}: {'PASS' if cond else 'FAIL'}", flush=True)

# ===== D1 -- the factorization frame, division-free (re-derivation of the
# candidate's CAS C3; 3x3 fully symbolic) =====
A0 = sp.Matrix(3, 3, lambda a, b: sp.Symbol(f'a0_{a}{b}'))
AA = sp.Matrix(3, 3, lambda a, b: sp.Symbol(f'aa_{a}{b}'))
X3 = sp.Matrix(3, 3, lambda a, b: sp.Symbol(f'x_{a}{b}'))
Y3 = sp.Matrix(3, 3, lambda a, b: sp.Symbol(f'y_{a}{b}'))
I3 = sp.eye(3)
D0 = (I3 + A0).det()
lhsM = sp.expand((I3 + A0)*(D0*I3 + (I3 + A0).adjugate()*(AA - A0)))
rhsM = sp.expand(D0*(I3 + AA))
ok("D1 frame division-free: (1+A0)(D0 I + adj(1+A0)(A - A0)) = D0 (1+A) EXACT;"
   " det(XY) = det X det Y EXACT -- jointly: where det(1+A0) != 0,"
   " det(1+A) = det(1+A0) det(1 + (1+A0)^{-1}(A - A0))",
   sp.expand(lhsM - rhsM) == sp.zeros(3, 3)
   and sp.expand((X3*Y3).det() - X3.det()*Y3.det()) == 0)

# ===== D2 -- baseline spectral facts on ran C_n =====
s = sp.Symbol('s', real=True)
sol_le1 = sp.solve_univariate_inequality((1 - 2*s)**2 - 1 <= 0, s,
                                         relational=False)
ok("D2 (1-2s)^2 <= 1 EXACTLY on s in [0,1] (solution set of the inequality"
   " IS [0,1]); s(1-s) = 1/4 - (s-1/2)^2 (per-factor kappa ceiling 1/4,"
   " maximum AT s = 1/2: near-1/2 eigenvalues MAXIMIZE kappa mass)",
   sol_le1 == sp.Interval(0, 1)
   and sp.expand(s*(1 - s) - (R(1, 4) - (s - R(1, 2))**2)) == 0)

# ===== D3 -- the numerator lower-bound ground: row-scaling + trace>=HS =====
s1, s2, s3 = sp.symbols('s_1 s_2 s_3', real=True)
Dg = sp.diag(1 - 2*s1, 1 - 2*s2, 1 - 2*s3)          # 1 + A_n(0) on ran C_n
Rg = sp.diag(1/(1 - 2*s1), 1/(1 - 2*s2), 1/(1 - 2*s3))
Dl = sp.Matrix(3, 3, lambda a, b: sp.Symbol(f'd_{a}{b}', real=True))
prod_back = sp.simplify(Dg*(Rg*Dl) - Dl)
RD = Rg*Dl
fro_delta = sp.expand(sum(Dl[i, j]**2 for i in range(3) for j in range(3)))
fro_scaled = sp.expand(sum(((1 - 2*[s1, s2, s3][i])**2 *
                            sp.together(RD[i, j])**2).expand()
                           for i in range(3) for j in range(3)))
sg1, sg2, sg3 = sp.symbols('sigma_1 sigma_2 sigma_3', nonnegative=True)
ok("D3 Delta = (1+A_n(0)) (R_n Delta) EXACT (row scaling; eigenbasis of the"
   " baseline); ||Delta||_F^2 = sum_i (1-2s_i)^2 ||row_i(R Delta)||^2 term"
   " by term, so with D2 ||Delta||_2 <= ||R_n Delta||_2; and trace >= HS:"
   " (sum sigma)^2 - sum sigma^2 = 2 sum_{i<j} sigma_i sigma_j >= 0",
   prod_back == sp.zeros(3, 3)
   and sp.simplify(fro_delta - fro_scaled) == 0
   and sp.expand((sg1 + sg2 + sg3)**2 - (sg1**2 + sg2**2 + sg3**2)
                 - 2*(sg1*sg2 + sg1*sg3 + sg2*sg3)) == 0)

# ===== D4 -- the rank/ceiling budget bookkeeping =====
n = sp.Symbol('n', positive=True)
N = 4*n**3                    # dim H_(n,ell) = n^3 Hermite triples x C^4 (PA A1)
mx = sp.Symbol('sigma_max', nonnegative=True)
ok("D4 trace-norm budget sum_{i<=3} sigma_i <= 3 sigma_max (3 sigma_max - sum"
   " = sum(sigma_max - sigma_i), each term >= 0 by definition of max); kappa"
   " ceiling: kappa_n = 2 sum s_i(1-s_i) <= 2 N (1/4) = N/2 = 2n^3 with"
   " N = 4n^3 EXACT",
   sp.expand(3*mx - (sg1 + sg2 + sg3)
             - ((mx - sg1) + (mx - sg2) + (mx - sg3))) == 0
   and sp.simplify(2*N*R(1, 4) - N/2) == 0
   and sp.simplify(N/2 - 2*n**3) == 0)

# ===== D5 -- Duhamel/variation-of-constants, exact scalar identity =====
# sympy returns the difference as a Piecewise over the branches aJ != 0 and
# aJ = 0; the identity must hold EXACTLY on BOTH branches (harness-form
# handling only; the identity itself is unconditional).
H, J, aa, ss = sp.symbols('H J a s')
lhs5 = sp.exp(-sp.I*(H + aa*J)) - sp.exp(-sp.I*H)
rhs5 = -sp.I*aa*J*sp.integrate(sp.exp(-sp.I*H*(1 - ss))
                               * sp.exp(-sp.I*(H + aa*J)*ss), (ss, 0, 1))
diff5 = sp.simplify(lhs5 - rhs5)
branch_vals = ([sp.simplify(e) for (e, c) in diff5.args]
               if isinstance(diff5, sp.Piecewise) else [diff5])
generic_zero = branch_vals[0] == 0
degenerate_zero = all(sp.simplify(v.subs(aa, 0)) == 0 for v in branch_vals[1:])
ok("D5 Duhamel shape, scalar identity-grade: e^{-i(H+aJ)} - e^{-iH} ="
   " -i a J int_0^1 e^{-iH(1-s)} e^{-i(H+aJ)s} ds EXACT on BOTH integration"
   " branches (generic aJ != 0 reduces to 0; the aJ = 0 branch expression"
   " vanishes at a = 0) -- the operator variation-of-constants derived in"
   " the text; a enters ONLY through aJ",
   generic_zero and degenerate_zero)

# ===== D6 -- the connection profile is bounded by 1 (PA A2 bytes) =====
t, x2 = sp.symbols('t x2', real=True)   # x2 = |x|^2 >= 0
sm = t**2 - x2
sm2 = (1 - t)**2 - x2
u = sp.Symbol('u', positive=True)       # u = s(t,x) in (0, 1/16]
ok("D6 b_D <= 1 = b_D(1/2,0): s_- <= t^2 and s_+ <= (1-t)^2 (drop x2 >= 0);"
   " t(1-t) <= 1/4 (1/4 - t(1-t) = (t-1/2)^2); hence s = s_- s_+ <="
   " t^2(1-t)^2 <= 1/16, so 16 - 1/s <= 0 on 0 < s <= 1/16 and"
   " b_D = e^{16 - 1/s} <= 1; b_D(1/2,0) = e^{16 - 16} = 1 EXACT",
   sp.expand(t**2 - sm - x2) == 0 and sp.expand((1 - t)**2 - sm2 - x2) == 0
   and sp.expand(R(1, 4) - t*(1 - t) - (t - R(1, 2))**2) == 0
   and sp.solve_univariate_inequality(16 - 1/u <= 0, u, relational=False,
                                      domain=sp.Interval.open(0, R(1, 16))
                                      ) == sp.Interval.open(0, R(1, 16))
   and sp.simplify(16 - 1/((R(1,4) - 0)*(R(1,4) - 0))) == 0)

# ===== D7 -- the polydisc difference-bound assembly (all symbolic) =====
eps = sp.Symbol('epsilon', positive=True)
Cb = sp.Symbol('C_b', positive=True)    # C_b <= 1: L1-in-time profile norm
ok("D7 monotone assembly: e^{eps C_b} <= e^{eps} for C_b <= 1 (exp increasing:"
   " eps - eps C_b = eps(1 - C_b) >= 0); two-factor split e^{eps}(eps e^{eps})"
   " + (eps e^{eps}) 1 = eps e^{eps}(1 + e^{eps}) =: c(eps) EXACT",
   sp.expand(eps - eps*Cb - eps*(1 - Cb)) == 0
   and sp.simplify(sp.exp(eps)*(eps*sp.exp(eps)) + eps*sp.exp(eps)
                   - eps*sp.exp(eps)*(1 + sp.exp(eps))) == 0)

# ===== D8 -- the denominator chain re-pin (r-2 X-1 consumed exactly) =====
kap, dmod = sp.symbols('kappa d', positive=True)
ok("D8 from |det_n(0)|^2 <= e^{-2 kappa_n}: -log|det_n(0)| >= kappa_n"
   " (log e^{-kappa} = -kappa exact; d^2 <= e^{-2k} => d <= e^{-k} for"
   " positive quantities) and kappa_n >= kappa_n/2 (the tasked weaker form)",
   sp.simplify(sp.log(sp.exp(-kap)) + kap) == 0
   and sp.simplify(sp.sqrt(sp.exp(-2*kap)) - sp.exp(-kap)) == 0
   and sp.simplify(kap - kap/2 - kap/2) == 0)

# ===== D9 -- the one-way witness (no reverse bound of -log|det| by kappa) ===
dl = sp.Symbol('delta', positive=True)
s_w = (1 - dl)/2
ok("D9 witness shape (the check's n-1, made exact): s = (1-delta)/2 gives"
   " 1 - 2s = delta with -log delta -> +infinity as delta -> 0+, while the"
   " kappa mass 2s(1-s) = (1 - delta^2)/2 <= 1/2 stays bounded: -log|det|"
   " admits NO upper bound by kappa; o(kappa_n) is SUFFICIENT-ONLY",
   sp.simplify(1 - 2*s_w - dl) == 0
   and sp.limit(-sp.log(dl), dl, 0, '+') == sp.oo
   and sp.simplify(2*s_w*(1 - s_w) - (1 - dl**2)/2) == 0
   and sp.simplify(R(1, 2) - (1 - dl**2)/2 - dl**2/2) == 0)

# ===== D10 -- the budget route can NEVER produce o(.): the ratio is n-free ==
c_sym, rho = sp.symbols('c rho', positive=True)   # c = c(eps); rho = ||R_n||
ratio = (rho*N*c_sym)/(N/2)
ok("D10 budget ratio (||R_n|| N c(eps)) / (N/2) = 2 rho c(eps) -- the carrier"
   " power CANCELS EXACTLY: rank x op-norm numerator budget against the"
   " kappa ceiling is n-FREE and never o(1); any product-of-norms discharge"
   " REQUIRES a sub-volume trace-norm rate (the missing MO-3)",
   sp.simplify(ratio - 2*rho*c_sym) == 0 and sp.simplify(ratio).has(n) is False)

print("R3-BATTERY-DONE")
```

Output, verbatim (10/10 PASS):

```text
D1 frame division-free: (1+A0)(D0 I + adj(1+A0)(A - A0)) = D0 (1+A) EXACT; det(XY) = det X det Y EXACT -- jointly: where det(1+A0) != 0, det(1+A) = det(1+A0) det(1 + (1+A0)^{-1}(A - A0)): PASS
D2 (1-2s)^2 <= 1 EXACTLY on s in [0,1] (solution set of the inequality IS [0,1]); s(1-s) = 1/4 - (s-1/2)^2 (per-factor kappa ceiling 1/4, maximum AT s = 1/2: near-1/2 eigenvalues MAXIMIZE kappa mass): PASS
D3 Delta = (1+A_n(0)) (R_n Delta) EXACT (row scaling; eigenbasis of the baseline); ||Delta||_F^2 = sum_i (1-2s_i)^2 ||row_i(R Delta)||^2 term by term, so with D2 ||Delta||_2 <= ||R_n Delta||_2; and trace >= HS: (sum sigma)^2 - sum sigma^2 = 2 sum_{i<j} sigma_i sigma_j >= 0: PASS
D4 trace-norm budget sum_{i<=3} sigma_i <= 3 sigma_max (3 sigma_max - sum = sum(sigma_max - sigma_i), each term >= 0 by definition of max); kappa ceiling: kappa_n = 2 sum s_i(1-s_i) <= 2 N (1/4) = N/2 = 2n^3 with N = 4n^3 EXACT: PASS
D5 Duhamel shape, scalar identity-grade: e^{-i(H+aJ)} - e^{-iH} = -i a J int_0^1 e^{-iH(1-s)} e^{-i(H+aJ)s} ds EXACT on BOTH integration branches (generic aJ != 0 reduces to 0; the aJ = 0 branch expression vanishes at a = 0) -- the operator variation-of-constants derived in the text; a enters ONLY through aJ: PASS
D6 b_D <= 1 = b_D(1/2,0): s_- <= t^2 and s_+ <= (1-t)^2 (drop x2 >= 0); t(1-t) <= 1/4 (1/4 - t(1-t) = (t-1/2)^2); hence s = s_- s_+ <= t^2(1-t)^2 <= 1/16, so 16 - 1/s <= 0 on 0 < s <= 1/16 and b_D = e^{16 - 1/s} <= 1; b_D(1/2,0) = e^{16 - 16} = 1 EXACT: PASS
D7 monotone assembly: e^{eps C_b} <= e^{eps} for C_b <= 1 (exp increasing: eps - eps C_b = eps(1 - C_b) >= 0); two-factor split e^{eps}(eps e^{eps}) + (eps e^{eps}) 1 = eps e^{eps}(1 + e^{eps}) =: c(eps) EXACT: PASS
D8 from |det_n(0)|^2 <= e^{-2 kappa_n}: -log|det_n(0)| >= kappa_n (log e^{-kappa} = -kappa exact; d^2 <= e^{-2k} => d <= e^{-k} for positive quantities) and kappa_n >= kappa_n/2 (the tasked weaker form): PASS
D9 witness shape (the check's n-1, made exact): s = (1-delta)/2 gives 1 - 2s = delta with -log delta -> +infinity as delta -> 0+, while the kappa mass 2s(1-s) = (1 - delta^2)/2 <= 1/2 stays bounded: -log|det| admits NO upper bound by kappa; o(kappa_n) is SUFFICIENT-ONLY: PASS
D10 budget ratio (||R_n|| N c(eps)) / (N/2) = 2 rho c(eps) -- the carrier power CANCELS EXACTLY: rank x op-norm numerator budget against the kappa ceiling is n-FREE and never o(1); any product-of-norms discharge REQUIRES a sub-volume trace-norm rate (the missing MO-3): PASS
R3-BATTERY-DONE
```

---

## 8. CHOICE LEDGER (Actual-Surface Guard discipline; every unforced choice, classified)

```text
CH-a CHASING 52f2490b AND 685afac8 AT PATH: FORCED — both are pinned by
     the tasked stock's own digest tables (r-2 G-5/G-7; ZF §4.1(c); CERT)
     and the tasking mandates chasing citations by pinned digest; seals
     verified before reliance (§1 G-9/G-10).
CH-b THE REDUCTION TARGET o(kappa_n): FORCED as the consumable SUFFICIENT
     route (r-2's sealed chain is the only sealed lower control on the
     denominator); its one-way-ness is DISPLAYED (§4.1, CAS D9) and no
     conclusion consumes equivalence — the verdict's undecidedness is
     stated against the TARGET, not only against o(kappa_n).
CH-c THE PROFILE-NORM SYMBOL C_b: IMMATERIAL(derived) — C_b <= 1 exactly
     (CAS D6) and it is eliminated from the final display (CAS D7); it is
     an F'-5-admissible functional of ||b_D||; no number frozen.
CH-d ADJOINT-CONTINUATION CONVENTION ON THE BRA BRANCH: IMMATERIAL(of
     record) — closed at 52f2490b LINK 2 (:92-95): both conventions obey
     the same bound; K-5 uses only |a_-bar| = |a_-|.
CH-e THE POLYDISC LOCUS OF THE NUMERATOR DIVERGENCE: consumed at ZF
     §4.1(c)'s own display quantifier (per pair, sup over n, of record);
     IMMATERIAL(derived) for the verdict — NOT-DERIVABLE-TODAY stands on
     §4.2/§4.4 alone; P-5 only closes the bounded-numerator shortcut.
CH-f RANK BOUND rank C_n <= 4n^3: FORCED (PA A1 bytes: n^3 Hermite
     triples tensor C^4; a projection's rank cannot exceed its space).
CH-g INHERITED PREMISE (r-2 CH-A, the pure Hermite projection realization
     of {C_n}): PREMISE(named), inherited at the clause's own
     eigenvalue-product display (V-N3-protected); load-bearing here ONLY
     for the displays written in the s_i spectral frame (§2.2-2.3, D2-D4,
     D9); the verdict NOT-DERIVABLE-TODAY is IMMATERIAL(derived) to it —
     under the mixed scheme no additional rate object exists either (the
     sweep §4.4 is scheme-blind).
CH-h QUANTIFYING OVER FRAME-DEFINED MEMBERS ONLY (§2.2): FORCED — the
     frame of record is itself conditional ("where 1 + A_n(0) is
     invertible", CERT :294-295); no repair invented, none available.
MACHINERY/RELEVANCE (guard append honored): the machinery is classical
     operator theory (variation of constants, log-norm bounds, singular-
     value inequalities) applied to SEALED constructions with booked
     surface traces (G-5, G-8, G-9); SURFACE-DERIVED, not surface-native;
     no surface verdict is anchored beyond the named conditionals.
```

## 9. TOY_SEPARATION (self-assessment)

```text
CLAIMED CLEAN at the stated quantifiers. Every CAS instance is an
identity-grade exhibit of an all-matrix/all-scalar identity, displayed
with its universal quantifier in the check name (D1 all 3x3; D2/D6/D7/D8
all-parameter inequalities with exact solution sets; D3/D4 term-by-term
identities; D5 the unconditional scalar Duhamel identity on both
integration branches; D10 symbolic cancellation). The ONE witness-shaped
exhibit (D9) instantiates the CHECK's OWN sealed sentence (n-1 :310-317)
at a single eigenvalue and is quoted no wider than that sentence: it
refutes only the existence of a universal reverse bound. No model family
is used as a premise; no instance is promoted to a family claim; no
spectral datum of the actual family is valued. The RULING is the
checker's/audit's, not this artifact's.
```

---

## 10. FLAG BLOCK

```text
R3_JOINT_RATE = NOT-DERIVABLE-TODAY( the r-3 input
  ||R_n Delta_n(a)||_1 = o(-log|det_n(0)|) uniformly on the closed pair
  polydisc is UNDECIDED IN BOTH DIRECTIONS on the sealed stock: both
  sides certified divergent, NEITHER side carries a sealed rate.
  Numerator: >= ||Delta_n(a)||_2 with sup_n = +infinity per pair of
  record (52f2490b via the exact lower bound ||R_n Delta||_1 >=
  ||R_n Delta||_2 >= ||Delta||_2, ||1 + A_n(0)||_op <= 1, CAS D2/D3);
  <= 4n^3 c(eps_*) derived; no rate between. Denominator:
  -log|det_n(0)| >= kappa_n -> +infinity of record (r-2, audited); no
  rate (lower semicontinuity is rate-free by construction); no upper
  bound at all (check n-1 shape, CAS D9). The rank x op budget provably
  cannot close: numerator budget 4n^3 c(eps_*) vs kappa ceiling
  kappa_n <= 2n^3 — the carrier power cancels exactly, ratio n-free,
  never o(1) (CAS D4/D10). )
PARTIALS_DERIVED = FIVE( P-1 frame at bytes division-free, per-member
  conditional; ||1+A_n(0)||_op <= 1; ||R_n||_op = 1/min|1-2s_i|
  uncontrolled of record — the S4/H-R shape, never defaults (F'-3);
  kappa_n -> infinity consistent with ||R_n|| -> infinity at any speed
  (s(1-s) maximal at 1/2). P-2 NEW n-free polydisc-uniform op-norm bound
  ||Delta_n(a)||_op <= c(eps_*) = eps_* e^{eps_*}(1 + e^{eps_*}) derived
  by Duhamel from the PA generator (a multiplies J alone; ||J|| <=
  ||b_D||_inf = 1 exact, CAS D5/D6/D7); consistent with sealed LINK 2.
  P-3 o(kappa_n) => target via -log|det_n(0)| >= kappa_n (CAS D8),
  SUFFICIENT-ONLY (CAS D9). P-4 numerator EXACTLY 0 at a = 0: r-3 is
  entirely an a != 0 statement. P-5 the numerator diverges along the
  family — no bounded-numerator shortcut; any product-of-norms discharge
  REQUIRES a sub-volume trace-norm rate: r-3 inherits the OPEN R-L2b
  sharpened target (p unknown, alpha underived) on that route. )
MISSING_OBJECTS = FOUR-NAMED( MO-1 n-uniform/rate-quantified ||R_n||_op
  bound (quantified 1/2-approach law; cannot trigger N.5 consistently
  with r-2 since bounded kappa_n is refuted); MO-2 certified lower RATE
  for kappa_n or -log|det_n(0)| (needs new spectral input; r-2's method
  cannot give it); MO-3 certified sub-volume trace-norm RATE for
  Delta_n(a) (uniform constant REFUTED of record; only a rate remains;
  = the R-L2b sharpened-target shape); MO-4 alternative product-level
  cancellation identity for R_n Delta_n(a) (none in the corpus, sweep
  §4.4). MO-1+MO-2+MO-3 close Route 1; MO-2+MO-4 close directly. )
F_D_HAZARD = NOT-EXHIBITED( nothing here bounds det(1 + A_n(a*)) away
  from zero along the family at any polydisc point; a refutation of the
  full-family vanishing needs exactly the uniform control that is
  missing; N.5 does not fire; reported plainly. )
CONSUMPTION_BOUNDARY = NOTHING-FIRED( R-L4b NOT discharged (the r-3 slot
  of N.3's discharge condition stays open) and NOT refuted; no flag
  flipped, no witness retired, no gate moved; all three R-L4 witnesses
  STAND; the registrar consumes; whether to commission the missing
  objects is not a lane's call. )
CONSISTENCY = CHECKED-EXACT( Y-1 frame = candidate C3 (CAS D1 re-run);
  Y-2 the denominator chain re-derived from r-2 X-1 exactly (CAS D8),
  tasked kappa_n/2 form implied; Y-3 P-5 consistent with (B1) — nothing
  constrains the ratio; Y-4 per-factor facts match CERT §2.3(c) and
  check n-1 (CAS D2/D9); Y-5 K-5 consistent with LINK 2 on and off the
  real slice; Y-6 the stricken display consumed nowhere, no value of D
  or any constant inferred. )
SEALS_VERIFIED = 10/10-PLUS-ONE( 72d5343e clause; e1da7446 R1; 3b5e95b6
  r-2; a4cf394c r-2 audit; 46846730 E1; a903716c CERT; 26f9314b ZF;
  789338ad PA; 52f2490b per-pair refutation (chased, read in full);
  685afac8 CERT-CHK (chased, n-1..n-3); PLUS sweep-located d1807b96
  R-L2b sharpened target (status evidence only). EXPECTED-UNLOCATABLE
  register tokens noted, not chased. )
FORBIDDEN_IMPORTS = none( exact symbolic only; no floating-point
  numerics as ground; no measured constant; NO value frozen — no numeric
  kappa, M, delta, D, eps, or rate constant (eps_* and C_b symbols
  throughout; c(eps_*) a displayed symbolic expression, not a number);
  M(t)/1_{D_t} sharp; the stricken display consumed nowhere as ground;
  no register/road_/ledger/lens/plan/tracker/THE_HANDOFF file opened; no
  git action; no existing file edited; ONE file written plus its seal;
  commission-distinct path S9AD probed ABSENT before write. )
MACHINERY_INVOKED = yes(CAS) — sympy 1.14.0, fresh venv r3venv under the
  session scratchpad; final run ONCE, 10/10 PASS, script and output
  reproduced verbatim in §7; one pre-final harness-form correction
  (D5 Piecewise branch handling) disclosed, no mathematical claim
  changed.
alpha_computed = false ; proof_authorized = false ;
kappa_record_computed = false
ALL_RESULTS = CLAIMED until checked.
R3_JOINT_RATE_RESULT = SEALED.
```
