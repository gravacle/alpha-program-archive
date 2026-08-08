# Stage 8 / 7A Step 11 — D-A35-02 Quasi-Free CAR-Lift Instance — Codex 2 v001

Date: 2026-08-08  
Lane: CODEX 2  
Scope: closed `TYPE; EXACT` schema instance for `C-D-A35-02-QUASIFREE-CAR-LIFT`

## 0. Preflight and custody

The relay input
`relay_inbox/RELAY_PASTE_744_A35_02_INSTANCE_CODEX2_V001.md`
rehashed to
`9e42b9f5d244109d18da1e48fcbfa46d6d97e01796686dedbad9ff1246d30673`;
its sidecar and CODEX 2 lane guard matched. `relay_outbox/744_ACK.md` was
written before task work. The requested report and package names were absent
from the cleanroom and archive workspace.

| Sealed source | SHA-256 | Use |
|---|---|---|
| packet `review_packets/STAGE7_QSPEC_CANDIDATE_V001/BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md` | `949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd` | sole instance-content source |
| `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V012.md` | `382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504` | row and two-opcode box |
| `STAGE8_7A_U7_DISPOSITION_CODEX2_V001.md` | `0145c5dbbed1681067a211021892100cf6d18c6ef25ba9c7e905aeedc8a7f20d` | `C:CS/compile_schema_instance` custody ruling |

The row bytes at `SPEC[85375,85767)` rehash to the registered descriptor
digest
`95c5e259db89a8343a4545ae3ec0641f10c836ea702f880795a66d802c82c2bd`.
The instance contains only the row’s declared `TYPE` and `EXACT` receivers;
no proof receiver was introduced.

Every element is covered by one or more exact packet blocks:

| Block | Byte span | Block SHA-256 | Content |
|---|---:|---|---|
| `B_GLOBAL_PREMISE` | `[334,1102)` | `52139a1c600db4a96bf17194cce7c57f308b5f0c7b34d32d85ebd5dcf0e54e7c` | operator-valued functorial CAR-lift premise and primitive-class exclusion |
| `B_GLOBAL_TYPED` | `[1103,1704)` | `daeb7bc7b448e78009703e6fc7a7946a76844f7ee6f479327e63ab6ab84057d2` | one global source CAR and distinct even record factors |
| `B_GLOBAL_DESCENT` | `[1705,4005)` | `fcbb16c6cad76b08a210d55d42a1ce82d165ae3a0adfd63f28ba16f30946d1ce` | relabeling and orientation covariance maps for `h_K` |
| `B_GLOBAL_CAR` | `[4006,5026)` | `f08456525bf3f5abb163b32bc3e7c9d1f084c79adb1d1ede879df10cc6cad76b` | operator-valued lift, one-source recovery, vacuum normalization, and quartic control |

No requirement sentence is serialized as a proof. `CAR(K_Sigma)` is unfolded
only as its defining canonical anticommutation relation set for `TYPE/EXACT`;
the remaining atoms are direct canonicalizations of displayed equations and
statements in these blocks.

## 1. Closed schema instance

The cleanroom package is `step11_a35_02_instance/`. Canonical JSON uses UTF-8,
sorted keys, tight separators, finite values, and no trailing newline. The
closed instance schema hashes to
`f47236e6033112f76801a515e2b2b9fc3ba71aa569bbd5153cb39bed028a9d7a`;
the closed element schema hashes to
`e194e1856fafcf85b261280d0f440d2b6b5dcbb0b98a409b3232e9dbe268914b`.

The complete instance `generated/A35_02_instance.json` hashes to
`47485f836710f3819bfda19744b9303e0f9cd065d93fa6859df4b27efb7eb03a`.
Its ordered six-element census and each content-addressed element are:

| ID | SHA-256 | Sealed content canonicalized | Receivers |
|---|---|---|---|
| `E01_GLOBAL_CAR_EVEN_RECORD_CARRIER` | `a4398ba485191e7a5ae5c7ac88b84254047a3b8b7c321e722b1502f607727513` | `K_Sigma`, single `CAR(K_Sigma)`, canonical CAR relations, distinct even `R_c`, trivial record fermion grading | `TYPE`, `EXACT` |
| `E02_OPERATOR_VALUED_ONE_PARTICLE_ACTION` | `e9184a11ebdbc74951ed8fc1054c6e647b6f8b36d71ffefba81598a39c0e302a` | `h_K=sum |e_i><e_j| tensor b_ij,K` with `b_ij,K` acting on the even record carrier | `TYPE`, `EXACT` |
| `E03_NUMBER_PRESERVING_QUASIFREE_LIFT` | `ed13fd4b45836f88e849f63dfc6186355edd8e8329643dd9847a94261654c81f` | `H_K=sum a_i^* a_j tensor b_ij,K`, with source and record operator types separated | `TYPE`, `EXACT` |
| `E04_FUNCTOR_COVARIANCE_MAPS` | `3b5115a99d0803041fc28cd8bcaec96965964f80d6096f6ffd7022ae70a33a41` | source permutation, record conjugation, and the packet’s operator-valued functorial-CAR-lift atom | `TYPE`, `EXACT` |
| `E05_VACUUM_AND_ONE_SOURCE_RESTRICTION` | `b766c163fee6f481aa38c9e2f8e85daaa0bb69663c242409001f799df75c84a3` | `<Omega|H_K|Omega>=0` and `H_K` restricted to one source equals `h_K` | `EXACT` |
| `E06_QUARTIC_HIGHER_SECTOR_CONTROL` | `e3e09cc021bd6bf9eec884d567f14f6b6189a567ffdffdbb1702082a3b1aa6d9` | `H_lambda`, equality on vacuum/one-source sectors, nonzero two-source difference, retained rejection control | `TYPE`, `EXACT` |

Each filename begins with the SHA-256 of its exact canonical bytes. The
instance binds the six file references by relative path, byte length, and
SHA-256, and carries `gaps=[]` with `status=COMPLETE`.

## 2. Compile against the row box

### 2.1 `TYPE`

| Check | Result |
|---|---|
| one global source space and one global CAR algebra | `PASS` |
| distinct record factors with trivial fermion grading | `PASS` |
| operator-valued one-particle coefficients act on the even record carrier | `PASS` |
| `a_i^*a_j` source action and `b_ij,K` record action remain type-distinct | `PASS` |
| relabeling and record-conjugation covariance maps are typed | `PASS` |
| the quartic control is a higher-CAR sector object, not erased from the carrier | `PASS` |

Receiver result: `r_auto_01_type.status=PASS` with six checked atoms.

### 2.2 `EXACT`

| Check | Result |
|---|---|
| canonical CAR relations from the sealed `CAR(K_Sigma)` type | `PASS` |
| operator-valued lift formula | `PASS` |
| exact one-source restriction | `PASS` |
| functor covariance atom | `PASS` |
| public vacuum normalization | `PASS` |
| quartic equality on vacuum and one-source sectors | `PASS` |
| quartic nonzero difference on the `i,j`-occupied two-source sector | `PASS` |
| negative control retained and nonzero primitive `lambda` rejected by the adopted premise | `PASS` |

Receiver result: `r_auto_02_exact.status=PASS` with eight checked atoms.

The compile record hashes to
`d8db9f47cc3df31b26dc8f6ea6e0937e3bebc812c3521272002ee5a29868957c`
and returns `TYPE_PASS_EXACT_PASS`, with no gaps. The bounded row-status
record hashes to
`58fa77e0241b20a510b5ef224ca1f72d43e93c14b983d26a9e72480d390fda18`
and returns `INSTANCE_COMPLETE_TYPE_EXACT_COMPILE_READY`.

This status says the closed row instance compiles against its two structural
receivers. No evaluator chain was invoked, so it is not a runtime PASS or a
board change.

## 3. Static battery and scope

The direct builder ran under `python3 -I -S -B`; AST parsing and all three
source pins and four block pins passed. An independent pass recanonicalized
every JSON file, rehashed all six content-addressed filenames and all their
source spans, reproduced six `TYPE` and eight `EXACT` successes, and
confirmed the empty gap list.

Five negative controls bit: missing element, unpinned element, non-even
record grading, non-exact one-source restriction, and erased quartic control.
A second builder launch over occupied outputs refused
`OUTPUT_COLLISION:package outputs`.

The final generated inventory has 14 members and SHA-256
`52800b53895050c9bd511860a4654f8e90ae3b8f51024a08ae3974e5947d81e9`.
The self-check hashes to
`0c1cab23dc4afeaebb8cf7195c2177e807405a3d263cd8273144d2b8ebda2235`.

M-2 checked exact, whitespace-normalized, scope/self-reference, and
hyphen/space/underscore surfaces in the four source blocks. The instance
distinguishes the displayed low-sector equality from the displayed
higher-sector difference; neither is inferred from the other.

`F_PLDEC`: CLEAN. The sector labels and operator identities are finite
structural records. No member binding, fixed-point execution, end test,
physical-quantity evaluation, or comparison with a measured constant
occurred. `alpha_computed=false`, `proof_authorized=false`, and
`kappa_record_computed=false` remain in force. Admission remains barred.

Verb audit under the verdict-line scope rule: CLEAN. “Complete” means all six
declared content-addressed elements are present with no named gap. “Compile”
is the bounded `TYPE; EXACT` instance compile, not evaluator execution,
admission, or proof authorization.

INSTANCE = complete
COMPILE = TYPE_PASS_EXACT_PASS
ROW = INSTANCE_COMPLETE_TYPE_EXACT_COMPILE_READY
ADMISSION = barred, stated
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
