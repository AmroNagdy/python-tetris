import abc
from typing import List, Final, Dict

from input import Input
from src.grid_offset import GridOffset


class Tetromino(abc.ABC):
    """
    A tetromino has 4 possible states to indicate its rotation.
    Each state has an associated list of 4 GridOffsets, i.e. relative pixels the tetromino occupies in a bounding box.
    This implementation of rotations follows the Super Rotation System.
    See: https://tetris.wiki/Super_Rotation_System.
    """

    def __init__(
            self,
            rotation_0: List[GridOffset],
            rotation_1: List[GridOffset],
            rotation_2: List[GridOffset],
            rotation_3: List[GridOffset]
    ):
        self.__state: int = 0
        self.__state_to_offsets: Final[Dict[int, List[GridOffset]]] = {
            0: rotation_0,
            1: rotation_1,
            2: rotation_2,
            3: rotation_3
        }

    def rotate(self, input: Input) -> None:
        input_to_state_modifier: Final[Dict[Input, int]] = {
            Input.ROTATE_CLOCKWISE: 1,
            Input.ROTATE_ANTI_CLOCKWISE: -1
        }

        if input not in input_to_state_modifier:
            raise ValueError(f"The input {input} is not handled by {self.rotate.__name__}.")

        state_modifier = input_to_state_modifier[input]
        self.__state = abs((self.__state + state_modifier) % 4)

    def get_offset(self) -> List[GridOffset]:
        return self.__state_to_offsets[self.__state]


class ITetromino(Tetromino):

    def __init__(self):
        super().__init__(
            [GridOffset(0, 1), GridOffset(1, 1), GridOffset(2, 1), GridOffset(3, 1)],
            [GridOffset(2, 0), GridOffset(2, 1), GridOffset(2, 2), GridOffset(2, 3)],
            [GridOffset(0, 2), GridOffset(1, 2), GridOffset(2, 2), GridOffset(3, 2)],
            [GridOffset(1, 0), GridOffset(1, 1), GridOffset(1, 2), GridOffset(1, 3)]
        )


class JTetromino(Tetromino):

    def __init__(self):
        super().__init__(
            [GridOffset(0, 0), GridOffset(0, 1), GridOffset(1, 1), GridOffset(2, 1)],
            [GridOffset(1, 0), GridOffset(2, 0), GridOffset(1, 1), GridOffset(1, 2)],
            [GridOffset(0, 1), GridOffset(1, 1), GridOffset(2, 1), GridOffset(2, 2)],
            [GridOffset(1, 0), GridOffset(1, 1), GridOffset(0, 2), GridOffset(1, 2)]
        )


class LTetromino(Tetromino):

    def __init__(self):
        super().__init__(
            [GridOffset(2, 0), GridOffset(0, 1), GridOffset(1, 1), GridOffset(2, 1)],
            [GridOffset(1, 0), GridOffset(1, 1), GridOffset(1, 2), GridOffset(2, 2)],
            [GridOffset(0, 1), GridOffset(1, 1), GridOffset(2, 1), GridOffset(0, 2)],
            [GridOffset(0, 0), GridOffset(1, 0), GridOffset(1, 1), GridOffset(1, 2)]
        )


class OTetromino(Tetromino):

    def __init__(self):
        super().__init__(
            [GridOffset(1, 0), GridOffset(2, 0), GridOffset(1, 1), GridOffset(2, 1)],
            [GridOffset(1, 0), GridOffset(2, 0), GridOffset(1, 1), GridOffset(2, 1)],
            [GridOffset(1, 0), GridOffset(2, 0), GridOffset(1, 1), GridOffset(2, 1)],
            [GridOffset(1, 0), GridOffset(2, 0), GridOffset(1, 1), GridOffset(2, 0)]
        )


class STetromino(Tetromino):

    def __init__(self):
        super().__init__(
            [GridOffset(1, 0), GridOffset(2, 0), GridOffset(0, 1), GridOffset(1, 1)],
            [GridOffset(1, 0), GridOffset(1, 1), GridOffset(2, 1), GridOffset(2, 2)],
            [GridOffset(1, 1), GridOffset(2, 1), GridOffset(0, 2), GridOffset(1, 2)],
            [GridOffset(0, 0), GridOffset(0, 1), GridOffset(1, 1), GridOffset(1, 2)]
        )


class TTetromino(Tetromino):

    def __init__(self):
        super().__init__(
            [GridOffset(1, 0), GridOffset(0, 1), GridOffset(1, 1), GridOffset(2, 1)],
            [GridOffset(1, 0), GridOffset(1, 1), GridOffset(2, 1), GridOffset(1, 2)],
            [GridOffset(0, 1), GridOffset(1, 1), GridOffset(2, 1), GridOffset(1, 2)],
            [GridOffset(1, 0), GridOffset(0, 1), GridOffset(1, 1), GridOffset(1, 2)]
        )


class ZTetromino(Tetromino):

    def __init__(self):
        super().__init__(
            [GridOffset(0, 0), GridOffset(1, 0), GridOffset(1, 1), GridOffset(2, 1)],
            [GridOffset(2, 0), GridOffset(1, 1), GridOffset(2, 1), GridOffset(1, 2)],
            [GridOffset(0, 1), GridOffset(1, 1), GridOffset(1, 2), GridOffset(2, 2)],
            [GridOffset(1, 0), GridOffset(0, 1), GridOffset(1, 1), GridOffset(0, 2)]
        )
