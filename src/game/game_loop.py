from src.tetromino.i import I
from src.tetromino.j import J
from src.tetromino.l import L
from src.tetromino.o import O
from src.tetromino.s import S
from src.tetromino.t import T
from src.tetromino.z import Z
from src.game.component.input_thread import InputThread
from src.game.component.input_handler import InputHandler

import queue
import sys
import curses
import random
import time

class GameLoop():

    def __init__(self, board, curses_utils, tick_frequency):
        self.board = board
        self.curses_utils = curses_utils
        self.tick_frequency = tick_frequency

        self.board_cursor_y = 0
        self.board_cursor_x = board.width // 2
        self.should_run = True
        self.active_tetromino = self.get_random_tetromino()
        self.input_thread = InputThread(curses_utils.stdscr, InputHandler(self))

    def run(self):
        self.input_thread.start()
        self.draw_active_tetromino()

        while self.should_run:
            time.sleep(self.tick_frequency)
            self.tick()

    def tick(self):
        tetromino_location = self.get_tetromino_location()

        if self.board.should_set_tetromino(tetromino_location):
            self.board.set(tetromino_location)
            # TODO: Check here whether to clear rows.
            self.reset_cursor()
            self.active_tetromino = self.get_random_tetromino()
            self.draw_active_tetromino()
        else:
            def cursor_update():
                self.board_cursor_y += 1
            self.move_tetromino(cursor_update)

    def move_cursor_left(self):
        if not self.tetromino_at_horizontal_edge('L'):
            def cursor_update():
                self.board_cursor_x -= 1
            self.move_tetromino(cursor_update)

    def move_cursor_right(self):
        if not self.tetromino_at_horizontal_edge('R'):
            def cursor_update():
                self.board_cursor_x += 1
            self.move_tetromino(cursor_update)

    def move_tetromino(self, cursor_update):
        previous_location = self.get_tetromino_location()
        self.curses_utils.clear_coords(previous_location)
        cursor_update()
        self.draw_active_tetromino()

    def draw_active_tetromino(self):
        self.curses_utils.draw_coords(self.get_tetromino_location())

    def drop_tetromino(self):
        pass

    def get_random_tetromino(self):
        tetrominoes = { 0: I, 1: J, 2: L, 3: O, 4: S, 5: T, 6: Z }
        return tetrominoes[random.randint(0, 6)]()

    def get_tetromino_location(self):
        tetromino_coords = self.active_tetromino.get_coords()

        return [(self.board_cursor_y + y, self.board_cursor_x + x) for y, x in tetromino_coords]

    def tetromino_at_horizontal_edge(self, direction):
        tetromino_location = self.get_tetromino_location()
        comparator = 0 if direction == 'L' else self.board.width - 1

        for _, x in tetromino_location:
            if x == comparator:
                return True

        return False

    def rotate_tetromino_left(self):
        previous_location = self.get_tetromino_location()
        self.curses_utils.clear_coords(previous_location)
        self.active_tetromino.rotate_left()
        self.draw_active_tetromino()

    def rotate_tetromino_right(self):
        previous_location = self.get_tetromino_location()
        self.curses_utils.clear_coords(previous_location)
        self.active_tetromino.rotate_right()
        self.draw_active_tetromino()

    def reset_cursor(self):
        self.board_cursor_y = 0
        self.board_cursor_x = self.board.width // 2

    def stop(self):
        self.should_run = False
        self.input_thread.stop()
