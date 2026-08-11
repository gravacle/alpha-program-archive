CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
PREDECLARATION_REGION = EMPTY (closure opens at byte 0; no text precedes it)
PREDECLARATION_OUTPUT_SCAN = 0 hits in authored prose (27-token sweep)
VERDICT_BEARING_SET = exactly the 7 content-addressed members below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
LANE = DARIO   ROLE_THIS_RELAY = BUILDER (not verifier)
ALL_OBJECTS = CLAIMED until the opposite-lane check
TUPLE_PARSE_REPLAY = part of this seal discipline; every tuple re-parsed at its declared count
```

| # | Closed member | SHA-256 | Role |
|---:|---|---|---|
| 01 | `relay_inbox/RELAY_PASTE_969_FAMILIES_V004_DARIO_V001.md` | `1ca436155ecb7b18376a84f6111ca8111b6c6178a4b6b2b6e389bf25eead8f4f` | assignment |
| 02 | `STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V004.md` | `a195edb03b36be44bf8ce1b71dbf1a01a3a0956c4afc65ddf17382cdca4ed0ab` | the **governing** instrument (approved Q-881); the closed suite schema and aligned JAC-14 row |
| 03 | `STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V003.md` — `G_joint` `[13731,14294)`; `Delta_0^joint` `[13565,13639)` | `105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f`; `bb73a8ec8816bddc9c84d84e48ca81bd8d315f316092cdf295dc8fb474e2826f` | the candidate grammar and defining conditions, byte-identical in V004 |
| 04 | `JOINT_ANCHOR_DECISION_INSTANCE_V003.md` — BI tag `[7250,7299)`; BI content `[7300,7469)` | `089af246cbc0d66e6ce70971dbb14d355a78ee0f5e294706a1acaeacd0d4236d`; `9a42dac44da482d07f186040d6e62edb85c23c0c886858a14ba8ce63e0d3a72c`; `19585bb3d660895ca65f1c52b0d97903f96257ec02ec5fd4b21b3b26a2146d38` | **where the principal's entries actually live** — the carrier, the fiber, the entered `{BI}` tag and BI content |
| 05 | `STAGE8_AXN_FOR_CLASS_FAMILIES_DARIO_V003.md` | `25845e9223e62374df699b474f0770191ef731f8123f2299b21af9683bf1b581` | my 966, whose mathematics is byte-carried |
| 06 | `STAGE8_AXN_FAMILIES_V003_CROSSCHECK_CODEX2_V001.md` | `ff587bada82efa5d829422fa33ac7116b727a774d4112a4e02c7ac00f1d58d52` | the check confirming the mathematics and ruling the five packaging items |
| 07 | `STAGE8_AXN_ENTERED_OBJECTS_BUILD_CODEX2_V002.md`; `STAGE8_AXN_STAGE_RULE_CONSTRUCTION_CODEX2_V002.md` | `fd2625a079c77fbc0a102a54a0dd8ba1d97dcfb393035c2b691b0475de254444`; `f450b0a356b249509fb59b897c4f6a14e6996ba7da5ea513e69112a89907eed9` | the booked `E_joint` and its certificates; the stage payload, unital `J_NM`, receipts root |

```text
BLIND HELD: the A0 fiber enters as a DIGEST COPY only; every rank-shaped object stays closed.
BASIS INDEPENDENCE PRESERVED.  THE MATHEMATICS OF 966 IS BYTE-CARRIED; ONLY PACKAGING MOVED.
```

CLOSURE_DECLARATION_END

# STAGE 8 — AXN `for_class` FAMILIES — DARIO LANE — V004
## RELAY 969 — `[PLAN:AXN-BUILD-D68]` — FIVE PACKAGING FIXES AND THE SUITE WRAPPER

Date: 2026-08-10
Status: **ALL FIVE APPLIED. Ten tuples now parse at their declared count, the suite is instantiated at
the correct schema path, and the BI binding moved to where the principal's entries live. CLAIMED.**

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. Fix 1 — the tuple escape, and a defect I built [PROVABLE]

My V003 payloads used `|` as the field separator **and** wrote `ker(Phi|Delta_0,N)` inside a field.
The literal bar broke the parse. Re-parsed at V003:

```text
FC-03  fields = 10  (declared 8)   BREAK
FC-08  fields = 10  (declared 8)   BREAK
CERT-IF fields = 10 (declared 8)   BREAK
```

Fixed by notation rather than escaping — `ker(Phi restricted-to Delta_0,N)` — so the payloads stay
readable and contain no separator byte. **Every tuple in V004 is re-parsed before sealing:**

```text
FC-01..FC-08, CERT-IF, CERT-A : fields = 8 each, declared 8 -> ALL PARSE AT COUNT
```

One correction to the ruling, offered because a checker should be checked too: **CERT-A was never
broken.** My `JAC14-CERT` tuple carries eight fields by design — the extra one is `instantiates` — so
its count of 8 was correct, and the three genuine breaks are exactly the ones named. I say so rather
than silently "fix" a payload that was already sound.

## 2. Fix 2 — the suite wrapper, at the correct path [PROVABLE]

The families are now wrapped in a real `JointAnchorCertificateSuite.v001` instance, with the eight
members at **`finite_stage_inventory.BOUNDED_CLASS.for_class`** — the schema's own path, not an
invented one:

```json
{"schema":"rd22.axn-joint-anchor-certificate-suite.v001","carrier_sha256":"1467ab9850022931e68dc9ffa625d95099d8f6bb74d734dc9d0466f169bd00b6","a0_rank_fiber_sha256":"5eaa8277097121cbe6fcfefc7fa2d0ac2b74c48f983a033ff40102a3549afe46","finite_stage_inventory":{"BOUNDED_CLASS":{"escape_text":"or state a bounded class and explicit reopening trigger","stage_rule_ground_sha256":"42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269","bounded_class_definition":"79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f","universal_restriction_and_limit_square_receipts_root_sha256":"9451020e12f72fe5ede31a7e75692e784c559a3854981db00105657d9d6bdb41","ordered_receipt_root_sha256":"9451020e12f72fe5ede31a7e75692e784c559a3854981db00105657d9d6bdb41","outer_receipts_identity":"byte-identical to restriction_and_limit_square_receipts","explicit_reopening_trigger":"79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f","for_class":{"fc_01":"8215042bb8e60b15a310b1c8a4438015ee55039312a4ccc7f6a450a566463d3e","fc_02":"8bb6080205f6451cb6b5fc9852711ddf9f5431aaf7987fbee05ecf078548a7ad","fc_03":"06233b1d5771903af2d5a723bb9d6e1fc9170467d1d7f2b129087a999350ca38","fc_04":"b07339b7599fdc2e05f41815f77c9e6e9340a57d35396f7ad75286a835d453fb","fc_05":"65aedce4c423b427adea9dfca8099223c600b637991adb4e07e30506340dd634","fc_06":"03698d14572cc91914bc5f4f7346bdedd9fc2f61f9bdef59daeeed34382dad5b","fc_07":"5b939147f0779f787a4f4cc5250372d83610a0112561060ddbfd23a9834cf03f","fc_08":"f743aee3ce8cc616f35ad33029896bf6c65fc92f356209b01957ae34e446f0e1"}}},"restriction_and_limit_square_receipts":"9451020e12f72fe5ede31a7e75692e784c559a3854981db00105657d9d6bdb41","canonical_serialization":"canonical bytes; closed fields; no extras","cert_if_joint_sha256":"7620ef432c977283fbf467b16b2fed89e60781268a5d68a5a5e674e35b3b5bae","cert_a_joint_sha256":"e18d2f4fe733ef1afb7403417dabe85a44d0cdd7c84cdacb9b066db58e88da51","replay_entry_point_sha256":"d66e758792a62ab69df68f5390334c26b3b2e00f0c7199a91daa3b7ba09e5980"}
```

```text
SUITE_SHA256 = 9a96cfbe1b704504385fa8008021df01cf93b33b99d8f1448cff82b607b7f3fc  (2165 bytes)
```

Outer fields drawn from booked ground: `carrier_sha256` is the entered `declared_joint_algebra`
realization; `a0_rank_fiber_sha256` is the instance's `a0_rank_fiber` binding **copied as a digest,
with nothing opened**; the bounded-class content is the sealed instantiation; the receipts and root
are the booked stage material; `canonical_serialization` is the schema const.

**One outer field is deliberately absent, and I name it rather than invent it.**
`frozen_pre_output_receipt_sha256` is downstream of the final suite bytes and freezing it is a
pre-output act — the record's own gate 3 says exactly this. Filling it here would manufacture a
receipt for bytes that are still `CLAIMED`. **SUITE = INSTANTIATED with that single field
pre-output-gated.**

## 3. Fix 3 — the two edges [PROVABLE]

**FC-05's ground was over-consumed, and that is my error.** I cited the booked commutation certificate
as giving "the charge action commutes with `J_NM`". Read at its bytes, that certificate proves three
identities — `E_joint i_src = i_src E_ch`, `E_joint i_R = i_R`, `E_joint i_B = i_B` — which fix the
charge action **on the sealed embeddings**, not stage-compatibility. V004 restates the consumption to
exactly what the certificate proves and takes stage stability from **Lemma C** instead, where it
actually comes from.

**FC-07's conclusion is now sent to a procedure, not listed.** V003 stated the scoped conclusion in the
`accept` field; V004's `procedure` **receives** it and **emits** the receiver's content, so the family
does work rather than announcing a result.

## 4. Fix 4 — the BI binding, moved to where the entries live [PROVABLE]

V003 cited `BI-CONTENT@` the *instrument*, whose anchor slot is **blank** — the principal's entries
live in the decision instance. V004 binds both FC-08 and CERT-A at the instance bytes:

```text
BI-TAG      089af246cbc0d66e...:[7250,7299)#9a42dac44da482d0...   "| top level | anchor_tag_class_entry | {BI} |"
BI-CONTENT  089af246cbc0d66e...:[7300,7469)#19585bb3d660895c...   the entered BI equations row
```

Both spans were rehashed by me from the instance file.

## 5. Fix 5 — FC-07's receiver, filled as scoped [PROVABLE]

The receiver is typed `fixed_space_and_mixing_certificate_family: exact total replay object on the
bounded class`. **It demands a replay object, not a particular conclusion** — the same type reading
that dissolved the selector at 963. So the honestly-scoped content *is* lawful receiver content, and
the receiver is **FILLED**: existence plus stage compatibility at every `N` for every admitted
candidate, with the stagewise-uniqueness exclusion displayed inside the family rather than hidden.
Nothing is inflated to fill it, and no `Omega_Phi` coordinate is exposed.

## 6. The ten objects

Declared closed tuple, eight fields, no separator byte inside any value:

```text
JAC14-FC-FAMILY|v=004|id|quantifier|inputs|carrier|procedure|accept
JAC14-CERT|v=002|id|instantiates|quantifier|inputs|procedure|accept
```

### FC-01

```text
JAC14-FC-FAMILY|v=004|id=FC-01-DELTA0-WITNESS|quantifier=JOINTLY-TOTAL-over-(N>=1)x(Phi_joint-in-G_joint)@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f;STAGE@42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269|inputs=DELTA0-DEF@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13565,13639)#bb73a8ec8816bddc9c84d84e48ca81bd8d315f316092cdf295dc8fb474e2826f;EJOINT@67e4d12b4053291b2c13d709d5e66f073d0ad7a483f3ae3a97a2d2f75b4b57b8-DIRECT;STAGE@42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269|carrier=for-arbitrary-N-set-Delta_0,N-as-Delta_0^joint-intersect-A_C0,N-cut-by-the-SAME-two-pinned-conditions-restricted;-for-arbitrary-Phi_joint-the-witness-does-not-mention-Phi-so-candidate-totality-is-vacuous-and-exact|procedure=decide-membership-by-evaluating-Tr_joint(Delta)=0-and-E_joint(Delta)=Delta-carrying-no-basis-and-no-frame|accept=the-witness-decides-Delta_0,N-membership-exactly-for-every-N>=1-and-every-Phi_joint-in-G_joint
```

### FC-02

```text
JAC14-FC-FAMILY|v=004|id=FC-02-PHI-RESTRICTION-OPERATOR|quantifier=JOINTLY-TOTAL-over-(N>=1)x(Phi_joint-in-G_joint)@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f;STAGE@42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269|inputs=FC-01;DELTA0-DEF@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13565,13639)#bb73a8ec8816bddc9c84d84e48ca81bd8d315f316092cdf295dc8fb474e2826f;G-GRAMMAR@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f|carrier=LEMMA-C=predicate-9-gives-Phi-commutes-with-every-finite-cylindrical-restriction-so-Phi-maps-A_C0,N-into-itself-for-arbitrary-N;LEMMA-A=Phi-preserves-Delta_0-since-TP-gives-Tr_joint(Phi(D))=Tr_joint(D)=0-and-predicate-3-gives-E_joint(Phi(D))=Phi(E_joint(D))=Phi(D);-together-for-arbitrary-N-and-arbitrary-admitted-Phi_joint-these-give-that-Phi_joint-maps-Delta_0,N-into-Delta_0,N-so-the-restriction-OPERATOR-exists-and-is-determined|procedure=form-Phi_joint-restricted-to-Delta_0,N-as-a-content-addressed-operator-and-replay-by-evaluation-on-FC-01-witnessed-elements-carrying-no-matrix|accept=the-restriction-operator-is-exactly-determined-for-every-N>=1-and-every-Phi_joint-in-G_joint
```

### FC-03

```text
JAC14-FC-FAMILY|v=004|id=FC-03-FACTORIZATION-AND-INVERSE|quantifier=JOINTLY-TOTAL-over-(N>=1)x(Phi_joint-in-G_joint)@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f;STAGE@42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269|inputs=FC-02;G-GRAMMAR@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f|carrier=LEMMA-B=injectivity-restricts-since-Delta_0,N-subset-Delta_0-forces-ker(Phi-restricted-to-Delta_0,N)-subset-ker(Phi-restricted-to-Delta_0)-equal-zero-by-predicate-5;-hence-for-arbitrary-N-and-arbitrary-admitted-Phi_joint-the-FC-02-restriction-is-injective-and-admits-an-inverse-on-its-range-stated-as-an-operator-identity|procedure=state-factorization-and-inverse-as-OPERATOR-IDENTITIES-on-the-FC-02-restriction-and-replay-them-as-equations-carrying-no-matrix-inverse|accept=the-operator-identities-hold-for-every-N>=1-and-every-Phi_joint-in-G_joint
```

### FC-04

```text
JAC14-FC-FAMILY|v=004|id=FC-04-CPTP|quantifier=JOINTLY-TOTAL-over-(N>=1)x(Phi_joint-in-G_joint)@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f;STAGE@42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269|inputs=G-GRAMMAR@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f;STAGE@42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269|carrier=predicate-1-gives-Phi_joint-normal-and-CPTP;LEMMA-C=predicate-9-gives-Phi-commutes-with-every-finite-cylindrical-restriction-so-Phi-maps-A_C0,N-into-itself-for-arbitrary-N;-the-booked-J_NM-is-a-unital-injective-star-homomorphism-so-compressing-a-CP-map-by-it-preserves-complete-positivity-and-the-trace-compatible-pair-preserves-trace-preservation-for-arbitrary-N|procedure=replay-normality-complete-positivity-and-trace-preservation-of-the-stage-N-restriction-of-an-arbitrary-admitted-Phi_joint|accept=CPTP-holds-at-every-N>=1-for-every-Phi_joint-in-G_joint
```

### FC-05

```text
JAC14-FC-FAMILY|v=004|id=FC-05-CHARGE-COVARIANCE|quantifier=JOINTLY-TOTAL-over-(N>=1)x(Phi_joint-in-G_joint)@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f;STAGE@42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269|inputs=G-GRAMMAR@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f;COMMUTATION-CERT@b6bc91777da3a69691f1b00ac4b30cfe61a472a7c55466098701018d4735d864-DERIVATIVE-SCOPED-TO-WHAT-IT-PROVES;STAGE@42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269|carrier=predicate-2-gives-joint-charge-covariance-of-Phi_joint;-the-booked-commutation-certificate-is-consumed-ONLY-for-what-it-actually-proves-namely-E_joint-compose-i_src=i_src-compose-E_ch-and-E_joint-compose-i_R=i_R-and-E_joint-compose-i_B=i_B-fixing-the-charge-action-on-the-sealed-embeddings;-stage-compatibility-is-then-supplied-by-LEMMA-C=predicate-9-gives-Phi-commutes-with-every-finite-cylindrical-restriction-so-Phi-maps-A_C0,N-into-itself-for-arbitrary-N-and-NOT-by-that-certificate|procedure=replay-the-equivariance-square-at-stage-N-using-predicate-2-for-covariance-and-LEMMA-C-for-stage-stability|accept=joint-charge-covariance-holds-at-every-N>=1-for-every-Phi_joint-in-G_joint
```

### FC-06

```text
JAC14-FC-FAMILY|v=004|id=FC-06-SUPERSELECTION-COMMUTATION|quantifier=JOINTLY-TOTAL-over-(N>=1)x(Phi_joint-in-G_joint)@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f;STAGE@42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269|inputs=G-GRAMMAR@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f;EJOINT@67e4d12b4053291b2c13d709d5e66f073d0ad7a483f3ae3a97a2d2f75b4b57b8-DIRECT;RECEIPT-ROOT@9451020e12f72fe5ede31a7e75692e784c559a3854981db00105657d9d6bdb41|carrier=predicate-3-gives-Phi_joint-E_joint=E_joint-Phi_joint-with-the-BOOKED-E_joint-as-the-grammar-named-comparison-object;LEMMA-C=predicate-9-gives-Phi-commutes-with-every-finite-cylindrical-restriction-so-Phi-maps-A_C0,N-into-itself-for-arbitrary-N;-E_joint-preserves-the-booked-stage-algebra-so-the-identity-restricts-to-stage-N-for-arbitrary-N-and-arbitrary-admitted-Phi_joint|procedure=replay-the-commutation-identity-at-stage-N-and-propagate-by-the-seven-universal-receipts|accept=the-commutation-holds-at-every-N>=1-for-every-Phi_joint-in-G_joint-and-passes-to-the-limit-square
```

### FC-07

```text
JAC14-FC-FAMILY|v=004|id=FC-07-FIXED-SPACE-AND-MIXING|quantifier=JOINTLY-TOTAL-over-(N>=1)x(Phi_joint-in-G_joint)@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f;STAGE@42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269|inputs=G-GRAMMAR@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f;FIXED-SPACE-CERT@7019826c3febf445b22892198d6e98839579f464a4f3d4be0e903c43c0ee3a45-DERIVATIVE;STAGE@42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269|carrier=predicate-4-gives-one-normalized-mixing-invariant-Omega_Phi-at-the-FULL-level;LEMMA-C=predicate-9-gives-Phi-commutes-with-every-finite-cylindrical-restriction-so-Phi-maps-A_C0,N-into-itself-for-arbitrary-N;-so-the-restriction-of-Omega_Phi-to-A_C0,N-is-invariant-for-the-stage-N-restriction-and-the-restricted-family-is-compatible-under-the-booked-J_NM-duals;-SCOPE-STATED-stagewise-UNIQUENESS-is-NOT-claimed-since-restricting-a-mixing-channel-to-a-subalgebra-may-admit-further-invariant-states-and-the-grammar-excludes-none|procedure=RECEIVE-the-scoped-conclusion-by-replaying-invariance-of-the-restricted-state-and-its-stage-compatibility-then-EMITTING-the-fixed_space_and_mixing_certificate_family-content-as-existence-plus-stage-compatibility-with-the-uniqueness-exclusion-displayed-exposing-no-Omega_Phi-coordinate|accept=the-receiver-fixed_space_and_mixing_certificate_family-is-FILLED-with-existence-and-stage-compatibility-at-every-N>=1-for-every-Phi_joint-in-G_joint-and-with-stagewise-uniqueness-expressly-excluded
```

### FC-08

```text
JAC14-FC-FAMILY|v=004|id=FC-08-BI-ANCHOR|quantifier=JOINTLY-TOTAL-over-(N>=1)x(Phi_joint-in-G_joint)@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f;STAGE@42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269|inputs=G-GRAMMAR@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f;BI-TAG@089af246cbc0d66e6ce70971dbb14d355a78ee0f5e294706a1acaeacd0d4236d:[7250,7299)#9a42dac44da482d07f186040d6e62edb85c23c0c886858a14ba8ce63e0d3a72c;BI-CONTENT@089af246cbc0d66e6ce70971dbb14d355a78ee0f5e294706a1acaeacd0d4236d:[7300,7469)#19585bb3d660895ca65f1c52b0d97903f96257ec02ec5fd4b21b3b26a2146d38;FC-03;PAIRING@aaa3b217d945c7c788eebacdb11814eca125a8966c5cfa3de3c75d01fc1288d3|carrier=the-entered-BI-content-at-the-INSTANCE-bytes-gives-Phi_joint(I_C0)=I_C0-for-the-arbitrary-admitted-candidate;-the-booked-J_NM-is-UNITAL-so-I_C0,N-is-the-stage-unit-and-the-identity-equation-restricts-BOUND-TO-ITS-OWN-WITNESS-the-stage-unit;-input-faithfulness-restricts-by-LEMMA-B=injectivity-restricts-since-Delta_0,N-subset-Delta_0-forces-ker(Phi-restricted-to-Delta_0,N)-subset-ker(Phi-restricted-to-Delta_0)-equal-zero-by-predicate-5|procedure=replay-the-unit-equation-on-the-stage-unit-and-the-faithfulness-equation-on-the-FC-03-injectivity-for-arbitrary-N-and-arbitrary-admitted-Phi_joint|accept=the-BI-equations-hold-at-every-N>=1-for-every-Phi_joint-in-G_joint-with-the-entered-tag-class-exactly-BI
```

### CERT-IF

```text
JAC14-CERT|v=002|id=CERT-IF-JOINT|instantiates=JointAnchorCertificateSuite.v001|quantifier=JOINTLY-TOTAL-over-(N>=1)x(Phi_joint-in-G_joint)|inputs=FC-01;FC-02;FC-03;DELTA0-DEF@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13565,13639)#bb73a8ec8816bddc9c84d84e48ca81bd8d315f316092cdf295dc8fb474e2826f;G-GRAMMAR@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f|procedure=exhibit-input-faithfulness-ker(Phi_joint-restricted-to-Delta_0,N)-equal-zero-by-LEMMA-B=injectivity-restricts-since-Delta_0,N-subset-Delta_0-forces-ker(Phi-restricted-to-Delta_0,N)-subset-ker(Phi-restricted-to-Delta_0)-equal-zero-by-predicate-5-and-replay-it-on-the-FC-01-witness-at-arbitrary-N|accept=Cert_IF_joint(Phi_joint)-is-an-exact-replayable-certificate-for-every-N>=1-and-every-Phi_joint-in-G_joint
```

### CERT-A

```text
JAC14-CERT|v=002|id=CERT-A-JOINT-BI|instantiates=JointAnchorCertificateSuite.v001|quantifier=JOINTLY-TOTAL-over-(N>=1)x(Phi_joint-in-G_joint)|inputs=FC-08;BI-TAG@089af246cbc0d66e6ce70971dbb14d355a78ee0f5e294706a1acaeacd0d4236d:[7250,7299)#9a42dac44da482d07f186040d6e62edb85c23c0c886858a14ba8ce63e0d3a72c;BI-CONTENT@089af246cbc0d66e6ce70971dbb14d355a78ee0f5e294706a1acaeacd0d4236d:[7300,7469)#19585bb3d660895ca65f1c52b0d97903f96257ec02ec5fd4b21b3b26a2146d38;G-GRAMMAR@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f|procedure=exhibit-the-entered-tag-A-equal-BI-at-the-instance-bytes-and-replay-the-entered-BI-equations-on-the-stage-unit-witness-at-arbitrary-N|accept=Cert_A_joint(Phi_joint)-is-exact-and-replayable-for-every-N>=1-and-every-Phi_joint-in-G_joint-with-the-tag-class-exactly-BI
```

### 6.1 Digest ledger — with the parse count carried

| Object | Bytes | Fields | SHA-256 |
|---|---:|---:|---|
| `FC-01` | 1072 | 8 | `8215042bb8e60b15a310b1c8a4438015ee55039312a4ccc7f6a450a566463d3e` |
| `FC-02` | 1346 | 8 | `8bb6080205f6451cb6b5fc9852711ddf9f5431aaf7987fbee05ecf078548a7ad` |
| `FC-03` | 1056 | 8 | `06233b1d5771903af2d5a723bb9d6e1fc9170467d1d7f2b129087a999350ca38` |
| `FC-04` | 1109 | 8 | `b07339b7599fdc2e05f41815f77c9e6e9340a57d35396f7ad75286a835d453fb` |
| `FC-05` | 1367 | 8 | `65aedce4c423b427adea9dfca8099223c600b637991adb4e07e30506340dd634` |
| `FC-06` | 1237 | 8 | `03698d14572cc91914bc5f4f7346bdedd9fc2f61f9bdef59daeeed34382dad5b` |
| `FC-07` | 1685 | 8 | `5b939147f0779f787a4f4cc5250372d83610a0112561060ddbfd23a9834cf03f` |
| `FC-08` | 1572 | 8 | `f743aee3ce8cc616f35ad33029896bf6c65fc92f356209b01957ae34e446f0e1` |
| `CERT-IF` | 891 | 8 | `7620ef432c977283fbf467b16b2fed89e60781268a5d68a5a5e674e35b3b5bae` |
| `CERT-A` | 885 | 8 | `e18d2f4fe733ef1afb7403417dabe85a44d0cdd7c84cdacb9b066db58e88da51` |

## 7. FREEDOMS-CONSUMED

```text
JOINT_ANCHOR_INPUT = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  the 966 mathematics -- Lemmas A, B and C and the joint quantifiers -- carried unchanged;
  the grammar and Delta_0 conditions; the entered BI tag and content at the INSTANCE bytes;
  the booked carrier, fiber digest, E_joint certificates, stage payload and receipts root.

SUBSTITUTED:
  NOTHING.  No basis, matrix, coordinate, candidate selection, or invented schema path.

NOT FILLED, AND NAMED:
  frozen_pre_output_receipt_sha256, which is downstream of the final suite bytes and whose
  freezing is a pre-output act; and stagewise uniqueness in FC-07, which the grammar does not give.

SCALING WEIGHTS: NONE CONSUMED; NONE FIXED; NONE SUBSTITUTED.
```

## 8. Flattening, custody, byte audit

- **S01-S37 FLATTENING CHECK:** walked. A separator byte was not identified with a field boundary
  (§1). A blank instrument slot was not identified with the principal's entered content (§4). A
  certificate's actual conclusions were not identified with what a consumer wished it proved (§3). A
  scoped receiver fill was not identified with an inflated one (§5). A pre-output receipt was not
  manufactured for bytes still CLAIMED (§2).
- **F_PLDEC:** digests and symbolic statements only. No physical quantity evaluated.
- **BLIND:** held. The A0 fiber enters as a digest copy; nothing rank-shaped is opened; no ratio,
  no fiber comparison, no `Omega_Phi` coordinate.
- **PE-1..PE-15:** pointer-only, zero verdict weight.
- **BUILDER-NEVER-VERIFIES:** all objects **CLAIMED**. Press §2's outer-field provenance and §3's
  FC-05 restatement first.
- **CHAIN:** no anchor act, member binding, fixed-point execution, end test, gauntlet run, numerical
  evaluation, or comparison with a measured constant was invoked.

```text
CLOSURE_BEGIN_BYTE = 0
CLOSURE_END_BYTE = 2691
PREDECLARATION_OUTPUT_SCAN = 0 hits
TUPLES_REPARSED = 10/10 at declared count ; PARSE_BREAKS_REMAINING = 0
SUITE = instantiated at finite_stage_inventory.BOUNDED_CLASS.for_class ; OUTER_FIELDS_GATED = 1
MATH = byte-carried from 966 ; BASIS_INDEPENDENCE = preserved
```

Self verb audit: "fixed" applies to the five packaging items, each shown against the V003 bytes that
were wrong. "Instantiated" is used of the suite with its one pre-output-gated field named. "Filled as
scoped" is used of FC-07 on the strength of its receiver's type. Two corrections are stated as mine —
the parse break I built and the FC-05 over-consumption — and one correction runs the other way, since
CERT-A was never broken. `VERB_AUDIT_SELF = CLEAN`.

## 9. Final lines

```text
CLOSURE = declared-first (byte position 0, closure end 2691; scan 0 hits)
TUPLES = ALL-REPARSED-AT-COUNT (FC-01..FC-08, CERT-IF, CERT-A: 8 fields each, declared 8). THE BREAK WAS MINE: my V003 used | as the field separator AND wrote ker(Phi|Delta_0,N) inside a field, giving FC-03, FC-08 and CERT-IF ten fields against a declared eight. Fixed by notation -- ker(Phi restricted-to Delta_0,N) -- so no value contains a separator byte, and tuple-parse replay is now part of my seal discipline. ONE CORRECTION RUNS THE OTHER WAY: CERT-A was NEVER broken, since my JAC14-CERT tuple carries eight fields by design (the extra is instantiates); the three genuine breaks are exactly those named, and I say so rather than silently "fix" a sound payload
SUITE = INSTANTIATED (suite_sha256 9a96cfbe1b704504385fa8008021df01cf93b33b99d8f1448cff82b607b7f3fc, 2165 bytes; correct path finite_stage_inventory.BOUNDED_CLASS.for_class -- the schema's own, not invented). Outer fields from booked ground: carrier_sha256 the entered declared_joint_algebra realization; a0_rank_fiber_sha256 the instance binding COPIED AS A DIGEST with nothing opened; bounded-class content the sealed instantiation; receipts and root the booked stage material. ONE OUTER FIELD DELIBERATELY ABSENT AND NAMED RATHER THAN INVENTED: frozen_pre_output_receipt_sha256 is downstream of the final suite bytes and its freezing is a pre-output act, so filling it here would manufacture a receipt for bytes still CLAIMED
CERTS = INSTANTIATE-THE-SUITE (CERT-IF 7620ef432c977283, 891 B; CERT-A e18d2f4fe733ef1a, 885 B; each carries instantiates=JointAnchorCertificateSuite.v001 and the joint quantifier)
EDGES = FC-05+FC-07 CORRECTED. FC-05: my V003 cited the booked commutation certificate as giving "the charge action commutes with J_NM" -- read at its bytes it proves E_joint i_src = i_src E_ch, E_joint i_R = i_R and E_joint i_B = i_B, fixing the charge action ON THE SEALED EMBEDDINGS, not stage compatibility. THAT OVER-CONSUMPTION WAS MINE; V004 restates it to exactly what the certificate proves and takes stage stability from LEMMA C, where it actually comes from. FC-07: the scoped conclusion is now SENT to a procedure that receives and emits the receiver's content, rather than listed in accept
BI = BOUND-AT-INSTANCE-BYTES (tag [7250,7299)#9a42dac44da482d0..., content [7300,7469)#19585bb3d660895c..., both rehashed by me from JOINT_ANCHOR_DECISION_INSTANCE_V003.md). My V003 cited the INSTRUMENT, whose anchor slot is BLANK -- the principal's entries live in the instance, and that is where FC-08 and CERT-A now bind
FC07_RECEIVER = FILLED-AS-SCOPED. The receiver is typed "exact total replay object on the bounded class" -- it demands a replay object, not a particular conclusion, the same type reading that dissolved the selector at 963. So the honestly-scoped content IS lawful receiver content: existence plus stage compatibility at every N for every admitted candidate, with the stagewise-uniqueness exclusion displayed INSIDE the family rather than hidden. Nothing inflated to fill it
MATH = BYTE-CARRIED-VERIFIED (Lemmas A, B and C and the joint quantifiers carried unchanged from 966; only packaging moved)
BASIS_INDEPENDENCE = PRESERVED (no basis, order, matrix, matrix inverse, or Omega_Phi coordinate anywhere)
BLIND = HELD (the A0 fiber enters as a digest copy only; nothing rank-shaped opened)
NUMERAL_GREP = RUN (ten field counts, ten byte lengths, ten digests, the suite byte count and suite_sha256 -- each re-derived from command output rather than carried)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
