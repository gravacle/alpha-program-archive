# STAGE 8 / TASK 6 / SUBGATE — CUSTODY REVIEW OF THE LP-MATRIX THIRTY-ROW LEDGER — DARIO V001

Lane: Dario (Claude Opus 5), cross-family custody review lane
Task: PASTE 620 / Task 6 subgate
Authority to review: DoR-020-A8. **THIS ARTIFACT CERTIFIES NO SEAL AND LIFTS NO GATE.**
Custody: Codex 3 executed; I verify. Adversarial posture throughout.

```text
REGISTER_HEAD = Q-554
LEDGER = CONFIRMED (+2 taxonomy overrides, neither gate-moving)
ROW_OVERRIDES = A25 FAIL -> BLOCKED ; A27 FAIL -> BLOCKED
LINEAGE = CONFIRMED
CONSEQUENCE = CONFIRMED
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none of my own
```

**The ledger's conclusion is right and I verified it independently.** Its lineage
reproduces bit-for-bit, its consequence chain is exact against the authoritative
machine graph, and its determination — `passed_A01_A29_and_A35 = false`,
`SPEC-SEAL = false` — stands unchanged under both overrides. What the overrides
correct is a **taxonomy** error that makes two rows inconsistent with the ledger's
own §0.2 definitions and with its own handling of A26 and A28.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-554 (live-append tolerant) | verified |
| `STAGE8_TASK6_LP_MATRIX_LEDGER_LANE3_V001.md` = `bc6c3e496ffd6e8d06cc3237e47a6a02b76faaa88b63b0ffb38684971c2d1362` | **verified before reading** |
| 1,081 lines | verified |
| Output name collision | none — clear to write |

---

## V1. THE LINEAGE — **CONFIRMED**

### 1.1 The root manifest digest reproduces bit-for-bit

[PROVABLE] I reconstructed the five LF-terminated UTF-8 rows exactly as displayed
and hashed them:

```text
computed  4c04e4aae924f87736809d2a119a0fdeda271f77cd5141d26aa453cfc5c4abc2
claimed   4c04e4aae924f87736809d2a119a0fdeda271f77cd5141d26aa453cfc5c4abc2   MATCH
```

### 1.2 All five member hashes verify

Four I had already verified independently at PASTE 600 (A32 V002 `32dbfc33…`,
V000 `13faf0bc…`, Q-25 masking `d7153b91…`, Q-27/Q-28 admissibility `a132f4b2…`).
The fifth — the packet manifest file's own digest `9d35f4ed…` — I verified here.

### 1.3 Packet closure re-run, not accepted

[PROVABLE] I re-ran the verifier in its own directory:

```text
manifest rows = 113
OK            = 113
FAILED        = 0
```

The 113/113 claim holds.

### 1.4 The lineage members are the lawful ones

[PROVABLE] Two membership judgments, both correct:

- **V000 is not an independent member.** *"V002 controls the incorporated V000
  ranges; V000 is not an independent later amendment."* This matches what I
  verified at PASTE 600 — V000 is *"not standalone-sealed; exact clauses sealed by
  V002 incorporation."*
- **The audit matrix and blocker ledger are protocol authorities, not lineage
  members.** *"They define tests against `LINEAGE_LP`."* A test definition is not
  a member of the subject it tests; including it would make the audit
  self-referential.

[YOURS] I also credit the **conservative** subject choice. The ledger rejects the
narrower five-governing-act digest *"alone"* because it *"would omit those
content-addressed companions"*, and takes the broader subject — packet manifest
plus four amendments. Choosing the larger audit subject is the harder,
right-facing choice.

---

## V2. PASS VERIFICATION — **CONFIRMED, 24/24**

### 2.1 The seven load-bearing displays, re-derived from V011 rather than checked for quotation fidelity

| Row | Verdict | The failure mode hunted, and what was found |
|---|---|---|
| **A10** Gram | **CONFIRMED** | Non-circular: `C_p(K)` is a direct sum over elementary `p`-cells, so those generators are a **basis** and the Gram matrix determines `M_p` completely — the step that makes a Gram argument sufficient rather than partial. Positive-definiteness is a standing property of the *admitted class*, declared before the hypothesis, so it is not smuggled in as its own premise. No PD/PSD gap in either direction. |
| **A13** colimit collapse | **CONFIRMED** | A collapse of the **object**, not the diagram. The index category has a terminal object, so the only cofinality needed is the trivial terminal case — nothing stronger is assumed. The hostile `(c,d)` family is genuinely complete because `Hom(L_s,L_t)` is one-dimensional in the rank-one setting. |
| **A14** frozen reduction + `D_x` | **CONFIRMED** | The hostile family question I considered most dangerous. The normalization-blind set is `S^3`, i.e. `S^2` modulo common phase — **two** parameters, while `D_x` as displayed covers only the `θ = 0` meridian with `0 < x < 2`. Both omissions (all `θ ≠ 0`; the poles) are **separately mandated and separately killed**, and both die under the same metric-free closure step because `a = b` is a complex equation. The union exhausts. |
| **A17** adjoint | **CONFIRMED** | `D^♯ = M_1^{-1} D^† M_0` is a genuine Hilbert adjoint, everywhere-defined; the dense-domain failure mode is structurally impossible because the carrier is finite. |
| **A21** CPT/CP-axial + **branch scoping** | **CONFIRMED** | **I verified this one personally** — see §2.2. |
| **A26** Moore-Penrose lift | **CONFIRMED** | Conditions established, not assumed. |
| **A29** loop preregistration columns | **CONFIRMED** | The anti-tuning row in disguise: the columns are fixed in the frozen declaration, and completion requires **type-checking**, not evaluating any of them — the ledger says so and no value is evaluated. |

[YOURS] One **disclosure** defect worth recording and expressly **not** fatal:
A14's normalization step imports the derived identity metric from A10, while its
own gate instructs it to start from all mandatory hostile counterfamilies —
including arbitrary positive-definite `M_0, M_1`. A10 carries a conditionality
caveat; A14 does not. I checked whether the conclusion survives the omission: the
kill steps are metric-free, and for any fixed positive-definite pair the
normalization still yields a unique `|a|`. **Robust; a hygiene defect, not a false
PASS.**

### 2.2 A21's branch scoping — verified by me, and the objection fails

The relay named this specifically, and it is the row where a scoped audit is most
easily consumed unscoped. I read the display myself.

[PROVABLE] The scoping is **explicit and self-limiting**: the gate closes
SP01–SP04 *"in the declared stationary exterior-vacuum, standard-CPT, ordinary
CP-even, zero-index closed-double-regulator branches"*, and states **"It does not
claim a universal or complete connected parent."**

[PROVABLE] And decisively — **the requirement itself demands the scoping.** Its
verbatim text includes *"disclose the regulator and topological branch."* A row
that discloses its branch is doing what was asked, not evading. An independent
adversarial verifier reached the same conclusion on this point: *"Branch-scoping
is expressly demanded, not a violation."*

**A21 = CONFIRMED** on the question I was asked to verify.

[YOURS] **A residual objection to A21 was raised on other grounds and I decline to
carry it.** Its several stated legs were broken under attack — including one that
was itself an M-2 hyphenation false negative (*"charge conjugation"* returning
zero while the sealed member reads *"charge-conjugation"*). One leg reportedly
survived on evidence I did not verify myself. **I do not book an override into a
seal-gating ledger on evidence I have not checked**, and I record the item as open
rather than resolved in either direction.

### 2.3 The remaining PASS rows

Seventeen rows spot-checked against their cited V011 ranges: **sixteen hold**
outright. One override was proposed against **A03 (status firewall)** and was
**refuted** on attack — the ledger's PASS stands.

---

## V3. THE FAIL / BLOCKED SET — **TWO OVERRIDES**

### 3.1 A25 and A27 are BLOCKED, not FAIL

[PROVABLE] The ledger's **own** §0.2 definitions decide this:

```text
FAIL     a conjunct is structurally false on LINEAGE_LP;
BLOCKED  the type/condition is present, but a demanded member, proof package,
         or executable is absent, so the row cannot be completed.
```

For both rows the record contains **no negation and no counterexample** — only an
outstanding-obligation clause plus a pre-gate authorization flag reading
`..._proved = false` / `..._passed = false`. A missing **proof package** is
BLOCKED by the ledger's own words.

Two further points make this the ledger's own standard rather than mine:

1. **The ledger demotes exactly this evidence class itself.** §0.2: *"A historical
   `true`, `false`, `PASS`, or `PENDING` status string is evidence about
   provenance, not a substitute for the displays below."* `cellulation_
   independence_proved = false` is such a string.
2. **The ledger already applies the correct taxonomy elsewhere.** It grades **A26
   PASS** despite `unique_flux_lift_proved = false`, and **A28 BLOCKED** on *"the
   demanded complete downstream member is absent."* A25/A27 as graded are
   inconsistent with both.

For A27 specifically, the sealed spec keeps failure and failure-to-prove apart:
*"Failure to prove this naturality either blocks the general claim or restricts
the result explicitly to that cellulation"* — **blocks**, which is the BLOCKED
verdict in the spec's own vocabulary. The kill-condition list elsewhere
(*"refinement naturality fails"*) has failure as its antecedent, not
failure-to-prove.

Both overrides **survived adversarial attack**, each attacker instructed to
default to refuting them.

### 3.2 The four BLOCKED rows — **CONFIRMED**

A23, A24, A28, A35 verify as BLOCKED under M-2's three guards, and the ledger
**preserves scope-limited honesty**: each absence is bounded and none reads as
proof of emptiness.

### 3.3 `FENCE_ADJACENT = 0` — **UPHELD**

[PROVABLE] I treated this as the classic "true by not looking" claim and it
survives. The ledger dispositions the fence question **row by row**, not by
omission: A23 *"stopped at the absent object and no value is evaluated"*; A24
*"No fenced interval or response value is computed"*; A35 *"The executable's
absence determines this row before any physical regression quantity is evaluated.
It is therefore BLOCKED, not FENCE-ADJACENT"*; A29 *"No characteristic
polynomial, eigenvalue, trace, or ratio is evaluated in this relay."* The §7.1
inventory names the forbidden object classes and disposes five rows against them.

An override to "not tested" was proposed and **refuted** — it died on its own
execution, having run the test and returned zero. Its supporting count was itself
an M-2 failure (eight "fence" hits where there are nine).

Two **editorial** notes survive, neither verdict-changing: line 44 states a
weaker proposition than §0.2's completion criterion, and §0.2 codifies no explicit
BLOCKED-vs-FENCE-ADJACENT tie-break — though the discriminator (*what actually
stops the row*) is applied consistently and displayed in-row three times.

### 3.4 Revised board

```text
PASS 24 / FAIL 0 / BLOCKED 6 / FENCE-ADJACENT 0        (24+0+6+0 = 30)
FAIL_SET    = {}
BLOCKED_SET = {A23, A24, A25, A27, A28, A35}
```

**Six rows remain non-PASS. The determination is untouched.**

---

## V4. THE CONSEQUENCE — **CONFIRMED**

### 4.1 Propagation, checked against the authoritative machine graph

[PROVABLE] `SPEC-SEAL <- []` matches the authoritative `stage_dependencies` I
parsed and verified at Q-546 and Q-551, and `passed_A01_A29_and_A35` is a
preserved non-seal conjunct of `SPEC-SEAL` per the ratified §1.4 table.

The ledger names as failed descendants: `CORE-RESULT-SEAL`,
`HOLDOUT-UNIVERSE-SEAL`, `QSPEC-SPEC-SEAL`, `PREDICTION-MAP-SEAL`,
`THOMSON-RESULT-SEAL`, `PARENT-COMPARISON`, `ALPHA-RESULT-SEAL`,
`HOLDOUT-RESULT-SEAL`, `END-TO-END-RECONSTRUCTION-SEAL`, `FINAL-CLAIM-SEAL` —
**exactly the ten non-root nodes** of the eleven-node graph, which is correct
under the fail-closed descendant rule for a false root. Neither override disturbs
it: six non-PASS rows still give `passed_A01_A29_and_A35 = false`.

### 4.2 The invalidation rule is the matrix's own — I attacked this and failed

[PROVABLE] I suspected the ledger of strengthening the rule, because the matrix
has a finer-grained clause (*"An edit to a row's input invalidates that row and
every row below it"*) that would license less than a full rerun. It does not. The
governing clause for repairing a failed row is the matrix's own:

> *"Finding and repairing one failed row invalidates that version. The repair
> must **increment the version and rerun every row, including rows that
> previously passed. No delta-only review can seal BID.**"*

The ledger's rendering — *"the repaired lineage must be incremented and all thirty
demanded rows rerun … no delta-only carry is licensed"* — is faithful in
substance and in prohibition. **My attack fails and I report it as failed.**

[YOURS] One precision: the ledger extends the rule to the BLOCKED set (*"Supplying
A23, A24, A28, or A35 likewise produces a new lineage and a fresh full
execution"*). The matrix's clause speaks of a *failed* row, so this extension
rests on the lineage-change reasoning rather than that clause literally — supplying
a missing object changes the audit subject, so every row must rerun. The reasoning
is sound and the direction is **conservative**: it demands more rerunning, not
less. Not a defect.

---

## V5. BATTERY AND FRESH ATTACK

### 5.1 Fresh attack — the strongest available, and it fails

[YOURS] My attack targeted the ledger's **weakest structural point**: that its two
FAIL verdicts and its `FENCE_ADJACENT = 0` are the three places where a verdict
could be true by construction rather than by test.

- On the **FAIL** verdicts the attack **fires** — but as a taxonomy correction that
  *tightens* internal consistency, not as a loosening (§3.1).
- On **`FENCE_ADJACENT = 0`** it **fails**: the count is dispositioned row by row
  and survives (§3.3).
- On the **invalidation rule** it **fails**: the ledger is faithful to the
  matrix's own words (§4.2).

**Two of three attacks failed, and the one that fired does not move the gate.**

### 5.2 `F_PLDEC` and anti-tuning

[PROVABLE] The ledger consumes only structural specifications, content-addressed
derivations and protocol decisions, and it states the exclusion explicitly: *"It
does not consume a reader output, local-shadow value, candidate outcome, measured
central value, fixed point, end test, or physical response value."* No row's
verdict is reached by evaluating a physical quantity.

### 5.3 Surface anchor

**Named actual objects:** the 113-row packet manifest; the five-row root manifest
and its digest; `C_p(K)`, `M_0/M_1/M_2`, `D^♯`, `D_(a,b)`, the `D_x` hostile
family, `Θ_D`, `U_X`, `J_star`, `B_square`, `LINEAGE_LP`.

**Rails awaiting members:** the six BLOCKED objects; `SPEC-SEAL` and all ten
descendants.

### 5.4 Verb audit on my own board

| My verb | Check |
|---|---|
| `LINEAGE = CONFIRMED` | Recomputed by me: digest bit-for-bit, 113/113 re-run, five member hashes. Not accepted from the ledger. |
| `CONSEQUENCE = CONFIRMED` | Propagation checked against the graph I parsed myself at Q-546/Q-551; the invalidation rule checked against the matrix's own text after I tried and failed to refute it. |
| `ROW_OVERRIDES` (A25, A27) | Grounded in the **ledger's own §0.2** and its own A26/A28 handling — not in an external standard. Both survived attackers instructed to default to refutation. |
| "does not move the gate" | Six rows remain non-PASS; `passed_A01_A29_and_A35 = false`; `SPEC-SEAL = false`. Stated because an override in a seal-gating ledger must be shown not to loosen it. |
| A21 | **CONFIRMED on the branch-scoping question I was asked and personally verified.** A residual objection on other grounds is recorded as **open**, not resolved — I decline to book an override I did not check myself. |
| A14 hygiene defect | Reported and explicitly **not** fatal, with the robustness check that establishes why. |
| `LEDGER = CONFIRMED` | Confirms the ledger's determination, lineage and consequence. It is not a certification of any seal, and the ledger itself certifies none. |
| Agent reliance | 9 agents; three proposed overrides were **refuted** (A03, `FENCE_ADJACENT`, and most legs of A21) and two survived. I verified the lineage, the consequence, A21's scoping and the invalidation rule personally. |

---

```text
LEDGER = CONFIRMED (+2 taxonomy overrides; the determination, lineage and
  consequence all verified independently and unchanged)
ROW_OVERRIDES =
  A25  FAIL -> BLOCKED   no negation or counterexample of record; the missing
       object is a proof package, which is BLOCKED under the ledger's own §0.2,
       and the supporting `..._passed = false` is a status string the ledger
       itself demotes to provenance evidence;
  A27  FAIL -> BLOCKED   same ground, and the sealed spec keeps the two apart in
       its own words -- "Failure to prove this naturality either BLOCKS the
       general claim or restricts the result explicitly to that cellulation".
  Both survived adversarial attack. Revised board PASS 24 / FAIL 0 / BLOCKED 6 /
  FENCE-ADJACENT 0; six rows still non-PASS, so nothing moves.
  Consistency gain: A25/A27 now match the ledger's own A26 (PASS despite
  `unique_flux_lift_proved = false`) and A28 (BLOCKED on an absent member).
LINEAGE = CONFIRMED (root digest 4c04e4aa... reproduced bit-for-bit from the
  displayed five rows; all five member hashes verify; packet manifest re-run
  113 rows / 113 OK / 0 FAILED; V000 correctly not an independent member; the
  audit matrix and blocker ledger correctly protocol authorities, not members)
CONSEQUENCE = CONFIRMED (SPEC-SEAL <- [] matches the authoritative
  stage_dependencies; passed_A01_A29_and_A35 = false => SPEC-SEAL = false; the
  ten named failed descendants are exactly the ten non-root nodes under the
  fail-closed rule; the invalidation rule is the matrix's own verbatim in
  substance, including "No delta-only review can seal BID" -- my attack on it
  failed and is reported as failed)
VERB_AUDIT_SELF = CLEAN
```

The ledger reaches the right determination by a lineage I could reproduce and a
consequence chain I could check node by node. Its two FAIL verdicts are mis-typed
against its own taxonomy — a correction that makes it internally consistent and
leaves `SPEC-SEAL = false` exactly where it was. `FENCE_ADJACENT = 0` is the claim
I most expected to be true-by-not-looking, and it is not: the ledger tested it row
by row and I could not break it.
