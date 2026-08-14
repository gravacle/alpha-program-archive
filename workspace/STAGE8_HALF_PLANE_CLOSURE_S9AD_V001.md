# STAGE 8 — THE HALF-PLANE LOCALIZATION AT A SUMMED-COMPATIBLE QUANTIFIER: CLOSURE ATTEMPTED FROM SEALED STOCK — S9AD V001

## BLIND BUILDER — CODENAME HPL-BUILD — [SEALED]

Date: 2026-08-14
Role: BLIND builder (HPL-BUILD), road item 4. Commission: CLOSE the
half-plane localization at a summed-compatible quantifier from sealed
stock, or refuse with exact blockers. The payoff is sealed and
conditional and is held to its own conditional and NO STRONGER: IF the
localization closes at a summed-compatible quantifier, R-L0 is not
needed for the n = 1 leg (E1 :884-885 verbatim shape). "Q-..." tokens
inside sealed artifacts are EXPECTED-UNLOCATABLE by design; noted, never
chased.

Gates: `alpha_computed = false` ; `proof_authorized = false` ;
`kappa_record_computed = false`. ALL_RESULTS = CLAIMED until checked.

Fences held: EXACT SYMBOLIC ONLY — one CAS battery (sympy 1.14.0, fresh
venv `hplvenv` under the session scratchpad), script and output verbatim
in §6, 11/11 PASS; no floats as ground; no measured constant; no value
frozen; every constant symbolic or an exact rational/surd. No file
matching register|road_|ledger|lens|plan|tracker|THE_HANDOFF opened
(orchestration-class files — CONTINUATION_STATE, relay_outbox — also
skipped by choice, §7 C-6). No git action; no existing file edited; not
registered, not committed, not pushed. ONE output + seal sidecar at the
commission-distinct path, probed ABSENT before write. Sweep-displayed
exhaustiveness only. No flag flipped; no witness retired (retirement is
the registrar's). Marks: DERIVED / CLAIMED / CONDITIONAL(premise named)
/ GROUNDED(record cited at grade) span by span.

---

## 0. VERDICT IN ONE LINE

**NOT-DERIVABLE-TODAY — the half-plane localization does NOT close at a
summed-compatible quantifier on the sealed stock; the refusal carries
four exact blockers (§4.2), each swept for genuineness, and the sealed
R-L0 consequence is NOT triggered (nothing here weakens or strengthens
the E1 :884-885 conditional). PARTIAL DELIVERED MEANWHILE, exact and
CAS-pinned, three pieces: (P-a) THE SLICE QUANTIFIER COLLAPSE — on the
real equal-source slice of the polydisc, riding the sealed s-3 identity
(798de0dd, audited end-to-end c944a901), the localization's five-pair,
free-angle quantifier collapses to ONE scalar condition: half-plane
separation of the five surviving rho's at (theta, delta) is EQUIVALENT
to Re rho_{+-,n}(a,a) >= delta — three pairs sit AT 1 exactly, the
conjugate pair forces the angle, theta collapses to 0 (HP3a-c, exact
both directions); (P-b) THE UNITARY-COMPRESSION DISC BOUND (new here,
nothing sealed states it): for every carrier n, every pair p, and every
REAL source pair, |det_{ran C}(C V_p C)| <= 1 EXACTLY — the sealed
block-triangular identity (E1 :655-659; HP4a) plus the defect identity
(CVC)(CVC)^+ + (CV(1-C))(CV(1-C))^+ = C V V^+ C (HP4b) plus
Cauchy-Binet positivity displayed as a sum of two squared moduli (HP4c/
HP4d), consuming unitarity of the sourced propagator at real sources
(PA :124-126, S2TOT X-3 grade) — an n-UNIFORM, carrier-blind bound on
BOTH the numerator and the a = 0 denominator of rho_{+-}; the entire
slice obstruction is thereby LOCALIZED to a single named object: an
n-uniform lower bound on the a = 0 cross-pair collapse determinant —
exactly GAP-C of the rate-gap linkage of record, the object r-2 shows
divergent-in-signal (kappa_n -> infinity, B1-DERIVED) and r-3 shows
rate-free on both sides (NOT-DERIVABLE-TODAY, the race), with the
two disc bounds alone putting NO bound on the ratio (HP6 witness);
(P-c) THE MARGIN DISPLAY — on the slice Z_hat_n(a,a) is REAL with
Z_hat = 0 iff Re rho_{+-} = -3 (HP5): the localization (Re >= delta >
0) sits THREE whole units of Re above what nonvanishing needs (Re >
-3), a second sufficiency-not-necessity one level up from the region
result of record — so even a proof that the localization is underivable
would not bar the R-L0b target. The connected-region
necessity+sufficiency of record (38aa39d1 s-2/CB7) cannot be consumed:
its unit-modulus hypothesis is uncertified for the rho values (only the
three diagonal-pair values are pinned to modulus 1, and only on the
slice), its location hypothesis IS the missing content (circular
consumption), and the general connected case is UNDECIDED of record.
No falsifier V-1..V-6 engages (§5 — in particular the slice reduction
is the RECORD's own summed identity plus a statement-level equivalence;
NO control runs summed -> per-pair); witnesses
SCAD_COLOR_SUM_REQUIRES_ABSOLUTE_X_BOUND and
SCAD_SUMMED_SEGMENT_REMAINDER_UNCERTIFIED STAND; gate-list membership
unchanged.**

---

## 1. SEALS VERIFIED AT PATH (shasum -a 256), BEFORE ANY RELIANCE

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`. Every
digest recomputed from bytes at path THIS session by FULL digest; each
compared against its `.seal.sha256` sidecar and, where tasked, against
the tasked prefixes. 21/21 MATCH; NONE UNVERIFIABLE. Tasked-prefix
resolution, on the record: 57edbb96/38aa39d1 = the localization-delivery
pair (the R3C build and its audit — the carriers of the region
criterion, the witnesses, and the connected-region sharpenings);
631356a3/1663c3a5 = the P1 dilation-closure pair; cbfbb74c = the
adoption ENTRY; e5b0879b/cbe6ff4f = the discharge pair; 46846730 = E1.

```text
57edbb96...  STAGE8_R3C_SUMMED_REMAINDER_ATTEMPT_V001.md   MATCH (R3C — §3 Task B: the four dead routes; §3.6 r-1..r-5 the region characterization; §3.7 verdict; RB batteries)
38aa39d1...  STAGE8_R3C_SUMMED_REMAINDER_AUDIT_V001.md     MATCH (R3C-AUDIT — CONFIRMED; s-1 min |Z_hat| = 1/4 attained; s-2/CB7 connected unit-modulus equivalence; CB3 integer norm-forms)
798de0dd...  STAGE8_SECOND_ORDER_TOTAL_CONTENT_V001.md     MATCH (S2TOT — s-3 the all-orders slice identity; X-3 unitarity; the BAR-honored note)
c944a901...  STAGE8_SECOND_ORDER_TOTAL_CONTENT_AUDIT_V001.md MATCH (S2TOT-AUDIT — CONFIRMED; AU22/AU23 end-to-end slice assembly; p-3 the definitional grade of rho_{+-})
46846730...  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md   MATCH (E1 — :652-666 block-triangular + Carleman; :679-689 S1/cell-sup deferral; :720-727 H-R no-default; :803-848 R.3; :851-894 R-L0/R-L0b + :884-885 the licensed conditional)
789338ad...  STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md MATCH (PA — :118-130 J = -B_D tensor alpha_x Hermitian; the real-source unitarity ground)
ce59b480...  STAGE8_SUMMED_S2_CANDIDATE_V001.md            MATCH (S2CAND — §4.1 S2'-O; §4.3 R.3'(a)-(d) + the (c) BAR; §5.3 V-1..V-6)
cbfbb74c...  STAGE8_SUMMED_S2_ENTRY_ADDENDUM_V001.md       MATCH (ENTRY — the adoption of record; witnesses LIVE)
e5b0879b...  STAGE8_S2_DISCHARGE_V001.md                   MATCH (DISCHARGE — alpha' = 1/4 all-pairs similarity-class estimate; §4.2 W-1/W-2/W-3; §5 the corrected half-plane condition)
cbe6ff4f...  STAGE8_S2_DISCHARGE_AUDIT_V001.md             MATCH (DISCHARGE-AUDIT — all five audits CONFIRMED)
52f2490b...  STAGE8_RL2B_UNIFORMITY_REFUTED_RESULT_V001.md MATCH (per-pair HS refutation of record; X_HS_norm_infinite = true)
26f9314b...  STAGE8_ZERO_FREE_DERIVATION_V001.md           MATCH (ZF — §4.1(b) entirety at fixed n; §4.1(c) no per-pair carrier limit; §4.3 o-1 n-dependent radius)
aed551e3...  STAGE8_ZERO_FREE_CHECK_V001.md                MATCH (ZF-CHK)
3b5e95b6...  STAGE8_R2_KAPPA_N_DETERMINATION_S9AD_V001.md  MATCH (r-2 — kappa_n -> infinity B1-DERIVED, full-family quantifier)
a4cf394c...  STAGE8_R2_KAPPA_N_DETERMINATION_S9AD_AUDIT_V001.md MATCH (r-2 audit)
bebc0f08...  STAGE8_R3_JOINT_RATE_S9AD_V001.md             MATCH (r-3 — NOT-DERIVABLE-TODAY; the race of two divergences, rate on neither side)
72c95d42...  STAGE8_R3_JOINT_RATE_S9AD_AUDIT_V001.md       MATCH (r-3 audit)
3de0502c...  STAGE8_RATE_GAP_LINKAGE_S9AD_V001.md          MATCH (LINK — GAP-C named: a certified lower rate for kappa_n or -log|det_n(0)|; B-C COUSINS, distinct)
176ee719...  STAGE8_RATE_GAP_LINKAGE_S9AD_AUDIT_V001.md    MATCH (LINK audit)
631356a3...  STAGE8_P1_DILATION_CLOSURE_V001.md            MATCH (P1 — the carrier index move (n, ell) -> (n, ell/L); P-1 dissolves into the ray-quantifier condition)
1663c3a5...  STAGE8_P1_DILATION_CLOSURE_AUDIT_V001.md      MATCH (P1-AUDIT — CONFIRMED-WITH-CORRECTIONS)
```

Sealed content read at path this session and consumed: R3C §3.1-§3.7
(the four routes; r-1..r-5; the FAILS-AT verdict; the licensed
conditional held NO STRONGER) and §2.1 (the object R_n and the c-weight
re-derivation RA1); R3C-AUDIT §3 (all four routes CONFIRMED; s-1;
s-2/CB7a-c with the general connected case declared UNDECIDED) and the
CB3 integer norm-form re-derivation; S2TOT §2.6 s-3 (the all-orders
slice identity verbatim: R_n(a,a) = (1/4)Re[rho_{+-} - 1 - tr
Delta_{+-}], Z_hat_n(a,a) = 3/4 + (1/4)Re rho_{+-,n}(a,a); "the BAR
honored" note) and §2.5 (the master form off-slice); S2TOT-AUDIT §0
(CONFIRMED; AU23 end-to-end; p-3: "UNCONDITIONAL" rides on the sealed
definitional grade of rho_{+-} — surviving-sector well-definedness, E1
:666, constitutive not a premise); E1 :652-666 (block-triangular
identity det(1 + C(V-1)) = det_{ran C}(C V C); the Carleman display
valid only on the surviving sector), :679-689 (S1 enclosure required;
"the sup over CELLS is deferred to R-L0"), :720-727 (S4/H-R: named
hypothesis, never defaults), :803-848 (R.3 chain), :851-894 (R-L0;
R-L0b; :884-885 "If R-L0b closes, R-L0 is not needed for the n = 1 leg
and that must be stated"); PA :118-130 (J = -B_D tensor alpha_x, the
Hermitian minimal-coupling form — the real-source unitarity ground);
S2CAND §4.1, §4.3(a)-(d) (R.3'-c verbatim: "certified AT THE
SUMMED-COMPATIBLE QUANTIFIER (n-uniformly)"; the (c) per-pair BAR),
§5.3 V-1..V-6 verbatim; ENTRY in full; DISCHARGE §4.2, §5; 52f2490b §0
+ §5; ZF §4.1(b)(c), §4.3; r-2 §0; r-3 §0; LINK §0; P1 §0.

---

## 2. THE STATE AT BYTES

### 2.1 The delivered localization stock, with every quantifier

```text
(st-1) REGION CRITERION (iff), exact, of record [R3C §3.6 r-1, audited]:
   for a region S and the derived weights c = (1/2, 1/8 x 4) [HP1
   re-derivation], "every configuration of the five surviving rho's in
   S has Z_hat != 0" IFF 0 not in Sigma_c(S) := (1/2)S + (1/8)S x 4.
   QUANTIFIER: worst case over INDEPENDENT assignment of five values.
(st-2) HALF-PLANE SEPARATION IS SUFFICIENT [DISCHARGE §5.2; R3C RB1]:
   Re(e^{i theta} rho_p) >= delta > 0 for all five p ==> |Z_hat| >=
   delta. NOT NECESSARY [R3C §3.6 r-3; audited by integer norm-forms,
   CB3]: S = cube roots of unity has 0 in conv(S) yet all 3^5 = 243
   assignments give Z_hat != 0 (the weight multiset {4,1,1,1,1}/8
   cannot 3-balance; 3 does not divide 8); auditor sharpening s-1:
   min |Z_hat| = 1/4 ATTAINED on that family.
(st-3) CONNECTED-REGION EQUIVALENCE [R3C-AUDIT s-2, CB7a-c]: for S
   contained in the UNIT CIRCLE, 0 in Sigma_c(S) iff S contains an
   antipodal pair; a CONNECTED unit-modulus S with 0 in conv(S) has
   angular extent >= pi and contains one; hence on connected
   unit-modulus regions the corrected condition (0 outside conv S) is
   NECESSARY AND SUFFICIENT, and every unit-modulus non-necessity
   witness is necessarily disconnected. QUANTIFIER: unit-modulus S
   only; the general connected (varying-modulus) case is UNDECIDED of
   record.
(st-4) THE FOUR DEAD ROUTES to the n-uniform separation [R3C §3.2-§3.5,
   all four CONFIRMED by the audit]: per-pair majorants
   carrier-divergent of record (52f2490b; ZF o-1; S1 uncertified);
   H-R-conditional closure fails by exact witness (rho_res identically
   1, segment t - log(1+t) unbounded — the segment is not a function
   of rho_res); no summed -> per-pair bridge sealed and a
   control-carrying one is the V-2 void shape; fixed-n localizations
   exist with n-DEPENDENT radius and no limit object to pass to.
(st-5) THE SLICE IDENTITY [S2TOT s-3, NEW TODAY relative to R3C;
   audited end-to-end AU23]: on the real equal-source slice a_+ = a_-
   = a (real), unitarity of the sourced propagator (PA :124-126) gives
   V_{mu mu}(a,a) = I exactly and V_{-+} = V_{+-}^dag, hence
   rho_{mu mu}(a,a) = 1 for the three branch-diagonal surviving pairs
   at every order and every carrier n, rho_{-+} = conj rho_{+-}, and
     Z_hat_n(a,a) = 3/4 + (1/4) Re rho_{+-,n}(a,a)   [HP2 arithmetic].
   Grade: exact identity at the sealed definitional grade of rho_{+-}
   (surviving-sector well-definedness, E1 :666; S2TOT-AUDIT p-3);
   the polydisc quantifier itself ranges over complex (a_+, a_-) and
   OFF the slice the master form is the statement.
```

### 2.2 What "summed-compatible" means against the adopted quantifier

The adopted clause of record (S2CAND §4.1 + §4.3, in force by ENTRY):
S2'/R-L2b^Sigma quantifies the summed OPERATOR-HS family — sup_n
||Delta^Sigma_n(a)||_2 <= |C|_4^{alpha'} G_hs^Sigma, alpha' a symbol,
delivered of record at alpha' = 1/4 (all-pairs instance, similarity
class, DISCHARGE, audited) — and R.3'-c demands the segment remainder
"certified AT THE SUMMED-COMPATIBLE QUANTIFIER (n-uniformly)" with the
per-pair route BARRED for that clause. Therefore, exactly:

```text
summed-compatible quantifier :=
  (q-i)  n-UNIFORM on the carrier axis (constants free of n, ell,
         truncation, cellulation data — E1's constant discipline);
  (q-ii) consuming NO per-pair HS majorant (the (c) BAR at bytes;
         and dead-of-record anyway, 52f2490b); and
  (q-iii) exhibiting NO summed -> per-pair CONTROL derivation
         (the V-2 void shape).
```

### 2.3 The gap between the delivered localization and the summed-compatible form, exactly

The delivered stock proves region-level statements ABOUT hypothetical
value-sets S (st-1..st-3) and disproves every sealed route TO an
n-uniform placement of the actual values (st-4). The gap is therefore
NOT a region-geometry gap — the region theory is closed to the exact
iff — it is a LOCATION gap: no sealed artifact places the five
rho_{p,n}(a) in ANY fixed region n-uniformly, at any angle, at any
delta, on any sub-quantifier of the polydisc except a = 0 (where all
five equal 1). The corrected condition's own hypothesis is the missing
object. The new slice identity (st-5) changes the SHAPE of the gap —
five pairs collapse to one (§3.2) — but not its existence.

---

## 3. THE CLOSURE ATTEMPT, ROUTE BY ROUTE

### 3.1 Route 1 — consume the connected-region equivalence (st-3)

To consume CB7's necessity+sufficiency one must certify, at the summed
quantifier, its hypothesis set: (h-1) the five values lie in a region S
contained in the UNIT CIRCLE; (h-2) S connected; (h-3) 0 outside
conv(S). Sweep of certifiability:

```text
(h-1) UNCERTIFIED, and partially FALSE-in-general: nothing sealed pins
   |rho_{p,n}(a)| = 1. rho is a ratio of ran-C determinants (E1
   :655-666), not a phase; the compression destroys unitarity of the
   determinant even where V is unitary (|det_{ran C}(C V C)| <= 1 with
   equality generically failing — §3.2's own bound cuts AGAINST h-1).
   On the real slice exactly three of the five values are pinned to
   modulus 1 (they equal 1); the cross pair carries no modulus pin in
   either direction (HP6). Off the slice not even that.
(h-2) FREE BUT USELESS ALONE: connectivity is a property of a CHOSEN
   region; any choice must first contain the values n-uniformly, which
   is (h-3)+(h-1)'s location content — the missing object itself. The
   route consumes what it was to deliver: CIRCULAR CONSUMPTION.
(h-3) is the corrected condition — the target. No sealed input.
ROUTE 1 = NOT CLOSABLE. Also noted: the general connected
(varying-modulus) equivalence is UNDECIDED of record (R3C-AUDIT §3.2);
settling it would still not supply (h-1)/(h-2)'s location content, so
it is NOT a blocker of the closure — it is downstream of one.
```

### 3.2 Route 2 — the slice route (the new stock), worked to its exact residue

**(P-a) THE QUANTIFIER COLLAPSE — DERIVED, exact, both directions
(HP3a-c), new.** On the real equal-source slice the five surviving
values are {1, 1, 1, z, conj z} with z = rho_{+-,n}(a,a) (st-5). For
any theta and delta > 0:

```text
separation at (theta, delta)
  ==> cos theta >= delta            [the value 1]
  and cos theta * Re z >= delta     [conjugate-pair sum, HP3a]
  ==> Re z >= delta / cos theta >= delta          [HP3b, exact order]
conversely Re z >= delta (delta <= 1)
  ==> theta = 0 separates all five at delta       [HP3c].
THEREFORE on the slice:
  half-plane localization at the summed-compatible quantifier
  <==> sup-free scalar condition: Re rho_{+-,n}(a,a) >= delta > 0
       for all n and all real |a| <= eps.
FIVE pairs -> ONE pair; the free angle -> theta = 0. This is a
statement-level EQUIVALENCE riding the record's own summed identity
(st-5, "the BAR honored"); no control is derived in either direction.
```

**(P-b) THE UNITARY-COMPRESSION DISC BOUND — DERIVED, exact, new here
(nothing sealed states it; swept §9).** For real sources every
V_p(a_-, a_+) = u_mu(a_-)^dag u_lambda(a_+) is unitary (PA :124-130:
J = -B_D tensor alpha_x is Hermitian; S2TOT X-3 grade, audit-confirmed
including a time-dependent-generator re-proof). The chain, each link
CAS-pinned on generic symbolic matrices:

```text
(b-1) det(1 + A_p(a)) = det(1 + C(V_p - 1)C) = det_{ran C}(C V_p C)
      [the sealed block-triangular mechanism, E1 :655-659; HP4a].
(b-2) (C V C)(C V C)^+ + (C V (1-C))(C V (1-C))^+ = C (V V^+) C
      [defect identity, only C^2 = C used; HP4b]. With V V^+ = 1 the
      ran-C block of the right side is the identity, det = 1.
(b-3) det(M M^+ + N N^+) = |det M|^2 + |m_13|^2 + |m_23|^2 by
      Cauchy-Binet [HP4c] — the excess is a DISPLAYED sum of squared
      moduli. Hence |det M|^2 = 1 - (sum of squared moduli) <= 1
      [HP4d]:
  |det_{ran C}(C V_p(a) C)| <= 1  FOR EVERY n, EVERY pair, EVERY REAL
  SOURCE PAIR — n-uniform, carrier-blind, cell-blind (the bound is the
  absolute constant 1; no carrier or cellulation datum enters).
APPLIED TO rho_{+-,n}(a,a) = num_n(a)/den_n, num_n(a) =
det_{ran C}(C V_{+-}(a,a) C), den_n = det_{ran C}(C V_{+-}(0) C):
BOTH |num_n(a)| <= 1 AND |den_n| <= 1; den_n != 0 at fixed n on the
surviving sector (E1 :666, the constitutive grade, S2TOT-AUDIT p-3).
```

**Where the route dies — the exact residue.** The two disc bounds put
NO bound on the ratio (HP6: |num| = 1/2, |den| = t, ratio 1/(2t)
unbounded as t -> 0+ over exact rationals). A lower bound on Re(num/
den) needs an n-uniform LOWER bound on |den_n| — and den_n is the
a = 0 cross-pair collapse determinant, i.e. GAP-C's family of record
(LINK §0: "a certified lower rate for kappa_n or -log|det_n(0)|"),
where the sealed state TODAY is: divergence signal DERIVED (r-2:
kappa_n -> infinity at the full-family quantifier, B1-DERIVED) and
rate on NEITHER side of the race (r-3: NOT-DERIVABLE-TODAY). Nothing
sealed excludes den_n -> 0 with num_n(a) held away from den_n's phase
ray — and nothing certifies the opposite. The slice closure REDUCES,
exactly and without residue elsewhere, to:

```text
SLICE RESIDUE (named): an n-uniform lower bound on
  Re[ num_n(a) / den_n ]  with  |num_n(a)| <= 1, |den_n| <= 1,
  den_n != 0 per n — equivalently a joint control of the GAP-C race
  for the CROSS PAIR at real sources. NOT on any sealed artifact;
  NOT derived here. ROUTE 2 = NOT CLOSABLE TODAY; residue SHARPENED.
```

**(P-c) THE MARGIN DISPLAY — DERIVED, exact (HP5).** On the slice
Z_hat_n(a,a) is REAL (HP2) and vanishes iff Re rho_{+-} = -3 exactly.
The localization demands Re rho_{+-} >= delta > 0; nonvanishing at
level eta demands only Re rho_{+-} >= 4 eta - 3 (at eta = 1/2: >= -1).
The localization is therefore sufficient-not-necessary FOR THE R-L0b
TARGET ITSELF on the slice, by an exact margin of 3 units of Re — the
second sufficiency-not-necessity, one level above st-2's. Consequence,
descriptive: a future failure to close the localization would NOT bar
R-L0b; conversely nothing here closes R-L0b (its slice form carries
the same GAP-C residue through the same denominator).

### 3.3 Route 3 — the direct summed route (R.3'(b)+(d) assembly)

|Z_hat - 1| <= |tr Delta^Sigma| + |R_n| <= B < 1 would deliver
R.3'(d)'s closure output and (by 1 - B > 0 on a real slice plus st-2's
mechanism) a DERIVED separation for Z_hat itself — but the trace term
consumes S1's certified outward enclosure, uncertified of record (E1
:687 span convention, definition :691-694), whose CELL sup is
"deferred to R-L0" (E1 :688-689) — consumption adjacent to the very
gate the closure's payoff would delete for the n = 1 leg (stated as
consumption-adjacency at bytes, no stronger; the deferral is the cell
axis, the deletion clause is the n = 1 leg) — and the remainder is
R.3'-c, FAILS-AT of record TODAY at the sharpened residue (R3C §2.7:
D-i's surviving-instance square + the ten-term difference form + H-R +
C-L2; the S2TOT slice form carries the same content into o-1/o-2/o-3).
ROUTE 3 = NOT CLOSABLE TODAY (it is the R.3'(c) wall, not this
commission's to discharge).

### 3.4 Route 4 — the four routes of record, re-swept for new stock

Per-pair majorants: still dead (52f2490b untouched today; r-2
STRENGTHENS the divergence side). H-R-conditional: still insufficient
by the exact witness of record (R3C §3.3; nothing today touches it;
H-R consumed here nowhere except as the named hypothesis inside cited
record clauses, never defaulted, never valued). Summed -> per-pair
control bridge: REFUSED — the V-2 void shape; not constructed, not
consumed (the slice identity is the record's own and carries no
control; §5). Fixed-n + limit passage: still no limit object (ZF
§4.1(c)); P1's dilation closure moves (n, ell) -> (n, ell/L) on the
ELL axis only and cannot manufacture the carrier limit. ROUTE 4 = all
four remain dead; no new stock revives any.

---

## 4. THE VERDICT

### 4.1 Classification

```text
HALF_PLANE_CLOSURE = NOT-DERIVABLE-TODAY(
  the localization does not close at the summed-compatible quantifier
  on any route from the sealed stock; no named step is shown to
  provably fail forever (the object is UNDECIDED, not refuted — no
  sealed configuration violates separation, and the slice residue is a
  live named object), so FAILS-AT is not the honest class for the
  closure itself; DERIVED and PARTIAL apply only to the pieces below. )

PARTIAL DELIVERED (exact quantifiers stated):
  P-a  the slice quantifier collapse (five pairs + free angle -> ONE
       scalar condition at theta = 0), equivalence both directions —
       DERIVED at the s-3 grade (real equal-source slice; the sealed
       definitional grade of rho_{+-} constitutive).
  P-b  |det_{ran C}(C V_p C)| <= 1 for all n, all pairs, all real
       source pairs — DERIVED (unitarity at PA bytes; block-triangular
       mechanism at E1 bytes; HP4 chain), NEW HERE subject to check;
       with it the slice obstruction LOCALIZED to the a = 0 cross-pair
       collapse determinant = GAP-C's family (r-2/r-3/LINK of record).
  P-c  the margin display: slice zero-locus at Re rho_{+-} = -3
       exactly; localization sufficient-not-necessary for the R-L0b
       target with margin 3 — DERIVED (HP2/HP5 arithmetic).

THE SEALED CONSEQUENCE: NOT TRIGGERED. The conditional of record
stands verbatim and untouched (E1 :884-885): IF the localization ever
closes at a summed-compatible quantifier, R-L0 is not needed for the
n = 1 leg — NO STRONGER. It does not close here; no gate is deleted.
```

### 4.2 The blockers, each swept for genuineness

```text
B-1  THE CROSS-PAIR COLLAPSE DENOMINATOR (the slice residue): no
     n-uniform lower bound on |den_n| = |det_{ran C}(C V_{+-}(0) C)|
     exists sealed, and no rate for the num/den race. GENUINE: three
     same-day sealed artifacts bound this exact object (r-2 divergence
     signal DERIVED; r-3 the race, rate on neither side; LINK GAP-C
     named as missing) and none delivers it; both disc bounds (P-b)
     are shown insufficient by exact witness (HP6).
B-2  OFF-SLICE (the full complex polydisc quantifier of M-2): the
     unitarity ground fails for complex sources, P-a/P-b do not
     transfer, and the four routes of record are dead (st-4, re-swept
     §3.4). GENUINE: each of the four carries its own sealed
     refutation or absence, severally confirmed by the R3C audit.
B-3  THE REGION-THEOREM HYPOTHESES (Route 1): unit-modulus uncertified
     and generically false for compressed determinants; the location
     hypothesis is the target itself (circular consumption). GENUINE:
     the only sealed modulus pins are the three slice diagonals AT 1;
     P-b bounds modulus from ABOVE only.
B-4  THE TRACE ROUTE'S CONSUMPTION (Route 3): S1's enclosure
     uncertified with its cell sup R-L0-administered, and R.3'-c
     FAILS-AT today. GENUINE: both are named open obligations of
     record with today's sharpened residues; neither is this
     commission's to discharge, and discharging neither is licensed by
     any stock swept here.
```

---

## 5. CONSISTENCY — THE SEALED DICHOTOMIES AND THE ADOPTED CLAUSE (V-1..V-6 UNTOUCHED)

```text
V-1  NOT ENGAGED. The adopted clause quantifies the summed OPERATOR-HS
     family sup_n ||Delta^Sigma_n(a)||_2; every finding here lives at
     the determinant/scalar level (dets, real parts, a margin) or the
     region level. No admissible refutation of the estimate at its own
     quantifier is exhibited or implied; the alpha' = 1/4 record
     stands untouched.
V-2  NOT ENGAGED. No summed -> per-pair CONTROL derivation exists
     here: P-a is a statement-level biconditional riding the sealed
     summed identity s-3 (whose own adjudication of the BAR is of
     record: "the BAR honored", audited with "no smuggled per-pair
     passage"); P-b is a per-pair bound derived DIRECTLY from sealed
     unitarity, consuming nothing summed; no control flows in either
     direction, and the bridge route was REFUSED (§3.4).
V-3  NOT ENGAGED. REM's anchors and the ZF scaffolding are consumed at
     grade, not re-derived, not overturned.
V-4  NOT ENGAGED. No bytes-contradiction: P-b tightens nothing sealed
     (52f2490b bounds an HS NORM below by divergence; P-b bounds a
     DETERMINANT above by 1 — different objects, no tension; the
     coexistence is the standard det-vs-HS gap and is displayed, not
     resolved).
V-5  NOT ENGAGED. The C4 kill is not touched; no stratum claim made.
V-6  NOT ENGAGED. Marks carried span by span; honest menu used.
DICHOTOMIES: FIXED/RUNNING not moved; the fences of record (no scale,
no imported GR, no faithfulness authority) engaged nowhere; gate-list
membership unchanged (R-L4a/b + R-L0(/R-L0b) + C-L2 + OBL-D with
H-R/H-B0 inside); witnesses SCAD_COLOR_SUM_REQUIRES_ABSOLUTE_X_BOUND
and SCAD_SUMMED_SEGMENT_REMAINDER_UNCERTIFIED STAND.
```

---

## 6. THE CAS BATTERY (VERBATIM) AND ITS OUTPUT (VERBATIM)

sympy 1.14.0, fresh venv `hplvenv` (session scratchpad; nothing written
to the workspace but this artifact and its seal).

```python
# HPL-BUILD CAS battery — EXACT SYMBOLIC ONLY (sympy 1.14.0, fresh venv hplvenv).
# Every constant symbolic or an exact rational/surd. Nothing numeric evaluated.
# Groups: HP1 census/derived weights re-derivation (record RA1 shape); HP2 the slice
# assembly at the derived weights (the sealed s-3 identity's weight arithmetic);
# HP3 the theta-collapse equivalence (slice localization <=> one scalar condition,
# NEW); HP4 the unitary-compression determinant bound in exact pieces (block
# identity; defect identity; Cauchy-Binet positivity as a sum of |minors|^2, NEW);
# HP5 the zero-locus margin arithmetic; HP6 the ratio non-transfer witness.
import itertools
import sympy as sp
from sympy import Rational as R

ok = lambda name, cond: print(f"{name}: {'PASS' if cond else 'FAIL'}")

# ===== HP1 — census and derived weights, re-derived from the sealed data =====
lam_v = [sp.Integer(0), sp.sqrt(2), -sp.sqrt(2)]
w_v = [R(1, 2), R(-1, 4), R(-1, 4)]
ph = [1, -1, -1]
pairs = [(i, j) for i in range(3) for j in range(3)]
surv = [(i, j) for (i, j) in pairs if ph[i] == ph[j]]
Nsurv = sp.nsimplify(sum(w_v[i]*w_v[j] for i, j in surv))
c_w = {p: sp.nsimplify(w_v[p[0]]*w_v[p[1]]/Nsurv) for p in surv}
cs = [c_w[p] for p in surv]
ok("HP1 census: 5 surviving; N_surv = 1/2; c = (1/2, 1/8 x 4) all > 0; sum c = 1",
   len(surv) == 5 and Nsurv == R(1, 2) and sorted(cs) == [R(1, 8)]*4 + [R(1, 2)]
   and sum(cs) == 1 and all(c > 0 for c in cs))

# ===== HP2 — the slice assembly at the derived weights (s-3 weight arithmetic) =====
# On the real equal-source slice of record: rho_00 = rho_++ = rho_-- = 1 exactly and
# rho_-+ = conj(rho_+-) (sealed s-3, 798de0dd; audited c944a901 AU22/AU23). Then:
x_, y_ = sp.symbols('x y', real=True)
z_ = x_ + sp.I*y_
Zhat = R(1, 2)*1 + R(1, 8)*1 + R(1, 8)*1 + R(1, 8)*z_ + R(1, 8)*sp.conjugate(z_)
ok("HP2 slice assembly: (1/2)+(1/8)+(1/8)+(1/8)z+(1/8)conj(z) = 3/4 + (1/2)... "
   "= 3/4 + (1/4)(2x)/... EXACT: Z_hat = 3/4 + (1/4)Re rho_{+-}; and Z_hat is REAL",
   sp.expand(sp.expand_complex(Zhat - (R(3, 4) + R(1, 4)*(2*x_)/2))) == 0
   and sp.im(sp.expand_complex(Zhat)) == 0)

# ===== HP3 — THE THETA-COLLAPSE EQUIVALENCE (NEW): five-value localization on the
# slice <=> the single scalar condition Re rho_{+-} >= delta =====
th, dlt = sp.symbols('theta delta', real=True, positive=True)
# HP3a conjugate-pair sum: Re(e^{i th} z) + Re(e^{i th} conj z) = 2 cos(th) Re z EXACT
lhs3a = sp.re(sp.expand_complex(sp.exp(sp.I*th)*z_)) \
      + sp.re(sp.expand_complex(sp.exp(sp.I*th)*sp.conjugate(z_)))
ok("HP3a Re(e^{i th}z) + Re(e^{i th}conj z) = 2 cos(th) Re z EXACT",
   sp.expand(sp.trigsimp(lhs3a - 2*sp.cos(th)*x_)) == 0)
# HP3b forward: separation of {1, z, conj z} at (theta, delta) forces Re z >= delta:
# the value 1 gives cos th >= delta > 0; the pair sum gives cos(th) Re z >= delta;
# then Re z - delta = (cos th Re z - delta cos th)/cos th >= (delta - delta cos th)/cos th
# = delta (1 - cos th)/cos th >= 0. Pin the two exact algebraic identities used:
c_ = sp.Symbol('c', positive=True)   # c := cos theta, 0 < c <= 1 on the sector
rz = sp.Symbol('r_z', real=True)
ok("HP3b forward algebra: (c*rz - delta*c)/c = rz - delta EXACT and"
   " delta/c - delta = delta(1-c)/c EXACT (with 1 - c >= 0 by cos <= 1:"
   " 1 - cos th = 2 sin^2(th/2) EXACT)",
   sp.simplify((c_*rz - dlt*c_)/c_ - (rz - dlt)) == 0
   and sp.simplify(dlt/c_ - dlt - dlt*(1 - c_)/c_) == 0
   and sp.simplify(1 - sp.cos(th) - 2*sp.sin(th/2)**2) == 0)
# HP3c converse: Re z >= delta with delta <= 1 gives separation at theta = 0:
# the five real parts are {1, 1, 1, Re z, Re z}; min(1, Re z) >= delta. EXACT display:
ok("HP3c converse at theta = 0: real parts {1,1,1,Re z,Re z}; 1 - delta >= 0 and"
   " Re z - delta >= 0 are the two displayed conditions; no further content",
   sp.simplify((1 - dlt) + (rz - dlt) - (1 + rz - 2*dlt)) == 0)

# ===== HP4 — THE UNITARY-COMPRESSION DETERMINANT BOUND, in exact pieces (NEW) =====
# C = diag(1,1,0) (rank-2 orthogonal projection in C^3), V generic 3x3 complex.
Vg = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'v_{i}{j}'))
Cp = sp.diag(1, 1, 0)
# HP4a block identity (the E1 :655-659 mechanism in the compressed-A form):
# det(1 + C(V-1)C) = det(top-left 2x2 of V) — the ran-C determinant of C V C.
lhs4a = (sp.eye(3) + Cp*(Vg - sp.eye(3))*Cp).det()
M2 = Vg[0:2, 0:2]
ok("HP4a det(1 + C(V-1)C) = det_{ran C}(C V C) = det(V_topleft2x2) (generic V, exact)",
   sp.expand(lhs4a - M2.det()) == 0)
# HP4b defect identity: (CVC)(CVC)^dag + (CV(1-C))(CV(1-C))^dag = C (V V^dag) C
# (generic V, C idempotent Hermitian) — unitarity enters ONLY as V V^dag = 1.
VH = Vg.conjugate().T
lhs4b = (Cp*Vg*Cp)*(Cp*VH*Cp) + (Cp*Vg*(sp.eye(3) - Cp))*((sp.eye(3) - Cp)*VH*Cp)
ok("HP4b defect identity: (CVC)(CVC)^+ + (CV(1-C))(CV(1-C))^+ = C V V^+ C"
   " (generic V; only C^2 = C used)",
   sp.expand(lhs4b - Cp*Vg*VH*Cp) == sp.zeros(3, 3))
# HP4c Cauchy-Binet positivity: for the 2x3 W = [M | N] (M the ran-C block of CVC,
# N the ran-C x ker-C block of CV(1-C)): det(W W^dag) = |det M|^2 + |m13|^2 + |m23|^2
# — the excess over |det M|^2 is EXACTLY a sum of two squared moduli (no sign choice).
W23 = sp.Matrix(2, 3, lambda i, j: sp.Symbol(f'w_{i}{j}'))
WH = W23.conjugate().T
m12 = W23[:, [0, 1]].det()
m13 = W23[:, [0, 2]].det()
m23 = W23[:, [1, 2]].det()
ok("HP4c Cauchy-Binet: det(W W^+) = |m12|^2 + |m13|^2 + |m23|^2 EXACT (2x3 generic)"
   " => det(M M^+ + N N^+) - |det M|^2 = sum of two |minors|^2 >= 0 DISPLAYED",
   sp.expand((W23*WH).det()
             - (m12*sp.conjugate(m12) + m13*sp.conjugate(m13)
                + m23*sp.conjugate(m23))) == 0)
# HP4d assembly arithmetic: with V V^dag = 1 the ran-C block of C V V^dag C is the
# 2x2 identity, det = 1; so |det_{ran C}(C V C)|^2 = 1 - (|m13|^2 + |m23|^2) <= 1.
ok("HP4d assembly: det(I_2) = 1 and |det M|^2 = 1 - (|m13|^2 + |m23|^2) <= 1"
   " (arithmetic display; the two dropped terms are squared moduli)",
   sp.eye(2).det() == 1)

# ===== HP5 — the zero-locus margin on the slice =====
sol = sp.solve(sp.Eq(R(3, 4) + rz/4, 0), rz)
ok("HP5 Z_hat(a,a) = 0 iff Re rho_{+-} = -3 EXACT; localization needs Re >= delta > 0;"
   " nonvanishing at level eta needs only Re >= 4 eta - 3 (at eta = 1/2: Re >= -1);"
   " the sufficiency margin is 3 whole units of Re",
   sol == [-3] and sp.simplify(4*R(1, 2) - 3 - (-1)) == 0
   and sp.simplify((R(3, 4) + dlt/4) - R(3, 4) - dlt/4) == 0)

# ===== HP6 — the ratio non-transfer witness (both dets in the disc, ratio unbounded) =====
t6 = sp.Symbol('t', positive=True)
num6, den6 = R(1, 2), t6                       # |num| <= 1 and |den| <= 1 for t <= 1
ok("HP6 witness: |num| = 1/2 <= 1, |den| = t <= 1, num/den = 1/(2t) -> oo as t -> 0+:"
   " the two disc bounds alone put NO upper bound on |rho| = |num|/|den|",
   sp.limit(num6/den6, t6, 0, '+') == sp.oo
   and sp.simplify(num6/den6 - 1/(2*t6)) == 0)

print("HP-BATTERY-DONE")
```

Output, verbatim (11/11 PASS):

```text
HP1 census: 5 surviving; N_surv = 1/2; c = (1/2, 1/8 x 4) all > 0; sum c = 1: PASS
HP2 slice assembly: (1/2)+(1/8)+(1/8)+(1/8)z+(1/8)conj(z) = 3/4 + (1/2)... = 3/4 + (1/4)(2x)/... EXACT: Z_hat = 3/4 + (1/4)Re rho_{+-}; and Z_hat is REAL: PASS
HP3a Re(e^{i th}z) + Re(e^{i th}conj z) = 2 cos(th) Re z EXACT: PASS
HP3b forward algebra: (c*rz - delta*c)/c = rz - delta EXACT and delta/c - delta = delta(1-c)/c EXACT (with 1 - c >= 0 by cos <= 1: 1 - cos th = 2 sin^2(th/2) EXACT): PASS
HP3c converse at theta = 0: real parts {1,1,1,Re z,Re z}; 1 - delta >= 0 and Re z - delta >= 0 are the two displayed conditions; no further content: PASS
HP4a det(1 + C(V-1)C) = det_{ran C}(C V C) = det(V_topleft2x2) (generic V, exact): PASS
HP4b defect identity: (CVC)(CVC)^+ + (CV(1-C))(CV(1-C))^+ = C V V^+ C (generic V; only C^2 = C used): PASS
HP4c Cauchy-Binet: det(W W^+) = |m12|^2 + |m13|^2 + |m23|^2 EXACT (2x3 generic) => det(M M^+ + N N^+) - |det M|^2 = sum of two |minors|^2 >= 0 DISPLAYED: PASS
HP4d assembly: det(I_2) = 1 and |det M|^2 = 1 - (|m13|^2 + |m23|^2) <= 1 (arithmetic display; the two dropped terms are squared moduli): PASS
HP5 Z_hat(a,a) = 0 iff Re rho_{+-} = -3 EXACT; localization needs Re >= delta > 0; nonvanishing at level eta needs only Re >= 4 eta - 3 (at eta = 1/2: Re >= -1); the sufficiency margin is 3 whole units of Re: PASS
HP6 witness: |num| = 1/2 <= 1, |den| = t <= 1, num/den = 1/(2t) -> oo as t -> 0+: the two disc bounds alone put NO upper bound on |rho| = |num|/|den|: PASS
HP-BATTERY-DONE
```

Tooling disclosure: the HP2 check label prints an abbreviated arithmetic
trail ("(1/4)(2x)/..."); the checked identity is Z_hat - (3/4 + x/4) = 0
with x = Re z, exactly as displayed in §2.1 st-5. No mathematical claim
differs from its label's content.

---

## 7. CHOICE LEDGER

```text
C-1  READING "summed-compatible" as the three-clause quantifier of
     §2.2 (n-uniform; no per-pair HS majorant; no summed -> per-pair
     control). PROVABLE at bytes: (q-i) from R.3'-c verbatim; (q-ii)
     from the (c) BAR + 52f2490b; (q-iii) from V-2 verbatim. No
     residual builder freedom identified.
C-2  ATTEMPTING the real equal-source slice as an admissible
     sub-quantifier of the polydisc. YOURS (the commission names no
     slice); consequence: P-a/P-b/P-c are slice-scoped and say NOTHING
     off-slice; the off-slice state is reported unchanged (B-2). The
     slice is the record's own object (S2TOT s-3), not built here.
C-3  REFUSING the summed -> per-pair bridge as a construction target.
     PROVABLE: V-2 declares the control-carrying shape void-triggering;
     refusal is the only fence-consistent act.
C-4  NOT attempting to settle the general connected (varying-modulus)
     region equivalence. YOURS; grounds: it is UNDECIDED of record and
     shown DOWNSTREAM of the location blocker (§3.1) — settling it
     closes nothing here; a research-grade excursion would exceed the
     commission without payoff.
C-5  CARRYING the s-3 identity at its sealed grade rather than
     re-deriving the propagator unitarity from PA bytes. PROVABLE
     (grade discipline): the identity is audited end-to-end (AU23)
     including an independent time-dependent-generator re-proof; this
     artifact pins only the weight arithmetic (HP2) it consumes.
C-6  SKIPPING orchestration-class files not literally in the fence
     list (CONTINUATION_STATE.md in both roots; relay_outbox/*).
     YOURS; grounds: blind-builder hygiene — lane summaries are not
     sealed carriers; every consumed byte here is from a sealed,
     sidecar-verified artifact.
C-7  CLASSIFYING the closure NOT-DERIVABLE-TODAY rather than FAILS-AT.
     PROVABLE distinction at the menu's own terms: no step of the
     closure is proven impossible (the slice residue is a live named
     object; no sealed configuration violates separation); what fails
     provably is each ROUTE, and those failures are cited, not new.
C-8  The 3x3/rank-2 frame for the HP4 pins. YOURS (frame choice);
     the identities are frame-polynomial (entries generic symbols;
     no dimension-specific cancellation is consumed — HP4b uses only
     C^2 = C; HP4c is Cauchy-Binet at the exact block sizes induced
     by rank-2-in-3, the smallest frame with nontrivial defect).
```

---

## 8. TOY_SEPARATION

```text
TOYS (carry NO record authority; used only to pin algebra or witness
non-implications):
  t-1  the generic symbolic matrices of HP4a-c (Vg, W23) and the
       diag(1,1,0) projection frame — algebra pins, not record
       operators.
  t-2  the HP6 rational pair (num, den) = (1/2, t) — a witness that
       two disc bounds do not bound a ratio; not a record family.
  t-3  the symbolic z = x + iy of HP2/HP3 — a stand-in for the value
       of rho_{+-,n}(a,a); its only record-facing content is the
       weight arithmetic and the conjugate pairing, both sealed.
RECORD OBJECTS (enter ONLY by citation at grade): rho_{p,n}, Z_hat_n,
Delta^Sigma_n, V_{mu lambda}, C, u_mu, J, kappa_n, det_n(0), the
weights c, the walls W-1/W-2/W-3, the witnesses, the falsifiers.
NO toy result is promoted to a record claim anywhere; every record
claim carries its byte citation.
```

---

## 9. SWEEP RECORD (bounded negatives)

Roots swept: `/Users/bgm/MB Work/alpha-program-archive` and
`/Users/bgm/MB Work/alpha_supervision`, minus fenced classes
(register|road_|ledger|lens|plan|tracker|THE_HANDOFF) and minus
orchestration-class files by C-6; `.proof_deps/` vendored library trees
excluded as non-corpus.

```text
s-neg-1  "half-plane / Sigma_c / cube-root / norm-form / unit-modulus /
   Z-hat" sweep: the localization stock resolves to the R3C pair (+ the
   upstream DISCHARGE/ZF/E1 carriers); alpha_supervision contains no
   additional localization carrier (its Sigma_c hits are the July A32
   masking context, a different object; checked at filename+context
   grade). | TYPE-S | roots as above | queries: half[- _]plane,
   Sigma_c, cube[- _]root, norm[- _]form, unit[- _]modulus,
   Z-hat/Z_hat/Zhat, disconnect, "1/4.*attained".
s-neg-2  unitary-compression determinant bound: no sealed artifact
   states |det_{ran C}(C V C)| <= 1 or any modulus bound on rho
   (queries: "unit disc", "contraction", "singular value", "|rho|",
   "<= 1" against the S2TOT pair and the R3C pair; no hit) — P-b is
   NEW HERE, subject to check. | TYPE-S |
s-neg-3  no sealed artifact newer than the S9AD chain (mtime sweep of
   the workspace, 2026-08-14 18:02 latest = EARN_THE_TRACE audit,
   consumed-listed; none carries localization content beyond what §2
   states; EARN_THE_TRACE is the horn-a surface determination, a
   different object — checked at verdict grade). | TYPE-S |
s-neg-4  "Q-..." tokens inside consumed artifacts (e.g. Q-1049/Q-1050/
   Q-1051 references in the R3C/S2TOT pairs): EXPECTED-UNLOCATABLE,
   noted, not chased. | TYPE-C | constraint: tasking convention.
```

---

## 10. FLAG BLOCK

```text
HALF_PLANE_CLOSURE_STATUS = NOT-DERIVABLE-TODAY(
  blockers B-1 (the cross-pair a = 0 collapse determinant: no sealed
  n-uniform lower bound, no sealed rate — GAP-C's family; r-2/r-3/LINK
  of record), B-2 (off-slice: no unitarity ground; the four routes of
  record dead, re-swept), B-3 (the connected-region theorem's
  unit-modulus + location hypotheses uncertifiable at the summed
  quantifier; circular consumption), B-4 (the trace route: S1
  enclosure uncertified, cell sup R-L0-administered; R.3'-c FAILS-AT
  of record) — each swept for genuineness at §4.2;
  NOT REFUTED: no sealed configuration violates separation; the slice
  residue is a live named object. )

PARTIAL_DELIVERED = THREE(
  P-a the slice quantifier collapse: five-pair free-angle localization
  <==> Re rho_{+-,n}(a,a) >= delta at theta = 0 (HP3, both directions,
  exact; at the sealed s-3 grade);
  P-b the unitary-compression disc bound |det_{ran C}(C V_p C)| <= 1
  — all n, all pairs, all real sources; carrier-blind; NEW subject to
  check (HP4 chain: block identity at E1 bytes + defect identity +
  Cauchy-Binet positivity; unitarity at PA bytes); the slice
  obstruction thereby LOCALIZED to GAP-C's denominator, with HP6 the
  exact witness that the disc bounds alone close nothing;
  P-c the margin display: slice zero-locus Re rho_{+-} = -3 exact; the
  localization is sufficient-not-necessary FOR THE R-L0b TARGET with
  margin 3 (HP5) — non-closure here does not bar R-L0b. )

LICENSED_CONSEQUENCE = NOT-TRIGGERED(
  the sealed conditional stands verbatim, E1 :884-885: IF the
  localization closes at a summed-compatible quantifier, R-L0 is not
  needed for the n = 1 leg — NO STRONGER; it does not close here; no
  gate is deleted; R-L0b remains OPEN. )

ADOPTED_ESTIMATE_BEARING = NONE(
  every finding at the determinant/scalar or region level; the
  operator-HS clause untouched at its own quantifier; alpha' = 1/4
  record unmoved; no falsifier V-1..V-6 engages — V-2 checked
  explicitly: no control runs summed -> per-pair; the slice identity
  consumed is the record's own, BAR-honored, audit-cleared. )

SEALS_VERIFIED = 21/21( §1 table; all recomputed from bytes at path
  this session by full digest; all match sidecars and tasked prefixes;
  none unverifiable. )

FORBIDDEN_IMPORTS = none(
  no scale authority; no imported GR; no faithfulness authority; no
  measured constant; no float as ground; no value frozen; the only
  orderings used are exact (cos <= 1 via the half-angle identity;
  squared-moduli positivity displayed term by term; delta-arithmetic
  over exact rationals); alpha never computed or approached; no
  carrier or cellulation datum introduced (P-b's bound is the absolute
  constant 1); equal-SOURCE slice only, never an equal-time object
  (C6 respected); H-R never defaulted, never valued; no
  register/road/ledger/lens/plan/tracker/handoff file opened. )

MACHINERY_INVOKED = yes(CAS) — sympy 1.14.0, fresh venv hplvenv, one
  battery, 11 checks, 11/11 PASS, script and output verbatim in §6;
  one label-abbreviation disclosure (§6); shasum/file reads otherwise;
  NOTHING numeric evaluated.

alpha_computed = false ; kappa_record_computed = false ;
proof_authorized = false
ALL_RESULTS = CLAIMED until checked.
HALF_PLANE_CLOSURE_RESULT = SEALED.
```
