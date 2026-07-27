# X to kappa_record: Extraction Determination V001

Date: 2026-07-27

## Status — the answer in one line

```text
THE DIRECT EXTRACTION FROM X = C(V(a)-V(0))C TO kappa_record IS ABSENT — X IS NOT THE
AMPLITUDE CHAIN'S INPUT AT ALL. BUT X IS NOT OFF THE PATH: IT IS THE SEALED S2 OBJECT
G_hs, AND THE NORMALIZATION IS THE REASON IT IS THERE.

SO THE PRINCIPAL'S HYPOTHESIS (b) SPLITS: the amplitude IS a normalized ratio, CONFIRMED
in five sealed spellings; but the corollary — that the ratio makes Hilbert-Schmidt
behaviour IRRELEVANT to kappa_record — IS DENIED BY SEALED TEXT. The ratio does not
cancel the HS question. It RELOCATES it from the baseline operator to the a-difference
operator, and the a-difference operator IS X.

NO BRIDGE WAS CONSTRUCTED. The principal's prohibition was the governing constraint of
this investigation and it was not breached; §8 records the check.
PRODUCTION PROHIBITED. alpha_computed = false. proof_authorized = false.
kappa_record_computed = false.
```

## 1. THE CHAIN, TRACED BACKWARDS FROM THE DOWNSTREAM END

Per instruction (a). Each link with its sealed status.

```text
LINK 4 — "MAXWELL SCALAR".  NO OBJECT OF THAT NAME EXISTS.
  Bounded search: the exact phrase "Maxwell scalar" returns ZERO hits over --include="*.md"
  corpus-wide. The terminal object is a TEST, not an extraction:
  V011:1565-1579 QUOTED — "Only the predeclared exact test [M_record,J_star]=0 may yield
    kappa_record,E = kappa_record,B = kappa_record >= 0."
  AND ITS OWN CEILING, V011:1583-1585 QUOTED — "Passing this test establishes Maxwell-form
    kinematics for the primitive response; it does not yet identify `kappa_record` with the
    physical electromagnetic action coefficient."
  => the far end of the path certifies Maxwell FORM, not a Maxwell COEFFICIENT.

LINK 3 — LOCAL TENSOR <- INTENSIVE HESSIAN.  DEFINED as a constructive recipe.
  V011:1351-1352 QUOTED — "mathcal_K_L(xi,zeta) = R_record,L(Q_flux xi, Q_flux zeta)".
  V011:1525-1531 QUOTED — rank-20 Hermitian system, exact Frobenius section, "M_record =
    lim_(odd L->infinity) M_L".
  V011:1549 QUOTED — "This stage yields a primitive record tensor, not yet the Thomson response."

LINK 2 — INTENSIVE HESSIAN <- NORMALIZED AMPLITUDE.  PARTLY DEFINED; ITS CONNECTED
  INGREDIENT IS ASSERTED, NOT DERIVED, AND IS RECORDED BLOCKED.
  V011:1292-1300 QUOTED — "R_record,L(a,b) = d^2/ds dt [Gamma_K(sa+tb)/N_4(K)]|_(s=t=0),
    evaluated after the thermodynamic/linked-cluster limit. The Duhamel covariance computed
    from `G_L` must reproduce this Hessian."
  V011:1280-1281 QUOTED — "The disjoint theorem is proved; the connected thermodynamic limit
    remains a Gate-5 obligation."
  RESPONSE GATE:55-59 — T7(ii) BLOCKED, T7(iii)-connected BLOCKED, T7(iv) NOT EXECUTABLE,
    ":23-24 Consequently no intensive connected Hessian exists yet against which the local
    Duhamel covariance can be checked."

LINK 1 — THE NORMALIZED-AMPLITUDE STEP.  *** ITS INPUT IS NOT X. ***
  MAJORANT SPEC:93 QUOTED —  K_pointer^(c)(a) = sum_lambda w_lambda Gamma(u_lambda^(c)(a));
  MAJORANT SPEC:116-117 QUOTED —
      Z_hat_comp(a) := Z_comp(a) / Z_comp(0),
      Z_comp(a)     := omega_in( K_pointer^(K)(a_-)^dagger K_pointer^(K)(a_+) )
  ULTIMATE INPUTS: the one-particle propagators u_lambda(a), the pointer weights w_lambda,
  and THE INCOMING STATE omega_in.
  X IS BUILT FROM THE SAME ONE-PARTICLE PROPAGATORS BUT IS NOT THIS INPUT, AND NO SEALED
  STEP RELATES THE TWO. That relation is the thing the principal asked for, and it is
  ABSENT — see §3 and §5.
```

## 2. INSTRUCTION (b) — NORMALIZED RATIO: CONFIRMED. THE COROLLARY: DENIED.

**Confirmed.** Five sealed spellings of one shape, numerator over the same matrix element of
the same operator between the same states at zero perturbation:
`Z_BR[A,g]`; `A_K(A)`; `Z_hat_comp(a) := Z_comp(a)/Z_comp(0)`; `Z_Q[A]/Z_Q[0]`;
`Z_h(A) = a_h(A)/a_h(0)`. "Normalized by" means the `a=0` baseline, nothing else.

**Two normalizations exist and the corpus keeps them strictly layered, not alternative.**
Inner: the `Z(a)/Z(0)` ratio. Outer: division by `N_4(K)`. One correction to the framing:
the outer normalization is **not a cell count** — D-3 defines `N_4(K) := |X(K)|_4`, the
cellulation 4-volume, and D5 makes a per-cell normalization a spec violation outright.

**And now the load-bearing answer.** The corpus **adopts half** of the principal's hypothesis
and **denies the other half**, both in sealed text:

```text
ADOPTED — the ratio DOES kill the BASELINE divergence, and the corpus acted on exactly that:
  S3 QUOTED — "*** DELETED. *** G_bl (the equal-time baseline HS density) is REMOVED FROM
  THE ARCHITECTURE ... ANY REAPPEARANCE OF G_bl OR OF ANY NORM OF THE BASELINE BLOCKS with
  witness SCAD_BASELINE_NORMED."
  That is the principal's intuition, already sealed, already acted on.

DENIED — the replacement constant IS STILL A HILBERT-SCHMIDT NORM, AND ITS OPERATOR IS X:
  S2 QUOTED — "G_hs(C, eps) := |C|_4^{-alpha} · || C(V(a) - V(0))C ||_2
               [SUBTRACTED HILBERT-SCHMIDT DENSITY ... *** THE EXPONENT alpha IS NOT
               ASSERTED. ***]"
  It feeds the per-cell majorant  g(C,eps) = G_tr + rho_res·G_hs·(G_cm + G_hs),
  and R-L2b IS the derivation of alpha, open, witness SCAD_HS_SCALING_EXPONENT_UNDERIVED.

AND THE CANCELLATION QUESTION IN THE a-DIFFERENCE IS EXPLICITLY OPEN, NOT SETTLED:
  QUOTED — "whether the singularity fully cancels is UNKNOWN."

AND THE OBVIOUS ESCAPE IS SEALED SHUT:
  QUOTED, of the corpus's own proposed bypass (define the intensive Hessian directly as the
  second-order Duhamel term) — "where the connected cross term (A-L0 arm 2) reappears at
  n = 2, and where R-L2b is consumed."
```

**Therefore: `‖C(V(a) − V(0))C‖₂` appears VERBATIM in the sealed definition of `G_hs`.**
X is the S2 operator. The normalization is precisely *why* X is the object that matters:
it deleted the baseline norm and left the subtracted one.

## 3. WHAT THIS MEANS FOR THE HELD RULING — THE HOLD IS INVERTED

The principal held F'-5 on the reasoning that if the extraction were normalized, then R-L2b,
the p > 3/2 threshold, the symbol-survives identity, the trilemma, U3's two readings and the
Trotter-Kato lemma would all be "statements about a quantity that cancels before it reaches
the target… not wrong, but beside the point."

**That reasoning is sound and its premise fails.** The extraction *is* normalized, and the
normalization is what puts X in the majorant rather than what removes it.

```text
NONE OF THAT WORK IS BESIDE THE POINT. IT IS LOAD-BEARING, AND MORE DIRECTLY THAN BEFORE:
  X            IS the S2 operator inside G_hs
  G_hs         feeds the per-cell majorant g(C,eps)
  g(C,eps)     gates the connected linked-cluster density
  that density IS link 2, and link 2 is on the corpus's own stated chain to kappa_record
  R-L2b        IS the derivation of S2's exponent alpha
F'-5 IS THEREFORE LIVE AND SHOULD BE RULED WHEN THE TROTTER-KATO REFERRAL RETURNS. The
reason for holding it has been checked and does not hold.
```

## 4. A CORRECTION TO MY OWN TRILEMMA — I WAS CARRYING THE WRONG OBJECT

```text
THE F'-5 TRILEMMA ARGUED ABOUT ||X||_2 BARE. THE SEALED OBLIGATION IS ABOUT
      G_hs = |C|_4^{-alpha} · ||X||_2 ,
WITH A PREFACTOR I WAS NOT CARRYING. That prefactor is not cosmetic: a divergent ||X||_2 with
a compensating alpha can still give a finite G_hs as cells shrink. So the trilemma's H1 —
"no uniform M exists" — was stated about an object that is NOT the one R-L2b bounds.
THE TRILEMMA IS NOT WITHDRAWN. Its lemma (P alpha_x P = -n_x P), its refutation of the
finite-rank framing, and its identification of U3 all stand unchanged. What is corrected is
its TARGET: the uniformity question is about |C|_4^{-alpha}||X||_2, not ||X||_2.
THIS IS THE SAME ERROR CLASS AS THE PREVIOUS SEVEN — reasoning about a real object that is
not quite the sealed one. Logged as INSTANCE 8.
AND NOTE WHAT MAKES THE PREFACTOR LEGAL: |C|_4 is a cellulation geometric datum, forbidden by
F'-5 in general and ADMITTED THIS DATE under the E-Q1 Option-3 scoped grant, witness
E1_CELL_4VOLUME_ADMITTED_ONLY_ON_PINNED_SKELETON. So S2 is well-formed ON THE PINNED SKELETON
and may not be claimed over D3.
```

## 5. INSTRUCTION (c) — THE DIRECT EXTRACTION IS ABSENT, AND IT IS WORSE THAN ABSENT

```text
BRIDGE_ABSENT. No artifact defines an extraction, formula, map or derivation taking X to
kappa_record. Searched: "kappa_record" against extract/extraction/bridge/read off/obtained
from/computed from/given by/equals/defined as/formula; and the operator side "C (V(a)",
"C(V(a)", "V(a) - V(0)", "CVC", sandwich, Hilbert-Schmidt, HS norm, trace norm, "Tr(",
Hessian, curvature, stiffness, response operator, CAR operator, operator-to-scalar, scalar
bridge — across *.md, *.json AND *.py, including scripts/ and stage8_execution/. Three
PARTIAL fragments exist that could be mistaken for a bridge; none connects the two ends.
BOUNDED NEGATIVE EXISTENTIAL, not an absolute one.

BOTH FLAGS FALSE EVERYWHERE, ALWAYS, NEVER TRUE:
  actual_finite_parent_operator_to_scalar_bridge_derived = false
  kappa_record_computed = false        (~40 sealed status blocks; no artifact assigns a value)
No artifact states an explicit discharge condition keyed to the first flag's name.

AND THE STEP IS NOT MERELY UNDONE — IT CARRIES A SEALED, INDEPENDENTLY CONFIRMED NO-GO:
  STAGE8_T7_SOURCE_SCALARIZATION_NO_GO_RESULT_V001
    PRIMITIVE_SOURCE_SCALARIZATION_BLOCKED
    INDEPENDENT_SOURCE_SCALARIZATION_BLOCK_CONFIRMED
  "The actual completed-record compression is a non-scalar operator on the source. The only
   normalized complex-linear closure invariant under every finite source-basis change is the
   normalized trace, and no normalized tracial state exists on the infinite source algebra.
   Smaller covariance groups leave multiple state functionals rather than selecting one."
  With a numerical witness: distance from scalar identity = 2.151758052952419, and
  "actual-parent non-scalar witness  PASS".
  ITS OWN SCOPE CLAUSE, QUOTED: "This is a scope result. It does not say that no physical
   scalar amplitude exists. It says the scalar requires the physical source/CTP closure of
   complete Q_spec."
  THIS IS WHAT omega_in IS. Link 1 needs a state to turn K_pointer into a scalar, and the
  canonical selection of that state is exactly what the no-go blocks in primitive Stage 8.

AND AT THE FAR END, V011:2077 QUOTED — "the equality kappa_record = kappa_Thomson is assumed
rather than derived." Recorded under the kappa rule: these are two quantities, and the link
between them is an assumption, not a result.
```

## 6. A CONFLICT BETWEEN TWO SEALED AUTHORITIES — reported, not resolved

```text
MASTER PLAN AMENDMENT_001 §D:  "Stage 8 ends ONLY when stage8_battery_evaluator_v001.py emits
  stage8_execution/result.json under schema stage8-gate5-kappa-record-v002", with an
  EXACT-RATIONAL kappa_record enclosure EXCLUDING ZERO.
SOURCE-SCALARIZATION NO-GO's recommended architecture: "primitive Stage 8 ends with the
  derived operator-valued completed-record response and its local Duhamel kernel; the
  physical source/CTP state, scalar amplitude, logarithm, zero-free domain, linked-cluster
  density, and scalar Hessian are derived in complete Q_spec; kappa_record is not emitted
  before that physical scalar closure exists."
THESE CANNOT BOTH HOLD. Either Stage 8 emits kappa_record or it does not.
The no-go's own text says "battery verdict changes."
STATUS OF THE AMENDMENT: authored as STAGE8_T7_OPERATOR_VALUED_PRIMITIVE_RESPONSE_ARCHITECTURE_
AMENDMENT_V001; a search for ACCEPTED / REJECTED / adjudicated markers in it found none, so on
this bounded search IT IS AUTHORED AND NOT MARKED ACCEPTED.
THIS IS THE PRINCIPAL'S. NOT RESOLVED HERE, NOT ACTED ON.
```

## 7. ONE THING FOUND THAT CUTS THE OTHER WAY, recorded because it does

```text
An EXECUTED, PASSING, TWO-LANE numerical Duhamel-versus-Hessian crosscheck exists and was
nearly missed: COMPLETE_QSPEC_FINITE_HOLONOMY_RESPONSE_RESULT_V001, g_Duhamel =
0.06481888687124183 at 3200 RK4 steps, verified by a lane that did not import the primary
script, on the same 8/4/70/9 fixture shape as the T7(iv) F-A leg.
ITS CEILING TRAVELS WITH IT, from its own text: it does NOT establish the intensive
Duhamel-Hessian theorem and does NOT establish kappa_record; its protected status carries
Duhamel_intensive_Hessian_equality_proved = false. And on its own numbers the H_CTP enclosure
is ~2200x wider than the Duhamel enclosure, so the three-way agreement is carried by the
g_FS/g_Duhamel pair, not by H_CTP. A one-coordinate finite diagnostic, not the equality.
RECORDED BECAUSE A NEGATIVE FINDING MUST NOT SUPPRESS THE POSITIVE EVIDENCE NEAR IT.
```

## 8. THE INVENTION CHECK — the constraint that governed this work

```text
The principal's prohibition was: "DO NOT CONSTRUCT A PLAUSIBLE EXTRACTION TO FILL THE GAP."
Every investigating agent was given it verbatim as its overriding rule, and every existence
claim was put to an adversarial verifier instructed to default to REFUTED and to hunt for
smuggled reasoning in connective tissue.
FOUR VERIFIERS REPORTED ON THIS DIRECTLY. Their findings: "NO INVENTED BRIDGE FOUND";
"NO INVENTED PHYSICS BRIDGE FOUND"; "NONE FOUND — no invented bridge, and no imported outside
physics"; and, on the one place a bridge was available (identifying W_h(A;·) with
U_L(A;tau)=exp(-i tau B_L(A))), the agent EXPLICITLY DECLINED and labelled the refusal.
Where verifiers returned WEAKENED it was for under-reporting sealed content or for an
over-broad uniqueness negative — errors in the SAFE direction. Those corrections are carried
above rather than discarded.
THE ONE PLACE THIS LANE SUPPLIED REASONING THE CORPUS DOES NOT CONTAIN: §4's observation that
a compensating alpha could tame a divergent ||X||_2. THAT IS FLAGGED AS AN OBSERVATION ABOUT
WHAT IS UNDETERMINED, NOT A DERIVATION, and it asserts no value or sign for alpha.
```

## 9. WHAT THIS IMPLIES, AND WHAT IS BEGUN

Per the principal's standing instruction to name the next work and begin it:

```text
THE SUCCESSOR QUESTION IS NOW WELL-POSED AND IT IS NOT THE ONE THIS LANE WAS ATTACKING:
      does there exist alpha such that   |C|_4^{-alpha} · ||C(V(a)-V(0))C||_2
      is finite and uniform as cells shrink, ON THE PINNED SKELETON?
This is R-L2b stated with the normalization visible. It is what S2 needs, it is what the
per-cell majorant needs, and it is the exponent the corpus marks NOT ASSERTED.
BEGUN. The prior diagonal-attack lemma and the trilemma feed it directly once re-typed onto
the prefactored object per §4.
TWO ITEMS GO TO THE PRINCIPAL, NEITHER ACTED ON HERE:
  1. The §6 conflict — does Stage 8 emit kappa_record at all?
  2. F'-5 is LIVE, not moot. The premise for holding it has been checked and fails. It should
     be ruled when the Trotter-Kato referral returns.
```

## Protected status

```text
direct_extraction_X_to_kappa_record = ABSENT   (bounded search over .md/.json/.py)
X_is_the_amplitude_chain_input = false
X_is_the_S2_operator_in_G_hs = true            [QUOTED sealed definition]
amplitude_is_a_normalized_ratio = true         (five sealed spellings)
ratio_makes_HS_irrelevant = FALSE — DENIED BY SEALED TEXT
ratio_deletes_the_BASELINE_HS_object = true    (S3, G_bl deleted, witness SCAD_BASELINE_NORMED)
ratio_RELOCATES_HS_to_the_a_difference = true  (S2, witness SCAD_HS_SCALING_EXPONENT_UNDERIVED)
a_difference_cancellation = UNKNOWN in sealed text
F5_is_moot = false — THE HOLD'S PREMISE FAILS; F'-5 IS LIVE
source_scalarization = BLOCKED, independently confirmed, non-scalar witness PASS
omega_in_canonically_selectable_in_primitive_stage8 = false
kappa_record_equals_kappa_Thomson = ASSUMED_NOT_DERIVED  (V011:2077)
actual_finite_parent_operator_to_scalar_bridge_derived = false
kappa_record_computed = false
sealed_authority_conflict = MASTER_PLAN_AMENDMENT_001_SECTION_D vs SOURCE_SCALARIZATION_NO_GO
conflict_resolved = false                      (the principal's)
bridge_constructed_by_this_lane = NONE
own_error_logged = INSTANCE_8 (trilemma targeted ||X||_2, not |C|_4^{-alpha}||X||_2)
trilemma_withdrawn = false                     (lemma and U3 identification stand; target re-typed)
production_authorized = false
alpha_computed = false
proof_authorized = false
```
