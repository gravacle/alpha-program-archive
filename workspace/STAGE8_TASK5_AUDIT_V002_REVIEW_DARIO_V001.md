# STAGE 8 TASK 5 — REVIEW OF AUDIT V002 + THE COMPARATIVE ROUTE ANALYSIS — DARIO V001

Date: 2026-08-05
Lane: Dario (Claude Opus 5), cross-family reviewer of record
Task: PASTE 577 / Task 5
Under review: `STAGE8_TASK5_CHAIN_CONFORMANCE_AUDIT_LANE3_V002.md` (`44202c06…`, verified, 1,137 lines)
Law: DoR-020-A7 (both E_C branches carried). My 574 findings (`73524d7a…`) are the standard.

## Lead result

```text
REGISTER_HEAD = Q-502

AUDIT_V002 = DEFECTIVE (+2 substantive, both in the CONSERVATIVE direction)
  The repairs I demanded are CORRECT. The modulus is fixed, my two
  counterexamples score exactly 1 and 1/4, Step 6 is retyped for the right
  reason, the residues are 3/6/9/12, the branch-carried lattice is total and
  untilted, and the F_PLDEC sweep holds. Nothing is made false.
  D1 METRIC_SECANT_FACTOR_CERT (M9) is EXISTENTIALLY TRIVIAL for chi != 0.
     V002 traded V001's substantive-but-mistyped collinearity witness for a
     correctly-typed but EMPTY one. The factorization now carries no
     information on the direct arm: A_loop = q/|chi| by construction.
  D2 Mode Q of the gate is VACUOUS under V002's own (M2) reissue, yet is
     carried as a hypothesis of (M4) and booked as undischarged debt.
     Provenance is mine: I offered a DISJUNCTION of fixes; V002 applied both
     arms and the first emptied the second.

ROUTE_ANALYSIS = stated (five heads per route, plus exclusivity and cost)

RECOMMENDATION = CARRY_BOTH  [YOURS]
  H prioritised for lane effort; Hol carried as the typed alternative pending
  the principal's A1 ruling; their non-identification carried as a bonus
  falsifier. Reasoning in §2.4. THE CHOICE REMAINS THE PRINCIPAL'S.

VERB_AUDIT_SELF = CLEAN (+1 disclosed defect in my own prior recommendation)

MEMBER_BOUND = false ; FIXED_POINT_EXECUTED = false ; END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = false
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

**The headline.** V002 does what a repair should: it fixes the decisive defect exactly, installs my
counterexamples as permanent regressions with the *rejected* values recorded for contrast, and
retypes Step 6 on the audit's own definition rather than on my say-so. Its two residual defects both
**over-state** remaining debt rather than understate it — the safe direction, but still a mis-pricing
of the decision the principal is about to make, which is why they matter here specifically.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-502 | verified |
| Audit V002 `44202c06…`, 1,137 lines | verified before reading |
| My 574 review `73524d7a…`; V001 `d02576c8…`; V004 `1da746c3…` | verified |
| DoR-020-A7 | read in full |
| Output name absent before construction | verified — no clobber |

## 1. J1 — the repairs

### 1.1 The modulus repair — PASS, and my own regressions rerun

[PROVABLE] (M2) is `q := sup_(K != K') d(B(K),B(K'))/d(K,K')` with **both slots the same Banach
metric** and the artifact stating "No ambient absolute value occurs in (M2)." (M3)'s biconditional is
correct in both directions — forward by taking `q = q_loop` in the supremum, reverse because every
quotient is `<= q < 1` so the supremum is too — and the singleton empty-sup `= 0` convention is right.

[PROVABLE] **I reran my own two counterexamples against (M2):**

```text
A. translated isometry   D=R, d=2|.|, B(K)=K+1
   q = sup 2|(K+1)-(K'+1)| / 2|K-K'| = 1.          EXPECTED 1, OBSERVED 1.
   1 < 1 is false, so no contraction is claimed -- correct, since K+1=K has no solution.
   (the rejected mixed quotient reported 1/2)

B. quarter-contraction   D=[0,1], d=|K^2-K'^2|, B(K)=K/2
   q = sup (|K^2-K'^2|/4)/|K^2-K'^2| = 1/4.        EXPECTED 1/4, OBSERVED 1/4.
   1/4 < 1, contraction correctly identified; K=0 is the fixed point.
   (the rejected mixed quotient reported infinity)
```

Both score exactly. The regressions are installed with their completeness and continuity premises
displayed, and correctly gated as "symbolic toy regression, not a program evaluation". **PASS.**

### 1.2 D1 — `METRIC_SECANT_FACTOR_CERT` is existentially trivial

[PROVABLE] (M9) asks only for **some** `a_sec : {(K,K') : K != K'} -> K_amb` with

```text
d(B(K),B(K')) = |chi| |a_sec(K,K')| d(K,K')     for every K != K'.
```

No further constraint is placed on `a_sec`. Since `K != K'` implies `d(K,K') > 0` and `d(BK,BK')` is
finite, for **any** `chi != 0` the explicit choice

```text
a_sec(K,K') := d(B(K),B(K')) / (|chi| d(K,K'))
```

is well defined and satisfies the identity identically. Then

```text
A_loop := sup |a_sec| = sup d(BK,BK')/(|chi| d(K,K')) = q_loop/|chi|   by (M2),
```

so (M10)'s `q_loop = |chi| A_loop` reduces to `q = |chi| (q/|chi|) = q` — **a rearrangement, not a
factorization.** The complete characterization is: (M9) holds iff `chi != 0` **or** `B` is
`d`-constant.

[PROVABLE] **What was traded away.** V001's (S9-5b) carried a genuine constraint — a secant
coefficient **on the same response line**:

```text
Y^per(K) - Y^per(K') = a_sec(K,K') d^per(K,K') Rhat_(Kcycle,w,N)
```

— a collinearity condition. V002 explicitly demotes it: "The response-line vector equation from V001
may be retained as a consistency witness, but it is **not** (M9)."

[PROVABLE] **The demotion's stated reason is sound; the repair is not.** V002 is right that "an
equality in an ambient coordinate does not by itself determine distance in an alternate complete
metric" — that is precisely why V001's form was mistyped. But the correct fix is to require **both**
the collinearity *and* the metric equality, not to drop the collinearity. As it stands `A_loop^per` is
a rails-shaped quantity (`q/|chi|`) wearing the name of the Step-8 Schur amplitude — the look-alike
pattern, at the amplitude level.

[PROVABLE] **Bearing.** No lattice cell is false; I checked and found no wrong entry. But the factor
decomposition is uninformative on the direct arm, and (M11)'s listed failure mode "the direct factor
branch lacks the metric-secant equality (M9)" is **unreachable** whenever `chi != 0`. Repair is one
clause: require `a_sec` to *be* the response-line coefficient **and** satisfy the metric equality.

### 1.3 D2 — Mode Q of the gate is vacuous, and the provenance is mine

[PROVABLE] `DIRECT_MODULUS_Q := "Step 9 defines q_loop^per directly by (M2), and the Step-8 derivative
is used only as a consistency witness, never as the definition"`. But (M4a) states
`(S9-2-V002) := (M2)` — V002's own Step 9 **is** defined by (M2) — and V002 honours the second
conjunct in its own text. Both conjuncts hold by construction, so `(M5;Q)` is unconditionally true.
Yet (M4) carries it as a hypothesis of the repaired Step-10 biconditional, and the residue ledger
books `(M5)` — unqualified by mode — as undischarged.

[PROVABLE] **The provenance is my own recommendation, and I own it.** My 574 review offered a
disjunction: "read the numerators as `d^per`, **or** gate (S10-1) on `PERIOD_MODULUS_COMPAT_CERT` as
well." V002 applied **both** arms. Applying the first is what emptied the second. My disjunction was
correct as stated but I did not flag that the arms are **not independent** — taking the first makes
the second vacuous on the direct branch. That is a defect in my recommendation, not only in the
audit's execution of it.

[PROVABLE] **Bearing.** Nothing false: a surplus hypothesis on a true implication stays true, and
V002 correctly refuses to let the gate's failure block the direct route. The defect is status
accuracy in the direction the program has named a failure pattern — presenting as gated what is
ungated. Repair: mark `(M5;Q)` vacuous-under-(M2), state row 9's debt as `(M5;FACTOR)`.

### 1.4 Step 6, the residues, the branch lattice, and F_PLDEC — PASS

[PROVABLE] **Step 6 retype: correct and for the right reason.** The audit's own (A0) makes a missing
**carrier** a residue trigger while RE-DERIVABLE covers only "map, domain, bound, or threshold"; Step
6's content *is* the carrier commitment. Residues are exactly **3/6/9/12**. No collateral retype; the
one-verdict rule holds.

[PROVABLE] **The identity branch's `q = 0` cell — recomputed by me.** A7's IDENTITY branch is
`E_C,RL c_RL = c_RL`. My (K-1) confinement gives `m_T,RL in im(P_H,RL) intersect ker(E_C,RL)
= span{c_RL} intersect ker(E_C,RL)`. For `x = lambda c_RL`, `E_C x = lambda c_RL`, so `x in ker(E_C)`
iff `lambda = 0`. Hence

```text
m_T,RL = 0   -- reciprocal vanishing FORCED on the identity branch,
=> chi^per = 0
=> q^per = 0   (multiplicative form)
=> 0 < 1: strict contraction, a LICENSED IN-LATTICE CELL RETURNING A VERDICT.
```

**The branch does not exit its lattice.** This matters more than it appears: A7's own falsifier is
"a branch whose period computation **exits its certified lattice** voids that branch's carriage." So
the two-sidedness I credited at 574 is now, under A7, a **condition of branch carriage** — and the
(M2) repair is therefore load-bearing for A7 itself. Had the modulus defect stood, branch-carriage
decisions would have been taken on a broken instrument.

[PROVABLE] **Lattices total, and untilted.** The `epsilon = 0` and `epsilon = 1` harmonic lattices and
the holonomy lattices are total, no cell silently assumes an unproved certificate, and I checked
specifically for a branch tilt: neither branch is given privileged development, and no cell wording
treats one as the expected case. **A7's equal carriage is respected.**

[PROVABLE] **F_PLDEC sweep verified independently.** I traced the dependency order rather than
accepting the table: neither the algebraic reader, nor `p_loc`, nor the false anchor (physical-J2's
`pi_Mx(Loc(Kernbar(Q(L_T)))) = 1`, an equation *of record* on an unbuilt composite, not a theorem),
nor any threshold or fixed-point consequence enters the period construction at any point. **Clean.**

## 2. J2 — the comparative route analysis

*Analysis for the principal. No route is chosen here; the audit chooses none either, and states "No
sealed implication orders these alternatives."*

### 2.1 The H route (through `Loc^C`)

| Head | Finding |
|---|---|
| **Objects still to build** | the physical `Loc` (`Loc_N^phys`, and `Loc_N^C = iota^H o Loc^phys`); `Ker` image-membership in `D_N^Loc`; `Gamma^H`, `Per^H`, `u^H`; the period-domain certificate; `FIXED_PERIOD_FACTOR_CERT`; `(M5;FACTOR)`; the A7-branchwise carrier and certificates; and the standing J2 premises **(F1)** and **(F3)** (`Loc_M eta_f^K = j_f^C Loc_N`, which exists nowhere in the corpus) |
| **Sealed results reused** | substantial: the projector cert's Hodge machinery (`d`, `delta`, `Delta`, `P_H`, and the *rank-preserving* intertwiners — confirmed); the ratified carrier metric; A5's contact-reducing law (authored); A6's scoped J2 (ratified); the assembly V003/V004 package bottom. **This route has by far the most confirmed machinery to stand on.** |
| **Failure modes, by name** | *look-alike substitution* at `Loc^phys` (the pattern that killed two builds at Q-459/Q-463 — a rails object standing for a physical face); *F_PLDEC circularity* at `pi_Mx` (the historical trap, currently clean and must stay so); *false anchor* at physical-J2 (1-3), already flagged and honoured; *status-verb optimism* at the `A_RP^+` inhabitance claim |
| **A7 interaction / two-sidedness** | `E_C` is consumed on this route, so the branches genuinely differ: `epsilon = 1` **forces** the reciprocal zero (my §1.4 recomputation), landing in-lattice at `q = 0` with a verdict; `epsilon = 0` leaves the pairing undecided and retains the full lattice. **Two-sidedness survives on both branches.** |
| **Seven relays instantiated** | R1 modulus repair (done, route-independent) · R2 route commitment · R3 Step-6 carrier seam · R4 `FIXED_PERIOD_FACTOR_CERT` · R5 `(M5;FACTOR)` · R6 Steps 4/5 reissue · R7 Step-10 lattice transfer, **with the `Loc` construction itself standing outside the relay count — it is not relay-sized and must not be scheduled as one** |

### 2.2 The Hol route (through `Xi_N` and (HOL1b)–(HOL2))

| Head | Finding |
|---|---|
| **Objects still to build** | `Xi_N` (the kernel-to-loop correspondence) — **which is an A1 where-clause amendment, i.e. a principal's ruling, not a lane task**; `Z_N^loop`; the `Hol` evaluation; a whole-image-in-`U_b` proof; the `log_b` and unit seam; the route carrier (or a new contraction-theorem instance on `U(1)`); a separate fixed-holonomy factor certificate; and `A7_HOL_BRANCH_COMPAT` |
| **Sealed results reused** | thinner, and must be read carefully. A1 adopts the U(1) bundle **with connection** and states "transport derived from the declared members" — so holonomy has genuine *structural* provenance. But A1 is twice marked **"law-only"**, its field-torsor horn permits the empty torsor which "supplies no witness", and the adopted text contains **zero** occurrences of "holonomy" or "Wilson". **Structural licence, no inhabitant.** |
| **Failure modes, by name** | the *hidden holonomy counterterm* hazard named by the earlier build ("without independently constructing (B6), (B7) is a hidden holonomy counterterm, not localization"); *look-alike substitution* at `Hol` (an abstract holonomy standing for the physical one); the *empty-torsor* problem (a law with no inhabitant); *scope-shrink* if `Z_N^loop` is drawn narrowly |
| **A7 interaction / two-sidedness** | `E_C` is **not consumed**, so the confinement is evaded and its map-level proof does not transfer. But this is **not** a free pass: A7 requires the reciprocal-vanishing outcome, and the audit's own unbuilt `(HOL1b)`–`(HOL2)` candidate is what types that outcome on Hol and yields `q = 0`; `epsilon = 0` retains the full lattice. **The E_C evasion is partly repaid as `A7_HOL_BRANCH_COMPAT`.** |
| **Seven relays instantiated** | the same seven, but **R2 becomes a principal's ruling rather than a lane task**, which changes the schedule *shape*, not just its length: the program cannot advance this route by lane work at all until the amendment is decided |

### 2.3 Exclusivity — the routes are NOT mutually exclusive

[PROVABLE] The audit treats them as parallel candidates, not alternatives to be eliminated: "no
identification with `Gamma^H`" for the Hol realization, and "No sealed implication orders these
alternatives. This audit does not choose a route." V001 said the same of the two `Gamma`
realizations. **Nothing in the record forbids building both.**

[PART-PROVABLE] But carrying both is not carrying two ways to compute one thing. The two routes are
**not known to agree**, and identifying them would itself be a theorem — the earlier build's warning
that an un-independently-constructed harmonic term is "a hidden holonomy counterterm, not
localization" is exactly the hazard of assuming agreement. So carrying both means carrying **two
candidate periods with an open identification question**.

[PART-PROVABLE] **Cost.** Not double. R1 (modulus, already done), R3 (Step-6 carrier seam), and the
common debts — addressed `K`-independent `Res^resp`, the nonzero addressed-line certificate, `Ker`'s
definition and image typing, support/units/reality, rank-preserving naturality, and the
cycle-creation old-image law — are **route-independent or share their form**. What is genuinely
route-specific is the blocking object (`Loc` vs `Xi_N`), the scalar seam, the carrier, and the factor
certificates.

[PROVABLE] **Lawful?** Yes, and A7 is the direct precedent: it carries a genuine freedom rather than
choosing. One honest caveat — a *branch* is a freedom in the theory, whereas a *route* is a
construction choice, so the precedent is analogical rather than binding. It nonetheless establishes
that "carry rather than choose" is within this program's discipline when nothing orders the options.

### 2.4 Recommendation

[YOURS] **`CARRY_BOTH`**, with H prioritised for lane effort and Hol carried as the typed alternative
pending the principal's A1 ruling. My reasoning, offered as reasoning and not as a decision:

1. **Nothing orders them.** No sealed implication does, and I found none. A forced choice now would be
   made on preference, not evidence — and this program's whole discipline is against that.
2. **Their blocking objects are different in kind.** H's is a *construction* (lane work, with the most
   confirmed machinery to reuse). Hol's is a *declaration* (a principal's amendment asserting a new
   physical correspondence — which source kernel encircles which loop). The program's own precedent is
   to author only where something is provably not derivable (A4, A5); nobody has shown `Loc` is not
   derivable. That asymmetry argues for putting lane effort on H **first** — not for discarding Hol.
3. **They fail differently, so neither de-risks the other.** H is exposed to look-alike substitution
   and the F_PLDEC trap at `pi_Mx`; Hol to the counterterm hazard and the empty torsor. Building one
   teaches you little about the other's soundness. That is precisely the condition under which
   carrying two candidates is worth its cost rather than wasteful.
4. **Carrying is cheap here and dear later.** The route-independent relays are shared now; if the
   program commits to one route and it blocks, the other restarts cold with its amendment unresolved.
5. **Their non-identification is an asset if carried deliberately.** Two independently constructed
   periods that agree would be strong cross-family evidence; if they disagree, that is a finding, not
   a failure. **Carry the identification question as a declared open falsifier** rather than letting a
   later lane assume it.

[YOURS] What I would *not* recommend: choosing Hol now on the strength of its `E_C` evasion. That
advantage is real but partly repaid as `A7_HOL_BRANCH_COMPAT`, and it is purchased with an amendment
the lanes cannot schedule.

**The choice is the principal's. This is analysis and a recommendation, not a ruling.**

## 3. J3 — fresh attack, and verb audit

[PROVABLE] **My attack was the repair-collateral sweep**: (M2) changes the modulus everywhere it
appears, so I swept every result citing (S5-1)/(S9-2)/(S9-5b) to see whether any downstream claim
silently changed truth value by inheritance rather than re-derivation. **The audit survives** — no
lattice cell is false and no step verdict was justified on the old numerator. The sweep is what
surfaced D1: the one place the repair *did* change something silently is `A_loop`'s content, where the
collinearity constraint was dropped along with the mistyped ambient equality. **The attack found a
defect by way of the repair being incomplete rather than wrong.**

[PROVABLE] **Branch-tilt attack: the audit survives.** Neither A7 branch is favoured in development,
conditionality, or wording.

[PROVABLE] **Verb audit on the audit's §6.4.** V002 **repaired** V001's lead defect (the unconditional
"is exact" is gone). Two residual overstatements, both from D1/D2: the residue ledger books `(M5)`
unqualified when Q-mode is vacuous, and `METRIC_SECANT_FACTOR_CERT` is presented as a falsifiable
gate when it is unfalsifiable off `chi = 0`. Correct board line:
`CLEAN_EXCEPT(row 9 mode-qualification; (M9) falsifiability)`.

### Verb audit on my own board

| My line | Strongest verb my sources carry | Honest? |
|---|---|---|
| modulus repair `PASS` | (M2)/(M3) read; both my counterexamples rerun by hand | **CLEAN** |
| `D1 (M9) trivial` | (M9)'s text — no constraint on `a_sec` beyond the identity; explicit construction | **CLEAN** |
| `D2 Q-mode vacuous` | (M8) vs (M4a)'s `(S9-2-V002) := (M2)` | **CLEAN** — and I record the provenance as my own |
| identity-branch `q = 0` | (K-1) applied to A7's IDENTITY branch, recomputed here | **CLEAN** |
| `RECOMMENDATION = CARRY_BOTH` | tagged **YOURS**; reasoning given as reasoning | **CLEAN** — the choice is left to the principal explicitly |

[PROVABLE] **One disclosed defect in my own prior work.** My 574 review offered the modulus fix as a
disjunction ("read the numerators as `d^per`, **or** gate (S10-1) on the cert as well") without
flagging that the arms are not independent — the first empties the second on the direct branch. V002
applied both and inherited a vacuous gate. **The mis-pricing in D2 originates in my recommendation,
not in the audit's execution of it**, and I record it here rather than leaving it to be found.

```text
VERB_AUDIT_SELF = CLEAN (+1 disclosed defect in my own prior recommendation)
```

## 4. Fence and stopping board

```text
MODULUS_REPAIR = CORRECT (+regressions score 1 and 1/4 exactly)
STEP_6 = correctly retyped; residues 3/6/9/12
BRANCH_LATTICE = total, untilted; identity branch in-lattice at q = 0
F_PLDEC = clean
(M9) = EXISTENTIALLY TRIVIAL off chi = 0 (+collinearity dropped, not replaced)
(M5;Q) = VACUOUS under (M2) (+carried as live debt)
ROUTES = not mutually exclusive; nothing sealed orders them
ROUTE_CHOSEN = none ; E_C_BRANCH_CHOSEN = none ; all authority preserved
MACHINERY_APPEAL = false
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

No register, plan, tracker, git, commit, push, member-binding, fixed-point, end-test, or evaluation
action was performed by this lane. No law was adopted and no route was chosen.

AUDIT_V002 = DEFECTIVE (+D1: `METRIC_SECANT_FACTOR_CERT` (M9) constrains `a_sec` only by the metric
identity, so for `chi != 0` the choice `a_sec := d(BK,BK')/(|chi| d(K,K'))` satisfies it identically,
`A_loop` collapses to `q/|chi|` and (M10) becomes `q = q` — V002 traded V001's substantive-but-mistyped
response-line collinearity for a correctly-typed but empty witness, when the fix was to require both;
+D2: `DIRECT_MODULUS_Q` is satisfied by construction since (M4a) sets `(S9-2-V002) := (M2)`, so
`(M5;Q)` is unconditionally true yet is carried as a hypothesis of (M4) and booked as undischarged
debt — provenance mine, my 574 fix was a disjunction whose arms are not independent; +both defects are
in the conservative direction and nothing is made false; the modulus repair, my two regressions at
exactly 1 and 1/4, the Step-6 retype, the 3/6/9/12 residues, the total untilted branch lattice with
the identity branch in-lattice at `q = 0`, and the F_PLDEC sweep all PASS)
ROUTE_ANALYSIS = stated (+per route: object list, sealed reuse, named failure modes, A7/two-sidedness
interaction, and the seven relays instantiated; +H reuses by far the most confirmed machinery and its
blocking object is a CONSTRUCTION; +Hol evades the `E_C` confinement but partly repays it as
`A7_HOL_BRANCH_COMPAT`, and its blocking object `Xi_N` is a PRINCIPAL'S AMENDMENT that lanes cannot
schedule; +the routes are NOT mutually exclusive, nothing sealed orders them, and the common debts are
shared so carrying is not double cost — but they are not known to agree, so carrying both means
carrying two candidate periods with an open identification question)
RECOMMENDATION = CARRY_BOTH (+reasoning tag YOURS: nothing orders them so a forced choice would rest on
preference not evidence; their blocking objects differ in kind — a construction versus a declaration,
and the program authors only where something is provably not derivable, which nobody has shown for
`Loc`; they fail differently so neither de-risks the other, which is exactly when carrying two
candidates earns its cost; carrying is cheap now and dear later; and their non-identification is an
asset if carried deliberately as a declared open falsifier. H prioritised for lane effort, Hol carried
pending the A1 ruling. THE CHOICE REMAINS THE PRINCIPAL'S.)
VERB_AUDIT_SELF = CLEAN (+1 disclosed defect in my own prior recommendation: the 574 modulus fix was
offered as a disjunction without flagging that its arms are not independent, which is the origin of D2)
