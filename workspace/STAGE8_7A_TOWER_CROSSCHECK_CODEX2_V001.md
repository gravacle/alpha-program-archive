# Stage 8 / 7A / Q-126 route — adversarial cross-check of the rebuilt tower

**Lane:** CODEX 2  
**Relay:** 767  
**Instruction:** refute the rebuilt tower if any load-bearing step fails  
**Overall disposition:** **REFUTED**, with the twisted spectrum and Casimir retained

## 0. Pickup, pins, and scope

The sole relay `RELAY_PASTE_767_TOWER_CROSSCHECK_CODEX2_V001.md` passed its adjacent seal before reading: artifact SHA-256 `77597cd593ba7e8d449d96216210d359815fbb84312aab81ccdecaa188aefc2f`, sidecar SHA-256 `25c7b26616a28d6e43688eaf3e67dd42f61b234a06eff67fce9ff44a43edc144`. The CODEX 2 lane guard matched; report, ACK, and DONE names were absent; `relay_outbox/767_ACK.md` was written before subject inspection.

| Source | SHA-256 | Status used here |
|---|---|---|
| `STAGE8_7A_TOWER_REBUILD_DARIO_V001.md` | `84ceeb49dd282736ce0cb1347e923c8a8c9b1d26ea151ccbb19f6d857dd9e0bf` | adjacent seal verified; sidecar SHA-256 `757a12cb3f4e57f4f9c4fb3c46a49cc4fa4ddc643abdd225a1a60bc98865e217` |
| `alpha_global_record_surface_superconnection_principle_v001.md` | `ae1d04922cb37f8b5631a11551b7db57f483bd6b0d8b7c54d59b4f4ae593768f` | digest-matched mirrored principle; operator `[1076,1194)`, parent carrier `[1194,1484)`, free-data list `[1532,1729)`, failure rule `[2022,2360)` |
| `alpha_br_full98_c2_two_cutoff_continuum_theorem_v001.md` | `7a3c6bc66257604916a95d82d1ac83c33332a64f7ab379d264c20f471efb829b` | unsealed `PROPOSED_NOT_CLOSED` target; fixed scope `[244,644)`, locked spectrum `[797,969)`, gap bar `[3948,4051)` |
| `STAGE8_7A_DBR_PUBLIC_LAYER_DARIO_V001.md` | `beff9f11263e6d9069d77980ea5fc455ae0ea65e1f4ee9629ba6415937a8b075` | adjacent seal verified |
| `STAGE8_7A_DBR_SPECTRUM_DARIO_V001.md` | `a27453107bc97fce05e377b696055c8c24d71d4888e9097fae146a5518cf9e20` | adjacent seal verified |
| structural spectral-gap determination | `e2fc00d21fdc4a1844648b7248140ab05d9205a652a2b42330c1a366d53e33ed` | adjacent seal verified |

No value was selected. The computations below are exact representation-theoretic identities, rational Casimirs, and integer multiplicities; no physical quantity or measured constant was evaluated.

## 1. AP1 — monopole-twisted `S^2` spectrum

### 1.1 Independent derivation

Let `L -> S^2` have degree `2q in Z` and let `D_q` be the unit-sphere Dirac operator twisted by `L`. Rotational covariance decomposes the twisted spinors into total-angular-momentum irreducibles. With long `su(2)` roots in the standard normalization, the square on the spin-`j` summand is

```text
D_q^2 = J^2 + 1/4 - q^2,
J^2 = j(j+1),
j = |q|-1/2+n,  n=0,1,2,...  when q != 0.
```

The first identity is the monopole angular-momentum form of the twisted Lichnerowicz operator: the curvature coupling subtracts `q^2`, while spin curvature supplies `1/4`. It was derived from the `SU(2)` decomposition, not copied from the tower report.

Writing Dario's `l` for `j` and `ell=n` gives

```text
l(l+1)-q^2+1/4
  = (l+1/2)^2-q^2
  = (ell+|q|)^2-q^2
  = ell(ell+2|q|).
```

This is an exact polynomial identity. A rational regression over `2|q|=1,...,9` and `ell=0,...,32` returned no mismatch; the regression is a check, while the displayed factorization is the proof.

### 1.2 Zero level and index

At `ell=0`, the eigenvalue square is zero and the `SU(2)` irrep has dimension

```text
2j+1 = 2(|q|-1/2)+1 = 2|q| = |deg L|.
```

Nonzero levels pair under chirality because `D_q` anticommutes with the sphere grading. The bottom level cannot pair: the index is `ind(D_q)=deg L=2q`, so its `2|q|` states occupy one chirality (which chirality is an orientation/sign convention). This confirms the zero-mode level and multiplicity.

### 1.3 Locked floor and the `+1`

For the nonzero monopole ladder,

```text
ell(ell+2|q|)-ell(ell+1) = ell(2|q|-1).
```

Thus the locked floor is attained at `|q|=1/2`; for every quantized nonzero charge it is a lower bound, and equality at every level occurs iff `|q|=1/2`. The report is correct on this exact comparison.

The `+1` in the unsealed target is an explicit background offset. Because the twisted sphere has a zero bottom level, that offset is sufficient to retain the target's displayed unit gap independently of the sphere term. Two qualifications are mandatory:

1. it is not the only positive term on the fixed 16, since a positive `C2_parent` is also present; and
2. neither source identifies the `+1` with `Phi^dagger Phi`. The principle leaves `Phi` unselected, while the target merely displays `+1` in `A0^dagger A0`'s spectrum.

The tower report's stronger sentence that the floor's “real content” is nonzero flux is not derivable from the locked inequality alone. The untwisted unit-sphere spectrum

```text
lambda_k^2=(k+1)^2,  k=0,1,...
```

also obeys `(k+1)^2 >= k(k+1)`. Moreover, the target's fixed external full98 label `q=(+/-1,0)` is nowhere identified with the monopole degree `2q`. The twisted-spectrum calculation is confirmed; the asserted selection of a nonzero chiral index is not.

**AP1 verdict: CONFIRMED for the twisted spectrum, zero modes, minimum-charge floor, and background-offset role; REFUTED for the claimed nonzero-index inference and the ungrounded identification `+1=Phi^dagger Phi`.**

## 2. AP2 — `Spin(10)` chiral 16, Casimir, and multiplicity

### 2.1 Casimir from the sealed representation datum

The principle fixes `E_parent = Lambda^even(C^5)`, the chiral spinor of `Spin(10)`. Its dimension follows without a table:

```text
sum over even k of binomial(5,k) = 2^4 = 16.
```

For `D_5` with long roots of squared length 2, choose the chiral highest weight and Weyl vector

```text
lambda = (1/2)(e1+e2+e3+e4+e5),
rho    = 4e1+3e2+2e3+e4.
```

Then

```text
(lambda,lambda+2rho)
  = 5/4 + (4+3+2+1+0)
  = 45/4.
```

In the tower's explicitly stated half-normalized Casimir convention, the vector has `C2(10)=9/2`; therefore

```text
C2(16) = (1/2)(lambda,lambda+2rho) = 45/8.
```

The value is confirmed in that convention. The sealed representation datum alone does not choose the factor `1/2`, and the tower report correctly records this normalization dependence.

### 2.2 Additive placement

The target writes

```text
K0=A0^dagger A0+C2_parent
```

and its locked eigenvalue display places `C2_parent` additively. Since the quadratic Casimir is scalar on an irreducible 16, this placement is algebraically consistent whenever the parent connection factorizes as assumed. The principle leaves the parent bundle and characteristic class free, so the flat `x16` factor is conditional rather than sealed; the tower report discloses that condition.

### 2.3 Multiplicity audit

At one `T^2` momentum point, `D_T2^2` acts on a rank-2 complex spinor fiber. At a nonzero sphere level, both Dirac signs contribute to `D_S2^2`, each with multiplicity `2l+1=2(ell+|q|)`. Hence

```text
generic nonzero-level spin multiplicity
  = 2 x 2 x (2l+1),
```

which is exactly four times the old one-sign, no-`T^2` count. Tensoring the internal 16 gives fiber rank `2 x 2 x 16=64`; the leading Weyl coefficient is therefore corrected by `x4`.

The phrase “wrong by exactly a factor of four” is not valid at the zero level. There the sphere modes are unpaired, so the old factor `2|q|` was already correct and only the omitted rank-2 torus spinor remains:

```text
ell=0 correction = x2, not x4.
```

The tower report's final piecewise formula has this exception correctly, but its unqualified headline and repeated “exactly x4” claim do not. Exact-rational checks gave `x4` for every tested `ell>=1` and `x2` at `ell=0`.

**AP2 verdict: CONFIRMED for `C2(16)=45/8` in the stated convention, additive placement, rank 64, and the generic/nonzero-level `x4`; qualified by an `x2` zero-level correction that refutes the unqualified factor-four claim.**

## 3. AP3 — cross-grade term and grade accounting

### 3.1 Operator formula

The principle displays

```text
D_BR^2 = D_(Sigma,A)^2
       + Gamma_Sigma[D_(Sigma,A),Phi]
       + Phi^dagger Phi.
```

No sealed sentence cancels the middle term, makes `Phi` covariantly constant, or sets `Phi^dagger Phi=1`. The same principle explicitly lists `Phi` as unselected. Thus carrying the cross term is required.

### 3.2 Failing grade step

Let the bidegree record spinor parity first and internal parity second. Then

| Term | Bidegree | Total parity |
|---|---|---:|
| `D_Sigma,A^2` | `(0,0)` | even |
| `Gamma_Sigma[D_Sigma,A,Phi] = Gamma_Sigma c(nabla_A Phi)` | `(1,1)` | even |
| `Phi^dagger Phi` | `(0,0)` | even |

`Gamma_Sigma` is even as a spinor-grading operator. The commutator contains one Clifford-odd factor and one internal-odd factor. It therefore flips the two factor gradings simultaneously but preserves the total grading. This is forced independently by the fact that `D_BR` is odd and the square of an odd operator is even.

The tower report calls the middle term “odd in the grading” and says it couples the even and odd sectors. That is false for the total superconnection grading. It may be described as off-diagonal in either factor separately, but it does not couple the two total-parity sectors.

### 3.3 Failing eigenvalue step

With `Phi` unselected, `Gamma[D,Phi]` is an operator-valued, generally mode-mixing term. Nothing sealed proves it commutes with the geometric square or the Casimir. Consequently it cannot be appended inside a scalar formula headed

```text
lambda_a(p_t,p_q,ell;q) = ... + [Gamma[D,Phi]] + ...
```

without either selecting `Phi`, proving the commutator zero, or diagonalizing the full operator. None of those steps exists. The operator decomposition is valid; the claimed exact scalar tower is not rebuilt from it.

**AP3 verdict: REFUTED.** Noncancellation is confirmed, but the report's total-grade label and its scalar-eigenvalue assembly both fail.

## 4. Free-data ledger re-derived

The principle's `[1532,1729)` supplies five free-data classes, with the three radii grouped as one geometric class:

| # | Free-data class | Sealed status |
|---:|---|---|
| 1 | `(R_T,R_flux,R_Q)` | unselected |
| 2 | spin structure on `T2_TQ` | unselected |
| 3 | parent bundle and characteristic class | unselected |
| 4 | odd profile `Phi` | unselected |
| 5 | chiral index | unselected |

The hard failure rule `[2022,2360)` explicitly tests inequivalent radii, spin structure, bundle class, or odd profile. It does not name chiral index, even though the preceding list leaves the index free.

The claimed “single constraint” `|q|>=1/2` does not follow from either source:

- the locked inequality is also obeyed by the untwisted sphere spectrum;
- the target never equates its external full98 mode label with `deg L/2`;
- the principle explicitly leaves the chiral index unselected; and
- the target is scoped to a fixed periodic spin structure and external mode, which is a target restriction, not a derivation selecting the principle's free data.

Likewise, `+1` cannot be counted as a constraint on `Phi` because no source binds it to `Phi^dagger Phi`. The five-item ledger is re-derived, but the asserted `+1` constraint is absent. This is a **divergence**, not `5+1`.

## 5. Verdict table

| Item | Verdict | Decisive step |
|---|---|---|
| twisted `S^2` spectrum | **CONFIRMED** | `D_q^2=J^2+1/4-q^2`; exact reparametrization and index multiplicity |
| Casimir on chiral 16 | **CONFIRMED** | raw `D5` value `45/4`; `45/8` in the displayed half-normalization |
| generic multiplicity correction | **CONFIRMED WITH EXCEPTION** | `x4` for `ell>=1`, `x2` at the unpaired zero level |
| cross-grade handling | **REFUTED** | bidegree `(1,1)` is total-even; unselected operator cannot be a scalar eigenvalue summand |
| five free-data classes | **CONFIRMED** | verbatim principle list |
| claimed one additional constraint | **REFUTED** | no sealed bridge from locked floor/external label to nonzero monopole index |
| rebuilt tower overall | **REFUTED** | load-bearing cross term prevents the claimed exact scalar tower |

## 6. Battery, custody, and verb audit

The exact-rational battery checked nine half-integral absolute charges across 33 levels, the factorized floor difference, the `D5` weight formula, the vector normalization, and generic/zero-level multiplicities. M-2 searched fixed formula strings, normalized symbol variants, punctuation variants, and the bounded source vocabulary for a cancellation, a covariant-constancy condition, a Casimir normalization, a monopole-index binding, and a `+1=Phi^dagger Phi` binding; none exists in the two governing texts.

No alternative datum was chosen to manufacture the refutation. The confirmed sub-results remain confirmed; the overall verdict turns only on displayed failing steps. No corpus member was bound, no fixed point or end test ran, no evaluator chain ran, and no physical quantity or measured constant was evaluated. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false` remain in force.

Verb audit: **CLEAN**. “REFUTED” applies to the claim that the full scalar tower was rebuilt exactly. It does not refute the monopole spectrum, the index count, the Casimir value in its stated convention, or the generic rank correction.

TWISTED_SPECTRUM = CONFIRMED
CASIMIR_16 = CONFIRMED (45/8 in C2(vector)=9/2 convention; raw D5 value 45/4)
CROSS_TERM = REFUTED
FREE_DATA = divergence (5 free classes re-derived; claimed +1 constraint not sealed)
OVERALL = REFUTED
VOID = clean
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
