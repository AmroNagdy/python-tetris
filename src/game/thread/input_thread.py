from threading import Thread

class InputThread(Thread):

    def __init__(self, name, stdscr, input_queue):
        Thread.__init__(self)
        self.name = name
        self.stdscr = stdscr
        self.input_queue = input_queue
        self.should_run = True

    def run(self):
        while self.should_run:
            self.input_queue.put(self.stdscr.getch())

    def stop(self):
        self.should_run = False
