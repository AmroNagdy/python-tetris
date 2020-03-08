import curses
import time

class CursesUtils():

    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.score_win = self.init_score_win()

    def init_score_win(self):
        height, width, begin_y, begin_x = 2, 40, 23, 0
        score_win = curses.newwin(height, width, begin_y, begin_x)

        return score_win

    def draw_board_border(self, height, width):
        self.stdscr.addstr(0, 0, '+' + ('-' * width) + '+')
        for i in range(1, height + 1):
            self.stdscr.addch(i, 0, '|')
            self.stdscr.addch(i, width + 1, '|')
        self.stdscr.addstr(height + 1, 0, '+' + ('-' * width) + '+')

    def draw_coords(self, coords):
        for y, x in coords:
            self.stdscr.addch(y + 1, x + 1, '#')
        self.refresh()

    def clear_coords(self, coords):
        for y, x in coords:
            self.stdscr.addch(y + 1, x + 1, ' ')
        self.refresh()

    def redraw_board(self, board_array):
        for y, row in enumerate(board_array):
            for x in range(len(row)):
                if board_array[y][x] == 0:
                    self.stdscr.addch(y + 1, x + 1, ' ')
                else:
                    self.stdscr.addch(y + 1, x + 1, '#')
        self.refresh()

    def refresh(self):
        self.stdscr.refresh()

    def write_score(self, score):
        self.score_win.addstr(0, 0, 'Score: ' + str(score))
        self.score_win.refresh()

    def display_start_screen(self):
        self.stdscr.addstr(0, 1, 'Welcome to Tetris!')
        self.stdscr.addstr(2, 1, 'Controls:')
        self.stdscr.addstr(3, 1, 'A: Rotate tetromino clockwise')
        self.stdscr.addstr(4, 1, 'D: Rotate tetromino anti-clockwise')
        self.stdscr.addstr(5, 1, 'LEFT ARROW: Move tetromino left')
        self.stdscr.addstr(6, 1, 'RIGHT ARROW: Move tetromino right')
        self.stdscr.addstr(7, 1, 'DOWN ARROW: Drop tetromino')
        self.stdscr.addstr(8, 1, 'Q: Quit game')
        self.stdscr.addstr(10, 1, 'Press any key to start...')
        self.refresh()
        self.stdscr.getch()
        self.stdscr.clear()

    def display_end_screen(self, final_score):
        self.stdscr.clear()
        self.score_win.clear()
        self.stdscr.addstr(1, 1, 'Thanks for playing!')
        self.stdscr.addstr(2, 1, f'Your final score is: {final_score}')
        self.refresh()
