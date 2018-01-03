'''
Enkel hangman

Tom Jarle Christiansen - CC BY SA - 2017
'''
# Tre lister
hemmelig = list(input('Tast inn hemmelig ord:'))
fasit = hemmelig.copy()
ord = [None] * len(hemmelig)

liv = 5 # Antal liv


# Hovedløkke
while True:
    gjettet = input('Tast inn bokstav:')
    if gjettet in hemmelig: # Sjekker om gjettet bokstav finnes i det hemmelige ordet.
        ord[hemmelig.index(gjettet)] = gjettet # Legger gjettet bokstav inn i ordet som bygges opp.
        hemmelig[hemmelig.index(gjettet)] = None # Fjerner gjettet bokstav fra det hemmelige ordet.
        print(ord, hemmelig) # Kontrollutskrift
        if ord == fasit: # Sjekker om ordet er riktig
            print('Du vant! Du har {} liv igjen.'.format(liv))
            break
    else:
        liv -= 1 # Trekk fra et liv når du har gjettet feil.
        print('Uh oh!, du har {} liv igjen'.format(liv))
        if liv == 0:
            print('Du tapte')
            break
