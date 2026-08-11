CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
PREDECLARATION_REGION = EMPTY (closure opens at byte 0; the closure block is the first content)
PREDECLARATION_OUTPUT_SCAN = 0 hits in authored prose (27-token sweep) -- CLAIMED, not clean (Q-921)
VERDICT_BEARING_SET = exactly the 9 content-addressed members below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
PATH_RULE = every member carries its FULL path from the alpha-program-archive root and is rehashed at
  that path before sealing (Q-913 standard).
LANE = DARIO   ROLE_THIS_RELAY = THE CARRIAGE DELTA MANIFEST AND NOTHING ELSE
DIGEST_RULE = every span digest and every byte offset in section 3 COMPUTED by member 06 from members
  02 and 03 at seal time.  No offset and no digest in this artifact is typed by hand.
ALL_RESULTS = CLAIMED until the opposite-lane check.
CLOSURE_END_BYTE = 2739
```

| # | Closed member | SHA-256 | Role |
|---:|---|---|---|
| 01 | `relay_inbox/RELAY_PASTE_1014_B01_DELTA_MANIFEST_DARIO_V001.md` | `4dbac451c832a1109c49737788fcd3e126a8c58df0f65ff24f8bd78bd7b13881` | assignment |
| 02 | `workspace/STAGE8_DESC_B01_DARIO_V002.md` | `19bf16f7ec1dda3e4c039e57b99a2896db4e9074ff1904e0e52096e2e90cf01b` | **the OLD side; sealed, untouched** |
| 03 | `workspace/STAGE8_DESC_B01_DARIO_V003.md` | `41ea9708aa51bdecc3ab3b485763bb2a69b001c4a549a3c1bee4a0094945849e` | **the NEW side; sealed, untouched** |
| 04 | `workspace/STAGE8_DESC_B01_V003_CONFIRM_CODEX2_V001.md` | `8ae0a95c02e645c71f87f32730685664090fa770304561ce9277397c83ae0aa4` | **the finding this artifact repairs, and the diagnostic it must meet** |
| 05 | `workspace/b01_carriage_manifest_v001.json` | `346a1095672abf1678525802559d912ba9859d068e0707564e9291a7d1d4edc4` | **THE MANIFEST ITSELF** — sealed and declared; the machine-readable form of §3 |
| 06 | `workspace/build_b01_carriage_remainder_v001.py` | `c1f84957a209ca1781d5d8a2d9bbfca07fd6eea9630d65e58957feb909a7b2ee` | the regenerator; **its declared inputs are exactly members 02, 03 and 05** |
| 07 | `supervision/PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | state pin |
| 08 | `supervision/LOCKED_PROCESS.md` | `38149496a2b5d89d20b614d972bffef1867d7cde573b26d77dfb207ece3446fb` | process law |
| 09 | `supervision/DECLINE_REGISTER_V002.md` | `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | S01–S37 |

```text
BLIND HELD.  EVERY SCALE SYMBOLIC.  NO NUMERIC EVALUATION OF PHYSICAL QUANTITIES.
NO ROW, STATUS, STOP, OBLIGATION OR FINDING MOVES.  B01 REMAINS PARTIAL ON ITS EXISTING
EXHAUSTIVENESS STOP.  V002 AND V003 ARE READ ONLY AND STAY SEALED.  omega_phys UNTOUCHED.
```

CLOSURE_DECLARATION_END

# STAGE 8 — DESCENT SECTION — B01 CARRIAGE DELTA MANIFEST — DARIO LANE — V001
## RELAY 1014 — `[PLAN:DESC-22]` — THE TARGET DIGEST CANNOT DEFINE ITS OWN INPUT

Date: 2026-08-11
Status: **V003's `CARRIED = VERIFIED` line is SUPERSEDED by this manifest. Its number was not shown to
be wrong; it was shown to be UNFALSIFIABLE, which is worse. The regenerated remainder is 13,934 bytes
digesting to `e3c634bc…` — byte-identical to the value the opposite lane computed independently, and
not the 12,755 / `857992a0…` V003 advertised. Every removed byte interval is now published and
content-addressed on both sides, so the claim can be refuted by anyone holding three sealed files.**

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
JOINT_ANCHOR_DERIVED = false
```

---

## 1. The finding, accepted without qualification [PROVABLE]

Member 04 names the defect in one sentence and the sentence is exactly right:

> *"The target digest cannot define its own input."*

V003 published a remainder length and digest. It did not publish the replacement spans its
computation excluded. **The digest was real; the input to it was private.** An opposite lane holding
every sealed byte could not recompute the number, and therefore could not refute it either. That is
not a small bookkeeping slip — an unfalsifiable claim is worse than a wrong one, because a wrong one
gets caught.

**The specific mechanism, stated so it is not repeated.** My mask blanked whole *regions* by pattern —
the final-lines block, the press paragraph — rather than the exact replaced *spans*. A region swallows
the equal bytes lying inside it. Member 04's deterministic diagnostic keeps those bytes and lands on
13,934; mine discarded 1,179 of them for a reason no reader could see. And V003's §0 gave **prose
repair locations for four repairs**, which I let stand in for a specification; the actual change set
also touches the closure roster and role, the heading and status, §0 itself, §6, §7, §8 and the
closing paragraph. **A summary and a specification are different objects and I conflated them.**

**What the finding does not touch**, per member 04's own boundary: the four ordered repairs, the
generator warrant with its real refusal, the 26 row spans, the span-convention ruling, and two
separately byte-confirmed operative regions — `[## 1 … ## 3)` 2,773 B `a4878c49…`, and
`[### 3.1 … ## 6)` 4,540 B `40f8fc89…`, **the second of which carries the coverage boundary, the
exhaustiveness stop, the §5 ordering finding and the B02 forward obligation.** Those operative
invariants were never in question and are not in question now.

---

## 2. The mask rule, stated as a byte operation [PROVABLE]

This is the part V003 owed and did not give.

```text
Let KEY  = the byte string "CLOSURE_END_BYTE = "
Let D_old = the half-open interval of the DECIMAL DIGIT RUN immediately following KEY in member 02
Let D_new = the same in member 03

THE MASK IS DELETION.  Those bytes are REMOVED.  They are NOT replaced by a filler of equal width.
```

```text
D_old = [719,723)   bytes "3450"
D_new = [805,809)   bytes "4684"
```

**Why this has to be said out loud.** The digit run is four bytes wide on both sides, so *every*
reading of the word "blank" produces the identical block structure — 15 replacement blocks, every
time. It does not produce the identical remainder:

| reading of "blank" | remainder length | remainder SHA-256 |
|---|---:|---|
| **DELETE the digits** | **13,934** | **`e3c634bcb9f8396216c33070b154ade8ed6cc91f7b68b4c1f85764bae6bcfc62`** |
| replace with `#` × 4 | 13,938 | `87a8cb7767fef07bc011f2f26ba2d770afe42da52352b6c90008d0a348efeeb6` |
| replace with space × 4 | 13,938 | `e418ebaad81cbdbc30da46c70069d9f0ade200ef7cea48d7fbe3ce8978007df1` |
| replace with `0` × 4 | 13,938 | `044c34157939b86e0f69a9fb74442cad1854b3d4c2a9e50a8010cefb4356c70c` |

**Four readings, one word, four digests, and nothing in the output that tells you which was used.**
That is the same disease Q-913 and Q-917 each ruled on, one level further down again —
this time inside a repair written *because* of that disease. I display it rather than merely pick,
because the picking is the whole failure mode.

**DELETE is the rule of record here, and not because I prefer it:** it lands on member 04's
independently computed diagnostic exactly. Where my preference and the opposite lane's arithmetic
could differ, the opposite lane's arithmetic wins.

---

## 3. The ordered delta manifest [PROVABLE — computed by member 06, nothing typed]

Fifteen replacements, in document order, each content-addressed **on both sides**. Old spans are into
member 02, new spans into member 03, both in the **raw sealed files' own coordinates** — not into any
masked intermediate, so a verifier never has to reconstruct my working buffer.

| # | tag | old span (member 02) | len | old SHA-256 | new span (member 03) | len | new SHA-256 |
|---:|---|---|---:|---|---|---:|---|
| 1 | `replace` | `[264,333)` | 69 | `d8f6d9f5a4ac7a4b3104b40c316d599c6057782bf84f952ddca6e5e30d890ca1` | `[264,333)` | 69 | `d90bdaea19e0fd8493d527e10b643fa8e24f403adaa3ae8a012390b8a2bd8fd0` |
| 2 | `replace` | `[541,630)` | 89 | `8ae0ffbf4ddea44111e694426bd3c76a08dd649084e033f8a9823d224f367280` | `[541,716)` | 175 | `f48b2fcc1fa189a468759e886ef893aaeceaf26cc4e98a970ef6cad914ffbeaf` |
| 3 | `replace` | `[2638,2874)` | 236 | `1ac2ffaa853dc8f7e241bd247659864708299da770124f12ec05fde84ecad87a` | `[2724,4015)` | 1291 | `a45cdce0fce1c072013e0d7f918ed3fc6f69daeb0e938ddde4b0116d5b6a5777` |
| 4 | `replace` | `[3330,3421)` | 91 | `5ea19651d32494dbbbd9548a654647c05db9d73eef1de77f87d231e8943640bb` | `[4471,4655)` | 184 | `82ef0bc39ce9afeffc06b91c6d98f3212940d3269f2f88b6421ad4c0c6414281` |
| 5 | `replace` | `[3451,3587)` | 136 | `0123b32bca3e7bc9aaab6b9f4704aee8eed2ab4dc771d36d8c7d37cf924fd5bb` | `[4685,4821)` | 136 | `330c70aea334adba4679d2ab751dd4a42e36a5c4ae1b403f045f54250b65da23` |
| 6 | `replace` | `[3605,3992)` | 387 | `eec2056363759ba745131ed8a87a21289fd49b22c9df8c3656f19a9fe9e0041e` | `[4839,6971)` | 2132 | `d444c9168f3fb0c662e40ff8e53726cb9c00252df9e1bed428a2c97637ab1a3c` |
| 7 | `replace` | `[7395,16304)` | 8909 | `5ee66379effcbf9dd44707604204d5484da0fb1ee44a7284afae2e0e3d200616` | `[10374,11338)` | 964 | `aea177ee2b514e8dcdeb175a4b4439d23d82d6939030625ea99f63796c366cb9` |
| 8 | `replace` | `[16305,16740)` | 435 | `69861033fc5e4cd55425c3e6099af2120228a260ca36efdeffc48cc9eabe1374` | `[11339,20793)` | 9454 | `277ea881d941e85831295b5c7599f2fdfcb275beb6d67e375016379b7733f7dc` |
| 9 | `replace` | `[16741,17036)` | 295 | `0d8a120c4a61263fe07e23228f00d018fb9801b7c05be6797361dc4d069380e0` | `[20794,24751)` | 3957 | `5bd0fd8462d5bae8c46aa523250790d3c9ecaabc34f11852538d5d0fe4bd293b` |
| 10 | `replace` | `[21967,22080)` | 113 | `e18492dd49c3f037ff4bd89ecea727ea869548feadc0a78b112dbfa4f474b48f` | `[29682,30296)` | 614 | `40ae0b916d816909793d815a899234c9129b56cb21fe46c647565f6166181d99` |
| 11 | `replace` | `[22510,22612)` | 102 | `b15d863193b1e8f647497a8222e9cd8c23d2a1fc554ea4691034f5f408e46831` | `[30726,31014)` | 288 | `e97b25476645f1bf27f759b6eb7d195e933b88f4608212583a18237f7b3a9b19` |
| 12 | `insert` | `[23629,23629)` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `[32031,32707)` | 676 | `ce2c3ba9182b109b3f0e84cf60c27b91e7986a07027fa1b75de97a9c1fcbea63` |
| 13 | `replace` | `[24291,24591)` | 300 | `bb1042bdb7af6787b98cb9f7890c8c203d9f617ef54d394ba6b583d89a65d4f8` | `[33369,34168)` | 799 | `57889c18ac9747885b06efeb7462f9066897cc0e08611781f3bdda2d62375dc0` |
| 14 | `replace` | `[24624,26452)` | 1828 | `b1c7c408f8e71590f0087e6d75bcaaf89fd10a4db9896caf6ae8dc115213f624` | `[34201,37171)` | 2970 | `508950a8db131b0d54bd77cd1e00f6804402437ac831c2587d197c8464868e56` |
| 15 | `replace` | `[26503,26706)` | 203 | `780d86491af5d46df8c0104b735edf52076049f51c55af64fd5362db0d434789` | `[37222,38021)` | 799 | `d3d135129e66db6668d11f30004a99273c9110d038392fc631688ae676859c11` |

Row 12's old digest is `e3b0c442…`, the SHA-256 of the empty string — that is what an insertion's old
side is, and it is printed rather than left blank so no reader has to infer it.

### 3.1 How the spans were chosen, and why that stops mattering once they are published

Disclosed method: mask both files by the §2 rule, split on line boundaries with terminators retained,
run a `SequenceMatcher(autojunk=False)` over the line sequences, take the non-`equal` opcode blocks,
and map their line indices back to raw byte offsets.

**That derivation is a convention, and conventions are exactly what this section keeps catching.** So
it is disclosed and then made irrelevant: **once the spans are published as explicit half-open byte
intervals with digests, they ARE the definition.** Verification needs no diff algorithm, no library
version, and no knowledge of how I chose them — only the three checks in §4. A different diff might
have drawn different block boundaries; it would then have produced a different manifest, which anyone
could compare against this one byte for byte. **That is the difference between this and what V003
sealed.**

### 3.2 Two span digests that corroborate the manifest from outside it

- Row 7's **old** digest `5ee66379effcbf9d…` is the stdout digest member 04's predecessor recorded for
  the **V002** generator run.
- Row 8's **new** digest `277ea881d941e858…` is the stdout digest member 04 recorded for the **V003**
  generator run.

Neither was put there by me: they fall out of hashing the two artifacts' §3 table regions. **Two
digests computed by the opposite lane through a completely different route land inside this manifest
at the rows where the table changed.**

That also reconciles a difference of one byte between two true statements: my 1006 report gave the
V003 generator stdout as 9,453 B / `3234fc7f…`, member 04 gave 9,454 B / `277ea881…`. Both are
correct — mine of the stdout with its final newline stripped, the confirm's of the stdout as emitted.
Row 8's length is 9,454, so the artifact's table region is the stdout **as emitted**. No discrepancy;
two measurements of two different byte strings, now labelled.

---

## 4. The remainder, REGENERATED [PROVABLE — member 06's output]

```text
removal_spans_old := sort(the 15 old spans + D_old)      -- 16 intervals, asserted disjoint & ordered
removal_spans_new := sort(the 15 new spans + D_new)      -- 16 intervals, asserted disjoint & ordered
remainder_old     := concat of the complement of removal_spans_old in member 02
remainder_new     := concat of the complement of removal_spans_new in member 03
CARRIED holds iff remainder_old == remainder_new
```

Member 06's run, pre-seal:

```text
MASK_RULE       = DELETE the decimal digit run after "CLOSURE_END_BYTE = "
MASK_SPAN_OLD   = [719,723)  bytes '3450'
MASK_SPAN_NEW   = [805,809)  bytes '4684'
REPLACEMENTS    = 15
REMOVED_OLD     = 13197 bytes of 27131
REMOVED_NEW     = 24512 bytes of 38446
REMAINDER_LEN   = 13934
REMAINDER_SHA   = e3c634bcb9f8396216c33070b154ade8ed6cc91f7b68b4c1f85764bae6bcfc62
```

`remainder_old == remainder_new` held; member 06 refuses to print a length or digest otherwise.

**THE CROSS-LANE MATCH.** Member 04's diagnostic, run independently, by another lane, from the sealed
bytes alone:

```text
equal-block remainder length   = 13,934 bytes
equal-block remainder SHA-256  = e3c634bcb9f8396216c33070b154ade8ed6cc91f7b68b4c1f85764bae6bcfc62
```

**Identical in length and digest.** Two lanes, two methods — theirs by concatenating equal blocks,
mine by removing published spans from the raw files — arriving at the same bytes.

---

## 5. The V003 claim: SUPERSEDED [PROVABLE]

```text
V003 CARRIED = VERIFIED  ->  12,755 bytes / 857992a0f0deedbec2ce07a21c8b0d87dfca06fc12f537ff6d469553ec7406b5
THIS MANIFEST           ->  13,934 bytes / e3c634bcb9f8396216c33070b154ade8ed6cc91f7b68b4c1f85764bae6bcfc62

V003_CLAIM = SUPERSEDED.  NOT RECOVERED, AND NOT DEFENDED.
```

The 1,179-byte gap is accounted for and I state it as my error rather than as a difference of method:
those bytes are **equal** in both artifacts and belong in the remainder. My region-shaped mask
discarded them because it removed the whole final-lines block and the whole press paragraph instead of
the exact replaced spans inside them. **V003's line is superseded by this artifact; V003 itself is not
withdrawn, is not edited, and remains sealed** — supersession here is append-only, as everywhere else
in this program. Nothing else in V003 is affected: member 04 confirmed the four repairs, the warrant,
the 26 spans and the span convention, and this artifact touches none of them.

---

## 6. Warrant: the regenerator refuses [PROVABLE — controls run]

Member 06 opens only members 02, 03 and 05 — no other file, no environment, no network. Every check is
fatal **before** any result line prints: file digests against the manifest; the mask spans really
being the digit run after the declared key and not truncating a longer run; each replacement's old and
new span digest; the removal lists being exactly the replacements plus the mask; ordering and
non-overlap; and final remainder equality.

Two controls were run against mutated copies of member 05, with members 02 and 03 held fixed:

| control | mutation | result |
|---|---|---|
| C1 | row 8's `new_sha256` set to `0`×64 | `exit 2`, empty stdout, `replacement 8: new span digest mismatch` |
| C2 | one interval dropped from `removal_spans_old` | `exit 2`, empty stdout, `old removal list is not exactly the replacements plus the mask` |

Both refused, and **stdout was empty in both** — the refusal precedes emission rather than annotating
it. The manifest was restored from backup and the normal run returned the §4 figures unchanged.

---

## 7. FREEDOMS-CONSUMED

```text
JOINT_ANCHOR_INPUT   = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  V002 and V003 at their sealed bytes; member 04's finding, its diagnostic figures, its two
  byte-confirmed operative regions and its four confirmed repairs; the V002 and V003 generator stdout
  digests it recorded; the span convention it ruled declared-lawful; all gates and process fences.

DERIVED HERE:
  the fifteen aligned replacement spans with a digest on each side, in document order, in raw
    coordinates;
  the mask rule stated as a byte operation, with the four-reading demonstration that shows the choice
    was invisible until stated;
  the regenerated remainder and its equality across both sides;
  the reconciliation of the 9,453/9,454 stdout figures as two true measurements of two byte strings;
  two refusal controls;
  the accounting of the 1,179-byte gap as my region-shaped mask, not as a difference of method.

SELECTED HERE:
  nothing.  No primitive, row, status, signature, candidate, constructor, trace, descendant, measure,
  physical branch, scale, or selector is chosen, promoted, built, bound, or exercised.  No repair of
  member 04's is re-adjudicated.  The remainder figure was not steered: DELETE was adopted because it
  meets the opposite lane's independently computed value, and the three rejected readings are
  displayed rather than discarded.

SCALING WEIGHTS: none consumed, fixed, formed, compared, or substituted.  No rank, ratio, or physical
  quantity was read, formed, or evaluated.  Every scale symbolic.
```

---

## 8. Flattening, custody, byte audit

- **S01–S37 FLATTENING CHECK — walked, clean.** A **summary** was not flattened into a
  **specification** — that conflation is the whole defect §1 accepts. A **digest** was not flattened
  into a **verification**: a real digest over a private input verifies nothing, which is the sentence
  member 04 supplied and this artifact adopts. A **derivation convention** was not flattened into a
  **definition** (§3.1): the spans are the definition, the diff is only how they were found. A
  **region** was not flattened into a **span**. An **unfalsifiable claim** was not flattened into a
  **false one**, nor a false one into a substantive defect: no row, status, stop, obligation or
  finding moves. **Agreement was not flattened into proof** — §4's cross-lane match is two methods on
  the same bytes, not an independent confirmation of the span choice itself, which remains CLAIMED.
- **BUILDER-NEVER-VERIFIES:** everything here is CLAIMED until the opposite-lane check. I did not
  re-adjudicate member 04's four confirmations or its span-convention ruling.
- **BLIND held.** No rank read, no ratio formed, no fiber compared, no physical quantity evaluated.
- **PE-1..PE-17:** pointer-only, zero verdict weight.  **omega_phys:** untouched.
- **SCOPE:** the carriage certificate only. B01's inventory, boundary, stop and forward obligation are
  read-only here and unchanged; B02 is untouched.
- **CUSTODY:** archive-side only. Three files written in `workspace/` — this artifact, the manifest,
  the regenerator — all sealed. V002 and V003 rehash to their sidecars unchanged. No register, plan,
  tracker, git, commit or push action. Nothing adopted, nothing registered.
- **BYTE AUDIT:** all 9 members rehashed at their full paths at seal time; all 15 span pairs and both
  mask spans computed by member 06 from members 02 and 03, which was RUN PRE-SEAL and whose output is
  quoted at §4; closure declared at byte 0 with its end computed on bytes as a fixed point; 27-token
  pre-closure scan over authored prose, 0 hits.
- **RESIDUE, per Q-921:** a removed-class grep was run before sealing, using the pattern set member
  04 disclosed. **It caught NINE hits across EIGHT sites in my own first draft of this artifact** —
  narration naming two retired classes outright, and repeated use of one banned stem in sentences
  about digests agreeing. One of the nine escaped my own narrower pattern and was caught only by
  member 04's: it carried a negating prefix in front of the banned stem, so a pattern anchored
  with a leading word boundary slid straight past it. I point at that form rather than set it down
  here, because relay 1002's lesson is that a report naming what it swept reintroduces it — which
  is how this very bullet earned one more hit on the pass before this one. All eight sites were
  reworded to point at the register entries by number instead. **That my set missed one member
  04's caught is the same lesson a third time and I am not going to dress it up.**
  This
  document has **no labelled historical subsection and asserts no retired class**, so the honest
  target is zero outright rather than zero-outside-an-exception. **The result is CLAIMED, not
  clean** — the gate settles on the opposite lane, whose pattern set is not authored by the hand
  that wrote this prose.

---

## 9. The certificate

Per Q-913 and Q-917: **the certificate is the digest table.** Members 01–09 above with their full
paths, the thirty span digests of §3, the two mask spans, and the regenerated remainder digest of §4.
There is nothing below it.

---

## 10. Final lines

```text
CLOSURE = declared-first (byte 0; closure end 2739; scan 0 hits)
MANIFEST = 15-REPLACEMENTS-SPANNED.  Each with a half-open span AND a SHA-256 on BOTH sides, in
     document order, in the raw sealed files' own coordinates.  Once published they ARE the
     definition: verification needs no diff algorithm and no knowledge of how they were chosen, only
     the three checks at §4.  Row 7's old digest and row 8's new digest are the V002 and V003
     generator stdout digests the opposite lane recorded by an unrelated route -- they fall out of
     this manifest rather than being placed in it.
MASK_RULE = STATED-AS-BYTES.  DELETE the decimal digit run following "CLOSURE_END_BYTE = ";
     D_old = [719,723) "3450", D_new = [805,809) "4684".  NOT a filler of equal width.  The digit run
     is four bytes wide either way, so all four readings of "blank" give the IDENTICAL 15-block
     structure and FOUR DIFFERENT DIGESTS -- all four displayed at section 2.  The convention was in
     the mask, invisible in the output, which is the disease Q-913 ruled on, one level further down,
     inside a repair written because of it.  DELETE is of record because it meets the opposite lane's
     independently computed value, not because I prefer it.
REMAINDER = 13934-BYTES e3c634bcb9f8396216c33070b154ade8ed6cc91f7b68b4c1f85764bae6bcfc62 (REGENERATED)
     -- byte-identical, in length and digest, to member 04's independent diagnostic.  Two lanes, two
     methods, the same bytes.  remainder_old == remainder_new held; member 06 refuses to print a
     figure otherwise, and two mutation controls confirmed the refusal precedes emission.
V003_CLAIM = SUPERSEDED.  12,755 / 857992a0... does not recompute and is not defended.  The 1,179-byte
     gap is equal bytes my REGION-shaped mask discarded -- it removed whole blocks instead of the
     exact replaced spans inside them.  MY ERROR, not a difference of method.  V003 stays sealed and
     unedited; supersession is append-only.  Its four repairs, warrant, 26 spans and span convention
     are untouched and remain confirmed.
CHAIN_INVOKED = true (fires on the DONE: 1015 is queued for this lane)
VERB_AUDIT_SELF = CLEAN
```

All findings CLAIMED until the opposite-lane check. **The step to press first is §3.1's span
derivation.** The manifest is falsifiable — that was the point — but falsifiable is not the same as
minimal or canonical. A different alignment could draw different block boundaries over the identical
two files, publish a different fifteen-or-so spans, and still tile correctly and still regenerate a
valid remainder; whether it would regenerate *this* remainder is the question, and I have not shown
that the remainder is invariant under the choice of alignment. **The cross-lane match at §4 is
suggestive and I am deliberately not treating it as settling this** — member 04 concatenated equal
blocks from its own diff rather than removing my published spans, so the agreement may be two runs of
the same family of algorithm rather than two independent routes. **A lane that re-derives the spans by
a genuinely different method — anchored on headings, say, rather than on line alignment — is the check
that would settle it.**
