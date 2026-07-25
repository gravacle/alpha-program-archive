from decimal import Decimal as D, getcontext
getcontext().prec = 60
def dexp(x, terms=80):
    s = D(1); t = D(1)
    for k in range(1, terms):
        t *= x / k; s += t
    return s
def dsqrt(x):
    g = D(x).sqrt()
    return g
R = D(1)/500
Lfree = (D(2)/3)*(1 + (2*R/3)*dexp(R/3))
delta = Lfree*R
eps = 3*(dexp(2*delta)-1)
eta = eps + D(1)/D(10)**10
X = D(1)/20
r = D(203)/250
sep = 1 - eta - eta*X - (r + eta)
gmap = eta/sep
lam_min = 1 - eta*(1+X)
Bmax = r + eta + eta*X
pdel = (2*X + 2*X*X)/(1 - X*X)
kS = (1+X)/(1-X)
tn = D('2.23606797749978978585902340396880473135254598337605091788')
sn = D('1.00000000000000032013099253051654101514362296494512686329')
ov_lo = D('1.00000000000000064026198506103318451413962450352763034760')
ov_err = D('6.40261985061033184514139624503527630347602856696555E-13')
prod = tn*sn
coeff_min = ov_lo - prod*pdel
q = Bmax/lam_min
pref = prod*kS/coeff_min
dom7 = pref*q**7
print("eps       =", +eps)
print("eta       =", +eta)
print("sep       =", +sep)
print("gmap      =", +gmap, "< 0.05:", gmap < D('0.05'))
print("lam_min   =", +lam_min)
print("Bmax      =", +Bmax)
print("coeff_min =", +coeff_min)
print("q         =", +q, "< 1:", q < 1)
print("pref      =", +pref)
print("dom7      =", +dom7, "< 1:", dom7 < 1)
for N in range(1, 7):
    b = ov_err + prod*N*eta*(1+eta)**(N-1)
    print(f"finite N={N}:", +b, "< 1:", b < 1)
n1 = D('1.163602006331267995306879734075857067758497991279003005E-13')
ninf = D('2.196458657382034741094490467017288991251092785135788898E-13')
print("sqrt(n1*ninf) =", +dsqrt(n1*ninf))
res = D('1.556582229217841E-14')
print()
print("leakage crossover (contraction reading, leak ~ sqrt(5)*N*res):")
for N in [10,100,1000,2000,2400,2600,3000,4000]:
    zlow = coeff_min*(lam_min**N)*(1-dom7) if N>=7 else None
    leak = dsqrt(D(5))*N*res
    print(f"  N={N}: |Z_N^red| certified lower ~ {float(zlow):.3e}  leak ~ {float(leak):.3e}  survives={zlow>leak}")
