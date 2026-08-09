# STAGE 8 / 7A / [PLAN:A1-CORRECTIVE-2] — RADII CARRIED, TIERS CONDITIONED TRUE

Lane: DARIO (Builder B, independent verifier). Relay 784.
State brief pinned by the relay: `PROGRAM_STATE_BRIEF_V005.md` = `e26f0d16055f3e83…` — **digest
matches the relay's pin**, seal OK, read before task work.
Governing: relay 783's cross-check of my 781 (`8cef86b990895978…`, SEALED-OK). **All three
refutations ADOPTED.** Law 7 (CORRECTION PROPAGATION): 781 is the named consumer; this is the
propagation. All headline items **CLAIMED**.

## Lead determination — CLAIMED

**783 is right on all three counts, and the third one reaches further than it says.**

```text
(i)   (F) does NOT extract the 16.   ADOPTED — and the negative existential is now CLOSED:
      no sealed ground anywhere in 2,972 files names a scalar-Phi-carrier condition.
      TIER 2 IS DROPPED as I stated it, and replaced by the weaker surface that is true.
(ii)  The printed sum and the member bounds SILENTLY SET ALL THREE RADII TO 1.   ADOPTED.
(iii) The member bounds also consume (F) — without it the parent factor is twisted and
      "the spectrum itself changes, not merely the count".   ADOPTED.
```

**The consequence of (ii) is sharper than a missing condition line.** With the radii restored,
the A–B bound separation is not `1`:

```text
              lambda_A  >=  P_min  +  1/r_flux^2  +  C2_parent
              lambda_B  >=  P_min  +     0        +  C2_parent
                                        ^^^^^^^^^
   THE SEPARATION IS 1/r_flux^2 — A FREE DATUM, NOT A PURE NUMBER.
```

So the *"exactly 1"* that survived 777's correction, survived 781's correction, and was restated
as robust in both — **was a unit-radius artifact the whole time.** 777 called it "`p2min`-free";
781 called it "unconditional". Both are true and both were beside the point: it is
`r_flux`-*dependent*, and `r_flux` is decline-register free data (D9/S28). **This is the third
consecutive relay in which that separation has been restated at too high a grade, each time by
correcting a different qualifier and missing this one.**

**What stands, and it is the robust core:** `lambda >= C2_parent` — **PROVED of record (Q-690)**,
and it is proved *because* it consumes nothing: not `(F)`, not `(S)`, not `(U)`, not the radii.
Every formula that needed a condition needed it because it reached past positivity into structure.

**And the `beta` mechanism is now IN the formulas** (AS1's demanded consequence), where it turns
out to have **four sectors, not U8's three** — the fourth being `Phi^dagger Phi`, whose weight is
unselected.

---

## 0. Preflight

```text
OUTPUT NAME     probed recursively before any write: artifact and sidecar ABSENT.
STATE BRIEF     PROGRAM_STATE_BRIEF_V005.md  e26f0d16055f3e83…  seal OK; digest MATCHES the pin.
783 (governing) STAGE8_7A_REBUILD_CROSSCHECK_CODEX2_V001.md  8cef86b990895978…  SEALED-OK
781 (subject)   STAGE8_7A_DBR_LAYER_REBUILD_DARIO_V001.md     d55b64459be8bdac…  SEALED-OK
768 (operator)  STAGE8_7A_TOWER_CONTEST_DARIO_V001.md         03db8d3da273f42c…  SEALED-OK
                spans re-derived this relay: [6410,6885) sha 4b6102e985b7a722…
                                             [10764,11705) sha d08cccc778b13b44…
DECLINES        DECLINE_REGISTER_V002.md  957476c8c605a370…  SEALED-OK  (S01–S37 authoritative)
Q-690           QUESTIONS_SETTLED_REGISTER_V001.md line 15023 — "lambda >= C2_parent is PROVED;
                the spectrum had silently set three radii to 1"

GATES: alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false.
No determinant evaluated; no member evaluated alone (FAMILY-BEFORE-DETERMINANT); no bundle class
adopted or eliminated; no member binding; no fixed-point execution; no end test; no numeric
evaluation of physical quantities; no comparison to measured constants; no common cell formed;
no junction map evaluated; no smooth data derived.
PE-1..PE-6: pointer-known, ZERO WEIGHT, NOT consulted, NOT opened.
NOTATION: the sealed source writes `r_flux`; the relay writes `R_flux`. Same object; the sealed
spelling is used throughout.
```

---

## 1. AS1 — RADII EXPLICIT EVERYWHERE

### 1.1 Derived, not pattern-matched

`Sigma_BR = T2_TQ × S2_flux` with a product metric and product spin structure. Then
`D_Sigma = D_(T2) ⊗ 1 + Gamma ⊗ D_(S2,A)` with the two summands anticommuting, so **their squares
add and commute**:

```text
D_(Sigma,A)^2  =  D_(T2)^2  +  D_(S2,A)^2
```

- `D_(T2)^2` on circles of radii `R_T`, `R_Q`: eigenvalues `p_t^2/R_T^2 + p_q^2/R_Q^2`, the
  integer labels `(p_t,p_q)` and their offsets fixed by the **unselected** spin structure.
- `D_(S2,A)^2` on a sphere of radius `r_flux`: the Dirac operator scales as `1/r`, so its square
  carries `1/r_flux^2`, giving `ell(ell+2|q|)/r_flux^2`.
- `Phi^dagger Phi` is a **zeroth-order endomorphism** — no derivative, therefore **no geometric
  radius denominator**. Its own scale is unselected.
- `C2_parent` is an internal `Spin(10)` invariant and `Sigma_BR` carries no `Spin(10)` directions,
  so it is **radius-free**.

```text
H_0  =  D_(T2)^2 + D_(S2,A)^2  +  Phi^dagger Phi  +  C2_parent

GEOMETRIC SPECTRUM (exact, radii explicit):
   spec(D_(Sigma,A)^2) = { p_t^2/R_T^2 + p_q^2/R_Q^2 + ell(ell+2|q|)/r_flux^2 }
   ell = 0,1,2,… ;  d_S2(0) = 2|q| = |deg L| ;  d_S2(ell>=1) = 4(ell+|q|)
```

**Typing kept honest:** the whole of `spec(H_0)` is **not** the sum of the summands' spectra —
`Phi^dagger Phi` need not commute with `D_(Sigma,A)^2`. 768's sealed display flags this with its
own brackets, `spec = {geometric} + [Phi^dagger Phi] + C2_parent`; the bracket **is** the
non-commutation flag, and it is only removable under `(S)`.

### 1.2 Condition (U), named

```text
(U)  UNIT-RADIUS CONVENTION:  R_T = R_Q = r_flux = 1.
     NOT a fact.  768's spectrum display is stated "at unit radii"; the radii are free data
     (DECLINE_REGISTER_V002 D9/S28).  (U) is a CONVENTION ON THE DISPLAY, never a selection.
```

**(U) is named at five sites** where prior formulas consumed it silently: the tier-3 trace sum
(§2.3); member bound A and member bound B (§3.1, two sites); the A–B separation (§3.2); and the
declined `mu^2 = 1` display (§2.4), which inherits it.

### 1.3 The beta mechanism, now IN the formula — and U8 has FOUR sectors, not three

Under a common rescaling `R_T, R_Q, r_flux → beta·(R_T, R_Q, r_flux)`, read directly off §1.1:

```text
p_t^2/R_T^2 , p_q^2/R_Q^2 , ell(ell+2|q|)/r_flux^2        ->  beta^-2   (two derivatives)
T = Gamma_Sigma c(nabla_A Phi)                            ->  beta^-1   (exactly one derivative)
C2_parent                                                 ->  beta^0    (radius-free, sealed)
Phi^dagger Phi                                            ->  beta^?    *** UNSELECTED ***
```

**U8 connected, and sharpened.** 775's `U8` said *"three beta weights … none of which depends on
the class."* With `Phi^dagger Phi` restored to the operator there is a **fourth sector**, and its
weight is not `beta^0` — it is **unselected**, because `Phi` is unselected and the record nowhere
states how it transforms under a geometric rescaling. 781 typed `U8` CONDITIONAL for exactly this
reason; the radii-explicit form now **displays** it instead of arguing it.

**And the two `beta`-invariant ratios are now visible rather than inferred.** `beta` is one
scalar; `R_T : R_Q : r_flux` are three independent free data, so the ratios survive any
quantification over `beta`. That is 777's **FC-e**, no longer an argument about a prose claim but
a reading of the denominators.

---

## 2. AS2 — THE TIERS, RESTATED TRUE

### 2.1 Tier 1 — the unconditional functional. **STANDS** (783: CONFIRMED)

```text
Tr f(H_0)  =  Tr_{L2(Sigma_BR, S_Sigma ⊗ E_parent)}  f( D_(Sigma,A)^2 + Phi^dagger Phi + C2_parent )
```
Consumes **no** condition — only the unselected analytic input `f`. It does not reduce.

### 2.2 Tier 2 — **DROPPED as stated at 781; replaced by the surface that is true**

**The negative existential, closed.** AS2 permits tier 2 only if sealed ground names a
scalar-Φ-carrier condition. It does not.

```text
GLOB: ./workspace/**/*.{md,json} + ./supervision/**/*.{md,json}
      (evaluator_build_A/ and checks/ EXCLUDED BY LAW; memory-bank never searched)
CORPUS SEARCHED: 2,972 files
KNOWN-POSITIVE CONTROLS, case-sensitive, all non-zero:
      Phi^dagger Phi 19 ; E_parent 21 ; C2_parent 20 ; "flat parent connection" 7
MEANING PROBE (13 forms; substring presence is not a display — every hit was READ):
      "Phi … proportional to the identity"    0     "Phi … central"              0
      "Phi … multiple of the identity"        0     "Phi … Id_E"                 0
      "scalar-Phi"                            0
      "Phi … scalar" 7 / "scalar … Phi" 4 / "Phi … commut" 6 / "covariantly constant … Phi" 3
            -> ALL READ.  NONE displays a sealed condition making Phi scalar on E_parent.
```

Two of the hits are **explicit sealed negatives on precisely this question**:

- **my own 768**, which already listed the missing object as a **WOULD-BUILD** (i.e. absent):
  *"WOULD-BUILD, to convert the block form into an exact spectrum — ANY ONE OF: (a) `nabla_A Phi
  = 0` … (b) `[T, D_(Sigma,A)^2] = 0` AND `[T, C2_parent] = 0` …"*
- **Codex 2's 764 cross-check**: *"No sealed sentence cancels the middle term, makes `Phi`
  covariantly constant, or sets `Phi^dagger Phi = 1`. The same principle explicitly lists `Phi`
  as unselected."*

**The lawful (F)-only surface** — quoted from 783 and adopted, with the radii of §1.1 restored:

```text
Tr f(H_0)  =  Tr_{L2(Sigma_BR,S_Sigma) ⊗ E_parent}
                 f( D_base^2 ⊗ Id  +  Phi^dagger Phi  +  C2(16)·Id )

   D_base^2 spectrum = p_t^2/R_T^2 + p_q^2/R_Q^2 + ell(ell+2|q|)/r_flux^2

   *** NOT 16 copies of one base trace. ***
```

**(F) buys two things and not the third:** it makes the geometric Dirac part act identically on
the flat parent multiplicity, and it makes `C2_parent` the scalar `C2(16)` on the irreducible
**16**. It says nothing that makes the unselected finite map `Phi` act as one scalar on all 16
internal directions. **S27's own wording bounds it** — the grant is of *"flat `×16`
**multiplicity**"*, which is a statement about the geometric operator's degeneracy, **not** a
licence to factor a `16` out of a trace whose argument contains `Phi^dagger Phi`. The conditional
grant, read exactly, refuses the use I made of it.

### 2.3 Tier 3 — `(F) + (S) + (U)`, all conditions displayed

```text
(S)  Phi^dagger Phi = mu^2 · Id on the full carrier, mu^2 >= 0 constant, and commuting.
     STATED AS A CONDITION, NEVER AS A FACT.  §2.2 establishes no sealed ground names it.

Under (F) AND (S), radii EXPLICIT — no (U):

  Tr f(H_0) = SUM_(p_t,p_q) 2·N_lattice(p_t,p_q) · SUM_(ell>=0) d_S2(ell) · 16
                 · f( p_t^2/R_T^2 + p_q^2/R_Q^2 + ell(ell+2|q|)/r_flux^2 + mu^2 + C2_parent )

Under (F) AND (S) AND (U)  [site 1 of 5]:  the three denominators drop to 1.
```

`N_lattice(p_t,p_q)` carried explicitly and not absorbed (783 found no suppression; the register
still settles it nowhere — **`N_lattice` remains OPEN**, per V005).

### 2.4 The declined case, displayed as declined  [(U) site 5 of 5]

```text
mu^2 = 1  ==>  775's trace.  DECLINE-REGISTER S01 (= seed D1).
*** Displayed ONLY as one member of the (S)-family.  CONSUMED BY NO STEP of this artifact.
*** 783 verified independently: "No use of mu^2 = 1 was found."
```

---

## 3. AS3 — MEMBER BOUNDS, CONDITIONED TRUE

Write `P_min := min over occupied lattice labels of ( p_t^2/R_T^2 + p_q^2/R_Q^2 )`.

### 3.1 The bounds, with every condition named

| bound | statement | conditions consumed |
|---|---|---|
| **universal floor** | `lambda >= C2_parent` | **NONE.** Not (F), not (S), not (U), not the radii. **PROVED of record — Q-690.** Cited, not re-derived. |
| **member A** (`n = 0`) | `lambda_A >= P_min + 1/r_flux^2 + C2_parent` | **(F)** — without it the parent factor is twisted and *"the spectrum itself changes, not merely the count"*. Unconditional in `Phi`. **No (U)** — radii explicit. Under (U) [site 2]: `+1`. |
| **kind B** (`n >= 1`) | `lambda_B >= P_min + 0 + C2_parent` | **(F)**. Unconditional in `Phi`. Under (U) [site 3]: unchanged (the S² term is 0 either way). |
| **exact bottoms** | not established | 778: the full-`H_0` bottoms are not established. Unchanged. |

**The (F) attachment at the member bounds is 783's item (iii), and I had omitted it entirely** —
781 presented these as unconditional in everything, when they are unconditional only *in `Phi`*,
after (F).

### 3.2 The separation  [(U) site 4 of 5]

```text
lambda_A bound  −  lambda_B bound  =  1/r_flux^2          NOT 1.
Under (U): 1.
```

`r_flux` is unselected free data (D9/S28). **The separation is a free datum, not a pure number.**

[YOURS] **Three relays running.** 777 asserted the *bottoms* separate by 1 (corrected at 781 to
*bounds*, needing (S) for bottoms). 781 asserted the bounds separate by *exactly 1*
"unconditionally" and called it `p2min`-free. Both corrections were real and both left the
radius in place. **Each pass fixed the qualifier it was looking for and preserved the number.**
The invariant statement is: *the separation equals the reciprocal squared flux radius, and is
therefore not a number the record has fixed.*

---

## 4. AS5 — SALVAGE LEDGER FROM 781: every item dispositioned

| 781 item | disposition |
|---|---|
| tier 1 unconditional functional | **STANDS** — 783 CONFIRMED |
| `lambda >= C2_parent`, tight | **STANDS, UPGRADED** — CLAIMED → **PROVED** (Q-690) |
| tier 2, `(F)`-alone `16 · Tr_base` | **DEAD as stated** → **RE-CONDITIONED** to §2.2's non-factoring surface |
| tier 3 `(F)+(S)` printed sum | **RE-CONDITIONED** — radii restored; (U) named where used |
| member bounds A and B | **RE-CONDITIONED** — radii explicit; **(F) attached**; separation `1/r_flux^2` |
| `N_lattice` carried explicitly | **STANDS** — no suppression found; still **OPEN** in the register |
| D1 / `mu^2 = 1` consumed nowhere | **STANDS** — independently verified by 783 |
| dead items `U2`, `U5`, `U7` not reinstated | **STANDS** — independently verified by 783 |
| `U1`, `U6`, `U9` survive | **STAND** |
| `U3`, `U4` conditional | **STAND** |
| `U8` conditional | **STANDS, SHARPENED** — four `beta` sectors, not three (§1.3) |
| the 777 twelve-item salvage table | **STANDS**, except the bound separation, now `1/r_flux^2` |
| rule draft: R3 amended, R4 conditional, DG-1 worsened | **STAND** |
| `FC-a … FC-f`, `DG-2 … DG-4` | **STAND** — none was operator- or radius-dependent; **FC-e is now displayed in-formula** (§1.3) |
| 781's freedoms-consumed block | **DEAD as written** — omitted `f`, the radius specialization, and the (F) attachment. Replaced by §5.1 |
| 781's flattening check (vs V001) | **DEAD as written** — V001 superseded by V002; re-run at §5.2 (flagged to the registrar at 782) |

**Nothing carried silently: 16 items, 16 dispositions.**

---

## 5. AS4 — FREEDOMS CONSUMED, AND THE FLATTENING CHECK

### 5.1 `FREEDOMS_CONSUMED` — complete this time

| free datum | tag | point(s) of consumption |
|---|---|---|
| **the analytic input `f`** | **CARRIED-AS-UNSELECTED** | every trace, §2.1–2.4. Never chosen; no convergence claimed; the two-parameter-net burden remains undischarged. *(Omitted entirely from 781's block — 783 item (iii).)* |
| `R_T` | **CARRIED-AS-PARAMETER**, explicit in every formula; **CONDITIONED-ON via (U)** | §1.1, §1.3, §2.3; (U) at sites 1–5 |
| `R_Q` | as `R_T` | as `R_T` |
| `r_flux` | as `R_T`; **and it carries the A–B separation** | §1.1, §2.3, §3.1, §3.2 |
| odd profile `Phi` | **CARRIED-AS-PARAMETER** (tier 1, both member bounds); **CONDITIONED-ON via (S)** (tier 3) | §2.1, §2.3, §3.1 |
| parent bundle + characteristic class | **CONDITIONED-ON via (F)** — at tier 2, tier 3, **and at BOTH member bounds** | §2.2, §2.3, §3.1 *(the member-bound attachment omitted at 781)* |
| `C2_parent` numerical value | **CARRIED-AS-PARAMETER** — convention-carrying (764) | §2, §3 |
| spin structure on `T2_TQ` (hence `Lambda`, `P_min`) | **CARRIED-AS-PARAMETER** | §1.1, §3.1 |
| bundle class / chiral index `n` | **CARRIED-AS-PARAMETER** — the family index; neither adopted nor eliminated | §3 |
| `N_lattice(p_t,p_q)` | **CARRIED-AS-PARAMETER** — explicit, not absorbed | §2.3 |

**SUBSTITUTED: none.** No decision-of-record cited because none is needed.

### 5.2 `FLATTENING_CHECK` — against `DECLINE_REGISTER_V002` (S01–S37), **not** the superseded V001

```text
S27  flat x16 granted ONLY under (F)      CLEAN — and LOAD-BEARING HERE: read exactly, the grant
     [source span 10764,11705)            is of flat x16 MULTIPLICITY, which is why it does NOT
                                          license extracting 16 from a trace containing
                                          Phi^dagger Phi.  The grant's own wording refuses the
                                          use 781 made of it.  Tier 2 dropped accordingly.
S28  the five free D_BR data unselected;  CLEAN — all five (radii, spin structure, bundle class,
     constrainable only by "boundary       odd profile, chiral index) appear in section 5.1, each
     closure + the induced action,         tagged; none constrained here; no boundary-closure
     before any comparison"                argument invoked.
S01  (= seed D1) the +1 / Phi^dagger Phi   CLEAN — mu^2 = 1 displayed only as a declined member of
     identification                        the (S)-family; consumed by no step; 783 concurs.
S02–S26, S29–S37                          not touched by this artifact.
FLATTENING_CHECK = clean (37 rows walked; 3 live, each discharged above).
```

---

## 6. GROUNDING, JURISDICTION, VERB AUDIT

### 6.1 Jurisdiction

**On adopting all three refutations without defending any part of 781.** *What was the rule
written to protect?* Law 7 exists so a correction reaches its downstream consumers. The risk was
live: 781's tier 2 and member bounds were about to be consumed by a discrimination rule. *Does the
outcome space distinguish adoption from capitulation?* Yes — §4 disposes 16 items individually,
11 of which STAND, and §3.2 adds a correction 783 did not make. *Would the evidence look different
if 781 were right?* Yes: some sealed text would name a scalar-Φ carrier. §2.2 shows 2,972 files
contain no such text, with controls, and with two explicit sealed negatives — one of them mine.

**On the VOID CONDITION.** No class adopted, preferred, or eliminated. `(S)` and `(U)` are
displayed as conditions and consumed by no bound in §3.1's first row. `mu^2 = 1` is displayed
only as declined.

**On BR-1.** The relay authorises the convergence; it does not authorise its result. §3.2 runs
against my own last two artifacts and against the framing of this relay's own AS3, which says the
separation *"becomes `1/R_flux^2`"* — I add that it was therefore never the pure number three
relays have been restating.

**On builder independence.** 783 is Codex 2's sealed cross-check **artifact** — lawful stock. No
`evaluator_build_A/` or `checks/` file was read; both trees were excluded from the §2.2 probe by
path. `~/.codex` untouched; `memory-bank` never searched.

### 6.2 Self verb audit — **NOT CLEAN: four disclosures**

1. **I set three free data to 1 and then wrote "SUBSTITUTED: none."** That is the exact shape law 2
   exists to catch: the freedoms block asserted a negative that the formulas above it contradicted.
   The block was not merely incomplete — **it was false as written**, and it was false in the one
   direction an auditor cannot see from the block alone.
2. **The A–B separation has now been restated at too high a grade in three consecutive relays**
   (777 bottoms → 781 bounds → here, radii). Each pass corrected the qualifier it went looking for
   and **preserved the number `1` untouched**. The lesson is narrower and worse than "check your
   conditions": *a quantity that survives several corrections starts to read as established, and
   the surviving part was the part nobody had re-derived.*
3. **I misused a conditional grant by reading its consequence instead of its wording.** S27 grants
   flat `×16` *multiplicity*; I used it to factor `16` out of a trace containing `Phi^dagger Phi`.
   The grant never said that, and reading it exactly is what closes tier 2.
4. **`f` never appeared in any freedoms block I have written**, across 781 and 784's predecessors,
   although every trace consumes it. 783 found it; I had not.

*Direction check:* all four run against my own work; none creates a result. **The pattern has
shifted and I record the shift honestly.** At 781 the failure was propagation — a correction that
did not travel. Here the failure is **conditioning**: formulas true under conditions I held
implicitly and asserted I had not used. Both are bookkeeping, not reasoning, and both were caught
by the other lane rather than by me.

---

```text
RADII = explicit everywhere; condition (U) named at 5 sites (tier-3 sum; member bound A; member
   bound B; the A-B separation; the declined mu^2 = 1 display).  Derived, not pattern-matched:
   product spin structure gives D_(Sigma,A)^2 = D_(T2)^2 + D_(S2,A)^2 with commuting summands, so
   spec(D_(Sigma,A)^2) = { p_t^2/R_T^2 + p_q^2/R_Q^2 + ell(ell+2|q|)/r_flux^2 }; Phi^dagger Phi is
   zeroth-order and carries NO radius denominator; C2_parent is radius-free.  TYPING KEPT: the
   whole of spec(H_0) is NOT the sum of the summands' spectra — 768's brackets around
   [Phi^dagger Phi] ARE the non-commutation flag, removable only under (S).
BETA_MECHANISM = displayed in-formula (U8 connected AND SHARPENED).  Read off the denominators:
   the three geometric terms ~ beta^-2; the cross term T = Gamma_Sigma c(nabla_A Phi) ~ beta^-1;
   C2_parent ~ beta^0 (radius-free, sealed); and Phi^dagger Phi ~ beta^UNSELECTED.  U8 said THREE
   weights; with Phi^dagger Phi restored to the operator there are FOUR SECTORS, the fourth
   unselected.  Also now visible rather than argued: beta is ONE scalar while R_T : R_Q : r_flux
   are THREE independent free data, so the two beta-invariant ratios survive any quantification
   over beta — 777's FC-e, read off the formula.
TIER2 = DROPPED as stated at 781 (no sealed ground names a scalar-Phi carrier), and REPLACED by
   the surface that is true: Tr f(H_0) = Tr_{L2(Sigma_BR,S_Sigma) tensor E_parent} f(D_base^2
   tensor Id + Phi^dagger Phi + C2(16) Id) — NOT 16 copies of one base trace.  NEGATIVE
   EXISTENTIAL CLOSED: glob ./workspace + ./supervision (*.md,*.json), 2,972 files searched,
   evaluator_build_A/ and checks/ excluded by law; controls all non-zero (Phi^dagger Phi 19,
   E_parent 21, C2_parent 20, "flat parent connection" 7); 13 meaning-probe forms, every hit READ;
   five forms returned ZERO and none of the non-zero hits displays a scalar-Phi condition.  TWO
   EXPLICIT SEALED NEGATIVES, one of them mine: 768 lists nabla_A Phi = 0 and the commutation pair
   as WOULD-BUILD (i.e. absent); Codex 2's 764 cross-check states "No sealed sentence cancels the
   middle term, makes Phi covariantly constant, or sets Phi^dagger Phi = 1."  (F) buys the flat
   parent multiplicity and C2_parent scalar on the irreducible 16; it does NOT make the unselected
   finite map Phi act as one scalar on all 16 internal directions.
TIER3 = (F)+(S)+(U) displayed.  Under (F) AND (S), radii EXPLICIT: Tr f(H_0) = SUM_(p_t,p_q)
   2 N_lattice(p_t,p_q) · SUM_(ell>=0) d_S2(ell) · 16 · f(p_t^2/R_T^2 + p_q^2/R_Q^2 +
   ell(ell+2|q|)/r_flux^2 + mu^2 + C2_parent).  Under (U) the three denominators drop.  N_lattice
   carried explicitly and NOT absorbed; it remains OPEN in the register.
MEMBER_BOUNDS = conditioned true.  lambda >= C2_parent consumes NOTHING — not (F), not (S), not
   (U), not the radii — and is PROVED of record (Q-690); cited, not re-derived.  lambda_A >=
   P_min + 1/r_flux^2 + C2_parent and lambda_B >= P_min + 0 + C2_parent each consume (F) (without
   it the parent factor is twisted and "the spectrum itself changes, not merely the count") and
   are unconditional in Phi; radii explicit, so no (U).  THE SEPARATION IS 1/r_flux^2, NOT 1 — a
   free datum (D9/S28), not a pure number.  The exact bottoms remain NOT ESTABLISHED (778).
FREEDOMS_CONSUMED = f CARRIED-AS-UNSELECTED (omitted entirely from 781's block) ; R_T, R_Q,
   r_flux CARRIED-AS-PARAMETER and CONDITIONED-ON via (U) at the five named sites ; Phi
   CARRIED-AS-PARAMETER at tier 1 and both member bounds, CONDITIONED-ON via (S) at tier 3 ;
   parent bundle and characteristic class CONDITIONED-ON via (F) at tier 2, tier 3 AND BOTH MEMBER
   BOUNDS (the attachment omitted at 781) ; C2_parent value CARRIED-AS-PARAMETER ; spin structure
   on T2_TQ (hence Lambda and P_min) CARRIED-AS-PARAMETER ; bundle class / chiral index n
   CARRIED-AS-PARAMETER ; N_lattice CARRIED-AS-PARAMETER.  SUBSTITUTED: NONE.
FLATTENING_CHECK = clean, run against DECLINE_REGISTER_V002 (S01–S37), not the superseded V001.
   37 rows walked; 3 live: S27 (LOAD-BEARING — the grant is of flat x16 MULTIPLICITY, which is
   precisely why it does not license extracting 16 from a trace containing Phi^dagger Phi; the
   grant's own wording refuses the use 781 made of it), S28 (all five free data tagged in the
   freedoms block; none constrained), S01/D1 (mu^2 = 1 displayed only as declined, consumed
   nowhere; 783 concurs).
SALVAGE = 16 items dispositioned individually, nothing carried silently.  STAND (11): tier-1
   functional; lambda >= C2_parent (UPGRADED CLAIMED -> PROVED, Q-690); N_lattice explicit;
   D1 consumed nowhere; U2/U5/U7 not reinstated; U1/U6/U9 survive; U3/U4 conditional; U8
   conditional but SHARPENED to four beta sectors; the 777 twelve-item table; R3/R4/DG-1;
   FC-a..FC-f and DG-2..DG-4 (FC-e now displayed in-formula).  RE-CONDITIONED (3): tier 2 (dropped
   as stated, replaced by the non-factoring surface); tier 3 (radii restored); member bounds
   (radii explicit, (F) attached, separation 1/r_flux^2).  DEAD AS WRITTEN (2): 781's
   freedoms-consumed block (omitted f, the radius specialization, the (F) attachment) and 781's
   flattening check (ran against the superseded V001; flagged to the registrar at 782 and re-run
   here against V002).
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+4): (1) I SET THREE FREE DATA TO 1 AND THEN WROTE "SUBSTITUTED:
   none" — the freedoms block was not merely incomplete, it was FALSE AS WRITTEN, in the one
   direction an auditor cannot see from the block alone; (2) the A-B separation has been restated
   at too high a grade in THREE CONSECUTIVE RELAYS (777 bottoms -> 781 bounds -> here, radii),
   each pass correcting the qualifier it went looking for and preserving the number 1 untouched —
   a quantity that survives several corrections starts to read as established, and the surviving
   part was the part nobody had re-derived; (3) I misused a conditional grant by reading its
   consequence instead of its wording — S27 grants flat x16 MULTIPLICITY and never licensed
   factoring 16 out of a trace containing Phi^dagger Phi; (4) f has never appeared in any freedoms
   block I have written, although every trace consumes it, and 783 found it rather than I.
   All four run against my own work and none creates a result.  THE PATTERN SHIFTED: at 781 the
   failure was PROPAGATION (a correction that did not travel); here it is CONDITIONING (formulas
   true under conditions I held implicitly while asserting I had not used them).  Both are
   bookkeeping, not reasoning, and both were caught by the other lane rather than by me.
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
