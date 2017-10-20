'''
Fotballpong v3
Lisens: Creative Commons BY-SA bitjungle
TODO versjon 3:
* Flytte kode ut fra main()
TODO versjon 4:
* Objektorientere
* Lydeffekter
* Player 2 AI
'''
import sys
import pygame

def center_rect_on_rect(rect, target_rect):
    '''Center a rect in the middle of a target rect'''
    rect.top = (target_rect.height // 2) - (rect.height // 2)
    rect.left = (target_rect.width // 2) - (rect.width // 2)

def flip_horiz(offset):
    '''Flip the x value in a [x, y] pair'''
    offset[0] = -offset[0]

def flip_vert(offset):
    '''Flip the y value in a [x, y] pair'''
    offset[1] = -offset[1]

def main():
    '''Game main loop'''
    pygame.init()

    # Color definitions
    PALE_GREEN = (152,251,152)
    LIGHT_GRAY = (211,211,211)
    GOLD = (255,215,0)

    # Loading images
    field = pygame.image.load('fotballpong_bane.png')
    ball = pygame.image.load("fotballpong_ball.png")
    player1 = pygame.image.load("fotballpong_spiller_v.png")
    player2 = pygame.image.load("fotballpong_spiller_h.png")

    fieldrect = field.get_rect()
    ballrect = ball.get_rect()
    player1rect = player1.get_rect()
    player2rect = player2.get_rect()

    goal1 = pygame.Surface((25,100))
    goal2 = pygame.Surface((25,100))
    goal1rect = goal1.get_rect()
    goal2rect = goal2.get_rect()
    goal1rect.top = (fieldrect.height // 2) - (goal1rect.height // 2)
    goal2rect.top = (fieldrect.height // 2) - (goal2rect.height // 2)
    goal1rect.left = 25
    goal2rect.left = fieldrect.width - 50
    goal1.fill(LIGHT_GRAY)
    goal2.fill(LIGHT_GRAY)

    # Initial speed of ball and players in x and y direction
    ball_offset = [5, 5]
    player1_vertical_offset = 0
    player2_vertical_offset = 0

     # Ball will bounce x pixels from the edge of the field
    FIELD_PADDING_LEFTRIGHT = 50
    FIELD_PADDING_TOPBOTTOM = 25

    screen = pygame.display.set_mode(fieldrect.size)
    caption = pygame.display.set_caption("Fotballpong v3")
    clock = pygame.time.Clock()
    FPS = 50 # Limit frames per second

    # Preparing the scoreboard
    font = pygame.font.Font("SourceCodePro-Regular.ttf", 24)
    TEXT_POS_TOP = 20
    PLAYER1_SCORE_POS_LEFT = fieldrect.width // 8
    PLAYER2_SCORE_POS_LEFT = (fieldrect.width // 2) + (fieldrect.width // 8)
    GOAL_POS_LEFT = (fieldrect.width // 2)

    # Set initial player positions
    player1rect.top = (fieldrect.height // 2) - (player1rect.height // 2)
    player2rect.top = (fieldrect.height // 2) - (player2rect.height // 2)
    player1rect.left = (fieldrect.width // 2) - (fieldrect.width // 4) - player1rect.width
    player2rect.left = (fieldrect.width // 2) + (fieldrect.width // 4)

    # Set initial ball position
    center_rect_on_rect(ballrect, fieldrect)

    # Set initial score
    player1_score = 0
    player2_score = 0
    goal_scored = False


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_w]: player1_vertical_offset = -4
            if key[pygame.K_s]: player1_vertical_offset = 4
            if key[pygame.K_o]: player2_vertical_offset = -4
            if key[pygame.K_l]: player2_vertical_offset = 4

        player1_score_txt = font.render("Player 1: {}".format(player1_score), True, PALE_GREEN)
        player2_score_txt = font.render("Player 2: {}".format(player2_score), True, PALE_GREEN)
        goal_text = font.render("GOAL!", True, GOLD)

        # Moving the ball
        ballrect = ballrect.move(ball_offset)

        # Check if the ball collides with a player or goal or field edge
        if ballrect.colliderect(player1rect):
            flip_horiz(ball_offset)
        elif ballrect.colliderect(player2rect):
            flip_horiz(ball_offset)
        elif ballrect.colliderect(goal1rect):
            player2_score += 1
            flip_horiz(ball_offset)
            center_rect_on_rect(ballrect, fieldrect)
            goal_scored = True
        elif ballrect.colliderect(goal2rect):
            player1_score += 1
            flip_horiz(ball_offset)
            center_rect_on_rect(ballrect, fieldrect)
            goal_scored = True
        elif ballrect.left < FIELD_PADDING_LEFTRIGHT or ballrect.right > fieldrect.width - FIELD_PADDING_LEFTRIGHT: 
            flip_horiz(ball_offset)
        elif ballrect.top - FIELD_PADDING_TOPBOTTOM < 0 or ballrect.bottom > fieldrect.height - FIELD_PADDING_TOPBOTTOM:
            flip_vert(ball_offset)
        else:
            pass # Do nothing
        
        # Move player 1, check if he collides with an edge
        player1rect = player1rect.move([0, player1_vertical_offset])
        if player1rect.top < 0 or player1rect.bottom > fieldrect.height:
            player1rect = player1rect.move([0, -player1_vertical_offset])

        # Move player 2, check if he collides with an edge
        player2rect = player2rect.move([0, player2_vertical_offset])
        if player2rect.top < 0 or player2rect.bottom > fieldrect.height:
            player2rect = player2rect.move([0, -player2_vertical_offset])

        # Print images to screen
        if goal_scored == True:
            screen.blit(goal_text,(GOAL_POS_LEFT-28, TEXT_POS_TOP+150))
            pygame.display.flip()
            pygame.time.wait(1000)
            goal_scored = False # resetting
        screen.blit(field, fieldrect)
        screen.blit(player1_score_txt,(PLAYER1_SCORE_POS_LEFT, TEXT_POS_TOP))
        screen.blit(player2_score_txt,(PLAYER2_SCORE_POS_LEFT, TEXT_POS_TOP))
        screen.blit(player1, player1rect)
        screen.blit(player2, player2rect)
        screen.blit(ball, ballrect)
        screen.blit(goal1, goal1rect)
        screen.blit(goal2, goal2rect)
        pygame.display.flip()

        clock.tick(FPS)

if __name__ == '__main__':
    main()
