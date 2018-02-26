""" Animasjon av vertikalt og skrått kast """
# Lisens: Creative Commons BY-SA fuzzbin (Tom Jarle Christiansen) og bitjungle (Rune Mathisen) 
#
# Animasjon av et vertikalt eller skrått kast. 
# Viser en ball som beveger seg friksjonsfritt.
# Sett v0x til 0 for et vertikalt kast.
# Ett piksel telles som 0,5 meter i denne animasjonen. 
import sys
import pygame
import numpy as np

# Modellen vår, fart som funksjon av tid
def fart(v0, a, tid):
    return v0 + a * tid

def ball_til_startpunkt():
    ballrect.top = fieldrect.height - ballrect.height
    ballrect.left = 10


# Definerer initialbetingelsene til modellen
v0x = 15  # Fart i x-retning (m/s). Sett til 0 for vertikalt kast.
v0y = 25  # Fart u y-retning (m/s).
a = -9.81 # Akselerasjon nedover (m/s^2)

teller = 0 # Holder styr på hvor langt i simuleringen vi har kommet.

tx = np.arange(0, 6, 0.05) # Liste med x-verdier - tiden
vy = [] # tom liste som skal inneholde fart som funksjon av tid

# Genererer v-verdier verdier for alle tidspunkt t
for x in tx:
    vy.append(-fart(v0y, a, x))

# Starter pygame
pygame.init()

field = pygame.image.load('anim_fotball_bane.png')
ball = pygame.image.load('anim_fotball.png')

fieldrect = field.get_rect()
ballrect = ball.get_rect()

# Setter vindusstørrelsen til det samme som størrelsen på bildet av banen.
screen = pygame.display.set_mode(fieldrect.size)

# Plasserer ballen der vi vil at den skal starte.
ball_til_startpunkt()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    try: # Flytter ballen og øker telleren.
        # Deler på 2 fordi ett piksel tilsvarer en halv meter.
        ballrect = ballrect.move([v0x // 2, vy[teller] // 2])
        teller += 1
    except IndexError: # Vi har kommet til enden av lista.
        teller = 0 # Nullstiller telleren.
        ball_til_startpunkt() # Flytter ballen tilbake til startpunkt.

    if ballrect.bottom > fieldrect.height: # Sjekker om ballen treffer nedkanten av banen.
        teller = 0 # Nullstiller telleren.
        ball_til_startpunkt() # Flytter ballen tilbake til startpunkt.

    # Skriver ut bakgrunnsbilde og ballen i sin nye posisjon.
    screen.blit(field, fieldrect)
    screen.blit(ball, ballrect)
    pygame.display.flip()