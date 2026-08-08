# STAGE 8 / TASK 6 / BUILD — V011 ENVELOPE AND THE RESOLVER KEYED BY CITATION — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 702 / Task 6 — envelope-check V011, key the resolver by the citation
Authority: RD-22. **THIS ARTIFACT INVOKES NOTHING.**

```text
ENVELOPE = one statement only (+1 finding)
ROWS_CHANGED_CONFIRMED = 0
RESOLVER_KEYED = citation; r_ground does NOT yet resolve on real inputs (blocker named,
                 two parts); it resolves end-to-end on a citation-bound row and both
                 perturbation controls flip
VERIFIER_ROOT = 2cf5f313a44e12859d199184c863e92bc8662073a3695ffb2c0ea7f535900652 (changed)
PIN_CLOSURE = 16 hits, all resolved
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 defect in my own resolver, caught by running it, §2.2)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**Preflight, pins generated.** V011 = `d48e0fa7…` (191,830 B); report
`STAGE8_TASK6_V011_CITATION_KEY_CODEX2_V001.md` = `82873bd5…`; inventory =
`d1cd7e70…`, **43 files**.

## 1. P1 — THE ENVELOPE

### 1.1 One schema-only statement, mechanical carriage

```text
66 descriptor rows   BYTE-IDENTICAL 66/66     rows changed = 0
criterion drift      none        procedure drift   none
partition            56 STRUCTURAL / 10 GATED-EXECUTION, both versions
carriage             7 hunks, 111 insertions, 24 deletions
                     2447 -> 2534 lines, net 87 = 111 - 24   SELF-CONSISTENT
```

V011-O1 is a **closed JSON Schema and nothing else** — no prose conditions were
added alongside it. Its nine required fields include `p0_index`
(`table: R9.P0.evidence_files_by_citation`, `key_fields: ["source_sha256","span"]`,
`interval: ZERO_BASED_HALF_OPEN`, `match: EXACT_TUPLE_EQUALITY`,
`cardinality: EXACTLY_ONE`, `member_binding:
MEMBER_KEY_BINDS_EXACT_ROW_MATCHING_DESCRIPTOR_ATOM_CITATION`) and
`descriptor_citation` (`carrier:
SEALED_DESCRIPTOR_ROW.atom[result_name].source_and_span`, `source_sha256`, `span`).

**The mapping is closed exactly as commissioned.** `forbidden_mappings` is a
`const` array naming all three:

```text
["PAYLOAD_FILENAME", "CONSTANT_DIGEST_SELF_REFERENCE", "PRODUCER_SUPPLIED"]
```

No filename, no digest self-reference, no producer mapping — each barred by name
rather than by implication.

### 1.2 [PROVABLE] A's byte-unchanged claim, controlled against the bytes that RAN

```text
run-031 ledger runner_sha256   == parent.py on disk now        UNCHANGED
run-031 module ledger producer == producer.py on disk now       UNCHANGED
```

The inventory can only agree with itself; the run is the control that matters.

### 1.3 [YOURS] The census transcription is gone from the spec too

V010-M1 previously read *"The currently sealed Builder B package generates
thirteen rows, including `verifier/preconditions.py`"*. V011 replaces it with
*"The current census is carried only by the sealed manifest instance."* My row
count is no longer transcribed into the specification. That is the same defect
class as 697's G2 and my own 700 §3.2 — a derived census living somewhere it will
go stale — removed at the third site. Recorded because a defect that gets fixed
should be recorded as fixed.

### 1.4 [PROVABLE] FINDING Q1 — the citation key has no lawful carrier, in two parts

V011-O1 answers my P1 refusal by fixing the mapping. Applied to the actual
`C-B-V009-06` row, **one of the two key fields still cannot be obtained**:

```text
descriptor_citation.carrier = SEALED_DESCRIPTOR_ROW.atom[result_name].source_and_span
  -> so the SEALED ROW is the only lawful source of both fields.

what the row actually carries:
  span                                     [18898,19830)            present
  the source, cited by PATH                provenance/…v011.json    present
  the source's own SHA-256 (13cf1e17…)     ABSENT from the row
  64-hex digests in the row                exactly two:
        STAGE_DEPENDENCIES_MEMBER_SHA256 = 47e7c329…   (the atom's own constant)
        precedence decision              = 70c4080e…   (not the cited source)

13cf1e17… occurrences in the whole sealed V011:            0
13cf1e17… among the 19 supplied evidence payloads:         absent
the producer's invocation DOES carry it:
        source_sha256 = 13cf1e17… , span = [18898,19830)
        -> and forbidden_mappings includes PRODUCER_SUPPLIED
```

**Three readings, each barred by a different clause of the same statement:**

```text
take it from the producer's invocation linkage  -> PRODUCER_SUPPLIED (const)
take the atom's own constant as the source id   -> CONSTANT_DIGEST_SELF_REFERENCE (const)
resolve the path to a payload by name           -> PAYLOAD_FILENAME (const)
```

And R9 cannot verify a producer-supplied `source_sha256` even in principle,
because it does not hold the source file to hash — so that path is trust, not
verification, which is what BR-1 exists to refuse.

**The gap has two parts, and both are needed:**

1. **the descriptor row must carry the source SHA-256 bound to the span it
   already carries** — V011's carrier const is `…source_and_span`, one unit, and
   the row presently binds that span to a path;
2. **the cited source must be a supplied payload**, or R9 can derive no row's
   citation to match against: `R9.P0.evidence_files_by_citation` is keyed by
   `(source_sha256, span)`, and R9 can only compute that key for a source whose
   bytes it holds.

§2.3 demonstrates that the moment both arrive, the resolution works and stays
non-vacuous. I do not supply either — one is a specification act and one is an
input act.

## 2. P2 — THE RESOLVER, KEYED BY CITATION

### 2.1 What was implemented

`verifier/ground_atoms.py` now carries the V011-O1 machinery: the amendment's
nine-field closed record (built and closed before any byte is compared), the
`R9.P0.evidence_files_by_citation` index, `EXACT_TUPLE_EQUALITY` matching with
`EXACTLY_ONE` cardinality, and all three forbidden mappings as refusals.

The index is **derived, never read from a producer record**: for each supplied
payload treated as a candidate source, R9 slices the descriptor's span and keys
the result by `(sha256(source_bytes), span)`. Nothing in that uses a filename, a
producer citation, or the atom's own constant.

### 2.2 [PROVABLE] A defect in my own resolver, caught by running it

My first `descriptor_citation` took *"the one 64-hex in the row that is not the
atom's constant"* as the source identity. Run against the real row it returned
**`70c4080e…` — the precedence decision** — and refused with that as the claimed
source. The refusal's conclusion was right and its reason was wrong, and had the
precedence digest ever matched a supplied payload the atom would have resolved
**against the wrong bytes**.

Repaired: the digest must be **syntactically bound to the span** —
`<64hex>:[start,end)` — because V011's carrier const is `source_and_span`, one
unit. A digest merely present in the row is not a citation. Third relay running
in which running the code, not reading it, caught the defect.

### 2.3 [PROVABLE] Every path executed

```text
REAL INPUTS (19 payloads, P0.success = True, 19 evidence rows)
  -> NAMED REFUSAL: "descriptor_citation.source_sha256 has no lawful carrier:
     the carrier const is …source_and_span, ONE unit, but the row binds its span
     [18898,19830) to a PATH … SPEC GAP, two parts …", citing all three
     forbidden mappings by name.

DRIVEN: a citation-bound row + the source supplied
  -> RESOLVES: success True, evidence_sha256_rehashed 47e7c329… ==
     constant_sha256 47e7c329…, resolved_by R9, producer_carrier false

PERTURBATION CONTROLS, both flip
  one source byte flipped at the span   success False   rehashed 1a19764f…
  the span shifted by one               success False   rehashed ac628ab6…
```

The controls matter more than the resolution: they show the citation-keyed path
compares *rehashed source bytes* against the sealed constant and can fail. It is
not `COMPARE(X,X)`, and condition 3 is honoured literally — the operand comes
from rehashing the sliced source, never from a declared digest.

Retained from relay 700 and re-verified: `r_dag` is still **not** a ground atom;
six closed-schema negatives still refuse; a smuggled producer `r_ground` is still
refused under BR-1, structurally, because the ground-atom name set is computed
from the sealed row before any invocation is consumed.

## 3. P3 — DELTA, RE-PIN, PIN CLOSURE

```text
CHANGED  verifier/ground_atoms.py   +V011-O1 constants and inventories,
                                    +descriptor_citation (digest BOUND to span),
                                    +evidence_files_by_citation,
                                    +resolve_member_key_by_citation,
                                    +citation_amendment_record; resolve_ground_atom
                                    takes the descriptor row; the pre-V011
                                    exact-key path is retained and marked superseded
CHANGED  verifier/replay.py         passes the descriptor row into the resolver;
                                    governing citation
CHANGED  verifier/verify.py         governing citation
CHANGED  verifier/contracts.py      governing citation
CHANGED  verifier/spec_census.py    SPEC_SHA256 -> V011
CHANGED  contracts/verifier_verdict.schema.json (+sidecar)   spec const -> V011
CHANGED  selfcheck/selfcheck.py     +4 permanent O1 assertions; V011 labels
CHANGED  README.md                  governing spec name and digest
CHANGED  rd22.verifier-manifest.v001.json (+sidecar)
CHANGED  inputs/verifier_root_members.generated.json (+sidecar)

verifier_root_sha256  ddc09a3d…  ->  2cf5f313a44e12859d199184c863e92bc8662073a3695f
                                     fb2c0ea7f535900652        (CHANGED)
root MEMBERSHIP unchanged at 14 -- the root moved only because member bytes changed
instance  1217571e… -> d4219a53f26aa19dad3b1119ee7f1cc7d4c9816b64b02b3f1c1efbea7a884d8a
sidecar   c3f0b62d… -> a59ce9239a30af12ca5383cfdc34d0cd1fcb9cd5ab9a5ebd8e1500aabba54c13
package 23 files
```

**The 700 lesson applied.** The instance and the members sidecar are written in
**one act**, from final bytes, after every edit — and when the stale-reference
sweep forced a second round of edits I regenerated both again rather than patch
one. All three values agree: sidecar root == instance root ==
`package_root_digest()`, checked.

### 3.1 Pin closure — value AND name

```text
0 files: 31ccee9c (V010 spec) / LANE2_V010 / 900a240d / LANE2_V009 / 3b24fc39 / d38d3171
0 files: every superseded root -- ddc09a3d, 10622f17, and the intra-relay 5d37db4c
0 files: every superseded instance/sidecar -- 1217571e, 9682b652, c3f0b62d
live V011 pin d48e0fa7 present in exactly the four sites that should carry it:
        README, spec_census, the instance, the verdict-schema const
16 hits resolved: 4 governing pin sites + 4 governing prose citations +
                  3 self-check labels + 2 derived-artifact regenerations +
                  3 stale-docstring corrections (§3.2)
```

**Retained deliberately**, under the standing rule — *a reference that tells a
reader which bytes govern must move; a reference that names a law or records when
a decision was taken stays*: the identifiers `V008-R9-1/2/3`, `V009-J3`,
`V009-J4` and `V010-M1`, each of which **V011 itself retains**, and the
self-check comment recording *when* the V005→V007 pin incident happened.

### 3.2 [YOURS] Three stale docstrings, one of them a false claim

The sweep found `ground_atoms.py` still asserting *"Condition 2 — and this is
where V010 stops determining… SPEC GAP"*. **V011 determined it.** Left in place
that docstring would have told the next reader the opposite of the governing
spec — a stale comment that had become a false statement rather than merely an
old one. Repaired, with the historical reasoning kept and labelled as *why
V011-O1 exists*, and `resolve_member_key` marked superseded rather than deleted.

Two lighter ones moved with it: `V010 closes it explicitly` → `V010-M1 closes it`,
and one self-check label whose quoted string my earlier sweep missed because the
`fail(...)` call wrapped across lines.

### 3.3 Every touched path run, not read

```text
citation amendment record closed (9 fields, consts checked)        executed
real inputs -> named refusal, two-part gap                         executed
driven citation -> resolves True on the true member                executed
two perturbation controls -> both flip                             executed
r_dag not a ground atom; 6 schema negatives; smuggled r_ground      executed
22-token argv end-to-end                    exit 2, fault verdict emitted
dry run, both cwds                          exit 2; 372 B; 0x7d; rstrip==raw; stderr 0
self-check                                  CLEAN, 23 files, 0 runtime asserts
```

## 4. PIN CHECK

| Claim | Verified before sealing |
|---|---|
| three preflight digests, 43 inventory files | generated and counted |
| 66/66 rows, 0 drift, partition held | computed on both files |
| carriage 7/111/24 self-consistent | computed |
| one statement, schema-only | the hunk carries the JSON block and no prose conditions |
| mapping closed | `forbidden_mappings` const names all three |
| A byte-unchanged | controlled against run 031's runner and module ledger |
| Q1 — `source_sha256` has no lawful carrier | every candidate carrier enumerated and barred |
| §1.3's census claim | asserted with a raw search that failed on line wrapping; re-verified whitespace-normalized — see §5 |
| the source is not supplied | 19 payloads searched by digest |
| my own citation defect | reproduced, then repaired and re-run |
| driven resolution succeeds | rehashed digest == sealed constant |
| both perturbations flip | executed |
| root recomputed, membership 14 | `2cf5f313…`; equals the instance and the sidecar |
| instance + sidecar written in one act | all three roots agree; regenerated twice, together |
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

**Coverage, stated exactly.** §2.3's `success True` is a **driven** demonstration
on a citation-bound row with the source supplied — it proves the machinery and
the non-vacuity, and it is **not** a resolution of the real atom, because neither
of Q1's two parts is present today. **I do not claim run 032 passes**: on today's
spec and inputs `r_ground` will record `PRECONDITION_NOT_REPLAYABLE` naming the
two-part citation gap. That is a refusal, not a criterion failure, and it is the
correct behaviour of a mapping whose key field has no lawful carrier.

## 5. SELF VERB AUDIT

| My verb | Check |
|---|---|
| Pins generated, never transcribed | Three preflight digests, seven input roots, fourteen member digests. |
| Byte-unchanged checked against the RUN | Not against the inventory. |
| `ENVELOPE = one statement only` | Rows, drift, partition, carriage computed; the closure read off the `const` list. |
| **Q1 located, not guessed around** | Each of the three candidate carriers is shown barred by a named `const`, and the producer path is shown unverifiable rather than merely forbidden. |
| Both parts of the cure stated | One specification act, one input act; I supply neither. |
| **Own defect disclosed** | My first citation rule adopted the precedence-decision digest as the source identity — right conclusion, wrong reason, and dangerous had it matched a payload. |
| Non-vacuity proven | Two perturbations flip; the driven case is labelled *driven*. |
| Stale docstring treated as a false claim | It asserted the opposite of the governing spec once V011 landed; superseded rather than deleted. |
| Derived artifacts in one act | Instance and sidecar regenerated together, twice, when a second edit round was forced. |
| No claim on run 032 | The expected outcome is named, and it is a refusal. |
| **Own assertion corrected** | My pin check tested §1.3's census sentence with a raw substring and it failed on line wrapping alone; whitespace-normalized it holds, and the transcription is confirmed present in V010 and absent from V011. Third relay in which a raw search of mine tripped on wrapping — the rule is to normalize whitespace before concluding a sentence was dropped. |

---

```text
ENVELOPE = one statement only (+1 finding) (V011-O1 is a CLOSED JSON SCHEMA AND
  NOTHING ELSE -- nine required fields, no prose conditions alongside it -- plus
  mechanical carriage: 66/66 descriptor rows BYTE-IDENTICAL, zero criterion drift,
  zero procedure drift, partition 56/10 held, carriage 7 hunks / 111 insertions / 24
  deletions with net 87 reproducing the line delta. THE MAPPING IS CLOSED AS
  COMMISSIONED: forbidden_mappings is a const array naming PAYLOAD_FILENAME,
  CONSTANT_DIGEST_SELF_REFERENCE and PRODUCER_SUPPLIED, so no filename, no digest
  self-reference and no producer mapping, each barred by name rather than by
  implication; p0_index fixes the table, key fields, ZERO_BASED_HALF_OPEN interval,
  EXACT_TUPLE_EQUALITY match and EXACTLY_ONE cardinality as consts. A's
  byte-unchanged claim is controlled against THE BYTES THAT RAN at 031 -- the
  ledger's runner_sha256 equals parent.py on disk and the module ledger equals
  producer.py on disk -- because an inventory can only agree with itself. Also noted:
  V010-M1's transcription of MY row count is gone, replaced by "the current census is
  carried only by the sealed manifest instance", so the staleness class from 697's G2
  and my own 700 §3.2 is now closed at the specification too. FINDING Q1: THE
  CITATION KEY HAS NO LAWFUL CARRIER, IN TWO PARTS. The carrier const is
  SEALED_DESCRIPTOR_ROW.atom[result_name].source_and_span, so the row is the only
  lawful source of both key fields -- but the C-B-V009-06 row binds its span
  [18898,19830) to a PATH and carries exactly two 64-hex digests, the atom's own
  constant and the precedence decision, NEITHER of which is the cited source. The
  source's digest 13cf1e17… occurs ZERO times in the whole sealed V011 and is not
  among the 19 supplied payloads. The producer's invocation does carry it, and
  PRODUCER_SUPPLIED is forbidden -- and R9 could not verify it even if permitted,
  because it does not hold the source file to hash, so that path is trust rather than
  verification. Three readings, three consts, three bars. THE CURE HAS TWO PARTS:
  (1) the descriptor row must carry the source SHA-256 BOUND to the span it already
  carries, since the carrier const is source_and_span, one unit; and (2) the cited
  source must be a supplied payload, or R9 can derive no row's citation to match
  against. I supply neither -- one is a specification act, one an input act.)
ROWS_CHANGED_CONFIRMED = 0 (computed on both files, criterion column and procedure
  column separately, IDs set-equal, partition unchanged.)
RESOLVER_KEYED = citation; r_ground does NOT yet resolve on real inputs (blocker
  named, two parts); it resolves END-TO-END on a citation-bound row and both
  perturbation controls flip. The V011-O1 machinery is implemented in full: the
  nine-field amendment record built and closed BEFORE any byte is compared, the
  R9.P0.evidence_files_by_citation index DERIVED rather than read from a producer
  record -- for each supplied payload treated as a candidate source, R9 slices the
  descriptor's span and keys by (sha256(source_bytes), span), which uses no filename,
  no producer citation and no self-reference -- EXACT_TUPLE_EQUALITY matching,
  EXACTLY_ONE cardinality, and all three forbidden mappings as refusals. ON REAL
  INPUTS the path produces a NAMED REFUSAL stating the two-part gap and citing all
  three forbidden mappings. DRIVEN with a citation-bound row and the source supplied
  it RESOLVES: success True, evidence_sha256_rehashed 47e7c329… equal to
  constant_sha256 47e7c329…, resolved_by R9, producer_carrier false. BOTH
  PERTURBATION CONTROLS FLIP -- one source byte flipped at the span gives False, and
  the span shifted by one gives False -- so the comparison is over REHASHED SOURCE
  BYTES and can fail; it is not COMPARE(X,X), and condition 3 is honoured literally.
  Retained and re-verified from 700: r_dag is still not a ground atom, six
  closed-schema negatives still refuse, and a smuggled producer r_ground is still
  refused under BR-1 structurally, the ground-atom name set being computed from the
  sealed row before any invocation is consumed.)
VERIFIER_ROOT = 2cf5f313a44e12859d199184c863e92bc8662073a3695ffb2c0ea7f535900652
  (CHANGED from ddc09a3d…; MEMBERSHIP UNCHANGED at 14, so the root moved only because
  member bytes changed. Instance d4219a53f26aa19dad3b1119ee7f1cc7d4c9816b64b02b3f1c1e
  fbea7a884d8a and sidecar a59ce9239a30af12ca5383cfdc34d0cd1fcb9cd5ab9a5ebd8e1500aab
  ba54c13 were written in ONE ACT from final bytes -- the 700 lesson -- and when the
  stale-reference sweep forced a second edit round I regenerated BOTH again rather
  than patch one. Sidecar root == instance root == package_root_digest(), checked.
  Self-check CLEAN with 4 new permanent O1 assertions; 23 files; zero runtime
  asserts; dry run exit 2 from both cwds with 372 bytes ending 0x7d, rstrip() == raw,
  stderr 0; the 22-token argv parses end-to-end and emits the fault verdict at exit 2.)
PIN_CLOSURE = 16 hits, all resolved (swept BY VALUE AND BY NAME: the V010 spec digest
  31ccee9c and filename LANE2_V010 both zero, V009 / V008 / V007 all zero, every
  superseded root -- ddc09a3d, 10622f17 and the intra-relay 5d37db4c -- zero, and every
  superseded instance and sidecar -- 1217571e, 9682b652, c3f0b62d -- zero. The live
  V011 pin d48e0fa7 is present in exactly the four sites that should carry it: README,
  spec_census, the instance and the verdict-schema const. THREE STALE DOCSTRINGS were
  found, and ONE HAD BECOME A FALSE CLAIM: ground_atoms.py still asserted "Condition 2
  -- and this is where V010 stops determining… SPEC GAP" after V011 determined it,
  which would have told the next reader the opposite of the governing spec. Repaired
  with the historical reasoning kept and labelled as WHY V011-O1 exists, and
  resolve_member_key marked SUPERSEDED rather than deleted. RETAINED DELIBERATELY
  under the standing rule: the identifiers V008-R9-1/2/3, V009-J3, V009-J4 and
  V010-M1, each of which V011 itself retains, and the self-check comment recording
  WHEN the V005->V007 incident happened.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. The envelope check
  reads sealed bytes, the resolver paths call pure functions on mirrored inputs, and
  the launch demonstration is the dry run, which opens no run input. NO OUTCOME IS
  CLAIMED: the success=True case is a DRIVEN demonstration on a citation-bound row
  with the source supplied -- it proves the machinery and the non-vacuity and is NOT a
  resolution of the real atom, because neither of Q1's two parts is present today. I
  do NOT claim run 032 passes: on today's spec and inputs r_ground will record
  PRECONDITION_NOT_REPLAYABLE naming the two-part citation gap, which is a refusal
  rather than a criterion failure and the correct behaviour of a mapping whose key
  field has no lawful carrier.)
VERB_AUDIT_SELF = CLEAN (+1 DEFECT IN MY OWN RESOLVER, caught by running it, §2.2: my
  first descriptor_citation took "the one 64-hex in the row that is not the atom's
  constant" as the source identity and returned 70c4080e…, THE PRECEDENCE DECISION.
  The refusal's conclusion was right and its reason was wrong, and had that digest
  ever matched a supplied payload the atom would have resolved AGAINST THE WRONG
  BYTES. Repaired by requiring the digest to be SYNTACTICALLY BOUND to the span,
  because V011's carrier const is source_and_span, one unit, and a digest merely
  present in the row is not a citation. Third relay running in which running the code,
  not reading it, caught the defect. +NOTE: one self-check label my earlier sweep
  missed because the fail(...) call wrapped across lines -- found by the second sweep
  and moved. +NOTE: my pin check asserted §1.3's census sentence with a RAW substring
  search and it failed on LINE WRAPPING alone; whitespace-normalized the sentence is
  present in V011 and absent from V010, so the claim holds and the assertion was what
  was wrong. THIRD relay in which a raw search of mine tripped on wrapping, and the
  standing rule it argues for is to normalize whitespace before concluding that a
  sealed sentence was dropped or added.)
```

V011 closed the mapping properly: three forbidden carriers named as consts, an
exact-tuple key, a cardinality of one. The resolver is built to it and works — on
a row that carries what the schema asks for. The row in front of it cites its
source by path where the schema wants a digest, and the file behind that path was
never handed to the verifier. Two small additions and the atom resolves; without
them the honest output is a refusal that names both, and that is what run 032 will
carry.

The other thing worth keeping from this relay is smaller and mine: the rule I first
wrote would have accepted a precedence-decision digest as a source identity. It
refused for the right reason only by accident, and I found that out by running it.
