# STAGE8 TASK 4B - METRIC V003 FINAL CHECK - LANE 1 V001

```text
ARTIFACT = STAGE8_TASK4B_METRIC_V003_FINAL_CHECK_LANE1_V001.md
LANE = CODEX LANE 1
TASK = PASTE 460 | final check of carrier metric V003
DATE = 2026-08-03
STATUS = COMPLETE | REVIEW ONLY | NOTHING ADOPTED

LEAD_RESULT:
  METRIC_PACKAGE = NOT_READY
  PASSING_ITEMS = V1 | V2
  KILLING_ITEMS = V3 | V4 | V5
  DEFECT = V003 drops V002's derived finite C-side dual metric/Riesz/quotient-norm construction
  CONSEQUENCE = the original Section 4.2 gap list is not closed self-containedly
  REPAIR_SCOPE = restore finite E_G, g_C,G, R_C,G, and quotient-norm/pendant theorem as derived

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 0. Preflight and bounded-review basis

Preflight passed before V003 was read.

| Check | Result |
|---|---|
| register head | `Q-378` exactly |
| V003 SHA-256 | `29ec770a8299fccadd68456b150f041eb64651ca2ba080b8a1c56c102f120fc9` - match |
| V003 sidecar | verified `OK` |
| fullness standard | `f422a0340e253a72223f3c11d240b9b6a08b25a78ebf309085e84e965d8067ad` |
| original gap standard | `2e1b011069043c1cc03277178be061a8b7d1704d2146be97eb799965aef9c679`, Section 4.2 |

The direct comparison used V002
`7788e29da98be54e983a660768c0c70258e7d6d89eb51a2dafc4dbe17a9ea825`
as the baseline. V002 has 870 lines and V003 has 699 lines. The textual delta is
not a verbatim carry with bounded insertions: complete mathematical sections were
rewritten or removed. That is not automatically a kill, but every removed load-bearing
object must still be present by an explicit derived or authored construction.

Symbol precision:

```text
E_G(edge)  = finite real oriented-edge carrier used by B_G and L_G;
Eval_G     = finite evaluation/duality map Q_G^lin -> K_G^*;
```

The second name avoids confusing V002's evaluation map `E_G` with the edge carrier.

## 1. Verdict table

| Item | Verdict | Reason |
|---|---|---|
| V1 fullness installation | **PASS** | the complete A2-R10 chain is quoted, the kernel proof is correct, full-carrier positivity has the right premises, null branches are removed, and the countermodel is correctly retained only as an admissibility regression |
| V2 W3 isometry | **PASS** | DoR-015's isometric inclusion/adjoint clause is used exactly once to derive rank-preserving cycle isometry; automorphism isometry remains authored and W3 is not extended to batching or cycle creation |
| V3 four-item residue | **KILL** | the completion/carrier row absorbs but does not construct the already-derived finite C-side metric and Riesz data; finite derived content is omitted/mislabeled as part of an authored completion condition |
| V4 original Section 4.2 gaps | **KILL** | `||.||_K` and `R_K` are supplied, but V003 contains no finite `g_C`, `R_C`, quotient-norm formula, or pendant/tree norm certificate |
| V5 delta, battery, DP, fresh attack | **KILL** | the delta is not bounded in the required substantive sense: V002 Section 4's finite complement theorem disappears, and the battery has no C-side or quotient-norm regression to catch it |

## 2. V1 - fullness theorem and null-branch cleanup

V003 carries the exact ratified chain:

```text
-i h_e^(-1) d h_e(a,theta)
  =(L_G a)_e+(B_G theta)_e,

A2-R10 => image(L_G)+image(B_G)=E_G(edge).       (V1-1)
```

For `c in ker(B_G^T)` with `u_c=0`, arbitrary `x=L_G a+B_G theta` gives

```text
c^T x=u_c(a)+(B_G^T c)^T theta=0.
```

Nondegeneracy of the edge pairing gives `c=0`. Therefore

```text
ker(I_K,G)=0,
s_G(c,d)=g_A4(u_c,u_d) is positive definite.     (V1-2)
```

The proof is uniform over the complete realization family and selects no member. The
directed-core and completion argument is also correct: using
`||c||_s=||I_K c||_A4`, the completed extension is isometric and injective.

V003 deletes the live quotient/null choices and records

```text
K_G/ker(I_K,G)=K_G/0=K_G.
```

Its old `R^2` model is correctly classified: the witness may be integral, but
`T_phys=span(e_1)` fails R10 and is not admitted. This is a valid permanent
admissibility regression.

```text
V1_VERDICT = PASS
```

## 3. V2 - W3 derivation and authored automorphism scope

DoR-015 ratifies:

```text
i_NM:C_N->C_M is an isometric source inclusion,
rho_MN=i_NM^*,
I_K,M j_K,NM=i_NM I_K,N.                         (V2-1)
```

Thus, for finite cycles `c,d`, V003 correctly computes

```text
s_M(j_K c,j_K d)
 =g_A4,M(i_NM I_K,N c,i_NM I_K,N d)
 =g_A4,N(I_K,N c,I_K,N d)
 =s_N(c,d).                                      (V2-2)
```

So `j_K,NM` is isometric and `rho_K,MN=j_K,NM^*` on the ratified
rank-preserving scope.

V003 does not infer from this that:

1. realization exchanges/relabelings are A4 isometries;
2. cycle-creating extensions have a physical upward quotient map;
3. generic batching is isometric;
4. an arbitrary R5 enlargement equals the forced completion.

The remaining A4 automorphism-isometry row is therefore correctly authored, with the
anisotropic exchange as a failure-capable test.

```text
V2_VERDICT = PASS
```

## 4. V3 - audit of the four-item residue

| Authored item | Alternatives/minimality/void audit | Verdict |
|---|---|---|
| R5 completed-carrier identification | alternatives and void conditions are genuine; however the row improperly carries finite `C_prop`-side duality without restoring its derived construction | **KILL** |
| positivity/reality completion convention | real-positive/Hermitian, real-only, or separately justified compatible convention are genuine; void conditions bar changed finite values, indefiniteness, and response-selected signature | **PASS** |
| A4 automorphism isometry | invariant retained form, disclosed invariant replacement, bounded covariance/no orthogonal propagation, or rejection are genuine; S8-A/reversal/stabilizer failures are testable | **PASS** |
| carrier units and R4 seam | formal dual carrier units, corrected Riesz powers, and no scale/member selection are properly scoped; the void conditions bar fixing `nu` or a response scale | **PASS** |

The first row's problem is provenance, not the legitimacy of an authored completion.
R5 identification is genuinely authored at the completed level. But finite Gate-4
duality after R10 already determines the finite C-side form from the derived K-side
metric. V003 neither lists that finite construction in its derived core nor gives it
an equation elsewhere. The statement

```text
"finite evaluation maps are dense, onto, closed-range compatible"
```

inside `CARRIER_IDENTIFICATION_CERT` is a condition, not the missing construction and
proof. Consequently the candidate both omits derived content and makes the authored
row do more work than its lawful completion-only scope.

```text
V3_VERDICT = KILL
```

## 5. V4 - original Section 4.2 gap list, item by item

The original adjudication required both carrier norms, both Riesz maps, unit maps,
orthogonal transport, quotient-norm descent, and automorphism isometry.

| Original gap | V003 standing | Verdict |
|---|---|---|
| `||.||_K` | `s_G=g_A4(I_K .,I_K .)` is positive definite by fullness; completion faithful | **SUPPLIED / DERIVED** |
| `R_K` | finite Riesz map follows from positive finite form; completed map follows after Hilbert identification | **SUPPLIED / DERIVED+AUTHORED SEAM** |
| `||.||_C` | no finite definition in V003; only the proposed statement that completed `C_prop` is the Hilbert dual | **MISSING CONSTRUCTION** |
| `R_C` | mentioned only through generic `R_A`; no C-side form or finite Riesz proof is installed | **MISSING CONSTRUCTION** |
| carrier units/R4 seam | formal `U_C,U_K`, corrected powers, and seam are listed | **SUPPLIED / AUTHORED** |
| rank-preserving orthogonal transport | derived from W3 | **SUPPLIED / DERIVED** |
| realization automorphism isometry | choice-table certificate with void conditions | **SUPPLIED / AUTHORED** |
| quotient-norm descent | no formula or theorem in V003 | **MISSING CONSTRUCTION** |
| pendant/tree regression | removed from the battery and not re-proved | **MISSING REGRESSION** |
| completed Hessian/Riesz transport | conditional on the authored carrier and automorphism certificates | **SUPPLIED / CONDITIONAL** |

### 5.1 The deleted derived construction

V002 contained the finite evaluation map

```text
Eval_G:T_phys,G->K_G^*,
Eval_G(t)(c)=u_c(t),                              (V4-1)
```

and proved it an isomorphism by separation and equal rank. Under V003's stronger R10
theorem, this becomes even cleaner:

```text
T_phys,G=Q_G^lin=E_G(edge)/image(B_G),
beta_G:Q_G^lin->K_G^*,
beta_G([x])(c)=c^T x                             (V4-2)
```

is the finite Gate-4 duality isomorphism. The missing C-side definitions are then
forced:

```text
g_C,G(q,q'):=g_(K_G^*)(beta_G q,beta_G q'),
R_C,G(q)(q'):=g_C,G(q,q'),                       (V4-3)

||[x]||_C
 =sup_(0!=c in K_G) |c^T x|/||c||_K.             (V4-4)
```

These formulas are not additional authored physics. They are the finite dual of the
already-derived K metric. They prove:

1. representative independence because `c^T B_G theta=0`;
2. positivity because `beta_G` is injective;
3. `R_C,G` is a finite Riesz isomorphism;
4. a tree/pendant coboundary has zero quotient norm;
5. every nonzero cycle-holonomy quotient class has positive norm.

V003 has none of `(V4-1)` through `(V4-4)`. Its final board nevertheless says the
finite full-carrier Riesz maps are derived. The plural claim is unsupported in the
self-contained candidate.

```text
ORIGINAL_GAP_LIST_CLOSED = false
V4_VERDICT = KILL
```

## 6. V5 - delta, battery, DP ledger, and fresh attack

### 6.1 Delta check

The commissioned cleanup required U1-U3 changes with everything else carried. The
direct diff is a broad rewrite: V002's 870 lines become 699 lines, and the finite
complement section is removed rather than carried or premise-marked. The delta table
does not disclose that deletion. Its claim

```text
"No other mathematical field ... is changed"
```

is false for the finite C-side construction.

### 6.2 Battery

The R10, W3, unit, response-support, hidden-scale, automorphism, cycle-creation, and
external-enlargement checks pass. But V003 removes the pendant/tree test and adds no
C-side Riesz or quotient-norm test. Its battery therefore cannot detect the deletion
found above.

### 6.3 DP1/DP7

The K-side statements are correct:

```text
DP1 finite K form/positivity/completion = derived;
DP7 rank-preserving K naturality = derived;
DP7 automorphism isometry = pending DoR-019;
generator and divergence data = still TYPE-U.
```

The ledger is incomplete for a germ that consumes both `C_prop` and `K_cycle`: DP1's
C-side metric/Riesz interface is not executable from V003 as written.

### 6.4 Fresh attack - C-side evaporation

Trace one nonzero complement covector through the proposed package. V003 supplies a
positive K metric and says completed `C_prop` will be its dual, but before that authored
identification there is no displayed finite map assigning the covector a C norm or
Riesz representative. Thus two implementations can agree on every V003 displayed
finite K equation while assigning different finite C norms. The omitted formulas
`(V4-3)` and `(V4-4)` are exactly what exclude that freedom.

This is not a demand for a fifth authored field. It is a demand to restore derived
content that V002 already had. The repair is bounded:

```text
restore Eval_G/beta_G and equations (V4-3)/(V4-4) as TYPE-P;
restore the pendant/tree quotient-norm regression;
list finite R_C in the derived board;
keep only the completed R5 identification authored.
```

```text
FRESH_ATTACK = succeeds
V5_VERDICT = KILL
```

## 7. Final determination

V003 correctly closes the fullness and W3 defects and its four-item authored residue
is nearly the right DoR-019 surface. It is not yet ratification-ready because the
bounded rewrite drops one previously derived half of the carrier geometry while
claiming all original gaps are supplied.

No new physical choice is needed to repair it. A V004 can restore the finite C-side
dual metric, Riesz map, quotient norm, and pendant regression as derived consequences
of R10, Gate-4 duality, and the positive K form.

```text
METRIC_PACKAGE = NOT_READY (V3, V4, V5)
READY_FOR_DOR019_RULING = no

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
