# Stage 8 Seam-10 Narrowing Adversarial Recalculation v001

Date: 2026-08-01  
Lane: CODEX 1  
Relay: 273  
Status: RESULT -- Bohm's seam-10 narrowing does not survive as stated

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 0. Lead

Two parts of the proposed narrowing fail.

First, the stated map

```text
T(w_S,w_R,w_E)=(w_R,w_S,-w_E)
```

does **not** preserve the kernel for all eight nullity-two triples. It preserves four and sends the
other four between two different kernel planes. The eight triples do have only four distinct kernel
planes, but the displayed uniform map is not the reason, and equality of kernel images does not identify
the underlying grading laws.

Second, `w_S+w_R+w_E=0` is not a sealed charge-conservation law for this carrier and is not a unique
selector on the full primitive family. It admits six of the forty-nine primitive triples, with nullities
`2`, `4`, `6`, and `8`. It leaves one kernel plane only after the attractive nullity-two sector has first
been selected. The governing obstruction explicitly rejects choosing a grading because it has the desired
dimension (`FULL_CARRIER_DILATION_SELECTOR_OBSTRUCTION_GATE_V001.md:100-103`).

Thus the exact arithmetic surviving Bohm's calculation is:

```text
eight primitive grading triples
    -> four distinct nullity-two kernel planes
    -> one plane after adding an unsealed channel-specific equation
```

The last arrow is a candidate restriction, not a derivation. Seam 10 remains open under its six-item
reopen condition.

## 1. Inputs and independent method

The governing artifact declares only a reduced three-factor carrier and expressly excludes the complete
spin, spacetime, gauge-transport, topology, ghost, and environment-spectrum data
(`FULL_CARRIER_DILATION_SELECTOR_OBSTRUCTION_GATE_V001.md:15-33`). It defines the real sixteen-dimensional
odd/odd Pauli-product span at `:35-49`, the candidate grading `Z_w` and commutator condition at `:51-68`,
and the primitive bounded census at `:87-103`.

I did not call, import, or translate the project audit. I independently:

1. constructed the sixteen `8 x 8` Hermitian Pauli products;
2. formed every coefficient of `[G,Z_w]` over the Gaussian integers;
3. split real and imaginary parts to obtain a real integer linear map;
4. computed rank and nullspace by exact rational row reduction; and
5. enumerated all primitive triples in `[-2,2]^3`, excluding zero and identifying overall sign.

There are exactly forty-nine representatives. The independently obtained nullity distribution is

```text
nullity 0: 22
nullity 2:  8
nullity 4: 12
nullity 6:  4
nullity 8:  3
```

This reproduces the sealed census at `FULL_CARRIER_DILATION_SELECTOR_OBSTRUCTION_GATE_V001.md:87-98`.

As an independent analytic cross-check, complexify the Pauli span and write each off-diagonal factor as
`sigma_s`, with `s` equal to `+1` or `-1`. A ladder monomial obeys

```text
[sigma_(s_S) sigma_(s_R) sigma_(s_E), Z_w]
    proportional to (s_S w_S + s_R w_R + s_E w_E)
```

up to the harmless overall commutator sign. Its Hermitian and anti-Hermitian combinations give the real
two-plane when the signed sum vanishes. For an `I_E` or `Z_E` factor, the third signed term is absent.
This cross-check gives the same eight triples and four planes.

## 2. Claim 1 -- half true, stated map false

The exact grouping is:

| Kernel plane | Primitive weight representatives |
|---|---|
| `sigma_+(S) sigma_-(R) sigma_-(E) + h.c.` | `(2,1,1)`, `(1,2,-1)` |
| `sigma_+(S) sigma_-(R) sigma_+(E) + h.c.` | `(2,1,-1)`, `(1,2,1)` |
| `sigma_+(S) sigma_+(R) sigma_-(E) + h.c.` | `(2,-1,1)`, `(1,-2,-1)` |
| `sigma_+(S) sigma_+(R) sigma_+(E) + h.c.` | `(2,-1,-1)`, `(1,-2,1)` |

So `8 -> 4` is correct as a count of **kernel images**.

The displayed map fails on the negative-`w_R` half. One exact counterexample is

```text
w = (2,-1,1)
T(w) = (-1,2,-1) equivalent modulo overall sign to (1,-2,1)

kernel(w)    = span_R of sigma_+(S) sigma_+(R) sigma_-(E) and its phase partner
kernel(T(w)) = span_R of sigma_+(S) sigma_+(R) sigma_+(E) and its phase partner
```

These are different planes. Likewise, `T(2,-1,-1)` lands on the third plane rather than preserving the
fourth. Exact row-reduced subspace comparison gives `same` on four triples and `different` on four.

Nor is a physical source-record exchange licensed. The reduced source and record gradings are assigned
different meanings (`SOURCE_RECORD_GENERATOR_STRUCTURE_GATE_V002.md:15-33`), and the same artifact says
the reduced factorization is not derived from the complete carrier at `:23-26`. More directly, the sealed
invariant-form gate states that an exact chirality/record-plane swap is not derived because chirality and
a public pointer have different transformation laws, operational roles, and anomaly obligations
(`TYPED_CHARGE_CHIRAL_RECORD_INVARIANT_FORM_GATE_V001.md:101-105`).

Therefore the result has two distinct counts:

```text
distinct reduced kernel planes = 4
distinct unselected candidate grading laws = 8
```

Equality after applying `w -> kernel([.,Z_w])` does not supply an equivalence relation on physical grading
laws.

## 3. Claims 2 and 3 -- confirmed

### 3.1 Local `Z` conjugations

Exact coefficient-space conjugation by `Z_R`, `Z_E`, and `Z_R Z_E` preserves each of the four real
two-planes. Each conjugation changes only signs or the phase partner within a fixed ladder channel. None
maps one of the four planes to another. Claim 2 is correct.

### 3.2 Environment/witness support

For all eight nullity-two triples, exact row reduction gives zero coefficient on every basis element with
`I_E` or `Z_E`. Every surviving plane is supported only on `X_E` and `Y_E`. Claim 3 is correct on the
declared reduced carrier. It does not promote that carrier to the complete physical environment; the
governing artifact withholds that promotion at `FULL_CARRIER_DILATION_SELECTOR_OBSTRUCTION_GATE_V001.md:31-33`.

## 4. Claim 4 -- arithmetic true, charge-conservation narrowing false

Among the eight nullity-two representatives, exactly two obey the unsigned equation:

```text
(1,-2,1)
(2,-1,-1)
```

They have the same all-raising kernel plane. That arithmetic statement is correct.

It is not a standalone selector. Over the full forty-nine-member primitive census, the unsigned equation
admits:

```text
(0,1,-1)   nullity 4
(1,-2,1)   nullity 2
(1,-1,0)   nullity 8
(1,0,-1)   nullity 4
(1,1,-2)   nullity 6
(2,-1,-1)  nullity 2
```

The condition is therefore nonvacuous but nonunique. It returns one plane only after conditioning on
nullity two. That conditioning is not supplied by the proposed conservation equation and is the same
desired-dimension selection the governing gate warns against.

There is also a typing error in calling the unsigned equation charge conservation. For a ladder channel
with signs `s=(s_S,s_R,s_E)`, conservation under the candidate grading is the signed equation

```text
s_S w_S + s_R w_R + s_E w_E = 0.
```

Every one of the four kernel planes satisfies its own signed equation by construction, because every
candidate was obtained from `[G,Z_w]=0`. The extra unsigned equation is the special case
`s=(+,+,+)`. It selects the all-raising channel whose survival it is then used to announce. It is not an
independent test of the four channels.

The sealed text keeps the relevant notions separate:

- `FULL_CARRIER_DILATION_SELECTOR_OBSTRUCTION_GATE_V001.md:66-68` says these finite commutators are not
  the axial Ward identity.
- `SOURCE_RECORD_GENERATOR_STRUCTURE_GATE_V002.md:73-83` calls combined-grading conservation conditional
  and says it is not derived from closed boundary accounting.
- The corpus's actual compact vector-`U(1)` charge treatment uses a source-sector generator `Q`, not the
  three weights, and states that charge conservation alone does not reduce the family further
  (`BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md:11-39`).

### Search for the proposed law

I searched four roots: the current cleanroom, the separate `cleanroom_output`, the parent gravity/EM tree,
and `alpha_supervision`. The fixed-string and bounded-regex queries covered
`w_S + w_R + w_E`, variants containing all three weight symbols, `charge conservation`,
`charge-conserv*`, and source/record swap/exchange/interchange language. Exclusions were
`a32_holdout/custodian_private/` (never entered or listed), `.git`, `node_modules`, paper/raw/external
source stores, seal sidecars, binaries, and media.

The exact unsigned equation occurs only in the unverified Q-178 register entry and the relay that asks for
this check. It occurs in no cleanroom or `cleanroom_output` authority and in no parent-tree physics
artifact. The nearest sealed conservation laws are the distinct conditional combined-grading and compact
vector-`U(1)` statements quoted above.

## 5. Relation to the automorphism adjudication

The four-plane count is not itself an automorphism-forcing result. It is the image size of the map

```text
weight triple -> commutant kernel plane.
```

Passing from eight weights to four images forgets which grading law produced an image. This is compatible
with the deflation principle in
`STAGE8_AUTOMORPHISM_FORCING_MECHANISM_ADJUDICATION_EINSTEIN_V001.md:99-126`: an invariance or quotient
returns an invariant subspace or orbit quotient, never a selected value. Here there is not even a sealed
physical group action implementing the proposed identification.

The adjudication's ratio-annihilation result at `:120-123` does not transfer: the present datum is a kernel
plane, not a ratio. The transferable conclusion is only the quotient/value distinction. Four images are
still four, and the quotient does not choose among them.

## 6. Reopen condition

The six-item reopen condition requires the physical environment degrees; their Lorentz, vector-`U(1)`,
CPT, and axial/inflow transformations; the full operator space and invariant positive forms; a unique ray;
the closure spectrum and cell interval; and the record channel plus chiral-odd self-energy from the same
unretuned matrix elements (`FULL_CARRIER_DILATION_SELECTOR_OBSTRUCTION_GATE_V001.md:141-155`).

The unsigned equation derives none of those inputs. At most it is a candidate restriction on a previously
declared reduced census. It is strictly weaker than the exact reopen condition.

## 7. Typed result

```text
sealed_nullity_census_independently_reproduced = true
nullity_two_weight_count = 8
distinct_nullity_two_kernel_plane_count = 4

claim1_four_distinct_kernel_planes = true
claim1_stated_exchange_map_preserves_all_eight_kernels = false | TYPE-R |
  test: exact rational row-reduced subspace comparison; four SAME, four DIFFERENT
source_record_environment_exchange_symmetry_derived = false | TYPE-U |
  would-build: a complete-carrier transformation theorem respecting the distinct source, record,
  and environment roles

claim2_ZR_ZE_conjugations_preserve_each_kernel_plane = true
claim3_nullity_two_environment_support_is_XY_only = true
claim4_two_nullity_two_triples_have_unsigned_zero_sum_and_share_one_plane = true

unsigned_zero_sum_is_unique_on_full_primitive_family = false | TYPE-R |
  test: exact enumeration returns six triples spanning nullities 2, 4, 6, and 8
unsigned_zero_sum_physical_law_found = false | TYPE-S |
  roots: current cleanroom; cleanroom_output; parent gravity/EM tree; alpha_supervision |
  exclusions: custodian_private; .git; node_modules; paper/raw/external stores; sidecars; binaries; media |
  queries: exact and bounded variants of all three weight symbols plus charge-conservation and
  source/record-exchange terms
charge_conservation_cuts_seam10_to_one = false | TYPE-R |
  test: the extra equation selects the all-raising signed channel and is nonunique on the full family

distinct_candidate_grading_laws_remaining = 8
unique_full_carrier_coupling_ray_derived = false | TYPE-U |
  would-build: the governing six-item reopen package
seam10_obstruction_discharged = false | TYPE-U |
  would-build: the governing six-item reopen package
```

## 8. Bearing symbol collisions

`G` here is the reduced Hermitian generator, not Newton's constant. `E` is the declared edge/witness
factor, not energy. `R` labels the record factor, not a radius. No identity involving those other uses is
transported into this calculation.

alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
