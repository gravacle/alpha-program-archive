# THE FLOOR BOUNDARY VALUE IS SETTLED: NEITHER A SPECTRAL FACT NOR A SUBTRACTION CHOICE

Reviewer lane, 2026-07-30, at the principal's instruction to settle it. Every claim carries
file:line and a verbatim quote. No value is computed.

## 1. THE QUESTION

`Gamma_BR,k_R = 0` — the vanishing of the public gauge stiffness at the record floor — was disputed.

**POSITION A (the slot-9 theory attack, `BOHM_SLOT9_THEORY_ATTACK_2026-07-29.md`, Class 2(i)):**
"`K_bare = 0` is not a derived property of a complete spectrum; it is the statement that the boundary
condition is imposed at the lower endpoint. **The floor *is* the subtraction.**" On this reading the
value is a scheme choice, `c_R` is "the integration constant of a first-order RG flow for a marginal
coupling," and slot 9 is unclosable as posed.

**POSITION B (the principal, 2026-07-29):** the lower endpoint of the proper-time integral IS the
record scale, so at that scale the range is empty and the coefficient is zero **by arithmetic, not by
stipulation**. Combined with the capacity principle — `lambda_0(D_BR^2) = k_R^2` with
`N_BR(k_R) = 1`, i.e. the record scale is the LOWEST EIGENVALUE OF THE OPERATOR, a fact about the
operator — the chain runs OPERATOR -> FLOOR -> BOUNDARY VALUE, and `c_R` is not an independent
freedom but the shadow of the action-form freedom. Leg 1 was judged SOUND on 2026-07-29; leg 2 failed,
on the recorded ground that the corpus forbids the circular order
`k_R -> Gamma_BR,k_R -> H_phys -> K_pub -> k_R` (ledger row 167, REJECTED
`violates_noncircular_capacity_order`) and that the capacity equation is a constraint, not a
definition.

## 2. THE DECISIVE POINT, AND IT IS NEW — THE TWO OBJECTS ACT ON OPPOSITE ENDS OF THE INTEGRAL

`alpha_induced_only_boundary_action_principle_v001.md:9-14`:

```
Gamma_BR,k
  = -(1/2) integral_(1/k_R^2)^(1/k^2) ds/s
      STr'_BR exp(-s L_BR).
```

`alpha_first_durable_record_capacity_principle_v001.md:10-22`:

```
N_BR(k) = Tr_BR 1_[0,k^2](D_BR^2).
...
N_BR(k) = 0                 for k < k_R,
N_BR(k_R) = 1,
lambda_0(D_BR^2) = k_R^2,
lambda_1(D_BR^2) > k_R^2.
```

**THE CAPACITY CONDITION IS A STATEMENT ABOUT THE BOTTOM OF THE SPECTRUM. THE PROPER-TIME FLOOR IS A
CUT AT SMALL `s`. THOSE ARE DIFFERENT ENDS OF THE SAME INTEGRAL, AND NEITHER ENTAILS THE OTHER.**

- In `STr' exp(-s L)`, the bottom of the spectrum governs LARGE `s`: as `s -> infinity` the trace is
  dominated by `exp(-s lambda_0)`. A positive `lambda_0 = k_R^2` therefore delivers exponential decay
  at large `s` — INFRARED convergence.
- The `F^2` coefficient's logarithm comes from SMALL `s`, where `integral ds/s` diverges and all modes
  contribute. The floor `s >= 1/k_R^2` cuts exactly there. It is an ULTRAVIOLET cutoff in proper time.
- **`exp(-s L)` is well defined and nonvanishing for every `s > 0` no matter where the spectrum
  starts.** A lowest eigenvalue cannot empty the small-`s` range. There is no value of `lambda_0`
  that makes the integrand absent below `1/k_R^2`.

So the second arrow of OPERATOR -> FLOOR -> BOUNDARY VALUE is not a weak step awaiting more work. It
is a **type mismatch**: it asks a bottom-of-spectrum condition to produce a top-of-integral cutoff.

**CONSEQUENCE THAT MATTERS OPERATIONALLY: the chain cannot be completed by discharging its own named
gaps.** `STAGE8_OPERATOR_FLOOR_BOUNDARY_CHAIN_CANDIDATE_DERIVATION_V001.md` names its first
obstruction at step 1 (the complete normalized `L_BR`) and its second at step 2 (the lowest
eigenvalue for the complete public operator). **Closing both would still not yield the floor.** Even a
fully derived complete operator with an isolated lowest eigenvalue exactly at `k_R^2` leaves the lower
limit of the proper-time integral unfixed. The chain's binding defect is at step 4, which it types
honestly as ADOPTED, and no repair of steps 1-3 reaches it.

**BOUNDED NEGATIVE, and it is the cleanest one this program has produced.** Roots:
`Documents/New project/gravity_emergence_evidence_program`, `MB Work/alpha_supervision`. Types
`*.md *.json`. Exclusions `node_modules`, `external/`, `custodian_private`. Case-insensitive on the
endpoint terms.

```
files mentioning a lower endpoint / lower limit / lower proper-time boundary:  12
files mentioning lambda_0:                                                    16
files mentioning BOTH:                                                         0
```

**The two objects have never appeared in the same file, in either direction.** The chain that links
them is asserting a connection between two things no artifact in the program has ever discussed
together. Separately, no artifact anywhere distinguishes the small-`s` from the large-`s` end of this
integral (searched `small s|small-s|large s|large-s|ultraviolet end|infrared end`; the only matches
were the substring `large-s` inside "large-scale" in the Newtonian-limit series, a different subject).

## 3. THE SETTLEMENT — BOTH POSITIONS WERE WRONG ABOUT THE THIRD OPTION

**THE FLOOR BOUNDARY VALUE IS THE CONTENT OF THE INDUCED-ONLY AXIOM. IT IS NOT A SPECTRAL
CONSEQUENCE, AND IT IS NOT A SUBTRACTION SCHEME.**

The principle says so in its own words, and the operative verb is decisive —
`alpha_induced_only_boundary_action_principle_v001.md:16-19`:

> "The lower proper-time boundary is the first durable record scale; `Gamma_BR,k_R=0` **states** that
> no separate public stiffness is installed before the record branch opens."

It *states*. It does not derive, and it is not a choice of where to subtract: it is a claim about
public field CONTENT — there is no public `F^2` above the record scale because there is no public
field there. That is a physical proposition with physical consequences, and it is adopted.

Position A is right that it is not derived from the spectrum. Position B is right that it is not an
arbitrary subtraction point. Neither is right that it is one or the other.

The corpus's own typing already agrees, and had been written before the dispute:
`STAGE8_OPERATOR_FLOOR_BOUNDARY_CHAIN_CANDIDATE_DERIVATION_V001.md` flags
`proper_time_floor_status = ADOPTED_BY_INDUCED_ONLY_FUNCTIONAL` and
`gamma_at_floor_zero = DERIVED_GIVEN_FLOOR`. The vanishing is derived *given* the floor; the floor is
the axiom. What was missing was the reason no future work changes that, and section 2 supplies it.

## 4. WHAT THIS SETTLES ABOUT F-SHIFT

**`alpha`'s conditionality equals the induced-only axiom's status, exactly and no more.** Not the
capacity principle's, not a scheme's. The attack's own parameter accounting states the size of the
debt: "with the whole bare basis allowed there are five unknowns; with induced-only adopted there are
two. The postulate supplies precisely the missing constraints."

And it supplies the attack's own escape clause: "Predicting a dimensionless number from a postulate
that contains exactly one free dimensionless number per predicted coefficient is a reparametrization,
not a prediction — **unless the postulate is independently earned by predicting something else
first.**"

**THAT CLAUSE IS SLOT 18**, the one unused structure-sensitive NON-alpha prediction. And FINAL-CLAIM
already rests on slot 18 rather than on alpha. So this settlement explains a design choice the program
had already made for other reasons: the axiom that gives alpha its conditionality is precisely what
slot 18 would earn. **Slot 18 is therefore load-bearing for alpha's EPISTEMIC STATUS while remaining
irrelevant to alpha's VALUE.** It cannot fix a normalization (Q-13) and it can retire the postulate's
freeness. Both are true and they are not in tension.

REVISED STATEMENT OF F-SHIFT, replacing "the leg with no instrument":

> F-shift admits no instrument from inside the program's condition class, and this is proved rather
> than merely unattempted — the class is closed under `K -> K + c`. Four exits were enumerated
> (E1 UV fixed point, E2 superconvergence, E3 boundary condition at a derived scale, E4 integer
> pairing); E2 contradicts the program's own running result, E3 has an executed countermodel, E4 has
> no candidate and the discrete measure data enter additively, and E1 cannot be posed because an
> induced-only action has no public ultraviolet region. **The floor route is not a fifth exit; it is
> the axiom restated.** The live options are exactly two: name a genuine fifth exit, or earn the
> induced-only axiom through slot 18.

## 5. ONE CANDIDATE FIFTH EXIT, TYPED AND NOT ADOPTED

`Gamma_K` + `C_record(K)` may be a fifth exit, and it is not any of E1-E4 in kind — it is an
EXISTENCE / ONSET condition, not a scale-boundary condition, a fixed point, compositeness, or a
topological pairing. `primitive_record_cell_selection_principle_v002.md:95-97,:104` poses
`C_record(K_*) = 0`, `dC_record/dK != 0`, `K_* > 0`, `alpha_micro = 1/(4 pi K_*)`.

**THE HONEST TYPING, AND IT CUTS BOTH WAYS.** An onset condition on the physical stiffness fixes the
TOTAL `K`, not the split between induced part and counterterm. For alpha's VALUE that is sufficient —
`alpha_micro = 1/(4 pi K_*)` consumes the total. For slot 9 AS POSED it is not: the slot demands
EXCLUSION of the deformation, and fixing the sum makes the deformation MOOT rather than excluded. That
is precisely the disposition the attack judged inadequate for E4 ("the anchor fixes the *sum*, so the
counterterm becomes moot instead of excluded").

**So the distinction to hold is between alpha and slot 9, and the attack's own recommendation already
points at it: "Slot 9 should be retired as posed and replaced by the exit question."** A condition
that determines the total would deliver the number while leaving slot 9 undischarged in its own terms.
Whether that is acceptable is a principal question, not a lane one, and it is NOT settled here.

REQUIRED BEFORE THIS COUNTS AS AN EXIT: the onset condition must itself be DERIVED rather than
adopted, and it must be overdetermined — two independent requirements meeting on one value. An adopted
onset condition is another postulate with one free number, which is the same defect one level up.

## 6. SCOPE — WHAT THIS DOES NOT DO

- Does NOT discharge slot 9, slot 6, slot 12, or any other slot. Zero of eighteen remain derived.
- Does NOT compute or authorize `alpha`, `kappa_record`, `kappa_Thomson`, `K`, `c_R`, `x`, `rho`,
  `T_R`, or any root, radius, scale, eigenvalue or coupling.
- Does NOT refute the induced-only axiom. It types it, and the typing is that it is a physical
  proposition carrying real content, adopted.
- Does NOT reopen E1. The structural obstruction stands: an induced action defined only below `k_R`
  has no public ultraviolet region for a fixed point to inhabit.
- Does NOT weaken leg 1 of the principal's argument. `Gamma_BR,k_R = 0` given the floor is exact
  arithmetic. What fails is the claim that the floor follows from the operator.
- Does NOT amend any immutable artifact, and edits no sealed artifact.

## 7. FALSIFIERS

- **F-FL1.** Exhibit an operator condition that fixes the SMALL-`s` end of the proper-time integral.
  Section 2's mismatch would then be repaired and leg 2 would reopen. A bottom-of-spectrum condition
  cannot do this; a statement about the domain, the measure, or the admissible mode content might.
  **This is the one repair worth attempting and it is well posed.**
- **F-FL2.** Show that the record scale enters the integral's lower limit by a route that does not
  pass through the induced-only axiom — i.e. that some other adopted or derived principle independently
  fixes it. The bounded negative in section 2 predicts no such route exists in the current corpus.
- **F-FL3.** Show that `alpha_micro = 1/(4 pi K_*)` consumes something other than the total physical
  stiffness, which would break section 5's reading.

`alpha_computed = false`; `proof_authorized = false`; `kappa_record_computed = false`.
