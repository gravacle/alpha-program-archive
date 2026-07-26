# F-8 Independent Re-Derivation Return — Sealed Transcript
Claude lane · 2026-07-26 · verbatim return of the fresh-context re-derivation
lane discharging the first half of the F-8 gate on the re-scoped majorant arm.
The lane was forbidden to read any draft artifact authored by the claiming lane
(phase-1/phase-2 proof drafts and primary JSONs) — the exposure the reviewer's
audit named. VERDICT: ROUTE_Q_INDEPENDENT, reproduced from sealed text with
three adversarial refutation attempts, all failing. TWO NEW FINDINGS: the
sealed O1 display's literal (interleaved) reading is FALSE and the CTP-nested
reading is FORCED; and Q6 (uniform bounded cell-adjacency degree over D3) is a
NEW UNDERIVED obligation of Route Q, independent of E1.

---

FRESH-CONTEXT F-8 RE-DERIVATION LANE — RETURN

INDEPENDENCE ATTESTATION. I read no draft artifact of the claiming lane. Not opened: `stage8_execution/work/MAJORANT_LEMMA0_PROOF_DRAFT_V001.md`, `MAJORANT_PHASE2_O3_O7_PROOF_DRAFT_V001.md`, `T07_majorant_phase1_primary_v001.json`, `T07_majorant_phase2_primary_v001.json`, and no other `stage8_execution/work/` file. Every mathematical statement below is my own algebra, verified in exact arithmetic by code I wrote in this session. I made no writes anywhere under the cleanroom; all my files are under `/private/tmp/claude-501/-Users-bgm-MB-Work/578abe61-ea1d-48e6-8fb1-b06509d933a1/scratchpad/f8_rederive/`.

---

## 0. SEAL VERIFICATION (drift check; run before and after the work — identical both times)

| Sealed text | SHA-256 recomputed | adjacent seal |
|---|---|---|
| `STAGE8_T7_CONNECTED_LINKED_CLUSTER_MAJORANT_DERIVATION_SPEC_V001.md` | `818083a52165bc5c…f84e3` | MATCH |
| `STAGE8_T7_D6_SPECS_REPAIR_AMENDMENT_V001.md` | `60223e6a175c5fee…9e5d` | MATCH |
| `STAGE8_T7_MAJORANT_ARM_RESCOPE_PRINCIPAL_DECISION_V001.md` | `209aa39015c955e4…bb53` | MATCH |
| `STAGE8_T7_L2_INTENSIVE_HESSIAN_TYPING_FREEZE_V001.md` | `cdbacdaf5efcd3a7…4746` | MATCH |
| `STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md` | `789338adb7d3d36d…5bc3` | MATCH (= the spec's Phase-A row) |
| `STAGE8_T7_COMPLETED_CONDITIONED_DUHAMEL_IDENTITY_AND_INTERCHANGE_SCHEMA_SPEC_V001.md` | `4fe8d42dc8287…cb37` | MATCH |
| `STAGE8_T7_OPEN_EXHAUSTION_ATTACHMENT_AND_RELAY_NECESSITY_RESULT_V001.md` | `0df721a170f4f4a1…0694` | matches spec authority row |
| `STAGE8_T7_RELAYED_FAMILY_RESOLUTION_RESULT_V001.md` | `52401eefc3ff84e2…893d` | matches spec authority row |
| `BID_MONOIDAL_EXTENSIVITY_DERIVATION_V001.md` | `451550c382528…d46b` | matches spec authority row |

NO DRIFT. (Note for the record: two files unrelated to this lane appeared in the cleanroom during my window — `STAGE8_T7_Q2_TRIGGER_AND_CLASSIFICATION_STANDARD_V001.md` and its seal. Not mine, not read.)

Runtime: `/Users/bgm/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3` (3.12.13). No numpy/scipy used; no floats used anywhere. All arithmetic is exact in the field **Q(√2, i)** (implemented as `A + Bi` with `A,B ∈ Q(√2)`, closed-form inverses), files:
- `/private/tmp/claude-501/-Users-bgm-MB-Work/578abe61-ea1d-48e6-8fb1-b06509d933a1/scratchpad/f8_rederive/exact_field.py`
- `…/f8_rederive/lemma0.py` (30 checks, 0 failures, 14 s), output `…/f8_rederive/lemma0_out.txt`
- `…/f8_rederive/witness_extras.py`, output `…/f8_rederive/witness_out.txt`
- `…/f8_rederive/e1_ksea_scaling.py`, output `…/f8_rederive/e1_out.txt`

---

## 1. LEMMA 0 — RE-DERIVED, WITH THE FORCED READING DETERMINED

### 1.1 Objects, re-derived from A3 (not typed in)

From the sealed A3 qutrit `c = [[0,0,−i],[0,0,+i],[+i,−i,0]]` I computed `c² = [[1,−1,0],[−1,1,0],[0,0,2]]`, hence spectrum `{0, ±√2}`, and constructed the projectors and verified `P_λ² = P_λ = P_λ†`, `cP_λ = λP_λ`, `Σ_λ P_λ = I₃` exactly:

```
P_0 = (1/2)[[1,1,0],[1,1,0],[0,0,0]]
P_± = (1/4)[[1,−1,∓i√2],[−1,1,±i√2],[±i√2,∓i√2,2]]
```

```
p_λ = <ready|P_λ|ready> = ( 1/2 , 1/4 , 1/4 )      for λ = ( 0 , +√2 , −√2 )
w_λ = <pointer|P_λ|ready> = ( 1/2 , −1/4 , −1/4 )
m0  = Σ_λ w_λ = 0            EXACTLY  (= <pointer|ready>)
```

Two structural facts fall out and are load-bearing later:

- **(M-7, independently re-derived)** `w_λ = ε_λ p_λ` with `ε = (+1,−1,−1)`, because `(P_λ)₁₀/(P_λ)₀₀ = (v_λ)₁/(v_λ)₀ ∈ {+1,−1}`. Hence `|w_λ| = p_λ` for every λ — exactly the identity amendment M-7 records.
- **COLOUR-MASS-ONE (named block, new).** `Σ_λ |w_λ| = Σ_λ p_λ = 1` exactly, so the CTP branch-pair colour mass `(Σ_λ|w_λ|)² = 1` exactly. **The colour sum in a coloured Kotecký–Preiss schema costs exactly 1 per cell** — not 3, not 9. The coloured KP schema therefore reduces to an uncoloured KP schema at the *same* η, with no colour-multiplicity inflation. This is a genuine simplification of M3 and it is a consequence of A3 alone.

### 1.2 LEMMA 0 — statement

Let `K` be a relayed causal exhaustion (D2) with cells `c = 1,…,N` in a linear extension of the causal order, each at full `τ_R = π/√2`. Let the cell-`c` record register be a fresh copy of `H_R = C³` in state `|ready>`; let `W_c(a_c) = Σ_λ Γ(u_λ^{(c)}(a_c)) ⊗ P_λ` (A4) and let the relay be the sealed typed isometry `R_c = ι_c ⊗ |r_{c+1}>`, `R_c|p_{c,h}> = |e_{c,h}> ⊗ |r_{c+1}>` (0df721a1). Then, with `Q` the completed-sector projector (the all-pointer record word):

**(i) Composition.**
```
K_pointer^(K)(a) = ∏_c^(relay-ordered) K_pointer^(c)(a_c),     later cells on the LEFT,
K_pointer^(c)(a_c) = Σ_λ w_λ Γ(u_λ^(c)(a_c)).
```

**(ii) Independent-colour expansion (H-IND's discharge).**
```
K_pointer^(K)(a) = Σ_{(λ_c) ∈ {0,±√2}^N}  ( ∏_c w_{λ_c} ) · Γ( u_{λ_N}^{(N)}(a_N) ⋯ u_{λ_1}^{(1)}(a_1) ),
```
an unconstrained product sum over 3^N independent per-cell colours.

**(iii) CTP kernel — the forced NESTED form.**
```
R_comp^(K)(a_+,a_-) = K_pointer^(K)(a_-)^† K_pointer^(K)(a_+)
 = Σ_{(μ_c),(λ_c)}  ( ∏_c w_{μ_c}^* w_{λ_c} ) ·
     Γ( u_{μ_1}^{(1)}(a_-)^† ⋯ u_{μ_N}^{(N)}(a_-)^† · u_{λ_N}^{(N)}(a_+) ⋯ u_{λ_1}^{(1)}(a_+) ).
```
The coefficient measure factorises over cells; the Γ-argument is a single **branch-nested** relay-ordered word. It is **not** `Γ(∏_c u_{μ_c}^{(c)}(a_-)^† u_{λ_c}^{(c)}(a_+))` unless the cells' one-particle operators commute.

No step uses `Σ_λ w_λ ≠ 0`, no unitality anchor, and no unitarity of `u`.

### 1.3 Proof

**Step 1 (one cell).** By A4, `(I_S ⊗ <pointer_c|) W_c(a_c) i_{r,c} = Σ_λ <pointer|P_λ|ready> Γ(u_λ^{(c)}) = Σ_λ w_λ Γ(u_λ^{(c)}) = K_pointer^{(c)}(a_c)`. Only `Σ_λ P_λ = I₃` (a *within-cell* completeness) is used; the record channel's unitality `Σ_λ w_λ = 1` is never available and never invoked.

**Step 2 (relay).** Write `R_c = ι_c ⊗ |r_{c+1}>` with `ι_c : L_{p_c} → E_c` the record-relabelling isometry. Then
```
R_c^† R_c = (ι_c^† ι_c) · <r_{c+1}|r_{c+1}> = I .
```
Two consequences, both used and both requiring nothing beyond `R_c^†R_c = I`:
 (a) the ready root supplied to cell `c+1` is a **fixed** vector `|r_{c+1}>`, independent of the colour realised at cell `c`;
 (b) contracting the archive factor with the pointer word on *both* CTP branches gives `ι_c^† |e_{c,pointer}><e_{c,pointer}| ι_c = |pointer><pointer|` — no cross-colour term, no extra norm factor. The relay isometries therefore **cancel exactly** between the branches: they leave neither an overlap factor `<e_{c,h}|e_{c,h'}>` nor a normalisation.

**Step 3 (induction on cells).** Compose. For `N = 2`, acting on `ψ`:
```
W_1(ψ⊗|0>_1) = Σ_λ Γ(u^{(1)}_λ)ψ ⊗ P_λ|0>
R_1 ↦        Σ_λ Γ(u^{(1)}_λ)ψ ⊗ (P_λ|0>)_{E_1} ⊗ |0>_2      ← fresh ready root, λ-independent
W_2 ↦        Σ_{λ,λ'} Γ(u^{(2)}_{λ'})Γ(u^{(1)}_λ)ψ ⊗ (P_λ|0>)_{E_1} ⊗ P_{λ'}|0>_2
<1|_{E_1}<1|_2 ↦  Σ_{λ,λ'} w_{λ'} w_λ Γ(u^{(2)}_{λ'})Γ(u^{(1)}_λ)ψ
              = [Σ_{λ'} w_{λ'}Γ(u^{(2)}_{λ'})][Σ_λ w_λΓ(u^{(1)}_λ)] ψ .
```
The two colour indices decouple **because** the register-2 ready root is a tensor factor supplied by the relay independently of λ (Step 2(a)). Induction on `c` gives (i); expanding the product and using functoriality `Γ(u)Γ(v) = Γ(uv)` gives (ii). **This is H-IND's discharge**: per-cell independent record-colour pairs are not an assumption but a consequence of the sealed relay's tensor-form ready-root supply.

**Step 4 (CTP).** `Γ(u)^† = Γ(u^†)` and `Γ(u)^†Γ(v) = Γ(u^†v)`. Applying `K^{(K)}(a_-)^†` on the left reverses the word and daggers each factor, giving the nested form (iii). No unitarity is used: `Γ = ⊕_k Λ^k` is a multiplicative functor with `(Λ^k M)^† = Λ^k(M^†)` for arbitrary `M`, so the identity survives the M-2 complexification of both branches verbatim. **Named block: LEMMA0_IS_FUNCTORIAL_NOT_UNITARY.**

**Step 5 (`m0 = 0`, no unitality anchor).** Because `Σ_λ w_λ = 0`, `K_pointer^{(c)}` is intrinsically a *difference* object:
```
K_pointer^{(c)}(a) = −(1/4)[ (Γ(u_+) − Γ(u_0)) + (Γ(u_−) − Γ(u_0)) ]    (verified exactly)
```
so if the record coupling does not split colours (`u_λ` λ-independent) then `K_pointer^{(c)} ≡ 0` and `Z_comp ≡ 0`. **Consequence (named block, H_B_IS_FORCED_BY_M0):** hypothesis H-B (`Z_comp(0) ≠ 0`) is not a technical convenience — it is exactly the statement that the record coupling at full `τ_R` splits the colour-resolved propagators enough to defeat the exact cancellation `Σ_λ w_λ = 0`. Any argument that "the diagonal is exact" (the exhaustive companion's `R_all(a,a) = I`) is unavailable by type, in agreement with F-3/L2 fence 3.

### 1.4 Exact-arithmetic verification (my own model)

**Model dimensions.** Source one-particle carrier `d₁ = 2` → fermionic Fock `dim 4`, `Γ(M) = 1 ⊕ M ⊕ det M`. Per-cell record register `C³` (sealed A3 `c`). Relay `R_c : C³ → C³ ⊗ C³`, `|x> ↦ |x>⊗|ready>` (a 9×3 isometry). Cells `N = 2` and `N = 3`; brute-force chain spaces of dimension `4·3^N` = **36** and **108**. Per-cell propagators `u_λ^{(c)}(a) = Cay(h₀^{(c)} + λG_c + aJ_c)`, `Cay(H) = (I−iH)(I+iH)^{-1}` — a Cayley surrogate for the time-ordered exponential, chosen because Lemma 0 is a purely algebraic identity independent of how `u` is generated. Generator triples (all Hermitian over Q) chosen pairwise non-commuting: `(σ_z, σ_x, σ_y)`, `([[2,1],[1,0]], σ_y, σ_z+σ_x)`, `([[0,1+i],[1−i,3]], σ_z, 2σ_x)`. Histories from the frozen A2 set `{0, 7/100, −11/100, 13/100, 4/100}`.

| # | Check | Result |
|---|---|---|
| 1 | `c` Hermitian; `c² = [[1,−1,0],[−1,1,0],[0,0,2]]` | PASS |
| 2 | `P_λ` projectors, `cP_λ = λP_λ`, `Σ P_λ = I₃` | PASS |
| 3 | `p = (1/2,1/4,1/4)`, `Σp = 1`; `w = (1/2,−1/4,−1/4)` | PASS |
| 4 | `m0 = Σ w_λ = 0` exactly | PASS |
| 5 | M-7: `\|w_λ\| = p_λ`; COLOUR-MASS-ONE `Σ\|w_λ\| = 1` | PASS |
| 6 | Cayley propagators exactly unitary (all cells × colours, real histories) | PASS |
| 7 | `Γ(u)Γ(v) = Γ(uv)`; `Γ(u)† = Γ(u†)` | PASS |
| 8 | cells 1,2 one-particle propagators do NOT commute (model generic) | PASS |
| 9 | difference form `K = −(1/4)[(Γu_+−Γu_0)+(Γu_−−Γu_0)]` | PASS |
| 10 | no colour splitting ⇒ `K_pointer = 0` exactly | PASS |
| 11 | `R_c†R_c = I₃` exactly; `R_cR_c† ≠ I₉` (archive, not mixing) | PASS |
| 12 | **N=2 (dim 36): brute-force relayed chain with explicit registers + relays `=` relay-ordered product** | PASS |
| 13 | **N=3 (dim 108): same** | PASS |
| 14 | N=2, N=3: independent-colour expansion (3^N terms) `=` product | PASS |
| 15 | **NC2** shared-colour variant DIFFERS; exact witness `(K_shared−K_prod)[0][0] = 3/8` | PASS |
| 16 | **N=2 NESTED sum `=` `K(a_-)†K(a_+)`** (81 colour-pair terms) | PASS |
| 17 | **N=2 INTERLEAVED reading FAILS**, exact nonzero witness in Q(√2,i) | PASS |
| 18 | **N=3 NESTED `=` direct** (729 terms); INTERLEAVED FAILS | PASS |
| 19 | disjoint (orthogonal-subspace) cells commute; NESTED `=` INTERLEAVED there | PASS |
| 20 | `R_comp(a,a) ≠ I`; exact deviation `(R_comp(a,a)−I)[0][0] = −1` | PASS |
| 21 | companion with `p`-weights: `R_all(a,a) = I` exactly (fenced, F-6) | PASS |
| 22 | **M-5 / NC5** erased-relay weight sum `m0′ = Σp_λ = 1` vs completed `m0 = 0` | PASS |
| 23 | complexified history: `u` not unitary; functoriality still exact | PASS |
| 24 | **M-2 pair polydisc**: NESTED `=` `K̃(a_-)K(a_+)` with `K̃(w) = [K(w̄)]†`, exactly | PASS |
| 25 | interleaved still fails on the polydisc | PASS |
| 26 | `ρ_C = det(I−C)Γ(C(I−C)^{-1})`, `Tr ρ_C = 1` exactly | PASS |
| 27 | **M1**: `ω_C(Γ(k)) = det(I − C + Ck)` exactly, arbitrary `k` | PASS |
| 28 | `Z_comp` as a termwise determinant sum `=` direct state evaluation | PASS |
| 29 | model baseline `Z_comp^{(12)}(0,0) = 13/1920 ≠ 0` (H-B holds in model) | PASS |
| 30 | two-cell connected cumulant exact ratio `Ẑ^{(12)}/(Ẑ^{(1)}Ẑ^{(2)}) = 63314943055943/62120417349042 − (1091338605905/31060208674521) i ≠ 1` | PASS |

**0 failures / 30 checks.**

Selected exact values: `Z_comp^{(12)}(7/100, 13/100 ; −11/100, 4/100)` = `9301837543353677208964843750000000000000000/1756508799245210346030691010102088020974067481 − (27157251050801904589843750000000000000000/195167644360578927336743445566898668997118609) i`. NC2 witness is exactly `Σ_λ w_λ² = 3/8` against `(Σ_λ w_λ)² = 0` in the Fock vacuum sector. (`3/8` also appears in the sealed 52401eef commutator-norm line and in TT2-P0; these are **different quantities that happen to share a rational value** and must not be conflated.)

### 1.5 VERDICT ON THE FORCED READING: **CTP-NESTED IS FORCED**

The sealed spec's O1 display

```
R_comp^(K)(a_+,a_-) = sum_((mu_c),(lambda_c)) prod_c w_(mu_c)^* w_(lambda_c)
                        Gamma( u_(mu_c)^(c)(a_-)^dagger u_(lambda_c)^(c)(a_+) )
```

is, read literally with `prod_c` scoping the whole term, the **interleaved** reading (a per-cell product of `Γ`'s). **That reading is false in general.** If `prod_c` scopes only the weights, the `Γ`-argument has a free index `c` and is ill-formed. The unique well-formed and true reading is the branch-nested one of §1.2(iii).

**Minimal hand-checkable exact witness** (`witness_extras.py`, W-A). Take the branch/colour assignment: cell 1 bra `= A`, ket `= I`; cell 2 bra `= I`, ket `= B`, with the rational unitaries
```
A = (1/5)[[3, 4i],[4i, 3]] ,      B = (1/13)[[5, 12],[−12, 5]]     (both exactly unitary)
NESTED       = A† · I† · B · I  =  A† B
INTERLEAVED  = (I† B) · (A† I)  =  B A†
A†B − BA†    = (96/65) i · diag(1, −1)      ≠ 0            (verified exactly)
```
So the discrepancy is exactly a commutator `[A†, B]` of the two cells' branch operators. It vanishes identically **iff** the cells' one-particle propagators commute. On the multi-cell model the discrepancy persists at N = 2 and N = 3 with the large exact rationals recorded in `lemma0_out.txt`. Because `Γ` is injective on its one-particle block, the one-particle discrepancy is equivalent to the Fock-level discrepancy.

**Where the interleaved display is legitimate:** exactly on the disjoint-cell specialisation — verified exactly by placing two cells on orthogonal one-particle subspaces, where 52401eef's "disjoint cells commute exactly" holds and nested = interleaved. That is the domain of the monoidal-extensivity authority 451550c3 cited by O6.

**F-8 finding (reading obligation, not a spec edit — the sealed text must not be modified):** any executor of O1 must read the sealed `R_comp^{(K)}` display as the **branch-nested** word. Reading it as a per-cell product of second quantisations silently assumes cross-cell commutation of the one-particle propagators, which the sealed corpus grants only for *disjoint* cells (52401eef) — and the linked-cluster expansion's whole point is the **overlapping/adjacent** clusters, precisely where the assumption fails. A downstream determinant factorisation built on the interleaved reading would be wrong at exactly the terms that carry the cluster activities. I flag this as the highest-value item in this return.

---

## 2. ROUTE-Q INDEPENDENCE — INDEPENDENT VERDICT

# **ROUTE_Q_INDEPENDENT**

Reproduced from the sealed text and my own derivation, with no draft artifact consulted. Below is the full input trace of the M3 colored-Kotecký–Preiss schema as **I** construct it, then three adversarial refutation attempts, all of which fail.

### 2.1 What M3 must deliver

Sealed O4 M3: *"colored Kotecky-Preiss-type convergence at eta(epsilon_star) <= 1/2 (threshold frozen in E1), uniform over the D3 quantifier."* D3 = pinned hypercubic skeleton ∪ family A (cubical bisection) ∪ family B (barycentric subdivision) ∪ all common refinements. Target: theorem clause (2), `−Log Ẑ_comp^{(K,X)} = Σ_γ Φ_γ` with `Σ_{γ∋C,|γ|=n}|Φ_γ| ≤ |C|₄ η^n`, `η ≤ 1/2`.

### 2.2 Complete input trace (every input, as I derive it)

| # | M3 input, as I need it | Where it comes from in my derivation | Route-T artifact? |
|---|---|---|---|
| Q1 | cell-local factorisation of `K_pointer^{(K)}`; branch-nested Γ-word | **O1 Lemma 0**, §1 above (my proof) | NO |
| Q2 | per-cell **independent** colour pairs `(μ_c,λ_c)` (polymer colours are free) | O1 Lemma 0 Step 2(a)+3; H-IND discharged, not assumed | NO |
| Q3 | colour-sum cost per cell = **exactly 1** | A3 record data: `\|w_λ\| = p_λ`, `Σ p_λ = 1` (my COLOUR-MASS-ONE) | NO |
| Q4 | each summand is a single second quantisation ⇒ a **determinant** on a quasifree state | **M1** + Phase-A A4 Gaussian-sum form; my exact identity `ω_C(Γ(k)) = det(I−C+Ck)` (check 27) | NO |
| Q5 | per-cell activity bound in D5 **action-density** form, constants functionals of `(‖b_D‖, τ_R, sea-kernel decay data, p_λ)` only | **M2** + spec-header scoping 1 (carrier-index-blind) | NO |
| Q6 | polymer combinatorics: bound on `#{connected clusters of size n containing C}` uniformly over D3 | cell-adjacency graph of `X`; needs `sup_X Δ(X) < ∞` | NO (and **underived** — §3) |
| Q7 | re-aggregation under refinement: `|C|₄` re-partitions exactly, majorant re-aggregates without loss | **O2** + amendment **M-4** poset induction; my R1/R2 exact check (W-D) | NO |
| Q8 | `η(ε)` as an explicit monotone functional; `ε*`; the frozen `1/2` threshold | **E1** steps 1–3 (Route-Q-internal) | NO (and **divergent as defined** — §3) |
| Q9 | log branch and normalisation anchor | T7(i) ratio `Ẑ = Z/Z(0)` + named hypothesis **H-B** | NO |
| Q10 | joint holomorphy of `−Log Ẑ_comp` on the closed pair polydisc | amendment **M-2** + Duhamel (H1)'s adjoint continuation `K̃(w) = [K_pointer(w̄)]†`; my check 24 | NO |
| Q11 | certified outward enclosures / exact arithmetic culture | **F-4** Frozen Numerics | NO |
| Q12 | KP criterion `Σ_{γ ≁ C}|z_γ|e^{a(γ)} ≤ a(C)` ⇒ absolute convergence + clustering | pure combinatorics/analysis; clustering is an **output** | NO |
| — | anchored transfer operator (**TT1**) | not consumed anywhere in Q1–Q12 | — |
| — | spectral-isolation certificate (**TT2**) | not consumed | — |
| — | clustering conversion (**TT3**) | not consumed | — |
| — | refinement intertwiner (**O7**) | not consumed | — |

**Zero Route-T inputs.** Trace closed.

### 2.3 Structural corroborations from the sealed text (each independently checkable)

1. **Scope contradiction argument.** O3 is explicitly scoped *"on the PINNED HYPERCUBIC SKELETON only"* and *"no TT certificate quantifies beyond the skeleton."* An input whose validity is skeleton-confined cannot be load-bearing for a claim quantified over the full D3 poset unless transported by O7. So *a priori* either M3 is Route-T-free, or M3 requires O7. Since O7's own stated job is to transport *"the O3 certificates plus the O4 constants"*, and Q1–Q12 consume **no O3 certificate**, O7's premise set is empty — it has nothing to transport and no consumer.
2. **Amendment M-10 fixes the arrow direction.** *"the E1 threshold's users are M3 (inside O4) and O5; O3 consumes epsilon_star only."* So the graph is `E1 → {M3, O5}` and `E1 → O3`. There is **no `O3 → M3` edge**; M3 and O3 are siblings fed by E1. This is sealed-text certification of independence that requires no draft.
3. **`ε*` is not a skeleton number.** E1 defines `ε*` from `η(·)` alone, and by spec-header scoping 1 `η` is a functional of `(‖b_D‖, τ_R, sea-kernel decay data, p_λ)` **only**, per-unit-4-volume by D5, on a frozen dyadic grid with a frozen `1/2`. No TT2 gap radius enters. F-4 additionally forbids `ε*` being tuned by any output, which forecloses any back-channel from an O3 certificate.
4. **The `1/2` threshold is a KP margin, not a spectral gap.** My exact arithmetic (W-C): at `η = 1/2`, `Σ_{n≥2} η^n = η²/(1−η) = 1/2` exactly — this is the M-1 spanning-tail comparator `|C|₄ η²/(1−η)`, a geometric-series fact. Nothing spectral is involved.

### 2.4 Three adversarial refutation attempts (all fail)

**Attempt 1 — dependence via `ε*`.** *"M3 is stated at `η(ε*) ≤ 1/2`; if `ε*` were the certified disk radius of TT2 on the skeleton, M3 inherits a skeleton-scoped, Route-T-derived number."* — **Fails.** E1's rule reads only `η(·)`, whose argument list is frozen by spec-header scoping 1 and contains no operator-theoretic object; the grid and threshold are frozen constants; M-10 says O3 *consumes* `ε*`; F-4 bars tuning. The arrow is `O3 ← E1`, never `E1 ← O3`.

**Attempt 2 — dependence via O4's own header wording.** *"O4 says 'Transport the skeleton majorant across families A, B, and common refinements' — so clause (2) on a refined `X` is by construction the transported skeleton bound, which needs O7."* — **Fails.** The named mechanism in the same sentence is *"via the sea-compressed determinant representation with CELLULATION-BLIND constants"*, i.e. M1+M2+M3, not O3's certificates. Theorem clause (2) is quantified **directly** over `X` and states the bound in D5 action-density form; D5 requires the re-aggregation identity to be *"proved, not assumed"*, and O2 (with M-4) owns that proof over the full common-refinement poset. So the bound on a refined `X` is derived **on** `X`, with the skeleton merely one member of the quantifier rather than the source. "Transport" in O4's header names the *goal* (quantifier coverage), not a mechanism that reads O3 output.

**Attempt 3 — a spectral gap hiding inside KP.** *"Uniform exponential clustering across a growing volume really needs a transfer-operator gap; KP is a disguise."* — **Fails.** Kotecký–Preiss is a purely combinatorial/analytic implication: the activity-domination hypothesis `Σ_{γ' ≁ γ}|z_{γ'}|e^{a(γ')} ≤ a(γ)` yields absolute convergence of the cluster series and exponential decay of connected correlations, with **no spectral input**. Exponential clustering is KP's *conclusion*. TT3 is the *converse* direction (gap ⇒ clustering) and is one alternative supplier confined to the skeleton. Redundant, not required.

### 2.5 Verdict, with its honest boundary

**ROUTE_Q_INDEPENDENT.** The M3 colored-KP schema's uniformity over the full D3 quantifier requires **no** Route-T artifact: not TT1, not TT2, not TT3, not the O7 intertwiner. The dependence claimed by the audit is reproducible from the sealed text alone, and it survives three adversarial angles. I concur with the rescope's Q1 answer and with accompaniment (a)'s wider statement (O3's TT1–TT3 skeleton certificates also drop out of the arm's predicate). O7 is refuted-and-not-required; the Route-T skeleton gap is uncertified-and-not-required.

**Boundary — stated so this is not over-read.** This is a verdict about the **architecture of inputs**, not a discharge of M3. Two of M3's inputs I could not derive (Q6, Q8). Route-Q therefore carries the full quantifier *in principle* and **not yet in fact**. The rescope's own "Consequence for the front" is correct and, in my reading, understated: there are **two** walls, not one (§3).

---

## 3. O4–O6: WHAT I RE-DERIVED AND WHAT I COULD NOT

### 3.1 Re-derived (named blocks)

- **O1 / LEMMA 0 — fully re-derived and exactly verified.** §1. Composition, independent-colour expansion, exact relay cancellation from `R_c†R_c = I` alone, H-IND discharged structurally, `m0 = 0` respected with no unitality anchor anywhere. Plus the forced-reading determination (§1.5), which is a correction to how the sealed display must be read.
- **O4 / M1 — re-derived, with an exact certificate.** Each term of the Lemma-0 sum is exactly one `Γ(u_μ^† u_λ)`; on a gauge-invariant quasifree state with one-particle density `C`, `ω_C(Γ(k)) = det(I − C + Ck)` — I proved and verified this exactly (`ρ_C = det(I−C)Γ(C(I−C)^{-1})`, `Tr ρ_C = 1`, non-diagonal rational `C`). Hence
  `Z_comp^{(K)}(a_+,a_-) = Σ_{(μ),(λ)} ∏_c w_{μ_c}^* w_{λ_c} · det(I − C + C·u_{(μ)}(a_-)^† u_{(λ)}(a_+))`,
  a **finite termwise** sum of determinants of genuine second quantisations. This honours the determinant fence (4e1282bc gate item 9) exactly as M1's compliance citation (i) claims: each single term *is* the corresponding second-quantised Gaussian operator, and no single postselected determinant replaces the sum. Caveat: the `u_{(μ)}` must be the **nested** words of §1.5, not interleaved products.
- **O4 / M3 — schema assembled, input list closed, colour cost computed.** COLOUR-MASS-ONE (§1.1) reduces the *coloured* KP schema to an uncoloured one at the same `η`: the branch-pair colour mass is exactly 1 per cell. The M-1 spanning-tail comparator `|C|₄ η²/(1−η)` is exact, `= |C|₄/2` at the frozen threshold `η = 1/2`.
- **O2 / re-aggregation, steps R1–R3 — re-derived exactly.** R1: one 4-d bisection step splits `C` into `2⁴ = 16` subcells with `Σ_i |C_i|₄ = |C|₄` exactly. R2: `Σ_i |C_i|₄ η^n = |C|₄ η^n` — the action-density majorant re-aggregates with **no loss**. R3 (**NC6's trap, exhibited**): a per-CELL-constant activity `κη^n` totals `16^k κ η^n` after `k` bisection steps (1, 16, 256, 4096, 65536, …) while the `|C|₄`-form stays fixed — divergent, exactly as NC6 predicts.
- **Negative-control witnesses obtained as by-products, all exact.** NC2: shared-colour variant differs, witness `Σ_λ w_λ² = 3/8` vs `(Σ_λ w_λ)² = 0`. NC5 / amendment M-5: the record-erasing advance restores `m0′ = Σ_λ p_λ = 1` against the completed chain's exact `0`, and restores diagonal unitality `R_all(a,a) = I` exactly, whereas `R_comp(a,a) − I` has exact entry `−1`. NC1's ground is confirmed by type: GHZ is the perfectly-correlated-colour limit, i.e. precisely the failure of Q2 / Lemma 0 Step 2(a), so refusal must cite H-IND.
- **O6 (4)(ii) — the *form* of the subextensive rate re-derived.** Grouping the cluster series by anchor cell and applying the per-anchor tail `|C|₄ η/(1−η)` gives `| |X|₄^{-1}(−Log Ẑ) − limit | ≤ (η/(1−η)) · |∂X|₄ / |X|₄`, i.e. a boundary-to-bulk 4-volume ratio. The *form* is derivable from clause (2) + R1/R2; the *certified constant* is not, because it is `η/(1−η)`.

### 3.2 NOT re-derived — with named obstructions

**(A) `E1_KSEA_FUNCTIONAL_NONEXISTENT_AS_DEFINED` — the wall, as expected.** E1 step 1 demands `η(ε) = F(ε; ‖b_D‖, τ_R, sea-kernel decay data, p_λ)` be *"an explicit monotone functional"* that is a **per-unit-4-volume** activity majorant and (spec-header scoping 1) **carrier- and cellulation-blind**. I could not derive it, and my own scaling analysis says it does not exist as defined. Exact radial arithmetic in `d = 4` (`e1_ksea_scaling.py`; `Ω₃ = 2π²` carried symbolically, never evaluated, so no transcendental enters):

```
I(p; a, L) / Omega_3 = int_a^L r^{3-p} dr :
   p < 4 : (L^{4-p} - a^{4-p})/(4-p)   -> IR divergent as L^{4-p}
   p = 4 : log(L/a)                    -> IR log-marginal
   p > 4 : (a^{4-p} - L^{4-p})/(p-4)   -> IR finite, UV a^{4-p}
```

- **Reading (a)** — `K_sea(C) = Σ_{C'≠C} sup|G| · |C'|₄` with the `|x|^{-3}` class named by O4's own confronted failure mode: `p = 3 < d = 4`, so `K_sea/Ω₃ = L − a`, **linear IR divergence**. Exact table at `a = 1/16`: `L = 1, 4, 16, 64, 256, 1024` → `15/16, 63/16, 255/16, 1023/16, 4095/16, 16383/16`. The object is not a functional of `(‖b_D‖, τ_R, decay data, p_λ)` at all — it depends on the IR cutoff `L`.
- **Reading (b)** — pair activity quadratic in the kernel (`p = 6`, the leading connected two-cell cumulant of a quasifree sea): IR-convergent, `K_sea/Ω₃ = (a^{-2} − L^{-2})/2`, but the **D5 per-unit-4-volume density** `K_sea/|C|₄ ~ a^{-6}` blows up under refinement. Exact table at `L = 1`, `a = 2^{-k}`: density `= 24, 1920, 129024, 8355840, 536346624, 34351349760, 2198889037824, 140735340871680` for `k = 1…8`.

**Either way this is an EXISTENCE failure, not a size failure.** Therefore E1 step 3's disposition `EPSILON_STAR_VACUOUS` **does not even apply** — it presumes `η` exists and is merely too large on the grid. E1 step 1 is unexecutable as written, so **E1 must be REPLACED, not certified**, which is the same conclusion the rescope decision records from the IR memo's C2 — reached here independently. *How to replace, minimally:* the sea kernel must enter through a **connected/truncated** (cumulant-subtracted) form whose complement sum converges (effective `p > 4`) **and** whose per-4-volume density is bounded uniformly as the cell scale `→ 0`, i.e. the replacement must be simultaneously IR-summable and refinement-stable. Those two requirements pull in opposite directions for a `|x|^{-3}` class kernel and that tension is the actual content of the front. *Stated assumption, since I do not have the IR memo (not in my read set and possibly draft-authored):* I assumed the decay class is the `|x|^{-3}` class the sealed spec itself names, and that `K_sea` is the complement-sum form or its quadratic pair form. If the sealed `K_sea` is some third functional, my diagnosis constrains but does not settle it.

**(B) `REFINEMENT_POSET_DEGREE_BOUND_UNDERIVED` (input Q6).** KP needs `#{connected size-`n` clusters containing `C`} ≤ (eΔ)^{n−1}`-type bounds with `Δ = sup_{X ∈ D3} Δ(X) < ∞`. For family A alone, `Δ` is a constant (`≤ 3⁴−1 = 80` for full adjacency in 4-d). For family B alone, `Δ` is bounded by the initial complex. **For A-with-B common refinements I could not derive any uniform `Δ`**: cells are intersections of cubes with simplices, and as the two families' scales become incommensurate I have no bound on the number of cells adjacent to a given piece.

**(C) `SLIVER_CELLS_BREAK_ACTION_DENSITY` (new obstruction I found; not previously named in the sealed text I read).** This one is sharper than (B) and is *independent of both E1 and Route T*, so it does not touch the §2 verdict — it adds a second Route-Q-internal wall. Common refinements of a cubical and a simplicial family produce **slivers**: cells whose 4-volume `|C|₄ → 0` while their diameter stays `O(1)`. The D5 bound `Σ_{γ∋C,|γ|=n}|Φ_γ| ≤ |C|₄ η^n` requires activity to be controlled by 4-volume, but the sea kernel couples cells through their **geometric extent**, not their measure. A sliver has `O(1)` extent and `o(1)` volume, so the ratio `activity/|C|₄` is unbounded on the common-refinement poset. This is the D5 refinement-stability trap biting in a way NC6 (per-cell-constant activity) does **not** test: NC6's fixture is volume-blind, whereas a sliver is volume-*aware* and still fails. **Recommendation for the successor: NC6 needs a companion control with a genuine sliver fixture**, or the D3 quantifier needs a shape-regularity qualifier — and per F-2 the latter would be a scope decision for Brian, not a lemma-shaped restriction.

**(D) `COMMON_REFINEMENT_POSET_CLOSURE_UNDERIVED` (amendment M-4's own flagged obligation; O6 (4)(i)).** I proved one-step re-aggregation (R1/R2) exactly, but I could **not** close the induction over the full common-refinement poset. M-4 is right that *"one step does not reach A-with-B common refinements"*: the poset of common refinements of a cubical-bisection family and a barycentric family is not generated by single refinement steps inside either family, and I found no generating set. Cellulation-independence of the intensive limit (clause (4)(i)) is therefore **not** derived — only the one-step invariance is.

**(E) `O5_DIFFERENTIATED_ACTIVITY_MAJORANT_UNDERIVED` (theorem clause (3); O6 (4)(iii)).** I could not derive it, and I record why the obvious shortcut is barred rather than merely discouraged. Each `Φ_γ` is holomorphic on the closed pair polydisc (verified structurally: `u_λ^{(c)}(a)` is holomorphic in `a`, `det` is polynomial, and check 24 shows the whole nested construction survives complexification). Cauchy estimates on a polydisc of radius `ε*(1−δ)` would give derivative bounds with a `1/(δε*)` loss. But clause (3) demands convergence *"on the same polydisc with the same form of bound"* — radius `ε*`, not `ε*(1−δ)` — so the Cauchy route does not reach the stated conclusion, and O5's own clause (*"No artifact may infer it from clause (2)"*) bars citing it anyway. A direct differentiated activity majorant is needed, and it depends on a derivative version of `η`, hence on (A). Clause (4)(iii) (the interchange consumed by T7(iv)) depends on O5 and is therefore also underived.

**(F) O3 / TT1–TT3, and O7.** Not attempted. Per the rescope, they are no longer in the arm's predicate; and my §2 finding is that M3 does not consume them. I make no claim about whether they could be derived.

**(G) The spec's W1 enclosure — cannot be discharged in this lane at all.** F-8's second half requires re-deriving the W1 enclosure from the spec. W1 is `−Log Ẑ_comp^{(12)} + Log Ẑ_comp^{(1)} + Log Ẑ_comp^{(2)}` on the **Phase-A** relayed completed chain at the frozen pair, which needs the actual Phase-A propagators `u_λ^{(c)}(a)`. Phase A is unexecuted (`actual_parent_regulated_CAR_operator_response_derived = false`), so those objects do not exist yet. What I *did* do is exercise the whole pipeline end-to-end in my own model and produce the exact model-internal cumulant argument `Ẑ^{(12)}/(Ẑ^{(1)}Ẑ^{(2)}) = 63314943055943/62120417349042 − (1091338605905/31060208674521)i ≠ 1` — clearly labelled: **this is not the spec's W1** and must never be cited as such. It does establish that the completed chain does not factorise cell-wise when cells share the source carrier, which is the structural reason the connected cumulant is nonzero (spec prediction P3's direction, on a model, not on the fixture).

Also worth recording under the M-9 heading: with the frozen pair `(7/100, −11/100)` used per M-9 only if `ε* ≥ 11/100`, and `ε*` drawn from the dyadic grid `{2^{-k}}`, the relevant grid points bracket as `2^{-4} = 1/16 = 6.25/100 < 11/100 ≤ 2^{-3} = 1/8 = 12.5/100`. So the frozen pair is admissible **iff** `ε* ≥ 1/8`, i.e. iff `η(1/8) ≤ 1/2` certified; otherwise M-9's fallback `(ε*, −ε*)` governs. That is a clean pre-execution consequence of E1's grid, derivable now — but it is moot until (A) is repaired.

---

## 4. RETURN SUMMARY

```
SEALS_VERIFIED                      = true    (9 texts, before and after; no drift)
DRAFT_ARTIFACTS_READ                = none    (independence preserved)
SEALED_FILES_MODIFIED               = none
MEASURED_CONSTANTS_USED             = none    (no 137.03.., no 0.00729.., no CODATA)
FLOATS_USED                         = none    (exact Q(sqrt2,i) throughout)

LEMMA 0
  composition identity              = DERIVED and exactly verified (N=2 dim 36, N=3 dim 108)
  relay cancellation from R^dag R=I  = DERIVED (no unitality, no unitarity used)
  H-IND discharged structurally      = YES (and shown load-bearing: NC2 witness 3/8)
  m0 = 0 respected, no anchor        = YES (R_comp(a,a) - I has exact entry -1)
  FORCED READING                     = CTP-NESTED
    interleaved reading is FALSE, exact witness A^dag B - B A^dag = (96/65) i diag(1,-1)
    interleaved valid iff cells' one-particle propagators commute (disjoint/monoidal only)
    => F-8 reading obligation on the sealed O1 display; highest-value finding here

ROUTE-Q INDEPENDENCE
  verdict                            = ROUTE_Q_INDEPENDENT
  Route-T inputs found in M3         = ZERO (TT1, TT2, TT3, O7 all absent from the trace)
  adversarial refutations attempted  = 3 (epsilon_star channel; O4 header wording;
                                        hidden spectral gap in KP) -- all FAIL
  corroborated by                    = M-10 arrow direction; O3's skeleton-only scoping;
                                        E1's argument list; KP's clustering being an OUTPUT
  NEW derived simplification         = COLOUR-MASS-ONE: the CTP colour sum costs exactly 1
                                        per cell (|w_lambda| = p_lambda, sum p = 1), so the
                                        COLOURED KP schema = uncoloured KP at the same eta

UNDERIVED, with named obstructions
  E1_KSEA_FUNCTIONAL_NONEXISTENT_AS_DEFINED   (existence failure, not size:
        reading (a) linear IR divergence p=3<d=4; reading (b) a^-6 refinement blow-up
        of the per-unit-4-volume density.  EPSILON_STAR_VACUOUS does not apply.
        E1 must be REPLACED, not certified.  Assumption stated; IR memo not in read set.)
  REFINEMENT_POSET_DEGREE_BOUND_UNDERIVED      (M3 input Q6, A-with-B common refinements)
  SLIVER_CELLS_BREAK_ACTION_DENSITY            (NEW; |C|_4 -> 0 at O(1) diameter defeats
        the D5 form; NOT tested by NC6; Route-T-independent, so verdict unaffected)
  COMMON_REFINEMENT_POSET_CLOSURE_UNDERIVED    (M-4's own obligation; kills clause (4)(i))
  O5_DIFFERENTIATED_ACTIVITY_MAJORANT_UNDERIVED (Cauchy route reaches only a shrunk
        polydisc, so it does not even give clause (3); and O5 bars it anyway)
  W1_ENCLOSURE_NOT_DISCHARGEABLE_IN_THIS_LANE  (Phase-A propagators do not exist yet)

RE-DERIVED (named blocks)
  O1 Lemma 0 (all three parts) ; O4/M1 termwise determinant with exact
  omega_C(Gamma(k)) = det(I - C + C k) ; O2 R1-R3 re-aggregation + the NC6 trap exhibited ;
  M-1 spanning tail eta^2/(1-eta) = 1/2 at eta = 1/2 ; M-5/NC5 exact witness (m0' = 1 vs 0) ;
  M-7 |w_lambda| = p_lambda ; M-2 polydisc holomorphy of the nested construction ;
  O6 (4)(ii) FORM of the subextensive rate (constant not certified) ;
  H_B_IS_FORCED_BY_M0 (no colour splitting => Z_comp identically 0)

PROTECTED STATUS UNCHANGED BY THIS LANE
  F8_rederivation_first_half_lemma0_reproduced          = true
  F8_rederivation_routeQ_independence_reproduced        = true
  F8_rederivation_and_hostile_review_discharged        = false   (second half + hostile
                                                                  review still outstanding)
  lemma0_completed_chain_composition_derived            = false  (this lane cannot seal)
  connected_linked_cluster_density_proved               = false
  epsilon_star_frozen                                  = false
  kappa_record_computed = false ; alpha_computed = false ; proof_authorized = false
```

Two items I would put in front of Brian rather than leave in a table. First, the **nested-vs-interleaved reading** of the sealed O1 `R_comp` display: the literal reading is false wherever the cells overlap, which is exactly where the cluster expansion lives, and an executor could easily build a determinant factorisation on it. Second, the **sliver obstruction**: it is a second wall, independent of E1 and of Route T, that the current control suite (NC6) does not detect, and closing it looks like an F-2 scope decision rather than a lemma.
