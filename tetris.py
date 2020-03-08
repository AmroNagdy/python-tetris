from src.game.game_loop import GameLoop
from src.game.component.curses_utils import CursesUtils
from src.game.component.board import Board

import curses

def main(stdscr):
    stdscr.clear()

    curses_utils = CursesUtils(stdscr)
    curses_utils.display_start_screen()

    board = Board(height=20, width=10)
    GameLoop(board, curses_utils, tick_frequency=0.5).run()

if __name__ == '__main__':
    curses.wrapper(main)
