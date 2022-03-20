import curses
from typing import List, Final

from src.grid_offset import GridOffset


class CursesUtils:

    def __init__(self, stdscr: curses.window):
        self.__stdscr: Final[curses.window] = stdscr
        self.__score_win: Final[curses.window] = self.init_score_win()

    @staticmethod
    def init_score_win() -> curses.window:
        height, width, begin_y, begin_x = 2, 40, 23, 0
        score_win = curses.newwin(height, width, begin_y, begin_x)

        return score_win

    def draw_board_border(self, height: int, width: int) -> None:
        self.__stdscr.addstr(0, 0, "+" + ("-" * width) + "+")

        for i in range(1, height + 1):
            self.__stdscr.addch(i, 0, "|")
            self.__stdscr.addch(i, width + 1, "|")

        self.__stdscr.addstr(height + 1, 0, "+" + ("-" * width) + "+")

    def draw_relative_pixels(self, grid_offsets: List[GridOffset]) -> None:
        for grid_offset in grid_offsets:
            self.__stdscr.addch(grid_offset.y + 1, grid_offset.x + 1, "#")
        self.refresh()

    def clear_relative_pixels(self, grid_offsets: List[GridOffset]) -> None:
        for grid_offset in grid_offsets:
            self.__stdscr.addch(grid_offset.y + 1, grid_offset.x + 1, " ")
        self.refresh()

    def redraw_board(self, board_array: List[List[int]]) -> None:
        for y, row in enumerate(board_array):
            for x in range(len(row)):
                if board_array[y][x] == 0:
                    self.__stdscr.addch(y + 1, x + 1, " ")
                else:
                    self.__stdscr.addch(y + 1, x + 1, "#")
        self.refresh()

    def refresh(self) -> None:
        self.__stdscr.refresh()

    def draw_score(self, score: int) -> None:
        self.__score_win.addstr(0, 0, f"Score: {score}")
        self.__score_win.refresh()

    def draw_start_screen(self) -> None:
        self.__stdscr.addstr(0, 1, "Welcome to Tetris!")
        self.__stdscr.addstr(2, 1, "Controls:")
        self.__stdscr.addstr(3, 1, "A: Rotate tetromino clockwise")
        self.__stdscr.addstr(4, 1, "D: Rotate tetromino anti-clockwise")
        self.__stdscr.addstr(5, 1, "LEFT ARROW: Move tetromino left")
        self.__stdscr.addstr(6, 1, "RIGHT ARROW: Move tetromino right")
        self.__stdscr.addstr(7, 1, "DOWN ARROW: Drop tetromino")
        self.__stdscr.addstr(8, 1, "Q: Quit game")
        self.__stdscr.addstr(10, 1, "Press any key to start...")
        self.refresh()
        self.__stdscr.getch()
        self.__stdscr.clear()

    def draw_end_screen(self, final_score: int) -> None:
        self.__stdscr.clear()
        self.__score_win.clear()
        self.__stdscr.addstr(1, 1, "Thanks for playing!")
        self.__stdscr.addstr(2, 1, f"Your final score is: {final_score}")
        self.refresh()
