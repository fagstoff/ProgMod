'''
Løsningsforslag til oppgave 3 på denne siden: 
https://github.com/fagstoff/ProgMod/blob/master/Fagstoff/euler.ipynb 
Lisens: Creative Commons BY-SA fuzzbin (Tom Jarle Christiansen) 2018
'''

# Importerer biblioteker
import matplotlib.pyplot as plt 
import numpy as np 

# Initialbetingelser
v0 = 0 # Startfart
dt = 0.1 # Tidsskritt
max_t = 20 # Hvor langt skal vi beregne

k = 0.47 # Luftmotstandskoeffisient
m = 60 # Massen til klossen
g = 9.81 # Tyngdens akselerasjon

# Euler
def neste_v(t, vn):
    return vn + t * ( g - (k/m) * vn**2 )

# Lister
x = np.arange(0, max_t, dt).tolist()
y = [v0]

# Beregner resten av y-verdiene ved hjelp av Euler
for i in x:
    y.append(neste_v(dt, y[-1]))

x.append(x[-1] + dt) # Legger til siste verdi i y-lista.

plt.plot(x, y)
plt.xlabel('$t [s]$') # Merker x-aksen
plt.ylabel('$v(t) [m/s]$') # Merker y-aksen
plt.grid()
plt.show()