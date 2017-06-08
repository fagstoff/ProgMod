"""
Creative Commons - BY SA - Tom Jarle Christiansen - 2017
Ligger tre punkter på linje?
"""

import numpy as np

# Leser inn tre punkter og konverterer til liste.
p1 = list(map(int, input("Tast inn punkt 1 pa formen x y:").split()))
p2 = list(map(int, input("Tast inn punkt 2 pa formen x y:").split()))
p3 = list(map(int, input("Tast inn punkt 3 pa formen x y:").split()))

def ligger_pa_linje(punkt1, punkt2, punkt3):
    print(punkt1, punkt2, punkt3)
    # Lager to vektorer av p1, p2 og p3
    v1 = np.array(punkt3) - np.array(punkt1)
    v2 = np.array(punkt2) - np.array(punkt1)
    # Sjekker om kryssporduktet er null
    if np.cross(v1, v2) == 0:
        return True
    else:
        return False

if ligger_pa_linje(p1, p2, p3):
    print("Punktene ligger pa linje")
else:
    print("Punktene ligge ikke pa linje")