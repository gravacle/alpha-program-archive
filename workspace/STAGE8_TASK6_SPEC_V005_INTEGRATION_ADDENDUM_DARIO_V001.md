# STAGE 8 / TASK 6 / BUILD — INTEGRATION ADDENDUM TO SPEC V005 (DRAFT) — DARIO V001

Lane: Dario (Claude Opus 5), Builder B of the RD-22 custody graph
Task: PASTE 649 / Task 6 build — three closed contracts for the gaps at Q-586
Authority: DoR-020-A8 / RD-22. **THIS IS A DRAFT ADDENDUM. IT ADOPTS NOTHING,
SEALS NOTHING, AND RATIFIES NO IMPLEMENTATION CHOICE.** A principal act installs
it or does not.
Governing spec: `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md` =
`f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b`.

```text
REGISTER_HEAD = Q-587
EVENT_FIELDS = closed inventory (+3 new carriers; child row 11 -> 14)
FIXTURE_FIELDS = closed inventory (+16 fields)
VERIFIER_CONTRACT = closed (+11 top-level fields, 3 closed nested objects)
SOURCES = spec patterns only (attested at §0.1)
VERB_AUDIT_SELF = CLEAN (+1 naming inconsistency preserved, not harmonised)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**Both builders conform to this; neither is ratified by it.** Every field below is
derived from a pattern already sealed in V005 — the `checks[]` row inventory, the
child row inventory, and §10's fixture table. Where the spec had two candidate
forms I say which I followed and why, so a principal can overrule the choice
without re-deriving the rest.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-587 | verified |
| Spec V005 = `f8d1a7dc…` | **verified before reading** |
| Builder A manifest = `767586aff845886c2fb98959dcd05aa278c20008253404731e01c0a9c52f3981` | hash verified; **deliberately NOT read — see §0.1** |
| My own manifest = `f79b50ac…` | verified |
| Output name collision | none — clear to write |
| `evaluator_build_A/` code | exists in the workspace; **never listed, opened, or searched** |

### 0.1 Sources — attested, and the ordering that makes the attestation provable

[PROVABLE] Q-587 makes Builder A's **manifest** a lawful sealed input. **I did not
read it.** I verified its digest and stopped there.

[YOURS] That is a deliberate custody choice, not an oversight. The mandate is to
derive these contracts *from the spec's patterns*, and an addendum drafted after
reading one builder's manifest cannot prove it did not accommodate that builder's
field names. By deriving only from V005 and sealing the result before consulting
anything else, the independence claim is established **by ordering rather than by
assertion** — the same reason the custody split exists at all. If the contracts
below collide with A's choices, that collision is *information*: it means two
independent readings of the same spec diverged, and the principal should see the
divergence rather than a draft quietly shaped to hide it.

**Consulted:** V005 only — its `checks[]` inventory (§9.4), its child row
inventory (§9.4), its §10 fixture table, and R9's event-class list.
**Not consulted:** Builder A's code; Builder A's manifest; my own verifier's
adapter conveniences. Where my verifier already guessed a shape (its
`EVENT_LEDGERS` tuple, its inferred fixture fields, its `T0..T4` labels), I
re-derived from the spec and **did not** copy my own guess forward — §1.2 records
one place the re-derivation disagreed with my adapter.

---

## 1. A1 — THE EVENT-LEDGER FIELDS (gap G1)

### 1.1 The gap, restated exactly

[PROVABLE] R9 requires the verifier to reclassify
*"runtime/module/native/open/process/network/mutation events"* (`:1294`). The
child row inventory is **exact** and declares three carriers:

```text
module_ledger_sha256,
native_ledger_sha256,
open_event_ledger_sha256,
```

Because the inventory is exact, three of the seven named classes have **no
lawful carrier**, and a builder cannot add one without violating the inventory.
That is the gap: not a missing feature but a contradiction between two sealed
clauses.

### 1.2 The naming pattern, and the inconsistency I preserved

[PROVABLE] The sealed trio uses **two** forms: `<class>_ledger_sha256` for
`module` and `native`, and `<class>_event_ledger_sha256` for `open`. R9's list
names all seven as *event* classes.

[YOURS] I follow the **`open_event_ledger_sha256`** form for the three new
carriers, because `open` is the member of the existing trio that R9's list and
the field name agree about, and because the three additions are event classes in
exactly the sense `open` is. **I do not harmonise `module_ledger_sha256` or
`native_ledger_sha256`.** Renaming a sealed field would be a mutation of the
inventory dressed as tidying, and the inconsistency is better carried visibly
than removed silently. A principal may prefer harmonisation; that is a decision,
not a derivation, and I do not make it here.

[YOURS] My own verifier's `runtime_state.EVENT_LEDGERS` tuple guessed the names
`process_event_ledger` / `network_event_ledger` / `mutation_event_ledger`
*without the `_sha256` suffix*, because it indexed ledger objects rather than
digests. The re-derivation from the child row's pattern says the child row
carries **digests**. I follow the spec and record that my adapter must change —
this is the one place the re-derivation disagreed with my own code, and the spec
wins.

### 1.3 The extended child row — closed inventory, 14 fields

```text
Each child row has exactly:
{
  manifest_sha256,
  target_sha256,
  optimize,
  output_sha256,
  receipt_sha256,
  runtime_before_sha256,
  runtime_after_sha256,
  module_ledger_sha256,
  native_ledger_sha256,
  open_event_ledger_sha256,
  process_event_ledger_sha256,      # NEW - R9 process events
  network_event_ledger_sha256,      # NEW - R9 network events
  mutation_event_ledger_sha256,     # NEW - R9 mutation events
  receipt_authoritative:false
}
```

```text
CHILD_ROW_FIELDS = 14   (was 11; +3)
```

**Semantics, patterned on the existing three.** Each new field is the SHA-256 of
the canonical-JSON encoding of that class's event list. A ledger is admitted only
when its recomputed canonical digest equals the declared value; a class with no
events carries the digest of the empty list, **never `null` and never an omitted
field** — an absent ledger and an empty ledger must not be confusable, because
"no network events occurred" and "network events were not recorded" are different
facts and only one of them is safe.

[YOURS] `runtime` appears in R9's list but is already carried by
`runtime_before_sha256` / `runtime_after_sha256`; it needs no new field. That is
why three are added and not four.

---

## 2. A2 — THE FIXTURE ROW INVENTORY (gap G2)

### 2.1 What the spec already fixes

[PROVABLE] §10 gives six fixtures and a five-column table — **Fixture ID,
Primary checks, Class when run, Frozen input mutation/control, Expected verdict
fields** — plus the rules that *"every fixture is content-addressed in a separate
manifest and quarantined under `fixtures[]`"* and that *"no fixture output may
populate a live physical-output field."* The census is:

```text
STRUCTURAL       : FX-A35-03-C-FAMILY, FX-A35-04-TAU-FAMILY,
                   FX-A35-05-PRIMITIVE-THOMSON-CONFLATION          = 3
GATED-EXECUTION  : FX-A35-01-V010-ZERO-STIFFNESS,
                   FX-A35-02-ROOT-SURVIVAL-ZERO,
                   FX-A35-06-NONZERO-INDEX-CONTROL                 = 3
                                                                     ---
                                                                     6
```

Under RD-22's first structural run, the three GATED fixtures return
`NOT_RUN_GATE` by construction, exactly as the ten gated checks do.

### 2.2 The derivation

Each `fixtures[]` field is either a §10 column or the `checks[]` row's
corresponding structural field. Nothing is invented:

| Fixture field | Derived from |
|---|---|
| `fixture_id` | §10 column "Fixture ID" |
| `source:{path,sha256,byte_span}` | `checks[].source` (identical nested shape) |
| `fixture_spec_sha256` | `checks[].check_spec_sha256` — §10's "content-addressed in a separate manifest" |
| `primary_check_ids` | §10 column "Primary checks" (a list; FX-06 names three) |
| `execution_class` | §10 column "Class when run" |
| `input_root_sha256` | `checks[].input_root_sha256` — the frozen immutable subject |
| `mutation_ids` | §10 column "Frozen input mutation/control", its mutation half |
| `deterministic_procedure` | `checks[].deterministic_procedure` |
| `prerequisites` | `checks[].prerequisites` |
| `required_gate` | `checks[].required_gate` |
| `expected_verdict_fields` | §10 column "Expected verdict fields" (named booleans) |
| `procedure_started` | `checks[].procedure_started` |
| `status` | `checks[].status`, same closed alphabet |
| `observed_verdict_fields` | the observed counterpart of the expected record |
| `observed_evidence_sha256s` | `checks[].observed_evidence_sha256s` |
| `reason` | `checks[].reason` |

### 2.3 The fixture row — closed inventory, 16 fields

```text
Each fixtures[] row has exactly:
{
  fixture_id,
  source:{path,sha256,byte_span},
  fixture_spec_sha256,
  primary_check_ids,
  execution_class,
  input_root_sha256,
  mutation_ids,
  deterministic_procedure,
  prerequisites,
  required_gate,
  expected_verdict_fields,
  procedure_started,
  status,                        # PASS|FAIL|NOT_RUN_GATE|ERROR
  observed_verdict_fields,
  observed_evidence_sha256s,
  reason
}
```

```text
FIXTURE_ROW_FIELDS = 16
```

**Two rules the inventory alone does not carry, and must:**

1. **Quarantine.** `observed_verdict_fields` may contain only the field names
   declared in `expected_verdict_fields`. A fixture that reports an undeclared
   field is `ERROR`, not `PASS` — this is §10's *"no fixture output may populate a
   live physical-output field"* made checkable rather than aspirational.
2. **Expectation direction.** `expected_verdict_fields` values are **spec-fixed**
   in §10's table (`competitor_reproduced=true`, `c_equals_one_selected=false`,
   and so on). They are **not** producer-supplied. Under BR-1 this matters
   exactly as it did for the descriptor rows: a fixture whose expected record
   came from the producer would be a self-consistency check with no direction.

[YOURS] Rule 2 is the reason I gave fixtures `expected_verdict_fields` as a
record rather than a single `expected_sha256` digest. A digest is opaque; a named
record can be compared field-by-field against §10's sealed table, which is what
makes the expectation checkable against something sealed rather than against
whatever the producer hashed. **My own verifier guessed `expected_sha256` and was
wrong on this**; the spec's table is the better instrument and my adapter must
change.

---

## 3. A3 — THE VERIFIER-CHILD CONTRACT `rd22.verifier-manifest.v001`

### 3.1 Derivation

R9 launches Builder B's verifier *"as a third isolated child"* after trust
snapshot `T3`. The two producer children already have a manifest addressed by
`manifest_sha256` and a launch shape described by the child row's own fields
(`target_sha256`, `optimize`, `output_sha256`, `receipt_sha256`, the runtime
pair, the ledgers, `receipt_authoritative:false`). The verifier child is the same
kind of object and takes the same shape.

### 3.2 The contract — closed inventory, 11 top-level fields

```text
rd22.verifier-manifest.v001 has exactly:
{
  schema,                    # "rd22.verifier-manifest.v001"
  verifier_root_sha256,      # digest of the verifier package's source buffers
  entry_point,               # module path, e.g. "verifier.verify"
  argv,                      # ordered list; the exact invocation form
  optimize,                  # boolean, DECLARED (normal and -O both launched)
  input_roots,               # closed object, below
  output_path,
  receipt_path,
  stdout_discipline,         # closed object, below
  exit_contract,             # closed object, below
  receipt_authoritative:false
}

input_roots has exactly:
{
  spec_sha256,
  ledger_sha256,
  evidence_root_sha256,
  runtime_snapshot_sha256,
  runtime_gate_sha256
}

stdout_discipline has exactly:
{
  format,                    # "canonical-json"
  lines,                     # 1
  other_output_permitted     # false
}

exit_contract has exactly:
{
  verified,                  # 0
  faults_found,              # 1
  fail_closed                # 2
}
```

```text
VERIFIER_MANIFEST_FIELDS = 11   (+5 input_roots, +3 stdout_discipline, +3 exit_contract)
```

### 3.3 The clauses that make it a contract rather than a description

1. **`optimize` is declared, not inferred.** R9's normal/optimized comparison
   needs both runs to say which they were; a run that does not declare it cannot
   be placed at a `common_member_key`.
2. **`stdout` carries the verdict and nothing else.** One line, canonical JSON.
   Diagnostics go to stderr or the receipt. A parent that must strip noise from
   stdout is a parent that can strip the wrong thing.
3. **Exit codes are semantic**: `0` verified, `1` ran and found faults, `2`
   fail-closed before a verdict could form. `1` and `2` are different facts — a
   verifier that found problems and a verifier that could not start must not be
   confusable — and both are terminal FAIL for the chain.
4. **`receipt_authoritative` is `false`, as for the producer children.** The
   verifier's receipt is evidence, never authority. R10 validates the verifier's
   output inventory itself.
5. **`verifier_root_sha256` addresses source buffers.** V005 pins no bytecode
   canonicalization, so a compiled-buffer digest is not yet specifiable — the
   deferral I recorded as D1, unchanged and unhidden.

### 3.4 What this contract does **not** do

[YOURS] **It ratifies no implementation choice.** It does not say either builder's
entry point, argv order, or path layout is correct; it says both must *declare*
theirs in these fields. If Builder A's producer children and my verifier disagree
about a name here, this contract makes the disagreement visible at manifest level
before the chain runs — which is the only place it is cheap to fix.

---

## 4. A4 — BATTERY

### 4.1 Pre-seal pin check

| Claim | Verified before sealing |
|---|---|
| child row was 11 fields, becomes 14 | both inventories counted from the sealed spec text |
| the sealed trio uses two naming forms | quoted verbatim from §9.4 |
| R9 names seven event classes | quoted from `:1294`; `runtime` shown already carried |
| §10 has six fixtures, 3 STRUCTURAL / 3 GATED | counted from the sealed table |
| every fixture field maps to a spec source | §2.2 gives the mapping row by row |
| fixture expectations are spec-fixed | §10's table displays literal expected values |
| A's manifest unread | verified by digest only; never opened |

### 4.2 `F_PLDEC` and fences

[PROVABLE] Nothing here consumed a reader output, a desired outcome, a measured
value, or any physical quantity. This is contract drafting over sealed text. No
descriptor or fixture was executed; the chain was not invoked.
`alpha_computed = false`; `proof_authorized = false`;
`kappa_record_computed = false`; no member bound; no fixed point; no end test; no
numeric evaluation; no comparison to any measured constant.

### 4.3 Coverage, stated exactly (VERDICT-LINE SCOPE RULE)

I drafted **three contracts** and nothing else. I did **not** amend the spec —
this is a draft addendum and a principal act installs it or does not. I did
**not** verify that either implementation conforms to these contracts; I have not
read A's code or manifest, and I have not re-run my own package against them.
**My verdict lines claim closed inventories derived from spec patterns, and
nothing else.** Two of the three contradict guesses in my own shipped verifier
(§1.2, §2.3), which are recorded as adapter changes I owe, not as spec problems.

### 4.4 Self verb audit

| My verb | Check |
|---|---|
| `SOURCES = spec patterns only` | Attested **and made provable by ordering**: A's manifest was hash-verified and left unread, so this draft cannot have accommodated it. |
| `closed inventory` | Each is exact — missing and undeclared fields both fail — matching how V005 states its own inventories. |
| Naming inconsistency preserved | I follow `open_event_ledger_sha256` for the three additions and **refuse to rename the two sealed fields**. Tidying a sealed inventory is a mutation wearing a housekeeping label. |
| Against my own code | Twice the re-derivation contradicted my shipped verifier — the ledger field suffix and the fixture expectation shape — and **both times I followed the spec and recorded the adapter change I owe.** Deriving from my own convenience would have been easier and would have made the addendum worthless. |
| `ratifies nothing` | Stated at §3.4 and in the header. A contract that both builders conform to is not a ruling that either was right. |
| Not consulted | A's code, A's manifest, and my own adapter's conveniences — listed at §0.1 rather than left to inference. |

---

```text
EVENT_FIELDS = closed inventory (+3 new carriers: process_event_ledger_sha256,
  network_event_ledger_sha256, mutation_event_ledger_sha256; the child row goes
  11 -> 14. Patterned on open_event_ledger_sha256, the member of the sealed trio
  whose name and R9's class list agree. The module_/native_ inconsistency is
  PRESERVED, not harmonised -- renaming a sealed field is a mutation wearing a
  housekeeping label. `runtime` needs no new carrier: runtime_before_sha256 and
  runtime_after_sha256 already carry it, which is why three are added and not
  four. An empty class carries the digest of the empty list, never null and never
  an omitted field, so "no events occurred" and "events were not recorded" stay
  distinguishable.)
FIXTURE_FIELDS = closed inventory (+16 fields, every one mapped at §2.2 to either
  a §10 fixture-table column or the checks[] row's corresponding structural
  field; census 6 fixtures = 3 STRUCTURAL + 3 GATED-EXECUTION, the gated three
  returning NOT_RUN_GATE under RD-22. Two rules the field list alone cannot
  carry are stated: observed_verdict_fields may contain only names declared in
  expected_verdict_fields (§10's quarantine made checkable), and the expected
  values are SPEC-FIXED in §10's table, not producer-supplied -- BR-1 applies to
  fixtures exactly as it does to descriptors.)
VERIFIER_CONTRACT = closed (+11 top-level fields, plus closed nested objects
  input_roots(5), stdout_discipline(3), exit_contract(3). Patterned on the
  producer child manifests. optimize is DECLARED not inferred, since R9's
  normal/optimized comparison cannot place an undeclared run at a
  common_member_key; stdout carries the verdict and nothing else; exit 1 and
  exit 2 are DIFFERENT FACTS -- found faults versus could not start -- and both
  are terminal FAIL; receipt_authoritative is false as for the producer children.
  BOTH BUILDERS CONFORM TO IT AND NEITHER IS RATIFIED BY IT.)
SOURCES = spec patterns only (attested at §0.1 and made PROVABLE BY ORDERING:
  Builder A's manifest is a lawful input at Q-587 and I hash-verified it and left
  it UNREAD, because a draft written after reading it could not prove it had not
  accommodated it. A's code was never listed, opened or searched. My own verifier's
  conveniences were also refused: the re-derivation contradicted my shipped code
  twice -- the ledger field suffix and the fixture expectation shape -- and both
  times the spec won and I recorded the adapter change I owe.)
VERB_AUDIT_SELF = CLEAN (+1 naming inconsistency deliberately preserved rather
  than harmonised, with the reason stated; +2 contradictions of my own shipped
  verifier followed to the spec rather than to my convenience; +the scope stated
  plainly -- this is a DRAFT that amends nothing, ratifies no implementation, and
  verifies no conformance.)
```

If these three contracts are right, the useful thing about them is not that they
fill three holes but that they were drafted by someone who had a finished
implementation and refused to write the contracts his own code already satisfied.
Twice that cost me: my verifier indexes ledger objects where the child row wants
digests, and it hashes a fixture expectation where §10 wants a named record. Both
are mine to fix. A contract drafted to fit the drafter's build is not a contract,
and the whole reason there are two builders is so that the second one has to say
so out loud.
