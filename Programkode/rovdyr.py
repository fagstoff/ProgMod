import numpy as np
# import scipy as sp
from scipy.integrate import odeint
import matplotlib.pyplot as plt

 # Definition of parameters
a = 1. #alfa
b = 0.1 #beta
c = 1.5 #delta
d = 0.75 #gamma

def dX_dt(X, t):
    """ Return the growth rate of fox and rabbit populations. X[0]=x og X[1]=y"""
    return ([ a*X[0] -   b*X[0]*X[1] ,
                  -c*X[1] + d*b*X[0]*X[1] ])

t = np.linspace(0,2,2) # x-verdier (Tidsaksen)
X0 = [10, 5]  # initialbetingelse v0 = 0 m/s
X = odeint(dX_dt, X0, t, full_output=True) # Løser difflikningen
X = np.array(X).flatten() # Formaterer tallene i en array

print(X)

#
#plt.grid(True)
#plt.title("Fart som funksjon av tid", fontsize=16)
#plt.xlabel('Tid [s]',fontsize=12)
#plt.ylabel('Fart [m/s]',fontsize=12)
#plt.plot(t,X)
#plt.show()