# STAGE 8 / TASK 6 / BUILD A — EVIDENCE PAYLOAD ASSEMBLY (D1) — LANE 2 V001

Lane: Lane 2, Builder A  
Relay: PASTE 652 / D1 evidence assembly  
Disposition: sealed corpus bytes cited and copied; no executable evidence or observation authored  
Authority claimed: none

```text
REGISTER_HEAD = Q-590 (satisfied by registrar-sealed cleanroom snapshot)
REGISTER_SNAPSHOT_SHA256 = 4169c03829a4059a096a346170c6a338c69fd906769fdb8a015faa9e58cc5c8c
SPEC_V005_SHA256 = f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b
CHECK_MAP_SHA256 = 034ebf3e071051d25d5b7f8871a03193da5bc9ab16a7c07c7cae1bbb8f467e26
EXECUTED_MATRIX_SHA256 = bc6c3e496ffd6e8d06cc3237e47a6a02b76faaa88b63b0ffb38684971c2d1362
SEARCH_SCOPE_MEMBERS = 120
SEARCH_SCOPE_SHA256 = 691e871e4b2a13f09cdf5481abb1c7a32c05ba9426bf657436a5f5f2597db032
PAYLOAD_FILES = 10 (byte-identical sealed-source copies)
STRUCTURAL_CHECKS = 56
STRUCTURAL_FIXTURE_OBSERVATIONS = 3
AVAILABLE_EXECUTABLE_RECORDS = 0
AVAILABLE_FIXTURE_OBSERVATIONS = 0
CHAIN_INVOKED = false
```

## 1. Preflight and governing distinction

| Check | Result |
|---|---|
| Register head | `REGISTER_HEAD_SNAPSHOT_Q590_2026-08-07.md` rehashed to the supplied `4169c038…`; its full entry states `HEAD = Q-590`. |
| Output collision | Artifact and sidecar absent in both cleanroom and archive immediately before creation. |
| V005 | Rehashed to `f8d1a7dc…` before use. |
| Check map | Rehashed to `034ebf3e…`; census 66 = 56 STRUCTURAL + 10 GATED-EXECUTION. |
| Prior evidence manifest | Rehashed before assembly; census 56 + 3, all unavailable. |
| Executed matrix | Rehashed to `bc6c3e49…`; its board contains 24 human-audited PASS rows. |
| Packet | `STAGE7_PACKET_MANIFEST_V001.sha256` rehashed to `9d35f4ed…`; `shasum -c` returned `OK` for all 113 members. |

The relay's distinction is decisive: a displayed proposition can be cited as sealed bytes, but the producer accepts a structural check only through the complete machine envelope

```text
{descriptor_sha256, input_files, input_root_sha256, invocations}
```

with every declared opcode invocation present and bound to the descriptor. The 24 matrix PASS displays locate useful sealed statements and spans; they do not contain that envelope, the descriptor hash binding, or the demanded grammar/certificate/proof-index objects. Converting those displays into fresh opcode arguments would author evidence and violate this relay. They therefore remain partial citations, never runtime PASS records.

The same rule applies to fixtures. V005 §10 seals expected records and symbolic subjects, but an expected record is not an observation. No sealed `observed_verdict_fields` plus `observed_evidence_sha256s` record was found for any of the three structural fixtures.

## 2. Payload custody — copied bytes only

Each payload filename begins with the SHA-256 of the whole source. Every copy was byte-compared with the source after copying. The source span is the whole file here; narrower per-record citation spans are recorded in `structural_evidence_manifest.json`.

| Content-addressed payload | Source | Span | Bytes / SHA-256 |
|---|---|---:|---|
| `0322763a…--BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md` | packet CPT construction | `[0,8478)` | 8478 / `0322763ac48a4428b432124a6947da81826a41f612efa6803ee9a87317929b98` |
| `414067e2…--STAGE8_TASK6_A21_OPEN_LEG_DISPOSITION_LANE2_V001.md` | sealed A21 disposition | `[0,6045)` | 6045 / `414067e25dbae39f7767d57144c953a0f98bb11d4c34178ec70097efabc0ebf7` |
| `5c679e37…--BID_SOURCE_PARENT_CLOSURE_GATE_V003.md` | packet source-parent gate | `[0,10997)` | 10997 / `5c679e3741abe782688b8a75ffa1928c308775248e41af192d03976f01cb4dbf` |
| `76589e94…--STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V005.md` | sealed assembly V005 | `[0,78368)` | 78368 / `76589e94bb4af318880c61c3d677dc2518add8480100a7afaf675e4dd3a394a8` |
| `9d35f4ed…--STAGE7_PACKET_MANIFEST_V001.sha256` | sealed packet manifest | `[0,13786)` | 13786 / `9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311` |
| `a83289e6…--STAGE8_TASK6_LP_MATRIX_LEDGER_REVIEW_DARIO_V001.md` | sealed matrix review | `[0,18647)` | 18647 / `a83289e67615d6faa2c1c942105ee6b595034f78d31fcf4e16ac5366fd1d7743` |
| `aa7c6d49…--BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` | packet V011 | `[0,78794)` | 78794 / `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` |
| `bc6c3e49…--STAGE8_TASK6_LP_MATRIX_LEDGER_LANE3_V001.md` | sealed executed matrix | `[0,51952)` | 51952 / `bc6c3e496ffd6e8d06cc3237e47a6a02b76faaa88b63b0ffb38684971c2d1362` |
| `c09f2c24…--BID_FULL_STACK_REVIEW_LEDGER_V003.md` | sealed blocker census | `[0,24108)` | 24108 / `c09f2c246c48ddfd0df127da26a22f08ba9ffd44f5c2118c178a0a5eba5d00e8` |
| `f8d1a7dc…--STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md` | sealed V005 | `[0,162641)` | 162641 / `f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b` |

`AUTHORED_BYTES = zero` refers to payload content: all ten payloads are exact source copies. The evidence manifest and this custody certificate are assembly metadata and make no claim to be pre-existing corpus bytes.

## 3. Bounded M-2 search

The search root contains exactly:

- 113 hash-verified packet members;
- the packet manifest itself; and
- six separately sealed workspace records: V005, the blocker ledger, executed matrix, matrix review, A21 disposition, and assembly V005.

Its content root is `691e871e4b2a13f09cdf5481abb1c7a32c05ba9426bf657436a5f5f2597db032`. Every record stores this root and `scope_members=120`.

For every check, queries included its ID, descriptor SHA-256, the literal runtime field `invocations`, and up to three distinctive demanded identifiers. Fixture queries included the fixture ID, both observation-field names, and every expected-record key. Four false-negative modes ran:

1. `fixed_string` — literal search, never regex interpretation;
2. `whitespace_normalized` — wrapped clauses and Markdown spacing collapsed;
3. `self_reference_scope` — hits classified as `sealed_packet`, `review_display`, or `requirements`; requirements/review repetition cannot become an executable record;
4. `hyphen_space_underscore` — `-`, `_`, and space variants normalized jointly.

The manifest preserves per-query counts in all modes. `complete_envelope_hits=[]` for all 59 records. Eight check records retain 11 narrow partial-display citations; all three fixtures retain their exact §10 subject/expected-row span with role `SPEC_FIXED_SUBJECT_NOT_OBSERVATION`. Partial citations do not change `available=false`.

In the tables below, `F/W/S/H` is the sum of fixed / whitespace / admissible sealed-packet-scope / hyphen-variant hits for that record's displayed queries. Every search has scope 120 and exact-envelope count zero.

## 4. Per-check evidence table — 56 structural rows

| Check ID | Descriptor | Partial cited bytes | M-2 `F/W/S/H` | Disposition |
|---|---|---|---:|---|
| `C-B-V008-01` | `50df72694acd…` | — | `5/5/0/5` | ABSENT_OF_RECORD |
| `C-B-V008-02` | `baf8cbf40f08…` | — | `4/4/0/4` | ABSENT_OF_RECORD |
| `C-B-V008-03` | `dc9d04dc876b…` | — | `4/4/0/4` | ABSENT_OF_RECORD |
| `C-B-V008-04` | `079a8e8542d0…` | matrix display | `26/26/17/48` | ABSENT_OF_RECORD |
| `C-B-V008-05` | `bb89abab6d5b…` | matrix + V011 | `30/30/12/30` | ABSENT_OF_RECORD |
| `C-B-V008-06` | `17d16a5a73a3…` | — | `4/4/0/4` | ABSENT_OF_RECORD |
| `C-B-V008-07` | `c2f640d9c5c0…` | A21 disposition | `56/56/92/195` | ABSENT_OF_RECORD |
| `C-B-V008-08` | `d2d5136b2e65…` | — | `13/13/0/13` | ABSENT_OF_RECORD |
| `C-B-V008-09` | `35cd71600261…` | — | `17/17/0/17` | ABSENT_OF_RECORD |
| `C-B-V008-10` | `408682420b77…` | — | `4/4/0/4` | ABSENT_OF_RECORD |
| `C-B-V008-11` | `2e6dca881e9a…` | — | `70/70/0/71` | ABSENT_OF_RECORD |
| `C-B-V009-01` | `43aeb544d137…` | matrix display | `18/18/13/31` | ABSENT_OF_RECORD |
| `C-B-V009-02` | `11dcaadba827…` | — | `18/18/0/18` | ABSENT_OF_RECORD |
| `C-B-V009-03` | `d60aa934b040…` | matrix display | `17/17/14/32` | ABSENT_OF_RECORD |
| `C-B-V009-04` | `338643e8b964…` | — | `9/9/0/9` | ABSENT_OF_RECORD |
| `C-B-V009-05` | `2e3b41c21066…` | — | `4/4/0/4` | ABSENT_OF_RECORD |
| `C-B-V009-06` | `060db9e9bbb0…` | — | `4/4/0/4` | ABSENT_OF_RECORD |
| `C-B-V009-07` | `6b110e781374…` | — | `17/17/0/17` | ABSENT_OF_RECORD |
| `C-B-V009-08` | `3902b83bd107…` | — | `4/4/0/4` | ABSENT_OF_RECORD |
| `C-B-V009-09` | `aba2f66fdfc3…` | — | `4/4/0/4` | ABSENT_OF_RECORD |
| `C-B-V009-10` | `700b5dc75442…` | — | `13/13/0/16` | ABSENT_OF_RECORD |
| `C-B-V009-11` | `57525498655c…` | — | `4/4/0/4` | ABSENT_OF_RECORD |
| `C-B-V009-12` | `a980cc09f4c3…` | — | `4/4/0/4` | ABSENT_OF_RECORD |
| `C-B-V009-13` | `d95f068088b7…` | — | `13/13/0/13` | ABSENT_OF_RECORD |
| `C-B-V010-02` | `4b9f25f383f7…` | — | `12/12/0/12` | ABSENT_OF_RECORD |
| `C-B-V010-03` | `a5255d5f6080…` | — | `11/11/0/13` | ABSENT_OF_RECORD |
| `C-B-V010-04` | `1383ce2c60d9…` | A21 + matrix | `143/143/101/145` | ABSENT_OF_RECORD |
| `C-B-V010-05` | `86bb63efda92…` | — | `4/4/0/4` | ABSENT_OF_RECORD |
| `C-B-V010-06` | `0a2b9c3fd581…` | — | `12/12/0/12` | ABSENT_OF_RECORD |
| `C-B-V010-07` | `e9291f46d722…` | — | `4/4/0/4` | ABSENT_OF_RECORD |
| `C-B-V010-08` | `40a655550915…` | matrix display | `23/23/13/25` | ABSENT_OF_RECORD |
| `C-B-V010-09` | `347b4b28baee…` | — | `4/4/0/4` | ABSENT_OF_RECORD |
| `C-B-V010-10` | `5ed6ddbbc6e9…` | — | `7/7/0/7` | ABSENT_OF_RECORD |
| `C-B-V010-11` | `bf7a6f71a6d9…` | — | `4/4/0/4` | ABSENT_OF_RECORD |
| `C-B-V010-12` | `f347a216b3cc…` | — | `4/4/0/4` | ABSENT_OF_RECORD |
| `C-B-V010-13` | `aacc7f2ca5f4…` | — | `22/22/0/22` | ABSENT_OF_RECORD |
| `C-B-V010-14` | `2713fa74adfb…` | — | `15/15/0/15` | ABSENT_OF_RECORD |
| `C-B-V011-MR-01` | `37631f4192bf…` | — | `14/14/0/14` | ABSENT_OF_RECORD |
| `C-B-V011-MR-02` | `2d1c29184171…` | — | `11/11/0/11` | ABSENT_OF_RECORD |
| `C-B-V011-MR-03` | `77d529347101…` | — | `4/4/0/4` | ABSENT_OF_RECORD |
| `C-B-V011-MR-04` | `67e345c05d46…` | — | `12/12/0/20` | ABSENT_OF_RECORD |
| `C-B-V011-MR-05` | `c8e2e2575f2f…` | — | `11/11/0/11` | ABSENT_OF_RECORD |
| `C-B-V011-MR-06` | `71f1105aba41…` | — | `11/11/0/11` | ABSENT_OF_RECORD |
| `C-B-V011-SP1-01` | `8b0e56c38538…` | — | `5/5/0/5` | ABSENT_OF_RECORD |
| `C-B-V011-SP1-02` | `8442d79f28b2…` | — | `10/10/0/10` | ABSENT_OF_RECORD |
| `C-B-V011-SP1-03` | `146dd896e7d7…` | — | `4/4/0/4` | ABSENT_OF_RECORD |
| `C-B-V011-SP1-05` | `927fbaf7df55…` | — | `10/10/0/10` | ABSENT_OF_RECORD |
| `C-B-V011-SP1-06` | `2c18b25abb5a…` | — | `54/54/0/55` | ABSENT_OF_RECORD |
| `C-B-V011-SP1-07` | `81bf06483070…` | — | `12/12/0/12` | ABSENT_OF_RECORD |
| `C-B-V011-SP1-09` | `8173f50e80b3…` | — | `12/12/0/12` | ABSENT_OF_RECORD |
| `C-B-V011-SP2-01` | `d19cc8e162c6…` | — | `5/5/0/5` | ABSENT_OF_RECORD |
| `C-B-V011-SP2-02` | `985212c72476…` | matrix + CPT | `123/123/97/124` | ABSENT_OF_RECORD |
| `C-B-V011-SP2-04` | `4c6fef553237…` | — | `23/23/1/25` | ABSENT_OF_RECORD |
| `C-B-V011-SP2-05` | `ee29eb19c512…` | — | `10/10/0/10` | ABSENT_OF_RECORD |
| `C-B-V011-SP2-07` | `d0454d55596e…` | — | `9/9/0/11` | ABSENT_OF_RECORD |
| `C-D-A35-02-QUASIFREE-CAR-LIFT` | `b3c2a14de2ae…` | — | `4/4/0/4` | ABSENT_OF_RECORD |

For every row, the missing object list is exactly the complete executable binding for that ID and the runtime envelope `{descriptor_sha256,input_files,input_root_sha256,invocations}`. Where a partial citation exists, its source path, source SHA-256, exact byte span, payload path, and payload SHA-256 are stored in the manifest record.

## 5. Structural fixture observations — 3 rows

| Fixture ID | Fixture-spec digest | Cited sealed bytes | M-2 `F/W/S/H` | Disposition |
|---|---|---|---:|---|
| `FX-A35-03-C-FAMILY` | `9f951cb11fbc…` | exact V005 §10 subject/expected row | `7/7/2/8` | ABSENT_OF_RECORD |
| `FX-A35-04-TAU-FAMILY` | `a91920d88d56…` | exact V005 §10 subject/expected row | `7/7/2/8` | ABSENT_OF_RECORD |
| `FX-A35-05-PRIMITIVE-THOMSON-CONFLATION` | `06ce18cbf270…` | exact V005 §10 subject/expected row | `4/4/0/5` | ABSENT_OF_RECORD |

The missing objects for each are the sealed observation, `observed_verdict_fields`, and `observed_evidence_sha256s`. The spec-fixed expected fields were not copied into an observed carrier.

## 6. Complete ABSENT_OF_RECORD list

```text
C-B-V008-01 C-B-V008-02 C-B-V008-03 C-B-V008-04 C-B-V008-05
C-B-V008-06 C-B-V008-07 C-B-V008-08 C-B-V008-09 C-B-V008-10 C-B-V008-11
C-B-V009-01 C-B-V009-02 C-B-V009-03 C-B-V009-04 C-B-V009-05
C-B-V009-06 C-B-V009-07 C-B-V009-08 C-B-V009-09 C-B-V009-10
C-B-V009-11 C-B-V009-12 C-B-V009-13
C-B-V010-02 C-B-V010-03 C-B-V010-04 C-B-V010-05 C-B-V010-06
C-B-V010-07 C-B-V010-08 C-B-V010-09 C-B-V010-10 C-B-V010-11
C-B-V010-12 C-B-V010-13 C-B-V010-14
C-B-V011-MR-01 C-B-V011-MR-02 C-B-V011-MR-03 C-B-V011-MR-04
C-B-V011-MR-05 C-B-V011-MR-06
C-B-V011-SP1-01 C-B-V011-SP1-02 C-B-V011-SP1-03 C-B-V011-SP1-05
C-B-V011-SP1-06 C-B-V011-SP1-07 C-B-V011-SP1-09
C-B-V011-SP2-01 C-B-V011-SP2-02 C-B-V011-SP2-04 C-B-V011-SP2-05
C-B-V011-SP2-07 C-D-A35-02-QUASIFREE-CAR-LIFT
FX-A35-03-C-FAMILY FX-A35-04-TAU-FAMILY
FX-A35-05-PRIMITIVE-THOMSON-CONFLATION
```

This is an input-integrity disposition, not a negative mathematical verdict. At runtime the 56 unavailable check records return `FAIL` with `INPUT_INTEGRITY: STRUCTURAL_EVIDENCE_NOT_SUPPLIED`; the three unavailable structural fixtures return `FAIL` with `INPUT_INTEGRITY: STRUCTURAL_FIXTURE_EVIDENCE_NOT_SUPPLIED`.

## 7. Updated package inventory

`package_inventory.json` has 31 self-addressed rows and excludes itself. Adding its own displayed digest gives 32 delivered package files.

| Relative path | Bytes | SHA-256 |
|---|---:|---|
| `README.md` | 3516 | `13634ef622aeae92ac69e790fee5aba86b67cafdda0321b1c1f9d3382b1611c7` |
| `checks/check_map.json` | 107235 | `034ebf3e071051d25d5b7f8871a03193da5bc9ab16a7c07c7cae1bbb8f467e26` |
| `fixtures/fixture_manifest.json` | 7894 | `dc635a83fe39e62bdc2b76c8c40cfce977ac67fdaf0eede32344d0b98dabf2db` |
| `inputs/evidence/0322763ac48a4428b432124a6947da81826a41f612efa6803ee9a87317929b98--BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md` | 8478 | `0322763ac48a4428b432124a6947da81826a41f612efa6803ee9a87317929b98` |
| `inputs/evidence/414067e25dbae39f7767d57144c953a0f98bb11d4c34178ec70097efabc0ebf7--STAGE8_TASK6_A21_OPEN_LEG_DISPOSITION_LANE2_V001.md` | 6045 | `414067e25dbae39f7767d57144c953a0f98bb11d4c34178ec70097efabc0ebf7` |
| `inputs/evidence/5c679e3741abe782688b8a75ffa1928c308775248e41af192d03976f01cb4dbf--BID_SOURCE_PARENT_CLOSURE_GATE_V003.md` | 10997 | `5c679e3741abe782688b8a75ffa1928c308775248e41af192d03976f01cb4dbf` |
| `inputs/evidence/76589e94bb4af318880c61c3d677dc2518add8480100a7afaf675e4dd3a394a8--STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V005.md` | 78368 | `76589e94bb4af318880c61c3d677dc2518add8480100a7afaf675e4dd3a394a8` |
| `inputs/evidence/9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311--STAGE7_PACKET_MANIFEST_V001.sha256` | 13786 | `9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311` |
| `inputs/evidence/a83289e67615d6faa2c1c942105ee6b595034f78d31fcf4e16ac5366fd1d7743--STAGE8_TASK6_LP_MATRIX_LEDGER_REVIEW_DARIO_V001.md` | 18647 | `a83289e67615d6faa2c1c942105ee6b595034f78d31fcf4e16ac5366fd1d7743` |
| `inputs/evidence/aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a--BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` | 78794 | `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` |
| `inputs/evidence/bc6c3e496ffd6e8d06cc3237e47a6a02b76faaa88b63b0ffb38684971c2d1362--STAGE8_TASK6_LP_MATRIX_LEDGER_LANE3_V001.md` | 51952 | `bc6c3e496ffd6e8d06cc3237e47a6a02b76faaa88b63b0ffb38684971c2d1362` |
| `inputs/evidence/c09f2c246c48ddfd0df127da26a22f08ba9ffd44f5c2118c178a0a5eba5d00e8--BID_FULL_STACK_REVIEW_LEDGER_V003.md` | 24108 | `c09f2c246c48ddfd0df127da26a22f08ba9ffd44f5c2118c178a0a5eba5d00e8` |
| `inputs/evidence/f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b--STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md` | 162641 | `f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b` |
| `inputs/structural_evidence_manifest.json` | 98663 | `722f4db56fc6e77de258273f06fd1ae487b9bb0143440f73adb76747779a5cb8` |
| `inputs/subject_lineage_manifest.json` | 1510 | `e6918e0254d63671dd0fd3652290e4a0b1781abb6c4d63e81043f1d8f3327d54` |
| `manifests/normal.json` | 9172 | `7697fb8c20d8b0589247c352d93dc91e4cc6351f570a8b8ba6e739567f1dee40` |
| `manifests/optimized.json` | 9181 | `8449ac7d29ba7a1297f183949d75826e45ede86249af9940ec9e75cba5780cbe` |
| `manifests/package_inventory.json` | 5512 | `80b71e4639b248d25c87b3221db2977c9e4b92c3af6e1ebe49c93f8829da8489` |
| `parent.py` | 36986 | `f07016cb7054d3696cd6e0f7552f81e74b8ee0f35cf8b55b7bd771e633b21831` |
| `producer.py` | 39567 | `93d717df36807e66ca09919ca90157e79b016831e5200852350d8887a57c3982` |
| `schemas/check-map.schema.json` | 456 | `8e971040ca4d96161303710bc391dd322cb581983c881eaf39b1547fb4e68192` |
| `schemas/child-manifest.schema.json` | 1420 | `f5325b40cd49db94e11cc44628ec46b6ac400489d99c574642461e0b8697ef1e` |
| `schemas/child-receipt.schema.json` | 1277 | `0ce216024263ee7b2de3643fc4b44cc1a581d7a2334968da8ebdf8b9d02fa7bf` |
| `schemas/fixture-manifest.schema.json` | 1347 | `3723297f9f9e9aa5b6e16f35a3315966d49997734c223580807b916ebfc4e986` |
| `schemas/producer-output.schema.json` | 2425 | `d3e4dc5c32e265ec5a8373b734f9d277573d862c97cb563f03c3e97f55e534b3` |
| `schemas/structural-evidence.schema.json` | 351 | `5d3ec96abcec19f664665f5a1bf316a9c4fa3d95aa66b8551de8036d85f97174` |
| `schemas/terminal-ledger.schema.json` | 3920 | `5635e68e13932915f6724f7a1aa2533fa52d8cc7170be9a44f09433ae9816af5` |
| `schemas/verifier-manifest.schema.json` | 1691 | `05cb23509293da9d8a184cd48a7f6cc1c36e56c3ab4114d8548bea8824fc9d15` |
| `schemas/verifier-output.schema.json` | 1476 | `145dfdf6aefa40766b9e680dd59714ffbd94133411ea89a0e7d7aab8d6f033ad` |
| `tools/assemble_evidence.py` | 13582 | `11addee3e9e9764fee711cf4b136bca003948c152f3f04ee8ba4c1cde88cd1a4` |
| `tools/materialize.py` | 30629 | `ba3c3ae4e825f3044ae4c9e781dbe1fb096443bc3dc1603b0223c14e129957d3` |
| `tools/self_check.py` | 23114 | `d10e40432f9f995105f78f1323d586054e8ba206aaba056b0765b5ceebdb2baf` |

Runtime and manifest pins after assembly:

```text
structural_evidence_manifest.json = 722f4db56fc6e77de258273f06fd1ae487b9bb0143440f73adb76747779a5cb8
normal.json                       = 7697fb8c20d8b0589247c352d93dc91e4cc6351f570a8b8ba6e739567f1dee40
optimized.json                    = 8449ac7d29ba7a1297f183949d75826e45ede86249af9940ec9e75cba5780cbe
package_inventory.json            = 80b71e4639b248d25c87b3221db2977c9e4b92c3af6e1ebe49c93f8829da8489
subject_lineage_root               = d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688
```

## 8. Static self-check transcript

```text
$ /usr/bin/python3 -I -S -B -c '<compile all evaluator_build_A Python sources>'
SOURCE_COMPILE_OK 5

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/assemble_evidence.py
{"authored_payload_bytes": 0, "checks_absent": 56, "checks_populated": 0, "fixtures_absent": 3, "fixtures_populated": 0, "payload_files": 10, "search_scope_members": 120, "search_scope_sha256": "691e871e4b2a13f09cdf5481abb1c7a32c05ba9426bf657436a5f5f2597db032"}

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/materialize.py
{"checks": 66, "fixtures": 6, "gated": 10, "normal_sha256": "7697fb8c20d8b0589247c352d93dc91e4cc6351f570a8b8ba6e739567f1dee40", "optimized_sha256": "8449ac7d29ba7a1297f183949d75826e45ede86249af9940ec9e75cba5780cbe", "structural": 56, "subject_lineage_root": "d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688"}

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/self_check.py
SELF_CHECK_OK syntax=5 canonical_json=all schemas=9 inventory=31 evidence_payloads=10 evidence=0/56 absent=56 fixture_obs=0/3 checks=66 structural=56 gated=10 fixtures=6 fixture_fields=16 child_fields=14 verifier_manifest_fields=11 exits=0/1/2 chain_invoked=false
```

The self-check rehashes all ten source/copy pairs; validates every partial source path, source SHA-256, span, payload path, and payload SHA-256; enforces one common 120-member search root and all four M-2 modes; binds every check to its descriptor digest and every fixture to its fixture-spec digest; verifies the complete package/runtime inventories; and confirms empty output/pycache directories.

## 9. PIN CHECK, fences, and verdict-line scope

### 9.1 PRE-SEAL PIN CHECK

| Item | Final result |
|---|---|
| Register snapshot | `4169c038…`, verified; Q-590 satisfied. |
| Packet | Manifest `9d35f4ed…`; 113/113 member checks `OK`. |
| Matrix map | `bc6c3e49…`, exact. |
| Spec/check map | `f8d1a7dc…` / `034ebf3e…`, exact. |
| Evidence copies | 10/10 byte-identical; content-addressed filenames agree. |
| Evidence manifest | `722f4db5…`; 56 + 3 exact IDs; all searches share root `691e871e…`. |
| Runtime manifests | `7697fb8c…` / `8449ac7d…`; evidence payload inventory 10/10. |
| Package inventory | 31 self-addressed rows + displayed self hash; 32 files total. |
| Output collision | Clear before artifact write; no overwrite. |
| Runtime products | No files in outputs or pycache; chain not invoked. |

### 9.2 F_PLDEC and fences

Only bytes, hashes, paths, spans, descriptor requirements, and search classifications were processed. No member was bound; no fixed point or end test ran; no physical quantity was numerically evaluated; no measured constant was read or compared. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false`. No fence prevented a structural assembly result, so `MACHINERY_APPEAL = none`.

### 9.3 Self verb audit

| Verb | Scope check |
|---|---|
| `payload` | Means a byte-identical copy of a sealed source, not a new proof or observation. |
| `cited` | Means source path/hash/span and payload hash are present and revalidated. It does not mean the citation satisfies the complete descriptor. |
| `PASS rows` | Refers only to the 24 verdicts in the sealed executed matrix. None was promoted to an RD-22 executor PASS. |
| `ABSENT_OF_RECORD` | Means the bounded 120-member, four-mode search found no complete runtime envelope for that descriptor/fixture. It is not a mathematical refutation. |
| `populated` | Counts only `available=true` complete executable records; partial citations do not count. |
| `AUTHORED_BYTES = zero` | Applies to evidence payload content. Metadata necessarily records custody and absence. |
| `SELF_CHECK = passed` | Static syntax/schema/hash/inventory/search validation only; no evaluator child launched. |

EVIDENCE = 0/56 populated + 56 ABSENT_OF_RECORD (+list)
FIXTURE_OBS = 0/3
AUTHORED_BYTES = zero
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN / (+payload-vs-metadata distinction; matrix PASS not promoted; absence is input-integrity only; static scope)
