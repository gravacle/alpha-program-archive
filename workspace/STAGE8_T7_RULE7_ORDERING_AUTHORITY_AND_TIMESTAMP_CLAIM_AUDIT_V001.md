# Stage-8 T7 Rule 7 — Ordering Authority, and an Audit of This Lane's Timestamp Claims V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY STANDING RULE + SELF-AUDIT + CITATION INDEX.
NOTHING IS PATCHED. Four ordering claims this lane sealed rested on
filesystem timestamps. Each is RE-GROUNDED on a permitted authority or
WITHDRAWN below. No conclusion changes; three of the four re-ground
cleanly and the fourth was never load-bearing.
```

## RULE 7 (ORDERING AUTHORITY) — standing, extending Rules 1-6

```text
ORDERING CLAIMS ARE ESTABLISHED ONLY BY:
 (a) GIT PUSH ORDER on origin/main of the public archive — third-party
     custody, force-push protected. THE PRIMARY AUTHORITY.
 (b) HASH CITATION CHAINS — artifact B citing artifact A's sha256 proves B
     postdates A, because the hash cannot be cited before the content
     exists. Cryptographic and clock-free.
FILESYSTEM TIMESTAMPS ARE NOT EVIDENCE OF ANYTHING and MAY NOT BE CITED in
any artifact as establishing order.
GROUND, verified by the reviewer: both fenced directories show ctime
11:28:13 while their mtimes read 10:50:36 and 08:35:39 — iCloud
Desktop-and-Documents sync perturbs them continuously. They are not merely
weak evidence; they are ACTIVELY UNRELIABLE in this workspace.
FORWARD REQUIREMENT: every artifact cites every authority it consumes BY
SHA-256, and any artifact that must be shown to precede another says so BY
BEING CITED, never by its file date.
```

## Self-audit: every timestamp-grounded claim this lane sealed

### W-1 — the fence diagnosis. Timestamp legs WITHDRAWN; conclusion UNCHANGED.

```text
WITHDRAWN AS EVIDENCE, from STAGE8_T7_CYCLE7_VERIFICATION_RETURN_AND_
FENCE_CLOSURE_V001.md (28398c58…) and STAGE8_T7_CYCLE7_PACKAGE_RECORD_
AND_THREE_FINDINGS_V001.md (6b76117a…):
  - "both directories carry ctime 2026-07-26 09:07:04 — THE IDENTICAL
    SECOND. One operation over both."
  - "the mode changed with NO mtime change ... chmod semantics, not a
    write."
  - "NO LOGGED TOOL CALL ... touched either directory at that second. The
    author-lane calls bracketing 09:07:04 (09:06:55 and 09:07:12) are both
    Edits under scripts/."
  - "manifest v006 did not exist ... at 09:07:04 and was first built at
    10:18 today."
  These rested on ctimes/mtimes and on correlating them against transcript
  clocks. Under Rule 7 they are not evidence. WITHDRAWN.

THE CONCLUSION STANDS ON THREE TIMESTAMP-FREE LEGS, all still valid:
  L-A  MODE-VALUE EXCLUSION. Every program path sets 0o555
       (FENCE_AT_REST_MODE) or 0o755 (FENCE_RAISED_MODE) and nothing else,
       verified by reading every chmod in controller v007 and in the
       manifest builder. A missed drop, a hard kill inside the raised
       window, and an interrupted raise ALL leave 0755. The observed mode
       was 0700, which no code path in this program produces. This also
       excludes the manifest-raise candidate on its own, without the
       timestamp leg: the builder drops to 0555 and records that it did.
  L-B  SELECTIVITY. Of 279 directories in the tree, EXACTLY TWO deviated
       from 0755, and they were precisely the two the fence had set to
       0555. A count, not a clock.
  L-C  CONTROLLED EXPERIMENT. The rsync hypothesis was tested by setting
       0555, running the exact command, and re-checking: mode unchanged.
       An experiment, not a timestamp.
  AND the reviewer has since identified the cause directly:
  FXICloudDriveDocuments = 1, workspace under iCloud Desktop-and-Documents
  sync. That is stronger than anything this lane offered.
```

### W-2 — DEFECT 1's ordering. RE-GROUNDED ON PUSH ORDER; defect unchanged.

```text
WITHDRAWN: "sealed at 2026-07-26 09:39:15 ... 17 MINUTES LATER at
09:56:26", from STAGE8_T7_CONSTRUCTION_LANE_THREE_DEFECT_ERRATUM_AND_
REVIEW_INCOMPLETENESS_V001.md (11d12ead…).
RE-GROUNDED ON AUTHORITY (a), GIT PUSH ORDER ON origin/main:
  STAGE8_T7_ARM2_SHARPENING_AND_PROJECTION_TAIL_BINDING_V001.md
    (782495ea…)  first appears in commit 2cffec7
  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md
    (46846730…)  first appears in commit 692e021
  and 2cffec7 PRECEDES 692e021 on origin/main.
THE BINDING DEMONSTRABLY PRECEDES THE SPEC IT BINDS, by the primary
authority, with no clock involved.
NOTE, and it is the important part: THE DEFECT NEVER DEPENDED ON ORDERING
AT ALL. It is that the spec contains ZERO occurrences of the binding's
markers — a content fact established by grep, independent of when either
was written. The ordering was colour; the defect is the substance, and it
stands either way.
```

### W-3 — the fence RECURRENCE. Precise times WITHDRAWN; recurrence RE-GROUNDED.

```text
WITHDRAWN: "ctime 10:47:08 and again by 10:50:36", "~29 minutes after I
restored it", from STAGE8_T7_ROW_AND_LADDER_CAPTURE_N48_RESULT_V001.md
(df4033cd…).
RE-GROUNDED ON PUSH ORDER: this lane recorded RESTORING the fence to 0555
in one anchored commit and then recorded FINDING IT OPEN AGAIN in a later
anchored commit, more than once, with each observation carried in a
separate push. Restoration-then-reopening across successive pushes
establishes RECURRENCE without any clock. The count of re-openings and
their spacing in minutes is withdrawn; THE FACT OF RECURRENCE STANDS, and
it is the only part the B3/B4 conclusion needs.
```

### W-4 — the pre-custody corpus. Was never load-bearing; RE-GROUNDED anyway.

```text
WITHDRAWN: "the pre-custody inherited corpus (Fable-era, 00:48-02:34 on
07-25 vs custody at 13:34)".
RE-GROUNDED ON PUSH ORDER: the COMPLETE_QSPEC_* family and the rest of the
inherited corpus FIRST APPEAR ON origin/main AT OR BEFORE the
custody-transfer snapshot commit ecc3867, whereas every artifact this lane
authored first appears AFTER it. That is the same claim, established by
authority (a). The seal-coverage conclusion — 100% coverage of this lane's
own artifacts, the unsealed remainder all inherited — is unchanged.
```

## THE CITATION INDEX — closing the gap append-only

The principal's finding: hash citation is inconsistent — the
primary-resolution successor spec cites 2 predecessor hashes, while
STAGE8_T7_D3_QUANTIFIER_READING_FREEZE_AND_LEMMA_CONSUMPTION_V001.md
(`9a0c2045…`) cites ZERO.

Sealed artifacts CANNOT be edited to add citations. The append-only
closure is this index: every artifact this lane authored, with its sha256
and its first-appearance commit, IN PUSH ORDER. Any artifact may now be
cited by hash, and any ordering between two of them is read off the commit
column. The machine-readable form of this index is the git history itself.

```text
 #  COMMIT    SHA-256                                                            ARTIFACT
 1  ecc3867  3d5bdbd097cdcd8a0e176823dbd9b0a5e9a50ab1c14c8141e503ce5b2866f072  REVIEW_2026-07-25_route2_implementation_hostile_rereview.md
 2  ecc3867  a86ebb6719a4f18a0bceb1fa72498503dfdc489ae1e0c3aec84dd6944bb53eec  REVIEW_2026-07-25_route2_phaseA_spec_hostile_preexecution.md
 3  ecc3867  dc7cdd15935c300627e8b72fd70bf6aba61b29d2c91d600348da070c71e1c10d  STAGE8_T7_ACTUAL_PARENT_CAR_IMPLEMENTATION_REPAIR_BINDING_V001.md
 4  ecc3867  6fa8845a2d30635d0b307c362051d97d80fb084042f695128d1ea469d5403c5a  STAGE8_T7_ACTUAL_PARENT_CAR_PHASE_A_EXECUTION_BINDING_V001.md
 5  1ec83f3  9e626d52393b15701f0a7743c3ab86a4e908f749f59d4dc94602b170b545960d  REVIEW_2026-07-25_route2_v002_verification_rounds.md
 6  cc4603c  a4e43bbd1269a07c2697ea5aec1f6059a4ebe95eed16d647b01ca99b032884c6  EXTERNAL_AUDIT_2026-07-25_fable_v002_return.md
 7  cc4603c  9178befef6a9697944fc8f6cb9737789cc71ed94c67fbd1baeccd5f9cda2f425  STAGE8_T7_ACTUAL_PARENT_CAR_IMPLEMENTATION_REPAIR_BINDING_V002.md
 8  cc4603c  2e0f9455350bb12c56ded1994a81bbe671558b14e6a67fd0f49c62d67552b0d8  STAGE8_T7_GPG_SIGNATURE_REQUIREMENT_SUPERSESSION_AMENDMENT_V001.md
 9  cc4603c  5bb0eb6a083c440863c0d380240bc6065f4069dea098a116af3bed8529b72005  STAGE8_T7_REPAIR_BINDING_R2_LINEAGE_CLAIM_FALSIFICATION_ERRATUM_V001.md
10  1cd6bc2  277654eed085e0e3fce0924536f27bd2fbbf1ef54f3a0336fdb45c071be1bfb4  STAGE8_T7_ER_FORK_KAPPA_INSENSITIVITY_BOUND_SPEC_V001.md
11  ac8b575  6b3cbe9f54415e58261e38f0bbc5943b50d8ad7e7f11394bb5a572b8c7357e30  REVIEW_2026-07-25_er_insensitivity_spec_v001_NOT_READY.md
12  ac8b575  8130ae5d11a582ab79bb19a624dc8e128a5ceddc349d3bd27585b1c975f98cff  ROUTE_MEMO_2026-07-25_duhamel_intensive_hessian.md
13  ac8b575  3e37eaa4d9183d171eb9e4b0dd0ad799a3503cd364c022858ac402396d04834e  ROUTE_MEMO_2026-07-25_linked_cluster_majorant.md
14  ac8b575  1e79b0b7baf9734c5c0d91a6f37db189c270a5dd88de31da4cee13b7bb8a099d  STAGE8_T7_ER_FORK_KAPPA_INSENSITIVITY_BOUND_SPEC_V002.md
15  e8ba253  562a2ab4b78b67e1a1de6c53004af04c2cb9ee8052c06304e22e5c6782ef569e  REVIEW_2026-07-25_er_insensitivity_spec_v002_READY_WITH_CONDITIONS.md
16  e8ba253  e37d39911992c91fddf4960caec9e512657922c83645bc8acd69dca34f156f78  STAGE8_T7_ER_FORK_KAPPA_INSENSITIVITY_V002_EXECUTION_NARROWING_BINDING_V001.md
17  a5cecce  94053bf33421abf0ecd3cd1acef21903be44e4c023bd87c7876c210cee3f9d35  EXTERNAL_REAUDIT_2026-07-25_fable_v003_return.md
18  a5cecce  febb819dff670a0d8d125098f4c459ee0b0127faf42bb0f18a979130bd571ad3  STAGE8_T7_MANIFEST_BINDING_BRIDGE_AMENDMENT_V001.md
19  a5cecce  296771751fd375a76350512140c0897529efa1539f2e26443cc5277b909c4db3  V003_VERIFICATION_RETURN_SEALED_TRANSCRIPT_V001.md
20  1880be7  a087e90a078e571c01b7de360cccfb831eb948f0a77fd618d0dd74e47b49271d  STAGE8_T7_ER_FORK_KAPPA_INSENSITIVITY_RESULT_V001.md
21  1880be7  b78e7de6a481bfd01741ebc4d606db14f3b82315a435fafee2f92269ab61da40  STAGE8_T7_MANIFEST_BINDING_BRIDGE_AMENDMENT_SUPPLEMENT_V001.md
22  44a4927  e21cb51ffaaa77caabfbfd4566b7b81053594164a529b49f8cfdca67c9260ab3  DECISION_2026-07-25_er_fork_option_gamma.md
23  8c96ca7  da6d8cc7bd4736b079e8262cc9ea15edfb6a574d038bc790eaad1432e8515875  ROUTE_MEMO_2026-07-25_gamma_record_level_insensitivity.md
24  f200328  143d4b494b5ce5c24e105ac8ddbaa3f7655803ce53b4803d72c1bb4c076ec638  DISPOSITION_2026-07-25_gamma_killtest_beta.md
25  f200328  5f7e99655cd92935406606ad03e33befded65a0091e2ccbe6d91689e76473e75  STAGE8_T7_GAMMA_REFUTATION_AND_PARITY_LEMMAS_GATE_SPEC_V001.md
26  503a42c  f2848ce7ca14d2e7765991fe9bad226197dc105f7cdd9a47728230b6690490f1  ANALYSIS_MEMO_2026-07-25_L2_typing_freeze.md
27  503a42c  cdbacdaf5efcd3a70a6ffa456bc790753e0ff36609c40c67b9bb606b79624746  STAGE8_T7_L2_INTENSIVE_HESSIAN_TYPING_FREEZE_V001.md
28  2d53707  2b9edaf8a0c1fd1e2e5004024eaaa2a67527199234313f9b3d1043ad3910d70e  REVIEW_2026-07-25_gamma_gate_spec_NOT_READY.md
29  2d53707  83ff0d4f818370b271c10caa265ffbea431f31c7b7437d98d4d040201c5c5759  STAGE8_T7_GAMMA_GATE_SPEC_REPAIR_AMENDMENT_V001.md
30  bda63cf  03543ab30e43c0c9f5710825dc88832ff49b80cd3bb058e22e22d5271f22844b  EXTERNAL_REAUDIT_2026-07-26_fable_v004_return.md
31  2931793  03fadd3634cf8dbc729795c4009012933d3ad836e663c9c509e4e43b7b4883bc  STAGE8_T7_L1_MULTICELL_LEMMA_ASSESSMENT_V001.md
32  2931793  c31173203dbf965d981e6f0df8bef8c87f654db0d5204d025baa4954a89c6166  STAGE8_T7_V004_ENUMERATION_CORRECTIONS_V001.md
33  2931793  79e793c8696da951022eeb03ed4e395d1a5cbd8e0dfef3c7b915430066477fad  V004_VERIFICATION_RETURNS_SEALED_TRANSCRIPT_V001.md
34  dda4722  818083a52165bc5c2ee86bd43e3b7e30d87f5c9eb82e54935e7829bb6f1f84e3  STAGE8_T7_CONNECTED_LINKED_CLUSTER_MAJORANT_DERIVATION_SPEC_V001.md
35  dcacb38  f7f93be82318ee036127363c0f24d8553814a8a44c2c6337b6dceac6dd247465  STAGE8_T7_GAMMA_GATE_CONTROL4_REPAIR_AMENDMENT_V001.md
36  bfde233  4fe8d42dc82879b1f0fad118554e4eb103c3a4a010e1e97304f1808b0d7dcb37  STAGE8_T7_COMPLETED_CONDITIONED_DUHAMEL_IDENTITY_AND_INTERCHANGE_SCHEMA_SPEC_V001.md
37  bfde233  ce20c82fa0454b1cb6e9128b2a4cfe4164615237acbfff3228b2c6ced4d02300  STAGE8_T7_I3_INTERFACE_BINDING_NOTE_V001.md
38  0c62299  5cc77b493c7876d644fe50a06c7862034c47eeb98584807b053c59d89d86ef5b  STAGE8_T7_SUPERSEDED_CHAIN_DISARM_DISPOSITION_V001.md
39  0c62299  b5c9408eebcadd518d1be5fcfabe531af0558ed953383a58531c7e7198d41d69  V005_VERIFICATION_RETURN_SEALED_TRANSCRIPT_V001.md
40  a55cac1  e1bb9e88580e20c1920d677a24b657f781760d1f9de4563a49fe2f014de3113b  D6_JOINT_REVIEW_RETURN_SEALED_TRANSCRIPT_V001.md
41  a55cac1  60223e6a175c5fee122f253491fd279daccfa15f8771af12104710f57ce09e5d  STAGE8_T7_D6_SPECS_REPAIR_AMENDMENT_V001.md
42  ec355f5  36e6ec72312beb299c0fba498dfcb7056b4f20576ab23a20ba11bbeb7907d433  DUHAMEL_VERIFIER_RETURN_SEALED_TRANSCRIPT_V001.md
43  ec355f5  6048b61f68f8e657a42aab44b35743c2d35365aae8c7a328c847895565b2b091  MAJORANT_PHASE1_RETURN_SEALED_TRANSCRIPT_V001.md
44  ec355f5  d05b115ae9f3c24f00451de089b9c9cc5f3836e6c0ba6cedc81af2eac30ae574  STAGE8_T7_D6_EXECUTION_ADDENDUM_AND_INTERRUPTION_RECORD_V001.md
45  ad73f20  bbc8bd6fb7e71159d4b80353998733df7235ccb6ae2b2da7fbc7aa42211f40f9  STAGE8_T7_GAMMA_BLIND_COMMITMENT_RELOCATION_RECORD_V001.md
46  9decedd  e01284594867c5e81776952ac3c7bc53db488e4566e9492a9d8c80728358ed8f  STAGE8_T7_CONTROLLER_V006_REPAIR_BINDING_V001.md
47  eb0b852  7e9dd224dd1cd97c63d79c40534bdc7c37aa22e7b580dc853bf9d9d0abeeb25f  EXTERNAL_BATCH_AUDIT_2026-07-26_return_and_dispositions.md
48  9ce3a11  10b4c6573e0f72e71bb0b6a8855d7a43ef02baf7fafe11653dc2c671849cace4  CONTROLLER_V006_AUTHOR_RETURN_SEALED_TRANSCRIPT_V001.md
49  9ce3a11  c855544c9beef653ee9e074349862b4c3a905641d2245cf04dc69a99add3ccee  STAGE8_T7_COMPLETED_CONDITIONED_DUHAMEL_IDENTITY_RESULT_V001.md
50  9ce3a11  fce4a19b14a657e58ef3d33e559d35c540c277e755deb3cfe9d70828b3350d79  STAGE8_T7_GAMMA_REFUTATION_GATE_RESULT_V001.md
51  9ce3a11  3c81647eb55ad01d4d71e23b2b45161427f82390098c95afa5721065206a7df2  STAGE8_T7_MAJORANT_PHASE2_STATUS_AND_O7_ESCALATION_V001.md
52  9ce3a11  8dd121e82638a19bd4922eadb951b5210a5078a3939c1fe0932f27086c5839b5  STAGE8_T7_RECORD_PARITY_LEMMAS_RESULT_V001.md
53  f06a999  aebff0466aab5cdf1dedb33871571f4f4f9bc93e28f81fc6fdf8a8cf1d74c6c5  STAGE8_T7_CONTROLLER_V006_REPAIR_BINDING_SUPPLEMENT_V001.md
54  f06a999  2508389d809a33cc8dff1bd4aa396ea5fecd5bf2ccccf03b6e2d495b4875850a  STAGE8_T7_QUARANTINE_BRIDGE_ROW_CONFLICT_FINDING_V001.md
55  518fb82  565acef4cbd4f444891edd93fcb3daeea311e981afb85ac6e3435d80185ffcf6  CALIBRATION_LEDGER.md   (LIVING; hash moves by design)
56  518fb82  18af67ce3d13488ef7d8d73283e5eb57ebc2ef7184cc509567a892a72780ecae  STAGE8_T7_BETA_ER_A_DISCLOSED_PREMISE_ADOPTION_V001.md
57  518fb82  65d54d6cf58e1e2a2f7f177444c68120c6989e09fa0402381796303781070425  STAGE8_T7_GAMMA_GATE_FINALITY_DECISION_RECORD_V001.md
58  09d8b07  67bb5cff532523daa60600bbd69517e4edf353d0425d255ae03e453567e6c271  STAGE8_T7_GAMMA_GATE_CONTROL4_V3_CONDITIONAL_AUTHORIZATION_V001.md
59  9bfc1d6  51f655a0a1bd3f20d7789f79e3ced16e08e56305521ebcafd4e9a7d4b8a3e528  ROUTE_MEMO_2026-07-26_ir_sea_kernel_attack.md
60  9bfc1d6  6c3e125ba7a43655b72ec75b218e64d1d5062213d5a10f740e89199cc1033aa1  STAGE8_T7_E1_RECLASSIFICATION_CORRECTIONS_AND_ESCALATION_V001.md
61  b65c152  d810c041fcba656a147e4f7b84db754155dd5d1771ef03b5b8e90df8e324c20d  CONDITION1_SAME_APPARATUS_ARGUMENT_SEALED_TRANSCRIPT_V001.md
62  b65c152  608eafb26c70cf3a4f2dc7b76e702eefcebf51514d37e72ab264663c20f78d47  STAGE8_T7_CONTROL4_CONDITION1_SAME_APPARATUS_RESULT_V001.md
63  b65c152  557c68a1aa5f75129dceb9261c393216a4e873a54ccbfc17915a0d0205fa8589  STAGE8_T7_CONTROL4_V3_SPEC_V001.md
64  7146d72  c4344f463a66082c140b28e2cfb6b27b3c3c739069d6da628ad5a1809ec57c9b  STAGE8_T7_CONTROL4_V3_RESULT_AND_L5_DETECTOR_SUPPORT_V001.md
65  f3bcdab  209aa39015c955e46ec84519c05b8de52e65288ba883e01590b245fcbfe0bb53  STAGE8_T7_MAJORANT_ARM_RESCOPE_PRINCIPAL_DECISION_V001.md
66  cdde49f  38e1517702f6ecb3792da9bb08334b4e344fb3d5bd4c2e1fac5bdc6ef08376a4  STAGE8_T7_Q2_TRIGGER_AND_CLASSIFICATION_STANDARD_V001.md
67  4104667  11512a7d6eba2ce647bf20310eb83caa4fbebaea7a658879c2be7e0eea685771  F8_REDERIVATION_RETURN_SEALED_TRANSCRIPT_V001.md
68  4104667  9cfafde1774e78b61b65d44858faf73f177c2ec75f323911473bae06a805ce7b  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V001.md
69  4104667  f84c30367e077ea722e2647696cb7e37374aa388056b444a3c236cd6dd1c5872  STAGE8_T7_F8_FIRST_HALF_RESULT_AND_TWO_NEW_FINDINGS_V001.md
70  bb97e42  e0a7151abdaf44ce9fc0c937b445fcc405ee142ef3792e0ddcf57a3135e9d20d  STAGE8_T7_QUARANTINE_COLLATERAL_V005_SUITE_RECORD_V001.md
71  83d47a2  19dbaccb14080c7db31a730f0acfda9d32a7ef46a39b83c2c59dacb7e3031acf  STAGE8_T7_QUARANTINE_NARROWING_RESTORATION_RECORD_V001.md
72  e950f46  d95c7a1657a2e6aedbf0f274a350c81da7bbd2b4b6975e6675b6b6cf1b6a86ab  E1_SPEC_HOSTILE_REVIEW_SEALED_TRANSCRIPT_V001.md
73  e950f46  3cacd4b748bbd1c67a3e49419da9728cda422f527236899fa36c6f293bc51b6d  F8_SECOND_HALF_REVIEW_SEALED_TRANSCRIPT_V001.md
74  e950f46  65a7b799f904a9d0fdaaafd7a462ff4258c3c3b4d1e7bf11ea46fe12881fd426  STAGE8_T7_C3_C5_REFUTATION_AND_F8_FLAG_ERRATUM_V001.md
75  eda4405  20b54b2e94c9213edfdfc4b9ee4820eeb75ad0fa6208b597cf65ae51d6c77e96  CODEX_ASSIGNMENT_A_E1_BLIND_RETURN_V001.md
76  eda4405  53717fca7d011eff70bb2fb2b6e598c59e21d8da04b0a20ef024ca98d59d7e9b  STAGE8_T7_E1_SPEC_REPAIR_BINDING_V001.md
77  5c14909  aa8758a9be4e9fa2171ad3817c069a9b946398137a79679218df8c7ba7bf36c9  STAGE8_T7_PRODUCTION_GATE_NOGO_AND_PIPELINE_REPAIR_BINDING_V001.md
78  07a8f88  fc4368c70140f477ecba6865e9db20b25d60ef5b095dd5f90148e7aa04fc6afa  STAGE8_T7_E1_REPAIR_BINDING_SUPPLEMENT_CODEX_RECONCILIATION_V001.md
79  ce491f7  994b99f5c157bce5efbb85694a67fcc7277a3197183c89b5014680b96f1863c2  STAGE8_T7_DIRECTORY_PERMISSION_FENCE_EVALUATION_AND_PROBES_V001.md
80  6bf3c28  9a0c20458c98b27aadeef0b2daee6329a0a6eef93ea78569c0a1e74a5fe20bb9  STAGE8_T7_D3_QUANTIFIER_READING_FREEZE_AND_LEMMA_CONSUMPTION_V001.md
81  e09c746  c373adba24baf35dd8e242eaebebf6a0cf157093f6ec7063da39a1842da132f4  STAGE8_T7_D3_FREEZE_RATIFICATION_AND_PREDICTION_WEIGHTING_RULE_V001.md
82  20cd32a  c1fed56342a113aea504da6f97d8d666172b9706872502c6bd2e3f229e81b557  STAGE8_T7_RULE6_RECOVERY_JUDGMENT_AMENDMENT_V001.md
83  2cffec7  782495eaa9bcfd123803f973ae4346a4cdaa2021a57e0eaba234666f979271e3  STAGE8_T7_ARM2_SHARPENING_AND_PROJECTION_TAIL_BINDING_V001.md
84  2cffec7  64605ab4c02c58bae2442baf22b8fe2134e66ceb50e2a71fc368603a1dbedf0d  STAGE8_T7_CODEX_BATTERY_RETURNS_AND_T16_INDEPENDENT_CONFIRMATION_V001.md
85  692e021  6b76117a8d6663ff2bf4785c43cb5c80913755b6933a1aa90caae06f18e9b9dc  STAGE8_T7_CYCLE7_PACKAGE_RECORD_AND_THREE_FINDINGS_V001.md
86  692e021  c8d693ce4081c6364f9cfe23ce703b7b8d58af79ee0b9121a249d5fb31edf47b  STAGE8_T7_E1_SPEC_V002_SEAL_RECORD_AND_RULE6_VERIFICATION_V001.md
87  692e021  468467303a109dc825b015107897dacc107800fc981030377c3f006b384cccb5  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md
88  692e021  d77dda56ec51a4e3cca0a7afd917a809b3dcd55b190d1e8c95c8fe948afb0250  STAGE8_T7_GENERATION_G7_COHERENCE_TABLE_V001.md
89  1193072  027708f05df3caa16c5e4810a2022ad9b6d4ca6cb1ea065683ad800e20662f96  STAGE8_T7_CYCLE7_PIPELINE_AUTHOR_LANE_RETURN_VERBATIM_V001.txt
90  1193072  28398c58e785a40e784fe2dfbf66316bdeca910ac21ccfe63a01c42b9254e128  STAGE8_T7_CYCLE7_VERIFICATION_RETURN_AND_FENCE_CLOSURE_V001.md
91  3fc6b9c  11d12ead907df8732dc9b53d4ace86d2cefb1ee49374c0e72f65d03dc36c23b7  STAGE8_T7_CONSTRUCTION_LANE_THREE_DEFECT_ERRATUM_AND_REVIEW_INCOMPLETENESS_V001.md
92  49083f7  0b7b7ea340cf1e22380b449330487e9a3533cfe65b1cc07c5f2eac707432f6ae  STAGE8_T7_PRIMARY_RESOLUTION_SUCCESSOR_SPEC_V001.md
93  49083f7  b7f3260f305c8839dfab63629de67bbf4909771ecaf51f7833da98fc5dd682ab  STAGE8_T7_PRINCIPAL_DECISION_PRIMARY_RESOLUTION_RELAY_RECORD_V001.md
94  96e7ab9  7af82798b92a7214cec3682ec432a7e019e497a6d74390a49aaa31abed4e16f5  STAGE8_T7_STEP3_BLOCKER_LADDER_DISCOVERY_AND_REVIEW_COMPLETION_V001.md
95  a376e66  cb56efd869d974fa4077d1caf0838ed3094da76b2a0a5079c5098eb5ac28c413  STAGE8_T7_ROW_AND_LADDER_CAPTURE_INSTRUMENT_V001.py
96  a376e66  839c138032c3239d468e3a3ea2d0803eca5dcbe24c9d5738f141ff6f76f94ec8  STAGE8_T7_ROW_AND_LADDER_CAPTURE_N48_DATA_V001.json
97  a376e66  df4033cd332f2ffc4fc133cea7174125f6ada88ee86f79d6d72c2d6a44ae9c10  STAGE8_T7_ROW_AND_LADDER_CAPTURE_N48_RESULT_V001.md
98  e293be6  14ddfc15f165ef411663f6b18f1189bce9e1374b755970f0fc0bf6c2996ce1b9  STAGE8_T7_CODEX_BATTERY_TIER2_RETURNS_V001.md
99  e293be6  810467de9d8274e59f192a0a829328857789973cc47fb1de43ee3b9db177df8f  STAGE8_T7_V003_AUTHORIZATION_CONDITIONS_AND_FROZEN_DIRECT_PREDICTIONS_V001.md
```

```text
READ THE INDEX THIS WAY: same commit = SIMULTANEOUS, no order claimed
between them. Different commit = the earlier commit's artifacts precede
the later commit's, by authority (a). The one LIVING row (55,
CALIBRATION_LEDGER.md) has a hash that moves by design; its listed value
is its value at the named commit, and it may not be cited as a fixed
authority.
```

## Protected status

```text
rule7_ordering_authority_adopted = true
filesystem_timestamps_admissible = false
timestamp_grounded_claims_audited = 4
claims_reground_on_push_order = 3     (W-2, W-3, W-4)
claims_reground_on_timestamp_free_evidence = 1   (W-1)
conclusions_changed_by_the_audit = 0
citation_index_artifacts = 99
production_authorized = false
alpha_computed = false
proof_authorized = false
```
