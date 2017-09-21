
''' Utregning av nullpunkter i et andregradspolynom. '''

# Programmet regner ut nullpunmkter i et andregradspolynom.
# Tast inn polynomfaktorene A, B og C.
# Lisens: Creative Commons BY-NC-SA fuzzbin (Tom Jarle Christiansen) 2017

import math # Henter inn matematikkbiblioteket

print('Tast inn a, b og c')
rotverdi = -1 # Setter en startverdi for å få whileløkka til å kjøre første gang.

while rotverdi < 0: # Løkke som leser inn verdier så lenge ROTVERDI er mindre enn null
    a = int(input('Tast inn a: '))
    b = int(input('Tast inn b: '))
    c = int(input('Tast inn c: '))
    rotverdi = math.pow(b, 2) - (4*a*c)
    if rotverdi < 0:
        print('Ingen losning. Prov igjen') # Feilmelding

# Regner ut ABC-formel
x1 = -b + math.sqrt(rotverdi) / (2 * a)
x2 = -b - math.sqrt(rotverdi) / (2 * a)

print('Nullpunktene til funksjonen er: X1={} og X2={}'.format(x1, x2))
print('Ha en fin dag!')
