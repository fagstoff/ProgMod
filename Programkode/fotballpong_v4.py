'''
Fotballpong v4
Lisens: Creative Commons BY-SA bitjungle
TODO versjon 5:
* Lydeffekter
TODO versjon 6:
* Player 2 AI
'''
import sys
import pygame

# Color definitions
PALE_GREEN = (152,251,152)
LIGHT_GRAY = (211,211,211)
GOLD = (255,215,0)

class GameObject(pygame.sprite.Sprite):
    '''Base class for all game objects'''
    def __init__(self, **kwargs):
        super(GameObject, self).__init__()
        self._vars = kwargs
        self.image = pygame.Surface((0,0))
        self.rect = self.image.get_rect()

    def get_variable(self, key):
        '''Get a variable value, returns None if the variable is not set'''
        return self._vars.get(key, None)

    def set_variable(self, key, val):
        '''Set a variable value'''
        self._vars[key] = val

    def set_top(self, pos):
        self.rect.top = pos 

    def set_left(self, pos):
        self.rect.left = pos 
    
    def center_on_rect(self, target_rect):
        '''Center the object in the middle of a target rect'''
        self.rect.top = (target_rect.height // 2) - (self.rect.height // 2)
        self.rect.left = (target_rect.width // 2) - (self.rect.width // 2)


class Field(GameObject):
    '''The football field'''
    def __init__(self, **kwargs):
        super(Field, self).__init__(**kwargs)
        self.image = pygame.image.load(self.get_variable('image'))
        self.rect = self.image.get_rect()

class Goal(GameObject):
    '''Football goal object'''
    def __init__(self, **kwargs):
        super(Goal, self).__init__(**kwargs)

        if self.get_variable('width') is None:
            self.set_variable('width', 25)
        if self.get_variable('height') is None:
            self.set_variable('height', 100)

        self.image = pygame.Surface((self._vars['width'],self._vars['height']))
        self.rect = self.image.get_rect()
        
        if self.get_variable('top') is None:
            self.set_top(0)
        if self.get_variable('left') is None:
            self.set_left(0)
        
        if self.get_variable('fill') is None:
            self.image.fill(LIGHT_GRAY)


class MovingImage(GameObject):
    '''A moving image object'''
    def __init__(self, **kwargs):
        super(MovingImage, self).__init__(**kwargs)
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

def main():
    '''Game main loop'''
    pygame.init()

    # Creating game objects
    field = Field(image='fotballpong_bane.png')
    ball = Ball(image="fotballpong_ball.png", offset=[5, 5])
    p1 = Player(image="fotballpong_spiller_v.png")
    p2 = Player(image="fotballpong_spiller_h.png")

    g1 = Goal()
    g1.set_top((field.rect.height // 2) - (g1.rect.height // 2))
    g1.set_left(25)
    g2 = Goal()
    g2.set_top((field.rect.height // 2) - (g1.rect.height // 2))
    g2.set_left(field.rect.width - 50)
    
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
    GOAL_TXT_POS_LEFT = (field.rect.width // 2)

    # Set initial player positions
    p1.set_top((field.rect.height // 2) - (p1.rect.height // 2))
    p2.set_top((field.rect.height // 2) - (p2.rect.height // 2))
    p1.set_left((field.rect.width // 2) - (field.rect.width // 4) - p1.rect.width)
    p2.set_left((field.rect.width // 2) + (field.rect.width // 4))

    # Set initial ball position
    ball.center_on_rect(field.rect)

    goal_scored = False
    goal_text = font.render("GOAL!", True, GOLD)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_w]: p1.set_offset(-4)
            if key[pygame.K_s]: p1.set_offset(4)
            if key[pygame.K_o]: p2.set_offset(-4)
            if key[pygame.K_l]: p2.set_offset(4)

        # Creating/updating the score board
        player1_score_txt = font.render("Player 1: {}".format(p1.get_variable('score')), True, PALE_GREEN)
        player2_score_txt = font.render("Player 2: {}".format(p2.get_variable('score')), True, PALE_GREEN)

        # Moving the ball
        ball.move()

        # Check if the ball collides with a player or goal or field edge
        if ball.colliderect(p1.rect):
            ball.flip_horiz()
        elif ball.colliderect(p2.rect):
            ball.flip_horiz()
        elif ball.colliderect(g1.rect):
            p2.increment_score()
            ball.flip_horiz()
            ball.center_on_rect(field.rect)
            goal_scored = True
        elif ball.rect.colliderect(g2.rect):
            p1.increment_score()
            ball.flip_horiz()
            ball.center_on_rect(field.rect)
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
            screen.blit(goal_text,(GOAL_TXT_POS_LEFT-28, TEXT_POS_TOP+150))
            pygame.display.flip()
            pygame.time.wait(1000)
            goal_scored = False # resetting
        screen.blit(field.image, field.rect)
        screen.blit(player1_score_txt,(PLAYER1_SCORE_POS_LEFT, TEXT_POS_TOP))
        screen.blit(player2_score_txt,(PLAYER2_SCORE_POS_LEFT, TEXT_POS_TOP))
        screen.blit(p1.image, p1.rect)
        screen.blit(p2.image, p2.rect)
        screen.blit(ball.image, ball.rect)
        screen.blit(g1.image, g1.rect)
        screen.blit(g2.image, g2.rect)
        pygame.display.flip()

        clock.tick(FPS)

if __name__ == '__main__':
    main()
