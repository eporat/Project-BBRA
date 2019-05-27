import pygame
from rect import Rect
from circle import Circle
from puck import Puck
from striker import Striker

class Simulation:
    def __init__(self, width, height, camera, draw=True):
        self.width = width
        self.height = height
        self.draw = draw
        self.camera = camera

        if self.draw:
            pygame.init()
            self.screen = pygame.display.set_mode((width, height))
            pygame.display.set_caption("Simulation")
        self.reset()

    def reset(self):
        self.animating = False
        if self.draw:
            self.clock = pygame.time.Clock()

        self.table  = Rect(50, 50, self.width-50, self.height-50)
        self.center_y = (self.table.y1 + self.table.y2) / 2
        self.puck = Puck(self.width/2, 0.75 * self.height, 20, pygame.Color('red'))
        self.striker = Striker(self.width/2, 0.25 * self.height, 40, pygame.Color('blue'))
        self.collide_rect = self.table.collide_rect(self.puck)

    def handle_events(self):
        if self.draw:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                # if event.type == pygame.KEYDOWN:
                #     if event.key == 32:
                #         self.animating = True

    def run(self, iterations=1):
        self.done = False

        for _ in range(iterations):
            if self.done:
                break

            self.handle_events()
            if self.draw:
                self.screen.fill(pygame.Color('white'))
                self.table.draw(self.screen)

            self.puck.vel = self.camera.puck['pos'] - self.puck.pos
            self.puck.pos = self.camera.puck['pos']
            print(self.puck.vel)
            self.striker.pos = self.camera.striker['pos']
            self.table = Rect(self.camera.table['min_x'], self.camera.table['min_y'],
                                self.camera.table['max_x'], self.camera.table['max_y'])
            self.puck.update(self)
            #self.striker.update(self)

            if self.draw:
                pygame.display.flip()

        return self.striker.vel

    def quit(self):
        if self.draw:
            pygame.quit()
