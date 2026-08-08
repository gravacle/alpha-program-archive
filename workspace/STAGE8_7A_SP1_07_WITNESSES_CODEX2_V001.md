# Stage 8 / 7A Step 11 — SP1-07 Witness Computation — Codex 2 v001

Date: 2026-08-08  
Lane: CODEX 2  
Scope: the seven named SP1-07 formalization gaps, in grammar order

## 0. Preflight and pinned baseline

The relay input
`relay_inbox/RELAY_PASTE_736_SP1_07_WITNESSES_CODEX2_V001.md` rehashed to
`0e545bb0c34b2d8de12a8f1cc8d29fc052c040aaa3a2bac38447e0acc4586108`;
its sidecar and CODEX 2 lane guard matched. `relay_outbox/736_ACK.md` was
written before task work. The requested report name was absent from the
cleanroom and archive workspace.

| ID | Sealed/content-addressed input | SHA-256 |
|---|---|---|
| `GLOBAL` | packet `BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md` | `949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd` |
| `SPEC` | `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V012.md` | `382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504` |
| `FORMAL-REPORT` | `STAGE8_7A_SP1_07_FORMAL_CODEX2_V001.md` | `f1dc27ad972a5e0429e778c8f62b9dad4b7463fdfde9459d79a6029f84d73a0f` |
| `P-BEFORE` | prior `generated/P_SP1_07.json` | `eee07455d902dd9390ddff6594b1728419096a3a23298dcc39f21cfef3b95f73` |
| `E` | prior `generated/E_SP1_07.json` | `3925d5333a7c5e53c65a307630c9150a0e218d352dafd1f944abe090e3d24fc3` |
| `COMPILE-BEFORE` | prior `generated/compile_result.json` | `288777edbebbf6b6ccec7d5116e40b106a12cff2ebe109d7c2bac8450afcefa9` |
| `FORMAL-INVENTORY` | prior `inventory.generated.json` | `314077a1f1d63d02263d02c88f29c475b14b95efd6ed1869594cd1bb3a3eb8b2` |

All seven pins reverified before construction. The witness records cite only
exact spans inside four rehashed `GLOBAL` blocks:

| Block | Byte span | SHA-256 |
|---|---:|---|
| `B_GLOBAL_TYPED` | `[1103,1704)` | `daeb7bc7b448e78009703e6fc7a7946a76844f7ee6f479327e63ab6ab84057d2` |
| `B_GLOBAL_DESCENT` | `[1705,4005)` | `fcbb16c6cad76b08a210d55d42a1ce82d165ae3a0adfd63f28ba16f30946d1ce` |
| `B_GLOBAL_CAR` | `[4006,5026)` | `f08456525bf3f5abb163b32bc3e7c9d1f084c79adb1d1ede879df10cc6cad76b` |
| `B_GLOBAL_ORDER` | `[5027,6406)` | `17314d1ffd972873a65ee99e3309610b70e25dfddf612dd7adb2a83df456d7ed` |

## 1. Decision rule

A witness is `COMPUTED` when the sealed finite carrier/type equations determine
a universal exact normal form. Universally quantified finite objects do not
require a favored member: a finite proof over all consistently labeled
one-complexes, all order pairs, or all vertex bijections is a closed witness.

A witness is `UNDERDETERMINED` when replay still consumes an object that the
sealed carrier merely names and does not type by bytes. Such an element is not
chosen from an unsealed example or inferred from dimension.

The closed witness schema hashes to
`4686c90954b82f9c026aeb76b13f8468bcac0638773c72557edbc48c4011022f`.
Every record binds its prior proof, exact expected conclusion, source spans,
disposition, and either a replay computation or one free element.

## 2. Seven witnesses in grammar order

| Ordinal / ID | Disposition | Record SHA-256 | Exact result or free element |
|---|---|---|---|
| 1 — `D02_THREE_CELL_LEFT_PARENTHESIZATION` | `COMPUTED` | `8ea778d12189ef29b0f4ec7ddd0ebbbad9e9fa2ef9b212e9a11d64e8d60acc73` | left pushout normalizes to the quotient of `V1 disjoint-union V2 disjoint-union V3` by the same generated shared-label incidence relation |
| 2 — `D03_THREE_CELL_RIGHT_PARENTHESIZATION` | `COMPUTED` | `aa5f9d7d9e99b04e75192053989add5df833b781db7c37f348c4b195f98cd33c` | right pushout normalizes to the identical quotient and label-union cell set |
| 3 — `D04_CELL_ORDER_INDEPENDENCE` | `COMPUTED` | `6dc97b0b63d0a7873d0143913cfef0d9187ec6e4ce04864abb8e0b9f08899095` | both total orders reindex by their unique finite cell-ID permutation to `SUM_BY_CELL_ID F_c` |
| 4 — `D06_GRADED_RECORD_FACTOR_COMMUTATION` | `COMPUTED` | `206e847eb758820648b2f50b2802571baf3aaf87a59fb33f3172fd238452a5ab` | disjoint tensor-slot products have the same normal form and even-even graded sign `1`, so the graded commutator is zero |
| 5 — `D07_VERTEX_RELABELING_COVARIANCE` | `COMPUTED` | `e3cd95a29b1e2bc450b4524aff5fe66f00beed6b073cd3a9c8bf60aee48e178a` | `d_sigma(c)=P_sigma d_c`, hence projectors and the finite `h_K` sum transform by conjugation |
| 6 — `D08_ORIENTATION_REVERSAL_COVARIANCE` | `UNDERDETERMINED` | `a702c80fe74572bd7e517b9e680eef13e3db37fabfaa482d084847260b92c54e` | free element: the cellular orientation unitary on each selected record factor |
| 7 — `D09_FINITE_STONE_ORDERING` | `COMPUTED` | `54aca2328a5d2497f89ef1079fb627894e3432db1bdae92f4f0d492afa77a006` | finite symbolic self-adjoint exponential calculus gives unitarity, composition, and uniqueness for the sealed generator |

### 2.1 Both three-cell parenthesizations

For any three finite consistently labeled oriented one-complexes, the left
term

`PUSHOUT(PUSHOUT(C1,C2),C3)`

and the right term

`PUSHOUT(C1,PUSHOUT(C2,C3))`

expand to the same canonical data:

```text
vertices = QUOTIENT(DISJOINT_UNION(V1,V2,V3),
                    EQ_CLOSURE(shared_label_incidence))
cells    = LABEL_UNION(C1.cells,C2.cells,C3.cells)
h_K      = SUM_BY_CELL_LABEL(P_c tensor gamma5 tensor iota_c(c_c)).
```

The two proof records separately retain their ordered syntax, cocone
expansion, quotient normalization, finite operator assembly, and the exact
expected left/right conclusion. No concrete triple is selected because the
proof is universal over the source's sealed finite class.

### 2.2 Cell-order independence

Let `order_1` and `order_2` be total orders of the same finite cell-ID set.
The unique finite permutation `pi=order_2^-1 o order_1` is a term bijection.
Reindexing both sums produces the same `SUM_BY_CELL_ID F_c` normal form. This
computes the demanded two-order equality; it does not assume a preferred
enumeration.

### 2.3 Graded commutation

The sealed carrier gives distinct tensor factors and trivial record fermion
grading. For `c != d` and even `x,y`, both products normalize exactly to

`I_before tensor x_at_c tensor I_between tensor y_at_d tensor I_after`.

The graded sign is `(-1)^(degree_x*degree_y)=1`; exact subtraction yields
`[iota_c(x),iota_d(y)]_graded=0`. This is symbolic tensor normalization, not a
numerical approximation.

### 2.4 Vertex-relabeling square

For every finite vertex bijection `sigma`, its permutation map satisfies
`d_sigma(c)=P_sigma d_c`. Substitution in the rank-one projector definition
gives

`P_sigma(c)=P_sigma P_c P_sigma^-1`.

Conjugation distributes over the finite cell sum, yielding the exact expected
square

`h_relabel=(P_sigma tensor I) h_K (P_sigma^-1 tensor I)`.

No particular relabeling is chosen; the finite symbolic proof covers all of
them.

### 2.5 The one underdetermined witness

The source fixes `d_c -> -d_c` and therefore fixes projector invariance under
orientation reversal. It then says that the record quadrature is conjugated by
the “cellular orientation unitary,” but supplies no typed map, matrix, domain,
codomain, or exact relation bytes defining that unitary.

The free element is therefore:

```text
U_c : R_c -> R_c,
U_c^* U_c = U_c U_c^* = I,
U_c c_c U_c^* = c_reversed.
```

A content-addressed `U_c` record for every selected cell would close D08. A
root executable occurrence is not imported: it is not a packet-sealed member
or a content reference in the current formal manifest, and using it would
replace the missing carrier with unbound testimony.

### 2.6 Finite Stone replay

The sealed source types `H_K` as finite and self-adjoint and defines
`U_K(t)=exp(-itH_K)`. With formal real `s,t` only:

```text
-i(t+s)H_K = (-itH_K)+(-isH_K),
[ -itH_K, -isH_K ] = 0,
exp(-i(t+s)H_K) = exp(-itH_K) exp(-isH_K),
U_K(t)^* U_K(t) = I.
```

Finite spectral resolution then gives the unique one-parameter unitary group
with generator `H_K`. No time value, eigenvalue, physical interval, or other
physical quantity is numerically evaluated.

## 3. Incremental recompilation

The row was recompiled after each disposition. Each recompile is itself a
content-addressed canonical record.

| After | Disposition | KERNEL-ready census | Row status |
|---|---|---:|---|
| D02 left pushout | computed | `3/9` | `PARTIAL_FORMALIZATION_3_OF_9_KERNEL_READY` |
| D03 right pushout | computed | `4/9` | `PARTIAL_FORMALIZATION_4_OF_9_KERNEL_READY` |
| D04 order independence | computed | `5/9` | `PARTIAL_FORMALIZATION_5_OF_9_KERNEL_READY` |
| D06 graded commutation | computed | `6/9` | `PARTIAL_FORMALIZATION_6_OF_9_KERNEL_READY` |
| D07 relabeling | computed | `7/9` | `PARTIAL_FORMALIZATION_7_OF_9_KERNEL_READY` |
| D08 orientation | underdetermined | `7/9` | `PARTIAL_FORMALIZATION_7_OF_9_KERNEL_READY` |
| D09 Stone | computed | `8/9` | `PARTIAL_FORMALIZATION_8_OF_9_KERNEL_READY` |

The updated proof index hashes to
`c4a1e73e717aa0cfa45aa1f754f29113d1fd8572d4ef3f1cdd38689dabbd0639`.
It retains the prior D01/D05 proofs, replaces six partial entries with their
computed witness records, and retains D08 as partial.

Final opcode results:

| Receiver | Result |
|---|---|
| `r_schema`, `r_type`, `r_expected` | `PASS` |
| `r_enum` | `PASS_9_IDS` |
| `r_nonempty`, `r_required_ids`, `r_proof_ids` | `PASS` |
| repeatable `r_d/r_cmp_d` | `8 KERNEL_READY / 1 PRECONDITION_NOT_REPLAYABLE` |
| `r_exact` | `PASS` |

The row still does not PASS because D08 prevents the universal repeatable
KERNEL/COMPARE conjunction. Compile outcome is
`PARTIAL_CONFORMANCE_8_OF_9_KERNEL_READY`; row status is
`PARTIAL_FORMALIZATION_8_OF_9_KERNEL_READY`.

## 4. Static battery and limits

The builder ran directly with `python3 -I -S -B`; AST parsing passed. The
21-member inventory replayed every byte length and SHA-256 and itself hashes
to `1af6e9dcc239c4bf3c74f5de8cfb219458a49d6331ca49f0daf536a586650426`.
The final compile record hashes to
`1d9d9a9774433d59a8c2741cabe9b70d20a8039ece7ba03c8f339e9c4f43e055`.
The self-check record hashes to
`bb042d9cc6f5e5a9bd0a96e8d5d59a694a5fffec2d390b5f81ab3f1a65d40d82`.

Four negatives bit: computed-without-source, underdetermined-without-free-
element, wrong computed normal form, and an uncited computation step. A second
launch over occupied outputs refused `OUTPUT_COLLISION:package outputs`.

`F_PLDEC`: CLEAN. Every computation is finite symbolic set, tensor, projector,
permutation, or exponential algebra. No numeric physical evaluation, measured
constant, member, target, fixed point, or end test occurs. M-2 checked exact,
whitespace-normalized, scope/self-reference, and hyphen/space/underscore
surfaces for all seven obligation names and the orientation-unitary near miss.

Admission remains `BARRED_STEP11_SUBGATE`. `proof_authorized=false`,
`alpha_computed=false`, and `kappa_record_computed=false`. No descriptor,
board, seal, evaluator package, or chain state changes.

Verb audit under the verdict-line scope rule: CLEAN. “Computed” means an exact
universal finite normal-form record ending at the prior expected conclusion.
“Underdetermined” names one unbound carrier; it is not criterion FAIL.
“KERNEL-ready” is the bounded formal input status, not proof authorization or
row admission.

WITNESSES = 6 computed / 1 underdetermined (D08: cellular orientation unitary `U_c` not fixed)
KERNEL_READY = 8/9
ROW = PARTIAL_FORMALIZATION_8_OF_9_KERNEL_READY
ADMISSION = barred, stated
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
