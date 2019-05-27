from vector2d import Vector2D
import pygame
import math

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.A = y1 - y2
        self.B = x2 - x1
        self.C = x2 * y1 - x1 * y2


    def intersection(self, line):
        D = self.A * line.B - self.B * line.A
        Dx = self.C * line.B - self.B * line.C
        Dy = self.A * line.C - self.C * line.A

        if D != 0:
            p = Vector2D(Dx / D, Dy / D)
            if (p.x - self.x1) * (self.x2 - self.x1) < 0 or (p.y - self.y1) * (self.y2 - self.y1) < 0:
                return
            if p in line:
                return p

    def find_t(self, p):
        if self.x1 == self.x2:
            return abs((p.y - self.y1) / (self.y1 - self.y2))
        return abs((p.x - self.x1) / (self.x1 - self.x2))

    def length(self):
        return math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2)**2)

    def __contains__(self, p):
        if self.x1 == self.x2:
            return abs(p.x - self.x1) < 1e-1 and min(self.y1, self.y2) - 0.1 <= p.y <= max(self.y1, self.y2) + 0.1

        elif self.y1 == self.y2:
            return abs(p.y - self.y1) < 1e-1 and min(self.x1, self.x2) -0.1 <= p.x <= max(self.x1, self.x2) + 0.1

        #dx = (p.x - ) / abs(self.x2 - self.x1)
        # dy = (p.y - min(self.y1, self.y2)) / abs(self.y2 - self.y1)

        return min(self.x1, self.x2) - 0.1 <= p.x <= max(self.x1, self.x2) + 0.1

    def draw(self, screen):
        pygame.draw.line(screen, pygame.Color('black'), (self.x1, self.y1), (self.x2, self.y2))
