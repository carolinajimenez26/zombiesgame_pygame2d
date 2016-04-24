from func import *

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(imagen,curdir,alpha=True)
        self.rect = self.image.get_rect()
        self.direccion=0
        self.jugador = (0,0)
        self.cont=0
        self.puntos=[]
    #def update(self):



class Boss(Enemigo):
    def __init__(self,imagen):
        Enemigo.__init__(self, imagen)




class Bala(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(imagen,curdir,alpha=True)
        self.rect = self.image.get_rect()
        self.velocidad=5
        self.jugadordir=0
    def update(self):
        if(self.jugadordir==0):
            self.rect.x+=self.velocidad
        elif 1:
            if(self.jugadordir==1):
                self.rect.x-=self.velocidad
            elif 1:
                if(self.jugadordir==2):
                    self.rect.y-=self.velocidad
                elif 1:
                    if(self.jugadordir==3):
                        self.rect.y+=self.velocidad


class Jugador(pygame.sprite.Sprite):

    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(imagen,curdir,alpha=True)
        self.imaged = []
        self.imagei = []
        self.imagenar = []
        self.imagena = []
        self.rect = self.image.get_rect()
        self.vida = 100
        self.speed = 1
        self.score = 0
        self.dir=0 #0 derecha , 1 izquierda, 2 arriba, 3 abajo
        self.score=0
        self.ventana=(0,0)
        self.enemigos=None
    def chocar(self):
        self.vida-=10
    def movderecha(self):
        for ene in self.enemigos:
            ls_impactos = pygame.sprite.spritecollide(self, self.enemigos, False)
            if(not(len(ls_impactos) != 0)):
                if(self.rect.x+self.speed < self.ventana[0]-self.rect[2]):
                    #time.sleep(0.01)
                    self.rect.x+=self.speed
                else:
                    self.rect.x-=self.speed
    def movizquierda(self):
        for ene in self.enemigos:
            ls_impactos = pygame.sprite.spritecollide(self, self.enemigos, False)
            if(not(len(ls_impactos) != 0)):
                if(self.rect.x+self.speed > (0)):
                    #time.sleep(0.01)
                    self.rect.x-=self.speed
            else:
                self.rect.x+=self.speed

    def movarriba(self):
        for ene in self.enemigos:
            ls_impactos = pygame.sprite.spritecollide(self, self.enemigos, False)
            if(not(len(ls_impactos) != 0)):
                if(self.rect.y+self.speed > (0)):
                    #time.sleep(0.01)
                    self.rect.y-=self.speed
            else:
                self.rect.y+=self.speed
    def movabajo(self):
        for ene in self.enemigos:
            ls_impactos = pygame.sprite.spritecollide(self, self.enemigos, False)
            if(not(len(ls_impactos) != 0)):
                if(self.rect.y+self.speed < (self.ventana[1]-self.rect[3])):
                    #time.sleep(0.01)
                    self.rect.y+=self.speed
            else:
                self.rect.y-=self.speed

def game(ANCHO,ALTO):

    #Inicializacion de pantalla
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
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

    jugador=Jugador('dere_1.png')
    jugador.rect.x=ANCHO/2
    jugador.rect.y=ALTO/2
    jugador.ventana=(ANCHO,ALTO)
    jugador.imaged.append(load_image('dere_1.png',curdir,alpha=True))
    jugador.imaged.append(load_image('dere_2.png',curdir,alpha=True))
    jugador.imagenar.append(load_image('up_1.png',curdir,alpha=True))
    jugador.imagenar.append(load_image('up_2.png',curdir,alpha=True))
    jugador.imagei.append(load_image('iz_1.png',curdir,alpha=True))
    jugador.imagei.append(load_image('iz_2.png',curdir,alpha=True))
    jugador.imagena.append(load_image('ab_1.png',curdir,alpha=True))
    jugador.imagena.append(load_image('ab_2.png',curdir,alpha=True))
    ls_todos.add(jugador)
    ls_jugadores.add(jugador)

    for i in range(0,5):
        ene = Enemigo('ene.png')
        ene.rect.x,ene.rect.y = random.randrange(ANCHO - 20),random.randrange(ALTO - 20)
        ene.jugador = (jugador.rect.x,jugador.rect.y)
        ls_enemigos.add(ene)
        ls_todos.add(ene)


    fondo=load_image('background.jpg',curdir, alpha=False)

    pantalla.blit(fondo,posinif)
    splash = False
    ls_todos.draw(pantalla)
    ls_enemigos.draw(pantalla)

    pygame.mouse.set_visible(False) #Oculta el puntero del mouse
    pygame.display.flip()
    reloj=pygame.time.Clock()
    terminar=False
    disparo=False
    player_current=0
    flag=False
    cont=0
    while(not terminar):

        events = pygame.event.get()
        posinip=[ANCHO/2,ALTO/2]
        tipo = pygame.font.SysFont("monospace", 15)
        blood = tipo.render(("Vida actual: " + str(jugador.vida)),1, (255,0,0))
        point = tipo.render(("Puntos: " + str(jugador.score)),1, (255,0,0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_current = (player_current+1)%len(jugador.imagei)
            jugador.image = jugador.imagei[player_current]
            jugador.enemigos=ls_enemigos
            jugador.movizquierda()
            jugador.dir=1


        if keys[pygame.K_w]:
            player_current = (player_current+1)%len(jugador.imagenar)
            jugador.image = jugador.imagenar[player_current]
            jugador.enemigos=ls_enemigos
            jugador.movarriba()
            jugador.dir=2


        if keys[pygame.K_d]:
            player_current = (player_current+1)%len(jugador.imaged)
            jugador.image = jugador.imaged[player_current]
            jugador.enemigos=ls_enemigos
            jugador.movderecha()
            jugador.dir=0


        if keys[pygame.K_s]:
            player_current = (player_current+1)%len(jugador.imagena)
            jugador.image = jugador.imagena[player_current]
            jugador.enemigos=ls_enemigos
            jugador.movabajo()
            jugador.dir=3

        for event in events:
            if event.type  == pygame.QUIT:
                terminar=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bala = Bala('bala.png')
                    bala.jugadordir=jugador.dir
                    bala.rect.x=jugador.rect.x+10
                    bala.rect.y=jugador.rect.y+10
                    ls_balaj.add(bala)
                    ls_todos.add(bala)
                    disparo=True

                if event.key == pygame.K_ESCAPE:
                    terminar=True

        for enemigo in ls_enemigos:
            if(checkCollision(jugador,enemigo)): # si se choco
                if(cont == 0):
                    jugador.chocar()
                    print jugador.vida
                    flag=True
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
				jugador.score+=1

        pantalla.blit(fondo,posinif)
        pantalla.blit(blood,(0,10))
        pantalla.blit(point,(0,20))
        ls_todos.draw(pantalla)
        ls_enemigos.draw(pantalla)
        ls_todos.update()
        pygame.display.flip()
        reloj.tick(60)
        
if __name__ == "__main__":
    main()
