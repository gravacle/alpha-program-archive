# Stage 8 / 7A Step 11 — P-B Instance and Receiver Choice — Codex 2 v001

Date: 2026-08-08  
Lane: CODEX 2  
Scope: the ruled P-B component for `C-B-V009-01`, followed by the bounded
`C-B-V010-14` receiver-choice display

## 0. Preflight, custody, and pins

The relay input
`relay_inbox/RELAY_PASTE_734_PB_INSTANCE_RECEIVER_CODEX2_V001.md` rehashed to
`71bb0a287cc402086dde17bde1afe6478e421b2911a285a110108ec1330aa696`;
its seal matched, its lane guard named CODEX 2, and
`relay_outbox/734_ACK.md` was written before task work. The requested report
name was absent from both the cleanroom and archive workspace.

The governing ruling was present in the registrar's sealed archive supervision
tree, not as a cleanroom duplicate. Its bytes and sidecar verified before use.
No unsealed root copy is cited.

| ID | Sealed source | SHA-256 | Use |
|---|---|---|---|
| `RULING` | `DECISION_V009_01_CARRIER_PB_2026-08-08.md` | `1741cdb311def6263d3ab333c6f7d4280e80f862bdf2208276f94a1f4297e870` | selects P-B and bars basis/trivialization |
| `G3-SPEC` | `36_GATE3_HILBERT_FUNCTOR_SPEC_V001.md` | `953e875b5080a24fee0d8515c0ec7c2d93b644c1ec8b53acc121bcd99d7a330b` | Gate-3 carrier and form contract |
| `G3-RESULT` | `38_GATE3_HILBERT_FUNCTOR_RESULT_V001.md` | `ea707b3a5e5a93297c793c9f4227b456b97d7f8e184da95d96436299076915da` | unique degree-zero form modulo congruence |
| `V011` | packet `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` | `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` | ordinary minimal first-opening graph |
| `U7` | `STAGE8_7A_U7_DISPOSITION_CODEX2_V001.md` | `0145c5dbbed1681067a211021892100cf6d18c6ef25ba9c7e905aeedc8a7f20d` | P-A/P-B and receiver facts |
| `BOX-DELTA` | `STAGE8_7A_BOX_SCHEMA_DELTA_CODEX2_V001.json` | `b52e66b79787a55bad1553c05dfa8df52e7b11153879589d9627073a8e06bba9` | `BX07` alias-corpus split and box conventions |
| `SPEC` | `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V012.md` | `382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504` | sealed descriptors and binding law |
| `CV2` | `STAGE8_TASK6_CONTRACT_V002_DISPOSITIONS_CODEX2_V001.md` | `c0af7131f0adc522ef14f7848ab38458df5af5a7a60dbe36131d1567351009c5` | Builder-B coverage-direction custody |

The builder verified the first six pins before it emitted bytes. Exact source
spans are also carried in the instance: Gate-3 spec `[582,2561)` with span
digest `d7f99182063f63764445f83cbc1046c142ec50213b0b1d4e7162e2df30b17231`
and Gate-3 result `[338,1785)` with span digest
`81826f886ce1ddab504162962f931dcfefa1625835b0b0610df592f8a184efd3`.

Jurisdiction is structural only. No member, physical magnitude, target value,
fixed point, end test, or measured constant is selected or evaluated.

## 1. Part A — ruled P-B instance

### 1.1 Rooted-star object

The generated instance is the ordinary rooted star

`r --M--> p_M`, `r --Q--> p_Q`, `r --G--> p_G`

with complex ID `K_open_PB`. Its endpoint carrier is the ordered abstract
direct sum

`E_open_PB = L_r direct-sum L_pM direct-sum L_pQ direct-sum L_pG`.

The four line objects are separately content-addressed. Dimension one is a
schema fact only; it is not used to choose a basis, scalar coordinate, unit
representative, or trivialization.

| Line / cell | Payload SHA-256 | Inclusion into `C_0(K_open_PB;L)` | Induced form |
|---|---|---|---|
| `L_r` / `r` | `e9c1988fbc87bc8b61e7f1ec669f9a5d352947b81ed81448a92a37b2019e8117` | `iota_L_r : L_r -> C_0(K_open_PB;L)`, image summand `r` | `h_L_r=iota_L_r^* M_0 iota_L_r` |
| `L_pM` / `p_M` | `7c590f1a087e0e928aa36bcfdc408c3b1d4dc54ea89225ce4fc7c7a792ff4b16` | `iota_L_pM : L_pM -> C_0(K_open_PB;L)`, image summand `p_M` | `h_L_pM=iota_L_pM^* M_0 iota_L_pM` |
| `L_pQ` / `p_Q` | `de6fe3c58cb7be10c08132c8f820ec28c389df3387c63902a09d74482ef95967` | `iota_L_pQ : L_pQ -> C_0(K_open_PB;L)`, image summand `p_Q` | `h_L_pQ=iota_L_pQ^* M_0 iota_L_pQ` |
| `L_pG` / `p_G` | `548c60b8e3b2af14d6321a0fdbc750849b7c2afc08970c5407d9f3d8c87db5fd` | `iota_L_pG : L_pG -> C_0(K_open_PB;L)`, image summand `p_G` | `h_L_pG=iota_L_pG^* M_0 iota_L_pG` |

Every induced form names the same content-pinned Gate-3 source form
`GATE3_M0_IDENTITY_FIBER_FORM`, whose sealed result states uniqueness only
modulo overall congruence. The instance's `licenses` object is exactly
`{basis:false, scalar_trivialization:false, unit_representative:false}`.

### 1.2 Explicit edge transports

| Edge | Transport | Domain/codomain | Exact abstract-unitary relations |
|---|---|---|---|
| `e_M` | `U_eM` | `L_r -> L_pM` | `U_eM^* U_eM=id_L_r`; `U_eM U_eM^*=id_L_pM`; `U_eM^* h_L_pM U_eM=h_L_r` |
| `e_Q` | `U_eQ` | `L_r -> L_pQ` | `U_eQ^* U_eQ=id_L_r`; `U_eQ U_eQ^*=id_L_pQ`; `U_eQ^* h_L_pQ U_eQ=h_L_r` |
| `e_G` | `U_eG` | `L_r -> L_pG` | `U_eG^* U_eG=id_L_r`; `U_eG U_eG^*=id_L_pG`; `U_eG^* h_L_pG U_eG=h_L_r` |

Each map has kind `ABSTRACT_UNITARY_HERMITIAN_LINE_MORPHISM` and
`coordinate_scalar_present=false`. Distinct line and cell IDs remain distinct.

### 1.3 Content addressing and schema compilation

The complete instance and compiled component have the same canonical bytes and
SHA-256:

`dcb90e6e0abf4419d8a82212a48a0339798ceb6d43498ebcc05447975dc25112`.

The new closed `BX-line` instance schema is
`contracts/bx_line_pb.schema.json`, SHA-256
`f2c98cbb6d6f1d6e5c36ea0a7b4316e488cd8641ebd2f317b74545358a97f655`.
It closes the topology, ordered four-line census, exact source references,
transport domains/codomains, three unitary relations per edge, and all three
negative licenses. The companion line-subobject schema hashes to
`5aae72f971089a4d8c48b2840986dae11b71baba62152b467d083a6cde888a32`.

Compilation returned `PASS_COMPONENT_BUILT`, not a row PASS. The honest row
status is `PARTIAL_CARRIER_READY_ALIAS_CORPUS_ABSENT`; the two remaining
requirements are the exact members of
`CD:C-B-V009-01:abstract-line-alias-corpus` and its pre-query member-selection
authority. This is the split already recorded by `BX07` in `BOX-DELTA`.

### 1.4 Self-check transcript

| Check | Result |
|---|---|
| direct isolated build (`python3 -I -S -B`) | generated the 15-file inventory and `PASS_COMPONENT_BUILT` record |
| Python AST parse | `PASS` |
| generated inventory byte-length/digest replay | `PASS`, 15/15 |
| closed-schema validation | `PASS` |
| content and source-span verification | `PASS` |
| distinct lines / inclusions / induced forms / transports | `4 / 4 / 4 / 3` |
| basis-license flip negative | refused `SCHEMA_CONFORMANCE` |
| duplicate-line-ID negative | refused `SCHEMA_CONFORMANCE` |
| coordinate-scalar transport negative | refused `SCHEMA_CONFORMANCE` |
| missing-unitarity-relation negative | refused `SCHEMA_CONFORMANCE` |
| second build over occupied output directory | refused `OUTPUT_COLLISION:package outputs`, preserving prior bytes |

The generated inventory itself is outside its recursive member set and hashes
to `f6552ff65d5b9fde743f2e28b408beba409bc06313ed2625d6d219e8bfdfc443`.
No chain entry point ran.

## 2. Part B — receiver repair choice

### 2.1 Defect fixed by either reading

The sealed V012 descriptor row for `C-B-V010-14` has row digest
`80557686eb5f01006825c0bbcf3f087c24d3618fbfda8cbe0d3dc4bb0a3cb3f7`
under the no-line-terminator convention. It contains bare `DAG` and `EXACT`
terms but only one named assignment, `r_m2`. Builder A therefore generated only
`M2/r_m2` in that row's `program_contract`. This violates the sealed binding
law regardless of which repair owner is chosen.

### 2.2 Touch-surface comparison

| Reading | Required whole state change | Relative surface |
|---|---|---|
| descriptor-owned explicit receivers | one descriptor row and carriage certificate; its row hash and V013 spec pin; Builder-A check map, byte spans, evidence/spec copies, manifests and inventories; Builder-B spec const, CV2-05b total-assignment reporting, tests, schema, root, instance, and A-side boundary pins | smaller: the descriptor is the single authoritative result-name and repeatability source; no second expansion language is created |
| sealed generated-expansion contract | new cross-builder expansion schema and instance; mutation-multiplicity rules; Builder-A generator/validator, check map, manifests and pins; Builder-B CV2-05b reporting, resolver coverage, negatives, schema, root, instance, and A-side boundary pins | larger: preserves one row only by introducing a second authoritative program representation plus cross-builder conformance machinery |

**Choice: descriptor-owned explicit receivers.** It has the smaller lawful
surface because the existing descriptor remains the sole executable-program
authority and the existing materializer already derives the ordered
`program_contract` from named assignments.

### 2.3 Full row display for the chosen repair

Current sealed row (before):

```text
| `C-B-V010-14` | STRUCTURAL | claim graph; amplitude/action provenance; FS relation; pre-seal conversion mutations | `DAG`; `r_m2:=M2(q_silent_conversion,preseal_sources)`; `EXACT` Hessian check; inject factor-two/factor-four/later coefficient mutations | FS appears only downstream as a check on the physical amplitude’s Hessian; `r_m2.success and r_m2.hits=empty`; no `A^c`, multiplicity, or later conversion is selected |
```

Chosen candidate row (after, display only; not issued as law here):

```text
| `C-B-V010-14` | STRUCTURAL | content-addressed claim/provenance graph `(G_claim,P_claim)` with fields `fs_role` and `selected_conversion`; physical-amplitude Hessian identity `H_FS`; sealed corpus-defined `preseal_sources`; query `q_silent_conversion`; fixed mutation grammar/certificate `(G_conversion,p_conversion)` enumerating factor-two, factor-four, and later-coefficient mutations; expected mutation ledger `E_conversion` with result `REJECTED`; constants `DOWNSTREAM_HESSIAN_CHECK_ONLY` and `NONE` | `r_dag:=DAG(G_claim,P_claim)`; `r_fs:=COMPARE(G_claim.fs_role,DOWNSTREAM_HESSIAN_CHECK_ONLY,empty)`; `r_selected:=COMPARE(G_claim.selected_conversion,NONE,empty)`; `r_m2:=M2(q_silent_conversion,preseal_sources)`; `r_hessian:=EXACT(Hessian(physical_amplitude)=H_FS)`; `r_mutations:=ENUM(G_conversion,p_conversion)`; `r_mutation_ids:=COMPARE(r_mutations.ids,E_conversion.ids,empty)`; for every `m` in `r_mutations.items`, `r_m:=EXACT(m)` and `r_cmp_m:=COMPARE(r_m.normal_form,E_conversion[m],empty)` | `P0 and r_dag.success and r_fs.success and r_selected.success and r_m2.success and r_m2.hits=empty and r_hessian.success and r_mutations.success and r_mutation_ids.success and (for every m in r_mutations.items: r_m.success and r_cmp_m.success)` |
```

Criterion identity: the after display preserves the same claim/provenance DAG,
downstream-only FS Hessian check, silent-conversion exclusion, and rejection of
factor-two, factor-four, and later-coefficient mutations. It does not weaken,
reverse, add a favorable target, or change the row class. It renders each
existing demand as a named receiver and makes mutation coverage finite and
enumerated.

The existing Builder-A parser was exercised read-only against that procedure.
Its dry-run output was:

```json
[{"opcode":"DAG","repeatable":false,"result_name":"r_dag"},{"opcode":"COMPARE","repeatable":false,"result_name":"r_fs"},{"opcode":"COMPARE","repeatable":false,"result_name":"r_selected"},{"opcode":"M2","repeatable":false,"result_name":"r_m2"},{"opcode":"EXACT","repeatable":false,"result_name":"r_hessian"},{"opcode":"ENUM","repeatable":false,"result_name":"r_mutations"},{"opcode":"COMPARE","repeatable":false,"result_name":"r_mutation_ids"},{"opcode":"EXACT","repeatable":true,"result_name":"r_m"},{"opcode":"COMPARE","repeatable":true,"result_name":"r_cmp_m"}]
```

This is a non-authoritative conformance display, not a spec issue or package
mutation.

### 2.4 Custody stop

The selected repair cannot lawfully ship whole in this lane alone. `CV2-05b`
assigns the required producer-carried / independently-R9-resolved / missing
total-assignment verdict carrier, its negative tests, verifier schemas, root,
manifest instance, and dependent boundary pins to the independent Builder-B
contract-and-replay subgate before any additional envelope is admitted.
Codex 2 cannot rewrite Builder B's sealed package or self-certify that
independent replay surface. Issuing only V013 and the A-side re-pin would create
the forbidden half-state.

Accordingly no descriptor, spec, check map, A/B package, schema, root, instance,
or boundary pin was changed. The value-and-name census over the current A/B
packages found 81 prospective closure hits: 40 occurrences of the V012 spec
name, 38 of its digest, and 3 of the V010-14 row digest. All 81 are displayed
as the bounded future closure set; zero were mutated under this custody stop.

## 3. Battery and limits

`F_PLDEC`: CLEAN. The build serializes only abstract line carriers, induced
forms, and abstract unitary morphisms already licensed by sealed structural
bytes. It does not evaluate a physical quantity.

M-2: the decision, Gate-3 sources, packet source, U7 report, box delta, V012
row, generated instance, line payloads, schemas, and inventory were checked by
fixed-string, whitespace-normalized, scope-self-reference, and
hyphen/space/underscore surfaces where applicable. Content digests and exact
span digests, not path spellings, are authoritative.

Admission remains barred. `PASS_COMPONENT_BUILT` is only a schema-component
compile outcome; the C-B-V009-01 row remains partial, the C-B-V010-14 repair is
not issued, the board is unchanged, and no evaluator chain was invoked.

Verb audit under the verdict-line scope rule: CLEAN. “Built” means the ruled
P-B component bytes exist and compiled against their closed schema. “Choice”
identifies the smaller surface delegated by the relay. “Custody stop” records
the independent Builder-B boundary and does not claim a repair, proof, row
PASS, admission, authorization, or seal.

INSTANCE = built per P-B (Gate-3 form cited; inclusions displayed)
COMPILE = PASS_COMPONENT_BUILT (component only; row status PARTIAL_CARRIER_READY_ALIAS_CORPUS_ABSENT)
RECEIVER = descriptor-owned explicit receivers (smaller surface justified; custody stop)
PIN_CLOSURE = 81 hits enumerated, 0 mutated (custody stop)
ADMISSION = barred, stated
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
