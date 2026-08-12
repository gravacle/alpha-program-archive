CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
CLOSURE_END_BYTE = 00013021
VERDICT_BEARING_SET = exactly the 9 content-addressed members below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
LIVE_MEMBERS = NONE
LANE = CODEX 2
ROLE = OPPOSITE-LANE DOCUMENTARY CHECK OF DESC SURFACE-FIRST V002 (relay 1056)
```

| # | Closed member | SHA-256 | Role |
|---:|---|---|---|
| 01 | `cleanroom/relay_inbox/RELAY_PASTE_1056_ACCOUNTING_CHECK_CODEX2_V001.md` | `74322e0849deb9f5336d9047a112e7a47737d37028e3ea6e193263b7906ff4b7` | assignment |
| 02 | `cleanroom/STAGE8_DESC_SURFACE_FIRST_DARIO_V002.md` | `801bc1683f08f1c7d4a94e49d8dc8685acf974c33c3a1ab1041182bdb7172f72` | documentary subject |
| 03 | `cleanroom/gen_stage8_desc_surface_first_dario_v002.py` | `21423c6645c040c4b42c6406a2cb2bb138013165ab476316c98129e6e828919c` | sealed manifest generator |
| 04 | `cleanroom/STAGE8_DESC_SURFACE_FIRST_DARIO_V001.md` | `953aa85b3aa7eac5f4763a8b26d85754270a114a38094a234ba33750af3608bd` | byte-untouched subject of the accounting |
| 05 | `cleanroom/STAGE8_DESC_SURFACE_FIRST_STEP12_PREFORM_DARIO_V001.md` | `73ef21bdbfef5fc9a3e602aedbf3a54e32a0274a4dd2fcc7214750b5b59ffe31` | fixed-text preform |
| 06 | `cleanroom/STAGE8_DESC_SURFACE_CHECK_CODEX2_V001.md` | `912c708e328a313cebe90314d7b893a87746b0a18084c35af5c2e44b612f54bd` | original opposite-lane finding and six-condition sweep |
| 07 | `cleanroom/STAGE8_TASK2D_FINITE_N_INFLUENCE_FUNCTIONAL_INSTANCE_CONSTRUCTION_RESULT_V001.md` | `c49d31200460e96209375f06a7a655d343767695ef09805f1e396d1814833b6b` | full three-entry cell action and projectors |
| 08 | `cleanroom/R3_4_CHARGED_INCIDENCE_OUTGOING_STATE_SPEC_V002.md` | `4a7600caa23d0c7a98eeef8a79941c20ca4e28a4f5a2c1cf5c2362e88c7d4721` | charge-projector source |
| 09 | `cleanroom/STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V003.md` | `1be5f6a7e40c34586f3b5ab78f9129de0b5d2041cb6695b0e549443ddd6c6ee0` | A0 and `kappa_ch` source |

```text
BLIND HELD. EVERY SCALE REMAINS SYMBOLIC.
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
JOINT_ANCHOR_DERIVED = false
NO MEMBER BOUND. NO PHYSICAL FIXED POINT EXECUTED. NO END TEST. NO FREEZE.
NO NUMERIC EVALUATION OF A PHYSICAL QUANTITY. NO MEASURED-CONSTANT COMPARISON.
PE-1..17 = POINTER-ONLY. omega_phys = UNTOUCHED.
ATTACH_CANDIDATE = NOT CONSUMED (separate relay 1055)
```

CLOSURE_DECLARATION_END

# STAGE 8 — DESC SURFACE-FIRST V002 OPPOSITE-LANE CHECK

Date: 2026-08-11  
Lane: Codex 2  
Status: CHECKED — CONFIRMS

## 1. Preflight and method

Members 02–06 rehashed to the assigned pins before semantic use, and the three source members 07–09
rehash to the values V002 cites. Member 02's declared-first closure ends at byte 3726 and its nine
members independently resolve and rehash `9/9`, with zero live members. Member 04 still hashes to
`953aa85b3aa7eac5f4763a8b26d85754270a114a38094a234ba33750af3608bd` after every read-only check.

The manifest was recomputed independently from members 04 and 05, without executing the generator's
write path. The generator's R3 route was then fire-tested safely by substituting an in-memory wrong
V001 expected digest. It returned `3` at the byte-untouched refusal before any write route.

## 2. Manifest reproduction

### 2.1 Regions

The generator's exact delimiter convention—start marker included, end marker excluded—reproduces:

| Region | Bytes | SHA-256 |
|---|---:|---|
| preform body, `## STEP 1 — THE BUILD` to before `END OF FIXED TEXT` | 13,259 | `08a589057f307e6af96a35807b916a29b1df39b4c25ec30f832409a922d0d85e` |
| V001 §§1–2, `## 1. STEP 1 — THE BUILD` to before `## 3. STEP 3 — THE EXHIBITION` | 15,976 | `c76748bfb04894f9a4204eb3c7dc6152eb7c3768a25b6faa08e777fe4ab06a69` |

Both equal member 02 `:43-49,92-117` and the constants in member 03.

### 2.2 Four substantive spans, both sides

All byte lengths and full span digests reproduce; the published table correctly displays their first
128 bits.

| ID | Preform exact span | Full SHA-256 | V001-region exact span | Full SHA-256 |
|---|---|---|---|---|
| C1 | L30–80, 3,200 B | `3fff9996bba00dd0b4e0ccd5aac88586a9b4ed41a60f0f02d67902f8c3d0c444` | L25–29, 483 B | `7484e8808144fc94dd1b7beb29d7cab0187fa9f24a231401f0384629fc285c00` |
| C2 | L83–84, 101 B | `aebda527cbfc9af1c5386bf914fbb5b5e0980b02ad973b69c734cd4bc1636b10` | L32–78, 2,724 B | `a3d3f74ba1d8a1c790b1deb31a51cd1b8ca12af2110bbb936f7db70aceeaa126` |
| C3 | L115–119, 374 B | `f7d145051d1458cacda4455038b93006abf736779f0d76a8b319b7f32b2015b2` | L113–138, 1,797 B | `ce376a3def863585c52cf000004144b4b7633f5f250d5567b969c723c6e3152d` |
| C4 | L198–200, 220 B | `b304f5f7e45b321fbdde66ee7b151cf00430bcdf31379d613b8edc3c5db42cf8` | L218–239, 1,460 B | `d20f2f3c8259a1806e0ed9f9f8739ef5d4b9417c30f748e8562f59c0754683d0` |

### 2.3 The 42/43 ruling

Using member 03's declared line sequence and `SequenceMatcher(..., autojunk=False)` produces exactly
42 non-equal opcodes. Those opcodes partition every changed line in the two fixed regions. The prior
check's 43 was a differently grouped line comparison over the same two pinned byte strings; it did
not identify a fifth content change. Thus this is `42 generated / 43 prior grouping`, same content,
not a missed group.

The four substantive spans map to the edge-entry provenance/relocation (C1/C2), projector plus A0
disclosure (C3), and marginal requalification (C4). Adversarial sampling of the remaining surface
found no fifth substantive change:

- the ready/write-hypothesis block merely merges identical premises and normalizes member citations;
- the added zero-response sentence restates the already present `U_N^0`/inert-`B` consequence with
  its sealed source;
- the common-origin block keeps the same SR-face/completed-object split while changing emphasis and
  citations;
- the expanded permissive display repeats the same continuum and at-least-four placement facts.

The other sampled groups are headings, Markdown reflow, punctuation, file-name-to-member citation
renaming, or repetitions of an unchanged claim at its new line position. The `38 PRESENTATIONAL / 4
SUBSTANTIVE` accounting therefore stands under the generator's grouping convention.

## 3. Claims accounting

### 3.1 Twelve preform claims

The twelve items at member 02 `:167-183` each occur in member 05's Steps 1–2: carrier; write
independence; invariant `omega_tr`; mating identity; `Omega_SR,N`; the `A_SR`/`A_C0` stop; the typed
Attach absence; sector split; dynamics; both marginal values; SR-face common origin; and the
permissive same-wall display. The load-bearing mating identity is present at member 05 `:83-125`, so
its content does not depend on a later V001 edit.

### 3.2 Four postform-touched claim units

The partition at member 02 `:189-203` is complete and correctly dispositioned:

| Unit | Manifest cause | Byte ruling | Disposition |
|---|---|---|---|
| edge-entry provenance | C1+C2 | member 07 `:145-158` supplies the whole `S`, including `S|e_Q>=-|e_Q>`; the value already existed in member 05 | STANDS; provenance improved |
| projector identity | C3 | member 08 `:31-36` defines `P_ch` from total charge and member 07 `:158` gives `P_0=I-P_ch` | NET-NEW; STANDS |
| A0 finiteness residual | C3 | member 09 `:347-386,896-906` calls the finite scalar source realization authored and carries its downstream price | NET-NEW DISCLOSURE; STANDS as a condition |
| unconditioned marginal forcing | C4 | member 05 `:198-202` is bare; member 04 `:348-367` adds TYPE-P premises, scope, and nonclaim | REQUALIFIED DOWNWARD; V001 form is honest |

The count is claims accounting, not a count of diff spans: C1/C2 jointly touch one provenance unit,
while C3 adds two distinct units. No V001 claim becomes ungroundable under these dispositions.

## 4. Withdrawals and the carried residue

### 4.1 `kappa_ch`

Member 02 `:221-240` withdraws the V001 different-route/independence claim and states the lawful
receiver relation: member 09 `:812-826` defines
`kappa_ch=Tr_A(rho_P P_ch)` and substitutes the same normalized identity that makes the record
marginal weight `Tr_A(P_ch)/Tr_A(I_src)`. It is one projector expectation exposed after two partial
traces. Every apparent survivor found by fixed-string search is inside the explicit withdrawal,
`IT IS NOT` block, or final withdrawal summary. There is no positive restatement of independence.

### 4.2 Localization headline and six conditions

Member 04 §3.2 rows 8–9, `:465-466`, already say that representation is not closed on the reached SR
face and that moving-front, tail, continuum-ordering, and connected-preparation conditions remain.
Those rows contradict V001's later one-factor/fail-once headline at `:479-489,513-517`. Member 02
`:263-271` withdraws that headline and preserves only the narrower truth: algebraic state-extension
freedom lies in `B`.

The six open conditions at member 02 `:242-260` match member 06 `:207-226,300` item for item:

1. authored A0 finiteness;
2. SR representation closure;
3. moving-front causal parent;
4. physical write/tail join and analyticity;
5. continuum ordering and connected preparation;
6. residual channel-family and character freedom.

No condition is dropped, merged away, or represented as discharged.

The withdrawal audit is complete.

## 5. Establishable / not-establishable display

The display at member 02 `:275-302` is honest.

The four `ESTABLISHABLE` entries reproduce from bytes: member 05 hashes to its pin; its Step-1/2 body
has zero occurrences of each of the nine field names; V001 differs under the declared convention by
42 groups; and the four substantive spans cite members 07/08 or the verb audit rather than the form.
The extended vocabulary check also reproduces: `SignatureFreezeInputs_0` occurs zero times, while
`PhysicalSig_0` occurs once in the preform file at header line 4 and zero times in its body.

The three `NOT ESTABLISHABLE` entries are exactly chronological assertions: authorship before the
form opened, priority of the exclusion list, and order of the four edits. No separately pinned
pre-reading receipt supplies them. Member 02 explicitly labels the §2.2 `WHEN` statements narration
at `:298-302`. Its §3 preform/postform partition is a comparison of content states keyed to C1–C4;
the only claimed session order remains the `WHEN` narration, not a byte-derived conclusion. No order
claim is used to rescue the quarantine.

The display audit is honest.

## 6. Generator, residue, and custody

The R3 fire test returned:

```text
REFUSED (R3): V001 MOVED: 953aa85b... != 00000000...
R3_FIRETEST_RETURN = 3
```

It stopped before closure mutation or sealing. A final rehash again returned member 04's assigned
digest.

Sixteen fresh output-inspection patterns were applied case-insensitively to member 02's authored
prose. They covered measurement-fit, observed-match, answer-shaped choice, tuning/optimization,
target-distance, experimental-agreement, scoring, data-comparison, and calibration constructions;
no literal was copied from member 03's token list. Result: zero hits. The generator's separate
27-token result is corroborating, not substituted for this scan.

The member-02 closure was independently parsed and all nine members rehashed `9/9`; zero live;
`STRICT==STABLE`. Structural byte lengths, group counts, span digests, and string-occurrence counts
were the only computed quantities in this check.

## 7. Flattening and freedoms consumed

Flattening check:

- alternate diff grouping was not flattened into missing content;
- a postform content difference was not flattened into a proved session chronology;
- a surviving conditional SR result was not flattened into repaired quarantine custody;
- one computation at two receivers was not flattened into independent derivations;
- state-extension freedom in `B` was not flattened into the whole unresolved load;
- a preform header assertion was not flattened into a receipt for its asserted order;
- a documentary confirmation was not flattened into a physical re-derivation.

```text
FREEDOMS-CONSUMED
  cited inputs: exactly the 9 closed members and only their declared roles
  derived here: region hashes; exact span hashes; 42-group opcode census; 42/43 ruling;
                12/4 accounting check; withdrawal sweep; display check; R3 refusal transcript
  not consumed: Attach candidate; member selection; physical fixed point; end test; numeric scale;
                measured target; PE content; freeze; omega_phys
  JOINT_ANCHOR_DERIVED = false
```

CLOSURE = declared-first (byte 0; end byte 00013021; 9 members; 9/9 strict-stable; fresh scan clean)
MANIFEST = REPRODUCED (42 generated / 43 prior grouping; same changed content, no missed group)
PARTITION = 12/4-CONFIRMED
WITHDRAWALS = COMPLETE
DISPLAY = HONEST
V001 = UNTOUCHED + R3-FIRE-TESTED
PROSE_DIGESTS = 9/9 STRICT==STABLE
RESIDUE_GREP = CLEAN (16 own patterns; 0 hits)
VERDICT = CONFIRMS
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
