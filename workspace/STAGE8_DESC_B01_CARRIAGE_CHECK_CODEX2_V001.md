CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
PREDECLARATION_REGION = EMPTY (closure begins at byte 0)
PREDECLARATION_OUTPUT_SCAN = 0 hits (no bytes precede this declaration)
VERDICT_BEARING_SET = exactly the 7 content-addressed full-path byte objects below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
LANE = CODEX 2
ROLE = OPPOSITE-LANE B01 CARRIAGE MANIFEST CHECK
DIGEST_RULE = each digest below was recomputed from the named bytes before sealing
CLOSURE_END_BYTE = 02589
```

| # | Closed full-path byte object | SHA-256 | Role |
|---:|---|---|---|
| 01 | `/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/relay_inbox/RELAY_PASTE_1017_CARRIAGE_MANIFEST_CHECK_CODEX2_V001.md` | `f7f40dbb20e06178ee8d50fdb0a7d13c49bf75babcc304fd15ba792d21173108` | assignment |
| 02 | `/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/STAGE8_DESC_B01_CARRIAGE_MANIFEST_DARIO_V001.md` | `eb481a2e8a443024ba0bffdff7803441f6de75b6bee4a051b73e13d7da7ea684` | manifest artifact under check |
| 03 | `/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/b01_carriage_manifest_v001.json` | `346a1095672abf1678525802559d912ba9859d068e0707564e9291a7d1d4edc4` | machine-readable span manifest |
| 04 | `/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/build_b01_carriage_remainder_v001.py` | `c1f84957a209ca1781d5d8a2d9bbfca07fd6eea9630d65e58957feb909a7b2ee` | regenerator and refusal path |
| 05 | `/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/STAGE8_DESC_B01_V003_CONFIRM_CODEX2_V001.md` | `8ae0a95c02e645c71f87f32730685664090fa770304561ce9277397c83ae0aa4` | prior finding and diagnostic |
| 06 | `/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/STAGE8_DESC_B01_DARIO_V002.md` | `19bf16f7ec1dda3e4c039e57b99a2896db4e9074ff1904e0e52096e2e90cf01b` | old sealed bytes |
| 07 | `/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/STAGE8_DESC_B01_DARIO_V003.md` | `41ea9708aa51bdecc3ab3b485763bb2a69b001c4a549a3c1bee4a0094945849e` | new sealed bytes |

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
JOINT_ANCHOR_DERIVED = false
```

CLOSURE_DECLARATION_END

# STAGE 8 — B01 CARRIAGE MANIFEST — OPPOSITE-LANE CHECK — CODEX 2 — V001

Date: 2026-08-11

Status: **DISCHARGED. All 15 old/new span pairs and both deletion-mask spans verify and tile their raw
files exactly. A separate structural-anchor derivation, with no line-alignment algorithm, produces
the same 13,934-byte remainder and `e3c634bc…` digest. Both refusal controls bite before emission.**

## 1. Preflight and verdict boundary

Members 02-05 rehash to the assignment pins and to their adjacent seals; member 02 is exactly 25,058
bytes. Members 06 and 07 likewise rehash to the manifest's old/new pins and their sidecars. The output
name was absent before authorship.

This check is documentary. It does not move B01's rows, statuses, coverage boundary, exhaustiveness
stop, finding, or B02 obligation. It checks only whether the replacement manifest is content-grounded,
whether its mask operation is determinate, whether a non-line-alignment route returns the same
remainder, whether the regenerator refuses mutations, and whether the manifest artifact carries
removed-class residue.

## 2. Mechanical manifest verification

The JSON was parsed directly. The old and new whole-file hashes first match members 06 and 07. Every
span was then extracted from the raw sealed bytes at its own coordinates, its stated length checked,
and its digest recomputed:

| Manifest rows | Old spans | New spans | Result |
|---|---:|---:|---|
| 01-05 | 5/5 | 5/5 | exact |
| 06-10 | 5/5 | 5/5 | exact |
| 11-15 | 5/5 | 5/5 | exact |
| **Total** | **15/15** | **15/15** | **30/30 span digests exact** |

The old zero-length side of insertion row 12 is `[23629,23629)` and hashes to the empty-string digest
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
it was verified rather than silently skipped.

### 2.1 Exact tiling

For each side, the published removal list was compared as a list to the sorted 15 replacement spans
plus the stated mask span. Both lists are exact, each has 16 intervals, and each is ordered and
non-overlapping. Complement construction accounts for every raw byte:

| Side | Raw bytes | Removed bytes | Complement bytes | Sum | Result |
|---|---:|---:|---:|---:|---|
| old V002 | 27,131 | 13,197 | 13,934 | 27,131 | exact |
| new V003 | 38,446 | 24,512 | 13,934 | 38,446 | exact |

The two complements are byte-equal. A zero-length insertion interval creates no coverage hole; it
binds the pairing position while the new side removes its 676-byte insertion.

## 3. The mask rule and all four readings

The decimal run immediately after the unique byte key `CLOSURE_END_BYTE = ` was found without using
the manifest offsets. It is exactly:

```text
D_old = [719,723) = bytes "3450"
D_new = [805,809) = bytes "4684"
```

The four readings were recomputed from members 06 and 07. For DELETE, the digit intervals join the
15 replacement spans. For a filler, only the replacement spans are removed and the four-byte digit
run on both sides is replaced by the named equal-width filler:

| Reading | Remainder length | Recomputed SHA-256 | Old/new equal |
|---|---:|---|---|
| **DELETE** | **13,934** | **`e3c634bcb9f8396216c33070b154ade8ed6cc91f7b68b4c1f85764bae6bcfc62`** | yes |
| `#` × 4 | 13,938 | `87a8cb7767fef07bc011f2f26ba2d770afe42da52352b6c90008d0a348efeeb6` | yes |
| space × 4 | 13,938 | `e418ebaad81cbdbc30da46c70069d9f0ade200ef7cea48d7fbe3ce8978007df1` | yes |
| `0` × 4 | 13,938 | `044c34157939b86e0f69a9fb74442cad1854b3d4c2a9e50a8010cefb4356c70c` | yes |

All four values reproduce Dario's table. Only deletion returns the independently diagnosed remainder;
the mask is therefore `DELETE-CONFIRMED`, not an equal-width fill.

## 4. Independent structural-anchor derivation

### 4.1 Method fixed without line alignment

No diff library, longest-common-subsequence routine, line sequence, or line-alignment opcode was used.
Instead, each raw artifact was parsed by a chain of its own named Markdown/record structure:

1. closure field keys and the decimal-run field;
2. closure table row identifiers 08 and 09;
3. the closure fence and declaration-end marker;
4. document title, date, status, and gate fence;
5. the inventory prelude, table/rationale boundaries, and blank structural separators;
6. the `### 3.1` heading and named FREEDOMS records;
7. audit-bullet leads, the final-section fence, final keys, and the press-paragraph continuation.

Every anchor token was required to occur exactly once on its side. Seventeen carried structural
segments were extracted between these markers and required byte-equal in order. The two one-byte
segments are the Markdown blank-line separators between inventory structural nodes; retaining them
is a syntax decision, not an alignment result. Replacement spans are the ordered gaps between the
17 segments; the decimal run is classified separately as the mask. Offsets below are outputs of the
unique-anchor searches, not entered coordinates.

### 4.2 Seventeen carried anchors

| # | Old span | New span | Bytes | SHA-256 | Equal |
|---:|---:|---:|---:|---|---|
| 01 | `[0,264)` | `[0,264)` | 264 | `6b9b13b3fb32aba5584f0176b1227f78e720e9d54e4608f83c7a386046d954bd` | yes |
| 02 | `[333,541)` | `[333,541)` | 208 | `11f47885c38a4a596d94f4a56ae42ad2ca721b5c3c96e91d0a414d0511f81311` | yes |
| 03 | `[630,719)` | `[716,805)` | 89 | `c36de5efa478880fff72587715276dc40f66d78f328a4a4c7f71e9a651c507d4` | yes |
| 04 | `[723,2638)` | `[809,2724)` | 1,915 | `c6f540526a52e9551fab2f161a19b36d6156e74286d3260cd8d0117c730d5518` | yes |
| 05 | `[2874,3330)` | `[4015,4471)` | 456 | `76a37bed7d16c23179cbd006d673c71918984d8672a70a3bed5f332fcaca2c34` | yes |
| 06 | `[3421,3451)` | `[4655,4685)` | 30 | `7db8bfc0418352d2ec9ff7d7ef815004d66f9c8575783f819f15b7ab2248f3bf` | yes |
| 07 | `[3587,3605)` | `[4821,4839)` | 18 | `acaa70caed7b7d537b0a41a487b95f483671cb6548963a30b3391f9b827b25f4` | yes |
| 08 | `[3992,7395)` | `[6971,10374)` | 3,403 | `dadc3b05e823709e4ef0a000da7f866e33ebf5f7b4e480a37e63249b306785ad` | yes |
| 09 | `[16304,16305)` | `[11338,11339)` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | yes |
| 10 | `[16740,16741)` | `[20793,20794)` | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | yes |
| 11 | `[17036,21967)` | `[24751,29682)` | 4,931 | `9d048c70f38ca1336f6e66328af748631ce7a6f7cac1397ee03869e781c8b2b3` | yes |
| 12 | `[22080,22510)` | `[30296,30726)` | 430 | `f0ea93c5409799b9faf8cd4a2e33c432d45c7c747d6244a4760af8e6f4e69139` | yes |
| 13 | `[22612,23629)` | `[31014,32031)` | 1,017 | `670a102b6afdde0030f43c15df436cbc2dc75b21eab124a29cfed964a8124725` | yes |
| 14 | `[23629,24291)` | `[32707,33369)` | 662 | `e8664a131ab1f4c4f64246b12abedd2223f2fc0f523cf471f1540e6c8a5241d1` | yes |
| 15 | `[24591,24624)` | `[34168,34201)` | 33 | `44a5b10b98f0988360d29c09a878a25680b6b4683b3664c1cacc8e13c0fa0264` | yes |
| 16 | `[26452,26503)` | `[37171,37222)` | 51 | `43567c21141973a29fa6734a13fa8945b5b00b8c73bc66a3870a22cc768373c7` | yes |
| 17 | `[26706,27131)` | `[38021,38446)` | 425 | `03c7029cf34a124757d29255ffde0017e0b3eb1f623c138e521c66c8215e6bad` | yes |

### 4.3 Independently derived gaps

Pairing the gaps around those anchors produces the following 15 replacement pairs; the mask gap is
shown separately. These are then compared to the JSON, never used as inputs from it:

| # | Old gap | New gap | Manifest comparison |
|---:|---:|---:|---|
| 01 | `[264,333)` | `[264,333)` | exact |
| 02 | `[541,630)` | `[541,716)` | exact |
| mask | `[719,723)` | `[805,809)` | exact decimal-run mask |
| 03 | `[2638,2874)` | `[2724,4015)` | exact |
| 04 | `[3330,3421)` | `[4471,4655)` | exact |
| 05 | `[3451,3587)` | `[4685,4821)` | exact |
| 06 | `[3605,3992)` | `[4839,6971)` | exact |
| 07 | `[7395,16304)` | `[10374,11338)` | exact |
| 08 | `[16305,16740)` | `[11339,20793)` | exact |
| 09 | `[16741,17036)` | `[20794,24751)` | exact |
| 10 | `[21967,22080)` | `[29682,30296)` | exact |
| 11 | `[22510,22612)` | `[30726,31014)` | exact |
| 12 | `[23629,23629)` | `[32031,32707)` | exact insertion |
| 13 | `[24291,24591)` | `[33369,34168)` | exact |
| 14 | `[24624,26452)` | `[34201,37171)` | exact |
| 15 | `[26503,26706)` | `[37222,38021)` | exact |

Concatenating the 17 carried anchors, with no manifest consulted in their derivation, returns:

```text
old/new byte equality = true
remainder length      = 13,934 bytes
remainder SHA-256     = e3c634bcb9f8396216c33070b154ade8ed6cc91f7b68b4c1f85764bae6bcfc62
```

This is a different method family and reproduces both the published spans and remainder. The earlier
line-alignment result is therefore invariant under this structural-anchor rederivation.

## 5. Regenerator warrant

The clean run was executed from the cleanroom with members 03, 06, and 07 unchanged:

```text
exit = 0
stderr = GROUNDED: 15 replacements + 1 mask span, both sides digest-checked; removal lists tile; remainders equal
REMAINDER_LEN = 13934
REMAINDER_SHA = e3c634bcb9f8396216c33070b154ade8ed6cc91f7b68b4c1f85764bae6bcfc62
```

The two controls were passed to the same code path as in-memory manifest instances, leaving the sealed
manifest untouched:

| Control | Mutation | Exit | Stdout | Stderr terminal fact |
|---|---|---:|---:|---|
| C1 | replacement 8 `new_sha256` = `0` × 64 | 2 | 0 bytes | `replacement 8: new span digest mismatch` |
| C2 | first `removal_spans_old` interval dropped | 2 | 0 bytes | `old removal list is not exactly the replacements plus the mask` |

Both refusals occur before any result emission. Restoring the unmodified manifest produces the clean
run above. `WARRANT = REFUSALS-REPRODUCED`.

## 6. Fresh self-catch replay

This scan did not reuse the prior confirm's disclosed alternatives. It fixed seven new semantic
families before inspecting hits:

```text
\bbyte[ _-]+identical\b
\b(?:unfalsifiable|private[ _-]+input)\b
\b(?:agreement|agreeing)\b
\b(?:whole|entire|global)\s+(?:artifact|document|remainder)\b[^\n]{0,32}\b(?:unchanged|identical|carried)\b
\b(?:all|every)\s+(?:bytes?|rows?|regions?)\b[^\n]{0,32}\b(?:same|unchanged|identical|carried)\b
\b(?:canonical|minimal|invariant)\s+(?:carriage|remainder|manifest)\b
\b(?:nothing|everything)\s+(?:outside|inside)\b[^\n]{0,32}\b(?:changed|moved|removed|carried)\b
```

No prose range was excluded. Cited register-entry numbers carry no lexical weight and none matches
these patterns. The scan returns nine raw hits:

| Pattern family | Subject lines / byte spans | Raw | Disposition |
|---|---|---:|---|
| byte equality | 45 `[3165,3179)`; 365 `[23202,23216)` | 2 | **LAWFUL:** both bind the current 13,934-byte remainder to member 05's bounded diagnostic |
| falsifiability/input custody | 44 `[3061,3074)`; 67 `[4086,4099)`; 301 `[18459,18472)`; 304 `[18762,18775)` | 4 | **LAWFUL:** current diagnosis of the superseded certificate and its explicit flattening rule |
| cross-method caution | 306 `[18924,18933)`; 324 `[20573,20581)`; 384 `[24795,24804)` | 3 | **LAWFUL:** current statements that the match is not proof and motivates this independent check |
| other four families | none | 0 | no locus |

All nine have current, bounded receivers. None reinstates a removed global carriage or process class.
Thus the fresh result is `9 raw / 0 residue`.

## 7. FREEDOMS-CONSUMED

```text
JOINT_ANCHOR_INPUT   = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  sealed V002 and V003; the carriage artifact, machine manifest, regenerator, and prior confirm; the
  B01 partial status, coverage boundary, exhaustiveness stop, and B02 obligation; all charter fences.

DERIVED HERE:
  thirty span-digest checks; two exact 16-interval removal-list comparisons; two full byte tilings;
  four mask readings; one seventeen-anchor structural rederivation with fifteen paired gaps and one
  mask; two refusal controls and one clean run; one fresh seven-family residue scan with nine loci.

SELECTED HERE:
  nothing. No primitive, row, status, signature, candidate, constructor, trace, descendant, measure,
  physical branch, scale, or selector is chosen, promoted, built, bound, or exercised.

SCALING WEIGHTS:
  none consumed, fixed, formed, compared, or substituted.
```

## 8. Flattening, blind, custody, and verb audit

- **FLATTENING CHECK:** file pins were not flattened into span pins; a removal list was not flattened
  into complete byte accounting; four equal block structures were not flattened into one mask
  reading; line-alignment agreement was not flattened into method independence until the structural
  anchor route reproduced it; nine lexical hits were not flattened into nine residues; documentary
  closure was not flattened into B01's unresolved exhaustiveness stop.
- **BLIND HELD / F_PLDEC:** only sealed bytes, paths, schemas, spans, digests, Markdown structure, and
  program control flow were inspected. No rank, ratio, response, fiber, physical quantity, or measured
  constant was read, formed, evaluated, or compared. Every scale stays symbolic.
- **PE-1..PE-17:** pointer-only; zero verdict weight.
- **omega_phys:** untouched.
- **BUILDER-NEVER-VERIFIES:** this is the assigned opposite-lane check and authors no B01 row.
- **CUSTODY:** cleanroom-side output only. The sealed inputs were read-only. No register, plan,
  tracker, git, commit, push, member binding, physical fixed-point execution, end test, or chain run.
- **VERB AUDIT:** `verified`, `exact`, `confirmed`, `invariant`, `reproduced`, `lawful`, and
  `discharged` receive displayed span hashes, byte sums, anchor spans, control exits, or lexical loci.
  They state documentary results only, not authorization, adoption, proof, or physical evaluation.

```text
CLOSURE = declared-first (byte 0; closure end 2589; scan 0 hits)
MANIFEST = 15/15-SPANS-VERIFIED
TILING = EXACT
MASK = DELETE-CONFIRMED
REDERIVATION = INVARIANT-CONFIRMED (structural-anchor chain)
WARRANT = REFUSALS-REPRODUCED
RESIDUE_GREP = 9/0 (fresh patterns)
VERDICT = DISCHARGED
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
```
