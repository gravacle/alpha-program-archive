# Common BR Local Induced-Coefficient Functions v001

Overall: `PASS_COMMON_BR_LOCAL_COEFFICIENT_FUNCTIONS_DEPTH_OPEN`

The coefficients are generated from the exact `Lambda^even(C5)` chiral-16 inventory carried by the same normalized BR operator. The executable grouping is:

`C2=0:dim=1:TrQ2=0:TrH2=0:TrQH=0, C2=2.4:dim=5:TrQ2=1.33333:TrH2=2:TrQH=1.33333, C2=3.6:dim=10:TrQ2=4:TrH2=6:TrQH=4`.

For `x=r^2/k_R^2` and `I_n(c)=integral_1^infinity tau^(-n) exp(-c tau) d tau`, the local terms of the one-carrier induced action are

```text
Gamma_ind,local = integral sqrt(g) [
    k_R^4 C_V(x)
  - k_R^2 C_R(x) R
  + (1/4) K_Q(x) F_Q^2
  + higher-curvature and finite-threshold terms ],

C_V = sum_a d_a I_3(x+C2_a)/(16 pi^2),
C_R = sum_a d_a I_2(x+C2_a)/(192 pi^2),
K_Q = sum_a Tr_a(Q^2) I_1(x+C2_a)/(24 pi^2).
K_H = sum_a Tr_a(H^2) I_1(x+C2_a)/(24 pi^2),
K_QH = sum_a Tr_a(Q H) I_1(x+C2_a)/(24 pi^2).
```

The `-C_R R` sign follows the Dirac-square endomorphism `E=-R/4+...` and the standard `a_2=(4 pi)^(-2) tr(E+R/6)` coefficient. The gauge normalization includes the one-half Weyl log-determinant factor; equivalently, the proper-time interval is a logarithm of squared scales. The electromagnetic coefficient agrees identically with the parent `SU(5)` projection `K_Q=(8/3)K_5`. The primitive parent-closing sphere cocharacter is kept separate: the actual carrier traces give `K_H=(3/2)K_Q` and `K_QH=K_Q`. None of these relations is entered from alpha.

The same explicit Dirac trace fixes the local gravitational `a_4` layer. Per internal Weyl state, including the one-half positive-square determinant normalization, it is `(5 R^2 - 8 Ric^2 - 7 Riem^2) I_1/(23040 pi^2)`, or `(-18 C^2 + 11 E_4) I_1/(23040 pi^2)` on the closed branch. The Euler integral is topological at fixed topology; the Weyl-squared term supplies the non-topological fourth-derivative local coefficient. This local derivative expansion does not replace the exact nonlocal metric form factor required for the external ultraviolet determinant.

The threshold map remains explicit: the three squared spectral thresholds are `x`, `x+12/5`, and `x+18/5`, with multiplicities `1`, `5`, and `10`. The rows verify the exact derivative recurrences and positivity before any saddle is attempted.

This closes the common local coefficient functions, not their numerical evaluation at a selected vacuum. The exact proper-time action contains higher-curvature terms and global compact contributions; the later saddle must evaluate the full spectrum and may not retain only the displayed Einstein-Maxwell terms if doing so changes the result. No alpha, endpoint, mass, or fitted residual enters this gate.

Heat-kernel normalization cross-check: D. V. Vassilevich, arXiv:hep-th/0306138, Eqs. (3.27) and (4.26)-(4.28).