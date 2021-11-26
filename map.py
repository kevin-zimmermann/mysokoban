import pygame
from config import *

class Map:
    def __init__(self, fichier, player, caisse):
        self.player = player
        with open(fichier, 'r') as fich:
            self.lvtest = [[int(l) for l in line.strip().split(" ")] for line in fich]
        self.ranger = len(self.lvtest)
        self.caisse = caisse
        self.objective = []
    def getRanger(self):
        return self.ranger
    def getMatrix(self):
        return self.lvtest
    def drawMap(self,screen):
        y = 0
        for l in self.lvtest:
            x = 0
            for m in l:
                if m == PLAYER:
                    screen.blit(pygame.transform.scale(pygame.image.load('img/player.gif'), (SIZE, SIZE)), (x * SIZE, y * SIZE))
                    self.player.setAxe(x, y)
                if m == MUR:
                    screen.blit(pygame.transform.scale(pygame.image.load('img/mur.jpg'), (SIZE, SIZE)), (x * SIZE, y * SIZE))
                if m == CAISSE:
                    self.caisse.setAxe([x, y])
                if m == OBJECTIF:
                    screen.blit(pygame.transform.scale(pygame.image.load('img/objectif.png'), (SIZE, SIZE)), (x * SIZE, y * SIZE))
                    self.objective.append([x, y])
                x = x + 1
            y = y + 1
    def done(self):
        win = []
        for c in self.caisse.getAxe():
            output = False
            for o in self.objective:
                if o[0] == c[0] and o[1] == c[1]:
                    output = True
            win.append(output)
        if False in win:
            return False
        return True
    def drawNewMap(self,screen):
        y = 0
        for l in self.lvtest:
            x = 0
            for m in l:
                playerX = self.player.getAxeX()
                playerY = self.player.getAxeY()
                continueLoop = True

                for c in self.caisse.getAxe():
                    if c[0] == x and c[1] == y:
                        if m == OBJECTIF:
                            screen.blit(pygame.transform.scale(pygame.image.load('img/caisse_ok.jpg'), (SIZE, SIZE)), (x * SIZE, y * SIZE))
                        else:
                            screen.blit(pygame.transform.scale(pygame.image.load('img/caisse.jpg'), (SIZE, SIZE)), (x * SIZE, y * SIZE))

                        continueLoop = False
                if continueLoop:
                    if playerX == x and playerY == y:
                        screen.blit(pygame.transform.scale(pygame.image.load('img/player.gif'), (SIZE, SIZE)), (playerX * SIZE, playerY * SIZE))
                    else:
                        if m == MUR:
                            screen.blit(pygame.transform.scale(pygame.image.load('img/mur.jpg'), (SIZE, SIZE)), (x * SIZE, y * SIZE))
                        if m == OBJECTIF:
                            screen.blit(pygame.transform.scale(pygame.image.load('img/objectif.png'), (SIZE, SIZE)), (x * SIZE, y * SIZE))
                x = x + 1
            y = y + 1

