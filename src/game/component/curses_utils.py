import curses

class CursesUtils():

    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.score_win = self.init_score_win()

    def init_score_win(self):
        height, width, begin_y, begin_x = 2, 40, 21, 0
        score_win = curses.newwin(height, width, begin_y, begin_x)

        return score_win

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

    def write_score(self, score):
        self.score_win.addstr(0, 0, 'Score: ' + str(score))
        self.score_win.refresh()
