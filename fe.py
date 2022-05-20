import numpy as np
import matplotlib.pyplot as plt
from scipy.odr import *


at     = np.array([0.276, 0.251, 0.231, 0.213])
at_err = np.array([0.005, 0.004, 0.004, 0.004])

ae     = np.array([0.2801, 0.2547, 0.2342, 0.2150])
ae_err = np.array([0.0007, 0.0022, 0.0018, 0.0004])

def f(B, x):
    
    return B[0]*x + B[1]

linear = Model(f)

mydata = RealData(at, ae, sx=at_err, sy=ae_err)    

myodr = ODR(mydata, linear, beta0=[1., 2.])

myoutput = myodr.run()

myoutput.pprint()

at_fit = np.linspace(at[0], at[-1], 1000)
ae_fit = f(myoutput.beta, at_fit)

plt.errorbar(at, ae, xerr=at_err, yerr=ae_err, linestyle='None')
plt.plot(at_fit, ae_fit)

plt.show()
