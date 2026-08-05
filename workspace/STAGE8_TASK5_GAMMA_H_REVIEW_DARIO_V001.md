# STAGE 8 TASK 5 — REVIEW OF THE Γ^H STOPS: ARE THE FOUR GAPS GENUINE? — DARIO V001

Date: 2026-08-05
Lane: Dario (Claude Opus 5), cross-family reviewer of record
Task: PASTE 580 / Task 5
Under review: `STAGE8_TASK5_GAMMA_H_ROUTE_LANE3_V001.md` (`f2317e41…`, verified, 812 lines, 30 pieces)
The Ξ_N ruling waits on this.

## Lead result

```text
REGISTER_HEAD = Q-506

JOINT I   = GENUINE_GAP   (+narrowed: the quotient-descent half DISSOLVES)
JOINT II  = GENUINE_GAP   (+the build's own negative is FALSE as phrased;
                            the gap stands on other, better ground)
JOINT III = GENUINE_GAP   (+REASON REPLACED: the unit half dissolves outright;
                            the gap is ORIENTATION, and the builder's stated
                            reason is wrong on both of its clauses)
JOINT IV  = GENUINE_GAP   (+independent of II, contra one sweep;
                            +MY OWN standing phrasing corrected)

LEDGER: sound on ~25 of 30 rows; 3 rows carry an unratified coinage as codomain,
1 row's seal status is imprecise, 1 sealed piece is omitted. NO mistype opens a
joint -- but the codomain mistype is why Joint III was stopped for the wrong reason.

COMPARISON = restated. "Four distinct gaps vs one map" OVER-COUNTS H's seams and
UNDER-COUNTS HOL's. The seam costs are largely COMMON to both routes. What
actually differs is the core: H needs a CONSTRUCTION (the realization arrow);
HOL needs a DECLARATION (the correspondence). The Xi_N ruling should weigh that,
not the raw joint count.

VERB_AUDIT_SELF = CLEAN (+1 disclosed correction to my own standing phrasing)

MEMBER_BOUND = false ; FIXED_POINT_EXECUTED = false ; END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = false
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

**All four stops stand. None dissolves.** But two of the four stand for reasons other than the ones
given, and in both cases the corrected reason is sharper. That matters here specifically, because a
ruling is waiting and a gap misdiagnosed is a gap mispriced.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-506 | verified |
| Build `f2317e41…`, 812 lines | verified before reading |
| My own prior artifacts (`a58400f6…`, `e287b057…`, `f76139e5…`, `73524d7a…`, `af955f81…`, `1b878d7a…`) | verified |
| Output name absent before construction | verified — no clobber |

## 1. M1 — the four joints

### 1.1 Joint III — GENUINE_GAP, and the reason is not the one given

[PROVABLE] **The unit half dissolves.** I derived the unit class of the Hodge-carrier pairing. With
`U_k` the torsor of `C_N^k` and the ratified rule `[R_A] = U_A^{-2}`:

```text
[d_k]        = U_(k+1) U_k^(-1)
[delta_(k+1)] = [R_k^(-1)][d_k^*][R_(k+1)]
              = U_k^2 · U_(k+1)U_k^(-1) · U_(k+1)^(-2) = U_k U_(k+1)^(-1)
[Delta_k]    = [d_(k-1)][delta_k] = (U_k U_(k-1)^(-1))(U_(k-1) U_k^(-1)) = 1
             = [delta_(k+1)][d_k] = (U_k U_(k+1)^(-1))(U_(k+1) U_k^(-1)) = 1
=> Delta_k and P_H,k are class-1 endomorphisms
=> [<x,h>_N] = [(R_k x)(h)] = U_k^(-1) · U_k = 1.
```

This reproduces the Maxwell/Hodge cert's own §2.2 — "`Delta` and `P_H` are endomorphisms of one unit
class", `IMPLICIT_CROSS_SECTOR_UNIT = none`, `PI_MX_OUTPUT_UNIT = dimensionless` — one level up on the
cochain degrees. Two cross-checks confirm the reading is forced: the cert's `<x,Delta x> = ||delta x||^2 + ||d x||^2`
adds pairings taken in three different degrees, so unit-homogeneity forces degree-independence; and
`g_Y = g_C (+) g_K` adds a C-sector to a K-sector scalar, which is only well formed if both are class 1.

[PROVABLE] **Two consequences, and both correct the build.** First, my own `chi_CK` hypothesis is
**refuted**: `(Z2-1)`/`(Z2-3)` forbid setting a coefficient of *nontrivial* class to 1, and class 1
has a canonical member — nothing is chosen, and the arrow is not C–K mixing. Second, the build's
stated reason — "no sealed law or metric identity determines a member of (JIII-5). Choosing one merely
because the codomain is real would be an invented cross-sector arrow" — **fails on both clauses**: a
ratified metric identity *does* determine the class, and the arrow is *not* cross-sector.

[PROVABLE] **So why does the joint still not close? Orientation.** Write `U_a` as multiplication by
`mu(a)`. Since `c_(N,-gamma) = -c_(N,gamma)` gives `ev_(a^-) = -ev_a`, covariance `u_(a^-) = u_a`
forces

```text
mu(a^-)·(-ev_a) = mu(a)·ev_a   =>   mu(a^-) = -mu(a).
```

If `U^H` is **address-independent** — which is exactly what `U^H = id` means — then `mu(a^-) = mu(a)`,
so `mu = -mu`, so `mu == 0` and the period functional vanishes identically. Invariantly: a
Z2-equivariant linear map from the sign representation to the trivial representation is zero.
**The route that dissolves the unit half is the route orientation kills.**

[PROVABLE] **And the verdict is robust to the one thing the sweeps disputed.** Audit V001 types the
orientation demand explicitly: "Equations `(S3-4a)`–`(S3-5a)` are **missing candidate premises, not
sealed facts**. If `(S3-4a)` is unavailable, the raw evaluation instead lies on an **odd signed-charge
line**. It does not define a covariant return into the trivially acted-on scalar coupling carrier."
So both horns close the joint:

- **with** the demand: `U^H` must be address-odd, i.e. a **trivialization of an orientation line** —
  and every trivialization selects a member of a retained covariance orbit, which the no-selection
  discipline forbids;
- **without** it: there is no covariant return into `K_amb` at all.

**GENUINE_GAP — but it is an orientation seam, not a units seam.** The correct typing is that
`ChargeUnit_N` is not a unit class but an orientation line of trivial unit class, and `U^H` is a
trivialization, not a conversion.

### 1.2 Joint I — GENUINE_GAP, narrowed by half

[PROVABLE] **The quotient-descent half dissolves.** `Q_N` is the corestriction of the R5 realization
`qtilde_N`, so any continuous map defined on `O_R5` descends through it automatically; the descent
`(JI-5)`/`(S6)` is therefore **not an independent obligation**. And `O^resp` *is* `O_R5` — the very
carrier `qtilde_N` maps into — so the "missing bridge" is not an arrow between unrelated carriers: the
canonical arrow already exists **in the opposite direction**.

[PROVABLE] **What remains is real:** the bridge in the *required* direction, together with the
source-extension package's image-membership. That is a genuine gap and I could not close it.

[PART-PROVABLE] A conditional strengthening was proposed and I do **not** adopt it: an incompatibility
between the sealed `L_F2'` membership clause `D_N^Loc subset Sch_N(Op_N^(loc,2))` and a sealed
pattern would convert a void condition from open to triggered — but only under an unsealed
support-compatibility hypothesis on `iota_N^Q408`. The theorem is sound; its hypothesis is not sealed.
**Recorded as a conditional, not banked.**

### 1.3 Joint II — GENUINE_GAP, on better ground than the build gives

[PROVABLE] **The build's §3.1 negative is false as phrased.** It asserts as `[PROVABLE]` that no
sealed domain/codomain declaration types `sigma_N^fin` as a map into a cochain carrier. Three sealed
artifacts do state such a declaration — one of them inside the build's own seal key.

[PROVABLE] **The gap nonetheless stands, and I judge it the load-bearing one of the four.** The
correct statement is that a *declaration* exists while a *construction* does not, and the latest
controlling authority withdraws the declaration for the physical case. My own seed adjudication is the
adjudicator-of-record on exactly this point and rules **with** the builder: `Loc_N = sigma_N^fin` has
no stated domain, codomain, or linear structure in sealed stock, and `Loc_N^physical_for_J2 = NOT_BUILT`.

[PROVABLE] **The sharpest corroboration:** the corpus's *only* source-side production of a member of
`C_N^k` is `m_T,N` — and it runs through `Loc_N^fin`, the shadow, on the normalization branch. There is
no second, physical production. **Joint II is the genuine unbuilt construction.**

### 1.4 Joint IV — GENUINE_GAP, and independent of II

[PROVABLE] One sweep argued Joint IV is downstream of Joint II — that naturality of a nonexistent
arrow is not a separate gap. I put weight on this myself before checking it, and it does **not** hold:
establishing it requires an unsealed step, and **four sealed or registered boards enumerate
nonidentity (F3) as a debt distinct from the physical-`Loc` construction.** Joint IV's `(F1)`
quotient-descent content is about the sealed `Q` and is independent on its face.

[PROVABLE] **A correction to my own standing record, which I own.** I have written in two prior
artifacts that `(F3)` — `Loc_M eta_f^K = j_f^C Loc_N` — "exists nowhere in the corpus." **That is
false as phrased.** The equation is *stated* in at least six files. What is absent is a **proof on any
nonidentity arrow**. My phrasing conflated "unstated" with "unproved", and the accurate finding is the
second. The defect it names is unchanged in substance and unchanged in consequence; the wording was
wrong and I have carried it twice.

## 2. M2 — the 30-piece ledger

[PROVABLE] Sound on roughly 25 of 30 rows. Four defects, **none of which opens a joint**:

| Defect | Content | Bearing |
|---|---|---|
| Rows 21/22/25 | codomain named `ChargeUnit_N` — an **unratified coinage** occurring in only three files corpus-wide, all of them the two audits and this build | Retyping to `K_amb` is a **relabelling**; it does not close Joint III. But it is why Joint III was stopped for the wrong reason. |
| Row 13 | seal status of `sigma_N^fin` imprecise | A declaration exists; a construction does not. A one-word erratum, not a mistype of substance. |
| Census omission | `lambda_N` / `pi_Mx,N : C_N^k -> R` is sealed in the build's own seal key and absent from the census | Worth a 31st row for completeness; opens no route — and importing it would run through the normalization branch, the F_PLDEC hazard. |
| Seal-key omission | the audit V001, which is the **origin** of `ChargeUnit_N`, the orientation derivation, and the seam typing, is not in the sixteen-entry seal key | The build reasons about a seam whose defining source it does not key. Recommend adding it. |

[PROVABLE] Custody is otherwise clean: all sixteen keyed sources re-hash correctly.

## 3. M3 — the comparison of record, restated

[PROVABLE] **The "four distinct gaps vs one map" framing does not survive this audit.** It
over-counts H and under-counts HOL.

**Over-counts H.** Joint III's unit half dissolves outright (§1.1); Joint I's quotient-descent half
dissolves outright (§1.2). What remains on H is: a bridge direction (I), **the realization arrow
(II)**, an orientation trivialization (III), and nonidentity naturality (IV). One of those — II — is a
genuine unbuilt construction. The other three are seams and interfaces around it.

**Under-counts HOL.** The HOL route carries its own scalar seam, and the parity is exact: `U^Hol : R -> K_amb`
is an **explicitly unbuilt obligation of record whose source is literally `R`**. Unit triviality does
not discharge it there either — which is independent confirmation that the H seam's difficulty was
never about units. HOL also carries its own orientation covariance and `A7_HOL_BRANCH_COMPAT`.

[YOURS] **What the Ξ_N ruling should now weigh.** Not four-versus-one. The seam costs are largely
**common** — orientation, a scalar seam, a carrier, unit discipline — and appear on both routes. What
genuinely differs is the core object:

- **H's core is a CONSTRUCTION**: the realization arrow (Joint II), buildable by lane work, standing on
  the most confirmed machinery in the corpus, with its hazards already mapped by name.
- **HOL's core is a DECLARATION**: the correspondence `Ξ_N`, which no lane can schedule and which
  asserts new physical content (which source kernel encircles which loop).

[YOURS] That is the same asymmetry I put to the principal at 577, and this audit **sharpens rather
than reverses it**: H's apparent four-fold disadvantage was partly an artifact of counting seams that
HOL also pays. My CARRY_BOTH recommendation is unchanged, and A8 has already ruled it. If anything,
this audit strengthens the case for keeping lane effort on H, because Joint II is the only one of the
four that is a construction rather than a seam — and it is the one the program knows how to attack.

[PROVABLE] **What this does not change:** all four joints stop; `Γ^H` is not built; the seed remains a
carried condition; membership remains DEFECTIVE on independent grounds.

## 4. M4 — fresh attack, and verb audit

[PROVABLE] **My fresh attack was the unit-class fork** — I posed it as a genuine fork (dimensionless ⟹
the joint dissolves; nontrivial class ⟹ the joint is *excluded* by `(Z2-1)`/`(Z2-3)`, a stop stronger
than claimed) rather than asserting either horn. **Both horns turned out wrong, and that is the
finding**: the class is 1, so the `chi_CK` exclusion does not apply *and* the joint does not dissolve,
because the obstruction was never units. Posing it as a fork is what made the third possibility
visible. Had I asserted the dimensionless horn I would have reported a false ROUTE_FOUND.

### Verb audit on my own board

| My line | Strongest verb my sources carry | Honest? |
|---|---|---|
| `JOINT III = GENUINE_GAP`, reason replaced | unit algebra derived; both orientation horns closed from audit V001's own text | **CLEAN** — I report the stop standing while refuting my own hypothesis |
| `JOINT I` narrowed | `Q_N` as corestriction; `O^resp = O_R5` | **CLEAN** — the conditional strengthening is recorded and **not** banked |
| `JOINT II = GENUINE_GAP` | the build's negative false as phrased; my own seed adjudication rules with the builder | **CLEAN** |
| `JOINT IV` independent | four sealed boards; the non-independence needs an unsealed step | **CLEAN** — I abandoned a position I had initially favoured |
| `COMPARISON` restated | the `U^Hol : R -> K_amb` parity | **CLEAN** — the restatement cuts *toward* my prior recommendation, and I say so rather than presenting it as neutral |

[PROVABLE] **One disclosed correction to my own standing record** (§1.4): my phrase "`(F3)` exists
nowhere in the corpus", carried in two prior artifacts, is **false as phrased** — `(F3)` is stated in
at least six files; what is absent is a proof on any nonidentity arrow. Substance and consequence
unchanged; the wording was wrong and I carried it twice before catching it.

```text
VERB_AUDIT_SELF = CLEAN (+1 disclosed correction to my own standing phrasing)
```

## 5. Fence and stopping board

```text
FOUR JOINTS = ALL STOPPED; none dissolves
J-III unit half = DISSOLVED (class 1; chi_CK inapplicable); gap is ORIENTATION
J-I descent half = DISSOLVED (Q_N is a corestriction; descent automatic)
J-II = the load-bearing gap; the only genuine unbuilt CONSTRUCTION of the four
J-IV = independent of J-II; (F3) stated but unproved on nonidentity arrows
LEDGER = ~25/30 sound; 3 codomain mistypes, 1 seal-status erratum, 1 omission,
         1 seal-key omission; none opens a joint
COMPARISON = seam costs largely COMMON to both routes; the real difference is
             construction (H) versus declaration (HOL)
MACHINERY_APPEAL = false
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

No register, plan, tracker, git, commit, push, member-binding, fixed-point, end-test, or evaluation
action was performed by this lane. No law was adopted and no route was chosen.

JOINT_I = GENUINE_GAP (+narrowed by half: the quotient descent `(JI-5)`/`(S6)` is NOT an independent
obligation, because `Q_N` is the corestriction of the R5 realization so maps on `O_R5` descend
automatically, and `O^resp` IS `O_R5` with the canonical arrow already existing in the opposite
direction; what remains is the bridge in the required direction plus image-membership; a conditional
exclusion theorem was offered and is recorded but NOT banked, its support-compatibility hypothesis
being unsealed)
JOINT_II = GENUINE_GAP (+the build's own §3.1 `[PROVABLE]` negative is FALSE as phrased — three sealed
artifacts, one in its own seal key, do declare `sigma_N^fin` into a cochain carrier; the gap stands on
better ground: a declaration exists, a construction does not, the latest controlling authority
withdraws the declaration for the physical case, and the corpus's only source-side production of a
member of `C_N^k` runs through the shadow on the normalization branch; this is the load-bearing joint
and the only genuine unbuilt construction of the four)
JOINT_III = GENUINE_GAP (+REASON REPLACED: the unit half dissolves outright — the Hodge-carrier pairing
has class 1 by the ratified `[R_A] = U_A^(-2)` rule, reproducing the cert's own `PI_MX_OUTPUT_UNIT =
dimensionless`, so my own `chi_CK` STRONGER_STOP hypothesis is refuted and the builder's stated reason
fails on both clauses, a metric identity DOES fix the class and the arrow is NOT cross-sector; +the
gap is ORIENTATION: address-independent `U^H` forces `mu = -mu`, hence `mu == 0` and the period
vanishes identically, so `U^H = id` is a proved impossibility rather than a missed arrow; +robust to
the disputed status of `(S3-4a)` — with the demand, `U^H` is an orientation-line trivialization and
therefore a member selection; without it, audit V001's own text says the evaluation lies on an odd
signed-charge line and defines no covariant return into `K_amb`)
JOINT_IV = GENUINE_GAP (+independent of Joint II, contra a position I initially favoured: the
downstream claim needs an unsealed step, and four sealed or registered boards enumerate nonidentity
`(F3)` as a debt distinct from the physical-`Loc` construction; +correction to my own standing record:
"`(F3)` exists nowhere in the corpus", which I carried in two prior artifacts, is false as phrased —
the equation is stated in at least six files and what is absent is a proof on any nonidentity arrow)
COMPARISON = restated (+"four distinct gaps vs one map" over-counts H and under-counts HOL: two of H's
four halves dissolve, while HOL carries its own scalar seam whose parity is exact — `U^Hol : R ->
K_amb` is an explicitly unbuilt obligation with source literally `R`, so unit triviality discharges
neither route; +the seam costs — orientation, scalar seam, carrier, unit discipline — are largely
COMMON; +what genuinely differs is the core: H's is a CONSTRUCTION the lanes can attack on the most
confirmed machinery in the corpus, HOL's is a DECLARATION no lane can schedule; +the Ξ_N ruling should
weigh construction-versus-declaration, not the raw joint count; this sharpens rather than reverses the
asymmetry I put to the principal at 577)
VERB_AUDIT_SELF = CLEAN (+1 disclosed correction to my own standing phrasing, carried twice before
being caught)
