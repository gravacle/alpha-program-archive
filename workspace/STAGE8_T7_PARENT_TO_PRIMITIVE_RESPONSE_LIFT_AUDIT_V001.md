# Stage-8 T7 Parent-to-Primitive Response-Lift Audit v001

## Verdict

```text
T7_BLOCKED_PARENT_TO_PRIMITIVE_RESPONSE_LIFT_UNDERIVED
```

T7 cannot currently pass. The finite connected parent and outgoing record
GNS are derived, but the sealed lineage does not derive the scalar,
normalized connected amplitude required for the response Hessian.

## Type obstruction

Projecting a connected source-record evolution onto completed record
alternatives leaves an element of `End(H_source)`. It does not produce a
complex scalar. A further source/final-boundary closure is required.

The existing authority explicitly leaves the normalized interacting CTP
amplitude, connected many-record amplitude, volume-uniform zero-free
neighborhood, connected linked-cluster density, and complete
parent-to-outgoing map open.

## Constructive non-uniqueness witness

For one fixed two-level source state `rho=I_2/2` and
`T(theta)=diag(exp(i theta),exp(-i theta))`, two standard normalized closures
of the same source operator are:

```text
Z_L(theta)   = Tr(rho T(theta))                   = cos(theta)
Z_CTP(theta) = Tr(T(theta) rho T(theta)^dagger)  = 1
```

Both equal one at `theta=0` and are zero-free in a neighborhood of zero, but

```text
[-log|Z_L|]''(0)   = 1
[-log|Z_CTP|]''(0) = 0.
```

Thus completed-record semantics and the finite parent alone do not select
the response Hessian. Choosing one closure during Stage-8 execution would
be a new theory choice, not a computation from the sealed battery.

## Closure condition

Before T7 can be rerun, derive and forward-seal a parent-to-primitive
response lift that fixes, without a coupling target:

1. the source/final-boundary functional or CTP branch prescription;
2. the completed-record effect and its normalization;
3. the map from the F1 connection tangent into the connected parent;
4. a volume-uniform zero-free neighborhood;
5. a local linked-cluster density; and
6. equality of its intensive Hessian with the declared Duhamel covariance.

The lift must reduce to the pinned one-handle completed-record amplitude.

## Authority custody

- `primitive_amplitude`: `6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb`; disclosures verified = `true`
- `monoidal_extensivity`: `451550c3825288d699db35c7289e408e8314ad042450253b58f32722c4ead46b`; disclosures verified = `true`
- `composition`: `b5a60c354d05e84e91d4f1fbeb45c3bce83776c59df7fc307e65ef2a529d5287`; disclosures verified = `true`
- `finite_parent`: `345d447eaf6d730caa6fa655b92a7b0cd93a68b5f86e0c8929cf969f40aeb7cb`; disclosures verified = `true`
- `outgoing_gns`: `10909b5c21e73ecf655462339a27bd645b8d35e3ad11fb6f8cb204c601992995`; disclosures verified = `true`
- `stage7_candidate`: `5026afb89b52ead9f309168cb2fa4f06b81039f8dd01b8940f40e64aad679a7e`; disclosures verified = `true`
- `stage8_spec`: `ddb36cbfe4edfc2a0520e9ae58063295214c64afed5cad5a64e9f311826358f5`; disclosures verified = `true`

## Protected status

```text
kappa_record_computed = false
physical_charged_amplitude_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
