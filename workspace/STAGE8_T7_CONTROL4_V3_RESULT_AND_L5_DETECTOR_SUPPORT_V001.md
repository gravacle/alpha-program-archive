# Stage-8 T7 Control-4 v3 Result, and Lemma L5 (Detector Support) V001

Date: 2026-07-26

## Verdict

```text
CONTROL4_V3_DOES_NOT_BITE_AS_PINNED
witness: CONTROL4_V3_DESIGN_DEFECT_DETECTOR_SUPPORT_MISMATCH
```

A FOURTH defeated falsifier — but defeated by a DESIGN DEFECT in the
sealed v3 spec (this construction lane's own pin), NOT by a protection.
Two independent lanes agree on the null; both also establish, exactly,
why it occurred. Commitment-first was enforced mechanically: the blind
commitment was sealed while no primary output existed in the workspace
(verified), and only then was the primary imported and sealed.

## Measurements (two lanes, independent reconstructions)

```text
(1) BROKEN, pinned falsifier at 100% amplitude: DOES NOT CLEAR 1e-9.
    certified CD upper bound  <= 2.27e-11
    h-free exact derivative    6.1e-24 ... 3.1e-21
    position vs frozen window (1e-8 .. 1e-4): BELOW, by 2.6 decades on
    the certified bound and 13-16 decades on the exact value.
(2) UNBROKEN (sealed J): CLEARS. certified <= 1.11e-13; exact
    4.0e-27 ... 3.6e-23 (inside the predicted <= 1e-18). Z(+h) and
    Z(-h) bit-identical at every rung, reproducing the a-parity lemmas.
(3) NON-VACUITY: CLEARS. max_k ||J'(t_k)||_2 = 2.6e-4 ... 7.4e-4.
(4) DETECTOR LOADED: ||sym(Psi)||_F <= 3.3e-15 (L4 reconfirmed
    pointwise, per lambda, both states, both ell) while
    ||antisym(Psi)||_F = 2.10e-2 (sealed envelope-A pure state).
Primary-lane apparatus validated against the sealed Hermite baseline
(completed amplitudes reproduced to 1.05e-14 ... 1.21e-13). The blind
lane RECOVERED, not typed, the record data: p = (1/4,1/2,1/4),
w = (-1/4,1/2,-1/4).
```

## LEMMA L5 (detector support) — the structural discovery

```text
STATEMENT. The alpha_x detector matrix Psi is supported EXACTLY on the
x-Hermite-ladder block: entries (m, m+4) in the sealed lexicographic
(a,b,c) spatial order.

PROOF (three involutions, all verified on the sealed data):
  T'  = P_x (x) (i gamma^1)  [Lemma 2's own involution]  =>  P_x Psi P_x = -Psi
  T_y = P_y (x) (i gamma^2)                              =>  P_y Psi P_y = +Psi
  T_z = P_z (x) (i gamma^3)                              =>  P_z Psi P_z = +Psi
  (T_y, T_z verified to commute with h_0 (residual 0.0), fix the record
   term (<= 8e-19), leave J even (<= 7e-23), and leave both pinned
   states invariant.)
  The simultaneous parity constraints force support on the x-ladder
  block and nowhere else.
VERIFICATION: max |Psi| outside the block <= 2.2e-16; inside ~7.4e-3.
```

L5 is a new lemma of the same family as L1-L4 (sealed in
STAGE8_T7_RECORD_PARITY_LEMMAS_RESULT_V001) and is cited from here.

## Why v3 read null: exact trace-orthogonality

The pinned A_0 (nearest-neighbour shift in the FLAT index, support
|m-n| = 1) is disjoint from the x-ladder block (|m-n| = 4). Hence

```text
tr[ antisym(Psi) . A_0 ] = 0  IDENTICALLY
  measured relative pairing <= 9.9e-17 in all eight configurations,
  while the same antisym(Psi) pairs with the x-ladder direction at
  0.992 ... 0.9998.
```

The construction lane authored that pin (v3 spec S2) without checking it
against the detector's support. The defect is this lane's, and it is the
FIFTH control-design defect of the gate — the same genus as the v1
CONTROL4_DESIGN_DEFECT, not the L4 genus.

## S4's interpretation is REFUTED by the same measurement

The sealed v3 spec's S4 says the observed combination — |Z'(0)| < 1e-9
at 100% amplitude with non-vacuity clearing and antisym(Psi) loaded —
"would mean the alpha_x channel is annihilated in BOTH tau gradings —
a FIFTH protection." Its literal criterion fired; its stated meaning is
FALSE:

```text
tau-ODD grading:  annihilated (sym(Psi) <= 3.3e-15) — that is L4.
tau-EVEN grading: NOT annihilated (antisym(Psi) = 2.1e-2), and a
  tau-EVEN direction inside the detector's support reads 5.2e-8 ...
  4.8e-5 under the same apparatus, same 100% pin.
THERE IS NO FIFTH PROTECTION.
```

S4 conflated "this particular direction reads zero" with "the channel is
annihilated". That conflation is a defect of the sealed v3 text and is
corrected here of record; the criterion may not be cited for a
fifth-protection claim.

## Disambiguating diagnostic (reported; NOT adopted)

The blind lane, to distinguish design defect from protection, replaced
A_0 by the antisymmetric x-ladder shift (still tau-EVEN, still 100%
pin, same apparatus): readings 5.2e-8 ... 4.8e-5 — every configuration
INSIDE the frozen window, and 4.57e-6 on the sealed envelope-A pure
state against S3(a)'s 1e-6 central prediction. The lane reported it as
a diagnostic only, explicitly did not propose it as a substitute
falsifier, and did not select it by its output. THIS CONSTRUCTION LANE
LIKEWISE DOES NOT ADOPT IT. Any v4 is a principal decision (below).

## Frozen-prediction outcomes (calibration, honest)

```text
S3(a) BROKEN magnitude: MISS (null; no window). Third consecutive
  magnitude miss by this prediction family.
  NOTE, explicitly POST HOC and NOT CREDITED: the underlying magnitude
  MODEL (transfer coefficient applied to the witnessed |dD|) evaluated
  on the supported direction gives 4.57e-6 against the 1e-6 central
  prediction — inside the window. The model was sound; the DIRECTION
  PIN was wrong. This is recorded so the calibration ledger reflects
  which component failed, and it is not counted as a hit.
S3(b) UNBROKEN: HIT (<= 1.11e-13 certified, exact <= 3.6e-23).
S3(c) STRUCTURAL: 4 of 5 — per-slot vanishing CONFIRMED (sum over all
  144 slots <= 9.5e-22); exact linearity CONFIRMED (deviation 0.0);
  Lemma 1 survival CONFIRMED (<= 1.5e-15); mixed-vs-pure identity
  CONFIRMED in its strongest form (relative difference exactly 0.0 —
  B_D is exactly diagonal in the sealed basis and Psi has no diagonal
  support); same-slot occupancy FAILED (0 of 144), which is the
  support mismatch itself.
```

## ESCALATION — the v4 question is the principal's, and it is subtle

```text
The x-ladder direction is where the detector lives, and L5 determines
that support A PRIORI FROM SYMMETRY — not by reading any output. An
argument therefore exists that a v4 pinned to "the detector support as
determined by L5" would be selected by THEOREM rather than by outcome,
which is a materially different epistemic position from v3's.
AGAINST: L5 was found after four defeats, and its supported direction
was measured to be effective before any v4 could be proposed. Adopting
it now is outcome-adjacent at one further remove — precisely the
concern the principal named, one level deeper.
THIS LANE TAKES NO POSITION and will not author v4 absent an explicit
principal decision. If v4 is authorized, its frozen prediction should
be stated BEFORE any further execution and the selection history
(five defeats, L5's discovery timing, the measured diagnostic) recorded
in the same artifact.
```

## Protected status

```text
control4_v3_executed = true
control4_satisfied = false
control4_v4_authorized = false
L5_detector_support_derived = true
gamma_gate_verdict = BLOCKED (unchanged; the control obligation remains
  undischarged and the gate's verdict is untouched by this result)
gamma_refutation_computed = false
alpha_computed = false
proof_authorized = false
```
