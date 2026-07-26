# Is There a Ward-Type Identity at the Diagonal? — BLIND ANSWER V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY. Answered BLIND; the independent lane's answer not seen.
*** ANSWER: THE IDENTITY EXISTS, IT IS SEALED AS C4, IT IS EXACTLY THE SHAPE
THE QUESTION HYPOTHESISED — AND IT DOES NOT ANSWER THE QUESTION, FOR TWO
INDEPENDENT REASONS. THE CORPUS ALREADY RECORDED THE NEGATIVE CONCLUSION
BEFORE THE QUESTION WAS ASKED. ***
R-L2b: no bound, alpha not derived, p unknown. kappa_record/kappa_Thomson
rule observed. PRODUCTION PROHIBITED. alpha_computed = false.
proof_authorized = false.
```

## §0 — Prediction, recorded honestly rather than dressed up

```text
This lane's prior, frozen before searching: "five mechanisms failing at
exactly p = 1 has the shape of a hidden symmetry — BUT the pattern could
equally mean that p = 1 is simply the answer and R-L2b fails." A HEDGE, not
a prediction, and it is recorded as a hedge. No credit is claimable either
way, and the temptation the question warned about was live: an identity here
would rescue the campaign.
```

## §1 — Q1: THE COINCIDENCE EXPANSION, AND WHAT WOULD HAVE TO ANNIHILATE IT

```text
Finiteness of || C X C ||_2 with X = V_(mu lambda)(a) - V_(mu lambda)(0)
requires, from the sealed kernel |C_off| = 1/(2 pi^2 |r|^3):
    int_{|r|<1} d^3 r |C(r)|^2 |X(r)|^2 < infinity ,  |C|^2 ~ r^-6 .
If X vanishes at coincidence like |r|^p then 4 pi int r^(2p-4) dr converges
IFF p > 3/2. Since jets come in integer orders, THE FULL FIRST JET OF X MUST
VANISH IDENTICALLY AT COINCIDENCE (p = 2) — no smoothing mechanism supplies
that; only an identity can.
SO WHAT MUST BE ANNIHILATED IS THE ORDER-0 AND ORDER-1 TERMS OF X's
COINCIDENCE (r) EXPANSION.
```

## §2 — Q2: THE IDENTITY EXISTS. IT IS C4, AND IT IS SEALED.

Full credit where due: it is exactly the shape the question hypothesised.

```text
C4, VERBATIM (reclassification corrections 6c3e125b..., lines 48-56):
  "THE POINTER WEIGHTS: TWO MOMENTS VANISH, AND THE CANCELLATION IS
   EXACTLY SATURATED AT FULL tau_R.
   m0 = m1 = 0 exactly; the completed Kraus operator IS the symmetric
   second difference -(1/4)[f(+sqrt2) - 2 f(0) + f(-sqrt2)]; ALL DYSON
   TERMS WITH FEWER THAN TWO RECORD INSERTIONS PER CTP BRANCH ARE
   ANNIHILATED, and the bare a-linear tadpole vanishes identically
   (also killed independently by the odd spinor trace -2 p-hat_x).
   BUT at full tau_R the record phases are exactly (+1,-1,-1)
   (lambda·tau_R in {0, +-pi}), so sum_lambda w_lambda·phase_lambda = 1"
VERIFIED INDEPENDENTLY HERE, exact:
    m_0 = 0, m_1 = 0, m_2 = -1, m_3 = 0, m_4 = -2, m_5 = 0
    matching the sealed m_(2j) = -2^(j-1) at j = 1,2,3.
    AND the phase sum: sum_lambda w_lambda e^(-i lambda tau_R) = 1.000000
    exactly, with sum |w_lambda| = 1.000000 — MAXIMAL SATURATION.
BOTH FACTS ARE CHECKED BY THE SAME SEALED SCRIPT: the E1 v001 verify.py row
lists "m_0=m_1=0, m_{2j}=-2^{j-1}, all odd moments zero (exact Q(sqrt2))"
AND "the tau_R phase saturation sum w_lambda phase_lambda = sum |w_lambda|
= 1" side by side. The corpus knew both halves at once.
```

## §3 — WHY IT DOES NOT ANSWER THE QUESTION. TWO INDEPENDENT REASONS.

### Reason 1 — WRONG GRADING. And this is the trap.

```text
C4 annihilates "ALL DYSON TERMS WITH FEWER THAN TWO RECORD INSERTIONS PER
CTP BRANCH". That is an order in the RECORD-INSERTION grading.
p is an order in the COINCIDENCE grading — powers of |r| = |x - y|.
*** THESE ARE DIFFERENT GRADINGS AND THE ANNIHILATION DOES NOT CONVERT. ***
The pointer weights are a second difference IN lambda, so m_0 = m_1 = 0
annihilates polynomials in LAMBDA of degree <= 1. Nothing in that statement
constrains the r-dependence of what survives.
*** NAMED AS THE TRAP IT IS: reading "two moments vanish" as "p = 2" IS A
GRADING CONFUSION, AND IT IS THE SAME CLASS OF ERROR THIS LANE COMMITTED
THIS MORNING when it imported the O7 tau_R obstruction across a typing
boundary from the activity to the normalized response. Fifth instance of the
family this program has now recorded (universal-vs-represented,
operator-vs-scalar, object-vs-bound, formula-vs-response-naturality, and now
insertion-grading-vs-coincidence-grading). The proved object is real and
graded differently from the label one wants. ***
```

### Reason 2 — SATURATED ANYWAY, and the corpus says so in as many words

```text
Even setting the grading aside, the mechanism is spent at the relevant point.
At FULL tau_R the record phases are exactly (+1, -1, -1), so
    sum_lambda w_lambda · phase_lambda  =  1  =  sum_lambda |w_lambda| .
That is not weak cancellation. IT IS MAXIMAL SATURATION — the weighted sum
attains its own absolute-value bound, so there is no cancellation left to
extract.
AND THE CORPUS DRAWS THE CONCLUSION EXPLICITLY, in E1 v001's PA-C3:
  "the degree-(-3) kernel's absolute integral is logarithmic with derived
   coefficient exactly 2/pi at BOTH ends, and NOTHING IN THE SEALED
   STRUCTURE SUPPLIES A CANCELLATION AT THE UV END — C4 SHOWS THE ONE
   CANDIDATE CANCELLATION IS EXACTLY SATURATED."
*** THE UV END IS THE COINCIDENCE LIMIT. THE CORPUS ALREADY ANSWERED THIS
QUESTION, IN THE NEGATIVE, AND RECORDED IT AS A GROUND FOR A FROZEN
PREDICTION. ***
```

### The other candidates, checked not assumed

```text
ODD SPINOR TRACE tr_spinor[C(p) alpha_x] = -2 p-hat_x — VERIFIED correct
  here: C(p) = (1 - alpha·p-hat)/2, tr[alpha_x] = 0, tr[alpha_j alpha_x] =
  4 delta_jx, giving -2 p-hat_x exactly. IT CANNOT SERVE THIS OBJECT:
  ||X||_2^2 = tr[X* X] is the trace of a POSITIVE operator, and oddness
  cannot annihilate a positive quadratic form. This is the same reason HS
  volume scaling failed — |C_off|^2 is even and positive. C4 itself uses the
  odd trace only for the a-LINEAR TADPOLE, a trace-level object.
CTP DOUBLING — the "CTP double-moment table" is checked by the same sealed
  verify.py row; it supplies the per-branch insertion counting C4 uses, i.e.
  more of Reason 1's grading, not coincidence order.
L4 ANTIUNITARY REALITY CLASS — its content is sym(Psi) = 0 with
  ||antisym(Psi)||_F = 6.8e-2 NONZERO. A reality-class statement, not a
  coincidence-order statement, and its antisymmetric part does not vanish.
LAMBDA-PARITY AND a-PARITY LEMMAS — parity gives ODDNESS, hence at most ONE
  order, and oddness does not survive squaring into an HS norm. Same wall as
  the odd trace.
NONE OF THE FIVE SUPPLIES TWO ORDERS IN THE COINCIDENCE VARIABLE.
```

## §4 — Q3: HOW MUCH p? ZERO, IN THE COINCIDENCE GRADING.

```text
C4 gives TWO ORDERS IN THE RECORD-INSERTION GRADING and, being saturated at
full tau_R, gives NOTHING at the UV end. In the coincidence grading it
supplies p = 0.
BEING QUANTITATIVE AS ASKED: the threshold is p > 3/2. The identity supplies
0. The five closed mechanisms supply at most 1. THE SHORTFALL IS NOT
CLOSED AND IS NOT NARROWED BY THIS ANSWER.
```

## §5 — Q4: WOULD SUPPLYING ONE BE A DERIVATION OR A NEW PRINCIPLE?

```text
*** A NEW PRINCIPLE. And the reason is stronger than "the corpus is silent".
THE CORPUS'S ONE CANDIDATE IS NOT ABSENT — IT IS MEASURED AND REFUTED.
C4 computed the candidate cancellation and found it EXACTLY SATURATED
(sum w·phase = sum |w| = 1, exact in Q(sqrt2)). A mechanism whose sole
candidate has been measured at maximal saturation cannot be recovered by
derivation from existing authorities; something not currently in the
structure would have to be posited. ***
AND ONE BRANCH IS ADDITIONALLY FORECLOSED: the saturation holds AT FULL
tau_R. Weakening tau_R below full would break it — but "every cell runs at
FULL tau_R" is sealed D2, and no small-record-coupling hypothesis exists
anywhere in the spec. So the obvious escape (make the record coupling small)
is not available without contradicting sealed text.
```

## §6 — CONSEQUENCE, stated plainly

```text
THIS CLOSES THE LAST PHYSICS CANDIDATE FOR R-L2b AS POSED. Six mechanisms
are now closed: commutator algebra, the HS ideal bound, HS volume scaling,
time integration, Q support structure, and now the Ward/pointer-weight
identity — the last one closed not by this lane's analysis but by the
corpus's own C4 measurement, which predates the question.
WHAT THIS DOES NOT SAY: it does NOT say p <= 3/2. It says NO IDENTIFIED
MECHANISM SUPPLIES p > 3/2, and that the one symmetry candidate is measured
saturated. The difference kernel's actual p REMAINS UNKNOWN — object-vs-bound
discipline: this is a statement about the available mechanisms, NOT about the
object.
WHAT FOLLOWS IS THE PRINCIPAL'S: R-L2b as posed has no remaining identified
route, so either the object changes or the campaign does. This lane adopts
nothing and proposes nothing here.
ONE OBSERVATION OFFERED, NOT A PROPOSAL: C4's saturation is exact AT FULL
tau_R because the phases land exactly on {0, +-pi}. That exactness is a
consequence of tau_R = pi/sqrt2 and lambda in {0, +-sqrt2} — i.e. of the
pinned record spectrum. It is the kind of coincidence that is either
structural or an artifact of the pinning, and this lane has not determined
which. Recorded because it is the only place the saturation could conceivably
be soft.
```

## Protected status

```text
identity_exists = true            (C4, sealed)
identity_answers_the_question = false
reasons_it_does_not = 2 (independent)
reason_1 = wrong grading: record-insertion order, not coincidence order
reason_2 = exactly saturated at full tau_R (sum w.phase = sum|w| = 1, exact)
corpus_already_recorded_the_negative = true (PA-C3, before the question)
p_supplied_by_the_identity = 0
threshold = p > 3/2
grading_confusion_named_as_5th_instance_of_the_family = true
odd_spinor_trace_verified = true; cannot serve a positive quadratic form
CTP_doubling = supplies insertion grading, not coincidence order
L4_reality_class = antisym part NONZERO (6.8e-2); not a coincidence statement
parity_lemmas = one order at most; does not survive squaring
supplying_an_identity = NEW_PRINCIPLE (sole candidate MEASURED and REFUTED)
small_record_coupling_escape = FORECLOSED by sealed D2
mechanisms_now_closed = 6
p_of_the_actual_object = UNKNOWN   (object-vs-bound discipline)
R_L2b_closed = false
campaign_has_no_remaining_identified_route = true
next_step_is_the_principal_s = true
production_authorized = false
alpha_computed = false
proof_authorized = false
```
