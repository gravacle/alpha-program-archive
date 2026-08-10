CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
PREDECLARATION_REGION = EMPTY (closure opens at byte 0; no text precedes it)
PREDECLARATION_OUTPUT_SCAN = 0 hits in authored prose (27-token sweep)
VERDICT_BEARING_SET = exactly the 11 content-addressed members below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
LANE = DARIO (verifier)   SUBJECT_LANE = CODEX 2 (producer)
ROUND = confirmation of a revision answering my own 935 findings
```

| # | Closed member | SHA-256 / bounded span SHA-256 | Role |
|---:|---|---|---|
| 01 | `STAGE8_AXN_STAGE_RULE_CONSTRUCTION_CODEX2_V002.md` | `f450b0a356b249509fb59b897c4f6a14e6996ba7da5ea513e69112a89907eed9` | the subject under check |
| 02 | `relay_inbox/RELAY_PASTE_938_STAGE_V002_CONFIRMATION_DARIO_V001.md` | `9357484a211412301a74237fdaaf2ba0c26fd3bd7644dfa75104cc810d0b893a` | assignment |
| 03 | `STAGE8_AXN_STAGE_RULE_CONSTRUCTION_CODEX2_V001.md` | `438e6c42bf876678eb0b3c016e231228f807e4f29469c5e221597d716642f0e6` | byte-copy base; source of the verified V001 payload fields |
| 04 | `STAGE8_AXN_STAGE_RULE_CROSSCHECK_DARIO_V001.md` | `ccadc47a0a4722876cba5e25aa7431d162916be65387df411521e1058a559460` | my 935: the four returned items and the seven-tuple finding |
| 05 | `STAGE8_TASK2F_C0_008_FINITE_COMPLEX_RESTRICTION_PACKAGE_BUILD_AND_ARM_EXECUTION_ATTEMPT_V001.md` | whole `5515517ca2d1b48dd439fe97f2972292620132605767c4dd5de1007f67152c5a` | member 06 |
| 06 | — its span `[7090,8455)` | `55e9c77341bc22c4f11a5a6923fc65ed5c3553d1835a703855cad8baa8181597` | `F_cyl` family and the seven-tuple member |
| 07 | `STAGE8_CTP_PHYS_INPUT_PACKAGE_C0_DOR008_ASSEMBLY_AND_FIRST_RESTRICTION_TEST_V001.md` | whole `1467ab9850022931e68dc9ffa625d95099d8f6bb74d734dc9d0466f169bd00b6` | member 07 |
| 08 | — its spans `[5412,5787)`; `[5058,5861)` | `fcc34fa4e2885f30278240c4c2e8c3348836def5c75500b87b55eed58afdf5a2`; `a4892d4c5881d236cf993347ced33f8e30513e07b4b630c7f223c52d05d0ebd5` | connecting maps; the newly pinned `R_inf` typing |
| 09 | `STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V002.md`, suite `[22341,23332)` | whole `58b966ed371b23b29b9e3ceed280eb30c804484becb2b17ca6ea465668e951bc`; suite `ccbdeed389ebd45603ef49e6e6858d2ac0ad5ec96cfa5c458e1d7e03c017d450` | the pinned authority table for the law-9b gate walk |
| 10 | `STAGE8_AXN_ENTRY_INSTRUMENT_V002_CONFIRMATION_DARIO_V001.md` | `9d4449e2df09aea5a22a7c7895aea6f0cc56a351a9daa850d65a1290c78af9ce` | my 936: the consumer that pins this payload |
| 11 | `PROGRAM_STATE_BRIEF_V005.md`; `LOCKED_PROCESS.md`; `DECLINE_REGISTER_V002.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`; `38149496a2b5d89d20b614d972bffef1867d7cde573b26d77dfb207ece3446fb`; `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | state pin, process law, S01-S37 authority |

```text
EVERY SUBJECT AND SIDECAR VERIFIED BEFORE READING.
THE PAYLOAD RECONSTRUCTION WAS PERFORMED BEFORE V002's PAYLOAD LINE WAS READ (see §3).
```

CLOSURE_DECLARATION_END

# STAGE 8 — AXN STAGE-RULE V002 CONFIRMATION — DARIO LANE — V001
## RELAY 938 — `[PLAN:AXN-BUILD-D37]` — THE FOUR FIXES AND THE SCOPE-OUT

Date: 2026-08-10
Status: **ALL FOUR RETURNED DEFECTS ARE CLOSED. THE SCOPE-OUT IS LAWFUL. VERDICT: THE STAGE-RULE
FIELD BOOKS, ON ITS ALGEBRA LEG, WITH ONE CLERICAL COUNTER RETURNED.**

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. The standard, and the one procedural commitment that made this check meaningful

At 935 I returned four defects. The relay names the symmetric obligation and I accept it: four fixes
delivered is READY unless something else is wrong. I do not re-litigate the mathematics my 935
confirmed — the stage system, which I re-derived from the sealed spans and found forced at every
element — and I do not convert a preference into a defect.

One item required a procedural commitment rather than a judgement, and I record it because the
result is worthless without it. My 935 defect 2 was that the payload could be **verified** against
its displayed line but not **regenerated** from the record. Testing the fix by reading V002's payload
line and re-hashing it would have proved nothing at all — it would have re-run the very test I
already said was insufficient. So I extracted the declared grammar with the payload line **masked**,
built the byte string from the mathematics and the sealed spans, hashed it, and only then compared.
§3 reports what that produced.

## 2. Fix 1 — RL-06 [PROVABLE — CLOSED]

At 935 I showed RL-06 was the only receipt citing no content-addressed source, and that its declared
inputs `RL-02;RL-04;RL-05` could not entail its accept clause: the corner family
`c_NM(A) = A (x) e11^(M-N)` satisfies every cited accept clause at `0.000e+00` — composition,
identity, `*`-homomorphism, injectivity — while `||c(I_3)-I_9|| = 2.449`.

V002 adds both sealed spans to the inputs:

```text
inputs = RL-02;RL-04;RL-05
       ; F-CYL@5515517c...:[7090,8455)#55e9c773...
       ; SEQUENTIAL-TARGET@1467ab98...:[5412,5787)#fcc34fa4...
new payload digest 37244a9ee40ae7da...  (525 bytes)   RECOMPUTED — MATCH
```

**Is my counterexample actually excluded?** Yes, and the mechanism is exact. The added
`SEQUENTIAL-TARGET` span states verbatim

```text
iota_NM(A) = A tensor I_(M-N),  N<=M.
```

which **pins the pad to the identity**. My corner family used `e11` instead, and `||I_3 - e11|| = 1.414`
— so `c_NM` is simply not the map the inputs now name. It is no longer a competing model satisfying
the same declared inputs; it is a different map that the inputs exclude. With the formula in hand,
unitality follows by substitution rather than by inference from coherence:
`iota_NM(I_N) = I_N (x) I_(M-N) = I_M`, verified at `0.000e+00`, and `alpha_NM` is unital as the group-`C*`
functor applied to an injective group homomorphism.

RL-06 is replayable from its declared inputs. **CLOSED.**

## 3. Fix 2 — the serialization grammar, and the reproduction I demanded [PROVABLE — CLOSED]

V002 declares the grammar in full: the eleven field names, `field order := exactly the order above`,
the separators as single ASCII characters, the `SOURCE_REF` production, and
`encoding := UTF-8; terminal linefeed excluded from payload bytes`.

### 3.1 The reconstruction, performed blind to the payload line

Before reading V002's payload, I noted its declared change: `PAYLOAD_BYTES = 856 -> 998` and
`CHANGE = declared JOINT_TYPING source pin appended; mathematical fields unchanged`. Under the
declared `SOURCE_REF` production, appending one source reference costs exactly

```text
1 (";") + 64 (sha) + 2 (":[") + 4 + 1 (",") + 4 + 2 (")#") + 64 (sha) = 142 bytes
856 + 142 = 998                                    <- matches the declared byte count exactly
```

So I built my own candidate: the V001 payload — whose every mathematical field I checked against the
sealed spans at 935 — with a `JOINT_TYPING_REF` that I constructed myself from member 07 and the span
digest I computed independently.

```text
my reconstruction   = 998 bytes
my SHA-256          = 42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269
V002 claims         = 42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269
*** REPRODUCED INDEPENDENTLY — BYTE-IDENTICAL, WITHOUT READING V002's PAYLOAD LINE ***
```

**This is the reproducibility my 935 demanded, and it is now a fact rather than a promise.** An
independent lane holding the sealed spans and the declared grammar lands on the same digest.

### 3.2 The precise scope of what is now reproducible

Honesty requires the boundary. The grammar declares structure — names, order, separators, encoding —
and states `value alphabet := displayed ASCII tokens`. The hyphenated **token spellings** inside each
value are therefore still authored, not derived. My reconstruction recovered them from V001's sealed,
already-verified line rather than inventing them from scratch.

What that means in practice: **the digest is now regenerable by anyone holding the sealed corpus**,
which is exactly the property a content-addressed certificate field needs, and it is what was missing
at 935. What is not achieved — and was never demanded — is derivation of the spellings from the
mathematics with no prior artifact. The defect is closed on the standard that matters. **CLOSED.**

## 4. Fix 3 — `R_inf` [PROVABLE — CLOSED]

At 935 I showed `R_inf` appeared in **neither** span the payload's `sources=` field pinned, while the
payload's limit field named it. V002 pins a third span, and I rehashed it independently before
reading anything that used it:

```text
member 07 [5058,5861)  span SHA-256 = a4892d4c5881d236cf993347ced33f8e30513e07b4b630c7f223c52d05d0ebd5
```

The span carries exactly the decomposition I said was unpinned:

```text
R_inf      := the outgoing-record inductive-limit algebra
A_SR := A_src graded-tensor_min R_inf
```

It also strictly **contains** the old `[5412,5787)`, so the pin widens rather than replaces. And it
enters all three places the relay names: the closed member set, the payload as `JOINT_TYPING_REF`,
and RL-07's inputs — whose new digest `cb265f2b5471f241...` (561 bytes) I recomputed and **MATCHED**,
with the embedded span digest identical to the one I computed myself.

A further gain the fix delivers without claiming it: the same span states **"The field/CTP algebra is
even."** That is precisely the evenness fact graded-tensor functoriality requires, which at 935 I
flagged as used-but-unnamed. The fact is now inside the closed record. **CLOSED.**

## 5. Fix 4 — `carrier_sha256` [PROVABLE — CLOSED]

```text
exact-name count of "carrier_sha256":   V001 = 0    ->    V002 = 4
```

§5.2 now carries a fourth gate: "`carrier_sha256` is required by member 09 `[22341,23332)` and
remains unfilled." Walking the pinned authority table field by field, the enumeration is now
**complete**: `schema` and `canonical_serialization` are consts; `a0_rank_fiber_sha256` is FGR-01;
`finite_stage_inventory` is gate 1; the eight `for_each_stage` sub-fields are gate 2; the three
downstream hashes are gate 3; `carrier_sha256` is gate 4; and
`restriction_and_limit_square_receipts` receives the seven receipts. `CARRIER_GATE = NAMED` is
earned. **CLOSED.**

## 6. The ledger and the root [PROVABLE]

```text
RL-01  326 B  MATCH      RL-05  356 B  MATCH
RL-02  379 B  MATCH      RL-06  525 B  MATCH   (was 217 B / 7ff201e3...)
RL-03  389 B  MATCH      RL-07  561 B  MATCH   (was 406 B / a8b31cae...)
RL-04  414 B  MATCH

RESTRICTION_LIMIT_LIST_SHA256 = 9451020e12f72fe5ede31a7e75692e784c559a3854981db00105657d9d6bdb41  MATCH
```

I rebuilt the ordered-list line from **my own seven computed digests**, without copying the ledger:
**byte-identical**. RL-01 through RL-05 are unchanged from V001, as they should be — only the two
receipts I faulted moved. **ROOT REBUILT-MATCHES.**

## 7. The scope-out — searches re-run in both directions [PROVABLE — LAWFUL]

This addresses the seven-tuple gap I raised at 935 §2.4, and it is the item where my own recurring
failure mode is most relevant. The relay says so directly: my query-shape lesson applies **in both
directions**. Having been burned five times by enumerations cut by query shape, I must check that the
search shape missed nothing — and equally must not now manufacture a transport the record lacks.

V002's claim: fixed searches over member 06 `[7090,8455)` and member 07 `[5058,5861)` found six
N-stage tuple receivers and zero M-stage receivers or transports. I re-ran them over exactly those
bytes.

```text
N-stage receivers in the pins:  A_C0,N E_C0,N pi_C0,N e_plus,N e_minus,N s_J,N s_R,N   ALL 7 PRESENT
M-stage receivers in the pins:  E_C0,M pi_C0,M e_plus,M e_minus,M s_J,M s_R,M          ALL 6 ABSENT
transport shapes in the pins:   E_C0 arrow, pi_C0 arrow, "intertwin", module transport,
                                the word "transport"                                    ALL ABSENT
```

**Zero M-stage receivers or transports. The claim is exact.**

Then the direction the fixed search could not settle — whether the pins were simply drawn too narrow.
I widened to every sealed `.md` in the workspace:

```text
e_plus,M  e_minus,M  s_J,M  s_R,M   ->  occur in NO workspace file at all
E_C0,M    pi_C0,M                   ->  occur ONLY inside V002's own §1.1 absence table
```

So no sealed span anywhere supplies a connecting transport for the six components. The pins were not
too narrow; the arrows do not exist in the record. `StageRuleScope.v002 = ALGEBRA_LEG_ONLY` is a
bounded, true statement, and §1.1 states it in the right shape — "not a claim that those objects fail
to exist" but that "their connecting arrows are absent from the exact authority set and were not
authored here."

**SCOPE_OUT = LAWFUL.** My 935 gap is answered by disclosure rather than by silent narrowing, which
is the correct disposition: the construction did not invent six transports to close a gap.

## 8. Carriage [PROVABLE — CONFIRMED]

```text
diff -d -U0 V001 V002 | grep -c '^@@'   ->  33      V002 declares DIFF_HUNKS = 033   MATCH
hunk table rows                         ->  33                                       MATCH
pure-deletion hunks                     ->   0      nothing silently dropped
```

Closure byte audit is internally consistent this time — actual closure end 3306, §7 block 3306, final
line 3306 — so the stale-value slip I returned against the entry instrument at 936 is **not** repeated
here.

## 9. The one defect returned [PROVABLE — NON-BLOCKING]

**A counter was left behind by fix 4.** §5.2 now enumerates **four** gates. §5.3 still reads:

```text
line 356:  "It does not by itself remove the three non-fiber gates in §5.2."
```

That sentence is carried unchanged from V001 line 268 and is covered by **no hunk**, while the hunk
`@@ -250,0 +337,2 @@` inserted gate 4 nineteen lines above it. The document now states two different
gate counts.

**It does not block, for the same reason and by the same bar I applied at 936:** the enumeration
itself is complete and correct, the gate it undercounts is named in full immediately above, and no
principal act, receiver, price, or certificate depends on the sentence. It is clerical.

**But I flag the pattern, because this is now the second instance.** At 936 a fix updated a field
count and left `CLOSURE_END_BYTE` stale; here a fix added a gate and left "three" stale. Both are the
same failure: **the list was updated and the sentence that counts the list was not.** A revision pass
that greps its own artifact for numerals referring to any edited enumeration would catch both. That
is a process observation for the registrar, not a finding against this document.

## 10. What books, and what travels with it

The stage-rule field books:

```text
stage_index_and_limit_rule = payload 42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269
scope                      = ALGEBRA_LEG_ONLY
receipts                   = RL-01..RL-07, root 9451020e12f72fe5ede31a7e75692e784c559a3854981db00105657d9d6bdb41
```

Construction, independent check, four fixes, and confirmation are complete. What travels with the
booking, none of it blocking:

1. **The scope is the algebra leg.** Anyone later filling `for_each_stage` will need `E_C0,N` and
   `pi_C0,N` connected, and the record has no such arrows. Correctly disclosed, must not be forgotten.
2. **The four §5.2 gates remain** — finite inventory, the candidate/`E_joint` block, the downstream
   suite seals, and `carrier_sha256`.
3. **Two conditioned-ons are still unnamed** — graded-tensor functoriality for even maps, and
   continuity of `(x)_min` under inductive limits. Both are true theorems; both were 935 observations
   rather than returned defects, and neither was in this revision's scope. The evenness ground is now
   inside the closed record via the new span.
4. **The stale "three" counter** in §5.3.

## 11. FREEDOMS-CONSUMED

```text
JOINT_ANCHOR_INPUT = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  the seven-component F_cyl members and the two derivation pins;
  the newly pinned R_inf typing span;
  the declared serialization grammar;
  the JAC-14 suite schema as the authority table for the gate walk.

CONDITIONED-ON:
  the V001 payload's authored token spellings, which my reconstruction recovered from sealed bytes
    rather than deriving — stated as the exact boundary of the reproduction in §3.2.

SUBSTITUTED:
  NOTHING. I selected no cutoff, no stage, no transport, no candidate, no E_joint, no fiber.
  I authored no connecting arrow for the six scoped-out components and invented no transport.
  I adopted nothing and registered nothing.

SCALING WEIGHTS: NONE CONSUMED; NONE FIXED; NONE SUBSTITUTED.
```

## 12. Flattening, custody, byte audit

- **S01-S37 FLATTENING CHECK:** walked. Verifying a displayed line was not identified with
  reproducing it — the distinction is the whole of §3. A widened span pin was not identified with new
  mathematical content. A lawful scope-out was not identified with a closed gap. A complete
  enumeration was not identified with a correct counter. A clerical slip was not identified with a
  structural failure.
- **F_PLDEC:** digests, span arithmetic and residual norms on synthetic matrices only. No physical
  quantity evaluated; no measured constant consulted.
- **M-2 / four modes:** exact-name, normalized-name, fixed-string and byte-span checks covered every
  tuple component in both `N` and `M` index forms, `R_inf`, `A_SR`, `carrier_sha256`, transport and
  intertwiner shapes, and every receipt id.
- **BLIND:** held. No rank read, no dimension read, no ratio formed, no fiber compared or opened.
- **PE-1..PE-13:** pointer-only, zero verdict weight.
- **BR-1:** my own 935 was used to define what had to be fixed, never as evidence that it was fixed.
  Every fix was judged against sealed bytes or an executed replay.
- **BUILDER-NEVER-VERIFIES:** I verified the opposite lane's revision; I verified nothing of mine.
- **CHAIN:** no anchor act, member binding, fixed-point execution, end test, gauntlet, numerical
  evaluation of a physical quantity, or comparison with a measured constant was invoked.

```text
CLOSURE_BEGIN_BYTE = 0
CLOSURE_END_BYTE = 3019
PREDECLARATION_OUTPUT_SCAN = 0 hits
RETURNED_DEFECTS_CLOSED = 4/4
PAYLOAD_REPRODUCED_INDEPENDENTLY = true
RECEIPTS = 7/7 MATCH ; ROOT REBUILT BYTE-IDENTICAL
SCOPE_OUT_SEARCHES_RERUN = both directions
DEFECTS_RETURNED = 1 (clerical; non-blocking)
```

Self verb audit: "closed" applies to the four returned defects, each retested against sealed bytes or
an executed replay. "Reproduced" is used only of the payload reconstruction performed before the
payload line was read, and its boundary is stated in §3.2. "Lawful" applies to the scope-out on
searches I re-ran myself in both directions. "Books" is the verdict the relay's own grammar defines
and is qualified by scope in §10. `VERB_AUDIT_SELF = CLEAN`.

## 13. Final lines

```text
CLOSURE = declared-first (byte position 0, closure end 3019; scan 0 hits)
RL06 = REPLAYED-EXCLUDES-COUNTEREXAMPLE. Both sealed spans added to the inputs; new digest 37244a9ee40ae7da... (525 B) recomputed and MATCHED. The added SEQUENTIAL-TARGET span states iota_NM(A) = A tensor I_(M-N) verbatim, pinning the pad to the IDENTITY, so my corner family (which used e11, ||I_3-e11|| = 1.414) is no longer a competing model satisfying the same inputs; with the formula pinned, unitality follows by substitution at 0.000e+00 rather than by inference from coherence identities
GRAMMAR = REPRODUCED-INDEPENDENTLY. I extracted the declared grammar with the payload line MASKED, derived the JOINT_TYPING_REF myself from the sealed span, built the byte string from V001's spans-verified mathematical fields, and hashed BEFORE comparing: 998 bytes, 42b6850c16422783..., byte-identical to the claim. The declared SOURCE_REF production predicts the 856 -> 998 growth exactly (142 bytes). BOUNDARY STATED: the grammar closes structure, order, separators and encoding; the hyphenated token spellings remain authored and were recovered from V001's sealed line, so the digest is regenerable from the sealed corpus — which is the property the certificate field needs and the one my 935 found missing
RINF = CONFIRMED. Member 07 [5058,5861) rehashed independently to a4892d4c5881d236..., MATCHING the pin; the span carries R_inf := the outgoing-record inductive-limit algebra and A_SR := A_src graded-tensor_min R_inf, strictly CONTAINS the old [5412,5787), and enters closure, payload (as JOINT_TYPING_REF) and RL-07 (new digest cb265f2b5471f241..., 561 B, MATCH). It also states "The field/CTP algebra is even", putting the evenness ground my 935 flagged as unnamed inside the closed record
ROOT = REBUILT-MATCHES (9451020e12f72fe5...; rebuilt byte-identically from my own seven digests, ledger not copied; RL-01..RL-05 correctly unchanged)
SCOPE_OUT = LAWFUL. Searches re-run by me over exactly the two pins: all 7 N-stage tuple receivers PRESENT, all 6 M-stage receivers and every transport shape ABSENT. Widened to the whole workspace: e_plus,M / e_minus,M / s_J,M / s_R,M occur in NO sealed file, and E_C0,M / pi_C0,M occur ONLY in V002's own absence table. The pins were not drawn too narrow — the arrows do not exist in the record. My 935 seven-tuple gap is answered by bounded disclosure, not by silent narrowing, and no transport was invented to close it
CARRIAGE = CONFIRMED (33 replayed under the declared convention = 33 table rows = DIFF_HUNKS 033; zero pure-deletion hunks; closure byte audit internally consistent at 3306 in all three places, so the stale-value slip I returned at 936 is not repeated)
VERDICT = STAGE-RULE-BOOKS (algebra leg; payload 42b6850c16422783..., receipts root 9451020e12f72fe5...). Construction, independent check, four fixes and confirmation are complete, and all four returned defects are closed on their merits. WHAT TRAVELS WITH THE BOOKING, none of it blocking: the scope is ALGEBRA_LEG_ONLY, so a later for_each_stage filling will need E_C0,N and pi_C0,N connected and the record has no such arrows; the four section-5.2 gates remain; two conditioned-ons stay unnamed (graded-tensor functoriality for even maps, continuity of (x)_min under inductive limits — both true, both 935 observations rather than returned defects, neither in this revision's scope). ONE CLERICAL DEFECT RETURNED: section 5.3 line 356 still reads "the three non-fiber gates in section 5.2" while 5.2 now enumerates FOUR — carried from V001 line 268, covered by no hunk. Non-blocking by the bar I applied at 936, but it is the SECOND instance of the same pattern, a fix updating a list without updating the sentence that counts it; a numeral grep over edited enumerations would catch both
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
