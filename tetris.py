from src.utils.curses_utils import CursesUtils
from src.game.game_loop import GameLoop
from src.game.component.board import Board
from src.game.thread.input_thread import InputThread

import queue
import curses
import time

def main(stdscr):
    stdscr.clear()

    board = Board(height=20, width=10)
    curses_utils = CursesUtils(stdscr)
    input_queue = queue.Queue()
    input_thread = InputThread('Input Thread', stdscr, input_queue)

    GameLoop(board, curses_utils, input_queue, input_thread).run()

if __name__ == '__main__':
    curses.wrapper(main)
