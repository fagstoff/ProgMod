'''
Løsningsforslag til oppgave 2 på denne siden: 
https://github.com/fagstoff/ProgMod/blob/master/Fagstoff/euler.ipynb 
'''

# Importerer nødvendige biblioteker
import math
import matplotlib.pyplot as plt
import numpy as np

# Initialbetingelser
y0 = 0
dx = 0.1

# For hvilken x skal beregningene stoppe?
max_x = 3

# Eksakt løsning
def A(x):
    return (1/4)*(-2*x + math.exp(2*x) - 1)

# Eulers metode for denne spesifikke problemstillingen
def next_y(dx, xn, yn):
    return yn + dx * (xn + 2*yn)

# x-verdier for plotting av eksakt løsning
x = np.arange(0, max_x, 0.1)
y = []

# Regner ut eksakt løsning
for i in x:
    y.append(A(i))

# x-verdier for plotting av Euler
xe = np.arange(0, max_x, dx).tolist()

# Initialiserer med startverdien for ye
ye = [y0] 

# Bruker Eulers metode for å regne ut neste y-verdi
for xn in xe:
    ye.append(next_y(dx, xn, ye[-1]))

# Legger til den siste x-verdien
xe.append(xe[-1] + dx)

# Utskrift av data
plt.grid() # Lager rutenett
plt.xlabel('$t$') # Merker x-aksen
plt.ylabel('$A(t)$') # Merker y-aksen
plt.plot(x, y, label='$f(x)$')
plt.plot(xe, ye, label='Euler med $\Delta x={}$'.format(dx))
plt.legend()
plt.show()