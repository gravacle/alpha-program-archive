# STAGE 8 / TASK 6 / BUILD — THE REPLAY DISAGREEMENT, DIAGNOSED AT SOURCE — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 693 / Task 6 build — run 030's `REPLAY_DISAGREE` on C-B-V009-06
Authority: RD-22. **THIS ARTIFACT INVOKES NOTHING.**

```text
FAILING_STEP = atom `P0`, the FIRST of three (displayed at §1); r_ground was never reached
SPEC_DETERMINES = yes for r_ground/r_dag (fixed to spec) / no for P0 (gap stated)
VERDICT_FOLLOWS = the spec (r_dag agrees with A; P0 pending the spec)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 BR-1 violation found in MY OWN replay, §2.1;
                         +1 defect in my own fix caught by the demonstration, §2.4;
                         +1 contract of mine below the spec, §3)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**The candidate root cause is refuted, and the true one is worse.** The registrar
proposed that my `r_ground` derivation — a wrap/strip recipe on the raw span —
differs from A's. My replay never reaches `r_ground`. And the row's `r_ground`
does not derive a value from the raw span at all.

## 1. G1 — THE FAILING STEP, REPRODUCED AND DISPLAYED

Run locally against `rd22_run_030/evidence/`, using the row's own recorded digests.

```text
observed_evidence_sha256s (producer order)
    a68204715597d161ece10ac731566e0b55bc3c4b237051b282e43adc1f73c736
    47e7c32915bc756fb5f6be25c4fc6dec5c079c8837176dc62499e0f34f4c9d3b

STEP 1  digest-verify ALL payloads via load_addressed          2/2 admitted

STEP 2  classify_payloads                                      faults: []
    CONSUMABLE  a6820471…   594 B      the canonical 11-node graph object
    RAW         47e7c329…   932 B      linkage=digest+span
    unrequired_args: ['authority']

STEP 3  EvidenceBundle built from the consumable payload
    bundle.sha256 = a6820471…            bundle bytes = 594
    bundle KEYS   = ['ALPHA-RESULT-SEAL', 'CORE-RESULT-SEAL',
                     'END-TO-END-RECONSTRUCTION-SEAL', …]   (11 total)

STEP 4  replay_predicate('P0 and r_ground.success and r_dag.success')
    atoms: ['P0', 'r_ground.success', 'r_dag.success']
      atom 'P0'  ->  False
      *** SHORT-CIRCUITS. The remaining two atoms are NEVER EVALUATED. ***
    replay_predicate -> False      producer status -> PASS     => REPLAY_DISAGREE
```

**The failing step, named:** atom `P0`, in `replay_atom`:

```python
if atom == "P0":
    return bundle.success("P0") if "P0" in bundle.results else False
```

```text
'P0'       in bundle.results : False
'r_ground' in bundle.results : False
'r_dag'    in bundle.results : False
```

`bundle.results` is the **11-node graph**, not an opcode-result object. The
predicate fails at its first conjunct and returns before `r_ground` exists as a
question. **No wrap/strip recipe ran, on either side of the disagreement.**

## 2. G2 — ADJUDICATION AT THE SPEC

### 2.1 [PROVABLE] The determined half: R9 replays FROM EVIDENCE BYTES

Sealed V007, state `R9`, duty list:

> replays each pass predicate **from evidence bytes**

and §2.2: *"Each opcode has one result object and one Boolean success bit."*

My replay read `.success` off a bundle the **producer** emitted. That is a
producer-declared object carrying the criterion's direction — **BR-1, the law
this lane has enforced against Builder A for twenty relays, violated inside
Builder B's own verifier.** Hash-pinning the bundle prevents substitution, not
fabrication. The spec determines the cure: recompute the atoms.

**Fixed.** `recompute_results()` now derives each recorded invocation's result
object from its arguments, and the bundle the predicate replays against is built
from *those*. Two opcodes are implemented, exactly the two this row's program
declares; **any other opcode is an explicit fault, never a silent pass** —
a criterion the verifier cannot replay is not a criterion the verifier has
confirmed.

```text
COMPARE(x,y,mask)   §2.2: canonicalize only the predeclared process-local fields
                    in `mask`, then require byte equality of all else.
DAG(G,P)            §2.2 + the V009-06 row: the SINGLE-AUTHORITY form only. `P`
                    must be the spec-fixed sentinel; the comparison clause is
                    discharged by the principal ruling's identity and this
                    function NEVER synthesizes COMPARE(X,X), which the row
                    expressly forbids.
```

### 2.2 [PROVABLE] The registrar's hypothesis, refuted at the row text

The row's first assignment is:

```text
r_ground := COMPARE(P0.evidence_files[stage_dependencies_member].sha256,
                    STAGE_DEPENDENCIES_MEMBER_SHA256, empty)
```

Both operands are **digests**. The raw span's *bytes* are never converted to a
value by `r_ground`; only its *digest* is compared, against a constant written
into the row itself. **The row text requires no wrap/strip recipe at all**, so
there is no recipe on which the two lanes could differ. Computed:

```text
member payload                      932 bytes
P0.evidence_files[member].sha256    47e7c32915bc756f…      (hashed by me)
STAGE_DEPENDENCIES_MEMBER_SHA256    47e7c32915bc756f…      (spec-fixed, in the row)
COMPARE(left, right, empty)      -> {'success': True, 'equal': True}
NEGATIVE control, one byte added -> {'success': False, 'equal': False}
```

### 2.3 [PROVABLE] The undetermined half: `P0` is a SPEC GAP

§2.1 defines P0 exactly, and §3 makes it universal — *"Every criterion is
implicitly conjoined with `P0`."* So its **content** is determined:

```text
P0 := strict_parse(BASE)
   and every_declared_sha256_matches_the_supplied_bytes
   and content_root(subject_files)=subject_manifest.declared_root
   and content_root(evidence_files)=evidence_manifest.declared_root
   and no_duplicate_path_or_key
   and every_required_input_present.
```

What is **not** determined is how R9 replays it. Two of the six conjuncts
quantify over the **subject manifest** and the **evidence manifest**, and R9's
launch argv is

```text
--spec  --ledger  --ledger-sha256  --evidence-dir  --runtime-snapshot  --runtime-gate
```

— neither manifest is supplied. I checked both alternatives and both are closed:
the evidence *directory* is not the evidence *manifest*, and no subject manifest
reaches the verifier by any argument.

**What the spec must state**, precisely, for this to be replayable:

1. **Who evaluates `P0` for R9's replay.** If the producer, then P0 is a
   producer-declared object carrying a criterion's direction and BR-1 forbids
   reading it — so the spec must say what makes that lawful, or say R9 computes it.
2. **If R9 computes it: which inputs.** The subject and evidence manifests must
   be added to R9's launch contract (a `--subject-manifest` / `--evidence-manifest`
   pair, each with its own digest, matching the `--ledger` / `--ledger-sha256`
   pattern already in argv), or §2.1 must state which conjuncts R9 is exempt from
   and why.
3. **What R9 records when a conjunct is unevaluable** — the closed status alphabet
   has no value for "precondition not replayable", and `FAIL` would misreport it
   as a criterion failure, which is exactly the defect §1 displays.

**I do not guess.** Until the spec states it, the atom faults explicitly:

```text
P0 is not replayable by this verifier: spec §2.1 defines it over
content_root(subject_files)=subject_manifest.declared_root and
content_root(evidence_files)=evidence_manifest.declared_root, and R9 is
launched with neither manifest. SPEC GAP -- the row or §9.4 must state
P0's replay carrier for R9
```

That is a change of kind, not merely of message. The old code returned **False**
— a criterion *failure* — for an atom it had never evaluated. **A verdict of FAIL
that was never evaluated is not a verdict.** It now fails closed *and says why*,
which is the difference between a refusal and a mistake. My replay's refusal
stands as lawful, per G2's own terms.

A second guard was added in the same place: if a producer *does* emit a `P0`
result object, that is now a **fault**, not an input. A producer-declared object
may not carry a criterion's direction.

### 2.4 [PROVABLE] A defect in my own fix, caught by the demonstration

My first `opcode_compare` read:

```python
left, right = dict(args["left"]), dict(args["right"]) \
    if isinstance(...) and isinstance(...) else (args["left"], args["right"])
```

The conditional binds to `right` alone, so `left = dict(args["left"])` runs
unconditionally and raises `ValueError` on the scalar digests `r_ground` actually
compares. **The opcode I wrote to fix the disagreement would have crashed on the
one invocation it exists to compute.** Rewritten with the branch around the whole
assignment; positive and negative controls in §2.2 and §4 are run against the
repaired version.

Second relay running in which the demonstration caught a defect in my own fix.
The pattern is now explicit: **write it, then run it against the real object, not
the one you had in mind.**

## 3. [PROVABLE] A CONTRACT OF MINE BELOW THE SPEC — found while adjudicating

V007 §9.4 specifies the row's `invocation` with **seven** fields:

```text
{opcode, result_name, args, instance_id, source_sha256, span:[start,end], span_sha256}
```

> "This is the byte-span linkage required for independent replay; the
> blocker-ledger `source.byte_span` and a digest without the source slice are not
> substitutes for it."

My contract declared **four** — from my own 686 write-out, which the spec has
superseded — and A emitted four. **Both builders were below the sealed spec, and
mine was the contract that should have caught it.** The spec wins: the inventory
is now seven, and the three linkage fields are **cross-checked against the
`instance_id`** rather than merely present — `span` must equal the parsed span,
`source_sha256` must equal the parsed source, both digests must be lowercase
sha256, and a null `instance_id` requires all three to be null.

This produces a **new refusal** the registrar must route to A:

```text
checks[16].invocation[0]: field inventory mismatch
  (missing=['source_sha256', 'span', 'span_sha256'] undeclared=[])
```

That refusal is the spec being enforced, not a preference of mine. Supplied with
the seven fields, the same row is accepted (§4).

## 4. G3 — WHOSE COMPUTATION MATCHED THE SEALED TEXT

**On the one atom that is replayable, the two builders agree.** Recomputed by me
from evidence bytes, never read from A's output:

```text
r_dag  RECOMPUTED  {'success': True, 'nodes': 11,
                    'roots': ['SPEC-SEAL'], 'sinks': ['FINAL-CLAIM-SEAL']}
       topological order covers 11/11; no cycle, no self-parenting, no missing
       parent, no duplicate parent
producer status                                    PASS
```

Negative controls, so the agreement is not an artifact of a permissive check:

```text
DAG cycle {"A":["B"],"B":["A"]}   -> success False, "cycle: 0 of 2 nodes ordered"
DAG self-parenting {"A":["A"]}    -> success False, "self-parenting at 'A'"
DAG missing parent {"A":["Z"]}    -> success False, "missing parents ['Z'] at 'A'"
DAG non-sentinel authority        -> REFUSED (the two-object form is not implemented)
COMPARE mask on scalar operands   -> REFUSED
unimplemented opcode (KERNEL)     -> REFUSED, never a silent pass
```

**So the resolution is: neither side's computation matched the sealed text, and
the graph was never in dispute.** A declared PASS from its own evaluation of a
predicate the spec requires *R9* to replay. I declared FAIL from an atom I never
evaluated. Corrected, my recomputation **confirms A on `r_dag`**, would confirm A
on `r_ground` (§2.2), and **cannot reach a verdict on `P0`** — which is the spec's
gap, not either builder's error.

Run 030's row through the post-693 verifier:

```text
contract   REFUSED  -- 4 invocation fields, spec §9.4 requires 7   (§3)
with the 7 fields supplied:
  contract ACCEPTED -- linkage agrees with instance_id
  roles    consumable=1  raw=1  faults=[]
  replay   FAULT, not FAIL: "P0 is not replayable … SPEC GAP"
  r_dag    recomputed True
```

The difference between the old behaviour and the new is the difference between
`REPLAY_DISAGREE` — which accuses the producer — and a named spec gap, which
accuses nobody and routes to the principal.

## 5. DELTA AND PIN CHECK

```text
CHANGED  verifier/replay.py     +IMPLEMENTED_OPCODES, +opcode_compare, +opcode_dag,
                                +recompute_results; the P0 atom now FAULTS with the
                                gap named and refuses a producer-declared P0 object
CHANGED  verifier/verify.py     the check-row bundle is built from RECOMPUTED
                                results, not from a producer payload
CHANGED  verifier/contracts.py  INVOCATION_FIELDS 4 -> 7 per §9.4, with the linkage
                                fields cross-checked against instance_id
CHANGED  selfcheck/selfcheck.py +15 permanent assertions
CHANGED  rd22.verifier-manifest.v001.json   433d208e… -> b987ee4818103a124544f56f98
                                8990a1eee470e19d976ea59f8f60254d7bd4c7
CHANGED  rd22.verifier-manifest.v001.json.seal.sha256   regenerated, verified OK

verifier_root_sha256  e3abd168…  ->  fd59672a588e1a62c18dea7ff70dc06945b4e3bbf98ef03
                                     7ce9dd803730aff6f
UNCHANGED  root MEMBERSHIP (12); run_verifier.py; spec_census; both contracts files;
           all five input roots -- spec d38d3171…, evidence fcaa97a0…, ledger sentinel
```

| Claim | Verified before sealing |
|---|---|
| the failing step is atom `P0` | reproduced on run-030 bytes; short-circuit displayed |
| `r_ground` never reached | atom order displayed; bundle keys displayed |
| no wrap/strip recipe in the row | both `r_ground` operands are digests, quoted from the sealed row |
| R9 replays from evidence bytes | quoted from V007's R9 duty list |
| opcodes recomputed, not read | the bundle is `encode_canonical(recompute_results(...))` |
| COMPARE and DAG correct | positive **and** five negative controls |
| unimplemented opcode faults | `KERNEL` refused |
| P0 faults with the gap named | asserted permanently, including the "SPEC GAP" text |
| producer-declared P0 refused | asserted |
| §9.4 seven fields, cross-checked | 7 cases: 2 accept, 5 refuse |
| root recomputed, membership 12 | `fd59672a…`; equals the instance field |
| instance canonical, sidecar OK | `b987ee48…` == `manifest_sha256()`; single line; 11 fields |
| input roots untouched | spec, evidence, ledger sentinel, snapshot, gate all unchanged |
| self-check CLEAN, 19 files, 0 asserts | executed |
| dry run both cwds; stdout canon | exit 2; 372 B; `0x7d`; `rstrip() == raw`; stderr 0 |

### 5.1 What is NOT fixed, and why

`P0` is not fixed because the spec does not determine it and **guessing a
precondition's replay carrier is exactly the fabrication BR-1 exists to prevent.**
§2.3 states what the spec must say. Until it says it, C-B-V009-06 cannot be
replayed to a verdict by R9, and my refusal is lawful rather than obstructive.

I also did not implement the other twelve opcodes. No row with evidence exercises
them, and an unimplemented opcode now faults explicitly rather than passing
silently, so the gap is visible rather than latent.

### 5.2 `F_PLDEC` and coverage

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. **The chain was not invoked**: the diagnosis reads
mirrored run-030 artifacts and calls pure functions on them; the launch
demonstration is the dry run, which opens no run input. `alpha_computed = false`;
`proof_authorized = false`; `kappa_record_computed = false`; no member bound; no
fixed point; no end test; no numeric evaluation; no comparison to any measured
constant.

**Coverage, stated exactly.** I diagnosed one disagreement, removed a BR-1
violation from my own replay, implemented two opcodes, and raised a contract to
the spec. I claim **no check or fixture outcome**. `r_dag = success:true` is *my
recomputation of one atom*, not a row verdict — the row cannot reach a verdict
while `P0` is unreplayable. **I do not claim run 031 passes**; it will meet the
§3 refusal first, and that is the correct next fault.

## 6. SELF VERB AUDIT

| My verb | Check |
|---|---|
| Hypothesis refuted, not deferred to | The registrar proposed an `r_ground` recipe difference; the replay never reaches `r_ground` and the row's `r_ground` compares two digests. Both shown from bytes and sealed text. |
| **BR-1 violation found in my own code** | My replay read `.success` off a producer-emitted object — the exact law I have enforced against Builder A for twenty relays. Named as mine. |
| Both G2 branches used where each applies | Determined for `r_ground`/`r_dag` → fixed. Undetermined for `P0` → gap stated, not guessed. |
| The gap is actionable | Three specific things the spec must state, including the argv change. |
| **Defect in my own fix disclosed** | `opcode_compare`'s conditional bound to one operand; it would have crashed on the scalars `r_ground` compares. Caught by running it. |
| Negative controls throughout | Cycle, self-parenting, missing parent, non-sentinel authority, masked scalars, unimplemented opcode. Agreement on a check that cannot fail is worthless. |
| Contract raised to the spec | My 4-field inventory was below §9.4's 7, and mine was the contract that should have caught it. The new refusal is disclosed as A's to clear. |
| No claim on run 031 | The next fault is named and is the contract refusal. |
| `CHAIN_INVOKED = false` | Literally true. |

---

```text
FAILING_STEP = (named, displayed) atom `P0`, the FIRST of the criterion's three
  atoms, in replay_atom: `return bundle.success("P0") if "P0" in bundle.results
  else False`. Reproduced on run-030's own bytes: both payloads digest-verify,
  classification is clean (CONSUMABLE 594 B canonical 11-node graph; RAW 932 B
  linkage=digest+span; zero faults), and the EvidenceBundle is built from the GRAPH
  payload, whose keys are seal names -- 'P0', 'r_ground' and 'r_dag' are all absent.
  The predicate SHORT-CIRCUITS at the first atom and returns False, so r_ground and
  r_dag are NEVER EVALUATED. THE REGISTRAR'S CANDIDATE ROOT CAUSE IS REFUTED TWICE:
  my replay never reaches r_ground, and the sealed row's r_ground is
  COMPARE(P0.evidence_files[member].sha256, STAGE_DEPENDENCIES_MEMBER_SHA256, empty)
  -- BOTH OPERANDS ARE DIGESTS, so the raw span's bytes are never converted to a
  value and no wrap/strip recipe exists on which the two lanes could differ.)
SPEC_DETERMINES = yes for r_ground/r_dag (fixed to spec) / no for P0 (gap stated)
  (DETERMINED: V007 state R9 requires the verifier to "replay each pass predicate
  FROM EVIDENCE BYTES". My replay read .success off a PRODUCER-EMITTED bundle --
  a producer-declared object carrying a criterion's direction, BR-1, the law this
  lane has enforced against Builder A for twenty relays, violated inside Builder B's
  own verifier. Fixed: recompute_results() derives each recorded invocation's result
  from its arguments and the predicate replays against THOSE. COMPARE and DAG are
  implemented -- exactly the two opcodes this row's program declares, with the DAG
  single-authority form only, which never synthesizes the COMPARE(X,X) the row
  forbids -- and any other opcode is an EXPLICIT FAULT, never a silent pass.
  UNDETERMINED: §2.1 fixes P0's CONTENT as six conjuncts and §3 makes it universal,
  but two conjuncts quantify over the SUBJECT and EVIDENCE MANIFESTS and R9's launch
  argv supplies neither; I checked both alternatives and both are closed. The spec
  must state (1) who evaluates P0 for R9's replay, since if the producer does then
  BR-1 forbids reading it; (2) if R9 computes it, which inputs -- a
  --subject-manifest/--evidence-manifest pair matching the existing
  --ledger/--ledger-sha256 pattern, or an explicit exemption; (3) what R9 records
  when a conjunct is unevaluable, since the closed status alphabet has no value for
  it and FAIL misreports a precondition as a criterion failure. I DO NOT GUESS: the
  atom now FAULTS with the gap named, and a producer-emitted P0 object is refused as
  a BR-1 violation. The old code returned FALSE for an atom it never evaluated, and
  A VERDICT OF FAIL THAT WAS NEVER EVALUATED IS NOT A VERDICT.)
VERDICT_FOLLOWS = the spec (ON THE ONE REPLAYABLE ATOM THE TWO BUILDERS AGREE:
  r_dag recomputed BY ME from evidence bytes gives success=True, 11 nodes, single
  root SPEC-SEAL, single sink FINAL-CLAIM-SEAL, topological order covering 11/11 --
  and the producer says PASS. Five negative controls prove the agreement is not an
  artifact of a permissive check: cycle, self-parenting, missing parent,
  non-sentinel authority and masked scalar operands are all refused, as is an
  unimplemented opcode. r_ground would likewise agree -- the member payload hashes
  to 47e7c329… and the row's spec-fixed constant IS 47e7c329…, so COMPARE returns
  success True, with a one-byte negative control returning False. THE GRAPH WAS
  NEVER IN DISPUTE. Neither side's computation matched the sealed text: A declared
  PASS from its own evaluation of a predicate the spec requires R9 to replay, and I
  declared FAIL from an atom I never evaluated. The row still cannot reach a verdict,
  but the reason is now a named SPEC GAP that accuses nobody and routes to the
  principal, rather than a REPLAY_DISAGREE that accused the producer.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. The diagnosis
  reads the mirrored run-030 artifacts and calls pure functions on them; the launch
  demonstration is the dry run, which opens no run input. NO OUTCOME IS CLAIMED:
  r_dag success=True is MY RECOMPUTATION OF ONE ATOM, not a row verdict, and the row
  cannot reach a verdict while P0 is unreplayable. I do NOT claim run 031 passes --
  it will meet the §3 contract refusal first, and that is the correct next fault.)
VERB_AUDIT_SELF = CLEAN (+1 BR-1 VIOLATION FOUND IN MY OWN REPLAY, §2.1, named as
  mine rather than as a design choice: reading a criterion's direction off a
  producer-emitted result object is precisely what I have refused Builder A twenty
  times, and hash-pinning the bundle prevents substitution, not fabrication. +1
  DEFECT IN MY OWN FIX caught by running it, §2.4: opcode_compare's conditional bound
  to one operand, so dict() ran unconditionally and the opcode written to resolve the
  disagreement would have CRASHED on the scalar digests r_ground actually compares --
  second relay running in which the demonstration, not the reading, caught the defect.
  +1 CONTRACT OF MINE BELOW THE SPEC, §3: V007 §9.4 specifies SEVEN invocation fields
  and my inventory declared FOUR, carried over from my own superseded 686 write-out;
  Builder A emitted four too, so both builders were below the sealed text and mine was
  the contract that should have caught it. Now seven, with the linkage fields
  CROSS-CHECKED against the instance_id rather than merely present. The resulting
  refusal of A's four-field emission is disclosed as a new fault the registrar must
  route -- it is the spec being enforced, not a preference of mine.)
```

The disagreement looked like two lanes computing one value differently. It was two
lanes each answering a question the spec had not asked them: A evaluated a
predicate the spec assigns to R9, and R9 returned a verdict on an atom it had never
evaluated. The graph both lanes actually computed was the same graph all along.
