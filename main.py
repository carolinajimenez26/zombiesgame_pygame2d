from game import *
from info import info

def main():

    while(True):
        ANCHO = 800
        ALTO = 600
        pygame.init()
        menu_d = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)
        backgroundm = load_image('backgroundm.jpg',curdir,alpha=False)
        ad1 = load_image('btn1.png', curdir, alpha=False)
        ad2 = load_image('btn3.png', curdir, alpha=False)
        ad3 = load_image('btn2.png', curdir, alpha=False)

        s_fondo = load_sound('fondo1.sf',curdir)
        s_fondo.play()
        rect = ad1.get_rect()
        button_x = ANCHO/2-50
        button_y = ALTO/2
        rect2 = ad2.get_rect()
        menu_d.blit(backgroundm,(0,0))
        menu_d.blit(ad1, (ANCHO/2, ALTO/2))
        menu_d.blit(ad2, (ANCHO/2, (ALTO/2)+50))
        menu_d.blit(ad3, (ANCHO/2, (ALTO/2)+100))

        pygame.mouse.set_visible(True)

        pygame.display.flip()

        terminar = False

        while(not terminar):
            ad1 = load_image('btn1.png', curdir, alpha=False)
            ad2 = load_image('btn3.png', curdir, alpha=False)
            ad3 = load_image('btn2.png', curdir, alpha=False)
            # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
            tipo_t = pygame.font.SysFont("comicsansms", 30)
            # render text
            text_sup = tipo_t.render("Magician-Zombie v0.1 - [Juan Diego H - Carolina J]", 1, (255,255,255))

            mouse_pos = pygame.mouse.get_pos()
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
                        terminar = True
                        #pygame.display.quit()
                        s_fondo.stop()
                        g = game(ANCHO,ALTO)#inicia el juego


                    if(pres_boton(ANCHO/2,ALTO/2+50,ad2)):
                        sys.exit()#se sale del juego

                    if(pres_boton(ANCHO/2,ALTO/2+100,ad3)):
                        print "Creditos" #Muestra la info del juego
                        info(ANCHO,ALTO)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

            menu_d.blit(backgroundm,(0,0))
            menu_d.blit(text_sup, (ANCHO/2-180, 30))
            menu_d.blit(ad1, (ANCHO/2-50, ALTO/2))
            menu_d.blit(ad2, (ANCHO/2-50, (ALTO/2)+50))
            menu_d.blit(ad3, (ANCHO/2-50, (ALTO/2)+100))
            pygame.display.flip()


if __name__ == "__main__":
    main()
