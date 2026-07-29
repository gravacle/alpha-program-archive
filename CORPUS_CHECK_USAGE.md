# Corpus Check Usage

`corpus_check.py` is the durable process instrument for the archive. It reports and blocks process defects; it never rules, adopts, retires, repairs, seals, or computes physical values.

Common commands:

```text
python3 corpus_check.py --report
python3 corpus_check.py --gate
python3 corpus_check.py --selftest
python3 corpus_check.py --report --check seal_integrity,fingerprint_currency
python3 corpus_check.py --gate --skip-check deploy_state
```

Modes:

- `--report` is the default. It prints a human-readable report and exits 0.
- `--gate` exits nonzero on RED checks and on YELLOW count growth above `corpus_check_baseline_v001.json`.
- `--selftest` runs the checker under normal Python and `python3 -O` and fails if the verdict changes.

The local archive pre-commit hook runs:

```text
python3 corpus_check.py --gate --skip-check deploy_state
```

The hook is LOCAL AND NOT CLONED. It is a convenience guard for this checkout only. The committed script and baseline are the durable instrument; cloned checkouts must install their own hook or run the script directly. `deploy_state` is skipped in pre-commit because a pre-commit checkout is intentionally not clean while a commit is being assembled; full deployment state is checked by running `python3 corpus_check.py --gate` after commit/push and by `deploy_status.sh`.

Fences:

- The checker refuses `a32_holdout/custodian_private/`.
- It reports defects; it does not edit, seal, or fix them.
- It computes no C-L3 coefficient, `kappa_record`, `kappa_Thomson`, alpha, `x`, `rho`, or `T_R`.

`alpha_computed = false`; `proof_authorized = false`.
