# JOINT ANCHOR DECISION — `JointAnchorDecision.v002` CONFORMANT INSTANCE (THE G0 REPAIR)
## DARIO LANE — RELAY 925 — `[PLAN:AXN-BUILD-D23]`

## 0. Preflight

Relay 925 verified before reading at
`f80a7bf6660116150f8dae0df017f3611140831b9109ff360fe37de14d4ea09a`. Lane guard read DARIO; the
pickup ACK was written before content access. `PROGRAM_STATE_BRIEF_V005.md` verified and read before
task work at `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`. All four subjects
verified against their own sidecars before reading, at the digests the relay states. The output name
was clear in both the archive root and `workspace/`.

---

## 1. Law-9b closure — declared first

```text
C_925 = {
 1  RELAY_PASTE_925_DECISION_INSTANCE_DARIO_V001.md
      f80a7bf6660116150f8dae0df017f3611140831b9109ff360fe37de14d4ea09a
 2  supervision/PROGRAM_STATE_BRIEF_V005.md
      e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c
 3  STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V002.md                    [the governing schema]
      58b966ed371b23b29b9e3ceed280eb30c804484becb2b17ca6ea465668e951bc
 4  JOINT_ANCHOR_DECISION_OF_RECORD_V001.md                        [the principal's act — UNTOUCHED]
      f0179d43b4b2ed89f4cfb9adc1daa8c7cc0c9c5f038e3bbe7332727fdddaaa8f
 5  JOINT_ANCHOR_DECISION_OF_RECORD_V001.md.seal.sha256            [the prospective-freeze receipt]
      6abd5f1416c15d88e2e1f42b225527446e454cc76c422d05de6e0da295d4c1ad
 6  JOINT_ANCHOR_CERTIFICATE_MANIFEST_V001.md
      589c12f7cb76b5f4a2ba895d5942061ec3d801d6983f656304b172bfde964b27
 7  STAGE8_AXN_GAUNTLET_RUN_CODEX2_V001.md                         [the G0 failure list]
      1eb2c14c9352156ff5cdfe011eb8f382b4ea2a5fa1574f3678c298e3356f0054
 8  STAGE8_CTP_PHYS_INPUT_PACKAGE_C0_DOR008_ASSEMBLY_AND_FIRST_RESTRICTION_TEST_V001.md
      1467ab9850022931e68dc9ffa625d95099d8f6bb74d734dc9d0466f169bd00b6
 9  STAGE8_TASK4A_ORIGIN_FED_REFINEMENT_TOWER_GENOMEGA_PORT_TYPECHECK_DETERMINATION_CODEX_LANE2_V001.md
      4e00c7edbec105cd9c60cba483f11c1888a541e5963f3c1168fc6d00085669b0
}
```

**Name probe.** `JOINT_ANCHOR_DECISION_INSTANCE_V002.md` and its sidecar: clear at pickup.

---

## 2. Gates and standing

```text
alpha_computed         = false
proof_authorized       = false
kappa_record_computed  = false
JOINT_ANCHOR_DERIVED   = false
```

This instance is **CLAIMED** until the gauntlet re-run. **I am transcribing a principal act into the
form its schema requires. I am not making, completing, or repairing one.** Every populated field
below displays where its content comes from. Every field whose content is absent from a sealed source
is **STOPPED and routed to the principal by name** — no default, no interpretation.

**V001 is untouched.** Its digest was verified `f0179d43b4b2ed89…` before this work and again after
writing; this instance **pins** it and does not amend it. Post-freeze mutation remains FORBIDDEN.

**BLIND held.** The A0 rank fiber is entered as pointer and digest only. No rank was read, no ratio
computed or quoted, no fiber compared. `BUILDER_SELECTED_TAG / STATE / FIBER` remain `false`.

---

## 3. The instance — populated fields, with provenance

### 3.1 `JointAnchorDecision.v002` — top level

```text
JointAnchorDecision.v002 {
  schema                        = "rd22.axn-joint-anchor-decision.v002"
  disposition                   = APPROVE
  decision_artifact_sha256      = f0179d43b4b2ed89f4cfb9adc1daa8c7cc0c9c5f038e3bbe7332727fdddaaa8f
  decision_time                 = 2026-08-10
  governing_instrument_sha256   = 58b966ed371b23b29b9e3ceed280eb30c804484becb2b17ca6ea465668e951bc
  scope                         = "joint-state producer into State(A_C0)"
  anchor_tag_class_entry        = {BI}
  anchor_content_entry          = the instrument's BI equations: Phi_joint(I_C0) = I_C0
                                  together with input-faithfulness, bound to the entered
                                  carrier and fiber
  certificate_manifest_sha256   = 589c12f7cb76b5f4a2ba895d5942061ec3d801d6983f656304b172bfde964b27
  prospective_freeze_receipt_sha256
                                = 6abd5f1416c15d88e2e1f42b225527446e454cc76c422d05de6e0da295d4c1ad
  supersession_rule             = "DERIVATION_SUPERSEDES_PROSPECTIVELY"
  post_freeze_mutation          = "FORBIDDEN"
  member_selection              = "FORBIDDEN"
  joint_carrier_entry           -> §3.2 (PARTIAL)
}
```

| field | provenance |
|---|---|
| `schema` | member 4 line 6, verbatim |
| `disposition` | member 4 line 7 — the principal's `APPROVE` |
| `decision_artifact_sha256` | member 4's own digest, recomputed here — **G0 item 1** |
| `decision_time` | member 4 line 18 |
| `governing_instrument_sha256` | member 4 line 8 = member 3's digest, recomputed |
| `scope` | member 4 line 9 |
| `anchor_tag_class_entry` | member 4 line 10; member 6 entries block |
| `anchor_content_entry` | member 4 lines 11–12; member 6; member 3's BI row |
| `certificate_manifest_sha256` | member 4 line 15 = member 6's digest, recomputed |
| `prospective_freeze_receipt_sha256` | `sha256` of member 5, the seal sidecar member 4 line 27–28 names as *"the prospective-freeze receipt … produced before any gauntlet computation"* — **G0 item 5** |
| `supersession_rule` / `post_freeze_mutation` / `member_selection` | member 4 lines 16–17 |

**Thirteen of thirteen top-level scalar fields populated by transcription.**

### 3.2 `JointCarrierEntry.v002` — 2 of 14 populated

```text
JointCarrierEntry.v002 {
  carrier_schema           = "rd22.axn-joint-carrier.v002"
  declared_joint_algebra   = content-addressed to member 8
                             1467ab9850022931e68dc9ffa625d95099d8f6bb74d734dc9d0466f169bd00b6
  a0_rank_fiber            -> §3.3 (PARTIAL)
  history_pairing_control_certificate -> §3.4 (PARTIAL)
  [ten further fields STOPPED — §4.1]
}
```

`declared_joint_algebra` is the sealed `A_C0` realization member 4 line 13 names. It is entered as a
pointer and digest, which is what "content-addressed realization" asks for.

### 3.3 `A0RankFiber.v001` — 2 of 8 populated, entered BLIND

```text
A0RankFiber.v001 {
  schema                = "rd22.axn-a0-rank-fiber.v001"
  source_carrier_sha256 = 4e00c7edbec105cd9c60cba483f11c1888a541e5963f3c1168fc6d00085669b0
  [six further fields STOPPED — §4.2]
}
```

`source_carrier_sha256` content-addresses member 9, the sealed DoR-013 fixed-A0 fiber source named at
member 4 line 13 and member 6 line 27. **Pointer and digest only: no rank read, no ratio computed, no
fiber compared.**

### 3.4 `HistoryPairingControl.v001` — 3 of 6 populated

```text
HistoryPairingControl.v001 {
  schema             = "rd22.axn-history-pairing-control.v001"
  control_relation   = NEITHER_EQUIVALENCE_PROVED
  pre_output_timestamp = 2026-08-10
  [three further fields STOPPED — §4.3]
}
```

`control_relation` is member 4 line 14 and member 6 line 29 — **G0 item 4's enum, transcribed**.

### 3.5 The JAC-03 scan surface — transcribed verbatim

Member 3's `JAC-03` fixes the scan surface, and it transcribes without interpretation:

```text
scan names: p_[A], r_0, r_ch, "rank ratio", "branch weight",
            identity-supported Dirac, product Haar, K4-K7,
            response, coupling, residual, and measured-target forms.
modes:      fixed-string, normalized-name, hyphen/spacing, semantic-receiver,
            over the complete frozen manifest.
rule:       control names permitted only in the designated HistoryPairingControl.v001
            disclosure and the preregistered G6 control block; reject any selection
            predicate that receives them.
```

**The scan surface transcribes. The candidate grammar it is to be scanned over does not exist** —
member 7 records it absent — so **G0 item 6 is addressed only in half**: the scan is specified, the
object to scan is missing. That half is routed at §4.4.

---

## 4. The stops — nineteen fields, each routed to the principal by name

Each field below has **no sealed source**. Supplying any of them would be an interpretation, a
default, or an invention, and the relay's rule is to stop and route.

### 4.1 `JointCarrierEntry.v002` — ten stopped

| # | field | why it stops |
|---|---|---|
| 1 | `stage_index_and_limit_rule` | member 8 contains no cylindrical system and no limit target; member 4 says "with its stage system", and the named realization does not carry one |
| 2 | `joint_identity` `I_C0` | **`I_C0` occurs zero times in member 8.** It occurs only where it is *demanded* — member 3 and member 4 — never where it is *defined* |
| 3 | `scalar_pairing_or_trace` | **no pairing or trace appears anywhere among the principal's entries** (member 4 lines 10–14; member 6 lines 24–30). The schema requires a faithful declared pairing with its normalization convention |
| 4 | `source_factor_embedding` `i_src` | **`i_src` occurs zero times in member 8**, the realization the entry names |
| 5 | `record_factor_embedding` `i_R` | **`i_R` occurs zero times in member 8** |
| 6 | `history_factor_embedding` `i_B` | **`i_B` occurs zero times in member 8, and `i_B` is absent from the entries altogether** — member 6 lists the algebra, stage system, `I_C0`, `i_src`, `i_R`, and stops there |
| 7 | `joint_superselection_map` `E_joint` | **`E_joint` occurs zero times in member 8** and is absent from the entries |
| 8 | `restriction_and_limit_certificates` | member 7 records the exact content-addressed inventory as absent |
| 9 | `equivalence_scope` | absent from the entries; no sealed representation-change invariance statement is entered |
| 10 | `physical_price` | **absent.** This is the field member 3 §3.2 makes the reverse-A2 guard — "explicit statement of every authored carrier/pairing/fiber datum". Nothing populates it |

On fields 4–7: those objects do exist elsewhere in the corpus — `i_B` in the state–algebra map, `i_src`
and `E_joint` in other artifacts. **Choosing which file supplies each is exactly the interpretation
the stop rule forbids**, because the entry names one realization and that realization does not
declare them.

### 4.2 `A0RankFiber.v001` — six stopped

| # | field | why it stops |
|---|---|---|
| 1 | `fiber_label` `[A]` | member 9 keeps the fiber symbolic and neutral; naming *which* `[A]` was entered is a determination the entries do not make |
| 2 | `I_A_sha256` | no addressable `I_A` artifact exists to content-address |
| 3 | `P_0_sha256` | no addressable `P_0` artifact exists |
| 4 | `P_ch_sha256` | no addressable `P_ch` artifact exists |
| 5 | `structural_rank_record_sha256` | **no declared fiber record exists of record.** Member 3 §3.1 permits structural ranks *only* inside such a record; there is none to address, and manufacturing one would breach the blind entry |
| 6 | `entry_freeze_receipt_sha256` | no entry-level freeze receipt exists. Reusing the decision's prospective receipt for this distinct field would be an interpretation |

### 4.3 `HistoryPairingControl.v001` — three stopped

| # | field | why it stops |
|---|---|---|
| 1 | `entered_pairing_sha256` | cascades from §4.1 field 3 — there is no entered pairing to address |
| 2 | `induced_history_functional_sha256` | no induced history functional exists as an addressable object |
| 3 | `exact_equivalence_or_nonclassification_certificate_sha256` | **no nonclassification certificate exists.** `NEITHER_EQUIVALENCE_PROVED` is the enum; the schema separately requires the certificate that establishes it |

### 4.4 The candidate grammar

Member 7: *"candidate grammar and admission predicates are not supplied."* The JAC-03 scan surface
transcribes (§3.5); the frozen grammar it must scan does not exist. **Routed.**

---

## 5. What this transcription establishes

**The G0 defect is not only that the decision document is prose.** That was the visible symptom.
Transcribing the principal's confirmed entries into the schema shows something the prose form
concealed: **the entries, transcribed perfectly and completely, populate twenty fields and leave
nineteen empty.** Reformatting cannot close that gap. Nineteen fields require content that no sealed
source contains — a pairing and its normalization, the superselection map, all three factor
embeddings, the stage/limit rule, the joint identity, the restriction/limit inventory, the
equivalence scope, the physical price, five fiber sub-digests, three control sub-digests, and the
candidate grammar.

Two of those deserve the principal's particular attention:

- **`physical_price` is empty.** Member 3 §3.2 makes it the reverse-A2 guard — the clause I recorded
  at 918 as the instrument's single best feature, the one that prices authored carrier and pairing
  data instead of letting a trace smuggle a history state. **The guard exists and has nothing in
  it.**
- **`scalar_pairing_or_trace` is empty, and `HistoryPairingControl.v001` depends on it.** The control
  certificate discloses what the entered pairing induces; with no entered pairing, the disclosure has
  no subject. The enum `NEITHER_EQUIVALENCE_PROVED` was entered, but the object it is a
  classification *of* was not.

This is a finding about **completeness of the entries**, not about their correctness. Everything the
principal did enter transcribes cleanly and travels verbatim. `BUILDER_SELECTED_*` stays `false`; the
anchor remains ADOPTED-AND-FROZEN, NOT DERIVED; the blind guard held throughout.

---

## 6. G0 checklist disposition

| # | G0 repair item | disposition |
|---|---|---|
| 1 | `decision_artifact_sha256` in the field | **ADDRESSED** — `f0179d43…` |
| 2 | `joint_carrier_entry` as a full instance | **PARTIAL** — 2 of 14; ten routed (§4.1) |
| 3 | `A0RankFiber.v001` instance, content-addressed, blind | **PARTIAL** — 2 of 8; six routed (§4.2); **blind held** |
| 4 | `HistoryPairingControl.v001` at `NEITHER_EQUIVALENCE_PROVED` | **PARTIAL** — 3 of 6, the enum itself addressed; three routed (§4.3) |
| 5 | `prospective_freeze_receipt_sha256` | **ADDRESSED** — `6abd5f14…` |
| 6 | JAC-03 scan surface | **PARTIAL** — surface transcribed verbatim; the grammar it scans is absent (§4.4) |

```text
G0_CHECKLIST = 2/6 fully addressed; 4/6 partial with every unmet part named and routed
```

---

## 7. FREEDOMS-CONSUMED (law 2a)

```text
JOINT_ANCHOR_INPUT   = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  the principal's act at member 4, verbatim and untouched;
  the manifest's entries block at member 6;
  member 3's schemas, transcribed rather than paraphrased;
  member 7's G0 failure list as the checklist;
  members 8 and 9 as the two sealed sources the entries name.

CONDITIONED-ON:
  nothing. Every populated field is a transcription with its provenance displayed;
  no field is conditional on a reading.

SUBSTITUTED:
  NOTHING. No pairing, trace, normalization, identity, embedding, superselection map,
  stage rule, limit target, inventory, equivalence scope, physical price, fiber label,
  rank, ratio, sub-digest, certificate, or candidate grammar was authored, defaulted,
  inferred, or supplied. Nineteen fields are STOPPED and routed to the principal by name.
  V001 was not amended.

SCALING WEIGHTS: NONE CONSUMED; NONE FIXED; NONE SUBSTITUTED.
```

---

## 8. Flattening check, verb audit, byte audit

**FLATTENING CHECK — S01–S37 walked, clean.** A transcription was not identified with an authorship:
§3 shows provenance per field and §4 stops rather than filling. A prose description was not identified
with an instance — that is the G0 defect and §5 keeps the distinction. An object existing *somewhere*
in the corpus was not identified with an object the named entry supplies (§4.1, fields 4–7). An enum
was not identified with the certificate that establishes it (§4.3). A pointer was not identified with
content: the fiber is addressed and unread. A guard was not identified with a filled guard —
`physical_price` exists and is empty, and §5 says so. A partial checklist item was not reported as
addressed.

**BUILDER-B INDEPENDENCE:** every field is drawn from sealed sources or stopped. A's code was not
accessed. No artifact of mine is load-bearing.

**SELF VERB AUDIT.** "Transcribed" is used only where a field's content is quoted from a sealed
source with its location shown. "Stopped" and "routed" are used for the nineteen, each with the
reason at its own receiver. "Addressed" is used for G0 items 1 and 5 only; "partial" for the other
four, never "addressed". No decision, entry, pairing, price, or certificate is claimed, and no
disposition is recommended. `VERB_AUDIT_SELF = CLEAN`.

**BYTE-POSITION SELF-AUDIT.** §1's heading begins at byte **656**, its closure fence opens at byte
**705**, and the exact member list ends at byte **2072**. A scan of bytes `[0,705)` over `no `,
`not `, `none`, `never`, `absent`, `missing`, `without`, `lack`, `fail`, `gap`, ` open`,
`unresolved`, `underived`, `false`, `cannot`, `zero`, `stop`, `block`, `wrong`, `refus`, `unswept`,
`unsealed` returns **zero hits**.

---

## 9. Final lines

```text
CLOSURE = declared-first (sec-1 heading 656, closure fence 705, members end 2072; pre-closure scan over 22 forms = 0 hits)
INSTANCE = STOPPED on nineteen fields, each routed to the principal by name: JointCarrierEntry.v002's stage_index_and_limit_rule, joint_identity, scalar_pairing_or_trace, source_factor_embedding, record_factor_embedding, history_factor_embedding, joint_superselection_map, restriction_and_limit_certificates, equivalence_scope and physical_price; A0RankFiber.v001's fiber_label, I_A_sha256, P_0_sha256, P_ch_sha256, structural_rank_record_sha256 and entry_freeze_receipt_sha256; HistoryPairingControl.v001's entered_pairing_sha256, induced_history_functional_sha256 and exact_equivalence_or_nonclassification_certificate_sha256; plus the candidate grammar. TWENTY FIELDS ARE POPULATED by transcription with per-field provenance displayed — all thirteen top-level scalars, two of the carrier's fourteen, two of the fiber's eight, three of the control's six.
G0_CHECKLIST = 2/6 fully addressed (item 1 decision_artifact_sha256 = f0179d43…; item 5 prospective_freeze_receipt_sha256 = 6abd5f14…, the digest of V001's own seal sidecar, which V001 names as the receipt produced before any gauntlet computation). 4/6 PARTIAL with every unmet part named: item 2 carrier 2/14; item 3 fiber 2/8 with the blind entry held; item 4 control 3/6 with the enum itself addressed; item 6 the JAC-03 scan surface transcribed verbatim while the candidate grammar it must scan is absent of record.
NEW_CONTENT = NONE. The STOP was mandatory on all nineteen: no sealed source supplies them, and supplying any would have been a default, an interpretation, or an invention. Notably, the objects behind four of the carrier stops DO exist elsewhere in the corpus — i_B in the state-algebra map, i_src and E_joint in other artifacts — but the entry names ONE realization and that realization declares none of them, so choosing a substitute file is precisely the interpretation the rule forbids.
ENTRIES = VERBATIM-FROM-V001 (verified): {BI}; the BI equations Phi_joint(I_C0) = I_C0 with input-faithfulness; the sealed A_C0 realization pointer; the blind DoR-013 fiber pointer; NEITHER_EQUIVALENCE_PROVED; supersession, post-freeze-mutation and member-selection constants. V001 UNTOUCHED — digest f0179d43… verified before and after writing; this instance pins it and amends nothing.
BLIND = HELD. The A0 fiber is entered as pointer and digest only. No rank was read, no ratio computed or quoted, no fiber compared. BUILDER_SELECTED_TAG / STATE / FIBER remain false. The blind guard is also why A0RankFiber's structural_rank_record_sha256 stops rather than resolves: member 3 permits structural ranks only inside a declared fiber record, none exists, and manufacturing one would breach the entry.
THE FINDING BEYOND THE FORM: the G0 defect is not only that the decision document is prose. Transcribing the confirmed entries into the schema shows that the entries — transcribed perfectly — POPULATE TWENTY FIELDS AND LEAVE NINETEEN EMPTY. Reformatting cannot close that; those fields need new principal entries. Two deserve particular attention: physical_price is EMPTY, and it is the reverse-A2 guard I recorded at 918 as the instrument's best feature — the guard exists with nothing in it; and scalar_pairing_or_trace is EMPTY while HistoryPairingControl.v001 depends on it, so the enum NEITHER_EQUIVALENCE_PROVED was entered but the object it classifies was not. This is a finding about COMPLETENESS of the entries, not their correctness: everything entered transcribes cleanly and travels verbatim.
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
```
