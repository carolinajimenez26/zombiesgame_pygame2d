from loser import game_over
from levelup import levelup
from main import main
from level1 import *
from level2 import *


def game(ANCHO,ALTO):

    terminarp=False
    level = 2

    while(not terminarp):

        if(level==1):
            level = level1(ANCHO,ALTO)

        if(level==2):
            level = level2(ANCHO,ALTO)
            if(level>=3):
                terminarp=True
