import pygame
import random
import sys
import os
curdir = os.getcwd()+"/sources"

blanco=(255,255,255)
rojo=(255,0,0)
#Algoritmo de Bresenham para la recta
def Bresenhamecta((x0,y0),(x1,y1)):
    dx=x1-x0
    dy=y1-y0
    res=[]
    #Determinar que punto usar para empezar y cual para terminar
    if(dy<0):
        dy=-dy
        stepy=-1
    else:
        stepy=1

    if(dx<0):
        dx=-dx
        stepx=-1
    else:
        stepx=1
    x=x0
    y=y0
    res.append((x,y))
    #Se cicla hasta llegar al final de la linea
    if(dx>dy):
        p=2*dy-dx
        incE=2*dy
        incNE=2*(dy-dx)
        while(x <= x1):
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
        while(y<=y1):
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
        self.jugador = (0,0)
        self.cont=0
        self.mov=0
        self.flag=True
        self.puntos=[]
    def update(self):
            if(self.mov==0):
                if(self.flag):
                    self.puntos=Bresenhamecta((self.rect.x,self.rect.y),self.jugador)
                    self.flag=False
                self.rect.x,self.rect.y=self.puntos[self.cont]
            if(self.cont <= (len(self.puntos)-2)):
                self.cont+=1
            if(self.mov==1):
                self.cont=0
                self.flag=True
                self.mov=0

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
        self.speed = 5
        self.dir=0 #0 derecha , 1 izquierda, 2 arriba, 3 abajo
        self.score=0
    def chocar(self):
        self.vida-=10

def menu(waves,dif,ANCHO,ALTO):
    pygame.init()
    tipo = pygame.font.SysFont("monospace", 13)
    menu_d=pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)
    backgroundm=load_image('backgroundm.jpg',curdir,alpha=False)
    ad1 = tipo.render(("Presiona +/- para manejar las oleadas por nivel" + " Oleadas: " + str(waves)),1, blanco)
    ad2 = tipo.render(("Presiona d/r para manejar la dificultad" + " Dificultad: " + str(dif)),1, blanco)
    ad3 = tipo.render("Escape para salir",1, blanco)
    s_fondo=load_sound('fondo1.sf',curdir)
    s_fondo.play()
    menu_d.blit(backgroundm,(0,0))
    menu_d.blit(ad1, (ANCHO/2-ANCHO/4, ALTO/2))
    menu_d.blit(ad2, (ANCHO/2-ANCHO/4, (ALTO/2)+30))
    menu_d.blit(ad3, (ANCHO/2-ANCHO/4, (ALTO/2)+60))

    pygame.display.flip()

    terminar=False
    max_waves=False
    min_waves=False
    while(not terminar):
        ad1 = tipo.render(("Presiona +/- para manejar las oleadas por nivel" + " Oleadas: " + str(waves)),1, blanco)
        ad2 = tipo.render(("Presiona d/r para manejar la dificultad" + " Dificultad: " + str(dif)),1, blanco)
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.K_SPACE or event.type == pygame.QUIT:
                terminar=True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_PLUS:
                    if(not waves>=10):
                        waves+=1
                if event.key == pygame.K_KP_MINUS:
                    if(not waves<=5):
                        waves-=1
                if event.key == pygame.K_d:
                    if(not dif>=3):
                        dif+=1
                if event.key == pygame.K_r:
                    if(not dif <= 1):
                        dif-=1
                if event.key == pygame.K_ESCAPE:
                    terminar=True


        menu_d.blit(backgroundm,(0,0))
        menu_d.blit(ad1, (ANCHO/2-ANCHO/4, ALTO/2))
        menu_d.blit(ad2, (ANCHO/2-ANCHO/4, (ALTO/2)+30))
        menu_d.blit(ad3, (ANCHO/2-ANCHO/4, (ALTO/2)+60))
        pygame.display.flip()

    s_fondo.stop()
    return waves,dif

def main():
    ANCHO = 800
    ALTO = 600
    """waves=5
    dificultad=1
    waves,dificultad = menu(waves,dificultad,ANCHO,ALTO)"""

    #Inicializacion de pantalla
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pygame.display.set_caption("Magician-zombie v0.1 - Level 1 ", 'Spine Runtime')
    pantalla.fill(blanco)
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
    ls_todos.draw(pantalla)
    ls_enemigos.draw(pantalla)

    pygame.mouse.set_visible(False) #Oculta el puntero del mouse
    pygame.display.flip()
    reloj=pygame.time.Clock()
    terminar=False
    disparo=False
    player_current=0


    while(not terminar):

        events = pygame.event.get()
        posinip=[ANCHO/2,ALTO/2]
        tipo = pygame.font.SysFont("monospace", 15)
        blood = tipo.render(("Vida actual: " + str(jugador.vida)),1, blanco)
        point = tipo.render(("Puntos: " + str(jugador.score)),1, blanco)
        keys = pygame.key.get_pressed()
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
            if keys[pygame.K_a]:
                player_current = (player_current+1)%len(jugador.imagei)
                jugador.image = jugador.imagei[player_current]
                jugador.rect.x-=jugador.speed
                jugador.dir=1
                for e in ls_enemigos:
                    e.mov=1

            if keys[pygame.K_w]:
                player_current = (player_current+1)%len(jugador.imagenar)
                jugador.image = jugador.imagenar[player_current]
                jugador.rect.y-=jugador.speed
                jugador.dir=2
                for e in ls_enemigos:
                    e.mov=1

            if keys[pygame.K_d]:
                player_current = (player_current+1)%len(jugador.imaged)
                jugador.image = jugador.imaged[player_current]
                if(jugador.rect.x+jugador.speed < ANCHO-jugador.rect[2]):
                    jugador.rect.x+=jugador.speed
                jugador.dir=0
                for e in ls_enemigos:
                    e.mov=1

            if keys[pygame.K_s]:
                player_current = (player_current+1)%len(jugador.imagena)
                jugador.image = jugador.imagena[player_current]
                jugador.rect.y+=jugador.speed
                jugador.dir=3
                for e in ls_enemigos:
                    e.mov=1



        pantalla.blit(fondo,posinif)
        ls_todos.draw(pantalla)
        ls_enemigos.draw(pantalla)
        ls_todos.update()
        pygame.display.flip()
        reloj.tick(60)


if __name__ == "__main__":
    main()
