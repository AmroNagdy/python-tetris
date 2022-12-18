import curses
import threading
from typing import Dict, Final, Optional

from src.input import Input
from src.input_handler import InputHandler


class InputThread(threading.Thread):

    def __init__(self, stdscr: curses.window, input_handler: InputHandler):
        threading.Thread.__init__(self, name="InputThread")

        self.__stdscr: Final[curses.window] = stdscr
        self.__input_handler: Final[InputHandler] = input_handler

        self.__stopped: Final[threading.Event] = threading.Event()
        self.daemon: Final[bool] = True  # Inherited from threading.Thread: Ensures thread dies with the game loop.

    def run(self) -> None:
        while not self.__stopped.is_set():
            input_ord = self.__stdscr.getch()
            input = InputThread.__transform(input_ord)

            if input is not None:
                self.__input_handler.handle(input)
                self.__stdscr.refresh()

    @staticmethod
    def __transform(input_ord: int) -> Optional[Input]:
        input_ord_to_enum: Final[Dict[int, Input]] = {
            curses.KEY_RIGHT: Input.MOVE_RIGHT,
            curses.KEY_LEFT: Input.MOVE_LEFT,
            curses.KEY_DOWN: Input.DROP,
            ord("d"): Input.ROTATE_CLOCKWISE,
            ord("a"): Input.ROTATE_ANTI_CLOCKWISE,
            ord("q"): Input.QUIT
        }

        return input_ord_to_enum.get(input_ord)

    def stop(self) -> None:
        self.__stopped.set()
