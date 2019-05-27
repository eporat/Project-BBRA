from __future__ import division
from math import sqrt, sin, cos

class Vector2D:
    def __init__(self, x, y):
        self.x = x;
        self.y = y

    def mag(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def setmag(self, mag):
        self.normalize()
        self *= mag
        return self

    def normalize(self):
        self = self / self.mag()
        return self

    def to_tuple(self):
        return (self.x, self.y)

    def distsq(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    @staticmethod
    def from_angle(angle):
        return Vector2D(cos(angle), sin(angle))

    def __truediv__(self, const):
        return Vector2D(self.x / const, self.y / const)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, const):
        return Vector2D(self.x * const, self.y * const)

    def __copy__(self):
        return Vector2D(self.x, self.y)

    def __str__(self):
        return f'Vector2D: {self.x} {self.y}'
