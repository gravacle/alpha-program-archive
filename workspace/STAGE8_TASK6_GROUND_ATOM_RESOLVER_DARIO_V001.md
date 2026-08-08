# STAGE 8 / TASK 6 / BUILD — V010 ENVELOPE CHECK AND THE R9 GROUND-ATOM RESOLVER — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 700 / Task 6 — envelope-check V010, implement the resolver, as one delta
Authority: RD-22. **THIS ARTIFACT INVOKES NOTHING.**

```text
ENVELOPE = one statement only (+1 finding)
ROWS_CHANGED_CONFIRMED = 0
RESOLVER = implemented, executed (+3 negative controls; condition 2 refuses, gap named)
VERIFIER_ROOT = ddc09a3d5b29ca1a775f8e9db33c4479baa4bb28c46c6186ca82ebcf8b7385a4 (changed)
PIN_CLOSURE = 14 hits, all resolved
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 staleness of my own, of the exact class I charged at 697)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**Preflight, pins generated.** V010 = `31ccee9c…` (187,737 B); report
`STAGE8_TASK6_V010_GROUND_ATOMS_CODEX2_V001.md` = `bf6a132d…`; inventory =
`b4c103e6…`, **42 files**.

## 1. N1 — THE ENVELOPE

### 1.1 One statement, mechanical carriage

```text
66 descriptor rows      BYTE-IDENTICAL 66/66     rows changed = 0
criterion drift         none        procedure drift   none
partition               56 STRUCTURAL / 10 GATED-EXECUTION, both versions
carriage                6 hunks, 118 insertions, 21 deletions
                        2350 -> 2447 lines, net 97 = 118 - 21   SELF-CONSISTENT
```

### 1.2 [PROVABLE] The qualifying rule is closed — an iff, with no admission by example

V010-M1 defines a ground atom *"if and only if"* its normalized record validates
against `rd22.r9-ground-atom.v001` — 8 required fields,
`additionalProperties:false`, `atom_class` and `opcode` const, `mask` with
`maxItems:0` and `items:false`, `operand_order` a two-value enum — **and** five
source-binding conditions hold. The closure is explicit rather than illustrative:

> …only a `COMPARE` atom satisfying every field and source-binding condition
> above qualifies. `STRICT`, `SCHEMA`, `TYPE`, `EXACT`, `KERNEL`, `ENUM`,
> `DOMAIN`, `UNITS`, `DAG`, `M2`, `SYMBOLIC`, `SPECTRAL`, and `RUNTIME`, and
> every other `COMPARE` atom, are not ground atoms under this rule; no class is
> admitted by analogy.

All thirteen other opcodes are named as excluded, *and* so is every other
`COMPARE` atom. That is a closed rule, not an example.

### 1.3 [PROVABLE] A's zero-code-change claim, controlled against the bytes that RAN

Inventory self-consistency proves only that the inventory agrees with itself. The
control that matters is against run 031, the run whose fault this relay answers:

```text
ledger runner_sha256            a09f333a133deb28…   == parent.py on disk NOW    UNCHANGED
run-031 module ledger producer  3c27890533eebe48…   == producer.py on disk NOW  UNCHANGED
ledger verifier_sha256          10622f170b979ae8…   == MY V009-sealed root
```

So both files are unchanged relative to the run, not merely relative to a
manifest. And `verifier_sha256` shows **my sealed root ran** — the parent consumed
the instance, so relay 697's G2 hazard did not materialize.

### 1.4 [YOURS] G2 from relay 697 was acted on

```text
inventory 43 -> 42 files
inputs/verifier_root_members.generated.json: absent from the inventory AND from disk
inventory members mentioning 'verifier_root': none
```

The stale private census of my package is gone. That was the cure I named; I note
it because a finding that gets fixed should be recorded as fixed.

### 1.5 [PROVABLE] FINDING P1 — condition 2 states a requirement without a rule

V010-M1's second source-binding condition reads, in full: *"`member_key` resolves
exactly one row in R9's own P0-verified evidence table."* **It never says by what
mapping**, and the two objects do not share a namespace:

```text
member_key pattern           [A-Za-z_][A-Za-z0-9_]*      -- an IDENTIFIER
the V009-06 row's key        stage_dependencies_member
my P0 evidence table keys    47e7c329…--C-B-V009-06-stage_dependencies.member
                             (content-addressed relative paths, 18 rows)
sealed occurrences of `member_key` in V010: the schema field, its pattern, and
this one condition sentence. Nothing else.
`stage_dependencies_member` occurs in V010 ONLY inside the V009-06 row itself.
A's report says only "P0.evidence_files[member_key].sha256, recomputed by R9".
```

Two mappings are in reach and **V010 bars both**:

```text
(a) match the identifier against the payload FILENAME
    -> payload filenames are producer-authored, so the comparison's truth would
       depend on a producer CHOICE. Condition 5 forbids exactly that.
(b) take the row whose digest equals the constant
    -> then the comparison is COMPARE(X,X) and cannot fail. The V007/V010
       C-B-V009-06 row forbids that synthesis by name, and this lane convicted
       it at relay 683.
```

**So the atom is not resolvable without inventing a rule, and inventing one is
the fabrication BR-1 exists to prevent.** I do not invent it. What the spec must
add, precisely:

> the `member_key` → evidence-row mapping, stated in the descriptor or §9, which
> may be neither the payload filename (producer choice, barred by condition 5)
> nor the constant's own digest (`COMPARE(X,X)`, barred by the row).

The cheapest sufficient form: let the **descriptor** name the evidence row by the
same source-and-span citation it already carries — `stage_dependencies` at
`provenance/…v011.json` bytes `[18898,19830)` — and let R9 key its P0 table by
that citation. Both operands then come from sealed text and supplied bytes, and
the comparison stays non-vacuous. I record the option; the choice is a principal
act.

## 2. N2 — THE RESOLVER

`verifier/ground_atoms.py` implements everything V010 determines. Qualification
is by **construction and refusal**: an atom that fails one condition is not a
ground atom, and one that is neither carried nor qualifying is a named refusal.

### 2.1 [PROVABLE] Executed against the real sealed row

```text
normalize_ground_atom("r_ground", <the sealed V010 C-B-V009-06 row>) ->
  {schema: rd22.r9-ground-atom.v001,
   atom_class: P0_EVIDENCE_SHA256_EQ_SEALED_SPEC_SHA256,
   opcode: COMPARE, result_name: r_ground,
   evidence_operand: {source: P0.evidence_files,
                      member_key: stage_dependencies_member, field: sha256},
   constant_operand: {source: SEALED_DESCRIPTOR_CONSTANT,
                      constant_name: STAGE_DEPENDENCIES_MEMBER_SHA256,
                      value: 47e7c32915bc756f…},
   operand_order: evidence_left_constant_right, mask: []}
  8 fields, validates against the closed schema

normalize_ground_atom("r_dag", <same row>) -> None      NOT a ground atom
```

The record is built **only** from the sealed row: the atom shape is matched by a
pattern that admits nothing but the one V010 form, and the constant is required
to occur *literally* as `NAME=<64 hex>` in that same row (condition 4).

### 2.2 [PROVABLE] Refusals, executed

```text
closed-schema negatives, each REFUSED
  opcode DAG                  "not a ground-atom opcode; V010-M1 admits COMPARE only"
  atom_class altered          const violation
  mask non-empty              "mask must be empty (maxItems 0)"
  operand_order outside enum  closed enum violation
  schema wrong                const violation
  undeclared field            exact field inventory

condition 4 negative
  the constant's `=` removed from the row  -> REFUSED, naming the condition

condition 2, on the REAL P0 table (18 rows, P0.success = True)
  -> NAMED REFUSAL: member_key 'stage_dependencies_member' resolves 0 rows by
     exact key match; V010-M1 condition 2 requires exactly one but states no
     mapping … SPEC GAP …
```

The refusal is routed as `GROUND_ATOM` with row status
`PRECONDITION_NOT_REPLAYABLE`, **never a criterion FAIL** — the atom was not
evaluated, and a FAIL that was never evaluated is not a verdict.

### 2.3 [PROVABLE] The three negative controls

**Control A — the atom is non-vacuous.** Driven with the key supplied explicitly,
so the unstated mapping is exercised without being adopted:

```text
true member bytes (932 B)   success=True    rehashed 47e7c329… vs constant 47e7c329…
one byte appended (933 B)   success=False   rehashed 20b35aef… vs constant 47e7c329…
one byte changed            success=False   rehashed 8bd16b3d… vs constant 47e7c329…
```

A perturbed operand **flips** the atom, so this is not `COMPARE(X,X)`. Condition 3
is honoured literally: the operand is obtained by **rehashing the resolved row's
supplied bytes**, never by reading a declared digest.

**Control B — a smuggled producer `r_ground` is refused.**

```text
producer invocation {opcode: COMPARE, result_name: r_ground, args:{left,right,mask}}
 -> REFUSED: "r_ground is a V010-M1 ground atom; no producer carrier exists for it
    and a producer-emitted invocation or result object purporting to supply one is
    a contract fault under BR-1"
```

The check is structural: `recompute_results` computes the ground-atom name set
from the sealed row **before** consuming any invocation, so a producer cannot
occupy the name.

**Control C — the lawful carrier still works.** Run 031's real `r_dag`
invocation still recomputes alongside: `success True, 11 nodes, root SPEC-SEAL,
sink FINAL-CLAIM-SEAL`. The two provenances are disjoint and both live.

## 3. N3 — DELTA, RE-PIN, PIN CLOSURE

```text
NEW      verifier/ground_atoms.py      the closed rule, resolver and refusal
CHANGED  verifier/replay.py           recompute_results computes the ground-atom
                                      name set from the sealed row, refuses a
                                      producer carrier for one, and resolves the
                                      rest from R9's own sources
CHANGED  verifier/spec_census.py      +descriptor_row(); rows now carry their own
                                      sealed text, V010-M1's only atom source
CHANGED  verifier/verify.py           threads the row, criterion, P0 table and
                                      evidence index; routes GroundAtomRefusal as
                                      a refusal, not a FAIL
CHANGED  verifier/contracts.py        governing citation
CHANGED  contracts/verifier_verdict.schema.json (+sidecar)  spec const -> V010
CHANGED  selfcheck/selfcheck.py       +11 permanent M1 assertions
CHANGED  README.md                    governing spec name and digest
CHANGED  rd22.verifier-manifest.v001.json (+sidecar)
CHANGED  inputs/verifier_root_members.generated.json (+sidecar)

verifier_root_sha256  10622f17…  ->  ddc09a3d5b29ca1a775f8e9db33c4479baa4bb28c46c6
                                     186ca82ebcf8b7385a4        (CHANGED)
root MEMBERSHIP 13 -> 14 (ground_atoms.py; disclosed)
instance 5bfe149f… -> 1217571eadda90b114bf9f25433d7b8e9e58c6d9a114e3302c9659b637b2522f
members sidecar    -> c3f0b62d975d4b243618c92d9723937f706337011c22c2d0e15e46c4ad9bb403
package 23 files
```

### 3.1 Pin closure — value AND name

```text
0 files: 900a240d (V009 spec) / LANE2_V009 / 3b24fc39 / LANE2_V008 / d38d3171
0 files: every superseded root -- 10622f17, 5bfe149f, 43cff85d, fd59672a,
         f4943bf8 (an intra-relay root)
live V010 pin 31ccee9c present in exactly the four sites that should carry it:
         README, the instance, the verdict schema const, spec_census
14 hits resolved: 4 governing pin sites + 4 governing prose citations +
                  3 self-check labels + 2 stale-artifact regenerations + 1 (§3.2)
```

**Retained deliberately**, under the standing rule — *a reference that tells a
reader which bytes govern must move; a reference that names a law or records when
a decision was taken stays*: the identifiers `V008-R9-1/2/3`, `V009-J3`, `V009-J4`
and `V010-M1`, each of which **V010 itself retains** (checked, all six present in
the sealed text), and the self-check comment recording *when* the V005→V007 pin
incident happened. Before moving the four prose citations I confirmed each cited
passage carries forward into V010 — including one that needed
whitespace-normalized comparison, because a raw substring search failed on line
wrapping alone and would have suggested the sentence had been dropped.

### 3.2 [YOURS] A staleness of my own, of the exact class I charged at 697

My pin closure found `10622f17…` — the superseded V009 root — still live in **my
own** `inputs/verifier_root_members.generated.json`. I had regenerated the
instance and not the sidecar, so the sidecar carried the previous root and 13
rows while the package had 14.

That is precisely finding G2 from relay 697, one relay later, in my package
rather than A's: a generated census of a package's own membership, gone stale the
moment the bytes moved. The structural lesson is the one G2 stated and I did not
apply to myself — **a derived artifact must be regenerated in the same act that
changes what it derives from, or it must not exist.** Both are now regenerated
together, from final bytes, after every edit; the sidecar's root, the instance's
root and `package_root_digest()` are all one value, checked.

### 3.3 Every new path run, not read

```text
normalize (2 cases) / closed-schema negatives (6) / condition 4 (1) /
condition 2 on real inputs (1) / non-vacuity flip (3) / smuggled carrier (1) /
lawful carrier alongside (1)                                  = 15 executed
22-token argv end-to-end                exit 2, fault verdict emitted
dry run, both cwds                      exit 2; 372 B; 0x7d; rstrip==raw; stderr 0
self-check                              CLEAN, 23 files, 0 runtime asserts
```

## 4. PIN CHECK

| Claim | Verified before sealing |
|---|---|
| three preflight digests, 42 inventory files | generated and counted |
| 66/66 rows, 0 drift, partition held | computed on both files |
| carriage 6/118/21 self-consistent | computed |
| the rule is closed, not exemplary | quoted; all 13 opcodes + other COMPAREs excluded |
| A's zero-code-change claim | controlled against run 031's runner and module ledger |
| G2 acted on | inventory 43→42; file absent from disk and inventory |
| P1 — condition 2 states no mapping | all sealed `member_key` occurrences enumerated |
| both candidate mappings barred | by condition 5 and by the row's own prohibition |
| the record is built from the sealed row only | pattern + literal-constant requirement |
| six closed-schema negatives | executed |
| non-vacuity | 3 cases; a perturbed operand flips |
| smuggled producer carrier refused under BR-1 | executed |
| refusal is not a FAIL | routed as `PRECONDITION_NOT_REPLAYABLE` |
| root recomputed, membership 14 | `ddc09a3d…`; equals the instance and sidecar |
| members + instance + sidecar regenerated once, last | all three agree on one root |
| pin closure | 0 by value, 0 by name; retentions stated with their rule |
| dry run both cwds; 22-token argv | executed |

### 4.1 `F_PLDEC` and coverage

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. **The chain was not invoked**: the envelope check reads
sealed bytes, the resolver paths call pure functions on mirrored inputs, and the
launch demonstration is the dry run, which opens no run input. `alpha_computed =
false`; `proof_authorized = false`; `kappa_record_computed = false`; no member
bound; no fixed point; no end test; no numeric evaluation; no comparison to any
measured constant.

**Coverage, stated exactly.** I checked an envelope and implemented a resolver. I
claim **no check or fixture outcome**. Control A's `success=True` is a **driven**
demonstration with the member key supplied explicitly — it shows the comparison is
non-vacuous, and it is **not** a resolution of the atom, because the mapping that
would resolve it is what P1 says the spec lacks. **I do not claim run 032 passes**:
on today's spec `r_ground` will record `PRECONDITION_NOT_REPLAYABLE` naming the
condition-2 gap, which is the correct behaviour of a rule that requires a mapping
nobody has stated.

## 5. SELF VERB AUDIT

| My verb | Check |
|---|---|
| Pins generated, never transcribed | Three preflight digests, seven input roots, fourteen member digests. |
| Zero-code-change checked against the RUN | Not against the inventory, which can only agree with itself. |
| `ENVELOPE = one statement only` | Rows, drift, partition and carriage all computed; the rule's closure quoted rather than paraphrased. |
| **P1 stated, not guessed around** | Both reachable mappings are shown barred by V010's own conditions, so refusing is the lawful act and inventing one would be the fabrication. |
| A cure offered, not chosen | The descriptor's existing source-and-span citation is the cheapest sufficient key; the choice is a principal act. |
| Non-vacuity proven, not asserted | Three cases; and Control A is labelled a *driven* demonstration, not a resolution. |
| Smuggle refused structurally | The ground-atom name set is computed from the sealed row *before* any invocation is consumed. |
| **Own staleness disclosed** | My generated sidecar carried the superseded root — G2's own defect in my package, found by my own pin closure, with the structural lesson stated. |
| G2's fix recorded | A finding that gets fixed is recorded as fixed. |
| No claim on run 032 | The expected outcome is named, and it is a refusal. |

---

```text
ENVELOPE = one statement only (+1 finding) (V010-M1 and mechanical carriage:
  66/66 descriptor rows BYTE-IDENTICAL, zero criterion drift, zero procedure drift,
  partition 56/10 held, carriage 6 hunks / 118 insertions / 21 deletions with net 97
  reproducing the line delta. THE RULE IS CLOSED, NOT EXEMPLARY: an iff against
  rd22.r9-ground-atom.v001 -- eight required fields, additionalProperties false,
  atom_class and opcode const, mask maxItems 0, operand_order a two-value enum --
  plus five source-binding conditions, and the closure is explicit, naming all
  thirteen other opcodes AND "every other COMPARE atom" as excluded with "no class
  admitted by analogy". A'S ZERO-CODE-CHANGE CLAIM IS CONTROLLED AGAINST THE BYTES
  THAT RAN, not against the inventory, which can only agree with itself: run 031's
  runner_sha256 a09f333a… equals parent.py on disk now, and its module ledger's
  producer.py 3c278905… equals producer.py on disk now. The ledger's verifier_sha256
  is my V009-sealed root 10622f17…, so the parent consumed my instance and relay
  697's G2 hazard did not materialize -- and G2 ITSELF WAS ACTED ON: the inventory
  is 43 -> 42 files and inputs/verifier_root_members.generated.json is gone from
  both the inventory and disk. FINDING P1: CONDITION 2 STATES A REQUIREMENT WITHOUT
  A RULE. "member_key resolves exactly one row in R9's own P0-verified evidence
  table" never says BY WHAT MAPPING; member_key is an identifier pattern while my
  P0 table is keyed by content-addressed relative paths, and the sealed occurrences
  of member_key are exactly the schema field, its pattern and that one sentence. The
  two reachable mappings are both BARRED BY V010'S OWN TEXT: matching the identifier
  against the payload FILENAME makes the comparison depend on a producer CHOICE,
  which condition 5 forbids; taking the row whose digest equals the constant makes
  it COMPARE(X,X), which the C-B-V009-06 row forbids by name and this lane convicted
  at 683. So the atom is not resolvable without inventing a rule, and inventing one
  is the fabrication BR-1 exists to prevent. The spec must state the member_key ->
  evidence-row mapping; the cheapest sufficient form is to key R9's table by the
  source-and-span citation the descriptor ALREADY carries, but the choice is a
  principal act and I do not make it.)
ROWS_CHANGED_CONFIRMED = 0 (computed on both files, criterion column and procedure
  column separately, IDs set-equal, partition unchanged.)
RESOLVER = implemented, executed (+negative controls) (verifier/ground_atoms.py
  implements everything V010 determines, qualifying BY CONSTRUCTION AND REFUSAL
  rather than by example. Against the real sealed row, r_ground normalizes to the
  closed eight-field record -- built ONLY from that row, with the constant required
  to occur LITERALLY as NAME=<64 hex> in it -- and r_dag returns None, not a ground
  atom. FIFTEEN PATHS RUN, NOT READ. Six closed-schema negatives refused: opcode DAG,
  altered atom_class, non-empty mask, out-of-enum operand_order, wrong schema,
  undeclared field. Condition 4 refused when the constant's `=` is removed. Condition
  2 on the REAL P0 table of 18 rows with P0.success = True produces a NAMED REFUSAL
  citing the SPEC GAP, routed as PRECONDITION_NOT_REPLAYABLE and NEVER as a criterion
  FAIL, because the atom was not evaluated. THREE NEGATIVE CONTROLS: (A) the atom is
  NON-VACUOUS -- driven with the key supplied explicitly so the unstated mapping is
  exercised without being adopted, the true 932-byte member gives success True while
  one byte appended and one byte changed both give False, so it is not COMPARE(X,X),
  and condition 3 is honoured literally by REHASHING the resolved row's supplied
  bytes rather than reading a declared digest; (B) a SMUGGLED producer r_ground
  invocation is REFUSED under BR-1, and the check is structural because the
  ground-atom name set is computed from the sealed row BEFORE any invocation is
  consumed, so a producer cannot occupy the name; (C) run 031's real r_dag carrier
  still recomputes alongside -- success True, 11 nodes, root SPEC-SEAL, sink
  FINAL-CLAIM-SEAL -- so the two provenances are disjoint and both live.)
VERIFIER_ROOT = ddc09a3d5b29ca1a775f8e9db33c4479baa4bb28c46c6186ca82ebcf8b7385a4
  (CHANGED from 10622f17…; membership 13 -> 14 for verifier/ground_atoms.py,
  disclosed. Instance 1217571eadda90b114bf9f25433d7b8e9e58c6d9a114e3302c9659b637b25
  22f == manifest_sha256(); members sidecar c3f0b62d…; the sidecar's root, the
  instance's root and package_root_digest() are ONE value, checked. All three
  regenerated ONCE, LAST, after every byte change. Self-check CLEAN with 11 new
  permanent M1 assertions; 23 files; zero runtime asserts; dry run exit 2 from both
  cwds with 372 bytes ending 0x7d, rstrip() == raw, stderr 0; the 22-token argv
  parses end-to-end and emits the fault verdict at exit 2.)
PIN_CLOSURE = 14 hits, all resolved (swept BY VALUE AND BY NAME: the V009 spec digest
  900a240d and filename LANE2_V009 both zero, V008 and V007 both zero, and EVERY
  superseded root -- 10622f17, 5bfe149f, 43cff85d, fd59672a and the intra-relay
  f4943bf8 -- zero. The live V010 pin 31ccee9c is present in exactly the four sites
  that should carry it: README, the instance, the verdict-schema const and
  spec_census. RETAINED DELIBERATELY under the standing rule: the identifiers
  V008-R9-1/2/3, V009-J3, V009-J4 and V010-M1, each of which V010 ITSELF RETAINS --
  checked, all six present in the sealed text -- and the self-check comment recording
  WHEN the V005->V007 incident happened. Before moving the four prose citations I
  confirmed each cited passage carries forward into V010, including one that needed
  WHITESPACE-NORMALIZED comparison because a raw substring search failed on line
  wrapping alone and would have suggested the sentence was dropped.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. The envelope
  check reads sealed bytes, the resolver paths call pure functions on mirrored
  inputs, and the launch demonstration is the dry run, which opens no run input. NO
  OUTCOME IS CLAIMED: Control A's success=True is a DRIVEN demonstration with the
  member key supplied explicitly -- it shows the comparison is non-vacuous and is NOT
  a resolution of the atom, because the mapping that would resolve it is exactly what
  P1 says the spec lacks. I do NOT claim run 032 passes: on today's spec r_ground
  will record PRECONDITION_NOT_REPLAYABLE naming the condition-2 gap, which is the
  correct behaviour of a rule that requires a mapping nobody has stated.)
VERB_AUDIT_SELF = CLEAN (+1 STALENESS OF MY OWN, OF THE EXACT CLASS I CHARGED AT 697:
  my pin closure found the superseded root 10622f17… still live in MY OWN
  inputs/verifier_root_members.generated.json. I had regenerated the instance and not
  the sidecar, so it carried the previous root and thirteen rows while the package had
  fourteen. That is finding G2 one relay later, in my package rather than Builder A's:
  a generated census of a package's own membership, stale the moment the bytes moved.
  The structural lesson is the one G2 stated and I did not apply to myself -- A DERIVED
  ARTIFACT MUST BE REGENERATED IN THE SAME ACT THAT CHANGES WHAT IT DERIVES FROM, OR
  IT MUST NOT EXIST. Both are now regenerated together from final bytes. +NOTE: a raw
  substring search of mine suggested a cited spec sentence had been dropped from V010;
  whitespace-normalized comparison showed it carries forward and only the line wrapping
  had changed -- checked before it became a finding.)
```

The spec closed the ground-atom class properly: an iff, thirteen opcodes named out,
no analogy. What it left open is one arrow — from an identifier to a row — and the
two arrows within reach are each forbidden by a different clause of the same
statement. The resolver is built and every other condition passes; it stops at the
one place the spec stops, and says so in the verdict rather than in a FAIL.

And the finding I filed against Builder A one relay ago turned up in my own
package this relay, in the same shape, found by the same sweep.
