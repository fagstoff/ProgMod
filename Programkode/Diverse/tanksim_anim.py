""" Animasjon av vanntank som fylles og tømmes """
# Lisens: Creative Commons BY-SA bitjungle (Rune Mathisen) 2018
#
# Dette er en animasjon laget med Pygame som viser en tank som fylles og tømmes.
# Det er ikke implementert noen modell som viser forløpet på en presis måte,  
# her er fylling og tømming en lineær funksjon av tiden. Vil du ha gode modeller 
# for hvordan forløpet virkelig er, se tankmodell 2-5 her:
# https://github.com/fagstoff/ProgMod/blob/master/Fagstoff/index.ipynb 

import sys
import pygame

pygame.init()

# Farge-definisjoner, RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (211,211,211)
SEA_BLUE = (0,105,148)

# Dimensjonene til programvinduet
SIZE = WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode(SIZE)
CENTER_HORIZ = WIDTH // 2
CENTER_VERT = HEIGHT // 2

# Hvor mange bilder i sekundet (FPS) skal vi tegne?
FPS = 10
timer = pygame.time.Clock()
timer_txt = pygame.font.SysFont('Consolas', 30)


tank_params = {
    "left": CENTER_HORIZ - 50, # Trekker fra halvparten av bredden
    "top": CENTER_VERT - 50,   # Trekker fra halvparten av høyden
    "width": 100,              # Tankens høyde
    "height": 100,             # Tankens bredde
    "level": 10,               # Nivået vi starter med
    "fill_color": SEA_BLUE,    # Farge på innholdet i tanken
    "outline_color": WHITE,    # Farge på omrisset av tanken
    "border_width": 3          # Bredde på omrisset av tanken
}

# Endring av nivå mellom hvert bilde som vises (FPS)
level_change = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Bakgrunnsfargen
    screen.fill(BLACK)
    
    # Tegner inn tanknivået
    pygame.draw.rect(screen, SEA_BLUE, 
                     pygame.Rect(tank_params["left"], 
                                 tank_params["top"] + (tank_params["height"] - tank_params["level"]), 
                                 tank_params["width"], 
                                 tank_params["level"]))
    # Tegner omrisset av tanken
    pygame.draw.rect(screen, WHITE, 
                     pygame.Rect(tank_params["left"], 
                                 tank_params["top"], 
                                 tank_params["width"], 
                                 tank_params["height"]), 
                     tank_params["border_width"])
    
    # Sjekk om vi har nådd topp eller bunn, og endre fortegn på level_cange
    if tank_params["level"] > tank_params["height"] or tank_params["level"] < 0:
        level_change *= -1

    # Endrer nivået i tanken
    tank_params["level"] += level_change

    # Tegner inn "vannstrålen" inn i eller ut av tanken
    if level_change > 0: # tanken fylles
        pygame.draw.line(screen, SEA_BLUE, 
                    (CENTER_HORIZ,0), 
                    (CENTER_HORIZ, tank_params["top"] + tank_params["height"] - tank_params["border_width"]), 4)
    else: # tanken tømmes
        pygame.draw.line(screen, SEA_BLUE, 
                    (CENTER_HORIZ, tank_params["top"] + tank_params["height"] - tank_params["border_width"]), 
                    (CENTER_HORIZ, HEIGHT), 4)

    timer_string = "Medgått tid: {} sekunder".format(round(pygame.time.get_ticks() / 1000, 1))
    screen.blit(timer_txt.render(timer_string, True, LIGHT_GRAY), (CENTER_HORIZ // 2, 10))
    pygame.display.flip()
    timer.tick(FPS)
