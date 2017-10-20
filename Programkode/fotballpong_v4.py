'''
Fotballpong v3
Lisens: Creative Commons BY-SA bitjungle
TODO versjon 4:
* Objektorientere
* Lydeffekter
TODO versjon 5:
* Player 2 AI
'''
import sys
import pygame

class Field():
    '''The football field'''
    def __init__(self, **kwargs):
        super(Field, self).__init__()
        self._vars = kwargs
        self.image = pygame.image.load(self.get_variable('image'))
        self.rect = self.image.get_rect()

    def get_variable(self, key):
        '''Get a variable value, returns None if the variable is not set'''
        return self._vars.get(key, None)

    def set_variable(self, key, val):
        '''Set a variable value'''
        self._vars[key] = val

class MovingImage():
    '''A moving image object'''
    def __init__(self, **kwargs):
        super(MovingImage, self).__init__()
        self._vars = kwargs
        self.image = pygame.image.load(self.get_variable('image'))
        self.rect = self.image.get_rect()
        if self.get_variable('offset') is None:
            self.set_variable('offset', [0, 0])

    def move(self):
        self.rect = self.rect.move(self._vars['offset'])

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

    def flip_horiz(self):
        '''Flip the x value in the offset [x, y] pair'''
        self._vars['offset'][0] = -self._vars['offset'][0]

    def flip_vert(self):
        '''Flip the y value in the offset [x, y] pair'''
        self._vars['offset'][1] = -self._vars['offset'][1]

    def get_variable(self, key):
        '''Get a variable value, returns None if the variable is not set'''
        return self._vars.get(key, None)

    def set_variable(self, key, val):
        '''Set a variable value'''
        self._vars[key] = val

class Player(MovingImage):
    '''Football player object'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._vars['offset'][0] = 0 # Players can only move vertical
        self._vars['score'] = 0 # initial score
    
    def set_offset(self, vert_offset):
        '''Set the vertical offset for the player'''
        self._vars['offset'][1] = vert_offset
    
    def increment_score(self):
        self._vars['score'] += 1

class Ball(MovingImage):
    '''Ball object'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

def center_rect_on_rect(rect, target_rect):
    '''Center a rect in the middle of a target rect'''
    rect.top = (target_rect.height // 2) - (rect.height // 2)
    rect.left = (target_rect.width // 2) - (rect.width // 2)

def main():
    '''Game main loop'''
    pygame.init()

    # Color definitions
    PALE_GREEN = (152,251,152)
    LIGHT_GRAY = (211,211,211)
    GOLD = (255,215,0)

    # Loading images
    field = Field(image='fotballpong_bane.png')
    ball = Ball(image="fotballpong_ball.png", offset=[5, 5])
    p1 = Player(image="fotballpong_spiller_v.png")
    p2 = Player(image="fotballpong_spiller_h.png")

    goal1 = pygame.Surface((25,100))
    goal2 = pygame.Surface((25,100))
    goal1rect = goal1.get_rect()
    goal2rect = goal2.get_rect()
    goal1rect.top = (field.rect.height // 2) - (goal1rect.height // 2)
    goal2rect.top = (field.rect.height // 2) - (goal2rect.height // 2)
    goal1rect.left = 25
    goal2rect.left = field.rect.width - 50
    goal1.fill(LIGHT_GRAY)
    goal2.fill(LIGHT_GRAY)

     # Ball will bounce x pixels from the edge of the field
    FIELD_PADDING_LEFTRIGHT = 50
    FIELD_PADDING_TOPBOTTOM = 25

    screen = pygame.display.set_mode(field.rect.size)
    caption = pygame.display.set_caption("Fotballpong v4")
    clock = pygame.time.Clock()
    FPS = 50 # Limit frames per second

    # Preparing the scoreboard
    font = pygame.font.Font("SourceCodePro-Regular.ttf", 24)
    TEXT_POS_TOP = 20
    PLAYER1_SCORE_POS_LEFT = field.rect.width // 8
    PLAYER2_SCORE_POS_LEFT = (field.rect.width // 2) + (field.rect.width // 8)
    GOAL_POS_LEFT = (field.rect.width // 2)

    # Set initial player positions
    p1.rect.top = (field.rect.height // 2) - (p1.rect.height // 2)
    p2.rect.top = (field.rect.height // 2) - (p2.rect.height // 2)
    p1.rect.left = (field.rect.width // 2) - (field.rect.width // 4) - p1.rect.width
    p2.rect.left = (field.rect.width // 2) + (field.rect.width // 4)

    # Set initial ball position
    center_rect_on_rect(ball.rect, field.rect)

    goal_scored = False


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_w]: p1.set_offset(-4)
            if key[pygame.K_s]: p1.set_offset(4)
            if key[pygame.K_o]: p2.set_offset(-4)
            if key[pygame.K_l]: p2.set_offset(4)

        player1_score_txt = font.render("Player 1: {}".format(p1.get_variable('score')), True, PALE_GREEN)
        player2_score_txt = font.render("Player 2: {}".format(p2.get_variable('score')), True, PALE_GREEN)
        goal_text = font.render("GOAL!", True, GOLD)

        # Moving the ball
        ball.move()

        # Check if the ball collides with a player or goal or field edge
        if ball.colliderect(p1.rect):
            ball.flip_horiz()
        elif ball.colliderect(p2.rect):
            ball.flip_horiz()
        elif ball.colliderect(goal1rect):
            p2.increment_score()
            ball.flip_horiz()
            center_rect_on_rect(ball.rect, field.rect)
            goal_scored = True
        elif ball.rect.colliderect(goal2rect):
            p1.increment_score()
            ball.flip_horiz()
            center_rect_on_rect(ball.rect, field.rect)
            goal_scored = True
        elif ball.rect.left < FIELD_PADDING_LEFTRIGHT or ball.rect.right > field.rect.width - FIELD_PADDING_LEFTRIGHT: 
            ball.flip_horiz()
        elif ball.rect.top - FIELD_PADDING_TOPBOTTOM < 0 or ball.rect.bottom > field.rect.height - FIELD_PADDING_TOPBOTTOM:
            ball.flip_vert()
        else:
            pass # Do nothing
        
        # Move player 1, check if he collides with an edge
        p1.move()
        if p1.rect.top < 0 or p1.rect.bottom > field.rect.height:
            p1.flip_vert()
            p1.move()

        # Move player 2, check if he collides with an edge
        p2.move()
        if p2.rect.top < 0 or p2.rect.bottom > field.rect.height:
            p2.flip_vert()
            p2.move()

        # Print images to screen
        if goal_scored == True:
            #BUG teksten vises ikke
            screen.blit(goal_text,(GOAL_POS_LEFT-28, TEXT_POS_TOP+150))
            pygame.display.flip()
            pygame.time.wait(1000)
            goal_scored = False # resetting
        screen.blit(field.image, field.rect)
        screen.blit(player1_score_txt,(PLAYER1_SCORE_POS_LEFT, TEXT_POS_TOP))
        screen.blit(player2_score_txt,(PLAYER2_SCORE_POS_LEFT, TEXT_POS_TOP))
        screen.blit(p1.image, p1.rect)
        screen.blit(p2.image, p2.rect)
        screen.blit(ball.image, ball.rect)
        screen.blit(goal1, goal1rect)
        screen.blit(goal2, goal2rect)
        pygame.display.flip()

        clock.tick(FPS)

if __name__ == '__main__':
    main()
