# R-L2b's Uniformity Is Refuted — Result V001

STATUS: LANE RESULT. **A REFUTATION, ESTABLISHED.** Not a ruling; **this artifact takes no Part 2
row** — Part 2 is for ruled items, and filing a lane finding there is the defect this lane reported
on 2026-07-27 (R-6/R-7/R-8).
LANE: EINSTEIN. CHARTER: PASTE #113. DATE OF RECORD: 2026-07-28.

```text
alpha_computed = false ; proof_authorized = false ;
coupling_evaluation_authorized = false ; kappa_record_computed = false
NOTHING COMPUTED. NO F'-5 RULING TAKEN — O-1 IS THE PRINCIPAL'S.
THE PROGRAM IS NOT DECLARED BLOCKED OR DEAD.
```

---

## §0 — THE RESULT

```text
*** H1's ANTECEDENT IS DISCHARGED. NO SUCH M EXISTS. R-L2b's UNIFORMITY IS REFUTED. ***

R-L2b requires  sup_n ||X_n||_2 <= M  with M admissible under F'-5,
where X_n = C_n (V_n(a) - V_n(0)) C_n.
  X_n -> X strongly, hence weakly;  ||X||_2 <= liminf ||X_n||_2 <= M;
  but ||X||_2 = infinity.   => NO SUCH M EXISTS.
```

**A REFUTATION CANNOT BE FITTED.** Every input was obtained blind, by lanes with no corpus access
and no knowledge of what turned on the answer, or measured before the question was asked.

---

## §1 — THE TWO CHECKS THIS LANE OWED. **BOTH PASS.**

The adjudicator's exact criterion: *uniformity holds iff `Im a` multiplies only operators whose
compressions are norm-bounded uniformly in n.* The blind lanes were told `a` enters only through a
bounded perturbation. **That was a translation, and translations have failed twice in this chain.**

### CHECK 1 — Does `a` touch anything unbounded? **NO. Three sealed statements, one wording.**

```text
MAJORANT_SPEC:179 (D4)          "The expansion parameter is the CONNECTION DIFFERENCE; the record
                                 coupling is NEVER EXPANDED IN."
MAJORANT_SPEC:25                "parameter is the connection difference, NEVER the record coupling."
TRANSPORT_CHARTER:93            same wording, independently.
MAJORANT_LEMMA0_PROOF_DRAFT:365 "the connection difference enters each cell ONLY THROUGH [J]"
MAJORANT_LEMMA0_PROOF_DRAFT:513 "J = 1_D J 1_D since supp b_D is the closed [cell diamond]"
```

```text
=> a MULTIPLIES J ALONE. J IS BUILT FROM b_D, WHICH IS SMOOTH (Gevrey, b_D = exp(16 - 1/s)) AND
   COMPACTLY SUPPORTED IN THE CELL DIAMOND — HENCE BOUNDED. Its norm ||b_D|| is one of F'-5's four
   PERMITTED functional arguments, so finiteness is not an assumption but a structural given.
=> a DOES NOT ENTER h_0, THE CARRIER, OR THE CELL GEOMETRY. The record coupling — where the sharp
   localizer and the unit-modulus phases live — IS EXPRESSLY NEVER EXPANDED IN.
=> THE UNIFORMITY INPUT HOLDS: for the Hermite projectors Q_n, which ARE orthogonal projectors,
   ||Q_n J Q_n|| <= ||J|| for every n. Exact, no estimate.
   (Note the distinction that mattered in the last return: Q_n's projectorhood is what this uses.
   C_mix's NON-idempotence bears on the C-factor, not on this input, and does not disturb it.)
```

### CHECK 2 — Is the profile deformed by `a`? **NO.**

```text
D6' IS a-FREE. Grepped for the parameter across the whole of D6': NO OCCURRENCE.
  r(t) = min(t, 1-t) ; v(t) = tau_R · 32 r(t)^3 ; M(t) = Q 1_{|x| <= r(t)} Q
  — all FROZEN SEALED DEFINITIONS, "not softenable by any lane", and ALL INDEPENDENT OF a.
=> a IS A BOUNDED COEFFICIENT, NOT A DEFORMATION. The one route to an eps threshold the
   adjudicator named — a complex-translating or dilating the profile — DOES NOT OCCUR.
   NO eps THRESHOLD. The bound is finite for every eps > 0.
```

---

## §2 — THE CHAIN, LINK BY LINK, WITH ITS PROVENANCE

```text
LINK 1  sup_n ||C_n|| <= 1, BOTH PINNED SCHEMES.
        MEASURED, and measured before the question was asked:
        C_pure_projector_residual = 2.220446049250313e-16  (machine zero: it IS a projector)
        C_mix spectrum = [0.03905128961944969, 0.9609487103805515]  (Hermitian contraction)
        Source: stage8_execution/work/T07_control4_v3_blind_commit_v001.json. THIS LANE.
LINK 2  sup_n sup_polydisc ||V_n(a)|| < infinity.   *** BLIND REFERRAL 3 (H-VU). ***
        sup_n ||V_n(a_-,a_+)|| <= exp( (|Im a_-| + |Im a_+|) * C_J ),  C_J := Int_J ||M_c(t)|| dt.
        n APPEARS NOWHERE IN THE CONSTANT. Lumer-Phillips / Dahlquist logarithmic-norm bound
        ||e^{-i(A+iB)t}|| <= e^{t||B||}, INDIFFERENT TO ||A|| — including ||A|| = infinity.
        THE ||Q_n h_0 Q_n|| ~ n^theta WORRY DOES NOT BITE: it sits inside a factor that is EXACTLY
        UNITARY FOR EVERY n, because 2 Re<phi, -i A_n phi> = 0 for ANY self-adjoint A_n whatever
        its norm. A large self-adjoint generator makes the flow OSCILLATE, not GROW.
        Two refinements over the crude bound: only the IMAGINARY parts enter (so it returns exactly
        1 on the real slice, as it must), and only the L^1-IN-TIME profile norm enters.
        THIS LANE'S ADJOINT-CONTINUATION OBJECTION IS CLOSED: G_n(t,a)^dagger = G_n(t,abar), so
        continuing-the-dagger and daggering-the-continuation differ exactly by a -> abar; since
        ||X^dagger|| = ||X|| and |abar| = |a|, BOTH CONVENTIONS OBEY THE SAME BOUND. A norm question
        cannot be sensitive to the convention. The non-normality attack was run by a dedicated
        refuter and died: the estimate is a NUMERICAL-abscissa estimate, blind to the
        spectral/numerical gap by construction; the condition-number form is closed by the LOWER
        half of the same Gronwall estimate.
LINK 3  PRODUCTS. Strong convergence is not preserved under products in general; IT IS under
        uniform boundedness. Links 1 and 2 supply exactly that. => X_n -> X strongly.
LINK 4  C_n -> C STRONGLY.  *** TWO INDEPENDENT DERIVATIONS. ***
        (a) BLIND REFERRAL 2: squeeze on spectral measures; the gap is exactly mu^psi({0}) = 0
            because 0 IS NOT AN EIGENVALUE of the massless h_0. Kernel objection dies (f(0)=g(0)=0);
            pollution objection dies twice (massless => no gap => the Dirac pollution disease is
            absent by construction; and spurious eigenvalues carry asymptotically zero weight).
            Covers C_pure directly.
        (b) THE CORPUS'S OWN 2026-07-24 RESULT, four days earlier and independent:
            PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_DERIVED, a79939ad… (hash-pinned "for Phase B",
            recomputed by this lane and matching). Same measure-zero-discontinuity argument.
        (c) C_mix: neither referral's route applies (it is not idempotent), and it does not need
            one — Q_n -> I strongly with ||Q_n|| <= 1 and P_- fixed gives Q_n P_- Q_n -> P_-
            strongly by LINK 3 itself. THIS LANE.
LINK 5  PROPAGATORS CONVERGE STRONGLY, uniformly on compact time intervals.
        *** BLIND REFERRAL 1 *** — requirement items (3), (4), (5), six agents, unanimous.
        Trotter-Kato on the free part plus a bounded-perturbation Duhamel/Gronwall step.
LINK 6  ||X||_2 = infinity.  C1's off-diagonal modulus EXACTLY 1/(2 pi^2 |r|^3), homogeneous
        degree -3 (E1 v001:99, :594, verified at source by this lane). A degree -3 kernel on R^3
        is NOT Hilbert-Schmidt. Corroborated by the spec's own D7'(b), which places the divergence
        at the same volume diagonal.
LINK 7  WEAK LOWER SEMICONTINUITY of ||·||_2. Standard.
```

**THE ONE INPUT THIS LANE DID NOT RE-RUN, SAID PLAINLY:** the derived lemma `P alpha_x P = -n_x P`
and its 1.145e-16 / 200-direction numerical check, taken from the trilemma as cited.

---

## §3 — THE BLIND PROTOCOLS, ON THE FACE OF THE RESULT

```text
REFERRAL 1 (Trotter-Kato / requirement items 3,4,5): six agents — THREE ASSIGNED TO PROVE, THREE TO
  REFUTE — each cross-examined. UNANIMOUS.
REFERRAL 2 (C_n -> C): six agents — three prove, two refute, ONE WELL-POSEDNESS SCEPTIC — each
  cross-examined. UNANIMOUS AT HIGH CONFIDENCE, with a hand-checked proof and numerical confirmation
  in an exactly-solvable surrogate. "NOT well posed" was tested by a dedicated sceptic and REJECTED
  ON PROOF.
REFERRAL 3 (H-VU): six agents — three prove, two refute, ONE ARGUING ILL-POSEDNESS — each
  cross-examined. UNANIMOUS AT HIGH CONFIDENCE, WITH THE MATHEMATICS RE-DERIVED BY THE ADJUDICATOR
  RATHER THAN VOTE-COUNTED, corrections issued to three of the six attempts, and a counterexample
  closing the weaker-hypothesis question.
NO LANE HAD CORPUS ACCESS. NO LANE KNEW WHAT TURNED ON THE ANSWER. Codex was offered referral 2 and
  STOPPED on its own contamination declaration (D1 = NO, D2 = NO, D3 = YES), which is why it ran
  elsewhere — recorded because a declined referral is part of the provenance.
AND THE INDEPENDENT-LANE C-L3 PART A PRE-REGISTRATION, which established that nothing sealed absorbs
  the divergence and that the nonzero-as-failure typing was adopted and NOT derived.
```

---

## §4 — CONSEQUENCES. **REPORTED, NOT ACTED ON.**

R-L2b carried **four** discharges. **This artifact changes the status of none of them by fiat; it
reports what the refutation implies and leaves every decision open.**

```text
(1) R-L2b ITSELF — THE OBLIGATION AS WRITTEN CANNOT BE MET. Not "the program fails": the
    obligation demanded a finite Hilbert-Schmidt bound uniform in the carrier, and no such bound
    exists because the limit object is not Hilbert-Schmidt at all.
(2) T11's RESPONSE HALF — consumed R-L2b. Now rests on an obligation shown unmeetable as written.
(3) THE D3 REFINEMENT-NATURAL WEIGHT'S RESPONSE SIDE — same.
(4) CONNECTED EXTENSIVITY — the campaign's own binding declared these FOUR OBLIGATIONS TO BE ONE
    ESTIMATE, with the outcome named in advance: "if R-L2b closes, extensivity closes with it."
    *** THAT BINDING WAS WRITTEN FOR THE CLOSING BRANCH. THE REFUTING BRANCH IS THE ONE THAT
    OCCURRED, AND WHAT THE BINDING IMPLIES ON IT IS NOT STATED ANYWHERE. NAMED AS A GAP, NOT
    FILLED. ***
```

```text
O-1 / F'-5 — *** ITS HELD-PENDING CONDITION IS NOW SATISFIED. *** O-1 was recorded HELD pending
  exactly the Trotter-Kato referral that has now returned, and the trilemma's own reading is that
  "keeping F'-5 selects the branch on which R-L2b is refuted." THE BRANCH HAS OCCURRED.
  *** THE F'-5 RULING IS THE PRINCIPAL'S AND IS NOT TAKEN HERE. O-1 IS NOW RIPE, NOT RULED. ***
THE FOURTH-HORN QUESTION — whether a finite Hilbert-Schmidt bound was EVER the right obligation —
  is the corpus's own, is open, and is the principal's. NOT ANSWERED HERE, AND NOT PREJUDGED: this
  result establishes that the obligation as written cannot be met; it says nothing about whether it
  should have been written that way.
```

## §5 — FLAGS

```text
RL2b_uniformity_refuted                 = true
H1_antecedent_discharged                = true
H_VU_discharged                         = true       # blind referral 3
H_VU_check1_a_touches_only_bounded      = PASS       # connection difference only; b_D bounded
H_VU_check2_profile_a_deformed          = false      # D6' is a-free
eps_threshold_exists                    = false
C_factor_uniform_bound                  = true       # both pinned schemes, measured
V_factor_uniform_bound                  = true       # exp((|Im a_-|+|Im a_+|) C_J), n-free
Cn_to_C_strong                          = true       # two independent derivations + C_mix route
propagators_converge_strongly           = true       # blind referral 1
X_HS_norm_infinite                      = true       # C1 degree -3 modulus, verified at source
blind_referrals_consumed                = 3
refutation_could_be_fitted              = false
RL2b_four_discharges_status_changed_here = false     # REPORTED, NOT ACTED ON
extensivity_binding_on_refuting_branch  = UNSTATED_IN_CORPUS   # §4(4), named as a gap
O1_F5_ripe                              = true
O1_F5_ruled                             = false      # THE PRINCIPAL'S
fourth_horn_answered                    = false      # THE PRINCIPAL'S
program_declared_blocked_or_dead        = false
part2_row_written                       = false      # THIS IS A FINDING, NOT A RULING
alpha_computed = false ; proof_authorized = false
```

## §6 — INVENTION CHECK

```text
NOTHING COMPUTED. NO kappa_record, NO alpha, NO coupling. NO F'-5 RULING TAKEN.
THE TWO CHECKS THIS LANE OWED WERE RUN AT SOURCE AND ARE THE ONLY REASON THIS SEALS: the blind
result transfers BECAUSE a multiplies the connection difference alone and the profile is a-free,
both verified in sealed text rather than accepted from the translation. Had either failed, per the
charter, nothing would have been sealed.
NOT RE-RUN BY THIS LANE AND SAID SO: the P alpha_x P = -n_x P lemma and its 200-direction check;
the three blind protocols themselves, which live in the supervision repo.
NO PART 2 ROW WRITTEN. A refutation established by a lane is a FINDING; Part 2 is for RULED items.
Filing lane determinations there is the R-6/R-7/R-8 defect this lane reported and does not repeat.
THE EXTENSIVITY BINDING'S SILENCE ON THE REFUTING BRANCH IS NAMED AS A GAP AND NOT FILLED — filling
it would be inferring a consequence the corpus never stated.
kappa NAMING OBSERVED: kappa_record in full, never bare.
```
