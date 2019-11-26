'''
Løsningsforslag til "Derivasjon" oppgave 6
Copyright (C) 2019 bitjungle. Subject to Apache License 2.0.
http://www.apache.org/licenses/LICENSE-2.0.txt
'''
import numpy as np
import matplotlib.pyplot as plt

def u(x):
    return np.sin(1/x**2)

def v(x):
    return np.sqrt(np.log(x))

def uv(x):
    return np.sin(1/x**2) * np.sqrt(np.log(x))

def derivert(f, x, h):
    return (f(x+h) - f(x)) / h

x = np.arange(1.1, 5.1, 0.1)
y_u = u(x)
y_v = v(x)
y_uv = uv(x)

# Implementer (u(x)*v(x))' her
y_derivert_venstreside = derivert(uv, x, 1E-6)

# Implementer u'(x)*v(x) + u(x)*v'(x) her
y_derivert_hoyreside = derivert(u, x, 1E-6)*v(x) + u(x)*derivert(v, x, 1E-6)

plt.subplot(2, 1, 1)
plt.plot(x, y_u, label="$u(x)$", color="magenta")
plt.plot(x, y_v, label="$v(x)$", color="red")
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(x, y_derivert_venstreside, label="$(u(x) \cdot v(x))'$")
plt.plot(x, y_derivert_hoyreside, label="$u'(x) \cdot v(x) + u(x) \cdot v'(x)$")
plt.legend()
plt.show()