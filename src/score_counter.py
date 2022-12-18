from typing import Final, Dict


class ScoreCounter:
    __rows_cleared_to_score: Final[Dict[int, int]] = {
        1: 40,
        2: 100,
        3: 300,
        4: 1200
    }

    def __init__(self):
        self.__total_score: int = 0

    def get_total_score(self) -> int:
        return self.__total_score

    def update_score(self, rows_cleared: int) -> None:
        if rows_cleared not in self.__rows_cleared_to_score:
            valid_values = ", ".join([rows.__str__() for rows in self.__rows_cleared_to_score.keys()])
            raise ValueError(f"Unrecognised rows cleared {rows_cleared}. Valid values: {valid_values}.")

        self.__total_score += self.__rows_cleared_to_score[rows_cleared]
