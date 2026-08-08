# Stage 8 / 7A Step 11 — Cellular Orientation Unitary — Codex 2 v001

Date: 2026-08-08  
Lane: CODEX 2  
Scope: one source-determined typed carrier, consumed by `C-B-V011-SP1-07` and `C-B-V011-SP2-05`

## 0. Preflight and sealed sources

The relay input
`relay_inbox/RELAY_PASTE_743_ORIENTATION_UNITARY_CODEX2_V001.md`
rehashed to
`fb3b5da738e9bde3af73c20bd3c22a56105bc62a528825ee4a40596786cb7469`;
its sidecar and CODEX 2 lane guard matched. `relay_outbox/743_ACK.md` was
written before task work. The requested report and package names were absent
from both the cleanroom and archive workspace.

The derive-or-gap probe used only sealed packet copies:

| Source | SHA-256 | Meaning probed |
|---|---|---|
| `BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md` | `949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd` | global `R_c`, `d_c -> -d_c`, invariant `P_c`, `c_c`, `h_K`, full covariance statement |
| `BID_GRADED_BOUNDARY_SUPERCONNECTION_REPAIR_V001.md` | `2215f79cbe69f1de1643427ad5d422b0c3064ff758327e43ff1629de8633f72d` | cellular basis, grading, boundary dilation, oddness, selected quadrature |
| `BID_COMPLETE_ONE_NORMAL_ZERO_FORM_ENUMERATION_V001.md` | `50b5a651df2aca90ee47c6f85b2a502461370a652706ebccad871f191565a2d9` | ordered three-dimensional carrier and explicit `Gamma_cell=diag(+1,+1,-1)` |
| `BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md` | `0322763ac48a4428b432124a6947da81826a41f612efa6803ee9a87317929b98` | the `+i/-i` quadrature pair is related by primitive incidence-orientation reversal |
| `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V012.md` | `382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504` | two consumer contracts |

The carrier cites six exact content-addressed spans. Their span hashes are
`daeb7bc7b448e78009703e6fc7a7946a76844f7ee6f479327e63ab6ab84057d2`,
`fcbb16c6cad76b08a210d55d42a1ce82d165ae3a0adfd63f28ba16f30946d1ce`,
`10262d72110ffaafdcaf4ea0419af4f780b1616e30567a9275c0b1315207ef72`,
`191cf84d2288f532f7d4df410be2c8947ffa006c4bc440a697a4120a9e6f1fde`,
`42188aeee574da63e53aa88a0204f472d59b377c959eb2f6439602d692eb9a7c`,
and `c9fc62a999110e443f87551110e914462029f2dd5a5dd331d7ca202cd894b6c5`.

The prior SP1 witness inventory and SP2 formal inventory rehashed completely
before use. Their inventory digests remain
`1af6e9dcc239c4bf3c74f5de8cfb219458a49d6331ca49f0daf536a586650426`
and `78d7ddcb980804d7a6f7bce9e6b3dd34f6455543f475b7c6980b1bad62a2b828`.
No predecessor bytes were modified.

## 1. Derive-or-gap verdict: determined

The sealed structure already contains the needed unitary. No exchange,
Bogoliubov map, endpoint convention, or new free operator is required.

Use the packet-fixed ordered record basis

```text
(|r_c>, |p_c>, |e_c>)
```

for `R_c=span_C{|r_c>,|p_c>,|e_c>}`. The sealed cellular grading is

```text
Gamma_cell = diag(+1,+1,-1).
```

The incidence column and its self-adjoint dilation are, exactly,

```text
d_partial = [-1,+1]^T,

b_partial = [[ 0, 0,-1],
             [ 0, 0,+1],
             [-1,+1, 0]].
```

The packet proves `Gamma_cell b_partial + b_partial Gamma_cell = 0` and
selects `c_partial=i Gamma_cell b_partial`. Therefore

```text
c_partial = [[0,0,-i],
             [0,0,+i],
             [+i,-i,0]].
```

Orientation reversal sends `d_partial` to `-d_partial`. Linearity of the
sealed dilation gives `b_(rev c)=-b_c`, hence

```text
c_(rev c)=i Gamma_cell b_(rev c)=-c_c.
```

Now set the typed carrier to the already sealed grading:

```text
U_c := Gamma_cell : R_c -> R_c.
```

It is a self-adjoint unitary involution. Using `Gamma_cell^2=I` and the
sealed oddness identity,

```text
U_c c_c U_c^*
 = Gamma_cell (i Gamma_cell b_c) Gamma_cell
 = i b_c Gamma_cell
 = -i Gamma_cell b_c
 = -c_c
 = c_(rev c).
```

Thus the formerly named-only carrier is determined by sealed structure.
Multiplication of `U_c` by a central phase does not change its conjugation
action; `Gamma_cell` is the packet-fixed canonical representative, so no
phase choice enters either consumer.

## 2. Complete `h_K` commuting square

For any finite selected subset `O` of reversed cells, define the record-space
unitary

```text
U_O = tensor_(c in K) (Gamma_cell if c in O else I_(R_c)).
```

The factors are self-adjoint unitary involutions and act on distinct record
factors. For each reversed cell, the source incidence changes sign but its
rank-one support projector satisfies `P_c(-d_c)=P_c(d_c)`, while the record
quadrature obeys the proven local conjugation equation. Terms for unreversed
cells commute with the other-factor unitaries. Applying these two cases to
the packet-fixed finite sum gives, term by term,

```text
h_(rev_O K) = U_O h_K U_O^*.
```

This proves the full source-record orientation-covariance square, including
simultaneous reversal of any finite selected cell subset. It is an exact
structural identity; no physical quantity is evaluated.

## 3. Content-addressed carrier and proof

The new package is `step11_orientation_unitary/`. Its canonical JSON uses
sorted keys, tight separators, UTF-8, integer-pair complex entries, and no
trailing newline.

| Object | SHA-256 | Result |
|---|---|---|
| closed carrier schema | `2f22dccd1836bc858f5c03eb6218f9995987cd5086c7f64b433536dbde38bb1c` | exact basis, matrices, typed domain/codomain, subset extension, and six source bindings |
| `U_CELL_ORIENTATION_CANONICAL` | `7c19430b1346cf6aab1a217f634add352bfc8e55cf3e2f7d87fc2d1f2f9f841f` | `U_c=Gamma_cell=diag(+1,+1,-1)` |
| closed proof schema | `37c8e7d4683a24e53a1d8a162fed3f8db39cdb11086fa3549859c7d7ca85852c` | seven exact checks, no gaps |
| `P_ORIENTATION_UNITARY_AND_COMPLETE_HK_SQUARE` | `2a1e0926529903be4b8a2abfbbb69071193547ec43f3bf9e1c863ef31f001be9` | `KERNEL_READY` |
| SP1 D08 consumer binding | `beddf242073645f2457d500d2ab88cd63921e65e7e8a8da6e6798f7e60cb97e1` | exact prior expected conclusion reached |
| SP2 O02 consumer binding | `cbd939d1a5e8780456426d3964659790a85a5157df3f75b942e1291d3fa91174` | exact prior expected conclusion reached |

The proof record checks `U_c^*U_c=I`, self-adjoint involution, record
oddness, reversed boundary, local quadrature conjugation, projector
invariance, and the complete finite-`h_K` square. Its `gaps` array is empty.

## 4. Both consumer recompiles

### 4.1 SP1-07 D08

The prior nine-entry index at
`c4a1e73e717aa0cfa45aa1f754f29113d1fd8572d4ef3f1cdd38689dabbd0639`
had eight `KERNEL_READY` entries and the single D08 partial. The successor
index replaces only that D08 reference with the shared carrier proof; the
other eight entries are byte-preserved references.

| SP1 artifact | SHA-256 | Result |
|---|---|---|
| successor proof index | `89bf844bc03891bb16b51495b34ec72c655793919771da72a675ff0df057f14c` | 9/9 `KERNEL_READY` |
| compile result | `e8da29f387264515b9c9c4bc23c74fcb8951d0bb65d001a9480f7846e3f37c7e` | `CONFORMANCE_COMPLETE_9_OF_9_KERNEL_READY` |
| row status | `30185f8f432867c66acea27213d96c5a479b9d204d2603c26dac07a808c96626` | `FORMALIZATION_COMPLETE_9_OF_9_KERNEL_READY` |

The repeatable KERNEL receiver now has `9 KERNEL_READY / 0
PRECONDITION_NOT_REPLAYABLE`; all other prior compile receivers remain
successful.

### 4.2 SP2-05 covariance bundle

The prior covariance bundle at
`973c1f628474d321c64cd31e21ca73f8d9972e91ec19369dc63caccf2f10a131`
had six ready components and the single O02 gap. The successor replaces only
that O02 reference with the shared proof.

| SP2 artifact | SHA-256 | Result |
|---|---|---|
| successor covariance bundle | `a1f377eec3d75d28a441fac197c05e6b3687da25b22feb804ee15fef2bfb3369` | 7/7 covariance objects `KERNEL_READY`; zero gaps |
| compile result | `52b3a110fa45270c4c702e9ea66de65808bf0e637fe1b5d88d51ec00103b0ed5` | `CONFORMANCE_COMPLETE_8_BUILT_0_GAPS` |
| row status | `1a0544c1e7a101a36433065aef6b24d1d856aba3617834970682efefc0a4b09f` | `FORMALIZATION_COMPLETE_8_OF_8_PROOF_OBJECTS_READY` |

`r_kernel_covariance` changes from `PRECONDITION_NOT_REPLAYABLE` to `PASS`
with `7/7` required components. The two enumerations and exact index
comparisons, typed graph, exact fixture, premise schema, quartic KERNEL, and
axiom-hash comparison retain their successful prior results.

These are bounded formalization statuses. No evaluator chain was invoked, so
this relay does not assert a runtime row PASS or change a board.

## 5. Static battery and custody

The direct builder ran under `python3 -I -S -B`. Two predecessor inventories
rehash completely. The exact Gaussian-integer matrix engine independently
checks all displayed matrices and identities. An independent second checker
recanonicalized every JSON file, rehashed every referenced proof, confirmed
9/9 SP1 entries and 7/7 SP2 covariance entries, and reproduced both compile
outcomes.

Five negative controls bit: replacing `Gamma_cell` with the identity,
corrupting a source-span digest, substituting the unreversed quadrature for
`c_(rev c)`, retaining the SP1 D08 partial, and retaining the SP2 gap. A
second builder launch over occupied outputs refused
`OUTPUT_COLLISION:package outputs`.

The final package inventory has 15 members and SHA-256
`246364f183d0e00ec209fec47f92fe1a0be6e5d486988383f58ca47abfddaf44`.
The self-check hashes to
`b42e9d5412bb3921cf2f355a05299d966c3af81d1eba8cfd38ed6bdb46ce735d`.

M-2 checked exact, whitespace-normalized, hyphen/space/underscore, and
scope/self-reference surfaces across the packet. Other `U_c` tokens belong
to unrelated cell-evolution or monoidal records; none is used as the
orientation carrier. The construction instead derives the carrier from the
sealed grading, boundary, and quadrature equations.

`F_PLDEC`: CLEAN. No member binding, fixed-point execution, end test,
physical-quantity evaluation, or measured-constant comparison occurred.
`alpha_computed=false`, `proof_authorized=false`, and
`kappa_record_computed=false` remain in force. Admission remains barred.

Verb audit under the verdict-line scope rule: CLEAN. “Constructed” means the
closed typed matrix carrier and both exact conjugation proofs were emitted
and independently rehashed. “Formalization complete” is a bounded source
compile status, not evaluator execution, proof authorization, or admission.

CARRIER = constructed (proofs displayed)
ROWS = SP1-07 FORMALIZATION_COMPLETE_9_OF_9_KERNEL_READY, SP2-05 FORMALIZATION_COMPLETE_8_OF_8_PROOF_OBJECTS_READY
ADMISSION = barred, stated
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
