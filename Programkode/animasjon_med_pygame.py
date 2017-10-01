'''
Fotballpong v1
Lisens: Creative Commons BY-SA bitjungle
Denne pygame-demoen er basert på http://pygame.org/docs/tut/PygameIntro.html 
'''
import sys
import pygame

pygame.init()

field = pygame.image.load('animasjon_med_pygame_bane.png')
ball = pygame.image.load("animasjon_med_pygame_ball.png")
caption = pygame.display.set_caption("Fotballpong v1")

fieldrect = field.get_rect()
ballrect = ball.get_rect()

offset = [5, 5]

screen = pygame.display.set_mode(fieldrect.size)

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
    screen.blit(ball, ballrect)
    pygame.display.flip()

