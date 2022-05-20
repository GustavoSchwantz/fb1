from uncertainties.umath import *
from uncertainties import ufloat


def acc_exp(delta_x, delta_t):
	return (2*delta_x)/(delta_t**2)


# Configuração 1
print( acc_exp(ufloat(0.8, 0.0005), ufloat(2.38994, 0.002850719207)) )

# Configuração 2
print( acc_exp(ufloat(0.8, 0.0005), ufloat(2.50644, 0.0108006759)) )

# Configuração 3
print( acc_exp(ufloat(0.8, 0.0005), ufloat(2.61366, 0.009977655035)) )

# Configuração 4
print( acc_exp(ufloat(0.8, 0.0005), ufloat(2.72808, 0.002526341228)) )

