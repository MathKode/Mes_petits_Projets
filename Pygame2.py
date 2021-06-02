import pygame
from pygame import locals as const
from game import Game


def main():
    print("Appuyez sur n'importe quelle touche pour lancer la partie !")

    pygame.init()

    ecran = pygame.display.set_mode((640, 480))
    fond = pygame.image.load("images/menu.png").convert_alpha()

    continuer = True
    jeu = Game(ecran)  # Game() est une class qui va se charger ... du jeu :)

    while continuer:
        for event in pygame.event.get():
            if event.type == const.QUIT or (event.type == const.KEYDOWN and event.key == const.K_ESCAPE):
                # de manière à pouvoir quitter le menu avec echap ou la croix
                continuer = 0
            if event.type == const.KEYDOWN:
                # start() sera une méthode de la class Game(), et s'occupera de lancer le jeu
                jeu.start()

        ecran.blit(fond, (0, 0))

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()