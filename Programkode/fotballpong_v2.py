'''
Fotballpong v2
Lisens: Creative Commons BY-SA bitjungle
Denne pygame-demoen er basert på http://pygame.org/docs/tut/PygameIntro.html 
'''
import sys
import pygame

def main():
    '''Game main loop'''
    pygame.init()

    # Loading images
    field = pygame.image.load('fotballpong_bane.png')
    ball = pygame.image.load("fotballpong_ball.png")
    player1 = pygame.image.load("fotballpong_spiller_v.png")
    player2 = pygame.image.load("fotballpong_spiller_h.png")

    fieldrect = field.get_rect()
    ballrect = ball.get_rect()
    player1rect = player1.get_rect()
    player2rect = player2.get_rect()

    ball_offset = [5, 5]
    player1_offset = [0, 2]
    player2_offset = [0, -2]

    FIELD_PADDING = 50 # Ball will bounce 50 pixels from the edge of the field

    screen = pygame.display.set_mode(fieldrect.size)
    caption = pygame.display.set_caption("Fotballpong v2")

    # Set initial player positions
    player1rect.top = (fieldrect.height // 2) - (player1rect.height // 2)
    player2rect.top = (fieldrect.height // 2) - (player2rect.height // 2)
    player1rect.left = (fieldrect.width // 2) - (fieldrect.width // 4) - player1rect.width
    player2rect.left = (fieldrect.width // 2) + (fieldrect.width // 4)

    # set initial ball position
    ballrect.top = (fieldrect.height // 2) - (ballrect.height // 2)
    ballrect.left = (fieldrect.width // 2) - (ballrect.width // 2)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        # Moving the ball
        ballrect = ballrect.move(ball_offset)

        # Check if the ball collides with a player
        if ballrect.colliderect(player1rect):
            player_kick = True
        elif ballrect.colliderect(player2rect):
            player_kick = True
        else:
            player_kick = False

        # Check if the ball collides with an edge
        if ballrect.left < FIELD_PADDING or ballrect.right > fieldrect.width - FIELD_PADDING or player_kick:
            ball_offset[0] = -ball_offset[0]
        if ballrect.top < 0 or ballrect.bottom > fieldrect.height:
            ball_offset[1] = -ball_offset[1]
        
        # Move player 1, check if he collides with an edge
        player1rect = player1rect.move(player1_offset)
        if player1rect.top < 0 or player1rect.bottom > fieldrect.height:
            player1_offset[1] = -player1_offset[1]

        # Move player 2, check if he collides with an edge
        player2rect = player2rect.move(player2_offset)
        if player2rect.top < 0 or player2rect.bottom > fieldrect.height:
            player2_offset[1] = -player2_offset[1]

        # Print images to screen
        screen.blit(field, fieldrect)
        screen.blit(player1, player1rect)
        screen.blit(player2, player2rect)
        screen.blit(ball, ballrect)
        pygame.display.flip()

if __name__ == '__main__':
    main()
