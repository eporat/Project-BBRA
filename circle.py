import pygame
from vector2d import Vector2D

class Circle:
    def __init__(self, x, y, r, c):
        self.pos = Vector2D(x, y)
        self.r = r
        self.c = c

    def draw(self, screen):
        pygame.draw.circle(screen, self.c, (int(self.pos.x), int(self.pos.y)), self.r)
