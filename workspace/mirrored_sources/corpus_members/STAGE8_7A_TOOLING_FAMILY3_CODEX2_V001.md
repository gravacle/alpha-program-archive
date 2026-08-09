# Stage 8 / 7A Step 11 — Tooling Family 3: mutation and observation generation

**Lane:** CODEX 2  
**Relay:** 754  
**Disposition:** deterministic negative-control generator built and run; admission barred

## 1. Pickup, custody, and bounded scope

| Object | SHA-256 | Result |
|---|---|---|
| `relay_inbox/RELAY_PASTE_754_TOOLING_FAMILY3_CODEX2_V001.md` | `655aded9cb33a3c9e45ad6095706868631de02fcfdf6d94b5725fe692b3f2bf3` | seal sidecar verified before reading |
| pickup acknowledgement | `754 \| CODEX 2 \| 655aded9cb33a3c9e45ad6095706868631de02fcfdf6d94b5725fe692b3f2bf3` | written before task work |

The requested report, report seal, `754_DONE.md`, and package directory were absent in the cleanroom and archive workspace at preflight. All writes were made in the cleanroom.

The generator consumed the four completed relay-744/745/747/748 instances and the completed SP1-07/SP2-05 proof-bundle lineage, including the shared orientation-unitary successors. It generated only mutation classes that the sealed V012 descriptor fixes together with an observable rejection receiver. A negative-control record is tooling evidence; it is not an evaluator row verdict, proof authorization, or admission event.

## 2. Generated pins and sealed input census

The governing spec reverified at SHA-256 `382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504`. The generator locates the unique five-column descriptor row, excludes its line terminator, and records the exact byte span, row digest, procedure digest, and predicate digest. It does not transcribe descriptor pins into source.

| Row | Adapter | Completed base SHA-256 | Descriptor-row SHA-256 |
|---|---|---|---|
| `C-B-V008-05` | opposite holonomy | `0a400a1d19c436edd1a407c95390916a908f57281176ec22491eb139fb107775` | `7cf4057fcfb553db6191f944ebcddb460998f06e842eed4f058aae27bc46cb00` |
| `C-B-V009-08` | scope promotion | `c41f5d05c0bc784281206aede14e310b7b7e68304cbb81c8b43e787a0ac23f84` | `19d59b84a63c3c761237316f377f7b293839afc323c62ea60e464f2ed7dd13f3` |
| `C-B-V010-11` | descriptor mutation-class probe | `664059f4b10f1b78b1e04f111b77adc556644378a741622603bfbba957aa2b2d` | `9345948b5e6fb0d40e2e737f61d19b199b54926fb8121ec11790cf3ac8446a57` |
| `C-D-A35-02-QUASIFREE-CAR-LIFT` | quartic erasure | `47485f836710f3819bfda19744b9303e0f9cd065d93fa6859df4b27efb7eb03a` | `95c5e259db89a8343a4545ae3ec0641f10c836ea702f880795a66d802c82c2bd` |
| `C-B-V011-SP1-07` | mandatory proof-index omission | `89bf844bc03891bb16b51495b34ec72c655793919771da72a675ff0df057f14c` | `22f8c1b0d78f634c87976ae5ddf5f533df1a1b2731a8a1d8c6495b1bb20f93ca` |
| `C-B-V011-SP2-05` | index omission plus quartic rejection | `a1f377eec3d75d28a441fac197c05e6b3687da25b22feb804ee15fef2bfb3369` | `8dbccdf91aa34912d3ec8e910a1ee23e58c7281bfd42d82c0f1f0724775e1686` |

The instance schemas and every nested content/source-span reference reverified before generation. These sealing reports and their sidecars also reverified:

| Sealed report | SHA-256 |
|---|---|
| `STAGE8_7A_V008_05_COMPETITOR_CODEX2_V001.md` | `7e9e7772df33d21ac46833539af8d561bf986f9153c34a85333c944376c24ae5` |
| `STAGE8_7A_V009_08_GRAPH_CODEX2_V001.md` | `dff7e3506022559dff7a25d90ec97dea6838bfb775f3e1f434ea7d1ad923c38c` |
| `STAGE8_7A_V010_11_CATEGORY_CODEX2_V001.md` | `a8ceb54a22f026e8f2953cd5289e7c1172aa1a5c096788cd9ea23e0866ff2c9e` |
| `STAGE8_7A_A35_02_INSTANCE_CODEX2_V001.md` | `04eab6a7e6264abcb0f04647967de4e0378650b229365cec3ebed74585969cf3` |
| `STAGE8_7A_SP1_07_FORMAL_CODEX2_V001.md` | `f1dc27ad972a5e0429e778c8f62b9dad4b7463fdfde9459d79a6029f84d73a0f` |
| `STAGE8_7A_SP1_07_WITNESSES_CODEX2_V001.md` | `8639afe8366adcfa59c65f907ec79d326dffd63b93fed7f79070db59c9979244` |
| `STAGE8_7A_SP2_05_FORMAL_CODEX2_V001.md` | `3e440b25ebdd37e9ac70ea2fa8cfc307349d13bd6375a5275cd2a3c87d4daf80` |
| `STAGE8_7A_ORIENTATION_UNITARY_CODEX2_V001.md` | `831c0dd826c40a4e156e5d6104ca87cd08116ba2d30af1f7b1d36f31c2c72ed2` |

The generated input manifest hashes to `ce6b232fe93364ecd7e9036141f39d2a4053705c00e049fc033d1bb2b72b9759`.

## 3. AF1 — tool, closed interfaces, and generation law

Package root: `step11_tooling_family3/`.

| Package object | Purpose | SHA-256 |
|---|---|---|
| `generate_mutations.py` | pin generation, sealed-input validation, six adapters, mutation/rejection emission, controls | `4af09436a00996ef34439fbdac7d88e0baf70bb590e76a90c6aea9053de984a0` |
| `contracts/tooling_family3.schema.json` | closed mutation, expected-rejection, row-status, and run-result interfaces | `5eb8669243cafc24b43afa34021c1ad0b831e0c236fa148c058babb6f767ce2c` |
| `inputs.generated.json` | generated input and descriptor-span pins | `ce6b232fe93364ecd7e9036141f39d2a4053705c00e049fc033d1bb2b72b9759` |
| `generated/run_result.json` | complete output census and underdetermination record | `c03c20ab5f5371ba1445aa2af7165280671b9c5a0ad7a9a3597070b537ad73fe` |
| `generated/self_check.json` | replay and biting-control transcript | `0ee608d656c4ffb810a2d63bf66e46c115e4733690d7aa79e27d16436e0e93e5` |
| `inventory.generated.json` | self-excluding 51-member package inventory | `2cd8d99913f91238e7698cb6410c80e228b7e974c702779c6e61aa7d2fc9b756` |

The tool is standard-library-only and ran directly under `python3 -I -S -B`. Canonical JSON is UTF-8, sorted-key, tight-separator, finite-number serialization with no trailing newline. Every mutation and expected-rejection filename begins with the SHA-256 of its exact canonical bytes. Absolute paths and cleanroom escapes are rejected. There is no load-bearing `assert` in the generator.

For every emitted pair:

1. the base object, sealed descriptor row, and relevant grammar/index/proof bytes are content-addressed inputs;
2. the adapter verifies the exact descriptor trigger before mutation;
3. the transformed subject must differ from the base bytes;
4. the expected rejection binds the mutation digest one-to-one and names its actual receiving opcode; and
5. both records state `BARRED_STEP11_SUBGATE` and `chain_invoked=false`.

Expected records state their basis as `SEALED_DESCRIPTOR_AND_INSTANCE_NOT_PRIOR_OUTCOME`. No prior positive compile or evaluator result supplies their direction.

## 4. AF2 — generated mutation and expected-rejection census

| Row | Mutations | Expected rejections | Descriptor-grounded class |
|---|---:|---:|---|
| `C-B-V008-05` | 1 | 1 | use the exact inverse/opposite-holonomy competitor where the row requires it to fail against `W` |
| `C-B-V009-08` | 1 | 1 | change the unique `DOES_NOT_ENTAIL` two-path/general edge into a positive promotion, which the scope predicate bars |
| `C-B-V010-11` | 0 | 0 | no mutation class or rejection encoding is named by the sealed descriptor |
| `C-D-A35-02-QUASIFREE-CAR-LIFT` | 1 | 1 | remove the uniquely named quartic higher-sector control, which the predicate says may not be erased |
| `C-B-V011-SP1-07` | 9 | 9 | omit each mandatory derivation ID once; each exact ID comparison must reject |
| `C-B-V011-SP2-05` | 8 | 8 | omit each of five pushout and two orientation proof-index IDs once; serialize the sealed nonzero-quartic primitive candidate and bind its KERNEL rejection |
| **Total** | **20** | **20** | **five rows receive generated controls** |

### 4.1 Individually content-addressed outputs

| Row | Selected mutation member | Mutation SHA-256 | Expected-record SHA-256 | Receiver / expected rejection |
|---|---|---|---|---|
| `C-B-V008-05` | `W^-1` | `f9c73d9989c55256f4062f84dabf10818fa0ca0ef5b215cbaaf367eb00f19ee4` | `a663d1ebef08dfef024eb2bf0e46d24bb32ee9156e47ed5f75189ca7ec4f8c74` | `EXACT / OPPOSITE_HOLONOMY_MISMATCH` |
| `C-B-V009-08` | `E04_TWO_PATH_DOES_NOT_ENTAIL_GENERAL` | `5cc32605b08c046bad38ad7b25ffa0c4d73b5c5d04a55af69b80c17c9f2eeb60` | `1099a1e2390b37812aaa671e7f3a5a60a4f9c2a6c28b7318cb7a11c03aa04b45` | `TYPE / SCOPE_PROMOTION` |
| `C-D-A35-02-QUASIFREE-CAR-LIFT` | `E06_QUARTIC_HIGHER_SECTOR_CONTROL` | `c077dd05ad3518ae9bc06f04f2ff6270b55c1a0bfb037f33ce05cf74a527eead` | `e1f39e68ade0c7974223d5a0109efd1d26f6cf44846828205c2644c598ea255e` | `EXACT / QUARTIC_CONTROL_ERASED` |
| `C-B-V011-SP1-07` | `D01_SHARED_BOUNDARY_DESCENT` | `4bc910b55e5fd0e0ba050aeb08f01b39099548a6487730a2ceb75913f2bb5701` | `5cbc0272be4269c7b1683bcc3236cdf2bd839add39acfe56ac021847942ef910` | `COMPARE / MANDATORY_ID_MISSING` |
| `C-B-V011-SP1-07` | `D02_THREE_CELL_LEFT_PARENTHESIZATION` | `adc0c5ccfc808346922b1820d01582164a6f848228febe68132c0cbe53c64c3b` | `723bfaa3ec1dc92bea9a8df32626fe45b58502be685a3c8e070e860b74ede1f7` | `COMPARE / MANDATORY_ID_MISSING` |
| `C-B-V011-SP1-07` | `D03_THREE_CELL_RIGHT_PARENTHESIZATION` | `b4dc3c64bf40fdfd10f3f01d25f0f1d96250869b6b811889dd9f91a72c1673d8` | `032a307dcad684092500bc209d9f1bb65d054eacab57015eff43f18dd14d1a25` | `COMPARE / MANDATORY_ID_MISSING` |
| `C-B-V011-SP1-07` | `D04_CELL_ORDER_INDEPENDENCE` | `400f1e32d14a59ee7e47c6b4fa65734af2d4a9b59b54cda7c5f2ded6e18dc5d9` | `07fbd04f87015a2b4d5c7662fd8dbbcd2a642702262f4e43e9a29917befff7b9` | `COMPARE / MANDATORY_ID_MISSING` |
| `C-B-V011-SP1-07` | `D05_PRIMITIVE_SHARED_SUPPORT_OVERLAP` | `aadf3aa8d513e047d340164c792abac2b6c4ba3a3b343331153148cd36690769` | `6e93eb640714e8c7b11b129e9e599472d4a341298d167d08da39382e7b714837` | `COMPARE / MANDATORY_ID_MISSING` |
| `C-B-V011-SP1-07` | `D06_GRADED_RECORD_FACTOR_COMMUTATION` | `11c8491efbcdf5e80beed9ecda63c419c9f5e7ae6a663b30cb3ccedb32200813` | `3e640ec6ed13e203d9d817a0ffda5c6be32140737f04595464170e818fd92f98` | `COMPARE / MANDATORY_ID_MISSING` |
| `C-B-V011-SP1-07` | `D07_VERTEX_RELABELING_COVARIANCE` | `8a3e7a5e58c268206ea35b0ad3a912363034cae42ccf578447a882c83c9e3893` | `63fb561cc8f7a79b3be9277ca8f59346e1329c515431fe47bc37fbf333cdec36` | `COMPARE / MANDATORY_ID_MISSING` |
| `C-B-V011-SP1-07` | `D08_ORIENTATION_REVERSAL_COVARIANCE` | `23d8c68c199049fc30cc4f0ec042ef166efdcf5739ba5c53d6914884fc6cb3ed` | `556776f6eaebed2143df8351511e55fe9f605b8cac54c4ebcfa7d8e42e2cbe05` | `COMPARE / MANDATORY_ID_MISSING` |
| `C-B-V011-SP1-07` | `D09_FINITE_STONE_ORDERING` | `33f9e1d8ba2eb2d3c1757df352bd9b8504c5d83fc56c650fab00101f396c265a` | `f630567086543a66221555d585387b11caf0cfcbd993c03df4cb6399896902d7` | `COMPARE / MANDATORY_ID_MISSING` |
| `C-B-V011-SP2-05` | `P01_SHARED_VERTEX_PUSHOUT_ONCE` | `cd8883fecd73888246942463b8325799f67508a26f1e8d19a45ac8601e0c082f` | `174560d661b65e665cc057ec2a8c249e432a5e6def73ded1766601226d804008` | `COMPARE / MANDATORY_ID_MISSING` |
| `C-B-V011-SP2-05` | `P02_LEFT_ASSOCIATIVITY` | `8df54ccd32156788a97bbd5b885d9be48d48794df9ee673c3fe308f5eea6c5be` | `b5c711c59bfd3da02cc664b88ee8f4d19ecd0ae060cbad859000eda54c1b2799` | `COMPARE / MANDATORY_ID_MISSING` |
| `C-B-V011-SP2-05` | `P03_RIGHT_ASSOCIATIVITY` | `d825f5dc8de54fd57a4145786f7adeface2c2d4bea408a90054b2d126de8d0eb` | `ae7c4eb1c93991786f47f95b754b181178b820d5a33834b6cbfd1f4c322224af` | `COMPARE / MANDATORY_ID_MISSING` |
| `C-B-V011-SP2-05` | `P04_CELL_ORDER_INDEPENDENCE` | `56e41ba1f1383e40b09cd525c68f504ba9e513ba650f39612780ff696a8870cc` | `b69cca8dd187c4d5d626ddf42c47275292041e0f4fce65f2aa56038401f9e431` | `COMPARE / MANDATORY_ID_MISSING` |
| `C-B-V011-SP2-05` | `P05_VERTEX_RELABELING_COVARIANCE` | `a3099e6085438ba9a8d4e48feabf3136b59443a2461ae7e1bda30b664906c82c` | `e11d3302dd8b8f6fbb23fa70be6a5a403100413c3783a8bae7b3b50a53dab918` | `COMPARE / MANDATORY_ID_MISSING` |
| `C-B-V011-SP2-05` | `O01_SOURCE_PROJECTOR_REVERSAL` | `ae77332c591401d36a43a7db68b696c952fe94c265e48f251af480e3eec1cca4` | `dcb93aaaaedb356f1ed05713dc72f6caceb64633dc5bd0a6c3e7120b04025de6` | `COMPARE / MANDATORY_ID_MISSING` |
| `C-B-V011-SP2-05` | `O02_FULL_SOURCE_RECORD_ORIENTATION_COVARIANCE` | `4c726873d403e2d617dae35864dc28a019005b7ff6b4bfa4fa02143414bebe44` | `15b8d079cbb9df5eb200981368b31d5bee92b9a7c5918a6005b3c40742a93f15` | `COMPARE / MANDATORY_ID_MISSING` |
| `C-B-V011-SP2-05` | `Q01_QUARTIC_PRIMITIVE_REJECTION` | `007006fbefdf0fec021306b92a5ad301d6950f1377323b0339f8d0604583f46a` | `8d8c69a7b948d8178081e931d71d87915be6455a008495bd143ebaf6445aadf8` | `KERNEL / QUARTIC_PRIMITIVE_REJECTION` |

The SP1 and SP2 omission families are complete over their sealed mandatory ID sets: 9/9, 5/5, and 2/2 respectively. The quartic mutation preserves the exact symbolic `H_lambda` formula, sector observations, and adopted-premise axiom hash from the sealed proof; it does not select or evaluate a numeric `lambda`.

## 5. Underdetermined item

`C-B-V010-11` requires positive `TYPE` checks over objects, first-opening subsets, labels, morphisms, identities, and composition. Its sealed descriptor names no mutation grammar, negative candidate, rejection value, or rejection receiver. Label deletion, label invention, morphism deletion, composition mutation, and identity mutation are all reachable but distinct choices.

Accordingly, Family 3 emits none of them. The run result records:

```text
MUTATION_CLASS_AND_EXPECTED_REJECTION_RECEIVER = UNDERDETERMINED
reason = SEALED_DESCRIPTOR_REQUIRES_POSITIVE_TYPE_AND_CATEGORY_LAWS_BUT_NAMES_NO_MUTATION_CLASS_OR_REJECTION_ENCODING
```

This is the only underdetermined item in the bounded six-row input census.

## 6. Rows advanced and admission boundary

The following bounded tooling-layer statuses now have generated mutation instances and expected-rejection bindings:

- `C-B-V008-05`;
- `C-B-V009-08`;
- `C-D-A35-02-QUASIFREE-CAR-LIFT`;
- `C-B-V011-SP1-07`; and
- `C-B-V011-SP2-05`.

“Advanced” here means only `MUTATION_CONTROLS_GENERATED_ADMISSION_BARRED`. No row is reported as evaluator PASS, FAIL, or admitted. The V010-11 positive instance remains intact and its missing negative-control law is named rather than supplied.

## 7. Static replay and negative controls

| Control | Observed refusal | Result |
|---|---|---|
| perturb a pinned input digest | `HASH_MISMATCH` | PASS |
| remove a descriptor trigger | `DESCRIPTOR_TRIGGER` | PASS |
| select an unknown adapter | `UNKNOWN_ADAPTER` | PASS |
| emit unchanged bytes as a mutation | `MUTATION_NO_CHANGE` | PASS |
| perturb the mutation-to-expectation binding | `EXPECTED_REJECTION_BINDING` | PASS |

The positive run verified 6 input rows, 20 mutation instances, 20 expected-rejection records, and 20 one-to-one digest bindings. An independent replay verified 51 canonical JSON files, all 51 self-excluding inventory members, all content-addressed filename prefixes, and the same 20 bindings. A second tool invocation refused occupied package outputs with `OUTPUT_COLLISION:package outputs`.

- `F_PLDEC`: CLEAN. The tool performs byte hashing, schema checks, finite list mutation, symbolic record copying, and exact structural comparison only.
- Anti-tuning: mutation membership is determined by the sealed descriptor and completed instance/grammar IDs, not by prior evaluator outcomes.
- Gates: `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false`; there was no member binding, fixed-point execution, end test, numeric physical evaluation, or comparison to a measured constant.
- Admission: every mutation, expectation, row status, and run record states `BARRED_STEP11_SUBGATE`.
- Chain: no evaluator chain was invoked.
- Verb audit: “generated,” “bound,” and “advanced” refer only to Family-3 tooling records. No proof, physics, evaluator, board, admission, or seal verdict is claimed.

TOOL = built (controls displayed)
PRODUCED = 20 mutations / 20 expected rejections bound
UNDERDETERMINED = C-B-V010-11: mutation class and expected-rejection receiver not named by sealed descriptor
ROWS_ADVANCED = C-B-V008-05, C-B-V009-08, C-D-A35-02-QUASIFREE-CAR-LIFT, C-B-V011-SP1-07, C-B-V011-SP2-05 (tooling-layer only)
ADMISSION = barred, stated
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
