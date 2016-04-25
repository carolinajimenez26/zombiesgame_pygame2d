from objects import *
from loser import game_over

class Vampire(pygame.sprite.Sprite): #Hereda de la clase sprite
    def __init__(self, img_name, table):
    	pygame.sprite.Sprite.__init__(self)
        self.table= table
        self.image = load_image(img_name, curdir, alpha=True)
    	self.rect = self.image.get_rect()
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]
        self.jugador = (0,0)
        self.direccion = 0
        self.display = (0,0)
        self.vida=0

    def getDir(self):
        return self.direccion

    def setImgInit():
        self.image = self.table[0][0]

    def setDir(self, dir):
        self.direccion = dir

    def setVida(vida):
        self.vida=vida

    def getRect(self):
    	return self.rect

    def getPos(self):
    	return [self.rect.x,self.rect.y]

    def setPos(self,pos):
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]

    def getMargen(self):
        return (self.rect[2],self.rect[3])

class Boss(Vampire):
    def __init__(self, img_name):
        Vampire.__init__(self, img_name)

def level2(ANCHO,ALTO):
    #Inicializacion de pantalla
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO + 50])
    pygame.display.set_caption("Magician-zombie v0.1 - Level 1 ", 'Spine Runtime')
    tipo = pygame.font.SysFont("monospace", 15)
    pantalla.fill((0,0,0))
    #Fin de inicializacion de pantalla

    #Cargando imagenes
    posinif = [0,0]

    #Grupos de sprites
    ls_todos = pygame.sprite.Group()
    #GRUPOS PERTENECIENTES A EL JUGADOR
    ls_jugadores = pygame.sprite.Group()
    ls_balaj = pygame.sprite.Group()
    #GRUPO PERTENECIENTES A LOS ENEMIGOS
    ls_enemigos = pygame.sprite.Group()
    ls_balase = pygame.sprite.Group()

    #Creamos los personajes

    #-----------------magician------------------------------------------------
    magician = Magician('dere_1.png',[0,0], ANCHO, ALTO - 50)
    (Margen_x,Margen_y)=magician.getMargen()
    middle = [0+Margen_x, (ALTO / 2) - (magician.getRect()[3] / 2)]
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

    #Creamos el jefe 26 x 33 or 32 x 48
    table= cargar_fondo(curdir + "/images/" + 'boss.png', 26, 33)
    boss = Boss('ab_1.png',table)
    (BMargen_x,BMargen_y)=boss.getMargen()
    boss.setPos((ANCHO-BMargen_x,(ALTO / 2) - (BMargen_y / 2)))
    boss.setVida(1000)

    fondo = load_image('background.jpg',curdir, alpha=False)
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO+10))
    pantalla.fill(blanco)
    pantalla.blit(fondo,posinif)

    while(not terminar):
        if(magician.getLife() <= 0): #vuelve al menu ppal
            #pygame.display.quit()
            game_over(ANCHO,ALTO)
            terminar=True
            print "yiyi"
        events = pygame.event.get()
        tipo = pygame.font.SysFont("monospace", 15)
        blood = tipo.render("Vida actual: " ,1, (255,0,0))
        pantalla.blit(blood, (0, ALTO))
        if(magician.getLife() > 0):
            point = tipo.render(("Puntos: " + str(magician.getScore())),1, (255,0,0))
        pantalla.fill(pygame.Color(0,0,0))

        keys = pygame.key.get_pressed()

        for event in events:

            if event.type  == pygame.QUIT:
                terminar = True

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

level2(800,600)
