# STAGE 8 / 7A / STEP 7 — THE THOMSON CHAIN: SCOPING

Lane: DARIO (Builder B, independent verifier). Relay 758.
Governing: the handoff package `a0a7e1d1…` (SEALED-OK); the frozen prereg; Q-661's correction.
Scoping, not derivation. Nothing adopted.

## Lead determination

**The chain is fully specified of record and completely unbuilt — and it cannot be entered
where the relay points.**

`C7`, frozen in the ledger and carried verbatim in a sealed review, is the chain:

```text
S03 -> S04 -> S05 -> S06 -> S07 -> S08 -> S13 -> S16 -> S17,
and no later item may be used to select an earlier one.               (C7)
```

`S16` is *"threshold-conditioned Thomson matching"*; `S13` is *"interacting charged pole or
infraparticle threshold"*. The conditioning the relay names is **C7's own**: `S16` sits
immediately downstream of `S13`, and **C7 forbids using `S16` to select `S13`.**

**Status: 0 of 18 slots filled, all TYPE-U** (road V002, step 10: *"the charged Q-spec
(A23/A24/A28; **V005 0/18**)"*). Every link of C7's nine is absent, including its head.

**So the first target cannot be `S16` or `S13`.** Entering at either would be exactly the
selection C7 bars, and everything upstream is unbuilt. **By the chain's own law the first
target is `S03`, the dynamical U(1) action.**

**And AJ2's premise does not survive the census.** Q-126's source — the beta closure hunt
`04c10c0d…`, sealed, four adversarial verifiers CONFIRMED — names the beta-sensitive junctions
exactly three:

- **the fiber proper radius `R` in `K_KK`** — **ADOPTED** ansatz; `K_KK` changes by `beta^2`
- **the complete normalized `D_BR` spectrum** — **UNBUILT**
- **the skeleton-to-cell embedding**, where the `4 pi`-class factors enter and which *"has never
  been attempted"* — **GAP**

**The word "Thomson" does not occur in that file at all.** No Thomson-chain link is named
beta-sensitive of record — and the census could not have named one, since it enumerates the
**thirteen sealed** interface quantities and every Thomson link is unbuilt. **Whether a derived
`S16` would be beta-sensitive is UNDETERMINED of record**, and the three grounded candidates for
Q-126's conjunction lie elsewhere.

---

## 0. Preflight

### 0.1 Output name

Probed **before any write**, recursively: **absent**, artifact and sidecar both.

### 0.2 Sources verified before use

```text
HAND   workspace/STAGE8_7A_HANDOFF_PACKAGE_V001.md                          a0a7e1d1…  SEALED-OK
ROAD2  workspace/ROAD_FROM_HERE_THROUGH_GRAVITY_V002.md                     b1ecae48…  SEALED-OK
ROAD1  workspace/ROAD_FROM_HERE_THROUGH_GRAVITY_V001.md                     9644e0cd…  SEALED-OK
REV    workspace/STAGE8_TASK6_LP_QSPEC_ASSEMBLY_REVIEW_LANE3_V001.md        f8bfff5b…
BETA   workspace/STAGE8_RECORD_CELL_SURFACE_AND_BETA_CLOSURE_HUNT_EINSTEIN_V001.md  04c10c0d…  SEALED-OK
BID    workspace/BID_CONSOLIDATED_HOSTILE_AUDIT_MATRIX_V005.md              78f6bb08…  NO SIDECAR
LPL    workspace/STAGE8_TASK6_LP_MATRIX_LEDGER_LANE3_V001.md                bc6c3e49…  SEALED-OK
REG    supervision/QUESTIONS_SETTLED_REGISTER_V001.md                       1ad7f0bd…  SEALED-OK
CARR   workspace/STAGE8_7A_R9JII_JOINT_LANDING_TEST_V001.md                 5f4979d5…  SEALED-OK
```

**Searched space:** recursive glob `./workspace/**/*.md` + `./supervision/**/*.md`, run **from
the archive root**, with `kappa_record` (1551) and `A28` (130) as known-positive controls and
the corpus size printed — the practice installed after 755.

**A defect in my own standing rule, found and fixed this relay.** The WRITER-EXCLUSION RULE I
installed at 725 has been implemented throughout as `*_DARIO_V001.md`. The archive holds **199**
Dario artifacts, including `…_DARIO_V003.md`, which that pattern **does not catch**. Corrected
here to exclude every `_DARIO_` file: **1,964 files** searched. One consequence is recorded in
§1.2 — a status line I would otherwise have cited as corpus is my own lane's.

### 0.3 Gates

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
No member binding.  No fixed-point execution.  No end test.  No numeric evaluation of
physical quantities.  No comparison to measured constants.  No common cell formed.
No junction map evaluated.  No smooth data derived.  Nothing adopted.
No register, plan, tracker, or git action.
```

---

## 1. AJ1 — THE CHAIN'S DEMAND STRUCTURE

### 1.1 The chain of record

[PROVABLE] `REV` `f8bfff5b…`, quoting the ledger's frozen order at its lines 142–156:

```text
S03 -> S04 -> S05 -> S06 -> S07 -> S08 -> S13 -> S16 -> S17,
and no later item may be used to select an earlier one.               (C7)
```

`REV` adds: *"The assembly quotes the same nine members in the same order and correctly uses C7
as an anti-selection rule."*

[YOURS] **C7 is two things at once** — a dependency order and an **anti-tuning instrument**. The
second is the operative one for scoping: it makes the chain enterable **only from the head**.

### 1.2 The eighteen slots, and their status

[PROVABLE] `REV` `f8bfff5b…` carries the governing ledger text for all eighteen. The nine on the
chain:

| Slot | Governing ledger text |
|---|---|
| S03 | `dynamical U(1) action` |
| S04 | `gauge fixing, ghosts, and gauge edge modes` |
| S05 | `normalized interacting CTP amplitude` |
| S06 | `parent-derived functional regulator and finite renormalization` |
| S07 | `induced-polarization transversality and photon-mass exclusion` |
| S08 | `Lorentz- and packing-independent renormalized response` |
| **S13** | **`interacting charged pole or infraparticle threshold`** |
| **S16** | **`threshold-conditioned Thomson matching`** |
| S17 | `CISP descendant test in the interacting outgoing sector` |

[PROVABLE] **Status: every link absent.** `ROAD2` `b1ecae48…`, step 10: *"The charged Q-spec
(A23/A24/A28; **V005 0/18**)"*. And `LPL` `bc6c3e49…[46365,46418)`:
`| A28 | BLOCKED | complete downstream Qspec absent |`.

[YOURS, **writer-flagged**] A prior artifact of my own lane records the same at finer grain —
`SLOTS = 18 (0 filled / 18 TYPE-U)`, `THOMSON = TYPE-U (S16; MISSING_SPECIFICATION, transport
UNDETERMINED)`. **It is Dario's, so it corroborates nothing here**; I cite it only to note that
the finer status exists and is my lane's, not the corpus's. The `0/18` above stands on `ROAD2`
and `LPL`, both non-Dario and sealed.

### 1.3 S16 and S13's conditioning demands

[PROVABLE] **The conditioning is in `S16`'s own name.** *"**Threshold-conditioned** Thomson
matching"* — the matching is conditioned on a threshold, and `S13` is the threshold slot:
*"interacting charged pole or infraparticle threshold"*. `C7` places `S13` immediately before
`S16` and bars using `S16` to select it.

[YOURS] So the demand pair is: **`S13` must fix the threshold — a charged pole or an
infraparticle threshold — independently, and `S16` must then perform the Thomson matching
conditioned on whichever `S13` returns.** The disjunction in `S13` is load-bearing: *pole* and
*infraparticle* are different kinematic situations, and `S16`'s conditioning has to cover the
case `S13` actually delivers, not a chosen one. That is exactly what C7's anti-selection rule
protects.

[PROVABLE] **`S14` and `S15` are not on C7's chain** — `complete charged-species and threshold
map` and `enlarged-branch exhaustion` — though `S14` is plainly threshold-adjacent. C7's nine
are the frozen chain; the other nine slots are demands of the Q-spec but not of this order.

### 1.4 The A28 firewall

[PROVABLE] `BID` `78f6bb08…[11932,12673)` — the row is **PENDING** and the file carries **no
sidecar**, so it is cited as the criterion text of record with that flagged:

```text
| A28 | Primitive/full charged separation | The primitive gate may use no determinant,
heat kernel, Wick rotation, regulator, counterterm, threshold, or source-mass
identification and may output only `kappa_record`. A distinct downstream `Q_spec` must
use one global fermionic CAR source algebra plus distinguishable record factors, and
include the spatial Dirac kinetic operator, charged current, antiparticles, gauge/ghost/
edge sectors, connected gluing and overlap terms, CTP preparation, durability,
measure/regulator, Ward identity, full source pole/residue, induced transverse response,
thresholds, decoupling, matching, and the zero-momentum Thomson limit. Only
`kappa_Thomson` may enter `alpha(0)=1/(4pi kappa_Thomson)`. | PENDING |
```

[YOURS] **What A28 requires of every link, stated as the firewall it is.** It is a *separation*,
enforced in both directions:

1. **Upward.** The primitive gate may use **no threshold** and **no matching**, and may output
   **only `kappa_record`**. So nothing in the Thomson chain may be reached back into the
   primitive gate — `S13`'s threshold and `S16`'s matching are named among the very things the
   gate may not use.
2. **Downward.** *"Only `kappa_Thomson` may enter `alpha(0)=1/(4 pi kappa_Thomson)`."* So the
   chain's terminal object is the **only** licensed entrant to the alpha map. `kappa_record`
   does not enter it; nor does any intermediate of `S03`–`S17`.
3. **The chain must be carried whole.** A28 lists thresholds, decoupling, matching and the
   zero-momentum Thomson limit as required contents of the *distinct downstream* `Q_spec`. A
   partial chain does not partially satisfy A28; A28 is `BLOCKED` on *"complete downstream Qspec
   absent"*.

---

## 2. AJ2 — THE BETA-SENSITIVITY QUESTION

### 2.1 What the census actually says

[PROVABLE] `BETA` `04c10c0d…`, sealed, the source behind Q-126 — and Q-126 records that **all
four adversarial verifiers returned CONFIRMED with citation-span corrections only**:

```text
- DERIVED junctions — all beta-blind: … the marker |Delta S_record| = pi hbar
  (action x phase); m_* T_R = pi (the brief's one "cross-geometry lock", mass x
  interval — contains no R, trivially beta-invariant); the balanced-geodesic
  identities; the onset inequality.
- beta-SENSITIVE junctions — none derived: the fiber proper radius R in K_KK
  (ADOPTED ansatz; K_KK changes by beta^2); the complete normalized D_BR spectrum
  (UNBUILT); the skeleton-to-cell embedding — where the brief says the 4 pi-class
  factors enter and which "has never been attempted" (GAP).
```

**Three beta-sensitive junctions, named, with their exact statuses: ADOPTED, UNBUILT, GAP.**

### 2.2 The Thomson chain is not among them

[PROVABLE] **`Thomson` occurs zero times in `BETA`.** I checked the file directly, not by
proximity. No Thomson-chain link is named beta-sensitive of record.

[YOURS] **And the census could not have named one.** Its subject is *"the **thirteen sealed**
interface quantities on the record cell"*. Every Thomson-chain link is TYPE-U and unbuilt, so
none is a sealed interface quantity. The census's silence on Thomson is a **scope fact, not a
finding against it**.

### 2.3 The premise, tested

[YOURS] The relay's context states that step 7 *"is its expected feeder"* for Q-126's
conjunction. **That expectation is not grounded in the census**, which names three candidates,
none of them on the chain. It is not refuted either: a derived `S16` would be a *new* junction
outside the thirteen.

[YOURS] **What would make `S16` beta-sensitive, stated as a reason and not a finding.** Thomson
matching lands a record-side quantity on a spacetime cross-section — an **area**. Converting to
a spacetime length is precisely what `beta` does (`R = beta c Delta tau`, the record cell's
internal/external conversion). So a derived `S16` is a natural place for `beta` to appear.
**This is an argument, not a sealed ground, and I book nothing on it.**

### 2.4 An instrument note, because the number looks like evidence and is not

[YOURS] A proximity probe for `Thomson` within 320 characters of `beta`/`length normalization`
returns **184 files**. Reading them, they are **almost entirely fence boilerplate** — *"No
alpha, `kappa_record`, `kappa_Thomson`, coupling, scale, root, eigenvalue, **beta function** …
was computed"*. The match is on *"beta function"* inside a declaration that nothing was
computed. **184 is a false-positive class, not support for a Thomson–beta link**, and I report
it as such rather than let a count stand in for a reading.

### 2.5 Verdict

```text
BETA_SENSITIVITY = candidate links named (grounds displayed).
  OF RECORD, on the chain:            NONE.  Thomson occurs zero times in the census.
  OF RECORD, off the chain:           THREE — R in K_KK (ADOPTED, K_KK changes by
                                      beta^2); the normalized D_BR spectrum (UNBUILT);
                                      the skeleton-to-cell embedding (GAP, "has never
                                      been attempted").
  S16 IF DERIVED:                     UNDETERMINED of record; a reason to expect
                                      beta-sensitivity is displayed at section 2.3 and
                                      is not booked.
```

[YOURS] **The scoping consequence, offered to the registrar.** If the goal is Q-126's
conjunction — a junction simultaneously **derived** and **beta-sensitive** — the Thomson chain is
the long way round: nine unbuilt links, entered only at the head, with the beta-sensitivity of
its terminal object undetermined. The census's own three candidates are each **one object**, and
one of them, the **skeleton-to-cell embedding**, is a GAP that has *"never been attempted"* — with
the brief's own guard attached (*"the diamond is a rich object; 'search until a ratio lands well'
is the numerology cliff"* — geometric ratios must be enumerated **blind**). **That is a shorter
route to the same conjunction, and it is not what step 7 is.**

---

## 3. AJ3 — DEPENDENCY ORDER, FIRST TARGET, EFFORT CLASSES

### 3.1 Dependency order

C7's, unchanged and frozen: `S03 → S04 → S05 → S06 → S07 → S08 → S13 → S16 → S17`, with **no
later item selecting an earlier one**.

### 3.2 First target — **`S03`**, and the justification is the chain's own law

[YOURS] Not `S16` and not `S13`, though those are what the relay names.

1. **C7 forbids it.** Entering at `S13` or `S16` and working back is precisely *"a later item
   used to select an earlier one"* — the anti-selection rule, and `REV` confirms the assembly
   uses C7 as such.
2. **Nothing upstream exists.** 0/18 filled; `S03`–`S08` are all TYPE-U. There is no partial
   chain to extend.
3. **A28 does not reward partial progress.** It is `BLOCKED` on *"complete downstream Qspec
   absent"* and requires the contents whole.

**`S03` — `dynamical U(1) action` — is the head, and the only lawful entry.**

### 3.3 Effort classes

| Target | Class | Basis |
|---|---|---|
| `S03` | **Large** — a dynamical action, the chain's head, with `S04`'s gauge/ghost/edge completion immediately behind it | C7 order; 0/18 |
| `S13` | **Gated** behind `S03`–`S08`; its own disjunction (pole *or* infraparticle) must be settled, not chosen | C7; `REV` slot text |
| `S16` | **Gated** behind `S13`; *threshold-conditioned* by name | C7; `REV` slot text |
| `R` in `K_KK` | **Medium, and adversarial** — replacing an **ADOPTED** ansatz with a derivation; a permission-shaped adoption cannot force, so the derivation must beat it outright | `BETA` |
| `D_BR` spectrum | **Large** — UNBUILT | `BETA` |
| skeleton-to-cell embedding | **Unknown, and guarded** — GAP, *"has never been attempted"*, numerology-cliff warning attached, ratios must be enumerated blind | `BETA` |

### 3.4 What this scoping does **not** do

[YOURS] It does not make R9-JII runnable. `CARR` §4's two entry conditions are **conjunctive**;
even a derived beta-sensitive junction leaves the **common-cell** condition open, and 757
established that identification is unsealed, guarded by an armed falsifier, and blocked below by
an unfixed complex. **Step 7 feeds one conjunct at most.**

---

## 4. GROUNDING, JURISDICTION, VERB AUDIT

### 4.1 Grounding

| # | Claim | Pin | Tag |
|---|---|---|---|
| 1 | C7's frozen nine-member order and anti-selection rule | `f8bfff5b…` §1.2 | PROVABLE |
| 2 | The eighteen slots' governing ledger text | `f8bfff5b…` §1.1 table | PROVABLE |
| 3 | `V005 0/18` | `b1ecae48…` step 10 | PROVABLE |
| 4 | A28 `BLOCKED`, "complete downstream Qspec absent" | `bc6c3e49…[46365,46418)` | PROVABLE |
| 5 | A28's criterion text and the `kappa_Thomson`-only firewall | `78f6bb08…[11932,12673)` (**no sidecar**) | PROVABLE |
| 6 | The three beta-sensitive junctions and their statuses | `04c10c0d…` | PROVABLE |
| 7 | `Thomson` = 0 occurrences in the census | direct file check | PROVABLE |
| 8 | Q-126's four verifiers CONFIRMED | `1ad7f0bd…` Q-126 | PROVABLE |
| 9 | Step 7 `[GATED]`; V001's "(S16, S13 conditioning)" parenthetical | `b1ecae48…`; `9644e0cd…` | PROVABLE |
| 10 | The 184-hit proximity probe is fence boilerplate | §2.4 | PROVABLE |
| 11 | First target `S03` and its justification | §3.2 | YOURS |
| 12 | Why a derived `S16` might be beta-sensitive | §2.3 | YOURS, **not booked** |

**Pin check: 12/12.**

### 4.2 Jurisdiction check

**On the relay's attribution.** The relay cites *"S16, S13 conditioning **per the road's own
line**"*. `ROAD2` — the current road, which supersedes V001 — carries **no such parenthetical**;
it is in `ROAD1` `9644e0cd…`. The attribution is accurate to V001 and stale to V002. **The
substance carries either way** (C7 supplies the conditioning independently), and I record the
provenance rather than repeat it unchecked.

**On A28.** *What was the rule written to protect?* A firewall between the primitive gate and the
charged Q-spec, so the alpha map is entered by exactly one object. The risk is live: a partial
chain that leaked an intermediate into `alpha(0)` would violate it silently. §1.4 states it in
both directions for that reason.

**On the VOID CONDITION.** Nothing chosen from a desired coefficient. §2.5's redirect names a
*shorter route to a conjunction*, not a route to a number, and §3.3 carries the brief's own
numerology-cliff guard on the one candidate where ratio-hunting would be the temptation.

**On BR-1.** The relay's context asserts step 7 *is* the expected feeder. I tested it against the
census rather than adopting it, and returned **undetermined** with the grounded alternatives
displayed. A commission may direct the work; it may not supply the finding.

**On R9 / R9-JII.** Untouched; §3.4 states explicitly that this scoping does not move the
carrier.

### 4.3 Self verb audit — **CLEAN, with four disclosures**

1. **My own standing WRITER-EXCLUSION rule was implemented too narrowly, for many relays.**
   `*_DARIO_V001.md` misses the 199-file Dario set's other versions. Fixed here; §1.2 records the
   one place it mattered, where a finer status line I might have cited as corpus is my lane's.
   The rule was mine, installed at 725, and the implementation defect is mine too.
2. **A 184-file proximity result that is not evidence** (§2.4). Counting would have supported a
   Thomson–beta link; reading showed fence boilerplate. Reported as a false-positive class.
3. **The relay's premise is not supported and I say so first**, rather than scoping the chain as
   though the feeder claim were settled.
4. **`BID` carries no sidecar** and is nonetheless the only place A28's criterion text appears in
   full. Cited with the gap flagged, and the row's *status* taken from the sealed `LPL` instead.

---

```text
CHAIN = mapped (links + statuses).  The chain of record is C7, frozen in the ledger and
    carried verbatim at f8bfff5b...: S03 -> S04 -> S05 -> S06 -> S07 -> S08 -> S13 ->
    S16 -> S17, "and no later item may be used to select an earlier one" — a dependency
    order AND the assembly's anti-tuning instrument.  STATUS: every link absent —
    V005 0/18 (ROAD2 b1ecae48..., step 10), A28 BLOCKED on "complete downstream Qspec
    absent" (LPL bc6c3e49...[46365,46418)).
S16_S13 = demands displayed.  S16 = "threshold-conditioned Thomson matching"; S13 =
    "interacting charged pole or infraparticle threshold".  The conditioning is C7's:
    S13 immediately precedes S16 and may not be selected by it.  S13's disjunction is
    load-bearing — pole and infraparticle are different kinematics, and S16 must
    condition on whichever S13 returns, not on a chosen one.  A28's firewall runs BOTH
    ways: the primitive gate may use "no ... threshold ... or source-mass identification"
    and "may output only kappa_record"; downstream, "Only kappa_Thomson may enter
    alpha(0)=1/(4pi kappa_Thomson)".
BETA_SENSITIVITY = candidate links named (grounds displayed).  ON THE CHAIN: NONE of
    record — "Thomson" occurs ZERO times in the sealed census 04c10c0d..., and the
    census could not name one, since its subject is the THIRTEEN SEALED interface
    quantities and every Thomson link is TYPE-U.  OFF THE CHAIN, of record, THREE:
    the fiber proper radius R in K_KK (ADOPTED; K_KK changes by beta^2); the complete
    normalized D_BR spectrum (UNBUILT); the skeleton-to-cell embedding (GAP, "has never
    been attempted", numerology-cliff guard attached).  S16 IF DERIVED: UNDETERMINED of
    record — a reason to expect beta-sensitivity is displayed and NOT booked.  The
    relay's premise that step 7 is the expected feeder is NOT grounded in the census,
    and is not refuted either.
FIRST_TARGET = chosen (justified): S03, "dynamical U(1) action" — the chain's head and
    its ONLY lawful entry.  Not S16 and not S13: entering there and working back is
    precisely the selection C7 bars, nothing upstream exists (0/18), and A28 does not
    reward a partial chain.  Effort classes at section 3.3.  SCOPING CONSEQUENCE offered
    to the registrar: if the goal is Q-126's conjunction, the Thomson chain is the long
    way round — nine unbuilt links, head-entry only, terminal beta-sensitivity
    undetermined — while the census's three candidates are each ONE object.
VOID = clean
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+4 disclosures at section 4.3, including that my own standing
    writer-exclusion rule has been implemented too narrowly for many relays)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
