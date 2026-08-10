# DECISION OF RECORD — SLOT 18: THE PREDICTION NOMINATED BY RULE, NOT BY CHOICE

STATUS: **SEALED — PRINCIPAL APPROVED 2026-08-10** (in-session selection: "Freeze a nomination rule now")

## The rule (frozen in advance of the action's completion)

At the moment the complete action stands of record (the build's discharge cascade registering its
final obligation), slot 18's prediction is nominated AUTOMATICALLY by this rule:

**The nominated observable is the first record-native observable the completed action FORCES that
(a) is not alpha, and (b) is consumed nowhere upstream of alpha's computation chain.**

Determinism completion (registrar-supplied, part of the frozen rule): if more than one observable
satisfies (a) and (b) at the completion moment, the nominee is the one with the SHORTEST derivation
chain (fewest consumed sealed artifacts from the action to the observable); a residual tie breaks by
the EARLIEST register entry of the forcing artifact. No human choice occurs at nomination time.

## Why this form

The slot census (Q-738) typed slot 18 as the Q_spec's single FREE-CONTENT slot — a
prediction-nomination protocol slot — and warned that nominating a specific observable in advance
would be the adoption the slot defers. This rule removes the freedom WITHOUT the adoption: the
commitment is made before the action exists (the preregistration discipline of the 7A recognition
spec, applied to the program's last free slot), and the record itself selects the nominee.

## Scope

No observable is named today; nothing is computed; no flag moves. The nomination fires as a
REGISTRAR ACT at action-completion, citing this document, and the nominee's subsequent testing is
governed by the release condition of record (frozen this same day) and the standing fences.
alpha_computed = false; proof_authorized = false; kappa_record_computed = false.

- [x] APPROVED by the principal (Brian Mulconrey) — 2026-08-10, in-session.
- Registrar countersignature: sealed, mirrored, pushed 2026-08-10.
