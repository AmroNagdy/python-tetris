import curses


class CursesWindowFactory:

    @staticmethod
    def build_score_win() -> curses.window:
        height, width, begin_y, begin_x = 2, 40, 23, 0
        score_win = curses.newwin(height, width, begin_y, begin_x)

        return score_win
