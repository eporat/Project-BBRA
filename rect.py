import pygame
from line import Line

class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = min(x1, x2)
        self.x2 = max(x1, x2)
        self.y1 = min(y1, y2)
        self.y2 = max(y1, y2)

        self.left = Line(x1, y1, x1, y2)
        self.right = Line(x2, y1, x2, y2)
        self.up = Line(x1, y1, x2, y1)
        self.down = Line(x1, y2, x2, y2)

        self.lines = [self.left, self.right, self.up, self.down]

    def collide_rect(self, circle):
        return Rect(self.x1 + circle.r, self.y1 + circle.r, self.x2 - circle.r, self.y2 - circle.r)

    def draw(self, screen):
        for line in self.lines:
            line.draw(screen)
