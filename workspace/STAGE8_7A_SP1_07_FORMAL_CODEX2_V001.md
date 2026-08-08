# Stage 8 / 7A Step 11 — SP1-07 Formalization Batch 1 — Codex 2 v001

Date: 2026-08-08  
Lane: CODEX 2  
Scope: source-bound TYPE/KERNEL formalization for `C-B-V011-SP1-07` only

## 0. Preflight, custody, and sealed sources

The relay input
`relay_inbox/RELAY_PASTE_735_SP1_07_FORMALIZATION_CODEX2_V001.md` rehashed
to `570d7a45691ed4c11a39f7e545b18ac28b2fbbd885b7e090cd55cc55ea035608`;
its sidecar and CODEX 2 lane guard matched. `relay_outbox/735_ACK.md` was
written before task work. The requested report name was absent from the
cleanroom and archive workspace.

| ID | Sealed source | SHA-256 | Use |
|---|---|---|---|
| `GLOBAL` | packet `BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md` | `949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd` | sole derivation source |
| `SPEC` | `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V012.md` | `382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504` | row and opcode contract |
| `U7` | `STAGE8_7A_U7_DISPOSITION_CODEX2_V001.md` | `0145c5dbbed1681067a211021892100cf6d18c6ef25ba9c7e905aeedc8a7f20d` | source-locus ruling and block index |

The current check-map descriptor digest for `C-B-V011-SP1-07` is
`22f8c1b0d78f634c87976ae5ddf5f533df1a1b2731a8a1d8c6495b1bb20f93ca`.
Its program requires closed `SCHEMA` inputs, a `TYPE` graph, a nonempty
`ENUM`, exact ID comparisons, a repeatable `KERNEL/COMPARE` pair over every
mandatory derivation, and a final `EXACT` check for graded commutation and
pushout parenthesizations.

Every emitted proof step carries at least one exact sealed citation contained
in one of these blocks:

| Block | `GLOBAL` byte span | Block SHA-256 | Content |
|---|---:|---|---|
| `B_GLOBAL_TYPED` | `[1103,1704)` | `daeb7bc7b448e78009703e6fc7a7946a76844f7ee6f479327e63ab6ab84057d2` | one source space/CAR, distinct even record factors |
| `B_GLOBAL_DESCENT` | `[1705,4005)` | `fcbb16c6cad76b08a210d55d42a1ce82d165ae3a0adfd63f28ba16f30946d1ce` | projectors, pushout, global `h_K`, overlap, associativity and covariance statements |
| `B_GLOBAL_ORDER` | `[5027,6406)` | `17314d1ffd972873a65ee99e3309610b70e25dfddf612dd7adb2a83df456d7ed` | Stone statement and executable obligation list |

The builder rehashed all three whole sources and all three blocks before
emission. No unsealed source, requirement sentence, or newly written
mathematical bridge is used as evidence.

## 1. Closed formal bundle

The cleanroom package is `step11_sp1_07_formal/`. Canonical JSON uses sorted
keys, tight separators, UTF-8, no non-finite numbers, and no trailing newline.
All proof files are named by the SHA-256 of their exact canonical bytes.

### 1.1 Schemas and row carriers

| Carrier | File | SHA-256 | Opcode role |
|---|---|---|---|
| `S_SP1_07` | `contracts/formal_manifest.schema.json` | `82b3598f5a9b22e46f0e0e5663dddd21299e7904cf47b64f21a7db77d30d3ee7` | closed `SCHEMA` for the formal manifest |
| proof-object schema | `contracts/proof_object.schema.json` | `4d0a74987115ca58546ef17f88a6098fbaf58c84814f5944da52c56308ca451c` | closed repeatable `KERNEL` input shape |
| typed-graph schema | `contracts/typed_global_graph.schema.json` | `fd33eceaae65bbc95730ce11fc0941a0631040ca64f4def0a9ca2132a4ac799d` | closed `TYPE` input shape |
| `S_SP1_07_expected` | `contracts/expected_ledger.schema.json` | `cf08e9888345916fa2f284beebc73914f61c6a819b581f8e5c6c4f556066f9fa` | closed expected-ledger schema |
| `M_SP1_07` | `generated/M_SP1_07.json` | `1c242a96c819bfeeb169ce2aa4a933531897b4032c5ba65e6ddf545ad4f30c0b` | manifest binding schemas, graph, grammar, certificate, ledger, and proof index |
| `G_SP1_07` | `generated/G_SP1_07.typed_graph.json` | `74866ef69479dd4e12b4c8c65fb463fcf8f6474cca43323955fa3300967d973e` | one `CAR(K_Sigma)`, distinct even `R_c`, pushout and `h_K` types |
| `G_overlap_order` | `generated/G_overlap_order.json` | `3b7dbe263087af2e8dcf0aa36cb8c0587db4563fc016a4f92a4cca7e7a48c0da` | ordered mandatory nine-ID grammar |
| `p_complete` | `generated/p_complete.json` | `d6bb2526579c76d7e56f2603823a116186540126f507db835e57f78c38389470` | nonempty clause-to-ID coverage certificate |
| `E_SP1_07` | `generated/E_SP1_07.json` | `3925d5333a7c5e53c65a307630c9150a0e218d352dafd1f944abe090e3d24fc3` | nine exact expected conclusions |
| `P_SP1_07` | `generated/P_SP1_07.json` | `eee07455d902dd9390ddff6594b1728419096a3a23298dcc39f21cfef3b95f73` | nine content-addressed proof records and statuses |

The grammar IDs, expected-ledger `required_ids`, and proof-index IDs are the
same ordered, nonempty nine-member list. No derived-ID-zero escape exists.

### 1.2 Proof-object census

The closed proof schema permits only `SEALED_SOURCE_ASSERTION`,
`DEFINITIONAL_UNFOLDING`, and `CONJUNCTION_INTRODUCTION`. Premise references
must point backward, every step must have a source citation, every citation
must rehash and lie inside its declared block, and a `KERNEL_READY` object must
have no gap and must end in its exact expected conclusion.

| ID | Status | Proof SHA-256 | Result |
|---|---|---|---|
| `D01_SHARED_BOUNDARY_DESCENT` | `KERNEL_READY` | `c6c01fc611f8e4c682a3d95b9d52d8a2b25a3fad947aa2f7c15c50d1c3cf2329` | one global CAR, distinct even factors, pushout-once, and displayed `h_K` construction replay exactly |
| `D02_THREE_CELL_LEFT_PARENTHESIZATION` | `PARTIAL_MISSING_STEP` | `e920f618914e1cad5e56f9f598aa3c97ef3c78b1cb07cc6c93daad25a3efa8a1` | gap `G02_LEFT_PUSHOUT_WITNESS` |
| `D03_THREE_CELL_RIGHT_PARENTHESIZATION` | `PARTIAL_MISSING_STEP` | `b1adaaea574a8035b2dd2c5fd748c6b47b429f404a5ed9a445e601eff270f9a6` | gap `G03_RIGHT_PUSHOUT_WITNESS` |
| `D04_CELL_ORDER_INDEPENDENCE` | `PARTIAL_MISSING_STEP` | `38e503f1821617e9fc3072ddeda77c0ab251c61433416d2017fd57b936767bd6` | gap `G04_CELL_ORDER_EQUALITY` |
| `D05_PRIMITIVE_SHARED_SUPPORT_OVERLAP` | `KERNEL_READY` | `38b1cd2fc1e17c61e0ff156391743f4dd64c70bfa446edaf932dc3ec051f1aed` | projector, nonzero shared support, trace formula, orientation independence, and `h_K`/`h_K^2` distinction replay exactly |
| `D06_GRADED_RECORD_FACTOR_COMMUTATION` | `PARTIAL_MISSING_STEP` | `e19f4a8dd42d696808527e2c9ba0ddc140022de1465edb00c537d4bbd65b93c5` | gap `G06_GRADED_COMMUTATION_IDENTITY` |
| `D07_VERTEX_RELABELING_COVARIANCE` | `PARTIAL_MISSING_STEP` | `ad4ebd170ad0ac97191b55a8fc65ca9a44e4ced8edaf3d40a78715363fe9656b` | gap `G07_RELABELING_SQUARE` |
| `D08_ORIENTATION_REVERSAL_COVARIANCE` | `PARTIAL_MISSING_STEP` | `d793ea4351b09b99403f50bb08bf2ba5b9336ecb49d557a832776a871b40bffb` | gap `G08_ORIENTATION_UNITARY_SQUARE` |
| `D09_FINITE_STONE_ORDERING` | `PARTIAL_MISSING_STEP` | `771f9e212dc44dc4c3e2f41fd50c2ce9c57fa6964897c41031fb32bf977bc78f` | gap `G09_STONE_REPLAY` |

Nine closed proof records were emitted. “Built” in the verdict line counts only
the two records that are actually KERNEL-ready; the seven partial records are
custody-preserving source skeletons and are not counted as proofs.

## 2. Named missing derivation steps

The sealed source states the high-level result or lists the executable
obligation for each item below, but it does not display the carrier needed for
machine replay. The compiler therefore returns
`PRECONDITION_NOT_REPLAYABLE`, not criterion FAIL.

| Gap | Required missing bytes | Blocks searched |
|---|---|---|
| `G02_LEFT_PUSHOUT_WITNESS` | explicit `c1,c2,c3` incidence-map objects, left-associated pushout cocone, and canonical equality map to `h_K(c1,c2,c3)` | descent, order |
| `G03_RIGHT_PUSHOUT_WITNESS` | explicit `c1,c2,c3` incidence-map objects, right-associated pushout cocone, and canonical equality map to `h_K(c1,c2,c3)` | descent, order |
| `G04_CELL_ORDER_EQUALITY` | the two sealed cell-order enumerations and term-by-term permutation/equality witness for their `h_K` assemblies | descent, order |
| `G06_GRADED_COMMUTATION_IDENTITY` | explicit calculation of `[iota_c(x),iota_d(y)]_graded=0` for distinct even record factors | typed, descent |
| `G07_RELABELING_SQUARE` | typed vertex permutation on incidence vectors and its commuting `h_K` conjugation square | descent, order |
| `G08_ORIENTATION_UNITARY_SQUARE` | content-addressed cellular orientation unitary and explicit `h_K` conjugation square | descent, order |
| `G09_STONE_REPLAY` | self-adjointness certificate for `H_K` and exponential-composition/uniqueness proof | order |

No universal-property map, equality witness, commutator calculation, unitary,
or Stone proof is synthesized from the corresponding prose assertion.

## 3. Compile against the descriptor

| Receiver | Result |
|---|---|
| `r_schema` | `PASS` — closed manifest and four schemas present |
| `r_type` | `PASS` — one global source CAR and distinct even record graph type |
| `r_expected` | `PASS` — closed nine-entry expected ledger |
| `r_enum` | `PASS_9_IDS` |
| `r_nonempty` | `PASS` |
| `r_required_ids` | `PASS` — grammar equals expected ledger |
| `r_proof_ids` | `PASS` — grammar equals proof index |
| repeatable `r_d/r_cmp_d` | `2 KERNEL_READY / 7 PRECONDITION_NOT_REPLAYABLE` |
| `r_exact` | `PRECONDITION_NOT_REPLAYABLE:G02,G03,G04,G06` |

Overall compile outcome:
`PARTIAL_CONFORMANCE_2_BUILT_7_GAPS`. The recomputed row status is
`PARTIAL_FORMALIZATION_2_OF_9_KERNEL_READY`. Because the PASS conjunction
requires every `r_d`, every `r_cmp_d`, and `r_exact`, the row does not PASS.

## 4. Static battery and does-not-do

The isolated builder ran with `python3 -I -S -B`. AST parsing passed. The
23-file generated inventory reverified byte length and SHA-256 for every
member; its own digest is
`314077a1f1d63d02263d02c88f29c475b14b95efd6ed1869594cd1bb3a3eb8b2`.
The self-check record hashes to
`7a1f2224dea7409187dfff3686f3c9303c2800caab4b278377766a46eaff1a29`
and records three source pins, three block pins, four schema files, 26 step
citations, two ready proofs, seven partials, and seven named gaps.

Four negative controls all refused as required: missing step citation, flipped
span digest, a ready proof carrying a gap, and an unknown derivation ID. A
second builder launch over occupied package outputs refused
`OUTPUT_COLLISION:package outputs`.

`F_PLDEC`: CLEAN. Only finite structural carriers and formal source statements
are serialized. No physical quantity, target constant, member, fixed point, or
end test is computed. M-2 checked exact, whitespace-normalized,
scope/self-reference, and hyphen/space/underscore surfaces inside the three
sealed source blocks; requirement-only statements were not promoted into a
missing proof step.

Admission remains `BARRED_STEP11_SUBGATE`. `proof_authorized=false`,
`alpha_computed=false`, and `kappa_record_computed=false`. No board, seal,
descriptor, evaluator package, or chain state changes here.

Verb audit under the verdict-line scope rule: CLEAN. “Built” means a closed
record ending at the exact expected conclusion with zero gaps. “Partial” means
the source-backed prefix exists but KERNEL cannot replay the named absent step.
“Compile” is this bounded source-bundle compilation, not an evaluator verdict
or proof authorization.

PROOF_OBJECTS = 2 built / 7 gaps named
COMPILE = PARTIAL_CONFORMANCE_2_BUILT_7_GAPS
ROW = PARTIAL_FORMALIZATION_2_OF_9_KERNEL_READY
ADMISSION = barred, stated
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
