from src.tetromino.abstract_tetromino import AbstractTetromino

class I(AbstractTetromino):

    @staticmethod
    def rotation_0():
        return [(1, 0), (1, 1), (1, 2), (1, 3)]

    @staticmethod
    def rotation_1():
        return [(0, 2), (1, 2), (2, 2), (3, 2)]

    @staticmethod
    def rotation_2():
        return [(2, 0), (2, 1), (2, 2), (2, 3)]

    @staticmethod
    def rotation_3():
        return [(0, 1), (1, 1), (2, 1), (3, 1)]
