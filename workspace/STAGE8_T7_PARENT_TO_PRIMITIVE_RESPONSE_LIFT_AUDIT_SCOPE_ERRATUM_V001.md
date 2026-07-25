# Stage-8 T7 Response-Lift Audit Scope Erratum v001

Date: 2026-07-24

## Correction

`STAGE8_T7_PARENT_TO_PRIMITIVE_RESPONSE_LIFT_AUDIT_V001.md` correctly
identifies an unresolved downstream `Q_spec` choice: a completed-record
compression of the source-inclusive parent does not by itself select a
unique scalar CTP/in-out amplitude.

That observation is **not** the Stage-8 primitive T7 blocker. Stage 8 is
restricted to `kappa_record`; the complete charged CTP amplitude is
explicitly downstream. The earlier audit therefore remains a valid
downstream warning but is superseded for T7 adjudication.

## Correct T7 question

The primitive T7 question is whether the derived one-cell completed-record
amplitude and local Duhamel generator have a unique connected many-record
lift with:

```text
a volume-uniform zero-free neighborhood;
a local linked-cluster thermodynamic density; and
an intensive Hessian equal to the declared Duhamel covariance.
```

The authoritative result is
`STAGE8_T7_CONNECTED_PRIMITIVE_RESPONSE_GATE_V001.md` and its executable
companions. No status flag is changed by this erratum.

```text
kappa_record_computed = false
physical_charged_amplitude_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
