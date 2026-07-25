# 02 — CURRENT_STATE Reconciliation

Method: 37 factual assertions in CURRENT_STATE.md were checked against the
copied evidence by a sealed lane. All 18 `.seal.sha256` files verify OK.
All 16 package files covered by the V013 audit's pin table hash exactly to
their pinned digests.

## Confirmed (selection; full list in lane record)

- V013 ledger seal verifies; stored status string exact
  (`PASS_AUTHORITY_V013_PINNED_SNAPSHOT_SEMANTIC_DELTA_ALPHA_BLOCKED`); no
  later sealed authority exists; BID v011 / source-parent v003 confirmed
  unsealed working lineage.
- All stored V013 count fields match recomputation from the audit script's
  own pinned constants; all seven ledger sections match the pinned maps;
  `execution_state_additions` equals `derive_execution_state_additions()`
  over the four subordinate JSONs actually present.
- Claim 2's five narrow results are present in sealed artifacts and mutually
  consistent (gate .md == result JSON == audit pins), including rank 12 /
  kernel 4, conditional 2-D exchange kernel, 2-D commutant / 1-D quotient,
  πħ/2 budget under the adopted onset rule, and the stored holonomy form.
- Claims 3–8 match their cited artifacts exactly (tier2 historical-scope
  flags; bridge-gate deductions; relative-marker non-physicality; frozen
  fidelity candidate; adopted bundle/connection/K_bare=0; disclosed charged
  matter).
- Claim 9 exact: closure gate contains exactly SP01–SP18; blocked rows are
  exactly SP08, SP09, SP14; 15 scoped passes; SP08/SP09 blocker text matches
  item-for-item.
- Retired-routes list fully supported (≈4 of 11 via review-ledger
  must-not-regress rows; the C4-carrier family via tier2 RETIRED_* entries;
  identity-trace and cosmological items via ACCEPTANCE_GATES / FORBIDDEN_INPUTS).
- Path warning confirmed: the v012 snapshot pins 6 absolute paths through the
  canonical long-form path; treated as provenance, not rewritten.

## Contradicted (least-favorable rule applied)

1. **"Physics audits converted away from load-bearing Python assert use" is
   false as a blanket claim.**
   `scripts/audit_bid_primitive_action_multiplier_v001.py` (lines 20, 28, 31)
   and the **sealed** `scripts/audit_source_record_closure_action_underdetermination_v001.py`
   (lines 38–54) retain load-bearing asserts, which vanish under `python -O`.
   The closure-gate enforcement covers only its 26 expected-output scripts
   and includes neither. (The magnitude-nonderivation v003 script is clean:
   0 asserts, `require()`-based, with an optimized-python test.)
2. **Package-path integrity broke mid-audit** (external mutation): see
   00 addendum. `ALLOWED_INPUTS/` was renamed to
   `AUDIT_ONLY_ADOPTED_INPUTS/` by a process outside this run while lanes
   were reading. All 8 relocated files remain **byte-identical** to their
   MANIFEST hashes (RELOCATED-OK); 95/103 manifest lines verify at original
   paths; the 8 path-level lines fail. INPUT_CLASSIFICATION.md still names
   the old section. Contents intact; path-level provenance broken.

## Unverifiable in-package (sealed claims, not re-derivable here)

- The V013 **PASS as an executable fact**: `audit_current_authority_v013.py`
  exits 1 here (requires a 54-role authority tree; 34 role files absent; 24
  of 40 pinned artifact targets absent). The stored PASS is a copied,
  internally-consistent artifact only.
- The four narrow results **as computations**: their per-gate audit scripts
  are not in the package; the authority audit verifies them only against
  expected-result dictionaries encoded in the audit script itself.
- `test_current_authority_v013.py` under bare `python3` runs **zero tests**
  (pytest-style, no `__main__`) — false-pass hazard; under pytest it fails
  on the flattened layout.
- The v011-allowlist-failure lineage and "supervisor edited after failure":
  attested only by a README status line and two filenames; the failing
  verifier output, v011 allowlist artifact, and any edit history are absent.
- V010 parent chain: known only as pinned constants inside the V013 audit.
- Runtime gate specification document is v010; snapshot/launcher/validator
  are v012; no v012 specification document is in the package.
