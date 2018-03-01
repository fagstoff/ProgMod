""" Animasjon av fotball """
# Lisens: Creative Commons BY-SA bitjungle (Rune Mathisen) 2018
#
# Dette er en animasjon laget med Pygame som viser en fotball i bevegelse
# med en fotballbane som bakgrunn. Denne kan være utgangspunkt for å lage 
# et spill, se for eksempel dette prosjektet:
# https://github.com/bitjungle/fotballpong

# importerer nødvendige biblioteker
import sys
import pygame

# Gjør pygame klar til bruk
pygame.init()

# Laster inn grafikk fra fil
field = pygame.image.load('anim_fotball_bane.png')
ball = pygame.image.load('anim_fotball.png')

# Lager rekatngulær instans/objekt med samme størelse om bane/ball
fieldrect = field.get_rect()
ballrect = ball.get_rect()

# Setter størrelsen på programvinduet.
screen = pygame.display.set_mode(fieldrect.size)

# Hvor mye skal ballen flyttes i [x,y]-retning for hver oppdatering
offset = [5, 5]

# Hovedløkka - Ball flyttes og bilde oppdateres
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(offset) # Flytter ballen [x,y] piksler

    # Snur ballens retning når den når kanten
    if ballrect.left < 0 or ballrect.right > fieldrect.width:
        offset[0] = -offset[0]
    if ballrect.top < 0 or ballrect.bottom > fieldrect.height:
        offset[1] = -offset[1]

    # Oppdaterer skjermbildet
    screen.blit(field, fieldrect)
    screen.blit(ball, ballrect)
    pygame.display.flip()