# STAGE8 Gen_Omega generative-origin rule adversarial kill determination V001

Date: 2026-08-02

Status: RESULT -- GEN_OMEGA V001 DEAD AT THE DOR-013 GATE

Review target:

```text
STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V001.md
SHA-256:
f2043a2a68d983430c96ff33f98675b0bf2740edd235616b25d3c956017e148f
```

Authority head checked before this review: Q-259. No later register row was
present when the review was frozen.

This artifact is an adversarial review. It adopts nothing, repairs nothing,
and does not authorize DoR-013. Its result is about V001 as proposed, not
about every possible future generative-origin construction.

```text
ALPHA_COMPUTED = false
KAPPA_RECORD_COMPUTED = false
PROOF_AUTHORIZED = false

A1_SELECTION_TRAP = SURVIVED
A2_FAMILY_LEVEL_COUNTERMODEL = KILLED
A3_FOUR_CONDITIONALS = KILLED
A4_D_LAW_FIDELITY = SURVIVED
A5_RAY_EXCHANGE = WOUNDED
A6_P_CH_PARAMETERIZATION = WOUNDED
A7_FINITE_AUTHORITY_AT_ORIGIN = SURVIVED

OVERALL_VERDICT = DEAD
DOR_013_RATIFICATION_READY = false | TYPE-R |
  test: replacement-channel subfamily plus B14 root-not-bag condition
```

The decisive counterexample is elementary and lies inside G1's declared
family. For every normalized charge-superselected source state `rho`, define

```text
R_rho(tau) := Tr(tau) rho.
```

`R_rho` is normal, completely positive, trace preserving, charge covariant,
commutes with the declared `P_0/P_ch` conditional expectation, has the unique
normalized fixed point `rho`, and reaches it in one step. It therefore passes
every stated G1 membership condition. But selecting `R_rho` is exactly
selecting `rho` in channel notation. Applying this construction to the two
Q-242 states reproduces the old same-law/two-state freedom as a same-law/
two-channel freedom. Fixed-member uniqueness is true but does not establish a
family-level generative origin.

The proposal's own residual kill condition therefore fires. V001 may not
advance to DoR-013.

## 1. Scope and method

### 1.1 Roots entered

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha_supervision
```

### 1.2 Exclusions and fences

```text
a32_holdout/custodian_private/                       NOT ENTERED
response evaluation, roots, K_*, alpha, scales       NOT PERFORMED
measured-constant comparison                         NOT PERFORMED
register modification, git, commit, push             NOT PERFORMED
proposal repair or principal adoption                NOT PERFORMED
```

### 1.3 Word-boundaried search terms

```text
Gen_Omega | P_src | rooted signed-incidence | Q-242 | root-not-bag
common origin | fixed point | transient | p_ch | B1 ... B14
K_square | 1088 | filtration | E_post | C1 ... C8 | ready | pointer
```

### 1.4 Principal sources

| Artifact | SHA-256 | Use |
|---|---|---|
| `STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V001.md` | `f2043a2a68d983430c96ff33f98675b0bf2740edd235616b25d3c956017e148f` | review target |
| `STAGE8_TASK4A_MISSING_PHYSICAL_LAYER_CONSOLIDATED_SPEC_AND_CONSTRAINT_BATTERY_V001.md` | `241bf43f04aed7f215bad6ea80170a9c7733000896df839ac80974769d0a46c3` | B1-B14 standards |
| `STAGE8_MINIMAL_OMEGA_P5_COMMON_ORIGIN_ROLE_REALIZATION_ATTEMPT_V001.md` | `576da30f300a0362469d6b4f447423a2298efc0dd28a60f38057e7f4cc8bd888` | Q-242 countermodel and root-not-bag test |
| `STAGE8_P5_COMMON_ORIGIN_DESCENT_REQUIREMENT_V001.md` | `a33be83c1ee7cbfbda2cc3857425cb9e7e90a23bbe3d61c9ec89432e50b77874` | executable common-origin descent standard |
| `STAGE8_LAW_READY_STATE_SEALED_COMMON_ORIGIN_DETERMINATION_V001.md` | `6745b3c5d08d1c1df89dbcbce301ce66315bf640c26ff41332f77e456f477c7a` | ready/pointer exchange and missing ready selector |
| `STAGE8_SOURCE_COUPLED_RECORD_TRANSITION_LAW_ADOPTION_PROPOSAL_V002.md` | `db1808e4da38cbfed8b12017885aff1bf63b0378e9971c37294e21fa08766fee` | exact E_post law and C1-C8 |
| `DECISION_OF_RECORD_009_THE_TRANSITION_LAW_RATIFIED_E_POST_2026-08-02_V001.md` | `11632fa30dfe9225c228f07a3be4717c73bdfc9e38b0c76c46d905d3fe193bc5` | ratified law authority |
| `STAGE8_TASK2F_FINITE_INCIDENCE_REALIZATION_FUNCTOR_FORCING_PROTOCOL_RESULT_V001.md` | `a4d8b9c44fd0705ba97fd49d1e0c8373c28e12e2c3acea9409b60217b274a0f8` | 1,088 filtration family and one-cell nonselection |
| `STAGE8_FINITE_INCIDENCE_REALIZATION_FUNCTOR_ADOPTION_PROPOSAL_V001.md` | `81446652aad65636174501ae1530f2a03fc6e9dcfbac4efd91927128d75c30b6` | Q-248 selection trap |
| `STAGE8_TASK4D_STITCHING_THEOREM_GERM_INDEPENDENT_HALF_V001.md` | `430f09715146cc03dabb0e349c422ae2499cff893d4e46b490fc0870954d1cb4` | J_ref type and geometric-limit boundary |

## 2. Frozen target content

G1 is stated at the target's lines 177-187. It admits every normal,
charge-covariant CPTP map on trace-class source operators satisfying

```text
Fix(P_src) intersect {positive trace-class, trace one} = {rho_S},
P_src^m(tau) -> rho_S
```

on the declared charge-superselected basin, and commuting with the
`P_0/P_ch` conditional expectation.

G3 is stated at lines 188-209. It is a finite one-cell object with vertices
`v_0`, `v_1`, `v_perp`, a unitary map to the ready/pointer/complement carrier,
and the signed operator

```text
S_inc v_0    = v_1,
S_inc v_1    = v_0,
S_inc v_perp = -v_perp.
```

The generated E_post law is stated at lines 300-305. The Q-242 defense is at
lines 370-439. The p_ch claim is at lines 446-474. The battery table is at
lines 508-530, and the proposal's own reparameterization kill condition is at
lines 612-630.

## 3. A1 -- selection trap

### 3.1 Type comparison

The G3 primitive and the 1,088-member family are not instances of the same
type.

```text
G3 member:
  one finite oriented cell;
  one root/successor/complement decomposition;
  one unitary representation on C^3;
  one local signed write.

K_square filtration member:
  one linear extension of four vertices and four edges;
  boundary-before-edge ordering on eight cells;
  one global support filtration for a realization functor.
```

The forcing result states at lines 277-305 that the one-cell base map does not
map the sequential label carrier to a vertex, edge, or chain carrier and
constrains no cell order. It states at lines 423-490 that all 1,088 global
filtrations survive. Even adding the extra rule that one named K_square vertex
comes first leaves 272 members, not one.

### 3.2 Relation between the families

No injective or surjective map from G3 members to K_square filtrations is
specified or induced by the data. The compatibility relation is instead
many-to-many: a fixed local G3 member is compatible with every one of the
1,088 global filtrations, and each filtration can carry the same local G3
data.

G3 therefore does not smuggle a selection among the 1,088. What it adds is
different physics: a local root-to-ready orientation and complement sign.
It does not supply J_ref's cells, boundaries, global refinement ordering,
source-incidence map, or geometric intertwiner.

```text
A1_VERDICT = SURVIVED
G3_IS_A_K_SQUARE_FILTRATION_SELECTION = false | TYPE-R |
  test: domain/codomain comparison and all-1088 compatibility
G3_UNBLOCKS_TASK4D_J_REF = false | TYPE-U |
  would-build: the complete geometric realization package listed by Task 4d
```

Q-259's suggestion that G3 might also unblock 4d is therefore not supported by
the type comparison.

## 4. A2 -- hostile family-level Q-242 countermodel

### 4.1 Replacement-channel subfamily

Let `rho` be any normalized positive charge-superselected trace-class source
state. Define

```text
R_rho(tau) = Tr(tau) rho.
```

This map satisfies G1 exactly:

1. It is linear and normal on the trace class.
2. It is completely positive: it is the measure-and-prepare channel with the
   sole scalar measurement `Tr` and prepared state `rho`.
3. It is trace preserving because `Tr(R_rho(tau))=Tr(tau)Tr(rho)=Tr(tau)`.
4. It is charge covariant because charge superselection gives
   `U rho U^*=rho`, hence `R_rho(U tau U^*)=U R_rho(tau) U^*`.
5. It commutes with the superselection conditional expectation `E`:
   `E R_rho(tau)=Tr(tau)rho=R_rho E(tau)`.
6. It is mixing in one step: every normalized `tau` is sent to `rho`.
7. Its unique normalized positive fixed point is `rho`.

Thus the map

```text
rho -> R_rho
```

embeds the complete old state family into the proposed G1 family without
adding independent preparation content.

### 4.2 Q-242 states

Apply the construction to Q-242's two concrete states `rho_S^(0)` and
`rho_S^(ch)`, while holding G3, character, E_post, histories, tensor grammar,
carrier, and law fixed. Then

```text
P_src^(0)  = R_(rho_S^(0)),
P_src^(ch) = R_(rho_S^(ch)).
```

Each fixed channel has one fixed state, exactly as V001 says. But the family
choice `P_src^(0)` versus `P_src^(ch)` is identical in information content to
the old choice `rho_S^(0)` versus `rho_S^(ch)`. The law remains unchanged.

The fixed-member statement therefore proves only the tautology that a fixed
channel has its fixed point. It does not prove that the channel family is a
common origin rather than a re-encoding of the independently supplied state.

```text
A2_VERDICT = KILLED
Q242_FIXED_MEMBER_UNIQUE_FIXED_POINT = true
Q242_FAMILY_LEVEL_STATE_FREEDOM_REMOVED = false | TYPE-R |
  test: rho -> R_rho embeds both Q-242 states with the same law
GEN_OMEGA_V001_SURVIVES_Q242_AT_ORIGIN_LEVEL = false | TYPE-R |
  test: replacement-channel subfamily
```

This is the proposal's own Section 10.5 kill condition, now supplied with a
concrete admitted witness.

## 5. A3 -- the four conditional battery rows

### 5.1 Accounting

The battery table explicitly marks only three rows conditional:

```text
B5  RetHess_phys class                    CONDITIONAL/DOWNSTREAM
B6  physical tail structure              CONDITIONAL/DOWNSTREAM
B9  consumer-specific tail certificate   CONDITIONAL/DOWNSTREAM
```

Yet the summary says four conditional rows. The target's P5 certificate table
at lines 480-501 marks Parent-State common provenance conditional, and B14's
row says `PASS ... with G1 weakness disclosed`. The only coherent reading of
the stated count is that B14/common origin is the fourth conditional.

```text
EXPLICIT_CONDITIONAL_ROWS_IN_BATTERY_TABLE = 3
CLAIMED_CONDITIONAL_COUNT = 4
FOURTH_CONDITIONAL = B14_COMMON_ORIGIN [ONLY COHERENT READING]
```

### 5.2 Classification

| Row | Condition | Class |
|---|---|---|
| B5 | construct P2-P6 and prove the physical response lies in a ratified separation class | downstream construction, dischargeable |
| B6 | construct P2-P6 and instantiate the physical tail/restrictions | downstream construction, dischargeable |
| B9 | build the selected consumer and prove its tail certificate | downstream construction, dischargeable |
| B14 | accept G1 as common-origin physics despite the unresolved reparameterization test | circular |

B14 requires an executable descent certificate, not a bundle or renamed
output. Saying that it passes if G1 is accepted as origin physics assumes the
very proposition the DoR-013 gate is testing. The replacement-channel
subfamily shows the missing condition is substantive, not clerical.

```text
A3_VERDICT = KILLED
BATTERY_ACCOUNTING_IS_SELF_CONSISTENT = false | TYPE-R |
  test: explicit row count versus stated 10/4/0 count
B14_DISCHARGE_IS_NONCIRCULAR = false | TYPE-R |
  test: G1 acceptance is used as the premise establishing G1 common origin
B14_COMMON_ORIGIN_PASSES_FOR_V001 = false | TYPE-R |
  test: replacement-channel subfamily
```

The first three conditionals are legitimate downstream obligations. B14 is
not downstream and cannot be deferred to P2-P6.

## 6. A4 -- d_law fidelity to DoR-009

The law was recomputed from the proposal's definitions and compared with the
ratified E_post formula at the source-law V002 lines 282-392:

```text
D_(n,j)[A_j]
  = |r_j><r_j| + z_(n,j)[A_j]|p_j><p_j| + |e_j><e_j|,

W_N^(n)[A] = tensor_j (D_(n,j)[A_j] S_j),

U_N^(n)[A]
  = P_0 tensor I_(3^N) + P_ch tensor W_N^(n)[A].
```

The proposal's `D_n`, `S_inc`, tensor product, and controlled source
decomposition reproduce this formula exactly. Certificate-by-certificate:

| Certificate | Independent result |
|---|---|
| C1 zero-source reduction | PASS: `D_n[0]=I`, hence the exact sealed write |
| C2 equal-history baseline | PASS: unitary branch factors cancel |
| C3 ready/pointer dephasing | PASS: same controlled source decomposition |
| C4 gauge/CTP covariance | PASS with the ratified E_post endpoint representations |
| C5 charge/flux access | PASS: the character is on the written/post endpoint |
| C6 one-cell authority | PASS: exact `S` and `D_n S` matrices |
| C7 sequential compatibility | PASS: zero extension appends `S` factors |
| C8 character/reality | PASS: faithful conjugate pair `n=+1,-1` |

```text
A4_VERDICT = SURVIVED
D_LAW_EQUALS_DOR009_E_POST = true | TYPE-P | premises: DoR-009
C1_C8 = PASS
```

No lookalike-law drift was found.

## 7. A5 -- ready/pointer exchange

The sealed law result states at lines 315-385 that, at zero history,

```text
W_N[0]|R_N> = |P_N>,
W_N[0]|P_N> = |R_N>.
```

Thus the law does not select the ready endpoint. G3 does: it labels `v_0` as
root/ready and `v_1` as successor/pointer. This breaks the ready/pointer
exchange symmetry at the preparation-origin level while leaving the law
operator itself unchanged.

That breaking is not a contradiction with DoR-009. It is new authored physics,
which a proposal may expose. But the V001 choice table does not list the
exchange-related alternative in which `v_1` is root and `v_0` is successor,
and no sealed text forces one member of that pair.

```text
A5_VERDICT = WOUNDED
RATIFIED_LAW_READY_POINTER_EXCHANGE_PRESERVED = true
G3_ORIGIN_IS_READY_POINTER_EXCHANGE_INVARIANT = false | TYPE-R |
  test: interchange v_0 and v_1 while holding S_inc fixed
SEALED_RULE_SELECTING_G3_ROOT_ORIENTATION_FOUND = false | TYPE-S |
  roots: Section 1.1
  exclusions: Section 1.2
  query: "ready|pointer|root|exchange|orientation|E_post"
```

Repair required: add the exchanged-root member to the choice table, state the
physical distinction, and price the root orientation as an explicit authored
choice. This repair does not cure A2 or A3.

## 8. A6 -- p_ch parameterization honesty

### 8.1 Span and target blindness

Let `rho_0` and `rho_ch` be normalized states supported on `P_0` and `P_ch`.
For symbolic `p` in `(0,1)`, define

```text
rho_p = (1-p) rho_0 + p rho_ch,
P_src,p = R_(rho_p).
```

Then `P_src,p` is an admitted G1 member and

```text
Tr(rho_p P_ch)=p.
```

So the proposal family really spans the full disclosed open p_ch interval.
The G1 membership conditions do not mention a response, coupling, stiffness,
root, measured value, or downstream target. No directional narrowing of p_ch
was found.

### 8.2 The one-to-one claim is false

For any fixed admitted `rho` and symbolic `lambda` with `0<=lambda<1`, define

```text
P_(rho,lambda)(tau)
  = lambda tau + (1-lambda) Tr(tau) rho.
```

Every member is normal, CPTP, charge covariant, commutes with the conditional
expectation, has the same unique invariant state `rho`, and is mixing. Distinct
`lambda` give distinct transient preparation channels but exactly the same
`p_ch`. Therefore `P_src -> p_ch` is many-to-one, not one-to-one.

```text
A6_VERDICT = WOUNDED
P_CH_OPEN_INTERVAL_SPANNED = true
TARGET_AWARE_NARROWING_FOUND = false | TYPE-S |
  roots: Section 1.1
  exclusions: Section 1.2
  query: "p_ch|response|kernel|coupling|stiffness|root|measured"
P_CH_IS_PARAMETERIZED_ONE_TO_ONE_BY_P_SRC = false | TYPE-R |
  test: P_(rho,lambda) family at fixed rho
P_CH_IS_PARAMETERIZED_MANY_TO_ONE_BY_P_SRC = true
```

Repair required: replace `one-to-one` with `surjectively and many-to-one over
the disclosed p_ch interval`. This is an accounting repair only; it does not
cure the origin-level kill.

## 9. A7 -- finite authority at the origin

Neither proposed primitive is tail-typed.

G3 is a finite one-cell incidence object represented on `C^3`. Every datum in
it is visible in its finite matrix, root inclusion, and one-cell law.

G1 is a map on trace-class source operators. Its fixed-point content is visible
in the generated finite state. Its transient content also has finite witnesses:
for `P_(rho,lambda)` and `P_(rho,mu)`,

```text
P_(rho,lambda)(tau)-P_(rho,mu)(tau)
  = (lambda-mu)(tau-Tr(tau)rho),
```

which is nonzero for a finite charge-superselected probe `tau` not proportional
to `rho`. No weak-* tail, bidual-only datum, or object killed by every finite
restriction is needed to distinguish the channels.

The corpus currently has no sealed consumer of that transient action, as V001
correctly reports at lines 612-625. That absence matters to A2/B14 because V001
does not require the independent witness. It does not turn the primitive into
a restriction-invisible tail.

```text
A7_VERDICT = SURVIVED
G3_HAS_FINITE_SHADOWS = true
P_SRC_FIXED_POINT_HAS_FINITE_SHADOWS = true
P_SRC_TRANSIENT_HAS_A_FINITE_FAILURE_CAPABLE_WITNESS = true
P_SRC_TRANSIENT_HAS_AN_EXISTING_SEALED_CONSUMER = false | TYPE-S |
  roots: Section 1.1
  exclusions: Section 1.2
  query: "P_src|preparation channel|transient|iterate|mixing"
ORIGIN_REQUIRES_BIDUAL_OR_RESTRICTION_INVISIBLE_CONTENT = false | TYPE-R |
  test: explicit finite G3 and finite P_(rho,lambda) witnesses
```

## 10. Combined verdict

| Attack | Verdict | Decisive reason |
|---|---|---|
| A1 selection trap | SURVIVED | local one-cell root is not a global K_square filtration |
| A2 family countermodel | KILLED | replacement channels re-encode arbitrary state choices |
| A3 four conditionals | KILLED | B14 is both mis-accounted and circular; replacement witness fails it |
| A4 d_law fidelity | SURVIVED | exact DoR-009 E_post formula and C1-C8 |
| A5 ray exchange | WOUNDED | G3 openly breaks the exchange, but omits the exchanged-root alternative |
| A6 p_ch honesty | WOUNDED | full span and blindness survive; one-to-one claim is false |
| A7 finite authority | SURVIVED | both primitives have explicit finite witnesses |

```text
ATTACKS_KILLED = 2
ATTACKS_WOUNDED = 2
ATTACKS_SURVIVED = 3

OVERALL = DEAD
```

V001 is not repair-then-ready because the killing defect is the proposed
origin's central information structure, not a missing disclosure. A lawful
successor would need, before another ratification gate:

1. a G1 family that excludes the information-free replacement subfamily, or
   an equivalence quotient proving why those members are not physical origins;
2. an independently failure-capable finite transient/preparation certificate
   required of every admitted member, not merely available for some members;
3. a consumer or operational map through which that transient datum matters
   independently of the invariant state;
4. a rerun of Q-242 and B14 against that narrower family;
5. the exchanged-root choice and the corrected many-to-one p_ch accounting.

Those requirements amount to a new origin proposal, not a narrow edit of V001.
No such successor is authored here.

```text
GEN_OMEGA_V001_STATUS = DEAD
DOR_013_MAY_RATIFY_V001 = false | TYPE-R |
  test: A2 and A3

GEN_OMEGA_CONCEPT_REFUTED_IN_ALL_FORMS = false | TYPE-S |
  scope: only V001's declared G1/G3 family was tested

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
