# STAGE 8 TASK 5 — Ξ_N V002: THE AFFINE-RELATIVE REDRAFT — DARIO V002

Date: 2026-08-05
Lane: Dario (Claude Opus 5), drafting lane
Task: PASTE 583 / Task 5
Supersedes: my V001 (`1b878d7a…`), reviewed **DEFECTIVE** at `c9b62076…`
Authority to draft: DoR-020-A8. **THIS ARTIFACT ADOPTS NOTHING.**

## Lead result

```text
REGISTER_HEAD = Q-508

ADOPTION LICENSES THE INTERFACE; IT DOES NOT INHABIT IT.  (kept in the lead
per the V001 review's V8 reclassification: emptiness is a global nonexistence
result belonging on the stopping board, not among single-datum falsifiers.)

CANDIDATE_V002 = DRAFTED (11 clauses, (Y1)-(Y11))
WINDING = TYPED   (the defined object is a class in R/2piZ; the 2pi<z,n>
                   ambiguity is stated as law, not hidden)
U_HOL = GATED     (R -> K_amb carried as gate item G1 with its own falsifier;
                   NOT discharged by unit triviality -- my own 580 correction)
READY_FOR_REREVIEW = yes
VERB_AUDIT_SELF = CLEAN (+2 disclosed defects in my own V001)

WHAT THE REVIEW KILLED, AND I ACCEPT IN FULL: R-linearity into the integral
lattice is impossible except trivially. I re-derived both horns myself.
WHAT REPLACES IT: Xi_N is a SCALE-INVARIANT, DISJOINT-SUPPORT-ADDITIVE
stratified assignment -- not a homomorphism at all. Doubling a source does not
change which loop it threads; that is the physical content, and it is what
makes a nonzero map into a discrete lattice possible.

MEMBER_BOUND = false ; FIXED_POINT_EXECUTED = false ; END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = false
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-508 | verified |
| Review of V001 `c9b62076…` | verified; N1 table, §4 Display I, §7 winding attack consumed |
| My V001 `1b878d7a…`; my 580 review `61d41a3e…` | verified |
| Output name absent before construction | verified — no clobber |

## 1. What I accept from the review, re-derived

[PROVABLE] **The kill is correct and I verified both horns myself.**

```text
(a) Xi_N : (D_N^Loc,+) -> (Lambda_N^cyc,+) continuous additive:
    D_N^Loc is connected, Lambda_N^cyc discrete, so the image is one point;
    a homomorphism sends 0 to 0, so the image is {0}.

(b) Xi_N : D_N^Loc -> K_N^(cyc,R) R-linear with im subset Lambda_N^cyc:
    {Xi_N(t x)} = {t Xi_N(x)} is a connected line through 0 inside a
    discrete lattice, hence {0}, so Xi_N(x) = 0.
```

**My V001 (X1) was genuinely ill-typed, and the defect was mine to catch.** I asserted R-linearity
because the domain is a real space, without checking what the *codomain* geometric holonomy actually
requires.

[PROVABLE] **The absolute display was also ill-typed, for a reason I should have seen.**
`Conn(P_N)` is **affine**: `A_1 - A_0` is a tangent vector, and `u_z(A_N)` is not typed on a
connection. Only the relative form is licensed, and the review derives it exactly:

```text
Hol_A(z) := product_(e in E_N) h_e(A)^(z_e)          on z in Lambda_N^cyc,

Hol_(A_1)(z) Hol_(A_0)(z)^(-1)
 = product_e (h_e(A_1) h_e(A_0)^(-1))^(z_e)
 = exp(i sum_e z_e integral_(gamma_e) (A_1 - A_0))
 = exp(i u_z(A_1 - A_0)).                             (D1-5)
```

Note the exponent `z_e` must be an **integer** for `(D1-4)` to be defined — that, not a metric
preference, is why the lattice is forced. `(D1-5)` is the exponential form of the sealed local phase
formula with `d Phi_z = u_z`, and it is independent of any cycle-basis decomposition.

## 2. V1 — the corrected clause set

[YOURS] **CANDIDATE Ξ V002 (eleven clauses). Drafted; not adopted.**

### 2.1 The type, corrected

```text
(Y1) TYPE -- INTEGRAL, NOT LINEAR.
     Xi_N : D_N^Loc -> Lambda_N^cyc, the INTEGRAL cycle lattice, for every
     admitted finite stage N. Lambda_N^cyc is a Z-module; NO R-linearity and
     NO continuity is claimed, and neither could hold nontrivially (§1).

(Y2) COMPATIBILITY LAW -- what replaces linearity.
     (i)  SCALE INVARIANCE:  Xi_N(t x) = Xi_N(x) for every real t != 0,
          and Xi_N(0) = 0.
     (ii) DISJOINT-SUPPORT ADDITIVITY: if x,y in D_N^Loc have disjoint
          record-visible supports, then Xi_N(x + y) = Xi_N(x) + Xi_N(y).
     No additivity is asserted on overlapping supports.
     Xi_N is thus a STRATIFIED ASSIGNMENT, locally constant away from 0 --
     not a homomorphism. This is consistent with (Y1): the ray {t x} maps to
     the single point Xi_N(x), so the connectedness argument of §1 does not
     apply.
```

[YOURS] **Why this is the right replacement and not a patch.** "Which loop does this source encircle"
is a **topological** datum, not a linear one: scaling a current does not change what it threads, and
sources in disjoint regions thread independently. Scale invariance is what makes a nonzero map into a
discrete lattice possible at all, and disjoint-support additivity is the loop-level form of the
program's own "what-lives-where" discipline. The `Z`-module structure is then used honestly — as the
target's own structure, consumed only through (Y2)(ii).

### 2.2 The holonomy, consumed relatively

```text
(Y3) RELATIVE CONSUMPTION -- the affine structure explicit.
     Conn(P_N) is AFFINE. Xi_N is consumed only through the RELATIVE
     character, against a retained reference member A_0:

       Theta_N^rel(x; A_1, A_0)
        := Hol_(A_1)(Xi_N(x)) Hol_(A_0)(Xi_N(x))^(-1)
         = exp( i u_(Xi_N(x))(A_1 - A_0) )        by (D1-5).

     NO absolute Hol_(A_N)(Xi_N(x)) is asserted, and NO reference is
     SELECTED: the whole affine family is retained and the object of record
     is the relative class, indexed by the ordered pair (A_1, A_0).

(Y4) WINDING -- stated as law, not hidden.
     u_(Xi_N(x))(A_1 - A_0) is a real number, but the character sees it only
     modulo 2 pi. The DEFINED object is therefore the class

       [ u_(Xi_N(x))(A_1 - A_0) ] in R / 2 pi Z.

     The ambiguity is exactly 2 pi <z,n> for z = Xi_N(x) in Lambda_N^cyc and
     n an integral shift, hence lies in 2 pi Z. Consequently:
       - any consumer of the CLASS is well defined;
       - any consumer of a REAL LOGARITHM is NOT, absent a certified chart.
     Clause (Y4) forbids extracting a real scalar without that chart, and
     names the extraction as gate item G2.
```

[PROVABLE] **Why (Y4) must be a clause and not a footnote.** The review's winding attack settles it:
granting the factor line and writing `p := u_(Xi(Ker(Rhat)))(A - A_0)`, neutrality supplies only
`p in 2 pi Z`; if `p != 0` then `t |-> exp(i t p)` winds through all of `U(1)`, so the factor line
**cannot** lie in one proper arc carrying a single-valued logarithm, and if `p = 0` the scalarized
coefficient is zero. So a global linear log-factorization is unavailable either way. **The candidate
must own that rather than inherit it.**

### 2.3 Units, and the real-to-integral passage separated

```text
(Y5) UNITS -- the D-side clause repaired.
     By the derivation of record, the Hodge-carrier pairing has unit class 1:
     from the ratified [R_A] = U_A^(-2), [Delta_k] = 1 and hence
     [<x,h>_N] = U_k^(-1) U_k = 1. So the D-side datum consumed here is
     DIMENSIONLESS, and NO unit conversion is required or asserted anywhere
     in (Y1)-(Y4).

(Y6) REAL-TO-INTEGRAL PASSAGE -- its own clause, not a unit clause.
     Membership of Xi_N(x) in Lambda_N^cyc is a TOPOLOGICAL/INTEGRALITY
     condition on the assignment, wholly separate from (Y5). It is supplied
     by (Y2)'s stratified typing, NOT by any unit compatibility. Conflating
     the two was a V001 defect and is prohibited here.
```

[PROVABLE] **This repairs the V001 defect exactly as diagnosed.** My V001 (X5) asked unit
compatibility to do two jobs — fix a dimensionless scale *and* supply the real-to-integral passage.
It can do neither: the class is already 1, so there is nothing to convert, and integrality is not a
unit property. **(Y5) and (Y6) separate them.**

### 2.4 Transport, written to what is sealed

```text
(Y7) RANK-PRESERVING TRANSPORT -- W3 scope only.
     For f : N -> M rank-preserving in the W3 scope, with j_f^K the ratified
     cycle inclusion restricted to the lattice, j_f^Lambda := j_f^K|_Lambda:

        Xi_M ( D-side transport of f )(x) = j_f^Lambda ( Xi_N(x) ).

     The D-side transport is NOT claimed sealed; it is gate item G3.

(Y8) CYCLE-CREATING ARROWS -- the downward equation WRITTEN.
     For f : N -> M cycle-creating, ONLY the downward old-image law is
     asserted. With rho_f^D the sealed old-image restriction on the D side and
     r_f^Lambda : Lambda_M^cyc -> Lambda_N^cyc the downward old-image cycle
     restriction:

        Xi_N ( rho_f^D (y) ) = r_f^Lambda ( Xi_M (y) )
          for every y in the licensed old-image domain.

     NO upward law is asserted on new cycles: there is no equation of the
     form Xi_M(...) = (upward map)(Xi_N(...)), in conformity with the no-lift
     theorem and FC4. On target-only new cycles Xi carries no assertion --
     an explicitly typed absence, not a zero map.
```

[PROVABLE] V001's (X6) said "the sealed D-side transport", which is not sealed, and *gestured* at the
cycle-creating case. **(Y7) names the unsealed part as a gate item and (Y8) writes the downward
equation out.**

### 2.5 The remaining discipline clauses

```text
(Y9)  SUPPORT (anti-counterterm). supp_Lambda(Xi_N(x)) is contained in the
      record-visible support closure of x. NOTE: this predicate is typeable
      only once the D-side/cycle-side support comparison is bridged; that
      bridge is gate item G4, and until it exists (Y9) is a STATED BUT
      UNRUNNABLE test -- recorded as such rather than presented as live.

(Y10) COVARIANCE AND NO SELECTION. For admitted u with D-side action u_D and
      cycle-side action u_Lambda: Xi_N o u_D = u_Lambda o Xi_N. The whole
      admitted family {Xi_N} and the whole affine family {A} are retained;
      no member, no reference connection, and no gauge representative is
      selected. The D-side action u_D is gate item G5.

(Y11) READER- AND CONSEQUENCE-FREEDOM. Xi_N is fixed before and independently
      of any reader, p_loc, response value, threshold, fixed point, end test,
      or numerical consequence.
```

## 3. V2 — `U^Hol` faced, not finessed

[PROVABLE] **My own 580 correction applies here and I apply it against my own candidate.** The scalar
seam `U^Hol : R -> K_amb` is an **explicitly unbuilt obligation of record** whose source is *literally*
`R`. Unit triviality discharges nothing there: I established that the Hodge pairing is dimensionless
and that this **did not** close the H route's seam either, because the obstruction was never units.
The same holds on HOL.

```text
GATE ITEM G1 -- U^Hol : R -> K_amb.
  STATUS: unbuilt obligation of record; NOT discharged by (Y5).
  FALSIFIER G1-F: any proposed U^Hol that is address-INDEPENDENT.
    Reason (my 580 derivation, transposed): the evaluated period is
    orientation-odd while K_amb carries the trivial orientation action;
    writing U as multiplication by mu(a), covariance forces
    mu(a^-) = -mu(a), so an address-independent U forces mu == 0 and the
    return vanishes identically. A Z2-equivariant map from the sign
    representation to the trivial one is zero.
  THEREFORE: any admissible U^Hol must CARRY ADDRESSES.
```

[PROVABLE] **The seam is COMMON, and I cite rather than duplicate.** This is the same
orientation-address structure the H route needs at its own final seam — the law-with-address principle
surfacing at both routes' scalar returns. **The Ξ_N candidate does not re-derive it and does not claim
credit for it**; it records that the two routes share this seam and that discharging it on one route
is evidence, not proof, for the other. Any rule proposed to discharge `U^H` must also discharge
`U^Hol`, or the rule is unsound.

[PROVABLE] **Consequence for the comparison, stated against my own draft's interest:** HOL's scalar
seam is not cheaper than H's. My 577 comparison already said the seams are largely common; this
candidate confirms it from the inside.

## 4. V3 — the gate rebuilt

### 4.1 Alternatives

| # | Alternative | Assessment |
|---|---|---|
| (a) | **V002 as drafted** — stratified, scale-invariant, disjoint-support-additive, relative, winding-typed | see minimality |
| (b) | **THE NULL CANDIDATE** — no `Ξ_N`; HOL closed; Γ built on H alone | **Lawful and retained.** Costs: the A8 identification falsifier goes vacuous, and Joint II becomes a single point of failure. Gains: no authored physical content. |
| (c) | **A linear `Ξ_N` into the real cycle space, dropping integrality** | **Refuted.** The geometric character `(D1-4)` needs integer exponents; without integrality there is no bounded holonomy to consume. This was V001's error. |
| (d) | **Absolute holonomy with a selected reference `A_0`** | **Refuted.** `Conn` is affine and A1 selects no reference and admits nontrivial bundles; selecting one violates no-selection. |
| (e) | **Strengthen `p = 0` on the full factor line** (winding attack option) | Live but stronger: it forces the scalarized coefficient to zero, which may empty the route. Kept of record. |
| (f) | **Derive `Ξ_N` instead of authoring it** | Not currently available; **must stay open** on the A4 precedent — if derived later, the authored row becomes contentless and upgrades to derived. |

### 4.2 Minimality on the corrected type

[YOURS] The candidate still introduces **one** new map. Its codomain `Λ_N^cyc` is the integral
sublattice of the already-ratified cycle carrier — not a new carrier. The holonomy is **derived**
relatively via `(D1-5)` from A1's adopted connection and adopted transport. Zero new coefficients,
zero new units (by (Y5) there is nothing to convert), zero new carriers, no member and no reference
selected.

[YOURS] **The corrected type is weaker than V001's, and that is the point.** V001 claimed R-linearity
and got a map that must vanish; V002 claims only scale invariance and disjoint-support additivity —
the least structure that (a) lands in a discrete lattice nontrivially and (b) suffices for
`(D1-5)`'s character to be applied. Nothing stronger is consumed anywhere in (Y1)–(Y11).

### 4.3 The eight voids revisited

[YOURS] Re-audited against the review's own verdicts. Two were unformed, one partial, one
misclassified; all four are repaired or relocated.

```text
V1 DEPENDENCY.        RETAINED, failure-capable. Unchanged.
V2 CURVATURE-RELABEL. RETAINED, failure-capable. A1's flat-holonomy attack is
                      the permanent regression.
V3 HIDDEN COUNTERTERM. REPAIRED IN STATUS: the support predicate is (Y9), and
                      (Y9) is now explicitly UNRUNNABLE until gate item G4
                      bridges the D-side/cycle-side support comparison. It is
                      carried as a stated-but-unrunnable test, NOT as a live
                      falsifier. The review was right that V001 presented it
                      as live.
V4 DISCIPLINE.        SPLIT. Live now: reality; no-upward-lift (testable
                      against (Y8)'s written equation); no-selection.
                      Deferred to gate items: support (G4), D-side covariance
                      (G5). Stated separately rather than as an omnibus.
V5 SELECTION.         RETAINED, failure-capable.
V6 A8 IDENTIFICATION. RETAINED, with the review's caveat ADOPTED: a displayed
                      disagreement voids the disagreeing construction(s)
                      PENDING ADJUDICATION and does not by itself isolate
                      Xi_N as the culprit. Fault isolation is a separate step.
V7 IDENTITY BRANCH.   REWRITTEN on the corrected type -- see (Y-A7) below.
V8 EMPTY FAMILY.      RELOCATED to the stopping board as a global nonexistence
                      result, per the review. Its content is kept IN THE LEAD
                      of this artifact: adoption licenses, it does not inhabit.

NEW GATE ITEMS (obligations, not voids):
G1 U^Hol : R -> K_amb, with falsifier G1-F (address-independence).
G2 the certified logarithm chart, absent which no real scalar may be extracted.
G3 the D-side transport.
G4 the D-side/cycle-side support bridge.
G5 the D-side covariance action u_D.
```

### 4.4 The (X9) repayment, re-verified on the corrected form

[YOURS] Restated as **(Y-A7)** and now correctly typed — precomposed with `Ker`, relative, integral,
and honest about what it does not supply:

```text
(Y-A7) A7 IDENTITY-BRANCH OBLIGATION (epsilon = 1).
   For every x in the addressed response family and for the addressed factor
   basis element,

     Theta_N^rel( Ker_(a,K)(x); A_1, A_0 ) = 1_(U(1))
     <=> u_( Xi_N(Ker_(a,K)(x)) )(A_1 - A_0) in 2 pi Z.

   On epsilon = 0 no such constraint is imposed.
```

[PROVABLE] **Three corrections to V001's (X9), all from the review:**

1. it now **precomposes `Ker_(a,K)`** — V001 applied `Ξ_N` directly to response-side objects, a
   domain error, and `Ker` remains unbuilt (gate item, not assumed);
2. it is **relative and integral**, inheriting neither the affine mis-typing nor the real/integer
   defect;
3. it supplies **raw neutrality only**. Per the winding attack it does **not** supply the arc/log/unit
   conjuncts that `(HOL2)` also requires. **(Y-A7) is therefore a partial repayment**, and G1/G2 carry
   the rest. V001 presented it as the whole repayment; that was wrong.

[PROVABLE] **Single-element refutability survives the correction:** one actual `x` in the addressed
family with `u_(Ξ(Ker(x)))(A_1 - A_0) not in 2 pi Z` refutes it. So the clause remains falsifiable on
record data, which is the authored-row standard.

## 5. V4 — verb audit on my own board

| My line | Strongest verb my sources carry | Honest? |
|---|---|---|
| `CANDIDATE_V002 = DRAFTED` | authored, tagged YOURS; nothing adopted | **CLEAN** |
| the kill accepted | both horns re-derived by me, not taken on report | **CLEAN** |
| `(Y2)` as the replacement type | **mine**, tagged YOURS; consistency with §1 shown explicitly | **CLEAN** — I show why the connectedness argument does not apply rather than asserting it |
| `(D1-5)` relative display | the review's derivation, consumed and cited | **CLEAN** — I do not re-present it as my own |
| `WINDING = TYPED` | the review's §7 attack, adopted as a clause | **CLEAN** |
| `U_HOL = GATED` | my own 580 correction, applied against my own candidate | **CLEAN** — it makes my route look worse, and I say so in §3 |
| `(Y9)` unrunnable | the review's V3 verdict, adopted | **CLEAN** — carried as unrunnable rather than quietly kept live |

[PROVABLE] **Two disclosed defects in my own V001, both real and both mine:**

1. **(X1) R-linearity into a discrete lattice.** I asserted linearity from the domain's structure
   without checking the codomain that geometric holonomy requires. The map would have been identically
   zero. This is a type error of exactly the kind I audit others for.
2. **(X2) absolute holonomy on an affine space.** I wrote `Hol_(A_N)(z) = exp(i u_z(A_N))` and tagged
   it PART-PROVABLE with an instruction that a lane display it. **The instruction was right and the
   formula was wrong** — `Conn` is affine, so `u_z(A_N)` is not typed. My hedge caught that the corpus
   does not write the relation; it did not catch that the relation is ill-formed.

[PROVABLE] I record a third item as a **near-miss rather than a defect**: my V001 minimality argument
claimed the candidate "reduces to a forced assignment where the record already determines one",
tagged PART-PROVABLE with an instruction to display it before relying on it. The review's Display II
examined exactly that and the instruction held — nothing was inherited that should not have been.

```text
VERB_AUDIT_SELF = CLEAN (+2 disclosed defects in my own V001)
```

## 6. Fence and stopping board

```text
STATUS = DRAFT FOR RE-REVIEW. NOTHING ADOPTED.
TYPE = integral lattice; scale-invariant, disjoint-support-additive; NOT linear
HOLONOMY = consumed RELATIVELY only; affine structure explicit; no reference selected
WINDING = the defined object is a class in R/2piZ; real-log extraction gated (G2)
UNITS = dimensionless by derivation; real-to-integral passage separated (Y6)
TRANSPORT = W3 rank-preserving written; cycle-creating downward equation written;
            no upward law on new cycles
NEW_OBJECTS = 1 (Xi_N); Hol derived relatively; Lambda_N^cyc a ratified sublattice
GATE_ITEMS = G1..G5 ; VOIDS = V1..V7 live-or-repaired ; V8 relocated to stopping board
ADOPTION_DELIVERS = the interface, NOT its inhabitance
MACHINERY_APPEAL = false
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

No register, plan, tracker, git, commit, push, member-binding, fixed-point, end-test, or evaluation
action was performed by this lane. No law was adopted.

CANDIDATE_V002 = DRAFTED (+11 clauses (Y1)–(Y11): integral-lattice type with no linearity claim;
the scale-invariance/disjoint-support-additivity law that replaces linearity and is consistent with
the discreteness argument that killed V001; relative consumption of the holonomy with the affine
structure explicit and no reference selected; the winding clause; the repaired dimensionless units
clause; the real-to-integral passage separated into its own clause; W3-scope transport with the
cycle-creating downward old-image equation written out and no upward law; support, covariance, and
reader-freedom; plus (Y-A7) as the corrected A7 repayment)
WINDING = TYPED (+the defined object is the class `[u_(Ξ(x))(A_1 − A_0)] in R/2πZ`, the ambiguity being
exactly `2π<z,n>` for integral `z` and integral shift `n`; consumers of the class are well defined,
consumers of a real logarithm are not, absent the certified chart carried as gate item G2 — the
review's winding attack shows basis neutrality gives only `p in 2πZ`, and a nonzero `p` winds the
factor line through all of U(1) so it cannot lie in one logarithm arc)
U_HOL = GATED (+carried as gate item G1 with falsifier G1-F: any address-INDEPENDENT `U^Hol` forces
`mu ≡ 0` and the return vanishes identically, since a Z₂-equivariant map from the sign representation
to the trivial one is zero — my own 580 derivation applied against my own candidate; +explicitly NOT
discharged by unit triviality, because the obstruction was never units; +its relation to the H route's
orientation-address seam is CITED, not duplicated, and the parity rule is stated: any rule discharging
`U^H` must also discharge `U^Hol` or it is unsound)
READY_FOR_REREVIEW = yes
VERB_AUDIT_SELF = CLEAN (+2 disclosed defects in my own V001: R-linearity into a discrete lattice,
which would have forced the map to vanish identically; and absolute holonomy written on an affine
connection space, where my PART-PROVABLE hedge caught that the corpus does not write the relation but
not that the relation is ill-formed)
