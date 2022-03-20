import unittest.mock
from typing import Callable

import pytest

from src.curses_utils import CursesUtils
from src.input_enum import InputEnum
from src.input_handler import InputHandler


@pytest.mark.parametrize(
    "input_enum",
    [
        InputEnum.MOVE_RIGHT,
        InputEnum.MOVE_LEFT,
        InputEnum.DROP,
        InputEnum.ROTATE_CLOCKWISE,
        InputEnum.ROTATE_ANTI_CLOCKWISE,
        InputEnum.QUIT
    ]
)
def test_handle_given_known_input_enum_invokes_expected_callable(
        input_enum: InputEnum
) -> None:
    # Arrange.
    curses_utils = unittest.mock.create_autospec(CursesUtils)
    move_right = unittest.mock.create_autospec(Callable[[], None])
    move_left = unittest.mock.create_autospec(Callable[[], None])
    drop = unittest.mock.create_autospec(Callable[[], None])
    rotate_clockwise = unittest.mock.create_autospec(Callable[[], None])
    rotate_anti_clockwise = unittest.mock.create_autospec(Callable[[], None])
    quit = unittest.mock.create_autospec(Callable[[], None])
    input_handler = InputHandler(
        curses_utils,
        move_right,
        move_left,
        drop,
        rotate_clockwise,
        rotate_anti_clockwise,
        quit
    )

    # Act.
    input_handler.handle(input_enum)

    # Assert.
    input_enum_to_expected_called_callable = {
        InputEnum.MOVE_RIGHT: move_right,
        InputEnum.MOVE_LEFT: move_left,
        InputEnum.DROP: drop,
        InputEnum.ROTATE_CLOCKWISE: rotate_clockwise,
        InputEnum.ROTATE_ANTI_CLOCKWISE: rotate_anti_clockwise,
        InputEnum.QUIT: quit
    }
    input_enum_to_expected_called_callable[input_enum].assert_called_once()

    curses_utils.assert_called_once()


def test_handle_raises_value_error_given_invalid_input_enum():
    # Arrange.
    curses_utils = unittest.mock.create_autospec(CursesUtils)
    mock_callable = unittest.mock.create_autospec(Callable[[], None])
    input_handler = InputHandler(
        curses_utils,
        mock_callable,
        mock_callable,
        mock_callable,
        mock_callable,
        mock_callable,
        mock_callable
    )

    # Act & Assert.
    with pytest.raises(ValueError):
        input_handler.handle(-1)
