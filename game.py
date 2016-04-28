from loser import game_over
from levelup import levelup
from level1 import *
from level2 import *


def game(ANCHO,ALTO):

    terminarp=False
    level = 2

    while(not terminarp):
        if(level==1):
            terminarp = level1(ANCHO,ALTO)

        if(level==2):
            terminarp = level2(ANCHO,ALTO)
            '''#Inicializacion de pantalla
            pygame.init()
            pantalla = pygame.display.set_mode([ANCHO,ALTO + 50])
            pygame.display.set_caption("Magician-zombie v0.1 - Level 2 ", 'Spine Runtime')
            tipo = pygame.font.SysFont("monospace", 15)
            pantalla.fill((0,0,0))
            #Fin de inicializacion de pantalla'''

        else:
            sys.exit()
