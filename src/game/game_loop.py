class GameLoop():

    def __init__(self, board, curses_utils):
        self.should_run = True
        self.board = board
        self.curses_utils = curses_utils

    def run(self):
        while self.should_run:
            self.should_run = False
