"""
Førsteutkast - Ikke ferdig!
Vertikalt fall med luftmotstand
Creative Commons - BY SA - Tom Jarle Christiansen 2017
"""

import math
import matplotlib.pyplot as plt

# Konstanter
g = 9.81
m = 100
k = 20
v_0 = 0
d_t = 0.01

t = [0]
v = [v_0]

def dv_tp1(v):
    return g - k * v / m #modell

for x in range(0,3000):
    t.append(t[-1] + d_t)
    v.append(v[-1] + dv_tp1(v[-1]) * d_t)

print(v)

plt.plot(t,v)
plt.xlabel('Tid [s]')
plt.ylabel('Fart [m/s]')
plt.grid()
plt.show()