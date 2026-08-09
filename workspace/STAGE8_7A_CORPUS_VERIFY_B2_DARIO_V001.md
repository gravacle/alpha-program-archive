# STAGE 8 / 7A / STEP 11 — HALF B COMPLETED: BOTH CANDIDATES CLEAN, WITH ONE RULE-LEVEL FINDING

Lane: DARIO (Builder B, independent verifier). Relay 772 (chained pickup after 770).
The registrar mirrored the member sets after my 766 custody finding; **half B is now executable
as the authority decision designed it**, and this artifact completes it.

## Lead determination

**Both candidates verify CLEAN, and my two 766 predictions both land.**

- **`MEMBERS = 133/133 byte-verified`**, plus 10/10 sidecars verifying against the files they
  name. No digest mismatch anywhere.
- **P1 CONFIRMED.** `V009` `b8168542…` — the artifact the row is *named* for — **is in
  `excluded_unsealed`**. Not silently dropped, exactly as `RULE` §1 requires.
- **P2 CONFIRMED.** The unsealed `V011` twin `20a3a17d…` **is also in `excluded_unsealed`**. The
  739 name-collision hazard is handled, not merely survived.
- **EXC-08-2 — the fourth half-A finding — RESOLVED.** The candidate carries
  `distinct_digests` (9,588), `attachment_counts`, `classification_counts`, `alias_tables`,
  `include_suffixes`, and all three exclusion tables. Every element half A reported missing is
  present.
- **A1, the rule ambiguity, is RESOLVED IN PRACTICE and remains open in the RULE.** The candidate
  reports `S3 = 0` and classifies `V009` as UNSEALED — so the registrar did **not** treat a
  full-stack review ledger as a sealed inventory. The permissive reading was declined; `V009`'s
  exclusion is lawful. **But `RULE` §1's wording still does not say so**, and §4.3 states what a
  one-line amendment would fix.

**The wrong-exclusion hunt, run with content in hand, finds nothing.** I tested all **37**
`EXCLUDED_ATTACHED_NONCLAIM` entries with a discriminator calibrated on the selected member — the
*defining* form of the claim (`Finite Pure-State Kinematics Premise`, `ds_FS^2 =`, *"infinitesimal
ray separation is the Fubini-Study"*). **Zero of 37 carry it; the selected member does.** The
mention/claim classification is correct.

**One finding, and it is at the rule level rather than the candidate's.** The corpus's own name
appears in two inconsistent forms — `corpus_id` reads `…:general-FS-corpus`, the candidate's
filename reads `…_general_FS_claim`. **Different trailing tokens.** The candidate probes on
`{FS, general}`; my 766 pass probed on `{general, FS, claim}`. The candidate's derivation is
lawful and is the conservative direction, but **V002's conjunction is defined on "corpus-name
tokens" and the corpus does not have one name.** That is a defect in the naming, not in the work.

---

## 0. Preflight

### 0.1 Output name

Probed **before any write**, recursively: **absent**, artifact and sidecar both.

### 0.2 Sources verified before use

```text
RULE   supervision/CORPUS_SELECTION_RULE_V001.md (+V002, V003)      653581bf…  SEALED-OK
AUTH   supervision/DECISION_CORPUS_SELECTION_AUTHORITY_2026-08-08.md 0dfc6e7b…  SEALED-OK
HALFA  workspace/STAGE8_7A_CORPUS_VERIFY_A_CODEX2_V001.md            a9fee84e…  SEALED-OK
REGEN  workspace/STAGE8_7A_CORPUS_REGEN_CODEX2_V001.md               682c94a3…  SEALED-OK
CAND8  …/corpus_members/0a134859…--C-B-V009-08_general_FS_claim_REGENERATED.json
                                                                     0a134859…  digest OK, 85,115 B
CAND1  …/corpus_members/722a7ea6…--C-B-V009-01_alias_registry.json    722a7ea6…  digest OK, 1,080 B
BX07   supervision/CORPUS_INSTANCE_BX07_ALIAS_REGISTRY_V001.json      5a14e376…  SEALED-OK
DEC01  supervision/DECISION_V009_01_CARRIER_PB_2026-08-08.md          1741cdb3…  SEALED-OK
MEMBER workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/
         BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md               aa7c6d49…  S2, two manifests
766    workspace/STAGE8_7A_CORPUS_VERIFY_B_DARIO_V001.md             a24ec458…
```

**Searched space:** `workspace/mirrored_sources/corpus_members/` — **227 files** enumerated at
run time; plus the archive tree for the content discriminator (`workspace/**`, `supervision/**`).

### 0.3 Gates

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
No member binding.  No fixed-point execution.  No end test.  No numeric evaluation of
physical quantities.  No comparison to measured constants.  Nothing adopted; NO INSTANCE
SEALED (that is the registrar's act); no M2 query run.  No register, plan, tracker, or
git action.
```

---

## 1. MEMBERS — BYTE-VERIFIED

```text
mirrored files                                     227
  genuine content-addressed members                133   ->  133/133 BYTE-VERIFIED OK
  sidecars (.seal.sha256)                           10   ->   10/10 verify against the
                                                                file each one names
  status/fixture files (not content-addressed)      84
digest mismatches                                    0
```

[YOURS] **An instrument artifact I caught by reading rather than reporting.** My first pass
counted **134** content-addressed names and reported **one mismatch**. The "mismatch" was
`…--general_FS_claim_sources.json.seal.sha256` — a **sidecar**, whose filename begins with the
digest of the file it *seals*, not its own. I had parsed every leading 64-hex string as a member
digest. **Corrected: sidecars excluded from the member count and verified separately.** The
corpus has no defect; my probe did.

---

## 2. C-B-V009-08 (REGENERATED) — WRONG INCLUSION AND WRONG EXCLUSION, WITH CONTENT

### 2.1 The single member — wrong-inclusion tests, all passed

| Test | Result |
|---|---|
| Byte-verified against declared digest | **OK** — `aa7c6d49…`, 78,794 B |
| V002 conjunction (`general`, `FS`) | **passes** — and also passes on `claim`, tested at 766 (9 / 8 / 21) |
| Seal attachment | **S2**, doubly attested (`STAGE7_PACKET_MANIFEST_V001.sha256`, `SOURCE_REFERENCE_MANIFEST_V001.sha256`) |
| Mention-not-use | **USE** — carries the defining form at `[37614,38217)`, verified verbatim at 766 |
| Self-citation | **clean** — `HALFA` and `REGEN` both satisfy the conjunction and both sit in `excluded_attached_nonclaim`, not in the member set |

**No wrong inclusion.**

### 2.2 The 37 `EXCLUDED_ATTACHED_NONCLAIM` — the wrong-exclusion surface, tested

[YOURS] These are the sealed files that matched the conjunction and were classified as mentions.
**They are where a wrong exclusion would hide.** I tested each by content with a discriminator
calibrated on the selected member:

```text
USE marker (the DEFINING form, as V011 states it):
   "Finite Pure-State Kinematics Premise"  |  "ds_FS^2 ="  |
   "infinitesimal ray separation is the Fubini-Study"

of the 37 excluded-attached-nonclaim files, carrying a defining-form USE:  0
control — the SELECTED member carries it:                                 TRUE
```

[YOURS] The 37 are registers, evaluator specs, tooling reports, envelopes, memos, relay pastes
and the corpus-verification artifacts themselves — every one a mention. **Reason recorded
uniformly as `PROCESS_OR_MENTION_NOT_CLAIM_SOURCE`, and the content agrees.** No wrong exclusion.

### 2.3 `excluded_token_miss` — half A's INC-08-1, now in the candidate's own table

[PROVABLE] Exactly **one** entry:

```text
step11_v009_08_graph/generated/premises/696c5475…--finite_pure_state_kinematics_premise.md
   byte_length 603 ; missing_tokens ["general"] ; reason TOKEN_CONJUNCTION_MISS
```

[YOURS] **That is the old member, the 603 bytes half A found to contain zero `general`** — and
the regeneration did not merely replace it, it **recorded its exclusion with the reason**. The
resolution is visible in the artifact rather than asserted about it.

### 2.4 The two 766 predictions — both CONFIRMED

| Prediction | Result |
|---|---|
| **P1** — `V009` `b8168542…` must appear in `EXCLUDED-UNSEALED` | **CONFIRMED**, present in `excluded_unsealed` |
| **P2** — the unsealed `V011` twin `20a3a17d…` likewise | **CONFIRMED**, present in `excluded_unsealed` |

[YOURS] Both were checkable in one grep, as I said, and both hold. **`RULE` §1's *"visible, not
silently dropped"* is satisfied for the two cases most at risk of a silent drop** — the artifact
the row is named for, and a same-named twin.

### 2.5 EXC-08-2 — the fourth half-A finding, RESOLVED

```text
search_record carries: distinct_digests = 9,588 ; attachment_counts {S1:37, S2:1, S3:0,
UNSEALED:144} ; classification_counts {SELECTED:1, EXCLUDED_ATTACHED_NONCLAIM:37,
EXCLUDED_UNSEALED:144} ; alias_tables ; include_suffixes ; and all three exclusion tables.
```

**All four half-A findings are now resolved**, three confirmed at 766 against external evidence
and the fourth here against the candidate's own bytes.

### 2.6 The finding: the corpus has two names

[PROVABLE] The candidate's `selection.tokens` is `["FS", "general"]`, derived from
`backticked_objects: ["general-FS"]` — lawful under `RULE` §2, which makes *"every backticked or
quoted object name in the row's M2 clause"* a source of probe terms.

[PROVABLE] But the two names disagree on their third token:

```text
corpus_id                 :  CD:C-B-V009-08:general-FS-corpus     ->  … "corpus"
candidate filename        :  …_general_FS_claim_REGENERATED.json  ->  … "claim"
```

[YOURS] **V002's conjunction is defined on "corpus-name tokens", and this corpus does not have a
single name.** My 766 pass used `{general, FS, claim}` from the filename; the candidate uses
`{FS, general}` from the backticked object. **Neither is wrong under the rule as written — which
is the problem.**

[YOURS] **Direction of risk, assessed rather than asserted:** the candidate's two-token probe is
**wider**, so it over-generates and then prunes by classification — the direction `RULE` §3
explicitly contemplates (*"deliberately over-generating"*). A three-token probe would have been
**narrower** and could have excluded a genuine claim source by token-miss. **The candidate chose
the safer direction**, and my 766 run — the narrower one — still had the member passing. **No
member is affected either way.** I record this as a naming defect for the registrar, not as a
defect in the candidate.

---

## 3. C-B-V009-01 — THE REGISTRY

### 3.1 Typing, against `RULE` V003's four elements

[PROVABLE] `CAND1` `722a7ea6…`, digest verified, 1,080 bytes:

| V003 element | Candidate | Verdict |
|---|---|---|
| Type is REGISTRY (accrues by decision, not found) | `"type": "REGISTRY"` | ✓ |
| Lawful instantiation is the CURRENT REGISTRY STATE, empty if nothing licensed | `"current_registry_state": "EMPTY"`, `candidate_members: []` | ✓ |
| Accrual authority declared | *"the principal licenses an alias/trivialization/unit-representative entry by decision of record; the registrar seals each accrual … no producer may enter a member"* | ✓ |
| A claim-sweep is wrong-typed | `"claim_sweep_allowed": false` | ✓ |

### 3.2 The wrong-exclusion test for a registry, and it passes

[YOURS] For a REGISTRY, wrong exclusion means: **something was licensed by decision and is
missing.** The state basis names its authority, and I verified it:

[PROVABLE] `DEC01` `1741cdb3…`, **SEALED-OK**: *"**NO BASIS OR TRIVIALIZATION IS LICENSED** by
this ruling — any future unit representative or scalar trivialization must be **separately
licensed and entered in the alias corpus**; nothing is inferred from dimension one."*

**Nothing has been licensed; therefore EMPTY is correct and nothing is wrongly excluded.**
Wrong *inclusion* is vacuous on an empty set.

[YOURS] `BX07` also retains *"the wrong-typed claim-sweep (267 mention-candidates) … cited as the
V003 incident"* as a **negative control**. That is the right disposition: the failed sweep is kept
as evidence rather than deleted.

### 3.3 One flag, already self-declared

[PROVABLE] `CAND1` uses schema `rd22.step11.corpus-candidate.**v001**` while `CAND8` uses
`**v002**`, and `CAND1`'s own status reads
`CANDIDATE_EMPTY_REGISTRY_AWAITING_REGISTRAR_SCHEMA_RECONCILIATION_AND_DUAL_VERIFY`. **The
divergence is declared by the candidate itself**, so it is a pending registrar act, not a finding
against the work. I note it because the dual-verify gate should not close over an unreconciled
schema without the registrar saying so.

---

## 4. VERDICTS AND THE CLOSED PROCESS FINDING

### 4.1 Verdicts

```text
C-B-V009-08 (regenerated, 0a134859…)  =  CLEAN.
   133/133 members byte-verified; the single member is a genuine S2-attached USE;
   no wrong inclusion; no wrong exclusion among the 37 nonclaim entries (0/37 carry
   the defining form, control fires on the selected member); all four half-A findings
   resolved; both 766 predictions confirmed.

C-B-V009-01 (722a7ea6…)  =  CLEAN.
   REGISTRY typing correct on all four V003 elements; EMPTY with a SEALED decision
   basis that licenses nothing; wrong inclusion vacuous, wrong exclusion tested and
   passed; schema-version divergence self-declared and pending the registrar.
```

### 4.2 The 766 process finding, closed

[YOURS] 766 reported that `AUTH` §3's dual-verify control was **not executable** by this lane —
half A could read the candidates and I could not, so the producing lane and the only reading
verifier coincided. **The registrar mirrored the members; the control is now executable and has
been executed.** I record the closure because a process finding that is acted on should be seen
to close, not merely lapse.

### 4.3 The rule-level finding, for the registrar

```text
FINDING (rule, not candidate):  The corpus has two names — corpus_id
"…:general-FS-corpus" and filename "…_general_FS_claim" — differing in the third
token.  V002's conjunction is defined on "corpus-name tokens".  Two lawful token
sets follow, and they differ.  A one-line amendment naming WHICH string is the
corpus name would close it.

RESOLVED IN PRACTICE, OPEN IN THE RULE (A1 from 766):  the candidate reports S3 = 0
and classifies V009 (whose digest appears only in a full-stack REVIEW LEDGER) as
UNSEALED.  So the permissive S3 reading was declined in practice.  RULE §1's S3
wording — "named with digest in a sealed package or baseline inventory" — still does
not say whether a review ledger qualifies.  Same fix: one line.
```

---

## 5. GROUNDING, JURISDICTION, VERB AUDIT

### 5.1 Grounding

| # | Claim | Basis | Tag |
|---|---|---|---|
| 1 | 133/133 members byte-verified; 10/10 sidecars | recomputed this relay | PROVABLE |
| 2 | P1: `V009` in `excluded_unsealed` | `CAND8` search_record | PROVABLE |
| 3 | P2: `V011` twin in `excluded_unsealed` | `CAND8` search_record | PROVABLE |
| 4 | `excluded_token_miss` = the 603-byte member, missing `general` | `CAND8` | PROVABLE |
| 5 | 0 of 37 nonclaim entries carry the defining form; control fires | §2.2 | YOURS |
| 6 | EXC-08-2's elements all present | `CAND8` search_record | PROVABLE |
| 7 | Tokens `{FS, general}` from the backticked object; lawful under `RULE` §2 | `CAND8`, `653581bf…` | PROVABLE |
| 8 | The two corpus names differ in their third token | `CAND8` `corpus_id` vs filename | PROVABLE |
| 9 | V009-01 REGISTRY typing on all four V003 elements | `722a7ea6…` | PROVABLE |
| 10 | Nothing licensed; EMPTY correct | `1741cdb3…` SEALED-OK | PROVABLE |
| 11 | `S3 = 0`: the review-ledger reading was declined in practice | `CAND8` attachment_counts | PROVABLE |

**Pin check: 11/11.**

### 5.2 Jurisdiction check

**On returning CLEAN where 766 returned NOT VERIFIABLE.** The difference is custody, not
judgement: the objects are now readable and every check 766 listed as unreachable has been run.
*Does the outcome space distinguish false from cannot-see?* Yes — 766 said cannot-see and named
what was missing; this says **clean, with the tests displayed and one finding that is not the
candidate's**.

**On BR-1.** Half A's CLEAN on V009-01 is a producer verdict I declined to adopt at 766. I do not
adopt it now either — §3 reaches CLEAN **by my own tests** against V003's four elements and the
sealed decision basis.

**On the VOID CONDITION.** Nothing chosen from a desired outcome. The convenient result would
have been to let the token divergence pass unremarked, since it changes no member; §2.6 records
it because the *rule* is what the next corpus will be built on.

### 5.3 Self verb audit — **CLEAN, with two disclosures**

1. **My first member count was wrong and I caught it by reading.** 134 names, one "mismatch" —
   which was a sidecar parsed as a member. Reported here rather than silently corrected, because
   the same class of error (a probe over-matching on filename shape) has cost me twice this
   session.
2. **My 766 token set differed from the candidate's and I checked the direction of risk rather
   than assuming mine was right.** The narrower probe was mine; the wider one is the candidate's
   and is the safer direction for a completeness hunt. **No member is affected**, and I say so
   instead of scoring a point.

---

```text
MEMBERS = byte-verified 133/133 (plus 10/10 sidecars verifying against the files they
   name; 84 status/fixture files not content-addressed).  ZERO digest mismatches.  My
   first pass reported 134 names and one mismatch; the "mismatch" was a SIDECAR whose
   filename carries the digest of the file it seals — my probe's artifact, not the
   corpus's, caught by reading rather than reporting.
PREDICTIONS = resolved (displayed).  P1 CONFIRMED: V009 b8168542... — the artifact the
   row is NAMED for — is in excluded_unsealed.  P2 CONFIRMED: the unsealed V011 twin
   20a3a17d... is in excluded_unsealed.  RULE section 1's "visible, not silently
   dropped" holds for exactly the two cases most at risk of a silent drop.  And
   excluded_token_miss contains precisely ONE entry — the old 603-byte member, missing
   "general" — so half A's INC-08-1 is recorded IN THE CANDIDATE'S OWN TABLE rather
   than merely fixed.
AMBIGUITY = resolved in PRACTICE, open in the RULE.  The candidate reports S3 = 0 and
   classifies V009 (digest present only in a full-stack REVIEW LEDGER) as UNSEALED —
   the permissive S3 reading was DECLINED, so V009's exclusion is lawful and is not a
   wrong exclusion.  RULE section 1's S3 wording still does not settle it; one line
   would.  SECOND RULE-LEVEL FINDING: the corpus has TWO NAMES — corpus_id
   "…:general-FS-corpus" vs filename "…_general_FS_claim" — differing in the third
   token, so V002's "corpus-name tokens" admits two lawful token sets.  The candidate's
   {FS, general} is the WIDER and therefore safer direction; my 766 {general, FS, claim}
   was narrower; NO MEMBER IS AFFECTED either way.  A defect in the naming, not the work.
VERDICTS = C-B-V009-08 CLEAN — single member byte-verified, S2-attached, a genuine USE
   not a mention, no self-citation, and 0 of the 37 EXCLUDED_ATTACHED_NONCLAIM entries
   carry the defining form of the claim (discriminator calibrated on the selected
   member, control fires).  All four half-A findings resolved.
   C-B-V009-01 CLEAN — REGISTRY typing correct on all four V003 elements; EMPTY with a
   SEALED decision basis (DECISION_V009_01_CARRIER_PB: "NO BASIS OR TRIVIALIZATION IS
   LICENSED"), so nothing is wrongly excluded and wrong inclusion is vacuous; the
   schema-version divergence is self-declared and pending the registrar.
   Reached by my own tests; half A's CLEAN is not adopted.
   PROCESS FINDING FROM 766 NOW CLOSED: the dual-verify control was not executable by
   this lane; the registrar mirrored the members; it is now executable and has been
   executed.
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+2 disclosures at section 5.3)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
