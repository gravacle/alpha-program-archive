# RELAY 766 — DONE — DARIO LANE

Task: PASTE 766 / [7A / STEP 11] — corpus verification half B: hunt both directions on
C-B-V009-01 and the regenerated C-B-V009-08; verify typings; verify the four half-A findings
resolved without new ones.
Lane guard: header names **DARIO**; satisfied. PICKUP-ACK written before source work.
Status: **COMPLETE, SEALED, STOPPED.** Nothing adopted; no instance sealed; no M2 query run.
No register, plan, tracker, or git action.

## Hashes

```text
INBOX    relay_inbox/RELAY_PASTE_766_CORPUS_VERIFY_B_DARIO_V001.md
         45d7d2be5d1672fd125ab1f6ee7a1fe97c0bb7e7012fba8017147f4732e1115a   sidecar OK

OUTPUT   workspace/STAGE8_7A_CORPUS_VERIFY_B_DARIO_V001.md
         a24ec45805a832349d1a0bc98c7409c197cc0d5b0b0467d4fdeae11466759b74
         419 lines / 23,760 bytes
SEAL     ...md.seal.sha256   shasum -c OK   (name probed ABSENT, recursively, before the write)
```

Eleven source pins verified. Pin check **11/11**.

## Final lines

```text
CANDIDATES = 2 verified — to the extent archive-side custody permits (partial / nil)
HALF_A_RESOLUTIONS = confirmed, three of four
FINDINGS = two checkable predictions + one rule ambiguity
VERDICTS = C-B-V009-08 NOT VERIFIABLE (partial, no defect found) · C-B-V009-01 NOT VERIFIABLE
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+3 disclosures at §6.3)
```

## Neither candidate is readable archive-side

`0a134859` returns nothing; `*REGENERATED*` returns nothing; **no `corpus_candidates/` directory
exists anywhere**; `step11_tooling_family4/` does not exist (family1 and family2 do). The
originals `cfa8db99…` and `722a7ea6…` are absent too.

**Half A could read them — it cited byte spans inside them** (`[211,470)`, `[0,603)`,
`[0,1805)`). I cannot. So the authority decision's control — *"BOTH LANES independently verify
set-completeness"* — is, for this lane under ARCHIVE-SIDE ONLY, **not executable as specified**.
On this instance the producing lane and the only reading verifier coincide, which is the
condition dual-verify exists to remove. **The fix is one registrar mirror**, exactly as was done
for the D_BR primaries at 762.

## What I could verify held — three of four

- **EXC-08-1 CONFIRMED.** Both spans half A cited verify **verbatim**: `[5505,5840)` names *"the
  V011 **general** finite-Hilbert premise"* and `[37614,38217)` **states** the Finite Pure-State
  Kinematics Premise with `ds_FS²` in V011's own voice. The first is a *mention*, the second the
  *use* on which membership rests — and half A's own verbs already distinguished them.
- **INC-08-1 CONFIRMED.** The V002 all-token conjunction **passes** on the new member: `general`
  = 9, `FS` = 8, `claim` = 21. The old member's defect was **zero** `general`. Resolved by
  satisfying the amendment, not relaxing it.
- **INC-08-2 CONFIRMED IN PART.** The `S2_PACKET_MANIFEST` attachment is real and **doubly
  attested** — the digest appears in two sealed manifests. Whether the member *record* carries
  the mode is inside the JSON: unreachable.
- **EXC-08-2 NOT VERIFIABLE**, and *"without introducing new ones"* is **untestable** — a diff of
  two files I do not hold.

**Independent corroboration:** my own archive-side conjunction sweep found **130 matching files,
39 S1-sealed**, against the regen's **1 selected + 37 attached-but-nonclaim = 38**. Different
lane, different glob, smaller universe — right order, and it supports the regen's central move
that most matches are mentions. **Self-citation checked and clean:** both verification artifacts
satisfy the conjunction, and the candidate does not self-include.

## Two checkable predictions and one rule ambiguity

**(P1)** **V009 itself** — the artifact the row is *named* for — passes the conjunction and
genuinely **uses** the claim (`Fubini-Study metric` at `[3102]`, `ds_FS` at `[34144]`), yet has no
S1 sidecar and its digest appears in **no `.sha256` file anywhere**, only in a review ledger. So
it is unsealed under the rule and **must appear in the `EXCLUDED-UNSEALED` table** — *"visible,
not silently dropped"*. One grep confirms it; absence would be a finding.

**(P2)** The unsealed top-level **V011 twin** `20a3a17d…` also passes the conjunction — the
739 name-collision hazard, still live, and another `EXCLUDED-UNSEALED` case.

**(A1)** The rule's **S3** wording does not settle whether a full-stack **review ledger** counts
as a *"sealed package or baseline inventory."* On the permissive reading, V009 is S3-attached and
its exclusion becomes a **wrong exclusion**. That is an ambiguity in the rule, not the candidate.

**I declined both verdict labels.** A CLEAN meaning *"nothing in the part I could see"* would
report a single-lane verification as a dual one.

---

## CARRIED: 765's outstanding hunt returned — verdict CONFIRMED, and one correction to me

**Confirmed.** Four hunters, ~50 requires, `survivors: []`. Their bottom line: *"**NO SEALED
REQUIRE FORCES A VALUE OF q, THE BUNDLE CLASS, OR THE CHIRAL INDEX ON S2_flux.**"* My 765
UNDERDETERMINED stands.

**Strengthened in two ways.** The only excluding statement — the `|q| ≥ 1/2` bound — lives in a
mirror with **zero in-corpus digest matches and zero filename mentions**, self-typed
`PROPOSED_NOT_CLOSED`; so even that lone constraint is un-attested. And on the chain I identified
and rejected, the corpus is sharper than I reported: it **does** seal integer charge structure on
the `S1_Q` side (integer character lattice, primitive unit winding `|n| = 1`), and it seals **in
three independent places** that this does **not** propagate to a flux — *"a **character**
lattice, not a flux"*, *"it does not seal a quantized curvature flux"* — with the missing bridge
named as a **would-build**: *"a theorem mapping unit character / `Q_Sigma` data to a fixed
beta-sensitive geometric flux or current."*

**And a correction to my own 765 preflight.** I stated the control `E_parent` = **217 files**.
That number is wrong, and I have reproduced the error: I ran the control **case-insensitively**,
so `e_parent` matched inside `complete_parent`, `source_parent`, and similar. Measured properly:

```text
case-insensitive 'E_parent' (what 765 printed): 218 files   <- substring artifact
case-sensitive   'E_parent' (the actual object):  11 files
```

The verdict is unaffected — a control's job is to be non-zero, and 11 is non-zero — but a stated
number in a sealed artifact is wrong, and it undercuts the practice I installed at 755. **Refined
practice, adopted here:** a control must be measured with the same precision as the finding —
case-sensitive and word-boundaried where the object's name is. A sloppy control is worse than
none, because it looks like calibration.

Nothing written archive-side but the ACK, the artifact, and its seal.
