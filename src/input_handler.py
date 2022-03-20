from typing import Final, Dict, Callable

from src.curses_utils import CursesUtils
from src.input_enum import InputEnum


class InputHandler:

    def __init__(
            self,
            curses_utils: CursesUtils,
            move_right: Callable[[], None],
            move_left: Callable[[], None],
            drop: Callable[[], None],
            rotate_clockwise: Callable[[], None],
            rotate_anti_clockwise: Callable[[], None],
            quit: Callable[[], None]
    ):
        self.__curses_utils: Final[CursesUtils] = curses_utils
        self.__controls: Final[Dict[InputEnum, Callable[[], None]]] = {
            InputEnum.MOVE_RIGHT: move_right,
            InputEnum.MOVE_LEFT: move_left,
            InputEnum.DROP: drop,
            InputEnum.ROTATE_CLOCKWISE: rotate_clockwise,
            InputEnum.ROTATE_ANTI_CLOCKWISE: rotate_anti_clockwise,
            InputEnum.QUIT: quit
        }

    def handle(self, input_enum: InputEnum) -> None:
        if input_enum not in self.__controls:
            # noinspection PyTypeChecker
            valid_values = ", ".join(self.__controls.keys())
            raise ValueError(f"Unrecognised input enum {input_enum}. Valid values: {valid_values}.")

        self.__controls[input_enum]()
        self.__curses_utils.refresh()
