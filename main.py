import pygame
import sys
import os
import random
curdir = os.getcwd()+"/sources" #Para la ruta total del sistema
from pygame.locals import *

HIGH = 400
WIDTH = 700
WHITE = (255,255,255)


def checkCollision(sprite1, sprite2):
    col = pygame.sprite.collide_rect(sprite1, sprite2)
    if col == True:
        return True
    else:
        return False


#Algoritmo de Bresenham para la recta
def Bresenhamrecta((x0,y0),(x1,y1)):
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
    return res
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
        self.jugador = (0,0)
        self.direccion = 0

    def getDir(self):
        return self.direccion

    def setDir(self, dir):
        self.direccion = dir

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
        movimiento = Bresenhamrecta(self.getPos(),self.jugador)

class Player(pygame.sprite.Sprite): #Hereda de la clase sprite
    def __init__(self, img_name, pos):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = load_image(img_name, curdir, alpha=True)
    	self.rect = self.image.get_rect()
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]
    	self.life = 5
        self.score = 0
        self.dir = 0 #0 derecha , 1 izquierda, 2 arriba, 3 abajo
        #imagenes para movimiento
        self.imaged = [] #derecha
        self.imagei = [] #izquierda
        self.imagenar = [] #arriba
        self.imagena = [] #abajo
        self.enemigos=0

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score += score

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
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(x - increment_x >= 0):
            self.setPos([x - increment_x,y])

    def moveRight(self):
        increment_x = self.getRect()[2] / 5
        increment_y = self.getRect()[3] / 5
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(x + increment_x < WIDTH - self.rect[2]):
            self.setPos([x + increment_x,y])

    def moveUp(self):
        increment_x = self.getRect()[2] / 5
        increment_y = self.getRect()[3] / 5
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(y + increment_y >= 0):
            self.setPos([x,y - increment_y])

    def moveDown(self):
        increment_x = self.getRect()[2] / 5
        increment_y = self.getRect()[3] / 5
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(y + increment_y < HIGH - self.rect[3]): # si no se pasa de la pantalla
            self.setPos([x,y + increment_y])

    def getLife(self):
    	return self.life

    def setLife(self,life):
    	self.life = life

    def crash(self):
        self.setLife(self.getLife() - 1) #quita una vida

    def getDir(self):
        return self.dir

    def setDir(self,dir):
        self.dir = dir

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
        self.magiciandir = 0 #dispara dependiendo de la posicion del magician

    def getRect(self):
    	return self.rect

    def getPos(self):
    	return [self.rect.x,self.rect.y]

    def setPos(self,pos):
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]

    def setDir(self,dir):#modifica la direccion del magician
        self.magiciandir = dir

    def getDir(self):
        return self.magiciandir

    def update(self):
        if(self.magiciandir == 0):
            self.rect.x += self.speed
        elif 1:
            if(self.magiciandir == 1):
                self.rect.x -= self.speed
            elif 1:
                if(self.magiciandir==2):
                    self.rect.y -= self.speed
                elif 1:
                    if(self.magiciandir==3):
                        self.rect.y += self.speed

def initGame():
    #por defecto:
    ANCHO = 800
    ALTO = 600
    waves = 5
    dif = 1

    pygame.init()
    tipo = pygame.font.SysFont("monospace", 13)
    menu_d = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)

    #imagen de fondo
    backgroundm = load_image('images/backgroundm.jpg',curdir,alpha = False)
    menu_d.blit(backgroundm,(0,0))

    #sonido de fondo
    s_fondo = load_sound('sounds/fondo1.sf',curdir)
    s_fondo.play()

    #--------------------opciones del juego------------------------------
    ad1 = tipo.render(("Presiona +/- para manejar las oleadas por nivel" + " Oleadas: " + str(waves)),1, WHITE)
    ad2 = tipo.render(("Presiona d/r para manejar la dificultad" + " Dificultad: " + str(dif)),1, WHITE)
    ad3 = tipo.render("Escape para salir",1, WHITE)

    #los posiciona
    menu_d.blit(ad1, (ANCHO/2-ANCHO/4, ALTO/2))
    menu_d.blit(ad2, (ANCHO/2-ANCHO/4, (ALTO/2)+30))
    menu_d.blit(ad3, (ANCHO/2-ANCHO/4, (ALTO/2)+60))

    #------------------------------------------------------------------------
    pygame.display.flip()

    terminar = False
    max_waves = False
    min_waves = False

    while(not terminar):

        ad1 = tipo.render(("Presiona +/- para manejar las oleadas por nivel" + " Oleadas: " + str(waves)),1, WHITE)
        ad2 = tipo.render(("Presiona d/r para manejar la dificultad" + " Dificultad: " + str(dif)),1, WHITE)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                terminar = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_PLUS: # +
                    if(not waves >= 10):
                        waves += 1
                if event.key == pygame.K_KP_MINUS: # -
                    if(not waves <= 5):
                        waves -= 1
                if event.key == pygame.K_d:
                    if(not dif >= 3):
                        dif += 1
                if event.key == pygame.K_r:
                    if(not dif <= 1):
                        dif -= 1
                if event.key == pygame.K_ESCAPE:
                    terminar = True


        menu_d.blit(backgroundm,(0,0))
        menu_d.blit(ad1, (ANCHO/2-ANCHO/4, ALTO/2))
        menu_d.blit(ad2, (ANCHO/2-ANCHO/4, (ALTO/2)+30))
        menu_d.blit(ad3, (ANCHO/2-ANCHO/4, (ALTO/2)+60))
        pygame.display.flip()

    s_fondo.stop()
    return waves,dif #retorna lo que escoge el usuario

def main():

    #------------------------Inicia el menu del juego----------------------
    #waves,dificultad = initGame()

    #----------------------General--------------------------------------------
    pygame.init()
    screen = pygame.display.set_mode([WIDTH,HIGH])
    background = load_image('images/background.jpg',curdir, alpha = False)
    #screen.blit(background,[0,0])
    pygame.display.set_caption("Magician-zombie v0.1 - Level 1 ", 'Spine Runtime')#nombre ventana

    #Grupos de sprites
    ls_todos = pygame.sprite.Group()
    ls_balaj = pygame.sprite.Group()
    ls_enemigos = pygame.sprite.Group()
    ls_balase = pygame.sprite.Group()
    ls_magicianes = pygame.sprite.Group()
    ls_choque= pygame.sprite.Group()
    #Creamos los personajes

    #-----------------magician------------------------------------------------
    magician = Magician('images/dere_1.png',[0,0])
    middle = [(WIDTH / 2) - (magician.getRect()[2] / 2), (HIGH / 2) - (magician.getRect()[3] / 2)]
    magician.setPos(middle) #posiciona el magician en la mitad de la pantalla

    #Agrega las imagenes del magician
    magician.imaged.append(load_image('images/dere_1.png',curdir,alpha=True))
    magician.imaged.append(load_image('images/dere_2.png',curdir,alpha=True))
    magician.imagenar.append(load_image('images/up_1.png',curdir,alpha=True))
    magician.imagenar.append(load_image('images/up_2.png',curdir,alpha=True))
    magician.imagei.append(load_image('images/iz_1.png',curdir,alpha=True))
    magician.imagei.append(load_image('images/iz_2.png',curdir,alpha=True))
    magician.imagena.append(load_image('images/ab_1.png',curdir,alpha=True))
    magician.imagena.append(load_image('images/ab_2.png',curdir,alpha=True))

    ls_todos.add(magician)
    ls_magicianes.add(magician)

    #----------------ENEMIGOS-------------------------
    #Tener en cuenta a la hora de posicionar los enemigos, que no se choque con ningun otro
    ls_enemies = pygame.sprite.Group()
    for i in range(0,5):
        enemy = Zombie('images/izqenemigo1_1.png',[0,0])
        ls_enemigos.add(enemy)
        ls_todos.add(enemy)
        enemy.setPos([random.randrange(WIDTH - 20),random.randrange(HIGH - 20)])

    screen.blit(background,[0,0])
    ls_todos.draw(screen)
    ls_enemigos.draw(screen)

    pygame.display.flip()
    reloj = pygame.time.Clock()
    terminar = False
    disparo = False
    player_current = 0
    cont=0
    flag=False
    while(not terminar):
        events = pygame.event.get()

        tipo = pygame.font.SysFont("monospace", 15)
        blood = tipo.render(("Vida actual: " + str(magician.getLife())),1, (0,0,0))
        point = tipo.render(("Puntos: " + str(magician.getScore())),1, (0,0,0))
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type  == pygame.QUIT:
                terminar=True
            if keys[pygame.K_SPACE]:
                bala = Bullet('images/bala.png',magician.getPos())
                bala.setDir(magician.getDir())
                bala.setPos([magician.getPos()[0] + 10 , magician.getPos()[1] + 10])
                ls_balaj.add(bala)
                ls_todos.add(bala)
                disparo = True


        if keys[pygame.K_a]:
            player_current = (player_current+1)%len(magician.imagei)
            magician.image = magician.imagei[player_current]
            magician.moveLeft()
            magician.setDir(1)


        if keys[pygame.K_w]:
            player_current = (player_current+1)%len(magician.imagenar)
            magician.image = magician.imagenar[player_current]
            magician.moveUp()
            magician.setDir(2)

        if keys[pygame.K_d]:
            player_current = (player_current+1)%len(magician.imaged)
            magician.image = magician.imaged[player_current]
            magician.moveRight()
            magician.setDir(0)

        if keys[pygame.K_s]:
            player_current = (player_current+1)%len(magician.imagena)
            magician.image = magician.imagena[player_current]
            magician.moveDown()
            magician.setDir(3)

        if keys[pygame.K_ESCAPE]:
            terminar = True


        screen.blit(background,[0,0])
        screen.blit(blood,[0,10])
        screen.blit(point,[0,25])
        ls_todos.draw(screen)
        ls_enemigos.draw(screen)
        ls_todos.update()
        pygame.display.flip()
        reloj.tick(60)
        magician.enemigos=len(ls_enemigos)

        for enemigo in ls_enemigos:
            if(checkCollision(magician,enemigo)): # si se choco
                if(cont == 0):
                    magician.crash()
                    print magician.getLife()
                    flag=True
        if(flag):
            cont+=1
        if(cont >= 8):
            cont=0

        for b in ls_balaj:
			ls_impactos = pygame.sprite.spritecollide(b, ls_enemigos, True)
			for impacto in ls_impactos:
				ls_balaj.remove(b)
				ls_todos.remove(b)
				magician.setScore(1)


        for enemigo in ls_enemigos:
            e.jugador = magician.getPos()

        magician.mov=0


if __name__ == "__main__":
    main()
