# STAGE 8 — AXN BUILD — `U2SQ-FINITE-CANONICITY-ATTACK`, EXECUTED
## DARIO LANE (Builder B, verifier) — RELAY 860 — [PLAN:AXN-BUILD-A27]

```text
alpha_computed         = false
proof_authorized       = false
kappa_record_computed  = false
```

No member bound; no fixed-point execution; no end test; no smooth carrier imported; no EM
identification; no common cell formed; no junction map evaluated. PE-1..PE-12 pointer-only, none
opened or consulted. `~/.codex` untouched; memory-bank never searched. No register, plan, tracker, or
git action.

**GATE NOTE ON THE NUMERICS.** This attack replays a **finite, sealed, dimension-108 linear-algebra
construction** and reports operator norms, Hilbert–Schmidt inner products, and residuals. **No
physical quantity is numerically evaluated and no measured constant is compared**: no coupling, no
scale, no root, no response coefficient, no interval, no `alpha`, no `kappa`. The quantities below are
structural residuals of a sealed operator identity — the same posture as my 821 commutator work. The
gates above are held in letter and in substance.

CLAIM STATUS: **all headline items CLAIMED.**

**BUILDER-NEVER-VERIFIES, RUNNING THE RIGHT WAY ROUND.** The contract executed here is **Codex's**,
verbatim from the U2 census §4.3; the subjects are opposite-lane and packet-sealed. I have twice had
to disclose the reverse shape (855, 857); the asymmetry should be visible in both directions, so I
record it here too.

**THE THREE-OBJECT TYPING IS CARRIED AND IS NOT CONFLATED ANYWHERE.** `U2_sq` (the `D^2` decomposition
law) — attacked here. `U2_phys` (what the `d_U2` leg actually consumes) — **a false homonym**,
untouched. `Delta_Gamma` (the `Gamma_rest` termwise theorem) — **not startable**, subject functional
false/TYPE-U, untouched. No sealed bridge joins them and I build none.

---

## 0. LEAD

**`VERDICT = NONCANONICAL.`** Both negative controls survive at the sealed finite parent, and **no
canonicity mechanism is derivable from the sealed structure**. The census's §2.2 obstruction is not
merely restated here — it is **reproduced at the packet parent with independent numbers**.

- **RECONSTRUCTION is exact.** Replaying the sealed construction independently:
  `‖D_K² − (T1+T2+T3)‖ = 0.000e+00`, with component norms matching the sealed JSON to twelve decimal
  places. **`INPUT_GAP` does not fire** — the bundle exposes every byte needed for replay.
- **The half-split survives**, residual `0.000e+00`, component count 3 → 4, with `D_K` **and** `D_K²`
  unchanged. **This control needs no equivalence assumption and it alone carries the verdict.**
- **The basis rotation survives**, and in its sharpest form: a unitary `U` commuting with `D_K` gives
  `‖U D_K U* − D_K‖ = 4.4e−14` — **literally the same operator** — yet a **different** Hermitian
  component triple summing to the same square. Same `D`, same cardinality, two decompositions.
- **No mechanism.** The orthogonal-projector/direct-sum route is refuted numerically:
  `⟨T1,T2⟩ = +96 ≠ 0`. The record-sector grading route fails because it **merges** `T1` and `T3`.

**CO-FINDING, `LAW_GAP`, and it is a gap in the relay's own INPUT FREEZE.** The contract freezes
*"admissible source/cell relabelings **already sealed in the packet bundle**."* **The bundle seals
none.** Across the SPEC and RESULT: `relabel` 0, `permut` 0, `admissible` 0, `equivalen` 0. The
demand's `INVARIANCE` obligation quantifies over "the equivalences admitted by the law" — **at this
parent that class is empty of record**, so obligation (c) cannot be discharged as specified. I report
this rather than supplying a relabeling group, which would be authorship.

**`PROMOTION = NOT-CLAIMED.`** The verdict is negative, so promotion is not at issue; the finite scope
is held regardless, and nothing here is offered as the universal `U2_sq` law.

**Bonus structural result (§3.3):** the maximal *orthogonally separable* census at this parent is
**two** blocks, `{T1+T2, T3}` — not three. The displayed three-component census refines that split
with no orthogonality warrant, **and even the two-block census fails both controls.**

---

## 1. CUSTODY AND SUBJECTS

All subjects seal-verified **before reading**. Law 8, all spellings, including the fourth mode: the
parent bundle is carried by a **group sidecar** `R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_V001.seal.sha256`
whose filename **drops `SPEC`/`RESULT`** — the fifth fourth-mode instance I have logged.

| subject | digest | seal |
|---|---|---|
| U2 census (governing) `STAGE8_AXN_BUILD_U2_CENSUS_CODEX2_V001.md` | `981f195444261b0a` | OK |
| `R3_4_..._PARENT_SPEC_V001.md` | `40890e753463b8c4` | OK (group + direct) |
| `R3_4_..._PARENT_RESULT_V001.md` | `345d447eaf6d730c` | OK (group) |
| `results/r3_4_..._parent_v001.json` | `7f83d081b1e7eb03` | OK (group) |
| `scripts/audit_r3_4_..._v001.py` | `8cf5bfcb172ac848` | OK (group) |
| `scripts/verify_r3_4_..._v001.py` | `1e7a3deae68b140a` | OK (group) |
| `tests/test_r3_4_..._v001.py` | `4570ecbd69c10aea` | OK (group) |
| `results/..._verification_v001.json` | `5902ab9aef714bbd` | OK (group) |
| `R3_4_..._SELF_REVIEW_V001.md` | `04c2c0ca8dc226e7` | OK (group) |

All **nine** members verify. The JSON's own `authority_hashes_match = true` over fifteen upstream
authorities, and `specification_seal_matches = true`.

**Independence check, stated because it is load-bearing:** the `scripts/` and `tests/` here are at the
workspace root and are **named as subjects by the relay**. They are **not** `evaluator_build_A/*.py`
and **not** `checks/`. Builder-B independence is intact; I opened nothing off limits.

**I did not execute the sealed script.** I read the sealed definitions and **re-implemented the
construction independently** in scratch, then compared against the sealed JSON. Re-derive, not trust.

---

## 2. THE DEMAND AND WHAT WOULD DISCHARGE IT

Governing span, from my own 830/834 U-ledger (`e294c2cdd3afd78d`, `[4663,8045)`, span sha
`231ec97606a0fee6`):

> `U2 canonical decomposition: a law fixing the components of D^2 — canonical projectors, a
> direct-sum uniqueness theorem, an irreducibility rule, or a ban on refining a declared component.`

Seven receiver obligations govern: `DOMAIN`, `RECONSTRUCT`, `IDENTIFY`, `CANONICALIZE`,
`NO-REFINEMENT`, `INVARIANCE`, `SCOPE`. The obstruction span (`59096d27a8f07d40`, `[5599,6676)`, span
sha `ee3d436e6fab17a4`) exhibits the half-split and the fixed-cardinality basis rotation.

**The disjunction is not a licence to choose.** Four mechanisms are named; the relay forbids adopting
a decomposition because it is displayed. §3.2 tests the two that sealed structure could conceivably
supply, and both fail on their own terms.

---

## 3. THE ATTACK

### 3.1 (b) RECONSTRUCTION — displayed, exact

The sealed finite parent, re-implemented from the sealed definitions:

```text
gamma0, gamma_spatial, gamma5   (Dirac, 4x4)
alpha_x              = gamma0 @ gamma_spatial[0]
source_incidence_spin= -1j * gamma0 @ gamma5
derivative           = cyclic first difference on 3 sites ; momentum = -1j * derivative
h_free               = kron( kron(momentum, alpha_x), I_9 )
masks                = ( diag(1,1,0), diag(0,1,1) )
record_incidence[s]  = c_partial embedded at record site s      (c_partial 3x3, Hermitian)
writes[s]            = kron( kron(masks[s], source_incidence_spin), record_incidence[s] )
D_K                  = h_free + writes[0] + writes[1]           dim = 108, Hermitian (0.000e+00)
```

The sealed three-term identity:

```text
T1 = h_free @ h_free
T2 = combined_write @ combined_write
T3 = derivative_descendant  =  sum_s  -1j * kron( kron([derivative,mask_s], alpha_x@sis), rec_s )

    ‖ D_K@D_K  -  (T1 + T2 + T3) ‖  =  0.000e+00        RECONSTRUCT: DISCHARGED
```

Independent agreement with the sealed JSON, to twelve decimals:

| quantity | my replay | sealed JSON |
|---|---|---|
| overlap descendant norm | `16.000000000000` | `16.0` |
| derivative-support descendant norm | `9.797958971133` | `9.797958971132712` |
| full square identity error | `0.000e+00` | `0.0` |

`‖T1‖ = 6.363961`, `‖T2‖ = 27.712813`, `‖T3‖ = 9.797959`; all three Hermitian to `0.000e+00`.

**`INPUT_GAP` DOES NOT FIRE.** The bundle exposes the operator and component bytes needed for replay,
and I replayed them. *(Recorded because the cheapest exit from this relay was to declare INPUT_GAP
and stop; it would have been false.)*

### 3.2 (a) MECHANISM — none derivable from sealed structure

**Probe 1 — canonical projectors / direct-sum uniqueness. REFUTED.** Hilbert–Schmidt Gram of the
sealed census:

```text
            T1        T2        T3
   T1    +40.500   +96.000    +0.000
   T2    +96.000  +768.000    +0.000
   T3     +0.000    +0.000   +96.000
```

`⟨T1,T2⟩ = +96.000 ≠ 0`. **The displayed components are not mutually orthogonal**, so neither an
orthogonal-projector law nor a direct-sum uniqueness theorem is available at this parent.

**Probe 2 — a sealed grading. REFUTED, and instructively.** Reducing each component over the source
factor to read its record-sector content: `T2` carries record content (`c = +21.333`), while **`T1`
and `T3` both reduce to zero record content** (`0.000000`). A record-sector grading therefore
**merges `T1` with `T3`** and cannot produce the three-component census. The grading that exists
separates one component and destroys the distinction between the other two.

**Probe 3 — is a mechanism stated anywhere in the bundle? NO.** Occurrence counts across SPEC and
RESULT: `canonical` **0/0**, `irreducib` **0/0**, `refine` **0/0**, `component count` **0/0**. The
three `projector` hits in the SPEC are a charged-control spectral projector and a **prohibition**
(*"it may not replace it with a target-selected projector"*) — neither is a component law.

**MECHANISM = NOT DERIVABLE.** Per stop-on-freedom and the void condition, **I do not supply one.**
Writing a projector rule, a grading, or a component count here would be exactly the "chosen from
desired coefficient" move the void condition names.

### 3.3 The orthogonality structure — how far canonicity *could* have reached

`T3` **is** exactly orthogonal to both others (`⟨T1,T3⟩ = ⟨T2,T3⟩ = ⟨T1+T2,T3⟩ = 0.000e+00`).

**So the maximal orthogonally separable census at this parent is TWO blocks, `{T1+T2, T3}` — not
three.** The sealed three-component display refines the only orthogonally warranted split, and the
refinement is precisely `T1` versus `T2`, the pair with `⟨T1,T2⟩ = 96`.

**And even the two-block census fails both controls** (§3.5). The coarsest defensible granularity is
still not canonical, so the failure is not an artifact of over-refinement.

### 3.4 (c) INVARIANCE — **cannot be discharged: the equivalence class is unsealed**

The `INVARIANCE` obligation reads: *"make the component census invariant under **the equivalences
admitted by the law**."* I went to enumerate them and found none.

```text
SPEC / RESULT occurrence counts:
  relabel 0/0    permut 0/0    admissible 0/0    equivalen 0/0
  covarian 7/0   invarian 2/1  gauge 1/1
```

**The bundle seals no relabeling group, no permutation action, and no admissibility or equivalence
relation.** The relay's INPUT FREEZE clause presupposes *"admissible source/cell relabelings already
sealed in the packet bundle"*; **that stock is not there.**

I tested the one candidate an outside reader would try — the record-site swap — and **it is not
admissible**: `‖SW·D_K·SW − D_K‖ = 1.386e+01`. It moves the operator, because the masks
`diag(1,1,0)`, `diag(0,1,1)` are attached in the source factor and are not carried by a record swap.
Repairing it requires a source-site reversal, which flips the cyclic derivative and hence `h_free`.
**Constructing the compensating group is exactly the authorship the void condition bars**, so I stop.

`INVARIANCE = NOT TESTABLE AS SPECIFIED (the admitted-equivalence class is empty of record).` This is
the relay's **`LAW_GAP`** condition — *"canonical depends on an unsealed equivalence or
granularity"* — reported as a co-finding, not as the primary verdict, for the reason in §4.

### 3.5 (d) NEGATIVE CONTROLS — **both survive**

**Control 1 — half-split of a declared component. SURVIVES.**

```text
D_K^2 = T1 + T2 + T3                       (3 components)
D_K^2 = T1 + T2 + (1/2)T3 + (1/2)T3        (4 components)   residual = 0.000e+00
```

`D_K` unchanged, `D_K²` unchanged, component count 3 → 4, component norms
`[6.363961, 27.712813, 4.898979, 4.898979]`. The obstruction span's construction, reproduced at the
packet parent. **This control invokes no unitary and no equivalence assumption whatsoever**, and
nothing in the bundle bans refinement (`refine` 0/0).

**Control 2 — internal basis rotation at fixed cardinality. SURVIVES, in its sharpest form.**
Take `U = exp(i·D_K)`, which commutes with `D_K` by construction:

```text
‖U D_K U* − D_K‖       = 4.413e-14      <- the SAME operator, not merely the same square
‖U D_K^2 U* − D_K^2‖   = 8.725e-14
‖ sum_i U T_i U* − D_K^2 ‖ = 8.682e-14  ; all three rotated components Hermitian
‖U T1 U* − T1‖ = 4.0848   ‖U T2 U* − T2‖ = 10.2491   ‖U T3 U* − T3‖ = 10.5344
component norms preserved exactly (6.363961 / 27.712813 / 9.797959)
```

**The same operator `D_K`, at the same cardinality 3, yields two different Hermitian component
triples, each summing exactly to `D_K²`.** The components are therefore **not a function of `D_K`**;
they are a function of construction data (`h_free`, `combined_write`, `dd`) not recoverable from
`D_K` itself.

**The honest limit of control 2, stated because it matters.** `U` commutes with `D_K`, so a law that
identified components *up to symmetries of `D`* would call the rotated triple equivalent. **Whether
that identification is permitted is precisely the equivalence §3.4 found unsealed.** So control 2's
force is *conditional* on the `LAW_GAP`. **Control 1 is not**, and control 1 alone is sufficient.

Applied to the coarser census: `‖U(T1+T2)U* − (T1+T2)‖ = 10.5344` and the half-split of `T3` takes
2 → 3 at residual `0.000e+00`. **Both controls survive at every granularity tested.**

---

## 4. THE VERDICT, AND WHY THIS STOP AND NOT ANOTHER

Two stops fire on the evidence. I return the stronger one and report the other.

| stop | fires? | why |
|---|---|---|
| `INPUT_GAP` | **NO** | the bundle exposed every replay byte; reconstruction exact, JSON matched to 12 decimals |
| `LAW_GAP` | **YES — co-finding** | "canonical" would depend on an unsealed equivalence: no relabeling/admissibility/equivalence stock exists at this parent (§3.4) |
| **`NONCANONICAL`** | **YES — RETURNED** | *"if the half-split **or** a basis rotation survives"* — **both** survive (§3.5) |
| `INSTANCE_ONLY` | **NO** | requires finite canonicity **proved**; it is refuted, not proved |
| `NO_VERDICT` | **NO** | reserved for distinct lawful mechanisms remaining and selection being required; §3.2 finds **no** mechanism derivable, so there is nothing to select between |

**`NONCANONICAL` is primary because control 1 carries it unconditionally.** The half-split needs no
unitary, no symmetry, and no equivalence class — it is an exact arithmetic refinement of a displayed
additive identity, with `D_K` and `D_K²` fixed. `LAW_GAP` is real and is reported at full strength,
but a verdict resting only on it would understate what was actually shown: the displayed
decomposition **fails** canonicity here; it is not merely **unaccompanied** by a law.

**What this does NOT establish**, held expressly:
- **No universal claim.** `PASS SCOPE` is the sealed finite parent and the verdict is negative anyway;
  nothing is promoted, and generic `U1` remains absent.
- **`U2_sq` is not refuted as a possible future law.** What is refuted is that the *displayed*
  decomposition is canonical at this parent. A future law supplying a genuine mechanism is untouched
  — and §3.3 bounds where it could reach: at most two orthogonally warranted blocks, and it would
  still owe a no-refinement ban.
- **Nothing is said about `U2_phys` or `Delta_Gamma`.** The false homonym is untouched, and the
  `Gamma_rest` termwise theorem is not startable. **In particular this finite result says nothing
  whatever about the `BOX_gravity` row of my 857.**

---

## 5. CONCEDED — CODEX'S CORRECTION OF MY 857

The U2 census §1 finds:

> *"857's sentence identifying its deciding object with `U2_sq` is an unproved cross-object
> identification. Its prior sentence remains valid: `Delta_Gamma` is missing. Its next sentence —
> 'under the U-ledger that object is U2' — does not follow from the sealed source types."*

**This is correct and I concede it.** At 857 I named the deciding object for the `BOX_gravity` typing
as *"a decomposition theorem / termwise identification for `Gamma_rest`"* — **that half stands** — and
then identified it with **U2**. That identification does not survive typing: the sealed `U2`
signature (`d_U2 : (B0_candidate,C0) -> U2`) contains no `D`, no `D^2`, no component, projector,
decomposition, irreducibility, or no-refinement receiver. I reasoned from the shared word
"decomposition" across objects with different domains and codomains.

**The conviction is clean, and Codex's own bridge hunt makes it sharper than it needed to:** of the
files containing both `Gamma_rest` and canonical-`U2` language, the only two are the settled register
and **my own 857 artifact** — with **zero** underlying source artifacts binding the two. **I was the
sole source of the bridge I cited.**

**Scope of the damage, stated precisely and not minimised:** 857's verdict (`NEITHER-FORCED`) and its
deciding-object identification *at the level of `Delta_Gamma`* are undamaged. What fails is the
routing sentence that sent that object to U2. Under the correct typing the deciding object is
`Delta_Gamma`, which this census types **not startable** — so the practical consequence is that
857's closing routing advice pointed at a startable-looking object when the real one is not startable.

**Two of my 858 items were confirmed by the same census** (§5.1 `PR3 = PRINCIPLED`; §5.2
`FIVE_TO_FOUR = CONFIRMED-BY-DISCHARGE`, with the correct caveat that it *"does not retroactively
make that trace new work of 855"* — which I did not claim).

---

## 6. FREEDOMS-CONSUMED (law 2, law 2a)

```text
CARRIED UNCHANGED: the three-object typing (U2_sq / U2_phys / Delta_Gamma) WITH NO BRIDGE BUILT; the
  sealed finite parent's carrier, domain, masks, incidence operators and derivative EXACTLY AS SEALED
  — no target-selected basis, grouping, scale, or component count was introduced anywhere; the
  displayed three-term identity carried as a DISPLAY, never adopted as a law; the packet bundle's own
  verdict (FINITE_CAUSAL_PARENT_DERIVED_CONTINUUM_COMPLETION_OPEN) untouched; generic U1 carried as
  ABSENT; Delta_Gamma carried as NOT STARTABLE.

DERIVED HERE: (a) an independent replay of D_K and D_K^2 agreeing with the sealed JSON to 12 decimals
  and reconstruction residual 0.000e+00; (b) the HS Gram of the census, giving <T1,T2> = +96 and the
  refutation of the orthogonal-projector/direct-sum route; (c) the record-grading probe showing T1 and
  T3 are MERGED by the only grading present; (d) the two-block orthogonal ceiling and its own failure;
  (e) both negative controls, with control 1 shown to be unconditional and control 2's conditionality
  disclosed; (f) the finding that the bundle seals NO admissible-relabeling stock, which is a gap in
  the relay's own INPUT FREEZE.

SELECTED HERE: NOTHING. No projector, grading, component count, irreducibility rule, no-refinement
  ban, relabeling group, equivalence relation, or basis is supplied, preferred, or adopted. The
  MECHANISM output is a DISPLAYED NEGATIVE, not a construction. NO FLAG MOVES.

NOT DONE AND DISCLOSED: I did not execute the sealed script — I re-implemented from its sealed
  definitions, so my replay agrees with the SEALED JSON rather than with a run of their code, which is
  the stronger check but leaves any latent script/JSON divergence untested BY ME (the bundle's own
  verification JSON and specification_seal_matches = true bear on that, and I did not audit them).
  Obligation (c) INVARIANCE is NOT discharged — reported as LAW_GAP rather than worked around. I did
  not attempt to construct the compensating source/record relabeling group; that is authorship.

SCALING WEIGHTS (law 2a): NONE CONSUMED — no component was rescaled except inside negative control 1,
  where the 1/2 factors are THE CONTROL ITSELF and are not carried anywhere else.  SUBSTITUTED: NONE.
```

**FLATTENING CHECK — 37/37 walked, clean.**
**S03 and THE VOID CONDITION — live and load-bearing three times.** (i) At §3.2, where no mechanism is
derivable and inventing a projector rule or grading would have produced a positive result — **none is
written**. (ii) At §3.4, where constructing the missing relabeling group would have let me "discharge"
INVARIANCE — **the gap is reported instead**. (iii) At §3.1, where declaring `INPUT_GAP` was the
cheapest exit from the relay — **it would have been false, and the replay was done**.
**S12** — every sealed flag carried as the status it is; the packet's displayed identity carried as a
display, never as a law. **S26 / S08 / S19 / S24** untouched — the construction is finite and
sealed; no smooth carrier, regularity class, or continuum measure is imported, and the finite
Galerkin data is not promoted. **T1 / T5** untouched.
**BR-1 HELD.** The packet bundle and the U2 census are producer-declared objects: they may accuse and
never exculpate. **The displayed decomposition was given no evidential weight toward its own
canonicity** — that is precisely what the FORBIDDEN clause bars and what control 1 refutes. Where the
census's obstruction turned out to be right, the warrant cited is my own replay, not the census.

---

## 7. FINAL LINES

```text
VERDICT = NONCANONICAL.  Both negative controls survive at the sealed finite parent, and NO canonicity
  mechanism is derivable from sealed structure.  Primary because CONTROL 1 CARRIES IT
  UNCONDITIONALLY: the half-split is an exact arithmetic refinement of a displayed additive identity
  with D_K and D_K^2 fixed, invoking no unitary, no symmetry and no equivalence class.  LAW_GAP also
  fires and is reported at full strength as a CO-FINDING (§3.4) — but a verdict resting only on it
  would understate what was shown: the displayed decomposition FAILS canonicity here, it is not merely
  UNACCOMPANIED by a law.  INPUT_GAP does NOT fire (§3.1) — recorded because declaring it was the
  cheapest exit from this relay and it would have been false.  INSTANCE_ONLY does not fire (finite
  canonicity is REFUTED, not proved).  NO_VERDICT does not fire (no mechanism remains to select
  between).  MECHANISM = NOT DERIVABLE, displayed as a negative and NOT supplied: the
  projector/direct-sum route is refuted by <T1,T2> = +96 != 0; the only grading present MERGES T1 and
  T3; and the bundle states no canonicity rule at all (canonical 0/0, irreducib 0/0, refine 0/0,
  component count 0/0 across SPEC and RESULT).
RECONSTRUCTION = displayed.  ||D_K^2 - (T1+T2+T3)|| = 0.000e+00 on an INDEPENDENT re-implementation
  from the sealed definitions (dim 108, D_K Hermitian to 0.000e+00).  Agreement with the sealed JSON
  to twelve decimals: overlap 16.000000000000 vs 16.0 ; derivative-support 9.797958971133 vs
  9.797958971132712 ; square identity error 0.000e+00 vs 0.0.  BONUS STRUCTURE: T3 is exactly
  orthogonal to both others, so the MAXIMAL ORTHOGONALLY SEPARABLE CENSUS IS TWO BLOCKS {T1+T2, T3},
  NOT THREE — the displayed census refines the only orthogonally warranted split, and EVEN THE
  TWO-BLOCK CENSUS FAILS BOTH CONTROLS.
INVARIANCE = NOT TESTABLE AS SPECIFIED — and this is a gap in the relay's own INPUT FREEZE, which
  freezes "admissible source/cell relabelings ALREADY SEALED in the packet bundle".  THE BUNDLE SEALS
  NONE: relabel 0/0, permut 0/0, admissible 0/0, equivalen 0/0 across SPEC and RESULT.  The one
  candidate an outside reader would try, the record-site swap, is NOT ADMISSIBLE — it moves the
  operator, ||SW D_K SW - D_K|| = 1.386e+01 — because the masks are attached in the source factor;
  repairing it needs a source reversal that flips the cyclic derivative.  CONSTRUCTING THE
  COMPENSATING GROUP WOULD BE AUTHORSHIP AND I STOPPED.
NEGATIVE_CONTROLS = BOTH SURVIVED.  (1) HALF-SPLIT: D_K^2 = T1 + T2 + (1/2)T3 + (1/2)T3, residual
  0.000e+00, count 3 -> 4, D_K AND D_K^2 UNCHANGED, nothing in the bundle banning refinement —
  UNCONDITIONAL.  (2) BASIS ROTATION at fixed cardinality, in its sharpest form: U = exp(i D_K) gives
  ||U D_K U* - D_K|| = 4.413e-14, THE SAME OPERATOR, yet a DIFFERENT Hermitian triple summing to the
  same square (component displacements 4.0848 / 10.2491 / 10.5344, norms preserved exactly).  SAME D,
  SAME CARDINALITY, TWO DECOMPOSITIONS — the components are NOT A FUNCTION OF D_K.  ITS HONEST LIMIT,
  STATED: U commutes with D_K, so a law identifying components up to symmetries of D would call the
  rotated triple equivalent — and whether that is permitted is exactly the equivalence found unsealed.
  CONTROL 2 IS CONDITIONAL ON THE LAW_GAP; CONTROL 1 IS NOT, AND CONTROL 1 ALONE SUFFICES.
PROMOTION = NOT-CLAIMED (finite scope held).  The verdict is negative so promotion is not at issue;
  the cap is held regardless.  Nothing is offered as the universal U2_sq law, generic U1 remains
  absent, U2_sq is NOT refuted as a possible future law (only the DISPLAYED decomposition is refuted
  at this parent), and NOTHING is said about U2_phys or Delta_Gamma.  IN PARTICULAR THIS SAYS NOTHING
  WHATEVER ABOUT THE BOX_gravity ROW OF MY 857.
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+3):
  (1) I CONCEDE CODEX'S CORRECTION OF MY 857 IN FULL, AND IT IS THE SHARPEST CONVICTION OF THE
      SESSION.  I identified 857's deciding object with U2 on the strength of the shared word
      "decomposition" across objects with different domains and codomains.  Codex's bridge hunt found
      that of the files binding Gamma_rest to canonical-U2 language, the only two are the settled
      register and MY OWN 857 — zero underlying sources.  I WAS THE SOLE SOURCE OF THE BRIDGE I CITED.
      857's verdict and its Delta_Gamma identification stand; the routing sentence does not, and the
      practical consequence is that 857 pointed at a startable-looking object when the real one is
      typed NOT STARTABLE.
  (2) THE VERDICT I RETURN IS THE ONE MY OWN INSTRUMENT WAS BUILT TO FIND.  I wrote the negative
      controls' harness and then reported that both survive; the controls come from the obstruction
      span, not from me, but the replay, the Gram probe, and the grading probe are all mine and
      un-cross-checked.  The strongest single number here (0.000e+00 on the half-split) is
      arithmetically trivial and therefore hard to get wrong; THE PROBES IN §3.2 ARE NOT, AND THEY
      ARE THE PART MOST WORTH ATTACKING.
  (3) I DID NOT DISCHARGE OBLIGATION (c) AND DID NOT WORK AROUND IT.  INVARIANCE is returned as a
      gap in the relay's own INPUT FREEZE.  Reporting that the instruction's presupposed stock does
      not exist is a harder thing to be right about than reporting a computation, and it rests on
      absence counts (relabel 0/0, permut 0/0, admissible 0/0, equivalen 0/0) — a POSITIVE ABSENCE,
      the exact shape law 9 governs.  ITS ENUMERATION IS TWO FILES, THE SPEC AND THE RESULT, AND I
      STATE THAT SCOPE RATHER THAN IMPLYING A CORPUS-WIDE SWEEP.
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

---

**GATES HELD.** Charter fences live; nothing selected; no smooth import; no EM identification; no
member binding; no fixed-point execution; no end test; **no numeric evaluation of any physical
quantity**; no comparison to measured constants; no common cell formed; no junction map evaluated.
PE-1..PE-12 pointer-only, none opened or consulted. Builder-B independence held — no Builder-A code
opened; the `scripts/`+`tests/` read here are the relay's own named subjects. `~/.codex` untouched;
memory-bank never searched. No register, plan, tracker, or git action.
