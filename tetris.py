import curses

from src.board import Board
from src.curses_utils import CursesUtils
from src.game_loop import GameLoop


def main(stdscr: curses.window):
    stdscr.clear()

    curses_utils = CursesUtils(stdscr)
    curses_utils.draw_start_screen()

    board = Board(height=20, width=10)
    GameLoop(board, curses_utils, tick_frequency=0.5).run()


if __name__ == '__main__':
    curses.wrapper(main)
