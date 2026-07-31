# STAGE8_B0_INPUT_OR_TARGET_ADJUDICATION_EINSTEIN_V001

LANE: EINSTEIN
RELAY: 201 ("IS `B0` AN INPUT OR THE TARGET?")
DATE: 2026-07-31
REGISTER HEAD AT ISSUE: Q-106.
ROAD JUSTIFICATION (Q-83): offered as `UNBLOCKS STEP 1`. **DISCHARGED PARTIALLY — one blocker-list
entry is retyped; NO blocker is removed and the total is unchanged (§4).**

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false;
coupling_evaluation_authorized = false; production_authorized = false.
NOTHING WAS COMPUTED. `B0` NOT constructed. `B0` NOT identified with P0, the threshold, or any
flag on resemblance alone (Q-69). The quotient/measure bundle (Codex 1, relay 199) and the
correlator-to-Hessian map's relation (Codex 2, relay 200) are CITED, never re-adjudicated.
`a32_holdout/custodian_private/` untouched. Read-only throughout.

METHOD: five attack tasks (consume/produce, category, B0↔P0, count, consumers), each adversarially
verified under an explicit **symmetric-framing duty** — verifiers were instructed not to demand
more evidence of the reviewer-confirming answer than of the reviewer-refuting one, and to check
specifically for the ordered asymmetry (never lower a count because a smaller count is better
news). Run wf_5ce9684e-3d6, ten agents. Statuses: consume/produce REFUTED, category WEAKENED,
B0↔P0 WEAKENED, count WEAKENED, consumers WEAKENED. **The verifiers disagreed with each other on
"in use" and on "indefinite"; that conflict is adjudicated by this lane in §2 on lines I read
myself.**

FILES: "the audit" = STAGE8_SEVEN_USED_AS_PRIMITIVES_SEALABILITY_AUDIT_V001.md (Q-105, Codex 2);
"the prefreeze" = STAGE8_FROZEN_PRIMITIVE_INVENTORY_PREFREEZE_RESULT_V001.md; "the B0 spec" =
STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md; "the triage" =
STAGE8_CTP_PHYS_INPUT_PACKAGE_TRIAGE_AND_LOAD_BEARING_FUNCTIONAL_SPEC_V001.md — all archive
workspace, cleanroom mirrors verified byte-identical.

---

## 0. LEAD

*** THE REVIEWER IS RIGHT — AND THE CORRECTION IS **BAD NEWS, NOT GOOD**. ***

`B0` is a **construction target**, not a primitive whose content happens to be unfixed. Three
independent sealed columns say so in their own words, and I read all three:

- the audit's **Authority** column: *"TYPE-U, not adopted primitive"* (`:23`);
- the audit's own **verdict prose**, inside the INDEFINITE cell: *"it is the object still to be
  constructed, **not a definite input**"* (`:23`);
- the prefreeze's **Status** column: *"TYPE-U construction debt; **not an adopted primitive**"*
  (`:202`).

And the B0 spec types itself: `B0_Q70_local_classification = TYPE_U_CONSTRUCTION_DEBT` (`:1452`),
with a dedicated would-build whose **output is B0** (`:1566-1568`).

**BUT THE COUNT DOES NOT SIMPLY FALL FROM THREE TO TWO, AND I WILL NOT REPORT IT THAT WAY.** Two
numbers move in opposite directions and both must be stated:

```text
"INDEFINITE OBJECTS IN LOAD-BEARING USE"    3  ->  2      B0 fails the conjunct
TOTAL UNSEALABLE / BLOCKER COUNT            7  ->  7      UNCHANGED. Q-105's ZERO OF SEVEN stands.
```

*** RE-BINNING IS NOT PROGRESS. B0 leaves the "indefinite" bin and enters the "unbuilt target"
bin; it leaves the blocker list not at all, and it still hard-blocks C0, U1, U2, U3, item 1 and
the package. AND THE RETYPE MAKES THE OBLIGATION HEAVIER: an indefinite input might be sharpened
by fixing a definition — a target must be BUILT. ***

**THE REGISTER'S OWN JUSTIFICATION FAILS FOR `B0`, AND THAT IS THE CLEANEST WAY TO SEE THE
MISCATEGORIZATION.** Q-105 explains why the middle row is serious: *"AN INDEFINITE OBJECT IN
LOAD-BEARING USE IS WORSE THAN A MISSING ONE, **BECAUSE IT LOOKS PRESENT**"* (register
`:4283-4284`). *** `B0` DOES NOT LOOK PRESENT. It is openly recorded as TYPE-U with a would-build
at every site. It is the *missing one* the gloss contrasts against, not the object the gloss
describes. ***

---

## 1. ANSWER 1 — WHAT `B0` IS, AND THE CONSUME/PRODUCE SPLIT

**THE NAMES, KEPT SEPARATE (Q-69).** Four distinct sealed identifiers, not merged:

- **`B0`** = `COMPLETE_MICROSCOPIC_BOUNDARY_OPERATOR` — sealed identity (triage `:853`; B0 spec
  `:30`, `:445`). Typed `derived = false | TYPE-U`.
- **`B0_CONSTRUCTION_WITNESS`** — *"a local specification placeholder, not an adopted primitive"*
  (B0 spec `:87-89`), and **upstream of B0**: the spec seals the direction *"construct B0 from
  `B0_CONSTRUCTION_WITNESS`"*. B-P2 states its content: *"One construction witness supplies an
  explicit primitive-input inventory and a target-independent construction rule"* (`:891`).
- **`B0` [T7-baseline-nonvanishing predicate]** — a *hypothesis* in the T7 family; the B0 spec
  explicitly *"does not import an object from the T7 family"* (`:52-53`). Kept separate.
- **`H-B0`** — *"a compound T7/E1 identifier, not a third standalone B0 family"*.

**THE SPLIT, AND IT IS THE ANSWER TO THE CHARTER'S QUESTION 1.**

- **PRODUCED.** A would-build exists whose **output is B0**: `COMPLETE_MICROSCOPIC_BOUNDARY_
  OPERATOR_derived = false | TYPE-U | would-build: B0_CONSTRUCTION_WITNESS followed by
  construction and proof of the declared package B0 object` (B0 spec `:1566-1568`).
- **CONSUMED.** `B0` is named in a dependency position pervasively — C0, U1, U2, U3, item 1 and
  the whole package name it as a prerequisite. *** BUT EVERY SUCH SITE IS ITSELF `derived = false
  | TYPE-U`, EXPLICITLY CONDITIONAL ("If B0 and C0/U1-U3 are independently derived"; "Conditionally
  on B0"), OR A FENCE/EXCLUSION LINE. NOT ONE COMPLETED ARTIFACT DRAWS CONTENT FROM `B0`. ***
- **THE TWO DIRECTIONS MUST NOT BE CONFLATED, AND THE CORPUS HAS A SENTENCE FOR EACH.** *"the
  present bounded corpus names no exact prerequisite node **into** B0"* (B0 spec `:68-69`) is
  about what feeds B0 — **nothing does**. That is a statement about B0's *inputs*, not about its
  consumers.

**THE DECISIVE STRUCTURAL LINE, WHICH I READ MYSELF — B-P4:**

> *"C0 descends from `B0`; U1/U2/U3 descend from the pair `(B0,C0)`; **none is an input to
> `B0`**"* (B0 spec `:893`)

*** `B0` TAKES NOTHING AND FEEDS EVERYTHING. IT IS THE ROOT OF THE DESCENT DAG. *** That is
precisely the *position* a primitive occupies — which is how it landed on a used-as-primitive list
— while its *status* is an unbuilt target with a would-build. **RULING: `BOTH_SPLIT`, in an exact
sense — PRIMITIVE-POSITIONED, TARGET-STATUSED.** A clean "INPUT" and a clean "TARGET" are both
refuted, and neither answer was the safe one.

---

## 2. ANSWER 2 — INDEFINITE OR MISCATEGORIZED? (THE VERIFIER CONFLICT, ADJUDICATED)

**MY VERIFIERS SPLIT.** One held that `B0` is genuinely indefinite and the register's failing
clause is only *"AND IN USE"*. Another held `B0` is not indefinite at all, because it has a sealed
identity, a fixed descent direction, and an explicit Q-70 typing. **Both are partly right, and the
resolution is a distinction neither drew cleanly.**

```text
B0's ROLE     DEFINITE   sealed identity (triage :853); fixed descent direction (B-P4 :893);
                         production codomain (DESCEND_B0); Q-70 typing TYPE_U_CONSTRUCTION_DEBT
B0's CONTENT  UNDETERMINED   B0_explicit_mathematical_map_domain_codomain_found = false | TYPE-S
                         (B0 spec :812-819) — no signature, domain, codomain, or carrier found
```

*** SO "INDEFINITE" IS TRUE OF `B0`'s CONTENT — **TRIVIALLY, AS IT IS OF EVERY UNBUILT TARGET.**
AN OBJECT THAT HAS NOT BEEN CONSTRUCTED NECESSARILY LACKS INTERNAL CONTENT. THAT IS WHAT TYPE-U
MEANS. *** The bin therefore carries no information about `B0` that its TYPE-U status did not
already carry — whereas for the other two indefinite rows it carries a great deal, because those
objects are *in use and underdetermined at once*.

**THE CATEGORY ERROR, STATED EXACTLY:** the audit asked *"can these seven be sealed **as
primitives**?"* The bin "INDEFINITE" answers *"it is a primitive whose content is not fixed."*
**`B0`'s answer is a category further back: it is not a primitive at all.** "Indefinite as a
primitive" presupposes primitive status that three sealed columns disavow. *** THE FAILING WORD IS
NOT "INDEFINITE" AND NOT ONLY "IN USE" — IT IS THE PRESUPPOSITION "AS A PRIMITIVE" THAT BOTH
CONJUNCTS RIDE ON. ***

**AND "INDEFINITE" DOES NOT MEAN THE SAME THING ACROSS THE THREE ROWS** — which is itself a
finding. The audit's own criteria: quotient/measure — *"the used bundle has no single definite
object, domain, or authority"* (`:21`); raw map — *"relation, domain, and physical quotient are not
fixed as one sealed map"* (`:22`). Both are **used-but-underdetermined**. `B0`'s cell instead
reads *"it is the object still to be constructed, not a definite input"* (`:23`) — **a statement
about category, not about determinacy.** The middle row is not one category but two.

**A SECOND DEFECT, INDEPENDENT, IN THE ROW ITSELF.** The audit's row is headed
``B0_CONSTRUCTION_WITNESS` / complete microscopic boundary operator` — **merging the two ends of a
construction edge.** The spec keeps them ordered (*"construct B0 from `B0_CONSTRUCTION_WITNESS`"*;
B-P2 at `:891`), and F-GK3 point 3 invokes Q-69 to insist they are *"separate nodes."* The row's
Authority text (*"TYPE-U, not adopted primitive"*) reproduces the **witness** paragraph (B0 spec
`:87-89`), while the register then read the row as being about **`B0`**. *** THE OBJECT THE AUDIT
TYPED AND THE OBJECT THE REGISTER COUNTED ARE THE TWO ENDS OF ONE EDGE. *** (The register's
compression to bare `B0` is nonetheless **faithful** to the row's second member, since
`B0 = COMPLETE_MICROSCOPIC_BOUNDARY_OPERATOR` is sealed at triage `:853` — a draft claim that the
compression was itself erroneous is **withdrawn**, §7.)

**RULING: MISCATEGORIZED.** The reviewer's reading is confirmed — on the audit's own words, not on
a reconstruction of them.

---

## 3. ANSWER 3 — THE `B0`/P0 RELATION

*** IDENTITY IS **REFUTED**, NOT MERELY UNASSERTED. ORDERING IS `NO_VERDICT`. THE PROGRAM IS
**NOT** COUNTING ONE BLOCKER TWICE. ***

Q-95 types P0 as *"One microscopic source-record-field operator/dynamics **B0-like** source"*
(rank-1 `:233`). By Q-69, "B0-like" is **resemblance, and resemblance is not identity**. The
corpus does not leave this to inference — **four sealed negatives, from three independent lanes**:

- rank-1: *"The class says B0-like, not `P0 = B0`"*;
- the joint-P0 buildability result: *"`B0` is a useful specification analogy but is **not** a P0
  constructor or an existing P0"*;
- the common-origin typing artifact's executed **P0/B0-IDENTITY-CHECK** negative;
- the Obj_0 spec: *"`Obj_0` = **NOT IDENTIFIED WITH** `B0`, `U_BR`, `D_BR`, a BID generator, or a
  flag."*

**Three lanes independently ran the identity query and each returned `qualifying_identity_found =
false`.** So `SAME_DEBT` is refuted, and the double-counting worry is answered: **no double
count.**

**BUT THE ORDERING IS GENUINELY UNRECORDED — `NO_VERDICT`, and this is missing information, not a
disposal.** No sealed sentence asserts that either is upstream of the other. Both are single
microscopic source-record-field operators serving as roots of their own descent structures, in two
separately-rooted specifications. **What would decide it:** a sealed sentence placing one in the
other's construction inputs, or a derived identity/inclusion. *** THE UNRECORDED ORDERING IS A
FINDING IN ITS OWN RIGHT: two construction debts of the same physical shape sit at the roots of
two different ladders, and nothing in the corpus says whether building one would serve the other.
That question is now named. ***

---

## 4. ANSWER 4 — THE CORRECTED COUNT, STATED PLAINLY BOTH WAYS

**RE-DERIVED FROM THE AUDIT'S OWN SEVEN ROWS, NOT INHERITED:**

| # | object | audit's bin | re-run bin |
|---|---|---|---|
| 1 | `rho_pre` | DESCENDANT | DESCENDANT (TYPE-R, Q-100 criterion) |
| 2 | `U_BR[A,g]` | DESCENDANT | DESCENDANT (TYPE-R) |
| 3 | Effects/domains | DESCENDANT | DESCENDANT (TYPE-R) |
| 4 | Quotient/measure | INDEFINITE | **INDEFINITE — in use, underdetermined** (Codex 1's object; cited, not re-adjudicated) |
| 5 | Raw-correlator → retarded-Hessian map | INDEFINITE | **INDEFINITE — in use, underdetermined** (Codex 2's object; cited, not re-adjudicated) |
| 6 | `B0` | INDEFINITE | *** CONSTRUCTION TARGET — retyped *** |
| 7 | `PrimitiveInventory_0` | INDEFINITE + circular | PLACEHOLDER, circular as posed |

```text
INDEFINITE-IN-USE            3  ->  2      (quotient/measure; raw map)
CONSTRUCTION TARGETS         0  ->  1      (B0)
MISFILED DESCENDANTS         3      3
CIRCULAR PLACEHOLDER         1      1
TOTAL UNSEALABLE             7  ->  7      *** UNCHANGED. ZERO OF SEVEN STANDS. ***
```

*** THE HONEST BOTTOM LINE: THE CORRECTION MAKES THE FOUNDATION **WORSE**, NOT BETTER. *** An
indefinite input is an object the program *has* and cannot pin down — sharpening a definition
might fix it. A construction target is an object the program *does not have*. Moving `B0` from the
first bin to the second converts a definitional problem into a construction obligation. **Nothing
was removed from the blocker list, and the one entry that moved got heavier.**

**AN INTERNAL INCONSISTENCY IN THE AUDIT, FOUND AND REPORTED:** its Result line says *"**Four** are
downstream descendants and must remain `S_sector`; **three** are indefinite or placeholders"*
(`:7-8`), while its own table has **three** descendants and **four** cells labelled INDEFINITE. The
register (`:4277-4279`) reproduces the *table*, not the Result line, and is correct to do so.
**Reported, not repaired.**

---

## 5. ANSWER 5 — WHAT WAS CONSUMING `B0`, AND WHAT THOSE CONSUMPTIONS ACTUALLY NEED

**Roughly two dozen distinct sites name package-`B0` in a dependency position across the three
roots. Every one falls into (i), (ii) or (iii) — and the census is the proof of the ruling:**

- **(i) genuinely blocked on the full constructed `B0`** — `C0`, `U1`, `U2`, `U3`, item 1, the
  package instantiation, and `DESCEND_B0`. *** EVERY ONE OF THESE IS ITSELF `derived = false |
  TYPE-U`. NOT ONE IS A COMPLETED ARTIFACT PROCEEDING AS THOUGH IT HAD `B0`. *** They are honest
  would-builds naming an unbuilt prerequisite.
- **(ii) needs only a property or interface** — none survived scrutiny into this bin: every
  dependency clause states *what must descend from* `B0`, never *what `B0` supplies as a usable
  interface*. Correspondingly, `B0`'s own signature is TYPE-S-absent (`:812-819`), so there is no
  interface to depend on even in principle.
- **(iii) decorative** — the graph-rule/authority sweeps, the JSON ledger sweep, the allowance
  envelope, the K0-K6 overlap remark, and two of this lane's own earlier artifacts: `B0` appears
  only in a fence, exclusion, or overlap line. **Deleting the token leaves each verdict intact.**

*** SO THE CHARTER'S WORRY — "a consumer that thinks it has an input it does not have is depending
on nothing" — DOES NOT MATERIALIZE. NO CONSUMER THINKS IT HAS `B0`. *** Every dependency is
declared conditional and every dependent object is itself unbuilt. **That is a clean result and it
is reported as one.**

**Q-69 CHECK, RUN EXPLICITLY AND CLEAN.** No consumer takes a `B0` *flag*
(`B0_role_contract_specified = true`, `correspondence_check_completed = true`,
`B0_exact_alias_recovered = true`, …) as though it were the `B0` *object*. The B0 spec pre-blocks
the merge with an executed refutation — `package_B0_is_any_of_the_four_enumerated_flags = false |
TYPE-R` — and B-P6 states it as a premise: *"No discharge flag, item-1 output, T7 predicate,
broad completed-package signature, or finite control is identified with `B0`"* (`:895`). **A clean
Q-69 result is a real result.**

**THE PACKAGE RELATION:** `B0` is not the CTP physical input package and is not in it — it is the
**single-origin stop upstream of it**, from which the package's components descend (B-P4).

---

## 6. TYPED NEGATIVES (Q-54)

- **N1 [TYPE-R, executed]** `B0_has_any_completed_consumer_drawing_content = false`. Test:
  read every word-boundaried `\bB0\b` clause in a dependency position across three roots and check
  the consuming object's own status flag — **100% carry `derived = false | TYPE-U`, conditional
  phrasing, or fence context; zero draw content.**
- **N2 [TYPE-R, executed]** `B0_is_an_adopted_primitive = false`. Three sealed columns disavow it
  (audit `:23` Authority; audit `:23` verdict prose; prefreeze `:202` Status), plus the B0 spec's
  own `B0_Q70_local_classification = TYPE_U_CONSTRUCTION_DEBT` (`:1452`).
- **N3 [TYPE-R, executed]** `B0_and_B0_CONSTRUCTION_WITNESS_are_the_same_node = false`. B0 spec
  `:87-89` (the witness is a specification placeholder), B-P2 `:891`, and the sealed direction
  *"construct B0 from `B0_CONSTRUCTION_WITNESS`"*. **Two nodes, one strictly before the other.**
- **N4 [TYPE-R, carried, four sealed instances]** `P0_is_identical_to_B0 = false` — rank-1, the
  joint-P0 result, the common-origin P0/B0-IDENTITY-CHECK, the Obj_0 spec (§3).
- **N5 [NO_VERDICT]** `B0_P0_construction_ordering_established`. **Information missing**, not a
  disposal: no sealed sentence places either in the other's construction inputs. Deciding
  evidence named in §3.
- **N6 [TYPE-S]** `B0_internal_mathematical_signature_recoverable = false` — the B0 spec's own
  `B0_explicit_mathematical_map_domain_codomain_found = false | TYPE-S` (`:812-819`, with its
  roots, exclusions, fences and query sealed there), independently reproduced this relay: every
  consumer states what must **descend from** `B0`; none states what `B0` **is**. Bounded absence,
  not impossibility.
- **N7 [TYPE-R, executed]** `any_consumer_takes_a_B0_flag_as_the_B0_object = false` — Q-69 sweep,
  clean (§5).
- **N8 [TYPE-R]** `audit_result_line_descendant_count_matches_its_own_table = false` — Result line
  says four descendants, table has three (§4).
- **N9 [TYPE-R]** `total_blocker_count_reduced_by_this_relay = false` — seven unsealable before,
  seven after; Q-105's ZERO OF SEVEN untouched.
- **N10 [TYPE-R]** `a_new_Q80_class_was_required = false` — every finding routed into existing
  bins without strain. **This lane has struck four manufactured classes; I add no fifth.** The
  near-miss I considered and rejected: *"a use-column citation that resolves to the object's own
  status declarations."* It types cleanly as TYPE-R with an executed, reproducible test, so Q-80's
  "categories are WRONG" trigger does not fire.

---

## 7. CORRECTIONS FOLDED, UNDER THIS LANE'S NAME

1. **A draft finding that the register's compression to bare `B0` was erroneous is WITHDRAWN** —
   `B0 = COMPLETE_MICROSCOPIC_BOUNDARY_OPERATOR` is sealed at triage `:853`, so the row's second
   member **is** `B0` and the compression is faithful. What survives is narrower and still real:
   the row *heading* merges the witness with its output (§2).
2. **A draft claim that `B0` is "not indefinite at all" is WITHDRAWN.** `B0`'s content **is**
   undetermined (`:812-819`) — trivially, as every unbuilt target's is. The correction is that
   this carries no information beyond TYPE-U, and that the failing presupposition is "as a
   primitive" (§2).
3. **A draft claim that `B0` is "not in use" is NARROWED.** `B0` **is** named as a prerequisite
   pervasively — one sealed line uses the word *"input"* verbatim, and the register elsewhere
   lists it among objects "used as primitives." What is true is the sharper statement: **no
   completed artifact draws content from it, and every dependent is itself unbuilt.**
4. **Search-scope corrections:** the relay's "31 files" is an undercount of the archive root
   (subdirectory and non-`.md` hits excluded); `B0_CONSTRUCTION_WITNESS` contains **no**
   word-boundaried `B0` (underscore is a word character), which is why the prefreeze file falls
   outside a naive `\bB0\b` file list — a substring/word-boundary subtlety in the opposite
   direction from the usual one.
5. **Citation-span repairs:** several multi-line status blocks were cited by their opening line
   only; the B0 spec's terminal block spans past the range the prefreeze cites for it (the
   imprecision is the corpus's own citation, reported faithfully rather than silently widened).

---

## 8. DISCIPLINE

- **Q-52:** nothing discharged, nothing declared derived; `B0` not constructed.
- **Q-54:** every negative typed with its executed test, scope, or missing-information statement.
  `NO_VERDICT` used once (§3), for genuinely missing information.
- **Q-69:** the four `B0` names kept separate; the witness kept distinct from its output; no flag
  identified with the object it would discharge; identity refused on resemblance.
- **Q-80:** **no new class constituted** (N10), and the rejected near-miss is recorded so the
  suppression is visible.
- **Q-83:** partially discharged — one entry retyped, **no blocker removed**, total unchanged.
- **Q-91:** no `git` of any kind; baseline untouched; `deploy_status.sh` not run; no publication
  authorization requested. Artifact and verified sidecar in the archive workspace; stop.
- **Q-92:** nothing constructed.
- **SYMMETRIC FRAMING, HONOURED AND AUDITED.** The reviewer-confirming answer was **not** held to a
  higher standard: I looked specifically for a single site treating `B0` as supplied — one would
  have flipped the ruling — and found none across three roots. The **ordered asymmetry** was
  honoured in the other direction: the indefinite-in-use count falls to two **only** because the
  conjunct genuinely fails, the total blocker count is reported **unchanged**, and the retype is
  reported as **worse news**, not better.

alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
