PASTE 135

Written 2026-07-30, for CODEX LANE 1. **A PASTE IS A SNAPSHOT.** Any ruling later than this overrides it
without notice. Lane 2 is registering the A32 ruling under paste 134 — that is what your commit is blocked
on. **Do not repair it, do not bypass the hook, do not touch A32 or slot-18 artifacts.** You handled that
correctly last turn; keep doing exactly that.

**YOUR SPEC IS REVIEWED: READY_WITH_CONDITIONS.** Review at
`MB Work/alpha_supervision/REVIEW_2026-07-30_gamma_k_construction_spec_hostile.md`, sha256
`27674c53f690398a62c288b8a700e6f97be31404f1aadc4a21ffc4559ff3f14a`. Subject verified at
`2d63dfadbb741c467b812f21e14f9e0e66015f1d86e2aa8307d8ae77acfe3d69`, 685 lines, sidecar verifies.

**ONE ITEM: discharge two conditions by APPEND-ONLY amendment. Still no execution.**

Fences unchanged. `alpha_computed = false; proof_authorized = false` on everything you write. Never touch
`a32_holdout/custodian_private/`.

---

### FIRST — THREE THINGS THE AMENDMENT MUST NOT WEAKEN

You strengthened your own spec beyond what paste 133 asked, and I want these preserved verbatim through
any amendment:

1. **Section 4's complementary-residual requirement.** You pulled in
   `primitive_zero_bare_induced_response_projection_principle_v004.md:131-138` — the route fails "if the
   scalar projection passes while the full operator residual does not" — and required that every
   complementary residual vanish before a scalar root is used. **Paste 133 did not ask for that and it
   closes the most likely way this construction produces a meaningless number.** Keep it.
2. **F-GK6, F-GK7, F-GK8.** Three falsifiers beyond the charter's five. F-GK8 in particular — making a
   hidden current-carrier conditionality a named failure rather than an oversight — is the right instinct.
3. **Section 2.2's refusal to choose an energy, and its scope line.** "This claim is scoped to the cited
   status block; it is not a corpus-wide search claim" is precisely the discipline the bounded-negative
   erratum installed, applied the same day. That sentence is a model for every future negative in this
   program.

### CONDITION 1 — ENUMERATE THE ADMITTED MUTATION FAMILY, PER CHANNEL. THIS IS THE MAIN ONE.

Section 5.2 names five channels — geometry, clock, measure, regulator, action-partition — and sets the
pass condition over "every admitted target-independent mutation." **The spec never enumerates what counts
as an admitted mutation in any channel.**

Why that is not a detail. Section 5.3 forbids narrowing the family "after seeing the root", and F-GK4
forbids an audit restricted to a pinned skeleton or cellulation. **Both guards act on narrowing that
happens after the root, or on a pinned carrier. Neither prevents a family chosen narrowly BEFORE the root
by a lane that can already see which mutations would be awkward.** An audit over an unenumerated family
is not falsifiable — there is no fixed set against which its completeness can be checked.

**REQUIRED: enumerate, per channel, the admitted target-independent mutations the audit will run.** In the
amendment, before execution. Same logic as frozen predictions: the set must exist before the outcome does.

**IF A CHANNEL'S FAMILY CANNOT BE ENUMERATED IN ADVANCE, SAY SO AND SAY WHY.** An honestly open family is
worth more than an implicitly narrow one, and "this channel's admitted family is not yet derivable, and
here is the missing object" is a finding I want rather than a gap I have to discover at execution.

Two anchors you already have: the exclusion's own live channel list at
`primitive_record_cell_selection_principle_v002.md:131-133` (hard failure rule 3 — "boundary condition,
measure, regulator, or action partition"), and the preregistration's "admitted geometry, clock, measure,
regulator, and action-partition alternatives." Neither enumerates members. If the corpus enumerates
members anywhere, cite it; if it does not, that is the finding.

### CONDITION 2 — CITE THE DERIVED EQUIVALENCE RELATION, OR DECLARE IT ABSENT

Section 5.2's pass condition requires mutations to be "physically equivalent under a derived equivalence
relation." **No such relation is specified, cited, or named anywhere in the spec**, and it is one of only
two ways a mutation can pass. As written, a mutation that moves the root could be declared equivalent
under a relation constructed for the purpose.

This is the program's characteristic failure in its recognized form: Q-11 records it as
match-by-name/fail-by-type, and Q-23 found the same shape in slot 18, where "unused" governs admissibility
and has no sealed definition. **An admissibility condition with an undefined predicate is not a
condition.**

**I RAN THE VERSION-LINEAGE CHECK MYSELF SO YOU DO NOT HAVE TO. THE ANSWER IS SPLIT, AND THE SPLIT IS THE
POINT.**

THE RELATION IS CITABLE. `primitive_record_cell_selection_principle_v002.md:55-56` — the live version —
carries the four members: "modulo gauge, public isometry, charge-conjugate orientation, and
Boundary-Resolved equivalence." **Cite that for the equivalence arm.**

**BUT THE CLAUSE THAT GAVE IT TEETH DID NOT SURVIVE.** v001`:40-42` read: "A continuous modulus that
changes any action integral or response coefficient is not a null transformation and fails the principle."
Measured: `physically null|null transformation` returns **2 hits in v001 and ZERO in v002, v003 and v004.**
The exclusion is v001-only.

Where the concern reappears is somewhere else doing a different job: v002`:82`, inside the UNIQUENESS
GATE — "no second inequivalent positive root or continuous modulus." That is a condition on ROOTS, not a
property of the equivalence relation.

*** SO THE LIVE EQUIVALENCE RELATION, AS CARRIED, DOES NOT ITSELF EXCLUDE A CONTINUOUS MODULUS THAT
CHANGES AN ACTION INTEGRAL. *** A mutation could be claimed equivalent under the four-member list, and the
only thing catching it downstream would be the uniqueness gate.

**WHAT THE AMENDMENT MUST DO — pick one and say which:**
(a) cite v002`:55-56` for the four members AND re-carry v001`:40-42`'s exclusion explicitly as a stated
    condition of the audit, noting it is recovered from v001 and why that is legitimate here (it constrains
    the relation, it is not the superseded division rule); or
(b) cite v002`:55-56` alone and state plainly that the equivalence arm cannot exclude continuous moduli,
    so the uniqueness gate at v002`:82` is the sole catch — and that the audit's conclusions are bounded
    accordingly.

**DO NOT do (a) silently.** Q-14 established that v001's division rule was superseded three minutes after
it was written, and the retirement index warns that a retired construction "may not be reused by renaming
its terms." Recovering a DIFFERENT clause from the same superseded file is defensible — the exclusion is
not the division rule — but it must be argued, not assumed.

### ALSO RECORD — SECTION 5 IS NOT YET A COMPLETE GATE

Your Section 5.3 note is correct and I am not asking you to change it: no tolerance can be set before a
numerical representation exists. **But add one line so no later lane misreads the heading:** Section 5 is
titled "Acceptance Criteria, Frozen Before Execution" and its tolerances are NOT yet frozen. They must be
frozen in the later executable spec, **before any root VALUE exists** — not merely before the solve is
written.

### PROHIBITED

Executing any step. Solving for `K_*`. Evaluating any response. Running the mutation audit. Rewriting
V001 — the amendment is append-only, as an amendment artifact or a V002 that preserves V001's bytes and
cites it. Choosing between `E_MS` and `E_BY`. Touching A32, slot-18, or lane-2 artifacts.

---

REPORT BACK: hashes, exact committed paths, gate verdict, deploy state, and for Condition 1 the per-channel
enumeration or the per-channel statement of why it cannot be enumerated. **If Condition 2's
null-transformation clause turns out not to survive into the live version, lead with that** — it would mean
the mutation audit has only one working pass route, which changes what the audit can conclude.

`alpha_computed = false; proof_authorized = false; kappa_record_computed = false.`
