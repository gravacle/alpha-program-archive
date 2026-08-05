# STAGE 8 TASK 5 / EQ6 — CROSS-FAMILY REVIEW OF RECORD: THE MEMBERSHIP THEOREM — DARIO V001

Date: 2026-08-05
Lane: Dario (Claude Opus 5), cross-family reviewer
Task: PASTE 560 / Task 5 / EQ6
Custody: review of record on a build produced by a different model family. Re-derived, not trusted.

## Lead result

```text
REGISTER_HEAD = Q-487
ARTIFACT_UNDER_REVIEW = STAGE8_TASK5_EQ6_MEMBERSHIP_THEOREM_LANE3_V001.md
  sha256 0d00c9cfdb7187d45bb7892a5f71131b2cf1e0d5b17f871bdde3a770de2c0ae6 (VERIFIED)

HASH_DEFECTS = none (21 of 21 stated hashes verify exactly)
CIRCULARITY = NOT FOUND (the historic circular-pi_Mx regression did NOT recur)
FC2_REPAIR = GENUINE (new mathematics, not an amendment)
J4_ALGEBRA = RECOMPUTED AND CORRECT
FC9_PUSHOUT_INJECTIVITY = RECOMPUTED AND CORRECT
CONTRACT_MATCH = RECOMPUTED AND EXACT

D1 = KILL   (scope-shrink: guard generator clause (vi) absent from Mor(I_F))
D2 = KILL   (FC6 over-claim; J2 A_RP half posed, not proved)
D3 = KILL   (J7 discharged by J2's own equation; FC11's two faces supplied by one)
D4 = MIXED  (citation drift not cured, only relabelled; look-alike NOT found; circularity NOT found)
D5 = PASS with NOTES (consequence typed correctly; tag discipline inconsistent)
D6 = KILL   (status-verb audit: five rows report a stronger verb than their sources carry)

MEMBERSHIP = DEFECTIVE (+D1, +D2, +D3, +D6)
READY_FOR_AXIOM_READJUDICATION = no

MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The build is not a fraud and it is not sloppy in its arithmetic. Every hash it states is
correct, its central algebra is correct where it shows the algebra, and the two failure modes
the program most feared — circular `pi_Mx` and look-alike substitution — did **not** recur.
The defect is of a different kind, and it is systematic: **at five points the build reports a
status its own cited sources do not carry**, and at one point it proves its theorem over a
smaller index category than the guard defines. Those are recoverable. They are not recoverable
by re-reading; they need construction.

## 0. Preflight

### 0.1 Access, no-clobber, register

| Check | Result |
|---|---|
| Cleanroom, archive workspace, supervision readable | PASS — all three returned entries |
| Output name absent before construction | PASS — `STAGE8_TASK5_EQ6_MEMBERSHIP_REVIEW_DARIO_V001.md` absent from workspace and cleanroom |
| Register head | Q-487 verified. Q-487 records this build as PROVEN **pending the cross-family review**. This artifact is that review. |
| Build's own head claim (Q-486) | Correct for its time; Q-487 is the row the build itself generated. |

### 0.2 Hash verification — every hash recomputed before reading

All 21 hashes stated by the build were recomputed with `shasum -a 256`. **All 21 match exactly.**

| Class | Count | Result |
|---|---|---|
| Commissioned archive objects (build §0.2) | 10 | 10/10 match |
| Sealed component stock (build §0.4) | 7 | 7/7 match |
| Ratified amended rows (build §0.3) | 4 | 4/4 match |

Additionally verified, not cited by the build: axiom V001 `66c71bb6…`, adjudication `9fe38e93…`,
constraint arm `96cd90b5…`, A6's own basis `088eccd9…` / `e104c092…`, the killed assembly
`e21cee30…`, its successor `e5381e66…`.

**Custody note of record.** The guard file does **not** contain the text of FC1–FC11/FC13. It
incorporates them by reference from axiom V001 (`66c71bb6…`, §1.2). Any lane walking the guard
condition-by-condition must open V001. This review did.

## 1. D1 — the tuple and the index category

### 1.1 What is correct

**The tuple itself is one tuple, and it has not drifted.** I enumerated the guard's B1.2 list
and the build's §1.2 list independently: thirteen components, **same names, same order**
(`rho_fin` and `j_fin` share a display line in the guard, which accounts for the apparent
12-vs-13). No component is dropped, renamed, split, or added. PASS.

**The compression is faithful.** The build's §1.2 compressed package

```text
F_actual(N) = (Act_N, P_N, Bot_N, Aux_N)
F_actual(f) = (Rel_f, Eta_f, BotStruct(f;r_f^Bot), Aux_f)
Bot_N = (Gate1-4_N, Q243_N, Q279_N, Q309_N, Q408_N, ActionBottom_N,
         WardBottom_N, ReaderBottom_N, WhereBottom_N, C1FaithBottom_N)
```

is **character-identical** to `F_003` in H_ASM3 lines 119, 125 and `(PKG-1)` at H_ASM3 lines
135–137. The build transcribed the confirmed object correctly. PASS.

**`K_f^new` is correctly excluded.** H_A6 lines 9–12 retain full J2 on the new-cycle factor as
"an explicitly typed POST-SCOPE CONDITION". The build's §1.1 declaration
`K_f^new in Components(F_actual) = false` is licensed by ratified law, not by builder
convenience. PASS.

### 1.2 KILL — the index category is smaller than the guard's

The guard defines `Mor(I_F)` by six generator clauses (guard B1.1, lines 232–240). Clause (vi) is:

> (vi) every finite-bottom arrow needed by a sealed package consumer

and the guard labels it explicitly at line 246:

> Including item (vi) is the anti-shrink clause. Omitting an active finite consumer or
> restricting to the one-generator `I_flip` category would repeat the Q-451 scope error.

The build's `Mor(I_F)` (lines 110–130) is

```text
Mor(I_F) := the finite closure of A_iso union A_RP union A_CC union A_CR
            under identities and the sealed admissible compositions.
```

Each of the four classes is defined by an **intrinsic geometric property** — isomorphism,
rank-preserving restriction, cycle-creating attachment, common-refinement leg. **None is indexed
by consumer demand.** Closure under composition cannot manufacture a generator that no class
admits.

Recomputed directly:

```text
grep -c "consumer"  guard  -> 10
grep -c "consumer"  build  ->  0
```

The concept that *defines* clause (vi) does not occur anywhere in the 562-line build.

**Why this is a KILL and not a bookkeeping note.** The guard's FC2 failure was not witnessed
generically. It was witnessed at B2.2 on exactly this class of arrow:

> Take an active finite consumer outside the one-generator flip bottom. Its Q-408 restriction
> exists, but the corresponding package R1/C2/C3 legs are not jointly defined.

and the guard's own fresh attack at B2.6 appended "one active asymmetric finite primitive" of
the same kind. The build never re-runs that attack, and never mentions the primitive. So the
membership theorem is proved over an index category from which the arrows that produced the
original failure have been removed by construction rather than repaired by proof.

I record the fair counter-argument: it is *possible* that A_iso∪A_RP∪A_CC∪A_CR extensionally
exhausts the consumer arrows, in which case clause (vi) is redundant and nothing is lost. The
build neither claims nor shows this, and the burden is the build's — the guard installed clause
(vi) precisely because the extensional question was already answered wrongly once (Q-451).

**Two lesser narrowings, same direction.** Guard (ii) is "the sealed W3/DoR-008 finite
restriction arrows" with no rank qualifier; the build's A_RP reads "a *rank-preserving* W3/DoR-008
restriction". The guard uses the rank qualifier deliberately and only in clause (iii), which
proves the omission in (ii) is meant. Guard (v) covers common refinements built for arrows in
(i)–(iv); the build's A_CR covers only "arrows in `A_RP` union `A_CC`", dropping A_iso.

### 1.3 DEFECT — the ledger contradicts its own uniformity claim

Build §1.2 asserts every component lives on the same `Obj(I_F)`/`Mor(I_F)`. Its own rows do not:

- row 3 (`C1_core^fin`) quantifies over `A_iso union A_RP union A_CC union A_CR` — the
  **generating set**, not the closure;
- row 6 (`C3_fin`) **bifurcates by arrow class**: "for `f in A_RP`, full finite naturality; for
  `f in A_CC`, only the displayed old-image projected comparison";
- row 7 (`R2_alg^fin`) declares an object domain only, with **no arrow part**, yet J1/J3 are
  claimed on it as tuple rows;
- row 12 (`Diamond_fin`) is indexed by the **built** squares, not by all squares in `I_F`.

Row 6 is honest about the scoping and I credit it as such — but a tuple whose sixth coordinate
has two different arrow behaviours is a *scoped* functor, and FC10/FC11 must then be read as
scoped claims. The build reads them as unscoped.

## 2. D2 — the guard, condition by condition

Walked FC1–FC11 + FC13 against the V001 text. Recomputations required by the paste are in
§2.2–§2.5.

| FC | V001 requirement (abridged) | Verdict on this build |
|---|---|---|
| FC1 actuality | Q-408 maps used extensionally, not an abstract isomorphic kernel | **PASS** — components 2/9 trace to H_Q408, H_SEC, H_FLIPR; no rails substitute found (§4.2) |
| FC2 finite bottom | every active restriction reproduces the sealed DoR-008 result incl. Gate 1–4, Q-243/279/309 shadows | **PASS** — genuinely repaired; see §2.2 |
| FC3 functoriality | identity/composition on actual arrows; built diamonds commute | **PASS on the 4-coordinate package**; unproved for the 13-tuple over the closure (§1.3) |
| FC4 contravariant honesty | only proved downward/old-image restrictions; no invented upward quotient | **PASS** — H_ASM3 line 492 states no `Bot_N^resp -> Bot_M^resp` exists |
| FC5 covariance | whole tuple carried covariantly, no representative selected | **PASS** — full orbits retained; A3-c1 action verified §2.3 |
| FC6 surface support | OLD_FID, RNL, LR, excision on their **proved finite scopes** | **DEFECTIVE** — over-claimed on every arrow; see §2.4 |
| FC7 bundle discipline | U(1) lift, pullback iso, full rank, char. class, density/coframe units | **PASS** — carried by `Where_A1^fin` from H_SEC/H_FLIPR |
| FC8 analytic core | Hausdorff cores, bounded on finite domains, no global uniform bound | **PASS** — no global bound smuggled |
| FC9 finite-kernel honesty | exact Ward/contact split; faithful horn zero kernel; no record-visible cycle deleted | **PASS on injectivity** (recomputed §2.5); the no-deletion clause is stated more broadly than sourced |
| FC10 joint compatibility | finite J1–J15 hold **on one tuple** | **DEFECTIVE** — J2 A_RP half posed not proved (§2.6); J7 not supplied (§3.1) |
| FC11 equalizer coherence | six generator components agree as one finite fiber-product term, incl. contact cocycle | **DEFECTIVE** — two hypotheses discharged by one equation (§3.1) |
| FC12 | struck by V002 | **correctly absent** from the conjunction |
| FC13 target blindness | nothing chosen from a response/threshold/fixed-point/end-test/numeric consequence | **PASS** — anti-tuning ledger reruns clean; no fence blocked a structural result |

### 2.2 FC2 — a genuine repair, and the build's best moment

The guard's FC2 failure was "no one package-wide bottom square covers every active consumer on
`I_F`" (B2.2). This is repaired by **new mathematics**, not by an amendment:

- H_ASM3 line 643: `FC2 one package-wide finite bottom | SUPPLIED | tagged tuple (PKG-1)`;
- the ten-entry `Bot_N` carries exactly the four shadows FC2 names (Gate 1–4, Q-243, Q-279,
  Q-309) plus six more;
- H_R3 and H_R4 both independently grade FC2 SUPPLIED.

I recomputed the entry count (ten) and matched the tuple character-for-character against the
build. **FC2 = PASS.** This one is real, and it should survive readjudication regardless of what
happens to the rest.

### 2.3 FC5 / J4 — the A3-c1 action, recomputed by hand

From `I_M = I_N∘rho_f + v_f` and `I_L = I_M∘rho_g + v_g`, substitution gives
`rho_gf = rho_f∘rho_g` (contravariant, consistent with `r_f^Bot : Bot_M^resp -> Bot_N^resp`) and
`v_gf = v_f∘rho_g + v_g`.

Under the **simultaneous** family action `I_X -> I_X + psi_X` at every stage,
`I_M + psi_M = (I_N + psi_N)∘rho_f + v_f'` forces

```text
v_f' = v_f + psi_M - psi_N∘rho_f
```

which is the corrigendum form, not the pre-corrigendum `v_f - psi_N∘rho_f`. Checking the primed
family satisfies the same cocycle:

```text
v_f'∘rho_g + v_g'
  = (v_f + psi_M - psi_N∘rho_f)∘rho_g + (v_g + psi_L - psi_M∘rho_g)
  = v_f∘rho_g + v_g + psi_L - psi_N∘(rho_f∘rho_g)
  = v_gf + psi_L - psi_N∘rho_gf
  = v_gf'.                                                    CLOSES
```

The intermediate `psi_M` terms cancel identically. The pre-corrigendum form leaves a residual
`-psi_M∘rho_g`, reproducing exactly the failure A3-c1 records ("the displayed form provably
breaks its own cocycle on an intermediate-stage change"). **The build uses the corrected form.
J4's core algebra is CORRECT.**

Type-check of the bottom composition: for `f:N->M`, `g:M->L`,
`r_f^Bot : Bot_M -> Bot_N` and `r_g^Bot : Bot_L -> Bot_M`, so
`r_f^Bot ∘ r_g^Bot : Bot_L -> Bot_N = r_gf^Bot`. **Order and variance as written are correct.**

### 2.4 FC6 — DEFECT, over-claimed against its own certificate

Build line 257 states FC6 holds "**On every `f in Mor(I_F)`**". Its cited certificate H_EXC ends:

```text
EXCISION_CERT_PHYSICAL_FAMILY = STOPPED_AT(NONEMPTY_COVARIANT_ZERO_DEFECT_SECTION)
D_DISJOINT = CONDITIONAL_PASS / PHYSICAL_TERM_OPEN
D_CONTACT  = CONDITIONAL_PASS / PHYSICAL_TERM_OPEN
ALL_RANK   = PARTIAL / TYPE-U
EXACT_REMAINING_OBJECT =
  Gamma_cov(Cert_LOE over actual positive-source primitives) != empty,
  coherent on every actual common-refinement diamond
```

The certificate's **physical family term is open on both the disjoint and the contact diamond**,
its all-rank status is PARTIAL/TYPE-U, and its exact remaining object is a *nonemptiness*
obligation. FC6's V001 text requires these to hold "on their **proved finite scopes**" — a
correctly scoped FC6 row would be defensible. A universally quantified one is not.

The A4 no-mixing algebra the build relies on is separately fine: for
`P_N = (R^rep ⊕ I^contact)/{(c,-c) : c in C_N}` with `C_N = R_N^rep ∩ I_contact,N` an actual
intersection, the quotient identifies only the overlap class. That statement is true. It is a
statement about the **quotient carrier**, and it does not by itself discharge OLD_FID/RNL/LR,
which are conditions on the support behaviour of the analysis maps.

### 2.5 FC9 — the kernel-honesty split, recomputed

A4 defines `C_N = R_N^rep ∩ I_contact,N`, so both legs `C_N -> R^rep` and `C_N -> I_contact`
are **inclusions**. For the strict pushout, the injection `r |-> [r,0]` has kernel

```text
{ r : (r,0) in {(c,-c) : c in C_N} }  =>  c = 0  =>  r = 0,
```

and symmetrically for the contact leg. **The A4 pushout injections are injective, and injective
for the right reason** — because `C_N` is the genuine intersection. Had `C_N` been an abstract
object with non-injective legs, a cycle could have been deleted. **PASS.**

The row's second clause ("neither a visible represented bulk cycle **nor a target-only new
cycle** is deleted") is broader than injectivity delivers — injectivity of the pushout legs
speaks to represented/contact content, not to `K_f^new`. The build's own regression #1 covers
the target-only case separately, so this is a NOTE on the row's phrasing, not a failure.

### 2.6 FC10 / J2 — KILL. The rank-preserving half is posed, not proved

This is the row the whole theorem turns on, because the guard's B2.4 found J2 "**absent as
physical equality**".

**First, the good news, and it is substantial.** The circularity charge is **refuted**:

- H_PROJ states `READER_REFERENCED = no` at both line 22 and line 200;
- H_J2 K2 states the reader family "is used only to evaluate consequences on closed overlap
  instances, **not to define `Loc` or `pi_Mx`**";
- H_J2 K5 item 1 re-runs the F_PLDEC circularity check: "no definition path sets
  `pi_Mx := reader`".

**The forbidden repair did not happen.** The build's §5.2 claim that `pi_Mx` is sourced from
finite Hodge/projector stock is CONFIRMED against source. This deserves to be on the record as a
clean pass.

**Now the defect.** H_J2's section head at line 43 is "K1. **Pose** J2 under the adopted row".
Its equality check for the rank-preserving class, at line 79, reads in full:

> **Rank-preserving routes**: the full composite equality **can be reconstructed** arrowwise
> using the rank-preserving covariance already in `V003` cert (`ρ_f d_M = d_N ρ_f`,
> `ρ_f δ_M = δ_N ρ_f`, `ρ_f P_H,M = P_H,N ρ_f`) and the assembled finite factors above.

"Can be reconstructed" is a **posability verb**. No reconstruction is displayed, in H_J2 or
anywhere downstream. The build's §2.4 J2 row nonetheless carries the full composite
`reader_f = pi_Mx,F ∘ Loc_F ∘ Kernbar_F ∘ Q_F` and tags the row `PROVABLE — PASS`.

FC10 requires the finite J-rows to **hold**. A row whose strongest source status is
"reconstructible in principle" does not hold. **KILL.**

**Typing gap, compounding.** `pi_Mx` is never typed in the build. The one indicative definition
in the chain is H_J2 line 69: `π_Mx,N := π_M^resp ∘ P_H,N ∘ Loc_N` — hedged as "**style**
descent". If read as definitional, then the composite `pi_Mx,N ∘ Loc_N` appearing on the
right-hand side of the A6 square expands to `π_M^resp ∘ P_H,N ∘ Loc_N ∘ Loc_N`, applying `Loc`
twice. Either the definition is wrong or the square is malformed; the "style" hedge means the
chain never settles which. DEFECT.

## 3. D3 — the joint checks

### 3.1 KILL — J7 is discharged by J2's own equation

I set the contract equations side by side from four independent sources:

| Source | Equation |
|---|---|
| H_DIAR U3 / line 37 | `r_f^Bot ∘ pi_Mx,M ∘ Loc_M ∘ η_f = pi_Mx,N ∘ Loc_N` |
| H_A6 line 7 (ratified) | `r_f^Bot ∘ pi_Mx,M ∘ Loc_M ∘ eta_f = pi_Mx,N ∘ Loc_N` |
| H_J2 K3 | `r_f^Bot ∘ pi_Mx,M ∘ Loc_M ∘ eta_f = pi_Mx,N ∘ Loc_N` |
| Build §2.4 J7 row | `r_f^Bot∘pi_Mx,M∘Loc_M∘eta_f = pi_Mx,N∘Loc_N` |

**Character-identical, and type-correct**: both sides run `D_f^old -> Bot_N^resp`. As a
*contract match* this is exact, and the build's §2.5 claim of a match is CONFIRMED.

But that is precisely the problem. The build's J2 row (line 303) puts this equation on
`D_J2^CC`, and its J7 row (line 308) puts **the same equation on the same domain**:
"Domain `D_J7^CC := D_J2^CC`; the corrected comparison face is the same A6 map equality."

J7's contract of record is **not** that equation. H_DIA line 136 titles the slot "**J7-OPEN slot
(physical rank-one coefficient face)**" and line 141 states the obligation:

> 2. prove `chi^Mx, T^Mx` extraction on each overlap arrow and verify the [coefficient
>    identities]

with the displayed coefficient equations at lines 146–147, and line 176 confirming "J7 provides
the same family's coefficient pair `(chi^Mx,T^Mx)` with overlap [naturality]". The guard's own
B2.4 J7 row agrees: "rank-one scalar formula exists algebraically; it is not a joint
physical-reader equation while J2 is absent."

**The `chi^Mx`/`T^Mx` extraction is never built, anywhere in the chain.** And H_DIA line 167 is
explicit that the completion theorem needs both faces as *two* inputs:

> Given J2 and J7, the only missing equations are precisely the two inserted faces.

COMPLETION_THEOREM_V2 therefore has two distinct hypotheses discharged by one equation. **FC11
does not follow. KILL.**

### 3.2 DEFECT — the five-face provenance is misstated

Build line 382 states:

> the five-face input is consumed through confirmed `H_ASM3=a46beae2…` plus repaired
> `H_ASM4=9bf34e27…` and their reviews `H_R3/H_R4`. The killed
> `...JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V001.md` is not an authority for this proof.

**All four of those artifacts record FC11 as OPEN and contain no diamonds:**

```text
H_ASM3 line 652:  | FC11 equalizer diamonds | OPEN | stage 2 |
H_ASM4 line 219:  FC11 = OPEN
H_R3   line 404:  | FC11 | OPEN | simultaneous equalizer diamonds are not built here |
H_R4   line 197:  FC_LEDGER = ... FC10 PARTIAL; FC11 OPEN; ...
```

The five faces exist only in H_DIA — the artifact that, at its line 47, derives `F_fin` "on all
`I_F` generators" **from the killed `..._LANE2_V001`**, and again at line 76 for the corrected
simultaneous action. That artifact was killed twice (Q-459: "substituted look-alikes at the
rails level for the physical faces"; Q-463: "RAILS_SUBSTITUTED_FOR_MISSING_GEOMETRY = true").

Q-486 ruled the H_DIA content correct and only the pointer wrong. That ruling stands and I do
not disturb it — the corrected simultaneous action is independently in H_R3 (H1-7)–(H1-9), which
A3-c1 cites. But the build's sentence asserts a provenance its own sources contradict. **The
Q-486 drift is relabelled, not cured.**

### 3.3 FC10 jointness — the original sin, partially recurring

FC10's V001 text: "The finite versions of J1–J15 hold on **one tuple**. Passing the rows on
different tuples does not qualify."

Several §2.4 rows state their domain in terms of a **single component** rather than the package:
J1/J3 on `D_reader,N` (component 7's own domain, which declares no arrow part at all); J5/J6 on
`A_fin`; J8 on "components 5–7"; J9 on "every ordered batching arrow in `A_iso`" — a sub-class
of arrows, not `Mor(I_F)`; J11 on `Where_A1^fin(N)`.

Attaching the phrase "on this same thirteen-coordinate tuple" to a componentwise row does not
make it joint. This is a weaker form of the exact defect the guard named, and it is not fully
cured. Rows J4, J10, J12, J13, J15 **are** genuinely joint and I credit them.

## 4. D4 — the four historical failure modes, hunted by name

| Mode | Verdict |
|---|---|
| **Circularity** | **NOT FOUND.** Cleanly refuted — see §2.6. `READER_REFERENCED = no` twice in H_PROJ; the reader is explicitly barred from defining `Loc`/`pi_Mx`; F_PLDEC re-run. `C_forbidden ∩ Components(F_actual) = ∅` holds: `P_H,N` is the finite-stage projector from H_PROJ, not `Hodge_Maxwell_bar`. |
| **Look-alike substitution** | **NOT FOUND in the build.** This was the killer at Q-459/Q-463, and the build does not repeat it — components 2 and 9 trace to actual Q-408/surface/bundle stock. One residual: the A4 no-mixing lemma is a statement about the quotient carrier offered toward FC6, which is about the analysis maps (§2.4) — a category slip, not a substitution. |
| **Citation drift** | **NOT CURED.** Zero hash defects, and the build names and avoids the killed pointer in its own text — but §2.5's provenance sentence is false against sealed text (§3.2). |
| **Scope-shrink** | **FOUND.** Guard clause (vi) absent; A_RP and A_CR additionally narrowed (§1.2). |

## 5. D5 — the consequence, typed

**Correct.** The axiom's consequent is existence-only "without a selector or uniqueness" (guard
A1), and the build does not slide from existence to selection: `MEMBER_SELECTION = none`,
`COMPLETED_FAMILY_ASSERTED = false`, and §3.3 says adoption "has not occurred here, so no
completed member is asserted, selected, or bound". The instantiation of the universally
quantified `F` with `F_actual` is formally valid. C_ret is kept independent, and §5.4's Q-448
disposition (`GUARD_SILENT / C_RET_STEPS_3-4_ONLY`) matches guard A2/A3.5 exactly. I recomputed
the counterexample: `b(-1) = -1/2 + 3/2 = 1`, `b(1) = 1/2 - 3/2 = -1`, `b'(±1) = 3/2 - 3/2 = 0`,
`Fix(b|D) = ∅`. Correct.

**What remains outside, correctly stated:** the full new-cycle `Loc/pi_Mx` construction and the
full intertwiner. The build's §3.3 reading — that a later post-scope construction "becomes a
falsifier/test ... it does not block the membership theorem" — matches H_A6's falsifier clause,
which assigns such a failure to "the completion route, not this row". **Correct as typed.**

**NOTE — tag discipline is inconsistent.** The build applies "PROVABLE from YOURS A4/A5" at
components 5 and 6 and at row J12, which is right. It does not apply it where A4/A5 are equally
load-bearing: FC6 (relies on the A4 pushout), FC9 (relies on A4 injectivity), FC11 and the
J2/J7 rows (rest on A6, whose own Grounds line 15–17 derive the scoped square from **A5 harmonic
descent**, and A5 is `RATIFIED, AUTHORED`). The chain `PROVABLE(J2) <- PROVABLE(A6) <- YOURS(A5)
<- YOURS(A4)` is never surfaced. This materially overstates how much of the theorem is derived
rather than authored — which is exactly the question a readjudication will ask.

## 6. D6 — fresh attack: the status-verb audit

**My attack, not one previously run.** Rather than asking "is the mathematics wrong", I asked:
*for every row the build marks PASS, what is the strongest status verb its own cited sources
assign to that row, and does any later cited source upgrade it?* A terminal claim cannot be
stronger than the chain that carries it. I ran this across the final boards of H_EXC, H_ASM3,
H_ASM4, H_R3, H_R4, H_PROJ, H_J2, H_DIA and H_DIAR.

| Build row | Build status | Strongest verb in its own cited sources | Upgraded later? |
|---|---|---|---|
| FC6, "on every `f in Mor(I_F)`" | PASS | `CONDITIONAL_PASS / PHYSICAL_TERM_OPEN` (D_DISJOINT, D_CONTACT); `ALL_RANK = PARTIAL/TYPE-U`; family `STOPPED_AT` — H_EXC board | no |
| FC10 · J2 on `A_RP` | PROVABLE — PASS | "**Pose**" (H_J2 K1 head); "can be **reconstructed**" (H_J2 line 79) | no |
| FC10 · J7 | PROVABLE — PASS | "**J7-OPEN slot**"; contract = `chi^Mx,T^Mx` extraction (H_DIA 136–146) | no — never built |
| FC11 | PROVABLE — PASS | `FC11 = OPEN` (H_ASM3 652, H_ASM4 219, H_R3 404, H_R4 197); `COMPLETION_THEOREM = GAP` (H_DIAR 38) | partially — H_J2 K3b, but conditional on the J7 face, which is unsupplied |
| FC10 overall | PASS | `FC10 = PARTIAL` (H_ASM3 651, H_ASM4 218, H_R3 403, H_R4 165/197) | partially |
| Projector naturality, all-arrow | carried | `MATE_CERT = BLOCKED` (H_PROJ line 20) | no — re-scoped by A6, not built |

**Five rows report a stronger verb than their chain carries, and the pattern is one-directional.**
Note the honest cases the audit also surfaced, which is why I trust it: FC2 reports SUPPLIED and
its sources say SUPPLIED; J4/J12/J15 report PASS and H_R3/H_R4 confirm them. The audit
discriminates. **KILL.**

**Sub-finding — vacuity is not excluded.** `D_f^old` and the fourfold intersection `D_square^old`
are nowhere shown inhabited. No source establishes nonemptiness; H_EXC's own
`EXACT_REMAINING_OBJECT` is precisely a nonemptiness obligation
(`Gamma_cov(...) != empty`). If `D_f^old` were empty on some cycle-creating arrow, the A6 square
would hold **vacuously** there — at exactly the arrows that caused the original failure — and the
build's §4 honesty audit (`JOINT_FAILURE_FOUND = none`) could not fire. Structurally the old
image should be inhabited whenever `N` carries retained old cycles, so I record this as a NOTE
and an exhibition debt in the Q-486 finding-2 style, not as a demonstrated error.

## 7. What would repair this

Stated as construction, not as re-reading. None of it is blocked by a fence.

1. **The `chi^Mx`/`T^Mx` coefficient face** (H_DIA D2 item 2) — the single highest-value missing
   object. Without it COMPLETION_THEOREM_V2 has an undischarged hypothesis and FC11 does not follow.
2. **The displayed reconstruction of full J2 on `A_RP`** — H_J2 line 79 says it can be done from
   `ρ_f d_M = d_N ρ_f`, `ρ_f δ_M = δ_N ρ_f`, `ρ_f P_H,M = P_H,N ρ_f`. Do it arrowwise and display it.
3. **A definitive typing of `pi_Mx` and `Loc`**, resolving the double-`Loc` reading of H_J2 line 69.
4. **Clause (vi)** — either display the consumer arrows inside the four classes, or restore the
   class and re-run the guard's B2.6 asymmetric-primitive attack against the repaired chain.
5. **FC6 re-scoped** to H_EXC's actual proved scope, or the physical family term closed.
6. **Provenance sentence at build line 382 corrected** to name H_DIA, with H_DIAR's independent
   recomputation carrying the faces.
7. **Tag propagation** of the `YOURS` dependency through FC6/FC9/FC11/J2/J7.

Items 1–3 are mathematical. Items 4–7 are exhibition and bookkeeping, and are cheap.

## 8. Fence and stopping board

```text
AXIOM_V002 = PROPOSED_NOT_ADOPTED
FINITE_MEMBERSHIP_THEOREM = NOT PROVEN ON CURRENT STOCK
COMPLETED_FAMILY_ASSERTED = false
MEMBER_SELECTION = none
FIXED_POINT_EXECUTION = none
END_TEST = none
NUMERIC_EVALUATION = none
MEASURED_CONSTANT_COMPARISON = none
FENCE_BLOCKED_STRUCTURAL_RESULT = false
MACHINERY_APPEAL = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No register, plan, tracker, git, commit, push, member-binding, fixed-point, end-test, or
evaluation action was performed by this lane.

MEMBERSHIP = DEFECTIVE (+D1 scope-shrink at clause (vi); +D2 FC6 over-claim and J2/`A_RP` posed
not proved; +D3 J7 discharged by J2's equation so COMPLETION_THEOREM_V2 has an undischarged
hypothesis; +D6 five rows report a stronger status than their sources carry)
READY_FOR_AXIOM_READJUDICATION = no
