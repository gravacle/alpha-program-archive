# External Re-Audit — v003 Files (Fable reviewer lane, relayed by Brian): NO-GO
Received 2026-07-25 (night). 8 raised, 7 confirmed after adversarial
refutation, 1 refuted. Read-only. Brian's disposition: fix what is broken,
do NOT gold-plate; scope is exactly the list below.

## What held (must not be disturbed by fixes)
- B1 (piece authenticity) CLOSED as mechanism: validate_piece_reconstruction
  genuinely pins pieces to the sealed spec; the commuting surrogate fails by
  many orders.
- B2 (transport pin) fixed correctly.
- Tolerances SOUND, quantified: honest same-rule scatter <= 3.5e-18 (M) /
  4.3e-20 (B) vs the 2e-11/5e-11 pins; a maximal adversarial 2e-11
  perturbation moves any propagator <= 6.5e-11, far under downstream
  floors. No retuning.

## FIX 1 (BLOCKING) — manifest-binding mismatch wedge
Derive lanes (byte-frozen) stamp the v001-path manifest digest (f573ae21…);
comparator v003 demands the v002 manifest digest (cffcdf67…). Never equal on
any authorized bundle -> first production run: both lanes succeed, comparator
writes sealed BLOCKED, canonical comparison path permanently consumed (its
absence is a pre-flight requirement). Same class as the GPG wedge: the
pre-flight rule existed but was not applied to this precondition. Causation
noted: consequence of correctly leaving the derive lanes unchanged, without
checking the cross-binding. Fix constraint: derive lanes frozen per binding
V002 S1 -> mechanism choice must be sealed BEFORE authoring; binding
agreement must be pre-flighted before any canonical path consumption.
DISPOSITION: STAGE8_T7_MANIFEST_BINDING_BRIDGE_AMENDMENT_V001 sealed —
comparator-side bridge (both manifests re-hashed from disk, seals verified,
authority rows compared row-by-row); derive-lane pedigree preserved;
controller v004 pre-flights the bridge.

## FIX 2 (MAJOR) — production reconstruction oracle has zero test coverage
Both oracle-facing negative tests are satisfied by the FIRST check (alpha
typed-equality); the load-bearing reconstruction code (Hermite values, basis
values, momenta, cell/bump quadratures, M/B comparison loop) is
monkeypatched away in every pass test and unreachable in every block test —
never executed anywhere in the suite. The surrogate that matters: verbatim
typed alpha/Sn + exact ladder p + assembled h0 + M_stack=0 + fabricated
constant B_stack + closed-form eigh propagators — rejected ONLY by the
untested M/B comparison. Required: ONE test driving the real oracle
end-to-end with that surrogate, blocking specifically on M/B (subsumes the
wrong-quadrature negative). DISPOSITION: enumerated in the amendment (A2
item 3).

## RE-SCOPE (MAJOR; no enforcement machinery)
Per-lane anchoring is doc-only: no code enforces anchor-before-next-lane or
push capability. Code not broken for cooperative operation; the DEFECT is a
sealed artifact asserting a guarantee the code does not provide. Re-scope
the docstring/S3 language to actual behavior; add ONLY the push-capability
pre-flight (a failing push after sealing reproduces the GPG wedge).
DISPOSITION: enumerated (A2 item 2).

## RECORD ONLY
R1: verification evidence existed in no artifact — DISPOSED: sealed
transcript V003_VERIFICATION_RETURN_SEALED_TRANSCRIPT_V001.md (2967717…).
R2: the 2e-11 piece pin certifies the DECLARED quadrature rule, not the
operator: measured rule bias on B up to 8.2e-8 (primary), 3.1e-8
(independent), inter-rule 7.9e-8 — ~3.5 orders under the cross-lane budget,
structurally invisible, affects nothing claimed; M rule error ~1e-14;
downstream entry only via a <= 0.13 shifting propagators <= ~1.6e-9,
cancelling in A5 identities. No rule/tolerance change; recorded so no later
artifact reads the pin as operator accuracy (the certified parent's B is
~4000x further from its defining integral than the pin suggests).
R3: binding V002 S1-1c ("every midpoint") implemented at the single stored
diagnostic midpoint per ell; derive lanes store one diagnostic connection
matrix and are frozen; narrowing recorded append-only (piece pins carry the
per-midpoint load).
DISPOSITION: R2+R3 recorded in the sealed amendment A3.

## Ordering
Fixes -> suites green -> fresh hostile verification (FIX-2 test must be seen
to exercise the real oracle) -> manifest v003 -> anchor -> reviewer re-audit
via Brian -> Brian's typed authorization -> production.
