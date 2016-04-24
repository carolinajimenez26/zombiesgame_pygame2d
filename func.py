from imports import *

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

#FIn funcion para determianr si el usuario tiene el mouse encima de lso botones
