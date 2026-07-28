# C-L1 Attempt — Result: **REFUTED AT A NAMED LINE**, With an Exact Counter-Identity

STATUS: LANE ATTEMPT RESULT. **A PROOF WAS ATTEMPTED AND THE NEGATION WAS PROVED.** Not a
determination. LANE: EINSTEIN. CHARTER: PASTE #116 (re-issue of #98). DATE: 2026-07-28.

```text
alpha_computed = false ; proof_authorized = false ;
coupling_evaluation_authorized = false ; kappa_record_computed = false
C-L3 NOT REACHED. F'-1 NOT TRIGGERED. D6' HONOURED — NOTHING SMOOTHED, MOLLIFIED OR REGULARIZED.
```

---

## §0 — THE RESULT

```text
OUTCOME: *** C-L1 IS FALSE AS WRITTEN. *** Not uncertified, not well-posed-but-hard.
OBSTRUCTION, AT THE LINE: STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:1133-1134,
  the words "exactly on the ball where M(t) = 1".
                        *** THERE IS NO SUCH BALL. ***
```

**AND IT DOES NOT REDUCE TO C-L2 — IT IS IN TENSION WITH IT.** The failure survives with the C-L2
commutator set identically to zero.

---

## §1 — THE MECHANISM. AN INTEGRAL WAS TAKEN WITH M(t) DROPPED, THEN M WAS PUT BACK.

D6', `SPEC_V002:465-466`, verbatim:

> `M(t) = Q 1_{|x| <= r(t)} Q,  r(t) = min(t, 1-t),  v(t) = tau_R · 32 r(t)^3,`
> `int_0^1 v(t) dt = tau_R = pi/sqrt(2) EXACTLY`

**THE NORMALIZATION `int v = tau_R` IS COMPUTED WITH M(t) DROPPED.** The propagator sees
`int_0^1 v(t) M(t) dt`, never `(int_0^1 v dt) · M` — because **`r(t) = min(t,1-t)` is t-dependent in
the same sealed line.** A point at radius `rho` lies inside the ball only while `min(t,1-t) >= rho`,
i.e. for `t in [rho, 1-rho]`. So the phase it actually accumulates is

```text
    f(rho)  =  int_rho^{1-rho} tau_R · 32 min(t,1-t)^3 dt  =  tau_R (1 - 16 rho^4)
```

**RE-DERIVED BY HAND AND VERIFIED AGAINST DIRECT QUADRATURE BY THIS LANE, INDEPENDENTLY OF THE
WORKFLOW:**

```text
rho = 0     quad 2.2214414693   formula 2.2214414691   ( = tau_R = pi/sqrt2 )
rho = 0.1   quad 2.2178871629   formula 2.2178871627
rho = 0.25  quad 2.0826013773   formula 2.0826013773
rho = 0.4   quad 1.3115390433   formula 1.3115390433
rho = 0.5   quad 0.0000000000   formula 0.0000000000   ( causal boundary: ZERO phase )
```

**THE CELL-INTEGRATED RECORD PHASE IS NOT TWO-VALUED ON A BALL. IT IS A RADIAL CONTINUUM**, sweeping
from `lambda tau_R` at the centre to `0` at the causal boundary. `lambda tau_R in {0, +pi, -pi}` is
an exact statement about the **numbers** `lambda` and `tau_R`; it is **the value of a radial profile
at one point.** C-L1 promotes a point value to an operator statement on a set of positive measure.

**AND THE CORPUS HAD FLAGGED THE PRESUPPOSITION AND NOT ACTED ON IT.**
`STAGE8_COLLAR_CONJUNCTION_CHARTER_RESULT_V001.md:152-158`, **DEFECT A, "reported, not repaired"**:
at least four load-bearing places reason as though M(t) were a bare sharp indicator, *"arguing 'on
the ball where M(t) = 1' … the very question this charter asks is PRESUPPOSED AWAY in four places
while being flagged open in two others."* **C-L1:1133-1134 is a fifth.** And `SPEC_V002:1441` says
it against itself: *"the exact record-phase collapse … is EXACT only where M(t) = 1"* — with D6' in
force, **that is nowhere.**

---

## §2 — THE COUNTER-IDENTITY, AND THE REFUTATION OF A FROZEN INPUT

Since every sealed `M(t)` is a concentric radial multiplication, time-ordering is trivial and

```text
    R_lambda  =  exp(-i lambda f(rho) S)  =  cos(lambda f) I  -  i sin(lambda f) S
```

With `w = (-1/4, +1/2, -1/4)` on `lambda = (0, +sqrt2, -sqrt2)` and `theta := 16 pi rho^4`:

```text
    *** sum_lambda w_lambda R_lambda  =  cos^2(8 pi rho^4) · I    (S-odd part identically zero) ***
```

**VERIFIED BY THIS LANE INDEPENDENTLY, TO 12 DIGITS:**

```text
rho = 0      sum = 1.000000000000    cos^2(8 pi rho^4) = 1.000000000000
rho = 0.15   sum = 0.999838122549                      = 0.999838122549
rho = 0.30   sum = 0.959126485840                      = 0.959126485840
rho = 0.45   sum = 0.264509455552                      = 0.264509455552
```

**C4 IS A FROZEN INPUT AND ITS OPERATOR-LEVEL CLAUSE IS FALSE.** `SPEC_V002:350-351`, verbatim:

> `sum_lambda w_lambda u_lambda = m_0(I-P) + 1·P = P — the weights`
> `PROMOTE the sharp causal-ball projector to the leading in-cell object.`

**That requires the weighted sum to equal 1 throughout the ball. At `rho = 0.45` it is 0.2645.**
`SPEC_V002:313-315` requires *"a new exact witness"* to contradict a frozen input; the two identities
above **are** that witness, and both were re-derived and re-verified by this lane.

```text
WHAT DIES:  C4's OPERATOR-LEVEL promotion only.
WHAT LIVES: C4's SCALAR clauses — m_0 = m_1 = 0, the symmetric-second-difference form, the ±pi
            arithmetic — ARE UNTOUCHED. The l1-mass saturation at rho = 0 is still exactly right.
CONSISTENCY CHECK THAT WOULD HAVE CAUGHT AN ERROR, AND DID NOT: the derived weighted sum is the
corpus's OWN closed form S(tau) = sin^2(sqrt2 tau/2) (C4_SATURATION_STRUCTURAL_BLIND_ANSWER:74-76)
evaluated at tau = f(rho) instead of only at rho = 0. The derivation REPRODUCES the sealed result as
its centre value and extends it — it does not contradict it.
```

---

## §3 — THE ERROR TERM, DERIVED. AND THE SHARP CONSTANT.

```text
inf_P  sup_lambda  || X_lambda - [(I-P) + phase_lambda·P] ||_op   =  SQRT(2)  EXACTLY,
                                                       attained at P = 1_{|x| <= 2^{-5/4}}
inf_P  sup_lambda  sup_psi |<psi, (·) psi>|                        =  1        (quadratic form)
```

**AN ERROR OF 1 IN THE QUADRATIC FORM AGAINST A UNITARY IS TOTAL, NOT SMALL.** There is no `eps < 1`,
and no small parameter anywhere in the frozen tuple makes it small — **it is the pure number 1.**

Not a thin-shell artifact: at the optimal `P` the pointwise error modulus is `>= 1` on **29.9%** of
the causal ball by volume, and `theta` exceeds `pi/2` on a fraction `1 - 2^{-3/4} = 0.4054` of it,
exactly.

**AND IT QUANTIFIES OVER EVERY P.** The refutation is not "the corpus chose P badly" — no orthogonal
projector works.

---

## §4 — **C-L1 DOES NOT REDUCE TO C-L2. THEY CANNOT BOTH BE SATISFIED.**

The reduction was attempted and the exact Duhamel split obtained: `X_lambda = R_lambda + E_comm`,
with `E_comm` generated **entirely** by `[h_0, M(t) ⊗ S]` — C-L2's object verbatim. If the residual
`R_lambda - [(I-P) + phase_lambda·P]` were zero, C-L1 would reduce cleanly to C-L2. **It is not
zero**, and therefore

```text
    | <psi, ( X_lambda - [(I-P) + phase_lambda·P] ) psi> |  >=  1 - eps_2     for EVERY P,
```

where `eps_2` is any C-L2 certification bound. **THE BETTER C-L2 DOES ITS JOB, THE SMALLER `eps_2`,
AND THE LARGER THE GUARANTEED C-L1 RESIDUAL.** Rescuing C-L1 would require the commutator to *cancel*
the geometric dephasing exactly; C-L2 offers a *bound*, and no bound is a cancellation.

```text
=> SPEC_V002:1166 "LIKELY FAILURE MODE: C-L2" IS MIS-SITED. The failure is UPSTREAM of C-L2 and
   INDEPENDENT of it — it survives at h_0 = 0, where C-L2's object vanishes identically and C-L1
   must therefore hold EXACTLY.
=> SPEC_V002:1137-1138 "C-L2 — THE WHOLE CONTENT OF THIS ROUTE" IS FALSIFIED in the direction that
   matters: there is content in C-L1 that C-L2 cannot reach and cannot repair.
NO QUADRATIC FORM WAS SELECTED FOR C-L2 AND NO COMMUTATOR WAS ESTIMATED. C-L2 WAS NOT ENTERED.
```

**AND IT SURVIVES EVERYTHING ELSE:** at `Q = I` (no compression at all); at every finite Hermite
carrier (where `M(t)` provably has **no eigenvalue 1**, by real-analyticity of finite Hermite spans —
the same shape as the measured `C_mix` spectrum `[0.0391, 0.9609]`, strictly inside `(0,1)`); and
under **both** sealed envelope branches — under ER-B the centre phase is **24 radians, not pi**, so
the premise fails even at `rho = 0`.

---

## §5 — STEP 1: C-L2's SCOPE

```text
CHOOSING THE QUADRATIC FORM IS A LANE ACT, with a mandatory disclosure duty — CONFIRMED.
C-L2 is NOT the MISSING_SPEC pattern that killed six obligations this week: the corpus does not
name an undefined object, it ASSIGNS a choice to the artifact and requires it to state which form
and why the operator-norm route is excluded. Bounded negative: no fence (F'-1..F'-17, the Q2 scope
limit, the verb calibration) reserves norm or form choices to the principal.
```

---

## §6 — WHAT C-L1 SUPPLIES TO C-L4/R-L4 — **REQUIRED EITHER WAY, AND ANSWERED**

`SPEC_V002:1159`: "C-L4 = R-L4/R-L4a/R-L4b, owned here because C-L1 supplies their input." **C-L1 is
the SOLE supplier of R.2's pair structure**, via the single line `:746`:
`V_{mu lambda}(0) - 1 = (phase_mu·phase_lambda - 1) P`.

**THE SUPPLY IS WITHDRAWN, AND AN EXACT REPLACEMENT IS HANDED BACK.** With `n := (lambda-mu)/sqrt2`:

```text
    *** V_{mu lambda}(0) = (-1)^n [ cos(n theta) I + i sin(n theta) S ] on rho <= 1/2 ;  = I beyond ***
    (verified to 3e-16 across all nine (mu,lambda) pairs at five radii)
```

```text
(1) THE "SURVIVING SECTOR" IS NOT SURVIVING. For the same-phase pair (+sqrt2,-sqrt2), n = ±2 and
    ||V(0) - I|| reaches 2 — the maximum possible for unitaries — and exceeds 1 on 61.1% of the
    causal ball by volume. So ":754 SAME-PHASE (SURVIVING) SECTOR: V(0) = I exactly" IS FALSE, and
    "det(1+A(0)) = 1" FAILS WITH THE C-L2 COMMUTATOR SET TO ZERO. R.0:668 makes the Carleman
    machinery "VALID ONLY ON THE SURVIVING SECTOR … where det(1+A(0)) != 0" — that sector's
    defining property is withdrawn.
(2) THE TWO-SECTOR PARTITION IS NOT A PARTITION. V depends on n, not on phase_mu·phase_lambda:
    THREE classes (n = 0, ±1, ±2), with n = 0 and n = ±2 both "same-phase" and behaving completely
    differently. The weight bookkeeping at :749-752, and hence kappa_bal = 1, is computed over a
    partition that does not exist. *** NO REPLACEMENT VALUE FOR kappa_bal IS SUPPLIED — that is
    C-L4's owner's, and supplying one would widen beyond C-L1. Only the withdrawal is reported. ***
(3) R-L4b's TARGET IS REPLACED EXACTLY: -2 cos(8 pi rho^4) exp(± i 8 pi rho^4 S) 1_{|x| <= 1/2}, in
    place of -2P — a CONTINUOUS profile falling to zero at the causal boundary, plus an S-ODD factor
    with no P-multiple representation at all.
(4) BUT R-L4a's CONCLUSION IS PROBABLY UNHARMED, AND IT IS RECORDED BECAUSE IT CUTS AGAINST THIS
    RESULT. C6:365-368 states the fatal integral is the VOLUME DIAGONAL, not the sharp boundary.
    The replacement softens only the BOUNDARY, so tr A = -infinity and R-L4a's "D IS UNDEFINED,
    NOT D = 0" should survive with a corrected display. *** NOT CERTIFIED HERE; flagged, not
    performed. ***
```

---

## §7 — HYPOTHESES, AND A CORRECTION TO THIS LANE'S OWN RECENT SEAL

```text
H-IP        ADOPTED, DISCLOSED, NOT VALUED. u_lambda is read in the interaction picture. Adopted
            because it is GENEROUS to C-L1 — without it C-L1 fails at lambda = 0 by inspection.
            The refutation is unconditional under it.
H-BALL-NONEMPTY   NAMED AND REFUTED. Empty at every finite carrier; a single point at Q = I.
H-BALL-CHOICE     NAMED AND REFUTED. Step 10 quantifies over EVERY orthogonal projector.
H-CONTINUUM-CARRIER  NAMED, NOT ADOPTED, FLAGGED AS THE PRINCIPAL'S. It contradicts finite Q as
            D6':465 displays it, and it does NOT save C-L1 in any case — the sqrt(2)/1 constants
            are computed AT Q = I.
NO CLUSTERING AXIOM. F'-1 UNTRIGGERED. H-B, H-B0, H-R, H-Z0 untouched.
```

**CORRECTION TO `STAGE8_T7II_ATTEMPT_RESULT_OBSTRUCTION_NAMED_V001.md:96-102` (`0f76ab73…`), sealed
by this lane earlier today:** it consumed C-L1 *conditionally* to conclude the zero-history in-cell
Kraus operator is the odd-parity projector `Pi_odd`, **"AN IDEMPOTENT."** The derived object is
`cos^2(8 pi rho^4)·I`, **which is not idempotent.** The T7(ii) obstruction there does not depend on
idempotence — it depends on degeneracy of the leading mode, which a smooth radial multiplier also
has — so **that return's conclusion stands and its supporting clause is corrected.**

## §8 — FLAGS

```text
record_phase_operator_collapse_certified = false, STRENGTHENED FROM "UNCERTIFIED" TO REFUTED
CL1_false_as_written                     = true      # at Q = I, at every finite Q, both envelopes
CL1_reduces_to_CL2                       = false     # THEY CANNOT BOTH BE SATISFIED
CL2_choice_is_lane_act                   = true
C4_operator_level_clause                 = FALSE     # frozen input; new exact witness supplied
C4_scalar_clauses                        = UNTOUCHED
witness_08b91543_supports_CL1            = PARTIAL   # the SCALAR PHASE ONLY; zero mention of a ball
M_has_eigenvalue_one                     = false     # proved; C_mix spectrum corroborates
RL4_pair_structure_input                 = WITHDRAWN_AND_REPLACED
kappa_bal_replacement_value              = NOT_SUPPLIED   # C-L4's owner's, not this lane's
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

## §9 — INVENTION CHECK

```text
THIS IS A RESULT, NOT A DETERMINATION. The proof was attempted in the most generous admissible
reading (H-IP), carried to an exact identity, and THE NEGATION WAS PROVED with a choice-free
constant. The error term was DERIVED, not posited.
VERIFIED BY THIS LANE INDEPENDENTLY OF THE WORKFLOW: f(rho) = tau_R(1-16 rho^4) re-derived by hand
from D6' and checked against direct quadrature at five radii; sum_lambda w_lambda R_lambda =
cos^2(8 pi rho^4) I checked to 12 digits at four radii; D6':465-466 and C4:350-351 read verbatim.
C-L3 NOT REACHED — read only far enough to confirm C-L1 is upstream of it, then stopped. No log
coefficient, no multiple of 2/pi, no decimal, nothing NC7-adjacent. kappa_record and alpha untouched;
kappa_bal is R-L4's baseline balance ratio and is NOT kappa_record.
D6' HONOURED: M(t) and 1_{D_t} used exactly as sealed. THE RESULT IS A CONSEQUENCE OF THE SHARPNESS
AND THE t-DEPENDENCE, NOT OF SOFTENING EITHER.
CARRIER-INDEXED NUMBERS (sup-eig M(t), C_mix spectrum) ARE F'-5 INADMISSIBLE AND ARE USED
REFUTATIONALLY ONLY — to decide negative existentials, which a measurement may do. They bind no
constant. The load-bearing constants sqrt(2), 1, 2^{-5/4}, 0.4054 are ABSOLUTE PURE NUMBERS,
independent of the frozen tuple, hence F'-5 clean a fortiori.
ONE CLAIM CUTTING AGAINST THIS RESULT IS RECORDED RATHER THAN OMITTED: R-L4a's conclusion probably
survives (§6(4)).
CORPUS READ-ONLY; all computation in the session scratchpad. kappa naming observed throughout.
```
