# RELAY 772 — DONE — DARIO LANE

Task: PASTE 772 / [7A / STEP 11] — complete half B against the mirrored members: byte-verify,
hunt both directions with content in hand, resolve the two predictions and the rule ambiguity,
confirm the fourth half-A resolution.
Lane guard: header names **DARIO**; satisfied. **CHAINED PICKUP** (smallest DARIO relay > 770;
771 absent). PICKUP-ACK written before source work.
Status: **COMPLETE, SEALED, STOPPED.** Nothing adopted; no instance sealed (registrar's act);
no M2 query run. No register, plan, tracker, or git action.

## Hashes

```text
INBOX    relay_inbox/RELAY_PASTE_772_CORPUS_VERIFY_B2_DARIO_V001.md
         fcf4e1f63a6347fdf44e1480d74653daf0f3ce11fa0a7f6f1b8f1d7206c3bdbf   sidecar OK

OUTPUT   workspace/STAGE8_7A_CORPUS_VERIFY_B2_DARIO_V001.md
         9e24b12d11d1ba93664b2784023df7ad2d4ed7b0196d0f1251ddd70abd382ec2
         365 lines / 19,778 bytes
SEAL     ...md.seal.sha256   shasum -c OK   (name probed ABSENT, recursively, before the write)
```

Eleven source pins verified. Pin check **11/11**.

## Final lines

```text
MEMBERS = byte-verified 133/133
PREDICTIONS = resolved (both CONFIRMED)
AMBIGUITY = resolved in practice, open in the rule — plus a second rule-level finding
VERDICTS = C-B-V009-08 CLEAN · C-B-V009-01 CLEAN
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+2 disclosures at §5.3)
```

## Both candidates CLEAN, and both 766 predictions land

**133/133 members byte-verify; 10/10 sidecars verify against the files they name; zero
mismatches.**

- **P1 CONFIRMED** — `V009`, the artifact the row is *named* for, **is in `excluded_unsealed`**.
- **P2 CONFIRMED** — the unsealed `V011` twin is there too. The 739 name-collision hazard is
  handled, not merely survived.
- **`excluded_token_miss` holds exactly one entry: the old 603-byte member, missing `general`** —
  half A's INC-08-1 recorded *in the candidate's own table* rather than merely fixed.
- **EXC-08-2 resolved** — census, exclusion tables, alias tables and attachment counts all
  present. **All four half-A findings are now resolved.**

**The wrong-exclusion hunt finds nothing.** I tested all **37** `EXCLUDED_ATTACHED_NONCLAIM`
entries with a discriminator calibrated on the selected member — the *defining* form of the claim.
**0 of 37 carry it; the control fires on the selected member.** The mention/claim classification
is correct.

**C-B-V009-01 CLEAN by my own tests**, not by adopting half A's verdict: REGISTRY typing correct
on all four V003 elements, `EMPTY` with a **sealed decision basis** — *"NO BASIS OR TRIVIALIZATION
IS LICENSED"* — so nothing is wrongly excluded and wrong inclusion is vacuous.

## Two rule-level findings — neither is a defect in the work

**The corpus has two names.** `corpus_id` reads `…:general-FS-corpus`; the filename reads
`…_general_FS_claim`. Different third token. V002's conjunction is defined on *"corpus-name
tokens"*, so **two lawful token sets follow and they differ** — the candidate probes `{FS,
general}`, my 766 pass probed `{general, FS, claim}`. The candidate's is the **wider and therefore
safer** direction for a completeness hunt, and **no member is affected either way**. One line
naming which string is the corpus name closes it.

**The S3 ambiguity (766's A1) is resolved in practice, open in the rule.** The candidate reports
`S3 = 0` and classifies `V009` as UNSEALED — the permissive review-ledger reading was **declined**,
so `V009`'s exclusion is lawful. `RULE` §1's wording still doesn't say so. Same one-line fix.

## The 766 process finding is closed

766 reported that the dual-verify control was **not executable** by this lane — half A could read
the candidates and I could not, so the producing lane and the only reading verifier coincided.
**The registrar mirrored the members; the control is now executable and has been executed.** A
process finding that gets acted on should be seen to close, not merely lapse.

## Disclosed (two)

**My first member count was wrong and I caught it by reading.** 134 names, one "mismatch" — which
was a **sidecar** whose filename carries the digest of the file it *seals*. My probe over-matched
on filename shape; the corpus was clean. Reported rather than silently corrected, because that
class of error has cost me twice this session.

And where my token set differed from the candidate's, **I checked the direction of risk instead of
assuming mine was right** — the wider probe is theirs and is the safer one.

**CHAINED PICKUP status:** on writing this file I check `relay_inbox` for the smallest DARIO relay
above 772. If none is present, the chain STOPS CLEANLY here.

Nothing written archive-side but the ACK, the artifact, and its seal.
