class CursesUtils():

    def __init__(self, stdscr):
        self.stdscr = stdscr

    def draw_coords(self, coords):
        for y, x in coords:
            self.stdscr.addch(y, x, '#')
            
        self.stdscr.refresh()

    def clear_coords(self, coords):
        for y, x in coords:
            self.stdscr.addch(y, x, ' ')

        self.stdscr.refresh()

    def redraw_board(self, board_array):
        for y, row in enumerate(board_array):
            for x in range(len(row)):
                if board_array[y][x] == 0:
                    self.stdscr.addch(y, x, ' ')
                else:
                    self.stdscr.addch(y, x, '#')

        self.stdscr.refresh()
