# Stage-8 T7 Primitive Connected-Lift Verifier Successor Note v001

Date: 2026-07-24

Fable correctly identified that the v001 local verifier formed its flat
residual array directly as zeros. Although the theorem and external
recomputation were correct, that local check did not independently exercise
the incidence construction.

The append-only successor
`scripts/verify_stage8_t7_primitive_connected_lift_v002.py` now:

```text
rebuilds every positive oriented edge at L=3,5,7;
uses a vertex indexing independent of the construction script;
computes each D^dagger J_r edge residual from its source, target, and
transport;
checks exact zero at the flat baseline; and
inserts one nontrivial edge phase as a negative control and requires a
strictly nonzero residual.
```

The sealed v001 bundle remains unchanged. The v002 verifier supersedes only
the local verification method, not the result or its external adjudication.

All protected flags remain false.
