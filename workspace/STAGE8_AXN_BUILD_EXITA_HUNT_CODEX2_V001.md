# STAGE 8 / [PLAN:AXN-BUILD-A10] — CIRCULARITY CHECK AND EXIT-A HUNT
## CODEX 2 LANE — V001

**Date:** 2026-08-09  
**Status:** CLAIMED — every headline in this artifact awaits the opposite lane's adversarial pass.  
**Scope:** PASTE 843 only. No action member, coefficient, carrier, topology, normalization, or physical identification is selected here.  
**Subject:** `STAGE8_AXN_BUILD_H1_INTEGRAND_DARIO_V001.md`, SHA-256 `e3c559875d68a55e436ab9155458fa5670e55a4c9adf455a545aebf5935090fb`.  
**Custody:** cleanroom-only write; registrar mirrors. Builder-never-verifies is respected: this lane adversarially checks Dario's claimed finding and does not upgrade its own claims.

---

## 0. Preflight, law, and pins

The relay inbox seal was verified before reading. `843_ACK.md` was written before the relay was opened. The pinned state brief was verified and read before task work.

| Object | SHA-256 | Pin result |
|---|---|---|
| `PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | PASS |
| `LOCKED_PROCESS.md` | `eae8f9d6f44ef1611b69cbc7d7bac735f7cfde44b6b1c3a2f4af6f1504a54066` | PASS |
| `DECLINE_REGISTER_V002.md` | `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | PASS |
| `AXN_BUILD_CHARTER_V001.md` | `c0ad6decf156ef06c34bc8886d433487dfdf518c650dd67d5de283febeb14542` | PASS |
| Dario 842 subject | `e3c559875d68a55e436ab9155458fa5670e55a4c9adf455a545aebf5935090fb` | PASS |
| Round-1 cross-check | `886cd9a36b66f3581413790ac617be722e3bfb7922ac40342493371c552ae53e` | PASS |
| Skeleton V2 | `5964b9c5ab6e8b429338d0c76c3b1d2b337c1d2bf6dd9f3caf1442df7b8d0f7a` | PASS |

Both sidecar spellings and packet/bundle membership were tested where applicable. `PE-1` through `PE-11` remained pointer-only; their contents were not opened or consulted.

Gates carried throughout:

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_binding = false
fixed_point_executed = false
end_test_executed = false
physical_numeric_evaluation = false
measured_constant_comparison = false
smooth_import = false
electromagnetic_identification = false
```

---

## 1. Task A — attempt to break the loop

### 1.1 The exact problem

Dario's corrected binding is borne out by the bytes. The six H1 clauses divide as follows (`H1_INTEGRAND` lines 50–99; the receiving correction is independently displayed by the round-1 cross-check at lines 148–193):

```text
C1       domain-side, primitive sector only:
         support(L_c) subset Omega_c; one-use; new record factors.

C2-C6    image/output-side tests:
         the required packet receiver, its unfitted envelope, its first-order
         record/incidence block, its mandatory square-generated descendants,
         and completed-record persistence.
```

C1 constrains support, not functional form, and it does not bound the permitted effective remainder (`H1_INTEGRAND` lines 101–113). Therefore the task is not simply to vary one known action. It is to find an `S_record` whose image under the action-to-output map satisfies C2–C6.

Let

```text
X  = the admissible record-sector integrands,
Y  = the output tuple tested by C2-C6,
U1 : X -> Y.
```

The demanded object is an `x in X` with `U1(x)` in the C2–C6 acceptance set. The sealed stock supplies neither such an `x` nor a class-defined `U1` whose inverse image can be formed.

### 1.2 The strongest bounded-subclass attacks

The following are the lawful partial schemes found in sealed stock. Each was tested as a possible loop-breaker rather than dismissed by name.

| Subclass / object | What is actually sealed | Partial operation that is lawful | Why it does not break H1 |
|---|---|---|---|
| `E_D={S_0,S_1}` | The source-parent pair is explicit except that both contain opaque `S_record[R,a,g]`; see `COMPLETE_PARENT_ACTION_UNDERDETERMINATION_GATE_V001.md` SHA `67816cfe…`, lines 26–64, and `STRATUM_TEST` SHA `6a316f1f…`, lines 75–91 and 179–186. | Compare their displayed source/Pauli terms; derive pair-local intersections and differences. | The object that U1 must vary is the same opaque symbol in both members. Restricting U1 to `E_D` does not define its value on either member's record sector. |
| `E_4={S_0,S_1,S_rot,S_BF}` | `S_rot` and `S_BF` are explicit boundary-record countermodels (`STRATUM_TEST`, lines 97–102 and 136–161). | Evaluate the T01 term-presence predicate; this already proves the source term is not family-forced. | Their status as packet-parent members is expressly untested (`STRATUM_TEST`, lines 229–240 and 258–275). No sealed map sends either boundary functional to the required record/incidence operator, envelope, descendants, and durability receiver. Varying them locally would test their own boundary equations, not H1's complete target. |
| Packet `h_K(t)` / `D_K` | R3.4 displays a first-order operator with the fixed envelope and its square-generated descendants (`R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md` SHA `40890e75…`, lines 103–190). | Replay the already-sealed output-side packet tests. | This starts in `Y`, not `X`. Inferring an action from it would author an inverse variational principle, its domain, and boundary data—the missing U1/pullback under another name. |
| Clause-local H3 | The cross-check derives `chi_P=0` on the sealed packet-parent branch (`ROUND1_CROSSCHECK`, lines 202–215 and 291–364). | Decide that one branch-scoped clause. | It proves that partial evaluation is lawful; it neither supplies `S_record` nor defines the remaining action-to-output map. |

**Attempted refutation result.** A partial variation on a bounded subclass would break the loop only if the sealed record already supplied both (i) integrands on that subclass and (ii) a map from their variations to H1's named packet receiver. `E_D` lacks (i) in the record sector. `S_rot/S_BF` lack (ii) and packet-parent admission. The packet operator is an output rather than an integrand. Thus every available partial operation is a local negative filter or output replay, not an H1 solver.

### 1.3 Why no independent Exit C exists

The two-exit classification is by carrier type, not by an assumed finite candidate list:

1. If an integrand is supplied independently and U1 is then applied to it, that is **Exit A**.
2. If a map is defined on any class or subclass so that C2–C6 can be pulled back, that is **Exit B**, including a bounded-subclass restriction of a class-wide scheme.

A supposed third route has only three possible shapes:

| Proposed Exit C shape | Classification |
|---|---|
| Directly import or derive a candidate before applying the output tests | Exit A by definition. |
| Define enough variational/inverse structure on a subclass to solve from the output tests | Restricted Exit B by definition. |
| Run clause-local predicates without a candidate-to-receiver map | Lawful partial evaluation, but not an exit from the H1/U1 mutual gate. |

A certificate that no inhabitant exists would kill the route rather than exit the loop. No such certificate is of record. Consequently the A/B dichotomy is exhaustive at H1's receiving type, and the strongest apparent Exit C reduces to restricted Exit B or to a non-solving local test.

### 1.4 NOT-EMPTY and tally

`H1_INTEGRAND` lines 121–135 explicitly distinguishes `UNDECIDABLE` from `EMPTY`: no nonexistence certificate exists. The member grammar independently says the global action/P5 census is open, several mutation directions remain only schematic, and no no-outside proof exists (`STAGE8_AXN_MEMBER_GRAMMAR_CODEX2_V001.md` SHA `a036bcca…`, lines 32–41, 321–360, 486–524). Therefore an `EMPTY` route verdict is not licensed. This is a certificate-status finding, not an assertion that a complete physical member has been selected or exhibited.

The cross-check's receiving-predicate tally is reproduced without drift (`ROUND1_CROSSCHECK`, lines 202–227 and 431–434):

```text
DECIDED, branch-scoped  = 1  (H3)
NARROWED                = 3  (H1, H4, H5)
UNMOVED                 = 7
UNPRESSED               = I6
```

Sixteen remains a lower bound, not a no-outside census.

---

## 2. Task B — Exit-A hunt

### 2.1 Search universe and probes

This report does **not** make an `EMPTY-OF-RECORD` claim. It reports `PARTIAL`, because real fragments exist and the global member grammar is expressly open. The hunt nevertheless used a displayed, reproducible superset to avoid a phrase-only false negative.

```text
SEARCH ROOT:
  alpha_fundamental_record_action_cleanroom_v003/

RECURSION / FORMATS:
  recursive; *.md, *.json, *.txt, *.csv, *.tsv, *.yaml, *.yml

EXCLUSIONS:
  relay_inbox/**, relay_outbox/**, rd22_run_*/**, **/a32_custodian_private/**,
  expectation-ledger material, live tracker, questions-settled register,
  and this not-yet-written report (writer exclusion).

SEARCHED FILES:
  2,028
```

Fixed-string hit-file counts, used only to route close reading:

| Probe | Files | Probe | Files |
|---|---:|---|---:|
| `S_record` | 23 | `S_cell` | 2 |
| `S_rot` | 9 | `S_BF` | 9 |
| `Q_K` | 3 | `K_G^fin` | 11 |
| `tau_density` | 8 | `w(s)` | 19 |
| `v_c(t)` | 19 | `h_K(t)` | 15 |
| `D_K` | 110 | `integrand` | 20 |
| `Lagrangian` | 6 | `action functional` | 19 |

M-2/meaning modes applied:

1. exact object names and symbol aliases (`S_record`, `BOX_record`, `L_c`, `S_cell`, `S_rot`, `S_BF`, `Q_K`, `K_G^fin`);
2. condition/role forms (`integrand`, `density`, `measure`, `weight`, `energy`, `action functional`, `Lagrangian`, `generator`);
3. verb forms (`vary`, `variation`, `evaluate`, `pushforward`, `restrict`, `square`, `generate`);
4. case, punctuation, hyphenation, and line-wrap variants, followed by whole-display reading so an echo or requirement sentence could not be counted as a supplied object.

The raw hit census is not asserted as a sealed-corpus completeness theorem. The law-9 consequence is the conservative `PARTIAL` verdict: named surviving fragments are classified, and absence beyond them is not promoted to a no-outside claim.

### 2.2 `w(s)` provenance — located

The source chain is exact:

1. `R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_RESULT_V001.md`, SHA `e60aec3c44cfc5f1ef5715d3445e53783b0185ef93e54d94e442ff1df2ae9b59`, evaluates response means under an exhibited intrinsic measure family and excludes its nonuniform members; lines 59–78 close the primitive flat-cell measure selector and explicitly leave the generator's spectral density open.
2. `R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md`, SHA `e4cfaef14309b3acf5674f8c8faee756f744fec4691d5e01d9de0fa422592be2`, classifies the normalized uniform four-volume measure; lines 103–118 expressly say it does not derive the complete parent generator, coupling, or durability.
3. R3.4 pushes that uniform causal-diamond four-volume measure forward to

   ```text
   w(s)=32 min(s,1-s)^3,
   ```

   and then uses it to define `v_c(t)` inside `h_K(t)` and `D_K` (`R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md`, SHA `345d447e…`, lines 30–42; governing spec SHA `40890e75…`, lines 87–116 and 118–190).

Thus the source derivation **evaluates measure-dependent response means and a pushforward**, not an action functional. In the later parent it **decorates an operator as an intrinsic envelope**. It is neither the record integrand nor a variation map from that integrand. The round-1 binding says exactly this: `w(s)` is confirmed at the receiver and is not required as literal action content (`ROUND1_CROSSCHECK`, lines 166–193).

### 2.3 Meaning-probe classification of every live fragment family

| Candidate family | Sealed content | Meaning under H1 | Exit-A status |
|---|---|---|---|
| `S_record` in `S_0/S_1` | `S_0` and the Pauli completion are displayed, but their record sector is the opaque symbol `S_record[R,a,g]` (`COMPLETE_PARENT_ACTION_UNDERDETERMINATION_GATE_V001.md`, SHA `67816cfe…`, lines 26–64). | A placeholder at the right action location, with no integrand, domain, normalization, or variation. | **Fragment only.** |
| `S_cell(theta)=-hbar log cos^2(theta/2)` | Pointwise fidelity formula and conditional principal-log action; the gate retires it as a standalone microscopic action and retains it only as a possible diagonal probability observable (`ONE_CELL_FIDELITY_ACTION_SELECTOR_GATE_V001.md`, SHA `84ab5b01…`, lines 118–152). | Observable/log marker, not a complete record-sector action. | **Rejected as complete candidate by its own source.** |
| Relative action character / FS budget | `Delta S` relative marker and `pi*hbar/2` FS budget; the source expressly leaves the complete microscopic Lagrangian/action unestablished (`PRIMITIVE_RECORD_ACTION_CHARACTER_BRIDGE_GATE_V002.md`, SHA `fc3e44f0…`, lines 121–185 and 218–227). | Onset/relative-phase bridge, not an absolute functional. | **Fragment only.** |
| `S_rot`, `S_BF` | Two explicit boundary action countermodels (`STRATUM_TEST`, SHA `6a316f1f…`, lines 97–102). | Action-shaped, but not sealed as complete packet-parent record actions; no H1 receiver map or common charged source binding. | **Partial negative controls, not runnable H1 candidates.** |
| `w(s)`, `v_c(t)`, `h_K(t)`, `D_K` | Intrinsic measure pushforward, envelope, and operator outputs. | Measure/weight plus already-generated receiver. | **Wrong side of U1.** |
| `tau_density` lineage | The reference determination returns `SILENT`: no sealed use types the token on a carrier; the nearest live objects are an intensive-response convergence notion and invariant coefficient (`STAGE8_7A_TAU_DENSITY_REFERENCE_DARIO_V001.md`, SHA `6441b787…`, lines 13–39, 89–150, 249–276). | Convergence/typing slot, not an action density formula. | **No integrand.** |
| `K_G^fin`, `J_c`, `S_R` lineage | Conserved-current/density transport and the intrinsic cell measure (`STAGE8_B1C_DENSITY_CHAIN_CROSSCHECK_DARIO_V001.md`, SHA `1e6460c5…`, especially lines 22–75 and 269–278). | Current/measure carrier; no action variation producing H1's packet receiver. | **No integrand.** |
| `Q_K(a)=sum_C Vol_4(C)||F_C||^2` | Exact intrinsic-volume quadratic compatibility on the discrete connection/refinement sector (`STAGE8_B1A_LIFT_FORCING_CODEX2_V001.md`, SHA `3966fdb1…`, line 176; corroborated by `RA27_2`, SHA `660e0c14…`, lines 456–467). | A genuine per-cell energy quadratic, but on curvature/cochain fields; it has no record factors, one-use incidence terms, packet `D_rec/inc`, or durability map. | **Action-shaped fragment in another sector.** |

### 2.4 Verdict on Exit A

The sealed stock contains action-shaped and integrand-adjacent fragments, so `EMPTY-OF-RECORD` would be false. It does not contain a sealed candidate with all of the following receiving data:

```text
record-sector functional form;
admissible variation domain and boundary data;
primitive one-use incidence support;
map to the fixed packet envelope and first-order D_rec/inc receiver;
mandatory square-generated descendants without an independent coefficient;
completed-record durability output.
```

The result is therefore **PARTIAL**. `S_record` is the correctly located hole; `S_rot/S_BF`, `S_cell`, the relative action marker, `Q_K`, the measure/current/density objects, and the packet operator each supply a proper fragment, but no one object supplies the missing integrand-to-receiver bridge. C2–C6 do not yet become runnable tests on a supplied Exit-A candidate.

---

## 3. Law checks

### 3.1 Freedoms consumed

| Datum touched | Treatment | Scope statement |
|---|---|---|
| `S_record[R,a,g]` / `BOX_record` form | CARRIED-AS-PARAMETER | Remains opaque; no term inserted. |
| admissible action/P5 family and effective remainder | CARRIED-AS-PARAMETER | Open grammar and no-outside gap retained. |
| `E_D`, `E_4` membership | CARRIED-AS-PARAMETER | Audit sets only; neither is selected as the physical stratum. |
| `S_rot`, `S_BF` packet-parent admission | CARRIED-AS-PARAMETER | Explicitly untested; neither admitted nor excluded. |
| `w(s)` | CONDITIONED-ON | Carried exactly as the sealed intrinsic-measure pushforward and operator envelope; not retyped as action content. |
| scaling weight of `w(s)` | CARRIED-AS-PARAMETER | No independent scaling weight chosen; the sealed normalized receiver is cited, not varied. |
| `tau_density` carrier/subject | CARRIED-AS-PARAMETER | SILENT status retained. |
| `K_G^fin` / density carrier | CARRIED-AS-PARAMETER | Current/measure role retained; no action role assigned. |
| `Q_K` curvature energy | CARRIED-AS-PARAMETER | Separate-sector quadratic; no identification with `S_record`. |
| U1 domain, inverse, and boundary terms | CARRIED-AS-PARAMETER | Missing class/subclass scheme remains missing. |
| any coefficient, topology, normalization, action member, or physical identification | SUBSTITUTED | **NONE.** |

### 3.2 Flattening check

The complete 37-row decline register was checked. Load-bearing live rows for this relay:

| Row | Result |
|---|---|
| S03 | CLEAN — no member, stratum, minimal action, or construction-end selector chosen. |
| S08 | CLEAN — no discrete object identified with electromagnetism, Maxwell theory, or a smooth public field. |
| S12 | CLEAN — `CLAIMED`, `PARTIAL`, `NARROWED`, and status labels are not treated as proof objects. |
| S16 | CLEAN — no Hessian-first replacement of the action obligation. |
| S19 | CLEAN — no decay/durability inference from a bounded operator fragment. |
| S21 | CLEAN — no gravitational energy convention selected. |
| S24 | CLEAN — no clustering axiom used to rescue the route. |
| S25 | CLEAN — no reparameterization, equal-action, or minimality principle introduced. |
| S26 | CLEAN — no `C_ref` or smooth comparison target used as a source. |

No status flag was promoted into a discharging object. The other decline rows are not touched by a load-bearing identification in this artifact.

### 3.3 Battery and self-audit

```text
F_PLDEC          = PASS (no physical quantity evaluated)
ANTI_TUNING      = PASS (no target constant, desired coefficient, or fitted profile used)
M2               = PASS (fixed strings + aliases + meaning/verb forms + wrap/hyphen/case review)
LAW9             = PASS AT CLAIM SCOPE (typed A/B partition displayed; no global no-outside claim)
PIN_CHECK        = PASS (named inputs recomputed; cited sealed/bundle copies used)
FLATTENING       = CLEAN (37/37 checked; load-bearing rows displayed)
PE_POINTER_ONLY  = PASS (PE-1..PE-11 unopened and unconsulted)
```

Self-attack: the tempting move was to call `S_rot/S_BF` an Exit C because they are explicit actions. That fails twice in their own sealed record: packet-parent membership is untested, and no map connects their variation to H1's complete receiver. The second temptation was to identify `w(s)` with the integrand because it appears inside the parent operator. Its provenance instead classifies it as a measure pushforward/envelope. Both promotions were refused.

---

CIRCULARITY = CONFIRMED (partial subclass schemes displayed; none supplies the H1-compatible U1 map)
EXITS = dichotomy confirmed (a subclass solver is restricted Exit-B; clause-local tests are not exits)
TALLY = confirmed (1 decided / 3 narrowed / 7 unmoved / I6 unpressed; 16 remains a lower bound)
EXIT_A = PARTIAL (opaque S_record; explicit S_rot/S_BF negative controls; S_cell/relative-marker/Q_K fragments; measure, density, current, and packet-output objects lack the integrand-to-receiver bridge)
W_S_SOURCE = located (R3_3 evaluates intrinsic-measure response means/classifies the uniform measure; R3_4 pushes it forward and uses it as an operator envelope, not an action variation)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+4 scope controls: all headlines CLAIMED; no emptiness/no-outside theorem; partial evaluation distinguished from H1 completion; no fragment promoted to a selected action)
