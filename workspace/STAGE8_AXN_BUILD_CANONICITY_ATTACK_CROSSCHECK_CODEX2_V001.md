# STAGE 8 — AXN BUILD — `U2SQ-FINITE-CANONICITY-ATTACK` CROSS-CHECK
## CODEX 2 LANE (Builder A) — RELAY 861 — [PLAN:AXN-BUILD-A28]

```text
alpha_computed         = false
proof_authorized       = false
kappa_record_computed  = false
```

No member is bound; no fixed point is executed; no end test is run; no smooth
carrier is imported; no EM identification is made.  The numbers below are
finite-dimensional residuals and Hilbert–Schmidt diagnostics of the sealed
dimension-108 operator identity.  No physical quantity is numerically evaluated
and no measured constant is compared.  PE-1 through PE-12 remained pointer-only,
unopened and unsearched.

**CLAIM STATUS: all headline items CLAIMED.**

## 0. Lead

The scalar arithmetic in Dario's 860 is reproducible, but its decisive grading
probe is not.  The sealed cellular grading does **not** merge `T1` with `T3`.
It makes `T1` and `T2` even and `T3` odd.  Consequently it supplies canonical
operator-space projectors

```text
P_even(A) = (A + G A G)/2,
P_odd(A)  = (A - G A G)/2,
G         = I_source tensor (Gamma_cell tensor Gamma_cell),
```

and, at the sealed finite parent,

```text
P_even(D_K^2) = T1 + T2,
P_odd(D_K^2)  = T3
```

to exact arithmetic zero.  The pair `{T1+T2,T3}` is therefore not merely an
"orthogonality ceiling": it is the unique parity-projector output of the sealed
grading.  Dario's half-split and `exp(i D_K)` rotation remain correct raw
identities, but neither defeats these projectors.  The half-split is not a
projector output, and `exp(i D_K)` does not preserve `G`.

The corrected verdict is therefore typed at three levels:

1. the displayed **three-term** census is not canonical under the available
   law: its `T1/T2` refinement of the even block has no sealed second projector;
2. the finite **two-block** census is canonically selected by the sealed grading
   and earns `INSTANCE_ONLY` at this parent;
3. a generic/universal `U2_sq` law remains unproved and unpromoted.

Thus 860's blanket `VERDICT = NONCANONICAL`, its "no mechanism derivable"
statement, its "even the two-block census fails" statement, and the asserted
invariance-stock absence require correction.  `NONCANONICAL` remains the right
word only when its object is explicitly the displayed three-term refinement;
it is not a verdict on every decomposition available at the parent.

## 1. Custody, independence, and closed inputs

Pickup ACK and lane guard were satisfied before reading.  The relay was
seal-verified as `c55a0eee5a231045e8cb51447bf9b187648b2208e6d77c5b993b87c2ef17bd16`.
The required state brief was verified and read at
`e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`.
Dario's subject was verified before reading:

```text
STAGE8_AXN_BUILD_U2SQ_FINITE_CANONICITY_ATTACK_DARIO_V001.md
SHA-256 = 5298e98ad732ca398973e0b0132d28f07700faa0794303906f3057c4a8c67d41
seal     = OK
```

The group sidecar
`R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_V001.seal.sha256` was run with
`shasum -c`; all nine members passed.  The relevant member digests independently
recomputed to:

| member | SHA-256 |
|---|---|
| parent SPEC | `40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9` |
| parent RESULT | `345d447eaf6d730caa6fa655b92a7b0cd93a68b5f86e0c8929cf969f40aeb7cb` |
| result JSON | `7f83d081b1e7eb03c07acfecc0255b17f728304152c65ef88e0c076d0b9b8539` |
| audit source | `8cf5bfcb172ac848f143aa70d9ac26bb90476fe6a074b1daf1d95fe08cf705d7` |
| independent verifier source | `1e7a3deae68b140afcb03b9f1d2b827a3956923a15a83ba3886343c1dbfdc807` |
| test source | `4570ecbd69c10aea657ef813ebd62292e18fa0d442dc1dbdb0b14f692ae2fab4` |
| verification JSON | `5902ab9aef714bbd8330d3b49c3ee7dd31cff2c942ba23eefef8986d389c5682` |
| self-review | `04c2c0ca8dc226e721df7f7c91231c9e8e4c69fc9ded7c803a0da1691e6218a0` |

I did not execute the sealed audit or verifier.  I reimplemented the matrices
directly from the sealed definitions in an independent scratch process.  The
parent SPEC's carrier/grading display is at bytes `[4934,5576)` (span SHA-256
`3f33b2a7b6afb9f3999ea5aaaeb720497d8ccd8cea37d3f5496e8d694720af98`);
its generated-square identity is at `[6867,7476)` (span SHA-256
`a4d3ed9969072152b1670fe5e88d57200d464ce51a564e625daee98fcb52e804`).
The parent RESULT's published descendant numbers are at `[998,1863)` (span
SHA-256 `7b9596e6181cc967b7df0f927fd4ccb1568014304f20cf84a3b6775fd312f322`).

The grading law is not an invented repair.  The parent SPEC hash-pins the
sealed packet member
`review_packets/STAGE7_QSPEC_CANDIDATE_V001/BID_GRADED_BOUNDARY_SUPERCONNECTION_REPAIR_V001.md`
at
`2215f79cbe69f1de1643427ad5d422b0c3064ff758327e43ff1629de8633f72d`.
The exclusively cited sealed packet copy matches that digest and its packet
manifest.  Its cellular grading is at bytes `[344,505)` (span SHA-256
`d2a52b849c04a3cc864752c468ca3c0ce8d5997816aa85a7ccb42ed6a4fc7571`);
its record-odd quadrature and graded-curvature law are at `[1166,1936)`
(span SHA-256
`08a06d3e7011aa0bfb0a3323b29dfb3bdeb2c5acf926e1f9f8d6de29458e7029`).

## 2. Independent reconstruction and the five requested checks

### 2.1 Reimplementation

I constructed the Dirac matrices, `alpha_x`,
`source_incidence_spin=-i gamma0 gamma5`, the cyclic three-site first
difference, the two source masks, and the two record embeddings of
`c_partial` directly.  With

```text
h = h_free
W = write_0 + write_1
D_K = h + W
T1 = h^2
T2 = W^2
T3 = sum_s -i kron([derivative,mask_s],
                    alpha_x source_incidence_spin,
                    record_incidence_s)
```

the scratch implementation returned:

```text
dimension                              108
||D_K-D_K*||                           0
||D_K^2-(T1+T2+T3)||                   0
||T1||                                 6.363961030678928
||T2||                                27.712812921102035
||T3||                                 9.797958971132712
overlap-descendant norm               16.000000000000
derivative-support descendant norm     9.797958971133
```

This confirms reconstruction and the requested twelve-decimal JSON
agreements.

### 2.2 Gram probe

The independent Hilbert–Schmidt Gram matrix is exactly the one in 860:

```text
            T1        T2        T3
T1        40.5      96.0       0.0
T2        96.0     768.0       0.0
T3         0.0       0.0      96.0
```

So `<T1,T2>=96` and `T3` is exactly orthogonal to both.  This refutes mutual
Hilbert–Schmidt orthogonality of the **three named terms**.  It does not refute
all projector mechanisms.  In particular, the sealed grading acts on operator
space and produces two orthogonal eigenspaces.  Also, "maximal orthogonally
separable" is valid only among coarsenings obtained by unions of the three
named terms; without that scope, arbitrary linear recombination makes the word
"maximal" too broad.

### 2.3 The grading probe — corrected

For each record factor the sealed law gives
`Gamma_cell=diag(+1,+1,-1)` and
`Gamma_cell c_partial + c_partial Gamma_cell=0`.  The two-record grading is

```text
G = I_12 tensor (Gamma_cell tensor Gamma_cell).
```

The independent checks are:

```text
||G^2-I||                               0
||Gamma_cell c+c Gamma_cell||           0

component      ||G Ti G-Ti||      ||G Ti G+Ti||      parity
T1                       0       12.727922061358      EVEN
T2                       0       55.425625842204      EVEN
T3         19.595917942265                       0    ODD
```

This follows structurally too: `h` is record-even and `W` is record-odd, so
`h^2` and `W^2` are even while `hW+Wh` is odd.  Therefore:

```text
||P_even(D_K^2)-(T1+T2)||               0
||P_odd(D_K^2)-T3||                     0
||D_K^2-(P_even(D_K^2)+P_odd(D_K^2))||  0
<P_even(D_K^2),P_odd(D_K^2)>            0
projector idempotence residuals         0 / 0
```

The subject's partial-source-trace diagnostic is not the cellular grading.
My direct trace over the 12-dimensional source factor gives record-operator
norms `18.0`, `78.383671769062`, and `0.0` for `T1,T2,T3`, respectively.
Thus that diagnostic does not yield the claimed `T1/T3` merge either.  The
sealed grading's actual merge is unambiguously `T1+T2`.

### 2.4 Control 1 and the top-level token absences

The arithmetic is confirmed:

```text
D_K^2 = T1 + T2 + (1/2)T3 + (1/2)T3
residual = 0
raw additive count = 3 -> 4
D_K and D_K^2 unchanged
```

The literal two-file counts are also confirmed:

```text
token             SPEC / RESULT
canonical          0 / 0
irreducib          0 / 0
refine             0 / 0
component count    0 / 0
```

But the inference "nothing in the bundle bans refinement" does not survive a
meaning probe through the SPEC's own closed authority table.  A canonical
projector law need not contain the token `refine`: it defines its component
census as its projector images.  Two copies of half of the odd image are a
true additive identity but are not two outputs of `P_odd`.  The half-split is
therefore not an admissible counterexample to the sealed parity census.

It still diagnoses the absence of a **finer** law if someone wants to retain
three or four named summands.  It does not make the canonical two-block output
noncanonical.

### 2.5 Control 2 and its actual limit

For `U=exp(iD_K)`, formed by independent Hermitian diagonalization:

```text
||UU*-I||                              2.335194327910e-14
||U D_K U*-D_K||                      4.413364215790e-14
||U D_K^2 U*-D_K^2||                  8.725292753475e-14
||sum_i U Ti U* - D_K^2||             8.681820368036e-14
component displacements               4.084814603655 /
                                     10.249148106279 /
                                     10.534447921371
component norms                       preserved
```

Those numbers and the statement that `U` commutes with `D_K` are confirmed.
The control's relevance is narrower than 860 states because the sealed input
is graded:

```text
||UG-GU||                              15.260879872746
```

The rotated individual terms are not parity-homogeneous.  Projecting their
invariant sum with the sealed grading recovers the same canonical blocks:

```text
||P_even(sum_i U Ti U*)-(T1+T2)||      6.371845480920e-14
||P_odd(sum_i U Ti U*)-T3||            5.896913605448e-14
```

Thus the rotation is a symmetry of `D_K` alone, not of the structured pair
`(D_K,G)`.  It remains a valid warning against any law claiming that the
three displayed construction terms are functions of `D_K` alone.  It is not a
counterexample to the grading-projector pair.  Under a covariant change of
presentation, both `D_K` and `G` conjugate and the projector outputs conjugate
with them.

## 3. Verdict ordering

The stop table must name its object.  With that correction:

| object | verdict | reason |
|---|---|---|
| displayed `{T1,T2,T3}` census | **NONCANONICAL AS DISPLAYED** | the sealed grading merges `T1,T2`; no second closed projector on the even block is supplied |
| grading census `{T1+T2,T3}` | **INSTANCE_ONLY** | canonical projector images are derived exactly at this finite parent; no generic promotion |
| universal `U2_sq` | **LAW_GAP / NOT PROMOTED** | generic `U1`, an even-sector splitter if three terms are required, and universal covariance/uniqueness are not proved |

`NONCANONICAL` is therefore not "control-1-carried, unconditional" over all
parent decompositions.  The half-split is unconditional as arithmetic; its
status as an admissible competing **component census** is law-dependent.  The
sealed grading supplies that law for two blocks and rejects the split as a
non-output.  For the displayed three-term refinement, `NONCANONICAL` remains
the primary outcome because the only derived component law coarsens it; the
unprovided finer law is also a `LAW_GAP`.  860's refusal to fire
`INSTANCE_ONLY` for the two-block result is corrected.

## 4. Invariance and law-9 closure

The `0/0` top-level occurrence counts for `relabel`, `permut`, `admissible`,
and `equivalen` across SPEC/RESULT are literally correct.  They do **not**
support the positive absence "the bundle seals none."  The SPEC exposes a
closed list of 15 content-addressed authorities, and the sealed result JSON
records `authority_hashes_match=true`.  I verified all 15 current bytes
against those pins.  Law 9 therefore requires traversing that list before
booking an absence.

One pinned packet authority,
`review_packets/STAGE7_QSPEC_CANDIDATE_V001/BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md`
(`949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd`),
states at bytes `[3195,3878)` (span SHA-256
`b21b7bb5b70f3c8f5b464e50e89c9f4dd5a395b5bb8bfa80560f4a4c8217994f`)
that vertex relabeling conjugates the finite parent by the induced source
permutation and that cell-orientation reversal is accompanied by the cellular
orientation unitary; its status block records both covariance results.  A
second pinned packet authority,
`review_packets/STAGE7_QSPEC_CANDIDATE_V001/BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md`
(`b786db3adec8cc335967d49ec13b59923d67f424644f72c535b27b579dd1489f`),
states at `[994,1416)` (span SHA-256
`7fbe4fdb070825937154c27f24519cddea9b5dbaf3c6c31a0140d91f78a1fd67`)
the admissible multiplicity-basis source equivalence and its naturality
requirement.

So:

- Dario's isolated record-factor swap result is numerically confirmed:
  `||SW D_K SW-D_K||=13.856406460551`;
- it is not the sealed relabeling action, which expressly includes the induced
  source permutation/orientation conjugation;
- declining to **invent** an additional compensating group was lawful, but
  declaring the admitted-action stock absent without following the pinned
  authority closure was not;
- the parity projector is automatically covariant under any admitted unitary
  action that conjugates `D_K` and `G`, so no new group is needed to establish
  this finite naturality statement.

The invariance finding is therefore corrected from blanket `LAW_GAP` to:
**finite admitted actions are present and the parity pair is covariant; a
complete universal equivalence class for a future generic `U2_sq` law remains
open.**

## 5. Supplier hunt and exact reopen condition

The law-9 hunt used the complete 15-authority list declared by the parent SPEC,
plus all nine group-sidecar members.  It found a partial supplier, not an empty
stock:

1. the graded-boundary repair supplies the cellular grading, record oddness,
   and the exact even/odd curvature split;
2. the global-boundary descent supplies finite vertex-relabeling and
   orientation-reversal covariance;
3. the controlled-coupling derivation supplies an additional named source
   equivalence/naturality class;
4. the graded-boundary repair's bytes `[4305,4753)` (span SHA-256
   `2ffaaac737f346c72fbc206b00719247e6219fa26f556f076778ed5c0feeade3`)
   separately preserve differential order and BID incidence degree, a possible
   **input** to a future finer law, but do not themselves define the missing
   even-sector projector.

To reopen the **three-term** route, a future sealed law must supply all of:

```text
1. a closed invariant or projector that splits P_even(D^2) into T1 and T2;
2. its exact domain and carrier, including which formal differential/incidence
   data survive representation and are inputs rather than retrospective labels;
3. reconstruction and uniqueness/idempotence/orthogonality checks for the
   resulting complete component census;
4. a closed no-refinement/component-count rule, so duplicate scalar splits are
   rejected by the law rather than by preference;
5. the admitted equivalence/relabeling action and a covariance proof for every
   projector under it;
6. a scope statement: finite-parent only, or a proof over generic U1 sufficient
   for universal promotion.
```

No enumerated source seals item 1 as a closed even-sector receiver, so the
three-term route is not reopened here.  The existing grading already reopens
and closes the **two-block finite** question at `INSTANCE_ONLY`; it supplies no
generic `U1` promotion.  Nothing in this finding identifies `U2_sq` with
`U2_phys` or `Delta_Gamma`.

## 6. Concession scope and law-8 log

### 6.1 Concession

860's concession of my 859 correction is correctly scoped.  The sealed U2
census (`981f195444261b0aafdb3ce62a75d1a1ab907d197a23e77b29016b6fd427af77`),
bytes `[2324,5131)`, distinguishes `U2_sq`, `U2_phys`, and `Delta_Gamma` and
shows the absent cross-object bridge.  Therefore:

```text
857 ROW_TYPE = NEITHER-FORCED                  STANDS
857 deciding object at Delta_Gamma level      STANDS
857 sentence routing Delta_Gamma to U2_sq     FALLS
```

The present parity correction concerns only `U2_sq`; it does not repair the
missing bridge and does not alter that residue.

### 6.2 Law 8

Locked law 8 names three base seal modes: `.md.seal.sha256`, the spelling that
drops `.md`, and packet-manifest membership.  The parent is carried by a fourth
**group-sidecar** shape:

```text
R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_V001.seal.sha256
```

whose filename drops `SPEC`/`RESULT` and whose contents seal nine members.
This is confirmed and logged as the fifth observed instance of the additional
group-sidecar mode in the current sequence.  The safe name is "group-sidecar
mode"; the phrase "fifth fourth-mode instance" conflates occurrence ordinal
with mode ordinal.

## 7. Freedoms consumed and flattening check

```text
CARRIED UNCHANGED:
  the sealed dimension-108 parent; h_free, masks, c_partial, record embeddings,
  D_K, and the three displayed terms exactly as defined; the finite scope; the
  three-object U2_sq/U2_phys/Delta_Gamma typing; generic U1 absent; no physical
  interpretation assigned to any structural residual.

DERIVED HERE:
  one independent matrix replay; the Gram matrix; the actual cellular-parity
  classification; the two exact projector images; control diagnostics; the
  complete 15-authority closure and its relabeling/equivalence hits.

SELECTED HERE:
  nothing.  Gamma_cell was already sealed and hash-pinned by the parent SPEC.
  G is its forced tensor-product action on the two already sealed record
  factors.  No new coefficient, basis, component count, equivalence, or
  relabeling is chosen.

NOT DONE:
  no generic U1 law; no even-sector T1/T2 projector; no universal promotion;
  no Delta_Gamma theorem; no U2_phys identification; no chain invocation.

SCALING WEIGHTS:
  none consumed.  The 1/2 factors occur only in the attacked raw identity and
  are not adopted as components.
```

**FLATTENING CHECK: 37/37 walked, clean.**  S03 and the void condition are
load-bearing: the missing even-sector splitter is reported, not written.  S12
holds every source at its sealed status.  S26/S08/S19/S24 remain untouched;
finite matrix data are not promoted into a smooth or physical result.  T1/T5
remain untouched.  The producer-declared three-term display receives no weight
toward its own canonicity; the positive two-block result rests instead on the
independently sealed packet grading and the cross-checked matrix identities.
`F_PLDEC = PASS`: every reported number is an algebraic residual, trace, norm,
or finite operator diagnostic; no physical observable is evaluated.
`ANTI_TUNING = PASS`: no target value, fitted coefficient, selected basis, or
post-evaluation adjustment enters the replay.

## 8. Final lines

```text
NUMBERS = CORRECTED (items 1, 2, 4, and 5 scalar arithmetic CONFIRMED at the reported values; item 3 corrected: the sealed grading makes T1,T2 EVEN and T3 ODD, with exact projector images P_even(D_K^2)=T1+T2 and P_odd(D_K^2)=T3)
GRAM = CORRECTED (entries CONFIRMED, including <T1,T2>=96 and exact T3 orthogonality; inference narrowed: this refutes mutual orthogonality of the three named terms, not the sealed grading projectors; two-block is canonically selected, not merely an orthogonality ceiling)
CONTROLS = CORRECTED (raw half-split and rotation numbers CONFIRMED; control 1 is unconditional only as additive arithmetic and is not an output of the sealed parity projectors; control 2 is conditional and does not preserve G, ||UG-GU||=15.260879872746; neither defeats the canonical two-block census)
VERDICT_ORDER = CORRECTED (displayed three-term census NONCANONICAL AS DISPLAYED; finite grading census {T1+T2,T3}=INSTANCE_ONLY; universal U2_sq remains LAW_GAP/not promoted; blanket NONCANONICAL and control-1-carried rationale rejected)
INVARIANCE_GAP = CORRECTED (top-level SPEC/RESULT 0/0 counts confirmed but the two-file enumeration is incomplete; the SPEC's closed 15-authority list contains sealed vertex-relabeling, orientation-reversal, and source-equivalence laws; finite parity pair is covariant, universal equivalence closure remains open)
CONCESSION_SCOPE = CONFIRMED (857 NEITHER-FORCED and Delta_Gamma-level deciding object stand; only the unproved routing Delta_Gamma -> U2_sq falls)
REOPEN_CONDITION = displayed (three-term route needs a sealed even-sector projector/invariant, domain, reconstruction+uniqueness, no-refinement census, admitted-action covariance, and scope; supplier hunt finds the sealed grading and finite covariance as partial suppliers, but no closed T1/T2 splitter and no generic U1 promotion)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+1: my 859 census called U2_sq a named law with no supplier; this complete parent-authority traversal finds a real partial supplier—the sealed cellular grading—and corrects my own prior supply classification to two-block INSTANCE_ONLY / finer split still absent)
```

Gates remain held: `alpha_computed=false`; `proof_authorized=false`;
`kappa_record_computed=false`; no member binding, fixed point, end test, smooth
import, EM identification, physical numerical evaluation, or comparison to a
measured constant occurred.
