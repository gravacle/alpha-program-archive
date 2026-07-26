# R-L2b: Is the Chartered Decomposition the Right Frame? — Answer, and the Campaign's Target V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY. Answers the principal's question before the campaign's shape is
committed. Cites: transport charter f58007a0f982343e...; extensivity verdict
and campaign opening 0f3082cab910f2eb...
kappa_record / kappa_Thomson rule observed. R-L2b REMAINS OPEN — no bound is
claimed and no exponent is derived. PRODUCTION PROHIBITED.
alpha_computed = false. proof_authorized = false.
```

## §1 — THE ANSWER IN ONE LINE

```text
THE DECOMPOSITION IS IRRELEVANT TO THE FINITENESS AND DECISIVE FOR THE
AGGREGATION. So it is the right frame — but for a different reason than the
charter was argued on, and the "relocation of anisotropy into the
combinatorics" is NOT harmless: IT IS EXACTLY WHERE THE CONSTRAINT BITES,
AND THAT IS PRODUCTIVE, because it converts a vague uniformity demand into a
sharp exponent requirement.
```

## §2 — WHY THE DECOMPOSITION CANNOT AFFECT FINITENESS

```text
The divergence established in the campaign's opening is a SHORT-DISTANCE
divergence: |C_off| = 1/(2 pi^2 |r|^3), so the pair integrand goes as
|r|^-6 and int d^3 r |r|^-6 diverges as r -> 0, at rate eps^-3.
*** r -> 0 IS INTERNAL TO WHATEVER DIAMOND ONE IS IN. *** The cancellation
that renders the object finite is therefore a UV phenomenon occurring BELOW
the diamond scale. The decomposition, by contrast, is a partition of the IR
structure — it says how an atom is cut into diamonds, which is a statement
about scales AT AND ABOVE the diamond size.
THEY LIVE AT OPPOSITE ENDS OF THE SCALE. So how the atom was cut up cannot
affect WHETHER the object is finite.
*** THE PRINCIPAL'S INTUITION IS CORRECT ON THIS HALF: the cancellation rate
does not care how the atom was cut up. ***
```

## §3 — WHY IT IS NEVERTHELESS DECISIVE, AND WHAT IT DECIDES

```text
The per-diamond bound aggregates. With N diamonds of 4-volume V/N each,
    sum_i |D_i|_4^alpha  =  N^(1-alpha) * V^alpha .
D5 requires the total activity to be proportional to |C|_4 — i.e. requires
    (V/N)^(alpha-1) bounded as N -> infinity at fixed V ,
which holds iff  *** alpha >= 1 ***  (=1 flat; >1 shrinking; <1 divergent).
COMPUTED, and this is the sliver failure derived rather than observed —
a sliver of aspect ratio A needs N ~ A^3 diamonds, so the aggregate grows as
A^(3(1-alpha)):
    alpha = 1/2   ->  A^1.50   ->  x31.6 at A=10,  x1000 at A=100
    alpha = 3/4   ->  A^0.75   ->  x5.6  at A=10,  x31.6 at A=100
    alpha = 1     ->  A^0      ->  x1    at every A
*** SO THE INDEPENDENT LANE'S REPORTED SLIVER FAILURE OF THE BOUND CLASS IS
NOT A SEPARATE FACT. IT IS WHAT alpha < 1 LOOKS LIKE UNDER AGGREGATION, AND
ITS RATE IS PREDICTED: A^(3(1-alpha)). ***
```

## §4 — AND alpha >= 1 IS EQUIVALENT TO COMPLETE CANCELLATION

```text
POWER COUNTING. The HS norm is over the one-particle (spatial) space:
    ||X||_2^2 = int int d^3x d^3y |X(x,y)|^2 .
IF THE DIFFERENCE KERNEL IS BOUNDED by M on the diamond, then
    ||X||_2  <=  M * |D|_3     (spatial 3-volume).
The a-insertion carries a TIME INTEGRAL across the diamond's extent, giving
one further power of the temporal extent L — this is A-L4's own mechanism,
"in-cell strength <= eps ||b_D||_inf x (cell time extent)".
For an ISOTROPIC diamond |D|_3 ~ L^3 and |D|_4 ~ L^4, so
    || C (V(a) - V(0)) C ||_2  <~  M * L * L^3  =  M * L^4  =  M * |D|_4
*** alpha = 1 IF AND ONLY IF THE DEGREE -3 SINGULARITY FULLY CANCELS IN THE
DIFFERENCE. ***
AND IT EXPLAINS v001's WITHDRAWN VALUE STRUCTURALLY: alpha = 1/2 would
require the pair integral to scale as |D|_4^(1/2) = L^2 — AN AREA. An area
law is the signature of a bound drawn from the SUPPORT (a boundary), not
from cancellation. That is precisely why C-13 struck it and why R-L2b was
told to DERIVE the exponent rather than assume 1/2.
DISCLOSURE, REQUIRED: the time-integral step reuses A-L4's strength
mechanism, and A-L4 is sealed ONLY for the two-line sector on family A. The
reuse is more defensible here than on a general atom, because UNDER THE
CHARTER EVERY DIAMOND IS ISOTROPIC and therefore family-A-like in the only
respect the mechanism uses. IT IS STILL A REUSE OUTSIDE ITS SEALED SCOPE and
is labelled as such: §4 is POWER COUNTING, NOT A DERIVATION, and it does not
discharge R-L2b.
```

## §5 — SO WHY THE CHARTER IS STILL THE RIGHT FRAME

```text
NOT for the reason the charter was argued on. The charter was adopted partly
because it "relocates the anisotropy into the combinatorics"; that
relocation turns out to be irrelevant to finiteness (§2). The charter is
right for two OTHER reasons, both load-bearing:
 1. IT MAKES alpha WELL-DEFINED AT ALL. A diamond is ISOTROPIC with ONE
    parameter, so the cancellation rate is a function of a single scale
    rather than of a shape. On a general anisotropic atom "the exponent"
    would not be a number — there would be no single scale for it to be an
    exponent OF. The charter is what makes R-L2b a question about a number.
 2. IT MAKES THE AGGREGATION REQUIREMENT EXPLICIT AND SHARP. Without a
    decomposition, D5-uniformity is a demand quantified over an infinite
    family of atoms. With one, it is alpha >= 1. A demand became an
    inequality on a single exponent.
SO THE RELOCATION IS NEITHER HARMLESS NOR THE WRONG VARIABLE — IT IS THE
PLACE THE CONSTRAINT LIVES, AND MOVING IT THERE IS WHAT MADE THE CONSTRAINT
STATEABLE.
```

## §6 — THE CAMPAIGN'S TARGET, now a single analytic question

```text
BEFORE: "certify a Schatten-2 bound uniformly over the unrestricted D3
quantifier, with alpha derived" — a uniformity demand over an infinite
family of atoms of unbounded aspect ratio.
NOW:
  *** DOES  V_(mu lambda)(a) - V_(mu lambda)(0)  HAVE A BOUNDED KERNEL ON A
  DIAMOND — I.E. DOES THE DEGREE -3 SINGULARITY OF C FULLY CANCEL IN THE
  DIFFERENCE? ***
    FULLY CANCELS  -> alpha = 1 -> aggregation FLAT in aspect ratio -> D5's
      action-density form satisfied -> the sliver problem DISSOLVES, and with
      it (per the campaign charter) T11's response half, the D3 weight's
      response side, and CONNECTED EXTENSIVITY.
    PARTIALLY CANCELS -> alpha < 1 -> aggregate divergence at the PREDICTED
      rate A^(3(1-alpha)) -> D5 fails, and the failure is quantitative and
      checkable rather than diffuse.
ONE YES/NO ANALYTIC QUESTION ABOUT A SINGLE ISOTROPIC OBJECT, REPLACING A
UNIFORMITY DEMAND OVER AN INFINITE FAMILY. That is the campaign's shape, and
it is committed on this answer.
NEXT STEP NAMED so it is not rediscovered: attack the cancellation via the
commutator route already opened — the corpus's worked identity
||[C,P]||_2^2 = 2 sum_i sigma_i (1 - sigma_i) shows commutators with C ARE
Hilbert-Schmidt in this program's own cases, so the target is to exhibit
C(V(a)-V(0))C in commutator form and read the cancellation off it.
STILL OPEN, STATED PLAINLY: no bound is claimed, alpha is not derived, and
whether the singularity fully cancels is UNKNOWN. §3-§4 are power counting
and aggregation arithmetic; they say what alpha must be for D5 to hold and
what it costs if it is not. They do not say what alpha is.
```

## Protected status

```text
decomposition_affects_finiteness = false      (UV, intra-diamond)
decomposition_affects_aggregation = true      (decisive)
principal_intuition_on_finiteness = CORRECT
relocation_of_anisotropy = neither_harmless_nor_wrong_variable; it_is_where
                           the_constraint_lives
D5_requires = alpha >= 1
sliver_growth_rate_if_alpha_lt_1 = A^(3(1-alpha))   (derived, not observed)
alpha_eq_1_iff = degree_minus_3_singularity_fully_cancels_in_the_difference
alpha_half_would_require = an_AREA_law -> support-drawn, not cancellation
                           -> why C-13 struck it
charter_right_frame_because = alpha_is_well_defined_only_on_an_isotropic
                              one_parameter_object; and_aggregation_becomes
                              a_single_inequality
A_L4_mechanism_reused_outside_sealed_scope = true (DISCLOSED; §4 is power
                                              counting, not a derivation)
campaign_target = does_the_difference_kernel_bound_on_a_diamond
campaign_shape_committed = true
R_L2b_closed = false
alpha_derived = false
production_authorized = false
alpha_computed = false
proof_authorized = false
```
