import pygame
from circle import Circle
from line import Line
from vector2d import Vector2D
from copy import copy
import math
import numpy as np

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('arial', 25)
NUM_RAYS = 16

class Striker(Circle):
    def __init__(self, x, y, r, c):
        self.vel = Vector2D(0, 0)
        self.max_vel = 10
        Circle.__init__(self, x, y, r, c)

    def min_time_strategy(self, game):
        best_angle = -1
        best_time = float("inf")
        best_vel = Vector2D(0,0)
        best_p = None
        best_d = 0

        for angle in np.linspace(0, math.pi * 2, NUM_RAYS):

            vel = Vector2D.from_angle(angle)
            line = Line(self.pos.x, self.pos.y, self.pos.x + vel.x * 1000, self.pos.y + vel.y * 1000)

            if game.draw:
                line.draw(game.screen)

            time = 0

            for other_line in game.puck.path:
                p = line.intersection(other_line)
                if p:
                    if game.draw:
                        Circle(p.x, p.y, 5, pygame.Color('yellow')).draw(game.screen)

                    t = other_line.find_t(p) * other_line.length () / game.puck.vel.mag()

                    if game.draw:
                        textsurface = myfont.render(str(round(time+t, 3)) + " frames", False, (0, 0, 0))
                        game.screen.blit(textsurface,(p.x,p.y))

                    if self.pos.distsq(p) < 5**2:
                        self.vel = Vector2D(0,0)

                    d = math.sqrt(self.pos.distsq(p))

                    if time + t < best_time and p.y <= game.center_y and d <= self.max_vel * (time + t) :
                        best_time = time + t
                        best_p = p
                        best_time = time + t
                        best_angle = angle
                        best_vel = copy(vel)
                        best_d = math.sqrt(self.pos.distsq(p))
                time += other_line.length() / game.puck.vel.mag()

        if best_p:
            if game.draw:
                Circle(best_p.x, best_p.y, 10, pygame.Color('purple')).draw(game.screen)
            self.vel = Vector2D.from_angle(best_angle).setmag(min(self.max_vel, best_d / best_time))

    def max_time_strategy(self, game):
        best_angle = -1
        best_time = 0
        best_vel = Vector2D(0,0)
        best_p = None
        best_d = 0

        for angle in np.linspace(0, math.pi * 2, NUM_RAYS):

            vel = Vector2D.from_angle(angle)
            line = Line(self.pos.x, self.pos.y, self.pos.x + vel.x * 1000, self.pos.y + vel.y * 1000)

            if game.draw:
                line.draw(game.screen)

            time = 0

            for other_line in game.puck.path:
                p = line.intersection(other_line)
                if p:
                    if game.draw:
                        Circle(p.x, p.y, 5, pygame.Color('yellow')).draw(game.screen)
                    t = other_line.find_t(p) * other_line.length () / game.puck.vel.mag()
                    if game.draw:
                        textsurface = myfont.render(str(round(time+t, 3)) + " frames", False, (0, 0, 0))
                        game.screen.blit(textsurface,(p.x,p.y))

                    if self.pos.distsq(p) < 5**2:
                        self.vel = Vector2D(0,0)

                    if time + t >= best_time and p.y <= game.center_y:
                        best_time = time + t
                        best_p = p
                        best_time = time + t
                        best_angle = angle
                        best_vel = copy(vel)
                        best_d = math.sqrt(self.pos.distsq(p))
                time += other_line.length() / game.puck.vel.mag()

        if best_p:
            if game.draw:
                Circle(best_p.x, best_p.y, 10, pygame.Color('purple')).draw(game.screen)
            self.vel = Vector2D.from_angle(best_angle).setmag(min(self.max_vel, best_d / best_time))

    def update(self, game):
        # if game.animating:
        #     self.pos += self.vel
        self.min_time_strategy(game)
        if game.draw:
            self.draw(game.screen)
