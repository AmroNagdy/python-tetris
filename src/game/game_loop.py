from src.tetromino.i import I
from src.tetromino.j import J
from src.tetromino.l import L
from src.tetromino.o import O
from src.tetromino.s import S
from src.tetromino.t import T
from src.tetromino.z import Z
from src.utils.curses_utils import CursesUtils
from src.game.thread.input_thread import InputThread
from src.game.thread.tick_thread import TickThread

import queue
import sys
import curses
import random
import time

class GameLoop():

    def __init__(self, board, curses_utils):
        self.board = board
        self.curses_utils = curses_utils

        self.board_cursor_y = 0
        self.board_cursor_x = board.width // 2
        self.input_queue = queue.Queue()
        self.input_thread = InputThread('Input Thread', curses_utils.stdscr, self.input_queue)
        self.tick_thread = TickThread('Tick Thread', self, tick_frequency=0.5)
        self.should_run = True
        self.active_tetromino = self.get_random_tetromino()
        self.controls = {
            ord('q'): self.stop,
            ord('a'): self.active_tetromino.rotate_left,
            ord('d'): self.active_tetromino.rotate_right,
            curses.KEY_LEFT: self.move_cursor_left,
            curses.KEY_RIGHT: self.move_cursor_right,
            curses.KEY_DOWN: self.drop_tetromino
        }

    def run(self):
        self.input_thread.start()
        self.tick_thread.start()
        self.set_and_draw_active_tetromino()

        while self.should_run:
            while not self.input_queue.empty():
                self.handle_input(self.input_queue.get())

    def handle_input(self, input):
        if input in self.controls.keys():
            self.controls[input]()
            self.curses_utils.refresh()

    def tick(self):
        self.board_cursor_y += 1
        self.set_and_draw_active_tetromino()

    def move_cursor_left(self):
        self.board_cursor_x -= 1
        self.set_and_draw_active_tetromino()

    def move_cursor_right(self):
        self.board_cursor_x += 1
        self.set_and_draw_active_tetromino()

    def set_and_draw_active_tetromino(self):
        tetromino_location = self.get_tetromino_location()
        self.board.set(tetromino_location)
        self.curses_utils.draw_coords(tetromino_location)

    def drop_tetromino(self):
        pass

    def get_random_tetromino(self):
        tetrominoes = { 0: I, 1: J, 2: L, 3: O, 4: S, 5: T, 6: Z }
        return tetrominoes[random.randint(0, 6)]()

    def get_tetromino_location(self):
        tetromino_coords = self.active_tetromino.get_coords()

        return [(self.board_cursor_y + y, self.board_cursor_x + x) for y, x in tetromino_coords]

    def stop(self):
        self.should_run = False
        self.input_thread.stop()
        self.tick_thread.stop()
