CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
PREDECLARATION_REGION = EMPTY (closure opens at byte 0; the closure block is the first content)
PREDECLARATION_OUTPUT_SCAN = 0 hits (empty byte range -- no possible hit)
VERDICT_BEARING_SET = exactly the 29 content-addressed members below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
PATH_RULE = every member carries its FULL path from the alpha-program-archive root and is rehashed
  at that path at seal time (Q-913).
LANE = DARIO   ROLE_THIS_RELAY = B03 V003 -- THE DERIVATION, TWO LEGS, BOTH STOPPED HONESTLY.
SUPERSESSION = this artifact supersedes STAGE8_DESC_B03_DARIO_V002.md APPEND-ONLY.  V002 remains
  sealed, on the books and BYTE-UNTOUCHED (4ffe99b2e816…, 36,519 B, rehashed here).  Its
  computations are CARRIED.  Its OPEN status is RESOLVED IN ONE DIRECTION AND REAFFIRMED IN THE
  OTHER -- see section 1.  V001 also remains byte-untouched (581ec505…, 74,533 B, rehashed here).
DIGEST_RULE = every digest and offset COMPUTED by member 29 and quoted from its output.  Nothing is
  pinned from a description of bytes.
SPAN_CONVENTION = DECLARED.  Offsets are byte offsets into raw file bytes, half-open [a,b), no
  decoding and no newline normalisation.  Two shapes only:
    FIXED   a literal [a,b) carried from an upstream pin; the generator recomputes the span digest
            and a mismatch is a REFUSAL, never a correction.  13 of 26 spans are FIXED; 13/13 MATCH.
    ANCHOR  a byte interval fixed by a UNIQUE start anchor running through the last byte of a named
            end anchor.  A second occurrence of the start anchor is a REFUSAL.
GENERATOR_REFUSAL = member 29 emits NOTHING on an unreadable member (R1), a FIXED span whose digest
  does not match its upstream pin (R2), an absent or AMBIGUOUS start anchor (R3), or an absent end
  anchor (R4), per Q-920/Q-924.  R2 and R3 were both EXERCISED AND OBSERVED this relay -- see
  section 8.  One anchor was rewritten because the generator refused it as ambiguous.
SUBJECT_READ_RULE = member 20 read ONLY WITH member 18 (overlay V002) and member 19 (DoR-013), per
  Q-931/Q-935.  status(member 20) := RATIFIED_FAMILY_LEVEL_BY_DOR_013, no-member clause carried.
  Section 3.7 quotes a span of member 20 CONTAINING a stale status surface; carried whole, flagged,
  never trimmed.
PREMISE_MARK_CARRIED = DoR-008 is a governing input to BOTH legs.  Everything the record builds on
  the field/CTP presentation is TYPE-P | premises: DoR-008 (member 27 [1993,2227)).  This artifact
  carries that mark forward and discharges none of it.
ALL_RESULTS = CLAIMED until the opposite-lane check.
CLOSURE_END_BYTE = 00008325
```

| # | Closed member | SHA-256 | Role |
|---:|---|---|---|
| 01 | `relay_inbox/RELAY_PASTE_1034_L3_DERIVATION_DARIO_V001.md` | `6427ab4f9c883f89514a496d34fc4119322d0a807b60bb3617ceb1e0d5963e6a` | the assignment |
| 02 | `relay_inbox/RELAY_PASTE_1033_FRESH_SESSION_BOOTSTRAP_DARIO_V004.md` | `be4f715dfaace27c8f118bc758ae35bb4fe1b5279967b8583e352881e1eee108` | the bootstrap; the SYMBOLIC LINE |
| 03 | `workspace/STAGE8_DESC_B03_DARIO_V002.md` | `4ffe99b2e8160a53db03dea69f229c62992d28def6ab2e11c9487e10157fcbb4` | **V002, superseded append-only, byte-untouched** |
| 04 | `workspace/STAGE8_DESC_B03_V002_CHECK_CODEX2_V001.md` | `7dd48338955417722cbbe8a14e14b8183398177536e94fd665963aa9669c6e3a` | **the TWO-OBJECTS ruling of record** |
| 05 | `workspace/STAGE8_DESC_B03_DARIO_V001.md` | `581ec505441b88b8a4d33d875ddc2d1d29ef8291fd140c4901a07a5513ac2506` | V001, still byte-untouched |
| 06 | `workspace/STAGE8_DESC_DIAG_B_CODEX2_V001.md` | `ab23d7c09e844712f04e64b79beaefcadd3b14979d960407b24bbc5c2ad609b6` | arm B |
| 07 | `workspace/STAGE8_DESC_DIAG_B_CHECK_DARIO_V001.md` | `cf9b577fdefd8704ab10801eef85819b3f24a12257092b95830bb54434951229` | arm B cross-check |
| 08 | `workspace/STAGE8_DESC_DIAG_A_DARIO_V001.md` | `a5d699ae6dc1f634c180ef6053a751b019dce8994b5968f0d96cbd22ba0fae62` | arm A; **its member table is what corrects the check's K4 locus** |
| 09 | `workspace/STAGE8_RANK1_CTP_PRODUCER_ALGEBRA_Q52_SPEC_V001.md` | `e191d37917c933a537c20152ac5899ab3d0d027d1f865709f2e816cad40ba706` | **THE DEMAND: P0–P7, and the named obstruction** |
| 10 | `workspace/STAGE8_CTP_PHYS_INPUT_PACKAGE_U2_DOR008_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md` | `2b6291227b7ac5967796014c2ad217c9eb084b5bb6df23fed0a7bca464e8bfab` | v004's `rho_pre` clause at its span |
| 11 | `workspace/STAGE8_AXN_STATE_ALGEBRA_MAP_CODEX2_V001.md` | `a67ed4352e939bd92e886672b9dfdb848cfcaa453a3760f0daa83d6586d60782` | **the `A_C0` typing, `res_B`, and the K4 handoff** |
| 12 | `workspace/STAGE8_AXN_ENTRY_CANDIDATE_SURVEY_DARIO_V001.md` | `4440af4f8d4a75c7e4b026d4fd901e4e290676f928275897bb55ce803b4c03db` | the three `i_src` declarations and their codomain |
| 13 | `workspace/STAGE8_AXN_ENTRY_DECISION_INSTRUMENT_CODEX2_V002.md` | `af26ab0354420f64718942b9bdcc61a4e6826a885b7ac0440988a25d7f0c95e1` | **THE REQUIREMENT SPAN: joint `i_src` EMPTY** |
| 14 | `workspace/STAGE8_AXN_STAGE_RULE_CONSTRUCTION_CODEX2_V002.md` | `f450b0a356b249509fb59b897c4f6a14e6996ba7da5ea513e69112a89907eed9` | **`A_F = C*(Lambda)`; the `A_C0` limit** |
| 15 | `workspace/STAGE8_FIELD_CTP_CARRIER_AND_C0_JOIN_INSTANTIATION_ATTEMPT_V001.md` | `e916f15742805a9f79f9386133c3a9662201e6363f739bddc682fbebb402ba37` | **THE PRIOR LEG-1 ATTEMPT and its stop** |
| 16 | `workspace/STAGE8_OBJ0_EXACT_SIGNATURE_DOMAIN_CODOMAIN_SPEC_AND_BUILD_STOP_V001.md` | `f7fa3c0ff4f7a13bcb953fced2b3e073a472410a6bc115b66157a4dae715c3a0` | the port signatures; the P1 domain-predicate `TYPE-S` |
| 17 | `workspace/STAGE8_CROSSING_PRODUCER_POSE_AND_GLUING_VERDICT_EINSTEIN_V001.md` | `80702f142edf14f22f0a2721475456fd00a1e7b1892fb7c9c8a9a15bdb4c7200` | S05's source: the tensor product refused **by name** |
| 18 | `workspace/MEMBER12_HEADER_OVERLAY_RECORD_V002.md` | `e85f444cbbd32db7cd8a3f794faee38d189f4bd12bd8e8bbfb43d8463c23cd75` | the overlay of record; the read rule |
| 19 | `supervision/DECISION_OF_RECORD_013_GEN_OMEGA_RATIFIED_FAMILY_LEVEL_2026-08-02_V001.md` | `f2a7838d41b7b7df42ae92bc3d59399ee04bbec65cecadc8a43f6a36ac4756ec` | the ratification, by digest |
| 20 | `workspace/STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V003.md` | `1be5f6a7e40c34586f3b5ab78f9129de0b5d2041cb6695b0e549443ddd6c6ee0` | the forced `d_state`. READ ONLY, with 18 and 19 |
| 21 | `workspace/STAGE8_AXN_LIVE_FAMILIES_CODEX2_V001.md` | `35f581dee0683add232367f953ec7807e89bb5eac47e34f4ad5d781a87c95be0` | `P_src`'s carrier |
| 22 | `workspace/STAGE8_DESC_DEMAND_DARIO_V008.md` | `968aad4fb387f8887959bd3f40888233b08b96bcd42d9ac8281556470afa0d54` | the demand map, CLOSED at V008 |
| 23 | `workspace/STAGE8_DESC_AUDIT_CODEX2_V002.md` | `078d6d54a2590f1caed4cea0245508981bd98e07adcef7f5b5df62d8419f838d` | the supply map |
| 24 | `supervision/PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | state pin |
| 25 | `supervision/LOCKED_PROCESS.md` | `38149496a2b5d89d20b614d972bffef1867d7cde573b26d77dfb207ece3446fb` | process law |
| 26 | `supervision/DECLINE_REGISTER_V002.md` | `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | S01–S37 |
| 27 | `supervision/DECISION_OF_RECORD_008_FIELD_CTP_ADOPTION_RATIFIED_WITH_FALSIFIER_2026-08-01_V001.md` | `d51a6d5c5bb0020a081cfd2adfb545b9f5ed86ce660d3feacadc5ef68140fb19` | **DoR-008 — THE RATIFICATION THIS RELAY FOUND, AND THE REASON LEG 1'S ANSWER IS NOT THE OBVIOUS ONE** |
| 28 | `workspace/STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md` | `76916244bdbcac7c2a6d4afae40f35127540d1d9e4cfc86fb72318506671161f` | the seven adoptions DoR-008 ratifies |
| 29 | `workspace/build_b03_v003_pins_v001.py` | `53feba2a4e600f4a10fe592fc9c0e2d111d1f6e035cd6edafaca9ca66b85e6bf` | the pin generator; declared inputs are exactly members 01–29 |

```text
BLIND HELD.  EVERY SCALE SYMBOLIC.  NO NUMERIC EVALUATION OF ANY PHYSICAL QUANTITY.  NO COMPARISON
TO A MEASURED CONSTANT.  NO MEMBER BOUND.  NO FIXED POINT EXECUTED (d_state's fixed-point
CHARACTERIZATION is cited, never run).  NO END TEST.  NO FREEZE.  NOTHING CHOSEN, ADOPTED,
IDENTIFIED, OR REGISTERED.  NO CARRIER IDENTIFICATION AUTHORED.  NO SUBAGENT DELEGATION.
```

CLOSURE_DECLARATION_END

# STAGE 8 — DESCENT SECTION — B03 — DARIO LANE — V003
## RELAY 1034 — `[PLAN:DESC-26]` — THE DERIVATION: TWO OBJECTS, TWO HONEST STOPS

Date: 2026-08-11
Status: **BOTH LEGS STOP, AND THE TWO STOPS ARE NOT THE SAME STOP — that is the result. LEG 1 is
not the absence the section expected. The record DOES supply a pre-algebra, a completion and a
common domain: DoR-008 ratified all of them on 2026-08-01, and `C0_prop` is AVAILABLE FOR USE. What
it does not supply is CANONICITY. The completion is SEVEN RATIFIED ADOPTIONS with alternatives
displayed, marked `TYPE-P | premises: DoR-008` and held under a standing falsifier; the record's own
slot for a theorem that would FORCE the presentation reads `NO_VERDICT`. So the completion exists
and is not forced, and what it completes to is `A_C0` — the object the record declines to identify
with `A_SRF_CTP`. LEG 2 then fails for a reason of its own, and this is the sharper half: the
required transport is NOT ENTAILED BY THE TWO TYPINGS, and it fails BEFORE it fails on Leg 1. An
arrow out of `A_C0` needs an arrow out of each of its three factors. The record types two of them
into `A_SRF_CTP` (`i_src` sealed, `i_rec` only as a proposed port signature) and types NOTHING out
of the third — `A_F_CTP`, the field/CTP factor. Nowhere in P0–P7, in any port signature, or in any
sealed span does an arrow declare that domain and that codomain. Even granting a completed
`A_SRF_CTP` satisfying every one of P0–P7, the transport still does not follow. THE TWO NAMES ARE
NOT TWO HALVES OF ONE ABSENCE: one is an unforced choice, the other is an unentailed arrow.**

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
JOINT_ANCHOR_DERIVED = false
```

---

## 1. What V003 carries, and what it resolves [PROVABLE]

V002 is superseded **append-only** and is byte-untouched at `4ffe99b2e816…`, 36,519 B, rehashed by
member 29 at seal time. V001 likewise remains at `581ec505…`, 74,533 B.

```text
CARRIED FROM V002, UNCHANGED
  the six-leg restatement of the demand from older receivers only (L1..L6), and its exclusion of
    the StatePort packaging and the "choose or derive" line as instrument-authored;
  L1 and L2 SATISFIED AT SOURCE-SECTOR SCOPE, and the refusal of the flattering two-of-six reading;
  L3 FAILS, L4 NOT SUPPLIED, L5 ABSENT, L6 PARTIAL;
  the exactness of res_B on its typed domain;
  V001's 38-row ledger, C34, C18/C19, and the four folded narrowings;
  the whole of V002's byte audit and its published span digests.

RESOLVED BY THIS RELAY
  V002's own press item -- "whether A_C0 and A_SRF_CTP are the same completed object" -- is
    RESOLVED AGAINST THE MERGE, and not by me: member 04 ruled TWO-OBJECTS and this relay
    re-verified its requirement span at bytes (F07).  V002 said that if they are not the same, its
    section 5.2 restriction argument "needs a transport it does not have."  IT DOES NOT HAVE ONE,
    and section 4 below shows the two typings do not give it one either.
  V002's second press item -- L4/L5 dispositioned quickly -- is NOT reopened here.  This relay was
    sent at L3's two objects and stays there.  Saying so is not a disposition.

REAFFIRMED
  V002's OPEN status stands.  Neither leg closed; nothing that was open is closed by this artifact.
  What changed is the SHAPE of the opening, and the shape is now two different shapes.
```

**I did not write this artifact to preserve V002's headline.** V002's most quotable sentence was
that `omega_phys` "is dissolved as a selector." That sentence was already corrected by member 04 and
this relay does not rehabilitate it: without the transport, the exact restriction does not reach the
L3 object, and the selector question is OPEN. Section 5 states that plainly rather than softening it.

---

## 2. Preflight: the requirement, re-verified rather than quoted from the check [PROVABLE]

Member 01 orders the requirement span to be taken **from the check and re-verified**. It was.

Member 13 `[10322,10545)` (FIXED), span SHA-256
`602ab0bff8d0d3d442271fe0850a6141f15fc1f139acb5b0311f13f63eaa26ff`:

```text
| joint `i_src` | **EMPTY** | member 05 §3.4; all three declarations land in `A_SRF_CTP`, while
member 09 declares `A_C0` | author the required carrier identification and typed embedding, or
author a new typed embedding |
```

Member 12 `[7028,7663)` (FIXED), span SHA-256
`43f3129a8b5059caa7979ab9ab0274296ec49c0cbd995c1785ab66d087af764d`, is the census behind it: the
three sealed `i_src` declarations all have codomain `A_SRF_CTP`, and it states in terms that
*"Pointing at any of the three sealed declarations requires deciding that `A_SRF_CTP` and `A_C0` are
the same carrier — an identification, not a transcription."*

**Two things follow immediately, and both bind this relay.**

1. The required act is typed **AUTHOR**, not **derive**. A builder lane may not author a carrier
   identification; that is a decision of record. This relay authors none.
2. Therefore the only lawful question left for Leg 2 is the one member 01 asks: is the embedding
   **entailed** by the two typings? Section 4 answers it, and the answer does not depend on my
   being permitted to author anything.

The demand legs themselves re-verify at their older receivers, unchanged from V002 and recomputed
here: P1 at member 09 `[8085,8283)` `375dd96a…` (F01), P5 at member 09 `[8954,9569)` `8917c67f…`
(F02), v004's clause at member 10 `[7290,7829)` `f9fb7a84…` (F03).

---

## 3. LEG 1 — THE COMPLETED CARRIER [PROVABLE]

### 3.1 What Leg 1 asks, stated before it is answered

Member 01: construct `A_SRF_CTP` from the pre-algebra the record supplies, the common dense domain
P1 names, and the completion — and decide whether the completion is **CANONICAL in what is sealed,
forced by the pre-object and its seminorm/state structure with nothing left open**, or whether it
requires data the record does not supply.

**The relay's phrasing presupposes that the record supplies a pre-algebra. It does — and finding
that out changed this leg's answer.** The hunt is recorded before the ruling, per RULING-LAST.

### 3.2 The hunt, and what it overturned in my own draft

My first reading was that the pre-algebra is absent. Member 15 says so in its own bytes, at
`[843,1152)` (ANCHOR) `a4910f51…` (A02):

> *"It does not fix the algebra generated by the compact connection, its generators and relations, a
> representation of that algebra, its join with the source-record algebra, or homomorphic
> forward/backward branch embeddings."*

and at `[11432,12082)` (ANCHOR) `13ebc11f…` (A03) it records **no generator set, no relation set, no
completion norm**, and at `[13204,13460)` (ANCHOR) `0ae3f21f…` (A04) that P1's common dense domain is
`ITEM_4_COMMON_DENSE_DOMAIN_INSTANTIATED = false | TYPE-U`.

**That reading is wrong as a statement about the present record, and I am recording the correction
rather than quietly adopting the second answer.** Member 15 is dated 2026-08-01 at register head
Q-202 and it says in its own lead that `ADOPTION_REQUIRED` is *"a present-stack construction status,
not a theorem."* **The adoption then happened.** Member 27 `[291,904)` (ANCHOR)
`95352c88…` (A09):

> *"The seven adoptions of `STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md`
> (`76916244...`) are RATIFIED as declared premises: sequential labels on Q-201's N <= M system with
> disclosed zero-extension . the C\* field algebra . forward/opposite-backward CTP tensor completion
> . the even spatial join to the Q-201 tuple . the Hilbert C\*-module representation . the common
> domain . branch embeddings . bounded finite-support source maps (with the four proved conditional
> consequences). Twice adversarially attacked; both found defects repaired by REMOVAL; second pass
> clean (Q-211). Honest count: SEVEN."*

So the pre-algebra, the completion **and** the common domain are all supplied. Member 28's own
build-bar at `[592,839)` (ANCHOR) `86f48544…` (A13) — *"No lane or relay may build on it unless a
later Decision of Record ratifies it"* — is **DISCHARGED by member 27**, which is exactly that later
decision. I flag this rather than leave it: the bar is not live, and reporting it as live would be
the cheap way to reach a stop.

### 3.3 What is actually built, at bytes

Member 14 `[4870,4999)` (ANCHOR) `c14a47f9…` (A07):

```text
Lambda = direct-sum_(j>=1) Z e_j,
A_F = C*(Lambda),
A_F_CTP = A_F,+ tensor_min (A_F,-)^op,
A_C0 = A_SR graded-tensor_min A_F_CTP.
```

and member 11 `[10436,11034)` (FIXED) `b9c7a355…` (F04) completes the typing: `A_SR := A_src
graded-tensor_min R_inf`, `B := A_F_CTP isomorphic to C(Y)`, with `i_R` and `i_B` the two canonical
factor inclusions.

**Read together, these are the completion Leg 1 was sent to build, and it is already built.** The
label lattice is completed to `A_F = C*(Lambda)`; the CTP doubling is completed by the
forward/opposite-backward minimal tensor; the join to the source-record tuple is the even spatial
tensor. Three of member 27's seven ratified adoptions are exactly these three completion steps.

### 3.4 The canonicity test — the actual question — fails

Leg 1 does not ask whether a completion exists. It asks whether it is **forced, with nothing left
open**. It is not, and the record says so in four independent ways:

1. **The adoptions are ratified AS PREMISES, not as derivations.** Member 27's own words are
   "RATIFIED as declared premises," and member 27 `[1993,2227)` (ANCHOR) `fc1a4e4a…` (A10) fixes the
   mark that propagates from them:

   ```text
   Everything built on this presentation is TYPE-P | premises: DoR-008, propagating downstream.
   NOT discharged: d_C0's common-origin provenance; DoR 007's discrete-to-continuum theorem.
   C0_prop is now AVAILABLE FOR USE under these marks.
   ```

2. **Alternatives are displayed beside the choices.** Member 07 §4 already ruled this at its own
   spans: the proposal's choice table *"displays seven proposed adoptions with alternatives,"* and
   **an adoption with displayed alternatives is a choice, not a derivation.** I execute that ruling;
   I do not re-adjudicate it.

3. **The record's own slot for the forcing theorem is empty and typed so.** Member 15
   `[16880,17121)` (ANCHOR) `dd01923b…` (A12):

   ```text
   future_derivation_can_select_the_field_CTP_presentation = NO_VERDICT
   reason: this attempt establishes the present construction debt; it does not
           prove that a future target-independent derivation cannot select the
           presentation
   ```

   `NO_VERDICT` is the exact status the canonicity question needs and does not have: the forcing
   theorem is neither supplied nor excluded.

4. **The ratification is conditional on a falsifier that is still live.** Member 27's standing
   falsifier requires the completed framework to reproduce every sealed finite result on
   restriction, and states that any disagreement *voids this decision and everything TYPE-P on it*.
   A completion that can be voided by a later restriction check is not a completion "with nothing
   left open."

```text
LEG 1 CANONICITY:  the pre-object does not force the completion.
  The seminorm structure is not derived from the pre-object -- the minimal C*-norm on each of the
  three completion steps is one of the SEVEN ADOPTIONS, displayed with alternatives.
  The state structure supplies nothing here: DoR-008's scope is a CARRIER interface and it carries
  no state at all (member 15 [16381,16559) e2f1c4d1..., A11: the adoption "cannot include state,
  dynamics, quotient, measure, effects, contacts, Ward data, inverse results, or U1 conventions
  without violating C0's narrow interface").
```

### 3.5 And what the completion completes to is not the object Leg 1 names

Even setting canonicity aside, the ratified completion delivers `C0_prop` / `A_C0`. Leg 1's object is
`A_SRF_CTP`. Member 04 ruled those **TWO OBJECTS**; member 13's requirement span (F07) says the
identification must be **authored**; and member 26's S05, whose source span is member 17
`[6905,8106)` (FIXED) `e7a873cd…` (F09), records the corpus refusing the tensor route to the
field/CTP extension by name:

> *"the tensor product of the source algebra with the record limit is rejected because the field/CTP
> component **is not an algebraic tensor factor**. A TENSOR PRODUCT IS CO-LOCATION, AND THE CORPUS
> DECLINED IT BEFORE THIS RELAY EXISTED."*

**S05 is read at its exact scope and not one word wider.** Its declined object is the SOURCE-ALGEBRA
/ RECORD-LIMIT tensor product — `A_SR`, the two-factor object. It is **not** a decline of `A_C0`,
which has the third factor S05 says is missing. Widening S05 into a decline of `A_C0` would be the
easy way to close this leg and it would be false. What S05 does establish is that the record has
refused to accept a tensor join as the *derivation* of the field/CTP extension — which is the same
distinction DoR-008 respects by ratifying the join as a **premise** and never as a derivation.

### 3.6 P1's own second datum, independently missing

P1 says *"a common dense domain **or equivalent domain object**."* DoR-008 ratifies "the common
domain," so the first branch is supplied. The second branch has no predicate. Member 16
`[35177,36199)` (ANCHOR) `333e16ad…` (A05) types it:

```text
P1_domain_equivalence_relation_found = false | TYPE-S |
  ...
  qualifying_definition_file_list: EMPTY
```

and member 16's own port text rules that the `PROVED_EQUIVALENT` branch *"cannot be frozen until its
exact relation and witness type exist."* This is a small datum next to the forcing theorem, and it is
named here because it is P1's and it is genuinely absent, not because it decides the leg.

### 3.7 The forced object, carried from V002 with its custody intact

Unchanged and re-verified: `d_state` is the unique normalized fixed state of `P_src` — member 20
`[22842,24541)` (FIXED) `84a5b750…` (F11) — and `P_src` is a channel on the authored finite scalar
**source** carrier, member 21 `[16571,16744)` (FIXED) `155721b5…` (F13). **The fixed-point
characterization is cited; no iteration is run.** That span CONTAINS overlay pin #7, member 20
`[22882,22958)` (FIXED) `65dfdedb…` (F12), a stale status surface reading
`PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL RATIFICATION (DoR-013 RESERVED)**`. **Stale, not
governing**: member 18's read rule and member 19 `[355,992)` (FIXED) `bc83e53d…` (F10) fix
`status(member 20) := RATIFIED_FAMILY_LEVEL_BY_DOR_013`. Quoted whole, flagged, never trimmed.

### 3.8 LEG 1 RESULT

```text
LEG 1 = MISSING-DATUM

DATUM 1 -- THE ONE THAT DECIDES THE LEG
  NAME   a forcing theorem for the field/CTP algebraic presentation: a target-independent
         derivation that SELECTS the seven adoptions from the pre-object and its structure,
         leaving no alternative displayed.
  TYPE   a theorem.  Its consequence would be to discharge the mark `TYPE-P | premises: DoR-008`
         that member 27 [1993,2227) propagates downstream, and to convert `A_C0`'s completion from
         ratified-premise to derived.
  LOCUS  the record already holds the slot open and empty: member 15 [16880,17121)
         `future_derivation_can_select_the_field_CTP_presentation = NO_VERDICT`.  A supplied theorem
         would live at member 28's seven choices and would be ratified by a successor to member 27.

DATUM 2 -- P1's OWN, SMALLER AND ALSO ABSENT
  NAME   the P1 domain-equivalence predicate, for the `equivalent domain object` branch.
  TYPE   an exact relation plus a witness type (member 16's `DomainEquivalence_1_witness`).
  LOCUS  member 16 [35177,36199); `qualifying_definition_file_list: EMPTY` across the six-file
         exactness packet.

NOT CLAIMED: that no completion exists.  One exists, is ratified, and is available for use --
  under DoR-008's marks and its standing falsifier, and it is `C0_prop`/`A_C0`, which the record
  declines to identify with `A_SRF_CTP`.
NOT CLAIMED: that the completion is wrong, or that the adoptions are bad.  They were twice
  adversarially attacked and passed.  UNFORCED IS NOT UNSOUND.
NOT CASCADE-TERRITORY: no step of this leg required a number.  Nothing was evaluated.
```

---

## 4. LEG 2 — THE TRANSPORT [PROVABLE]

### 4.1 The question, and why it does not inherit Leg 1's answer

Member 01 asks whether the required embedding is **entailed by the two typings** (the Q-940
entailment pattern — an embedding two typings force), **constructible from sealed grounds**, or
**genuinely absent**.

The lazy answer is "Leg 1 stopped, so Leg 2 cannot start." **That answer is available and I am not
taking it, because it is weaker than what the typings actually say.** The entailment question is
answerable on the typings alone, and it is answerable in the strongest form: *even granting a
completed `A_SRF_CTP` that satisfies every one of P0–P7*, the transport does not follow.

### 4.2 The direction, fixed first

The transport must be an algebra arrow

```text
phi : A_C0 -> A_SRF_CTP
```

in that direction, because states pull back contravariantly: `phi` induces
`phi^* : State(A_SRF_CTP) -> State(A_C0)`, and only then is

```text
res_B compose phi^* : State(A_SRF_CTP) -> State(B)
```

typed. That composite is precisely what K4's sealed handoff consumes — member 11 `[21194,21565)`
(FIXED) `e76be5c6…` (F08) computes `omega_hist = Omega_C0 compose i_B`, whose input is a state on
`A_C0`. `res_B` itself is exact on its typed domain, member 11 `[14039,14411)` (FIXED)
`438e92ae…` (F05); nothing in this section touches that.

### 4.3 What an arrow out of `A_C0` requires — stated as structure, every scale symbolic

`A_C0` is a graded minimal tensor product of three C\*-algebras (A07, F04):

```text
A_C0 = A_src  graded-tensor_min  R_inf  graded-tensor_min  A_F_CTP.
```

A \*-homomorphism out of such an object is not free data. It is exactly the data of:

```text
T1  three *-homomorphisms, one out of each factor, into the codomain:
       phi_src : A_src   -> A_SRF_CTP
       phi_rec : R_inf   -> A_SRF_CTP
       phi_F   : A_F_CTP -> A_SRF_CTP
T2  a GRADED-COMMUTATION certificate: the three ranges pairwise graded-commute in A_SRF_CTP.
       (The arrows out of a graded tensor product are exactly the graded-commuting families;
        this is the universal property being invoked, and it is invoked as structure, not
        as a numerical fact.)
T3  a MIN-CONTINUITY certificate: the induced map on the algebraic graded tensor product is
       bounded for the minimal C*-norm, so that it extends to the completion A_C0.
```

### 4.4 The census, at bytes: what the record types into `A_SRF_CTP`

An identifier-boundaried census over every corpus occurrence of `A_SRF_CTP`, run before this section
was written, returns exactly two arrow shapes with that codomain and no others:

```text
i_src : A_src -> A_SRF_CTP                 (and i_src : A_src[S_2] -> c1.A_SRF_CTP)
i_rec : RecordSector[S_3] -> c1.A_SRF_CTP
```

Measured against T1:

| requirement | what the record supplies | status |
|---|---|---|
| `phi_src : A_src -> A_SRF_CTP` | P2 types `i_src`, member 09 `[8085,8283)` context and member 12 `[7028,7663)` (F06): all three sealed declarations carry this codomain | **TYPED** (as a required component of an unbuilt package) |
| `phi_rec : R_inf -> A_SRF_CTP` | P3 types "a completed record embedding"; member 16 `[38867,39276)` (ANCHOR) `56a575d1…` (A06) gives `i_rec` **inside a PROPOSED PORT SIGNATURE** | **TYPED, AND ONLY PROPOSED** |
| `phi_F : A_F_CTP -> A_SRF_CTP` | — | **NOTHING** |

**The third row is the finding.** No sealed span, no port signature, no proposal, and no line of
P0–P7 declares any arrow whose domain is `A_F_CTP`, or `A_F`, or `C*(Lambda)`, and whose codomain is
`A_SRF_CTP`. P4 does require "branch embeddings" of the completed carrier, but P4's branch embeddings
are internal structure of the physical CTP package with no declared domain; the record's *instantiated*
branch embeddings `e_plus, e_minus` have codomain `A_C0`, not `A_SRF_CTP`, and they run the wrong way
for this purpose. `A_C0`'s field factor is reached by nothing.

And T2 fares no better. The **only** sealed commutation statement in this neighbourhood is member 11
`[10750,11207)` (ANCHOR) `bf0514d3…` (A08), and it is about `i_R` and `i_B` **inside `A_C0`**, with
its force limited in the same span:

> *"Their ranges commute. … The sealed C0 text immediately limits their force: this tensor relation
> is a kinematic commutation premise, **not** a state-factorization or dynamical-independence
> theorem."*

Nothing anywhere states a commutation — graded or ungraded — among ranges inside `A_SRF_CTP`. T3 is
likewise uncertified: no min-continuity, nuclearity, or faithful-representation certificate is
declared for any family of arrows into `A_SRF_CTP`. **I decline to supply T3 from general
mathematical facts about the factors' classes**: that would be importing a premise the record has not
sealed, and it would in any case leave T1 and T2 exactly where they are.

### 4.5 The entailment verdict, and why it is independent of Leg 1

```text
DO THE TWO TYPINGS ENTAIL phi?   NO.
```

The failure is located at **T1, third row**, and it is independent of Leg 1 for a reason that can be
stated exactly: **P0–P7 never mention `A_F_CTP`, `A_F`, `Lambda`, or `C*(Lambda)`.** The producer
signature and the `A_C0` construction share no vocabulary at the field factor. Therefore, for any
object whatsoever satisfying P0–P7 — including a canonically completed one, had Leg 1 closed — the
typings still license no arrow accepting `A_C0`'s third factor. **Leg 2's absence is not downstream
of Leg 1's; it is a second, independent absence, and this is the section's sharpest result.**

Three routes to `phi` exist in principle and each is barred here, for a different and stated reason:

```text
ROUTE 1  IDENTIFY A_C0 with A_SRF_CTP, then phi = id.
         BARRED: member 13 [10322,10545) types the required act as AUTHOR; member 04 ruled
         TWO-OBJECTS; a builder lane may not author a carrier identification.  NOT DONE.
ROUTE 2  DERIVE phi from the typings.
         FAILS at T1's third row, above.  This is the finding, not a stop.
ROUTE 3  AUTHOR a new typed embedding.
         BARRED by the same rule as route 1, and member 01 forbids choosing anything.  NOT DONE.
```

### 4.6 LEG 2 RESULT

```text
LEG 2 = MISSING-DATUM

DATUM
  NAME   the field-factor arrow: a *-homomorphism phi_F : A_F_CTP -> A_SRF_CTP, together with the
         graded-commutation certificate for the ranges of phi_src, phi_rec and phi_F inside
         A_SRF_CTP, and the min-continuity certificate that extends the algebraic map to the
         completion.  Three data, one leg; the first is primary because the other two are
         unstatable until it exists.
  TYPE   an algebra arrow plus two certificates.  Equivalently, and this is the record's own
         wording at member 13 [10322,10545): "the required carrier identification and typed
         embedding, or ... a new typed embedding."
  LOCUS  it would live at the producer's port list -- a port typed for the field/CTP factor, which
         P0-P7 do not currently contain -- and it would be entered by the decision instrument row
         that member 13 records as EMPTY.

NOT CLAIMED: that no such arrow can exist.  This is a statement about what the SEALED TYPINGS
  ENTAIL, and they entail nothing here.  A future construction may supply phi_F; the record's
  refusal is of a derivation, not of a possibility.
NOT CASCADE-TERRITORY: no step of this leg required a number.
```

---

## 5. THE 'THEN' SECTION — NOT REACHED [PROVABLE]

Member 01 conditions the downstream statement on **both legs standing**. Neither stands. The
downstream statement is therefore **not made**, and this section exists to say so and to record what
that costs, not to make the statement in weaker words.

```text
L3 pre-state existence route on the completed carrier      NOT STATED -- no completed carrier of the
                                                           demanded name; no transport to it
d_state's relation to it under the transport               NOT STATED -- there is no transport
common-origin certificate shape                            NOT STATED -- V002's "no object exists to
                                                           certify" stands unchanged
omega_hist as exact restriction, re-established            NOT RE-ESTABLISHED
K4's requirement                                           NOT MET
```

On the last two, precisely. `res_B` is exact on `State(A_C0)` (F05) and K4's handoff consumes
`omega_hist = Omega_C0 compose i_B` (F08) — a state on `A_C0`. So K4 would be met in shape by either
of two things: an actual `Omega_C0`, or the transport that would let an L3 state on `A_SRF_CTP` pull
back to one. **Section 4 shows the second is not entailed, and nothing in this relay supplies the
first.** Member 04's consequence therefore stands exactly as it ruled it: K4 requires an independent
`omega_hist` or a new transport, and `ZERO-CHOICE` stays refuted.

**The selector question is OPEN, and V002's "dissolved" is not rehabilitated here.** I record that
without softening because V002 is mine.

---

## 6. A CORRECTION TO THE CHECK OF RECORD — LOCUS ONLY [PROVABLE]

Member 04 §5 attributes the K4 span to arm A's own bytes:

> *"The sealed Arm A span `STAGE8_DESC_DIAG_A_DARIO_V001.md [21194,21565)`, SHA-256 `e76be5c6…`"*

**That span is not in member 08.** Verified exhaustively: no interval of member 08 hashes to
`e76be5c6…` at the declared length, at any offset, and no interval beginning at byte 21194 hashes to
it at any end within 3,000 bytes. Both the archive and cleanroom copies of member 08 are
byte-identical (`a5d699ae…`, 48,990 B), so this is not a copy divergence.

**The span is real and its digest is exact — at a different file.** Member 08's own member table
attributes it correctly: its row reads `member 12 [21194,21565) e76be5c6… K4: requires an ACTUAL
omega_hist`, and member 08's closure names its member 12 as
`workspace/STAGE8_AXN_STATE_ALGEBRA_MAP_CODEX2_V001.md` at `a67ed435…`. Recomputed there: member 11
of THIS closure, `[21194,21565)`, digest `e76be5c6f0536f2573c79f5d02a46e94f497cac5e87b744613ccf9c0636d011d`
— **MATCH** (F08).

```text
CORRECTION      LOCUS ONLY.  The cited file name is wrong; the span, the digest and the quoted
                content are all correct.  Member 04's ruling is UNAFFECTED: K4 does require an
                actual omega_hist, and that requirement is what refutes the zero-choice census.
CAUSE           member 04 read a citation IN member 08 and attributed it TO member 08.  The
                closure-local member numbering makes this easy: "member 12" means a different file
                in every closure that uses it.
DOWNSTREAM CONSUMERS, named per CORRECTION PROPAGATION
  1  member 04 §5 itself -- the K4 counterexample that refutes ZERO-CHOICE.  Ruling stands; the
     citation should read member 11 of this closure.
  2  this artifact, section 4.2 and section 5 -- both consume F08 and both cite it at the corrected
     locus.
  3  any future artifact quoting member 04 §5's locus rather than its content.
NOT DONE        member 04 is NOT edited.  It is byte-untouched at 7dd483389554….  A check of record
                is corrected by an append-only successor naming the defect, never in place.
```

**A second, smaller observation, recorded rather than ruled.** Member 04 §5 introduces the span as
"the sealed Arm A span" and reasons from it correctly throughout; nothing in its argument depends on
the file name. I am not treating this as a substantive defect and I am not inflating it into one.

---

## 7. FREEDOMS-CONSUMED

```text
JOINT_ANCHOR_INPUT   = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  V002's six-leg restatement and every leg disposition; V001's 38-row ledger, C34, C18/C19 and the
  four folded narrowings; member 04's TWO-OBJECTS ruling, its res_B exactness confirmation, its
  L4/L5 standings and its ZERO-CHOICE refutation; member 07 §4's ruling that an adoption with
  displayed alternatives is a choice; DoR-008's seven ratified adoptions, its TYPE-P mark and its
  standing falsifier; DoR-013's family-level ratification and no-member clause; member 18's read
  rule; S01-S37 including S05 at its exact scope; Q-194's narrow C0 interface; all charter fences.

DERIVED HERE:
  the location of DoR-008 as a governing input to this section, and the consequent correction of my
    own first reading that the pre-algebra is absent;
  the canonicity test for LEG 1 and its four-way negative -- premises not derivations, alternatives
    displayed, the forcing-theorem slot at NO_VERDICT, and a live voiding falsifier;
  the reading of S05 at its exact scope (A_SR, not A_C0), and the refusal to widen it;
  the T1/T2/T3 decomposition of what an arrow out of a graded minimal tensor product requires;
  the arrow census into A_SRF_CTP, and the finding that its third row is empty;
  THE INDEPENDENCE RESULT: P0-P7 never name A_F_CTP, A_F, Lambda or C*(Lambda), so LEG 2's
    entailment fails for ANY object satisfying P0-P7 -- it is not downstream of LEG 1;
  the K4 locus correction of section 6, with its downstream consumers named.

SELECTED HERE:
  nothing.  No carrier identification is authored.  No typed embedding is authored.  No presentation
  is adopted or re-adopted.  No state, member, measure, covariance-class member, selector, freeze,
  rank, candidate or preference is chosen, supplied, or approached.  No stop is lifted and none is
  defended.  DoR-008's premises are carried, never discharged.  Member 04's ruling is executed, not
  re-adjudicated.

SCALING WEIGHTS: none consumed, formed, fixed, compared, substituted, or evaluated.  Every scale
  symbolic.  The universal properties in section 4.3 are invoked as STRUCTURE; no norm was computed,
  estimated, bounded, or compared.
```

---

## 8. Flattening, custody, byte audit

- **S01–S37 FLATTENING CHECK — walked, clean.**
  - **A ratified premise was not flattened into a derivation** (§3.4) — this is the leg's whole
    finding, and the flattering error available here was to report "the completion exists" and stop.
  - **An absent construction was not flattened into an absent object, nor the reverse** (§3.2): my
    first reading was the former and it was wrong; the correction is recorded, not swapped in.
  - **S05 was not flattened from `A_SR` onto `A_C0`** (§3.5). The wider reading would have closed
    Leg 1 in one line and would have been false.
  - **A proposal's build-bar was not flattened into a live prohibition** (§3.2): member 27 is the
    later decision member 28's bar names, so the bar is discharged.
  - **A leg blocked by its predecessor was not flattened into a leg with no finding of its own**
    (§4.5) — Leg 2's absence is independent, and reporting it as consequential would have hidden
    that.
  - **An entailment failure was not flattened into an impossibility theorem** (§4.6).
  - **A locus error was not flattened into a substantive defect** (§6), and a check of record was
    not edited to repair it.
  - **A stale surface was not flattened into a governing status** (§3.7), and a ratified object was
    not trimmed to make a quotation tidy.
  - **Two absences were not flattened into one absence** — the headline result of this artifact is
    that they are different in kind.
- **BUILDER-NEVER-VERIFIES:** every result above is CLAIMED until the opposite-lane check. I did not
  re-adjudicate member 04's ruling, member 07 §4's choice-versus-derivation finding, DoR-008's
  adversarial passes, or arm B's provenance findings. I executed them.
- **BLIND HELD.** No physical quantity was formed, evaluated, or compared. No measured constant was
  approached. No member of the origin family was bound. `d_state`'s fixed-point characterization is
  cited at F11 and **no iteration was run**. `omega_phys` was neither derived nor chosen.
- **PE-1..PE-17:** pointer-only, zero verdict weight. The PE-17 display standard is the format of
  §3.8 and §4.6 (name, type, locus); it is used as a display rule and carries no verdict weight.
- **NO OUTPUT INSPECTION — CERTIFIED, and with its specific temptation named.** The temptation this
  relay carried was to identify `A_C0` with `A_SRF_CTP` because doing so would immediately satisfy
  K4, restore `res_B`'s reach, and close the section. That consequence was known to me and **did
  not enter the construction**: §3.5 and §4.5 are decided at the requirement span and the arrow
  census, and the K4 consequence is stated only in §5, after both legs had already stopped. No
  downstream object was opened for what it would need the answer to be; nothing was validated,
  adjusted, or selected by its downstream fitness; grounds first, at bytes.
- **CUSTODY:** archive-side only. Two files written under `workspace/`, both sealed, plus the outbox
  reports. Nothing in the cleanroom was written. **No register, plan, tracker, git, commit, push,
  chain execution, end test, or subject edit occurred. NO SUBAGENT DELEGATION.**
- **BYTE AUDIT:** all 29 members rehashed at full archive-root paths at seal time by member 29; all
  26 spans computed by it; **13 FIXED spans re-verify upstream pins, 13/13 MATCH.** V002 and V001
  both rehashed and both byte-untouched. Closure declared at byte 0 with its end computed on bytes
  as a fixed point under a fixed-width field; the predeclaration region is empty, so its scan has
  zero possible hits.
- **GENERATOR CUSTODY (Q-920/Q-924):** member 29's declared inputs are exactly members 01–29. Its
  four refusal paths are declared in its header. **Two were exercised and observed rather than
  asserted:** R2 refused a deliberately corrupted FIXED pin and emitted no table; R3 refused an
  ambiguous start anchor and emitted no table. **The R3 refusal was not a test — it happened.** The
  anchor for A05 was first written as `P1_domain_equivalence_relation_found = false`, which occurs
  twice in member 16; the generator refused it, and the anchor was rewritten to a unique start. The
  span was not pinned until the generator would emit it.
- **RESIDUE, per Q-921:** removed-class grep run over authored prose before sealing, fenced blocks
  excluded — scope declared, and a fence is any line whose first non-space characters are three
  backticks, so INDENTED fenced blocks are excluded too; getting that wrong moved my own count by
  two before it was fixed. Five over-generating families, case-insensitive: the `reproduce`
  family; the `reconstruct/rebuild/rerun/replay` family;
  `byte-identical`/`identical-bytes`/`same-bytes`/`verbatim`/`byte-untouched`; the
  `remove/delete/nothing-removed` family; and `set-delta`/`diff-triple`/`membership-movement`/
  `row-continuity`. **The scan was RUN, and its loci are read rather than predicted — a draft of
  this bullet named a `removed` occurrence in §3.2 that the scan does not find, and that claim is
  withdrawn here rather than left standing.**

  ```text
  RESIDUE = 18 RAW / 0 OPERATIVE
    11  this bullet's own naming of the classes it counts        META-LABEL
     7  content loci, all outside this bullet:
        5  byte-stability claims, each with its digest displayed beside it -- member-table rows
           03 and 05, section 1, section 6, and the byte-audit bullet above
        1  "repaired by REMOVAL", inside section 3.2's quotation of member 27's own bytes
        1  "reproduce", in section 3.4's statement of DoR-008's standing falsifier
  ```

  The eleven meta-label hits are counted, not exempted — that is exactly the distinction V002's fourth
  narrowing was ordered to fix, and I apply it to myself. **No locus asserts artifact
  reconstruction, a historical rerun certificate, deletion carriage, or membership movement.** The
  one `reproduce` hit outside this bullet is the record's own word about a completed framework
  reproducing sealed finite results on restriction — the falsifier — not a claim that any build
  re-runs to identical bytes; this document makes no such claim. **CLAIMED, not clean**: the hand that wrote the
  prose ran the scan, and the gate settles opposite-lane.

---

## 9. The certificate

Per Q-913/Q-917/Q-921/Q-930: **the certificate is the digest table.** Members 01–29 at their full
archive-root paths, and the twenty-six span digests quoted in place with computed offsets and
declared shapes — spans published WITH digests on both sides. Every FIXED span carries the upstream
pin it re-verifies. **There is nothing below the digests.**

---

## 10. Final lines

```text
CLOSURE = declared-first (byte position, scan)
     byte 0; closure end 8325 under a fixed-width field; predeclaration region EMPTY, so the
     27-token pre-closure scan has zero possible hits.

LEG1 = MISSING-DATUM (name, type, locus)
     NAME: a forcing theorem for the field/CTP algebraic presentation -- a target-independent
     derivation SELECTING the seven adoptions, leaving no alternative displayed.  TYPE: a theorem,
     whose consequence would be to discharge `TYPE-P | premises: DoR-008` (member 27 [1993,2227)
     fc1a4e4a...).  LOCUS: the record's own empty slot, member 15 [16880,17121) dd01923b...,
     `future_derivation_can_select_the_field_CTP_presentation = NO_VERDICT`.
     SECOND DATUM: P1's `equivalent domain object` predicate, member 16 [35177,36199) 333e16ad...,
     `qualifying_definition_file_list: EMPTY`.
     THE LEG'S REAL FINDING, and it is not the absence this section expected: THE RECORD DOES
     SUPPLY A PRE-ALGEBRA, A COMPLETION AND A COMMON DOMAIN.  DoR-008 (member 27 [291,904)
     95352c88...) ratified all of them on 2026-08-01 and `C0_prop` is AVAILABLE FOR USE.  WHAT IS
     MISSING IS CANONICITY, not construction: seven adoptions with alternatives displayed, ratified
     AS PREMISES, under a falsifier that VOIDS the decision and everything TYPE-P on it if the
     completion disagrees with any sealed finite result on restriction.  A completion that a later
     restriction check can void is not "forced with nothing left open."
     AND WHAT IT COMPLETES TO IS `A_C0`, which member 04 ruled is NOT `A_SRF_CTP`.
     S05 IS READ AT ITS EXACT SCOPE: it declines the SOURCE/RECORD two-factor tensor `A_SR`, not
     `A_C0`.  Widening it would have closed this leg in one line and would have been false.

LEG2 = MISSING-DATUM (name, type, locus)
     NAME: the field-factor arrow `phi_F : A_F_CTP -> A_SRF_CTP`, plus the graded-commutation
     certificate for the three ranges inside `A_SRF_CTP` and the min-continuity certificate
     extending the algebraic map to the completion.  TYPE: an algebra arrow and two certificates --
     the record's own wording at member 13 [10322,10545) 602ab0bf...: "the required carrier
     identification and typed embedding, or ... a new typed embedding".  LOCUS: a producer port
     typed for the field/CTP factor, which P0-P7 do not contain, entered at the decision-instrument
     row member 13 records as EMPTY.
     THE ENTAILMENT ANSWER, WHICH IS THE SHARP RESULT: **NOT ENTAILED, AND NOT BECAUSE OF LEG 1.**
     An arrow out of `A_C0 = A_src (x)_min R_inf (x)_min A_F_CTP` (member 14 [4870,4999) c14a47f9...;
     member 11 [10436,11034) b9c7a355...) requires an arrow out of EACH factor, a graded-commutation
     certificate, and a min-continuity certificate.  The census of every corpus occurrence of
     `A_SRF_CTP` returns exactly two arrow shapes into it -- `i_src` (sealed as a required component,
     member 12 [7028,7663) 43f3129a...) and `i_rec` (member 16 [38867,39276) 56a575d1..., inside a
     PROPOSED PORT SIGNATURE).  THE THIRD FACTOR IS REACHED BY NOTHING.  P0-P7 never name
     `A_F_CTP`, `A_F`, `Lambda` or `C*(Lambda)`; therefore FOR ANY OBJECT SATISFYING P0-P7 --
     including a canonically completed one -- the typings still license no arrow accepting `A_C0`'s
     field factor.  Leg 2 fails BEFORE Leg 1 would have mattered.
     T2 fares no better: the ONLY sealed commutation statement is member 11 [10750,11207)
     bf0514d3..., inside `A_C0`, and its own span limits it to "a kinematic commutation premise,
     not a state-factorization or dynamical-independence theorem."
     NOT an impossibility theorem.  This is what the SEALED TYPINGS ENTAIL, and they entail nothing
     here.  Routes 1 and 3 -- identify, or author a new embedding -- are AUTHORING acts barred to a
     builder lane, and none was performed.

L3_STATE = N/A
     Member 01 conditions the downstream statement on BOTH legs standing.  Neither stands.  Section
     5 states what is therefore NOT stated, rather than stating it in weaker words.

OMEGA_HIST = STILL-OPEN
     `res_B` is exact on `State(A_C0)` (member 11 [14039,14411) 438e92ae...) and K4's handoff
     consumes `omega_hist = Omega_C0 compose i_B` (member 11 [21194,21565) e76be5c6...), whose input
     is a state on `A_C0`.  Without the transport, an L3 state on `A_SRF_CTP` does not pull back to
     one.  V002's "dissolved as a selector" is NOT rehabilitated here, and V002 is mine.

K4 = NOT-MET
     Met in shape by either an actual `Omega_C0` or the transport.  Section 4 shows the second is
     not entailed; nothing here supplies the first.  Member 04's ZERO-CHOICE refutation stands.

OUTPUT_INSPECTION = NONE-CERTIFIED
     The temptation is named rather than merely denied: identifying `A_C0` with `A_SRF_CTP` would
     have satisfied K4, restored `res_B`'s reach, and closed the section.  That consequence was
     known and DID NOT ENTER THE CONSTRUCTION -- both legs are decided at the requirement span and
     the arrow census, and the K4 consequence appears only in section 5, after both had stopped.
     No downstream object was opened for what it would need the answer to be.  Nothing was shaped
     by its fitness.  Grounds first, at bytes.

CORRECTION = MEMBER 04 SECTION 5, LOCUS ONLY (propagated)
     The K4 span is cited as arm A's own bytes and is not in member 08 -- verified exhaustively at
     every offset and every end.  It belongs to member 08's OWN member 12, which is member 11 of
     this closure, where it re-verifies EXACTLY.  Member 04's ruling is unaffected and its bytes are
     untouched.  Downstream consumers named at section 6.

CHAIN_INVOKED = false
     The inbox holds no unstarted paste addressed to the DARIO lane behind 1034; 1030/1031/1032 are
     Codex 2's and are complete.

VERB_AUDIT_SELF = CLEAN
     "Derived" appears in the FREEDOMS block for work performed, in sealed status names, and inside
     quotations.  Nothing is called derived that is adopted: DoR-008's seven adoptions are called
     RATIFIED PREMISES throughout, which is what member 27 calls them.  No selector selected, no
     member bound, no carrier identified, no embedding authored, no stop lifted or defended.
```

All findings CLAIMED until the opposite-lane check.

**The step to press first is section 4.4's census, because it is the load-bearing new claim and it
is mine.** The census is a negative over the corpus, and a negative is only as wide as its surface.
Mine was identifier-boundaried on `A_SRF_CTP` and on arrow shapes ending in it; a declaration that
reaches `A_C0`'s field factor under a *different spelling of the codomain* — one of the five-plus
producer spellings Q-78's N5 records as never equated in a sealed sentence — would not appear in it.
**I looked for such a spelling and did not find one, and I am recording that as the residual rather
than as a finding**, because the honest statement is that the census is exact against a declared
surface and the surface is what a second pass should widen.

**The second thing to press is section 3.4's canonicity test.** That the adoptions are premises is
member 27's own word and that alternatives are displayed is member 07 §4's ruling; what is mine is
the inference that these two together mean the completion is **not forced by the pre-object**. A lane
could reasonably ask whether some subset of the seven is in fact forced — whether, for instance, the
minimal C\*-norm is the only one compatible with the rest of the sealed structure — and a positive
answer there would narrow this leg's missing datum without closing it.
