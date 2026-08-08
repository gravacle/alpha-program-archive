# STAGE 8 TASK 6 — LINEAGE V2 BASELINE AND THIRTY-ROW RERUN

**Lane:** Codex 2 Lane  
**Date:** 2026-08-08  
**Scope:** PASTE 706 only  
**Custody:** cleanroom write; registrar mirrors

## 1. Lead determination

```text
LINEAGE = V2
BASELINE_DOCUMENTS = 48
BASELINE_DOCUMENT_ROOT = 52c5e039e178102b1c17c4939dcec42e8e06d9329acb5dd95ce607c594c3a0f8
BASELINE_MANIFEST_SHA256 = 59e05791f7d68a3c1e8185ca4994d970edaff2d327b2142cc9cddfe101b60ef2
ROWS_RERUN = 30
PASS = 24
FAIL = 0
BLOCKED = 6
BLOCKED_SET = {A23,A24,A25,A27,A28,A35}
FLIPS = none
SPEC_SEAL = false
```

The reviewed old board, not the superseded provisional board inside the first execution ledger, is the comparison base: `24 PASS / 0 FAIL / 6 BLOCKED`. Every row was recomputed against the V2 document set below. No old PASS was carried merely because it was old, and no expected flip was used as a target.

The principal expectation that A35 would flip does not survive the current sealed bytes. The runner and verifier now exist, but the certification of record limits confirmation to one row and the current evidence manifest carries 55 absent structural envelopes and three absent structural fixture observations. A35's unchanged criterion requires the evaluator to reproduce or reject its named regression subjects, not merely contain code paths that refuse missing inputs. It therefore remains BLOCKED on a narrower, evidence-layer blocker. This preserves C77 and the Q-604 partial-row guard.

## 2. Generated baseline manifest

The manifest was generated from current bytes, not a typed digest list. The generator read packet-member pins from the packet manifest, inherited-authority pins from sealed V011, the five original lineage roots from the sealed matrix ledger, package-member pins from the current Builder A package inventory, and sidecars where present. Its closed schema is `rd22.lineage-v2-baseline.v001`.

The document-root algorithm is:

```text
SHA256(
  "LINEAGE-V2-DOCUMENT-ROOT-v1\0"
  + SORT_LEX(each document's "id\0path\0byte_length\0sha256\n")
)
```

Canonical manifest bytes follow. Each row binding is also the evidence-source inventory for the corresponding board row.

```json
{"document_root":"52c5e039e178102b1c17c4939dcec42e8e06d9329acb5dd95ce607c594c3a0f8","documents":[{"byte_length":13786,"id":"D001","path":"cleanroom/review_packets/STAGE7_QSPEC_CANDIDATE_V001/STAGE7_PACKET_MANIFEST_V001.sha256","seal_basis":"matrix-ledger-preflight","sha256":"9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311"},{"byte_length":78794,"id":"D002","path":"cleanroom/review_packets/STAGE7_QSPEC_CANDIDATE_V001/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md","seal_basis":"packet-manifest:9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311","sha256":"aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a"},{"byte_length":7057,"id":"D003","path":"archive/supervision/A32_FREEZE_V002_RATIFIED_2026-07-28.md","seal_basis":"matrix-ledger:canonical-root-manifest","sha256":"32dbfc33b4f07407903ec014627ea64de57b5b1a6dc017dd27c6504729c3a327"},{"byte_length":7207,"id":"D004","path":"archive/supervision/A32_FREEZE_DRAFT_V000_2026-07-28.md","seal_basis":"matrix-ledger:canonical-root-manifest","sha256":"13faf0bc9a455590bd99d1a40587d798bc558e87aa1d1bc6dcf6778731138123"},{"byte_length":4526,"id":"D005","path":"archive/supervision/A32_MASKING_DISPOSITION_PRINCIPAL_DECISION_2026-07-30.md","seal_basis":"matrix-ledger:canonical-root-manifest","sha256":"d7153b91039974af15ab88fa6698e0573a0113fa826aa4f4ba9651b2277467bc"},{"byte_length":5129,"id":"D006","path":"archive/supervision/SLOT18_ADMISSIBILITY_PRINCIPAL_DECISION_2026-07-30.md","seal_basis":"matrix-ledger:canonical-root-manifest","sha256":"a132f4b2421610c7df4e9a8746286999b31672f1f2d805588ed3f1ad81ad6259"},{"byte_length":16593,"id":"D007","path":"cleanroom/BID_CONSOLIDATED_HOSTILE_AUDIT_MATRIX_V005.md","seal_basis":"matrix-ledger-preflight:bc6c3e496ffd6e8d06cc3237e47a6a02b76faaa88b63b0ffb38684971c2d1362","sha256":"78f6bb08b7ae89d700cf84a19ebf8e62fa489a4ec6762429ac46d027538cbfe3"},{"byte_length":24108,"id":"D008","path":"cleanroom/BID_FULL_STACK_REVIEW_LEDGER_V003.md","seal_basis":"matrix-ledger-preflight:bc6c3e496ffd6e8d06cc3237e47a6a02b76faaa88b63b0ffb38684971c2d1362","sha256":"c09f2c246c48ddfd0df127da26a22f08ba9ffd44f5c2118c178a0a5eba5d00e8"},{"byte_length":51952,"id":"D009","path":"cleanroom/STAGE8_TASK6_LP_MATRIX_LEDGER_LANE3_V001.md","seal_basis":"sidecar","sha256":"bc6c3e496ffd6e8d06cc3237e47a6a02b76faaa88b63b0ffb38684971c2d1362"},{"byte_length":18647,"id":"D010","path":"cleanroom/STAGE8_TASK6_LP_MATRIX_LEDGER_REVIEW_DARIO_V001.md","seal_basis":"sidecar","sha256":"a83289e67615d6faa2c1c942105ee6b595034f78d31fcf4e16ac5366fd1d7743"},{"byte_length":6045,"id":"D011","path":"cleanroom/STAGE8_TASK6_A21_OPEN_LEG_DISPOSITION_LANE2_V001.md","seal_basis":"sidecar","sha256":"414067e25dbae39f7767d57144c953a0f98bb11d4c34178ec70097efabc0ebf7"},{"byte_length":61791,"id":"D012","path":"cleanroom/STAGE8_TASK6_A25_A27_SCOPING_LANE2_V003.md","seal_basis":"sidecar","sha256":"74bbb7aa971554f83d5ce2eb38710b6aae38d340055ab31eca1c23379bc685da"},{"byte_length":27458,"id":"D013","path":"cleanroom/STAGE8_TASK6_RA25_2_RA27_1_FINITE_CERTS_LANE3_V001.md","seal_basis":"sidecar","sha256":"7a07d3b8ac66baa130c772d78d84ae163fb54ae082da0c071341580a9771a091"},{"byte_length":78368,"id":"D014","path":"cleanroom/STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V005.md","seal_basis":"sidecar","sha256":"76589e94bb4af318880c61c3d677dc2518add8480100a7afaf675e4dd3a394a8"},{"byte_length":197462,"id":"D015","path":"cleanroom/STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V012.md","seal_basis":"sidecar","sha256":"382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504"},{"byte_length":20423,"id":"D016","path":"cleanroom/STAGE8_TASK6_SPEC_V005_INTEGRATION_ADDENDUM_DARIO_V001.md","seal_basis":"sidecar","sha256":"d17c5e79986bea431dec0b572019096f9c059bcc43876fda9134abc96ce0f260"},{"byte_length":2921,"id":"D017","path":"archive/supervision/DECISION_RD22_BUILD_AUTHORIZED_2026-08-07.md","seal_basis":"sidecar","sha256":"ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340"},{"byte_length":28142,"id":"D018","path":"cleanroom/STAGE8_TASK6_ENVELOPE_FORMALIZATION_MAP_LANE2_V001.md","seal_basis":"sidecar","sha256":"e85a6113e5b45624d19f987ae2603f63ac418df10f33669cc6a44742e5918ed5"},{"byte_length":12422,"id":"D019","path":"cleanroom/STAGE8_TASK6_V012_ROW_CITATION_CODEX2_V001.md","seal_basis":"sidecar","sha256":"135424d187bec7108041b6d437be35a197c2920ea357559f0058fd1486e9f335"},{"byte_length":20754,"id":"D020","path":"cleanroom/STAGE8_TASK6_V012_CONFIRM_DARIO_V001.md","seal_basis":"sidecar","sha256":"2a2194211ff7e31187682b3d0a1d601b7ae736f522e21eaa7d00c4be8799dfe4"},{"byte_length":7939,"id":"D021","path":"cleanroom/STAGE8_TASK6_BOUNDARY_REPIN_CODEX2_V001.md","seal_basis":"sidecar","sha256":"d3fc9442a6574072707a69841b45678bfaaf8b1a4d5b3c2b6b0befc18549a3cc"},{"byte_length":2683,"id":"D022","path":"archive/supervision/CERTIFICATION_FIRST_LAWFUL_PASS_2026-08-08.md","seal_basis":"sidecar","sha256":"e086a5cea8bab1c2f4b70200fcbda104b89252aa91a9fb4da4b7a62a8959b47f"},{"byte_length":8593,"id":"D023","path":"cleanroom/evaluator_build_A/manifests/package_inventory.json","seal_basis":"D021:sealed-boundary-repin","sha256":"9884f019a0883f0b40dc32445645e57f3479c6bfeebc9be9141eb5c898351cbc"},{"byte_length":6551,"id":"D024","path":"cleanroom/evaluator_build_A/manifests/pins.json","seal_basis":"D023:package-inventory","sha256":"c450b90dc93dfd0ae041d939a34ffa60e9bc286a81a7ff5efd044b3474d2b101"},{"byte_length":12117,"id":"D025","path":"cleanroom/evaluator_build_A/manifests/normal.json","seal_basis":"D023:package-inventory","sha256":"b01a91c584615f2b38b847525901ffd02d61c1ab824b82a4c782e9744c8cc18e"},{"byte_length":12126,"id":"D026","path":"cleanroom/evaluator_build_A/manifests/optimized.json","seal_basis":"D023:package-inventory","sha256":"a3cee4fa8a58935814fb8df48a06341cb4a5843344dc6347d36b9a1ccd31dc29"},{"byte_length":108112,"id":"D027","path":"cleanroom/evaluator_build_A/checks/check_map.json","seal_basis":"D023:package-inventory","sha256":"280004821c532def203ae81cec35bcac26bd3ab4bdd03752f5196aa7b9c23f3d"},{"byte_length":105986,"id":"D028","path":"cleanroom/evaluator_build_A/inputs/structural_evidence_manifest.json","seal_basis":"D023:package-inventory","sha256":"20c68f9cf0eb81238bae0f0835e9d7a6e55a979818e783726b793e2cf0773bb0"},{"byte_length":3513,"id":"D029","path":"cleanroom/evaluator_build_B/rd22.verifier-manifest.v001.json","seal_basis":"sidecar","sha256":"b43912455db38ebdebe603547d8a733b294b7a16b9f5999f1180da16a7d11961"},{"byte_length":5154,"id":"D030","path":"cleanroom/evaluator_build_B/contracts/verifier_verdict.schema.json","seal_basis":"sidecar","sha256":"1674aada096dba33c7026d70fb5df8705429224b2d3e81b2911e508851bfe9e8"},{"byte_length":10997,"id":"D031","path":"cleanroom/review_packets/STAGE7_QSPEC_CANDIDATE_V001/BID_SOURCE_PARENT_CLOSURE_GATE_V003.md","seal_basis":"packet-manifest:9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311","sha256":"5c679e3741abe782688b8a75ffa1928c308775248e41af192d03976f01cb4dbf"},{"byte_length":8478,"id":"D032","path":"cleanroom/review_packets/STAGE7_QSPEC_CANDIDATE_V001/BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md","seal_basis":"packet-manifest:9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311","sha256":"0322763ac48a4428b432124a6947da81826a41f612efa6803ee9a87317929b98"},{"byte_length":6963,"id":"D033","path":"cleanroom/review_packets/STAGE7_QSPEC_CANDIDATE_V001/STAGE7_QSPEC_REVIEW_CANDIDATE_V001.md","seal_basis":"packet-manifest:9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311","sha256":"ac0b49e591bf40415bf98d29866a834b6b964634cb7fecf5e4184904550c3e81"},{"byte_length":3583,"id":"D034","path":"cleanroom/review_packets/STAGE7_QSPEC_CANDIDATE_V001/BID_FIRST_OPENING_INTERVAL_DERIVATION_V001.md","seal_basis":"packet-manifest:9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311","sha256":"7471988138233218430c6b6dd07b39f33508a75907557723654dbc712c0c4476"},{"byte_length":8862,"id":"D035","path":"cleanroom/review_packets/STAGE7_QSPEC_CANDIDATE_V001/BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md","seal_basis":"packet-manifest:9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311","sha256":"b786db3adec8cc335967d49ec13b59923d67f424644f72c535b27b579dd1489f"},{"byte_length":7722,"id":"D036","path":"cleanroom/review_packets/STAGE7_QSPEC_CANDIDATE_V001/BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md","seal_basis":"packet-manifest:9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311","sha256":"949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd"},{"byte_length":3571,"id":"D037","path":"cleanroom/review_packets/STAGE7_QSPEC_CANDIDATE_V001/BID_MONOIDAL_EXTENSIVITY_DERIVATION_V001.md","seal_basis":"packet-manifest:9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311","sha256":"451550c3825288d699db35c7289e408e8314ad042450253b58f32722c4ead46b"},{"byte_length":2389,"id":"D038","path":"cleanroom/review_packets/STAGE7_QSPEC_CANDIDATE_V001/R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_RESULT_V001.md","seal_basis":"packet-manifest:9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311","sha256":"e60aec3c44cfc5f1ef5715d3445e53783b0185ef93e54d94e442ff1df2ae9b59"},{"byte_length":5414,"id":"D039","path":"cleanroom/FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V001.md","seal_basis":"packet-v011:pinned-inherited-authority","sha256":"9894228202a4f2d53f8ef2eec3273401b773e0828e0ef04b40db1a03dae1138a"},{"byte_length":7250,"id":"D040","path":"cleanroom/PRIMITIVE_RECORD_ACTION_CHARACTER_BRIDGE_GATE_V002.md","seal_basis":"packet-v011:pinned-inherited-authority","sha256":"fc3e44f0ce78955c3c3ecbce57a901ca5f2770728b051052cc3ea638bcf3acdf"},{"byte_length":2751,"id":"D041","path":"program/primitive_comparison_group_provenance_gate_v001.md","seal_basis":"packet-v011:pinned-inherited-authority","sha256":"baa5f8150de019ed36fa9f946f8fc798aa5f272f1aefb3ea4be0ce66e7e09483"},{"byte_length":2126,"id":"D042","path":"program/minimal_public_carrier_principle_v001.md","seal_basis":"packet-v011:pinned-inherited-authority","sha256":"43f295a776ea1a789a1bb24d01fe3c068700e1c5cc823056a8f8e9a5d9a2f436"},{"byte_length":4323,"id":"D043","path":"program/primitive_action_character_carrier_completion_v001.md","seal_basis":"packet-v011:pinned-inherited-authority","sha256":"9b2c0b93fb4bd2fbb34a8e9f5adb578b9b29422ea7adc8849ff425ad4139e23a"},{"byte_length":4157,"id":"D044","path":"program/primitive_complete_boundary_transition_functional_principle_v001.md","seal_basis":"packet-v011:pinned-inherited-authority","sha256":"698051f21310c029f6e3b52aa49b3e129b94240214c48ffa75be6be00ca5e0a6"},{"byte_length":3187,"id":"D045","path":"program/primitive_boundary_native_record_CAR_functional_principle_v001.md","seal_basis":"packet-v011:pinned-inherited-authority","sha256":"099440a4ca77d022ffb7a1977834c83155c9b53e3958fb56efa926e16c5ba0b7"},{"byte_length":3241,"id":"D046","path":"program/primitive_physical_charged_dirac_trace_completion_v001.md","seal_basis":"packet-v011:pinned-inherited-authority","sha256":"fe9f4e157e9beda7e8351575add717d28e10c49f17dcb0a0fc8dc50a7e2cabee"},{"byte_length":2368,"id":"D047","path":"program/primitive_inclusive_record_spectral_kernel_principle_v001.md","seal_basis":"packet-v011:pinned-inherited-authority","sha256":"b8c03857602e6f2bc5d07b0b30d2a335d721e49699c5951f9486f3b2a7bf4c32"},{"byte_length":329948,"id":"D048","path":"program/results/primitive_same_cell_discrete_parent_action_v001.json","seal_basis":"packet-v011:pinned-inherited-authority","sha256":"3f5991ef3ca62bc2166b73f6ae61c69a22648639af16021f0db458c49f81a262"}],"row_bindings":[{"documents":["D001","D002","D039","D040","D041","D042","D043","D044","D045","D046","D047","D048"],"row":"A01"},{"documents":["D002","D003","D004","D005","D006"],"row":"A02"},{"documents":["D002","D003","D004","D005","D006"],"row":"A03"},{"documents":["D002"],"row":"A04"},{"documents":["D002"],"row":"A05"},{"documents":["D002"],"row":"A06"},{"documents":["D002"],"row":"A07"},{"documents":["D002"],"row":"A08"},{"documents":["D002"],"row":"A09"},{"documents":["D002"],"row":"A10"},{"documents":["D002"],"row":"A11"},{"documents":["D002"],"row":"A12"},{"documents":["D002"],"row":"A13"},{"documents":["D002"],"row":"A14"},{"documents":["D002"],"row":"A15"},{"documents":["D002"],"row":"A16"},{"documents":["D002"],"row":"A17"},{"documents":["D002"],"row":"A18"},{"documents":["D002"],"row":"A19"},{"documents":["D002"],"row":"A20"},{"documents":["D002","D011","D031","D032"],"row":"A21"},{"documents":["D002"],"row":"A22"},{"documents":["D002","D014","D033"],"row":"A23"},{"documents":["D002","D014","D031","D034","D035","D036","D037"],"row":"A24"},{"documents":["D002","D012","D013","D036"],"row":"A25"},{"documents":["D002"],"row":"A26"},{"documents":["D002","D012","D013","D038"],"row":"A27"},{"documents":["D002","D014","D031","D033"],"row":"A28"},{"documents":["D002"],"row":"A29"},{"documents":["D007","D008","D015","D016","D017","D018","D019","D020","D021","D022","D023","D024","D025","D026","D027","D028","D029","D030"],"row":"A35"}],"schema":"rd22.lineage-v2-baseline.v001"}
```

Generation transcript:

```text
GENERATOR_OK documents=48 rows=30 missing=0
document_root=52c5e039e178102b1c17c4939dcec42e8e06d9329acb5dd95ce607c594c3a0f8
manifest_sha256=59e05791f7d68a3c1e8185ca4994d970edaff2d327b2142cc9cddfe101b60ef2
manifest_bytes=13061
```

No cited row document lacked a current content-addressed version. `D007` and `D008` have no local sidecars; their exact hashes are sealed as load-bearing preflight pins in `D009`, and `D008` is independently carried through the current evaluator pin chain. Packet members bind through `D001`; the ten A01 authorities bind through the pinned-authority table in `D002`; Builder A package files bind through `D023`, whose hash is sealed in `D021`.

## 3. Rerun discipline

The unchanged row criteria are the exact A01–A29 and A35 cells in `D007`. The old verdict source is the reviewed correction `D010`, which replaces the provisional A25/A27 `FAIL` labels with `BLOCKED` without changing the criteria. For every row, the rerun asked whether every original conjunct has a current witness in that row's manifest binding. A status string, implementation claim, or partial certificate was not accepted in place of the requested object or result.

Verdict meanings remain:

```text
PASS    every row conjunct is exhibited or derived on V2;
FAIL    a row conjunct is structurally negated on V2;
BLOCKED a demanded object, proof package, or executable evidence carrier is absent.
```

## 4. Full thirty-row board

Every `Dxxx` reference below resolves to a full source path and digest in the generated manifest. The evidence cell is therefore a content-addressed citation, not narrative.

| Row | Old | V2 | Evidence citation | Recomputed disposition |
|---|---|---|---|---|
| A01 | PASS | PASS | D001, D002, D039–D048 | all ten inherited authority bytes match their V011 pins |
| A02 | PASS | PASS | D002–D006 | target firewall and A32 amendments remain compatible and target-free |
| A03 | PASS | PASS | D002–D006 | result, proof, and seal flags remain false |
| A04 | PASS | PASS | D002 | object carriers remain distinct with typed canonical maps |
| A05 | PASS | PASS | D002 | comparison quotient remains well-defined, continuous, and faithful |
| A06 | PASS | PASS | D002 | rooted-star and `4+3` remain disclosed premise consequences |
| A07 | PASS | PASS | D002 | category, labels, morphisms, composition, and forgetful functors remain typed |
| A08 | PASS | PASS | D002 | cell carriers, reversal, gauge action, and `J0–J2` remain consistent |
| A09 | PASS | PASS | D002 | full positive Hermitian competitor class still precedes the hypothesis |
| A10 | PASS | PASS | D002 | the displayed Gram derivation still gives the three identity metrics |
| A11 | PASS | PASS | D002 | complete differential hostile family remains admitted |
| A12 | PASS | PASS | D002 | involution, covariance, and coefficient swap remain derived |
| A13 | PASS | PASS | D002 | public colimit still gives `[c:d]=[1:1]` without magnitude |
| A14 | PASS | PASS | D002 | frozen reduction still leaves one normalized equivalence class |
| A15 | PASS | PASS | D002 | differential naturality remains typed and full-B substitution refused |
| A16 | PASS | PASS | D002 | only declared equivalences are used |
| A17 | PASS | PASS | D002 | weighted adjoint remains the directional difference |
| A18 | PASS | PASS | D002 | algebra, ideal, completion, and representation scopes remain separated |
| A19 | PASS | PASS | D002 | curvature paths, gauge covariance, and logarithm domains remain exact |
| A20 | PASS | PASS | D002 | universal lower order remains separated from represented exact order |
| A21 | PASS | PASS | D002, D011, D031, D032 | declared-branch Dirac/CPT/CP-axial audit remains closed; the residual open leg was NOT_OF_RECORD and closed without board change |
| A22 | PASS | PASS | D002 | postulate, incompatibility theorem, and generated-coefficient buckets remain distinct |
| A23 | BLOCKED | BLOCKED | D002, D014, D033 | complete charged normalized amplitude and action normalization remain absent; V005 has 0/18 filled slots |
| A24 | BLOCKED | BLOCKED | D002, D014, D031, D034–D037 | durable endpoint, uniform zero-free physical amplitude, connected preparation, and thermodynamic domain remain absent |
| A25 | BLOCKED | BLOCKED | D002, D012, D013, D036 | RA25-2 is now complete, but RA25-1, RA25-3, RA25-4, and RA25-5 remain absent |
| A26 | PASS | PASS | D002 | Moore–Penrose flux lift remains uniquely minimum-norm on `im d1` |
| A27 | BLOCKED | BLOCKED | D002, D012, D013, D038 | RA27-1 is now proven, but RA27-2 through RA27-6 remain absent |
| A28 | BLOCKED | BLOCKED | D002, D014, D031, D033 | complete interacting downstream Qspec remains absent; V005 remains 0/18 filled |
| A29 | PASS | PASS | D002 | loop preregistration remains internally consistent and immutable |
| A35 | BLOCKED | BLOCKED | D007, D008, D015–D030 | machinery exists, but 55 structural envelopes and 3 structural fixture observations remain absent; only one row is certified |

Board arithmetic:

```text
PASS_SET = {A01-A22,A26,A29}
FAIL_SET = {}
BLOCKED_SET = {A23,A24,A25,A27,A28,A35}
24 + 0 + 6 = 30
```

## 5. Candidate flips adjudicated from the repair bytes

### 5.1 A25 — no flip

`D013` supplies the exact RA25-2 joint-fixed-space census: `Fix_L` is five-dimensional and its whole projectivization is `CP^4`. Its own consequence board states that C25.1, C25.3, and C25.4 remain untouched. `D012` defines the complete PASS condition as RA25-1 + RA25-2 + RA25-3 + RA25-4 + RA25-5. Importing the held-out certificate into V2 therefore closes one conjunct, not the row.

Named V2 blocker:

```text
missing_A25_V2 =
  FirstOpeningPrepCert_L
  + PreparationExclusionAndUniquenessCert_L
  + connected refinement-addressed response/thermodynamic subject
  + UniformLocalityCert for the actual response kernel.
```

### 5.2 A27 — no flip

`D013` supplies the exact six-by-six Lorentzian Hodge matrix and proves `J_star^2=-I_6`, closing RA27-1/C27.2. The same sealed certificate expressly leaves physical `Ref/J_ref`, response naturality, boundary/contact subextensivity, and coefficient invariance untouched. `D012` requires RA27-1 through RA27-6 for PASS.

Named V2 blocker:

```text
missing_A27_V2 =
  RA27-2 refinement grammar
  + RA27-3 physical realization
  + RA27-4 exactly commuting response squares
  + RA27-5 coefficient-boundary certificate
  + RA27-6 cellulation-independent coefficient theorem.
```

### 5.3 A35 — machinery repair confirmed, row flip not earned

The old missing-object declaration is exactly `D009` bytes `[43926,44103)`:

```text
missing_A35 :=
  content-addressed optimization-safe parent runner
  + independent verifier/evaluator
  + an explicit executable mapping for every V003/A35 blocker.
```

Those machinery bytes now exist:

| Added V2 object | Exact supplied bytes |
|---|---|
| parent | D023 inventory row: 73959 bytes, `a09f333a133deb28f57f4dda5b78fd54f708c553b0c5ec1df98d3682c79100cc` |
| producer | D023 inventory row: 46742 bytes, `3c27890533eebe485f1f41688a7268d3898e6b1582ce933164113db28ba737a8` |
| executable mapping | D027 `[0,108112)`, 66 descriptors = 63 blocker IDs + 3 discrepancy IDs |
| normal/optimized manifests | D025 `[0,12117)` and D026 `[0,12126)` |
| independent verifier instance | D029 `[0,3513)`, 14 members, root `2294dfe53a77a6069913822616bedffb4e16d062b1e968deeb727552f9f906db` |
| end-to-end certification | D022 `[0,2683)`, run 033 and one independently replayed PASS |

The unchanged A35 criterion in D007 is stronger than the old absence summary: it requires the evaluator to reproduce/reject named regression subjects and execute the blocker checks. Current D028 records only `1/56` structural envelopes available and `0/3` structural fixture observations. D022 says, in sealed words, that the other 55 structural rows and three fixture observations lack machine evidence and that nothing in the certification extends beyond one row. The two mode children consequently produced `1 PASS / 55 FAIL(INPUT_INTEGRITY) / 10 NOT_RUN_GATE`; the independent verifier reported the same 58 evidence absences.

Treating those fail-closed refusals as proof of the unavailable regression outcomes would weaken “reproduce and reject” to “detect absent input.” The machinery repair is real, but the row remains BLOCKED on:

```text
missing_A35_V2 =
  55 structural evidence envelopes
  + 3 structural fixture observations
  + independent replay of the resulting criterion outcomes.
```

This disposition does not deny the certified V009-06 PASS. It keeps that PASS exactly at n=1.

### 5.4 Physics-gap rows — no flips

`D014` remains `SLOTS = 18 (0 filled / 18 TYPE-U)`. In particular, the normalized interacting amplitude, uniform zero-free domain, connected preparation/thermodynamic subject, complete interacting Qspec, charged pole/threshold, and Thomson transport remain uninhabited. D033 and D031 independently preserve the same incomplete-completion flags. A23, A24, and A28 therefore remain BLOCKED without evaluating any physical quantity.

## 6. Tool execution, pin closure, and battery

The baseline generator/validator was executed against the actual sources. It resolved 48 documents, verified every byte length and SHA-256 against its named seal basis, established 30 unique row bindings, and found zero missing current versions. It emitted the canonical manifest and root displayed in §2. No persistent tool was shipped and no evaluator child was launched.

Pin closure checks:

- every manifest document ID is unique;
- every row binding names an existing document ID;
- all 30 required rows occur exactly once;
- all sidecar-backed entries match their sidecars;
- every packet member matches D001;
- every A01 authority matches D002's pin table;
- every Builder A package member matches D023;
- no unsealed root V011 is included;
- no superseded assembly, scoping, evaluator-spec, or Builder B instance is included.

F_PLDEC and the gates remain clean: no member binding, fixed-point execution, end test, numeric evaluation of a physical quantity, or comparison to a measured constant occurred. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false` remain unchanged.

Because six rows remain non-PASS:

```text
passed_A01_A29_and_A35 = false
SPEC_SEAL = false
```

BASELINE = 48 documents, generated, pinned
BOARD = 24 PASS / 0 FAIL / 6 BLOCKED (old 24/0/6)
FLIPS = none (A25/A27 certificates partial; A35 machinery repaired but 58 evidence carriers remain absent)
SPEC_SEAL = false
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
