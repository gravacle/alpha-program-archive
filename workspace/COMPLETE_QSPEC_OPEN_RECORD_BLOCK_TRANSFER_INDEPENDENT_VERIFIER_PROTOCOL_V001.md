# Complete-Qspec Open-Record Block Transfer Independent Verifier Protocol v001

Date: 2026-07-25

## Independent test

Verify the sealed open-record block theorem with:

```text
source dimension       2
R1 dimension           2
R2 dimension           3
initial cross-operator full-rank and non-Hermitian
U_1 support            {source,R1}
U_12 support           {source,R1,R2}
U_2 support            {source,R2}
```

Use independently generated plus/minus random unitaries. Evolve the full
global cross-operator by explicitly embedded matrices, then compare its
final source partial trace with the event-driven block construction.

Require relative Frobenius disagreement below `1e-12`.

Independently validate the last-incidence schedule and require the
predeclared early close of `R1` to be rejected.

## Verdict

Return:

```text
INDEPENDENT_OPEN_RECORD_BLOCK_TRANSFER_MAP_CONFIRMED
```

only if every check passes. No coupling or protected physics status may
advance.
