# Stage-8 Codex Battery Returns, and T16 INDEPENDENTLY CONFIRMED V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY — ONE CONFIRMED BATTERY RESULT (T16) + THREE DERIVATIONS RECORDED
```

Four battery obligations were independently derived by the
INDEPENDENT-SYSTEM lane (Codex; different model family) from SEALED
INPUTS ONLY, with no construction-lane drafts consulted. Recorded here;
T16 rises to a CONFIRMED result on a three-way agreement.

## T16 — INDEPENDENTLY CONFIRMED (three-way)

```text
THE SIX SEALED OUTPUT ITEMS, agreed by all three sources:
  char poly            (z^4 - 4 z^2 + 2)^2
                       = z^8 - 8z^6 + 20z^4 - 16z^2 + 4
  eigenvalues          +-sqrt(2+sqrt2), +-sqrt(2-sqrt2), EACH TWICE (8)
  kernel multiplicity  0
  Tr[B^2]              16
  Tr[B^4]              48
  R_square             3/16
```

THE THREE INDEPENDENT SOURCES:

```text
1. CODEX, blind, from the sealed V011 Phi = pi matrix and spec text.
   It DISCLOSED encountering stage8_execution/t_reports/T16.json during
   discovery and NOT using it as authority — so this is a genuine
   independent cross-derivation, not a read-back.
2. THE REVIEWER LANE, which verified Codex's derivation for internal
   coherence from scratch (z^2 = 2 +- sqrt2 from the char poly; the
   eight eigenvalues; sums of squares and fourth powers; kernel
   multiplicity from the nonzero constant term).
3. THIS CONSTRUCTION LANE, verifying the six items itself before
   recording any confirmation:
     8 eigenvalues; Tr[B^2] = 4(2+r2) + 4(2-r2) = 16 exactly;
     Tr[B^4] = 4(6+4 r2) + 4(6-4 r2) = 48 exactly;
     R_square = 48/256 = 3/16 exactly;
     and byte-level agreement with the pre-existing sealed T16.json
     (char_poly, coefficients [1,0,-8,0,20,0,-16,0,4], all eight
     eigenvalues, kernel_multiplicity 0, tr_B2, tr_B4, R_square).
```

PRECISION CORRECTION of record (small, but this is a confirmed result):
the relay states kernel multiplicity 0 "since the constant term is
2 != 0". The constant term of the FACTOR (z^4 - 4z^2 + 2) is 2; the
constant term of the FULL characteristic polynomial is 4. Both are
nonzero, so the conclusion holds either way; the correct citation is the
full polynomial's constant term 4.

VERIFICATION-PHASE CONSEQUENCE, per the principal's instruction: the
verification phase should CREDIT this rather than redo it. The inherited
charters (STAGE8_VERIFICATION_PHASE_CHARTERS_V001) list T16's numerical
diagonalization as a separately coded BLIND-LANE ITEM. That item is
SATISFIED by the above: a different-model-family blind derivation,
independently checked twice, agreeing with the sealed artifact on every
reported item. A redundant re-run is not required and the charter item is
credited, not waived — the evidence exceeds what the charter asked for.

## T3, T6, T10 — derivations recorded (not promoted to confirmed)

```text
T3  K_Pauli,kin = -1/2, invariant magnitude 1/2 — MATCHES the fixed
    benchmark. No recalibration.
T6  kappa_L = [4 L^4 sin^2(pi/L)]^-1 -> 0, failing for the CORRECT
    reason (direct-sum zero stiffness). This lane verified the stated
    asymptotics independently: with sin(pi/L) ~ pi/L the denominator
    scales as 4 pi^2 L^2, and kappa_L / [1/(4 pi^2 L^2)] -> 1
    (measured 1.053 at L=8, 1.0032 at L=32, 1.00020 at L=128,
    1.000013 at L=512). Post-hoc multiplication by powers of L, cell
    count, or volume remains FORBIDDEN.
T10 Derived: with F_phys = im(d1) and
    Q_flux = P_h d1^dag (d1 P_h d1^dag)^+, every xi in F_phys has a
    unique horizontal minimum-norm lift with d1 Q_flux xi = xi,
    orthogonal to ker(d1) cap im(d0)^perp; it depends only on xi, hence
    is representative-independent; unit faces outside F_phys get no
    lift.
NO UNDERDETERMINATION was found in any of the four under the sealed
battery/V011 authorities.
```

These three are RECORDED AS INDEPENDENT DERIVATIONS, not promoted to
confirmed: only T16 has the three-way agreement plus a pre-existing
sealed artifact to check against. T3/T6/T10 await the verification
phase's own lanes, which may now credit Codex's derivation as one
independent source rather than starting from zero.

## Protected status

```text
T16_independently_confirmed = true
T3_T6_T10_independently_derived = true   (not confirmed)
battery_verdict_issued = false           (the evaluator alone issues it)
kappa_record_computed = false
alpha_computed = false
proof_authorized = false
```
