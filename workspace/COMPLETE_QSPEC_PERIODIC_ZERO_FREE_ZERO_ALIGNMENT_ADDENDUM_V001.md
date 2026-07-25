# Complete-Qspec Periodic Zero-Free Zero-Alignment Addendum v001

Date: 2026-07-25

## Hostile-review finding

The promotion spec's analytic perturbation is based at the unretracted
Taylor branch at `z=0`, while the accepted dyadic `T0` certificate uses the
canonically polar-retracted zero-history cell. Therefore

```text
epsilon + ||T0-A||
```

omits the zero-alignment offset unless both zero objects are explicitly
related.

No promotion execution occurred before this finding.

## Required repair

Construct, on the same repaired reachable support:

```text
T_an(0) =
  reduced_transfer(
    Taylor analytic zero composite,
    repaired zero composite
  ).
```

Its canonical binary64-hex hash must be:

```text
5e59e660c1b0859e915f86258944972b0ecf5e939c4ca264158edc3eb95aec39
```

Using exact dyadic Arb balls, reconstruct

```text
P = |t><t|/<t|t>,
R = Q T0 Q,
A = P+R
```

and certify directly:

```text
||T_an(0)-A||_2 < 1e-10.
```

Only that combined bound authorizes the promotion script to retain

```text
eta = epsilon + 1e-10.
```

The floating diagnostic size of the omitted transfer-to-transfer offset is
not proof and may not carry the verdict.

All fixed coupling, alpha, and proof-authorization flags remain false.
