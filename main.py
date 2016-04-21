import pygame
import sys
import os
import random
curdir = os.getcwd()+"/sources" #Para la ruta total del sistema
from pygame.locals import *

HIGH = 400
WIDTH = 700
WHITE = (255,255,255)

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

#Funcion para verificar que las imagenes se cargan correctamente
def load_image(nombre_a, dir_img, alpha = False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_img, nombre_a)
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

#Carga los sonidos verificando la ruta
def load_sound(nombre_s,dir_son):
    ruta = os.path.join(dir_son, nombre_s)
    try:
        sound = pygame.mixer.Sound(ruta)
    except:
        print "Error, no se puede cargar el sonido, verifique el formato: ", ruta
        sys.exit(1)
    return sound

class Enemy(pygame.sprite.Sprite): #Hereda de la clase sprite
    def __init__(self, img_name, pos):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = load_image(img_name, curdir, alpha=True)
    	self.rect = self.image.get_rect()
    	self.pos = pos
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]

    def getRect(self):
    	return self.rect

    def getPos(self):
    	return [self.x,self.y]

    def setPos(self,pos):
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]

    def moveLeft(self):
        self.setPos([self.getPos()[0] - 5,self.getPos()[1]])

    def moveRight(self):
        self.setPos([self.getPos()[0] + 5,self.getPos()[1]])

    def moveUp(self):
        self.setPos([self.getPos()[0],self.getPos()[1] - 5])

    def moveDown(self):
        self.setPos([self.getPos()[0],self.getPos()[1] + 5])


class Zombie(Enemy):#Hereda de la clase Enemigo
    def __init__(self, img_name, pos):
        Enemy.__init__(self, img_name, pos)

    def update(self):
        if(self.rect.x >= (WIDTH - self.rect[2])):
            self.direccion=1
        if(self.rect.x <= (self.rect[2])):
            self.direccion=0
        if (self.direccion == 0):
            self.rect.x+=5
        else:
            self.rect.x-=5

class Player(pygame.sprite.Sprite): #Hereda de la clase sprite
    def __init__(self, img_name, pos):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = load_image(img_name, curdir, alpha=True)
    	self.rect = self.image.get_rect()
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]
    	self.life = 5
        self.points = 0

    def getRect(self):
    	return self.rect

    def getPos(self):
    	return [self.rect.x,self.rect.y]

    def setPos(self,pos):
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]

    def moveLeft(self):
        increment_x = self.getRect()[2] / 5
        increment_y = self.getRect()[3] / 5
        self.setPos([self.getPos()[0] - increment_x,self.getPos()[1]])

    def moveRight(self):
        increment_x = self.getRect()[2] / 5
        increment_y = self.getRect()[3] / 5
        self.setPos([self.getPos()[0] + increment_x,self.getPos()[1]])

    def moveUp(self):
        increment_x = self.getRect()[2] / 5
        increment_y = self.getRect()[3] / 5
        self.setPos([self.getPos()[0],self.getPos()[1] - increment_y])

    def moveDown(self):
        increment_x = self.getRect()[2] / 5
        increment_y = self.getRect()[3] / 5
        self.setPos([self.getPos()[0],self.getPos()[1] + increment_y])

    def getLife(self):
    	return self.life

    def setLife(self,life):
    	self.life = life

    def crash(self):
        self.setLife(self.getLife() - 1) #quita una vida

class Magician(Player): #Hereda de la clase Player
    def __init__(self, img_name, pos):
        Player.__init__(self, img_name, pos)

class Bullet(pygame.sprite.Sprite): #Hereda de la clase sprite
    def __init__(self, img_name, pos): #img para cargar, y su padre(de donde debe salir la bala)
    	pygame.sprite.Sprite.__init__(self)
    	self.image = load_image(img_name, curdir, alpha=True)
    	self.rect = self.image.get_rect()
    	self.pos = pos
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]
        self.speed = 5

    def getRect(self):
    	return self.rect

    def getPos(self):
    	return [self.rect.x,self.rect.y]

    def setPos(self,pos):
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]

    def update(self):
        self.rect.x += self.speed


def main():

    #----------------------General--------------------------------------------
    pygame.init()
    screen = pygame.display.set_mode([WIDTH,HIGH])
    #background = load_image('images/ground.jpg',curdir, alpha=False)
    #screen.blit(background,[0,0])

    menu_display = pygame.display.set_mode((WIDTH, HIGH))
    background_menu = load_image('images/backgroundm.jpg',curdir,alpha=False)
    background_sound = load_sound('sounds/fondo1.sf',curdir)
    menu_display.blit(background_menu,(0,0))
    background_sound.play()

    ls_all = pygame.sprite.Group() #Se almacenan todos los objetos del juego

    #Creamos los personajes
    '''
    #-----------------Jugador------------------------------------------------
    magician = Magician('images/dere_1.png',[0,0])
    ls_all.add(magician)
    middle = [(WIDTH / 2) - (magician.getRect()[2] / 2), (HIGH / 2) - (magician.getRect()[3] / 2)]
    magician.setPos(middle)

    #----------------ENEMIGOS-------------------------
    #Tener en cuenta a la hora de posicionar los enemigos, que no se choque con ningun otro
    ls_enemies = pygame.sprite.Group()
    for i in range(0,5):
        enemy = Zombie('images/izqenemigo1_1.png',[0,0])
        ls_enemies.add(enemy)
        ls_all.add(enemy)
        enemy.rect.x = random.randrange(WIDTH - 20)
        enemy.rect.y = random.randrange(HIGH - 20)

    #ls_enemies.draw(screen)#posiciona los enemigos

	#----------------BALA-------------------------
	ls_bullet = pygame.sprite.Group()

    '''
    end = False
    while(not end):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                #sys.exit(0)
                end = True
            if event.type == KEYDOWN:
                if event.key == 97 :
                    magician.moveLeft()
                if event.key == 100 :
                    magician.moveRight()
                if event.key == 119 :
                    magician.moveUp()
                if event.key == 115 :
                    magician.moveDown()

        #ls_all.draw(screen)
        pygame.display.flip()
        #screen.blit(background,[0,0])

if __name__ == "__main__":
    main()
