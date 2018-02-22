""" Maks volum til en eske brettet fra et ark """
#
# Lisens: Creative Commons BY-SA bitjungle (Rune Mathisen) 2018
#
# Program bruker sidelengdene til et rektangel som input, og finner største mulige volum
# til en eske når det brettes opp kanter fra rektangelet. Et A4-ark brukes som standardverdi
# dersom brukeren ikke oppgir andre mål.

import matplotlib.pyplot as plt

def get_user_input(default_value):
    """Henter brukerinput og sjekker om det er gyldig data. Returnerer standardverdi ved feil eller ingen brukerdata."""
    val = input("Tast inn sidelengde i mm, eller trykk [ENTER] for å bruke {}: ".format(default_value))
    # Validerer input og returnerer et heltall
    try:
        v = int(val)
        if v > 0:
            return v 
        else:
            raise ValueError("Value must be larger than zero")
    except ValueError as e: # Trigges dersom input ikke er et tall, er 0 eller et negativt tall
        print(e)
        print("Bruker standardverdi {}".format(default_value))
        return default_value

def volume(x, y, z):
    """Returnerer volumet til en prisme med rektangulær grunnflate."""
    return x*y*z


if __name__ == '__main__':
    # Mål på A4-ark. Brukes som standardverdier dersom brukeren ikke taster inn egne verdier.
    LENGTH_A4 = 279 # mm
    WIDTH_A4 = 210  # mm 

    # Steglengde for beregning
    STEP = 1 # mm

    # Henter bruker-input for lengde og bredde på arket
    # Bruker lengde og bredde til et A4-ark som standardverdier
    length = get_user_input(LENGTH_A4)
    width = get_user_input(WIDTH_A4)
    
    # Beregner største mulige høyde på kantene
    # Finner minste sidelengde, og deler på 2 med en "floor division"
    height_max = min(width, length) // 2

    # Initialiserer lister som skal brukes til plotting av resultater
    x = []
    y = []

    # Regner steg for steg alle mulige volumer
    for h in range(1, height_max, STEP):
        l = length - 2*h 
        w = width - 2*h 
        V = volume(l, w, h) / 1000000 # volum i dm^3
        x.append(h)
        y.append(V)

    # Finner det største volumet og den tilhørende kanthøyden
    V_max = max(y)
    idx_max = y.index(V_max)
    h_max = x[idx_max]

    # Lagrer resultatet i en tekststreng
    result_txt = "Største volum er {} liter. Da er kanthøyden {} mm.".format(round(V_max, 2), h_max)

    # Utskrift av resultat
    plt.grid() # Lager rutenett
    plt.xlabel('Kanthøyde') # Merker x-aksen
    plt.ylabel('Volum') # Merker y-aksen
    plt.plot(x, y)
    plt.title(result_txt)
    plt.show()
    