from imports import *

class Enemy(pygame.sprite.Sprite): #Hereda de la clase sprite
    #cargar_fondo('zombie1.png',ancho,alto)
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
        if(y + increment_y >= 10):
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

    def getMargen(self):
        return (self.rect[2],self.rect[3])

class Boss(Enemy):
    def __init__(self, img_name,table,pos,w,h):
        Enemy.__init__(self, img_name,pos,w,h)
        self.table = table
        self.life = 1000
        self.speed = 5

    def getLife(self):
    	return self.life

    def setLife(self,life):
    	self.life = life

    def getSpeed(self):
        return self.speed

    def restartMovements(self,pos):#calcula el camino por donde debe moverse (recibe el punto final)
        self.moves = Bresenhamrecta([self.getPos(),pos])#carga los nuevos movimientos
        self.i = 0 #debe empezar a recorrerla desde cero

    def update(self): #se mueve
        if(self.i < len(self.moves)):
            self.setPos(self.moves[self.i])
            self.i += 1 #para que recorra el siguiente

class Vampire(Enemy):
    def __init__(self, img_name,table,pos,w,h):
        Enemy.__init__(self, img_name,pos,w,h)
        self.table = table
        self.life = 5
        self.speed = 5

    def getLife(self):
    	return self.life

    def setLife(self,life):
    	self.life = life

    def getSpeed(self):
        return self.speed

    def restartMovements(self,pos):#calcula el camino por donde debe moverse (recibe el punto final)
        self.moves = Bresenhamrecta([self.getPos(),pos])#carga los nuevos movimientos
        self.i = 0 #debe empezar a recorrerla desde cero

    def update(self): #se mueve
        if(self.i < len(self.moves)):
            self.setPos(self.moves[self.i])
            self.i += 1 #para que recorra el siguiente

class Zombie(Enemy):#Hereda de la clase Enemigo
    def __init__(self, img_name, pos, w, h):
        Enemy.__init__(self, img_name, pos, w, h)
        self.moves = [0 for x in range(w*h)] #movimientos que debe realizar
        self.i = 0

    def restartMovements(self,pos):#calcula el camino por donde debe moverse (recibe el punto final)
        self.moves = Bresenhamrecta([self.getPos(),pos])#carga los nuevos movimientos
        self.i = 0 #debe empezar a recorrerla desde cero

    def update(self): #se mueve
        if(self.i < len(self.moves)):
            self.setPos(self.moves[self.i])
            self.i += 1 #para que recorra el siguiente

class Player(pygame.sprite.Sprite): #Hereda de la clase sprite
    def __init__(self, img_name, pos,w, h):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = load_image(img_name, curdir, alpha=True)
    	self.rect = self.image.get_rect()
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]
    	self.life = 100
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
        #speed
        self.increment_x = self.getRect()[2] / 5
        self.increment_y = self.getRect()[3] / 5

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score += score

    def setSpeed(self, speed):
        self.increment_x = speed[0]
        self.increment_y = speed[1]

    def getRect(self):
    	return self.rect

    def getPos(self):
    	return [self.rect.x,self.rect.y]

    def setPos(self,pos):
    	self.rect.x = pos[0]
    	self.rect.y = pos[1]

    def moveLeft(self):
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(x - self.increment_x >= 0):
            self.setPos([x - self.increment_x,y])
            self.dir = 1

    def moveRight(self):
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(x + self.increment_x < self.WIDTH - self.rect[2]):
            self.setPos([x + self.increment_x,y])
            self.dir = 0

    def moveUp(self):
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(y + self.increment_y >= 10):
            self.setPos([x,y - self.increment_y])
            self.dir = 2

    def moveDown(self):
        x = self.getPos()[0]
        y = self.getPos()[1]
        if(y + self.increment_y < self.HIGH - self.rect[3]): # si no se pasa de la pantalla
            self.setPos([x,y + self.increment_y])
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

    def getMargen(self):
        return (self.rect[2],self.rect[3])

class Magician(Player): #Hereda de la clase Player
    def __init__(self, img_name, pos, w, h):
        Player.__init__(self, img_name, pos, w, h)

class OldMan(Player):
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

def oleadas(oleada, ANCHO, ALTO, ls_enemigos, ls_todos,jugador,nivel):
    if(nivel == 1):
        if(oleada == 1):
            for i in range(0,5):
                enemy = Zombie('izqenemigo1_1.png',[0,0], ANCHO, ALTO - 50)
                ls_enemigos.add(enemy)
                ls_todos.add(enemy)
                enemy.setPos([random.randrange(ANCHO - enemy.getRect()[2]),random.randrange(ALTO - 50 - enemy.getRect()[3])])
                enemy.restartMovements(jugador.getPos())
        if(oleada == 2):
            for i in range(0,10):
                enemy = Zombie('izqenemigo1_1.png',[0,0], ANCHO, ALTO - 50)
                ls_enemigos.add(enemy)
                ls_todos.add(enemy)
                enemy.setPos([random.randrange(ANCHO - enemy.getRect()[2]),random.randrange(ALTO - 50 - enemy.getRect()[3])])
                enemy.restartMovements(jugador.getPos())
        if(oleada == 3):
            for i in range(0,15):
                enemy = Zombie('izqenemigo1_1.png',[0,0], ANCHO, ALTO - 50)
                ls_enemigos.add(enemy)
                ls_todos.add(enemy)
                enemy.setPos([random.randrange(ANCHO - enemy.getRect()[2]),random.randrange(ALTO - 50 - enemy.getRect()[3])])
                enemy.restartMovements(jugador.getPos())
    if(nivel == 2): #una sola oleada, pero muy fuerte
        table = cargar_fondo(curdir + "/images/" + 'ene.png', 26, 33)
        for i in range(0,15):
            enemy = Vampire('ene.png',table,[0,0], ANCHO, ALTO - 50)
            ls_enemigos.add(enemy)
            ls_todos.add(enemy)
            enemy.setPos([random.randrange(ANCHO - enemy.getRect()[2]),random.randrange(ALTO - 50 - enemy.getRect()[3])])
            enemy.restartMovements(jugador.getPos())


def checkCollision(sprite1, sprite2):
    col = pygame.sprite.collide_rect(sprite1, sprite2)
    if col == True:
        return True
    else:
        return False

def cargar_fondo(archivo, ancho, alto):
    imagen = pygame.image.load(archivo).convert_alpha()
    imagen_ancho, imagen_alto = imagen.get_size()
    #print 'ancho: ', imagen_ancho, ' xmax: ', imagen_ancho/ancho
    #print 'alto: ',imagen_alto, ' ymax: ', imagen_alto/alto
    tabla_fondos = []

    for fondo_x in range(0, imagen_ancho/ancho):
       linea = []
       tabla_fondos.append(linea)
       for fondo_y in range(0, imagen_alto/alto):
            cuadro = (fondo_x * ancho, fondo_y * alto, ancho, alto)
            linea.append(imagen.subsurface(cuadro))
    return tabla_fondos


def Bresenhamrecta(p): #algoritmo para dibujar rectas

    x0 = p[0][0]
    y0 = p[0][1]
    x1 = p[1][0]
    y1 = p[1][1]
    res = []
    dx = (x1 - x0)
    dy = (y1 - y0)
    #determinar que punto usar para empezar, cual para terminar
    if (dy < 0) :
        dy = -1*dy
        stepy = -1
    else :
        stepy = 1
    if (dx < 0) :
        dx = -1*dx
        stepx = -1
    else :
        stepx = 1
    x = x0
    y = y0
    #se cicla hasta llegar al extremo de la linea
    if(dx>dy) :
        p = 2*dy - dx
        incE = 2*dy
        incNE = 2*(dy-dx)
        while (x != x1) :
            x = x + stepx
            if (p < 0) :
                p = p + incE
            else :
                y = y + stepy
                p = p + incNE
            p_new = [x, y]
            res.append(p_new)

    else :
        p = 2*dx - dy
        incE = 2*dx
        incNE = 2*(dx-dy)
        while (y != y1) :
            y = y + stepy
            if (p < 0) :
                p = p + incE
            else :
                x = x + stepx
                p = p + incNE

            p_new = [x, y]
            res.append(p_new)
    return res


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

#FIn funcion para determianr si el usuario tiene el mouse encima de lso botones

def lifebars(player, surface, pos):
    if(player.getLife() > 75):
        color = verde
    elif(player.getLife() > 50):
        color = amarillo
    else:
        color = rojo
    pygame.draw.rect(surface, color, (pos[0],pos[1],player.getLife(),10))
    #pygame.display.update()
