""" Gjett tallet """
# Lisens: Creative Commons BY-SA bitjungle (Rune Mathisen) 2017
#
# Dette er et spill hvor du skal gjette på et tall mellom 1 og 20.
# Spillet er basert på "GUESS THE NUMBER" i boka "Invent Your Own Computer Games With Python"
# av Al Sweigart: http://inventwithpython.com/chapter4.html
#
# Forslag til endringer og forbedringer som du kan gjøre:
#
# * Endre antall forsøk spilleren får til å gjette tallet.
# * Endre tall-området som spilleren skal gjette i.
# * La spilleren selv taste inn antall gjettinger som er lov å gjøre.
# * Lage en egen funksjon som tester om spilleren har gjettet riktig.
# * Lage kode som håndterer feil dersom spilleren ikke taster inn et tall.
# * Bytte ut for-loop med en while-loop.
#
# Kan du selv komme på andre ting som kan gjøre spillet bedre?

import random # Her importerer vi en modul med funksjoner som vi skal bruke i programmet vårt.

def main():
    """ Hovedprogrammet main starter her """

    antall_forsok = 0 # Dette er en variabel hvor vi skal lagre det spilleren gjetter.

    print("Hei, hva heter du?")
    spillernavn = input() # Vi henter spillerens navn, og lagrer det i en variabel.

    tall = random.randint(1, 20) # Nå plukker vi et tilfeldig tall mellom 1 og 20.
    print("Ok {}, jeg tenker på et tall mellom 1 og 20.".format(spillernavn))

    for antall_forsok in range(6): # Vi gir spilleren 6 forsøk på å gjette riktig.
        print("Gjett hvilket tall det er:")
        gjettet = input() # Venter på at spilleren skal taste inn et tall.
        gjettet = int(gjettet) # Gjør om til heltall (hva skjer om spilleren taster inn noe annet?).

        if gjettet < tall: # Gjettet spilleren lavere enn tallet vårt?
            print("Du gjettet {}, men det er for lavt {}.".format(gjettet, spillernavn))
        elif gjettet > tall: # Gjettet spilleren høyere enn tallet vårt?
            print("Du gjettet {}, men det er for høyt {}.".format(gjettet, spillernavn))
        else: # Ikke for lavt og ikke for høyt, da må det være riktig!
            break # Hopper ut av loopen.

    # Her er for-loopen ferdig, legg merke til innrykket på linjene nedenfor.

    if gjettet == tall: # Sammenlikner det spilleren gjettet med det vi tenkte på. Er tallene like?
        print("Wow {}, du gjettet riktig på {} forsøk.".format(spillernavn, antall_forsok))
    else: # Dersom tallen ikke var like, så må de være ulike.
        print("Dette var litt for vanskelig. Jeg tenkte på tallet {}.".format(tall))



if __name__ == '__main__':
    # Programmet starter her. Vi kaller på funksjonen main().
    main()
    # Når vi er ferdige, skriver vi ut en liten avskjedshilsen på skjermen.
    print("=== Game Over ===")
