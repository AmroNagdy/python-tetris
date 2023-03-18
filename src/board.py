from typing import List, Final

from src.board_state import BoardState
from src.grid_offset import GridOffset


class Board:

    def __init__(self, height: int, width: int):
        self.__height: Final[int] = height
        self.__width: Final[int] = width
        self.height: Final[int] = height - 1
        self.width: Final[int] = width - 1
        self.array: List[List[BoardState]] = Board.build_2d_array(height, width)

    @staticmethod
    def build_2d_array(height: int, width: int) -> List[List[BoardState]]:
        return [[BoardState.EMPTY] * width for _ in range(height)]

    def set(self, grid_offsets: List[GridOffset], board_state: BoardState) -> None:
        self.__update_array(grid_offsets, board_state)

    def unset(self, grid_offsets: List[GridOffset]) -> None:
        self.__update_array(grid_offsets, BoardState.EMPTY)

    def __update_array(self, grid_offsets: List[GridOffset], board_state: BoardState):
        for grid_offset in grid_offsets:
            self.array[grid_offset.y][grid_offset.x] = board_state

    def should_set_tetromino(self, grid_offsets: List[GridOffset]):
        return self.__is_at_bottom(grid_offsets) or self.__is_piece_below(grid_offsets)

    def __is_at_bottom(self, grid_offsets: List[GridOffset]):
        return any(grid_offset.y + 1 > self.height for grid_offset in grid_offsets)

    def __is_piece_below(self, grid_offsets: List[GridOffset]):
        return any(self.array[grid_offset.y + 1][grid_offset.x] != BoardState.EMPTY for grid_offset in grid_offsets)

    def collides(self, grid_offsets: List[GridOffset]) -> bool:
        return any(self.array[grid_offset.y][grid_offset.x] != BoardState.EMPTY for grid_offset in grid_offsets)

    def clear_full_rows(self) -> int:
        self.array = [row for row in self.array if not all(e != BoardState.EMPTY for e in row)]
        rows_cleared = self.__height - len(self.array)

        if rows_cleared > 0:
            self.array = self.build_2d_array(rows_cleared, self.__width) + self.array

        return rows_cleared
