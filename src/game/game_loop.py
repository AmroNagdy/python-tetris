from src.tetromino.i import I
from src.tetromino.j import J
from src.tetromino.l import L
from src.tetromino.o import O
from src.tetromino.s import S
from src.tetromino.t import T
from src.tetromino.z import Z
from src.game.component.input_thread import InputThread
from src.game.component.input_handler import InputHandler
from src.game.component.score_counter import ScoreCounter
from operator import itemgetter

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
        self.tetromino = self.get_random_tetromino()
        self.input_thread = InputThread(curses_utils.stdscr, InputHandler(self))
        self.score_counter = ScoreCounter(curses_utils)

    def run(self):
        self.input_thread.start()
        self.curses_utils.draw_board_border(self.board.height + 1, self.board.width + 1)
        self.curses_utils.write_score(0)
        self.draw_tetromino()

        while self.should_run:
            time.sleep(self.tick_frequency)
            self.tick()

    def stop(self):
        self.should_run = False
        self.input_thread.stop()
        self.curses_utils.display_end_screen(self.score_counter.total_score)
        time.sleep(5)

    def tick(self):
        tetromino_location = self.get_tetromino_location()

        if self.board.should_set_tetromino(tetromino_location):
            self.board.set(tetromino_location)

            rows_cleared = self.board.clear_full_rows()
            if rows_cleared > 0:
                self.curses_utils.redraw_board(self.board.array)
                self.score_counter.update_score(rows_cleared)
            self.reset_cursor()
            self.tetromino = self.get_random_tetromino()
            # Check lose condition (i.e. the tetromino collides with an existing one).
            if self.board.collides(self.get_tetromino_location()):
                self.stop()
            self.draw_tetromino()
        else:
            def cursor_update():
                self.board_cursor_y += 1
            self.move_tetromino(cursor_update)

    def reset_cursor(self):
        self.board_cursor_y = 0
        self.board_cursor_x = self.board.width // 2

    # Move the cursor that points to the active location on the board.
    def move_cursor(self, direction):
        x_operator = -1 if direction == 'L' else 1
        if not self.tetromino_at_horizontal_edge(direction) and not self.will_side_merge(x_operator):
            def cursor_update():
                self.board_cursor_x += x_operator
            self.move_tetromino(cursor_update)

    def move_cursor_left(self):
        self.move_cursor('L')

    def move_cursor_right(self):
        self.move_cursor('R')

    def tetromino_at_horizontal_edge(self, direction):
        tetromino_location = self.get_tetromino_location()
        board_edge = 0 if direction == 'L' else self.board.width

        for _, x in tetromino_location:
            if x == board_edge:
                return True

        return False

    def will_side_merge(self, x_operator):
        future_tetromino_coords = [(y, x + x_operator) for y, x in self.get_tetromino_location()]
        return self.board.collides(future_tetromino_coords)

    # Move and redraw the tetromino according to where the cursor should move.
    def move_tetromino(self, cursor_update):
        previous_location = self.get_tetromino_location()
        self.curses_utils.clear_coords(previous_location)
        cursor_update()
        self.draw_tetromino()

    def draw_tetromino(self):
        self.curses_utils.draw_coords(self.get_tetromino_location())

    def drop_tetromino(self):
        while not self.board.should_set_tetromino(self.get_tetromino_location()):
            self.tick()

    # Create and get a new tetromino.
    def get_random_tetromino(self):
        tetrominoes = { 0: I, 1: J, 2: L, 3: O, 4: S, 5: T, 6: Z }
        return tetrominoes[random.randint(0, 6)]()

    # Get coords of the tetromino on the board.
    def get_tetromino_location(self):
        tetromino_coords = self.tetromino.get_coords()

        return [(self.board_cursor_y + y, self.board_cursor_x + x) for y, x in tetromino_coords]

    # Rotate the tetromino either clockwise (L) or anti-clockwise (R).
    def rotate_tetromino(self, direction):
        previous_location = self.get_tetromino_location()
        self.curses_utils.clear_coords(previous_location)
        self.tetromino.rotate(direction)

        # Perform out-of-bounds adjustment if rotation takes the tetromino out the board.
        x_adjustment = self.get_x_adjustment()
        if x_adjustment is not None:
            self.adjust_board_cursor_x(x_adjustment)

        if self.board.collides(self.get_tetromino_location()):
            self.undo_rotation(direction)
            self.curses_utils.redraw_board(self.board.array)

        self.draw_tetromino()

    def rotate_tetromino_left(self):
        self.rotate_tetromino('L')

    def rotate_tetromino_right(self):
        self.rotate_tetromino('R')

    def undo_rotation(self, direction):
        if direction == 'L':
            self.rotate_tetromino_right()
        else:
            self.rotate_tetromino_left()

    # If the tetromino will go outside the board because of rotation, the cursor's
    # x coord needs to be adjusted.
    def get_x_adjustment(self):
        tetromino_location = self.get_tetromino_location()
        leftmost_x = min(tetromino_location, key=itemgetter(1))[1]
        rightmost_x = max(tetromino_location, key=itemgetter(1))[1]

        # Check that it is not going outside the board's array.
        if leftmost_x < 0:
            return -leftmost_x
        elif rightmost_x > self.board.width:
            return self.board.width - rightmost_x
        else:
            return None

    def adjust_board_cursor_x(self, x_adjustment):
        self.board_cursor_x += x_adjustment
        self.draw_tetromino()
