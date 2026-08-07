# STAGE 8 / TASK 6 / BUILD — THE INDEPENDENT VERIFIER (BUILDER B) — DARIO V001

Lane: Dario (Claude Opus 5) **as Builder B** of the RD-22 custody graph
Task: PASTE 648 / Task 6 build — the independent verifier, per sealed spec V005 §R9
Authority: RD-22 (`DECISION_RD22_BUILD_AUTHORIZED_2026-08-07.md`,
`ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340`)
Custody: Builder A = Codex Lane 2 (producer + parent); **Builder B = Dario
(verifier)**; Custodian C = the registrar (invokes; authored neither).

```text
REGISTER_HEAD = Q-585
PACKAGE = complete (+5 deferred, listed at §3)
FILES = 12 (inventory hashed at §2)
INDEPENDENCE = sealed inputs only (attested at §1)
SELF_CHECK = syntax/schema only (transcript at §4)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+2 spec gaps reported, not peeked at)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**I have written the verifier and I have not run the chain.** Builder B does not
run what Builder B wrote; Custodian C invokes it. The self-check below is
syntax and schema validation only, and its last line says so.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-585 | verified |
| RD-22 authorization = `ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340` | **verified before reading**; read in full — it binds scope, pin and custody |
| Governing spec V005 = `f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b` | **verified before reading** |
| Output artifact name collision | none — clear to write |
| `evaluator_build_A/` | **does not exist in the workspace; never listed, opened, or searched** |

**Scope as authorized:** implementation plus the **first structural run** — the
56 STRUCTURAL checks and structural fixtures only; the 10 GATED-EXECUTION checks
return `NOT_RUN_GATE` **by construction**, not by runtime choice. RD-22 opens no
physical gate, and a runner PASS confers no seal and no physics authority.

---

## 1. INDEPENDENCE — attested

[PROVABLE] The package imports nothing from the producer. Its every expectation
is parsed at run time out of the **sealed specification bytes**, admitted only
after those bytes hash to `f8d1a7dc…`:

```text
verifier/spec_census.py derives, from the sealed spec alone:
  the 63 blocker IDs + 3 discrepancy IDs          = 66 check-ID universe
  the execution-class partition                    = 56 STRUCTURAL / 10 GATED
  the §8.3 binding board                           = 35 BOUND + 13 RE-RENDERED
                                                     + 8 V004-REPAIRED
                                                     + 10 V005-REPAIRED
  each descriptor row's own content address        = check_spec_sha256
```

Every one of those figures is **re-derived by the code, not transcribed by me**,
and the self-check prints them from a live parse (§4). If the producer's ledger
and the sealed spec disagree on any of them, `SpecCensus` raises and the run
fails closed — the spec wins.

[YOURS] The design rule I held to: **an expectation that could only come from
Builder A's code is a spec gap, not a lookup.** Twice I wanted such a detail and
both times I wrote it down as a gap (§3) rather than reach for it. Builder A's
directory does not yet exist, so independence here is structural rather than
merely disciplined — but the rule would have held either way, and the two gaps
are the evidence that it bound something real.

---

## 2. FILE INVENTORY — 12 files, per-file SHA-256

```text
a2fdf0fe45a143a570e2bd70c3188b1eb804300f59d9ffcf5548d8603d188d24  README.md
9a50ce5bd83d0e58c493f64f5a181de963a88ebfd041f72545894909a5d76296  contracts/verifier_verdict.schema.json
62cd0b71f93b3ccdb320d698accfca553c9c5da41545797a07f57cd8fe0ff6b9  selfcheck/selfcheck.py
896bfc3837e7e68fbaab68d922df49f9d05ea69e0489d6a862b696e96d5c3e40  verifier/__init__.py
b1424025b1f1f14fb31c5cdbfd42802229ef8c611677135b9f919e00283147b7  verifier/canonical_json.py
dbce53e5f0a30c08f4d3a61d6201b97aeaf037e944f4ca27bdc54131cf2c7025  verifier/comparison.py
e62a724bec7b99f8217db00de60d421d41b142d3b841e2f4bedb29e901f2291a  verifier/contracts.py
aee8826ceeed26ec1da7b7859d2c08b7d3d67be3dc873ccdae715a067ebf0632  verifier/hashing.py
03201a1caf6a5344ed2524dc949a9ea914d0b6b2fbbb093cd95e4e15ceebcb89  verifier/replay.py
a7b9cec968e4715218585da14316b9f6319abbb5f5d5f58582711001a05ddf2f  verifier/runtime_state.py
d38a66cdaa029addf342fe571fd6c212ed09f522df14e24f46bfc1331f307048  verifier/spec_census.py
f4f971a74425fea2ffc1028a1864aac29d83f6255a09e8fe8e93ebc3597bd01a  verifier/verify.py
```

`__pycache__` is removed before hashing; no `.pyc` is part of the package.

### 2.1 Entry point and invocation contract (Custodian C)

Run from `evaluator_build_B/` so `verifier` is importable:

```text
python3 -m verifier.verify \
  --spec              <STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md> \
  --ledger            <producer canonical verdict ledger JSON> \
  --ledger-sha256     <expected sha256 of that ledger> \
  --evidence-dir      <dir of content-addressed evidence, named <sha256>.json> \
  --runtime-snapshot  <provenance/primitive_step6_runtime_snapshot_v012.json> \
  --runtime-gate      <primitive_step6_content_addressed_runtime_gate_v010.md>
```

```text
exit 0 = VERIFIED
exit 1 = verifier ran, faults found (verdict FAIL, findings enumerated)
exit 2 = fail-closed fault before a verdict could be formed
```

Any non-zero exit is a terminal FAIL for the chain. Output is one line of
canonical UTF-8 JSON conforming to `contracts/verifier_verdict.schema.json`.

### 2.2 R9 duties — where each is implemented

| R9 duty | Module |
|---|---|
| rehash every input and source buffer | `hashing.load_addressed`, `verify._self_digest` |
| strict-parse manifests, outputs, receipts | `canonical_json.loads_strict`, `contracts.*` |
| 63+3 census, 66 descriptor digests, 56/10 partition, the binding board | `spec_census.SpecCensus` |
| replay each pass predicate from evidence bytes | `replay.replay_predicate` |
| replay every fixture's expected result | `replay.replay_fixture` |
| reclassify runtime/module/native/open events | `runtime_state.reclassify_events`, `verify` child loop |
| revalidate before/after trust records | `runtime_state.revalidate_trust_snapshots` (T4=T3=T2=T1=T0) |
| compare normal and optimized outputs | `comparison.compare_semantic_outputs` (`COMMON_MEMBER_ONLY`) |
| authorization hash and gate discipline | `comparison.check_authorization`, `check_gate_discipline` |
| authority-firewall fields false unless authorized | `contracts.validate_authority_firewall` |

---

## 3. IMPLEMENTED vs DEFERRED — listed, not silent

**Implemented and exercised by the self-check:** canonical JSON with
duplicate-key and nonfinite rejection; content-addressed admission with no path
trust; the census derivation; the exact field inventories for the ledger, check
rows, child rows and firewall; criterion splitting and opcode-reducible atom
replay including the finite universal over an `ENUM` result; the runtime pin
with the **v014 substitution explicitly refused**; trust-drift fail-closed;
event-ledger digest recomputation; `COMMON_MEMBER_ONLY` comparison that reports
unmatched members instead of intersecting them; gate discipline.

**Deferred, with reasons:**

| # | Deferred | Why | Consequence |
|---|---|---|---|
| D1 | **Compiled-source-buffer rehash** | R9 says "exact compiled source buffer". `.pyc` content varies with interpreter build and the spec pins no bytecode canonicalization. `verify._self_digest` hashes the **source** buffers instead. | The verifier's self-digest is source-exact, not bytecode-exact. If the chain requires bytecode identity, the canonicalization must be specified first. |
| D2 | **Fixture manifest schema** | `replay.replay_fixture` implements the replay, but §9.4 fixes no field inventory for a fixture row the way it does for checks and children. I used `fixture_id`, `expected_sha256`, `observed_result_name`. | If Builder A's fixture rows carry different field names, this binds on the first run. **Reported as gap G2 below rather than resolved by reading A's code.** |
| D3 | **process / network / mutation event ledgers** | R9 requires reclassifying them, but the exact child-row inventory in §9.4 declares carriers for **module, native and open** ledgers only. `runtime_state.EVENT_LEDGERS` names all six; the child loop can only fetch the three that have declared digests. | **Spec gap G1 below.** Three of six event classes have no declared carrier field. |
| D4 | **Trust-snapshot label set** | R9/R10 name `T0`–`T4` in prose; no sealed schema declares the object's shape. I required exactly `{T0..T4}`. | If the producer emits different labels, this binds on the first run. |
| D5 | **`BRANCH_OUTCOME` per-ID values check** | RD-22 carries the Q-583 obligation that these be *displayed in the implementation manifest* — which is Builder A's manifest. I have no sealed source for the values, so I cannot verify them. | **Spec gap G3 below.** I can check that a display *exists* once its location is specified; I cannot check its correctness against anything sealed. |

### 3.1 Spec gaps reported (not peeked at)

**G1 — three event classes have no declared carrier.** R9 requires reclassifying
`process`, `network` and `mutation` events; §9.4's exact child-row inventory
provides `module_ledger_sha256`, `native_ledger_sha256` and
`open_event_ledger_sha256` and nothing else. Since the inventory is *exact*,
adding fields would itself be a violation. **Either the child inventory needs
three more declared digest fields, or R9's list needs to name the carrier these
three travel in.** I did not guess, and I did not look at how Builder A solved it.

**G2 — no fixture-row field inventory.** Checks and children have exact
inventories; fixtures do not. Two independent builders will therefore invent two
shapes. **A fixture row inventory belongs in §9.4.**

**G3 — `BRANCH_OUTCOME` values are still undisplayed anywhere sealed.** This is
the item I carried forward at Q-583 and declined to charge as a BR-1 violation.
RD-22 turns it into a build obligation on the implementation manifest. As
verifier I record that **there is no sealed artifact against which I could check
those values**, so a verifier "PASS" on that obligation would today be a check of
existence, not of correctness.

[YOURS] All three gaps are of one kind: **a detail two independent builders must
agree on that no sealed document fixes.** That is precisely what independent
custody is for — it surfaces them before the first run instead of after, and it
only works if the second builder writes them down rather than reaching for the
first builder's answer.

---

## 4. SELF-CHECK TRANSCRIPT — syntax and schema only

```text
$ python3 selfcheck/selfcheck.py
== Builder B self-check (syntax/schema only) ==
compileall verifier/ : OK
import verifier.*    : OK
LEDGER_FIELDS             : 18 fields
CHECK_ROW_FIELDS          : 14 fields
CHILD_ROW_FIELDS          : 11 fields
AUTHORITY_FIREWALL_FIELDS : 9 fields
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

[PROVABLE] **`python -O` parity, which is what B-V011-SP2-07 actually demands.**
The blocker's grammar puts "load-bearing" on *audit*, not on *assert*: a
load-bearing audit must be free of Python `assert`. So I tested the consequence
rather than the word —

```text
$ python3    selfcheck/selfcheck.py  > normal.txt   (exit 0)
$ python3 -O selfcheck/selfcheck.py  > opt.txt      (exit 0)
$ diff normal.txt opt.txt   ->  IDENTICAL
```

zero `assert` statements found by scan **and** byte-identical behaviour with
assertions disabled. The census line is a live parse of the sealed spec, not a
constant: it is the same 66 / 56-10 / 35-13-8-10 the spec's own board carries.

---

## 5. BATTERY

### 5.1 `F_PLDEC`

[PROVABLE] Nothing here consumed a reader output, a desired outcome, a measured
value, or any physical quantity. The package computes digests, parses text, and
compares records. **No descriptor was executed and the chain was not invoked.**
`alpha_computed = false`; `proof_authorized = false`;
`kappa_record_computed = false`; no member bound; no fixed point; no end test; no
numeric evaluation of any physical quantity; no comparison to any measured
constant. `F_PLDEC = CLEAN`.

### 5.2 Anti-tuning

[YOURS] The structural anti-tuning property of this build is that **the verifier
cannot be tuned toward agreement with the producer, because it never sees the
producer's expectations.** Its census comes from sealed bytes; its predicate
replay comes from the descriptor's own criterion and content-addressed evidence;
its comparison is `COMMON_MEMBER_ONLY` and reports unmatched members rather than
intersecting to the agreeable subset. A verifier that computed its expectations
from A's manifest would agree with A by construction, which is the whole failure
this custody split exists to prevent.

### 5.3 Pre-seal pin check

| Claim | Verified before sealing |
|---|---|
| 12 files, digests as listed | `find` + `shasum` after `__pycache__` removal |
| census 66 / 56-10 / 35-13-8-10 | live parse of the sealed spec by the shipped code |
| zero `assert` | source scan **and** `-O` output equality |
| self-check does not invoke the chain | it has no call path to `verify.verify`; prints `CHAIN_INVOKED: false` |
| RD-22 pin honoured | `runtime_state` constants equal the authorization's triple; v014 refused by name |
| firewall fields | `FIREWALL_NEVER_TRUE_UNDER_RD22` covers all six physics/seal fields |

### 5.4 Coverage, stated exactly (VERDICT-LINE SCOPE RULE)

I built and self-checked the **verifier only**. I did **not** build the parent,
producer, manifests, schemas or fixtures — those are Builder A's. I did **not**
invoke the chain, and I make **no claim whatever** about whether any check
passes: no check has been run, and `checks_replayed` is empty until Custodian C
invokes. My verdict lines claim package completeness, an attested independence
discipline, a hashed inventory and a syntax/schema self-check — **and nothing
else.**

---

## 6. SELF VERB AUDIT

| My verb | Check |
|---|---|
| `PACKAGE = complete` | Complete **for the R9 verifier duties**, with five deferrals listed and reasoned at §3 — not silent. |
| `INDEPENDENCE = sealed inputs only` | Attested and *demonstrated*: the census is a live parse of sealed bytes. A's directory was never listed, opened or searched, and it does not exist. |
| `SELF_CHECK = syntax/schema only` | The script has no call path into `verify.verify`, and prints `CHAIN_INVOKED: false` as its own last check. |
| `CHAIN_INVOKED = false` | Literally true. Builder B does not run what Builder B wrote. |
| Two gaps reported | G1 and G3 are places I wanted a detail only A's code could supply. **Reporting them is the deliverable; peeking would have destroyed the thing the custody split buys.** |
| `assert` discipline | Tested by consequence (`-O` parity), not by word-matching — the same reading of B-V011-SP2-07 I convicted V002 for getting backwards. |
| No physics claim | The package computes no physical quantity and the manifest asserts none. A runner PASS confers no seal — encoded in the firewall check, not just written here. |

---

```text
PACKAGE = complete (+5 deferred, each with its reason at §3: D1 compiled-source-
  buffer rehash -- the spec pins no bytecode canonicalization, so the self-digest
  is source-exact; D2 fixture-row field inventory -- §9.4 fixes one for checks and
  children but not fixtures; D3 process/network/mutation event ledgers -- R9
  requires reclassifying them but the EXACT child inventory declares carriers for
  module/native/open only; D4 trust-snapshot label set -- T0..T4 appear in prose,
  not in a sealed schema; D5 BRANCH_OUTCOME per-ID values -- no sealed source
  exists against which to check them)
FILES = 12 (+inventory hashed at §2; __pycache__ removed before hashing)
INDEPENDENCE = sealed inputs only (attested at §1 and DEMONSTRATED: the 63+3
  census, the 56/10 partition, the 35/13/8/10 board and every descriptor digest
  are parsed at run time from the sealed spec bytes by the shipped code, not
  transcribed. evaluator_build_A/ was never listed, opened or searched, and does
  not exist in the workspace. Three details I wanted are reported as SPEC GAPS
  G1-G3 rather than resolved by reading A's implementation.)
SELF_CHECK = syntax/schema only (+transcript at §4: compileall OK; imports OK;
  four contract inventories sized; canonical JSON sorted/compact; strict parse
  rejects duplicate keys and NaN; criterion split reducible; ZERO assert hits;
  and the census printed from a LIVE PARSE of the sealed spec at 66 ids
  (63 blocker + 3 discrepancy), 56 STRUCTURAL / 10 GATED-EXECUTION, board
  35 BOUND + 13 RE-RENDERED + 8 V004-REPAIRED + 10 V005-REPAIRED. python -O
  output is BYTE-IDENTICAL to normal, which is what B-V011-SP2-07 actually
  demands -- its "load-bearing" modifies AUDIT, not ASSERT.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote; Custodian C
  invokes. No check has been run and no check outcome is claimed here.)
VERB_AUDIT_SELF = CLEAN (+2 spec gaps reported rather than peeked at -- G1 three
  event classes with no declared carrier field, G3 BRANCH_OUTCOME with no sealed
  source; +G2 the missing fixture inventory. All three are the same kind: a
  detail two independent builders must agree on that no sealed document fixes,
  which is exactly what independent custody exists to surface.)
```

The verifier is written and the chain is untouched. What this build is *for* is
not that a second implementation exists but that a second one was written without
seeing the first, and the honest yield of that discipline is three questions no
sealed document answers. I would rather hand over a package with three gaps named
than one with three gaps quietly filled in from the other builder's answers —
those would agree on the first run and neither of us would know why.
