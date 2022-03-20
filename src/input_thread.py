import curses
import threading
from typing import Dict, Final, Optional

from src.input_enum import InputEnum
from src.input_handler import InputHandler


class InputThread(threading.Thread):

    def __init__(self, stdscr: curses.window, input_handler: InputHandler):
        threading.Thread.__init__(self)

        self.__stdscr: Final[curses.window] = stdscr
        self.__input_handler: Final[InputHandler] = input_handler

        self.__should_run: bool = True
        self.daemon: Final[bool] = True  # Inherited from threading.Thread: Ensures thread dies with the game loop.

    def run(self) -> None:
        while self.__should_run:
            input_ord: int = self.__stdscr.getch()
            input_enum = InputThread.__transform(input_ord)

            if input_enum is not None:
                self.__input_handler.handle(input_enum)

    @staticmethod
    def __transform(input_ord: int) -> Optional[InputEnum]:
        input_ord_to_enum: Final[Dict[int, InputEnum]] = {
            curses.KEY_RIGHT: InputEnum.MOVE_RIGHT,
            curses.KEY_LEFT: InputEnum.MOVE_LEFT,
            curses.KEY_DOWN: InputEnum.DROP,
            ord("d"): InputEnum.ROTATE_CLOCKWISE,
            ord("a"): InputEnum.ROTATE_ANTI_CLOCKWISE,
            ord("q"): InputEnum.QUIT
        }

        return input_ord_to_enum.get(input_ord, None)

    def stop(self) -> None:
        self.__should_run = False
