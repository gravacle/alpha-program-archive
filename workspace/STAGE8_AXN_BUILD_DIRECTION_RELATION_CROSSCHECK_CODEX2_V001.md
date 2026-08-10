# STAGE 8 / [PLAN:AXN-BUILD-A18] — DIRECTION-RELATION CROSS-CHECK AND `A_c` SUPPLIER HUNT
## CODEX 2 LANE — V001

Relay 851. Lane guard: `CODEX 2`. Inbox seal
`8c2e12abd7015509ae087479221a9ec09692cbff2f3699b72529622ae9d785d1`
verified before reading; pickup acknowledgement written first. State brief
`PROGRAM_STATE_BRIEF_V005.md` =
`e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`
verified and read. Subject
`STAGE8_AXN_BUILD_DIRECTION_RELATION_DARIO_V001.md` =
`a94e9ae1ec80a3a507811df8b2e55fd100e3d43f5c8da5124aa2f040654a7e49`
and its sidecar verified before reading.

GATES: `alpha_computed = false`; `proof_authorized = false`;
`kappa_record_computed = false`. No member binding, fixed-point execution,
end test, numerical evaluation of a physical quantity, comparison to a
measured constant, smooth import, or electromagnetic identification occurred.
All headline register items are `CLAIMED`; PE-1..PE-12 remain pointer-only.

---

## 1. Verdict map

| claim in 849 | verdict | source-level reason |
|---|---|---|
| D1 support preservation | **CONFIRMED AFTER CARRIER-NEUTRAL RENDERING** | CIS makes `Omega_c` parent-assigned and requires `support(L_c) subset Omega_c`; every admitted member of a later-supplied same-`c` path must preserve that support. The displayed additive expression `L_c + epsilon delta L_c` is not licensed yet because 847 proves no additive/affine carrier for `A_c`. |
| D2 one-use preservation | **FORCED, WITH A QUALIFICATION TO THE IMPLICATION** | One-use is preserved automatically only after the candidate is typed as a path/neighbor through the *same incidence* `c`. Support containment alone does not encode incidence identity or forbid a duplicate use. Thus D2 is redundant in the fixed-incidence path relation, but it is not a theorem of D1 alone. |
| D3 new-record-factor targeting | **CONFIRMED AND INDEPENDENT, CARRIER-NEUTRALLY** | CIS permits shared source support yet requires later incidences to use their own new record factors. A same-support candidate can still target an earlier record factor, so D1 does not imply D3. The statement applies to each admitted same-`c` path member; `delta L_c` remains unavailable until the carrier supplies that form. |
| CIS as stabilizer, not generator | **CONFIRMED** | CIS states preservation/admission restrictions and explicitly says it supplies only the microscopic support law. It neither enumerates nor constructs directions. |
| CIS supplies lawfulness completely | **CORRECTED IN SCOPE** | CIS supplies the complete *CIS preservation predicate* once a carrier and same-`c` path/neighbor relation are supplied. It does not supply a complete executable lawfulness relation while the very type of “direction” is absent. |
| packet receivers declined | **CORRECT** | The record carrier `R_c`, fixed receiver `c_c`, multiplication operator `M_c(t)`, common-domain obligations, and Galerkin allowance are receiver/operator structures. No sealed U1 map pulls them back to admissible `L_c` directions. |
| transport/incidence identities declined | **CORRECT** | The exact `sd*_2 d'_1 = d_1 sd*_1` and 36+882 identities are explicitly typed as a finite connection–coframe transport projection. No sealed relation binds that carrier `S` to `L_c` or `A_c`. |
| SC5 uncoupled | **CONFIRMED** | Neither the derivation nor this correction consumes a boundary prescription, B0 object, U3 package, or global-to-cell descent. SC5 remains its separate absence chain. |
| six components reduce to `A_c` plus the triple | **CORRECTED** | Sharing the subject `A_c` is not a binding proof. Membership, a path relation, U1-total closure, and primitive-scope completeness remain separate obligations; the triple conditionally sharpens only the CIS-preservation component. |

### 1.1 Pins and controlling spans

| object | SHA-256 | controlling span |
|---|---|---|
| 847 SC4 typing | `e28ac418d87cb240acb5bfce0253c65905d4b7418349a45bbf0f324525b51fda` | bytes `[17830,18243)`, span SHA `c2d31f7a1135b16dc18b32de7329b0e30b18f55870bd94aabf90a264b0405448` — the six-component `SC4_NATIVE(c)` list |
| CIS | `b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30` | bytes `[513,1397)`, span SHA `836f6b65b289c88a9bc928562aa646225a5c0bedd894119ad0215e9a08c5dc1e` — parent-assigned cell, support, one-use, and new-factor clauses |
| packet parent | `40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9` | bytes `[4287,4905)`, span SHA `a4953cb66daa6dacf588351447c24defea88068681cbd586e7dd8452a1207f6a`; bytes `[5711,6867)`, span SHA `eddc2e9ab66e1036e7defdc514b61214e0adef3b48fced3c3aa7a67b6df5f2c3` |
| transport projection | `a449cfb31b4c96569c8a2845bc4b018affa157b1d95b87f8dcddca646197537c` | exact connection–coframe transport equations and the source's own no-action-form-direction conclusion |

---

## 2. The stabilizer triple, repaired at its binding boundary

### 2.1 What the sealed bytes actually license

CIS assigns one Lorentz-covariant causal cell `Omega_c` and one primitive
interaction density `L_c` per incidence, requires the density's support to lie
inside that cell, removes a completed incidence from later reuse, and requires
new incidences to act on their own new record factors. Therefore, for any
later-supplied admissible path or neighbor relation through the same incidence
`c`, every member on that path must satisfy:

```text
D1(c,L') := support(L') subset Omega_c
D2(c,L') := L' remains the one use assigned to incidence c
D3(c,L') := L' acts only on c's own new record factor and not an earlier one
```

This is deliberately carrier-neutral. The sealed corpus has not said that
`A_c` is linear, affine, a manifold, a discrete generator set, or a path-germ
space. Consequently it has not licensed addition, scalar multiplication,
`epsilon`, or a tangent object `delta L_c`. The expression
`L_c + epsilon delta L_c` in 849 presupposes one of the still-open answers to
the very carrier question under review.

### 2.2 The D2 implication and the two-constraint collapse

The narrow collapse survives, but its stated proof needs repair:

```text
same-incidence path typing + D1  =>  D2 is not an additional direction predicate;
D1 alone                         !=  D2.
```

Support inside `Omega_c` does not, by itself, prohibit a second use bearing the
same support. The no-duplicate conclusion comes from the premise that the
candidate is a variation/path member of the already assigned incidence `c`,
combined with CIS one-use typing. Once that premise is explicit, D2 is part of
the path's typing rather than a third independent preservation predicate.

Accordingly, CIS leaves two independent *content* predicates on an already
typed same-`c` candidate:

1. support remains inside `Omega_c`; and
2. the target remains `c`'s own new record factor.

The independence argument for D3 is sound. Two incidences may share source
support, and overlapping cells do not identify record factors. A candidate may
satisfy D1 while wrongly coupling to an earlier record factor; conversely,
correct targeting does not prove support containment.

---

## 3. Structural characterization

The conservation-of-typing diagnosis is correct. CIS is a stabilizer law: it
tests whether a supplied candidate preserves incident support, use identity,
and record-factor typing. It is not a generator and supplies no candidate.

849's sentence “CIS supplies lawfulness completely” is too broad in the
current type state. There is no executable domain on which that complete
relation could be evaluated. The binding-safe statement is:

```text
CIS supplies the complete CIS-preservation predicate
CONDITIONED ON a supplied A_c carrier and a supplied same-c path/neighbor relation.
CIS is silent on existence and does not supply that relation.
```

This preserves the real narrowing without turning a conditional predicate into
a constructed object. It also respects CIS's own statement that it supplies
only the microscopic support law and may not choose a generator, density,
cutoff, or response normalization.

---

## 4. Declines and separation

### 4.1 Packet receiver structures

The packet parent supplies a finite receiver carrier
`R_c = span{r_c,p_c,e_c}`, a fixed vector `c_c`, distinct record factors, and a
parent in which `M_c(t)` is multiplication by a causal-cell spatial section;
it permits a Galerkin compression in the finite regulator. These objects
receive or evaluate an interaction. They do not declare the class of
primitive interaction densities, its direction relation, or U1. The decline
is therefore correct and prevents the same action/output conflation rejected
in round 1.

### 4.2 Transport/incidence identities

The 36+882 exact identities and `sd*_2 d'_1 = d_1 sd*_1` constrain the sealed
connection–coframe transport projection. The source itself distinguishes this
finite transport object from action-form directions. No relation to `L_c` is
sealed. S13 therefore requires declining the proposed transfer.

### 4.3 SC5

No cited inference consumes SC5 or produces any of its five absent carriers.
SC4 remains freedom-shaped/typing-open; SC5 remains absence-shaped. They are
conjunctive blockers at the H1 gate, not derivationally coupled here.

---

## 5. Relocation checked against 847's exact list

847's byte-pinned list contains six separately receiving obligations:

| # | exact component | disposition after this check |
|---:|---|---|
| 1 | one declared carrier `A_c` for admissible primitive interaction densities | OPEN; neither branch supplied |
| 2 | a membership statement `L_c in A_c` | OPEN as a binding object; CIS support is not this membership declaration |
| 3 | the admissible-direction/path relation through each admitted `L_c` | OPEN as an object; conditionally constrained by the repaired CIS predicate |
| 4 | closure sufficient for class-wide variation U1 to be defined | OPEN; being “about `A_c`” does not prove closure or U1 totality |
| 5 | preservation of CIS support, one-use, and new-record-factor typing | CONDITIONALLY SUPPLIED as the repaired D1/D2/D3 predicate |
| 6 | proof that the declaration is complete at the claimed primitive scope | OPEN; no generator/corpus enumeration or no-outside proof exists |

Thus component 3 does not reduce to component 1 plus the triple unless the
carrier declaration itself includes and proves its path structure. Components
4 and 6 remain proof obligations even after a carrier form is named. The load
is not one unstructured choice called `A_c`; it is the six-component binding
package, with component 5 now sharply characterized and the rest still open.

---

## 6. Law-9 supplier hunt

### 6.1 Search universe and over-generation

The bounded search walked 2,047 sealed-stock text/data candidates (`md`,
`json`, `txt`, `csv`, `tsv`, `yaml`, `yml`), excluding relay custody files,
run outputs, holdout material, `.git`, the questions register, and expectation
fixtures. Case/spacing/hyphenation and semantic expansions covered:

| query family | over-generated hit count |
|---|---:|
| exact `L_c` forms | 28 |
| `A_c` symbol forms | 46 |
| finite manifest/generator/completeness terms | 53 |
| continuum section/function/carrier terms | 169 |
| receiver/evaluator near-misses | 858 |
| transport/incidence identity terms | 70 |

The exact SC4-specific semantic probe
`admissible primitive interaction densities | carrier A_c for admissible |
finite generator manifest for A_c | section/function carrier for A_c`
returned only 847, 849, the questions register, and this relay assignment.
Those are the requirement, its restatement, and custody records—not an
independent supplier. A cross-probe requiring finite-manifest or
section-carrier language near `L_c` found no independent source.

### 6.2 Finite-branch fragments

| sealed fragment | pin | what it supplies | why it is not the required manifest |
|---|---|---|---|
| CIS | `b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30` | per-incidence support, one-use, new-factor admission typing | no `A_c` member list, generator list, enumeration certificate, or no-outside proof |
| one-normal zero-form enumeration | `50b5a651df2aca90ee47c6f85b2a502461370a652706ebccad871f191565a2d9` | finite pointwise zero-form inventory and one-complex-dimensional incidence line | receiver/operator inventory; no binding to primitive action-density directions |
| member grammar | `a036bcca07e8405c1d17b96b211769050a104943e2d86cb32c0606b9f641a24f` | finite labels and grammar fragments | census explicitly open; no complete generator manifest or no-outside certificate |
| native finite-algebra audit | `4065fdcc77211d27fd06a95b6c6a572de1a2f8f29cdb065bc6e4c71b1e282f9d` | a real universal incidence-algebra/filtration skeleton | explicitly lacks coefficient descent, full response/action-universe coverage, and no-outside completeness |
| transport projection | `a449cfb31b4c96569c8a2845bc4b018affa157b1d95b87f8dcddca646197537c` | finite exact connection–coframe identities | different carrier; no sealed map to `L_c` |

No finite candidate supplies both the generator inventory *and* its primitive-
scope completeness proof.

### 6.3 Continuum-branch fragments

| sealed fragment | pin | what it supplies | why it is not the required carrier |
|---|---|---|---|
| CIS `Omega_c` | `b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30` | a Lorentz-covariant causal support cell | a support region is not a section/function carrier and provides no path topology |
| packet `M_c(t)` and spatial section | `40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9` | multiplication operator and its continuum receiver section; finite Galerkin receiver allowed | receiver-side object; no `A_c` declaration, membership, or U1 closure |
| P2 source topology/calculus | `40b2af34443e051fffdc7bf2ec7025c811a98c501a82d19164596ee6f37f00c1` | source/germ Banach and trace-class carriers | different typed carrier; no binding to primitive `L_c` densities |
| local cell measure selector spec | `05233fb27ba6852b2ddb99bc06794ce0c0f67fe5046f4af538c3dc9484da054e` | forward alternatives involving finite-jet data or boundary profiles | competing readings in a specification, not an adopted and complete `A_c` carrier |

No continuum candidate declares a section/function carrier for all admitted
primitive `L_c`, its membership relation, its admissible paths, and closure
sufficient for U1. These fragments evaluate, localize, or receive candidate
objects; they do not supply the missing carrier.

### 6.4 Hunt verdict

Both complete supplier branches are absent. The result is reported as
`PARTIAL`, rather than hiding the typed fragments: the corpus contains finite
operator/generator-like structures and continuum support/section-like
structures, but each fails the meaning probe at the `A_c` binding or the
completeness receiver. No branch is selected.

---

## 7. FREEDOMS-CONSUMED

| datum | treatment |
|---|---|
| `A_c` form | CARRIED-AS-PARAMETER; finite and continuum branches both left open |
| ambient direction/path structure | CARRIED-AS-PARAMETER; no addition, scalar multiplication, tangent, topology, or discrete adjacency authored |
| `L_c` membership | CARRIED-AS-PARAMETER; support typing is not promoted to a complete membership manifest |
| `Omega_c` | CARRIED-AS-PARENT-DATA; not varied |
| fixed-incidence path premise | CONDITIONED-ON; used only to state the D2 redundancy, not supplied here |
| packet receiver/operator structure | DECLINED as an action-direction supplier |
| transport/incidence identities | DECLINED as a different-carrier supplier |
| U1 closure and primitive-scope completeness | CARRIED-AS-OPEN proof obligations |
| SC5 | CARRIED-AS-SEPARATE absence chain |
| scaling weights | NONE CONSUMED |
| substitutions or selections | NONE |

---

## 8. FLATTENING CHECK, battery, and self-audit

The 37-row decline register was walked. S03/void remains live at the temptation
to assume a linear or affine carrier; S12 bars promotion of finite labels and
status words into a complete manifest; S13 bars identifying `S` with `A_c`;
S26/S08 bar importing a smooth section space or electromagnetic identity;
S19/S24 bar using packet or source carriers to close the missing action
carrier. T5 is untouched.

```text
FLATTENING_CHECK = CLEAN (37/37)
F_PLDEC          = PASS
ANTI_TUNING      = PASS
M2               = PASS (case, spacing/hyphenation, boundary, and semantic-carrier modes)
LAW9             = PASS at stated 2,047-file search scope
PIN_CHECK        = PASS before seal
PE_POINTER_ONLY  = PASS
```

Verb audit controls: every conclusion is typed as a check of a `CLAIMED`
subject; “derived” is restricted to the conditional preservation predicates;
no missing carrier is said to exist; no source fragment is promoted across its
receiver; no supplier branch, member, smooth carrier, or physical identity is
selected.

TRIPLE = CORRECTED (D1 and D3 confirmed carrier-neutrally; additive delta-L form unbound; D2 redundant only under fixed-incidence path typing)
COLLAPSE = CONFIRMED (two independent CIS content predicates after the fixed-incidence qualification; not an implication of D1 alone)
STRUCTURAL = CORRECTED (stabilizer-not-generator confirmed; CIS supplies a conditional preservation template, not a complete executable lawfulness relation)
DECLINES = CORRECT (packet receiver and transport-carrier sources displayed)
RELOCATION = CORRECTED (components 2, 3, 4, and 6 remain separately binding; component 5 is conditionally supplied)
A_C_SUPPLIER = PARTIAL (finite and continuum fragments displayed; both complete supplier branches absent)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+6 scope controls: CLAIMED subject retained; additive structure not assumed; D2 implication qualified; receiver/carrier types kept distinct; no branch selected; SC5 uncoupled)
