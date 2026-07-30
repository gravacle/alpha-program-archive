# A32 SIX-ITEM PROPOSALS — written before ratification (2026-07-28, late night)

STATUS: proposals only. NOT a ruling. Written by the reviewer lane for principal ratification,
following the established pattern (the D >= 5 proposal itself came from the Codex lane).
Recorded BEFORE the principal was asked, so the record shows rationale preceding ratification.

ATTESTATION: no candidate outcome, registry content, or measured value was accessed or
evaluated in forming these proposals. Selection criteria are PROCEDURAL ONLY (enumerability,
version-pinnability, discretion-elimination, freeze-cleanliness). Registry and beacon are
specified by name/vintage/endpoint from general knowledge; the collector (fresh context,
under item-9 custodian commitments) is the first process that may touch registry bytes, and
endpoint drift falls to the fail-closed rules. alpha_computed = false; nothing here selects
by value; an empty eligible set under these choices FAILS CLOSED per the already-sealed rule
(V011:2011-2015) and that outcome is accepted in advance.

## Item 1 — Registry/API source

PROPOSAL: the NIST CODATA recommended-values table, 2022 adjustment, as a single
fixed-vintage machine-readable artifact (canonical ASCII table at
physics.nist.gov/cuu/Constants/Table/allascii.txt, or the equivalent versioned JSON if the
collector verifies it as the canonical form), retrieved once by the collector, full raw
bytes hashed (mechanical item 8), T_cutoff = the 2022 adjustment vintage itself.
PROCEDURAL RATIONALE: (a) exhaustive enumeration is trivially verifiable (~350 rows, one
artifact, one hash — the cleanest possible freeze; "exhaust every page" is discharged by
construction); (b) externally maintained, versioned by adjustment, stable identifiers,
values + uncertainties + units on every row; (c) the alpha datum and its deterministic
re-expressions are machine-excludable under the sealed eligibility rule, and CODATA's
published correlation structure makes "shares the alpha datum" checkable mechanically.
DISCLOSED RISK (accepted, fail-closed): the CODATA universe is heavily alpha-correlated;
after eligibility + computability filtering the eligible set may be EMPTY, which returns
A32_FAIL rather than a threshold or family renegotiation. That is the honest design.
ALTERNATIVE OFFERED: the Particle Data Group annual edition (versioned, machine API) —
larger universe, weaker overlap with any plausible BID prediction surface, much larger
contamination-audit surface, pagination nontrivial.

## Item 2 — External randomness beacon

PROPOSAL: drand (League of Entropy) mainnet as primary — canonical retrieval by round
number from the public HTTP endpoints (api.drand.sh and mirrors), round computed
deterministically from the frozen genesis time and period for the first round strictly
after PREDICTION-MAP-SEAL; value = the round's 32-byte randomness, hex, parsed verbatim.
FALLBACK (predeclared, no discretion): if the drand round is unretrievable from all frozen
mirrors for 24 hours, the NIST Randomness Beacon v2 pulse at the first whole UTC minute
after the same seal instant (beacon.nist.gov/beacon/2.0/pulse/time/<ms-timestamp>); if both
are unavailable for 72 hours, FAIL CLOSED (no third source may be improvised).
PROCEDURAL RATIONALE: drand is distributed (no single institution can be accused of
steering), round arithmetic is deterministic from frozen constants (zero retrieval
discretion), values are trivially parseable; NIST provides an institutionally independent
fallback with signed pulses. Beacon substitution beyond the frozen fallback chain is
A32_FAIL under sealed text (V011:2013).
COLLECTOR VERIFICATION CLAUSE: exact chain hash, genesis, period, and mirror list are
verified and recorded by the collector AT FREEZE EXECUTION, before PREDICTION-MAP-SEAL;
drift discovered later = fail closed.

## Item 3 — Same-alpha comparator class

PROPOSAL: the published standard-theory prediction class — for each candidate observable,
the standard QED/standard-model expression as published in citable literature BEFORE
candidate-universe construction, evaluated with the identical alpha input
(alpha(0) = 1/(4 pi kappa_Thomson), the frozen convention, V011:1661-1663) and identical
candidate metadata, at a perturbative order FROZEN PER FORMULA at preregistration, with no
candidate-specific fitted parameter, refit, channel coefficient, or post-selection
(verbatim prohibitions, V011:1987-1988). A candidate with no such published expression is
ineligible FOR THAT CANDIDATE (the draft's item-4 clause).
PROCEDURAL RATIONALE: this is the only class that makes the sealed structure-sensitivity
requirement meaningful — "BID and at least one preregistered comparator calibrated to the
same alpha must make distinct predictions" (V011:1991-1992) is precisely the statement that
BID differs from standard theory at the same alpha. Identical-prediction comparators are
A32_FAIL by sealed text (V011:2014).

## Item 4 — Calibration rule

PROPOSAL: ratify the draft's stated rule UNCHANGED (identical alpha input, identical
candidate metadata; refit / channel-specific coefficient / post-selection makes the
comparator ineligible for that candidate). The convention half is already sealed
(alpha_Thomson_convention_map_frozen = true, V011:2202); the draft rule adds nothing that
contradicts sealed text and its prohibition triplet is verbatim from V011.

## Item 5 — Distinctness threshold

PROPOSAL: ratify D >= 5 UNCHANGED, with the draft's formula
D = |mu_BID - mu_comp| / sqrt(sigma_BID^2 + sigma_comp^2 + sigma_meas^2) after unit
conversion and covariance projection (singular covariance fails eligibility unless a
projection rule was frozen beforehand), and the fail-closed empty-set clause (which is
independently sealed-required regardless of this ratification).
PROCEDURAL RATIONALE: the number is the one pure judgment; 5 is the conservative
conventional discovery-grade separation, proposed by the drafting lane, fixed before any
prediction exists. Nothing in the corpus constrains or contradicts it. The reviewer note
stands: lateness, not magnitude, is what voids the test.

## Item 6 — Observable family

PROPOSAL: ratify the draft's all-eligible rule UNCHANGED: ALL machine-enumerated registry
candidates satisfying the five sealed eligibility conditions (V011:1983-1993) and
computability under the frozen prediction-map interface; NO human subfamily carved out
after registry collection (manual curation is a sealed stop-rule violation, V011:2088-2089).

## Execution path on ratification (per the decision sheet, unchanged)

Principal rules per item -> A32_FREEZE_V001.md written in this directory with the six
rulings + the thirteen mechanical items -> sidecar .seal.sha256 in the same act ->
numbered relay paste prepared for the construction lane to write the freeze fields into the
V011 specification bundle (this lane does not write to the workspace) -> STAGE8_LANE_STATUS
index and CONTINUATION_STATE record in the same act. Ladder-grade flag flips remain blocked
on the unimplemented independent evaluator (RD-22) and are NOT claimed.

## CLARIFICATION APPENDED BEFORE RATIFICATION (principal's challenge, 2026-07-28)

The principal challenged whether alpha-correlation-based exclusion enforces a questionable
measure, since a correct record-structure theory predicts its discriminating signal exactly
on alpha's geometric surface. RESOLUTION, on the record before any ruling:

1. The sealed eligibility rule (V011:1985-1990) is a DATA-LINEAGE exclusion, not a proximity
   exclusion: a row is out only if its tabulated value IS the alpha datum or a deterministic
   re-expression (arithmetic on the alpha measurement, not an independent measurement).
   Physically alpha-adjacent, independently measured observables (e.g., electron g-2) are
   ELIGIBLE, and are exactly where structure-sensitive candidates are expected to live. The
   sealed rule survives the challenge.
2. WITHDRAWN: the reviewer's floated optional "frozen correlation ceiling" (previous
   message, not in this document's proposals). A statistical-correlation ceiling is a
   proximity measure and would systematically exclude the theory's expected signal region —
   precisely the principal's objection. The published correlation matrix remains legitimate
   only as a detector of deterministic sharing (|r| = 1 by construction), never as an
   eligibility knife.
3. RETAINED AS DISCLOSURE, NOT RULE: CODATA adjusted values presume standard-theory
   relations (conservative lean, to be disclosed in the freeze instrument). No extra
   exclusion rule is proposed for it.
4. CONSEQUENCE FOR ITEM 1: under lineage-only exclusion the CODATA emptiness risk narrows to
   the computability + structure-sensitivity filters (D >= 5), where it belongs. The pool is
   otherwise taken exactly as it is.
