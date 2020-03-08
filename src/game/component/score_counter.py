class ScoreCounter():

    def __init__(self, curses_utils):
        self.curses_utils = curses_utils

        self.total_score = 0
        self.rows_cleared_score_map = {
            1: 40,
            2: 100,
            3: 300,
            4: 1200
        }

    def update_score(self, rows_cleared):
        self.total_score += self.rows_cleared_score_map[rows_cleared]
        self.curses_utils.write_score(self.total_score)
