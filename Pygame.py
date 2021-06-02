import pygame

pygame.init()

ecran = pygame.display.set_mode((500, 300)) #pygame.FULLSCREEN à utiliser pour le full screen avec (0,0),pyagem...

pygame.display.set_caption("Mon super titre de Ouf !")

continuer = True
while continuer:
    # ici on crée un rectangle de couleur rose, en x=0, y=0 et de taille 300 sur 200
    # la première parenthèse contient les couleurs en RGB
    pygame.draw.rect(ecran, (180, 20, 150), (0, 0, 10, 10))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            po = str(event.pos).split(', ')
            p1 = int(po[0][1:])
            p2 = int(po[1][:-2])+100
            print(po,p1,p2)

            pygame.draw.rect(ecran, (180, 20, 150), (p1,p2,10,10))
    # ici on actualise l'écran, car on a affiché un rectangle rose, et on veut qu'il soit
    # visible. Si l'on avait pas mit cette instruction, on n'aurait jamais vu le rectangle !
    pygame.display.flip()

pygame.quit()