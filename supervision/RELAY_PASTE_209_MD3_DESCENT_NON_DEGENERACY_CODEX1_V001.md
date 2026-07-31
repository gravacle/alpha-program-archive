PASTE 209 — CODEX LANE 1 — WRITE MD-3, THE `B0` ACCEPTANCE TEST

ROAD: **UNBLOCKS STEP 1.** Step 1's foundation is `B0`. MD-3 is the test that decides whether any
candidate `B0` may be accepted. Without it, a correct construction cannot be recognized and an
incorrect one cannot be rejected. It is blocked behind nothing and it has been on no blocker list
since relay 203.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false;
coupling_evaluation_authorized = false; production_authorized = false.

---

## 1. THE SITUATION, STATED PLAINLY

Six routes have now asked what determines `B0` and all six returned nothing: accessor (Q-106),
codomain (Q-110), primitive (Q-111), historical (Q-112), joint (Q-113), incidence (Q-114).

*** BUT THE DEEPER FINDING IS NOT THAT `B0` IS UNBUILT. IT IS THAT `B0` IS **UNPINNED**. *** Relay
203 established that no test the corpus can run — **and none in the sealed battery even after every
named blocker lands** — could distinguish a real `B0` from an object that does no work at all.

**The countermodel that makes this concrete is CM-3**, the opaque-carrier constant-descent root. It
survived relay 208's combinatorial attack: a candidate may carry the full incidence skeleton of a
designated complex **as declared internal data** and remain indiscriminable, because CM-3 constrains
only the outgoing constant descent maps and says nothing about the atom's interior.

**The missing discriminator has a name: MD-3, `B0_DESCENT_NON_DEGENERACY`.** It is a wiring
obligation on an existing named interface. **Write it.**

---

## 2. THE TASK

**Specify MD-3 as an executable acceptance test.** At minimum it must state:

```text
2.1  WHAT IT CONSUMES     the candidate B0, and which of its descendants are probed
2.2  THE NON-DEGENERACY   the precise sense in which descent must be non-constant --
     CONDITION            i.e. that varying the candidate varies what descends
2.3  THE DISCRIMINATION   the exact step at which CM-3 fails the test, quoted against
     CLAIM                CM-3's own statement in relay 203
2.4  WHAT IT DOES NOT     it is an ACCEPTANCE test, not a construction. It must not
     CLAIM                smuggle in a uniqueness theorem it has not proved.
```

*** IT MUST DEFEAT CM-3 EXPLICITLY OR SAY IT CANNOT. A test that CM-3 passes is not a
discriminator, and reporting that honestly is the correct result under Q-92. ***

---

## 3. THE SECOND QUESTION, WHICH IS THE SAME OBJECT FROM THE OTHER SIDE

Q-113 named a residual fiber: `IprimPresentedCodomainCompatibleBoundaryOriginRealizer` — the set of
realizers consistent with everything the algebraic routes fixed (0/9 collapse, 3/9 shrink, **0/9
conflict**).

> **DOES THAT FIBER ACT ON THE ROAD? Do two distinct realizers in it produce different
> `C_record(K)`, or the same one?**

**These are one test.** Descent non-degeneracy asks whether a candidate `B0` does downstream work;
the fiber question asks whether distinct realizers are downstream-distinguishable. **Answer them
together.**

*** AND THE CONSEQUENCE IS SYMMETRIC — REPORT WHICHEVER YOU FIND, WITH EQUAL WILLINGNESS: ***

```text
IF DESCENT IS NON-DEGENERATE   the fiber ACTS. B0 genuinely must be pinned, MD-3 becomes a
                               hard gate on every future construction, and the road is
                               correctly blocked where we think it is. LEAD WITH IT.

IF DESCENT IS DEGENERATE       distinct realizers give the same C_record. Then B0's
                               underdetermination is GAUGE, not a gap -- and six routes have
                               been measuring a quantity that does not act. THIS WOULD BE THE
                               LARGER RESULT. LEAD WITH IT.
```

**Neither outcome is the one this relay wants.** If the evidence is mixed, or the test cannot be
made executable, say so and name what is missing — that is a complete answer under Q-92.

---

## 4. RULES THAT APPLY

- **Q-54 typing on every negative:** TYPE-R refuted · TYPE-U unbuilt · TYPE-S scope-empty · TYPE-C
  constraint-blocked. `NO_VERDICT` is legal. **Only TYPE-R is physical content.**
- **Q-80:** if something fits no existing class, name a new one — **but relay 208 found the existing
  vocabulary sufficed and struck four manufactured classes. Do not manufacture a fifth to avoid a
  plain answer.**
- **Q-69:** never identify a flag with the object that discharges it.
- **Word-boundaried matching only.** Substring and name matching have produced false positives in
  the corpus, in the audit script, in the audit of the audit, and in the register.
- **Report search scope** — roots, exclusions, and the queries actually run.

## 5. FENCES — VERBATIM, NON-NEGOTIABLE

- **Never touch `a32_holdout/custodian_private/`.**
- **Do not compute** alpha, `kappa_record`, `kappa_Thomson`, a coupling, a scale, a root, an
  eigenvalue, a beta function, `E_R`, `T_R`, `k_R`, or any absolute interval.
- **No comparison to any measured constant.**
- **Do not resolve the Misner-Sharp / Brown-York fork by choosing — it must be DERIVED.**
- **Report refutations; never repair them.**

## 6. CUSTODY (Q-91)

*** NO LANE RUNS ANY GIT COMMAND. *** Write the artifact in the cleanroom, compute its
`.seal.sha256` sidecar and **verify it matches**, mirror artifact + sidecar to
`alpha-program-archive/workspace/`, report hashes and paths, and **stop**. You may run
`corpus_check.py --report` on your own artifact; `--gate` is not your concern and **a red gate is
never a reason to stop working.** The reviewer verifies, baselines, commits and pushes.

alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
