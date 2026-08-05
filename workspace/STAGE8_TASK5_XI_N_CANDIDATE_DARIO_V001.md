# STAGE 8 TASK 5 — THE Ξ_N WHERE-CLAUSE CANDIDATE: FULL-GATE DRAFT — DARIO V001

Date: 2026-08-05
Lane: Dario (Claude Opus 5), drafting lane for the HOL route's blocking object
Task: PASTE 579 / Task 5
Authority to draft: DoR-020-A8 (Γ carried on both routes; the Ξ_N where-clause amendment "drafted
through the full gate for the principal's separate ruling; construction follows only if gated and
adopted").

**THIS ARTIFACT ADOPTS NOTHING.** It drafts a candidate for the principal's ruling. No lane may treat
any clause below as law, and no construction may proceed on it until it is gated and adopted.

## Lead result

```text
REGISTER_HEAD = Q-504 ; DoR-020-A8 = LAW

CANDIDATE = DRAFTED (9 clauses, (X1)-(X9))
GATE = COMPLETE (8 void conditions, all directly falsifiable on actual record data)
NULL_ALTERNATIVE = stated (alternative (b): no Xi_N, HOL route closed -- lawful)

THE DESIGN CHOICE THAT MAKES THIS MINIMAL: the candidate introduces exactly ONE
new map. Its codomain is the ALREADY-RATIFIED cycle carrier K_N = ker(B_N^T),
and the holonomy it feeds is DERIVED from A1's already-adopted connection member
through A1's own "transport derived from the declared members" clause. Zero new
carriers, zero new coefficients, zero new scales, no member selected.

WHAT ADOPTION WOULD AND WOULD NOT DELIVER -- stated up front because the
distinction is the whole lesson of A1's empty torsor: adoption licenses the
INTERFACE. It does not inhabit it. The admitted Xi family must still be shown
nonempty on actual record data, and that is a witness burden of the same shape
as the H route's Loc.

MEMBER_BOUND = false ; FIXED_POINT_EXECUTED = false ; END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = false
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-504; A8 read in full | verified |
| My provenance determination `a58400f6…` | verified |
| Loc build `b53d9e93…` ((B6)/(B7) and the counterterm fence) | verified |
| A1 decision `c4dc5976…`; adopted where-clauses `19b20603…` | verified |
| Audit V002 `44202c06…` ((HOL1)–(HOL2a)) | verified |
| My J7 adjudication `f76139e5…` (the filing-level falsifier signal) | verified |
| Output name absent before construction | verified — no clobber |

## 1. W1 — the candidate clause text

### 1.1 What Ξ_N is, and what it is not

[PROVABLE] The gap this fills is the one I determined at `a58400f6…`, and it is decisive and prior to
every value question: **(B6) demands a map out of a kernel space**, `Hol_N : D_N^Loc -> …`, while
holonomy is a function of `(loop, connection)` and carries **no kernel argument**. A1's path/current
clause is a covariance law relating currents *across arrows*; it is not a construction of a cycle from
a source kernel. Nothing adopted closes that gap.

[YOURS] **Ξ_N is exactly that missing interface and nothing more: the declaration of which
record-visible cycle a given source-kernel datum encircles.** In the program's own idiom it is a
"what-encircles-what" clause, the loop-level companion of A1's "what-lives-where".

[YOURS] It is **not**: a holonomy (that is derived, below); a curvature datum; a new carrier; a
coefficient; a normalization; or an additive contribution to the period. The last exclusion is the
(B7) fence and it is carried into void 3.

### 1.2 The objects reused rather than introduced

[PROVABLE] All of the following are already ratified or adopted, and the candidate takes them as they
stand:

```text
K_N := ker(B_N^T)                      the ratified cycle carrier (metric V005, W1)
u_z                                     the period functional, (L_N a)_e = integral_(gamma_e) a
A_N                                     the adopted U(1) connection member (A1 clause 2)
eta_conn,R(A_G') = tilde_f_R^* A_G'     its adopted transport ("transport derived from
                                        the declared members")
D_N^Loc = span{kappa_T,N}
          + iota_N^Q408(Kernbar_N^cyc(O_N^cyc))    the sealed kernel domain
```

[PART-PROVABLE] **The holonomy is derived, not authored.** For `z in K_N`,

```text
Hol_(A_N)(z) := exp(i u_z(A_N)),                                   (D1)
```

the exponentiated period of the adopted connection along the cycle `z`. This is the standard
relation, and it uses only `u` (ratified) and `A_N` (adopted) — which is precisely what A1's
"transport derived from the declared members" licenses. Tagged PART-PROVABLE because the corpus
nowhere writes (D1); it writes the ingredients. **A lane adopting this candidate should display (D1)
once against the adopted transport rather than inherit it from here.**

[PROVABLE] `Hol_(A_N)` is then a homomorphism `(K_N,+) -> U(1)`, and is **gauge-invariant on closed
cycles** — for `A -> A + d log g`, the period shifts by an element of `2 pi Z` and the exponential is
unchanged. So no gauge representative is selected by (D1), which matters for clause (X7).

### 1.3 The candidate clauses

[YOURS] **CANDIDATE Ξ (nine clauses). Drafted; not adopted.**

```text
(X1) TYPE.
     Xi_N : D_N^Loc -> K_N, for every admitted finite stage N.
     R-linear and continuous for the declared quotient topology on D_N^Loc
     and the ratified topology on K_N.

(X2) DERIVED COMPOSITE.
     Hol_N := Hol_(A_N) compose Xi_N : D_N^Loc -> U(1),
     Theta_(a,K)^Hol := Hol_N compose Ker_(a,K) : O_a^resp -> U(1).
     Hol_N is DERIVED from (X1) and (D1); it is not separately authored.

(X3) SUPPORT (the anti-counterterm clause).
     supp(Xi_N(x)) is contained in the record-visible support closure of x,
     for every x in D_N^Loc. Xi_N may not carry a source to a cycle it does
     not meet.

(X4) COVARIANCE AND NO SELECTION.
     For every admitted realization automorphism, relabeling, reality,
     orientation, frame, or bundle-gauge arrow u,
        Xi_N compose u = u_* compose Xi_N.
     The whole admissible family {Xi_N} is retained; no member is selected,
     and orbits are carried entire.

(X5) UNITS.
     Xi_N carries the declared D_N^Loc unit class to the ratified K_N class
     U_K, so that u_(Xi_N(x))(A_N) is dimensionless and (D1) lands in U(1)
     with NO new conversion factor. No unit is introduced.

(X6) RESTRICTION AND NATURALITY.
     On a rank-preserving arrow f : N -> M,
        Xi_M compose (the sealed D-side transport of f) = j_f^K compose Xi_N.
     On a cycle-creating arrow, ONLY the proved downward old-image law holds;
     no upward lift is created, in conformity with the no-lift theorem and
     FC4.

(X7) READER- AND CONSEQUENCE-FREEDOM.
     Xi_N is fixed before, and independently of, any reader, p_loc, response
     value, threshold, fixed point, end test, or numerical consequence. Its
     dependency position is upstream of every such object.

(X8) ADDRESS.
     Where the addressed factor line is formed, Xi_N sends the addressed
     source datum to the addressed primitive cycle, fixing the address
     without selecting a member of the retained family.

(X9) A7 BRANCH OBLIGATION  (the A7_HOL_BRANCH_COMPAT repayment).
     On the A7 IDENTITY branch (epsilon = 1) the candidate carries the
     explicit obligation
        u_(Xi_N(x))(A_N) in 2 pi Z
     for every x in the addressed response family and for the addressed
     factor basis -- equivalently, Xi_N lands in ker(Hol_(A_N)) there.
     On the A7 ZERO branch (epsilon = 0) no such constraint is imposed and
     the full lattice is retained.
```

### 1.4 How (X9) repays `A7_HOL_BRANCH_COMPAT`

[PROVABLE] The audit's (HOL2) demands `Theta^Hol(Y_1(K)) = 1_(U(1))` and
`Theta^Hol(Rhat_(Kcycle,a)) = 1_(U(1))`, plus `1 in U_b`, `log_b(1) = 0`, `U^Hol(0) = 0`; and (HOL2a)
then *displays* `q_1^Hol = 0` and `chi_1^Hol = 0` rather than stipulating them. The audit is explicit
that "(HOL2) is not derived by pretending that `E_C` acts on `U(1)`", and that absent it the identity
branch is "**unformed**, not silently dropped."

[YOURS] **(X9) puts that obligation where the only freedom actually lives.** Under (X2), `Theta^Hol`
factors as `Hol_(A_N) o Xi_N o Ker` with `Hol_(A_N)` derived and `Ker` sealed — so the sole free
object is `Ξ_N`, and (HOL2)'s neutrality condition is exactly the statement that `Ξ_N` lands in
`ker(Hol_(A_N))` on the identity branch. Stating it as a condition on `Ξ_N` rather than as a property
of `U(1)` is what keeps it falsifiable on record data: a single actual `x` in the addressed family
with `u_(Ξ(x))(A_N) not in 2 pi Z` refutes it. That is void 7.

[PROVABLE] Note the shape this preserves: on the identity branch the Hol route reaches `q_1^Hol = 0`,
which is **in-lattice and verdict-returning** (strict contraction) — so **two-sidedness, which A7 makes
a condition of branch carriage, survives on this route**. That is the same structural property I
verified for the H route's identity branch, reached by a different mechanism.

## 2. W2 — the gate

### 2.1 Genuine alternatives, kept of record

| # | Alternative | Content | Assessment |
|---|---|---|---|
| (a) | **The candidate (X1)–(X9)** | one new map into the ratified cycle carrier | see minimality, §2.2 |
| (b) | **THE NULL CANDIDATE — no Ξ_N** | the HOL route is closed; Γ is built on H alone | **Lawful, and it must stay on the board.** Costs: the H route stands alone with its `E_C` exposure on both A7 branches; A8's identification falsifier becomes vacuous (nothing to compare against); if H blocks at `Loc`, no second route exists. Gains: no authored physical content, and the program's authored-row count does not rise. |
| (c) | **Addressed-only Ξ_N** | define the correspondence only where the address is formed | Cheaper and weaker. It cannot support a general period, so the Hol route would be addressed-only and could not serve as an independent check of H off the address — which is most of what carrying two routes is for. |
| (d) | **Ξ_N with an integrality/quantization condition** | require `Ξ_N` to land in the integral cycle lattice | **Stronger than anything consumes.** It would author flux quantization — new physics well beyond an interface — and (HOL2) does not need it. Declined on minimality. |
| (e) | **Derive Ξ_N instead of authoring it** | a theorem from sealed stock | Not currently available: my provenance determination established A1 supplies no correspondence from a source kernel to a loop. **But this path must stay open**, on the A4 precedent — if a later theorem derives the correspondence, this authored row becomes contentless and upgrades to derived. |

### 2.2 Minimality, argued from what (HOL1b)–(HOL2) actually consume

[PROVABLE] What the audit's interfaces consume is exactly two things: a map carrying `O^resp` through
`Ker` into something `Hol` can eat, and the identity-branch neutrality of the resulting composite.

[YOURS] The candidate supplies precisely those and nothing else:

- **one** new map, `Ξ_N`, and no other new object;
- codomain `K_N` — **already ratified**, not a new carrier;
- `Hol_N` **derived** by (D1) from the adopted connection and its adopted transport, not authored;
- **zero** new coefficients, scales, normalizations, bases, or complements;
- **no member selected** — the whole admitted family is retained (X4);
- the identity-branch obligation stated as a condition on `Ξ_N` (X9), so it adds no independent law.

[PART-PROVABLE] **The candidate reduces to a forced assignment where the record already determines
one.** Where a source datum's support closure meets exactly one record-visible cycle, (X3) leaves
`Ξ_N` no freedom beyond scale, and (X5) fixes the scale; so the candidate supplies genuinely new
content only where the correspondence is actually underdetermined. Tagged PART-PROVABLE: the
single-cycle reduction is my argument, not a sealed theorem, and a lane should display it before
relying on it.

### 2.3 Void conditions — eight, all directly falsifiable on actual record data

[YOURS] The standard here is the filing-level signal I recorded at `f76139e5…`: **derived** rows defer
to the sealed number, **authored** rows must carry directly-falsifiable void conditions on actual
record data. `Ξ_N` would be authored, so every void below is written to be refutable by an exhibited
datum, not by a later computation.

```text
V1  DEPENDENCY VOID. Any Xi_N whose definition is traceable to a reader,
    p_loc, response value, threshold, fixed point, end test, or numerical
    consequence. FALSIFIABLE by the dependency-order ledger (the F_PLDEC
    instrument, which has caught this class before).

V2  CURVATURE-RELABELING VOID. Any Xi_N or Hol_N defined from curvature F,
    from c_1, or from any characteristic-class datum rather than from the
    connection's transport. The A1 flat-holonomy fence is decisive here:
    equal curvature and equal characteristic class do NOT determine
    holonomy, so curvature data cannot be relabeled as a period.
    FALSIFIABLE by exhibiting the definition path.

V3  HIDDEN-COUNTERTERM VOID  (the (B7) fence, and the reason this clause
    exists at all). Any Xi_N violating (X3) -- i.e. any x whose image
    Xi_N(x) has support outside the record-visible support closure of x.
    Such an Xi_N would be adding period content the source does not carry,
    which is exactly the Loc build's "hidden holonomy counterterm, not
    localization". FALSIFIABLE by exhibiting one such x.

V4  DISCIPLINE VOID. Failure of support, units, reality, restriction, or
    covariance; or any upward lift created on a cycle-creating arrow.
    FALSIFIABLE by an exhibited arrow or datum.

V5  SELECTION VOID. Any selection of a member from the admitted Xi family,
    or any use of Xi_N that is not member-sensitivity tagged where the
    consumer requires a member. FALSIFIABLE on the consumer's own text.

V6  IDENTIFICATION VOID  (A8, law). On any cell where BOTH routes are
    formed, a displayed disagreement between the H period and the Hol
    period. Per A8 this voids the disagreeing construction(s) pending
    adjudication; on this route the disagreeing construction is Xi_N. No
    lane may assume the identification. FALSIFIABLE, and it is the sharpest
    external check this candidate has.

V7  A7 IDENTITY-BRANCH VOID. On epsilon = 1, an actual x in the addressed
    response family, or an addressed factor basis element, with
    u_(Xi_N(x))(A_N) not in 2 pi Z. This falsifies (X9)/(HOL2) and, per the
    audit, triggers A7's own branch falsifier. DIRECTLY FALSIFIABLE.

V8  EMPTY-FAMILY VOID. If the admitted Xi family is empty on actual record
    data, the row is CONTENTLESS and the HOL route is UNFORMED -- recorded
    as such, never silently carried. This is A1's empty-torsor lesson
    written into the candidate's own gate rather than left to be
    rediscovered.
```

## 3. W3 — the consequence board

### 3.1 Under adoption

[PROVABLE] **Adoption licenses the interface; it does not inhabit it.** This is the A1 lesson stated
against my own draft: A1 adopted the bundle-with-connection as *law-only*, with an empty-torsor horn
that "supplies no witness", and the program then spent relays discovering that a law is not an
inhabitant. The same is true here.

[YOURS] The HOL route's remaining construction under adoption:

| Item | Relay-sized? |
|---|---|
| Display (D1) against the adopted transport | **yes**, one relay |
| Exhibit an admitted `Ξ_N` on the two actual reciprocal-loop prototypes | **yes**, one relay |
| The arc/log/unit scalar seam (`U_b` image proof, `log_b`, `U^Hol`) | **yes**, one relay |
| `A7_HOL_BRANCH_COMPAT` via (X9) on the identity branch | **yes**, one relay |
| The route carrier, metric, and completeness for the Hol return | **yes**, one relay |
| **Inhabitance of the admitted Ξ family across the actual tower** | **NO — a witness burden, not a relay.** Same shape as the H route's `Loc`. It must not be scheduled as a relay, and adoption must not be read as discharging it. |

### 3.2 Under rejection

[PROVABLE] The H route stands alone, carrying its `E_C` exposure explicitly: on `epsilon = 1` the
confinement forces the reciprocal vanishing (in-lattice at `q = 0`, verdict-returning); on
`epsilon = 0` the pairing is left undecided and the full lattice is retained. A8's identification
falsifier becomes **vacuous** — there is no second route to disagree — so the program loses its one
independent cross-check on the period, and the `Loc` construction becomes a single point of failure.

### 3.3 Both A7 branches, both outcomes

| | HOL adopted | HOL rejected |
|---|---|---|
| **`epsilon = 0` (ZERO)** | both routes run the full lattice; the pairing decides on H, the period decides on Hol; **V6 is live and is the strongest available check** | H alone runs the full lattice; the pairing decides; no cross-check |
| **`epsilon = 1` (IDENTITY)** | H reaches `q = 0` by the `E_C` confinement; Hol reaches `q_1^Hol = 0` by (X9)/(HOL2a) — **the same verdict by two independent mechanisms**, which is itself evidence; both in-lattice, so carriage survives on both routes | H reaches `q = 0` by the confinement; carriage survives; the agreement evidence is unavailable |

[PART-PROVABLE] The bottom-left cell is worth the principal's attention: on the identity branch the two
routes reach the same verdict through genuinely different mechanisms — a metric confinement on one
side, a holonomy neutrality obligation on the other. That is the kind of convergence that is hard to
arrange by accident, and it is only visible if both routes are carried.

## 4. W4 — verb audit on my own board

| My line | Strongest verb my sources carry | Honest? |
|---|---|---|
| `CANDIDATE = DRAFTED` | authored clause text, tagged **YOURS** throughout; nothing adopted | **CLEAN** |
| "one new map" minimality | `K_N`, `u`, `A_N` and its transport all verified adopted/ratified before drafting | **CLEAN** |
| `Hol_(A_N)(z) = exp(i u_z(A_N))` | ingredients ratified; the relation itself is **not written in the corpus** | **CLEAN** — tagged PART-PROVABLE, with an explicit instruction that a lane display it rather than inherit it from me |
| the single-cycle reduction | my argument, not a sealed theorem | **CLEAN** — tagged PART-PROVABLE with the same instruction |
| `GATE = COMPLETE (8 voids)` | each void written to be refuted by an exhibited datum, per the authored-row standard | **CLEAN** |
| `NULL_ALTERNATIVE = stated` | alternative (b), with its costs and gains both given | **CLEAN** — I state the case *for* the null candidate, not merely its name |
| adoption ≠ inhabitance | A1's empty-torsor precedent applied against my own draft | **CLEAN** — the caveat is in the lead, not buried |

[PROVABLE] **No prior finding of mine required correction in this drafting.** The three uncarried
properties I determined at `a58400f6…` map onto the draft as follows, and I record the mapping so the
principal can check it: **GAP 1** (the kernel-argument gap) is (X1) — the whole point of the clause;
**GAP 2** (units) is (X5); **GAP 3** (law-only, no witness) is void V8 and the §3.1 caveat. Nothing in
the determination is contradicted or quietly softened here.

```text
VERB_AUDIT_SELF = CLEAN
```

## 5. Fence and stopping board

```text
STATUS = DRAFT FOR THE PRINCIPAL'S RULING. NOTHING ADOPTED.
NEW_OBJECTS_INTRODUCED = 1 (Xi_N); Hol_N derived; K_N, u, A_N reused as ratified
NEW_COEFFICIENTS = 0 ; NEW_CARRIERS = 0 ; NEW_UNITS = 0 ; MEMBERS_SELECTED = none
CLAUSES = 9 ; VOIDS = 8 ; ALTERNATIVES = 5 (including the null candidate)
ADOPTION_DELIVERS = the interface, NOT its inhabitance
IDENTIFICATION_FALSIFIER = carried as void V6 (A8, law)
TWO_SIDEDNESS = preserved on this route via (X9)/(HOL2a)
MACHINERY_APPEAL = false
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

No register, plan, tracker, git, commit, push, member-binding, fixed-point, end-test, or evaluation
action was performed by this lane. No law was adopted and no route was chosen.

CANDIDATE = DRAFTED (+9 clauses (X1)–(X9): type/linearity; the derived composite `Hol_N` and
`Theta^Hol`; the support anti-counterterm clause; covariance and no-selection; units; restriction and
naturality with no upward lift; reader- and consequence-freedom; the address; and the A7
identity-branch obligation `u_(Ξ(x))(A_N) in 2πZ` that repays `A7_HOL_BRANCH_COMPAT` by placing it on
the only free object; +the design keeps it to ONE new map by taking `K_N = ker(B_N^T)` as codomain and
deriving the holonomy from A1's adopted connection through A1's own transport clause — zero new
carriers, coefficients, units, or selected members)
GATE = COMPLETE (+8 voids, every one refutable by an exhibited datum rather than by a later
computation, per the authored-row standard: V1 dependency/F_PLDEC; V2 curvature-relabeling, fenced by
A1's flat-holonomy result; V3 the hidden-counterterm void carrying the (B7) fence as a support
condition; V4 discipline; V5 selection; V6 the A8 identification falsifier, which is law and is this
candidate's sharpest external check; V7 the A7 identity-branch obligation; V8 the empty-family void,
which writes A1's empty-torsor lesson into the candidate's own gate)
NULL_ALTERNATIVE = stated (+alternative (b): no `Ξ_N`, the HOL route closed, Γ built on H alone —
lawful, and argued rather than merely named: it costs the independent cross-check and makes `Loc` a
single point of failure while A8's identification falsifier goes vacuous; it gains the program no new
authored physical content; three further alternatives are kept of record, including the
derive-instead-of-author path which must stay open on the A4 precedent)
VERB_AUDIT_SELF = CLEAN
