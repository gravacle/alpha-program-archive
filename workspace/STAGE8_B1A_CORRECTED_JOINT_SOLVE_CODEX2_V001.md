# STAGE 8 / 7A / [PLAN:B1a-10] — THE CORRECTED JOINT SOLUTION VARIETY

Lane: CODEX 2. Relay 807. All headline determinations are **CLAIMED** pending registrar cross-check.

## Lead determination

The corrected joint system is **NONEMPTY AND FREE**.

The relay-797 `(a2)` verdict reverses: after removing the duplicated frame conversion located in 805, component inheritance is the exact identity carrier. It passes incidence, integrability, the intrinsic quadratic, identity/composition, and the exhibited A1/A2 common-refinement equation. The orientation-weighted `(b2)` verdict does not reverse: its corrected target is `sgn(p) I_6`, and it still fails global refined-coboundary integrability with exact augmented rank `56>50`.

The complete corrected common-refinement system has a full-rank identity stratum of exact dimension

```text
1887.
```

The identity is a member, `(a2)` is that member, `(b2)` is not, and every solution obeying the section equation is curvature-nonzero on nonzero parent curvature. The maximal real stratum is the full-rank stratum; rank-deficient Gram strata impose additional minors and do not increase the dimension. Hence B1a lands **FREE, dimension 1887**, rather than forced or empty.

## 0. Preflight, authority, and correction boundary

| object | SHA-256 | result |
|---|---|---|
| `PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | digest and adjacent seal verified; read before task work |
| governing 805, `STAGE8_B1A_DIVERGENCE_LOCATE_CODEX2_V001.md` | `4f1db6c0835bc12e7f130125bdde38fb276a07fc8d4df8b8378ab80c23550a3f` | adjacent seal verified |
| tainted subject 797, `STAGE8_B1A_FULL_SOLUTION_SET_CODEX2_V001.md` | `78882cbe04c460bf7a7000277e3d24048c4639d3cdcaa6e37dd04050a8bfb5d9` | adjacent seal verified; prior verdicts not consumed |
| 786, `STAGE8_B1A_LIFT_FORCING_CODEX2_V001.md` | `3966fdb124c6fed887499ac56907510ed4bc5666be74f32f49f60875c61fc2f0` | adjacent seal verified |
| 794, `STAGE8_B1A_CARRIER_CROSSCHECK_NATURALITY_CODEX2_V001.md` | `614e20c8bfd1978a4273c831b76bd6145483876c975ea87f80ef31a589b8bdc7` | adjacent seal verified |
| 795, `STAGE8_B1A_COFRAME_HALF_DARIO_V001.md` | `590b3979d5a0fadfd570e3a73a13bb3a717d5450f7eb5c9f2e79f481039fc1e2` | adjacent seal verified |
| 753, `STAGE8_7A_SIMPLICIAL_COFRAME_DARIO_V001.md` | `d6f490b80e8d8775af9ee54095e34da03a4af01541736e2cb138f366c2caa75e` | adjacent seal verified |
| packet V011 | `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` | packet-manifest membership verified |
| common-refinement source, `stage8_execution/work/MAJORANT_PHASE2_O3_O7_PROOF_DRAFT_V001.md` | `08b91543fdb72f656c756ca5f8df8233b87eb5487284c7fd2170cba67f7e0e3b` | adjacent seal content verified |

Decisive spans:

| content | sealed span | span SHA-256 |
|---|---:|---|
| 805 exact corrected `L` and identity control | 805 `[3394,7301)` | `3bc21b8507b865986d265087743258a612a1f56fa88ceed3abdcc1cc728fceb8` |
| 805 corrected A2 family | 805 `[8804,11290)` | `653206f4d66d55c5903ad8d0691d15b8f25f6a5ba568bfbf626200022729aae8` |
| typed connection–coframe refinement carrier | 786 `[13746,14962)` | `438270addbc1d612d6707a3d371ee4e9102bde05567f7a1969a3a18b4ea6a88c` |
| independently rebuilt A0/A1/A2 incidence carrier | 794 `[3953,7622)` | `cbac23d7b14d4902042b559cda69e210036da81a8260dc481618dfcc3bdc62fd` |
| coframe candidates and intrinsic quadratic | 795 `[4034,7537)` | `51603bf6059bfbf1f60acf9c94fda11d1e907d807f1f8a407a991aec39ac235f` |
| O1 identity/composition | 795 `[7537,9127)` | `be8c0f9c983bfbebda7e9a7791b8cd6e376fba61aebc4393fc131b60e42bb7e0` |
| exact O4 common-refinement conjunct | packet V011 `[47025,47247)` | `9ff6852634e78e6d886896c27bce16b4ec9e092620642a86bae00848df2f276c` |
| exhibited 384-cell common refinement | MAJ `[19632,19996)` | `b3c67e8c433385a4cb519c2f564649e98b2a9686491487db663592b4b48d6b43` |

`QUESTIONS_SETTLED_REGISTER_V001.md` was grepped as the state brief requires. Q-713's correction boundary was adopted. Dario's relay-806 artifact was not opened, searched, or consumed; its receiver work remains lane-opposite and untouched. PE-1 through PE-7 were pointer-known only, unopened, unconsulted, and carry zero verdict weight.

## 1. AS1 — corrected recheck of `(a2)` and `(b2)`

### 1.1 Corrected target representation

Keep 805's exact conventions: 65 lexicographically ordered comparable edges; 24 Freudenthal simplices in permutation order; bivectors `(01,02,03,12,13,23)`; and

```text
B : Q^65 -> Q^(24*6)
```

given by the exact barycentric-gradient formula with factor `2`. Since `B` already returns coordinate components, the corrected targets are

```text
T_a2,p = I_6,
T_b2,p = sgn(p) I_6.
```

The 797 targets involving an additional `W_p` conversion belong to the tainted pipeline and are not reused.

### 1.2 Exact ranks and parent section

Exact fraction RREF gives

| system | base rank | augmented rank | verdict |
|---|---:|---:|---|
| `B a=T_a2` | 50 | 50 | globally integrable |
| `B a=T_b2` | 50 | 56 | inconsistent for all six input directions |
| stacked carrier `[B;C] a=[T_a2;I_6]` | 50 | 50 | integrable and a parent section |
| stacked carrier `[B;C] a=[T_b2;I_6]` | 50 | 56 | inconsistent |

For `(a2)`, an exact edge representative for each input pair `(mu,nu)` is

```text
a_(mu,nu)(u,v)
  = (1/2) [u_mu(v_nu-u_nu)-u_nu(v_mu-u_mu)].
```

Entrywise substitution returns

```text
B_p a = I_6                 for p=1..24,
C a   = I_6,
(1/24) sum_p I_6^T I_6 = I_6.
```

The same constant-form formula restricts and composes on A0, A1, A2, and the 384-cell common refinement, so the identity and composition equations are exact. Thus:

```text
a2 = SURVIVES THE FULL CORRECTED CONSTRAINT SET; JOINT MEMBER.
b2 = FAILS C5 GLOBAL COBoundary INTEGRABILITY; NOT A MEMBER.
```

The 797 `(a2)` zero-parent-curvature map was entirely an artifact of applying the wrong frame conversion. The `(b2)` failure is independently reproduced after that correction and therefore stands.

## 2. AS2 — the corrected joint system

### 2.1 One common-refinement carrier, with composites eliminated definitionally

Use the sealed common refinement

```text
Z = Freudenthal subdivision of each of the 16 A1 subcubes.
```

It has the exact coordinate presentation

```text
vertices:  {0,1,2}^4 / 2                                      count 81
edges:     (u,v), v-u in {0,1}^4 minus {0}, coordinatewise     count 544
cells:     (o,p), o in {0,1}^4, p in S_4                      count 384
```

The curvature quotient is

```text
H_Z = im(d'_1),
dim H_Z = 544-(81-1) = 464,
```

with the 80-dimensional kernel exactly vertex gauge. Let

```text
S : Q^6 -> H_Z,              464*6 = 2784 quotient variables.
```

The exact maps are generated as follows:

- `B_z S` gives the six coordinate components on each Z simplex using 805's corrected barycentric-gradient receiver;
- `A_o S` aggregates the Z edge cochain to each of the 16 A1 cubes by the incidence-derived boundary-square map;
- `D_p S` sums each coarse A2 edge's two Z subedges and applies the corrected six-component A2 receiver, for each of 24 coarse simplices;
- `C S=I_6` is the parent section equation.

There are no independent composite variables. `A_o S` and `D_p S` are the two coarse legs of the same `S`; therefore

```text
L_(r1)L_A1 = L_(r2)L_A2
```

is enforced as equality of one content-addressed cochain on `Z`, not as a later comparison of two authored outputs. Conversely, a coherent pair of path carriers determines this `S` modulo the same 80-dimensional vertex gauge. This elimination is bijective on connection gauge classes.

A0 contributes `L_id=id` and no variable. Longer composites are the displayed matrix compositions and contribute no independent variable.

### 2.2 Closed exact equation inventory

The parent section block is

```text
C S=I_6:                                      36 linear equations, rank 36.
```

The intrinsic-`Vol_4` response equations are imposed at every elementary parent cell on both paths:

```text
parent -> A1:                         1 symmetric 6x6 block = 21
parent -> A2:                         1 symmetric 6x6 block = 21
each of 16 A1 cubes -> its 24 Z cells: 16 blocks            = 336
each of 24 A2 cells -> its 16 Z cells: 24 blocks             = 504
                                                        total = 882.
```

Every block is an exact Gram equation. For example, for an A1 cube `o`,

```text
(1/24) sum_(z in o) (B_z S)^T(B_z S) = (A_o S)^T(A_o S),
```

and the A2-cell equation is the analogous `1/16` identity with `D_p S`. These are exactly the forced volume ratios `1/24` and `1/16`; no fitted weight or tolerance occurs.

The 384-cell incidence census is:

```text
cells per A1 cube = 24,
cells per A2 simplex = 16,
distinct (A1 cube,A2 simplex) incidences = 120,
bipartite partition graph = 40 vertices, 1 connected component, rank 39.
```

For offset `o` and local permutation `p`, the containing coarse A2 permutation is generated without a lookup table: list the coordinates with `o_i=1` in `p` order, followed by those with `o_i=0` in `p` order.

### 2.3 Identity check and exact Jacobian certificate

On the scaled grid, the same constant-form representative is

```text
a_(mu,nu)(u,v)
  = (1/2) [(u_mu/2)((v_nu-u_nu)/2)-(u_nu/2)((v_mu-u_mu)/2)].
```

Exact substitution gives, without a residual,

```text
B_z S_id = I_6 on all 384 Z cells,
A_o S_id = I_6 on all 16 A1 cubes,
D_p S_id = I_6 on all 24 A2 simplices,
C S_id   = I_6.
```

Thus every one of the `36+882` equations vanishes exactly at the identity.

Linearizing the closed equation inventory at this rational point produces a `918 x 3264` edge-presentation Jacobian. The 3264 columns are six copies of the 544 fine edges. Its 480 vertex-gauge columns lie in the kernel, leaving the 2784 quotient columns above.

There is one universal symmetric-block dependency:

```text
[sum of the 16 A1-to-Z equations] + [parent-to-A1 equation]
 = [sum of the 24 A2-to-Z equations] + [parent-to-A2 equation].
```

It contributes exactly 21 row dependencies, so the combined rank is at most

```text
918-21 = 897.
```

After clearing denominators, sparse exact elimination modulo three primes gives

```text
rank mod 1000003 = 897
rank mod 1000033 = 897
rank mod 1000037 = 897.
```

The explicit 21-dimensional rational dependency is the upper bound; any one of the modular ranks is the matching lower bound. Therefore

```text
rank_Q(J_identity) = 897
```

exactly, with no probabilistic rank inference.

The identity is a regular point of the full-rank stratum, and

```text
dim = 2784-897 = 1887.
```

For a rank-`r` coframe block, a real Gram fibre has dimension `n r-r(r+1)/2`; decreasing `r` adds the corresponding vanishing-minor equations and cannot enlarge the full-rank stratum. Hence the full-rank identity stratum is maximal and the real solution variety has dimension `1887`. In particular, the identity is very far from isolated.

### 2.4 Reproducibility fingerprints

Canonical encoding convention: sparse rows are arrays of `[zero_based_column,"n/d"]` entries in increasing column order; nested blocks remain in the generation order above; tight JSON, no trailing newline.

```text
Z barycentric receiver B_z     aedcee64ceb395fd2340d28f70393bbd4b3c803a091fc2feea609cd9c6441693
A1 aggregation blocks A_o      30aeab64be08c19d048fbf131f5accc2266cb86d74c6a14ebe5b1e6d8d425a06
A2 aggregation blocks D_p      9636ede810e60f6d16cc4c265515a546d1aa1b155f971d0122d26945cb0d522a
parent aggregation C           6238ef25a6062f382ad35b05738a60cc5bb20a40031534e42e4d62bf668663fc
full identity Jacobian          dae87953d6602f33c6af198f3988ba59d5f5e0920ae4e8419dd170c68b5ff73b
count/rank transcript           79e95fb08a25c45a70cb6249d138c8ae283e8aa52ab3533310542cbaa7880c53
```

The displayed generating rules plus these fingerprints make every rank and carrier mechanically reproducible without consuming 797's verdicts.

## 3. AS3 — consequences

### 3.1 B1a forcing trichotomy

The corrected joint variety is not empty and not zero-dimensional. Therefore

```text
B1A = FREE, dimension 1887.
```

The identity is one member, not a forced selection. The freedom is joint-carrier freedom after incidence, coframe compatibility, intrinsic measure transport, identity/composition, and O4 conjunct 1—not the objectwise fibre freedom that 786 correctly warned was insufficient.

### 3.2 B1c member-existence bearing

This computation establishes **existence** of at least one joint A1/A2 connection–coframe–measure transport member: the exact identity carrier. It does not bind that member and does not decide any additional receiver predicate outside this system. Dario's lane-opposite 806 work remains untouched.

```text
MEMBER_EXISTENCE_BEARING = existence obstruction removed; identity witness supplied structurally, no member bound.
```

### 3.3 B2 runnability

B2's B1a input now exists as a sealed parameter space rather than a missing carrier. It is therefore structurally runnable **parametrically over the full joint variety**. No member-specific execution is authorized, and any independent B1b/B1c gate retains its own status.

```text
B2_RUNNABLE = yes at the B1a interface, family-parametric only; no bound-member run.
```

## 4. Freedoms consumed

| datum | treatment |
|---|---|
| `F'/F` law | full linear family solved; `(a2)` used only as existence/control; no law adopted |
| `(b2)` orientation signs | derived from the sealed child orientations; tested, not adopted |
| connection representative | quotient by all 80 Z vertex-gauge directions; never fixed |
| refined interior-edge values | carried as the 1887-dimensional joint family; no minimizer or equidistribution chosen |
| parent two-form | symbolic basis over `Q`; no physical value selected |
| A0 | identity/relabeling action carried as derived; no variable authored |
| A1/A2 representatives | the sealed exhibited pair and its sealed common refinement used for the commissioned solve; not promoted to the only allowed cellulations |
| common-refinement carrier | exact 384-cell sealed exhibit; one shared cochain enforces both paths |
| intrinsic `Vol_4` | forced weights `1/16`, `1/24`, `1/384`; no alternative measure |
| metric | none adopted; the norm is the sealed intrinsic response receiver, not a selected counting metric |
| smooth constituent | not imported; S26 remains barred |
| electromagnetic identification | none; S08 remains intact |

`SUBSTITUTED = none.` Modular primes are exact rank instruments after denominator clearing, not physical inputs or tuning freedoms.

## 5. Flattening, gates, and self audit

`FLATTENING_CHECK = clean (37 rows walked).` S26 is live and clean: no smooth `C_ref` coframe or connection supplies any map. S08 is clean: finite edge cochains and two-form coordinates are not identified with electromagnetism, Maxwell data, or a smooth public field. The 384-cell finite common-refinement complex is not a J-II common cell; no junction cell was formed and no junction map was evaluated. No object was selected by outcome.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member binding = none
fixed-point execution = none
end test = none
numeric evaluation of physical quantities = none
comparison to measured constants = none
smooth import = none
EM identification = none
exact solution-set geometry only = true
```

Self verb audit: **NOT CLEAN — one correction disclosure.** Relay 797's `(a2)` killer is reversed. It ran the candidate through the same duplicated-frame-conversion pipeline later located in 805 and reported a zero parent map that the corrected exact carrier returns as `I_6`. The `(b2)` failure was re-derived independently and survives. No 797 verdict was silently carried.

CANDIDATES_RECHECKED = a2: SURVIVES, joint identity member / b2: FAILS global refined-coboundary integrability (corrected computations displayed; ranks 50/50 and 50/56)
JOINT_VARIETY = dim 1887 (identity member: yes; a2 member: yes; b2 member: no; curvature-nonzero: yes)
B1A = FREE (dim 1887)
MEMBER_EXISTENCE_BEARING = joint A1/A2 connection–coframe–measure member existence established by identity witness; no member bound; 806 untouched
B2_RUNNABLE = yes at B1a interface, parametrically over the family (no member-bound execution)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+1: 797 a2 verdict reversed after corrected-L recheck)
