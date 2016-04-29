from func import *

def levelup(ANCHO,ALTO, level):
    #Inicializacion de pantalla
    pygame.init()
    levelup_d = pygame.display.set_mode((ANCHO, ALTO+50))#, pygame.FULLSCREEN)
    pygame.display.set_caption("Magician-zombie v0.1 - Level UP ", 'Spine Runtime')
    tipo = pygame.font.SysFont("monospace", 25)
    levelup_d.fill((0,0,0))
    #Fin de inicializacion de pantalla
    #Cargando imagenes
    posinif = [0,0]
    title = load_image("level.jpg",curdir,alpha=False)
    title = pygame.transform.scale(title, (ANCHO, ALTO-100))
    level_s=load_sound('congrats.wav',curdir)
    level_s.play()
    terminar=False
    reloj=pygame.time.Clock()
    while(not terminar):
        msg = tipo.render(("Felicidades has avanzado al nivel " + str(level)),1, (255,0,0))
        levelup_d.fill((0,0,0))
        levelup_d.blit(title,posinif)
        levelup_d.blit(msg, (ANCHO/2-250, ALTO-30))
        pygame.display.flip()
        reloj.tick(0.2)
        terminar=True
    
    return level
