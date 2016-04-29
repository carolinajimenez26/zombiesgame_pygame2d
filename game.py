from loser import game_over
from levelup import levelup
from main import main
from level1 import *
from level2 import *


def game(ANCHO,ALTO):

    terminarp=False
    level = 1
    vidalifemago=100
    while(not terminarp):

        if(level==1):
            level,vidalifemago = level1(ANCHO,ALTO)
            if(level>=3):
                terminarp=True

        if(level==2):
            level = level2(ANCHO,ALTO,vidalifemago)
            if(level>=3):
                terminarp=True
