CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
PREDECLARATION_REGION = EMPTY (closure opens at byte 0; no text precedes it)
PREDECLARATION_OUTPUT_SCAN = 0 hits in authored prose (27-token sweep)
VERDICT_BEARING_SET = exactly the 9 content-addressed members below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
LANE = CODEX 2   ROLE_THIS_RELAY = OPPOSITE-LANE CHECKER
SUBJECT_STATUS = CLAIMED until this check
```

| # | Closed member | SHA-256 / bounded-span SHA-256 | Role |
|---:|---|---|---|
| 01 | `relay_inbox/RELAY_PASTE_967_FAMILIES_V003_CROSSCHECK_CODEX2_V001.md` | `c1a93942b56b1e1c04dfb965c13d0cd9686f489d301590f351800420571fd2ad` | assignment |
| 02 | `PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | state pin |
| 03 | `STAGE8_AXN_FOR_CLASS_FAMILIES_DARIO_V003.md` | `25845e9223e62374df699b474f0770191ef731f8123f2299b21af9683bf1b581` | subject |
| 04 | `STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V003.md` | `79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e`; `G_joint` `[13731,14294)` `105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f`; `Delta_0^joint` `[13565,13639)` `bb73a8ec8816bddc9c84d84e48ca81bd8d315f316092cdf295dc8fb474e2826f` | closed suite, grammar, and tangent-space definition |
| 05 | `STAGE8_AXN_FAMILIES_V002_CROSSCHECK_CODEX2_V001.md` | `43108d1479d4d121a9546051e07c413fa414cac1dac04c1752d4b5c57f2d3a7c` | four defects to recheck |
| 06 | `STAGE8_AXN_ENTERED_OBJECTS_BUILD_CODEX2_V002.md` | `fd2625a079c77fbc0a102a54a0dd8ba1d97dcfb393035c2b691b0475de254444` | booked `E_joint`, commutation, and fixed-space objects |
| 07 | `STAGE8_AXN_STAGE_RULE_CONSTRUCTION_CODEX2_V002.md` | `f450b0a356b249509fb59b897c4f6a14e6996ba7da5ea513e69112a89907eed9`; stage payload `42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269`; RL-06 `[14820,15345)` `37244a9ee40ae7dad0bdd66e94b6f088773f9ca26c594aa9791316d2379d10af` | stage rule and exact unit-preservation ground |
| 08 | `QUESTIONS_SETTLED_REGISTER_V001.md#Q-877` | `[1777417,1779839)` `24013c8f9648a7d3169d0ddd4eba88af280c28b91872023c3e5cd3d77a341f50` | exact adjudication span; live-append tolerance used for the enclosing file |
| 09 | `JOINT_ANCHOR_DECISION_INSTANCE_V003.md` | `089af246cbc0d66e6ce70971dbb14d355a78ee0f5e294706a1acaeacd0d4236d`; `{BI}` row `[7250,7299)` `9a42dac44da482d07f186040d6e62edb85c23c0c886858a14ba8ce63e0d3a72c`; BI-content row `[7300,7469)` `19585bb3d660895ca65f1c52b0d97903f96257ec02ec5fd4b21b3b26a2146d38` | location of the actual entered BI value; used to test the subject's claimed input binding |

All eight ordinary whole-file members and their adjacent seals verified before use. Q-877 was
rehash-verified at its exact half-open span under live-append tolerance. No physical quantity was
evaluated.

CLOSURE_DECLARATION_END

# STAGE 8 — AXN `for_class` FAMILIES V003 — OPPOSITE-LANE CROSS-CHECK
## CODEX 2 — RELAY 967 — `[PLAN:AXN-BUILD-C66]`

Date: 2026-08-10  
Status: **FAILURES NAMED. Lemmas A/B/C re-derive cleanly, but the ten-object book does not instantiate
the closed suite: three lines are not closed tuples, both certificate lines miss the suite schema,
FC-08 does not bind the entered BI bytes, and two advertised derivative `E_joint` edges are not
received by their procedures. RUN 4 does not go on these V003 family bytes.**

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_binding = false
fixed_point_execution = false
end_test = false
JOINT_ANCHOR_DERIVED = false
```

## 1. The lemmas, independently re-derived

| Lemma | Independent derivation from the sealed grammar | Press result |
|---|---|---|
| A — preservation of `Delta_0^joint` | For arbitrary admitted `Phi_joint`, predicate 1 is trace preserving, so `Tr_joint(Phi_joint(Delta))=Tr_joint(Delta)=0`. Predicate 3 gives `E_joint(Phi_joint(Delta))=Phi_joint(E_joint(Delta))=Phi_joint(Delta)`. Both defining equations survive. | **CLEAN.** This uses only predicates 1 and 3 and the two pinned defining equations. No candidate-specific or stage hypothesis is inserted. |
| B — kernel restriction | For every defined stage subspace `Delta_0,N subset Delta_0^joint`, `ker(Phi_joint restricted to Delta_0,N)` is a subset of `ker(Phi_joint restricted to Delta_0^joint)={0}` by predicate 5. | **CLEAN.** It proves injectivity on each restriction, and no more. In particular it does not independently provide a two-sided inverse outside the restriction's range. |
| C — stagewise action | Predicate 9 requires every finite/cylindrical restriction and limit square to commute. For arbitrary `N`, its stage square therefore receives the admitted `Phi_joint` and gives an endomorphism on the stage carrier. | **CLEAN.** This is exactly the stagewise-action content of predicate 9, not an added invariance assumption. |

The quantifier strings on all eight family rows now do bind both axes, `(N>=1) x (Phi_joint in
G_joint)`, and each row has a `carrier=` field. Thus the mathematical universal-carrier repair is
real at the bytes. It does not cure malformed serialization or an input that points at the wrong
sealed object.

## 2. Closed-tuple replay — a new byte defect

The subject declares exactly this pipe-delimited shape:

```text
JAC14-FC-FAMILY|v=003|id|quantifier|inputs|carrier|procedure|accept
```

A lawful line therefore has eight pipe-separated fields. The literal operator notation
`ker(Phi|Delta_0,N)` is not escaped. It introduces two additional delimiters in three objects.
Terminal linefeeds were excluded, as in the earlier replay.

| Object | Subject byte span | Bytes | SHA-256 | Parsed fields | Closed-tuple verdict |
|---|---:|---:|---|---:|---|
| FC-01 | `[5565,6679)` | 1114 | `65071665e0faf2916db1fb732b91334fdc62cd6276036eb3e6d807b00b26f483` | 8 | PASS |
| FC-02 | `[6704,8050)` | 1346 | `364e17ac6f24836788e8e33f1bd51707046f6a9cbef3cbcc03dc5a327fce9eea` | 8 | PASS |
| FC-03 | `[8075,9099)` | 1024 | `bac6c430bce02df7bdbacc3c6512c33b1f8f7d9ad335a6e99f581b02ef4b1f06` | **10** | **FAIL — two unescaped `|` bytes** |
| FC-04 | `[9124,10233)` | 1109 | `738da1c45b067b82577e58248a8428c3d9465adfeb6edde0f48f8b1c827e071f` | 8 | PASS |
| FC-05 | `[10258,11324)` | 1066 | `e9dc87dad92dd252a135b652821500afd7e0780b6e0b4a51eccf4d79c83b3523` | 8 | PASS |
| FC-06 | `[11349,12586)` | 1237 | `627aeb34adaac865b4255bd45cd39a5b18fe95a8241ed33057de1abf58133faa` | 8 | PASS |
| FC-07 | `[12611,14191)` | 1580 | `e4e8400b5dd2e91ca0f4c9f75832c18b639e1389bf6ed0781afd006552d8ef2d` | 8 | PASS |
| FC-08 | `[14216,15696)` | 1480 | `9f8663984f8228ee8e1ead1b070be4669534d8eb4c77807d89079c13b662e4c8` | **10** | **FAIL — two unescaped `|` bytes** |
| CERT-IF | `[17165,18024)` | 859 | `edec6f7aca6f24d67e80ff7b8e853972e0ba481754cd21a90bb94e6c58e582bb` | **10** | **FAIL — two unescaped `|` bytes** |
| CERT-A | `[18050,18727)` | 677 | `f48714ac856c3daa4fbed3fea33d8d571c5c0ddd241aec11e65b8ca439f16e1e` | 8 | PASS |

The list line at `[19809,20630)` is 821 bytes and rehashes exactly to
`2c5e3dfed520adf87ad00efb5f0176c21d5efdda0b7bab7f7492e38a663a219d`.
That confirms byte custody; it does not make the three malformed members valid instances of the
declared tuple.

## 3. The two certificate objects do not instantiate the closed suite

The normative schema begins `JointAnchorCertificateSuite.v001 := {` at instrument byte 21684. Its
`for_class` object is nested under
`finite_stage_inventory.BOUNDED_CLASS.for_class` at byte 23079; there is no schema receiver named
`JointAnchorCertificateSuite.v001.for_class`.

Both certificate lines nevertheless declare
`instantiates=JointAnchorCertificateSuite.v001.for_class`. Neither line supplies the suite's outer
closed fields: `schema`, carrier and fiber digests, the selected bounded-class wrapper and its
ground/class/receipts/root/identity/reopening fields, outer receipts, canonical serialization,
replay entry, suite digest, and pre-output receipt. CERT-IF is additionally malformed as a tuple.
The eight family lines may be candidate values for the nested `for_class` keys, but two separate
`JAC14-CERT` lines are not a `JointAnchorCertificateSuite.v001` instance.

```text
CERT_IF = exact kernel-restriction theorem is stated, but closed-suite instantiation fails
CERT_A  = BI theorem is stated, but closed-suite instantiation and entered-content binding fail
```

## 4. `E_joint` scope map — edgewise audit

| Family | Claimed edge | Byte audit |
|---|---|---|
| FC-01 | DIRECT | **CONFIRMED.** Its pinned `Delta_0^joint` input contains `E_joint(Delta)=Delta`. |
| FC-06 | DIRECT | **CONFIRMED.** Predicate 3 and the booked `E_joint` comparison object are direct inputs. |
| FC-02, FC-03, FC-08 | TRANSITIVE | **CONFIRMED as dependency reachability** through the `Delta_0^joint` witness and Lemmas A/B. |
| FC-04 | NONE | **CONFIRMED.** Its CPTP restriction argument has no `E_joint` receiver. |
| FC-05 | DERIVATIVE | **FAIL — wrong derivative ground.** The cited `b6bc9177...` object proves only `E_joint compose i_src=i_src compose E_ch`, `E_joint compose i_R=i_R`, and `E_joint compose i_B=i_B`. It does not state that the charge action commutes with `J_NM`, which is the exact proposition the FC-05 carrier attributes to it. The stage rule plus a separately bound factorwise charge-action proof could establish that proposition; this input does not. |
| FC-07 | DERIVATIVE | **FAIL — unreceived derivative.** The cited `7019826c...` object proves `Fix(E_joint)=Fix(E_ch) graded-tensor-min R_inf graded-tensor-min B`. FC-07's carrier derives stage invariant-state existence solely from predicate 4 and Lemma C and never sends the fixed-space conclusion to an operation. Merely listing the certificate in `inputs` does not bind the edge. |

The displayed category census is textually honest about where inputs were placed, but two derivative
edges fail receiving-procedure replay.

## 5. FC-08 — unit ground succeeds; entered BI binding does not

The stage-unit portion is correct and was independently rehashed. The stage payload hashes to
`42b6850c...`, and RL-06 at `[14820,15345)` hashes to `37244a9e...` and concludes
`J_NM(I_C0,N)=I_C0,M`. The identity equation therefore has its own stage-unit witness. The
input-faithfulness equation restricts by clean Lemma B rather than being sent to the unit witness.

The remaining input is not pinned to the entered content. FC-08 says
`BI-CONTENT@79f0c351...` with the whole V003 instrument digest and no span. That instrument contains
the BI **template**, while its `ANCHOR_TAG_CLASS_ENTRY` is still a blank principal-entry slot. The
actual entered `{BI}` and BI-content bytes occur in `JOINT_ANCHOR_DECISION_INSTANCE_V003.md` at
`[7250,7299)` and `[7300,7469)` respectively, but neither span nor that file digest occurs in FC-08
or CERT-A. A whole-file pointer to a blank template is not the entered value. FC-08 also fails its
declared tuple shape as shown in §2.

Thus the wrong-receiver defect is repaired, while the earlier operand/content-addressing defect is
not.

## 6. FC-07 scope

Declining stagewise uniqueness is mathematically correct: predicate 4 supplies full-level mixing,
and restriction to an invariant stage need not preserve uniqueness. The stated existence and
compatibility theorem is therefore not an over-claim.

It remains **under the declared receiver**. Instrument bytes `[23630,23728)` name
`fixed_space_and_mixing_certificate_family: exact total replay object on the bounded class`.
FC-07 expressly omits stagewise uniqueness/mixing and its procedure replays only invariance and
compatibility. If the receiver is meant to require only that weaker theorem, the schema must say so;
the payload cannot silently weaken a named fixed-space-and-mixing certificate to fit what follows
from the grammar.

```text
FC07_THEOREM_SCOPE = CORRECT RESTRAINT
FC07_RECEIVER_COVERAGE = UNDER
```

## 7. Joint-totality and basis-independence verdicts

At the theorem level, Lemmas A/B/C genuinely quantify over arbitrary `N` and arbitrary admitted
candidate. At the object level, joint totality is not 8/8 because FC-03 and FC-08 are not instances
of their declared carrier format, FC-08 lacks the entered BI object, and FC-07 underfills its named
receiver. No family may acquire a PASS merely because its unparsed bytes hash correctly.

The dissolved basis selector does not reappear. None of the ten payloads introduces a basis,
ordering, coordinate list, restriction matrix, matrix inverse, or `Omega_Phi` coordinate. The
three lemmas are basis-free subspace/operator arguments. `BASIS_INDEPENDENCE = 10/10` is therefore
confirmed independently of the receiver failures.

## 8. FREEDOMS-CONSUMED, flattening, and fences

```text
JOINT_ANCHOR_INPUT = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false
SCALING_WEIGHTS = NONE CONSUMED; NONE FIXED; NONE SUBSTITUTED
```

- **FLATTENING CHECK:** held. Byte custody was not flattened into schema validity; a listed input was
  not flattened into a consumed input; a template was not flattened into an entered value; and
  full-level uniqueness was not flattened into stagewise uniqueness.
- **BLIND:** held. No fiber, rank, ratio, fiber comparison, or `Omega_Phi` coordinate was exposed.
- **PE-1..PE-15:** pointer-only and assigned zero verdict weight.
- **F_PLDEC:** only symbolic predicates, byte spans, tuple arities, and cryptographic digests were
  checked. No physical quantity was numerically evaluated and no measured constant was compared.
- No anchor member was bound, no fixed point or end test executed, and no gauntlet chain was invoked.
- **PIN CHECK:** the output name and sidecar were absent before write; every ordinary closed member
  matched its adjacent seal, and the live register claim matched the declared Q-877 span digest.

## 9. Verdict and required bounded repairs

V003 needs a successor before an eight-family book can be claimed:

1. escape or replace the literal `|` in the three affected payloads and regenerate their hashes and
   the ordered root;
2. construct the closed `JointAnchorCertificateSuite.v001` wrapper (or accurately name the nested
   field receiver) rather than declaring the nonexistent `.for_class` schema path;
3. bind FC-08/CERT-A to the exact entered `{BI}` and BI-content bytes;
4. replace FC-05's wrong commutation ground with a content-addressed proof that the charge action is
   compatible with `J_NM`, and either consume FC-07's fixed-space object or remove the derivative
   claim;
5. align FC-07's receiver with the theorem actually proved, without inventing stagewise uniqueness.

Self verb audit: “clean” is confined to the three displayed derivations. “Confirmed” is confined to
rehash, direct/transitive/none edges, unit ground, and basis-independence. No malformed tuple,
uninstantiated suite, unbound BI value, or underfilled receiver is called booked.

## 10. Final lines

```text
CLOSURE = declared-first (byte position 0, scan 0 hits)
LEMMAS = A/B/C RE-DERIVED-CLEAN
JOINT_TOTALITY = FAIL (FC-03 malformed; FC-07 under receiver; FC-08 malformed + entered BI unbound)
CERTS = FAIL (nonexistent `.for_class` schema path; no closed suite wrapper; CERT-IF malformed; CERT-A BI input unbound)
SCOPE_MAP = FAIL (FC-05 wrong derivative ground; FC-07 derivative input unreceived; other six edges confirmed)
FC08 = FAILS (unit ground rehashed and Lemma B clean; entered BI bytes unbound; tuple malformed)
FC07_SCOPE = UNDER (correctly declines stagewise uniqueness, but underfills `fixed_space_and_mixing_certificate_family`)
PAYLOADS = BYTE-DIGESTS 10/10 + ROOT; CLOSED-TUPLE REPLAY FAILS FC-03/FC-08/CERT-IF
BASIS_INDEPENDENCE = 10/10
VERDICT = FAILURES NAMED; NOT EIGHT-BOOK; RUN 4 DOES NOT GO ON V003 FAMILY BYTES
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
```
