import curses

from curses_window_factory import CursesWindowFactory
from input_handler import InputHandler
from input_thread import InputThread
from score_counter import ScoreCounter
from src.board import Board
from src.curses_utils import CursesUtils
from src.game_loop import GameLoop


def main(stdscr: curses.window):
    stdscr.clear()

    curses_utils = CursesUtils(stdscr, CursesWindowFactory.build_score_win())
    curses_utils.draw_start_screen()

    board = Board(height=20, width=10)
    score_counter = ScoreCounter()
    input_handler = InputHandler()
    input_thread = InputThread(stdscr, input_handler)
    tick_frequency = 0.5

    game_loop = GameLoop(curses_utils, board, score_counter, input_handler, input_thread, tick_frequency)
    game_loop.start()


if __name__ == '__main__':
    curses.wrapper(main)
