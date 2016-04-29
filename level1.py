from func import *
from loser import game_over
from levelup import levelup

def level1(ANCHO,ALTO, level = 1):
    aux_oleada = 1 #para que sepa que oleada va a mandar
    contador_vida = 0 #Para saber cuando mandar vidas

    #Inicializacion de pantalla
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO + 50])
    pygame.display.set_caption("Magician-zombie v0.1 - Level 1 ", 'Spine Runtime')
    tipo = pygame.font.SysFont("monospace", 15)
    pantalla_s=load_sound('background.ogg',curdir)
    shot_s=load_sound('shot.wav',curdir)
    pantalla.fill((0,0,0))
    #Fin de inicializacion de pantalla

    #Cargando imagenes
    posinif = [0,0]

    #Grupos de sprites
    ls_todos = pygame.sprite.Group()
    ls_balaj = pygame.sprite.Group()
    ls_enemigos = pygame.sprite.Group()
    ls_balase = pygame.sprite.Group()
    ls_jugadores = pygame.sprite.Group()
    ls_vidas = pygame.sprite.Group()
    #Creamos los personajes

    #-----------------magician------------------------------------------------
    magician = Magician('dere_1.png',[0,0], ANCHO, ALTO)
    middle = [(ANCHO / 2) - (magician.getRect()[2] / 2), (ALTO / 2) - (magician.getRect()[3] / 2)]
    magician.setPos(middle) #posiciona el magician en la mitad de la pantalla

    #Agrega las imagenes del magician
    magician.imaged.append(load_image('dere_1.png',curdir,alpha=True))
    magician.imaged.append(load_image('dere_2.png',curdir,alpha=True))
    magician.imagenar.append(load_image('up_1.png',curdir,alpha=True))
    magician.imagenar.append(load_image('up_2.png',curdir,alpha=True))
    magician.imagei.append(load_image('iz_1.png',curdir,alpha=True))
    magician.imagei.append(load_image('iz_2.png',curdir,alpha=True))
    magician.imagena.append(load_image('ab_1.png',curdir,alpha=True))
    magician.imagena.append(load_image('ab_2.png',curdir,alpha=True))

    ls_todos.add(magician)
    ls_jugadores.add(magician)

    fondo = load_image('background.jpg',curdir, alpha=False)
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO+10))
    pantalla.fill(blanco)

    pantalla.blit(fondo,posinif)
    splash = False
    ls_todos.draw(pantalla)
    ls_enemigos.draw(pantalla)

    pygame.mouse.set_visible(False) #Oculta el puntero del mouse
    pygame.display.flip()
    reloj = pygame.time.Clock()
    terminar = False
    disparo = False
    player_current = 0
    flag = False
    cont = 0
    pantalla_s.play()

    #Variables del reloj
    con_cuadros=0
    tasa_cambio=60
    tiempo_ini=10
    seflim=0

    while(not terminar):

        if(magician.getLife() <= 0): #vuelve al menu ppal
          ls_todos.draw(pantalla)
          pygame.display.flip()
          magician.image = load_image("muerte.png", curdir, alpha=True)
          ls_todos.draw(pantalla)
          pygame.display.flip()
          pantalla_s.stop()
          reloj.tick(0.3)
          game_over(ANCHO,ALTO)
          terminar=True

        if((len(ls_enemigos) == 0 ) and (aux_oleada == 4)):
          pantalla_s.stop()
          reloj.tick(0.6)
          level+=1
          terminar=True
          levelup(ANCHO,ALTO,2)

        #----------------ENEMIGOS-------------------------
        if(len(ls_enemigos) == 0 and aux_oleada < 4): #si ya los mato a todos
          tipo2 = pygame.font.SysFont("comicsansms", 50)
          texto_oleada = tipo2.render("OLEADA "+str(aux_oleada),1, (0,0,0))
          pantalla.blit(texto_oleada,(ANCHO/2 - 100,ALTO/2 - 30))
          pygame.display.flip()
          reloj.tick(0.5)
          oleadas(aux_oleada,ANCHO, ALTO, ls_enemigos, ls_todos,magician,level)
          print "enemigos : " , len(ls_enemigos)
          aux_oleada += 1 #proxima oleada
          contador_vida = 0

        events = pygame.event.get()
        #print "cont : " , contador_vida
        if(magician.getLife() < 35 and contador_vida >= 300):#si se va a morir, debe coger una vida
          anciano = OldMan('viejo_vida.png',[0,0],ANCHO, ALTO)
          anciano.setPos([random.randrange(ANCHO - anciano.getRect()[2]),random.randrange(ALTO - 50 - anciano.getRect()[3])])
          ls_todos.add(anciano)
          ls_vidas.add(anciano)
          contador_vida = 0

        total_segundos=con_cuadros // tasa_cambio
        minutos= total_segundos // 60
        segundos = total_segundos % 60
        tiempo_final = "Tiempo: {0:02}:{1:02}".format(minutos,segundos)
        if total_segundos >60:
          total_segundos=0

        reloj2=tipo.render(tiempo_final, True, blanco)
        tipo = pygame.font.SysFont("monospace", 15)
        blood = tipo.render("Vida actual: " ,1, (255,0,0))
        pantalla.blit(blood, (0, ALTO))
        point = tipo.render(("Puntos: " + str(magician.getScore())),1, (0,0,0))

        if(magician.getLife() > 0):
          point = tipo.render(("Puntos: " + str(magician.getScore())),1, (255,0,0))

        pantalla.fill(pygame.Color(0,0,0))

        keys = pygame.key.get_pressed()

        for event in events:

            if event.type  == pygame.QUIT:
              pantalla_s.stop()
              terminar = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    bala = Bullet('bala.png',magician.getPos())#la posicion inicial depende de objeto que este disparando
                    dir = magician.getDir()
                    bala.setDir(dir)
                    shot_s.play()
                    if(dir == 0):#derecha
                        bala.setPos([magician.getPos()[0] + magician.getRect()[2]/2,magician.getPos()[1]])
                    if(dir == 1):#izquierda
                        bala.setPos([magician.getPos()[0] - magician.getRect()[2]/2,magician.getPos()[1]])
                    if(dir == 2):#arriba
                        bala.setPos([magician.getPos()[0],magician.getPos()[1] - magician.getRect()[3]])
                    if(dir == 3):#abajo
                        bala.setPos([magician.getPos()[0],magician.getPos()[1] + magician.getRect()[3]])

                    ls_balaj.add(bala)
                    ls_todos.add(bala)
                    disparo = True


        if keys[pygame.K_a]:
            player_current = (player_current+1)%len(magician.imagei)
            magician.image = magician.imagei[player_current]
            magician.moveLeft()
            magician.setDir(1)

            for e in ls_enemigos:
              e.restartMovements(magician.getPos())

        if keys[pygame.K_w]:
            player_current = (player_current+1)%len(magician.imagenar)
            magician.image = magician.imagenar[player_current]
            magician.moveUp()
            magician.setDir(2)

            for e in ls_enemigos:
                e.restartMovements(magician.getPos())

        if keys[pygame.K_d]:
            player_current = (player_current+1)%len(magician.imaged)
            magician.image = magician.imaged[player_current]
            magician.moveRight()
            magician.setDir(0)

            for e in ls_enemigos:
                e.restartMovements(magician.getPos())

        if keys[pygame.K_s]:
            player_current = (player_current+1)%len(magician.imagena)
            magician.image = magician.imagena[player_current]
            magician.moveDown()
            magician.setDir(3)

            for e in ls_enemigos:
                e.restartMovements(magician.getPos())

        if keys[pygame.K_ESCAPE]:
          pantalla_s.stop()
          terminar = True

        magician.enemigos=len(ls_enemigos)

        for enemigo in ls_enemigos:
            if(checkCollision(magician,enemigo)): # si se choco
                if(cont == 0):
                    magician.crash()
                    lifebars(magician,pantalla,[ANCHO/2,ALTO])#cambia la bara de vida
                    flag = True

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
                magician.setScore(10)

        for enemigo in ls_enemigos:
            enemigo.jugador = magician.getPos()

        magician.mov=0

        for v in ls_vidas:
            ls_vidas_i = pygame.sprite.spritecollide(magician, ls_vidas, True)
            for vida in ls_vidas_i:
                ls_vidas.remove(vida)
                ls_todos.remove(vida)
                magician.setLife(magician.getLife()+10)
                lifebars(magician,pantalla,[ANCHO/2,ALTO])#cambia la bara de vida

        pantalla.blit(fondo,[0,0])
        pantalla.blit(blood,[0,ALTO+15])
        pantalla.blit(point,[300,ALTO+15]) #+ 15])
        pantalla.blit(reloj2, [500,ALTO+15])
        lifebars(magician,pantalla,[120,ALTO+18])
        ls_todos.draw(pantalla)
        ls_enemigos.draw(pantalla)
        ls_todos.update()
        pygame.display.flip()

        con_cuadros+=1
        reloj.tick(tasa_cambio)
        contador_vida += 1


    return True

#pantalla = pygame.display.set_mode([10,10])
#pygame.display.flip()
