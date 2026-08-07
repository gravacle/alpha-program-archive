# STAGE8 TASK 6 / A35–RD-22 — evaluator specification V007

**Artifact:** `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V007.md`  
**Lane:** Codex Lane 2  
**Date:** 2026-08-07  
**Custody:** V007 repairs the five principal-ruled specification classes and coordinates Builder A's content-addressed re-pin; exactly one of the 66 V006 descriptor rows changes; any RD-22 invocation and any Builder B re-pin remain separate custody acts  
**Status:** V007 FINITE-DELTA SPECIFICATION ONLY — the Q-608 findings, explicit single-authority V009-06 criterion, fixture-span migration, P0 precedence, and fifth M-2 surface are installed; no criterion, physical check, fixture, physical quantity, fixed point, end test, or authorization is executed here

```text
V007 = 5 repairs
M2_CORPUS_RULE = executable and schema-bound
M2_REGISTRY = 17 rows (SPEC-INCOMPLETE pending sealed corpus definitions)
DESCRIPTOR_ROWS = 65 unchanged + C-B-V009-06 re-rendered
PROTECTED_SECTIONS = unchanged
CARRIAGE = complete_finite_delta
AUTHORIZATION = not_claimed
VERB_AUDIT_SELF = CLEAN
```

## 0. Preflight, scope, and authority boundary

### 0.1 Register and no-clobber checks

[PROVABLE] The commissioned live preflight identifies register head `Q-610`.
That entry records the explicit single-authority V009-06 ruling and the
coordinated V007 re-pin sequence. The Q-604 guard remains: one lawful row is
one row and is not evaluator closure.

[PROVABLE] Before V007 was written, neither its requested filename nor the
commissioned Lane 2 report filename existed in the cleanroom or archive
workspace. V006 remains intact. V007 is a byte-copy-plus-named-replacements
finite delta, not an overwrite.

### 0.2 Hash-verified authorities

| Authority | SHA-256 verified before use | Load-bearing use |
|---|---|---|
| `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V006.md` | `1b8b03e4b2688acb30d8c3f5afea3529be8322f8541406adae520aa51e654995` | immutable V007 carriage base |
| `STAGE8_TASK6_ENVELOPE_V006_CHECK_DARIO_V001.md` | `759caa1c0232d89f82cee6f46d0c6d01d4f4c069894c54ecc4cb31ac5c0bda83` | Q-608 four findings, fixture-span drift, and P0 precedence finding |
| `STAGE8_TASK6_REPLAY_ROLES_DARIO_V001.md` | `3fa5461f6639a02003a72e2ae667c527a5583522e1b111f5081092b5af48763f` | Q-610 replay-role result and Builder A invocation-linkage obligation |
| `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md` | `f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b` | immutable V006 carriage base; all descriptor criteria |
| `STAGE8_TASK6_GROUNDING_RELOCATION_DARIO_V001.md` | `69334875b94679c16da9b8d6153242241ca3c202f0facc6130596b9807189e6f` | C77 V009-06 grounding relocation and four-row Q-606 seed registry |
| `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V004.md` | `2c767bfc953c7efeeaf4a33542974b10e0a674a161a5f1a651f3486ac36fad8b` | immutable V005 carriage base |
| `STAGE8_TASK6_BR1_ADJUDICATION_DARIO_V001.md` | `ec0412d22db709e915abea001dfc110fe3050f5f0b6a74050f0421cf14304e38` | ten-row closed list; six lawful controls; BR-1/A regime text |
| `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V003.md` | `f910815c84fd29d3dc6ca55f43ebe5d4c7015f457ddcde7bd7a69afdf81658dc` | immutable V004 carriage base |
| `STAGE8_TASK6_SPEC_V003_CLASS_CHECK_CORRECTION_DARIO_V001.md` | `1f588534257ef274db43f3015ee3c587c76c114467a77acc38c62f354d248a5a` | Q-574 closed work list; BR-1/BR-2 law text and conformance criteria |
| `STAGE8_TASK6_SPEC_V003_CLASS_CHECK_DARIO_V001.md` | `01adfa83043bf1e01ffa965a7f955ebcce6b74b27e4e6728b71c375df7976063` | parent four-line residual check and blank-line-safe insertion correction |
| `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE3_V002.md` | `25e89ed24933d66fcb6991b83bb971775be834070f8570a8b89cd0248f22edb7` | immutable V003 carriage base |
| `STAGE8_TASK6_SPEC_V002_RERENDER_CHECK_DARIO_V001.md` | `da6575b0f366ec5af6aef008dd48c21ce028290fd7019a55b615afbbab67d772` | Q-567 binding-class conviction; implement without relitigation |
| `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE3_V001.md` | `eb2073ebb4f23cbc0c0bfa20a36c482e24c59dc6b6e1ccbcd1ef1bd1150d0ecb` | immutable V002 carriage base |
| `STAGE8_TASK6_A35_EVALUATOR_SPEC_REVIEW_DARIO_V001.md` | `a1f5b4c305dfa5f1ba0866e0f741ccdb611070cfa8b70e0aa362152be2ab44b6` | Q-559 census and aggregate firewall, confirmed and not relitigated |
| `STAGE8_TASK6_A35_SPEC_REVIEW_COMPLETION_DARIO_V001.md` | `0f57b662ed8d2ec383975a04a9d9b0764fca2b5e36e918fa6d456e89e2412442` | Q-561 map/runner/runtime confirmation and four required re-renders |
| `BID_FULL_STACK_REVIEW_LEDGER_V003.md` | `c09f2c246c48ddfd0df127da26a22f08ba9ffd44f5c2118c178a0a5eba5d00e8` | immutable blocker census and permanent regressions |
| `BID_CONSOLIDATED_HOSTILE_AUDIT_MATRIX_V005.md` | `78f6bb08b7ae89d700cf84a19ebf8e62fa489a4ec6762429ac46d027538cbfe3` | A35 requirement of record |
| `BID_SOURCE_PARENT_CLOSURE_GATE_V003.md` | `5c679e3741abe782688b8a75ffa1928c308775248e41af192d03976f01cb4dbf` | SP14 runner demands and source-parent scopes |
| `STAGE8_TASK6_LP_MATRIX_LEDGER_LANE3_V001.md` | `bc6c3e496ffd6e8d06cc3237e47a6a02b76faaa88b63b0ffb38684971c2d1362` | `missing_A35` and seal-rail consequence |
| `primitive_step6_content_addressed_runtime_gate_v012.md` | `34faecbfc0f0a741fbd93ed2698b7ba5a1f3262d4b7cb83c37a375c3c3abe63b` | detailed content-addressed, optimization-safe runner contract |
| `provenance/primitive_step6_runtime_snapshot_v012.json` | `50a6fc141a45451678aa7543e4f267ce26beb6e53182170b478acb6fb0e0f5bb` | runtime-v012 snapshot candidate |
| `provenance/primitive_step6_runtime_snapshot_v014.json` | `fb74b7566b5c7ae8da64096754b16570dc613c8afdd140abd7a0100d5fcc1a08` | runtime-pin discrepancy witness only |
| packet `STAGE7_PACKET_MANIFEST_V001.sha256` | `9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311` | sealed packet-native citation authority |
| packet `BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md` | `949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd` | SP1-07/SP2-05 executable positive obligations |
| packet `BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md` | `6f6b822ac8ccf9ea19659f4ccf811268f60a27a361f817ee6513479d63b62546` | SP2-06 free-subgate boundary |

[PROVABLE] In obedience to Q-562's custody correction, every line-number pin
added by V002 refers to a manifest-native sealed packet copy. The hash-pinned
V003 blocker ledger is cited by byte span; no unsealed-root V011 line number is
consumed.

The A35 row says, load-bearingly:

> Every blocker recorded in `BID_FULL_STACK_REVIEW_LEDGER_V003.md` has an
> executable check.

Its following “In particular” list is treated as a non-exhaustive refinement,
not as permission to omit earlier blockers.

SP14 requires, load-bearingly, a fresh direct parent, separate
content-addressed normal and real `python -O` children, an independent
verifier, parent-side runtime reclassification, before/after mutable macOS
trust-record validation, producer-output comparison, and one detached-signed
terminal local-assurance record. Child receipts are non-authoritative.

The LP-MATRIX ledger displays the missing object as

```text
missing_A35 :=
  content-addressed optimization-safe parent runner
  + independent verifier/evaluator
  + an explicit executable mapping for every V003/A35 blocker.
```

This specification defines those three components. It does not claim that
they exist as executable members.

### 0.3 Fences and non-actions

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
RD_22_execution_authorized = false
independent_seal_evaluator_implemented = false
```

[PROVABLE] No member is bound, no fixed point is run, no end test is formed,
no numerical value is evaluated, and no measured constant is read or compared.
The artifact does not alter a register, plan, tracker, git branch, commit, or
remote state.

## 1. S1 — blocker census

### 1.1 Stable-ID rule

[YOURS] A blocker ID is the immutable snapshot label plus its ordinal in the
numbered blocker list. Repair-map restatements do not create new IDs, because
the ledger rule says the failed rows persist and are not erased. The executable
`B_lambda` counterfamily is evidence for several many-record blockers, not an
additional numbered blocker.

The exact census is

```text
B-V008-01 .. B-V008-11       = 11
B-V009-01 .. B-V009-13       = 13
B-V010-01 .. B-V010-14       = 14
B-V011-MR-01 .. MR-09         = 9
B-V011-SP1-01 .. SP1-09       = 9
B-V011-SP2-01 .. SP2-07       = 7
                                      --
NUMBERED V003 BLOCKERS              = 63
```

The source spans are V003 lines 30–49, 107–134, 241–298, 331–352,
373–389, and 401–438 respectively, all inside the verified
`c09f2c24…` byte object.

### 1.2 V008 — eleven blockers

| Stable ID | Requirement of record |
|---|---|
| `B-V008-01` | Complete the maps among endpoint, chain, projective, tangent, and face carriers. |
| `B-V008-02` | Supply category identities/composition and decorated-morphism typing. |
| `B-V008-03` | Make public collapse natural and orientation coherent, and treat the overall constraint scale honestly. |
| `B-V008-04` | Do not apply a free-group representation to partial shifts on arbitrary finite complexes. |
| `B-V008-05` | Correct the universal plaquette word’s opposite holonomy. |
| `B-V008-06` | Do not infer Fubini–Study uniqueness from passive coordinate covariance; disclose imported kinematic scope. |
| `B-V008-07` | Complete disconnected gauge stabilizers and real/complex face-map typing. |
| `B-V008-08` | Restrict the flux lift to `im(d_1)`. |
| `B-V008-09` | Make physical-interval and Maxwell-completion obligations executable without later choices. |
| `B-V008-10` | Separate specification, core, and final seals and content-address reconstruction/review dependencies. |
| `B-V008-11` | Preserve historical target awareness and require a genuinely forward external holdout. |

### 1.3 V009 — thirteen blockers

| Stable ID | Requirement of record |
|---|---|
| `B-V009-01` | Define `E_open` on actual object fibers before any trivialization. |
| `B-V009-02` | Remove the undefined common positive dimensionful-scale equivalence. |
| `B-V009-03` | Reconcile global `pi_U(W_univ)` with the displayed local holonomy block. |
| `B-V009-04` | Give formal I-adic, holomorphic-principal, and norm-Taylor logarithms distinct domains. |
| `B-V009-05` | Define `F_pi^n`, `gr_pi^n`, and the kernel quotient testing a nonzero represented symbol. |
| `B-V009-06` | Encode the seal graph literally through specification, core, parent, holdout, reconstruction, and final review. |
| `B-V009-07` | Freeze the response complex, background connection, root preparation, and finite-to-continuum sequence. |
| `B-V009-08` | Do not promote a two-path authority to general finite-Hilbert Born/Fubini–Study kinematics. |
| `B-V009-09` | Keep the dimensionless charged response independent of a future favorable interval. |
| `B-V009-10` | Supply a deterministic local-Maxwell reconstruction from the global response. |
| `B-V009-11` | Freeze the Lorentzian Hodge operator and its exact application domain. |
| `B-V009-12` | Freeze the Hamiltonian-to-action map and normalization. |
| `B-V009-13` | Make holdout selection outcome-masked, deterministic, and fail-closed under contamination. |

### 1.4 V010 — fourteen blockers

| Stable ID | Requirement of record |
|---|---|
| `B-V010-01` | Reproduce the nonextensive direct-sum response with zero thermodynamic stiffness and reject every after-the-fact extensive factor. |
| `B-V010-02` | Admit the complete `Gamma_c=-c log\|A\|`, `c>0`, family until a physical amplitude fixes normalization. |
| `B-V010-03` | Admit the complete `exp(-i tau B_L)`, `tau>0`, family until a target-free record rule fixes the interval. |
| `B-V010-04` | Keep primitive `kappa_record` distinct from the complete threshold-matched Thomson coupling. |
| `B-V010-05` | Prove anisotropic scale cancellation from an exact tetrad/Hodge face measure. |
| `B-V010-06` | Derive a target-independent preparation domain and enumerate all invariant competitors. |
| `B-V010-07` | Freeze exact real modes, polarization normalization, Hermitian rows, volumes, and real/complex factors. |
| `B-V010-08` | Define the normalized topological tensor and Frobenius-orthogonal section of the rank-20 quotient. |
| `B-V010-09` | Replace finite-ray locality by a uniform full-neighborhood analytic theorem with remainder. |
| `B-V010-10` | Establish invariance on a sealed refinement class or state the restricted scope. |
| `B-V010-11` | Type first-opening edges and `{M,Q,G}` labels in objects and morphisms. |
| `B-V010-12` | Compute a noncyclic seal DAG from immutable reports; omit alpha from core. |
| `B-V010-13` | Make the holdout universe exhaustive, canonical, independently committed, externally beaconed, and structure-sensitive. |
| `B-V010-14` | Use Fubini–Study only as a check after the independently fixed physical amplitude/action convention. |

### 1.5 V011 many-record — nine blockers

| Stable ID | Requirement of record |
|---|---|
| `B-V011-MR-01` | Derive or disclose the target monoidal category and strong-monoidal structure. |
| `B-V011-MR-02` | Resolve or carry the bosonic/fermionic/hard-core/distinguishable statistics family. |
| `B-V011-MR-03` | Fix shared-boundary gluing rather than infer it from disjoint composition. |
| `B-V011-MR-04` | Detect overlap interactions invisible on vacuum and one-record sectors. |
| `B-V011-MR-05` | Resolve continuous-sum, ordered, sequential, Trotter, and circuit evolutions. |
| `B-V011-MR-06` | Resolve connected product/entangled/thermal/ground/clustering preparation alternatives. |
| `B-V011-MR-07` | Prove the certified zero-free domain contains the independently derived record interval. |
| `B-V011-MR-08` | Reproduce the exactly zero root-survival amplitude and reject semantic substitution of a convenient response. |
| `B-V011-MR-09` | Derive charged access for the full star or a complete composite-handle operator; one handle is insufficient. |

### 1.6 V011 source-parent round 1 — nine blockers

| Stable ID | Requirement of record |
|---|---|
| `B-V011-SP1-01` | Replace chirality-label `C^2` by a typed Dirac particle/antiparticle carrier and hypersurface inner product. |
| `B-V011-SP1-02` | Derive the chiral-odd boundary map as a Lorentz-covariant intertwiner. |
| `B-V011-SP1-03` | Define and verify complete CPT. |
| `B-V011-SP1-04` | Retain/classify the axial phase through measure, anomaly, topology, and CP, or prove response independence. |
| `B-V011-SP1-05` | Classify the complete source-decorated incidence family. |
| `B-V011-SP1-06` | Derive the charged source-flux projector from the sealed current. |
| `B-V011-SP1-07` | Compose one global source CAR algebra with even record factors and derive gluing, overlap, and ordering. |
| `B-V011-SP1-08` | Derive a complete physical two-point function before assigning mass meaning. |
| `B-V011-SP1-09` | Replace representative arithmetic checks with an independent exhaustive source-parent audit. |

### 1.7 V011 source-parent round 2 — seven blockers

| Stable ID | Requirement of record |
|---|---|
| `B-V011-SP2-01` | Execute standard Dirac CPT, normal pushforward/reorientation, different-normal transport, weighted adjoint, phase nullspace, and nonzero neutral/charged controls. |
| `B-V011-SP2-02` | Keep raw `b_partial` distinct from physical `c_partial=i Gamma_cell b_partial` even when their squares agree. |
| `B-V011-SP2-03` | Construct C and P separately, combine CP, preserve the axial domain, and account for Fujikawa Jacobian, determinant ratio, boundary/eta, spectral pairing, and a nonzero-index control. |
| `B-V011-SP2-04` | Separate multiplicity from Dirac spin and solve the complete projection-module control family uniquely as `PBP`. |
| `B-V011-SP2-05` | Build one source CAR/even-record global carrier from cell pushouts, prove covariance/associativity, recover SP17, keep primitive overlap distinct from `h_K^2`, and reject the quartic competitor. |
| `B-V011-SP2-06` | Derive Lorentzian pole/threshold status, sign, state/CTP, durability, spectral positivity, gauge/edge dressing, IR behavior, and absence of adjustable subtraction. |
| `B-V011-SP2-07` | Every load-bearing audit must be free of Python `assert`, agree under normal and optimized execution, run under a content-addressed isolated runtime, and pass a terminal seal. |

### 1.8 Census discrepancies — displayed, not harmonized

[PROVABLE] The exact/scope/synonym sweep gives these discrepancies:

1. **Title/operative-scope mismatch.** A35’s title says “V010/V011,” while its
   first sentence imports every V003 blocker. Therefore all 24 V008/V009 rows
   remain in scope; the title cannot truncate the universal sentence.
2. **`D-A35-01`, A35-only sharpening.** A35 expressly requires a *zero-index*
   anomaly/determinant evaluation. V003 SP2-03 requires the Jacobian,
   determinant ratio, boundary/eta accounting, and a nonzero-index control but
   does not state a zero-index evaluation as a blocker.
3. **`D-A35-02`, A35-only sharpening.** A35 expressly requires an
   *operator-valued quasi-free CAR lift*. V003 SP2-05 requires the global CAR
   carrier and quartic control, but its blocker sentence does not state that
   lift as a standalone property.
4. **`D-A35-03`, A35-only sharpening.** A35 expressly requires physical
   *residue*. V003 SP2-06 requires a positive physical spectral measure and
   pole/threshold classification, but does not state residue as a standalone
   blocker property.

[PROVABLE] V003 also records two unnumbered, permanent pre-seal regression
obligations: reject the rank-21/topological-null route and reject an implicit
response-to-action conversion factor. They are not silently promoted to
numbered blockers. Their exact predicates are carried as additional conjuncts
of `C-B-V010-08` and `C-B-V010-14` below. This avoids both omission and double
counting.

Thus:

```text
numbered blockers                 = 63
A35-only refinement requirements =  3
executable check descriptors      = 66
```

No numbered V003 blocker is omitted by A35’s operative universal sentence.

## 2. S2 — executable-check language and content addressing

### 2.1 One immutable subject and mandatory inputs

[YOURS] Every check descriptor consumes the following **content-addressed**
base tuple `BASE`; no path or status string is authority:

```text
BASE := (
  requirement_source = {path, sha256, byte_span, stable_id},
  A35_source          = {path, sha256, byte_span},
  subject_manifest    = {canonical_manifest_bytes, sha256},
  subject_files       = sorted[{relative_path, byte_length, sha256}],
  evidence_manifest   = sorted[{relative_path, byte_length, sha256}],
  check_descriptor    = {canonical_descriptor_bytes, sha256},
  checker_module      = {source_bytes, sha256},
  proof_axioms        = {canonical_manifest_bytes, sha256},
  runtime_subject     = {snapshot_bytes, sha256, trust_root_sha256},
  fixture_manifest    = {canonical_manifest_bytes, sha256},
  authorization       = {RD22_artifact_or_null, sha256_or_null}
)
```

The content root is defined without path trust:

```text
content_root(M) :=
  SHA256("A35-CONTENT-ROOT-v1\0" ||
         concat(sort(relative_path || NUL || decimal_byte_length || NUL ||
                     lowercase_sha256 || LF))).
```

Precondition `P0` for every row is

```text
P0 := strict_parse(BASE)
   and every_declared_sha256_matches_the_supplied_bytes
   and content_root(subject_files)=subject_manifest.declared_root
   and content_root(evidence_files)=evidence_manifest.declared_root
   and no_duplicate_path_or_key
   and every_required_input_present.
```

If `P0=false`, the row returns `FAIL(INPUT_INTEGRITY)`. It never infers PASS
from a manuscript flag, filename, prior child receipt, or absent input.

[YOURS] **Precedence is total.** P0 integrity is evaluated first. If `P0=false`,
the row terminates as `FAIL(INPUT_INTEGRITY)` before any `SPEC-INCOMPLETE`
classification is considered. Only a P0-clean row may then be classified
`SPEC-INCOMPLETE` because a required sealed corpus definition is absent. The
classification does not replace, mask, or outrank a P0 failure.

### 2.2 Deterministic procedure opcodes

[YOURS] A check procedure is a finite ordered list over this closed opcode set.
Each opcode has one result object and one Boolean success bit:

| Opcode | Deterministic operation |
|---|---|
| `STRICT` | Parse canonical UTF-8 JSON/text with duplicate keys, nonfinite numbers, undecodable bytes, and undeclared fields rejected. |
| `SCHEMA(s,x)` | Validate `x` against the content-addressed closed schema `s`; extra and missing fields fail. |
| `TYPE(g)` | Validate every object, domain, codomain, decoration, identity, and composable edge in graph `g`. |
| `EXACT(e)` | Normalize rational, integer, finite-matrix, polynomial, exterior-algebra, or declared algebraic expressions and compare canonical normal forms. |
| `KERNEL(p,a)` | Replay proof object `p` using only hash-pinned axioms `a`; an unproved step or undeclared axiom fails. |
| `ENUM(grammar,cert)` | Enumerate the finite grammar in canonical lexicographic order and replay an independent completeness certificate. |
| `DOMAIN(f,D)` | Prove from the typed graph that `f` is used exactly on `D`; any implicit extension fails. |
| `UNITS(e)` | Propagate declared dimensions/sector units through `e`; an implicit conversion or “set to one” fails. |
| `DAG(G,P)` | Parse nodes and exact parent lists, reject cycles/self-parenting/missing parents, and compare with required parents `P`. The single-authority form `DAG(G,PRINCIPAL_SINGLE_AUTHORITY)` is permitted only where a pinned principal ruling declares that the one sealed encoding `G` is itself both graph and required-parent schema; in that form no second object is synthesized and the comparison clause is discharged by the ruling's identity. |
| `M2(q,S)` | Before searching, require `S` to resolve to a P0-verified, content-addressed instance of the closed `SEALED_CORPUS_DEFINITION` schema below and verify every declared member; otherwise do not start and classify the row `SPEC-INCOMPLETE`. Then run fixed-string, whitespace-normalized, and scope-and-synonym AST/context guards over exactly those members, neutralizing the five registered false-negative modes in §12.4 and recording every hit with its source span. |
| `SYMBOLIC(e)` | Reduce a declared symbolic expression/limit exactly; permitted only in a `GATED-EXECUTION` row after its gate opens. |
| `SPECTRAL(e)` | Form determinant/index/resolvent/pole/residue/spectral objects under their declared domain; permitted only in a gated row. |
| `COMPARE(x,y,mask)` | Canonicalize only the predeclared process-local fields in `mask`, then require byte equality of all other fields. |
| `RUNTIME(r)` | Rehash/reclassify modules, native images, open events, runtime trees, process/network/mutation events, and trust snapshots under the pinned runtime contract. |

No opcode invokes an approximate optimizer, stochastic search, desired target,
measured constant, reader, or undeclared network service.

#### V007 sealed-corpus law for `M2(q,S)`

[YOURS] For every invocation `M2(q,S)`, the operand `S` **MUST name a
`SEALED_CORPUS_DEFINITION`**: a sealed canonical UTF-8 JSON object with exactly
the following fields and no others:

```text
{
  schema: "rd22.sealed-corpus-definition.v001",
  members: sorted[{relative_path:string, byte_length:nonnegative_integer,
                   sha256:lowercase_sha256}],
  declared_root: lowercase_sha256
}
```

`members` is sorted lexicographically by `relative_path`; member paths are
unique and relative; and `declared_root = content_root(members)` under §2.1.5.
The definition itself is named by path plus SHA-256 in the P0-verified input
manifest. **The implementation must verify the definition bytes, its closed
schema, its declared root, and every member's byte length and SHA-256 before
`M2` starts.** A directory listing, an inline ad hoc set, a generic source-set
label, or a set inferred by the evaluator is not a sealed corpus definition.

If a row invokes `M2(q,S)` but `S` does not name such a sealed definition, that
row is `SPEC-INCOMPLETE`: its evidence remains unavailable, `M2` does not
start, and the row cannot return PASS. Supplying the missing corpus definition
is a later content-addressed input action; it does not authorize changing the
row's criterion or choosing members after the query is known.

The V007 sweep of all 66 descriptor rows finds the following complete affected
registry. `S operand` reproduces the current operand when the descriptor names
one; `unnamed` means the shorthand descriptor does not expose a second
argument. None is presently a sealed corpus definition of record.

| Check ID | Current `S` operand or shorthand corpus | V007 classification |
|---|---|---|
| `C-B-V008-06` | unnamed: all Fubini–Study/uniqueness claim sources | `SPEC-INCOMPLETE` |
| `C-B-V008-10` | unnamed: alpha/core and reconstruction/review dependency sources | `SPEC-INCOMPLETE` |
| `C-B-V008-11` | `preseal_sources` | `SPEC-INCOMPLETE` |
| `C-B-V009-01` | unnamed: abstract-line-alias sources | `SPEC-INCOMPLETE` |
| `C-B-V009-08` | unnamed: general-FS-claim sources | `SPEC-INCOMPLETE` |
| `C-B-V010-02` | `{p_c_status,G_c_selector_parents}` | `SPEC-INCOMPLETE` |
| `C-B-V010-03` | `{p_selector_status,G_selector_parents}` | `SPEC-INCOMPLETE` |
| `C-B-V010-04` | unnamed: all `kappa_record`, `kappa_Thomson`, and alpha occurrence sources | `SPEC-INCOMPLETE` |
| `C-B-V010-10` | `output_claim_sources` | `SPEC-INCOMPLETE` |
| `C-B-V010-13` | `preseal_sources` | `SPEC-INCOMPLETE` |
| `C-B-V010-14` | `preseal_sources` | `SPEC-INCOMPLETE` |
| `C-B-V011-MR-02` | `selector_sources` | `SPEC-INCOMPLETE` |
| `C-B-V011-MR-04` | `S_claim` | `SPEC-INCOMPLETE` |
| `C-B-V011-MR-06` | `{p_prep_selector,G_prep_parents}` | `SPEC-INCOMPLETE` |
| `C-B-V011-SP1-04` | `response_sources` | `SPEC-INCOMPLETE` |
| `C-B-V011-SP1-05` | `selection_sources` | `SPEC-INCOMPLETE` |
| `C-B-V011-SP2-07` | `{producer_sources,verifier_sources}` | `SPEC-INCOMPLETE` |

#### V003 criterion-result binding

[YOURS] V003 adds no opcode. It makes the existing success bits executable in
the criterion language. For each ordered invocation, write

```text
r_name := OPCODE(arguments),
b_name := r_name.success.
```

A finite universal conjunction ranges only over the canonical finite output of
an `ENUM` call. A proof input has the closed content-addressed shape

```text
{canonical_goal_bytes, goal_sha256,
 proof_bytes, proof_sha256, axiom_manifest_sha256},
```

and contributes a Boolean only through `KERNEL(proof,axioms).success`. A
completeness input has a finite grammar plus an independent certificate and
contributes a Boolean only through `ENUM(grammar,certificate).success`.
`SCHEMA`, `TYPE`, `DOMAIN`, `UNITS`, `DAG`, `M2`, `EXACT`, `COMPARE`,
`RUNTIME`, `SYMBOLIC`, and `SPECTRAL` likewise contribute only their defined
result fields. Every indexed manifest must carry the SHA-256 of the graph,
grammar, proof, or result it indexes and must match the `P0`-verified supplied
bytes.

[YOURS] A criterion is **opcode-reducible** exactly when each of its atoms is
one of:

```text
an opcode success/result field;
a field admitted by a content-addressed closed schema;
an exact content-addressed input or expected fixture record;
a finite conjunction over an ENUM result;
a term defined by the preceding three forms.
```

Words such as `certified`, `derived`, `proved`, `silently`, `displayed`,
`target-independent`, `exhaustive`, or `all structural laws` have no Boolean
force by themselves. A proof, premise entailment, or derivation contributes only
through a pinned `KERNEL(...).success`; completeness contributes only through
`ENUM(grammar,cert).success`; comparison of enumerated objects contributes only
through `COMPARE` applied to their enumerated IDs or result records. A criterion
atom using one of the listed adjectives must name its receiving opcode result or
be deleted.

[YOURS] A carried compact row is BOUND only when its backticked opcode sequence
has a one-to-one expansion into ordered result objects and every prose atom in
its `PASS iff` cell is exactly a field of those results. The compact notation
does not excuse a proof, completeness certificate, enumerated comparison, or
load-bearing adjective; those classes require the explicit named form used by
the 28 V003 re-renders below.

#### V005 binding-receiver laws and conformance classes

[YOURS] The following are specification **LAW**, not review guidance.

```text
(BR-1) NO PRODUCER-DECLARED OBJECT MAY CARRY A CRITERION'S DIRECTION.

If the truth of a PASS-criterion atom depends on the CONTENT of a producer-supplied
object E -- an expected ledger, status record, or manifest VALUE -- then the row
must also contain an opcode result that forces that content independently of the
producer. Admissible forcers, exhaustively:
  (a) a content-addressed CLOSED SCHEMA that fixes the required VALUES, not merely
      the field shape;
  (b) a KERNEL replay whose conclusion is COMPAREd to E; or
  (c) a SPEC-FIXED constant or constant set that E is COMPAREd against.
A COMPARE between a computed object and a producer-declared expectation is a
SELF-CONSISTENCY check and carries NO directional force by itself.

Rationale of record: hash-pinning prevents SUBSTITUTION, not FABRICATION. The
existing manifest rule at 12.2 forces every indexed manifest to be content-addressed
and P0-verified, which stops post-hoc swapping and does not constrain what was
pinned.

(BR-2) A REDUCTION OPCODE'S .success IS NOT A TRUTH VALUE.

SYMBOLIC(e).success and SPECTRAL(e).success mean the reduction or formation
succeeded, not that e holds. Any criterion atom asserting that a RELATION HOLDS must
either pair the reduction with a COMPARE against a spec-fixed expected value, or use
EXACT (which compares canonical normal forms) or KERNEL (which replays a proof).
A bare SYMBOLIC/SPECTRAL success bit may be conjoined only where the row asserts
nothing about the reduced expression's value.
```

The spec-fixed BR values used below are the canonical tokens `ADMITTED`,
`REJECTED`, `FAILS`, `ALLOWED`, `REJECTED_DIMENSIONFUL`, `CONTAINED`,
`INSUFFICIENT`, `INDEX_ONE`, `Z_NOT_SUFFICIENT`, and
`INTERTWINER_IDENTITY`. They are constants in this specification, not producer
fields. `ASSERTION_FREE_FORMATION(r)` is descriptor metadata, not an opcode or
Boolean: it is lawful only when `r.success` asserts formation/reduction and no
criterion atom consumes `r`'s value.

```text
BR1_CONFORMANCE_CLASS = ADJUDICATED
BR2_CONFORMANCE_CLASS = MECHANICAL
```

[YOURS] The TEST-CLASS RULE is exact: mechanical candidate generation is not a
BR-1 verdict, while BR-2's pairing question is decided from the spec syntax
itself. The law's BR-1 regime is:

```text
(BR-1/A) BR-1 CONFORMANCE IS ADJUDICATED, NOT SWEPT.

A BR-1 verdict is a per-row reading, performed by a reviewer and DISPLAYED. It has
three ordered steps, all of which must appear in the artifact that claims the verdict:

  1. CANDIDATE GENERATION (mechanical, over-generating).
     Emit every PASS-criterion atom whose expected side is a field of a producer
     supplied E_*/M_* object, EXCLUDING (i) pure ID-set comparisons paired with a
     proof-index or enumeration comparison, and (ii) comparisons whose expected side
     is a spec-fixed constant. The generator MUST over-generate: a candidate is not
     a finding, and a zero-candidate row still requires step 3's one-line note.

  2. CLAUSE DECOMPOSITION (from the SEALED BLOCKER, not from the spec).
     Split the blocker at its span into its separate directional demands. A clause
     joined by "and", or introduced by a semicolon, is a separate demand.

  3. ADJUDICATION (per candidate).
     For each candidate, name which blocker clause its field carries.
       - If that clause is received elsewhere in the row by a spec-fixed constant,
         a KERNEL conclusion comparison, or a value-fixing closed schema, the
         candidate is LAWFUL and the receiver MUST BE NAMED.
       - If the field carries a clause with no other receiver, the row is DEFECTIVE.
     A candidate dismissed without naming its receiver is not adjudicated.

A BR-1 report states: candidates generated, clauses decomposed, and a verdict with a
named receiver for every candidate. A report of "zero failures" without those three
displays is NOT a BR-1 result and may not be registered as one.

(BR-2 is unaffected: it IS mechanical, and two independent implementations agreed
at zero. The distinction is that BR-2 asks a question about the SPEC's own syntax --
is this success bit paired -- while BR-1 asks a question whose answer lives in the
BLOCKER.)
```

The BR-2 procedure remains named and closed:

```text
BR2_REDUCTION_TRUTH_CONFORMANCE_V001(spec_bytes):
  rows := strict_parse_the_66_descriptor_rows(spec_bytes)
  for each assignment r := SYMBOLIC(...) or r := SPECTRAL(...):
    if r.success reaches PASS directly or through a named finite conjunction:
      accept only if (i) a conjoined COMPARE(r.result_or_classification,
      SPEC_FIXED_VALUE,empty) receives the asserted relation, (ii) the relation
      is instead received by EXACT or KERNEL, or (iii) the row contains
      ASSERTION_FREE_FORMATION(r) and no value/result field of r reaches a
      criterion atom
    emit {check_id,result_name,opcode,unreceived_relation} for every failure
  return failures sorted by {check_id,result_name}
```

BR-1/A and BR-2 each consume the whole final file, not a repair-row allowlist. A
self-consistency comparison may remain as evidence, but it is never counted as
the directional receiver. A row outside the ten-row closed list requiring an
edit is a finding and may not be silently changed.

### 2.3 Execution classes and statuses

[PROVABLE] The task’s class boundary is applied literally:

```text
STRUCTURAL       := the procedure checks types, exact symbolic identities,
                    finite enumerations, schemas, provenance, or protocols
                    without forming a fenced physical quantity.

GATED-EXECUTION  := running the procedure would form/evaluate a physical
                    response, survival amplitude, determinant/anomaly,
                    record-interval containment, two-point/pole, or residue.
```

[YOURS] The only row statuses are:

```text
PASS | FAIL | NOT_RUN_GATE | ERROR
```

For a gated row:

```text
gate_open=false or RD22 authorization absent
  => status=NOT_RUN_GATE,
     procedure_started=false,
     PASS=false.
```

This artifact supplies descriptors only. Every row therefore has
`implementation=false` and `execution_status=UNEXECUTED_SPEC`; that fact is
not a row verdict.

## 3. V008/V009 blocker-to-check map

For every table in §§3–8, the blocker requirement and source anchor are
[PROVABLE]; the finite executable procedure and exact Boolean criterion are
[YOURS]. “Inputs” means hash-pinned additions to `BASE`. Every criterion is
implicitly conjoined with `P0`.

### 3.1 V008 checks

| Check ID | Class | Content-addressed inputs beyond `BASE` | Ordered executable procedure | PASS iff |
|---|---|---|---|---|
| `C-B-V008-01` | STRUCTURAL | carrier/map schema; endpoint, chain, projective, tangent, face manifests | `STRICT; SCHEMA; TYPE` the entire carrier graph; compose every generator path | all five carrier classes exist, every required arrow has exact domain/codomain, and every declared composite is typed and equal on a canonical basis |
| `C-B-V008-02` | STRUCTURAL | category/decorated-morphism schema; finite generator list | `TYPE` all objects/morphisms/decorations; `EXACT` identities, every composable generator triple, and label preservation | identities and associativity hold and no decoration is lost or invented |
| `C-B-V008-03` | STRUCTURAL | collapse covectors; orientation involution; sequential-composition proof | `KERNEL` replay naturality and orientation squares; `EXACT` sequential collapse and `ker(lambda q)=ker(q)` for symbolic nonzero `lambda` | all squares commute, reversal has the declared sign, sequential collapse agrees, and only the constraint ray—not an absolute scale—is claimed |
| `C-B-V008-04` | STRUCTURAL | periodic `K_L`; global shifts; nonperiodic partial-shift negative fixture | `TYPE` shift domains; `EXACT` unitarity and word multiplication on `K_L`; apply the same contract to the nonperiodic fixture | periodic global shifts pass the representation laws and the partial/nonperiodic competitor is rejected |
| `C-B-V008-05` | STRUCTURAL | universal word; `pi_U`; noncommuting plaquette fixture | `EXACT` expand `pi_U(W_univ)` blockwise and compare with `W` and `W^{-1}` | equality with `W` holds and the inverse/opposite-holonomy competitor fails on the noncommuting fixture |
| `C-B-V008-06` | STRUCTURAL | claim/authority AST; passive-coordinate maps; standard-input manifest | `M2` all Fubini–Study/uniqueness claims; `TYPE` passive pullback; `EXACT` orbit-pullback identity | the FS premise is marked imported, passive covariance proves only pullback covariance, and no uniqueness inference remains |
| `C-B-V008-07` | STRUCTURAL | gauge complex by component; real and complex face maps | `EXACT` connected-component quotient `A_R^0/ker d0`; `TYPE` the real-form map and complexification seams | every component’s stabilizer quotient is present and all real/complex domains and seams compose |
| `C-B-V008-08` | STRUCTURAL | `d1`; `F_phys`; `Q_flux`; finite in-image basis grammar/certificate `(G_im,p_im)`; pinned right-inverse/minimum-norm proofs `(p_right,p_min)`; expected proof ledger `E_flux`; outside-image unit-face fixture | `r_im:=ENUM(G_im,p_im)`; `r_exact_im:=EXACT(F_phys=im(d1))`; `r_domain:=DOMAIN(Q_flux,im(d1))`; `r_right:=KERNEL(p_right,proof_axioms)`; `r_min:=KERNEL(p_min,proof_axioms)`; `r_compare_right:=COMPARE(r_right.conclusion,E_flux.right_inverse,empty)`; `r_compare_min:=COMPARE(r_min.conclusion,E_flux.minimum_norm,empty)`; `r_out_domain:=DOMAIN(Q_flux,outside_fixture)`; `r_out:=COMPARE(r_out_domain.status,E_flux.outside_rejection,empty)` | `P0 and r_im.success and r_exact_im.success and r_domain.success and r_right.success and r_min.success and r_compare_right.success and r_compare_min.success and r_out.success` |
| `C-B-V008-09` | STRUCTURAL | interval/Maxwell closure schemas; finite candidate/tie/failure grammar and certificate `(G_branch,p_branch)`; expected branch-ID ledger `E_branch`; spec-fixed per-ID map `BRANCH_OUTCOME:G_branch.ids->{ADMITTED,REJECTED}`; dependency graph | `r_enum:=ENUM(G_branch,p_branch)`; `r_ids:=COMPARE(r_enum.ids,E_branch.ids,empty)`; for every `b` in `r_enum.items`, `r_schema_b:=SCHEMA(S_branch,b)` and `r_out_b:=COMPARE(r_schema_b.classification,BRANCH_OUTCOME[b],empty)`; `r_dag:=DAG(G_dependencies,P_dependencies)` | `P0 and r_enum.success and r_ids.success and r_dag.success and (for every b in r_enum.items: r_schema_b.success and r_out_b.success)` |
| `C-B-V008-10` | STRUCTURAL | seal-stage schemas and exact parent lists | `DAG` the specification/core/final graph; `M2` alpha/core and reconstruction/review dependencies | stages are distinct, parents are literal and acyclic, content hashes are mandatory, and alpha is absent from core |
| `C-B-V008-11` | STRUCTURAL | holdout registry/commitment/beacon/eligibility schema and manifest `(S_holdout,M_holdout)`; protocol proof `p_holdout`; finite contamination-transition grammar/certificate `(G_contam,p_contam)`; expected transition-ID ledger `E_contam`; spec-fixed transition result `FAILS`; outcome-access query `q_outcome` | `r_schema:=SCHEMA(S_holdout,M_holdout)`; `r_access:=M2(q_outcome,preseal_sources)`; `r_protocol:=KERNEL(p_holdout,proof_axioms)`; `r_enum:=ENUM(G_contam,p_contam)`; `r_ids:=COMPARE(r_enum.ids,E_contam.ids,empty)`; for every `m` in `r_enum.items`, `r_m:=EXACT(m(M_holdout))` and `r_cmp_m:=COMPARE(r_m.normal_form,FAILS,empty)` | `P0 and r_schema.success and r_access.success and r_access.hits=empty and r_protocol.success and r_enum.success and r_ids.success and (for every m in r_enum.items: r_m.success and r_cmp_m.success)` |

### 3.2 V009 checks

| Check ID | Class | Content-addressed inputs beyond `BASE` | Ordered executable procedure | PASS iff |
|---|---|---|---|---|
| `C-B-V009-01` | STRUCTURAL | actual object fibers; `E_open`; canonical summand inclusions | `TYPE` each fiber and inclusion before any basis/trivialization; `M2` abstract-line aliases | every `E_open` component lands in its actual object-fiber carrier and no unlicensed trivialization is consumed |
| `C-B-V009-02` | STRUCTURAL | equivalence grammar/certificate `(G_equiv,p_equiv)` containing spec-fixed `DIMENSIONFUL_SCALE_EQUIVALENCE_ID`; unit/sector declarations; expected allowed-ID ledger `E_equiv`; spec-fixed per-ID map `EQUIV_CLASS:G_equiv.ids->{ALLOWED,REJECTED_DIMENSIONFUL}` with `EQUIV_CLASS[DIMENSIONFUL_SCALE_EQUIVALENCE_ID]=REJECTED_DIMENSIONFUL` | `r_enum:=ENUM(G_equiv,p_equiv)`; `r_ids:=COMPARE(r_enum.ids,E_equiv.ids,empty)`; `r_dim:=EXACT(DIMENSIONFUL_SCALE_EQUIVALENCE_ID in r_enum.ids)`; for every `e` in `r_enum.items`, `r_units_e:=UNITS(e)` and `r_cmp_e:=COMPARE(r_units_e.classification,EQUIV_CLASS[e],empty)` | `P0 and r_enum.success and r_ids.success and r_dim.success and (for every e in r_enum.items: r_units_e.success and r_cmp_e.success)` |
| `C-B-V009-03` | STRUCTURAL | `M_W`, global word, fiber restrictions | `TYPE` the direct sum and restrictions; `EXACT` global equality then each local block | global and local equations have distinct correct types and every restriction equals its named holonomy block |
| `C-B-V009-04` | STRUCTURAL | three logarithm definitions/domains; finite admitted-input/domain-partition grammar and independent completeness certificate `(G_log_domain,p_log_domain)`; boundary fixtures indexed by the enumerated IDs | `r_enum:=ENUM(G_log_domain,p_log_domain)`; `r_ids:=COMPARE(r_enum.ids,boundary_fixtures.ids,empty)`; for every `x` in `r_enum.items`, `r_formal_x:=DOMAIN(log_formal,D_formal[x])`, `r_principal_x:=DOMAIN(log_principal,D_principal[x])`, `r_taylor_x:=DOMAIN(log_taylor,D_taylor[x])`, `r_distinct_x:=EXACT(pairwise_disjoint(D_formal[x],D_principal[x],D_taylor[x]))`, `r_one_x:=EXACT(exactly_one_in_domain(r_formal_x.status,r_principal_x.status,r_taylor_x.status))`, and `r_bound_x:=EXACT(taylor_norm_bound(x))` | `P0 and r_enum.success and r_ids.success and (for every x in r_enum.items: r_formal_x.success and r_principal_x.success and r_taylor_x.success and r_distinct_x.success and r_one_x.success and r_bound_x.success)` |
| `C-B-V009-05` | STRUCTURAL | represented filtration, graded pieces, kernel quotient; zero/nonzero-symbol fixtures | `TYPE` quotient maps; `EXACT` filtration products and represented order | the quotient is well-defined and zero/nonzero fixtures receive their exact represented orders |
| `C-B-V009-06` | STRUCTURAL | principal-ruled sealed `stage_dependencies` encoding at `provenance/boundary_incidence_dynamics_preregistration_v011.json` bytes `[18898,19830)`; `STAGE_DEPENDENCIES_MEMBER_SHA256=47e7c32915bc756fb5f6be25c4fc6dec5c079c8837176dc62499e0f34f4c9d3b`; precedence decision `70c4080eae018bd644a3f0694557f1c0e854d621aa61097c775737887fec528f` | `r_ground:=COMPARE(P0.evidence_files[stage_dependencies_member].sha256,STAGE_DEPENDENCIES_MEMBER_SHA256,empty)`; `r_dag:=DAG(stage_dependencies,PRINCIPAL_SINGLE_AUTHORITY)` parses/types the node-parent lists and rejects cycles, self-parenting, and missing parents. By principal ruling, `stage_dependencies` is one sealed object serving as both graph and required-parent schema; the parent-comparison clause is discharged by that identity, never by synthesizing `COMPARE(X,X)` or duplicating the object as two independently authored arguments. | `P0 and r_ground.success and r_dag.success` |
| `C-B-V009-07` | STRUCTURAL | response configuration schema/manifest `(S_config,M_config)`; spec-pinned frozen digest `SPEC_CONFIG_SHA256`; finite mutation grammar/certificate `(G_config_mut,p_config_mut)`; expected mutation-ID ledger `E_config_mut`; spec-fixed mutation result `REJECTED` | `r_schema:=SCHEMA(S_config,M_config)`; `r_frozen:=COMPARE(content_root(M_config),SPEC_CONFIG_SHA256,empty)`; `r_enum:=ENUM(G_config_mut,p_config_mut)`; `r_ids:=COMPARE(r_enum.ids,E_config_mut.ids,empty)`; for every `m` in `r_enum.items`, `r_m:=EXACT(m(M_config))` and `r_cmp_m:=COMPARE(r_m.normal_form,REJECTED,empty)` | `P0 and r_schema.success and r_frozen.success and r_enum.success and r_ids.success and (for every m in r_enum.items: r_m.success and r_cmp_m.success)` |
| `C-B-V009-08` | STRUCTURAL | citation-to-claim graph; two-path and general-FS authority records | `TYPE` each entailment edge; `M2` general-FS claims | the general kinematic premise is separately pinned and no two-path result is promoted beyond its scope |
| `C-B-V009-09` | STRUCTURAL | charged-response expression; unit and dependency graphs | `UNITS` and `DAG` response dependencies; `EXACT` symbolic scale cancellation | the response is dimensionless, its scale cancels in four dimensions, and no favorable future interval is a parent |
| `C-B-V009-10` | STRUCTURAL | frozen rank-20 design; finite 20-basis grammar/certificate `(G_basis20,p_basis20)`; finite parity-branch grammar/certificate `(G_parity,p_parity)`; reconstruction graph `G_reconstruct`; pinned deterministic-reconstruction proof `p_deterministic_reconstruction`; expected reconstruction ledger `E_reconstruct`; topological-null fixture | `r_type:=TYPE(G_reconstruct)`; `r_basis:=ENUM(G_basis20,p_basis20)`; `r_parity:=ENUM(G_parity,p_parity)`; `r_basis_ids:=COMPARE(r_basis.ids,E_reconstruct.basis_ids,empty)`; `r_parity_ids:=COMPARE(r_parity.ids,E_reconstruct.parity_ids,empty)`; `r_det:=KERNEL(p_deterministic_reconstruction,proof_axioms)` with exact goal `deterministic_local_Maxwell_reconstruction(G_reconstruct,G_basis20,G_parity)`; `r_det_cmp:=COMPARE(r_det.conclusion,E_reconstruct.reconstruction_record,empty)`; for every `u` in `r_basis.items`, `r_u:=EXACT(reconstruct(u))` and `r_cmp_u:=COMPARE(r_u.normal_form,E_reconstruct[u],empty)`; for every `p` in `r_parity.items`, `r_p:=EXACT(reconstruct_branch(p))` and `r_cmp_p:=COMPARE(r_p.normal_form,E_reconstruct[p],empty)`; `r_null:=EXACT(reconstruct(T_top)=0)` | `P0 and r_type.success and r_basis.success and r_parity.success and r_basis_ids.success and r_parity_ids.success and r_det.success and r_det_cmp.success and r_null.success and (for every u in r_basis.items: r_u.success and r_cmp_u.success) and (for every p in r_parity.items: r_p.success and r_cmp_p.success)` |
| `C-B-V009-11` | STRUCTURAL | metric `eta`; orientation `epsilon`; Hodge generator/domain | `EXACT` generate the matrix; `DOMAIN` its carrier; check square, sign, and required commutator | the Hodge map is generated—not inserted—has the frozen domain, and satisfies every exact identity |
| `C-B-V009-12` | STRUCTURAL | phase-space premise; Legendre transform; units/sign conventions | `TYPE; UNITS; KERNEL` replay the Hamiltonian-to-action derivation | the action map and coefficient are unique under the pinned premise and no adjustable conversion survives |
| `C-B-V009-13` | STRUCTURAL | registry schema/manifest `(S_registry,M_registry)`; eligible-ID grammar/certificate `(G_eligible,p_eligible)`; selection proof `p_select`; finite contamination grammar/certificate `(G_contam,p_contam)`; expected selection/contamination-ID ledger `E_holdout`; spec-fixed contamination result `FAILS` | `r_schema:=SCHEMA(S_registry,M_registry)`; `r_eligible:=ENUM(G_eligible,p_eligible)`; `r_eligible_ids:=COMPARE(r_eligible.ids,M_registry.eligible_ids,empty)`; `r_select:=KERNEL(p_select,proof_axioms)`; `r_select_cmp:=COMPARE(r_select.conclusion,E_holdout.selection,empty)`; `r_contam:=ENUM(G_contam,p_contam)`; `r_contam_ids:=COMPARE(r_contam.ids,E_holdout.contamination_ids,empty)`; for every `m` in `r_contam.items`, `r_m:=EXACT(m(M_registry))` and `r_cmp_m:=COMPARE(r_m.normal_form,FAILS,empty)` | `P0 and r_schema.success and r_eligible.success and r_eligible_ids.success and r_select.success and r_select_cmp.success and r_contam.success and r_contam_ids.success and (for every m in r_contam.items: r_m.success and r_cmp_m.success)` |

## 4. V010 blocker-to-check map

| Check ID | Class | Content-addressed inputs beyond `BASE` | Ordered executable procedure | PASS iff |
|---|---|---|---|---|
| `C-B-V010-01` | **GATED-EXECUTION** | `FX-A35-01`; V010 response formula; declared symbolic-limit domain; finite post-hoc-multiplier mutation grammar and independent completeness certificate `(G_factor,p_factor)`; spec-fixed classification `REJECTED` | after the physical-evaluation gate: `r_response:=SYMBOLIC(V010_canonical_response)` with `ASSERTION_FREE_FORMATION(r_response)`; `r_domain:=DOMAIN(V010_canonical_response,D_limit)`; `r_enum:=ENUM(G_factor,p_factor)`; for every `m` in `r_enum.items`, `r_m:=SYMBOLIC(m(V010_canonical_response))` and `r_cmp_m:=COMPARE(r_m.classification,REJECTED,empty)` | `P0 and r_response.success and r_domain.success and r_enum.success and (for every m in r_enum.items: r_m.success and r_cmp_m.success)` |
| `C-B-V010-02` | STRUCTURAL | positive-`c` symbolic grammar/certificate `(G_c,p_c)`; closed controls schema/record `(S_c_controls,M_c_controls)`; controls proof `p_c_controls`; selector-status schema/record `(S_c_status,M_c_status)`; selector-status proof `p_c_status` with canonical `CARRIED_FAMILY` or `DERIVED_SELECTOR` goal; selector-parent graph; target query `q_target`; hard-coded-`c=1` rejection proof `p_c1_reject`; expected rejection record | `r_enum:=ENUM(G_c,p_c)`; `r_controls:=SCHEMA(S_c_controls,M_c_controls)`; `r_controls_proof:=KERNEL(p_c_controls,proof_axioms)`; `r_status:=SCHEMA(S_c_status,M_c_status)`; `r_status_proof:=KERNEL(p_c_status,proof_axioms)`; `r_parents:=DAG(G_c_selector_parents,P_c_selector)`; `r_target:=M2(q_target,{p_c_status,G_c_selector_parents})`; `r_mut_proof:=KERNEL(p_c1_reject,proof_axioms)`; `r_mut:=COMPARE(r_mut_proof.conclusion,expected_c1_rejection,empty)` | `P0 and r_enum.success and r_controls.success and r_controls_proof.success and r_status.success and r_status_proof.success and r_parents.success and r_target.success and r_target.hits=empty and r_mut_proof.success and r_mut.success` |
| `C-B-V010-03` | STRUCTURAL | positive-`tau` grammar `G_tau` and completeness certificate `p_tau`; closed controls schema/record `(S_tau_controls,M_tau_controls)`; proof `p_controls` that two named unequal symbolic controls lie in the enumerated family; closed selector-status schema/record `(S_selector_status,M_selector_status)`; typed status graph `G_selector_status`; proof `p_selector_status` with canonical goal `(status=CARRIED_FAMILY and selector=null) or (status=DERIVED_SELECTOR and selector in G_tau and least_positive_G_tau(selector) and nondegenerate(selector))`; actual/required parent graphs `(G_selector_parents,P_sel)`; target-value query `q_target`; content-addressed hard-coded-`tau=1` rejection proof `p_tau1_reject` and expected rejection record | `r_enum:=ENUM(G_tau,p_tau)`; `r_controls:=SCHEMA(S_tau_controls,M_tau_controls)`; `r_controls_proof:=KERNEL(p_controls,proof_axioms)`; `r_status:=SCHEMA(S_selector_status,M_selector_status)`; `r_type:=TYPE(G_selector_status)`; `r_status_proof:=KERNEL(p_selector_status,proof_axioms)`; `r_parents:=DAG(G_selector_parents,P_sel)`; `r_target:=M2(q_target,{p_selector_status,G_selector_parents})`; `r_mut_proof:=KERNEL(p_tau1_reject,proof_axioms)`; `r_mut:=COMPARE(r_mut_proof.conclusion,expected_rejection_record,empty)` | `P0 and r_enum.success and r_controls.success and r_controls_proof.success and r_status.success and r_type.success and r_status_proof.success and r_parents.success and r_target.success and r_target.hits=empty and r_mut_proof.success and r_mut.success` |
| `C-B-V010-04` | STRUCTURAL | primitive/Thomson type graph; complete-`Q_spec` dependency schema; `FX-A35-05` | `TYPE; DAG; M2` every `kappa_record`, `kappa_Thomson`, and alpha occurrence; apply alias mutation | primitive output cannot populate the Thomson/alpha field, the complete charged stage is a required parent, and the conflation fixture is rejected |
| `C-B-V010-05` | STRUCTURAL | tetrad, Jacobian, induced bivector/face measures; anisotropic symbolic fixtures | `EXACT; UNITS` transform every fixture | coordinate-shape factors cancel from the local coefficient without an inserted compensator and covariance holds for every sealed fixture |
| `C-B-V010-06` | STRUCTURAL | invariant-preparation grammar/certificate `(G_prep,p_prep)`; typed root-domain graph `G_root`; pinned target-independence derivation `p_domain` with expected conclusion `E_prep.domain`; proof-index manifest `P_competitor` assigning a decision proof and displayed-premise hashes to every enumerated candidate; expected candidate-ID/decision ledger `E_prep` | `r_enum:=ENUM(G_prep,p_prep)`; `r_type:=TYPE(G_root)`; `r_domain:=KERNEL(p_domain,proof_axioms)`; `r_domain_cmp:=COMPARE(r_domain.conclusion,E_prep.domain,empty)`; `r_candidate_ids:=COMPARE(r_enum.ids,P_competitor.ids,empty)`; `r_expected_ids:=COMPARE(r_enum.ids,E_prep.candidate_ids,empty)`; for every `c` in `r_enum.items`, `r_c:=KERNEL(P_competitor[c].decision_proof,proof_axioms)` and `r_c_cmp:=COMPARE({r_c.conclusion,r_c.used_axiom_hashes},E_prep[c],empty)` | `P0 and r_enum.success and r_type.success and r_domain.success and r_domain_cmp.success and r_candidate_ids.success and r_expected_ids.success and (for every c in r_enum.items: r_c.success and r_c_cmp.success)` |
| `C-B-V010-07` | STRUCTURAL | real sine/cosine modes; polarizations; Hermitian rows; finite-volume and complex-conversion tables | `EXACT` every Gram/design entry and conversion | the finite design is exactly normalized and real/complex reconstructions agree with no implicit volume factor |
| `C-B-V010-08` | STRUCTURAL | `T_top`, Frobenius metric, rank-20 quotient, candidate sections, pre-seal rank-21 fixture | `EXACT` norm/nullspace/orthogonality and quotient-section identities; run rank-21 mutation | nullity is exactly one with `F wedge F` generator, the section is unique, and revival of the rank-21 route fails |
| `C-B-V010-09` | STRUCTURAL | analytic theorem, neighborhood radius, remainder certificate; finite-ray impostor | `KERNEL` replay uniform theorem and bound; `DOMAIN` the full neighborhood | every direction in one certified neighborhood is covered with a remainder bound and a finite-ray-only proof fails |
| `C-B-V010-10` | STRUCTURAL | elementary-refinement grammar/certificate `(G_ref,p_ref)`; composite-path grammar/certificate `(G_comp,p_comp)`; common-refinement graph; generator/composite proof indexes `(P_ref,P_comp)`; closed status/scope record `(S_ref_status,M_ref_status)` with mode `UNIVERSAL_DERIVED` or `RESTRICTED_SCOPE`; universality-claim query `q_universal`; expected ID/scope ledger `E_ref` | `r_ref:=ENUM(G_ref,p_ref)`; `r_comp:=ENUM(G_comp,p_comp)`; `r_ref_ids:=COMPARE(r_ref.ids,P_ref.ids,empty)`; `r_comp_ids:=COMPARE(r_comp.ids,P_comp.ids,empty)`; `r_expected_ref:=COMPARE(r_ref.ids,E_ref.generator_ids,empty)`; `r_expected_comp:=COMPARE(r_comp.ids,E_ref.composite_ids,empty)`; for every `g` in `r_ref.items`, `r_g:=KERNEL(P_ref[g].commuting_square_proof,proof_axioms)`; for every `c` in `r_comp.items`, `r_c:=KERNEL(P_comp[c].composite_naturality_proof,proof_axioms)`; `r_status:=SCHEMA(S_ref_status,M_ref_status)`; `r_claims:=M2(q_universal,output_claim_sources)`; `r_branch:=EXACT((M_ref_status.mode=UNIVERSAL_DERIVED and every r_g.success and every r_c.success) or (M_ref_status.mode=RESTRICTED_SCOPE and M_ref_status.scope=E_ref.restricted_scope and r_claims.hits=empty))` | `P0 and r_ref.success and r_comp.success and r_ref_ids.success and r_comp_ids.success and r_expected_ref.success and r_expected_comp.success and r_status.success and r_claims.success and r_branch.success` |
| `C-B-V010-11` | STRUCTURAL | decorated-category schema and generator list | `TYPE` objects, first-opening subsets, labels, morphisms, identities, composition | every label is part of the typed object/morphism data and all functorial laws hold |
| `C-B-V010-12` | STRUCTURAL | report schemas; exact stage-parent requirements; alpha/core mutation | launch-spec only: `DAG` from report bytes, not statuses; mutate a parent and core alpha field | graph is acyclic, every parent is content-addressed, mutations fail closed, and core has no alpha map |
| `C-B-V010-13` | STRUCTURAL | closed registry/dedupe/commitment/beacon/eligibility schemas and manifests including `producer_principal`; exhaustive registry grammar/certificate `(G_registry,p_registry)`; typed custodian graph `G_custodian` including `principal`; pinned custodian-independence proof `p_independence`; selection proof `p_selection`; expected selection ledger `E_holdout`; contamination/drift grammar and independent completeness certificate `(G_failure,p_failure)`; spec-fixed failure classification `FAILS`; outcome-access query `q_outcome` | `r_registry:=ENUM(G_registry,p_registry)`; `r_schema:=SCHEMA(S_holdout,M_holdout)`; `r_custodian:=TYPE(G_custodian)`; `r_indep:=KERNEL(p_independence,proof_axioms)` with exact goal `G_custodian.principal != M_holdout.producer_principal`; `r_selection:=KERNEL(p_selection,proof_axioms)`; `r_selection_cmp:=COMPARE(r_selection.conclusion,E_holdout.selection,empty)`; `r_access:=M2(q_outcome,preseal_sources)`; `r_failure:=ENUM(G_failure,p_failure)`; for every `m` in `r_failure.items`, `r_m:=EXACT(m(M_holdout))` and `r_cmp_m:=COMPARE(r_m.normal_form,FAILS,empty)` | `P0 and r_registry.success and r_schema.success and r_custodian.success and r_indep.success and r_selection.success and r_selection_cmp.success and r_access.success and r_access.hits=empty and r_failure.success and (for every m in r_failure.items: r_m.success and r_cmp_m.success)` |
| `C-B-V010-14` | STRUCTURAL | claim graph; amplitude/action provenance; FS relation; pre-seal conversion mutations | `DAG`; `r_m2:=M2(q_silent_conversion,preseal_sources)`; `EXACT` Hessian check; inject factor-two/factor-four/later coefficient mutations | FS appears only downstream as a check on the physical amplitude’s Hessian; `r_m2.success and r_m2.hits=empty`; no `A^c`, multiplicity, or later conversion is selected |

## 5. V011 many-record blocker-to-check map

| Check ID | Class | Content-addressed inputs beyond `BASE` | Ordered executable procedure | PASS iff |
|---|---|---|---|---|
| `C-B-V011-MR-01` | STRUCTURAL | source/target monoidal categories and functor; closed target-source record `(S_target,M_target)` with mode `DERIVED` or `DISCLOSED_PREMISE`; proof `p_target_scope` of the derivation or exact premise-address/scope claim; coherence-diagram grammar/certificate `(G_coherence,p_coherence)`; proof index `P_coherence`; expected scope/diagram ledger `E_monoidal` | `r_type:=TYPE(G_monoidal)`; `r_target:=SCHEMA(S_target,M_target)`; `r_target_proof:=KERNEL(p_target_scope,proof_axioms)`; `r_target_cmp:=COMPARE(r_target_proof.conclusion,E_monoidal.target_scope,empty)`; `r_enum:=ENUM(G_coherence,p_coherence)`; `r_ids:=COMPARE(r_enum.ids,P_coherence.ids,empty)`; `r_expected_ids:=COMPARE(r_enum.ids,E_monoidal.diagram_ids,empty)`; for every `d` in `r_enum.items`, `r_d:=KERNEL(P_coherence[d].proof,proof_axioms)` and `r_cmp_d:=COMPARE(r_d.conclusion,E_monoidal[d],empty)` | `P0 and r_type.success and r_target.success and r_target_proof.success and r_target_cmp.success and r_enum.success and r_ids.success and r_expected_ids.success and (for every d in r_enum.items: r_d.success and r_cmp_d.success)` |
| `C-B-V011-MR-02` | STRUCTURAL | statistics grammar/certificate `(G_stats,p_stats)`; spec-fixed declaration `SPEC_STATS_MODE=RESOLVE`; one-record restriction functor; expected restriction ledger `E_stats`; closed selector-status record `(S_stats_status,M_stats_status)`; selector proof `p_stats_selector`; one-record-inference query `q_one_record_selector` | `r_enum:=ENUM(G_stats,p_stats)`; `r_ids:=COMPARE(r_enum.ids,E_stats.ids,empty)`; for every `s` in `r_enum.items`, `r_s:=EXACT(restrict_one_record(s))` and `r_cmp_s:=COMPARE(r_s.normal_form,E_stats[s],empty)`; `r_resolve:=EXACT(SPEC_STATS_MODE=RESOLVE and pairwise_distinct({r_s.normal_form : s in r_enum.items}))`; `r_status:=SCHEMA(S_stats_status,M_stats_status)`; `r_selector:=KERNEL(p_stats_selector,proof_axioms)`; `r_selector_cmp:=COMPARE(r_selector.conclusion,M_stats_status,empty)`; `r_query:=M2(q_one_record_selector,selector_sources)` | `P0 and r_enum.success and r_ids.success and r_resolve.success and r_status.success and r_selector.success and r_selector_cmp.success and r_query.success and r_query.hits=empty and (for every s in r_enum.items: r_s.success and r_cmp_s.success)` |
| `C-B-V011-MR-03` | STRUCTURAL | cell/span/pushout grammar; two- and three-cell fixtures | `TYPE` pushouts; `EXACT` shared-boundary descent and associativity | gluing is defined on overlaps, agrees on common faces, and is associative on the three-cell fixture |
| `C-B-V011-MR-04` | STRUCTURAL | `B_lambda` grammar; two distinct symbolic `lambda` controls; vacuum/one-record/higher-sector restrictions; content-addressed proof `p_high_distinct` with exact higher-sector-inequality goal; source/evidence set `S_claim`; fixed uniqueness query `q_unique`; closed claim-manifest schema `S_unique`; manifest `M_unique` mapping every claim ID/span to an independent completeness grammar/certificate; claim grammar `G_unique` and certificate `p_unique` | `r_low:=EXACT(B_lambda0\|_(vacuum+one)=B_lambda1\|_(vacuum+one))`; `r_high:=KERNEL(p_high_distinct,proof_axioms)` with goal `B_lambda0\|_higher != B_lambda1\|_higher`; `r_hits:=M2(q_unique,S_claim)`; `r_manifest:=SCHEMA(S_unique,M_unique)`; `r_enum:=ENUM(G_unique,p_unique)`; `r_match:=COMPARE(r_hits.hits,M_unique.claim_spans,empty)`; `r_claim_ids:=COMPARE(r_enum.ids,M_unique.claim_ids,empty)`; for every `c` in `r_enum.items`, `r_c:=KERNEL(M_unique[c].completeness_certificate,proof_axioms)` | `P0 and r_low.success and r_high.success and r_hits.success and r_manifest.success and r_enum.success and r_match.success and r_claim_ids.success and (for every c in r_enum.items: r_c.success)`; the last finite conjunction is true for the empty claim set |
| `C-B-V011-MR-05` | STRUCTURAL | evolution grammar/certificate `(G_evolution,p_evolution)`; commutator-sensitive overlap fixture; closed rule-source record `(S_rule,M_rule)` with `ADOPTED_PREMISE` or `DERIVED`; rule proof `p_rule`; expected coefficient/rule ledger `E_evolution` | `r_enum:=ENUM(G_evolution,p_evolution)`; `r_ids:=COMPARE(r_enum.ids,E_evolution.ids,empty)`; for every `e` in `r_enum.items`, `r_e:=EXACT(second_order_coefficients(e))` and `r_cmp_e:=COMPARE(r_e.normal_form,E_evolution[e],empty)`; `r_distinct:=EXACT(pairwise_distinct({r_e.normal_form : e in r_enum.items}))`; `r_source:=SCHEMA(S_rule,M_rule)`; `r_rule:=KERNEL(p_rule,proof_axioms)`; `r_rule_cmp:=COMPARE(r_rule.conclusion,E_evolution.rule_source,empty)`; `r_selected:=COMPARE(M_rule.rule_id,E_evolution.selected_rule_id,empty)` | `P0 and r_enum.success and r_ids.success and r_distinct.success and r_source.success and r_rule.success and r_rule_cmp.success and r_selected.success and (for every e in r_enum.items: r_e.success and r_cmp_e.success)` |
| `C-B-V011-MR-06` | STRUCTURAL | connected-preparation grammar/certificate `(G_prep,p_prep)`; expected preparation ledger `E_prep`; closed selector-status record `(S_prep_status,M_prep_status)` with `CARRIED_FAMILY` or `DERIVED_SELECTOR`; target-independent selector proof `p_prep_selector`; selector-parent graph `G_prep_parents`; one-record/target query `q_prep_target` | `r_enum:=ENUM(G_prep,p_prep)`; `r_ids:=COMPARE(r_enum.ids,E_prep.ids,empty)`; `r_status:=SCHEMA(S_prep_status,M_prep_status)`; `r_selector:=KERNEL(p_prep_selector,proof_axioms)`; `r_selector_cmp:=COMPARE(r_selector.conclusion,M_prep_status,empty)`; `r_parents:=DAG(G_prep_parents,P_prep_parents)`; `r_target:=M2(q_prep_target,{p_prep_selector,G_prep_parents})`; `r_member:=COMPARE({M_prep_status.status,M_prep_status.selector_id},E_prep.selector_status,empty)` | `P0 and r_enum.success and r_ids.success and r_status.success and r_selector.success and r_selector_cmp.success and r_parents.success and r_target.success and r_target.hits=empty and r_member.success` |
| `C-B-V011-MR-07` | **GATED-EXECUTION** | pinned zero-free-domain proof `p_zero_free`; pinned record-interval derivation `p_tau_R`; expected conclusion ledger `E_zero_free`; spec-fixed containment result `CONTAINED`; analytic response domain; regulator/cell fixture grammar/certificate `(G_fixture,p_fixture)` | after the interval/response gate: `r_zero:=KERNEL(p_zero_free,proof_axioms)`; `r_tau:=KERNEL(p_tau_R,proof_axioms)`; `r_zero_cmp:=COMPARE(r_zero.conclusion,E_zero_free.domain,empty)`; `r_tau_cmp:=COMPARE(r_tau.conclusion,E_zero_free.tau_R,empty)`; `r_domain:=DOMAIN(response,r_zero.conclusion)`; `r_enum:=ENUM(G_fixture,p_fixture)`; for every `f` in `r_enum.items`, `r_f:=SYMBOLIC(containment(r_tau.conclusion,r_zero.conclusion,f))` and `r_cmp_f:=COMPARE(r_f.result,CONTAINED,empty)` | `P0 and r_zero.success and r_tau.success and r_zero_cmp.success and r_tau_cmp.success and r_domain.success and r_enum.success and (for every f in r_enum.items: r_f.success and r_cmp_f.success)` |
| `C-B-V011-MR-08` | **GATED-EXECUTION** | `FX-A35-02`; root-survival expression; completed-record/CTP candidate schema | after the response gate: `SYMBOLIC` the survival amplitude at the recorded handle interval; `TYPE` replacement provenance | exact zero is reproduced, the object is rejected as a finite-log response subject, and no alternate amplitude is auto-selected merely to avoid zero |
| `C-B-V011-MR-09` | **GATED-EXECUTION** | handle and full-star projector graph `G_star`; pinned proof `p_full_star_access` with canonical disjunctive goal `derived_source_access or derived_complete_composite_handle`; expected access ledger `E_star`; spec-fixed one-handle result `INSUFFICIENT`; interval action | after the charged-access gate: `r_type:=TYPE(G_star)`; `r_proof:=KERNEL(p_full_star_access,proof_axioms)`; `r_proof_cmp:=COMPARE(r_proof.conclusion,E_star.access_conclusion,empty)`; `r_one:=EXACT(one_handle_action)`; `r_full:=EXACT(full_star_action)`; `r_one_cmp:=COMPARE(r_one.normal_form,INSUFFICIENT,empty)`; `r_full_cmp:=COMPARE(r_full.normal_form,E_star.full_star_action,empty)` | `P0 and r_type.success and r_proof.success and r_proof_cmp.success and r_one.success and r_full.success and r_one_cmp.success and r_full_cmp.success` |

## 6. V011 source-parent round-1 blocker-to-check map

| Check ID | Class | Content-addressed inputs beyond `BASE` | Ordered executable procedure | PASS iff |
|---|---|---|---|---|
| `C-B-V011-SP1-01` | STRUCTURAL | particle/antiparticle Cauchy carriers; hypersurface form; CAR/chirality maps | `TYPE; EXACT` positivity/nondegeneracy and CAR relations | both charge sectors and hypersurface inner product are typed and the chirality-label surrogate alone is rejected |
| `C-B-V011-SP1-02` | STRUCTURAL | boundary data; Lorentz representation; candidate-map grammar/certificate `(G_map,p_map)`; Lorentz-generator grammar/certificate `(G_Lor,p_Lor)`; selected-map derivation `p_selected_map`; expected selected-map/ID ledger `E_map`; spec-fixed `INTERTWINER_IDENTITY` | `r_maps:=ENUM(G_map,p_map)`; `r_lor:=ENUM(G_Lor,p_Lor)`; `r_map_ids:=COMPARE(r_maps.ids,E_map.candidate_ids,empty)`; `r_lor_ids:=COMPARE(r_lor.ids,E_map.generator_ids,empty)`; `r_selected:=KERNEL(p_selected_map,proof_axioms)`; `r_selected_cmp:=COMPARE(r_selected.conclusion,E_map.selected_map,empty)`; `r_type:=TYPE(E_map.selected_map)`; for every `g` in `r_lor.items`, `r_g:=EXACT(Lorentz_square(E_map.selected_map,g))` and `r_cmp_g:=COMPARE(r_g.normal_form,INTERTWINER_IDENTITY,empty)` | `P0 and r_maps.success and r_lor.success and r_map_ids.success and r_lor_ids.success and r_selected.success and r_selected_cmp.success and r_type.success and (for every g in r_lor.items: r_g.success and r_cmp_g.success)` |
| `C-B-V011-SP1-03` | STRUCTURAL | CPT antiunitary, carrier involutions, charge exchange, orientation action | `TYPE; EXACT` antiunitarity, square, Hamiltonian/incidence covariance, and charge exchange | every complete CPT equation holds on its stated carrier and the legacy incomplete surrogate fails |
| `C-B-V011-SP1-04` | **GATED-EXECUTION** | axial-phase grammar/certificate `(G_phase,p_phase)`; branch proof index `P_phase`; measure/anomaly/topology/CP inputs; expected branch ledger `E_phase`; closed resolution record `(S_phase_status,M_phase_status)` with `CLASSIFIED_ALL` or `RESPONSE_INDEPENDENT`; response-independence proof `p_response_independent`; phase-setting query `q_phase_set` | after anomaly/response authorization: `r_enum:=ENUM(G_phase,p_phase)`; `r_ids:=COMPARE(r_enum.ids,P_phase.ids,empty)`; `r_expected:=COMPARE(r_enum.ids,E_phase.ids,empty)`; for every `p` in `r_enum.items`, `r_spectral_p:=SPECTRAL(branch_terms(p))`, `r_kernel_p:=KERNEL(P_phase[p].classification_proof,proof_axioms)`, and `r_cmp_p:=COMPARE({r_spectral_p.result,r_kernel_p.conclusion},E_phase[p],empty)`; `r_status:=SCHEMA(S_phase_status,M_phase_status)`; `r_independent:=KERNEL(p_response_independent,proof_axioms)`; `r_independent_cmp:=COMPARE(r_independent.conclusion,E_phase.response_independence,empty)`; `r_no_set:=M2(q_phase_set,response_sources)`; `r_branch:=EXACT((M_phase_status.mode=CLASSIFIED_ALL and every r_spectral_p.success and every r_kernel_p.success and every r_cmp_p.success) or (M_phase_status.mode=RESPONSE_INDEPENDENT and r_independent.success and r_independent_cmp.success))` | `P0 and r_enum.success and r_ids.success and r_expected.success and r_status.success and r_no_set.success and r_no_set.hits=empty and r_branch.success` |
| `C-B-V011-SP1-05` | STRUCTURAL | source-incidence grammar and independent completeness certificate `(G_source_incidence,p_source_incidence)` covering positive metrics, intermediates, refinements, and covariant columns; typed candidate graphs; fixed pre-enumeration-selection query `q_selection_before_enum`; selection-source set `selection_sources` | `r_enum:=ENUM(G_source_incidence,p_source_incidence)`; `r_order:=M2(q_selection_before_enum,selection_sources)`; for every `c` in `r_enum.items`, `r_c:=TYPE(c)` | `P0 and r_enum.success and r_order.success and r_order.hits=empty and (for every c in r_enum.items: r_c.success)` |
| `C-B-V011-SP1-06` | STRUCTURAL | sealed current `j`; hypersurface charge `Q_Sigma`; charged projector `P_ch`; typed construction graph `G_jQP`; conservation proof `p_cons`; current-to-charge proof `p_charge` with goal `Q_Sigma=integral_Sigma star(j)` and slice independence; charge-to-projector proof `p_proj` with goal `P_ch=1_(R\{0})(Q_Sigma)`; declared spectral domain | `r_type:=TYPE(G_jQP)`; `r_cons:=KERNEL(p_cons,proof_axioms)`; `r_charge:=KERNEL(p_charge,proof_axioms)`; `r_proj:=KERNEL(p_proj,proof_axioms)`; `r_dom:=DOMAIN(1_(R\{0})(Q_Sigma),spec(Q_Sigma))`; `r_idem:=EXACT(P_ch^2=P_ch)`; `r_adj:=EXACT(P_ch^*=P_ch)`; `r_range:=EXACT(P_ch=1_(R\{0})(Q_Sigma))` | `P0 and r_type.success and r_cons.success and r_charge.success and r_proj.success and r_dom.success and r_idem.success and r_adj.success and r_range.success` |
| `C-B-V011-SP1-07` | STRUCTURAL | closed composition schema/manifest fixing one global source CAR and distinct even record factors; typed source/record/pushout graph; finite overlap/ordering derivation grammar/certificate `(G_overlap_order,p_complete)`; closed nonempty mandatory derivation-ID ledger `(S_SP1_07_expected,E_SP1_07)` containing shared-boundary descent, both three-cell parenthesizations, primitive shared-support overlap, and finite Stone ordering; proof-index manifest `P_SP1_07` mapping every mandatory ID to a pinned proof and expected conclusion | `r_schema:=SCHEMA(S_SP1_07,M_SP1_07)`; `r_type:=TYPE(G_SP1_07)`; `r_expected:=SCHEMA(S_SP1_07_expected,E_SP1_07)`; `r_enum:=ENUM(G_overlap_order,p_complete)`; `r_nonempty:=EXACT(cardinality(r_enum.ids)>0)`; `r_required_ids:=COMPARE(r_enum.ids,E_SP1_07.required_ids,empty)`; `r_proof_ids:=COMPARE(r_enum.ids,P_SP1_07.ids,empty)`; for every `d` in `r_enum.items`, `r_d:=KERNEL(P_SP1_07[d].proof,proof_axioms)` and `r_cmp_d:=COMPARE(r_d.conclusion,E_SP1_07[d],empty)`; `r_exact:=EXACT(graded_commutation_and_both_two_three_cell_pushout_parenthesizations)` | `P0 and r_schema.success and r_type.success and r_expected.success and r_enum.success and r_nonempty.success and r_required_ids.success and r_proof_ids.success and r_exact.success and (for every d in r_enum.items: r_d.success and r_cmp_d.success)` |
| `C-B-V011-SP1-08` | **GATED-EXECUTION** | closed state/CTP two-point schema/manifest `(S_2pt,M_2pt)`; derivation proof `p_2pt`; regulator and spectral domain; pole/threshold expected ledger `E_2pt`; mass-provenance graph | after the physical two-point gate: `r_schema:=SCHEMA(S_2pt,M_2pt)`; `r_proof:=KERNEL(p_2pt,proof_axioms)`; `r_proof_cmp:=COMPARE(r_proof.conclusion,E_2pt.two_point,empty)`; `r_spectral:=SPECTRAL(M_2pt)`; `r_class:=COMPARE(r_spectral.classification,E_2pt.classification,empty)`; `r_domain:=DOMAIN(M_2pt,D_state_CTP_regulator)`; `r_mass:=DAG(G_mass,P_mass)` | `P0 and r_schema.success and r_proof.success and r_proof_cmp.success and r_spectral.success and r_class.success and r_domain.success and r_mass.success` |
| `C-B-V011-SP1-09` | STRUCTURAL | independently implemented enumerator; SP1-01…08 admissible grammar/certificate `(G_SP1,p_SP1)`; closed reference-verdict schema/ledger `(S_SP1_verdict,E_SP1_verdict)`; producer verdict ledger | `r_enum:=ENUM(G_SP1,p_SP1)`; `r_expected:=SCHEMA(S_SP1_verdict,E_SP1_verdict)`; `r_ids:=COMPARE(r_enum.ids,E_SP1_verdict.ids,empty)`; `r_producer_ids:=COMPARE(r_enum.ids,producer_verdicts.ids,empty)`; `r_verdicts:=COMPARE(independent_verdicts,E_SP1_verdict.verdicts,process_local_mask)`; `r_cross:=COMPARE(independent_verdicts,producer_verdicts,process_local_mask)` | `P0 and r_enum.success and r_expected.success and r_ids.success and r_producer_ids.success and r_verdicts.success and r_cross.success` |

## 7. V011 source-parent round-2 blocker-to-check map

| Check ID | Class | Content-addressed inputs beyond `BASE` | Ordered executable procedure | PASS iff |
|---|---|---|---|---|
| `C-B-V011-SP2-01` | STRUCTURAL | standard CPT, normals, Lorentz maps, weighted adjoints, phase-nullspace matrix, neutral/charged controls | `TYPE; EXACT` CPT/normal pushforward/future reorientation/different-normal transport; exact nullspace and controls | every listed equation and both nonzero controls hold; the `gamma5`-only competitor fails |
| `C-B-V011-SP2-02` | STRUCTURAL | `b_partial`, `c_partial`, `Gamma_cell`; alias mutation | `TYPE; EXACT` both operators and their squares; compare byte/AST identities | `b_partial != c_partial`, their declared square relation holds, and the alias mutation fails |
| `C-B-V011-SP2-03` | **GATED-EXECUTION** | closed SP04 schema/manifest requiring separate `C`, `P`, `CP`, complete scalar/pseudoscalar grammar, axial map and Dirac domain, regulator, Fujikawa Jacobian, determinant ratio, boundary/eta, spectral-pairing output, zero-index branch, and index-one control; grammar/certificate; proof bundles `p_CP`, `p_pair`, `p_measure_sign`; gated spectral inputs; content-addressed expected-result schema/ledger `(S_expected_SP04,E_SP04)`; spec-fixed nonzero-index control `INDEX_ONE` | after anomaly authorization: `r_schema:=SCHEMA(S_SP04,M_SP04)`; `r_expected:=SCHEMA(S_expected_SP04,E_SP04)`; `r_type:=TYPE(G_C_P_CP)`; `r_enum:=ENUM(G_scalar_ps,p_complete)`; `r_domain:=DOMAIN(axial_map,D_Dirac)`; `r_kernel_CP:=KERNEL(p_CP,proof_axioms)`; `r_compare_CP:=COMPARE(r_kernel_CP.conclusion,E_SP04.expected_CP_relation,empty)`; `r_kernel_pair:=KERNEL(p_pair,proof_axioms)` with goal `DOMAIN(gamma5,D) and {D,gamma5}=0 and D psi=lambda psi => D(gamma5 psi)=-lambda(gamma5 psi)`; `r_kernel_measure_sign:=KERNEL(p_measure_sign,proof_axioms)` with exact zero-index measure/sign-equivalence goal; `r_spectral:=SPECTRAL(E_measure_and_index)`; `r_compare_pair:=COMPARE(r_spectral.pairing,r_kernel_pair.conclusion,empty)`; `r_compare_measure:=COMPARE(r_spectral.zero_index_measure_tuple,E_SP04.expected_zero_index_measure_tuple,empty)`; `r_compare_sign:=COMPARE(r_kernel_measure_sign.conclusion,E_SP04.expected_sign_equivalence,empty)`; `r_compare_control:=COMPARE(r_spectral.control,INDEX_ONE,empty)` | `P0 and r_schema.success and r_expected.success and r_type.success and r_enum.success and r_domain.success and r_kernel_CP.success and r_compare_CP.success and r_kernel_pair.success and r_kernel_measure_sign.success and r_spectral.success and r_compare_pair.success and r_compare_measure.success and r_compare_sign.success and r_compare_control.success` |
| `C-B-V011-SP2-04` | STRUCTURAL | multiplicity/Dirac factorization and commutant; complete control-superoperator grammar/certificate `(G_control,p_control)`; expected solution ledger `E_control`; rescaled-control grammar/certificate `(G_rescaled,p_rescaled)` | `r_type:=TYPE(G_factorization)`; `r_enum:=ENUM(G_control,p_control)`; `r_ids:=COMPARE(r_enum.ids,E_control.control_ids,empty)`; for every `c` in `r_enum.items`, `r_c:=EXACT({support,retraction,bimodule_covariance,affine_nullspace}(c))` and `r_cmp_c:=COMPARE(r_c.normal_form,E_control[c],empty)`; `r_unique:=COMPARE(E_control.solution_ids,{PBP},empty)`; `r_rescaled:=ENUM(G_rescaled,p_rescaled)`; for every `m` in `r_rescaled.items`, `r_m:=EXACT(m)` and `r_cmp_m:=COMPARE(r_m.normal_form,E_control.rescaled[m],empty)` | `P0 and r_type.success and r_enum.success and r_ids.success and r_unique.success and r_rescaled.success and (for every c in r_enum.items: r_c.success and r_cmp_c.success) and (for every m in r_rescaled.items: r_m.success and r_cmp_m.success)` |
| `C-B-V011-SP2-05` | STRUCTURAL | closed global-composition schema/manifest; typed one-global-CAR/distinct-even-record graph; finite cell-pushout grammar/certificate; finite full source-record-orientation grammar/certificate; proof-index manifests; pushout/relabeling/orientation proof bundle; SP17 one-cell object; primitive `h_K` and induced `h_K^2`; quartic fixture; content-addressed adopted quasi-free premise and rejection proof | `r_schema_global:=SCHEMA(S_global,M_global)`; `r_type:=TYPE(G_global)`; `r_enum_pushout:=ENUM(G_pushout,p_pushout_complete)`; `r_enum_orientation:=ENUM(G_orientation,p_orientation_complete)`; `r_compare_pushout_index:=COMPARE(r_enum_pushout.ids,p_pushout.index,empty)`; `r_compare_orientation_index:=COMPARE(r_enum_orientation.ids,p_orientation.index,empty)`; `r_kernel_covariance:=KERNEL(p_pushout_relabel_orientation,proof_axioms)` over every associativity/relabeling and source-record orientation-covariance square; `r_exact:=EXACT(SP17_restriction_and_primitive_overlap_vs_hK2_and_quartic_low_high_controls)`; `r_schema_premise:=SCHEMA(S_premise,premise_record)`; `r_kernel_quartic:=KERNEL(p_quartic_reject,quasi_free_axioms)`; `r_compare_axioms:=COMPARE(r_kernel_quartic.used_axiom_hashes,descriptor.allowed_axiom_hashes,empty)` | `P0 and r_schema_global.success and r_type.success and r_enum_pushout.success and r_enum_orientation.success and r_compare_pushout_index.success and r_compare_orientation_index.success and r_kernel_covariance.success and r_exact.success and r_schema_premise.success and r_kernel_quartic.success and r_compare_axioms.success` |
| `C-B-V011-SP2-06` | **GATED-EXECUTION** | closed SP08 schema/manifest requiring state/CTP, Lorentzian resolvent and `(+---)` signature, branch enum `{ISOLATED_POLE,INFRAPARTICLE_THRESHOLD}`, durability, absolute `T_R`, positive physical spectral measure, gauge/edge dressing, IR analysis, regulator family, and mass-subtraction family; content-addressed reality-factor schema/carrier `(S_reality,E_reality)` with named factor `rho_L`, carrier/domain `D_reality`, signature and resolvent hash; finite symbolic branch/regulator/subtraction grammars with certificates; content-addressed expected spectral schema/ledger `(S_expected_SP08,E_SP08)`; exact-goal proof bundles for reality/sign/classification, positive physical spectral measure, durability/`T_R`, dressing/IR/regulator independence, and exclusion of mass-shifting freedom | after physical-pole authorization: `r_schema:=SCHEMA(S_SP08,M_SP08)`; `r_reality:=SCHEMA(S_reality,E_reality)`; `r_expected:=SCHEMA(S_expected_SP08,E_SP08)`; `r_type:=TYPE(G_state_CTP_dressing)`; `r_domain:=DOMAIN(resolvent,D_CTP)`; `r_reality_domain:=DOMAIN(E_reality.rho_L,E_reality.D_reality)`; `r_units:=UNITS(signature_and_T_R)`; `r_enum_branch:=ENUM(G_branch,p_branch)`; `r_enum_reg:=ENUM(G_regulator_symbolic,p_reg)`; `r_enum_sub:=ENUM(G_subtraction_symbolic,p_sub)`; `r_spectral:=SPECTRAL({E_reality,E_interacting_support})`; `r_compare_class:=COMPARE(r_spectral.classification,E_SP08.classification,empty)`; `r_kernel_sign:=KERNEL(p_reality_sign_class,proof_axioms)`; `r_compare_sign:=COMPARE(r_kernel_sign.conclusion,E_SP08.expected_reality_sign_classification_record,empty)`; `r_kernel_positive:=KERNEL(p_measure_positive,proof_axioms)`; `r_compare_positive:=COMPARE(r_kernel_positive.conclusion,E_SP08.expected_positive_measure_record,empty)`; `r_compare_measure:=COMPARE(r_spectral.positive_measure_record,E_SP08.expected_positive_measure_record,empty)`; `r_kernel_durability_TR:=KERNEL(p_durability_TR,proof_axioms)`; `r_kernel_dressing_IR_reg:=KERNEL(p_dressing_IR_reg,proof_axioms)`; `r_kernel_no_mass_shift:=KERNEL(p_no_mass_shift,proof_axioms)`; `r_compare_sub_ids:=COMPARE(r_kernel_no_mass_shift.enumerated_ids,r_enum_sub.ids,empty)` | `P0 and r_schema.success and r_reality.success and r_expected.success and r_type.success and r_domain.success and r_reality_domain.success and r_units.success and r_enum_branch.success and r_enum_reg.success and r_enum_sub.success and r_spectral.success and r_compare_class.success and r_kernel_sign.success and r_compare_sign.success and r_kernel_positive.success and r_compare_positive.success and r_compare_measure.success and r_kernel_durability_TR.success and r_kernel_dressing_IR_reg.success and r_kernel_no_mass_shift.success and r_compare_sub_ids.success` |
| `C-B-V011-SP2-07` | STRUCTURAL | producer/verifier source sets; fixed Python-`assert` query `q_assert`; normal, real-`python -O`, and independent-verifier launch contracts/manifests; content-addressed isolated-runtime/trust manifests; declared comparison masks; child-receipt schema requiring `authority=false`; terminal-ledger schema; terminal-seal proof `p_terminal` and pinned trust-root axioms | `r_assert:=M2(q_assert,{producer_sources,verifier_sources})`; `r_normal:=RUNTIME(normal_contract)`; `r_opt:=RUNTIME(opt_contract)`; `r_verify:=RUNTIME(verifier_contract)`; `r_children:=COMPARE(normal_manifest,opt_manifest,child_mask)`; `r_verdicts:=COMPARE(producer_verdicts,verifier_verdicts,verdict_mask)`; `r_receipts:=SCHEMA(S_receipt,{normal_receipt,opt_receipt,verifier_receipt})`; `r_terminal:=SCHEMA(S_terminal,terminal_ledger)`; `r_seal:=KERNEL(p_terminal,trust_root_axioms)`; `r_seal_cmp:=COMPARE(r_seal.conclusion,terminal_ledger.expected_seal_record,empty)` | `P0 and r_assert.success and r_assert.hits=empty and r_normal.success and r_opt.success and r_verify.success and r_children.success and r_verdicts.success and r_receipts.success and r_terminal.success and r_seal.success and r_seal_cmp.success` |

## 8. A35-only discrepancy checks

[PART-PROVABLE] These three requirements are stated by A35 but are not
standalone numbered blockers in V003. They therefore receive their own check
IDs rather than being silently equated with a broader V003 row.

| Check ID | Class | Content-addressed inputs beyond `BASE` | Ordered executable procedure | PASS iff |
|---|---|---|---|---|
| `C-D-A35-01-ZERO-INDEX` | **GATED-EXECUTION** | zero-index Dirac/regulator fixture; Jacobian, determinant ratio, eta/boundary formulae; `FX-A35-06` nonzero-index control | after anomaly authorization: `SPECTRAL` the zero-index branch and nonzero-index control under identical domain rules | zero-index measure terms are evaluated and mutually consistent, while the nonzero-index control is detected and rejects false axial sign equivalence |
| `C-D-A35-02-QUASIFREE-CAR-LIFT` | STRUCTURAL | operator-valued one-source lift; CAR/even-record carrier; covariance maps; quartic control | `TYPE; EXACT` CAR relations, one-source restriction, functor covariance, and quartic higher-sector difference | the lift is genuinely operator-valued, agrees with the primitive one-source action, is covariant, and does not erase the quartic control |
| `C-D-A35-03-PHYSICAL-RESIDUE` | **GATED-EXECUTION** | physical state/CTP two-point schema/manifest `(S_residue,M_residue)`; branch grammar/certificate `(G_residue_branch,p_residue_branch)`; spectral projection; regulator/dressing domain; residue/threshold proof `p_residue`; expected ledger `E_residue`; spec-fixed finite-cell result `Z_NOT_SUFFICIENT` | after physical-pole authorization: `r_schema:=SCHEMA(S_residue,M_residue)`; `r_enum:=ENUM(G_residue_branch,p_residue_branch)`; `r_ids:=COMPARE(r_enum.ids,E_residue.branch_ids,empty)`; `r_domain:=DOMAIN(M_residue,D_state_CTP_regulator_dressing)`; `r_spectral:=SPECTRAL(M_residue)`; `r_proof:=KERNEL(p_residue,proof_axioms)`; `r_class:=COMPARE(r_spectral.classification,E_residue.classification,empty)`; `r_weight:=COMPARE(r_spectral.residue_or_threshold_weight,E_residue.weight,empty)`; `r_proof_cmp:=COMPARE(r_proof.conclusion,E_residue.positivity_covariance,empty)`; `r_z:=COMPARE(M_residue.finite_cell_z,Z_NOT_SUFFICIENT,empty)` | `P0 and r_schema.success and r_enum.success and r_ids.success and r_domain.success and r_spectral.success and r_proof.success and r_class.success and r_weight.success and r_proof_cmp.success and r_z.success` |

### 8.1 Completeness and class count

[PROVABLE] The check IDs form the disjoint union

```text
{C-B-V008-01..11}
⊔ {C-B-V009-01..13}
⊔ {C-B-V010-01..14}
⊔ {C-B-V011-MR-01..09}
⊔ {C-B-V011-SP1-01..09}
⊔ {C-B-V011-SP2-01..07}
⊔ {C-D-A35-01..03}.
```

The gated base rows are

```text
C-B-V010-01,
C-B-V011-MR-07, C-B-V011-MR-08, C-B-V011-MR-09,
C-B-V011-SP1-04, C-B-V011-SP1-08,
C-B-V011-SP2-03, C-B-V011-SP2-06.
```

The discrepancy rows add two gated checks and one structural check. Hence

```text
63 V003 checks = 55 STRUCTURAL + 8 GATED-EXECUTION
 3 A35 checks  =  1 STRUCTURAL + 2 GATED-EXECUTION
66 total       = 56 STRUCTURAL + 10 GATED-EXECUTION.
```

Each blocker has exactly one primary row. Shared routines may be reused by
hash, but they must emit a distinct verdict for every stable ID; semantic
deduplication cannot erase a ledger row.

### 8.2 G1 — sealed positive halves and the four commissioned re-renders

[PROVABLE] The hash-pinned blocker object
`BID_FULL_STACK_REVIEW_LEDGER_V003.md` (`c09f2c24…`) is cited here by
zero-based half-open **byte span**, not by unsealed-root line number. Every
line-number corroboration is to a manifest-native packet member pinned by
packet manifest `9d35f4ed…`.

#### `C-B-V011-SP1-07`

The positive half at blocker bytes `[20261,20408)` is:

> compose one global fermionic CAR source algebra with distinguishable
> record-cell factors and derive connected gluing, overlap, and ordering.

Packet `BID_SOURCE_PARENT_CLOSURE_GATE_V003.md` (`5c679e37…`) line 33 records
the one-global-CAR/distinct-even-record carrier and its pushout, covariance,
primitive-overlap, and quartic-completeness obligations. Packet
`BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md`
(`949181d7…`) lines 168–187 gives the executable list, including both
three-cell parenthesizations, both cell orders, orientation reversal,
primitive `h_K` versus induced `h_K^2`, the quartic control, and finite Stone
composition.

[YOURS] The V003 row removes the coverage/scope carve-out completely. Its
nonempty mandatory derivation-ID ledger is compared byte-exactly with both the
`ENUM(G_overlap_order,p_complete)` output and the proof index. Every enumerated
derivation is replayed by its own `KERNEL` call and compared with its expected
conclusion. The PASS conjunction therefore cannot succeed with zero derived
IDs or with any gluing, overlap, associativity, or ordering ID excused.

#### `C-B-V011-SP2-03`

The positive half at blocker bytes `[21592,22022)` is:

> construct C and P separately, compute the combined constraint on the full
> scalar/pseudoscalar family, and establish physical sign equivalence with a
> regulator whose Dirac domain is preserved by the axial map. The Fujikawa
> Jacobian, determinant ratio, boundary/eta contribution, and a nonzero-index
> control are mandatory.

Packet gate `5c679e37…` line 30 is the sealed corroborating pin: it records
separate combined C/P reduction, the closed-domain regulator, pairing derived
from chiral anticommutation, the zero-index Jacobian/determinant branch, and
the index-one control.

[YOURS] V002 uses `ENUM` for the complete scalar/pseudoscalar grammar,
`DOMAIN` for the axial map, separate `KERNEL` replays for CP, spectral pairing,
and the zero-index measure/sign relation, `SPECTRAL` for the gated measure
terms, and byte-exact `COMPARE` against the CP conclusion, pairing, expected
zero-index tuple, sign-equivalence conclusion, and index control. Closed
`SCHEMA` success—not the phrase `all terms are accounted`—requires every
measure slot.

#### `C-B-V011-SP2-05`

The positive half at blocker bytes `[22455,23038)` is:

> reconstruct the global carrier from explicit cell pushouts, test three-cell
> associativity, relabeling, and full source-record orientation covariance,
> recover the actual SP17 incidence zero-form on one cell, compute connected
> structure in the primitive operator itself, and keep induced `h_K^2`
> propagation distinct. A quartic competitor matching vacuum and one-source
> sectors remains mandatory.

Packet gate `5c679e37…` line 33 and packet global-boundary descent
`949181d7…` lines 168–187 are the sealed pins. In particular, the latter
requires orientation-reversal covariance, primitive-overlap separation, and
the quartic two-source discriminator.

[YOURS] V002 separately enumerates the pushout and **full source-record
orientation** grammars, compares both complete ID sets with the proof indexes,
replays every named covariance square with `KERNEL`, checks SP17/primitive/
`h_K^2`/quartic identities with `EXACT`, and pins the adopted quasi-free axiom
set. The undefined criterion `all structural laws hold` has been deleted.

#### `C-B-V011-SP2-06`

The positive half at blocker bytes `[23038,23527)` is:

> With signature `(+---)`, the Lorentzian reality factor and pole sign must be
> derived before use. Complete SP08 additionally requires the state/CTP
> prescription, durability and absolute `T_R`, positive physical spectral
> measure, gauge/edge dressing, infrared behavior, and absence of an adjustable
> mass subtraction.

Packet gate `5c679e37…` line 34 is the sealed current-scope pin. Packet
`BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md` (`6f6b822a…`)
lines 95–105 independently records that the free subgate establishes neither
durability nor the interacting gauge/IR pole-versus-threshold outcome.

[YOURS] V003 additionally names the content-addressed reality-factor carrier
`(S_reality,E_reality)`, its factor `rho_L`, and its declared carrier/domain
`D_reality`. `DOMAIN(E_reality.rho_L,E_reality.D_reality)` and
`SPECTRAL({E_reality,E_interacting_support})` consume that same pinned object;
the reality/sign/classification `KERNEL` conclusion is compared with the
expected record. The separate A35-only residue row is not collapsed into
SP2-06.

#### `C-B-V011-SP2-07`

The exact blocker at bytes `[23527,23774)` is:

> 7. Every load-bearing audit must be free of Python `assert`, agree under
>    normal and optimized execution, run under a content-addressed isolated
>    runtime, and pass a terminal seal. A sanitized but unsealed interpreter is
>    not final closure.

[YOURS] V003 restores that exact demand. `M2` must return an empty Python-assert
hit set; no proof may relabel a hit as non-load-bearing. The normal, optimized,
and independent-verifier runs each pass `RUNTIME`; their semantic outputs are
compared; the receipt and terminal ledgers pass closed schemas; and the terminal
seal is a pinned `KERNEL` replay whose conclusion is compared with the expected
seal record.

### 8.3 G2 — V005 BR-1/A adjudication board, all 66 rows

[YOURS] The board retains the exact 66-ID universe from §§3–8. `BOUND`,
`RE-RENDERED`, and `V004-REPAIRED` retain their prior scoped meanings;
`V005-REPAIRED` is one of the ten adjudicated-defective descriptor rows repaired
here. BR-1/A verdicts arise only from §8.6's displayed candidate/clause/receiver
record; BR-2 coverage is mechanical and displayed per row there. No descriptor
was executed, and no prior semantic claim is broadened.

| # | Check row | Binding disposition | Receiver or unbound item repaired |
|---:|---|---|---|
| 01 | `C-B-V008-01` | BOUND | closed carrier schema plus `TYPE` receives every arrow/composite atom |
| 02 | `C-B-V008-02` | BOUND | `TYPE` and `EXACT` receive identities, triples, associativity, and labels |
| 03 | `C-B-V008-03` | BOUND | the pinned proof is replayed by `KERNEL`; scale and sequential identities use `EXACT` |
| 04 | `C-B-V008-04` | BOUND | `TYPE` receives domains and `EXACT` receives both positive and negative laws |
| 05 | `C-B-V008-05` | BOUND | both holonomy alternatives are canonical `EXACT` normal forms |
| 06 | `C-B-V008-06` | BOUND | `M2`, `TYPE`, and `EXACT` receive premise disclosure and scope limitation |
| 07 | `C-B-V008-07` | BOUND | quotient and seams are received by `EXACT` and `TYPE` |
| 08 | `C-B-V008-08` | RE-RENDERED | right-inverse/minimum-norm proofs were bare; now pinned `KERNEL` conclusions are compared |
| 09 | `C-B-V008-09` | V005-REPAIRED | “without later choices” is forced per enumerated branch by spec-fixed `BRANCH_OUTCOME[b]` in `{ADMITTED,REJECTED}` |
| 10 | `C-B-V008-10` | BOUND | `DAG` and `M2` receive every stage, parent, and forbidden-core atom |
| 11 | `C-B-V008-11` | V005-REPAIRED | the forward-holdout contamination result is compared to spec-fixed `FAILS` |
| 12 | `C-B-V009-01` | BOUND | `TYPE` receives fiber inclusions and `M2` receives alias exclusion |
| 13 | `C-B-V009-02` | V005-REPAIRED | the dimensionful equivalence ID is required present and maps to spec-fixed `REJECTED_DIMENSIONFUL` |
| 14 | `C-B-V009-03` | BOUND | global/local typing and identities are received by `TYPE` and `EXACT` |
| 15 | `C-B-V009-04` | V004-REPAIRED | all three `DOMAIN.success` bits are conjoined; `EXACT` receives pairwise domain distinctness and exactly-one admitted dispatch |
| 16 | `C-B-V009-05` | BOUND | quotient typing and represented orders are exact opcode outputs |
| 17 | `C-B-V009-06` | BOUND | the literal parent graph is wholly received by `DAG` |
| 18 | `C-B-V009-07` | V005-REPAIRED | the frozen manifest is compared to `SPEC_CONFIG_SHA256`; every mutation targets spec-fixed `REJECTED` |
| 19 | `C-B-V009-08` | BOUND | premise scope is pinned in the entailment graph and enforced by `TYPE` plus `M2` |
| 20 | `C-B-V009-09` | BOUND | `UNITS`, `DAG`, and `EXACT` receive scale and parentage atoms |
| 21 | `C-B-V009-10` | V005-REPAIRED | pinned `r_det` carries deterministic local-Maxwell reconstruction; its conclusion is compared to `E_reconstruct` |
| 22 | `C-B-V009-11` | BOUND | generation, carrier, square, sign, and commutator are `EXACT`/`DOMAIN` outputs |
| 23 | `C-B-V009-12` | BOUND | the phase-space premise is consumed by the pinned `KERNEL` derivation |
| 24 | `C-B-V009-13` | V005-REPAIRED | contamination is fail-closed through spec-fixed `FAILS`; selection proof remains separately received |
| 25 | `C-B-V010-01` | V004-REPAIRED | every enumerated multiplier classification is compared to spec-fixed `REJECTED`; the base response reduction is explicitly assertion-free formation |
| 26 | `C-B-V010-02` | RE-RENDERED | selector premises were not a pinned proof and the symbolic family lacked explicit completeness binding |
| 27 | `C-B-V010-03` | BOUND | explicit `ENUM`, three `KERNEL` replays, `DAG`, `M2`, and `COMPARE` conjunction |
| 28 | `C-B-V010-04` | BOUND | type separation, parentage, occurrence search, and fixed mutation are opcode-received |
| 29 | `C-B-V010-05` | BOUND | sealed finite fixtures are consumed by `EXACT` and `UNITS` |
| 30 | `C-B-V010-06` | RE-RENDERED | target-independence had merely been typed; displayed premises and uniqueness proof were unbound |
| 31 | `C-B-V010-07` | BOUND | every carried finite table entry is an `EXACT` result |
| 32 | `C-B-V010-08` | BOUND | quotient identities and the fixed rank-21 mutation are `EXACT` results |
| 33 | `C-B-V010-09` | BOUND | theorem/remainder proof uses `KERNEL`; full-neighborhood scope uses `DOMAIN` |
| 34 | `C-B-V010-10` | RE-RENDERED | certified-composite reachability, proof indexing, and restricted-scope branch were unbound |
| 35 | `C-B-V010-11` | BOUND | all object/morphism/category laws are fields of the closed `TYPE` result |
| 36 | `C-B-V010-12` | BOUND | stage parents/cycles and the two fixed mutations are received by `DAG` |
| 37 | `C-B-V010-13` | V004-REPAIRED | pinned `KERNEL` receives producer/custodian inequality and every enumerated contamination/drift result is compared to spec-fixed `FAILS` |
| 38 | `C-B-V010-14` | V004-REPAIRED | the prior `silently inserted` atom now names `r_m2.success and r_m2.hits=empty` |
| 39 | `C-B-V011-MR-01` | RE-RENDERED | derived-or-disclosed target scope and coherence-proof completeness were not separately bound |
| 40 | `C-B-V011-MR-02` | V005-REPAIRED | the row declares the `RESOLVE` arm and `r_resolve` forces pairwise-distinct statistics normal forms |
| 41 | `C-B-V011-MR-03` | BOUND | pushout typing and two/three-cell descent identities are received by `TYPE`/`EXACT` |
| 42 | `C-B-V011-MR-04` | BOUND | claim hits, claim IDs, completeness certificates, and higher-sector proof are explicitly bound |
| 43 | `C-B-V011-MR-05` | V004-REPAIRED | `EXACT(pairwise_distinct(...))` receives the five-evolution distinctness atom; the rule proof/selection receivers carry |
| 44 | `C-B-V011-MR-06` | RE-RENDERED | target-independent selector proof and `silently selects` exclusion lacked receivers |
| 45 | `C-B-V011-MR-07` | V004-REPAIRED | both proofs replay through `KERNEL`; containment uses their conclusions and paired `SYMBOLIC`/`COMPARE(...,CONTAINED,...)` |
| 46 | `C-B-V011-MR-08` | BOUND | gated `SYMBOLIC` and `TYPE` results receive zero/rejection/provenance atoms |
| 47 | `C-B-V011-MR-09` | V005-REPAIRED | the separate one-handle clause is compared to spec-fixed `INSUFFICIENT`; access proof remains received |
| 48 | `C-B-V011-SP1-01` | BOUND | carrier, inner-product, CAR, and surrogate-rejection atoms are `TYPE`/`EXACT` results |
| 49 | `C-B-V011-SP1-02` | V004-REPAIRED | selected-map `KERNEL` carries derivation; every Lorentz square is compared to spec-fixed `INTERTWINER_IDENTITY` |
| 50 | `C-B-V011-SP1-03` | BOUND | the complete fixed CPT equation set is received by `TYPE`/`EXACT` |
| 51 | `C-B-V011-SP1-04` | RE-RENDERED | phase completeness, classification proofs, response-independence proof, and silent-set exclusion were unbound |
| 52 | `C-B-V011-SP1-05` | V004-REPAIRED | `r_enum.success` receives completeness; `r_order.hits=empty` receives selection-after-enumeration ordering; every candidate is typed |
| 53 | `C-B-V011-SP1-06` | BOUND | current, charge, and projector derivations are separate pinned `KERNEL` successes |
| 54 | `C-B-V011-SP1-07` | RE-RENDERED | unauthorized scope/coverage escape hatch removed; mandatory nonempty proof index now exhaustive |
| 55 | `C-B-V011-SP1-08` | RE-RENDERED | `complete` two-point construction and precedence had no proof/result comparison |
| 56 | `C-B-V011-SP1-09` | RE-RENDERED | exhaustive independent enumeration and producer/verifier comparisons were bare prose |
| 57 | `C-B-V011-SP2-01` | BOUND | the fixed equation/control set is received by `TYPE` and `EXACT` |
| 58 | `C-B-V011-SP2-02` | BOUND | operator distinction, squares, and alias mutation are `TYPE`/`EXACT` outputs |
| 59 | `C-B-V011-SP2-03` | V005-REPAIRED | the nonzero-index control is forced by spec-fixed `INDEX_ONE`; the other exact-goal proof receivers carry |
| 60 | `C-B-V011-SP2-04` | RE-RENDERED | full control-family completeness and uniqueness/rescaling comparisons were unbound |
| 61 | `C-B-V011-SP2-05` | BOUND | both complete grammars are compared with proof indexes and all proofs replay through `KERNEL` |
| 62 | `C-B-V011-SP2-06` | RE-RENDERED | the reality-factor carrier was unnamed and therefore not consumed by `DOMAIN`/`SPECTRAL` |
| 63 | `C-B-V011-SP2-07` | RE-RENDERED | non-load-bearing-assert exception weakened the exact blocker; zero hits are now mandatory |
| 64 | `C-D-A35-01-ZERO-INDEX` | BOUND | fixed zero/nonzero branches are received by gated `SPECTRAL` |
| 65 | `C-D-A35-02-QUASIFREE-CAR-LIFT` | BOUND | operator-valued CAR, covariance, restriction, and quartic atoms are `TYPE`/`EXACT` outputs |
| 66 | `C-D-A35-03-PHYSICAL-RESIDUE` | V005-REPAIRED | finite-cell `z` is compared to spec-fixed `Z_NOT_SUFFICIENT`; positivity/covariance proof receivers carry |

The mechanical totals are

```text
CARRIED BOUND = 35
CARRIED RE-RENDERED = 13
V004-REPAIRED = 8
V005-REPAIRED = 10
TOTAL = 66
```

[YOURS] BR-1/A's generator scans all 66 final descriptor rows and over-generates
the displayed candidate set; every candidate is adjudicated against a sealed
blocker clause in §8.6. BR-2's named mechanical procedure scans all 66 rows and
returns zero failures with per-row coverage displayed. No class assignment
changes.

### 8.4 G3 — consistency propagation

```text
numbered blocker IDs = 63
A35-only IDs         =  3
check descriptors    = 66
class partition      = 56 STRUCTURAL / 10 GATED-EXECUTION
fixture IDs          =  6
```

[YOURS] Exactly ten V004 descriptor rows change in V005: `C-B-V008-09`,
`C-B-V008-11`, `C-B-V009-02`, `C-B-V009-07`, `C-B-V009-10`,
`C-B-V009-13`, `C-B-V011-MR-02`, `C-B-V011-MR-09`,
`C-B-V011-SP2-03`, and `C-D-A35-03-PHYSICAL-RESIDUE`. Consequently the V005
specification hash, future `check_map_root`, and every future child/verifier
manifest and receipt that binds that root must change. No ID, class, fixture,
runtime pin, or aggregate conjunct changes.

[YOURS] The independent verifier's expected census is correspondingly:

```text
exact blocker IDs       = 63
exact discrepancy IDs   = 3
exact descriptor hashes = all 66 V005 descriptors, including the 10 V005 repairs
exact class partition   = 56/10
exact binding board     = 35 carried BOUND + 13 carried RE-RENDERED
                          + 8 V004-REPAIRED + 10 V005-REPAIRED
```

[PROVABLE] Q-559's census/firewall, Q-561's class/runner/runtime-pin verdicts,
Q-567's binding-class conviction, Q-574's closed V004 scope, and Q-580's BR-1/A
adjudication stand. V005 installs only the ruled regime and ten closed repairs;
it does not relitigate the protected determinations.

### 8.5 Closed V005 ten-row disposition

| # | Subject | Chosen exact repair from the adjudication column | Verification | Status |
|---:|---|---|---|---|
| 1 | `C-B-V008-09` | spec-fixed `BRANCH_OUTCOME[b]` in `{ADMITTED,REJECTED}` | `E_branch[b]` absent; every enumerated branch compares to the fixed map | REPAIRED |
| 2 | `C-B-V008-11` | compare each transition normal form to `FAILS` | `E_contam[m]` absent; result conjoined | REPAIRED |
| 3 | `C-B-V009-02` | spec-fixed `EQUIV_CLASS` map plus required dimensionful ID | `r_dim.success`; dimensionful ID maps to `REJECTED_DIMENSIONFUL` | REPAIRED |
| 4 | `C-B-V009-07` | compare manifest content root to `SPEC_CONFIG_SHA256`; mutations to `REJECTED` | expected freeze side is a spec pin; `E_config_mut[m]` absent | REPAIRED |
| 5 | `C-B-V009-10` | `r_det:=KERNEL(p_deterministic_reconstruction,...)` and compare its conclusion to `E_reconstruct` | exact deterministic goal; `r_det.success` and `r_det_cmp.success` conjoined; `r_null` retained | REPAIRED |
| 6 | `C-B-V009-13` | compare each contamination normal form to `FAILS` | `E_holdout[m]` absent; selection proof remains separate | REPAIRED |
| 7 | `C-B-V011-MR-02` | declare `SPEC_STATS_MODE=RESOLVE`; `r_resolve:=EXACT(...pairwise_distinct...)` | chosen arm is spec-forced and `r_resolve.success` is conjoined | REPAIRED |
| 8 | `C-B-V011-MR-09` | compare one-handle normal form to `INSUFFICIENT` | `E_star.one_handle_insufficient` absent; access proof retained | REPAIRED |
| 9 | `C-B-V011-SP2-03` | compare the spectral control to `INDEX_ONE` | producer control field absent from expected side; result conjoined | REPAIRED |
| 10 | `C-D-A35-03-PHYSICAL-RESIDUE` | compare finite-cell `z` to `Z_NOT_SUFFICIENT` | `E_residue.z_not_sufficient` absent; result conjoined | REPAIRED |

[PROVABLE] Descriptor-row diffing returns exactly those ten IDs. The six
adjudicated-lawful descriptor rows — `C-B-V008-08`, `C-B-V011-MR-04`,
`C-B-V011-MR-05`, `C-B-V011-SP1-08`, `C-B-V011-SP2-04`, and
`C-B-V011-SP2-06` — are byte-identical V004/V005. There is no deviation from an
adjudication-column option and no outside-list descriptor edit.

### 8.6 BR-1/A adjudication record and BR-2 mechanical coverage over final V005

Declared generator convention: all 66 descriptor rows are parsed as logical
Markdown rows; step 1 of the exact BR-1/A law is applied over the final
descriptor bytes with candidate multiplicity preserved per PASS atom. The set is
intentionally over-inclusive. Blocker clauses below are taken from the sealed
ledger `c09f2c24…`, not inferred from descriptor prose.

```text
DESCRIPTOR_ROWS_SCANNED = 66
CANDIDATE_ROWS = 12
CANDIDATE_ATOMS = 29
ZERO_CANDIDATE_ROWS = 54
REPAIRED_ZERO_CANDIDATE_ROWS = 4
ADJUDICATED_CANDIDATES = 29/29
DEFECTIVE_AFTER_REPAIR = 0
```

#### 8.6.1 Candidate set, clauses, receivers, and verdicts

| Candidate | Row and emitted atom | Sealed blocker clause carried by the field | Named receiver | Verdict |
|---|---|---|---|---|
| A01 | `V008-08:r_compare_right -> E_flux.right_inverse` | restrict the flux lift to `im(d1)` | `r_right:=KERNEL(...)`, plus `r_exact_im`/`r_domain` | LAWFUL (adjudication L1) |
| A02 | `V008-08:r_compare_min -> E_flux.minimum_norm` | same restriction/unique-lift clause | `r_min:=KERNEL(...)`, plus `r_exact_im`/`r_domain` | LAWFUL (L1) |
| A03 | `V008-08:r_out -> E_flux.outside_rejection` | outside-image control is subsidiary to the restriction demand | `r_exact_im` and `r_domain` carry the demand; `r_out` is only a control | LAWFUL (L1) |
| A04 | `V009-10:r_det_cmp -> E_reconstruct.reconstruction_record` | deterministic local-Maxwell reconstruction | `r_det:=KERNEL(p_deterministic_reconstruction,...)` | LAWFUL (V005 repair 5) |
| A05 | `V009-10:r_cmp_u -> E_reconstruct[u]` | deterministic per-basis reconstruction | `r_det` exact goal covers `G_basis20`; conclusion compared by `r_det_cmp` | LAWFUL (repair 5) |
| A06 | `V009-10:r_cmp_p -> E_reconstruct[p]` | deterministic per-parity reconstruction | `r_det` exact goal covers `G_parity`; `r_null` retained | LAWFUL (repair 5) |
| A07 | `V009-13:r_select_cmp -> E_holdout.selection` | selection from the eligible set | `r_select:=KERNEL(p_select,...)`; fail-closed clause separately uses `FAILS` | LAWFUL (repair 6) |
| A08 | `MR-02:r_cmp_s -> E_stats[s]` | resolve or carry the statistics family | declared `RESOLVE` arm and `r_resolve:=EXACT(pairwise_distinct(...))` | LAWFUL (repair 7) |
| A09 | `MR-02:r_selector_cmp -> M_stats_status` | no silent one-record selector | `r_selector:=KERNEL(...)` and `r_query.hits=empty` | LAWFUL (repair 7) |
| A10 | `MR-04:r_match -> M_unique.claim_spans` | detect higher-sector overlap invisible on vacuum/one-record sectors | `r_low:=EXACT(...)` and `r_high:=KERNEL(p_high_distinct,...)` | LAWFUL (adjudication L2) |
| A11 | `MR-05:r_cmp_e -> E_evolution[e]` | resolve the five evolution prescriptions | `r_distinct:=EXACT(pairwise_distinct(...))` | LAWFUL (L3) |
| A12 | `MR-05:r_rule_cmp -> E_evolution.rule_source` | exactly one adopted/derived rule provenance | `r_rule:=KERNEL(p_rule,...)` | LAWFUL (L3) |
| A13 | `MR-05:r_selected -> E_evolution.selected_rule_id` | the declared rule is the selected rule | `r_source:=SCHEMA(...)`, `r_rule`, and their conjoined comparisons | LAWFUL (L3) |
| A14 | `MR-09:r_proof_cmp -> E_star.access_conclusion` | derive charged access/full composite handle | `r_proof:=KERNEL(p_full_star_access,...)` | LAWFUL (repair 8) |
| A15 | `MR-09:r_full_cmp -> E_star.full_star_action` | complete full-star/composite-handle action | the same canonical disjunctive `r_proof` goal plus `r_full:=EXACT(...)`; insufficiency separately fixed | LAWFUL (repair 8) |
| A16 | `SP1-08:r_proof_cmp -> E_2pt.two_point` | derive a complete physical two-point function | `r_proof:=KERNEL(p_2pt,...)` | LAWFUL (L4) |
| A17 | `SP1-08:r_class -> E_2pt.classification` | assign mass meaning only after the derivation | `r_proof_cmp` carries derivation; `r_mass:=DAG(...)` carries ordering | LAWFUL (L4) |
| A18 | `SP2-03:r_compare_CP -> E_SP04.expected_CP_relation` | separate and account for CP relation | `r_kernel_CP:=KERNEL(p_CP,...)` | LAWFUL (repair 9) |
| A19 | `SP2-03:r_compare_measure -> E_SP04.expected_zero_index_measure_tuple` | exact zero-index measure/sign account | `r_kernel_measure_sign:=KERNEL(...)` exact goal | LAWFUL (repair 9) |
| A20 | `SP2-03:r_compare_sign -> E_SP04.expected_sign_equivalence` | exact sign-equivalence clause | `r_kernel_measure_sign`; nonzero control separately compares to `INDEX_ONE` | LAWFUL (repair 9) |
| A21 | `SP2-04:r_cmp_c -> E_control[c]` | solve the complete control family uniquely as `PBP` | `r_unique:=COMPARE(E_control.solution_ids,{PBP},empty)` | LAWFUL (L5) |
| A22 | `SP2-04:r_cmp_m -> E_control.rescaled[m]` | reject rescaled alternatives to unique `PBP` | the same spec-fixed `{PBP}` uniqueness receiver | LAWFUL (L5) |
| A23 | `SP2-06:r_compare_class -> E_SP08.classification` | derive Lorentzian pole/threshold status and sign | `r_kernel_sign:=KERNEL(...)` exact classification goal | LAWFUL (L6) |
| A24 | `SP2-06:r_compare_sign -> E_SP08.expected_reality_sign_classification_record` | same reality/sign/classification clause | `r_kernel_sign` and this conclusion comparison | LAWFUL (L6) |
| A25 | `SP2-06:r_compare_positive -> E_SP08.expected_positive_measure_record` | positive physical spectral measure | `r_kernel_positive:=KERNEL(...)` | LAWFUL (L6) |
| A26 | `SP2-06:r_compare_measure -> E_SP08.expected_positive_measure_record` | same positivity clause | `r_kernel_positive` conclusion comparison; spectral comparison is redundant | LAWFUL (L6) |
| A27 | `A35-03:r_class -> E_residue.classification` | derived pole/residue or threshold branch | `r_proof:=KERNEL(p_residue,...)` and complete `r_enum` | LAWFUL (repair 10) |
| A28 | `A35-03:r_weight -> E_residue.weight` | positive/covariant physical residue or threshold weight | `r_proof` exact goal and `r_proof_cmp` | LAWFUL (repair 10) |
| A29 | `A35-03:r_proof_cmp -> E_residue.positivity_covariance` | positivity and covariance | `r_proof:=KERNEL(p_residue,...)`; finite-`z` separately fixed to `Z_NOT_SUFFICIENT` | LAWFUL (repair 10) |

The four repaired rows that now generate zero candidates still receive the
required step-3 note:

| Row | Candidates | Sealed clause | Named receiver/adjudication note |
|---|---:|---|---|
| `C-B-V008-09` | 0 | executable without later choices | every branch compares to spec-fixed `BRANCH_OUTCOME[b]`; LAWFUL after repair |
| `C-B-V008-11` | 0 | genuinely forward external holdout | every contamination result compares to `FAILS`; LAWFUL after repair |
| `C-B-V009-02` | 0 | remove dimensionful-scale equivalence | `r_dim` requires the case and `EQUIV_CLASS` fixes `REJECTED_DIMENSIONFUL`; LAWFUL after repair |
| `C-B-V009-07` | 0 | freeze the configuration and sequence | content root compares to `SPEC_CONFIG_SHA256`; mutations compare to `REJECTED`; LAWFUL after repair |

#### 8.6.2 All-row coverage index and BR-2 mechanical transcript

`NC` means: **zero BR-1/A candidates; generator note only; no BR-1 clean verdict
is inferred for that row.** `Axx` and `Zx` point to the displayed adjudications
above. BR-2 `NONE` means the row has no `SYMBOLIC`/`SPECTRAL` assignment.

| # | Row | BR-1/A coverage | BR-2 per-row coverage |
|---:|---|---|---|
| 01 | `C-B-V008-01` | NC | NONE |
| 02 | `C-B-V008-02` | NC | NONE |
| 03 | `C-B-V008-03` | NC | NONE |
| 04 | `C-B-V008-04` | NC | NONE |
| 05 | `C-B-V008-05` | NC | NONE |
| 06 | `C-B-V008-06` | NC | NONE |
| 07 | `C-B-V008-07` | NC | NONE |
| 08 | `C-B-V008-08` | A01–A03 | NONE |
| 09 | `C-B-V008-09` | Z1 (0 candidates; receiver named) | NONE |
| 10 | `C-B-V008-10` | NC | NONE |
| 11 | `C-B-V008-11` | Z2 (0 candidates; receiver named) | NONE |
| 12 | `C-B-V009-01` | NC | NONE |
| 13 | `C-B-V009-02` | Z3 (0 candidates; receiver named) | NONE |
| 14 | `C-B-V009-03` | NC | NONE |
| 15 | `C-B-V009-04` | NC | NONE |
| 16 | `C-B-V009-05` | NC | NONE |
| 17 | `C-B-V009-06` | NC | NONE |
| 18 | `C-B-V009-07` | Z4 (0 candidates; receiver named) | NONE |
| 19 | `C-B-V009-08` | NC | NONE |
| 20 | `C-B-V009-09` | NC | NONE |
| 21 | `C-B-V009-10` | A04–A06 | NONE |
| 22 | `C-B-V009-11` | NC | NONE |
| 23 | `C-B-V009-12` | NC | NONE |
| 24 | `C-B-V009-13` | A07 | NONE |
| 25 | `C-B-V010-01` | NC | `r_response` formation-only; `r_m -> r_cmp_m(REJECTED)`; PASS |
| 26 | `C-B-V010-02` | NC | NONE |
| 27 | `C-B-V010-03` | NC | NONE |
| 28 | `C-B-V010-04` | NC | NONE |
| 29 | `C-B-V010-05` | NC | NONE |
| 30 | `C-B-V010-06` | NC | NONE |
| 31 | `C-B-V010-07` | NC | NONE |
| 32 | `C-B-V010-08` | NC | NONE |
| 33 | `C-B-V010-09` | NC | NONE |
| 34 | `C-B-V010-10` | NC | NONE |
| 35 | `C-B-V010-11` | NC | NONE |
| 36 | `C-B-V010-12` | NC | NONE |
| 37 | `C-B-V010-13` | NC | NONE |
| 38 | `C-B-V010-14` | NC | NONE |
| 39 | `C-B-V011-MR-01` | NC | NONE |
| 40 | `C-B-V011-MR-02` | A08–A09 | NONE |
| 41 | `C-B-V011-MR-03` | NC | NONE |
| 42 | `C-B-V011-MR-04` | A10 | NONE |
| 43 | `C-B-V011-MR-05` | A11–A13 | NONE |
| 44 | `C-B-V011-MR-06` | NC | NONE |
| 45 | `C-B-V011-MR-07` | NC | `r_f -> r_cmp_f(CONTAINED)`; PASS |
| 46 | `C-B-V011-MR-08` | NC | NONE |
| 47 | `C-B-V011-MR-09` | A14–A15 | NONE |
| 48 | `C-B-V011-SP1-01` | NC | NONE |
| 49 | `C-B-V011-SP1-02` | NC | NONE |
| 50 | `C-B-V011-SP1-03` | NC | NONE |
| 51 | `C-B-V011-SP1-04` | NC | `r_spectral_p -> r_cmp_p/r_branch`; PASS |
| 52 | `C-B-V011-SP1-05` | NC | NONE |
| 53 | `C-B-V011-SP1-06` | NC | NONE |
| 54 | `C-B-V011-SP1-07` | NC | NONE |
| 55 | `C-B-V011-SP1-08` | A16–A17 | `r_spectral -> r_class`; PASS |
| 56 | `C-B-V011-SP1-09` | NC | NONE |
| 57 | `C-B-V011-SP2-01` | NC | NONE |
| 58 | `C-B-V011-SP2-02` | NC | NONE |
| 59 | `C-B-V011-SP2-03` | A18–A20 | `r_spectral -> r_compare_pair/r_compare_measure/r_compare_control(INDEX_ONE)`; PASS |
| 60 | `C-B-V011-SP2-04` | A21–A22 | NONE |
| 61 | `C-B-V011-SP2-05` | NC | NONE |
| 62 | `C-B-V011-SP2-06` | A23–A26 | `r_spectral -> r_compare_class/r_compare_measure`; PASS |
| 63 | `C-B-V011-SP2-07` | NC | NONE |
| 64 | `C-D-A35-01-ZERO-INDEX` | NC | NONE |
| 65 | `C-D-A35-02-QUASIFREE-CAR-LIFT` | NC | NONE |
| 66 | `C-D-A35-03-PHYSICAL-RESIDUE` | A27–A29 | `r_spectral -> r_class/r_weight`; PASS |

```text
BR2_DESCRIPTOR_ROWS_SCANNED = 66
BR2_ROWS_WITH_REDUCTIONS = 7
BR2_ROWS_WITHOUT_REDUCTIONS = 59
BR2_REDUCTION_ASSIGNMENTS = 8
BR2_FAILURES = []
BR2_SWEEP = 0 failures
```

[PROVABLE] The BR-1/A record is adjudicated, not called a zero-failure sweep.
The BR-2 record is mechanical source-language coverage. Neither executes a
descriptor or asserts a physical relation true.

## 9. S3 — runner architecture

### 9.1 Runtime-subject determination

[PART-PROVABLE] SP14 says “against runtime v012.” The sealed runtime objects do
not make that phrase a unique content hash:

```text
runtime_snapshot_v012
  sha256 = 50a6fc141a45451678aa7543e4f267ce26beb6e53182170b478acb6fb0e0f5bb
  schema = gravacle.content-addressed-runtime.v012
  gate   = primitive_step6_content_addressed_runtime_gate_v010.md
  gate_sha256 = 2ad7f72a88184c11e1253f2c47598fca11e60d05e8e71a26db4e19b16bf98d42

logical_gate_v012
  sha256 = 34faecbfc0f0a741fbd93ed2698b7ba5a1f3262d4b7cb83c37a375c3c3abe63b

runtime_snapshot_v014
  sha256 = fb74b7566b5c7ae8da64096754b16570dc613c8afdd140abd7a0100d5fcc1a08
  schema = gravacle.content-addressed-runtime.v014
  gate   = logical_gate_v012
  gate_sha256 = 34faecbfc0f0a741fbd93ed2698b7ba5a1f3262d4b7cb83c37a375c3c3abe63b.
```

[YOURS] The implementation manifest must contain exactly one principal- or
review-authorized `runtime_subject={snapshot_sha256,gate_sha256,trust_root}`.
Absent that unique content pin, the parent returns
`FAIL(RUNTIME_SUBJECT_AMBIGUOUS)` before launching a child. This specification
follows SP14’s wording and does **not** silently replace v012 by v014.

The ambiguity does not prevent architectural specification; it prevents an
implementation from choosing its runtime by name or convenience.

### 9.2 Custody separation

[YOURS] The custody graph is mandatory:

```text
Lane 3                 writes this specification only
Dario                   cross-family reviews the specification
Builder A               implements producer/check executor and fresh parent
Builder B               independently implements verifier
Custodian C             authored neither A nor B and invokes the parent
Principal               issues the content-addressed RD-22 authorization
Signature custodian     signs only after the validated fresh chain exits
```

Builder B may share only the sealed schemas, this specification, immutable
inputs, and output contracts with Builder A. B may not import A’s check
functions, expected-verdict generator, comparison function, or mutable receipt.
Custodian C may not patch code, manifests, fixtures, or expected results.
Neither builder, child, parent, verifier, nor signature infers authorization.

### 9.3 Architecture state machine

[PROVABLE] Items marked “SP14/v012” below are demanded by the sealed runner
stock. Exact manifest and field names are [YOURS].

#### State `R0` — fresh direct parent preflight

The parent is invoked as a direct script by the uniquely pinned CPython with
`-I -S -B`, no `-c`, no `-m`, and no undeclared `PYTHONPATH`, `PYTHONHOME`,
startup/inspect, `DYLD_*`, or `LD_*` influence. It must establish:

```text
output_path_absent
and receipt_path_absent
and verifier_output_path_absent
and pycache_root_exists_and_is_empty
and parent_source_contains_no_load_bearing_assert
and all_input_hashes_match
and runtime_subject_is_unique
and authorization.rd22_hash_is_present_and_valid
```

Every condition is an explicit fail-closed branch and nonzero exit; Python
`assert` is never load-bearing. The parent hashes its own exact compiled byte
buffer, both producer/verifier sources, launchers, manifests, this check map,
the 66 descriptors, fixtures, subject lineage, runtime, schemas, and proof
axioms before any child receives control.

#### State `R1` — immutable manifests

The parent accepts distinct closed manifests for normal, optimized, and
verifier children. Each manifest contains:

```text
exact file -> {byte_length,sha256} inventory
subject_lineage_root
specification_sha256
check_map_root and exact check-ID set
fixture_manifest_root and exact fixture-ID set
runtime_subject and trust_root
expected output and receipt paths (which must not exist)
optimization level: 0, 1, or verifier-declared
exact allowed input/read/write/event inventories
exact output schema and authority firewall
```

Changing one byte changes the manifest root and invalidates the run.

#### State `R2` — trust snapshot `T0`

Immediately before the normal child, the parent reads the mutable macOS trust
tuple

```text
T0 = {machine, platform, sw_vers, SIP_status, disclosed_policy_fields}
```

and requires exact equality with the authorized runtime trust root. System
images under `/System/Library`, `/usr/lib`, and the dyld shared cache are
carried only under this disclosed/revalidated trust base. Every non-system
native image is individually content-addressed.

#### State `R3` — normal producer child

The normal child is a fresh process using the normal manifest and
`sys.flags.optimize=0`. It has a cleared environment, source-only imports, an
empty isolated pycache root, no network or process creation, and no filesystem
mutation except exclusive creation of its declared output and child receipt.
Its audit hook records all module loads, loader transactions, native images,
open events, process/network events, environment changes, and writes.

The sole environment exception is the exact ordered four-event BLAS sequence:

```text
set OPENBLAS_MAIN_FREE=1
set GOTOBLAS_MAIN_FREE=1
remove OPENBLAS_MAIN_FREE
remove GOTOBLAS_MAIN_FREE.
```

Any missing, extra, reordered, or changed event fails. The C-process
environment must be empty before numerical imports and after target return.

#### State `R4` — trust snapshot `T1`

Immediately after the normal child, the parent rereads the full trust tuple and
requires `T1=T0=authorized_trust_root`. Drift terminates the chain.

#### State `R5` — optimized producer child

The optimized child is a second fresh process with the same source bytes,
subject root, check map, fixtures, and output contract, but a separate manifest,
separate writable paths, a real `-O`, and `sys.flags.optimize=1`. It may share
no writable state with the normal child. Its runtime/event contract is
otherwise identical.

#### State `R6` — trust snapshot `T2`

Immediately after the optimized child, the parent requires
`T2=T1=T0=authorized_trust_root`.

#### State `R7` — parent-side reclassification

The parent does not trust child labels. From the raw ledgers it independently:

1. rehashes every loaded Python source and non-system native image;
2. reclassifies every module, native image, open event, process/network event,
   environment mutation, and write against the sealed allowlist;
3. verifies the baseline module identities and every loader transaction;
4. rejects `.pyc`, unsealed reads, device reads, undeclared writes, unknown or
   originless modules, and runtime/source drift;
5. applies only the sealed causal alias exceptions for live-reconstructed
   builtin or sealed-parent aliases; names or mutable metadata alone never
   suffice; and
6. rehashes runtime trees, sources, manifests, outputs, and receipts after
   each child.

Child receipts are evidence. They are never terminal authority and never
supply expected row counts or verdicts.

#### State `R8` — producer comparison

`COMPARE(normal,optimized,mask)` may mask only the predeclared process-local
fields `process_id`, `monotonic_duration`, and `python_optimize`. It requires
exact equality of:

```text
all 66 check IDs and per-row statuses
all evidence hashes and pass predicates
all six fixture verdicts
execution classes and gate states
blocker/check/fixture counts
input and procedure hashes
scope and authority-firewall fields.
```

One-branch success is not merged. A missing/malformed row or any semantic
difference terminates the chain.

#### State `R9` — independent verifier child

After a fresh before-verifier trust snapshot `T3`, the parent launches Builder
B’s verifier as a third isolated child. The verifier obtains the immutable
inputs independently and does not import producer code. It independently:

```text
rehashes every input and exact compiled source buffer;
strict-parses all manifests, outputs, and receipts;
checks the exact 63 blocker IDs plus 3 discrepancy IDs, all 66 V005 descriptor
  hashes, the 56/10 class partition, and the 35 carried BOUND + 13 carried
  RE-RENDERED + 8 V004-REPAIRED + 10 V005-REPAIRED specification binding
  board;
replays each pass predicate from evidence bytes;
replays every fixture’s expected result;
reclassifies runtime/module/native/open/process/network/mutation events;
revalidates before/after trust records;
compares normal and optimized semantic outputs;
checks the authorization hash and gate discipline;
checks all authority-firewall fields are false unless separately authorized.
```

The parent rereads trust immediately after the verifier and requires
`T4=T3=T2=T1=T0=authorized_trust_root`.

#### State `R10` — terminal ledger and local assurance

The parent validates the verifier’s exact output inventory itself. Any child
or verifier failure, malformed/missing/duplicate field, trust drift, hash
mismatch, class mismatch, unauthorized gated execution, or receipt promotion
returns terminal FAIL.

Only after the complete fresh chain exits successfully may the signature
custodian detached-sign the canonical machine-readable verdict ledger and its
protocol SHA-256 sidecar. The signature means reproducible local assurance. It
does not mean remote attestation, physics validity, `SPEC-SEAL`,
`CORE-RESULT-SEAL`, `FINAL-CLAIM-SEAL`, alpha computation, or proof authority.

### 9.4 Machine-readable verdict ledger

[YOURS] The output is canonical UTF-8 JSON with sorted keys, no insignificant
whitespace, duplicate keys, `NaN`, infinity, or undeclared fields. The exact
top-level field inventory is:

```text
{
  schema,
  spec_sha256,
  runner_sha256,
  verifier_sha256,
  runtime_subject,
  authorization,
  subject_lineage,
  check_map_sha256,
  fixture_manifest_sha256,
  children,
  trust_snapshots,
  checks,
  fixtures,
  producer_comparison,
  summary,
  scope,
  authority_firewall,
  terminal_content_sha256
}
```

Each `checks[]` row has exactly:

```text
{
  blocker_id,
  source:{path,sha256,byte_span},
  check_id,
  check_spec_sha256,
  execution_class,
  input_root_sha256,
  deterministic_procedure,
  prerequisites,
  required_gate,
  expected_predicate,
  invocation,                   # null, or the recorded consumed-argument invocation carrying byte-span linkage
  procedure_started,
  status,                       # PASS|FAIL|NOT_RUN_GATE|ERROR
  observed_evidence_sha256s,
  reason
}
```

For a row that consumes structured evidence, `invocation` is the producer's
recorded closed object

```text
{opcode, result_name, args, instance_id,
 source_sha256, span:[start,end], span_sha256}
```

where `instance_id` names the same grounding source and half-open byte span and
`span_sha256` is the digest of exactly those source bytes. Rows that do not
consume structured evidence carry `invocation:null`. This is the byte-span
linkage required for independent replay; the blocker-ledger `source.byte_span`
and a digest without the source slice are not substitutes for it.

Each child row has exactly:

```text
{
  manifest_sha256,
  target_sha256,
  optimize,
  output_sha256,
  receipt_sha256,
  runtime_before_sha256,
  runtime_after_sha256,
  module_ledger_sha256,
  native_ledger_sha256,
  open_event_ledger_sha256,
  receipt_authoritative:false
}
```

The specification-time authority firewall is exact:

```text
implemented = false
executed = false
authorization_claimed = false
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
SPEC_SEAL = false
CORE_RESULT_SEAL = false
FINAL_CLAIM_SEAL = false.
```

A future authorized run may truthfully change only fields licensed by its
principal authorization. It cannot infer any seal or physics authority from a
runner PASS.

### 9.5 Aggregate decision rule

[YOURS] After all required physical gates separately open, A35’s executable
row could return PASS only if

```text
all 66 check rows = PASS
and all 6 fixture rows = expected verdict
and normal_semantics = optimized_semantics
and independent_verifier = PASS
and parent_reclassification = PASS
and trust_chain_intact
and input/output roots match
and authorization valid
and terminal local-assurance seal verifies.
```

Before those gates open, every affected row is `NOT_RUN_GATE`; therefore the
aggregate cannot be PASS. This specification does not instantiate that rule.

## 10. S4 — mandatory regression fixtures

[PROVABLE] The six named behaviors are demanded by A35/V003. Fixture names and
closed output fields are [YOURS]. Every fixture is content-addressed in a
separate manifest and quarantined under `fixtures[]`; no fixture output may
populate a live physical-output field.

| Fixture ID | Primary checks | Class when run | Frozen input mutation/control | Expected verdict fields |
|---|---|---|---|---|
| `FX-A35-01-V010-ZERO-STIFFNESS` | `C-B-V010-01` | GATED-EXECUTION | Immutable V010 direct-sum global-ray route; canonical mode; post-hoc `L^2`, `L^4`, and volume mutations | `competitor_reproduced=true`; `physical_response_accepted=false`; `after_the_fact_factor_accepted=false` |
| `FX-A35-02-ROOT-SURVIVAL-ZERO` | `C-B-V011-MR-08` | GATED-EXECUTION | Recorded root-survival subject at the handle interval plus an auto-substitution mutation | `zero_reproduced=true`; `response_subject_accepted=false`; `alternate_amplitude_auto_selected=false` |
| `FX-A35-03-C-FAMILY` | `C-B-V010-02` | STRUCTURAL | Symbolic family `Gamma_c=-c log\|A\|`, `c>0`, including two unequal controls | `family_admitted=true`; `c_equals_one_selected=false` |
| `FX-A35-04-TAU-FAMILY` | `C-B-V010-03` | STRUCTURAL | Symbolic family `exp(-i tau B)`, `tau>0`, including two unequal controls | `family_admitted=true`; `tau_equals_one_derived=false` |
| `FX-A35-05-PRIMITIVE-THOMSON-CONFLATION` | `C-B-V010-04` | STRUCTURAL | Mutation routing primitive `kappa_record` into a Thomson/alpha field | `type_violation_detected=true`; `competitor_accepted=false`; primitive and Thomson fields remain distinct |
| `FX-A35-06-NONZERO-INDEX-CONTROL` | `C-B-V011-SP1-04`, `C-B-V011-SP2-03`, `C-D-A35-01-ZERO-INDEX` | GATED-EXECUTION | Index-one/unpaired-zero-mode control; rephasing and hand-inserted-pairing mutations | `axial_sign_equivalence=false`; `control_rejected=true`; both mutations fail |

[PROVABLE] The three structural fixture source rows migrate to these V007
zero-based half-open byte spans; each generated fixture-manifest row must use
the matching V007 path and final V007 SHA-256:

| Fixture ID | V007 source byte span |
|---|---|
| source row for `FX-A35-03-C-FAMILY` | `[129056,129245)` |
| source row for `FX-A35-04-TAU-FAMILY` | `[129245,129433)` |
| source row for `FX-A35-05-PRIMITIVE-THOMSON-CONFLATION` | `[129433,129686)` |

Expected outcomes come from the immutable rejection obligations, not from any
desired numerical consequence. A fixture descriptor can be hashed now; its
gated physics procedure cannot be run under the present fences.

## 11. Dependency re-audit

[PROVABLE] Every design decision that changes a count, class, or runner field
was re-walked through its dependents:

| Decision | Direct dependents re-audited | Result |
|---|---|---|
| V008/V009 remain in scope despite A35’s title | census, check-ID universe, expected row count, producer comparison, verifier comparison | 24 early rows are present; no `V010/V011-only` truncation remains |
| three A35-only sharpenings receive separate IDs | check count, class partition, schema, verifier, aggregate rule | count is 66, not 63; partition is 56/10 everywhere |
| zero-index and residue sharpenings are gated | row statuses, fixtures, aggregate PASS | gate-closed rows return `NOT_RUN_GATE`; no PASS is available under current fences |
| quasi-free CAR lift is structural | SP2-05 relation, quartic control, verifier | it checks a typed operator lift without selecting a physical parameter |
| two V003 pre-seal obligations are unnumbered | V010-08 and V010-14 predicates | rank-21 revival and later conversion mutations are explicit conjuncts without new blocker IDs |
| runtime-v012 name is hash-ambiguous | preflight `R0`, manifest `R1`, verifier, terminal ledger | unique authorized runtime hash is mandatory; no silent v014 substitution occurs |
| fixture outputs are quarantined | schema, producer comparison, verifier, authority firewall | no fixture field can populate a live response, coupling, alpha, or proof field |
| child receipts are non-authoritative | `R7`, `R8`, `R9`, aggregate rule | expected counts/verdicts arise only from sealed spec/manifests and independent replay |
| criterion prose must reduce to the closed opcode language | all 66 PASS fields, descriptor schemas, verifier expected census | 35 rows carry BOUND; 13 V003 re-renders carry; 8 rows are V004-REPAIRED; 10 rows are V005-REPAIRED |
| producer expectations cannot carry direction and reduction success is not truth | BR-1/A adjudicated regime, BR-2 mechanical procedure, all 66 descriptor rows | 29 over-generated atoms in 12 rows are individually adjudicated with named receivers; BR-2 returns zero failures with per-row coverage |
| Q-567's three direct row defects are repaired | SP1-07, SP2-06, SP2-07; sealed blocker spans; verifier | escape hatch removed, reality carrier consumed, exact zero-assert demand restored |
| two convicted and three warned rows are repaired | V009-10, V010-06, MR-06, SP1-04, V010-10 | basis/parity, derivation, selection, phase, and composite claims now bind |
| full class sweep finds twenty further unbound rows | per-row §8.3 ledger; descriptor hashes and check-map root | every proof/completeness/comparison/adjective item is named at its row |
| 8 V004 descriptor input/procedure/criterion records changed | `R1`, `R8`, `R9`, machine ledger, future manifests/receipts | IDs/counts/classes stay fixed; all future roots must bind the V004 bytes |
| 10 V005 descriptor records change under the closed adjudication | BR-1/A record, board, `R1`, `R8`, `R9`, machine ledger, future manifests/receipts | exactly the adjudicated ten change; the six lawful controls remain byte-identical to V004; all future roots must bind the V005 bytes |

[YOURS] A future edit after V005 to any blocker description, check predicate, class,
runtime pin, fixture expectation, schema, or custody identity changes the spec
hash and invalidates all manifests and receipts. Delta-only inheritance is not
allowed.

## 12. S5 — battery

### 12.1 F_PLDEC

[PROVABLE] The specification was derived from the blocker ledger, A35 row,
SP14/runtime protocol, and the prior missing-object statement. It does not read
or call:

```text
reader_F,
the local-shadow response value,
a fixed-point return,
an end-test value,
kappa_record,
alpha,
or any measured constant.
```

The check language has no reader opcode. Every physical-response,
survival-amplitude, interval containment, anomaly/determinant, two-point,
pole, or residue procedure is classed `GATED-EXECUTION` and is unrun here.

```text
F_PLDEC = CLEAN.
```

[PROVABLE] The V005 BR-1/A adjudication, BR-2 mechanical coverage, and C-V5a
re-diff compare only sealed text, descriptor structure, opcode bindings, and
byte ranges. They execute no descriptor and form no physical object.

### 12.2 Anti-tuning ledger

| Hazard | Mechanical guard | Result |
|---|---|---|
| desired number determines a check | IDs and predicates are sourced from the immutable V003/A35 obligations before any result | CLEAN |
| measured constant enters | no measured value, uncertainty, or comparator is read | CLEAN |
| negative competitor is hidden | all six mandatory competitors/controls are named with frozen expected dispositions | CLEAN |
| a family is collapsed to a member | `c`, `tau`, statistics, evolution, and preparation remain enumerated families until an independent selector exists | CLEAN |
| physical execution closes a structural task | ten physical rows are gate-classed and `NOT_RUN_GATE` under current fences | CLEAN |
| fixture output becomes live physics | schema quarantine and authority firewall forbid that data path | CLEAN |
| a manuscript status is promoted | every PASS requires content bytes, deterministic replay, both children, parent reclassification, and independent verification | CLEAN |
| normal/optimized mismatch is averaged | exact semantic equality is required; one-branch success is terminal failure | CLEAN |
| runtime chosen for favorable output | runtime subject must be an authorized content hash; the v012/v014 discrepancy is displayed | CLEAN |
| cross-sector unit silently set to one | `UNITS` rejects implicit conversions; this spec constructs no cross-sector conversion | CLEAN / NOT_APPLICABLE TO CONSTRUCTION |
| authorization inferred from signature | signature is local assurance only; RD-22 is a separate principal artifact | CLEAN |
| a positive-half proof is weakened to a favorable presence check | every carried/repaired derivation is a content-addressed `KERNEL` replay and every completeness claim is an `ENUM(grammar,cert)` result | CLEAN |
| a producer expectation fabricates the favorable direction | BR-1/A mechanically over-generates candidates, then a reviewer decomposes sealed clauses and names the independent receiver for every atom; §8.6 displays all 29 candidate adjudications and four repaired zero-candidate notes | CLEAN |
| a successful reduction is promoted to a favorable truth value | BR-2 requires a paired fixed-value comparison or `EXACT`/`KERNEL`; its final procedure returns zero failures | CLEAN |
| a prior sample is presumed complete | all 66 rows appear individually in §§8.3 and 8.6; BR-1/A is scoped to 29 displayed atoms plus explicit zero-candidate coverage, and BR-2 displays every row | CLEAN |

### 12.3 Surface anchor

[PROVABLE] The geometry-side predicates name the actual sealed objects and
families in the V005 lineage: the finite `K_L`, actual object-fiber
`E_open`, the connection complex and `d0/d1`, `F_phys=im(d1)`, `Q_flux`, the
rank-20 design and `T_top`, the Lorentzian Hodge map, the source Dirac/CAR
carrier, `b_partial`, `c_partial`, `Gamma_cell`, the SP17 incidence form,
`B_lambda`, the handle and full-star projectors, and the sealed refinement
class. A check cannot pass on an anonymous isomorphic placeholder because its
subject/evidence bytes and carrier maps are roots of `BASE`.

[YOURS] The new material here is rails, not geometry: stable IDs, closed check
descriptors, manifests, runtime state machine, verdict schema, and custody
separation. None of those rails selects a physical member or changes a sealed
geometric law.

[PROVABLE] V005 carries V004's binding repair over actual manifest-native packet
objects: the SP04/SP07/SP08 closure rows, the global-boundary executable
obligations, and the free-CTP boundary. The added proof/certificate schemas are
rails for testing those objects; they are not new source, pole, preparation, or
response inhabitants. V005 changes only the BR-1 regime text and the ten
adjudicated descriptor rows recorded in §8.5; the six adjudicated-lawful rows
retain their V004 bytes.

[PART-PROVABLE] A future implementation must freeze **one immutable V011
lineage manifest** as the subject for every one of the 66 rows. Until that
manifest and the runtime hash are authorized, the architecture is specified
but no evaluator member is claimed.

```text
SURFACE_ANCHOR = PRESENT.
```

### 12.4 M-2 — three guards and all five false-negative modes

[PROVABLE] The V005 BR-1/A adjudication and BR-2 mechanical sweep used all three guards
and V007 registers all five false-negative modes explicitly:

1. **Regex-metacharacter mode** (`d^per`): fixed-string searches were run before
   any regex-shaped query. The exact V005 ordinal headings and A35/SP14 phrases,
   including `Every blocker recorded`, `zero-index`, `operator-valued`,
   `residue`, `rank 21`, `response-to-action normalization`, `python -O`,
   `independent verifier`, and `runtime v012`, were searched literally.
2. **Line-wrap mode:** whitespace-normalized copies joined wrapped clauses and
   normalized Markdown emphasis, code ticks, and repeated spaces before
   comparing blocker clauses and executable rows. This preserves the SP2-05
   `full source-record orientation covariance` phrase across a source line
   break.
3. **Self-reference/scope mode:** every hit was classified by source role and
   containing section, so V005's own discussion of a phrase could not satisfy
   the source requirement. Hits for evaluator/runner/audit, seal/status,
   zero-free/domain, pole/threshold/residue, CAR/quasi-free, topology/null,
   action/Hessian/normalization, and runtime/snapshot/gate were read in their
   containing section. Repair-map restatements were not counted as new
   blockers; scope sharpenings were not erased as synonyms.
4. **Hyphenation mode** (`open-event` / `open event` / `open_event`):
   `[-_ ]` variants were jointly normalized and then checked in context.
   Whitespace normalization alone was not treated as closure.
5. **Corpus-membership mode:** before any query guard runs, the sealed corpus
   definition is checked against its authorizing content-addressed member list.
   Omitting a source capable of carrying the queried violation is a membership
   failure, not an empty search result. A producer-supplied or post-query corpus
   may accuse by exposing a mismatch but may never exculpate a row by omission.

The three guards, with all five modes neutralized, preserve the 63-row census,
the three A35-only sharpenings, the two unnumbered V003 regression conjuncts,
the runtime-pin discrepancy, and the 66-row V005 board. They also identify the
ten changed descriptor rows, preserve the six lawful controls, and distinguish
candidate generation from adjudication. A zero hit under guards 1–2 was never
used as an absence claim.

[PROVABLE] The binding edition additionally searched the escape identifiers and
the proof/premise/derivation/certificate/adjective family by fixed string first.
Whitespace-normalized comparison reproduces the complete SP2-07 blocker at
`[23527,23774)`; self-reference classification separates the sealed blocker,
descriptor, adjudication row, and carriage prose; and joint hyphen/space/
underscore normalization covers `target-independent`, `reality-factor`,
`proof-index`, `content-addressed`, and their variants. The old escape
identifiers have zero hits in the 66 executable descriptor rows. The
V004/V005 fixed strings `REJECTED`, `FAILS`, `CONTAINED`,
`INTERTWINER_IDENTITY`, `r_m2.hits=empty`, and
`ASSERTION_FREE_FORMATION` were searched literally before contextual
classification. Whitespace-normalized row copies preserve the V009-04
distinct/exact-one clauses and SP1-05 pre-enumeration ordering query;
self-reference classification separates §2 law, §8 transcript, and descriptor
uses; and joint hyphen/space/underscore normalization covers
`producer-declared`, `spec-fixed`, and `assertion-free`. The V005 additions
`ADMITTED`, `REJECTED_DIMENSIONFUL`, `INSUFFICIENT`, `INDEX_ONE`,
`Z_NOT_SUFFICIENT`, `BR1_CONFORMANCE_CLASS = ADJUDICATED`, and
`BR2_CONFORMANCE_CLASS = MECHANICAL` were likewise searched literally and read
in row context. That is a bounded source-structure/adjudication result for this
V005 byte subject, not an impossibility claim.

### 12.5 R9 quantification check

[PROVABLE] The repaired R9 lesson permits comparison per common member, not a
universal comparison across an orientation/family orbit. The runner obeys it:

```text
common_member_key :=
  (subject_lineage_root,
   check_id,
   check_spec_sha256,
   input_root_sha256,
   fixture_id_or_null).
```

Normal, optimized, and verifier results are compared only at the same
`common_member_key`. The runner does not compare different `c`, `tau`,
statistics, evolution, preparation, orientation-address, or physical-branch
members as if they were one. Family enumeration is covariant; no representative
is selected by the comparison.

```text
R9_QUANTIFICATION = COMMON_MEMBER_ONLY.
```

### 12.6 Self verb audit

| Verb used | Display immediately supporting it |
|---|---|
| `verified` | full SHA-256 strings in §0.2 and the runtime-pin byte records in §9.1 |
| `enumerated` | six disjoint ordinal ranges and all 63 requirement rows in §1 |
| `mapped` | one deterministic descriptor for each blocker plus three discrepancy descriptors in §§3–8 |
| `specified` | closed opcodes, runner states `R0–R10`, custody graph, and exact ledger schema in §§2 and 9 |
| `requires` | quoted A35/SP14 authority and explicit Boolean preconditions |
| `rejects` / `fails` | a displayed mutation/negative fixture and exact false predicate in the relevant row |
| `does not run` | gates/status transition in §2.3 and non-actions in §§0.3 and 12.8 |
| `cannot pass` | aggregate conjunction plus ten `NOT_RUN_GATE` rows in §9.5 |
| `re-rendered` / `repaired` | ten V005 descriptor rows named individually in §§8.3 and 8.5; the six adjudicated-lawful descriptor rows retain their V004 bytes |
| `adjudicated` | the over-generated 29-atom candidate set, per-candidate sealed clause, named receiver, and verdict in §8.6 |
| `swept 66/66` | BR-2's one-row-per-ID mechanical coverage and transcript in §8.6 |
| `opcode-reducible` | criterion grammar in §2.2 plus each self-audit disposition in §8.3 |
| `BOUND` / `RE-RENDERED` / `V004-REPAIRED` / `V005-REPAIRED` | exact 66-ID map/board bijection and the scoped 35/13/8/10 totals in §8.3 |
| `restored` | byte-exact SP2-07 blocker quotation plus the zero-hit `M2` predicate at its row |
| `unchanged` | anchor-bounded runtime, firewall, and aggregate hashes in the V005 pin check match V004 |
| `carriage verified` | raw named V004→V005 diff, declared C-V5a conventions, and exact hunk assignment in the V005 certificate |
| `zero failures` | BR-2's mechanical source-structure result over all 66 final rows in §8.6; BR-1/A is instead adjudicated and no physical execution verdict is claimed |

No unnegated present-tense `implemented`, `executed`, `authorized`, `computed`,
`proved physical`, or `seal attained` occurrence claims a run or physical
result. Their appearances are quoted descriptor requirements, fence/state
fields, future conditions, or explicit negations. “PASS iff” states a future
machine criterion; it is not a present verdict.

```text
VERB_AUDIT_SELF = CLEAN.
```

### 12.7 C-V5 named finite-diff carriage certificate

[YOURS] The carriage subject is exactly

```text
CARRIAGE_BASE = STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE3_V001.md @ sha256 eb2073ebb4f23cbc0c0bfa20a36c482e24c59dc6b6e1ccbcd1ef1bd1150d0ecb

CARRIAGE_OUTPUT = STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE3_V002.md

DIFF = /usr/bin/diff -U 0 CARRIAGE_BASE CARRIAGE_OUTPUT
```

The final raw diff hunks are named in file order. Each hunk belongs to exactly
one finite delta row in the table below; the table is the carriage claim.

<!-- C_V5_HUNK_TABLE_BEGIN -->
| Hunk | Final raw range | Named finite delta | Authority |
|---|---|---|---|
| H01 | `-1 +1` | Add `V002` to the title. | C-V5 version identity |
| H02 | `-3 +3` | Replace the V001 artifact filename by the V002 filename. | C-V5 version identity |
| H03 | `-7 +7` | State the eight-row finite-delta specification status. | PASTE 628; Q-561 |
| H04 | `-14,2 +14,3` | Refresh the living-register head to Q-563 without changing the review state. | PASTE 628 preflight; Q-563 |
| H05 | `-17,3 +18,4` | Retype no-clobber as V002 carriage over intact V001. | PASTE 628 output rule; C-V5 |
| H06 | `-24,0 +27,3` | Add the V001 base and both reviews of record to the verified authority table. | PASTE 628 preflight |
| H07 | `-31,0 +37,3` | Add the sealed packet manifest and two packet-native derivation sources. | G1; Q-562 custody rule |
| H08 | `-32,0 +41,5` | State the packet-line/root-byte citation discipline. | Q-562 custody rule |
| H09 | `-140 +153` | Escape the literal modulus bars so the carried V010-02 requirement remains one Markdown cell. | G4 self-audit |
| H10 | `-293 +306` | Extend `M2` to the four registered false-negative modes without adding an opcode. | G4; M-2 |
| H11 | `-300,0 +314,27` | Bind opcode invocations and content-addressed proof/completeness result fields. | G1–G2; Q-561 |
| H12 | `-301,0 +342,15` | Define opcode-reducibility and strip bare criterion words of Boolean force. | G1–G2; Q-561 |
| H13 | `-382 +437` | Re-render `C-B-V010-03`. | G2 newly found defect |
| H14 | `-402 +457` | Re-render `C-B-V011-MR-04`. | G2 newly found defect |
| H15 | `-418,2 +473,2` | Re-render `C-B-V011-SP1-06` and `C-B-V011-SP1-07`. | G2 finding; Q-561 commissioned defect |
| H16 | `-429 +484` | Re-render `C-B-V011-SP2-03`. | Q-561 commissioned defect |
| H17 | `-431,3 +486,3` | Re-render `C-B-V011-SP2-05`, `-06`, and `-07`. | Q-561 commissioned defects; G2 finding |
| H18 | `-481,0 +537,219` | Add the four positive-half displays, 66-row audit, totals, consistency propagation, and review inheritance. | G1–G3; Q-562 |
| H19 | `-683 +957,3` | Propagate all 66 V002 descriptor hashes and the 58/8 board to verifier expectations. | G3 |
| H20 | `-826 +1102` | Escape the literal modulus bars in the `c`-family fixture cell. | G4 self-audit |
| H21 | `-849,0 +1126,4` | Add the eight-row dependency re-audit. | G3; C-V5 |
| H22 | `-851 +1131` | Scope the future-edit invalidation rule to edits after V002. | G3 |
| H23 | `-880,0 +1161,4` | Record that the audit/rediff executes no descriptor or physical object. | F_PLDEC |
| H24 | `-896,0 +1181,2` | Add positive-half and unsampled-row false-negative regressions. | G4 |
| H25 | `-913,0 +1200,6` | Add packet-native surface anchors for the repaired predicates. | G4; Q-562 |
| H26 | `-923 +1215` | Retitle M-2 to expose all four false-negative modes. | G4 |
| H27 | `-925 +1217,2` | State the four-mode M-2 sweep. | G4 |
| H28 | `-927 +1220,2` | Separate the regex-metacharacter/fixed-string mode. | G4; M-2 |
| H29 | `-930,5 +1224,9` | Separate line-wrap and self-reference/scope modes. | G4; M-2 |
| H30 | `-938,0 +1237,3` | Add the hyphen/space/underscore mode. | G4; M-2 |
| H31 | `-940,3 +1241,4` | Restate M-2 outputs including the eight-row V002 repair set. | G4 |
| H32 | `-978 +1280` | Correct the self-audit's non-action cross-reference to §12.8. | G4 self-audit |
| H33 | `-979,0 +1282,4` | Add re-render, 66-row, opcode, and carriage verbs to the self-audit. | G4 |
| H34 | `-989 +1295` | Insert §12.7 and renumber the non-action section to §12.8. | C-V5 |
| H35 | `-990,0 +1297,79` | Add this named 36-hunk carriage certificate and immutable-block comparisons. | C-V5 |
| H36 | `-1001,4 +1386,4` | Replace V001 final lines with the PASTE-628 V002 final board. | PASTE 628 output contract |
<!-- C_V5_HUNK_TABLE_END -->

```text
FINAL_RAW_HUNKS = 36
FINAL_ADDED_LINES = 423
FINAL_DELETED_LINES = 38
UNASSIGNED_HUNKS = 0
MULTIPLY_ASSIGNED_HUNKS = 0
```

[PROVABLE] Anchor-bounded byte comparisons are required separately for the two
confirmed regions that V002 must not touch:

```text
runtime-pin §9.1 expected block hash =
  712a861aaf5f2f43590f41405435663dff8efd52a93e30d33cc2399636442172

aggregate §9.5 expected block hash =
  bfad44417f766cc97a8942a8ffab7f9accd5791a2c2f1169a6534f3643543648
```

Their final V002 comparison results are recorded with the completed hunk table.
Whitespace normalization is used for M-2 searching, never to hide a carriage
edit.

### 12.7A V003 complete finite-delta carriage certificate

[PROVABLE] The V003 carriage subject and declared diff convention are:

```text
CARRIAGE_BASE = STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE3_V002.md
CARRIAGE_BASE_SHA256 = 25e89ed24933d66fcb6991b83bb971775be834070f8570a8b89cd0248f22edb7
CARRIAGE_OUTPUT = STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V003.md
DIFF = /usr/bin/diff -U 3 CARRIAGE_BASE CARRIAGE_OUTPUT
FINAL_HUNKS = 21
FINAL_INSERTIONS = 261
FINAL_DELETIONS = 163
```

| Hunk | Final unified range | Complete named delta | Authorizing item |
|---|---|---|---|
| H01 | `-1,29 +1,31` | Advance artifact/lane/status to V003; refresh Q-568/no-clobber; pin the V002 base and Q-567 conviction. | B1/B2/B3 |
| H02 | `-312,9 +314,9` | Retitle the criterion-result binding edition from V002 to V003. | B3 |
| H03 | `-350,10 +352,22` | State the binding-class rule for proof, premise, derivation, completeness, enumerated comparison, and load-bearing adjectives. | B3 |
| H04 | `-405,75 +419,75` | Re-render the affected V008/V009/V010/MR/SP1 descriptor rows, including convicted/warned rows and SP1-07 escape-hatch removal. | B1/B3 |
| H05 | `-482,10 +496,10` | Re-render SP2-04, SP2-06, and SP2-07; name the reality carrier and require zero Python-assert hits. | B2/B3 |
| H06 | `-497,7 +511,7` | Re-render the A35 physical-residue discrepancy row with explicit grammar, proof, spectral, domain, and comparison receivers. | B3 |
| H07 | `-558,11 +572,12` | Replace SP1-07's obsolete coverage narrative with the nonempty mandatory proof-index account. | B1 |
| H08 | `-624,103 +639,117` | Record the SP2-06 carrier repair, quote SP2-07 at its sealed span, and replace the unsound board with the 66-row 38/28 binding adjudication. | B2/B3 |
| H09 | `-732,9 +761,9` | Propagate 28 changed descriptor hashes and the V003 check-map root. | B3 |
| H10 | `-744,14 +773,14` | Update the independent verifier's expected descriptors and binding-board counts; carry Q-567. | B3 |
| H11 | `-954,9 +983,9` | Update the R9 verifier child to the V003 descriptor hashes and 38/28 board. | B3 |
| H12 | `-1123,12 +1152,13` | Re-audit dependencies for the direct defects, convicted/warned rows, twenty further sweep rows, and 28 changed descriptors. | B1/B2/B3 |
| H13 | `-1159,7 +1189,7` | Retype F_PLDEC's text-only audit subject as the V003 binding audit. | B3 |
| H14 | `-1178,8 +1208,8` | Update anti-tuning to `ENUM(grammar,cert)` and the complete 38/28 per-row sweep. | B3 |
| H15 | `-1197,7 +1227,7` | Re-anchor the added rails to the V003 binding repair and sealed packet objects. | B3 |
| H16 | `-1214,7 +1244,7` | Retype the M-2 sweep as V003. | B3 |
| H17 | `-1228,7 +1258,7` | Update the M-2 self-reference/scope guard to V003. | B3 |
| H18 | `-1240,8 +1270,18` | Propagate the 28-row result and binding-specific fixed/normalized/scope/variant guards through the M-2 summary. | B3 |
| H19 | `-1279,10 +1319,13` | Update self-verb-audit support for 28 re-renders, restoration, protected hashes, and V002-to-V003 carriage. | B2/B3 |
| H20 | `-1371,6 +1414,59` | Add this complete V003 carriage table, displayed re-diff summary, and three protected-block hashes. | B1/B2/B3 |
| H21 | `-1383,9 +1479,11` | Replace the V002 terminal board with the commissioned V003 dispositions and complete row list. | B1/B2/B3 |

[PROVABLE] Anchor-bounded hashes over the unchanged V002 and final V003 bytes
match exactly:

```text
runtime-pin §9.1 =
  712a861aaf5f2f43590f41405435663dff8efd52a93e30d33cc2399636442172
authority firewall =
  a9e7e50afb466ead16c43b45352d1c04273bb9c3e5671f5f7c386df70cdf0afa
aggregate rule §9.5 =
  bfad44417f766cc97a8942a8ffab7f9accd5791a2c2f1169a6534f3643543648
```

[YOURS] Every final unified-diff hunk is assigned exactly once in the table.
Outside those hunks, V003 is byte-identical to V002.

### 12.7B V004 complete finite-delta and pin-check certificate

[PROVABLE] V004 was constructed by byte-copy of the pinned V003 base followed
by the named replacements in this table. The declared conventions are:

```text
CARRIAGE_BASE = STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V003.md
CARRIAGE_BASE_SHA256 = f910815c84fd29d3dc6ca55f43ebe5d4c7015f457ddcde7bd7a69afdf81658dc
CARRIAGE_OUTPUT = STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V004.md
DIFF = /usr/bin/diff -U 3 CARRIAGE_BASE CARRIAGE_OUTPUT
RANGE_CONVENTION = raw unified-diff header, in final file order
COUNT_CONVENTION = exclude only the ---/+++ file headers; count every other
  line beginning + or -, including a bare + or - blank line
ASSIGNMENT_CONVENTION = one physical hunk row; a shared hunk lists every
  logically distinct authorized replacement contained in that hunk
```

| Hunk | Final unified range | Complete named delta | Authorizing item |
|---|---|---|---|
| H01 | `-1,29 +1,43` | Advance identity/custody/status to V004; add the scoped lead verdict; refresh Q-574/no-clobber; pin the base, correction, and parent. | P1/P2/P4/output |
| H02 | `-204,7 +218,7` | Restore the exact SP2-07 load-bearing-audit requirement summary. | P2 item 11 |
| H03 | `-367,7 +381,78` | Install BR-1/BR-2 as law, their rationale, spec-fixed values, and the two named whole-file conformance procedures. | P1 |
| H04 | `-431,7 +516,7` | Repair V009-04 distinctness, exact-one direction, all three domain successes, and per-item bound. | P2 item 1 |
| H05 | `-446,7 +531,7` | Repair V010-01 with spec-fixed `REJECTED` and mark the formation-only reduction. | P2 item 4 / BR-2 |
| H06 | `-458,8 +543,8` | Repair both V010-13 defects and give V010-14's M-2 ordering atom a named receiver. | P2 items 5, 6, 9 |
| H07 | `-469,9 +554,9` | Add MR-05 pairwise distinctness and pair MR-07's SYMBOLIC result with spec-fixed `CONTAINED`. | P2 items 7, 2 |
| H08 | `-480,10 +565,10` | Force SP1-02 to `INTERTWINER_IDENTITY`; render SP1-05 completeness, ordering, and candidate typing. | P2 items 8, 3 |
| H09 | `-663,13 +748,15` | Scope the 66-row board under the verdict-line rule and define the three V004 dispositions. | P2/P3 |
| H10 | `-687,7 +774,7` | Propagate V009-04's V004 repair to its board row. | P2 item 1 |
| H11 | `-697,7 +784,7` | Propagate V010-01's V004 repair to its board row. | P2 item 4 |
| H12 | `-709,22 +796,22` | Propagate the other six changed descriptor rows to the board without changing any class. | P2 items 2, 3, 5–9 |
| H13 | `-743,13 +830,17` | Correct the board totals to 36/22/8 and bind the scoped result to the two named tests. | P2/P3 |
| H14 | `-761,27 +852,93` | Propagate eight descriptor hashes; display all 11 repairs; display the final BR-1/BR-2 transcript and zero-failure/outside-list results. | P2/P3/P4 |
| H15 | `-983,9 +1140,9` | Update the independent verifier census to V004 and 36/22/8. | P2/P3 |
| H16 | `-1152,13 +1309,14` | Re-audit dependencies for BR law, eight changed rows, final roots, and future edits after V004. | P1/P2/P3 |
| H17 | `-1189,7 +1347,7` | Retype F_PLDEC's source-structure subject as the V004 closed-list/BR audit. | P5 |
| H18 | `-1208,13 +1366,15` | Add BR-1/BR-2 anti-tuning hazards and retag the carried surface lineage as V004. | P5 |
| H19 | `-1227,11 +1387,12` | State that the surface change is rails-only and limited to the laws plus closed list. | P5 |
| H20 | `-1244,21 +1405,21` | Retype the four-mode M-2 guard descriptions for the V004 sweep. | P5 |
| H21 | `-1268,10 +1429,11` | Update the guarded M-2 result to the 66-row board, eight row changes, and eleven items. | P5 |
| H22 | `-1280,8 +1442,16` | Display V004 fixed-string, line-wrap, scope, and hyphenation checks with bounded scope. | P5 |
| H23 | `-1319,17 +1489,20` | Update the self verb audit for eight changes, 36/22/8, named tests, V004 carriage, and verdict-line scope. | P5 |
| H24 | `-1424,7 +1597,7` | Correct the historical V003 insertion count from 248 to the blank-line-safe value 261. | P2 item 10 |
| H25 | `-1467,6 +1640,97` | Add this diff-derived certificate and pin-check. | P4 |
| H26 | `-1479,11 +1743,11` | Replace the terminal disposition block with the scoped V004 output contract. | output |

```text
FINAL_HUNKS = 26
FINAL_INSERTIONS = 350
FINAL_DELETIONS = 86
UNASSIGNED_HUNKS = 0
MULTIPLY_ASSIGNED_HUNKS = 0
REFLOW_ONLY_CLAIMS = 0
CONTENT_BEARING_HUNKS = 26
```

[PROVABLE] The seven physical hunks containing more than one logical
assignment are displayed rather than hidden by a one-row-per-hunk convention:

```text
SHARED_ASSIGNMENT_HUNKS =
  H01 [identity/lead verdict/preflight/authority pins]
  H06 [V010-13 independence; V010-13 failure direction; V010-14 M-2]
  H07 [MR-05 distinctness; MR-07 reduction truth]
  H08 [SP1-02 direction; SP1-05 completeness/order]
  H12 [six repaired board entries]
  H14 [hash propagation; 11-item disposition; two conformance transcripts]
  H18 [BR anti-tuning hazards; V004 surface-lineage tag]
RESTORATION_OR_REFLOW_CLASSIFICATIONS = []
DESCRIPTOR_ROW_CHANGES = 8
CLOSED_LIST_ITEMS = 11
```

[PROVABLE] PRE-SEAL PIN CHECK over the final bytes returns:

| Claim | Fixed location/check | Final result |
|---|---|---|
| BR laws and test names | §2.2 exact fixed-string search | both laws; both names present |
| full-file sweeps | §8.6 parsed descriptor rows | 66 each; BR-1 failures `[]`; BR-2 failures `[]` |
| closed descriptor delta | V003/V004 descriptor-row diff | exactly the eight IDs in §8.4; no outside-list row |
| closed work list | §8.5 numbered table | 11/11 `REPAIRED` |
| paired verdict blocks | lead code block versus final eight lines | byte-identical; SHA-256 `e28baa0d4c1f4b8648f64d3cf15e1213066e403f2f3656e1310b7322c2fb9d51` |
| historical insertion correction | §12.7A fixed string | `FINAL_INSERTIONS = 261` |
| runtime pin §9.1 | anchor-bounded byte block | `712a861aaf5f2f43590f41405435663dff8efd52a93e30d33cc2399636442172` |
| authority firewall | anchor-bounded byte block | `a9e7e50afb466ead16c43b45352d1c04273bb9c3e5671f5f7c386df70cdf0afa` |
| aggregate rule §9.5 | anchor-bounded byte block | `bfad44417f766cc97a8942a8ffab7f9accd5791a2c2f1169a6534f3643543648` |

[YOURS] Regenerating the final diff reproduces every header above. No raw hunk
falls outside the table, no table row lacks a hunk, no descriptor outside the
eight-ID set changes, and outside these 26 hunks V004 is byte-identical to V003.

### 12.7C V005 C-V5a complete finite-delta and pin-check certificate

[PROVABLE] V005 was constructed by byte-copy of the pinned V004 base followed
by the closed replacements named below. The declared conventions are:

```text
CARRIAGE_BASE = STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V004.md
CARRIAGE_BASE_SHA256 = 2c767bfc953c7efeeaf4a33542974b10e0a674a161a5f1a651f3486ac36fad8b
CARRIAGE_OUTPUT = STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md
DIFF = /usr/bin/diff -U 3 CARRIAGE_BASE CARRIAGE_OUTPUT
RANGE_CONVENTION = raw unified-diff header, in final file order
COUNT_CONVENTION = exclude only the ---/+++ file headers; count every other
  line beginning + or -, including a bare + or - blank line
ASSIGNMENT_CONVENTION = one physical hunk row; a shared hunk lists each
  logically distinct authorized replacement with line-level attribution
```

| Hunk | Final unified range | Complete named delta with line-level attribution | Authority |
|---|---|---|---|
| H01 | `-1,18 +1,18` | Lines 1/3 advance the artifact to V005; lines 6–7 state custody/status; lines 10–17 install the scoped lead verdict. | T1/T3/T4/output |
| H02 | `-21,20 +21,22` | Lines 24–27 refresh Q-580; lines 29–32 record the no-clobber byte-copy; lines 38–39 pin the V004 base and BR-1 adjudication. | preflight/T4 |
| H03 | `-382,7 +384,7` | Retitle the law section for V005 and the two conformance classes. | T1 |
| H04 | `-414,27 +416,62` | Lines 417–426 extend the spec-fixed token set; lines 428–431 classify BR-1 as ADJUDICATED and BR-2 as MECHANICAL; lines 433–478 replace the runnable-test claim with the exact BR-1/A regime and retain the named BR-2 procedure. | T1 |
| H05 | `-448,10 +485,10` | Retype whole-file scope and outside-list edit discipline for the adjudicated/mechanical split. | T1/T2 |
| H06 | `-505,27 +542,27` | Descriptor lines repair, individually, `V008-09` (fixed branch map), `V008-11` (`FAILS`), `V009-02` (dimensionful case/fixed class), `V009-07` (spec digest/`REJECTED`), `V009-10` (deterministic KERNEL goal), and `V009-13` (`FAILS`). | T2 items 1–6 |
| H07 | `-551,14 +588,14` | Descriptor lines repair `MR-02` by declared `RESOLVE`/pairwise distinctness and `MR-09` by spec-fixed `INSUFFICIENT`. | T2 items 7–8 |
| H08 | `-580,7 +617,7` | Repair `SP2-03` by comparing the nonzero-index control to spec-fixed `INDEX_ONE`. | T2 item 9 |
| H09 | `-596,7 +633,7` | Repair A35 physical residue by comparing finite-cell `z` to spec-fixed `Z_NOT_SUFFICIENT`. | T2 item 10 |
| H10 | `-748,15 +785,14` | Retitle and scope the 66-row board; define the four V005 dispositions and verdict-line boundary. | T2/T3 |
| H11 | `-768,22 +804,22` | Board lines separately propagate the six repaired descriptors `V008-09`, `V008-11`, `V009-02`, `V009-07`, `V009-10`, and `V009-13`. | T2 items 1–6 |
| H12 | `-799,14 +835,14` | Board lines separately propagate repaired `MR-02` and `MR-09`. | T2 items 7–8 |
| H13 | `-818,29 +854,30` | Board lines separately propagate repaired `SP2-03` and A35 residue; count 35/13/8/10; scope BR-1/A as adjudicated and BR-2 as mechanical. | T2/T3 |
| H14 | `-852,92 +889,200` | Lines 892–918 propagate the ten hashes/board; lines 920–935 display the exact ten and six lawful controls; lines 937–1084 display the 29 candidate atoms, four repaired zero-candidate notes, all-row candidate index, and per-row BR-2 transcript. | T2/T3/T4 |
| H15 | `-1140,9 +1285,10` | Propagate all 66 V005 descriptor hashes and the 35/13/8/10 board to independent-verifier expectations. | T3/T4 |
| H16 | `-1309,14 +1455,15` | Dependency rows separately propagate the four-part board, 29-atom adjudication, ten-row/six-control descriptor delta, and future V005 root. | T1/T2/T3/T4 |
| H17 | `-1347,9 +1494,9` | Retype F_PLDEC's text-only subject as V005 BR-1/A, BR-2, and C-V5a review. | T5 |
| H18 | `-1367,14 +1514,14` | Anti-tuning lines separately scope BR-1/A to displayed adjudications, BR-2 to its mechanical sweep, full-row coverage, and the V005 surface-lineage tag. | T3/T5 |
| H19 | `-1387,12 +1534,13` | State V005's rails-only ten-row change and byte-preservation of the six lawful descriptors. | T2/T5 |
| H20 | `-1405,11 +1553,11` | Retype the M-2 battery and fixed-string subject from V004 to V005. | T5 |
| H21 | `-1419,7 +1567,7` | Retype the M-2 self-reference/scope guard to the V005 subject. | T5 |
| H22 | `-1431,9 +1579,10` | Propagate ten repaired rows, six lawful controls, and candidate/adjudication separation through the guarded result. | T2/T3/T5 |
| H23 | `-1443,15 +1592,19` | Add V005 token/class fixed strings and bound the source-structure/adjudication result to the V005 bytes. | T1/T2/T5 |
| H24 | `-1489,14 +1642,15` | Update the self verb audit for ten repairs, 29 adjudications, BR-2 66/66, 35/13/8/10, protected pins, C-V5a carriage, and verdict-line scope. | T2/T3/T4/T5 |
| H25 | `-1731,6 +1885,88` | Insert this diff-derived C-V5a certificate, declared conventions, shared-hunk line attribution, displayed counts, and pre-seal pin check. | T4 |
| H26 | `-1743,11 +1979,11` | Replace the V004 terminal board with the exact scoped V005 output contract. | output/T3/T4/T5 |

```text
FINAL_HUNKS = 26
FINAL_INSERTIONS = 409
FINAL_DELETIONS = 173
UNASSIGNED_HUNKS = 0
MULTIPLY_ASSIGNED_HUNKS = 0
REFLOW_ONLY_CLAIMS = 0
CONTENT_BEARING_HUNKS = 26
```

[PROVABLE] C-V5a's shared-hunk requirement is met at line level: H01, H02, H04,
H06, H07, H10–H14, H16, H18–H19, and H22–H24 enumerate every logical
assignment inside their physical hunk. The mapping from the 26 physical hunks
to H01–H26 is total and injective; no line is licensed by an implicit editorial
or reflow category.

[PROVABLE] PRE-SEAL PIN CHECK over the final pre-seal bytes returns:

| Claim | Fixed location/check | Final result |
|---|---|---|
| base and adjudication pins | §0.2 SHA-256 plus sidecar verification | exact V004 `2c767bfc…` and adjudication `ec0412d2…` |
| BR-1/A law text and classes | exact block comparison plus fixed strings in §2 | exact adjudication text; `ADJUDICATED` / `MECHANICAL` |
| descriptor universe/delta | parsed §§3–8 rows and V004/V005 row diff | 66 rows; exactly the ten IDs in §8.5; no outside-list descriptor edit |
| lawful controls | exact row-byte comparison V004/V005 | 6/6 byte-identical |
| BR-1/A record | §8.6 candidate and coverage tables | 12 candidate rows; 29 atoms; 54 zero-candidate row notes; 29/29 adjudicated |
| BR-2 transcript | §8.6 parsed per-row coverage | 66/66 rows; 8 assignments across 7 rows; failures `[]` |
| paired verdict blocks | lead block versus terminal eight lines | byte-identical; SHA-256 `c8715a045b896611d3fd9d3c67a16abba24557e500d621ba1fab9dd25489648f` |
| runtime pin §9.1 | anchor-bounded byte block | `712a861aaf5f2f43590f41405435663dff8efd52a93e30d33cc2399636442172` |
| authority firewall | anchor-bounded byte block | `a9e7e50afb466ead16c43b45352d1c04273bb9c3e5671f5f7c386df70cdf0afa` |
| aggregate rule §9.5 | anchor-bounded byte block | `bfad44417f766cc97a8942a8ffab7f9accd5791a2c2f1169a6534f3643543648` |
| finite carriage | regenerated `/usr/bin/diff -U 3` | 26 raw hunks; every header assigned once; blank-line-safe counts shown above |

[YOURS] The pin check is specification-source review only. It neither executes a
descriptor nor opens a physical gate. Outside the 26 displayed hunks, V005 is
byte-identical to V004.

### 12.7D V006 correction and V007 complete finite-delta certificate

[PROVABLE] V007 was constructed by byte-copy of the pinned V006 base followed
only by the named replacements recorded below. Counts use `/usr/bin/diff -U 3`;
file headers are excluded and every other `+` or `-` line, including a bare
blank-line marker, is counted. The V005→V006 certificate's published insertion
count is corrected from 58 to **63**: its four displayed hunk ranges themselves
sum to 63 insertions and 21 deletions, net +42.

```text
CARRIAGE_BASE = STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V006.md
CARRIAGE_BASE_SHA256 = 1b8b03e4b2688acb30d8c3f5afea3529be8322f8541406adae520aa51e654995
CARRIAGE_OUTPUT = STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V007.md
COUNT_CONVENTION = diff -U 3; exclude only ---/+++ headers; include blank lines
FINAL_HUNKS = 13
FINAL_INSERTIONS = 122
FINAL_DELETIONS = 34
UNASSIGNED_HUNKS = 0
MULTIPLY_ASSIGNED_HUNKS = 0
```

| Delta item | Exact authorization and content |
|---|---|
| V7-01 | E1(a): advance header/preflight/pins; correct V006's insertion count to 63. |
| V7-02 | E1(a,d): restore the 14-opcode fence, schema-bind `SEALED_CORPUS_DEFINITION`, restore the full implementation obligation, and order P0 before `SPEC-INCOMPLETE`. |
| V7-03 | E1(b): re-render only `C-B-V009-06` into the principal-ruled single-authority DAG plus byte-grounding digest criterion. |
| V7-04 | E2/686: add the recorded invocation carrier that links consumed arguments to source SHA-256, byte span, and raw span digest. |
| V7-05 | E1(c): display the three final V007 structural-fixture byte spans. |
| V7-06 | E1(e): register corpus membership as the fifth M-2 false-negative surface. |
| V7-07 | E3/output: add this complete finite-delta certificate and replace the scoped terminal verdict. |

[PROVABLE] A regenerated diff assigns every physical hunk and every changed
line to V7-01–V7-07. The protected runtime pin (§9.1), authority firewall, and
aggregate rule (§9.5) are byte-identical to V006.

### 12.8 What this artifact does not do

This artifact does **not** implement a parent, producer, check, verifier,
fixture, signature, or seal evaluator. It does **not** launch Python in normal
or optimized mode. It does **not** execute even a structural descriptor. It
does **not** evaluate a physical quantity, bind a family member, run a fixed
point/end test, compare a measured constant, compute `kappa_record` or alpha,
authorize RD-22, attain A35, or change any seal-rail status.

It supplies only the complete reviewable definition needed for a later,
separately authorized implementation.

V007 = 5 repairs
M2_CORPUS_RULE = executable and schema-bound
M2_REGISTRY = 17 rows (SPEC-INCOMPLETE pending sealed corpus definitions)
DESCRIPTOR_ROWS = 65 unchanged + C-B-V009-06 re-rendered
PROTECTED_SECTIONS = unchanged
CARRIAGE = complete_finite_delta
AUTHORIZATION = not_claimed
VERB_AUDIT_SELF = CLEAN
