# STAGE 8 / TASK 6 / BUILD — BUILDER B CONFORMED TO THE SEALED CONTRACT — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 651 / Task 6 build — conform the verifier to the sealed integration addendum
Authority: RD-22 + the addendum sealed at Q-588. **THIS ARTIFACT ADOPTS NOTHING
AND INVOKES NOTHING.**
Custody: Builder A conformed at Q-589; this is Builder B's conformance.

```text
REGISTER_HEAD = Q-589
CONFORMED = contract + inventories
OWED_CHANGES = 2/2 made
DELTAS = 13 disclosed (+table at §2)
SELF_CHECK = passed (+transcript at §4)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 cosmetic duplicate line, disclosed)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**The two changes I owed are made, and both were changes against my own code.**
When I drafted the addendum I found my shipped verifier disagreed with the spec
twice, and I wrote the contract the spec supported rather than the one my build
already satisfied. Paying that debt is this relay.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-589 | verified |
| Sealed addendum = `d17c5e79986bea431dec0b572019096f9c059bcc43876fda9134abc96ce0f260` | **verified before reading** |
| My prior manifest = `f79b50ac951522c636193e7fdbc3e4c216b9373be58c3ada8523f8bd7505133b` | verified |
| Output name collision | none — clear to write |
| `evaluator_build_A/` | exists; **never listed, opened, or searched.** Builder A's Q-589 conformance was not read either |

---

## 1. THE TWO OWED CHANGES

### 1.1 Owed change 1 — ledger objects → digests

[PROVABLE] **Before.** `runtime_state.EVENT_LEDGERS` named six ledger *objects*
(`module_ledger`, …) and `reclassify_events` expected each to be an object
carrying `{declared_sha256, events}`. **Only three classes were reachable at all**,
because the sealed child row declared only three carriers.

[PROVABLE] **After.** `contracts.EVENT_LEDGER_FIELDS` names the six **digest**
carriers of addendum §1.3, and `reclassify_events(child_row, evidence_dir, where,
loader)` fetches each ledger *by the child row's own declared digest*, recomputes
the canonical digest of the event list, and compares. All six classes are now
reachable.

```text
EVENT_LEDGER_FIELDS = (module_ledger_sha256, native_ledger_sha256,
                       open_event_ledger_sha256, process_event_ledger_sha256,
                       network_event_ledger_sha256, mutation_event_ledger_sha256)
EMPTY_LEDGER_SHA256 = sha256(b"[]")
```

The empty-class rule is implemented as the addendum states it: a class with no
events carries the digest of the empty list and is reported
`{"event_count": 0, "note": "declared-empty"}` — **never `null`, never omitted**,
so "no events occurred" cannot be confused with "events were not recorded".

### 1.2 Owed change 2 — fixture expectation as a named record

[PROVABLE] **Before.** `replay_fixture` compared a single opaque
`expected_sha256`. A digest cannot be checked against spec §10's sealed table.

[PROVABLE] **After.** `replay_fixture(fixture_row, bundle)` compares
`expected_verdict_fields` to `observed_verdict_fields` **field by field**,
reporting `missing_fields` and per-field `mismatches`, and additionally
recomputes the observed record from the evidence bundle so a ledger row that
disagrees with its own evidence is caught. The quarantine rule
(`contracts.validate_fixture_row`) rejects any observed field not declared in the
expected record — spec §10's *"no fixture output may populate a live
physical-output field"* made checkable.

[YOURS] Both changes were **against my own convenience**, which is the only
reason the addendum was worth writing. A contract that ratified my build would
have cost me nothing and told the program nothing.

---

## 2. DELTA TABLE — 13 disclosed

| # | File | Change | Authority |
|---|---|---|---|
| D1 | `verifier/contracts.py` | `CHILD_ROW_FIELDS` 11 → 14 (three event carriers) | addendum §1.3 |
| D2 | `verifier/contracts.py` | `EVENT_LEDGER_FIELDS` (6 digest carriers) added | §1.3 |
| D3 | `verifier/contracts.py` | `FIXTURE_ROW_FIELDS` (16) + `validate_fixture_row` with the quarantine rule | §2.3 |
| D4 | `verifier/contracts.py` | `VERIFIER_MANIFEST_FIELDS` (11) + nested `input_roots`(5) / `stdout_discipline`(3) / `exit_contract`(3) + `validate_verifier_manifest` | §3.2 |
| D5 | `verifier/runtime_state.py` | **OWED 1**: `EVENT_LEDGERS` objects → digest fields; `EMPTY_LEDGER_SHA256` added | §1.3 |
| D6 | `verifier/runtime_state.py` | `reclassify_events` re-signatured to fetch by declared digest and recompute | §1.3 |
| D7 | `verifier/replay.py` | **OWED 2**: `replay_fixture` → named-record comparison with missing/mismatch reporting and evidence cross-check | §2.3 |
| D8 | `verifier/verify.py` | child loop reclassifies **all six** event classes (was three, inline) | §1.3 |
| D9 | `verifier/verify.py` | `fixtures[]` processed: contract validation, gated → `NOT_RUN_GATE`, structural → replayed; `fixtures_replayed` added to the verdict | §2.3 |
| D10 | `verifier/verify.py` | stdout discipline: fail-closed diagnostics to **stderr**; stdout carries the verdict only | §3.3 clause 2 |
| D11 | `verifier/child_manifest.py` | **new**: builds and validates `rd22.verifier-manifest.v001`; `optimize` declared, not inferred | §3.2 |
| D12 | `contracts/rd22.verifier-manifest.v001.json` | **new**: the closed JSON schema for the launch manifest | §3.2 |
| D13 | `README.md`, `selfcheck/selfcheck.py` | manifest contract documented; self-check exercises the four inventories, the launch manifest, and the quarantine rule | §§1.3, 2.3, 3.2 |

**Files touched:** 6 changed, 2 new, **6 byte-unchanged** —
`verifier/__init__.py`, `canonical_json.py`, `comparison.py`, `hashing.py`,
`spec_census.py`, `contracts/verifier_verdict.schema.json`. The independence
core (`spec_census.py`) is among the unchanged: **the addendum did not touch how
expectations are derived**, only what shape they take.

---

## 3. UPDATED FILE INVENTORY — 14 files

```text
cbbe6583fe829dc0318f814010fdd50b94727b3c8c8538d03f3d9e05f0da915f  README.md                                  CHANGED
1fdaa0f6181bea11cd264c088dd054499d71bcc0569f3ed3678f5cff20199f29  contracts/rd22.verifier-manifest.v001.json NEW
9a50ce5bd83d0e58c493f64f5a181de963a88ebfd041f72545894909a5d76296  contracts/verifier_verdict.schema.json     unchanged
48bfc493edfa39508513393c8a872782cc5a04d5da5f54f1e7b709ba88d40604  selfcheck/selfcheck.py                     CHANGED
896bfc3837e7e68fbaab68d922df49f9d05ea69e0489d6a862b696e96d5c3e40  verifier/__init__.py                       unchanged
b1424025b1f1f14fb31c5cdbfd42802229ef8c611677135b9f919e00283147b7  verifier/canonical_json.py                 unchanged
2fb497a44877ad76a5b2c71cad4d478bb36c88fcacab5d49db0489bb968ba62e  verifier/child_manifest.py                 NEW
dbce53e5f0a30c08f4d3a61d6201b97aeaf037e944f4ca27bdc54131cf2c7025  verifier/comparison.py                     unchanged
16a55b629c5ca7f2b827e9b66797c9674b944f8e7a06951bc1706b6a7098b4af  verifier/contracts.py                      CHANGED
aee8826ceeed26ec1da7b7859d2c08b7d3d67be3dc873ccdae715a067ebf0632  verifier/hashing.py                        unchanged
eeefe1424559ff31ebdde7803fdf417190536c39c16bdb641fb8da1b559980b2  verifier/replay.py                         CHANGED
081c6b41f7c00ffdd6d586e8afb74e5a70a857911cde2b94c294579c0a67bde9  verifier/runtime_state.py                  CHANGED
d38a66cdaa029addf342fe571fd6c212ed09f522df14e24f46bfc1331f307048  verifier/spec_census.py                    unchanged
e342a381e6d3d913138469e8c2b59517858a66ae557d8ce3a6d99934c107c480  verifier/verify.py                         CHANGED
```

`__pycache__` removed before hashing; no `.pyc` is part of the package.

---

## 4. SELF-CHECK TRANSCRIPT — syntax, schema, and live spec parse

```text
$ python3 selfcheck/selfcheck.py
== Builder B self-check (syntax/schema only) ==
compileall verifier/ : OK
import verifier.*    : OK
LEDGER_FIELDS             : 18 fields
CHECK_ROW_FIELDS          : 14 fields
CHILD_ROW_FIELDS          : 14 fields
AUTHORITY_FIREWALL_FIELDS : 9 fields
CHILD_ROW_FIELDS          : 14 fields (+3 carriers)
FIXTURE_ROW_FIELDS        : 16 fields
VERIFIER_MANIFEST_FIELDS  : 11 fields
EVENT_LEDGER_FIELDS       : 6 digest carriers
launch manifest           : validates, addressable
fixture quarantine        : rejects undeclared field
canonical JSON       : sorted, compact
strict parse rejects : duplicate key
strict parse rejects : NaN literal
criterion split      : 3 atoms
assert scan          : 0 hits (B-V011-SP2-07)
spec census          : 66 ids (63 blocker + 3 discrepancy),
                       {'STRUCTURAL': 56, 'GATED-EXECUTION': 10},
                       board {'BOUND': 35, 'RE-RENDERED': 13,
                              'V004-REPAIRED': 8, 'V005-REPAIRED': 10}
CHAIN_INVOKED        : false
== SELF-CHECK CLEAN ==
exit=0
```

[PROVABLE] **`python -O` parity retained:** normal and optimized runs both exit
`0` with **byte-identical output**, and a fresh scan finds **zero `assert`
statements** across the package. B-V011-SP2-07's demand is tested by consequence,
not by word-match.

[YOURS] Two of the new lines are the ones that would have caught the bugs I
shipped: `EVENT_LEDGER_FIELDS : 6 digest carriers` fails if anyone reverts to
object indexing, and `fixture quarantine : rejects undeclared field` fails if the
named-record comparison is replaced by a digest. **The checks that bite are the
ones aimed at my own prior mistakes.**

---

## 5. BATTERY

### 5.1 Pre-seal pin check

| Claim | Verified before sealing |
|---|---|
| 14 files, digests as listed | `find` + `shasum` after `__pycache__` removal |
| 6 changed / 2 new / 6 unchanged | each digest compared against my prior manifest `f79b50ac…` |
| four inventories at 14 / 16 / 11 / 6 | asserted by the self-check, which fails on any other count |
| launch manifest validates and is addressable | `child_manifest.build_manifest` → `validate_verifier_manifest` → `manifest_sha256` |
| quarantine rule bites | self-check feeds a smuggled field and requires the rejection |
| `-O` parity | both runs captured and diffed |
| census unchanged | 66 / 56-10 / 35-13-8-10 from a live parse; `spec_census.py` byte-unchanged |

### 5.2 `F_PLDEC` and fences

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. No descriptor or fixture was executed and **the chain
was not invoked**. `alpha_computed = false`; `proof_authorized = false`;
`kappa_record_computed = false`; no member bound; no fixed point; no end test; no
numeric evaluation; no comparison to any measured constant.

### 5.3 Coverage, stated exactly (VERDICT-LINE SCOPE RULE)

I conformed **Builder B's verifier** to the sealed addendum and re-ran its
self-check. I did **not** invoke the chain, and I claim **no check outcome** —
`checks_replayed` and `fixtures_replayed` are empty until Custodian C invokes. I
did **not** read Builder A's code or its Q-589 conformance, so I make **no claim
that the two implementations agree**; whether they do is exactly what the first
run is for. My verdict lines claim contract conformance, two owed changes made,
thirteen disclosed deltas, and a passing syntax/schema self-check — **and nothing
else.**

---

## 6. SELF VERB AUDIT

| My verb | Check |
|---|---|
| `CONFORMED = contract + inventories` | All four inventories at the addendum's counts, asserted by a self-check that fails on any other value. |
| `OWED_CHANGES = 2/2 made` | Both displayed before/after at §1, and both are changes **against my own shipped code**. |
| `DELTAS = 13 disclosed` | Tabled with file and authority; 6 changed, 2 new, and the 6 byte-unchanged files named so the untouched set is checkable too. |
| Independence preserved | `spec_census.py` is byte-unchanged: the addendum changed the *shape* of expectations, never their *source*. A's code and A's conformance were not read. |
| `SELF_CHECK = passed` | Syntax, schema, live spec parse, `-O` parity, zero asserts. It still cannot invoke the chain and still says so on its last line. |
| `CHAIN_INVOKED = false` | Literally true. Builder B does not run what Builder B wrote. |
| **Cosmetic defect disclosed** | The self-check prints `CHILD_ROW_FIELDS` **twice** — once from the original inventory loop, once from the new conformance block with `(+3 carriers)`. Harmless duplication in a transcript, not a wrong value; I record it rather than quietly tidy the output I am about to seal. |
| No agreement claimed | I do not say the builders agree. I have not looked, and saying it would be the one thing this custody split cannot survive. |

---

```text
CONFORMED = contract + inventories (CHILD_ROW_FIELDS 11->14 with the three event
  carriers; FIXTURE_ROW_FIELDS 16 with the quarantine rule enforced;
  VERIFIER_MANIFEST_FIELDS 11 plus closed input_roots(5)/stdout_discipline(3)/
  exit_contract(3); EVENT_LEDGER_FIELDS 6 digest carriers. rd22.verifier-
  manifest.v001 is emitted, validated and content-addressed by
  verifier/child_manifest.py, with optimize DECLARED not inferred, stdout
  carrying the verdict alone, and exit 1 vs exit 2 kept as different facts.)
OWED_CHANGES = 2/2 made (1: ledger OBJECTS -> DIGESTS -- reclassify_events now
  fetches each of the six classes by the child row's own declared digest and
  recomputes the canonical digest, where the pre-conformance code indexed objects
  and could reach only three classes; the empty class carries sha256(b"[]"),
  never null and never omitted. 2: the fixture expectation is a NAMED RECORD --
  expected_verdict_fields compared field-by-field with missing/mismatch
  reporting and an evidence cross-check, where the pre-conformance code compared
  one opaque expected_sha256 that could not be checked against spec §10's sealed
  table. Both changes are against MY OWN code, which is the only reason the
  addendum was worth writing.)
DELTAS = 13 disclosed (+table at §2: D1-D4 contracts.py inventories; D5-D6
  runtime_state.py owed change 1; D7 replay.py owed change 2; D8-D10 verify.py
  six-class reclassification, fixture processing, stdout discipline; D11-D12 the
  new launch-manifest module and its closed schema; D13 README and self-check.
  6 files changed, 2 new, and 6 BYTE-UNCHANGED and named -- including
  spec_census.py, so the independence core is demonstrably untouched: the
  addendum changed the SHAPE of expectations, never their SOURCE.)
SELF_CHECK = passed (+transcript at §4: compileall and imports OK; four
  conformance inventories at 14/16/11/6, each asserted so a revert fails the
  check; the launch manifest validates and is content-addressable; the fixture
  quarantine rejects a smuggled field; canonical JSON sorted/compact with
  duplicate-key and NaN rejection; ZERO assert statements; and the census from a
  LIVE PARSE at 66 ids (63+3), 56 STRUCTURAL / 10 GATED, board 35/13/8/10.
  python -O output is BYTE-IDENTICAL to normal.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. No check and
  no fixture has been run; no outcome is claimed. I have NOT read Builder A's
  code or its Q-589 conformance, so I claim NO agreement between the two
  implementations -- whether they agree is what the first run is for.)
VERB_AUDIT_SELF = CLEAN (+1 cosmetic defect disclosed rather than tidied: the
  self-check prints CHILD_ROW_FIELDS twice, once from the original loop and once
  from the new conformance block. Harmless duplication in a transcript I am about
  to seal, and I would rather name it than quietly clean the evidence.)
```

The debt this relay pays was one I created deliberately. Drafting the addendum, I
could have written the two contracts my verifier already satisfied and no one
would have known — my build would have passed its own checks and the divergence
would have surfaced, if at all, as a confusing disagreement with Builder A on
the first run. Writing them the other way cost two changes and bought a fact:
where my implementation and the specification differed, the specification was
right both times.
