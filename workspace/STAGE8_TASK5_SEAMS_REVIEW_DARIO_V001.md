# STAGE 8 TASK 5 — REVIEW OF THE COMMON SEAMS — DARIO V001

Date: 2026-08-05
Lane: Dario (Claude Opus 5), cross-family reviewer of record
Task: PASTE 584 / Task 5
Under review: `STAGE8_TASK5_COMMON_SEAMS_LANE3_V001.md` (`5de94e16…`, verified, 1,592 lines)

**This build implements my own 580 findings.** That is exactly the artifact I am least able to see
clearly, so I have been harder on it than on a build I had no stake in — and the decisive finding
below is against the consumption of my own diagnosis.

## Lead result

```text
REGISTER_HEAD = Q-510

SEAMS = DEFECTIVE (+3, one DECISIVE)
  THE CONSTRUCTION S1 IS SOUND. I re-derived (O11)-(O17) myself: the orbit
  quotient chooses no address, ev^or is address-INDEPENDENT into R_or,[a],
  mu_T(b^-) = -mu_T(b) is derived not asserted, well-definedness checks, and
  the most likely hiding place (1_Kamb) is clean -- r_T is left free and
  "r = 1 claimed as forced" is an explicit void.

  D1 [DECISIVE] (R9) IS NOT A FALSIFIER. It is a THEOREM THAT BOTH ROUTE
     RETURNS VANISH. Quantifying universally over Triv_[a] forces
     2 mu_T(b) p 1_Kamb = 0, hence p = 0 on every commonly-formed cell.
     The relay-580 no-go that S1 correctly defeated AT THE SCALAR SEAM is
     reinstated one level up AT THE IDENTIFICATION SEAM.
  D2 The modulus is FAMILY-DEPENDENT and the board does not say so; its
     interaction with A7's carriage condition is undisplayed and SPLITS BY
     BRANCH (my derivation, §1.3).
  D3 S2's remaining package double-counts what its automatic half discharged;
     both route boards omit the carrier and modulus-certificate rows.

PARITY_DISCHARGE = PARTIAL (+HOL's log-branch oddness and Ker address-oddness
  remain; S1 types only the carrier half of HOL's address covariance)
F3_COLLAPSE = CONFIRMED
CONSOLIDATED_BOARD = stated
VERB_AUDIT_SELF = CLEAN (+2: a refinement of my own parity rule; +one place
  the build is HARDER than my own 580 phrasing deserved)

MEMBER_BOUND = false ; FIXED_POINT_EXECUTED = false ; END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = false
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-510 | verified |
| Build `5de94e16…`, 1,592 lines | verified before reading |
| My 580 review `61d41a3e…`; my Ξ_N V002 `7958b54d…`; audit V002 `44202c06…`; A8 | verified |
| Output name absent before construction | verified — no clobber |

## 1. P1 — the orientation family

### 1.1 The construction is sound, and I re-derived it

[PROVABLE] Verified personally, not taken on report:

```text
(O11) R_or,[a] := (R x [a])/~ ,  (q,a^-) ~ (-q,a).   No address chosen.
(O13) ev_(b^-)^or(lambda) = iota_(b^-)(-lambda(c_b)) = iota_b(lambda(c_b))
      = ev_b^or(lambda).        ev^or is ADDRESS-INDEPENDENT into R_or,[a];
                                the sign-oddness is absorbed into the carrier.
(O16) mu_T(b^-) 1 = T(iota_(b^-)(1)) = T(iota_b(-1)) = -T(iota_b(1))
      = -mu_T(b) 1.             My 580 law, now CARRIED per orbit.
(O17) T_(r,sigma)(iota_b(q)) := r sigma(b) q 1_Kamb, well defined because
      r sigma(b^-)(-q) = r(-sigma(b))(-q) = r sigma(b) q.
```

**This respects the 580 no-go rather than evading it.** My no-go was that an *address-independent*
seam forces `mu == 0`; S1 claims no address-independent map, it carries a family each member of which
is address-sensitive. That is the correct resolution and I confirm it.

[PROVABLE] **No hidden representative.** I hunted the likeliest hiding places and the build is clean:
`1_Kamb` enters only as a reference for *defining* the coefficient, `r_T := |mu_T(b)|` is left free in
`R_(>0)`, void 2 explicitly forbids "`r=1` claimed as forced without a normalization premise", and the
text states "metric positivity and the unit rule do not force `r=1`". `Sigma_[a]`'s two members carry
no canonical `+` label. The presentation `(O11)` privileges no address. **PASS.**

[PROVABLE] One refinement worth recording: `r_T` is address-independent (`|mu_T(b^-)| = |mu_T(b)|`)
but `1_Kamb`-dependent — rescaling the reference rescales every `r_T`. So there is **no canonical
`r = 1` member**, and any per-member statement must be made against a declared reference or in the
basis-free ratio form `q_T/q_{T'} = r_T/r_{T'}`.

[PROVABLE] **FC4 on target-only new cycles: PASS.** Giving a target-only new cycle its own orientation
orbit is a purely target-side datum; the build installs "no upward sign or scale lift" explicitly, and
the covariance transports `r_{f_*T} = r_T` without creating an upward map. No invented upward quotient.

### 1.2 D1 (DECISIVE) — (R9) annihilates instead of falsifying

[PROVABLE] `(R9)` quantifies **universally over both families**, and the build defends the reading in
words: "Carrying `T_H` and `S_Hol` universally does not bind either member; it retains the two families
and exposes every jointly formed candidate pair to the law."

[PROVABLE] **That quantification is fatal.** Write `p := (Per_(a,eps,K)^H(Y))(c_b)`, so that by
`(O12)`,`(O17)`,`(O18)`,`(R2a)` the H return is `B^H_T(Y) = mu_T(b) p 1_Kamb`. Fix any `S_Hol`; the
right-hand side of `(R9)` is then independent of `T_H`. Take `T, T'` with the same `r` and opposite
`sigma` — distinct members, since `Sigma_[a]` has two. Then `mu_{T'}(b) = -mu_T(b)` by `(O16)`, and
`(R9)` applied to each gives

```text
mu_T(b) p 1_Kamb = B^Hol_S(Y) = mu_(T')(b) p 1_Kamb = -mu_T(b) p 1_Kamb
=> 2 mu_T(b) p 1_Kamb = 0.
```

`mu_T(b) != 0` because `T in Iso_R(R_or,[a], K_amb)` by `(O14)`, and `1_Kamb != 0`. Therefore

```text
p = 0  =>  B^H_T(Y) = 0 for every T,  and  B^Hol_S(Y) = 0 for every S,
on EVERY commonly-formed cell.
```

The scale half gives it independently: `r = 1` against `r = 2` with the same `sigma` yields
`(2-1) mu p 1_Kamb = 0`.

[PROVABLE] **So `(R9)` is not the identification falsifier — it is an annihilator.** A8's law reads
"wherever both routes are formed, their periods MUST agree; a displayed disagreement … voids the
disagreeing construction(s)." A8 says nothing about quantifying over scalarization members. **The
universal-universal form is the build's own rendering, and it makes A8 degenerate — with or without
`Ξ_N`.**

[PROVABLE] **This is my 580 no-go reinstated one level up.** S1 correctly defeated
"address-independent ⟹ `mu == 0`" at the scalar seam by carrying the family. `(R9)` then demands one
equation across the whole carried family — which is address-independence in a new place, and it
forces the *return* to zero instead of the coefficient. **The pathology moved; it was not removed.**

[YOURS] **The repair is derivable and is the build's own third option.** Replace the
universal-universal equation by either

1. a family of equations under a declared, **output-independent** correspondence
   `Phi : Triv_[a] -> Scal^Hol`, i.e. `B^H_T = B^Hol_(Phi(T))` for every `T`; or
2. equality of the two families' **invariant quotients** — equality of the induced maps modulo the
   `R^x`-action, or equality of period *ratios* across two cells, in which `r` and `sigma` cancel.

Both instance the build's own line "a consumer must … prove a sign/scale-invariant quotient"; neither
is the forbidden output-dependent "agreement-filtered `Match`". **Until `(R9)` is repaired, the ruling
should not weigh the argument that "without `Ξ_N`, A8 goes vacuous" — `(R9)` as drafted makes A8
degenerate either way.**

[PROVABLE] **The drafting question the lane must answer and I cannot:** does A8's "their periods" mean
one scalar per route, or the `T`-indexed family the build just constructed? **A8's text does not
decide it**, and the answer changes `(R9)`'s correct form.

### 1.3 D2 — the modulus is family-dependent, and A7 carriage splits by branch

[PROVABLE] `T` is **post-composed** onto the route composite, never conjugated with it: `(R2a)` puts
`T` only in `u^r`, and the domain point `K` enters upstream of `T` and never passes through it. So the
`(M2)` numerator carries `T` and the denominator does not. With a positively homogeneous carrier
metric — which both of the audit's own certified regressions are — this gives `q_T = h(r_T) q_1` with
`h` strictly increasing. **The modulus is family-dependent.**

[PART-PROVABLE] The exact law needs the metric's homogeneity degree, which is not sealed; the
**metric-free core** does not: `T` enters only through `(r_T, sigma_T)`, the domain is `T`-free, and no
conjugation is available, so `q` cannot be `T`-invariant in general. `sigma` drops out (`|sigma| = 1`);
it is the scale that survives.

[PROVABLE] **The build handles this correctly at the consumer layer** — `B` is explicitly `T`-indexed,
"a single unindexed scalar `B^H` is not licensed", the three lawful consumer options are named, and
collapsing the family without a proved invariant is a void.

[PROVABLE] **But the interaction with A7 is undisplayed, and it splits by branch.** A7's falsifier is
that "a branch whose period computation exits its certified lattice voids that branch's carriage."
With `q_T = h(r_T) q_1`:

```text
epsilon = 1 (IDENTITY): (H4)/(HOL2a) force q_1 = 0, so q_T = 0 for EVERY T.
   Carriage is FAMILY-INVARIANT; two-sidedness survives family-wide.
epsilon = 0 (ZERO): if q_1 != 0, then since r_T ranges over all of R_(>0)
   there are members with q_T < 1 and members with q_T >= 1.
   Carriage is FAMILY-DEPENDENT and A7's falsifier is not evaluable
   without a quotient or a carry-all-T convention.
```

**A7's carriage condition is well defined on one branch and not on the other.** The build's board
mentions A7 only in the HOL certificate list and does not follow S1 into the modulus layer at all —
verified: no occurrence of `q_loop`, `q^per`, `D^per`, or the modulus certificates anywhere in 1,592
lines. **That is a consequence-board gap, not a construction defect.**

### 1.4 P1(c) — the parity rule's reach: PARTIAL

[PROVABLE] S1's H-side address covariance consumes **two** ingredients: the carrier quotient
(`iota_(b^-) = iota_b o (-id)`) **and** the sealed fact `c_(a^-) = -c_a`. The two odd signs cancel.

[PROVABLE] **On HOL there is no exhibited analogue of the second.** The address enters through
`Ker_(a,K)`, which the build's own board records as uninhabited, and nothing sealed makes `Ker` odd in
the address. Further, transposing the argument needs `log_b^S(g^(-1)) = -log_b^S(g)`, which requires
`U_b^S` closed under inversion and the branch odd — the build types neither. **So S1 supplies the
carrier half of HOL's address covariance and leaves the log-branch-oddness half open.**

[PROVABLE] **A refinement of my own parity rule, which I accept.** My 583 rule was that "any *rule*
discharging `U^H` must also discharge `U^Hol`". S1 is not a rule — it is a *construction* consuming an
H-side sealed fact. The parity rule therefore does not transport it, and correctly so: **it constrains
cheap rules, not constructions.** I record the clarification rather than letting the rule be read too
broadly.

[PROVABLE] Independently worth doing: retyping the HOL seam's source from bare `R` to a HOL
orientation line. My 580 no-go **does** apply to the naked `R`. That discharges the *typing*, not the
covariance.

## 2. P2 and P3

### 2.1 The corestriction — PARTIAL, and one correction to me

[PROVABLE] **The automatic half is automatic algebraically**, exactly as my 580 finding said:
`ker(qtilde_N) subset ker(Kraw_N)` needs nothing but linearity. **PASS.**

[PROVABLE] **But the build is HARDER than my 580 phrasing deserved, and it is right to be.** I asserted
flatly that "`Q_N` is the corestriction of the R5 realization, so any map on `O_R5` descends". The
build shows the step to `Rel_N = closure(ker qtilde_N)` needs more than linearity, and it flags its own
`kappa_N` topology-agreement as unproved: "Giving `I_N^q` the quotient topology makes `beta_N` a
topological isomorphism by definition; it does not prove that the identity `kappa_N` is continuous or
that the quotient and inherited topologies agree." **My phrasing was too flat and the build corrected
it. Recorded.**

[PROVABLE] **D3(a): the remaining package double-counts.** `Sbar_N` is constructed, then re-listed as
an uninhabited `ExtSrc` member and re-typed; its naturality square is charged twice. The remaining
obligation should be stated net of what the automatic half discharged.

### 2.2 The F3 partial — CONFIRMED

[PROVABLE] **The honesty holds.** The build keeps the statement-versus-proof distinction throughout —
the very distinction I had to correct in myself at 580 — and does not upgrade any declaration.

[PROVABLE] **The collapse is real.** I tested whether anything stays independent: `j_f^Sym` and
`rho_a^Sym` are typed components of the sealed `L_F2` realization tuple, and `S24`/`S25`/`S25b` are
`L_F2` **membership clauses** — so an inhabited J-II realization member discharges them by
construction, not by a further proof. **F3's remainder collapses into the J-II realization-family
inhabitance. CONFIRMED.**

[PROVABLE] One inconsistency, running *opposite* to the direction a reviewer would expect: the build's
own `MACHINERY-APPEAL(S3)` **over-lists** the S3 debt relative to its own board — items 2 and 3 are
subsumed by item 1 once item 1 is discharged. The build charges itself too much, not too little.

## 3. P4 — the consolidated board

[PROVABLE] **Both route lists are accurate but incomplete, symmetrically.** Both omit the Step-6
carrier package `(C6-1)` and the Step-9/10 modulus certificates (`FIXED_PERIOD_FACTOR_CERT`, `(M5)`)
that the audit's own route board `(RB1)` owes on **both** routes. The omission is symmetric, so it does
not move the H/HOL balance — but it is precisely the layer where D2's family-dependence bites.

[PROVABLE] **What the identification falsifier can bite on today: NOTHING.** Both routes are gated by
the same uninhabited `ExtSrc`/`Ker_(a,K)` — a **single common blocker** — so no differential formation
of one route without the other is available. And when A8 eventually can bite, it will bite on only half
the branch space: on `epsilon = 1`, `(H4)` and `(HOL2a)` force both returns to `0` for every member, so
A8 could there only ever confirm `0 = 0`. **A8's entire discriminating power lives on `epsilon = 0`.**

[PROVABLE] **The 580 asymmetry, re-examined honestly.** It **weakens in pricing** but does not reverse:
the shared `ExtSrc`/`Ker` precondition means the two routes are closer in absolute distance than the
raw core-count suggests. What does *not* change is the kind of the remaining core — H's is a
construction, HOL's a declaration — and the width of HOL's declaration is if anything *understated*:
deriving `Ξ_N` instead of authoring it would have to cross both a continuum-to-record and a
real-to-integral boundary, and A1's "no declarations remain anywhere in Task 5" stands as a real
standing presumption `Ξ_N` must overcome.

[YOURS] **What the Ξ_N ruling should now weigh:**

1. **`(R9)` first.** Until it is repaired, the "without `Ξ_N`, A8 goes vacuous" argument is unavailable
   — `(R9)` as drafted makes A8 degenerate either way. This is the single highest-value repair on the
   board and it is derivable, not a judgement call.
2. **The common blocker.** Neither route can be formed without `ExtSrc`/`Ker`. A ruling that funds one
   route does not unblock it any sooner than the other.
3. **The branch asymmetry.** A8's discriminating power is `epsilon = 0`-only; on `epsilon = 1` both
   routes are forced to zero and the falsifier is blind.
4. **Construction versus declaration**, unchanged as the qualitative difference — with HOL's
   declaration wider than previously priced.

## 4. P5 — fresh attack, and verb audit

[PROVABLE] **My fresh attack was the scale question**, aimed at a build implementing my own finding.
It was **anticipated and correctly handled at the consumer layer** — and pursuing it is what surfaced
D1, because the same universal-quantification move that is harmless at the `B`-index layer is fatal at
the `(R9)` layer. **The attack found the decisive defect by way of being answered.**

### Verb audit on my own board

| My line | Strongest verb my sources carry | Honest? |
|---|---|---|
| S1 construction sound | (O11)–(O17) re-derived by me, including the hiding-place check | **CLEAN** |
| `D1 (R9) annihilates` | (R9)'s own universal quantifier; elementary algebra I verified | **CLEAN** — and it is a defect in the consumption of *my own* diagnosis |
| `D2` family-dependence | metric-free core derived; the exact law flagged as homogeneity-dependent | **CLEAN** — I state the caveat rather than the stronger claim |
| A7 branch split | `(H4)`/`(HOL2a)` for `eps=1`; `r_T` unbounded for `eps=0` | **CLEAN** |
| `PARITY = PARTIAL` | S1's two ingredients; HOL's missing analogue | **CLEAN** |
| `F3_COLLAPSE = CONFIRMED` | `S24`/`S25`/`S25b` as `L_F2` membership clauses | **CLEAN** — I tested for an independent remainder and found none |
| `A8 can bite on nothing today` | the single common blocker; the `eps=1` blindness | **CLEAN** |

[PROVABLE] **Two disclosed items against my own record:**

1. **My parity rule needed a refinement** (§1.4): it constrains *rules*, not *constructions*. S1 does
   not violate it, and reading it broadly would have wrongly deleted a genuine HOL obligation.
2. **My 580 corestriction phrasing was too flat** (§2.1): I said descent follows because `Q_N` is a
   corestriction; the build correctly shows the closure step needs more, and flags its own topology
   agreement as unproved. **The build was harder on my finding than I was, and it was right.**

```text
VERB_AUDIT_SELF = CLEAN (+2 disclosed items, both against my own record)
```

## 5. Fence and stopping board

```text
S1 CONSTRUCTION = SOUND (no hidden representative; FC4 respected; family carried)
(R9) = ANNIHILATOR, not falsifier -- DECISIVE, repair derivable
MODULUS = family-dependent; A7 carriage well defined on eps=1, not on eps=0
S2 = automatic half confirmed; remaining package double-counts
S3 = collapse CONFIRMED into J-II inhabitance; appeal over-lists
BOARDS = symmetric omission of carrier and modulus-certificate rows
A8 TODAY = can bite on nothing; both routes gated by one common blocker
ROUTE_CHOSEN = none ; E_C_BRANCH_CHOSEN = none ; all authority preserved
MACHINERY_APPEAL = false
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

No register, plan, tracker, git, commit, push, member-binding, fixed-point, end-test, or evaluation
action was performed by this lane. No law was adopted and no route was chosen.

SEAMS = DEFECTIVE (+D1 DECISIVE: `(R9)` quantifies universally over `Triv_[a]`, so taking two members
with the same `r` and opposite `sigma` gives `2 mu_T(b) p 1_Kamb = 0` with `mu_T(b) != 0` and
`1_Kamb != 0`, forcing `p = 0` — both route returns vanish on every commonly-formed cell, so `(R9)` is
an annihilator rather than a falsifier, and my own relay-580 no-go is reinstated one level up at the
identification seam; the repair is derivable and is the build's own third option, either a declared
output-independent correspondence `Phi : Triv_[a] -> Scal^Hol` or equality of the families' invariant
quotients; +D2: the modulus is family-dependent because `T` is post-composed and never conjugated, and
its interaction with A7's carriage condition is undisplayed and splits by branch — family-invariant on
`epsilon = 1` where `q_1 = 0`, family-DEPENDENT on `epsilon = 0` where `r_T` ranges over all of
`R_(>0)`; +D3: S2's remaining package double-counts what its automatic half discharged, and both route
boards symmetrically omit the carrier and modulus-certificate rows; the S1 CONSTRUCTION ITSELF IS
SOUND and I re-derived it, including the `1_Kamb` hiding-place check and FC4 on target-only new cycles)
PARITY_DISCHARGE = PARTIAL (+S1's H-side covariance consumes two ingredients — the carrier quotient and
the sealed `c_(a^-) = -c_a` — and HOL has no exhibited analogue of the second: `Ker_(a,K)` is
uninhabited and nothing makes it odd in the address, while transposing needs `log_b^S(g^(-1)) =
-log_b^S(g)`, requiring `U_b^S` inversion-closed and the branch odd, neither typed; +so S1 types the
CARRIER half of HOL's address covariance and the log-branch-oddness half remains; +my own 583 parity
rule refined: it constrains RULES, not CONSTRUCTIONS, so S1 does not trigger it)
F3_COLLAPSE = CONFIRMED (+`j_f^Sym` and `rho_a^Sym` are typed components of the sealed `L_F2`
realization tuple and `S24`/`S25`/`S25b` are `L_F2` membership clauses, so an inhabited J-II member
discharges them by construction; I tested each candidate remainder — composition/induction,
common-refinement legs, cycle-creating old-image scope — and found no independent remainder; +the
build's own `MACHINERY-APPEAL(S3)` over-lists its debt, charging itself too much rather than too little)
CONSOLIDATED_BOARD = stated (+both route lists accurate but symmetrically incomplete, omitting the
`(C6-1)` carrier package and the `FIXED_PERIOD_FACTOR_CERT`/`(M5)` rows the audit's own `(RB1)` owes on
both; +THE IDENTIFICATION FALSIFIER CAN BITE ON NOTHING TODAY — both routes are gated by the same
uninhabited `ExtSrc`/`Ker_(a,K)`, a single common blocker, and when it can bite it will bite only on
`epsilon = 0`, since `epsilon = 1` forces both returns to zero for every member; +the 580 asymmetry
weakens in pricing through the shared precondition but does not reverse in kind, and HOL's declaration
is wider than previously priced, having to cross both a continuum-to-record and a real-to-integral
boundary against A1's standing "no declarations remain")
VERB_AUDIT_SELF = CLEAN (+2 disclosed items, both against my own record: my parity rule needed
narrowing to rules rather than constructions, and my 580 corestriction phrasing was too flat — the
build was harder on my own finding than I was, and it was right)
