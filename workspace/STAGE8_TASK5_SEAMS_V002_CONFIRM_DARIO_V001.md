# STAGE 8 TASK 5 — CONFIRMATION OF SEAMS V002 (BOUNDED) — DARIO V001

Date: 2026-08-05
Lane: Dario (Claude Opus 5), cross-family reviewer of record
Task: PASTE 589 / Task 5 — bounded confirmation
Under review: `STAGE8_TASK5_COMMON_SEAMS_LANE3_V002.md` (`2525096b…`, verified, 892 lines)
Standard: my own 584 `(R9)` degeneracy computation (`7a0cb7ad…`, verified).

## Lead result

```text
REGISTER_HEAD = Q-514

SEAMS_V002 = CONFIRMED
NEW_DEGENERACY = none (+the address-covariance loophole hunted and shown not to
  fire -- and it turns CONSTRUCTIVE: see C3)
VERB_AUDIT_SELF = CLEAN

MY OWN DEGENERACY IS REPAIRED, and the repair is the right one. The two-member
computation rerun against R9-V002 yields the FULL DIAGONAL {(p,p)}, not the
singleton {(0,0)}. The diagnosis of my old attack is exact: it "froze the HOL
return while reversing only T_H"; the common-member form removes the
independent quantifier that made that possible.

MEMBER_BOUND = false ; FIXED_POINT_EXECUTED = false ; END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = false
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-514 | verified |
| Build `2525096b…`, 892 lines | verified before reading |
| My 584 review `7a0cb7ad…` | verified |
| Output name absent before construction | verified — no clobber |

## 1. C1 — my two-member computation, rerun

### 1.1 The carrier construction, re-derived

[PROVABLE] I verified the orbit carrier myself rather than reading it. With `g_(T,T') := T o T'^(-1)`:

```text
cocycle:      g_(T'',T') o g_(T',T) = T'' T'^(-1) T' T^(-1) = T'' T^(-1) = g_(T'',T)
reflexive:    g_(T,T) = id
symmetric:    x' = g_(T',T)x => x = g_(T,T')x'
transitive:   x'' = g_(T'',T')x' => x'' = g_(T'',T)x
psi well-def: T'^(-1)(x') = T'^(-1)(g_(T',T)x) = T'^(-1)(T' T^(-1) x) = T^(-1)(x)
inverse:      psi([T,T(z)]) = z  and  [T,T(psi([T,x]))] = [T,x]
rep-free:     [T',T'(z)] = [T', g_(T',T)T(z)] = [T,T(z)]
=> Kbar_[a] isomorphic_to R_or,[a].
```

**All correct.** The quotient removes the choice of trivialization representative and, as the build
states, "does not quotient away a sign or magnitude" — which matters, because quotienting the sign
would have been a second way to reach my degeneracy.

### 1.2 My computation, rerun — it no longer forces p = 0

[PROVABLE] With `T^- := (-id) o T` so `mu_(T^-)(a) = -mu_T(a)`, and both returns carried at the
**same** representative:

```text
at T   :   mu_T(a) ( p_H(c) - p_Hol(c) ) 1_Kamb = 0
at T^- : - mu_T(a) ( p_H(c) - p_Hol(c) ) 1_Kamb = 0
```

Since `mu_T(a) != 0` and `1_Kamb != 0`, **both lines impose the identical condition**
`p_H(c) = p_Hol(c)`, whose solution set is the full diagonal `{(p,p) : p in R}` — **not** `{(0,0)}`.

[PROVABLE] **The reason my old attack worked and no longer does.** V001's `(R9)` carried *independent*
quantifiers over `Triv_[a]` and `Scal^Hol`, so I could reverse `T_H` while holding `S_Hol` frozen and
obtain `x = -x`. R9-V002 compares the two **orbit sections** `Bbar^H(c), Bbar^Hol(c) in Kbar_[a]`,
which are representative-independent; changing the representative transports **both sides together**
by `g_(T',T)`. There is no configuration in which one side reverses and the other does not.

[PROVABLE] **The positive-scale arm is likewise clean:** `B_(T_s) = s B_(T)` on both routes, so
equality at `T` gives equality at `T_s`. No normalization `r_T = 1` is introduced anywhere.

### 1.3 Does it quantify over exactly what A8 names? — YES

[PROVABLE] R9-V002's only quantifier ranges over common physical cells on which both typed
period-return constructions are formed. **No independent quantifier over `Triv_[a]`, `Scal^Hol`, or
their Cartesian product survives.** Checked against A8's text element by element: A8 names both routes
being formed, one commonly formed cell, agreement of their period returns, a displayed disagreement as
first-order, voiding the disagreeing construction(s) pending adjudication, and no assumed
identification. **A8 names no scalarization-family quantifier, no Cartesian product, no normalization,
and no output-dependent matching relation — and R9-V002 adds none.**

[PROVABLE] The build is also honest about the current status: `ScalOrb^Hol` has no exhibited member
and both period-return constructions remain unformed, so **A8 is unexecutable rather than passed,
failed, or vacuously true.** That is consistent with my own 584 finding that A8 can bite on nothing
today, and it is the correct verb — "unexecutable" rather than "vacuous".

### 1.4 The new-degeneracy hunt

[PROVABLE] I hunted two classes.

**(a) A different member pair — none found.** Reversal (`T^-`) and positive rescaling (`T_s`) both
transport the two sides together. Any `T' = g o T` acts by the same `g` on both sections by (R9g), so
no member pair can separate them. The general statement: because both returns are `T(iota_a(.))` of a
**`T`-free** period, every member pair yields the same condition `p_H = p_Hol`. **No member-pair
degeneracy exists in the repaired form.**

**(b) A covariance loophole — hunted, and it does not fire.** This was my live candidate. The concern:
if R9-V002 could be asserted at both addresses of an orbit for one physical cell, then with H's period
sealed odd (`ev_(a^-) = -ev_a`) and HOL's log-branch oddness *not* typed — which the 587 re-review
established — one would get

```text
at a  :  p_H = p_Hol
at a^-:  -p_H = p_Hol^-     [using p_H(c^-) = -p_H(c)]
and if p_Hol were EVEN, these give p_H = -p_H, hence p_H = p_Hol = 0.
```

**It does not fire, and the reason is structural.** The build's cell is

```text
c = (a, epsilon, K, Y, A1, A0, N; one alleged H construction; one alleged HOL construction),
```

with **the address `a` as the first component**. So `a` and `a^-` are **two different cells**, each
carrying its own independent assertion. R9-V002 imposes no equation across an address orbit, and the
collapse cannot be assembled.

**NEW_DEGENERACY = none.**

## 2. C2 — the ε = 0 carriage typing

[PROVABLE] **The route-specific full-cell form is well defined.** The scalarization index is
route-specific (`I^H = Triv_[a]`, `I^Hol = Scal^Hol`) rather than conflated, and the build states
explicitly that a common R9 package supplies only the **diagonal** subfamily `S_T`, while **A7
carriage on HOL still ranges over every retained `S`, not only that diagonal.** That is exactly the
right care: the R9 repair's diagonal does not silently narrow A7's quantifier.

[PROVABLE] **The typing matches my own 584 derivation.** "The domain and denominator metric are
index-free … only the scalarized self-map in the numerator carries `i`" — which is precisely the
post-composition asymmetry I derived. And (C7) reproduces my law:

```text
q_(a,epsilon,T')^(per,H) = h_d(g) q_(a,epsilon,T)^(per,H),
```

with `h_d` the metric's homogeneity factor — my `q_T = r_T q_1` in its correct, homogeneity-explicit
form. **The build states the dependence I said was undisplayed; the 584 bonus finding is closed.**

[PROVABLE] **The lattice entry is the FULL audit cell**, not the `q`-projection, and the certified
full-cell lattice is fixed **before** the cell is classified and is response-independent. A formed and
certified cell outside it is an exit witness; a missing or inconsistent certificate is `PENDING` or
its own earlier falsifier and is **"not silently reclassified as an A7 lattice exit."** That is the
correct discipline — an unformed object is not an exit — and it is the anti-tuning direction.

[PROVABLE] **The stronger orbit covariance is genuinely gated, not silently used.**
`PERIOD_ORBIT_COVARIANCE_CERT` (C8) types the orbit-covariant full-cell class with coherent
transports (`kappa_id = id`, `kappa_(g2 g1) = kappa_g2 o kappa_g1`) and **"no member is asserted"**.
The gating sentence is explicit: **"Without C8, C4 remains the well-typed carry-all-index predicate,
while the stronger numeric/lattice orbit class is `PENDING`."** And (C9)'s sign-reversal invariance
`q_(-T) = q_T` is itself conditional on an inhabited inversion-isometry arm — not assumed. **PASS.**

## 3. C3 — fresh attack, and verb audit

[PROVABLE] **My fresh attack was the address-covariance loophole** (§1.4(b)) — a class distinct from
the member-pair attack that produced the original finding, and the one place a repaired
common-member form could still have collapsed. **It does not fire**, blocked by the address's
presence in the cell tuple.

[PART-PROVABLE] **And it turns constructive, which is worth recording because the build does not say
it.** Because `a` and `a^-` are separate cells, R9-V002 applies independently at each. If **both**
address-cells of an orbit are formed, then with `p_H(c^-) = -p_H(c)` sealed on the H side:

```text
p_H(c)   = p_Hol(c)
p_H(c^-) = p_Hol(c^-)
=>  p_Hol(c^-) = -p_Hol(c).
```

**HOL's log-branch oddness follows** — the very property the 587 re-review flagged as untyped
(needing `U_b^S` inversion-closed and the branch odd). Contrapositively: **if HOL's period fails to be
odd, one of the two address-cells displays a disagreement and voids the disagreeing construction.**

So R9-V002, applied across an address orbit, gives that untyped obligation **a falsifier it did not
previously have**. It does not discharge the obligation — nothing here builds `U_b^S` or the branch —
but it converts it from an unbitten condition into one A8 can test wherever both address-cells form.
**I record this as a finding in the build's favour that the build itself does not claim.**

### Verb audit on my own board

| My line | Strongest verb my sources carry | Honest? |
|---|---|---|
| `SEAMS_V002 = CONFIRMED` | carrier construction re-derived by me; my own regression rerun to the full diagonal | **CLEAN** — I confirm a repair to my own finding without softening the standard |
| `NEW_DEGENERACY = none` | both attack classes run; the covariance one blocked by (T7)'s cell tuple | **CLEAN** — I name the attack I *tried* and why it failed, not only the result |
| C2 `PASS` | (C7) reproduces my 584 law; (C8) explicitly gated with `PENDING` absent it | **CLEAN** |
| the constructive corollary | derived by me from (T7) plus the sealed H-side oddness | **CLEAN** — tagged PART-PROVABLE, and flagged as *not* discharging the obligation |
| A8 status | the build's own "unexecutable rather than … vacuously true" | **CLEAN** — consistent with my 584 finding, and I adopt the build's sharper verb |

[PROVABLE] **No correction to my own prior record was required by this relay.** My 584 computation was
correct as stated, its repair is correct, and my characterisation of the failure mode — independent
quantifiers over the two families — is the one the build itself adopts. I record that plainly rather
than manufacturing a self-correction for symmetry with earlier relays.

```text
VERB_AUDIT_SELF = CLEAN
```

## 4. Fence and stopping board

```text
R9 = REPAIRED; my two-member regression yields the full diagonal, not {(0,0)}
QUANTIFIER = exactly A8's; no Triv x Scal product, no normalization, no
             output-dependent matching
MEMBER-PAIR DEGENERACY = none possible in the repaired form
COVARIANCE LOOPHOLE = hunted; blocked by the address in the cell tuple;
             turns into a falsifier for HOL's log-branch oddness
EPSILON=0 CARRIAGE = well-typed, route-specific, full-cell, index-free domain;
             stronger orbit covariance GATED with PENDING absent C8
A8 TODAY = UNEXECUTABLE (no exhibited member; both returns unformed)
MACHINERY_APPEAL = false
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

No register, plan, tracker, git, commit, push, member-binding, fixed-point, end-test, or evaluation
action was performed by this lane. No law was adopted and no route was chosen.

SEAMS_V002 = CONFIRMED (+my own two-member computation rerun against R9-V002 gives the identical
condition `p_H(c) = p_Hol(c)` at both `T` and `T^-`, solution set the full diagonal `{(p,p)}` rather
than `{(0,0)}`, so `p = 0` is no longer forced; +the diagnosis of my old attack is exact — it froze
the HOL return while reversing only `T_H`, and the common-member orbit form transports both sides
together by `g_(T',T)` so no such configuration exists; +the orbit carrier `Kbar_[a] ≅ R_or,[a]` was
re-derived by me including the cocycle, all three equivalence properties, `psi`'s well-definedness and
representative-independence, and it removes the trivialization representative without quotienting away
sign or magnitude; +the quantifier matches A8 element by element and adds no scalarization-family
quantifier, Cartesian product, normalization, or output-dependent matching; +the ε=0 carriage is
well-typed and route-specific with the R9 diagonal explicitly NOT narrowing A7's HOL quantifier, the
domain and denominator metric index-free as my 584 derivation requires, `(C7)` reproducing my
`q_{T'} = h_d(g) q_T` law, the full-cell lattice fixed before classification, unformed certificates
held `PENDING` rather than reclassified as lattice exits, and the stronger orbit covariance genuinely
gated by `(C8)` with `PENDING` absent it)
NEW_DEGENERACY = none (+two attack classes run: no member pair can separate the two sections, since
both returns are `T(iota_a(·))` of a `T`-free period and every `T' = g∘T` acts by the same `g` on
both; +the covariance loophole — asserting R9-V002 at both addresses of an orbit, which would force
`p = 0` if HOL's period were not odd — does NOT fire, because `(T7)` makes the address the first
component of the cell so `a` and `a^-` are different cells carrying independent assertions; +and it
turns CONSTRUCTIVE, which the build does not claim: with both address-cells formed and `p_H(c^-) =
−p_H(c)` sealed, R9-V002 yields `p_Hol(c^-) = −p_Hol(c)`, giving HOL's log-branch oddness — flagged
untyped at the 587 re-review — a falsifier it did not previously have, without discharging it)
VERB_AUDIT_SELF = CLEAN
