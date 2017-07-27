""" Skrått kast """
#
# Lisens: Creative Commons BY-SA fuzzbin (Tom Jarle Christiansen) og bitjungle (Rune Mathisen) 2017
#
# Program simulerer posisjonen til et objekt som kastes skrått

import numpy as np
# import scipy as sp
import matplotlib.pyplot as plt

# Definerer initialbetingelser
v_0x = 20
v_0y = 25
g = 9.81
tid = np.linspace(0.0, 5.0, num=50) # 50 tidsmerker mellom 0.0 og 5.0

# Definerer modeller for x- og y-posisjon
def y_pos(t):
    return v_0y*t - 0.5*g*t**2

def x_pos(t):
    return v_0x*t



# Utskrift
plt.grid(True)
plt.title("Posisjon som funksjon av tid", fontsize=16)
plt.xlabel('Lengde [meter]', fontsize=12)
plt.ylabel('Høyde [meter]', fontsize=12)
plt.plot(x_pos(tid), y_pos(tid), 'r', label='Ballens posisjon')
plt.legend(loc='best')
plt.show()
