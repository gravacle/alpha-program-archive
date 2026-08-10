# STAGE 8 / [PLAN:AXN-BUILD-A12] — EXIT-B SCHEME CROSS-CHECK
## CODEX 2 LANE — V001

**Date:** 2026-08-09  
**Status:** CLAIMED — every headline awaits the opposite lane's adversarial pass.  
**Subject:** `STAGE8_AXN_BUILD_EXITB_SCHEME_DARIO_V001.md`, SHA-256 `37b499b65875b764f78eca132c22eb4c248ed4dc6546faab9d49fbc28699967f`.  
**Scope:** PASTE 845 only: source-resolution of SC5, the SC4 supplier hunt, B0/C0 typing, P1 algebra, and the restricted-Exit-B scope.  
**Custody:** cleanroom-only write; registrar mirrors. This lane checks Dario's claimed construction and does not upgrade its own claims.

---

## 0. Preflight and pins

The relay seal was verified before reading; `845_ACK.md` was written before the relay was opened. The pinned state brief was then verified and read.

| Object | SHA-256 | Result |
|---|---|---|
| `PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | PASS |
| `LOCKED_PROCESS.md` | `eae8f9d6f44ef1611b69cbc7d7bac735f7cfde44b6b1c3a2f4af6f1504a54066` | PASS |
| `DECLINE_REGISTER_V002.md` | `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | PASS |
| `AXN_BUILD_CHARTER_V001.md` | `c0ad6decf156ef06c34bc8886d433487dfdf518c650dd67d5de283febeb14542` | PASS |
| Dario 844 subject | `37b499b65875b764f78eca132c22eb4c248ed4dc6546faab9d49fbc28699967f` | PASS |
| Codex 843 Exit-A hunt | `f27d6fa3c91d0169e7058aa341474955595943d0fa9643cb504442c1297f10ac` | PASS |

The questions-settled register was searched before analysis. Q-748 records Dario 844 as CLAIMED and expressly sends the second-hand SC5 citation, SC4 absence, B0/C0 path, and P1 to this relay. `PE-1` through `PE-11` remained pointer-only; their contents were not opened or consulted.

Gates carried throughout:

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_binding = false
fixed_point_executed = false
end_test_executed = false
physical_numeric_evaluation = false
measured_constant_comparison = false
smooth_import = false
electromagnetic_identification = false
```

---

## 1. SC5 citation resolved at the BID source

### 1.1 Custody and exact bytes

The primary file is `BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md`, SHA-256

```text
b00683c2c7a508a0fec7f2fe089ce64656bd4de832b8c8f189ce1c1007157dd6
```

That digest is a content-addressed authority member in the sealed `COMPLETE_QSPEC_ABSOLUTE_SCALE_AND_CONTINUUM_PREREQUISITE_AUDIT_V001.md`, SHA-256 `ef36122c1592e96328e1d5a5799f91fedb126c50e01e349ca2797684b538c754`, lines 156–170. The direct source's lines 171–185 are bytes `[5092,5750)`, SHA-256 `c39637da92f79af93d90cadb4f84e8f05677bf73a8d16cc8303786bd064c69ba`:

```text
Stage 3 closes only when one target-independent complete source-record-
gravity action:

1. fixes the global/subregion boundary terms and time-flow vector;
2. derives the CTP Hamilton-Jacobi energy;
3. proves that this energy is constant on the first durable-record saddle;
4. proves that it equals the gravitating energy entering the closure
   condition;
5. derives the baseline/reference subtraction and excludes spectator
   energy;
6. derives, rather than assumes, the marginal closure condition; and
7. yields one isolated stable positive `T_R/t_P`.

Until then the causal-cell formulas are exact conditional algebra, not an
absolute scale derivation.
```

Dario's second-hand source was `STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md`, SHA-256 `2d63dfadbb741c467b812f21e14f9e0e66015f1d86e2aa8307d8ae77acfe3d69`. Its bytes `[25236,25776)` reproduce SHA-256 `27534a51dd8d10462b2d73e83c6a439feea35e6f66de5dea1b294d4ab54f772c` and accurately report the BID source, although that span itself stops mid-word. The direct source above supplies the complete sentence.

**Citation verdict:** supported as a quotation and as a condition for **Stage 3's absolute-scale closure**.

### 1.2 The direction the source does—and does not—license

The gate's own opening statement is narrower than Dario's inference. At lines 16–31 it says that a Hamilton-Jacobi relation is available for a completely specified package containing:

```text
Lorentzian CTP action;
state;
boundary conditions;
time-flow vector.
```

The exact closure block then requires one complete action to fix the global/subregion boundary terms and time-flow **as one conjunct among seven needed to derive the absolute interval**. It does not state either of these universal claims:

```text
every variational problem receives its boundary prescription only from a complete action;
every restricted primitive-incidence variation needs the entire Stage-3 package.
```

The first would reverse a sufficient Stage-3 package condition into an exclusive source theorem. The second would erase the distinction between SC5's restricted calculus and the HJ scale bridge. Neither inference appears in the primary bytes.

Therefore the direct citation supports the gate, but **refutes its use as proof of the claimed second circularity**.

---

## 2. The dependency graph: the two loops do not close through the same object

### 2.1 The first loop

The first loop remains exactly as 842/843 typed it:

```text
H1 needs a record-sector integrand whose output meets C2-C6;
pulling C2-C6 back needs U1 on an admissible integrand class;
the sealed stock supplies neither the complete candidate nor that class-wide map.
```

Its missing action-side object is `S_record` inside the complete action.

### 2.2 The SC5 supplier graph at source

The sealed CTP package lineage names a different forward graph. `STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md`, SHA-256 `ec848d293d0d824150c21b252452ae46732705cf972c857c2dc02671af53878c`, states:

```text
B0 = COMPLETE_MICROSCOPIC_BOUNDARY_OPERATOR
B0 -> C0
(B0,C0) -> U1,U2,U3
```

and requires the state, action, carrier, sources, quotient, measure, and domains to descend from B0 (lines 830–860 and 977–1000). Its type block is explicit:

```text
B0 = a complete microscopic source-record-field boundary operator/dynamics role;
B0_CONSTRUCTION_WITNESS = false | TYPE-U;
the action is a descendant datum, not B0 itself;
U3 boundary/edge data are another descendant datum.
```

The boundary-data requirement is independently recorded by:

- `STAGE8_CTP_PHYS_INPUT_PACKAGE_ITEM1_WORD_BOUNDARY_TRIAGE_REVERIFICATION_V001.md`, SHA `ebdad2b9…`, lines 450–475: global skeleton partial; complete boundary/edge data TYPE-U; would-build from B0/C0;
- `STAGE8_CTP_PHYS_INPUT_PACKAGE_TRIAGE_AND_LOAD_BEARING_FUNCTIONAL_SPEC_V001.md`, SHA `498a5bf2…`, lines 669–699: common domain, preparation/gluing variation, boundary orbit, edge variables, reductions, and boundary functionals remain incomplete;
- `STAGE8_TASK4A_P3_COMPLETE_U3_PACKAGE_CONSTRUCTION_AND_FOUR_FIELD_STOP_V001.md`, SHA `f97ee43e…`, lines 331–360 and 540–554: source glue exists, but it is TYPE-R as the complete CTP boundary package; the complete boundary package remains TYPE-U.

This makes the lawful dependency:

```text
unbuilt B0 construction witness
  -> B0 boundary operator/dynamics
  -> C0 and U3
  -> complete_CTP_boundary_edge_data
  -> a possible SC5 boundary prescription
```

That path is **licensed but uninhabited**. It is not the complete action: the complete action and U3 boundary data are distinct descendants required to share B0 provenance. A named supplier is not a discharged carrier, so SC5 remains stopped. But a future, acyclic supplier path is enough to refute the statement that SC5 can close **only** through the action H1 is trying to derive.

### 2.3 Second-circularity verdict

```text
FIRST LOOP OBJECT  = missing S_record / action-to-receiver map.
SC5 SUPPLIER       = unbuilt B0 -> C0/U3 -> boundary-data descent.
IDENTITY           = false; action and boundary-data package are sibling descendants.
```

The second circularity is therefore **broken as a dependency-graph claim**. The construction is not thereby complete: SC5 remains TYPE-U on an unbuilt B0/C0/U3 path. This is the exact not-a-kill reading licensed by the sources.

---

## 3. SC4 supplier hunt under law 9

### 3.1 What counts as an SC4 supplier

For `X_prim`, a complete supplier must jointly bind:

```text
R1  carrier: the primitive record-incidence densities L_c;
R2  an admissible function/topological space for those L_c;
R3  tangent/admissible variations in that same space;
R4  boundary/trace behavior on the closure faces;
R5  enough regularity for the variation map into H1's receiver to be defined.
```

This is the complete requirement enumeration searched. A source-space calculus, an output-operator domain, or a requirement sentence is not an SC4 supplier unless it binds all five to `L_c`.

### 3.2 Search universe and M-2 probes

```text
SEARCH ROOT:
  alpha_fundamental_record_action_cleanroom_v003/

RECURSION / FORMATS:
  recursive; *.md, *.json, *.txt, *.csv, *.tsv, *.yaml, *.yml

EXCLUSIONS:
  relay_inbox/**, relay_outbox/**, rd22_run_*/**, **/a32_custodian_private/**,
  expectation-ledger material, live tracker, questions-settled register,
  and this not-yet-written report.

SEARCHED FILES = 2,030
BROAD MEANING-CANDIDATE FILES = 621
```

Writer-exclusion reconciliation: after this report was created, the same glob
returned `2,031` files and `622` broad candidates because the report contains
the probe vocabulary. Re-running with
`!STAGE8_AXN_BUILD_EXITB_CROSSCHECK_CODEX2_V001.md` restores `2,030 / 621`.
The writer contributes no evidence to its own absence finding.

The 621-file broad set is the union of fixed/normalized probes for:

```text
admissible integrand; integrand class; function space; action/variation/
variational domain; admissible variation; regularity; asymptotic decay;
compact support; fixed-boundary/Dirichlet; preparation/gluing variation;
common domain; Sobolev; C_c; Frechet/Fréchet; Gateaux/Gâteaux.
```

Raw fixed-string hit-file counts that controlled the close reading include:

| Probe | Files | Probe | Files |
|---|---:|---|---:|
| `admissible integrand` | 0 | `admissible-integrand` | 1 |
| `integrand class` | 1 | `function space` | 5 |
| `action domain` | 5 | `variational domain` | 1 |
| `variation domain` | 1 | `admissible variation` | 2 |
| `regularity` | 65 | `asymptotic decay` | 3 |
| `fixed at the boundary` | 2 | `preparation/gluing variation` | 11 |
| `Sobolev` | 14 | `Fréchet` | 11 |

M-2 modes were exact symbol/name, hyphenation and punctuation, line-wrap/case normalization, and meaning/receiver classification. Every positive was classified by carrier and status, rather than counted as an SC4 supplier by vocabulary.

### 3.3 Complete candidate-family enumeration after meaning classification

| Candidate family | What it supplies | Why it is not SC4 |
|---|---|---|
| Causal-cell global-domain lineage | Generic Cauchy data, “regularity and asymptotic decay,” a non-null Dirichlet gravity completion, and CTP gluing language; sealed triage SHA `ebdad2b9…` classifies the boundary package PARTIAL. | It does not define the record-integrand space, tangent variations, or the complete closure-face prescription. This **corrects** Dario's literal “no regularity condition exists” wording: generic regularity language exists, but no receivable SC4 class does. |
| Task-4A P2 source calculus | `E_src`, a Banach source space, complex Fréchet calculus, and `Reg_D1/Reg_D2`; `STAGE8_TASK4A_P2...V002.md`, SHA `40b2af34…`, lines 339–402 and 589–604. | It varies source parameters `J,R`, not action densities `L_c`. P3 expressly says source Fréchet differentiability is not an endpoint operator/domain theorem (SHA `f97ee43e…`, lines 372–383). Retyping it would be a carrier substitution. |
| Task-4A P3 / U3 partial package | Finite/source gluing and a provenance port. | Complete boundary/edge data and unbounded domains remain TYPE-U; it explicitly refuses the identification with the complete CTP package. |
| R3.4 packet operator domain | Common self-adjoint domain and smooth-envelope limit for `h_K/D_K`. | Receiver-side `Y`, not integrand-side `X`; 843 already barred this inverse promotion. |
| Skeleton Euler derivative | A bulk derivative “with the variation fixed at the boundary.” | Its own source calls that a formal consequence, not a new boundary law (`STAGE8_AXN_BUILD_SKELETON_CODEX2_V001.md`, SHA `5a51b940…`, lines 327–335). |
| Cellular comparison/function-space artifacts | Pullbacks on finite cellular/cochain action presentations. | Comparison/refinement carriers, not the record-incidence functional class or H1 map. |
| Task-5 regular/Banach/Sobolev classes | Scalar-return, modulus, refinement, or completion spaces. | Different receivers and roads; no `L_c` binding. |
| CTP/action adoption proposals | Proposed contours, presentations, or action domains. | Proposals are not adopted suppliers; several explicitly retain missing domains. |
| Gravity variational-domain line | Names a certified global CTP variational domain as a would-build (`STAGE8_GRAVITY_MATTER_SOURCE_SUMMANDS_LIVE_V004_STANDING_V001.md`, SHA `58208084…`, lines 199–240). | TYPE-U requirement, not a supplied domain, and not record-sector `L_c`. |
| H1/Exit-A/Exit-B artifacts | State the exact missing integrand/action-domain problem. | Requirements and reports, not suppliers. |

No family satisfies R1–R5 jointly. The corrected conclusion is:

```text
SC4_COMPLETE_SUPPLIER = NONE-CONFIRMED.
PARTIAL_REGULARITY_OR_CALCULUS_FRAGMENTS = PRESENT, on other carriers or at TYPE-U scope.
```

This preserves Dario's stop while narrowing its overbroad absence sentence.

---

## 4. Fragment P1 — algebra confirmed, claimed consequence refuted

### 4.1 What is algebraically valid

For operators on a common domain,

```text
(sum_c A_c)^2 = sum_c A_c^2 + sum_(c != c') A_c A_c'.
```

For pointwise multiplication/local bundle endomorphisms, one also has the upper bound

```text
support(A_c A_c') subset support(A_c) intersect support(A_c')
                         subset Omega_c intersect Omega_c'.
```

That is all the displayed algebra forces.

### 4.2 Two failures in P1's inference

**First: overlap does not imply a nonzero cross term.** Even with `Omega_c intersect Omega_c'` nonempty, take local endomorphisms

```text
A_c(x)  = f(x) P,
A_c'(x) = g(x) Q,
P Q = Q P = 0,
```

with `f,g` both supported in the overlap. Then both supports meet there while both ordered products vanish. Scalar functions with disjoint sub-supports inside overlapping cells give the same counterexample. Therefore

```text
support(A_c A_c') subset overlap
```

does not imply “nonempty exactly on cell overlaps,” much less automatic production of the packet's required nonzero overlap descendants.

**Second: the closure-face term is not a cross term.** The sealed packet's square is (`R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md`, SHA `40890e75…`, lines 160–190):

```text
D_K^2
 = (i gamma^mu nabla_mu)^2
   - C_K^2
   - gamma^mu gamma^5 nabla_mu C_K.
```

`-C_K^2` contains the single-cell and overlap terms. The **separate derivative term** `-gamma^mu gamma^5 nabla_mu C_K` carries opening/closure-face support. Cross terms in the square do not by themselves establish that derivative-support descendant.

There is also a typing gap before either inference: `X_prim` contains densities `L_c`, while P1 assumes output operators `A_c` with local multiplication support. The missing SC5 map is precisely what must derive the latter from the former. P1 cannot assume its output before the map exists.

The packet's own finite parent does generate both descendant classes, but that is an instance in `Y`; it does not prove every `X_prim` member does. Thus P1's algebraic expansion and support upper bound survive, while its advertised conclusion—“C5 is automatically generated and is not an obstruction”—is refuted. Sufficiency remains unshown, exactly as Dario cautioned.

---

## 5. Restricted Exit-B scope

843's type partition expressly says that a map defined on a class **or subclass** so that C2–C6 can be pulled back is restricted Exit B. Dario's

```text
X_prim := families {L_c}, one density per primitive incidence,
          support(L_c) subset Omega_c
```

is therefore a lawful restricted-Exit-B analysis surface because its support typing is the one domain-side content the sealed H1 correction supplies. Dario also says the effective/nonprimitive remainder is unbounded and out of scope and makes no exhaustion claim. That scope declaration is honest.

Two qualifications remain load-bearing:

1. selecting `X_prim` as the analysis subclass does not select it as the physical or exhaustive action stratum;
2. until SC4 and SC5 are supplied, it is a typed set description, not the domain of an executable variation map.

The restriction stands; P1 does not strengthen it.

---

## 6. Corrected scheme ledger

| Component | Cross-check verdict |
|---|---|
| SC1 receiver `Y` | CONFIRMED forced; `w(s)` remains receiver-side. |
| SC2 domain | CONFIRMED not class-wide specifiable; `X_prim` restriction licensed and honestly nonexhaustive. |
| SC3 support typing | CONFIRMED at primitive scope; support, not form. |
| SC4 function space | STOP CONFIRMED, but absence wording CORRECTED: generic/source/operator regularity fragments exist; none binds the complete R1–R5 record-integrand class. |
| SC5 variation/boundary | STOP CONFIRMED as TYPE-U; CIRCULARITY REFUTED. The HJ citation is Stage-3-specific, and the licensed B0→C0/U3 supplier graph is distinct and unbuilt. |
| SC6 pullback | BLOCKED. P1's expansion survives only as an upper-bound identity; its automatic-C5 consequence is REFUTED. |

The resulting H1 system remains gated, but on two **unbuilt suppliers**, not on a proved second cycle:

```text
SC4 = no complete admissible L_c function/tangent space of record;
SC5 = no instantiated B0/C0/U3 boundary prescription of record.
```

---

## 7. Freedoms consumed and flattening

### 7.1 Freedoms consumed

| Datum | Treatment | Scope |
|---|---|---|
| `X_prim` | CARRIED-AS-PARAMETER | Restricted analysis surface only; not selected as exhaustive or physical. |
| effective/nonprimitive record sector | CARRIED-AS-PARAMETER | Remains unbounded and out of this restricted scheme. |
| SC4 topology/function space | CARRIED-AS-PARAMETER | Missing; P2 source calculus not substituted. |
| SC5 boundary prescription | CARRIED-AS-PARAMETER | Missing; neither Dirichlet, free, compact-support, nor edge prescription chosen. |
| B0 construction witness | CARRIED-AS-PARAMETER | TYPE-U; the licensed path is not called inhabited. |
| C0/U3 boundary package | CARRIED-AS-PARAMETER | TYPE-U/partial; no status flag promoted to data. |
| packet common domain and descendants | CONDITIONED-ON | Cited only as receiver-side target/instance. |
| `w(s)` and its scaling | CONDITIONED-ON | Exact packet envelope only; not an integrand or free weight. |
| P1 counterexample endomorphisms | CONDITIONED-ON | Structural falsifier of an implication, not adopted physical content. |
| any action member, coefficient, topology, boundary law, or physical identification | SUBSTITUTED | **NONE.** |

### 7.2 Flattening check

The complete 37-row decline register was walked.

| Row | Result |
|---|---|
| S03 / void condition | CLEAN — no function space, boundary law, B0 witness, or member selected to continue the build. |
| S08 | CLEAN — no discrete or CTP object identified with electromagnetism or a smooth public field. |
| S12 | CLEAN — TYPE-U and CLAIMED labels are not treated as their discharge objects. |
| S16 | CLEAN — source Fréchet calculus is not substituted for the action variation. |
| S19 | CLEAN — no durability or decay conclusion imported from generic regularity/asymptotic language. |
| S21 | CLEAN — no gravitational energy or time-flow convention chosen. |
| S24 | CLEAN — no clustering axiom used. |
| S25 | CLEAN — no equal-action, minimality, or reparameterization principle introduced. |
| S26 | CLEAN — no smooth comparison target or `C_ref` used as source. |

No other decline row receives a load-bearing identification here. `FLATTENING_CHECK = CLEAN (37/37)`.

### 7.3 Battery and self-audit

```text
F_PLDEC          = PASS
ANTI_TUNING      = PASS
M2               = PASS (four modes; receiver/status classification after hits)
LAW9             = PASS AT CLAIM SCOPE (R1-R5 complete supplier predicate + searched enumeration displayed)
PIN_CHECK        = PASS
PE_POINTER_ONLY  = PASS
```

Self-attack: the primary-source quotation is genuine, so the easy verdict was to preserve Dario's circularity. That would confuse “the complete action is required for Stage 3's seven-conjunct absolute-scale closure” with “the complete action is the exclusive source of every restricted boundary prescription.” The source does not say the latter, and the B0 graph says otherwise. A second easy pass was P1's support inclusion; the orthogonal-fiber counterexample and the packet's separate derivative-support term kill its advertised consequence. Both attractive passes were refused.

---

SCHEME = corrected (SC4 absence narrowed; SC5 stop retained but circularity removed; P1 consequence refuted)
SECOND_CIRCULARITY = BROKEN (licensed unbuilt B0 -> C0/U3 -> boundary-data closer displayed)
SAME_OBJECT = distinct (complete action and U3 boundary data are sibling B0 descendants, not identical)
SC5_CITATION = RESOLVED-SUPPORTED (direct bytes [5092,5750), SHA c39637da…; support is Stage-3-specific)
SC4_SUPPLIER = NONE-CONFIRMED (complete R1-R5 X_prim supplier; 2,030-file / 621-candidate enumeration displayed; partial other-carrier regularity exists)
B0C0_PATH = LICENSED (distinct upstream producer path, still TYPE-U/unbuilt; named supplier is not discharge)
P1 = refuted (square expansion/support upper bound valid; nonzero-overlap, closure-face, and automatic-C5 conclusions do not follow)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+5 scope controls: all headlines CLAIMED; direct citation separated from inference; named B0 supplier not called inhabited; SC4 absence limited to a complete receivable supplier; P1's surviving algebra separated from its killed consequence)
