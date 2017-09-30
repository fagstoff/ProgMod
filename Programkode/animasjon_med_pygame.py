'''
Lisens: Creative Commons BY-SA bitjungle
Denne pygame-demoen er basert på http://pygame.org/docs/tut/PygameIntro.html 
'''
import sys
import pygame

def main():
    '''Hoved-loopen i programmet'''

    pygame.init()

    field = pygame.image.load('animasjon_med_pygame_bane.png')
    ball = pygame.image.load("animasjon_med_pygame_ball.png")

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

if __name__ == '__main__':
    main()
