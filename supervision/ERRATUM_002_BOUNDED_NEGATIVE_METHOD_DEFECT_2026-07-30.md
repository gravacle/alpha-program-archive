# ERRATUM 002 — A BOUNDED NEGATIVE IN Q-18 IS RETRACTED, AND THE METHOD THAT PRODUCED IT IS DEFECTIVE

Reviewer lane, 2026-07-30, issued within the hour of the error. Self-caught during the slot-1 wiring
check, before any downstream artifact consumed the figure.

## 1. WHAT IS RETRACTED

`RESULT_FLOOR_BOUNDARY_VALUE_SETTLED_2026-07-30.md` §2 and register row Q-18 both stated:

> "files mentioning a lower endpoint / lower limit / lower proper-time boundary: **12**; files mentioning
> `lambda_0`: **16**; files mentioning **BOTH: 0**. The two objects have never appeared in the same file,
> in either direction."

**THE FIGURES ARE WRONG AND THE CONCLUSION DRAWN FROM THEM IS FALSE.** Corrected, null-safe:

```
lower endpoint / lower limit / lower proper-time boundary:  16 files
lambda_0:                                                  19 files
BOTH:                                                       7 files
```

The seven: `STAGE8_OPERATOR_FLOOR_BOUNDARY_CHAIN_CANDIDATE_DERIVATION_V001.md`,
`BOHM_TWO_STEPS_WORKFLOW_RESULTS_2026-07-28.md`, `CONTINUATION_STATE.md`,
`QUESTIONS_SETTLED_REGISTER_V001.md`, `RELAY_PASTE_127_OPERATOR_FLOOR_CHAIN_2026-07-29.md`,
`RESULT_FLOOR_BOUNDARY_VALUE_SETTLED_2026-07-30.md`,
`TEST_RESULT_OPERATOR_CHAIN_AND_PARAMETRIZATION_2026-07-29.md`.

**RETRACTED SENTENCE:** "The two objects have never appeared in the same file, in either direction. The
chain that links them is asserting a connection between two things no artifact in the program has ever
discussed together." That is false. The operator-floor chain discusses them together at length — it is
what the chain IS — and I was reading that chain when I formed the argument.

## 2. WHAT SURVIVES, AND WHY IT SURVIVES MORE STRONGLY THAN BEFORE

**THE SETTLEMENT'S CONCLUSION IS UNAFFECTED. IT NEVER RESTED ON THE COUNT.** The deciding argument is
mathematical and stands on its own:

> The capacity condition constrains the BOTTOM of the spectrum, which governs LARGE `s` in
> `STr' exp(-s L)` and supplies infrared decay `exp(-s lambda_0)`. The proper-time floor cuts SMALL `s`,
> where the `F^2` logarithm lives. `exp(-s L)` is well defined and nonvanishing for every `s > 0`
> regardless of where the spectrum starts, so no value of `lambda_0` can empty the small-`s` range.

Unchanged: the type mismatch; that the chain cannot be completed by discharging its named gaps; the
corpus's own honest flags (`proper_time_floor_status = ADOPTED_BY_INDUCED_ONLY_FUNCTIONAL`,
`gamma_at_floor_zero = DERIVED_GIVEN_FLOOR`); the induced-only axiom's "**states**"; alpha's
conditionality equalling that axiom's status; slot 18's epistemic role; and repair condition F-FL1.

**AND THE CORRECTION MAKES THE FINDING MORE CONSEQUENTIAL, NOT LESS.** On the false reading, the type
mismatch was a gap nobody had noticed in an unexamined corner. On the true reading, it is **a defect in
an actively-cited chain that two lanes have worked and that a relay paste carried** — one that reasons
about both objects explicitly and still crosses the ends of the integral. A defect inside live work is
worth more than a gap in dead ground.

The second bounded negative in the same section — that no artifact distinguishes the small-`s` from the
large-`s` end of this integral — was computed by a direct grep, not the defective pattern, and re-runs
clean: 3 files, of which one is this settlement, one is Codex's O-SC1 inventory written after and from
paste 130, and one (`xi_ep_original_derivation_v001.md:3152`) uses "infrared endpoint" for a different
object entirely (where exterior charge becomes a durable record). **That claim stands.**

## 3. THE METHOD DEFECT, AND IT GENERALIZES BEYOND THIS ERRATUM

**CAUSE:** the intersection was computed by piping a file list into a second `grep` via `xargs`. **Both
program roots contain spaces** — `/Users/bgm/Documents/New project/...` and `/Users/bgm/MB Work/...`.
`xargs` splits on whitespace by default, so every path was fragmented into non-existent filenames, every
inner `grep` matched nothing, and **the pipeline reported zero intersection while exiting successfully.**

*** THIS FAILS SILENTLY AND IT FAILS TOWARD "ZERO HITS", WHICH IS THE DIRECTION THAT MANUFACTURES
BOUNDED NEGATIVES. *** A bounded negative is an assertion that something is absent. This defect produces
exactly that assertion, with no error, from a correct-looking command.

**SCOPE OF THE RISK — STATED, NOT MEASURED.** The reviewer lane has produced many bounded negatives, and
the program carries 223 re-scoped ones. I do not know how many were computed with a piped path list; I am
not going to guess. What is certain: **any bounded negative in this program whose value is an
INTERSECTION of two searches, computed by piping paths, is suspect and must be re-run.** Single-pass
`grep -rl` and `grep -rn` results are unaffected.

**THE CORRECT PATTERN**, for any lane computing an intersection over these roots:

```
grep -rlZ <opts> -e PATTERN_A ROOT1 ROOT2 | tr '\0' '\n' | sort -u > A.txt
grep -rlZ <opts> -e PATTERN_B ROOT1 ROOT2 | tr '\0' '\n' | sort -u > B.txt
comm -12 A.txt B.txt          # and report the file list, not only the count
```

**RECOMMENDED corpus_check DETECTOR (for the lane):** flag any script or recorded command that pipes a
path list into a second search without null delimiting — `xargs` without `-0`, or `$(grep -l ...)` word
splitting — when the search roots contain spaces. This is the same class as the two defects already
detected: substring certification and cannot-fail checks. It is a check that cannot fail *loudly*, which
is why it needs a detector rather than care.

**AND REPORT THE FILE LIST, NOT ONLY THE COUNT.** Had the retracted claim been stated as "BOTH: 0, list
empty" next to a 12 and a 16, the emptiness of the list against two non-trivial populations would have
looked wrong immediately. Counts hide what lists expose.

## 4. THE SLOT-1 WIRING HYPOTHESIS IS WITHDRAWN

The check that caught this was run to test a hypothesis I raised: that `T_R` might not be wired to the
coupling at all, which would have removed slot 1 from the critical path and reduced Q-13's four
scale-breakers to three. **The hypothesis has no support and is withdrawn.** Null-safe, roots as above,
types md/json/csv/py:

```
T_R    934 files   with kappa_record|kappa_Thomson|alpha_micro: 187   with K_Q|K_R|K_H:  86
k_R    173 files   with kappa_record|kappa_Thomson|alpha_micro:  27   with K_Q|K_R|K_H:  58
```

The apparent zeros were the same defect. **Slot 1 remains typed as Q-13 typed it**, and the question
"does `T_R` reach the coupling?" is not answered by co-occurrence either way — co-occurrence was never
evidence of a derivational path, which I said when I raised it. If the question is worth answering it
needs an actual dependency trace, not a grep.

**WHAT DOES STAND FROM THE SLOT-1 WORK**, because it came from reading rather than counting:
1. The `sqrt(2)` is not a convention fork. The gate: the diamond "is declared to be the support of a CTP
   history difference, not a material timelike boundary. Therefore neither finite-boundary Brown-York
   energy nor asymptotic ADM/Misner-Sharp energy is automatically the Hamiltonian conjugate to the local
   tip-to-tip proper interval." Both candidates are the wrong TYPE; the required object does not exist.
2. `E_BY/E_MS = 2/[1+sqrt(1-C)]`, which is 1 at `C = 0` and exactly 2 at `C = 1`. **The ambiguity is
   maximal precisely at the adopted marginal selector and vanishes as `C -> 0`** — its size is a function
   of an adopted premise, so closure items 2 and 6 of the gate are not independent.

## 5. DISPOSITION

- Erratum pointers appended to `RESULT_FLOOR_BOUNDARY_VALUE_SETTLED_2026-07-30.md` and to register row
  Q-18. Both re-sealed after the append; no prior bytes rewritten.
- **THE GOVERNING CHAIN IS CLEAN.** `STAGE8_Q13_Q19_GOVERNING_REGISTRATION_RECORD_V001.md` registered the
  type-mismatch argument, the operational consequence, the axiom quote, the conditionality finding and
  F-FL1 — **and did not carry the counts.** Verified by direct search: zero occurrences of the retracted
  figures or phrasing anywhere in the cleanroom. No erratum is owed in the governing chain for the
  figures themselves.
- Owed to the lane via relay: the detector recommendation, and the standing intersection pattern.
- Paste 130's item 6 carried the retracted figures in its text. It has been sent and consumed; Codex did
  not propagate them. Recorded here rather than by amending a sent paste.

## 6. WHAT THIS COSTS AND WHAT IT BUYS

Cost: one retracted sentence in a sealed artifact, and a rhetorical claim that overstated the finding's
novelty. The physics is untouched.

Buys: a named, detectable, silent failure mode that manufactures false absences in a program whose
central instrument is the bounded negative — found by the lane that made the error, within the hour,
because a second check was run against a suspicious result rather than around it.

`alpha_computed = false`; `proof_authorized = false`; `kappa_record_computed = false`.
