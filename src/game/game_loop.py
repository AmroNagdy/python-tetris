from src.tetromino.i import I
from src.tetromino.j import J
from src.tetromino.l import L
from src.tetromino.o import O
from src.tetromino.s import S
from src.tetromino.t import T
from src.tetromino.z import Z

import curses
import random

class GameLoop():

    def __init__(self, board, curses_utils, input_queue, input_thread):
        self.should_run = True
        self.active_tetromino = self.get_random_tetromino()
        self.controls = {
            curses.KEY_LEFT: self.active_tetromino.rotate("L"),
            curses.KEY_RIGHT: self.active_tetromino.rotate("R"),
            curses.KEY_DOWN: self.drop_tetromino()
        }
        self.board = board
        self.curses_utils = curses_utils
        self.input_queue = input_queue
        self.input_thread = input_thread

    def run(self):
        self.input_thread.start()

        while self.should_run:
            while not self.input_queue.empty():
                self.handle_input(self.input_queue.get())

    def handle_input(self, input):
        self.controls[input]

    def drop_tetromino(self):
        pass

    def get_random_tetromino(self):
        tetrominoes = { 0: I, 1: J, 2: L, 3: O, 4: S, 5: T, 6: Z }
        return tetrominoes[random.randint(0, 6)]()
