import pygame
import map
from config import *

screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
class Joueur:
    def __init__(self, positionJoueurX, positionJoueurY, caisse):
        self.x = positionJoueurX,
        self.y = positionJoueurY,
        self.matrix = []
        self.ranger = 0
        self.caisse = caisse
    def setMatrix(self, matrix):
        self.matrix = matrix
    def setRanger(self, ranger):
        self.ranger = ranger
    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed:
            if pressed[pygame.K_UP]:
                if self.y > 0 and self.test(self.x, self.y - 1) and self.testWithCaisse():
                    self.y = self.y - 1
            if pressed[pygame.K_DOWN]:
                if self.y < self.ranger - 1 and self.test(self.x, self.y + 1) and self.testWithCaisse():
                    self.y = self.y + 1
            if pressed[pygame.K_LEFT]:
                if self.x > 0 and self.test(self.x - 1, self.y) and self.testWithCaisse():
                    self.x = self.x - 1
            if pressed[pygame.K_RIGHT]:
                if self.x < self.ranger - 1 and self.test(self.x + 1, self.y) and self.testWithCaisse():
                    self.x = self.x + 1

    def testWithCaisse(self):
        pressed = pygame.key.get_pressed()
        output = []
        for c in self.caisse.getAxe():
            content = False
            if pressed[pygame.K_RIGHT]:
               if self.x + 1 != c[0] or self.y != c[1]:
                   content = True
               elif c[1] < self.ranger - 1 and self.test(c[0] + 1, c[1]) and self.testIfCase(c[0] + 1, c[1]):
                   content = True
            if pressed[pygame.K_DOWN]:
                if self.y + 1 != c[1] or self.x != c[0]:
                    content = True
                elif c[0] < self.ranger - 1 and self.test(c[0], c[1] + 1) and self.testIfCase(c[0], c[1] + 1):
                    content = True
            if pressed[pygame.K_LEFT]:
                if self.x - 1 != c[0] or self.y != c[1]:
                    content = True
                elif c[0] > 0 and self.test(c[0] - 1, c[1]) and self.testIfCase(c[0] - 1, c[1]):
                    content = True
            if pressed[pygame.K_UP]:
                if self.x != c[0] or self.y - 1 != c[1]:
                    content = True
                elif c[1] > 0 and self.test(c[0], c[1] - 1) and self.testIfCase(c[0], c[1] - 1):
                    content = True

            output.append(content)
        if False in output:
            return False
        return True
    def test(self, x, y):
        if self.matrix[y][x] == MUR:
            return False
        return True
    def testIfCase(self, x, y):
        for c in self.caisse.getAxe():
            if c[0] == x and c[1] == y:
                return False
        return True
    def setAxe(self, x, y):
        self.x = x
        self.y = y
    def getAxeY(self):
        return self.y
    def getAxeX(self):
        return self.x
    def getNextCase(self):
        for c in self.caisse.getAxe():
            if self.y == c[1] and self.x == c[0]:
                return 2
        return 0

