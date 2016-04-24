import pygame
import random
import time
import sys
import os

curdir = os.getcwd()+"/sources"

blanco=(255,255,255)
rojo=(255,0,0)

def checkCollision(sprite1, sprite2):
    col = pygame.sprite.collide_rect(sprite1, sprite2)
    if col == True:
        return True
    else:
        return False

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

#Funcion para determianr si el usuario tiene el mouse encima de lso botones
def pres_boton(button_x,button_y,sprite):
    x_len = sprite.get_width()
    y_len = sprite.get_height()
    mos_x, mos_y = pygame.mouse.get_pos()
    if mos_x>button_x and (mos_x<button_x+x_len):
        x_inside = True
    else:
        x_inside = False
    if mos_y>button_y and (mos_y<button_y+y_len):
        y_inside = True
    else:
        y_inside = False
    if x_inside and y_inside:
        return True
    else:
        return False

#FIn funcion para
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


def menu(ANCHO,ALTO):
    pygame.init()

    menu_d=pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)
    backgroundm=load_image('backgroundm.jpg',curdir,alpha=False)
    ad1 = load_image('btn1.png', curdir, alpha=False)
    ad2 = load_image('btn3.png', curdir, alpha=False)
    ad3 = load_image('btn2.png', curdir, alpha=False)
    s_fondo=load_sound('fondo1.sf',curdir)
    s_fondo.play()
    rect = ad1.get_rect()
    button_x = ANCHO/2-50
    button_y = ALTO/2
    rect2 = ad2.get_rect()
    menu_d.blit(backgroundm,(0,0))
    menu_d.blit(ad1, (ANCHO/2, ALTO/2))
    menu_d.blit(ad2, (ANCHO/2, (ALTO/2)+50))
    menu_d.blit(ad3, (ANCHO/2, (ALTO/2)+100))

    pygame.display.flip()

    terminar=False


    while(not terminar):
        ad1 = load_image('btn1.png', curdir, alpha=False)
        ad2 = load_image('btn3.png', curdir, alpha=False)
        ad3 = load_image('btn2.png', curdir, alpha=False)
        # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
        tipo_t = pygame.font.SysFont("comicsansms", 30)
        # render text
        text_sup = tipo_t.render("Magician-Zombie v0.1 - [Juan Diego H - Carolina J]", 1, (255,255,255))

        mouse_pos=pygame.mouse.get_pos()
        events = pygame.event.get()

        if(pres_boton(ANCHO/2,ALTO/2,ad1)):
            ad1 = load_image('btn1_p.png', curdir, alpha=False)

        if(pres_boton(ANCHO/2,(ALTO/2)+50,ad2)):
            ad2 = load_image('btn3_p.png', curdir, alpha=False)

        if(pres_boton(ANCHO/2,(ALTO/2)+100,ad3)):
            ad3 = load_image('btn2_p.png', curdir, alpha=False)


        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                if(pres_boton(ANCHO/2,ALTO/2,ad1)):
                    terminar=True
                if(pres_boton(ANCHO/2,ALTO/2+50,ad2)):
                    sys.exit()
                if(pres_boton(ANCHO/2,ALTO/2+100,ad3)):
                    print "Creditos"

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()




        menu_d.blit(backgroundm,(0,0))
        menu_d.blit(text_sup, (ANCHO/2-180, 30))
        menu_d.blit(ad1, (ANCHO/2-50, ALTO/2))
        menu_d.blit(ad2, (ANCHO/2-50, (ALTO/2)+50))
        menu_d.blit(ad3, (ANCHO/2-50, (ALTO/2)+100))
        pygame.display.flip()

    s_fondo.stop()

def main():
    ANCHO = 800
    ALTO = 600
    menu(ANCHO,ALTO)

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
