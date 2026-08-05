# STAGE 8 TASK 5 / EQ6 — THE SEED ADJUDICATION: DOES THE SOURCE THREAD THE LOOP? — DARIO V001

Date: 2026-08-05
Lane: Dario (Claude Opus 5), cross-family adjudicator of record
Task: PASTE 567 / Task 5 / EQ6
Custody: adjudication of the program's sharpest physical question to date.
Under adjudication: `STAGE8_TASK5_EQ6_TWO_LEMMAS_LANE3_V001.md` (`48616c23…`, verified; the
`_PREAUDIT_SUPERSEDED` copy was ignored entirely).

## Lead result

```text
REGISTER_HEAD = Q-493

ENTAILMENT_CONTROL = CONFIRMED
  (S9) recomputed independently; (M4) genuinely unexcluded; Ward genuinely
  period-blind; no sealed injectivity for P_H o Loc. No route to (M5) found.

ANCHOR = ABSENT
  -- and the finding is STRONGER than "unproved": the subject term of (M5) is
  UNDEFINED in sealed stock, at two independent points.

SEED_TYPE = END_TEST_STRUCTURAL
  Not DERIVABLE (no anchor). Not OBSTRUCTED (a real structural headwind exists
  but is blocked by a type shift). Not AUTHORABLE -- foreclosed on three
  independent grounds, the decisive one being that there is no defined object
  to author about.

VERB_AUDIT_SELF = CLEAN (+1 disclosed strengthening of a prior finding)

MEMBER_BOUND = false ; FIXED_POINT_EXECUTED = false ; END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = false
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

**The headline.** The Lane 3 artifact is correct, honest, and correctly stopped. But the situation
is worse than it reports, and in a way that changes the adjudication. The artifact asks whether the
pairing `q_T,RL = <Loc Kernbar Q(L_T), c_RL>` is nonzero. **In sealed stock that pairing has no
defined left argument.** `Kernbar`'s defining formula is scoped to the cycle-profile operator
component and `L_T` is adjoined as a *separate* summand; and `Loc_N^physical_for_J2` is recorded
`NOT_BUILT`. So (M5) is not an unproved statement about a known quantity — it is a statement whose
subject term does not yet exist. That is strictly upstream of both "unproved" and "false", and it
forecloses authoring outright.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-493 | verified |
| Artifact `48616c23…` | verified before reading; §§1.2–1.5 read in full |
| Pre-audit copy | present, clearly marked `_PREAUDIT_SUPERSEDED`; **ignored entirely** |
| My J7 adjudication `f76139e5…` | verified |
| Output name absent before construction | verified — no clobber |

## 1. S1 — the entailment control: CONFIRMED

### 1.1 The reduction, recomputed

[PROVABLE] I recomputed (S5)–(S9) independently. For a one-dimensional harmonic sector
`H_N_RL = span{c_RL}` with `c_RL != 0`, the orthogonal projector is
`P_H(s) = <s,c_RL>/<c_RL,c_RL> * c_RL`. Since `<c_RL,c_RL> > 0` by metric positivity and `c_RL != 0`,

```text
P_H(s) != 0   <=>   <s, c_RL> != 0.
```

So `m_T,N_RL != 0  iff  q_T,RL != 0` exactly, neither more nor less. **(S9) is correct.**

[PROVABLE] Scope note, offered as calibration rather than criticism: this equivalence was already
sealed — the diamond census states it as (MT-4). The artifact's genuine new content is the *named
actual stage* and the (M1)–(M5) entailment controls, not the equivalence.

### 1.2 The three negative facts, attacked

[PROVABLE] **(M4) is genuinely unexcluded for this vector.** `s_T != 0 => P_H s_T != 0` is false as
linear algebra: any nonzero vector in `H^perp` is a counterexample. The question is whether anything
excludes that case *for this vector*. Nothing does. I attacked the most promising exclusion route
myself — if the Hodge carrier `C_N^k` had dimension equal to the harmonic sector, `P_H` would be the
identity and (M4) would hold. It fails: the projector cert's own (1-9) gives

```text
C_N^k = im d_(k-1),N  (+)perp  H_k,N  (+)perp  im delta_(k+1),N,
```

so `H^perp` is genuinely nontrivial at the Maxwell degree and `s_T` is unconstrained within it.

[PROVABLE] **Ward is genuinely period-blind.** The sealed Ward statements are homogeneous —
`Kern^raw(H)[d alpha, b] = 0` and `Kern^raw(H)[a, d beta] = 0` — conditions annihilating exact
arguments. They are obeyed by the entire realized profile family and single out no period and no
particular harmonic direction. I found no inhomogeneous Ward identity and no source equation of the
form `d*F = J` anywhere in the Q-408 stock; had one existed it would have been the anchor, because it
would tie the source to the loop's own current. **The record carries a conservation law, not a source
law.** That is the precise reason Ward cannot help.

[PROVABLE] **No sealed injectivity for `P_H o Loc`.** Faithfulness is sealed *before* `Loc`:
`Kern_N^raw(H) = 0 iff H = 0` (2-4). Composition with `Loc` and then projection destroys it —
injectivity is not preserved under composition with a projector whose kernel is nontrivial. And no
sealed source anywhere states injectivity, rank, or an image characterization for `Loc`.

[PROVABLE] **The normalization routes are correctly rejected.** `p_loc(L_T) = 1` is a functional's
value on its declared local-symbol domain; it does not identify `Loc Kernbar Q(L_T)` with anything of
nonzero period. And `lambda(m_T) = 1` cannot serve, because `lambda` is only formed after
`m_T != 0` — the artifact's §1.5 circularity rejection is exactly right.

### 1.3 The most seductive false anchor — named, because a future reader will find it

[PROVABLE] The physical-J2 artifact contains, at (1-3):

```text
pi_Mx,N(Loc_N(Kernbar_N(Q_N(L_T,N)))) = 1.
```

Read carelessly this **is** the seed — it asserts the composite is nonzero on `L_T`. It is not an
anchor. Its own context settles it: (1-3) is introduced as "**The physical J2 equation of record**",
i.e. the equation J2 is *required to satisfy*, and the very next lines read "The four factors in
`(1-3)` must be constructed independently of `ell_N`. **Equality is a theorem only after both sides
are maps on the same carrier.**" The same artifact's board records
`Loc_N^physical_for_J2 = NOT_BUILT / TYPE-U`.

[PROVABLE] So (1-3) is a desideratum on an unbuilt composite — the operator-level twin of the
`lambda(m_T)=1` circularity the artifact already rejects. **Consuming it as an anchor would be the
F_PLDEC class.** I record it prominently because it is the single most likely future error on this
question.

**S1 verdict: the entailment control is CONFIRMED. No route to (M5) was found.**

## 2. S2 — the corpus hunt: ANCHOR ABSENT

### 2.1 The sweeps

[PROVABLE] Register sweep (done first, as directed): the settled register was swept for *flux*,
*period*, *holonomy*, *thread*, *linking*, *pairing*. **No anchor under any name**; every hit belongs
to an unrelated Stage-8 thread. Corpus sweeps then covered the Q-408 foundational stock, the
where-clauses and DoR-020-A1, the carrier metric, the Maxwell/Hodge and projector certs, the physical
J2 artifact, and the local Maxwell symbol artifact, under the additional names *threading*,
*encircles*, *winds*, *circulation*, *line integral*, *contour*, *Stokes*, *class*, *generator of
H^1*, *de Rham*, *linking*.

[PROVABLE] **Nothing states a nonzero flux, period, or pairing of the `L_T` source through the
reciprocal loop.** Three sealed sources independently type this exact pairing UNDETERMINED by name —
the diamond census at (MT-4) ("do not prove (MT-4)'s nonzero pairing for the particular `L_T`
symbol"), the physical-J2 artifact ("the existing stock has not proved that
`Loc_N Kernbar_N Q_N(L_T,N)` lies in a nonzero normalized local Maxwell summand"), and the manifests.

### 2.2 Where an anchor would have come from — the gap has a name

[PROVABLE] The corpus's one nonzero reciprocal-loop witness is real but sits on the **wrong
direction**. The physical-J2 artifact proves `Kernbar_N(Q_N H_x) != 0` for a reciprocal-loop profile
`H_x = [f(r^2) + 2r^2 f_1(r^2)] R_K,N` — built from the **`R_K`** direction, not `L_T` — and then
stops: "neither `Loc_N` … nor `pi_Mx,N` exists on (3-3)."

[PROVABLE] The relation that would transfer that witness to `L_T` is itself explicitly unproved. The
local Maxwell symbol artifact lists exactly three missing relations at (S1-5) — the first being
`Rhat_K = a_K L_T + R_perp` with `p_loc(R_perp) = 0` — and states: "**No authority proves any line of
(S1-5).**" Its own lead says the same: "normalization fixes `p_loc[L_T]=1` but no ratified relation
identifies `R_K` with `L_T` or places `R_K` in its complement."

[PROVABLE] So the anchor's absence is not an oversight in this relay. **It traces to a named,
long-standing Task-4B gap: the `R_K`–`L_T` relation.** That is where a future anchor would come from,
and naming it is more useful than reporting a bare negative.

### 2.3 The finding that changes the adjudication: the subject term is undefined

[PROVABLE] `q_T,RL` presupposes that `s_T,RL := Loc Kernbar Q(L_T)` denotes a vector. In sealed stock
it does not, at **two independent points**:

1. **`Kernbar` is not defined on the `L_T` summand.** The presentation adjoins `L_T` as a *separate*
   direct summand — `E_G := R L_T,G (+)_1 A_prof,G`, with `Q_G(a,b,C) = a L_T,G + j_R4,G(b R_K,G + C)`
   — while the Q-408 realization formula is scoped: "**On the cycle-profile operator component** it is
   the basis-free map `Kern_N^raw(H)[a,b] = H(R_K^(-1) A_N a, R_K^(-1) A_N b)` (2-2)". `L_T` is not in
   that component. The faithfulness statement (2-4) is scoped the same way and likewise does not reach
   `L_T`.
2. **`Loc` is not built.** `Loc_N^shadow = BUILT / TYPE-P` but
   `Loc_N^physical_for_J2 = NOT_BUILT / TYPE-U`; and my J7 review of record already recorded that
   `Loc_N = sigma_N^fin` has no stated domain, codomain, or linear structure, with two conflicting
   sealed readings in play.

[PROVABLE] **This is absence of definition, strictly upstream of absence of proof — and strictly
upstream of proof of absence.** It is why the anchor hunt cannot succeed as posed, and it is the
decisive fact for the typing in §3.

### 2.4 A structural headwind — recorded honestly, and it points the other way

[PART-PROVABLE] One route deserves recording because it inverts the burden. `L_T` is the transverse
Maxwell kernel; its sealed explicit form is `Pi_R,M = -hbar K (q^2 eta - q q)`, and the cellular
construction gives the same object as `M = delta d` with symbol `|xi|^2 Id - xi tensor xi`. Now, from
the projector cert's own definitions — `delta` adjoint to `d`, and `H = ker d ∩ ker delta` — for any
`v` and any harmonic `c`:

```text
<delta d v, c> = <d v, d c> = <d v, 0> = 0.
```

So the entire **range of the operator `delta d` is orthogonal to the harmonic sector**. The physics is
familiar and the record already names it: harmonic 1-forms are flat connections, carrying holonomy but
zero field strength, so an `F^2`-type Maxwell kernel is blind to them — the Aharonov–Bohm sector, which
the axiom's constraint arm guards under "no … flat-holonomy laundering". The reciprocal-loop cycle is
exactly such a flat direction.

[PART-PROVABLE] **This does not prove `q_T,RL = 0`, and I do not report it as doing so.** The
orthogonality is about *outputs of the operator* `delta d`; `s_T,RL` is the *localized symbol of that
operator treated as a vector* in `C_N^k`. The map effecting that type shift is `Loc`, which is not
built — one cannot prove a property of the image of an unbuilt map. The headwind is therefore
suggestive, not conclusive.

[PART-PROVABLE] But it matters for the decision. **If the program authors the nonzero branch, it
authors against the structural grain**, and it does so on an object it has not defined. That is the
opposite of the situation in which A4 and A5 were adopted.

**S2 verdict: ANCHOR = ABSENT.**

## 3. S3 — typing the seed

### 3.1 (a) AUTHORABLE — foreclosed, on three independent grounds

[PROVABLE] **Ground 1 — the template does not fit.** A4 and A5 were adopted as
`RATIFIED, AUTHORED` on the explicit basis "provably **not derivable** and provably **not
obstructed**". Here the second limb is unavailable: nobody has shown (M5) is not obstructed — indeed
§2.4 is a headwind *toward* obstruction. Authoring requires a genuine freedom between lawful
alternatives; (M5) is not known to be one.

[PROVABLE] **Ground 2 — there is no object to author about.** By §2.3, `q_T,RL` has no defined
subject term. A law asserting "this scalar is nonzero" about a scalar with no domain, codomain, or
construction is not a minimal row — it is a placeholder wearing the grammar of a law.

[PROVABLE] **Ground 3 — the corpus's own exhaustive alternatives list omits it.** My J7 review's §3.5
"Genuine alternatives, kept of record" lists five candidates and types the seed as
"(b) **Prove the seed theorem** … The real repair." *Authoring it* appears nowhere.

[PROVABLE] **A fourth, filing-level signal, which I checked and record because it is independent of
all the mathematics.** The four ratified DoR-020 rows split cleanly by custody idiom: the two
**derived** rows (A3 J4-R, A6 J2-scoped) carry "the sealed number remains the final test"; the two
**authored** rows (A4, A5) do not — they carry directly-falsifiable void conditions on actual record
data instead. An authored (M5) could carry no such void condition: its only falsifier is a computation
that does not yet have its inputs. It would be the program's first **unfalsifiable authored row**.

### 3.2 (c) OBSTRUCTED — not established

[PROVABLE] The only forced zero of record is the acyclic branch (`H_X = {0} => P_H = 0 => m_T = 0`),
which cannot reach `N_RL` because `H_N_RL != {0}`. The §2.4 headwind is blocked by the type shift.
The honest statement is **absence of proof in both directions**, and the artifact's own
[PART-PROVABLE] verb — "a proof failure, not a proof that `q_T,RL = 0`" — should be upheld verbatim.

[PART-PROVABLE] I note for the record that (c) is now the *more* interesting hypothesis, and that
commissioning its refutation-or-proof — "prove `q_T,RL = 0` identically once `Loc` is built compatibly
with the Hodge structure" — may be a better use of a relay than continuing to hunt a positive anchor.

### 3.3 (b) END-TEST-STRUCTURAL — the typing the law supports

[PROVABLE] **Adopted.** The seed is carried as an explicit **CONDITION**, not a declaration: the J7
support's inhabitance clause, the coefficient face, and the membership row are each stated *conditional
on* `q_T,RL != 0` at the named stage, with the condition displayed rather than discharged.

[PROVABLE] This is the A6 post-scope idiom, already ratified and already in use: A6 retains full J2 on
the new-cycle factor as "an explicitly typed POST-SCOPE CONDITION, pending an INDEPENDENT
construction". The seed is the same shape and should use the same instrument.

[PART-PROVABLE] **On the name, stated carefully so it is not over-read.** The program has a
preregistered, frozen evaluation protocol that computes the response to threading integer flux through
a closed two-cycle — `K_B = [·][Gamma_even(+1) + Gamma_even(-1) - 2 Gamma_even(0)]` over sectors
`n in {-1,0,+1}` — currently gated `flux_curvature_evaluation_authorized = false`, and governed by
"no item may be selected by comparison with alpha" and "the numerical value remains hidden from
construction and branch selection". That protocol is the eventual arbiter of *this physical coupling*,
which is the substantive reason to carry rather than declare. **But I do not assert that the escrowed
quantity is `q_T,RL`**: the protocol's object is a completed-level two-cycle flux response, `q_T,RL` is
a finite-stage record pairing, and no sealed statement identifies them. The typing name should be read
as "the nonvanishing belongs to the class the end test adjudicates", not as a claim that the end test
computes this scalar.

### 3.4 Consequences, per typing

| | under (a) AUTHORABLE | under (b) END-TEST-STRUCTURAL *(adopted)* | under (c) OBSTRUCTED |
|---|---|---|---|
| **J7 amendment** (inhabitance clause) | clause discharged by fiat; support declared inhabited | clause stands **open and displayed**: the support is stated intensionally and its inhabitance is an explicit condition, citing (S9) as the address test — exactly what my J7 §3.7 already requires | the support is **empty**; the coefficient face is vacuous on every `A_RP` component and the amendment is pointless |
| **FC11 in DoR-020-A2** | FC11 discharged on wholly-`A_RP^+` squares, conditional on an authored row | FC11 **support-scoped and conditional**; A2's text must carry the condition explicitly, not bury it in the address | FC11 unobtainable by this route; the axiom text must say the Maxwell coefficient route is closed |
| **Membership V002** | membership becomes conditional on an unfalsifiable authored row — the weakest of the three | membership stays **DEFECTIVE** (D1/D2/D3/D6 stand) with the seed added as a named condition; nothing is claimed that is not carried | membership fails on this route permanently; the whole `chi^Mx`/`T^Mx` coefficient programme is void |

[PROVABLE] Note that under **all three** typings the membership theorem remains not proven. The seed
does not rescue it: my D1, D3 and D6 are independent of it, and D2's `(F3)` `Loc`-naturality gap is
*the same missing `Loc`* that makes `q_T,RL` undefined. **The seed and the `(F3)` defect are one
object seen twice** — build `Loc` properly and both move together.

### 3.5 What would settle it, in dependency order

[PROVABLE] The order matters, and the cheapest-looking step is not available first.

1. **Define `Loc_N`** — supply the domain, codomain and linear structure my J7 review recorded
   missing, and resolve the two conflicting sealed readings. Until this exists, `q_T,RL` is not a
   scalar and *both* the anchor question and the obstruction question are premature. This also
   discharges the `(F3)` defect.
2. **Extend or scope `Kernbar` to the `L_T` summand**, or prove the (S1-5) relation
   `Rhat_K = a_K L_T + R_perp` that would let the existing `R_K`-direction witness transfer.
3. **Then compute `q_T,RL`.** Nonzero: the anchor exists, the typing dissolves, `A_RP^+` is inhabited.
   Zero: OBSTRUCTED, and note the failure is a **pole** of the coefficient extraction rather than a
   benign non-formation — `chi_K^Mx` carries `q_T,RL` in a denominator, and the licensed case lattice
   has no infinite-`chi_K` cell. That consequence should be recorded under whichever typing is adopted.

## 4. S4 — the physical reading, for the principal

[PART-PROVABLE] The record axioms prove everything *around* the coupling and nothing *of* it. At the
reciprocal-loop stage they give you a genuine loop, a genuine conserved current running in it, a
genuine field test that detects it, and a genuine guarantee that *some* local input registers on it.
What they never state is whether the Maxwell source itself registers on that loop — whether, in
ordinary language, the source threads it. That single number is what the entire coefficient
construction stands on: it is the denominator that converts the loop into a Maxwell coefficient, and if
it vanishes the coefficient does not merely become inconvenient, it becomes infinite and leaves the
licensed range of the chain. The reason the axioms are silent is structural rather than accidental.
The record carries a *conservation* law and not a *source* law, and conservation is homogeneous — it
constrains how charge moves, never how strongly the source couples to any particular loop. There is
also a headwind worth stating plainly: the loop's harmonic direction is a flat one, carrying holonomy
but no field strength, and an `F²`-type Maxwell kernel is blind to exactly such directions. Whether
that blindness reaches this pairing cannot yet be determined, because the map that would carry the
source into the loop's carrier has not been built. **Adopting a seed would mean declaring, as law,
that the source does thread the loop — asserting the answer to the program's central non-vanishing
question in advance of the computation designed to decide it, and doing so about a quantity the corpus
has not yet defined. Carrying a condition means saying instead: everything downstream is true *if* the
source threads the loop, and here is exactly the number that decides it.** The second keeps the
program's central physical claim falsifiable. The first would spend its falsifiability to buy a
theorem.

## 5. S5 — verb audit on my own board

| My board line | Strongest verb my sources carry | Honest? |
|---|---|---|
| `ENTAILMENT_CONTROL = CONFIRMED` | (S9) recomputed by me; (1-9) for `H^perp` nontrivial; the homogeneous Ward statements; (2-4)'s scoping | **CLEAN** |
| `ANCHOR = ABSENT` | register sweep + corpus sweeps; three sealed sources typing the pairing UNDETERMINED by name; (S1-5) "No authority proves any line" | **CLEAN** |
| subject term undefined | (2-2) scoped "on the cycle-profile operator component"; (LM1-9) adjoining `L_T` separately; `Loc_N^physical_for_J2 = NOT_BUILT` | **CLEAN** — stated as absence of definition, not as proof of absence |
| §2.4 headwind | `Pi_R,M = -hbar K(q^2 eta - q q)`; `<delta d v, c> = <dv, dc> = 0`; (1-9) | **CLEAN** — tagged PART-PROVABLE, with the type shift that blocks it stated in the same breath rather than in a footnote |
| `SEED_TYPE = END_TEST_STRUCTURAL` | A4/A5 template; the A3/A6 vs A4/A5 filing split; my J7 §3.5 alternatives list; the frozen flux protocol | **CLEAN** — and I explicitly decline to assert that the escrowed quantity *is* `q_T,RL` |
| (c) not established | only forced zero is the acyclic branch, which cannot reach `N_RL` | **CLEAN** |

[PROVABLE] **One disclosed strengthening of my own prior work.** My J7 review recorded the `(F3)`
`Loc`-naturality gap as a defect of the displayed J2 chain. This adjudication shows it is larger than
I characterised: the same unbuilt `Loc` is what leaves the seed's subject term undefined. I recorded
two symptoms as separate items; they are one missing object. Stated here rather than left for a later
lane to notice.

```text
VERB_AUDIT_SELF = CLEAN (+1 disclosed strengthening)
```

## 6. Fence and stopping board

```text
SEED_THEOREM = NOT ESTABLISHED (failed by absence of the anchor)
SUBJECT_TERM_OF_(M5) = UNDEFINED IN SEALED STOCK (Kernbar scoping + Loc NOT_BUILT)
OBSTRUCTION = NOT ESTABLISHED (headwind recorded, blocked by a type shift)
A_RP_PLUS = EMPTY_OF_RECORD (no established inhabitant; not proved empty)
SEED_CARRIED_AS = CONDITION (A6 post-scope idiom)
LAW_ADOPTED = none
MEMBERSHIP_THEOREM = still DEFECTIVE; D1/D2/D3/D6 stand and are independent of the seed
MACHINERY_APPEAL = false
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

No register, plan, tracker, git, commit, push, member-binding, fixed-point, end-test, or evaluation
action was performed by this lane. No law was adopted, and no seed was declared.

ENTAILMENT_CONTROL = CONFIRMED (+no route to (M5) found; +(M4) unexcluded because `H^perp` is
nontrivial at the Maxwell degree by the projector cert's own (1-9); +Ward is homogeneous — the record
carries a conservation law, not a source law, which is the precise reason it cannot anchor a period;
+the seductive false anchor (1-3) is a requirement on an unbuilt composite, not a theorem)
ANCHOR = ABSENT (+the gap has a name: the unproved (S1-5) `R_K`–`L_T` relation is where an anchor
would come from, since the corpus's one nonzero reciprocal-loop witness sits on the `R_K` direction;
+and the finding is stronger than "unproved" — the subject term of (M5) is UNDEFINED, because
`Kernbar`'s formula is scoped to the cycle-profile operator component while `L_T` is a separate
summand, and `Loc_N^physical_for_J2 = NOT_BUILT`)
SEED_TYPE = END_TEST_STRUCTURAL (+AUTHORABLE foreclosed on three independent grounds — the A4/A5
template's non-obstruction limb is unavailable, there is no defined object to author about, and the
review of record's own exhaustive alternatives list says "prove it" not "author it"; +a filing-level
signal agrees: derived rows A3/A6 carry the sealed-number falsifier, authored rows A4/A5 carry
directly-falsifiable void conditions on actual data, and an authored (M5) could carry neither, making
it the program's first unfalsifiable authored row; +OBSTRUCTED not established but now the more
interesting hypothesis, given the flat-holonomy headwind; +the seed and the `(F3)` defect are one
missing object — `Loc` — seen twice)
VERB_AUDIT_SELF = CLEAN (+1 disclosed strengthening of my own prior finding)
