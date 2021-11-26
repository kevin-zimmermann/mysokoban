import pygame
from config import *

class Caisse:
    def __init__(self):
        self.axe = []
        self.matrix = []
        self.ranger = 0

    def setAxe(self, axe):
        self.axe.append(axe)
    def getAxe(self):
        return self.axe
    def setMatrix(self, matrix):
        self.matrix = matrix
    def setRanger(self, ranger):
        self.ranger = ranger
    def move(self, x, y):
        pressed = pygame.key.get_pressed()
        index = 0
        for c in self.axe:
            if x == c[0] and y == c[1]:
                if pressed[pygame.K_UP]:
                    if c[1] > 0 and self.test(c[0], c[1] - 1):
                        self.axe[index][1] = c[1] - 1
                if pressed[pygame.K_DOWN]:
                    if c[1] < self.ranger - 1 and self.test(c[0], c[1] + 1):
                        self.axe[index][1] = c[1] + 1
                if pressed[pygame.K_LEFT]:
                    if c[0] > 0 and self.test(c[0] - 1, c[1]):
                        self.axe[index][0] = c[0] - 1
                if pressed[pygame.K_RIGHT]:
                    if c[0] < self.ranger - 1 and self.test(c[0] + 1, c[1]):
                        self.axe[index][0] = c[0] + 1
            index = index + 1
    def test(self, x, y):
        if self.matrix[y][x] == MUR:
            return False
        return True