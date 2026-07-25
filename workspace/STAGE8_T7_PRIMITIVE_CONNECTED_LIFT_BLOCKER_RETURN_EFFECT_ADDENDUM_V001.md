# Stage-8 T7 Primitive Connected-Lift Blocker Return: Effect Addendum v001

Date: 2026-07-24

This addendum strengthens
`STAGE8_T7_PRIMITIVE_CONNECTED_LIFT_BLOCKER_RETURN_V001.md`.

The zero-baseline obstruction applies not only to completed endpoint rays but
to every positive completed-record effect and subordinate instrument.
No-output-without-record gives:

```text
<r_L|E_L|r_L>=0.
```

For `E_L>=0`, this forces `E_L r_L=0`. If `K_L^dagger K_L<=E_L`, it also
forces `K_L r_L=0`. Since the flat periodic evolution fixes `r_L`, neither a
POVM effect nor a Kraus/instrument boundary can provide the missing nonzero
baseline.

The primitive repair must therefore change the connected open-boundary
construction itself. Generalizing the final boundary from a ray to an effect
does not reopen T7.

Sealed supporting bundle:

```text
b038fe156ea43ebdb17f96225ad12f5d7dfd2c7221bc71c1de35def8dee9fc8a  stage8_execution/t7_primitive_connected_lift/T07_COMPLETED_EFFECT_ZERO_BASELINE_V001.seal.sha256
```

All protected flags remain false.
