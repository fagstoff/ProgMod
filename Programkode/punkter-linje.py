
# Ligger tre punkter på linje
#
# Lisens: Creative Commons BY-SA fuzzbin (Tom Jarle Christiansen) 2017
#
# Program som leser inn tre punkter på formatet <x y> og avgjør om
# disse ligger på en rett linje. Passer godt til matematikk R1

# Importerer biblioteker som skal brukes
import numpy as np
import matplotlib.pyplot as plt

# Leser inn tre punkter og konverterer til liste.
P1 = list(map(int, input("Tast inn punkt 1 pa formen <x y>:").split()))
P2 = list(map(int, input("Tast inn punkt 2 pa formen <x y>:").split()))
P3 = list(map(int, input("Tast inn punkt 3 pa formen <x y>:").split()))

def ligger_pa_linje(punkt1, punkt2, punkt3):
    # Avgjør om punktene ligger på en rett linje. Returnerer True/False
    # Lager to vektorer av punktene P1, P2 og P3
    v_1 = np.array(punkt3) - np.array(punkt1)
    v_2 = np.array(punkt2) - np.array(punkt1)
    print(v_1, v_2)
    # Sjekker om kryssporduktet er null
    if np.cross(v_1, v_2) == 0:
        return True
    else:
        return False

# Mainfunksjonen
def main():
    # Hovedfunksjonen - Skriver ut svar og plotter punktene
    if ligger_pa_linje(P1, P2, P3):
        print("Punktene {}, {} og {} ligger pa en rett linje".format(P1, P2, P3))
    else:
        print("Punktene {}, {} og {} ligger ikke pa en rett linje".format(P1, P2, P3))
        # Skriver ut punktene i et koordinatsystem
        plt.plot([P1[0], P2[0], P3[0]], [P1[1], P2[1], P3[1]], 'bo')
        plt.ylabel('Y')
        plt.xlabel('X')
        plt.show()

if __name__ == '__main__':
    # Programmet starter her. Vi kaller på funksjonen main().
    main()
    # Når vi er ferdige, skriver vi ut en liten avskjedshilsen på skjermen.
    print("=== Have a nice day! ===")
