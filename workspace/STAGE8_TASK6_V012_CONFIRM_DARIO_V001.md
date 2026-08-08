# STAGE 8 / TASK 6 / BUILD — V012 CONFIRMATION: THE LAST GATE BEFORE RUN 032 — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 704 / Task 6 — confirm the V012 amendment, resolve `r_ground` on real inputs
Authority: RD-22. **THIS ARTIFACT INVOKES NOTHING.**

```text
AMENDMENT = linkage only, independently recomputed (+0 findings)
R_GROUND = resolves on real inputs (controls hold)
VERIFIER_ROOT = 2294dfe53a77a6069913822616bedffb4e16d062b1e968deeb727552f9f906db (changed)
PIN_CLOSURE = 11 hits, all resolved
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 pattern of mine that had to be widened, §2.1)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**Preflight, pins generated.** V012 = `382052c4…` (197,462 B); report
`STAGE8_TASK6_V012_ROW_CITATION_CODEX2_V001.md` = `135424d1…`; inventory =
`fbcd75f2…`, **45 files**; evidence census **21 payloads**, and the grounding
source `13cf1e17…` **is supplied**. `parent.py` and `producer.py` are
byte-unchanged against the bytes that actually ran at run 031.

## 1. R1 — THE AMENDMENT, INDEPENDENTLY RECOMPUTED

### 1.1 The delta, derived from bytes rather than read from a display

```text
66 descriptor rows        IDs equal; 65 of 66 BYTE-IDENTICAL
ROWS CHANGED              exactly one: C-B-V009-06
class partition           56 STRUCTURAL / 10 GATED-EXECUTION, both versions
spec carriage             6 hunks, 89 insertions, 21 deletions
                          2534 -> 2602 lines, net 68 = 89 - 21   SELF-CONSISTENT
```

Column by column on the one changed row — my own split, not A's summary:

```text
col1  check_id            IDENTICAL
col2  class               IDENTICAL
col3  inputs (linkage)    CHANGED   <- the only column that moved
col4  procedure           IDENTICAL
col5  PASS iff            IDENTICAL

columns differing = [3]   exactly
```

The inserted text, in full:

```text
with `source_sha256=13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd`
```

nothing else. The row digests move as they must:

```text
old (no trailing NL)  b63a1335f20f71a3cd02f2192b4d696576344fd6ae28464ba543e6efba4643c0
new (no trailing NL)  da486b9a044bd8c1354f809ba5212a9da78a66dd0fcddaee18a19ed740707560
```

### 1.2 [PROVABLE] THE ANTI-TUNING QUESTION, ANSWERED OF RECORD

The question is whether a linkage amendment could have moved the row toward a
pass. It could not, and the reason is stronger than column identity.

**The PASS condition was fixed five versions before this linkage existed, and it
has never moved:**

```text
version   STAGE_DEPENDENCIES_MEMBER_SHA256   span
V007      47e7c32915bc756f…                  [18898,19830)
V008      47e7c32915bc756f…                  [18898,19830)
V009      47e7c32915bc756f…                  [18898,19830)
V010      47e7c32915bc756f…                  [18898,19830)
V011      47e7c32915bc756f…                  [18898,19830)
V012      47e7c32915bc756f…                  [18898,19830)
CONSTANT BYTE-IDENTICAL ACROSS ALL SIX : True
SPAN     BYTE-IDENTICAL ACROSS ALL SIX : True
```

**And the added digest is the true one, computed by me:**

```text
the row now says   source_sha256 = 13cf1e178a9fdced8859…
I hash the file    sha256(…preregistration_v011.json) = 13cf1e178a9fdced8859…   MATCH
```

**The closing argument.** Slicing the real source at the sealed span and
rehashing gives `47e7c329…` — exactly the constant sealed at V007. So the
amendment names *where the bytes already were*; it does not choose which bytes
satisfy the test. **Tuning would have required moving the constant, and the
constant is byte-identical in all six versions.**

Verdict on R1: **linkage completion only.** Criterion, procedure, class and
partition untouched; no drift; **no findings.**

## 2. R2 — `r_ground` RESOLVES ON REAL INPUTS

### 2.1 [YOURS] My own pattern had to be widened — and why that is not a loosening

V012 writes the citation as `` …with `source_sha256=<hex>` bytes `[start,end)` ``.
My 702 resolver accepted only the colon form `<hex>:[start,end)`, so it **refused
the V012 row on first contact**. That refusal was mine, not A's.

I widened it, and the widening is deliberately narrow. Relay 702 taught the
hazard: a rule that took *"the one digest that is not the atom's constant"*
adopted the **precedence decision** as the source identity. So the second form
binds by two independent constraints, not by proximity:

```text
1. the digest must be introduced by the literal key `source_sha256=`
2. it must lie in the SAME `;`-separated citation clause as the span
```

The precedence digest sits in a later clause, so it is excluded **structurally**
rather than by my judgement about which digest looks like a source. Tested three
ways:

```text
V012 row                                   BINDS   -> 13cf1e17…, [18898,19830)
V011 row (no source_sha256 at all)         REFUSED -> the 702-era named refusal
V012 row with the source_sha256 removed    REFUSED -> and the precedence digest
                                                      70c4080e… is NOT adopted
```

### 2.2 [PROVABLE] End to end on the real inputs

```text
P0.success = True    21 payloads    6 of 6 subject resolutions

r_ground = {
  atom_class: P0_EVIDENCE_SHA256_EQ_SEALED_SPEC_SHA256,
  success: true, equal: true,
  evidence_sha256_rehashed: 47e7c32915bc756f…,
  constant_sha256:          47e7c32915bc756f…,
  resolved_by: "R9", producer_carrier: false
}
```

The evidence operand was obtained by **rehashing the P0-verified source at the
sealed span** — condition 3 honoured literally — and compared against the
constant the row has carried since V007. `producer_carrier` is false: no producer
record touched this atom.

**The perturbation controls still flip**, so the resolution is not a check that
cannot fail:

```text
one source byte flipped at the span   success=False   rehashed 1a19764f2715…
the span shifted by one               success=False   rehashed ac628ab64c86…
```

### 2.3 [PROVABLE] The full criterion replays

```text
atom P0                 -> True     (six §2.1 conjuncts, all satisfied)
atom r_ground.success   -> True     (R9-resolved, above)
atom r_dag.success      -> True     (11 nodes, acyclic, single root/sink)

replay_predicate("P0 and r_ground.success and r_dag.success") -> True
```

This is the first time the criterion has reduced to a value rather than to a
refusal. **It is my replay, not a run verdict** — see §4.1.

### 2.4 The contract change V012 required

Exactly one: the governing row hash. My census **derives** `check_spec_sha256`
from the row bytes rather than pinning it, so the change propagates without a
literal edit:

```text
grep for the OLD row hash b63a1335 in my package : 0 hits
my census, from V012 bytes: C-B-V009-06 -> da486b9a044bd8c1354f809ba5212a9da78a66dd0…
                            == my §1.1 derivation
census/partition/board still reproduce           : 66 / 56-10 / board
```

## 3. R3 — DELTA, RE-PIN, PIN CLOSURE

```text
CHANGED  verifier/ground_atoms.py   descriptor_citation accepts the V012
                                    named, clause-scoped citation form
CHANGED  verifier/spec_census.py    SPEC_SHA256 -> V012
CHANGED  verifier/replay.py, verify.py, contracts.py   governing citations
CHANGED  contracts/verifier_verdict.schema.json (+sidecar)  spec const -> V012
CHANGED  selfcheck/selfcheck.py     +3 permanent V012-citation assertions
CHANGED  README.md                  governing spec name and digest
CHANGED  rd22.verifier-manifest.v001.json (+sidecar)
CHANGED  inputs/verifier_root_members.generated.json (+sidecar)

verifier_root_sha256  2cf5f313…  ->  2294dfe53a77a6069913822616bedffb4e16d062b1e968
                                     deeb727552f9f906db      (CHANGED)
root MEMBERSHIP unchanged at 14 -- the root moved only because member bytes changed
instance  d4219a53… -> b43912455db38ebdebe603547d8a733b294b7a16b9f5999f1180da16a7d11961
sidecar   a59ce923… -> 3e3780d591341d8e1cfe170d32448e30922496e106044c895850bb57cab0b656
package 23 files
```

Instance and sidecar were written **in one act, from final bytes, after every
edit** — my own 700 lesson. Sidecar root == instance root ==
`package_root_digest()`, checked.

### 3.1 Pin closure — value AND name

```text
0 files: b63a1335 (the OLD ROW HASH) — and it was never pinned, because my census
         derives row digests rather than transcribing them
0 files: d48e0fa7 (V011 spec) / LANE2_V011 / 31ccee9c / LANE2_V010 / 900a240d
0 files: every superseded root — 2cf5f313, ddc09a3d, 10622f17
0 files: every superseded instance and sidecar — d4219a53, a59ce923
live V012 pin 382052c4 in exactly the four sites that should carry it:
         README, spec_census, the instance, the verdict-schema const
11 hits resolved: 4 governing pin sites + 4 governing prose citations +
                  3 self-check labels
```

**Retained deliberately**, under the standing rule — *a reference that tells a
reader which bytes govern must move; a reference that names a law, a blocker, or
records when a decision was taken stays*: `B-V011-SP2-07` is a **blocker ID**,
not a spec version, and appears in three files that must keep it; the identifiers
`V008-R9-1`, `V009-J3`, `V009-J4`, `V010-M1` and `V011-O1`, each of which **V012
itself retains** (checked, all five present in the sealed text); and
`ground_atoms.py`'s "pre-V011 exact-key path", which records *when* that path was
superseded.

### 3.2 Every touched path run, not read

```text
V012 citation binds / V011 row still refused / later-clause digest not adopted   3
r_ground resolves on real inputs; both perturbations flip                        3
full criterion replays to True                                                   1
P0 six conjuncts, six subject resolutions                                        1
22-token argv end-to-end                    exit 2, fault verdict emitted
dry run, both cwds                          exit 2; 372 B; 0x7d; rstrip==raw; stderr 0
self-check                                  CLEAN, 23 files, 0 runtime asserts
```

## 4. PIN CHECK

| Claim | Verified before sealing |
|---|---|
| three preflight digests, 45 inventory files, 21 payloads | generated and counted |
| the source is supplied | searched the evidence set by digest |
| parent/producer byte-unchanged | against run 031's runner and module ledger |
| 65/66 rows identical; only V009-06 moved | computed on both files |
| only column 3 changed | five-column split, compared cell by cell |
| the constant and span never moved | all six versions V007–V012 |
| the added digest is the true one | I hashed the source myself |
| the slice rehashes to the V007 constant | computed |
| r_ground resolves on real inputs | executed; `producer_carrier` false |
| both perturbations flip | executed |
| the full criterion replays True | executed, atom by atom |
| the new row hash derives | `da486b9a…` from V012 bytes, equal to §1.1 |
| root recomputed, membership 14 | `2294dfe5…`; equals instance and sidecar |
| instance + sidecar in one act | all three roots agree |
| pin closure | 0 by value, 0 by name; retentions stated with their rule |
| dry run both cwds; 22-token argv | executed |

### 4.1 `F_PLDEC` and coverage

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. **The chain was not invoked**: the confirmation reads
sealed bytes and mirrored inputs and calls pure functions on them; the launch
demonstration is the dry run, which opens no run input. `alpha_computed = false`;
`proof_authorized = false`; `kappa_record_computed = false`; no member bound; no
fixed point; no end test; no numeric evaluation; no comparison to any measured
constant.

**Coverage, stated exactly.** §2.3's `replay_predicate -> True` is **my
independent replay of one row's criterion**, not a row verdict and not a run
result. Builder B does not run the chain. What run 032 tests is whether the
producer's own execution agrees with this replay, and whether the other 65 rows,
the fixtures, the children, the trust records and the comparison all hold — none
of which is in evidence here. **I do not claim run 032 passes.** What I claim is
narrower and checked: the amendment is linkage only, and on the inputs as they
stand this atom now resolves rather than refuses.

## 5. SELF VERB AUDIT

| My verb | Check |
|---|---|
| Pins generated, never transcribed | Preflight digests, input roots, member digests, and the source digest I hashed myself. |
| Delta derived, not read | Five-column split computed from both files; A's display was not consulted for the answer. |
| **Anti-tuning answered structurally** | Not "the criterion column matches" but "the constant has been fixed since V007 and tuning would have required moving it". |
| **My own pattern was the blocker** | The V012 row refused on first contact because *my* 702 regex was too narrow; disclosed as mine before the widening is described. |
| The widening is narrow | Bound by an explicit key **and** clause scoping, with the 702 trap re-tested and still refused. |
| Controls before conclusions | Both perturbations flip; a resolution that could not fail would prove nothing. |
| Row hash derived, not pinned | `b63a1335` never appeared in my package; the new digest falls out of the census. |
| Derived artifacts in one act | Instance and sidecar regenerated together from final bytes. |
| Blocker ID not mistaken for a version | `B-V011-SP2-07` retained; a sweep that renamed it would have corrupted a citation. |
| No claim on run 032 | The replay is mine; the run is the registrar's, and it tests far more than this row. |

---

```text
AMENDMENT = linkage only, independently recomputed (+0 findings) (65 of 66
  descriptor rows BYTE-IDENTICAL with only C-B-V009-06 moving, partition 56/10 held,
  spec carriage 6 hunks / 89 insertions / 21 deletions with net 68 reproducing the
  line delta. COLUMN BY COLUMN on the changed row, from my own five-way split rather
  than any display: check_id IDENTICAL, class IDENTICAL, PROCEDURE IDENTICAL, PASS-IFF
  IDENTICAL, and only the inputs/linkage column moved -- the differing-column set is
  exactly [3]. The inserted text is nothing but `with source_sha256=13cf1e17…`. Row
  digest b63a1335… -> da486b9a…. THE ANTI-TUNING QUESTION IS ANSWERED STRUCTURALLY,
  NOT BY COLUMN IDENTITY: the PASS condition was fixed FIVE VERSIONS BEFORE this
  linkage existed and has never moved -- STAGE_DEPENDENCIES_MEMBER_SHA256 =
  47e7c329… and the span [18898,19830) are BYTE-IDENTICAL in V007, V008, V009, V010,
  V011 and V012. The added source digest is the TRUE one, which I computed by hashing
  the file myself, and slicing that source at the sealed span rehashes to exactly the
  V007 constant. So the amendment NAMES WHERE THE BYTES ALREADY WERE; it does not
  choose which bytes satisfy the test, and tuning would have required moving the
  constant. No drift, no findings.)
R_GROUND = resolves on real inputs (controls hold) (P0.success True over 21 payloads
  with six of six subject resolutions; r_ground resolves to success True with
  evidence_sha256_rehashed 47e7c329… equal to constant_sha256 47e7c329…, resolved_by
  R9 and PRODUCER_CARRIER FALSE -- the operand obtained by REHASHING the P0-verified
  source at the sealed span, condition 3 honoured literally, with no producer record
  touching the atom. BOTH PERTURBATION CONTROLS STILL FLIP: one source byte altered at
  the span gives False, and the span shifted by one gives False, so this is not a check
  that cannot fail. THE FULL CRITERION REPLAYS: P0 True, r_ground.success True,
  r_dag.success True, and replay_predicate("P0 and r_ground.success and r_dag.success")
  returns True -- the first time the criterion has reduced to a value rather than a
  refusal. MY OWN PATTERN WAS THE BLOCKER FIRST: V012 writes the citation as
  `source_sha256=<hex>` … `[start,end)` while my 702 resolver accepted only the colon
  form, so it refused the V012 row on first contact. The widening is deliberately
  narrow -- the digest must be introduced by the LITERAL KEY source_sha256= AND lie in
  the SAME `;`-separated clause as the span -- because relay 702 taught that a looser
  rule adopts the PRECEDENCE DECISION as the source identity. Re-tested: the V012 row
  binds, the V011 row still refuses, and with the source_sha256 removed the
  later-clause precedence digest is still NOT adopted. The only contract change V012
  required is the governing row hash, and my census DERIVES row digests rather than
  pinning them, so b63a1335… never appeared in my package and da486b9a… falls out of
  the V012 bytes, matching my independent derivation.)
VERIFIER_ROOT = 2294dfe53a77a6069913822616bedffb4e16d062b1e968deeb727552f9f906db
  (CHANGED from 2cf5f313…; MEMBERSHIP UNCHANGED at 14, so the root moved only because
  member bytes changed. Instance d4219a53… -> b43912455db38ebdebe603547d8a733b294b7a1
  6b9f5999f1180da16a7d11961 and sidecar a59ce923… -> 3e3780d591341d8e1cfe170d32448e30
  922496e106044c895850bb57cab0b656 were written in ONE ACT from final bytes -- the 700
  lesson -- with sidecar root == instance root == package_root_digest() checked.
  Self-check CLEAN with 3 new permanent V012-citation assertions; 23 files; zero
  runtime asserts; dry run exit 2 from both cwds with 372 bytes ending 0x7d,
  rstrip() == raw, stderr 0; the 22-token argv parses end-to-end at exit 2.)
PIN_CLOSURE = 11 hits, all resolved (swept BY VALUE AND BY NAME: the OLD ROW HASH
  b63a1335 returns ZERO files -- and it was never pinned in the first place, because
  my census derives row digests rather than transcribing them; the V011 spec digest
  d48e0fa7 and filename LANE2_V011 both zero, V010 and V009 zero; every superseded
  root -- 2cf5f313, ddc09a3d, 10622f17 -- zero; every superseded instance and sidecar
  -- d4219a53, a59ce923 -- zero. The live V012 pin 382052c4 sits in exactly the four
  sites that should carry it. RETAINED DELIBERATELY: B-V011-SP2-07 is a BLOCKER ID,
  not a spec version, and a sweep that renamed it would have corrupted a citation; the
  identifiers V008-R9-1, V009-J3, V009-J4, V010-M1 and V011-O1, each of which V012
  itself retains, checked in the sealed text; and ground_atoms.py's "pre-V011
  exact-key path", which records WHEN that path was superseded.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. The confirmation
  reads sealed bytes and mirrored inputs and calls pure functions on them; the launch
  demonstration is the dry run, which opens no run input. NO OUTCOME IS CLAIMED: the
  replay_predicate -> True is MY INDEPENDENT REPLAY OF ONE ROW'S CRITERION, not a row
  verdict and not a run result. What run 032 tests is whether the producer's own
  execution agrees with this replay, and whether the other 65 rows, the fixtures, the
  children, the trust records and the normal/optimized comparison all hold -- none of
  which is in evidence here. I do NOT claim run 032 passes. What I claim is narrower
  and checked: the amendment is linkage only, and on the inputs as they stand this
  atom now resolves rather than refuses.)
VERB_AUDIT_SELF = CLEAN (+1 PATTERN OF MINE THAT HAD TO BE WIDENED, §2.1: the V012 row
  refused on first contact because MY 702 regex accepted only the colon-bound citation
  form, so the blocker at the start of this relay was mine and not Builder A's. I say
  that before describing the fix. The widening is bound by an EXPLICIT KEY and by
  CLAUSE SCOPING rather than by proximity, precisely because 702's looser rule adopted
  the precedence-decision digest as a source identity, and that trap is re-tested here
  and still refused. +NOTE: the anti-tuning answer is given structurally -- the
  constant fixed since V007 and never moved -- rather than as "the criterion column
  matches", because column identity alone would not rule out a constant that had been
  adjusted in an earlier relay.)
```

The amendment does one thing: it tells the verifier where the bytes it was already
required to compare actually live. Everything that decides the outcome — the
constant, the span, the criterion — has been fixed since V007 and is byte-identical
today, which is why this is a linkage completion and not a tuning.

The atom resolves now. It resolves because the source was supplied and the row was
completed, and it still fails when a single byte of that source moves. What run 032
tests is whether the producer's own execution agrees with the replay — and that is
the registrar's to invoke, not mine to predict.
