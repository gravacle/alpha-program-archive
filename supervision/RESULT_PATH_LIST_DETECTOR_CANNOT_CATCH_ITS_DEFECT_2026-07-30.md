# THE PATH-LIST DETECTOR HAS ZERO TRUE POSITIVES, AND CANNOT CATCH THE DEFECT IT WAS BUILT FOR

Reviewer lane, 2026-07-30. Sweep of the 18 `path_list_word_splitting` findings I requested in paste 131
and Codex lane 1 implemented. **VERDICT: all flagged sites are false positives, no prior bounded negative
is impugned by this check, and the check cannot intersect the failure mode it was designed for.** I asked
for this detector; the finding is against my own request.

## 1. WHAT THE DETECTOR MATCHES

`corpus_check.py:123`:

```
GREP_L_SUBST_RE = re.compile(r"(?:\$\(\s*|`\s*)(?:grep|rg|ripgrep)\b[^)`\n]*(?:\s-l\b|\s-rl\b|\s--files-with-matches\b)")
```

It treats a **backtick** as the opening of a shell command substitution. Run against the six flagged
prior artifacts, its 19 matches are:

```
BOHM_BLIND_DOF_COUNT_2026-07-28.md:135                    `grep -rl
BOHM_RESCOPE_REGISTER_2026-07-29.md:483, :1089 (x2)       `grep -rl
BOHM_ROUTE_RUNNABILITY_WORKFLOW_RECOVERED:641 (x2), :651, :1512 (x3)   `grep -rl
BOHM_SWEEP_2026-07-27_rl2b_campaign.md:716                `grep -rl
BOHM_V007_BACKWARD_INVENTORY_CRITIC:139 (x2), :714, :716  `grep -rl
BOHM_RATIO_ROUTE_ADJUDICATION_RESULTS:466                 `grep -rl
BOHM_V007_BACKWARD_INVENTORY_CRITIC:271                   `grep -oE "^\| A[0-9]+ " | wc -l
BOHM_REPLAN_AUDIT_RESULTS_2026-07-29.md:125 (x2)          `grep -o 'Preparation' | wc -l
```

**EVERY ONE IS A MARKDOWN INLINE-CODE SPAN.** In a `.md` file, `` `grep -rl H_energy` `` is prose — a
command being *described*, formatted as code. It is not a shell backtick being *executed*. The regex
cannot distinguish the two, so on Markdown it systematically over-flags.

The last three are a different class and also harmless: `grep ... | wc -l` pipes into a counter. **No paths
are passed to a second command at all**, so word-splitting cannot occur.

Independent confirmation: a literal scan of those six files for `xargs`, `$(grep`, `$(rg`, `` `grep -l ``
and `` `rg -l `` returns **zero occurrences.** The files contain no shell pipeline of the risky form.

The remaining baseline entries are mine: `ERRATUM_002:75, :86` and `RELAY_PASTE_131:55` — the erratum and
relay that **document the bad pattern deliberately**, quoting it as the thing not to do. Also false
positives, and the funniest possible ones.

**TRUE POSITIVES IN THE BASELINE OF 18: ZERO.**

## 2. THE DESIGN FLAW, WHICH IS THE REAL FINDING

*** THE DETECTOR CANNOT CATCH THE DEFECT IT WAS BUILT FOR, AND WOULD NOT HAVE CAUGHT MINE. ***

My error was in a **command I executed in a shell**, not in a document. The detector inspects **committed
artifacts**. Those sets barely intersect. It can fire only when a lane records its command verbatim in an
artifact — which is good practice — so:

**THE CHECK PENALIZES LANES THAT DOCUMENT THEIR COMMANDS AND IS BLIND TO LANES THAT DO NOT.** That is
backwards, and it is the same failure class the corpus already names twice: `substring_certification` and
`cannot_fail_checks` — a check whose scope does not intersect the failure it claims to guard.

I asked for this detector in paste 131 without asking whether an artifact scanner could see an execution
defect. The lane implemented what was requested, correctly, and reported it honestly as flagging risk
rather than proving anything. **The specification error is mine.**

## 3. WHAT WOULD ACTUALLY CATCH IT

The control that would have caught my error is not a pattern match on text. It is the reporting rule I
already adopted in ERRATUM 002 for a different reason:

> **An intersection-valued bounded negative must report the FILE LIST, not only the count.**

My false claim was "12 / 16 / BOTH 0". An empty list printed beneath two non-trivial populations looks
wrong immediately; a bare `0` does not. That control acts at the moment of claim rather than at the moment
of commit, and it does not care how the number was computed.

**RECOMMENDED DISPOSITION, for the lane:**
1. **Restrict `GREP_L_SUBST_RE` to shell contexts** — `.sh` and `.py` files, where a backtick is a
   substitution — and stop scanning `.md`, where it is formatting. Keep the `xargs` arm, which is
   correctly scoped but should exempt lines whose surrounding window marks them as a quoted
   counter-example.
2. **Add a check with the right target:** an artifact stating an intersection-valued bounded negative
   (two populations and a shared count) must also contain a file list or an explicit "list empty"
   statement. That check inspects claims, which is where the defect becomes visible.
3. **Re-type the baseline from 18 to 0** with this artifact cited, rather than carrying 18 phantom risks.
   A noisy detector trains lanes to ignore it, which is worse than no detector.

## 4. THE LIMITATION, STATED PLAINLY — THIS SWEEP DOES NOT CLEAR THE PRIOR WORK

**The sweep returns clean, and NOT because prior bounded negatives were verified.** It returns clean
because the detector was not measuring the right thing. Those are different results and must not be
conflated.

**STILL OWED:** prior intersection-valued bounded negatives remain unverified. Finding them requires
reading each artifact's claims and identifying which are intersections of two searches — a semantic
question a regex cannot answer — then re-running those intersections null-safely. That is a real sweep,
it is still open, and this artifact does not perform it.

**Scale of what remains:** the program carries 223 re-scoped bounded negatives. I do not know how many are
intersection-valued and will not guess. The one I know was wrong was mine, caught by accident, within the
hour.

## 5. SCOPE

- Discharges no slot. Zero of eighteen remain derived.
- Computes nothing physical; compares nothing to any measured value.
- Does NOT retract any prior bounded negative. It establishes only that this detector does not impugn
  them.
- Does NOT criticize the lane's implementation, which matches what paste 131 requested and was reported
  with correct hedging ("flags risk, does not prove a false bounded negative").

`alpha_computed = false`; `proof_authorized = false`; `kappa_record_computed = false`.
