from typing import Final, Dict, Callable, Optional

from src.curses_utils import CursesUtils
from src.input import Input


class InputHandler:

    def __init__(self):
        self.__controls: Optional[Dict[Input, Callable[[], None]]] = None

    def initialise(
            self,
            move_right: Callable[[], None],
            move_left: Callable[[], None],
            drop: Callable[[], None],
            rotate_clockwise: Callable[[], None],
            rotate_anti_clockwise: Callable[[], None],
            quit: Callable[[], None]
    ) -> None:
        if self.__controls is not None:
            raise RuntimeError(f"{type(self).__name__} is already initialised.")

        self.__controls = {
            Input.MOVE_RIGHT: move_right,
            Input.MOVE_LEFT: move_left,
            Input.DROP: drop,
            Input.ROTATE_CLOCKWISE: rotate_clockwise,
            Input.ROTATE_ANTI_CLOCKWISE: rotate_anti_clockwise,
            Input.QUIT: quit
        }

    def handle(self, input: Input) -> None:
        if self.__controls is None:
            raise ValueError("Cannot handle inputs until initialised.")

        if input not in self.__controls:
            valid_values = ", ".join([str(enum) for enum in self.__controls.keys()])
            raise ValueError(f"Unrecognised input enum {input}. Valid values: {valid_values}.")

        self.__controls[input]()
