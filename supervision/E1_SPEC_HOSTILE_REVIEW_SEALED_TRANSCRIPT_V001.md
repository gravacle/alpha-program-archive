# E1 Successor Spec — Hostile Pre-Execution Review, Sealed Transcript
Claude lane · 2026-07-26 · verbatim. VERDICT NOT_READY. Its finding B-1 REFUTES
by exact witness the sealed C3/C5 corrections (the 'two-line R^-6' claim) that this
construction lane sealed as corrections of record AND reported to the principal as a
headline finding. Errata sealed same-cycle.

---

VERDICT: NOT_READY

================================================================================
FINDINGS
================================================================================

--- BLOCKING ---

B-1. SECTION: §B / C3; §O.A A-L3; C5; NC8; §V (E1S_N_GE_2_CERTIFIED_BLOCK_ISOLATED_TO_N1); §G row 1.
DEFECT: The frozen baseline's load-bearing structural claim — "the lowest connected
two-cell cumulant is a TWO-LINE object (the first-order determinant term has no cross
term)" — IS FALSE AS STATED, and I have an exact witness. The memo §1.5 justifies it by
writing `V - 1 = X_1 + X_2` with `X_i` diamond-supported. That decomposition is not
exact: for relay-ordered cell evolutions `V^{(12)} = V_2 V_1`, so
`V^{(12)} - 1 = Y_1 + Y_2 + Y_2 Y_1` with `Y_i = V_i - 1`, and the Möbius difference of
the LINEAR (trace) term is `tr[C Y_2 Y_1 C] != 0`. Exact truncated-power-series
computation (exact Fractions, rank-3 rational projector, n=6; scratch
`/private/tmp/.../e1_review/crossterm.py`) gives, with each cell vertex carrying one
power of eps:

    Phi_12 = -[L(12) - L(1) - L(2)],  eps^1 coefficient = 0 (connected, correct)
    eps^2 coefficient of Phi_12  =  -346463176730651/17428667193612
      -tr[C Y_2 Y_1 C]  (ONE sea line)   = -1337849531/65078154
      +tr[C Y_1 C Y_2]  (TWO sea lines)  = 35484269897501/52286001580836
    eps^2 == oneline + twoline  ->  TRUE
    eps^2 == twoline alone     ->  FALSE
    one-line term identically zero -> FALSE

So the lowest connected two-cell cumulant is
`Phi_12 = -tr[C Y_2 Y_1] + tr[C Y_1 C Y_2] + O(Y^3)` — TWO terms at the SAME order, only
one of which is two-line. The one-line term carries a SINGLE factor of the sea kernel
(R^-3) plus free propagation between the cells; the memo's `Phi_12 ⊃ -tr[CX_1CX_2]` is
honest, but the inference "Hence the pair activity carries R^-6, not R^-3" does not
follow, and C3/C5 freeze that inference as a non-re-litigable input. The vanishing
`Y_2 Y_1 = 0` holds only in the strict equal-time multiplication-operator idealization
with disjoint supports; the actual `V_i - 1` are Dyson-dressed by free `h_0` propagation
over the whole interval, so `Y_2 Y_1 != 0`. Note the corpus already owns the governing
object: the one-root temporal-return `t^-3` data — i.e. exactly NC3. C3's dismissal of
NC3 ("a one-line counting artifact; says nothing about E1") is therefore not established;
NC3 may be the control that detects this term.
CONSEQUENCES: (i) C5's "the long-distance direction has margin" and "clustering was never
the missing ingredient" are unproven; (ii) IR-A's n>=2 leg would certify a bound on the
WRONG object, making `E1S_N_GE_2_CERTIFIED_BLOCK_ISOLATED_TO_N1` — the spec's own
PREDICTED outcome — a FALSE POSITIVE-capable verdict; (iii) NC8, as written, mandates
that a one-line bound MUST FAIL and be dismissed, which entrenches the error; (iv) §B's
"an obligation that contradicts C1-C6 without a new exact witness is a spec violation and
BLOCKS" fences an executor away from the correct algebra (the exact witness above is
available, so the fence is escapable, but the freeze should never have been placed).
REPAIR (append-only): (a) DEMOTE C3's no-cross-term clause from frozen input to a numbered
obligation `A-L0` — prove `Y_2 Y_1 = 0` on the sealed forms for the admitted cell pairs,
or bound `tr[C Y_2 Y_1 C]` with a certified decay in the cell separation, uniformly over
D3, with named witness `E1_ONE_LINE_CONNECTED_CROSS_TERM_UNCERTIFIED`; (b) restate C5 and
A-L3/A-L4 as covering the two-line SECTOR only, and forbid any verdict asserting "the
n >= 2 sums are certified" until A-L0 closes; (c) restate NC8 as a two-SECTOR control
(one-line sector must be shown either to vanish or to be separately bounded — its
divergence is a PASS only conditional on A-L0); (d) issue a correction of record against
the sealed C1-C6 artifact (`6c3e125b…`) and the route memo (`51f655a0…`), whose
one-line summary to the principal states `R^-6` as fact.

B-2. SECTION: §R.1 S3 (`G_bl`); §R.3 derivation; via C6 + C-L1.
DEFECT: S3 is frozen as a finite constant, and the spec itself labels it "BASELINE HS
DENSITY = the cell-level Shale-Stinespring quantity. Records at full tau_R." C6 — a
FROZEN INPUT of this same spec — states that this quantity is INFINITE
(`||[C, 1_B]||_2 = +infinity`; equal-time localization of the 3-D massless Dirac sea
fails Shale-Stinespring). C-L1's exact record-phase collapse makes the baseline exactly
that equal-time object: for opposite-phase pairs `V(0) - 1 = -2P` with `P` the SHARP ball
projector, so `||C(V(0)-1)C||_2 = 2||CPC||_2`, and by dilation covariance of the sealed
construction (which R-L0 ground (i) itself cites) `||CPC||_2` is INDEPENDENT of the ball
radius — a scale-free constant, infinite by C6. Hence
`G_bl = sup_C |C|_4^{-1/2} · 2||CPC||_2 = +infinity` twice over: once because the
quantity itself diverges, and again because a scale-invariant numerator divided by
`|C|_4^{1/2} -> 0` under refinement diverges regardless. Since R.3 uses
`||A_s||_2 <= |C|_4^{1/2}(G_bl + G_hs)`, this gives `g(eps) = infinity`,
`eta_1 = infinity`, and the SCAD architecture certifies nothing. §R.0 notices the adjacent
fact ("the unsubtracted per-pair baseline trace tr A(0) is itself divergent at full
tau_R … a per-pair Carleman split of the unsubtracted baseline is singular") and then
freezes S3 as finite and consumes it in the bound anyway. S2 is explicitly protected
against exactly this error ("the equal-time version is FALSE by C6"); S3 is not.
REPAIR (append-only): restructure §R so the baseline is NEVER normed. Under C-L1 the
same-phase sector has `V(0) = I` exactly (M(t)=0 off the ball, phases equal on it), hence
`A(0) = 0` up to the C-L2 commutator error; the opposite-phase sector has
`tr A(0) = -2 tr(CPC) = -infinity`, so its determinant is 0 at a = 0 AND at a != 0 and
the sector drops out identically. Delete S3; replace `G_bl` in R.3 by a certified bound on
the C-L2 commutator error, with named witness. STATE THE CONSEQUENCE HONESTLY: after this
repair all four surviving SCAD constants rest on C-L2, i.e. SCAD is not an independent
route — it is IR-C's wall re-expressed, and §V/§P must say so.

B-3. SECTION: §R.3 (color-sum closure, `rho_{mu lambda}`, `c_{mu lambda}`); §R.1 S4
(`rho_res`); interacting with §R.2 / PA-3.
DEFECT: R.3 decomposes `Z_hat = sum c_{mu lambda} rho_{mu lambda}` with
`rho := det(1+A(a))/det(1+A(0))` and `c := w*w det(1+A(0))/N(0)`. Under the spec's OWN
predicted baseline (PA-3, "D = 0 exactly", moderate-high confidence) the opposite-phase
pairs have `det(1+A(0)) = D = 0`, so `rho` is UNDEFINED and each such pair contributes
`0 · (0/0)` — i.e. exactly one half of the total `|w*w|` weight is silently dropped, and
the derivation of `sum c = 1`, `sum |c| = kappa_bal` and (R.3.b) is void in precisely the
regime the spec predicts. Independently, S4 defines
`rho_res := sup_{s in [0,1]} ||(1 + A_{mu lambda,s}(a))^{-1}||_op` over ALL color pairs;
at `s = 0` the segment starts at `1 + A(0) = 1 - 2CPC`, whose Fredholm determinant is not
defined (not a trace-class perturbation of the identity), so `rho_res = +infinity` as
written. The architecture's advertised gain (D = 0 ⇒ kappa_bal = 1) and its resolvent
hypothesis are therefore in direct conflict.
REPAIR (append-only): add the obligation "OPPOSITE-PHASE SECTOR VANISHES IDENTICALLY on
the closed pair polydisc" (`tr A_{mu lambda}(a) = -infinity` for all a, hence
`det(1+A(a)) = 0`), with named witness; re-derive `sum c = 1` and `sum |c| = kappa_bal`
over the SURVIVING sector only; restrict S4's sup and the Carleman segment to that sector;
and state that `kappa_bal = 1` then follows as `(1/2)/(1/2)` from the surviving weights,
not from the `(1+|D|)/|1-D|` display.

B-4. SECTION: §R.2 "Consequence to be certified"; R-L4/C-L4; PA-3; §Q2-STOP option (i)
cost block.
DEFECT: The chain "C6 gives `||[C,1_B]||_2 = +infinity`; the inequality
`D^2 <= exp(-2||[C,P]||_2^2)` was verified on 200 exact finite trials; therefore
`D = 0 EXACTLY`, hence `b_0 = 1/2 EXACTLY` and `kappa_bal = 1 EXACTLY`" is an invalid
limit of a bound. `D = det_{ran C}(1 - 2CPC)` is a Fredholm determinant requiring `CPC`
trace class; `tr(CPC)` is the mode count of the sea inside the ball and is `+infinity`
(this is C2's own divergence). At the point where the hypothesis holds, the CONCLUSION'S
OBJECT DOES NOT EXIST — the correct statement is "D is undefined", not "D = 0". A
finite-dimensional inequality certified on rational projector pairs cannot be evaluated at
an infinite right-hand side. The spec is hedged in R.2 ("to be certified, not assumed";
"no artifact may report H-B as discharged") but then asserts the same content as an
outcome-class prediction (PA-3) and, worse, USES IT inside the Q2 escalation cost
statement to the principal ("If R-L4/C-L4 certifies, the single-cell baseline is 1/2
exactly and kappa_bal = 1 exactly"). Note the conclusion may well be RECOVERABLE by the
regularized route (`D = det_2 · e^{tr}` with `tr = -infinity` ⇒ D = 0), which is a
different and honest argument — it is not the one written.
REPAIR (append-only): strike the `D^2 <= exp(-2||[C,P]||_2^2)` route as the ground for
`D = 0`; replace with an explicit obligation to establish existence-or-nonexistence of the
baseline determinant via the Carleman factorization `det = det_2 · e^{tr}` and to state the
regularization used; re-state PA-3 as conditional on that obligation; and remove the
`b_0 = 1/2` / `kappa_bal = 1` clause from the Q2 option-(i) cost block (see C-11).

B-5. SECTION: §R.4 R-L0; §R.1 (sup-first definitions of S1-S5); F'-5; §V
(E1S_REPLACEMENT_ARCHITECTURE_CERTIFIED).
DEFECT: R-L0 demands `X_*(eps)`, a functional of the permitted tuple ONLY, with
`x(C,eps) = |C|_4 g(eps) <= X_*(eps)` for EVERY admitted cell. But `g(eps)` is built from
S1-S5, each of which is ALREADY a sup over admitted cells — so `g` is a single
cell-independent number and `sup_C |C|_4 g(eps) = (coarsest admitted cell 4-volume) ·
g(eps)`. That coarsest-cell 4-volume is exactly what R-L0's own FORBIDDEN clause and F'-5
prohibit. R-L0's two admissible grounds are both foreclosed by the sup-first freeze:
ground (i) (scale covariance, "g carries a compensating negative scaling weight") is
unavailable because `g` is a number and cannot carry a scaling weight; ground (ii)
(uniform smallness in the cell scale) is a statement about per-cell scale dependence,
likewise destroyed. So R-L0 IS UNSATISFIABLE AS WRITTEN, not merely "may fail", and the
verdict `E1S_REPLACEMENT_ARCHITECTURE_CERTIFIED` (which requires R-L0..R-L5) is vacuous.
Note that the requirement arises SOLELY from the color-sum step (the exponentiation
`|rho - 1| <= x e^x` and the `1/(1 - kappa x e^x)` denominator); the linear Carleman
estimate alone already yields action-density form.
REPAIR (append-only): (a) re-freeze S1-S5 as PER-CELL functionals `S_i(C,eps)` with the
sup taken only after the scale weight is exhibited, so ground (i) is testable; (b) add an
obligation to bound `Log(sum c rho)` without an absolute bound on x (e.g. a signed-weight
convexity argument on the surviving sector), or else (c) ESCALATE to the principal the
scoping question "is the pinned skeleton's cell 4-volume an admissible constant under
spec-header scoping clause 1?" — weakening F'-5 is not a lane's to do, and the spec must
not be executed with an obligation that is provably unsatisfiable under its own fence.

B-6. SECTION: §O.A A-L3, A-L4; C5; §G row 1; NC7 permitted outputs; Z.6 / §X (Q6).
DEFECT: The "exact constants" `24 zeta(4) + 2 zeta(6)` and `64 zeta(3) + 16 zeta(5)` come
from CHEBYSHEV SHELL COUNTS ON A CUBIC CELLULATION — `(2k+1)^3-(2k-1)^3 = 24k^2+2`,
`(2k+1)^4-(2k-1)^4 = 64k^3+16k` (both re-verified exact here, k=1..59). The memo says so
explicitly ("With Chebyshev shell counts on a cubic cellulation"); C5 and A-L3 DROP that
qualifier and freeze the constants as if uniform. The D3 quantifier includes family B
(oriented simplicial/barycentric subdivision) and ALL common refinements, for which these
shell counts are false. Two independent violations follow: (i) F'-5 / spec-header scoping
clause 1 — the constants are cellulation geometric data, the very thing R-L0 was written
to forbid; (ii) THE SPEC SILENTLY DEPENDS ON Q6. A uniform cluster/shell count over D3 is
precisely `Q6_UNIFORM_CELL_ADJACENCY_DEGREE_UNDERIVED`; A-L3 is titled "SPLIT
KOTECKY-PREISS CLOSURE" and closes `Gamma_star^split <= 1`, i.e. it does M3-grade polymer
combinatorics. So Z.6's and §X's disclaimer that Q6 is "NOT owned here and NOT absorbed by
any route below" is FALSE for IR-A as specified. (Z.6's other clause — that discharging
every obligation here does not by itself deliver the Route-Q predicate — is correctly
stated and survives.)
REPAIR (append-only): restate A-L3/A-L4/C5 as SCOPED TO THE CUBIC SKELETON AND FAMILY A,
with a named witness for the family-B / common-refinement gap
(`E1_SHELL_COUNT_NOT_UNIFORM_OVER_D3`); state explicitly that any D3-uniform version of
A-L3 CONSUMES Q6 and is therefore not deliverable by this program; and correct the §G
"honest partial result that survives" cell accordingly (it currently promises certified
constants "with the obligation narrowing to null-separated cell chains" — it must also
narrow to the cubic family).

B-7. SECTION: §E1' step 2 vs F'-3 and §R.1 S4.
DEFECT: §E1' step 2 requires `eta_1(2^-k) <= 1/2 CERTIFIED` for grid selection. `eta_1 = 2
kappa_bal g(eps) e^{X_*}` contains `rho_res` multiplicatively, and `rho_res` is declared
NAMED HYPOTHESIS H-R, undischarged, which F'-3 forbids valuing ("Assigning any of them a
numeric value, a default (including 1), or an 'assume for now' placeholder INSIDE A
CERTIFIED BOUND BLOCKS"). PA-4 predicts H-R is NOT discharged by this program. So either
the n=1 grid leg can never qualify (permanent `EPSILON_STAR_VACUOUS_n1`, making the split's
n=1 leg decorative) or F'-3 is violated. §V's phrase "under the named hypotheses … as
disclosed premises" does not resolve it, because step 2's comparison is a hard certified
inequality.
REPAIR (append-only): restate §E1' step 2 for the n=1 leg as a CONDITIONAL certification —
certify the implication "if `rho_res <= rho_bar` then `eta_1(2^-k) <= 1/2`" with
`rho_bar` an explicit disclosed-premise symbol, require the admissible range of `rho_bar`
to be stated in the artifact, and record that `eps_*^{(1)}` so obtained is
premise-conditional and may not be supplied to I3 as unconditional. Reconcile with F'-3 by
naming this the ONLY permitted form of premise-carrying in a threshold comparison.

--- CONDITION ---

C-8. SECTION: Pinned authorities table; §Z (all); Z.6.
DEFECT: The sealed Q2 standard that §Z declares GOVERNING
(`STAGE8_T7_Q2_TRIGGER_AND_CLASSIFICATION_STANDARD_V001.md`) IS NOT IN THE PINNED
AUTHORITIES TABLE and carries no hash anywhere in the spec (single mention, prose only,
line 1504). The executor's mandatory pre-computation hash re-verification ("drift blocks")
therefore does not cover the one artifact that governs the program's most consequential
fence. Same defect for the F-8 findings artifact that Z.6 relies on
(`STAGE8_T7_F8_FIRST_HALF_RESULT_AND_TWO_NEW_FINDINGS_V001.md` — never named or hashed),
which also carries the correction of record that the sealed O1 display's interleaved
reading is FALSE and the CTP-NESTED reading is FORCED. §D inherits O1 "verbatim from the
parent as repaired", and the D6 repair amendment does NOT contain that correction, so the
spec inherits a display that is false as literally read. (The spec's own R.0 and C-L5 are
consistent with the nested reading — this is a citation/pinning defect, not a mathematical
one.)
REPAIR: add both rows to the Pinned authorities table with the hashes verified here
(Q2 standard `38e1517702f6ecb3792da9bb08334b4e344fb3d5bd4c2e1fac5bdc6ef08376a4`, SEAL_OK;
F-8 findings `f84c30367e077ea722e2647696cb7e37374aa388056b444a3c236cd6dd1c5872`, SEAL_OK),
and record in §D that the CTP-nested reading of O1 governs of record.

C-9. SECTION: Z.2 (object-vs-bound tripwire) — ENFORCEABILITY.
DEFECT: A route return CAN satisfy the letter of Z.2 while excluding the sharp localizer on
provability grounds. Z.2 makes (b) require-grade "ONLY IF the finiteness demanded is itself
a sealed principle rather than a convenience of the proof" — and the parent majorant spec
supplies a ready-made citation for exactly that move: D5 is headed "Action-density activity
form (REQUIREMENT, not a convenience)". A lane can declare (b), cite D5's own
"REQUIREMENT" language as the sealed principle, and thereby launder a proof-architecture
need into a require-grade exclusion. Nothing in Z.2 distinguishes principles UPSTREAM of
the activity architecture (definitional / Axis-level) from requirements INTERNAL to it.
REPAIR: append to Z.2 — "D5, Kotecky-Preiss convergence, action-density form, and every
other requirement internal to the majorant/activity architecture are CONVENIENCES OF THE
PROOF for the purposes of (b) and MAY NOT be cited as the sealed principle grounding a
require-grade (b). A require-grade (b) must name a principle upstream of the activity
architecture. Which principle is invoked, and its grade, is classified by fresh-context
hostile review, never by the returning lane."

C-10. SECTION: §Q2-STOP (steps 1-3, trigger list) vs Z.2 and Z.5.
DEFECT: Three wiring failures between the drafting lane's §Q2-STOP and the construction
lane's §Z. (i) §Q2-STOP step 1 says "STOP. No further obligation is attempted… No bound is
re-derived", with "NO OTHER ACTION PERMITTED" — an executor can read that as forbidding the
(a)/(b)/(c) analysis Z.2 makes MANDATORY, and step 2 (seal the finding) does not list the
declaration among the sealed contents. (ii) §Q2-STOP step 3 and §V's
`E1S_CERTIFIED_DIVERGENT_AT_SHARP_LOCALIZER` both say "with BOTH options" — a two-option
template — while Z.5 requires (i), (ii) AND (iii). (iii) NO OPTION (iii) COST BLOCK EXISTS
anywhere in the spec: §Q2-STOP supplies full cost blocks for (i) and (ii) only, and nothing
instructs the executor to produce one, even though the sealed standard orders (iii)
evaluated FIRST.
REPAIR: append to §Q2-STOP — step 2 explicitly includes the Z.2 (a)/(b)/(c) declaration as
part of the sealed finding and step 1's prohibition does not extend to it; step 3 reads
"all three options (i), (ii), (iii)"; and add a §Q2-STOP option (iii) block stating its
scope and costs (what a derivation attempt of the spatial profile would consume, and that a
failed attempt is a recorded result licensing (ii)), with no argument for or against.

C-11. SECTION: §Q2-STOP option (i) and (ii) cost blocks; §G row "IR-C (coefficient
nonzero)".
DEFECT: The sealed standard says "DO NOT ARGUE FOR EITHER … COSTS ONLY." The cost blocks
carry evaluative comparatives and one pre-judgment: option (i) is framed as "strictly more
information than the status quo", the §G row calls the same outcome "Strictly better than
the status quo", and the "WHAT IS *NOT* REFUTED … so the cost is not overstated" clause
asserts that "what is refuted is the ACTIVITY architecture, not the baseline" and that
"EVERY sealed result depending on it is untouched". That last clause PRE-DECIDES Z.2's
(a)/(b)/(c) classification toward (b)/(c) — before the finding exists and before the
hostile classifier has seen it — which is the exact move Z.2 exists to catch. Option (ii)'s
block is by contrast an eleven-item liability list plus "the front stops". The net framing
tilts.
REPAIR: strike "strictly more/better than the status quo" and equivalent comparatives from
§Q2-STOP and §G; replace the "what is not refuted" clause with the neutral statement "which
of Z.2 (a)/(b)/(c) this finding establishes is not determined by this spec and is
classified by hostile review; the cost of option (i) is stated separately under each of the
three classifications"; and state that no cost block may assert a Z.2 grade in advance.

C-12. SECTION: Z.3 (tiers); §Z preamble.
DEFECT: Z.3's compression of the sealed Part 3 drops Tier 1's operative uniqueness
criterion ("forces the spatial profile UNIQUELY (up to sealed conventions), COMPETITORS
EXCLUDED — the standard the temporal pulse met") and drops the T5b bucket-rule citation
from Tier 2. A governing paraphrase that omits the uniqueness test lowers the bar a lane
can propose Tier 1 against. Compounding this, the §Z preamble says the standard "GOVERNS
this spec and supersedes any narrower Q2 language ELSEWHERE IN THIS TEXT" — which does not
state that the sealed text governs over §Z's own paraphrase.
REPAIR: append to §Z — "Where §Z's paraphrase and the sealed standard
(`38e15177…`) differ in any respect, THE SEALED TEXT GOVERNS"; and restore Tier 1's
"uniquely, up to sealed conventions, competitors excluded" and Tier 2's T5b bucket-rule
citation verbatim.

C-13. SECTION: §R.1 S2/S3 normalization exponents; §R.3 ("the answer to C2").
DEFECT: The `|C|_4^{-1/2}` exponent in S2/S3 is asserted, never derived. R.3's celebrated
step — "The two `|C|_4^{1/2}` normalizations multiply to `|C|_4` EXACTLY: the quadratic
Carleman structure recovers D5 action-density form on its own. This is the structural
reason Hilbert-Schmidt replaces trace-norm, and it is the answer to C2" — is a bookkeeping
tautology: it holds for ANY exponent pair summing to 1, and asserts nothing unless the HS
norms are actually finite at exponent 1/2 uniformly over the refinement quantifier. If the
true scaling is `|C|_4^{alpha}` with `alpha < 1/2`, the sup diverges under refinement
(B-2 exhibits exactly that for S3, where the true scaling is `alpha = 0`).
REPAIR: add obligation `R-L2b` — DERIVE the scaling exponent: certify
`||C(V(a)-V(0))C||_2 <= |C|_4^{1/2} G_hs` with `G_hs` finite uniformly over the D3
refinement quantifier, exhibiting the mechanism that supplies the two half-powers (cell
time extent from the Duhamel bound; Gevrey `b_D`), named witness
`SCAD_HS_SCALING_EXPONENT_UNDERIVED`; and downgrade R.3's claim to "bookkeeping consistent
with D5 CONDITIONAL on R-L2b", deleting "it is the answer to C2".

C-14. SECTION: F'-1 "RECORDED FOR THE REVIEWER" clause.
DEFECT: The fence itself (block immediately, escalate, adoption principal-only) is correct
and absolute, and no route in the spec reaches for a clustering axiom — that check passes.
But F'-1's rationale instructs the escalation artifact to say that a clustering reach "is
therefore not merely forbidden, it is evidence that the reaching obligation has been
MIS-DERIVED". That instruction rests entirely on C5's margin claim, which B-1 and B-6
undercut. If the one-line connected term is real, or the shell counts are not D3-uniform,
a reach for clustering may be evidence of a genuine need — and the spec would have
pre-scripted the escalation to tell the principal the opposite.
REPAIR: strike the "evidence that the reaching obligation has been mis-derived" sentence and
the instruction that the escalation "must say so", pending closure of A-L0 (B-1) and the
D3-uniformity scoping (B-6). The fence's operative clauses are unchanged.

C-15. SECTION: §X; interaction with parent O5 and M-10.
DEFECT: Parent M-10 makes O5 (the DIFFERENTIATED cluster series) a consumer of
`epsilon_star`, and the parent's O5 states expressly that convergence of the
undifferentiated series does not imply it "and may not be cited for it". SCAD bounds
`Phi_C` only; no a-derivative versions of S1/S2 or of R.3 exist. §X's list of
non-claims does not disclaim O5.
REPAIR: add to §X — "It supplies no bound on the differentiated cluster series; parent O5
remains unsupplied and may not be inferred from anything in this program," and add the
corresponding row to the fence register.

C-16. SECTION: NC7 permitted-outputs list vs PA-C4.
DEFECT: NC7 permits "the C-L3 log coefficient" as an output; PA-C4 predicts its modulus in
`1e-2 .. 1e+2` times `2/pi`, i.e. roughly `6.4e-3 .. 64` — a window that BRACKETS the
program's target magnitude. A permitted numeric output with a pre-registered window
containing the forbidden target is a live interaction with the no-target fence, in both
directions (spurious evaluator hits; and the temptation the fence exists to remove).
REPAIR: append to NC7 — the C-L3 coefficient is reported ONLY in exact symbolic form as an
explicit rational/algebraic multiple of `2/pi`, never as a decimal; the evaluator's
transform-grep is run on it with a pre-registered exemption keyed to that symbolic form;
and any numerical proximity to a target-adjacent value is recorded as coincidence and may
not be commented on, compared, or propagated.

--- NOTE ---

N-17. Handoff checklist item 1 instructs the construction lane to "decide the disposition of
the ELEVEN rows marked 'no adjacent seal'". There are EIGHT such rows (lines 53, 60-66);
the ledger row is separately marked "living document, unsealed by design". A seal-time
instruction with a wrong count invites an incomplete disposition. Repair: correct to eight
and enumerate them by path.

N-18. §S claims "the parent's fences F-1..F-8 (carried as F'-1..F'-13)". Parent F-2 (O7
failure handled ONLY by `T7III_SCOPE_RESTRICTED_ESCALATE`; never a silent pinning, never a
lemma-shaped restriction) has no F' counterpart — F'-2 is the Q2 stop rule. Its substance
survives in §X ("does not pin the D3 quantifier to any finite list, under any outcome"), and
O7 is retired by the re-scope, so nothing is lost; but the mapping claim is inaccurate and
the F' list runs to F'-14, not F'-13. Repair: append an explicit F-to-F' mapping table.

N-19. The calibration ledger's standing-calibration header still reads "MAGNITUDE / SCALING
predictions: MISSED TWICE CONSECUTIVELY" while its own entry table records the third miss
(07-26 Control-4 v3 S3(a)). The spec's §P says THREE and names the direction-pin cause
correctly, so the spec is more accurate than the living document it cites. Defect is in the
ledger, not the spec. Repair: update the ledger header (out of scope for this spec).

N-20. Prediction hygiene, per handoff item D ("is any OUTCOME-CLASS prediction a disguised
magnitude prediction?"): PA-A5 (`eta_{>=2}(eps_*)` in 1/64..1/2) is near-unfalsifiable — the
upper bound is the grid-selection criterion itself and, with A-L4's derived
`eta_{>=2} = eps/sqrt2` on a ratio-2 grid, the value is pinned to roughly (1/4, 1/2]; it
could only fail via gross non-monotonicity, which M-8/§E1'-6 leaves possible but unmeasured.
PA-C4 is gated behind PA-C2, which predicts the gate does not open, so the program's only
sharp magnitude prediction will most likely never be tested. PA-B4 predicts the lane's own
future failure to certify — informative only in one direction (it is properly flagged as
granting no permission). PA-3 is not a magnitude prediction but is an invalid-limit
prediction (B-4). Repair: restate PA-A5 as a prediction about the FUNCTIONAL FORM
(`eta_{>=2}(eps) = eps/sqrt2` exactly, per A-L4), which is falsifiable, and mark PA-C4
explicitly as conditional-and-probably-untested.

N-21. The D5' split, W1/M-1/M-9 handling, NC4-as-fence, F'-6 envelope-class posture, F'-10
dependency verdict, F'-12 F-8 gate, and the §G graceful-block table (7 memo rows reproduced
faithfully in substance plus 5 self-declared rows) all check out and are not the subject of
any finding above. The D5' split is honest: `Gamma_star^split = eta_1 +
eta_{>=2}^2/(1-eta_{>=2})` reproduces the parent's `Gamma_star = eta/(1-eta)` term by term,
equals 1 at `eta_1 = eta_{>=2} = 1/2` exactly as the parent does at `eta = 1/2`, and
§E1' step 2 independently enforces `<= 1/2` on BOTH legs, so no number is loosened; the
"KOTECKY-PREISS DOES NOT RELEASE n = 1" clause with witness `D5_SPLIT_MISREAD_AS_RELEASE`
isolates rather than evades `n = 1`, exactly as claimed.

================================================================================
BASELINE_CHECK — my own re-derivations of the load-bearing C1-C6
================================================================================
Runtime: pinned `codex-primary-runtime` python3 3.12.13, no scipy, exact `Fraction` and a
hand-rolled exact `Q(sqrt2)`. Scripts: `/private/tmp/claude-501/-Users-bgm-MB-Work/
578abe61-ea1d-48e6-8fb1-b06509d933a1/scratchpad/e1_review/rederive.py`, `crossterm.py`.

C1 — CLOSED-FORM SEA KERNEL, DEGREE, PARITY: CONFIRMED, derived independently.
`C(p) = (I - alpha·p-hat)/2`. With the 3-D transform `FT[|p|^{-1}](x) = 1/(2 pi^2 |x|^2)`
and `FT[p_j f] = -i partial_j FT[f]`:
`partial_j [1/(2 pi^2 |x|^2)] = -x_j/(pi^2 |x|^4)`, so
`FT[p_j/|p|] = +i x_j/(pi^2 |x|^4)`, and
`-(1/2) alpha_j FT[p_j/|p|] = -i alpha·x/(2 pi^2 |x|^4)`. Hence
`C(x) = (1/2) delta^3(x) I - i alpha·x/(2 pi^2 |x|^4)` — exactly C1. Verified numerically
exactly that `(alpha·r)^2 = |r|^2 I_4` (Dirac alphas, r = (3,-5,7): all four diagonal
entries 83 = |r|^2, off-diagonals identically 0), giving
`||C_off||_op = 1/(2 pi^2 |r|^3)` — degree -3, odd, zero spherical mean,
Calderon-Zygmund. Marginality constant: `int_{a<|r|<R} |C_off| d^3r = int (4 pi r^2)/(2 pi^2
r^3) dr = (2/pi) log(R/a)` — CONFIRMED exactly.
BONUS, and it validates the spec's own correction: `||alpha·r||_F^2 = 4|r|^2` (computed
exactly: 332 = 4·83), so `||C_off||_F^2 = 1/(pi^4 |r|^6)`. The memo's A-L1 constant
`1/(4 pi^4 R^6)` is the per-component reading and is a factor 4 optimistic; the spec's
frozen conservative `1/(pi^4 R^6)` IS CORRECT. PA-A2's direction prediction is right.

C2 — K_sea DIVERGENT, NOT MERELY UNPROVEN: CONFIRMED at the level of the mechanism, and it
is stronger than the spec uses. `||C_state · u · Q 1_{D_t} Q||_1` contains, from the
`delta/2` half of `C`, the mode count of the sea inside `D_t`: `tr(CPC)` for `P` a spatial
region is `+infinity` carrier-blind (power, `~|D_t| Lambda^3`), finite only on a fixed
carrier, which scoping clause 1 forbids. So the Phase-1 functional must be replaced — but
note the SAME divergence is what kills S3/`G_bl` and what makes R.2's `D` a
non-existent-rather-than-zero determinant (findings B-2, B-4). C2 is right; the spec does
not follow it all the way into its own replacement.

C3 — TWO-LINE STRUCTURE / "NO CROSS TERM AT FIRST ORDER": REFUTED AS STATED. See B-1 for
the exact witness. The correct lowest connected two-cell cumulant is
`Phi_12 = -tr[C Y_2 Y_1] + tr[C Y_1 C Y_2] + O(Y^3)`; only the second term is two-line.
`V^{(12)} - 1 = Y_1 + Y_2 + Y_2 Y_1` for relay-ordered cell evolutions, and `Y_2 Y_1 = 0`
holds only for strictly-localized equal-time multiplication vertices with disjoint
supports — not for the Duhamel-dressed `V_i - 1`. Exact eps^2 coefficient matches
`oneline + twoline` and NOT `twoline` alone; `oneline != 0`. This is the single most
serious defect in the reviewed chain, because C3 is frozen as non-re-litigable and the
whole reclassification headline ("not an infrared clustering problem", `R^-6`) rests on it.

C4 — m0 = m1 = 0, SECOND-DIFFERENCE IDENTITY, tau_R SATURATION: FULLY CONFIRMED, exact
`Q(sqrt2)`.
`m_k` for k = 0..9 = 0, 0, -1, 0, -2, 0, -4, 0, -8, 0; all odd moments exactly 0;
`m_{2j} = -2^{j-1}` for j >= 1 (checked j = 1..4).
`sum_lambda w_lambda f(lambda) = -(1/4)[f(+sqrt2) - 2 f(0) + f(-sqrt2)]` verified exactly
on monomials of degree 0..8 — the completed Kraus operator IS the symmetric second
difference.
`int_0^1 32 min(t,1-t)^3 dt = 2·32·(1/4)·(1/2)^4 = 1` EXACTLY, so `int_0^1 v = tau_R =
pi/sqrt2`, hence `lambda tau_R in {0, +pi, -pi}` and, with `S^2 = I`,
`exp(-i lambda tau_R S) = cos(lambda tau_R) I - i sin(lambda tau_R) S = (+1,-1,-1)·I`
exactly on the ball.
SATURATION: `sum_lambda w_lambda phase_lambda = 1/2 + 1/4 + 1/4 = 1 = sum_lambda
|w_lambda|` — EXACTLY EQUAL, so Phase-1's l1-mass step is TIGHT and the zero-sum weights
buy no decay. Second difference applied to `(+1,-1,-1)`: `-(1/4)(-1 -2 -1) = 1`, agreeing.
Operator level: `sum_lambda w_lambda u_lambda = m_0 (I-P) + 1·P = P` — the weights do
promote the SHARP ball projector to the leading in-cell object. C4 is correct in every
particular. It is also, per B-2, what makes S3 infinite.

C5 — LONG-DISTANCE MARGIN AND ZETA CONSTANTS: ARITHMETIC CONFIRMED, SCOPE AND STANDING
NOT. Shell identities exact for k = 1..59: `(2k+1)^3-(2k-1)^3 = 24k^2+2`,
`(2k+1)^4-(2k-1)^4 = 64k^3+16k`. Two-line sums: `sum (24k^2+2)/k^6 = 24 zeta(4)+2 zeta(6)`,
and `24/90 = 4/15` exactly so the closed form `4 pi^4/15 + 2 pi^6/945` is right; exact
rational partials S(100) = 28.010436, S(1000) = S(3000) = 28.010444. 4-D:
`sum (64k^3+16k)/k^6 = 64 zeta(3)+16 zeta(5)`, partials 93.519318 / 93.522454 / 93.522482
(no closed form — the spec is right to say so). One-line legs diverge as advertised:
3-D S(1000) = 182.0554 against `24 H_1000 = 179.6513` (difference converging on
`2 zeta(3) = 2.40411`); 4-D S(1000) = 64026.3, i.e. `~64K` linear. Refinement scaling
re-derived: `int_L^inf R^-3 dR = 1/(2L^2)`, total `eps^2 L^4/2 = |C|_4 (eps^2/2)`,
`eta^2 = eps^2/2` L-INDEPENDENT — confirmed (the memo's display has a typo `/ L^...`; the
spec's A-L4 states it correctly). BUT: these are CUBIC-cellulation counts (B-6), and the
two-line sum is not the whole cumulant (B-1/C3). So "the long-distance direction has
margin" and "clustering was never the missing ingredient" are NOT established by this
arithmetic.

C6 — BLOCK CONFINED TO n = 1: CONFIRMED as a statement, and it is BINDING ON THE SPEC'S
OWN CONSTANTS in a way the spec missed. Dilation covariance: `C` is invariant and
`P_R -> P_{lambda R}`, so `||CPC||_2` is independent of the ball radius; with the
Shale-Stinespring failure of C6 it is infinite; hence S3 = `+infinity` (B-2). C6 also makes
`tr(CPC) = +infinity`, so the baseline Fredholm determinant `D` does not exist (B-4). The
Lipschitz remark (`int d^3r · r^2/r^6 = int dr/r^2`, divergent) is right and correctly
used to caveat NC9. C6's "only two-time / scattering-type objects can work" is honoured by
S2 and violated by S3.

R.2 BOOKKEEPING (independent check): `S_+ = 1/2`, `S_- = -1/2`; same-phase signed weight
`S_+^2 + S_-^2 = 1/2`, opposite-phase signed `2 S_+ S_- = -1/2`; absolute weights 1/2 and
1/2. So `N(0) = (1 - D)/2` and `kappa_bal = (1+|D|)/|1-D|` are correct AS BOOKKEEPING, and
`kappa_bal = 1` at `D = 0`. The defects are in what `D` is and what happens to the
opposite-phase sector (B-3, B-4), not in the weight algebra.

================================================================================
Z_SECTION_CHECK — fidelity of §Z to the sealed standard, stated bluntly
================================================================================
Seal verified first: `STAGE8_T7_Q2_TRIGGER_AND_CLASSIFICATION_STANDARD_V001.md` =
`38e1517702f6ecb3792da9bb08334b4e344fb3d5bd4c2e1fac5bdc6ef08376a4`, matching its adjacent
`.seal.sha256`. No drift.

BLUNT SUMMARY: §Z is SUBSTANTIVELY FAITHFUL. I looked hard for softening, discretion, or
self-serving latitude in a section written at seal by a lane inside the spec's own
production chain, and on the four items that matter most I did not find it. Nothing in §Z
is weakened relative to the sealed standard; in one place it is STRONGER. The defects are
of wiring, pinning, and compression, not of substance — plus one genuine exploitable
loophole in the tripwire's (b) branch that the sealed standard also contains and §Z had the
opportunity to close.

ITEM BY ITEM:
- OPTION (iii) EXISTS AND IS ORDERED BEFORE (ii): FAITHFUL. Z.1 reproduces the ordering
  rule verbatim in substance, keeps "(i) remains available throughout", and keeps "A FAILED
  DERIVATION ATTEMPT IS A RECORDED RESULT, NOT A DEFEAT … cleanly licenses (ii)". The
  derived temporal pulse `w(s) = 32(1/2-|s-1/2|)^3` is quoted correctly and is identical to
  the sealed `32 min(t,1-t)^3` (`min(t,1-t) = 1/2 - |t-1/2|`), so the "the temporal profile
  was DERIVED, the spatial one POSTULATED" contrast is accurately drawn. NOT WEAKENED.
  BUT the rest of the spec was never updated to a three-option escalation, and no (iii)
  cost block exists (C-10).
- OBJECT-VS-BOUND TRIPWIRE, MANDATORY ON IR-C's CERTIFIED-DIVERGENT ARM, WITH A BLOCK ON
  OMISSION: FAITHFUL AND STRENGTHENED. Z.2 reproduces (a)/(b)/(c) with their grades intact,
  reproduces "SELECTING FOR PROVABILITY: route-shopping at the definition level", and ADDS
  what the sealed standard did not spell out: "Any route return omitting the (a)/(b)/(c)
  declaration BLOCKS. IR-C's certified-divergent arm may not be reported without it." That
  is a genuine strengthening, correctly aimed.
  ENFORCEABILITY: NO — the letter can be satisfied while excluding the sharp localizer on
  provability grounds, via (b) + a citation of the parent's own D5 heading "REQUIREMENT, not
  a convenience" as the "sealed principle". See C-9 for the repair. Separately, the
  tripwire is not wired into §Q2-STOP's ordered ON-TRIGGER list or into §V, and
  §Q2-STOP step 1 ("No further obligation … NO OTHER ACTION PERMITTED") can be read as
  forbidding the declaration (C-10). And §Q2-STOP's option (i) cost block ALREADY asserts a
  classification ("what is refuted is the ACTIVITY architecture, not the baseline";
  "EVERY sealed result depending on it is untouched") — a pre-judgment of the very question
  Z.2 reserves for hostile review (C-11).
- TIER ASSIGNMENT BY HOSTILE REVIEW, NO SELF-CLASSIFICATION: FAITHFUL. Z.3 states "THE
  AUTHORING LANE PROPOSES; A FRESH-CONTEXT HOSTILE REVIEW CLASSIFIES. No execution of this
  spec may assign its own tier," and §X reaffirms that the spec does not answer or rank Q2.
  Tier 2's two-separate-things requirement (DERIVED EXCLUSION plus SELECTION, never blurred)
  and the ER-B failure class are preserved; Tier 3's cumulative-conditionality register
  beside ER-A and complex-vs-real is preserved. DEFECT: Tier 1's uniqueness criterion is
  compressed away ("competitors excluded", "up to sealed conventions") and the T5b bucket
  rule citation is dropped (C-12). Nothing here is made discretionary.
- RECORD-INVARIANCE CRITERION WITH ITS SCOPE LIMIT: FAITHFUL, including the parts a
  self-interested lane would have been tempted to lose. Z.4 keeps GAUGE conditional on
  invariance "established AT THE OPERATOR LEVEL", keeps "THE GAMMA STANDARD APPLIES
  VERBATIM: a numerical coincidence across sampled members is NOT the theorem and may not
  be labeled as one", keeps PREMISE as the default including when invariance cannot be
  proven, and reproduces the SCOPE LIMIT in full — classification rule for Q2's residual
  only, not a sealed physical principle, not citable as authority for the underlying idea
  anywhere else, must earn its own derivation under its own spec. NOT WEAKENED.
- STOP RULE: FAITHFUL. Z.5 keeps STOP-AT-THE-FINDING, seal, escalate with FULL COSTS and
  NO ARGUMENT FOR ANY, and "No lane may answer Q2, pre-empt it, or design around it
  silently." §Q2-STOP's own version adds a trigger list and a `Q2_ANSWERED_BY_A_LANE`
  witness, consistent with the standard.
- Q6 (Z.6): CORRECT IN ITS FORM — "This spec owns E1 only … Discharging every obligation of
  this spec does not by itself deliver the Route-Q predicate" is exactly the right
  statement. It is FALSE IN ITS CONTENT for IR-A, which silently consumes a D3-uniform
  cluster/shell count, i.e. Q6 (B-6).
- STRUCTURAL EXPOSURE, NAMED: §Z is a self-authored compliance section certifying the
  spec's conformity to a standard, added at seal by a lane in the spec's own production
  chain, and it is the one section with no independent check other than this review. The
  disclosure at the head of §Z is honest about the authorship. On the substance it holds up.
  Its most consequential defect is that THE GOVERNING STANDARD IS NOT PINNED OR HASHED
  ANYWHERE IN THE SPEC (C-8), so the executor's "drift blocks" discipline does not protect
  the one authority §Z declares supreme.

================================================================================
HASH_CHECK
================================================================================
Method: `shasum -a 256` recomputed on every pinned row; each row's adjacent
`.seal.sha256` located and compared where one exists. Runtime and tooling as specified.

SEALS I RELY ON (verified before use, all MATCH their adjacent seal files):
  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V001.md            9cfafde1774e78b61b65d44858faf73f177c2ec75f323911473bae06a805ce7b  SEAL_MATCH
  STAGE8_T7_E1_RECLASSIFICATION_..._V001.md              6c3e125ba7a43655b72ec75b218e64d1d5062213d5a10f740e89199cc1033aa1  SEAL_MATCH
  ROUTE_MEMO_2026-07-26_ir_sea_kernel_attack.md          51f655a0a1bd3f20d7789f79e3ced16e08e56305521ebcafd4e9a7d4b8a3e528  SEAL_MATCH
  STAGE8_T7_CONNECTED_LINKED_CLUSTER_MAJORANT_..._V001   818083a52165bc5c2ee86bd43e3b7e30d87f5c9eb82e54935e7829bb6f1f84e3  SEAL_MATCH
  STAGE8_T7_D6_SPECS_REPAIR_AMENDMENT_V001.md            60223e6a175c5fee122f253491fd279daccfa15f8771af12104710f57ce09e5d  SEAL_MATCH
  STAGE8_T7_Q2_TRIGGER_AND_CLASSIFICATION_STANDARD_V001  38e1517702f6ecb3792da9bb08334b4e344fb3d5bd4c2e1fac5bdc6ef08376a4  SEAL_MATCH
  STAGE8_T7_F8_FIRST_HALF_RESULT_..._V001.md             f84c30367e077ea722e2647696cb7e37374aa388056b444a3c236cd6dd1c5872  SEAL_MATCH
NO DRIFT on anything this review depends on.

PINNED AUTHORITIES TABLE — all 22 file rows RECOMPUTED AND MATCH the spec's stated hashes,
byte for byte. Zero discrepancies. The ledger row also matches
(`fcf35d0d458d6720fa19965a4ac976ea85fc52ad5c6ba08db29594b3fd336a04`), correctly labelled
"living document, unsealed by design". Independent seal-file audit of those 22 rows:
  SEAL_MATCH (14): E1 reclassification; parent majorant spec; D6 repair; majorant-arm
    re-scope (209aa390…); Phase-A A1-A4 (789338ad…); L2 typing freeze (cdbacdaf…); L1
    assessment (03fadd36…); gate item 9 (4e1282bc…); A4 relocation (8a7f52ff…); O7 record
    (3c81647e…); Phase-1 draft (679ba036…); Phase-2 draft (08b91543…); Phase-1 primary
    (e4a725a9…); Phase-2 primary (8d986314…).
  NO SEAL FILE PRESENT (8) — the spec's "no adjacent seal" markings are ACCURATE, and the
  eight are exactly: STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_RESULT_V001.md
  (3a6ff617…); BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md (b786db3a…);
  BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md (6f6b822a…);
  STAGE8_T7_ENVELOPE_REALIZATION_COMPARISON_SPEC_V001.md (4059eff5…);
  STAGE8_T7_OPEN_EXHAUSTION_ATTACHMENT_AND_RELAY_NECESSITY_RESULT_V001.md (0df721a1…);
  STAGE8_T7_RELAYED_FAMILY_RESOLUTION_RESULT_V001.md (52401eef…);
  BID_MONOIDAL_EXTENSIVITY_DERIVATION_V001.md (451550c3…);
  STAGE8_T7_CONNECTED_ANALYTIC_CLOSURE_RESULT_V001.md (f891d3af…).

IS THE "no adjacent seal" DISPOSITION ACCEPTABLE? QUALIFIED YES, with one correction and
one carve-out.
- Acceptable in principle, and the drafting lane's posture is right: it flags the absence
  rather than treating a computed hash as a seal, and it routes the disposition to the
  construction lane. A content hash pinned in a reviewed, sealed spec plus mandatory
  executor re-verification with "drift blocks" is adequate custody for a READ-ONLY input:
  it detects post-seal mutation, which is what a seal file buys here.
- CORRECTION REQUIRED: the handoff says "the ELEVEN rows marked 'no adjacent seal'". There
  are EIGHT (N-17). A disposition instruction with a wrong count risks three rows going
  undisposed.
- CARVE-OUT, NOT ACCEPTABLE AS-IS: `3a6ff617…` (state-regulator restriction result) is the
  sole source of C1 — the exact sea covariance — and C1 is the derived starting point for
  the entire program, including the A-L1 kernel constant, the C-L3 log coefficient, and the
  marginality coefficient `2/pi`. An unsealed sole-source authority for the spec's most
  load-bearing input should be sealed before execution, not merely hash-pinned. Same
  argument, one grade lower, for `b786db3a…` (`tau_R = pi/sqrt2`), which every exact-phase
  collapse in C4/C-L1 depends on. Repair: require adjacent `.seal.sha256` for these two
  before execution; the remaining six may proceed hash-pinned.
- MISSING ROWS (C-8): the sealed Q2 standard (`38e15177…`) — which §Z declares GOVERNING —
  and the F-8 findings artifact (`f84c3036…`) relied on by Z.6 are absent from the table
  entirely. Both are sealed and both verify; both must be added so the executor's drift
  check covers them.
