# Stage 8 / 7A Step 11 — SP2-05 Formalization — Codex 2 v001

Date: 2026-08-08  
Lane: CODEX 2  
Scope: source-bound `SCHEMA` / `TYPE` / `ENUM` / `COMPARE` / `KERNEL` / `EXACT` formalization for `C-B-V011-SP2-05` only

## 0. Preflight and custody

The relay input
`relay_inbox/RELAY_PASTE_741_SP2_05_FORMALIZATION_CODEX2_V001.md`
rehashed to
`1c56e3a3b9dcd6e6cbfabf576520cfae7954ef736ac0938bb1a1e98938aaef62`;
its `.seal.sha256` sidecar and CODEX 2 lane guard matched. The pickup record
`relay_outbox/741_ACK.md` was written before task work. The requested report
name was absent from the cleanroom and archive workspace.

| ID | Sealed source | SHA-256 | Use |
|---|---|---|---|
| `GLOBAL` | packet `review_packets/STAGE7_QSPEC_CANDIDATE_V001/BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md` | `949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd` | sole mathematical source |
| `SPEC` | `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V012.md` | `382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504` | row and opcode contract |
| `U7` | `STAGE8_7A_U7_DISPOSITION_CODEX2_V001.md` | `0145c5dbbed1681067a211021892100cf6d18c6ef25ba9c7e905aeedc8a7f20d` | source-locus ruling |

The descriptor bytes for `C-B-V011-SP2-05`, excluding their line terminator,
rehash to
`8dbccdf91aa34912d3ec8e910a1ee23e58c7281bfd42d82c0f1f0724775e1686`.
The builder rehashed that row directly from `SPEC`; it did not transcribe the
deterministic procedure.

The sealed source block used by U7 is `GLOBAL[334,6406)`, SHA-256
`abef6d52ec372c48a407fcf5a87e8d5a9b41064f5255f9bdac8cbe697726d07b`.
Its closed sub-blocks are:

| Block | Byte span | SHA-256 | Bound content |
|---|---:|---|---|
| `B_GLOBAL_PREMISE` | `[334,1102)` | `52139a1c600db4a96bf17194cce7c57f308b5f0c7b34d32d85ebd5dcf0e54e7c` | adopted primitive quasi-free completeness premise |
| `B_GLOBAL_TYPED` | `[1103,1704)` | `daeb7bc7b448e78009703e6fc7a7946a76844f7ee6f479327e63ab6ab84057d2` | one global CAR and distinct even record factors |
| `B_GLOBAL_DESCENT` | `[1705,4005)` | `fcbb16c6cad76b08a210d55d42a1ce82d165ae3a0adfd63f28ba16f30946d1ce` | pushout, `h_K`, one-cell restriction, overlap, associativity, relabeling, orientation |
| `B_GLOBAL_CAR` | `[4006,5026)` | `f08456525bf3f5abb163b32bc3e7c9d1f084c79adb1d1ede879df10cc6cad76b` | CAR lift and low/high quartic control |
| `B_GLOBAL_ORDER` | `[5027,6406)` | `17314d1ffd972873a65ee99e3309610b70e25dfddf612dd7adb2a83df456d7ed` | finite ordering and executable obligations |

No unsealed root copy is cited. Every proof step is bound to one or more of
these exact packet spans.

## 1. Closed formal package

The cleanroom package is `step11_sp2_05_formal/`. Canonical JSON is UTF-8,
sorted-key, tight-separator, finite-number serialization with no trailing
newline. Proof filenames begin with the SHA-256 of their exact bytes.

The package contains a direct isolated builder, four closed schemas, both
finite grammars and completeness certificates, two proof-index manifests,
the typed global graph, the exact-control fixture, the adopted-premise record,
the covariance proof bundle, eight content-addressed proof records, the
compile and row-status records, and a self-check record. Its generated
inventory has 27 members and SHA-256
`78d7ddcb980804d7a6f7bce9e6b3dd34f6455543f475b7c6980b1bad62a2b828`.

### 1.1 Schema and manifest carriers

| Carrier | File | SHA-256 | Receiver |
|---|---|---|---|
| `S_global` | `contracts/formal_manifest.schema.json` | `8962baa6380131c13d1d479fa68488c452c8ebec6ad9989bd42e219970bd7b6f` | `SCHEMA` |
| `S_premise` | `contracts/premise_record.schema.json` | `eb1cf8a9bfd481d91788aa6e921604460ee5cb2314bbcb233cfa9dc4ba5d858e` | `SCHEMA` |
| proof schema | `contracts/proof_object.schema.json` | `0e257e7bd564e5a3518cad0af6ca55e576da1689560a459c1c4a6f41c1be1940` | both `KERNEL` inputs |
| typed-graph schema | `contracts/typed_global_graph.schema.json` | `786a766c9c72769dba414050b518b85d59fcb0e383b7958af9bf9e9145cf32aa` | `TYPE` input |
| `M_global` | `generated/M_global.json` | `7ab63e59326b77b2c0fe03b039ce8781c8db5b718b38208e5d9241ccf281a8f3` | content-addressed manifest |
| `G_global` | `generated/G_global.json` | `da5f0508cd0237dc02dd2a821001a4175e7303f2fb973642ae3208815fd8b848` | one-global-CAR / distinct-even-record graph |
| `premise_record` | `generated/premise_record.json` | `5d4f249bb5dd1beaa9d246a8c9e93411da33df8d9e50e1a08e8eef3d3e21151d` | adopted premise, content-addressed |
| exact fixture | `generated/SP17_overlap_quartic_exact.json` | `6af9e60ea1c6731f8eaefe23af18eb142ea8950cc0791bfdaf32501caca33eab` | `EXACT` |

The premise record binds the adopted premise by its exact span hash
`52139a1c600db4a96bf17194cce7c57f308b5f0c7b34d32d85ebd5dcf0e54e7c`.
The quartic proof preserves that same value, and only that value, in
`used_axiom_hashes`; the descriptor-side allowed-axiom comparison is exact.

### 1.2 Two finite enumerations

The pushout grammar is a nonempty ordered five-member enumeration:

```text
P01_SHARED_VERTEX_PUSHOUT_ONCE
P02_LEFT_ASSOCIATIVITY
P03_RIGHT_ASSOCIATIVITY
P04_CELL_ORDER_INDEPENDENCE
P05_VERTEX_RELABELING_COVARIANCE
```

The orientation grammar is a nonempty ordered two-member enumeration:

```text
O01_SOURCE_PROJECTOR_REVERSAL
O02_FULL_SOURCE_RECORD_ORIENTATION_COVARIANCE
```

| Carrier | SHA-256 | Check |
|---|---|---|
| `G_pushout` | `12730215a5d8ffa1fd95bac456296b5a45a47571a28745ea8d33d422303d3dfc` | five ordered IDs |
| `p_pushout_complete` | `5777bc15ff1753dec0c8bf21f51586d46fc0eca3db85bfded00da3ecd48793d0` | clause-to-ID surjection, nonempty |
| `p_pushout.index` | `af061957a6dbfbc85a6ef8d1d44314105c5e43fa129bc5d699d1aa8bd0fe9824` | same five ordered IDs |
| `G_orientation` | `515709544acbcbb45fdb74cce780fa99b25e0eeb026261d03a02855a123f0c33` | two ordered IDs |
| `p_orientation_complete` | `dc9cb5fd51576ccb7654ac0d6402ad44d5aa1db2f2d35b72e64a02ad7bb006e6` | clause-to-ID surjection, nonempty |
| `p_orientation.index` | `f8cd8851d6aef1950d04bf807c42e77b29ec24cb50846d15946255601d60cbe1` | same two ordered IDs |

Both `ENUM` outputs compare byte-for-byte in ID order with their proof
indexes. A zero-derived-ID completion cannot satisfy either certificate.

## 2. Proof-object and witness census

The schema permits only sealed-source assertion, definitional unfolding,
finite quotient normalization, finite reindexing, linear projector
calculation, tensor-factor normalization, CAR number-sector relations, and
conjunction introduction. Each premise reference points backward; every one
of the 20 proof steps has at least one exact citation, for 31 checked citation
instances total. A ready proof must end in its exact declared conclusion and
carry no gap.

| Proof ID | Status | Proof SHA-256 | Computed witness or exact gap |
|---|---|---|---|
| `P01_SHARED_VERTEX_PUSHOUT_ONCE` | `KERNEL_READY` | `dc7ba62cb0ba7b50e6d8aa635d3f40f17766b5aa36c12383ba9aed9aef83fa30` | quotient of the disjoint vertex union by the shared-label equivalence closure; record labels remain distinct |
| `P02_LEFT_ASSOCIATIVITY` | `KERNEL_READY` | `ad827c4a7122a5760ad1018df5dae215c9effc51cee520ea17c4e10a3a44021c` | left-associated finite pushout normalizes to `Q3_SHARED_LABEL_EQUIVALENCE_CLOSURE` and the cell-label operator sum |
| `P03_RIGHT_ASSOCIATIVITY` | `KERNEL_READY` | `1fd718a564950a579a904da50ed4597b9cb82de2b5f09b8f53057afce4536fa6` | right-associated finite pushout normalizes to the same quotient and operator sum |
| `P04_CELL_ORDER_INDEPENDENCE` | `KERNEL_READY` | `1b89333bfc4b7d7bece56e57dfdd6ebe971518e311b7fdab4bf80426b7693b4e` | finite reindexing preserves the sum by cell label |
| `P05_VERTEX_RELABELING_COVARIANCE` | `KERNEL_READY` | `4f8156b2bdd82a21b5dcdedabbb9248c50c4362170b562e4a46feff5042a7b03` | the induced finite source permutation closes the displayed conjugation square |
| `O01_SOURCE_PROJECTOR_REVERSAL` | `KERNEL_READY` | `75cb66b168f8e9d2c185aa5f586fddc42faf4bf33356c5934ccaff58e38b6a92` | direct rank-one calculation gives `P_c(-d_c)=P_c(d_c)` |
| `O02_FULL_SOURCE_RECORD_ORIENTATION_COVARIANCE` | `PARTIAL_MISSING_STEP` | `88b4d36f1de146a6f462c930c09955dc53e6c3771cf3412f1fff50c7e29b9836` | gap `G_ORIENTATION_UNITARY_CARRIER` |
| `Q01_QUARTIC_PRIMITIVE_REJECTION` | `KERNEL_READY` | `226dc3f8c10b477cdf6a7e8551b5379d27f24b797e8d6be9634046f13f963fe2` | CAR number sectors give vacuum/one-source equality and the two-source difference; the pinned adopted premise rejects nonzero `lambda` |

The source determines seven replayable witnesses. It states the complete
orientation covariance but does not type or display the cellular record
unitary. The missing carrier is exactly:

```text
content-addressed typed U_c:R_c->R_c,
U_c c_c U_c^*=c_(rev c),
and its commuting complete-h_K conjugation square.
```

M-2 searched `GLOBAL[334,6406)` under exact, whitespace-normalized,
hyphen/space/underscore, and scope/self-reference modes. The only hit is the
bare phrase “orientation unitary”; there is no `U_c`, defining equation, or
typed map. Promoting that assertion into a carrier would fabricate the one
remaining witness, so the partial proof object preserves the gap.

The covariance aggregate
`generated/p_pushout_relabel_orientation.json` hashes to
`973c1f628474d321c64cd31e21ca73f8d9972e91ec19369dc63caccf2f10a131`.
It lists all seven grammar proofs, six ready and one non-replayable. The
quartic proof is separately bound so its successful replay is not erased by
the covariance gap.

## 3. Compile against the sealed row

| Receiver | Result |
|---|---|
| `r_schema_global` | `PASS` |
| `r_type` | `PASS` |
| `r_enum_pushout` | `PASS`, five IDs |
| `r_enum_orientation` | `PASS`, two IDs |
| `r_compare_pushout_index` | `PASS` |
| `r_compare_orientation_index` | `PASS` |
| `r_kernel_covariance` | `PRECONDITION_NOT_REPLAYABLE:G_ORIENTATION_UNITARY_CARRIER` — 6/7 component proofs ready |
| `r_exact` | `PASS` — SP17 one-cell restriction, primitive overlap versus induced `h_K^2`, and quartic low/high controls |
| `r_schema_premise` | `PASS` |
| `r_kernel_quartic` | `PASS` |
| `r_compare_axioms` | `PASS` — used and allowed hashes are the same singleton premise-span hash |

The compile record, SHA-256
`470ec4636d5bfd9ab4975faaf71dd27b565bf41b0864c9f47321badb11a0976c`,
returns `PARTIAL_CONFORMANCE_7_BUILT_1_GAP`. The row-status record, SHA-256
`b5d989ff0ac740d7a8ab0d257e87a94f7317c820c5d8a0d875f0d3947a33b4d4`,
returns `PARTIAL_FORMALIZATION_7_OF_8_PROOF_OBJECTS_READY`.

This is not criterion FAIL: the full covariance precondition is not yet
replayable. It is also not PASS: the sealed PASS conjunction requires
`r_kernel_covariance.success`.

## 4. Static battery and scope

The builder ran directly under `python3 -I -S -B`. AST parsing passed. An
independent pass rehashed all 27 inventory members, decoded and recanonicalized
all JSON, checked all eight content-addressed proof filenames, confirmed seven
ready records and one partial record, rechecked the premise hash comparison,
and reproduced the compile outcome.

Five negative controls all refused: empty pushout grammar, missing proof-step
citation, a ready proof carrying a gap, a quartic used-axiom mismatch, and
promotion of the untyped orientation unitary. A second builder launch over
occupied package outputs refused `OUTPUT_COLLISION:package outputs`.

`F_PLDEC`: CLEAN. This relay serializes only finite structural objects and
symbolic identities already displayed in sealed prose. It performs no member
binding, fixed-point execution, end test, physical-quantity evaluation, or
comparison with a measured constant. `alpha_computed=false`,
`proof_authorized=false`, and `kappa_record_computed=false` remain in force.
No descriptor, evaluator package, board, admission, or seal state is changed.

Verb audit under the verdict-line scope rule: CLEAN. “Built” counts only a
closed proof record ending in the exact expected conclusion with no gap.
“Computed” means finite symbolic normalization or sector evaluation from the
pinned source bytes. “Underdetermined” names the absent typed carrier. The
compile result is this bounded formal-bundle compile, not an evaluator-chain
verdict or proof authorization.

PROOF_OBJECTS = 7 built / 1 gaps named
WITNESSES = 7 computed / 1 underdetermined
COMPILE = PARTIAL_CONFORMANCE_7_BUILT_1_GAP
ROW = PARTIAL_FORMALIZATION_7_OF_8_PROOF_OBJECTS_READY
ADMISSION = barred, stated
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
