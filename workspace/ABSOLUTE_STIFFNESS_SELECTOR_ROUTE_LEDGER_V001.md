# Absolute Stiffness Selector Route Ledger v001

## Hard solve-alpha gate

With primitive unit charge fixed,

```text
S_Maxwell
  = -(hbar K_R/4) integral sqrt(-g) F_mu_nu F^mu_nu d^4x,

alpha = 1/(4 pi K_R).
```

The construction has not computed alpha if an arbitrary finite

```text
delta S = -(hbar c/4) integral sqrt(-g) F_mu_nu F^mu_nu d^4x
```

remains admissible at the matching scale.

This is the terminal anti-self-deception test. Algebraic reproducibility,
compact charge, a small residual, a fixed-point root, or agreement with a
known endpoint cannot override it.

## Route decisions

### Symmetry, compactness, and charge quantization

```text
result:
  pointwise projective U(1) stabilizer and integer character lattice;

failure as absolute selector:
  c F^2 preserves every current symmetry and compact period;

status:
  CLOSED AS KINEMATICS;
  RETIRED AS A STANDALONE K_R SELECTOR.
```

### Allow/require record threshold

```text
result:
  determines whether declared support can become a record;

failure as absolute selector:
  does not by itself determine field multiplicities, fluctuation weights,
  a finite coincident extension, or the coefficient of F^2;

status:
  RETAINED AS A SUPPORT/CELL CONSTRAINT;
  RETIRED AS A STANDALONE K_R SELECTOR.
```

### Topology, anomalies, and electric-magnetic duality

```text
result:
  can quantize charge, flux, parity-odd levels, and constrain spectra;

failure as absolute selector:
  arbitrary parity-even c F wedge *F remains allowed;
  simple modular fixed points select order-one coupling and require an
  independently derived duality/vacuum choice;

status:
  SUPPORTING CONSTRAINTS ONLY.
```

### Spectral action

```text
result:
  can derive Maxwell form and relative gauge-normalization relations from a
  fully fixed spectral triple;

failure as current absolute selector:
  the record Dirac operator, finite representation, spectral measure,
  overall normalization, Lorentzian continuation, and renormalization
  condition are not derived;

status:
  DEFERRED SUBROUTE OF THE COMPLETE INDUCED-ACTION PROGRAM.
```

### Coupled gravity-charged fixed point

```text
result:
  a complete flow can select alpha_* = f_grav/b_ch;

failure as current selector:
  neither coefficient, the local charged field, the fixed-point
  universality class, nor Thomson matching is currently derived;

status:
  RETAINED AS THE LATER DYNAMICAL SELECTOR/CROSSCHECK;
  NOT AN INPUT TO THE MICROSCOPIC ACTION.
```

### Complete induced record action

```text
required result:
  one forward-sealed parameter-free gravity-plus-record Q_spec;
  a derived physical local charged connection;
  a derived zero-bare/compositeness condition or an equivalent theorem
    excluding an independent c F^2 term;
  complete charged spectrum, measure, regulator, and finite extension;
  an induced K_R and coupled flow with no adjustable finite normalization;
  full threshold matching;

status:
  ACTIVE ROUTE.
```

## Active sequence

```text
1. State and seal the new fundamental-boundary-record action principle.
2. Derive the local record bundle and decide whether its connection is
   auxiliary/composite or independently dynamical.
3. Derive the complete charged record/source carrier, including statistics,
   multiplicities, and thresholds.
4. Derive one parameter-free microscopic action and complete Q_spec.
5. Prove that no independent finite c F^2 deformation is admissible.
6. Evaluate the exact induced response and coupled RG flow.
7. Match to the Thomson limit.
8. Reveal alpha only after all preceding gates pass.
9. Evaluate the preregistered independent running/endpoint prediction.
```

## Current status

```text
active_route = COMPLETE_INDUCED_RECORD_ACTION_PLUS_DYNAMICAL_FIXED_POINT
complete_parameter_free_action_sealed = false
finite_c_F2_deformation_excluded = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
