from func import *
def info(ANCHO,ALTO):

    pygame.init()
    menu_d = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)
    backgroundm = load_image('backgroundm.jpg',curdir,alpha=False)
    terminar = False
    tipo = pygame.font.SysFont("comicsansms", 30)

    header = tipo.render("Instrucciones de juego: ",1, (255,255,255))

    izq = "Para moverse hacia la izquierda, utilice el boton A "
    der = "Para moverse hacia la derecha, utilice el boton D "
    arr = "Para moverse hacia arriba, utilice el boton W "
    aba = "Para moverse hacia abajo, utilice el boton S "
    disparo = "Para disparar, utilice la barra espaciadora "
    objetivo = "El objetivo del juego es matar todos los zombies"

    Salida0 = tipo.render(izq,1, (255,255,255))
    Salida1 = tipo.render(der,1, (255,255,255))
    Salida2 = tipo.render(arr,1, (255,255,255))
    Salida3 = tipo.render(aba,1, (255,255,255))
    Salida4 = tipo.render(disparo,1, (255,255,255))
    obj = tipo.render(objetivo,1, (255,255,255))

    Salir = tipo.render("Para volver, presione ENTER",1, (255,255,255))


    while(not terminar):

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    terminar = True

        menu_d.blit(backgroundm,(0,0))
        menu_d.blit(header,(0, 30))

        menu_d.blit(Salida0,(30, 30+50))
        menu_d.blit(Salida1,(30, 30+70))
        menu_d.blit(Salida2,(30, 30+90))
        menu_d.blit(Salida3,(30, 30+110))
        menu_d.blit(Salida4,(30, 30+130))
        menu_d.blit(obj,(30, 60+150))

        menu_d.blit(Salir,(0, ALTO - 50))
        pygame.display.flip()
