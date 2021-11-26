import pygame
from joueur import Joueur
from map import Map
from config import *
from caisse import Caisse
pygame.init()
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
background = pygame.image.load('img/background.jpeg')
screen.blit(background, (0,0))
caisse = Caisse()
joueur = Joueur(0, 0, caisse)
map = Map('lvl/map', joueur, caisse)
map.drawMap(screen)
caisse.setRanger(map.getRanger())
caisse.setMatrix(map.getMatrix())

joueur.setRanger(map.getRanger())
joueur.setMatrix(map.getMatrix())
done = False

while not done:
    screen.blit(background, (0, 0))
    map.drawNewMap(screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            joueur.move()

            if joueur.getNextCase() == 2:
                print(joueur.getNextCase())
                caisse.move(joueur.getAxeX(), joueur.getAxeY())
            if map.done():
                print('dkjsdnfjkdskj')


