# RELAY 709 — DONE — DARIO LANE

Task: PASTE 709 / 7A handoff — freeze the OBS-22 recognition preregistration as V002.
Status: **COMPLETE, SEALED, STOPPED.** No register, plan, tracker, or git action taken.

## Hashes

```text
OUTPUT   STAGE8_7A_OBS22_RECOGNITION_PREREG_V002_FROZEN.md
         9f0d12b4556427eb965bcd9c869f645b984009fdbcc0d1d19a2c7216d31c51f1
         802 lines / 48,744 bytes
SEAL     STAGE8_7A_OBS22_RECOGNITION_PREREG_V002_FROZEN.md.seal.sha256   shasum -c OK

BASE     STAGE8_7A_OBS22_RECOGNITION_PREREG_DARIO_V001.md
         c9c1f2dc00a70682bc526948e8624346f04164318a089b50f1e25dba14d5489d
         (the digest the ruling cites; re-derived here, not transcribed)
RULING   supervision/DECISION_F1_SPLIT_K2_SLOT_2026-08-08.md
         e76746aeea351bf6a7e6bb97297ae21a9811ac7e05d0aebff31288102ca2d6a7
```

## Final lines

```text
FROZEN = true
DELTAS = F1' + K-2 slot + freeze execution only
CRITERIA = 15 unchanged
UNGROUNDED = 2 carried
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 miscount in my own delta certificate, caught by my own
                         pin check before sealing; +3 items at §D.3)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

## What was done

**Carriage method: byte-copy plus asserted surgical replacement.** V002 is V001
copied byte for byte, then **fourteen** named string replacements, each asserted
to match exactly once before application. "Nothing else moves" therefore holds by
construction rather than by claim — the standard this lane has held Builder A to,
applied to itself.

**D1 — F1' authored (Ruling 1).** F1 and F1' are displayed side by side at §2.4.
The weak-rule reading **still kills**, exactly as F1 did. The scale-dependence
reading **routes to measurement** under K-1/K-3 and can still lose there, never by
mere family-hood. The original F1 is **not re-worded in its own sealed file** — it
stays at `3c008ecc… [10484,10508)`, superseded of record, and the supersession is
recorded here rather than performed in someone else's bytes.

**D2 — K-2 as a named-open slot (Ruling 2).** The kill set freezes as
**{K-1, K-3}**. K-2 is written into the frozen artifact, left empty, and frozen
empty with its name on it — with a five-field status block stating it is fillable
only by a sealed grounding entering as a surfaced revision. An empty slot written
down is not a silent omission; its absence is visible at every future reading.

**D3 — the freeze executed (Ruling 3).** Title, status, §5 and the final lines now
state FROZEN rather than proposed. From this seal, any change to a criterion,
test, evidence form, guard, verdict definition, kill condition or ledger schema is
a revision of record, surfaced to the principal before it takes effect.

## Invariance, asserted rather than assumed

Eleven sections were extracted from both files and compared byte for byte, all
identical: §1.1 the PASS bar; §1.2 R1–R9; §1.3 R10–R14; §1.4 U1 and U2; guards
G-1, G-2, G-3, G-5; §3 the three verdicts and schema; §4 the ledger schema; §6 the
classical-tests audit. The K-1 and K-3 rows are byte-identical. **G-4 is the one
guard that moved**, and only because F1' is authored there under Ruling 1.

## Disclosures

**A miscount in my own delta certificate.** I wrote "nine" replacements and had
made **fourteen**. My pin check caught it before sealing. This is the exact defect
class this lane charged Builder A with at relay 683 (58 declared / 63 true) and
695 (160/26 declared / 155/21 true), and the cure is the one I demanded there:
§D.1 now enumerates every replacement individually, so the total cannot drift from
the list.

**One correction of record against my own V001.** V001 proposed routing the
scale-dependence reading to `NOT-RECOGNIZABLE-AS-STATED`. The ruling routes it to
**measurement under K-1/K-3**, which is stronger — a third-verdict routing parks
the reading, whereas measurement under a preregistered kill condition can still
lose. **The authored F1' follows the ruling, not my draft**, and §2.4 says so.

**Two things I declined to do**, both recorded at §D.3: I did not re-word the
sealed F1, and I did not fill K-2. Filling it would have been the fitting
REQUIREMENT 5 exists to stop.

## Gates

No junction map was computed or evaluated. No junction object formed, no numeric
produced, no member bound, no fixed point, no end test, no comparison to any
measured constant.

## Queue rule

The standing queue rule is noted and in force from the next relay: on a bare
number N, read `relay_inbox/RELAY_PASTE_N_*.md`, verify its `.seal.sha256`, execute
under all standing session rules, seal outputs, write `relay_outbox/N_DONE.md`, and
STOP; if the inbox file is missing or its seal fails, report that and STOP.
