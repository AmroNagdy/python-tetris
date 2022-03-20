from typing import List, Final

from src.grid_offset import GridOffset


class Board:

    def __init__(self, height: int, width: int):
        self.__height: Final[int] = height
        self.__width: Final[int] = width
        self.height: Final[int] = height - 1
        self.width: Final[int] = width - 1
        self.array: List[List[int]] = Board.build_2d_array(height, width)

    @staticmethod
    def build_2d_array(height: int, width: int) -> List[List[int]]:
        return [[0] * width for _ in range(height)]

    def set(self, grid_offsets: List[GridOffset]) -> None:
        self.__update_array(grid_offsets, 1)

    def unset(self, grid_offsets: List[GridOffset]) -> None:
        self.__update_array(grid_offsets, 0)

    def __update_array(self, grid_offsets: List[GridOffset], array_value: int):
        for grid_offset in grid_offsets:
            self.array[grid_offset.y][grid_offset.x] = array_value

    def should_set_tetromino(self, grid_offsets: List[GridOffset]):
        return self.__is_at_bottom(grid_offsets) or self.__is_piece_below(grid_offsets)

    def __is_at_bottom(self, grid_offsets: List[GridOffset]):
        for grid_offset in grid_offsets:
            if grid_offset.y + 1 > self.height:
                return True

        return False

    def __is_piece_below(self, grid_offsets: List[GridOffset]):
        for grid_offset in grid_offsets:
            if self.array[grid_offset.y + 1][grid_offset.x] == 1:
                return True

        return False

    def collides(self, grid_offsets: List[GridOffset]) -> bool:
        for grid_offset in grid_offsets:
            if self.array[grid_offset.y][grid_offset.x] == 1:
                return True

        return False

    def clear_full_rows(self) -> int:
        self.array = [row for row in self.array if not all(e == 1 for e in row)]
        rows_cleared = self.__height - len(self.array)

        if rows_cleared > 0:
            self.array = self.build_2d_array(rows_cleared, self.__width) + self.array

        return rows_cleared
