from func import *

def game_over(ANCHO,ALTO):

    #Inicializacion de pantalla
    pygame.init()
    gameover_d = pygame.display.set_mode((ANCHO, ALTO+50), pygame.FULLSCREEN)
    pygame.display.set_caption("Magician-zombie v0.1 - Game over ", 'Spine Runtime')
    tipo = pygame.font.SysFont("monospace", 25)
    gameover_d.fill((0,255,0))
    #Fin de inicializacion de pantalla
    #Cargando imagenes
    posinif = [0,0]
    gameo = cargar_fondo(curdir + "/images/gameover.png", 355, 355)
    gameo_s=load_sound('gameover.ogg',curdir)
    gameo_s.play()
    reloj=pygame.time.Clock()
    terminar=False
    actual=0
    tiempo=400
    game = gameo[actual][0]
    while(not terminar):
        blood = tipo.render("Presione R para continuar perdiendo :v ",1, (0,0,0))

        events = pygame.event.get()
        for event in events:

            if event.type  == pygame.QUIT:
                terminar = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    #pygame.display.quit()
                    terminar=True


        if(tiempo==0):
            if(actual <= 2):
                game=gameo[actual][0]
                actual+=1
                tiempo=400
            else:
                actual = 0
        else:
            tiempo-=1

        gameover_d.fill((0,255,0))
        gameover_d.blit(blood, (ANCHO/2-300, ALTO+20))
        gameover_d.blit(pygame.transform.scale(game, (ANCHO, ALTO+10)),posinif)

        pygame.display.flip()
