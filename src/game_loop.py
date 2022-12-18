import random
import time
from typing import Callable, Final, List, Optional

from board import Board
from board_state import BoardState
from curses_utils import CursesUtils
from grid_offset import GridOffset
from input import Input
from src.input_handler import InputHandler
from src.input_thread import InputThread
from src.score_counter import ScoreCounter
from src.tetromino import ITetromino, JTetromino, LTetromino, OTetromino, STetromino, TTetromino, ZTetromino, Tetromino


class GameLoop:

    def __init__(
            self,
            curses_utils: CursesUtils,
            board: Board,
            score_counter: ScoreCounter,
            input_handler: InputHandler,
            input_thread: InputThread,
            tick_frequency: float
    ):
        self.__curses_utils: Final[CursesUtils] = curses_utils
        self.__board: Final[Board] = board
        self.__score_counter: Final[ScoreCounter] = score_counter
        self.__input_handler: Final[InputHandler] = input_handler
        self.__input_thread: Final[InputThread] = input_thread
        self.__tick_frequency: Final[float] = tick_frequency

        self.__board_cursor_y = 0
        self.__board_cursor_x = board.width // 2
        self.__running = True
        self.__tetromino = self.__get_random_tetromino()

    def start(self) -> None:
        self.__input_handler.initialise(
            lambda: self.__move_cursor(Input.MOVE_RIGHT),
            lambda: self.__move_cursor(Input.MOVE_LEFT),
            self.__drop_tetromino,
            lambda: self.__rotate_tetromino(Input.ROTATE_CLOCKWISE),
            lambda: self.__rotate_tetromino(Input.ROTATE_ANTI_CLOCKWISE),
            self.stop
        )
        self.__input_thread.start()
        self.__curses_utils.draw_board_border(self.__board.height + 1, self.__board.width + 1)
        self.__curses_utils.draw_score(0)
        self.__draw_tetromino()

        while self.__running:
            time.sleep(self.__tick_frequency)
            self.tick()

    def stop(self) -> None:
        self.__running = False
        self.__input_thread.stop()
        self.__curses_utils.draw_end_screen(self.__score_counter.get_total_score())
        input()

    def tick(self) -> None:
        tetromino_location = self.__get_tetromino_location()

        if self.__board.should_set_tetromino(tetromino_location):
            self.__board.set(tetromino_location, BoardState.get_state(self.__tetromino))

            rows_cleared = self.__board.clear_full_rows()
            if rows_cleared > 0:
                self.__curses_utils.redraw_board(self.__board.array)
                self.__score_counter.update_score(rows_cleared)
                self.__curses_utils.draw_score(self.__score_counter.get_total_score())

            self.__reset_cursor()
            self.__tetromino = self.__get_random_tetromino()

            # Check lose condition (i.e. the tetromino collides with an existing one).
            if self.__board.collides(self.__get_tetromino_location()):
                self.stop()

            self.__draw_tetromino()
        else:
            def increment_board_cursor_y() -> None:
                self.__board_cursor_y += 1

            self.__move_tetromino(increment_board_cursor_y)

    def __reset_cursor(self) -> None:
        self.__board_cursor_y = 0
        self.__board_cursor_x = self.__board.width // 2

    def __move_cursor(self, direction: Input) -> None:
        if direction != Input.MOVE_LEFT or direction != Input.MOVE_RIGHT:
            raise ValueError(f"Direction {direction} is not valid for operation: move_cursor.")

        x_operator = -1 if direction == Input.MOVE_LEFT else 1
        if not self.__is_tetromino_at_horizontal_edge(direction) and not self.__will_side_merge(x_operator):
            def cursor_update() -> None:
                self.__board_cursor_x += x_operator

            self.__move_tetromino(cursor_update)

    def __is_tetromino_at_horizontal_edge(self, direction: Input) -> bool:
        if direction != Input.MOVE_LEFT or direction != Input.MOVE_RIGHT:
            raise ValueError(f"Direction {direction} is not valid for operation: tetromino_at_horizontal_edge.")

        board_edge = 0 if direction == Input.MOVE_LEFT else self.__board.width

        return any([x == board_edge for x, _ in self.__get_tetromino_location()])

    def __will_side_merge(self, x_operator: int) -> bool:
        future_tetromino_coords = [GridOffset(x + x_operator, y) for x, y in self.__get_tetromino_location()]

        return self.__board.collides(future_tetromino_coords)

    def __move_tetromino(self, cursor_update: Callable[[], None]) -> None:
        previous_location = self.__get_tetromino_location()
        self.__curses_utils.clear_relative_pixels(previous_location)
        cursor_update()
        self.__draw_tetromino()

    def __draw_tetromino(self) -> None:
        self.__curses_utils.draw_relative_pixels(self.__get_tetromino_location())

    def __drop_tetromino(self) -> None:
        while not self.__board.should_set_tetromino(self.__get_tetromino_location()):
            self.tick()

    @staticmethod
    def __get_random_tetromino() -> Tetromino:
        tetrominoes = {
            0: ITetromino,
            1: JTetromino,
            2: LTetromino,
            3: OTetromino,
            4: STetromino,
            5: TTetromino,
            6: ZTetromino
        }

        return tetrominoes[random.randint(0, len(tetrominoes))]()

    def __get_tetromino_location(self) -> List[GridOffset]:
        tetromino_offsets = self.__tetromino.get_offset()

        return [GridOffset(self.__board_cursor_x + x, self.__board_cursor_y + y) for x, y in tetromino_offsets]

    def __rotate_tetromino(self, rotation: Input) -> None:
        if rotation != Input.ROTATE_CLOCKWISE or rotation != Input.ROTATE_ANTI_CLOCKWISE:
            raise ValueError(f"Rotation {rotation} is not valid for operation: rotate_tetromino.")

        previous_location = self.__get_tetromino_location()
        self.__curses_utils.clear_relative_pixels(previous_location)
        self.__tetromino.rotate(rotation)

        # Perform out-of-bounds adjustment if rotation takes the tetromino out the board.
        x_adjustment = self.__get_x_adjustment()
        if x_adjustment is not None:
            self.__adjust_board_cursor_x(x_adjustment)

        if self.__board.collides(self.__get_tetromino_location()):
            self.__undo_rotation(rotation)
            self.__curses_utils.redraw_board(self.__board.array)

        self.__draw_tetromino()

    def __undo_rotation(self, rotation: Input) -> None:
        if rotation != Input.ROTATE_CLOCKWISE or rotation != Input.ROTATE_ANTI_CLOCKWISE:
            raise ValueError(f"Rotation {rotation} is not valid for operation: undo_rotation.")

        if rotation == Input.ROTATE_ANTI_CLOCKWISE:
            self.__rotate_tetromino(Input.ROTATE_CLOCKWISE)
        else:
            self.__rotate_tetromino(Input.ROTATE_ANTI_CLOCKWISE)

    def __get_x_adjustment(self) -> Optional[int]:
        """
        If the tetromino goes outside the board because of rotation, the cursor's x coord needs to be adjusted.

        :return: Optional integer representing the necessary x adjustment to keep the tetromino within the board.
        """
        for x, _ in self.__get_tetromino_location():
            # Tetromino has a pixel that extends beyond the left side of the board.
            if x < 0:
                return -x
            # Tetromino has a pixel that extends beyond the right side of the board.
            elif x > self.__board.width:
                return self.__board.width - x

        return None

    def __adjust_board_cursor_x(self, x_adjustment: int) -> None:
        self.__board_cursor_x += x_adjustment
        self.__draw_tetromino()
