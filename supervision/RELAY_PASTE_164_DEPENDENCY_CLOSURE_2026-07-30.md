PASTE 164 — EINSTEIN — ITEM: WALK THE DEPENDENCY GRAPH TO ITS ROOTS

2026-07-30. Snapshot; later rulings override. **REGISTER HEAD AT ISSUE: Q-60.** If a ruling lands mid-run
that bears on your item, **report it rather than finishing against a stale set.**

```text
EINSTEIN (you) = the full transitive dependency closure of alpha    [relay 164]
CODEX 1        = free
CODEX 2        = the CTP_PHYS_INPUT_PACKAGE                         [relay 162]
```

**OFF LIMITS TO YOU:** do not open, specify, or attempt to build **any** object you find. This is a
**census**, not construction. Codex 2 holds `CTP_PHYS_INPUT_PACKAGE`; **you may record its existence and
its stated dependencies, but do not inspect its internals or duplicate its triage.**

Fences: never touch `a32_holdout/custodian_private/`. **Do not compute** alpha, kappa_record,
kappa_Thomson, a coupling, a radius, a scale, a root, an eigenvalue, or a beta function. **No comparison to
any measured constant.**

**Q-54:** every negative typed. **`NO_VERDICT` is legal.** A TYPE-S negative without its scope is void.

---

### WHY THIS, AND WHY IT IS OVERDUE

**The principal noticed the pattern.** Five times on 2026-07-30 the program localized its blocker, and each
time a new layer appeared underneath:

```text
the untyped source-record composition
  -> no: Gamma_K is the target
    -> no: Gamma_K cannot start; the response-extraction layer is upstream (Q-51)
      -> that layer needs CTP_PHYS_INPUT_PACKAGE -- nine more objects (Q-57)
        -> and C_R = 1 needs a scale bridge, a DIFFERENT upstream layer -- six more (Q-59, Q-60)
```

*** THAT IS NOT FIVE DISCOVERIES. IT IS ONE STRUCTURAL FACT APPEARING FIVE TIMES: EVERY ARTIFACT NAMES ITS
IMMEDIATE PREREQUISITE AND STOPS. NOBODY HAS EVER TRAVERSED TO THE ROOTS. ***

**So the program cannot currently answer "how deep is this?"** Each session rediscovers depth one level at
a time. **This is a census task and it is the largest fan-out available.**

### THE TASK

1. **BUILD THE GRAPH.** Every `derived = false | TYPE-U` in the sealed corpus is a node. **Its
   `would-build` field names its children.** Walk each chain backwards until you reach either (a) something
   `derived = true`, or (b) something with no stated `would-build` — **a leaf that names no path to its own
   construction.** *** TYPE-U flags predating Q-54 will lack `would-build` fields; record those as
   UNTYPED-LEAF and count them separately — do not guess their dependencies. ***

2. *** DOES IT BOTTOM OUT? *** Report, plainly: **how many distinct unbuilt objects exist; how deep the
   longest chain runs; how many leaves are UNTYPED-LEAF; and whether every chain terminates in something
   derived.** **If some chain does not terminate, say where it stops and why.**

3. *** IS THERE A CYCLE? *** **This is the question that changes the diagnosis.** If object A's
   `would-build` requires B, and B's requires A — directly or through any path — **the program is not deep,
   it is circular, and no amount of construction will close it.** **Report any cycle you find with its full
   path. A cycle is a far more serious finding than depth and must lead the report.**

4. **DO THE TWO KNOWN LAYERS CONVERGE?** Q-60 established the scale bridge (issue 1) and the
   response-extraction layer (issue 2) are **different**, with the bridge upstream, and conjectured they
   *may* share `CTP_PHYS_INPUT_PACKAGE`. **That conjecture is unverified — lane 1 was fenced from checking.
   Your graph settles it: do the two chains share any node?** Answer from the graph, **not from the
   conjecture.**

5. **WHAT IS THE CRITICAL PATH?** Given the graph, **which single unbuilt object unblocks the most
   downstream nodes?** That is where the next construction lane should go, and nobody currently knows what
   it is.

### CONSTRAINTS

- **A census, not a plan.** Do not recommend what to build beyond answering 5 from the graph.
- **Do not infer dependencies that are not stated.** An object whose `would-build` is silent is
  UNTYPED-LEAF, not a dead end — the distinction matters and guessing would corrupt the whole graph.
- **State your scope.** Roots searched, exclusions, queries. **A census with unstated scope is a TYPE-S
  negative and void.**
- **F-GK3:** declare any premise beyond the current stack at the outset.

---

REPORT BACK, with **EINSTEIN** on your first line: hashes, exact committed paths, gate verdict, the five
answers, **and every negative typed.** *** IF THERE IS A CYCLE, LEAD WITH IT. *** Otherwise lead with the
depth and the count. **The program has never known how much unbuilt work stands between it and a number;
after this it will.**

`alpha_computed = false; proof_authorized = false; kappa_record_computed = false.`
