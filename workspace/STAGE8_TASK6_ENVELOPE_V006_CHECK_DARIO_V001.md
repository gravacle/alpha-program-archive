# STAGE 8 / TASK 6 / TRANCHE — BOUNDED CHECK: THE V009-06 ENVELOPE AND SPECIFICATION V006 — DARIO V001

Lane: Dario (Claude Opus 5), cross-family reviewer
Task: PASTE 683 / Task 6 tranche — the envelope (`832a3c10…`) and spec V006 (`1b8b03e4…`) vs base V005 (`f8d1a7dc…`)
Authority: my own relocation `69334875…` is the grounding of record. **THIS ARTIFACT INVOKES NOTHING.**

```text
ENVELOPE = CONFIRMED byte-exact (+1 finding against my own grounding)
SPEC_V006 = content CONFIRMED; registry 17/17 by independent re-derivation (+4 findings)
RUN_PIN = lawful for 023 (+A's stated ground is insufficient; the sufficient grounds differ)
READY_FOR_RUN_023 = yes
VERB_AUDIT_SELF = CLEAN (+2 findings of mine withdrawn, +3 near-misses, +2 subagent claims refused)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**Preflight.** All four stated digests verified before reading. Output name absent.
Register head `Q-607` present; `Q-606` records the relocation. Builder A's `.py`
files were **not read**; where §4.1 declares their digests I verified by hashing
only, which discloses nothing. Two facts in this relay are obtainable only from
A's code; both are named as gaps, not taken.

---

## 1. D1 — THE ENVELOPE: CONFIRMED BYTE-EXACT

Every figure below was recomputed from the sealed source, not read from the report.

### 1.1 Payload bytes

```text
source  provenance/boundary_incidence_dynamics_preregistration_v011.json
        13cf1e17…  36,108 bytes                                    VERIFIED
member  [18898,19830)  932 B  sha 47e7c329…                        VERIFIED
value   [18920,19830)  910 B  sha 889515d3…                        VERIFIED (= my 681 value)
        18920 - 18898 = 22 = len('"stage_dependencies": ')          consistent framing

payload …--C-B-V009-06-stage_dependencies.member
        932 B ; BYTE-IDENTICAL to source[18898:19830] = True
        filename digest == content digest = True ; no trailing newline
```

The member digest `47e7c329…` is new here; my 681 published only the value-object
digest. They agree on the spans, and A's is the strictly more useful pin because
it covers the key name as well as the value.

### 1.2 DAG-argument serialization

```text
payload …--C-B-V009-06-dag-args.json   1218 B  sha 344fecdc…       VERIFIED
canonical round-trip identical = True ; keys sorted ; tight separators ; no trailing NL
graph == required_parents == json.loads(source[18920:19830]) = True ; 11 nodes
value arrays preserve SOURCE order (not sorted); only keys are sorted            correct
A's §2.1 eleven-row node/parent table == source order and values, row by row      11/11 OK
```

Faithful to my grounding as commissioned: the dict is the adjacency and its value
arrays are the required parents. **§1.5 records why faithfulness to my grounding
is not sufficient.**

### 1.3 The barred encoding and the status field

```text
member   contains 'stage_dag' / 'status' / 'acyclic' : False / False / False
dag-args contains 'stage_dag' / 'status' / 'acyclic' : False / False / False
```

Structural, not filtered: in the source, `stage_dag` sits at offset 17106 and the
`status` object at 23998 — both outside `[18898,19830)`. Nothing was excised.

### 1.4 Manifest row, roots, and the criterion conjuncts

```text
manifest 007b01f7…                                              VERIFIED
check_records 56 ; available 1 (C-B-V009-06) ; absent 55
input_root      e368211b…   recomputed over the two input files    MATCH
declared_root   1fbb3c07…   recomputed over 12 payloads            MATCH
CONTROL: old root e7820ca5… recomputed over the prior 10           MATCH
```

The control matters more than the result: the **same recipe** reproduces both
endpoints of the transition, so the root moved for the stated reason and no other.
Method is my 657 convention (`relative_path` = the filename, spec V005 :288-292).

The three criterion conjuncts, computed by me, not asserted:

```text
1. every required parent is literal   parents ⊆ nodes, 0 dangling, all strings   True
2. the graph is acyclic               Kahn topological order covers 11/11        True
                                      single root SPEC-SEAL ; single sink FINAL-CLAIM-SEAL
3. no prose-only dependency           no free text among parents                 True
```

[PROVABLE] **This is not a row verdict.** The chain produces verdicts; I confirm
that the envelope's contents are consistent with the criterion's structural
conjuncts. No member was bound and no fixed point was executed.

### 1.5 [PROVABLE] THE FINDING — the descriptor names two objects; the envelope supplies one, twice

The opcode contract, V006 line 325:

> `DAG(G,P)` — Parse nodes and exact parent lists, reject cycles/self-parenting/
> missing parents, **and compare with required parents `P`**.

Every parenthesised `DAG` invocation in the spec supplies **two distinct symbols**:

```text
C-B-V008-09     DAG(G_dependencies,P_dependencies)
C-B-V010-02     DAG(G_c_selector_parents,P_c_selector)
C-B-V010-03     DAG(G_selector_parents,P_sel)
C-B-V011-MR-06  DAG(G_prep_parents,P_prep_parents)
C-B-V011-SP1-08 DAG(G_mass,P_mass)
```

`C-B-V009-06` carries a **bare** `` `DAG` `` with no operands, and the binding
`r_auto_01_dag := DAG(graph,required_parents)` exists nowhere in the spec:

```text
occurrences in V006 of 'r_auto_01' / 'required_parents' / 'graph,required'  =  0 / 0 / 0
```

The binding is Builder A's materializer's synthesis. With `G = P` — the same
object in both operands — the clause *"compare with required parents `P`"* is
`compare(X,X)` and **cannot fail**. The row's own input column asks for *"machine
seal graph **and** parent schema"*: two objects. One was supplied for both.

**This follows from my own 681 grounding**, which the commission cites as
controlling and which says the one object populates both `DAG` arguments. That is
a correct reading of the source and an incomplete reading of the opcode. I checked
what the encoding *is* and never checked what the opcode *does with two operands*.

Scoped exactly: the parse/reject half is live and I computed it True; the compare
half is inert. The row can still light up on real structural work — acyclicity
over 11 nodes is not nothing — but **what it proves is half the opcode**, and that
must be recorded rather than counted as a discharged obligation. Three cures, in
my order of preference: (a) rule explicitly that for a bare-`DAG` row with one
authoritative encoding `P := G`, and record the comparison as inert; (b) source
`P` from a second sealed display — 681 found none, so this needs new grounding;
(c) withhold the row. **(a) costs one sentence and loses nothing that is presently
being gained.** I do not choose; the choice is a principal act.

### 1.6 What I could not check, and one gap named rather than taken

The manifest also stores the full `graph`/`required_parents` objects **inline** at
`evidence.invocations[0].args`. I verified the inline object canonicalizes
byte-for-byte to the 1218-byte payload — but nothing *declares* that invariant:
`input_root_sha256` covers the two files only, the inline args carry no digest
field, and the closed four-field evidence contract does not require agreement.
**Which one the producer reads is determinable only from `producer.py`. That is a
GAP, not a peek — I did not open it.** If the producer reads the inline args, the
payload files and the `instance_id` span binding are decorative.

Second gap: `observed result digest = 87fa71f2…` and the `DAG.success = true`
self-check are A's tooling's outputs with no reproduction recipe in the spec
bytes. I neither confirm nor dispute them.

---

## 2. D2 — SPECIFICATION V006

### 2.1 The corpus rule is faithful to the Q-606 finding

Q-606 recorded that no sealed corpus definition exists for any `M2` row — *"the
M2 rows demand a scan and the spec never says what to scan"* — and flagged the one
right-shaped candidate for two reasons: nothing bound it to those rows, and it
would have returned `hits=empty` for the wrong reason.

V006 §2 answers both. It requires `S` to name a `SEALED_CORPUS_DEFINITION` with
member paths, byte lengths, SHA-256 values and a content root; it rejects
directory inference, inline ad hoc sets, generic source-set labels and
evaluator-inferred sets; it makes an unsatisfied row `SPEC-INCOMPLETE` with
evidence unavailable, `M2` not started and PASS unreachable; and it bars *"choosing
members after the query is known."* That last clause is the anti-tuning half of my
second flag. **Faithful.**

Control that the law is not self-satisfying: `SEALED_CORPUS_DEFINITION` occurs in
exactly one file in the workspace — V006 itself. No corpus of record exists, so no
row can be populated by the rule that created the requirement.

### 2.2 The 17-row registry — re-derived, EXACT set equality

I over-generated: every row containing the token `M2` anywhere, over all 66
descriptor rows, then compared sets both ways.

```text
descriptor rows parsed   V005 66 / V006 66   (63 C-B- blocker + 3 C-D- discrepancy)
class partition          56 STRUCTURAL / 10 GATED-EXECUTION in BOTH
ID sets equal            True
ROWS BYTE-IDENTICAL      66 / 66
M2 sweep                 17 rows
sweep == V006 registry   True   (sweep-only: none ; registry-only: none)
spec §2 table IDs == report §3.2 table IDs, order-identical
declared S operands vs row bytes   17/17 correct (12 named, 5 genuinely unnamed)
Q-606's four seeds present, +13 mechanically found
```

Completeness beyond the declared scope: I swept the 49 rows *outside* the 17 for
corpus-shaped language (`sources|corpus|corpora|scan|search|aliases|occurrence`).
**Zero hits.** The registry is complete not merely for the `M2` token but for
corpus-shaped demands generally. `M-2` occurs elsewhere in V006 only as the
battery name, never as a row invocation.

**Registry verdict: CONFIRMED, 17/17, by independent re-derivation.**

### 2.3 [PROVABLE] CARRIAGE — assignment complete; one declared figure wrong

```text
diff -U 3 (as declared)   4 hunks, ranges EXACTLY as declared
H01 -1,18 +1,17    +8  -9      H02 -21,20 +20,23   +10 -7
H03 -326,6 +328,47 +41 -0      H04 -1979,11 +2022,10 +4 -5
UNASSIGNED = 0 ; MULTIPLY_ASSIGNED = 0 ; C-V5a disjointness trivial (4 hunks, 4 rows, 1:1)

FINAL_DELETIONS  = 21   declared 21   CORRECT
FINAL_INSERTIONS = 63   declared 58   WRONG BY 5
```

Three independent confirmations, in increasing order of force:

1. **Arithmetic control.** V005 1989 lines → V006 2031 lines, net +42. `63−21 = 42`.
   `58−21 = 37`. 58 is not merely wrong under one convention; it is *impossible*
   for any line-based diff counting each line once.
2. **The certificate refutes itself from its own printed numbers**, without either
   file: the four declared hunk nets are `(17−18) + (23−20) + (47−6) + (10−11)`
   = `−1 + 3 + 41 − 1` = **+42**, printed nine lines above `58 − 21 = +37`.
3. **The mechanism, and the reason it is not a fresh mistake.** Added blank lines
   = 5; `63 − 5 = 58`. The certificate declares
   `COUNT_CONVENTION = … including blank lines` and then counts excluding them —
   the `grep -c '^+[^+]'` artifact. Deletions survive only by luck: zero deleted
   lines are blank.

**This is a regression against law settled inside the very document that commits
it.** V006 §12.7B H24 reads *"Correct the historical V003 insertion count from 248
to the blank-line-safe value 261"*; §12.7B and §12.7C both declare the convention
*"line beginning + or -, including a bare + or - blank line"*; §12.7 certifies
*"blank-line-safe counts shown above."* I reproduced all three predecessor
certificates and every declared figure is blank-line-safe and exactly right:

```text
V002->V003  21 hunks  261 ins (13 blank)  163 del   declared 261   OK
V003->V004  26 hunks  350 ins (31 blank)   86 del   declared 350   OK
V004->V005  26 hunks  409 ins (25 blank)  173 del   declared 409   OK
V005->V006   4 hunks   63 ins ( 5 blank)   21 del   declared  58   WRONG
```

248 is precisely the non-blank count of the V003 delta. The defect being repaired
at H24 is the one I raised at relay 635 — V006's own authority table cites that
artifact for *"blank-line-safe insertion correction"* — and the new certificate
commits it again. **Carriage assignment is complete; one figure is wrong; the
repair is one token.**

### 2.4 [PROVABLE] H03 EXCEEDED ITS DECLARED ASSIGNMENT

H03's assignment reads *"add **only** the §2 sealed-corpus law and complete 17-row
registry."* It also moved a fence:

```text
"No opcode invokes an approximate optimizer, stochastic search, desired target,
 measured constant, reader, or undeclared network service."

V005 line 330  nearest preceding heading: ### 2.2 Deterministic procedure opcodes  -> ALL 14 OPCODES
V006 line 373  nearest preceding heading: #### V006 sealed-corpus law for M2(q,S)  -> ONE OPCODE
```

The insertion went **between** the opcode table and the sentence that governs it.
Under any heading-scoped reading, a fence over the whole catalogue now sits inside
a subsection about one opcode. No byte of the sentence changed, which is exactly
why a hunk-count check cannot see it: this is what the C-V5 discipline exists to
catch and what a ranges-and-assignment check alone does not. **Cure: place the new
subsection after the fence sentence rather than before it.**

### 2.5 [PROVABLE] THE LAW IS NOT WIRED INTO THE CLOSED OPCODE TABLE

§2.2 introduces the table as *"a finite ordered list over this **closed opcode
set**."* The `M2(q,S)` row is **byte-identical to V005** and still reads *"Run
three guards over content set `S`…"* with no precondition. `SEALED_CORPUS_DEFINITION`
appears **exactly once in all of V006** — bolded as a normative type, then never
given a schema, a canonical serialization, or a content-root algorithm, and never
referenced by any of the 66 rows.

An implementer reading the closed opcode table alone gets pre-V006 `M2` semantics.
The law is real and it is adjacent to the machinery rather than in it.

### 2.6 [PART-PROVABLE] `SPEC-INCOMPLETE` — a fifth token with no carrier

```text
'SPEC-INCOMPLETE' occurrences   V005 0   V006 21
§2.3 (byte-unchanged, outside all four hunks): "The only row statuses are:
                                               PASS | FAIL | NOT_RUN_GATE | ERROR"
V006 registry table column header:            "V006 status"
```

Run 022's operative encoding shows what an evidence-absent structural row actually
emits: `status = FAIL`, `reason = "INPUT_INTEGRITY: STRUCTURAL_EVIDENCE_NOT_SUPPLIED"`,
`procedure_started = false`. So the four-value alphabet is not broken in the
ledger — the right reading is that SPEC-INCOMPLETE is a registry classification,
not a row status, and the column header should say so.

**I withdraw the stronger form I first drafted.** I had written that the two are
"indistinguishable" and that the Q-606 defect becomes "invisible." That is
overstated: V006's registry names all 17 rows explicitly, so the classification is
recorded — in the specification. The exact and defensible claim is narrower:
**it has no carrier in the run record.** A row blocked by a specification defect
and a row merely awaiting evidence produce the same status, the same reason string
and the same `procedure_started`, and they have different owners and different
cures — one is a specification act, the other an input act. That is the
absent-vs-empty principle this program ruled on at Q-591 and Q-601, and the cure
is a distinct reason token (e.g. `INPUT_INTEGRITY: CORPUS_DEFINITION_ABSENT`), not
a fifth status.

One collision is unresolved either way: `C-B-V011-SP1-04` is the single
GATED-EXECUTION row among the 17. §2.3 already fixes gated rows to `NOT_RUN_GATE`
when the gate is closed. Two mandatory dispositions now attach to one row with no
precedence rule.

### 2.7 [PROVABLE] SEALED IS NOT ADEQUATE — the corpus is an unregistered surface

```text
12 of the 17 registered rows have PASS conditions satisfied by an EMPTY M2 result.
C-B-V010-14's ENTIRE criterion is:  `r_m2.success and r_m2.hits=empty`
```

V006 makes a corpus sealed, content-addressed, pre-declared and non-tunable. It
does not make it **adequate to the question**. A perfectly sealed corpus that omits
the sources where a violation would live returns `hits=empty` and 12 rows PASS for
the wrong reason. Under BR-1 this is sharp: if the producer supplies the corpus
definition, then a producer-declared object carries the direction of 12 rows —
and *hash-pinning prevents substitution, not fabrication*. A pinned corpus that
omits the incriminating file is fabrication by omission.

I tried to refute this three ways and could not:

```text
§12.4  registers FOUR M-2 false-negative modes — regex metacharacters, line wraps,
       self-reference/scope, hyphen/space/underscore. ALL FOUR are query-technique
       modes operating on a fixed S. None is about membership of S.
§12.2  the closest hazard row, "a prior sample is presumed complete", is guarded by
       "all 66 rows appear individually in §§8.3 and 8.6" — ROW-scoped, not
       corpus-member-scoped. The hazard class is registered; the guard doesn't reach.
P0     requires content_root(evidence_files) = declared_root and
       every_required_input_present — integrity of the SUPPLIED set, not adequacy
       of the corpus.
```

**Corpus membership is a fifth false-negative surface, and V006 is the first
document that makes it nameable.** The rule as written is necessary and not
sufficient; what it still needs is a statement of who may supply a corpus
definition and under what authority, since for 12 rows that supplier decides the
outcome.

### 2.8 [PROVABLE] The envelope's quoted "installed law" is a paraphrase

The report §3.1 presents the law as a blockquote. That text **does not occur in
V006** (substring test: False). V006 reads *"For every invocation `M2(q,S)`, the
operand `S` **MUST name a `SEALED_CORPUS_DEFINITION`**…"*. The paraphrase drops the
type name and drops *"The implementation must verify the definition and every
member before `M2` starts"* — the only clause in the law carrying an
implementation obligation. A blockquote is a carriage claim; this one does not
carry. The bytes installed in the spec are correct; the report's display of them
is not.

### 2.9 Census denominators

`check_records` has 56 entries — exactly the 56 STRUCTURAL rows. The 10
GATED-EXECUTION rows have **no evidence record of any kind, not even
absent-of-record**. So *"available 0/56 → 1/56, absent 56/56 → 55/56"* is 1/66 and
65/66 against the actual board. The denominators are not wrong, but only the
56-denominators are reported, and the same absent-vs-empty distinction applies:
a row recorded as absent and a row with no record are different states.

---

## 3. D3 — THE RUN PIN: LAWFUL FOR 023, ON DIFFERENT GROUNDS

### 3.1 The conclusion holds

```text
run 022 ledger spec_sha256                       f8d1a7dc…  (V005)
run 022 verifier.manifest.bound input_roots.spec f8d1a7dc…  (V005)
```

Keeping V005 for run 023 is lawful. Three grounds, each computed:

1. **Run 023 invokes no `M2`.** Exactly one row has evidence — `C-B-V009-06`, a
   `DAG` row, not among the 17. The other 55 structural rows fail at evidence
   before any opcode starts (`procedure_started=false` throughout run 022). The one
   new law cannot bear on any row in this run.
2. **Everything the chain reads as criteria is byte-identical.** 66/66 rows;
   partition 56/10; §8.3 board untouched (no hunk in §8); the §9.1 runtime, the
   authority firewall and the §9.5 aggregate blocks byte-identical, carrying
   `712a861a…`, `a9e7e50a…`, `bfad4441…` unchanged.
3. **Positively: pinning V006 would risk deviation.** V006 §2 is operative law
   over 17 rows, 16 of which reported `FAIL(INPUT_INTEGRITY)` in run 022. Whether
   `P0`'s `FAIL(INPUT_INTEGRITY)` or §2's `SPEC-INCOMPLETE` governs those 16 is
   **not determinable from the spec text**, so a V006 pin puts 16 of the
   preregistered 56 into an undetermined disposition.

### 3.2 [PROVABLE] A's stated ground is insufficient

The report grounds the pin on *"all 66 V006 descriptor rows are byte-identical to
V005."* That is true and does not carry the conclusion: **the spec is pinned as a
whole file**, not row by row. `spec_sha256` moves the moment any byte moves, and
V006 changes 2,859 bytes — including §2, which is precisely what a verifier
declaring `expectations_source: "sealed specification bytes"` consumes. Row
identity is a necessary condition A verified and not the sufficient one. The
sufficient grounds are §3.1 above.

### 3.3 [PROVABLE] The mechanical hazard nobody named: byte spans go stale by 2921

Three fixture records carry `partial_payloads[].span` into the V005 spec:

```text
FX-A35-03-C-FAMILY                      [122979,123168)   true V006 offset +2921
FX-A35-04-TAU-FAMILY                    [123168,123356)   true V006 offset +2921
FX-A35-05-PRIMITIVE-THOMSON-CONFLATION  [123356,123609)   true V006 offset +2921
```

At those same offsets V006 holds unrelated text. Today the pins are safe because
V005 is still the evidence payload — **and that is the hazard**: the package would
then hold a spec-of-record (V006) and an evidence-of-record (V005) that are
different files. Re-pointing at V006 without a migration rule **mis-resolves
silently rather than failing closed.**

### 3.4 What lineage V2 must carry

```text
new subject lineage root, single V005->V006 substitution   defa3eb9…   COMPUTED, NOT AUTHORIZED
  (control: the present root d09f6b30… reproduces exactly from the 6 declared members)
```

The lineage manifest lists V005 as a member, and its root is carried as
`input_root_sha256` on all 66 run-022 rows and as `subject_lineage.root_sha256` —
two of the five `common_member_key` slots. So V2 must carry:

1. **The new declared root, and both spec digests with an explicit supersession
   edge** `f8d1a7dc… → 1b8b03e4…`, so V2 rows remain joinable to the V005-rooted
   record rather than merely different from it.
2. **A span-migration rule** for the three fixture partial payloads — re-cut spans
   or a declared `+2921` offset — since silent mis-resolution is the failure mode.
3. **The relocation authority `69334875…` and the precedence decision `70c4080e…`.**
   Both live outside the lineage, the package and the evidence set; `C-B-V009-06`'s
   entire lawfulness rests on the second. If V2 drops them the one lawful row loses
   its ground.
4. **The evidence root kept distinct from the lineage root.** They are different
   objects (`1fbb3c07…` vs `defa3eb9…`); the manifest presently keeps them separate
   and V2 must not merge them.
5. **A carrier for `SPEC-INCOMPLETE` and a precedence rule against `P0`** (§2.6),
   or the 17 rows enter V2 as ordinary evidence gaps.
6. **A decision on the bare-`DAG` operand binding** (§1.5), since V2 is where the
   V009-06 row's coverage is recorded.

### 3.5 Two claims of mine withdrawn here

[YOURS] I drafted, and now withdraw, that a V006 pin *"breaks comparability with
runs 001–022."* §12.5 says *"Normal, optimized, and verifier results are compared
only at the same `common_member_key`"* — an **intra-run** join across three
parties, not a cross-run one. I also called it *"the Q-591 common_member_key"*; the
key is defined in A35 §12.5, and the Q-591 preregistration file contains no
occurrence of `common_member` or `input_root`. The arithmetic I published was
right and the consequence I drew from it was not.

I also withdraw *"required"*. The runtime pin (`spec_sha256`) and lineage
membership are **separate bindings**; whether A's materializer couples them is
determinable only from A's code. **GAP, named not taken.** The pin is lawful and
should be kept; it is not proven forced.

---

## 4. VERDICT UNDER THE VERDICT-LINE SCOPE RULE

Coverage, stated exactly. I verified: the two payloads byte-exactly against the
sealed source; the canonical serialization and its equality with the parsed member;
the absence of the barred encoding and the status field; the evidence root and the
per-row input root, each with a control; the manifest record's shape and the
descriptor pin's preimage; all 66 descriptor rows in both specs; the class
partition; the M2 registry by independent over-generating sweep with a
completeness probe beyond its declared scope; every declared `S` operand; the four
hunks, their ranges, their assignment and their true counts; the three predecessor
carriage certificates as controls; the three protected anchor blocks; the lineage
root and its V006 counterfactual; the three fixture spans; and all seven §4.1
package digests by hashing only.

I did **not** verify: A's `DAG.success`/observed-result self-check, the
`descriptor_terminators_excluded=66/66` transcript, the no-clobber assertion, the
register-head assertion, or which of the payload files versus the inline args the
producer reads. The first four are unverifiable from sealed bytes; the fifth is a
named gap in A's code. **No row outcome is claimed.**

### 4.1 Self verb audit

| My verb | Check |
|---|---|
| `CONFIRMED` on the envelope | Byte-identity computed against the source span, not the report; both roots reproduced with a control at each end. |
| **Finding against my own grounding** | §1.5 convicts my 681 relocation of licensing an inert comparison. I checked what the encoding is and never what the opcode does with two operands. Filed first, not last. |
| Two findings withdrawn | The descriptor-pin gap (§4.2) and the lineage "required"/"comparability" claims (§3.5). Both withdrawn on evidence, and the withdrawn text is displayed rather than deleted. |
| One finding narrowed | §2.6 — "indistinguishable/invisible" was overstated; the registry does record the 17. The narrow claim, no ledger carrier, survives. |
| Two adversarial claims REFUSED | §4.3. A subagent's finding is a candidate, not a result. |
| `insertions = 63` | Three independent confirmations, one of which needs neither file. Charged only after checking the certificate's own declared convention — the 635 rule. |
| A's code not read | Two facts named as gaps. Seven `.py`/manifest digests verified by hashing, which discloses nothing, and stated as such. |
| `READY = yes` | A readiness finding. I authorize nothing; the registrar invokes. |

### 4.2 [YOURS] The finding I refuted before raising it

I had drafted that `descriptor_sha256 = 0effdb71…` was not reproducible from
sealed spec bytes and that an independent reviewer could therefore not confirm row
identity. I tested ten candidate preimages before writing it. The second matched:

```text
SHA256(descriptor row bytes WITHOUT the trailing newline)  226 B
  V006 [41173,41399)  =  V005 [38252,38478)  =  0effdb71…   (byte-identical rows)
SHA256(the same row WITH the trailing newline)  227 B      =  060db9e9…
```

The pin is independently checkable and I was one convention — a single `\n` — from
charging a false gap. **The convention is worth recording for the next reviewer,
since nothing in the spec states it:** `descriptor_sha256 := SHA256(row bytes,
trailing newline excluded)`.

### 4.3 [YOURS] Two adversarial claims refused

An adversarial pass produced twelve candidates. Ten survived my own re-derivation
and are above. Two did not, and I record them because a reviewer who forwards a
subagent's finding unchecked has verified nothing:

- **"V006 §0.2 pins gate v012 `34faecbf…` while run 022 used v010 `2ad7f72a…` — a
  version divergence."** Refused. V006 §9.1 distinguishes the **runtime** gate
  (v010, `2ad7f72a…`) from the **logical** gate (v012, `34faecbf…`). Two objects,
  both pinned, no divergence.
- **"Every other sealed provenance JSON has a seal sidecar; this one does not."**
  Refused as stated. Five preregistration JSONs in that directory lack sidecars, so
  the series is not sidecar-sealed as a rule. The narrow true version stands and is
  modest: the grounding source is **hash-pinned by concurring citation of record,
  not sidecar-sealed**, so an independent verifier holding only the package can
  confirm the payload's digest but not that it is that span of that file.

### 4.4 [YOURS] Three near-misses of my own, disclosed

1. My first descriptor parse found **54 rows**, not 66: it missed the eight
   `**GATED-EXECUTION**` rows (bold markers in the class cell), the `C-B-V011-MR-04`
   row (unescaped pipes split it into nine cells), and all three `C-D-` discrepancy
   rows. Had I stopped there I would have charged the registry with two false
   extras, `MR-04` and `SP1-04`.
2. My operand cross-check keyed rows by first occurrence and landed on the §1
   blocker-census table instead of the descriptor tables, producing **12 false
   "operand not found" mismatches**. Caught by noticing that `M2(` matched zero
   times in rows that visibly contain it.
3. §4.2 above.

All three are the same failure: **a parser that under-reaches produces a charge, not
a null result.** That is the third relay in which an under-parse nearly became a
false finding, and the working rule it argues for is that a mechanical sweep must
publish its own denominator — here, 66 — and stop when the denominator is wrong.

### 4.5 `F_PLDEC` and the gates

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value
or any physical quantity. The graph computation is over prose seal-names.
`alpha_computed = false`; `proof_authorized = false`; `kappa_record_computed = false`;
no member bound; no fixed point; no end test; no numeric evaluation; no comparison
to any measured constant. `MACHINERY_APPEAL = none`.

**The Q-604 guard, stated arithmetically.** Run 022's verifier verdict is `FAIL`
with **59 findings**. This envelope clears exactly **one** row. If run 023 succeeds,
the verdict remains `FAIL` with 58. One lawful PASS row is one row.

---

```text
ENVELOPE = CONFIRMED (+1 finding, against my own grounding. Byte-exact: the 932-byte
  member payload is BYTE-IDENTICAL to source span [18898,19830) of 13cf1e17…; the
  1218-byte DAG-args payload is canonical, round-trips, and graph == required_parents
  == the parsed member (11 nodes, keys sorted, arrays in SOURCE order); the barred
  stage_dag encoding and the status field are absent from both payloads structurally,
  not by filtering; declared_root 1fbb3c07… reproduces over 12 payloads WITH THE OLD
  ROOT e7820ca5… REPRODUCED OVER THE PRIOR 10 AS A CONTROL, so the root moved for the
  stated reason and no other; input_root e368211b… reproduces; A's 11-row node/parent
  table matches the source row by row; and the three criterion conjuncts compute True
  (0 dangling parents, Kahn order 11/11, single root SPEC-SEAL, single sink
  FINAL-CLAIM-SEAL). THE FINDING: DAG(G,P) is specified to "compare with required
  parents P", every parenthesised DAG row in the spec supplies TWO DISTINCT symbols,
  and C-B-V009-06 is a BARE-DAG row whose binding r_auto_01_dag := DAG(graph,
  required_parents) occurs ZERO times in V006 -- it is the materializer's synthesis.
  With G = P the comparison clause is compare(X,X) and CANNOT FAIL; the row's own
  input column asks for "machine seal graph AND parent schema", two objects, and one
  was supplied for both. THIS FOLLOWS FROM MY OWN 681 GROUNDING: I checked what the
  encoding IS and never what the opcode DOES WITH TWO OPERANDS. The parse/reject half
  is live and computes True; the compare half is inert and must be RECORDED as inert
  rather than counted as a discharged obligation. One gap named not taken: whether the
  producer reads the payload files or the manifest's inline args is knowable only from
  producer.py, which I did not open.)
SPEC_V006 = CONFIRMED (+17-row registry verdict: EXACT SET EQUALITY. An
  over-generating sweep for the M2 token across all 66 descriptor rows returns the 17
  registry IDs and nothing else, both directions; all 17 declared S operands match the
  row bytes; the four Q-606 seeds are present with 13 mechanically found; and a
  completeness probe BEYOND the declared scope finds ZERO rows outside the 17 carrying
  corpus-shaped language, so the registry is complete for corpus demands generally and
  not merely for one token. 66/66 descriptor rows BYTE-IDENTICAL V005/V006; partition
  56 STRUCTURAL / 10 GATED-EXECUTION in both; the three protected anchor blocks
  byte-identical, carrying 712a861a… / a9e7e50a… / bfad4441…; the law is faithful to
  Q-606 on both flags and is not self-satisfying, SEALED_CORPUS_DEFINITION existing in
  exactly one file, V006 itself. FOUR FINDINGS. (1) CARRIAGE ARITHMETIC:
  FINAL_INSERTIONS = 63, declared 58. The certificate REFUTES ITSELF FROM ITS OWN
  PRINTED NUMBERS -- the four declared hunk nets sum to +42 while 58-21 = +37 -- and
  1989 -> 2031 lines confirms +42 independently. Cause: 5 added blank lines, the
  grep -c '^+[^+]' artifact, under a COUNT_CONVENTION that says "including blank
  lines". THIS IS A REGRESSION AGAINST LAW SETTLED INSIDE THE SAME DOCUMENT: V006
  §12.7B H24 repairs exactly this defect for V003 ("from 248 to the blank-line-safe
  value 261"), §12.7B and §12.7C both declare the convention, and all three
  predecessor certificates reproduce blank-line-safe and exactly right. Assignment is
  complete -- 4 hunks, ranges as declared, none unassigned or multiply assigned -- and
  the repair is one token. (2) H03 EXCEEDED ITS "add only" ASSIGNMENT: it was inserted
  BETWEEN the opcode table and the fence "No opcode invokes an approximate optimizer,
  stochastic search, desired target, measured constant, reader, or undeclared network
  service", which now sits under a subsection about ONE opcode instead of under §2.2
  and all fourteen. No byte of the sentence changed, which is why a hunk-count check
  cannot see it. (3) THE LAW IS NOT WIRED INTO THE CLOSED OPCODE TABLE: the M2(q,S)
  row is byte-identical to V005 and still carries pre-V006 semantics;
  SEALED_CORPUS_DEFINITION appears once, is never schema-defined, has no canonical
  serialization or content-root algorithm, and is referenced by no row. (4) THE
  ENVELOPE'S QUOTED LAW IS A PARAPHRASE -- it does not occur in V006 and it drops the
  sole implementation-obligation clause, "The implementation must verify the definition
  and every member before M2 starts". Plus two carried observations: SPEC-INCOMPLETE
  occurs 21 times in V006 and 0 in V005, sits in a column headed "V006 status" against
  a byte-unchanged §2.3 that closes the alphabet at four, and HAS NO CARRIER IN THE RUN
  RECORD -- a spec-blocked row and an evidence-absent row emit the same status, reason
  and procedure_started, though their owners and cures differ; and SEALED IS NOT
  ADEQUATE -- 12 of the 17 rows PASS on hits=empty, V010-14's whole criterion being
  r_m2.success and r_m2.hits=empty, so an under-inclusive but perfectly sealed corpus
  passes them for the wrong reason. §12.4's four false-negative modes are all
  QUERY-TECHNIQUE modes over a fixed S, §12.2's "prior sample presumed complete" guard
  is ROW-scoped, and P0 tests integrity of the SUPPLIED set: corpus membership is an
  unregistered fifth surface, and under BR-1 the supplier of a corpus decides 12 rows.)
RUN_PIN = lawful for 023 (+finding: A'S STATED GROUND IS INSUFFICIENT. The report
  grounds the pin on "all 66 V006 descriptor rows are byte-identical to V005", which is
  true and does not carry it -- the spec is pinned AS A WHOLE FILE, spec_sha256 moves
  the moment any byte moves, and V006 changes 2,859 bytes including §2, precisely what
  a verifier declaring expectations_source = "sealed specification bytes" consumes. The
  SUFFICIENT grounds are three: run 023 invokes no M2 at all, the only evidenced row
  being the DAG row C-B-V009-06 which is not among the 17; everything read as criteria
  is byte-identical including §8.3, §9.1, the firewall and §9.5; and POSITIVELY, a V006
  pin would RISK DEVIATION, because whether P0's FAIL(INPUT_INTEGRITY) or §2's
  SPEC-INCOMPLETE governs the 16 structural M2 rows is not determinable from the spec
  text, putting 16 of the preregistered 56 into an undetermined disposition. Also
  unnamed by anyone until now: three fixture partial_payload spans point into V005 and
  drift by EXACTLY +2921 under V006, where those offsets hold unrelated text, so
  re-pointing MIS-RESOLVES SILENTLY RATHER THAN FAILING CLOSED. LINEAGE V2 MUST CARRY:
  the new subject-lineage root -- defa3eb9… for the single V005->V006 substitution,
  COMPUTED AND NOT AUTHORIZED, with the present root d09f6b30… reproduced from the six
  declared members as a control; both spec digests with an explicit supersession edge;
  a span-migration rule for the three fixtures; the relocation authority 69334875… and
  the precedence decision 70c4080e…, which live outside the lineage and on which the
  one lawful row's entire lawfulness rests; the evidence root kept DISTINCT from the
  lineage root; a carrier and a P0 precedence rule for SPEC-INCOMPLETE; and a decision
  on the bare-DAG operand binding. TWO CLAIMS OF MINE WITHDRAWN HERE: "breaks
  comparability with runs 001-022" -- §12.5's common_member_key is an INTRA-run join
  across normal/optimized/verifier, not a cross-run one; and "the Q-591
  common_member_key" -- the key is defined in A35 §12.5 and the Q-591 preregistration
  contains no occurrence of common_member or input_root. I also withdraw "REQUIRED":
  the runtime pin and lineage membership are SEPARATE BINDINGS and whether A's
  materializer couples them is knowable only from A's code. GAP, named not taken. The
  pin is lawful and should be kept; it is not proven forced.)
READY_FOR_RUN_023 = yes (a readiness finding, not an authorization -- the registrar
  invokes. None of the ten findings touches bytes run 023 consumes: V006 is not
  consumed under a V005 pin, no M2 row runs, and the envelope itself is byte-exact with
  both roots reproduced against controls. TWO THINGS MUST BE RECORDED BEFORE THE RUN,
  NOT AFTER: that C-B-V009-06 exercises the parse/reject half of DAG and cannot
  exercise the compare half; and the Q-604 arithmetic -- run 022's verifier verdict is
  FAIL with 59 findings, this envelope clears exactly ONE, so a successful run 023
  leaves FAIL with 58. One lawful PASS row is one row.)
VERB_AUDIT_SELF = CLEAN (+2 findings of mine WITHDRAWN and displayed rather than
  deleted: the descriptor-pin gap, refuted by my own preimage test before it was ever
  raised -- 0effdb71… IS SHA256 of the descriptor row WITHOUT its trailing newline, 226
  bytes, V006[41173,41399) = V005[38252,38478), and I was one '\n' from charging a
  false gap, so I record the convention since the spec never states it; and the lineage
  claims at §3.5. +1 finding NARROWED: SPEC-INCOMPLETE is not "invisible", the registry
  does name all 17; the surviving claim is the narrow one, that it has no carrier in
  the RUN RECORD. +2 ADVERSARIAL CLAIMS REFUSED after my own check -- the "gate v010 vs
  v012 divergence", which is two distinct pinned objects, runtime and logical, not one;
  and "every other sealed provenance JSON has a sidecar", false, five preregistration
  JSONs lack one, leaving only the modest true version that the grounding source is
  hash-pinned by concurring citation rather than sidecar-sealed. A subagent's finding is
  a candidate, not a result. +3 NEAR-MISSES of my own: a first parse that found 54 rows
  instead of 66, missing bold-marked gated rows, a pipe-split row and the three C-D-
  discrepancy rows, which would have charged the registry with two false extras; an
  operand check that keyed on the §1 census table and produced 12 false mismatches; and
  §4.2. All three are one failure -- AN UNDER-REACHING PARSER PRODUCES A CHARGE, NOT A
  NULL RESULT -- and the rule they argue for is that a mechanical sweep must publish its
  own denominator and stop when the denominator is wrong.)
```

The envelope is byte-exact and the registry is exactly right, and neither of those
is the interesting result. The interesting result is that the one relocation I
authorised turns out to license an inert comparison, because I read the encoding
and not the opcode — and that a specification which repairs the blank-line counting
defect in three of its own certificates commits it again in the fourth. Both are
cheap to fix and neither is visible to the check that was run.
