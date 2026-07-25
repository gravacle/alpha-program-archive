# Stage-8 T7 Completed-Effect Zero-Baseline Result v001

Date: 2026-07-24

## Verdict

```text
COMPLETED_EFFECT_ESCAPE_EXCLUDED
```

The primitive connected-lift obstruction is not limited to pure endpoint
rays.

Let `E_L` be any positive completed-record effect. The sealed
no-output-without-record rule gives:

```text
<r_L|E_L|r_L>=0.
```

Positivity gives the exact identity:

```text
<r_L|E_L|r_L>=norm(E_L^(1/2)r_L)^2.
```

Therefore:

```text
E_L^(1/2)r_L=0,
E_L r_L=0.
```

Because the flat periodic evolution fixes `r_L`, the completed effect has
zero baseline after evolution as well:

```text
E_L exp(-i tau_R B_L(0))r_L=E_L r_L=0.
```

For any completed-record instrument with Kraus operator `K_L` subordinate to
the effect, `K_L^dagger K_L<=E_L`, so:

```text
norm(K_L exp(-i tau_R B_L(0))r_L)^2
 <=<r_L|E_L|r_L>
 =0.
```

Thus neither a POVM effect nor a more general completed-record instrument can
provide the missing nonzero baseline. Relaxing no-output-without-record does
permit one, and the exact negative control confirms that this assumption is
load-bearing.

## Status

```text
pure_endpoint_escape_available = false
positive_effect_escape_available = false
completed_instrument_escape_available = false
connected_primitive_completed_endpoint_derived = false
connected_primitive_amplitude_derived = false
kappa_record_computed = false
alpha_computed = false
proof_authorized = false
```
