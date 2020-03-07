import curses

class CursesUtils():

    def __init__(self, stdscr):
        self.stdscr = stdscr
        height, width, begin_y, begin_x = 5, 40, 25, 0
        self.debug_win = curses.newwin(height, width, begin_y, begin_x)

    def draw_coords(self, coords):
        for y, x in coords:
            self.stdscr.addch(y, x, '#')
        self.refresh()

    def clear_coords(self, coords):
        for y, x in coords:
            self.stdscr.addch(y, x, ' ')
        self.refresh()

    def redraw_board(self, board_array):
        for y, row in enumerate(board_array):
            for x in range(len(row)):
                if board_array[y][x] == 0:
                    self.stdscr.addch(y, x, ' ')
                else:
                    self.stdscr.addch(y, x, '#')
        self.refresh()

    def refresh(self):
        self.stdscr.refresh()

    def write_to_debug(self, input):
        self.debug_win.addstr(0, 0, str(input))
        self.debug_win.refresh()
