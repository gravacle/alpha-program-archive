# SURFACE V002 FIDELITY CHECK — AUDIT V001 (2026-08-14)

Auditor: FID-AUDIT (independent adversarial; default posture REFUTE — the check's verdict
assumed wrong until each component survived an independent pass; where verdicts differ, this
audit governs). Subject of audit: `SURFACE_V002_FIDELITY_CHECK_V001.md` (6cf12597, verified =
sidecar at path). Subject of the check: `SURFACE_DEFINITION_OF_RECORD_V002.md` (62e3ad8f,
verified = sidecar = tasked digest). Fences live throughout: alpha_computed = false;
proof_authorized = false; kappa_record_computed = false. No value of any physical quantity
computed, bounded, estimated, or compared; every numeral below is a sealed-text quotation, a
digest, an occurrence count, a line number, or a declared structural byte-count (byte-counts
of file segments are classified here as structural occurrence counts of bytes, not physical
quantities). No fenced-class file opened; no git; register row IDs (Q-….) are
EXPECTED-UNVERIFIABLE by design; the Documents origin tree was NOT entered — source-located
claims adjudicated against the sealed kstar audit bytes only.

---

## 0. VERDICT (one line)

CONFIRMED-WITH-CORRECTIONS — the check's FAITHFUL-WITH-CORRECTIONS verdict tier, its
byte-carry TRUE, all five of its corrections, both honest-quantifier adjudications, its lens
scan, its fence scan, and its §6 custody account each survived independent re-derivation with
zero support-failures in its claim-to-source tables; but the check's §3.5 sentence "honest
status; no over-claim" for the §VII preamble is REFUTED at one untraced phrase — V002 :108
"(the pushback fork's horn-b decider)" is an unsourced registrar role-claim colliding with the
sealed decider assignment (K* build :293-298) and the guard's own fork clause (:105) — a
sixth, WORDING-grade correction to V002 the check missed; plus three check-hygiene notes. The
missed item is of the same class as the check's four WORDING corrections and reverses no
entry's substance, so the verdict tier stands: FAITHFUL-WITH-CORRECTIONS, now SIX corrections
(1 SUBSTANCE, 5 WORDING).

---

## 1. SEAL VERIFICATION (my own pass, before any content read)

All recomputed with `shasum -a 256` at path and compared to `.seal.sha256` sidecars:

| Document | Recomputed = sidecar | vs tasked prefix |
|---|---|---|
| alpha_supervision/SURFACE_DEFINITION_OF_RECORD_V002.md | `62e3ad8fc8205240c3b5166251fefcc7ecdd89138fa2d651a086c5e99c120a05` MATCH | 62e3ad8f MATCH |
| alpha_supervision/SURFACE_DEFINITION_OF_RECORD_V001.md | `20ee87c0…86f842df` MATCH | 20ee87c0 MATCH |
| alpha_supervision/ACTUAL_SURFACE_GUARD_V001.md | `2baa4c31…788c4fd5` MATCH | 2baa4c31 MATCH |
| workspace/SURFACE_V002_FIDELITY_CHECK_V001.md | `6cf12597…40c71c614` MATCH | (no tasked digest; sidecar-verified) |
| workspace/BARE_SURFACE_I2_DETERMINATION_V001.md | `95235195…af9adb4c` MATCH | 95235195 MATCH |
| workspace/BARE_SURFACE_I2_DETERMINATION_AUDIT_V001.md | `97ae605d…4c545d73` MATCH | 97ae605d MATCH |
| workspace/STAGE8_TRANSPORT_LAW_POSED_V001.md | `22a2a478…e324ad0b` MATCH | 22a2a478 MATCH |
| workspace/STAGE8_TRANSPORT_LAW_POSE_CHECK_V001.md | `a5c71b2a…0489110c` MATCH | a5c71b2a MATCH |
| workspace/STAGE8_D0_SQUARE_CERTIFICATE_V001.md | `bb1b88ad…982d08c4` MATCH | bb1b88ad MATCH |
| workspace/STAGE8_D0_SQUARE_CHECK_V001.md | `d83655ae…07de492e` MATCH | d83655ae MATCH |
| workspace/STAGE8_T7_D3_QUANTIFIER_READING_FREEZE_AND_LEMMA_CONSUMPTION_V001.md | `9a0c2045…4a5fe20bb9` MATCH | 9a0c2045 MATCH |
| workspace/KSTAR_TYPING_DETERMINATION_V001.md | `2b12dc40…4c2a88d1c` MATCH | 2b12dc40 MATCH |
| workspace/KSTAR_TYPING_DETERMINATION_AUDIT_V001.md | `bb928de4…9d9ab161f` MATCH (sidecar) — **NOT the tasked 36183948** | see below |
| workspace/KSTAR_TYPING_DETERMINATION_AUDIT_PRIOR_V001.md | `3618394825a2adbc3a1fb28de6676799eb9927cdc1adb0f0e451061d1671710b` MATCH (sidecar) | 36183948 = tasked digest FOUND HERE |

**The one divergence from my tasking, resolved:** the tasked digest for the K* audit
(36183948) is not at the tasked path; the file at path is a successor (bb928de4, self-titled
"second issue", mtime 14:29:56). The tasked bytes survive sidecar-verified at
`KSTAR_TYPING_DETERMINATION_AUDIT_PRIOR_V001.md` (30829 bytes). This exactly matches the
check's §6 custody account, which I re-verified in content (§5 below). Entry 18 was
adjudicated — by the check and independently by me — against the 36183948 bytes, the artifact
V002 cites. Timeline consistency verified at path: V002 mtime 14:28 (sealed before the swap);
successor 14:29:56; successor sidecar 14:30; PRIOR copy 14:32:44; check 14:40 + sidecar 14:41.

---

## 2. INDEPENDENT BYTE-CARRY (my own method — no assumed split point)

The check assumed the title-block split (V002 lines 1-6) and ran `head -c`/`cmp` (its CL-1).
My method removes that assumption: read both files as raw bytes; take V001-body = everything
after V001's first newline (6536 bytes, SHA-256
`eeb83fb93aa95b81f9b70969ea93216bfd3bf87680ca056e679406f44831fa0f`); SEARCH V002's raw bytes
for that 6536-byte string as a substring.

Result: exactly ONE occurrence, at byte offset 339. The 339 bytes before it are exactly V002's
6-line title block (the `#` header, one blank line, the four-line italic block); the bytes
after it are exactly one blank line followed by `## VII. 2026-08-14 REFRESH …` through
end-of-file (V002 :105-161, 4736 bytes). The carried segment's SHA-256 equals V001-body's
(`eeb83fb9…`, both). No interior edit anywhere; the split point is FOUND by the bytes, not
assumed — which also independently discharges the check's CL-1 premise. **BYTE-CARRY TRUE;
the check's §2 result and its declared counts (6536; remainder = blank line + §VII) are
reproduced exactly.**

---

## 3. INDEPENDENT PASS — ENTRY 17 (the OPEN quantifier vs the frozen D3 reading)

Question: did V002, or the check, silently collapse "licensed generator family exhausts the
frozen D3 quantifier"? Independent findings, all at sealed bytes:

- The frozen reading: T7 :21-24 "FROZEN READING (the standard one): 'all common refinements of
  members of A and B' means ANY cellulation refining BOTH parents — unrestricted, universally
  quantified." V002's quotation "all common refinements of members" is a contiguous substring
  of the sealed text (T7 :30-31) — faithful truncation. T7 :67-69: full D3 admits
  "star-refined atoms of unbounded facet count, so NO uniform raw adjacency-degree bound
  exists over full D3" — V002's "admitting star-refined atoms of unbounded facet count" is the
  sealed content.
- The certificate's scope: CERT :8 "For every LICENSED generator … commutes EXACTLY over Z";
  the licensed inventory at CERT :136-140 is "cubical bisection; oriented
  simplicial/barycentric subdivision; and common refinements preserving the same smooth
  coframe and connection" — a RESTRICTED subclass of D3's unrestricted quantifier (the
  coframe/connection-preservation restriction is visible in the sealed inventory itself).
  CERT :143-144 seals "common refinements = composites, free by the sealed composite-closure
  step."
- My occurrence scans: the token `D3` occurs ZERO times in CERT and ZERO times in the D0
  check — neither asserts anything about D3, let alone exhaustion. D0 CHECK :13 scopes
  exhaustiveness explicitly: "the generator list is exhaustive of the sealed licensing" — of
  the LICENSING, not of D3. POSED :212-213 books O6e's obstruction "OUT OF SCOPE (star/fan
  refinement not in the working class)" and POSED flag :551-553 books O3 (O-D3
  decomposition-independence) UNBUILT/UNTOUCHED.
- Non-discharge (Spot A): the phrase "refinement/coarsening" occurs ZERO times in ALL FIVE
  entry-17 sources (my scan), and POSED :312 states in sealed bytes: "NO item is the derived
  law; nothing above is a ratified discharge" — stronger sealed support for V002's
  "candidate home, not a discharge" than the check exhibited. The register half of Spot A is
  EXPECTED-UNVERIFIABLE (registrar-vouched), as for the check.
- The count: POSED :29 "decomposes of record into FOURTEEN obligations"; POSED :551
  "OBLIGATION_LIST = 14 items, typed of record"; POSE_CHECK :316 "all 14 items trace to
  verified spans"; the tokens "fifteen"/"15 typed"/"15 obligations" occur ZERO times in POSED.
  Decisive strengthener the check did not cite: POSED :307-308 "SUMMARY TALLY over the
  fourteen numbered items (O6 counted once, its seven fields itemized)" — O6's fields are
  itemized WITHIN one counted obligation, so POSE_CHECK C1's "add the volume field as O6h
  BUILT" (:354-355) leaves the obligation count at FOURTEEN even after the correction.
  V002's "15 typed obligations" is unsupported under every reading. The check's Correction 1
  (SUBSTANCE) is CONFIRMED, and its adjudication (O6h = a field, not a fifteenth obligation)
  is CONFIRMED at POSED :307.
- POSE verdict grade: POSE_CHECK :354 "POSE_VERDICT = SOUND-WITH-CORRECTIONS(C1 …)" — the
  check's Correction 2 (V002's bare "checked" omits the grade) CONFIRMED.

**ENTRY-17 RESULT: the OPEN is genuinely open in the sealed sources, asserted closed nowhere
in the five sources, and neither V002 nor the check silently decided it. The check's Spot A
and Spot B adjudications are CONFIRMED; its Corrections 1, 2, 3 are CONFIRMED (for 3: V001
§I.3 (:22-23), §II.9 (:46-47), §II.10 (:48-49) verified inline-source-less via the proven
byte-identity, line map V001:N = V002:N+5).**

---

## 4. INDEPENDENT PASS — ENTRY 18 (STATUS-not-verdict; F1; source custody)

- **Guard CALIBRATION (:69-80):** "APPARATUS-ONLY is a STATUS, not a verdict: it means the
  object has not yet proven its place, never that it is condemned," with three lawful exits,
  the first primary. V002 entry 18: "K* is APPARATUS-ONLY as of today — a STATUS per the
  guard's CALIBRATION clause, not a verdict." The build's own bytes carry the same calibrated
  language (build :22 "APPARATUS-ONLY as of today — a STATUS, not a verdict"; flag :371-374
  "a STATUS per the guard's CALIBRATION, not a verdict: exit (1), primary …"). Entry 18
  reads exactly as the CALIBRATION clause demands and adds no condemnation and no promotion.
  V002 names the primary exit implicitly via the tie-theorem sentence and U-11 consumer — the
  presentation does not run the "harsher standard" the guard bars (exits are not reduced to
  discard/construct). CONFIRMED.
- **F1 treatment:** build :22 (F1 :124-125, echoed OPUS5 :93, unsupported homonym-binding
  whose cited spans contain zero K* occurrences), build :70 (the checker artifact has "NO
  SIDECAR anywhere in the archive" — V002's "sidecar-less checker"), build :330-333 ("caught
  by this determination rather than by the artifact's own checker"), build :143 (the FABLE
  path and :124-125 anchor); prior audit :149-163 re-verifies all four §2.4 points at bytes
  and rules "The build's OPEN ruling on beta-consumption (§3.2) is the correct quantifier;
  F1's shortcut is not." V002's sentence carries exactly this and no more. CONFIRMED.
- **β-consumption OPEN:** build :244-251 ("CANNOT be occurrence-decided today … OPEN, and
  named as such"); flag :363-364. V002: "OPEN of record." Not silently decided. CONFIRMED.
- **Identity + reverse sweep:** build :310-322 (five phrase-level byte-anchors); prior audit
  :240-246 ("verified phrase by phrase … IDENTITY — now anchored end to end"); prior audit
  :257-272 (reverse sweep: K_R, k_R, K_KK, K_n, K_square, kappa_record, kappa_Thomson — "None
  satisfies §IV's three byte-anchors simultaneously … §IV's referent is unique"). V002's "the
  whole K-family finds no other claimant" is the sealed content. Homonym: build :324-334,
  flag :367-370; prior audit :248-255. CONFIRMED.
- **Source custody:** the located-source parenthetical ((K/4)∫√|g| F_μν F^μν d⁴x on
  metric-carrying cell data gated by the D_BR spectrum; a3c7349b; manifest sealed_date
  2026-07-20) is carried at prior audit :26, :72-82, :185-190 — and the prior audit locates
  that source OUTSIDE the archive roots ("stepping outside the build's boundary … the origin
  program tree", its step-out carried as a named premise). V002 drops the boundary qualifier —
  the check's Correction 5 (WORDING) is CONFIRMED. Custody-carry discipline respected on my
  side: I verified against the sealed audit bytes only and did not enter the origin tree.
  The successor audit at path independently DEMOTES that location finding to
  "PRIOR-AUDIT-CLAIM at flagged custody, unverifiable under this brief" (successor :56-57,
  :346-347) — which RAISES the importance of the check's Correction 5 and of the registrar
  currency decision its §6 flags; my finding concurs with the check that this is a registrar
  matter, not a V002-vs-cited-source infidelity (V002 sealed 14:28, before the swap).
- **Tie-creating theorem:** build :178-189 ((i) appointed executable C_record(K), CODEX2 link
  9 ABSENT — link 9 verified at build :102; (ii) a theorem, not a substitution; (iii) if via
  saturation it must DERIVE saturation, booked ADOPTED); prior audit :165-173 ("confirmed and
  double-anchored" at the definition's own source sentence). U-11: build :266-270. Decision
  digest 75450619 at build :32. CONFIRMED.

**ENTRY-18 RESULT: all rows re-derived at sealed bytes; the check's §3.4 table is CONFIRMED
with zero support-failures; STATUS language guard-conformant; neither quantifier silently
decided.**

---

## 5. SPOT-VERIFICATION OF ALL REMAINING CHECK ROWS

| Check row / claim | My independent result |
|---|---|
| §3.1 entry-15 rows (11) | ALL CONFIRMED at build :9, :281, :284, :297, :303-307, :330, :345, :116, :39, :95-99, :3, :22; audit :9; the §IV-lever both-ends grounding verified at V002 :75 (= V001 :70) + build :284/:345 + audit :267 ("similar wording exists in off-ground §IV") |
| §3.1 omission check (C12) | CONFIRMED — build :322 C12 CONDITIONAL verified; build flag :345 itself states "referent-vacancy DERIVED" without restating C12; carry unchanged |
| §3.2 entry-16 rows (5) | ALL CONFIRMED at audit :61 (C-A verbatim), :62 (C-B verbatim), :63 (C-C verbatim), :9, :303; "zero free" occurs in build/audit ONLY as "zero free dimensionless slots" (build :176, :301, :313; audit :9, :177, :235, :303) — Correction 4 CONFIRMED as WORDING (the entry's own sentence restores the dimensionless scope) |
| §3.3 rows | see §3 above — ALL CONFIRMED; CERT :4 (CLAIMED-until-checked), :8-16, :251-259, :1864 verified; D0 CHECK :9/:528 CERT_VERDICT = CONFIRMED verified |
| §3.4 rows (11) | see §4 above — ALL CONFIRMED |
| §3.5 preamble | PARTIALLY REFUTED — "nothing below is authored physics" holds as corrected, BUT "honest status; no over-claim" missed the untraced V002 :108 phrase; Correction A1 below |
| §4 fence scan | CONFIRMED independently — my own numeral sweep of V002 :106-161 traces every numeral to a sealed carrier except exactly one: "15 typed obligations" (V002 :134-135). Sole hit reproduced |
| Lens scan | CONFIRMED independently — my vocabulary scan (lens/ether/narrat/beautif/remarkab/striking/tantaliz/suggest/hint/converg/motivat/elegan/compelling/story) over all of V002 returns 3 hits, ALL substring artifacts ("whether" ⊃ 'ether' at :69/:143; "history" ⊃ 'story' at :126); zero motivational/convergence content in §VII; the sources' "lens grade" markings appear nowhere in V002 |
| §6 custody event | CONFIRMED in content — successor at path self-titled "second issue" (:1), "runs under the stricter brief" (:50), demotes C3 to PRIOR-AUDIT-CLAIM at flagged custody (:56-57, :346-347), carrier set SEVENTEEN (:138, :322); prior copy = tasked 36183948 bytes, sidecar-verified; mtime sequence consistent (§1) |
| Check's V002/V001 line-cites | ALL CONFIRMED (entry 15 = :112-123; 16 = :125-131; 17 = :133-144; 18 = :146-161; preamble :108-110; title block :1-6; V001 map N↔N+5 proven by byte-identity) |

Hunted and NOT found: (i) support the check accepted that fails — none; (ii) unfaithfulness
the check missed — ONE (Correction A1); (iii) lens-grade content the check failed to flag —
none.

---

## 6. CORRECTIONS (this audit's, numbered; tags: VERDICT-CHAIN = touches a verdict-bearing
sentence of the check; COSMETIC = does not)

1. **A1 / VERDICT-CHAIN (at the check's §3.5 sentence; WORDING-grade for V002)** — V002 :108
   "(the pushback fork's horn-b decider)" is an unsourced registrar role-claim the check never
   traced. No sealed source appoints the refresh a fork decider: the K* build states in sealed
   bytes "What would decide between them: the appointed executable `C_record(K)` (link 9) plus
   the §2.5 theorem … Neither is decided here; the fork stays open" (build :293-298); the
   guard's fork clause ends "The fork stays open until a determination closes it" (guard
   :105), and horn (b)'s own content ("a booked absence records what has been derived, not
   necessarily what the actual surface carries", guard :100-101) cannot be decided by ANY
   refresh of booked content; the successor audit likewise books "named deciders" as the
   build's (successor :479). At most the refresh serves horn-b adjudication hygiene (pushback
   must target the current booked description — the clause after the colon says exactly this).
   The parenthetical also violates V002's own charter clause "Every clause carries its booked
   source" (V002 :12). Suggested fix: strike the parenthetical or reword to "(so pushback
   adjudications target the current booked description — the fork's horn-b hygiene)".
   Grade for V002: WORDING (sixth correction; no horn is actually decided anywhere in V002's
   operative entries — entry 18 preserves STATUS + OPEN; possible register grounding
   EXPECTED-UNVERIFIABLE, none cited inline). Effect on the check: its §3.5 "no over-claim"
   sentence is refuted; its verdict tier is not.
2. **A2 / COSMETIC (check hygiene)** — the check's §3.3 and flag block use the bare label
   "CHECK" for two different sealed artifacts ("CHECK :13" = the D0 check d83655ae; "CHECK
   :316" = the pose check a5c71b2a). Both resolve correctly at the cited bytes, but the label
   is ambiguous in a document whose currency is citations.
3. **A3 / COSMETIC (check hygiene)** — the check's Spot-B row writes "the licensed inventory
   verbatim: cubical bisection; oriented simplicial/barycentric subdivision; composites"; the
   sealed inventory's third item is "and common refinements preserving the same smooth coframe
   and connection" (CERT :139-140); "composites" is CERT's own gloss (:143-144 "common
   refinements = composites"), so nothing is misattributed — but a list labeled "verbatim"
   should not substitute a gloss for the third item, especially since the sealed
   coframe/connection-preservation restriction is itself evidence for the very OPEN being
   adjudicated.
4. **A4 / COSMETIC (registrar attention; unresolvable at bytes)** — the check's CL-7 declares
   "writes = this artifact + its sidecar only," while its §6 rests on the preservation copy
   `KSTAR_TYPING_DETERMINATION_AUDIT_PRIOR_V001.md` (mtime 14:32:44, after the 14:29:56 swap
   and before the check's 14:40 seal). The check's wording ("re-verified INTACT at") reads as
   verification of an existing file, implying another agent (the swapping registrar) wrote the
   preservation copy — consistent, but authorship is not decidable from bytes here. Registrar
   should confirm who wrote the PRIOR copy; if the checker wrote it, its CL-7 needs one line.

None of A1-A4 reverses the check's verdict tier or any entry's substance.

---

## 7. CHOICE LEDGER (this audit's unforced choices)

- **AL-1 byte-carry method** — IMMATERIAL(proven): substring search finds the split rather
  than assuming it; the unique-occurrence result subsumes every split convention (and thereby
  discharges the check's CL-1 premise independently).
- **AL-2 entry-18 standard** — PREMISE(named): entry 18 adjudicated against the 36183948
  bytes V002 cites (at the PRIOR-copy path, digest = sidecar = tasked digest), same as the
  check's CL-2; the successor (bb928de4) consumed only to verify the check's §6 custody
  account. The registrar owns the currency decision.
- **AL-3 register rows** — PREMISE(named): Q-1056/Q-1025/Q-1026/Q-1063, the Spot-A register
  half, and any register grounding of the A1 phrase are EXPECTED-UNVERIFIABLE by design.
- **AL-4 lens-scan scope** — OPEN at the margin: my vocabulary list is a choice; lens-grade
  phrasing outside it would evade the regex. Mitigation: full manual read of §VII (56 lines)
  found no motivational/convergence framing; margin shared with the check's own scan.
- **AL-5 occurrence-scan scope** — PREMISE(named): "asserted nowhere" confirmations range
  over the sealed sources at path (same narrowing as the check's CL-4); a corpus-wide
  assertion outside the tasked set would evade both passes.
- **AL-6 numeral classification** — IMMATERIAL(named convention): dates, entry numbers, and
  structural byte counts treated as document metadata / structural occurrence counts; every
  physics-adjacent numeral in this artifact is a sealed-text quotation, digest, count, or
  line number.
- **AL-7 A1 severity call** — PREMISE(named): the horn-b-decider phrase graded WORDING, not
  SUBSTANCE, because V002's operative entries preserve STATUS/OPEN and no fork horn is
  anywhere decided; a stricter reading (role-claim = silent partial fork-collapse) would
  grade it SUBSTANCE and flip my outcome to REFUTED-AT the check's §3.5. The stricter reading
  is rejected because the guard's fork clause polices pushback ADJUDICATIONS, and V002
  performs none — it consolidates.

**TOY_SEPARATION (this audit) = clean** — every verdict step is byte-reading at digests
verified in §1; the named margins (AL-4 vocabulary, AL-5 scope, AL-7 severity) are disclosed
with mitigations and none is load-bearing alone; no load-bearing step rests on an unproven
convenience.

---

## 8. FLAG BLOCK

```text
AUDIT_VERDICT = CONFIRMED-WITH-CORRECTIONS — the check's FAITHFUL-WITH-CORRECTIONS tier
    stands; zero support-failures found in its claim-to-source tables; its five corrections
    all re-derived CONFIRMED at sealed bytes (the SUBSTANCE count correction strengthened:
    POSED :307-308 "fourteen numbered items (O6 counted once, its seven fields itemized)"
    fixes the count at FOURTEEN even post-C1); byte-carry independently TRUE by a
    split-agnostic method (V001 body eeb83fb9…, 6536 bytes, exactly one occurrence in V002
    at offset 339; remainder = blank line + SVII, :105-161).
CHECK_MISS = ONE, wording-grade: V002 :108 "(the pushback fork's horn-b decider)" —
    unsourced registrar role-claim; sealed decider assignment is link 9 + the S2.5 theorem
    (K* build :293-298, "the fork stays open"); guard :105 "until a determination closes
    it"; violates V002's own "Every clause carries its booked source" (:12). Becomes V002's
    SIXTH correction (1 SUBSTANCE, 5 WORDING). The check's S3.5 "no over-claim" sentence is
    refuted; its verdict tier is not.
ENTRY_17 = independently re-derived — the licensed-family-vs-frozen-D3 OPEN is genuine
    (zero D3 tokens in CERT and D0 check; D0 CHECK :13 scopes to "the sealed licensing";
    T7 :67-69 star-refined atoms; POSED :212-213 star/fan not in the working class; POSED
    flag O3 O-D3 UNBUILT/UNTOUCHED) and V002 does NOT silently decide it; non-discharge
    additionally sealed at POSED :312 "nothing above is a ratified discharge".
ENTRY_18 = independently re-derived — STATUS-not-verdict language conforms to guard
    CALIBRATION :69-80 and is the build's own (build :22, flag :371-374); F1 adjudication,
    reverse sweep, tie-theorem, U-11, beta-consumption OPEN all carried faithfully; located-
    source custody qualifier dropped (check Correction 5 CONFIRMED, importance RAISED by the
    successor audit's demotion to PRIOR-AUDIT-CLAIM).
CUSTODY = the tasked K* audit digest 36183948 is NOT at the tasked path (successor bb928de4
    at path, sidecar-verified); tasked bytes verified INTACT at
    KSTAR_TYPING_DETERMINATION_AUDIT_PRIOR_V001.md; check's S6 account CONFIRMED in content
    and timeline; PRIOR-copy authorship not decidable at bytes (Correction A4) — registrar
    to confirm writer and adjudicate entry-18 citation currency.
LENS_SCAN = clean (independent) — 3 regex hits, all substring artifacts (whether/history);
    zero motivational or convergence content in SVII.
FENCE_SCAN = concurs — sole unsupported numeral in V002 is "15 typed obligations"
    (V002 :134-135); every other numeral traces to a sealed carrier.
CORRECTIONS(THIS AUDIT) = 4: A1 VERDICT-CHAIN (the missed horn-b-decider phrase);
    A2 COSMETIC (ambiguous "CHECK" label for two artifacts); A3 COSMETIC ("verbatim"
    inventory list substitutes CERT's own composites gloss for item three); A4 COSMETIC
    (CL-7 vs PRIOR-copy authorship, registrar to confirm). None reverses substance.
FENCES = intact — alpha_computed = false; proof_authorized = false;
    kappa_record_computed = false; no value computed/bounded/estimated/compared; every
    numeral a sealed-text quotation, digest, occurrence count, line number, or declared
    structural byte-count; no fenced-class file opened (fenced filename hits in listings
    not opened); no git; no existing file edited; writes = this artifact + its sidecar.
```
