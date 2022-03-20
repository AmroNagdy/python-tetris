import abc
from typing import Dict, List, Callable, Final

from src.grid_offset import GridOffset
from src.input_enum import InputEnum


class AbstractTetromino(abc.ABC):
    """
    A tetromino has 4 possible states to indicate its rotation.
    Each state has an associated list of 4 GridOffsets, i.e. relative pixels the tetromino occupies in a bounding box.
    This implementation of rotations follows the Super Rotation System.
    See: https://tetris.wiki/Super_Rotation_System.
    """

    def __init__(self):
        self.state: int = 0
        self.state_to_offsets: Final[Dict[int, Callable[[], List[GridOffset]]]] = {
            0: self._rotation_0,
            1: self._rotation_1,
            2: self._rotation_2,
            3: self._rotation_3
        }

    def rotate(self, input_enum: InputEnum) -> None:
        input_to_state_modifier: Final[Dict[InputEnum, int]] = {
            InputEnum.ROTATE_CLOCKWISE: 1,
            InputEnum.ROTATE_ANTI_CLOCKWISE: -1
        }

        if input_enum not in input_to_state_modifier:
            raise ValueError(f"The input {input_enum} is not handled by {self.rotate.__name__}.")

        state_modifier = input_to_state_modifier[input_enum]
        self.state = abs((self.state + state_modifier) % 4)

    def get_offset(self) -> List[GridOffset]:
        return self.state_to_offsets[self.state]()

    @staticmethod
    def _rotation_0() -> List[GridOffset]:
        raise NotImplementedError

    @staticmethod
    def _rotation_1() -> List[GridOffset]:
        raise NotImplementedError

    @staticmethod
    def _rotation_2() -> List[GridOffset]:
        raise NotImplementedError

    @staticmethod
    def _rotation_3() -> List[GridOffset]:
        raise NotImplementedError
