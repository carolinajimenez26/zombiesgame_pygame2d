from func import *


class Enemy(pygame.sprite.Sprite): #Hereda de la clase sprite
    def __init__(self, img_name, pos, w, h):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = load_image(img_name, curdir, alpha=True)
    	self.rect = self.image.get_rect()
    	self.pos = pos
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]
        self.jugador = (0,0)
        self.direccion = 0
        self.WIDTH = w
        self.HIGH = h

    def getDir(self):
        return self.direccion

    def setDir(self, dir):
        self.direccion = dir

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
            self.dir = 1

    def moveRight(self):
        increment_x = self.getRect()[2] / 5
        increment_y = self.getRect()[3] / 5
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(x + increment_x < self.WIDHT - self.rect[2]):
            self.setPos([x + increment_x,y])
            self.dir = 0

    def moveUp(self):
        increment_x = self.getRect()[2] / 5
        increment_y = self.getRect()[3] / 5
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(y + increment_y >= 0):
            self.setPos([x,y - increment_y])
            self.dir = 2

    def moveDown(self):
        increment_x = self.getRect()[2] / 5
        increment_y = self.getRect()[3] / 5
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(y + increment_y < self.HIGH - self.rect[3]): # si no se pasa de la pantalla
            self.setPos([x,y + increment_y])
            self.dir = 3



class Zombie(Enemy):#Hereda de la clase Enemigo
    def __init__(self, img_name, pos, w, h):
        Enemy.__init__(self, img_name, pos, w, h)

    def move(self, pos): #recibe la posicion actual del jugador
        print "move"
        moves = Bresenhamrecta([self.getPos(),pos],self)
        for i in range(0,len(moves)):
            self.setPos(moves[i])
            print (moves[i])
            pygame.display.flip()
            #self.moveLeft()
        print "end"

    def update(self):
        pass

class Player(pygame.sprite.Sprite): #Hereda de la clase sprite
    def __init__(self, img_name, pos,w, h):
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
        self.WIDTH = w
        self.HIGH = h

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
            self.dir = 1

    def moveRight(self):
        increment_x = self.getRect()[2] / 5
        increment_y = self.getRect()[3] / 5
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(x + increment_x < self.WIDTH - self.rect[2]):
            self.setPos([x + increment_x,y])
            self.dir = 0

    def moveUp(self):
        increment_x = self.getRect()[2] / 5
        increment_y = self.getRect()[3] / 5
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(y + increment_y >= 0):
            self.setPos([x,y - increment_y])
            self.dir = 2

    def moveDown(self):
        increment_x = self.getRect()[2] / 5
        increment_y = self.getRect()[3] / 5
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(y + increment_y < self.HIGH - self.rect[3]): # si no se pasa de la pantalla
            self.setPos([x,y + increment_y])
            self.dir = 3

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
    def __init__(self, img_name, pos, w, h):
        Player.__init__(self, img_name, pos, w, h)

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

    def setDir(self,dir):
        self.magiciandir = dir

    def getDir(self):
        return self.magiciandir

    def update(self):
        if(self.magiciandir == 0): #derecha
            self.rect.x += self.speed
        if(self.magiciandir == 1):#izquierda
            self.rect.x -= self.speed
        if(self.magiciandir == 2):#arriba
            self.rect.y -= self.speed
        if(self.magiciandir == 3):#abajo
            self.rect.y += self.speed


def game(ANCHO,ALTO):

    #Inicializacion de pantalla
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    pygame.display.set_caption("Magician-zombie v0.1 - Level 1 ", 'Spine Runtime')
    tipo = pygame.font.SysFont("monospace", 15)
    pantalla.fill((0,0,0))


    #Fin de inicializacion de pantalla

    #Cargando imagenes
    posinif=[0,0]

    #Grupos de sprites
    ls_todos=pygame.sprite.Group()
    ls_balaj=pygame.sprite.Group()
    ls_enemigos=pygame.sprite.Group()
    ls_balase=pygame.sprite.Group()
    ls_jugadores=pygame.sprite.Group()

    #Creamos los personajes

    #-----------------magician------------------------------------------------
    magician = Magician('dere_1.png',[0,0], ANCHO, ALTO)
    middle = [(ANCHO / 2) - (magician.getRect()[2] / 2), (ALTO / 2) - (magician.getRect()[3] / 2)]
    magician.setPos(middle) #posiciona el magician en la mitad de la pantalla

    #Agrega las imagenes del magician
    magician.imaged.append(load_image('dere_1.png',curdir,alpha=True))
    magician.imaged.append(load_image('dere_2.png',curdir,alpha=True))
    magician.imagenar.append(load_image('up_1.png',curdir,alpha=True))
    magician.imagenar.append(load_image('up_2.png',curdir,alpha=True))
    magician.imagei.append(load_image('iz_1.png',curdir,alpha=True))
    magician.imagei.append(load_image('iz_2.png',curdir,alpha=True))
    magician.imagena.append(load_image('ab_1.png',curdir,alpha=True))
    magician.imagena.append(load_image('ab_2.png',curdir,alpha=True))

    ls_todos.add(magician)
    ls_jugadores.add(magician)

    #----------------ENEMIGOS-------------------------
    #Tener en cuenta a la hora de posicionar los enemigos, que no se choque con ningun otro
    for i in range(0,5):
        enemy = Zombie('izqenemigo1_1.png',[0,0], ANCHO, ALTO)
        ls_enemigos.add(enemy)
        ls_todos.add(enemy)
        enemy.setPos([random.randrange(ANCHO - 20),random.randrange(ALTO - 20)])


    fondo = load_image('background.jpg',curdir, alpha=False)

    pantalla.blit(fondo,posinif)
    splash = False
    ls_todos.draw(pantalla)
    ls_enemigos.draw(pantalla)

    pygame.mouse.set_visible(False) #Oculta el puntero del mouse
    pygame.display.flip()
    reloj = pygame.time.Clock()
    terminar = False
    disparo = False
    player_current = 0
    flag = False
    cont = 0

    while(not terminar):

        events = pygame.event.get()

        tipo = pygame.font.SysFont("monospace", 15)
        blood = tipo.render(("Vida actual: " + str(magician.getLife())),1, (0,0,0))
        point = tipo.render(("Puntos: " + str(magician.getScore())),1, (0,0,0))
        keys = pygame.key.get_pressed()

        for event in events:

            if event.type  == pygame.QUIT:
                terminar=True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    bala = Bullet('bala.png',magician.getPos())#la posicion inicial depende de objeto que este disparando
                    dir = magician.getDir()
                    bala.setDir(dir)

                    if(dir == 0):#derecha
                        bala.setPos([magician.getPos()[0] + magician.getRect()[2]/2,magician.getPos()[1]])
                    if(dir == 1):#izquierda
                        bala.setPos([magician.getPos()[0] - magician.getRect()[2]/2,magician.getPos()[1]])
                    if(dir == 2):#arriba
                        bala.setPos([magician.getPos()[0],magician.getPos()[1] - magician.getRect()[3]])
                    if(dir == 3):#abajo
                        bala.setPos([magician.getPos()[0],magician.getPos()[1] + magician.getRect()[3]])

                    ls_balaj.add(bala)
                    ls_todos.add(bala)
                    disparo = True


        if keys[pygame.K_a]:
            player_current = (player_current+1)%len(magician.imagei)
            magician.image = magician.imagei[player_current]
            magician.moveLeft()
            magician.setDir(1)

            for e in ls_enemigos:
                #e.move(magician.getPos()) #se mueve hacia el jugador
                e.moveLeft()

        if keys[pygame.K_w]:
            player_current = (player_current+1)%len(magician.imagenar)
            magician.image = magician.imagenar[player_current]
            magician.moveUp()
            magician.setDir(2)

            for e in ls_enemigos:
                #e.move(magician.getPos()) #se mueve hacia el jugador
                e.moveLeft()

        if keys[pygame.K_d]:
            player_current = (player_current+1)%len(magician.imaged)
            magician.image = magician.imaged[player_current]
            magician.moveRight()
            magician.setDir(0)

            for e in ls_enemigos:
                #e.move(magician.getPos()) #se mueve hacia el jugador
                e.moveLeft()

        if keys[pygame.K_s]:
            player_current = (player_current+1)%len(magician.imagena)
            magician.image = magician.imagena[player_current]
            magician.moveDown()
            magician.setDir(3)

            for e in ls_enemigos:
                #e.move(magician.getPos()) #se mueve hacia el jugador
                e.moveLeft()

        if keys[pygame.K_ESCAPE]:
            terminar = True


        pantalla.blit(fondo,[0,0])
        pantalla.blit(blood,[0,10])
        pantalla.blit(point,[0,25])
        ls_todos.draw(pantalla)
        ls_enemigos.draw(pantalla)
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
                    if(magician.getLife() == 0): #vuelve al menu ppal
                        terminar = True
        if(flag):
            cont+=1
        if(cont >= 8):
            cont=0
        #lista de balas
        for b in ls_balaj:
			ls_impactos = pygame.sprite.spritecollide(b, ls_enemigos, True)
			for impacto in ls_impactos:
				ls_balaj.remove(b)
				ls_todos.remove(b)
				magician.setScore(1)


        for enemigo in ls_enemigos:
            enemigo.jugador = magician.getPos()

        magician.mov=0

    return 0

if __name__ == "__main__":
    main()
