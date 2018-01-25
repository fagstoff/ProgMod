# Importerer nødvendige biblioteker
import matplotlib.pyplot as plt
import numpy as np

#Initialbetingelser
y0 = 0
delta_x = 0.01
xn = 0 # initierer

# Eksakt løsning
def A(x):
    return (1/4)*(-2*x + np.exp(2*x) - 1)

# Eulers metode for denne spesifikke problemstillingen
def next_y(x, delta_x, yn):
    return yn + delta_x * (x + 2*yn)

# x-verdier for plotting av eksakt løsning
x = np.arange(0, 1, 0.01)
y = []

# Regner ut eksakt løsning
for i in x:
    y.append(A(i))

# x-verdier for plotting av Euler
xe = np.arange(0, 1, delta_x).tolist()
ye = [y0] # Initialiserer med startverdien for y

# Bruker Eulers metode for å regne ut neste y-verdi
for verdi in xe:
    ye.append(next_y(xn, delta_x, ye[-1]))
    xn += delta_x # oppdaterer

# Legger til den siste x-verdien
xe.append(xe[-1] + delta_x)

# Utskrift av data
plt.grid() # Lager rutenett
plt.xlabel('$t$') # Merker x-aksen
plt.ylabel('$A(t)$') # Merker y-aksen
plt.plot(x, y, label='$f(x)= \\frac{1}{4} ( -2x + e^{2x} - 1)$')
plt.plot(xe, ye, label='Euler med $\Delta x={}$'.format(delta_x))
plt.legend()
plt.show()