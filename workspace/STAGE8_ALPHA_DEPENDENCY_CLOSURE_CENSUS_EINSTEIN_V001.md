# The Full Transitive Dependency Closure of Alpha: Census (EINSTEIN) V001

LANE: EINSTEIN. CHARTER: relay 164. DATE: 2026-07-30. REGISTER HEAD AT ISSUE: Q-60; **HEAD AT
EXECUTION: Q-61** (the paste-163 zero-live-pairs registration landed before this census began;
no Q-62+ exists as of the final graph run). STATUS: LANE CENSUS. A census, not a plan; nothing
opened, specified, or built.

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
F-GK3: no premise beyond the sealed stack. The graph analysis (cycle detection, depth,
reachability) is DETERMINISTIC CODE run over EXTRACTED SEALED STATEMENTS — no judgment enters
after extraction, and no edge exists that sealed text does not literally state.
FENCES: CTP_PHYS_INPUT_PACKAGE recorded by existence + stated dependency surface ONLY (its
header flags and register text); its 34 internal would-build markers NOT enumerated; Codex 2's
triage NOT duplicated. a32_holdout/custodian_private/ not opened (verified: no such path exists
under supervision; grep pipelines excluded it defensively). Nothing computed, no
measured-constant comparison.
```

---

## §0 — THE FIVE ANSWERS

```text
*** NO CYCLE EXISTS. *** (Q3 — the lead-with condition does not fire.) Zero strongly-connected
components of size > 1 and zero non-test self-loops over all 122 stated construction edges. THE
PROGRAM IS DEEP, NOT CIRCULAR. One "Circular until..." phrase exists in sealed prose
(EXECUTION_TRACKER:67, the C_R falsifier) and it is a TEST-gating loop — "cannot TEST until
built" — which is the known Q-52 problem, NOT a build cycle. The distinction was enforced in
the analysis: test/would-execute edges were excluded from cycle detection by kind.

1. THE GRAPH: 172 distinct named unbuilt objects on the typed graph — 82 sealed identifiers +
   90 prose-named targets that appear ONLY as would-build children (leaves that name no path).
   122 stated edges (112 build, 6 release, 4 ordering; test edges tracked separately). PLUS the
   untyped mass, counted separately per the charter: ~1,050 pre-Q-54 "derived = false" flag
   lines ≈ 350 distinct identifiers with no would-build (UNTYPED-LEAF).
2. DOES IT BOTTOM OUT? *** IT BOTTOMS OUT IN UNBUILT LEAVES, NOT IN DERIVED GROUND. NO WALKED
   CHAIN TERMINATES IN ANYTHING derived = true. *** Longest stated chain: DEPTH 5 —
   Gamma_K -> raw-correlator map -> CTP_PHYS_INPUT_PACKAGE -> its premises (P1..P8) -> their
   would-build targets. Depth is a LOWER BOUND twice over: the package's internals are fenced
   (Codex 2's), and 90 chains end at prose-targets because nothing further is STATED.
3. CYCLES: ZERO (lead, above).
4. CONVERGENCE: *** THE TWO LAYERS SHARE ZERO NODES ON STATED EDGES. *** The Q-60 conjecture
   (the bridge "may share" CTP_PHYS_INPUT_PACKAGE) is NOT SUPPORTED by any stated edge — the
   graph, not the conjecture, answers: TYPE-S bounded (§4).
5. CRITICAL PATH: *** THERE ARE TWO, AND THEY ARE DISJOINT — WHICH IS ITSELF THE FINDING. ***
   Response side: CTP_PHYS_INPUT_PACKAGE (through P1-P8) transitively unblocks the most stated
   downstream nodes (the map, all four Q-51 objects, Gamma_K/C_record — 7 stated ancestors
   each at the P-row targets). Bridge side: the six Q-59 objects unblock the selector chain and
   NOTHING on the response side. Since they share nothing, THEY CAN PROCEED IN PARALLEL — and
   Codex 2 already sits on the response side's head, while the bridge side's head is currently
   UNASSIGNED (Codex 1 is free).
```

---

## §1 — QUESTION 1. THE GRAPH, BUILT

**Method.** Extraction (two agents, two adversarial verifiers; 34/35 and 23-point spot checks
verbatim, one phantom node corrected — `T1_through_T7` does not exist, the identifier is
`T1_through_T8` — missed edges and alias verdicts folded in), then deterministic assembly.
**Linking was conservative by construction:** an edge exists iff (a) exact identifier match,
(b) a verifier-noted explicit correspondence (the four Q-51 children to their four flags;
P1–P8 short refs to their table rows), or (c) unique ≥5-token prefix containment. Everything
else became a **prose-target node** — never a guessed link. **No inferred edge exists in the
graph.**

```text
NODES 172 = 82 sealed identifiers + 90 prose-targets      EDGES 122 (112 build / 6 release /
4 ordering; would-execute/test edges excluded from construction analysis by kind)
MIRRORS: all 600 shared workspace/cleanroom relpaths byte-identical (cmp); recorded once.
CLEANROOM-ONLY: exactly one .md — Codex 2's package triage (existence + header flags only).
CORPUS DRIFT DURING CENSUS, recorded: STAGE8_KAPPA_RECORD_KSTAR_PAIR_TEST_UNDER_Q61_V001.md
landed 18:40 with ~10 new typed flags (its same-object question adjudicated NO_VERDICT — the
corpus itself refusing an unstated merge); its flags are IN the node set via the verification
pass. Head still Q-61 at the final graph run.
```

**Alias discipline, and the census's own near-miss.** Four unresolved alias candidates are
carried UNMERGED with evidence both sides (notably `C_R_marginal_selector_derived_rather_than_
adopted` vs `marginal_closure_condition_derived_rather_than_assumed` — same file, both TYPE-C,
no sealed equation; and the Q-51 "complete BR/CTP fluctuation-response operator" vs the
raw-correlator spec's `finite_operator_bundle_to_complete_BR_CTP_response_extension_derived`).
**And one demonstration that the discipline is load-bearing: this census's first convergence
run reported 43 shared nodes — ALL FALSE, produced by a seed regex in which `C_R` substring-
matched `C_record`.** Caught by path-tracing before anything was reported; the corrected
word-boundary run gives the §4 answer. The program's aliasing disease bites tooling too.

---

## §2 — QUESTION 2. IT BOTTOMS OUT — IN THE WRONG THING

```text
DISTINCT UNBUILT OBJECTS:  172 named on the typed graph (+ ~350 untyped legacy identifiers,
                           counted separately, never walked, possible referent overlap with
                           the 172 NOT adjudicated — merging without sealed equations is
                           forbidden).
LONGEST STATED CHAIN:      5 —
  Gamma_K / C_record(K)
    -> raw_correlator_to_retarded_Hessian_map     [the one Q-51 object now SPECIFIED]
      -> CTP_PHYS_INPUT_PACKAGE                    [Q-57; Codex 2's]
        -> P1..P8 premises                         [each derived = false | TYPE-U]
          -> their would-build targets             [prose-targets; nothing further stated]
UNTYPED-LEAF (pre-Q-54, no would-build field):  ~350 distinct / ~1,050 lines, by file class:
  spec 197 · result 200 · determination 48 · register 41 · other 564 (lines, before identifier
  aggregation; workspace 911 / supervision 138 / cleanroom-only 1).
LEAVES THAT NAME NO PATH:  90 prose-targets + 27 sealed identifiers with no stated would-build
  of their own. THE CHARTER'S "(b)" CLASS INCLUDES THREE LITERALLY-REQUIRED PATHLESS NODES at
  identifier level (children of C_R_equals_1_truth_status's blocked_by), one of which is the
  unresolved alias above — if the alias resolves, its release exists; if not, it is a required
  node with no stated path.
*** TERMINATION VERDICT: EVERY CHAIN TERMINATES — NONE IN A DERIVED OBJECT. The graph is
finite and acyclic and ITS ENTIRE BOUNDARY IS UNBUILT. Nothing stated connects any chain's
bottom to derived = true ground. ***
```

## §3 — QUESTION 3. NO CYCLE

```text
SCCs of size > 1: ZERO. Non-test self-loops: ZERO. (Tarjan over build+release+ordering.)
THE ONE CIRCULARITY IN SEALED PROSE IS A TEST LOOP, NOT A BUILD LOOP: "A test for C_R = 1 —
designable (paste 154) but gated on the unstartable object. Circular until..."
(EXECUTION_TRACKER:67). C_R = 1's FALSIFIER needs the response-side object; C_R = 1's
CONSTRUCTION does not. Cannot-test-until-built is the Q-52 problem the program already named.
NO CONSTRUCTION DEADLOCK EXISTS ON STATED TEXT.
CAVEAT, honestly: a cycle could hide inside (i) the fenced package internals, (ii) the 90
pathless prose-targets, or (iii) an unresolved alias (a true merge can create an edge). The
verdict is NO CYCLE ON STATED, LINKABLE TEXT — TYPE-S, scope in §6.
```

## §4 — QUESTION 4. THE TWO LAYERS DO NOT CONVERGE ON STATED EDGES

```text
Seeds (word-boundaried, verified by hand against the seed list printed at run time):
  BRIDGE:   the Q-59/Q-60 chain — C_R = 1 selector, the six bridge objects, Misner-Sharp /
            Brown-York / HJ-conjugate-energy selection flags, marginal-closure nodes,
            absolute_record_interval (branch form).
  RESPONSE: the Q-51/Q-57 chain — Gamma_K, the four upstream objects, the map, the package,
            P1..P8, scalarization, operator bundle.
DOWNWARD CLOSURE OF EACH, INTERSECTED: *** ZERO SHARED NODES. ***
=> Q-60's "may consume CTP_PHYS_INPUT_PACKAGE" CONJECTURE IS UNSUPPORTED BY ANY STATED EDGE:
   nothing in the six bridge objects' stated would-builds names the package, any P-row, or any
   response-side object. TYPE-S: the absence claim is scoped to STATED dependency text in the
   three roots as of Q-61; it does NOT prove the layers are physically independent — it proves
   NOBODY HAS STATED a shared prerequisite. (First run's 43 false positives: §1.)
CONSEQUENCE: the two blocking layers are SEPARABLE WORKSTREAMS on current sealed text.
```

## §5 — QUESTION 5. THE CRITICAL PATH — THERE ARE TWO

```text
BY TRANSITIVE UNBLOCK COUNT (stated edges only):
  RESPONSE SIDE: the package's P1-P8 premises and their targets each carry the maximum stated
  ancestor set (7): completing CTP_PHYS_INPUT_PACKAGE unblocks the map; the map plus the other
  three Q-51 objects unblock Gamma_K / C_record(K); Gamma_K unblocks the S9-A/SP4
  overdetermination target and O-SC1's ordering gate. *** THE PROGRAM'S EXISTING ASSIGNMENT
  (CODEX 2 ON THE PACKAGE) IS ALREADY SITTING ON THIS PATH'S HEAD. THE CENSUS CONFIRMS RATHER
  THAN REDIRECTS. ***
  BRIDGE SIDE: the six Q-59 objects (Lorentzian CTP action/boundary/time-flow data; constant
  HJ energy on the stationary cell; branch-energy = gravitating-closure-energy equality;
  reference subtraction / no-spectator theorem; derived marginal first durable/public closure;
  one isolated stable positive interval solution) unblock the SELECTOR chain — C_R = 1's
  consummation, hence every absolute-scale claim — and NOTHING on the response side.
ANSWER TO "WHICH SINGLE OBJECT UNBLOCKS THE MOST": on stated edges, THE PACKAGE — but the
census's more useful sentence is that THE BRIDGE CHAIN IS A SECOND, DISJOINT CRITICAL PATH
WHOSE HEAD IS CURRENTLY UNASSIGNED (Codex 1 is free), and nothing on stated text forces the
two to wait for each other.
(A census, not a plan: no recommendation beyond this graph fact.)
```

## §6 — SCOPE AND TYPED NEGATIVES

```text
SCOPE (a census with unstated scope is void): roots = archive workspace (604 .md), supervision
(200 .md), cleanroom (601 .md; 600 byte-identical mirrors + 1 Codex-2 file, header-only);
exclusions = a32_holdout/custodian_private (nonexistent under supervision, defensively
excluded), package internals (fence), both Codex lanes' live work; queries = derived=false
variants, TYPE-U, would-build/would-execute all forms with 2-line continuation lookahead,
prose forms ("to become live", "requires first", "gated on", "cannot start until", "selects
only after", "prerequisite", "upstream of", "must exist before"), blocked_by/NO_VERDICT
chains; verification re-ran with independent patterns and found 8 missed-edge classes, ALL
FOLDED IN. As of register head Q-61.
N1 [TYPE-R, lead] NO CYCLE on stated construction edges — refutation of the circularity
   hypothesis at the stated-text level (caveats in §3 are TYPE-S residue, not hedges).
N2 [TYPE-S] Zero shared nodes between the two layer chains (§4 scope).
N3 [TYPE-S] No walked chain terminates in derived ground (§2; scoped to stated edges).
N4 [TYPE-U] Depth below the package's P-rows: unbuilt/fenced — the depth-5 figure is a floor.
N5 [NO_VERDICT] The three literally-required pathless identifiers (§2): whether the alias
   resolves is the custodian's; both branches recorded.
N6 [TYPE-S] "T1_through_T7_execution_completed" DOES NOT EXIST — phantom corrected to
   T1_through_T8 (grep: zero corpus occurrences of the phantom).
N7 [TYPE-C, cited] The package's completion is gated as Codex 2's assignment (fence), release:
   Codex 2's delivery — recorded as lane structure, not physics.
```

## §7 — DISCIPLINE

```text
CENSUS ONLY. Nothing opened, specified, built, or recommended beyond §5's graph fact. No
dependency inferred anywhere — 90 would-build children remain prose-targets rather than
guessed links, and four alias candidates remain unmerged with evidence both sides. The
package's internals were not read past its header status block by any agent (verified by the
fence audit; one mislabel — "triage internals" for a header-visible flag — corrected). The
graph analysis is reproducible: node records and edge rules are mechanical, and the final
counts were re-derived after the seed-regex correction was caught by path-tracing.
alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
```
