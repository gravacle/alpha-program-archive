# STAGE 8 / AXN-CONSTRUCT-O5 — THE LIGHT-CONE LEMMA
## SPACELIKE CAUSAL FACTORIZATION FOR THE INTERACTING FINITE-CELL PARENT — CODEX 2 V001

Relay 822. `PICKUP-ACK` and lane guard passed: the sealed inbox names CODEX 2.
`ALL HEADLINE ITEMS ARE CLAIMED.`

## 0. Custody, jurisdiction, and gates

The unique inbox file was verified at its adjacent seal before its body was
read. `relay_outbox/822_ACK.md` was written before task work. The required
state brief `PROGRAM_STATE_BRIEF_V005.md` =
`e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`
verified `OK` and was read first.

Dario's governing relay-820 audit
`STAGE8_AXN_COMPLETION_AUDIT_DARIO_V001.md` =
`3e7e3a96f757a1ea5cd7d7f0a49476ea4f9ca96713558937f7422c8431553f09`
verified at its adjacent seal before reading. Its O5 finding is at lines
152–171, bytes `[9660,11285)`, span SHA-256
`b3e005c5f1cf3888bc56641420bd1dbc5685141a0d0e1ef94bf40ff4dad0957b`:
the missing object is “a derived spacelike causal-factorization/light-cone
lemma for the interacting finite-cell parent.” Q-727 was then verified in the
sealed `QUESTIONS_SETTLED_REGISTER_V001.md` =
`231288dd9d518a081d935bb0d269c1985e5bac94a132825c46a0a7915affb972`.

The parent was read **only** from the packet copy required by the relay:

```text
review_packets/STAGE7_QSPEC_CANDIDATE_V001/
  R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md
SHA-256 = 345d447eaf6d730caa6fa655b92a7b0cd93a68b5f86e0c8929cf969f40aeb7cb
packet-manifest verification = OK
```

No workspace-root copy, parent spec, producer code, or unsealed substitute was
opened or consulted. Law 8 was also applied before reading the ARCH/CDL/RED
stock:

| Source | SHA-256 | Seal mode/result |
|---|---|---|
| `CAUSAL_DIRECT_LIMIT_ARCHITECTURE_TEST_SPEC_V001.md` | `e8635914554741333f05db3fea8b055bfb76df2cfca322c1c177c53a99a50317` | group sidecar `OK` |
| `CAUSAL_DIRECT_LIMIT_ARCHITECTURE_ADJUDICATION_RESULT_V001.md` | `9be3f55fd527b9a857bdd4ea2298105e44a69e85db79b90772ecb30001aba022` | group sidecar `OK` |
| `CAUSAL_DIRECT_LIMIT_RECORD_PRINCIPLE_V002.md` | `7333204581ef3183665c9dd056d79f2caa073724e3566295ab888ccc5494c53a` | adjacent sidecar `OK` |
| `CAUSAL_DIRECT_LIMIT_REDUNDANT_RECORD_SPEC_V001.md` | `e335d2590dd16f13bd7b42d2ec43338fb6d41e298914e8fc659bc4a595ca70ff` | group sidecar `OK` |
| `CAUSAL_DIRECT_LIMIT_REDUNDANT_RECORD_RESULT_V001.md` | `3359960fb411eff8ac0360a8c052bfc4d00a6281bd151c390fa3addd3603d05a` | group sidecar `OK` |

The prior U_Omega typing report was carried at its sealed status, not treated
as independent verification of this lane's own work:
`STAGE8_C1_U_OMEGA_TYPED_CODEX2_V001.md` =
`fd21ed03b04df73f3d32af466d12dc46b8e700e7fb4e1c787392b929113245e1`,
seal `OK`.

Gates declared and held:

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_bound = false
fixed_point_executed = false
end_test_run = false
physical_quantity_numerically_evaluated = false
measured_constant_compared = false
smooth_lightcone_imported = false
EM_identification = false
```

PE-1 through PE-11 remained pointer-only: unopened, unconsulted, and assigned
zero verdict weight. No register, plan, tracker, git, production, response,
or chain action was taken.

## 1. The exact target and its receivers

Let `(C, prec)` denote the finite incidence causal order of primitive cells.
The only light-cone relation derivable without importing smooth geometry is
the order-native concurrency relation

```text
c || d  iff  not(c prec d) and not(d prec c).
```

This definition names incomparability. It does **not** itself prove that the
interacting parent assigns causally disjoint operator supports to `c` and `d`,
and it does not prove that their operations commute on the shared source.

The requested O5 theorem has three distinct receivers:

```text
LC1  INCIDENCE-TO-SUPPORT:
     the parent derives for each primitive cell c a cell-operation carrier
     (S_c,L_c or W_c) and its incidence-causal support Supp(c);
     c || d forces Supp(c) and Supp(d) to be causally disjoint in the
     incidence order itself.

LC2  PARENT MICROCAUSALITY:
     for every c || d, the source-inclusive parent operations commute
     (equivalently, their local generators strongly commute on the common
     invariant domain at all relevant cell parameters).

LC3  FACTORIZATION / ORDER INDEPENDENCE:
     LC2 makes the finite evolution factorize and makes every two linear
     extensions differing only by concurrent-cell swaps produce the same
     parent propagator.
```

LC1 is geometry/support. LC2 is an operator theorem. LC3 is the algebraic
consequence. A sentence declaring “local causal composition” cannot be sent
to all three receivers.

## 2. Sealed supply, without receiver flattening

| ID | Sealed span | What it actually supplies | What it does not supply |
|---|---|---|---|
| P1 | packet parent lines 5–28, `[77,774)`, SHA `5686572af79254546723dfa42a8f205763e871026288dd8fa33021be667ba937` | one finite parent; one shared charged source; distinct record factors; common self-adjoint domain; unique finite propagator; compact-support Møller maps | no map `c -> Supp(c)` and no incomparable-cell commutator |
| P2 | packet parent lines 47–70, `[1066,1863)`, SHA `c096269069e028c428fe9941f0b97db9d9a6780d8cfc4df05b3b97ee0b17c6c8` | generated overlap/closure descendants from one first-order parent | no proof that those descendants split into commuting cell suboperators |
| P3 | packet parent lines 72–105, `[1864,3023)`, SHA `2a903f50b1113fddf9ad5c0eb9560a2d940b409c62d68247d3834cd265edcc5e` | finite evolution, order sensitivity for causally overlapping cells, source-dressed incoming representation | a biting overlap control, but no result for incomparable cells |
| P4 | packet parent lines 126–142, `[3687,4301)`, SHA `3ed3de02d79d8882e20eee83f09e83cab3779cb27c4f9bc2372f8dab124ef4e1` | compact support at finite-cell scope and quasi-local record compatibility; later cells keep acting on the shared source | compact support is not support disjointness; record compatibility is not source-inclusive commutation |
| A1 | ARCH spec lines 86–108, `[2180,2702)`, SHA `06db450a8e6ad984ceb70ade36e67d4d59baf71e3fcb7c07ec73b6c08360853e` | “local causal composition” is a selector criterion for the architecture class | it is an input criterion, not an LC1/LC2 proof |
| A2 | ARCH result lines 15–35, `[349,1514)`, SHA `3e2103fb763b650c9058f7d568bcb168b53e021b56dd22981c685c53cb1fe13b` | Lorentz-covariant causal-complex **class** survives | no unique complex, refinement, support map, or cell commutator |
| A3 | ARCH result lines 73–118, `[2692,3886)`, SHA `2503173a675d82408a132b1eef370c822360560dca3df2647800d855c822ecc5` | bounded-incidence direct-limit theorem for the global incidence generator | strong convergence of global compressions is not local causal factorization |
| C1 | CDL v002 lines 5–30, `[63,1274)`, SHA `ee17cf9c98f9080ab0d3b282517957067f188c01fe349b99bf7dc0c7e3274ae0` | exact record compatibility only for causally sequential exhaustions | explicitly says arbitrary concurrent cells require the missing O5 lemma |
| R1 | RED spec lines 5–27, `[77,907)`, SHA `d7763c8031cc0514c35ae66bf73f97a18c466364152846bb252043f98e129fda` | adopted controlled-write formula; acyclic ready-cell architecture; “no causal support” gates declared commuting | the primitive write and interaction-window rules are inherited/adopted, not parent-derived |
| R2 | RED result lines 45–60, `[1003,1737)`, SHA `42a5e13d97ec32f53e0afbb8f120a0ed5d9e2255f0c6b5a769c017b195de98f2` | spacelike-disjoint **controlled writes** commute; linear-extension independence at that scope | it expressly does not derive the primitive controlled-write rule and does not complete the parent |
| R3 | RED result lines 62–77, `[1738,2334)`, SHA `99f699f6415803178cac254b7e48a45c970a4157b625e27615f160ac00dde12f` | `causal_linear_extension_independence_scoped = true`; parent/write derivation flags remain false | no promotion from adopted write to interacting parent |

The CDL status block at `[1275,1737)`, span SHA
`d2eb634f737060c32597ec56ff5d788895385b39f216d0796bc79c595d6c8a45`,
is decisive corroboration:
`spacelike_concurrent_extension_derived = false`.

## 3. The part that is derivable — displayed proof

### 3.1 Order-native concurrency

Because the RED architecture is a finite future-directed acyclic complex, its
transitive causal relation is a partial order. The relation `||` above is
therefore symmetric and irreflexive. No smooth cone, metric, continuum
cellulation, or preferred foliation is needed. This derives only the
**combinatorial concurrency class**.

### 3.2 Exact controlled-write commutation at RED scope

For a cell `c`, write the adopted RED gate on the source pointer and the
cell's own record factor as

```text
U_c = P_0 tensor I_c + P_1 tensor X_c,
```

with identities on every other record factor. For two distinct record cells
`c,d`, the pointer projectors obey `P_h P_k = 0` for `h != k` and
`P_h^2=P_h`; `X_c` and `X_d` act on distinct record factors. Hence

```text
U_c U_d
 = P_0 tensor I_c tensor I_d
   + P_1 tensor X_c tensor X_d
 = U_d U_c.
```

This is an exact algebraic proof of RED's commutation sentence for its adopted
controlled writes. It uses no decay, no continuum geometry, and no target.

### 3.3 Linear-extension invariance

For completeness, the order step is also displayed. Any two linear extensions
of a finite poset are connected by adjacent swaps of incomparable elements:
compare their first elements; move the first element of the second extension
leftward in the first extension. Every crossed predecessor must be
incomparable—if it preceded the moved element in the partial order, it would
also have to precede it in the second extension. Remove the common first
element and iterate. Each swap therefore exchanges a pair `c || d`.

At RED scope, §3.2 says each exchanged gate pair commutes, so every swap leaves
the circuit product unchanged. Induction over the swaps gives the same circuit
for both linear extensions. This proves LC3 **only for the adopted RED gate
family after its no-causal-support condition is already satisfied**.

## 4. The interacting-parent derivation stops — exact failing step

### 4.1 What must be sent into the proof

To promote §3 from the adopted RED model to the requested interacting parent,
the sealed parent must emit at least this carrier:

```text
rd22.parent-incidence-microcausality.v001 = {
  cells: finite incidence-poset cells,
  per_cell: [{cell_id, operator_or_generator, incidence_support,
              common_domain_binding, parent_provenance}],
  support_theorem:
    c || d -> incidence_support(c) causally_disjoint incidence_support(d),
  operator_theorem:
    c || d -> COMMUTE(parent_operation(c), parent_operation(d)),
  write_identification:
    the RED controlled write is the restriction induced by that same parent
}
```

This is a typed description of the missing proof receiver, not a newly adopted
schema or axiom.

### 4.2 The exact failure

The packet parent emits one shared charged source, distinct record factors, a
common self-adjoint domain, one finite propagator, and finite compact-support
Møller maps. It does **not** emit the per-cell operator/support rows above. In
particular, no sealed statement proves either implication

```text
c || d  ->  parent supports are incidence-causally disjoint;       [LC1]
c || d  ->  parent source-inclusive operations commute.            [LC2]
```

The proof therefore stops before the first parent-level commutator can be
formed. The absence is substantive because both operations act through one
shared source. Distinct record factors alone commute; whole cell operations
need not.

The exact algebraic failure surface can be displayed without binding a member.
For generic source operators `A_c,A_d` and distinct record-factor operators
`R_c,R_d`, a source-inclusive local form has

```text
L_c = A_c tensor R_c tensor I_d,
L_d = A_d tensor I_c tensor R_d,

[L_c,L_d] = [A_c,A_d] tensor R_c tensor R_d.
```

If the parent equations force `[A_c,A_d]=0`, factorization follows; if they do
not, record-factor separation does not help. The supplied parent result names
neither `A_c,A_d` nor a theorem forcing their commutator. This is an
underdetermination schema, not a claimed counterexample to the actual parent.
The absent complete parent equations may still force LC1 and LC2.

### 4.3 Verdict for O5

The order-only relation and adopted-RED factorization are derived. The
interacting-parent light-cone lemma is **not** derived. It is not classified as
a no-go: no sealed parent instance violates it. The truthful disposition is
therefore `PARTIAL`, scoped to the finite incidence order plus the adopted RED
controlled-write family, with the parent-level failure typed as
`PARENT INCIDENCE MICROCAUSALITY MISSING`.

The CDL concurrent-cell extension remains open. A later proof must fill LC1
and LC2 from the packet parent's own operator construction; citing RED's
assumption or a smooth microcausality principle would be circular.

## 5. U_Omega co-benefit — adjacency tested, identity declined

The sealed U_Omega proof skeleton requires the complete parent to derive a
Lorentz-equivariant causal tip pair or equivalent cell carrier for each
primitive incidence, contain the cell interaction support in that carrier,
and prove any second parent-admissible output equal. Its exact missing lemma is
`PARENT-CAUSAL-CELL FUNCTIONALITY` (prior report lines 173–240,
`[13000,15789)`, span SHA
`e6449a530e27ea28aa0c7d0887f79c3f2026eec92ea19ed89eea46d7faa1f41a`).

The O5 and U_Omega gaps touch at the absent incidence-to-support carrier:

```text
O5 needs:      incidence -> support + disjoint-support commutation.
U_Omega needs: incidence -> tip pair/cell + support containment + uniqueness.
```

But neither theorem implies the other:

- even a unique tip pair does not make two shared-source operators commute;
- even commuting incomparable-cell operations do not select a tip pair,
  invariant anchor/interval, or prove assignment uniqueness.

The machinery in this relay derived no tip pair and no uniqueness statement.
`U_OMEGA_COBENEFIT = adjacency only.` The common missing carrier is displayed;
the two theorem receivers remain separate.

## 6. FREEDOMS-CONSUMED

```text
CARRIED, NOT CONSUMED:
  the packet-sealed finite parent and its one shared source
  the ARCH causal-complex class
  the CDL causally-sequential scope
  the adopted RED controlled-write family
  the finite incidence partial order

DERIVED HERE:
  order-native concurrency as poset incomparability
  exact RED controlled-write commutation at its adopted scope
  linear-extension invariance from adjacent incomparable swaps at that scope

NOT SELECTED OR ADOPTED:
  no causal complex or refinement member
  no smooth spacetime/light-cone model
  no cell tip pair, anchor, interval, or diamond assignment
  no source operator pair
  no parent microcausality axiom
  no interaction-window rule
  no identification of the adopted RED write with the interacting parent
  no U_Omega uniqueness output

SCALING WEIGHTS CONSUMED = none
SUBSTITUTIONS = none
```

## 7. FLATTENING CHECK

The 37-row decline register was checked at its sealed digest
`957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a`.
The two relay-named rows remain live:

| Row | Fence | Result |
|---|---|---|
| S19 | Decay may not be inferred from masslessness/gaplessness. Registered source span `[9317,9726)`, SHA `0f85bc90ffbaf0c0b8ddb02f6acb6deb7ebe5685ac8e905101575d48a6b74d4b`. | **LIVE / CLEAN.** No decay proposition appears in the proof. ARCH return-decay stock is not used as microcausality evidence. |
| S26 | `C_ref` is barred as a source and may be used only as an audit/target interface. Registered source span `[24860,25338)`, SHA `14b17738bd9df6ec36cae2a9b6a25c9b9d6d1f8e9ddc5b3a6e320d1089f6fbab`. | **LIVE / CLEAN.** Concurrency is defined only by incidence-order incomparability. No smooth cone, manifold, cellulation, or `C_ref` fact is imported to prove LC1/LC2. |

Additional receiver checks:

- “Lorentz-covariant causal-complex class” is not flattened into one selected
  complex or one support map.
- “compact support” is not flattened into spacelike-disjoint support.
- “distinct record factors” is not flattened into whole-operation commutation
  on a shared source.
- RED's adopted-write theorem is not flattened into a theorem of the parent.
- order sensitivity for overlapping cells is a negative control, not a proof
  that incomparable cells commute.
- U_Omega adjacency is not flattened into theorem identity.

`FLATTENING_CHECK = clean; S19 and S26 live.`

## 8. Battery, pin check, and verb audit

F_PLDEC passed: no physical quantity was evaluated, no target or measured
constant was used, and no physical response was produced. M-2 covered exact
phrase, hyphen/reflow, flag/status, and semantic-equivalent forms. Anti-tuning
passed. The light-cone relation used in the partial result is incidence-native.

PRE-SEAL PIN CHECK: the output and sidecar names were absent before writing;
the parent packet member returned `OK`; every ARCH/CDL/RED group or adjacent
seal returned `OK`; every displayed byte span was rehashed from its sealed
source. The output sidecar is generated only from the final bytes.

Verb audit scope includes headings, prose, tables, displays, and final lines.
Every use of “derived” is restricted to the sealed stock or the two scoped
algebra/order consequences proved in §3. The requested parent theorem is
called partial/open, never proved. “Spacelike” in the partial theorem refers
only to RED's own sealed controlled-write scope; the new order relation is
called concurrency/incomparability. No authorization, member, smooth
geometry, response, or coupling is claimed.

LEMMA = partial (order-native concurrency + adopted RED controlled-write factorization only; interacting-parent LC1/LC2 remain open)
U_OMEGA_COBENEFIT = adjacency only
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
