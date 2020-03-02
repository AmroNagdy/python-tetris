class T(AbstractTetromino):

    def rotation_0():
        return [(0, 1), (1, 0), (1, 1), (1, 2)]

    def rotation_1():
        return [(0, 1), (1, 1), (1, 2), (2, 1)]

    def rotation_2():
        return [(1, 0), (1, 1), (1, 2), (2, 1)]

    def rotation_3():
        return [(0, 1), (1, 0), (1, 1), (2, 1)]
