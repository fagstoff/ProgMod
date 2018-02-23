""" Animasjon av skrått kast """
# Lisens: Creative Commons BY-SA fuzzbin (Tom Jarle Christiansen) og bitjungle (Rune Mathisen) 
#
# Animasjon av et skrått kast. Viser en ball som beveger seg friksjonsfritt
# med en fart på 10 m/s i x-retning og en startfart på 20 m/s i y-retning. 
# Ett piksel telles som 0,5 meter i denne animasjonen. 
import sys
import pygame
import numpy as np

# Modellen vår, fart som funksjon av tid
def fart(v0, a, tid):
    return v0 + a * tid


# Definerer initialbetingelsene til modellen
s0 = 0    # m
v0x = 15  # m/s
v0y = 25  # m/s
a = -9.81 # m/s^2

teller = 0 # index

# Liste med x-verdier - tiden
tx = np.arange(0, 6, 0.05)
vy = [] # tom liste som skal inneholde fart som funksjon av tid

# Genererer v-verdier verdier for alle tidspunkt t
for x in tx:
    vy.append(-fart(v0y, a, x)) # Studer denne! Legger til ny verdi i lista (append).
                        #Minus grunnet koordinatsystemet.

# Starter pygame
pygame.init()

field = pygame.image.load('anim_fotball_bane.png')
ball = pygame.image.load('anim_fotball.png')

fieldrect = field.get_rect()
ballrect = ball.get_rect()

# Setter vindusstørrelsen til det samme som størrelsen på bildet 
screen = pygame.display.set_mode(fieldrect.size)

# Plasserer ballen der vi vil at den skal starte
ballrect.top = fieldrect.height - ballrect.height
ballrect.left = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    try: # Flytter ballen og øker teller
        ballrect = ballrect.move([v0x // 2, vy[teller] // 2])
        teller += 1
    except IndexError: # Vi har kommet til enden av lista
        # Nullstiller teller
        teller = 0
        # Flytter ball tilbake til startpunkt
        ballrect.top = fieldrect.height - ballrect.height
        ballrect.left = 10

    # Skriver ut bakgrunnsbilde og ballen i sin nye posisjon.
    screen.blit(field, fieldrect)
    screen.blit(ball, ballrect)
    pygame.display.flip()