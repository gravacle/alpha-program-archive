# STAGE 8 / 7A / [PLAN:C1-PRE-3] — E4 EXHAUSTION-THEOREM CROSS-CHECK

## Lead determination — CLAIMED

`E4a` survives the attempted refutation. On the exact `ARCH` class, the
operator `B` is defined once on `l2(V)` and every admitted exhaustion is only
a sequence of compressions of that same bounded operator. The strong limit is
therefore exhaustion-independent; cofinality is not used.

The stronger `E4b` proof sentence does not survive whole. Its finite-poset
connectivity lemma is correct, but `RED` does not turn every cofinal physical
exhaustion into a prefix chain, and `ARCH`'s strong convergence is a theorem
about incidence dynamics rather than completed-record states. The surviving
statement is the narrower, already packet-sealed `CDL` promotion result:
within the promoted ordinary `3+1` flat-asymptotic branch, two cofinal physical
exhaustions governed by the same parent give the same stabilized
completed-record restriction after both contain the observable's finite
causal support and its causal buffer. No stronger claim about arbitrary
cofinal finite-subcomplex exhaustions being globally related by `RED` swaps is
confirmed here.

The `GNS` compatibility identity is independently verified on its stated
canonical inductive chain. It supports the surviving completed-record result,
but is not, by itself, a theorem identifying arbitrary causal-complex
exhaustions with that chain.

All determinations in this report are this lane's `CLAIMED` cross-check
findings pending registrar treatment. `E4c` is not reopened or closed here.

## 0. Preflight, custody, and jurisdiction

| object | SHA-256 | result |
|---|---|---|
| `PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | pin and adjacent seal verified before task work |
| `STAGE8_C1_E4_VERIFICATION_DARIO_V001.md` | `b760e1b91c93154517ca15e7d93cbf15b490f9667147319b5d6293393ee12eaf` | subject seal verified |
| `STAGE8_C1_E4B_PROOF_AND_MOLLER_HUNT_DARIO_V001.md` | `162c6d7ddcd280f567645eb863828d86c3d9a8cd06f49c0641a4361ff8a1a0f5` | subject seal verified |
| packet manifest `review_packets/STAGE7_QSPEC_CANDIDATE_V001/STAGE7_PACKET_MANIFEST_V001.sha256` | `9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311` | mode-3 custody source |

The packet-manifest entries and the packet-copy bytes agreed for every source
used:

| packet source | SHA-256 | decisive lines |
|---|---|---:|
| `CAUSAL_DIRECT_LIMIT_ARCHITECTURE_ADJUDICATION_RESULT_V001.md` (`ARCH`) | `9be3f55fd527b9a857bdd4ea2298105e44a69e85db79b90772ecb30001aba022` | 73–103 |
| `CAUSAL_DIRECT_LIMIT_RECORD_PRINCIPLE_V001.md` (`CDLP`) | `625b4ed9c91b28dd15a2884498f980dcbb792c8b9cf9b13a743b2e8ec2bb8953` | 17–55 |
| `CAUSAL_DIRECT_LIMIT_REDUNDANT_RECORD_RESULT_V001.md` (`RED`) | `3359960fb411eff8ac0360a8c052bfc4d00a6281bd151c390fa3addd3603d05a` | 45–48 |
| `R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md` (`GNS`) | `10909b5c21e73ecf655462339a27bd645b8d35e3ad11fb6f8cb204c601992995` | 25–67 |
| `CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md` (`CIS`) | `b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30` | 18–36 |
| `FORK_8_CAUSAL_DIRECT_LIMIT_PROMOTION_SPEC_V001.md` | `ac73f30ae529f4ad3a789b7cc4318540b52275cf98fe2b0498c3ec40d8fec8dc` | 38–59 |
| `FORK_8_CAUSAL_DIRECT_LIMIT_PROMOTION_RESULT_V001.md` | `f84d5b5e8789e5e336db53265cc87dd25f5efddf1cd9c8931f1e521240125d4a` | 36–49 |
| `PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md` | `532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb` | 16–48 |

Only packet copies were used for these sources. The output name and both
sidecar spellings were absent before write. `PE-1` through `PE-7` were not
opened, were used only as pointer-known objects, and have zero evidentiary
weight.

The full standard gate remains in force: no alpha or kappa computation, no
member binding, no fixed-point execution, no end test, no physical numerical
evaluation, no comparison to measured constants, no smooth import, no EM
identification, and no channel decomposition selection occurred.

## 1. AS1 — independent derivation of `E4a`

### 1.1 One operator, not one operator per exhaustion

`ARCH` fixes a locally finite infinite causal complex `V` and the
unit-weight incidence generator

```text
B : l2(V) -> l2(V).
```

The carried bounded-incidence condition gives `||B||<infinity`. An exhaustion
`{V_n}` supplies only the coordinate projections `P_n` and the compressions

```text
B_n = P_n B P_n.
```

There is no exhaustion index on `B`, no boundary counterterm, and no
exhaustion-selected weight. Consequently two exhaustions of the same `V`
start from the same operator.

### 1.2 Strong convergence for every admitted exhaustion

For any `psi in l2(V)` and `epsilon>0`, choose a finite set `F subset V` whose
complement carries less than `epsilon` of the `l2` norm. An exhaustion
eventually contains `F`, hence `P_n psi -> psi`. Thus `P_n -> I` strongly.
The sealed estimate then gives

```text
||P_n B P_n psi - B psi||
 <= ||P_n B(P_n psi-psi)|| + ||(P_n-I)B psi||
 -> 0.
```

The family is uniformly bounded by `||B||`. Polynomial approximation of the
bounded exponential therefore yields

```text
exp(-it P_nBP_n) P_n psi -> exp(-itB) psi
```

strongly, uniformly for `t` in every compact interval. The right-hand side
contains no exhaustion data, so any second exhaustion `{W_m}` has the same
limit.

### 1.3 Counterexample attempts

| attack | outcome |
|---|---|
| reorder or irregularly grow the finite stages while retaining an exhaustion | `P_n -> I` still holds; the limit is unchanged |
| use an exhaustion whose stages have complicated boundaries | the compression estimate is boundary-shape independent |
| add an exhaustion-dependent boundary term to `B_n` | outside `ARCH`, which fixes `B_n=P_nBP_n` |
| use a sequence that revisits or permanently drops basis vectors | it need not have `P_n->I`, so it is not an exhaustion in the theorem's stated sense |
| use unbounded incidence | outside the carried bounded-incidence hypothesis |

No counterexample remains inside the sealed operator class. This confirms
`E4a` at exactly its stated strength: any two admitted exhaustions of the
same bounded-incidence `V` give the same dynamics. It does not compare two
different complexes or two different incidence generators.

## 2. AS2 — the four-step `E4b` proof under attack

### 2.1 Step-by-step verdict

| step | cross-check | verdict |
|---|---|---|
| 1. `RED` forces a linear extension | On a fixed finite set of writes, “causally dependent writes retain their causal order” means that any total write order respects the causal partial order. | **BOUND, but only after a write set and total write order are present.** |
| 2. prefixes are down-sets | Every prefix of a linear extension is an order ideal. | **THE COMBINATORIAL FACT IS TRUE; ITS APPLICATION TO EVERY PHYSICAL EXHAUSTION IS UNBOUND.** |
| 3. finite connectivity by adjacent incomparable swaps | The theorem is valid for every finite poset, not merely the random samples displayed by the subject. | **CONFIRMED on each fixed finite poset.** |
| 4. finite stages pass to the record-state limit through `ARCH` | Cofinality captures finite supports, but `ARCH` proves convergence of compressed incidence generators on `l2(V)`, not convergence or equality of completed-record states. | **TYPE MISMATCH; the cited limit carrier does not receive the claimed object.** |

### 2.2 The finite connectivity theorem

Let `L` and `L'` be linear extensions of a finite poset. Move the first
element of `L'` leftward in `L`. Every element crossed is incomparable with
it: a predecessor could not come after it in `L'`, and a successor could not
come before it in `L`. The adjacent swaps are therefore swaps of incomparable
elements. Delete the common first element and induct. This proves the claim
for every finite poset.

For a locally finite infinite complex, this theorem can be used on an actual
finite common causal support. It does not assert that two entire infinite
orders are connected by one finite swap sequence, and the cross-check does
not need such an assertion.

### 2.3 Weakest link: prefix compatibility was assumed in the bridge

The subject's decisive sentence is:

```text
An exhaustion compatible with a write order has its stages among those
prefixes.
```

That conditional is true by the meaning assigned to “compatible”; it does
not derive compatibility. `RED` constrains the order of writes already in a
circuit. It does not state that every cofinal increasing sequence of finite
subcomplexes is a sequence of prefixes of one total write order. `CIS` says
that a physical exhaustion adds new future incidences and does not rerun a
completed incidence, but it likewise does not define every stage as an order
ideal or supply a global enumeration whose prefixes are exactly the stages.

The logical gap can be exposed on the bare mathematical wording. In the
locally finite chain `0<1<2<...`, an increasing cofinal finite-set sequence
may begin `{1}`, then `{0,1}`, then `{0,1,2}`, and so on. Its first stage is
not a prefix of any linear extension. This is a countermodel to the bare
“cofinal increasing finite subsets” formulation unless “physical
subcomplex” is separately defined to be causally down-closed. The sealed
sources consulted here do not state that missing definition. The example is
not promoted as a physical exhaustion; it demonstrates that `RED` alone
does not prove the bridge.

### 2.4 The limit-passage carrier is also misbound

Cofinality does imply that every finite support is eventually contained in
both increasing exhaustions. The subject then says local finiteness makes
each *finite* down-set finite; finiteness was already stipulated. If the word
“finite” were removed, local finiteness would not repair the sentence: a
locally finite poset can have an infinite down-set.

More importantly, agreement of finite write circuits is a statement about
record transformations or states. `ARCH` lines 73–103 establish strong
convergence of `P_nBP_n` to `B` on `l2(V)`. No map in that theorem accepts a
record state as input. The missing passage must instead be supplied by exact
state-restriction compatibility and stabilization after the causal buffer.
Those are the objects carried by `GNS`, Parent-State Covariance, and the
packet-sealed Fork-8 promotion result—not by `ARCH`.

## 3. Independent `GNS` verification and its boundary

`GNS` fixes

```text
R_N = tensor_(j=1)^N M_3(C),
iota_NM(A) = A tensor I_(M-N),
W_M = V_(M,N)(W_N tensor I_new),
```

with `V_(M,N)` acting identically on the first `N` completed record factors.
Therefore it commutes with `I_source tensor iota_NM(A)`. Direct substitution
into the displayed state gives, for the full matrix algebra and every finite
`M>N`,

```text
omega_M(iota_NM(A)) = omega_N(A).
```

The algebraic inductive-limit state and its norm-continuous quasi-local
extension follow. This argument is exact and does not depend on the
three-cell numerical regression. The `GNS` compatibility theorem is therefore
independently verified.

Its stated index category is the canonical count chain `N<M`. It does not
name an arbitrary finite causal subcomplex `K`, a second exhaustion, or a map
identifying each exhaustion's stages with the first `N` tensor factors.
Accordingly, the subject's phrase “exhaustion-compatibility ... independently
of §1.2–1.5” is too strong. `GNS` proves compatibility once the finite record
system and its canonical embeddings are supplied; it does not independently
prove the missing prefix/exhaustion identification.

## 4. Exact surviving `E4b` statement

The packet-sealed Fork-8 promotion result, lines 36–49, supplies the lawful
route without the failed prefix lemma:

1. every completed-record observable has finite cell support;
2. after its causal buffer, later primitive incidences act identically on its
   completed record factors;
3. the output state and dressed map stabilize exactly; and
4. two cofinal physical exhaustions eventually contain that same finite
   causal support.

Thus the statement surviving cross-check is:

```text
Within the promoted ordinary 3+1 flat-asymptotic branch, for physical
exhaustions governed by the same finite source-record parent which add future
primitive cells without subdividing an already primitive cell, the
restriction of every stabilized completed-record state to a finite causal
support is identical after that support and its causal buffer occur in both
exhaustions.
```

This is response equivalence of the outgoing record net. It is not the
subject's stronger combinatorial assertion that arbitrary cofinal finite-
subcomplex exhaustions differ only by adjacent spacelike swaps. The latter
is neither needed nor proved.

## 5. Verdict ledger

| claim | disposition | exact reason |
|---|---|---|
| `E4a`: exhaustion-independent dynamics | **CONFIRMED** | fixed global bounded `B`, strong compression convergence for every admitted exhaustion, common exhaustion-free limit |
| finite linear-extension connectivity | **CONFIRMED** | constructive induction for all finite posets |
| every physical exhaustion is a prefix/down-set chain by `RED` | **REFUTED AS A DERIVATION** | `RED` orders writes; it does not type exhaustion stages as prefixes |
| `ARCH` transports finite record-state equality to the limit | **REFUTED AS A BINDING** | its receiving object is the compressed incidence generator, not record states |
| `GNS` exact compatibility | **CONFIRMED IN ITS STATED CATEGORY** | full `R_N`, every finite `M>N`, canonical embeddings |
| `GNS` alone compares arbitrary cofinal causal exhaustions | **SCOPE-NARROWED** | the causal-subcomplex-to-canonical-chain identification is absent |
| `E4b` completed-record exhaustion invariance | **SCOPE-NARROWED, THEN CONFIRMED IN THE DISPLAYED PROMOTED-BRANCH FORM** | earned by finite support, causal-buffer stabilization, and cofinal containment in the sealed promotion result |

## 6. `FREEDOMS_CONSUMED`

| possible freedom | treatment |
|---|---|
| causal complex `V` | carried as the common fixed complex quantified by `E4`; none selected |
| exhaustion `{V_n}` or `{W_m}` | universally quantified inside the displayed scope; neither selected |
| global incidence generator `B` | used exactly as packet-sealed; no weight or boundary term added |
| write order / linear extension | no order selected; the finite theorem quantifies over both orders |
| physical-exhaustion definition | not supplemented; the missing prefix rule is reported rather than invented |
| parent, state, embeddings, and causal buffer | used only at their packet-sealed scope |
| channel decomposition | not selected |
| smooth field, EM interpretation, coupling, member, or physical number | not supplied or evaluated |

`FREEDOMS_CONSUMED = none selected; fixed sealed objects and universal
parameters only.`

## 7. `FLATTENING_CHECK`

The cross-check keeps separate:

- a bounded-operator dynamics theorem (`E4a`);
- a finite-poset connectivity theorem;
- a canonical-chain record-state compatibility theorem (`GNS`);
- the promoted physical-exhaustion response-equivalence theorem; and
- the still-open infinite-future dressed-map/Møller issue (`E4c`).

No hypothesis is renamed as a derived theorem, no finite regression is used
as an all-stage proof, no arbitrary exhaustion is flattened into a linear
extension, and no record-state limit is flattened into an incidence-operator
limit. The ordinary-branch and same-parent qualifiers remain visible.

`FLATTENING_CHECK = clean.`

## 8. Jurisdiction and self audit

This relay performed a read-only adversarial proof comparison and authored
only this report and its seal. It did not modify either subject or any packet
source; did not invoke a chain; did not register, plan, track, or use git; and
did not change a board, seal status, or authorization state.

The finite chain displayed in §2.3 is a structural countermodel to an
unstated implication. It is not a selected physical exhaustion or a physical
quantity evaluation. Dario's reported random-poset and finite numerical
checks were read as disclosures and carry no weight in this proof.

E4A = CONFIRMED
E4B = NARROWED (promoted-branch stabilized completed-record restrictions agree after common finite causal support and buffer; arbitrary cofinal finite-subcomplex swap-equivalence not proved)
GNS_SUPPORT = independently verified (canonical inductive chain; not alone an arbitrary-exhaustion bridge)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
