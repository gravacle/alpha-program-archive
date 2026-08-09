# Stage 8 / 7A Step 11 — V008-05 competitor normal forms and fixture assignments

**Lane:** CODEX 2  
**Relay:** 748  
**Row:** `C-B-V008-05`  
**Disposition class:** derive-or-gap; admission barred

## 1. Preflight and custody

| Object | SHA-256 | Result |
|---|---|---|
| `relay_inbox/RELAY_PASTE_748_V008_05_COMPETITOR_CODEX2_V001.md` | `abd2d653e7848515e8149868fc4354c3af4b73cbbdf4e7bb24c2f37a09325c8a` | seal sidecar verified before reading |
| pickup acknowledgement | `748 \| CODEX 2 \| abd2d653e7848515e8149868fc4354c3af4b73cbbdf4e7bb24c2f37a09325c8a` | written before task work |

The requested report, report seal, `748_DONE.md`, and package directory were absent in the cleanroom and archive workspace at preflight. The report names were checked again immediately before this write. All relay writes are confined to the cleanroom. No register, plan, tracker, git, evaluator-chain, member-binding, fixed-point, end-test, physical-quantity evaluation, or measured-constant comparison action occurred.

## 2. Pinned inputs and derive-or-gap probe

### 2.1 File pins

| Role | Sealed input | SHA-256 |
|---|---|---|
| governing closed box schema | `STAGE8_7A_BOX_SCHEMA_DELTA_CODEX2_V001.json` | `b52e66b79787a55bad1553c05dfa8df52e7b11153879589d9627073a8e06bba9` |
| evaluator descriptor law | `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V012.md` | `382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504` |
| target table | `step11_tooling_family1/targets.generated.json` | `477d038935d69ada049e570a693a3218e4c7bf2706330f8ae3888fe0cc56cdf6` |
| authoring plan | `step11_instance_batch1/authoring_plan.json` | `e460e4557760dd2452186be54d62132a0b96a665e273e2a754753da01a212b0f` |
| CS partial | `step11_instance_batch1/generated/instances/CS_C-B-V008-05_universal-word-representation.partial.json` | `310a913f18367f0ad2c2a78620fc33ec290c0876652f94b9f2753ae41fd96fdd` |
| MG partial | `step11_instance_batch1/generated/instances/MG_C-B-V008-05_inverse-opposite-holonomy-competitor.partial.json` | `6387f8962206a48d00029413d271f2778921697da758306f700ffcc0480384ca` |
| noncommuting-plaquette source | `review_packets/STAGE7_QSPEC_CANDIDATE_V001/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` | `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` |
| packet manifest | `review_packets/STAGE7_QSPEC_CANDIDATE_V001/STAGE7_PACKET_MANIFEST_V001.sha256` | `9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311` |

The packet manifest was checked for the exact V011 member digest. Both partial instances agree that `representation`, `universal_word`, and `target_word` are the known side and that `inverse_competitor` plus `fixture_assignments` are the missing side. The extracted BX01 schema is closed and requires exactly those five element references plus `schema` and `source_bindings`; it contains no target-ID field. Consequently, the two partial target requests lawfully converge to one completed box instance and remain distinguished by two content-addressed target bindings.

### 2.2 Exact meaning-probe spans

All spans below are half-open byte spans in sealed V011. Each span digest was independently recomputed from the source bytes.

| Source block | Span | Bytes | Span SHA-256 | Use |
|---|---:|---:|---|---|
| translation fixture law | `[29318,29791)` | 473 | `482b6f48e629a55a674ba87d1a6d04d45e4db10eac6deee4c198b042e0f9a14f` | periodic `K_L=(Z/LZ)^4`, `L>=3`, arbitrary unitary link transports |
| global shift law | `[29792,29955)` | 163 | `b1e130de8e773fbe0ad57d7ef17be090296e0d11e59aae1b53966c62c3d3a50c` | exact action of each `T_mu` |
| plaquette paths | `[30722,30847)` | 125 | `77f8ebb9caf593ce9d22845d5aed804aec10d0ab69ff5afbc692dc124e5b06f2` | `U_+` and `U_-` orderings |
| commutator | `[30849,31093)` | 244 | `55aa1c248bae7a5578dd727c192b98ad1f234792d5f7dbc1b6af3e4b789cf13e` | ordered-shift comparison |
| holonomy | `[31095,31273)` | 178 | `9f5f30e362aed5bbbf49f3bf2d2a9f8151818f23f5116ae7539b4591fd33174b` | `W=U_-^{-1}U_+` |
| representation law | `[32193,32334)` | 141 | `275a3063c8246e63e185f6d3e38ddcc095227a17ac5cf2bcf5d3422d198edc42` | generator-to-shift homomorphism |
| universal word | `[32937,33055)` | 118 | `7e8893decefd7ecfbcab4ae93e187e18e79bb5df734ab3740cfefce6eec157f8` | current four-token word |
| block target | `[33813,33927)` | 114 | `86d576ab87a60610c431bce11c894b0effef7c5bfabea30c503380b3a74c87a5` | represented word equals block holonomy operator |
| opposite normal form | `[33929,34250)` | 321 | `226fcecf93a4a754be60eabc9074124b9c1244b16b77e33d4865356f1cdaa20e` | opposite commutator represents the adjoint/inverse holonomy |

The search covered the exact symbols, word-order variants, inverse/adjoint vocabulary, hyphenated and line-wrapped forms, and the semantic notions “opposite ordering,” “noncommuting plaquette,” and “magnetic translation.” The last span directly determines the competitor word and its general represented normal form; it is not inferred from the old absence label.

## 3. Competitor normal form

The sealed current word and opposite word are:

| Role | Token sequence | Represented normal form |
|---|---|---|
| current | `T_nu T_mu T_nu^-1 T_mu^-1` | `M_W,(mu nu)` |
| competitor | `T_mu T_nu T_mu^-1 T_nu^-1` | `M_W,(mu nu)^dagger = M_W,(mu nu)^(-1)` |

This is a genuine reversed-order competitor, not a second spelling of the current word. The canonical competitor element is 546 bytes, SHA-256 `11edc8cf18be138823885639b56d816593029c0ac01eab017714412e546e9c01`.

## 4. Exact noncommuting witness

### 4.1 Declared construction convention and bounded underdetermination

V011 permits every periodic `K_L` with `L>=3` and arbitrary unitary link transports. It does **not** select a unique connection, a unique physical background, a preferred `L`, or a preferred fixture. This construction therefore uses the transparent deterministic test convention “smallest permitted `L`” and supplies one exact witness inside the sealed family. It claims neither uniqueness nor physical selection.

Set `L=3`, take one-dimensional complex fibers, choose distinct directions `mu=0`, `nu=1`, and let `omega` obey

`omega^2 + omega + 1 = 0`, `omega^3=1`, `omega!=1`, and `omega^dagger=omega^2`.

On `K_3=(Z/3Z)^4`, set

- `U_mu(x)=1`;
- `U_nu(x)=omega^(x_mu)`; and
- `U_rho(x)=1` for the other directions.

The assignment is periodic because `x_mu` is taken modulo 3, and it is unitary by the displayed exact root relation. The fixture element is 2,459 bytes, SHA-256 `f42893a6a060ca5dbb21559497f7eb0bc0408a7208fa4a5ebceac43b03e92e08`.

### 4.2 Block computation

The sealed path ordering gives

`U_+(x)=U_nu(x+mu)U_mu(x)=omega^(x_mu+1)`

and

`U_-(x)=U_mu(x+nu)U_nu(x)=omega^(x_mu)`.

Hence every block has `W(x)=U_-(x)^(-1)U_+(x)=omega`, while the opposite word has `W(x)^(-1)=omega^2`.

| `x_mu mod 3` | `U_+` exponent | `U_-` exponent | `W` exponent | inverse exponent |
|---:|---:|---:|---:|---:|
| 0 | 1 | 0 | 1 | 2 |
| 1 | 2 | 1 | 1 | 2 |
| 2 | 0 | 2 | 1 | 2 |

There are `3^4=81` blocks. The exact global normal forms are therefore `omega I_81` and `omega^2 I_81`; they are unequal because `omega!=1` and `omega^2!=omega`, and their product is the identity.

### 4.3 Noncommutation computation

From the sealed shift law and this assignment,

`(T_mu T_nu psi)_x = omega^(-(x_mu+1)) psi_(x+mu+nu)`,

whereas

`(T_nu T_mu psi)_x = omega^(-x_mu) psi_(x+mu+nu)`.

The factors differ by `omega^-1`, so the shifts do not commute. The compiler represented both shifts as exact monomial operators on all 81 coordinates, with coefficients stored only as exponents in `Z/3Z`; it used no floating-point approximation. Exhaustive evaluation returned current-word exponent 1 and opposite-word exponent 2 at every coordinate. The content-addressed proof is 743 bytes, SHA-256 `74f0e1fa5eb35668fa2a40522c66691817a199b77d23bcf1192a9487aaa94479`.

## 5. Content-addressed elements and complete instance

| BX01 field | Bytes | SHA-256 | Disposition |
|---|---:|---|---|
| `universal_word` | 449 | `0ba3aac69cf5ebea4bd27d774deae0c9c91039afd9849230c04733235e57d53d` | known side retained and structured |
| `representation` | 1,146 | `862f477177b92c4e8dd1a97488a8fdb431ca3d53642d65a544f2017c7c96eea9` | known side retained and structured |
| `target_word` | 1,118 | `d7653f3ae9d7fe917436eac92b4d212260d24b02dbb9b0ce622100b384733105` | known side retained and structured |
| `inverse_competitor` | 546 | `11edc8cf18be138823885639b56d816593029c0ac01eab017714412e546e9c01` | built from sealed opposite-normal-form span |
| `fixture_assignments` | 2,459 | `f42893a6a060ca5dbb21559497f7eb0bc0408a7208fa4a5ebceac43b03e92e08` | exact witness built; uniqueness not claimed |

The complete closed BX01 instance is 4,051 bytes, SHA-256 `0a400a1d19c436edd1a407c95390916a908f57281176ec22491eb139fb107775`. It carries all nine exact source-and-span bindings and five content references. Each content-addressed filename prefix, recorded byte length, and digest was independently reverified.

Target bindings:

| Target | Prior partial SHA-256 | Binding SHA-256 | Complete instance |
|---|---|---|---|
| `CS:C-B-V008-05:universal-word-representation` | `310a913f18367f0ad2c2a78620fc33ec290c0876652f94b9f2753ae41fd96fdd` | `ee37112edc0ff19835847822fb26a372fbd53081f0c96cf35b26c549ea8e11f1` | common instance above |
| `MG:C-B-V008-05:inverse-opposite-holonomy-competitor` | `6387f8962206a48d00029413d271f2778921697da758306f700ffcc0480384ca` | `d5441e2a63bcab23d003d7873cd7f4d5b4cc09eb0c1f851029872a0fa789f7e6` | common instance above |

Element manifest SHA-256: `4e5f8c9142d9fe710af1e9c6ee9cb6f58a7e31e699c18603418e6381f7f082de`.

## 6. Compilation and honest statuses

Both target paths were actually invoked under `python -I -S -B`. Before evaluating the words, the compiler now binds its exact monomial construction to the serialized domain, directions, and link-assignment fields; a changed fixture cannot inherit the hard-coded witness result.

| Target | Observation SHA-256 | Component outcome |
|---|---|---|
| CS universal-word representation | `e1c9ba30ba0b12598930ae511613b066b17e8ba76c6673fe92625ef13efc7d23` | `PASS_UNIVERSAL_WORD_REPRESENTS_TARGET_HOLONOMY` |
| MG inverse/opposite competitor | `67aee0ff506a0a25c629a57a6e7c1afab8b36dcc9caf682a92040917ddf37318` | `PASS_INVERSE_OPPOSITE_COMPETITOR_REJECTED` |

Combined compile-result SHA-256: `35004b51858846bee4e702addbb6e79827d076e64e929f404a0a531011b2262e`.  
Row-status SHA-256: `ba651f514d0dfba79956e7d3048edeec0fb501273a64a7f2cbe25a13ce518376`.

These are Step-11 component outcomes, not evaluator verdicts. The two former partial target requests are now stateable with their required components present and admission barred. Their common row record is `STATEABLE_BOTH_TARGETS_COMPILED_ADMISSION_BARRED`. No board, seal-gating verdict, or evaluator admission changed.

## 7. Battery, self-check, and pin check

- Canonical form: every JSON file is tight sorted UTF-8 with no trailing newline; NaN is rejected.
- Schema: the BX01 schema was extracted from the sealed schema delta rather than transcribed; the object and content-reference surfaces are closed.
- Source integrity: 8 file pins, the packet-manifest membership, and 9 exact source spans verified.
- Content addressing: every element, binding, instance, and proof filename prefix equals its byte digest; all recorded lengths and hashes reverified.
- Exact execution: both positive target paths executed; all 81 monomial-operator coordinates agreed with the three-row block calculation.
- Mutation controls: 5/5 bit under the actual compiler — swapped current word (`UNIVERSAL_WORD_NORMAL_FORM`), commuting link assignment (`FIXTURE_ASSIGNMENTS`), wrong competitor normal form (`COMPETITOR_FIXTURE_NORMAL_FORM`), content-digest mutation (`CONTENT_DIGEST`), and missing source binding (`SOURCE_BINDINGS`).
- Rebuild control: a second isolated build refused occupied output at the package boundary.
- Inventory: `step11_v008_05_competitor/inventory.generated.json` has SHA-256 `2c1a6173be17ddcfca922e99b6ad01d96f28ec2901bc4c231765096750469a60`; its 20 recorded members all rehashed. The inventory file itself is outside its member root.
- Static self-check: SHA-256 `2e4f740eef038cff1a0533747e1728e0e53bc7425faf25eecc598f88e1677f2d`; Python AST parse passed for both scripts.
- M-2: exact, normalized, hyphenation/line-wrap, and semantic-equivalent searches were applied to the sealed noncommuting-plaquette material.
- F_PLDEC: only finite symbolic group/exponent arithmetic and structural censuses were used; no physical quantity was numerically evaluated and no measured constant was compared.
- Anti-tuning: the current and opposite words come from sealed orderings. The witness convention was declared before compilation, both word values were computed exhaustively, and the opposite control was required to differ rather than selected from a desired board result.
- PIN CHECK: all input pins, span pins, generated content references, compiler outputs, and inventory rows reverified immediately before sealing.
- Verb audit: “built,” “PASS,” and “compiled” are confined to the five box elements and two bounded component compiles. The report does not claim an evaluator PASS, authorization, admission, unique physical connection, or preferred fixture.

ELEMENTS = 5/5 built (3 known-side elements retained; competitor normal form + noncommuting fixture built; unique physical connection/preferred fixture underdetermined and not claimed)
COMPILE = CS PASS_UNIVERSAL_WORD_REPRESENTS_TARGET_HOLONOMY; MG PASS_INVERSE_OPPOSITE_COMPETITOR_REJECTED
ROWS = CS STATEABLE_COMPONENT_PRESENT_ADMISSION_BARRED; MG STATEABLE_COMPONENT_PRESENT_ADMISSION_BARRED; common row STATEABLE_BOTH_TARGETS_COMPILED_ADMISSION_BARRED
ADMISSION = barred, stated
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
