import pygame
import sys
import os
curdir = os.getcwd()

ALTO=400
ANCHO=700
blanco=(255,255,255)

#Carga los sonidos verificando la ruta
def load_sound(nombre_s,dir_son):
    ruta = os.path.join(dir_son, nombre_s)
    try:
        sound = pygame.mixer.Sound(ruta)
    except:
        print "Error, no se puede cargar el sonido, verifique el formato: ", ruta
        sys.exit(1)
    return sound

#Funcion para verificar que las imagenes se cargan correctamente
def load_image(nombre_a, dir_img, alpha=False):
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

def main():
    #Inicializacion de pantalla
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(blanco)

     #Cargando imagenes
    personaje=load_image('PJ1.png', curdir, alpha=True)
    fondo=load_image('fondo.jpg',curdir, alpha=False)

    #Muestra las imagenes en primera instancia
    posinip=[10,10]
    posinif=[0,0]
    pantalla.blit(fondo,posinip)
    pantalla.blit(personaje,posinip)

    #Obtengo x,y del objeto
    marco=personaje.get_rect()

    pygame.display.flip()

    terminar=False
    while(not terminar):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                terminar=True

if __name__ == "__main__":
    main()
