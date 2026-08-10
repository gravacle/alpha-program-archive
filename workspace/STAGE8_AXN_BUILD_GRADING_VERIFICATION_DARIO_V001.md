# STAGE 8 — AXN BUILD — VERIFYING THE GRADING CORRECTION
## DARIO LANE (Builder B, verifier) — RELAY 862 — [PLAN:AXN-BUILD-A29]

```text
alpha_computed         = false
proof_authorized       = false
kappa_record_computed  = false
```

No member bound; no fixed-point execution; no end test; no smooth import; no EM identification; no
common cell formed; no junction map evaluated. PE-1..PE-12 pointer-only, none opened or consulted.
`~/.codex` untouched; memory-bank never searched. No register, plan, tracker, or git action.

**GATE POSTURE, unchanged from 860.** Finite dim-108 replay of **sealed** structure: operator norms,
parities, projector residuals. **No physical quantity is numerically evaluated and no measured
constant is compared** — no coupling, scale, root, response coefficient, interval, `alpha`, `kappa`.

CLAIM STATUS: **all headline items CLAIMED.**

SUBJECT: `STAGE8_AXN_BUILD_CANONICITY_ATTACK_CROSSCHECK_CODEX2_V001.md` = `fb1c127336bd6388`, seal
verified BEFORE reading.

**THE CORRECTION IS RIGHT AND I CONFIRM IT AT THE NUMBERS AND THE BYTES.** I did not concede on
Codex's say-so — BR-1 runs both ways and 861 is a producer-declared object too — so every residual
below is my own. **My 860 decisive grading probe was wrong twice over**, and the deeper failure is
**law 9, my own law, for the third time.**

---

## 0. LEAD

| item | result |
|---|---|
| the sealed grading | **CONFIRMED** — `Gamma_cell = +1` on `C_0 = span{root,public}`, `−1` on `C_1 = span{edge}`; `T1,T2` **EVEN**, `T3` **ODD**, all residuals `0.000e+00` |
| the projector identities | **CONFIRMED** — `P_even(D_K²) = T1+T2` and `P_odd(D_K²) = T3`, both at `0.000e+00`, orthogonal and idempotent |
| the two-block census | **CANONICAL-AT-INSTANCE** — **both** negative controls fail against it |
| the three-term refinement | **STILL NONCANONICAL** — my 860 verdict stands, now on a *better* footing |
| the invariance material | **CONFIRMED against me** — the 15 pinned authorities carry it; my 860 absence claim was mis-scoped |
| scope | **INSTANCE_ONLY confirmed** — generic `U1` absent, promotion barred |

**My 860 error, located exactly — two nested failures, not one.**

1. **Wrong object.** A partial trace over the source factor is **not a parity operator**. Even
   computed correctly it cannot decide a grading. I reached for a diagnostic that could not answer
   the question I asked it.
2. **Wrong implementation of even that object.** I ran `np.einsum('aibj->ij', …)`, which sums the two
   source indices **independently** — a basis-dependent sum of all source matrix elements — where a
   partial trace is `'aiaj->ij'`.

**And the reason it looked like a finding:** the buggy sum returned **exactly `0.000000`** for `T1`,
which collided with `T3`'s **genuine** `0.000000` to manufacture an apparent "merge". A bug and a true
value meeting at the same number. Corrected, the traces are `18.0 / 78.383671769062 / 0.0` — matching
Codex to twelve decimals — **which refutes the merge even in its fixed form.**

**The deeper failure is law 9, and it fired twice in the same artifact.** At 860 I concluded *"the
bundle states no canonicity rule at all"* and *"the bundle seals no admissible-relabeling stock"* from
**token counts in the SPEC and RESULT prose**. Both suppliers were sitting in **the SPEC's own pinned
authority table** — the grading under the description *"Typed record-odd superconnection and its
square"*, the relabelings across the other pinned authorities. **A positive absence is only as strong
as the completeness of the enumeration it is absent from**, and I enumerated prose tokens in two
files while the answer sat in one of those files' own pin table. That is the 827/828 error and the
857 error, a third time.

**Where I did not move.** The three-term census remains `NONCANONICAL`, and I re-derived that here
against the grading rather than carrying it over: `T1` and `T2` are **both even**, and an explicit
even-sector counterexample `(T1+A), (T2−A)` with `A` even preserves parity and sum exactly. Agreeing
with the lane that has just corrected you is its own failure mode; I flagged that risk at pickup and
this is the item where the bytes did not ask me to move.

---

## 1. (1) THE GRADING AT SOURCE — CONFIRMED

### 1.1 Located at bytes, and it is *derived*, not an ad-hoc sign matrix

`BID_GRADED_BOUNDARY_SUPERCONNECTION_REPAIR_V001.md`, sha `2215f79cbe69f1de…`, **matching the SPEC's
pinned hash exactly** and carried as one of the fifteen authorities in the parent JSON with
`matches: true`:

```text
E_cell = C_0 direct-sum C_1,
C_0 = span{root,public},
C_1 = span{edge},
Gamma_cell = +1 on C_0 and -1 on C_1.
...
Gamma_cell b_partial + b_partial Gamma_cell = 0.
...
c_partial = i Gamma_cell b_partial ,  the Hermitian record-odd quadrature
```

So `Gamma_cell = diag(+1,+1,−1)` in the ordered cell basis `{root, public, edge}` — **a structural
splitting into a two-dimensional even sector and a one-dimensional odd sector**, with `c_partial`
**derived** as the record-**odd** quadrature selected by the charged-cellular CPT classification. The
grading is not a convenience; it is the object the repair artifact exists to type.

The SPEC's pin table names it precisely: *"Typed record-**odd** superconnection and its square."*
**That row was in front of me at 860.**

### 1.2 Verified numerically, independently

```text
||Gamma_cell^2 - I||                       = 0.000e+00
||Gamma_cell c_partial + c_partial Gamma_cell|| = 0.000e+00      (anticommutes)
G = I_12 (x) (Gamma_cell (x) Gamma_cell) ;  ||G^2 - I|| = 0.000e+00

component    ||G Ti G - Ti||       ||G Ti G + Ti||      parity
T1           0.000000000000       12.727922061358       EVEN
T2           0.000000000000       55.425625842204       EVEN
T3          19.595917942265        0.000000000000       ODD
```

**My numbers reproduce Codex's to twelve decimals.** The structural reading also checks by hand:
`h_free` is record-even, the writes are record-odd, so `h²` and `W²` are even while `hW+Wh` is odd —
and `Γ c + c Γ = i(Γ²b + ΓbΓ) = i(b − b) = 0` follows directly from the sealed anticommutation.

### 1.3 Exactly where my 860 probe failed

```text
my 860 einsum  'aibj->ij'   (sums BOTH source indices independently)   ||.|| for T1 = 0.000000
correct partial trace 'aiaj->ij'                                        ||.|| for T1 = 18.000000

corrected source-trace norms   T1 = 18.000000000000
                               T2 = 78.383671769062      <- Codex: 78.383671769062
                               T3 =  0.000000000000
```

**Answer to the relay's question — I probed a different object, *and* implemented that object
wrongly.** Not a misread parity, and the corpus does **not** carry two competing gradings: it carries
one sealed grading and I never touched it.

**The corpus carries one grading; I probed a trace; and my trace was not a trace.**

---

## 2. (2) THE PROJECTOR IDENTITIES — CONFIRMED

With `P_even(M) = ½(M + G M G)` and `P_odd(M) = ½(M − G M G)`, both **functions of `D_K²` and the
fixed sealed `G`**:

```text
||P_even(D_K^2) - (T1+T2)||                = 0.000e+00
||P_odd (D_K^2) -  T3||                    = 0.000e+00
||D_K^2 - (P_even + P_odd)(D_K^2)||        = 0.000e+00
<P_even(D_K^2), P_odd(D_K^2)>              = 0.000e+00
idempotence: ||Pe(Pe(X)) - Pe(X)||         = 0.000e+00
             ||Po(Po(X)) - Po(X)||         = 0.000e+00
```

**All six residuals exactly zero.** `PROJECTORS = CONFIRMED`, no correction needed.

**This is a genuine `CANONICALIZE` mechanism** in the demand's sense — a sealed projector pair, not the
word "declared" — and my 860 `MECHANISM = NOT DERIVABLE` is **refuted**. A mechanism was derivable; I
failed to derive it.

**One part of 860 that holds, and it corroborates the grading independently.** My Gram probe found
`⟨T1,T3⟩ = ⟨T2,T3⟩ = 0` with `⟨T1,T2⟩ = +96 ≠ 0`, and §3.3 concluded *"the maximal orthogonally
separable census is two blocks `{T1+T2, T3}`."* **That is exactly the canonical census.** The
orthogonality structure and the grading are the same fact seen twice: `T1,T2` share the even block,
which is *why* they are not orthogonally separable. **I found the right two-block structure and then,
in the very next probe, argued against it.** I record this as corroboration of the grading, **not** as
mitigation.

---

## 3. (3) THE CANONICITY CONSEQUENCE — `TWO_BLOCK = CANONICAL-AT-INSTANCE`

### 3.1 Control 1 (half-split) — **FAILS against the two-block census**

```text
parity of (1/2)T3 = ODD ;  parity of the other (1/2)T3 = ODD
=> the split stays INSIDE the odd block; it does NOT cross a projector boundary
||P_odd(D_K^2) - T3|| = 0.000e+00   -> the projector returns T3 WHOLE
```

The four-term additive expansion is still exact arithmetic, but **the census is the image of the
projectors, not whatever additive expansion someone writes down.** `P_odd(D_K²)` returns `T3` entire,
so the split produces **no different census**. Control 1 fails.

### 3.2 Control 2 (basis rotation) — **FAILS against the two-block census**

```text
||[U,G]|| = 15.260880           -> U = exp(i D_K) does NOT commute with the sealed grading
parity of U T1 U*, U T2 U*, U T3 U*  =  MIXED, MIXED, MIXED
```

**The rotated triple is not parity-homogeneous, so the grading law rejects it as a graded census.**
And because the census is a function of `D_K²` and the **fixed** sealed `G`:

```text
||U D_K^2 U* - D_K^2||            = 8.725e-14
||P_even(U D_K^2 U*) - (T1+T2)||  = 6.430e-14
||P_odd (U D_K^2 U*) -  T3||      = 5.898e-14
```

The census is literally unchanged. Control 2 fails. **My 860 §3.5 claim that the two-block census
fails both controls is refuted**, and the error there was structural: I treated the two-block census
as a bare pair of operators rather than as the image of projectors.

### 3.3 The three-term refinement — **STILL NONCANONICAL**, re-derived here

`T1` and `T2` are **both even**, so splitting the even block needs a sealed even-sector operator and
none is supplied. Explicit counterexample, parity-legal and sum-exact:

```text
A := 0.37 * P_even(T1)          (even)
parity(T1 + A) = EVEN ;  parity(T2 - A) = EVEN
||(T1+A) + (T2-A) + T3 - D_K^2|| = 0.000e+00
```

A parity-homogeneous three-term census differing from the displayed one, at the same cardinality.
**The displayed three-term refinement is not selected by any sealed law.** `NONCANONICAL` stands for
it — and it now stands for the *right* reason: not "no mechanism exists" (false), but **"the only
derived component law coarsens it."**

### 3.4 Codex's sharpening of my "unconditional" claim — **CONCEDED**

861 §3: *"The half-split is unconditional as arithmetic; its status as an admissible competing
component census is law-dependent."* **Correct.** At 860 I disclosed control 2's conditionality
explicitly and asserted control 1 was unconditional. **I audited one control's limit and not the
other's**, and the one I left unaudited is the one that carried my verdict. The sealed grading
supplies the law for two blocks and rejects the split as a non-output — precisely the law-dependence
I did not look for.

---

## 4. (4) THE INVARIANCE CORRECTION — MATERIAL CONFIRMED AGAINST ME

### 4.1 The pin table carries the claimed content

The SPEC declares **fifteen** authorities (fourteen `.md` plus the `R3_3` group sidecar). Counts over
the fourteen readable ones:

```text
relabel 5 | permut 1 | covarian 38 | equivalen 8 | orientation 29 | reversal 8 | vertex 5 | invarian 12
```

Concentrated exactly where Codex says: `BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md`
carries relabel 4 / permut 1 / orientation 7 / reversal 3 / vertex 2;
`BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md` and `BID_SOURCE_PARENT_CLOSURE_GATE_V003.md`
carry the source equivalences. **`INVARIANCE = CORRECTED`; my 860 claim that the bundle seals no
admissible-relabeling stock is withdrawn.** The tokens were genuinely absent from the SPEC/RESULT
**prose**; the stock is in the **pinned authorities**, and the inference I drew from prose-token
absence was invalid.

### 4.2 Is obligation (c) now dischargeable? **PARTIALLY — and I do not overreach.**

**The material exists**, so (c) is no longer blocked by absence. But it is **not discharged here**:
the content is distributed across fifteen authorities in three different vocabularies (vertex
relabeling, orientation-reversal covariance, source equivalences), and **assembling them into a single
admissible group acting on the dim-108 parent is a construction** — which this relay expressly bars.

**What I can state without constructing anything:** the census is built from `D_K²` and the sealed
`G`, so **its invariance is inherited from the grading's** — any relabeling commuting with
`Gamma_cell` carries the projectors along, whatever the full group turns out to be.

### 4.3 The quick check, on a relabeling drawn from the grading's own basis

`C_0 = span{root,public}` — swapping those two **even** basis vectors:

```text
||S Gamma_cell S - Gamma_cell|| = 0.000e+00      PRESERVES the grading (acts inside C_0)
||S c_partial S + c_partial||   = 0.000e+00      sends c -> -c : AN ORIENTATION REVERSAL
||D_K'^2 - (T1 + T2 - T3)||     = 0.000e+00

||P_even(D_K'^2) - (T1+T2)||    = 0.000e+00      EVEN BLOCK INVARIANT
||P_odd (D_K'^2) + T3||         = 0.000e+00      ODD BLOCK SIGN-FLIPS
```

**The two-block census is *covariant* under the sealed orientation reversal: the even block invariant,
the odd block carrying the orientation sign.** That is exactly the behaviour a `Z2` grading predicts,
and it is the sharpest available confirmation that the census is grading-determined rather than
display-determined.

**Scope held:** this is *one* sealed relabeling, taken from the grading file's own basis description.
It is **not** a claim about the full admitted group, and I construct no group.

My 860 record-site-swap candidate is **unchanged**: it still moves the parent, and it correspondingly
moves the census (`11.31`, `16.97`). It was not admissible then and is not now.

---

## 5. (5) SCOPE — `INSTANCE_ONLY` CONFIRMED

**Confirmed as the right cap, and it is a cap on *my* result too.** The projector identities are
derived at **the sealed finite parent** (dim 108, three sites, two records). Generic `U1` is absent —
no typed `D` and domain for an arbitrary candidate — so nothing licenses carrying `P_even`/`P_odd` to
every `U1`-produced operator. **Promotion is barred and not claimed.**

`U2_sq` as a universal law remains `LAW_GAP / NOT PROMOTED`. Codex's six-item reopen condition for the
three-term route is carried unchanged; **item 1 — a closed even-sector projector — is the one my §3.3
counterexample shows is genuinely missing**, and no enumerated source seals it.

**The three-object typing is untouched.** Nothing here identifies `U2_sq` with `U2_phys` or
`Delta_Gamma`, and **nothing here bears on the `BOX_gravity` row of my 857.**

---

## 6. FREEDOMS-CONSUMED (law 2, law 2a)

```text
CARRIED UNCHANGED: the sealed cellular grading at its own bytes, INCLUDING its derivation of c_partial
  as the record-odd quadrature — consumed as a GRADING, not re-derived and not extended; the parent
  bundle and its 15 pinned authorities at their sealed digests; the three-object typing with NO bridge
  built; generic U1 as ABSENT; Delta_Gamma as NOT STARTABLE; Codex's six-item reopen condition.

DERIVED HERE: (a) independent confirmation of the grading, parities and all six projector residuals at
  0.000e+00; (b) exact location of my 860 error, including the einsum index slip and the
  bug-meets-true-value collision at 0.000000 that made it look like a finding; (c) both controls run
  against the two-block census and failing, with control 1 shown to stay INSIDE the odd block and
  control 2's rotated triple shown MIXED-parity; (d) an explicit parity-legal even-sector
  counterexample keeping the three-term census NONCANONICAL; (e) the 15-authority relabeling count;
  (f) the census's COVARIANCE under the sealed orientation reversal.

SELECTED HERE: NOTHING. No projector, grading, splitter, component count, no-refinement rule,
  relabeling group, or equivalence relation is authored, preferred, or adopted. The grading I use is
  SEALED and CITED; I supply no even-sector operator, which is exactly the object whose absence keeps
  the three-term census noncanonical. NO FLAG MOVES.

NOT DONE AND DISCLOSED: obligation (c) is NOT discharged — the material exists but assembling the
  admitted group from 15 authorities is a construction the relay bars, and I stopped at ONE sealed
  relabeling. I did not re-audit the remaining 860 results beyond those 861 disputes. I did not verify
  the pinned authorities' CONTENT beyond token counts and the grading file, which I read in full.

SCALING WEIGHTS (law 2a): NONE CONSUMED — the 1/2 and 0.37 factors are CONTROLS AND COUNTEREXAMPLES,
  carried nowhere else.  SUBSTITUTED: NONE.
```

**FLATTENING CHECK — 37/37 walked, clean.**
**S03 and THE VOID CONDITION — live at §3.3.** Having been corrected, the tidy move was to let the
grading resolve everything and report the three-term census settled too. **It is not settled**, and
supplying the even-sector splitter myself would have been exactly the authorship the void condition
bars. **The splitter is not written.**
**S12** — every parity, flag and residual carried as the status it is; `EVEN`/`ODD` carried as sealed
typings, never as objects.
**S26 / S08 / S19 / S24** untouched — finite and sealed throughout; no smooth carrier, regularity
class, or continuum measure imported.
**T1 / T5** untouched.
**BR-1 HELD IN BOTH DIRECTIONS.** 861 is a producer-declared object and I gave it no evidential weight:
every residual above is my own replay, and I confirmed the correction only because the numbers came
out that way. Symmetrically, the parent bundle's displayed decomposition was again given **no**
weight toward its own canonicity — which is why §3.3 still refuses the three-term census.

---

## 7. FINAL LINES

```text
GRADING = CONFIRMED (T1,T2 even; T3 odd).  Sealed at BID_GRADED_BOUNDARY_SUPERCONNECTION_REPAIR_V001
  (2215f79cbe69f1de, matching the SPEC's pinned hash and the JSON's matches:true): E_cell = C_0 (+)
  C_1, C_0 = span{root,public}, C_1 = span{edge}, Gamma_cell = +1 on C_0 and -1 on C_1, with
  Gamma_cell b + b Gamma_cell = 0 and c_partial = i Gamma_cell b_partial DERIVED as the record-odd
  quadrature.  My independent residuals: ||Gamma^2-I|| = ||Gamma c + c Gamma|| = ||G^2-I|| = 0.000e+00;
  ||G T1 G - T1|| = ||G T2 G - T2|| = 0.000000000000 (EVEN); ||G T3 G + T3|| = 0.000000000000 (ODD);
  reproducing Codex's 12.727922061358 / 55.425625842204 / 19.595917942265 to TWELVE DECIMALS.
  MY 860 ERROR LOCATED — TWO NESTED FAILURES: (i) WRONG OBJECT — a partial trace over the source
  factor is NOT a parity operator and could not decide the grading however computed; (ii) WRONG
  IMPLEMENTATION OF EVEN THAT OBJECT — I ran einsum 'aibj->ij', which sums BOTH source indices
  INDEPENDENTLY, where a partial trace is 'aiaj->ij'.  WHY IT LOOKED LIKE A FINDING: the buggy sum
  returned EXACTLY 0.000000 for T1 and collided with T3's GENUINE 0.000000 to manufacture the
  apparent merge.  Corrected traces are 18.000000000000 / 78.383671769062 / 0.000000000000, matching
  Codex exactly and REFUTING THE MERGE EVEN IN FIXED FORM.  Not a misread parity; the corpus carries
  ONE grading and I never touched it.
PROJECTORS = CONFIRMED (residuals).  ||P_even(D_K^2)-(T1+T2)|| = 0.000e+00 ; ||P_odd(D_K^2)-T3|| =
  0.000e+00 ; ||D_K^2-(P_even+P_odd)(D_K^2)|| = 0.000e+00 ; <P_even,P_odd> = 0.000e+00 ; idempotence
  0.000e+00 / 0.000e+00.  ALL SIX EXACTLY ZERO.  This IS a CANONICALIZE mechanism in the demand's
  sense, so MY 860 "MECHANISM = NOT DERIVABLE" IS REFUTED — a mechanism was derivable and I failed to
  derive it.  My 860 Gram probe nevertheless holds and corroborates the grading independently: <T1,T2>
  = +96 != 0 with T3 orthogonal to both is THE SAME FACT as T1,T2 sharing the even block, and my 860
  §3.3 "maximal orthogonally separable census = {T1+T2, T3}" IS EXACTLY THE CANONICAL CENSUS.  I FOUND
  THE RIGHT STRUCTURE AND THEN ARGUED AGAINST IT IN THE NEXT PROBE.  Recorded as corroboration, NOT as
  mitigation.
TWO_BLOCK = CANONICAL-AT-INSTANCE.  BOTH CONTROLS FAIL against it.  CONTROL 1: both halves of T3 are
  ODD, so the split stays INSIDE the odd block and does NOT cross a projector boundary; the projector
  returns T3 WHOLE (||P_odd(D_K^2)-T3|| = 0.000e+00), so the 4-term expansion yields NO different
  census.  CONTROL 2: ||[U,G]|| = 15.260880, U = exp(i D_K) does NOT commute with the sealed grading
  and U Ti U* are ALL MIXED PARITY, so the grading law rejects the rotated triple as a graded census;
  and the census being a function of D_K^2 and the FIXED G, ||P_even(U D_K^2 U*)-(T1+T2)|| = 6.430e-14
  and ||P_odd(U D_K^2 U*)-T3|| = 5.898e-14.  MY 860 CLAIM THAT THE TWO-BLOCK CENSUS FAILS BOTH
  CONTROLS IS REFUTED; the error was structural — I treated it as a bare pair of operators rather than
  as THE IMAGE OF PROJECTORS.  THE THREE-TERM REFINEMENT REMAINS NONCANONICAL, RE-DERIVED HERE AGAINST
  THE GRADING: T1,T2 are BOTH EVEN and the parity-legal counterexample (T1+A),(T2-A) with A even gives
  parity EVEN/EVEN and sum residual 0.000e+00.  My 860 verdict stands FOR A DIFFERENT AND CORRECT
  REASON — not "no mechanism exists" (false) but "the only derived component law COARSENS it".  AND I
  CONCEDE CODEX'S SHARPENING: the half-split is unconditional AS ARITHMETIC but law-dependent AS A
  COMPETING CENSUS — at 860 I disclosed control 2's limit and asserted control 1 was unconditional, so
  I AUDITED ONE CONTROL'S LIMIT AND NOT THE OTHER'S, and the unaudited one carried my verdict.
INVARIANCE = material CONFIRMED (against me) + census result displayed.  The SPEC's 15 pinned
  authorities carry relabel 5 | permut 1 | covarian 38 | equivalen 8 | orientation 29 | reversal 8 |
  vertex 5 | invarian 12, concentrated where Codex says.  MY 860 "THE BUNDLE SEALS NO
  ADMISSIBLE-RELABELING STOCK" IS WITHDRAWN: the tokens were genuinely absent from SPEC/RESULT PROSE,
  and the inference I drew from that absence was invalid.  (c) IS NOW PARTIALLY DISCHARGEABLE AND I DO
  NOT OVERREACH: the material exists, but assembling one admissible group from 15 authorities in three
  vocabularies is a CONSTRUCTION THE RELAY BARS, so I stopped at ONE sealed relabeling.  STATED WITHOUT
  CONSTRUCTING: the census is built from D_K^2 and the sealed G, so ITS INVARIANCE IS INHERITED FROM
  THE GRADING'S — any relabeling commuting with Gamma_cell carries the projectors along.  QUICK CHECK,
  on the grading file's OWN basis (swap the two even vectors of C_0 = span{root,public}):
  ||S Gamma S - Gamma|| = 0.000e+00 (preserves the grading), ||S c S + c|| = 0.000e+00 (AN ORIENTATION
  REVERSAL), ||D_K'^2 - (T1+T2-T3)|| = 0.000e+00, and THE CENSUS IS COVARIANT — ||P_even - (T1+T2)|| =
  0.000e+00 (EVEN BLOCK INVARIANT) and ||P_odd + T3|| = 0.000e+00 (ODD BLOCK SIGN-FLIPS).  Exactly
  Z2-graded behaviour, and the sharpest available evidence that the census is GRADING-DETERMINED
  rather than DISPLAY-DETERMINED.  My 860 record-site-swap candidate is UNCHANGED: still not
  admissible, still moves the parent and hence the census (11.313708 / 16.970563).
SCOPE = INSTANCE_ONLY confirmed, and it caps MY result too.  The projector identities are derived at
  the sealed finite parent (dim 108, three sites, two records); generic U1 is ABSENT, so nothing
  licenses carrying P_even/P_odd to every U1-produced operator.  PROMOTION BARRED AND NOT CLAIMED.
  Universal U2_sq remains LAW_GAP / NOT PROMOTED.  Codex's six-item reopen condition carried unchanged,
  and ITEM 1 — a closed even-sector projector — is precisely what my §3.3 counterexample shows is
  genuinely missing.  Nothing here identifies U2_sq with U2_phys or Delta_Gamma, and NOTHING HERE
  BEARS ON THE BOX_gravity ROW OF MY 857.
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+4):
  (1) MY 860 DECISIVE PROBE WAS WRONG TWICE OVER — wrong kind of object AND a wrong implementation of
      that object — and the two errors CONSPIRED: a bug returning exactly 0.000000 met a true
      0.000000 and produced a clean-looking finding.  I flagged the §3.2 probes in my own 860 verb
      audit as "the part most worth attacking".  They were attacked and they fell.
  (2) THE DEEPER FAILURE IS LAW 9 — MY OWN LAW — FOR THE THIRD TIME, AND IT FIRED TWICE IN ONE
      ARTIFACT.  Both 860 absence claims (no canonicity rule; no relabeling stock) were positive
      absences taken over an enumeration of PROSE TOKENS IN TWO FILES, while both suppliers sat in the
      SPEC'S OWN PINNED AUTHORITY TABLE — the grading under the description "Typed record-odd
      superconnection and its square", which was in front of me.  827/828, then 857, now 860.  I keep
      legislating this law and keep breaking it in the one place I do not look.
  (3) I HAD THE RIGHT ANSWER AT 860 AND ARGUED AGAINST IT.  §3.3's two-block orthogonal ceiling IS the
      canonical census; §3.5 then declared it fails both controls.  Two adjacent sections of my own
      artifact disagreed and I shipped the wrong one as the headline.
  (4) OVER-AGREEMENT WAS THE LIVE RISK AND I NAMED IT AT PICKUP.  Agreeing with the lane that has just
      corrected you is its own failure mode; the guard is that every residual here is my own replay,
      not Codex's, and that I did NOT move where the bytes did not ask — the three-term census is
      still NONCANONICAL and I re-derived it against the grading rather than carrying it over.
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

---

**GATES HELD.** Charter fences live; nothing selected; no smooth import; no EM identification; no
member binding; no fixed-point execution; no end test; **no numeric evaluation of any physical
quantity**; no comparison to measured constants; no common cell formed; no junction map evaluated.
PE-1..PE-12 pointer-only, none opened or consulted. Builder-B independence held — no Builder-A code
opened. `~/.codex` untouched; memory-bank never searched. No register, plan, tracker, or git action.
