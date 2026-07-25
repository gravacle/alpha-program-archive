# Primitive Reversible Record-Write Principle v001

## Logical status

This is a target-independent Level-1 record-dynamics principle. It replaces
the rejected use of a balanced comparator autocorrelation as a durable record.
It is adopted as the primitive one-bit write rule, not claimed as a theorem of
unitarity alone.

## Primitive write task

Let `H_S=C^2` carry the two source alternatives and `H_R=C^2` carry a ready
record state `|0_R>`. A primitive durable write must:

```text
leave the source alternative unchanged;
map the two alternatives to orthogonal conditional record states;
use no additional carrier;
be reversible before downstream environmental tracing;
and complete during one physical write interval tau_R.
```

After endpoint phases and labels are calibrated, the required action on the
ready subspace is

```text
|0_S 0_R> -> |0_S 0_R>,
|1_S 0_R> -> |1_S 1_R>.
```

The adopted no-surplus reversible extension is the controlled endpoint swap

```text
U_write
  = P_0^S tensor I_R
    + P_1^S tensor X_R.
```

This is the two-state nondemolition measurement interaction. It creates
orthogonal conditional records for arbitrary source amplitudes; no balanced
source preparation is required.

## Principal integrated generator

On the active `P_1^S` block,

```text
X_R = exp[-i (pi/2)(I_R-X_R)].
```

The adopted shortest principal-log implementation over a constant interaction
window gives

```text
H_write
  = (pi hbar/(2 tau_R))
    P_1^S tensor (I_R-X_R).
```

Other logarithm branches execute additional windings and are excluded by the
primitive shortest-write rule. Gauge-independent endpoint phases do not
change the record map.

At closure the interaction window ends. Persistence then requires the
post-write record generator and subsequent admissible interactions to preserve
the record projectors. Environmental redundancy is downstream amplification,
not part of the primitive unitary.

## Exact boundary of the adoption

The ready-subspace write requirement alone does not uniquely determine a
unitary on the unused input subspace. The controlled-swap extension and its
principal logarithm are the substantive adopted content of this principle.

The principle does not yet identify:

- which Dirac or field-history alternatives supply `P_i^S`;
- how the compact connection controls the write;
- the spatial causal cell and density;
- the left-right source return map;
- the physical value of `tau_R`;
- the induced Maxwell response.

## Status

```text
durable_record_defined_by_conditional_record_orthogonality = true
primitive_record_write_rule_adopted = controlled_endpoint_swap
balanced_source_state_required = false
principal_integrated_write_generator_fixed = true
record_write_rule_derived_from_unitarity_alone = false
field_history_control_projectors_derived = false
source_mass_derived = false
finite_response_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
