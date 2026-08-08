# STAGE 8 TASK 6 — CLOSING LEDGERS: FALSIFIER DISPOSITION + OBS RECONCILIATION

Lane: CODEX 2 / Builder A custody lane  
Version: V001  
Date: 2026-08-08  
Scope: sealed-byte compilation only; no claim construction, re-litigation, chain invocation, register edit, plan edit, tracker edit, or git action

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = none
```

## 0. Preflight, custody, and closed conventions

The output name and seal-sidecar name were absent in the cleanroom, and the
output name was absent in the archive workspace, before this file was written.
The accessible sealed questions register verifies at Q-617; the sealed
observation register verifies through OBS-22. The independently sealed lineage
V2 artifact was read only as a status input and was not edited.

This compilation uses the following closed mappings:

```text
FALSIFIER_DISPOSITION := one of
  {UPHELD, RETIRED, STANDING, STANDING-UNRESOLVED}.

OBS_DISPOSITION := one of {CONFIRMED, KILLED, OPEN}.

EVIDENCE_TAG := one of {PROVABLE, PART-PROVABLE, YOURS}.

UNCLAIMED, PARKED, FRAMING-UNDER-TEST, or an explicit OPEN with no later
complete confirmation or kill maps to OPEN.

A scoped partial confirmation does not close an observation whose own record
keeps a deciding condition open. A falsifier firing against the observation's
express strong form maps that registered form to KILLED even when the record
also preserves a narrower successor statement.
```

`UPHELD` is used only where sealed bytes say an attack fired or a registered
kill condition occurred. `RETIRED` is used only where the purported falsifier
was withdrawn as not well-formed for its target. `STANDING` names a 7A custody
step, and where execution lies later, names that later step too.

### 0.1 Sealed source manifest

Roots: `CR` = cleanroom;
`SUP` = `/Users/bgm/MB Work/alpha-program-archive/supervision`.
Line spans are one-based and bind to the exact file digest in this table.

| ID | Root / sealed source | SHA-256 | Load-bearing span or use |
|---|---|---|---|
| S01 | SUP `QUESTIONS_SETTLED_REGISTER_V001.md` | `07535259cde04db4c8d702f0870e97ea94a32a6f3534056134bf481308adc337` | Task 6 Q-552–Q-617; cited Q spans below |
| S02 | SUP `OBSERVATIONS_REGISTER_V001.md` | `ff68cc24c87b18d54051a8da9d69c82144cbc585e77f87f9487120bc1872ce2c` | OBS-01–OBS-22, L30–L815 |
| S03 | CR `STAGE8_TASK6_EVALUATION_DOR_LANE3_V006.md` | `30b17b2a0cedd09046a12d5733109cfedc74d181d394a23eecfb00597be2cc0b` | armed suite and dispositions, L484–L540; anti-tuning falsifier, L555–L570 |
| S04 | CR `STAGE8_TASK5_EQ6_COMPLETED_EXISTENCE_AXIOM_LANE2_V001.md` | `66c71bb619eac824b2d7d53fe36e49750945820428204f5b3db7f892bdfd1464` | F0–F7, L403–L418 |
| S05 | SUP `DOR_020_A8_GAMMA_BOTH_ROUTES_2026-08-05.md` | `0ee6c897055f803b31bc570b9f4ef852ccb3c4aba21fcd5274a7d740c8eb601d` | identification falsifier, L5–L20 |
| S06 | SUP `DOR_020_A9_XI_N_ADOPTED_2026-08-05.md` | `e0b661807f172337ad1cca1b89feec2b6472d531f6dbaae3bd3e39a953510c15` | four armed A9-era falsifiers, L6–L19 |
| S07 | CR `STAGE8_TASK5_XI_N_CANDIDATE_LANE3_V004.md` | `ac9335dc7a2e90ba088467ae0b6409d178c53950568be42af976469b5f917ede` | Z13/V3, L260–L354; Z-A7, L428–L465 and L750–L758 |
| S08 | CR `STAGE8_TASK5_COMMON_SEAMS_LANE3_V002.md` | `2525096ba06973b70064d6b9f9578470e0afca9c48e2cca6cf0f5c1194d12c52` | repaired R9, L352–L470; A7 lattice exit, L586–L594 |
| S09 | SUP `DOR_020_A4_J12_CONTACT_GLUE_STRICT_PUSHOUT_2026-08-04.md` | `5fd95472bd6f0507a371779505fe91e2c3c4657ee3afc664ca563a3743d668a4` | five A4 voids, L23–L27 |
| S10 | SUP `DOR_020_A5_CONTACT_LAPLACIAN_REDUCING_2026-08-04.md` | `5beccc617f4c5f5f76aba777c664f3dd4393f72257fc850950e2246109a7a424` | six A5 voids, L22–L27 |
| S11 | SUP `SLOT18_ADMISSIBILITY_PRINCIPAL_DECISION_2026-07-30.md` | `a132f4b2421610c7df4e9a8746286999b31672f1f2d805588ed3f1ad81ad6259` | F-U1/F-U2, L26–L35; F-C3, L44–L64 |
| S12 | CR `STAGE8_TASK6_DOR_V002_CONFIRM_LANE3_V001.md` | `93b516c57bd18ded9a52455c6272b5f5e9aebdea0b6d39e716b2add681fed192` | F-1/F-2 fire, L400–L429 |
| S13 | CR `STAGE8_TASK6_DOR_V003_RECONFIRM_LANE3_V001.md` | `8cc53e9b1f6f1742040ed896b6aa687a26580b69a034627a7c7cc4e5d66551e3` | F-1 closed by two prohibitions, L135–L156 and L363–L367 |
| S14 | CR `STAGE8_TASK6_LP_QSPEC_ASSEMBLY_REVIEW_LANE3_V001.md` | `f8bfff5bb01ce33f2e973a9ae58fb80bd07650dd9f0d83f02202eda9b3bc48ee` | F-S18 not well-formed, L413–L424 |
| S15 | CR `STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V005.md` | `76589e94bb4af318880c61c3d677dc2518add8480100a7afaf675e4dd3a394a8` | F-S18 withdrawal, L397–L411 |
| S16 | CR `STAGE8_TASK5_CHAIN_CONFORMANCE_AUDIT_LANE3_V002.md` | `44202c060821728fba2c46b81b82487002e639f3242565b7a5fed387e41fcae8` | two permanent modulus regressions, L348–L430 |
| S17 | CR `STAGE8_TASK5_AUDIT_V002_REVIEW_DARIO_V001.md` | `af955f8159e1cc4c464966d38070ddbda501828b39630a9f585e86ce7693e610` | independent rerun, L61–L83; open route falsifier, L245–L259 |
| S18 | CR `STAGE8_TASK6_LP_MATRIX_LEDGER_REVIEW_DARIO_V001.md` | `a83289e67615d6faa2c1c942105ee6b595034f78d31fcf4e16ac5366fd1d7743` | A25/A27 hold no negation or counterexample, L154–L161 |
| S19 | CR `STAGE8_TASK6_LINEAGE_V2_MATRIX_CODEX2_V001.md` | `fe4c083d915c00824575fe6ae53339500a805f4c1fd0b5f3174a74fdb8c9dba8` | read-only current board input; no modification |
| S20 | SUP `ROAD_FROM_HERE_THROUGH_GRAVITY_V001.md` | `3f8fac1f270f8526a08048ba4109d9ce32a6b2236ac9fee29c76c1f82260e082` | 7A steps 6–14, L15–L32; 7B steps 21–24, L44–L50 |
| S21 | SUP `NOTE_7A_RECOGNITION_SPEC_REQUIREMENT_2026-08-08.md` | `49aed793fb77247a3b38ec0b39822840b3ca06a6ae5dd48e876f0767a8689b7c` | OBS-22 recognition preregistration, L7–L25; correspondence channel, L28–L43 |
| S22 | CR `STAGE8_GAMMA_K_SOURCE_RECORD_COMPOSITION_TYPING_TESTS_V001.md` | `1fa7c918d6c397320e1e7db06b2a5b271a648a25fa695a86ad01056e1f62e17f` | OBS-04 owner |
| S23 | CR `STAGE8_GAMMA_K_FINITE_REVERSIBLE_WRITE_OBS05_TEST_V001.md` | `b4250480a9f4d3fc4b4b4d7db8e6a1dcfe2e6149ca8947dc8051d407cfd5e47d` | OBS-05 kill owner |
| S24 | CR `STAGE8_GAMMA_K_NONRETURN_CHARGED_SPECTRUM_OBS06_TEST_V001.md` | `2f99c574b55fc8c0b2af414547c899db2df91734f3c303627218f526f78144fc` | OBS-06 kill owner |
| S25 | CR `STAGE8_INSIDE_OUTSIDE_CONSISTENCY_CONDITION_EINSTEIN_V001.md` | `15793db5d7869356947cea69b7541db96d23b351692c8543314bf9e4bcf15184` | OBS-10 Step-6 kill owner |
| S26 | CR `STAGE8_OBS11_AXIS_COLLAPSE_ATTACK_V001.md` | `63e8301ffa967dc158cd7d10a70826da705d67515420558909da0098b0f4f3ef` | OBS-11 kill owner |
| S27 | CR `STAGE8_DOWNSTREAM_SMOOTH_CONNECTION_REQUIREMENT_AUDIT_V001.md` | `46bfeb7d1c05a70661caa473cb47700efce70d074507563de8af576f26e7c207` | OBS-12 shape-confirmation owner |
| S28 | CR `STAGE8_RESPONSE_STATE_FACTORIZATION_TEST_FIXTURE_RESULT_V001.md` | `e8ce5095f02d8291b43350880fff40b0362d1c81f2d1bbc5b51b41db3926d770` | OBS-14 kill owner |
| S29 | CR `STAGE8_TASK4A_N_UNIQUENESS_GERM_V007_AND_FULL_DOOR_D_CROSS_VERIFICATION_V001.md` | `6e36bf05d653b0874579d796e4e8c3c0a9a9a70ad2cd87fb65a0814fe736d0b5` | OBS-16 supporting confirmation |
| S30 | CR `STAGE8_TASK4A_DETERMINER_DOOR7_CROSS_REVIEW_LANE2_V001.md` | `d738661e1e8038bd0a4a7f7121e244b15dffab76d5fad7ca2584017ebff49b14` | OBS-17 correction/partial build owner |
| S31 | CR `STAGE8_TASK4B_REPRESENTATIVE_INDEPENDENCE_LANE1_V001.md` | `f0f8b09b1aa6a16c0ed0dffedbd275aba9e647fb5841fc8ce06ce9e6a8b00857` | OBS-19 first-confirmation owner |
| S32 | CR `STAGE8_TASK5_EQ6_V003_CHECK_AND_PACKAGE_R_TYPING_LANE1_V001.md` | `99c34408b86f93a343b372595bb7f7b199501b1eaab4ef241d5aea2f853f9757` | OBS-20 strong-form kill owner |
| S33 | CR `STAGE8_TASK6_JII_BETA_IDENTIFICATION_DARIO_V001.md` | `8e31df94fd2076cdb7803b0c516457fee577538f290f2ace3679cf1f4cfa4a76` | OBS-22 source owner |
| S34 | CR `STAGE8_SLOT18_Q34_NATIVENESS_AND_HOLONOMY_BRIDGE_RESULT_V001.md` | `8abb40899bda75d90a36c17448ced180df311e55aa50d10f66fa01c1f024d095` | OBS-01 source owner |
| S35 | CR `STAGE8_MODULAR_CONJUGATE_ENERGY_LIMIT1_APPLICABILITY_RESULT_V001.md` | `73a5a36c9de72a476fcb5f8dacd1615383c05a6dc4d9407c8e7406265a9fcd94` | OBS-02 source owner |
| S36 | CR `STAGE8_TASK5_XI_N_V004_REVIEW_DARIO_V001.md` | `cdd54b94d44cd9d3d8db9eb1ed4a2560ba2ce49ff464b9a1a8f0cbf42e3b07bd` | repaired R9 oddness/type distinction, L263–L270 |

## 1. Falsifier disposition ledger

Closed row schema:

```text
{
  id: unique string,
  falsifier: registered test or void,
  trigger: exact bounded failure condition,
  disposition: FALSIFIER_DISPOSITION,
  consequence_or_7A_owner: string,
  tag: EVIDENCE_TAG,
  citations: nonempty list of source-ID with optional line-span;
             every source-ID resolves to the pinned digest in §0.1
}
additionalProperties = false
```

The Task 6 DoR's final carried roster is the census root: F0–F7, the four
A9-era falsifiers, A4/A5 voids, the comparator falsifiers, counterexample
regressions, and fail-closed conversion/selection attacks (S03:L524–L540).
Task 6's own fired and withdrawn attacks and the observation-register
falsifiers are then added once. Descriptor negative controls, BR candidate
tests, and A25/A27's demand that future certificates carry falsifiers are not
registered falsifiers and are not inflated into rows. S18 verifies that A25
and A27 have no current negation or counterexample.

| ID | Falsifier | Trigger | Disposition | What it killed, or 7A owner | Tag | Citation |
|---|---|---|---|---|---|---|
| F01 | Axiom F0 — typing | Actual carriers or any domain/codomain make the completed-existence proposal ill-typed. | STANDING | 7A-10/11 construct and formalize carriers; 7A-13 reruns the full lineage. | PROVABLE | S04:L403–L414; S03:L524–L532 |
| F02 | Axiom F1 — finite | An instance fails DoR-008 exact finite restrictions. | STANDING | 7A-10 supplies the charged package; 7A-13 replays finite restrictions. | PROVABLE | S04:L407–L414 |
| F03 | Axiom F2 — geometry | Support, bundle, cycle-creation, or covariance regressions fail. | STANDING | 7A-6 junction and 7A-8 stitching; 7A-13 lineage rerun. | PROVABLE | S04:L407–L414 |
| F04 | Axiom F3 — joint | No single `W` satisfies J1–J15 simultaneously; separate witnesses do not substitute. | STANDING | 7A-6/8 joint junction-stitching work; 7A-13 rerun. | PROVABLE | S04:L409–L414 |
| F05 | Axiom F4 — conservativity | A finite consequence does not reduce to the sealed finite datum `F`. | STANDING | 7A-10/11; 7A-13 rerun. | PROVABLE | S04:L410–L414 |
| F06 | Axiom F5 — completion | Exhibit a qualifying `F` for which no allowed completed witness `W` exists. | STANDING | 7A-10 charged completion work; 7A-13 rerun. | PROVABLE | S04:L411–L414 |
| F07 | Axiom F6 — downstream structure | Conditional C1–C3, symbol, or return interfaces fail to commute on `W`. | STANDING | 7A-6/7/8/10 and 7A-13. | PROVABLE | S04:L412–L414 |
| F08 | Axiom F7 — final sealed test | A future duly bound package gives a wrong final sealed result. | STANDING | 7A-13 owns carriage into the complete lineage; Phase-III-17 owns execution. One member cannot refute the family without rigidity. | PROVABLE | S04:L413–L418; S03:L534–L540 |
| F09 | A9-1 / A8 identification, repaired diagonal form | On one common formed cell, the H and HOL orbit-return sections disagree. | STANDING | 7A-6 junction arc; the two routes must be formed before the comparison can run. | PROVABLE | S05:L5–L12; S06:L16–L19; S08:L352–L470 |
| F10 | A9-2 — R9-generated oddness | The HOL composite period fails the repaired address-orbit oddness requirement on formed gate data. | STANDING | 7A-6 junction/route realization; it does not by itself prove `Xi` parity. | PART-PROVABLE | S06:L16–L19; S07:L210–L218; S36:L263–L270 |
| F11 | A9-3 — Z13 one-element counterterm void | Once FULL-G4 is formed, one `x_*` lies in `CT_N`, placing cycle support outside record-support closure. | STANDING | 7A-6 junction realization and 7A-13 replay. | PROVABLE | S06:L16–L19; S07:L260–L354 |
| F12 | A9-4 — Z-A7 one-element refutation | One addressed identity-branch tuple has `p_x` outside `2 pi Z`. | STANDING | 7A-6 route realization; 7A-13 lineage replay. | PROVABLE | S06:L16–L19; S07:L428–L465; S07:L750–L758 |
| F13 | A4 void 1 — unequal overlap images | Represented and boundary images differ on an actual overlap element. | STANDING | 7A-8 stitching certificates; 7A-13 rerun. | PROVABLE | S09:L23–L27 |
| F14 | A4 void 2 — deleted visible bulk cycle | Strict gluing deletes a `D_G^*`-visible bulk cycle. | STANDING | 7A-8; 7A-13. | PROVABLE | S09:L23–L27 |
| F15 | A4 void 3 — structural-law failure | Beta cocycle, restriction, reality, units, Ward, OLD_FID, RNL, LR, or subextensivity fails. | STANDING | 7A-8; 7A-13. | PROVABLE | S09:L23–L27 |
| F16 | A4 void 4 — outcome-selected automorphism | A contact automorphism is selected from response, threshold, fixed point, end test, or numerical consequence. | STANDING | 7A-8 anti-tuning custody; 7A-13. | PROVABLE | S09:L23–L27 |
| F17 | A4 void 5 — actual nontrivial contact twist | Actual contact data exhibit a twist inconsistent with the adopted member. | STANDING | 7A-8; 7A-13. | PROVABLE | S09:L23–L27 |
| F18 | A5 void 1 — nonreducing actual contact vector | An actual contact vector has a noncontact component in `Delta_N^Hdg c`. | STANDING | 7A-8; 7A-13. The prior abstract countermodel was not actual record-surface data. | PROVABLE | S10:L22–L27; S01:L12653–L12691 |
| F19 | A5 void 2 — inherited A4 failure | A4 overlap equality or any A4 void fails. | STANDING | 7A-8; 7A-13. | PROVABLE | S10:L22–L27 |
| F20 | A5 void 3 — deleted visible/harmonic cycle | A `D_G^*`-visible bulk or harmonic cycle is deleted. | STANDING | 7A-8; 7A-13. | PROVABLE | S10:L22–L27 |
| F21 | A5 void 4 — structural-law failure | Reality, units, restriction, OLD_FID, RNL, or LR fails. | STANDING | 7A-8; 7A-13. | PROVABLE | S10:L22–L27 |
| F22 | A5 void 5 — outcome-selected complement/member | A contact complement, commutator, or member is chosen from a reader or later outcome. | STANDING | 7A-8 anti-tuning custody; 7A-13. | PROVABLE | S10:L22–L27 |
| F23 | A5 void 6 — refinement incoherence | Common-refinement coherence fails for the reducing family. | STANDING | 7A-8 stitching; 7A-13. | PROVABLE | S10:L22–L27 |
| F24 | F-U1 — unbounded/unsearchable lineage | Rule-11 complete-history scope proves unbounded or unsearchable. | STANDING | 7A-13 owns custody in the sealed lineage; 7B-23 owns the S18 eligibility execution. | PROVABLE | S11:L26–L35 |
| F25 | F-U2 — derivation contamination | A candidate passes appearance screening but is later shown to have shaped the construction. | STANDING | 7A-13 custody; 7B-23 execution. | PROVABLE | S11:L29–L35 |
| F26 | F-C3 — comparator fence breach | Comparator-precision clause cannot be applied without a measured central value. | STANDING | 7A-13 custody; 7B-23 eligibility/comparator execution. | PROVABLE | S11:L44–L64 |
| F27 | Task6 `(F-1)` row-8 countermodel | Result seal and parents certified while gate 7 is false, yet V002 row 8 admitted the numeric act. | UPHELD | Killed V002's rendered prerequisite sufficiency and forced the V003 two-prohibition repair. | PROVABLE | S12:L400–L429; S13:L135–L156 |
| F28 | Task6 `(F-2)` fresh-attack verdict | `row8_prerequisites(F-1)=true` while `symbolic_first(F-1)=false`. | UPHELD | Killed the V002 custody-only bypass; V003 closes it by the conjunction and symbolic-first clause. | PROVABLE | S12:L419–L429; S13:L147–L156 |
| F29 | `(F-S18)` | Noninteger assignment, inhabitance failure, or Z3 typing failure offered against “derived, not imposed.” | RETIRED | It did not falsify the provenance headline; V005 withdraws it pending a valid S18 candidate. | PROVABLE | S14:L413–L424; S15:L397–L411 |
| F30 | A7 certified-lattice exit | One formed branch exits its certified full-cell lattice. Missing certificates are pending, not an exit. | STANDING | 7A-13 owns carriage; Phase-III-17 owns the structural end-test execution. | PROVABLE | S03:L515–L523; S08:L586–L594 |
| F31 | Permanent modulus regression A — translated isometry | A same-metric quotient must score `q^per=1`, not the rejected mixed-metric `1/2`. | UPHELD | Killed the mixed-metric modulus rendering; V002 scores the regression exactly. | PROVABLE | S16:L348–L391; S17:L61–L83 |
| F32 | Permanent modulus regression B — quarter contraction | A same-metric quotient must score `q^per=1/4`, not the rejected mixed-metric infinity. | UPHELD | Killed the mixed-metric modulus rendering; V002 scores the regression exactly. | PROVABLE | S16:L393–L430; S17:L68–L83 |
| F33 | Undeclared cross-sector conversion | A consumed cross-sector arrow lacks a declared carrier/unit factorization or silently sets the factor to one. | STANDING | 7A-6/8/10, with replay at 7A-13. | PROVABLE | S03:L526–L532; S03:L555–L570 |
| F34 | Residual `counterexample regressions` umbrella | Task 6 carries this class but supplies no closed member list; F31/F32 are the only named members located in the bounded sweep. | STANDING-UNRESOLVED | 7A-11 formalization and 7A-13 lineage custody; registrar must rule the missing census rather than accept an inferred roster. | PART-PROVABLE | S03:L524–L532; S16:L348–L430; S17:L61–L83 |
| F35 | OBS-15 falsifier | One forced state datum is not derived through a transition fact. | STANDING | 7A-9 preparation principle; 7A-13 rerun. | PROVABLE | S02:L640–L659 |
| F36 | OBS-16 falsifier | A ratified `Gen_Omega` rule requires a state-side primitive that no transition requirement pins. | STANDING | 7A-9 preparation principle; prior strong-reading failure did not meet this exact ratified-draft condition. | PART-PROVABLE | S02:L663–L673; S01:L10409–L10415 |
| F37 | OBS-17 falsifier | A residue item derives from record structure alone, or the EM phase line requires authored amplitude content. | STANDING | 7A-6 junction, 7A-8 stitching, 7A-10 charged package; 7B-21/22 later GR confirmation. | PART-PROVABLE | S02:L677–L711 |
| F38 | OBS-18 three-arm falsifier | Amplitude/registration derives from phase alone; a require fact fixes without amplitude; or weights become depth-sensitive. | STANDING | 7A-6/10; 7B-21/22. | PROVABLE | S02:L713–L723 |
| F39 | OBS-19 two-arm falsifier | Completed family becomes fully finite-derived, or the finite/continuum seam dissolves. | STANDING | 7A-6/8 builds the junction/stitching evidence; 7B-22 owns final confirmation/kill. | PART-PROVABLE | S02:L726–L742; S31 owner |
| F40 | OBS-20 falsifier | A genuine locality component—especially disjoint-sector independence—is derived from ratified record content. | UPHELD | Killed OBS-20's strong prediction: relative no-leakage is constructible. The narrower “what lives where” residue survives separately. | PROVABLE | S02:L744–L770; S01:L12319–L12324; S32 owner |
| F41 | OBS-21 registered kill suite | Re-review refutes the typing, inhabitance fails structurally, or the discrete sector is empty. | UPHELD | The first arm fired against the exact headline: integrality is authored, not derived. This is distinct from malformed F-S18. | PROVABLE | S02:L783–L803; S01:L13329–L13340; S14:L413–L424 |
| F42 | OBS-22 kill suite | The two maps collapse to one; a third crossing breaks one-locus typing; or Einstein-limit work relocates the junction. | STANDING | 7A-6 is the opening test under S21's recognition preregistration; 7B-22 owns final confirmation/kill. | PROVABLE | S02:L805–L815; S20:L15–L20; S20:L44–L49; S21:L7–L25 |

Disposition count check:

```text
UPHELD              = {F27,F28,F31,F32,F40,F41}                  = 6
RETIRED              = {F29}                                      = 1
STANDING             = {F01-F26,F30,F33,F35-F39,F42}             = 34
STANDING-UNRESOLVED  = {F34}                                      = 1
TOTAL                = 42
```

## 2. Observation reconciliation ledger

Closed row schema:

```text
{
  obs_id: /^OBS-(0[1-9]|1[0-9]|2[0-2])$/,
  registered_statement: string,
  disposition: OBS_DISPOSITION,
  owner_and_bounded_basis: string,
  test_ownership: string,
  tag: EVIDENCE_TAG,
  citations: nonempty list of source-ID with optional line-span;
             every source-ID resolves to the pinned digest in §0.1
}
additionalProperties = false
```

For OBS-21 and OBS-22, `registered_statement` below reproduces the exact
pre-registered claim from S02, not a paraphrase.

| OBS | Registered statement | Disposition | Owning artifact and bounded basis | 7A / 7B test ownership | Tag | Citation |
|---|---|---|---|---|---|---|
| OBS-01 | `Z_Q` is dimensionless because it is alpha's reciprocal—so the access impedance is the coupling. | OPEN | S34 owns the original observation; the Slot-18 disqualification stands, while the theory-content identity remains explicitly unestablished. | 7A-10 may supply the charged response object; no 7B test is yet registered specifically for this framing. | PROVABLE | S02:L30–L53; S34 |
| OBS-02 | Nobody has asked what the modular structure of a record algebra is. | OPEN | S35 refutes one free-field applicability route, not modular structure in general; the register keeps the question unclaimed. | No named 7A critical-path owner; it remains banked unless a 7A consumer names it. | PROVABLE | S02:L57–L83; S35 |
| OBS-03 | The coupled gravity–EM surface saddle's content was never mined. | OPEN | The sealed observation preserves unused ordering/failure content while its direct `Gamma_K` substitution remains closed. | 7A-6 junction work is the nearest lawful consumer; no result is preregistered. | PROVABLE | S02:L87–L111 |
| OBS-04 | The record carrier exists before the source acts; only durability is generated. | CONFIRMED | S22 returns the carrier/durability type split; the principal-confirmed premise is recorded in OBS-05's opening. | 7A-10 consumes the source/record distinction; no 7B retest required by the record. | PROVABLE | S02:L116–L152; S22 |
| OBS-05 | If alpha is the impedance of the durability-conferring action, it is the impedance of the write. | KILLED | S23 proves the write is forced to unit strength and carries no surviving coupling parameter. | No carry as a live observation; the response-side residue proceeds through 7A-10. | PROVABLE | S02:L147–L205; S01:L1868–L1889; S23 |
| OBS-06 | Alpha runs through charged particles—and non-return may run through the same spectrum. | KILLED | S24 proves non-return generic and not charged-sector consuming; the proposed structural common cause closes. | No live 7A falsifier; charged response and durability remain separate work in 7A-10. | PROVABLE | S02:L209–L242; S01:L1984–L1991; S24 |
| OBS-07 | An underived magnitude sits in the write-tail join—at a stage nobody enumerated. | OPEN | Q-53/observation record types the join and exchange magnitude TYPE-U; no later sealed closure was located. | 7A-10 charged Q-spec owns the missing physical write-tail construction. | PROVABLE | S02:L246–L276; S01:L2233–L2238 |
| OBS-08 | If the rank-1 object has a common origin, the dependency-graph model may not apply to it. | OPEN | The graph-walker prediction was refuted only on six returns; the ontology question was explicitly parked and remains `NO_VERDICT`. | 7A-10/13 only if the common-origin producer becomes a blocking graph issue. | PART-PROVABLE | S02:L280–L318; S01:L3425–L3428; S01:L4957–L4967 |
| OBS-09 | The N6 opening is two steps from `B0`, and the second step does not exist. | CONFIRMED | Gate-history premise corrected, but the no-bridge conclusion survives and is strengthened: BID is determined and `B0` remains unmapped. | 7A-10 owns any future bridge that would reopen it. | PROVABLE | S02:L322–L395; S01:L5289–L5296 |
| OBS-10 | The two routes are the inside and outside views of one surface—so `beta` is the dictionary, and their agreement is a condition on it. | KILLED | S25 refutes Step 6, the operational condition on `beta`; Step 5 survives only as an undefeated inference and is not promoted. | The residue is carried into 7A-6 junction work and 7B-22 beta-era work, but the registered operational claim is killed. | PART-PROVABLE | S02:L399–L465; S01:L5890–L5940; S25 |
| OBS-11 | Every derived result is fixed-instance; §5.3 requires family-uniformity; that mismatch is the whole blockage. | KILLED | S26 executes the requested cross-case attack and separates family-uniformity from sector-reach. | No live observation; both independent requirements remain in 7A-10/13. | PROVABLE | S02:L477–L571; S01:L6581–L6619; S26 |
| OBS-12 | Smoothness lives in the fiber, not the base. | CONFIRMED | S27 confirms the shape: the smooth-required subset is exactly the continuum-limit obligations; it remains framing, not a theorem. | 7A-8 refinement/stitching tests the emergent-limit side; 7B-21 owns the Einstein limit. | PART-PROVABLE | S02:L593–L600; S01:L8817–L8846; S27 |
| OBS-13 | Alpha-in-the-electron versus induced: the fixed point is where they agree. | OPEN | The record labels it framing and the fixed point has not executed. | 7A-10 constructs its inputs; Phase-III-16 owns the fixed-point test. | PROVABLE | S02:L604–L616; S20:L34–L38 |
| OBS-14 | The state may be a role, not an object. | KILLED | S28's preregistered fixture gives zero versus nonzero response operators for two admissible states. | Killed at the response producer; 7A-9 owns the localized response-relevant state class. | PROVABLE | S02:L620–L636; S01:L9474–L9492; S28 |
| OBS-15 | The allow/require boundary is the transition/state divide. | OPEN | Its one-state-datum falsifier remains armed; no sealed firing was located. | 7A-9 preparation principle; 7A-13 rerun. | PROVABLE | S02:L640–L659 |
| OBS-16 | Only transition requirements can force the origin state; allow-shaped generation contributes only gauge. | OPEN | The strong reading failed at the anchor derivation, while the exact ratified-draft falsifier did not fire; S29 supplies later supporting require-forcing evidence. | 7A-9 preparation principle. | PART-PROVABLE | S02:L663–L673; S01:L10409–L10415; S29 |
| OBS-17 | The derivable/authored provenance split is the EM/GR emergence split. | OPEN | Evidence supports and narrows the split; S30 kills the overbroad Door-7 declaration and leaves a narrower unbuilt interface. | 7A-6/8/10; 7B-21/22 supplies the gravity-side confirmation test. | PART-PROVABLE | S02:L677–L711; S01:L11441–L11469; S30 |
| OBS-18 | GR is the allow/require boundary-former; amplitude/weight writes the record. | OPEN | The sealed register leaves all three falsifier arms open. | 7A-6/10; 7B-21/22. | PROVABLE | S02:L713–L723 |
| OBS-19 | The completed-family underdetermination is the start of the continuum. | OPEN | S31 fires the preregistered NOT_INVARIANT branch, but whether the freedom enters alpha remains open. | 7A-6/8 builds the seam; 7B-22 owns the final confirmation/kill. | PART-PROVABLE | S02:L726–L742; S01:L11983–L11999; S31 |
| OBS-20 | Package R is the locality postulates of field theory: the record layer supplies everything algebraic; “where” is boundary-former content. | KILLED | S32 fires the registered strong-form falsifier: relative disjoint-sector independence is constructible. The narrower where-content survives as a successor statement. | The surviving where-content rides 7A-6/8; the exact registered strong observation is killed. | PART-PROVABLE | S02:L744–L781; S01:L12319–L12324; S32 |
| OBS-21 | **Exact preregistration:** “The claim: on the record surface, the source-to-loop threading assignment is a topological charge — integer-valued by structure (the winding lattice; periods mod 2π; discontinuity at zero and at every support-birth boundary as the DEFINING property, not a defect) — so charge quantization is derived, not imposed. Source: the Ξ_N V003 clause (Z3) and its physical reading (\"which loop a source encircles cannot vary continuously to no loop at all\"), `STAGE8_TASK5_XI_N_CANDIDATE_DARIO_V003.md`.” | KILLED | Q-556/S14 establish that integrality is the authored codomain condition and A9 inhabits nothing; the exact “derived, not imposed” headline is refuted. A narrower conditional-discontinuity statement is not this headline. | 7A supplies no decisive OBS-21 test. 7B-22 owns confirmation/kill of the beta-era companion; 7B-23 owns any lawful S18 prediction candidate. | PROVABLE | S02:L783–L803; S01:L13329–L13340; S14:L413–L424; S20:L44–L49 |
| OBS-22 | **Exact preregistration:** “The claim: the correspondence boundary between the record's interior (internal, unit-normalized, dimensionless) and measured physics (dimensional, external) is ONE physical locus crossed by (at least) TWO independent missing maps — the Ward-symbol realization (LP-JII/Phitilde) and the length normalization (the era-1 beta gap) — same genus, same junction, disjoint domains; every lawful crossing declares its unit (A2 clause 8). Source: the identification determination (`8e31df94…`), Q-542. If confirmed by Task 7's charter work, the junction is gravity-side content (the where/how-much of external realization) and \"closing one map is not closing the boundary\" is its law. KILL CONDITIONS: a sealed derivation collapsing the two maps into one; or a third crossing map appearing that breaks the one-locus typing; or Task 7's Einstein-limit work relocating the junction. Companion: OBS-21; the beta gap's two-era typing files with this.” | OPEN | S33 identifies one locus/two maps; neither confirmation nor a kill has run. S21 requires a frozen record-native recognition spec with three verdicts and a zero-weight correspondence channel. | **7A-6 is the junction arc's opening test under the recognition preregistration.** 7B-22 owns the later confirmation/kill after the Einstein-limit/beta-era work. | PROVABLE | S02:L805–L815; S01:L13191–L13195; S20:L15–L20; S20:L44–L49; S21:L7–L25; S33 |

Observation count check:

```text
CONFIRMED = {OBS-04,OBS-09,OBS-12} = 3
KILLED    = {OBS-05,OBS-06,OBS-10,OBS-11,OBS-14,OBS-20,OBS-21} = 7
OPEN      = {OBS-01,OBS-02,OBS-03,OBS-07,OBS-08,OBS-13,
             OBS-15,OBS-16,OBS-17,OBS-18,OBS-19,OBS-22} = 12
TOTAL     = 22
```

## 3. Bounded-search and verb audit

### 3.1 M-2 disposition search

| False-negative mode | Check | Result |
|---|---|---|
| literal/regex | fixed-string searches for `falsifier`, `FALSIFIER`, `F-`, `void`, `kill condition`, `counterexample regression`, and OBS identifiers across the questions register, observation register, Task 6 matrix ledgers, DoR chain, Q-spec chain, and sealed Task 6 artifacts | named suites and Task 6 attacks located |
| whitespace/reflow | line-numbered reads plus whitespace-insensitive context searches | A4/A5 and A9 lists recovered from their sealed decisions rather than summary prose |
| scope/self-reference | historical delta/certificate mentions separated from operative decisions; descriptor negative controls and BR checks excluded unless explicitly typed as falsifiers | no historical mention double-counted |
| hyphenation/identifier | `F0-F7` / `F0–F7`; `F-U1` / `F_U1`; `A9-era`; `F-S18`; `STANDING-UNRESOLVED`; `OBS-01` / `OBS-1` checked | identifier variants reconciled |

The one bounded negative that remains load-bearing is F34: S03 names the
counterexample-regression class but provides no closed membership list. The
matrix review independently confirms that A25/A27 have no current negation or
counterexample (S18). Neither absence is converted into a claim that no such
object exists.

### 3.2 `F_PLDEC`, authority, and verdict-scope audit

No desired physical result, reader value, measured constant, target value,
member, route, or branch was consumed to assign a disposition. The observation
statuses reproduce sealed outcomes or explicit open states. `CONFIRMED` on
OBS-12 is explicitly scoped by `PART-PROVABLE` to “confirmed in shape”; KILLED
on OBS-10 and OBS-20 preserves their surviving narrower residues rather than
silently deleting them. F-S18's retirement and OBS-21's kill are nonconflicting:
the former did not target provenance, while the latter's independent typing
condition fired against the provenance headline.

### 3.3 YOURS audit

No disposition required a new substantive ruling. Every row is tagged
`PROVABLE` or `PART-PROVABLE`; there are no `YOURS` rows to place before the
registrar. F34 is unresolved by rule, not self-ruled.

---

FALSIFIERS = 42 total (6 upheld / 1 retired / 34 standing / 1 unresolved)
OBS = 22 total (3 confirmed / 7 killed / 12 open)
YOURS_ROWS = 0 (none for registrar ruling)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
