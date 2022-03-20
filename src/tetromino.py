from typing import List

from src.abstract_tetromino import AbstractTetromino
from src.grid_offset import GridOffset


class I(AbstractTetromino):

    @staticmethod
    def _rotation_0() -> List[GridOffset]:
        return [GridOffset(0, 1), GridOffset(1, 1), GridOffset(2, 1), GridOffset(3, 1)]

    @staticmethod
    def _rotation_1() -> List[GridOffset]:
        return [GridOffset(2, 0), GridOffset(2, 1), GridOffset(2, 2), GridOffset(2, 3)]

    @staticmethod
    def _rotation_2() -> List[GridOffset]:
        return [GridOffset(0, 2), GridOffset(1, 2), GridOffset(2, 2), GridOffset(3, 2)]

    @staticmethod
    def _rotation_3() -> List[GridOffset]:
        return [GridOffset(1, 0), GridOffset(1, 1), GridOffset(1, 2), GridOffset(1, 3)]


class J(AbstractTetromino):

    @staticmethod
    def _rotation_0() -> List[GridOffset]:
        return [GridOffset(0, 0), GridOffset(0, 1), GridOffset(1, 1), GridOffset(2, 1)]

    @staticmethod
    def _rotation_1() -> List[GridOffset]:
        return [GridOffset(1, 0), GridOffset(2, 0), GridOffset(1, 1), GridOffset(1, 2)]

    @staticmethod
    def _rotation_2() -> List[GridOffset]:
        return [GridOffset(0, 1), GridOffset(1, 1), GridOffset(2, 1), GridOffset(2, 2)]

    @staticmethod
    def _rotation_3() -> List[GridOffset]:
        return [GridOffset(1, 0), GridOffset(1, 1), GridOffset(0, 2), GridOffset(1, 2)]


class L(AbstractTetromino):

    @staticmethod
    def _rotation_0() -> List[GridOffset]:
        return [GridOffset(2, 0), GridOffset(0, 1), GridOffset(1, 1), GridOffset(2, 1)]

    @staticmethod
    def _rotation_1() -> List[GridOffset]:
        return [GridOffset(1, 0), GridOffset(1, 1), GridOffset(1, 2), GridOffset(2, 2)]

    @staticmethod
    def _rotation_2() -> List[GridOffset]:
        return [GridOffset(0, 1), GridOffset(1, 1), GridOffset(2, 1), GridOffset(0, 2)]

    @staticmethod
    def _rotation_3() -> List[GridOffset]:
        return [GridOffset(0, 0), GridOffset(1, 0), GridOffset(1, 1), GridOffset(1, 2)]


class O(AbstractTetromino):

    @staticmethod
    def _rotation_0() -> List[GridOffset]:
        return [GridOffset(1, 0), GridOffset(2, 0), GridOffset(1, 1), GridOffset(2, 1)]

    @staticmethod
    def _rotation_1() -> List[GridOffset]:
        return [GridOffset(1, 0), GridOffset(2, 0), GridOffset(1, 1), GridOffset(2, 1)]

    @staticmethod
    def _rotation_2() -> List[GridOffset]:
        return [GridOffset(1, 0), GridOffset(2, 0), GridOffset(1, 1), GridOffset(2, 1)]

    @staticmethod
    def _rotation_3() -> List[GridOffset]:
        return [GridOffset(1, 0), GridOffset(2, 0), GridOffset(1, 1), GridOffset(2, 0)]


class S(AbstractTetromino):

    @staticmethod
    def _rotation_0() -> List[GridOffset]:
        return [GridOffset(1, 0), GridOffset(2, 0), GridOffset(0, 1), GridOffset(1, 1)]

    @staticmethod
    def _rotation_1() -> List[GridOffset]:
        return [GridOffset(1, 0), GridOffset(1, 1), GridOffset(2, 1), GridOffset(2, 2)]

    @staticmethod
    def _rotation_2() -> List[GridOffset]:
        return [GridOffset(1, 1), GridOffset(2, 1), GridOffset(0, 2), GridOffset(1, 2)]

    @staticmethod
    def _rotation_3() -> List[GridOffset]:
        return [GridOffset(0, 0), GridOffset(0, 1), GridOffset(1, 1), GridOffset(1, 2)]


class T(AbstractTetromino):

    @staticmethod
    def _rotation_0() -> List[GridOffset]:
        return [GridOffset(1, 0), GridOffset(0, 1), GridOffset(1, 1), GridOffset(2, 1)]

    @staticmethod
    def _rotation_1() -> List[GridOffset]:
        return [GridOffset(1, 0), GridOffset(1, 1), GridOffset(2, 1), GridOffset(1, 2)]

    @staticmethod
    def _rotation_2() -> List[GridOffset]:
        return [GridOffset(0, 1), GridOffset(1, 1), GridOffset(2, 1), GridOffset(1, 2)]

    @staticmethod
    def _rotation_3() -> List[GridOffset]:
        return [GridOffset(1, 0), GridOffset(0, 1), GridOffset(1, 1), GridOffset(1, 2)]


class Z(AbstractTetromino):

    @staticmethod
    def _rotation_0() -> List[GridOffset]:
        return [GridOffset(0, 0), GridOffset(1, 0), GridOffset(1, 1), GridOffset(2, 1)]

    @staticmethod
    def _rotation_1() -> List[GridOffset]:
        return [GridOffset(2, 0), GridOffset(1, 1), GridOffset(2, 1), GridOffset(1, 2)]

    @staticmethod
    def _rotation_2() -> List[GridOffset]:
        return [GridOffset(0, 1), GridOffset(1, 1), GridOffset(1, 2), GridOffset(2, 2)]

    @staticmethod
    def _rotation_3() -> List[GridOffset]:
        return [GridOffset(1, 0), GridOffset(0, 1), GridOffset(1, 1), GridOffset(0, 2)]
