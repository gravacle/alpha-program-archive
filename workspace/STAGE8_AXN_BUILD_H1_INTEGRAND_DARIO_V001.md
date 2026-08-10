# STAGE 8 / [PLAN:AXN-BUILD-A9] — H1'S INTEGRAND, ON THE CORRECTED SHAPE
## DARIO LANE (Builder B) — V001

RELAY 842 (re-invoked; the first pickup stopped cleanly at the gate and produced nothing).
Lane guard PASS (DARIO). Inbox = `51b269611c83f7d3…`, seal verified BEFORE reading, unchanged on
re-pickup. State brief `e26f0d16055f3e83…` verified and read. Charter `c0ad6decf156ef06`, seal OK.

**GATE: OPEN, AND IT RETURNS CORRECTIONS, NOT CONFIRMATION.**
`STAGE8_AXN_BUILD_ROUND1_CROSSCHECK_CODEX2_V001.md` = `886cd9a36b66f358`, `.md.seal` OK, verified
BEFORE reading. The relay's alternative branch applies — *"or apply its corrections first"* — and
**§1 applies them before anything is derived.**

GATES: `alpha_computed = false`; `proof_authorized = false`; `kappa_record_computed = false`.
**DERIVE-NEVER-SELECT ABSOLUTE.** No smooth import; no EM identification. PE-1..PE-11 pointer-only.
**ALL HEADLINE ITEMS CLAIMED.**

---

## 1. CORRECTIONS APPLIED FIRST — AND THEY CHANGE WHAT THE TASK IS

The cross-check returns four results that bear on this relay, and one of them **dissolves the task as
posed.** All adopted; none defended.

**(1a) A SIXTEENTH CENSUS ROW — `I6 SLOT9_F2_EXCLUSION_THEOREM`.** My V3 claimed completeness against
838's list and warned in the same breath that this was *"NOT proof that no SIXTEENTH row exists."*
**The warning landed.** Census is now 16 rows and, per the cross-check, **16 remains a lower bound,
not no-outside closure.** I6 is unpressed.

**(1b) THE ORDERING INVERSION — PARTIALLY CORRECTED.** I claimed AS1 cannot precede AS2. The
cross-check: *"partial evaluation lawful (full PASS/stratum selection blocked by H1; clause-local
constraints and H3 exclusion remain evaluable)."* **My claim was too strong.** The blockage is on the
*full* PASS and stratum selection, not on all evaluation — and the proof is H3, which was decidable
and got decided.

**(1c) `chi_P` IS DECIDED, NOT MERELY NARROWED.** `chi_P = 0` on the sealed packet-parent branch, by
the vertex comparison I declined to perform and correctly assigned to LEG A. Branch-scoped: a
*generated square-level* Pauli structure and a *global* Pauli-exclusion theorem remain distinct
objects. **Corrected tally: 1 decided / 3 narrowed / 7 unmoved, plus I6 unpressed.**

**(1d) `K_R` — MY "NOT RULING-SHAPED" IS CORRECTED.** UNMOVED is confirmed, and the triple bar
(S03 construction end / C7 response end / S25 rescaling) does block lane, response and rescaling
selection — **but the sealed release condition RESERVES PRINCIPAL RE-RULING.** I wrote that *"a
freedom the instrument cannot reach is not thereby a freedom a ruling should fill."* That over-read:
S03's release branch (c) exists precisely for a principal re-ruling, and I do not get to close it.
**Withdrawn.**

**(1e) `BOX_gravity` DECLINATION — CONFIRMED.** *"background g is reached; no gravitational-action or
measure receiver is."* My declination of the relay's suggested direction stands.

### 1.6 THE CORRECTION THAT DISSOLVES THE TASK AS POSED

The cross-check re-binds all six H1 constraints. The decisive move is that **five of six bind the
OUTPUT of the variation, not the action integrand:**

| # | my round-1 reading | cross-check's binding |
|---|---|---|
| 1 | `BOX_record` is a sum over primitive incidences; cannot be nonlocal | **OVERBOUND.** CIS constrains every **primitive incidence component**; it *"neither defines all of `S_record` as `sum_c L_c` nor bans every nonlocal effective contribution"* |
| 2 | one-use on new record factors | **CONFIRMED AT PRIMITIVE SCOPE** — not a statement about every term in the full record functional |
| 3 | carries `w(s)`, no fitted profile | **CONFIRMED AT THE RECEIVER, NOT AS LITERAL ACTION CONTENT.** *"The clauses do not require the action integrand literally to contain `w(s)`"* |
| 4 | first-order restriction supplies `D_rec/inc` | **CONFIRMED AS AN OUTPUT TEST.** *"This does not fix the action functional's own domain"* |
| 5 | square-generated descendants, no independent coefficient | **A MANDATORY SUBSET, NOT A COMPLETE INVENTORY.** U3 open, so *"descendant inventory fixed" is false* |
| 6 | exact completed-record persistence | **A PASS CONDITION** — *"neither selects an action normalization nor supplies the still-open durability map"* |

**And the withdrawal is explicit:** *"the claims that domain, descendant inventory, and cell coupling
are fixed at the action-functional level, and that normalization is thereby supplied, are
withdrawn."*

**My 840 verb audit flagged the `w(s)` line as the weakest joint and predicted the failure mode:
"clause 2 could instead be read as constraining only the PACKET's profile."** That is exactly
correction (3). The instinct was right; I took the stronger reading anyway and sealed it.

---

## 2. AS1 — THE SYSTEM, POSED HONESTLY

The relay directs: *"pose the constraint system on the per-cell term space; solve exactly."*

**On the corrected binding, that system cannot be posed on that space.** Five of the six constraints
are conditions on `delta S`'s output — the reproduced first-order parent, its envelope, its
descendants, its persistence. **The integrand lives in the domain of the variation; the constraints
live in its image.** Pulling image-constraints back to domain-constraints requires the map between
them.

```text
POSED SYSTEM (corrected):

  DOMAIN            the space of admissible record-sector integrands  S_record
  MAP               delta : S_record  |-->  (output operators, envelope, descendants, persistence)
                    == U1, the action-to-operator/variation map
  IMAGE CONSTRAINTS C2..C6  (envelope unfitted; first-order receiver D_rec/inc; mandatory
                    square-generated overlap/closure subset with no independent coefficient;
                    exact completed-record persistence)
  DOMAIN CONSTRAINT C1 only, and only on the PRIMITIVE SECTOR:
                    per primitive incidence c, one Omega_c, one L_c, support(L_c) subset Omega_c,
                    one-use, on new record factors.

  TO SOLVE FOR THE INTEGRAND one needs  delta^{-1}(image constraints), i.e. THE PULLBACK.
  THE PULLBACK REQUIRES U1 DEFINED ON THE CLASS, NOT ON A GIVEN CANDIDATE.
```

### 2.1 What the one domain-level constraint actually gives — and what it does not

C1 is a genuine integrand-level constraint: `support(L_c) ⊆ Omega_c` is a statement about the
interaction density itself. **But it constrains SUPPORT, not FORM.** It localizes each primitive term
to its cell and forbids reuse; it says nothing about what the term *is* on that cell. And per
correction (1), it does not even claim to exhaust `S_record`:

```text
S_record  =  [ primitive sector ]        support-localized by CIS, FORM-FREE
           +  [ effective / nonprimitive remainder ]   EXPRESSLY PERMITTED BY CIS, UNCONSTRAINED HERE
```

So even the sector C1 reaches is not solved, and the sector it does not reach is not bounded.

---

## 3. AS2 — THE SOLVE

**`INTEGRAND = UNDECIDABLE`, and the missing object is nameable exactly.**

Not `UNIQUE`: no constraint determines a functional form.
Not `FAMILY`: I cannot give a dimension or a parametrization, because the effective remainder is
unenumerated and C1 constrains support rather than form. Reporting a dimension would be fabrication.
**Not `EMPTY`, and this matters:** there is no certificate of non-existence — the situation is the
opposite, an unbounded admissible set. Calling it EMPTY would be a route-level kill the evidence does
not support.

```text
MISSING OBJECT, NAMED:
  a VARIATION SCHEME DEFINED ON THE ADMISSIBLE CLASS — U1 as a map on the class of admissible
  record-sector integrands, not the variation of one supplied candidate.
  WHY EXACTLY THIS: image-constraints pull back to domain-constraints only if the map is defined on
  the domain class.  A per-candidate U1 can TEST a supplied integrand against C2..C6; it cannot
  SOLVE for one.
```

### 3.1 The circularity, which is the round's structural finding — CLAIMED

```text
MY ROUND 1:      U1 is gated on H1  (the map cannot be applied: no candidate action, because
                                     BOX_record has no content)
CORRECTED H1:    H1's integrand is gated on U1  (the constraints are image-side; solving for the
                                     integrand needs the pullback)

                 ==>  U1 <-> H1 IS CIRCULAR.
```

Neither can be produced from the other, and **the loop is not broken by more pressure of this kind.**
Two exits exist and I display both without taking either:

```text
EXIT-A  an integrand supplied from OUTSIDE this constraint system (another sealed route), after
        which U1 becomes applicable and C2..C6 become TESTS rather than a system to solve.
EXIT-B  U1 promoted from a per-candidate variation to a CLASS-WIDE SCHEME, after which the pullback
        exists and C2..C6 become genuine integrand constraints.
        EXIT-B is the one that would make this relay's task well-posed.
```

**Neither is selected. EXIT-B is not a freedom I may fill: constructing a class-wide variation scheme
is construction, and the charter's stop-on-freedom law says stop and display.**

### 3.2 `DURABILITY_MAP`

**Still open, and now known to be downstream of the same gap.** Correction (6): C6 *"neither selects
an action normalization nor supplies the still-open durability map."* The durability map is an
output-side object; reaching it from the integrand needs the same pullback. **UNMOVED, same missing
object.**

---

## 4. AS3 — WHAT FOLLOWS FOR THE STRATUM AND U1

```text
STRATUM   unchanged: NONE predicate-selected.  Round 1's blockage stands, but with correction (1b):
          the block is on FULL PASS and STRATUM SELECTION.  Partial, clause-local evaluation IS
          lawful — and H3/chi_P is the worked proof of it, now DECIDED at chi_P = 0 on the sealed
          packet-parent branch.
U1        status upgraded in precision, not in progress: not merely "gated on H1" but MUTUALLY GATED
          with it.  The build's forcing instrument cannot break the loop from either side.
CENSUS    16 rows (15 + I6), and 16 IS A LOWER BOUND, NOT CLOSURE.
TALLY     1 decided (H3) / 3 narrowed (H1 re-scoped, H4, H5) / 7 unmoved / I6 unpressed.
```

**What round two needs, restated on the corrected shape:** not "the integrand" — that is not
derivable from this system — but **EXIT-A or EXIT-B**, i.e. either an integrand from another sealed
route, or a class-wide variation scheme. **Everything this relay was asked to compute sits behind one
of those two, and both are construction objects rather than pressure results.**

---

## 5. FREEDOMS-CONSUMED · FLATTENING CHECK

```text
CARRIED, NOT CONSUMED: all six H1 constraints AT THE CROSS-CHECK'S CORRECTED BINDINGS, not mine;
  the primitive/effective split CARRIED AS CIS STATES IT, with the effective sector NOT bounded;
  chi_P = 0 CARRIED AS THE CROSS-CHECK DECIDES IT, branch-scoped, and NOT generalized to a global
  Pauli-exclusion theorem; K_R UNMOVED WITH PRINCIPAL RE-RULING EXPRESSLY RESERVED; I6 carried
  unpressed; EXIT-A and EXIT-B both displayed, NEITHER TAKEN.
DERIVED HERE: nothing.  No integrand, no functional form, no per-cell term, no normalization, no
  durability map, no dimension, no parametrization, and NO CERTIFICATE OF EMPTINESS.
WITHDRAWN HERE (mine, from round 1): "domain, cell coupling and descendant inventory are FIXED";
  "normalization is CONSTRAINED"; the literal-w(s) reading of the integrand; "BOX_record is a sum
  over primitive incidences and cannot be nonlocal"; "AS1 cannot precede AS2" (too strong — partial
  evaluation is lawful); and "a freedom the instrument cannot reach is not thereby a freedom a ruling
  should fill" (K_R's principal re-ruling is reserved by the sealed release condition).
SCALING WEIGHTS (law 2a): NONE CONSUMED.  SUBSTITUTED: NONE.
```

**FLATTENING CHECK — 37 rows walked.** **S03 and the void condition are the live rows and they are
load-bearing here**: this relay asked for an integrand, and the tidy move — writing a plausible
per-cell term that satisfies the six constraints — is precisely what the corrected binding shows is
*not* determined. **No integrand is written, and no dimension is invented to dress UNDECIDABLE as
FAMILY.** **S12**: every correction is cited to the cross-check's clause, not to a status word.
**S26/S08** untouched. **S19/S24** untouched — no decay or clustering assumption is used to bound the
effective sector; it is left unbounded.
`FLATTENING_CHECK = clean (37/37; S03 and the void condition live at the integrand).`

## 6. SELF-AUDIT

**VERB AUDIT: NOT CLEAN (+4).**

**(1) MY OWN FLAG PREDICTED THE CORRECTION AND I SEALED THE STRONGER READING ANYWAY.** At 840 I wrote
that the `w(s)` line "could instead be read as constraining only the PACKET's profile" and flagged it
for attack first. Correction (3) is exactly that. **Predicting a failure mode and then committing to
the reading anyway is the same error I recorded at 834** — flagging a hazard is not declining to walk
into it. **Second occurrence, and the charter's stop-on-freedom law is the rule I keep brushing.**

**(2) FOUR OF MY SIX H1 CLAIMS WERE OVER-BOUND, AND THE PATTERN IS ONE-DIRECTIONAL.** Every
over-reach bound an *output* condition to the *action*. That is a systematic direction of error, not
four independent slips: I was reading a reproduction condition as a construction constraint
throughout.

**(3) THE ONE THING I DECLINED TO DO IS THE ONE THING THAT GOT DECIDED.** I assigned the vertex
reading to LEG A rather than performing it, and LEG A performed it and decided `chi_P = 0`. **The
declination was correct on custody and cost the round its only decided row.** Both are true and I
record both rather than claiming the caution as a virtue.

**(4) THE RELAY ASKED FOR A DERIVATION AND I RETURN A CIRCULARITY.** That is the honest answer on the
corrected binding, but I note the alternative I rejected: with the *uncorrected* H1 I could have
posed a per-cell system and produced *something*. It would have been a solution to a system whose
binding the opposite lane had just withdrawn. **The gate's value was not procedural — it changed the
answer.**

---

```
SYSTEM = posed (constraints, spans) — BUT NOT ON THE PER-CELL TERM SPACE THE RELAY NAMES
  On the cross-check's corrected binding (886cd9a36b66f358 §3), FIVE OF SIX constraints bind the
  OUTPUT of the variation, not the action integrand: the envelope is "CONFIRMED AT THE RECEIVER, NOT
  AS LITERAL ACTION CONTENT" and "the clauses do not require the action integrand literally to
  contain w(s)"; the first-order restriction is "AN OUTPUT TEST" that "does not fix the action
  functional's own domain"; the descendants are "A MANDATORY SUBSET, NOT A COMPLETE INVENTORY";
  persistence is "A PASS CONDITION" that "neither selects an action normalization nor supplies the
  still-open durability map".  The cross-check withdraws my claims that domain, descendant inventory
  and cell coupling are fixed at action-functional level and that normalization is thereby supplied.
  ONLY C1 IS DOMAIN-LEVEL, and only on the PRIMITIVE sector: support(L_c) subset Omega_c, one-use, on
  new record factors — WHICH CONSTRAINS SUPPORT, NOT FORM.  CIS expressly permits an effective /
  nonprimitive remainder that this system does not reach.

INTEGRAND = UNDECIDABLE (object named)
  NOT UNIQUE: no constraint determines a functional form.  NOT FAMILY: I can give no dimension or
  parametrization — the effective remainder is unenumerated and C1 constrains support rather than
  form, so a dimension would be fabricated.  NOT EMPTY, AND THAT MATTERS: there is no certificate of
  non-existence; the admissible set is UNBOUNDED, and an EMPTY verdict would be a route-level kill
  the evidence does not support.
  MISSING OBJECT: A VARIATION SCHEME DEFINED ON THE ADMISSIBLE CLASS — U1 as a map on the class of
  admissible record-sector integrands, not the variation of one supplied candidate.  Image
  constraints pull back to domain constraints only if the map is defined on the domain class; a
  per-candidate U1 can TEST a supplied integrand against C2..C6 but cannot SOLVE for one.
  *** THE STRUCTURAL FINDING: U1 <-> H1 IS CIRCULAR.  My round 1 had U1 gated on H1 (no candidate
  action because BOX_record is empty); the corrected H1 has the integrand gated on U1 (the pullback).
  Neither is producible from the other, and MORE PRESSURE OF THIS KIND DOES NOT BREAK THE LOOP.
  TWO EXITS DISPLAYED, NEITHER TAKEN: EXIT-A an integrand supplied from another sealed route, after
  which C2..C6 become TESTS; EXIT-B U1 promoted to a CLASS-WIDE SCHEME, after which the pullback
  exists and C2..C6 become genuine integrand constraints.  EXIT-B would make this relay's task
  well-posed, and constructing it is CONSTRUCTION — stop-on-freedom applies. ***

DURABILITY_MAP = still open, and now known to be DOWNSTREAM OF THE SAME GAP — an output-side object
  reachable from the integrand only through the same missing pullback.  UNMOVED, same missing object.

STRATUM/U1 = STRATUM unchanged (NONE predicate-selected), with round 1's inversion CORRECTED: the
  block is on FULL PASS and STRATUM SELECTION only — partial clause-local evaluation IS lawful, and
  H3 is the worked proof, now DECIDED at chi_P = 0 on the sealed packet-parent branch (branch-scoped;
  a global Pauli-exclusion theorem remains a distinct object).  U1 upgraded in PRECISION, NOT
  PROGRESS: not merely "gated on H1" but MUTUALLY GATED with it.
  CENSUS now 16 rows (my 15 + I6 SLOT9_F2_EXCLUSION_THEOREM), and SIXTEEN IS A LOWER BOUND, NOT
  CLOSURE — my V3 warned a sixteenth row could exist and it does.  CORRECTED TALLY: 1 decided /
  3 narrowed / 7 unmoved / I6 unpressed.
  ROUND 2 NEEDS EXIT-A OR EXIT-B, not "the integrand" — everything this relay was asked to compute
  sits behind one of the two, and both are CONSTRUCTION objects, not pressure results.

CHAIN_INVOKED = false

VERB_AUDIT_SELF = NOT CLEAN (+4)
  (1) MY OWN 840 FLAG PREDICTED CORRECTION (3) AND I SEALED THE STRONGER READING ANYWAY — the same
      error I recorded at 834.  SECOND OCCURRENCE; flagging a hazard is not declining to walk into it.
  (2) FOUR OF MY SIX H1 CLAIMS WERE OVER-BOUND IN ONE DIRECTION — every over-reach bound an OUTPUT
      condition to the ACTION.  A systematic misreading of a reproduction condition as a construction
      constraint, not four independent slips.
  (3) THE ONE THING I DECLINED TO DO IS THE ONE THING THAT GOT DECIDED — I assigned the vertex reading
      to LEG A and LEG A decided chi_P = 0.  The declination was right on custody AND cost the round
      its only decided row; both true, and I do not claim the caution as a virtue.
  (4) THE RELAY ASKED FOR A DERIVATION AND I RETURN A CIRCULARITY.  With the UNCORRECTED H1 I could
      have posed a per-cell system and produced something — a solution to a system whose binding the
      opposite lane had just withdrawn.  THE GATE'S VALUE WAS NOT PROCEDURAL; IT CHANGED THE ANSWER.

alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
