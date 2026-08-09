# STAGE 8 / 7A / [PLAN:B1a-6] — FULL SOLUTION-SET TEST

## Lead determination — CLAIMED

The complete test does **not** land in any member of the requested trichotomy. The trichotomy omitted the empty solution set.

```text
(a2) component inheritance:
     locally integrable on the Freudenthal A2 complex, but its induced coarse curvature is ZERO;
     it violates the section/incidence square for every nonzero parent curvature.

(b2) orientation-weighted component inheritance:
     its 24 child-cell curvature display is not the curvature of any global refined edge cochain;
     it fails child-coframe integrability before a section can be formed.

COMPLETE NATURAL LIFT FAMILIES IN THE DECLARED JOINT FREEDOM SPACE = 0.
```

The exact common-refinement sign/response square is coherent for both *cellwise formulas* on the exhibited 384-cell common refinement. That does not rescue either formula: O4 coherence is downstream of the missing connection lift, and both candidates have already failed O2/O3 on the licensed A2 generator.

All headlines are this lane's `CLAIMED` determinations pending registration/cross-check. No candidate is adopted or eliminated as a member of the cellulation class.

## 0. Preflight and custody

| source | SHA-256 | result |
|---|---|---|
| `PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | pin and adjacent seal verified |
| `STAGE8_B1A_COFRAME_HALF_DARIO_V001.md` (795) | `590b3979d5a0fadfd570e3a73a13bb3a717d5450f7eb5c9f2e79f481039fc1e2` | adjacent seal verified before reading |
| `STAGE8_B1A_CARRIER_CROSSCHECK_NATURALITY_CODEX2_V001.md` (794) | `614e20c8bfd1978a4273c831b76bd6145483876c975ea87f80ef31a589b8bdc7` | adjacent seal verified |
| `STAGE8_B1A_LIFT_FORCING_CODEX2_V001.md` (786) | `3966fdb124c6fed887499ac56907510ed4bc5666be74f32f49f60875c61fc2f0` | adjacent seal verified |
| `STAGE8_B1A_REFINEMENT_CARRIER_DARIO_V001.md` (788) | `97f073c101d8cf4a6743660b96e3861e21914ac48877ce538314616b51d70cb6` | adjacent seal verified |
| `STAGE8_7A_SIMPLICIAL_COFRAME_DARIO_V001.md` (753) | `d6f490b80e8d8775af9ee54095e34da03a4af01541736e2cb138f366c2caa75e` | adjacent seal verified |
| packet `review_packets/STAGE7_QSPEC_CANDIDATE_V001/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` | `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` | packet-sealed copy; all load-bearing V011 bytes taken from this copy |
| `stage8_execution/work/MAJORANT_PHASE2_O3_O7_PROOF_DRAFT_V001.md` | `08b91543fdb72f656c756ca5f8df8233b87eb5487284c7fd2170cba67f7e0e3b` | adjacent seal verified |

Decisive spans:

| content | source/span | span SHA-256 |
|---|---|---|
| four obligations | 786 `[9706,11861)` | `5b5d6b0e358e0663f725ee0498d5fd26f4d33bebab203058883d1fc9ab47ecb2` |
| independently rebuilt A0/A1/A2 incidence carrier | 794 `[3953,7622)` | `cbac23d7b14d4902042b559cda69e210036da81a8260dc481618dfcc3bdc62fd` |
| coframe candidates and quadratic | 795 `[4034,7537)` | `51603bf6059bfbf1f60acf9c94fda11d1e907d807f1f8a407a991aec39ac235f` |
| O1 identity/composition | 795 `[7537,9127)` | `be8c0f9c983bfbebda7e9a7791b8cd6e376fba61aebc4393fc131b60e42bb7e0` |
| exact common-refinement conjunct and boundary-asymptotic conjunct | packet V011 `[47025,47247)` | `9ff6852634e78e6d886896c27bce16b4ec9e092620642a86bae00848df2f276c` |
| corrected O4 reading and common-refinement relation | 788 `[11607,13805)` | `a031d41477012531e452de522d786390e4c783600bc995b9bc372665562e063c` |
| 24 exact child frames | 753 `[4420,6672)` | `01a0c8dbf7dcdd37474242af7791689892e0220c7f59b314ed8204ac1ebe8f22` |
| exhibited `A1`–`A2` common refinement `Z` | MAJ `[19632,19996)` | `b3c67e8c433385a4cb519c2f564649e98b2a9686491487db663592b4b48d6b43` |

PE-1..7 were not consulted and have zero weight.

## 1. AS1 — the complete constraint set

The four-obligation display becomes seven atomic checks when the two O1 laws and O4's tolerance-free first conjunct are made explicit.

| ID | sealed constraint | carrier-level receiver |
|---|---|---|
| C1 | per-generator `Ref_a` lift/naturality | one `L_g:Conn(K)->Conn(K')` for every A0/A1/A2 generator and composite |
| C2 | O1 identity | `L_id=id` on connection gauge classes |
| C3 | O1 composition | `L_(h o g)=L_h o L_g`; composites are not assigned independently |
| C4 | incidence intertwining | `sd*_1 J_1=id` and `d'_1 J_1=J_2 d_1`, hence `sd*_2 J_2=id` on parent curvature |
| C5 | child-coframe compatibility | `J_2(D_e F)=D_(e')F'`, with the `F'/F` law declared, and `D_(e')F'` in `im(d'_1)` |
| C6 | intrinsic-`Vol_4` quadratic | the forced cell measure and quadratic obey the elementary-refinement clause, with only the sealed boundary-asymptotic allowance |
| C7 | O4 conjunct 1, exact | response pullback to a common refinement is path-independent; no tolerance applies |

### 1.1 How C7 is posed

For a common-refinement square

```text
             g             r_1
        K --------> K_1 --------> M
        |                         ^
      h |                         | r_2
        v                         |
        K_2 ----------------------
```

C7 requires the two carrier pullbacks to agree on the same codomain:

```text
L_(r_1) L_g = L_(r_2) L_h : Conn(K) -> Conn(M),
```

and the response computed after either pullback must be the same response on `M`. This is the exact receiver for V011's sentence “The response map must commute with pullback to a common refinement.”

The displayed finite instance is the unit 4-cube `K`, its 16-cell cubical bisection `A1(K)`, its 24-cell Freudenthal subdivision `A2(K)`, and `Z=A2(A1(K))`, the 384-cell common refinement. A0 supplies units/relabelings; longer composite squares are obtained by adjoining the same generators to either leg. C7 is therefore a path-equality on existing finite maps, not a prose analogy.

## 2. AS2 — exact solution-set computation

### 2.1 Exact A2 receiver

The Freudenthal A2 complex was rebuilt independently from the Boolean vertices and monotone chains:

```text
vertices = 16
global comparable edges = 65
4-simplices = 24
ordered bivector components per simplex = 6
```

For every simplex `p`, barycentric gradients were obtained by exact rational inversion of its `5 x 5` affine vertex matrix. The integer matrix

```text
B : Q^65 -> Q^(24*6)
```

maps a global refined edge cochain to its six constant curvature components on every simplex, using

```text
F_(mu nu) = 2 sum_(i<j) a_ij (g_i_mu g_j_nu - g_i_nu g_j_mu).
```

`rank_Q(B)=50=65-(16-1)`: its kernel is exactly vertex gauge, as expected on this contractible complex.

Let `E_p` be 753's exact child frame and `W_p=wedge^2(E_p)`. In the ordered-pair convention `(01,02,03,12,13,23)`, the two candidate target matrices are

```text
T_a2(p) = W_p^T F,
T_b2(p) = sgn(p) W_p^T F.
```

This is precisely “same component vector in the child's frame,” with the second law carrying 753's derived orientation. Using `W_p` instead of `W_p^T` as a convention control produces the same verdicts below.

### 2.2 `(a2)` — local integrability, then exact section failure

Exact rational ranks over all six basis two-forms give

```text
rank(B) = 50
rank([B | T_a2]) = 50.
```

So `(a2)` does define a global refined curvature cochain before the parent section condition is imposed. Solving the system exactly leaves 15 free edge variables, all vertex gauge. The induced circulation on **each of the 24 parent square faces** was then computed from any solution. Its complete `6 x 6` parent-curvature map is

```text
          parent output rows 01,02,03,12,13,23
          input columns       01,02,03,12,13,23

          [0 0 0 0 0 0]
          [0 0 0 0 0 0]
          [0 0 0 0 0 0]
          [0 0 0 0 0 0]
          [0 0 0 0 0 0]
          [0 0 0 0 0 0].
```

Equivalently, adjoining the 24 parent-face constraints `sd*_2 J_2 F=F` gives

```text
rank(carrier equations) = 50
rank([carrier equations | a2 targets]) = 56.
```

The cancellation is exact: `(a2)` coarsens every input to zero curvature. It satisfies the section square only on the zero-curvature subspace, not on `Conn(K)`. A natural lift required on every connection class therefore does not exist.

```text
SOLUTION_SET_A2 = EMPTY.
KILLER_A2 = C4 incidence/section equation (sd*_2 J_2 = id).
```

### 2.3 `(b2)` — no global refined curvature

For the orientation-weighted target,

```text
rank(B) = 50
rank([B | T_b2]) = 56.
```

All six target directions add independent inconsistency. Thus the signed per-simplex display is not the curvature of any global refined edge cochain for a nonzero basis input. It fails `D_(e')F' in im(d'_1)` before parent aggregation or naturality can be asked.

```text
SOLUTION_SET_B2 = EMPTY.
KILLER_B2 = C5 global child-coframe integrability (and therefore C4).
```

The transpose-convention control (`W_p` in place of `W_p^T`) again gives augmented rank `56` for both candidates once the parent-curvature constraints are included. The verdict is not an artifact of row/column convention.

### 2.4 Machine transcript and completeness of the counterexample

```text
Freudenthal receiver: 144 local equations x 65 global edge variables.
Exact ranks: B=50 ; [B|a2]=50 ; [B|b2]=56.
With 24 parent-face equations: carrier=50 ; [carrier|a2]=56 ; [carrier|b2]=56.
a2 induced parent map: zero 6x6 matrix, checked on all 24 parent faces.
Arithmetic: fractions/integers only; six basis inputs span the whole two-form input space.
```

A2-Freudenthal is a licensed A2 generator. Failure on this one admitted generator refutes existence of a family quantified over **every** A0/A1/A2 generator and composite. No narrowing to the barycentric representative is permitted or used.

### 2.5 O4 common-refinement diagnostic

Although neither connection lift reaches C7, the two *cellwise* coframe laws were checked on `Z` to separate an O4 defect from the earlier carrier defects.

For each of the 16 subcube offsets and 24 local permutations, the containing global Freudenthal simplex was derived from the coordinate order. For `(b2)`, orientation along the two paths agrees because relative orientation multiplies:

```text
sgn(K -> A2 cell) * sgn(A2 cell -> Z cell) = sgn(K -> A1 -> Z cell).
```

Transcript:

```text
Z cells = 384
orientation-path mismatches = 0
direct signs = 192 positive / 192 negative
257 independent integer six-component trials
A1/A2/Z intrinsic-Vol_4 quadratic mismatches = 0 (exact Fraction arithmetic)
```

Thus both candidate **formulas** are composition/coherence-compatible at the cell-response level and their signs disappear quadratically. But C7 asks for a response pulled through `L`; no such `L` exists for either candidate. The complete-family solution set remains empty.

## 3. AS3 — verdict and the missing fourth case

The commissioned alternatives were:

```text
FORCED_UNIQUE  cardinality = 1
FREE           cardinality >= 2
UNDECIDABLE    predicate cannot be posed
```

All predicates were posed. The computed cardinality is `0`. Relabelling `0` as `1`, `>=2`, or “unposed” would be false. Therefore the honest result is the omitted fourth case:

```text
EMPTY — the declared candidate space contains no complete natural lift.
```

The two candidates have the same cardinality verdict but different failure layers: `(a2)` is globally integrable and fails coarse incidence; `(b2)` fails global integrability itself. O4 conjunct 1 kills neither cellwise formula; it is never reached by a complete carrier.

## 4. AS4 — consequences

### 4.1 B1a

The bounded two-candidate solution-set test is closed **EMPTY**, but B1a is not closed by a transport. Its remaining object is now sharper:

```text
a new sealed F'/F law, outside {a2,b2}, that simultaneously
  (i) lies in im(d'_1),
  (ii) is a section of curvature aggregation,
  (iii) satisfies the intrinsic-Vol_4 quadratic,
  (iv) forms an identity/composition family, and
  (v) obeys exact common-refinement response coherence.
```

The eliminated `(a1)` cannot be silently reinstated: 795 killed it under the intrinsic quadratic. No surviving law is selected here.

### 4.2 B1c member

`JOINT_A1_A2_FIELD_EXT_MEMBER` is **not supplied**. A member requires a joint A1/A2 field-extension family; both available coframe laws fail the A2 connection carrier. The B1c receiver remains typed but uninhabited.

### 4.3 B2 gluing obstruction

B2 is **not runnable**. The forced gluing computation begins only after B1 supplies its transport inputs. The connection/field-extension input is still absent, now for the exact empty-set reason above rather than an unposed coframe square.

## 5. Freedoms consumed and flattening check

### 5.1 `FREEDOMS_CONSUMED`

| datum | treatment |
|---|---|
| `F'/F` law | both sealed candidates tested; neither adopted; `(a1)` remains eliminated by 795 |
| section `J_1` freedom | exhaustively retained in the 65-variable systems; the 15-dimensional kernel is vertex gauge; no representative selected |
| parent two-form `F` | carried symbolically; six basis inputs are a spanning structural test, not a selected field value |
| child frames `E_p` | carried as derived from 753 |
| child orientation `sgn(p)` | carried as derived; used only to instantiate `(b2)` and the path check |
| intrinsic `Vol_4` | carried as forced/classified; no alternate measure |
| A2 representative | Freudenthal used as one licensed universal-claim counterexample; not adopted as the sole A2 member and no other member eliminated |
| `Ref_a` directedness/common-refinement grammar | carried with its adopted status; not re-derived or strengthened |
| counting inner product / `Q_flux` | not consumed; this test is exact incidence/coframe algebra |
| scaling weights (law 2a) | none consumed; no scaling statement occurs |
| metric | not adopted; the only quadratic is the sealed intrinsic-`Vol_4` receiver |
| smooth coframe/connection constituent | not consumed; barred by S26 |

`SUBSTITUTED: none.` Trial seed and trial count are diagnostics only; the verdict is carried by exact ranks and the exact zero parent map.

### 5.2 `FLATTENING_CHECK`

- S26 remains live and clean: no smooth `C_ref` constituent supplies a connection or field. The full test uses the combinatorial complexes, 753's derived frames, and packet D10/O4 only.
- S08 remains clean: `F`, edge cochains, and response carriers are not identified with electromagnetism, Maxwell data, or a smooth public field.
- No common cell was formed and no junction map was evaluated.
- S01–S07 and S09–S37 are untouched.

`FLATTENING_CHECK = clean (37 rows walked; S26 and S08 live, both discharged).`

## 6. Gates, jurisdiction, and self verb audit

The exact finite ranks, derived orientation signs, and path identities are the commissioned structural class. No physical quantity was numerically evaluated. No bundle member, `F'/F` law, metric, or A2 representative was adopted. No fixed point, end test, common cell, or junction map was evaluated. The evaluator chain was not invoked.

**Self verb audit — NOT CLEAN (+1 custody disclosure).** During source discovery, one broad filename/text search unintentionally scanned the unsealed root `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` despite the relay's packet-exclusive instruction. No root bytes, offsets, or claims enter any derivation above: every load-bearing V011 quotation, span, and hash was subsequently read and rehashed from the packet-sealed `aa7c6d49…` copy exclusively. The read itself remains a custody breach and is disclosed rather than called clean.

```text
CONSTRAINTS = assembled (7 atomic constraints, span-cited; O4c1 posed as L_(r1)L_g = L_(r2)L_h and response equality on the A1/A2 common-refinement square Z)
TEST_A2 = EMPTY (killer: incidence section; locally integrable target coarsens identically to zero)
TEST_B2 = EMPTY (killer: child-coframe/global coboundary integrability; augmented rank 56 > 50)
CROSS_CASE = same cardinality verdict EMPTY; different failure layers displayed
B1A = remaining stated (declared two-candidate test closed EMPTY; new simultaneous incidence+coframe+quadratic+coherence law required)
B1C_MEMBER = not yet (JOINT_A1_A2_FIELD_EXT_MEMBER remains uninhabited)
B2_RUNNABLE = no (complete B1 connection/field-extension transport still absent)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+1: broad discovery search scanned unsealed root; zero root evidence consumed)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
