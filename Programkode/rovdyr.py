import numpy as np
# import scipy as sp
from scipy.integrate import odeint
import matplotlib.pyplot as plt

 # Definition of parameters
a = 1. #alfa
b = 0.1 #beta
c = 1.5 #delta
d = 0.75 #gamma

w0 = [5, 15] # initialbetingelser

# Definerer differensiallikningen
def dX_dt(X, t, a, b, c, d):
    """ Returnerer antall rev og kanin. X[0]=x og X[1]=y"""
    return ([ a*X[0] -   b*X[0]*X[1], -c*X[1] + d*b*X[0]*X[1] ])


# Løser differensiallikningen
t = np.linspace(0,15,200) # x-verdier (Tidsaksen)
w0 = [5, 15] # initialbetingelser 5 kaniner og 15 rev
X = odeint(dX_dt, w0, t, args=(a, b, c, d)) # Løser difflikningen

# Utskrift
plt.grid(True)
plt.title("Populasjoner som funksjon av tid", fontsize=16)
plt.xlabel('Tid',fontsize=12)
plt.ylabel('Populasjon [antall individer]',fontsize=12)
plt.plot(t, X[:, 0], 'b', label='Rev')
plt.plot(t, X[:, 1], 'g', label='Kanin')
plt.legend(loc='best')
plt.show()