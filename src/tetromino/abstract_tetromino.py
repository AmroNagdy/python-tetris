from abc import ABC

import curses

class AbstractTetromino(ABC):

    def __init__(self):
        self.rotation = 0
        self.coords = {
            0: self.rotation_0,
            1: self.rotation_1,
            2: self.rotation_2,
            3: self.rotation_3
        }

    def rotate(self, direction):
        rotation_operator = -1 if input == 'L' else 1
        self.rotation = (self.rotation + rotation_operator) % 4

    def rotate_left(self):
        self.rotate('L')

    def rotate_right(self):
        self.rotate('R')

    def get_coords(self):
        return self.coords[self.rotation]()

    # Rotations are a list of 4 elements giving the (y, x) offsets of each
    # block of a tetromino relative to the top left corner of some n x m array.

    @staticmethod
    def rotation_0():
        raise NotImplementedError

    @staticmethod
    def rotation_1():
        raise NotImplementedError

    @staticmethod
    def rotation_2():
        raise NotImplementedError

    @staticmethod
    def rotation_3():
        raise NotImplementedError
