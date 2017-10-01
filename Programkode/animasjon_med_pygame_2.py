'''
Fotballpong v2
Lisens: Creative Commons BY-SA bitjungle
Denne pygame-demoen er basert på http://pygame.org/docs/tut/PygameIntro.html 
TODO:
* Lage klasse for spillerne
* Implementere styring med tastatur
* Kollisjonsdeteksjon med spiller og ball
* Registrere mål
* Telle og vise antall mål
'''
import sys
import pygame

def main():
    '''Hoved-loopen i programmet'''

    pygame.init()

    field = pygame.image.load('animasjon_med_pygame_bane.png')
    ball = pygame.image.load("animasjon_med_pygame_ball.png")
    player1 = pygame.image.load("animasjon_med_pygame_spiller_v.png")
    player2 = pygame.image.load("animasjon_med_pygame_spiller_h.png")

    fieldrect = field.get_rect()
    ballrect = ball.get_rect()
    player1rect = player1.get_rect()
    player2rect = player2.get_rect()

    offset = [5, 5]

    screen = pygame.display.set_mode(fieldrect.size)
    caption = pygame.display.set_caption("Fotballpong v2")

    font = pygame.font.Font("SourceCodePro-Regular.ttf", 24)
    PALE_GREEN = (152,251,152)
    TEXT_POS_TOP = 20
    TEXT_POS_LEFT = fieldrect.width // 8

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        text = font.render("(top,left)=({},{})".format(ballrect.top, ballrect.left), True, PALE_GREEN)

        ballrect = ballrect.move(offset)
        if ballrect.left < 0 or ballrect.right > fieldrect.width:
            offset[0] = -offset[0]
        if ballrect.top < 0 or ballrect.bottom > fieldrect.height:
            offset[1] = -offset[1]

        screen.blit(field, fieldrect)
        screen.blit(text,(TEXT_POS_LEFT, TEXT_POS_TOP))
        screen.blit(player1, (200, 200))
        screen.blit(player2, (600, 100))
        screen.blit(ball, ballrect)
        pygame.display.flip()

if __name__ == '__main__':
    main()
