from abc import ABC

class AbstractTetromino(ABC):

    def __init__(self):
        self.rotation = 0
        self.coords = {
            0: self.rotation_0,
            1: self.rotation_1,
            2: self.rotation_2,
            3: self.rotation_3
        }

    def rotate_right(self):
        self.rotation = (self.rotation + 1) % 4

        return self.coords[self.rotation]

    def rotate_left(self):
        self.rotation = (self.rotation - 1) % 4

        return self.coords[self.rotation]

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
