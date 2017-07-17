""" Rovdyr - Lotka/Volterra - Rovdyr/Byttedyr-modell """
#
# Lisens: Creative Commons BY-SA fuzzbin (Tom Jarle Christiansen) og bitjungle (Rune Mathisen) 2017
#
# Program simulerer hvordan populasjonen av rovdyr/byttedyr påvirkes over tid

import numpy as np
# import scipy as sp
from scipy.integrate import odeint
import matplotlib.pyplot as plt

 # Definition of parameters
A = 1. #alfa
B = 0.1 #beta
C = 1.5 #delta
D = 0.75 #gamma

# Definerer differensiallikningen
def d_pop(X, t_0, a_0, b_0, c_0, d_0):
    """ Returnerer antall rev og kanin. X[0]=x og X[1]=y"""
    return ([a_0*X_0[0] -   b_0*X[0]*X[1], -c_0*X[1] + d_0*b_0*X[0]*X[1]])


# Løser differensiallikningen
T = np.linspace(0, 15, 200) # x-verdier (Tidsaksen)
P0 = [5, 15] # initialbetingelser 5 kaniner og 15 rev
P = odeint(d_pop, P0, T, args=(A, B, C, D)) # Løser difflikningen

# Utskrift
plt.grid(True)
plt.title("Populasjoner som funksjon av tid", fontsize=16)
plt.xlabel('Tid', fontsize=12)
plt.ylabel('Populasjon [antall individer]', fontsize=12)
plt.plot(T, P[:, 0], 'r', label='Rev')
plt.plot(T, P[:, 1], 'b', label='Kanin')
plt.legend(loc='best')
plt.show()
