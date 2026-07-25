# NEEDS_EXTERNAL_EXECUTION — SP14 Terminal Runtime Assurance

The copied runtime slice is **insufficient** for an in-package SP14 terminal
run, on five independent grounds (verified by honest execution attempts, all
of which failed exactly where the pinning predicts; no seal was weakened):

1. **Layout**: the v003 supervisor computes ROOT/PROJECT_ROOT from its own
   path and requires `provenance/`, `scripts/`, `results/` trees that do not
   exist in this flat slice (verified: FileNotFoundError on the pinned
   snapshot path).
2. **Absolute-path pinning**: `primitive_step6_runtime_snapshot_v012.json`
   pins launcher/builder/gate under the original
   `gravity_emergence_evidence_program` tree (outside this workspace); the
   launcher hard-fails unless its own resolved path equals the pinned path.
3. **Sealed interpreter**: the pinned python3.12 at
   `~/.cache/codex-runtimes/...` (sha256 eb9d74b9…) plus 747/6597/2585
   hash-pinned runtime/site-package files are not in the package.
4. **Producer dependency set incomplete**: 14/25 documents and 21/26
   subordinate audit scripts required by the producer-manifest builder are
   absent from the handoff.
5. **Signing + host pinning**: detached signature requires
   `/opt/homebrew/bin/gpg` with secret key fingerprint
   18488605D44F65A9B57B610AA5F3A86512A04D61 and byte-exact host trust record
   (macOS 26.5 build 25F71, arm64, SIP enabled).

## Exact external command (single line, on the pinned host, from the
original project tree)

```
"/Users/bgm/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3.12" -I -S -B -X "pycache_prefix=/Users/bgm/Documents/Documents - Brian’s MacBook Pro/New project/gravity_emergence_evidence_program/provenance/primitive_step6_empty_pycache_v012" "<SOURCE_PARENT_DIR>/scripts/run_bid_source_parent_terminal_supervisor_v003.py"
```

where `<SOURCE_PARENT_DIR>` is the original source-parent working directory
whose `scripts/` holds the v003 supervisor (its exact name is not recorded
in the copied slice).

Preconditions enforced by the supervisor itself: sealed interpreter and
libpython hashes; launcher/builder/gate at pinned paths with pinned sha256;
byte-equal host trust record; empty pinned pycache dir; none of the 11
produced artifacts pre-existing under PROJECT_ROOT/{provenance,results}
(archive v011 leftovers first); environment free of PYTHONPATH/PYTHONHOME/
PYTHONSTARTUP/PYTHONINSPECT and DYLD_*/LD_*; gpg secret key available with
VALIDSIG verification. Expected success output: paths of
`bid_source_parent_sp14_terminal_v003.json` and `.asc`, then
`SP14_LOCAL_RUNTIME_ASSURANCE=PASS`, `source_parent_closure=false`,
`alpha_computed=false`.

## To make the v011 failure diagnosable (currently label-attested only)

Supply from the original tree: the v011-generation launcher/validator
sources, the v011 execution manifests and receipts, and the failed run's
stderr transcript. In-package findings meanwhile: the failure was
verifier-stage (both producer outputs are sealed, contract-complete, and
identical modulo `python_optimize` 0/1); the failure class is the sealed
import/open origin allowlist; the copied v012 chain is the post-v011 repair
and has never executed end-to-end; the post-failure-edited v003 supervisor
now agrees with the v012 validator except one strictly weaker
`cython_runtime` creator-origin check (consistency drift, not a new failure
source).

Executable assurance cannot promote any physical premise (SP14 is
physics-neutral); its completion would not alter the BLOCKED physics verdict.
