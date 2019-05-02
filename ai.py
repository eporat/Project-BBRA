#import tensorflow as tf

class AI:
    def __init__(self, camera):
        self.puck = self.camera.puck
        self.player = self.camera.player

    def get_move(self):
        return (self.puck.pos[0] - self.player.pos[0], self.puck.pos[1] - self.player.pos[1])
