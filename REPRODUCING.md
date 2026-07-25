# Reproducing the Program

## Read order for a cold start
1. `supervision/CONTINUATION_STATE.md` — the complete program state and arc.
2. `cleanroom_output/00_*` and `01_*` — the original sealed protocol and premise ledger.
3. `workspace/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` — the sealed gate definitions.
4. `workspace/STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.json` — premise/status ledger.
5. Any gate: its SPEC, then RESULT, then `.seal.sha256`.

## Verifying integrity
Every `.seal.sha256` is `sha256  filename` lines. From the containing directory:
    shasum -a 256 -c <name>.seal.sha256
The cleanroom corpus has a hash-chained manifest (`cleanroom_output/PRECOMPARISON_MANIFEST.sha256`).

## Environment
- Construction-lane scripts (`workspace/scripts/`): Python; most run with
  `python3 -I` (isolated). Historical runs used macOS system Python 3.9.6
  and a pinned 3.12.13 runtime. Stdlib-only by design where sealed
  (`decimal`/`fractions` for high precision; `mpmath` deliberately avoided).
- Supervision blind lanes (`supervision/blind_lane_scripts/`): Python 3.9+
  with numpy. These are the independent, target-blind reconstructions cited
  in the supervision returns; each is self-contained.
- Stage-8 evaluator: `supervision/stage8_battery_evaluator_v001.py`
  (stdlib-only; `--selftest` proves its fences fire).

## Discipline invariants a repetition must preserve
- Specs seal BEFORE execution (predictions frozen, hashed).
- Failures are reported, never repaired in place; supersession is append-only.
- No measured constant (alpha, CODATA) may be read, used, or compared
  before the final authorized stage. `alpha_computed = false` everywhere
  in this archive.
- Load-bearing numerics require independent fresh-context reproduction
  (commitment-first where values are undisclosed).
- Verdicts on the Stage-8 battery belong to the evaluator script alone.

## Deliberately excluded from this archive
Raw AI-session transcripts (construction lane). Reason: size, and they
contain historical contamination text with the target value — this archive
must remain target-free. The sealed corpus is self-contained without them.
