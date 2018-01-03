''' Plotting av to perioder til sinusfunksjonen. '''

# Programmet plotter de to første periodene av en sinusfunksjon
# med amplitude a, og frekvens f
#
# y(x) = a * sin(f * x);
#
# Lisens: Creative Commons BY-NC-SA fuzzbin (Tom Jarle Christiansen) 2017

# Importerer biblioteker
import math
import numpy as np
import matplotlib.pyplot as plt

a = int(input('Tast inn amplituden:'))
f = int(input('Tast inn frekvensen:'))

# Lager en liste med x-verdier avgrenset til to perioder.
# Sinusfunksjonen bruker radianer. To perioder er 4*Pi radianer
x_akse = np.linspace(0, (4 * math.pi) / f, num=100)

# Lager x-verdier som vi skal beregne sinusfunksjonen utifra
x_frekv = [] # Tom liste som skal fylles med verdier

# Alle x-verider i definisjonsområdet ganges med frekvensen.
for verdi in x_akse:
    x_frekv.append(verdi * f)

# Bergener y-verdier med np.sin()
y_verdier = np.sin(x_frekv)

# Ganger alle y-verdier med amplituden
y_amp = [] # Tom liste som skal fylles med y-verdier * amplitude
for verdi in y_verdier:
    y_amp.append(verdi * a)

# Skriver ut y-verdiene som funksjon av de opprinnelige x-verdiene.
plt.title('En sinuskurve')
plt.ylabel('amplitude')
plt.xlabel('radianer')
plt.grid(True)
plt.plot(x_akse, y_amp)
plt.show()
