# STAGE 8 / TASK 6 / BUILD — V009 ENVELOPE CHECK AND INDEPENDENT CONFIRMATION — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 697 / Task 6 — envelope-check V009, then confirm and re-pin, as one delta
Authority: RD-22. **THIS ARTIFACT INVOKES NOTHING.**

```text
ENVELOPE = four dispositions only (+2 findings)
ROWS_CHANGED_CONFIRMED = 0
P0_ALL_SIX_REPLAYABLE = confirmed on real inputs
MANIFEST_INSTANCE = re-authored, sealed
VERIFIER_ROOT = 10622f170b979ae83ad8b496bafac41087b976512025669f5b38a97c028af488 (changed)
PIN_CLOSURE = 12 hits, all resolved
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 near-miss that would have been a false charge, §1.3)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**All three preflight digests generated, not transcribed.** V009 = `900a240d…`
(182,779 B); Q-612 disposition `STAGE8_TASK6_Q612_FIXES_CODEX2_V001.md` =
`493d0b40…`; package inventory = `37d7202b…`, **43 files** confirmed by count.

## 1. K1 — THE ENVELOPE

### 1.1 Four dispositions, and the carriage is mechanical

```text
66 descriptor rows           BYTE-IDENTICAL 66/66      rows changed = 0
criterion drift (col 5)      none
procedure drift (col 4)      none
class partition              56 STRUCTURAL / 10 GATED-EXECUTION, both versions
carriage arithmetic          9 hunks, 120 insertions, 23 deletions
                             2253 -> 2350 lines, net 97 = 120 - 23   SELF-CONSISTENT
                             and the certificate declares exactly 9/120/23
schemas, not prose           J3's resolution record and J4's membership row are
                             both closed JSON Schema; the manifest required-list
                             is 12 fields and the argv schema 22 ordered consts
```

### 1.2 [PROVABLE] J1 — the regenerated span table is row-exact

The three spans are now generated from source bytes *including each row's
terminating newline*, which is what my 695 F1 said the convention of record was.
Verified three ways:

```text
FX-A35-03-C-FAMILY                      [136130,136319)  len 189  row-exact  digest MATCH
FX-A35-04-TAU-FAMILY                    [136319,136507)  len 188  row-exact  digest MATCH
FX-A35-05-PRIMITIVE-THOMSON-CONFLATION  [136507,136760)  len 253  row-exact  digest MATCH

row-exact = the slice begins `| \`<FIXTURE_ID>\`` , ends ` |\n`, and contains
            exactly one newline
digest    = h(slice) equals the fixture_spec_sha256 run 030 declared
contiguous again, and the lengths are the ORIGINAL V007 lengths 189/188/253
```

The +1 correction is not merely applied; the slices are the rows.

### 1.3 [PROVABLE] J2 — the stated cause is a FACT, and I nearly charged it as a story

V009 corrects V008's `160/26` to `155/21` — matching my 695 computation — and
states the cause: *"produced by Python `difflib.SequenceMatcher`, whose alignment
emitted five additional canceling replacement pairs."*

My first probe **refuted it**: `SequenceMatcher(autojunk=False)` gives `155/21`,
the same as `/usr/bin/diff`. I had disabled the very heuristic that causes the
discrepancy. Under the default:

```text
SequenceMatcher  autojunk=True (DEFAULT)  ->  160/26   MATCH, all three line-splittings
SequenceMatcher  autojunk=False           ->  155/21
difflib.unified_diff  n=3                 ->  160/26   MATCH, all three line-splittings
difflib.ndiff                             ->  155/21
```

**The cause reproduces exactly.** Six variants hit `160/26`; the named tool, on
its documented defaults, produces the erroneous figures. This is my recurring
failure in a new costume — a probe run with the wrong option produced a false
negative — and it is the second consecutive relay in which my own check, not the
subject, was the thing at fault.

**FINDING G1 — the mechanism as described is wrong, though the cause is right.**
Decomposed:

```text
                 equal blocks / lines      replace blocks / lines(each side)
autojunk=True      13 / 2093                 10 / 26
autojunk=False     17 / 2098                 14 / 21
```

Replace *blocks* go **down** from 14 to 10 — four fewer, not five more. What rises
by five is the *line count* on each side: five lines leave the `equal` blocks and
are absorbed into fewer, larger `replace` blocks. So the true mechanism is **five
context lines reclassified as replaced on both sides, in four fewer replacement
blocks**, not "five additional canceling replacement pairs." The arithmetic effect
is right; the noun is wrong. Worth correcting because a correction of record that
misstates its own mechanism invites the same error again.

### 1.4 [PROVABLE] J3 — the binding is closed over ALL SIX subject rows

```text
evidence set now 17 payloads / 17 distinct digests; inventory 17

  OK  c09f2c24…    24108 B   BID_FULL_STACK_REVIEW_LEDGER_V003.md
  OK  900a240d…   182779 B   …EVALUATOR_SPEC_LANE2_V009.md
  OK  d17c5e79…    20423 B   …SPEC_V005_INTEGRATION_ADDENDUM_DARIO_V001.md   <- the 695 blocker
  OK  5c679e37…    10997 B   BID_SOURCE_PARENT_CLOSURE_GATE_V003.md
  OK  aa7c6d49…    78794 B   BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md
  OK  9d35f4ed…    13786 B   STAGE7_PACKET_MANIFEST_V001.sha256

each: in the evidence manifest inventory, EXACTLY ONE payload, length agrees
BINDING CLOSED OVER ALL SIX: True
```

No argv or `input_roots` slot was added — the addendum rides the existing evidence
carrier, as claimed. The V008-hash occurrences in the manifests are payload
members of a superseded-witness kind and are not live pins; the live spec pin is
`900a240d…`, which I re-derived.

### 1.5 [PROVABLE] J4 — the membership schema, and it is my scheme already

V009-J4: `verifier_root_sha256 = SHA256(concat(row.sha256 for row in members))`
in `relative_path` order. Applied literally to my 13 members it returns **exactly
what `package_root_digest()` already returned**:

```text
V009-J4 formula over my 13 rows   = 43cff85d…   (my 695-sealed root)
my package_root_digest()          = 43cff85d…
IDENTICAL SCHEME -- no change to the root computation was required
```

So J4 required only that the array become *instance data*. The schema is closed
(3 fields per row, sorted, unique, package-relative), and I now validate it and
**derive the root from it**, refusing a root that does not.

### 1.6 [PROVABLE] FINDING G2 — J4's own defect, reintroduced one level down

V009-J4's purpose is *"verifier-root membership is instance data, not a Builder A
constant… The parent consumes this sealed array and has no private membership
census."* Builder A also ships
`evaluator_build_A/inputs/verifier_root_members.generated.json`. That file:

```text
declares root 43cff85d…  == the root I sealed at relay 695, not the current one
same 13 relative_paths
7 of 13 digests STALE -- exactly the files this relay changed:
   contracts/verifier_verdict.schema.json, verifier/child_manifest.py,
   verifier/contracts.py, verifier/preconditions.py, verifier/replay.py,
   verifier/spec_census.py, verifier/verify.py
array key is `members`; the V009 schema field is `verifier_root_members`
```

A generated it correctly from my then-sealed bytes; it was true when written. But
**it is a snapshot of another builder's package, and it goes stale the moment my
bytes change — which is the exact failure mode J4 was written to remove, moved
from a parent constant into a parent input file.** The spec is on the right side
of this: the authoritative array is the one in *my sealed instance*. **If the
parent consumes A's copy for run 031 it will compare my root `10622f17…` against
a stale `43cff85d…` and mismatch.** Cure: the parent reads
`verifier_root_members` from the sealed instance and A's generated file is
deleted, or explicitly marked non-authoritative and regenerated from the instance
rather than from my directory. I do not choose.

## 2. K2 — CONFIRMATION AND RE-PIN

### 2.1 Inventories confirmed against sealed V009 text, not memory

```text
argv          22 sealed prefixItems consts vs my 22 tokens     ORDER-EXACT MATCH
input_roots   7 sealed required names vs my 7                  SET EQUAL
manifest      sealed required list = 12 fields; mine was 11
              sealed - mine = ['verifier_root_members']   mine - sealed = []
```

Extracted by parsing the sealed JSON out of the spec bytes. One imprecise regex of
mine dropped `verifier_root_sha256` (it contains digits and `[a-z_]+` cannot match
it); I re-extracted with a JSON parse rather than reason around a sloppy probe, and
the conclusion is unchanged.

### 2.2 [PROVABLE] P0 — all six conjuncts replayable on the REAL inputs

The 695 counterfactual is now the real path:

```text
P0.success = True
  strict_parse_BASE                                    True
  every_declared_sha256_matches_the_supplied_bytes     True
  content_root_subject_files_equals_declared_root      True
  content_root_evidence_files_equals_declared_root     True
  no_duplicate_path_or_key                             True
  every_required_input_present                         True

subject_resolutions: 6 of 6, every record a closed 5-field J3 record, every
  evidence_payload_sha256 == subject_sha256
the 695 blocker: the addendum resolves to exactly ONE evidence payload
```

Both negatives bite, so the confirmation is not a check that cannot fail:

```text
inject a second payload with the addendum's digest  -> REFUSED, naming
     "resolves to 2 evidence payloads; V009-J3 requires exactly one"
remove the addendum again                            -> the 695 refusal RETURNS
```

`_index_evidence` now maps digest → **list** of payloads. A dict keyed by digest
would have collapsed two copies into one and hidden the ambiguity J3 exists to
catch — the "exactly one" rule needs a carrier that can count.

### 2.3 The re-authored instance

```text
VERIFIER_ROOT   43cff85d… -> 10622f170b979ae83ad8b496bafac41087b976512025669f5b38a
                             97c028af488                                (CHANGED)
INSTANCE        35b0ec66… -> 5bfe149f2395c406ce0d39b88e3d9b03aa2a3121a474da22ba5604
                             f0a35f6f79
MEMBERS SIDECAR inputs/verifier_root_members.generated.json = 64810ce3…, sealed
fields 12   argv 22   input_roots 7   verifier_root_members 13 rows
manifest_sha256() == the file == the sidecar
evidence root recomputed over 17 payloads == the evidence manifest's declared_root
```

**Membership was generated last, after every byte change**, because the array
digests the package that contains the code that generates it; generating it early
would seal a root the package no longer has. The generated sidecar lives under
`inputs/` and is deliberately **not** a root member — a file derived from the root
cannot be inside it.

## 3. K3 — PIN CLOSURE

```text
by VALUE                                    by NAME
  3b24fc39 (V008 spec)      0 files           LANE2_V008   0 files
  d38d3171 (V007 spec)      0 files           LANE2_V007   0 files
superseded roots
  fd59672a (693)  0      43cff85d (695)  0
  585fb6d2 (intra-relay)  0      957a0e60 (intra-relay)  0
stale instances
  35b0ec66 (695)  0
instance fields == the sealed V009 required set, no extra keys anywhere

TOTAL 12 hits resolved: 4 governing pin sites (spec_census const, verdict-schema
const, README name+digest, self-check filename hint) + 4 governing prose
citations + 4 self-check label/fixture sites.
```

**Retained deliberately, with the rule that retains them:** the identifiers
`V008-R9-1/2/3` remain in my code because **V009 itself retains them** — I checked,
each occurs in the sealed V009 text — so they are statement *names* like `BR-1`,
not claims about which bytes govern. And the self-check comment recording *when*
the V005→V007 pin incident happened stays. *A reference that tells a reader which
bytes govern must move; a reference that names a law or records when a decision was
taken stays.* Before moving the four prose citations I confirmed each cited
passage carries forward byte-identically into V009.

## 4. DELTA — V009 required exactly this and no more

```text
CHANGED  verifier/contracts.py       VERIFIER_MANIFEST_FIELDS 11 -> 12;
                                     +ROOT_MEMBER_ROW_FIELDS, +validate_root_members,
                                     +root_from_members, +SUBJECT_RESOLUTION_FIELDS,
                                     +validate_subject_resolution; the manifest
                                     validator now derives the root from its members
CHANGED  verifier/child_manifest.py  +root_member_rows; build_manifest emits the array
CHANGED  verifier/preconditions.py   J3 resolution records; "exactly one payload" rule
CHANGED  verifier/verify.py          evidence index digest -> LIST of payloads
CHANGED  verifier/replay.py          governing-spec citations
CHANGED  verifier/spec_census.py     SPEC_SHA256 -> V009
CHANGED  contracts/verifier_verdict.schema.json (+sidecar)   spec const -> V009
CHANGED  selfcheck/selfcheck.py      +11 permanent assertions; V009 fixtures
CHANGED  README.md                   governing spec name and digest
NEW      inputs/verifier_root_members.generated.json (+sidecar)
CHANGED  rd22.verifier-manifest.v001.json (+sidecar)   re-authored
UNCHANGED  root MEMBERSHIP 13; run_verifier.py; hashing; canonical_json; comparison;
           runtime_state; the manifest contract schema
package 22 files
```

No opcode was added, no criterion touched, no P0 conjunct weakened.

## 5. PIN CHECK

| Claim | Verified before sealing |
|---|---|
| three preflight digests, 43 inventory files | generated and counted |
| 66/66 rows, 0 drift, partition held | computed on both files |
| carriage 9/120/23 self-consistent and as declared | computed |
| J1 spans row-exact | slice shape + digest against run-030 declarations |
| J2 cause is a fact | six difflib variants reproduce 160/26 |
| G1 mechanism | equal/replace block-and-line decomposition |
| J3 closed over all six | evidence dir indexed by observed digest |
| J4 formula == my scheme | applied literally to my 13 rows |
| argv / input_roots / 12 fields | parsed out of the sealed spec |
| P0 true on real inputs, 6/6 | executed |
| both J3 negatives bite | executed |
| J4 refuses unsorted/empty/dup/absolute/mismatched-root | executed, 5 cases |
| instance canonical, sidecar OK | `5bfe149f…` == `manifest_sha256()`; 12 fields |
| evidence root double-derived | mine == the manifest's declared_root |
| root recomputed, membership 13 | `10622f17…`; equals the instance field |
| members generated last | after every byte change; root stable across the final check |
| pin closure | 0 by value, 0 by name; retentions stated with their rule |
| self-check CLEAN, 22 files, 0 asserts | executed; my draft said 23 -- see §6 |
| dry run both cwds; stdout canon | exit 2; 372 B; `0x7d`; `rstrip() == raw`; stderr 0 |

### 5.1 `F_PLDEC` and coverage

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. **The chain was not invoked**: the envelope check reads
sealed bytes, the P0 confirmation calls pure functions on mirrored inputs, and the
launch demonstration is the dry run, which opens no run input. `alpha_computed =
false`; `proof_authorized = false`; `kappa_record_computed = false`; no member
bound; no fixed point; no end test; no numeric evaluation; no comparison to any
measured constant.

**Coverage, stated exactly.** I checked an envelope, confirmed a precondition, and
re-pinned. I claim **no check or fixture outcome**. `P0.success = true` is the
precondition, not a row verdict; the criterion still has to replay, and
`C-B-V009-06`'s `r_ground` invocation is still not recorded in the row (relay 693
§1, unchanged here). **I do not claim run 031 passes** — and G2 names a way it
could fail on my root for a reason that has nothing to do with my bytes.

## 6. SELF VERB AUDIT

| My verb | Check |
|---|---|
| Pins generated, never transcribed | Three preflight digests, seven input roots, thirteen member digests. |
| `ROWS_CHANGED_CONFIRMED = 0` | Computed, columns 4 and 5 separately. |
| J2 cause tested, not accepted | And my first test was wrong; §1.3 says so before it says the cause is a fact. |
| G1 is a correction, not a charge | The cause is right; only the described mechanism is wrong, and I decomposed it. |
| G2 named against the spec's own purpose | J4 removes a stale parent constant; A's generated file reintroduces staleness one level down, and I say which digests are already stale. |
| Confirmation with negatives | Duplicate payload and removed payload both refused; a confirmation that cannot fail confirms nothing. |
| J4 required no scheme change | Verified by applying the sealed formula to my own rows, not assumed from similarity. |
| Members generated last | The array digests the package that generates it; order matters and is stated. |
| Sidecar outside the root | A file derived from the root cannot be inside it. |
| Pin closure with a stated rule | Statement identifiers retained *because V009 retains them* — checked, not asserted. |
| No claim on run 031 | And the residual criterion gap from 693 is named as still open. |
| **Own file count corrected** | I drafted "23 files"; the package is 22 (20 at relay 695, plus the generated members file and its sidecar). Caught by my own pin check, which is what it is for. |

---

```text
ENVELOPE = four dispositions only (+2 findings) (J1 the regenerated span table, J2
  the recomputed carriage counts, J3 the subject-to-evidence binding, J4 the
  membership schema -- and nothing else: 66/66 descriptor rows BYTE-IDENTICAL, zero
  criterion drift, zero procedure drift, partition 56/10 held, carriage 9 hunks /
  120 insertions / 23 deletions computed and matching the certificate exactly with
  net 97 reproducing the line delta. J1 IS ROW-EXACT, not merely +1: each slice
  begins with its fixture ID, ends ` |\\n`, contains exactly one newline, and hashes
  to the fixture_spec_sha256 run 030 declared; the lengths are the original V007
  189/188/253 and the spans are contiguous again. J3 IS CLOSED OVER ALL SIX subject
  rows including the addendum d17c5e79…, each resolving to EXACTLY ONE evidence
  payload of the declared length, with no argv or input_roots slot added. J4's
  formula, applied literally to my thirteen rows, returns EXACTLY what my
  package_root_digest() already returned -- the schemes are identical, so J4 required
  only that membership become instance data. FINDING G1: J2's CAUSE IS A FACT BUT ITS
  MECHANISM IS MISDESCRIBED. Six difflib variants reproduce 160/26 -- SequenceMatcher
  on its DEFAULT autojunk=True across all three line-splittings, and unified_diff
  likewise -- so the named tool does produce the erroneous figures. But the claim of
  "five additional canceling replacement pairs" is wrong: replace BLOCKS go DOWN from
  14 to 10, while replace LINES rise by five on each side as five lines leave the
  equal blocks. Five context lines reclassified as replaced in FOUR FEWER blocks, not
  five extra pairs. FINDING G2: J4's OWN DEFECT REINTRODUCED ONE LEVEL DOWN. Builder
  A ships inputs/verifier_root_members.generated.json declaring root 43cff85d… --
  exactly the root I sealed at relay 695 -- with the same 13 paths but SEVEN STALE
  DIGESTS, precisely the files this relay changed, and under the key `members` where
  the V009 schema field is `verifier_root_members`. A generated it correctly from my
  then-sealed bytes; but it is a snapshot of another builder's package that goes
  stale the moment my bytes change, which is the failure mode J4 exists to remove,
  moved from a parent constant into a parent input file. The spec is on the right
  side: the authoritative array is the one in MY SEALED INSTANCE. If the parent
  consumes A's copy for run 031 it will compare my root 10622f17… against a stale
  43cff85d… and mismatch.)
ROWS_CHANGED_CONFIRMED = 0 (computed on both files, criterion column and procedure
  column separately, IDs set-equal, partition unchanged -- not read from the
  certificate that asserts it.)
P0_ALL_SIX_REPLAYABLE = confirmed on real inputs (P0.success = TRUE with all six
  §2.1 conjuncts satisfied against A's real subject manifest, evidence manifest and
  17-payload evidence directory: the relay-695 COUNTERFACTUAL IS NOW THE REAL PATH.
  Six of six subject rows produce closed five-field J3 resolution records with
  evidence_payload_sha256 == subject_sha256 throughout, and the 695 blocker -- the
  integration addendum -- resolves to exactly one payload. BOTH NEGATIVES BITE, so
  this is not a check that cannot fail: injecting a second payload with the
  addendum's digest is REFUSED naming "requires exactly one", and removing the
  addendum makes the 695 refusal RETURN. The evidence index now maps digest to a
  LIST of payloads, because a dict keyed by digest would collapse two copies into one
  and hide the very ambiguity J3 exists to catch -- the "exactly one" rule needs a
  carrier that can count. NOTE: this is the PRECONDITION, not a row verdict. The
  criterion still has to replay, and C-B-V009-06's r_ground invocation is still not
  recorded in the row -- relay 693 §1, unchanged here.)
MANIFEST_INSTANCE = re-authored, sealed (5bfe149f2395c406ce0d39b88e3d9b03aa2a3121a47
  4da22ba5604f0a35f6f79 == manifest_sha256(), sidecar verified OK; 12 fields, argv 22
  order-exact against the sealed prefixItems, input_roots 7 set-equal to the sealed
  required list, verifier_root_members 13 rows. Inventories CONFIRMED BY PARSING THE
  SEALED V009 BYTES, not from memory -- and one imprecise regex of mine silently
  dropped verifier_root_sha256 because [a-z_]+ cannot match digits, so I re-extracted
  with a JSON parse rather than reason around a sloppy probe. MEMBERSHIP WAS GENERATED
  LAST, after every byte change, because the array digests the package containing the
  code that generates it; generating it early would seal a root the package no longer
  has. The generated sidecar inputs/verifier_root_members.generated.json = 64810ce3…
  is sealed and deliberately NOT a root member, since a file derived from the root
  cannot be inside it. Evidence root double-derived: my computation over 17 payloads
  equals the evidence manifest's own declared_root.)
VERIFIER_ROOT = 10622f170b979ae83ad8b496bafac41087b976512025669f5b38a97c028af488
  (CHANGED from 43cff85d…; membership UNCHANGED at 13 rows, so the root moved only
  because seven member files changed content. The J4 validators refuse unsorted
  members, an empty array, a duplicate relative_path, an absolute path, and a
  verifier_root_sha256 that does not derive from its own members -- five negative
  cases executed and now permanent.)
PIN_CLOSURE = 12 hits, all resolved (swept BY VALUE AND BY NAME: the V008 spec digest
  3b24fc39 and filename LANE2_V008 both zero, the V007 pair both zero, and every
  superseded root -- fd59672a, 43cff85d, and the two intra-relay roots 585fb6d2 and
  957a0e60 -- zero, as is the stale 695 instance 35b0ec66. Instance fields are exactly
  the sealed V009 required set with no extra keys. RETENTIONS STATED WITH THEIR RULE:
  the identifiers V008-R9-1/2/3 stay because V009 ITSELF RETAINS THEM -- checked in
  the sealed text, each occurring there -- so they are statement names like BR-1 and
  not claims about which bytes govern; and the self-check comment recording WHEN the
  V005->V007 incident happened stays. A reference that tells a reader which bytes
  govern must move; a reference that names a law or records when a decision was taken
  stays. Before moving the four prose citations I confirmed each cited passage carries
  forward byte-identically into V009.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. The envelope check
  reads sealed bytes, the P0 confirmation calls pure functions on mirrored inputs, and
  the launch demonstration is the dry run, which opens no run input. Self-check CLEAN
  with 11 new permanent assertions; 22 files; zero runtime asserts; dry run exit 2
  from both cwds under -I -S -B with 372 bytes ending 0x7d, rstrip() == raw, stderr 0.
  NO OUTCOME IS CLAIMED and I do NOT claim run 031 passes -- G2 names a way it could
  fail on my root for a reason that has nothing to do with my bytes.)
VERB_AUDIT_SELF = CLEAN (+1 NEAR-MISS THAT WOULD HAVE BEEN A FALSE CHARGE, §1.3: my
  first test of J2's stated cause used SequenceMatcher with autojunk=False and
  returned 155/21, refuting the claim -- I had disabled the very heuristic that causes
  the discrepancy. Under the documented default the cause reproduces exactly across
  six variants. Had I stopped at one probe I would have charged a true correction of
  record as a fabrication. Second consecutive relay in which my own check, not the
  subject, was the thing at fault, and the third distinct costume of the same failure:
  a probe run with the wrong option produces a false negative. +NOTE: a second
  imprecise regex of mine dropped a field name containing digits; re-extracted by JSON
  parse rather than reasoned around. +NOTE: my draft stated the package as 23 files;
  it is 22 -- twenty at relay 695 plus the generated members file and its sidecar. The
  pin check failed on it and the artifact is corrected before sealing, which is the
  one thing a pin check is for.)
```

Two clean corrections and two schema repairs, with sixty-six rows untouched — and
the interesting result is not in the spec at all. J4 was written to stop a parent
from keeping a private census of my package. The generated file that implements it
is a private census of my package, already seven digests out of date, and the only
reason it is harmless is that the spec makes my sealed instance the authority
instead.
