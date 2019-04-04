class AI:
    def __init__(self):
        self.i = 0
        return

    def get_move(self):
        self.i += 1
        self.i %= 256
        return self.i