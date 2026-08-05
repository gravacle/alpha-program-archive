# STAGE 8 TASK 5 — REVIEW OF THE CHAIN CONFORMANCE AUDIT + THE CONVERGENCE ADJUDICATION — DARIO V001

Date: 2026-08-05
Lane: Dario (Claude Opus 5), cross-family reviewer and adjudicator of record
Task: PASTE 574 / Task 5
Under review: `STAGE8_TASK5_CHAIN_CONFORMANCE_AUDIT_LANE3_V001.md` (`d02576c8…`, verified, 1,452 lines)
Chain of record: `STAGE8_TASK5_LICENSED_CONDITIONAL_CHAIN_LANE2_V004.md` (`1da746c3…`, verified)

## Lead result

```text
REGISTER_HEAD = Q-499

AUDIT = DEFECTIVE (+2, one of them decisive and repairable in one line)
  D1 (S9-2)/(S10-1) MIX THE AMBIENT NORM WITH d^per. Both the threshold
     implication and its asserted converse are FALSE as displayed. I verified
     this with two counterexamples computed by hand. This reopens, on the very
     route the audit prescribes, the alternate-complete-metric attack that
     V004's MODULUS_COMPATIBILITY_CERT exists to close.
  D2 Step 6 is MISTYPED: RE-DERIVABLE_RECORD_FIRST where the audit's own (A0)
     makes it CONTINUUM_RESIDUAL. Its content IS the carrier commitment, and
     "carrier" is in (A0)'s trigger list and absent from RE-DERIVABLE's.
     The residue set is 3/6/9/12, not 3/9/12.
  +1 verb defect: lead line 21 asserts "is exact" unconditionally where the
     body conditions it on two undischarged certificates.

PERIOD_CANDIDATE = SOUND in its shape, DEFECTIVE in its modulus
  The multiplicative form, the case lattice, the two certs and the
  difference-quotient construction are right and are a genuine advance. The
  numerator is wrong. One-line fix.

CONVERGENCE = PARTIAL
  +GAIN, real: the trial becomes TWO-SIDED. chi^per enters multiplicatively,
   so chi^per = 0 lands at q^per = 0 INSIDE the lattice and returns a verdict
   -- curing the K3 one-sidedness. Conditional on D1's repair.
  +REMAINS: the K5 construction debt is NOT paid. It is relocated to Gamma,
   and on the displayed route Gamma = Loc^C o Ker factors through the very
   unbuilt map that is the debt. Both K5 limbs still fail.
  +E_C is neither typed nor evaded: conditionally INHERITED on the displayed
   route, evaded only on the route that is unbuilt.

REDERIVATION_PROGRAM = stated (+7 relays, +1 standing construction that is
  not relay-sized and must not be described as one)

VERB_AUDIT_SELF = CLEAN (+1 disclosed qualification of my own prior credit)

MEMBER_BOUND = false ; FIXED_POINT_EXECUTED = false ; END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = false (the audit's own stands; I add none)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-499 | verified |
| Audit `d02576c8…`, 1,452 lines | verified before reading |
| Chain V004 `1da746c3…` | verified |
| My 572 review `9c232579…` | verified |
| Output name absent before construction | verified — no clobber |

## 1. G1 — review of the audit

### 1.1 DEFECT 1 (decisive) — the modulus mixes two metrics

[PROVABLE] The audit's record-native contraction functional is

```text
q_loop,w^per := sup_(K!=K' in D_w^per)
                 |B_w^per(K) - B_w^per(K')| / d_w^per(K,K').     (S9-2)
```

**Ambient `|·|` in the numerator; `d^per` in the denominator.** Banach's theorem requires
`d^per(B(K),B(K')) <= q · d^per(K,K')`. The displayed quotient bounds a different thing, and the two
are incomparable — the displayed `q^per` is not invariant under rescaling `d^per`, while the true
`d^per`-modulus is.

[PROVABLE] I verified both failures by hand.

**The implication fails.** Take `D^per = R`, `d^per(K,K') = 2|K-K'|` — complete, inclusion into
`K_amb` continuous, so `CompleteMetricWitness^per` holds and (S4-3) is satisfied — and `B(K) = K+1`.
Then

```text
q^per = sup |K-K'| / (2|K-K'|) = 1/2 < 1,
but  d^per(B(K),B(K')) = 2|K-K'| = d^per(K,K').
```

`B` is a `d^per`-**isometry with no fixed point** (`K+1 = K` is unsatisfiable). So (S10-1) asserts
strict contraction, and (S11-1) would assert a unique fixed point, where none exists.

**The converse fails.** Take `D^per = [0,1]`, `d^per(K,K') = |K^2 - K'^2|` — the pullback of the
Euclidean metric along the injection `K |-> K^2`, hence a complete metric with continuous inclusion —
and `B(K) = K/2`. Then

```text
d^per(BK,BK') = |K^2-K'^2|/4 = d^per(K,K')/4      [a strict contraction, constant 1/4]
q^per = sup (|K-K'|/2) / (|K-K'|(K+K')) = sup 1/(2(K+K')) = infinity.
```

A genuine strict contraction is assigned `q^per = infinity`.

[PROVABLE] **This is exactly the attack V004 closed.** V004 installed `MODULUS_COMPATIBILITY_CERT`
as a separate falsifiable gate precisely against "a complete `d_w` metric that lacks (1) and (2)
[making] `sup|dot B_w|` disagree with the true `sup d_w` modulus (the alternate-complete-metric
attack)", and its `DIRECT_MODULUS` witness requires Step 9 to define `A_loop` by **`d_w`-difference
quotients directly**. The audit drops "`d_w`-difference" and reinstates the ambient numerator. And the
audit routes around its own gate: it states that if the factor certificates fail, "(S9-2) remains the
record-native object", and its board prescribes "use direct `q^per < 1`" — so on the direct branch
there is **no** modulus-compatibility gate at all.

[PROVABLE] **Scope.** This is STRUCTURAL, not a value claim. It touches no verdict label and not the
`LOCAL_SHADOW` determination. It invalidates the **repair the audit prescribes**. On the
`DIFF_TO_METRIC_per` branch the certified chart clause supplies the missing compatibility; the defect
bites on `DIRECT_MODULUS_per`. **The fix is one line:** read the numerators of (S5-1), (S9-2) and
(S9-5b) as `d^per`, or gate (S10-1) on `PERIOD_MODULUS_COMPAT_CERT` as well.

### 1.2 DEFECT 2 — Step 6 is mistyped, by the audit's own definitions

[PROVABLE] The audit's (A0):

```text
RE-DERIVABLE_RECORD_FIRST := the theorem schema survives, but its actual
  instantiated map, domain, bound, or threshold must be reissued ...
CONTINUUM_RESIDUAL := a missing record-to-continuum comparison or CARRIER
  prevents the claimed physical-number reading; the exact residue is named.
```

"Carrier" is in the residue trigger list and **absent** from the re-derivable list. Step 6 is typed
`RE-DERIVABLE_RECORD_FIRST`, yet its own text says the closure equation "is not an equation on the old
scalar Banach carrier. It **requires a changed or augmented carrier** and new metric/completeness
data. No such choice is made here." The audit's own lead carries `FIXED_POINT_CARRIER = UNDETERMINED`.

[PROVABLE] Step 6's content **is** the carrier commitment; there is no instantiated map to reissue on
the branch where no `D^per subset K_amb` exists, so the defining condition of RE-DERIVABLE is not met.
**Step 6 is a CONTINUUM_RESIDUAL.** The residue set is **3/6/9/12**, and the re-derivable set is
**4/5/10**. The board's downstream *prescription* for Step 6 is already right ("prove period-return
closure and the carrier seam"); only the type label is wrong.

### 1.3 Step 4, Step 10, and a claimed-conformal step — the typings that hold

[PROVABLE] **Step 4: verdict CORRECT.** I attacked it from the conformal side and failed. It violates
the record lessons directly — the object certified literally contains the local reader, and the
certificate carries a consumer scope but no stage/support/arrow-class index. The defect is not worse
than re-derivable: its clause list is carrier-agnostic and instantiable on any route carrier, with
`D^per subset K_amb` a single reissuable line. **One display gap:** the audit never names *which*
lesson Step 4 violates. It should.

[PROVABLE] **Step 10: verdict CORRECT on its subject.** The V004 threshold
`q_loop = |p_loc[Rhat_K]| A_loop` is genuinely `LOCAL_SHADOW` — exact only on its local scope — and
that is what makes Step 10 nonconformal. But (S10-1), Step 10's *replacement*, carries DEFECT 1.
So the diagnosis is right and the prescription is not yet.

[PROVABLE] **Claimed-conformal steps: no mistype found in the lenient direction.** Step 8's rank-one
factorization is the likeliest place to hide a locality or selection assumption; it survives — the
factorization is stated with its uniqueness condition (`Rhat_(Kcycle) != 0`) explicit and gated.
Steps 0/1/2/7/11 hold. The one-verdict rule is followed: no step carries two incompatible verdicts.

### 1.4 The period candidate — sound in shape

[PROVABLE] **The difference-quotient form is the right move.** It is a Lipschitz seminorm, not a
derivative — "without differentiability or a frozen period functional" — which is genuinely more
record-native than V004's derivative form, and the `sup` over a declared domain with a named
certificate is correctly typed. The `A_loop = infinity` case is carried in the extended reals and the
bookkeeping is consistent.

[PROVABLE] **`FIXED_PERIOD_FACTOR_CERT` is not circular.** `F` is defined at (S9-3) from `u^H` and
`Per^H`, both typed at Step 3, *before* the cert appears at (S9-5). `chi^per := F(Rhat_(Kcycle))` then
uses an already-typed `F`. I checked this specifically because the definition looked mutually
dependent; it is not. Two conjuncts of the cert are redundant (a fixed `F` trivially has
`partial_K F = 0`; the existential is satisfied by typing alone), which is harmless.

[PROVABLE] **The degenerate cells recompute correctly.** `A_loop^per = 0 -> q = 0`;
`chi^per = 0 and F fixed -> F(J^per(K)) = 0 pointwise -> q^per = 0`;
`0 < A_loop < inf and chi != 0 -> q = |chi| A_loop`; `A_loop = inf and chi != 0 -> q = inf`. And
(S10-4) is right that the old `(A_loop = inf, chi = 0)` cell does **not** transfer without the certs —
the motion term may be nonzero, or the derivative may fail to equal the `d^per` modulus. No cell is
missing. **The coefficient is global as claimed, and the audit correctly declines to assert equality
with V004's local coefficient anywhere downstream.**

[PROVABLE] **Scale-invariance is real but not distinguishing.** `Rhat -> t Rhat` sends
`a_loop -> a_loop/t` and `chi -> t chi`, leaving the product invariant. The identical algebra holds on
the *local* route. It should not be banked as a period-specific virtue.

## 2. G2 — the convergence adjudication

### 2.1 The gain is real: the trial becomes two-sided

[PROVABLE] In V004's Mx route, the coefficient extraction carries the seed pairing in a
**denominator**, so seed-failure sends the coefficient to infinity and the chain **exits** its
certified lattice — the threshold theorem opens "for finite `chi_K`". That is the one-sidedness I
recorded at K3: the escrowed computation could confirm the seed and not refute it.

[PROVABLE] In the period route, `chi^per := F(Rhat_(Kcycle))` enters **multiplicatively**. So
`chi^per = 0` lands at `q^per = 0 < 1` — strict contraction — a **licensed cell inside the lattice
that returns a verdict**. And the direct record-first trichotomy `q^per = 0 / 0 < q^per < 1 /
q^per >= 1` is total over the extended reals. **This genuinely cures the one-sidedness.**

[PROVABLE] **A qualification of my own credit, which I found by attacking it.** I first tested whether
the cure is certificate-dependent and concluded it is not, because the trichotomy is total. That
reasoning was incomplete: totality of a trichotomy on `q^per` is not the same as `q^per`
*characterising contraction*. Given DEFECT 1, the displayed `q^per` does **not** characterise
contraction on the `DIRECT_MODULUS_per` branch. **So the cure is conditional after all** — on the
`DIFF_TO_METRIC_per` branch's certified chart clause, or on DEFECT 1's one-line repair. The credit
stands; its scope narrows.

### 2.2 The debt is not paid

[PROVABLE] My K5 criterion: a deferral is lawful iff **(a)** the subject term is CONSTRUCTED and
**(b)** the loop PRODUCES rather than CONSUMES the quantity.

**(a) fails.** `q^per`'s definition requires `B^per`, hence `Per^H`, hence `Gamma`. The audit types
two routes and neither is inhabited:

```text
(S3-6)  O^resp --Ker--> D_N^Loc --Loc_N^C--> C_N^k,   Gamma = Loc^C o Ker
        "one prospective realization"; "unproved obligations"
(S3-7)  O^resp --Ker--> D_N^Loc --Xi_N--> Z_N^loop --Hol_(A_N)--> U(1)
        "the genuinely different connection-period route"
```

`Gamma`, `Per^H`, `u^H` and the period-domain certificate are, in the audit's own words, "named
missing objects, not silently assumed members." **And on the displayed route `Gamma` factors through
`Loc^C` — the very unbuilt map that is the K5 debt.** The debt is not paid; on (S3-6) it is not even
relocated, it is *inherited*. On (S3-7) it is relocated to `Xi_N` — which is precisely the A1
amendment candidate I named in my Loc review, still unauthored.

**(b) fails.** `q^per` is consumed as a threshold condition on `B^per`; the loop does not produce it.

[PROVABLE] **Therefore the period construction DOES NOT pay the construction debt.** What it does is
sharpen it: from "build the physical `Loc`" to a bounded, named list — `Gamma` (on a chosen route),
`Per^H`, `u^H`, the period-domain cert, and two factor/modulus certs. That is real progress of a
different kind than payment, and it should be recorded as such.

### 2.3 E_C: neither typed nor evaded

[PROVABLE] `Per^H(Y) := lambda_(P_H,N Gamma(Y))` applies the harmonic projector on `C_N^k`. My (K-1)
confinement — `[E_C,Delta^Hdg]=0 => [E_C,P_H]=0`, and with `ran(iota^H) subset ker(E_C)` this puts
the harmonic component in `im(P_H) intersect ker(E_C)` — was derived for composites **factoring
through `iota^H`**.

[PART-PROVABLE] So the precise statement, and I state it more carefully than I did in 572:

- On **(S3-6)**, where `Gamma = Loc^C o Ker` and `Loc^C = iota^H o Loc^phys`, the confinement
  **would** apply and `E_C,RL c_RL = 0` would remain necessary for a nonzero period. Since `Gamma` is
  unbuilt, this is **conditional inheritance**, not an established confinement.
- On **(S3-7)**, which lands in `U(1)` and never enters `C_N^k`, `E_C` is **evaded entirely** — but
  that route is unbuilt and needs `Xi_N`.

**The audit does not equivocate between the routes** — it states they "are alternatives; this audit
neither identifies nor adds them," and (S3-7) carries its own separate scalarization. I checked for
route-equivocation specifically and found none. But the consequence stands: **the period construction
neither types nor evades `E_C`**; it inherits the exposure conditionally on the route whose
realization is displayed.

### 2.4 Verdict

```text
CONVERGENCE = PARTIAL
  GAIN:    two-sidedness of the trial -- real, structural, conditional on D1's repair
  REMAINS: (a) subject term unconstructed (Gamma, on either route);
           (b) loop still consumes rather than produces;
           (c) E_C conditionally inherited on the displayed route;
           (d) the (S3-7) route that would cure (c) requires the unauthored Xi_N.
```

## 3. G3 — the re-derivation program

[YOURS] Dependency-ordered. **The critical ordering fact:** Step 10's period threshold depends on
`Gamma` (Step 3), so **Step 10 cannot be re-derived before Step 3's route is chosen.** Any program
that schedules 10 before 3 is mis-ordered.

| # | Relay | Delivers | Depends on |
|---|---|---|---|
| R1 | **Modulus repair** | re-issue (S5-1), (S9-2), (S9-5b) with `d^per` numerators, or gate (S10-1) on `PERIOD_MODULUS_COMPAT_CERT`; re-state (S10-1) and its converse | — (do this first; it is one line and everything downstream inherits it) |
| R2 | **Route commitment** | a principal-facing determination: (S3-6) vs (S3-7) for `Gamma`, with the price of each displayed — (S3-6) inherits the `Loc` debt and the `E_C` exposure; (S3-7) requires the `Xi_N` where-clause amendment | R1 |
| R3 | **Step-6 retype + carrier seam** | re-type Step 6 as `CONTINUUM_RESIDUAL`; state the carrier residue exactly and what carries it | R2 |
| R4 | **`FIXED_PERIOD_FACTOR_CERT`** | prove or type it; without it the product form and the factor lattice do not exist | R2 |
| R5 | **`PERIOD_MODULUS_COMPAT_CERT`** | prove or type it on both branches | R1, R4 |
| R6 | **Steps 4/5 re-issue** | reissue the return-object certificate and the boundedness bound on the global period observable | R2 |
| R7 | **Step 10 lattice transfer** | transfer the factor lattice under R4+R5; otherwise carry direct `q^per < 1` | R4, R5, R6 |
| R8 | **Residue treatment 3/6/9/12 + witness boundary** | state what is carried, what is named missing, and what the witness certification then certifies | all |

[PROVABLE] **Not relay-sized, and it must not be described as one:** the construction of `Gamma`
itself — on (S3-6) that *is* the physical `Loc` build, which three prior artifacts terminate at; on
(S3-7) it is the `Xi_N` amendment plus its full gate. This is the program's standing open object. R1–R8
are the bounded work around it; they do not substitute for it.

[PROVABLE] **What the witness certification would then certify, stated honestly.** After R1–R8 with
`Gamma` built: that the chain's steps are record-first conformal, that the period threshold is
well-posed on a certified domain, and that the contraction question returns a two-sided verdict. It
would **not** certify: that `A_RP^+` is inhabited, that the seed holds, that the membership theorem is
repaired (it is DEFECTIVE on D1/D2/D3/D6 independently), or that any number has been computed.

## 4. G4 — the A2 consequence

[YOURS] What the axiom text should freeze, given all of the above:

1. **The deferral criterion, with its anti-excuse clause** (mine, already in the draft queue): a
   condition may be carried as pre-fixed-point undetermined only if its subject term is
   **constructed** and the loop **produces** rather than consumes it; and an unbuilt map is never a
   pre-fixed-point undetermination. **This adjudication is the criterion's first live test, and the
   period route fails both limbs** — which is evidence the criterion has teeth rather than being
   decoration.
2. **The one-sided-trial rider, with its period cure conditioned.** A2 must record that a threshold
   whose coefficient sits in a denominator yields a trial that can confirm and not refute; that the
   period form cures this by making the coefficient multiplicative; and that **the cure requires the
   modulus to be the `d^per`-modulus** (DEFECT 1). Freezing the cure without that condition would
   freeze a false comfort.
3. **The period threshold's standing: CARRIED-CONDITIONAL, not adopted-for-certification.** It is not
   yet adoptable: its modulus is mis-stated, its two certs are unproved, and its `Gamma` is unbuilt on
   both routes. A2 should carry it as the named replacement candidate with its gate list displayed —
   the same idiom A6 used for the post-scope condition.
4. **The residue ledger corrected to 3/6/9/12**, with the carrier obligation booked at Step 6 rather
   than silently inherited from Step 3.

## 5. G5 — fresh attack, and verb audit

[PROVABLE] **My attack was the lattice-totality attack, aimed at my own conclusion** rather than the
audit's — the honest target, since I was the one who credited the cure. Result: the trichotomy is
indeed total without the certs, so my first reasoning survived on its own terms; but the attack
surfaced the deeper question the reasoning never asked — whether `q^per` characterises contraction at
all — and that is where DEFECT 1 lives. **The attack found a defect in the audit by way of finding an
incompleteness in me.** Recorded in §2.1.

[PROVABLE] **Route-equivocation attack: the audit SURVIVES.** (S3-7) lands in `U(1)`, is not a
realization of `Gamma`, carries its own separate map and scalarization, and the audit states the two
routes "are alternatives; this audit neither identifies nor adds them." No benefits are claimed for
one route from the other's properties.

[PROVABLE] **Cert-circularity attack: the audit SURVIVES.** `F` is typed before the cert that fixes it.

[PROVABLE] **Verb audit on the audit's §5.5.** `VERB_AUDIT_SELF = CLEAN` overstates. Lead line 21
asserts `q_loop = |p_loc[Rhat_K]| A_loop` **"is exact"** for the declared local reader; the body
conditions the same identity on V004's `MODULUS_COMPATIBILITY_CERT` **and** a separate
zero-times-infinity rule, neither of which is discharged — V004's only board status for that cert is
`ADDED`. And §5.5 audits the twelve step rows without enumerating the lead block, so `CLEAN` reads as
covering what it never examined. Correct board line: `CLEAN_EXCEPT(lead line 21; lead-block coverage)`.

### Verb audit on my own board

| My line | Strongest verb my sources carry | Honest? |
|---|---|---|
| `AUDIT = DEFECTIVE (+2)` | (S9-2) read directly; two counterexamples computed by hand; (A0) vs Step 6's own text | **CLEAN** |
| `PERIOD_CANDIDATE = SOUND in shape, DEFECTIVE in modulus` | cells recomputed; cert non-circularity traced; numerator read | **CLEAN** — I separate the shape from the defect rather than condemning both |
| `CONVERGENCE = PARTIAL` | K5 criterion applied to both limbs; (S3-6)/(S3-7) read | **CLEAN** |
| E_C "conditionally inherited" | (K-1) derived only for composites factoring through `iota^H`; `Gamma` unbuilt | **CLEAN** — weaker and more accurate than my 572 phrasing would have licensed here |
| `REDERIVATION_PROGRAM = 7 relays` | audit's own repair statements per step | **CLEAN** — and I refuse to size the `Gamma` construction as a relay |

[PROVABLE] **One disclosed qualification of my own prior credit** (§2.1): I credited the period route
with a cert-independent cure of the one-sidedness. The credit stands, but its scope is narrower than I
stated — the cure requires the modulus to be the `d^per`-modulus, which DEFECT 1 shows the displayed
form is not on the direct branch. Found by attacking my own conclusion; recorded rather than quietly
narrowed.

```text
VERB_AUDIT_SELF = CLEAN (+1 disclosed qualification of my own prior credit)
```

## 6. Fence and stopping board

```text
THRESHOLD_V004 = LOCAL_SHADOW (audit's determination CONFIRMED)
(S9-2)/(S10-1) = INVALID AS DISPLAYED (+ambient numerator over d^per denominator;
  +both the implication and its converse fail; +one-line repair available)
STEP_6 = MISTYPED (CONTINUUM_RESIDUAL by (A0)); residue set = 3/6/9/12
PERIOD_FORM = the right shape; chi^per multiplicative; lattice cells recompute
GAMMA = UNBUILT ON BOTH ROUTES (Loc^C unbuilt; Xi_N unauthored)
CONVERGENCE = PARTIAL (two-sidedness gained; construction debt unpaid)
SEED = still a condition; MEMBERSHIP = still DEFECTIVE on independent grounds
MACHINERY_APPEAL = false
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

No register, plan, tracker, git, commit, push, member-binding, fixed-point, end-test, or evaluation
action was performed by this lane. No law was adopted.

AUDIT = DEFECTIVE (+D1 decisive: (S9-2)/(S10-1) put the ambient norm over the `d^per` metric, so the
threshold implication and its asserted converse are both false — verified by two hand-computed
counterexamples, a `d^per`-isometry with `q^per = 1/2` and no fixed point, and a genuine `d^per`-quarter-
contraction with `q^per = infinity`; this reopens the alternate-complete-metric attack V004's
MODULUS_COMPATIBILITY_CERT exists to close, and the audit's direct branch carries no such gate;
repairable in one line by reading the numerators as `d^per`; +D2: Step 6 is typed RE-DERIVABLE where
the audit's own (A0) makes a missing carrier a CONTINUUM_RESIDUAL and Step 6's own text says it
"requires a changed or augmented carrier" — the residue set is 3/6/9/12; +1 verb defect at lead
line 21; the per-step typings otherwise hold, Step 4's verdict survives attack from the conformal
side, and no step is mistyped in the lenient direction)
PERIOD_CANDIDATE = SOUND in shape, DEFECTIVE in modulus (+the difference-quotient form is genuinely
more record-native than the derivative form; +FIXED_PERIOD_FACTOR_CERT is not circular — `F` is typed
before the cert that fixes it; +every cell of the case lattice recomputes correctly and (S10-4)'s
non-transfer is right; +the coefficient is global and no equality with V004's local coefficient is
assumed downstream; +but the modulus carries D1, and scale-invariance should not be banked as a
period-specific virtue since the local route has it too)
CONVERGENCE = PARTIAL (+GAIN, real: `chi^per` enters multiplicatively, so `chi^per = 0` lands at
`q^per = 0` inside the lattice and returns a verdict — the K3 one-sidedness is cured, conditional on
D1's repair; +REMAINS: the K5 debt is NOT paid — `Gamma` is unbuilt on both routes and on the displayed
route `Gamma = Loc^C o Ker` factors through the very map that is the debt, so limb (a) fails, and
`q^per` is still consumed as a threshold so limb (b) fails; +E_C is neither typed nor evaded but
CONDITIONALLY INHERITED on the displayed route, since (K-1) was derived for composites factoring
through `iota^H` and `Gamma` is unbuilt — evaded only on (S3-7), which needs the unauthored `Xi_N`;
+what the period route genuinely achieves is sharpening the debt from "build the physical Loc" to a
bounded named list, which is progress of a different kind than payment)
REDERIVATION_PROGRAM = stated (+7 relays, in dependency order: R1 modulus repair first since
everything inherits it; R2 route commitment for `Gamma`, principal-facing; R3 Step-6 retype and
carrier seam; R4 FIXED_PERIOD_FACTOR_CERT; R5 PERIOD_MODULUS_COMPAT_CERT; R6 Steps 4/5 re-issue;
R7 Step 10 lattice transfer; R8 residue treatment 3/6/9/12 and the witness boundary; +the critical
ordering fact is that Step 10 depends on `Gamma`, so 10 cannot precede 3's route choice; +the `Gamma`
construction itself is NOT relay-sized and must not be described as one — it is the program's standing
open object)
VERB_AUDIT_SELF = CLEAN (+1 disclosed qualification of my own prior credit: the two-sidedness cure is
conditional on the modulus being the `d^per`-modulus, which D1 shows the displayed form is not on the
direct branch — found by attacking my own conclusion rather than the audit's)
