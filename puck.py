import pygame
from circle import Circle
from line import Line
from vector2d import Vector2D
from copy import copy
from time import sleep

class Puck(Circle):
    def __init__(self, x, y, r, c):
        self.vel = Vector2D(0, 0)
        self.max_velocity = 40
        self.path = []
        Circle.__init__(self, x, y, r, c)

    def update(self, game):
        # if game.animating:
        #     if self.pos.y < game.collide_rect.y1 or self.pos.y > game.collide_rect.y2 or self.pos.distsq(game.striker.pos) < (self.r + game.striker.r) ** 2:
        #         sleep(3)
        #         game.reset()
        #     self.pos += self.vel
        #     if self.pos.x > game.collide_rect.x2:
        #         self.pos.x = game.collide_rect.x2
        #         self.vel.x *= -1
        #     if self.pos.x < game.collide_rect.x1:
        #         self.pos.x = game.collide_rect.x1
        #         self.vel.x *= -1
        #
        #     self.intersect(game.collide_rect)
        #     for line in self.path:
        #         line.draw(game.screen)
        # else:
        self.intersect(game.collide_rect)
        for line in self.path:
            line.draw(game.screen)

        if game.draw:
            self.draw(game.screen)



    def intersect(self, board):
        line = Line(self.pos.x, self.pos.y, self.pos.x + self.vel.x, self.pos.y + self.vel.y)
        v = copy(self.vel)
        self.path = []
        p = copy(self.pos)

        for _ in range(100):
            for other_line in board.lines:
                intersection = line.intersection(other_line)
                if intersection:
                    self.path.append(Line(p.x, p.y, intersection.x, intersection.y))
                    p = intersection
                    if other_line is board.left  or other_line is board.right:
                        v.x *= -1
                        line = Line(p.x, p.y, p.x + v.x, p.y + v.y)
                    if other_line in [board.up, board.down]:
                        return
