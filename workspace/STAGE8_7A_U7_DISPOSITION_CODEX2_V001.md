# Stage 8 / 7A Step 11 — Seven-U Disposition — Codex 2 v001

Date: 2026-08-08  
Lane: CODEX 2  
Scope: source-locus disposition, principal decision brief, and cross-contract
receiver routing only

## 0. Custody, pins, and method

The relay input
`relay_inbox/RELAY_PASTE_732_U7_DISPOSITION_CODEX2_V001.md` rehashed to
`94f8693c438e9ff8ffd283d9ef1a456ca642c24f8bfef0fd7de2927d6a9ed207`;
its seal matched and the lane guard named CODEX 2. `relay_outbox/732_ACK.md`
was written before this work. The requested output name was absent from both
the cleanroom and archive workspace.

Load-bearing whole-file pins reverified before reading:

| ID | Sealed source | SHA-256 |
|---|---|---|
| `SPLIT` | `STAGE8_7A_CONSTRUCTIBLE_SPLIT_CODEX2_V001.md` | `1417390cab756a05c8f1940c78afbe198863c7e7c8b87ed35f7d36924be6a0cf` |
| `MAP` | `STAGE8_TASK6_ENVELOPE_FORMALIZATION_MAP_LANE2_V001.md` | `e85a6113e5b45624d19f987ae2603f63ac418df10f33669cc6a44742e5918ed5` |
| `SPEC` | `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V012.md` | `382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504` |
| `LEDGER` | `BID_FULL_STACK_REVIEW_LEDGER_V003.md` | `c09f2c246c48ddfd0df127da26a22f08ba9ffd44f5c2118c178a0a5eba5d00e8` |
| `PACKET-MANIFEST` | `review_packets/STAGE7_QSPEC_CANDIDATE_V001/STAGE7_PACKET_MANIFEST_V001.sha256` | `9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311` |
| `V011` | packet `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` | `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` |
| `GLOBAL` | packet `BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md` | `949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd` |
| `CPT` | packet `BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md` | `0322763ac48a4428b432124a6947da81826a41f612efa6803ee9a87317929b98` |
| `SOURCE-GATE` | `BID_SOURCE_PARENT_CLOSURE_GATE_V003.md` | `5c679e3741abe782688b8a75ffa1928c308775248e41af192d03976f01cb4dbf` |
| `RELOCATION` | `STAGE8_TASK6_GROUNDING_RELOCATION_DARIO_V001.md` | `69334875b94679c16da9b8d6153242241ca3c202f0facc6130596b9807189e6f` |
| `CV2` | `STAGE8_TASK6_CONTRACT_V002_DISPOSITIONS_CODEX2_V001.md` | `c0af7131f0adc522ef14f7848ab38458df5af5a7a60dbe36131d1567351009c5` |
| `CHECK-MAP` | `evaluator_build_A/checks/check_map.json` | `280004821c532def203ae81cec35bcac26bd3ab4bdd03752f5196aa7b9c23f3d` |

The search covered the 113-row packet manifest (51 Markdown members), the
current sealed spec and generated check map, the current source-parent gate and
blocker ledger, and the sealed Q-595/Q-626 search record. That record covers the
120-member D1 evidence space and its 2,972-file delta probe. Each object name
was checked in four false-negative modes: exact spelling; whitespace-normalized;
scope/self-reference; and hyphen/space/underscore variants. Requirement-only,
status-only, machine-copy, relay, and report occurrences were not treated as
proof or carrier bytes. `SPLIT[4252,6220)` block
`138581d54aec12e40e8f4370cfef6bee1a042b57cce564051ea0ff9990e5c17d`
records the searched spaces and probe families.

### 0.1 Block-coverage index

Every positive source disposition below is covered by a half-open byte block
from a packet member. Near-miss and contract blocks are included so that an
absence or route does not rest on narrative recollection.

| Block | Whole source | Byte span | Block SHA-256 | Use |
|---|---|---:|---|---|
| `B-GLOBAL-DESCENT` | `GLOBAL` | `[1705,4005)` | `fcbb16c6cad76b08a210d55d42a1ce82d165ae3a0adfd63f28ba16f30946d1ce` | finite pushout, `h_K`, overlap, associativity, relabeling, orientation |
| `B-GLOBAL-CAR` | `GLOBAL` | `[4006,5026)` | `f08456525bf3f5abb163b32bc3e7c9d1f084c79adb1d1ede879df10cc6cad76b` | operator-valued CAR lift, one-source restriction, quartic control |
| `B-GLOBAL-ORDER` | `GLOBAL` | `[5027,6406)` | `17314d1ffd972873a65ee99e3309610b70e25dfddf612dd7adb2a83df456d7ed` | Stone ordering and executable obligations |
| `B-CPT-NEAR-MISS` | `CPT` | `[4185,6119)` | `9cca1b78bc39d69d0a2756e85ee54e3760ed8057136365da95fa10f219439cb9` | cellular quadrature/CPT result; not the SP1-02 boundary Riesz-map proof |
| `B-V011-OPEN` | `V011` | `[7823,9984)` | `326c1bc46fa1c961eff71d486b5f9a60a3285653bf61afb74b17b5166645c2d7` | universal `K_open`, `E_open`, `iota_open`, no basis/normalization |
| `B-V011-STAR` | `V011` | `[12070,14031)` | `dd70c14a7670e5f71048aa38bb4885be95a0e0c998746863f768f82ebee62e4e` | minimal rooted-star premise and object/fiber/transport types |
| `B-V011-CATEGORIES` | `V011` | `[15668,17074)` | `9bec60c9c716a85fe457fecea2ff7035b0f95e0209323028e90eb94be92b6649` | `OpenRec_2`/`DecRec_2`, first-opening and labels |
| `B-RELOCATION` | `RELOCATION` | `[5426,7165)` | `cb060d3fd1f82838ba30256be41ffc7771d9055af87ab12f3c536a3113741518` | why the universal open-object schema is not an instance |
| `B-BINDING-LAW` | `SPEC` | `[28527,29513)` | `d13bf740cf2405e64c140916c7a1abb2ea1ec6984580c5b6b475813e7ba8f4ae` | every compact opcode and PASS atom needs a named receiver |
| `B-V010-14` | `SPEC` | `[59021,59449)` | `2713fa74adfb322ba66ee0725d685015db7a6b3847e77631ed2f373a280bb292` | compact descriptor with bare `DAG` and `EXACT` |
| `B-MAP-V010-14` | `CHECK-MAP` | `[52747,53737)` | `641fc2dbddf19ab3f27d36bea916e9d253e0186f467f7bc858d2fade5dab0cb1` | generated contract contains only `M2/r_m2` |
| `B-CV2-05B` | `CV2` | `[9947,11851)` | `af836f60251dbe045f9da8c5db74717607cc4445cfe6c27e3870bbdb7dfcebd0` | general assignment-coverage carrier remains deferred to Step 11 |

## 1. QQ1 — five source-locus dispositions

The U atom in each row is treated separately from the C and D atoms already
assigned by Q-626. Finding source prose does not itself create a KERNEL proof:
where replayable proof objects are still needed, the source question resolves
to D with `S11-FORMAL` ownership. A displayed TYPE/EXACT carrier that can be
serialized without new mathematical judgment resolves to C.

### 1.1 Closed disposition table

| Row | Object names probed and typed spaces | Byte result | Disposition and owner |
|---|---|---|---|
| `C-B-V011-SP1-02` | `G_map`, `p_map`, `G_Lor`, `p_Lor`, `p_selected_map`, `E_map`, `INTERTWINER_IDENTITY`; charged boundary fiber `E_q=S tensor L^q`, positive hypersurface space `(E_q,h_n)`, chiral-odd map, and Lorentz generators | **UNRESOLVED.** `B-CPT-NEAR-MISS` derives the cellular `c_partial` phase and its CPT relations, not the selected chiral-odd boundary Riesz map demanded by SP1-02. `PACKET-MANIFEST` has zero member-name hits for `BID_LORENTZ_COVARIANT_SOURCE_BOUNDARY_MAP_DERIVATION_V001.md`; `SOURCE-GATE[1233,1510)` (`c49cc7b5f7612dba4ad6b49ee9a6493624d1a0fcc6477e9885aa3ab80a9a9161`) closes only bare-incidence Lorentz covariance and expressly leaves parent zero-forms elsewhere. | Remains `U-SOURCE`. Exact missing locus: a packet-sealed, content-addressed derivation of the selected boundary map from the declared boundary data, plus complete candidate-map and Lorentz-generator indices, conclusion ledger, and every Lorentz-square identity required by `SPEC[68195,69207)`. |
| `C-B-V011-SP1-06` | `j`, `Q_Sigma`, `P_ch`, `G_jQP`, `p_cons`, `p_charge`, `p_proj`; conserved-current domain, CAR finite-particle charge space, and the spectral domain of `1_(R\\{0})(Q_Sigma)` | **UNRESOLVED.** `SOURCE-GATE[2957,3322)` (`c5342dc7a24a11b751717567067201cc404c53e120dfb0f4a6e65a185a4bb677`) states a PASS summary for the standard Dirac/CAR chain but supplies no replayable proof objects. No packet-manifest member carries the exact current-to-charge derivation filename or the three named proof bundles. | Remains `U-SOURCE`. Exact missing locus: packet-sealed bytes for `p_cons`, `p_charge` proving `Q_Sigma=integral_Sigma star(j)` with slice independence, and `p_proj` proving `P_ch=1_(R\\{0})(Q_Sigma)`, all typed by `G_jQP` and bound to the declared spectral domain required by `SPEC[71591,72425)`. |
| `C-B-V011-SP1-07` | `S_SP1_07`, `M_SP1_07`, `G_SP1_07`, `G_overlap_order`, `p_complete`, `E_SP1_07`, `P_SP1_07`; `K_Sigma=K_orb tensor S_Dirac`, separate even `R_c`, `R(K)`, `A_SR(K)`, `P_c`, `h_K`, `H_K`, and finite Stone `U_K(t)` | **RESOLVED.** `B-GLOBAL-DESCENT` gives the one-global-source/separate-record construction, cell pushout, both associativity orders, primitive overlap, relabeling, and orientation covariance. `B-GLOBAL-ORDER` gives the finite Stone law and enumerates the executable obligations. These are the authoritative source blocks for every mandatory SP1-07 derivation class. | Reclassify this U atom to **D**, owner **`S11-FORMAL`**: formalize the displayed derivations into the finite grammar/certificate, proof index, and replayable proof objects. No new physics statement is needed, but the prose is not itself a KERNEL proof. |
| `C-B-V011-SP2-05` | `S_global`, `M_global`, `G_global`, `G_pushout`, `p_pushout_complete`, `G_orientation`, `p_orientation_complete`, `p_pushout_relabel_orientation`, `S_premise`, `premise_record`, `p_quartic_reject`; the same global source/record spaces, `h_K`, `h_K^2`, SP17 one-cell restriction, and low/high CAR sectors | **RESOLVED.** `GLOBAL[334,6406)` (block SHA `abef6d52ec372c48a407fcf5a87e8d5a9b41064f5255f9bdac8cbe697726d07b`) contains the adopted quasi-free premise, global graph, pushouts, orientation/relabeling covariance, one-cell restriction, primitive overlap versus induced two-step propagation, the operator-valued lift, and the quartic low/high-sector control. | Reclassify this U atom to **D**, owner **`S11-FORMAL`**: produce the two finite completeness certificates and replayable covariance/quartic proof bundles from the cited blocks, preserving the premise hash in `used_axiom_hashes`. |
| `C-D-A35-02-QUASIFREE-CAR-LIFT` | `h_K=sum |e_i><e_j| tensor b_ij,K`, `H_K=sum a_i^*a_j tensor b_ij,K`, CAR/even-record carriers, covariance maps, vacuum/one-source/two-source sectors, and `H_lambda` quartic control | **RESOLVED.** `B-GLOBAL-CAR` displays the operator-valued lift, exact one-source recovery, covariance-compatible typed carrier, vacuum normalization, and a quartic competitor that agrees below and differs in the two-source sector; `B-GLOBAL-DESCENT` supplies the covariance maps. | Reclassify this U atom to **C:CS**, owner **`compile_schema_instance`**: canonicalize the already displayed finite TYPE/EXACT carrier and controls. The row has no KERNEL receiver and requires no newly authored derivation statement. |

### 1.2 Source-locus result and census effect

Three of five source questions resolve: SP1-07 and SP2-05 become D under
`S11-FORMAL`; D-A35-02 becomes C under `compile_schema_instance`. SP1-02 and
SP1-06 remain U with exact missing proof loci. Applied to Q-630's corrected
atom census, this bounded disposition changes

```text
C199 / D35 / U7 / PROGRAM-FUTURE19
to
C200 / D37 / U4 / PROGRAM-FUTURE19.
```

The remaining U4 are the two missing sources, the principal item in §2, and
the routed contract item in §3. This is a planning classification only; no
carrier, proof, envelope, admission, board verdict, or chain result is created.

## 2. QQ2 — neutral principal decision brief

### 2.1 Item requiring a ruling

`C-B-V009-01` needs one content-addressed **instance**, not another universal
definition: a concrete representative of the V011 minimal first-opening rooted
star, its four actual one-dimensional Hermitian object-fiber carriers, its
three first-opening edges/transports, `E_open`, and the canonical summand
inclusion `iota_open`. The separately absent `M2` corpus for abstract-line
aliases remains an `S11-SPEC` item and is not decided by selecting the instance.

The graph's isomorphism shape is not open. `B-V011-STAR` fixes the minimal
first-opening complex to the rooted three-star with one unresolved root and
three public endpoints. `B-V011-OPEN` defines `E_open` and `iota_open` but is
universally quantified and forbids an unearned basis or metric normalization;
`B-RELOCATION` proves why that schema alone is not a TYPE-consumable instance.
The principal must select a representative and fiber realization within those
sealed constraints.

### 2.2 Lawful candidate forms

The candidates are stated without preference.

| Candidate | Sealed grounds | Selected object | Downstream commitments |
|---|---|---|---|
| `P-A — basis-free formal-line instance` | `B-V011-STAR`; `B-V011-OPEN`; `B-V011-CATEGORIES`; SOURCE-GATE SP05 block `[2601,2957)` / `d3d2678a3aed33ac1c3697d979e95278d61f9867f9096f05ff28260833696d5a` | Vertex IDs `{r,p_M,p_Q,p_G}`; first-opening edge IDs `{e_M,e_Q,e_G}` with `e_h:r->p_h` and label `h`; four **distinct named abstract Hermitian line objects** `{L_r,L_pM,L_pQ,L_pG}`; three explicitly named unitary transports; basis-free direct sum and summand injection. | The instance schema must preserve distinct object IDs even when dimensions agree; no identification with four copies of a common scalar carrier, no chosen basis, and no claim that `iota_open` is an isometry before Gate 3. Every later TYPE payload and alias corpus must use these IDs and transports. |
| `P-B — Gate-3-realized line-subobject instance` | The same star/category blocks; `B-V011-OPEN` states that only after Gate 3 derives the counting Hermitian forms may `iota_open` be called an isometry or a unit representative used. | The same labeled rooted star, with each `L_v` selected as a distinct content-addressed one-dimensional line subobject of the Gate-3-derived counting Hilbert carrier, carrying the induced Hermitian form and explicit unitary edge transports. | The instance must cite the Gate-3 form and the four line-subobject inclusions; it commits future payloads to those subobjects and their induced metrics. Any unit representatives or scalar trivializations must be separately licensed and entered in the alias corpus; they cannot be inferred from dimension one. |

Both candidates preserve the sealed minimal-star topology, handle labels, and
actual-fiber requirement. Neither permits an enlarged first-opening graph:
V011 classifies parallel paths, public intermediates, loops, and faces as
enlarged branches, while its first-opening premise fixes the ordinary minimal
object. Neither candidate selects a physical magnitude, coupling, target, or
member. The principal's ruling must name the candidate, pin the exact instance
bytes, and state whether any basis/trivialization is licensed. No recommendation
is made here.

## 3. QQ3 — cross-contract receiver question

### 3.1 Facts determined by sealed bytes

The contracts determine the defect but not the repair owner:

1. `B-BINDING-LAW` requires a one-to-one expansion of each backticked opcode
   into ordered result objects and requires every PASS atom to be a field of a
   named result.
2. `B-V010-14` names `DAG`, `r_m2:=M2(...)`, and `EXACT` Hessian/mutation work,
   but names a receiver only for `M2`.
3. `B-MAP-V010-14` confirms the generated `program_contract` is exactly
   `[{opcode:M2,repeatable:false,result_name:r_m2}]`; no DAG or EXACT assignment
   exists.
4. `B-CV2-05B` leaves the general producer-carried/R9-resolved/missing
   assignment carrier to the Step-11 Builder-B contract/replay subgate before
   any additional envelope is admitted.

Thus the current row cannot lawfully receive a V010-14 envelope. The sealed
bytes do not select one of the following two whole repairs.

### 3.2 Reading A — descriptor-owned explicit receivers

The specification owner amends the V010-14 row so that the claim/provenance
graph has a named `DAG` result, the Hessian relation has a named `EXACT` result,
and each factor-two/factor-four/later-coefficient mutation is assigned either a
declared repeatable EXACT receiver or separately named results. The PASS cell
then consumes those result fields explicitly. This reading changes the
descriptor row hash and spec pin; Builder A regenerates the check map, and
Builder B's coverage-direction field reports every assignment.

### 3.3 Reading B — sealed generated-expansion contract

The descriptor bytes remain compact, but a new sealed expansion rule makes
their one-to-one receiver expansion authoritative. Builder A's generated check
map then carries stable DAG and EXACT result names/repeatability in addition to
`r_m2`; the expansion rule must determine mutation multiplicity rather than
guess it. Builder B's CV2-05b carrier records each assignment as
producer-carried, independently R9-resolved, or missing and refuses incomplete
coverage. This reading preserves the descriptor row only by adding a closed
cross-builder contract that the current bytes do not contain.

### 3.4 Route

**ROUTED, not adjudicated.** Owner: `S11-SPEC` together with the Builder-A /
Builder-B contract-and-replay subgate, before the first V010-14 envelope. The
principal/spec authority must choose Reading A or Reading B; the chosen state
change must ship whole with schema, check-map, verifier reporting, fixtures,
roots, instances, and boundary re-pins. Synthesizing `r_auto_*` names in an
envelope relay would be an authored contract and is barred.

## 4. Battery, jurisdiction, and does-not-do

`F_PLDEC`: CLEAN. The dispositions use only sealed structural bytes and
contract custody. They do not use a target constant, measured quantity, desired
physical answer, member output, fixed point, or end test.

The outcome space remains failure-capable: unresolved source means source
absent, not false; routed receiver means contract ownership undecided, not a
criterion FAIL. A later proof may still pass or fail its existing criterion.
No criterion, kill condition, opcode set, aggregate rule, board row, road row,
or seal state is altered.

PIN CHECK: every whole-file digest in §0 and every block digest in §0.1 was
recomputed from bytes. The two exact packet-manifest name probes absent from
the packet (`BID_LORENTZ_COVARIANT_SOURCE_BOUNDARY_MAP_DERIVATION_V001.md` and
`BID_GLOBAL_CAR_CHARGE_AND_ACTIVATION_DERIVATION_V001.md`) returned zero;
the positive `GLOBAL` and `CPT` member probes each returned one. No unsealed
root copy is cited as authority.

Verb audit under the verdict-line scope rule: CLEAN. “Resolved” means the
authoritative source block has been located, not that its proof object exists
or passes. “Reclassify” changes the Q-626 planning atom only. “Candidate” is a
neutral decision form. “Routed” records missing contract authority. No proof,
authorization, evaluation, admission, physical, board, or chain verdict is
claimed.

SOURCE_LOCUS = 3 resolved / 2 unresolved (SP1-07 -> D:S11-FORMAL; SP2-05 -> D:S11-FORMAL; D-A35-02 -> C:CS/compile_schema_instance; SP1-02 and SP1-06 remain U-SOURCE with exact missing loci)
PRINCIPAL_ITEM = decision brief displayed (C-B-V009-01 instance; P-A/P-B; no recommendation)
RECEIVER = routed (descriptor-owned explicit receivers / sealed generated-expansion contract readings displayed)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
