# STAGE 8 / 7A / STEP 8 — TAU_DENSITY AS A CARRIER, AND THE MATRIX RE-RUN

**Lane:** Dario (Opus 5, cross-family from the Codex build lanes)
**Date:** 2026-08-08
**Scope:** PASTE 722 only — GG1 define, GG2 re-run, GG3 verdict, GG4 ledger
**Custody:** archive-side read and write; the registrar owns any mirror
**Governing:** frozen prereg `9f0d12b4…`; carrier `5f4979d5…`; my 719 hunt `961a76c4…`
**Charge:** re-derive, not trust. Nothing adopted; the principal rules on the result.

## Lead determination

```text
VERDICT = DEFINITION-INCOMPLETE (two gaps named; tau_density stays untestable)

WHAT I FOUND, AND IT IS MORE THAN I EXPECTED:
  The corpus DOES supply the density-convergence notion, and as a genuine
  COMPLETE topological carrier -- locally uniform convergence on a polydisc for
  intensive logs gamma_K := -Log Ghat_K / N_4(K), complete by Montel and
  limit-preserving by Vitali-Porter.  It is sealed, it is precise, and my 719
  artifact was wrong to imply nothing of the kind existed.

WHY IT STILL DOES NOT DEFINE tau_density:

  GAP 1 -- THE INDEX.  The sealed instance is indexed by "the relayed
  causally-sequential EXHAUSTION" (growing volume).  tau_density is defined by
  4d as density convergence "over C_ref" -- the REFINEMENT family.  The schema
  mentions C_ref zero times.  Supplying that index is exactly RA27-2's
  same-region relation.  THE SAME MISSING OBJECT AS EVERYTHING ELSE ON THIS
  THREAD.

  GAP 2 -- THE CARRIER CLASS, and this one reframes the question.  The sealed
  instance carries intensive DENSITIES (holomorphic functions on a polydisc).
  tau_norm and tau_cyl are topologies on the ratified operator COMPLETION.
  These are not three topologies on one object.  If tau_density is a topology
  on a different carrier, then R3/R5/R6 -- all properties of the completion
  class -- do not straightforwardly APPLY to it, and "choose one of three" is
  under-posed as a question.

NEW_REQUIRE = 1.  The definition work surfaced a hard adoption fence (S5.3):
  any attempt to DISCHARGE the density-convergence hypothesis is BLOCKED.
  Tested against both survivors at §2.2.  It disqualifies neither.
```

---

## 0. Preflight

[PROVABLE] `relay_outbox/722_ACK.md` was written **before** source work. The relay
header names **DARIO**; lane guard satisfied. Read only after its sidecar verified:

```text
relay_inbox/RELAY_PASTE_722_TAU_DENSITY_CARRIER_DARIO_V001.md
  cea4e0f81d1338136275a697fd40b41bba64a6a327f8277faead48e08f85471e   shasum -c OK
```

[PROVABLE] `STAGE8_7A_TAU_DENSITY_CARRIER_DARIO_V001.md` and its seal sidecar were
probed before the write and returned ABSENT.

### 0.1 Sources verified before use

```text
DUH   STAGE8_T7_COMPLETED_CONDITIONED_DUHAMEL_IDENTITY_AND_INTERCHANGE_SCHEMA_SPEC_V001.md  4fe8d42d…
4d    STAGE8_TASK4D_STITCHING_THEOREM_GERM_INDEPENDENT_HALF_V001.md   430f0971…
V011  review_packets/.../BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md aa7c6d49…
CPKG  STAGE8_TASK5_CONTINUUM_PACKAGE_ADOPTION_PROPOSAL_LANE2_V005.md  09883a0d…  PROPOSED_NOT_ADOPTED
RT2   STAGE8_ROUTE2_RESPONSE_INVARIANT_CONVERGENCE_RESUMMATION_DETERMINATION_V001.md d8e12e51…
TFC   STAGE8_TRANSPORT_FUNCTOR_CHARTER_V001.md                        f58007a0…
TCO   STAGE8_TRANSPORT_CHARTER_OPTIONS_WITH_COSTS_V001.md             97149d08…
719   STAGE8_7A_TOPOLOGY_REQUIRE_HUNT_DARIO_V001.md                   961a76c4…  (mine)
716   STAGE8_7A_RA27_2_SAME_REGION_DARIO_V001.md                      5234141f…  (mine)
CARR  STAGE8_7A_R9JII_JOINT_LANDING_TEST_V001.md                      5f4979d5…
PREREG STAGE8_7A_OBS22_RECOGNITION_PREREG_V002_FROZEN.md              9f0d12b4…  unchanged
```

### 0.2 The anti-tuning declaration, made before the definition work

[YOURS] The relay names the R4-kernel **void condition** my own 719 hunt surfaced — a
topology may not be *"chosen from desired coefficient"*. I record the discipline I
actually followed, because a declaration after the fact is worth less than one before:

**No coefficient, response value, or downstream number was consulted at any point in
building the definition below.** The construction was driven by two questions only —
*what does V011's operational text say the convergence is*, and *does any sealed source
instantiate that notion as a topology*. I did not at any stage ask what either
candidate would do to any number, and §3's verdict is the one the definition work
produced rather than one I found congenial. The verdict is in fact the least convenient
of the four available.

### 0.3 Gates

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

No common cell formed, no junction map evaluated, no member bound, no fixed point, no
end test, no numeric evaluation, no measured constant. **Nothing adopted.** No
register, plan, tracker, git, commit or push action. The frozen preregistration was not
altered.

---

## 1. GG1 — THE DEFINITION ATTEMPT

### 1.1 What must be supplied

[YOURS] For `tau_density` to be a **complete topological carrier** the corpus must
supply three things, not one:

```text
(a) CARRIER    the object class on which the topology lives;
(b) TOPOLOGY   the convergence notion, and completeness of the carrier in it;
(c) INDEX      the directed system along which the limit is taken.
```

4d names `tau_density` by (b) alone — *"local-response/action-density convergence over
`C_ref`"* — which is why it records the candidate as *"not defined as a complete
topological carrier."* The hunt below finds (a) and (b) sealed, and (c) missing.

### 1.2 The corpus supplies the notion — and it is precise

[PROVABLE] `DUH` `4fe8d42d…[26396,26835)`:

```text
(H2) [= battery T7(iii); uniform intensive bound + density convergence]
     With the log branch anchored at Ghat_K(0,0) = 1 (well-defined on the
     simply connected polydisc by (H1)), the intensive logs
        gamma_K := -Log Ghat_K / N_4(K)
     satisfy: (i) sup_K sup_P |gamma_K| <= Gamma_* < infinity; and
     (ii) gamma_K converges pointwise on a subset of P with an accumulation
     point in each variable, to a limit gamma_inf.
```

[PROVABLE] This is a **density** in the exact sense V011 uses: an extensive quantity
divided by the four-volume count `N_4(K)`. And it is the same shape as V011's own
operational requirement, `aa7c6d49…[47025,47247)`, that the intensive coefficient be
invariant *"up to a boundary term whose ratio to four-volume tends to zero."*

### 1.3 And the completeness is sealed too

[PROVABLE] `DUH` `4fe8d42d…[26899,27360)`:

```text
**Theorem schema (conditional).** Assume (H1) and (H2), plus C1 and C2
uniformly along the exhaustion. Then, by Montel (uniform boundedness on P)
and Vitali-Porter (pointwise convergence on a set with accumulation points),
`gamma_K -> gamma_inf` locally uniformly on the open polydisc; `gamma_inf`
is jointly holomorphic; and by the Cauchy integral representation of
derivatives on a polydisc contour strictly inside P, every mixed partial
derivative converges.
```

[PART-PROVABLE] Read as a carrier specification this gives (a) and (b) completely:
the objects are the intensive logs on the polydisc `P`; the topology is **locally
uniform convergence**; Montel supplies compactness of bounded families and
Vitali–Porter supplies that limits stay in the class. Locally uniform convergence on an
open polydisc is a complete, metrizable topology, and the schema uses exactly the two
classical facts that make it one. **This is a complete topological carrier.**

[YOURS] My 719 artifact recorded `tau_density` as *"not defined as a complete
topological carrier"* and left the impression that no such definition existed anywhere.
That impression was wrong, and the object-names probe found the correction. What 4d
says is narrower and remains true: it is not defined **as `tau_density`** — see §1.4.

### 1.4 GAP 1 — the index is the exhaustion, not `C_ref`

[PROVABLE] `DUH` `4fe8d42d…[8077,8147)`:

```text
Let `K` denote a member of the relayed causally-sequential exhaustion.
```

[PROVABLE] Every limit in the schema is `lim_K` along that exhaustion. And in `DUH`,
searched in full: `refinement` occurs once, `cellulation` once, **`C_ref` zero times.**

[PROVABLE] `4d` `430f0971…[11220,11414)` defines the candidate as:

```text
tau_norm    = C-star/module norm on the ratified completion;
tau_cyl     = projective convergence of every finite restriction;
tau_density = local-response/action-density convergence over C_ref.
```

[YOURS] So the sealed instance converges along a **growing volume**; `tau_density`
requires convergence along a **refinement family**. These are different directed
systems, and nothing transports one to the other. Supplying the refinement index is
supplying a relation saying which complexes refine which — which is **RA27-2's
same-region relation**, the object my 716 artifact located as the root of the whole
A27 chain.

**GAP 1, named: the directed index over `C_ref`. It is RA27-2.**

### 1.5 GAP 2 — the carrier class, and why this reframes the question

[PROVABLE] The sealed instance's objects are intensive logs `gamma_K` — scalar
holomorphic functions on a polydisc. `tau_norm` and `tau_cyl` are, by 4d's own words,
topologies on *the ratified completion* and on *finite restrictions* of it — an
operator/module object.

[PART-PROVABLE] These are not the same carrier. A topology on a space of holomorphic
densities and a topology on an operator completion are not two options on one object;
they are structures on two objects. 4d's list presents them in one column because it is
enumerating *candidate senses of the limit*, not asserting a common carrier — and 4d
never states one.

[YOURS] **The consequence is the sharpest thing in this artifact.** Requires R3, R5 and
R6 from my 719 hunt are all properties of the **completion class**: no bidual moving
tail; `J_ref` lands in the ratified norm/module class; P7 separation rules out
norm-class content invisible to finite restrictions. If `tau_density` is a topology on
derived densities rather than on that completion, those three requires do not *fail*
for it — they may not **apply** to it at all. Testing a function-space topology for
whether its limits acquire an operator bidual tail is not a test that has a truth
value.

So "which of three topologies" may be **under-posed**: two candidates are alternatives
on one carrier, and the third is a different structure that the same requires cannot
address. I record this as a question the principal should see before ruling, not as a
finding that 4d erred — 4d's own text supports the narrower reading, and it never
claimed a common carrier.

**GAP 2, named: whether `tau_density` is a topology on the ratified completion or on
derived intensive densities. Unsealed, and the only sealed instance is the latter.**

### 1.6 The partial definition, displayed

Per GG1's instruction — *"if the definition cannot be completed without an undetermined
element, the deliverable is the partial definition plus the named gap, not an
invention"* — here is exactly what is grounded and exactly what is not.

```text
tau_density — PARTIAL DEFINITION

  (a) CARRIER   [GROUNDED, but see GAP 2]
      Intensive densities: an extensive quantity divided by the four-volume
      count, gamma_K := -Log Ghat_K / N_4(K), valued in holomorphic functions
      on the polydisc P.                              DUH 4fe8d42d…[26396,26835)

  (b) TOPOLOGY  [GROUNDED, and complete]
      Locally uniform convergence on the open polydisc.  Bounded families are
      normal (Montel); limits remain in the class and all mixed partials
      converge (Vitali-Porter + Cauchy).               DUH 4fe8d42d…[26899,27360)

  (c) INDEX     [MISSING — GAP 1]
      The sealed instance is indexed by the relayed causally-sequential
      exhaustion.  DUH 4fe8d42d…[8077,8147).  tau_density requires the C_ref
      refinement family.  The transporting object is RA27-2's same-region
      relation, which 716 established is not forced by stock.

  CARRIER-CLASS IDENTIFICATION  [MISSING — GAP 2]
      Whether this carrier is the ratified completion (comparable with
      tau_norm/tau_cyl) or a distinct density space.  Unsealed.

  STANDING FENCE ON THE NOTION       DUH 4fe8d42d…[28659,29028)
      (H2) may be USED as a definition; it may not be DISCHARGED by
      assumption.  See §2.2 R9.

  STATUS = PARTIAL.  (a) and (b) sealed; (c) missing; class identification
           missing.  NOT COMPLETABLE from sealed sources without RA27-2.
```

[PROVABLE] **Nothing else supplies the missing index.** SEARCHED SPACE:
`workspace/` + `supervision/`, `*.md`, recursive; object-names probed —
`density convergence`, `action-density`, `local-response`, `response density`,
`intensive response`, `intensive quadratic coefficient`, `four-volume`,
`boundary/four-volume`, `seminorm`, `density class`, `tau_density`. Every file
carrying a density-convergence notion **and** `C_ref` was opened. The two nearest,
`TFC` `f58007a0…` and `TCO` `97149d08…`, contain **zero** occurrences of `topology`
and both state of record that *"IT DOES NOT RESOLVE C_ref/D3, which remains the
principal's"* — independently corroborating my 716 finding that the shape conflict is
still held. `CPKG` `09883a0d…` is `PROPOSED_NOT_ADOPTED` and obstructed at
`[590,737)` on *"no ratified or proposed datum exhibits an actual physical
path/test-form/coframe/density realization"* — the same absence from the package side.

---

## 2. GG2 — THE MATRIX, RE-RUN

`S` satisfies · `V` violates · `U` undetermined · `N/A` require does not apply to this
carrier class · `–` non-discriminating

| | R1 derived theorem | R2 V011 density | R3 no bidual tail | R4 one frozen topology | R5 §9 class premise | R6 separation | R7 anti-tuning | R8 J2 invariance | **R9 (new) discharge fence** |
|---|---|---|---|---|---|---|---|---|---|
| **tau_norm** | – | U | S | S | S | S | S | U | **S** |
| **tau_cyl** | – | U | **V** | S | U | **V** | S | U | S |
| **tau_density** | – | **U→ near-native** | U / N/A? | **U (no index)** | U / N/A? | U / N/A? | S | U | **S, with burden** |

### 2.1 What changed from 719, and what did not

[PROVABLE] `tau_cyl` is unchanged: eliminated, certificate at 719 §2.2. `tau_norm`'s
row is unchanged; the definition work surfaced no require that moves it.

[PART-PROVABLE] `tau_density`'s row changes in three cells and in no others:

- **R4** sharpens from bare `U` to **`U` with a named cause**: the candidate has a
  complete topology but no directed index over `C_ref`. It is not "one frozen topology"
  because the thing it would be frozen over does not exist.
- **R3, R5, R6** become `U / N/A?` rather than plain `U`: under GAP 2 these may not be
  applicable to a density carrier at all. I score the ambiguity rather than resolve it.
- **R2** is the one cell where `tau_density` is *stronger* than `tau_norm`, and honesty
  requires saying so. R2 is V011's own requirement, stated in four-volume ratio terms;
  the sealed density carrier is built as an over-`N_4` quotient. The notion is
  **native** to R2 in a way `tau_norm`'s is not — 719 recorded `tau_norm` as `U` on R2
  precisely because the ratified completion carries no measure. Neither candidate
  satisfies R2 today; only one speaks its language.

### 2.2 R9 — the new require, tested against both survivors

[PROVABLE] `DUH` `4fe8d42d…[28659,29028)`:

```text
Any attempt, anywhere in the execution, to DISCHARGE (H1) or (H2) — by
assumption, by citation of exhaustive-chain zero-freeness (F2.1), by
citation of the periodic zero-free lineage (F2.5), by adoption of
`BUFFERED_EXHAUSTION_CLUSTERING` or ANY clustering principle, or by any
"physically reasonable" interpolation — is

CLUSTERING_ADOPTION_ATTEMPT_BLOCKED
```

Modality: a hard fence — REQUIRE. Tested against both, as GG2 directs:

- **`tau_norm` — S.** Its definition invokes neither (H1) nor (H2); the fence has no
  purchase on it.
- **`tau_density` — S, with a burden.** The fence does **not** forbid defining the
  carrier from (H2)'s shape, which is what §1.6 does. It forbids *discharging* (H2).
  So an instantiated `tau_density` would carry a standing obligation its rival does
  not: its defining convergence must be **proved**, never assumed. That is a real cost
  and not a disqualification, and I score it as such.

[YOURS] I record explicitly that I have not discharged (H1) or (H2) and do not assert
they hold. This artifact uses (H2) as a **specification of a notion**, which is the
one use the fence leaves open.

---

## 3. GG3 — VERDICT

```text
VERDICT = DEFINITION-INCOMPLETE
          GAP 1: the directed index over C_ref  (= RA27-2's same-region relation)
          GAP 2: the carrier-class identification (completion vs density space)
          tau_density remains UNTESTABLE; tau_cyl remains ELIMINATED;
          tau_norm remains the only candidate satisfying every require it can
          be tested against.
```

[YOURS] Why not one of the other three. `FORCED(tau_norm)` still requires treating an
unevaluated candidate as dead, and this relay has made that *less* available rather
than more: `tau_density` now has a sealed complete topology behind it and is native to
R2, so scoring it dead would be worse-founded than at 719. `FORCED(tau_density)` is
unavailable — it has no index. `UNDERDETERMINED({both})` would assert both survive
every require, which is false: one of them cannot be tested at all.

[YOURS] **The result that matters is not the verdict — it is where the gap landed.**
I proposed this relay at 719 as the cheap decisive test, on the reasoning that defining
`tau_density` was a small self-contained job. It was not self-contained. The definition
runs out at exactly the object the whole thread runs out at: **RA27-2's same-region
relation.** That makes three independent routes now blocked on one thing — A27's
remainder, R9-JII's J2 quantifier, and now the topology choice.

[YOURS] And it corrects my 719 framing. I called freezing the topology *"the smallest
adoption"* and said it *"adds no generator, member, shape condition or smooth import."*
For `tau_norm` that stands. But it is **not prior to `J_ref`/RA27-2 in general**: one
of the two survivors cannot even be stated without the refinement relation. The
topology question is not upstream of the same-region relation; for half the candidate
set it is downstream of it. **A principal reading my 719 artifact could have concluded
the topology could be settled first. For `tau_density` it cannot.**

[YOURS] What would now settle the topology question, in order of cost:

```text
1. RULE on the carrier-class question (GAP 2) -- is tau_density a topology on
   the ratified completion, or on a density space?  This is a typing question,
   answerable without building anything.  If the completion: R3/R5/R6 apply and
   the matrix decides.  If a density space: the "three-way choice" dissolves and
   the real question becomes which CARRIER the limit lives on.

2. Only then, or in parallel, RA27-2 -- which supplies GAP 1 and unblocks the
   rest of the chain regardless.
```

Item 1 is genuinely cheap and I did not see it before doing this work. It is the
honest successor to the test I proposed at 719.

---

## 4. GG4 — CORRESPONDENCE LEDGER (verdict weight = 0)

| # | Encountered at | Classical likeness | Weight |
|---|---|---|---|
| L1 | locally uniform convergence on a polydisc, complete and limit-preserving | the compact-open topology on holomorphic functions — a Fréchet space; Montel's theorem as normality | 0 |
| L2 | `gamma_K := -Log Ghat_K / N_4(K)` as the carried object | free-energy density per unit volume; an intensive thermodynamic quantity | 0 |
| L3 | a density notion needing a measure the discrete side lacks | distribution-theory carriers, where the test-function space must be fixed before the dual means anything | 0 |
| L4 | exhaustion index vs refinement index as two directed systems | thermodynamic limit versus continuum limit — distinct limits routinely conflated | 0 |

[YOURS] L4 is the one that earned its place and the one to fence hardest: the
*resemblance* between the two limits is exactly what would make GAP 1 easy to miss, and
noticing the gap came from reading the schema's index line, not from the analogy.

---

## 5. SEARCHED SPACES, GROUNDING, JURISDICTION, VERB AUDIT

### 5.1 Searched spaces

| Claim | Searched space | Method |
|---|---|---|
| The (H2) carrier is the only sealed instance of the density-convergence notion | `workspace/` + `supervision/`, `*.md`, recursive | object-names probe (12 terms, §1.6); every hit opened |
| Nothing indexes a density limit over `C_ref` | same | files carrying a density-convergence notion ∩ `C_ref`; all opened, including `TFC`, `TCO`, `CPKG` |
| No new require beyond R9 | same | modality probes across the density material |

[YOURS] Not searched, therefore not claimed about: the cleanroom mirror, the origin
corpus outside the archive, non-`.md` files, `rd22_run_*/evidence/` digest-prefixed
mirrors. Per `STAGE8_LANE_STATUS.md`'s standing caveat every absence here is a **lower
bound**.

### 5.2 Grounding

| # | Step | Source + span | Tag |
|---|---|---|---|
| 1 | (H2) supplies the density-convergence notion | `4fe8d42d…[26396,26835)` | PROVABLE |
| 2 | Montel + Vitali–Porter give completeness and limit preservation | `4fe8d42d…[26899,27360)` | PROVABLE |
| 3 | The index is the relayed causally-sequential exhaustion | `4fe8d42d…[8077,8147)` | PROVABLE |
| 4 | `DUH` never mentions `C_ref` | full-file count: 0 | PROVABLE |
| 5 | 4d defines `tau_density` as convergence **over `C_ref`** | `430f0971…[11220,11414)` | PROVABLE |
| 6 | V011's requirement is a four-volume ratio | `aa7c6d49…[47025,47247)` | PROVABLE |
| 7 | The S5.3 discharge fence | `4fe8d42d…[28659,29028)` | PROVABLE |
| 8 | `CPKG` obstructed at coframe/density realization | `09883a0d…[590,737)` | PROVABLE |
| 9 | `TFC`/`TCO` define no topology; C_ref/D3 remains the principal's | both files, `topology` count 0 | PROVABLE |
| 10 | (a)+(b) constitute a complete topological carrier | §1.3, from 1–2 | PART-PROVABLE |
| 11 | GAP 1 = the `C_ref` index = RA27-2 | §1.4, from 3–5 + `5234141f…` | PART-PROVABLE |
| 12 | GAP 2 = carrier-class identification unsealed | §1.5, from 1 + 5 | PART-PROVABLE |
| 13 | R3/R5/R6 may not apply to a density carrier | §1.5 | **YOURS** |
| 14 | R9 tested against both; disqualifies neither | §2.2, from 7 | PART-PROVABLE |
| 15 | `tau_density` is native to R2 | §2.1, from 1 + 6 | PART-PROVABLE |
| 16 | Verdict DEFINITION-INCOMPLETE | §3 | **YOURS** |
| 17 | The carrier-class ruling is the cheap next step | §3 | **YOURS** |
| 18 | Correction to my 719 "smallest adoption" framing | §3 | **YOURS** |

```text
GROUNDED_STEPS = 14 / 18
YOURS, NAMED: 13, 16, 17, 18.  None is a premise for any PROVABLE row.
```

### 5.3 Jurisdiction check

**The R4-kernel void condition (no topology chosen from desired coefficient).** Written
against selecting the limit's sense by the number it yields. Squarely present in a
relay whose whole job is to define a candidate. §0.2 declares the discipline before the
work; no coefficient was consulted; and the verdict reached is the least convenient of
the four.

**The S5.3 discharge fence.** Written so a hard analytic hypothesis is never assumed
into existence. Present: (H2) is exactly what a `tau_density` instantiation would want
to assume. Its outcome space distinguishes false from cannot-see — defining the notion
is permitted, discharging it is blocked — and it permits the evidence: a *proved* (H2)
satisfies it.

**R9-JII / R9.** Unchanged. `tau_density`'s `U`s are recorded as unevaluable, never as
failures, and §3 declines `FORCED` for the same reason it declined at 719.

**DoR-007.** No smooth structure imported, requested, or assumed. The density carrier
is built from record-side intensive quantities; the missing index is named, not
supplied from a smooth background.

### 5.4 Self verb audit

| Verb or status | Warrant |
|---|---|
| `complete topological carrier` | applied to (a)+(b) only, on Montel/Vitali as the schema states them |
| `PARTIAL` | the definition's own status line, with each element marked grounded or missing |
| `GAP 1 / GAP 2` | each named as an object, not as a difficulty |
| `N/A?` | applicability of R3/R5/R6 to a density carrier — scored as a question, not resolved |
| `S, with burden` | R9 on `tau_density` — a standing proof obligation, not a disqualification |
| `DEFINITION-INCOMPLETE` | the verdict, chosen over three alternatives with reasons at §3 |

[YOURS] Disclosures against myself:

1. **My 719 artifact left a false impression, and this relay corrects it.** I recorded
   `tau_density` as *"not defined as a complete topological carrier"* — 4d's words, and
   true — but I wrote around it as though **no** definition of the notion existed
   anywhere. One does, it is precise, and it is complete. The object-names probe found
   it in the first pass. Had I run that probe at 719 the hunt would have been sharper.
2. **The test I proposed at 719 was not the cheap decisive one I called it.** I said
   defining `tau_density` was *"cheaper than anything left in the RA27 chain."* It is
   not a self-contained job: it runs out at RA27-2, the same object everything else
   runs out at. A lane that proposes a next step should say what that step depends on,
   and I did not check before recommending it.
3. **My 719 "smallest adoption" framing was too general.** Freezing the topology adds
   nothing *for `tau_norm`*. For `tau_density` it cannot be done at all without the
   refinement relation. A principal reading 719 could reasonably have concluded the
   topology was settleable first; §3 says plainly that it is not, for half the set.
4. **GAP 2 may be the more important finding and I nearly missed it**, because I went
   looking for an index and only noticed the carrier mismatch while writing §1.5. If
   the three candidates are not structures on one object, the question I have been
   answering for two relays is under-posed.
5. No verb here proves, authorizes, computes, binds a member, forms a common cell,
   evaluates a junction map, discharges (H1) or (H2), adopts anything, or grants a seal.

```text
DEFINITION = partial (GAP 1 the C_ref directed index = RA27-2; GAP 2 the
             carrier-class identification, completion vs density space)
MATRIX = re-run, displayed at §2 (3 x 9 with R9 added)
VERDICT = DEFINITION-INCOMPLETE (gaps named; tau_density untestable stands;
          tau_cyl remains eliminated; tau_norm remains the only candidate
          satisfying every require it can be tested against)
NEW_REQUIRES = 1 (R9, the S5.3 discharge fence) — tested against both survivors;
          tau_norm S, tau_density S-with-burden; it disqualifies neither
LEDGER_ENTRIES = 4
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+5 disclosures at §5.4)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
