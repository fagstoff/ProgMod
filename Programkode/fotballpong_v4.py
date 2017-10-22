'''
Fotballpong v4
License: Creative Commons BY-SA bitjungle
TODO versjon 5:
* Lydeffekter
* Spiller beveger seg bare ved keypress
* Ball spretter med vinkel fra spiller avhengig av treffpunkt
TODO versjon 6:
* Player 2 AI
* Tidsbegrenset spill (klokke)
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
        self.image = pygame.image.load(self.get_variable('imagefile'))
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
        self.image = pygame.image.load(self.get_variable('imagefile'))
        self.rect = self.image.get_rect()
        if self.get_variable('offset') is None:
            self.set_variable('offset', [0, 0])

    def move(self):
        self.rect = self.rect.move(self._vars['offset'])

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

    def flip_horiz(self):
        '''Flip the x value in the offset [x, y] pair'''
        self._vars['offset'][0] *= -1

    def flip_vert(self):
        '''Flip the y value in the offset [x, y] pair'''
        self._vars['offset'][1] *= -1

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
        '''Increment player score'''
        self._vars['score'] += 1

class Ball(MovingImage):
    '''Ball object'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class TextElement(GameObject):
    '''Game text elements'''
    def __init__(self, **kwargs):
        super(TextElement, self).__init__(**kwargs)
        if self.get_variable('fontfile') is None:
            self.set_variable('fontfile', 'SourceCodePro-Regular.ttf')
        if self.get_variable('fontsize') is None:
            self.set_variable('fontsize', 24)
        
        try: 
            self._font = pygame.font.Font(self.get_variable('fontfile'), self.get_variable('fontsize'))
        except OSError as e:
            self._font = pygame.font.SysFont('courier', self.get_variable('fontsize'))

        if self.get_variable('color') is None:
            self.set_variable('color', (0,0,0))
        if self.get_variable('text') is None:
            self.set_variable('text', '')
        if self.get_variable('antialias') is None:
            self.set_variable('antialias', True)
        
        self.render(self.get_variable('text'))
    
    def render(self, text=None):
        if text != None: self.set_variable('text', text)
        self.image = self._font.render(self.get_variable('text'), 
                                       self.get_variable('antialias'), 
                                       self.get_variable('color'))



def main():
    '''Game main loop'''
    pygame.init()

    # Creating game objects
    field = Field(imagefile='fotballpong_bane.png')
    ball = Ball(imagefile="fotballpong_ball.png", offset=[5, 5])
    p1 = Player(imagefile="fotballpong_spiller_v.png")
    p2 = Player(imagefile="fotballpong_spiller_h.png")
    g1 = Goal()
    g2 = Goal()

    # Setting up goal positions on field
    g1.set_top((field.rect.height // 2) - (g1.rect.height // 2))
    g1.set_left(25)
    g2.set_top((field.rect.height // 2) - (g1.rect.height // 2))
    g2.set_left(field.rect.width - 50)
    
     # Ball will bounce x pixels from the edge of the field
    FIELD_PADDING_LEFTRIGHT = 50
    FIELD_PADDING_TOPBOTTOM = 25

    # Preparing the scoreboard
    PLAYER1_STATIC_TXT = 'Player 1 (↑W ↓S): {}'
    PLAYER2_STATIC_TXT = 'Player 2 (↑O ↓L): {}'
    p1_txt = TextElement(fontfile='SourceCodePro-Regular.ttf', fontsize=24, color=PALE_GREEN)
    p1_txt.set_top(20)
    p1_txt.set_left(field.rect.width // 8)
    p2_txt = TextElement(fontfile='SourceCodePro-Regular.ttf', fontsize=24, color=PALE_GREEN)
    p2_txt.set_top(20)
    p2_txt.set_left((field.rect.width // 2) + (field.rect.width // 8))

    # Set initial player positions
    p1.set_top((field.rect.height // 2) - (p1.rect.height // 2))
    p2.set_top((field.rect.height // 2) - (p2.rect.height // 2))
    p1.set_left((field.rect.width // 2) - (field.rect.width // 4) - p1.rect.width)
    p2.set_left((field.rect.width // 2) + (field.rect.width // 4))

    # Set initial ball position
    ball.center_on_rect(field.rect)

    goal_scored = False # Used for flagging a goal
    GOAL_TXT_DISPLAY_TIME = 1000 # Number of milliseconds to display GOAL!
    goal_txt_display_start_time = 0 # Keeping track of how long GOAL! has been displayed
    goal_text = TextElement(fontfile='SourceCodePro-Regular.ttf', fontsize=48, text='GOAL!', color=GOLD)
    goal_text.center_on_rect(field.rect)

    # Preparing the screen
    screen = pygame.display.set_mode(field.rect.size)
    #screen = pygame.display.set_mode(field.rect.size, pygame.FULLSCREEN)
    caption = pygame.display.set_caption("Fotballpong v4")

    # Setting up the clock
    clock = pygame.time.Clock()
    FPS = 50 # Limit frames per second

    while True:
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == pygame.QUIT or key[pygame.K_q] or key[pygame.K_ESCAPE]: sys.exit()
            if key[pygame.K_w]: p1.set_offset(-4)
            if key[pygame.K_s]: p1.set_offset(4)
            if key[pygame.K_o]: p2.set_offset(-4)
            if key[pygame.K_l]: p2.set_offset(4)

        # Creating/updating the score board
        p1_txt.render(PLAYER1_STATIC_TXT.format(p1.get_variable('score')))
        p2_txt.render(PLAYER2_STATIC_TXT.format(p2.get_variable('score')))

        # Moving the ball
        ball.move()

        # Check if the ball collides with a player or goal or field edge
        if ball.colliderect(p1.rect): # hitting player 1
            ball.flip_horiz()
        elif ball.colliderect(p2.rect): # hitting player 2
            ball.flip_horiz()
        elif ball.colliderect(g1.rect): # player 2 scores
            p2.increment_score()
            ball.flip_horiz()
            ball.center_on_rect(field.rect)
            goal_scored = True
        elif ball.colliderect(g2.rect): # player 1 scores
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
        screen.blit(field.image, field.rect)
        screen.blit(p1_txt.image,p1_txt.rect)
        screen.blit(p2_txt.image,p2_txt.rect)
        screen.blit(p1.image, p1.rect)
        screen.blit(p2.image, p2.rect)
        screen.blit(ball.image, ball.rect)
        screen.blit(g1.image, g1.rect)
        screen.blit(g2.image, g2.rect)

        if goal_scored == True:
            if goal_txt_display_start_time == 0:
                goal_txt_display_start_time = pygame.time.get_ticks()
            if pygame.time.get_ticks() - goal_txt_display_start_time < GOAL_TXT_DISPLAY_TIME:
                #TODO fix positioning
                screen.blit(goal_text.image,(goal_text.rect.left - 60, goal_text.rect.top - 70))
            else:  # resetting 
                goal_txt_display_start_time = 0
                goal_scored = False

        # Finish the loop, redraw display and tick the clock
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
