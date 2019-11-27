import numpy as np
import matplotlib.pyplot as plt

def v(t):
    return (1000/3600)*(20 + 30*np.log((1/2)+(t/4)) - (t/4) + 2*np.sin(t/(4*np.pi)))

def midtsum(f, a, b, dx):
    msum = 0
    for x in np.arange(a, b, dx):
        msum += f(x + dx/2) * dx
    return msum

t = np.arange(0, 360, 0.1)
fart = v(t)

gj_fart = np.average(fart)
print("Estimat med gjennomsnittsfart:", gj_fart * 360)

strekning = midtsum(v, 0, 360, 1E-3)
print("Estimat med Riemansum:", strekning)
plt.plot(t, fart)
plt.grid()
plt.xlabel("Tid (s)")
plt.ylabel("Fart (m/s)")
plt.title("Bilen har kjørt {:.1f} meter".format(strekning))
plt.show()