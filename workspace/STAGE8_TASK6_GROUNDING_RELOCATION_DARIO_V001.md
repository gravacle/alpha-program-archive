# STAGE 8 / TASK 6 / TRANCHE — THE GROUNDING RELOCATION — DARIO V001

Lane: Dario (Claude Opus 5), cross-family reviewer
Task: PASTE 681 / Task 6 tranche — relocate the grounding for Batch 1's ten refusals
Authority: DoR-020-A8. **THIS ARTIFACT AUTHORIZES NOTHING AND LIFTS NO GATE.**
Custody: Batch 1's refusal is correct and binding; these are its work orders.

```text
REGISTER_HEAD = Q-605
RELOCATED = 1/10
TRUE_ABSENT = 9
CORPORA = 0 defined / 4 flagged (+1 candidate named for ratification)
VERB_AUDIT_SELF = CLEAN (+1 grounding of my own refuted, §2.1)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**One of the four leads is real; three are not, and one of the three was the one I
verified myself and was ready to sign.** The relocation pass returns a single
envelope to the S tranche. That is a thin result, and it is the honest one: the
corpus's derivations are prose and definition *schemas*, and the evaluator needs
graph *instances*.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-605 | verified (live-append tolerance) |
| Batch 1 refusal = `5bea1f59f119681d5a6161e324d2b6ebdea4d97510663ce27db639a2edcf1a1e` | **verified before reading** |
| Map = `e85a6113e5b45624d19f987ae2603f63ac418df10f33669cc6a44742e5918ed5` | verified (`STAGE8_TASK6_ENVELOPE_FORMALIZATION_MAP_LANE2_V001.md`) |
| Output collision | none — clear to write |

**The bar, carried verbatim from Batch 1:** a span grounds an argument only if its
bytes **determine** it — no edge, carrier, corpus member, normal form, or outcome
chosen. A requirement sentence is not a display; a blocker sentence is not a
display; a fragment whose nouns can be copied into JSON keys is not a display.

---

## 1. B1 — THE ONE RELOCATION

### `C-B-V009-06` — **RELOCATED**

```text
SOURCE  provenance/boundary_incidence_dynamics_preregistration_v011.json
        file sha256 13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd
SPAN    review_stage_semantics.stage_dependencies
        member span [18898,19830) ; value-object span [18920,19830) (910 bytes)
        span sha256 889515d30cedf7d3af5da1a9e1ff7c7a88a1bf0d9227bdf37d64113302dfcb86
        parses standalone as JSON: yes

POPULATES
  DAG args.graph            <- the 11-key object itself (child -> parent adjacency)
  DAG args.required_parents <- the same object's value arrays, literally
```

The object, in full:

```text
SPEC-SEAL                      <- []
CORE-RESULT-SEAL               <- [SPEC-SEAL]
PARENT-COMPARISON              <- [CORE-RESULT-SEAL]
HOLDOUT-UNIVERSE-SEAL          <- [SPEC-SEAL]
QSPEC-SPEC-SEAL                <- [SPEC-SEAL]
PREDICTION-MAP-SEAL            <- [HOLDOUT-UNIVERSE-SEAL, QSPEC-SPEC-SEAL]
THOMSON-RESULT-SEAL            <- [CORE-RESULT-SEAL, QSPEC-SPEC-SEAL]
ALPHA-RESULT-SEAL              <- [THOMSON-RESULT-SEAL, PARENT-COMPARISON,
                                    HOLDOUT-UNIVERSE-SEAL, PREDICTION-MAP-SEAL]
HOLDOUT-RESULT-SEAL            <- [ALPHA-RESULT-SEAL]
END-TO-END-RECONSTRUCTION-SEAL <- [ALPHA-RESULT-SEAL, HOLDOUT-RESULT-SEAL]
FINAL-CLAIM-SEAL               <- [END-TO-END-RECONSTRUCTION-SEAL, HOLDOUT-RESULT-SEAL]
```

**Why it determines, against each clause of the criterion:**

- *"every required parent is **literal**"* — the parents are explicit arrays, not
  derived from any status field.
- *"the graph is **acyclic**"* — **verified by me, not asserted**: a topological
  order over all 11 nodes computed without a cycle, every parent resolving to a
  declared node, exactly one root (`SPEC-SEAL`) and one sink (`FINAL-CLAIM-SEAL`).
- *"no **prose-only** dependency is accepted"* — the object is machine JSON, which
  is precisely the property the criterion demands and the ledger blocker said was
  missing.
- *"all nodes from **specification through final review**"* — `SPEC-SEAL` through
  `FINAL-CLAIM-SEAL`, the full closure.

**Nothing is chosen, and that is settled by a principal act rather than by me.**
`PREREGISTRATION_ENCODING_PRECEDENCE_PRINCIPAL_DECISION_2026-07-29.md`
(`70c4080eae018bd644a3f0694557f1c0e854d621aa61097c775737887fec528f`) rules at
:36-38 that *"`stage_dependencies` IS AUTHORITATIVE FOR GRAPH STRUCTURE — the node
set, the edges"*, at :19 that *"this is the encoding the evaluator consumes,"* and
at :49-50 that the ruling *"RATIFIES WHAT THE MACHINE ALREADY DOES … makes that
consumption authorized rather than incidental."*

[YOURS] That citation is what carries this envelope. The file contains a **second**
encoding, `stage_dag` (10 nodes), so selecting between them would otherwise be
exactly the carrier choice the bar forbids. The principal decision made the
selection, on the record, before this relay existed. **Also barred and worth
naming:** `/status/stage_dependency_graph_acyclic` is a boolean in the same file —
a *status* — and V010-12's criterion says "from report bytes, **not statuses**."
The DAG must be re-derived from the adjacency, never read off that flag.

---

## 2. B2 — THE NINE TRUE-ABSENT

Each was searched corpus-wide under M-2 all four modes (workspace including
`review_packets/`, `provenance/`, plus the sealed supervision decisions), and each
proposed grounding was put to adversarial refutation. **Every proposed grounding
across all nine was refuted.**

### 2.1 `C-B-V009-01` — and the lead I verified myself was refuted

The lead was specific: *"V009-01's carriers are V011:128-192 IN FULL."* I read that
range in the sealed packet copy (`aa7c6d49…`) and judged it a complete display:
`E_open` as a literal direct sum over an enumerated index `{M,Q,G}`, `iota_open`
with domain and codomain, and its action fixed as *"the identity on each displayed
object fiber and zero on all other vertex summands. No basis vector or metric
normalization is chosen here."* I was ready to relocate it.

**Three independent refutations, and they are right.** The decisive point I missed:
the passage opens *"For a first-opening object `K_open` with root vertex `r`,
endpoint vertices `p_h` …"* — it is **universally quantified**. It is a definition
**schema**, not an instance. `TYPE(g)` validates *"every object, domain, codomain,
decoration, identity, and composable edge in graph `g`"*, which requires a concrete
`g`; producing one from this passage means instantiating `K_open`, and that is
choosing a carrier. A secondary refutation is also correct: the span containing the
inclusion's action opens with the anaphor *"It is the identity…"*, whose referent
lies outside the span.

[YOURS] **I had the display in front of me and read "complete" where the bar
requires "instantiated."** The mathematics is fully determined; the graph is not.
That distinction is the entire content of Batch 1's refusal, and I reproduced the
error it was written to prevent.

The `M2` half is separately absent: the V005 row writes only "`M2` abstract-line
aliases" with **no `S` argument at all**, where every other M2 row in the spec names
its set (`M2(q_outcome,preseal_sources)`, `M2(q_unique,S_claim)`, …).

### 2.2 The other eight

| Envelope | What is missing after the search |
|---|---|
| `C-B-V010-12` | The `stage_dependencies` graph supplies the adjacency, but the criterion also demands *"every parent is **content-addressed**"* — the parents are stage **names**, 0 of 10 are digests — and the parent mutation and forbidden core-alpha mutation have no sealed machine instances. |
| `C-B-V008-10` | Same graph half available; but *"content hashes are **mandatory**"* fails for the same reason, and both `M2` scans lack a sealed source corpus (§3). |
| `C-B-V010-14` | `M2` has a query name (`q_silent_conversion`) and **no** sealed `preseal_sources`. A hand-picked list would make the demanded `hits=empty` true by construction. |
| `C-B-V010-11` | No complete decorated-category generator table anywhere: no closed object list, no `{name,domain,codomain}` morphism triples, no composition table. |
| `C-B-V009-08` | No citation-node set, no claim-node set with IDs, no typed entailment edges; and no bounded general-Fubini–Study authority corpus. |
| `C-B-V009-03` | No enumerated fiber/carrier object list — producing objects requires **choosing `L`** in `K_L=(Z/LZ)^4`, free at `L>=3`; restriction morphisms are never named or typed; no left/right normal forms for the global equality or the local blocks. |
| `C-B-V008-05` | The **repaired** word is displayed; the **competitor** normal form is not — corpus-wide hits for an inverse/opposite-holonomy expression: **zero**. No noncommuting plaquette fixture exists. |
| `C-B-V011-SP2-02` | The ledger's `c_partial = i Gamma_cell b_partial` is a lawful partial fact; domains/codomains, the declared square relation, both squared normal forms, and the alias-mutation AST are absent. |

**One near-miss, examined and refused — worth recording.** The literal opposite
plaquette word `T_mu T_nu T_mu^(-1) T_nu^(-1)` **does** exist, at
`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V008.md` byte 24207 and in the v008
preregistration JSON. It is the **superseded** artifact, and there the string is
the value of the *same symbol* `W_univ` — i.e. it is the defect the blocker
records, not the competitor normal form. Importing it would mean choosing a corpus
member **and** re-binding a colliding symbol across two artifact versions. Refused
on both grounds.

---

## 3. B3 — THE M2 CORPORA: **0 defined / 4 flagged**

All four M2-bearing rows are flagged: **no sealed corpus definition exists** for
any of them.

```text
C-B-V008-10   alpha/core and reconstruction/review dependency queries   NO SEALED CORPUS
C-B-V010-14   preseal_sources for q_silent_conversion                   NO SEALED CORPUS
C-B-V009-08   general-Fubini-Study authority corpus                     NO SEALED CORPUS
C-B-V009-01   abstract-line-alias sources                               NO SEALED CORPUS
              (and this row names no S argument at all)
```

[PROVABLE] A fixed-string search for a definition of any named source set —
`preseal_sources =`, `preseal_sources":` — returns **zero hits corpus-wide**. The
identifiers are used in descriptor rows and never defined.

**The one candidate, proposed and flagged rather than adopted:**

```text
review_packets/STAGE7_QSPEC_CANDIDATE_V001/STAGE7_PACKET_MANIFEST_V001.sha256
sha256 9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311
13,786 bytes ; 113 content-addressed member lines
```

This is a genuinely sealed enumerated member list — the right *shape* for a lawful
corpus. Two flags, both disqualifying until ratified:

1. **Adopting it is still choosing.** Nothing binds this manifest to these rows.
   It would need a ruling of the kind the precedence decision supplies for
   `stage_dependencies` — which is precisely why V009-06 relocates and these do not.
2. **It would not catch the historical aliases.** The superseded
   `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V009.md` — where the alias tokens
   actually live — is **not a member** of that manifest. A scan over it would
   return `hits=empty` for the wrong reason, which is the exact failure mode
   Batch 1 refused.

[YOURS] The general shape of the gap: **the M2 rows demand a scan but the spec
never says what to scan.** That is a specification defect, not an evidence
absence, and it will recur for every future M2 row until a corpus-definition rule
is installed.

---

## 4. B4 — BATTERY

### 4.1 Pre-seal pin check

| Claim | Verified before sealing |
|---|---|
| Batch 1 and map digests | both recomputed and matched before reading |
| `stage_dependencies` span and content | member span located by brace-matching; parses standalone; span digest computed |
| acyclicity | topological order computed by me; single root, single sink; no dangling parent |
| parents are names not digests | 0 of 10 match `^[0-9a-f]{64}$` |
| the status flag is barred | `/status/stage_dependency_graph_acyclic` located and excluded, per V010-12's "not statuses" |
| precedence decision authority | read in full; the three governing lines quoted |
| V009-01 lead | read in full at V011:140-163; refutation verified against the quantifier |
| V008 near-miss | located, and its cross-version symbol collision confirmed |

### 4.2 `F_PLDEC` and coverage

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. No descriptor, fixture, or chain was invoked. This is a
search over sealed bytes.

**Coverage, stated exactly (VERDICT-LINE SCOPE RULE):** I relocated one envelope
and classified nine TRUE-ABSENT on a bounded search. **`ABSENT` here is bounded
absence over the searched corpus, not proof of non-existence** — the same standard
Q-591 used. I did **not** serialize any envelope, did not change any
`check_record` to `available=true`, and **certify no envelope as buildable except
`C-B-V009-06`**, whose two DAG arguments I display in full.

### 4.3 Self verb audit

| My verb | Check |
|---|---|
| `RELOCATED = 1/10` | Thin, and reported as the result rather than padded. Nine envelopes leave the S tranche and join the 7A remainder. |
| The one relocation | Rests on a **principal act**, quoted, not on my judgment that the graph "looks like" the required one — which is exactly why it survives the carrier-choice objection that killed the others. |
| Acyclicity | Computed, not asserted, because the criterion demands it. |
| **My own lead refuted** | I verified V009-01's display, judged it complete, and was wrong: it is a definition **schema**, not an instance. Recorded in full at §2.1, including what I read past. |
| Near-miss refused | The opposite plaquette word exists in the superseded V008 and would have completed V008-05's competitor — refused for corpus-member choice and cross-version symbol collision, and disclosed rather than quietly dropped. |
| `CORPORA = 0/4` | The one candidate is **proposed with its two disqualifying flags**, not adopted; adopting it would be the same choosing the bar forbids. |
| Bounded absence | Named as bounded over the searched corpus, never as proof of non-existence. |

---

```text
RELOCATED = 1/10 (+span set:
  C-B-V009-06 -- provenance/boundary_incidence_dynamics_preregistration_v011.json,
  file sha256 13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd,
  member review_stage_semantics.stage_dependencies at bytes [18898,19830), value
  object [18920,19830), span sha256 889515d30cedf7d3af5da1a9e1ff7c7a88a1bf0d9227b
  df37d64113302dfcb86, parses standalone. It populates BOTH DAG arguments: args.graph
  is the 11-key child->parent object itself and args.required_parents is its value
  arrays, literally. Criterion met clause by clause -- parents LITERAL (explicit
  arrays, not status-derived); ACYCLIC VERIFIED BY ME (topological order over all 11
  nodes, no cycle, every parent resolving, single root SPEC-SEAL, single sink
  FINAL-CLAIM-SEAL); NOT PROSE (machine JSON, the precise property the blocker said
  was missing); and spanning specification through final review.
  NOTHING IS CHOSEN BECAUSE A PRINCIPAL ACT CHOSE IT: the file carries a SECOND
  encoding, stage_dag, so selection would otherwise be the carrier choice the bar
  forbids -- but PREREGISTRATION_ENCODING_PRECEDENCE_PRINCIPAL_DECISION_2026-07-29,
  sha256 70c4080eae018bd644a3f0694557f1c0e854d621aa61097c775737887fec528f, rules
  stage_dependencies "AUTHORITATIVE FOR GRAPH STRUCTURE -- the node set, the edges",
  calls it "the encoding the evaluator consumes", and states it "RATIFIES WHAT THE
  MACHINE ALREADY DOES". ALSO BARRED: /status/stage_dependency_graph_acyclic is a
  STATUS flag in the same file and V010-12 demands "from report bytes, not statuses".)
TRUE_ABSENT = 9 (+list: C-B-V010-12 and C-B-V008-10 -- graph half available but
  "content-addressed"/"content hashes mandatory" fails since parents are NAMES, 0 of
  10 digests, and their mutations and M2 corpora are absent; C-B-V010-14 -- query
  named, preseal_sources absent, and a hand-picked list would make hits=empty true
  by construction; C-B-V010-11 -- no decorated-category generator table anywhere;
  C-B-V009-08 -- no citation/claim node sets, no typed entailment edges, no bounded
  FS authority corpus; C-B-V009-01 -- see below; C-B-V009-03 -- objects require
  CHOOSING L in K_L=(Z/LZ)^4, free at L>=3; C-B-V008-05 -- the repaired word is
  displayed, the COMPETITOR normal form is not, zero corpus-wide, and no noncommuting
  fixture exists; C-B-V011-SP2-02 -- one lawful partial formula, no domains/codomains,
  no square relation, no alias AST. ABSENT here is BOUNDED absence over the searched
  corpus, not proof of non-existence.
  NEAR-MISS REFUSED AND DISCLOSED: the literal opposite plaquette word
  T_mu T_nu T_mu^(-1) T_nu^(-1) DOES exist at BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_
  V008.md byte 24207 -- but in the SUPERSEDED artifact, as the value of the SAME
  symbol W_univ, i.e. it is the defect the blocker records. Importing it means
  choosing a corpus member AND re-binding a colliding symbol across versions.)
CORPORA = 0 defined / 4 flagged (C-B-V008-10, C-B-V010-14, C-B-V009-08, C-B-V009-01
  all lack any sealed corpus definition; a fixed-string search for a definition of
  any named source set returns ZERO hits corpus-wide -- the identifiers are used in
  descriptor rows and never defined, and the V009-01 row names no S argument at all.
  ONE CANDIDATE PROPOSED, NOT ADOPTED: STAGE7_PACKET_MANIFEST_V001.sha256, sha256
  9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311, 113
  content-addressed members -- the right SHAPE, with two disqualifying flags:
  (a) nothing binds it to these rows, so adopting it is still CHOOSING and it needs
  a ruling of the kind the precedence decision supplies for stage_dependencies;
  (b) it would not catch the historical aliases, since the superseded V009 artifact
  where those tokens live is NOT a member -- a scan would return hits=empty FOR THE
  WRONG REASON. The general shape: the M2 rows demand a scan and the spec never says
  what to scan. That is a SPECIFICATION DEFECT, not an evidence absence, and it will
  recur for every future M2 row until a corpus-definition rule is installed.)
VERB_AUDIT_SELF = CLEAN (+1 grounding of my own refuted and recorded in full: I read
  V011:140-163, the named V009-01 lead, judged it a complete display and was ready to
  relocate it. It is UNIVERSALLY QUANTIFIED -- "For a first-opening object K_open
  with root vertex r, endpoint vertices p_h..." -- so it is a definition SCHEMA, not
  a graph instance, and TYPE(g) needs a concrete g. I read "complete" where the bar
  requires "instantiated", which is the exact error Batch 1's refusal exists to
  prevent. The mathematics is fully determined; the graph is not.)
```

Nine of ten envelopes leave the S tranche, and the one that stays does so because a
principal act had already ruled which of two encodings the machine consumes — not
because its bytes looked sufficient. That is the difference the whole pass turned
on, and I only saw it clearly after my own reading of the V009-01 lead was refuted
on the same ground I had used to accept it.
