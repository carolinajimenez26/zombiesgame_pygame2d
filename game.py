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

        else:
            sys.exit()
