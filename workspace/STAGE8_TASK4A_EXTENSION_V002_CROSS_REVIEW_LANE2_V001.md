# STAGE8 TASK 4A: EXTENSION V002 CROSS-REVIEW — CODEX LANE 2 V001

Date: 2026-08-03  
Task: PASTE 435 / Task 4a / adversarial cross-review of Q-351  
Lane: CODEX LANE 2  
Register head: Q-352

```text
LEAD_RESULT = CONFIRMED-WITH-ONE-EXTERNAL-SEAM-STILL-OPEN

EXTENSION_V002 = CONFIRMED

REPAIR =
  rho_G,MN compose T_(M,G_M)^char compose j_NM^Q
    =T_(N,G_N)^char

REPAIR_PROOF_ENDPOINT =
  Z_M compose j_NM^Q=Z_N

RANK1_UNIQUENESS_SCOPE =
  uniqueness among maps satisfying Hol_(c_G) compose T=Z_N

DESCENT_PENDING_SEAMS = OPEN | P-432-3 only |
  P-432-1 CLOSED;
  P-432-2 CLOSED;
  P-432-3 awaits relay 434's independent cross-review of the descent and
  the joint merge, not any further V002 repair

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

V002 performs the repair requested by the V001 cross-review and does not
alter the already-confirmed fixed-stage classification, automorphism no-go,
or kernel/image theorem. Its rank-one square is now typed and proved. The
information-layer foundation is mathematically composable on the finite
edge-resolved scope; process-level closure still awaits the independent
review of the descent artifact in relay 434.

---

## 1. Preflight and custody

### 1.1 Artifact under review

The Lane-1 artifact and its sidecar were verified before the file was read:

```text
artifact =
  alpha-program-archive/workspace/
  STAGE8_TASK4A_MAP1_FULL_FAMILY_EXTENSION_LANE1_V002.md

expected_sha256 =
  eb3675d525af7d1420c4ed033a5e5b94eb7494c1bac1305029b25ac9169567a0

actual_sha256 =
  eb3675d525af7d1420c4ed033a5e5b94eb7494c1bac1305029b25ac9169567a0

sidecar_verification = PASS
```

### 1.2 Authorities

| Authority | Verified SHA-256 | Result/use |
|---|---|---|
| V001 cross-review | `4bcc286e1cb1adf5fbdbc725d0bbd1947c04c56bfa72b2394afeb129a237c1a3` | PASS; exact repair and Y7 standard |
| Q-313 Map 1 | `ea8f4e9a79a9e4aca4a0b9e9aab470d78cd4d9c78794c20d9e979c0db16fbeab` | PASS; `j_NM^Q`, zero extension, uniqueness |
| Q-315 squares | `f886284c632f238bb01d02de2cc64e3f7ed76c0bae4ba14487ac0b2bde7a22e3` | PASS; fixed-square restriction |
| DoR-015 / V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | PASS; quotient and separation |
| Q-352 descent build | `5c5d2c828a62e302920c827e95678c9e9e00b2fdc1a2415c553383fcbbfe3a84` | PASS; three pending seam declarations |

All sidecars passed. `LOCKED_PROCESS.md` was read in full, including the Q-351
local-sidecar rule. The reviewer-maintained questions-settled register and
its local sidecar now match, and the live head is Q-352.

```text
DOES_THE_OBJECT_EXIST = yes | sealed V002 repair
IS_THE_VERSION_CURRENT = yes | register head Q-352
ARE_THE_INPUTS_PRESENT = yes
PREFLIGHT = PASS
```

### 1.3 Current-version precision

V002 was built at Q-350. Its final line saying the prefix descent remained
unbuilt was true at construction time. Q-352 now supersedes that status by
building the descent on finite signed edge-resolved realizations. This
historical status line is not part of V002's bounded repair and does not
invalidate its theorem.

---

## 2. Verdict table V1–V6

| Item | Verdict | Determination |
|---|---|---|
| V1 repair | **PASS** | `j_NM^Q` is inserted on the source side; every domain/codomain matches; the proof reaches `Z_M j_NM^Q=Z_N` and closes by rank-one holonomy injectivity. |
| V2 scope precision | **PASS** | Uniqueness is expressly limited to maps satisfying `Hol_(c_G) T=Z_N`; square compatibility alone is expressly refuted as sufficient. |
| V3 delta table | **PASS** | A direct unified diff finds twelve semantic hunk classes, all covered by D01–D12; the confirmed classification, obstruction, and kernel/image text is unchanged except for terminal-scope wording. |
| V4 regressions | **PASS** | The suite reruns. The repaired square is independently executed below on the fixed Q-313 square for `N=1`, `M=2`, with both quotient classes computed exactly. |
| V5 descent seams | **PASS WITH STATUS SPLIT** | P-432-1 and P-432-2 close. P-432-3 remains open only for relay 434's independent descent review/joint merge. |
| V6 fresh attack | **PASS** | A non-identity two-cell split with arbitrary factors preserves the rank-one quotient output; a degree-changing target map is correctly outside the primitive-class scope. |

No item kills V002.

---

## 3. V1 — the repair itself

### 3.1 Type table

V002 declares

```text
j_NM^Q:Q_rel,N->Q_rel,M,
T_(N,G_N)^char:Q_rel,N->Q_(G_N),
T_(M,G_M)^char:Q_rel,M->Q_(G_M),
rho_G,MN:Q_(G_M)->Q_(G_N).
```

Therefore

```text
rho_G,MN compose T_(M,G_M)^char compose j_NM^Q
```

has domain `Q_rel,N` and codomain `Q_(G_N)`, exactly matching
`T_(N,G_N)^char`.

This is the precise insertion required by the V001 cross-review. It adds no
new map: `j_NM^Q` is Q-313's sealed source zero extension.

```text
V1_DOMAIN_LEFT = Q_rel,N
V1_CODOMAIN_LEFT = Q_(G_N)
V1_DOMAIN_RIGHT = Q_rel,N
V1_CODOMAIN_RIGHT = Q_(G_N)
TYPECHECK = PASS
```

### 3.2 Recomputed proof

The target restriction carries the primitive oriented character:

```text
Hol_(c_GN) compose rho_G,MN=Hol_(c_GM).            (V1-1)
```

The rank-one components obey

```text
Hol_(c_GM) compose T_(M,G_M)^char=Z_M,
Hol_(c_GN) compose T_(N,G_N)^char=Z_N.             (V1-2)
```

Apply `Hol_(c_GN)` to the repaired left side:

```text
Hol_(c_GN) rho_G,MN T_(M,G_M)^char j_NM^Q
 =Hol_(c_GM) T_(M,G_M)^char j_NM^Q
 =Z_M j_NM^Q
 =Z_N
 =Hol_(c_GN) T_(N,G_N)^char.                      (V1-3)
```

The penultimate equality is exactly Q-313's identity-zero-extension theorem.
Since `Hol_(c_GN)` is an isomorphism at rank one, it is injective, so

```text
rho_G,MN T_(M,G_M)^char j_NM^Q
 =T_(N,G_N)^char.                                 (V1-4)
```

The square is proved rather than asserted.

```text
J_NM_INSTALLED_EXACTLY = true
Q313_ZERO_EXTENSION_USED = true
REPAIRED_SQUARE = PASS | TYPE-P
V1 = PASS
```

### 3.3 No over-repair

V002 does not claim that `(V1-4)` supplies arbitrary rank-changing
cellulation naturality. Its printed scope is:

```text
cycle-rank-preserving arrows carrying the primitive class.
```

Arrows creating a second independent cycle remain outside E2 and are handled
only by the terminal-scalar no-go. This is the bounded repair ordered by
Q-350.

---

## 4. V2 — Y7 scope precision

For a rank-one graph, the quotient coordinate is an isomorphism

```text
Hol_(c_G):Q_G->U(1).
```

V002 defines

```text
T=Hol_(c_G)^(-1) compose Z_N
```

and states that it is unique among maps satisfying

```text
Hol_(c_G) compose T=Z_N.                           (V2-1)
```

It then explicitly adds:

```text
RANK1_UNIQUENESS_FROM_SQUARE_COMPATIBILITY_ALONE = false | TYPE-R.
```

This matches the V001 cross-review's Y7 finding. Indeed, without `(V2-1)`,
the maps

```text
Hol_(c_G)^(-1) compose Z_N^m,
m in Z,
```

remain continuous, batching-compatible candidates on an unrelated rank-one
component. Equation `(V2-1)` alone forces `m=1`.

```text
UNIQUENESS_UNDER_EXACT_FACTORIZATION = PASS
UNIQUENESS_FROM_SQUARE_AGREEMENT_ALONE_CLAIMED = false
V2 = PASS
```

---

## 5. V3 — delta-table audit

### 5.1 Direct diff method

The sealed V001 and V002 files were compared directly with a unified textual
diff. Every changed hunk belongs to one of these groups:

| Actual hunk | V002 row | Audit |
|---|---|---|
| version title | D01 | covered |
| lead key narrowed; repair/supersession/scope block added | D02 | covered |
| authority/preflight update | D03 | covered |
| Q-347–Q-350 register sweep append | D04 | covered |
| E1 “terminal scalar” precision | D05 | covered |
| exact-equation uniqueness paragraph and flags | D06 | covered |
| full typed square, `j_NM^Q`, proof chain, repaired flag | D07 | covered |
| E3 heading, scope flag, terminal-only board key | D08 | covered |
| explicit regression and rerun block | D09 | covered |
| higher-rank no-go scope line | D10 | covered |
| final terminal-only wording and repair board | D11 | covered |
| new delta section and final-section renumbering | D12 | covered |

No thirteenth hunk class exists.

### 5.2 Confirmed-body spot checks

The following were compared against V001:

1. **Classification:**

   ```text
   Hom_cont(U(1),Q_G) is classified by lambda in Hom(C_G,Z),
   Hol_G(s_G(z))(c)=z^(lambda(c)).
   ```

   The formula and residual family are unchanged.

2. **S8-A obstruction:**

   ```text
   sigma(c_1)=c_2,
   sigma(c_2)=c_1,
   sigma(c_3)=-c_3,
   lambda(c_3)=0.
   ```

   The proof is unchanged; only its terminal-scalar scope is made explicit.

3. **Kernel/image disclosure:**

   ```text
   Ann(image(s_G^lambda))=ker(lambda),
   dim image<=1,
   rank ker(lambda)>=rank(C_G)-1.
   ```

   The equations and source-kernel cases are unchanged.

4. Rank-zero construction, rank-one formula, quotient compatibility,
   reality, batching, one-edge, S8-A, identity extension, and selection
   accounting are unchanged except where the delta table says otherwise.

```text
DELTA_TABLE_COMPLETE = true
UNLISTED_CHANGED_HUNK_FOUND = false
CONFIRMED_V001_MATHEMATICS_CARRIED = true
V3 = PASS
```

---

## 6. V4 — regressions and explicit repaired-square execution

### 6.1 Independent explicit `N=1`, `M=2` pair

Use Q-313's same sealed target `Q_square` at both relative-history stages.
Thus

```text
G_N=G_M=G_square,
rho_G,21=id_(Q_square),
c_GN=c_GM=c_square.
```

For arbitrary symbolic `u in U(1)` and either faithful
`n in {+1,-1}`,

```text
j_12^Q(u)=(u,1),
Z_1(u)=u^n,
Z_2(u,1)=(u 1)^n=u^n.                             (V4-1)
```

Compute the left quotient class, not merely its holonomy:

```text
rho_G,21 T_(2,G_square)^char j_12^Q(u)
 =id Hol_(c_square)^(-1)(Z_2(u,1))
 =Hol_(c_square)^(-1)(u^n).                       (V4-2)
```

Compute the right quotient class:

```text
T_(1,G_square)^char(u)
 =Hol_(c_square)^(-1)(Z_1(u))
 =Hol_(c_square)^(-1)(u^n).                       (V4-3)
```

The two sides are identical. This independently instantiates V002's generic
`N=1`, `M=2` holonomy check with an actual target and restriction map.

```text
EXPLICIT_N1_M2_TARGET = Q_square
EXPLICIT_RHO = identity
BOTH_QUOTIENT_CLASSES_COMPUTED = true
REPAIRED_SQUARE_EXPLICIT_TEST = PASS
```

### 6.2 Remaining suite

The remaining checks recompute:

```text
one edge:
  ker(B_1^T)={0}; target cycle quotient is the point; PASS

S8-A:
  B_M^T(1,0,-1)=0;
  terminal scalar is sigma-fixed;
  lambda(c_3)=0; PASS against scalar-only full extension

reality:
  Z_N(Theta r)=conjugate(Z_N(r));
  T(Theta r)=Theta T(r); PASS

identity zero extension:
  Z_M(r,1,...,1)=Z_N(r); PASS

batching:
  Z(h_2 compose h_1)=Z(h_2)Z(h_1); PASS
```

No rank, ratio, orientation, or `p` value is selected.

```text
V002_REGRESSION_SUITE = PASS
V4 = PASS
```

---

## 7. V5 — the three descent seams

The Q-352 descent artifact named three PENDING comparison points. They are
resolved one by one, without changing either artifact.

### 7.1 P-432-1 — rank-one family agreement

On the Q-313-compatible signed rank-one realization, the descent proves

```text
Hol_(c_G) compose D_G=Z_N.                         (V5-1)
```

V002 proves that there is one and only one map satisfying `(V5-1)`:

```text
T_(N,G)^char=Hol_(c_G)^(-1) compose Z_N.
```

Therefore

```text
D_G=T_(N,G)^char                                  (V5-2)
```

pointwise on every shared Q-313-compatible rank-one member. V002's repaired
naturality then promotes this from pointwise agreement to agreement of the
rank-one natural families on their common domain.

```text
P_432_1 = CLOSED
```

The descent's honest non-edge-resolved boundary remains outside the shared
domain and is not hidden by `(V5-2)`.

### 7.2 P-432-2 — corrected restriction-square composition

The descent's cellular square is

```text
D_(G_N) P_f=rho_f D_(G_M).                        (V5-3)
```

For Q-313's identity zero extension, specialize

```text
P_f=j_NM^Q,
rho_f=rho_G,MN,
D_(G_N)=T_(N,G_N)^char,
D_(G_M)=T_(M,G_M)^char
```

using `(V5-2)`. Then `(V5-3)` becomes exactly V002's repaired square:

```text
T_(N,G_N)^char
 =rho_G,MN T_(M,G_M)^char j_NM^Q.                 (V5-4)
```

Every domain and codomain matches the V1 table.

```text
P_432_2 = CLOSED
```

### 7.3 P-432-3 — joint-foundation readiness

V002 supplies everything this seam awaited from relay 432:

```text
rank-one extension formula,
exact-equation uniqueness,
typed zero-extension square,
agreement with Q-313/Q-315.
```

However P-432-3 was explicitly defined to await **external review/merge**.
At register head Q-352, relay 434—the independent cross-review of the descent
itself—is still outstanding. This cross-review cannot substitute for that
separation-of-custody step.

```text
P_432_3_V002_DEPENDENCY = CLOSED
P_432_3_EXTERNAL_DESCENT_REVIEW = OPEN | relay:434
P_432_3 = OPEN
```

Thus the exact final seam status is:

```text
DESCENT_PENDING_SEAMS = OPEN | P-432-3 only
```

The openness is procedural/evidentiary, not a newly found mathematical
incompatibility between V002 and the descent.

```text
V5 = PASS_WITH_STATUS_SPLIT
```

---

## 8. V6 — fresh attack on the repaired square

### 8.1 Non-identity refinement split

The installed `j_NM^Q` uses the canonical identity extension
`u->(u,1)`. Attack the theorem with a genuinely split two-cell history:

```text
(a,b) in U(1)^2,
ab=u,
a and b otherwise arbitrary.                      (V6-1)
```

This is not `j_12^Q(u)` unless `b=1`. Nevertheless the terminal character is

```text
Z_2(a,b)=(ab)^n=u^n=Z_1(u).                       (V6-2)
```

For any admitted rank-one target restriction obeying `(V1-1)`,

```text
Hol_(c_GN)[rho_G,21 T_(2,G_2)^char(a,b)]
 =Z_2(a,b)
 =u^n
 =Hol_(c_GN)[T_(1,G_1)^char(u)].                  (V6-3)
```

Injectivity again gives equality of quotient outputs. Therefore the
rank-one **output** does not depend on how the terminal character is split
between two fine cells.

This does not create a canonical coarse-to-fine source section: the family
of pairs `(a,b)` with `ab=u` remains nonunique. V002 does not claim such a
section. It claims the canonical zero-extension square and terminal-scalar
factorization, both of which survive.

```text
NONIDENTITY_SPLIT_CHANGES_RANK1_OUTPUT = false | TYPE-R
NONIDENTITY_SPLIT_DEFINES_CANONICAL_SOURCE_SECTION = false | TYPE-R
FRESH_ATTACK_RESULT = SURVIVES
```

### 8.2 Primitive-class boundary attack

If a target arrow sent the primitive cycle to a nonprimitive multiple
`k c`, `|k|>1`, then its holonomy relation would be

```text
Hol_(c_GN) rho=(Hol_(c_GM))^k,
```

not V002's premise `(V1-1)`. Such an arrow could not satisfy the repaired
square for generic `Z` without a matching source power. V002 expressly scopes
its theorem to arrows carrying the primitive class, so this is a boundary
test, not a counterexample.

```text
NONPRIMITIVE_DEGREE_ARROW_INCLUDED = false | TYPE-S
SCOPE_OVERCLAIM_FOUND = false
V6 = PASS
```

---

## 9. Final determination

V002 meets the V001 cross-review exactly:

1. `j_NM^Q` is installed at the missing source precomposition;
2. the corrected chain ends at Q-313's `Z_M j_NM^Q=Z_N` identity;
3. all four corners of the restriction square are typed;
4. uniqueness is limited to the exact factorization equation;
5. every changed hunk is disclosed;
6. confirmed terminal-scalar classification, obstruction, and kernel/image
   results are carried without mathematical alteration;
7. the regression executes on an explicit fixed-square `N=1`, `M=2` pair;
8. the repaired theorem composes with the constructed descent on their
   shared rank-zero/rank-one domain.

The two mathematical descent seams dependent on V002 are closed. The third
remains open solely because the independent descent review in relay 434 has
not yet returned at register head Q-352.

```text
V1 = PASS
V2 = PASS
V3 = PASS
V4 = PASS
V5 = PASS_WITH_STATUS_SPLIT
V6 = PASS

EXTENSION_V002 = CONFIRMED
DESCENT_PENDING_SEAMS = OPEN | P-432-3 only |
  reason: independent descent cross-review/joint merge relay 434 pending;
  P-432-1 and P-432-2 closed

RANK0_EXTENSION = CONFIRMED
RANK1_EXTENSION = CONFIRMED |
  scope: Hol_(c_G) compose T=Z_N and primitive-class-preserving arrows
TERMINAL_SCALAR_RANK_GE_2_OBSTRUCTION = CONFIRMED
PREFIX_FAMILY_DESCENT_COMPATIBILITY_RANK01 = CONFIRMED

FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S
TRANSVERSE_ACTION_COMPARISON_SQUARE = NOT_BUILT / TYPE-U
PHYSICAL_P_VERDICT = NO_VERDICT

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No alpha, `K_*`, root, response value, rank ratio, or measured constant was
evaluated.

