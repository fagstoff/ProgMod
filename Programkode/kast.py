""" Skrått kast """
#
# Lisens: Creative Commons BY-SA fuzzbin (Tom Jarle Christiansen) og bitjungle (Rune Mathisen) 2017
#
# Program simulerer posisjonen til et objekt som kastes skrått
# Vi ser bort fra alle andre krefter enn gravitasjonen i dette eksempelet.

# Henter inn biblioteker som skal brukes
import numpy as np
import matplotlib.pyplot as plt

# Definerer initialbetingelser
VX0 = 20
VY0 = 25
GRAV = 9.81
TID = np.linspace(0.0, 5.0, num=50) # 50 tidsmerker mellom 0.0 og 5.0

# Definerer modeller for x- og y-posisjon
def y_pos(tid):
    """ Beregner y-posisjonen til objektet """
    return VY0*tid - 0.5*GRAV*tid**2

def x_pos(tid):
    """ Beregner x-posisjonen til objektet """
    return VX0*tid

# Utskrift
plt.grid(True)
plt.title("Posisjon som funksjon av tid", fontsize=16)
plt.xlabel('Lengde [meter]', fontsize=12)
plt.ylabel('Høyde [meter]', fontsize=12)
plt.plot(x_pos(TID), y_pos(TID), 'r', label='Ballens posisjon')
plt.legend(loc='best')
plt.show()
