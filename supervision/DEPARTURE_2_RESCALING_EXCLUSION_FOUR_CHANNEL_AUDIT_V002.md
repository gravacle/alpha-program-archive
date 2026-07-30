# DEPARTURE 2 — THE RESCALING EXCLUSION: AUDIT TRACKER V002

SUCCEEDS `DEPARTURE_2_RESCALING_EXCLUSION_FOUR_CHANNEL_AUDIT_V001.md` (sealed, bytes untouched,
cited throughout). Version incremented per V001's own instruction at `:3-5` — this is the same
tracker, not a second plan document.

Opened V001 2026-07-30 05:53 on the principal's instruction. V002 written 2026-07-30 on resume,
after executing V001's channel-4 step one: "determining what the corpus even says about it."

**THE SHORT VERSION. Channel 4 does not exist as a live channel, the deletion was not silent, the
requirement survives verbatim in the successor file, the live channel list is FIVE and different, and
the audit cannot be run at all yet — it is acceptance check 5 of 5 on an operator that was never
built. Two claims of record are corrected. The audit is not discharged; it is re-scoped and
re-sequenced.**

## 1. WHAT THE CORPUS SAYS ABOUT THE FIELD-ENERGY INTEGRAL

It says one thing, in the same file as the exclusion, sixteen lines above it.

`primitive_record_cell_selection_principle_v001.md:74-77`:

```
I_F,* = integral_(Omega_*) sqrt(|g_*|) F_*^{mu nu} F_*(mu nu) d^4x.
```

and at `:71-72`, `:88-89`:

```
Phi_* = (K_R / 4) I_F,* + Gamma_rest,*
K_R,* = 4 Delta Phi_EM,* / I_F,*,   alpha_* = 1 / (4 pi K_R,*)
```

**BOUNDED NEGATIVE.** Roots: `Documents/New project/gravity_emergence_evidence_program`,
`Documents/New project/_external_handoffs`, `MB Work/alpha_supervision`. Types `*.md *.json *.csv
*.py`. Exclusions: `node_modules`, `external/` (a cosmosis venv — it produces substring noise on
short tokens), `custodian_private`. Case-insensitive. Terms `field-energy integral` and
`energy integral` return **6 hits in 6 files, and every one is the exclusion sentence itself or a
restatement of it** (source `v001:108`; `STAGE8_RESCALING_EXCLUSION_RECOVERY_ERRATUM_V001.md:33`;
`RECOVERY_STIFFNESS_AND_ALLOW_REQUIRE_2026-07-29.md:55`; three in our own V001 and
CONTINUATION_STATE). **Zero independent occurrences.** Nothing in the program discusses the object
under that name except the sentence that names it.

So V001's channel 4 was not under-examined for want of effort. It had a definition all along and no
literature, and the reason is section 2.

## 2. CHANNEL 4 IS AN INGREDIENT OF A FORMULA THAT WAS SUPERSEDED THREE MINUTES AFTER IT WAS WRITTEN

V001's four channels — cell, duration, matter action, field-energy integral — are **exactly the four
ingredients of the post-saddle division rule** `K_R = 4(Phi_* - Gamma_rest,*)/I_F,*`. That is why the
list has four members and that is all the list is.

`primitive_record_cell_selection_principle_v002.md:3-16`, section headed **"## Correction to v001"**:

```
Version 001 was externally sealed before numerical work and is retained as an
audit record. Its explicit rearrangement

    K_R = 4 (Phi_* - Gamma_rest,*) / I_F,*

is valid only if the selected field configuration and the action partition are
already independent of `K_R`. A coupled matter-electromagnetic-gravitational
saddle need not have that property. Version 002 therefore replaces the direct
division rule with a joint saddle-and-closure selection problem. No numerical
cell or alpha value was evaluated between the two versions.
```

`I_F` survives in v002 in exactly one place — the envelope identity at `:111-120`,
`d Gamma_K[X_K]/dK = (1/4) integral sqrt(|g_K|) F_K^2` — and v002`:121-123` disposes of it in its own
words: **"This identity checks the implementation. It does not select `K_*`; the durable-record
closure equation must do that."**

**CHANNEL 4'S LIVE ROLE IS AN IMPLEMENTATION CHECK, NOT A SELECTOR CHANNEL.** Auditing it for a
surviving stiffness-changing family is auditing a quantity that the live principle does not use to
set the stiffness.

## 3. CORRECTION OF RECORD 1 — THE DELETION WAS NOT SILENT, AND "NO SUPERSESSION NOTE" IS WITHDRAWN

V001 of this tracker, `:63-65`: "An unversioned tree is how a necessary condition disappears in three
minutes with no supersession note." **THE FIRST HALF IS RIGHT AND THE SECOND HALF IS WRONG.**

The supersession note is `primitive_record_cell_selection_principle_v002.md:3-16`, quoted above. It
is in the immediately succeeding version of the same file, it names the deleted rule explicitly, it
gives the mathematical reason, and it certifies that nothing numerical happened in between. mtimes,
measured 2026-07-30, all 2026-07-20:

```
15:10  primitive_record_cell_selection_principle_v001.md          exclusion present
15:10  provenance/primitive_record_cell_selection_preregistration_v001.json
15:11  provenance/primitive_record_cell_selection_manifest_v001.json
15:13  primitive_record_cell_selection_principle_v002.md          exclusion absent, CORRECTION present
15:13  provenance/primitive_record_cell_selection_preregistration_v002.json  same correction, restated
```

The preregistration v002 `correction` field carries it independently: "The field configuration may
depend on K. The protocol now requires a joint solution of the complete coupling-indexed saddle and
durable-record closure equation rather than a post-saddle division formula."

**WHAT THE REAL DEFECT IS, NARROWED AND STILL REAL:** the reason was recoverable only by opening the
next version or the provenance JSON, and until 2026-07-29 nothing in the working set cited v001 at
all. As of today v001 is cited by `STAGE8_RESCALING_EXCLUSION_RECOVERY_ERRATUM_V001.md`, by its own
provenance manifest, and by four supervision artifacts — all created 07-29 or later. The loss was a
citation-graph loss, not an unrecorded deletion.

OWED, AND NOW SUPERSEDED BY THIS SECTION RATHER THAN BY THE V001 TIMELINE ALONE:
- `RECOVERY_STIFFNESS_AND_ALLOW_REQUIRE_2026-07-29.md:55` — "deleted at the v003 edit". Wrong twice:
  it is absent already at v002, and it was superseded, not dropped.
- `STAGE8_RESCALING_EXCLUSION_RECOVERY_ERRATUM_V001.md` — same attribution, in the governing chain.
  This one still needs a relay; it is the only affected artifact Codex owns.
- V001 of this tracker `:52-56, :63-65` — corrected here.
- V001 `:58-61` argued that `BID_MINIMAL_PUBLIC_CAUSAL_CELL_DERIVATION_V001` (07-24) "could not have
  known the requirement existed." **That framing is withdrawn.** The requirement was live and
  strengthened at v002 on 07-20; what 07-24 could not see was the v001 wording, not the requirement.

## 4. CORRECTION OF RECORD 2 — THE REQUIREMENT SURVIVES, AND THE LIVE CHANNEL LIST IS FIVE, NOT FOUR

`primitive_record_cell_selection_principle_v002.md:131-133`, hard failure rules 3 and 4 — the
construction BLOCKS if:

```
3. changing an admitted boundary condition, measure, regulator, or action
   partition changes `K_*` without a theory-derived exclusion;
4. `A` is rescaled after the unit U(1) character is fixed;
```

`provenance/primitive_record_cell_selection_preregistration_v002.json`, `required_construction`, last
item: **"a mutation audit over admitted geometry, clock, measure, regulator, and action-partition
alternatives."**

So Departure 2 was never discharged, never withdrawn, and is stated more sharply in the live version
than in the deleted one — it is a blocking condition rather than a remark. **But its channels are:**

| Live channel (v002) | V001 tracker channel | Change |
|---|---|---|
| geometry | 1 cell | maps across |
| clock | 2 duration | maps across |
| action-partition | 3 matter action | maps across, and is the sharper name |
| measure | — | **the tracker had it inside channel 4; it is its own channel** |
| **regulator** | — | **ABSENT FROM THE TRACKER ENTIRELY** |
| — | 4 field-energy integral | **not a live channel; see section 2** |

Note that v001 itself already enumerated the classes three inconsistent ways in 131 lines — `:105`
"clock, source, measure, or cell deformation", `:106-109` the four the tracker used, and `:118-119`
"clock, field, cell-shape, measure, and action-partition". **"Four channels" was an artifact of
picking the middle list.** v002 rule 3 plus the preregistration settle it at five.

Also live and unchanged from v001, and it belongs in the ledger: `v001:59-60` — "the microscopic
measure, gauge quotient, zero-mode prescription, and field domains are part of the selector." That is
the measure channel's content, spelled out.

## 5. THE FINDING THAT MATTERS MOST — THE MISSING CHANNEL IS SLOT 6

**REGULATOR is a live mutation channel of Departure 2 and the tracker did not have it.** And slot 6
is "parent-derived functional regulator + finite renormalization."

`EM_DEPENDENCY_ORDER_FREEZE_V001.md:32-34`, quoted in the register at Q-13: "Because zero bare `F^2`
is adopted, **the functional-regulator and finite renormalization step is where response
normalization can originate**."

Q-13 (2026-07-30 05:56, six hours before this audit ran) reached slot 6 from a completely different
direction — classifying all eighteen obligation slots by whether discharging them introduces a
dimensionful independently-fixed quantity — and named it "the most under-prioritised item in the
program," status merely "OPEN, PRINCIPAL-GUARDED."

**TWO INDEPENDENT LINES NOW TERMINATE AT SLOT 6: the slot classification, and the live mutation-channel
list of the one departure aimed at the scaling family.** PART-PROVABLE: the two citations are exact,
the convergence is an inference and is offered as one.

Q-13's unadjudicated slot-6/slot-12 contradiction applies here without change: if slot 12
(continuum-regulator independence, "no hidden finite selector") is discharged as written, slot 6
cannot supply a scale, and then the regulator channel of Departure 2 is closed by fiat and the
scale must come from somewhere else. That contradiction is now load-bearing in two places.

## 6. THE AUDIT CANNOT BE RUN YET, AND THIS IS THE SEQUENCING ERROR IN V001

`results/primitive_record_cell_joint_selector_readiness_v001.json` is the execution record of the
v002 route. Its `failed_authorization_checks`, verbatim, five of them:

```
complete_joint_operator_is_present
joint_operator_derives_stationary_proper_interval
joint_operator_derives_closure_residual
joint_operator_proves_unique_simple_positive_root
joint_operator_passes_mutation_audit
```

`adjudication`: "The stronger Primitive Record-Cell Principle is externally sealed and **would turn
alpha into a surface-selected eigenvalue if its joint operator were constructed.** The current post-C4
stack supplies the compact unit character, charged Dirac current, and response shape, but **it does
not yet instantiate `Gamma_K`, a stationary record clock, or `C_record(K)`.** Existence and uniqueness
language cannot substitute for those objects."

`next_gate`: "derive one complete target-independent `Gamma_K` and BR closure operator whose joint
stationary problem outputs `Delta_tau(K)` and a scalar `C_record(K)`."

*** THE MUTATION AUDIT IS THE FIFTH OF THE FIVE FAILED CHECKS, AND IT IS A CHECK ON THE OPERATOR. ***
`joint_operator_passes_mutation_audit` presupposes a `K_*(mutation)` to vary. There is no
`C_record(K)`, so there is no `K_*`, so there is nothing for a channel-by-channel audit to move.
**Running the four-channel audit today audits nothing.** V001 treated the audit as the work item; it
is the acceptance criterion of a construction nobody has performed.

APPLY THE PROGRAM'S OWN TEST. The mutation audit is a REQUIRE-shaped demand, which is why it looked
like the lever. But it is require-shaped ABOUT an object that does not exist. The require-shaped
*target* is `Gamma_K` + `C_record(K)`; the audit is how you would find out whether the target
succeeded. That distinction is the same one Q-11 turned on.

## 7. WHAT THIS DOES AND DOES NOT DO TO THE ADJACENT ROUTES

DO NOT CONFLATE THE V002 ROOT CONDITION WITH THE REFUTED `L_open` ROUTE. v002`:95-97, :104` poses
`C_record(K_*) = 0`, `dC_record/dK != 0` at `K_*`, `K_* > 0`, `alpha_micro = 1/(4 pi K_*)` — the same
first-positive-root shape as `primitive_same_cell_opening_normalization_principle_v001.md` (07-21, one
day later, plausibly its operator realization; the lineage is not asserted here).

Q-11 refuted that principle **as a fixer of `beta`**, on the ground that `beta` does not appear in
`L_open` so every member of `R = beta c Delta tau` satisfies the condition trivially. **That argument
does not touch `K_*`.** `K_*` is what `L_open` was built to select. And
`STAGE8_FIRST_OPENING_ROOT_PRINCIPLE_RECOVERY_INDEX_V001.md:70-79` retires the route by
NON-COMPUTABILITY, not refutation — `first_opening_root_computable_from_current_working_set = false`
— while leaving the question open in its own words: "Whether a first-opening root can be formed from
one microscopic CTP functional is open."

So: **the `beta` arm is refuted (Q-11); the `K_*` arm is unbuilt, and its non-computability verdict is
about the current working set, not about the mathematics.** Different targets, different verdicts. The
prohibition still binds: "the retired `L_open` subtraction may not be reused by renaming its terms."

## 8. NAMESPACE — A NEW UNREGISTERED COLLISION, AND IT SITS ON THE OBJECT THIS AUDIT POINTS AT

`Gamma_K` collides. In `primitive_record_cell_selection_principle_v002.md` it is **the complete
microscopic CTP functional indexed by the coupling `K`**. In the live cleanroom it is a BID amplitude
functional indexed by a cell set: `BID_MONOIDAL_EXTENSIVITY_DERIVATION_V001.md:34` —
`Gamma_K(A) = -log|A_K(A)|`, and `:51` `Gamma_K(A) = sum_i Gamma_(K_i)(A_i)`. 12 cleanroom files carry
the BID sense.

**Same symbol, different index set, different type, and the next-gate item of this audit is named
after it.** Register it before any lane writes `Gamma_K` in a Departure-2 context. This is the third
instance of the pattern after `C_R` and `K_H`.

CITATION FACT, same class as 718-of-821: **the only cleanroom file citing the live v002 principle is
`STAGE8_RESCALING_EXCLUSION_RECOVERY_ERRATUM_V001.md`, created 07-29.** v003 is cited once, v004 zero
times, and the readiness result zero times. The joint-selector route is outside the working set.

## 9. CHANNEL LEDGER V002 — UPDATE THIS TABLE, DO NOT REWRITE THIS FILE

| Channel (v002 authority) | Status | Blocking condition | Updated |
|---|---|---|---|
| geometry | GATED behind the joint operator | no `C_record(K)` exists to mutate | 2026-07-30 |
| clock | GATED behind the joint operator | same; `sqrt(2)` energy convention also open | 2026-07-30 |
| measure (incl. gauge quotient, zero-mode prescription, field domains, `v001:59-60`) | GATED, and never separately examined | same | 2026-07-30 |
| regulator | GATED, and ABSENT FROM V001 OF THIS TRACKER | same; and it is slot 6 | 2026-07-30 |
| action-partition | GATED | same; `Gamma_rest,*` never constructed | 2026-07-30 |
| ~~field-energy integral~~ | NOT A LIVE CHANNEL | superseded with the division rule, `v002:3-16`; live role is the `:111-123` implementation check | 2026-07-30 |
| bare rescaling `A -> lambda A` | CLOSED | compact unit winding; retained as v002 failure rule 4 | 2026-07-30 (unchanged from V001 §3) |

## 10. WHAT SURVIVES OF V001

- **§3, the closure of the bare rescaling.** Unchanged and correct.
- **§5, the three guards.** All three still bind, and guard 1 gains force: nothing here reaches slot 9,
  because `partial c_R / partial x = 0` and a shift is not a dilation.
- **§6, the ceiling.** Unchanged: discharging the exclusion is a NECESSARY condition on a selector, not
  a selector. It does not produce a number.
- **The judgment that Departure 2 is different in kind** from the other three departures. It is the
  only one that demands the scaling family be defeated, and v002 rule 3 makes that demand blocking.

## 11. WHAT V001 GOT WRONG

1. Channel 4 is not a live channel (§2).
2. "No supersession note" (§3).
3. The channel list is five, and one of the five was missing (§4).
4. The audit is an acceptance check, not the next work item (§6).

## 12. THE RECOMMENDATION, TAGGED

**PROVABLE, and executed in this document:** sections 1-4, 6, 8. Every claim carries file:line and a
verbatim quote; the bounded negative states roots and exclusions.

**PART-PROVABLE:** the slot-6 convergence in §5, and the `L_open` lineage guess in §7 (flagged as a
guess, not used).

**YOURS, PRINCIPAL:** three decisions, and the first two are the same decision seen twice.

1. **Does Departure 2 get re-pointed at `Gamma_K` + `C_record(K)`** — the readiness file's own
   `next_gate` — or does it stay a four-channel audit? If re-pointed, it stops being an audit and
   becomes the construction the whole program has been circling: the complete microscopic functional
   whose uniqueness four independent lines converged on 07-29.
2. **Does slot 6 get promoted?** Two independent lines reached it in six hours. It is currently
   "OPEN, PRINCIPAL-GUARDED", which is why neither line could act on it.
3. **Slot 6 vs slot 12** — Q-13's unadjudicated contradiction, now load-bearing in two places. If 12
   is discharged as written, the regulator channel closes and Departure 2 loses the channel that
   makes it interesting.

Not recommended: continuing the channel-by-channel audit as V001 posed it. It has no object to act on
until the operator exists, and it would produce artifacts that read as progress. That is precisely the
ALLOW shape.

alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
