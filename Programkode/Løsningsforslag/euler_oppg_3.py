'''
Løsningsforslag med bruk av eulers metode til oppgave 3 på denne siden: 
https://github.com/fagstoff/ProgMod/blob/master/Fagstoff/euler.ipynb
Se også videoforklaring av dette eksempelet: https://www.youtube.com/watch?v=NjPjO86NX7o
Lisens: Creative Commons BY-SA fuzzbin (Tom Jarle Christiansen) 2018
'''

# Import av nødvendige biblioteker
import matplotlib.pyplot as plt
import numpy as np

# Initialbetingelser
v0 = 0 # slippfart
dt = 0.01 # Tidsskritt
max_t = 10 # Hvor mange sekunder programmet skal beregne

k = 1 # Luftmotstandskoeffisient i L = k*v^2
m = 60 # Massen til objektet
g = 9.81 # Tngdens akselerasjon

# Eulers metode beregner neste verdi
def neste_v(dt, vn):
    return vn + dt * ( g - (k/m) * vn**2 )

# Initierer lister der verdiene t og v lagres
t = np.arange(0, max_t, dt).tolist() # Fyller listen med t-verdier
v = [v0]

# Generer y-verdier utifra listen med tidspunkt
for i in t:
    v.append(neste_v(dt, v[-1]))

t.append(t[-1] + dt) # Legger til siste t-verdi for å få like lange lister

# Utskrift til skjerm
plt.grid()
plt.title("Fall med luftmotstand")
plt.xlabel('Tid [s]', fontsize=12)
plt.ylabel('Fart [m/s]', fontsize=12)
plt.plot(t,v, label='Euler, $\\Delta t = {}$ s'.format(dt))
plt.legend()
plt.show()