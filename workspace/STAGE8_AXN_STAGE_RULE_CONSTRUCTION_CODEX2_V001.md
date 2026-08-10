CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = CLAIMED
CLOSURE_BEGIN_BYTE = 00000000
PREDECLARATION_OUTPUT_SCAN = 0 hits for this artifact and its sidecar
VERDICT_BEARING_SET = exactly the 10 content-addressed members below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
FINDER_BUILDS = true
OPPOSITE_LANE_MUST_VERIFY = true
```

| # | Closed member | SHA-256 / bounded span SHA-256 | Role |
|---:|---|---|---|
| 01 | `PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | state pin |
| 02 | `LOCKED_PROCESS.md` | `38149496a2b5d89d20b614d972bffef1867d7cde573b26d77dfb207ece3446fb` | process, claim-status, and correction law |
| 03 | `DECLINE_REGISTER_V002.md` | `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | S01–S37 flattening guard |
| 04 | `relay_inbox/RELAY_PASTE_933_STAGE_RULE_CONSTRUCTION_CODEX2_V001.md` | `0aaadfeee79ae09e289f53ecbd78f0bcf86b705d0683f07e3b0c026527653a96` | assignment |
| 05 | `STAGE8_AXN_CONSTRUCTIONS_CROSSCHECK_CODEX2_V001.md` | `0ca75a7d57476f5134a58eae7dd6e4177b1c4bfaf498c794f1c4aae3e3f5acb3` | finder result and correction boundary |
| 06 | `STAGE8_TASK2F_C0_008_FINITE_COMPLEX_RESTRICTION_PACKAGE_BUILD_AND_ARM_EXECUTION_ATTEMPT_V001.md`, `[7090,8455)` | whole file `5515517ca2d1b48dd439fe97f2972292620132605767c4dd5de1007f67152c5a`; span `55e9c77341bc22c4f11a5a6923fc65ed5c3553d1835a703855cad8baa8181597` | ratified `F_cyl(C0_008)` stage objects and TYPE-P family status |
| 07 | `STAGE8_CTP_PHYS_INPUT_PACKAGE_C0_DOR008_ASSEMBLY_AND_FIRST_RESTRICTION_TEST_V001.md`, `[5412,5787)` | whole file `1467ab9850022931e68dc9ffa625d95099d8f6bb74d734dc9d0466f169bd00b6`; span `fcc34fa4e2885f30278240c4c2e8c3348836def5c75500b87b55eed58afdf5a2` | record maps, label zero-extension, full field/CTP algebra, and `A_C0` target |
| 08 | `JOINT_ANCHOR_DECISION_INSTANCE_V002.md` | `72191e0115d6f36d2327236e7a6d16e21f953422ba3fb2188b75e3db009cea99` | current open receiver and blind fiber status |
| 09 | `STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V002.md`, field `[9946,10026)`, suite `[22341,23332)` | whole file `58b966ed371b23b29b9e3ceed280eb30c804484becb2b17ca6ea465668e951bc`; field `5face4888aafecaebdb93e0f59b94a1637c22f05428e835c679996551ac3a9e1`; suite `ccbdeed389ebd45603ef49e6e6858d2ac0ad5ec96cfa5c458e1d7e03c017d450` | exact stage receiver and JAC-14 format |
| 10 | `QUESTIONS_SETTLED_REGISTER_V001.md#Q-246`, `[614648,616505)`, and `#Q-839`, `[1712305,1714590)` | `1e9d487a697dc8b7b3f446878b95f07e942891dcfe6461d76b44a5fd1ae861ea`; `ca52a471434e9e0b7452aa440bd385447c26f4743030293e1d00e9181e493233` | living-file pins: sequential analogues TYPE-P and stage stop overturned |

CLOSURE_DECLARATION_END

# STAGE 8 — AXN STAGE-RULE CONSTRUCTION AND CERTIFICATE RE-SCOPE — V001
## CODEX 2 LANE — RELAY 933 — `[PLAN:AXN-BUILD-C32]` — [CLAIMED]

Date: 2026-08-10  
Status: **CONSTRUCTION CLAIMED — OPPOSITE-LANE CHECK REQUIRED**.  
Scope: derive `stage_index_and_limit_rule` from the ratified sequential-cylinder family and emit all
fiber-independent structural restriction/limit receipts that can be replayed without selecting a
stage cutoff, a candidate, a superselection extension, or an A0 fiber.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. Exact receiver and zero-freedom source [CLAIMED]

Member 09 demands, at exact bytes `[9946,10026)`:

```text
stage_index_and_limit_rule: exact finite/cylindrical system and limit target,
```

Member 06 then supplies, for every ratified sequential stage `N>=1`,

```text
Lambda_N = Z^N,
A_F,N = C*(Z^N),
B_N = A_F,N,+ tensor_min (A_F,N,-)^op,
R_N = tensor_(j=1)^N M_3(C),
A_SR,N = A_src graded-tensor_min R_N,
A_C0,N = A_SR,N graded-tensor_min B_N.
```

It names the exact family `F_cyl(C0_008)`, says every member is supplied by the same ratified
formulas and exact zero-extension system, and records
`F_CYL_IS_INSTANTIATED_STRUCTURAL_FAMILY = true | TYPE-P | premises: DoR-008`.

Member 07 supplies the connecting data and target:

```text
iota_NM(A) = A tensor I_(M-N),                         N<=M,
j_NM^Lambda(n_1,...,n_N) = (n_1,...,n_N,0,...,0),
Lambda = direct-sum_(j>=1) Z e_j,
A_F = C*(Lambda),
A_F_CTP = A_F,+ tensor_min (A_F,-)^op,
A_C0 = A_SR graded-tensor_min A_F_CTP.
```

No finite-complex object map appears in this rule. No `N` is selected from vertices, edges, or any
other downstream complex.

## 2. Constructed stage rule [CLAIMED]

### 2.1 Derived maps [CLAIMED]

Write `alpha_NM` for the injective star-homomorphism induced functorially by
`j_NM^Lambda` on `A_F,N`, and

```text
beta_NM := alpha_NM,+ tensor_min (alpha_NM,-)^op : B_N -> B_M.
```

This is notation for the sealed zero-extension, not a choice. The joint connecting map is forced:

```text
J_NM := id_A_src graded-tensor iota_NM graded-tensor beta_NM
       : A_C0,N -> A_C0,M.
```

For `N<=M<=L`, appending zeros twice appends exactly the same zeros as the direct `N->L` map;
tensoring identities twice gives `I_(M-N) tensor I_(L-M)=I_(L-N)`. Functoriality of the group
C-star construction, opposite algebra, and minimal tensor product therefore gives

```text
J_ML compose J_NM = J_NL,
J_NN = id_A_C0,N.
```

Each map is injective, unital, and star-preserving. The target maps into the full direct-limit
labels, `R_inf`, and hence the entered
`A_C0=A_src graded-tensor_min R_inf graded-tensor_min A_F_CTP`. The canonical maps `J_N,infinity`
satisfy

```text
J_M,infinity compose J_NM = J_N,infinity.
```

### 2.2 Canonical field bytes [CLAIMED]

The constructed field value is the following single UTF-8 line, with no terminal linefeed included
in its content digest:

```text
STAGE-RULE|v=001|index=positive-integers-N>=1-with-unique-arrow-N-to-M-iff-N<=M|stage=A_C0,N=(A_src-graded-tensor-min-R_N)-graded-tensor-min-B_N|record-map=iota_NM(A)=A-tensor-I_(M-N)|label-map=j_NM^Lambda(n_1,...,n_N)=(n_1,...,n_N,0,...,0)|field-map=alpha_NM=Cstar(j_NM^Lambda)|ctp-map=beta_NM=alpha_NM,+-tensor-min-(alpha_NM,-)^op|joint-map=J_NM=id_A_src-graded-tensor-iota_NM-graded-tensor-beta_NM|coherence=J_ML-compose-J_NM=J_NL-and-J_NN=id|limit=A_C0=A_src-graded-tensor-min-R_inf-graded-tensor-min-A_F_CTP|limit-square=J_M,infinity-compose-J_NM=J_N,infinity|sources=5515517ca2d1b48dd439fe97f2972292620132605767c4dd5de1007f67152c5a:[7090,8455)#55e9c77341bc22c4f11a5a6923fc65ed5c3553d1835a703855cad8baa8181597;1467ab9850022931e68dc9ffa625d95099d8f6bb74d734dc9d0466f169bd00b6:[5412,5787)#fcc34fa4e2885f30278240c4c2e8c3348836def5c75500b87b55eed58afdf5a2
```

```text
STAGE_RULE_PAYLOAD_SHA256 = 986cc0585d7513aed30151db4bd5aeb774104ab27bbcd4b640f1a8e1615800d4
```

### 2.3 The fixed source leg [CLAIMED]

At this receiver `A_src` is the same sealed factor at every `N`; the stage maps act on it by
`id_A_src`. Therefore the system does not ask for finite-rank subspaces of a continuum source
operator, convergence of compressed source generators, or a source propagator approximation. The
absent source-Galerkin chain remains a real absence at its own analytic receiver but is not an input
to this cylindrical carrier system. Requiring it here would replace member 06's explicit
`A_SR,N=A_src tensor R_N` with a different, unratified family.

```text
SOURCE_LEG_AT_STAGE_N = fixed A_src
SOURCE_CONNECTING_MAP = id_A_src
SOURCE_GALERKIN_DATUM_CONSUMED = none
```

## 3. JAC-14 restriction/limit receipt convention [CLAIMED]

Member 09 requires exact replay objects, canonical bytes, closed fields, and no extras. It does not
give a sub-schema for each entry of `restriction_and_limit_square_receipts`. The serialization below
therefore uses one closed administrative tuple, disclosed rather than hidden:

```text
JAC14-RL-RECEIPT|v=001|id|quantifier|inputs|procedure|accept
```

Each payload is the exact single UTF-8 line between its fence markers, excluding its terminal
linefeed. The convention adds no carrier, map, stage, cutoff, fiber, candidate, or physical datum;
it serializes only consequences of members 06 and 07. Each `procedure` is symbolic and terminates
for the displayed quantified variables.

## 4. Fiber-independent exact-replay receipts [CLAIMED]

### RL-01 — stage-object typing [CLAIMED]

```text
JAC14-RL-RECEIPT|v=001|id=RL-01-STAGE-OBJECTS|quantifier=all-N>=1|inputs=F-CYL@5515517ca2d1b48dd439fe97f2972292620132605767c4dd5de1007f67152c5a:[7090,8455)#55e9c77341bc22c4f11a5a6923fc65ed5c3553d1835a703855cad8baa8181597|procedure=parse-R_N,B_N,A_SR,N,A_C0,N-and-typecheck-each-tensor-factor|accept=A_C0,N-is-typed-for-every-N
```

### RL-02 — record-map coherence [CLAIMED]

```text
JAC14-RL-RECEIPT|v=001|id=RL-02-RECORD-COHERENCE|quantifier=all-1<=N<=M<=L|inputs=SEQUENTIAL-TARGET@1467ab9850022931e68dc9ffa625d95099d8f6bb74d734dc9d0466f169bd00b6:[5412,5787)#fcc34fa4e2885f30278240c4c2e8c3348836def5c75500b87b55eed58afdf5a2|procedure=expand-iota_ML(iota_NM(A))-and-contract-I_(M-N)-tensor-I_(L-M)-to-I_(L-N)|accept=iota_ML-compose-iota_NM=iota_NL-and-iota_NN=id
```

### RL-03 — label zero-extension coherence [CLAIMED]

```text
JAC14-RL-RECEIPT|v=001|id=RL-03-LABEL-COHERENCE|quantifier=all-1<=N<=M<=L|inputs=SEQUENTIAL-TARGET@1467ab9850022931e68dc9ffa625d95099d8f6bb74d734dc9d0466f169bd00b6:[5412,5787)#fcc34fa4e2885f30278240c4c2e8c3348836def5c75500b87b55eed58afdf5a2|procedure=append-M-N-zeros-then-L-M-zeros-and-compare-with-appending-L-N-zeros|accept=j_ML^Lambda-compose-j_NM^Lambda=j_NL^Lambda-and-j_NN^Lambda=id
```

### RL-04 — field/CTP functoriality [CLAIMED]

```text
JAC14-RL-RECEIPT|v=001|id=RL-04-FIELD-CTP-COHERENCE|quantifier=all-1<=N<=M<=L|inputs=RL-03;F-CYL@5515517ca2d1b48dd439fe97f2972292620132605767c4dd5de1007f67152c5a:[7090,8455)#55e9c77341bc22c4f11a5a6923fc65ed5c3553d1835a703855cad8baa8181597|procedure=apply-group-Cstar-functor-then-plus-minus-opposite-and-minimal-tensor-functors-to-RL-03|accept=alpha_ML-compose-alpha_NM=alpha_NL-and-beta_ML-compose-beta_NM=beta_NL
```

### RL-05 — joint-carrier coherence [CLAIMED]

```text
JAC14-RL-RECEIPT|v=001|id=RL-05-JOINT-COHERENCE|quantifier=all-1<=N<=M<=L|inputs=RL-02;RL-04;F-CYL@5515517ca2d1b48dd439fe97f2972292620132605767c4dd5de1007f67152c5a:[7090,8455)#55e9c77341bc22c4f11a5a6923fc65ed5c3553d1835a703855cad8baa8181597|procedure=tensor-id_A_src-with-record-and-CTP-coherence-equalities|accept=J_ML-compose-J_NM=J_NL-and-J_NN=id_A_C0,N
```

### RL-06 — unit preservation [CLAIMED]

```text
JAC14-RL-RECEIPT|v=001|id=RL-06-UNIT-PRESERVATION|quantifier=all-1<=N<=M|inputs=RL-02;RL-04;RL-05|procedure=apply-J_NM-to-1_A_src-tensor-1_R_N-tensor-1_B_N-and-rewrite-each-unital-factor-map|accept=J_NM(I_C0,N)=I_C0,M
```

### RL-07 — limit-square compatibility [CLAIMED]

```text
JAC14-RL-RECEIPT|v=001|id=RL-07-LIMIT-SQUARE|quantifier=all-1<=N<=M|inputs=RL-05;SEQUENTIAL-TARGET@1467ab9850022931e68dc9ffa625d95099d8f6bb74d734dc9d0466f169bd00b6:[5412,5787)#fcc34fa4e2885f30278240c4c2e8c3348836def5c75500b87b55eed58afdf5a2|procedure=embed-record-and-label-zero-extensions-into-R_inf-and-direct-sum-Lambda-then-tensor-id_A_src|accept=J_M,infinity-compose-J_NM=J_N,infinity-with-target-A_C0
```

### 4.1 Receipt digest ledger [CLAIMED]

| Receipt | Payload SHA-256 |
|---|---|
| `RL-01` | `9c8a59013b4fca4f50dbe6371326532b5b1757a785ebf31a32df18dcb46f6913` |
| `RL-02` | `da32d82e0790391df7de262cab00df2c0a32e1008ca37227824ae083f1b85aaf` |
| `RL-03` | `295c8410b1d919a2cbb7c2d13a5896e6a36c76be4e37073ee72e149d81b717cd` |
| `RL-04` | `93d96b38d4f0e36ab8baab7e8d69b654abe6797005bafaaa02fa533c5631d8af` |
| `RL-05` | `eff9ea75626eb283d7d3919329cc6890211d137ec747c1bc2813a6b4c5acc79f` |
| `RL-06` | `7ff201e3adf8d1aa5d2a063420a13fd7ff01d507731e8f7562ae5d5d2958ca71` |
| `RL-07` | `a8b31caed51ede08e28db17551b4ce44a4972f8c8b2dc9a4506ee28cb5b8d52e` |

The exact ordered list carrier is:

```text
JAC14-RL-LIST|v=001|count=7|items=RL-01:9c8a59013b4fca4f50dbe6371326532b5b1757a785ebf31a32df18dcb46f6913;RL-02:da32d82e0790391df7de262cab00df2c0a32e1008ca37227824ae083f1b85aaf;RL-03:295c8410b1d919a2cbb7c2d13a5896e6a36c76be4e37073ee72e149d81b717cd;RL-04:93d96b38d4f0e36ab8baab7e8d69b654abe6797005bafaaa02fa533c5631d8af;RL-05:eff9ea75626eb283d7d3919329cc6890211d137ec747c1bc2813a6b4c5acc79f;RL-06:7ff201e3adf8d1aa5d2a063420a13fd7ff01d507731e8f7562ae5d5d2958ca71;RL-07:a8b31caed51ede08e28db17551b4ce44a4972f8c8b2dc9a4506ee28cb5b8d52e
```

```text
RESTRICTION_LIMIT_LIST_SHA256 = 20f12ff18ce33785f5bbb7b100f68d39d2345b26aa655b4f46caac73698e8f5a
```

These seven receipts are exact structural material for the suite's
`restriction_and_limit_square_receipts` field. They do not claim to instantiate the entire
`JointAnchorCertificateSuite.v001`.

## 5. Exact stop boundary and fiber-gated remainder [CLAIMED]

### 5.1 What the stage construction unlocks [CLAIMED]

The prior “no stage set” gate is gone. `RL-01` through `RL-07` cover the algebraic stage objects,
record/label/field/CTP/joint connecting maps, units, and the limit square for all `F_cyl` stages.
No A0 fiber datum appears in any receipt.

### 5.2 What cannot be produced without a choice or missing carrier [CLAIMED]

The full JAC-14 suite is not produced. Its remaining non-fiber gates are:

1. `finite_stage_inventory` is specified by member 09 as an **exhaustive ordered
   content-addressed list**, while `F_cyl` has the infinite index set `N>=1`. The seven universal
   receipts certify the grammar but do not turn that infinite family into a finite list. Choosing a
   cutoff would consume a new freedom. No cutoff is chosen.
2. `delta0_basis`, `phi_restriction_matrix`, factorization/inverse, CPTP, charge covariance,
   superselection commutation, fixed-space/mixing, and anchor certificates require the exact entered
   `Phi_joint`, `E_joint`, and tag/candidate data. The current instance does not supply those objects.
   They are not consequences of the stage rule.
3. `replay_entry_point_sha256`, `suite_sha256`, and the frozen pre-output receipt are downstream of
   the complete suite bytes; they cannot be computed over a partial suite.

These gates are named to prevent the fiber from being misreported as the only missing input to the
entire suite.

### 5.3 Fiber-only item [CLAIMED]

Exactly one current suite element is gated on the blind fiber entry and on nothing else:

```text
FGR-01 = JointAnchorCertificateSuite.v001.a0_rank_fiber_sha256
entry method = copy the verified opaque A0RankFiber.v001 object digest into the closed suite field
rank read = forbidden
ratio = forbidden
fiber comparison = forbidden
```

Once the principal enters that opaque object, `FGR-01` is a mechanical digest binding. It does not
by itself remove the three non-fiber gates in §5.2. No other suite element is honestly classifiable
as fiber-only in the current partial instance.

## 6. FREEDOMS-CONSUMED [CLAIMED]

```text
JOINT_ANCHOR_INPUT = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  the exact F_cyl stage objects;
  iota_NM, label zero-extension, and their full limit targets;
  the stage-field receiver and closed JAC-14 suite schema;
  the current instance's opaque, incomplete fiber receiver.

CONDITIONED-ON:
  standard functoriality of group C-star algebras, opposite algebras, and minimal tensor products;
  universal receipts applying only to the ratified sequential/cylindrical category N<=M.

SUBSTITUTED:
  NOTHING. No finite cutoff, complex-to-stage map, candidate, E_joint, tag, fiber, rank datum,
  certificate matrix, replay program, or suite hash was selected or invented.

SCALING WEIGHTS: NONE CONSUMED; NONE FIXED; NONE SUBSTITUTED.
```

## 7. Flattening, batteries, custody, and byte audit [CLAIMED]

- **S01–S37 FLATTENING CHECK:** walked. A constant source leg was not identified with a missing
  Galerkin approximation. Universal structural receipts were not identified with a finite ordered
  stage inventory. Stage coherence was not identified with candidate dynamics. An opaque fiber
  digest was not identified with rank content or with completion of the whole suite.
- **F_PLDEC:** symbolic stage maps and exact content digests only; no physical quantity was
  numerically evaluated and no measured constant was consulted.
- **M-2 / four modes:** exact-name, normalized-name, fixed-string, and byte-span/semantic-receiver
  checks covered `F_cyl`, `A_C0,N`, `iota_NM`, label zero-extension, induced field/CTP maps,
  `finite_stage_inventory`, every JAC-14 field, and the blind fiber receiver.
- **BLIND:** the fiber remains an opaque pointer. No rank or dimension was read, no ratio formed or
  quoted, and no fiber compared.
- **PE-1..PE-13:** pointer-only and zero verdict weight.
- **BUILDER-NEVER-VERIFIES:** this construction is CLAIMED. Member 05 found the route; the opposite
  lane must check the constructed map formulas, receipt hashes, completeness boundary, and gates.
- **PIN CHECK:** every named subject and available sidecar verified before reading; both register
  entries were rehashed at their exact live-file spans.
- **CHAIN:** no anchor act, member binding, fixed-point execution, end test, gauntlet, physical
  numerical evaluation, or comparison with measured constants was invoked.

```text
CLOSURE_BEGIN_BYTE = 0
CLOSURE_END_BYTE = 2709
PREDECLARATION_OUTPUT_SCAN = 0 hits
STAGE_RULE_PAYLOADS = 1
RESTRICTION_LIMIT_RECEIPTS = 7
COMPLETE_JAC14_SUITES = 0
PRINCIPAL_ENTRIES_FILLED = 0
```

Self verb audit: “derived” applies to the stage rule and seven structural receipts with their
replay procedures displayed. “Produced” counts those receipt payloads, not a complete suite.
“Stopped” names the finite-list, candidate/superselection, and downstream-seal gates. No cutoff,
fiber, candidate, map beyond functorial induction, or verdict is selected. `VERB_AUDIT_SELF = CLEAN`.

## 8. Final lines [CLAIMED]

```text
CLOSURE = declared-first (byte position 0, closure end 2709; scan 0 hits)
STAGE_RULE = DERIVED (member 06 [7090,8455); member 07 [5412,5787); payload SHA-256 986cc0585d7513aed30151db4bd5aeb774104ab27bbcd4b640f1a8e1615800d4)
SOURCE_GALERKIN_AT_RECEIVER = IRRELEVANT-SHOWN (A_src fixed at every N; connecting map id_A_src; no source compression datum consumed)
CERTIFICATES_PRODUCED = 7 (JAC-14 restriction/limit exact-replay receipts; ordered-list root 20f12ff18ce33785f5bbb7b100f68d39d2345b26aa655b4f46caac73698e8f5a) / STOPPED (0 complete suites: infinite-family versus finite-list inventory, candidate/E_joint blocks, blind fiber, downstream suite seals)
FIBER_GATED_REMAINDER = enumerated (FGR-01 suite.a0_rank_fiber_sha256 only; opaque digest copy; all other current gates separately named)
NEW_CONTENT = NONE-BEYOND-DERIVATION
BLIND = HELD
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
