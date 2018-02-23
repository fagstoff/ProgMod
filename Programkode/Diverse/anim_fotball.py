""" Animasjon av fotball """
# Lisens: Creative Commons BY-SA bitjungle (Rune Mathisen) 2018
#
# Dette er en animasjon laget med Pygame som viser en fotball i bevegelse
# med en fotballbane som bakgrunn. Denne kan være utgangspunkt for å lage 
# et spill, se for eksempel dette prosjektet:
# https://github.com/bitjungle/fotballpong
import sys
import pygame

pygame.init()

field = pygame.image.load('anim_fotball_bane.png')
ball = pygame.image.load('anim_fotball.png')

fieldrect = field.get_rect()
ballrect = ball.get_rect()

offset = [5, 5]

screen = pygame.display.set_mode(fieldrect.size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(offset)

    if ballrect.left < 0 or ballrect.right > fieldrect.width:
        offset[0] = -offset[0]
    if ballrect.top < 0 or ballrect.bottom > fieldrect.height:
        offset[1] = -offset[1]

    screen.blit(field, fieldrect)
    screen.blit(ball, ballrect)
    pygame.display.flip()