from typing import Final, Dict

from src.curses_utils import CursesUtils


class ScoreCounter:
    __rows_cleared_to_score: Final[Dict[int, int]] = {
        1: 40,
        2: 100,
        3: 300,
        4: 1200
    }

    def __init__(self, curses_utils: CursesUtils):
        self.__curses_utils: Final[CursesUtils] = curses_utils
        self.total_score: int = 0

    def update_score(self, rows_cleared: int):
        if rows_cleared not in self.__rows_cleared_to_score:
            # noinspection PyTypeChecker
            valid_values = ", ".join(self.__rows_cleared_to_score.keys())
            raise ValueError(f"Unrecognised rows cleared {rows_cleared}. Valid values: {valid_values}.")

        self.total_score += self.__rows_cleared_to_score[rows_cleared]
        self.__curses_utils.draw_score(self.total_score)
