from src.game.game_loop import GameLoop
from src.game.component.curses_utils import CursesUtils
from src.game.component.board import Board

import curses

def main(stdscr):
    stdscr.clear()

    board = Board(height=20, width=10)
    curses_utils = CursesUtils(stdscr)

    GameLoop(board, curses_utils, tick_frequency=0.25).run()

if __name__ == '__main__':
    curses.wrapper(main)
