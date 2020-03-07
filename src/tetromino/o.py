from src.tetromino.abstract_tetromino import AbstractTetromino

class O(AbstractTetromino):

    @staticmethod
    def rotation_0():
        return [(0, 1), (0, 2), (1, 1), (1, 2)]

    @staticmethod
    def rotation_1():
        return [(0, 1), (0, 2), (1, 1), (1, 2)]

    @staticmethod
    def rotation_2():
        return [(0, 1), (0, 2), (1, 1), (1, 2)]

    @staticmethod
    def rotation_3():
        return [(0, 1), (0, 2), (1, 1), (1, 2)]
