# Stage 8 Task 4a p_loc Candidate-W Battery and Consumption-Typing Determination v001

Date: 2026-08-02  
Lane: CODEX LANE 1  
Task: 4a, relay 365  
Register head at start and completion: Q-282  
Standing: structural determination only; no physical tail, consumer, response,
fixed point, or value is constructed or evaluated.

## 0. Lead verdict

**CANDIDATE W IS NOT BATTERY-DEAD AS A CLASS.** The battery kills the
independently authored, provenance-free form

```text
p_loc^W(H_cyl+t) = p_cyl(H_cyl) + ell_tail(t)
```

when `ell_tail` is inserted solely because all finite restrictions are silent.
It does **not** kill a common-origin-generated `ell_tail` whose topology,
physical tail domain, descent, and B1-B14 certificates are frozen before any
output. B13 says that a tail-sensitive term needs its own declared physical
provenance; it does not say that every such term is forbidden. Q-282 then gives
an explicit logical countermodel to the stronger prohibition: a tail rule
placed in a hypothetical common-origin realization and frozen before output
satisfies B13-B14 while remaining invisible to every finite restriction.

Therefore the Q-255 phrase "effectively battery-dead" is too strong. What is
dead is `W_free`, the unsupported tail covector. What survives is `W_gen`, the
common-origin/emergent-tail form. `W_gen` is not built, adopted, or shown
nonempty in the physical response class. Its survival refutes only the claim
that the standing battery forces Candidate F.

```text
CANDIDATE_W_BATTERY_DEAD_AS_A_CLASS = false | TYPE-R |
  test: B13 expressly admits a tail-sensitive term with declared physical
        provenance, and Q-282:260-278 supplies a B1-B14-compatible
        common-origin tail-action countermodel

INDEPENDENT_PROVENANCE_FREE_W_ADMISSIBLE = false | TYPE-P |
  premises: DoR-008:24-31 and B13-B14 |
  reason: finite silence supplies neither authority nor executable provenance

COMMON_ORIGIN_GENERATED_W_ADMISSIBLE_AS_A_CANDIDATE = true | TYPE-P |
  premises: DoR-008 limit-only caveat, B1-B14, Q-250, Q-282 |
  boundary: logical admissibility, not physical construction or adoption

COMMON_ORIGIN_GENERATED_W_CONSTRUCTED = false | TYPE-U |
  would-build: P5/P6 physical response class and restrictions; a physical
               Tail_ind embedding; a canonical splitting or tail projection;
               a covariant ell_tail generated on the frozen common-origin
               trace; B1-B14 certificates including its tail action

P_LOC_CONSUMPTION_FORCED_TO_CANDIDATE_F = false | TYPE-R |
  test: W_gen is a standing-battery model not equivalent to F when
        ell_tail is nonzero on an admitted physical tail

B_IND_TAIL_BLIND_BY_TYPING = NO_VERDICT |
  prerequisite: either Candidate F is derived/ratified, Tail_ind is zero, or
                every admitted W_gen has ell_tail restricted to Tail_ind zero
```

## 1. Scope, premises, exclusions, and queries

### 1.1 Premises declared at the outset

No premise beyond the current stack is used. The distinction between
`PROVABLE` and `YOURS` is load-bearing:

```text
PROVABLE:
  consequences derived inside the current formal stack from DoR-008,
  Q-247, Q-250, Q-253, Q-254, Q-255, and Q-282.

YOURS / PRINCIPAL PREMISE:
  DoR-008:24-31 -- the completion has no independent authority and the
  infinite is treated as emergent from the finite, while genuinely limit-only
  quantities may exist if separately proved.
```

The principal premise is not reported as derived physics. All conclusions that
exclude an independently sourced `ell_tail` carry that premise explicitly.

### 1.2 Roots entered

| Root | SHA-256 | Role |
|---|---|---|
| `alpha_supervision/LOCKED_PROCESS.md` | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | custody, typing, and act-based fences |
| `alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md` | `73f97ec6c2e29d426f8f49023cbb047ff6d81224a1efdc128e1a4541283a1a1f` | current ruling set and stale-work check, read through Q-282 |
| `alpha_supervision/DECISION_OF_RECORD_008_FIELD_CTP_ADOPTION_RATIFIED_WITH_FALSIFIER_2026-08-01_V001.md` | `d51a6d5c5bb0020a081cfd2adfb545b9f5ed86ce660d3feacadc5ef68140fb19` | finite authority, restriction falsifier, limit-only caveat |
| `alpha_supervision/DECISION_OF_RECORD_013_GEN_OMEGA_RATIFIED_FAMILY_LEVEL_2026-08-02_V001.md` | `f2a7838d41b7b7df42ae92bc3d59399ee04bbec65cecadc8a43f6a36ac4756ec` | ratified common-origin family and finite falsifier inheritance |
| `alpha_supervision/DECISION_OF_RECORD_014_SOURCE_GERM_PHYS_RATIFIED_2026-08-02_V001.md` | `b6e4116df63403478d28be8cdb6589b091cc1aa8b6ad5a40776a28b135cd138f` | ratified executable common-origin descent and open P5/P6 boundary |
| `workspace/STAGE8_TASK4A_P_LOC_TAIL_ANNIHILATION_CERTIFICATE_DETERMINATION_V001.md` | `df2dbdccb25d5ee62e0de9051a8300c3933fb4c07250e765632d2f6247a6df45` | exact Candidates F and W; Q-255 battery reading |
| `workspace/STAGE8_TASK4A_MISSING_PHYSICAL_LAYER_CONSOLIDATED_SPEC_AND_CONSTRAINT_BATTERY_V001.md` | `241bf43f04aed7f215bad6ea80170a9c7733000896df839ac80974769d0a46c3` | B1-B14 exact text |
| `workspace/STAGE8_TASK4A_FINITE_RESTRICTION_SEPARATION_AND_BIDUAL_TAIL_DETERMINATION_V001.md` | `60b5b4c5788eca2be2d9f11d67983b2e7a5823066cdabf9a734f7a59aae0ecd1` | mathematical bidual tail, topology split, physical-transport boundary |
| `workspace/STAGE8_TASK4A_RESPONSE_CLASS_FORCING_AND_TAIL_OUTPUT_INERTNESS_DETERMINATION_V001.md` | `fccd16a74269386a2fdb7bac122f907cd659c8eb09ae5f45eabf39e5e9180d79` | exact modulo-tail countermodel and output criterion |
| `workspace/STAGE8_TASK4A_BIND_INPUT_SIGNATURE_AND_DOMAIN_TAIL_BLINDNESS_DETERMINATION_V001.md` | `790ae95bfa7f7747f383a387842939cb8f024d3e0107a9cbe15683666058c73f` | exact reduction of B_ind tail-blindness to `p_loc|Tail_ind=0`; background separation |
| `workspace/STAGE8_TASK4A_FOUR_DEPENDENCE_PRESERVATION_CERTIFICATES_FAMILY_LEVEL_DETERMINATION_V001.md` | `78ec90ce3274c706622fb96cd639ae3fd7d65a101aa3287a0c311618275433b5` | Q-282 finite-shadow theorem and B13-B14-compatible common-origin tail model |

### 1.3 Exclusions and searches

Excluded: `a32_holdout/custodian_private/`; all measured targets; all value
evaluation; all root solving; all construction or selection of a physical
response class, tail, `p_loc`, stationary background, or fixed point. No git
command was run.

Queries were word-boundaried or exact-phrase searches for `p_loc`,
`Candidate F`, `Candidate W`, `p_cyl`, `ell_tail`, `Tail_ind`, `Tail_R`,
`finite-authority`, `common-origin`, `provenance`, `restriction`, `B13`, and
the principal's exact emergent-finite statement. The register tail was checked;
no ruling later than Q-282 was present.

## 2. Candidate W, exactly

Q-255 defines Candidate W at
`STAGE8_TASK4A_P_LOC_TAIL_ANNIHILATION_CERTIFICATE_DETERMINATION_V001.md:465-496`.
Its data are not merely a formula. They include:

1. a physical response class with a declared weak-star/bidual completion;
2. physical restrictions and `Tail_ind`;
3. a certified physical embedding of `Tail_ind` into that completion;
4. a cylindrical component `p_cyl`;
5. a tail projection or splitting `H=H_cyl+t`;
6. a covariant linear `ell_tail`, nonzero on at least one admitted tail;
7. `p_loc^W(H_cyl+t)=p_cyl(H_cyl)+ell_tail(t)`;
8. normalization and target-independent pre-output freeze; and
9. CTP reality, Ward, support, boundary, domain, regulator, and **physical
   provenance** certificates for `ell_tail`.

Q-247 proves only the mathematical shape

```text
Tail_B** = intersection_N ker((r_N^B)**)
         = M_cyl(Y)^perp
         = z_tail B** != {0}
```

and a weak-star witness `v_U`; see
`STAGE8_TASK4A_FINITE_RESTRICTION_SEPARATION_AND_BIDUAL_TAIL_DETERMINATION_V001.md:345-449`.
It expressly withholds the identity between that mathematical tail and a
physical response tail at `:563-584`. Thus the mathematics shows that W is
well-typed as a possible completion architecture; it does not instantiate W.

```text
CANDIDATE_W_ILL_POSED = false | TYPE-R |
  test: Q-247 constructs a nonzero weak-star tail and Q-255 gives a complete
        typed candidate signature

MATHEMATICAL_BIDUAL_TAIL_IS_PHYSICAL_TAIL_IND = false | TYPE-R |
  test: Q-247:563-584 expressly withholds physical transport

PHYSICAL_TAIL_IND_INSTANTIATED = false | TYPE-U |
  would-build: P5/P6 physical class, restriction intertwiners, and the
               support/reality/Ward/boundary/domain-preserving embedding
```

## 3. Exhaustive provenance split for ell_tail

The logically distinct source classes are:

| Source of `ell_tail` | Status under current stack | Reason |
|---|---|---|
| Finite silence alone | `REFUTED` | DoR-008 supplies no positive origin for invisible content; Q-255:555-558 already tests and rejects this inference. |
| Arbitrary authored covector/constant on `Tail_ind` | `BLOCKED BY PRINCIPAL PREMISE` | It gives the completion independent authority contrary to DoR-008:24-31 and lacks B14 descent. A future principal reversal could adopt it, but the current stack cannot. |
| Arbitrary bidual or ultrafilter choice | `MATHEMATICAL ONLY` | Q-247 gives such witnesses, but no canonical physical embedding, no physical covariance package, and no common-origin descent. |
| Independently supplied boundary, contour, measure, or domain datum | `NOT ADMISSIBLE AS AN INDEPENDENT ADD-ON` | It is post-finite continuum physics unless brought into the common-origin trace before output and certified through B1-B14. |
| Stationary background | `WRONG CHANNEL` | Q-253:384-421 proves the tail-at-fixed-background and background-variation channels are distinct. |
| Target- or output-chosen functional | `BARRED` | B14 and the standing no-fitting rule forbid post-output supplementation. |
| Canonical limit theorem generated from the finite directed system | `ADMISSIBLE CANDIDATE` | DoR-008:26-31 expressly allows limit-only quantities with their own theorems. It must be canonical/unique in a named topology and carry the physical embedding and B1-B14 certificates. |
| Executable common-origin P3-P6 descent, including a sourced boundary/contour/domain tail action | `ADMISSIBLE CANDIDATE` | Q-282:260-278 places precisely such a hypothetical tail rule inside the standing battery without violating B13-B14. |

The last two rows are one surviving class:

```text
W_gen:
  ell_tail is not an independent datum;
  ell_tail is generated by an executable, frozen common-origin construction;
  its topology and physical tail domain are named;
  its finite shadow is zero;
  its nonzero complete action is proved by a limit/descent theorem;
  every B1-B14 certificate is carried before output.
```

An arbitrary free-ultrafilter witness is not yet `W_gen`: existence of a
weak-star limit is not uniqueness or physical provenance. A lawful construction
must either derive a canonical limit or carry the residual choice openly as a
new premise; the latter is not authorized by the present stack.

```text
FINITE_SILENCE_PRODUCES_ELL_TAIL = false | TYPE-R |
  test: DoR-008 and B13 reserve invisible content for a separate provenance
        theorem

ARBITRARY_BIDUAL_WITNESS_HAS_PHYSICAL_PROVENANCE = false | TYPE-U |
  would-build: physical tail embedding, canonical topology/limit, common-origin
               descent, and all physical certificates

BACKGROUND_SUPPLIES_ELL_TAIL = false | TYPE-R |
  test: Q-253:384-421 separates background variation from Tail_ind

COMMON_ORIGIN_W_GEN_EXISTS_PHYSICALLY = NO_VERDICT |
  prerequisite: P5/P6 plus a concrete B1-B14 realization
```

## 4. Battery run, row by row

The distinction in the last column is between **constraint compatibility** and
**an executed certificate**. W_gen survives the former; no physical W has yet
executed the latter.

| Row | Test on W | Determination |
|---|---|---|
| B1 finite-restriction reproduction | `ell_tail` vanishes on every finite restriction; `p_cyl` must reproduce the sealed finite outputs. | **Can pass; not a kill.** Q-250:292-317 proves `H` and `H+t` have identical finite receipts. |
| B2 finite retarded baseline | W changes only a restriction-invisible tail term. | **Can pass; not a kill.** The finite zero, p-free block is unchanged. |
| B3 finite restrictions stay p-free | Any W dependence enters only through physical tail content, exactly one of B3's two reserved channels. | **Can pass; not a kill.** B3:510-515 expressly leaves the tail channel open. |
| B4 no naive extension | W must name weak-star/bidual topology and prove its limit/descent. | **Conditional.** Arbitrary continuation fails; a named theorem-generated completion can pass. |
| B5 separation only on ratified classes | W deliberately uses a class beyond the separated norm/module class. | **Open TYPE-U.** It must prove physical membership; B5 does not ban the larger class. |
| B6 explicit tail | W names the tail, embedding, splitting, and action. | **Open TYPE-U.** The signature is complete, but the physical objects are absent. |
| B7 modulo-tail determinacy | W preserves the distinction between a finite-data coset and a complete representative. | **Passes structurally.** It does not claim finite agreement implies identity. |
| B8 finite visible quotients | W does not identify the finite `p` quotient with a completed response output. | **Passes structurally.** |
| B9 consumer-specific certificate | W takes B9's second legal branch: exhibit a lawful witness that the output sees the tail. | **Open TYPE-U, not forbidden.** It needs admitted `t_ind` with certified `ell_tail(t_ind)!=0`. |
| B10 no finite interior stationary point | W introduces no finite stationary point. | **Passes structurally.** |
| B11 C1 not an evaluation rule | W does not use C1 to select a completed background. | **Passes structurally.** |
| B12 three zero surfaces distinct | W identifies none of them. | **Passes structurally.** |
| B13 finite authority | `W_free` fails; `W_gen` carries its own physical common-origin provenance. | **Split.** B13 kills unsupported authorship, not sourced tail physics. |
| B14 target independence/common origin | `W_free` fails; W_gen must be frozen and descend executably before output. | **Can pass.** Q-282's common-origin tail countermodel demonstrates logical compatibility. |

The decisive existing statement is Q-282 at
`STAGE8_TASK4A_FOUR_DEPENDENCE_PRESERVATION_CERTIFICATES_FAMILY_LEVEL_DETERMINATION_V001.md:258-278`:

```text
B13-B14: the tail rule is placed in the hypothetical common-origin
realization and frozen before output; it is not inferred from finite silence
or tuned after a result.
```

That artifact then concludes that the present battery does not logically
exclude such tail extensions. It does not ratify one. This is a direct
counterexample to the blanket claim that W is battery-dead.

```text
DOR008_RESTRICTION_FALSIFIER_KILLS_W = false | TYPE-R |
  test: tail addition preserves every finite restriction (Q-250:292-317)

Q282_FINITE_SHADOW_THEOREM_KILLS_W = false | TYPE-R |
  test: Q-282:264-278 shows tail extensions satisfy the finite-shadow theorem
        and the standing battery at the level of a logical countermodel

W_FREE_PASSES_B13_B14 = false | TYPE-P |
  premises: DoR-008 principal basis and Q-254 B13-B14

W_GEN_PASSES_B1_B14_AS_AN_EXECUTED_PHYSICAL_OBJECT = false | TYPE-U |
  would-build: the physical response/tail package and every certificate in
               the row-by-row table
```

## 5. Consequence for the consumption fork

The current program has two still-lawful structural futures:

```text
F:
  p_loc = p_tilde compose R_fin;
  p_loc(t_ind)=0;
  B_ind is tail-blind at fixed background;
  the background channel remains open.

W_gen:
  p_loc(H_cyl+t)=p_cyl(H_cyl)+ell_tail(t);
  B_ind^(t)(K)-B_ind(K)=ell_tail(t_ind) may be nonzero;
  the fixed-point map can depend on common-origin, limit-only physics;
  the background channel remains separately open.
```

No value follows from either row. The consequence is relational only: F makes
the fixed-point map constant on tail cosets; W_gen may not. Q-253:364-382 proves
that exact equivalence at fixed `p_loc`; Q-253:384-421 keeps the background
channel separate.

The standing task is therefore not a principal choice between an arbitrary
finite functional and an arbitrary infinite one. It is a construction test:

1. build P5/P6 and instantiate the physical response class and `Tail_ind`;
2. derive the consumer from the same common-origin trace;
3. determine whether its generated tail action vanishes;
4. if it vanishes, the result has Candidate-F behavior;
5. if it is nonzero with full provenance, the result has W_gen behavior;
6. only if the construction leaves a residual inequivalent family does a
   principal authorship decision remain.

```text
ITEM_C_CLOSED_BY_FORCING_TO_F = false | TYPE-R |
  test: W_gen is compatible with B1-B14 and differs from F on a nonzero
        admitted tail

ITEM_C_REDUCED_TO_P5_P6_COMMON_ORIGIN_CONSUMER_CONSTRUCTION = true | TYPE-P |
  premises: Q-253 exact reduction, Q-254 commissioning order, Q-282

P_LOC_TAIL_ACTION_ZERO = NO_VERDICT |
  prerequisite: instantiate p_loc and Tail_ind on the P5/P6 physical class
P_LOC_TAIL_ACTION_NONZERO = NO_VERDICT |
  prerequisite: one admitted t_ind with a certified nonzero p_loc(t_ind)
TAIL_IND_ZERO = NO_VERDICT |
  prerequisite: instantiate the physical response class and all rho_H,N
BACKGROUND_CHANNEL_CLOSED = false | TYPE-U |
  would-build: STAT_BG_LIFT_FIBER and the completed stationary map (Q-281)
```

## 6. Final determination

```text
GATE_VERDICT = W_SURVIVES_ONLY_AS_COMMON_ORIGIN_GENERATED_FORM

Q255_EFFECTIVELY_BATTERY_DEAD_READING = REFUTED_AT_CLASS_LEVEL

UNSUPPORTED_W_FREE = EXCLUDED | TYPE-P |
  premises: DoR-008 principal basis and B13-B14

PROVENANCE_CERTIFIED_W_GEN = ADMISSIBLE_BUT_UNBUILT | TYPE-U |
  would-build: physical class, Tail_ind, generated ell_tail, and B1-B14

P_LOC_CONSUMPTION_SIGNATURE_FORCED_TO_F = false | TYPE-R
B_IND_FIXED_POINT_TAIL_BLIND_BY_TYPING = NO_VERDICT |
  prerequisite: instantiate the physical class, Tail_ind, and generated p_loc

FENCE_BLOCKED_STRUCTURAL_RESULT = false
MACHINERY_APPEAL = NOT_TRIGGERED

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

Custody: seal this artifact, verify its sidecar, mirror artifact and sidecar to
`/Users/bgm/MB Work/alpha-program-archive/workspace/`, report hashes and exact
paths, and stop. No register, git, commit, push, gate, or deploy action is
performed by this lane.
