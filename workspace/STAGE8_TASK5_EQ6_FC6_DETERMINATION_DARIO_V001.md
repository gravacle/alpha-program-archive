# STAGE 8 TASK 5 / EQ6 — THE FC6 DETERMINATION: THE OPEN PHYSICAL FAMILY TERM — DARIO V001

Date: 2026-08-05
Lane: Dario (Claude Opus 5), cross-family reviewer
Task: PASTE 562 / Task 5 / EQ6
Custody: forward analysis on my own D2 finding (Q-488). Determination, not construction.
Basis: my review of record `STAGE8_TASK5_EQ6_MEMBERSHIP_REVIEW_DARIO_V001.md` (`9caef0f7…`, verified)

## Lead result

```text
REGISTER_HEAD = Q-488

OPEN_TERM = (H3-2) = Gamma_cov(Cert_LOE over actual positive-source
            primitives) != empty, coherent on every actual
            common-refinement diamond

TERM_TIGHTENED = yes | H_EXC did not consume H_SEC's K1 theorem;
  OLD_FID (LOE1) is PROVED on the same-carrier horn the actual diamonds
  inhabit, so (H2-4)'s alpha=alpha_0 / delta=delta_0 conjuncts are
  DISCHARGED and the residue is strictly smaller than H_EXC states

RESIDUE_AFTER_TIGHTENING =
  zeta = 0 on exclusive blocks (LOE2/LOE3)   -- AUTHORABLE
  + Def_supp = 0 / LR (LOE4)                  -- OPEN / TYPE-U, independent
  + W4 commutes                               -- SUPPLIED on both diamonds

FC6_CLOSURE = AUTHORABLE (binding sub-term)
  both limbs already sealed and CONFIRMED in H_SEC section 2.2 at Q-449:
    "GENERAL_PRIMITIVE_ZERO_DEFECT_NONEMPTINESS is not derivable;
     GENERAL_PRIMITIVE_ZERO_DEFECT_NONEMPTINESS is not structurally impossible."
  -- verbatim the Q-470/A5 typing pattern.
  CAVEAT OF RECORD: authoring the zeta law alone does NOT close (H3-2);
  LOE4/LR is a separate construction burden and must not be swept in.

GUARD_ROW = scope_qualified
DOWNSTREAM_CONSEQUENCE = none | the sector-mixer exclusion survives on FC6's
  SECOND, UNQUALIFIED conjunct; A4/A5 void conditions bite on VIOLATION, not
  on UNPROVEN; no other consumer needs the open term

VERB_AUDIT_SELF = CLEAN (+1 disclosed correction to my own prior artifact)

MEMBER_BOUND = false ; FIXED_POINT_EXECUTED = false ; END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = false
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

## 0. Preflight

| Check | Result | Tag |
|---|---|---|
| Register head Q-488 | verified; it is my own verdict row | PROVABLE |
| My review of record `9caef0f7…` | verified | PROVABLE |
| H_EXC `STAGE8_TASK5_EQ6_LOCAL_ORTHOGONAL_EXCISION_CERT_LANE2_V001.md` `d61a550a…` | verified | PROVABLE |
| Guard `a681c784…` | verified | PROVABLE |
| Output name absent before construction | verified — no clobber | PROVABLE |

Additionally hash-verified and read: axiom V001 `66c71bb6…`; carrier metric V005
`2a379098…`; H_SEC `a78c2450…`; Q-441 all-rank members `dec99497…`; Q-442 typing
`6cd40961…`; where-clauses V005 `19b20603…`; witness-hunt pass 2 `c0cc9511…`.

## 1. E1 — the open term, named exactly

### 1.1 Its statement

[PROVABLE] From H_EXC (H3-2), lines 694–697, the exact remaining object is

```text
Gamma_cov(Cert_LOE over actual positive-source primitives) != empty,
with common-refinement coherence.
```

It is an **inhabitance** statement, not another certificate definition. H_EXC line 691
says so in terms: "The exact remaining object is not another certificate definition."

### 1.2 Its mathematical content

[PROVABLE] Unpacked via H_EXC section 1.4 (H1-18), it demands, for **every** actual
positive-source primitive `r:G->G'`, the simultaneous vanishing of four finite
symbolic defect operators plus the bundle and coherence rows:

| Row | Operator | Condition |
|---|---|---|
| LOE1 | `Def_fid(r) := S_r^* R_K,G' S_r - R_K,G` | OLD_FID |
| LOE2 | `Def_orth(r;O,W) := E^geom_{r;O,W} - E^orth_{r;O,W}` | local orthogonal excision |
| LOE3 | `Def_leak(r;O,W) := i_W^* R_K,G' S_r Phi_G i_O` | RNL on the transported analysis image |
| LOE4 | `Def_supp(r;O) := q_{G',F_r(O)} P_r i_O`, i.e. `P_r(Tbar_G(O)) subset Tbar_G'(F_r(O))` | LR |
| LOE5 | the W1/W4 bundle equations (H1-22) | bundle discipline |
| LOE6 | covariance, reality, units, restriction, composition, diamond coherence | — |

[PROVABLE] On the two minimal actual diamonds, with the fixed target Gram form
`[[alpha,zeta],[conj(zeta),delta]]`, H_EXC (H2-4) reduces the whole question to
`alpha=alpha_0`, `delta=delta_0`, `zeta=0` on every exclusive block, all `Def_supp`
vanishing, and W4 commuting. The excision equality holds on the local pair exactly when
`zeta=0`, because H_EXC section 1.2 computes `E^orth_{U;O,W}(c_V)=(conj(zeta)/alpha)c_U`
against `E^geom_{U;O,W}(c_V)=0`.

### 1.3 Which sector pairs and rank classes it governs

[PROVABLE] **Rank classes governed:** positive-source, cycle-rank-**increasing**
primitives only — source cycle rank >= 1, target strictly greater. Call this class
`A_CC^+`.

[PROVABLE] **Rank classes NOT governed, and why:**

- *rank-preserving subdivision* — H_EXC (H3-1): `S=id`, `N_r(W)=0`, so
  `Def_fid=Def_orth=Def_leak=Def_supp=0` and `P=id` is admitted. Passes identically.
- *zero-source first-cycle members* (`A_CC^0`, Q-439/Q-440) — `K_G={0}`, so
  `A_r(O)=0` and H_EXC section 1.2's zero-map case applies; witness-hunt `c0cc9511…`
  line 20 records "OLD_FID + RNL + LR = exact/**vacuous** on `K_G0={0}`". **This pass is
  vacuous by empty source domain, not by metric behaviour**, and any scoped row must say so.
- *unrelated pre-existing cycle pairs* — H_EXC section 3.3 and 5.3: the certificate
  "imposes no condition on off-diagonal pairings between unrelated pre-existing cycles."
  This is what keeps the Q-432 `P=id` witness admissible.

[PROVABLE] **Sector pairs governed:** RNL-relevant local pairs `(O,W)`, `O` an old local
region and `W` a new-cycle local region, with

- disjoint case: the ordinary antecedent `F_r(O) intersect W = empty`;
- contact case: the exclusive family (H1-14), `O subset old_support\C_r`,
  `W subset new_support\C_r`, `F_r(O) intersect W = empty` — i.e. the recorded contact
  locus `C_r` is **excluded**. Contact-containing pairs may falsify the antecedent but
  "do not remove the exclusive family."

### 1.4 Why the certificate stopped at CONDITIONAL_PASS

[PROVABLE] Because H_EXC separated two things the earlier lanes had run together, and
then refused to launder one into the other:

1. the certificate **class** — a real proof object with data, zero-defect equations, a
   decision procedure on every finite candidate, covariance, composition, and a
   common-refinement law: `EXCISION_CERT_CLASS = BUILT / TYPE-P`;
2. physical **inhabitance** — whether the actual retained DoR-019/Q-408 family supplies a
   member with those zeros: `EXCISION_CERT_INHABITANCE_ASSERTED = false`.

[PROVABLE] The direct-sum model (H1-29) inhabits (1) but explicitly not (2):
`DIRECT_SUM_MODEL_IS_PHYSICAL_INHABITANT = false` (line 42); "It does not prove | some
actual retained DoR-019/Q-408 surface member realizes (H1-29)" (lines 540–545); and the
hostile row "direct-sum laundering | `(H1-29)` is labeled model term, never physical
inhabitant | **REJECTED**" (line 789).

[PROVABLE] H_EXC also fixes what the stop is *not*: `LAW_REVISION_NEEDED = false`,
`NEW_CLAUSE_NEEDED = false`, and section 5.4 — "It is also not a new-physics clause
request: the where-laws already say which members are admissible. It is the witness
burden under those laws."

### 1.5 A tightening H_EXC did not make

[PROVABLE] H_EXC's (H2-4) still carries `alpha=alpha_0` and `delta=delta_0` as open
conjuncts. **They are not open on the actual diamonds.** H_SEC section 1.1 (`a78c2450…`,
built Q-446, hostile-checked and CONFIRMED Q-449) proves:

```text
J_G'(S_r c) = J_G(c)                       [W1 same-carrier attachment]
=> I_K,G'(S_r c) = I_K,G(c)                                    (K1-1)
=> g_K,G'(S_r c, S_r d) = g_A4(I_K,G c, I_K,G d) = g_K,G(c,d)  (K1-2)
=> S_r^* R_K,G' S_r = R_K,G,  i.e. Def_fid(r) = 0.             (K1-3)

OLD_FID_SAME_CARRIER_W1 = PROVED / TYPE-P
OLD_FID_GENERAL_EMBEDDED_HORN = OPEN / TYPE-U
```

[PROVABLE] I recomputed this and it is correct, and correct for an instructive reason:
**no isometry premise is used at all**. Because the attachment is same-carrier, the old
edges' realized paths are untouched and `S_r c` carries the same coefficients on them, so
`u_{S_r c}` and `u_c` are *literally the same functional on the same field space*. The two
arguments of `g_A4` are the same vectors. That is why the derivation evades the W3 scope
limit, and H_SEC line 154 says so: "This derivation does not use W3."

[PROVABLE] The scope limit is real and correctly stated: on a general **embedded** horn
(`f_R : M_G -> M_G'` with `M_G != M_G'`) one would need `g_A4`-invariance under a proper
embedding, which the ratified automorphism-isometry row does not supply. The actual
diamonds are same-carrier (Q-441: one retained surface `calB`, corridors `U,V subset calB`).

[PROVABLE] Note also what does *not* work, since it is the natural first attempt: the
metric's isometry row (W4-3) `g_K,M(j_K c,j_K d)=g_K,N(c,d)` sits under section 4.1
"Rank-preserving W3 isometry" and its `j_K` is the W3 inclusion of (W4-2). Lines 374–376
close the door — "W3 does not prove automorphism isometry, generic batching isometry, or a
cycle-creating physical upward quotient map" — reinforced by the standing falsifier that
voids the package if it "claims batching/cycle-creation isometry beyond W3". **(W4-3) does
not reach `S_r`.** Q-440 concurs: "DoR-019 supplies no generic batching isometry."

[PROVABLE] **Consequence:** the residue tightens to `zeta = 0` on exclusive blocks, plus
`Def_supp = 0` (LR), plus W4 — the latter already supplied, since both actual diamonds are
recorded "W1/W4 COMMUTES".

## 2. E2 — the determination

### 2.1 Verdict

[PROVABLE] **AUTHORABLE**, for the binding sub-term (`zeta = 0`, i.e. LOE2/LOE3). Both
limbs are not merely inferable — they are stated verbatim in a CONFIRMED artifact. H_SEC
section 2.2 closes:

```text
GENERAL_PRIMITIVE_ZERO_DEFECT_NONEMPTINESS is not derivable;
GENERAL_PRIMITIVE_ZERO_DEFECT_NONEMPTINESS is not structurally impossible.
```

That is exactly the Q-470 typing formula that produced the authored law A5.

### 2.2 Limb (a) — NOT DERIVABLE, with the countermodel displayed

[PROVABLE] H_SEC (K2-1) exhibits the asymmetric-primitive countermodel: a same-carrier
rank-one-to-rank-two primitive whose new path geometry is decorated asymmetrically, so its
actual stabilizer fixes both cycle directions instead of reversing the new one — "Distinct
endpoint incidence, support labels, or bundle-field data can make the stabilizer trivial
while all W1/W4 laws continue to hold." On it,

```text
R_K,G' = [[1,epsilon],[conj(epsilon),1]],  0<|epsilon|<1     (K2-1)
Def_leak = theta epsilon != 0.                               (K2-2)
```

[PROVABLE] I verified admissibility myself: leading minor `1>0` and
`det = 1-|epsilon|^2 > 0`, so positive definite; Hermitian; unit-correct; and vacuously
stabilizer-invariant because the stabilizer is trivial. H_SEC: "No current ratified clause
excludes `(K2-1)` on an asymmetric cycle-creating primitive."

[PROVABLE] The structural reason nothing excludes it: the metric is
`g_K,G(c,d) = g_A4(u_c,u_d)` (W1-1) with `u_c` the **period functional**
`a |-> sum_e c_e integral_{gamma_e} a` (W1-3). It pairs two loops through their
holonomies, and `g_A4` itself is unforced — the field-signature records
`A4_NORM_FORCED_BY_GATE4 = false / TYPE-U`. No ratified entry supplies a locality theorem
for `g_A4` on disjoint physical supports. Q-441 states the conclusion directly: "Q-430 and
Q-440 show that a positive off-diagonal Riesz class is **live** under the ratified metric
law; **DoR-019 does not force `zeta=0`**."

[PART-PROVABLE] Worth recording because it forecloses the obvious repair: `g_A4` **cannot**
be made strictly support-local. A bilinear form annihilating every disjointly-supported
pair has a kernel supported on the diagonal, and such a kernel does not give a finite
positive `alpha_0 = g_A4(u_c,u_c)` on a one-dimensional line current in a background of
dimension >= 2. So `g_A4` is necessarily non-local, and disjoint support of the *current*
gives no information about the pairing of the *period functionals*. Tagged PART-PROVABLE:
the finiteness and positivity are sealed (W1-2, W1-7, F1-9), the kernel-support step is my
argument, not a ratified theorem.

### 2.3 Limb (b) — NOT OBSTRUCTED, by an actual family (not by the model)

[PROVABLE] **Correction of record, and it matters:** the direct-sum model H1-29 cannot
serve as the non-obstruction witness — H_EXC disqualifies it at lines 42, 540–545 and 789.
Any determination resting on it would be direct-sum laundering.

[PROVABLE] The proper witness is the **flip family**, an actual physical construction.
H_SEC (K1-4) defines a primitive to be *flippable* when its actual surface realization has
a stabilizer `tau_j` with

```text
tau_j S_r c = S_r c   for every old cycle c,
tau_j n_j = -n_j      for the new cycle current,
tau_j preserves background, bundle, fields, supports, and A4 rigging.
```

and exhibits a nonempty family: a symmetric convex normal tube, two future-directed paths
with the same endpoints, an involutive surface symmetry exchanging them, their difference a
nonzero conserved current; finitely many disjoint tubes give commuting involutions
`T_m=(Z_2)^m`.

[PROVABLE] The cross block then vanishes by parity. DoR-019's A4 automorphism-isometry
certificate (metric V005 section 6.2: "Admitted exchanges/relabelings must preserve
`g_A4`; … stabilizers must preserve the same form") applies to each actual `tau_j`:

```text
g_K,G'(S_r v, n_j) = g_K,G'(tau_j S_r v, tau_j n_j)
                   = g_K,G'(S_r v, -n_j)
                   = -g_K,G'(S_r v, n_j)          (K1-6)
=> g_K,G'(S_r v, n_j) = 0.                        (K1-7)
```

[PROVABLE] I recomputed this. It is valid over R and over C (with the Hermitian
convention `conj(-1)=-1` the same conclusion follows from either slot); the only
arithmetic hypothesis is characteristic != 2. `tau_j` is a linear realization
automorphism, not antilinear, so no conjugation subtlety enters. It is the program's
standard odd/even move — the same one that gives `Def_j = tau_j Def_j = -Def_j => Def_j=0`
in the guard's flip diamond. **The zero is forced by a symmetry of the retained surface
acting on the fixed metric — not chosen, not a basis convention, not a repair of `S_r`.**

[PROVABLE] And the flip family is a *complete* zero-defect section, H_SEC (K1-13):

```text
Def_fid=0  by (K1-3),   Def_orth=0 by (K1-7),
Def_leak=0 by (K1-7),   Def_supp=0 by (K1-12),
```

with W1/W4 inherited from the same-carrier construction. Q-446 records this as "the
program's first inhabited equalizer"; Q-449 confirms it by hostile check.

[PART-PROVABLE] One realizability step the sources assert rather than display: (K1-4)
requires `tau_j` to fix **every** old cycle while reversing the new one. On a connected
analytic carrier an isometry that is the identity on an open set is the identity, so the
flip family is not "attach a symmetric tube anywhere" — it requires the old configuration
to lie in the fixed locus of a global involution (e.g. a reflection through a hypersurface,
with the two new paths exchanged by it). H_SEC's symmetric-tube construction satisfies this,
but the fixed-locus condition should be displayed in any artifact that consumes (K1-4).

### 2.4 The residue is exactly the asymmetric primitive — and it is one object with my D1

[PROVABLE] Putting §2.2 and §2.3 together: `zeta=0` is **derived** where a stabilizer
exists and **unforced** where it does not. The entire open term therefore lives on the
**asymmetric positive-source primitive**.

[PROVABLE] That is the *same object* as the guard's own anti-shrink fresh attack. Guard
B2.6: "append one active **asymmetric** finite primitive to the flip scope. Its actual
Q-408 data and finite bottom exist, but its R1 naturality and six-component overlap maps do
not." And H_SEC's standing regression row reads "Q-430 mixer | rejected on flip terms;
**retained as the asymmetric countermodel** | PASS."

[PART-PROVABLE] So my two membership findings converge: D1 (the guard's anti-shrink clause
(vi) dropped from `Mor(I_F)`) and D2 (FC6's open term) are one gap seen from two
directions. Restoring clause (vi) readmits consumer-indexed arrows, among them asymmetric
positive-source attachments; FC6 then requires the open term precisely there. Conversely,
the build's four-class `I_F` is part of why FC6 looked unconditional.

### 2.5 The full-gate candidate — FOR THE PRINCIPAL, NOT ADOPTED HERE

[YOURS] Offered as a full-gate candidate only. No lane adopts it; this artifact does not.

**Candidate law — EXCLUSIVE-REGION ORTHOGONALITY FOR POSITIVE-SOURCE ATTACHMENTS.**

```text
For every admitted actual positive-source cycle-creating W1/W4 primitive
r:G->G' and every RNL-relevant exclusive local pair (O,W),

  g_K,G'(S_r Phi_G(a), n) = 0   for a in Tbar_G(O), n in N_r(W),

equivalently Def_leak(r;O,W)=0 and Def_orth(r;O,W)=0.
The family is covariant under admitted relabeling/reality/orientation; no
member, basis, complement, attachment, or scale is selected.
```

**Genuine alternatives, kept of record.**

| Candidate | Content | Why it is not preferred |
|---|---|---|
| (a) Stabilizer-restricted admission | restrict W1 to flippable attachments; then everything is DERIVED via (K1-13) | Shrinks the admitted family — the exact move guard clause (vi) and Q-451 bar. Also asserts a physical claim (asymmetric attachments are inadmissible) needing its own warrant. |
| **(b) The candidate above** | one bilinear vanishing on already-typed exclusive pairs | **minimal** — see below |
| (c) A locality law on `g_A4` itself | constrain the A4 kernel's support | Stronger than anything requires, and collides with the finiteness of `alpha_0` (§2.2): a diagonal-supported kernel diverges on a line current. |
| (d) Reject / leave open | no row; `[EQ6]` stays conditional on positive-source arrows | Lawful. FC6 stays permanently scope-qualified; the all-rank cascade (H4-2) stays PARTIAL. |

**Minimality.** (b) adds one vanishing condition on pairs the ratified typing already
defines, introduces **zero new coefficients**, selects no member, and **reduces to a
theorem** — (K1-7) — on the flip sub-family. It is therefore a conservative extension of
already-proved content, which is the same minimality standard A4 and A5 were adopted under.

**Void conditions (all falsifiable, of record).**

```text
1  an ACTUAL positive-source primitive exhibiting Def_leak != 0 or Def_orth != 0
   on an exclusive pair -- DIRECTLY FALSIFIABLE, and (K2-1) is the shape to hunt;
2  any use of the row to select a member, attachment, metric, or coefficient
   -- "witness-by-certificate tuning", already barred at Q-441;
3  failure of OLD_FID on the same-carrier horn (would contradict (K1-3));
4  ANY READING THAT TREATS THE ROW AS SUPPLYING LR -- it does not (see 2.6);
5  any use on rank-preserving arrows to constrain unrelated pre-existing sector
   pairs -- would reintroduce the Q-432 global-orthogonality overreach;
6  failure of common-refinement coherence for the admitted family.
```

### 2.6 What authoring would NOT close — stated so it cannot be swept in

[PROVABLE] **LOE4 / LR remains a separate, open burden on asymmetric primitives.** H_EXC
section 1.3 is explicit: "`Def_orth=0` does not by itself imply `(H1-17)`; the Q-408
analysis map can remain nonlocal even for a diagonal Gram matrix." Q-441 repeats it: "For
`zeta=0`, LR still requires the independent support-naturality fact." H_EXC's hostile row
"RNL-implies-LR shortcut | `Def_supp` remains an independent zero operator | **REJECTED**"
forecloses the collapse.

[PROVABLE] Therefore: **(H3-2) as a whole is not closed by adopting the candidate law.**
Its typing is a split — `zeta` AUTHORABLE, LR OPEN/TYPE-U with a named buildable object
(support-naturality of the Q-408 canonical test transport `P_r` on asymmetric
positive-source primitives). On the flip family LR is already proved, by (K1-12).

## 3. E3 — the guard consequence either way

### 3.1 If the term closes

[PROVABLE] The unconditional row becomes assertible:

> **FC6 surface support.** For every `f in Mor(I_F)`, OLD_FID, RNL, LR and local
> orthogonal excision hold, and disjoint new-cycle sectors are not mixed. — PROVABLE (from
> YOURS, if the exclusive-region row is adopted) — PASS.

### 3.2 If it stays open — the row the guard already licenses

[PROVABLE] FC6's own wording is scope-qualified, and the guard's own exhibition used it
that way. The guard graded FC6 **"PASS ON PROVED SCOPES"** (line 303) and then concluded
`FiniteCoherent_020^V002(F_actual) = false` "**by FC2 and FC3 and FC10 and FC11**" (line
316) — **FC6 is not among the failures**. The lane that authored the guard therefore
treated a scope-qualified FC6 as discharging the conjunct.

[PROVABLE] Paste-ready row:

> **FC6 surface support.** On `A_iso` and `A_RP`: OLD_FID, RNL, LR and local orthogonal
> excision hold identically (`S=id`, `N_r(W)=0`, `P=id` admitted) — H_EXC (H3-1). On the
> zero-source cycle-creating class `A_CC^0`: they hold **vacuously**, because `K_N={0}`
> gives `A_r(O)=0` and an empty test source domain — witness-hunt `c0cc9511…`. On the
> flippable subclass of `A_CC^+`: all four defects vanish by (K1-13), OLD_FID by (K1-3) and
> the rest by the stabilizer parity (K1-7)/(K1-12). On the remaining **asymmetric**
> positive-source subclass of `A_CC^+`: OLD_FID holds by (K1-3) on the same-carrier horn;
> local orthogonal excision, RNL and LR are `CONDITIONAL_PASS / PHYSICAL_TERM_OPEN`
> (H_EXC), and the certificate class with its decision procedure is BUILT on every finite
> candidate. Disjoint new-cycle sectors are not mixed — unqualified, and independently
> settled at Q-434. — PART-PROVABLE — PASS ON PROVED SCOPES; residue explicitly typed.

[PART-PROVABLE] **Honest caveat.** Whether FC6's *arrow* quantifier may be narrowed at all
is contestable: FC7 says "on every finite arrow" explicitly while FC6 is silent, and the
guard's own B1.2 requires "proved arrow scopes retained as part of the type" while the
axiom's section 4.1 rejects scope-selection. The guard's own grading is the strongest
evidence for the permissive reading, and I rely on it — but a one-line ruling from the
axiom's author arm would settle it and is cheap.

### 3.3 Downstream consumers — walked

[PROVABLE]

| # | Consumer | Needs the open term? | Consequence if it stays open |
|---|---|---|---|
| 1 | Membership FC6 row (build line 257, "On every `f in Mor(I_F)`") | **yes, as written** | Row unbacked as phrased; replace with §3.2. Not fatal — see §3.4. |
| 2 | **Sector-mixer exclusion** (axiom section 2.2; void condition 6; battery A5/A11; membership regression #7) | **no** | FC6's text has a **second, unqualified conjunct**: "…hold on their proved finite scopes; **disjoint new-cycle sectors are not mixed**." The mixer is defined by `1_(S2)P_mix1_(S1) != 0` and is caught by that clause regardless of the first clause's scoping. Independently: Q-434 settled the mixer rejection two relays before the axiom existed, and Q-432 types RNL as CONSTRUCTIBLE. Also the certificate is failure-capable — `FAIL(named defect, witness)` — and its decision procedure is BUILT on every finite candidate, so it returns FAIL on the mixer even where inhabitance is open. **The exclusion job survives.** |
| 3 | DoR-020-A4 (void 3: failure of OLD_FID/RNL/LR/…) | **no** | Void conditions bite on **violation**, not on **unproven**. Nothing exhibits a violation on actual data. A4 not at risk. |
| 4 | DoR-020-A5 (void 4: same list) | **no** | Same reasoning. A5 not at risk. |
| 5 | DoR-020-A6 (scoped J2) | **no** | A6's grounds are A5 harmonic descent + the J15 mate + old-image discipline; none consumes (H3-2). |
| 6 | FC11 / the built diamonds | **no new exposure** | H_EXC section 1.8 proves diamond coherence conditionally on the four legs carrying terms; the cycle-creating legs there already carry exactly the conditional status recorded. FC11's independent defects are the ones in my D3, not this. |
| 7 | Twelve-step chain Steps 2–7 | **no** | Step 2 consumes finite/rail regressions; Steps 3–4 are `C_ret`, independent by ruling. |
| 8 | The all-rank cascade (H4-2) | **yes** | `B_Q408` stays PARTIAL, and `B_R1`/`C1`/faithfulness/`C2` receive no new admitted physical arrow. This is the real cost, and it is upstream of `[EQ6]`, not downstream of membership. |

[PROVABLE] **Answer to E3's question: the scope-qualified reading weakens nothing
downstream of membership.** The one genuine cost (row 8) is the all-rank cascade, which was
already PARTIAL/TYPE-U before this determination and is not a membership consumer.

### 3.4 Bearing on my own prior verdict — correction

[PROVABLE] In my review of record I listed the FC6 over-claim inside D2 among four
KILL-grade items. The over-claim is real and stands: the build asserts FC6 "on every
`f in Mor(I_F)`" while its certificate is `CONDITIONAL_PASS / PHYSICAL_TERM_OPEN`. But on
this determination its **consequence** was overstated: the correctly-scoped row of §3.2
discharges the guard conjunct, so the FC6 half of D2 is a **rewording defect, not a
membership blocker**. The J2 half of D2 (full J2 on `A_RP` posed, not proved) is unaffected
and remains fatal, as do D1, D3 and D6. `MEMBERSHIP = DEFECTIVE` is unchanged; one of its
supporting items is downgraded.

## 4. E4 — the physical reading, plainly

[PART-PROVABLE] If this term stays open, what the record has not yet said is that a newly
created cycle is metrically independent of the cycles already present. Where the surface
carries a symmetry that flips the new loop while holding the old ones fixed, independence
is not assumed but forced: the cross term equals its own negative, so it vanishes. That is
a theorem, and it is why the symmetric case is settled. The asymmetric case is different in
kind. The carrier form is not a sum over edges; it pairs two loops through their period
functionals — their holonomies — and holonomy is an intrinsically global quantity, so two
loops occupying disjoint corridors can still be correlated. Nothing in the ratified metric
law forbids that correlation, and nothing can make the form strictly local without making a
single loop's own norm diverge. So the open question is physical rather than clerical: does
the record's geometry make disjoint cycles genuinely independent carriers of flux, or only
when a symmetry compels it? If independence holds only under symmetry, then sector
independence is a symmetry-derived feature of the record rather than a structural one, and a
general emergent-geometry claim would have to either restrict itself to symmetric
attachments or adopt independence as law — which is precisely the choice §2.5 puts to the
principal.

## 5. E5 — verb audit on my own final board

[PROVABLE] My own D6 instrument, turned on this artifact. For each board line: the
strongest verb its sources carry, and whether I report a stronger one.

| My board line | Strongest verb in my sources | Reported honestly? |
|---|---|---|
| `OPEN_TERM = named` | H_EXC (H3-2) verbatim | **CLEAN** |
| `TERM_TIGHTENED = yes` | H_SEC `OLD_FID_SAME_CARRIER_W1 = PROVED / TYPE-P`, confirmed Q-449 | **CLEAN** |
| `FC6_CLOSURE = AUTHORABLE` | H_SEC section 2.2 states both limbs verbatim; confirmed Q-449 | **CLEAN** — and I attach the LR qualifier rather than letting "AUTHORABLE" imply (H3-2) closes |
| `GUARD_ROW = scope_qualified` | guard line 303 grading; line 316 omission; FC6's unqualified second conjunct | **CLEAN**, with the arrow-quantifier caveat flagged at §3.2 |
| `DOWNSTREAM_CONSEQUENCE = none` | Q-434, Q-432, FC6 second conjunct, H_EXC (H1-19) failure-capability | **CLEAN** |
| Non-obstruction limb | flip family (K1-13), an actual construction — **not** H1-29 | **CLEAN** once the correction in §2.3 is stated |

[PROVABLE] Two items disclosed rather than claimed clean:

1. **Correction to my own prior artifact** (§3.4): I overstated the consequence of the FC6
   over-claim in `…MEMBERSHIP_REVIEW_DARIO_V001.md`. Logged, not buried.
2. **Correction made during this task**: I initially read H_EXC's direct-sum model as
   supplying the non-obstruction limb. It does not — H_EXC disqualifies it explicitly. The
   flip family supplies it. Had I not caught this, the determination would have rested on
   laundering the very object H_EXC rejects.

```text
VERB_AUDIT_SELF = CLEAN (+2 disclosed corrections, both to my own work)
```

## 6. Fence and stopping board

```text
OPEN_TERM_STATUS = named, tightened, and split
FC6_PHYSICAL_TERM = OPEN on asymmetric positive-source primitives only
LAW_REVISION_NEEDED = false
NEW_CLAUSE_NEEDED = candidate offered, NOT ADOPTED (principal's ruling)
MEMBER_BOUND = false
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
evaluation action was performed by this lane. No law was adopted.

OPEN_TERM = named
FC6_CLOSURE = AUTHORABLE (+binding sub-term `zeta`=0; +LOE4/LR remains OPEN/TYPE-U and is
not closed by the candidate law; +both limbs sealed verbatim at H_SEC §2.2, confirmed Q-449)
GUARD_ROW = scope_qualified (+downstream consequence: none — the sector-mixer exclusion
survives on FC6's unqualified second conjunct and on Q-434; A4/A5/A6 void conditions bite on
violation, not on unproven; the sole real cost is the all-rank cascade, which is upstream of
`[EQ6]` and was already PARTIAL/TYPE-U)
VERB_AUDIT_SELF = CLEAN (+2 disclosed corrections, both to my own work)
