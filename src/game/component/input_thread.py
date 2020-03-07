from threading import Thread

class InputThread(Thread):

    def __init__(self, stdscr, input_handler):
        Thread.__init__(self)

        self.stdscr = stdscr
        self.input_handler = input_handler

        self.should_run = True
        self.daemon = True # Ensures thread dies with the game loop.

    def run(self):
        while self.should_run:
            input = self.stdscr.getch()
            self.input_handler.handle(input)

    def stop(self):
        self.should_run = False
