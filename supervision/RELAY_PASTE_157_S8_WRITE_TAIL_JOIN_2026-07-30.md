PASTE 157 — CODEX 1 — ITEM: SPECIFY AND TEST THE S8 WRITE-TAIL JOIN

2026-07-30. Snapshot; later rulings override. **REGISTER HEAD AT ISSUE: Q-54.** If your work consults
rulings later than Q-54, say so; if a ruling lands mid-run that bears on your item, **report it rather than
finishing against a stale set.** Three artifacts went stale that way today.

```text
CODEX 1  (you) = specify and test the S8 write-tail join            [paste 157]
CODEX 2        = idle — awaiting assignment
EINSTEIN       = idle — enumeration audit returned (Q-53)
```

Fences unchanged. Never touch `a32_holdout/custodian_private/`.

---

### TWO RULE CHANGES THAT APPLY TO YOU FROM NOW ON

**1. Q-52 — NO CONSTRAINT MAY PREVENT A TEST.** *** THE STANDING INSTRUCTION NOT TO SUPPLY WHAT IS ABSENT
IS WITHDRAWN WHERE THE PURPOSE IS A TEST. *** You may now write a specification for a missing object,
provided it is **declared at the outset, marked `derived = false`, and never reported as derived.**
`Gamma_K` is no longer the sole construction target.

**2. Q-54 — EVERY NEGATIVE CARRIES A TYPE.** Bare `= false` is no longer a finding. Use:

```text
foo_derived = false | TYPE-U | would-build: <what would construct it>
bar_found   = false | TYPE-S | roots: <...> | excl: <...> | fences: <...> | query: "<...>"
baz_holds   = false | TYPE-R | test: <the test that ran and failed>
qux_checked = false | TYPE-C | constraint: <name> | release: <condition or NONE WRITTEN>
```

**TYPE-R refuted — the ONLY type that is physical content. TYPE-U unbuilt. TYPE-S scope-empty. TYPE-C
constraint-blocked.** A TYPE-S negative without its scope is void. Terminal fence declarations are exempt.

*** AND `NO_VERDICT` IS NOW A LEGAL ANSWER. *** If a test's failure condition rests on premises that are
untested, inapplicable, or themselves unbuilt, **return NO_VERDICT and say which premise blocked it.** Do
not manufacture a failure from an inapplicable requirement. **A negative now carries the same evidentiary
burden as a positive: reporting "not found" requires stating the search.**

---

### THE ITEM

Einstein's audit (Q-53) found that theory candidate 001's chain has ~12 stages where the candidate named
four, and that **stage S8 — the physical write-tail join — is covered by no closure and closed by no other
ruling.** Recorded as OBS-07.

```text
physical_write_tail_join_derived = false | TYPE-U
exchange_magnitude_derived       = false | TYPE-U
```

*** WHAT MAKES IT INTERESTING: EXACTNESS HOLDS ONLY "FOR FIXED INTEGRATED ACTION" — WHICH IS A
MAGNITUDE. *** Every other site in the chain was closed by something that FORBADE a strength. This one is
not forbidden. It is unbuilt, and there is a magnitude sitting in it.

1. **WHAT IS THE WRITE-TAIL JOIN, AS SEALED TEXT HAS IT?** At file:line. Its type, its domain, what it
   joins to what, and where the "fixed integrated action" qualifier enters.

2. **IS THE EXCHANGE MAGNITUDE FREE, OR DETERMINED UPSTREAM?** This is the whole question. **If free, the
   theory's negative half is refuted and a coupling could live at S8. If determined upstream, name what
   determines it.** Answer by what the equations require, not by what surrounding prose asserts.

3. **UNDER Q-52 YOU MAY NOW SPECIFY IT IN ORDER TO TEST IT.** If a specification is needed to decide
   question 2, write one — **declared, `derived = false`, never reported as derived.** State every premise
   you add at the outset (F-GK3).

4. **WHAT WOULD FALSIFY YOUR ANSWER?** Attach the test. If none can be designed, say so and say why — that
   is a finding, not a failure.

### CONSTRAINTS

- **Do not compute** alpha, kappa_record, kappa_Thomson, a coupling, a radius, a scale, a root, an
  eigenvalue, or a beta function. **Do not evaluate a response or solve for `K_*`.**
- **Report refutations; never repair them.** If S8 refutes theory 001's negative half, report that — the
  candidate exists to be cheap to kill.
- Do not touch Codex 2's or Einstein's artifacts, or the reviewer's registers.

---

REPORT BACK, with **CODEX 1** on your first line: hashes, exact committed paths, gate verdict, the four
answers, **and every negative typed.** **If the exchange magnitude is free, LEAD WITH IT** — that would be
the first refutation of the theory's negative half, and it is worth more today than tomorrow.

`alpha_computed = false; proof_authorized = false; kappa_record_computed = false.`
