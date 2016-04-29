from func import *

def winner(ANCHO,ALTO):
    #Inicializacion de pantalla
    pygame.init()
    levelup_d = pygame.display.set_mode((ANCHO, ALTO+50))#, pygame.FULLSCREEN)
    pygame.display.set_caption("Magician-zombie v0.1 -GANASTE", 'Spine Runtime')
    tipo = pygame.font.SysFont("monospace", 25)
    levelup_d.fill((0,0,0))
    #Fin de inicializacion de pantalla
    #Cargando imagenes
    posinif = [0,0]
    title = load_image("won.png",curdir,alpha=False)
    title = pygame.transform.scale(title, (ANCHO, ALTO-100))
    level_s=load_sound('won.wav',curdir)
    level_s.play()
    terminar=False
    reloj=pygame.time.Clock()
    while(not terminar):
        levelup_d.fill((0,0,0))
        levelup_d.blit(title,posinif)
        pygame.display.flip()
        reloj.tick(0.2)
        terminar=True
