# Stage 8 / 7A Step 11 — corpus candidates, verification half A

**Lane:** CODEX 2  
**Relay:** 761  
**Disposition:** one candidate clean; one candidate has inclusion, exclusion, and completeness-carrier findings; no corpus instance sealed or admitted

## 1. Pickup, authorities, and custody

The single relay `RELAY_PASTE_761_CORPUS_VERIFY_A_CODEX2_V001.md` verified before reading at SHA-256 `352311d794e3616546e67ca4891d54db60ac4fe31f66aa415807c0e8af70b198`; its sidecar hashes to `f4d902e9c4f0e74655e2c40d5304ba8f5e220769b4d752e0336a41485aa0f930`. The CODEX 2 lane guard matched, the output/report/ACK/DONE names were clear in both workspaces, and `relay_outbox/761_ACK.md` was written before candidate inspection.

The governing bytes reverified through their adjacent seals:

| Object | SHA-256 | Relevant byte span |
|---|---|---:|
| corpus-selection rule V001 with V002/V003 amendments | `653581bf54313ef026add193c1d08dde29bcb5e9cde78e5b0383e140114fd495` | CLAIM typing `[1004,1501)`; V002 `[2436,3220)`; V003 `[3220,4200)` |
| principal corpus-selection authority | `0dfc6e7bb761850e7cb4996c9a0b63e94567c7ae88c7de837f78b3b5628e2ad7` | whole sealed decision |
| V009-01 P-B decision | `1741cdb311def6263d3ab333c6f7d4280e80f862bdf2208276f94a1f4297e870` | `[576,942)` |
| current registrar register | `eb272fe8c030e063e8c105312988b1c589ceee2c67e3c7e589775203312b2c0e` | Q-640 `[1303957,1305647)` |
| BX07 registry snapshot | `5a14e376032f372f5f696c89e5ba3327a8f711cdc259be13b04f7f9dd2a0d43f` | whole 873-byte JSON |

The two unsealed Family-4 candidate wrappers rehashed to their content-addressed names:

| Row | Candidate SHA-256 | Bytes |
|---|---|---:|
| `C-B-V009-08` | `cfa8db997637f724c31131a14c068850fc0d0ba08351c77ba0c50bc685339ed5` | 1,805 |
| `C-B-V009-01` | `722a7ea616eb159a188987646f345c6423d1764b59a717af7fc941d5b9aff2d3` | 1,080 |

This artifact is one lane's verification half only. It neither seals a candidate as an instance nor supplies the other lane's verification.

## 2. Search universe and probes

### 2.1 Current pre-output universe

The audit enumerated these roots directly; the archive mirror and `memory-bank` were not counted as distinct program content:

```text
/Users/bgm/Documents/Documents - Brian’s MacBook Pro/New project/gravity_emergence_evidence_program/**
/Users/bgm/MB Work/alpha_supervision/**
/Users/bgm/Documents/Documents - Brian’s MacBook Pro/New project/_external_handoffs/**
```

Included globs were `**/*.md`, `**/*.py`, `**/*.json`, and `**/*.csv`. Directory basenames `.git`, `node_modules`, `site-packages`, `sympy`, `.cache`, `.proof_deps`, `.python_deps`, `external`, `third_party`, `sources`, and `review_packet*` were pruned, matching the standing census convention. The current pre-output enumeration was **16,100 path entries / 9,582 distinct byte digests**: 15,040 program-tree entries, 904 supervision entries, and 156 handoff entries. Counts are current and exclusion-dependent; they are not the withdrawn historical denominator.

### 2.2 Four modes

For V009-08, fixed-string tokens were `general` and `FS`, conjoined under V002. The normalized and punctuation surfaces were `general FS`, `general-FS`, and `general_FS`, case-insensitive, with `Fubini-Study`, `Fubini–Study`, whitespace, and underscore forms included because the sealed target source itself displays the `FS`/`Fubini-Study` vocabulary. Apostrophe normalization found no additional spelling. The candidate says `object-vocabulary-aliases` but pins no sealed alias table; no further alias was invented.

That probe returned **181 path hits / 127 distinct digests**. Thirty-one paths (30 digests) had valid adjacent S1 seals. The packet V011 digest also occurred in 12 content-addressed runtime copies and was resolved back to its authoritative S2 packet member. Inspection of every distinct hit left one lawful claim-source digest: packet V011. The other 126 digests were rejected as requirement/spec/tool/envelope/relay/run-ledger/register mentions, self-citations, unsealed historical/root copies, runtime-library `FS` uses, unrelated subject matter, or wrong-scope FS uses. Those are mention-not-use and process-artifact exclusions, not corpus members.

For V009-01, the same universe was probed as the required negative control with conjoined `abstract`, `line`, and `alias` tokens plus whitespace/hyphen/underscore variants. It returned **183 paths / 151 digests**, with one exact `abstract[- _]line[- _]alias` object-form path. Under V003 every one is wrong-typed as membership evidence: the corpus is a decision-accrual REGISTRY, not a claim sweep. Registry completeness was instead checked against sealed decisions and the live register tail.

## 3. Candidate `C-B-V009-08`: FINDINGS

### 3.1 Typing

`CLAIM_SCOPED` is the correct type: the descriptor operand names the `general-FS` claim family, and V002 requires the `general` AND `FS` token conjunction. The finding is not the type label; it is the member set emitted under that label.

### 3.2 Wrong inclusion

| ID | Finding | Pinned span |
|---|---|---|
| `INC-08-1` | The sole member does not satisfy the V002 conjunction. Its complete 603 bytes contain `Fubini-Study` at `[270,282)` and `ds_FS` at `[291,296)`/`[419,424)`, but contain **zero** fixed, normalized, punctuation-variant, or recorded-alias occurrences of `general`. | candidate member record `[211,470)`; member payload `[0,603)` |
| `INC-08-2` | The member record supplies only `{byte_length,relative_path,sha256}`. It records none of V001's S1/S2/S3 seal-attachment modes. The generated copy has no adjacent seal; its source span's packet attachment is not carried into the member record. A content digest does not by itself establish the required attachment. | candidate `[211,470)` |

The member bytes and declared one-member root rehash internally. That proves faithful packaging of the wrong set; it does not cure either inclusion finding.

### 3.3 Wrong exclusion

| ID | Finding | Pinned span |
|---|---|---|
| `EXC-08-1` | The actual sealed claim source is omitted: packet `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md`, SHA-256 `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a`. The same sealed source calls out the exact half-turn/`FS` budget and the V011 `general` finite-Hilbert premise at `[5505,5840)`, then states the finite pure-state/Fubini-Study premise and local identity at `[37614,38217)`. This is use, not a tooling mention. Its S2 attachment is the packet-manifest row `[7694,7808)` in `STAGE7_PACKET_MANIFEST_V001.sha256` (manifest SHA-256 `9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311`). | V011 `[5505,5840)`, `[37614,38217)`; packet manifest `[7694,7808)` |
| `EXC-08-2` | The candidate carries no searched roots, glob/exclusion census, `EXCLUDED-UNSEALED` table, or sealed alias-table pin. Consequently its one-member list cannot be a V001 §3 set-completeness record even apart from `EXC-08-1`. | complete candidate `[0,1805)` |

**Verdict:** `FINDINGS`. The candidate is correctly typed but its included member is unlawful, its lawful packet member is absent, and its declared root is therefore not the root of the rule-selected set. It must not be sealed or consumed by M2 in this form.

## 4. Candidate `C-B-V009-01`: CLEAN

### 4.1 Typing and current state

The P-B decision's `[576,942)` says no basis or trivialization is licensed; any future unit representative or scalar trivialization must be separately licensed and entered in the alias corpus, and no member is selected. That accrual verb is exactly V003's REGISTRY test. The candidate's `REGISTRY` type, no-producer rule, principal licensing authority, and empty current member list agree.

The sealed BX07 snapshot independently carries `members:[]`. Its empty content root recomputes as:

```text
SHA256("A35-CONTENT-ROOT-v1" || 0x00)
= 6a666c3166fd15026fe5996065f32d5e84a92edd7e99439f72cc0c7b4d496054
```

This equals the candidate's declared root.

### 4.2 Both-direction hunt

- **Wrong inclusion:** none. The member set is empty. The prior 267-mention sweep recorded at Q-640 `[1303957,1305647)` and the current 183-path negative-control sweep are both correctly excluded as wrong-typed claim searches.
- **Wrong exclusion:** none. The decision/ruling filename sweep over the stated universe found exactly one V009-01/BX07/alias-corpus decision: `DECISION_V009_01_CARRIER_PB_2026-08-08.md`. The exact `V009-01|BX07|alias corpus` sweep after Q-640 found no later register entry, and no sealed decision licenses an accrual.
- **Seal attachment:** vacuous for `members:[]`; the state basis and BX07 snapshot each reverified through S1 sidecars.

**Verdict:** `CLEAN` for membership and V003 typing. The known v001-schema `minItems`/V003-empty interface remains for the registrar/spec owner to reconcile before any new instance packaging; it is not evidence of a missing registry member and does not authorize this lane to rewrite the schema.

## 5. Battery, custody, and verb audit

The two candidate files, every cited source byte range, the packet row, the P-B decision, the BX07 snapshot, the rule, and the register were hashed independently. The audit searched both inclusion and exclusion directions, exercised fixed, normalized, punctuation, and bounded alias surfaces, and separated mention, process, register self-citation, wrong attachment, unrelated runtime use, and actual claim use.

No candidate was sealed, repaired, admitted, or bound to an envelope. No M2 query, evaluator chain, register, plan, tracker, git, member binding, fixed-point execution, end test, physical-quantity evaluation, or measured-constant comparison occurred. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false` remain in force.

Verb audit: **CLEAN**. `CLEAN` is restricted to the V009-01 candidate's set and typing; it is not admission. `FINDINGS` is restricted to the V009-08 candidate and does not relitigate its separately built graph.

CANDIDATES = 2 verified (typings checked)
INCLUSION_FINDINGS = C-B-V009-08: INC-08-1, INC-08-2; C-B-V009-01: none
EXCLUSION_FINDINGS = C-B-V009-08: EXC-08-1, EXC-08-2; C-B-V009-01: none
VERDICTS = C-B-V009-08 FINDINGS; C-B-V009-01 CLEAN
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
