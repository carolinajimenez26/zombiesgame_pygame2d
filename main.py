import pygame
import random
import sys
import os
curdir = os.getcwd()+"/sources"

blanco=(255,255,255)

#Algoritmo de Bresenham para la recta
def Bresenhamecta((x0,y0),(x1,y1),pantalla):
    dx=x1-x0
    dy=y1-y0
    res=[]
    if(dy < 0 ):
        dy=-1*dy
        stepy=-1
    else:
        stepy=1
    if(dx<0):
        dx=-1*dx
        stepx=-1
    else:
        stepx=1
        x=x0
        y=y0
    res.append((x,y))
    if(dx>dy):
        p=2*dy-dx
        incE=2*dy
        incNE=2*(dy-dx)
        while(x != x1):
            x=x+stepx
            if(p<0):
                p=p+incE
            else:
                y=y+stepy
                p=p+incNE
        res.append((x,y))
    else:
        p=2*dx-dy
        incE=2*dx
        incNE=2*(dx-dy)
        while(y != y1):
            y=y+stepy
            if(p<0):
                p=p+incE
            else:
                x=x+stepx
                p=p+incNE
        res.append((x,y))
#fin Algoritmo de Bresenham para la recta

#Dibuja los 8 octantes para el Algoritmo de Bresenham para la circunferencia
def plotpoint((x0,y0),(x,y),pantalla,res):
    res.append((x0+x,y0+y))
    res.append((x0-x,y0+y))
    res.append((x0+x,y0-y))
    res.append((x0-x,y0-y))
    res.append((x0+y,y0+x))
    res.append((x0-y,y0+x))
    res.append((x0+y,y0-x))
    res.append((x0-y,y0-x))
#Fin dibuja 8 octantes Algoritmo de Bresenham para la circunferencia

#Algoritmo de Bresenham para la circunferencia
def CircunfPtoMedio((x0,y0),r, pantalla):
    x=0
    y=r
    p=1-r
    res=[]
    #pygame.draw.line(pantalla, blanco, (x0,y0), (x,y), 1 )
    plotpoint((x0,y0),(x,y),pantalla,res)
    while(x<y):
        x=x+1
        if(p<0):
            p=p+2*x+1
        else:
            y=y-1
            p=p+2*(x-y)+1
    plotpoint((x0,y0),(x,y),pantalla)
    return res
#fin Algoritmo de Bresenham para la circunferencia


#Carga los sonidos verificando la ruta
def load_sound(nombre_s,dir_son):
    ruta = os.path.join(dir_son+"/sounds", nombre_s)
    try:
        sound = pygame.mixer.Sound(ruta)
    except:
        print "Error, no se puede cargar el sonido, verifique el formato: ", ruta
        sys.exit(1)
    return sound

#Funcion para verificar que las imagenes se cargan correctamente
def load_image(nombre_a, dir_img, alpha=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_img+"/images", nombre_a)
    try:
        image = pygame.image.load(ruta)
    except:
        print "Error, no se puede cargar la imagen: ", ruta
        sys.exit(1)
    # Comprobar si la imagen tiene "canal alpha" (como los png)
    if alpha == True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image


class Enemigo(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(imagen,curdir,alpha=True)
        self.rect = self.image.get_rect()
        self.direccion=0
    def update(self):
        if(self.rect.x >= (ANCHO-self.rect[2])):
            self.direccion=1
        if(self.rect.x <= (self.rect[2])):
            self.direccion=0
        if (self.direccion == 0):
            self.rect.x+=5
        else:
            self.rect.x-=5

class Bala(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(imagen,curdir,alpha=True)
        self.rect = self.image.get_rect()
        self.velocidad=5
    def update(self):
        self.rect.x+=self.velocidad


class Jugador(pygame.sprite.Sprite):

    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(imagen,curdir,alpha=True)
        self.rect = self.image.get_rect()
        self.vida = 100
        self.score=0
    def chocar(self):
        self.vida-=10

def menu():
    pygame.init()
    menu_d=pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
    backgroundm=load_image('backgroundm.jpg',curdir,alpha=False)
    s_fondo=load_sound('fondo1.sf',curdir)
    s_fondo.play()
    menu_d.blit(backgroundm,(0,0))

    pygame.display.flip()

    terminar=False

    while(not terminar):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                terminar=True

def main():
    menu()



if __name__ == "__main__":
    main()
