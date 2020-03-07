import curses

class InputHandler():

    def __init__(self, game_loop):
        self.game_loop = game_loop
        self.controls = {
            ord('q'): self.game_loop.stop,
            ord('a'): self.game_loop.rotate_tetromino_left,
            ord('d'): self.game_loop.rotate_tetromino_right,
            curses.KEY_LEFT: self.game_loop.move_cursor_left,
            curses.KEY_RIGHT: self.game_loop.move_cursor_right,
            curses.KEY_DOWN: self.game_loop.drop_tetromino
        }

    def handle(self, input):
        if input in self.controls.keys():
            self.controls[input]()
            self.game_loop.curses_utils.refresh()
