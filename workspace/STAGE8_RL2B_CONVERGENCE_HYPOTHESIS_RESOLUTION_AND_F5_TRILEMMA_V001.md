# R-L2b: Resolution of the Convergence Hypothesis, and the F'-5 Trilemma V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY. Successor to STAGE8_RL2B_DIAGONAL_ATTACK_RESULT_V001
(07ea1496b3391aa3f514), which closed by naming ONE unestablished
hypothesis and handing a typing decision to the principal.
THIS ARTIFACT RESOLVES THE STATUS OF THAT HYPOTHESIS FROM SEALED TEXT
and CORRECTS THE PRIOR ARTIFACT'S FRAMING OF THE DECISION.
No numerical value is computed. No spec is edited. No obligation is
weakened. F'-5 IS NOT TOUCHED.
PRODUCTION PROHIBITED. alpha_computed = false. proof_authorized = false.
coupling_evaluation_authorized = false.
```

## 0. What was asked, and what this answers

The prior attack derived, conditional on ONE hypothesis, that the continuum
`X = C (V(a) - V(0)) C` is not Hilbert-Schmidt and therefore that R-L2b's
uniform bound cannot hold. The hypothesis was: **the Galerkin scheme
converges.** It was named, flagged as unestablished, and not resolved.

This artifact does not need the principal's typing decision to proceed, so
it was taken first. It establishes the hypothesis's status in the sealed
corpus, and finds that the decision the prior artifact handed over is
NARROWER THAN THAT ARTIFACT SAID.

## 1. What the corpus DERIVES

```text
SEALED, STAGE8_T7_PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_RESULT_V001:
  C_n^(pure) -> P_-  STRONGLY.
  pure_state_strong_convergence_derived = true
AND ITS OWN LIMITING CLAUSE, quoted:
  "Strong convergence of one-particle covariances does not by itself imply
   convergence of growing-dimensional quasifree determinants."
  global_determinant_convergence_derived = false
```

So one-particle covariance convergence is DERIVED. The corpus then stops,
explicitly, at the boundary of the extrapolation — and that caution is
correct and is respected below.

## 2. A SEALED IMPOSSIBILITY that reframes the whole question

`STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001` withdrew the label
`PARENT_STATE_REGULATOR_RESTRICTION_DERIVED` and recorded, verbatim:

```text
The sealed specification required a nonzero nested finite-rank family Q_n
satisfying [Q_n,h_0]=0; Q_n -> I strongly.
"That family does not exist for the free massless Dirac multiplier. A
 nonzero finite-dimensional reducing subspace would contain an L2
 eigenvector of h_0, while h_0 has purely continuous spectrum."
genuine_finite_rank_continuum_restriction_constructed = false
```

**This is a proof of impossibility, not a gap.** It is also the reason the
Galerkin carrier cannot be treated as a harmless bookkeeping device: `Q_n`
PROVABLY does not commute with `h_0`, so the finite object is never a
sub-dynamics of the parent. The correction states the consequence itself:
`"Exact commutation with h_0 is neither required nor possible."`

## 3. The corpus HAS ALREADY WRITTEN DOWN my hypothesis — as an obligation

The same correction specifies the replacement. Quoted verbatim:

```text
A genuine Galerkin family must instead satisfy:
  Q_n is finite rank and nested;
  Q_n -> I strongly;
  Q_n h_0 Q_n converges to h_0 on a common core;
  Q_n M_c(t) Q_n converges strongly to M_c(t);
  and the finite propagators converge strongly, uniformly on compact times.
```

**That list IS the hypothesis the diagonal attack named.** The corpus stated
it before I did, as a REQUIREMENT ON FUTURE WORK. Its status, item by item:

```text
(1) finite rank and nested          STANDARD, holds for Hermite projectors
(2) Q_n -> I strongly               STANDARD (Hermite basis is complete)
(3) Q_n h_0 Q_n -> h_0 on a core    NOT DISCHARGED
(4) Q_n M_c Q_n -> M_c strongly     NOT DISCHARGED
(5) finite propagators converge     NOT DISCHARGED  <-- what my argument needs
```

A parallel list appears in `STAGE8_T7_COMPLETED_CONTINUUM_RESPONSE_PROVENANCE_SPEC_V001`
(six clauses, same content plus charge/grading/spinor typing and a no-fitted-pulse
clause). Same status.

## 4. The one theorem that looked like a discharge, and why it is NOT

`FINITE_PARENT_ANALYTIC_AUTHORITY_V001` contains a smooth-to-sharp
stability theorem concluding, verbatim: `"Thus the propagators converge in
operator norm, hence strongly."` **That sentence does not discharge item (5),
and the theorem says so itself.**

```text
ITS HYPOTHESIS:   integral ||V_epsilon(t) - V(t)|| dt -> 0   [OPERATOR NORM]
ITS EXCLUSION, verbatim: "The theorem does not assert this limit for
  approximation families that fail the stated L1 operator-norm condition."
```

**The Galerkin family fails that condition, provably:**

```text
Q_n -> I STRONGLY but NEVER IN NORM: ||Q_n - I|| = 1 for every n, since a
finite-rank projection cannot norm-approximate the identity in infinite
dimensions.
||Q_n V Q_n - V|| -> 0 would therefore require V COMPACT.
V IS NOT COMPACT: it contains multiplication by b_D(t,x) and by the cell
indicator 1_{|x|<=r(t)}, and a multiplication operator on L2(R^3) is
compact ONLY IF the multiplier vanishes a.e.
=> the L1 operator-norm hypothesis FAILS. The theorem is inapplicable.
```

That theorem is about **smooth-to-sharp regularization of the interaction**
(`V_eps -> V`), an entirely different limit from **Galerkin truncation of
the carrier** (`Q_n V Q_n -> V`). Reading it as covering the second is the
program's characteristic failure mode again — the proved object is real but
is not the object the verdict would need.

**What item (5) actually needs is Trotter-Kato**: strong resolvent
convergence of generators on a common core implies strong propagator
convergence, uniformly on compact time intervals. That is exactly what item
(3)'s common-core clause is for. So the requirement list is a well-formed
Trotter-Kato hypothesis set, it is very likely satisfiable for a nested
Hermite family on a Schwartz core, and **it is not proved anywhere in this
corpus.**

## 5. F'-5 REMOVES THE FREEDOM THE PRIOR ARTIFACT ASSUMED

`STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002` F'-5, verbatim:

```text
"Every constant, radius, decay rate and tolerance is an explicit functional
 of (||b_D||, tau_R, sea-kernel decay data, |w_lambda|) ONLY. No carrier
 index n, no ell, no truncation level, no cellulation-family index, AND NO
 CELLULATION GEOMETRIC DATUM."
AND, in the same spec: "weakening F'-5 is not a lane's to do and this spec
 may not execute on a provably unsatisfiable obligation."
```

**F'-5 is, in substance, the demand that the answer be UNIFORM IN n.** The
prior artifact framed the open question as "finite carrier OR continuum
limit, the principal's choice." That framing is too generous to the first
branch: F'-5 already forbids the constant to carry a carrier index. The
choice is not which carrier — it is whether F'-5 stands.

## 6. THE TRILEMMA

Let `X_n = C_n (V_n(a) - V_n(0)) C_n`. R-L2b requires `sup_n ||X_n||_2 <= M`
with `M` admissible under F'-5.

```text
H1  THE REQUIREMENT LIST IS DISCHARGED (items 3,4,5 proved).
    Then X_n -> X strongly, hence weakly.
    The Hilbert-Schmidt norm is weakly lower semicontinuous:
        ||X||_2 <= liminf ||X_n||_2 <= M.
    But the DERIVED lemma P alpha_x P = -n_x P  (verified 1.145e-16 over 200
    random directions) gives C alpha_x C = -p_x C, degree 0, hence a
    degree -3 kernel for X, hence ||X||_2 = infinity -- consistent with the
    sealed C1 off-diagonal modulus exactly 1/(2 pi^2 |r|^3).
    => NO SUCH M EXISTS. R-L2b's UNIFORMITY IS REFUTED.

H2  THE LIST IS NOT DISCHARGED (and cannot be).
    Then the finite objects do not approximate the parent at all. Any bound
    proved on X_n is a bound on something that is not the parent's object --
    the OBJECT-VS-BOUND failure form, instance 3 of the standing tripwire --
    and its constant carries n, violating F'-5 directly.

H3  DENY THE CONTINUUM TARGET: the theory IS the finite-carrier theory.
    Then kappa_record acquires a carrier index and F'-5 must be weakened.
    The spec forbids a lane to do this, and it is the principal's alone.
```

**Every horn costs something, and no horn delivers R-L2b as written.** H1
refutes it. H2 disqualifies the bound as evidence about the parent. H3
requires amending a sealed scoping clause.

Note also the self-executing clause: if H1 holds, R-L2b under F'-5 is a
**provably unsatisfiable obligation**, and E1 v002's own text then says the
spec may not execute on it. That consequence was written into the spec
before today and is not being invoked by preference.

## 7. CORRECTION TO MY OWN PRIOR ARTIFACT

`STAGE8_RL2B_DIAGONAL_ATTACK_RESULT_V001` closed: *"the question 'does R-L2b
close' has become the question 'at what carrier is kappa_record defined',
which is a typing decision he holds."* **That understated the constraint.**
F'-5 has already excluded carrier-indexed constants, so the principal's
decision is not a free choice between two live typings; it is whether to
keep F'-5, and keeping it selects the branch on which R-L2b is refuted.
The prior artifact is NOT withdrawn — its lemma, its refutation of the
finite-rank framing, and its identification of U3 all stand. Only its
closing characterisation of the decision is corrected here.

## 8. WHAT IS NOT CLAIMED

```text
R-L2b IS NOT DECLARED DEAD. H1's hypothesis is UNDISCHARGED, and the whole
refutation rests on it.
THE NEGATIVE EXISTENTIAL IS BOUNDED, NOT ABSOLUTE: searched the corpus for
common core / propagators converge / uniformly on compact times /
norm-resolvent and for convergence-flag booleans; three files matched and
all three were read. DEFECT 2 was a false negative existential from exactly
this kind of search, so this is stated as "not found in a targeted search,"
never "does not exist."
THIS LANE'S ERROR RECORD ON THIS EXACT CLASS IS SEVEN INSTANCES, the most
recent being continuum-vs-Galerkin -- the same axis as this finding. That is
a reason for independent check, and the reason the recommendation below is
a blind referral rather than an adoption.
```

## 9. RECOMMENDATION

```text
1. REFER TO CODEX BLIND: "Does the sealed successor Galerkin requirement
   list admit a Trotter-Kato discharge for a nested Hermite family on a
   Schwartz core?" A YES makes H1 live and refutes R-L2b's uniformity. Do
   not send this artifact's conclusion with the question.
2. THE PRINCIPAL'S DECISION IS RESTATED: not "which carrier", but "does
   F'-5 stand as written". Nothing else in this artifact is his to decide.
3. U3 REMAINS THE PROPAGATION DEFECT. It is now load-bearing twice over --
   named in the arm-2 binding, missing from E1 v002, and the pivot of both
   the prior attack and this trilemma. The append-only amendment closing it
   is still unauthorized and still recommended.
```

## Protected status

```text
convergence_hypothesis_status = WRITTEN_AS_A_SEALED_REQUIREMENT_NOT_DISCHARGED
requirement_list_items_discharged = 2 of 5   (both standard; 3,4,5 open)
smooth_to_sharp_theorem_covers_galerkin_truncation = false   (DERIVED: V not compact)
trotter_kato_discharge_attempted_here = false
F5_forbids_carrier_indexed_constants = true   (verbatim)
RL2b_uniform_bound_refuted = CONDITIONAL_ON_H1
RL2b_declared_dead = false
prior_artifact_withdrawn = false   (closing characterisation corrected only)
spec_edited = false
F5_weakened = false
obligation_weakened = false
kappa_record_carrier_typing = UNDECIDED_PRINCIPALS
production_authorized = false
alpha_computed = false
proof_authorized = false
```
