from uncertainties.umath import *
from uncertainties import ufloat


def acc_teo(M, m, g = 9.81):
	return (m*g)/(M + m) 	

# Configuração 1
print( acc_teo(ufloat(0.1992, 1e-4), ufloat(0.00577, 1e-4)) )

# Configuração 2
print( acc_teo(ufloat(0.21938, 1e-4), ufloat(0.00577, 1e-4)) ) 

# Configuração 3
print( acc_teo(ufloat(0.2395, 1e-4), ufloat(0.00577, 1e-4)) )

# Configuração 4
print( acc_teo(ufloat(0.25965, 1e-4), ufloat(0.00577, 1e-4)) )