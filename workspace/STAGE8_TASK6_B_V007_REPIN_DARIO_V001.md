# STAGE 8 / TASK 6 / BUILD — BUILDER B'S V007 RE-PIN — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 688 / Task 6 build — the governing spec moves to V007
Authority: RD-22. **THIS ARTIFACT INVOKES NOTHING.**

```text
SPEC_PIN = V007 (d38d3171…, independently computed)
PARSE = census/partition/board reproduce (+V009-06 row reducible, 3 opcode atoms)
DELTA = disclosed (4 pin sites, not 1; +evidence root rebound, not commissioned)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 pin found only by its NAME, §2.2; +1 prediction of mine
                         refuted, §4.2; +1 observation on corpus residue, §4.1)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**The re-pin was not one line.** The commission named the const and the instance
root; the package carried the governing spec in **four** places, and the fourth was
invisible to a digest grep because it was carried by *filename*.

## 1. V007, VERIFIED BEFORE USE

```text
computed  d38d31719b64839744a98da5ee005fb50119f9a26b2b98b0e1a1de445b5d4973
stated    d38d31719b64839744a98da5ee005fb50119f9a26b2b98b0e1a1de445b5d4973   MATCH
171,532 bytes ; 2,119 lines
```

Hashed from the file's own bytes before anything was pinned to it, per the 657
discipline. The value in the commission is a cross-check, not my source.

### 1.1 What V007 changed — checked, because it bears on whether the pin is safe

V007 is where my four 683 findings land, and each is verified here rather than
taken on the changelog's word:

```text
the global fence "No opcode invokes an approximate optimizer…"
  nearest preceding heading in V006:  #### V006 sealed-corpus law for M2(q,S)   ONE opcode
  nearest preceding heading in V007:  ### 2.2 Deterministic procedure opcodes   ALL FOURTEEN
                                                                              -> RESTORED

the M2(q,S) OPCODE ROW itself now carries the precondition (byte-changed from V005/V006),
  and SEALED_CORPUS_DEFINITION is a CLOSED SCHEMA -- exact fields, sorted unique members,
  declared_root = content_root(members), named by path+SHA-256 in the P0-verified manifest

§2.3 gains "Precedence is total. P0 integrity is evaluated first… The classification
  does not replace, mask, or outrank a P0 failure."  The registry column header is now
  "V007 classification", not "V006 status".

§12.4 is retitled "three guards and all FIVE false-negative modes" (was four).

DAG(G,P) gains the single-authority form, and C-B-V009-06 becomes a real program
  contract (§3).
```

The diff is 13 hunks, +122/−34, `2031 → 2119` lines; `88 = 122 − 34` reproduces the
line delta, so the counts are blank-line-safe — the defect I charged in the
V005→V006 certificate is not repeated here.

## 2. THE DELTA — four pin sites, one cause

```text
CHANGED  verifier/spec_census.py            SPEC_SHA256 const + governing-spec docstring
CHANGED  contracts/verifier_verdict.schema.json   the `spec_sha256` CONST
CHANGED  contracts/verifier_verdict.schema.json.seal.sha256
                                            300a475e… -> 5acf066a01eec3762de6364766424be57ce6a1a19a4a34f0e15edc081b0cc1a2
CHANGED  selfcheck/selfcheck.py             the spec FILENAME lookup hint
CHANGED  README.md                          2 filenames + 1 digest
                                            cbbe6583… -> df5f03b6ea221facc710d6aa1c397b010f2d7f69a6b4f593bf7d5984fb433a16
CHANGED  rd22.verifier-manifest.v001.json   spec root, evidence root, verifier root
                                            4c6e4783… -> 2b1d195bb894b3c07e2aa42dd4407ba3855d0e1877bd8660f0f9181dc5ee1403
CHANGED  rd22.verifier-manifest.v001.json.seal.sha256   regenerated, verified OK

verifier_root_sha256  0f67e57a…  ->  02da5c8efdcc075d6a7e602449c8918c5d8d544cd3310ef8
                                     3f49383eca3254c4
UNCHANGED  root MEMBERSHIP (12); run_verifier.py; every verifier/*.py except spec_census;
           the manifest contract schema; the three input roots that did not move
```

`selfcheck.py` and `README.md` are **not** root members, so they cannot move the
root; I verified the root after editing them and it did not. The root moved for
exactly one reason: two root members changed content.

### 2.1 [PROVABLE] The third site would have failed my verdict against my own contract

A grep for the old digest found three pins, not the two commissioned. The third is
`contracts/verifier_verdict.schema.json`, where `spec_sha256` is a **`const`**:

```text
"spec_sha256": { "const": "f8d1a7dc…" }        <- the governing spec, enforced
```

Had I re-pinned the census const and the instance and left this, **every verdict I
emit would have been refused by my own schema** — a self-inflicted fault on every
run. That const is not decoration: at 674 it refused my own fake test sample before
it refused anything real, which is exactly why it bites here.

### 2.2 [PROVABLE] The fourth site was carried by NAME, and only the self-check found it

After the first three edits the self-check **refused**:

```text
FAIL  spec census: governing spec: content-address mismatch for
      …/STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md
      (expected d38d3171…, observed f8d1a7dc…)
```

`selfcheck.py` located the spec by a hard-coded **filename**. A grep for
`f8d1a7dc` cannot see that, because the pin was carried by name rather than by
value. Two things worth keeping:

1. **The refusal was correct behaviour, not a defect.** `SpecCensus` loads through
   `load_addressed`, so the filename is only a lookup hint and the digest is what
   admits the bytes. Handed the wrong file, it failed closed on a content-address
   mismatch instead of silently parsing V005 while claiming V007.
2. **The rule this argues for:** *a pin can be carried by its name as well as by
   its value; a re-pin must grep the name too.* Doing that then found three more
   references in `README.md` — stale documentation of the very fact being changed,
   so repaired under the same cause rather than deferred.

```text
residual `f8d1a7dc` or `LANE2_V005` anywhere in the package:  NONE
```

## 3. PARSE — the expectations derive from V007

### 3.1 Census, partition, board — reproduced, with the source of truth unedited

`verifier/spec_census.py`'s expectation constants are **byte-unchanged**. Only the
digest that admits the file moved. So this is a re-derivation, not a restatement:

```text
                       EXPECTED (shipped)     DERIVED FROM V007 BYTES
total_ids              66                     66            OK
blocker / discrepancy  63 / 3                 63 / 3        OK
class_partition        56 STRUCTURAL /        56 / 10       OK
                       10 GATED-EXECUTION
binding_board          BOUND 35, RE-RENDERED  identical      OK
                       13, V004-REPAIRED 8,
                       V005-REPAIRED 10
all 66 descriptor digests derived, all unique                OK
```

V007's R9 duty passage is **byte-identical** to V005's, which is why the
expectations still hold; I checked that rather than assuming it. The board's
`V004-REPAIRED`/`V005-REPAIRED` labels are historical tags naming *when* a row was
repaired — not a claim about which spec governs — and the docstring now says so.

### 3.2 Two-builder agreement on the descriptor pin

```text
C-B-V009-06 descriptor digest, derived by ME from V007 bytes : b63a1335f20f71a3…
C-B-V009-06 descriptor digest, in Builder A's manifest       : b63a1335f20f71a3…
AGREE
```

Independently computed on both sides, under the convention I had to reconstruct at
683 §4.2 — the row bytes **without** the trailing newline. That convention is now
confirmed by agreement rather than by inference.

### 3.3 [PROVABLE] The V009-06 row is reducible — the exact thing 686 could not deliver

V007's row is a program contract, not prose:

```text
r_ground := COMPARE(P0.evidence_files[stage_dependencies_member].sha256,
                    STAGE_DEPENDENCIES_MEMBER_SHA256, empty)
r_dag    := DAG(stage_dependencies, PRINCIPAL_SINGLE_AUTHORITY)
PASS iff   P0 and r_ground.success and r_dag.success
```

```text
split_conjuncts -> ['P0', 'r_ground.success', 'r_dag.success']     3 atoms, all reducible
declared_opcodes -> [('r_ground','COMPARE'), ('r_dag','DAG')]

replay against a shape-only bundle, every atom tracked:
  P0 T, r_ground T, r_dag T  -> True
  P0 T, r_ground T, r_dag F  -> False
  P0 T, r_ground F, r_dag T  -> False
  P0 F, r_ground T, r_dag T  -> False

CONTROL: the V006 prose criterion, replayed under the same code, still raises
  "criterion atom not opcode-reducible: 'every required parent is literal, the
   graph is acyclic,'"
```

At 686 §4.1 I computed that exact fault as what the row would meet next and said it
was a specification matter, not a verifier defect, and not mine to repair. **It was
repaired at the specification, and the same verifier code now reduces the row with
no change to the replay.** The control matters: the reducibility is a property of
the new criterion, not of a loosened parser.

[PROVABLE] The single-authority form is BR-1-admissible on its face:
`PRINCIPAL_SINGLE_AUTHORITY` is a **spec-fixed constant**, forcer class (c), and
the row states the comparison clause is discharged by the principal ruling's
identity "never by synthesizing `COMPARE(X,X)` or duplicating the object as two
independently authored arguments." A's payload conforms — the dag-args object is
now 645 bytes carrying `{authority, graph}`, where the V006-era object was 1218
bytes carrying `{graph, required_parents}`, the duplication the row now forbids.

## 4. THE EVIDENCE ROOT — rebound, and NOT commissioned

[YOURS] A's coordinated re-pin also moved the evidence set: **12 → 14 payloads**.
The commission named `spec_sha256`. I bound the evidence root as well, and the
reasoning is here so it can be overruled:

```text
evidence root recomputed BY ME over the 14 files' bytes  fcaa97a01a9796a6313ce2f81f
                                                         7710d9848ca972ede5699b84c9
                                                         14e09a15d364
manifest declared_root (observed AFTER computing)         identical
CONTROL: same recipe over the prior 12                    1fbb3c07…  == what the
                                                          instance was attesting
new members: + 645 B  b5f15a9c…  the V007 dag-args object
             + 171,532 B d38d3171…  the V007 spec itself
```

Both roots moved from **one event** — A re-emitting the envelope for V007 — and a
re-pin that left the instance attesting a superseded census would stop run 026 at
`VERIFIER_INPUT_ROOT`, which is precisely where run 023 stopped and what relay 684
existed to repair. The two fields are independent, so the registrar can reject this
half without touching the spec half. Method and control are 684's, unchanged.

### 4.1 [YOURS] Observation — the superseded payload is still in the corpus

```text
digests referenced by ANY record's input_files:  2
    47e7c329…  the 932-byte relocated member
    b5f15a9c…  the 645-byte V007 dag-args
resident but referenced by nothing:
    344fecdc…  the 1218-byte {graph, required_parents} object -- the very shape
               V007's V009-06 row forbids
    f8d1a7dc…  spec V005, alongside d38d3171… spec V007
```

**Not a fault for run 026.** Unreferenced members are inert for every row that
runs, and P0 asks only that `content_root(evidence_files)` equal the declared root,
which it does. But it is a live hazard the moment any `SEALED_CORPUS_DEFINITION` is
drawn from this set: a corpus holding both a superseded object and two versions of
the same spec returns hits from the superseded one. That is my own 683 §2.7 finding
— corpus membership as an outcome-bearing surface — which V007 has now installed as
the fifth false-negative mode. I record it for A and the registrar; it is not mine
to prune, and pruning it would move the root I just bound.

### 4.2 [YOURS] A prediction of mine, tested and refuted

I predicted my 686 coverage guard would **false-fault** on the single-authority
form: `authority: "PRINCIPAL_SINGLE_AUTHORITY"` is a spec-fixed constant, not
evidence, and Guard B demands every argument be reproduced by a digest-verified
payload. Run against A's *actual* invocation and payload:

```text
faults = 0
```

The guard's second clause — an argument reproduced as a **named field** of a
consumable payload — covers it, because the 645-byte payload carries `authority`
itself. My synthetic counter-example supplied the graph object alone; **the
counter-example was mis-built, not the guard.** It is doubly unreachable in any
case: `_recorded_invocation()` still returns `None`, the check-row contract having
no invocation field (686 §2.3, still owed). Recorded because I raised it, and a
hazard I cannot reproduce is not a hazard.

## 5. PIN CHECK

| Claim | Verified before sealing |
|---|---|
| V007 hashed from its own bytes | `d38d3171…`, 171,532 B; stated value used only as cross-check |
| four pin sites, zero residual | grep by digest **and** by filename; `f8d1a7dc`/`LANE2_V005` absent from the package |
| verdict-schema const re-pinned | old digest absent; sidecar regenerated, `shasum -c` OK |
| census/partition/board reproduce | derived from V007 with expectation constants byte-unchanged |
| 66 descriptor digests, unique | computed |
| descriptor pin agrees with A | `b63a1335…` both sides, independently |
| V009-06 reducible | 3 atoms; replay tracks all four truth combinations |
| control: prose still not reducible | V006 criterion still raises |
| evidence root computed, controlled | `fcaa97a0…` over 14; `1fbb3c07…` over the prior 12 |
| instance canonical, matches contract | `2b1d195b…` == `manifest_sha256()`; single line; 11 fields |
| roots: two changed, three untouched | ledger sentinel, snapshot, gate all unchanged |
| root recomputed; membership 12 | `02da5c8e…`; equals the instance field; README/selfcheck not members |
| self-check CLEAN against V007 | executed; census line shows 66/63+3/56-10/board |
| dry run, both cwds; stdout canon | exit 2; 372 B; last byte `0x7d`; `rstrip() == raw`; stderr 0 |
| 19 files; zero runtime `assert` | executed |

One assertion failed on the first pass — *"zero residual V005 pins"* — and it was
**right**: `README.md` still carried three. Unlike 686's failed assertion, which
was reading a docstring as code, this one found real staleness. A pin check earns
its keep by failing occasionally for the correct reason.

### 5.1 `F_PLDEC` and coverage

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. **The chain was not invoked**: the census parses sealed
spec bytes, the replay demonstration runs against a shape-only bundle I constructed
to exercise the reduction, and the launch demonstration is the dry run, which opens
no run input. `alpha_computed = false`; `proof_authorized = false`;
`kappa_record_computed = false`; no member bound; no fixed point; no end test; no
numeric evaluation; no comparison to any measured constant.

**Coverage, stated exactly.** I moved four pins and rebound two input roots. I
claim **no check or fixture outcome**, and the reducibility result is about the
*criterion*, not about the row: it shows my replay can now reduce V009-06 to three
opcode success bits, and says nothing about whether those bits will be true. **I do
not claim run 026 passes.**

## 6. SELF VERB AUDIT

| My verb | Check |
|---|---|
| `independently computed` | V007 hashed from its bytes before any pin moved; the commission's value used as cross-check only. |
| **Four sites, not one** | Two commissioned, a third found by digest grep that would have failed my verdict against my own contract, a fourth found only because the self-check refused — carried by name, invisible to a digest grep. |
| The refusal read correctly | The self-check failing was the guard working, not a defect: filename is a hint, digest admits, mismatch fails closed. |
| Expectations not edited | The constants are byte-unchanged; only the digest that admits the file moved, so §3.1 is a re-derivation and not a restatement. |
| `reducible` with a control | The V006 prose criterion still fails under the same code — the property is the criterion's, not a loosened parser's. |
| Uncommissioned change disclosed | The evidence root is named as not commissioned, with the reason, the control, and the note that the registrar can reject it independently. |
| **Prediction refuted, not buried** | I raised a coverage-guard hazard; run against A's real invocation it does not occur, and my counter-example was the thing that was wrong. |
| Corpus residue recorded, not pruned | Pruning would move the root I just bound; it is A's and the registrar's call. |
| No claim on run 026 | The pins are right and the criterion reduces; whether the bits are true is what the run tests. |

---

```text
SPEC_PIN = V007 (d38d31719b64839744a98da5ee005fb50119f9a26b2b98b0e1a1de445b5d4973,
  INDEPENDENTLY COMPUTED from the file's own 171,532 bytes before anything was pinned
  to it, with the commission's value used only as a cross-check. THE RE-PIN WAS FOUR
  SITES, NOT ONE: the commissioned SPEC_SHA256 const and the instance's spec_sha256
  root; a THIRD found by grepping the old digest -- the `const` on spec_sha256 in my
  own verifier_verdict.schema.json, which would have made EVERY VERDICT I EMIT FAIL
  MY OWN CONTRACT on every run; and a FOURTH that a digest grep CANNOT SEE because it
  was carried BY FILENAME, found only when the self-check refused with a
  content-address mismatch on …LANE2_V005.md. That refusal was the guard working, not
  a defect: SpecCensus loads through load_addressed, so the filename is a lookup hint
  and the digest is what admits the bytes -- handed the wrong file it failed closed
  rather than parsing V005 while claiming V007. THE RULE: a pin can be carried by its
  NAME as well as by its VALUE, and a re-pin must grep the name too. Doing so found
  three more stale references in README.md, repaired under the same cause. Residual
  f8d1a7dc or LANE2_V005 anywhere in the package: NONE.)
PARSE = census/partition/board reproduce (+V009-06 row reducible) (the expectation
  constants in spec_census.py are BYTE-UNCHANGED -- only the digest that admits the
  file moved -- so this is a RE-DERIVATION, not a restatement: 66 ids = 63 blocker + 3
  discrepancy, partition 56 STRUCTURAL / 10 GATED-EXECUTION, board BOUND 35 /
  RE-RENDERED 13 / V004-REPAIRED 8 / V005-REPAIRED 10, all 66 descriptor digests
  derived and unique. V007's R9 duty passage is BYTE-IDENTICAL to V005's, checked
  rather than assumed, which is why the expectations still hold; the board's
  V004/V005-REPAIRED labels are HISTORICAL tags naming when a row was repaired, not a
  claim about which spec governs, and the docstring now says so. TWO-BUILDER
  AGREEMENT on the descriptor pin: C-B-V009-06 = b63a1335f20f71a3… derived by me from
  V007 bytes and identical in Builder A's manifest, confirming by agreement the
  trailing-newline convention I had to reconstruct at 683 §4.2. V009-06 IS NOW
  REDUCIBLE: `P0 and r_ground.success and r_dag.success` splits to THREE opcode atoms
  and the replay tracks every one of the four truth combinations, with declared
  opcodes COMPARE and DAG. CONTROL: the V006 prose criterion still raises "criterion
  atom not opcode-reducible" under the same code, so the reducibility is a property of
  the NEW CRITERION and not of a loosened parser. At 686 §4.1 I computed that fault as
  what the row would meet next and said it was a specification matter, not mine to
  repair; it was repaired at the specification and the replay reduces the row with NO
  CHANGE TO THE REPLAY.)
DELTA = disclosed (root MEMBERSHIP unchanged at 12 and verifier_root_sha256 0f67e57a…
  -> 02da5c8efdcc075d6a7e602449c8918c5d8d544cd3310ef83f49383eca3254c4, moved because
  two root members changed content; selfcheck.py and README.md are NOT root members
  and the root was recomputed after editing them to verify, not assume. Instance
  4c6e4783… -> 2b1d195bb894b3c07e2aa42dd4407ba3855d0e1877bd8660f0f9181dc5ee1403 ==
  manifest_sha256(), canonical single line, 11 fields, sidecar regenerated and OK;
  verdict schema 300a475e… -> 5acf066a…, its sidecar regenerated. THE EVIDENCE ROOT
  WAS ALSO REBOUND AND WAS NOT COMMISSIONED: A's re-pin moved the evidence set 12 ->
  14 payloads, and I recomputed 1fbb3c07… -> fcaa97a01a9796a6313ce2f81f7710d9848ca972
  ede5699b84c914e09a15d364 from the 14 files' OWN BYTES with the 684 control -- the
  same recipe over the prior 12 reproduces the value the instance was attesting.
  Reason: both roots moved from ONE EVENT, and a re-pin leaving a superseded census
  attested would stop run 026 at VERIFIER_INPUT_ROOT, exactly where run 023 stopped.
  The fields are independent, so the registrar can reject this half without touching
  the spec half. The three roots that did not move -- ledger sentinel, runtime
  snapshot, runtime gate -- are untouched.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. The census parses
  sealed spec bytes, the reducibility demonstration runs against a SHAPE-ONLY bundle I
  constructed to exercise the reduction, and the launch demonstration is the dry run,
  which opens no run input. No check and no fixture has been run and NO OUTCOME IS
  CLAIMED: the reducibility result is about the CRITERION, not the row -- it shows the
  replay can reduce V009-06 to three opcode success bits and says nothing about
  whether those bits will be true. I do NOT claim run 026 passes.)
VERB_AUDIT_SELF = CLEAN (+1 pin found ONLY BY ITS NAME, §2.2, with the rule it argues
  for stated. +1 PREDICTION OF MINE REFUTED, §4.2: I expected my 686 coverage guard to
  false-fault on `authority: "PRINCIPAL_SINGLE_AUTHORITY"`, a spec-fixed constant
  rather than evidence; run against A's ACTUAL invocation and payload it produces ZERO
  faults, because the guard's second clause covers an argument reproduced as a named
  FIELD of a consumable payload and the 645-byte object carries `authority` itself --
  MY COUNTER-EXAMPLE WAS MIS-BUILT, NOT THE GUARD, and it is doubly unreachable since
  _recorded_invocation() still returns None. A hazard I cannot reproduce is not a
  hazard. +1 OBSERVATION recorded and NOT acted on, §4.1: the superseded 1218-byte
  {graph, required_parents} object -- the shape V007's own V009-06 row forbids -- is
  still RESIDENT in the evidence corpus, referenced by nothing, as are BOTH spec V005
  and spec V007. Not a fault for run 026, since unreferenced members are inert and P0
  is satisfied, but a live hazard the moment any SEALED_CORPUS_DEFINITION is drawn
  from this set -- my own 683 §2.7 finding, now installed as V007's fifth
  false-negative mode. Pruning it would move the root I just bound, so it is A's and
  the registrar's call. +NOTE: one pin-check assertion failed on the first pass and was
  RIGHT -- README.md was genuinely stale -- unlike 686's failed assertion, which was
  reading a docstring as code.)
```

The commission said re-pin the const and the root. The work was finding the two
pins nobody had listed, one of which would have made my own contract refuse my own
verdict on every run, and the other of which no digest search could reach. What the
re-pin buys is that the row I have been reporting faults about for three relays is
now a program contract my replay reduces without my touching the replay.
