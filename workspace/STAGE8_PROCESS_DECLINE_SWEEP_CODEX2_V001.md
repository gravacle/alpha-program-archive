# STAGE 8 PROCESS — DECLINE SWEEP (CODEX 2) V001

Date: 2026-08-09  
Lane: CODEX 2  
Task: PASTE 779 / flattening-check evidence base  
Custody: cleanroom-only; catalogue only; no decline is resolved, lifted, or interpreted

## 1. Preflight and search contract

The relay seal verified before reading. `DECLINE_REGISTER_V001.md` verified at
`9913262a8f9104ffd1186a04ec8c33035d7faa4d5f343faa6cb095166d8ac664`.
The output and sidecar were absent before this write, and pickup ACK `779_ACK.md`
was written before substantive work.

The declared search superset was:

```text
alpha_fundamental_record_action_cleanroom_v003/**/*.{md,json,txt,csv,tsv,yaml,yml}
```

The pre-write census contained 2,363 files. The exact, case-insensitive combined
probe was:

```text
declin(e|es|ed|ing)|we do not identify|not identified|
refus(e|es|ed|ing)|does not supply|still not supplied|not authorable|
beyond an interface|BLOCK_ABSOLUTE|BARRED|graveyard|shall not|
may not be re-proposed|conditional on|only under|iff|provided that|
under the condition|ABSENT
```

It returned 5,059 matching lines after coalescing overlaps on the same line.
Exact spellings, case-folded/word-boundary variants, and the semantic forms
specified by the relay were all included. Every raw hit was then subjected to
the meaning probe. A survivor had to be a content decision, not merely a token.

Custody was checked after the superset search. Every source below has a verified
adjacent SHA-256 sidecar except the V011 packet member, whose digest is itself a
member of `review_packets/STAGE7_QSPEC_CANDIDATE_V001/STAGE7_PACKET_MANIFEST_V001.sha256`.
No unsealed root copy is cited. Spans are raw UTF-8 byte intervals, half-open and
line-aligned; each span includes the selected lines' terminators.

PE-4, PE-5, and PE-6 were recorded as existing and were not consulted. They have
zero verdict weight here.

## 2. Meaning-probe law and exclusions

The five allowed result types are closed:

```text
DECLINED-IDENTIFICATION
DECLINED-AUTHORSHIP
BARRED-ABSOLUTE
CONDITIONAL-GRANT
RULED-ABSENT
```

The following large raw-hit classes were rejected rather than flattened into
declines:

| Excluded class | Meaning-probe result |
|---|---|
| Ordinary missing premise, payload, proof, carrier, or implementation | Mere absence; not a decision about what the record declines to grant. |
| A lane saying it did not perform work outside that relay | Task-scoped stop; not a program-content decision. |
| Runtime, custody, no-measurement, no-end-test, authorization, or verb fence | Process gate; expressly excluded by AS3(c). |
| `ABSENT` inside fixture data, test expectations, schemas, or quoted blocker text | Status token without a new decision. |
| `iff`/`only if` in ordinary theorem logic | Excluded unless it guarded an identification, adoption, or value. |
| Later reports repeating an earlier refusal | Deduplicated to the earliest or clearest currently sealed decision span. |

## 3. Register-shaped survivor table

`seed` gives the content match to `DECLINE_REGISTER_V001`; `—` means new beyond
the seed. The decision/condition column is a one-sentence register entry. For a
conditional grant, the quoted text after `condition:` is the exact sealed guard.

| ID | seed | type | decision or exact condition | source (SHA-256) | half-open span | span SHA-256 |
|---|---|---|---|---|---|---|
| S01 | D1 | DECLINED-IDENTIFICATION | The `+1` in the displayed tower is not identified with `Phi^dagger Phi`; that identification was withdrawn. | `STAGE8_7A_TOWER_CONTEST_DARIO_V001.md` (`03db8d3da273f42c62acdea5d453ec0b780934c73aa897fdf2cfb986c0e7bc9b`) | `[6410,6885)` | `4b6102e985b7a7228333083e8f6a222c369f0609c32a150f9ede315538d889b7` |
| S02 | — | DECLINED-IDENTIFICATION | The target's external label `q=(±1,0)` is not identified with the monopole degree `deg L/2`; the attempted `|q|>=1/2` selection is withdrawn. | `STAGE8_7A_TOWER_CONTEST_DARIO_V001.md` (`03db8d3da273f42c62acdea5d453ec0b780934c73aa897fdf2cfb986c0e7bc9b`) | `[1423,2290)` | `45e4900edbb62854827d3e91a0c6b5480ccc449aaed7c1592f8cba8d0d1af29c` |
| S03 | — | DECLINED-IDENTIFICATION | The comparison group, local gauge-coordinate action, and projective-ray quotient are related through the associated bundle but are not three interchangeable `U(1)` assumptions. | packet `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` (`aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a`) | `[10764,11678)` | `8cbc92991ab1648715947c9ca43ab26f0ca50a758646c21cfa9a0c533b3daeeb` |
| S04 | — | DECLINED-IDENTIFICATION | The record interval `Delta tau` is not identified with `T_R`; the source says that equality was explicitly refused with a bounded negative. | `STAGE8_SECOND_RATIO_DERIVATION_HUNT_AND_BRANCH_INDEX_EINSTEIN_V001.md` (`06763cfb8ca7f5d3666f3ac261050401183f88fea4fe64e98266dd53ab12dbe8`) | `[4161,4957)` | `5fec8fd28d8048be3e7fdc8dcf3b33bc4a0eaa19cb3941b6eefd659e87c1d371` |
| S05 | — | DECLINED-IDENTIFICATION | The source-algebra/record-limit tensor product is only co-location and is refused as the missing field/CTP extension. | `STAGE8_CROSSING_PRODUCER_POSE_AND_GLUING_VERDICT_EINSTEIN_V001.md` (`80702f142edf14f22f0a2721475456fd00a1e7b1892fb7c9c8a9a15bdb4c7200`) | `[6905,8106)` | `e7a873cd5e3026d362b545e2297ec70b75697ecf62a1f629a71e6cf2ad83111f` |
| S06 | — | DECLINED-IDENTIFICATION | The sea kernel's `r^-3` falloff is not identified with uniform preparation clustering. | `STAGE8_PARENT_PREPARATION_CLUSTERING_DETERMINATION_V001.md` (`58f894356ae3559cdd53771b6a85ffb2baf9c98d18ed767e594c79c2e10ed672`) | `[8804,9317)` | `f7737ebcf5b6c1bf590c3a91cadfd207876f7930303eebd0abed7146749a8d43` |
| S07 | — | DECLINED-IDENTIFICATION | The retired Stage-9/10/11 labels are not identified by a sealed Stage-to-EM-step mapping. | `STAGE8_STAGE_LABEL_RETIREMENT_9_10_11_V001.md` (`c2417d657f22512bbc903bc41594bc3eed7fb7ce17c09733a5c49cdc1790a30c`) | `[5488,5901)` | `10516f53f26f64f0455545e6e229b968deb93aaab078cc7f7313f9c1408d524f` |
| S08 | — | DECLINED-IDENTIFICATION | The derived discrete incidence connection is not identified with electromagnetism, a smooth public field, a Maxwell connection, or a response object. | `STAGE8_PRPS_SMOOTH_PHRASING_IMPORT_ADJUDICATION_V001.md` (`e09349f5b71a790b40700669227268e7a4615750c9d03d164daa373bb40af3df`) | `[11897,12813)` | `29d0efd6a4eed478a1754f87901382b06d848b670f24c71ae4b8ade8ae36cc43` |
| S09 | — | DECLINED-IDENTIFICATION | `Tail_germ={0}` is not identified with the physical `Tail_R`. | `STAGE8_SOURCE_GERM_PHYS_V002_ADVERSARIAL_REVIEW_DETERMINATION_V001.md` (`5d2559e41a3ebdad6b86c524ad3f0c62092eae0b72f5736245e76f4ac3c63a75`) | `[10131,10887)` | `c70c52633765378fbc1457275ade49a8ffe59027f2b2fbf20652547c0553d315` |
| S10 | — | DECLINED-IDENTIFICATION | The critical point on the diagnostic scalar source quotient is expressly not identified with a physical background. | `STAGE8_TASK4A_COMPLEMENT_SCOPED_PHYSICAL_STATIONARY_RESPONSE_PACKAGE_FLAT_FAMILY_DETERMINATION_V001.md` (`30532ecb2c08d21e28af05f1228b9c29264be99731f63c8cf5b30273bb51e7b8`) | `[2057,2389)` | `88cf09a5ce2af56bb220fe0a99d4a1749dcbf66b9e50f68454c7deede0cca568` |
| S11 | — | DECLINED-IDENTIFICATION | Independent CTP branch transformations are not identified with the required simultaneous/common transformation of both histories. | `STAGE8_CTP_PHYS_INPUT_PACKAGE_U3_DOR008_DOR009_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md` (`b0118d89e0b4b321fbf9caab5bfb811a0b5fd572e808d02615ee8503db2bc1ac`) | `[7569,7866)` | `e8a3d086aaa2b5559fd58f8024ded66d535a1f195e6e014110dbd76223d8359f` |
| S12 | — | DECLINED-IDENTIFICATION | Status flags are not identified with the objects that discharge them. | `STAGE8_PROSE_FLAG_DEPENDENCY_EXTRACTION_V001.md` (`c2b1d21c049065a729f6883b3a7e2122d4a1655b86e8c70800a24cbdbc2e9843`) | `[1462,1757)` | `0e43c7c67fe712ee398c4efa80ce853c5a8f539be7b4c4d3401d1d50647a879c` |
| S13 | — | DECLINED-IDENTIFICATION | Arm 2 is not identified with `R-L2b` in either direction; only the one-way consumption relation is retained. | `STAGE8_R2_WELL_POSEDNESS_AND_INPUT_SEAL_DETERMINATION_V001.md` (`eed30aec51ef3feb72348037c78288732bcc3dbec0d1743e02f0e40e45cac6c2`) | `[19029,19502)` | `f18ee4f98b48f926b173800fff4b14fb1e3275624e86d73e3ae4da401468577a` |
| S14 | D2 | DECLINED-AUTHORSHIP | Adding an integrality condition to `Xi_N` would author flux quantization, new physics beyond the interface, and was declined on minimality. | `STAGE8_TASK5_XI_N_CANDIDATE_DARIO_V001.md` (`1b878d7a89fc2d48290dcdbd6494bb05c382124b74ae99d58a9e7f6f3e63409a`) | `[8995,10618)` | `e358aaa29cafa06e88d90a24281ba0bd30bddce0bd175cd8e02f7c33efa99ab0` |
| S15 | D6 | DECLINED-AUTHORSHIP | No `D_BR` bundle class is adopted; the principal declines to author flux quantization and leaves the selector open. | `DECISION_SELECTOR_OPEN_AND_GAP_CLASSIFICATION_2026-08-09.md` (`cbdc9432de77b29b4ec5fcf1f4f1e9bfb4a185f661b656b98b56103a39257bfb`) | `[55,945)` | `5ffe62af47f95ddd767fec065af9c53ce8bb9ff38a54bcb83ea373546afdc02a` |
| S16 | — | DECLINED-AUTHORSHIP | Hessian-first supersession is not chartered because it would conceal the all-order extensivity question without evidence that the original obligation is unprovable. | `STAGE8_EXTENSIVITY_VERDICT_AND_RL2B_CAMPAIGN_OPENING_V001.md` (`0f3082cab910f2eb6769698fc03cdb0201830c2551ecd8201fa6748b24e07505`) | `[5173,5677)` | `0da19d8d23d4ed06ecfbc1fc33972b12ac477ec4e52ac49edcd48337c42a62b1` |
| S17 | — | DECLINED-AUTHORSHIP | The known class-leaving gamma falsifier was deliberately not adopted because it was selected with foreknowledge after three defeated designs. | `STAGE8_T7_GAMMA_GATE_FINALITY_DECISION_RECORD_V001.md` (`65d54d6cf58e1e2a2f7f177444c68120c6989e09fa0402381796303781070425`) | `[1740,2406)` | `e0efbe0ce7d3353a6bc4cd26fec4f9de8482c4b1f111de577e0b173919c4f186` |
| S18 | — | DECLINED-AUTHORSHIP | The two collar-versus-projector halves are deliberately not conjoined into “the collar is broken”; the sealed answer remains conditional. | `STAGE8_COLLAR_CONJUNCTION_CHARTER_RESULT_V001.md` (`f3b2259aa5200c63385ff452507e9f258e8ed0dd1a7d9b41eae66c8e37197390`) | `[1074,1919)` | `f2137fbf80ab7528358326277676be2ba55499310f6a07c365e2bb7b8b791656` |
| S19 | — | DECLINED-AUTHORSHIP | Decay is not inferred from masslessness/gaplessness because doing so would import external physics. | `STAGE8_PARENT_PREPARATION_CLUSTERING_DETERMINATION_V001.md` (`58f894356ae3559cdd53771b6a85ffb2baf9c98d18ed767e594c79c2e10ed672`) | `[9317,9726)` | `0f85bc90ffbaf0c0b8ddb02f6acb6deb7ebe5685ac8e905101575d48a6b74d4b` |
| S20 | — | DECLINED-AUTHORSHIP | The source-germ specification refuses to choose a topology/calculus profile from the named alternatives. | `STAGE8_CTP_PHYS_INPUT_PACKAGE_ITEM2_PHYSICAL_LOG0_GERM_SPEC_V001.md` (`14573a676a385dd4c814f3fd12d8fb53caa601598e96b35525c6372329d506b3`) | `[5322,6307)` | `01011df0977e5dfc417b6fb5f6e26b8eaa8dfc9e44f19673ea723ca2ce48d662` |
| S21 | — | DECLINED-AUTHORSHIP | The gamma construction refuses to choose Misner-Sharp or Brown-York energy; the Hamilton-Jacobi conjugate energy must instead be derived. | `STAGE8_GAMMA_K_CONSTRUCTION_SPEC_AMENDMENT_001.md` (`5bbf0152c511956e7903d86b7a989affd5c8689e9c4ba8b49675e895ab7b8a05`) | `[15876,16442)` | `9156064f2d3e28531aa1d34a3c94e88cef6ac12586d8abf5e3daaaeb12303244` |
| S22 | — | DECLINED-AUTHORSHIP | The covector ray's positive scale remains free because the governing spec declines to fix it. | `STAGE8_HOLONOMY_FIRST_OPENING_TENSION_ADJUDICATION_EINSTEIN_V001.md` (`8fbdc8300b28166564e4ba32e6747bc643135e25d674cc37da706de3afbbf019`) | `[9080,9496)` | `c8c57d511f94f578163b51978f9080acaae409f6c7d576b11eef11d28e5e8550` |
| S23 | D4 | BARRED-ABSOLUTE | Flux quantization may not be re-proposed as a stiffness selector; the route graveyard marks this `BLOCK_ABSOLUTE`. | `STAGE8_7A_MAGNETIC_SECTOR_HUNT_DARIO_V001.md` (`54d9cb5af3c6bb3d1dddd79a00f5f7954c167fb76f65d60272f480275d7ef2d2`) | `[5467,6217)` | `cc632c32494a71ab8585d43254f82e1fcee8014054965965bb932240ccb0bf24` |
| S24 | — | BARRED-ABSOLUTE | Any lane reach for a clustering axiom blocks immediately; adoption is principal-only and may not rescue a route. | `STAGE8_APPARATUS_PROVENANCE_ERRATUM_001.md` (`c871ed6e4a6c5cb99dd1291c66ffeeaae60863697070693ca7d0119a2ff69a70`) | `[2301,2777)` | `336d01b7944b6f51ec10832f164a6f6fcdfe6fb4f19f68fcd96319ff4298ebe0` |
| S25 | — | BARRED-ABSOLUTE | No reparameterization or equal-action principle may be introduced; the principal refused that route. | `STAGE8_T7_GAMMA_REFUTATION_AND_PARITY_LEMMAS_GATE_SPEC_V001.md` (`5f7e99655cd92935406606ad03e33befded65a0091e2ccbe6d91689e76473e75`) | `[5933,6411)` | `911ba2fbcfb9de3b532b47f5c375dcb970f36da036f39f9d627123b889077c92` |
| S26 | — | BARRED-ABSOLUTE | `C_ref` is barred as a source and may be used only as an audit/target interface. | `STAGE8_7A_RA27_2_SAME_REGION_DARIO_V001.md` (`5234141f065d57684de6e54f453bb835408749f81752c186750cfd11cc29fc06`) | `[24860,25338)` | `14b17738bd9df6ec36cae2a9b6a25c9b9d6d1f8e9ddc5b3a6e320d1089f6fbab` |
| S27 | D1 | CONDITIONAL-GRANT | Flat `×16` multiplicity is granted only under the exact condition: “the flux U(1) is external to Spin(10) with flat parent connection.” | `STAGE8_7A_TOWER_CONTEST_DARIO_V001.md` (`03db8d3da273f42c62acdea5d453ec0b780934c73aa897fdf2cfb986c0e7bc9b`) | `[10764,11705)` | `d08cccc778b13b4422097cefba00247c28f7dbe960668481328684ec16274dc2` |
| S28 | D9 | CONDITIONAL-GRANT | The five free `D_BR` data classes remain unselected and may be constrained lawfully only by “boundary closure + the induced action, before any comparison.” | `STAGE8_7A_TOWER_CONTEST_DARIO_V001.md` (`03db8d3da273f42c62acdea5d453ec0b780934c73aa897fdf2cfb986c0e7bc9b`) | `[12531,13213)` | `a451238549a62fdc0eab3b556648689a103cf71e78215f3c93237cb80694414f` |
| S29 | — | CONDITIONAL-GRANT | `C_R=1` selects only after “an unbuilt source-record-gravity Hamilton-Jacobi bridge,” and the energy fork remains unresolved. | `STAGE8_SECOND_RATIO_DERIVATION_HUNT_AND_BRANCH_INDEX_EINSTEIN_V001.md` (`06763cfb8ca7f5d3666f3ac261050401183f88fea4fe64e98266dd53ab12dbe8`) | `[5535,6559)` | `c086e622222137448e5405fffcc7fe01e659fe8ea2750949d947a78e152f6a52` |
| S30 | — | CONDITIONAL-GRANT | Hessian-first is available only “IF R-L2b FAILS,” and only with F1–F5: explicit supersession/non-discharge, zero-stiffness control, cellulation independence, sourced-Hessian typing, and the five-condition open register. | `STAGE8_EXTENSIVITY_VERDICT_AND_RL2B_CAMPAIGN_OPENING_V001.md` (`0f3082cab910f2eb6769698fc03cdb0201830c2551ecd8201fa6748b24e07505`) | `[5677,6451)` | `db933e4e75d4a2765ff199a4881823b5aa6c177ab175b5207967bba29293cd84` |
| S31 | — | CONDITIONAL-GRANT | Control-4 v3 is authorized only after a typed same-apparatus argument; iff Outcome A, a pre-execution spec freezes widened predictions/refuters and disclosure; the result then has the sealed bite/no-bite semantics and never itself establishes gamma refutation. | `STAGE8_T7_GAMMA_GATE_CONTROL4_V3_CONDITIONAL_AUTHORIZATION_V001.md` (`67bb5cff532523daa60600bbd69517e4edf353d0425d255ae03e453567e6c271`) | `[545,4426)` | `414c31b4959bdc72fc9bd883dedef8c0c4d34aa2e89aaa46536bf26c1dd08cc3` |
| S32 | — | CONDITIONAL-GRANT | A connected volume-density limit follows only if V011 proves uniform finite-range/bounded terms, uniform preparation clustering, a volume-independent nonzero neighborhood, uniform absolute convergence of the differentiated cluster sum, and subextensive boundary corrections. | `STAGE8_EXTENSIVITY_QUESTION_BLIND_ANSWER_V001.md` (`f3e62798bac4b9d3da3fe4f966f784607a3b39945332fc13630eb16fdc004c0c`) | `[2749,3618)` | `1daabb8725c39b9050840015964ed4bb51d551390c81b078f79a1b3466bb2996` |
| S33 | — | CONDITIONAL-GRANT | The four-dimensional coefficient is constant only if “the parent normalization is rescaled with the fiber extent.” | `STAGE8_HELD_FIXED_BRANCH_DERIVABILITY_AND_AXIOM_PRICE_V001.md` (`39f7ea6d95dcdad323f3cd74ebd0e973b95fc8de3c87a52f1a624da7cf725625`) | `[2083,2741)` | `36039e3ab954e11fd7def57c1bc877a593ce62fcc6edcad52c950c4ea6abfda3` |
| S34 | — | CONDITIONAL-GRANT | Absolute scale closes only if “the complete parameter-free parent supplies a Lorentz-scalar equation with one isolated positive stable solution.” | `STAGE8_HELD_FIXED_BRANCH_DERIVABILITY_AND_AXIOM_PRICE_V001.md` (`39f7ea6d95dcdad323f3cd74ebd0e973b95fc8de3c87a52f1a624da7cf725625`) | `[3765,4145)` | `80ef473adc99fea95b682ad7be25e67ffeb2e0c16fd12c3743ee069455431e3f` |
| S35 | — | CONDITIONAL-GRANT | The final claim remains explicitly conditional on the one-source branch unless the complete charged spectrum and threshold map are derived. | `STAGE8_MASTER_PLAN_TO_ALPHA_V001.md` (`12f204c64f0c0fd92cc77527309deb48e48610eb78772500870a1cfb884708dd`) | `[5411,5915)` | `98072af2fea3dc619b0c5ec570378fb98c5664de3110e3551f130bb961b3ef94` |
| S36 | D5 | RULED-ABSENT | The sealed integer-character lattice is ruled to be a character lattice, not a flux; flux is `ABSENT`. | `STAGE8_7A_MAGNETIC_SECTOR_HUNT_DARIO_V001.md` (`54d9cb5af3c6bb3d1dddd79a00f5f7954c167fb76f65d60272f480275d7ef2d2`) | `[5467,5709)` | `4e6fef4b9bd8500e61c2b76201e438b935d2fcc5e3cb50053fe0cf7707ced964` |
| S37 | D3 | RULED-ABSENT | The parent-arm monopole correspondence is ruled “still not supplied.” | `STAGE8_7A_MAGNETIC_SECTOR_HUNT_DARIO_V001.md` (`54d9cb5af3c6bb3d1dddd79a00f5f7954c167fb76f65d60272f480275d7ef2d2`) | `[5709,5848)` | `3c9f1e1b0ee8a349726397df0328237951b1e5fd89052fe09148ca10afac5769` |

## 4. Seed reconciliation

| seed | disposition | survivor(s) or actual finding |
|---|---|---|
| D1 | CONFIRMED | S01 confirms the withdrawn `+1 = Phi^dagger Phi` identification; S27 records the exact conditional `×16` grant. |
| D2 | CONFIRMED | S14 is the sealed minimality refusal to author flux quantization. |
| D3 | CONFIRMED | S37 is the ruled not-supplied parent-arm monopole correspondence. |
| D4 | CONFIRMED | S23 is the graveyard `BLOCK_ABSOLUTE`. |
| D5 | CONFIRMED | S36 is the character-not-flux ruled absence. |
| D6 | CONFIRMED | S15 is the principal's no-class-adopted/open-selector decision. |
| D7 | NOT-FOUND-AS-SEEDED | What was found is a relay-775 task-scoped stop over an unbuilt quotient and a local refusal to fill missing compatibility text. AS3(b) excludes that from a record-wide authorship decline. |
| D8 | NOT-FOUND-AS-SEEDED | What was found is the Q-681 classification that 19 Step-11 objects are `FREE_MULTIPLE` and adoption-gated. It is an open/freedom classification, not an express refusal among the five closed result types. |
| D9 | CONFIRMED | S28 carries all five data classes as unselected and quotes their exact lawful selection condition. |
| D10 | NOT-FOUND-AS-SEEDED | What was found is the no-measured-constants/process fence and an unwritten release condition. AS3(c) expressly excludes a fence from the decline register. |

Seven of ten seeded entries therefore survive the meaning probe. The eight
survivor rows marked with seed IDs represent those seven entries because D1
contains two independently typed decisions. The other 29 survivor rows are new
beyond the seed.

## 5. Battery and custody conclusion

F_PLDEC is clean: the sweep catalogued language and byte provenance only. No
physical quantity was numerically evaluated, no constant was compared to a
measurement, no member was bound, and no fixed point or end test was executed.
The three gates remain false. The verb audit is scoped to this artifact: words
such as “confirmed,” “ruled,” and “refused” report sealed source content and do
not claim a new program verdict. This artifact does not modify the seeded
register; it is shaped for registrar splice.

SEARCHED = `alpha_fundamental_record_action_cleanroom_v003/**/*.{md,json,txt,csv,tsv,yaml,yml}` (2363 files)
HITS_RAW = 5059
SURVIVORS = 37 typed (DECLINED-ID: 13 / DECLINED-AUTH: 9 / BARRED: 4 / CONDITIONAL: 9 / RULED-ABSENT: 2)
SEEDED_CONFIRMED = 7/10
NEW_BEYOND_SEED = 29
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
