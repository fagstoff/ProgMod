'''
Fotballpong v1
Lisens: Creative Commons BY-SA bitjungle
Denne pygame-demoen er basert på http://pygame.org/docs/tut/PygameIntro.html 
'''
import sys
import pygame

# Laster moduler i Pygame-biblioteket
pygame.init()

# Laster inn bilder
field = pygame.image.load('fotballpong_bane.png')
ball = pygame.image.load("fotballpong_ball.png")

# Rektangler for banen og ballen
fieldrect = field.get_rect()
ballrect = ball.get_rect()

# Initiell hastighet på ballen i x- og y-retning
offset = [5, 5]

# Oppretter vinduet, og setter navn på det
screen = pygame.display.set_mode(fieldrect.size)
caption = pygame.display.set_caption("Fotballpong v1")

# Gjør klar en font som skal brukes for å skrive info til vinduet
font = pygame.font.SysFont("monospace", 24)
PALE_GREEN = (152,251,152)
TEXT_POS_TOP = 20
TEXT_POS_LEFT = fieldrect.width // 8

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() # Avslutter programmet når vinduet lukkes

    # Skriver info om posisjonen til ballen
    text = font.render("(top,left)=({},{})".format(ballrect.top, ballrect.left), True, PALE_GREEN)

    # Flytter på ballen
    ballrect = ballrect.move(offset)

    # Sjekker om ballen har truffet en kant
    if ballrect.left < 0 or ballrect.right > fieldrect.width:
        offset[0] = -offset[0] # Endrer fortegn for å skifte retning på ballen
    if ballrect.top < 0 or ballrect.bottom > fieldrect.height:
        offset[1] = -offset[1] # Endrer fortegn for å skifte retning på ballen

    # Tegner bilder til skjermen
    screen.blit(field, fieldrect)
    screen.blit(text,(TEXT_POS_LEFT, TEXT_POS_TOP))
    screen.blit(ball, ballrect)
    pygame.display.flip()

