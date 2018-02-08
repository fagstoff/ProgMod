'''
Løsningsforslag med bruk av odeint() til oppgave 2 på denne siden: 
https://github.com/fagstoff/ProgMod/blob/master/Fagstoff/euler.ipynb 
Lisens: Creative Commons BY-SA bitjungle (Rune Mathisen) 2018
'''
import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y, x):
    '''Definerer modellen y' = x+2y som en funksjon'''
    dydx = x + 2*y
    return dydx

# Initialbetingelser
y0 = 0

# Intervallet vi skal kjøre beregninger i
x0 = 0
xmax = 3
x = np.linspace(x0, xmax)

# Kjører beregninger
y = odeint(model, y0, x)

# Plotter resultatet
plt.grid(True)
plt.title("$\\frac{dy}{dx}=x + 2y$", fontsize=16)
plt.xlabel('x',fontsize=12)
plt.ylabel('y(x)',fontsize=12)
plt.plot(x,y)
plt.show()