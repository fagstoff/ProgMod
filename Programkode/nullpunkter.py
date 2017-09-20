
'''
Utregning av nullpunkter i et andregradspolynom.
Lisens: Creative Commons BY-NC-SA fuzzbin (Tom Jarle Christiansen) 2017
'''



import math # Henter inn matematikkbiblioteket

print('Tast inn A, B og C')
ROTVERDI = -1 # Setter en startverdi for å få whileløkka til å kjøre første gang.

while ROTVERDI < 0: # Løkke som leser inn verdier så lenge ROTVERDI er mindre enn null
    A = int(input('Tast inn A: '))
    B = int(input('Tast inn B: '))
    C = int(input('Tast inn C: '))
    ROTVERDI = math.pow(B, 2) - (4*A*C)
    if ROTVERDI < 0:
        print('Ingen losning. Prov igjen') # Feilmelding

# Regner ut ABC-formel
X1 = -B + math.sqrt(ROTVERDI) / (2 * A)
X2 = -B - math.sqrt(ROTVERDI) / (2 * A)

print('Nullpunktene til funksjonen er: X1={} og X2={}'.format(X1, X2))
print('Ha en fin dag!')
