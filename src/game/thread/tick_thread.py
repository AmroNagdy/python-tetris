from threading import Thread
from time import sleep

class TickThread(Thread):

    def __init__(self, name, game_loop, tick_frequency):
        Thread.__init__(self)

        self.name = name
        self.game_loop = game_loop
        self.tick_frequency = tick_frequency

        self.should_run = True
        self.daemon = True # Ensures thread dies with the game loop.

    def run(self):
        while self.should_run:
            sleep(self.tick_frequency)
            self.game_loop.tick()

    def stop(self):
        self.should_run = False
