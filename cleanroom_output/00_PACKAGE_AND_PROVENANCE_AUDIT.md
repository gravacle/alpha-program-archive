# 00 — Package and Provenance Audit

Date: 2026-07-23 (run start)
Agent: Claude (Fable 5), acting as independent derivation agent and hostile reviewer per HANDOFF.md.

## Workspace boundary

- `pwd` resolved to `/Users/bgm/Documents/New project/_external_handoffs/fable_alpha_cleanroom`. Confirmed.
- All reads and writes in this run are confined to this directory. Writes occur only under `OUTPUT/`.
- No parent or sibling directory was inspected during this run. No internet access was used. No repository discovery was invoked from this workspace.

## Package integrity

- Symlink check: `find . -type l` → **0 symlinks**.
- Manifest verification: `shasum -a 256 -c MANIFEST.sha256` → **all lines OK, 0 failures**.
- Coverage check: manifest lists **103 files**; disk holds **103 files** (excluding `MANIFEST.sha256` itself). Set equality holds exactly (an apparent mismatch in the first comparison was a `./` prefix artifact in the comparison tooling, not a package defect; normalized sets are identical).
- **Zero undeclared files. Zero missing files.**

Gate A mechanical requirements: **PASS**.

## Control files read (in prescribed order)

`README_FIRST.md`, `HANDOFF.md`, `CURRENT_STATE.md`, `INPUT_CLASSIFICATION.md`,
`WORK_PLAN.md`, `ACCEPTANCE_GATES.md`, `OUTPUT_SCHEMA.md`, `FORBIDDEN_INPUTS.md`,
`HOLDOUT_POLICY.md`, `DEPENDENCY_POLICY.md`, `SOURCE_MAP.md` — all read in full
before any analysis or execution.

## Blindness disclosure (required; Gate A / FORBIDDEN_INPUTS)

- **Historical target blindness is not claimed and cannot be claimed.** The
  orchestrating agent is a pretrained model that knows measured physical
  constants, and the project's own documents state the historical program was
  target-aware. This run claims **process blindness only**: no measured
  coupling value is written, compared against, or used as a selector at any
  point prior to the (currently unauthorized) Stage 12 comparison.
- Additional disclosure specific to this run: the orchestrating agent's
  session context predates this handoff. Mitigation adopted: **all
  load-bearing audit and derivation lanes are executed by fresh subagents
  whose entire instruction context is this handoff directory plus the sealed
  workspace rules** (no session history, no external material). Their
  instructions explicitly forbid use of any measured constant as evidence or
  selector. The orchestrator's role is synthesis and gate-checking against
  the package's own documents.

## Authority classification adopted (from INPUT_CLASSIFICATION.md)

- `ALLOWED_INPUTS/` — inspectable principles/conditional results; inclusion
  does not promote adopted premises into derivations.
- `CURRENT_WORK/` — evidence to audit, not premises to assume; PASS labels
  are rechecked, not inherited.
- Sealed authority: `CURRENT_AUTHORITY_LEDGER_V013.json` is the last
  authoritative state; BID v011 and source-parent v003 artifacts are unsealed
  working lineage.
- Least-favorable-status rule adopted for all prose/status/executable
  disagreements.

## Non-negotiable status at run start (carried forward unchanged)

```text
alpha_computed = false
physical_Thomson_stiffness_computed = false
complete_Q_spec_sealed = false
proof_authorized = false
```

## Run structure

Five parallel sealed audit lanes (fresh-context subagents):

1. Premise ledger over the 8 `ALLOWED_INPUTS` files → feeds `01_PREMISE_LEDGER.md`.
2. Authority reconciliation of `CURRENT_STATE.md` against `CURRENT_WORK/provenance/`
   (including seal verification and execution of the V013 audit scripts)
   → feeds `02_CURRENT_STATE_RECONCILIATION.md`.
3. BID v011 specification audit against the HANDOFF's eight BID obligations.
4. Source-parent physics lane: SP08 closure-item accounting, SP09 family
   enumeration state, execution and Gate-D inspection of the negative gates
   (action underdetermination v001; magnitude nonderivation v003).
5. SP14 runtime lane: v011 allowlist failure diagnosis, slice sufficiency,
   rerun attempt if and only if the copied slice suffices.

Lane results are synthesized into the numbered OUTPUT documents. No coupling
calculation occurs before Stage-1 completion, per WORK_PLAN.md.

## ADDENDUM — Mid-audit external workspace mutation (recorded, not repaired)

During the sealed audit lanes' execution, a process external to this run
renamed `ALLOWED_INPUTS/` to `AUDIT_ONLY_ADOPTED_INPUTS/` (observed
independently by two lanes). Effects and handling:

- All 8 relocated files remain **byte-identical** to their MANIFEST.sha256
  hashes (verified RELOCATED-OK); 95/103 manifest lines verify at their
  original paths; the 8 `./ALLOWED_INPUTS/*` lines fail at path level only.
- The initial full-manifest verification in this document (103/103 OK)
  predates the rename and was accurate when run.
- No lane modified any input file; this run's only writes are under
  `OUTPUT/`. The rename was not performed by this run and has not been
  reversed by it (inputs are treated as immutable — including their
  mutations, which are evidence).
- Consequence: path-level provenance is broken until a curator reissues the
  manifest or reverses the rename (DEPENDENCY_REQUEST item 11).
  INPUT_CLASSIFICATION.md still refers to the old directory name.
- Interpretation: the workspace was concurrently writable by another agent
  during this run. That is a process finding about the environment, recorded
  here for the curator; all load-bearing conclusions were verified against
  content hashes, not paths.

## Final status of this run

`BLOCKED` — see STATUS.json, 05_ALTERNATIVE_EXHAUSTION.md, and
NEEDS_THEORY_DECISION.md. The precomparison manifest seals the OUTPUT set;
no coupling was computed; no measured value was consulted.
