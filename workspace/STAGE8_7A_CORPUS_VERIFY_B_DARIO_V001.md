# STAGE 8 / 7A / STEP 11 — CORPUS VERIFICATION, HALF B: THE CANDIDATES ARE NOT ARCHIVE-SIDE

Lane: DARIO (Builder B, independent verifier). Relay 766.
Under `DECISION_CORPUS_SELECTION_AUTHORITY_2026-08-08` `0dfc6e7b…`: this is half B; the
registrar seals only after both halves. Nothing adopted.

## Lead determination

**Neither candidate is readable archive-side, so the member-set verification the decision
commissions cannot be completed by this lane — and that is itself the relay's most useful
finding.**

Searched by name, by digest, and by directory across the whole archive (7,195 path entries):
`0a134859…` returns **nothing**; `*REGENERATED*` returns **nothing**; **no
`corpus_candidates/` directory exists anywhere**; `step11_tooling_family4/` does not exist
(family1 and family2 do). The original candidates `cfa8db99…` (1,805 B) and `722a7ea6…`
(1,080 B) are likewise absent.

**Half A could read them and cited byte spans inside them** — `[211,470)`, `[0,603)`,
`[0,1805)`. **I cannot.** So the decision's control — *"BOTH LANES independently verify
set-completeness … BEFORE any M2 query runs"* — is, for this lane and under ARCHIVE-SIDE ONLY,
**not executable as specified**. §4 states that as a process finding of record.

**What I could verify, I did, and it holds.** Three of the four half-A findings are resolvable
against archive-side evidence without reading the candidate, because they name external objects:

- **EXC-08-1 — CONFIRMED RESOLVED.** The lawful member is the packet copy
  `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` `aa7c6d49…`, and **both spans half A cited
  verify verbatim from bytes**: `[5505,5840)` names *"the V011 **general** finite-Hilbert
  premise"*, and `[37614,38217)` is the **Finite Pure-State Kinematics Premise** stating
  `ds_FS^2 = <d psi|d psi> − |<psi|d psi>|^2` in V011's own voice.
- **INC-08-1 — CONFIRMED RESOLVED.** The V002 all-token conjunction **passes** on the new
  member: `general` = 9, `FS` = 8 (3 × `FS` + 5 × `Fubini-Study`), `claim` = 21. The old
  member's failure was zero occurrences of `general`; the new member has nine.
- **INC-08-2 — CONFIRMED RESOLVABLE.** The claimed `S2_PACKET_MANIFEST` attachment is real: the
  member's digest appears in **two** sealed manifests — `STAGE7_PACKET_MANIFEST_V001.sha256` and
  `SOURCE_REFERENCE_MANIFEST_V001.sha256`.
- **EXC-08-2 — NOT VERIFIABLE.** The searched-roots census and the `EXCLUDED-UNSEALED` table
  live **inside** the candidate JSON. Unreachable.

**And an independent census corroborates the regeneration.** My own archive-side four-mode
conjunction sweep finds **130 matching files, 39 of them S1-sidecar-sealed** — against the
regen's reported `1 selected + 37 attached-but-nonclaim = 38` sealed matches. **39 ≈ 38** from a
different lane, a different glob, and a smaller universe. The regen's classification is not
under-inclusive by accident.

**One checkable prediction, offered because I cannot read the table myself.** `V009` itself —
the artifact the row is *named* for — satisfies the conjunction (`general` = 7, `Fubini-Study` =
6, `claim` = 6) and genuinely **uses** the claim (`Fubini-Study metric` at `[3102]`, `ds_FS` at
`[34144]`). It has **no S1 sidecar**, and its digest `b8168542…` appears in **no `.sha256` file
anywhere** — only in `BID_FULL_STACK_REVIEW_LEDGER_V002/V003`, which is a review ledger, not a
package or baseline inventory. **So V009 is UNSEALED under the rule's S1/S2/S3 test and must
appear in the candidate's `EXCLUDED-UNSEALED` table.** The registrar can confirm that in one
grep. If it is absent from that table, that is a finding.

---

## 0. Preflight

### 0.1 Output name

Probed **before any write**, recursively over the whole archive: **absent**, artifact and
sidecar both.

### 0.2 Sources verified before use

```text
AUTH   supervision/DECISION_CORPUS_SELECTION_AUTHORITY_2026-08-08.md   0dfc6e7b…  SEALED-OK
RULE   supervision/CORPUS_SELECTION_RULE_V001.md (with V002, V003)     653581bf…  SEALED-OK
HALFA  workspace/STAGE8_7A_CORPUS_VERIFY_A_CODEX2_V001.md              a9fee84e…  SEALED-OK
REGEN  workspace/STAGE8_7A_CORPUS_REGEN_CODEX2_V001.md                 682c94a3…  SEALED-OK
MEMBER workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/
         BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md                 aa7c6d49…  S2 (two manifests)
V009   workspace/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V009.md         b8168542…  **UNSEALED** (§3.2)
```

**ABSENT ARCHIVE-SIDE — the objects under verification:**

```text
step11_tooling_family4/generated/corpus_candidates/
  0a134859…--C-B-V009-08_general_FS_claim_REGENERATED.json   (85,115 B)   NOT PRESENT
  C-B-V009-08 original  cfa8db99…  (1,805 B)                              NOT PRESENT
  C-B-V009-01 candidate 722a7ea6…  (1,080 B)                              NOT PRESENT
searched: find by name '*0a134859*', '*REGENERATED*', '*C-B-V009*';
          find -type d 'corpus_candidates' and 'step11_tooling_family*'
          -> family1 and family2 exist; family3/family4 and corpus_candidates DO NOT.
```

**Searched space for every claim below:** the whole archive tree, **7,195 path entries** (all
file types, `.git` and memory-bank excluded), enumerated at run time. The rule's universe is the
**full program space** — the regen's own census records **16,107** path entries across the
program tree, `alpha_supervision`, and `_external_handoffs`. **My universe is the archive
portion only**, and every count below is scoped to it.

### 0.3 Gates

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
No member binding.  No fixed-point execution.  No end test.  No numeric evaluation of
physical quantities.  No comparison to measured constants.  Nothing adopted; no instance
sealed; no M2 query run.  No register, plan, tracker, or git action.
```

---

## 1. WHAT I COULD VERIFY, AND DID

### 1.1 EXC-08-1 — the lawful member and its two spans

[PROVABLE] Half A's finding: *"The actual sealed claim source is omitted: packet
`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md`, SHA-256 `aa7c6d49…`… calls out the exact
half-turn/`FS` budget and the V011 `general` finite-Hilbert premise at `[5505,5840)`, then
states the finite pure-state/Fubini-Study premise and local identity at `[37614,38217)`."*

[PROVABLE] **Both spans verified from bytes this relay.** `[5505,5840)`:

```text
| `PRIMITIVE_RECORD_ACTION_CHARACTER_BRIDGE_GATE_V002.md` | Gives a conditional
balanced two-path action bridge and its exact half-turn/FS budget; it is not
authority for the V011 general finite-Hilbert premise, physical amplitude,
alpha, or the full BID operator | `fc3e44f0…` |
```

and `[37614,38217)`:

```text
V011 retains the following **Finite Pure-State Kinematics Premise** only as a
standard kinematic input:
   For every finite Gate-3 Hilbert carrier, pure preparations are rays,
   transition probabilities obey the Born overlap, and infinitesimal ray
   separation is the Fubini-Study metric
   ds_FS^2 = <d psi|d psi> - |<psi|d psi>|^2.
```

[YOURS] **A precision worth recording, and half A got it right.** The first span is a
**mention** — a provenance row saying another artifact is *not* authority for the general
premise. The second is a **use** — V011 stating the premise in its own voice. Half A's own verbs
distinguish them (*"calls out"* vs *"states"*), so the mention-not-use discipline the relay asks
me to check is **already satisfied in half A's citation**, and the member's lawfulness rests on
the **use** at `[37614,38217)`.

### 1.2 INC-08-1 — the V002 conjunction, tested on the new member

[PROVABLE] `RULE` V002: *"a candidate member must match **EVERY** corpus-name token (each token
in any of its four-mode variants) — a conjunction, not a disjunction."* Corpus name
`C-B-V009-08_general_FS_claim`; tokens split on `-`/`_`: **`general`, `FS`, `claim`**.

[PROVABLE] Counted on `aa7c6d49…` this relay:

| Token | Four-mode variants found | Total |
|---|---|---|
| `general` | `general` × 9 | **9** |
| `FS` | `FS` × 3, `Fubini-Study` × 5 | **8** |
| `claim` | `claim` × 16, `CLAIM` × 2, `claims` × 1, `claimed` × 2 | **21** |

**The conjunction passes.** Half A's INC-08-1 was that the *old* member had **zero** occurrences
of `general`; the new member has nine. **Resolved, and by a member that satisfies the amendment
rather than by relaxing it.**

### 1.3 INC-08-2 — the seal attachment

[PROVABLE] `RULE` §1 requires the attachment mode be **recorded**, S1/S2/S3. The regen declares
`S2_PACKET_MANIFEST`. **Verified independently:** the member's digest
`aa7c6d4904706276…f81f108a` appears in `review_packets/STAGE7_QSPEC_CANDIDATE_V001/
STAGE7_PACKET_MANIFEST_V001.sha256` **and** in `review_packets/STAGE8_GATE5_AUTHORING_HANDOFF_V001/
SOURCE_REFERENCE_MANIFEST_V001.sha256`. **S2 is real, and doubly attested.**

[YOURS] What I cannot verify is that the *member record inside the JSON* carries the mode — that
was the exact defect (*"supplies only `{byte_length, relative_path, sha256}`"*), and it lives in
bytes I cannot read. **The attachment exists; whether it is recorded is unverifiable here.**

### 1.4 An independent census cross-check

[YOURS] I ran the four-mode all-token conjunction over the archive-side universe myself:

```text
archive-side path entries scanned      7,195
files satisfying the V002 conjunction    130
   of which S1-sidecar-sealed             39
```

against the regen's reported classification over its (larger) probe surface: **182 digests = 1
selected + 37 attached-but-nonclaim + 144 unsealed**, i.e. **38 sealed matches**.

**39 against 38**, from a different lane, a different glob, and a smaller universe. [YOURS] This
is corroboration, not proof — my sweep counts S1 only and cannot see S2/S3-attached files that
lack sidecars, and the universes differ. But it is the right order and it independently supports
the regen's central classification move: **most conjunction-matching sealed files are mentions,
not claim sources.** Spot-reading my 39 confirms the character — registers, inventories, memos,
relay pastes, and the corpus-verification artifacts themselves.

### 1.5 Self-citation — checked, and clean

[YOURS] The relay names self-citation as a wrong-inclusion mode. My sweep found that **`HALFA`
and `REGEN` themselves satisfy the conjunction** — so a naive probe would ingest the verification
artifacts into the corpus they verify. **The regenerated candidate has member count 1 and that
member is `aa7c6d49…`, so it does not self-include.** Clean on this mode, insofar as the declared
member count is accurate.

---

## 2. WHAT I COULD NOT VERIFY

| Item | Why |
|---|---|
| The candidate's member list beyond the one declared member | Candidate JSON absent |
| Whether the member record carries the S1/S2/S3 mode (INC-08-2's actual defect) | Inside the JSON |
| The searched-roots census, glob/exclusion record (**EXC-08-2**) | Inside the JSON |
| The `EXCLUDED-UNSEALED` table (**EXC-08-2**) | Inside the JSON |
| The sealed alias-table pin (**EXC-08-2**) | Inside the JSON |
| The declared root `af9d8c32…` rehashing to the member set | Inside the JSON |
| **C-B-V009-01 — anything at all** | Candidate absent; half A's CLEAN verdict is unreproducible here |
| Whether the regeneration introduced **new** members or fields | Requires diffing two absent files |

[YOURS] **The last row is the one that matters for the commission.** *"WITHOUT introducing new
ones"* is a difference between two objects, and I hold neither.

---

## 3. THE WRONG-EXCLUSION HUNT

### 3.1 Method

Four-mode object-names probe over the archive-side universe (§0.2), all-token conjunction per
V002, then seal-attachment classification per V001 §1. Glob stated; universe count printed;
`general`/`FS`/`claim` each expanded to fixed-string, case, hyphen/space/underscore and
alias variants (`Fubini-Study`, `Fubini Study`, `Fubini_Study`, `FubiniStudy`).

### 3.2 The one substantive candidate: V009 itself

[PROVABLE] `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V009.md`, `b8168542…`, 55,391 bytes:

```text
conjunction: general = 7 ; FS = 2 + Fubini-Study = 6 ; claim = 6      -> PASSES
USE markers : "Fubini-Study metric" at [3102] ; "ds_FS" at [34144]    -> a USE, not a mention
seal S1     : NO adjacent sidecar
seal S2/S3  : its digest appears in NO .sha256 file anywhere in the archive;
              it appears only in BID_FULL_STACK_REVIEW_LEDGER_V002/V003 —
              a REVIEW LEDGER, which is neither a packet manifest nor a
              "sealed package or baseline inventory" per RULE §1's S3.
```

[YOURS] **So V009 is UNSEALED under the rule's own test**, and `RULE` §1 is explicit about where
it then belongs: *"A file matching content but sealed no way is listed in the instance's
EXCLUDED-UNSEALED table — **visible, not silently dropped**."*

**PREDICTION, checkable by the registrar in one grep:** `b8168542…` **must appear in the
candidate's `EXCLUDED-UNSEALED` table**. It is the artifact the row is *named* for, it passes the
conjunction, and it uses the claim — so its absence from that table would be a silent drop of
exactly the kind §1's clause exists to prevent. **I cannot check it; you can.**

[YOURS] I record the alternative honestly: if the registrar's S3 reading admits a full-stack
review ledger as a "sealed inventory", then V009 is **S3-attached** and its exclusion from the
member set becomes a **wrong exclusion**, not a lawful unsealed entry. **The rule's S3 wording
does not settle which reading governs**, and that ambiguity is a finding in the rule, not in the
candidate.

### 3.3 The name-collision hazard, still live

[PROVABLE] The archive holds a **second, unsealed** `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md`
at `workspace/` top level, `20a3a17d…`, 84,987 bytes — which **also passes the conjunction**
(`claim` = 17 + 2 vs the packet copy's 16 + 2) and carries the same USE markers at **different
offsets** (`ds_FS` at `[37905]` in both copies here, but the files differ in length by 6,193
bytes and their spans are not interchangeable).

[YOURS] The candidate selected the **packet** copy, which is correct. But a content-matching
probe over the program space meets both, and the unsealed twin is precisely an
`EXCLUDED-UNSEALED` case. **Second prediction:** `20a3a17d…` should appear in that table too.
This is the hazard I recorded at 739 §0.2 and it is still live in the corpus machinery.

---

## 4. THE PROCESS FINDING — THE DUAL-VERIFY CONTROL HAS A CUSTODY ASYMMETRY

[PROVABLE] `AUTH` §3: *"**BOTH LANES** independently verify set-completeness (each lane hunts for
wrongly included AND wrongly excluded members) BEFORE any M2 query runs against the instance."*

[YOURS] **Half A executed that; half B cannot.** Half A cited byte spans *inside* the candidates
(`[211,470)`, `[0,603)`, `[0,1805)`), so the objects were in its reach. Under ARCHIVE-SIDE ONLY
they are not in mine, and no relay instruction lifts that.

[YOURS] **Why this matters beyond one relay.** The decision's rationale is that *"producer
selection is BR-1's shape"* and that dual verification supplies the catch a pure mechanism lacks.
**If only one lane can read the object, the catch is single-lane** — which is the condition the
control was designed to remove. The regeneration was performed by the same lane that verified
half A, so on this instance the producing lane and the only reading verifier coincide.

[YOURS] **The fix is small and is the registrar's:** mirror the candidate JSONs into
`workspace/mirrored_sources/` as was done for the D_BR primaries at 762. **One mirror makes half
B executable as designed.** I state the need; I do not reach for the files.

---

## 5. VERDICTS

```text
C-B-V009-08 (regenerated, 0a134859…)  =  NOT VERIFIABLE ARCHIVE-SIDE — PARTIAL.
   Three of four half-A findings CONFIRMED RESOLVED against external evidence
   (EXC-08-1's two spans verbatim; INC-08-1's conjunction now passing 9/8/21;
   INC-08-2's S2 attachment real and doubly attested).  EXC-08-2 UNREACHABLE.
   "Without introducing new ones" UNTESTABLE — it is a diff of two absent files.
   No defect found in anything I could reach.

C-B-V009-01 (722a7ea6…)  =  NOT VERIFIABLE ARCHIVE-SIDE.
   Candidate absent; half A's CLEAN verdict is unreproducible by this lane.
   No independent verification exists for this candidate.
```

[YOURS] **Neither verdict is CLEAN and neither is FINDINGS**, and I decline to force either
label. A CLEAN that means *"I found nothing in the part I could see"* would misreport a
single-lane verification as a dual one — which is the precise thing `AUTH` §3 was written to
prevent.

---

## 6. GROUNDING, JURISDICTION, VERB AUDIT

### 6.1 Grounding

| # | Claim | Basis | Tag |
|---|---|---|---|
| 1 | The candidates are absent archive-side | name/digest/dir search, 7,195 entries | PROVABLE |
| 2 | Half A cited spans inside the candidates | `a9fee84e…` | PROVABLE |
| 3 | EXC-08-1's two spans verify verbatim | `aa7c6d49…[5505,5840)`, `[37614,38217)` | PROVABLE |
| 4 | The V002 conjunction passes 9 / 8 / 21 on the member | counted this relay | PROVABLE |
| 5 | S2 attachment real, in two sealed manifests | `STAGE7_PACKET_MANIFEST_V001.sha256`; `SOURCE_REFERENCE_MANIFEST_V001.sha256` | PROVABLE |
| 6 | Archive-side census 130 matching / 39 S1-sealed vs regen's 38 | §1.4 | YOURS |
| 7 | V009 passes the conjunction and USES the claim | `b8168542…`, markers at `[3102]`, `[34144]` | PROVABLE |
| 8 | V009's digest appears in no `.sha256` anywhere | full-archive grep | PROVABLE |
| 9 | The S3 wording does not settle the review-ledger reading | `653581bf…` §1 | YOURS |
| 10 | The unsealed V011 twin also passes the conjunction | `20a3a17d…` | PROVABLE |
| 11 | The dual-verify asymmetry | `0dfc6e7b…` §3 vs §0.2 | YOURS |

**Pin check: 11/11.**

### 6.2 Jurisdiction check

**On returning NOT VERIFIABLE rather than CLEAN.** *What was the rule written to protect?*
`AUTH` §3 protects against a single lane's selection standing unchecked. Recording a partial
one-lane pass as CLEAN would defeat exactly that. *Does the outcome space distinguish false from
cannot-see?* Yes — §1 reports what I verified, §2 lists precisely what I could not and why, §3
delivers two checkable predictions. *Would the evidence appear if the theory is right?* Yes: one
mirror makes half B executable, and §4 names it.

**On ARCHIVE-SIDE ONLY.** I searched for the candidates by name, digest, and directory and did
not reach outside the archive for them. Where half A read the objects, I substituted verification
of the *external claims about* them, and labelled which is which.

**On BR-1.** The relay states C-B-V009-01 is *"unchanged, Codex-half CLEAN"*. That is a
producer-lane verdict; it may accuse but not exculpate, and I do not adopt it. §5 records that
this candidate has **no** independent verification.

**On the VOID CONDITION.** Nothing here is chosen from a desired outcome. The convenient result
would have been CLEAN on both, closing the dual-verify gate; §5 declines it.

### 6.3 Self verb audit — **CLEAN, with three disclosures**

1. **I could not perform the commissioned task and say so first**, rather than delivering the
   verifiable fraction under a verdict label that implies more.
2. **My census cross-check (§1.4) is corroboration, not proof**, and I mark it so: it counts S1
   only, over a smaller universe, and 39-vs-38 is the right order rather than a match.
3. **§3.2's V009 result depends on an ambiguity in the rule I cannot resolve** — whether a
   full-stack review ledger counts as S3. I display both readings and their different
   consequences (lawful unsealed entry vs wrong exclusion) instead of choosing the one that
   makes my prediction cleaner.

---

```text
CANDIDATES = 2 verified — TO THE EXTENT ARCHIVE-SIDE CUSTODY PERMITS, WHICH IS PARTIAL
   FOR ONE AND NIL FOR THE OTHER.  Both candidate JSONs are ABSENT archive-side:
   '0a134859' and '*REGENERATED*' return nothing, no corpus_candidates/ directory
   exists, and step11_tooling_family4/ does not exist (family1 and family2 do).
   Half A cited byte spans INSIDE the candidates; this lane cannot read them.
HALF_A_RESOLUTIONS = confirmed, three of four, against external evidence:
   EXC-08-1 CONFIRMED — the lawful member is the packet V011 aa7c6d49..., and BOTH
     cited spans verify verbatim: [5505,5840) names "the V011 general finite-Hilbert
     premise" (a MENTION, in a provenance row) and [37614,38217) STATES the Finite
     Pure-State Kinematics Premise with ds_FS^2 in V011's own voice (the USE on which
     membership rests).  Half A's own verbs already distinguished the two.
   INC-08-1 CONFIRMED — the V002 all-token conjunction PASSES on the new member:
     general = 9, FS = 8 (3 + 5 Fubini-Study), claim = 21.  The old member's defect was
     ZERO 'general'.  Resolved by satisfying the amendment, not by relaxing it.
   INC-08-2 CONFIRMED IN PART — the S2_PACKET_MANIFEST attachment is REAL and doubly
     attested (STAGE7_PACKET_MANIFEST_V001.sha256 and SOURCE_REFERENCE_MANIFEST_V001
     .sha256).  Whether the member RECORD carries the mode is inside the JSON: unreachable.
   EXC-08-2 NOT VERIFIABLE — census, globs, EXCLUDED-UNSEALED table and alias pin all
     live inside the candidate.  "WITHOUT introducing new ones" is UNTESTABLE: it is a
     diff of two files I do not hold.
FINDINGS = two checkable predictions and one rule ambiguity, none a defect I can confirm:
   (P1) V009 ITSELF — the artifact the row is NAMED for — passes the conjunction
     (7 / 2+6 / 6) and USES the claim ("Fubini-Study metric" [3102], "ds_FS" [34144]),
     has NO S1 sidecar, and its digest b8168542... appears in NO .sha256 file anywhere,
     only in a REVIEW LEDGER.  So it is UNSEALED under the rule and MUST appear in the
     EXCLUDED-UNSEALED table — "visible, not silently dropped".  Registrar-checkable in
     one grep; absence there would be a finding.
   (P2) The unsealed top-level V011 twin 20a3a17d... also passes the conjunction and is
     an EXCLUDED-UNSEALED case; the 739 name-collision hazard is still live.
   (A1) RULE section 1's S3 does not settle whether a full-stack REVIEW LEDGER is a
     "sealed package or baseline inventory".  On the permissive reading V009 is
     S3-attached and its exclusion becomes a WRONG EXCLUSION.  Ambiguity in the RULE,
     not in the candidate.
   Independent corroboration: my archive-side conjunction sweep found 130 matching files,
   39 S1-sealed, against the regen's 1 selected + 37 attached-but-nonclaim = 38.
   Self-citation checked and CLEAN: HALFA and REGEN both satisfy the conjunction, and
   the candidate does not self-include.
VERDICTS = C-B-V009-08: NOT VERIFIABLE ARCHIVE-SIDE (PARTIAL; no defect found in what I
   could reach).  C-B-V009-01: NOT VERIFIABLE ARCHIVE-SIDE (candidate absent; half A's
   CLEAN is unreproducible here and this candidate has NO independent verification).
   Neither is CLEAN and neither is FINDINGS; I decline both labels, because a CLEAN
   meaning "nothing in the part I could see" would report a single-lane verification as
   a dual one — the precise thing the authority decision was written to prevent.
   PROCESS FINDING: the dual-verify control has a CUSTODY ASYMMETRY.  On this instance
   the producing lane and the only reading verifier coincide.  The fix is one registrar
   mirror into workspace/mirrored_sources/, as was done for the D_BR primaries at 762.
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+3 disclosures at section 6.3)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
