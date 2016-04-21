import pygame
import sys
import os
import random
curdir = os.getcwd() #Para la ruta total del sistema
from pygame.locals import *

HIGH = 400
WIDTH = 700
WHITE = (255,255,255)

'''Teclas de juego:
        A = 97 (izq)
        D = 100 (der)
        W = 119 (Arriba)
        S = 115 (Abajo)
'''

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

class Player(pygame.sprite.Sprite): #Hereda de la clase sprite
    def __init__(self, img_name, pos):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = load_image(img_name, curdir, alpha=True)
    	self.rect = self.image.get_rect()
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]
    	self.life = 5

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

	def getRect(self):
		return self.rect

	def getPos(self):
		return [self.rect.x,self.rect.y]

	def setPos(self,pos):
		self.rect.x = pos[0]
		self.rect.y = pos[1]

	def update(self):
		pass #el disparo depende de hacia donde este mirando el muneco


def main():

    #----------------------General--------------------------------------------
    pygame.init()
    screen = pygame.display.set_mode([WIDTH,HIGH])
    background = load_image('sprites/ground.jpg',curdir, alpha=False)
    screen.blit(background,[0,0])

    ls_all = pygame.sprite.Group() #Se almacenan todos los objetos del juego

    #Creamos los personajes

    #-----------------Jugador------------------------------------------------
    magician = Magician('sprites/P1.png',[0,0])
    ls_all.add(magician)
    middle = [(WIDTH / 2) - (magician.getRect()[2] / 2), (HIGH / 2) - (magician.getRect()[3] / 2)]
    magician.setPos(middle)

    #----------------ENEMIGOS-------------------------
    #Tener en cuenta a la hora de posicionar los enemigos, que no se choque con ningun otro
    ls_enemies = pygame.sprite.Group()
    for i in range(0,5):
        enemy = Zombie('sprites/zombie_izq.png',[0,0])
        ls_enemies.add(enemy)
        ls_all.add(enemy)
        enemy.rect.x = random.randrange(WIDTH - 20)
        enemy.rect.y = random.randrange(HIGH - 20)

    #ls_enemies.draw(screen)#posiciona los enemigos

	#----------------BALA-------------------------
	ls_bullet = pygame.sprite.Group()


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

        ls_all.draw(screen)
        pygame.display.flip()
        screen.blit(background,[0,0])

if __name__ == "__main__":
    main()
