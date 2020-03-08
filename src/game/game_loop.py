from src.tetromino.i import I
from src.tetromino.j import J
from src.tetromino.l import L
from src.tetromino.o import O
from src.tetromino.s import S
from src.tetromino.t import T
from src.tetromino.z import Z
from src.game.component.input_thread import InputThread
from src.game.component.input_handler import InputHandler
from operator import itemgetter

import queue
import sys
import curses
import random
import time

class GameLoop():

    # TODO: Bugfix: When a piece is to the side of another, it can merge into it.

    def __init__(self, board, curses_utils, tick_frequency):
        self.board = board
        self.curses_utils = curses_utils
        self.tick_frequency = tick_frequency

        self.board_cursor_y = 0
        self.board_cursor_x = board.width // 2
        self.should_run = True
        self.tetromino = self.get_random_tetromino()
        self.input_thread = InputThread(curses_utils.stdscr, InputHandler(self))

    def run(self):
        self.input_thread.start()
        self.draw_tetromino()

        while self.should_run:
            time.sleep(self.tick_frequency)
            self.tick()

    def tick(self):
        tetromino_location = self.get_tetromino_location()

        if self.board.should_set_tetromino(tetromino_location):
            self.board.set(tetromino_location)
            if self.board.clear_full_rows():
                self.curses_utils.redraw_board(self.board.array)
            # TODO: Check here whether to clear rows.
            self.reset_cursor()
            self.tetromino = self.get_random_tetromino()
            self.draw_tetromino()
        else:
            def cursor_update():
                self.board_cursor_y += 1
            self.move_tetromino(cursor_update)

    def move_cursor(self, direction):
        operator = -1 if direction == 'L' else 1
        if not self.tetromino_at_horizontal_edge(direction):
            def cursor_update():
                self.board_cursor_x += operator
            self.move_tetromino(cursor_update)

    def move_cursor_left(self):
        self.move_cursor('L')

    def move_cursor_right(self):
        self.move_cursor('R')

    def move_tetromino(self, cursor_update):
        previous_location = self.get_tetromino_location()
        self.curses_utils.clear_coords(previous_location)
        cursor_update()
        self.draw_tetromino()

    def draw_tetromino(self):
        self.curses_utils.draw_coords(self.get_tetromino_location())

    def drop_tetromino(self):
        pass

    def get_random_tetromino(self):
        tetrominoes = { 0: I, 1: J, 2: L, 3: O, 4: S, 5: T, 6: Z }
        return tetrominoes[random.randint(0, 6)]()

    def get_tetromino_location(self):
        tetromino_coords = self.tetromino.get_coords()

        return [(self.board_cursor_y + y, self.board_cursor_x + x) for y, x in tetromino_coords]

    def tetromino_at_horizontal_edge(self, direction):
        tetromino_location = self.get_tetromino_location()
        board_edge = 0 if direction == 'L' else self.board.width

        for _, x in tetromino_location:
            if x == board_edge:
                return True

        return False

    def rotate_tetromino(self, direction):
        previous_location = self.get_tetromino_location()
        self.curses_utils.clear_coords(previous_location)

        # if not self.rotation_will_cause_collision():
        if direction == 'L':
            self.tetromino.rotate_left()
        else:
            self.tetromino.rotate_right()

        x_adjustment = self.get_x_adjustment()
        if x_adjustment is not None:
            self.adjust_board_cursor_x(x_adjustment)

        self.draw_tetromino()

    def get_x_adjustment(self):
        tetromino_location = self.get_tetromino_location()
        leftmost_y, leftmost_x = min(tetromino_location, key=itemgetter(1))
        rightmost_y, rightmost_x = max(tetromino_location, key=itemgetter(1))

        # Check that it is not going outside the board's array.
        if leftmost_x < 0:
            return -leftmost_x
        elif rightmost_x > self.board.width:
            return self.board.width - rightmost_x
        else:
            return None

    def rotation_will_cause_collision(self):
        pass

    def adjust_board_cursor_x(self, x_adjustment):
        self.board_cursor_x += x_adjustment
        self.draw_tetromino()

    def rotate_tetromino_left(self):
        self.rotate_tetromino('L')

    def rotate_tetromino_right(self):
        self.rotate_tetromino('R')

    def reset_cursor(self):
        self.board_cursor_y = 0
        self.board_cursor_x = self.board.width // 2

    def stop(self):
        self.should_run = False
        self.input_thread.stop()
